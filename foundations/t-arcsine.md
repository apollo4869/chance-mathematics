# T-ARCSINE：三种路径时间的弧正弦分布

本专题完成[第26章](../chapters/26-brownian-properties.md#brownian-arcsine)所用的三条弧正弦律。T>0始终是固定的确定时刻。只使用本章已经证明的反射、确定时刻的独立增量、第25章Donsker，以及简单随机游走的首次返回分解；不调用局部时、Itô公式或最后离开时刻的强Markov性。

## 1. 先确定三个可测的时间

<a id="t-arcsine-functionals"></a>

\[
\begin{gathered}
A_T=\int_0^T\mathbf1_{\{B_s>0\}}\,ds,\qquad
G_T=\max\{s\le T:B_s=0\},\\
\rho_T=\min\{s\le T:B_s=M_T\},\qquad
M_T=\max_{0\le s\le T}B_s.
\end{gathered}
\]

对从0出发的连续路径，零集与最大点集非空紧，因此G和最早最大点ρ总有定义，不需要先假定最大点唯一。事件{G≥s}由[s,T]上|路径|的下确界是否为0决定；事件{ρ≤s}由[0,s]与[0,T]上两个最大值是否相等决定。它们是闭的路径事件，给Borel可测性。占有时间的可测性由路径评价的联合连续性及非负积分得到。

Brownian零集的Lebesgue长度几乎必然为0：Tonelli给其期望等于∫₀ᵀP(\(B_s\)=0)ds=0，单点s=0不影响积分。于是若连续路径xₙ一致趋于x，且x的零集长度0，则1_{xₙ(s)>0}在几乎每个s趋于1_{x(s)>0}，DCT给占有时间连续。这正是最后把随机游走送到Brownian时需要的条件。

## 2. 最后一次为零：在确定时刻切开路径

<a id="t-arcsine-last-zero"></a>

固定0<s<T。在s时刻知道\(B_s\)=x以后，后段是从x出发的独立Brownian运动。若x≠0，它在T−s内不碰0的概率，由反射原理等于2Φ(|x|/√(T−s))−1。\(B_s\)=0的概率为0，所以边界不影响下式。注意我们在s切开，而不是在\(G_T\)切开。

\[
\begin{aligned}
P(G_T\le s)
&=E\!\left[2\Phi\!\left(\frac{|B_s|}{\sqrt{T-s}}\right)-1\right]\\
&=P\!\left(\sqrt{T-s}|Z_2|\le\sqrt{s}|Z_1|\right)
=\frac2\pi\arctan\sqrt{\frac{s}{T-s}}
=\frac2\pi\arcsin\sqrt{\frac{s}{T}},
\end{aligned}
\]

Z₁、Z₂是独立标准正态。最后一个概率可直接用二维Gaussian密度的极坐标计算：角度均匀，第一象限中允许的角宽是arctan√(s/(T−s))，再用四象限对称。s↓0与s↑T的极限分别为0与1，故没有端点原子。

这也揭示\(G_T\)不是停止时刻。对任意0<s<T，P(\(G_T\)≤s|\(\mathcal F_s\))=2Φ(|\(B_s\)|/√(T−s))−1几乎必然严格介于0与1。如果{\(G_T\)≤s}属于\(\mathcal F_s\)，这个条件概率必须是0或1，矛盾。要确认“最后一次”，必须知道尚未发生的后段。

## 3. 最大值何时出现

<a id="t-arcsine-argmax"></a>

先证明对这个固定T，最大点几乎必然唯一。若有两个不同最大点，可以在它们之间插入有理r∈(0,T)。于是过去最大值M_r恰好等于\(B_r\)加上未来区间上的最大增量。后者独立于\(\mathcal F_r\)，并有连续半正态分布，因此等于这个\(\mathcal F_r\)可测差额的概率为0。对可数有理r取并即可。这里没有宣称对所有随机T同时唯一。

在s以前取到全局最大值，当且仅当未来最大增量不超过\(D_s\)=M_s−\(B_s\)。倒过来看[0,s]上的增量，过程u↦\(B_s\)−B_{s−u}仍是Brownian运动：它连续、中心Gaussian，协方差为min(u,v)。再用对称性，\(D_s\)与M_s同分布，因此与√s|Z₁|同分布。未来最大增量与\(D_s\)独立，分布是√(T−s)|Z₂|。

\[
P(\rho_T\le s)
=P\!\left(\sqrt{T-s}|Z_2|\le\sqrt{s}|Z_1|\right)
=\frac2\pi\arcsin\sqrt{\frac{s}{T}}.
\]

同一角度计算再次出现，但原因不是\(\rho_T\)等于\(G_T\)，而是两个不同的路径问题都变成两份独立半正态量的比较。\(\rho_T\)也不能被拿来无条件使用强Markov性；上述证明始终只在确定的s处分割。

## 4. 先在格点上数正半轴的时间

<a id="t-arcsine-excursions"></a>

令R_k是从0出发的对称±1随机游走。对2m步定义H₂ₘ=Σᵢ₌₁²ᵐ1_{Rᵢ₋₁+Rᵢ>0}，即位于正半轴的边的条数。单位步不会从负整数直接跨到正整数；零端点的单点时间无长度。因此折线插值在正半轴的时间比例，恰等于H₂ₘ/(2m)。这个计数避免了把零点机械算成半次访问的歧义。

\[
\begin{gathered}
u_{2j}=P(R_{2j}=0)=\frac{\binom{2j}{j}}{4^j},\qquad
U(z)=\sum_{j\ge0}u_{2j}z^j=(1-z)^{-1/2},\\
\tau=\inf\{k\ge1:R_k=0\},\qquad
F(z)=\sum_{j\ge1}P(\tau=2j)z^j.
\end{gathered}
\]

二项式级数给U；也可从系数递推求解(1−z)U′=U/2、U(0)=1。按第一次返回分解路径，独立后段重新从0开始，于是U=1+FU。故F=1−√(1−z)。若q_j=P(τ>2j)，其尾和母函数Q(z)=Σq_jz^j=(1−F(z))/(1−z)=U(z)。这包括长度0的尚未完成段。

每条偶数长度路径唯一分解为若干完整离零游程，后接一段未完成的游程。每个游程在返回以前保持同号；条件于长度，正负号对称。用z记录半步数，用w记录正边数的一半。一个完整游程的双变量母函数是[F(zw)+F(z)]/2；末段是[Q(zw)+Q(z)]/2。长度0末段在两项中各占一半，合起来正好为1。把完整游程数求和便得到

\[
\begin{aligned}
\sum_{m,k\ge0}P(H_{2m}=2k)z^m w^k
&=\frac{Q(zw)+Q(z)}{2-F(zw)-F(z)}\\
&=\frac1{\sqrt{1-zw}\sqrt{1-z}}=U(zw)U(z),\\
P(H_{2m}=2k)&=u_{2k}u_{2m-2k},\qquad0\le k\le m.
\end{aligned}
\]

在0≤z,w<1上，几何级数与Tonelli使以上运算合法；相应非负幂级数的系数唯一。因此这是确切概率公式，不是只匹配若干矩的猜测。H₂ₘ确实为偶数，因为完整游程及偶数长末段都占偶数条边。

## 5. 端点附近的质量不能丢掉

<a id="t-arcsine-occupation"></a>

第13章跨度为2的局部CLT给u₂ⱼ∼1/√(πj)，并由渐近及有限初项得到u₂ⱼ≤C/√(j+1)。因此在εm≤k≤(1−ε)m上，上一节的精确概率是弧正弦密度的Riemann和。还必须控制靠近0和1的质量，不能把奇异端点从积分中悄悄删去。对0<ε≤1/2，

\[
\begin{gathered}
P(H_{2m}\le2\varepsilon m)
\le\frac C{\sqrt m}\sum_{k=0}^{\lfloor\varepsilon m\rfloor}
\frac1{\sqrt{k+1}}
\le C'\sqrt\varepsilon+\frac{C'}{\sqrt m},\\
\frac{H_{2m}}{2m}\ \Rightarrow\
\frac{\mathbf1_{(0,1)}(x)}{\pi\sqrt{x(1-x)}}\,dx.
\end{gathered}
\]

