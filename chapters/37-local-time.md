# 第三十七章：一条路径在某个位置停留了多少？——局部时间、占用与游程

把一段Brownian运动留下的记录按位置整理。每一次经过0都是真实发生的，但如果把所有满足Bₜ=0的时刻长度相加，答案却是0。记录没有造假，路径也确实反复回来；失去信息的是我们所使用的计量方式。

## 37.1 一个零答案，丢失了什么

<a id="local-question"></a>

第36章已严格区分命中与普通时间占用。对从0出发的标准Brownian运动，任何固定t>0时Bₜ有密度，Tonelli给单点的累计普通时间为0；连续性和常返却使它不断经过0。我们不重复证明常返，而问这份零答案能否恢复一些关于接触的细节。

\[ \int_0^t\mathbf1_{\{B_s=0\}}ds=0\quad\text{a.s.},\qquad \Lambda_t^\varepsilon=\frac1{2\varepsilon}\int_0^t\mathbf1_{\{|B_s|<\varepsilon\}}ds. \]

一个传感器并不必只报告“是否精确等于0”。它可以记录粒子处于宽度2ε的小带内的时间，再除以带宽。这个比值不是单点集合的时间长度，而是一种位置密度的候选。Gaussian核给EΛᵋ趋√(2t/π)，不是0；但期望有极限还不能证明每条路径真的拥有一份密度。

## 37.2 绝对值的尖点，恰好看见接触

<a id="local-smoothing"></a>

若用光滑函数观察路径，第32章Itô公式已经足够。要突出经过a的事件，绝对值|x−a|更合适：远离a时斜率恒定，所有曲率集中在a。但它不是C²，不能直接把普通二阶导数写成0，宣称修正项消失。先把尖角磨圆。

\[ F_\varepsilon(B_t-a)-F_\varepsilon(B_0-a)=\int_0^tF_\varepsilon^\prime(B_s-a)dB_s+\frac12\int_0^tF_\varepsilon^{\prime\prime}(B_s-a)ds,\qquad F_\varepsilon=|\cdot|*\rho_\varepsilon. \]

Fᵋ一致趋绝对值，导数有界且趋sgn；Itô等距加Doob使随机积分按L²最大范数收敛。因而曲率项也有ucp极限，非负并随t递增。不是先发明一个符号再寻找解释，而是现有变量变换公式强迫我们保留这份无法消失的累积。

\[ |B_t-a|=|B_0-a|+\int_0^t\operatorname{sgn}(B_s-a)dB_s+L_t^a,\qquad \operatorname{sgn}(0)=0. \]

