"""Reader information architecture; preserve mathematical bodies and legacy IDs."""
from pathlib import Path
from functools import lru_cache
import html,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
def config(root=ROOT):return json.loads((root/'publication/academic-navigation.json').read_text('utf8'))
def esc(s):return html.escape(str(s),quote=True)
def label(zh,en,english):return en if english else zh

@lru_cache(maxsize=64)
def section_headings(markup):
    """Parse each immutable section once, rather than on every page's sidebar."""
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(markup,'html.parser');result=[]
    for n in soup.select('h2[id],h3[id]'):
        if 'draft-preview' in n.get('class',[]):continue
        clone=BeautifulSoup(str(n),'html.parser')
        for child in clone.select('[id]'):del child['id']
        result.append((n['id'],clone.find(n.name).decode_contents()))
    return tuple(result)
def module_body_html(markup):
    """Strip the archival wrapper only; title and all content after its first rule remain."""
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(markup,'html.parser');root=soup.select_one('.book-section') or soup
    rule=root.find('hr',recursive=False);assert rule,'module wrapper boundary missing'
    keep_title=root.find('h1',recursive=False);removed=[]
    for node in list(root.contents):
        if node is rule:break
        if node is keep_title:continue
        if getattr(node,'attrs',None) is not None:
            removed.extend(n['id'] for n in [node,*node.select('[id]')] if n.get('id'))
        node.extract()
    # Keep the original rule and every mathematical node that follows it.
    for node in list(root.select(':scope > .chapter-links')):node.decompose()
    for key in removed:
        alias=soup.new_tag('span',attrs={'id':key,'class':'legacy-editorial-anchor','aria-hidden':'true'});root.insert(0,alias)
    return str(soup)

def split_supplement(markup,english=False):
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(markup,'html.parser');root=soup.select_one('.book-section') or soup
    blocks={k:[] for k in 'ABCDEFG'};preface=[];current=None;title=None
    for node in list(root.contents):
        if getattr(node,'name',None)=='h1' and title is None:title=node;continue
        if getattr(node,'get',None) and 'chapter-links' in node.get('class',[]):continue
        if getattr(node,'name',None)=='h2':
            match=re.match(r'^([A-G])\.\s',node.get_text(' ',strip=True))
            if match:current=match[1]
        if current:blocks[current].append(node)
        else:preface.append(node)
    assert all(blocks.values()),'appendix A–G partition incomplete'
    # G's opening/restoration note and final editorial permission note are not proofs.
    g_paragraphs=[n for n in blocks['G'] if getattr(n,'name',None)=='p']
    assert len(g_paragraphs)==2,'review the G editorial classification'
    blocks['G']=[n for n in blocks['G'] if n not in g_paragraphs]
    preface+=g_paragraphs
    result={}
    for key,item in config()['supplement_facets'].items():
        out=BeautifulSoup('<section class="book-section"></section>','html.parser');target=out.section
        target['id']=key;target['data-title']=item['title_en' if english else 'title_zh']
        if key=='supplement':
            title.string=item['title_en' if english else 'title_zh'];target.append(title)
            for node in preface:
                for original in ([node]+list(node.select('[id]')) if getattr(node,'select',None) else []):
                    if original.get('id'):
                        target.append(out.new_tag('span',attrs={'id':original['id'],'class':'legacy-editorial-anchor','aria-hidden':'true'}))
        for letter in item['letters']:
            for node in blocks[letter]:target.append(node)
        result[key]=str(out)
    return result

def organize_sections(sections,english=False):
    result=dict(sections)
    # Keep old search/formula bookmarks even after wrappers and appendix pages split.
    from bs4 import BeautifulSoup
    def legacy_ids(markup,key):
        soup=BeautifulSoup(markup,'html.parser')
        for i,node in enumerate(soup.select('h1,h2,h3,h4,h5,h6,p,li,td,th,.formula'),1):
            if node.find_parent(class_='formula') or node.find_parent(class_='chapter-links'):continue
            if not node.get('id'):node['id']=f'search-{key}-{i}'
        return str(soup)
    for item in config()['modules']:
        key='advanced-'+item['slug'];result[key]=module_body_html(legacy_ids(result[key],key))
    result.update(split_supplement(legacy_ids(result['supplement'],'supplement'),english))
    return result

def chapter_reference(n,slugs,english):
    text=label('第'+str(n)+'章','Chapter '+str(n),english)
    if n<=len(slugs):return '<a href="'+('/en' if english else '')+'/chapters/'+slugs[n-1]+'.html">'+text+'</a>'
    return '<span class="planned-chapter">'+text+' <small>'+label('（尚未写成）','(not yet written)',english)+'</small></span>'

