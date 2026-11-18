"""Local, reversible overlays for adopted figures and volume VI candidates."""
from pathlib import Path
from urllib.parse import urljoin
from html import escape as E
import re,json,hashlib,subprocess
R=Path(__file__).resolve().parents[2]
O=R/'reports/volume6-visual-batch1-2026-11-05';A=R/'assets/visuals/explanatory-volume6-v1';P=A/'local-preview'
BASE='/assets/visuals/explanatory-volume6-v1/';PREFIX=BASE+'local-preview/'
GIT='C:/Program Files/Git/cmd/git.exe'
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
SHELL='body{margin:0;background:#f8f6ef;color:#173f39;font:18px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1080px;margin:auto;padding:26px}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:15px}a{color:#146d61}h1{font-size:28px;line-height:1.5}.note{padding:18px;background:#eaf2ee}section.review{border-top:1px solid #ccd9d1;padding-top:20px;margin:30px 0}.twins{display:grid;grid-template-columns:1fr 1fr;gap:20px}.shots img{width:100%;height:auto}figure{margin:0}figcaption{font-size:15px}@media(max-width:700px){main{padding:12px}.twins{grid-template-columns:1fr}}'
def shell(title,body,includes='',lg='zh'):return f'<!doctype html><html lang="{lg}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(title)}</title><style>{SHELL}</style>{includes}<main>{body}</main></html>'
def assets(names):return ''.join(f'<link rel="stylesheet" href="/assets/visuals/{n}/figures.css"><script defer src="/assets/visuals/{n}/interactions.js"></script>' for n in sorted(names))
def rewrite(s,lg,slug,inc):
 s=re.sub(r'<script\b[^>]*src="[^"]*(?:campaign-attribution|reading-analytics)[^"]*"[^>]*>\s*</script>','',s)
 base='/book/'+('en/' if lg=='en' else '')+'chapters/'+slug+'.html'
 def link(m):
  v=m[2]
  if not v or v.startswith(('#','http:','https:','//','data:','mailto:','tel:')):return m[0]
  return m[1]+'="'+('/book'+v if v.startswith('/') else urljoin(base,v))+'"'
 return re.sub(r'(?<![\w:-])(href|src)="([^"]*)"',link,s).replace('</head>',inc+'</head>',1)
def insert(s,row):
 h=re.search(r'<h[23] id="([^"]+)">'+re.escape(row['section'])+r'\s[^<]+</h[23]>',s);assert h,(row['id'],row['lang'])
 start=s.rfind('<div class="reading-unit"',0,h.start());end=s.find('<div class="reading-unit"',h.end());assert start>=0 and end>start
 at=s.rfind('</div>',start,end);assert f'id="visual-{row["id"]}"' not in s
 t=s[:at]+row['html']+s[at:];assert t.replace(row['html'],'',1)==s
 return t,h[1]
def protect():
 old=json.loads((R/'reports/early-explanations-batch4-2026-11-04/protected-baseline.json').read_text('utf-8'))
 assert all((R/p).is_file() and sha(R/p)==h for p,h in old.items())
 tracked=subprocess.check_output([GIT,'ls-files','-z'],cwd=R).decode('utf-8').split('\0')
 for p in tracked:
  if p and (R/p).is_file():old.setdefault(p,sha(R/p))
 jsave(O/'protected-baseline.json',old)
 jsave(O/'baseline-lineage.json',dict(parent='aff0d034e7e2ab6ecb03059d36ec778fdea48c94',inherited='reports/early-explanations-batch4-2026-11-04/protected-baseline.json',protected=len(old)))
