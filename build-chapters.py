"""Publish the exact existing book sections as independent HTML documents."""
from pathlib import Path
from html.parser import HTMLParser
import sys,posixpath,shutil
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
import re,json,hashlib,html
from tools.homepage import hero, utility, english_catalogue, english_sidebar
from tools.publication_site import PublicationSite, ROUTES as PUBLICATION_ROUTES, LABELS as PUBLICATION_LABELS
from tools.academic_navigation import organize_sections,sidebar as academic_sidebar,page_panel,home_resources,config as academic_config
from tools.math_visuals import insert_figures,copy_assets,records as visual_records,figure_html
from tools import volume_navigation as volumes
root=Path(__file__).parent
def write_page(file,data):
    # Build into a sibling first: a failed Windows open must not truncate an
    # otherwise valid preview, and replacement keeps readers from partial HTML.
    import time
    if file.exists() and file.read_bytes()==data:return
    pending=file.with_name(file.name+'.building')
    try:
        for attempt in range(6):
            try:
                pending.write_bytes(data)
                pending.replace(file)
                break
            except OSError as error:
                if attempt==5 or (getattr(error,'winerror',None) not in {5,32} and error.errno!=22):raise
                time.sleep(.15*2**attempt)
    finally:
        if pending.exists():pending.unlink()
publication=PublicationSite(root)
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
supporting=inputs.get('supporting_proofs',[])
assert len(sections)==len(inputs['chapters'])+6+len(modules)+len(supporting)
sections=organize_sections(sections,english_book)
opening_anchors=json.loads((root/'publication/chapter11-opening-anchors.json').read_text('utf8')) if (root/'publication/chapter11-opening-anchors.json').exists() else {'reserved_paragraphs':{}}
if opening_anchors.get('retired_body_ids'):
    s=BeautifulSoup(sections['chapter-11'],'html.parser')
    heading=next(n for n in s.select('h2') if n.get_text().startswith('11.1 '))
    for anchor_list,target in [(opening_anchors['retired_body_ids'],heading),(opening_anchors['retired_intro_ids'],s.find(id='chapter-11-intro-p3'))]:
        for key in anchor_list:
            alias=s.new_tag('span',attrs={'id':key,'class':'opening-retired-anchor','aria-hidden':'true'})
            target.insert_after(alias);target=alias
    sections['chapter-11']=str(s)
