# 第二十六章：连续的路径为什么如此粗糙？

把一条随机游走的折线不断放大，细小的棱角并没有消失；新的棱角总会在更细的尺度出现。第25章证明的是这些路径的概率规律趋于Brownian motion，并没有保证微观的斜率也趋于某个答案。现在，连续的极限已经存在，我们可以真正问：这条曲线在任何一处会变得平滑吗？

还有一种更直接的观察。粒子第一次碰到一条水平线以后，后面的运动是否真的像重新开始？第一次碰到与最后一次碰到，看起来只差一个词，却需要完全不同的数学理由。要研究粗糙的路径，先得知道什么时候可以合法地把它切开。

## 26.1 Gaussian增量还没有告诉我们的事情

<a id="brownian-rough-question"></a>

以下B是从0出发、方差参数为1的实标准Brownian motion，采用连续路径版本。对固定t和h>0，差商\((B_{t+h}-B_t)/h\)服从\(N(0,1/h)\)。它的分布越来越分散。若右导数有限，差商在所有充分小h必被某个整数M控制；但对每个M，这种最终受控事件的概率至多\(\liminf_{n\to\infty}P\!\left(\left|\frac{B_{t+1/n}-B_t}{1/n}\right|\le M\right)=0\)。因此在这个固定t，有限右导数存在的概率为0。

但这还不是“路径处处不可微”。对每个确定t得到一个零概率坏集，再对不可数个t取并，结果未必仍是零集。第23章已经展示过这种危险。我们最终需要排除的是：一条路径能否偷偷在某个依赖于它自己的时刻具有有限斜率。这个量词的变化，是本章第一项真正的证明困难。

同样，确定时刻以后的独立增量，并不自动准许在第一次命中时刻以后重新开始。命中时刻本身由整段过去选择；需要先把这种选择化为可数、可核查的步骤。

## 26.2 什么信息允许我们承认已经到达

<a id="brownian-filtration"></a>

取自然滤过\(\mathcal F_t=\sigma(B_s:0\le s\le t)\)，也可以统一加入原概率空间的零集。这里不预先要求右连续增广，更不借用后面章节的一般连续时间正则化。若任意t都有{T≤t}∈\(\mathcal F_t\)，就称T为停止时刻，允许T=∞。第16章的停止σ-代数原样适用：

\[
\mathcal F_T=\{A\in\mathcal F:
A\cap\{T\le t\}\in\mathcal F_t\ \text{for every }t\ge0\}.
\]

\(\mathcal F_T\)记录的是到T为止能够确认的事件。连续适应过程在[0,t]上的联合可测性，可用左网格阶梯逐点逼近证明；所以\(B_{T\wedge t}\)是\(\mathcal F_t\)可测的。对Borel集合C，{\(B_T\)∈C}∩{T≤t}可通过T∧t及{T≤t}表示，故\(B_T\)在{T<∞}上是\(\mathcal F_T\)可测。停止路径的有理坐标\(B_{q\wedge T}\)同样可测：在{T≤t}上用\(B_{q\wedge T\wedge t}\)表示即可。\(C_{\mathrm{loc}}\)的坐标Borel结构再给整条停止路径的可测性。

这一论证依赖我们选择的滤过。若在时刻0就额外透露B₁，未来增量当然不再独立于\(\mathcal F_0\)。所谓“重新开始”是过程与信息结构共同具有的性质，不只是曲线外形的性质。

## 26.3 先把随机时刻推到右边的网格上

<a id="brownian-strong-markov-grid"></a>

先设T有界，令\(T_n=2^{-n}\lceil2^nT\rceil\)。这是有限网格上的停止时刻，\(T_n\downarrow T\)。若A∈\(\mathcal F_T\)，则\(A\cap\{T_n=k2^{-n}\}\)属于\(\mathcal F_{k2^{-n}}\)：对k≥1，将它写成\(A\cap\{(k-1)2^{-n}<T\le k2^{-n}\}\)即可；k=0单独相同处理。于是可以逐格使用确定时刻的独立增量。

