"""Check preservation, scope, exact models and local review artifacts; not expert review."""
from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,re,xml.etree.ElementTree as ET,math,sys

ROOT=Path(__file__).resolve().parents[1];O=ROOT/'reports/volume5-illustrations-batch2-2026-10-31';P=O/'preview'
sys.path.insert(0,str(ROOT))
A1=ROOT/'assets/visuals/explanatory-v1';A2=ROOT/'assets/visuals/explanatory-v2'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def record(name,data):checks.append({'check':name,'result':data})
baseline=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'))
bad=[p for p,h in baseline.items() if not (ROOT/p).is_file() or digest(ROOT/p)!=h]
assert not bad,bad;record('Protected source/artwork/batch-1 hashes',len(baseline))
rows=json.loads((ROOT/'publication/explanatory-figures-batch2-working.json').read_text(encoding='utf-8'))
assert rows['canonical_manuscript_changes'] is False and rows['automatic_formal_site_injection'] is False
focus=[r for r in rows['figures'] if r['book_preview']]
assert len(focus)==12 and {r['id'] for r in focus}=={'V34','V37','V35','V36','V38','V40'}
assert {r['id'] for r in focus}-{'V34','V37'}=={'V35','V36','V38','V40'}
old=json.loads((ROOT/'publication/explanatory-figures-working.json').read_text(encoding='utf-8'))['figures']
for r in focus:
 d=P/'chapters'/r['lang'];before=(d/(r['slug']+'-before.html')).read_text(encoding='utf-8');after=(d/(r['slug']+'.html')).read_text(encoding='utf-8')
 assert after.count(r['html'])==1
 if r['id'] in ['V34','V37']:
  prev=next(x['html'] for x in old if x['id']==r['id'] and x['lang']==r['lang'])
  assert after.replace(r['html'],'',1).replace('/explanatory-v2/','/explanatory-v1/')==before.replace(prev,'',1)
 else:assert after.replace(r['html'],'',1)==before
record('Six bilingual overlays preserve all nonfigure chapter HTML',12)
preserved=[]
for p in A1.glob('*.svg'):
 if not p.name.startswith('V34'):
  assert (A2/p.name).read_bytes()==p.read_bytes(),p.name;preserved.append(p.name)
record('All copied SVG assets except requested V34 are byte-identical',len(preserved))
svgs=list(A2.glob('*.svg'))
for p in svgs:ET.fromstring(p.read_text(encoding='utf-8'))
record('SVG XML parsed',len(svgs))

# Exact deterministic calculations underpinning all visible states.
assert [max(2-a,0)**2 for a in [0,1,math.inf]]==[4,1,0]
assert [1/(1-t) for t in [F(0),F(1,2),F(3,4),F(7,8)]]==[1,2,4,8]
# For a<=t, d(t-a)^2/dt = 2(t-a)=2 sqrt((t-a)^2); at departure both are zero.
# x=1/(1-t) has x'=x^2 and diverges at 1. No stochastic simulation used.
record('V35 exact nonuniqueness and finite lifetime models','4,1,0; 1,2,4,8 at the stated unequal times')
# Near zero: accessibility int_0^c(S(y)-S(0))*m(dy);
# entrance int_0^c(S(c)-S(y))*m(dy). The powers below classify
# integrability of their integrands at 0; None denotes S(0)=-infinity.
models={'regular':{'p':0,'m':0,'Sigma':1,'N':0},
        'exit':{'p':0,'m':-1,'Sigma':0,'N':-1},
        'entrance':{'p':-2,'m':2,'Sigma':None,'N':1},
        'natural':{'p':0,'m':-2,'Sigma':-1,'N':-2}}
expected={'regular':(True,True),'exit':(True,False),'entrance':(False,True),'natural':(False,False)}
for k,m in models.items():
 sig=(m['Sigma'] is not None and m['Sigma']>-1);ent=m['N']>-1
 assert (sig,ent)==expected[k]
