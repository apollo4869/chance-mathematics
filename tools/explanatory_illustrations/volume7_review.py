"""Reversible, local-only volume VII reading overlays; never updates a live site."""
from pathlib import Path
from html import escape
from urllib.parse import urlparse,unquote
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import argparse,json,re,hashlib,subprocess
from .volume7 import R,A,O,BASE,META,write,CAP
from .volume6_review import insert

PUBLIC=Path(r'D:\codex\日常\sites\chance-mathematics-illustrations-cloud-2026-11-05\public')
P=A/'local-preview'
GIT='C:/Program Files/Git/cmd/git.exe'
CSS='''body{margin:0;background:#f8f6ef;color:#173f39;font:17px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1120px;margin:auto;padding:24px}h1{font-size:29px;line-height:1.4}h2{font-size:23px}a{color:#16776d}nav{display:flex;gap:18px;flex-wrap:wrap;font-size:14px}section{margin:35px 0;padding-top:20px;border-top:1px solid #ccd9d1}.note{padding:15px;background:#eaf2ee}.twins{display:grid;grid-template-columns:1fr 1fr;gap:20px}.twins iframe{width:100%;height:650px;border:1px solid #ccd9d1}img{max-width:100%;height:auto}.status{color:#a45b30}figcaption{font-size:13px;color:#65756e}@media(max-width:700px){main{padding:14px}.twins{grid-template-columns:1fr}h1{font-size:25px}}'''
INC=f'<link rel="stylesheet" href="{BASE}figures.css"><script defer src="{BASE}interactions.js"></script>'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def shell(title,body,lg='zh',inc=''):
 return f'<!doctype html><html lang="{lg}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{escape(title)}</title><style>{CSS}</style>{inc}</head><body><main>{body}</main></body></html>'
def protect():
 tracked=subprocess.check_output([GIT,'-c',f'safe.directory={R.as_posix()}','ls-files','-z'],cwd=R).decode('utf8').split('\0')
 old={p:sha(R/p) for p in tracked if p and (R/p).is_file()}
 jsave(O/'protected-baseline.json',old)
 return old
