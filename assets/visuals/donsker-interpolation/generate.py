"""Shared deterministic source for the Chapter25 interpolation-error figure."""
import os,sys,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(R/'qa/visual-runtime'))
os.environ.setdefault('MPLCONFIGDIR',str(R/'qa/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
P=Path(__file__).parent
spec={'id':'interpolation-gap','chapter':25,'n':8,'increments':[1,-1,2,-2,1,1,-1,-1],
      'simulation':False,'normalization':'sqrt(n)','error_bound':'max(abs(increments))/sqrt(n)',
      'purpose':'Show why step and polygonal paths differ by at most the largest normalized increment.'}
inc=np.array(spec['increments']);n=spec['n'];t=np.arange(n+1)/n
y=np.r_[0,np.cumsum(inc)]/np.sqrt(n);bound=max(abs(inc))/np.sqrt(n)
assert len(inc)==n and y[0]==0 and y[-1]==0
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'path','pdf.fonttype':42,
                     'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,1,figsize=(8.4,5.8),sharex=True,gridspec_kw={'height_ratios':[1.2,1]})
axs[0].plot(t,y,'-',color='0.12',lw=1.8,label=r'polygon $L_n$')
for i in range(n):
 axs[0].plot(t[i:i+2],[y[i],y[i]],'--',color='#216266',lw=1.8,label=r'step $W_n$' if i==0 else None)
 axs[0].plot([t[i+1],t[i+1]],[y[i],y[i+1]],':',color='0.65',lw=.7)
 axs[0].plot(t[i+1],y[i],'o',mfc='white',mec='#216266',ms=5,zorder=4)
 axs[1].plot(t[i:i+2],[0,abs(inc[i])/np.sqrt(n)],color='0.2',lw=1.5)
 axs[1].plot(t[i+1],abs(inc[i])/np.sqrt(n),'o',mfc='white',mec='0.2',ms=5,zorder=4)
axs[0].plot(t,y,'o',color='0.12',ms=3,zorder=6)
axs[1].plot(t,np.zeros(n+1),'o',color='0.2',ms=3,zorder=6)
axs[1].axhline(bound,color='#216266',ls='--',lw=1.4,label=r'bound $\max_i|\xi_i|/\sqrt{n}$')
axs[0].set_title(r'A. Same grid records, two paths ($n=8$)',loc='left',pad=10)
axs[1].set_title(r'B. Absolute discrepancy $|L_n(t)-W_n(t)|$',loc='left',pad=10)
axs[0].set_ylabel('normalized position');axs[1].set_ylabel('absolute error')
axs[0].set_ylim(-.09,.94);axs[1].set_ylim(-.06,.91)
for ax in axs:
 ax.set_xlim(-.015,1.015);ax.set_xticks(t);ax.grid(axis='x',alpha=.15)
 ax.legend(loc='upper right',frameon=False,fontsize=9)
axs[1].set_xlabel('time t')
fig.text(.09,.012,'Open points are excluded left limits; filled points are actual grid values. No random simulation is used.',fontsize=8)
fig.tight_layout(rect=(0,.04,1,1),h_pad=1.7)
fig.savefig(P/'interpolation-gap.svg',metadata={'Date':None})
fig.savefig(P/'interpolation-gap.pdf',metadata={'CreationDate':None,'ModDate':None})
plt.close(fig)
# Check the pointwise geometric bound independently on every cell.
for i in range(n):
 for u in [0,.1,.5,.9,.999]:
  error=abs(u*inc[i])/np.sqrt(n)
  assert error<=bound+1e-14
(P/'model.json').write_bytes((json.dumps(spec,indent=2)+'\n').encode())
files=['generate.py','model.json','interpolation-gap.svg','interpolation-gap.pdf']
(P/'manifest.json').write_bytes((json.dumps({'id':spec['id'],'files':{f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in files}},indent=2)+'\n').encode())
print('Interpolation figure SVG/vector PDF and exact finite-cell model checks completed.')
