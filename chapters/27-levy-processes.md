# 第二十七章：如果随机运动会跳跃而不只是扩散？——Lévy processes 与 Lévy–Khintchine 理论

把许多独立的小扰动加在一起，未必只得到一条连续而粗糙的曲线。设有一排彼此独立的时钟：第k只每单位时间平均响2ᵏ次，每响一次，位置就向右移动2⁻ᵏ。越往后，单次移动越难看见，但声音也越密。每一层在时间t内贡献的平均位移都是t。

如果照原样把所有层加起来，位移没有有限答案。然而，将每层减去自己的平均位移以后，剩下的总波动却能够形成一条真正的随机路径。问题不在于是否容许很小的跳跃，而在于无穷多个小跳应该以什么方式合在一起。

## 27.1 每一层都有限，总和却不一定存在

<a id="levy-clocks"></a>

\[
\begin{gathered}
N_k(t)\sim\operatorname{Poisson}(2^k t),\qquad
J_k(t)=2^{-k}N_k(t),\qquad k\ge1,\\
EJ_k(t)=t,\qquad
E[J_k(t)-t]^2=t\,2^{-k}.
\end{gathered}
\]

这些是第21章已经构造的独立Poisson时钟，可以在第8章的可数乘积空间中同时实现。不能仅因均值之和无穷，就断言随机和几乎必然无穷：第7章的尖峰已经警告过我们。这里有更强的论证。

\[
P\{N_k(t)<2^{k-1}t\}
\le\frac{4}{2^k t}\quad(t>0).
\]

Chebyshev与Borel–Cantelli说明，对每个固定正t，最终每一层的位移至少为t/2，普通正项和因而几乎必然发散。另一方面，中心化后的方差之和有限，第12章保证固定时刻的级数收敛。两个结论并不矛盾：我们更改了所加的对象。

但固定时刻的答案还不够。分别在每个t求极限，未必得到同一条右连续、有左极限的路径，更不能直接对不可数个t交概率1事件。这与Brownian路径构造遇到的是同一种量词困难。本章要同时解释两件事：哪些跳跃强度容许极限存在，以及怎样把分布上的答案落实为整条路径。

## 27.2 保留的是增量结构，不是连续性

<a id="levy-definition"></a>

Brownian与Poisson运动有一项共同的计算便利：不相交时间段提供独立的增量，相同长度时间段提供同一种增量分布。连续性却只有前者具备。为了同时研究它们，我们保留共同的增量结构，并要求短时间的位移在概率意义下变小。

\[
\begin{gathered}
X_0=0,\qquad X_t\in\mathbb R^d,\qquad
X_{t+s}-X_s\overset d=X_t,\\
X_{t_1}-X_{t_0},\ldots,X_{t_m}-X_{t_{m-1}}
\text{ independent}\quad(0=t_0<\cdots<t_m),\\
X_{t+h}-X_t\xrightarrow{P}0\quad(h\to0,\ t+h\ge0).
\end{gathered}
\]

本章把同时具有càdlàg路径的这种过程称为Lévy过程；càdlàg意为右连续且每个正时刻有左极限。路径条件是当前采用的定义的一部分。我们会从全部允许的参数实际构造这样的版本，不把一个只有有限维分布的抽象过程未经证明就当成已有正则路径。

随机连续性不等于样本路径连续。Poisson过程在每条有限时间窗内可能跳跃，但在一个指定时刻附近的短区间发生跳跃的概率趋0。càdlàg与随机连续性合起来排除固定时刻的跳：从左趋近时，增量既几乎必然趋于该跳量，又依概率趋0，因此该时刻的跳量几乎必然为0。随机时刻的跳仍可大量存在。

若仅要求独立平稳增量，不要求任何时间正则性（既不要求càdlàg，也不要求随机连续），抽象加法函数给出一个边界：不连续的实加法函数a所定义的确定过程Xₜ=a(t)具有前两项结构，却不能由下面的连续时间指数描述。这不是现实模型，而是说明正则性要求承担了真正的数学工作。

## 27.3 从计数率看见一个测度

<a id="levy-measure"></a>

有限活动模型只需一个时钟和一份标记分布：时钟速率λ，标记律F，跳大小按F独立抽取。跳跃的全部信息可写成有限测度λF。现在沿着章首时钟向更小尺度看去，一个总速率已经不够：总跳数可能无穷，而每一种离零的跳仍应只有有限频率。

\[
\nu(B)=\text{mean number per unit time of jumps with size in }B,
\qquad B\subset\mathbb R^d\setminus\{0\}.
\]

这句话暂时是构造的动机，不是对任意过程已证的事实。我们先给一个候选Borel测度，再制造时钟；稍后才从任意给定Lévy路径恢复它。为使小跳中心化后的平方波动可加，需要的条件是

\[
\nu(\{0\})=0,\qquad
\int_{\mathbb R^d}(1\wedge\|x\|^2)\,\nu(dx)<\infty .
\]

这就是Lévy测度。离零区域有限质量，保证看得见的大跳不会在有限时间无限堆积；原点附近按平方加权，保证补偿波动可在L²中求和。它不要求一阶绝对可积，也不要求总质量有限。章首例子的测度在2⁻ᵏ处放2ᵏ的质量，平方积分有限，一阶积分却无穷。