slugs=[Path(p).stem for p in inputs['chapters']]
pages={'rules':'/writing-rules.html',**{f'chapter-{i+1}':f'/chapters/{s}.html' for i,s in enumerate(slugs)},'supplement':'/proofs.html','references':'/references.html'}
pages.update({m['id']:'/advanced/'+m['slug']+'.html' for m in modules})
pages.update({m['id']:'/proofs/'+m['slug']+'.html' for m in supporting})
pages['reading-routes']='/reading-routes.html'
pages.update({k:v['route'] for k,v in academic_config()['supplement_facets'].items()})
if english_book:pages={k:'/en'+v for k,v in pages.items()}
volumes.boundary_links(sections,pages,english_book)
titles={key:html.unescape(re.search(r'data-title="([^"]*)"',sections[key])[1]) for key in pages}
titles['reading-routes']='Topics and Mathematical Proofs' if english_book else '专题阅读与数学证明'
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
css=asset('reader',base_css+'\n'+extra_css+'\n'+(root/'reader-mode.css').read_text(encoding='utf-8')+'\n'+(root/'home.css').read_text(encoding='utf-8')+'\n'+(root/'publication/publication.css').read_text('utf-8')+'\n'+(root/'publication/academic-navigation.css').read_text('utf-8')+'\n'+(root/'publication/volumes.css').read_text('utf8'))
shutil.copytree(root/'assets/images',dist/'assets/images',dirs_exist_ok=True)
shutil.copytree(root/'assets/ui',dist/'assets/ui',dirs_exist_ok=True)
home_ui_asset=asset('home-ui',(root/'home-ui.js').read_text(encoding='utf-8'))
publication_asset=asset('publication',(root/'publication/publication.js').read_text('utf-8'))
reading_analytics_asset=asset('reading-analytics',(root/'analytics-host/public/reader-analytics.js').read_text('utf-8'))
privacy_asset=asset('privacy-controls',(root/'analytics-host/public/privacy-controls.js').read_text('utf-8'))
attribution_asset=asset('campaign-attribution',(root/'analytics-host/public/campaign-attribution.js').read_text('utf-8'))
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
    opening_offset=0;retired_offset=0
    for i,node in enumerate(soup.select('h1,h2,h3,h4,h5,h6,p,li,td,th,.formula'),1):
        if node.get('id','').startswith(('chapter-11-intro-p','chapter-13-revision-p')):opening_offset+=1
        if section_id=='chapter-11' and node.name=='h2':
            part=re.match(r'^(11\.\d+)\s',node.get_text())
            if part:retired_offset+=opening_anchors['reserved_paragraphs'].get(part[1],0)
        if node.find_parent(class_='formula') or node.find_parent(class_='chapter-links'):continue
        if not node.get('id'):node['id']=f'search-{section_id}-{i-opening_offset+retired_offset}'
        clone=BeautifulSoup(str(node),'html.parser')
        for f in clone.select('.formula'):f.replace_with(' '+f.get('data-tex','')+' ')
        text=clone.get_text(' ',strip=True)
        if text:search.append({'id':node['id'],'text':text,'section':section_id})
    from tools.review_anchors import preserve as preserve_review_anchors
    preserve_review_anchors(soup,section_id,search,english_book)
    if section_id in {'chapter-17','chapter-20'}:
        for element in soup.select('[id]'):owners[element['id']]=pages[section_id]
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

# Publication companions are inserted after original search anchors are assigned.
# No protected Markdown or existing paragraph/formula/heading ID changes.
copy_assets()
sections=insert_figures(sections,english_book)
for visual in visual_records():
    owners['visual-'+visual['id']]=pages['chapter-'+str(visual['chapter'])]
owners['experiment-typewriter']=pages['chapter-7']

# Wrap existing direct children only: no text or formula nodes are recreated.
pre_reading_chapters={k:v for k,v in sections.items() if k.startswith('chapter-')}
reading_manifest={}
paired_units=json.loads((root/'build/reading-units.json').read_text('utf-8')) if english_book else {}
for key in [k for k in pages if k.startswith('chapter-')]:
    soup=BeautifulSoup(sections[key],'html.parser');book=soup.find('section',id=key)
    unit_prefix=key+'-recreation' if key=='chapter-20' and (root/'publication/chapter20-recreation-anchors.json').exists() else key+'-charter' if key=='chapter-17' and (root/'publication/chapter17-charter-anchors.json').exists() else key+'-revision' if key=='chapter-17' and (root/'publication/chapter17-revision-anchors.json').exists() else key
    groups=[];unit=soup.new_tag('div',attrs={'class':'reading-unit','id':unit_prefix+'-unit-0','data-reader-title':'Introduction' if english_book else '章首导读'})
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
            unit=soup.new_tag('div',attrs={'class':'reading-unit','id':unit_prefix+'-unit-'+str(len(groups)),'data-reader-title':label})
            book.insert(book.contents.index(groups[-1])+1,unit);groups.append(unit)
        unit.append(child.extract())
    for u in groups:
        head=u.find(re.compile('^h[1-6]$'))
        u['data-reader-anchor']=head['id'] if head else u['id']
    for chapter_nav in book.find_all('div',class_='chapter-links',recursive=False):
        book.append(chapter_nav.extract())
    reading_manifest[key]=[{'id':u['id'],'title':u['data-reader-title'],'anchor':u['data-reader-anchor']} for u in groups]
    if key=='chapter-14':
        history=groups[-1].find_all('h2')[-1]
        groups[-1]['data-reader-title']=history.get_text(' ',strip=True)
        groups[-1]['data-reader-anchor']=history['id']
        reading_manifest[key][-1].update(title=history.get_text(' ',strip=True),anchor=history['id'])
    sections[key]=str(soup)
