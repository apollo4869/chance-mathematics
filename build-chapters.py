"""Publish the exact existing book sections as independent HTML documents."""
from pathlib import Path
from html.parser import HTMLParser
import sys,posixpath,shutil
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
import re,json,hashlib,html
from tools.homepage import hero, utility, english_catalogue, english_sidebar
root=Path(__file__).parent
english_book='--english' in sys.argv
suffix='-en' if english_book else ''
ui_labels=json.loads((root/'translations/en/ui-labels.json').read_text('utf-8')) if english_book else {}
ui_labels.update({'缩小正文字号':'Decrease text size','放大正文字号':'Increase text size','公式原码':'TeX source','打印':'Print','阅读目录':'Contents','版本说明':'About this edition','编排与资料':'Notes and resources'})
def english_ui(value):
    return re.sub(r'[\u4e00-\u9fff]+',lambda m:ui_labels.get(m[0],m[0]),value) if english_book else value
dist=root/'dist';dist.mkdir(exist_ok=True);(dist/'chapters').mkdir(exist_ok=True);(dist/'assets').mkdir(exist_ok=True)
source=root/('build/book-source'+suffix+'.html')
if not source.exists():raise SystemExit('Run build.py: Markdown must be rendered first; no frozen-HTML fallback.')
baseline=json.loads((root/'baseline-manuscript.json').read_text(encoding='utf-8'))
approved=baseline['files']
actual={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in approved}
if actual!=approved:raise SystemExit('Protected input changed; author review required.')
if json.loads((root/('build/input-sha256'+suffix+'.json')).read_text(encoding='utf-8'))!=actual:raise SystemExit('Generated HTML is stale; run build.py from Markdown.')
if english_book:
    translated_inputs=json.loads((root/'build/translation-render-inputs.json').read_text('utf-8'))
    assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==digest for p,digest in translated_inputs.items()),'English rendering is stale'
original=english_ui(source.read_bytes().decode('utf-8'))
sections={m[1]:m[0] for m in re.finditer(r'<section id="([^"]+)"[^>]*>[\s\S]*?</section>',original)}
inputs=json.loads((root/'provenance/build-inputs.json').read_text(encoding='utf-8'))
site_links=json.loads((root/'site-links.json').read_text(encoding='utf-8'))
modules=inputs.get('advanced_modules',[])
assert len(sections)==len(inputs['chapters'])+6+len(modules)
slugs=[Path(p).stem for p in inputs['chapters']]
pages={'rules':'/writing-rules.html',**{f'chapter-{i+1}':f'/chapters/{s}.html' for i,s in enumerate(slugs)},'supplement':'/proofs.html','references':'/references.html'}
pages.update({m['id']:'/advanced/'+m['slug']+'.html' for m in modules})
pages['reading-routes']='/reading-routes.html'
if english_book:pages={k:'/en'+v for k,v in pages.items()}
titles={key:html.unescape(re.search(r'data-title="([^"]*)"',sections[key])[1]) for key in pages}
chapter_count_label=(str(len(slugs))+' chapters') if english_book else '前'+re.match(r'第([^章]+)章',titles['chapter-'+str(len(slugs))])[1]+'章'
book_home='/en/index.html' if english_book else '/'
owners={'cover':book_home,'edition':book_home}
for key,block in sections.items():
    for value in re.findall(r'\bid="([^"]+)"',block):owners[value]=pages.get(key,book_home)
def route(anchor):
    page=owners.get(anchor,book_home)
    return page if anchor in pages or anchor in ('cover','edition') else page+'#'+anchor
