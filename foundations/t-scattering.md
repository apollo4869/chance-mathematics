# T-SCATTERING：独立位移、耗散与Cox极限

返回[第49章](../chapters/49-random-measures.md#mass-scattering)。输入空间E、目标F均LCSC度量；Ξₙ为局部有限整数点测度，Kₙ为E到F的确定次概率核，缺少的质量送到墓地点。概率核是特例；次概率版本同时包含稀释。各点给定输入后独立，不假设输入点彼此独立。全篇不使用Palm或Mecke公式。

## 1. 可测条件构造与无限乘积

<a id="scattering-construction"></a>

T-POINT-MEASURES枚举Ξ的每次出现，包括重数。以第10章可测随机化函数和可数独立均匀变量产生各Yᵢ，墓地点不计入输出η。每个评价η(A)为可数可测示性和。若\(\Lambda(B)=\sum_iK(x_i,B)<\infty\)对每个目标紧穷竭B成立，条件期望有限使η(B)有限a.s.，可数B统一零集，从而η是随机Radon点测度。Λ本身由T-MASS-KERNELS联合可测结论成为随机测度。

给定输入，有限前r项的Laplace泛函是\(\prod_{i\le r}(1-a_i)\)，其中\(a_i=K(1-e^{-f})(x_i)\)。有限部分计数单调增加，指数递减并有界，故条件支配收敛给无限乘积公式。若f支撑于B，\(\sum_i a_i\le\Lambda(B)<\infty\)。没有将无穷乘积的log展开当作无条件合法运算。

## 2. 整个窗口的总变差耦合

<a id="scattering-coupling"></a>

固定B，使m=Λ(B)<∞。第i个来源的窗口计数为Bernoulli(qᵢ)，\(q_i=K(x_i,B)\)。将其与Poisson(qᵢ)最大耦合，\(d_{TV}(\operatorname{Bern}(q_i),\operatorname{Poi}(q_i))=q_i(1-e^{-q_i})\le q_i^2\)。等计数1时共用一个按K(xᵢ,·∩B)/qᵢ抽出的点；Poisson端其余点独立按同一条件律抽样，qᵢ=0时统一为空。故整个单来源点测度也有这个误差界。

各来源独立耦合，有限前r个叠加的失配概率≤\(\sum_{i\le r}q_i^2\)。Poisson端叠加具有强度\(\sum_{i\le r}K(x_i,\cdot\cap B)\)，由48独立叠加定理。尾部在任一端出现任何点的概率≤\(\sum_{i>r}q_i\to0\)，所以取r→∞合法并给出

\[ d_{\rm TV}(\mathcal L(\eta|_B\mid\Xi),\operatorname{PRM}(\Lambda|_B))\le1\wedge\sum_iq_i^2\le1\wedge\{(\sup_iq_i)\Lambda(B)\}. \]

这里总变差定义为事件概率差的上确界，没有额外的二倍约定。条件核可测，故对其积分，任意事件的无条件差受右侧期望控制。这不要求在不同n之间使用同一个最大耦合，更不把耦合当作原系统的真实共同驱动。

参数耦合也可显式取可测版本：计数k的重叠质量取两概率质量的最小值，先按重叠总量选择共享计数，否则从各自剩余概率抽样；重叠量为0或1时分别固定约定。所有计数质量都是q的连续或可测函数，逆CDF抽样因而联合可测。条件位置核除以q，q=0时固定墓地点，再用10章核随机化。8章可数乘积完成全部来源，所以上面的条件比较确实来自可测概率核。

## 3. 平滑紧性与散射紧性等价

<a id="scattering-tightness"></a>

对任意一族，假设各Λₙ局部有限。给定输入，ηₙ(B)为可求和独立Bernoulli和，条件均值mₙ=Λₙ(B)，条件方差≤mₙ。有限部分L²收敛证明方差公式，不把无限方差交换直接略过。若mₙ一致紧，\(\mathbb P\{\eta_n(B)>R\}\le\mathbb P\{m_n>A\}+A/R\)，先A后R得窗口计数紧性。

反向，若mₙ>max(2R,8)，Chebyshev给\(\mathbb P\{\eta_n(B)\le R\mid\Xi_n\}\le4/m_n<1/2\)。所以\(\mathbb P\{m_n>\max(2R,8)\}\le2\mathbb P\{\eta_n(B)>R\}\)。散射窗口计数紧便推出平滑窗口质量紧。T-RANDOM-MEASURE-LIMITS及48点版本把逐紧窗口条件变成两类随机元的律紧性。这个等价甚至不需要耗散；耗散用于下一步Poisson近似。

## 4. 耗散Cox判据与完整双向极限

<a id="scattering-cox"></a>

再假设每个紧B有\(\epsilon_n(B)=\sup_xK_n(x,B)\to0\)。若Λₙ律紧，上一耦合界的期望趋0：在mₙ≤A上至多εₙA，补集至多P(mₙ>A)，先取A后取n。因而ηₙ与Cox(Λₙ)的每个紧窗口总变差趋0。对支撑于B的f，两个Laplace泛函差也趋0。

若\(\Lambda_n\Rightarrow\Lambda\)，T-MASS-KERNELS的Cox连续性与上述比较给ηₙ⇒Cox(Λ)。反向，若ηₙ⇒η，上一节先给Λₙ紧；任取其收敛子列Λₙⱼ⇒Λ′，正向结论迫使η等律Cox(Λ′)。T-MASS-KERNELS已完整证明Cox映射对指导测度律单射，故全部子列指导极限律相同。Prokhorov遂给Λₙ全序列收敛，且η必是Cox。由单射性，极限η为PRM(μ)当且仅当指导极限恒为确定测度μ。

需要的是输出局部有限、条件独立、目标窗口耗散及平滑律紧性，未假设输入简单、均匀、Poisson或有限平均。若不用耗散，恒等核作用在确定格点上保持格点，平滑也相同，却不会自动产生Poisson近似。若不用条件独立，共用同一大位移的格点反例保留刚性。

## 5. 可以任意细分的稀释恰好识别Cox律

<a id="scattering-thinning"></a>

一个直接的Cox刻画如下：局部有限点过程η为Cox，当且仅当对每个正整数n，存在局部有限点过程Ξₙ，使它的独立保留概率1/n稀释与η等律。不同n无需给在同一空间。充分性取次概率核Kₙ(x,dy)=δₓ(dy)/n，则εₙ(B)≤1/n、Λₙ=Ξₙ/n。输出律恒为η，故紧；上一节给指导极限存在及η为Cox。必要性若η=Cox(Λ)，取Ξₙ=Cox(nΛ)，给定Λ使用48独立稀释定理，输出正是Cox(Λ)。

这个刻画谈的是存在更大的点过程供独立稀释，不是把固定过程自己任意稀释以后保持原律。后者对于有限窗口正计数通常不成立。它也没有把任意强化或聚集过程都判成Cox。

## 6. 实线平稳平均的完整专用证明

<a id="scattering-averaging"></a>

设Ξ为实线上平稳随机Radon测度，\(c=\mathbb E\Xi[0,1)<\infty\)。在规范测度空间上平移\(\theta_h\mu(A)=\mu(A+h)\)联合可测：对f∈Cc，\((h,x)\mapsto f(x-h)\)联合连续，T-MASS-KERNELS给联合积分；可数坐标决定域。平均测度平移不变且局部有限，区间可加性与从有理长度单调逼近给\(\mathbb E\Xi(dx)=c\,dx\)。故固定位置没有平均原子，也没有a.s.原子，固定端点差异可以略去。

令Y(μ)=μ[0,1)，T=θ₁。第41章Birkhoff及L¹收敛给正向平均趋\(C=\mathbb E[Y\mid\mathcal I_T]\)于L¹和a.s.。T可逆，反向平均也给同一条件期望，因为\(\mathcal I_{T^{-1}}=\mathcal I_T\)。两者合并得\(\Xi[-N,N)/(2N)\to C\)于L¹。对实R取N=⌊R⌋，边界差的期望≤2c、分母之差趋0，故同一L¹极限成立。

对每个固定h，两长度2R窗口的对称差长度≤2|h|，故\(\|C\circ\theta_h-C\|_1=0\)。这里对每个h为模P不变，不声称删一个零集后对不可数所有h逐点相同。令\(\mathcal I\)为对全部h模P不变事件组成的σ代数，则C可取\(\mathcal I\)-可测版本；对A∈I，保测及A不变使\(\mathbb E[\mathbf1_AC]=\mathbb E[\mathbf1_AY]\)，所以\(C=\mathbb E[Y\mid\mathcal I]\)。全平移遍历时I平凡，C=c。

令\(K_R(x,dy)=\mathbf1_{\{|y-x|\le R\}}dy/(2R)\)。Tonelli给\(\Xi K_R(dy)=q_R(y)dy\)，且\(q_R(y)\to C\)于L¹，对固定y由窗口平移界得到。对f∈Cc，\(\mathbb E|\Xi K_Rf-C\int f|\le\int|f(y)|\mathbb E|q_R(y)-C|dy\to0\)，支配函数为2c|f|。可数测试及度量尾界给\(\Xi K_R\to Cdy\)依概率vague。若Ξ为点过程，\(\sup_xK_R(x,B)\le|B|/(2R)\)，耗散判据推出独立散射⇒Cox(Cdy)。Λₙ的共同极限存在于原规范空间，但散射结论仅声明分布极限。

## 7. 格点例子与独立性的边界

<a id="scattering-examples"></a>

对\(\Xi=\sum_{k\in\mathbb Z}\delta_{k+U}\)，任意窗口[y−R,y+R]计数与2R之差≤2，所以qR一致于y趋1。耗散散射趋PRM(dy)，不需再引用遍历性。格距随机为a∈{1,1/2}，给定a相位均匀于[0,a)，则窗口密度趋1/a，故极限Cox((1/a)dy)。其不交窗口计数协方差在二阶矩有限时为Var(1/a)乘两窗口长度，非普通Poisson独立性。

若全部格点共享同一位移，无论位移分布多宽，相位模1仍均匀，配置律仍为相位格点。长度小于1的窗口至多含一个点，Poisson极限却有正概率至少两个点，故两律不相同。它准确定位条件独立缺失，不诉诸图像上“看起来仍规则”。