def loadreg(name):return json.loads((R/'publication'/name).read_text('utf-8'))['figures']
def adopted():
 selection=[('explanatory-figures-batch2-working.json',['P01','V31','V33','V34','V37']),('explanatory-early-pilots-working.json',['E06','E08','E16','E20']),('explanatory-early-batch2-working.json',['E12','E13','E17','E24']),('explanatory-early-batch3-working.json',['E14','E30','E39']),('explanatory-batch3-revision-working.json',['E22','E28']),('explanatory-early-batch4-working.json',['E27','E29'])]
 rows=[]
 for f,ids in selection:
  for r in loadreg(f):
   if r['id'] not in ids:continue
   r=r.copy();r.update(selected_registry=f,selected_registry_sha256=sha(R/'publication'/f),html_sha256=hashlib.sha256(r['html'].encode()).hexdigest(),status='visual working draft adopted; final aesthetics, device and PDF review open');rows.append(r)
 assert len(rows)==40 and len({(r['id'],r['lang']) for r in rows})==40
 jsave(R/'publication/explanatory-adopted-volumes1-5.json',dict(automatic_formal_site_injection=False,canonical_manuscript_changes=False,figures=rows))
 targets={};inventory=[]
 for r in rows:targets.setdefault((r['slug'],r['lang']),[]).append(r)
 for (slug,lg),rr in targets.items():
  # The v2 runtime contains the adopted earlier pilot and V31/V33 controls.
  nss=set(re.findall(r'/assets/visuals/([^/]+)/', ''.join(r['html'] for r in rr)))
  if 'explanatory-v1' in nss:nss.remove('explanatory-v1');nss.add('explanatory-v2')
  inc=assets(nss);src=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');before=rewrite(src.read_text('utf-8'),lg,slug,inc);after=before
  for r in rr:
   r=r.copy();r['html']=r['html'].replace('href="/print/',f'href="{PREFIX}adopted/print/')
   after,anchor=insert(after,r)
   inv=dict(id=r['id'],lang=lg,section=r['section'],registry=r['selected_registry'],html_sha256=r['html_sha256'],source_sha256=sha(src),copies=after.count(f'id="visual-{r["id"]}"'),url=f'{PREFIX}adopted/chapters/{lg}/{slug}.html#visual-{r["id"]}')
   assert inv['copies']==1;inventory.append(inv)
   nav=f'<nav><a href="{PREFIX}adopted/index.html">前五卷已采用</a><a href="{inv["url"]}">章节嵌入</a><a href="{PREFIX}adopted/figures/{r["id"]}.{"en" if lg=="zh" else "zh"}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
   write(P/'adopted/figures'/f'{r["id"]}.{lg}.html',shell(r['title'],nav+r['html'],inc,lg))
   static=re.search(r'/assets/visuals/[^"<>]+/'+re.escape(r['id'])+r'\.'+lg+r'\.svg',r['html']);assert static,r['id']
   write(P/'adopted/print'/f'{r["id"]}.{lg}.html',shell(r['title'],nav+f'<img style="width:100%" src="{static[0]}" alt="{E(r["title"])}">',lg=lg))
  # Remove all selected overlays and recover the exact original local page.
  after_check=after
  for r in rr:after_check=after_check.replace(r['html'].replace('href="/print/',f'href="{PREFIX}adopted/print/'),'',1)
  assert after_check==before
  write(P/'adopted/chapters'/lg/(slug+'.html'),after)
 title='第一至第五卷 · 已采用解释图统一预览'
 body=f'<nav><a href="{PREFIX}index.html">本轮总览</a></nav><h1>{title}</h1><p class="note">20组已采用工作稿，中文与英文各一份。只汇合本地预览，历史原图不改；不等于所有潜在插图完成。最终审美、真机及原生PDF验收继续开放。</p>'
 for n in range(1,41):
  rr=[r for r in rows if r['lang']=='zh' and int(r['slug'][:2])==n]
  if rr:body+=f'<section class="review"><h2>第{n}章</h2>'+''.join(f'<p>{r["id"]} {E(r["title"])} · <a href="{PREFIX}adopted/chapters/zh/{r["slug"]}.html#visual-{r["id"]}">正文</a> · <a href="{PREFIX}adopted/figures/{r["id"]}.zh.html">中文</a> · <a href="{PREFIX}adopted/figures/{r["id"]}.en.html">English</a></p>' for r in rr)+'</section>'
 body+='<p>V35、V36、V38、V40已有候选，未见明确作者采用决定；保护原稿，保持待审。第1章骰子映射与依赖切换等原生图未改、未重复制作。</p>'
 write(P/'adopted/index.html',shell(title,body));jsave(O/'adopted-inventory.json',inventory)
 audit=json.loads((R/'reports/early-explanations-batch4-2026-11-04/remaining-audit.json').read_text('utf-8'))
 for r in audit:
  r['completed_here']=[x['id'] for x in rows if x['lang']=='zh' and int(x['slug'][:2])==r['chapter']]
  if r['completed_here']:r['status']='列明位置的高优先级视觉工作稿已采用；剩余候选不等于必须配图'
 jsave(O/'volumes1-5-remaining.json',audit)
 return rows
