# T-LIL：一致振幅与 Brownian 函数型重对数律

这里给出[第26章](../chapters/26-brownian-properties.md#brownian-functional-lil)使用的完整技术证明。B是已经构造出的实标准Brownian motion。只使用Gaussian有限维结构、反射最大界、Borel–Cantelli、L²完备性和C空间紧性；不调用Schilder、一般大偏差、Cameron–Martin或强逼近。归一化只取T≥eᵉ，避免log log T在下端退化。

## 1. 能量球为何是一个紧的路径集合

<a id="t-lil-energy"></a>

\[
\begin{gathered}
I(g)=\int_0^1|v_g(s)|^2\,ds\quad
 \left(g(t)=\int_0^t v_g(s)\,ds,\ v_g\in L^2([0,1])\right),\\
I(g)=\infty\quad\text{if no such }v_g\text{ exists},\qquad
K=\{g\in C([0,1]):I(g)\le1\}.
\end{gathered}
\]

先核对这个定义没有歧义。若v、w给同一积分路径，则∫(v−w)u=0对全部阶梯u成立；阶梯在L²中稠密，故v=w几乎处处。这个积分表示还使g绝对连续：在总长度足够小的有限个不交叠区间上，增量绝对值之和不超过这些区间中|v|的积分，再用T-INTEGRAL的积分绝对连续性即可。证明只用积分速度，不预先调用关于点态导数的Lebesgue微分定理。

对有限分区π，记Eπ(g)=\(\sum(\Delta g)^2/\Delta t\)。若g有上述L²积分表示，Cauchy–Schwarz逐格给Eπ(g)≤I(g)。反方向也必须证明：设g连续、g(0)=0，全部分区能量≤C。对阶梯函数u=Σcᵢ1_(tᵢ₋₁,tᵢ]定义ℓ(u)=Σcᵢ(g(tᵢ)−g(tᵢ₋₁))。共同细化表明定义不依赖表示；加权Cauchy–Schwarz给|ℓ(u)|≤√C‖u‖₂。

阶梯在L²中稠密，故ℓ唯一连续延拓。用第23章从可数稠密阶梯建立的正交基eⱼ，令aⱼ=ℓ(eⱼ)。测试Σⱼ≤ₙaⱼeⱼ得到Σⱼ≤ₙaⱼ²≤C；T-LP的完备性给v=Σaⱼeⱼ∈L²，且ℓ(u)=∫uv。取u=1_(0,t]便得g(t)=∫₀ᵗv，因此g具有定义所需的积分表示，且I(g)≤C。这实际证明了有界分区能量不能隐藏一个奇异连续部分。

因而K恰由g(0)=0与所有Eπ(g)≤1刻画，是C中的闭集。其元素满足|g(t)−g(s)|≤√|t−s|、‖g‖∞≤1；Arzelà–Ascoli给紧性。若Pₘg为等距m格折线，则I(Pₘg)≤I(g)，且一致误差≤2/√m。先乘以1−η，再把有限节点值逼近为有理数，能量仍可保持严格小于1。这给K中一个可数稠密的有理折线族𝒟，且每个成员能量<1。

## 2. 一致模连续性的精确尺度

<a id="t-lil-uniform-modulus"></a>

固定0<T<∞，记w(B,δ)=sup_{s,t∈[0,T],|t−s|≤δ}|\(B_t\)−\(B_s\)|。第26章已证反射界P(sup_{u≤h}|B_u|>x)≤4exp(−x²/(2h))。另外，标准正态Z在x≥1时满足P(Z>x)≥c x⁻¹e⁻ˣ²ᐟ²：只在[x,x+1/x]积分密度，就得到一个绝对正常数c。

取几何尺度δₙ=q⁻ⁿ，q>1固定，并设细网格a=δ/m，m随后固定。任意距离≤δ的两点，其左网格点距离≤δ+2a。相关网格点对至多C_Tm²/δ个。对阈值(1+ε)√(2δlog(1/δ))，Gaussian尾界与并集界使网格点对超限概率至多下式第一项。把每个原时刻移回左网格点，另需两份短段残差。每份容许ε√(2δlog(1/δ))/2，反射并界给第二项。

\[
\begin{gathered}
P\!\left(w(B,\delta)>(1+2\varepsilon)\sqrt{2\delta\log(1/\delta)}\right)\\
\le C_{T,m}\delta^{(1+\varepsilon)^2/(1+2/m)-1}
   +C_{T,m}\delta^{m\varepsilon^2/4-1}.
\end{gathered}
\]

先取m足够大，使两个幂都正，再沿δₙ求和，用第一BC得到最终上界。对任意δₙ₊₁<δ≤δₙ，w单调，而归一化尺度在小δ时递增；所以全部δ的上极限至多(1+2ε)√q。最后只对可数q↓1、ε↓0取交，得到上界1。

下界取⌊T/δ⌋个不交叠δ长增量。它们除以√δ后独立标准正态。若所有绝对值均不超过(1−ε)√(2log(1/δ))，概率至多exp(−⌊T/δ⌋\(p_\delta\))，其中\(p_\delta\)≥c[log(1/δ)]⁻¹ᐟ²δ^{(1−ε)²}。乘积中的指数随δ→0以正幂爆长，故这些失败概率在几何尺度可求和。BC给最终下界；再用相邻几何尺度与q↓1，得到完整极限，而不只是某条子列。

\[
\lim_{\delta\downarrow0}
\frac{w(B,\delta)}{\sqrt{2\delta\log(1/\delta)}}=1
\quad\text{almost surely, for each fixed }T>0.
\]

对正有理T取可数交，还使这项路径性质在每个有限窗口同时成立；任意正T的下界可从更小有理窗口取到，上界从更大有理窗口取到。这里的log(1/δ)来自在窗口内搜索约1/δ个位置；它不同于固定起点LIL中的log log(1/δ)。

## 3. 几何时刻上的路径能量上界

<a id="t-lil-upper"></a>

\[
\begin{gathered}
Y_T(t)=\frac{B(Tt)}{\sqrt{2T\log\log T}},\quad 0\le t\le1,\ T\ge e^e,\\
T_n=q^n,\quad L_n=\log\log T_n=\log(n\log q).
\end{gathered}
\]

固定ε>0，先选δ>0使√(1+δ)−1<ε/2。令Pₘ为m格折线。若I(PₘY)≤1+δ且‖Y−PₘY‖∞≤ε/2，则把PₘY除以√(1+δ)送入K，得到dist(Y,K)≤ε。因为高能量折线在缩小后的一致改变量至多√(1+δ)−1，这一步把能量控制变成了路径距离控制。

Brownian缩放给\(Y_{T_n}\)与W/√(2Lₙ)同分布，其中W为[0,1]上标准Brownian。m个标准化网格增量独立N(0,1)，所以I(PₘW)为\(\chi_m^2\)。其矩母函数由一维Gaussian积分直接给E exp(θ\(\chi_m^2\)/2)=(1−θ)⁻ᵐᐟ²。取1/(1+δ)<θ<1，Markov给能量超限概率的可求和指数。

\[
P\!\left(I(P_mY_{T_n})>1+\delta\right)
\le (1-\theta)^{-m/2}e^{-\theta(1+\delta)L_n}.
\]

折线误差不超过各格相对左端的最大波动的两倍。反射并界因而给下式。再把m取到mε²/16>1，两项都形如C exp(−cLₙ)，c>1；因Lₙ=log(nlog q)，对n可求和。第一BC及可数精度交得到dist(\(Y_{T_n}\),K)→0几乎必然。参数δ、θ、m都在取n极限前固定，不能随n任意改变。

\[
P\!\left(\|Y_{T_n}-P_mY_{T_n}\|_\infty>\varepsilon/2\right)
\le4m\exp\{-m\varepsilon^2L_n/16\}.
\]

## 4. 为什么不能只停在几何时刻

<a id="t-lil-all-times"></a>

取T∈[\(T_{n-1}\),Tₙ]，a=T/Tₙ∈[1/q,1]。下面是同一路径的精确恒等式。关键不是把两条路径粗略相减，而是观察K在限制与平方根缩放下保持不变。

\[
\begin{gathered}
Y_T(t)=\kappa_n(T)\frac{Y_{T_n}(at)}{\sqrt a},
\qquad \kappa_n(T)=\sqrt{\frac{L_n}{\log\log T}}\longrightarrow1
\quad\text{uniformly for }T\in[T_{n-1},T_n],\\
g\in K\quad\Longrightarrow\quad
I\!\left(\frac{g(a\,\cdot)}{\sqrt a}\right)
=\int_0^a|v_g(u)|^2\,du\le1.
\end{gathered}
\]

这里的速度变换可直接验证：g(at)/√a的积分速度是√a v_g(at)，仿射换元即给上式；不需要先证明g的点态可微性。

选gₙ∈K逼近\(Y_{T_n}\)，则新路径到K的距离至多κₙ√q‖\(Y_{T_n}\)−gₙ‖∞+|κₙ−1|，一致趋0。故dist(\(Y_T\),K)→0对全部T→∞成立。K紧，给出渐近相对紧性；有限区间T∈[eᵉ,M]上的路径族也紧，因为T↦\(Y_T\)在一致范数下连续。这证明整个所述路径族相对紧，且每个T→∞聚点在K中。

## 5. 一个折线形状出现的概率

<a id="t-lil-tube"></a>

需要一个直接的Gaussian小管下界。固定从0出发的折线h，分区包含其全部拐点。设cₙ=√((1−a)/(2Lₙ))，0<a<1固定。在每个分区格上，要求W的增量落在Δh/cₙ左右宽度1的盒子内。Gaussian密度在这个盒子上的下界相乘，给出指数主项I(h)/(2cₙ²)，以及至多C/cₙ+C的误差。

\[
P(\text{all increment boxes})
\ge C_0\exp\!\left\{-\frac{L_n I(h)}{1-a}-C_1\sqrt{L_n}-C_2\right\}.
\]

还不能只检查端点。每格减去端点间的直线后得到连续Gaussian桥；它与全部网格增量协方差为0，故独立。有限个桥在稠密坐标上的Gaussian独立性，经C空间坐标Borel结构扩张为路径独立性。桥范数几乎必然有限，所以乘以cₙ后全部桥误差<ε/2的概率趋1；它与增量盒事件独立。盒子内端点误差至多mcₙ，最终<ε/2。因此

\[
P(\|c_nW-h\|_\infty<\varepsilon)
\ge C\exp\!\left\{-\frac{L_n I(h)}{1-a}-C'\sqrt{L_n}\right\}
\quad\text{for all sufficiently large }n.
\]

这只是针对一条有限折线及一条固定管子的实际密度估计，不是未经证明的一般路径大偏差原理。只要I(h)/(1−a)<p<1，右边最终可下界为常数乘\(n^{-p}\)；√Lₙ误差由p与主指数的严格间距吸收。

## 6. 独立时间块怎样找回整个能量球

<a id="t-lil-lower"></a>

取第1节可数族中的g，I(g)<1；令q为整数，a=1/q。在[\(T_{n-1}\),Tₙ]上的增量经标准化给相互独立的[0,1] Brownian路径Wₙ。独立性只使用确定性不交叠区间，不调用停止时刻定理。把原路径在[0,a]置零，之后只保留此块从0开始的运动，得到Zₙ。

\[
\begin{gathered}
Z_n(t)=0\quad(t\le a),\qquad
Z_n(t)=c_nW_n\!\left(\frac{t-a}{1-a}\right)\quad(t\ge a),\\
h_a(u)=g(a+(1-a)u)-g(a),\qquad
\frac{I(h_a)}{1-a}=\int_a^1|v_g(s)|^2\,ds\le I(g)<1.
\end{gathered}
\]

第5节小管下界使事件‖cₙWₙ−\(h_a\)‖∞<ε的概率和发散。这些事件相互独立，所以第二BC给无穷多次发生。此时Zₙ与g在后段只差g(a)及ε，在前段差至多√a，故‖Zₙ−g‖∞≤√a+ε。

被删去的旧路径不能直接丢掉。第4节上界与‖K‖∞≤1给sup_{u≤\(T_{n-1}\)}|B_u|≤(1+o(1))√(2\(T_{n-1}\)log log \(T_{n-1}\))。除以当前归一化，至多(1+o(1))√a；它同时控制前段旧运动与后段原起点。故无穷多次有‖\(Y_{T_n}\)−g‖∞≤2√a+ε+o(1)。

只对g∈𝒟、整数q≥2和有理ε>0取可数交。给任意所需精度，再选择q足够大、ε足够小，并从无穷多个合适n中递增选择，就说明每个g∈𝒟都是聚点。相对紧族的聚点集是闭的：对聚点gⱼ→g，依次选Tⱼ>j且‖\(Y_{T_j}\)−gⱼ‖<1/j即可。因此聚点集包含闭包K，结合上界便恰等于K。没有对不可数个目标直接并零集。

## 7. 实际结论与标量LIL的分工

<a id="t-lil-statement"></a>

\[
\text{Almost surely, }\{Y_T:T\ge e^e\}
\text{ is relatively compact in }C([0,1]),
\quad\operatorname{Cluster}_{T\to\infty}Y_T=K.
\]

评价g↦g(1)将K送到[−1,1]，端点由g(t)=±t实现；所以这个结论包含标量LIL。主章先用更短的最大估计和独立块证明标量版，以展示log log尺度；本专题则说明不仅端点，而且整条归一化形状受能量约束。这是Brownian的实值、无穷时间函数型LIL，不冒充一般独立和强不变原理、多元版本或近零函数型定理。

K由绝对连续曲线组成，并不说明Brownian原路径变得可微。这里观察的是越来越大时间窗口中、经过额外重对数压缩后留下的聚点。原路径在每个固定窗口中的处处不可微，与这些宏观形状可以光滑，回答的是不同问题。
