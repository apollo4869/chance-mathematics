"""One-time, explicitly author-authorized restructuring, from the tagged long draft.
Never deploys. Every advanced span is copied verbatim, with independent hash evidence.
"""
from pathlib import Path
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
TAG='snapshot/long-manuscript-before-brownian-2026-10-25'
def old(p):return subprocess.check_output(['git','-C',str(ROOT),'show',TAG+':'+p])
sha=lambda b:hashlib.sha256(b).hexdigest()
def write(p,s):
    t=ROOT/p;t.parent.mkdir(parents=True,exist_ok=True);t.write_bytes(s.encode('utf-8'))
original=old('chapters/04-brownian.md');s=original.decode('utf-8');nl='\r\n' if '\r\n' in s else '\n'
archive='archives/before-brownian-restructure/04-brownian.md'
(ROOT/archive).parent.mkdir(parents=True,exist_ok=True);(ROOT/archive).write_bytes(original)
baseline_old=old('baseline-manuscript.json');(ROOT/'archives/before-brownian-restructure/baseline-manuscript.json').write_bytes(baseline_old)
def at(marker):return s.index(marker)
def span(start,end):return s[at(start):at(end)]
rows=[];modules=[]
specs=[
('donsker','Donsker 与路径紧性','## 4.7 Donsker','## 4.8 我们终于',
 '第12章《分布进入函数空间》；第27章《离散路径为什么趋向连续路径》',
 '第7章收敛、函数空间可测性、Arzelà–Ascoli、Prokhorov 与 Kolmogorov 紧性准则。',
 '保留插值、四阶矩计算与全部原推导。原稿仍调用紧性准则与弱极限识别工具，并非已经给出 Donsker 的完整自足证明；一般有限二阶矩情形也尚需补证。'),
('wiener','连续版本与 Wiener measure','### 4.8.1 连续的','## 4.9 从随机游走',
 '第8章《从局部规则构造无限实验》；第24章《连续随机路径的严格诞生》',
 '测度扩张、Gaussian 向量、一致有限维分布、Kolmogorov 连续修正及路径映射可测性。',
 '原稿中的“得到”“构造”是调用扩张与连续修正定理后的条件性结论；这些定理的证明并未在第四章完成。这里完整保存构造路线，不将其冒充已完成的 Wiener 测度构造。'),
('semigroup','从随机运动到半群与生成元','### 4.9.3 一个统一','## 4.10 连续',
 '第20章《只记住现在的系统》；第31章《概率演化与确定性方程》',
 'Lebesgue 积分、条件分布、Markov 性、算子半群与生成元定义域。',
 '半群与生成元原推导完整后移；本模块以已经构造的 Brownian motion 为前提，不声称第四章已建立半群理论。'),
('quadratic','路径粗糙性、平方变差与 Itô 动机','## 4.10 连续','## 4.11 为什么随机路径',
 '第24章路径正则性；第28章《不能用普通微积分累积的噪声》；第29章《二阶变化留下的项》',
 'Brownian motion 的存在、L2 收敛、Borel–Cantelli、随机积分与 Itô 公式。',
 '原文开头“现在，我们已经真正构造出了”沿用旧章语境，仅在完成上述构造后成立。固定时刻差商论证不能代替几乎必然处处不可导证明；平方变差的原证明固定 T 且沿二进网格；Itô 公式仍为预告。'),
('reflection','首次到达与反射原理','## 4.11 为什么随机路径','## 4.12 为什么 Brownian',
 '第25章《到达、反射与路径分解》',
 '连续路径、停止时刻、自然滤过、强 Markov 定理及反射变换的保测性。',
 '原有反射叙述、公式与首次到达时间计算全部保留。强 Markov 性及反射变换保测性仍需系统证明，不把图形对称性当作完整证明。'),
('crt','从 Brownian 路径到随机树','## 4.12 为什么 Brownian','# 第四章结语',
 '第25章 excursion 与路径分解；第43章路径编码；第45章实树；第46章 Brownian CRT（沿既有草案位置）',
 'excursion、伪距离及商空间、实树性质、归一化与函数空间弱收敛。',
 '旧节开头“已经发展出”的清单是旧稿回顾，不是当前阅读版的完成清单。树编码公式与 SVG 示意原样保存；CRT 构造与极限定理尚未在六章内证明。'),
]
for slug,title,start,end,dest,prereq,boundary in specs:
    raw=span(start,end);file='advanced/'+slug+'.md';id='advanced-'+slug
    header=(f'# 进阶阅读：{title}\n\n> 本模块完整迁移自调整前第四章，保留旧节号和全部原文。它是供后续章节接续的技术工作稿，不属于当前第四章的必读证明。\n\n'
      f'**目的章节：**{dest}。\n\n**前置：**{prereq}\n\n**证明边界：**{boundary}\n\n'
      '[返回第四章阅读主线](#chapter-4) · [查看旧第四章完整快照](/downloads/04-brownian-before-restructure.md)\n\n---\n\n')
    write(file,header.replace('\n',nl)+raw)
    modules.append({'id':id,'file':file,'title':'进阶阅读：'+title,'slug':slug})
    rows.append({'source':'chapters/04-brownian.md','source_snapshot':TAG,'start_line':s[:at(start)].count('\n')+1,'end_line':s[:at(end)].count('\n'),
        'start_byte':len(s[:at(start)].encode()),'end_byte':len(s[:at(end)].encode()),'sha256':sha(raw.encode()),'destination':file,'destination_chapters':dest,'proof_boundary':boundary,'verbatim':True})
