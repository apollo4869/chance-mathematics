"""Read-only localhost delivery; deliberately no deployment endpoint."""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import mimetypes
R=Path(__file__).resolve().parents[1];O=R/'reports/volumes1-5-visual-review-2026-10-31'
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):self.respond(True)
 def do_HEAD(self):self.respond(False)
 def respond(self,body):
  path=unquote(urlsplit(self.path).path)
  roots=[('/assets/visuals/explanatory-early-v1/',R/'assets/visuals/explanatory-early-v1'),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/references/',O/'references')]
  base,rel=O/'preview',path.lstrip('/') or 'index.html'
  for prefix,root in roots:
   if path.startswith(prefix):base,rel=root,path[len(prefix):];break
  p=(base/rel).resolve()
  if not p.is_relative_to(base.resolve()) or not p.is_file():self.send_error(404);return
  data=p.read_bytes();typ=mimetypes.guess_type(str(p))[0] or 'application/octet-stream';self.send_response(200);self.send_header('Content-Type',typ+(';charset=utf-8' if typ.startswith('text/') else ''));self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.send_header('X-Robots-Tag','noindex,nofollow');self.end_headers()
  if body:self.wfile.write(data)
 def log_message(self,*a):pass
if __name__=='__main__':
 print('LOCAL ONLY http://127.0.0.1:8860/',flush=True);ThreadingHTTPServer(('127.0.0.1',8860),Handler).serve_forever()