def links(s):return re.sub(r'href="#([^"]*)"',lambda m:'href="'+route(m[1])+'"',s)
header=links(re.search(r'<header class="topbar">[\s\S]*?</header>',original)[0])
sidebar=re.search(r'<aside id="sidebar">[\s\S]*?</aside>',original)[0]
dialog=re.search(r'<dialog id="search-dialog">[\s\S]*?</dialog>',original)[0]
footer=re.search(r'<footer>[\s\S]*?</footer>',original)[0]
base_css=re.search(r'<style>([\s\S]*?)</style>',original)[1]
extra_css='''
.reading-context{font:12px/1.6 "Microsoft YaHei",sans-serif;color:var(--muted);padding:22px 0 0;display:flex;justify-content:space-between;gap:12px}.reading-context a{text-decoration:none}.book-section{padding-bottom:25px}.home .cover{min-height:auto;padding:45px 0 25px}.home .cover h1{margin-top:28px}.home .cover-lead{margin:25px 0}.home .cover-line{display:none}.home .cover-mark{top:10px}.catalogue{margin:25px 0 60px}.catalogue h2{font-size:26px;font-weight:500}.catalogue-item{display:grid;grid-template-columns:40px 1fr 24px;gap:16px;border-top:1px solid var(--line);padding:20px 2px;text-decoration:none;color:var(--ink)}.catalogue-item:last-of-type{border-bottom:1px solid var(--line)}.chapter-number{font:20px Georgia,serif;color:var(--teal)}.catalogue-title{font-size:19px;font-weight:600;line-height:1.6}.catalogue-description{display:block;font-size:13px;line-height:1.8;color:var(--muted);margin-top:6px}.catalogue-arrow{color:var(--teal)}.extra-pages{display:flex;flex-wrap:wrap;gap:14px;margin-top:22px;font-size:14px}.catalogue-home{display:block;font:14px/1.8 sans-serif;margin-bottom:20px;text-decoration:none}aside summary a[aria-current=page]{color:var(--teal);font-weight:700}.section-search-hint{font-size:12px;color:var(--muted)}.home .edition{margin-top:40px;margin-bottom:50px}.section-kicker{padding-top:25px}.chapter-links{margin-top:45px}.home .start{margin-top:12px}@media(max-width:800px){.home .cover h1{font-size:43px}.home .cover{padding-top:32px}.reading-context{font-size:11px;padding-top:18px}.catalogue-title{font-size:18px}.catalogue-item{grid-template-columns:28px 1fr 16px;gap:11px}.catalogue h2{font-size:24px}}
'''
def asset(name,text):
    digest=hashlib.sha256(text.encode()).hexdigest()[:12]
    file=f'{name}-{digest}.'+('css' if name=='reader' else 'js')
    (dist/'assets'/file).write_bytes(text.encode())
    return '/assets/'+file
css=asset('reader',base_css+'\n'+extra_css+'\n'+(root/'reader-mode.css').read_text(encoding='utf-8')+'\n'+(root/'home.css').read_text(encoding='utf-8'))
shutil.copytree(root/'assets/images',dist/'assets/images',dirs_exist_ok=True)
shutil.copytree(root/'assets/ui',dist/'assets/ui',dirs_exist_ok=True)
home_ui_asset=asset('home-ui',(root/'home-ui.js').read_text(encoding='utf-8'))
scripts=re.findall(r'<script>([\s\S]*?)</script>',original)
assert len(scripts)==3
if english_book:
    # The protected scripts use these punctuation marks only in UI text/comments.
    punctuation=str.maketrans({'，':', ','。':'. ','；':'; ','：':': ','（':' (','）':')','、':', '})
    scripts=[script.translate(punctuation) for script in scripts]
