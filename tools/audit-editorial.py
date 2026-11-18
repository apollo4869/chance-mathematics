"""Read-only English prose triage and generated-HTML link audit. Never edits sources."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlsplit,unquote
import argparse,hashlib,json,re,collections
ROOT=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def mask(text):
 patterns=[r'```[\s\S]*?```',r'`[^`\n]*`',r'\\\[[\s\S]*?\\\]',r'\\\([\s\S]*?\\\)',r'https?://[^\s<>)]*',r'\]\([^)]*\)',r'<[^>]+>']
 for p in patterns:text=re.sub(p,lambda m:''.join('\n' if c=='\n' else ' ' for c in m[0]),text)
 return text
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=True);self.ids=collections.Counter();self.links=[];self.formulas=[];self.feed(s)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids[a['id']]+=1
  if 'formula' in a.get('class','').split():self.formulas.append(a.get('data-tex',''))
  for attr in ['href','src','poster']:
   if a.get(attr):self.links.append((tag,attr,a[attr]))
def audit(output,site):
 findings=[];scanned=[]
 rules=[('chapter_spacing',r'\bChapters?\d+\b'),('inline_math_left_spacing',r'[A-Za-z]\\\('),('inline_math_right_spacing',r'\\\)[A-Za-z]'),('prose_number_join',r'\b[A-Za-zÀ-ž]{3,}\d+\b'),('punctuation_spacing',r'[,;:][A-Za-z]{2,}'),('markdown_artifact',r'\b(?:MATH(?:INLINE|BLOCK)TOKEN\d+END|nullnull)\b')]
 for p in sorted((ROOT/'chapters-en').glob('*.md')):
  text=p.read_text('utf8');safe=mask(text);scanned.append(p.relative_to(ROOT).as_posix())
  for kind,pattern in rules:
   # Inline-math delimiters must remain visible, while the formula body is masked.
   probe=re.sub(r'\\\(([\s\S]*?)\\\)',lambda m:r'\('+(' ' * len(m[1]))+r'\)',text) if kind.startswith('inline_math') else safe
   for m in re.finditer(pattern,probe):
    line=text.count('\n',0,m.start())+1
    findings.append({'file':scanned[-1],'line':line,'kind':kind,'match':text[m.start():m.end()],'context':text[max(0,m.start()-60):min(len(text),m.end()+85)].replace('\n',' '),'classification':'MANUAL_TRIAGE_NOT_AUTOMATIC_CORRECTION'})
 assert len(scanned)==58
 pages={p.relative_to(site).as_posix():Page(p.read_text('utf8')) for p in site.rglob('*.html')}
 missing=[];citations=[];duplicates=[];checked=0
 for rel,page in pages.items():
  duplicates.extend({'page':rel,'id':i,'count':n} for i,n in page.ids.items() if n>1)
  for tag,attr,value in page.links:
   u=urlsplit(urljoin('https://audit.local/'+rel,value))
   if u.netloc!='audit.local' or u.scheme not in {'http','https'}:continue
   path=unquote(u.path).lstrip('/') or 'index.html'
   if (site/path).is_dir():path=path.rstrip('/')+'/index.html'
   checked+=1
   bad=not (site/path).exists() or bool(u.fragment and path in pages and unquote(u.fragment) not in pages[path].ids)
   record={'page':rel,'href':value,'target':path,'fragment':unquote(u.fragment),'valid':not bad}
   if bad:missing.append(record)
   if u.fragment.startswith('ref-'):citations.append(record)
 result={'scope':'Read-only automated triage, not semantic English or mathematical final review','English_chapters':len(scanned),'findings':findings,'finding_counts':dict(collections.Counter(x['kind'] for x in findings)),'HTML_pages':len(pages),'local_resources_and_links_checked':checked,'missing':missing,'duplicate_ids':duplicates,'citation_links':len(citations),'invalid_citation_links':[r for r in citations if not r['valid']],'chapter1_citations':[r for r in citations if r['page'] in ['chapters/01-gambling.html','en/chapters/01-gambling.html']],'source_math':{p.relative_to(ROOT).as_posix():{'source_sha256':sha(p.read_bytes()),'math_sha256':sha(json.dumps(re.findall(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)',p.read_text('utf8')),ensure_ascii=False).encode()),'math_count':len(re.findall(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)',p.read_text('utf8')))}for folder in ['chapters','chapters-en','foundations','foundations-en','advanced','advanced-en','volumes','volumes-en']for p in (ROOT/folder).glob('*.md')}}
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print(json.dumps({k:v for k,v in result.items() if k in ['English_chapters','finding_counts','HTML_pages','local_resources_and_links_checked','citation_links']},ensure_ascii=False));print('Broken local targets:',len(missing),'Broken citations:',len(result['invalid_citation_links']))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);p.add_argument('--site',type=Path,default=ROOT/'dist');a=p.parse_args();audit(a.output,a.site)