def module_panel(item,slugs,english=False):
    cfg=config();locale='en' if english else 'zh';prefix='/en' if english else ''
    title=label('归属与证明范围','Chapter ownership and proof scope',english)
    owner=chapter_reference(item['owner_chapter'],slugs,english)
    related=' · '.join(chapter_reference(n,slugs,english) for n in item['supporting_chapters'])
    rows=''.join('<li><span class="proof-state '+s['status']+'">'+esc(cfg['status_labels'][s['status']][int(english)])+'</span><p>'+esc(s[locale])+'</p></li>' for s in item['statements'])
    file=ROOT/('advanced-en' if english else 'advanced')/(item['slug']+'.md')
    prelude=file.read_text('utf8').split('\n---\n',1)[0]
    prereq=next((s.split('**',2)[-1].strip() for s in prelude.splitlines() if s.startswith('**') and ('前置' in s or 'Prerequisites' in s)),'')
    return '<section class="academic-panel" aria-label="'+title+'"><p class="academic-eyebrow">'+title+'</p><p>'+label('主要证明归属：','Primary proof chapter: ',english)+owner+'</p><p>'+label('相关工具与应用：','Related tools and applications: ',english)+related+'</p><ul class="proof-status-list">'+rows+'</ul><details><summary>'+label('分段阅读所需工具','Tools needed by the individual arguments',english)+'</summary><p>'+esc(prereq)+'</p></details><p class="academic-note">'+label('状态限定于已写材料，不表示本专题已全部证明或通过数学终审。','These states describe the existing material; they do not certify a complete theorem treatment or final mathematical review.',english)+'</p><nav><a href="'+prefix+'/chapters/04-brownian.html">'+label('返回第四章','Return to Chapter 4',english)+'</a> · <a href="'+prefix+'/reading-routes.html">'+label('专题与证明索引','Topic and proof index',english)+'</a></nav></section>'

def page_panel(key,slugs,english=False):
    cfg=config();prefix='/en' if english else ''
    if key.startswith('advanced-'):
        item=next(x for x in cfg['modules'] if 'advanced-'+x['slug']==key);return module_panel(item,slugs,english)
    if key=='reading-routes':
        intro=label('正式章节是主要阅读路线。这里的专题与证明服务于对应章节，现有工作材料不构成另一套平行教材。','The chapters are the main reading route. These topics and proofs support their chapters; working material is not a second parallel textbook.',english)
        cards=''.join('<article class="academic-topic-card"><h2><a href="'+prefix+'/advanced/'+x['slug']+'.html">'+esc(x['title_en' if english else 'title_zh'])+'</a></h2><p>'+label('主要归属：','Primary chapter: ',english)+chapter_reference(x['owner_chapter'],slugs,english)+'</p><ul>'+''.join('<li><span class="proof-state '+s['status']+'">'+esc(cfg['status_labels'][s['status']][int(english)])+'</span> '+esc(s['en' if english else 'zh'])+'</li>' for s in x['statements'])+'</ul></article>' for x in cfg['modules'])
        proof_links=[('/proofs.html',label('数学证明 A–D','Mathematical proofs A–D',english)),('/proofs/finite-dimensional.html',label('有限维计算与边界','Finite-dimensional calculations and scope',english)),('/proofs/t-mclass.html',label('生成类与测度唯一性','Generating classes and measure uniqueness',english)),('/proofs/t-integral.html',label('积分与DCT','Integration and DCT',english)),('/proofs/t-measure.html',label('完备化与Borel集','Completion and Borel sets',english)),('/proofs/t-lp.html',label('Hölder、Minkowski与Lp完备性','Hölder, Minkowski and Lp completeness',english))]
        proof_nav='<h2>'+label('基础与补充证明','Foundations and companion proofs',english)+'</h2><nav>'+''.join('<p><a href="'+prefix+p+'">'+esc(t)+'</a></p>' for p,t in proof_links)+'</nav>'
        return '<section class="academic-panel academic-hub"><h1>'+label('专题阅读与数学证明','Topics and Mathematical Proofs',english)+'</h1><p>'+intro+'</p><p><a href="'+prefix+'/index.html#contents">'+label('回到正文章节目录','Return to the chapter contents',english)+'</a></p>'+cards+proof_nav+'</section>'
    texts={
      'supplement':('本页集中列出附录A–D的书面数学证明。可测版本约定、有限维计算与早期证明边界各有独立入口；书面证明不等于数学终审。','This page collects the written mathematical proofs in Appendices A–D. Measurable-version errata, finite-dimensional calculations and historical proof boundaries have separate pages. A written proof is not final mathematical approval.'),
      'errata':('这里说明公开的可测性与版本约定。一般零集修改及DCT证明见积分基础补证；不含内部工程记录。','These are public measurability and version conventions. General null-set and DCT proofs are in the integral companion; internal engineering records are excluded.'),
      'finite-dimensional-proof':('以下有限维增量的等式与特征函数乘积计算已有书面推导；最终向量极限识别仍调用多元连续性与连续映射工具，第十四章负责完整建立。本段不是路径空间收敛证明。','The finite-dimensional increment identities and characteristic-function product calculations are written out. Vector-limit identification still invokes multivariate continuity and continuous-mapping tools, whose full development belongs to Chapter 14. This is not a path-space convergence proof.'),
      'proof-boundaries':('下表限定为早期六章工作稿的历史证明范围，并非当前全书完成清单。第十一、十二章和基础补证已提供部分后续证明；六个高级专题的当前归属和待证范围以专题索引为准。','This table records the historical proof scope of the early six-chapter manuscript, not the current book’s completion state. Chapters 11–12 and the foundation companions provide later proofs. Consult the topic index for current ownership and pending results.')}
    if key not in texts:return ''
    title=cfg['supplement_facets'][key]['title_en' if english else 'title_zh']
    routes=' · '.join('<a href="'+prefix+x['route']+'">'+esc(x['title_en' if english else 'title_zh'])+'</a>' for k,x in cfg['supplement_facets'].items() if k!=key)
    return '<section class="academic-panel"><h1>'+esc(title)+'</h1><p>'+texts[key][int(english)]+'</p><nav>'+routes+' · <a href="'+prefix+'/reading-routes.html">'+label('专题索引','Topic index',english)+'</a></nav></section>'