search=[]
for section_id in pages:
    soup=BeautifulSoup(sections[section_id],'html.parser')
    if english_book:
        for heading in soup.find_all(['h1','h2']):
            if heading.get_text(' ',strip=True)=='The Mathematics of Chance':
                heading['class']=heading.get('class',[])+['book-series-title']
                volume=heading.find_next_sibling('p')
                if volume and volume.get_text().startswith('Volume '):volume['class']=volume.get('class',[])+['book-volume']
    if section_id=='chapter-6':
        for heading in soup.find_all(['h1','h2']):
            if (english_book and re.search(r'Next Chapter.*Chapter 7',heading.get_text(),re.I)) or (not english_book and '下一章' in heading.get_text() and '第七章' in heading.get_text()):
                a=soup.new_tag('a',href=pages['chapter-7'])
                for child in list(heading.contents):a.append(child.extract())
                heading.append(a)
    for i,node in enumerate(soup.select('h1,h2,h3,h4,h5,h6,p,li,td,th,.formula'),1):
        if node.find_parent(class_='formula') or node.find_parent(class_='chapter-links'):continue
        if not node.get('id'):node['id']=f'search-{section_id}-{i}'
        clone=BeautifulSoup(str(node),'html.parser')
        for f in clone.select('.formula'):f.replace_with(' '+f.get('data-tex','')+' ')
        text=clone.get_text(' ',strip=True)
        if text:search.append({'id':node['id'],'text':text,'section':section_id})
    sections[section_id]=str(soup)

search_js='const BOOK_SEARCH='+json.dumps(search,ensure_ascii=False).replace('<','\\u003c')+';\nconst BOOK_PAGES='+json.dumps({k:v.lstrip('/') for k,v in pages.items()})+';\nconst BOOK_SECTION_TITLES='+json.dumps(titles,ensure_ascii=False)+';'
search_asset=asset('search',search_js)
experiment_asset=asset('experiments',scripts[1])
app="const BOOK_ROOT=document.body.dataset.bookRoot||'./';\n"+scripts[2]
def replace_once(old,new):
    global app
    assert app.count(old)==1,old
    app=app.replace(old,new)
replace_once('href="#${r.id}"','href="${BOOK_ROOT}${BOOK_PAGES[r.section]}#${r.id}"')
replace_once("document.getElementById(r.section)?.dataset.title||r.section","BOOK_SECTION_TITLES[r.section]||r.section")
old="let lastAnchor=storage.get('anchor');if(lastAnchor&&document.getElementById(lastAnchor)){$('#resume').hidden=false;$('#resume').onclick=()=>{location.hash=lastAnchor}};"
new="let reading=null;try{reading=JSON.parse(storage.get('reading')||'null')}catch{};const resume=$('#resume');if(resume&&reading&&reading.path&&reading.anchor){resume.hidden=false;resume.onclick=()=>{location.href=reading.path+'#'+reading.anchor}};"
replace_once(old,new)
replace_once("storage.set('anchor',cur.id)","storage.set('reading',JSON.stringify({path:location.pathname,anchor:cur.id}))")
replace_once('.toc-sub[href="#${cur.id}"]','.toc-sub[href$="#${cur.id}"]')
replace_once('for(const h of heads){if(h.getBoundingClientRect().top<150)', 'for(const h of heads){if(h.closest("[hidden]"))continue;if(h.getBoundingClientRect().top<150)')
replace_once('h.getBoundingClientRect().top<150', 'h.getBoundingClientRect().top<(document.getElementById("reader-controls")?.getBoundingClientRect().bottom||132)+20')
app_asset=asset('app',app)
reader_asset=asset('reading-mode',english_ui((root/'reader-mode.js').read_text(encoding='utf-8')))

