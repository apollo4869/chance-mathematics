"""Prepare the author-authorized nine-chapter edition; never export Chapter10.

Run after building a public-only, nine-chapter source copy. Mathematics sections
are compared with the canonical local candidate before any publishing decoration.
"""
from pathlib import Path
from io import BytesIO
import argparse,hashlib,html,json,re,shutil,subprocess,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--checkout',required=True);a=ap.parse_args()
source=Path(a.source).resolve();checkout=Path(a.checkout).resolve();dist=source/'dist';public=checkout/'public'
assert source!=ROOT and checkout!=ROOT and (checkout/'.git').exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
inputs=json.loads((source/'provenance/build-inputs.json').read_text('utf-8'))
assert len(inputs['chapters'])==9
# Some old standalone diagrams survive in the verified web artifact rather than
# the manuscript asset folder. Preserve those exact files and include them in
# the editable source as independent assets as well.
old_assets=json.loads((checkout/'formal-analytics-preservation.json').read_text('utf-8'))['static_asset_hashes']
for n,h in old_assets.items():
    payload=(ROOT/'dist'/n).read_bytes();assert sha(payload)==h,n
    p=source/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(payload)
shutil.copytree(source/'assets',dist/'assets',dirs_exist_ok=True)
for n in ['lib/dashboard.mjs','lib/reading-analytics.mjs']:
    shutil.copyfile(ROOT/'analytics-host'/n,source/'analytics-host'/n)
for language in ['zh','en']:
    shutil.copyfile(ROOT/'publication'/('privacy.'+language+'.html'),source/'publication'/('privacy.'+language+'.html'))
shutil.copyfile(Path(__file__),source/'tools/prepare-formal-nine.py')
origin='https://chance-mathematics-six-chapters.goldenmath7.chatgpt.site/'
edition='nine-chapters-27ac355'
content_commits={n:subprocess.check_output(['git','log','-1','--format=%H','--',n],cwd=ROOT).decode().strip() for folder in ['chapters','chapters-en'] for n in [folder+'/'+x for x in inputs['chapters']]}

def section(text,key):
    m=re.search(r'<section\b[^>]*\bid="'+re.escape(key)+r'"[^>]*>',text);assert m,key
    depth=0
    for t in re.finditer(r'</?section\b[^>]*>',text[m.start():]):
        depth+=-1 if t[0].startswith('</') else 1
        if depth==0:return m.start(),m.start()+t.end()
    raise AssertionError(key)

def body(text,key):
    start,end=section(text,key);s=BeautifulSoup(text[start:end],'html.parser')
    for n in s.select('.section-kicker,.chapter-links'):n.decompose()
    return s.get_text(),[n.get('data-tex') for n in s.select('.formula')],[n['id'] for n in s.select('[id]')]

protected={};formula_count=0
for folder in ['chapters','chapters-en']:
    for name in inputs['chapters']:
        p=folder+'/'+name;data=(source/p).read_bytes()
        assert data==(ROOT/p).read_bytes(),p
        protected[p]=sha(data)
for prefix,mdfolder in [('', 'chapters'),('en/','chapters-en')]:
    for i,name in enumerate(inputs['chapters'],1):
        relative=prefix+'chapters/'+Path(name).with_suffix('.html').name
        before=(dist/relative).read_text('utf-8');canonical=(ROOT/'dist'/relative).read_text('utf-8')
        assert body(before,'chapter-'+str(i))==body(canonical,'chapter-'+str(i)),relative
        formula_count+=len(body(before,'chapter-'+str(i))[1])

# A source snapshot is independent of the hosting version/deployment receipt.
archive_files={p.relative_to(source).as_posix():p.read_bytes() for folder in ['chapters','chapters-en','advanced','advanced-en'] for p in (source/folder).glob('*.md')}
archive_files.update({n:(source/n).read_bytes() for n in ['校订与证明补充.md','引用与配图来源.md','延伸阅读与证明路线.md']})
hashes={n:sha(b) for n,b in archive_files.items()}
snap=dist/'releases'/(edition+'.zip')
with zipfile.ZipFile(snap,'w',zipfile.ZIP_DEFLATED) as z:
    for n,b in sorted(archive_files.items()):z.writestr(n,b)
    z.writestr('contents-sha256.json',json.dumps(hashes,ensure_ascii=False,indent=2))