# Retain the long problem-driven development, then core definition and heat motivation.
front=s[:at('## 4.7 Donsker')]
front=front.replace('一条连续却几乎处处无法用速度描述的路径，是如何从最简单的随机跳跃中诞生的？','一张张 Gaussian 分布的快照，能否拼成一条真正的随机路径？')
front=front.replace('首先，我们可以利用一致的有限维分布，通过概率测度的扩张定理构造一个随机过程。','后续在适用的状态空间条件下，我们将用概率测度的扩张定理，把一致的有限维分布放进同一个随机过程。这里先辨认构造必须解决的问题，不预先调用这一定理来宣布构造完成。')
front=front.replace('因此，对于随机过程，我们需要一套新的收敛理论。','因此，对于随机过程，我们需要一套新的收敛理论。第七章将先辨清各种随机收敛，后续再把这些问题放进函数空间。')
finite_note=r'''
> 这里用特征函数从增量的极限走到向量的联合极限，调用了多维特征函数连续性定理及连续线性映射的分布收敛性质；它们将在第9、11章系统建立，收敛语言从第7章开始。附录 F 保留乘积分解计算。本节完成的是给定这些工具后的有限维极限论证，不是路径极限定理。

'''.replace('\n',nl)
front=front.replace('### 4.5.3 协方差结构自然出现',finite_note+'### 4.5.3 协方差结构自然出现')
boundary=r'''
这里必须分清两个障碍。只有单个时刻的分布，连不同时刻之间怎样关联都不知道；知道全部有限维分布之后，还必须选定路径空间并建立相应的可测结构与正则性。

刚才的随机尖峰不是说连续路径的概率规律永远不能由有限维分布决定。若已经把过程建立为连续函数空间上的 Borel 随机元素，所有有限维分布便能够决定它的路径分布；证明这一点需要后文的可测结构。反例说明的是：不能在没有说明路径空间与版本的情况下，从有限维信息直接宣告路径连续。

**一张张快照可以告诉我们粒子出现在哪里，却还不能自动给出一条可以谈论“曾经到达”“始终停留”的随机路径。**

这就是本章真正的转折。Gaussian 极限没有失效；它把我们带到了自己无法独自回答的问题面前。

'''.replace('\n',nl)
front+=boundary
definition=span('## 4.8 我们终于','### 4.8.1 连续的').replace('## 4.8 我们终于可以定义 Brownian motion 了','## 4.7 我们希望找到的连续随机运动')
for number in range(1,5):
    definition=definition.replace(f'{nl}{number}. ',f'{nl}{nl}**{number}.** ')