(root/('build/reading-units'+suffix+'.json')).write_text(json.dumps(reading_manifest,ensure_ascii=False,indent=2),encoding='utf-8')
def nav(current):
    return links(academic_sidebar(current,pages,titles,sections,english_book))
def localize(value,key):
    value=value.replace('href="../assets/visuals/','href="/assets/visuals/')
    current='/en/index.html' if key=='home-en' else pages.get(key,'/index.html');parent=posixpath.dirname(current).lstrip('/') or '.'
    return re.sub(r'(\b(?:href|src)=")/([^"<>]*)(")',lambda m:m[1]+posixpath.relpath(m[2] or 'index.html',parent)+m[3],value)

def document(key,body,home=False,english=None):
    if english is None:english=english_book
    if key=='chapter-14':body=volumes.reader_closing_view(body,english)
    title=('The Mathematics of Chance' if english else '全书目录') if home else titles[key]
    page_header=header
    current_page=pages.get(key,'/en/index.html' if english else '/index.html')
    counterpart=current_page.removeprefix('/en') if english else '/en'+current_page
    page_header=header.replace('<div class="tools">',utility(site_links,english,counterpart)+'<div class="tools">',1)
    page_nav=nav(key)
    page_dialog=dialog
    page_footer=footer
    if english:
        for old,new in [('>检索<','>Search<'),('>夜间<','>Theme<'),('>目录<','>Contents<')]:page_header=page_header.replace(old,new)
        page_dialog=page_dialog.replace('检索全部正文','Search all chapter text').replace('输入人物、概念或一句原文','Search the English manuscript').replace('关闭检索','Close search')
        page_footer='<footer>The Mathematics of Chance · '+str(len(slugs))+' long-form chapters<br>Complete English working translation · For author review</footer>'
    page_footer=publication.footer(english)
    context='' if home or key.startswith('volume-') else '<div class="reading-context"><a href="'+book_home+'">'+('The Mathematics of Chance / Contents' if english else '偶然的数学 / 全书目录')+'</a><span>'+(('Chapter progress' if key.startswith('chapter-') else 'Page progress') if english else ('本章阅读进度' if key.startswith('chapter-') else '本页阅读进度'))+'</span></div>'
    context+=volumes.breadcrumb(key,pages,english)
    reader_controls=''
    if key in reading_manifest:
        options=''.join('<option value="'+str(i)+'">'+html.escape(u['title'])+'</option>' for i,u in enumerate(reading_manifest[key]))
        reader_controls='<div id="reader-controls" class="reader-controls" aria-label="阅读方式"><div class="reader-mode-buttons" role="group" aria-label="阅读模式"><button type="button" data-reading-mode="section" aria-pressed="true">按小节阅读</button><button type="button" data-reading-mode="chapter" aria-pressed="false">整章阅读</button><button type="button" id="reader-previous-top" aria-label="上一节（顶部）" disabled>← 上一节</button><button type="button" id="reader-next-top" aria-label="下一节（顶部）">下一节 →</button><span id="reader-status" aria-live="polite"></span></div><label class="reader-section-label" for="reader-section">小节<select id="reader-section">'+options+'</select></label></div>'
        body+='<nav class="reader-pagination" aria-label="小节导航"><button type="button" id="reader-previous" disabled>← 上一节</button><button type="button" id="reader-next">下一节 →</button></nav>'
    body=publication.chapter_bar(key,english)+page_panel(key,slugs,english)+body
    result='<!doctype html><html lang="'+('en' if english else 'zh-CN')+'"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="'+('An original book on the history, ideas and mathematical structures of probability. Complete English chapters, proofs and references, alongside the unchanged Chinese manuscripts.' if english else '偶然的数学：'+str(len(slugs))+'章长篇工作稿，独立章节阅读，保留历史、推导、引用与交互。')+'"><title>'+html.escape(title)+' · 偶然的数学</title><link rel="stylesheet" href="'+css+'"></head><body class="'+('home english-home' if home and english else 'home' if home else 'chapter-page english-reading' if english else 'chapter-page')+'" data-book-root="'+('../' if english or key.startswith(('chapter-','advanced-','foundation-')) else './')+'" data-reader-page="'+key+'"><div class="progress" id="progress"></div>'+page_header+page_nav+page_dialog+'<main>'+context+body+page_footer+'</main><button id="back-top" aria-label="'+('Back to top' if english else '返回顶部')+'">↑</button>'+''.join('<script src="'+p+'"></script>' for p in [search_asset,experiment_asset,app_asset])+'</body></html>'
    if reader_controls:
        result=result.replace('<main>'+context,'<main>'+context+reader_controls,1).replace('</body>','<script src="'+reader_asset+'"></script></body>',1)
    result=result.replace('</body>','<script src="'+home_ui_asset+'"></script></body>',1)
    if key=='visuals' or key in {'chapter-16','chapter-19','chapter-20','chapter-21','chapter-22','chapter-23','chapter-24','chapter-25','chapter-26'} or key in {'chapter-'+str(v['chapter']) for v in visual_records()}:
        result=result.replace('</head>','<link rel="stylesheet" href="/assets/visuals/typewriter.css"><style>'+(root/'publication/math-visuals.css').read_text('utf8')+'</style></head>',1)
    if key in {'chapter-7','visuals'}:
        result=result.replace('</body>','<script defer src="/assets/visuals/math-model.js"></script><script defer src="/assets/visuals/typewriter.js"></script></body>',1)
    result=result.replace('</head>',publication.head(key,english)+'</head>',1).replace('</body>','<script src="'+publication_asset+'"></script></body>',1)
    result=result.replace('</body>','<script defer src="'+attribution_asset+'"></script></body>',1)
    if key in {'chapter-4','chapter-14'} or (key=='chapter-22' and volumes.chapter_volume(key).get('ending')):
        v=volumes.chapter_volume(key)
        ending_index=len(reading_manifest[key])-(1 if key=='chapter-14' else 0)
        end_url=posixpath.relpath(volumes.url(v,'ending',english).lstrip('/'),posixpath.dirname(current_page).lstrip('/') or '.')
        result=result.replace('data-reader-page="'+key+'"','data-reader-page="'+key+'" data-volume-end="'+end_url+'" data-volume-ending-index="'+str(ending_index)+'"')
    if key.startswith('chapter-'):result=result.replace('</body>','<script defer src="'+reading_analytics_asset+'"></script></body>',1)
    if key=='privacy':result=result.replace('</body>','<script defer src="'+privacy_asset+'"></script></body>',1)
    if key=='supplement':
        # Preserve old /proofs.html#... links after E/F/G acquire their own pages.
        redirects={anchor:posixpath.relpath((owner+'#'+anchor).lstrip('/'),posixpath.dirname(pages[key]).lstrip('/') or '.') for anchor,owner in owners.items() if anchor.startswith(('supplement-','search-supplement-','p')) and owner in {pages['errata'],pages['finite-dimensional-proof'],pages['proof-boundaries']}}
        fallback='<noscript><nav>'+''.join('<a href="'+p+'">'+html.escape(titles[k])+'</a> ' for k,p in pages.items() if k in {'errata','finite-dimensional-proof','proof-boundaries'})+'</nav></noscript>'
        script='const proofAnchorRoutes='+json.dumps(redirects)+';let proofHash;try{proofHash=decodeURIComponent(location.hash.slice(1))}catch{};if(proofHash&&proofAnchorRoutes[proofHash])location.replace(proofAnchorRoutes[proofHash]);'
        result=result.replace('</body>',fallback+'<script>'+script+'</script></body>',1)
    if english_book:
        if key not in PUBLICATION_ROUTES:result=english_ui(result)
        result=result.replace('data-book-root="../"','data-book-root="../../"' if key.startswith(('chapter-','advanced-','foundation-')) else 'data-book-root="../"')
    if key.startswith('volume-'):
        result=re.sub(r'data-book-root="[^"]*"','data-book-root="'+('../../' if english else '../')+'"',result)
    return localize(result,key)

