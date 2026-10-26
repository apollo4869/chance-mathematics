from pathlib import Path
from urllib.parse import urlsplit,unquote
import zipfile,json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'probability-project-audit-2026-10-25/runtime/python'))
from bs4 import BeautifulSoup
import posixpath
failures=[];links=0
with zipfile.ZipFile(ROOT/'dist/downloads/complete-offline.zip') as z:
    names=set(z.namelist())
    for name in names:
        if not name.endswith('.html'):continue
        soup=BeautifulSoup(z.read(name).decode('utf-8'),'html.parser')
        for n in soup.select('a[href],script[src],link[href],img[src]'):
            value=n.get('href',n.get('src'));u=urlsplit(value)
            if u.scheme or u.netloc or not u.path:continue
            links+=1;target=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(u.path)))
            if target not in names:failures.append({'page':name,'missing':value})
    source=json.loads((ROOT/'baseline-manuscript.json').read_text(encoding='utf-8'))
    for p in source['files']:
        target='editable-source/'+p
        if target not in names or z.read(target)!=(ROOT/p).read_bytes():failures.append({'source_file_missing_or_changed':p})
    for p in (ROOT/'dist/chapters').glob('*.html'):
        name='chapters/'+p.name
        if z.read(name)!=p.read_bytes():failures.append({'chapter_output_changed_in_zip':name})
result={'status':'FAIL' if failures else 'PASS','offline_local_references':links,'chapter_html_byte_identical':not any('chapter_output_changed_in_zip' in f for f in failures),'source_files_checked':len(source['files']),'failures':failures,'scope':'ZIP content, local paths and byte preservation; browser file-protocol behavior checked separately.'}
(ROOT/'reports/offline-package.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False));raise SystemExit(bool(failures))
