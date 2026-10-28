"""Attach analytics to the exact deployed six-chapter artifact, never the nine-chapter preview.

Run against a separate Sites source checkout. The original archive and manuscripts stay immutable.
"""
from pathlib import Path
from io import BytesIO
import argparse,hashlib,html,json,re,shutil,subprocess,sys,tarfile,zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
parser=argparse.ArgumentParser();parser.add_argument('--checkout',required=True);args=parser.parse_args()
dest=Path(args.checkout).resolve();assert dest!=ROOT and (dest/'.git').exists()
release=json.loads((ROOT/'publication/releases/formal-six-web-v4.json').read_text('utf-8'))
archive=ROOT.parent/'publication-artifacts/chance-mathematics-phone-review-2026-10-26.tar.gz'
sha=lambda b:hashlib.sha256(b).hexdigest()
original={}
source_checks=[]
with tarfile.open(archive) as tar:
    for member in tar:
        if member.isfile() and member.name.startswith('dist/'):
            name=member.name[5:];assert not Path(name).is_absolute() and '..' not in Path(name).parts
            data=tar.extractfile(member).read()
            if name=='.openai/hosting.json':
                assert json.loads(data)['project_id']=='appgprj_6add5ada774c819199489ea9858f15c8'
            else:
                source=subprocess.check_output(['git','show',release['source_commit']+':dist/'+name],cwd=ROOT)
                if source!=data:
                    assert name=='assets/diagrams/chapter-4-1.svg' and source.replace(b'\r\n',b'\n')==data.replace(b'\r\n',b'\n'),name
                    source_checks.append({'file':name,'difference':'CRLF_ONLY','source_sha256':sha(source),'input_sha256':sha(data)})
            original[name]=data

def section_span(text,key):
    match=re.search(r'<section\b[^>]*\bid="'+re.escape(key)+r'"[^>]*>',text);assert match,key
    depth=0
    for tag in re.finditer(r'</?section\b[^>]*>',text[match.start():]):
        depth+=-1 if tag[0].startswith('</') else 1
        if depth==0:return match.start(),match.start()+tag.end()
    raise AssertionError(key)
def protected(text,key):
    a,b=section_span(text,key);return text[a:b]

public=dest/'public';public.mkdir(exist_ok=True)
# Copy only authored server-template sources, not development secrets/state or generated nine-chapter pages.
for base,dirs,files in __import__('os').walk(ROOT/'analytics-host'):
    dirs[:]=[d for d in dirs if d not in {'node_modules','.git','.wrangler','.sites-runtime','.vinext','.next','dist','examples'}]
    for name in files:
        p=Path(base)/name;relative=p.relative_to(ROOT/'analytics-host')
        if name.startswith(('.dev.vars','.env')) and name!='.env.example':continue
        if name.endswith(('.tsbuildinfo','.log')):continue
        if relative.parts[0]=='public' and name not in {'reader-analytics.js','campaign-attribution.js','privacy-controls.js','analytics-dashboard.js','favicon.svg'}:continue
        q=dest/relative;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
# In this deployment checkout public/ is the frozen publication source, not an ignored preview copy.
ignore=(dest/'.gitignore').read_text('utf-8').split('# Generated, byte-preserved book copy')[0]
(dest/'.gitignore').write_bytes((ignore+'\n/qa/\n').encode())

pages={n:b.decode('utf-8') for n,b in original.items() if n.endswith('.html')}
active=set()
for page,text in pages.items():
    for value in re.findall(r'(?:href|src)="([^"]+)"',text):
        clean=value.split('?')[0].split('#')[0]
        if clean.endswith(('.js','.css')):active.add(Path(clean).name)
for name,data in original.items():
    if name.startswith(('downloads/','.openai/')) or name.endswith('.html'):continue
    if name=='assets/formulas/rules.json':continue
    if re.fullmatch(r'assets/(?:reader|search|reading-mode|app|experiments)-[a-f0-9]{12}\.(?:js|css)',name) and Path(name).name not in active:continue
    q=public/name;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data)

public_rules=[]
for block in (ROOT/'publication/writing-principles.zh.md').read_text('utf-8').split('\n\n'):
    block=block.strip()
    if not block:continue
    if block.startswith('# '):public_rules.append('<h1 id="rules-h1">'+html.escape(block[2:])+'</h1>')
    elif block.startswith('## '):public_rules.append('<h2>'+html.escape(block[3:])+'</h2>')
    else:public_rules.append('<p>'+html.escape(block).replace('\n',' ')+'</p>')
public_rules='<section class="book-section" id="rules">'+''.join(public_rules)+'</section>'

def privacy_nav(text):
    def replace(match):
        old=match[0];link=re.search(r'<a\b[^>]*href="([^"]*writing-rules\.html)"[^>]*>',old)
        if not link:return old
        return '<details><summary><a href="'+link[1]+'">公开写作原则</a></summary></details>'
    return re.sub(r'<details\b[^>]*><summary>[\s\S]*?</summary>[\s\S]*?</details>',replace,text)

rows=[]
for name,text in pages.items():
    original_text=text;text=privacy_nav(text)
    prefix='../' if '/' in name else ''
    if name=='writing-rules.html':
        a,b=section_span(text,'rules');text=text[:a]+public_rules+text[b:]
    # All instrumentation and links are outside each protected mathematics section.
    text=text.replace('</footer>','<p><a href="'+prefix+'privacy.html">阅读统计与隐私</a></p></footer>')
    text=text.replace('</body>','<script defer src="'+prefix+'campaign-attribution.js"></script></body>')
    if name.startswith('chapters/'):
        text=text.replace('</body>','<script defer src="'+prefix+'reader-analytics.js"></script></body>')
    for key in re.findall(r'<section\b[^>]*\bid="((?:chapter-\d+|advanced-[^\"]+|supplement|references))"',original_text):
        before=protected(original_text,key);after=protected(text,key);assert before==after,(name,key)
        rows.append({'page':name,'section':key,'sha256':sha(before.encode()),'byte_identical':True})
    q=public/name;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())

