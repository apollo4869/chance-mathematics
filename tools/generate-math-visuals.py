"""Reproducible, bilingual publication vectors from the shared mathematical JS source.

Requires matplotlib==3.10.7 (and its dependencies), Node.js, and a CJK font.
No browser screenshots are used. Local QA PNGs are not publication originals.
Run: python tools/generate-math-visuals.py
"""
from pathlib import Path
import os,sys,json,subprocess,shutil,hashlib,math,datetime,warnings
ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'qa/matplotlib-config'))
if (ROOT/'qa/visual-runtime').exists():sys.path.insert(0,str(ROOT/'qa/visual-runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager,patches
import numpy as np

BASE=ROOT/'assets/visuals';OUT=BASE/'print';OUT.mkdir(parents=True,exist_ok=True)
QA=ROOT/'qa/math-visuals';QA.mkdir(parents=True,exist_ok=True)
node=shutil.which('node') or r'C:\Users\golde\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
data=json.loads(subprocess.check_output([node,str(BASE/'math-model.js')],cwd=ROOT))
(BASE/'data.json').write_bytes((json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode())
(BASE/'spec.json').write_bytes((json.dumps(data['spec'],ensure_ascii=False,indent=2)+'\n').encode())
font_candidates=[os.environ.get('CHANCE_CJK_FONT',''),r'C:\Windows\Fonts\NotoSansSC-VF.ttf',r'C:\Windows\Fonts\msyh.ttc','/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc']
cjk=next((Path(x) for x in font_candidates if x and Path(x).exists()),None)
if not cjk:raise SystemExit('Set CHANCE_CJK_FONT to an installed CJK font. No font is downloaded or redistributed.')
original_cjk=cjk
from fontTools.ttLib import TTFont
original_font=TTFont(original_cjk,fontNumber=0,recalcTimestamp=False)
font_records={str(i):sorted({n.toUnicode() for n in original_font['name'].names if n.nameID==i}) for i in [0,1,13,14]}
dejavu_license=Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU'
notice='Font notices for the mathematical publication vectors\n\nThe project does not redistribute TTF files. SVG uses outlined glyphs; PDF contains subset fonts.\n\nInstalled CJK font original name-table records:\n'+''.join(f'Name ID {i}:\n'+ '\n'.join(v)+'\n\n' for i,v in font_records.items())+'\nMatplotlib DejaVu font notice (verbatim):\n\n'+dejavu_license.read_text('utf8')
(BASE/'font-notice.txt').write_bytes(notice.encode())
# Resolve the variable font at a fixed weight so every export has a stable face.
if cjk.suffix.lower()=='.ttf':
 from fontTools.ttLib import TTFont
 from fontTools.varLib.instancer import instantiateVariableFont
 font=TTFont(cjk,recalcTimestamp=False)
 if 'fvar' in font:
  # Cache is keyed by input bytes and conversion policy, never by creation time.
  source_hash=hashlib.sha256(cjk.read_bytes()).hexdigest()
  fixed=QA/('CJK-Regular-'+source_hash[:16]+'-stable-head-v1.ttf')
  if not fixed.exists():
   fixed_font=instantiateVariableFont(font,{'wght':400},inplace=True)
   fixed_font.recalcTimestamp=False
   fixed_font['head'].created=original_font['head'].created
   fixed_font['head'].modified=original_font['head'].modified
   fixed_font.save(fixed)
  cjk=fixed
font_manager.fontManager.addfont(str(cjk));cjk_name=font_manager.FontProperties(fname=cjk).get_name()
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'chance-math-visuals-v1','pdf.fonttype':42,'ps.fonttype':42,'font.size':10.5,'axes.titlesize':11.5,'axes.labelsize':10.5,'xtick.labelsize':9,'ytick.labelsize':9,'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':0.8,'savefig.facecolor':'white','figure.facecolor':'white','text.color':'#182a29','axes.labelcolor':'#182a29','xtick.color':'#182a29','ytick.color':'#182a29'})
INK='#182a29';TEAL='#12635e';GRAY='#6d7272';LIGHT='#e6ecea';BLACK='#111111'
def text(en,zh,lang):return zh if lang=='zh' else en
def base_axes(ax):
 ax.set_axisbelow(True);ax.grid(axis='y',color='#d5dbd8',lw=.55,linestyle=':');ax.tick_params(length=3)
def finish(fig,slug,lang):
 fig.savefig(OUT/f'{slug}.{lang}.svg',metadata={'Date':'2026-10-26','Creator':'The Mathematics of Chance reproducible vector figures'})
 fig.savefig(OUT/f'{slug}.{lang}.pdf',metadata={'Creator':'The Mathematics of Chance','CreationDate':datetime.datetime(2026,10,26,tzinfo=datetime.timezone.utc),'ModDate':datetime.datetime(2026,10,26,tzinfo=datetime.timezone.utc)})
 fig.savefig(QA/f'{slug}.{lang}.png',dpi=150)
 plt.close(fig)
def title(fig,en,zh,lang):fig.suptitle(text(en,zh,lang),fontsize=15,fontweight='normal',y=.97)
def foot(fig,en,zh,lang):fig.text(.5,.025,text(en,zh,lang),ha='center',va='bottom',fontsize=9,color=GRAY)

def walks(lang):
 fig,axes=plt.subplots(1,3,figsize=(10.8,4.2),sharex=True,sharey=True);fig.subplots_adjust(left=.07,right=.98,bottom=.25,top=.76,wspace=.2)
 title(fig,'Random walks on the square-root scale','平方根尺度下的随机游走',lang)
 for ax,row in zip(axes,data['walk']):
  p=np.array(row['points']);ax.step(p[:,0],p[:,1],where='post',lw=1.1,color=INK);n=row['n'];ax.set_title(rf'$n={n}$'+'\n'+rf'$\Delta t=1/{n},\quad\Delta x=1/\sqrt{{{n}}}$',fontsize=10.5)
  ax.set(xlim=(0,1),ylim=(-2.6,2.6),xlabel=r'$t$');ax.set_xticks([0,.5,1]);ax.axhline(0,color=GRAY,lw=.6,linestyle='--');base_axes(ax)
 axes[0].set_ylabel(r'$S_{\lfloor nt\rfloor}/\sqrt{n}$')
 foot(fig,'Seed 918273 · Shared increment prefixes, separately rescaled; no pathwise refinement or limit proof.','种子918273 · 使用同一增量序列的前缀分别缩放；不是逐条路径的逐级逼近或极限定理证明。',lang)
 finish(fig,'walk-scaling',lang)

def typewriter(lang):
 fig,axes=plt.subplots(1,2,figsize=(10.8,6.5),sharex=True,sharey=True);fig.subplots_adjust(left=.09,right=.98,bottom=.18,top=.83,wspace=.19)
 title(fig,'Equal snapshot probabilities, different long-term records','每次命中的概率相同，整条记录的命运不同',lang)
 u=data['spec']['typewriter']['sample'];rows=data['typewriter']
 for ix,ax in enumerate(axes):
  ax.set_title(text('Moving window $A_n$' if ix==0 else 'Left-anchored window $B_n$','移动窗口 $A_n$' if ix==0 else '固定左端窗口 $B_n$',lang),pad=12)
  ax.axvline(u,color=BLACK,linestyle='--',lw=1)
  for i,row in enumerate(rows):
   y=len(rows)-i;left=row['left'] if ix==0 else 0;width=row['width'];hit=row['hit'] if ix==0 else row['fixedHit']
   rect=patches.Rectangle((left,y-.29),width,.58,facecolor=LIGHT,edgecolor=INK,lw=.9,hatch='///' if hit else None);ax.add_patch(rect)
   ax.plot(left,y,marker='o',ms=3,color=INK);ax.plot(left+width,y,marker='o',ms=3,mfc='white',mec=INK)
   if hit:ax.plot(u,y,marker='D',ms=4,color=BLACK,zorder=5)
  ax.set(xlim=(-.025,1.025),ylim=(.35,14.9),xlabel=r'$u\in[0,1)$');ax.set_xticks([0,u,.5,1]);ax.set_xticklabels(['0',r'$u_*=0.3$','0.5','1']);ax.set_yticks(range(1,15));ax.set_yticklabels([str(n) for n in range(14,0,-1)]);ax.grid(axis='y',lw=.45,linestyle=':',color='#ccd3d0')
  for y in [8.5,12.5]:ax.axhline(y,color=GRAY,lw=.6,linestyle=':')
 axes[0].set_ylabel(text('Observation $n$ (rounds $k=1,2,3$)','观察序号 $n$（轮次 $k=1,2,3$）',lang))
 foot(fig,'Filled/open circles mean included/excluded endpoints. Diamonds mark hits of $u_*=0.3$.\nEach moving round hits every $u$ once; the fixed windows eventually miss every $u>0$ ($u=0$ is exceptional).','实心/空心端点表示包含/不包含；菱形标出固定点 $u_*=0.3$ 的命中。\n移动窗口每轮命中每个点一次；固定窗口最终离开每个 $u>0$，只有零点例外。',lang)
 finish(fig,'typewriter',lang)

def spikes(lang):
 fig,axes=plt.subplots(1,3,figsize=(10.8,4.5),sharex=True,sharey=True);fig.subplots_adjust(left=.07,right=.98,bottom=.27,top=.79,wspace=.2)
 title(fig,'Height grows, support shrinks, area stays one','越来越高，越来越窄，面积始终为1',lang)
 for ax,row,hatch in zip(axes,data['spikes'],['//','\\\\','xx']):
  n=row['n'];w=row['width'];ax.add_patch(patches.Rectangle((0,0),w,n,fc=LIGHT,ec=INK,lw=1.1,hatch=hatch));ax.plot([0,w],[n,n],'o',mfc='white',mec=INK,ms=5);ax.plot([0,w],[0,0],'o',color=INK,ms=4);ax.plot([w,1],[0,0],color=INK,lw=1)
  ax.set_title(rf'$n={n},\quad |(0,1/n)|={w:g}$');ax.set(xlim=(-.025,1.02),ylim=(-.3,9.2),xlabel=r'$u$');ax.set_xticks([0,.5,1]);base_axes(ax);ax.text(.6,6.7,text('area = 1','面积 = 1',lang),ha='center',fontsize=10)
 axes[0].set_ylabel(r'$X_n(u)=n\,\mathbf{1}_{(0,1/n)}(u)$')
 foot(fig,r'$X_n\to0$ a.e., but $\mathbb{E} X_n=1$. For every $K\geq0$: $\sup_n\mathbb{E}[X_n\mathbf{1}_{\{X_n>K\}}]=1$; UI fails.',r'$X_n\to0$ 几乎处处，但 $\mathbb{E} X_n=1$。任意 $K\geq0$，$\sup_n\mathbb{E}[X_n\mathbf{1}_{\{X_n>K\}}]=1$，故不一致可积。',lang)
 finish(fig,'spike-ui',lang)

def projection(lang):
 fig,ax=plt.subplots(figsize=(8.9,5.4));fig.subplots_adjust(left=.06,right=.96,bottom=.21,top=.83);title(fig,'Conditional expectation as the best square prediction','条件期望：最佳平方预测与正交残差',lang)
 X=np.array(data['spec']['projection']['X']);P=np.array(data['spec']['projection']['P']);V=np.array(data['spec']['projection']['other_predictor'])
 ax.axhline(0,color=GRAY,lw=1);ax.annotate('',xy=X,xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':INK,'lw':1.7,'mutation_scale':13});ax.annotate('',xy=P,xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':TEAL,'lw':2,'mutation_scale':13});ax.annotate('',xy=X,xytext=P,arrowprops={'arrowstyle':'-|>','color':INK,'lw':1.4,'linestyle':'--','mutation_scale':13});ax.plot([V[0],X[0]],[V[1],X[1]],color=GRAY,lw=1,linestyle=':');ax.plot(*V,'s',color=GRAY,ms=5)
 ax.add_patch(patches.Rectangle((P[0]-.15,0),.15,.15,fill=False,ec=INK,lw=.9))
 ax.text(X[0]+.12,X[1],r'$X$',fontsize=13);ax.text(P[0],-.29,r'$P_{\mathcal{G}}X=\mathbb{E}[X\mid\mathcal{G}]$',ha='center',fontsize=11);ax.text(3.13,1.04,text('orthogonal residual','正交残差',lang)+'\n'+r'$X-P_{\mathcal{G}}X$',fontsize=10);ax.text(.8,-.28,r'$V$',fontsize=12);ax.text(4.1,-.28,r'$L^2(\mathcal{G})$',fontsize=13);ax.text(-.13,-.23,r'$0$',fontsize=11)
 ax.text(.15,2.85,r'$\|X-V\|_2^2=\|X-P_{\mathcal{G}}X\|_2^2+\|P_{\mathcal{G}}X-V\|_2^2$',fontsize=11)
 ax.set(xlim=(-.25,4.9),ylim=(-.5,3.1),aspect='equal');ax.axis('off')
 foot(fig,'Abstract geometry in a Hilbert space: the drawing is two-dimensional, not the space of all random variables.','这是 Hilbert 空间的抽象几何示意；图画是二维的，不表示所有随机变量构成二维空间。',lang)
 finish(fig,'conditional-projection',lang)