def build():
 O.mkdir(parents=True,exist_ok=True)
 if not (O/'protected-baseline.json').exists():protect()
 rows=json.loads((R/'publication/explanatory-volume7-batch1-working.json').read_text('utf8'))['figures']
 manifest=[];contexts=[];read=[]
 for n,slug in [(48,'48-point-processes'),(49,'49-random-measures'),(50,'50-palm-gibbs'),(51,'51-random-closed-sets'),(52,'52-discrete-trees'),(53,'53-tree-scaling')]:
  for lg,d in [('zh','chapters'),('en','chapters-en')]:
   md=R/d/(slug+'.md');text=md.read_text('utf8')
   read.append(dict(chapter=n,lang=lg,path=md.relative_to(R).as_posix(),sha256=sha(md),characters=len(text),sections=len(re.findall(r'(?m)^## ',text)),status='actual chapter read; paired terminology and selected mathematical sections checked'))
 for row in rows:
  code,lg,slug=row['id'],row['lang'],row['slug'];prefix='en/' if lg=='en' else ''
  source=PUBLIC/prefix/'chapters'/(slug+'.html');original=source.read_text('utf8');assert original.count('id="visual-'+code+'"')==0
  before=original.replace('</head>',INC+'</head>',1)
  after,anchor=insert(before,row)
  assert after.replace(row['html'],'',1).replace(INC,'',1)==original
  chapter=f'/{prefix}chapters/{slug}.html';beforeurl=f'/before{chapter}#{anchor}';afterurl=chapter+'#visual-'+code
  write(P/prefix/'chapters'/(slug+'.html'),after)
  write(P/'before'/prefix/'chapters'/(slug+'.html'),before)
  nav=f'<nav><a href="/review/">总览 / Review</a><a href="{afterurl}">实际章节 / Chapter</a><a href="/review/figures/{code}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+f'</a><a href="/print/figures/{code}.{lg}.html">静态打印 / Static</a></nav>'
  write(P/'review/figures'/f'{code}.{lg}.html',shell(row['title'],nav+row['html'],lg,INC))
  # Each model state is a separate printable page, with its conditions retained.
  pages=re.search(r'<div class="v7-print">(.*?)</div>',row['html'],re.S)[1]
  printcss='<style>main{max-width:850px}.pages section{margin:20px 0;padding:0;border:0}.pages img{width:100%}.pages p{font-size:13px;line-height:1.6}@page{size:A4 portrait;margin:12mm}@media print{nav,.print-note{display:none}body{background:white}main{padding:0}.pages section{break-after:page;break-inside:avoid;margin:0}.pages section:last-child{break-after:auto}.pages img{max-height:215mm;object-fit:contain}.pages p{font-size:8pt}.pages h4{font-size:12pt;margin:0}}</style>'
  write(P/'print/figures'/f'{code}.{lg}.html',shell(row['title'],nav+'<p class="print-note">静态候选；原生PDF分页尚待验证 / Static candidate; native PDF pagination not yet verified.</p><div class="pages">'+pages+'</div>',lg,printcss))
  manifest.append(dict(id=code,lang=lg,section=row['section'],chapter=afterurl,before=beforeurl,figure=f'/review/figures/{code}.{lg}.html',print=f'/print/figures/{code}.{lg}.html',source=str(source),source_sha256=sha(source),overlay_sha256=hashlib.sha256(row['html'].encode()).hexdigest(),exact_original_recovery=True))
  md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');parts=re.split(r'(?m)(?=^## )',md.read_text('utf8'))
  for sec in row['coverage_sections']:
   selected=[s for s in parts if s.startswith('## '+sec+' ')];assert len(selected)==1,(code,lg,sec)
   contexts.append(dict(id=code,lang=lg,section=sec,path=md.relative_to(R).as_posix(),sha256=sha(md),text=selected[0]))
 body='<h1>第七卷 · 首批五组解释图候选</h1><p class="note">本地独立工作分支；不修改数学母稿，不发布、不推送。第50章直接复用已采用P03。五组候选尚待作者审美批准。</p><p class="status">浏览器接口仍报告本地浏览器被禁用。实际桌面／手机／交互／章节与打印截图待采集。下列PNG只是SVG静态栅格检查，不能替代浏览器实测。</p><nav><a href="/review/status.html">核验与限制</a><a href="/chapters/50-palm-gibbs.html#visual-P03">第50章已采用P03</a></nav>'
 for code,(_,_,zh,en) in META.items():
  body+=f'<section><h2>{code} · {zh}</h2><nav><a href="/review/figures/{code}.zh.html">中文交互</a><a href="/review/figures/{code}.en.html">English</a><a href="/review/compare/{code}.html">实际章节前后对照</a><a href="/print/figures/{code}.zh.html">静态打印</a></nav><a href="/review/static-renders/{code}-zh-wide-narrow.png"><img loading="lazy" src="/review/static-renders/{code}-zh-wide-narrow.png" alt="{code} SVG静态宽窄布局检查，不是浏览器截图"></a></section>'
  cb=f'<nav><a href="/review/">总览</a></nav><h1>{code} · 实际正文前后对照</h1><p>原位置没有解释图：左为原正文，右为新增候选。iframe是实际页面，不是截图；浏览器截图待权限恢复。</p>'
  for m in [m for m in manifest if m['id']==code]:
   cb+=f'<h2>{m["lang"]}</h2><nav><a href="{m["before"]}">原页面</a><a href="{m["chapter"]}">加入候选</a><a href="{m["figure"]}">交互</a><a href="{m["print"]}">静态打印</a></nav><div class="twins"><iframe loading="lazy" src="{m["before"]}" title="原页面"></iframe><iframe loading="lazy" src="{m["chapter"]}" title="加入候选"></iframe></div><h3>SVG静态排版检查（非浏览器截图）</h3><img loading="lazy" src="/review/static-renders/{code}-{m["lang"]}-wide-narrow.png" alt="静态渲染">'
  write(P/'review/compare'/f'{code}.html',shell(code+' before / after',cb))
 adopted=all(r.get('status','').startswith('adopted') for r in rows)
 if adopted:
  body=body.replace('第七卷 · 首批五组解释图候选','第七卷 · 高优先级视觉工作稿').replace('五组候选尚待作者审美批准。','五组已采用为当前视觉工作稿；V51、V48定点修正已落实。作者最终审美与浏览器验收仍开放。')
  body+='<nav><a href="/review/closeout.html">定点修正与剩余视觉缺口</a></nav>'
 write(P/'review/index.html',shell('第七卷视觉工作稿' if adopted else '第七卷首批候选',body))
 write(P/'review/status.html',shell('核验边界','<nav><a href="/review/">总览</a></nav><h1>实际核验与尚缺交付</h1><p>已完成：有限模型计算、SVG XML结构、双语资源、正文精确逆向恢复、历史资产字节保护、静态SVG栅格逐图检查。</p><p>尚未完成：真实浏览器桌面和手机视口、交互点击、章节嵌入渲染与打印截图。工具报告“Local browser use is disabled in Work settings”；不绕过权限，不用栅格图冒充浏览器截图。真实设备、原生PDF、作者最终审美及专家数学终审继续开放。</p>'))
 # Preserve the actual adopted Palm page; never insert another P03.
 reuse=[]
 for prefix in ['', 'en/']:
  p=PUBLIC/prefix/'chapters/50-palm-gibbs.html';assert p.read_text('utf8').count('id="visual-P03"')==1
  reuse.append(dict(path=str(p),sha256=sha(p),copies=1,changes=False))
 jsave(O/'manifest.json',manifest);jsave(O/'reading-contexts.json',contexts);jsave(O/'source-reading.json',read);jsave(O/'P03-reuse.json',reuse)
 plan=[]
 for m in manifest:
  for tag in ['desktop','mobile','interaction-desktop','interaction-mobile','chapter-before-desktop','chapter-after-desktop','chapter-before-mobile','chapter-after-mobile','print']:
   plan.append(dict(id=m['id'],lang=m['lang'],tag=tag,status='blocked: local browser disabled',file=None))
 jsave(O/'browser-capture-plan.json',plan)
 print(f'Built {len(manifest)} bilingual overlays, exact source recovery passed. P03 unchanged. Real browser captures pending.')

def serve(port):
 class Handler(SimpleHTTPRequestHandler):
  def translate_path(self,path):
   rel=unquote(urlparse(path).path).lstrip('/');rel='review/index.html' if not rel else rel
   if rel.startswith('review/static-renders/'):roots=[(O,rel.removeprefix('review/'))]
   elif rel.startswith('assets/visuals/explanatory-volume7-v1/'):roots=[(R,rel)]
   else:roots=[(P,rel),(PUBLIC,rel.removeprefix('before/'))]
   for root,part in roots:
    target=(root/part).resolve()
    if root.resolve() not in target.parents:continue
    if target.is_dir():target=target/'index.html'
    if target.is_file():return str(target)
   return str(P/'__missing__')
  def list_directory(self,path):self.send_error(403,'Directory listing disabled');return None
 print(f'Local-only review: http://127.0.0.1:{port}/review/',flush=True)
 ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--serve',type=int);args=a.parse_args()
 serve(args.serve) if args.serve else build()
