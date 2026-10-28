"""Stage an explicitly authorized reading edition without changing book bodies.

Uses the already verified local build. Runtime identity/D1 configuration stays in
the existing Sites checkout; private author records are excluded by the shared
public-source policy. Run again only before saving the immutable hosting archive.
"""
from pathlib import Path
from io import BytesIO
import argparse, hashlib, json, re, shutil, subprocess, sys, zipfile
ROOT=Path(sys.argv[sys.argv.index('--source-root')+1]).resolve()
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
from publication_policy import checked_public_sources
ap=argparse.ArgumentParser();ap.add_argument('--checkout',required=True);ap.add_argument('--previous-source',required=True);ap.add_argument('--source-root',required=True);ap.add_argument('--content-commit',required=True);a=ap.parse_args()
host=Path(a.checkout).resolve();public=host/'public';dist=ROOT/'dist'
assert host!=ROOT and (host/'.git').exists()
project='appgprj_6add5ada774c819199489ea9858f15c8'
assert json.loads((host/'.openai/hosting.json').read_text())['project_id']==project
assert json.loads((host/'.openai/hosting.json').read_text())['d1']=='DB'
previous_releases={n:subprocess.check_output(['git','show',a.previous_source+':'+n],cwd=host) for n in subprocess.check_output(['git','ls-tree','-r','--name-only',a.previous_source,'--','public/releases'],cwd=host).decode().splitlines()}
sha=lambda b:hashlib.sha256(b).hexdigest()
commit=a.content_commit
inputs=json.loads((ROOT/'provenance/build-inputs.json').read_text('utf8'));count=len(inputs['chapters'])
assert count==15
edition='fifteen-chapters-'+commit[:7]
origin='https://chance-mathematics-six-chapters.goldenmath7.chatgpt.site/'
sources=dict(checked_public_sources(ROOT))
for folder in ['chapters','chapters-en']:
    for n in inputs['chapters']:assert sources[folder+'/'+n]==(ROOT/folder/n).read_bytes()
# The source snapshot is independent of the deployment archive/hosting receipt.
snapshot_names=[n for n in sources if n.startswith(('chapters/','chapters-en/','advanced/','advanced-en/','foundations/','foundations-en/','volumes/','volumes-en/','assets/','translations/')) or n in {'校订与证明补充.md','引用与配图来源.md','延伸阅读与证明路线.md'}]
hashes={n:sha(sources[n]) for n in snapshot_names}
runtime={'analytics-dashboard.js','reader-analytics.js','campaign-attribution.js','privacy-controls.js','favicon.svg'}
desired={p.relative_to(dist).as_posix() for p in dist.rglob('*') if p.is_file()}
for p in public.rglob('*'):
    if p.is_file() and p.relative_to(public).as_posix() not in desired|runtime:
        assert p.resolve().is_relative_to(public);p.unlink()
shutil.copytree(dist,public,dirs_exist_ok=True)
for n,b in previous_releases.items():
    p=host/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
for n in ['lib/reading-analytics.mjs','lib/dashboard.mjs','public/reader-analytics.js','tests/analytics.test.mjs']:
    shutil.copyfile(ROOT/'analytics-host'/n,host/n)

