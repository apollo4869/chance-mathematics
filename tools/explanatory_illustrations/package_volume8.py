"""Whitelist-only portable review ZIP. Never deploys or publishes source repositories."""
from pathlib import Path
from urllib.parse import urljoin,urlparse,unquote
import json,re,hashlib,shutil,subprocess,zipfile,argparse
from .volume8 import R,A,O,write
from .volume8_review import PUBLIC,P

GIT='C:/Program Files/Git/cmd/git.exe';D=R/'deliverables'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def cp(a,b):b.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a,b)
SERVER='''from pathlib import Path
from urllib.parse import urlparse,unquote
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import argparse
ROOT=Path(__file__).resolve().parent/'site'
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  rel=unquote(urlparse(path).path).lstrip('/') or 'review/index.html'
  if rel.startswith('before/assets/'):rel=rel.removeprefix('before/')
  p=(ROOT/rel).resolve()
  if ROOT.resolve() not in p.parents:return str(ROOT/'__missing__')
  return str(p/'index.html' if p.is_dir() else p)
 def list_directory(self,path):self.send_error(403);return None
a=argparse.ArgumentParser();a.add_argument('--port',type=int,default=8895);args=a.parse_args()
print(f'Local review only: http://127.0.0.1:{args.port}/review/',flush=True)
ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
'''
def assemble(revision='r1',date='20261106'):
 assert re.fullmatch(r'r[0-9]+',revision) and re.fullmatch(r'[0-9]{8}',date)
 commit=subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),'rev-parse','HEAD'],cwd=R).decode().strip();version=f'volume8-visual-review-{commit[:8]}-{revision}-{date}';dest=D/version
 blobs=subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),'ls-tree','-r',commit,'--','assets/visuals/explanatory-volume8-v1'],cwd=R).decode('utf8').splitlines()
 for record in blobs:
  info,name=record.split('\t',1);raw=(R/name).read_bytes()
  assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==info.split()[2],name
 assert not dest.exists(),'Use a distinct version, do not overwrite a completed package.'
 dest.mkdir(parents=True);jsave(D/'volume8-current-package.json',dict(version=version,source_commit=commit,root=str(dest)))
 for p in A.glob('*'):
  if p.is_file() and p.suffix in ['.svg','.js','.css','.json']:cp(p,dest/'site/assets/visuals/explanatory-volume8-v1'/p.name)
 for p in P.rglob('*.html'):cp(p,dest/'site'/p.relative_to(P))
 # Bundle the exact existing P04/P05 state assets; do not regenerate or replace them.
 for id_ in ['P04','P05']:
  for p in (PUBLIC/'assets/visuals/explanatory-v2').glob(id_+'*.svg'):cp(p,dest/'site/assets/visuals/explanatory-v2'/p.name)
 queue=list((dest/'site').rglob('*.html'));seen=set();missing=set();templates=set()
 while queue:
  p=queue.pop()
  if p in seen:continue
  seen.add(p);s=p.read_text('utf8');url='http://review.local/'+p.relative_to(dest/'site').as_posix()
  refs=re.findall(r'(?:href|src|srcset)=["\']([^"\']+)["\']',s)
  if p.suffix=='.css':refs+=re.findall(r'url\(\s*["\']?([^\s)"\']+)',s)
  if p.suffix in ['.js','.json']:refs+=re.findall(r'["\'](/assets/[^"\'\s]+)["\']',s)
  for ref in refs:
   if '${' in ref:templates.add(ref);continue
   if ref.startswith(('data:','#','mailto:')):continue
   u=urlparse(urljoin(url,ref));rel=unquote(u.path).lstrip('/').removeprefix('before/')
   if u.netloc!='review.local' or not (rel.startswith('assets/') or rel.startswith('favicon')):continue
   out=(dest/'site'/rel).resolve();src=(PUBLIC/rel).resolve()
   if (dest/'site').resolve() not in out.parents or PUBLIC.resolve() not in src.parents:continue
   if out.exists():continue
   if not src.is_file():missing.add(rel);continue
   cp(src,out)
   if out.suffix in ['.css','.js','.json','.svg']:queue.append(out)
 for p in (O/'static-renders').glob('*.png'):cp(p,dest/'site/review/static-renders'/p.name)
 allowed=['REVIEW.md','verification.json','runtime-unit-check.json','manifest.json','source-reading.json','reading-contexts.json','adopted-reuse.json','browser-status.json','public-sources.json','selection.json','http-content-check.json']
 for name in allowed:
  if (O/name).exists():cp(O/name,dest/'records'/name)
 for name in ['volume8.py','volume8_check.py','volume8_runtime_check.cjs','volume8_revision_check.py','volume8_revision_render.cjs']:cp(R/'tools/explanatory_illustrations'/name,dest/'source'/name)
 revision_report=R/'reports/volume8-visual-revision-2026-11-07'
 for name in ['REVIEW.md','targeted-check.json','local-http-check.json']:
  if (revision_report/name).exists():cp(revision_report/name,dest/'records/revision-2026-11-07'/name)
 if (revision_report/'static-renders').exists():
  for p in (revision_report/'static-renders').glob('*.png'):cp(p,dest/'records/revision-2026-11-07/static-renders'/p.name)
 cp(R/'publication/explanatory-volume8-batch1-working.json',dest/'source/explanatory-volume8-batch1-working.json')
 write(dest/'serve_review.py',SERVER)
 write(dest/'START-REVIEW.cmd','@echo off\ncd /d "%~dp0"\nif exist "%USERPROFILE%\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe" (\n "%USERPROFILE%\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe" serve_review.py\n) else (\n python serve_review.py\n)\npause\n')
 jsave(dest/'records/package-provenance.json',dict(version=version,source_commit=commit,ids=['V54','V55','V56','V57','V58'],status='adopted visual working drafts; targeted revision author spot-check pending',unpublished_research_used=False,missing_literal_assets=sorted(missing),dynamic_book_templates=sorted(templates),browser_screenshots=0,browser_attempted_this_round=False,published=False,pushed=False))
 print(str(dest))

