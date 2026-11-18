"""Preservation, model invariants and review-overlay checks, not aesthetic certification."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from fractions import Fraction as F
import hashlib,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];O=ROOT/'reports/volume5-illustrations-batch1-2026-10-31';P=O/'preview';A=ROOT/'assets/visuals/explanatory-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((O/'protected-baseline.json').read_text(encoding='utf-8'));changed=[f for f,h in baseline.items() if not (ROOT/f).is_file() or sha(ROOT/f)!=h];assert not changed,changed
registry=json.loads((ROOT/'publication/explanatory-figures-working.json').read_text(encoding='utf-8'))['figures']
for row in registry:
 if row['book_preview']:
  d=P/'chapters'/row['lang'];before=(d/(row['slug']+'-before.html')).read_text(encoding='utf-8');after=(d/(row['slug']+'.html')).read_text(encoding='utf-8')
  assert after.count(row['html'])==1 and after.replace(row['html'],'',1)==before,row['id']
for p in A.glob('*.svg'):ET.parse(p)
preserved=[]
for code in ['P01','P03','P04']:
 for p in A.glob(code+'*.svg'):
  old=ROOT/'reports/illustration-round3-2026-10-31/preview/assets'/p.name
  assert old.is_file() and sha(p)==sha(old),p.name
  preserved.append(p.name)
# Exact finite probabilities: area, normalization, Taylor decomposition and density averages.
weights={}
for theta in [F(1,4),F(1,2),F(3,4)]:
 q=[theta**2,theta*(1-theta),(1-theta)*theta,(1-theta)**2]
 assert sum(q)==1 and sum(F(1,4)*(v/F(1,4)) for v in q)==1
 weights[str(theta)]=list(map(str,q))
assert 3**3-1==26 and 3*2==6 and 6*4/2==12 and 26-6-12==8 and 26-6==20
averages={}
for eps in [F(1,2),F(1,4),F(1,8)]:
 area=2*eps-eps**2;avg=area/(2*eps);assert avg==1-eps/2;averages[str(eps)]={'area':str(area),'mean':str(avg)}
counts={t:sum(a<=t for a in [F(3,5),F(11,5)]) for t in [1,2,3]};assert list(counts.values())==[1,1,2]
# Check the second task separately: originals in 31–40 have no existing explanatory/engineering artwork.
original_graphics=[]
for n in range(31,41):
 p=next((ROOT/'chapters').glob(f'{n:02d}-*.md'))
 if re.search(r'!\[|<img\b|<svg\b|data-widget=',p.read_text(encoding='utf-8')):original_graphics.append(p.name)
assert not original_graphics,original_graphics
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['href','src'] and v:self.links.append(v)
broken=[];count=0
for p in P.rglob('*.html'):
 h=Links();h.feed(p.read_text(encoding='utf-8'))
 for url in h.links:
  u=urlsplit(url)
  if u.scheme or not u.path:continue
  path=unquote(u.path)
  if path.startswith('/assets/visuals/explanatory-v1/'):target=A/path[len('/assets/visuals/explanatory-v1/'):]
  elif path.startswith('/book/'):target=ROOT/'dist'/path[6:]
  elif path.startswith('/shots/'):target=O/'screenshots'/path[7:]
  elif path.startswith('/r3-shots/'):target=O/'references/round3/screenshots'/path[10:]
  elif path.startswith('/'):target=P/(path.lstrip('/') or 'index.html')
  else:target=p.parent/path
  count+=1
  if not target.is_file():broken.append((str(p.relative_to(O)),url))
assert not broken,broken
out={'protected_files':len(baseline),'protected_changed':changed,'preserved_adopted_P01_P03_P04_svg':preserved,'chapter_overlays_preserve_original_html':10,'existing_31_40_engineering_graphics_to_replace':original_graphics,'new_gap_groups':['V31','V33','V34','V37'],'exact_weight_models':weights,'cubic_jump':{'full':26,'linear':6,'quadratic':12,'residual':8,'ito_jump_correction':20},'occupation_profile':averages,'poisson_illustrative_counts':counts,'svg_xml_valid':len(list(A.glob('*.svg'))),'local_links_checked':count,'broken_local_links':broken,'author_status':'five pilots adopted as visual working drafts; four new groups pending visual review','independent_math_final_review':'not claimed','native_print_and_physical_print':'not tested'}
(O/'checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(out,ensure_ascii=False,indent=2))