另一端相同。先固定ε做内部Riemann和，再令ε↓0，便得任意有界连续测试函数的收敛。由第25章Donsker，R的折线缩放在C([0,1])中趋于Brownian；第1节证明占有时间泛函在几乎所有Brownian路径处连续。因此连续映射定理把同一极限识别为A₁。Brownian时间缩放给\(A_T\)/T与A₁同分布。

## 6. 相同分布不是相同时间

<a id="t-arcsine-conclusion"></a>

\[
\begin{gathered}
\frac{A_T}{T}\ \overset d=\ \frac{G_T}{T}\ \overset d=\ \frac{\rho_T}{T},\qquad
P(U\le x)=\frac2\pi\arcsin\sqrt x,\quad0\le x\le1,\\
EU=\frac12,\qquad \operatorname{Var}(U)=\frac18,\qquad
P\!\left(U\notin[1/4,3/4]\right)=\frac23.
\end{gathered}
\]

矩由x=sin²θ直接积分得到。这三份时间各自描述占有、最后返回与最大值位置，不是在同一路径上相等，也没有被证明彼此独立。尤其\(A_T\)/T的分布不随T缩向1/2；它不依概率趋于1/2。Brownian的对称性保证均值平衡，却不把一条路径的正负占有变成独立投币频率。
