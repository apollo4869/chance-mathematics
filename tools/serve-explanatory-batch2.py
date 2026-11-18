"""Read-only localhost review server; no upload, mutation or deployment endpoint."""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import unquote,urlsplit
import mimetypes
ROOT=Path(__file__).resolve().parents[1];O=ROOT/'reports/volume5-illustrations-batch2-2026-10-31'
class Handler(BaseHTTPRequestHandler):
 def do_HEAD(self):self.send_file(False)
 def do_GET(self):self.send_file(True)
 def send_file(self,body):
  path=unquote(urlsplit(self.path).path)
  if path.startswith('/assets/visuals/explanatory-v2/'):root=ROOT/'assets/visuals/explanatory-v2';part=path[len('/assets/visuals/explanatory-v2/'):]
  elif path.startswith('/book/'):root=ROOT/'dist';part=path[6:]
  elif path.startswith('/assets/visuals/explanatory-v1/'):root=ROOT/'assets/visuals/explanatory-v1';part=path[len('/assets/visuals/explanatory-v1/'):]
  elif path.startswith('/shots/'):root=O/'screenshots';part=path[7:]
  elif path.startswith('/r3-shots/'):root=O/'references/round3/screenshots';part=path[10:]
  else:root=O/'preview';part=path.lstrip('/') or 'index.html'
  p=(root/part).resolve()
  if not p.is_relative_to(root.resolve()) or not p.is_file():self.send_error(404);return
  raw=p.read_bytes();typ=mimetypes.guess_type(str(p))[0] or 'application/octet-stream';self.send_response(200);self.send_header('Content-Type',typ+(';charset=utf-8' if typ.startswith('text/') else ''));self.send_header('Content-Length',len(raw));self.send_header('Cache-Control','no-store');self.send_header('X-Robots-Tag','noindex,nofollow');self.end_headers()
  if body:self.wfile.write(raw)
 def log_message(self,*args):pass
if __name__=='__main__':
 print('VOLUME V BATCH 2 · LOCAL ONLY http://127.0.0.1:8859/',flush=True);ThreadingHTTPServer(('127.0.0.1',8859),Handler).serve_forever()