# Strip private author-note records from every retained search bundle.
for p in (public/'assets').glob('search-*.js'):
    text=p.read_text('utf-8');start=text.index('[');entries,end=json.JSONDecoder().raw_decode(text[start:])
    entries=[r for r in entries if r['section']!='rules']+[{'id':'rules-h1','text':'公开写作原则：历史问题、完整推导与独立审校','section':'rules'}]
    data=(text[:start]+json.dumps(entries,ensure_ascii=False)+text[start+end:]).encode()
    fresh=p.with_name('search-'+sha(data)[:12]+'.js');fresh.write_bytes(data)
    for page in public.rglob('*.html'):
        content=page.read_bytes().decode('utf-8')
        page.write_bytes(content.replace(p.name,fresh.name).encode())
    if fresh!=p:p.unlink()

privacy=(ROOT/'publication/privacy.zh.html').read_text('utf-8').replace('部署启用后，数据存储于本站的','数据存储于本站的')
template=(public/'index.html').read_text('utf-8')
privacy_page=re.sub(r'<main>[\s\S]*?</main>','<main><article class="publication-page">'+privacy+'</article><footer><a href="index.html">返回全书目录</a> · <a href="admin/analytics">作者后台</a></footer></main>',template,count=1)
privacy_page=re.sub(r'<title>[\s\S]*?</title>','<title>阅读统计与隐私 · 偶然的数学</title>',privacy_page,count=1)
privacy_page=privacy_page.replace('</body>','<script defer src="privacy-controls.js"></script></body>')
(public/'privacy.html').write_bytes(privacy_page.encode())

downloads=public/'downloads';downloads.mkdir(exist_ok=True)
with zipfile.ZipFile(ROOT/'publication/releases/formal-six-web-v4.zip') as z:manuscript={n:z.read(n) for n in release['files']}
for n,data in manuscript.items():assert sha(data)==release['files'][n],n
old_fourth=original['downloads/04-brownian-before-restructure.md'];manuscript['archives/04-brownian-before-restructure.md']=old_fourth
manuscript['writing-principles.md']=(ROOT/'publication/writing-principles.zh.md').read_bytes()
manuscript['LICENSE.md']=(ROOT/'LICENSE.md').read_bytes()
manuscript['PRIVACY.html']=privacy.encode()
for name,data in original.items():
    if name.startswith(('assets/images/','assets/diagrams/','assets/charts/')):manuscript[name]=data
def make_zip(path,entries):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for name,data in sorted(entries.items()):z.writestr(name,data)
make_zip(downloads/'editable-manuscript.zip',manuscript)
(downloads/'04-brownian-before-restructure.md').write_bytes(old_fourth)
combined=b'\n\n'.join([manuscript['writing-principles.md']]+[manuscript[n] for n in release['files']])
(downloads/'manuscript.md').write_bytes(combined)
offline={p.relative_to(public).as_posix():p.read_bytes() for p in public.rglob('*') if p.is_file() and p.name!='complete-offline.zip'}
# The offline copy links to the hosted protected dashboard; it never contains analytics data.
offline['privacy.html']=offline['privacy.html'].replace(b'href="admin/analytics"',b'href="https://chance-mathematics-six-chapters.goldenmath7.chatgpt.site/admin/analytics"')
make_zip(downloads/'complete-offline.zip',offline)

# Verify body preservation, assets, privacy and absence of unpublished chapter routes.
assert len(list((public/'chapters').glob('*.html')))==6
assert not (public/'en').exists()
for p in public.rglob('*'):
    if not p.is_file():continue
    name=p.relative_to(public).as_posix()
    assert not re.search(r'(?:^|/)chapters/0[789]-',name),name
    if name.startswith(('assets/images/','assets/diagrams/','assets/charts/')):assert p.read_bytes()==original[name],name
    if p.suffix in {'.html','.js'}:
        text=p.read_text('utf-8')
        assert not re.search(r'(?:href|src)="[^\"]*chapters/0[789]-',text),name
        assert '读者直接提出的要求（原话）' not in text,name
def scan_zip(blob):
    with zipfile.ZipFile(BytesIO(blob)) as z:
        for name in z.namelist():
            assert not any(v in name for v in ['chat-messages','conversion-ledger','写作约定与全书编排','.git/','.env','.sqlite']),name
            data=z.read(name)
            if name.endswith('.zip'):scan_zip(data)
for p in downloads.glob('*.zip'):scan_zip(p.read_bytes())
asset_hashes={n:sha(data) for n,data in original.items() if n.startswith(('assets/images/','assets/diagrams/','assets/charts/'))}
manifest={'source_formal_release':release['release_id'],'source_commit':release['source_commit'],'input_local_archive_sha256':sha(archive.read_bytes()),'hosting_original_artifact_hash':release['original_deployment_archive_sha256'],'archive_note':'Local archive container differs from the server receipt. Every payload file is checked against the verified deployed Git source; the sole SVG difference is CRLF-only. No claim that the two archive hashes match.','source_payload_checks':source_checks,'chapter_count':6,'languages':['zh-CN'],'protected_sections':rows,'static_asset_hashes':asset_hashes,'body_byte_identical':True,'private_notes_in_public_downloads':False,'unpublished_chapters_deployed':False}
(dest/'formal-analytics-preservation.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'formal_six_candidate':'PASS','protected_sections':len(rows),'chapter_count':6,'unpublished_chapters':False,'private_notes_exported':False}))