\[
\begin{aligned}
&E\!\left[\mathbf1_A f(B_{T_n+s_1}-B_{T_n},\ldots,
B_{T_n+s_r}-B_{T_n})\right]\\
&\quad=\sum_kP(A\cap\{T_n=k2^{-n}\})\,
E f(B_{s_1},\ldots,B_{s_r})
=P(A)E f(B_{s_1},\ldots,B_{s_r}).
\end{aligned}
\]

先取有界连续f。路径连续使左边逐点收敛，有界支配使期望收敛，于是相同恒等式对T成立。有界连续测试函数确定有限维概率测度，再经π–λ定理扩张到Borel柱集。最后用\(C_{\mathrm{loc}}\)的有理评价生成Borel集合，把恒等式扩张到整个未来路径。这里证明的是路径值随机元素的独立性，不只是几个观察点的计算。

## 26.4 强Markov性在无穷时刻处究竟说什么

<a id="brownian-strong-markov"></a>

不先假定T几乎必然有限。对A∈\(\mathcal F_T\)，令\(A_m\)=A∩{T≤m}。它属于\(\mathcal F_{T\wedge m}\)：当t<m时用停止σ-代数定义，当t≥m时用A∩{T≤m}∈\(\mathcal F_m\)。把上一节用于T∧m和\(A_m\)，再令m↑∞，得到真正需要的局部形式。

\[
E\!\left[\mathbf1_A\mathbf1_{\{T<\infty\}}
H\big((B_{T+s}-B_T)_{s\ge0}\big)\right]
=P(A\cap\{T<\infty\})\,E H(B).
\]

它对每个有界Borel路径泛函H成立。在{T=∞}上可任意指定未来路径，指标保证它不影响公式。若T有限的概率为1，便得到通常说法：T以后的增量是一份独立于\(\mathcal F_T\)的标准Brownian motion。这是Brownian的专用强Markov性，已经完整证明；并没有顺便证明任意Markov过程在任意滤过下都有这个性质。

## 26.5 第一次碰到一条线

<a id="brownian-hitting-time"></a>

固定a>0，令\(\tau_a=\inf\{t\ge0:B_t=a\}\)，空集下确界为∞。连续性给\(\{\tau_a\le t\}\)=\(\{\max_{s\le t}B_s\ge a\}\)；最大值可通过有理时刻连同端点t求上确界，故它是停止时刻。在它有限时，连续性又保证\(B_{\tau_a}\)=a。注意我们还没有证明τ_a一定有限，上一节的局部版本正是为避免在这里偷加结论。

与首次命中不同，“T以前最后一次碰到0”必须确认未来不再返回，通常不是停止时刻。把两种时间混用，会使一幅看似正确的路径图掩盖一个错误的条件独立断言。弧正弦律中我们会实际遇到这个区别。

## 26.6 沿第一次命中把未来翻过去

<a id="brownian-reflection"></a>

\[
(R_aB)_t=
\begin{cases}B_t,&t\le\tau_a,\\2a-B_t,&t>\tau_a,\end{cases}
\qquad R_aB=B\ \text{if }\tau_a=\infty.
\]

反射后的曲线仍连续，第一次命中a的时间没有改变，再反射一次就回到原曲线。这个映射也是可测的：每个坐标可按\(\{\tau_a\le t\}\)分开表示，再用路径空间的坐标Borel结构。真正关键的还不是几何上的可逆，而是它是否保持概率。

在\(\{\tau_a<\infty\}\)上，停止以前的路径及\(\tau_a\)本身是\(\mathcal F_{\tau_a}\)可测的，未来\(Z_s=B_{\tau_a+s}-a\)由强Markov性独立，且Z与−Z同分布。对“停止前信息的有界函数乘未来路径的有界函数”，联合期望因而在Z换成−Z以后不变。有限和与单调类定理把它扩张到停止前后路径的任意有界Borel函数；把二者在\(\tau_a\)处拼接，便得到\(R_aB\)与B整条路径同分布。在\(\{\tau_a=\infty\}\)上它们本来相同。

