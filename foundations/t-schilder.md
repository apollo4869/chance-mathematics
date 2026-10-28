# T-SCHILDER：有限网格、平方能量与完整路径大偏差

固定T>0、整数d≥1，B为标准d维Brownian运动。路径空间为起点0的连续函数，距离是一致范数；它是可分完备度量空间，使用第23–24章的可测和紧性结构。Xε=√ε B，速度1/ε。以下直接构造证明，不使用Girsanov、Dawson–Gärtner、随机积分或尚未证明的RKHS表示。

## W.1 有限Gaussian向量的完整LDP

<a id="t-schilder-grid"></a>

将[0,T]等分为m格，Δ=T/m。令zⱼ为Xε的第j个增量。其Rᵈᵐ密度如下，二次型Qₘ正定。固定m时，ε乘密度前因子的对数趋0。

\[
p_\varepsilon(z)=(2\pi\varepsilon\Delta)^{-dm/2}e^{-Q_m(z)/\varepsilon},\qquad Q_m(z)=\frac1{2\Delta}\sum_{j=1}^m|z_j|^2.
\]

对开O和其中z，取闭小球包含于O；其体积为正常数，密度至少为前因子乘e的−球上最大Qₘ/ε次方。取下极限，再缩小球，得到−Qₘ(z)，对z优化。对紧K，取包含K的有限体积球，积分不超过该体积乘前因子及e的−inf_K Qₘ/ε次方，给紧上界。

任意闭集还需尾控制。高维Gaussian平方的指数矩由各一维Gaussian积分相乘算得下式，因此有指数紧。紧上界加尾控制给所有闭集上界，而非只在有界集上成立。Qₘ子水平紧，所以速率好。

\[
E\exp\left\{\frac{|z|^2}{4\Delta\varepsilon}\right\}=2^{dm/2},\qquad P(|z|>R)\le2^{dm/2}e^{-R^2/(4\Delta\varepsilon)}.
\]

把增量累加为网格值，再作线性插值，是连续且单射的有限维映射Γₘ。其像Vₘ是该网格折线空间；Πₘh=h刻画它，故像闭。正文已证明的收缩原理给ΠₘXε的完整LDP，速率在Vₘ上为Eₘ(h)，在Vₘ外为无穷。这里不把Eₘ对任意路径的读数误认为整个空间上的折线分布速率。

\[
E_m(h)=\frac12\sum_{j=1}^m\frac{|h(j\Delta)-h((j-1)\Delta)|^2}{\Delta}.
\]

## W.2 二进网格识别全部有限能量路径

<a id="t-schilder-energy"></a>

取层级k，mₖ=2ᵏ。令vₖ为Π₂ᵏh的速度。细化时每个粗单元的速度积分不变，故细速度与粗速度的L²内积恰是粗速度平方范数。得到下式以及网格能量单调性。

\[
\langle v_\ell,v_k\rangle_2=\|v_k\|_2^2,\quad\|v_\ell-v_k\|_2^2=\|v_\ell\|_2^2-\|v_k\|_2^2\quad(\ell\ge k),\qquad\|v_k\|_2^2=2E_{2^k}(h).
\]

若能量上确界有限，单调有界的平方范数收敛，故vₖ在L²中Cauchy。T-LP完备性给g。积分映射从L²到一致路径连续，下面的界使积分速度极限就是h，因为连续h的折线一致趋h。

\[
\sup_{t\le T}\left|\int_0^t(v_k-g)(s)\,ds\right|\le\sqrt T\|v_k-g\|_2\longrightarrow0,\qquad h(t)=\int_0^tg(s)\,ds.
\]

反向若h有L²积分速度g，vₖ是其单元平均，Jensen给平方范数有界。同一Cauchy论证给极限w，其从0到t的积分也等于h。对各坐标，(w−g)dt是有限带符号测度，所有区间质量0，T-MCLASS测度唯一性给w=g几乎处处。因此能量上确界恰等于g平方积分的一半。

\[
I_T(h):=\sup_{k\ge0}E_{2^k}(h)=\begin{cases}\tfrac12\int_0^T|g(s)|^2\,ds,&h(t)=\int_0^t g(s)\,ds,\ g\in L^2,\\\infty,&\text{otherwise}.\end{cases}
\]

这里以积分表示定义L²速度，其唯一性已由区间积分证明，不先对每条路径求导。积分关于Lebesgue测度的绝对连续性（T-INTEGRAL）保证这类h确为绝对连续：不交小区间的位移总和由其并集上|g|积分控制。一般连续而非绝对连续路径不能有此表示，能量必无穷。

I是连续网格能量的上确界，下半连续。I≤L给统一上界和平方根模连续界。Arzelà–Ascoli给相对紧，水平集闭使其紧。于是能量是好速率，而不靠尚未证明的Hilbert弱紧性或RKHS定理。