descriptions=['从中断的赌局出发，追问公平、对称性、独立性与可加性。','从经验频率到 Bernoulli、Bayes 与未知概率的推断。','沿着二项分布与特征函数，追问正态极限及其成立条件。','从 Gaussian 快照走向整条随机路径的存在与可测性问题。','从无限集合的矛盾建立 σ-代数、外测度和概率测度。','从公平收益的加权平均，完整建立积分与极限交换的语言。','从罕见而反复的异常与收缩尖峰，理解四种收敛及一致可积性。','从有限实验的相容规则出发，构造乘积概率与无限随机记录，再回到 Brownian 路径。','从公平定价与部分观察出发，建立条件期望、投影几何、Bayes更新和信息流。','从密度与奇异质量，走向条件分布、概率核、析取与无限顺序实验。','从有界频率读数与 Gaussian 平滑，走向分布识别、Lévy 连续性及有限方差 CLT 的完整证明。']
descriptions.append('从途中越界到随机级数、三系判别、一般可积强律与尾部信息。')
descriptions.append('从稀有计数到Poisson误差界、独立标记、Laplace变换与格点局部极限。')
descriptions.append('从改变尺度的独立行，到Lindeberg–Feller、多元极限、稳定吸引域与无限可分。')
descriptions.append('从始终公平却归零的本钱，建立最大估计、上穿、UI闭鞅、Lp与反向条件平均的完整离散理论。')
descriptions.extend(['从玩家的停止规则，理解有界抽样、UI清算与赌博反例。','从过去如何被现在概括，建立Markov核、链构造、强Markov与平稳结构。','从首次返回与Green核，揭示维度怎样改变随机游走的命运。','从返回周期到关键更新、时间偏置与平稳等待。','从一个祖先到灭绝、人口鞅、脊柱与xlogx条件。'])
descriptions.append('从等待年龄到指数无记忆、完整计数构造、独立窗口、补偿鞅和到达流的分合。')
descriptions.append('从随状态变化的时钟，建立最小跳链、爆炸、前后向方程、时间平衡与连续分枝。')
descriptions.append('从Gaussian有限观察到网格连续修改、Wiener测度、条件桥、OU与内积中的随机性。')
descriptions.append('从漏看的尖峰到Polish弱极限、共同紧性、连续路径振荡与跳跃时钟对齐。')
descriptions.append('从最大单步与固定截断到有限方差路径极限，再进入经验桥与更新逆时钟。')
descriptions.append('从首次命中的路径反射，到处处不可微、精确振幅、函数型LIL与时间分配的弧正弦律。')
descriptions.append('从密集小跳的补偿，建立Lévy三元组、原空间分解、稳定吸引域与跳跃极限。')
descriptions.append('从未来收益的平均，到生成元定义域、折扣占有、算子构造与正规Markov路径。')
descriptions.append('从全正面的硬币，到指数倾斜、相对熵、经验分布与Brownian路径的平方能量。')
descriptions.append('从刚出现的到达，区分可选与可预测信息，建立正则化、Doob–Meyer及有限变差补偿。')
descriptions.append('从左端积分和的二阶余量，建立Itô等距、预测L2延拓、连续鞅括号与随机能量时钟。')
catalogue='<section class="catalogue" id="contents"><h2>'+chapter_count_label+' · 阅读目录</h2><p class="section-search-hint">每章独立打开。左侧目录或手机顶部“目录”可随时切换章节。</p>'
for i in range(1,len(slugs)+1):
    key=f'chapter-{i}';label=re.sub(r'^第.章：','',titles[key])
    catalogue+=f'<a class="catalogue-item" href="{pages[key]}"><span class="chapter-number">{i:02d}</span><span><span class="catalogue-title">{html.escape(label)}</span><span class="catalogue-description">{descriptions[i-1]}</span></span><span class="catalogue-arrow">→</span></a>'
