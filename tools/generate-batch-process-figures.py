"""Reproducible, bilingual process figures for Chapters 16, 19 and 20.

All numerical data, captions, SVG and vector PDF are generated together.
Run with the installed publication runtime: python tools/generate-batch-process-figures.py
These finite explanatory figures do not prove the associated infinite-time results.
"""
from pathlib import Path
from fractions import Fraction
import datetime, hashlib, json, os, random, sys

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR', str(ROOT/'qa/matplotlib-config'))
sys.path.insert(0, str(ROOT/'qa/visual-runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

BASE = ROOT/'assets/visuals/batch16-20'
QA = ROOT/'qa/batch16-20'
BASE.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)
font = Path(os.environ['CHANCE_CJK_FONT']) if os.environ.get('CHANCE_CJK_FONT') else next(iter((ROOT/'qa/math-visuals').glob('CJK-Regular-*-stable-head-v1.ttf')), None)
if font is None:
    raise SystemExit('Use the existing licensed CJK publication font cache or set CHANCE_CJK_FONT; no font is downloaded.')
font_manager.fontManager.addfont(str(font))
family = font_manager.FontProperties(fname=font).get_name()
plt.rcParams.update({'font.family':family, 'svg.fonttype':'path', 'svg.hashsalt':'chance-process-batch-v1', 'pdf.fonttype':42,
    'font.size':10, 'axes.spines.top':False, 'axes.spines.right':False, 'axes.linewidth':.8,
    'figure.facecolor':'white', 'savefig.facecolor':'white'})
DATE = datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc)
INK, TEAL, GREY = '#172c2a', '#12635e', '#777777'

increments = [1,-1,1,1,-1,1,1,-1,-1,1,1,-1,-1,-1]
path = [0]
for d in increments: path.append(path[-1]+d)
threshold = 3
tau = next(i for i,x in enumerate(path) if x >= threshold)
stopped = [path[min(i,tau)] for i in range(len(path))]
assert tau == 7 and all(x < threshold for x in path[:tau]) and path[tau] == threshold
assert stopped[:tau+1] == path[:tau+1] and len(set(stopped[tau:])) == 1

lengths = [1,1,2,1,5,1,2,1,5,1]
support = sorted(set(lengths))
event_weights = [Fraction(lengths.count(k),len(lengths)) for k in support]
time_weights = [Fraction(k*lengths.count(k),sum(lengths)) for k in support]
assert sum(event_weights) == sum(time_weights) == 1
assert sum(Fraction(k)*p for k,p in zip(support,event_weights)) == 2
assert sum(Fraction(k)*p for k,p in zip(support,time_weights)) == Fraction(16,5)

seed, depth = 20261027, 6
rng = random.Random(seed)
nodes = [{'id':0, 'parent':None, 'generation':0, 'children':[]}]
generations = [[0]]
for g in range(depth):
    next_gen = []
    for idx in generations[g]:
        count = 2 if rng.random() < .5 else 0
        for _ in range(count):
            child = len(nodes)
            nodes.append({'id':child, 'parent':idx, 'generation':g+1, 'children':[]})
            nodes[idx]['children'].append(child)
            next_gen.append(child)
    generations.append(next_gen)
population = [len(g) for g in generations]
assert population == [1,2,2,4,6,4,4]
assert all(len(n['children']) in (0,2) for n in nodes if n['generation'] < depth)
assert all(len(g)%2 == 0 for g in generations[1:])
leaf_counter = 0
def position(idx):
    global leaf_counter
    n = nodes[idx]
    if n['children']:
        xs = [position(j) for j in n['children']]
        n['x'] = sum(xs)/len(xs)
    else:
        n['x'] = leaf_counter
        leaf_counter += 1
    return n['x']
position(0)

models = {
 'stopping-prefix':{'randomness':'NONE; a fixed explanatory nearest-neighbour path', 'increments':increments, 'path':path,
   'threshold':threshold, 'first_hitting_time':tau, 'stopped_path':stopped, 'convention':'tau=min{n>=0:X_n>=3}; X_stopped(n)=X_min(n,tau)'},
 'inspection-length-bias':{'randomness':'NONE; finite deterministic interval collection', 'intervals':lengths, 'total_length':sum(lengths),
   'length_support':support, 'uniform_interval_probabilities':[str(x) for x in event_weights],
   'uniform_time_probabilities':[str(x) for x in time_weights], 'uniform_interval_mean_length':'2', 'uniform_time_mean_containing_length':'16/5',
   'sampling':'Choose one of the 10 intervals uniformly, versus choose a Lebesgue-uniform time in [0,20). Endpoints have probability zero.'},
 'finite-gw-family':{'randomness':'CPython random.Random, MT19937; random()<1/2 gives two children, otherwise zero',
   'seed':seed, 'offspring':{'p0':'1/2','p2':'1/2'}, 'mean_offspring':1, 'observed_generations':[0,depth],
   'population':population, 'nodes':nodes, 'boundary':'Children of generation 6 are not sampled, so boundary tips are not classified as childless.'}}

