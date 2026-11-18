"""Package the committed volume VII candidates without redesigning any artwork."""
from pathlib import Path
from urllib.parse import urljoin,urlparse,unquote
import argparse,hashlib,json,re,shutil,subprocess,zipfile

R=Path(__file__).resolve().parents[2]
ART=R/'assets/visuals/explanatory-volume7-v1'
REPORT=R/'reports/volume7-visual-batch1-2026-11-06'
PUBLIC=Path(r'D:\codex\日常\sites\chance-mathematics-illustrations-cloud-2026-11-05\public')
VERSION='volume7-visual-review-69f0b1ac-r1-20261106'
OUT=R/'deliverables'/VERSION
ZIP=OUT.parent/('chance-mathematics-'+VERSION+'.zip')
GIT='C:/Program Files/Git/cmd/git.exe'
SOURCE_COMMIT='69f0b1ac0f3dc16c091bec2ffc6af94a59a63dee'
IDS=['V48','V49','V51','V52','V53']

def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf8',newline='\n')
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
def tracked_art():
 names=subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),'ls-tree','-r','--name-only',SOURCE_COMMIT,'--','assets/visuals/explanatory-volume7-v1'],cwd=R).decode('utf8').splitlines()
 assert names
 for name in names:
  old=subprocess.check_output([GIT,'-c','safe.directory='+R.as_posix(),'show',SOURCE_COMMIT+':'+name],cwd=R)
  assert (R/name).read_bytes()==old,'Artwork changed since adopted source commit: '+name
 return names

SERVER='''"""Local review server. No deployment; no external packages required."""
from pathlib import Path
from urllib.parse import urlparse,unquote
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import argparse
ROOT=Path(__file__).resolve().parent/'site'
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  rel=unquote(urlparse(path).path).lstrip('/')
  if not rel:rel='review/index.html'
  rel=rel.removeprefix('before/') if rel.startswith('before/assets/') else rel
  p=(ROOT/rel).resolve()
  if ROOT.resolve() not in p.parents:return str(ROOT/'__missing__')
  if p.is_dir():p=p/'index.html'
  return str(p)
 def list_directory(self,path):self.send_error(403,'Directory listing disabled');return None
a=argparse.ArgumentParser();a.add_argument('--port',type=int,default=8890);args=a.parse_args()
print(f'Local review only: http://127.0.0.1:{args.port}/review/',flush=True)
ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
'''

