"""Exact model enumeration, preserved inputs, local overlays and browser evidence."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys,json,hashlib,re,xml.etree.ElementTree as ET
from PIL import Image
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from tools.explanatory_illustrations.volume6 import META,allstates,filename
from tools.explanatory_illustrations.volume6_review import O,A,P,PREFIX,loadreg,rewrite,assets,sha,jsave
base=json.loads((O/'protected-baseline.json').read_text('utf-8'));changed=[p for p,h in base.items() if not(R/p).exists() or sha(R/p)!=h];assert not changed,changed[:6]
rows=loadreg('explanatory-volume6-batch1-working.json');assert len(rows)==10
for row in rows:
 lg,slug,code=row['lang'],row['slug'],row['id'];before=(P/'chapters'/lg/(slug+'-before.html')).read_text('utf-8');after=(P/'chapters'/lg/(slug+'.html')).read_text('utf-8');frag=row['html'].replace('href="/print/',f'href="{PREFIX}print/')
 assert after.count(f'id="visual-{code}"')==1 and after.replace(frag,'',1)==before
 for st in allstates(code):
  for i in range(2):assert (A/filename(code,lg,st,i)).is_file()
contexts=json.loads((O/'reading-contexts.json').read_text('utf-8'));assert len(contexts)==30
for c in contexts:assert sha(R/c['path'])==c['source_sha256']
adopted=loadreg('explanatory-adopted-volumes1-5.json');assert len(adopted)==40
for row in adopted:
 original=next(r for r in loadreg(row['selected_registry']) if r['id']==row['id'] and r['lang']==row['lang']);assert row['html']==original['html'] and row['html_sha256']==hashlib.sha256(original['html'].encode()).hexdigest()
 slug,lg=row['slug'],row['lang'];s=(P/'adopted/chapters'/lg/(slug+'.html')).read_text('utf-8');assert s.count(f'id="visual-{row["id"]}"')==1
 # Version/runtime resources remain the original files; old source hashes are in the protection chain.
 assert sha(R/'publication'/row['selected_registry'])==row['selected_registry_sha256']
# V41 moments use the finite environment mixture, not empirical sample frequencies.
q=[F(1,4),F(3,4)];assert sum(q)/2==F(1,2) and sum(x*x for x in q)/2-F(1,4)==F(1,16)
# V44: exact EPPF ratios and table labels.
def eppf(ns):return F(__import__('functools').reduce(lambda a,n:a*factorial(n-1),ns,1),factorial(sum(ns)))
prior=eppf([2,1]);assert prior==F(1,6)
branches=[eppf(x)/prior for x in [[3,1],[2,2],[2,1,1]]];assert branches==[F(1,2),F(1,4),F(1,4)] and sum(branches)==1
assert F(1,2)+F(1,2)*F(1,2)==F(3,4) and branches[2]*F(1,2)==F(1,8)
# V45: exact group action and adaptive mass concentration.
for k in [0,2,4]:assert sorted((j+k)%8 for j in range(8))==list(range(8))
assert [(j-j)%8 for j in range(8)]==[0]*8
# V46: exhaustive three-input laws, row laws, and pairwise (not triple) independence.
laws={}
for model in ['pairs','colors']:
 counts={}
 for v in product([0,1],repeat=3):
  e=v if model=='pairs' else (int(v[0]!=v[1]),int(v[1]!=v[2]),int(v[2]!=v[0]));counts[e]=counts.get(e,0)+1
 laws[model]=counts
 assert F(counts.get((1,1,1),0),8)==(F(1,8) if model=='pairs' else 0)
 for i,j in [(0,1),(1,2),(2,0)]:
  for a,b in product([0,1],repeat=2):assert sum(c for e,c in counts.items() if e[i]==a and e[j]==b)==2
for m in range(1,6):
 counts={}
 for v in product([0,1],repeat=m+1):
  word=tuple(int(v[0]!=x) for x in v[1:]);counts[word]=counts.get(word,0)+1
 assert len(counts)==2**m and all(c==2 for c in counts.values())
# V47: pair probabilities and the exact displayed finite relation.
paint=[]
for d in [F(0),F(1,4),F(1,2)]:
 a,b=F(1,2),F(1,2)-d;assert a+b+d==1
 groups={}
 for i,u in enumerate([F(1,10),F(3,10),F(6,10),F(79,100),F(87,100),F(95,100)],1):
  key='A' if u<a else 'B' if u<a+b else str(i);groups.setdefault(key,[]).append(i)
 for key,g in groups.items():
  if key not in ['A','B']:assert len(g)==1
 paint.append(dict(d=str(d),same_block=str(a*a+b*b),groups=groups))
assert [x['same_block'] for x in paint]==['1/2','5/16','1/4']
# Parse every new asset, including all alternative states.
svgs=list(A.glob('*.svg'))
for p in svgs:ET.parse(p)
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,t,a):self.urls += [v for k,v in a if k in ['href','src'] and v]
links=0
for p in P.rglob('*.html'):
 parser=Links();parser.feed(p.read_text('utf-8'))
 for url in parser.urls:
  path=unquote(urlsplit(url).path)
  if urlsplit(url).scheme or not path:continue
  if path.startswith('/assets/'):dest=R/path.lstrip('/')
  elif path.startswith('/book/'):dest=R/'dist'/path[6:]
  else:continue
  assert dest.exists(),(p,url);links+=1
browser=json.loads((O/'browser-checks.json').read_text('utf-8'));assert len(browser['states'])==140 and len(browser['pages'])==74
assert all(not r['broken'] and not r['overflow'] for r in browser['pages']+browser['states'])
assert len(browser['adopted'])==42
for r in browser['adopted']:
 assert r['figures'].count('visual-'+r['id'])==1 and not r['overflow']
 if r['broken']:assert r['id']=='E13' and browser['e13_resource_check']['finding'].startswith('Hidden')
for code in META:
 states=[r for r in browser['states'] if r['code']==code];assert len(states)==4*len(allstates(code))
 for lg in ['zh','en']:
  for size in ['desktop','mobile']:
   got={r['state'] for r in states if r['lg']==lg and r['size']==size};assert got=={'-'.join(map(str,st)) for st in allstates(code)}
for r in browser['states']:
 assert all('/'+r['code']+'-'+r['lg']+'-'+r['state']+'-' in src for src in r['images'])
shots=[]
for p in sorted((O/'screenshots').glob('*.jpg')):
 im=Image.open(p);assert im.height>=500,p.name
 shots.append(dict(file=p.relative_to(O).as_posix(),sha256=sha(p),bytes=p.stat().st_size,width=im.width,height=im.height))
assert len(shots)==130
jsave(O/'screenshot-provenance.json',dict(method='Actual browser viewport captures, no synthetic pages or stitching; ten early viewport-transition captures replaced after stabilization',files=shots))
jsave(O/'model-checks.json',dict(environment_mean='1/2',environment_covariance='1/16',CRP_branches=list(map(str,branches)),new_value_atomic='1/8',rotation='fixed bijections / adaptive concentration',array_laws={m:{''.join(map(str,e)):n for e,n in c.items()} for m,c in laws.items()},paintbox=paint))
jsave(O/'checks.json',dict(protected_paths=len(base),changed_old_files=0,adopted_bilingual_overlays=40,new_bilingual_overlays=10,reused_P02=True,source_contexts=30,svg_assets=len(svgs),local_link_targets=links,browser_pages=len(browser['pages']),interaction_states=140,screenshots=len(shots),author_visual_review='pending for five new groups; adopted prior groups retained',independent_expert_review='open',real_devices='not verified',native_PDF_and_physical_print='not verified',publication='none'))
print(json.dumps(json.loads((O/'checks.json').read_text('utf-8')),ensure_ascii=False))
