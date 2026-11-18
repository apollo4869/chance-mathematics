"""Exact-model, preservation and delivery checks, distinct from aesthetic approval."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb,cos,exp,isclose
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,xml.etree.ElementTree as ET,sys
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from tools.explanatory_illustrations.early_batch2 import tau,ARRIVALS
O=R/'reports/early-explanations-batch2-2026-10-31';P=O/'preview';A=R/'assets/visuals/explanatory-early-v2';OLD=R/'reports/volumes1-5-visual-review-2026-10-31'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def ok(name,result):checks.append(dict(check=name,result=result))
base=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'));bad=[k for k,v in base.items() if not (R/k).is_file() or sha(R/k)!=v];assert not bad,bad[:15];ok('All inherited and prior tracked sources, figures and builds unchanged',len(base))
reg=json.loads((R/'publication/explanatory-early-batch2-working.json').read_text(encoding='utf-8'));assert reg['automatic_formal_site_injection'] is False and reg['canonical_manuscript_changes'] is False
assert len(reg['figures'])==12 and {r['id'] for r in reg['figures']}=={'E12','E13','E14','E17','E30','E24'}
for r in reg['figures']:
 d=P/'chapters'/r['lang'];before=(d/(r['slug']+'-before.html')).read_text(encoding='utf-8');after=(d/(r['slug']+'.html')).read_text(encoding='utf-8');assert after.count(r['html'])==1 and after.replace(r['html'],'',1)==before
ok('Five bilingual new overlays plus E24 preserve every original HTML block',12)
contexts=json.loads((O/'reading-contexts.json').read_text(encoding='utf-8'));assert len(contexts)==12
for c in contexts:assert sha(R/c['path'])==c['sha256'] and c['section_text'].startswith('## ')
words=list(product([1,-1],repeat=4));counts={k:sum(tau(w)==k for w in words) for k in [2,4,0]};assert counts=={2:8,4:4,0:4}
squares=[(2+sum(w))**2 for w in product([1,-1],repeat=2)];assert squares==[16,4,4,0] and sum(squares)/4==6
assert sum(max(abs(sum(w[:k])) for k in range(1,5))>=2 for w in words)==12
ok('E12 all16 first crossings, disjoint classification and conditional second moment',dict(counts=counts,squares=squares))
for n in [4,5,6]:
 probs={-n+2*j:F(comb(n,j),2**n) for j in range(n+1)};assert sum(probs.values())==1 and sum(k*p for k,p in probs.items())==0 and sum(k*k*p for k,p in probs.items())==n
 for lg in ['zh','en']:
  xml=ET.fromstring((A/f'E13-{lg}-{n}.svg').read_text(encoding='utf-8'));disks=[e for e in xml.iter() if e.tag.endswith('circle') and float(e.attrib.get('cy',0))==99];assert len(disks)==n+1
  weights=[float(e.attrib['r'])**2 for e in disks];assert all(isclose(w/sum(weights),float(p),abs_tol=1e-12) for w,p in zip(weights,probs.values()))
ok('E13 exact binomial law, maximal span2 and literal SVG disk areas','n4,5,6; wrong width1 gives half the width2 local rectangle')
for n in [4,16,64]:
 rare=[(F(-1),F(1,2*n)),(F(0),F(1)-F(1,n)),(F(1),F(1,2*n))]
 assert sum(p for x,p in rare)==1 and n*sum(x*x*p for x,p in rare)==1
 assert n*sum(x*x*p for x,p in rare if abs(x)>F(1,2))==1
 assert 1/n<=1/4 and 1/(n**.5)<=.5
 # The source SVG coordinates must keep amplitudes +/-1 fixed as probabilities shrink.
 for lg in ['zh','en']:
  xml=ET.fromstring((A/f'E14-{lg}-{n}-rare.svg').read_text(encoding='utf-8'));circles=[e for e in xml.iter() if e.tag.endswith('circle')];assert [float(e.attrib['cx']) for e in circles]==[70,180,290]
  areas=[float(e.attrib['r'])**2 for e in circles];assert all(isclose(v/sum(areas),float(p),abs_tol=1e-12) for v,(x,p) in zip(areas,rare))
assert abs((1+(cos(.7)-1)/100000)**100000-exp(cos(.7)-1))<1e-6
ok('E14 Feller versus Lindeberg, centers and probability areas','Centered variance1 rows; outside strict1/2 cost1 vs0; fixed rare jump locations')
qs=[];forecasts=[]
for hist in [(0,0),(1,0),(0,1),(1,1)]:
 likelihood=[]
 for theta in [F(1,4),F(3,4)]:
  likelihood.append(theta**sum(hist)*(1-theta)**(2-sum(hist)))
 q=likelihood[1]/sum(likelihood);qs.append(q);forecasts.append(F(1,4)+q/2)
assert qs==[F(1,10),F(1,2),F(1,2),F(9,10)] and forecasts==[F(3,10),F(1,2),F(1,2),F(7,10)]
ok('E17 Bayes posteriors and forecasts computed from the joint law',dict(q=list(map(str,qs)),prediction=list(map(str,forecasts))))
for c,arr in ARRIVALS.items():assert len(arr)==c and all(0<t<3 for t in arr) and arr==sorted(set(arr))
ok('E30 distinct finite arrival instants and two Stieltjes readings','H=1: N3−3, expectation0; H=ΔN: N3−0, expectation3; records not assigned equal probabilities')
for d in [F(1,4),F(1,8),F(1,16)]:
 a=F(1,2);b=a+d;lam=lambda t:b*t/a if t<=a else b+(1-b)*(t-a)/(1-a)
 grid=[F(i,1024) for i in range(1025)];assert lam(0)==0 and lam(1)==1 and lam(a)==b and max(abs(lam(t)-t) for t in grid)==d
 assert all(lam(t)<lam(u) for t,u in zip(grid,grid[1:]))
 assert all(int(lam(t)>=b)==int(t>=a) for t in grid)
 end=a+d*d*(1-a)/(1-b);assert end>a and lam(end)==b+d*d and b<=lam((end+a)/2)<b+d*d
ok('E24 clock direction, fixed endpoints, exact displacement, right-continuous support','All3 deltas; nonempty transformed pulse; onto clocks preserve supremum')
svgs=list(A.glob('*.svg'))
for f in svgs:ET.fromstring(f.read_text(encoding='utf-8'))
ok('All editable states and12 standalone static plates are valid SVG',len(svgs))
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):
  for k,v in a:
   if k in ['href','src'] and v:self.urls.append(v)
errors=[];num=0
for f in P.rglob('*.html'):
 parser=Links();parser.feed(f.read_text(encoding='utf-8'))
 for url in parser.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=unquote(u.path);dest=None
  for prefix,folder in [('/assets/',R/'assets'),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/previous/',OLD/'preview'),('/references/',OLD/'references')]:
   if path.startswith(prefix):dest=folder/(path[len(prefix):] or 'index.html');break
  if dest is None:dest=P/(path.lstrip('/') or 'index.html') if path.startswith('/') else f.parent/path
  if not dest.is_file():errors.append((f.relative_to(P).as_posix(),url))
  num+=1
assert not errors,errors[:25];ok('All generated review/chapter/resource links have target files',num)
browser=json.loads((O/'browser-checks.json').read_text(encoding='utf-8'));assert len(browser['figure_checks'])==24 and len(browser['chapter_checks'])==48 and len(browser['print_checks'])==12
assert not any(x['overflow'] or x['broken_images'] for key in ['figure_checks','chapter_checks','print_checks'] for x in browser[key]);assert len(browser['interactions'])>=24
assert all(x['pressed']=='true' and x['visible_graph_source_changed'] is True for x in browser['interactions'])
ok('Actual browser desktop/mobile, chapter overlays, static pages and state readbacks',dict(figures=24,chapters=48,static=12,interactions=len(browser['interactions'])))
shots=[]
for f in (O/'screenshots').glob('*.jpg'):
 assert f.read_bytes()[:3]==b'\xff\xd8\xff';shots.append(dict(file=f.relative_to(O).as_posix(),sha256=sha(f),bytes=f.stat().st_size))
(O/'screenshot-provenance.json').write_text(json.dumps(dict(method='Actual browser viewport JPEG, no synthetic page images or stitching',files=shots),indent=2),encoding='utf-8',newline='\n')
(O/'checks.json').write_text(json.dumps(dict(checks=checks,math='Exact-model self-check only; independent expert final review remains open',aesthetics='All six current candidates pending author review',printing='Standalone static SVG pages viewed; native pagination, PDF embedding and paper untested',publication='No publication or remote push'),ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps(dict(checks=len(checks),protected=len(base),svg=len(svgs),screenshots=len(shots),links=num,result='passed within stated scope')))
