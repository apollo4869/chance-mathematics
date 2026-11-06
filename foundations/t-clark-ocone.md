# T-CLARK-OCONE：可预测投影怎样识别鞅表示的系数

配套[第39章](../chapters/39-malliavin.md#noise-clark)。固定有限T>0，H=L²[0,T]、W(h)=∫h dB，滤过为Brownian通常自然滤过，终值对其\(F_T\)可测。33章已经实际证明L²鞅表示及滤过右连续性，本页不倒用本公式证明它们。

## 1. 适应过程的散度确实就是Itô积分

<a id="clark-proof-adapted"></a>

取U=G1_{(a,b]}，G为光滑、对\(\mathcal F_a\)可测的柱函数，其所有Gaussian方向支撑[0,a]。伴随公式给δU=G(B_b−B_a)−〈DG,1_{(a,b]}〉，第二项为0。有限和同样成立。一般G∈L²(\(\mathcal F_a\))由a以前Gaussian柱函数L²逼近，适应增量独立性及Itô等距使U和对应δU都L²收敛；δ闭性把身份延过去。

\[ U\ \hbox{predictable},\quad E\int_0^T U_t^2dt<\infty\quad\Longrightarrow\quad U\in\operatorname{Dom}\delta,\quad\delta U=\int_0^T U_t\,dB_t. \]

31章简单可预测过程在该能量空间稠密，等距与δ闭性再给上式。对F∈\(\mathbb D^{1,2}\)，先在光滑核心测试，再按图范数取极限，得到E[F∫U dB]=E∫DₜF Uₜdt。没有要求每个适应U也具有Malliavin导数。

## 2. 逐时条件平均需要可预测版本

<a id="clark-proof-projection"></a>

先令F=f(W(h₁),…,W(hₙ))。记Mᵢ(t)=∫₀ᵗhᵢdB，Qᵢⱼ(t)=∫ₜᵀhᵢhⱼds。给定\(\mathcal F_t\)，未来读数是独立中心Gaussian、协方差Q(t)，故E[DₜF|\(\mathcal F_t\)]=Σᵢhᵢ(t)E_Z[∂ᵢf(M(t)+Q(t)^{1/2}Z)]。Q及其非负平方根连续；Gaussian矩支配与f的多项式增长使括号内是连续适应过程。乘确定Borel hᵢ(t)仍可预测。

条件Jensen与Fubini给‖K‖_{L²(dt⊗P)}≤‖DF‖_{L²(H)}。对\(F_n\)→F于\(\mathbb D^{1,2}\)，上述K_n在可预测L²闭子空间收敛到K。取子列使D\(F_n\)(t)和K_n(t)对几乎每个t在L²(P)收敛，条件期望收缩给\(K_t\)=E[\(D_tF\)|\(\mathcal F_t\)]对dt几乎处处成立。因此这个写法指一个dt⊗P等价类的可预测版本，不是对每个t任意选择不相容条件版本。

## 3. 表示系数由对偶性唯一识别

<a id="clark-proof-formula"></a>

\[ F\in\mathbb D^{1,2}\quad\Longrightarrow\quad F=EF+\int_0^T E[D_tF\mid\mathcal F_t]\,dB_t. \]

33章给F−EF=∫H dB，H可预测平方可积。对所有这样的U，第1节与投影定义给E∫HU dt=E[F∫U dB]=E∫DF U dt=E∫KU dt。取U=H−K得H=K于dt⊗P，等距及Doob给对应过程版本唯一。这个证明同时说明本公式比存在表示多了什么：它把被积系数识别为事前可用的噪声敏感度，而不是任意一个事后导数。

例如F=B_T²，DₜF=2B_T，而Kₜ=2Bₜ，所以F=T+∫2BₜdBₜ。这里不重复31章平方变差证明，而解释为何要投影未来敏感度。若T时刻另揭开独立硬币Z，其终值条件平均在T跳跃，Brownian Itô积分却连续，不能表示它；Z也不属于本页的σ(W)终值类。信息结构是定理的条件，不是附属语言。[回正文](../chapters/39-malliavin.md#noise-information)。
