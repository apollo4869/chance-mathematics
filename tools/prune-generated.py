"""Remove only stale, reproducible hashed bundles; old search indexes may contain private notes."""
from pathlib import Path
import json,re
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1];dist=ROOT/'dist';assets=(dist/'assets').resolve()
active=set()
for page in dist.rglob('*.html'):
    for value in re.findall(r'\b(?:href|src)="([^"]+)"',page.read_text('utf-8')):
        u=urlsplit(value)
        if u.scheme or u.netloc:continue
        active.add((page.parent/unquote(u.path)).resolve())
removed=[]
for p in assets.iterdir():
    if p.is_file() and re.fullmatch(r'(?:search|reader|reading-mode|reading-analytics|campaign-attribution|privacy-controls|experiments|app|home-ui|publication)-[0-9a-f]{12}\.(?:js|css)',p.name) and p.resolve() not in active:
        assert p.resolve().parent==assets
        p.unlink();removed.append(p.name)
current={f['section'] for f in json.loads((ROOT/'build/formulas.json').read_text('utf-8'))}
for p in (assets/'formulas').glob('*.json'):
    if p.stem not in current:
        assert p.resolve().parent==assets/'formulas'
        p.unlink();removed.append('formulas/'+p.name)
print(json.dumps({'stale_generated_bundles_removed':len(removed),'manuscripts_modified':False}))