# Wrap existing direct children only: no text or formula nodes are recreated.
pre_reading_chapters={k:v for k,v in sections.items() if k.startswith('chapter-')}
reading_manifest={}
paired_units=json.loads((root/'build/reading-units.json').read_text('utf-8')) if english_book else {}
for key in [k for k in pages if k.startswith('chapter-')]:
    soup=BeautifulSoup(sections[key],'html.parser');book=soup.find('section',id=key)
    groups=[];unit=soup.new_tag('div',attrs={'class':'reading-unit','id':key+'-unit-0','data-reader-title':'Introduction' if english_book else '章首导读'})
    book.append(unit);groups.append(unit)
    for child in list(book.contents):
        if getattr(child,'get',None) and 'reading-unit' in child.get('class',[]):continue
        if getattr(child,'get',None) and 'chapter-links' in child.get('class',[]):continue
        title=child.get_text(' ',strip=True) if getattr(child,'name',None) in ['h1','h2','h3'] else ''
        is_numbered=bool(re.match(r'^'+key.split('-')[1]+r'\.\d+(?![\d.])(?:\s|$)',title))
        is_ending=getattr(child,'name',None) in ['h1','h2'] and bool(re.search(r'Closing Chapter|Conclusion|Summary of ideas|^Toward|^Next Chapter' if english_book else r'结语|思想小结|^通向|^下一章',title,re.I) or (getattr(child,'get',None) and 'draft-preview' in child.get('class',[])))
        if english_book:
            # Paired heading IDs preserve the author's exact section boundaries in both languages.
            is_numbered=getattr(child,'get',None) and child.get('id') in {u['anchor'] for u in paired_units[key][1:]}
            is_ending=False
        if is_numbered or is_ending:
            label=title.replace('\\sqrt n','√n').replace('\\sigma','σ')
            unit=soup.new_tag('div',attrs={'class':'reading-unit','id':key+'-unit-'+str(len(groups)),'data-reader-title':label})
            book.insert(book.contents.index(groups[-1])+1,unit);groups.append(unit)
        unit.append(child.extract())
    for u in groups:
        head=u.find(re.compile('^h[1-6]$'))
        u['data-reader-anchor']=head['id'] if head else u['id']
    for chapter_nav in book.find_all('div',class_='chapter-links',recursive=False):
        book.append(chapter_nav.extract())
    reading_manifest[key]=[{'id':u['id'],'title':u['data-reader-title'],'anchor':u['data-reader-anchor']} for u in groups]
    sections[key]=str(soup)
(root/('build/reading-units'+suffix+'.json')).write_text(json.dumps(reading_manifest,ensure_ascii=False,indent=2),encoding='utf-8')
def nav(current):
    # One global chapter list; only this page's detailed contents start expanded.
    def detail(m):
        value=m[0];value=re.sub(r'^<details\b[^>]*>','<details>',value)
        if f'href="#{current}"' in value:value=value.replace('<details>','<details open>',1).replace(f'href="#{current}"',f'aria-current="page" href="#{current}"',1)
        return value
    value=re.sub(r'<details\b[^>]*>[\s\S]*?</details>',detail,sidebar)
    value=value.replace('<nav>','<a class="catalogue-home" href="'+book_home+'">← '+('Book contents' if english_book else '全书目录')+'</a><nav>',1)
    return links(value)
def localize(value,key):
    current='/en/index.html' if key=='home-en' else pages.get(key,'/index.html');parent=posixpath.dirname(current).lstrip('/') or '.'
    return re.sub(r'(\b(?:href|src)=")/([^"<>]*)(")',lambda m:m[1]+posixpath.relpath(m[2] or 'index.html',parent)+m[3],value)

