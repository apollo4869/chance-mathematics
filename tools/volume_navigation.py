"""Volume-level reading views. Chapter manuscripts remain the canonical sources."""
from pathlib import Path
import html, json, os, re, shutil, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
    from bs4 import BeautifulSoup
esc = html.escape

def records():
    return json.loads((ROOT/'publication/volumes.json').read_text('utf8'))['volumes']

def label(v, en=False):
    return ('Volume '+v['roman']+' · '+v['en']) if en else ('第'+'一二三四五六七八'[v['number']-1]+'卷 · '+v['zh'])

def url(v, kind='opening', en=False):
    return ('/en' if en else '')+'/volumes/'+f"{v['number']:02d}-{kind}.html"

def chapter_volume(key):
    m=re.fullmatch(r'chapter-(\d+)',key)
    return next((v for v in records() if v['range'][0]<=int(m[1])<=v['range'][1]),None) if m else None

def sidebar(current, chapters, entry, en=False):
    result=''
    for v in records():
        keys=[k for k in chapters if v['range'][0]<=int(k.split('-')[1])<=v['range'][1]]
        active=current in keys or current.startswith(v['id']+'-')
        title=label(v,en);a,b=v['range']
        range_text=(f'Chapters {a}–{b}' if en else f'第{a}–{b}章')
        result+='<details class="volume-nav-group" id="nav-'+v['id']+'"'+(' open' if active else '')+'><summary>'+esc(title)+'<small>'+range_text+'</small></summary><nav>'
        if v.get('opening'):
            result+='<a class="volume-entry" href="'+url(v,en=en)+'"'+(' aria-current="page"' if current==v['id']+'-opening' else '')+'>'+('Volume opening' if en else '卷首')+'</a>'
            result+=''.join(entry(k,True) for k in keys)
            if v.get('ending'):result+='<a class="volume-entry" href="'+url(v,'ending',en)+'"'+(' aria-current="page"' if current==v['id']+'-ending' else '')+'>'+('Volume ending' if en else '卷末')+'</a>'
        else:
            result+='<p class="volume-planned">'+('Planned · Text not yet written' if en else '规划卷 · 正文尚未写成')+'</p>'
        result+='</nav></details>'
    return result

def catalogue(flat, en=False):
    soup=BeautifulSoup(flat,'html.parser');root=soup.select_one('.catalogue')
    if not root:return flat
    cards=list(root.select(':scope > .catalogue-item'))
    for v in records():
        block=soup.new_tag('section',attrs={'class':'volume-catalogue'+(' planned' if not v.get('opening') else ''),'id':v['id']})
        a,b=v['range'];title=esc(label(v,en));heading='<a href="'+url(v,en=en)+'">'+title+'</a>' if v.get('opening') else title
        meta=(f'Chapters {a}–{b}' if en else f'第{a}–{b}章')
        if not v.get('opening'):meta+=' · '+('Planned · Text not yet written' if en else '规划卷 · 正文尚未写成')
        block.append(BeautifulSoup('<header><h3>'+heading+'</h3><p>'+meta+'</p></header>','html.parser'))
        for i in range(a,b+1):
            if i<=len(cards):block.append(cards[i-1].extract())
        root.append(block)
    return str(soup)

def boundary_links(sections, pages, en=False):
    """Change only navigation outside the mathematical reading units."""
    for v in [x for x in records() if x.get('opening')]:
        first,last=v['range']
        for number,kind in [(first,'opening'),(last,'ending')]:
            if 'chapter-'+str(number) not in sections:continue
            k='chapter-'+str(number);s=BeautifulSoup(sections[k],'html.parser')
            nav=s.select_one('.chapter-links')
            if not nav:continue
            anchors=nav.find_all('a')
            if kind=='opening':
                anchor=anchors[0] if anchors else s.new_tag('a')
                if not anchors:nav.insert(0,anchor)
                anchor['href']=url(v,en=en);anchor.string=('← Volume opening' if en else '← 本卷卷首')
            else:
                anchor=anchors[-1] if anchors else s.new_tag('a')
                if not anchors:nav.append(anchor)
                if not v.get('ending'):
                    anchor['href']=('/en' if en else '')+'/index.html#'+v['id']
                    anchor.string='Chapter complete · Contents →' if en else '本章结束 · 全书目录 →'
                    sections[k]=str(s)
                    continue
                anchor['href']=url(v,'ending',en);anchor.string=('Complete this volume →' if en else '本卷结束 · 卷末 →')
                # The old in-text continuation is a navigation link, not prose:
                # retain its wording, but take the reader through the volume boundary.
                if number==4:
                    for a in s.select('a[href="#chapter-5"]'):
                        if not a.find_parent(class_='chapter-links') and a.get_text(strip=True) in {'继续阅读第五章','Continue to Chapter 5'}:
                            a['href']=url(v,'ending',en)
            sections[k]=str(s)
        if 'chapter-'+str(last) not in sections:
            available=[k for k in sections if k.startswith('chapter-') and first<=int(k.split('-')[1])<=last]
            if available:
                key=max(available,key=lambda k:int(k.split('-')[1]));s=BeautifulSoup(sections[key],'html.parser');a=s.select('.chapter-links a')[-1]
                a['href']=('/en' if en else '')+'/index.html#'+v['id'];a.string='Chapter complete · Contents →' if en else '本章结束 · 全书目录 →';sections[key]=str(s)

