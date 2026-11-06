# 第三十九章：如何对随机性求导？——Malliavin calculus

一台仪器只报告Brownian运动在时刻1的位置平方。原始位置是Gaussian，输出却不是：同一个正读数可能来自正、负两个位置，而零附近的读数挤在一起。若换成一份依赖整条轨迹、甚至没有显式表达式的输出，怎样判断它的分布是否仍能用密度描述？我们想测量的不是曲线在下一秒的斜率，而是改变驱动噪声以后，输出怎样回应。

## 39.1 平方读数已经暴露了两个问题

<a id="noise-output"></a>

令Z=B₁，F=Z²。对x>0，把两个原像±√x的Gaussian密度相加并乘变量变换的Jacobian，得到下面的密度。F在0没有原子，但密度在那里无界。存在密度与拥有光滑密度，已经是两件不同的事。

\[ p_F(x)=\frac{e^{-x/2}}{\sqrt{2\pi x}}\mathbf1_{\{x>0\}}. \]

这里可以直接算，因为只需反解一个函数。对于随机方程在时刻t的输出，反解整条Brownian轨迹通常没有意义。值得保留的线索是：平方映射在原像0附近反应迟钝。我们能否不反解输出，而通过它对噪声的响应识别分布？

## 39.2 粗糙路径仍然可以被平移

<a id="noise-directions"></a>

取h∈L²[0,1]，让每条路径增加同一确定曲线k_h(t)=∫₀ᵗh(s)ds。第33章证明，这类平移与原Wiener测度等价，能量是‖h‖₂²。若平移不在Cameron–Martin类，两份路径律可能已经奇异，便失去用同一概率权重比较微小响应的基础。H的选择来自这个结构，不是要求Brownian本身属于H。

\[ \left.\frac d{d\varepsilon}(B_1+\varepsilon k_h(1))^2\right|_{\varepsilon=0}=2B_1\int_0^1h(s)ds,\qquad \left.\frac d{d\varepsilon}\int_0^1(B_s+\varepsilon k_h(s))ds\right|_0=\int_0^1(1-s)h(s)ds. \]

一个响应由\(2B_1\mathbf1_{[0,1]}\)表示，另一个由确定函数1−s表示。它们是H中的敏感度，不是dBₜ/dt。Brownian处处不可微的结论仍然原封不动；我们改变的是微分的对象与方向。

## 39.3 Gaussian权重会参与分部积分

<a id="noise-ibp"></a>

对标准Gaussian向量ξ及光滑多项式增长f，普通积分分部给E∂ᵢf(ξ)=E[ξᵢf(ξ)]。积分测度不是平坦体积：密度求导会留下ξᵢ。正是这个项，使输出的导数有希望被转移到一份可积权重上，从而研究输出概率律，而不必先知道它的密度。

\[ E[G\langle DF,h\rangle_H]=E\left[F\left(GW(h)-\langle DG,h\rangle_H\right)\right]. \]

先把这些方向响应的Hilbert表示记作DF，并把F,G理解成有限Gaussian坐标的光滑函数，公式就是逐坐标积分。后面所有无限维延拓都要保留这条身份；它比“对随机性求导”这个口号精确得多。

## 39.4 用Hilbert结构记录全部方向

<a id="noise-isonormal"></a>

取23章的实可分Hilbert H与isonormal族W，协方差E W(h)W(k)=〈h,k〉。只使用σ(W)生成的随机变量。若F=f(W(h₁),…,W(hₙ))为光滑柱函数，f及各阶导数至多多项式增长，定义下式。把所有方向放进同一个有限正交空间，Gaussian密度满支撑保证不同表示给同一导数；定义不依赖挑选哪几个坐标。

\[ DF=\sum_i\partial_if(W(h_1),\ldots,W(h_n))h_i,\qquad D_hF=\langle DF,h\rangle_H. \]

这并不是一颗H值“标准Gaussian随机点”的普通梯度。无限维恒等协方差不能给H值Gaussian样本，23章已说明；但每个柱输出的敏感度确实是H向量。微分结构可以存在于输出的变化中，而不要求把噪声本身误当成一个有界线性泛函。

## 39.5 只逼近函数值，不足以逼近敏感度

