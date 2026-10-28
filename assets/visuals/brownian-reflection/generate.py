"""Deterministic reflection geometry; not a simulated Brownian sample."""
from pathlib import Path
import sys,os,json,hashlib
R=Path(__file__).resolve().parents[3];P=Path(__file__).parent
sys.path.insert(0,str(R/'qa/visual-runtime'))
os.environ.setdefault('MPLCONFIGDIR',str(R/'qa/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'path','pdf.fonttype':42})
t=np.array([0,.12,.23,.34,.43,.51,.63,.74,.85,1.])
y=np.array([0,.31,.18,.72,1,.83,.65,.88,.52,.35])
a=1.;j=4;ref=y.copy();ref[j:]=2*a-y[j:]
assert np.all(y[:j]<a) and y[j]==a and ref[-1]==2*a-y[-1]
fig,ax=plt.subplots(figsize=(8.6,4.8))
ax.plot(t,y,color='0.12',lw=2,label=r'original path $b$')
ax.plot(t[j:],ref[j:],color='#28676b',ls=(0,(5,3)),lw=2,label=r'reflected path $R_ab$')
ax.axhline(a,color='0.5',lw=1,ls=':')
ax.axvline(t[j],color='0.65',lw=.9,ls=':')
ax.scatter([t[j],1,1],[a,y[-1],ref[-1]],color='0.12',s=22,zorder=5)
ax.annotate(r'first hit $\tau_a$',(t[j],a),xytext=(.29,1.43),arrowprops={'arrowstyle':'->','color':'0.3'})
ax.text(.02,a+.045,r'level $a$')
ax.text(1.025,y[-1],r'$x<a$',va='center')
ax.text(1.025,ref[-1],r'$2a-x>a$',va='center')
ax.set(xlim=(0,1.23),ylim=(-.06,1.95),xlabel=r'time $t$',ylabel='position')
ax.set_xticks([0,t[j],1],[r'$0$',r'$\tau_a$',r'$T$'])
ax.set_yticks([0,a],[r'$0$',r'$a$'])
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='upper left',frameon=False)
fig.text(.12,.016,'Deterministic schematic: the reflected future has equal path law only after the probabilistic proof.',fontsize=8)
fig.tight_layout(rect=(0,.045,1,1))
fig.savefig(P/'reflection.svg',metadata={'Date':None})
fig.savefig(P/'reflection.pdf',metadata={'CreationDate':None,'ModDate':None})
plt.close(fig)
spec={'id':'brownian-reflection','chapter':26,'t':t.tolist(),'b':y.tolist(),'a':a,'first_hit_index':j,'reflected':ref.tolist(),'simulation':False,'seed':None,'purpose':'First-hit reflection is an involution; endpoint below a becomes above a. Geometry is not a probability proof.','print':'SVG and vector PDF; solid/dashed plus labels; monochrome compatible','caption_source':'chapters/26-brownian-properties.md and chapters-en/26-brownian-properties.md'}
(P/'model.json').write_bytes((json.dumps(spec,indent=2)+'\n').encode())
(P/'manifest.json').write_bytes((json.dumps({'id':spec['id'],'files':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['generate.py','model.json','reflection.svg','reflection.pdf']}},indent=2)+'\n').encode())
print('Reflection vector SVG/PDF and deterministic invariants PASS')