def document(key,body,home=False,english=None):
    if english is None:english=english_book
    title=('The Mathematics of Chance' if english else '全书目录') if home else titles[key]
    page_header=header
    current_page=pages.get(key,'/en/index.html' if english else '/index.html')
    counterpart=current_page.removeprefix('/en') if english else '/en'+current_page
    page_header=header.replace('<div class="tools">',utility(site_links,english,counterpart)+'<div class="tools">',1)
    page_nav=english_sidebar(slugs) if english and home else nav(key)
    page_dialog=dialog
    page_footer=footer
    if english:
        for old,new in [('>检索<','>Search<'),('>夜间<','>Theme<'),('>目录<','>Contents<')]:page_header=page_header.replace(old,new)
        page_dialog=page_dialog.replace('检索全部正文','Search all chapter text').replace('输入人物、概念或一句原文','Search the English manuscript').replace('关闭检索','Close search')
        page_footer='<footer>The Mathematics of Chance · '+str(len(slugs))+' long-form chapters<br>Complete English working translation · For author review</footer>'
    context='' if home else '<div class="reading-context"><a href="'+book_home+'">'+('The Mathematics of Chance / Contents' if english else '偶然的数学 / 全书目录')+'</a><span>'+(('Chapter progress' if key.startswith('chapter-') else 'Page progress') if english else ('本章阅读进度' if key.startswith('chapter-') else '本页阅读进度'))+'</span></div>'
    reader_controls=''
    if key in reading_manifest:
        options=''.join('<option value="'+str(i)+'">'+html.escape(u['title'])+'</option>' for i,u in enumerate(reading_manifest[key]))
        reader_controls='<div id="reader-controls" class="reader-controls" aria-label="阅读方式"><div class="reader-mode-buttons" role="group" aria-label="阅读模式"><button type="button" data-reading-mode="section" aria-pressed="true">按小节阅读</button><button type="button" data-reading-mode="chapter" aria-pressed="false">整章阅读</button><button type="button" id="reader-previous-top" aria-label="上一节（顶部）" disabled>← 上一节</button><button type="button" id="reader-next-top" aria-label="下一节（顶部）">下一节 →</button><span id="reader-status" aria-live="polite"></span></div><label class="reader-section-label" for="reader-section">小节<select id="reader-section">'+options+'</select></label></div>'
        body+='<nav class="reader-pagination" aria-label="小节导航"><button type="button" id="reader-previous" disabled>← 上一节</button><button type="button" id="reader-next">下一节 →</button></nav>'
    result='<!doctype html><html lang="'+('en' if english else 'zh-CN')+'"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="'+('An original book on the history, ideas and mathematical structures of probability. Complete English chapters, proofs and references, alongside the unchanged Chinese manuscripts.' if english else '偶然的数学：'+str(len(slugs))+'章长篇工作稿，独立章节阅读，保留历史、推导、引用与交互。')+'"><title>'+html.escape(title)+' · 偶然的数学</title><link rel="stylesheet" href="'+css+'"></head><body class="'+('home english-home' if home and english else 'home' if home else 'chapter-page english-reading' if english else 'chapter-page')+'" data-book-root="'+('../' if english or key.startswith(('chapter-','advanced-')) else './')+'" data-reader-page="'+key+'"><div class="progress" id="progress"></div>'+page_header+page_nav+page_dialog+'<main>'+context+body+page_footer+'</main><button id="back-top" aria-label="'+('Back to top' if english else '返回顶部')+'">↑</button>'+''.join('<script src="'+p+'"></script>' for p in [search_asset,experiment_asset,app_asset])+'</body></html>'
    if reader_controls:
        result=result.replace('<main>'+context,'<main>'+context+reader_controls,1).replace('</body>','<script src="'+reader_asset+'"></script></body>',1)
    result=result.replace('</body>','<script src="'+home_ui_asset+'"></script></body>',1)
    if english_book:
        result=english_ui(result).replace('data-book-root="../"','data-book-root="../../"' if key.startswith(('chapter-','advanced-')) else 'data-book-root="../"')
    return localize(result,key)

descriptions=['从中断的赌局出发，追问公平、对称性、独立性与可加性。','从经验频率到 Bernoulli、Bayes 与未知概率的推断。','沿着二项分布与特征函数，追问正态极限及其成立条件。','从 Gaussian 快照走向整条随机路径的问题；高级技术完整后移。','从无限集合的矛盾建立 σ-代数、外测度和概率测度。','从公平收益的加权平均，完整建立积分与极限交换的语言。','从罕见而反复的异常与收缩尖峰，理解四种收敛及一致可积性。','从有限实验的相容规则出发，构造乘积概率与无限随机记录，再回到 Brownian 路径。']
catalogue='<section class="catalogue" id="contents"><h2>'+chapter_count_label+' · 阅读目录</h2><p class="section-search-hint">每章独立打开。左侧目录或手机顶部“目录”可随时切换章节。</p>'
for i in range(1,len(slugs)+1):
    key=f'chapter-{i}';label=re.sub(r'^第.章：','',titles[key])
    catalogue+=f'<a class="catalogue-item" href="{pages[key]}"><span class="chapter-number">{i:02d}</span><span><span class="catalogue-title">{html.escape(label)}</span><span class="catalogue-description">{descriptions[i-1]}</span></span><span class="catalogue-arrow">→</span></a>'