entries = {
 'stopping-prefix':{'chapter':16,'classification':'AUXILIARY_UNDERSTANDING',
  'caption_zh':'首次到达只使用已经发生的记录。固定近邻路径在第7步首次达到高度3；实线保留停止前缀，方形点虚线在此后冻结为3，细点线显示未停止的原路径。这里没有随机抽样，有限路径示意不是可选抽样定理的证明，也不保证任意停止规则保持期望。',
  'caption_en':'A first hit uses only the record already observed. This fixed nearest-neighbour path first reaches level 3 at step 7. The solid prefix is retained; the dashed line with square markers then stays at 3, while the thin dotted line shows the unstopped path. No randomness is sampled. This finite illustration neither proves optional sampling nor asserts expectation preservation for arbitrary stopping rules.',
  'alt_zh':'路径在第7步首次命中高度3。停止路径此前与原路径相同，此后恒为3；原路径继续上下运动。',
  'alt_en':'The path first hits level 3 at step 7. The stopped path agrees before that time and remains at 3 afterward, while the original path continues moving.',
  'learning_purpose_zh':'区分合法首达规则、停止前缀和停止后的冻结。',
  'learning_purpose_en':'Distinguish a legitimate first-hit rule, its observed prefix and the subsequent frozen process.'},
 'inspection-length-bias':{'chapter':19,'classification':'AUXILIARY_UNDERSTANDING',
  'caption_zh':'同一组10个间隔，按事件均匀选取与按时间均匀观察，得到不同的长度分布。长度1、2、5各出现6、2、2次；事件权重为0.6、0.2、0.2，时间权重为0.3、0.2、0.5。较长间隔占用更多时间，含观察时刻的间隔平均长度由2变为3.2。本图是总长度20上的确定性有限示意，不是平稳更新构造或更新极限定理的证明；含时刻的总间隔长度也不等于余寿命。',
  'caption_en':'The same ten intervals produce different length distributions under uniform interval sampling and uniform time observation. Lengths 1, 2 and 5 occur 6, 2 and 2 times: their event weights are 0.6, 0.2 and 0.2, but their time weights are 0.3, 0.2 and 0.5. Longer intervals occupy more time, raising the mean containing-interval length from 2 to 3.2. This deterministic illustration on a total length of 20 is not a proof of stationary renewal construction or a renewal limit theorem. Containing-interval length is not residual life.',
  'alt_zh':'总长20的时间轴包含六个长度1、两个长度2和两个长度5的间隔。并列条形图显示长度5的权重从按间隔的0.2增加为按时间的0.5。',
  'alt_en':'A timeline of total length 20 contains six unit intervals, two intervals of length 2 and two of length 5. Paired bars show the weight of length 5 increasing from 0.2 by intervals to 0.5 by time.',
  'learning_purpose_zh':'看见检查悖论中的长度偏置，避免把总间隔长度误当余寿命。',
  'learning_purpose_en':'Make the length bias behind the inspection paradox visible, without confusing interval length with residual life.'},
 'finite-gw-family':{'chapter':20,'classification':'AUXILIARY_UNDERSTANDING',
  'caption_zh':'一个临界Galton–Watson家族的有限记录。每个已观察生育的个体以相等概率有0或2个孩子，平均子女数为1；固定种子20261027，MT19937生成，先按代、再按从左到右顺序抽样。第0至6代人口为1、2、2、4、6、4、4。第6代只画已出生个体，不抽样其后代；有限图既不证明临界灭绝，也不能据此判断这一家族的无限未来。',
  'caption_en':'A finite record of a critical Galton–Watson family. Every individual whose reproduction is observed has either 0 or 2 children with equal probability, so mean offspring is 1. The MT19937 seed is 20261027; reproduction is sampled generation by generation, left to right. Populations in generations 0 through 6 are 1, 2, 2, 4, 6, 4 and 4. Generation 6 shows births only; its offspring are not sampled. The finite figure neither proves critical extinction nor determines this family’s infinite future.',
  'alt_zh':'有限家族树按第0至6代排列，连线保留亲子关系；每代人口在右侧标为1、2、2、4、6、4、4，第6代是观察边界。',
  'alt_en':'A finite family tree in generations 0 through 6 retains every parent-child edge. Population labels on the right are 1, 2, 2, 4, 6, 4 and 4; generation 6 is the observation boundary.',
  'learning_purpose_zh':'将人口递推与亲缘结构区分，显示平均子女数1不等于每代人数恒定。',
  'learning_purpose_en':'Separate population recursion from genealogy, and show that mean offspring 1 does not make every generation equally large.'}}

