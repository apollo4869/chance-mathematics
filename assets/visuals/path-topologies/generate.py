"""Deterministic J1 examples. Run with the project's matplotlib runtime."""
import os,sys,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(R/'qa/visual-runtime'))
os.environ.setdefault('MPLCONFIGDIR',str(R/'qa/matplotlib-config'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fractions import Fraction
P=Path(__file__).parent
model={'id':'jump-alignment','chapter':24,'a':0.5,'n':[8,16],
       'domain':[0,1],'view_window':[0.45,0.8],'simulation':False,
       'purpose':'Distinguish a time-alignable jump from a non-tight shrinking excursion.',
       'print':'SVG and vector PDF share this deterministic mathematical source.'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'path',
                     'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,1,figsize=(8.5,5.8),sharex=True)
styles=[('0.1','-',2.1),('#216266','--',1.8),('0.45',':',2.0)]
a=Fraction(1,2)
def path(ax,up,down=None,color='k',style='-',width=2,label=''):
    end=Fraction(1) if down is None else down
    ax.plot([.45,float(up)],[0,0],color=color,ls=style,lw=width,label=label)
    ax.plot([float(up),float(end)],[1,1],color=color,ls=style,lw=width)
    ax.plot([float(up),float(up)],[0,1],color=color,ls=':',lw=.7,alpha=.6)
    ax.plot(float(up),0,'o',mfc='white',mec=color,ms=5,zorder=5)
    ax.plot(float(up),1,'o',mfc=color,mec=color,ms=4,zorder=6)
    if down is not None:
        ax.plot([float(down),.8],[0,0],color=color,ls=style,lw=width)
        ax.plot([float(down),float(down)],[0,1],color=color,ls=':',lw=.7,alpha=.6)
        ax.plot(float(down),1,'o',mfc='white',mec=color,ms=5,zorder=5)
        ax.plot(float(down),0,'o',mfc=color,mec=color,ms=4,zorder=6)
path(axs[0],a,*(),color=styles[0][0],style=styles[0][1],width=styles[0][2],label=r'$x=1_{[a,1]}$')
for n,(c,l,w) in zip(model['n'],styles[1:]):
 up=a+Fraction(1,n);down=up+Fraction(1,n*n)
 assert 0<a<up<down<1 and down-up==Fraction(1,n*n)
 path(axs[0],up,color=c,style=l,width=w,label=rf'$x_{{{n}}}$')
 path(axs[1],up,down,color=c,style=l,width=w,label=rf'$z_{{{n}}}$')
axs[1].axhline(0,color='0.1',lw=1,label='zero limit at fixed times')
axs[0].set_title('A. One jump: a small clock change aligns its time',loc='left',pad=12)
axs[1].set_title('B. A shrinking excursion: time change cannot remove its height',loc='left',pad=12)
for i,ax in enumerate(axs):
 ax.set_ylim(-.15,1.27);ax.set_yticks([0,1]);ax.set_ylabel('path value')
 ax.set_xlim(.45,.8);ax.grid(axis='x',alpha=.15)
 ax.legend(loc='lower right' if i==0 else 'upper right',fontsize=8,frameon=False)
axs[1].set_xlabel(r'time $t$ (detail of paths defined on $[0,1]$)')
fig.text(.09,.01,'Filled point = included value; open point = excluded value. Dotted vertical guides are not graph segments.',fontsize=8)
fig.tight_layout(rect=(0,.035,1,1),h_pad=2)
fig.savefig(P/'jump-alignment.svg',metadata={'Date':None})
fig.savefig(P/'jump-alignment.pdf',metadata={'CreationDate':None,'ModDate':None})
plt.close(fig)
(P/'model.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
files=['generate.py','model.json','jump-alignment.svg','jump-alignment.pdf']
(P/'manifest.json').write_text(json.dumps({'id':model['id'],'files':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in files}},indent=2)+'\n',encoding='utf8')
print('Created reproducible SVG and vector PDF; exact interval checks passed.')