descriptions.append('从等待年龄到指数无记忆、完整计数构造、独立窗口、补偿鞅和到达流的分合。')
descriptions.append('从随状态变化的时钟，建立最小跳链、爆炸、前后向方程、时间平衡与连续分枝。')
catalogue=volumes.catalogue(catalogue+'</section>',False)+home_resources(False)
if english_book:
    en_version=f'<details class="home-version"><summary>About this reading edition</summary><p>All {len(slugs)} chapters, advanced modules, supplementary proofs, references and writing guidance have full English working translations. Chinese manuscripts are protected; only explicitly authorized errata and cross-references are applied. Translations await semantic review and do not change the independent mathematical or historical review states.</p><p>Chapter 11 has been adopted by the author. Chapter 13 and its latest refinements have been adopted; Chapter 12 awaits author reading. Chapter 14 is a complete draft under mathematical verification and awaits formal author confirmation. Chapter 15 is a complete bilingual continuation draft awaiting author review; T-LP provides its analysis prerequisites. The published twelve-chapter edition has not been replaced. See the version page for the separate chapter states.</p></details>'
    (dist/'en').mkdir(exist_ok=True)
    en_catalogue=volumes.catalogue(re.sub(r'<div class="extra-pages">[\s\S]*?</div>','',english_catalogue(slugs)),True)
    write_page(dist/'en/index.html',document('home-en',hero(site_links,len(slugs),True)+publication.author_card(True)+en_catalogue+home_resources(True)+en_version,True,True).encode())