def stopping(zh):
    fig,ax = plt.subplots(figsize=(10.5,4.8))
    fig.subplots_adjust(left=.085,right=.97,bottom=.23,top=.82)
    ax.plot(range(len(path)),path,color=GREY,ls=':',lw=1.15,marker='o',ms=3,mfc='white',label='原路径（细点线）' if zh else 'Original path (thin dotted line)')
    ax.plot(range(tau+1),path[:tau+1],color=TEAL,lw=2.1,label='停止前缀（实线）' if zh else 'Observed prefix (solid line)')
    ax.plot(range(tau,len(path)),stopped[tau:],color=INK,ls='--',lw=1.5,marker='s',mfc='white',ms=4,label='冻结部分（方形点虚线）' if zh else 'Frozen part (dashes and squares)')
    ax.axhline(threshold,color=GREY,lw=.8,ls='-.')
    ax.axvline(tau,color=GREY,lw=.8,ls=':')
    ax.annotate(r'$\tau=7$',xy=(tau,threshold),xytext=(tau+.55,threshold+.65),arrowprops={'arrowstyle':'->','lw':.8},fontsize=12)
    ax.set(xlim=(-.3,len(path)-.65),ylim=(-.3,4.0),xlabel=r'$n$',ylabel=r'$X_n\ ;\ X_{n\wedge\tau}$')
    ax.set_xticks(range(0,len(path),1));ax.set_yticks(range(4));ax.grid(axis='y',lw=.5,ls=':',color='#cccccc')
    ax.legend(frameon=False,loc='lower center',bbox_to_anchor=(.5,1.01),ncol=3,fontsize=8.6)
    fig.suptitle('停止不是删去过去，而是冻结后续本钱' if zh else 'Stopping keeps the past and freezes the subsequent capital',y=.97,fontsize=14)
    fig.text(.5,.095,r'$\tau=\min\{n\geq0:X_n\geq3\},\qquad X_n^\tau=X_{n\wedge\tau}$',ha='center',fontsize=12)
    fig.text(.5,.035,'固定路径示意；不构成可选抽样定理的证明。' if zh else 'A fixed-path illustration, not a proof of optional sampling.',ha='center',fontsize=9)
    return fig

def inspection(zh):
    fig,axes=plt.subplots(1,2,figsize=(11.4,4.9),gridspec_kw={'width_ratios':[1.25,1]})
    fig.subplots_adjust(left=.06,right=.98,bottom=.24,top=.75,wspace=.26)
    ax=axes[0];start=0
    hatches={1:'',2:'//',5:'..'}
    for length in lengths:
        ax.barh(.5,length,left=start,height=.45,color='white',edgecolor=INK,lw=.9,hatch=hatches[length])
        ax.text(start+length/2,.5,str(length),ha='center',va='center',fontsize=10)
        start+=length
    ax.set(xlim=(0,sum(lengths)),ylim=(0,1),xlabel='观察时间 t' if zh else 'Observation time t')
    ax.set_xticks([0,5,10,15,20]);ax.set_yticks([]);ax.spines['left'].set_visible(False)
    ax.set_title('同一组间隔：总长度20' if zh else 'The same intervals: total length 20',fontsize=11)
    ax=axes[1];x=list(range(len(support)));width=.34
    ax.bar([i-width/2 for i in x],[float(p) for p in event_weights],width,color='white',edgecolor=INK,hatch='//',label='按间隔' if zh else 'By intervals')
    ax.bar([i+width/2 for i in x],[float(p) for p in time_weights],width,color='white',edgecolor=INK,hatch='..',label='按时间' if zh else 'By time')
    for i,(e,t) in enumerate(zip(event_weights,time_weights)):
        ax.text(i-width/2,float(e)+.018,f'{float(e):.1f}',ha='center',fontsize=9)
        ax.text(i+width/2,float(t)+.018,f'{float(t):.1f}',ha='center',fontsize=9)
    ax.set(ylim=(0,.72),xlabel='所处间隔的总长度' if zh else 'Total length of the containing interval',ylabel='概率' if zh else 'Probability')
    ax.set_xticks(x,[str(k) for k in support]);ax.legend(frameon=False,ncol=2,fontsize=9,loc='upper center',bbox_to_anchor=(.5,1.18))
    ax.grid(axis='y',ls=':',lw=.5,color='#cccccc');ax.set_axisbelow(True)
    fig.suptitle('较长的间隔，更容易被随机时刻撞见' if zh else 'A random time is more likely to fall in a longer interval',fontsize=14,y=.97)
    fig.text(.5,.115,'事件权重：次数 / 10；时间权重：长度 × 次数 / 20。' if zh else 'Event weight = count / 10; time weight = length × count / 20.',ha='center',fontsize=10)
    fig.text(.5,.055,'确定性有限示意；总间隔长度不等于余寿命，也不是更新极限定理的证明。' if zh else 'A finite deterministic illustration: interval length is not residual life; no renewal limit theorem is proved.',ha='center',fontsize=9)
    return fig