def breadcrumb(key, pages, en=False):
    v=chapter_volume(key) or next((x for x in records() if key.startswith(x['id']+'-')),None)
    if not v:return ''
    home='/en/index.html' if en else '/index.html'
    return '<nav class="volume-crumb" aria-label="'+('Reading hierarchy' if en else '阅读层次')+'"><a href="'+home+'">'+('Book' if en else '全书')+'</a><span>›</span><a href="'+url(v,en=en)+'">'+esc(label(v,en))+'</a><span>›</span><span>'+esc(('Chapter '+key.split('-')[1]) if key.startswith('chapter-') and en else ('第'+key.split('-')[1]+'章') if key.startswith('chapter-') else ('Volume ending' if key.endswith('ending') and en else '卷末' if key.endswith('ending') else 'Volume opening' if en else '卷首'))+'</span></nav>'

def closing_fragment(section, en=False):
    """Extract one shared rendered epilogue, including its original stable anchors."""
    s=BeautifulSoup(section,'html.parser');v=records()[1]
    h=next(n for n in s.find_all(['h1','h2']) if n.get_text(' ',strip=True)==v['ending']['heading_en' if en else 'heading_zh'])
    nodes=[h]
    for n in h.next_siblings:
        if getattr(n,'name',None) in {'h1','h2'}:break
        if getattr(n,'get',None) and 'chapter-links' in n.get('class',[]):break
        nodes.append(n)
    return ''.join(str(n) for n in nodes),h['id']

def reader_closing_view(body,en=False):
    """Keep the canonical fragment verifiable, but show it only on the volume page.

    The non-rendering fragment retains old anchors and search integrity. It never
    becomes visible in chapter mode or print. No second Markdown source is made.
    """
    s=BeautifulSoup(body,'html.parser')
    fragment,anchor=closing_fragment(body,en)
    h=s.find(id=anchor);nodes=[h]
    for n in h.next_siblings:
        if getattr(n,'name',None) in {'h1','h2'}:break
        nodes.append(n)
    wrapper=s.new_tag('div',attrs={'class':'volume-epilogue-canonical','style':'display:none!important','aria-hidden':'true'})
    h.insert_before(wrapper)
    for n in nodes:wrapper.append(n.extract())
    nav=s.new_tag('nav',attrs={'class':'volume-ending-forward','aria-label':'Volume ending' if en else '本卷结语'})
    a=s.new_tag('a',href=url(records()[1],'ending',en))
    a.string='Read the Volume II epilogue →' if en else '阅读第二卷结语 →'
    nav.append(a);wrapper.insert_after(nav)
    return str(s)

def restore_reader_fragment(s):
    """For independent preservation checks only, restore the canonical chapter DOM."""
    try:from .continuation_headers import restore
    except ImportError:from continuation_headers import restore
    restore(s)
    for n in list(s.select('.volume-ending-forward')):n.decompose()
    for n in list(s.select('.volume-epilogue-canonical')):n.unwrap()
    return s

def render_md(path):
    node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
    env=dict(os.environ)
    if not (ROOT/'node_modules/markdown-it').exists():
        fallback=ROOT.parent/'chance-mathematics-restored-v2/node_modules'
        if fallback.exists():env['NODE_PATH']=str(fallback)
    return subprocess.check_output([node,'-e',"let s='';process.stdin.setEncoding('utf8');process.stdin.on('data',x=>s+=x);process.stdin.on('end',()=>process.stdout.write(require('markdown-it')().render(s)));"],input=(ROOT/path).read_bytes(),cwd=ROOT,env=env).decode('utf8')