else:
    cover=hero(site_links,len(slugs))
    version='<details class="home-version"><summary>版本与阅读说明</summary><p>当前本地预览包含'+str(len(slugs))+'章中英文长篇工作稿及四份数学基础补证。第十一章主体与小修已获作者采用；第十三章及最新完善已采用，数学持续校订；第十二章待作者阅读；第十四章为完整初稿、数学核验中、作者待确认。第十五章已在原六节基础上完整续写，待作者审阅；前十四章、旧补证、插图及认可的卷级文字和样式受保护。</p><p>正文采用、数学核验、史料核验、作者阅读、工程预览与正式发布分别记录，详见<a href="/versions.html">逐章版本页</a>。正式站点为前十二章，第十三至十五章仅本地构建，不覆盖线上版本。</p></details>'
    write_page(dist/'index.html',document('home',cover+publication.author_card()+catalogue+version,True).encode())

manifest=[]
for key,path in pages.items():
    body=links(sections[key])
    file=dist/path.lstrip('/');file.parent.mkdir(parents=True,exist_ok=True)
    write_page(file,document(key,body).encode())
    manifest.append({'section':key,'url':path,'title':titles[key],'source_section_sha256':hashlib.sha256(sections[key].encode()).hexdigest(),'routed_section_sha256':hashlib.sha256(body.encode()).hexdigest(),'formula_count':body.count('class="formula '),'bytes':file.stat().st_size})
