"""Read-only isolated preview. Bind localhost only; no publishing endpoint."""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import mimetypes,re
R=Path(__file__).resolve().parents[1];O=R/'reports/early-explanations-batch2-2026-10-31';OLD=R/'reports/volumes1-5-visual-review-2026-10-31'
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):self.respond(True)
 def do_HEAD(self):self.respond(False)
 def respond(self,body):
  path=unquote(urlsplit(self.path).path);roots=[('/assets/',R/'assets'),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/old-shots/',OLD/'screenshots'),('/previous/',OLD/'preview'),('/references/',OLD/'references')]
  base,rel=O/'preview',path.lstrip('/') or 'index.html'
  for prefix,root in roots:
   if path.startswith(prefix):base,rel=root,path[len(prefix):] or 'index.html';break
  target=(base/rel).resolve()
  if not target.is_relative_to(base.resolve()) or not target.is_file():self.send_error(404);return
  data=target.read_bytes()
  if path.startswith('/previous/') and target.suffix=='.html':
   old=data.decode('utf-8').replace('"/shots/','"/old-shots/')
   old=re.sub(r'((?:href|src)=")/(?!assets/|book/|references/|old-shots/|https?)([^"#]*)',r'\1/previous/\2',old);data=old.encode('utf-8')
  typ=mimetypes.guess_type(str(target))[0] or 'application/octet-stream';self.send_response(200);self.send_header('Content-Type',typ+(';charset=utf-8' if typ.startswith('text/') else ''));self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.send_header('X-Robots-Tag','noindex,nofollow');self.end_headers()
  if body:self.wfile.write(data)
 def log_message(self,*args):pass
if __name__=='__main__':
 print('LOCAL ONLY http://127.0.0.1:8861/',flush=True);ThreadingHTTPServer(('127.0.0.1',8861),Handler).serve_forever()