def page_bodies(sections, pages, en=False):
    lang='en' if en else 'zh';out={}
    for v in [x for x in records() if x.get('opening')]:
        a,b=v['range'];range_text=(f'Chapters {a}–{b}' if en else f'第{a}–{b}章')
        actual=[n for n in range(a,b+1) if 'chapter-'+str(n) in pages]
        if not actual:range_text+=(' · Chapter text not yet written' if en else ' · 章节正文尚未写成')
        elif len(actual)<b-a+1:range_text+=(' · Available: Chapter '+str(actual[-1]) if en else ' · 当前正文：第'+str(actual[-1])+'章')
        ordinal=('Volume '+v['roman']) if en else ('第'+'一二三四五六七八'[v['number']-1]+'卷')
        common='<p class="volume-ordinal">'+ordinal+'</p>'
        prose=render_md(v['opening'][lang]) if v['opening'][lang] else ''
        draft='<p class="volume-range">'+('Working introduction · Author review pending' if en else '卷首导言工作稿 · 作者待审')+'</p>' if v.get('opening_status')=='AUTHOR_REVIEW_PENDING' else ''
        body=common+'<h1>'+esc(v[lang])+'</h1><p class="volume-theme">'+esc(v['theme_'+lang])+'</p>'+draft+'<hr class="volume-rule"><div class="volume-prose">'+prose+'</div><p class="volume-range">'+range_text+'</p>'
        if 'chapter-'+str(a) in pages:body+='<nav class="volume-actions"><a href="'+pages['chapter-'+str(a)]+'">'+('Begin Chapter '+str(a)+' →' if en else '进入第'+str(a)+'章 →')+'</a></nav>'
        out[v['id']+'-opening']=('<article class="volume-title-page" id="'+v['id']+'-opening">'+body+'</article>',label(v,en))
        if not v.get('ending'):continue
        if 'chapter' in v['ending']:
            fragment,anchor=closing_fragment(sections['chapter-'+str(b)],en)
            chapter=BeautifulSoup(sections['chapter-'+str(b)],'html.parser')
            previous=next(n['id'] for n in chapter.find_all('h2') if n.get_text(strip=True).startswith('14.23 '))
            body=common+'<div class="volume-ending-text">'+fragment+'</div><p class="volume-origin"><a href="'+pages['chapter-'+str(b)]+'#'+previous+'">'+('← Return to §14.23' if en else '← 返回 §14.23')+'</a></p>'
        else:
            body=common+'<h1>'+v['ending']['title_'+lang]+'</h1><hr class="volume-rule"><div class="volume-prose">'+render_md(v['ending'][lang])+'</div>'
        back=pages['chapter-'+str(b)]+('#'+previous if 'chapter' in v['ending'] else '')
        if v.get('ending_status')=='AUTHOR_REVIEW_PENDING':
            body+='<p class="volume-range">'+('Working epilogue · Author review pending' if en else '卷尾工作稿 · 作者待审')+'</p>'
        body+='<p class="volume-complete">'+('END OF VOLUME '+v['roman'] if en else '本卷结束')+'</p><nav class="volume-actions"><a href="'+back+'">'+('← Return to Chapter '+str(b) if en else '← 返回第'+str(b)+'章')+'</a>'
        if v['number']==1:body+='<a href="'+url(records()[1],en=en)+'">'+('Enter Volume II →' if en else '进入第二卷 →')+'</a>'
        elif v['number']==2 and records()[2].get('opening'):body+='<a href="'+url(records()[2],en=en)+'">'+('Enter Volume III →' if en else '进入第三卷 →')+'</a>'
        elif v['number']<len(records()):
            next_v=records()[v['number']]
            if next_v.get('opening'):body+='<a href="'+url(next_v,en=en)+'">'+('Enter Volume '+next_v['roman']+' →' if en else '进入第'+'一二三四五六七八'[next_v['number']-1]+'卷 →')+'</a>'
            else:body+='<span class="volume-planned">'+(label(next_v,en)+' · '+('Text not yet written' if en else '正文尚未写成'))+'</span>'
        else:body+='<span class="volume-planned">'+('End of the book' if en else '全书结束')+'</span>'
        body+='</nav>'
        out[v['id']+'-ending']=('<article class="volume-title-page" id="'+v['id']+'-ending">'+body+'</article>',('Epilogue to Volume '+v['roman']) if en else ('第'+'一二三四五六七八'[v['number']-1]+'卷尾声'))
    return out

def print_page(page, source, target):
    """Script-free print HTML, from the exact same volume article as the web view."""
    from urllib.parse import urlsplit
    import posixpath
    s=BeautifulSoup(page,'html.parser');body=s.select_one('.volume-title-page');head=s.head
    for n in list(head.find_all('script')):n.decompose()
    for n in [*head.select('[href],[src]'),*body.select('[href],[src]')]:
        attr='href' if n.has_attr('href') else 'src';u=urlsplit(n[attr])
        if u.scheme or u.netloc or not u.path:continue
        dest=(source.parent/u.path).resolve()
        n[attr]=posixpath.relpath(dest.as_posix(),target.parent.resolve().as_posix())+('?' +u.query if u.query else '')+('#'+u.fragment if u.fragment else '')
    head.append(BeautifulSoup('<style>@page{size:A4;margin:22mm}body{background:var(--paper);margin:0}main{max-width:170mm;margin:0 auto;padding:12mm}.volume-title-page{break-before:auto}.volume-actions,.volume-origin{display:none}@media print{body,main{background:white;color:#111}main{padding:0}}</style>','html.parser'))
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(('<!doctype html><html lang="'+s.html['lang']+'">'+str(head)+'<body><main>'+str(body)+'</main></body></html>').encode())