def disintegration(lang):
 fig,axes=plt.subplots(1,3,figsize=(11.1,4.6));fig.subplots_adjust(left=.07,right=.98,bottom=.28,top=.78,wspace=.34);title(fig,'A joint law, its slice, and normalization','联合分布、竖切片与重新归一化',lang)
 x=data['slice']['x'];ax=axes[0];ax.add_patch(patches.Polygon([[0,0],[1,0],[1,1]],fc=LIGHT,ec=INK,lw=1.1,hatch='///'));ax.plot([x,x],[0,x],color=INK,lw=2.2);ax.set(xlim=(0,1.03),ylim=(0,1.03),xlabel=r'$x$',ylabel=r'$y$',aspect='equal');ax.set_title(text('Joint support','联合支持区域',lang));ax.text(.64,.23,r'$p(x,y)=2$',ha='center',fontsize=10);ax.text(.38,.78,r'$0<y<x<1$',fontsize=10);ax.text(x+.03,x+.08,r'$x_*=0.6$',fontsize=10);ax.plot(x,x,'o',ms=4,mfc='white',mec=INK)
 for ax,height,ylabel,panel in [(axes[1],2,r'$p(x_*,y)$',text('Unnormalized slice','未归一化切片',lang)),(axes[2],1/x,r'$p(y\mid x_*)$',text('Conditional density','条件密度',lang))]:
  ax.add_patch(patches.Rectangle((0,0),x,height,fc=LIGHT,ec=INK,lw=1.1,hatch='///'));ax.plot([0,x],[height,height],'o',mfc='white',mec=INK,ms=4);ax.set(xlim=(-.03,1.03),ylim=(0,2.55),xlabel=r'$y$',ylabel=ylabel);ax.set_xticks([0,x,1]);ax.set_title(panel);base_axes(ax)
 axes[1].text(.5,2.25,r'$\int p(x_*,y)\,dy=2x_*=1.2$',ha='center',fontsize=9.5);axes[2].text(.5,2.25,r'$\frac{2}{2x_*}=\frac{1}{x_*}$',ha='center',fontsize=12);axes[2].text(.3,.8,text('area = 1','面积 = 1',lang),ha='center',fontsize=10)
 foot(fig,r'For $0<x<1$: $p_X(x)=2x$ and $p(y\mid x)=x^{-1}\mathbf{1}_{(0,x)}(y)$. Boundary values do not determine a conditional version.',r'当 $0<x<1$：边缘密度 $p_X(x)=2x$，条件密度 $p(y\mid x)=x^{-1}\mathbf{1}_{(0,x)}(y)$；边界点值不由此公式决定。',lang)
 finish(fig,'disintegration',lang)

