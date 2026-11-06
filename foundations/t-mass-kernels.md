# T-MASS-KERNELS：质量核、平滑与Poisson化

返回[第49章](../chapters/49-random-measures.md#mass-smoothing)。E、F均为局部紧第二可数度量空间。核的参数空间Z只需可测；随机概率核的随机化另外使用第10章标准Borel目标结论。所有无符号积分交换先对非负量使用Tonelli，不以有限均值作隐藏条件。

## 1. 参数与测度的联合积分

<a id="mass-kernel-measurable"></a>

若\(h:Z\times E\to[0,\infty]\)联合可测，则\((z,\mu)\mapsto\int h(z,x)\mu(dx)\)在\(Z\times\mathcal M_+(E)\)上可测。对\(h=\mathbf1_A(z)\mathbf1_B(x)\)这就是评价可测性；有限非负简单线性组合成立。先把x限制在紧穷竭Kₘ内，μ(Kₘ)处处有限，补集减法合法，矩形的π–λ或函数单调类给有界联合可测h；再令Kₘ穷竭，对一般非负h截断、单调逼近。这给出实际联合结论，不仅是分别可测。

设K为Z×E到F的概率核。\((\mu K_z)(A)=\int K(z,x,A)\mu(dx)\)逐实现由MCT可数可加。取F的紧穷竭Dₘ，令G为全部\(\mu K_z(D_m)<\infty\)的参数测度对；G可测。其上输出局部有限Borel测度，故由T-RIESZ为Radon；G外统一定义零测度后，全部评价仍可测，得到到\(\mathcal M_+(F)\)的可测映射。若应用中G概率1，这个修订只改零集。

对固定K，全部非负Borel f有\((\mu K)f=\mu(Kf)\)，由示性→简单→MCT建立。随机Ξ的平均\(\nu=\mathbb E\Xi\)于是满足\(\mathbb E[(\Xi K)f]=\nu(Kf)\)，允许无穷。Laplace泛函满足\(L_{\Xi K}(f)=\mathbb E e^{-\Xi(Kf)}\)；Kf未必连续或紧支撑，因此右侧是原随机测度的扩展可测读数，不能在未证明时直接拿vague收敛代入。

## 2. 连续核与小尺度平滑

<a id="mass-kernel-continuity"></a>

一个足够的确定性连续条件是：\(Kf\in C_c(E)\)对所有\(f\in C_c(F)\)。这时\(\mu_n\xrightarrow v\mu\)直接给\(\mu_nK\xrightarrow v\mu K\)，但仍须先保证这些输出局部有限。若K为概率核且对每个紧B⊂F，存在紧A⊂E使\(K(x,B)=0\)于x∉A，则\((\mu K)(B)\le\mu(A)\)，自动局部有限。配合K的Feller连续性便给上述充分条件。它不是任意核的性质。

在\(\mathbb R^d\)取非负连续紧支撑ρ且积分1，\(K_\varepsilon(x,dy)=\rho_\varepsilon(y-x)dy\)。若f支撑于B且ρ支撑于半径r球，ε≤1时Kεf支撑于共同紧集B加半径r球。并且\(\sup_x|K_\varepsilon f(x)-f(x)|\le\sup_{|z|\le\varepsilon r,x}|f(x+z)-f(x)|\to0\)，因为紧支撑连续函数在全空间一致连续。对任何Radon μ积分，得μKε vague→μ。

密度\(p_\varepsilon(y)=\int\rho_\varepsilon(y-x)\mu(dx)\)在每个紧y窗口有限连续：被积量只涉及共同紧x窗口，ρ一致连续，μ在该窗口有限。\((y,\mu)\mapsto p_\varepsilon(y)\)的联合可测性由上一节得到，故对随机Ξ有真正的随机连续密度。δ₀与ρεdy对单点0的质量差1，证明一般没有总变差收敛。若μ已有L¹密度，则另由L¹平移连续性可得L¹逼近，但本章不把它无条件推广到奇异测度。

## 3. 条件Poisson化的过程级构造

<a id="mass-poisson-approximation"></a>

给定随机Radon Λ，使用[T-POISSON-SPACE](t-poisson-space.md)中对评价可测强度实际建立的Poisson概率核。第8章可数核构造在扩充空间上同时生成\((\Lambda,N_1,N_2,\ldots)\)，条件于Λ取Nₙ独立、强度nΛ；无需宣称原空间已经有额外随机数。可数n和紧穷竭统一局部有限零集。定义\(\widehat\Lambda_n=N_n/n\)。

由第48章有限窗口的Poisson二阶等距，对每个实\(f\in C_c\)，条件均值Λf、条件方差Λ(f²)/n成立；条件Λ(f²)有限a.s.，其无条件期望可以无穷。对任意A,δ>0，

\[ \mathbb P\{|\widehat\Lambda_nf-\Lambda f|>\delta\}\le\mathbb P\{\Lambda(f^2)>A\}+\frac{A}{n\delta^2}. \]

先n→∞再A→∞给每个坐标依概率收敛。给ε，先选J使\(\sum_{j>J}2^{-j}<\varepsilon/2\)，再对前J坐标用并集界，即得\(d_v(\widehat\Lambda_n,\Lambda)\to0\)依概率。这是同一扩充空间上的测度收敛，比单独的边缘律收敛更强；不声称任意独立选择的副本逐实现收敛。

## 4. Cox映射的连续性与强度识别

<a id="mass-cox-map"></a>

若\(\Lambda_n\Rightarrow\Lambda\)于Radon vague空间，则条件Poisson核输出Cox(Λₙ)⇒Cox(Λ)。因为\(g=1-e^{-f}\in C_c^+\)，函数\(\lambda\mapsto e^{-\lambda g}\)有界连续，故全部输出Laplace泛函收敛。T-RANDOM-MEASURE-LIMITS（或第48章点版本）给分布收敛。这个证明不要求随机强度的均值有限。

Cox映射对指导测度的概率律还是单射。若两个Cox律相同，对任意h∈\(C_c^+\)及\(0<s<1/\|h\|_\infty\)，取\(f=-\log(1-sh)\)，得到两份随机变量Λh的Laplace变换在小区间相同。非负有限Y的Laplace变换在每个a>0有收敛Taylor展开，半径至少a：逐项绝对和被\(e^{-(a-|u|)Y}\le1\)支配，故对|u|<a可交换期望与级数。已知区间内的导数相同，选内部点a把同一展开延拓到(0,2a)，重复扩大区间，得到全部正s的相同变换。上一专题的唯一性给Λh等律，再对h的线性组合和可数族识别整份随机测度律。
