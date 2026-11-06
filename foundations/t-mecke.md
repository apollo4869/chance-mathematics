# T-MECKE：Poisson识别、Cox偏置与簇Palm计算

返回[第50章](../chapters/50-palm-gibbs.md#palm-mecke)。使用T-PALM的单次删除与联合可测性。Poisson部分允许强度原子和重数；级数与σ有限拼接的身份也适用于标准Borel父空间；将输出视为局部有限Radon对象时取LCSC度量及局部有限强度。Cox与簇的Palm概率另要求其平均强度σ有限。

## 1. 有限强度的逐个出现计算

<a id="mecke-finite"></a>

先令μ(E)=a<∞，a=0两边均0。第48章构造N=Σᵢ≤KδZi，K为Poisson(a)，Zi iid μ/a。对非负可测g，由标签对称、Tonelli及\(k/k!=1/(k-1)!\)，有

\[ \mathbb E\sum_{i=1}^Kg(Z_i,N-\delta_{Z_i})=e^{-a}\sum_{k\ge1}\frac{a^k}{k!}k\int g(x,\eta)\frac{\mu(dx)}a\,\mathcal L\!\left(\sum_{j=1}^{k-1}\delta_{Z_j}\right)(d\eta)=\int\mathbb E g(x,N)\mu(dx). \]

重合位置的两个标签仍是两次出现，去掉i只去掉它自己，故公式同样适用于有原子μ。这一步不是先对“x有一点”作条件化；它直接比较完整Poisson级数中的相邻项。

## 2. σ有限拼接与完整Mecke身份

<a id="mecke-sigma"></a>

将E分成μ有限的不交Dⱼ。N在Dⱼ及其补集的限制独立；固定补集配置，以有限强度公式处理Dⱼ内求和，g可以依赖整个配置。再对独立补集积分，得到\(\mathbb E\int_{D_j}g(x,N-\delta_x)N(dx)=\int_{D_j}\mathbb E g(x,N)\mu(dx)\)。对j求和用Tonelli，给全部非负g的Mecke公式。等价非约化形式由替换g(x,η)=f(x,η+δₓ)得到。

\[ \mathbb E\int g(x,N-\delta_x)N(dx)=\int\mathbb E g(x,N)\mu(dx),\qquad \mathbb E\int f(x,N)N(dx)=\int\mathbb E f(x,N+\delta_x)\mu(dx). \]

把g换成依次删除后依赖余下配置的非负测试，重复单点身份r次，便得r个不同出现的阶乘Mecke公式。每次删除后下一次只遍历剩余出现，恰对应有序且不重复的标签；允许空间坐标重合。每次积分都是非负，可用Tonelli调换。有限r归纳因此不需要把空间对角删除；对有原子强度，删除对角反而会给错结果。

## 3. 身份为什么反过来识别Poisson

<a id="mecke-characterization"></a>

设Ξ为局部有限点过程，满足上面的约化身份，右侧为固定Radon μ。先取g(x,η)=h(x)，得到平均μ。对\(f\in C_c^+\)有EΞf=μf<∞。令\(L(t)=\mathbb E e^{-t\Xi f}\)，支配差商由Ξf控制，故在t≥0可求右导数、t>0可求导。取\(g(x,\eta)=f(x)e^{-tf(x)}e^{-t\eta f}\)，Mecke身份变成

\[ -L^{\prime}(t)=L(t)\mu(fe^{-tf}),\qquad L(0)=1,\qquad L(t)=\exp\{-\mu(1-e^{-tf})\}. \]

线性常微分方程可用积分因子直接求解，无须预设L不为0。t=1给Poisson泛函，49章唯一性给Ξ等律PRM(μ)。反过来已在前两节证明。因此这不只是Poisson的一个矩恒等式，而是整份概率律的刻画。T-PALM结合它给非约化Palm律N+δₓ、约化Palm律N；在平稳有限强度下，P⁰=Law(N+δ₀)也反向刻画齐次Poisson，由平稳Campbell将它还原为Mecke身份。

## 4. Cox环境怎样被重新加权

<a id="mecke-cox"></a>

设N给定随机Radon Λ为PRM(Λ)，ν=EΛσ有限。T-PALM对质量Λ及环境标记Λ析取，记指导测度的Palm核为Rₓ(dλ)。对Λ逐条件使用Mecke，再用塔式法则与该析取，得到

\[ \mathbb E\int g(x,N-\delta_x)N(dx)=\int\nu(dx)\int R_x(d\lambda)\int g(x,\eta)\operatorname{PRM}(\lambda)(d\eta). \]

所以约化Palm是对重新加权的强度核作Cox混合，完整Palm另加一次δₓ。不是把原指导测度律直接沿用。全部身份先对非负联合测试成立；核的共同ν零集由可数生成类统一，不要求给每个x的不可测任意版本。

特别地Λ=Zμ，0<EZ<∞，则Rₓ中Z的律为\(P^*(dz)=zP_Z(dz)/\mathbb EZ\)，于μ-a.e. x。取Z以相同概率为1和3，得到P*(Z=3)=3/4。若EZ²有限，E*Z=EZ²/EZ；若无穷则该期望无穷。对有界递增a，\(\operatorname{Cov}(Z,a(Z))=\frac12\mathbb E[(Z-Z^{\prime})(a(Z)-a(Z^{\prime}))]\ge0\)，说明典型事件偏向高强度不是一句比喻。EZ=∞时，Zdx的平稳强度无穷，不能使用有限λ的Palm概率归一化。

## 5. 一个典型子点怎样选中整簇

<a id="mecke-clusters"></a>

设Poisson父标记(x,ζ)强度a(dx)Q(x,dζ)，ζ为局部有限点测度，Ψ=Σζᵢ局部有限a.s.；另假设\(\nu(A)=\int a(dx)\int\zeta(A)Q(x,d\zeta)\)σ有限。49章局部质量判据建立构造，但这里的平均σ有限是额外条件。把对子点的求和先按父出现分组，再对父PRM用Mecke，得到

\[ \mathbb E\int g(u,\Psi-\delta_u)\Psi(du)=\int a(dx)\int Q(x,d\zeta)\int\zeta(du)\,\mathbb E g(u,\Psi+\zeta-\delta_u). \]

右侧Ψ是独立、同律的背景簇过程；Poisson加点只恢复被选父的完整子簇。对联合测度a(dx)Q(x,dζ)ζ(du)沿u作T-PALM同样的有限加权析取，便得到选中簇与父位置的核。该核与独立背景相加、再删去一次δᵤ，就是约化Palm。这一论证没有要求父位置局部有限，只要求父强度σ有限与输出条件成立。

平稳平移簇的专用版本取父强度κdy，独立有限形状ζ，K=ζ(E)，0<EK<∞，以父位置平移形状。Tonelli给ν=κEK du，保证局部有限。变换u=y+v后，上式说明完整P⁰为独立背景Ψ加\(\theta_V\zeta^*\)，其中\(Q^*(d\zeta)=KQ(d\zeta)/EK\)，V给定ζ*在其K次出现中均匀选择。约化版本再删δ₀。若每簇为Kδ₀、P(K=1)=P(K=2)=1/2，则根处重数为1、2的Palm权重是1/3、2/3；背景在0无点，由有限弥散平均强度保证。
