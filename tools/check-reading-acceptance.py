"""Inventory real generated HTML and resolve resources. This is not browser QA."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlsplit,unquote
from collections import Counter,defaultdict
import csv,hashlib,json,re,posixpath
R=Path(__file__).resolve().parents[1];SITE=R/'work/reading-acceptance/site';O=R/'reports/full-book-reading-2026-11-07'
FILES={p.relative_to(SITE).as_posix():p for p in SITE.rglob('*') if p.is_file()}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')

class ReadHTML(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.ids=[];self.tags=Counter();self.refs=[];self.visuals=[];self.headings=[];self.active_heading=None;self.heading_text=[];self.current_heading='';self.formulas=0;self.heading_level=None;self.canvases=0;self.inline_explanatory_svg=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags[tag]+=1;cls=a.get('class','').split()
  if a.get('id'):self.ids.append(a['id'])
  if 'formula' in cls:self.formulas+=1
  if tag in {'h1','h2','h3','h4'}:self.active_heading=tag;self.heading_text=[]
  if tag=='canvas':self.canvases+=1
  if tag=='svg' and a.get('class') not in ['formula-svg']:self.inline_explanatory_svg+=1
  for attr in ['src','href','srcset','poster']:
   if attr not in a:continue
   values=[a[attr]]
   if attr=='srcset' and not a[attr].startswith('data:'):values=[x.strip().split()[0] for x in a[attr].split(',') if x.strip()]
   for value in values:self.refs.append(dict(tag=tag,attr=attr,url=value))
  if tag in {'img','canvas'}:self.visuals.append(dict(kind=tag,id=a.get('id',''),src=a.get('src',''),alt=a.get('alt',''),heading=self.current_heading))
 def handle_endtag(self,tag):
  if self.active_heading==tag:
   self.current_heading=''.join(self.heading_text).strip();self.headings.append(self.current_heading);self.active_heading=None
 def handle_data(self,text):
  if self.active_heading:self.heading_text.append(text)

def resolve(page,url):
 if not url or url.startswith(('data:','mailto:','javascript:','tel:')):return None
 u=urlsplit(urljoin('http://reading.local/'+page,url))
 if u.netloc!='reading.local':return None
 rel=posixpath.normpath(unquote(u.path)).lstrip('/')
 if rel in {'.',''}:rel='index.html'
 if rel not in FILES and rel+'/index.html' in FILES:rel+='/index.html'
 p=SITE/rel
 return p,u.fragment

def run():
 reg=json.loads((O/'accepted-figures.json').read_text('utf8'))['figures'];chapter_rows=[];visual_rows=[];resources=defaultdict(set);missing=[];badanchors=[];duplicates=[];ids_cache={}
 pages=sorted(SITE.rglob('*.html'))
 # Read each actual HTML page once; no source re-rendering.
 parsed={}
 for p in pages:
  q=ReadHTML();q.feed(p.read_text('utf8'));parsed[p]=q;ids_cache[p]=set(q.ids)
 for p,q in parsed.items():
  rel=p.relative_to(SITE).as_posix()
  # Metadata/archive pages are inventoried but the QA gate concerns real reader pages.
  is_reader=rel.startswith(('chapters/','en/chapters/','print/','volumes/','en/volumes/')) or rel in {'index.html','en/index.html','book-closing.html','en/book-closing.html'}
  if not is_reader:continue
  counts=Counter(q.ids);dups=[i for i,n in counts.items() if n>1]
  if dups:duplicates.append(dict(page=rel,ids=dups))
  for x in q.refs:
   found=resolve(rel,x['url'])
   if found is None:continue
   target,anchor=found
   if target.relative_to(SITE).as_posix() not in FILES:
    # The local static server intentionally does not implement analytics/admin APIs.
    missing.append(dict(page=rel,tag=x['tag'],attribute=x['attr'],url=x['url'],target=target.relative_to(SITE).as_posix()))
   elif x['tag'] in {'img','source','script','link','use','image'}:
    resources[target.relative_to(SITE).as_posix()].add(rel)
   if anchor and target in ids_cache and anchor not in ids_cache[target]:badanchors.append(dict(page=rel,url=x['url'],target=target.relative_to(SITE).as_posix(),fragment=anchor))
  if re.fullmatch(r'(en/)?chapters/[^/]+\.html',rel):
   lg='en' if rel.startswith('en/') else 'zh';slug=p.stem;expected=[r for r in reg if r['slug']==slug and r['lang']==lg]
   for row in expected:assert q.ids.count('visual-'+row['id'])==1,(rel,row['id'])
   chapter_rows.append(dict(chapter=int(slug[:2]),lang=lg,page=rel,headings=q.headings,adopted_groups=[r['id'] for r in expected],formulas=q.formulas,images=q.tags['img'],canvas=q.canvases,duplicate_ids=dups,metadata_at_footer='data-chapter-publication="footer"' in p.read_text('utf8')))
   for v in q.visuals:
    rr=resolve(rel,v['src']) if v['src'] else None
    visual_rows.append(dict(chapter=int(slug[:2]),lang=lg,page=rel,**v,resource=rr[0].relative_to(SITE).as_posix() if rr else '',resource_exists=rr[0].relative_to(SITE).as_posix() in FILES if rr else None))
 asset_rows=[dict(path=n,bytes=(SITE/n).stat().st_size,sha256=sha(SITE/n),used_by=sorted(users)) for n,users in sorted(resources.items())]
 save(O/'chapter-inventory.json',chapter_rows);save(O/'visual-resource-inventory.json',dict(visuals=visual_rows,resources=asset_rows))
 save(O/'link-and-resource-check.json',dict(reader_pages_checked=sum(1 for p in parsed if p.relative_to(SITE).as_posix().startswith(('chapters/','en/chapters/','print/','volumes/','en/volumes/'))),all_html_parsed=len(parsed),missing=missing,missing_anchors=badanchors,duplicate_ids=duplicates,scope='HTML/resources only; browser layout, interaction, devices and PDF are separate'))
 with (O/'chapter-inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f,lineterminator='\n');w.writerow(['chapter','language','page','adopted groups','formula count','images','canvas','metadata at footer'])
  for x in chapter_rows:w.writerow([x['chapter'],x['lang'],x['page'],', '.join(x['adopted_groups']),x['formulas'],x['images'],x['canvas'],x['metadata_at_footer']])
 with (O/'visual-resources.csv').open('w',encoding='utf-8-sig',newline='') as f:
  cols=['chapter','lang','page','heading','kind','id','alt','src','resource','resource_exists'];w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(visual_rows)
 print(json.dumps(dict(chapter_pages=len(chapter_rows),adopted_groups=len({r['id'] for r in reg}),visual_records=len(visual_rows),referenced_resources=len(asset_rows),missing_resources=len(missing),missing_anchors=len(badanchors),duplicate_id_pages=len(duplicates)),ensure_ascii=False))

if __name__=='__main__':run()
