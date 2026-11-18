"""Check only E22/E28 revision models, preservation and actually collected evidence."""
from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,xml.etree.ElementTree as ET,sys
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from tools.explanatory_illustrations import early_batch3 as previous
O=R/'reports/early-explanations-batch3-revision-2026-11-04';P=O/'preview';A=R/'assets/visuals/explanatory-early-v3r2'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'));changed=[p for p,v in base.items() if not (R/p).is_file() or sha(R/p)!=v];assert not changed,changed[:10]
reg=json.loads((R/'publication/explanatory-batch3-revision-working.json').read_text(encoding='utf-8'));assert not reg['automatic_formal_site_injection'] and not reg['canonical_manuscript_changes'];rows=reg['figures'];assert len(rows)==4 and {r['id'] for r in rows}=={'E22','E28'}
assert set(reg['adopted_and_protected'])=={'E14','E30','E39'}
for r in rows:
 root=P/'chapters'/r['lang'];before=(root/(r['slug']+'-before.html')).read_text(encoding='utf-8');after=(root/(r['slug']+'.html')).read_text(encoding='utf-8');assert after.count(r['html'])==1 and after.replace(r['html'],'',1)==before
for c in json.loads((O/'reading-contexts.json').read_text(encoding='utf-8')):assert sha(R/c['path'])==c['sha256']
for lg in ['zh','en']:
 for n in [4,6]:
  assert sum(F(1,2**j) for j in range(1,n+1))+F(1,2**n)==1
  for fast in [0,1]:
   svg=(A/f'E22-{lg}-{n}-{fast}.svg').read_text(encoding='utf-8');assert previous.clock(lg,n,fast).fragment() in svg
   assert ('ζ &lt; ∞  a.s.' if fast else 'ζ = ∞  a.s.') in svg
  static=(A/f'E22.{lg}.svg').read_text(encoding='utf-8');assert ('左右不共用时间刻度' if lg=='zh' else 'the panels do not share a time scale') in static
Pmat=[[F(3,4),F(1,4)],[F(1,4),F(3,4)]]
states=[]
for u in [0,1,2]:
 for flip in [0,1]:
  p=F(u,2);mu=[p,1-p];f=[4,0] if flip else [0,4];out=[sum(mu[i]*Pmat[i][j] for i in range(2)) for j in range(2)];tf=[sum(Pmat[i][j]*f[j] for j in range(2)) for i in range(2)];v=sum(out[j]*f[j] for j in range(2));assert v==sum(mu[i]*tf[i] for i in range(2))
  for lg in ['zh','en']:
   root=ET.fromstring((A/f'E28-{lg}-{u}-{flip}-0.svg').read_text(encoding='utf-8'));circles=[e for e in root.iter() if e.tag.endswith('circle') and e.attrib.get('fill')=='#16776d'];areas=[float(c.attrib['r'])**2/27**2 for c in circles];expected=[float(x) for x in mu+out if x>0];assert len(areas)==len(expected) and all(abs(a-b)<1e-12 for a,b in zip(areas,expected))
   text=[e.text for e in root.iter() if e.tag.endswith('text')];assert text.count('3/4')==2 and text.count('1/4')==2
   assert sum(e.tag.endswith('svg') for e in root.iter())==2 # one outer SVG, one central formal matrix
  states.append(dict(muA=str(p),payoff=f,result=str(v)))
for f in A.glob('*.svg'):ET.fromstring(f.read_text(encoding='utf-8'))
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,attrs):self.urls += [v for k,v in attrs if k in ['href','src'] and v]
broken=[];links=0
for f in P.rglob('*.html'):
 parser=Links();parser.feed(f.read_text(encoding='utf-8'))
 for url in parser.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or not u.path:continue
  path=unquote(u.path);dest=None
  for prefix,folder in [('/assets/',R/'assets'),('/book/',R/'dist'),('/shots/',O/'screenshots'),('/previous-shots/',O/'previous-screenshots')]:
   if path.startswith(prefix):dest=folder/path[len(prefix):];break
  if dest is None:dest=P/(path.lstrip('/') or 'index.html') if path.startswith('/') else f.parent/path
  if not dest.is_file():broken.append((f.relative_to(P).as_posix(),url))
  links+=1
assert not broken,broken[:10]
browser=json.loads((O/'browser-checks.json').read_text(encoding='utf-8'))
assert [len(browser[k]) for k in ['figure_checks','chapter_checks','print_checks']]==[8,16,4]
assert not any(x['overflow'] or x['broken_images'] for k in ['figure_checks','chapter_checks','print_checks'] for x in browser[k])
assert len(browser['kernel_states'])==24
for state in browser['kernel_states']:
 assert state['mu_pressed']=='true' and state['payoff_pressed']=='true' and state['graph_changed']
 expected=1+state['u'] if state['flip'] else 3-state['u'];assert state['output']==f'(μP)f = μ(Tf) = {expected}'
assert len(browser['clock_states'])==8 and all(x['pressed']=='true' and x['graph_changed'] for x in browser['clock_states'])
assert len(browser['details_checks'])==4 and all(x['open'] for x in browser['details_checks'])
shots=[]
for folder in ['screenshots','previous-screenshots']:
 for f in (O/folder).glob('*.jpg'):
  assert f.read_bytes().startswith(b'\xff\xd8\xff');shots.append(dict(file=f.relative_to(O).as_posix(),sha256=sha(f),bytes=f.stat().st_size,origin='e5ab29b2 preserved reference' if folder=='previous-screenshots' else 'actual browser HTTP viewport'))
(O/'screenshot-provenance.json').write_text(json.dumps(dict(method='Real viewport JPEG, no synthetic pages or stitching',files=shots),indent=2),encoding='utf-8',newline='\n')
result=dict(source_commit=reg['source_commit'],protected_paths=len(base),changed_old_files=0,revised_groups=['E22','E28'],adopted_and_protected=['E14','E30','E39'],E22_original_geometry='Exact original fragment retained in all eight clock states',E28_exact_states=states,E28_formal_matrix='One central 2×2 matrix with all four row-column entries',links=links,browser=dict(figures=8,chapters=16,static_pages=4,kernel_states=24,clock_states=8,details_checks=4),screenshots=sum(1 for f in (O/'screenshots').glob('*.jpg')),original_reference_screenshots=8,review='Revision awaiting author check; no expert final-review claim',printing='Static candidates viewed; native pagination/PDF fonts/physical print not verified',publication='No publication or push')
(O/'checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n');print(json.dumps(result,ensure_ascii=False))
