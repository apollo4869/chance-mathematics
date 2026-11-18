"""Independent finite-model arithmetic, visual encoding, preservation and browser evidence."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys,json,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from tools.explanatory_illustrations.early_batch4 import tilt,weight,kvalue
O=R/'reports/early-explanations-batch4-2026-11-04';P=O/'preview';A=R/'assets/visuals/explanatory-early-v4'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'));changed=[p for p,v in base.items() if not (R/p).is_file() or sha(R/p)!=v];assert not changed,changed[:10]
reg=json.loads((R/'publication/explanatory-early-batch4-working.json').read_text(encoding='utf-8'));assert not reg['automatic_formal_site_injection'] and not reg['canonical_manuscript_changes'];rows=reg['figures'];assert len(rows)==4 and {r['id'] for r in rows}=={'E27','E29'}
for r in rows:
 d=P/'chapters'/r['lang'];before=(d/(r['slug']+'-before.html')).read_text(encoding='utf-8');after=(d/(r['slug']+'.html')).read_text(encoding='utf-8');assert after.count(r['html'])==1 and after.replace(r['html'],'',1)==before
contexts=json.loads((O/'reading-contexts.json').read_text(encoding='utf-8'));assert len(contexts)==6
for c in contexts:assert sha(R/c['path'])==c['sha256']
for N in [2,4,6]:
 v=F(1,2**N);assert sum(F(1,2**k) for k in range(1,N+1))+v==1
 for K in [N+1,N+2,N+10]:assert sum(F(1,2**k) for k in range(N+1,K+1))==v-F(1,2**K)<v
 for lg in ['zh','en']:
  r=ET.parse(A/f'E27-{lg}-{N}-means.svg').getroot();rects=[e for e in r.iter() if e.tag.endswith('rect')];assert sum(e.get('fill')=='#eaf2ee' for e in rects)==sum(2**k for k in range(1,N+1))
  assert sum(e.get('fill')=='#fbf0df' for e in rects)==N
  r=ET.parse(A/f'E27-{lg}-{N}-energy.svg').getroot();rects=[e for e in r.iter() if e.tag.endswith('rect') and e.get('x')=='42' and e.get('width')=='126'];tail=[e for e in rects if e.get('fill')=='white'];assert len(tail)==1 and abs(float(tail[0].get('height'))/252-float(v))<1e-12
  filled=[e for e in rects if e.get('fill') not in ['white','none']];assert len(filled)==N and all(abs(float(e.get('height'))/252-2**(-k))<1e-12 for k,e in enumerate(filled,1))
  for focus in ['end','whole']:
   text=(A/f'E27-{lg}-{N}-{focus}.svg').read_text(encoding='utf-8');assert 'E|D(1)|² ≤' in text and 'E sup |D(t)|² ≤' in text

model_results=[]
with localcontext() as ctx:
 ctx.prec=90
 for n in [64,512,4096]:
  m=tilt(n);event={};normalizations={}
  # Independent binomial recurrence, rather than the generator's integer-combination sum.
  for name,q in [('P',Decimal(1)/2),('Q',Decimal(3)/4)]:
   p=(1-q)**n;mass=Decimal(0);first=Decimal(0);second=Decimal(0);selected=Decimal(0)
   for k in range(n+1):
    mass+=p;first+=k*p;second+=(Decimal(k)-n*q)**2*p
    if m['lo']<=k<=m['hi']:selected+=p
    if k<n:p*=Decimal(n-k)/(k+1)*q/(1-q)
   assert abs(mass-1)<Decimal('1e-65') and abs(first-n*q)<Decimal('1e-60') and abs(second-n*q*(1-q))<Decimal('1e-60')
   assert abs(selected-m[name])/m[name]<Decimal('1e-65');event[name]=selected;normalizations[name]=str(mass)
  assert 0<event['P']<event['Q']<1
  delta=Decimal(m['delta'].numerator)/m['delta'].denominator;bound=Decimal(3)/(4*m['root']);assert 1-event['Q']<=bound
  shift=-event['Q'].ln()/n;assert m['D']-m['theta']*delta+shift<=m['rate']<=m['D']+m['theta']*delta+shift
  record_results=[]
  for pos in ['low','target','high']:
   k=kvalue(m,pos);L,r=weight(n,k);exact=Decimal(2**n)/Decimal(3**k);assert abs(L-exact)/exact<Decimal('1e-65')
   assert abs(r-(Decimal(k)/n*m['theta']-Decimal(2).ln()))<Decimal('1e-65')
   assert abs(r-m['D'])<=m['theta']*delta+Decimal('1e-65')
   for lg in ['zh','en']:
    root=ET.parse(A/f'E29-{lg}-{n}-{pos}-record.svg').getroot();strips=[e for e in root.iter() if e.tag.endswith('rect') and e.get('y')=='62'];assert len(strips)==2
    assert abs(float(strips[0].get('width'))/310-k/n)<1e-12 and abs(sum(float(e.get('width')) for e in strips)-310)<1e-12
   record_results.append(dict(position=pos,K=k,likelihood=str(L),per_sample_log_cost=str(r)))
  for lg in ['zh','en']:
   root=ET.parse(A/f'E29-{lg}-{n}-event.svg').getroot();sectors=[e for e in root.iter() if e.tag.endswith('path') and e.get('fill')=='#16776d'];assert len(sectors)==(2 if n==64 else 1)
  model_results.append(dict(n=n,lower=m['lo'],upper=m['hi'],delta=str(m['delta']),P=str(event['P']),Q=str(event['Q']),finite_event_rate=str(m['rate']),D=str(m['D']),chebyshev_complement_bound=str(bound),normalizations=normalizations,records=record_results))
assert weight(64,40)[0]>1 # A valid finite-parameter boundary, not silently suppressed.
for f in A.glob('*.svg'):ET.fromstring(f.read_text(encoding='utf-8'))
(O/'model-checks.json').write_text(json.dumps(dict(method='90-digit independent binomial recurrence checked against 75-digit exact-integer-sum generator; finite dyadic moments and SVG geometry',models=model_results),ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):self.urls += [v for k,v in a if k in ['href','src'] and v]
broken=[];count=0
for f in P.rglob('*.html'):
 parser=Links();parser.feed(f.read_text(encoding='utf-8'))
 for url in parser.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=unquote(u.path);dest=None
  for prefix,folder in [('/assets/',R/'assets'),('/book/',R/'dist'),('/shots/',O/'screenshots')]:
   if path.startswith(prefix):dest=folder/path[len(prefix):];break
  if dest is None:dest=P/(path.lstrip('/') or 'index.html') if path.startswith('/') else f.parent/path
  if not dest.is_file():broken.append((f.relative_to(P).as_posix(),url))
  count+=1
assert not broken,broken[:10]
browser=json.loads((O/'browser-checks.json').read_text(encoding='utf-8'));assert [len(browser[k]) for k in ['figure_checks','chapter_checks','print_checks']]==[8,16,4]
assert not any(x['overflow'] or x['broken_images'] for k in ['figure_checks','chapter_checks','print_checks'] for x in browser[k])
assert len(browser['compensation_states'])==24 and len(browser['tilt_states'])==36
assert all(s['pressed']=='true' and s['scope_pressed']=='true' and s['graph_changed'] for s in browser['compensation_states'])
for s in browser['tilt_states']:
 assert s['n_pressed']=='true' and s['record_pressed']=='true' and s['graph_changed'];m=tilt(s['n']);assert f'{m["rate"]:.5f}' in s['finite_rate'] and f'{m["D"]:.5f}' in s['finite_rate']
 assert str(m['lo']) in s['event_definition'] and str(m['hi']) in s['event_definition']
assert len(browser['details_checks'])==8 and all(x['open'] for x in browser['details_checks']);assert len(browser['layer_details'])==2 and all(x['open'] for x in browser['layer_details'])
shots=[]
for f in (O/'screenshots').glob('*.jpg'):
 assert f.read_bytes().startswith(b'\xff\xd8\xff');shots.append(dict(file=f.relative_to(O).as_posix(),sha256=sha(f),bytes=f.stat().st_size))
(O/'screenshot-provenance.json').write_text(json.dumps(dict(method='Actual browser HTTP viewport JPEG, no synthetic pages or stitching',files=shots),indent=2),encoding='utf-8',newline='\n')
result=dict(source_commit=reg['source_commit'],new_groups=['E27','E29'],protected_paths=len(base),changed_old_files=0,bilingual_overlays=4,actual_source_sections=6,model_check='Independent high-precision finite arithmetic and literal SVG encodings pass',links=count,browser=dict(figures=8,chapters=16,static_pages=4,compensation_states=24,tilt_states=36,details=8,mobile_layer_details=2),screenshots=len(shots),author_visual_review='pending',independent_expert_review='open',printing='Static candidates viewed; native pagination/PDF fonts/physical print not verified',publication='No publication or push')
(O/'checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n');print(json.dumps(result,ensure_ascii=False))