def family(zh):
    fig,ax=plt.subplots(figsize=(9.2,6.0));fig.subplots_adjust(left=.08,right=.87,bottom=.2,top=.85)
    for n in nodes:
        for child in n['children']:
            c=nodes[child]
            ax.plot([n['x'],c['x']],[n['generation'],c['generation']],color=INK,lw=.9)
    for n in nodes:
        ax.plot(n['x'],n['generation'],'o',ms=5.6,mfc='white' if n['generation']==depth else INK,mec=INK,mew=1.0)
    for g,z in enumerate(population):ax.text(leaf_counter+.25,g,rf'$Z_{g}={z}$',va='center',fontsize=11)
    ax.axhline(depth+.32,color=GREY,lw=.8,ls='--')
    ax.set(xlim=(-.5,leaf_counter-.15),ylim=(depth+.7,-.5),ylabel='代数 n' if zh else 'Generation n')
    ax.set_xticks([]);ax.set_yticks(range(depth+1));ax.spines['bottom'].set_visible(False)
    fig.suptitle('平均子女数为1，不等于每一代人数不变' if zh else 'Mean offspring 1 does not make generation sizes constant',fontsize=14,y=.96)
    fig.text(.5,.115,r'$p_0=p_2=1/2,\qquad m=1,\qquad \mathrm{seed}=20261027$',ha='center',fontsize=11)
    fig.text(.5,.062,'空心点：第6代观察边界，尚未抽样其后代。有限模拟不证明灭绝结论。' if zh else 'Open circles: generation-6 observation boundary; offspring not sampled. A finite simulation does not prove extinction.',ha='center',fontsize=8.8)
    return fig

builders={'stopping-prefix':stopping,'inspection-length-bias':inspection,'finite-gw-family':family}
files={}
for key,builder in builders.items():
    for lang in ['zh','en']:
        fig=builder(lang=='zh');stem=BASE/f'{key}.{lang}'
        fig.savefig(str(stem)+'.svg',metadata={'Date':'2026-10-27','Creator':'The Mathematics of Chance reproducible process figure'})
        fig.savefig(str(stem)+'.pdf',metadata={'Creator':'The Mathematics of Chance','CreationDate':DATE,'ModDate':DATE})
        fig.savefig(QA/f'{key}.{lang}.png',dpi=150)
        # Inspectable grayscale QA without relying on colour to distinguish objects.
        for artist in fig.findobj():
            if hasattr(artist,'get_color') and hasattr(artist,'set_color'):
                try:artist.set_color('#222222')
                except (ValueError,TypeError):pass
            if hasattr(artist,'set_markeredgecolor'):
                try:artist.set_markeredgecolor('#222222')
                except (ValueError,TypeError):pass
        fig.savefig(QA/f'{key}.{lang}.grayscale.png',dpi=150);plt.close(fig)
        for ext in ['svg','pdf']:
            name=f'assets/visuals/batch16-20/{key}.{lang}.{ext}'
            files[name]={'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
    entries[key].update({'id':key,'model':models[key],'print':{lang:{ext:f'assets/visuals/batch16-20/{key}.{lang}.{ext}' for ext in ['svg','pdf']} for lang in ['zh','en']},
        'interactive':None,'author_adoption':'PENDING_AUTHOR_READING','rendering':'white static panel in both light and dark reader themes; lines/markers/hatches also distinguish grayscale'})

data_path=BASE/'models.json';data_path.write_bytes((json.dumps(models,ensure_ascii=False,indent=2)+'\n').encode())
source='tools/generate-batch-process-figures.py'
for name in [source,'assets/visuals/batch16-20/models.json']:
    files[name]={'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
manifest={'generator':source,'command':'python tools/generate-batch-process-figures.py','matplotlib_version':matplotlib.__version__,
    'font_sha256':hashlib.sha256(font.read_bytes()).hexdigest(),'font_notice':'assets/visuals/font-notice.txt',
    'figures':list(entries.values()),'files':files,'checks':['first hitting time exactly7','stopped prefix and constant tail',
        'exact rational interval and time weights each sum1','containing-length means2 and16/5','GW generation counts and parent-child consistency',
        'generation6 offspring explicitly unobserved','grayscale QA PNG generated'],'scope':'Optional local author-review assets, not published or author-adopted; no infinite theorem is proved by the figures.'}
(BASE/'manifest.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'figures':len(entries),'vector_files':12,'checks':'PASS','manifest':'assets/visuals/batch16-20/manifest.json'}))
