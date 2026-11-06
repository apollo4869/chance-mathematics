# T-MALLIAVIN：闭导数、Sobolev域、散度与高阶控制

配套[第39章](../chapters/39-malliavin.md#noise-closed)。固定实可分H及isonormal W，全部随机变量对σ(W)可测。S为f(W(h₁),…,W(hₙ))，f光滑且自身与各阶导数至多多项式增长；H值及张量值柱函数为有限确定向量乘S的和。各结论不需要先有chaos。

## 1. 内在方向导数与Gaussian分部积分

<a id="malliavin-proof-ibp"></a>

\[ DF=\sum_{i=1}^n\partial_if(W(h_1),\ldots,W(h_n))h_i,\qquad E\langle DF,h\rangle=E[F W(h)]. \]

若两种柱表示给同一F，把所有h放入同一个有限维正交空间。对应Gaussian向量有严格正密度；两光滑函数几乎处处相同即处处相同，其一阶与高阶导数亦相同。因此DF与表示无关。有限维Gaussian密度的导数为−xᵢ乘密度，逐坐标积分给上式；多项式增长使边界项为0。乘积规则由普通微分先得，再应用上式，得到核心测试身份。

\[ E[G\langle DF,h\rangle]=E\big[F(GW(h)-\langle DG,h\rangle)\big],\qquad F,G\in S. \]

S在每个Lᵖ、1≤p<∞中稠密：可数正交坐标生成σ(W)，有限坐标条件平均以15章结果逼近有界变量；有限Gaussian测度的紧正则性与光滑卷积逼近给光滑柱逼近，最后截断一般Lᵖ变量。H值及可分Hilbert张量值空间先截断确定基，再用标量稠密性。

## 2. 为什么柱导数能成为闭算子

<a id="malliavin-proof-closed"></a>

设1<p<∞，Fₙ→0于Lᵖ，DFₙ→U于Lᵖ(H)。对任意G∈S及h∈H用上一节，右侧趋0，因为括号内测试有全部Gaussian矩。故E[G〈U,h〉]=0。用Lᑫ稠密性及Hölder扩到所有有界测试，再取可数正交基得U=0。因此D可闭；没有假设逐样本方向导数在任意代表上存在。对张量值变量逐确定分量做同一检验即得相同闭性。

\[ \|F\|_{k,p}^p=E|F|^p+\sum_{j=1}^k E\|D^jF\|_{H^{\otimes j}}^p,\qquad \mathbb D^{k,p}=\overline S^{\,\|\cdot\|_{k,p}},\qquad \mathbb D^\infty=\bigcap_{k\ge1,\,p>1}\mathbb D^{k,p}. \]

递归闭性把上述完备化嵌入Lᵖ，导数唯一。Bochner Lᵖ完备性可由可求和子列证明：范数差可求和时，几乎处处在完备Hilbert值空间绝对收敛，Minkowski控制尾部；无需另借Banach空间紧性。对C¹且导数有界的φ，先对柱函数用链式法则，φ′有界与DF的Lᵖ控制使闭性可移去逼近，得到Dφ(F)=φ′(F)DF。高阶有界导数及多元情形逐次处理。

乘积要检查矩条件：例如F,G∈\(\mathbb D^{1,4}\)保证FG∈\(\mathbb D^{1,2}\)，D(FG)=F DG+G DF，由Hölder及闭性证明，不能只假设两者\(\mathbb D^{1,2}\)。D∞中的有限乘积、内积与多项式增长光滑复合由截断、Hölder及逐阶链式法则保留；p可先选大，再送到所需p。若单个Gaussian坐标的光滑函数及其各阶导数有全部正矩，也可用χ(x/n)截断，乘积导数由各阶原导数之和支配，DCT与闭性给D∞；例如e^Z不必错误地归入多项式增长核心。

## 3. 散度是伴随，不是所有平方可积过程的积分

<a id="malliavin-proof-divergence"></a>

对U∈L²(H)，若存在C使|E〈DG,U〉|≤C‖G‖₂对所有G∈S成立，则Hilbert Riesz给唯一δU∈L²，使E[GδU]=E〈DG,U〉。这定义Domδ；S稠密保证唯一。若Uₙ→U、δUₙ→Y均为L²，则测试极限给U∈Domδ且δU=Y，故δ闭。

\[ \delta(Gh)=G W(h)-\langle DG,h\rangle,\qquad E\delta U=0. \]

对光滑有限秩U,V，取同一有限Gaussian基，δU=Σᵢ(ξᵢUᵢ−∂ᵢUᵢ)。两次分部积分给下面恒等式；转置项可为负，但由Hilbert–Schmidt Cauchy–Schwarz给上界。有限秩柱场在\(\mathbb D^{1,2}\)(H)稠密，δ闭性遂证明该空间包含于Domδ。

\[ E(\delta U)(\delta V)=E\langle U,V\rangle+E\sum_{i,j}(D_iU_j)(D_jV_i),\qquad \|\delta U\|_2^2\le\|U\|_{L^2(H)}^2+\|DU\|_{L^2(H^{\otimes2})}^2. \]

这里不是一般等距。H=L²[0,T]、U=\(B_T\mathbf1_{[0,T]}\)时，δU=B_T²−T，方差2T²，而E‖U‖²=T²。若强行把随机系数当作已知确定数，便丢掉伴随所要求的修正。对K值场，逐分量求δ并以K内积求和，得到完全相同的L²上界。

## 4. 导数与散度如何交换

<a id="malliavin-proof-commutation"></a>

\[ D_h\delta U=\langle U,h\rangle+\delta(D_hU). \]

在有限坐标公式中求∂ⱼ，导ξᵢ产生Uⱼ，其余项正好δ(∂ⱼU)。对张量值输出保持H散度指标，其他指标只作参数；因此DᵏδU是δ(DᵏU)加k个\(D^{k-1}U\)的指标置换。每个置换为Hilbert等距。此公式先在光滑柱场成立，延到闭域时必须有相应导数及δ可积性；下一节给足够而非最优的控制。

## 5. 高阶可积性不能只靠L²不等式

<a id="malliavin-proof-moments"></a>

\[ E\|\delta U\|_K^{2r}\le C_r\sum_{j=0}^{2r}E\|D^jU\|_{H^{\otimes(j+1)}\otimes K}^{2r},\quad r\in\mathbb N. \]

先令U依赖有限Gaussian坐标、取有限维H及K值。展开‖δU‖^{2r}为2r个散度因子的全收缩，K指标两两配对。对一个尚在的δ用伴随身份，把它移到其余乘积的导数上。若导数击中普通系数，散度数少1；若击中另一个δ，用上一节交换式，得到普通项或保留那个δ并多一阶导数。无论哪种，尚在的散度数至少少1。重复至多2r次便没有δ，也没有Gaussian坐标乘子留下。每个原始U仍只出现一次，至多被求导2r次；项数只依r。

所有最终指标都在两个不同因子间成对收缩，没有单个因子内部的自由迹：伴随时导数从不作用于刚被移走的场本身。下面的收缩界因此没有维数常数。把因子当作图的顶点、配对指标当边。对一个顶点的全部边指标用Cauchy–Schwarz；其余因子按相邻顶点分组，沿这些边平方积分得到新的因子，新的全Hilbert范数等于原范数。删去该顶点，归纳得到每个全收缩绝对值≤各因子的Hilbert–Schmidt范数乘积。此证对多重边同样成立；若有自环则不成立，故前面的无自环检查必要。

对每项再用2r因子Hölder，随后对有限项求和，便得上式。有限维投影常数独立于维数；对\(\mathbb D^{2r,2r}\)(H⊗K)的光滑柱逼近，差场满足同一估计，故δUₙ在L^{2r}(K) Cauchy，其L²极限由δ闭性识别。结合交换式，对每个k,r以U的k+2r阶导数控制DᵏδU，得到δ:D∞(H⊗K)→D∞(K)。这是真正需要的足够结果，不把它夸成最优的Meyer不等式。

## 6. 闭导数仍然回应真实的噪声平移

<a id="malliavin-proof-shift"></a>

把噪声实现成可数Gaussian坐标，平移τ_{sh}使ξⱼ变为ξⱼ+s〈h,eⱼ〉。33章可数Gaussian平移已给严格正密度exp(sW(h)−s²‖h‖²/2)。因此对1<q<p，Hölder给‖G∘τ_{sh}‖_q≤C‖G‖_p，C在有界s区间一致。先对柱G用连续性，再以此界逼近，得到平移在Lᵖ→Lᑫ的强连续性；不声称它对任意Lᵖ变量是Lᵖ有界算子。

\[ F\in\mathbb D^{1,p},\ h\in H,\ 1<q<p\quad\Longrightarrow\quad \frac{F\circ\tau_{\varepsilon h}-F}{\varepsilon}\longrightarrow\langle DF,h\rangle_H\quad\hbox{in }L^q. \]

对柱F，普通微积分给差商等于∫₀¹〈DF,h〉∘τ_{θεh}dθ。图范数逼近与上面的统一Hölder界把身份延到D^{1,p}，Bochner积分的可测性在坐标实现下直接成立；强连续性再使右边趋〈DF,h〉。这个方向是Cameron–Martin能量方向，不是Brownian曲线关于时间的差商，更不声称任意代表都逐路径Fréchet可微。[回正文](../chapters/39-malliavin.md#noise-directions)。