平方条件并非只为某个方便的证明而设。若实线上小跳密度为|x|⁻³，对称截断的特征函数模等于指数的负积分。对每个非零频率，原点附近1−cos(ux)至少为常数乘u²x²，积分随截断解除而无穷。因此特征函数的点态候选在0为1、其余为0，不连续，根本不能是一份弱极限概率。任何确定漂移只能改变相位，救不了这个模。

## 27.4 把每个尺度的时钟放进同一个空间

<a id="levy-prm"></a>

将非零空间分为单位球外及一列二进环带。每带的测度有限，分别使用第21章的Poisson时钟，速率取该带质量；每次响铃独立抽取该带归一化测度给出的标记。不同带独立，零质量带不响。第8、10章的可数乘积构造使这些选择同时存在。

每一个响铃产生一对“时间、跳大小”。把这些点计成一个随机计数测度N；对任意非负可测函数，N(f)就是所有点上的函数值之和，允许无穷。它在每条实现上可数可加，因为它本来就是可数个Dirac测度的和。

\[
\begin{gathered}
\mu(ds,dx)=ds\,\nu(dx),\qquad
E e^{-N(f)}=\exp\!\left\{-\int(1-e^{-f})\,d\mu\right\},\\
E N(f)=\int f\,d\mu\quad(f\ge0).
\end{gathered}
\]

为什么这些公式成立？在一个有限带与有限时间窗中，给定总计数后，到达时间是独立均匀点的排序，标记又独立。因此条件Laplace变换是一份单点平均的计数次幂，再对Poisson计数求平均即得第一式。有限带数逐次增加，由单调收敛放开限制。均值公式先对指标，再对简单函数及非负极限成立。