record={'release_id':edition,'kind':'AUTHOR_AUTHORIZED_WEB_READING_EDITION','author':'Haobai Wang','chapter_count':9,'languages':['zh-CN','en-working-translation'],'content_source_commit':'27ac355','archive_file':snap.name,'archive_sha256':sha(snap.read_bytes()),'files':hashes,'academic_final_review':False}
(dist/'releases'/(edition+'.json')).write_bytes((json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode())

def bib(en=False,chapter=None):
    title='The Mathematics of Chance: The History, Ideas and Mathematical Structures of Probability' if en else '偶然的数学：概率论的历史、思想与数学结构'
    note=edition+'; nine-chapter public reading edition; academic final review not implied'
    url=origin+('en/' if en else '')
    if chapter:
        filename=inputs['chapters'][chapter-1];folder='chapters-en' if en else 'chapters'
        text=(source/folder/filename).read_text('utf-8')
        title=next(line.lstrip('# ') for line in text.splitlines() if line.startswith('# Chapter ') or re.match(r'^# 第.+章[：:]',line))
        note+='; SHA-256 '+protected[folder+'/'+filename]
        url+='chapters/'+Path(filename).with_suffix('.html').name
    return '@misc{wang2026chance'+('_ch'+str(chapter) if chapter else '')+('_en' if en else '')+',\n  author = {Wang, Haobai},\n  title = {{'+title+'}},\n  year = {2026},\n  url = {'+url+'},\n  note = {'+note+'}\n}'

for p in dist.rglob('*.html'):
    text=p.read_text('utf-8');frozen=[]
    # Decorate only outside book sections; retained chapter/proof bytes stay exact.
    for key in re.findall(r'<section\b[^>]*\bid="((?:chapter-\d+|advanced-[^\"]+|supplement|references))"',text):
        start,end=section(text,key);fragment=text[start:end];token='PRESERVEDBOOKFRAGMENT'+str(len(frozen))+'END'
        text=text[:start]+token+text[end:];frozen.append((token,fragment))
    text=text.replace('Local preview','Public reading edition').replace('local preview','public reading edition').replace('本地预览','公开阅读版')
    text=text.replace('This is a public reading edition. The published edition has not been replaced.','Nine-chapter public reading edition. English translations await author review.')
    text=text.replace('不填造出版社、ISBN、DOI或一个并不存在的公开第九章网址','不填造出版社、ISBN或DOI；九章正式阅读网址已公开')
    text=text.replace('No publisher, ISBN, DOI or nonexistent public Chapter 9 URL is invented.','No publisher, ISBN or DOI is invented. Chapter 9 is available at the official reading URL.')
    for token,fragment in frozen:text=text.replace(token,fragment)
    if p.name=='citation.html':
        en='en' in p.relative_to(dist).parts;s=BeautifulSoup(text,'html.parser')
        lead=s.select_one('.pub-lead');lead.string='请引用 Haobai Wang，并注明九章公开阅读版及内容指纹；英文是完整翻译工作稿。' if not en else 'Credit Haobai Wang and identify this nine-chapter public reading edition. English remains a full working translation.'
        for code in s.select('code[id^="cite-"]'):
            ident=code['id'];chapter=int(ident.rsplit('-',1)[-1]) if ident.startswith('cite-chapter-') else None
            code.string=bib(en,chapter)
        # Keep the old six-chapter receipt as history, without presenting it as the current edition.
        for h in s.find_all('h2'):
            if h.get_text() in ['正式网页版本','Formal web edition']:
                para=h.find_next_sibling('p');para.clear();para.append('Haobai Wang · '+edition+' · '+('前九章公开阅读版。' if not en else 'Nine-chapter public reading edition.'))
        for para in s.find_all('p'):
            val=para.get_text()
            if '当前预览尚未正式发布' in val or 'This preview is unpublished.' in val:
                para.string='本页对应已获作者授权的九章公开阅读版；原稿快照与逐章指纹可在版本页核对。' if not en else 'This page identifies the author-authorized nine-chapter public reading edition; the versions page preserves its source snapshot and chapter fingerprints.'
        text=str(s)
    if p.name=='versions.html':
        marker='<article class="publication-page">'
        card='<section class="panel"><h2>九章公开阅读版 · '+edition+'</h2><p>Haobai Wang · Chapters 1–9 · English working translations await author review.</p><p><a href="/releases/'+edition+'.json">内容指纹 / Content fingerprints</a> · <a href="/releases/'+edition+'.zip">原稿快照 / Source snapshot</a></p></section>'
        text=text.replace(card+card,card)
        if card not in text:text=text.replace(marker,marker+card)
        text=text.replace('本轮没有新正式发布。','本轮发布九章阅读版；旧六章托管记录保留为历史。').replace('No new formal publication occurred in this update.','The nine-chapter reading edition is published in this update; the six-chapter hosting receipt remains historical.')
        text=text.replace('所有下列条目均为公开阅读版','下列条目对应本次九章公开阅读版').replace('All entries below are local previews','The entries below identify this public reading edition')
        commits=iter(content_commits[folder+'/'+name] for name in inputs['chapters'] for folder in ['chapters','chapters-en'])
        text=re.sub(r'<code>uncommitted</code>',lambda m:'<code>'+next(commits)+'</code>',text)
        text=text.replace('本地网页已生成（不代表学术审校通过）','公开阅读页已构建（不代表学术审校通过）').replace('Local pages generated (not academic approval)','Public reading pages built (not academic approval)')
    if p.name=='privacy.html':
        language='en' if 'en' in p.relative_to(dist).parts else 'zh'
        privacy=(source/'publication'/('privacy.'+language+'.html')).read_text('utf-8')
        privacy=privacy.replace('部署启用后，数据存储于本站的','数据存储于本站的').replace('Once enabled in production, events are stored','Events are stored')
        text=re.sub(r'(<article class="publication-page">)[\s\S]*?(</article>)',lambda m:m[1]+privacy+m[2],text,count=1)
    p.write_bytes(text.encode())

meta=dist/'metadata/chapter-versions.json';v=json.loads(meta.read_text('utf-8'));v['reading_edition']=edition
for c in v['chapters']:
    c['edition_status']='AUTHOR_AUTHORIZED_WEB_READING_EDITION'
    for language in c['languages'].values():
        language['last_content_commit']=content_commits[language['path']];language['uncommitted_content']=False
meta.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode())
(dist/'metadata/book-citation.bib').write_bytes((bib()+'\n').encode())
book_meta=dist/'metadata/book.json';book=json.loads(book_meta.read_text('utf-8'));book['edition_status']='AUTHOR_AUTHORIZED_NINE_CHAPTER_WEB_EDITION';book['reading_edition']=edition;book_meta.write_bytes((json.dumps(book,ensure_ascii=False,indent=2)+'\n').encode())
cff=dist/'metadata/CITATION.cff';cff_text=cff.read_text('utf-8')
if '\nversion:' not in cff_text:cff.write_bytes((cff_text+'\nversion: "'+edition+'"\n').encode())

