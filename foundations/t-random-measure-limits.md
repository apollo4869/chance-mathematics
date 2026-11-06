# T-RANDOM-MEASURE-LIMITS：随机质量的识别与收敛

返回[第49章](../chapters/49-random-measures.md#mass-law-limits)。使用[T-RADON-SPACE](t-radon-space.md)的LCSC空间、紧穷竭、可数测试与Polish结论。以下“分布收敛”指随机元外层概率律的弱收敛；须另说明内层测度采用vague还是有限测度weak拓扑。

## 1. Laplace泛函与联合读数唯一性

<a id="mass-transform-unique"></a>

设Ξ、η是随机非负Radon测度，\(\mathbb E e^{-\Xi f}=\mathbb E e^{-\eta f}\)对所有\(f\in C_c^+\)成立。对有限族f₁,…,fᵣ及非负a，使用\(f=\sum a_jf_j\)，得到向量Y、Z全部联合Laplace变换相同。它们有限a.s.，因为每个测试紧支撑。令\(V_j=e^{-Y_j}\)、\(W_j=e^{-Z_j}\)，取非负整数a得到[0,1]ʳ上全部混合矩相同。

第13章的Bernstein逼近在各坐标逐次应用，一致逼近紧立方体上任意连续函数：可直接把多元多项式写为独立二项随机向量的函数期望，由一致连续性和各坐标方差界控制误差。故V、W等律；指数逆映射可测给Y、Z等律。可数测试的全部有限维分布相同，经柱集π–λ给相同序列律，再由评价域生成性给Ξ、η等律。这里没有以矩唯一性替代Laplace唯一性，也未假设Ξ的矩有限。

## 2. 随机局部质量紧性的充要条件

<a id="mass-random-tightness"></a>

对一族\(\Xi_\alpha\)，其在\(\mathcal M_+\)上的概率律紧，当且仅当每个紧K的\(\Xi_\alpha(K)\)一致紧。必要性：对任意ε选概率≥1−ε的测度紧集C，连续读数μχ在C有上界，且χ≥1于K。于是窗口质量的尾概率至多ε。

充分性：对每个m选aₘ使\(\sup_\alpha\mathbb P\{\Xi_\alpha(K_m)>a_m\}<\varepsilon2^{-m}\)。集合\(D=\{\mu:\mu(K_m)\le a_m,\ \forall m\}\)在T-RADON-SPACE下相对紧，闭包C紧。并集界给\(\inf_\alpha\mathbb P\{\Xi_\alpha\in C\}\ge1-\varepsilon\)。D是Borel，故概率合法；不要求D自己闭，也不要求各窗口界来自有限平均。Markov均值界只是一个额外可用的充分方法。

## 3. Laplace收敛怎样推出随机测度收敛

<a id="mass-law-convergence"></a>

定理：若Ξₙ、Ξ均已是随机Radon测度，则\(\Xi_n\Rightarrow\Xi\)在vague空间中成立，当且仅当对所有\(C_c^+\)测试有\(L_n(f)\to L(f)\)。必要性来自\(\mu\mapsto e^{-\mu f}\)有界连续。充分性取χ≥1于K，a>0，R>0，在\(\{\Xi_nK>R\}\)上有\(1-e^{-a\Xi_n\chi}\ge1-e^{-aR}\)，得到正文尾界。

给ε，因Ξχ有限a.s.，支配收敛允许先选a使1−L(aχ)<ε/4；再取N使n≥N的分子小于ε/2；再取R使分母≥1/2，必要时先把ε常数缩小。最后加大R控制有限个n<N。于是上一节给紧性，第24章的Polish Prokhorov给每个子列的弱收敛子子列。连续读数识别其Laplace泛函为L，第一节给唯一性，故全序列收敛。每一步使用的是外层概率弱收敛，不是逐路径收敛。

若B相对紧且\(\mu(\partial B)=0\)，连续内外逼近给\(\mu_n(B)\to\mu(B)\)于确定性vague收敛。用Radon正则性先把边界邻域质量压小，再选连续夹逼，故只需局部有限而不需总量有限。随机版在\(\mathbb P\{\Xi(\partial B)=0\}=1\)时由连续映射定理成立。可选一族可数基球，其半径同时避开随机边界：固定大窗口及l，对\(\{\Xi K\le l\}\)上的球面质量取期望，不交球面的期望和≤l，故只有可数半径有正概率正质量；再对窗口、l取可数并。

## 4. 有限质量的weak与vague

<a id="mass-finite-weak"></a>

设μₙ、μ为有限非负Radon测度。全部\(C_b\)测试收敛，显然推出vague与总量收敛。反向取\(0\le\chi\le1\)紧支撑，\(\mu(1-\chi)<\varepsilon\)。若总量也收敛，则\(\mu_n(1-\chi)=\mu_nE-\mu_n\chi\to\mu E-\mu\chi\)。任意\(f\in C_b\)满足

\[ |\mu_nf-\mu f|\le|\mu_n(\chi f)-\mu(\chi f)|+\|f\|_\infty\{\mu_n(1-\chi)+\mu(1-\chi)\}. \]

先取n极限再ε↓0即得结论。特别地，\(\mathcal P(E)\)上的weak与vague子空间拓扑相同。前者不允许概率丢失，后者在更大的\(\mathcal M_+\)中允许；如δₙ在实线vague趋0，而0不在\(\mathcal P(E)\)。在固定紧E上所有有限测度的两种拓扑相同，因为1也紧支撑。

若\(P_n\Rightarrow P\)是外层vague分布收敛，且Pₙ和P均a.s.在\(\mathcal P(E)\)，则也是外层weak概率空间收敛。可用第24章Skorokhod在Polish\(\mathcal M_+\)上的共同表示：表示副本vague a.s.收敛，在共同满概率集上总量均1，上一确定性结论给weak a.s.收敛，再回到分布。这样不把子空间拓扑与“极限仍在子空间”混同。

## 5. 随机归一化与截断尾部

<a id="mass-random-normalize"></a>

设Ξₙ、Ξ有限，总质量均正a.s.，且\((\Xi_n,\Xi_nE)\Rightarrow(\Xi,\Xi E)\)在\(\mathcal M_+\times\mathbb R_+\)中成立。Skorokhod表示及上节确定性论证先给有限测度weak a.s.收敛。分母趋正数，再除即得归一化概率weak a.s.收敛，因而原外层律收敛。若Ξ可能零，归一化在该点没有连续延拓；若总质量无穷，连分母也不是合法归一化。

一个可用的无逃逸充分条件是，对任意ε>0，有紧支撑\(0\le\chi\le1\)使\(\sup_n\mathbb P\{\Xi_n(1-\chi)>\varepsilon\}<\varepsilon\)，且Ξ有限。结合vague分布收敛，尾部截断使\((\Xi_n,\Xi_nE)\Rightarrow(\Xi,\Xi E)\)：先对固定χ使用连续坐标，再以概率尾界令χ穷竭；Ξ自己的尾部由有限性趋0。第24章的逼近引理或有界Lipschitz测试的三角界给联合结论。若只有均值总量有界而没有尾部位置控制，δₙ仍是反例。
