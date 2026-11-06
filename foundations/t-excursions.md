# T-EXCURSIONS：从阈值再生证明游程的Poisson性

配套[第37章](../chapters/37-local-time.md#local-excursion-clock)。B从0出发，L为T-LOCAL-TIME的对称Brownian局部时；R=|B|，不是把R在0的右局部时误记成L。n在本页始终表示R的正游程强度，按L标号；带正负号的B游程各占n的一半。前置是26强Markov/反射、21指数更新、27最小PRM与本章已经构造的L。

## 1. 路径切片、标号与可测性

<a id="excursion-proof-space"></a>

E是有限寿命ζ>0的连续非负路径：e(0)=0，在(0,ζ)严格正，在[ζ,∞)为0。取C_loc×(0,∞)中的(e,ζ)编码。零终值条件、ζ以后的零值及每个内部有理紧区间上最小值严格正，都可用可数坐标及连续性表达，故这是Borel集合，亦为标准Borel空间；ζ由路径唯一决定。高度H=sup e可测。

零集的补集为可数不交开区间(g,d)。可按其中最先出现的有理数枚举；两端是该有理点左右最近零，均为路径的Borel泛函。令e(t)=R(g+t)直到d−g，随后置0，标号ℓ=\(L_g\)=\(L_d\)。不能对g直接调用强Markov，因为最后离开0一般不是停止时刻。

两个不同游程的标号不同。证明L的支撑恰为零集：任意有理p<q，若(p,q)含零，首个p以后的零是停止时刻；在它与q之间，强Markov及T-LOCAL-TIME的Skorokhod表示使L严格增加几乎必然。对全部有理区间取并即可。因此逆局部时的非零跳跃与全部游程一一对应，零集普通时间为0又给出τℓ等于此前游程寿命之和。

## 2. 先证明一份有限强度的标记Poisson过程

<a id="excursion-proof-poisson"></a>

固定ε>0。先等Hε=inf{t:|Bₜ|=ε}，再等Dε=inf{t≥Hε:Bₜ=0}，以后从Dε重启。它们都是有限停止时刻。每轮保留包含Hε的完整游程，其高度≥ε；其它游程丢弃。由对称性高度恰等ε的区别无影响，下面也可统一采用≥。

令U=L_Hε。在[−ε,ε]取h(x)=A+C|x|，边界h=1，要求C=qA。Tanaka与有限变差乘积公式使\(e^{-qL}\)h(B)停于Hε后为有界鞅：dL系数C−qh(0)=0，其余漂移为0。Hε有限，DCT给下面的Laplace变换，所以U为均值ε的指数变量。

\[ Ee^{-qU}=\frac1{1+q\varepsilon},\qquad q\ge0. \]

还须证明完整游程形状与U独立，不能仅证明指数间隔。对确定l，在{U>l}上\(\tau_l\)<Hε且B\(\tau_l\)=0；\(\tau_l\)以后的第一个达ε游程正是同一个待保留标记。强Markov于\(\tau_l\)给P(U>l,e∈F)=P(U>l)Qε(F)，其中Qε为首个保留游程的分布。U无原子排除U=l的端点问题。这些半直线事件生成U的σ-代数，故独立。Dε处强Markov使各轮(U,e)独立同律。

因此按局部时标号的达ε游程是速率1/ε的Poisson时钟，带独立Qε标记。21章的有序密度/标记计算给，对任意非负Borel f，有限局部时窗内其Laplace泛函为exp[−∫dl∫(1−e^{−f})ε⁻¹Qε(de)]。这一步是本路径上的Poisson性证明，不是另造一个同均值的点过程。

不同ε给出的点过程只是从同一批真实游程删除小高度标记；其强度在交叠处相容，由期望计数即可核验。定义n在{H≥ε}上等于ε⁻¹Qε。取ε=1/k，集合递增覆盖E，给唯一σ有限测度。对任意f≥0，用这些限制过程及MCT得到全体游程的Laplace泛函，故为强度dl n(de)的PRM。

\[ n(H\ge a)=a^{-1},\qquad E\exp\!\left[-\sum_\ell f(\ell,e_\ell)\right]=\exp\!\left[-\int_0^\infty\!\int_E(1-e^{-f(\ell,e)})n(de)d\ell\right]. \]

对称反号使每个标记的符号公平，且与绝对值形状独立；同轮指数独立性也保留。因此标记定理给B的正、负游程为相互独立的PRM，各强度dl n(de)/2。27章的有限带Laplace唯一性足以识别所有不交Borel集合的独立计数，未借48章一般点过程。

## 3. 寿命强度与逆时钟归一化

<a id="excursion-proof-lifetime"></a>

由τℓ为游程寿命和及PRM泛函，Laplace指数为n(1−e^{−λζ})。T-LOCAL-TIME已经独立算出逆时钟变换，因此其值必须是√(2λ)。直接积分给出下列寿命密度；唯一性也应说明：对λ微分后得到有限加权测度ζe^{−ζ}n(dζ)的Laplace变换，再用13章唯一性恢复原测度。微分可先用差商与单调支配，指数积分的有限性保证ζe^{−λζ}可积。

\[ n(1-e^{-\lambda\zeta})=\sqrt{2\lambda},\qquad n(\zeta\in ds)=\frac{ds}{\sqrt{2\pi}s^{3/2}},\qquad n(\zeta>t)=\sqrt{\frac2{\pi t}}. \]

这些常数依赖局部时标度。R在0的右局部时等于2L：对非负R用Tanaka正部式，R=∫1_{R>0}dR+½\(L_R^{0,+}\)，与R=β+L比较即可。若改按\(L_R^{0,+}\)标号，则强度减半，不能在同一证明中混用。

## 4. 入口律不是从零点直接调用Markov

<a id="excursion-proof-entrance"></a>

\[ q_t(x,y)=\frac{e^{-(y-x)^2/(2t)}-e^{-(y+x)^2/(2t)}}{\sqrt{2\pi t}},\qquad k_t(y)=\lim_{x\downarrow0}\frac{q_t(x,y)}x=\frac{2y}{\sqrt{2\pi}t^{3/2}}e^{-y^2/(2t)}. \]

q是正半轴Brownian在0杀死的核，由反射原理得到。我们证明n下的入口律为kₜ(y)dy，并在以后时刻使用q转移。保留达ε游程，记其首次达ε的内部时间ρ。Qε下ρ≤Hε逐路径，所以\(E_{Q_\varepsilon}\rho\)≤E Hε=ε²。实际全路径的Hε是停止时刻，在其后到首返0，游程遵循从ε出发的杀死Brownian，独立于此前初段。

取0<t₁<⋯<tⱼ、各坐标紧支撑的有界连续测试。若ρ≤t₁/2，把实际tᵢ改成tᵢ−ρ只改变第一个q核的时间。由上式Gaussian差分，qᵤ(ε,y)/ε及其u导数在u≥t₁/2、y的紧集上有可积统一界；中间q核的时间差不变。因此除以ε后的时间移位期望误差≤C Eρ，趋0。ρ>t₁/2的n质量≤2Eρ/(εt₁)≤2ε/t₁，也趋0。

令ε↓0。被删去的低高度游程在{ζ>t₁}内质量趋0，因为该集合n质量有限。故有限维律实际为下面的乘积密度。连续测试的单调类推广给Borel测试；时间切片之后的余程规律为杀死Brownian。全过程没有在最后零点g使用强Markov。

\[ n(e(t_1)\in dy_1,\ldots,e(t_j)\in dy_j,\ t_j<\zeta)=k_{t_1}(y_1)\prod_{i=2}^jq_{t_i-t_{i-1}}(y_{i-1},y_i)\,dy_1\cdots dy_j. \]

## 5. 寿命条件化与规范游程的实际构造

<a id="excursion-proof-normalized"></a>

\[ h_u(y)=\frac{y}{\sqrt{2\pi}u^{3/2}}e^{-y^2/(2u)},\qquad c_s=\frac1{\sqrt{2\pi}s^{3/2}},\qquad Q_s(dy_1\cdots dy_j)=\frac{k_{t_1}(y_1)\prod_{i=2}^jq_{t_i-t_{i-1}}(y_{i-1},y_i)h_{s-t_j}(y_j)}{c_s}\,dy_1\cdots dy_j. \]

h是首达0的密度；上一节在tⱼ之后使用该密度，得到n联合ζ的分解。10章标准Borel分解定理给寿命条件律，仅几乎处处s唯一。为选定全部s且证明存在连续路径，取三个独立从0到0、时长s的Brownian bridges，其欧氏范数为Eˢ。这个过程连续，端点0，内部严格正：任意[δ,s−δ]上三维bridge律局部绝对连续于三维Brownian，后者不碰单点；对有理δ取并。

核对其有限维律：三维Brownian半径从x>0到y的密度是qₜ(x,y)y/x，由三维Gaussian在球面上的积分直接给出；从0的密度为√(2/π)y²\(t^{-3/2}\)\(e^{-y^2/(2t)}\)。桥的终端校正为\((s/(s-t_j))^{3/2}\)\(e^{-y_j^2/(2(s-t_j))}\)。乘积中相邻y/x因子望远镜相消，恰得上式Q_s。于是Eˢ的律就是寿命条件游程律，且按时间s、空间√s缩放E¹得到全部Q_s。

e=E¹称规范Brownian excursion。它不是普通Brownian bridge在“全程为正”这一零概率事件下未经定义的条件分布；此处由三个bridge实际构造，并由寿命分解识别。这里未证明条件随机树的函数极限，后者仍由53章承担。返回[正文的规范游程](../chapters/37-local-time.md#local-normalized)。
