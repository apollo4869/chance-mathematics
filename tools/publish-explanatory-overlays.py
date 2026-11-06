"""Publish selected existing illustration drafts without changing manuscript bodies.

Only explicitly selected registry rows and root-level SVG/CSS/JS/JSON assets
are exported. Review pages, screenshots, reports and private Git history are not.
"""
from pathlib import Path
from html import escape
import argparse, hashlib, json, re, shutil

def digest(b): return hashlib.sha256(b).hexdigest()
def write(p, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data.encode('utf-8') if isinstance(data, str) else data)

def selected(source):
    if (source/'publication/illustration-release.json').exists():
        return json.loads((source/'publication/illustration-release.json').read_text('utf-8'))['figures']
    selections = [('explanatory-adopted-volumes1-5.json', None),
                  ('explanatory-figures-batch2-working.json', {'P02','P03','P04','P05','V35','V36','V38','V40'}),
                  ('explanatory-volume6-batch2-working.json', None)]
    rows = []
    for name, ids in selections:
        for row in json.loads((source/'publication'/name).read_text('utf-8'))['figures']:
            if ids is not None and row['id'] not in ids: continue
            rows.append({k:row[k] for k in ['id','lang','slug','section','title','html','condition','status'] if k in row})
    assert len(rows)==70 and len({(r['id'],r['lang']) for r in rows})==70
    return rows

def insert(page, row, fragment):
    heading = re.search(r'<h[23]\b[^>]*>\s*'+re.escape(row['section'])+r'\s[^<]+</h[23]>', page)
    assert heading, (row['id'],row['lang'],row['section'])
    if '<div class="reading-unit"' in page:
        start=page.rfind('<div class="reading-unit"',0,heading.start())
        end=page.find('<div class="reading-unit"',heading.end())
        if end<0: end=page.find('</article>',heading.end())
        assert start>=0 and end>start
        at=page.rfind('</div>',start,end)
    else:
        following=re.search(r'<h2\b',page[heading.end():])
        at=heading.end()+following.start() if following else page.find('</main>',heading.end())
        if at<0: at=page.find('</article>',heading.end())
    assert at>heading.end()
    return page[:at]+fragment+page[at:]

