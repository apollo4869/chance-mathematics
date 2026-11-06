# T-MALLIAVIN-DENSITY：绝对连续性、光滑性与一个真实SDE应用

配套[第39章](../chapters/39-malliavin.md#noise-covariance)。先证明标量\(\mathbb D^{1,2}\)绝对连续判据，再证明高阶Sobolev向量判据及负矩条件下的光滑密度。它们是不同的定理；本页不以更强条件版本冒充向量最弱\(\mathbb D^{1,2}\)版本，也不证明一般Hörmander定理。

## 1. 标量的一阶导数怎样排除奇异质量

<a id="density-proof-scalar"></a>

先证明确定性事实：若f=c+∫g、g在区间上可积，则f绝对连续，并由38章Lebesgue微分定理几乎处处可微；N⊂R为Lebesgue零集，则f′=0几乎处处于f^{-1}(N)。在f可微且|f′|>1/k的点，存在n使对所有|y−x|<1/n有|f(y)−f(x)|≥|y−x|/(2k)。把这类点再分进长度<1/n的小区间，其限制逆映射是2k-Lipschitz。Lipschitz映射把零测集送到零测集：用任意小总长度的区间覆盖，再将长度乘Lipschitz常数。于是f^{-1}(N)在这些点的测度为0。对k,n及小区间可数并，剩下只可能f′=0或不可微点；后者对绝对连续f零测。

令F∈\(\mathbb D^{1,2}\)。固定Gaussian基坐标ξⱼ，把其余坐标记z。取柱逼近使Fₙ及DⱼFₙ的L²误差平方可求和，Fubini保证对几乎所有z在L²(γ₁)中收敛。在紧区间Gaussian密度有正下界，故这些切片在通常W^{1,2}中收敛。其极限有绝对连续版本，弱导数为DⱼF；这一点由基本定理及区间Poincaré直接证明，不使用待证密度定理。对每个零集N应用前段，得E[1_{F∈N}|DⱼF|²]=0。

\[ F\in\mathbb D^{1,2},\quad \|DF\|_H>0\ \hbox{a.s.}\quad\Longrightarrow\quad\mathcal L(F)\ll dx. \]

对可数j求和用Tonelli，得到E[1_{F∈N}‖DF‖²]=0；严格正性使P(F∈N)=0。注意不需要‖DF‖^{-1}的矩来证明这个标量结论，也没有因此证明密度连续。

## 2. 向量的满秩必须在真实方向上建立

<a id="density-proof-vector"></a>

\[ \gamma_F=(\langle DF_i,DF_j\rangle_H)_{i,j\le m},\qquad F_i\in\bigcap_{k\ge1}\mathbb D^{k,2},\quad\det\gamma_F>0\ \hbox{a.s.}\ \Longrightarrow\ \mathcal L(F)\ll dx\ \hbox{on }\mathbb R^m. \]

先证明有限坐标切片有C¹版本。固定前n个ξ为y，其余为z；取在\(\mathbb D^{n+1,2}\)收敛且误差可求和的柱逼近。Fubini及紧集Gaussian下界给几乎每个z的局部W^{n+1,2}收敛。对支撑在固定长方体的光滑v，迭代基本定理给v(x)=\((-1)^n\)\(\int_{x_1}^{\infty}\cdots\int_{x_n}^{\infty}\partial_1\cdots\partial_n v(y)\,dy\)，所以sup|v|≤‖∂₁…∂ₙv‖₁；对一阶导数同理，所需总阶≤n+1。乘紧支撑截断，以L²到L¹控制得函数和梯度一致Cauchy。因此切片C¹、普通梯度等于Gaussian弱方向导数。

在C¹映射y↦F(y,z)的秩m点，选m个非零子式，将F的m个分量与剩余n−m个坐标合成方映射Ψ。导数可逆；邻域内导数与固定可逆矩阵足够接近，差分积分给局部逆Lipschitz，收缩映射给局部满射到一个开邻域。因此Ψ局部双Lipschitz。对零集N⊂Rᵐ，N×R^{n−m}在Rⁿ零测，局部Lipschitz逆把它的预像也送成零测。用可数邻域覆盖全部满秩点，再对z积分。

有限方向协方差γ⁽ⁿ⁾=Σⱼ≤ₙ(DⱼF)(DⱼF)ᵀ逐点趋γ。若γ正定，有限某n已经正定，故以上满秩事件的并在detγ>0上为全部事件，得到结论。这个证明完整兑现所声明的高阶向量版本；向量只假设\(\mathbb D^{1,2}\)的更强Bouleau–Hirsch版本没有在这里冒充完成。

## 3. 非退化的方向怎样换成输出的导数

<a id="density-proof-weights"></a>

现在假设F_i∈D∞，detγ>0几乎必然，且E(detγ)^{-p}<∞对每个p>1成立。γ的条目、行列式及余子式属于D∞。对行列式取在x≤1/n为0、在x≥2/n为1/x的光滑截断，逐阶导数在x>0受C_k x^{-k−1}控制。多元链式法则、Hölder及全部负矩给各阶Lᵖ控制及DCT收敛，闭性推出\(\gamma^{-1}\)各条目属于D∞。

\[ U_i=\sum_j(\gamma_F^{-1})_{ij}DF_j,\qquad \langle DF_k,U_i\rangle=\delta_{ik},\quad H_i(G)=\delta(GU_i),\qquad E[(\partial_i\varphi)(F)G]=E[\varphi(F)H_i(G)]. \]

对G∈D∞，Uᵢ与GUᵢ也在D∞(H)，T-MALLIAVIN的实际高阶散度估计给Hᵢ(G)∈D∞，故不只是形式地写δ。测试φ先取光滑紧支撑，链式法则及伴随定义给身份；递归\(H_{i_1\ldots i_k}(G)=H_{i_k}(H_{i_1\ldots i_{k-1}}(G))\)，得到任意阶分部积分，所有权重都有L¹乃至所有正矩。

## 4. 从分部积分真正得到光滑密度

<a id="density-proof-smooth"></a>

取φ(x)=exp(i〈θ,x〉)，先乘扩大紧支撑截断，再用权重可积及F全部矩移去截断。于是(iθⱼ)ᵏϕ_F(θ)=E[e^{i〈θ,F〉}H_{j…j}(1)]。选|θⱼ|≥|θ|/√m，得到每个k的|ϕ_F(θ)|≤C_k(1+|θ|)^{-k}。因此Fourier逆及每阶导数绝对可积。

\[ p_F(x)=\frac1{(2\pi)^m}\int_{\mathbb R^m}e^{-i\langle\theta,x\rangle}\varphi_F(\theta)d\theta,\qquad \partial^\beta p_F(x)=\frac1{(2\pi)^m}\int(-i\theta)^\beta e^{-i\langle\theta,x\rangle}\varphi_F(\theta)d\theta. \]

为不循环假设F已有密度，加独立√ε标准Gaussian；14章Gaussian平滑确实给其密度，Fourier函数为ϕ_F exp(−ε|θ|²/2)。DCT使这些密度及每阶导数一致趋上式，故p≥0且C∞。同时F+√εZ→F几乎必然，紧支撑连续测试的期望极限识别p dx为F的律；递增测试至1给∫p=1。这还证明p及各阶导数有界。只要已有分部积分权重到N阶且N>m+r，同一论证就给Cʳ密度；无须把无穷阶条件说成必要条件。

反例分开检验：F=Z²属于D∞且γ=4Z²>0几乎必然，所以绝对连续；但其密度\(\mathbf1_{\{x>0\}}e^{-x/2}/\sqrt{2\pi x}\)在0发散，负矩条件确实失败。另一方面，φ(x)=0于x≤0、φ(x)=exp(−1/x²)于x>0是各阶导数有界的光滑函数，φ(Z)∈D∞却有质量1/2的0原子；此时γ在一半样本上为0。导数存在、非退化、负矩分别有不同职责。

## 5. 一个没有显式解的扩散，也能证明光滑密度

<a id="density-proof-sde"></a>

固定T>0、确定x及常数σ≠0，考虑Xₜ=x+σBₜ+∫₀ᵗb(Xᵣ)dr。假设b∈C∞且一阶及更高导数有界；b自身可线性增长。35章的全局Lipschitz存在唯一性适用。这里重新证明输出对噪声可微，不能因已有解就直接对方程形式求导。

令Bⁿ为二进网格Brownian折线，驱动对应普通积分方程Xⁿ。它是有限Gaussian坐标的光滑函数。这些折线近似只用作Gaussian柱逼近，不声称它们在原滤过下适应，也不把它们拿作Itô被积策略。Gronwall给sup|Xⁿ−X|≤|σ|e^{LT}sup|Bⁿ−B|；Brownian连续性与Doob全部正阶最大矩保证右边在每个Lᵖ趋0。H=L²[0,T]中DBⁿₜ=\(P_n\mathbf1_{[0,t]}\)，Pₙ为二进阶梯正交投影，supₜ‖\(P_n\mathbf1_{[0,t]}\)−\(\mathbf1_{[0,t]}\)‖≤√(网格长度)。

有限维普通微分先给Y₁ⁿ(t)=σ\(P_n\mathbf1_{[0,t]}\)+∫b′(Xᵣⁿ)Y₁ⁿ(r)dr。高阶Yₖⁿ的方程由集合{1,…,k}的分划给出：单块为b′Yₖⁿ，其余每个分划π贡献b^{(|π|)}(Xⁿ)乘各块对应的\(Y^n_{|A|}\)，按块分配张量指标。由有界系数及Gronwall逐k归纳，Yₖⁿ的H张量范数在[0,T]有确定上界\(C_{k,T}\)。

同样归纳收敛：b^{(j)}的Lipschitz常数由下一阶有界导数控制；产品差逐因子展开，旧阶收敛与确定上界使积分差在Lᵖ最大范数趋0，再用Gronwall。故每个Yₖⁿ收敛，闭性给Xₜ∈D∞。Xⁿ的函数值矩由线性增长及Brownian最大矩控制，各有限Gaussian方向导数的多项式增长保证它确属柱核心。

\[ D_sX_t=\sigma\exp\!\left(\int_s^t b^\prime(X_r)dr\right)\mathbf1_{\{s\le t\}},\qquad \gamma_{X_t}\ge\sigma^2 t e^{-2Lt}>0,\quad L=\|b^\prime\|_\infty,\quad t>0. \]

该式由极限Y₁的线性积分方程按s求解，在ds⊗P意义下成立。γ的确定下界给所有负矩，前节遂证明每个固定t>0的Xₜ有C∞密度。例如b=−tanh无需显式转移核；OU是线性特例，但这里新增的是非线性输出的噪声响应及非退化证明。没有证明一般乘性噪声、退化多维扩散或Hörmander括号定理，也不把t=0的点质量算作密度。返回[正文应用](../chapters/39-malliavin.md#noise-sde)。
