"""Read-only local server, with no publishing endpoint."""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import mimetypes,sys
R=Path(__file__).resolve().parents[1];O=R/'reports/early-explanations-batch3-2026-11-04';OLD=R/'reports/early-explanations-batch2-2026-10-31'
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):self.respond(True)
 def do_HEAD(self):self.respond(False)
 def respond(self,body):
  p=unquote(urlsplit(self.path).path);base,rel=O/'preview',p.lstrip('/') or 'index.html'
  for prefix,root in [('/assets/',R/'assets'),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/previous-shots/',OLD/'screenshots')]:
   if p.startswith(prefix):base,rel=root,p[len(prefix):];break
  target=(base/rel).resolve()
  if not target.is_relative_to(base.resolve()) or not target.is_file():self.send_error(404);return
  data=target.read_bytes();typ=mimetypes.guess_type(str(target))[0] or 'application/octet-stream';self.send_response(200);self.send_header('Content-Type',typ+(';charset=utf-8' if typ.startswith('text/') else ''));self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.end_headers()
  if body:self.wfile.write(data)
 def log_message(self,*args):pass
if __name__=='__main__':
 port=int(sys.argv[1]) if len(sys.argv)>1 else 8862
 print(f'LOCAL ONLY http://127.0.0.1:{port}/',flush=True);ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