definition=definition.replace(f'相互独立；{nl}',f'相互独立；{nl}{nl}')
definition+=r'''
这四条是我们向极限对象提出的要求，还不是它存在的证明。第四条尤其不能由前面几张 Gaussian 快照自动推出。

本章不再把严格构造压进这个定义之后。后续我们将分别解决：如何把一致的有限维分布扩张成概率测度，如何选择连续版本，以及随机游走的整条路径为什么能趋向这个过程。原有构造路线与技术计算完整保存在[连续版本与 Wiener measure 模块](#advanced-wiener)和[Donsker 与路径紧性模块](#advanced-donsker)中。

---

'''.replace('\n',nl)
heat=span('## 4.9 从随机游走','### 4.9.3 一个统一').replace('## 4.9 ','## 4.8 ').replace('### 4.9.1 ','### 4.8.1 ').replace('### 4.9.2 ','### 4.8.2 ')
heat=heat.replace('到目前为止，我们沿着随机路径的路线，建立了 Brownian motion。','到目前为止，我们沿着随机游走的路线，辨认出了 Brownian motion 应当满足的要求；它的严格存在性仍留待后文建立。')
ending=r'''
从随机跳跃得到的密度，竟然满足一个确定性的扩散方程。对标准 Brownian motion，这里的系数是 \(D=1/2\)；一般的 \(D>0\) 对应过程 \(\sqrt{2D}\,B_t\)。这解释了我们为什么既追问粒子的随机轨迹，又研究分布随时间的确定性演化。

但验证 Gaussian 密度满足热方程，并不能替代连续随机路径的存在证明。密度描述每一时刻的分布；路径如何把这些时刻连接起来，仍是刚才留下的问题。半群、生成元与更深的随机微积分联系，已完整移入[半群与生成元模块](#advanced-semigroup)，等待相应工具建立。

## 4.9 当“曾经发生”成为一个事件

假如一个粒子最后回到了原点附近，我们能否就说它从未走远？

当然不能。它可能曾经越过一条高线，随后又回来。最终位置只留下最后一张快照；“曾经越过”则需要整条路径。

假定我们已经有一条连续的 Brownian 路径，在 \([0,1]\) 上问：

\[
A=\left\{\omega:\sup_{0\le t\le1}B_t(\omega)>1\right\}.
\]

这个集合装着的不是一串可能的骰子点数，而是一整批具有某种经历的函数。我们想写下 \(P(A)\)，却必须先回答：哪些路径集合允许赋予概率？这个 \(A\) 为什么属于其中？

连续性在这里给了我们一个线索。若一条连续路径在某时刻严格高于1，那么它在附近的某个有理时刻也高于1。因此，对于连续路径，

\[
\left\{\sup_{0\le t\le1}B_t>1\right\}
=\bigcup_{q\in\mathbb Q\cap[0,1]}\{B_q>1\}.
\]

右边只需可数多个观察时刻。这里在连续路径空间中逐条路径理解这个等式；若过程只保证几乎必然连续，等式就在同一个概率为1的连续性事件上成立。连续性与严格不等号都起作用，不能把这个推理无条件套在先前的随机尖峰上。我们还没有用这个等式算出概率，但它已经指出：要描述整条路径，哪些集合运算应当仍然产生可讨论的事件。

我们需要的语言必须容纳补集、可数并和极限；也需要说明为什么连续函数上的最大值可以作为随机量。第五章将从允许讨论的集合开始，第六章再建立对函数求平均的积分语言，第七章继续进入各种随机收敛。此后我们才有条件返回 Brownian motion，补全构造和路径极限。

## 第四章结语：先看见路径的问题

第一章从一场没有结束的赌博追问公平，第二章追问未知机会怎样被观察更新，第三章从许多独立误差中发现 Gaussian 极限。

现在，我们把同样的随机增量按时间排列。方差相加给出平方根尺度，中心极限定理给出固定时刻的 Gaussian 分布，独立增量又带来有限维联合结构。

然而，单个时刻的分布不能告诉我们整条路径发生过什么；即使有限维分布已经确定，连续版本和路径收敛也需要额外的理论。Brownian motion 的定义让我们知道要寻找什么，扩散方程让我们看见这个对象与物理规律的联系，却没有替我们完成所有存在性证明。

**读者先遇见的不是一套抽象基础，而是一个已经无法用原有工具完整回答的问题：怎样给无限多条随机路径及其事件赋予概率？**

我们不必在第四章匆忙解决一切。路径的粗糙性、平方变差、Itô 理论、反射和随机树都将在后面回来。它们的原文没有删除，而是沿着各自需要的数学基础，进入下列进阶模块：

- [Donsker 不变性原理与路径紧性](#advanced-donsker)：第12、27章。
- [连续版本与 Wiener measure](#advanced-wiener)：第8、24章。
- [半群、生成元与确定性演化](#advanced-semigroup)：第20、31章。
- [路径粗糙性、平方变差与 Itô 动机](#advanced-quadratic)：第24、28、29章。
- [首次到达与反射原理](#advanced-reflection)：第25章。
- [excursion、实树与 Brownian CRT](#advanced-crt)：第25、43、45、46章。

这些是原技术稿的保留入口；“迁移完成”不表示其中尚未建立的定理已经补证完成，也不表示未来章节已经写成。

---

## 通向第五章：为什么概率需要测度论？

刚才的问题发生在函数空间里。为了看清障碍，我们先退回看起来最简单的无限空间：一个区间。

假如我们希望在 \([0,1]\) 上均匀地选择一个点，那么区间的概率应当等于它的长度。我们还能不能给它的每一个子集都赋予概率，并同时保留长度所要求的平移一致性与可数可加性？这里的平移一致性，是指平移后的集合仍在区间内时应具有相同概率；在整条实数轴上，则对应延伸长度的平移不变测度。

若连这个问题都有边界，随机路径空间便更不能靠“所有集合都算事件”的直觉来处理。第五章将让我们看到，这个限制如何迫使 Borel 集、\(\sigma\)-代数与可测性成为必要的数学语言。

到这里，我们已经知道为什么要转向测度论：我们想真正理解的，仍然是那一颗不停运动的微粒。

[继续阅读第五章](#chapter-5)

《偶然的数学》· 第一卷第四章 · 结构调整阅读候选版，2026-10-25
'''.replace('\n',nl)
write('chapters/04-brownian.md',front+definition+heat+ending)
# Chapter 3: additive annotations only. Its full original text remains in order.
third=old('chapters/03-normal.md').decode('utf-8');n3='\r\n' if '\r\n' in third else '\n'
notes=[('### 3.6.2 用特征函数重新证明中心极限定理',
 r'> 后续理论依赖：以下是对历史结果的现代语言重建，不是 de Moivre 或 Laplace 当年的证明。二阶展开的余项控制见附录 D；复数随机变量的积分语言在第6章建立，特征函数唯一性与 Lévy 连续性定理在第9、11章系统证明，第7章先区分相应收敛概念。本节沿乘积与二阶项的故事继续推导，不把这些外部调用冒充已在本章证明的结论。'),
 ('### 3.7.1 从最佳估计反推出概率分布',
 r'> 阅读路线：这里回到 Gauss 的误差与估计问题，是 Gaussian 规律的另一条历史来源，不是说 Gauss 在现代特征函数证明之后工作。下文的函数方程推导是现代重建；可测加性函数的线性结论仍作为待补工具，相关正则性问题保留在审校问题册。'),
 ('### 3.8.1 Cauchy 分布：一个不会被平均驯服的随机变量',
 r'> 后续理论依赖：本例的特征函数公式与由特征函数识别分布，仍按已知结果使用，计算及唯一性理论安排在第9章；不因这里展示一个反例就宣称相应理论已经建立。')]
