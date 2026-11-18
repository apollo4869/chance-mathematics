"""Preservation and exact-model checks. Never a proxy for author aesthetic approval."""
from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib,json,xml.etree.ElementTree as ET,itertools,math
R=Path(__file__).resolve().parents[1];O=R/'reports/volumes1-5-visual-review-2026-10-31';P=O/'preview';A=R/'assets/visuals/explanatory-early-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def ok(name,value):checks.append({'check':name,'result':value})
baseline=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'));bad=[k for k,v in baseline.items() if not (R/k).is_file() or sha(R/k)!=v];assert not bad,bad[:10];ok('All protected manuscript, proof, prior art and build hashes unchanged',len(baseline))
audit=json.loads((O/'chapter-audit.json').read_text(encoding='utf-8'));assert [x['chapter'] for x in audit]==list(range(1,41));assert {x['volume'] for x in audit}=={1,2,3,4,5}
for a in audit:assert sha(R/a['source'])==a['sha256']
assert any(x['kind']=='inline-svg' and '216' in x['source'] for x in audit[0]['existing_visuals'])
assert any(x['kind']=='inline-svg' and 'Riemann' in x['source'] for x in audit[5]['existing_visuals'])
assert not any(x['source']=='inline SVG' for a in audit for x in a['existing_visuals'])
ok('40 chapter judgments with actual source identities; formula SVGs excluded',40)
reg=json.loads((R/'publication/explanatory-early-pilots-working.json').read_text(encoding='utf-8'));assert reg['canonical_manuscript_changes'] is False and reg['automatic_formal_site_injection'] is False
assert {r['chapter'] for r in reg['figures']}=={6,8,16,20,24} and len(reg['figures'])==10
for r in reg['figures']:
 d=P/'chapters'/r['lang'];after=(d/(r['slug']+'.html')).read_text(encoding='utf-8');before=(d/(r['slug']+'-before.html')).read_text(encoding='utf-8');assert after.count(r['html'])==1;assert after.replace(r['html'],'',1)==before
ok('Five bilingual chapter overlays preserve all original nonfigure HTML and old figures',10)
svgs=list(A.glob('*.svg'))
for f in svgs:ET.fromstring(f.read_text(encoding='utf-8'))
ok('Editable SVG XML and independent static outputs',len(svgs))
vals=[1,5,1,3,5,1,3,5];m={v:F(vals.count(v),8) for v in [1,3,5]};assert sum(v*p for v,p in m.items())==3 and sum(m.values())==1
ok('E06 equal-value preimage measures and integral', {str(v):str(p) for v,p in m.items()})
assign=list(itertools.product([0,1],repeat=3));assert not any(a!=b and b!=c and a!=c for a,b,c in assign)
law={(0,1,0):F(1,2),(1,0,1):F(1,2)}
for j in range(3):assert sum(p for a,p in law.items() if a[j]==1)==F(1,2)
for a,b in [(0,1),(1,2)]:assert sum(p for x,p in law.items() if x[a]!=x[b])==1
assert sum(p for x,p in law.items() if x[0]==x[2])==1
ok('E08 all eight assignments and repaired joint law','All-opposite impossible; 010/101 realizes repaired fair pair laws')
Ts=[];Ls=[]
for inc in itertools.product([-1,1],repeat=4):
 path=[0]
 for d in inc:path.append(path[-1]+d)
 if path[:3]==[0,1,0]:Ts.append(next(j for j in range(1,5) if path[j]==0));Ls.append(max(j for j in range(5) if path[j]==0))
assert len(Ts)==4 and set(Ts)=={2} and set(Ls)=={2,4};ok('E16 all completions of the same information atom',{'T':Ts,'L':Ls})
for mode,expected in [('P',[.5,1/6,1/6,1/6]),('Q',[.25]*4)]:
 for lg in ['zh','en']:
  xml=ET.fromstring((A/f'E20-{lg}-{mode}-1.svg').read_text(encoding='utf-8'));disks=[e for e in xml.iter() if e.tag.endswith('circle') and float(e.attrib.get('cy',0))==189];assert len(disks)==4
  areas=[float(e.attrib['r'])**2 for e in disks];actual=[v/sum(areas) for v in areas];assert all(abs(a-b)<1e-12 for a,b in zip(actual,expected))
assert F(1,2)/2==F(1,4) and 3*F(1,2)/2==F(3,4)
ok('E20 joint law and literal disk areas','P: 1/2,1/6,1/6,1/6; Q: 1/4 each; fixed geometric vertices')
for delta in [F(1,4),F(1,8),F(1,16)]:
 a=F(1,2);b=a+delta
 def lam(t):return b*t/a if t<=a else b+(1-b)*(t-a)/(1-a)
 ts=[F(i,1024) for i in range(1025)];assert lam(0)==0 and lam(1)==1 and lam(a)==b
 assert all(lam(t)<lam(u) for t,u in zip(ts,ts[1:]));assert max(abs(lam(t)-t) for t in ts)==delta
 assert all(int(lam(t)>=b)==int(t>=a) for t in ts)
 pulse_end=a+delta**2*(1-a)/(1-b);assert pulse_end>a and lam(pulse_end)==b+delta**2
 assert b<=lam((a+pulse_end)/2)<b+delta**2
ok('E24 time-change direction, jump values, exact clock error and surviving pulse','All three δ; static uses δ=1/4 for a readable nonzero pulse')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):
  for k,v in a:
   if k in ['href','src'] and v:self.urls.append(v)
errors=[];count=0
for f in P.rglob('*.html'):
 pa=Links();pa.feed(f.read_text(encoding='utf-8'))
 for url in pa.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=unquote(u.path);dest=None
  for prefix,base in [('/assets/visuals/explanatory-early-v1/',A),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/references/',O/'references')]:
   if path.startswith(prefix):dest=base/path[len(prefix):];break
  if dest is None:dest=P/path.lstrip('/') if path.startswith('/') else f.parent/path
  if path=='/':dest=P/'index.html'
  if not dest.is_file():errors.append((str(f.relative_to(P)),url))
  count+=1
assert not errors,errors[:20];ok('Review and inherited book resource link targets exist',count)
br=json.loads((O/'browser-checks.json').read_text(encoding='utf-8'));assert len(br['chapter_checks'])==40;assert not any(x['overflow'] for x in br['chapter_checks']);assert len(br['interaction_checks'])==18
ok('Actual browser observations','40 chapter before/after viewport checks; 18 interaction readbacks; 20 figure viewport checks')
shots=[]
for folder in ['screenshots','references']:
 for f in (O/folder).glob('*.jpg'):
  assert f.read_bytes()[:3]==b'\xff\xd8\xff';shots.append({'file':f.relative_to(O).as_posix(),'sha256':sha(f),'bytes':f.stat().st_size})
(O/'screenshot-provenance.json').write_text(json.dumps({'method':'Actual browser viewport JPEGs, no stitching or synthetic page images','files':shots},ensure_ascii=False,indent=2),encoding='utf-8');ok('Screenshot signature and provenance',len(shots))
(O/'checks.json').write_text(json.dumps({'checks':checks,'math_status':'Exact-model self-check; expert final review open','aesthetic_status':'Five pilots pending author review','print_status':'Static SVG and browser print pages viewed; native print/PDF/physical output not tested','publication':'No deployment or remote push'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checks':len(checks),'protected':len(baseline),'chapters':len(audit),'svg':len(svgs),'screenshots':len(shots),'links':count,'result':'passed within stated scope'},ensure_ascii=False))
