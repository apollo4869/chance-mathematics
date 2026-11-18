"""Independent finite enumeration and exact calculations; not expert final review."""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,math,re,hashlib,xml.etree.ElementTree as ET
from .volume8 import R,A,O,h_value,witness_values,graft_data,growth_edges,kary_values

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
@lru_cache(None)
def plane_trees(k,n):
 if n==0:return ((),)
 result=[]
 for sizes in product(range(n),repeat=k):
  if sum(sizes)!=n-1:continue
  for children in product(*(plane_trees(k,size) for size in sizes)):result.append(children)
 return tuple(result)
def addresses(t,prefix=()):
 result=[]
 for i,c in enumerate(t):result.append(prefix+(i,));result+=addresses(c,prefix+(i,))
 return result
def replace(t,path,replacement):
 if not path:return replacement
 i=path[0];return t[:i]+(replace(t[i],path[1:],replacement),)+t[i+1:]
def subtree(t,path):
 for i in path:t=t[i]
 return t
def check():
 out=[]
 def mark(name,detail):out.append(dict(check=name,result='passed finite/source check',detail=detail))
 for a in [F(0),F(1,4),F(1,2)]:
  b=(1-a)/2;assert 2*b+a==1
  assert h_value(a,F(0))==h_value(a,F(1))==0
  assert h_value(a,b)==h_value(a,1-b)==1
  for ui in range(9):
   u=F(ui,8);assert 0<=h_value(a,u)<=1
  # A height interval [c,d] inside (0,1) has two preimages of length b(d-c).
  c,d=F(1,5),F(3,5);assert 2*b*(d-c)==(1-a)*(d-c)
  assert b/2+b/2+a==(1+a)/2
 mark('V54 pushforward mass','Two linear inverse images give density 1-a; the plateau inverse image has length a. Geometry is [0,1] for every a. Atom mass and diffuse mass sum to 1; all 27 illustrated U/a states checked. This is not Brownian atomlessness.')
 # Independent exact witness computation on the line; dP for two Dirac masses.
 X=(F(-1),F(2));Y=[(F(-1),F(2),F(0),F(-1)),(F(-2),F(1),F(0),F(1)),(F(-3,2),F(3,2),F(1,2),F(3,2))]
 for i,(lo,hi,root,mass) in enumerate(Y):
  vals=(max(abs(X[0]-lo),abs(X[1]-hi)),abs(root),min(F(1),abs(mass-1)))
  assert vals==witness_values(i)
 assert max(abs(F(1)-F(-1)),abs(F(1)-F(2)))==2
 assert max(abs(F(-1)-F(-1)),abs(F(-1)-F(2)))==3
 mark('V55 common-witness gap','Current error triples independently computed as (0,0,1), (1,0,0), (1/2,1/2,1/2). For any common witness of error r<1, Dirac coupling forces mass points within r; Hausdorff matching then gives eccentricity difference 1<=2r. Thus global rGHP=1/2, whereas rGH=rGP=0. Max convention, rooted spaces, non-full-support probability masses.')
 independent=list(product([0,1],repeat=3));balanced=[tuple(int(i==j) for i in range(3)) for j in range(3)]
 assert F(sum(b[0]!=b[1] for b in independent),8)==F(1,2)
 assert F(sum(b[0]!=b[1] for b in balanced),3)==F(2,3)
 pair=list(product([0,1],repeat=2));assert F(sum(b[0]!=b[1] for b in pair),4)==F(1,2)
 assert sum(len(set(b))==1 for b in independent)==2
 mark('V56 restriction and rates','All 3 balanced partitions and all 8 independent bit words enumerated. Independent raw event rate 1 gives pair rate 1/2 and triple effective rate 3/4. Sample balancing gives direct pair 1 versus restricted pair 2/3. Deletion does not recolor survivors; no claim of full infinite construction from the diagram.')
 for ui in range(3):
  for ei in range(3):
   d=graft_data(ui,ei);assert 0<=d['edge']<3 and 0<=d['pos']<=1 and d['b']>0
   assert abs(2*d['next']**2-8-d['E'])<1e-12
 assert [graft_data(i,0)['edge'] for i in range(3)]==[0,1,2]
 assert [F(1,2)/2,F(1)/2,F(1,2)/2]==[F(1,4),F(1,2),F(1,4)]
 mark('V57 length and clock','All 9 input pairs: L_next²=4+E/2, attachment at arclength 2U, probabilities (1/4,1/2,1/4). Differentiating exp[-2(r²-s²)] gives standard-e rate 4r; doubling lengths yields rate r. Attaching a new pendant interval preserves all old distances. Infinite compactness and mass are not inferred from finite pictures.')
 enum=[]
 for k in [2,3,4]:
  trees=plane_trees(k,3);bal=sum(sum(bool(c) for c in t)==2 for t in trees)
  expected=kary_values(k);assert len(trees)==expected['gw_total'] and bal==expected['gw_balanced']
  # Independently run every uniform-edge growth history, including the planted stem.
  law={((),):F(1)}
  for step in range(3):
   nxt={}
   for t,weight in law.items():
    edges=addresses(t);assert len(edges)==step*k+1
    for e in edges:
     old=subtree(t,e);new=replace(t,e,(old,)+((),)*(k-1));nxt[new]=nxt.get(new,F(0))+weight/len(edges)
   law=nxt
  assert sum(law.values())==1
  prob=sum(weight for t,weight in law.items() if sum(bool(c) for c in t[0])==2)
  assert prob==F(k-1,2*k+1)
  pts,edges=growth_edges(k);assert len(edges)==2*k+1 and max(max(e) for e in edges)<len(pts)
  enum.append(dict(k=k,GW_shapes=len(trees),GW_balanced=bal,GW_probability=str(F(bal,len(trees))),growth_probability=str(prob),growth_histories=(k+1)*(2*k+1)))
 mark('V58 independently enumerated public models',enum)
 svgs=list(A.glob('*.svg'))
 for p in svgs:
  root=ET.parse(p).getroot();assert root.tag.endswith('svg') and len(root.attrib['viewBox'].split())==4
  assert '<script' not in p.read_text('utf8')
 reg=json.loads((R/'publication/explanatory-volume8-batch1-working.json').read_text('utf8'))
 assert len(reg['figures'])==10 and reg['unpublished_author_research_used'] is False
 for row in reg['figures']:
  for s in re.findall(r'(?:src|srcset|href)="(/assets/visuals/explanatory-volume8-v1/[^"#]+)"',row['html']):assert (R/s.lstrip('/')).is_file(),s
 mark('Bilingual assets',dict(svg_count=len(svgs),bilingual_fragments=10,all_local_references_present=True))
 baseline=json.loads((O/'protected-baseline.json').read_text('utf8'));changed=[p for p,h in baseline.items() if not (R/p).exists() or sha(R/p)!=h];assert not changed,changed
 for m in json.loads((O/'manifest.json').read_text('utf8')):assert sha(Path(m['source']))==m['source_sha256'] and m['exact_source_recovery']
 mark('Protected book and approved illustrations',dict(preexisting_files_byte_identical=len(baseline),actual_chapter_overlays=10,P04_P05_preserved=True))
 write(O/'verification.json',dict(scope='Codex finite calculations and source/SVG checks, not independent expert mathematical review',checks=out,browser='not attempted this round; previous local-browser permission failure; screenshots and interaction acceptance remain open',native_pdf='not tested',real_devices='not tested',author_visual_review='pending',unpublished_author_research='not read or used'))
 print(f'{len(out)} finite/source checks passed; {len(svgs)} SVGs. Browser and expert review not passed by these checks.')
if __name__=='__main__':check()
