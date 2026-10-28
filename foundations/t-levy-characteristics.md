# T-LEVY-CHARACTERISTICS：三元组、紧性与无穷小阵列

本专题完成[第27章](../chapters/27-levy-processes.md#levy-khintchine)的分布级主证。状态空间为有限维实向量空间。使用第11、14章的特征函数唯一性/连续性、第24章有限测度的紧性选择以及第14章的中位数中心化机制；不用随机积分、Lévy–Itô分解或第49章的一般随机测度极限。

## 1. 连续截断与一个有限的替代测度

<a id="t-levy-canonical"></a>

\[
\begin{gathered}
h(x)=\frac{x}{1+\|x\|^2},\qquad w(x)=\frac{\|x\|^2}{1+\|x\|^2},\qquad x\in\mathbb R^d,\\
\Psi(u)=i\langle\gamma,u\rangle-\tfrac12u^\top Au+
\int_{x\ne0}(e^{i\langle u,x\rangle}-1-i\langle u,h(x)\rangle)\nu(dx),\\
A=A^\top\ge0,\qquad \nu(\{0\})=0,\qquad
\int(1\wedge\|x\|^2)\nu(dx)<\infty.
\end{gathered}
\]

小跳测度可能有无穷总质量，不能直接对它用概率测度紧性。乘上w便成为有限测度。向量情形还要保留趋于零的方向：把非零点写成半径r与单位方向θ，将wν推到[0,∞)乘单位球面上，原来暂不在零层放质量。

\[
\begin{gathered}
K_u(r,\theta)=
\frac{e^{ir\langle u,\theta\rangle}-1-
i\,r\langle u,\theta\rangle/(1+r^2)}{r^2/(1+r^2)}\quad(r>0),\\
K_u(0,\theta)=-\tfrac12\langle u,\theta\rangle^2.
\end{gathered}
\]

Taylor余项说明这个核连续且有界。对r≤1，分子先减去线性项，余项至多常数乘r²，连续截断与rθ的差是O(r³)；对r≥1，分母至少1/2，分子有统一界。对有界频率集合，核也有共同上界，并在每个紧的半径—方向集合上随频率趋0而一致趋0。

Gaussian矩阵可在零层表示：取其谱分解，在相应单位特征方向放特征值大小的质量。反过来，零层测度对θθ转置的积分给一个半正定矩阵。零层的角分布未必唯一，唯一的物理参数是矩阵A；不可把它叫作跳测度在原点的原子。

## 2. 先证明给定参数确实产生概率

<a id="t-levy-sufficiency"></a>

把ν限制到半径超过ε的区域，得到有限测度。用第13、21章的复合Poisson和、独立Gaussian向量及确定平移，构造下面的特征函数；截断后的漂移积分有限。

\[
\exp\!\left\{i\left\langle\gamma-\int_{\|x\|>\varepsilon}h(x)\nu(dx),u\right\rangle
-\tfrac12u^\top Au+
\int_{\|x\|>\varepsilon}(e^{i\langle u,x\rangle}-1)\nu(dx)\right\}.
\]

当ε下降到0，二阶余项支配给指数趋向Ψ。用第1节的有限极测度和核的有界性，DCT说明Ψ在频率0连续且为0。第14章多元连续性定理因此给一份真正的概率，特征函数是exp Ψ。将全部参数除以任意正整数，重复同一构造，再把特征函数相乘，得到无限可分性。这里没有把一个形式指数直接宣布为概率。

## 3. 概率紧性怎样控制跳跃和Gaussian质量

<a id="t-levy-budget"></a>

设一列上述三元组的分布弱收敛；有限复合Poisson加漂移是其中的特例。紧性给其特征函数在频率0附近一致趋于1：先把随机向量限制在共同的大球内，再用指数函数的Lipschitz界，球外误差至多尾概率的两倍。因而小δ时，下式有限且趋于0。有限个开头也在同一族中处理。

\[
\begin{gathered}
a(\delta)=\sup_n\sup_{\|u\|_\infty\le\delta}
[-\log|\phi_n(u)|]\longrightarrow0,\\
\frac{\delta^2}{6}\operatorname{tr}(A_n)+
\int\left[1-\prod_{j=1}^d\operatorname{sinc}(\delta x_j)\right]\nu_n(dx)
\le a(\delta).
\end{gathered}
\]

第二行是把负对数模在频率立方体上平均，Tonelli适用，因为Gaussian二次型与1减cos均非负。sinc在0取1。存在只依赖维度的正常数，使方括号至少为该常数乘min(δ²‖x‖²,1)：零附近用Taylor；远处至少一个坐标足够大；中间紧环上乘积严格小于1。固定一个小δ，便同时控制Gaussian迹与w加权的跳质量。

\[
\sup_n\left[\operatorname{tr}(A_n)+\int w\,d\nu_n\right]<\infty,\qquad
\nu_n(\|x\|>2\sqrt d/\delta)\le2a(\delta).
\]

第二项是独立的远尾控制，不能从第一项总质量有界偷推出。半径与球面乘积是Polish空间，球面紧。将总质量补到一个固定常数并加一个孤立点，化为概率；第24章Prokhorov遂给极测度的弱收敛子列。孤立点只处理缺少的总质量，不会被误算作Gaussian质量。

## 4. 漂移也不能逃到无穷远

<a id="t-levy-drift"></a>

记核对极测度的积分为J。质量有界与远尾紧性，使这些J在频率0附近一致趋0：大半径外用核共同界，紧集内用核一致连续。于是exp(i〈u,γ〉)=φ(u)exp(−J(u))也一致趋1。如果漂移范数沿子列趋于无穷，取u=πγ/‖γ‖²，频率趋0而这个指数恰等于−1，矛盾。因此漂移有界。

抽出漂移收敛、极测度弱收敛的共同子列。固定频率的核有界连续，所以极限指数仍是第1节形式：正半径部分给ν，零层给A。有限极质量保证ν满足Lévy条件。我们已证明三元组类在弱极限下闭合，尚未在此处假设极限参数唯一。

## 5. 每份无限可分分布都能进入这个极限

<a id="t-levy-necessity"></a>

先把第14章的伴随复合Poisson论证明确推广到向量。这里每行只含有限项：k=1,…,rₙ，rₙ<∞；行内独立，无穷小指对每个η>0，行内超过η的最大概率趋0。若经过确定中心cₙ的行和收敛，各坐标行和也紧。逐坐标取中位数，利用14.20对独立差的sinc预算，得到以下向量预算；最后的不等式使逐坐标控制确实控制向量。

\[
\begin{gathered}
Y_{nk}=Z_{nk}-m_{nk},\quad
v_{nk}=E(1\wedge\|Y_{nk}\|^2),\quad b_{nk}=E(\sin Y_{nk}),\quad
W_{nk}=Y_{nk}-b_{nk},\\
\sup_n\sum_kv_{nk}<\infty,\qquad\max_kv_{nk}\to0,\qquad
1\wedge\|y\|^2\le\sum_j(1\wedge y_j^2)\le d(1\wedge\|y\|^2).
\end{gathered}
\]

sin逐坐标取值。中位数尾界来自独立副本落在中位数另一侧至少一半概率，因此截断二阶矩至多独立差预算的两倍。无穷小性使中位数与Y都一致趋于0，故最大预算趋0；这些论证不需要均值或方差存在。

\[
\begin{gathered}
|e^{i\langle u,y\rangle}-1-i\langle u,\sin y\rangle|
\le C_u(1\wedge\|y\|^2),\qquad \|b_{nk}\|^2\le d\,v_{nk},\\
\theta_{nk}(u)=Ee^{i\langle u,W_{nk}\rangle},\qquad
|\theta_{nk}(u)-1|\le C'_u v_{nk},\qquad
\sum_k|\theta_{nk}(u)-1|^2\to0 .
\end{gathered}
\]

第一个界在单位球内由Taylor相消线性项，在球外由有界sin得到；乘以减中心的相位后仍有相同阶数的界。对数只在1附近选择，且其实部总和非正，故14.21的误差估计逐字适用于向量内积。下面的Q因此与原行和有同一个弱极限。它是真正的有限复合Poisson加漂移。

\[
\begin{gathered}
d_n=\sum_k(m_{nk}+b_{nk})-c_n,\\
Q_n(u)=\exp\left\{i\langle u,d_n\rangle+
\sum_k(\theta_{nk}(u)-1)\right\}.
\end{gathered}
\]

对任意无限可分向量分布，取其n次卷积根。无需先假定特征函数处处非零：在每条坐标轴的固定小频率区间，原特征函数模大于1/2，根的独立差满足下面的界。sinc平均便给各坐标对称截断矩O(1/n)，中位数中心后的根趋于0。用n个这样的根组成一行，加回确定的中位数平移，行和恒有原分布。

\[
1-|\phi_{\mathrm{root},n}(t e_j)|^2
=1-|\phi_\mu(te_j)|^{2/n}
\le-\frac2n\log|\phi_\mu(te_j)|
\quad(|t|\le\delta).
\]

这就得到一列伴随复合Poisson分布收敛到原分布。第3–4节的紧性与参数抽取给出LK表示，必要性完成。特征函数全空间非零现在是表示的推论，而不是证明中的隐藏假设。

根的中心不能在这一步丢掉。设Vₙ是n次根，mₙ为中位数向量，Yₙ=Vₙ−mₙ，bₙ=E sin Yₙ，Wₙ=Yₙ−bₙ。局部sinc界给vₙ=E(1∧‖Yₙ‖²)=O(1/n)，所以对每个固定u有如下精确恒等式与误差界。

\[
\begin{gathered}
\theta_n(u)=Ee^{i\langle u,W_n\rangle},\qquad
\phi_\mu(u)=e^{i\langle u,n(m_n+b_n)\rangle}\theta_n(u)^n,\\
n|\theta_n(u)-1|^2=O(n^{-1}),\qquad
\left|\phi_\mu(u)-
e^{i\langle u,n(m_n+b_n)\rangle+n(\theta_n(u)-1)}\right|\to0 .
\end{gathered}
\]

在1附近取log，余项至多常数乘|θₙ−1|²；伴随指数的实部非正，故相乘后的特征函数误差至多exp(Cn|θₙ−1|²)−1。确定相位始终模为1，不要求n mₙ有界。例子μ=δₐ的根为a/n处的点质量，Wₙ恒0，全部位置由n mₙ=a保存；漏去相位会把δₐ错误变成δ₀。

## 6. 不用二阶矩，也能识别唯一参数

<a id="t-levy-uniqueness"></a>

相同特征函数若有两个连续指数，二者之差取值于2πi整数，且在0为0；实向量空间连通，故指数相同。现在做有限差分，不对指数求二阶导数。

\[
\begin{gathered}
-\{\Psi(u+v)+\Psi(u-v)-2\Psi(u)\}=\widehat M_v(u),\\
M_v=(v^\top Av)\delta_0+2(1-\cos\langle v,x\rangle)\nu(dx).
\end{gathered}
\]

这个测度有限：小跳权重是O(‖x‖²)，大跳权重有界。第14章有限测度Fourier唯一性识别每个M。取方向v为每个坐标单位向量以及它的√2倍；全部相应权重之和在非零点严格正，因为一个非零坐标不可能同时是2π整数与2π/√2整数。相加后在非零点除以这个正权重，便唯一恢复整个ν，允许其总质量无穷。

去掉已识别的跳积分，实部唯一确定二次型及A的全部非对角元，虚部唯一确定γ。只凭坐标方向的零点原子不能声称识别了非对角元。表示因此唯一到三元组，而不是唯一到人为选取的零层角分布。

## 7. 三元组怎样收敛

<a id="t-levy-convergence"></a>

所有漂移采用同一个连续截断h。离零vague收敛只指：对非零空间中每个连续紧支撑函数，测度积分收敛。它不保证远尾没有逃逸，也不记录聚到零点的二阶波动。正确的完整判别是下列四项，其中球半径沿ν不给球面质量的值趋于0。

\[
\begin{gathered}
\mathrm{ID}(\gamma_n,A_n,\nu_n)\Rightarrow
\mathrm{ID}(\gamma,A,\nu)\\
\Longleftrightarrow\
\gamma_n\to\gamma,\quad \nu_n\xrightarrow{v}\nu\text{ on }\mathbb R^d\setminus\{0\},\\
\lim_{R\to\infty}\limsup_n\nu_n(\|x\|>R)=0,\\
\lim_{\varepsilon\downarrow0}\limsup_n
\left\|A_n+\int_{\|x\|\le\varepsilon}xx^\top\nu_n(dx)-A\right\|=0.
\end{gathered}
\]

充分性把指数积分切成小球、中间环带与远尾。小球上核的未除权版本等于−〈u,x〉²/2加O_u(‖x‖³)，误差积分至多C_u ε乘小球二阶矩；协方差条件同时给这个矩的有界性。环带由vague收敛及无质量的边界识别，远尾由第三项及有界核分子消除。先n趋于无穷，再缩小ε、扩大R，得到每个指数收敛；连续性定理完成。

必要性先用第3–4节，对任意子列再抽取极测度和漂移极限。第6节唯一性迫使每个此类极限有同一γ、A、ν。远尾界已由a(δ)得到；固定无质量球面的半径时，实际测试的是半径r≤ε上(1+r²)θθ转置，包含r=0层；其积分正是Aₙ加小球跳协方差。这个整体收敛，随后半径趋0便得双极限，不能只对正半径部分单独断言收敛。反之若四项之一失败，选违反它的子列，再作相同抽取，就与已识别的参数矛盾。这也说明为什么多元情形不能把某一个零层角测度的弱收敛列为必要条件。

把最后的量词写清楚。对固定的无球面质量半径ε，极坐标测试函数为(1+r²)θθ转置乘{r≤ε}指标；它包含零层。用连续径向截断逼近指标，误差由ε附近薄环的质量控制，极限测度不给该球面质量，故误差趋0。任一子列都可再抽取并得到相同的矩阵极限；若整列不收敛，选距离该极限有固定间隔的子列就会矛盾。因此先得到整列在固定ε的收敛，再令ε下降：

\[
\begin{gathered}
Q_n(\varepsilon)=A_n+\int_{0<\|x\|\le\varepsilon}xx^\top\nu_n(dx),\\
Q_n(\varepsilon)\longrightarrow
A+\int_{0<\|x\|\le\varepsilon}xx^\top\nu(dx),\\
\limsup_n\|Q_n(\varepsilon)-A\|=
\left\|\int_{0<\|x\|\le\varepsilon}xx^\top\nu(dx)\right\|
\longrightarrow0\quad(\varepsilon\downarrow0).
\end{gathered}
\]

最后一项趋0由Lévy二阶可积性及支配收敛，不交换n与ε的次序。检验这一零层步骤的例子是实线测度在±1/n各放n²/2质量、Gaussian参数为0；它的指数为n²(cos(u/n)−1)，极限为−u²/2。原来全是跳，最终的Gaussian方差却为1。

## 8. 实线上的有限canonical测度

<a id="t-levy-real-canonical"></a>

\[
\begin{gathered}
\rho=\sigma^2\delta_0+w(x)\nu(dx),\qquad
K_u(x)=\frac{e^{iux}-1-iu x/(1+x^2)}{x^2/(1+x^2)},\
K_u(0)=-u^2/2,\\
\mathrm{ID}(\gamma_n,\rho_n)\Rightarrow\mathrm{ID}(\gamma,\rho)
\quad\Longleftrightarrow\quad
\gamma_n\to\gamma,\quad \rho_n\Rightarrow\rho
\quad\text{as finite measures on }\mathbb R.
\end{gathered}
\]

在实线上，零点两种方向给相同的平方，因此可以合并成唯一原子。充分性由有界连续K积分直接得到。必要性由第3–4节紧性抽取，再由唯一性识别所有子列。这里有限测度弱收敛测试全部有界连续函数，包括常数1，因而记录总质量。它容许离零质量聚到原点，却不要求每个ρₙ在原点的原子质量收敛到ρ的原子；上一节的对称小跳例子中，前者恒0、后者为1。有限测度弱收敛同时记录总质量和原点附近质量的聚集；ν自身的离零vague收敛不具备这些信息。

## 9. 一般无穷小阵的精确判别

<a id="t-levy-arrays"></a>

采用第5节逐坐标的中位数、sin中心及W，下面的ν每行虽然总质量有限，却可能在零附近有大量质量。去掉零点原子不改变任何指数积分。

\[
\begin{gathered}
\nu_n=\sum_k\mathcal L(W_{nk})\big|_{\mathbb R^d\setminus\{0\}},\qquad
\gamma_n=d_n+\int h(x)\nu_n(dx),\qquad A_n=0.
\end{gathered}
\]

原中心化行和趋于给定LK分布，当且仅当这组三元组满足第7节四项条件。必要性来自伴随复合Poisson收敛。充分性还需补回第5节的二阶预算，而不能循环假定原行已经紧。对充分大的行，每个sin中心坐标绝对值≤1；负的这个坐标是W相应坐标的中位数，故下列估计成立。

\[
\begin{gathered}
Ew(\|W_{nk}\|)\ge b_{nk,j}^{\,2}/4,\qquad
v_{nk}\le(4+8d)\,Ew(\|W_{nk}\|).
\end{gathered}
\]

第一界用中位数一侧至少一半概率及w(b)≥b²/2。第二界用Y=W+b、截断平方的三角界，以及min(‖W‖²,1)≤2w(‖W‖)。四项条件在一个小球和外环上控制加权总质量，所以预算总和有界。无穷小性再给最大预算趋0，对数误差遂消失。实值情形等价于第8节canonical测度判别。

不能删去中心化再套公式。例如每行n个确定项1/√n，总和减去√n恒为0；若把这些原项直接泊松化，反而制造出趋于方差1的随机波动。正确的中位数中心使每个W恰为0，留下的极限也确实是0。

这个错误极限可以直接算，而不靠方差猜测：

\[
\exp\!\left\{n(e^{iu/\sqrt n}-1)-iu\sqrt n\right\}
\longrightarrow e^{-u^2/2}.
\]

这里恢复预算的三段估计如下。先取足够小的连续性半径0<ε<1，使Qₙ(ε)的范数最终有界；这些矩阵半正定，迹也有界。再取大R，使远尾质量最终小于1。在非零空间取连续紧支撑f，全空间0≤f≤1，并在ε≤‖x‖≤R恒为1。由于小球上w≤‖x‖²、其余地方w≤1，有

\[
\int w\,d\nu_n\le
\operatorname{tr}Q_n(\varepsilon)+\int f\,d\nu_n+
\nu_n(\|x\|>R).
\]

三项分别由小球条件、vague收敛及远尾条件控制。有限个初始行各自是有限测度，可合并进共同上界。结合前述(4+8d)界，得到Σₖvₙₖ有界；再用最大vₙₖ趋0，Σₖ|θₙₖ−1|²才确实趋0。这证明充分方向，而不是重新假定原行和已经紧。有限行的限制是本判别的一项假设；若改成可数无穷行，还须另建随机级数及无限乘积的论证。

## 10. 截断改变的是漂移记账，而不是跳跃

<a id="t-levy-truncation"></a>

\[
\begin{gathered}
\chi(x)=x\mathbf1_{\{\|x\|\le1\}},\qquad
b=\gamma+\int(\chi-h)\,d\nu,\\
\Psi(u)=i\langle b,u\rangle-\tfrac12u^\top Au+
\int(e^{i\langle u,x\rangle}-1-i\langle u,\chi(x)\rangle)\nu(dx).
\end{gathered}
\]

转换积分绝对收敛：小球上χ−h是O(‖x‖³)，球外h有界而ν质量有限。更一般地，两个截断均须为全空间有界Borel函数，且各自与x在原点附近相差O(‖x‖²)。两者之差在小球二阶可积，在离零处有界且ν质量有限，故同一计算给出绝对收敛的漂移差。连续截断便于参数收敛，单位球截断便于路径上的大跳/小跳分工；二者不能混用同一个未经转换的漂移。