<a id="noise-closed"></a>

仪器输出可能只能被有限坐标逼近。若Fₙ→F于L²，能否直接把DFₙ的极限叫作DF？例子sin(nZ)/n已提醒不能：函数值趋0，导数cos(nZ)的平方均值却趋1/2；取间隔增大的频率，导数不Cauchy。需要的是函数值和敏感度同时受控。

关键结论是可闭性：Fₙ→0于Lᵖ且DFₙ→U于Lᵖ(H)，1<p<∞，则U=0。证明不是一种约定。用39.3的身份测试G h，右边由Hölder趋0，左边趋E[G〈U,h〉]；柱测试稠密、可数方向分离H，迫使U=0。[完整证明](../foundations/t-malliavin.md#malliavin-proof-closed)因此给出一个与逼近方式无关的闭导数。

## 39.6 Sobolev域描述的是哪种可微性

<a id="noise-sobolev"></a>

\[ \|F\|_{k,p}^p=E|F|^p+\sum_{j=1}^kE\|D^jF\|_{H^{\otimes j}}^p,\qquad \mathbb D^{k,p}=\overline S^{\|\cdot\|_{k,p}},\quad1<p<\infty. \]

把所有阶k≥1及p>1的域取交，记为D∞。这个完备化成为Lᵖ中的实际随机变量，靠的是刚证的闭性。它记录噪声方向的弱导数及其可积性，不要求每条样本的时间导数。链式与乘积法则先在柱函数成立，再由图范数、Hölder和截断延拓；例如两个\(\mathbb D^{1,2}\)变量的乘积未必仍在\(\mathbb D^{1,2}\)，\(\mathbb D^{1,4}\)是一个足够条件。

闭导数并未失去原来的平移意义：对F∈D^{1,p}、确定h和1<q<p，Cameron–Martin差商在Lᑫ趋〈DF,h〉。[平移的精确证明](../foundations/t-malliavin.md#malliavin-proof-shift)说明为什么这里保留q<p，不随便声称任意代表逐路径Fréchet可微。

## 39.7 把导数转移出去，需要一个伴随

<a id="noise-divergence"></a>

若想把E〈DG,U〉写成E[G乘某个随机变量]，对G的依赖必须受‖G‖₂控制。满足该条件的U才属于散度δ的定义域。Hilbert表示给出δU；这不是对任意平方可积随机过程自动可用的新积分符号。

\[ E[G\delta U]=E\langle DG,U\rangle_H,\qquad \delta(Gh)=GW(h)-\langle DG,h\rangle_H. \]

对确定h，δh=W(h)；对随机G，额外项不能丢。有限维公式给‖δU‖₂²≤E‖U‖²+E‖DU‖²，所以\(\mathbb D^{1,2}\)(H)是足够的定义域。下一步要把这份有限坐标微分与所有Gaussian输出联系起来，而不是只在容易微分的柱函数中打转。

## 39.8 平方以后留下的，不只是平均值

<a id="noise-hermite"></a>

Z²先减去平均1，得到Z²−1；Z³则减去3Z，才与低阶项正交。Hermite多项式系统地去掉这些低阶投影。对标准Gaussian，反复分部积分给EHₙHₘ=n!1_{n=m}，其中H₀=1、H₁=x、H₂=x²−1。归一化中的n!以后决定导数与积分的常数。

\[ e^{tx-t^2/2}=\sum_{n\ge0}\frac{t^n}{n!}H_n(x),\qquad H_n^\prime=nH_{n-1}. \]

这不是把一般随机变量写成普通Taylor级数。正交性在L²概率空间中，而非每条路径上的点态展开。不同阶也不独立：Z与Z²−1仍由同一个Z决定。

## 39.9 Wiener chaos为什么能穷尽L²

<a id="noise-chaos"></a>

用H的一组正交基，Gaussian噪声成为可数独立坐标。Hermite乘积按总次数分层；把次数n的系数整理成对称张量fₙ，便得到下面的展开。Iₙ先由这些乘积定义，n!等距再延到完整对称张量空间。

\[ F=\sum_{n=0}^\infty I_n(f_n),\quad E|F|^2=\sum_{n=0}^\infty n!\|f_n\|^2,\qquad E[I_n(f)I_m(g)]=\mathbf1_{n=m}n!\langle f,g\rangle. \]

完备性不能从正交性直接得出。Gaussian指数的Hermite部分和在L²趋于该指数，而33章已证明Gaussian指数全性；所以与全部chaos正交的变量只能为0。[T-GAUSSIAN 1–2](../foundations/t-gaussian.md#gaussian-proof-chaos)完成这一步及基无关性。

## 39.10 有序积分与对称核，是同一层随机性

<a id="noise-multiple"></a>

对Brownian H=L²[0,T]，Iₙ也能由31章Itô积分迭代得到：先在时间单纯形积分，再乘n!。这个因子不是习惯任选；对称核在n!个时间排列中贡献相同，时间对角的Lebesgue体积为0。

\[ I_n(f)=n!\int_{0<t_1<\cdots<t_n<T} f(t_1,\ldots,t_n)\,dB_{t_1}\cdots dB_{t_n}. \]

确定指数的Picard级数与Hermite生成函数比较，先证明纯张量，再由极化和等距证明一般核。[完整识别](../foundations/t-gaussian.md#gaussian-proof-multiple)说明这不是先定义散度再倒过来证明Itô积分。chaos阶数描述输出的Gaussian组合结构，不描述样本路径有多少阶时间导数。

## 39.11 高阶chaos为什么更昂贵

<a id="noise-number"></a>

\[ E\|DF\|_H^2=\sum_{n\ge1}n\,n!\|f_n\|^2,\qquad F\in\mathbb D^{1,2}\ \Longleftrightarrow\ \sum_{n\ge1}n\,n!\|f_n\|^2<\infty\quad(F\in L^2). \]

求导让次数n降一阶，却乘n；正交性使这份敏感度成本成为精确的级数权重。并非全部L²输出都可微：Σₙ≥₁Hₙ(Z)/(n√n!)的L²范数有限，导数能量却含Σ1/n而发散。有限坐标可计算，不意味着无限极限自动保留导数。

把W与独立副本按\(e^{-t}\)和√(1−\(e^{-2t}\))混合再平均，得到Mehler半群；它在第n阶乘\(e^{-nt}\)，生成元是−N，N在第n阶乘n。δD=N在明确的L²定义域成立。这里重新出现OU结构，却是在噪声空间中抑制高阶响应，而非把原Brownian时间加速。[系数与定义域全证](../foundations/t-gaussian.md#gaussian-proof-number)。

## 39.12 随机系数使散度超出普通等距

<a id="noise-divergence-bounds"></a>

例如U=\(B_T\mathbf1_{[0,T]}\)依赖增量发生以后的信息。伴随公式给δU=B_T²−T，而非把B_T当确定系数直接拿出的B_T²。其方差2T²也不等于E‖U‖²=T²。散度允许某些非适应输入，但必须付出新的定义域与修正项；它没有取消Itô积分对信息顺序的要求。

在光滑场上D_hδU=〈U,h〉+δ(D_hU)。后面要反复转移导数，正是这条交换式决定需要控制多少阶敏感度，而不能只反复引用一次L²上界。[散度域与交换式](../foundations/t-malliavin.md#malliavin-proof-divergence)均从有限Gaussian分部积分建立。

## 39.13 一阶敏感度何时足以排除奇异分布

<a id="noise-absolute"></a>

对标量有一个精确的一阶结论：F∈\(\mathbb D^{1,2}\)且‖DF‖>0几乎必然，则F的律绝对连续，不要求逆导数矩。其证明先沿单个Gaussian坐标切片；Sobolev闭性使几乎每个切片绝对连续。一个绝对连续实函数在零测集的原像上，其导数只能几乎处处为0，否则局部逆Lipschitz会把零测集的原像也压成零测。

\[ E\big[\mathbf1_{\{F\in N\}}\|DF\|_H^2\big]=0\quad\hbox{for every Lebesgue-null }N,\qquad \|DF\|_H>0\ \hbox{a.s.}\ \Longrightarrow\ \mathcal L(F)\ll dx. \]

对可数Gaussian方向求和就得到上式。[切片与零集论证](../foundations/t-malliavin-density.md#density-proof-scalar)实际完成，不把非零导数直觉当证明。它排除的是奇异质量，尚未控制密度在某处是否尖锐。

## 39.14 协方差记录输出能否被独立推动

<a id="noise-covariance"></a>

向量输出可能重复报告同一信息。F=(B₁,2B₁)虽然有两个坐标，却始终在一条直线上。需要检查能否通过噪声方向独立推动每个输出分量；把各DFᵢ组成Gram矩阵就是Malliavin协方差。

\[ \gamma_F=(\langle DF_i,DF_j\rangle_H)_{i,j\le m},\qquad F=\left(B_1,\int_0^1B_sds\right)\Longrightarrow\gamma_F=\begin{pmatrix}1&1/2\\1/2&1/3\end{pmatrix},\quad\det\gamma_F=1/12. \]

同一条随机路径可以产生满秩二维输出，决定因素不是“有几条Brownian轨迹”，而是敏感度方向是否线性独立。对Fᵢ∈∩ₖ\(\mathbb D^{k,2}\)，detγ>0几乎必然足以给向量绝对连续：有限方向Gram矩阵最终满秩；条件于其余坐标，输出有C¹有限维版本，局部逆映射把零集原像送成零测。[完整证明](../foundations/t-malliavin-density.md#density-proof-vector)包含切片C¹构造，不把这个高阶版本冒充仅\(\mathbb D^{1,2}\)的最弱向量定理。

## 39.15 几乎处处非退化，仍然允许尖锐密度

<a id="noise-degeneracy"></a>

回看章首平方读数，不重新计算密度。它的DF=2Z、γ=4Z²，几乎必然不为0，却可任意接近0。正是这些反应极弱的样本使密度在0附近堆积。非退化只排除真正丢失方向，尚未限制方向接近丢失时的频率。

反过来，仅有很多阶导数也不够。取φ(x)=0于x≤0、φ(x)=exp(−1/x²)于x>0，所有导数有界，φ(Z)却有质量1/2的0原子。这次半数样本根本不响应。光滑性、满秩与逆协方差的可积性因而需要分别检查。

## 39.16 逆协方差给出恰好所需的方向

<a id="noise-weights"></a>

为了把输出坐标的∂ᵢφ(F)转移到噪声空间，我们需要一个随机方向Uᵢ，使〈DFₖ,Uᵢ〉等于δᵢₖ。这是线性方程，不是随意猜的权重；Gram矩阵可逆时解为下式。链式法则随后把输出导数变成Dφ(F)与Uᵢ的内积，散度再把它转移出去。

\[ U_i=\sum_j(\gamma_F^{-1})_{ij}DF_j,\qquad E[(\partial_i\varphi)(F)G]=E[\varphi(F)\delta(GU_i)]. \]

但\(\gamma^{-1}\)可很大，GUᵢ也未必在δ域中。我们需要的矩条件来自这个具体困难，而非为定理外观附加。若Fᵢ属于39.6的D∞且detγ的全部负矩有限，则截断倒数、链式法则及Hölder证明\(\gamma^{-1}\)、Uᵢ仍在D∞。[倒数截断证明](../foundations/t-malliavin-density.md#density-proof-weights)还明确保留了所有阶可积性。

## 39.17 反复分部积分不能跳过高阶控制

<a id="noise-higher"></a>

第一轮δ(GUᵢ)以后，下一轮还要对这个权重求导。若只掌握一次L²估计，证明会在这里断掉。我们实际建立足够的高阶散度界：对每个整数r，δU的2r阶矩由U到2r阶的Hilbert张量导数矩控制，常数不随有限坐标维数增长。

机制是反复用伴随与交换式，每次至少移去一个散度；最后只留下不同因子之间的张量收缩，Cauchy–Schwarz及Hölder控制全部项。[完整有限算法与极限](../foundations/t-malliavin.md#malliavin-proof-moments)证明δ把D∞场送回D∞。因此分部积分可真正迭代，而不是用一个尚未证明的最优不等式作黑箱。

## 39.18 光滑密度由高频衰减严格产生

<a id="noise-smooth-density"></a>

现在可以正式给结论：F的分量属于D∞，γ几乎必然正定，E(detγ)^{-p}<∞对所有p>1成立，则F有C∞密度。证明把φ取成exp(i〈θ,x〉)，反复分部积分把θ的幂移成可积权重；选择θ最大坐标，就得到任意多项式阶的特征函数衰减。

\[ |\varphi_F(\theta)|\le C_k(1+|\theta|)^{-k},\qquad p_F(x)=(2\pi)^{-m}\int e^{-i\langle\theta,x\rangle}\varphi_F(\theta)d\theta. \]

Fourier逆及每阶导数因而绝对可积。为避免先假设密度，加小Gaussian噪声先得到真实密度，再以一致极限和概率弱极限识别p_F。这条路线在[T-DENSITY 4](../foundations/t-malliavin-density.md#density-proof-smooth)完整实现；负矩只是一个明确充分条件，不是所有光滑密度的必要条件。

## 39.19 非退化不等于处处有统一下界

<a id="noise-lognormal"></a>

F=e^Z的γ=e^{2Z}没有确定正下界，但全部负矩都有限，F及所有噪声导数也有全部正矩。定理适用，给出整个实线上的光滑密度；在负半轴为0，在0的连接是平滑的。这个例子说明控制的是接近退化的概率与可积性，不一定要求每条样本都远离退化。

它同时提醒，光滑密度并不意味着密度在每个点都严格正。支持集、严格正性和光滑性仍是不同问题，不能让同一个“非退化”词替代全部证明。

## 39.20 没有显式解，也可以算敏感度

<a id="noise-sde"></a>

考虑确定初值及常数σ≠0的方程Xₜ=x+σBₜ+∫₀ᵗb(Xᵣ)dr，其中b光滑、所有正阶导数有界，b自身允许线性增长。第35章保证解存在唯一，这次要研究的是这份解对驱动路径的变化。先以二进Brownian折线驱动普通积分方程，它是有限Gaussian坐标的光滑函数；逐阶微分及Gronwall，再利用导数闭性，才能合法移去网格。

\[ D_sX_t=\sigma\exp\!\left(\int_s^t b^\prime(X_r)dr\right)\mathbf1_{\{s\le t\}},\qquad \gamma_{X_t}\ge\sigma^2t e^{-2\|b^\prime\|_\infty t}. \]

于是每个固定t>0都有光滑密度，例如b=−tanh时不需要显式转移核。这不是对35章存在唯一性换一种说法，而是新增了输出的分布正则性。[全部阶导数、网格极限与非退化证明](../foundations/t-malliavin-density.md#density-proof-sde)均已写出。一般乘性噪声与Hörmander括号条件并未因此完成。

## 39.21 未来敏感度怎样成为事前可用的系数

<a id="noise-clark"></a>

第33章已经知道Brownian自然滤过中的L²终值能表示为Itô积分，但存在定理没有直接给出系数。DF通常依赖未来；要把它变成事前可以使用的系数，应该保留当前信息能够识别的那一部分。

\[ F\in\mathbb D^{1,2}\quad\Longrightarrow\quad F=EF+\int_0^T E[D_tF\mid\mathcal F_t]\,dB_t. \]

这是Clark–Ocone公式。条件平均指dt⊗P等价类的可预测版本，不是逐时随意选版本。对柱函数，未来Gaussian增量的条件平均实际构造这个过程；L²收缩再移到闭域。对所有可预测U，散度δU正好等于Itô积分，伴随身份与33章表示等距便唯一识别系数。[完整版本及证明](../foundations/t-clark-ocone.md)。

平方读数的DₜF=2B_T，条件平均后成为2Bₜ。原来31章的平方恒等式在这里获得新的解释：积分系数不是终点敏感度本身，而是把它投影到当前信息后的读数。无需重复那里的平方变差证明。

## 39.22 噪声相同，信息不同，表示能力也会不同

<a id="noise-information"></a>

若在T时刻另揭开一枚独立硬币，硬币终值的条件平均会在T跳跃；Brownian Itô积分连续，不可能表示这份鞅。该终值不是σ(W)中的Gaussian可测输出，不能套用上一节。

所以“噪声能够表示一类鞅”同时依赖噪声和观察者的信息结构。Malliavin导数说明输出怎样响应扰动，Clark–Ocone又说明其中哪一部分能够按时间合法使用。敏感度不是预言，条件平均也没有把未来事件变成已知。

## 39.23 Cameron–Martin结构不局限于Wiener坐标

<a id="noise-banach"></a>

对可分Banach中的中心Radon Gaussian变量X，先以所有连续线性读数的L²闭包构造H，再定义i(h)=E[XW(h)]。Gaussian旋转给指数范数矩，保证这个向B的积分实际存在；i把噪声能量方向嵌入状态空间。i(H)不是预先指定的所有连续路径，而是由这份Gaussian律本身决定。

\[ \frac{d\mathcal L(X+i(h))}{d\mathcal L(X)}=e^{W(h)-\|h\|^2/2},\qquad b\notin i(H)\Longrightarrow\mathcal L(X+b)\perp\mathcal L(X). \]

[T-GAUSSIAN 5–6](../foundations/t-gaussian.md#gaussian-proof-fernique)完整证明指数矩、嵌入、平移等价与范围外的奇异性，兑现33章留下的Banach推广。与Wiener情形相比，新收获是：Hilbert能量不是只来自一组方便的时间坐标，它可以从一般Gaussian空间内在恢复。

## 39.24 改变输出坐标，不能制造或消除方向

<a id="noise-coordinates"></a>

在链式法则与可积性适用的范围，光滑坐标变换ψ给下面的协方差关系。若Jacobian可逆，秩不变；但D∞与全部负矩是全局可积性要求，任意增长过快的ψ未必保持它们。结构不变与某一组充分估计保持，不能混为一谈。

\[ \gamma_{\psi(F)}=D\psi(F)\gamma_FD\psi(F)^{\mathsf T},\qquad p_{\psi(F)}(y)=p_F(\psi^{-1}(y))\,|\det D\psi^{-1}(y)|. \]

第二式对Rᵐ上的光滑微分同胚及已有密度是普通变量变换；它保留光滑性，不需要重新假装证明一遍噪声非退化。这也使一个几何问题变得具体：若运动必须在重叠坐标图里描述，哪些对象依赖坐标写法，哪些来自运动本身？

## 39.25 粗糙没有消失，新的微分结构被辨认出来

<a id="noise-insight"></a>

Brownian路径仍然不能按普通时间微分。我们真正建立的是另一套结构：可比较的Cameron–Martin扰动、与逼近相容的闭导数、把导数移到概率权重上的散度，以及由协方差识别输出方向的机制。chaos又让敏感度能量成为一个可精确计算的阶数成本。

这些结构没有保证一切随机输出都光滑。平坦响应可以留下原子，几乎处处非退化仍允许尖锐密度，反复分部积分需要真正的可积性；额外信息又能破坏Brownian表示。边界与反例没有削弱理论，反而使我们知道它第一次能够可靠回答什么。

同一条粗糙随机轨迹，现在既可以用时间积分累积，也可以通过噪声方向研究响应。若再把轨迹放进弯曲空间，微分的表示便要接受坐标一致性的检验。我们需要分清的，将不只是“能否求导”，还有不同坐标中的随机微分究竟是否描述同一对象。

### 资料与证明范围

本章按有限Gaussian计算、闭算子、正交展开与概率律识别组织现代重建，不声称复现历史人物的原始思考。技术条件与[Hairer作者公开讲义](https://hairer.org/notes/StochasticAnalysisCourse.pdf)的Gaussian/Malliavin部分及[Nualart与Nualart原出版社目录](https://assets.cambridge.org/97811070/39124/frontmatter/9781107039124_frontmatter.pdf)对照，不复制其正文。

实际证明：[T-GAUSSIAN](../foundations/t-gaussian.md)、[T-MALLIAVIN](../foundations/t-malliavin.md)、[T-MALLIAVIN-DENSITY](../foundations/t-malliavin-density.md)、[T-CLARK-OCONE](../foundations/t-clark-ocone.md)。向量仅\(\mathbb D^{1,2}\)的最弱绝对连续版本、最优Meyer估计与一般Hörmander理论未在本章声称完成。