if __name__=='__main__':protect();adopted();print('20 adopted groups / 40 bilingual overlays, exact source recovery passed')
def candidates():
 from .volume6 import META
 rows=loadreg('explanatory-volume6-batch1-working.json');inc=assets(['explanatory-volume6-v1']);manifest=[];contexts=[]
 for row in rows:
  code,lg,slug=row['id'],row['lang'],row['slug'];src=R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html');before=rewrite(src.read_text('utf-8'),lg,slug,inc)
  # Routes in new fragment are review-only; mathematical and visual content is identical.
  fragment=row['html'].replace('href="/print/',f'href="{PREFIX}print/');r=dict(row,html=fragment);after,anchor=insert(before,r)
  for suffix,s in [('-before',before),('',after)]:write(P/'chapters'/lg/(slug+suffix+'.html'),s)
  other='en' if lg=='zh' else 'zh';nav=f'<nav><a href="{PREFIX}index.html">总览 / Review</a><a href="{PREFIX}chapters/{lg}/{slug}.html#visual-{code}">正文 / In chapter</a><a href="{PREFIX}print/{code}.{lg}.html">静态打印 / Static</a><a href="{PREFIX}figures/{code}.{other}.html">'+('English' if lg=='zh' else '中文')+'</a></nav>'
  write(P/'figures'/f'{code}.{lg}.html',shell(row['title'],nav+fragment,inc,lg))
  printcss='<style>@page{size:A4 portrait;margin:12mm}main{max-width:900px}img.static{width:100%;height:auto}@media print{nav{display:none}body{background:white}main{padding:0;margin:0}img.static{width:180mm;max-width:100%}}</style>'
  write(P/'print'/f'{code}.{lg}.html',shell(row['title'],nav+f'<img class="static" src="{BASE}{code}.{lg}.svg" alt="{E(row["title"])}"><span id="static-end"></span>',printcss,lg))
  manifest.append(dict(id=code,lang=lg,slug=slug,section=row['section'],source_sha256=sha(src),before=f'{PREFIX}chapters/{lg}/{slug}-before.html#{anchor}',chapter=f'{PREFIX}chapters/{lg}/{slug}.html#visual-{code}',figure=f'{PREFIX}figures/{code}.{lg}.html',print=f'{PREFIX}print/{code}.{lg}.html',html_sha256=hashlib.sha256(row['html'].encode()).hexdigest()))
  md=R/('chapters-en' if lg=='en' else 'chapters')/(slug+'.md');parts=re.split(r'(?m)(?=^## )',md.read_text('utf-8'))
  for sec in row['coverage_sections']:
   selected=[s for s in parts if s.startswith('## '+sec+' ')];assert len(selected)==1
   contexts.append(dict(id=code,lang=lg,section=sec,path=md.relative_to(R).as_posix(),source_sha256=sha(md),section_text=selected[0]))
 body=f'<h1>前五卷收束 · 第六卷首批候选</h1><p class="note">五组新候选，待作者视觉审核；另复用已采用P02。数学正文与旧图受保护，不发布、不推送，不进入第七、八卷。</p><nav><a href="{PREFIX}adopted/index.html">前五卷20组已采用图</a><a href="{PREFIX}figures/P02.zh.html">第43章已采用P02</a><a href="{PREFIX}review.html">核验边界</a></nav>'
 for code,(_,_,zh,en) in META.items():
  body+=f'<section class="review"><h2>{code} · {zh}</h2><nav><a href="{PREFIX}figures/{code}.zh.html">中文交互</a><a href="{PREFIX}figures/{code}.en.html">English</a><a href="{PREFIX}compare/{code}.html">实际章节前后与截图</a><a href="{PREFIX}print/{code}.zh.html">静态打印</a></nav></section>'
  cbody=f'<nav><a href="{PREFIX}index.html">总览</a></nav><h1>{code} · 实际章节前后</h1><p>正文、证明、现有图完整保留。以下为真实浏览器视口截图；不作页面拼接。</p>'
  for m in [m for m in manifest if m['id']==code]:
   lg=m['lang'];cbody+=f'<h2>{lg}</h2><nav><a href="{m["before"]}">原页面</a><a href="{m["chapter"]}">加入候选</a><a href="{m["figure"]}">交互</a></nav>'
   for tags in [('chapter-before-desktop','chapter-after-desktop'),('chapter-before-mobile','chapter-after-mobile'),('desktop','mobile'),('interaction-desktop','interaction-mobile'),('print','print-end')]:
    cbody+='<div class="twins">'+''.join(f'<figure class="shots"><a href="{PREFIX}screenshots/{code}-{lg}-{tag}.jpg"><img loading="lazy" src="{PREFIX}screenshots/{code}-{lg}-{tag}.jpg" alt="{tag}"></a><figcaption>{tag}</figcaption></figure>' for tag in tags)+'</div>'
  write(P/'compare'/f'{code}.html',shell(code+' comparison',cbody))
 write(P/'index.html',shell('第六卷首批候选',body))
 write(P/'review.html',shell('核验边界',f'<nav><a href="{PREFIX}index.html">总览</a></nav><h1>模型、工程与审美分开记录</h1><p>五组使用精确有限模型和正文已有结论。长程极限、一般表示和无限paintbox证明仍由原正文负责。浏览器手机视口不等于真实手机；静态打印候选不等于原生PDF、分页及实体打印通过。作者视觉审核待审，独立专家数学终审开放。</p>'))
 # Reuse the adopted P02 exactly, with local routing only.
 for row in loadreg('explanatory-figures-batch2-working.json'):
  if row['id']!='P02':continue
  lg=row['lang'];slug=row['slug'];inc2=assets(['explanatory-v2']);r=dict(row,html=row['html'].replace('href="/print/',f'href="{PREFIX}print/'))
  before=rewrite((R/'dist'/('en' if lg=='en' else '')/'chapters'/(slug+'.html')).read_text('utf-8'),lg,slug,inc2);after,_=insert(before,r)
  write(P/'chapters'/lg/(slug+'.html'),after)
  write(P/'figures'/f'P02.{lg}.html',shell(row['title'],f'<nav><a href="{PREFIX}index.html">总览</a><a href="{PREFIX}chapters/{lg}/{slug}.html#visual-P02">正文</a></nav>'+r['html'],inc2,lg))
  write(P/'print'/f'P02.{lg}.html',shell(row['title'],f'<img style="width:100%" src="/assets/visuals/explanatory-v2/P02.{lg}.svg">',lg=lg))
 jsave(O/'manifest.json',manifest);jsave(O/'reading-contexts.json',contexts)
 print(f'{len(manifest)} bilingual new overlays and {len(contexts)} source contexts; P02 reused unchanged')
def sync_shots():
 import shutil
 d=P/'screenshots';d.mkdir(parents=True,exist_ok=True)
 for p in (O/'screenshots').glob('*.jpg'):shutil.copyfile(p,d/p.name)