这就是本书归一化的Tanaka公式。新量L称局部时间。系数没有另放½，因为平滑绝对值的曲率总量为2。后面所有游程速率、速度时钟和Bessel维数都要服从这个选择。[完整构造](../foundations/t-local-time.md#local-proof-tanaka)包括参数可测性及局部化。

## 37.3 密度必须同时适用于所有位置

<a id="local-occupation"></a>

目前只在每个固定a构造了一个过程。若想把空间切成许多小格，再拼回一份占用测度，仅有逐点存在还不够。把平滑Tanaka的曲率项乘连续紧支撑f(a)，关于a积分；Fubini把它变成沿路径积分的卷积测试，随后令ε趋0。

\[ \int_0^tf(B_s)ds=\int_{\mathbb R}f(a)L_t^a da\qquad(f\ge0\text{ Borel}). \]

连续测试先确定有限测度，再由单调类推广到Borel函数。在一个共同零集之外，它对所有t及所有Borel集合成立。因此L不是互不相干的一批随机变量，而是整条路径占用测度的一份空间密度。也正因为是密度，它在某一点的值可以非零，而该单点的测度仍为0。

特别要防止倒置逻辑：我们不是从“每个点普通时间为0”推出密度存在。许多无原子的测度仍然奇异。密度存在是平滑曲率、随机积分极限和测度识别共同证明的结果。

## 37.4 为什么能够看见一整张连续的局部时曲面

<a id="local-joint"></a>

占用密度按Lebesgue几乎处处位置本来就允许修改。如果某些位置的读数可以随意跳动，谈论“在a累积了多少”仍有版本问题。这里Brownian路径给予更强结构。两份水平a、b的Tanaka积分作差，只剩路径在两水平之间时的积分。

\[ E\left\|\int_0^\cdot\bigl(\operatorname{sgn}(B_s-b)-\operatorname{sgn}(B_s-a)\bigr)dB_s\right\|_{C[0,T]}^{2p}\le C_{p,T}|b-a|^p,\qquad p\ge2. \]

证明先用连续鞅高阶上界，再把括号中的带状占用改写为∫ₐᵇLᵞdy，用积分Hölder和局部时的一致矩界控制。二进网格方法于是给空间连续版本，取值于时间连续函数空间；L可联合连续，并在紧空间范围内具有任意低于1/2的空间Hölder阶。[证明3](../foundations/t-local-time.md#local-proof-regularity)写出这些步骤，不把“选连续版本”当成论证。

\[ \sup_{t\le T,\ |a|\le K}\left|\frac1{2\varepsilon}\int_0^t\mathbf1_{\{|B_s-a|<\varepsilon\}}ds-L_t^a\right|\longrightarrow0\quad\text{a.s.} \]

窄带极限现在来自占用公式与紧集上一致连续性，整张曲面的解释终于不再依赖每个位置各选一个零集。

## 37.5 换成一般连续半鞅，哪些连续性会失去

<a id="local-semimartingale"></a>

对X=X₀+M+V，L的占用测度必须是d[M]，不一定是ds。尖点导数的约定也开始重要。取sgn₋(0)=−1定义右局部时，完整Tanaka仍成立；它在t连续，在a右连续有左极限。空间跳跃由有限变差部分精确决定。

\[ \int_0^tf(X_s)d[M]_s=\int f(a)L_t^{a,+}da,\qquad L_t^{a,+}-L_t^{a-,+}=2\int_0^t\mathbf1_{\{X_s=a\}}dV_s. \]

这不是细微的记号游戏。反射Brownian的推回量正集中在0，右局部时在0的值与从负水平逼近的值不同；不能把Brownian的联合连续结论无条件推广给所有连续半鞅。若V=0，或者36章非退化SDE的漂移不在单点积累，则空间跳跃消失。

## 37.6 接触集合怎样成为一个时钟

<a id="local-two-clocks"></a>

dLᵃ只在B=a时增加：若一段路径与a保持正距离，足够窄的平滑曲率在该段完全为0。因而零集虽然没有普通时间，却支撑整份L⁰。Tanaka还允许我们准确计算这份累积的大小，而不是只宣称它“非平凡”。

\[ |B_t|=\beta_t+L_t^0,\quad \beta_t=\int_0^t\operatorname{sgn}(B_s)dB_s,\quad [\beta]_t=t,\qquad L_t^0=\sup_{s\le t}(-\beta_s)^+\ \overset d=\ \sup_{s\le t}B_s. \]

β由Lévy刻画为Brownian。最后一个身份来自确定Skorokhod引理：要把连续w推到非负半轴、又只准在0增加推力，最小且唯一的推力量就是此前负向最低点的相反数。反射原理于是给ELₜ⁰=√(2t/π)，且L随时间无界。接触没有持续长度，仍有可计算的累计强度。

31章Cantor时钟说明随机积分的能量取决于哪份时间测度；这里新增的是由路径自身与位置共同生成的时钟。可预测H=\(\mathbf1_{\{B=0\}}\)对dB的积分为0，因为其平方能量为0；对dL⁰的积分却是L⁰。可预测性没有让两份积分成为同一对象。

## 37.7 把时钟倒过来，空白成为跳跃

<a id="local-inverse"></a>

\[ \tau_\ell=\inf\{t:L_t^0>\ell\},\qquad Ee^{-\lambda\tau_\ell}=e^{-\ell\sqrt{2\lambda}}. \]

τℓ是“累计接触超过ℓ需要多少普通时间”，是有限停止时刻。B在该时刻为0；强Markov与局部时加性使增加相同局部时所需的未来时间彼此独立、规律不变。Skorokhod表示把其固定ℓ的规律转成Brownian首达−ℓ，给出Laplace式。它是1/2稳定的增长过程，不是连续的线性换钟。

L在离开0的一整段运动中不变。倒钟时，这段真实运动被压缩成τ的一次跳跃。我们应当保留跳跃之间究竟藏着哪一段路径，而不只记录它的持续时间。

## 37.8 游程的切分，尚未包含独立性

<a id="local-excursion-path"></a>

连续路径的零集闭，补集为可数不交开区间(g,d)。每一段给出一条从0出发、在内部不再碰0、最终回0的游程，寿命ζ=d−g。按\(L_g\)给它标号。以区间内第一个有理数枚举，能把这份路径分解做成可测对象。[专题1](../foundations/t-excursions.md#excursion-proof-space)给标准Borel编码。

这一步还没有证明游程独立。g是最后一个零点，通常不是停止时刻，不能从g直接调用强Markov。无穷多个小游程也不可能组成普通有限速率的到达序列。必须先找到合法的再生实验。

## 37.9 只保留足够大的游程

<a id="local-excursion-clock"></a>

固定ε。等到|B|首次达到ε，再等它回0，重复。这些才是停止时刻。每轮只保留达到ε的那条完整游程，其它小游程暂不记录。令U是这一轮在首达ε以前累积的L。对分段线性h=A+C|x|应用Tanaka，使\(e^{-qL}\)h(B)无漂移，只须C=qA；边界h(±ε)=1决定A。

\[ Ee^{-qU}=\frac1{1+q\varepsilon}. \]

U因此是均值ε的指数变量。形状独立还需另一论证：在{U>l}上，\(\tau_l\)是0处的合法停止时刻，之后的第一个达ε游程仍是同一个尚未出现的标记；强Markov使它的形状规律不随已经等过的l改变。于是等待局部时与整个游程形状独立，各轮也独立同律。21章的指数更新计算现在可以使用。

## 37.10 Itô测度为什么不是概率测度

<a id="local-ito-measure"></a>

对R=|B|的正游程，记n为按L标号的强度。达ε游程的强度为1/ε，其形状有概率律Qε。不同ε只是在同一批路径中删去小游程，强度在交叠处相容，所以n由这些有限限制唯一拼成。

\[ n(H\ge a)=\frac1a,\quad N=\sum_\ell\delta_{(\ell,e_\ell)},\quad Ee^{-N(f)}=\exp\left[-\int_0^\infty\!\int_E(1-e^{-f(\ell,e)})n(de)d\ell\right]. \]

n总质量无穷，却在每个{H≥a}上有限。它不是“随机挑一条游程”的概率分布，而是一单位接触累积中各种形状出现的强度。上式经有限阈值极限完整证明了Poisson性质；实际路径切分与PRM现在才被联系起来。带正负号的B游程由独立公平标记得到，正、负两侧各强度n/2，彼此独立。

## 37.11 寿命常数也必须由时钟核对

<a id="local-excursion-lifetime"></a>

\[ \tau_\ell=\sum_{s\le\ell}\zeta(e_s),\qquad n(1-e^{-\lambda\zeta})=\sqrt{2\lambda},\qquad n(\zeta\in dt)=\frac{dt}{\sqrt{2\pi}t^{3/2}}. \]

零集的普通时间为0，所以倒钟正是游程寿命之和，没有额外普通时间漂移。Poisson泛函与已经独立算出的倒钟Laplace式识别寿命强度。该密度在0不可积，解释了任意局部时窗口内的小游程为何无穷多；而∫(1∧ζ)n有限，保证其总寿命在有限局部时窗口几乎必然有限。

若改用R在0的右局部时，它等于2L，强度便减半。一个看似无关紧要的局部时系数，会同时改变首达、游程与后面的Ray–Knight公式；所以本章始终固定同一归一化。

## 37.12 从零出发的游程，如何获得入口律

<a id="local-entrance-law"></a>

普通Brownian从0出发立刻跨越两侧，不能拿它在0的转移密度当作正游程的起点规律。先从x>0出发，在0杀死；反射原理给差分Gaussian核q。达ε游程在首次ε以后按这个核运行，而此前初段的平均时长至多ε²。强度乘1/ε后，其时间移位误差仍可控制，才允许令ε趋0。

\[ q_t(x,y)=p_t(y-x)-p_t(y+x),\qquad n(e_t\in dy,t<\zeta)=\frac{2y}{\sqrt{2\pi}t^{3/2}}e^{-y^2/(2t)}dy,\quad y>0. \]

以后时刻使用q的乘积。这份入口律把“从0离开但内部不碰0”的限制真正放入了数学。[专题4](../foundations/t-excursions.md#excursion-proof-entrance)逐项估计初段和小高度尾部，不用“从0连续延拓”代替证明。

## 37.13 一条规范游程究竟怎样选出来

<a id="local-normalized"></a>

n不是概率，却可以按寿命分解。给定寿命s，其有限维密度由入口核、内部杀死核和最后首返0密度相乘，再除以寿命密度。10章的分解先只给几乎处处s的版本；我们仍需实际构造一条寿命恰为1的连续正路径。

\[ e_t=\sqrt{(b_t^1)^2+(b_t^2)^2+(b_t^3)^2},\quad 0\le t\le1,\qquad b^1,b^2,b^3\text{ independent standard Brownian bridges}. \]

这条路径在两端为0，内部严格正。三维径向Gaussian核与bridge的终端校正计算，恰好给寿命分解中的全部有限维密度，所以其律就是规范Brownian excursion。时长s的版本为√s e(t/s)。它不依赖在“bridge全程正”这个零概率事件上含混地条件化，也没有借未来条件随机树极限。[完整核对](../foundations/t-excursions.md#excursion-proof-normalized)保留常数和可测版本。

## 37.14 把空间看成新的演化参数

<a id="local-spatial-profile"></a>

现在Lₜᵃ不仅能对a积分，也能把a作为参数观察。固定一个合适的停止时刻，整条占用剖面可能拥有自己的Markov结构。这远比一份平均Green密度更强：它涉及相邻位置的随机依赖，而不是期望曲线的形状。

最先需要识别的是其联合律。取非负空间权重φ，计算exp(−∫φL)的期望；占用公式把这份空间读数重新变为沿Brownian路径的加权时间。在一维，要求这个读数停止后公平，会产生一个二阶ODE。与其先公布Ray–Knight的答案，我们先看看这份ODE藏着什么过程。

## 37.15 线性方程中藏着平方根噪声

<a id="local-riccati"></a>

\[ \tfrac12v^{\prime\prime}=\varphi v,\quad v(0)=1,\quad v^\prime(R)=0,\qquad u=-\frac{v^\prime}{2v}:\quad u^\prime=2u^2-\varphi,\quad u(R)=0. \]

φ在[0,R]外为0。终端导数0对应远处没有额外惩罚的常数读数。v严格正，u非负。把v的对数斜率取出来，二阶线性方程就变成Riccati式；其中2u²恰好是扩散系数2√z作用在指数\(e^{-zu}\)时产生的项。

\[ dZ_x=\delta(x)dx+2\sqrt{Z_x}\,d\beta_x,\quad Z_0=z,\qquad E_ze^{-\int_0^R\varphi(x)Z_xdx}=\exp\left[-zu(0)-\int_0^R\delta(x)u(x)dx\right]. \]

这个平方Bessel过程先由35章存在与模唯一性构造，再以有界指数鞅验证变换，不倒借Ray–Knight。δ=0是没有移民的连续状态临界分枝，δ=2加入确定的空间移民率。空间参数x在这里承担原来时间的角色；它不是说Brownian粒子真的沿空间方向作另一场运动。

## 37.16 首达一个高度，得到第一Ray–Knight定理

<a id="local-ray-first"></a>

从0等到首达a>0。将φ的支撑包含在R>a以内。反向数空间距离x=a−位置，定义Zx=\(L_{T_a}^{a-x}\)。在刚达到的端点a，局部时尚未累积，故Z₀=0。占用公式和停止Itô把这份剖面的Laplace读数算成v(a)。

\[ Ee^{-\int_0^R\varphi(x)L_{T_a}^{a-x}dx}=v(a)=\exp\left[-2\int_0^au(x)dx\right]. \]

这与上式z=0、δ=2直到a而后δ=0完全一致。非负连续场的Laplace读数确定其律，所以在[0,a]上Z是BESQ2；超过a以后，给定Za，它以BESQ0继续。重要的是停止方式和空间方向：不能删掉Tₐ、倒转a−x，或者把确定时刻t的剖面也直接称作同一个过程。

[证明3](../foundations/t-ray-knight.md#ray-proof-first)由有界停止指数实际得到v(a)，没有预借38章的一般Feynman–Kac。它也以Green期望2min(x,a)核对Bessel系数。

## 37.17 累计固定接触量，得到第二Ray–Knight定理

<a id="local-ray-knight"></a>

若改在τℓ停止，所有正游程的收益相加；Poisson泛函把它的Laplace读数写成exp[−ℓn(1−\(e^{-A_\varphi}\))/2]。同一ODE给n(1−\(e^{-A_\varphi}\))=−v′(0)=2u(0)。因子½来自正负公平分割，恰好抵消这个2。

\[ (L_{\tau_\ell}^{x}:x\ge0)\ \overset d=\ \mathrm{BESQ}^{0}(\ell),\qquad (L_{\tau_\ell}^{-x}:x\ge0)\ \overset d=\ \mathrm{BESQ}^{0}(\ell),\quad\text{independently}. \]

两个剖面共享的是确定初值ℓ，不是一个额外随机变量；其后独立来自两份独立游程PRM。BESQ0的转移变换还给出明确的分枝与灭绝机制。

\[ E_ze^{-qZ_x}=\exp\left(-\frac{zq}{1+2qx}\right),\qquad P_z(Z_x=0)=e^{-z/(2x)},\qquad EZ_x=z\quad(x>0,q\ge0,z\ge0). \]

初值可加时独立过程之和与从和初值出发的过程同律，正是连续状态分枝性。每条剖面最终灭绝，有限空间位置的期望却不下降。20章关于家族与平均的区别，在这里获得一份新的、严格可识别的空间过程，而不只是重复一个期望流失故事。[证明4–5](../foundations/t-ray-knight.md#ray-proof-second)保留全部匹配和边界条件。

## 37.18 扩散的局部时间，和普通时间相差一个系数

<a id="local-diffusion-density"></a>

回到36章的非退化SDE。它的二阶时钟是σ(X)²dt，因此占用公式给普通时间的空间密度为Lᵃ/σ(a)²，而不是Lᵃ。尺度变换也改变局部时：位置单位改变时，密度必须相应变化。

\[ \int_0^tf(X_s)ds=\int_I f(a)\frac{L_t^a(X)}{\sigma(a)^2}da,\qquad L_t^{S(a)}(S(X))=S^\prime(a)L_t^a(X). \]

前式由两份测度比较，后式由占用与变量代换证明。至此36章平均Green规律与逐路径占用有了真正回链：先有每条路径的密度，再取期望得到Green；不是把平均密度本身当成每条路径的停留记录。

## 37.19 速度甚至可以是一份奇异测度

<a id="local-speed-clock"></a>

如果速度集中在稀疏的位置，直接要求m有密度就会丢掉模型。局部时间允许另一种构造：先让Brownian走，按它在各位置的接触强度向速度测度收费，再把收费时钟倒过来。

\[ A_s=\frac12\int_JL_s^y(B)m(dy),\qquad T_t=\inf\{s:A_s>t\},\qquad Y_t=B_{T_t}. \]

在开区间J取局部有限Radon速度，每个非空开子区间质量正，Brownian在离开J时停止。连续局部时使A有限连续；满支撑使A严格增加，因而Y确有连续路径。强Markov及局部时加性证明Y强Markov。半因子不可省：Brownian本身的速度为2dy，此时A=s。

[构造与逆向表示](../foundations/t-diffusion-time.md#time-proof-construction)给出Green核、奇异速度和自然尺度过程的准确类别。没有满支撑，时钟可能跳过Brownian穿越某段空间的时间，换时路径便可能产生跳跃；连续性不是只从“Brownian原来连续”自动继承的。

例如在(0,1)枚举有理点qₙ，取m=∑2⁻ⁿ\(\delta_{q_n}\)。它局部有限、满支撑却完全原子化，上述构造仍给连续路径。占用身份说明路径在无理位置的普通时间总量为0，但不能据此说它从未经过无理位置；连续地跨过一个区间必经过其中全部位置。这里速度的支撑、停留时间与路径经过的集合又一次被严格区分。

## 37.20 36章的方程，怎样从时钟恢复

<a id="local-speed-converse"></a>

当m′=2/α²连续严格正，普通积分换元给Tₜ=∫₀ᵗα(Y)²du；Y的括号恰为T。再除以α构造括号t的鞅，就得到Brownian驱动及dY=α(Y)dW。以S⁻¹变回原坐标，正好恢复36章的漂移与波动。

更一般，给定自然尺度的连续正则强Markov过程，若紧区间退出均值有限，则这些均值是凹函数，其负的二阶Stieltjes测度唯一确定m。Tanaka对凹函数的积分形式与强Markov的剩余退出时间鞅相比较，强迫t=½∫Lₜᵃm(da)。DDS随后恢复同一Brownian时钟表示。[逆向证明](../foundations/t-diffusion-time.md#time-proof-converse)实际构造这份测度，没有假设速度已经具有密度。

## 37.21 把质量放在边界，会怎样

<a id="local-sticky"></a>

36章曾把反射与吸收分开。现在可以构造介于即时反射与永久陷阱之间的粘滞边界。取反射Brownian R=x+β+K，K只在0推回；其0处右局部时是2K。在速度2dy之外放一颗质量θ的原子，得到

\[ A_s=s+\theta K_s,\qquad Y_t=R_{T_t},\qquad \int_0^t\mathbf1_{\{Y_u=0\}}du=\theta K_{T_t}. \]

θ>0时，零点真的获得普通时间；但路径并不是在0等一段指数时间才突然重启。它没有有限平坦等待段，接触集合通过时钟获得正的总时间。再按K的独立指数阈值杀死，得到弹性边界。内部算子未改，光滑测试的边界关系却变成f′(0)=θAf(0)+κf(0)。

[边界证明](../foundations/t-diffusion-time.md#time-proof-boundaries)在有限正则端点、连续局部Feller规则的范围说明这些参数的来源：去掉内部游程后，边界用时作为局部时参数下的连续增长Lévy过程，只能是确定漂移θl；死亡则对应无记忆阈值。一般边界跳入和内部杀死不在这个分类内。

## 37.22 两种边界积分，仍然各自回答不同问题

<a id="local-boundary-recovery"></a>

尺度—速度构造并未取消36章的Σ与N。Green公式延伸到奇异Radon速度，λ调和ODE相应变成Stieltjes—Volterra式；Tanaka让它仍能产生合法的折扣鞅。于是Σ判断内部能否有限时抵达，N在不可达端点判断能否从那里连续即时进入。

奇异模型没有一份Lipschitzσ可直接调用。入口构造改用相遇后同行的有序耦合、Green返回界和局部时钟的路径律连续性；[证明5](../foundations/t-diffusion-time.md#time-proof-feller)说明替换的每个环节。正则、出口、入口、自然四类没有被合并；端点可达性、起点合法性和抵达后规则仍是不同数学主张。

## 37.23 一份空间测度，怎样指认一种累积

<a id="local-revuz"></a>

固定位置只是一种收费方式。对正Radon测度μ，令Aᵗμ=∫Lₜᵃμ(da)。它是实际有限连续的加性泛函，因为紧时间的Brownian路径范围紧、L联合连续。取μ为单点质量得到局部时间，取μ=q(a)da得到普通时间收益∫q(B)ds，奇异μ则描述集中在普通时间零集上的累积。

\[ \lim_{t\downarrow0}\frac1t\int_{\mathbb R}g(x)E_x\!\int_0^tf(B_s)dA_s^\mu dx=\int_{\mathbb R}f(a)g(a)\mu(da). \]

这里f非负连续紧支撑，g非负有界连续，参考测度为dx。支持性质、Gaussian核对称性和DCT完整证明这份小时间身份，识别μ为该泛函的Revuz测度。参考换成2dx时右边也加倍。我们已经构造并识别这类Brownian泛函，但一般右过程上任意PCAF与平滑测度的双射、例外集合和版本技术仍归38章；没有用这句身份把最广定理提前登记通过。

## 37.24 零长度的接触，留下了一种完整结构

<a id="local-insight"></a>

最初的零答案没有被推翻。Brownian在一个固定位置的普通时间仍然是0。改变的是我们现在知道怎样把这份信息放回正确的层次：先在位置上构造占用密度，再用它计量接触、排列游程、改变时钟，甚至把整条空间剖面识别为另一类扩散。

Tanaka说明曲率集中在哪里会留下累积；游程证明零集可以组织相互独立的一批路径；Ray–Knight把占用剖面和连续状态分枝严格联系；速度原子则使原先忽略的接触获得普通时间。这些是不同定理支持的联系，不是“零等于非零”的悖论。

现在可以问得更具体：给定一份空间收费、一个边界和一种折扣，沿路径累积的平均值满足什么方程？当收费集中在一个点或一份奇异测度上，方程中的源项与边界条件应当怎样读？局部时间已经让这些问题有了可构造的随机对象；接下来要辨认的，是它们对应的势与确定性方程。

### 来源与证明范围

Ray与Knight的1963年原始工作研究了扩散的sojourn density及其空间Markov结构；本章采用Tanaka、显式ODE与Poisson游程的现代重建，不声称复现原始发现顺序。原始书目：[Knight](https://doi.org/10.1090/S0002-9947-1963-0154337-6)、[Ray的书目核验](https://www.ams.org/books/surv/018/surv018-endmatter.pdf)。游程标度亦与[Perman–Wellner作者公开论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4847753/)的对称Brownian局部时约定对照；该文用带符号测度，本章的n为其绝对值推前，正负各半。

主要证明分置[T-LOCAL-TIME](../foundations/t-local-time.md)、[T-EXCURSIONS](../foundations/t-excursions.md)、[T-RAY-KNIGHT](../foundations/t-ray-knight.md)、[T-DIFFUSION-TIME](../foundations/t-diffusion-time.md)。一般右过程的完整Revuz对应不在本章冒充完成。