# Keep old bookmarks useful after the root URL becomes a chapter catalogue.
legacy='const oldAnchors='+json.dumps({k:posixpath.relpath(route(k).lstrip('/') or 'index.html','en' if english_book else '.') for k in owners})+';const h=decodeURIComponent(location.hash.slice(1));if(h&&oldAnchors[h])location.replace(oldAnchors[h]);'
home=dist/('en/index.html' if english_book else 'index.html');text=home.read_bytes().decode();text=text.replace('</body>','<script>'+legacy+'</script></body>');write_page(home,text.encode())
(root/('build/chapter-pages'+suffix+'.json')).write_text(json.dumps({'pages':manifest,'total_formulas':sum(x['formula_count'] for x in manifest),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'content_policy':'Each original section is retained in full; only internal link destinations are rewritten to their owning page. No prose, equations, images, citations, or experiments are removed.'},ensure_ascii=False,indent=2),encoding='utf-8')
expected_formulas=json.loads((root/('build/render-check'+suffix+'.json')).read_text(encoding='utf-8'))['mathCount']
assert sum(x['formula_count'] for x in manifest)==expected_formulas
assert all((dist/p.lstrip('/')).exists() for p in pages.values())
# Volume pages are derived reading views, not additional mathematical chapters.
# In particular Volume II's ending is extracted from the canonical Chapter 14 DOM.
volume_bodies=volumes.page_bodies(sections,pages,english_book)
for key,(body,title) in volume_bodies.items():
    v=next(v for v in volumes.records() if key.startswith(v['id']+'-'))
    pages[key]=volumes.url(v,key.rsplit('-',1)[1],english_book);titles[key]=title;sections[key]=body
for key,(body,_) in volume_bodies.items():
    file=dist/pages[key].lstrip('/');file.parent.mkdir(parents=True,exist_ok=True)
    print_url='/print/'+key+('.en' if english_book else '.zh')+'.html'
    printable='<a class="volume-print-link" href="'+print_url+'">'+('Printable volume page' if english_book else '可打印卷页')+'</a>'
    page=document(key,links(body)+printable)
    write_page(file,page.encode())
    volumes.print_page(page,file,dist/print_url.lstrip('/'))
(root/('build/pre-reading-chapters'+suffix+'.json')).write_bytes(json.dumps({k:localize(links(v),k) for k,v in pre_reading_chapters.items()},ensure_ascii=False).encode('utf-8'))
print(json.dumps({'locale':'en' if english_book else 'zh-CN','pages':len(manifest)+1,'chapters':len(slugs),'formulas':expected_formulas,'home_bytes':home.stat().st_size,'chapter_bytes':[x['bytes'] for x in manifest if x['section'].startswith('chapter-')]},ensure_ascii=False))

# Publication pages are presentation metadata, outside protected chapter sections.
for key,name in PUBLICATION_ROUTES.items():
    pages[key]=('/en/' if english_book else '/')+name
    titles[key]=PUBLICATION_LABELS[key][int(english_book)]
for key,body in publication.bodies(english_book).items():
    target=dist/pages[key].lstrip('/');target.parent.mkdir(parents=True,exist_ok=True)
    write_page(target,document(key,'<article class="publication-page">'+body+'</article>').encode())
publication.export_metadata()

# Review gallery: the identical figure/caption source used in the chapters.
pages['visuals']=('/en' if english_book else '')+'/visuals.html'
titles['visuals']='Mathematical Figures and Experiments' if english_book else '数学图示与实验'
gallery='<h1>'+titles['visuals']+'</h1><p>'+('Six explanatory figure groups, with standalone print vectors. Only the typewriter example adds a new optional interaction. These figures aid the proofs; they do not replace them.' if english_book else '六组辅助理解图，每组均有独立出版矢量原图。本批只新增移动窗口交互。图像帮助看见数学机制，不代替正文证明。')+'</p>'
for row in visual_records():
    gallery+='<p><a href="'+pages['chapter-'+str(row['chapter'])]+'#visual-'+row['id']+'">'+('Read in Chapter ' if english_book else '在正文中阅读：第')+str(row['chapter'])+('' if english_book else '章')+'</a></p>'+figure_html(row,english_book)
write_page(dist/pages['visuals'].lstrip('/'),document('visuals',gallery).encode())
