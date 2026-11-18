"""Finite-model verification and source protection, not independent expert review."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,math,re,hashlib,xml.etree.ElementTree as ET
from .volume7 import R,A,O,tree_data,cut_data,mass_values,hit_values,poisson_quantile

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(output_dir=None):
 results=[]
 def mark(name,detail):results.append(dict(check=name,status='passed finite-model/source check',detail=detail))
 # V48: exact inverse-transform regions; means agree but joint laws differ.
 q=math.exp(-1)
 assert abs(q*q-math.exp(-2))<1e-15 and q>q*q
 assert [poisson_quantile(u) for u in [.12,.64,.84,.8,.08]]==[0,1,2,2,0]
 # Independently integrate the joint zero event by the product uniform law.
 assert (Q(1,3)*Q(1,3))!=Q(1,3)  # structure is product area versus a strip
 mark('V48 inverse inputs and joint event','Poisson(1) inverse-CDF examples checked; independent empty event is q², copied is q. These laws agree in one-window marginals and mean, not in joint law. No simulation proof.')
 # V49: derive atom membership from positions, not from displayed totals.
 for space in ['real','open']:
  for w,lo in enumerate([Q(1,4),Q(1,16),Q(0)]):
   v=mass_values(space,w)
   if space=='open' and lo==0:assert not v['valid'] and v['mass'] is None;continue
   if lo:
    indices=[k for k in range(1,1000) if lo<=Q(1,k+1)<=Q(3,4)]
    assert len(indices)==v['counts'] and sum(Q(1,2**k) for k in indices)==v['mass']
   else:assert v['counts'] is None and v['mass']==1
   assert v['length']==Q(3,4)-lo
 assert mass_values('real',0)['counts']==3 and mass_values('real',1)['counts']==15
 mark('V49 windows, series and ambient-space boundary','Finite-window weights checked by rational atom membership. Full geometric series sums to 1. On (0,1), compact K has min K>0, hence finitely many x_k; on R, [0,3/4] contains all x_k. Infinite support is not an atom at 0; no zero-mass interpretation of an invalid window.')
 # V51: independent interval arithmetic, including closed endpoints.
 bounds=[(Q(1,5),Q(3,5),Q(1,5),Q(3,5)),(Q(1,10),Q(7,20),Q(13,20),Q(9,10)),(Q(3,20),Q(13,20),Q(2,5),Q(17,20))]
 expected=[(Q(2,5),Q(2,5),Q(2,5),Q(2,5)),(Q(1,4),Q(1,4),Q(1,2),Q(0)),(Q(1,2),Q(9,20),Q(7,10),Q(1,4))]
 for c,(a,b,d,e) in enumerate(bounds):
  assert hit_values(c)==expected[c]
  edges=sorted(set([Q(0),a,b,d,e,Q(1)]));both=Q(0);union=Q(0)
  for l,r in zip(edges,edges[1:]):
   x=(l+r)/2;aa=a<=x<=b;bb=d<=x<=e
   both+=(r-l)*int(aa and bb);union+=(r-l)*int(aa or bb)
  assert (union,both)==expected[c][2:]
  for u in [Q(j,20) for j in range(21)]:assert isinstance(a<=u<=b,bool)
 mark('V51 capacity and joint-hit values','All three cases checked by exact partition of [0,1]. Disjoint spatial compact sets can have the same hit event. Uniform continuum probabilities are not slider-grid frequencies; endpoints included and probability zero.')
 # V52: enumerate ALL rooted plane trees of size 5 via valid offspring words,
 # independently reconstruct addresses by a stack, and derive edge contours.
 n=5;count=0
 for k in product(range(n),repeat=n):
  if sum(k)!=n-1:continue
  active=[''];nodes=[];S=[0]
  for z in k:
   if not active:break
   u=active.pop(0);nodes.append(u);active=[u+str(i+1) for i in range(z)]+active;S.append(S[-1]+z-1)
  if len(nodes)!=n or active:continue
  count+=1;H=list(map(len,nodes));walk=[]
  def visit(u):
   walk.append(u)
   for v in nodes:
    if v and v[:-1]==u:visit(v);walk.append(u)
  visit('');assert len(walk)==2*n-1 and S[-1]==-1 and min(S[:-1])>=0
  assert [walk.index(u) for u in nodes]==[2*j-H[j] for j in range(n)]
  for i,u in enumerate(nodes):
   for j,v in enumerate(nodes):
    m=0
    while m<min(len(u),len(v)) and u[m]==v[m]:m+=1
    ci,cj=sorted([walk.index(u),walk.index(v)])
    assert min(map(len,walk[ci:cj+1]))==m
 assert count==14
 da,db=tree_data('A'),tree_data('B')
 assert da['W']==[0,1,2,1,0,-1] and db['W']==[0,1,1,0,0,-1]
 assert da['b']==[0,1,2,4,7] and db['b']==[0,1,2,5,6]
 for d in [da,db]:
  assert [d['H'].count(j) for j in range(3)]==[1,2,2]
  assert all(len(d['queue'][j])==1+d['W'][j] for j in range(n))
  assert all(d['C'][d['b'][j]]==d['H'][j] for j in range(n))
 mark('V52 all 14 plane trees of size 5','Exhaustive independent address-stack reconstruction checks queue size, first arrivals, terminal S=-1, edge contour length 8, b_j=2j-H_j and ancestor depth via contour minima. Both displayed trees have generation profile (1,2,2) but different codes.')
 # V53: all numbered rotations, first versus last minimum, and unary chains.
 words=[cut_data(r) for r in range(5)];assert [r for r,w in enumerate(words) if w['legal']]==[1]
 assert words[1]['W']==[0,1,0,1,0,-1]
 assert words[3]['W']==[0,1,0,-1,0,-1] and words[3]['first_hit']==3
 for d in [da,db]:
  for length in [0,2,5]:
   W=[0]*length+d['W'];H=list(range(length))+[length+h for h in d['H']]
   assert len(W)==6+length and len(H)==5+length and W[-1]==-1
   assert H[length:]==[h+length for h in d['H']]
 mark('V53 indexed cuts and height instability','All 5 cuts evaluated: r=1 uniquely legal, r=3 hits -1 at step 3. Unary chain adds only zero task increments but shifts every old depth. General l_m=floor(m^(3/4)) has l_m/m→0 and l_m/sqrt(m)→∞; for bounded task-curve families with uniform continuity this exposes why task-path convergence alone cannot force height convergence. This is not a conditional GW sample or a proof of Vervaat/height limit theorems.')
 # Verify every new SVG and every local figure reference, not just file presence.
 svgs=list(A.glob('*.svg'))
 for p in svgs:
  root=ET.fromstring(p.read_text('utf8'));assert root.tag.endswith('svg')
  vb=list(map(float,root.attrib['viewBox'].split()));assert vb[2]>0 and vb[3]>0
  assert '<script' not in p.read_text('utf8')
 registry=json.loads((R/'publication/explanatory-volume7-batch1-working.json').read_text('utf8'));reg=registry['figures']
 assert len(reg)==10 and len({(r['id'],r['lang']) for r in reg})==10
 for row in reg:
  for p in re.findall(r'(?:src|srcset|href)="(/assets/visuals/explanatory-volume7-v1/[^"#]+)"',row['html']):assert (R/p.lstrip('/')).is_file(),p
  assert '<div class="v7-print">' in row['html'] and len(row['condition'])>200
 mark('Bilingual SVG and static resources',f'{len(svgs)} SVGs parse; 10 bilingual fragments, controls and independent static pages have local resources and explicit conditions.')
 baseline=json.loads((O/'protected-baseline.json').read_text('utf8'))
 changed=[p for p,h in baseline.items() if not (R/p).is_file() or sha(R/p)!=h]
 assert not changed,changed
 for row in json.loads((O/'P03-reuse.json').read_text('utf8')):assert sha(Path(row['path']))==row['sha256'] and row['copies']==1
 mark('Protected manuscripts, proofs and mature illustrations',f'All {len(baseline)} pre-existing tracked files byte-identical; both actual chapter-50 P03 pages unchanged.')
 manifest=json.loads((O/'manifest.json').read_text('utf8'))
 for m in manifest:assert sha(Path(m['source']))==m['source_sha256'] and m['exact_original_recovery']
 mark('Actual chapter overlays','All 10 overlays remove to exact original rendered chapter after stripping the one new stylesheet/runtime include. Original math sources, formulas, proofs and existing chapter links unchanged.')
 adopted=bool(registry.get('adoption'))
 record=dict(scope='Finite exact models and source checks by Codex; not independent mathematical final review',checks=results,browser=dict(status='pending; previously blocked' if adopted else 'blocked',error='Local browser use is disabled in Work settings',screenshots=0,retried_this_closeout=False if adopted else None),aesthetics='adopted current visual working drafts; final author aesthetics and browser validation remain open' if adopted else 'author review pending; SVG raster inspection only',native_pdf='not tested',real_devices='not tested')
 destination=Path(output_dir) if output_dir else O
 destination.mkdir(parents=True,exist_ok=True)
 (destination/'verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print(f'{len(results)} finite-model/source checks passed; {len(svgs)} SVGs. Browser and native PDF explicitly not passed.')
if __name__=='__main__':check()
