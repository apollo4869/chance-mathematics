"""Targeted text/probability regression checks and volume VII working-draft adoption."""
from pathlib import Path
from fractions import Fraction
from html import escape
import hashlib,json,re,xml.etree.ElementTree as ET
from .volume7 import R,A,hit_values,hit_conclusion,write
from .volume7_review import P,shell,build

O=R/'reports/volume7-visual-closeout-2026-11-06'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jsave(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def svg_text(p):return [n.text or '' for n in ET.parse(p).getroot().iter() if n.tag.endswith('text')]

REMAINING=[
 dict(chapter=48,sections=['48.14','48.15'],priority='P2 非阻塞候选',topic='点映射制造重数、集中无限来源破坏局部有限性；独立稀释为什么不等于随意删点',gain='与V48的联合计数区别开：展示映射／删点机制如何改变合法性及独立性。',decision='登记，不制作；已有V48和严格证明足以支持当前阅读。'),
 dict(chapter=49,sections=['49.11','49.12','49.13'],priority='P2 非阻塞候选',topic='同一个核：质量平滑与逐点独立散射',gain='平滑是条件平均，散射每次实现仍是整数点；不重复V49的紧窗质量比较。',decision='剩余候选中教学增益较高；需要新授权，当前不生产。'),
 dict(chapter=50,sections=['50.15','50.16','50.20'],priority='P3 复用／技术文字',topic='复用P03；一般Palm核和Papangelou的参考测度条件',gain='P03已经解释典型事件与典型时间；一般核的条件须准确阅读。',decision='不重做同义抽样图；析取、共同零集和绝对连续性证明无需机械配图。'),
 dict(chapter=51,sections=['51.19','51.20','51.21'],priority='P2 非阻塞候选',topic='小质量幽灵支撑与交集映射的不连续',gain='区别于V51的容量识别：测度读数收敛未必控制支撑几何，边界会影响集合运算。',decision='登记；不从已采用图再扩写新故事，不立即制作。'),
 dict(chapter=52,sections=['52.13','52.18'],priority='P3 可选深入',topic='轮廓最低值与先序高度最低值的端点修正；编号切口与不同旋转词',gain='V52已覆盖三种编码和时钟，V53已画编号切口；后续必须有新的祖先公式或周期计数收益才值得配图。',decision='不重画三编码／同义循环图；算法和循环引理的逐行证明不必各配一图。'),
 dict(chapter=53,sections=['53.16','53.18','53.20'],priority='P2 技术阅读候选',topic='条件祖先链、共同祖先与从典型点误差提升到一致误差',gain='V53只揭示高度不自动收敛；若画，应解释额外估计怎样补足该缺口。',decision='保持为技术阅读密度观察项；不以示意图替代高度紧性证明或独立专家终审。')]

def closeout():
 expected={
  'zh':['高度相同：共同命中概率2/5','高度分离：共同命中概率0','高度重叠：共同命中概率1/4'],
  'en':['Same heights: P(both)=2/5','Separated heights: P(both)=0','Overlapping heights: P(both)=1/4']}
 checked=[]
 for lg in ['zh','en']:
  for case,value in enumerate([Fraction(2,5),Fraction(0),Fraction(1,4)]):
   assert hit_values(case)[3]==value and hit_conclusion(lg,case)==expected[lg][case]
   for u in range(21):
    for size in ['desktop','mobile']:
     p=A/f'V51-{lg}-{case}-{u}-{size}.svg';texts=svg_text(p)
     assert texts[-1]==expected[lg][case]
     assert not any(t in ['空间不交，仍能同时命中','Disjoint windows can both be hit'] for t in texts)
     checked.append(p.name)
   assert expected[lg][case] in svg_text(A/f'V51.{lg}.page{case+1}.svg')
   assert expected[lg][case] in svg_text(A/f'V51.{lg}.svg')
  for preset in range(3):
   for size in ['desktop','mobile']:
    copied=svg_text(A/f'V48-{lg}-copied-{preset}-{size}.svg');independent=svg_text(A/f'V48-{lg}-independent-{preset}-{size}.svg')
    note='V未使用；两区计数都只由U生成' if lg=='zh' else 'V unused; both counts use U'
    assert note in copied and note not in independent
  assert note in svg_text(A/f'V48.{lg}.svg') and note in svg_text(A/f'V48.{lg}.page2.svg')
 frozen=json.loads((O/'protected-adopted-assets.json').read_text('utf8'))
 assert all(sha(R/p)==h for p,h in frozen.items())
 old=json.loads((O/'registry-before.json').read_text('utf8'))
 path=R/'publication/explanatory-volume7-batch1-working.json';reg=json.loads(path.read_text('utf8'))
 for before,row in zip(old['figures'],reg['figures']):
  assert (before['id'],before['lang'])==(row['id'],row['lang'])
  if row['id'] in ['V49','V52','V53']:assert before['html']==row['html'] and before['condition']==row['condition']
  row['status']='adopted as current visual working draft; final aesthetics, real devices, native PDF, browser and expert mathematical review remain open'
  if row['id']=='V51':row['status']+='; required scenario-label correction applied'
 reg['adoption']=dict(reviewed_artwork_commit='69f0b1ac',date='2026-11-06',scope='author adoption as visual working drafts; V51 scenario-label fix and V48 unused-V clarification applied',phase='volume VII high-priority visual optimization provisionally complete',browser='pending; no browser retry this round',new_volume8_work=False)
 jsave(path,reg)
 build()  # Refresh chapter/print overlays only; never regenerates protected figures.
 for lg in ['zh','en']:
  html=(P/'print/figures'/f'V51.{lg}.html').read_text('utf8')
  assert all(f'V51.{lg}.page{n}.svg' in html for n in [1,2,3])
 jsave(O/'remaining-priorities.json',REMAINING)
 original_receipt=R/'deliverables/volume7-visual-review-69f0b1ac-r1-20261106-receipt.json'
 preserved_zip=None
 if original_receipt.exists():
  receipt=json.loads(original_receipt.read_text('utf8'));assert sha(Path(receipt['zip']))==receipt['sha256']
  preserved_zip=dict(version=receipt['version'],sha256=receipt['sha256'],unchanged=True,note='Historical review ZIP preserved; it predates these corrections and is not relabelled as the revised version.')
 jsave(O/'targeted-verification.json',dict(scope='finite model and source/SVG checks; not browser or independent expert review',V51=dict(joint_probabilities=['2/5','0','1/4'],bilingual_interactive_states_checked=len(checked),three_static_cases_checked=True,incorrect_generic_footer_removed=True),V48=dict(copied_states_checked=12,unused_V_explicit=True,counts_and_probabilities_unchanged=True),protected_assets=len(frozen),V49_V52_V53_fragments_unchanged=True,historical_zip=preserved_zip,browser=dict(retried=False,status='pending; previous interface denied local browser use',screenshots=0),publication=False,push=False))
 content='<nav><a href="/review/">总览 / Review</a><a href="/review/figures/V51.zh.html">V51 中文</a><a href="/review/figures/V51.en.html">V51 English</a><a href="/review/figures/V48.zh.html">V48 中文</a></nav><h1>第七卷视觉工作稿：定点修正与阶段性收束</h1><p>五组采用为当前视觉工作稿。V51共同命中概率依场景为2/5、0、1/4；V48复制模型明确V未使用。V49、V52、V53原图和交互机制受保护。浏览器／真机／原生PDF和最终审美仍待验收，本轮不重试浏览器。</p><h2>剩余候选：登记而不制作</h2>'
 for row in REMAINING:content+=f'<section><h3>第{row["chapter"]}章 · {escape(row["priority"])}</h3><p>{escape(row["topic"])}</p><p>{escape(row["decision"])}</p></section>'
 write(P/'review/closeout.html',shell('第七卷视觉工作稿收束',content))
 print(f'V51: {len(checked)} bilingual state labels checked; V48: 12 copied states; {len(frozen)} adopted assets byte-identical. No browser retry.')

if __name__=='__main__':closeout()