![在首次命中水平线以后反射路径](../assets/visuals/brownian-reflection/reflection.svg)

图26.1　首次命中把路径分成可确认的过去与独立、对称的未来。图中的折线只说明映射：末点x<a被送到2a−x>a。它不是Brownian样本，也不代替强Markov及可测性证明。实线和虚线在黑白印刷中仍可区分。

## 26.7 最大值与首次到达的分布

<a id="brownian-maximum"></a>

令\(M_t=\max_{s\le t}B_s\)。若x<a，反射把\(\{M_t\ge a,B_t\le x\}\)一一送到\(\{B_t\ge2a-x\}\)，因为后一事件的路径必先穿过a。端点正态分布无原子，所以不等号边界不产生额外质量。取x↑a并补上\(B_t\)≥a的一半，得到

\[
\begin{gathered}
P(M_t\ge a,B_t\le x)=P(B_t\ge2a-x)\quad(x<a),\\
P(M_t\ge a)=2(1-\Phi(a/\sqrt t)),\qquad M_t\overset d=|B_t|,\\
P(\tau_a\le t)=2(1-\Phi(a/\sqrt t)),\qquad
P(\tau_a\in dt)=\frac{a}{\sqrt{2\pi}\,t^{3/2}}e^{-a^2/(2t)}\,dt.
\end{gathered}
\]

t↑∞时分布函数趋于1，至此才证明\(\tau_a\)有限几乎必然。密度由对t求导得到，总质量由端点极限保证。相反，等待的平均值是无穷大：\(P(\tau_a>t)=2\Phi(a/\sqrt t)-1\sim\sqrt{2/\pi}\,a/\sqrt t\)，尾积分发散。一次必然到达的事件，可以有无限平均等待。

还得到以后反复使用的估计\(P(\sup_{s\le t}|B_s|>u)\le4e^{-u^2/(2t)}\)。常数4来自正负两个最大值的并集界，不是宣称二者独立。它把单个Gaussian尾部提升成整段路径的振幅控制。

## 26.8 必然赢到a，为什么没有免费收益

<a id="brownian-stopping-expectation"></a>

对有界停止时刻S，取右网格\(S_n\)↓S。离散采样\(B_{k2^{-n}}\)是鞅，第16章有界离散抽样给\(EB_{S_n}=0\)。若S≤H，所有\(S_n\)≤H+1，反射尾界给\(\sup_{u\le H+1}|B_u|\)可积。连续性与DCT于是给\(EB_S=0\)。这个专用论证没有借用尚未建立的一般连续时间抽样定理。

\[
EB_{\tau_a\wedge t}=0\quad(t<\infty),\qquad
B_{\tau_a\wedge t}\longrightarrow a\ \text{almost surely},\qquad EB_{\tau_a}=a.
\]

如果停止族一致可积，第7章Vitali判别就会准许期望通过极限，与上式矛盾。因此这个停止族并不UI。不是Brownian motion在命中以后破坏公平，而是越来越罕见、越来越深的负端路径仍携带期望，不能在极限中直接抛弃。首次命中分布和无界抽样条件，在同一个例子中有了具体内容。

## 26.9 连续性可以强到什么程度

<a id="brownian-holder"></a>

Gaussian矩给\(E|B_t-B_s|^p=c_p|t-s|^{p/2}\)。第23章的连续修改网格证明说明，在每个有限窗口，路径对任意γ<1/2几乎必然γ-Hölder。取p足够大使γ<1/2−1/p；原连续版本与该修改在有理时刻一致，因连续而不可分辨，所以结论适用于同一条路径。再对整数窗口和可数γ↑1/2取交。

