"""Deterministic isolated-spike graph; shared source for SVG and vector PDF."""
from pathlib import Path
import os, sys, math, json, hashlib, datetime
R=Path(__file__).resolve().parents[3]; B=Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR',str(R/'qa/matplotlib-config'))
sys.path.insert(0,str(R/'qa/visual-runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
qa=R/'qa/chapter23';qa.mkdir(parents=True,exist_ok=True)
u=math.sqrt(2)/2; observations=[0,.25,.5,.75,1]
assert u not in observations and 0<u<1
model={'stable_id':'path-version-spike','u':u,'observations':observations,
 'randomness':'NONE: fixed illustrative u; theorem uses Uniform(0,1) U, not a simulation',
 'graph':'X(t)=0; Y(t)=1 if t=u else0. Vertical dashed line is only a guide.',
 'caption_zh':'孤立尖点逃过有限观察；空心点移除u处零值，实心点给出Y(u)=1。虚竖线不是函数图像。',
 'caption_en':'Finite observations miss an isolated spike. The open circle removes zero at u; the filled point gives Y(u)=1. The dashed vertical line is not the graph.',
 'mathematical_purpose':'Same finite-dimensional laws do not force the given version to have continuous paths.'}
(B/'model.json').write_bytes((json.dumps(model,ensure_ascii=False,indent=2)+'\n').encode())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'pdf.fonttype':42,
 'svg.fonttype':'path','svg.hashsalt':'path-version-spike-v1','figure.facecolor':'white',
 'savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(2,1,figsize=(9.2,5.7),sharex=True)
fig.subplots_adjust(left=.09,right=.97,bottom=.13,top=.87,hspace=.48)
for ax in axes:
 ax.set(xlim=(-.035,1.035),ylim=(-.19,1.25),yticks=[0,1])
 ax.axhline(0,color='#172c2a',lw=1.7,zorder=1)
 ax.scatter(observations,[0]*5,marker='s',s=37,color='#172c2a',zorder=4)
 ax.set_ylabel('Value')
 ax.set_xticks(observations)
axes[0].set_title(r'$X(t)=0$ — continuous',loc='left')
axes[1].set_title(r'$Y(t)=\mathbf{1}_{\{t=u\}}$ — one isolated spike',loc='left')
axes[1].plot([u,u],[0,1],ls='--',color='#777777',lw=.85,zorder=0)
axes[1].scatter([u],[0],s=75,facecolor='white',edgecolor='#172c2a',lw=1.6,zorder=5)
axes[1].scatter([u],[1],s=65,color='#12635e',edgecolor='#172c2a',zorder=5)
axes[1].annotate(r'$u=\sqrt{2}/2$',xy=(u,1),xytext=(.38,1.04),
 arrowprops={'arrowstyle':'->','lw':.8},ha='left')
axes[1].set_xlabel('Time t — squares: fixed observation times')
fig.suptitle('Finite observations agree; sample-path continuity differs',fontsize=14)
stamp=datetime.datetime(2026,10,28,tzinfo=datetime.timezone.utc)
fig.savefig(B/'path-version-spike.svg',metadata={'Date':'2026-10-28'})
fig.savefig(B/'path-version-spike.pdf',metadata={'CreationDate':stamp,'ModDate':stamp})
fig.savefig(qa/'path-version-spike.png',dpi=150);plt.close(fig)
Image.open(qa/'path-version-spike.png').convert('L').save(qa/'path-version-spike-grayscale.png')
names=['generate.py','model.json','path-version-spike.svg','path-version-spike.pdf']
(B/'manifest.json').write_bytes((json.dumps({'stable_id':'path-version-spike','kind':'auxiliary-understanding',
 'source':'generate.py + model.json','formats':['svg','vector-pdf'],'random_simulation':False,
 'font_notice':'assets/visuals/font-notice.txt','author_adoption':'PENDING',
 'copyright':'Programmatic mathematical illustration; no blanket AI-content copyright claim.',
 'checks':['u outside fixed observation grid','open point at (u,0)','filled point at (u,1)','dashed guide is not graph'],
 'files':{n:hashlib.sha256((B/n).read_bytes()).hexdigest() for n in names}},ensure_ascii=False,indent=2)+'\n').encode())
print('Path-version vector illustration generated; no stochastic sample claim.')