catalogue+='<div class="extra-pages">'+''.join(f'<a href="{pages[k]}">{titles[k]}</a>' for k in ['rules','supplement','reading-routes','references'])+'</div>'
catalogue+='<h2>第四章后续 · 进阶阅读</h2><p>原技术段落完整后移，保留旧节号；证明依赖与目的章节在模块开头说明。无需先读完这些模块再进入第五章。</p><div class="extra-pages">'+''.join(f'<a href="{pages[m["id"]]}">{html.escape(m["title"])}</a>' for m in modules)+'</div></section>'
if english_book:
    en_version='<details class="home-version"><summary>About this reading edition</summary><p>All eight chapters, advanced modules, supplementary proofs, references and writing guidance have full English working translations. The Chinese manuscripts remain unchanged. Translations await author review and do not change the independent mathematical or historical review states.</p><p>This is a local preview. The published edition has not been replaced.</p></details>'
    (dist/'en').mkdir(exist_ok=True)
    (dist/'en/index.html').write_bytes(document('home-en',hero(site_links,len(slugs),True)+english_catalogue(slugs)+en_version,True,True).encode())
else:
    cover=hero(site_links,len(slugs))
    version='<details class="home-version"><summary>版本与阅读说明</summary>'+sections['edition']+'</details>'
    (dist/'index.html').write_bytes(document('home',cover+catalogue+version,True).encode())

manifest=[]
for key,path in pages.items():
    body=links(sections[key])
    file=dist/path.lstrip('/');file.parent.mkdir(parents=True,exist_ok=True)
    file.write_bytes(document(key,body).encode())
    manifest.append({'section':key,'url':path,'title':titles[key],'source_section_sha256':hashlib.sha256(sections[key].encode()).hexdigest(),'routed_section_sha256':hashlib.sha256(body.encode()).hexdigest(),'formula_count':body.count('class="formula '),'bytes':file.stat().st_size})
# Keep old bookmarks useful after the root URL becomes a chapter catalogue.
legacy='const oldAnchors='+json.dumps({k:posixpath.relpath(route(k).lstrip('/') or 'index.html','en' if english_book else '.') for k in owners})+';const h=decodeURIComponent(location.hash.slice(1));if(h&&oldAnchors[h])location.replace(oldAnchors[h]);'
home=dist/('en/index.html' if english_book else 'index.html');text=home.read_bytes().decode();text=text.replace('</body>','<script>'+legacy+'</script></body>');home.write_bytes(text.encode())
(root/('build/chapter-pages'+suffix+'.json')).write_text(json.dumps({'pages':manifest,'total_formulas':sum(x['formula_count'] for x in manifest),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'content_policy':'Each original section is retained in full; only internal link destinations are rewritten to their owning page. No prose, equations, images, citations, or experiments are removed.'},ensure_ascii=False,indent=2),encoding='utf-8')
expected_formulas=json.loads((root/('build/render-check'+suffix+'.json')).read_text(encoding='utf-8'))['mathCount']
assert sum(x['formula_count'] for x in manifest)==expected_formulas
assert all((dist/p.lstrip('/')).exists() for p in pages.values())
(root/('build/pre-reading-chapters'+suffix+'.json')).write_bytes(json.dumps({k:localize(links(v),k) for k,v in pre_reading_chapters.items()},ensure_ascii=False).encode('utf-8'))
print(json.dumps({'locale':'en' if english_book else 'zh-CN','pages':len(manifest)+1,'chapters':len(slugs),'formulas':expected_formulas,'home_bytes':home.stat().st_size,'chapter_bytes':[x['bytes'] for x in manifest if x['section'].startswith('chapter-')]},ensure_ascii=False))