def finish():
 cfg=json.loads((D/'volume8-current-package.json').read_text('utf8'));dest=Path(cfg['root']);version=cfg['version'];commit=cfg['source_commit'];zpath=D/('chance-mathematics-'+version+'.zip');assert not zpath.exists()
 renders=json.loads((dest/'records/png-renders.json').read_text('utf8'));svgs=list((dest/'site/assets/visuals/explanatory-volume8-v1').glob('*.svg'));assert len(svgs)==len(renders)==354
 assert {p.name for p in svgs}=={Path(r['svg']).name for r in renders}
 for row in renders:
  assert row['width']==2400 and row['height']>0 and row['density']==300
  assert sha(dest/row['svg'])==row['svg_sha256'] and sha(dest/row['png'])==row['png_sha256']
 # Readability entry point works without serving; interactions need the tiny local server.
 body='<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第八卷五组候选</title><style>body{max-width:1050px;margin:25px auto;padding:15px;color:#173f39;background:#fffefa;font:18px/1.8 sans-serif}img{width:100%;height:auto}a{color:#16776d}section{border-top:1px solid #ccd9d1;margin-top:35px}</style><h1>第八卷 · 五组视觉工作稿 · 定点修订待抽查</h1><p>实际SVG静态渲染，不是浏览器截图。交互与章节对照请按根目录README启动本地服务。</p>'
 for code in ['V54','V55','V56','V57','V58']:
  body+=f'<section><h2>{code}</h2>'
  for lg in ['zh','en']:body+=f'<p>{lg} · <a href="../site/assets/visuals/explanatory-volume8-v1/{code}.{lg}.svg">完整SVG</a> · <a href="../png/{code}/{code}.{lg}.png">高清PNG</a></p><img loading="lazy" src="../png/{code}/{code}.{lg}.png" alt="{code} {lg} static SVG render">'
  body+='</section>'
 write(dest/'gallery/index.html',body+'</html>')
 write(dest/'README.zh.md',f'''# 第八卷首批独立审阅包

版本 `{version}`，源提交 `{commit}`。五组已获当前视觉工作稿采用；本轮V56初始教学状态与V58定点精确化待作者抽查，最终设备、PDF与审美验收仍开放。没有发布或推送。

2026-11-07定点修订、概率对照与前后静态图见 `records/revision-2026-11-07/REVIEW.md`。V58在k=2显示事件B概率相同，k=3、4显示不同；V56从不相容的均分模型开始。原版ZIP不覆盖。

先打开 `gallery/index.html`：中英文完整静态SVG和高清PNG可直接查看。`png/`有全部354份本批SVG逐一实际渲染的PNG，宽2400像素、300 DPI元数据，完整画布不裁切。它们不是浏览器截图，也不是源代码截图。

交互及实际章节前后：双击Windows的 `START-REVIEW.cmd`，或运行 `python serve_review.py`，再打开 http://127.0.0.1:8895/review/ 。只使用Python标准库，绑定localhost；这不是部署。若端口占用，可用 `python serve_review.py --port 8896`。

`site/chapters`、`site/en/chapters`为实际章节嵌入；`site/before`为原页面；`site/review/compare`为前后对照。P04、P05的原图和状态资源保留。本包仅有五章及相应资源，其他全书导航和外部文献不打包。

交互代码在 `site/assets/visuals/explanatory-volume8-v1/interactions.js`；全部预生成交互状态的SVG、模型条件和静态打印页一并提供。`site/print/figures`为逐场景静态打印候选，并不代表原生PDF分页已实测。

数学核验、适用边界、公开文献、候选选择与批判性设计判断见 `records/REVIEW.md`、`verification.json`、`public-sources.json`。`runtime-unit-check.json`使用本地DOM适配器，不是浏览器实测。`png-renders.json`记录每份SVG／PNG哈希及尺寸。`source`中生成器代码供溯源，依赖原项目辅助模块；启动交互不需要运行生成器。

## 未完成的验收

本轮没有重试此前权限受阻的浏览器接口，没有真实网页截图。浏览器桌面／手机渲染、真实点击与触摸、滚动定位、字体与溢出、浏览器打印、真机和原生PDF均未验收。静态图检查不升级作者最终审美或独立专家数学终审。

本包只依据公开模型和现有已认可书稿，不含作者未发表研究、私人笔记、聊天记录、密钥、全库源码或完整PDF文献。数学母稿和成熟旧图未修改。V58的有限配置计数不冒充一般多叉CRT分类、质量密度或连续极限证明。

ZIP附逐文件SHA-256清单，并在交付前检查CRC及全部文件哈希。
''')
 write(dest/'README.en.md',f'''# Volume VIII review candidates

Source commit `{commit}`; package `{version}`. V54–V58 are adopted visual working drafts. Targeted V56/V58 revisions await an author spot-check; final device, PDF and aesthetic acceptance remains open. See `records/revision-2026-11-07/REVIEW.md` for the event-specific labels and the revised starting state.

Open `gallery/index.html` for complete bilingual SVG and high-resolution PNG files. All 354 candidate SVG files have individual uncropped 2400-pixel-wide PNG renders, with 300 DPI metadata. These are **static SVG rasterizations, not browser screenshots**.

Run `python serve_review.py` and visit http://127.0.0.1:8895/review/ for interactions, actual chapter embeds and before/after comparisons. Only Python's standard library is needed. The approved P04/P05 assets are preserved. Other book chapters and external papers are not included.

`records` contains finite-model verification, exact calculations, public-source and privacy boundaries, reading context and design criticism. Browser rendering, pointer/touch interaction, real devices, browser printing, native PDF, final aesthetics and independent expert mathematics remain unverified. No browser retry, deployment, push, unpublished research use or manuscript edit occurred.
''')
 write(dest/'records/interaction-states.md','''# 全部交互状态 / Interaction states

文件名中的末项为desktop或mobile，前面的索引含义如下。每份SVG都配有同名PNG；默认状态并不代表随机模拟。

|组|状态与默认值|真正发生的图形变化|
|---|---|---|
|V54|pause=0/1/2对应a=0、1/4、1/2；time=0,…,8对应U=time/8。默认1-4|停顿时间区间、连续密度带、顶端原子面积和投影点变化；树长不变|
|V55|0恒等摆放；1反射；2反射后平移1/2。默认0|整个Y区间、根与原子点一起等距移动，三项见证误差改变|
|V56|balanced-0/1/2分别孤立标签1/2/3；iid-0,…,7为000至111。默认balanced-2，先看不相容均分，再切换到独立投位|标签所在半块与删除3后的投影改变；全部输入列表和可见分离率随模型改变|
|V57|U索引0/1/2为1/8、1/2、7/8；E索引0/1/2为1、4、8；末项0/1为接枝前/后。默认1-1-1|实际接点、新枝长度、总长和新增叶出现；旧距离保持|
|V58|k=2/3/4；edge=0,…,2k。默认3-2|GW合法形状计数随k改变，增长树可选边及新插点位置改变；B/C事件根据所选边计算|

V58的边0是辅助根干，边1连接两个已有内部节点；边2,…,k连接内部根的其他叶，恰是会产生B事件的边；其余边位于既有内部孩子下。B为内部根有两个内部孩子，C为三个内部节点成链。三步前图不是连续极限或随机模拟。

The controls select exact illustrative states. V54 changes the time-to-mass mapping; V55 changes a common isometric placement; V56 changes a finite split input and its restriction; V57 changes the arclength attachment and a branch length; V58 changes public-model parameters and the selected edge. See the complete bilingual conditions in each static figure and the mathematical verification records. None of these state inventories is browser interaction acceptance.
''')
 files=[dict(path=p.relative_to(dest).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(dest.rglob('*')) if p.is_file()]
 jsave(dest/'PACKAGE-MANIFEST.json',dict(version=version,source_commit=commit,groups=['V54','V55','V56','V57','V58'],candidate_svg=354,candidate_png=354,author_visual_review='targeted revision spot-check pending; final acceptance open',files=files))
 with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(dest.rglob('*')):
   if p.is_file():z.write(p,version+'/'+p.relative_to(dest).as_posix())
 with zipfile.ZipFile(zpath) as z:
  assert z.testzip() is None;assert len(z.namelist())==len(set(z.namelist()))
  for f in files:assert hashlib.sha256(z.read(version+'/'+f['path'])).hexdigest()==f['sha256']
 receipt=dict(version=version,source_commit=commit,path=str(zpath),bytes=zpath.stat().st_size,sha256=sha(zpath),candidate_svg=354,candidate_png=354,crc_and_all_member_hashes_verified=True,author_review='targeted revision spot-check pending; final acceptance open',browser_screenshots=0,published=False,pushed=False)
 jsave(D/(version+'-receipt.json'),receipt);print(json.dumps(receipt,ensure_ascii=False,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('phase',choices=['assemble','finish']);p.add_argument('--revision',default='r1');p.add_argument('--date',default='20261106');args=p.parse_args();assemble(args.revision,args.date) if args.phase=='assemble' else finish()
