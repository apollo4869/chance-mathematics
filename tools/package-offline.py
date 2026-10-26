from pathlib import Path
import zipfile,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1];dist=ROOT/'dist';downloads=dist/'downloads';downloads.mkdir(exist_ok=True)
(downloads/'manuscript.md').write_bytes((ROOT/'build/combined-manuscript.md').read_bytes())
if (ROOT/'build/combined-manuscript-en.md').exists():
    (downloads/'manuscript-en.md').write_bytes((ROOT/'build/combined-manuscript-en.md').read_bytes())
def write_zip(target,files):
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for name,data in sorted(files):
            info=zipfile.ZipInfo(name,date_time=(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,data)
source=[]
for folder in ['chapters','advanced','chapters-en','advanced-en','translations','archives','assets','provenance','docs']:
    source.extend((p.relative_to(ROOT).as_posix(),p.read_bytes()) for p in (ROOT/folder).rglob('*') if p.is_file())
source.extend((name,(ROOT/name).read_bytes()) for name in ['写作约定与全书编排.md','校订与证明补充.md','引用与配图来源.md','延伸阅读与证明路线.md','baseline-manuscript.json','experiments.js','app.js'])
(downloads/'04-brownian-before-restructure.md').write_bytes((ROOT/'archives/before-brownian-restructure/04-brownian.md').read_bytes())
write_zip(downloads/'editable-manuscript.zip',source)
if (downloads/'manuscript-en.md').exists():
    english_source=[(n,b) for n,b in source if n.startswith(('chapters-en/','advanced-en/','translations/en/','assets/'))]
    english_source.append(('The-Mathematics-of-Chance.md',(downloads/'manuscript-en.md').read_bytes()))
    write_zip(downloads/'english-manuscript.zip',english_source)
files=[]
for p in dist.rglob('*'):
    if not p.is_file() or p.name=='complete-offline.zip':continue
    data=p.read_bytes()
    if p.suffix=='.html':
        # Only remove the package's self-download control, never chapter prose.
        data=re.sub(r'<a\b[^>]*href="[^"]*downloads/complete-offline\.zip"[^>]*>[\s\S]*?</a>','',data.decode('utf-8')).encode('utf-8')
    files.append((p.relative_to(dist).as_posix(),data))
files.extend(('editable-source/'+n,b) for n,b in source)
write_zip(downloads/'complete-offline.zip',files)
print(json.dumps({'offline_files':len(files),'source_files':len(source),'source_kind':'reorganized long working draft; original-chat equivalence unverified'}))