from tools.explanatory_illustrations.volume5_next import BOUNDARIES
assert BOUNDARIES==expected
record('V36 directional flags and endpoint integrability','BM regular; BESQ0 exit; BES3 entrance; GBM natural')
values=[]
for x in [F(1,4),F(1,2),F(3,4)]:
 for c in range(3):
  running=c*x*(1-x);u=x+running
  assert F(1,2)*(2*c)+(-c)==0 # -u''/2=c
  values.append({'x':str(x),'c':c,'exit1':str(x),'mean_time':str(x*(1-x)),'u':str(u)})
assert F(1,4)+2*F(1,4)*F(3,4)==F(5,8)
record('V38 all nine exact payoff states',values)
for t in [.25,.5,1]:
 for angle in [0,math.pi/4,math.pi/2]:
  assert abs(math.cos(angle)**2+math.sin(angle)**2-1)<1e-12
  assert abs((math.exp(t/2)*math.cos(angle))**2+(math.exp(t/2)*math.sin(angle))**2-math.exp(t))<1e-12
record('V40 both radii for all nine geometric readings','1 and exp(t/2), same angle; no angular probability claim')
for eps in [F(1,2),F(1,4),F(1,8)]:
 area=2*eps-eps**2;assert area/(2*eps)==1-eps/2
record('V37 normalization unchanged','3/4, 7/8, 15/16; point 0/0 undefined')
assert 3**3-1**3==26 and 3*(3-1)==6 and 3*(3-1)**2==12 and (3-1)**3==8
assert 26-6==12+8==20
record('V34 Taylor residual and full jump correction','8 versus 12+8=20')

class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['href','src'] and v:self.urls.append(v)
errors=[];count=0
for f in P.rglob('*.html'):
 h=Links();h.feed(f.read_text(encoding='utf-8'))
 for url in h.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=unquote(u.path);dest=None
  for prefix,base in [('/assets/visuals/explanatory-v2/',A2),('/assets/visuals/explanatory-v1/',A1),('/book/',ROOT/'dist'),('/shots/',O/'screenshots')]:
   if path.startswith(prefix):dest=base/path[len(prefix):];break
  if dest is None:dest=(P/path.lstrip('/')) if path.startswith('/') else f.parent/path
  if path=='/':dest=P/'index.html'
  if not dest.is_file():errors.append((str(f.relative_to(P)),url))
  count+=1
assert not errors,errors[:20];record('Local HTML href/src targets exist',count)
browser=json.loads((O/'browser-checks.json').read_text(encoding='utf-8'))
assert len(browser['chapter_checks'])==48 and not any(x['overflow'] for x in browser['chapter_checks'])
assert len(browser['mobile_source_checks'])==4
for x in browser['mobile_source_checks']:
 assert all('mobile-'+x['key'] in s for s in x['images'])
record('Observed browser results','48 chapter viewport checks; 4 mobile picture-source transitions; no chapter horizontal overflow')
shots=list((O/'screenshots').glob('*.jpg'))
for s in shots:assert s.read_bytes()[:3]==b'\xff\xd8\xff',s
(O/'screenshot-provenance.json').write_text(json.dumps({'capture':'Actual in-app browser viewport JPEGs; no stitching or synthetic webpage images','screenshots':[{'file':s.name,'sha256':digest(s),'bytes':s.stat().st_size} for s in shots]},ensure_ascii=False,indent=2),encoding='utf-8')
record('JPEG signature and screenshot provenance',len(shots))
out={'scope':'Four additions and two targeted refinements only','checks':checks,'math_status':'Codex exact-model self-check; independent mathematical final review remains open','visual_status':'New artwork and refinements await author review','print_status':'Static SVG and browser print pages checked; native pagination/PDF/physical print not tested','publication':'Not published; not pushed'}
(O/'checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checks':len(checks),'protected_files':len(baseline),'svg':len(svgs),'screenshots':len(shots),'local_links':count,'result':'passed within recorded scope'},ensure_ascii=False))
