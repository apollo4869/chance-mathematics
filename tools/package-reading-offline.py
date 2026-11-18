"""Package a reader-only offline site; no private/source repository export."""
from pathlib import Path
import hashlib,json,re,zipfile
R=Path(__file__).resolve().parents[1];SITE=R/'work/reading-acceptance/site';O=R/'reports/full-book-reading-2026-11-07'
SERVER='''from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import argparse
p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8900);a=p.parse_args()
root=Path(__file__).resolve().parent
print(f'Offline reading on this device: http://127.0.0.1:{a.port}/',flush=True)
ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(root))).serve_forever()
'''
GUIDE='''偶然的数学 / Chance Mathematics — 本地离线作者阅读版

八卷58章中英文、卷首卷尾、公开证明、已采用图示、交互与打印页均在本包中。
这是工作稿，不代表独立专家数学终审通过。没有包含私人研究材料或本地源码仓库。

解压后运行：python serve_offline.py
然后访问：http://127.0.0.1:8900/
需要本设备已有Python；服务只绑定本机。绝对路径导航需要这个本地服务器，
不能把双击HTML的file://模式当作全部交互及链接已经通过。阅读正文不需要互联网。

本包不嵌套既有源码ZIP；这些下载链接指向原公开网站，需联网。
离线副本不发送阅读统计。原生PDF分页与真实打印设备仍需验收。
中文入口 /index.html；English /en/index.html。

After extracting, run `python serve_offline.py` and open http://127.0.0.1:8900/ .
This is a localhost reader, not an internet deployment. The complete bilingual
book, public proof pages, illustrations and interactions are included. Existing
source ZIP downloads are not nested; those links require internet access.
No analytics scripts run in this offline copy. Native PDF and physical devices
remain separate review tasks.
'''

def run():
 target=SITE/'downloads/complete-offline.zip';manifest=[];chapter_counts={'zh':0,'en':0};groups=set()
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(SITE.rglob('*')):
   if not p.is_file():continue
   rel=p.relative_to(SITE).as_posix()
   if p.suffix=='.zip' or p.name=='_headers':continue
   assert not any(x.startswith(('.', '__')) or x in {'author-work','reports','node_modules','local-preview'} for x in p.relative_to(SITE).parts),rel
   raw=p.read_bytes()
   if p.suffix=='.html':
    text=raw.decode('utf8')
    text=re.sub(r'<a\b[^>]*href="[^"]*downloads/complete-offline\.zip"[^>]*>.*?</a>','',text,flags=re.S)
    text=re.sub(r'(<a\b[^>]*href=")[^"]*downloads/([^"/]+\.zip)(")',lambda m:m[1]+'https://chancemathematics.org/downloads/'+m[2]+m[3],text)
    text=re.sub(r'<script\b[^>]*src="[^"]*(?:reading-analytics-|campaign-attribution-|reader-analytics\.js|campaign-attribution\.js)[^"]*"[^>]*>\s*</script>','',text)
    raw=text.encode('utf8')
    if re.fullmatch(r'chapters/[^/]+\.html',rel):chapter_counts['zh']+=1
    if re.fullmatch(r'en/chapters/[^/]+\.html',rel):chapter_counts['en']+=1
    if re.fullmatch(r'(?:en/)?chapters/[^/]+\.html',rel):groups.update(re.findall(r'<figure\b[^>]*id="visual-([^"]+)"',text))
   z.writestr(rel,raw);manifest.append(dict(path=rel,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
  for name,text in [('serve_offline.py',SERVER),('OFFLINE-READING.txt',GUIDE)]:
   raw=text.encode('utf8');z.writestr(name,raw);manifest.append(dict(path=name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
  z.writestr('OFFLINE-MANIFEST.json',json.dumps(dict(version='reading-acceptance-20261107',chapters=chapter_counts,files=manifest,analytics='disabled in offline copy only',source_zip_downloads='external links, not nested'),ensure_ascii=False,indent=2))
 assert chapter_counts=={'zh':58,'en':58}
 with zipfile.ZipFile(target) as z:
  assert z.testzip() is None
  for f in manifest:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
 rec=dict(path=str(target),bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest(),chapters=chapter_counts,files=len(manifest),CRC_and_member_hashes=True,requires_local_python_server=True,file_scheme_full_acceptance=False,private_source_repository_exported=False,native_pdf='open',physical_devices='open')
 (O/'offline-package.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n');print(json.dumps(rec,ensure_ascii=False))

if __name__=='__main__':run()
