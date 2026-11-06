# T-PALM：Campbell测度与Palm核的实际构造

返回[第50章](../chapters/50-palm-gibbs.md#palm-disintegration)。E为LCSC度量空间，\(\Xi\)为非负随机Radon测度，Z为标准Borel空间S中的环境标记。可以取Z=Ξ，但不假定原概率空间本身标准Borel。使用第10章概率核析取、T-MASS-KERNELS联合积分与T-RADON-SPACE评价域。

## 1. 先构造一份联合测度

<a id="palm-campbell-construction"></a>

对非负联合可测g定义\(Cg=\mathbb E\int g(x,Z)\Xi(dx)\)。T-MASS-KERNELS先在有限紧窗口上对矩形用单调类，保证此积分是随机变量；MCT给g的可数可加性。因此C是E×S上的测度，不需要先有Palm核。其第一边缘\(\nu(A)=\mathbb E\Xi(A)\)。若νσ有限，取不交Aⱼ覆盖E、ν(Aⱼ)<∞，便有C(Aⱼ×S)<∞，所以Cσ有限。

边缘σ有限不能由样本局部有限代替。例如Ξ=Zdx于实线，Z有限a.s.而EZ=∞，则ν在每个正长度集上都无穷，不是σ有限；但完整Campbell测度仍可在紧窗口与{Z≤n}上σ有限。联合测度σ有限不自动保证边缘σ有限，也不自动允许相对于边缘的概率核析取。以下存在定理明确假设νσ有限。

## 2. 有限加权以后析取，再去掉权重

<a id="palm-kernel-construction"></a>

若ν非零σ有限，取处处正有限w，使\(0<c=\nu w<\infty\)：在上述Aⱼ上取\(w=2^{-j}/(1+\nu A_j)\)。令\(\widetilde C(dx,dz)=w(x)C(dx,dz)/c\)，它是概率，第一边缘为wν/c。第10章给概率核Qₓ，使\(\widetilde C=(w\nu/c)Q\)。对非负g，先将g乘c/w，再用MCT，得到

\[ \mathbb E\int g(x,Z)\Xi(dx)=\int_E\int_Sg(x,z)Q_x(dz)\nu(dx). \]

这就是环境Z的Palm概率核。ν=0时Ξ=0 a.s.：对可数紧穷竭每个质量期望0，再统一零集；此时核任取固定概率，身份无内容。若两份核满足上式，在每个有限ν片上比较事件积分，对S的可数生成π类合并例外零集，再用概率唯一性扩展到全部Borel事件。故有一个共同ν零集以外，两份核作为整份概率相同。不能将这一版本结论改成每个x都唯一。

## 3. 一次出现怎样被合法删除

<a id="palm-delete-one"></a>

现在Ξ为整数点测度，S取\(\mathcal M_p(E)\)，Z=Ξ。加点\((x,\eta)\mapsto\eta+\delta_x\)由评价可测。删除只定义在\(D=\{(x,\eta):\eta\{x\}\ge1\}\)。取第48章的相容proper度量，\(\eta\{x\}=\lim_n\eta(B(x,1/n))\)；联合核积分使D可测。其上各紧窗口评价为\(\eta(A)-\mathbf1_A(x)\)，从而删除映射可测；全空间评价的∞−1约定为∞，D外统一定义零配置。

Campbell测度集中D，因为每个实现的每次出现确实在自己的位置。用可数有限ν片及析取，得到\(Q_x\{\eta:\eta\{x\}\ge1\}=1\)于ν-a.e. x；这个依赖x的事件仍由联合可测性合法积分。定义约化Palm核\(Q_x^!=Q_x\circ(\eta\mapsto\eta-\delta_x)^{-1}\)，异常x统一固定版本。于是\(C^!(dx,d\eta)=\nu(dx)Q_x^!(d\eta)\)，且

\[ \mathbb E\int g(x,\Xi-\delta_x)\Xi(dx)=\int_E Q_x^!g(x,\cdot)\,\nu(dx). \]

若η在x有重数k，删除后仍有k−1。将η限制到E∖{x}会删去全部k份，是另一个运算。一般随机质量的Palm核仍由上一节构造，但不能没有整数出现结构就删除一个单位。

## 4. 平移、平稳与一份真正的Palm分布

<a id="palm-stationary"></a>

在\(\mathbb R^d\)令\(\theta_x\eta(A)=\eta(A+x)\)。对\(f\in C_c\)，\((\theta_x\eta)f=\int f(y-x)\eta(dy)\)。若xₙ→x、ηₙ vague→η，所有f(·−xₙ)支撑在共同紧集且一致趋f(·−x)；局部质量界给积分收敛。因此平移作用联合连续，当然联合可测。

设Ξ平稳、\(\nu=\lambda dx\)、\(0<\lambda<\infty\)，定义中心化Campbell\(C^0g=\mathbb E\int g(x,\theta_x\Xi)\Xi(dx)\)。对固定环境事件D，\(A\mapsto C^0(A\times D)\)由平稳性平移不变，且≤λ|A|，所以由45章Haar唯一性等于常数倍dx。取任意0<|B|<∞的有界Borel窗口，\(P^0(D)=C^0(B\times D)/(\lambda|B|)\)是概率，且与B无关。矩形π–λ与MCT给

\[ \mathbb E\int g(x,\theta_x\Xi)\Xi(dx)=\lambda\int_{\mathbb R^d}\int g(x,\eta)P^0(d\eta)\,dx. \]

这也给非中心化核\(Q_x=\mathcal L(\theta_{-x}\eta),\ \eta\sim P^0\)，是一个对全部x定义的可测版本。点过程的P⁰满足η{0}≥1 a.s.；若原过程简单，则η{0}=1。对一般随机质量，P⁰不必在0有原子，例如确定长度测度的P⁰仍是长度测度。有限正强度是概率归一化条件；λ=0时过程空，λ=∞时此公式不能直接归一成概率。