def characteristic(lang):
 fig,axes=plt.subplots(2,2,figsize=(10.8,6.9),sharex='row',sharey='row');fig.subplots_adjust(left=.075,right=.98,bottom=.17,top=.88,hspace=.44,wspace=.22);title(fig,'The same mean and variance do not identify a distribution','相同均值与方差，仍然可能是不同分布',lang)
 for i,name in enumerate(['X','Y']):
  m=data['spec']['characteristic'][name];ax=axes[0,i];ax.vlines(m['values'],0,m['probabilities'],colors=INK,lw=1.2,linestyles='-' if i==0 else '--');ax.scatter(m['values'],m['probabilities'],c=INK,s=38,marker='o' if i==0 else 'D',zorder=3);ax.set(xlim=(-2.2,2.2),ylim=(0,.77),xlabel=r'$x$',ylabel=text('Probability','概率质量',lang));ax.set_title(r'$X:\ P(\pm1)=1/2$' if i==0 else r'$Y:\ P(0)=2/3,\ P(\pm\sqrt{3})=1/6$',fontsize=11);ax.set_xticks([-math.sqrt(3),-1,0,1,math.sqrt(3)]);ax.set_xticklabels([r'$-\sqrt{3}$','−1','0','1',r'$\sqrt{3}$']);base_axes(ax)
 a=np.array(data['characteristic'])
 for i in [0,1]:
  ax=axes[1,i];ax.plot(a[:,0],a[:,i+1],color=INK,lw=1.4,linestyle='-' if i==0 else '--');ax.set(xlim=(0,2*math.pi),ylim=(-1.12,1.12),xlabel=r'$t$',ylabel=text('Real part','实部',lang));ax.set_xticks([0,math.pi,2*math.pi]);ax.set_xticklabels(['0',r'$\pi$',r'$2\pi$']);ax.axhline(0,color=GRAY,lw=.6);ax.set_title(r'$\varphi_X(t)=\cos t$' if i==0 else r'$\varphi_Y(t)=\frac{2}{3}+\frac{1}{3}\cos(\sqrt{3}\,t)$',fontsize=12);base_axes(ax)
 foot(fig,r'$\mathbb{E}X=\mathbb{E}Y=0$, $\mathrm{Var}(X)=\mathrm{Var}(Y)=1$. The full characteristic function identifies the law; these two functions differ.',r'$\mathbb{E}X=\mathbb{E}Y=0$，$\mathrm{Var}(X)=\mathrm{Var}(Y)=1$。低阶矩相同，完整特征函数却不同；完整特征函数能够识别分布。',lang)
 finish(fig,'characteristic-identification',lang)

