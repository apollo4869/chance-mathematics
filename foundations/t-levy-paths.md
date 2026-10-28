# T-LEVY-PATHS：跳测度、补偿极限与原空间分解

本专题补全[第27章](../chapters/27-levy-processes.md#levy-ito)的路径证明。给定有限维Lévy三元组，先实际构造路径；对任意已经具有càdlàg路径的Lévy过程，再恢复其本身的跳测度与独立Gaussian余项。只需有理坐标σ-代数，不以J₁拓扑的Polish性或紧性定理为前提，也不使用随机可预测积分。

## 1. 从独立带构造计数测度

<a id="t-levy-prm"></a>

把非零标记空间分成可数个有限ν质量的Borel带。每带用第21章的Poisson时钟，速率等于该带质量；标记独立，分布为该带归一化的ν。零质量带为空。第8、10章的可数乘积使所有带与独立Gaussian过程共存。对时间与标记的Borel集合，令N计数这些原子，允许无穷。每条实现都是可数个Dirac测度之和，故可数可加。

给定一个有限窗口内的时钟计数，第21章给到达时间为独立均匀时间排序。加入独立标记后，对一个带内的非负可测函数f，条件期望是一个单点积分的计数次幂。再用Poisson母函数，得到下式。先处理有限窗口和有限带数，再用MCT扩展；不要求f有有限积分。

\[
\begin{gathered}
\mu(ds,dx)=ds\,\nu(dx),\qquad
Ee^{-N(f)}=\exp\!\left[-\int(1-e^{-f})\,d\mu\right],\\
E N(f)=\int f\,d\mu\quad(f\ge0).
\end{gathered}
\]

第二式也可直接由简单函数、单带计数均值与MCT得到。对互不相交的有限强度集合，令f为各指标的非负线性组合，第一式分解为Poisson计数的联合Laplace变换；各计数为非负整数，联合PGF幂级数系数逐坐标唯一（逐次用第13章的一维唯一性），所以联合律是Poisson乘积律，计数独立。无穷强度集合的计数几乎必然无穷，因为其e的负计数次幂期望为0。这证明的是实际计数与独立性，而非只取一个“PRM”名称。

## 2. 确定函数的补偿等距

<a id="t-levy-isometry"></a>

若简单函数由互不相交的有限强度集合组成，定义I(f)为各系数乘“计数减强度”的和。Poisson方差等于均值、不同集合计数独立，逐项相乘给出等距。σ有限性使这类简单函数在L²中稠密，T-LP完备性于是唯一延拓I。

\[
EI(f)=0,\qquad E[I(f)I(g)]=\int fg\,d\mu,\qquad
E|I(f)-I(g)|^2=\|f-g\|_{L^2(\mu)}^2.
\]

这里的f、g是确定实函数；向量函数逐坐标定义，再对平方范数求和。它不是尚未建立的可预测随机被积函数积分。对同时L¹和L²的函数，普通计数积分减去强度积分与此延拓相同，先简单逼近，再用两种范数的收敛即可。

## 3. 从固定时刻L²走到共同路径极限

<a id="t-levy-compensated-path"></a>

\[
\begin{gathered}
M^\varepsilon_t=\int_{(0,t]\times\{\varepsilon<\|x\|\le1\}}
x\,[N(ds,dx)-ds\,\nu(dx)],\qquad
v(\varepsilon)=\int_{0<\|x\|\le\varepsilon}\|x\|^2\nu(dx)\downarrow0,\\
E\sup_{t\le T}\|M^\delta_t-M^\varepsilon_t\|^2
\le4T v(\varepsilon)\quad(0<\delta<\varepsilon\le1).
\end{gathered}
\]

这里使用过去全部计数与Gaussian坐标生成的自然滤过的完成，即在每个时刻加入总σ-代数的全部概率零集；不要求右连续。有限截断是有限跳和减线性函数，为càdlàg。时间窗的独立计数给它相对于全部过去计数及独立Gaussian过去的鞅性质。先在每个二进网格应用第15章实坐标L² Doob，把各坐标上确界求和；再用càdlàg使稠密网格上确界等于连续时间上确界，MCT/Fatou给所示向量界。右边的终端方差由第2节计算，没有调用连续时间一般最大定理。

\[
\begin{gathered}
v(\varepsilon_j)\le2^{-4j},\qquad \varepsilon_j\downarrow0,\\
P\!\left(\sup_{t\le j}\|M^{\varepsilon_{j+1}}_t-
M^{\varepsilon_j}_t\|>2^{-j}\right)\le4j\,2^{-2j}.
\end{gathered}
\]

BC使这些差最终不超过2⁻ʲ，望远镜求和遂在一个共同概率1事件上给所有紧区间的一致Cauchy性。在滤过已完成的条件下，异常零集上设为0不破坏适应性。均匀极限仍càdlàg：给定误差，先固定一个一致逼近的截断，再用该截断的右连续与左极限；左极限值也由一致Cauchy性形成Cauchy列。以M记极限，坏集上设为0。

\[
E\sup_{t\le T}\|M_t-M^\varepsilon_t\|^2
\le4T v(\varepsilon)\longrightarrow0.
\]

再用Fatou得到整个截断族的估计，而不只选定子列。固定时刻的L²收敛及条件期望的L²收缩，把鞅性质传给M；其增量方差为时间长度乘小跳二阶积分。有限截断的增量联合特征函数分解，依概率极限保持此分解，故M有独立平稳增量，并随机连续。

固定任意0<ε≤1，充分大的j满足εⱼ<ε；共同一致极限使上确界差也收敛，Fatou给

\[
E\sup_{t\le T}\|M_t-M^\varepsilon_t\|^2
\le\liminf_{j\to\infty}4T
\int_{\varepsilon_j<\|x\|\le\varepsilon}\|x\|^2\nu(dx)
=4T v(\varepsilon).
\]

所以结论覆盖全部截断ε，而不是只覆盖选中的离散序列。所有紧窗口的概率1事件先在正整数T上相交，任意有限T再由包含关系得到。鞅的固定时间条件期望等式先由L²收缩通过极限；不同时间窗增量的联合特征函数逐项通过依概率极限，保留独立平稳性。

## 4. 构造模型的原子确实就是它的跳

<a id="t-levy-model-jumps"></a>

\[
Y_t=bt+G_t+
\int_{(0,t]\times\{\|x\|>1\}}x\,N(ds,dx)+M_t,\qquad
E[G_sG_t^\top]=(s\wedge t)A.
\]

G用第23章Brownian和矩阵平方根构造，与N独立。大跳在紧窗口内有限，哪怕标记没有一阶矩也仍是有限和。模型因此càdlàg、具有独立平稳增量并随机连续。有限截断特征函数相乘，二阶支配使ε趋0，给单位球截断的LK指数。

任意两个不同带的到达时刻相等的概率为0，因为各个时刻有连续分布并相互独立；取可数并排除全部跨带同时到达。每带内部也无同时到达。在共同一致收敛事件上，极限余项的跳量至多两倍其一致范数。因此每个实际原子最终被截断看见并恢复同样跳量；不在原子处，每个截断的跳都为0，极限的跳也为0。这个估计同时控制全部时间，不拼接固定时刻零集。

\[
\|\Delta(M-M^{\varepsilon_j})_t\|
\le2\sup_{s\le T}\|M_s-M^{\varepsilon_j}_s\|,
\qquad N_Y=\sum_{t>0:\Delta Y_t\ne0}\delta_{(t,\Delta Y_t)}=N.
\]

## 5. 从有理坐标读出一条路径的跳测度

<a id="t-levy-jump-measurability"></a>

先给一个确定性引理。每条紧区间[0,T]上的càdlàg向量路径z都可一致逼近为有限阶梯。约定空集下确界为∞，按下式递归，首次达到T即停止；在每段[tⱼ,tⱼ₊₁)取锚值z(tⱼ)，终点T单独取z(T)。

\[
t_0=0,\qquad
t_{j+1}=\inf\{s\in(t_j,T]:\|z(s)-z(t_j)\|>\eta\}\wedge T .
\]

右连续使每段长度为正，在新段开始前误差至多η。若新时刻小于T，取触发集合中向该时刻下降的序列，右连续保证相邻锚值距离至少η。若分段时刻无限积聚于某点，其左极限会使这些锚值成为Cauchy列，矛盾。因而只有有限段，终点另赋值处理T的单独跳；η可任意小，所需一致逼近得证。这是确定性函数论证，不调用随机首次命中可测性。

取连续紧支撑的标记函数f，且它在半径η以内为0；时间权a连续。用误差小于η/4的有限阶梯逼近原路径。足够细的二进网格中，不含阶梯边界的格子增量小于η，所以不贡献；所有能使f非零的真实跳也在这个有限边界集中：若s不是阶梯边界，则跳量范数至多2倍一致逼近误差，小于η。网格充分细时，每格至多容一个边界；只有这些有限格需要保留。它们的端点分别趋向该边界的左右值，时间权也收敛。因此

\[
\sum_i a(t_i)f(x(t_i)-x(t_{i-1}))
\longrightarrow\sum_{0<s\le T}a(s)f(\Delta x_s).
\]

格子一律为(tᵢ₋₁,tᵢ]：二进边界由左侧一格捕获，T的跳由末格捕获，0不计。取整数T与二进端点，左边只用有理坐标，所以右边可测。对相对开时间—标记矩形，取连续非负乘积函数递增逼近指标；标记先限制在离零有界环带，故上述测试适用。令路径记为z，选择递增窗口如下。

\[
\begin{gathered}
E_m=(0,m)\times\{x:1/m<\|x\|<m\},\qquad m\ge2,\\
N_z(E_m)<\infty,\qquad
N_z(B)=\lim_{m\to\infty}N_z(B\cap E_m).
\end{gathered}
\]

固定m，满足“路径z到\(N_z(B)\)可测”的Borel子集B⊂Eₘ构成λ-system：它包含Eₘ；取相对补集时使用有限差\(N_z(E_m)-N_z(B)\)，没有∞−∞；不交可数并由可数和处理。相对开矩形构成生成Borel(Eₘ)的π-system，所以π–λ给每个Borel子集的计数可测。最后按窗口递增取极限，得到全部Borel计数，允许最终为无穷。有限阶梯引理保证每个Eₘ内只有有限跳，这是补集论证不可省略的条件。

大跳和J^{>1}及有限补偿截断的每个有理时间坐标都是可测积分。共同好集可具体写成下面的可数式，m、r、J、j、k均取正整数。

\[
\begin{gathered}
\mathcal H=\bigcap_{m,r\ge1}\ \bigcup_{J\ge1}\ 
\bigcap_{j,k\ge J}
\left\{z:\sup_{q\in\mathbb Q\cap[0,m]}
\|M_q^{\varepsilon_j}(z)-M_q^{\varepsilon_k}(z)\|\le1/r\right\},\\
C_t(z)=z_t-bt-J_t^{>1}(z)-M_t(z).
\end{gathered}
\]

每个截断差càdlàg，所以有理时间上确界等于整个紧窗口上确界。因而H恰给紧上一致Cauchy性；在H上定义M为一致极限，H外设0。极限仍càdlàg，残差C也càdlàg，其每个有理坐标均可测。这里只使用有理坐标σ-代数，不需要D空间的Polish性或拓扑紧性定理。

## 6. 分解回到原过程所在空间

<a id="t-levy-original-space"></a>

现在X是给定的càdlàg、随机连续、独立平稳增量过程，X₀=0。X₁无限可分，所以先用T-LEVY-CHARACTERISTICS取得其唯一LK参数；这一步不使用本节的路径分解。若单位时间指数为Ψ，则1/n时间特征函数乘exp(−Ψ/n)连续且取n次单位根值，在频率0等于1，因连通性恒为1。独立性先给所有有理时间的指数，再由随机连续性给全部时间。

因此X与第4节模型Y有相同的有理有限维律。π–λ使它们在有理坐标σ-代数上同律，第5节所有可测联合泛函便同律。在模型上已证明跳泛函恢复N，补偿极限恢复M，残差恢复G；把这一联合恒等式传回X，就得到下面真正发生在原空间的结论。

\[
\begin{gathered}
N_X=\sum_{s>0:\Delta X_s\ne0}\delta_{(s,\Delta X_s)}
\text{ is PRM with intensity }ds\,\nu(dx),\\
X_t=bt+C_t+\int_{(0,t]\times\{\|x\|>1\}}x\,N_X(ds,dx)
+\lim_j\int_{(0,t]\times\{\varepsilon_j<\|x\|\le1\}}x\,[N_X-ds\,\nu],\\
C\text{ is continuous Gaussian with covariance }(s\wedge t)A,\qquad
C\ \perp\!\!\!\perp\ N_X .
\end{gathered}
\]

等式在一个共同概率1事件上对全部时间成立，补偿极限在紧区间一致且全截断族ucp收敛。若A退化，只断言这个连续Gaussian余项存在；不能声称原空间必有可供补齐零方差方向的额外标准Brownian坐标。零矩阵时C恰为0。

还要把“连续余项”本身放进可测转移，不能只转移各个固定时刻。càdlàg函数C在每个紧窗连续，当且仅当它在有理坐标上满足下面的一致模条件。充分性由有理值的一致连续延拓及C的右连续识别，必要性是紧区间上一致连续。

\[
\mathcal C=\bigcap_{m,r\ge1}\ \bigcup_{n\ge1}\
\bigcap_{\substack{p,q\in\mathbb Q\cap[0,m]\\|p-q|<1/n}}
\{z:\|C_p(z)-C_q(z)\|\le1/r\}.
\]

H与上述连续性事件都属有理坐标σ-代数，在模型上概率1，故在原X上也概率1。Gaussian有限维律先对有理坐标转移。对任意有限个此类坐标及有限个Borel计数事件，模型的Gaussian/计数独立性给联合概率的乘积分解；π–λ分别扩到两边生成的全部σ-代数。连续性再把有理坐标扩到全部时间。分解在有理时间成立后，各项均càdlàg，同一事件上的稠密时间恒等式便扩到所有时间，不是对不可数零集直接取并。

在X自然滤过的完成中，分解还具有相应的信息结构。固定t，把第5节的网格限制在[0,t]，即使t无理也只用时刻不超过t的坐标；所以过去跳计数、有限补偿和以及其极限都对完成后的X自然过去可测。残差定义给C的过去同样可测。反过来，路径分解从C及N的过去恢复X的过去，故

\[
\overline{\mathcal F_t^X}=
\overline{\sigma\!\left(C_s,N_X((0,s]\times B):
s\le t,\ B\text{ Borel},\ \nu(B)<\infty\right)}.
\]

横线仅表示加入原概率空间总σ-代数的零集，不要求右连续增广。模型中(C,N)的未来增量独立于这份过去，逐个有限柱集转移及π–λ使原空间也具有该独立性。因此连续余项相对于这份自然信息具有协方差A的Brownian增量结构；不对任意额外泄露未来的扩大滤过作此断言。

## 7. 有限活动与有限变差的充要

<a id="t-levy-variation"></a>

有限跳活动当且仅当ν总质量有限。有限时，Poisson计数在每个紧窗口有限；无限时，Laplace公式给每个正长度有理窗口内的计数几乎必然无穷，再取可数交。这里只是在数跳，不排除独立的粗糙Gaussian部分。

\[
X\text{ has finite variation on compact intervals a.s.}
\quad\Longleftrightarrow\quad
A=0,\qquad\int_{0<\|x\|\le1}\|x\|\nu(dx)<\infty.
\]

若积分发散，Laplace公式使小跳绝对和的负指数期望为0，故该和几乎必然无穷。任何确定càdlàg路径的变差至少为其跳量范数之和：先取有限个跳，各取互不相交的左侧小邻域，令邻域缩小，再对跳集取上确界。因此有限变差不可能。

若A非零，选一个非零方差投影。连续Gaussian部分与完整跳路径独立。对固定跳路径j，假如Gaussian加j为有限变差的概率p(j)>0，取两份独立Gaussian共享这个j，两条均为有限变差的概率为p(j)²。相减便是一份非零缩放Brownian且有限变差，与26章矛盾。Fubini说明若总概率正，则p(j)²的积分也正，完成必要性，不需一般二次变差。有限变差事件可用有理分割上确界表达，故所用事件可测。

反向，Campbell均值给小跳绝对和在每个紧窗口有限。补偿项可改写为绝对收敛的普通跳和，加一个有限线性漂移。大跳局部有限，于是总变差有限。

\[
X_t=dt+\sum_{s\le t}\Delta X_s,\qquad
d=b-\int_{\|x\|\le1}x\,\nu(dx)\quad\text{in the finite-variation case}.
\]

补足变差判据中的两个极限。必要方向若一阶积分发散，用1−e^{−r}≥(1−e^{−1})r（0≤r≤1）及Poisson Laplace公式，得到绝对跳和的负指数期望0，所以绝对跳和几乎必然无穷。充分方向则有如下可积随机总量及路径尾界。

\[
\begin{gathered}
A_T^{\rm jump}=\sum_{\substack{s\le T\\0<\|\Delta X_s\|\le1}}
\|\Delta X_s\|,\qquad
EA_T^{\rm jump}=T\int_{0<\|x\|\le1}\|x\|\nu(dx)<\infty,\\
\sup_{t\le T}\left\|\sum_{\substack{s\le t\\0<\|\Delta X_s\|\le\varepsilon}}\Delta X_s\right\|
\le\sum_{\substack{s\le T\\0<\|\Delta X_s\|\le\varepsilon}}
\|\Delta X_s\|\longrightarrow0 .
\end{gathered}
\]

在每个整数窗口绝对和有限的共同事件上，末式对全部t同时成立；确定补偿尾另由T乘小球一阶积分控制而趋0。因此普通绝对跳和减线性积分确实等于先前构造的M，而不是仅在每个固定时刻分布相同。Gaussian必要方向使用的变差事件也可测：紧窗口上的总变差等于有理分割增量和的上确界。将Gaussian路径与跳路径看成独立有理坐标随机元，Fubini直接给两份独立Gaussian共享一份跳路径的计算，无需调用未建立的条件路径分布。

## 8. 单调等待的完整边界

<a id="t-levy-subordinator"></a>

在实线、不杀死、无限寿命的范围内，X为从0出发的subordinator，当且仅当A=0、ν没有负半轴质量、小跳一阶可积，且第7节的真实漂移d非负。充分性由正跳普通和显然得到；必要性除漂移符号以外，已由单调路径的有限变差及其非负跳得到。

令S为正跳和，在短时间h按阈值ηh分开。超过此阈值的跳出现概率至多hν((ηh,∞))，在(0,1]上由x/η支配后DCT趋0，在(1,∞)上则是h乘有限总质量，也趋0；其余跳和除以h的均值为阈值以下一阶积分，也趋0。因此S_h/h依概率趋0，而X_h/h趋于d。X_h非负迫使d非负。

\[
Ee^{-qX_t}=
\exp\left[-t\left(dq+\int_{(0,\infty)}(1-e^{-qx})\nu(dx)\right)\right],
\qquad q\ge0.
\]

ν在(0,1)上密度为1/x，给无限活动而有限变差的例子。密度改为1/x²并作补偿，虽然仍只有正跳，小跳绝对和却发散；它不是subordinator。该补偿过程均值0、方差t而非退化，若它非负则均值0会迫使退化，也直接说明“没有负跳”不足以推出单调。
