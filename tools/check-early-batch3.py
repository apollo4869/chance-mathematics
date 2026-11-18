"""Scoped exact-model, inherited preservation and real-browser evidence checks."""
from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];O=R/'reports/early-explanations-batch3-2026-11-04';P=O/'preview';A=R/'assets/visuals/explanatory-early-v3'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'))
allowed={'tools/explanatory_illustrations/early_batch2.py'}|{f'assets/visuals/explanatory-early-v2/E14-{lg}-{n}-{kind}.svg' for lg in ['zh','en'] for n in [4,16,64] for kind in ['rare','small']}|{f'assets/visuals/explanatory-early-v2/{code}.{lg}.svg' for code in ['E14','E30'] for lg in ['zh','en']}
changed={p for p,v in base.items() if not (R/p).is_file() or sha(R/p)!=v}
assert changed==allowed,dict(unexpected=sorted(changed-allowed),expected_but_unchanged=sorted(allowed-changed))
(O/'authorized-local-corrections.json').write_text(json.dumps(dict(source_commit='c7d426b52338eb77b7a024fe0da8d1f4c656eb1d',reason='Only author-requested E14 index and E30 predictability clarifications',files=[dict(path=p,before=base[p],after=sha(R/p)) for p in sorted(allowed)]),indent=2),encoding='utf-8',newline='\n')
reg=json.loads((R/'publication/explanatory-early-batch3-working.json').read_text(encoding='utf-8'));assert reg['automatic_formal_site_injection'] is False and reg['canonical_manuscript_changes'] is False
rows=reg['figures'];assert len(rows)==10 and {r['id'] for r in rows}=={'E22','E28','E39','E14','E30'}
for row in rows:
 root=P/'chapters'/row['lang'];before=(root/(row['slug']+'-before.html')).read_text(encoding='utf-8');after=(root/(row['slug']+'.html')).read_text(encoding='utf-8');assert after.count(row['html'])==1 and after.replace(row['html'],'',1)==before
for row in json.loads((O/'reading-contexts.json').read_text(encoding='utf-8')):assert sha(R/row['path'])==row['sha256']
for n in [4,6]:assert sum(F(1,2**j) for j in range(1,n+1))+F(1,2**n)==1
matrix=[[F(3,4),F(1,4)],[F(1,4),F(3,4)]]
for u in [0,1,2]:
 mu=[F(u,2),1-F(u,2)]
 for f in [[0,4],[4,0]]:
  push=[sum(mu[i]*matrix[i][j] for i in range(2)) for j in range(2)];pull=[sum(matrix[i][j]*f[j] for j in range(2)) for i in range(2)]
  assert sum(push[j]*f[j] for j in range(2))==sum(mu[i]*pull[i] for i in range(2))
assert 12*(F(1,3)-F(1,2)+F(1,4))==1 and F(1,2)-F(1,2)==0
for matrix,expected in [([[1,0],[2,0]],0),([[1,0],[1,1]],1)]:
 gram=[[sum(matrix[i][k]*matrix[j][k] for k in range(2)) for j in range(2)] for i in range(2)];assert gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]==expected
for lg in ['zh','en']:
 for n in [4,16,64]:
  for kind,symbol in [('rare','X'),('small','Y')]:
   text=(R/f'assets/visuals/explanatory-early-v2/E14-{lg}-{n}-{kind}.svg').read_text(encoding='utf-8');assert all(symbol+s in text for s in ['ₙ₁','ₙ₂','ₙₙ']) and '…' in text
 row=next(r for r in rows if r['id']=='E30' and r['lang']==lg);assert ('不是合法的可预测事前策略' if lg=='zh' else 'not a legitimate predictable strategy') in row['html']
for f in A.glob('*.svg'):ET.fromstring(f.read_text(encoding='utf-8'))
resources=json.loads((O/'e13-resource-check.json').read_text(encoding='utf-8'))['resources'];assert len(resources)==2 and all(sha(R/r['target'])==r['sha256'] for r in resources)
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,attrs):self.urls += [v for k,v in attrs if k in ['src','href'] and v]
broken=[];links=0
for f in P.rglob('*.html'):
 parser=Links();parser.feed(f.read_text(encoding='utf-8'))
 for url in parser.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=unquote(u.path);dest=None
  for prefix,folder in [('/assets/',R/'assets'),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/previous-shots/',R/'reports/early-explanations-batch2-2026-10-31/screenshots')]:
   if path.startswith(prefix):dest=folder/path[len(prefix):];break
  if dest is None:dest=P/(path.lstrip('/') or 'index.html') if path.startswith('/') else f.parent/path
  if not dest.is_file():broken.append((f.relative_to(P).as_posix(),url))
  links+=1
assert not broken,broken[:10]
browser=json.loads((O/'browser-checks.json').read_text(encoding='utf-8'))
assert [len(browser[k]) for k in ['figure_checks','chapter_checks','print_checks','interactions']]==[20,40,10,40]
assert not any(r['overflow'] or r['broken_images'] for k in ['figure_checks','chapter_checks','print_checks'] for r in browser[k])
assert all(x['pressed']=='true' and x['graph_source_changed'] for x in browser['interactions'])
assert not browser['e13']['broken_images'] and all(i['loaded'] for i in browser['e13']['images'])
shots=[]
for f in (O/'screenshots').glob('*.jpg'):
 assert f.read_bytes().startswith(b'\xff\xd8\xff');shots.append(dict(file=f.relative_to(O).as_posix(),sha256=sha(f),bytes=f.stat().st_size))
(O/'screenshot-provenance.json').write_text(json.dumps(dict(method='Actual browser HTTP viewport JPEG, no synthetic pages, stitching or full-page capture claim',files=shots),indent=2),encoding='utf-8',newline='\n')
result=dict(source_commit=reg['source_commit'],protected_paths=len(base),unchanged=len(base)-len(changed),authorized_old_file_changes=len(changed),new_groups=['E22','E28','E39'],localized_corrections=['E14','E30'],bilingual_overlays=10,exact_models='E22 mean tails, E28 finite-kernel duality and E39 orthogonal Gram matrices checked',links=links,real_browser=dict(figures=20,chapters=40,static_pages=10,interactions=40),screenshots=len(shots),e13_actual_dist_resources='Both language paths and actual browser loading pass; no cloud failure inferred',aesthetic_review='New figures pending author review',math_final_review='Independent expert final review remains open',printing='Static candidates viewed; native pagination, embedded PDF fonts and physical paper not verified',publication='No publication or push')
(O/'checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n');print(json.dumps(result,ensure_ascii=False))
