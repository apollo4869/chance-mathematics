# T-POTENTIAL：调和、过分、Green、容量与扫掠的实际证明

配套[第38章](../chapters/38-feynman-kac.md#potential-excessive)。一般Markov部分使用明确的有界连续版本；完整Riesz分解、平衡测度及扫掠在有界区间的被杀Brownian类实际证明。高维Dirichlet与极性反例见T-FEYNMAN-KAC；不把一维曲率证明说成所有Hunt过程的Riesz理论。

## 1. 未来的收益为什么比现在的总收益小

<a id="potential-proof-excessive"></a>

令X为强Markov，寿命ζ，A为从0开始、连续非负递增的加性泛函，u(x)=Eₓ∫₀ζe^{-αs}dAₛ有限。分割时间积分及Markov给u−\(e^{-\alpha t}\)Pₜu=Eₓ∫₀^{t∧ζ}e^{-αs}dAₛ≥0。t↓0时右侧由单调收敛趋0，所以u是α-过分函数：\(e^{-\alpha t}\)Pₜu≤u且极限为u。后一个条件排除人为修改的坏版本，不是可有可无的装饰。

\[ u\ge e^{-\alpha t}P_tu,\qquad \lim_{t\downarrow0}e^{-\alpha t}P_tu=u,\qquad e^{-\alpha t}u(X_t)\ \hbox{is a supermartingale when integrable}. \]

超鞅结论对确定时刻是条件Markov的一行计算；若u连续、局部有界，则X连续时路径连续，停止在紧集后可用16/30章抽样，再去局部化。一般Borel过分函数沿Hunt路径的精细右连续版本需要额外定理，本页不借这项尚未证明的推广。对于调和函数，球内退出前等式成立；“平均不变”与“平均只能下降”是不同结构。

## 2. 区间上的Green核与Riesz分解

<a id="potential-proof-riesz"></a>

取I=(a,b)，Brownian在退出τ时被杀，参考测度dx。36章停止与37章占用已给核G；也可直接对x检验端点0、分段线性、导数在y跳−2，从广义Itô取期望重新验证。它是相对于dx的占用核，不是相对于速度2dx的半核。

\[ G_I(x,y)=2\frac{(x\wedge y-a)(b-(x\vee y))}{b-a},\qquad E_x\int_0^\tau f(B_s)ds=\int_IG_I(x,y)f(y)dy. \]

此节固定α=0。设u在I连续、有限、非负且为被杀Brownian的0-过分函数。停止在任意子区间(c,d)的退出，因u在那里有界，抽样给u(x)≥[(d−x)u(c)+(x−c)u(d)]/(d−c)，所以u凹。反过来非负凹u以紧区间停止、广义Itô给超鞅，Fatou移去停止；时间0由连续性给极限，因此过分。凹性强迫两个端点极限有限且非负：若某端趋∞，与固定内点的弦值将迫使另一个内点无限。

\[ \mu=-\frac12u^{\prime\prime}\ge0,\qquad u(x)=h(x)+\int_IG_I(x,y)\mu(dy),\qquad h(x)=\frac{b-x}{b-a}u(a+)+\frac{x-a}{b-a}u(b-). \]

二阶导数按分布理解：凹u的单侧导数单调，Stieltjes构造给局部有限μ。先在Iₙ=(aₙ,bₙ)⊂⊂I积分二阶测度，u−hₙ与G_{Iₙ}μ有相同二阶导数及端点值，故相等。取aₙ↓a、bₙ↑b，Green核逐点递增到G_I，hₙ趋h；MCT给上式，且势有限。唯一性由二阶导数和端点极限分别识别μ与h。任何非负调和小于u的函数是线性的，其端点值不超过u的极限，故它不超过h；h是最大非负调和下界。

这里的μ可以在端点附近总质量无穷，只要Gμ在内部有限；它仍为Radon测度。由37章局部时间令Aₜ=∫L_{t∧τ}ʸμ(dy)，在任何t<τ其路径范围是I内紧集，故Aₜ有限；EₓAτ=Gμ(x)<∞又排除终端无穷。于是Riesz中的势确实等于一份路径累积的期望。边界的调和部分不是源项，它记录尚未在内部消耗的终端信息。

## 3. 容量衡量的不是长度

<a id="potential-proof-capacity"></a>

在I上取H₀¹为绝对连续零端点且导数平方可积的函数，能量E(v)=½∫|v′|²dx。对非空紧K⊂I定义cap_I(K)=inf{E(v):v∈H₀¹,v≥1于K}。这一约束逐点有意义，因为一维H₀¹具有连续版本；这里不借高维未证的准连续理论。取p=minK，q=maxK。候选e在(a,p)线性从0到1，在[p,q]为1，在(q,b)线性回0。

\[ e_K(x)=P_x(T_K<\tau),\qquad \operatorname{cap}_I(K)=\frac1{2(p-a)}+\frac1{2(b-q)},\qquad \eta_K=-\frac12e_K^{\prime\prime}=\frac{\delta_p}{2(p-a)}+\frac{\delta_q}{2(b-q)}. \]

任意可行v可先截断到[0,1]而不增能量。Cauchy–Schwarz给∫ₐᵖ|v′|²≥1/(p−a)，另一侧同样；中间能量非负，候选达到下界，故最优且唯一。连续路径在K的两端之间不可能先逃出I而不命中K，区间命中概率使候选等于所写概率。导数跳跃给η，其总质量恰为能量；Riesz给e=Gη。特别单点c的容量为(b−a)/(2(c−a)(b−c))>0，虽然它的长度为0。

\(d\ge2\)中的点则可为极性；T-FEYNMAN-KAC的径向计算已给穿孔球实例。因此“参考测度为零”和“路径几乎不可能触及”并非同义。一般Revuz平滑测度不能给极集收费。把一维δ_c的合法性直接搬到二维δ_c，是维数敏感的错误。

## 4. 把内部的源扫到可命中的集合

<a id="potential-proof-balayage"></a>

仍在I，取紧K、有限正μ，T=\(T_K\)。把从y出发先命中K再退出I的命中分布对μ混合，得μᴷ。强Markov把普通占用分成T以前和以后，给Green核分解。T以前的过程是在\(I\setminus K\)中被杀，其Green核对称：各连通开区间使用上面的对称核，跨分量为0。因此分解的余项在x,y也对称。

\[ \mu^K(C)=\int_I P_y(B_T\in C,T<\tau)\mu(dy),\quad G_I\mu^K(x)=E_x[G_I\mu(B_T);T<\tau]\le G_I\mu(x). \]

将Green分解的余项先关于μ积分，再用对称性，把x的命中积分移到y，正好得到上式。所有交换都是非负Tonelli。扫掠势在K与原势相等，在I\K调和，并且不超过原势；它是保留集合K上的观测而移除其他内部源后的确定对象。对有限带符号μ可在绝对Green势有限处分别应用正负部分，不无条件宣称全空间有界。返回[正文的扫掠](../chapters/38-feynman-kac.md#potential-sweeping)。