\[
\|h\|_\infty\le\sqrt{2LT},\qquad |h(t)-h(s)|\le\sqrt{2L|t-s|}\quad(I_T(h)\le L).
\]

## W.3 反射界给指数好逼近

<a id="t-schilder-approximation"></a>

单个格内，用路径到左端的增量减去其终点增量的线性比例，故到弦的差至多2倍该格增量上确界。若欧氏范数超过δ，则某坐标超过δ/平方根d。每个坐标Brownian最大绝对值在Δ时间超过u的概率，反射及Gaussian Chernoff给不超过4e的−u²/(2Δ)次方。联合m格、d坐标，并缩放√ε，得下式。

\[
P\{\|X^\varepsilon-\Pi_mX^\varepsilon\|_\infty>\delta\}\le4dm\exp\left\{-\frac{\delta^2m}{8dT\varepsilon}\right\},\qquad\lim_{k\to\infty}\limsup_{\varepsilon\downarrow0}\varepsilon\log P\{\|X^\varepsilon-\Pi_{2^k}X^\varepsilon\|_\infty>\delta\}=-\infty.
\]

每个固定网格的前因子在ε乘对数中消失，随后网格加密使代价无穷。此处未将不同网格的前因子在无穷并界中直接丢弃；下一节专门处理那一步。

## W.4 一个可核查的路径指数紧集

<a id="t-schilder-exponential-tightness"></a>

给L>0，令δⱼ=2⁻ʲ。选递增二进网格mⱼ，使下式成立；线性m项最终超过其对数，故能选到。再选M使M²/(2dT)−log(4d)≥L+2。

\[
\frac{\delta_j^2m_j}{8dT}-\log(4dm_j)\ge L+j+2,\qquad K_L=\{h:\|h\|_\infty\le M,\ \|h-\Pi_{m_j}h\|_\infty\le\delta_j\ \forall j\ge1\}.
\]

Kᴸ闭。给任意η>0，选δⱼ<η/3，所有Πₘⱼh的网格值被M界住，位于有限维紧折线集合中；取有限η/3网，再加上δⱼ误差，给Kᴸ有限η网。所以Kᴸ全有界，路径空间完备使它紧。

对0<ε≤1，把每项前因子的对数吸收到1/ε指数中，上一节给第j个逼近约束失败概率≤e的−(L+j+2)/ε次方。反射坐标界还给范数约束失败概率≤e的−(L+2)/ε次方。因此无穷和有以下统一界，确实给指数紧性。

\[
P(X^\varepsilon\notin K_L)\le e^{-(L+2)/\varepsilon}\left(1+\frac1{e^{1/\varepsilon}-1}\right),\qquad\limsup_{\varepsilon\downarrow0}\varepsilon\log P(X^\varepsilon\notin K_L)\le-(L+2).
\]

## W.5 完整路径上下界

<a id="t-schilder-full"></a>

对紧K，Xε在K意味着Π₂ᵏXε在Π₂ᵏK；后者紧，W.1给上指数不超过−inf_K E₂ᵏ。递增连续函数E₂ᵏ在紧K上满足下式。证明：若r<inf_K I，则闭集K∩{E₂ᵏ≤r}递减且交为空，紧性迫使某一级已空；取所有这样的r即可。

\[
\sup_k\inf_{h\in K}E_{2^k}(h)=\inf_{h\in K}\sup_kE_{2^k}(h)=\inf_K I_T.
\]

所以紧上界成立。对闭F，以W.4的Kᴸ分解，用有限和上指数规则，得不超过max{−inf_F I,−L−2}。L趋无穷给全闭上界。

对开G和其中有限能量h，取r>0使一致r球落在G。选足够大二进m，既使范数Πₘh−h小于r/3，也使bₘ=(r/3)²m/(8dT)>I(h)+1。折线在Πₘh的r/3球内，且自身逼近误差≤r/3时，原路径在G，故下式成立。

\[
P(X^\varepsilon\in G)\ge P(\|\Pi_mX^\varepsilon-\Pi_mh\|_\infty<r/3)-P(\|X^\varepsilon-\Pi_mX^\varepsilon\|_\infty>r/3).
\]

第一项有限维LDP下指数至少−Eₘ(h)≥−I(h)，第二项W.3上指数至多−bₘ，严格更小。T-LDP的相减引理使差保留至少−I(h)的下指数。再对h优化，得开下界。不存在有限能量点时下界为负无穷，无需另证。W.2好性已完成，所以这就是完整Schilder定理。

最终极限先ε趋0，m作为足够大的固定网格被选定。不存在对每个固定m误差自动超指数小的断言，也没有从有限维分布直接宣布全路径LDP。全结论范围是固定有限T、标准d维Brownian及一致路径拓扑。
