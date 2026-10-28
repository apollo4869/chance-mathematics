"""One deterministic record, three expressions; SVG and vector PDF share exact data."""
from pathlib import Path
import datetime,hashlib,json,os,sys
ROOT=Path(__file__).resolve().parents[3]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'qa/matplotlib-config'))
sys.path.insert(0,str(ROOT/'qa/visual-runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
QA=ROOT/'qa/chapter21';QA.mkdir(parents=True,exist_ok=True)
model={'stable_id':'arrival-record','kind':'auxiliary-understanding','randomness':'NONE; deterministic illustration, not an observed or simulated Poisson sample',
       'waits':[0.6,1.1,0.4,1.3,0.8],'horizon':5,'partition':[0,2,4,5],
       'right_endpoint':'included','not_claimed':'A finite drawing proves neither exponential waiting nor independence.',
       'caption_zh':'同一记录的三种表达：等待、到达位置和右连续计数。竖虚线分出(0,2]、(2,4]、(4,5]，计数分别为2、2、1。数据是确定性示意，不是Poisson样本或独立性证明。',
       'caption_en':'One record expressed as waits, arrival locations and a right-continuous count. Dashed lines partition (0,2], (2,4], (4,5], with counts2,2,1. Deterministic illustration, not a Poisson sample or proof of independence.'}
arrivals=[];total=0
for w in model['waits']:total=round(total+w,10);arrivals.append(total)
counts=[sum(a<x<=b for x in arrivals) for a,b in zip(model['partition'],model['partition'][1:])]
assert arrivals==[.6,1.7,2.1,3.4,4.2] and counts==[2,2,1] and all(w>0 for w in model['waits'])
model.update(arrivals=arrivals,window_counts=counts)
(BASE/'model.json').write_bytes((json.dumps(model,ensure_ascii=False,indent=2)+'\n').encode())
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'arrival-record-v1','pdf.fonttype':42,
 'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,(top,bottom)=plt.subplots(2,1,figsize=(10.3,5.7),sharex=True,gridspec_kw={'height_ratios':[1,2.3]})
fig.subplots_adjust(left=.085,right=.98,bottom=.13,top=.9,hspace=.22)
top.hlines(0,0,5,color='#172c2a',linewidth=1)
top.plot(arrivals,[0]*5,'o',color='#172c2a',ms=5)
for j,(a,b) in enumerate(zip([0]+arrivals[:-1],arrivals),1):
 top.annotate('',xy=(a,.32),xytext=(b,.32),arrowprops={'arrowstyle':'<->','color':'#172c2a','lw':.8})
 top.text((a+b)/2,.45,fr'$W_{j}$',ha='center',va='center')
 top.text(b,-.27,fr'$S_{j}$',ha='center')
top.text(0,-.27,'0',ha='center');top.set_ylim(-.6,.8);top.axis('off')
xx=[0]+arrivals+[5];yy=list(range(6))+[5]
bottom.step(xx,yy,where='post',lw=1.5,color='#12635e')
for j,t in enumerate(arrivals,1):
 bottom.plot(t,j,'o',color='#12635e',ms=5)
 bottom.plot(t,j-1,'o',mfc='white',mec='#12635e',ms=5)
for x in [2,4]:
 top.axvline(x,color='#777',ls='--',lw=.9)
 bottom.axvline(x,color='#777',ls='--',lw=.9)
for a,b,n in zip(model['partition'],model['partition'][1:],counts):
 bottom.text((a+b)/2,5.5,fr'$\Delta N={n}$',ha='center')
bottom.set(xlim=(0,5),ylim=(-.18,5.9),xlabel=r'$t$',ylabel=r'$N(t)$')
bottom.set_xticks([0,1,2,3,4,5]);bottom.set_yticks(range(6));bottom.grid(axis='y',ls=':',lw=.5)
fig.suptitle(r'$W_n=S_n-S_{n-1}\qquad N(t)=\#\{n:S_n\leq t\}$',fontsize=14)
stamp=datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc)
fig.savefig(BASE/'arrival-record.svg',metadata={'Date':'2026-10-27'})
fig.savefig(BASE/'arrival-record.pdf',metadata={'CreationDate':stamp,'ModDate':stamp})
fig.savefig(QA/'arrival-record.png',dpi=160)
for line in bottom.lines:line.set_color('#111');line.set_markeredgecolor('#111')
fig.savefig(QA/'arrival-record-grayscale.png',dpi=160)
plt.close(fig)
files=['generate.py','model.json','arrival-record.svg','arrival-record.pdf']
manifest={'id':'arrival-record','source':'generate.py','parameters':'model.json','formats':['svg','vector-pdf'],
 'languages':'Shared mathematical labels with separate complete Chinese/English captions in Chapter21',
 'model_checks':{'positive_waits':True,'partial_sums':True,'half_open_window_counts':counts,'right_continuous_markers':True},
 'licensing':'Project-created mathematical code figure; no blanket copyright claim for AI-generated material; Matplotlib/DejaVu notices retained with existing dependencies.',
 'files':{n:hashlib.sha256((BASE/n).read_bytes()).hexdigest() for n in files}}
(BASE/'manifest.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print('Shared-source SVG/vector PDF generated; exact window counts:',counts)