def zipwrite(path,rows):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for n,b in sorted(rows):
            info=zipfile.ZipInfo(n,date_time=(2026,10,27,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,b)
snap=public/'releases'/(edition+'.zip')
zipwrite(snap,[(n,sources[n]) for n in snapshot_names]+[('contents-sha256.json',json.dumps(hashes,ensure_ascii=False,indent=2).encode())])
record={'release_id':edition,'kind':'AUTHOR_AUTHORIZED_WEB_READING_EDITION','author':'Haobai Wang','chapter_count':count,'languages':['zh-CN','en-working-translation'],'content_source_commit':commit,'archive_file':snap.name,'archive_sha256':sha(snap.read_bytes()),'files':hashes,'academic_final_review':False,'snapshot_scope':'Reader source: complete mathematical bodies; archival editorial wrappers separately disclosed in editable source.'}
(public/'releases'/(edition+'.json')).write_bytes((json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode())

def bib(en=False,chapter=None):
    title='The Mathematics of Chance: The History, Ideas and Mathematical Structures of Probability' if en else '偶然的数学：概率论的历史、思想与数学结构'
    url=origin+('en/' if en else '');note=edition+'; academic final review not implied; English is a working translation'
    if chapter:
        name=inputs['chapters'][chapter-1];folder='chapters-en' if en else 'chapters'
        title=next(l.lstrip('# ') for l in sources[folder+'/'+name].decode().splitlines() if l.startswith('# Chapter ') or re.match(r'^# 第.+章[：:]',l))
        url+='chapters/'+Path(name).with_suffix('.html').name;note+='; SHA-256 '+hashes[folder+'/'+name]
    return '@misc{wang2026chance'+('_ch'+str(chapter) if chapter else '')+('_en' if en else '')+',\n  author = {Wang, Haobai},\n  title = {{'+title+'}},\n  year = {2026},\n  url = {'+url+'},\n  note = {'+note+'}\n}'

body_pattern=re.compile(r'<section\b[^>]*\bid="(?:chapter-\d+|advanced-[^"]+|supplement|references)"[^>]*>')
def fragments(text):
    out=[]
    for m in body_pattern.finditer(text):
        depth=0
        for t in re.finditer(r'</?section\b[^>]*>',text[m.start():]):
            depth+=-1 if t[0].startswith('</') else 1
            if depth==0:out.append(text[m.start():m.start()+t.end()]);break
    return out

for p in public.rglob('*.html'):
    text=p.read_bytes().decode('utf8');before=fragments(text);frozen=[]
    for fragment in before:
        token='FROZENBOOKBODY'+str(len(frozen))+'END';text=text.replace(fragment,token,1);frozen.append((token,fragment))
    text=text.replace('当前为本地预览','十五章公开阅读版').replace('本地预览','公开阅读版').replace('Local preview','Public reading edition').replace('local preview','public reading edition')
    text=text.replace('not a formal release or an independent proof of authorship','not academic final approval or an independent proof of authorship').replace('不表示正式发布或独立的作者身份证明','不表示学术终审或独立的作者身份证明')
    en='en' in p.relative_to(public).parts
    if p.name=='citation.html':
        s=BeautifulSoup(text,'html.parser')
        lead=s.select_one('.pub-lead')
        if lead:lead.string=('Credit Haobai Wang and identify this fifteen-chapter public reading edition. English remains a working translation.' if en else '请引用 Haobai Wang，并注明十五章公开阅读版及内容指纹；英文仍为完整翻译工作稿。')
        for code in s.select('code[id^="cite-"]'):
            chapter=int(code['id'].rsplit('-',1)[-1]) if code['id'].startswith('cite-chapter-') else None;code.string=bib(en,chapter)
        for para in s.find_all('p'):
            v=para.get_text()
            if '当前预览尚未正式发布' in v or 'This preview is unpublished.' in v:para.string=('Author-authorized fifteen-chapter public reading edition; source fingerprints are on the versions page.' if en else '本页对应已获作者授权的十五章公开阅读版；原稿快照与逐章指纹见版本页。')
        text=str(s)
    if p.name=='versions.html':
        card='<section class="panel"><h2>'+('Fifteen-chapter public reading edition' if en else '十五章公开阅读版')+' · '+edition+'</h2><p>Haobai Wang · Chapters 1–15 · English working translations.</p><p><a href="/releases/'+edition+'.json">内容指纹 / Content fingerprints</a> · <a href="/releases/'+edition+'.zip">原稿快照 / Source snapshot</a></p></section>'
        text=text.replace('<article class="publication-page">','<article class="publication-page">'+card,1)
        text=text.replace('所有下列条目均为公开阅读版','下列条目对应本次十五章公开阅读版').replace('All entries below are public reading editions','The entries below identify this fifteen-chapter public reading edition')
        text=text.replace('本轮没有新正式发布。','本轮发布十五章公开阅读版；既有托管版本保留供回溯。').replace('No new formal publication occurred in this update.','This update publishes the fifteen-chapter reading edition; earlier hosting versions remain available for rollback.')
    if p.name=='privacy.html':
        text=text.replace('部署启用后，数据存储于本站的','数据存储于本站的').replace('Once enabled in production, events are stored','Events are stored')
    for token,fragment in frozen:text=text.replace(token,fragment)
    assert fragments(text)==before,('Book body changed',p)
    p.write_bytes(text.encode())

meta=public/'metadata/chapter-versions.json';v=json.loads(meta.read_text('utf8'));v['reading_edition']=edition
for c in v['chapters']:c['edition_status']='AUTHOR_AUTHORIZED_WEB_READING_EDITION';c['engineering_build']='PUBLIC_PAGES_BUILT'
meta.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode())
bookmeta=public/'metadata/book.json';book=json.loads(bookmeta.read_text('utf8'));book['edition_status']='AUTHOR_AUTHORIZED_TWELVE_CHAPTER_WEB_EDITION';book['reading_edition']=edition;bookmeta.write_bytes((json.dumps(book,ensure_ascii=False,indent=2)+'\n').encode())
(public/'metadata/book-citation.bib').write_bytes((bib()+'\n').encode())
cff=public/'metadata/CITATION.cff';c=cff.read_text('utf8');c=re.sub(r'\nversion:.*','',c);cff.write_bytes((c.rstrip()+'\nversion: "'+edition+'"\n').encode())
# Store only the allowlisted public source in a separate subtree, not private Git history.
source_root=host/'book-source-fifteen';source_root.mkdir(exist_ok=True)
for n,b in sources.items():
    p=source_root/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
zipwrite(public/'downloads/editable-manuscript.zip',list(sources.items()))
english=[(n,b) for n,b in sources.items() if n.startswith(('chapters-en/','advanced-en/','foundations-en/','translations/en/','assets/','licenses/','publication/')) or n in {'LICENSE.md','CONTRIBUTING.md','CITATION.cff'}]
english.append(('The-Mathematics-of-Chance.md',(public/'downloads/manuscript-en.md').read_bytes()))
zipwrite(public/'downloads/english-manuscript.zip',english)
offline=[]
for p in public.rglob('*'):
    if not p.is_file() or p.name in runtime or p.suffix=='.zip':continue
    b=p.read_bytes()
    if p.suffix=='.html':
        text=re.sub(r'<a\b[^>]*href="[^"]*downloads/complete-offline\.zip"[^>]*>[\s\S]*?</a>','',b.decode())
        # The full extracted manuscript is included once. Historical ZIP links
        # remain explicit online archive links rather than duplicate payloads.
        import posixpath
        here=p.relative_to(public).parent.as_posix()
        def offline_zip(m):
            target=posixpath.normpath(posixpath.join(here,m[1])) if not m[1].startswith('/') else m[1].lstrip('/')
            if target.startswith('downloads/'):
                return 'href="'+posixpath.relpath('editable-source/README.md',here)+'"'
            return 'href="'+origin+target+'"'
        text=re.sub(r'href="([^"?#]+\.zip)"',offline_zip,text)
        b=text.encode()
    offline.append((p.relative_to(public).as_posix(),b))
zipwrite(public/'downloads/complete-offline.zip',offline+[('editable-source/'+n,b) for n,b in sources.items()])

def scan(data):
    with zipfile.ZipFile(BytesIO(data)) as z:
        for n in z.namelist():
            assert not any(t in n for t in ['chat-messages','conversion-ledger','写作约定与全书编排','.dev.vars','.sqlite','.git/','BOOK_MASTER_OUTLINE','CHAPTER_DEPENDENCIES','THEOREM_COVERAGE','CHAPTER_STATUS','planning/']),n
            assert not n.startswith('provenance/authorized-'),n
            assert not n.startswith('archives/') or n=='archives/before-brownian-restructure/04-brownian.md' or n=='editable-source/archives/before-brownian-restructure/04-brownian.md',n
            if n.endswith('.zip'):scan(z.read(n))
for p in (public/'downloads').glob('*.zip'):scan(p.read_bytes())
preservation={'edition':edition,'content_source_commit':commit,'chapters':count,'languages':2,'source_chapters':{n:hashes[n] for n in hashes if n.startswith(('chapters/','chapters-en/'))},'web_pages':{p.relative_to(public).as_posix():sha(p.read_bytes()) for p in public.rglob('*.html')},'body_fragments_unchanged':True,'private_records_exported':False,'mobile_background_timing':'PENDING_PHYSICAL_DEVICE_REVIEW','platform_analytics':'NATIVE_CONSOLE_LINKED_NOT_AUTOMATIC_NUMERIC_SYNC'}
(host/'formal-fifteen-preservation.json').write_bytes((json.dumps(preservation,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'fifteen_chapter_candidate':'PASS','edition':edition,'source_files':len(sources),'chapter_sources':len(preservation['source_chapters']),'book_bodies':'BYTE_EXACT','private_records':False}))