for anchor,note in notes:
    assert third.count(anchor)==1
    third=third.replace(anchor,note+n3+n3+anchor)
write('chapters/03-normal.md',third)
inputs=json.loads(old('provenance/build-inputs.json'))
inputs['advanced_modules']=modules
write('provenance/build-inputs.json',json.dumps(inputs,ensure_ascii=False,indent=2)+'\n')
manifest={'authorization':'2026-10-25 author explicitly requested Chapter 4 restructuring and full relocation; local-only.',
 'snapshot_tag':TAG,'snapshot_commit':subprocess.check_output(['git','-C',str(ROOT),'rev-parse',TAG],text=True).strip(),
 'full_original_archive':archive,'original_sha256':sha(original),'original_chat_equivalence':'UNVERIFIED',
 'unchanged_chapters':[1,2,5,6],'chapter3_change':'additive dependency annotations only','chapter7':'convergence; no prose authored',
 'moves':rows,'replaced_context_retained_in_full_archive':['opening question','extension forward call','old conclusion and next-chapter preview'],
 'author_reading_approval':[1,2],'revised_chapter4_author_acceptance':'PENDING'}
write('docs/brownian-relocation.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
baseline=json.loads(baseline_old)
baseline['author_policy']='Explicit 2026-10-25 authorization: Chapter 4 redistribution; Chapter 3 dependency notes only. No publication. Other body changes require approval.'
baseline['previous_baseline']='archives/before-brownian-restructure/baseline-manuscript.json'
for p in ['chapters/03-normal.md','chapters/04-brownian.md','provenance/build-inputs.json']+[x['file'] for x in modules]+[archive,'archives/before-brownian-restructure/baseline-manuscript.json']:
    baseline['files'][p]=sha((ROOT/p).read_bytes())
write('baseline-manuscript.json',json.dumps(baseline,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'moved_modules':len(rows),'full_original_archive_sha256':sha(original),'new_chapter4_bytes':(ROOT/'chapters/04-brownian.md').stat().st_size},ensure_ascii=False))
