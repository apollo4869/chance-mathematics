"""Exact two-state visit/time weights; common data for publication SVG and vector PDF."""
from pathlib import Path
from fractions import Fraction
import os,sys,json,hashlib,datetime
R=Path(__file__).resolve().parents[3];B=Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR',str(R/'qa/matplotlib-config'))
sys.path.insert(0,str(R/'qa/visual-runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
qa=R/'qa/chapter22';qa.mkdir(exist_ok=True,parents=True)
a,b=Fraction(1),Fraction(4);visits=[Fraction(1,2)]*2;time=[b/(a+b),a/(a+b)]
assert sum(time)==sum(visits)==1 and time[0]*a==time[1]*b
data={'stable_id':'state-time-weight','rates':{'a':str(a),'b':str(b)},'embedded_visit_weights':list(map(str,visits)),
 'stationary_time_weights':list(map(str,time)),'model':'A --a--> B --b--> A',
 'randomness':'NONE; exact theoretical probabilities, not simulated frequencies',
 'purpose':'State visits count equally; time occupancy weights each visit by mean holding time.',
 'not_claimed':'A figure does not prove a convergence theorem.',
 'caption_zh':'两状态链a=1、b=4：按跳数A和B各占1/2，按时间平稳权重为4/5和1/5。差异来自平均停留1与1/4。精确理论值，不是有限轨迹频率。',
 'caption_en':'For rates a=1,b=4, visit weights are1/2 each, while stationary time weights are4/5 and1/5, reflecting mean holds1 and1/4. Exact theoretical values, not finite-path frequencies.'}
(B/'model.json').write_bytes((json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode())
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'state-time-weight-v1','pdf.fonttype':42,
 'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(9.6,4.2),sharey=True)
fig.subplots_adjust(left=.08,right=.98,bottom=.14,top=.76,wspace=.26)
for ax,vals,title in zip(axes,[visits,time],[r'Visits: $\nu$',r'Time: $\pi$']):
 bars=ax.bar(['A','B'],list(map(float,vals)),width=.55,color=['#12635e','#eeeeee'],edgecolor='#172c2a',hatch=['','///'])
 for bar,v in zip(bars,vals):ax.text(bar.get_x()+bar.get_width()/2,float(v)+.035,r'$\frac{'+str(v.numerator)+'}{'+str(v.denominator)+'}$',ha='center',va='bottom',fontsize=15)
 ax.set(ylim=(0,1.03),title=title);ax.set_yticks([0,.25,.5,.75,1]);ax.grid(axis='y',ls=':',lw=.6);ax.set_axisbelow(True)
axes[0].set_ylabel('Probability')
fig.suptitle(r'$a=1,\quad b=4\qquad \pi_i\ \propto\ \nu_i/q_i$',fontsize=15)
stamp=datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc)
fig.savefig(B/'state-time-weight.svg',metadata={'Date':'2026-10-27'})
fig.savefig(B/'state-time-weight.pdf',metadata={'CreationDate':stamp,'ModDate':stamp})
fig.savefig(qa/'state-time-weight.png',dpi=150);plt.close(fig)
Image.open(qa/'state-time-weight.png').convert('L').save(qa/'state-time-weight-grayscale.png')
files=['generate.py','model.json','state-time-weight.svg','state-time-weight.pdf']
(B/'manifest.json').write_bytes((json.dumps({'id':'state-time-weight','kind':'auxiliary-understanding',
 'shared_source':'generate.py + model.json','format':['svg','vector-pdf'],'vector_font_notice':'assets/visuals/font-notice.txt',
 'author_adoption':'PENDING','mathematical_checks':['normalization','detailed balance','holding-time reweighting'],
 'copyright':'Project mathematical code illustration; no automatic blanket AI-content copyright claim.',
 'files':{n:hashlib.sha256((B/n).read_bytes()).hexdigest() for n in files}},ensure_ascii=False,indent=2)+'\n').encode())
print('Exact visit/time diagram: SVG/vector PDF; weights',time)