def main():
    a=argparse.ArgumentParser();a.add_argument('--source',type=Path,required=True);a.add_argument('--site',type=Path);a.add_argument('--output-dir',type=Path)
    args=a.parse_args();source=args.source.resolve();site=args.site.resolve() if args.site else source;pub=args.output_dir.resolve() if args.output_dir else site/'public'
    rows=selected(source);groups={};nss=set();files={};audits=[]
    for r in rows:
        groups.setdefault((r['slug'],r['lang']),[]).append(r)
        nss.update(re.findall(r'/assets/visuals/([^/]+)/',r['html']))
    # v2 contains adopted P01/P02 and V31/V33 controls. v6-v2 adds to v1.
    nss.update({'explanatory-v2','explanatory-volume6-v1','explanatory-volume6-v2'})
    for ns in sorted(nss):
        for p in sorted((source/'assets/visuals'/ns).iterdir()):
            if p.is_file() and p.suffix in {'.svg','.css','.js','.json'}:
                name='assets/visuals/'+ns+'/'+p.name
                write(pub/name,p.read_bytes());files[name]=digest(p.read_bytes())
    print_style='''<style data-illustration-print-style>img.illustration-print-only{display:none!important}@media print{.illustration-screen-only{display:none!important}img.illustration-print-only{display:block!important;width:100%;height:auto;max-height:none!important;break-inside:avoid}figure.illustration-static{break-inside:avoid;margin:2rem 0}figure.illustration-static img{width:100%;height:auto;max-height:none!important}figure.illustration-static figcaption{font-size:12px;line-height:1.6}}</style>'''
    for (slug,lg),rr in groups.items():
        paths=[(pub/('en/' if lg=='en' else '')/'chapters'/(slug+'.html'),False),
               (pub/'print'/(slug+'.'+lg+'.html'),True)]
        for p,is_print in paths:
            if not p.exists():
                assert is_print, p
                continue
            before=p.read_text('utf-8');after=before;frags=[]
            assert '<!-- illustration-release:' not in before, 'Run on the retained pre-release source, not an already modified page'
            needed=set()
            for r in rr:
                code=r['id'];assert f'id="visual-{code}"' not in after, (p,code)
                svgs=re.findall(r'/assets/visuals/[^"<>]+/'+re.escape(code)+r'\.'+lg+r'\.svg',r['html'])
                assert svgs,(code,lg)
                static=svgs[0];title=escape(r['title']);condition=escape(r.get('condition',''))
                static_html=f'<figure class="illustration-static" id="visual-{code}"><img src="{static}" alt="{title}"><figcaption>{condition}</figcaption></figure>'
                if is_print: fragment=static_html
                else:
                    fragment=r['html'].replace(f'href="/print/{code}.{lg}.html"',f'href="/print/figures/{code}.{lg}.html"')
                    fragment='<div class="illustration-screen-only">'+fragment+'</div><img class="illustration-print-only" src="'+static+'" alt="'+title+'">'
                fragment='<!-- illustration-release:'+code+' -->'+fragment+'<!-- /illustration-release:'+code+' -->'
                after=insert(after,r,fragment);frags.append(fragment)
                needed.update(re.findall(r'/assets/visuals/([^/]+)/',r['html']))
                printpage=f'<!doctype html><html lang="{lg}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title}</title><style>body{{max-width:1000px;margin:24px auto;padding:16px;color:#173f39;background:#fffefa;font:16px/1.7 sans-serif}}img{{display:block;width:100%;height:auto}}@page{{size:A4 portrait;margin:12mm}}@media print{{nav{{display:none}}body{{padding:0;margin:0;background:white}}}}</style></head><body><nav><a href="/'+('en/' if lg=='en' else '')+f'chapters/{slug}.html#visual-{code}">'+('返回正文' if lg=='zh' else 'Back to chapter')+'</a></nav>'+static_html+'</body></html>'
                write(pub/'print/figures'/f'{code}.{lg}.html',printpage)
            if 'explanatory-v1' in needed:needed.remove('explanatory-v1');needed.add('explanatory-v2')
            if 'explanatory-volume6-v2' in needed:needed.add('explanatory-volume6-v1')
            if 'explanatory-volume6-v1' in needed:needed.add('explanatory-volume6-v2')
            includes=print_style+('' if is_print else ''.join(f'<link rel="stylesheet" href="/assets/visuals/{ns}/figures.css"><script defer src="/assets/visuals/{ns}/interactions.js"></script>' for ns in sorted(needed)))
            after=after.replace('</head>',includes+'</head>',1)
            restored=after.replace(includes,'',1)
            for f in frags:restored=restored.replace(f,'',1)
            assert restored==before, p
            for r in rr:assert after.count(f'id="visual-{r["id"]}"')==1
            write(p,after)
            audits.append(dict(path=p.relative_to(site).as_posix(),before=digest(before.encode()),after=digest(after.encode()),exact_body_recovery=True,figures=[r['id'] for r in rr]))
    # Assert all first-render asset and print links are real files.
    for (slug,lg),rr in groups.items():
        p=pub/('en/' if lg=='en' else '')/'chapters'/(slug+'.html')
        s=p.read_text('utf-8')
        for v in re.findall(r'(?:src|href)="(/(?:assets/visuals/explanatory[^"#?]+|print/figures/[^"#?]+))"',s):
            assert (pub/v.lstrip('/')).is_file(),v
    payload=dict(edition='illustrations-2026-11-05',groups=35,bilingual_figures=70,chapter_pages=len(groups),source_manuscripts_modified=False,figures=rows)
    write(site/'illustration-release.json',json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    write(site/'illustration-preservation.json',json.dumps(dict(pages=audits,assets=files,private_materials_exported=False),ensure_ascii=False,indent=2)+'\n')
    # The existing public-only editable source receives the same approved assets,
    # not the author workspace or review package.
    if args.site:
        editable=site/'book-source-current'
        for name in files:write(editable/name,(pub/name).read_bytes())
        write(editable/'publication/illustration-release.json',json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(groups=35,bilingual_figures=70,chapter_pages=len(groups),print_pages=sum(x['path'].startswith('public/print/') for x in audits),assets=len(files),all_original_page_bodies_recovered=True)))

if __name__=='__main__': main()