这说明路径并不是任意地乱跳：局部位移小于某个随机常数乘\(|t-s|^\gamma\)。但γ达到1/2时，常数能否保持有限？方差的平方根尺度只给典型增量，不控制许多位置中挑出的最大增量。回答之前，先证明更基本的事实：有限斜率在任何位置都不可能出现。

## 26.10 把不可数个可能的切点困在网格里

<a id="brownian-nowhere-differentiable"></a>

固定整数H,M≥1。若某个t∈[0,H]具有有限右导数，则存在δ>0及整数M，使0<u<δ时\(|B_{t+u}-B_t|\le Mu\)。令h=2⁻ⁿ、j=⌊t/h⌋。当4h<δ，t右侧四个网格点(j+1)h,…,(j+4)h都落在控制范围。因此它们之间三个相邻增量，每个绝对值至多8Mh。

对固定j，三个增量独立N(0,h)。正态密度上界给P(|N(0,h)|≤8Mh)≤CM√h，所以三个同时很小的概率≤\(CM^3h^{3/2}\)。可能的j只有H/h+1个；并集界给

\[
P\!\left(\exists j\le H/h:\quad
\bigcap_{i=1}^{3}\{|B_{(j+i+1)h}-B_{(j+i)h}|\le8Mh\}\right)
\le C_HM^3h^{1/2}.
\]

沿h=2⁻ⁿ求和有限。第一BC说明这样的三连小增量只能在有限多个尺度出现。但有限右导数要求它在所有充分细的尺度出现，矛盾。对可数H,M取并，便在同一个概率1事件上排除全部t≥0的有限右导数，尤其排除普通有限导数。没有对不可数个固定时刻零集取并，而是把所有可能切点一次装进一个可数网格事件。

为什么用了三个增量？单个小增量的概率约√h，网格位置却约有1/h个，直接并界失败；三个独立约束留下\(h^{1/2}\)，足以对几何尺度求和。这才是证明的机制。

## 26.11 总路程无穷，却留下确定的平方尺度

<a id="brownian-dyadic-variation"></a>

把固定[a,b]等分成2ⁿ格，记\(Q_n=\sum_i(B_{t_i}-B_{t_{i-1}})^2\)。独立Gaussian增量给下列均值及方差；Chebyshev与BC给\(Q_n\to b-a\)几乎必然。

\[
EQ_n=b-a,\qquad\operatorname{Var}(Q_n)=2(b-a)^2\,2^{-n},\qquad Q_n\longrightarrow b-a.
\]

沿有限分割把曲线各段位移的绝对值相加，再对全部分割取上确界，便是总变差：它是任意精细的分段测量所能记录的总路程。如果连续路径总变差有限，则\(Q_n\le\max_i|\Delta B_i|\sum_i|\Delta B_i|\to0\)，因为一致连续使最大网格增量趋0，矛盾。对有理端点区间取可数交，任意非退化区间包含这样的子区间，故Brownian路径在每个非退化区间都有无穷总变差。

这里实际证明的是确定二进分割上的平方和极限。随机分割下的一般二次变差、括号过程和Itô积分仍由后续章节建立，不能把这一计算冒充全部随机积分理论。它已经说明：一阶长度控制失败，不表示二阶尺度也失去规律。

## 26.12 比平方根多出的那一点增长

<a id="brownian-lil-upper"></a>

固定时刻\(B_t/\sqrt t\)总是标准正态；可在越来越长时间里反复观察同一条路径，偶尔会找到比通常尺度更大的涨落。正确的修正不是一个新的幂，而是很慢的重对数。先证明无穷时间的标量重对数律，记\(b(t)=\sqrt{2t\log\log t}\)，\(t\ge e^e\)。

固定ε>0，选\(1<q<(1+\varepsilon)^2\)。在t∈[qⁿ⁻¹,qⁿ]上，若\(B_t>(1+\varepsilon)b(t)\)，则[0,qⁿ]的最大值超过(1+ε)b(qⁿ⁻¹)。反射与Gaussian尾界给这个事件概率至多\(2\exp(-c\log\log q^{n-1})\)，其中\(c=(1+\varepsilon)^2/q>1\)。它对n可求和，因为\(\log\log q^{n-1}=\log((n-1)\log q)\)。