# Repack after decorating; source archive remains restricted to the nine-chapter tree.
sys.path.insert(0,str(source/'tools'))
from publication_policy import checked_public_sources
public_source=checked_public_sources(source)
def zipwrite(path,rows):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for n,b in sorted(rows):z.writestr(n,b)
zipwrite(dist/'downloads/editable-manuscript.zip',public_source)
english=[(n,b) for n,b in public_source if n.startswith(('chapters-en/','advanced-en/','translations/en/','assets/','licenses/','publication/')) or n in {'LICENSE.md','CONTRIBUTING.md','CITATION.cff'}]
english.append(('The-Mathematics-of-Chance.md',(dist/'downloads/manuscript-en.md').read_bytes()))
zipwrite(dist/'downloads/english-manuscript.zip',english)
zipwrite(dist/'downloads/complete-offline.zip',[(p.relative_to(dist).as_posix(),p.read_bytes()) for p in dist.rglob('*') if p.is_file() and p.name!='complete-offline.zip']+[('editable-source/'+n,b) for n,b in public_source])

def scan(data):
    with zipfile.ZipFile(BytesIO(data)) as z:
        for n in z.namelist():
            assert '10-densities-and-kernels' not in n,n
            assert not any(x in n for x in ['chat-messages','conversion-ledger','写作约定与全书编排','.dev.vars','.sqlite']),n
            if n.endswith('.zip'):scan(z.read(n))
for p in (dist/'downloads').glob('*.zip'):scan(p.read_bytes())
runtime={'analytics-dashboard.js','reader-analytics.js','campaign-attribution.js','privacy-controls.js','favicon.svg'}
desired={p.relative_to(dist).as_posix() for p in dist.rglob('*') if p.is_file()}
for p in public.rglob('*'):
    if p.is_file() and p.relative_to(public).as_posix() not in desired|runtime:
        assert p.resolve().is_relative_to(public.resolve());p.unlink()
shutil.copytree(dist,public,dirs_exist_ok=True)
for n in ['lib/dashboard.mjs','lib/reading-analytics.mjs']:shutil.copyfile(ROOT/'analytics-host'/n,checkout/n)
preservation={'edition':edition,'chapters':9,'chapter10_published':False,'source_chapters':protected,'formulas_in_chapters_both_languages':formula_count,'web_pages':{p.relative_to(public).as_posix():sha(p.read_bytes()) for p in public.rglob('*.html')},'mobile_background_timing':'PENDING_PHYSICAL_DEVICE_REVIEW','platform_analytics':'NATIVE_CONSOLE_LINKED_NOT_AUTOMATIC_NUMERIC_SYNC'}
(checkout/'formal-nine-preservation.json').write_bytes((json.dumps(preservation,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'nine_chapter_candidate':'PASS','chapter_source_files':len(protected),'chapter_formulas':formula_count,'chapter10':False,'private_records':False}))
