# T-MANIFOLD-DIFFUSIONS：从坐标方程到真正的流形扩散

配套[第40章](../chapters/40-stochastic-geometry.md#geometry-patching)，先用[T-GEOMETRY](t-geometry.md)的实际几何工具。滤过通常；本页半鞅均连续，定义与等式在最大寿命前成立。除给定嵌入的一节外，不假设M嵌入某个欧氏空间。

## 1. 一般连续驱动的局部存在不能留作黑箱

<a id="manifold-proof-clock"></a>

给定Rᵐ连续半鞅Z=M+A，M₀=0为连续局部鞅，A局部有限变差；常数初值可计入A，确定dt项则并入一个Z⁰=t分量。取光滑向量场Vᵢ。Stratonovich方程先解释成下述Itô方程，而不是在未知解上预设一个积分。32章公式随后证明两种写法相同。坐标内以光滑截断把V及一、二阶导数变为有界，于是V和DVᵢVⱼ全局Lipschitz。

\[ dY^a=V_i^a(Y)\,dZ^i+\frac12\partial_bV_i^a(Y)V_j^b(Y)\,d[M^j,M^i],\qquad C_t=t+\sum_i\operatorname{Var}(A^i)_t+\sum_i[M^i]_t. \]

协变差矩阵测度为正半定：对有理向量的二次变差递增，再取可数公共零集，给各分量相对于迹测度的正半定密度。因此交叉项的总变差不超过相应两对角之和的一半，所有有限变差项受C控制。先停至C≤N并固定有限T，使M的停止增量平方可积；这由31章括号等距、局部化和Fatou得到。

把时间分成C每增加δ的一段。对Picard映射Γ，31章向量积分等距、Doob最大不等式及有限变差积分的Cauchy–Schwarz给下面的收缩估计；K只依截断后系数和维数，不依时段。选δ使右侧系数小于1。连续适应过程的最大L²空间完备，故逐段得到解。C≤N时至多需要⌈N/δ⌉+1段。一般有限初值先按其幅度局部化，按35章同初值事件上的唯一性拼接；再放开N、T与状态截断。

\[ E\sup|\Gamma(Y)-\Gamma(\widetilde Y)|^2\le K(\delta+\delta^2)E\sup|Y-\widetilde Y|^2. \]

同一估计给路径唯一性；有界截断解与更大截断解在共同退出前一致。所有积分极限在停止后的最大L²中成立，放开停止后为ucp，连续版本使方程不可分辨。最后对光滑Vᵢ(Y)用32章，得其与Z的协变差正好是Itô式中的修正，从而确实解原Stratonovich方程。本证明不循环使用本页后面的流形构造。

## 2. 测试函数定义与坐标定义相同

<a id="manifold-proof-coordinates"></a>

连续适应M值X为流形半鞅，是指每个全局光滑实函数f的f(X)在寿命前局部为连续实半鞅；等价地可只测紧支撑光滑函数。证明后一等价：紧区域上用等于1的截断把f变成紧支撑函数，再沿紧区域耗尽。坐标函数本非全局函数，但在较小图域用截断延拓，故坐标过程在离开该域前也是半鞅。反向对坐标用32章Itô公式，给任何f(X)的局部分解。可数图域使拼合和零集统一合法。

\[ dy^a(X)=\partial_i y^a(X)\,dx^i(X)+\frac12\partial_{ij}y^a(X)\,d[x^i(X),x^j(X)]. \]

这已经证明Itô描述具有正确的坐标相容性。Stratonovich只是把同一个身份写成普通链式形式，不是修复一个“不一致的Itô理论”。对连续半鞅A、B、Z，乘积公式及31章积分括号给下述结合律；有限变差项没有额外括号。先在停止能量有界时计算，随后局部化，便证明所有坐标一形式积分的相容性。

\[ Y=\int B\circ dZ\quad\Longrightarrow\quad \int A\circ dY=\int AB\circ dZ,\qquad [AB,Z]=\int A\,d[B,Z]+\int B\,d[A,Z]. \]

具体地，左式展开为∫AB dZ+½∫A d[B,Z]+½∫B d[A,Z]，正好等于右式。对分量求和即给向量版本。因此αᵢ(X)∘dxⁱ在图变换下保持同一积分；定义在相邻停止区间上相加即可，不要求全局坐标。

## 3. 拼接、可测性与真正的寿命

<a id="manifold-proof-patching"></a>

对光滑全局V₁,…,Vₘ及给定连续半鞅Z，在T-GEOMETRY的局部有限Pⱼ⊂⊂Qⱼ中，从含当前点的最小编号Pⱼ开始，用第1节欧氏解直到离开Qⱼ。下一个初值属于停止σ-代数；同一随机时段上的Picard仍适应，不需假定Z有独立增量。第2节链式法则与路径唯一性使重叠图中两份解相同。图域的最小编号选择Borel，可数停止及Picard极限保证全部过程可测。对初值与驱动的联合变量，用全部Picard序列的收敛事件并在失败处给固定默认值，得到Borel解映射；不需要捏造对所有初值同时成立的公共概率零集。

不能仅说“不断换图就完成了”。若换图时间累积在有限S且过程留在紧K内，取T-GEOMETRY的有限分离函数F。每个分量满足同一Stratonovich方程的测试身份；在K上所有系数有界。停至C≤N后，鞅积分与有限变差积分都连续延到S，所以F(X)有极限。紧性及F的连续逆给X极限。有限个与K相交的图有统一正的分离距离：从闭Pⱼ到M\Qⱼ。每次换图都跨越这段距离，但F(X)的连续延拓有一致连续性，故不可能无限次发生。

有限最大寿命ζ还必须意味着最终离开每个紧集，而不只“没有统一有界坐标”。若靠近ζ仍反复访问某紧K，取全局紧支撑f等于1于K。Vᵢf和VⱼVᵢf全球有界，所以f(X)的积分表示连续延到ζ；访问K的子列使极限为1。于是X最终留在{f≥1/2}这个紧集，前段论证又可延长，矛盾。对可数紧耗尽统一即可。因此没有人为内点杀死的最大解，寿命确为紧集退出时刻之极限。

欧氏局部唯一性再证明全局路径唯一性：在首个共同图域比较，依次到下一停止时刻；若有有限分离时间，在其前紧区域上会违反局部唯一性。对Brownian驱动和确定光滑场，Picard与图拼接给初值和驱动的可测解函数，Brownian在停止时刻后的专用强Markov性给最大解的强Markov性。一般半鞅驱动没有这个附加结论。

## 4. 二阶算子、联络漂移与局部概率律

<a id="manifold-proof-generator"></a>

\[ A f=b^i\partial_i f+\frac12a^{ij}\partial_{ij}f,\quad a'^{ab}=\partial_i y^a\,a^{ij}\partial_jy^b,\quad b'^a=\partial_i y^a b^i+\frac12a^{ij}\partial_{ij}y^a. \]

对V₀dt及Brownian向量场Vα的Stratonovich方程，32章给A=V₀+½ΣVα²。上式由Itô应用于新坐标与任意测试f得到。a也可从A(fh)−fAh−hAf识别，所以是非负的对称二阶张量；b单独不是向量。T-GEOMETRY的Γ变换式与逆坐标二阶求导相消，给下面真正的向量β。

\[ \beta^k=b^k+\frac12\Gamma^k_{ij}a^{ij},\qquad Af=\beta(f)+\frac12a^{ij}(\operatorname{Hess}f)_{ij},\qquad \beta=V_0+\frac12\sum_\alpha\nabla_{V_\alpha}V_\alpha. \]

还要证明生成元在这里确实识别概率律。设a在图内光滑正定，b光滑，X为无额外杀死的最大连续过程，使f(X)−∫Af为局部鞅。先用截断坐标及其乘积作测试，32章乘积式给Mⁱ=xⁱ(X)−∫bⁱ、[Mⁱ,Mʲ]=∫aⁱʲ。局部Gram–Schmidt或Cholesky给光滑可逆σ、σσᵀ=a，于是W=∫σ⁻¹dM有单位时间括号。停止出图后加独立Brownian增量，33章Lévy刻画证明这是真正Brownian运动，不只是一个形式符号。

所以X在此停止区间满足欧氏SDE。35章Picard构造和路径唯一性在任一这样的弱实现上把它识别为同一驱动的解函数，给停止律唯一。按第3节可数图域拼合，得到最大律唯一。这里使用光滑严格椭圆的局部范围；不能由一个形式算子就宣布一般退化或任意边界版本唯一。

## 5. 圆与球面的可计算核验

<a id="manifold-proof-sphere"></a>

\[ Y=\tan(B/2):\quad dY=\frac{1+Y^2}{2}\,dB+\frac{Y(1+Y^2)}4\,dt,\qquad Z=-1/Y:\quad dZ=\frac{1+Z^2}{2}\,dB+\frac{Z(1+Z^2)}4\,dt. \]

这两式在各自角度图的停止区间成立。对−1/y用Itô，二阶项精确把新漂移化成z(1+z²)/4。Brownian退出(−π,π)有限，但e^{iB}全球存在；坐标极点不是路径爆炸。圆的此图度量为4(1+y²)⁻²dy²，T-GEOMETRY的Δ公式逐项给这份方程的生成元Δ/2。

\[ P(x)=I-xx^{\mathsf T},\qquad dX=P(X)\,dW-\frac n2X\,dt,\quad X_0\in S^n\subset\mathbb R^{n+1}. \]

固定球面初值x，先用35章局部光滑系数构造这个环境方程。令R=|X|²。32章给dR=2(1−R)X·dW+(R−1)(R−n−1)dt。停至|X|≤K，R−1的平方期望由Gronwall为0，所以R≡1；放开停止，路径在紧球面而不爆炸。这一步没有预先假定球面不变。

在球面上Vα=Peα，直接微分得ΣDVαVα=−nx，故上述方程等价于dX=P(X)∘dW。若漏掉法向漂移，Itô给d|X|²在球面上的漂移为n，约束就被破坏。对圆的n=1情形，均值分量满足E Xₜ=\(e^{-t/2}\)X₀；一般球面为\(e^{-nt/2}\)X₀。这是由路径方程和有界鞅期望实际推出的读数，不等于已经证明全部长期混合理论。

## 6. 给定等距嵌入的等价，以及旋转标架的反例

<a id="manifold-proof-embedding"></a>

设i:(M,g)→Rᴺ为给定的光滑等距嵌入，Pₓ为环境正交投影到TₓM，Vα=Pₓeα。它们是全局光滑切场；第3节实际构造dX=ΣVα∘dW直到M的最大寿命。对f∈C∞(M)，取第5节T-GEOMETRY的局部环境延拓。投影导数满足P(DP)P=0，由对P²=P求导并左右乘P得到。

在一个点把环境基正交旋转成切向和法向：法向对应的Vα在该点为0，切向项∇ᵥV的切分量由P(DP)P为0。因此Σ∇Vα Vα=0，且ΣVα⊗Vα=g⁻¹。Hessian分解给ΣVα²f=Δg f。第4节椭圆律唯一性遂把它与水平标架构造的Brownian律识别；这不是从外观相似推出等价。非闭、非proper嵌入时必须仍用M中紧退出寿命，不能用环境坐标有界代替。

\[ E_1=(\cos x,\sin x),\quad E_2=(-\sin x,\cos x)\quad\hbox{on }\mathbb R^2,\qquad \sum_i\nabla_{E_i}E_i=(0,1). \]

最后直接求导此旋转正交标架：∇E₁E₁=cos x E₂，∇E₂E₂=sin x E₁，和为(0,1)。所以朴素Stratonovich方程ΣEᵢ∘dWⁱ的生成元为½Δ+½∂ᵧ，并不是标准平面Brownian；减去½(0,1)dt才正确。Stratonovich使向量场方程坐标相容，但并不让任意正交标架自动生成同一度量Brownian。[回正文](../chapters/40-stochastic-geometry.md#geometry-frame-choice)。