BC再对−B使用一次，给最终\(|B_t|\le(1+\varepsilon)b(t)\)。对可数ε↓0取交，得到limsup≤1和liminf≥−1。上界必须在整段时间上用最大值证明；仅检查B(qⁿ)不能排除两个观察时刻之间的越界。

## 26.13 下界为什么需要彼此分开的新波动

<a id="brownian-lil-lower"></a>

现在取很大的整数q。不同区间[qⁿ⁻¹,qⁿ]上的增量\(D_n\)相互独立，方差\(q^n(1-1/q)\)。对\(0<c<\sqrt{1-1/q}\)，正态下尾估计\(P(Z>x)\ge c_0x^{-1}e^{-x^2/2}\)给

\[
\begin{gathered}
D_n=B_{q^n}-B_{q^{n-1}},\\
P(D_n>c\,b(q^n))\ge
C_q(\log n)^{-1/2}n^{-c^2/(1-1/q)}
\quad\text{for all sufficiently large }n.
\end{gathered}
\]

级数发散，第二BC给无穷多次大正增量。上一节上界又控制旧位置：\(|B(q^{n-1})|/b(q^n)\le(1+o(1))/\sqrt q\)。故\(\limsup B_t/b(t)\ge c-1/\sqrt q\)。对可数整数q→∞，每个q再取可数c↑√(1−1/q)，得到下界1；负方向用对称性。正态下尾估计本身只需在[x,x+1/x]上积分Gaussian密度，并非新的极限定理。

\[
\limsup_{t\to\infty}\frac{B_t}{\sqrt{2t\log\log t}}=1,\qquad
\liminf_{t\to\infty}\frac{B_t}{\sqrt{2t\log\log t}}=-1
\quad\text{almost surely}.
\]

上界用相邻尺度足够接近来填满时间，下界用相邻尺度相隔足够远来减弱旧位置。两个q的任务不同；把它们混成同一个随n变化的参数，会丢掉可求和与独立性的严格依据。

## 26.14 把很远的时间翻到起点附近

<a id="brownian-local-lil"></a>

时间反演提供简洁桥梁，但必须先验证它在0连续。先不用LIL：Gaussian尾界使\(\sum_nP(|B_n|>\varepsilon n)<\infty\)，反射使\(\sum_nP(\sup_{u\le1}|B_{n+u}-B_n|>\varepsilon n)<\infty\)。BC再对可数ε↓0给\(B_t/t\to0\)。令\(\widehat B_0=0\)，\(\widehat B_t=tB_{1/t}\)。它在0连续，其他时刻也连续；有限维是中心Gaussian，\(\operatorname{Cov}(\widehat B_s,\widehat B_t)=\min(s,t)\)。由第23章连续路径的测度唯一性，B̂仍是标准Brownian。把无穷时间LIL用于B̂，便得到

\[
\limsup_{h\downarrow0}
\frac{B_h}{\sqrt{2h\log\log(1/h)}}=1,\qquad
\liminf_{h\downarrow0}
\frac{B_h}{\sqrt{2h\log\log(1/h)}}=-1
\quad\text{almost surely}.
\]

这是固定起点0附近的LIL。对每个指定的确定r，\(B_{r+h}-B_r\)仍是Brownian，所以同样成立；强Markov又允许对每个指定的、几乎必然有限的停止时刻应用它。但不能把“每个指定时刻”的零集随意并到全部随机时刻上。取可数有理r已足以说明：任何非退化区间都不可能满足1/2-Hölder界，因为局部重对数因子无界。

## 26.15 在所有位置寻找最大的短段

<a id="brownian-uniform-modulus"></a>

固定起点与在整段路径中寻找最剧烈的位置，是两种不同观察。给定T>0，定义\(w(B,\delta)=\sup_{\substack{s,t\in[0,T]\\|t-s|\le\delta}}|B_t-B_s|\)。现在约有1/δ个候选位置，最大涨落比固定起点更大。精确结论为