def assemble():
 names=tracked_art();OUT.mkdir(parents=True,exist_ok=True)
 if (OUT/'PACKAGE-MANIFEST.json').exists():raise RuntimeError('A completed package already exists; use a new version instead of overwriting.')
 # Exact source assets; no re-generation or edits to the artwork.
 for p in sorted(ART.glob('*.svg')):cp(p,OUT/'site/assets/visuals/explanatory-volume7-v1'/p.name)
 for name in ['figures.css','interactions.js','models.json']:cp(ART/name,OUT/'site/assets/visuals/explanatory-volume7-v1'/name)
 for p in (ART/'local-preview').rglob('*.html'):cp(p,OUT/'site'/p.relative_to(ART/'local-preview'))
 # Supply the original page resources using a narrow, public-asset dependency closure.
 # Chapter texts outside the five selected chapters are not copied.
 queue=list((OUT/'site').rglob('*.html'));seen=set();copied=[];external=set();unresolved=set();templates=set()
 def reference(value,url):
  if value.startswith(('data:','#','mailto:','tel:','javascript:')):return
  if '${' in value:templates.add(value);return
  full=urljoin('http://review.local'+url,value);u=urlparse(full)
  if u.netloc!='review.local':external.add(full);return
  rel=unquote(u.path).lstrip('/');rel=rel.removeprefix('before/')
  # Before/after chapter aliases share the same public asset tree.
  if not (rel.startswith('assets/') or rel in ['favicon.svg','favicon.ico','apple-touch-icon.png','site.webmanifest']):return
  target=(OUT/'site'/rel).resolve()
  if (OUT/'site').resolve() not in target.parents:return
  if target.exists():return
  original=(PUBLIC/rel).resolve()
  if PUBLIC.resolve() not in original.parents:return
  if original.is_file():
   cp(original,target);copied.append(rel)
   if original.suffix.lower() in ['.html','.css','.js','.json','.svg']:queue.append(target)
  else:unresolved.add(rel)
 while queue:
  p=queue.pop()
  if p in seen:continue
  seen.add(p);s=p.read_text('utf8');url='/'+p.relative_to(OUT/'site').as_posix()
  for value in re.findall(r'(?:src|href|srcset)=["\']([^"\']+)["\']',s):
   if ',' not in value:reference(value,url)
  if p.suffix.lower()=='.css':
   for value in re.findall(r'url\(\s*["\']?([^\s)"\']+)',s):reference(value,url)
  if p.suffix.lower() in ['.js','.json']:
   for value in re.findall(r'["\'](/assets/[^"\'\s]+)["\']',s):reference(value,url)
 # Explicit report whitelist: no AGENTS, private notes, full repository inventory or research files.
 for name in ['REVIEW.md','verification.json','runtime-unit-check.json','http-content-check.json','browser-capture-plan.json','manifest.json','reading-contexts.json','source-reading.json','P03-reuse.json']:
  cp(REPORT/name,OUT/'records'/name)
 for p in (REPORT/'static-renders').glob('*.png'):cp(p,OUT/'site/review/static-renders'/p.name)
 cp(R/'publication/explanatory-volume7-batch1-working.json',OUT/'source/explanatory-volume7-batch1-working.json')
 for name in ['volume7.py','volume7_check.py','volume7_runtime_check.cjs']:
  cp(R/'tools/explanatory_illustrations'/name,OUT/'source'/name)
 write(OUT/'serve_review.py',SERVER)
 write(OUT/'START-REVIEW.cmd','@echo off\ncd /d "%~dp0"\nif exist "%USERPROFILE%\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe" (\n  "%USERPROFILE%\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe" serve_review.py\n) else (\n  python serve_review.py\n)\npause\n')
 jsave(OUT/'records/dependency-inventory.json',dict(public_assets=copied,unresolved_asset_paths=sorted(unresolved),dynamic_template_references=sorted(templates),external_references=sorted(external),note='Only assets referenced by existing selected chapter pages are copied; no new network fetch was used. Out-of-scope book navigation and external literature links are not bundled.'))
 jsave(OUT/'records/artwork-provenance.json',dict(version=VERSION,source_commit=SOURCE_COMMIT,figures=IDS,source_tracked_files_checked=len(names),source_unchanged=True,author_visual_status='待审 / pending',browser='not attempted this packaging round; previously blocked',published=False,pushed=False))
 print('Assembled exact committed artwork and chapter overlays; PNG render is the next phase.')

