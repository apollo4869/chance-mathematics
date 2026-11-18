"""Local overlays for volume VIII. P04/P05 and all canonical manuscripts stay intact."""
from pathlib import Path
from html import escape
from urllib.parse import urlparse,unquote
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import argparse,json,re,hashlib,subprocess
from .volume8 import R,A,O,META,BASE,write
from .volume6_review import insert
from .volume7_review import shell as shared_shell,PUBLIC

P=A/'local-preview';GIT='C:/Program Files/Git/cmd/git.exe'
INC=f'<link rel="stylesheet" href="{BASE}figures.css"><script defer src="{BASE}interactions.js"></script>'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def shell(t,b,lg='zh',inc=''):return shared_shell(t,b,lg,inc)
def protect():
 paths=subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),'ls-files','-z'],cwd=R).decode('utf8').split('\0')
 jsave(O/'protected-baseline.json',{s:sha(R/s) for s in paths if s and (R/s).is_file()})
def build():
 if not (O/'protected-baseline.json').exists():protect()
 rows=json.loads((R/'publication/explanatory-volume8-batch1-working.json').read_text('utf8'))['figures'];manifest=[];contexts=[];read=[];reuse=[]
 for code,(slug,_,_,_) in META.items():
  for lg,folder in [('zh','chapters'),('en','chapters-en')]:
   p=R/folder/(slug+'.md');text=p.read_text('utf8');read.append(dict(chapter=int(slug[:2]),lang=lg,path=p.relative_to(R).as_posix(),sha256=sha(p),characters=len(text),sections=len(re.findall(r'(?m)^## ',text)),scope='Chinese full chapter read; English selected mathematical sections and terminology cross-checked'))
 for row in rows:
  code,lg,slug=row['id'],row['lang'],row['slug'];prefix='en/' if lg=='en' else '';src=PUBLIC/prefix/'chapters'/(slug+'.html');original=src.read_text('utf8');assert 'id="visual-'+code+'"' not in original
  before=original.replace('</head>',INC+'</head>',1);after,anchor=insert(before,row);assert after.replace(row['html'],'',1).replace(INC,'',1)==original
  for id_ in ['P04','P05']:
   if 'id="visual-'+id_+'"' in original:assert after.count('id="visual-'+id_+'"')==1;reuse.append(dict(id=id_,lang=lg,page_source_sha256=sha(src),existing_html_unchanged=True))
  chapter=f'/{prefix}chapters/{slug}.html';beforeurl='/before'+chapter+'#'+anchor;afterurl=chapter+'#visual-'+code
  write(P/prefix/'chapters'/(slug+'.html'),after);write(P/'before'/prefix/'chapters'/(slug+'.html'),before)
  nav=f'<nav><a href="/review/">总览 / Review</a><a href="{afterurl}">实际章节 / Chapter</a><a href="/review/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+f'</a><a href="/print/figures/{code}.{lg}.html">静态打印 / Static</a></nav>'
  write(P/'review/figures'/f'{code}.{lg}.html',shell(row['title'],nav+row['html'],lg,INC))
  pages=re.search(r'<div class="v8-print">(.*?)</div>',row['html'],re.S)[1]
  printcss='<style>.pages section{border:0;margin:20px 0}.pages img{width:100%}.pages p{font-size:13px;line-height:1.6}@page{size:A4 portrait;margin:12mm}@media print{nav,.print-note{display:none}body{background:white}main{margin:0;padding:0}.pages section{break-after:page;break-inside:avoid}.pages section:last-child{break-after:auto}.pages img{max-height:205mm;object-fit:contain}.pages p{font-size:8pt}.pages h4{font-size:12pt}}</style>'
  write(P/'print/figures'/f'{code}.{lg}.html',shell(row['title'],nav+'<p class="print-note">静态候选；浏览器及原生PDF分页待验。 / Static candidate; browser and native PDF checks pending.</p><div class="pages">'+pages+'</div>',lg,printcss))
  manifest.append(dict(id=code,lang=lg,slug=slug,section=row['section'],source=str(src),source_sha256=sha(src),chapter=afterurl,before=beforeurl,figure=f'/review/figures/{code}.{lg}.html',print=f'/print/figures/{code}.{lg}.html',exact_source_recovery=True))
  md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');parts=re.split(r'(?m)(?=^## )',md.read_text('utf8'))
  for sec in row['coverage_sections']:
   found=[p for p in parts if p.startswith('## '+sec+' ')];assert len(found)==1,(code,lg,sec)
   contexts.append(dict(id=code,lang=lg,section=sec,source=md.relative_to(R).as_posix(),sha256=sha(md),text=found[0]))
 body='<h1>第八卷 · 首批五组解释图工作稿</h1><p class="note">2026-11-07：V54–V57采用；V58定点精确化后采用。本轮V56初始状态与V58修订待作者抽查。P04、P05在实际章节中保留；不修改数学母稿，不发布、不推送。</p><p class="status">本轮未重试此前被拒绝的浏览器接口。PNG为真实SVG静态栅格渲染，不是网页截图。浏览器交互、桌面／手机页面、打印、真机及原生PDF均待验。</p><nav><a href="/chapters/54-brownian-crt.html#visual-P04">已采用P04</a><a href="/chapters/55-metric-measure-limits.html#visual-P05">已采用P05</a></nav>'
 for code,(_,_,zh,en) in META.items():
  body+=f'<section><h2>{code} · {zh}</h2><nav><a href="/review/figures/{code}.zh.html">中文交互</a><a href="/review/figures/{code}.en.html">English</a><a href="/review/compare/{code}.html">实际章节前后</a><a href="/print/figures/{code}.zh.html">静态打印</a></nav><img loading="lazy" src="/review/static-renders/{code}-zh-wide-narrow.png" alt="{code} 静态SVG排版检查，非浏览器截图"></section>'
  b=f'<nav><a href="/review/">总览</a></nav><h1>{code} · 实际章节前后</h1><p>原位置为正文；既有P04／P05等图保留。下面是实际HTML页面对照，不是浏览器截图。</p>'
  for m in [m for m in manifest if m['id']==code]:
   b+=f'<h2>{m["lang"]}</h2><nav><a href="{m["before"]}">原页面</a><a href="{m["chapter"]}">加入候选</a><a href="{m["figure"]}">交互</a></nav><div class="twins"><iframe loading="lazy" src="{m["before"]}" title="原页面"></iframe><iframe loading="lazy" src="{m["chapter"]}" title="加入候选"></iframe></div><img loading="lazy" src="/review/static-renders/{code}-{m["lang"]}-wide-narrow.png" alt="静态栅格检查">'
  write(P/'review/compare'/f'{code}.html',shell(code+' comparison',b))
 write(P/'review/index.html',shell('第八卷首批候选',body))
 jsave(O/'manifest.json',manifest);jsave(O/'source-reading.json',read);jsave(O/'reading-contexts.json',contexts);jsave(O/'adopted-reuse.json',reuse)
 jsave(O/'browser-status.json',dict(attempted_this_round=False,prior_error='Local browser use is disabled in Work settings',status='not verified',screenshots=0,open=['actual browser desktop/mobile rendering','pointer/touch interaction','chapter scroll/embedding','browser print','native PDF','real devices','author final aesthetics','independent expert mathematics']))
 print('Ten reversible bilingual overlays built; original P04/P05 preserved.')
def serve(port):
 class Handler(SimpleHTTPRequestHandler):
  def translate_path(self,path):
   rel=unquote(urlparse(path).path).lstrip('/') or 'review/index.html'
   if rel.startswith('review/static-renders/'):roots=[(O,rel.removeprefix('review/'))]
   elif rel.startswith('assets/visuals/explanatory-volume8-v1/'):roots=[(R,rel)]
   else:roots=[(P,rel),(PUBLIC,rel.removeprefix('before/'))]
   for root,part in roots:
    p=(root/part).resolve()
    if root.resolve() not in p.parents:continue
    if p.is_dir():p=p/'index.html'
    if p.is_file():return str(p)
   return str(P/'__missing__')
  def list_directory(self,path):self.send_error(403);return None
 print(f'Local review: http://127.0.0.1:{port}/review/',flush=True);ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--serve',type=int);args=p.parse_args();serve(args.serve) if args.serve else build()