def validate():
 rows=data['typewriter']
 for k in data['spec']['typewriter']['rounds']:
  these=[x for x in rows if x['k']==k];assert len(these)==2**k and sum(x['hit'] for x in these)==1
  assert abs(sum(x['width'] for x in these)-1)<1e-14
 for row in data['walk']:
  n=row['n'];p=row['points'];assert len(p)==n+1 and p[0]==[0,0] and p[-1][0]==1
  assert all(abs(abs(p[i+1][1]-p[i][1])-1/math.sqrt(n))<1e-12 for i in range(n))
 for row in data['spikes']:assert row['width']*row['height']==1
 for m in data['spec']['characteristic'].values():
  if not isinstance(m,dict):continue
  values=m['values'];p=m['probabilities'];mean=sum(x*w for x,w in zip(values,p));var=sum((x-mean)**2*w for x,w in zip(values,p))
  assert abs(sum(p)-1)<1e-12 and abs(mean)<1e-12 and abs(var-1)<1e-12
 assert abs(2*data['slice']['x']-data['slice']['marginal'])<1e-12 and abs(data['slice']['conditionalHeight']*data['slice']['x']-1)<1e-12
 return {'interval_partition':'PASS','half_open_fixed_point_hits':'PASS','walk_increment_scaling':'PASS','spike_area':'PASS','pmf_mass_mean_variance':'PASS','slice_normalization':'PASS'}