\[
\lim_{\delta\downarrow0}
\frac{w(B,\delta)}{\sqrt{2\delta\log(1/\delta)}}=1
\quad\text{almost surely}.
\]

证明不能只在粗网格上并界，任意时刻可能藏在缝里。[T-LIL第2节](../foundations/t-lil.md#t-lil-uniform-modulus)实际采用δ/m细网格，以Gaussian尾界控制距离约δ的网格点对，以反射控制两端移回网格的误差。m先固定足够大，再沿几何δ求和。下界来自约T/δ个独立短增量的正态下尾，再用相邻尺度补全所有δ。

这里的log(1/δ)与固定起点的log log(1/δ)并不矛盾。前者允许在每个尺度重新挑选最有利的位置，后者坚持同一起点。允许怎样选择观察位置，与单个增量分布同样重要。

## 26.16 重对数律能否记录整条形状

<a id="brownian-functional-lil"></a>

标量LIL只看\(B_T\)，仍可能漏掉达到末点之前的运动。把[0,T]压回[0,1]，用同一重对数尺度得到连续函数\(Y_T\)。我们不问它们收敛到一条曲线，正负端点已经表明不可能；要找的是所有可能反复逼近的形状。

\[
\begin{gathered}
Y_T(u)=\frac{B_{Tu}}{\sqrt{2T\log\log T}},\quad0\le u\le1,\quad T\ge e^e,\\
K=\left\{g:g(t)=\int_0^t v(u)\,du,\quad
v\in L^2([0,1]),\quad\int_0^1|v(u)|^2\,du\le1\right\}.
\end{gathered}
\]

Brownian函数型LIL断言：几乎必然，\(\{Y_T:T\ge e^e\}\)在一致范数下相对紧，且T→∞的聚点集恰为K。既要证明每个聚点属于K，也要证明K的每个形状真的出现。评价g(1)把K送到[−1,1]，端点由±u实现，因此它包括标量律，却有更强的路径内容。

Strassen的1964年论文《An Invariance Principle for the Law of the Iterated Logarithm》发表于Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete第3卷211–226页，作者本人出版目录可以核对。本章给出Brownian实值版本的现代独立重建，不把原论文的一般独立和不变性原理一并宣称为已经证明。

## 26.17 为什么限制形状的是平方能量

<a id="brownian-lil-energy"></a>

在有限分区上强迫Brownian增量接近指定Δg，Gaussian密度相乘，产生\(\sum(\Delta g)^2/\Delta u\)。分区越来越细，留下的不是长度，而是把曲线写成\(g(t)=\int_0^t v(u)\,du\)之后的平方积分\(\int_0^1|v(u)|^2\,du\)。能量直接来自独立增量的密度指数。若所有分区能量有界，用阶梯函数上的有界线性泛函及L²完备性，便证明这样的L²速度v确实存在，而且唯一。积分的绝对连续性又给g绝对连续；有界分区能量不容许额外的奇异变化。这样可以直接从增量建立能量，不先假定关于点态导数的微分定理。

完整证明在[T-LIL第1、3–7节](../foundations/t-lil.md#t-lil-energy)。上界在\(T_n=q^n\)用网格增量的χ²指数矩及反射残差，使偏离K的概率可求和，再用K在\(g(a\,\cdot)/\sqrt a\)下的稳定性填满所有实数T。下界选能量<1的有理折线，在不交叠大时间块中要求Brownian落入它的小管。Gaussian增量盒给约\(n^{-I(g)}\)的概率，桥误差由连续性控制；指数小于1使第二BC适用。旧时间段不能丢掉，而由上界控制到\(O(q^{-1/2})\)后再令q增大。

这不提前调用第29章Schilder，也不依赖尚未建立的路径变换公式。K中的曲线比Brownian原路径光滑并不矛盾：它们是扩大窗口、额外压缩涨落后留下的宏观聚点，不是原曲线在微观尺度获得了导数。

## 26.18 对称运动会把一半时间留在正半轴吗

<a id="brownian-arcsine"></a>

每个确定s>0都有P(\(B_s\)>0)=1/2，所以正半轴占有时间\(A_T\)的均值为T/2。若误读成独立投币频率，就会猜\(A_T/T\)在T很大时接近1/2。可是相邻时刻共享连续历史，一次长正游程会同时占据许多相邻观察。

\[
A_T=\int_0^T\mathbf1_{\{B_s>0\}}\,ds,\qquad
G_T=\max\{s\le T:B_s=0\},\qquad
\rho_T=\min\{s\le T:B_s=M_T\}.
\]

另外两份时间记录最后返回和首次达到全局最大值。对固定确定T，三个比例竟有相同的分布：

\[
\begin{gathered}
P(U\le x)=\frac2\pi\arcsin\sqrt x,\quad
f_U(x)=\frac1{\pi\sqrt{x(1-x)}}\quad(0<x<1),\\
\frac{A_T}{T}\overset d=\frac{G_T}{T}\overset d=\frac{\rho_T}{T}.
\end{gathered}
\]

密度在两端变大，但0和1没有原子。这不是三份时间在每条路径上相等，也不表示彼此独立。每条律都要有自己的路径论证，只证明一个再给另两个贴同样名字，不能建立三条定理。

## 26.19 两份半正态量的比较

<a id="brownian-arcsine-times"></a>

在确定s处分割。条件于\(B_s\)=x≠0，未来直到T不碰0的概率由反射给2Φ(|x|/√(T−s))−1。于是\(G_T\)≤s的概率化成两份独立标准正态绝对值的比较：

\[
P(G_T\le s)=P\!\left(\sqrt{T-s}|Z_2|\le\sqrt{s}|Z_1|\right)
=\frac2\pi\arctan\sqrt{\frac{s}{T-s}}
=\frac2\pi\arcsin\sqrt{\frac{s}{T}}.
\]

二维Gaussian角度均匀，所以概率就是四个对称扇形的角宽。对最大值位置，过去回落\(D_s=M_s-B_s\)由时间反向和对称性，仍服从\(\sqrt s\,|Z_1|\)；未来最大增量独立，服从\(\sqrt{T-s}\,|Z_2|\)。\(\rho_T\)≤s恰要求后者不超过前者，因而出现相同角度。

还须排除两个最大点。[T-ARCSINE第3节](../foundations/t-arcsine.md#t-arcsine-argmax)在两个假想最大点间插入有理r；未来最大值有连续分布、独立于过去，恰好打平过去最大值的概率为0。可数r给固定T上的唯一性。专题也明确处理\(G_T\)的可测性及非停止性。这里从未在最后零点或最大点使用强Markov性。

## 26.20 占有时间需要数完整游程

<a id="brownian-arcsine-occupation"></a>

占有时间不能只比较两个端点。令R从0出发，每步以相同概率独立取±1。这里把边的开区间内部位于正半轴的整条边计为正边：0到1与1到0都计一次，0到−1与−1到0都不计。由于单位步不会穿越零点而不以零点为端点，这等价于边中点为正。令\(H_{2m}\)计数前2m条正边，\(L_{2m}\)为按时间1/(2m)、空间1/√(2m)缩放的线性插值；于是正占有时间与正边比例精确相等，零端点不贡献时间长度。在零点切开，每个完整离零游程直到返回保持同号，最后还有一段未完成游程。独立返回分解和符号对称给确切公式

\[
\begin{gathered}
H_{2m}=\sum_{i=1}^{2m}\mathbf1_{\{R_{i-1}+R_i>0\}},\qquad
L_{2m}\!\left(\frac{i}{2m}\right)=\frac{R_i}{\sqrt{2m}},\\
\int_0^1\mathbf1_{\{L_{2m}(t)>0\}}\,dt=\frac{H_{2m}}{2m},\\
P(H_{2m}=2k)=u_{2k}u_{2m-2k},\qquad
u_{2j}=\frac{\binom{2j}{j}}{4^j},\quad0\le k\le m.
\end{gathered}
\]

为什么是乘积而不是二项概率？返回母函数\(U(z)=(1-z)^{-1/2}\)，首次返回母函数\(F=1-1/U\)；未完成段的尾和母函数也恰是U。双变量母函数中，z记录总步数的一半m，w记录正边数的一半k；正游程2j条边贡献\((zw)^j\)，负游程只贡献\(z^j\)。\(H_{2m}\)为偶数，是因为完整游程及偶数长度末段的边数均为偶数。按此约定给正游程加权，全部完整游程加末段的母函数化为U(zw)U(z)，比较系数便得上式。[T-ARCSINE第4节](../foundations/t-arcsine.md#t-arcsine-excursions)逐项给出分解，包括长度0末段。

第13章跨度2的局部CLT给\(u_{2j}\sim(\pi j)^{-1/2}\)，内部求和成为弧正弦密度的Riemann和。端点附近质量以C√ε控制，不能忽略。折线正占有比例恰是\(H_{2m}/(2m)\)，Donsker把折线送到Brownian。占有泛函在零集长度0的连续路径处连续，Tonelli又给Brownian零集几乎必然长度0，故连续映射定理将格点公式真正转成Brownian弧正弦律。

## 26.21 均值平衡与一条路径的时间分配

<a id="brownian-arcsine-meaning"></a>

\[
EU=\frac12,\qquad\operatorname{Var}(U)=\frac18,\qquad
P\!\left(U\notin[1/4,3/4]\right)=\frac23.
\]

这些值由x=sin²θ积分得到。更重要的是\(A_T/T\)的分布不随T改变，所以不依概率趋于1/2。不是大数定律失效，而是独立重复样本条件从未适用于这些符号观察。一次长游程能把时间分配推向一端；正负对称只在许多路径之间保证均值平衡。

Lévy原文《Sur certains processus stochastiques homogènes》可在Numdam原刊数字档案查到，档案标为Compositio Mathematica 7（1940），283–339页。这里仅把它作为相关Brownian路径研究的原始文献入口；本章网格、游程母函数与现代路径空间论证是我们的重建，不把当前写法或全部中间结论归到某位作者当年的表述上。

## 26.22 粗糙不是失去结构

<a id="brownian-rough-conclusion"></a>

最初那条放大以后总有新棱角的曲线，现在有了更精确的面貌。它没有任何有限切线，任何区间的总路程都无限；然而短段最大振幅有确定尺度，极端涨落有重对数边界，长期压缩后的形状受平方能量限制。连续性没有把运动变成平滑运动，概率也没有把粗糙性变成无法讨论的混乱。

首次命中允许重新开始，最后返回却需要未来信息；每个时刻正负机会相同，也不意味着一条路径把时间平分。这些区别不能从一份Gaussian边缘分布读出。路径空间、可测事件、停止信息与整段振幅估计，才让我们看清那份分布怎样在时间中展开。

Brownian运动还有一个鲜明限制：它没有跳跃。稀有事件曾产生Poisson规律，重尾求和又产生新的稳定极限。如果增量继续独立、平稳，却允许路径突然改变位置，连续小波动与罕见大跳怎样共存在同一份过程里？不能只给Brownian曲线添几条竖线；我们必须理解一份运动怎样被分成彼此独立的部分。

**证明与原始文献。** [T-LIL](../foundations/t-lil.md)；[T-ARCSINE](../foundations/t-arcsine.md)；[Strassen本人出版目录](https://www.math.uni-konstanz.de/~strassen/publ.html)与[1964年论文DOI](https://doi.org/10.1007/BF00534910)；[Lévy原刊数字档案](https://numdam.org/item/CM_1940__7__283_0/)。
