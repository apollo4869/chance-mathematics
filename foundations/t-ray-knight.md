# T-RAY-KNIGHT：用可核算的Laplace读数识别空间过程

配套[第37章](../chapters/37-local-time.md#local-spatial-profile)。本页证明标准实Brownian的两条经典Ray–Knight定理：首达a>0，以及零点局部时的右逆τℓ。L采用Tanaka中的对称归一化；BESQδ采用dZ=δdx+2√Z dβ。一般扩散或图上过程的Ray–Knight推广不在此自动获得。

## 1. 平方Bessel过程先实际存在

<a id="ray-proof-besq"></a>

仅需δ=0、2及在确定空间位置从2切到0。将σ(z)=2√(z⁺)延至实线，b=δ。连续、线性增长，35章Euler紧性与Brownian重构给弱解；|σ(x)−σ(y)|≤2√|x−y|满足该章模唯一性条件，故路径唯一，并由其已证Yamada–Watanabe构造得到强解。此处没有从Ray–Knight倒推出BESQ存在。

非负性也须核验。右局部时在0的带宽公式给Lₜ^{0,+}≤4∫₀ᵗ\(\mathbf1_{\{0<Z_s<\varepsilon\}}\)ds→0；左侧带的括号为0。负部Tanaka于是给Z⁻≤−δ∫\(\mathbf1_{\{Z<0\}}\)ds≤0。停止于首次Z=K，E Zₜ∧τK=z+δE(t∧τK)，所以有限T的爆炸概率≤(z+δT)/K，趋0。Fatou先给EZₜ≤z+δt，故E∫₀ᵀ4Zₛds有限，随机积分是真鞅，进而EZₜ=z+δt。δ=0一到0后保持0，由路径唯一性；δ=2也可由两个独立Brownian坐标的平方和核验。

\[ dZ_x=\delta(x)dx+2\sqrt{Z_x}\,d\beta_x,\quad Z_0=z\ge0,\qquad \delta(x)=0\ \text{or}\ \delta(x)=2\mathbf1_{[0,a]}(x). \]

## 2. Riccati方程为什么出现

<a id="ray-proof-laplace"></a>

取φ≥0连续、支撑于[0,R]，可先让R大于其支撑。由终端值v(R)=1、v′(R)=0向左解v″=2φv，得到v>0、v′≤0；例如反向Volterra迭代每项非负，导数符号随积分式直接得出。把v除以v(0)，并在R以后延为常数。令u=−v′/(2v)，则u≥0、有界，满足下式。它把二阶线性方程改写成平方噪声恰能抵消的非线性读数。

\[ u^\prime=2u^2-\varphi,\qquad u(R)=0,\qquad v(x)=\exp\!\left(-2\int_0^xu(y)dy\right). \]

对BESQ，取F(x,z)=exp[−zu(x)−∫ₓᴿδ(y)u(y)dy]。在δ分段处分别使用Itô，再以连续性拼合。对\(\exp(-\int_0^x\varphi(s)Z_s\,ds)\)F(x,Zx)，dx系数为z(−u′+2u²−φ)及相消的δu−δu，恰为0。过程介于0与1，先停止再DCT即为真鞅，无需总体高阶矩。x=R时F=1，给下式。

\[ E_z\exp\!\left(-\int_0^R\varphi(x)Z_xdx\right)=\exp\!\left[-zu(0)-\int_0^R\delta(x)u(x)dx\right]. \]

这些读数确定非负连续空间过程的律。用连续窄帽逼近有限个坐标的Dirac质量，路径连续性使∫φZ趋于坐标的非负线性组合；指数有界，DCT保留期望。多元Laplace唯一性逐坐标使用13章结果，得到全部有限维律；C空间由有理坐标生成Borel，故过程律相等。

## 3. 首达时刻的第一Ray–Knight定理

<a id="ray-proof-first"></a>

令Tₐ=inf{t:Bₜ=a}，a>0、B₀=0。定义Zx=\(L_{T_a}^{a-x}\)，x≥0；联合连续性使它是连续非负空间过程，Z₀=0，因为此前尚未到a。取R>a及φ如上，利用普通时间占用，把其Laplace读数写成Brownian到a以前的加权时间。

\[ E_0e^{-\int_0^R\varphi(x)L_{T_a}^{a-x}dx}=E_0\exp\!\left[-\int_0^{T_a}\varphi(a-B_s)ds\right]=v(a). \]

最后一个等式不偷用38章一般Feynman–Kac：在y≤a设h(y)=v(a−y)，0<h≤1、h(a)=1、½h″=φ(a−y)h。Itô乘上对应指数后停止于Tₐ、首达−n及固定时间T，漂移为0、过程有界。Brownian首达a有限；n、T趋∞时，误差由P₀(τ_{−n}<Tₐ)=a/(a+n)及P(Tₐ>T)控制，都趋0，DCT给期望h(0)=v(a)。

由v(a)=exp[−2∫₀ᵃu]，正好等于上一节z=0、δ=2直到a而后为0的BESQ读数。因而Z在[0,a]为BESQ2，从0开始；在a以后的空间增量，条件于Za，按BESQ0继续，且可用独立Brownian驱动。这里的条件Markov结构由整条空间过程的律识别给出，不是从平均曲线推断。

\[ E L_{T_a}^{a-x}=2\min(x,a),\qquad x\ge0. \]

期望式由BESQ停止取均值，或36章单边Green直接得到，两条路线核对因子2。Brownian随机时间Tₐ无穷期望，与其每条路径有限不冲突。

## 4. 逆局部时的第二Ray–Knight定理

<a id="ray-proof-second"></a>

固定ℓ>0。τℓ以前的正、负游程为独立PRM，正侧强度dl n(de)/2。令\(A_\varphi(e)=\int_0^{\zeta(e)}\varphi(e_s)\,ds\)。零集没有普通时间，故∫φ(x)\(L_{\tau_\ell}^x\) dx为正游程收益之和。对Poisson泛函，

\[ Ee^{-\int_0^\infty\varphi(x)L_{\tau_\ell}^xdx}=\exp\left[-\frac\ell2n(1-e^{-A_\varphi})\right]. \]

仍取上面的v。由相同停止Itô，v(ε)=Eε exp[−\(\int_0^{\tau_0}\)φ(B_s)ds]。将n限制在达ε游程，在首达ε以后使用强Markov，初段收益误差至多||φ||∞n[ρ;H≥ε]≤||φ||∞ε。小高度游程的完整收益误差可用占用入口律估计：nAφ=∫φ(y)∫₀∞kₜ(y)dt dy=2∫φ(y)dy有限；故对H<ε由DCT趋0。于是

\[ n(1-e^{-A_\varphi})=\lim_{\varepsilon\downarrow0}\frac{1-v(\varepsilon)}\varepsilon=-v^\prime(0)=2u(0). \]

注意k在时间上的积分为2，而不是1；它正对应本书按Brownian对称L标号的n。代回Poisson指数得到exp[−ℓu(0)]，与z=ℓ的BESQ0完全相同。因此正侧空间场(\(L_{\tau_\ell}^x\),x≥0)为BESQ0从ℓ开始；负侧(\(L_{\tau_\ell}^{-x}\),x≥0)为独立同分布副本。L在0等于ℓ，符合两侧共同的确定初值。

## 5. 临界分枝结构与适用边界

<a id="ray-proof-boundary"></a>

对BESQ0另取终值Laplace读数，以u(x)=q/(1+2q(t−x))重复有界指数鞅计算，得下面的转移变换。乘法性表明初值z₁+z₂的过程律等于两份独立初值过程之和的律，过程级由相同转移核与Markov构造确认。q→∞给零点概率，吸收性再给有限空间距离内灭绝几乎必然。

\[ E_ze^{-qZ_t}=\exp\!\left(-\frac{zq}{1+2qt}\right),\qquad P_z(Z_t=0)=e^{-z/(2t)},\qquad EZ_t=z\quad(t>0,q\ge0,z\ge0). \]

因此Brownian的局部时剖面带有连续状态临界分枝结构，而不是仅与家族树形状相像。每条剖面最终为0，却在每个有限空间位置仍有相同期望，说明该空间参数鞅不一致可积；这里的新内容是实际分枝转移规律，不重复20章脊柱证明。没有把这两个停止版本推广到确定时刻的任意局部时场，更未证明所有Lévy高度过程的Ray–Knight。返回[第37章](../chapters/37-local-time.md#local-ray-knight)。