if __name__=='__main__':
 warnings.filterwarnings('error',message='Glyph .* missing from font')
 checked=validate()
 for lang in ['zh','en']:
  plt.rcParams['font.family']=[cjk_name,'DejaVu Sans'] if lang=='zh' else ['DejaVu Sans',cjk_name]
  for f in [walks,typewriter,spikes,projection,disintegration,characteristic]:f(lang)
 import fontTools
 manifest={'generator':'tools/generate-math-visuals.py','shared_source':'assets/visuals/math-model.js','matplotlib':matplotlib.__version__,'numpy':np.__version__,'fontTools':fontTools.__version__,'CJK_font':{'name':font_records['1'],'original_file_sha256':hashlib.sha256(original_cjk.read_bytes()).hexdigest(),'resolved_face_sha256':hashlib.sha256(cjk.read_bytes()).hexdigest(),'variable_font_policy':'wght=400; retain source head.created/head.modified; recalcTimestamp=False; source-SHA-keyed cache','embedding':'SVG outlined glyphs; PDF subset TrueType','notice':'assets/visuals/font-notice.txt'},'checks':checked,'files':{p.relative_to(ROOT).as_posix():{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(OUT.glob('*'))}}
 (BASE/'print-manifest.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
 print(json.dumps({'groups':6,'languages':['zh','en'],'publication_vectors':len(manifest['files']),'checks':checked},ensure_ascii=False))