对互不相交的有限强度集合，把f取为它们指标的线性组合，联合Laplace变换分解。这既证明每个计数是Poisson，也证明这些计数独立。我们称N为强度μ的Poisson随机测度。这一名称现在压缩的是已经构造出的对象，不是代替构造的术语。[配套证明第1节](../foundations/t-levy-paths.md#t-levy-prm)给出全部可测集合的扩展。

## 27.5 补偿不是减掉一个无穷常数

<a id="levy-compensation"></a>

先固定正截断ε，只相加大于ε、至多1的跳，然后减去这一有限带上的均值。两个有限数的差完全合法。最后才研究ε趋0的极限，绝不先写“无穷跳和减去无穷均值”。

\[
\begin{gathered}
M^\varepsilon_t=
\int_{(0,t]\times\{\varepsilon<\|x\|\le1\}}
x\,N(ds,dx)-t\int_{\varepsilon<\|x\|\le1}x\,\nu(dx),\\
E M^\varepsilon_t=0,\qquad
E\|M^\delta_t-M^\varepsilon_t\|^2
=t\int_{\delta<\|x\|\le\varepsilon}\|x\|^2\nu(dx),\qquad 0<\delta<\varepsilon\le1.
\end{gathered}
\]

等距来自独立Poisson计数的方差等于均值。先在互不相交有限强度集合的简单函数上逐项计算，再用T-LP完备性延拓到确定的L²函数。因此这里的积分记号只表示确定函数的L²延拓，不需要尚未发展的可预测随机被积函数理论。

有限截断过程是鞅：未来带内计数独立于全部过去，补偿使其条件均值为0。在每个二进时间网格上使用第15章Doob不等式，再以右连续性放开网格，便得到比固定时刻等距强得多的控制。

\[
\begin{gathered}
v(\varepsilon)=\int_{0<\|x\|\le\varepsilon}\|x\|^2\nu(dx)\downarrow0,\\
E\sup_{t\le T}\|M^\delta_t-M^\varepsilon_t\|^2
\le4T\,v(\varepsilon)\qquad(0<\delta<\varepsilon).
\end{gathered}
\]

## 27.6 一份平方估计怎样制造整条路径

<a id="levy-path-limit"></a>

选择下降截断序列，使第j项剩余二阶积分至多2⁻⁴ʲ。在时间窗[0,j]上，相邻截断的上确界差超过2⁻ʲ的概率至多4j2⁻²ʲ，概率和有限。Borel–Cantelli和望远镜求和保证：在同一个概率1事件上，这列有限跳路径在每个紧区间一致收敛。

càdlàg函数的一致极限仍càdlàg：先用一个足够近的有限截断控制误差，再使用它的右连续及左极限。由Fatou还可把估计传给全部截断，而非只传给选定子列。

\[
\begin{gathered}
M^{\varepsilon_j}\longrightarrow M
\quad\text{locally uniformly a.s.},\\
E\sup_{t\le T}\|M_t-M^\varepsilon_t\|^2
\le4T\,v(\varepsilon)\to0 .
\end{gathered}
\]

因此整个截断族在紧区间上一致依概率收敛，简称ucp。固定时刻的L²收敛把鞅性质传给极限；有限截断增量的联合特征函数分解也传给依概率极限，故独立平稳增量仍保留。短时间二阶矩趋0，又给随机连续性。我们所需的路径，不是凭固定时刻的若干答案拼起来的，而是由一个共同上确界估计制造出来的。

这是章首例子真正缺少的一步。它的跳全向右，补偿过程却并不单调。每个有限截断是一条确定性下降线加有限正跳；极限只由这一整列补偿截断共同定义，不能拆成普通无穷正跳和减一条有限下降线。极限在每个时刻均值0且有正方差，若路径非降就会非负，进而被均值0迫成恒0，矛盾。

## 27.7 三种彼此独立的运动

<a id="levy-model"></a>

现在加入独立的连续Gaussian运动G，协方差矩阵A非负；再加入确定漂移及单位球外的大跳。Gaussian部分可用第23章的独立Brownian坐标与矩阵平方根实际构造。大跳在有限窗内只有有限个，哪怕跳大小没有均值，也没有路径求和困难。

\[
\begin{gathered}
X_t=bt+G_t+
\int_{(0,t]\times\{\|x\|>1\}}x\,N(ds,dx)+M_t,\\
E[G_sG_t^\top]=(s\wedge t)A,\qquad G\perp\!\!\!\perp N .
\end{gathered}
\]

这已经是一条Lévy过程。有限截断时各部分特征函数相乘，补偿给跳项减去线性项。小球上二阶余项由Lévy积分条件支配，解除截断便得到

\[
\begin{gathered}
E e^{i\langle u,X_t\rangle}=e^{t\Psi(u)},\\
\Psi(u)=i\langle b,u\rangle-\frac12u^\top Au+
\int_{\mathbb R^d\setminus\{0\}}
\left(e^{i\langle u,x\rangle}-1-
i\langle u,x\rangle\mathbf1_{\{\|x\|\le1\}}\right)\nu(dx).
\end{gathered}
\]

积分中的线性减项不是为了改变跳跃规律，而是记录有限截断下的中心化。整体小跳一阶积分未必存在，不能把它当成一个有限均值再搬到漂移里。在单位跳Poisson过程里，测度为λδ₁、Gaussian部分为0，按这里包含边界1的约定，b必须取λ：小跳部分是Nₜ−λt，加回λt才是原计数。因而b不能未经检查就叫作实际速度或均值。

路径构造完成了“给参数，造过程”。但Lévy–Khintchine理论更强：任何独立平稳增量的正则运动，都只能有这种形式。若没有反方向，我们只展示了一大类例子，尚未解释为什么它们穷尽可能性。

## 27.8 为什么任意分布不能成为单位时间增量

<a id="levy-khintchine"></a>

把单位时间切成n段。其增量必须是n个独立同分布小增量之和，所以单位时间分布无限可分。第14章已证明无穷小独立阵列的极限无限可分；现在要把当时的结构判断变成一组具体、唯一的参数。

Lévy–Khintchine定理的有限维形式如下：一份实向量概率分布无限可分，当且仅当它的特征函数是上一节公式中t=1的指数，A为非负对称矩阵，ν为Lévy测度，b为实向量；在固定截断约定下三者唯一。对Lévy过程，该同一指数乘任意时间t便给全部增量律；独立性再给全部有限维分布。

充分性已经由路径构造证明：把参数同时除以n，单位时间模型的n个独立副本相加便还原原参数。必要性与唯一性不能靠这个构造倒推。下面把两个真正困难的步骤展开：紧性怎样约束参数，以及不假定二阶矩时怎样识别参数。

## 27.9 把无穷测度换成有限的观察对象

<a id="levy-finite-measure"></a>

直接对ν抽子列会遇到障碍：它在原点附近的总质量可以无穷，普通概率测度紧性不适用。另一方面，小跳在特征指数中只以二阶方式出现。于是给跳测度乘一个在原点像平方、远处有界的权重，正好得到有限测度。为便于参数收敛，同时采用连续截断h。

\[
\begin{gathered}
h(x)=\frac{x}{1+\|x\|^2},\qquad
w(x)=\frac{\|x\|^2}{1+\|x\|^2},\\
\Psi(u)=i\langle\gamma,u\rangle-\tfrac12u^\top Au+
\int(e^{i\langle u,x\rangle}-1-i\langle u,h(x)\rangle)\nu(dx),\\
b=\gamma+\int\left(x\mathbf1_{\{\|x\|\le1\}}-h(x)\right)\nu(dx).
\end{gathered}
\]

漂移转换积分绝对收敛：原点附近差为三阶，远处有界而ν质量有限。跳跃没有因截断约定改变；改变的只是被放到确定线性项里的那一份补偿。

在实线上，把Gaussian方差放成原点原子，便有唯一的有限canonical测度。相应积分核在原点有连续延拓。

\[
\begin{gathered}
\rho=\sigma^2\delta_0+w\nu,\qquad
\Psi(u)=iu\gamma+\int K_u(x)\rho(dx),\\
K_u(x)=\frac{e^{iux}-1-iux/(1+x^2)}{x^2/(1+x^2)}
\quad(x\ne0),\qquad K_u(0)=-u^2/2.
\end{gathered}
\]

这解释了一个容易误读的极限：原先都是跳的分布，为什么会留下Gaussian部分？若加权质量不断挤向原点，它在连续核中留下二次项。Gaussian质量不是“大小为0的跳”；原点原子属于这个加权替代测度，不属于ν。

向量情形还要记住接近原点的方向。把非零点写成半径与单位向量，提升到半径—方向空间；原点层的方向二阶积分给协方差矩阵。不同角测度可以给同一个矩阵，所以不能宣称角测度本身也是唯一参数。[参数证明第1节](../foundations/t-levy-characteristics.md#t-levy-canonical)给出有界连续核及全部矩阵细节。

## 27.10 紧性如何迫使三种参数留下来

<a id="levy-necessity"></a>

先看一列已经具有表示的复合Poisson加Gaussian分布。如果它们弱收敛，特征函数在原点附近共同趋近1。取负对数的模，确定漂移消失，剩下的都是非负项。对一个小频率立方体平均，跳项的cos变成各坐标sinc的乘积。

\[
\begin{gathered}
a(\delta)=\sup_n\sup_{\|u\|_\infty\le\delta}
[-\log|\phi_n(u)|]\longrightarrow0,\\
\frac{\delta^2}{6}\operatorname{tr}A_n+
\int\left[1-\prod_{j=1}^d\operatorname{sinc}(\delta x_j)\right]\nu_n(dx)
\le a(\delta).
\end{gathered}
\]

核在小球上至少为常数乘δ²‖x‖²，在远处至少为正常数。固定一个小δ就控制全部加权质量；再让δ下降，还会控制远尾逃逸。于是半径—方向上的有限测度真正紧，可以使用第24章的选择原理。漂移也不能任意逃走：去掉已控制的积分项后，若漂移无界，沿它的方向选一个趋0的频率，其相位却等于−1，与特征函数在原点共同连续矛盾。

抽出的极测度在正半径上还原ν，在原点层产生A，漂移给γ；连续核把参数极限转成特征函数极限。因此具有表示的分布类在弱收敛下封闭。这里没有先假设极限过程已经有独立的跳和Brownian部分。

最后把任意无限可分分布放进这个闭包。取它的n次卷积根，逐坐标减中位数，再减有界sin平均。对称化的局部特征函数给每项截断平方矩为O(1/n)，所以这些根在正确中心后无穷小。第14章的预算证明控制每行截断平方矩总和；Taylor余项使原行特征函数与伴随复合Poisson特征函数的对数差趋0。于是原分布是有表示的分布的弱极限，必要性完成。

这一步不能事先假定根的特征函数在全空间非零：那正是表示稍后才给出的推论。[参数证明第3–5节](../foundations/t-levy-characteristics.md#t-levy-budget)从原点附近的非零性开始，完整处理中心化、误差和参数抽取。

## 27.11 不求二阶导数，也能找回全部跳跃

<a id="levy-uniqueness"></a>

若二阶矩不存在，不能把指数求二阶导数来识别跳测度。有限差分却始终合法，因为两次差分自然产生一个压低小跳的非负权重。

\[
\begin{gathered}
-\{\Psi(u+v)+\Psi(u-v)-2\Psi(u)\}=\widehat M_v(u),\\
M_v=(v^\top Av)\delta_0+
2(1-\cos\langle v,x\rangle)\nu(dx).
\end{gathered}
\]

M是有限测度，所以第14章的Fourier唯一性适用。取每个坐标方向及其√2倍，两组权重之和在每个非零点都正：非零坐标不可能同时是2π整数与2π/√2整数。把测度相加，再在离零处除以这个严格正的权重，便恢复全部ν。

去掉跳积分以后，实部是一个确定的二次型，识别A的全部非对角元；虚部识别漂移。两个连续特征指数若给同一特征函数，差只能取2πi整数值，连通性及原点值0使差恒为0。唯一性因而包括指数、矩阵、跳测度和固定约定下的漂移，而不需要任何额外矩条件。

## 27.12 回到原来的路径，而不只另造一个模型

<a id="levy-ito"></a>

给定一条原本就在某概率空间上的Lévy过程，我们现在知道其单位时间分布有唯一三元组。时间1/n的特征函数与相应指数的比是连续的n次单位根，在原点等于1，故处处等于1。先由独立性得到有理时间指数，再用随机连续性扩到所有时间。其全部有限维分布与第7节的构造模型一致。

但同有限维律还不足以随口断言原空间已经有独立的Gaussian余项。需要从原路径本身读出跳，并证明这种读取可测。对任意càdlàg路径，在有限时间窗内只有有限个大于给定阈值的跳；否则跳时聚集会破坏某侧极限。它还能被有限阶梯函数一致逼近。

\[
\begin{gathered}
N_X=\sum_{s>0:\Delta X_s\ne0}\delta_{(s,\Delta X_s)},\\
\sum_i a(t_i)f(X_{t_i}-X_{t_{i-1}})
\longrightarrow \sum_{0<s\le T}a(s)f(\Delta X_s)
\end{gathered}
\]

后一式取二进划分、连续时间权a，以及连续紧支撑且在原点邻域为0的f。用有限阶梯逼近后，只有包含有限个阶梯边界的格子可能贡献；左右极限给出各格极限。先取整数T及有理二进网格，每个左式只用有理坐标，故跳测度是有理坐标的可测泛函。单调类再给全部Borel计数。

在构造模型上，不同环带几乎必然没有同时响铃；一致极限的跳量误差至多两倍一致范数，所以模型的实际跳正是原先放入的Poisson点。跳测度、补偿极限、连续余项都是联合可测泛函。同有理有限维律及π–λ就把这一整组事实传回给定X，得到原空间上的Lévy–Itô分解：

\[
\begin{gathered}
X_t=bt+C_t+
\int_{(0,t]\times\{\|x\|>1\}}x\,N_X(ds,dx)
+\lim_j\int_{(0,t]\times\{\varepsilon_j<\|x\|\le1\}}
x\,[N_X(ds,dx)-ds\,\nu(dx)],\\
C\text{ continuous centered Gaussian},\quad
E[C_sC_t^\top]=(s\wedge t)A,\quad C\perp\!\!\!\perp N_X .
\end{gathered}
\]

等式在同一个概率1事件上对全部时间成立，选定截断子列紧区间一致收敛，全部截断ucp收敛。若A退化，只断言协方差为A的连续余项存在，不替原空间凭空补出额外的标准Brownian坐标。[路径证明第4–6节](../foundations/t-levy-paths.md#t-levy-original-space)完整处理这些可测性和共同零集。

## 27.13 分布收敛时，哪些参数必须一同收敛

<a id="levy-triplet-convergence"></a>

Poisson逼近常会使某些跳缩到0，Gaussian极限又可能正从这些小跳出现。所以不能要求原来的Gaussian矩阵单独收敛到最终矩阵；应把尚未分辨的小跳协方差一起算进去。离零的跳测度收敛也不够，还须排除质量逃向无穷远。

\[
\begin{gathered}
\mathrm{ID}(\gamma_n,A_n,\nu_n)\Rightarrow\mathrm{ID}(\gamma,A,\nu)
\quad\Longleftrightarrow\\
\gamma_n\to\gamma,\qquad
\nu_n\xrightarrow{v}\nu\text{ on }\mathbb R^d\setminus\{0\},\\
\lim_{R\to\infty}\limsup_n\nu_n(\|x\|>R)=0,\\
\lim_{\varepsilon\downarrow0}\limsup_n
\left\|A_n+\int_{\|x\|\le\varepsilon}xx^\top\nu_n(dx)-A\right\|=0 .
\end{gathered}
\]

这里全部漂移使用第9节同一连续截断；小半径沿极限测度不给球面质量的值趋0。充分性将指数积分切为小球、紧环带和远尾：小球二阶Taylor余项由ε乘二阶质量控制，环带用vague收敛，远尾用第三项。必要性则对任意子列抽取有限加权测度，再用刚证的唯一性识别所有极限。[参数证明第7节](../foundations/t-levy-characteristics.md#t-levy-convergence)给出双极限的完整顺序。

在实线上它简化为γ收敛及有限canonical测度ρ的弱收敛。特别地，给定三元组，按越来越小的ε删除小跳，再调整漂移，复合Poisson加Gaussian分布便逼近原律。若还希望只用复合Poisson，Gaussian部分也可用对称小跳替代：沿矩阵特征方向放频率与步长，使频率乘步长平方等于相应特征值。

\[
\frac{\lambda}{2a^2}\delta_{a e}+
\frac{\lambda}{2a^2}\delta_{-a e}
\quad(a\downarrow0)
\quad\Longrightarrow\quad
\text{Gaussian covariance }\lambda\,ee^\top .
\]

这是分布与有限维时间律的逼近；本节没有额外宣称任意三元组收敛就已证明路径J₁收敛。后者仍需第24章的路径紧性控制。

## 27.14 阵列极限里，中心化不能随便省

<a id="levy-array-limits"></a>

第14章的三角阵列现在有了完整的识别工具。每行项独立，并满足无穷小条件；不要求同分布，也不要求原项均值存在。先逐坐标选中位数，再减有界sin平均。这个看似特别的中心选择，是为了消掉特征函数展开的一阶项，又只用始终存在的有界期望。

\[
\begin{gathered}
k=1,\ldots,r_n,\quad r_n<\infty,\qquad \max_{k\le r_n}P(\|Z_{nk}\|>\eta)\to0\quad(\eta>0),\\
Y_{nk}=Z_{nk}-m_{nk},\quad
b_{nk}=E(\sin Y_{nk,1},\ldots,\sin Y_{nk,d}),\quad
W_{nk}=Y_{nk}-b_{nk},\\
d_n=\sum_k(m_{nk}+b_{nk})-c_n,\quad
\nu_n=\sum_k\mathcal L(W_{nk})\big|_{\mathbb R^d\setminus\{0\}},\\
\gamma_n=d_n+\int h\,d\nu_n,\qquad A_n=0 .
\end{gathered}
\]

结论精确而实用：原行和减cₙ趋于某指定无限可分律，当且仅当这组三元组满足上一节四项判别。证明把每个正确中心后的项替换成Poisson次重复：其单项特征函数与1之差由截断二阶预算控制，全部对数余项由最大预算乘总预算控制而趋0。反方向从三元组条件先恢复预算有界，不能循环假定原行已经紧。[参数证明第5、9节](../foundations/t-levy-characteristics.md#t-levy-arrays)把两个方向实际写完。

为什么不直接把原项Poisson化？每行n个确定的1/√n，原总和减√n恒等于0；直接Poisson化却使总计数随机，错误地造出方差1的Gaussian波动。中位数中心使每个W恰为0，正确保留退化极限。这里决定成败的不是一个更漂亮的公式，而是确定位置与真实随机波动必须先分开。

## 27.15 跳得无穷多次，是否就走过无穷路程

<a id="levy-variation"></a>

将活动次数与路径总变差混为一谈，会漏掉两种不同的无限。ν总质量有限，当且仅当每个有限时间窗的跳数有限；这由Poisson计数直接得到。总质量无穷时，每个正长度有理时间窗的计数几乎必然无穷，但跳的绝对大小之和仍可能有限。

\[
\begin{gathered}
X\text{ has finite variation on every compact interval a.s.}\\
\Longleftrightarrow\quad
A=0,\qquad
\int_{0<\|x\|\le1}\|x\|\,\nu(dx)<\infty .
\end{gathered}
\]

充分性很具体：Campbell公式给小跳绝对和有限，可以把补偿重新并入一条有限线性漂移。必要性也不只是一句“Brownian粗糙”：若小跳绝对积分无穷，Poisson Laplace公式使绝对跳和几乎必然无穷，而任一càdlàg路径的变差至少为全部跳量范数之和。

若Gaussian矩阵非零，取一项正方差投影。固定一条跳路径，假如加上Gaussian以后有正概率成为有限变差，就取两份独立Gaussian加同一条跳路径；两条都有限变差有正概率，其差便是一份非零缩放Brownian的有限变差事件，违反第26章。对跳路径Fubini积分完成论证。[路径证明第7节](../foundations/t-levy-paths.md#t-levy-variation)逐步给出这个不借一般二次变差的证明。

\[
\begin{gathered}
d=b-\int_{\|x\|\le1}x\,\nu(dx),\qquad
X_t=dt+\sum_{s\le t}\Delta X_s
\quad\text{in the finite-variation case}.
\end{gathered}
\]

单位区间上密度1/x的正跳测度，总质量无穷而一阶积分有限，给出无限活动、有限变差。密度1/x²仍满足Lévy平方条件，却不满足一阶条件，补偿以后是无限变差。相同的“只有正跳”外观，隐藏着完全不同的求和机制。

## 27.16 没有负跳，也未必一直向上

<a id="levy-subordinator"></a>

等待与累计输入常需要单调运动。实值Lévy过程若路径非降，称为subordinator；这里从0出发、不杀死、寿命无穷。单调性强迫有限变差，于是前一节已经除去Gaussian部分和不可绝对求和的小跳，还强迫跳测度只在正半轴。剩下的条件是实际线性漂移非负。

\[
\begin{gathered}
A=0,\quad \nu((-\infty,0))=0,\quad
\int_{(0,1]}x\,\nu(dx)<\infty,\quad
d=b-\int_{(0,1]}x\,\nu(dx)\ge0,\\
E e^{-qX_t}=
\exp\!\left[-t\left(dq+\int_{(0,\infty)}(1-e^{-qx})\nu(dx)\right)\right],
\quad q\ge0.
\end{gathered}
\]

这些条件也充分，普通正跳和就构造出单调路径。漂移非负的必要性不能仅从“看起来如此”得到：把短时间正跳和按阈值ηt分开，大跳出现概率及小跳和除t后的均值都趋0，故跳和除t依概率趋0。于是Xₜ/t依概率趋d，非负性迫使d≥0。这个估计只用小跳一阶可积及大跳有限质量，不要求大跳均值。

例如仅在(0,1)取密度1/x²、按本章方式补偿且b=0，过程均值0、方差t、非退化。若它总非负，均值0就会迫使它恒为0，矛盾。因此正跳并没有免除负向补偿。Lévy测度描述离散跳的方向，完整路径方向还取决于补偿与漂移。

## 27.17 稳定律不再只是一列例子

<a id="levy-stable"></a>

第14章通过重尾求和构造了新的稳定分布，却把“还可能有哪些稳定律”留作主证责任。现在可以不猜特征函数的形状，而让表示的唯一性反过来限制尺度。稳定律任意多个独立副本相加只改变位置与尺度；它无限可分，所以有连续卷积族。

收敛类型引理保证尺度与平移不能在相同非退化极限下任意变动。有理时间的稳定关系先扩到实时间，卷积族的时间乘法迫使尺度函数连续且可乘，故为一个幂。协方差与跳测度分别比较时间伸缩和空间伸缩，得到

\[
\begin{gathered}
a(t)=t^{1/\alpha},\qquad
t\sigma^2=t^{2/\alpha}\sigma^2,\qquad
\nu(rB)=r^{-\alpha}\nu(B),\\
0<\alpha<2:\quad
\nu(dx)=
\bigl(c_+\mathbf1_{\{x>0\}}+c_-\mathbf1_{\{x<0\}}\bigr)
|x|^{-1-\alpha}\,dx,\quad \sigma^2=0,\\
c_\pm\ge0,\quad c_++c_->0;\qquad
\alpha=2:\quad \nu=0,\quad\sigma^2>0.
\end{gathered}
\]

这里的尺度乘法来自对同一指数的两次运算。先用时间t的仿射表达，再将其卷积指数乘s，便得到

\[
st\Psi(u)=\Psi(a(s)a(t)u)
+iu\{a(t)b(s)+s b(t)\}.
\]

它与时间st的仿射表达描述同一非退化分布，正尺度与平移的唯一性才迫使a(st)=a(s)a(t)。时间连续性把这种乘法关系变成幂函数；Gaussian协方差与跳测度随后必须服从同一个尺度，而非各自任意选择。

跳密度不是预先假定的。齐次性先给两侧尾为幂函数，再对区间作差才得到密度；小跳平方条件强迫α<2。非零Gaussian方差则强迫α=2。两者都没有只剩确定平移，与非退化矛盾。这穷尽全部非退化实稳定律，不以Cauchy一个例子冒充一般结论。

α=1的中心尤其不能略去。记两侧密度常数之差为Δ，尺度换元后截断边界留下一项对数。它不是计算误差，也不能由一个固定位置平移消除。

\[
\alpha=1:\qquad Z_1+\cdots+Z_n
\overset d=nZ+n(c_+-c_-)\log n .
\]

对称时对数项消失；α≠1可选适当固定中心取得严格稳定。密度常数与尾常数相差α这一因子，也必须保持：[完整分类及中心证明](../foundations/t-levy-domains.md#t-levy-stable-classification)从收敛类型到所有参数逐步给出。这里的稳定是分布在独立求和下的自相似性，不是单条路径在放大后保持不变。

## 27.18 从极限还原尾部：吸引域的反方向

<a id="levy-attraction"></a>

构造一份稳定律只是问题的一半。给定原始变量，哪些尾会把独立和送向它？充分性说明一种机制能够发生；必要性才说明别的尾部行为不能偷偷产生同一个完整序列极限。对非Gaussian稳定极限，答案由绝对尾的正则变化和两侧尾平衡共同给出。

\[
\begin{gathered}
F(x)=P(|Z|>x)\text{ regularly varying with index }-\alpha,\quad0<\alpha<2,\\
\frac{P(Z>x)}{F(x)}\to p_+,\qquad
\frac{P(Z<-x)}{F(x)}\to p_-,\qquad p_++p_-=1,\\
nF(a_n)\to C>0,\qquad c_\pm=\alpha C p_\pm,\\
c_n=a_n\{nE h(Z/a_n)-\gamma\}
\quad\Longrightarrow\quad
\frac{S_n-c_n}{a_n}\Rightarrow\mathrm{ID}(\gamma,0,\nu_\alpha).
\end{gathered}
\]

这个中心只用有界函数，因此均值不存在也仍有意义。离零尾极限识别ν，小跳截断二阶矩由正则变化界压到ε的一个正幂，远尾由R的负幂压住，三元组判别便给充分性。不过在使用原项Poisson化以前，还要证明对数误差消失；适当q阶绝对矩给n乘单项特征误差平方趋0。

反方向不能先假定尾正则变化。对已经收敛的独立和，先使用正确中位数中心的阵列判别，识别缩放尾在每个非零阈值的极限。收敛类型给相邻尺度比趋1；首次越过任意大阈值的指标将尺度序列上的尾极限扩成全部实阈值上的正则变化。这才允许回到原项中心，得到同一漂移条件的必要性。

因此这里证明的是完整实值稳定吸引域的充要条件，不只重复第14章的重尾构造。[吸引域证明第4–5节](../foundations/t-levy-domains.md#t-levy-stable-domain-sufficient)写出分位数尺度、截断界、移动阈值及全部中心化步骤。若尾在不同尺度间振荡而无正则变化，局部若干子列仍可能近似某个稳定形状，却不能据此宣称整列进入同一吸引域。

精确指定cₙ的等式只是一个方便选择；一般中心的必要且充分条件为下面的极限。

\[
nE h(Z/a_n)-c_n/a_n\longrightarrow\gamma.
\]

## 27.19 无穷方差，也可能留下Gaussian

<a id="levy-normal-domain"></a>

“有限方差给Gaussian、无穷方差给非Gaussian”并不正确。真正控制极限的是所选尺度上可见的大跳与未分辨小波动。某些无穷方差尾很薄：在适当尺度上大跳全部消失，截断二阶质量却累积成一个非零原点原子。

\[
\begin{gathered}
\mu=EZ,\qquad V(x)=E[(Z-\mu)^2\mathbf1_{\{|Z-\mu|\le x\}}],\\
\frac{S_n-c_n}{a_n}\Rightarrow N(\ell,\sigma^2),\quad\sigma^2>0\\
\Longleftrightarrow\
\begin{cases}
E|Z|<\infty,\quad V\text{ slowly varying},\quad a_n\to\infty,\\
nV(a_n)/a_n^2\to\sigma^2,\quad(n\mu-c_n)/a_n\to\ell.
\end{cases}
\end{gathered}
\]

这里Z非退化、各项独立同分布、aₙ为正；右侧的V在均值已存在后定义。慢变包含趋向有限正常数的有限方差情形，也容许V缓慢趋向无穷。其尾部意义是：x²乘超过x的尾概率，相对V(x)趋0。全部可见大跳消失，剩下的二阶质量就是Gaussian方差。

必要性不能暗中先假设均值存在。先取独立差Z−Z′，其中心自动为0；canonical测度向原点聚集，给差变量的截断二阶矩慢变。二进尾积分再证明差变量一阶可积，中位数尾界把一阶可积传回Z；此后才能减均值，并证明原变量截断方差渐近为差变量的一半。充分性则用同一尾界控制大跳、漂移与对数余项。[证明第6–8节](../foundations/t-levy-domains.md#t-levy-normal-tail)完整处理这些方向。

\[
\begin{gathered}
f(y)=|y|^{-3}\mathbf1_{\{|y|\ge1\}},\qquad
EY=0,\quad EY^2=\infty,\quad V(x)=2\log x\ (x\ge1),\\
a_n=\sqrt{n\log n}\quad(n\ge2),\qquad
\frac{Y_1+\cdots+Y_n}{a_n}\Rightarrow N(0,1).
\end{gathered}
\]

这个密度已经归一化。平方根时间并非Gaussian极限唯一可能的原始归一化；它是单位方差输入的一种特例。缓慢增长的截断方差改变了尺度，却没有留下离零跳测度。这把Gaussian与稳定重尾极限放到同一套参数收敛机制里，而没有抹去两者的差异。

## 27.20 越过一个高度以后，为什么不能照搬反射

<a id="levy-ladders"></a>

Brownian第一次碰到高度时恰好位于那个高度，连续性使反射有精确的拼接点。跳跃运动可能一下越过它；越过量与后续位置产生新的结构，Brownian反射公式不能原样照搬。先回到离散随机游走，可以把这个困难看得最清楚。

先固定符号：R是末点相对最大值的有符号位移，D才是通常非负的回落量（drawdown）。

\[
M_n=\max_{0\le j\le n}S_j,\qquad
R_n=S_n-M_n\le0,\qquad D_n=M_n-S_n=-R_n\ge0.
\]

取独立的几何观察时刻N，概率为(1−z)zⁿ，0<z<1。每条有限路径第一次取得全局最大值的位置唯一：此前是严格新高，之后全部相对部分和不正。几何权重又恰好在这点左右分解，于是\(M_N\)与\(R_N\)独立，因而也与\(D_N\)独立。固定时刻一般不独立：一步对称游走的(M₁,R₁)为(1,0)或(0,−1)；若写非负回落，(M₁,D₁)则为(1,0)或(0,1)。

\[
\begin{gathered}
T^+=\inf\{n\ge1:S_n>0\},\quad
T^-=\inf\{n\ge1:S_n\le0\},\\
F_\pm(z,u)=E[z^{T^\pm}e^{iuS_{T^\pm}};T^\pm<\infty],\\
1-z\phi_Z(u)=\bigl(1-F_+(z,u)\bigr)\bigl(1-F_-(z,u)\bigr).
\end{gathered}
\]

这就是本章承担的离散Wiener–Hopf乘积。为什么一边严格、一边容许相等？因为选的是第一次全局最大值；平手必须留给后半。反转后半的增量，路径“不正前缀”恰转为“末点弱新低”，再由停止后独立性把两半分别写成严格上升及弱下降梯级的更新级数。每个梯级变换模至多z，级数绝对收敛；乘回几何末点特征函数便得公式。

若把两边都写严格，恒为0的增量已经给出反例。[梯级证明第9节](../foundations/t-levy-domains.md#t-levy-wiener-hopf)从唯一路径拆分到完整变换逐式证明，容许格点、平手及无穷梯级时间。这里不把z直接置1，也不把这份离散结论冒称全部连续时间涨落理论。它揭示的是：跳跃以后，越界问题需要记录高度与等待时间，连续反射只是更特殊的一种几何。

## 27.21 表示定理的历史与我们采用的证明

<a id="levy-history"></a>

这份表示连接了两条原本可以分别研究的路线：独立随机变量之和的极限，以及随时间展开的独立增量运动。Lévy的1934年原文《Sur les intégrales dont les éléments sont des variables aléatoires indépendantes》刊于《Annali della Scuola Normale Superiore di Pisa》，原刊数字版保存在Numdam。Khintchine的1937年论文《Zur Theorie der unbeschränkt teilbaren Verteilungsgesetze》则以无限可分分布为题，MathNet保留官方书目及原文入口。

这些是可核查的原始文献入口，不意味着本章的每个中间引理或当前记号都出自某一篇原文。本章以现代测度、紧性、可数坐标和L²工具重建证明；有限维参数紧性、原空间跳泛函转移及吸引域补证按本书已经建立的依赖重新组织。相关构造还可与Winkel本人Oxford讲义中Poisson随机测度及补偿过程部分对照。

**原始文献与数学证明。** [Lévy 1934原刊](https://www.numdam.org/item/ASNSP_1934_2_3_3-4_337_0/)；[Khintchine 1937官方档案](https://www.mathnet.ru/eng/sm5562)；[Winkel本人讲义](https://www.stats.ox.ac.uk/~winkel/ms3b10.pdf)；[参数、唯一性与阵列证明](../foundations/t-levy-characteristics.md)；[跳路径及原空间分解证明](../foundations/t-levy-paths.md)；[稳定分类、吸引域与梯级证明](../foundations/t-levy-domains.md)。

## 27.22 同一种增量规律，可以有不同的路径面貌

<a id="levy-conclusion"></a>

章首那排时钟没有被删去任何一个。我们改变的是求和的方式：可见大跳按实际位置相加，密集小跳先在有限尺度补偿，再以共同上确界控制解除截断。若它们的二阶质量挤到0，留下连续Gaussian部分；若离零仍留有质量，就留下能够逐个辨认的跳。漂移说明我们怎样给这次求和选择位置。

因此Brownian与Poisson不是两种互不相关的偶然例子。它们分别显露同一结构的不同部分，而稳定律进一步显示尾与尺度怎样决定这些部分在放大后还剩多少。连续性、有限活动、有限变差、只有正跳和真正单调，是彼此不同的性质；一个特征指数把它们放在同一张可核查的地图上，却不替我们取消它们的区别。

本章的增量仍与所在位置无关。若粒子走到另一个区域，下一小段的运动规则也随之改变，单个指数就不再足以记录全部演化。刚才依靠独立增量完成的拼接，必须换成能够随状态变化的转移规律；同时，时间连续与路径正则性仍需要证明。我们已经学会从局部跳频率构造整条运动，接下来要理解局部运动规则怎样作用在观察函数上。
