"""Local-only reading candidate assembled from the retained public edition.

Never writes the public baseline, manuscripts, adopted figures, hosting or Git
remotes. Only explicit public static trees and approved illustration registries
are copied. Original page mathematics is checked by exact byte recovery.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,shutil,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.chapter_reading_layout import relocate_existing

R=Path(__file__).resolve().parents[1]
O=R/'reports/full-book-reading-2026-11-07'
OUT=R/'work/reading-acceptance/site'
PUBLIC=R.parent/'sites/chance-mathematics-illustrations-cloud-2026-11-05/public'
ALLOWED_DIRS={'assets','chapters','en','volumes','print','advanced','proofs','metadata','releases','downloads'}
ALLOWED_SUFFIX={'.html','.css','.js','.json','.svg','.png','.jpg','.jpeg','.img','.webp','.gif','.woff','.woff2','.ttf','.otf','.ico','.txt','.md','.zip','.pdf','.bib'}

def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,b):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b.encode('utf8') if isinstance(b,str) else b)
def save(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def load(name):return json.loads((R/'publication'/name).read_text('utf8'))['figures']
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def book_fragment(s):
 opening=re.search(r'<section\b[^>]*class="book-section"[^>]*>',s);assert opening
 depth=0
 for tag in re.finditer(r'<(/?)section\b[^>]*>',s[opening.start():]):
  depth+=-1 if tag[1] else 1
  if depth==0:return s[opening.start():opening.start()+tag.end()]
 raise AssertionError('Unclosed book section')

def main():
 assert PUBLIC.is_dir() and OUT!=PUBLIC and not OUT.is_relative_to(PUBLIC)
 O.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
 baseline=[]
 for p in sorted(PUBLIC.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(PUBLIC);parts=rel.parts
  if any(x.startswith(('.', '__')) or x in {'local-preview','reports','source','node_modules'} for x in parts):continue
  if len(parts)>1 and parts[0] not in ALLOWED_DIRS:continue
  if p.suffix.lower() not in ALLOWED_SUFFIX and rel.as_posix()!='_headers':continue
  if p.name=='complete-offline.zip':continue
  raw=p.read_bytes();write(OUT/rel,raw);baseline.append(dict(path=rel.as_posix(),sha256=sha(raw),bytes=len(raw)))
 # Existing groups are authoritative; never rerun any visual generator.
 pub=module('accepted_publisher',R/'tools/publish-explanatory-overlays.py')
 old=pub.selected(R);new=load('explanatory-volume7-batch1-working.json')+load('explanatory-volume8-batch1-working.json')
 rows=old+new;assert len(rows)==90 and len({(x['id'],x['lang']) for x in rows})==90
 for ns in ['explanatory-volume7-v1','explanatory-volume8-v1']:
  for p in sorted((R/'assets/visuals'/ns).iterdir()):
   if p.is_file() and p.suffix in {'.svg','.css','.js','.json'}:write(OUT/'assets/visuals'/ns/p.name,p.read_bytes())
 css=(R/'publication/chapter-reading-layout.css').read_bytes();css_url='/assets/chapter-reading-layout-'+sha(css)[:12]+'.css';write(OUT/css_url.lstrip('/'),css)
 include='<link rel="stylesheet" href="'+css_url+'">'
 # Derive new runtime assets from the retained bilingual variants. Only the
 # reviewed capture-loop repair changes; existing language strings stay intact.
 original_loop='else { if (!node) node = n; break; }'
 source=(R/'reader-mode.js').read_text('utf8')
 begin=source.index('      else {\n        // In the leading gap')
 end=source.index('\n    }\n    return node ?',begin)
 repaired_loop=source[begin:end].strip()
 runtime_map={}
 for p in (PUBLIC/'assets').glob('reading-mode-*.js'):
  text=p.read_text('utf8');assert text.count(original_loop)==1
  text=text.replace(original_loop,repaired_loop,1);name='reading-mode-'+sha(text.encode())[:12]+'.js'
  write(OUT/'assets'/name,text);runtime_map[p.name]=name
 for p in OUT.rglob('*.html'):
  s=p.read_text('utf8');newtext=s
  for oldname,newname in runtime_map.items():newtext=newtext.replace(oldname,newname)
  if newtext!=s:write(p,newtext)
 recovery=[];layout=[];prints=[]
 for lg,folder in [('zh','chapters'),('en','en/chapters')]:
  files=sorted((OUT/folder).glob('*.html'));assert len(files)==58
  for p in files:
   original=p.read_text('utf8');page,change=relocate_existing(original,lg=='en');assert change
   page=page.replace('</head>',include+'</head>',1)
   assert book_fragment(page)==book_fragment(original)
   assert page.replace(include,'',1).replace(change['notes'],'',1).replace(change['badge'],'',1)==change['without_old_bar']
   slug=p.stem;rr=[r for r in new if r['lang']==lg and r['slug']==slug];fragments=[];nss=set()
   for row in rr:
    assert f'id="visual-{row["id"]}"' not in page
    frag=row['html'];page=pub.insert(page,row,frag);fragments.append(frag)
    nss.update(re.findall(r'/assets/visuals/([^/]+)/',frag))
    ns='explanatory-volume7-v1' if row['id'] in {'V48','V49','V51','V52','V53'} else 'explanatory-volume8-v1'
    static=R/'assets/visuals'/ns/'local-preview/print/figures'/f'{row["id"]}.{lg}.html'
    assert static.is_file()
    static_text=static.read_text('utf8')
    # Prototype-only /review links must not leak into a complete reading build.
    other='en' if lg=='zh' else 'zh'
    nav=f'<nav><a href="/{"en/" if lg=="en" else ""}chapters/{slug}.html#visual-{row["id"]}">'+('Back to chapter' if lg=='en' else '返回正文')+f'</a><a href="/print/figures/{row["id"]}.{other}.html">'+('中文' if lg=='en' else 'English')+f'</a><a href="/assets/visuals/{ns}/{row["id"]}.{lg}.svg">SVG</a></nav>'
    static_text,n=re.subn(r'<nav>.*?</nav>',lambda m:nav,static_text,count=1,flags=re.S);assert n==1
    write(OUT/'print/figures'/static.name,static_text)
   inc=''.join(f'<link rel="stylesheet" href="/assets/visuals/{ns}/figures.css"><script defer src="/assets/visuals/{ns}/interactions.js"></script>' for ns in sorted(nss))
   if inc:page=page.replace('</head>',inc+'</head>',1)
   restored=page.replace(inc,'',1) if inc else page
   for frag in fragments:restored=restored.replace(frag,'',1)
   assert book_fragment(restored)==book_fragment(original),p
   expected=[r['id'] for r in rows if r['lang']==lg and r['slug']==slug]
   found=re.findall(r'<figure\b[^>]*\bid="visual-([^"]+)"',page)
   # Legacy explanatory/engineering figures outside the new registry stay intact.
   assert set(found)&{r['id'] for r in rows}==set(expected),(p,found,expected)
   assert len(found)==len(set(found)),p
   assert '<details class="chapter-edition"><summary>' in page and 'class="chapter-edition" open' not in page
   assert page.index('data-chapter-publication="footer"')>page.index(book_fragment(page))+len(book_fragment(page))
   write(p,page)
   recovery.append(dict(path=p.relative_to(OUT).as_posix(),original_sha256=sha(original.encode()),candidate_sha256=sha(page.encode()),original_math_book_sha256=sha(book_fragment(original).encode()),original_book_restored_exactly=True,adopted_figures=found,new_groups=[x['id'] for x in rr]))
   layout.append(dict(path=p.relative_to(OUT).as_posix(),metadata_default_closed=True,metadata_at_footer=True,metadata_preserved=True))
   # Existing static chapter pages retain their mathematics and gain the same new figures.
   pp=OUT/'print'/f'{slug}.{lg}.html'
   if not pp.exists():continue
   before=pp.read_text('utf8');pr=before;static_fragments=[]
   for row in rr:
    m=re.search(r'<div class="v[78]-print">(.*?)</div>',row['html'],re.S);assert m
    f='<figure class="reading-static-insert" id="visual-'+row['id']+'">'+m[1]+'</figure>'
    pr=pub.insert(pr,row,f);static_fragments.append(f)
   restored=pr
   for f in static_fragments:restored=restored.replace(f,'',1)
   assert restored==before
   style=include+'<style>@media print{.reading-static-insert section{break-after:page;break-inside:avoid}.reading-static-insert section:last-child{break-after:auto}.reading-static-insert img{width:100%;height:auto;max-height:205mm;object-fit:contain}.reading-static-insert p{font-size:8pt}}</style>'
   pr=pr.replace('</head>',style+'</head>',1)
   # Printing starts with the title and quiet draft state, not repeated author metadata.
   pr=re.sub(r'(<header class="print-meta">)Haobai Wang · ([^<]+)(<br\s*/?>)',lambda m:m[1]+m[2]+' · '+('Working draft' if lg=='en' else '工作稿')+m[3],pr,count=1)
   notes=change['notes'];pr=pr.replace('</main>',notes+'</main>',1)
   write(pp,pr);prints.append(dict(path=pp.relative_to(OUT).as_posix(),original_sha256=sha(before.encode()),original_book_restored_exactly=True,new_groups=[x['id'] for x in rr]))
 save(O/'baseline-public-files.json',dict(source=str(PUBLIC),files=baseline))
 save(O/'integration.json',dict(chapter_pages=116,groups=45,bilingual_figures=90,new_groups=10,chapters=recovery,layout=layout,chapter_print_pages=prints,published=False,pushed=False,manuscripts_modified=False))
 save(O/'accepted-figures.json',dict(source_commit='771fb0ee',figures=rows,final_author_aesthetics='open',independent_expert_mathematics='open',unpublished_research_used=False))
 save(O/'runtime-repair.json',dict(reason='Confirmed chapter 7 mobile section rollback in a leading gap',assets=runtime_map,math_changed=False,illustration_code_changed=False))
 save(OUT/'metadata/reading-candidate.json',dict(version='reading-acceptance-20261107',chapters=58,languages=['zh','en'],illustration_groups=45,status='author reading working draft; independent mathematical final review incomplete',published=False))
 print(json.dumps(dict(local_site=str(OUT),chapter_pages=116,adopted_groups=45,bilingual_figures=90,newly_integrated_groups=10,static_chapter_pages=len(prints),original_math_exact_recovery=True),ensure_ascii=False))

if __name__=='__main__':main()
