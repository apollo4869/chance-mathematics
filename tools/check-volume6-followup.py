"""Finite algebra, protected sources, visual geometry and actual capture auditing."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys,json,hashlib,re,xml.etree.ElementTree as ET
from PIL import Image
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from tools.explanatory_illustrations.volume6_followup import O,A,P,PREFIX,FULL,restrict,record
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
base=json.loads((O/'protected-baseline.json').read_text('utf-8'));changed=[p for p,h in base.items() if not (R/p).is_file() or sha(R/p)!=h];assert not changed,changed[:8]
rows=json.loads((R/'publication/explanatory-volume6-batch2-working.json').read_text('utf-8'))['figures'];previous=json.loads((R/'publication/explanatory-volume6-batch1-working.json').read_text('utf-8'))['figures'];assert len(rows)==14
for code in ['V41','V45','V46','V47']:
 for lg in ['zh','en']:
  new=next(r for r in rows if r['id']==code and r['lang']==lg);old=next(r for r in previous if r['id']==code and r['lang']==lg);assert new['html']==old['html'] and new['condition']==old['condition']
for lg in ['zh','en']:
 r=next(x for x in rows if x['id']=='V44' and x['lang']==lg);old=next(x for x in previous if x['id']=='V44' and x['lang']==lg)
 stripped=re.sub(r'<div class="v44-mobile-summary">.*?</small></div>','',r['html'],count=1,flags=re.S);assert stripped==old['html'];assert r['condition']==old['condition']
# Exact split kernel and lawful finite paths.
for x in ['a','b']:
 p=[F(1,2)*F(1,2)+F(1,2)*int(x==z) for z in ['a','b']];assert p==([F(3,4),F(1,4)] if x=='a' else [F(1,4),F(3,4)])
 for r in [0,1,2]:
  coins,states,ends=record(x,r);assert sum(coins)==3 and ends==[r+1,5,8]
  assert all(states[j+1]==states[j] for j,c in enumerate(coins) if not c)
  left=list(range(ends[0],ends[1]));right=list(range(ends[1],ends[2]));assert not set(left)&set(right) and ends[1] not in left and ends[1] in right
# P(L=l,Z=z)=2^(-l-1), from nu; exact truncated sums plus exact tail.
for m in [1,8,20]:assert sum(F(1,2**l) for l in range(1,m+1))+F(1,2**m)==1
# Generate all finite partitions without an external coalescent black box.
def partitions(n):
 if n==0:return [()]
 out=[]
 for p in partitions(n-1):
  out.append(p+((n,),))
  for j in range(len(p)):out.append(tuple(p[k]+((n,) if k==j else ()) for k in range(len(p))))
 return out
def merge(p,i,j):return tuple(sorted([p[k] for k in range(len(p)) if k not in [i,j]]+[tuple(sorted(p[i]+p[j]))],key=lambda b:b[0]))
def rates(p):
 d={}
 for i,j in combinations(range(len(p)),2):q=merge(p,i,j);d[q]=d.get(q,0)+1
 return d
p4=partitions(4);assert len(p4)==15
verified=0
for p in p4:
 for n in [2,3]:
  small=restrict(p,n);push={};invisible=0
  for target,v in rates(p).items():
   rr=restrict(target,n)
   if rr==small:invisible+=v
   else:push[rr]=push.get(rr,0)+v
  assert push==rates(small);q=len(p)*(len(p)-1)//2;v=len(small)*(len(small)-1)//2;assert q==v+invisible;verified+=1
projection_models=[]
for n in [2,3]:
 rr=[restrict(p,n) for p in FULL]
 if n==2:assert rr[0]==rr[1]==rr[2] and rr[2]!=rr[3]
 else:assert rr[0]==rr[1] and rr[1]!=rr[2]!=rr[3]
 for step,p in enumerate(FULL):
  b=len(p);c=len(rr[step]);projection_models.append(dict(n=n,step=step,total_rate=b*(b-1)//2,visible_rate=c*(c-1)//2,restriction=rr[step]))
# Reversible overlays, preserving adopted paintbox in the shared chapter.
for r in rows:
 code,lg,slug=r['id'],r['lang'],r['slug'];after=(P/'chapters'/lg/(slug+'.html')).read_text('utf-8');assert after.count('id="visual-'+code+'"')==1
 if code in ['V42','V47C','V44']:
  before=(P/'chapters'/lg/(slug+'-before.html')).read_text('utf-8');frag=r['html'].replace('href="/print/',f'href="{PREFIX}print/')
  if code=='V44':
   old=next(x for x in previous if x['id']==code and x['lang']==lg);assert after.replace(frag,old['html'].replace('href="/print/',f'href="{PREFIX}print/'),1)==before
  else:assert after.replace(frag,'',1)==before
 if code=='V47C':assert after.count('id="visual-V47"')==1
contexts=json.loads((O/'reading-contexts.json').read_text('utf-8'));assert len(contexts)==14
for c in contexts:assert sha(R/c['path'])==c['sha256']
svgs=list(A.glob('*.svg'))
for p in svgs:ET.parse(p)
# Reuse only this round's decoded entries whose exact bytes are unchanged.
cache={}
if (O/'screenshot-audit.json').exists():
 d=json.loads((O/'screenshot-audit.json').read_text('utf-8'));cache={x['file']:x for group in ['old','new'] for x in d[group]}
# Detect actual pure-black rectangles and deficient captures, not merely file existence.
def inspect(p,largest=False):
 key=p.relative_to(O).as_posix();prior=cache.get(key)
 if prior and prior['sha256']==sha(p):return {k:v for k,v in prior.items() if k!='file'}
 im=Image.open(p).convert('RGB');w,h=im.size;pixels=list(im.getdata());black=[max(v)<=12 for v in pixels];count=sum(black);dark=sum(max(v)<160 for v in pixels);area=0;rect=None
 if largest and count:
  hist=[0]*w
  for y in range(h):
   for x in range(w):hist[x]=hist[x]+1 if black[y*w+x] else 0
   stack=[]
   for x in range(w+1):
    v=hist[x] if x<w else 0;start=x
    while stack and stack[-1][1]>v:
     at,hh=stack.pop();a=(x-at)*hh
     if a>area:area=a;rect=[at,y-hh+1,x-at,hh]
     start=at
    if not stack or stack[-1][1]<v:stack.append((start,v))
 return dict(width=w,height=h,near_black_pixels=count,largest_black_rectangle=rect,largest_black_area=area,foreground_dark_pixels=dark,sha256=sha(p),bytes=p.stat().st_size)
old=[];new=[]
for p in sorted((O/'references').glob('*.jpg')):old.append(dict(file=p.relative_to(O).as_posix(),**inspect(p,True)))
for p in sorted((O/'screenshots').glob('*.jpg')):
 m=inspect(p);assert m['height']>=500 and m['foreground_dark_pixels']>1500,(p,m);assert m['near_black_pixels']<1000,(p,'black capture',m);new.append(dict(file=p.relative_to(O).as_posix(),**m))
assert len(old)==6 and sum(x['largest_black_area']>10000 for x in old)==3
assert len(new)==78
# The screenshot count is fixed only after all requested captures have been collected.
if (O/'browser-checks.json').exists():
 b=json.loads((O/'browser-checks.json').read_text('utf-8'));assert len(b['states'])==104
 assert all(not x['overflow'] and not x['broken'] for x in b['pages']+b['states'])
 for x in b['states']:
  if x['code']=='V44':assert x['summary']==('1/8' if x['requested'][0]=='atomic' else '1/4')
  else:assert x['state']=='-'.join(map(str,x['requested']))
 for x in b['pages']:
  if x['code']=='V44' and x['kind']=='figure':
   assert x['summary_visible']==(x['size']=='mobile')
   if x['size']=='mobile':assert 0<x['summary_bottom']<x['height']
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):self.urls.extend(v for k,v in a if k in ['href','src'] and v)
links=0
for p in P.rglob('*.html'):
 parser=Links();parser.feed(p.read_text('utf-8'))
 for u in parser.urls:
  v=urlsplit(u)
  if v.scheme or not v.path:continue
  path=unquote(v.path)
  if path.startswith('/assets/'):dest=R/path[1:]
  elif path.startswith('/book/'):dest=R/'dist'/path[6:]
  else:continue
  assert dest.exists(),(p,u);links+=1
save(O/'screenshot-audit.json',dict(old=old,new=new,scope='Six previous default desktop screenshots plus every current capture; actual pixel/black-rectangle and foreground checks, complemented by browser and visual inspection'))
save(O/'model-checks.json',dict(kernel_rows=[['3/4','1/4'],['1/4','3/4']],regeneration_endpoints=[[r+1,5,8] for r in [0,1,2]],kingman_partitions=15,projection_rate_checks=verified,displayed_states=projection_models))
save(O/'checks.json',dict(protected_paths=len(base),changed_old_files=0,new_groups=['V42','V47C'],V44='mobile summary only; old structure retained',old_black_default_captures=3,reacquired_defaults=6,new_capture_count=len(new),new_capture_black_rectangles=0,interaction_states=104,local_link_targets=links,author_new_candidate_review='pending',independent_expert_math_final='open',real_devices='not verified',native_PDF='not verified',publication='none'))
print(json.dumps(json.loads((O/'checks.json').read_text('utf-8')),ensure_ascii=False))
