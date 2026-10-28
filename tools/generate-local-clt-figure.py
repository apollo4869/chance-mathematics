"""Exact lattice masses and local Gaussian approximation: bilingual SVG/vector PDF.

Uses the installed publication font/runtime; never regenerates the six old groups.
Run: python tools/generate-local-clt-figure.py
"""
from pathlib import Path
from fractions import Fraction
import datetime,hashlib,json,math,os,sys
ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'qa/matplotlib-config'))
sys.path.insert(0,str(ROOT/'qa/visual-runtime'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
BASE=ROOT/'assets/visuals';OUT=BASE/'print';QA=ROOT/'qa/local-clt';QA.mkdir(parents=True,exist_ok=True)
font=next(iter((ROOT/'qa/math-visuals').glob('CJK-Regular-*-stable-head-v1.ttf')),None)
if font is None:
    original=Path(os.environ.get('CHANCE_CJK_FONT',r'C:\Windows\Fonts\NotoSansSC-VF.ttf'))
    if not original.exists():raise SystemExit('Set CHANCE_CJK_FONT to an installed publication-compatible CJK font.')
    f=TTFont(original,recalcTimestamp=False)
    if 'fvar' in f:f=instantiateVariableFont(f,{'wght':400},inplace=True)
    f.recalcTimestamp=False;font=QA/'CJK-Regular.ttf';f.save(font)
font_manager.fontManager.addfont(str(font));family=font_manager.FontProperties(fname=font).get_name()
plt.rcParams.update({'font.family':family,'svg.fonttype':'path','svg.hashsalt':'chance-local-clt-v1','pdf.fonttype':42,'ps.fonttype':42,'font.size':10,'axes.spines.right':False,'axes.spines.top':False,'axes.linewidth':.8,'figure.facecolor':'white','savefig.facecolor':'white'})
spec={'id':'local-clt-parity','steps':[20,21],'display_k':[-10,10],'maximal_span':2,'step_mean':0,'step_variance':1,'randomness':'none; exact binomial probabilities','approximation':'2/sqrt(n) * phi(k/sqrt(n)); only at k congruent n mod2','not_claimed':'A finite plot is not a local-CLT proof, error-rate bound, or continuous-Gaussian TV convergence.'}
rows=[]
for n in spec['steps']:
    masses=[]
    for k in range(-n,n+1):
        numerator=math.comb(n,(n+k)//2) if (n+k)%2==0 else 0
        masses.append({'k':k,'allowed':(k-n)%2==0,'numerator':numerator,'denominator':2**n,'mass':numerator/2**n,'local_gaussian':2/math.sqrt(n)*math.exp(-k*k/(2*n))/math.sqrt(2*math.pi) if (k-n)%2==0 else None})
    weights=[Fraction(x['numerator'],x['denominator']) for x in masses]
    assert sum(weights)==1 and sum(w*x['k'] for w,x in zip(weights,masses))==0
    assert sum(w*x['k']**2 for w,x in zip(weights,masses))==n
    allowed=[x['k'] for x in masses if x['mass']>0];assert math.gcd(*(b-a for a,b in zip(allowed,allowed[1:])))==2
    assert next(x['mass'] for x in masses if x['k']==0)>0 if n%2==0 else next(x['mass'] for x in masses if x['k']==0)==0
    rows.append({'n':n,'full_support':masses,'omitted_display_mass':sum(x['mass'] for x in masses if abs(x['k'])>10)})
(BASE/'local-clt-data.json').write_bytes((json.dumps({'spec':spec,'rows':rows},ensure_ascii=False,indent=2)+'\n').encode())
for lang in ['zh','en']:
    zh=lang=='zh';fig,axes=plt.subplots(1,2,figsize=(11.4,4.8),sharex=True,sharey=True)
    fig.subplots_adjust(left=.085,right=.98,bottom=.26,top=.73,wspace=.14)
    fig.suptitle('钟形轮廓相似，允许格点却随奇偶改变' if zh else 'A similar bell shape, but different allowed lattice points',fontsize=14,y=.97)
    for ax,row in zip(axes,rows):
        n=row['n'];m=[x for x in row['full_support'] if abs(x['k'])<=10];yes=[x for x in m if x['allowed']];no=[x for x in m if not x['allowed']]
        x=[a['k'] for a in yes];p=[a['mass'] for a in yes];g=[a['local_gaussian'] for a in yes]
        ax.axhline(0,color='#777777',lw=.7);ax.axvline(0,color='#bbbbbb',lw=.6,ls=':')
        ax.vlines(x,0,p,color='#182a29',lw=1.1)
        exact=ax.plot(x,p,'o',color='#182a29',ms=4,label='精确质量（实心圆）' if zh else 'Exact mass (filled circles)')[0]
        approx=ax.plot(x,g,color='#12635e',ls='--',lw=1.2,marker='D',mfc='none',mec='#12635e',ms=6,label='局部 Gaussian 近似（空心菱形）' if zh else 'Local Gaussian approximation (open diamonds)')[0]
        forbidden=ax.plot([a['k'] for a in no],[0]*len(no),'x',color='#666666',ms=5,label='不允许格点：质量严格为0' if zh else 'Forbidden points: mass exactly zero')[0]
        if zh:ax.set_title(f'n = {n}：'+('仅偶数位置可达' if n%2==0 else '仅奇数位置可达'),fontsize=11)
        else:ax.set_title(f'n = {n}: '+('even positions only' if n%2==0 else 'odd positions only'),fontsize=11)
        ax.set(xlim=(-10.7,10.7),ylim=(-.012,.205),xlabel=r'$k$');ax.set_xticks(range(-10,11,2));ax.set_yticks([0,.05,.10,.15,.20]);ax.grid(axis='y',ls=':',lw=.55,color='#cccccc');ax.set_axisbelow(True)
    axes[0].set_ylabel('概率质量（不是密度）' if zh else 'Probability mass (not density)')
    fig.legend([exact,approx,forbidden],[x.get_label() for x in [exact,approx,forbidden]],loc='upper center',bbox_to_anchor=(.53,.88),ncol=3,frameon=False,fontsize=8.7,handlelength=2.2)
    line1=r'$P(S_n=k)=2^{-n}\binom{n}{(n+k)/2}$'+'  '+('（仅允许格点）' if zh else '(allowed points only)')
    line2=r'$h=2,\ \sigma=1:\quad P(S_n=k)\approx\frac{2}{\sqrt{n}}\,\varphi(k/\sqrt{n})$'
    fig.text(.5,.12,line1,ha='center',fontsize=10);fig.text(.5,.055,line2,ha='center',fontsize=11)
    prefix=OUT/('local-clt-parity.'+lang)
    fig.savefig(str(prefix)+'.svg',metadata={'Date':'2026-10-27','Creator':'The Mathematics of Chance exact lattice figure'})
    fig.savefig(str(prefix)+'.pdf',metadata={'Creator':'The Mathematics of Chance','CreationDate':datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc),'ModDate':datetime.datetime(2026,10,27,tzinfo=datetime.timezone.utc)})
    fig.savefig(QA/('local-clt-parity.'+lang+'.png'),dpi=160)
    for artist in fig.findobj():
        if hasattr(artist,'get_color') and hasattr(artist,'set_color'):
            try:artist.set_color('#222222')
            except (ValueError,TypeError):pass
        if hasattr(artist,'set_markeredgecolor'):
            try:artist.set_markeredgecolor('#222222')
            except (ValueError,TypeError):pass
    fig.savefig(QA/('local-clt-parity.'+lang+'.grayscale.png'),dpi=160);plt.close(fig)
names=['assets/visuals/local-clt-data.json','tools/generate-local-clt-figure.py']+[f'assets/visuals/print/local-clt-parity.{lang}.{ext}' for lang in ['zh','en'] for ext in ['svg','pdf']]
manifest={'id':spec['id'],'generator':'tools/generate-local-clt-figure.py','model':spec,'matplotlib':matplotlib.__version__,'font_sha256':hashlib.sha256(font.read_bytes()).hexdigest(),'font_notice':'assets/visuals/font-notice.txt','files':{n:{'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in names},'checks':['exact rational total1','mean0','variance n','maximal span2','parity at0','no simulation'],'author_adoption':'PENDING_REVIEW_OF_NEW_FIGURE'}
(BASE/'local-clt-manifest.json').write_bytes((json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'local_clt_figure':'GENERATED','exact_models':2,'vector_files':4,'randomness':'NONE'}))
