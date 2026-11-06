# T-GAUSSIAN：Hermite、Wiener chaos及Gaussian Banach平移

配套[第39章](../chapters/39-malliavin.md#noise-chaos)。H为实可分Hilbert空间，W:H→L²为23章已构造的isonormal族，E W(h)W(k)=〈h,k〉。本页L²空间只取σ(W)的完备化，不包含外加独立信息。基向量eⱼ的坐标ξⱼ=W(eⱼ)独立标准Gaussian，有限向量Gaussian唯一性用14章。

## 1. Hermite的归一化和正交性

<a id="gaussian-proof-hermite"></a>

定义概率论归一化Hₙ(x)=\((-1)^n\)e^{x²/2}(d/dx)ⁿe^{-x²/2}。对Gaussian密度反复分部积分，边界是多项式乘Gaussian，趋0，得到E[Hₙ(Z)f(Z)]=E f^{(n)}(Z)，先对多项式及光滑有界测试成立。由最高项xⁿ和次数较低项组成，故EHₙHₘ=n!1_{n=m}。生成函数可由x、t的求导递推直接验证；每个有限t区间上指数的Gaussian矩支配所有求导。

\[ e^{tx-t^2/2}=\sum_{n=0}^\infty\frac{t^n}{n!}H_n(x),\quad H_n^\prime=nH_{n-1},\quad xH_n=H_{n+1}+nH_{n-1}. \]

有限支撑多重指标α下，H_α=∏H_{αⱼ}(ξⱼ)彼此正交、平方范数α!=∏αⱼ!。Gaussian指数E_h=exp(W(h)−‖h‖²/2)的系数为h^α/α!，且这些系数的平方范数和为exp(‖h‖²)=E E_h²。于是正交部分和确在L²趋E_h，不只逐点形式展开。有限坐标指数在L²全性由33.20–21的实际Laplace/Fourier证明给出；也可先用它识别每个有限坐标条件平均再增加坐标。故所有H_α构成L²(σ(W))的完备正交族。

## 2. 从对称张量到所有随机变量

<a id="gaussian-proof-chaos"></a>

\(H^{\odot n}\)为H的n重Hilbert张量积的对称闭子空间。若|α|=n，e^{⊙α}是按α重复基向量再对n!排列取平均，其范数平方α!/n!。定义Iₙ(e^{⊙α})=H_α；正交性证明这一定义线性相容、E Iₙ(f)Iₘ(g)=1_{n=m}n!〈f,g〉，故以完备性延到全部对称张量。不使用“多重积分”名字替代构造。

\[ F=\sum_{n=0}^\infty I_n(f_n),\qquad E|F|^2=\sum_{n=0}^\infty n!\|f_n\|_{H^{\otimes n}}^2,\qquad I_0(f_0)=EF. \]

完备Hermite展开按总次数分组即给上式，L²收敛由正交Parseval，fₙ唯一。改变H的正交基不会改变Iₙ：对非零h的纯幂\(h^{\otimes n}\)，生成函数给Iₙ(\(h^{\otimes n}\))=‖h‖ⁿHₙ(W(h)/‖h‖)；纯幂由极化张成稠密的对称张量，故两种基构造一致。不同阶正交不等于独立：Z与Z²−1正交，但后者由前者决定。

## 3. 这个展开确实包含多重Itô积分

<a id="gaussian-proof-multiple"></a>

取H=L²[0,T]及W(h)=∫h dB。对确定h，33章指数E_t(zh)满足E_t=1+z∫₀ᵗE_s h_s dB_s。反复代入给有序积分；第31章等距逐层给第n阶项平方范数(∫h²)ⁿ/n!，所以幂级数在L²中、局部一致于z收敛，且代回方程。唯一性由等距/Gronwall；再与Hermite生成函数比较系数。

\[ I_n(f)=n!\int_{0<t_1<\cdots<t_n<T}f(t_1,\ldots,t_n)\,dB_{t_1}\cdots dB_{t_n},\quad f\in L^2_{\rm sym}([0,T]^n). \]

先对\(h^{\otimes n}\)成立，再用极化及等距延到任意对称f。时间对角Lebesgue为0，不需要给相等时刻人为排序。张量范数的n!与有序单纯形恰好匹配。所有积分均为先前已建的确定核迭代Itô积分，没有倒用Malliavin散度。

## 4. 导数的阶数预算与Mehler算子

<a id="gaussian-proof-number"></a>

在多项式柱函数上直接求导H_α，Parseval给如下范数。对一般\(\mathbb D^{1,2}\)变量，Gaussian分部积分把其导数每个Hermite系数确定为F的对应升阶系数；对H值空间先逐基坐标再用非负Tonelli，得到同一等式。反向若级数有限，有限chaos和的导数Cauchy，闭性给F属于\(\mathbb D^{1,2}\)。这不是只对多项式宣布公式。

\[ E\|DF\|_H^2=\sum_{n\ge1} n\,n!\|f_n\|^2,\quad E\|D^kF\|^2=\sum_{n\ge k}\frac{n!}{(n-k)!}\,n!\|f_n\|^2. \]

第二式同样逐次求导，\(\mathbb D^{k,2}\)的条件是0到k阶对应和均有限。取独立副本W′，Mehler算子对柱函数定义为把W换成\(e^{-t}\)W+√(1−\(e^{-2t}\))W′后平均。对1≤p<∞，Jensen给Lᵖ收缩，有限柱逼近给强连续；生成函数使TₜIₙ=\(e^{-nt}\)Iₙ。其L²生成元L=-N，N Iₙ=nIₙ，定义域Σn²n!‖fₙ‖²<∞。在此域δDF=NF，由分部积分及系数比较证明。t是衰减噪声坐标的参数，不是原Brownian运动的物理时间。

## 5. Gaussian Banach变量的可积性不是额外假设

<a id="gaussian-proof-fernique"></a>

设B可分Banach，X为中心Radon Gaussian变量。用单位球面稠密序列及Hahn–Banach取可数范数化泛函ℓⱼ，‖x‖=supⱼ|ℓⱼ(x)|；带可数正边距的闭球交表示及B可分性给σ(ℓⱼ)=Borel(B)。因此有限线性读数足以识别概率律。X,Y独立同律时，(X+Y)/√2与(X−Y)/√2独立同律于X，由所有有限读数的Gaussian特征函数及上述唯一性证明。

\[ p(t)=P(\|X\|>t),\quad a=P(\|X\|\le r)>0,\quad a\,p(\sqrt2t+r)\le p(t)^2. \]

因为‖X‖>√2t+r而‖Y‖≤r会使两个旋转后的范数都>t。取t₀使p(t₀)<a，令tₙ₊₁=√2tₙ+r，则p(tₙ)/a≤(p(t₀)/a)^{2ⁿ}，而tₙ≤C2^{n/2}。在相邻tₙ之间比较得到p(t)≤C₁exp(−c₁t²)。尾积分遂给某η>0的Eexp(η‖X‖²)<∞，特别X有所有范数矩。有限维Gaussian旋转与初等尾估计实际完成这里需要的Fernique版本。

## 6. 把Cameron–Martin方向从路径空间中抽出来

<a id="gaussian-proof-banach"></a>

令H为闭包span{ℓ(X):ℓ∈B*}⊂L²，W(h)=h。它可分：若H中变量与上述全部ℓⱼ(X)正交，则Gaussian独立性使它与σ(X)独立；它自身又对σ(X)可测，只能为0。因此可数线性读数的张成已稠密。定义i(h)=E[XW(h)]为Bochner积分；上一节矩界与Cauchy–Schwarz保证存在、连续：可先把X按B的可数网格量化为L²收敛的简单变量，有限和E[XₙW(h)]在B内Cauchy，其极限定义此积分，且ℓ(i(h))=〈ℓ(X),h〉。若i(h)=0，稠密性给h=0，所以i嵌入H到B。

\[ \frac{d\mu_{i(h)}}{d\mu}(x)=\exp\!\left(W(h)(x)-\frac12\|h\|_H^2\right),\quad \mu_{i(h)}=\mathcal L(X+i(h)),\qquad b\notin i(H)\Longrightarrow\mu_b\perp\mu. \]

充分性：右侧平均1且严格正。对任意有限线性读数做Gaussian完成平方，权重把均值移为ℓ(i(h))，协方差不变；Borel唯一性识别平移概率律。W(h)以L²极限取可测版本，等价测度保证零集版本无影响。没有把W(h)说成每个x上的有界连续线性泛函。

必要性：在span{ℓ(X)}上尝试定义L_b(ℓ(X))=ℓ(b)。若不良定义，某零方差读数在平移后成为非零常数，直接分离两律。若良定义且有界，Hilbert Riesz给h，所有ℓ满足ℓ(b)=〈ℓ(X),h〉=ℓ(i(h))，故b=i(h)。否则L_b无界，选有限线性读数gⱼ、‖gⱼ‖₂=1、L_b(gⱼ)≥2ʲ。Chebyshev与第一Borel–Cantelli给gⱼ(X)/L_b(gⱼ)→0，而在X+b下同一读数趋1，两个Borel极限事件分离两律。这完成Banach平移的必要充分结论，不声称已做协方差改变的全部Gaussian测度等价理论。

第4节的导数闭性来自[T-MALLIAVIN](t-malliavin.md#malliavin-proof-closed)的独立Gaussian分部积分证明，后者不使用chaos，故无循环。[回正文](../chapters/39-malliavin.md#noise-banach)。