def finish():
 svgs=sorted((OUT/'site/assets/visuals/explanatory-volume7-v1').glob('*.svg'))
 renders=json.loads((OUT/'records/png-renders.json').read_text('utf8'))
 assert len(svgs)==len(renders)==398
 assert all((OUT/r['png']).is_file() and r['width']==2400 and r['height']>0 for r in renders)
 groups=[]
 for code in IDS:
  rows=[r for r in renders if Path(r['svg']).name.startswith(code)]
  for lg in ['zh','en']:
   assert any(Path(r['svg']).name==f'{code}.{lg}.svg' for r in rows)
   assert any('-'+lg+'-' in Path(r['svg']).name and '-mobile.svg' in r['svg'] for r in rows)
   assert any('-'+lg+'-' in Path(r['svg']).name and '-desktop.svg' in r['svg'] for r in rows)
  groups.append(dict(id=code,svg=len(rows),png=len(rows),languages=['zh','en']))
 body='''<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第七卷独立审阅包</title><style>body{max-width:1100px;margin:30px auto;padding:16px;font:17px/1.8 sans-serif;color:#173f39;background:#fffefa}img{max-width:100%;height:auto}section{margin:35px 0;border-top:1px solid #ccd9d1}a{color:#16776d}</style><h1>五组作者视觉待审候选</h1><p>原作版本69f0b1ac；PNG均为实际SVG栅格渲染，不是网页或浏览器截图。可直接打开此页看高清图；交互及实际章节请先运行根目录serve_review.py，再打开本地审阅入口。</p><p><a href="../README.zh.md">审阅说明与验证边界</a> · <a href="../records/interaction-states.md">交互状态说明</a></p>'''
 for code in IDS:
  body+=f'<section><h2>{code}</h2>'
  for lg in ['zh','en']:
   body+=f'<p>{lg} · <a href="../site/assets/visuals/explanatory-volume7-v1/{code}.{lg}.svg">原始完整SVG</a> · <a href="../png/{code}/{code}.{lg}.png">2400像素完整PNG</a></p><a href="../png/{code}/{code}.{lg}.png"><img loading="lazy" src="../png/{code}/{code}.{lg}.png" alt="{code} {lg} SVG静态渲染"></a>'
  body+='</section>'
 write(OUT/'gallery/index.html',body+'</html>')
 write(OUT/'README.zh.md',f'''# 第七卷五组解释图 · 独立审阅包

版本：`{VERSION}`。原作独立提交：`{SOURCE_COMMIT}`。五组仍为作者视觉待审，不发布、不推送，不进入第八卷。

## 先看哪里

直接双击 `gallery/index.html`：查看中英文完整SVG和高清PNG，无须运行服务。`png/`包含全部398份SVG逐一渲染的398份PNG，统一宽2400像素、300 DPI元数据，白底完整画布，不裁切、不拼接源代码截图。手机构图有各自独立PNG；完整静态版本和逐页打印版本均保留。

交互与实际正文：在本文件所在目录运行 `python serve_review.py`，打开 http://127.0.0.1:8890/review/ 。这是解压后的本地审阅服务，不是部署。若端口被占用，可用 `python serve_review.py --port 8891`。目录名变化不影响资源定位。

`site/review/figures/`是五组中英文交互页面；`site/chapters/`和`site/en/chapters/`是实际嵌入候选的章节，`site/before/`是原页面；`site/review/compare/`给出前后对应；`site/print/figures/`保留静态分页候选。普通书籍导航指向的其他章节不在本包内；外部文献也未下载。原页面、原章节链接保持不变。

## 文件与数学说明

- `site/assets/visuals/explanatory-volume7-v1/`：398份最新版中英文SVG、原交互JS、CSS、模型数据；与原作提交逐文件核对一致。
- `png/V48`、`V49`、`V51`、`V52`、`V53`：所有状态、宽窄构图、完整静态图及逐页打印图的高清PNG。`records/png-renders.json`逐项记录输入／输出哈希、尺寸、渲染器与来源。
- `records/interaction-states.md`：各按钮、滑块、默认与对照状态，以及精确计算和适用边界。
- `records/verification.json`：有限模型和源保护检查；`runtime-unit-check.json`是本地DOM适配器检查，**不是浏览器交互实测**。
- `records/reading-contexts.json`保留实际中英文数学上下文；`records/REVIEW.md`保留候选设计判断、数学说明与限制。
- `source/`保留现有生成器／核验代码供溯源；生成器依赖原项目辅助模块，不是本包的启动入口。交互运行无须这些生成器。
- `PACKAGE-MANIFEST.json`记录全部打包文件和SHA-256；ZIP生成后还会做CRC、成员路径和文件内容复核。

## 不能宣称已经验证的项目

本轮没有尝试真实浏览器截图。此前工具权限错误为 `Local browser use is disabled in Work settings`。没有桌面／手机浏览器截图，没有指针和触摸交互实测，没有浏览器字体、页面黑屏、嵌入滚动与溢出实测，没有浏览器打印或原生PDF分页测试。PNG是SVG真实静态渲染，**不是网页截图**。既有对照页里的状态提示和90项待采集列表保留原状。

真实设备、最终作者审美、原生PDF与独立专家数学终审仍开放。数学自查、DOM单元检查、HTTP内容检查、静态栅格检查彼此独立，不自动升级审校状态。

本包不包含私人笔记、聊天记录、密钥、全库源码或未发表论文。数学正文及现有图未被修改；本次只是封装现有作品和补充高清栅格渲染。
''')
 write(OUT/'README.en.md',f'''# Volume VII illustration review package

Package `{VERSION}`; original artwork commit `{SOURCE_COMMIT}`. V48/V49/V51/V52/V53 remain pending author visual review. No publication or push.

Open `gallery/index.html` directly for complete bilingual SVG/PNG art. Every one of the 398 committed SVG files has its own uncropped 2400-pixel-wide PNG, with 300 DPI metadata. These are real static SVG rasterizations, **not browser screenshots**.

For interaction and actual chapter before/after pages, run `python serve_review.py` from this folder, then open http://127.0.0.1:8890/review/ . The server binds only to localhost and uses only Python's standard library. Other chapters and external references are outside this package.

`records/interaction-states.md` explains all states and mathematical calculations. `records/verification.json` records finite-model checks; `runtime-unit-check.json` uses a DOM adapter and is not a browser test. `records/png-renders.json` identifies each source and render by hash. Original chapter embeds, comparisons, static print candidates, interactive code and mathematical context are included.

No browser was retried in this packaging round. Actual browser desktop/mobile screenshots, pointer/touch interaction, embedded-page rendering, font and overflow behavior, browser printing, native PDF pagination and real-device checks remain unverified. Author aesthetic approval and independent expert mathematical review remain open. No private research, notes, secrets or full source repository is bundled.
''')
 states='''# 交互状态与精确模型 / Interaction states and exact models

所有PNG来自对应SVG的实际渲染，覆盖下列全部离散状态。滑块只选择示意位置，不把连续概率改成离散均匀模型。

|组|可见交互状态|默认与重要对照|精确计算与边界|
|---|---|---|---|
|V48|独立／复制两模型 × 3组U,V；两语言、桌面／手机|默认independent-0；copied-0为共享输入对照|两Poisson(1)边缘相同；联合空窗概率e⁻²与e⁻¹。允许两点空间重数；不是一般PRM构造证明|
|V49|R／(0,1) × 3个紧窗候选；两语言、宽／窄构图|real-0默认；real-2揭示无限局部计数，open-2显示非法紧窗|x_k=1/(k+1)，加权Σ2⁻ᵏ=1；窗口质量7/8、32767/32768、1。非法窗口标—不是质量0|
|V51|3种高度区间关系 × U=0,1/20,…,1；两语言、宽／窄构图|0-10默认；1-10对照空间不交且命中互斥|连续U下四读数分别(2/5,2/5,2/5,2/5)、(1/4,1/4,1/2,0)、(1/2,9/20,7/10,1/4)。端点包括在内但单点概率0|
|V52|树A／B × 首次访问节点j=0,…,4；两语言、宽／窄构图|A-3默认；B-3对照b=4与b=5|Q_j=1+S_j，b_j=2j−H_j，C(b_j)=H_j。节点5、边4、轮廓8步；全部14棵五节点树另行核查|
|V53|5个编号循环切口；第二层单孩子链长度0／2／5；两语言、宽／窄构图|切口1默认合法，切口3提前到−1失败|r=1首次最低点合法；r=3第三步已到−1。加链给出零任务增量却增加高度；确定性机制不冒充条件GW定理|

V48 compares independent versus copied Poisson counts. V49 separates ambient space, compactness and local mass. V51 compares spatial disjointness with overlap of hit events. V52 links a vertex to its task list, preorder height and contour clock. V53 compares all numbered cuts and adds a unary-chain height-instability example. General theorems and their independent expert review retain the original scope and status.

源码与数据：`site/assets/visuals/explanatory-volume7-v1/interactions.js`、`models.json`；原双语HTML片段：`source/explanatory-volume7-batch1-working.json`。全部有限模型详见 `records/REVIEW.md` 与 `verification.json`。
'''
 write(OUT/'records/interaction-states.md',states)
 entries=[]
 for p in sorted(OUT.rglob('*')):
  if p.is_file() and p.name!='PACKAGE-MANIFEST.json':entries.append(dict(path=p.relative_to(OUT).as_posix(),bytes=p.stat().st_size,sha256=sha(p)))
 jsave(OUT/'PACKAGE-MANIFEST.json',dict(version=VERSION,artwork_commit=SOURCE_COMMIT,groups=groups,svg_count=len(svgs),png_count=len(renders),png_kind='uncropped static SVG raster; not browser screenshots',browser_retried=False,author_visual_review='pending',files=entries))
 assert not ZIP.exists(),'Do not overwrite an earlier ZIP.'
 with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(OUT.rglob('*')):
   if p.is_file():z.write(p,VERSION+'/'+p.relative_to(OUT).as_posix())
 with zipfile.ZipFile(ZIP) as z:
  assert z.testzip() is None
  names=z.namelist();assert len(names)==len(set(names))
  for m in entries:
   data=z.read(VERSION+'/'+m['path']);assert hashlib.sha256(data).hexdigest()==m['sha256']
  assert all(not n.startswith('/') and '..' not in Path(n).parts for n in names)
 receipt=dict(version=VERSION,artwork_commit=SOURCE_COMMIT,zip=str(ZIP),bytes=ZIP.stat().st_size,sha256=sha(ZIP),groups=groups,files=len(names),crc_and_all_member_hashes_verified=True,source_unchanged=True,real_browser_screenshots=0,browser_retried=False)
 jsave(OUT.parent/(VERSION+'-receipt.json'),receipt)
 print(json.dumps(receipt,ensure_ascii=False,indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('phase',choices=['assemble','finish']);a=p.parse_args()
 assemble() if a.phase=='assemble' else finish()
