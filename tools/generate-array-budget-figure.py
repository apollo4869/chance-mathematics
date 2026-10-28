"""Deterministic Lindeberg budgets; optional Matplotlib3.10.7 publication tool."""
from pathlib import Path
import sys,os,json,hashlib,datetime,math
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'qa/visual-runtime'));os.environ.setdefault('MPLCONFIGDIR',str(R/'qa/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
font=Path(os.environ['CHANCE_CJK_FONT']) if os.environ.get('CHANCE_CJK_FONT') else next(iter((R/'qa/math-visuals').glob('CJK-Regular-*-stable-head-v1.ttf')),None)
if font is None:raise SystemExit('Install a licensed CJK font; provide its path with CHANCE_CJK_FONT or generate the local publication font cache first.')
font_manager.fontManager.addfont(str(font));family=font_manager.FontProperties(fname=font).get_name()
plt.rcParams.update({'font.family':family,'svg.fonttype':'path','svg.hashsalt':'chance-array-budget-v1','pdf.fonttype':42,'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.8,'figure.facecolor':'white','savefig.facecolor':'white'})
base=R/'assets/visuals';out=base/'print';qa=R/'qa/array-budget';qa.mkdir(exist_ok=True,parents=True)
ns=[16,64,256,1024];curves=[16,64,256]
model={'id':'lindeberg-budget','models':{'small':{'law':'P(X=+1/sqrt(n))=P(X=-1/sqrt(n))=1/2','row_length':'n','variance_per_term':'1/n','total_variance':1,'L_n(epsilon)':'1 if epsilon<1/sqrt(n), else0'},'rare':{'law':'P(X=+1)=P(X=-1)=1/(2n); P(X=0)=1-1/n','row_length':'n','variance_per_term':'1/n','total_variance':1,'L_n(epsilon)':'1 if epsilon<1, else0'}},'n':ns,'curves_n':curves,'randomness':'NONE; exact expectations','purpose':'Feller maximal variance is identical; Lindeberg tail budgets differ.','not_claimed':'Finite plots do not prove convergence; theorem proved in Chapter14.'}
(base/'array-budget-data.json').write_bytes((json.dumps(model,ensure_ascii=False,indent=2)+'\n').encode())
for lang in ['zh','en']:
 zh=lang=='zh';fig,axes=plt.subplots(1,2,figsize=(11.4,4.8));fig.subplots_adjust(left=.08,right=.98,bottom=.24,top=.78,wspace=.27)
 fig.suptitle('同样没有方差大户，为什么极限仍不同？' if zh else 'Equal maximal variances, different limits',fontsize=14,y=.97)
 ax=axes[0];ax.plot(ns,[1/n for n in ns],color='#172c2a',lw=1.2,marker='o',label='两种模型：1/n' if zh else 'Both models: 1/n');ax.set_xscale('log',base=2);ax.set_yscale('log',base=2);ax.set_xticks(ns,[str(n) for n in ns]);ax.set_yticks([1/n for n in ns],['1/'+str(n) for n in ns]);ax.set_xlabel('行长 n' if zh else 'Row length n');ax.set_ylabel('最大单项方差' if zh else 'Maximal individual variance');ax.set_title('Feller 条件看不出区别' if zh else 'Feller cannot distinguish them',fontsize=11);ax.grid(ls=':',lw=.55);ax.legend(frameon=False,fontsize=9)
 ax=axes[1];styles=['-','--',':'];markers=['o','s','^']
 grid=sorted(set([i/100 for i in range(111)]+[1/math.sqrt(n) for n in curves]+[.3]))
 for n,style,mark in zip(curves,styles,markers):
  values=[1.0 if x<1/math.sqrt(n) else 0.0 for x in grid]
  ax.step(grid,values,where='post',color='#172c2a',ls=style,lw=1.2,label=('小步' if zh else 'Small')+f' n={n}');ax.plot([1/math.sqrt(n)],[0],marker=mark,mfc='white',mec='#172c2a',ms=5)
 ax.step(grid,[1.0 if x<1 else 0.0 for x in grid],where='post',color='#a14c2e',lw=2,ls='-.',label='罕见单位跳：所有 n' if zh else 'Rare unit jumps: every n');ax.plot([1],[0],marker='D',mfc='white',mec='#a14c2e',ms=5);ax.axvline(.3,color='#777777',ls=':',lw=.8)
 ax.set(xlim=(0,1.1),ylim=(-.06,1.08),xlabel=r'$\varepsilon$',ylabel=r'$L_n(\varepsilon)$');ax.set_yticks([0,1]);ax.set_title('大跳带走的整行二阶预算' if zh else 'Row second-moment budget in large terms',fontsize=11);ax.legend(frameon=False,fontsize=8,loc='center right');ax.grid(axis='y',ls=':',lw=.55)
 fig.text(.5,.12,'每行均值0、总方差1、行内独立；左侧完全相同，右侧相差一整份预算。' if zh else 'Independent centered rows, total variance 1: both models coincide on the left; large-term budgets differ.',ha='center',fontsize=10)
 fig.text(.5,.055,'小步 → Gaussian；罕见单位跳 → 对称标记 compound Poisson。图示为精确计算，不是模拟或证明。' if zh else 'Small steps → Gaussian; rare unit jumps → symmetric compound Poisson. Exact calculations, not simulation or proof.',ha='center',fontsize=9)
 stem=out/('lindeberg-budget.'+lang);fig.savefig(str(stem)+'.svg',metadata={'Date':'2026-10-27'});fig.savefig(str(stem)+'.pdf',metadata={'CreationDate':datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc),'ModDate':datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc)});fig.savefig(qa/('lindeberg-budget.'+lang+'.png'),dpi=160);plt.close(fig)
names=['assets/visuals/array-budget-data.json','tools/generate-array-budget-figure.py']+[f'assets/visuals/print/lindeberg-budget.{l}.{e}' for l in ['zh','en'] for e in ['svg','pdf']]
v={'id':'lindeberg-budget','model':model,'matplotlib':matplotlib.__version__,'font_sha256':hashlib.sha256(font.read_bytes()).hexdigest(),'font_notice':'assets/visuals/font-notice.txt','files':{n:{'sha256':hashlib.sha256((R/n).read_bytes()).hexdigest()} for n in names},'author_adoption':'PENDING_AUTHOR_READING'}
(base/'array-budget-manifest.json').write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode());print('Bilingual Lindeberg SVG/vector PDF generated')