def sidebar(current,pages,titles,sections,english=False):
    prefix='/en' if english else '';cfg=config()
    def entry(key,details=False):
        active=key==current;name=titles[key];href=pages[key]
        a='<a'+(' aria-current="page"' if active else '')+' href="'+href+'">'+esc(name)+'</a>'
        if not details:return a
        sublinks=['<a class="toc-sub" href="'+href+'#'+esc(anchor)+'">'+heading+'</a>' for anchor,heading in section_headings(sections[key])]
        subs=''.join(sublinks)
        return '<details class="'+('chapter-nav-item' if key.startswith('chapter-') else 'topic-nav-item')+'"'+(' open' if active else '')+'><summary>'+a+'</summary><div>'+subs+'</div></details>'
    chapters=[k for k in pages if k.startswith('chapter-')]
    from tools.volume_navigation import sidebar as volume_sidebar
    chapter_list=volume_sidebar(current,chapters,entry,english)
    topic_open=current.startswith(('advanced-','foundation-')) or current in {'reading-routes','supplement','finite-dimensional-proof'}
    topics='<details id="academic-topics-nav" class="academic-nav-group"'+(' open' if topic_open else '')+'><summary>'+label('专题阅读与数学证明','Topics and Mathematical Proofs',english)+'</summary><nav class="topic-links">'+entry('reading-routes')+'<p class="nav-subheading">'+label('六个专题','Six supporting topics',english)+'</p>'+''.join(entry('advanced-'+x['slug'],True) for x in cfg['modules'])+'<p class="nav-subheading">'+label('数学证明','Mathematical proofs',english)+'</p>'+entry('supplement')+entry('finite-dimensional-proof')+''.join(entry(k) for k in pages if k.startswith('foundation-'))+'</nav></details>'
    resource_open=current in {'references','rules','errata','proof-boundaries','versions'}
    aux=[('references',label('引用与配图来源','References and Image Sources',english)),('errata',label('公开勘误','Public errata',english)),('proof-boundaries',label('早期证明范围','Historical proof scope',english)),('rules',label('写作原则','Writing principles',english))]
    resources='<details class="academic-nav-group resources-nav"'+(' open' if resource_open else '')+'><summary>'+label('资料与版本','Sources and Versions',english)+'</summary><nav>'+''.join('<a href="'+pages[k]+'">'+esc(t)+'</a>' for k,t in aux)+'<a href="'+prefix+'/citation.html">'+label('引用本书','Cite this book',english)+'</a><a href="'+prefix+'/versions.html">'+label('版本与正式快照','Versions and formal snapshots',english)+'</a></nav></details>'
    topics=topics.replace('<p class="nav-subheading">','<a href="'+prefix+'/visuals.html">'+label('数学图示与实验','Mathematical figures and experiments',english)+'</a><p class="nav-subheading">',1)
    return '<aside id="sidebar"><div class="side-label">'+label('正文章节','BOOK CHAPTERS',english)+'</div><a class="catalogue-home" href="'+prefix+'/index.html">← '+label('全书目录','Book contents',english)+'</a><nav class="primary-chapters">'+chapter_list+'</nav>'+topics+resources+'</aside>'

