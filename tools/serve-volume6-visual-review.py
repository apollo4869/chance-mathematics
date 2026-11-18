from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit,unquote
R=Path(__file__).resolve().parents[1];P=R/'assets/visuals/explanatory-volume6-v1/local-preview'
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  p=unquote(urlsplit(path).path)
  if p.startswith('/assets/'):base=R/'assets';rel=p[8:]
  elif p.startswith('/book/'):base=R/'dist';rel=p[6:]
  else:base=P;rel=p.lstrip('/') or 'index.html'
  target=(base/rel).resolve()
  return str(target) if target.is_relative_to(base.resolve()) else str(base/'__not_allowed__')
 def end_headers(self):self.send_header('Cache-Control','no-store');self.send_header('X-Robots-Tag','noindex,nofollow');super().end_headers()
 def log_message(self,*a):pass
if __name__=='__main__':ThreadingHTTPServer(('127.0.0.1',8867),Handler).serve_forever()