def home_resources(english=False):
    prefix='/en' if english else ''
    return '<section class="academic-home-resources"><details><summary>'+label('专题阅读与数学证明','Topics and Mathematical Proofs',english)+'</summary><p>'+label('按章节归属查阅六个专题及配套证明。','Browse the six topics and companion proofs by their chapter ownership.',english)+'</p><a href="'+prefix+'/reading-routes.html">'+label('打开专题与证明索引','Open the topic and proof index',english)+'</a></details><details><summary>'+label('资料与版本','Sources and Versions',english)+'</summary><nav><a href="'+prefix+'/references.html">'+label('引用与配图来源','References and image sources',english)+'</a><a href="'+prefix+'/errata.html">'+label('公开勘误','Public errata',english)+'</a><a href="'+prefix+'/versions.html">'+label('版本信息','Version information',english)+'</a></nav></details></section>'

def sanitize_reader_sources(root,files):
    """Clean only archival wrappers in exported reader sources; math bodies stay exact."""
    cfg=config(root);out=dict(files);changes={}
    for item in cfg['modules']:
        for english,folder in [(False,'advanced'),(True,'advanced-en')]:
            name=folder+'/'+item['slug']+'.md';raw=files[name];s=raw.decode();nl='\r\n' if '\r\n' in s else '\n';text=s.replace('\r\n','\n')
            header,body=text.split('\n---\n',1);lines=header.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('> '):lines[i]='> '+label('专题工作材料；分项证明范围以网页说明为准。','Working topic material; see the page for the scope of each argument.',english)
                if line.startswith('**') and ('目的章节' in line or 'Destination chapters' in line or 'Destination Chapters' in line):lines[i]='**'+label('主要归属：','Primary chapter:',english)+'** '+str(item['owner_chapter'])
                if line.startswith('**') and ('证明边界' in line or 'Scope of the proof' in line):lines[i]='**'+label('证明范围：','Proof scope:',english)+'** '+' '.join(s['en' if english else 'zh'] for s in item['statements'])
                if line.startswith('[返回第四章') or line.startswith('[Return to '):lines[i]=label('[返回第四章](#chapter-4) · [专题与证明索引](#reading-routes)','[Return to Chapter 4](#chapter-4) · [Topic and proof index](#reading-routes)',english)
            cleaned='\n'.join(lines).rstrip('\n')+'\n\n---\n'+body
            assert cleaned.split('\n---\n',1)[1]==body
            out[name]=cleaned.replace('\n',nl).encode();changes[name]={'canonical_sha256':hashlib.sha256(raw).hexdigest(),'reader_source_sha256':hashlib.sha256(out[name]).hexdigest(),'mathematical_body_sha256':hashlib.sha256(body.encode()).hexdigest(),'scope':'ARCHIVAL_WRAPPER_ONLY_MATHEMATICAL_BODY_IDENTICAL'}
    for english,name in [(False,'校订与证明补充.md'),(True,'translations/en/proofs.md')]:
        raw=files[name];s=raw.decode();nl='\r\n' if '\r\n' in s else '\n';blocks=re.split(r'\n\s*\n',s.replace('\r\n','\n').strip())
        assert blocks[0].startswith('# ') and blocks[2].startswith('## A.')
        blocks[1]=label('本附录保存数学补证；公开勘误、有限维计算及证明范围在网站中分类阅读。','This appendix preserves mathematical supplements; the website separates public errata, finite-dimensional calculations and proof scope.',english)
        at=next(i for i,b in enumerate(blocks) if b.startswith('## G.'))
        blocks[at+1]=label('下表限于早期六章工作稿的证明范围；当前归属与分项状态见专题索引。','The table concerns the early six-chapter manuscript only; see the topic index for current ownership and proof states.',english)
        blocks[-1]=label('当前证明状态须按具体结果与假设核对；书面证明不等于数学终审。','Check current proof states result by result under their hypotheses; a written proof is not final mathematical approval.',english)
        out[name]=('\n\n'.join(blocks)+'\n').replace('\n',nl).encode();changes[name]={'canonical_sha256':hashlib.sha256(raw).hexdigest(),'reader_source_sha256':hashlib.sha256(out[name]).hexdigest(),'scope':'EDITORIAL_INTRODUCTION_AND_SCOPE_FRAMING_ONLY_MATHEMATICAL_SECTIONS_UNCHANGED'}
    m=json.loads(out['translations/en/manifest.json'])
    for row in m['files']:
        if row['source'] in changes:row['source_sha256']=hashlib.sha256(out[row['source']]).hexdigest()
        if row['translation'] in changes:row['translation_sha256']=hashlib.sha256(out[row['translation']]).hexdigest()
    out['translations/en/manifest.json']=(json.dumps(m,ensure_ascii=False,indent=2)+'\n').encode()
    out['publication/reader-source-sanitization.json']=(json.dumps({'policy':'Canonical originals stay in the author review export; reader-source cleanup changes editorial wrappers only.','files':changes},ensure_ascii=False,indent=2)+'\n').encode()
    return out,changes
