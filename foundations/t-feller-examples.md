# T-FELLER-EXAMPLES：边界定义域与Lévy生成元

## E.1 两个半直线半群确实存在

<a id="t-feller-boundary-domains"></a>

令Hₜ为实线Gaussian卷积。反射半群对f作偶延拓再卷积并限制回半轴；偶函数经Hₜ仍偶，所以半群关系成立。偶延拓为一致连续有界函数，Gaussian增量趋0给强连续；其在无穷远消失也保留。核正且积分1。

吸收但保留0时，将f−f(0)奇延拓为v，定义Tₜᵃf=f(0)+Hₜv。v连续且一致连续，Hₜ保奇，因此边界值始终f(0)，再次奇延拓恰是Hₜv，给半群性。展开积分就是正文的核：y>0的核gₜ(y−x)−gₜ(y+x)非负，余质量2Φ(−x/√t)放在0。

强连续由v的一致连续性得到。无穷远消失可用核公式：终点落在固定紧区间及命中0的概率都随x趋无穷而趋0，区间外f很小。于是两个算子都在同一C₀([0,∞))上正、保守、强连续。取f=e⁻ˣ²，吸收时从0平均永远为1，反射时为(1+2t)⁻¹ᐟ²，所以确实不同。

## E.2 Laplace热核与全部resolvent值域

令κ为2λ的平方根。先证明热核的Laplace积分H(x)等于e⁻κ|x|/κ。x>0处，热方程与分部积分给H″=2λH；微分在离0的紧区间可由小时间的Gaussian指数衰减及大时间的指数折扣支配。H在无穷远趋0，由支配gₜ(0)的控制收敛得出；H(0)=1/κ由Gaussian积分算出。二阶常系数方程遂给结论，偶性处理x<0。

\[
\int_0^\infty e^{-\lambda t}g_t(x)\,dt=\frac{e^{-\kappa|x|}}{\kappa},\qquad r_\lambda^{D/R}(x,y)=\frac{e^{-\kappa|x-y|}\mp e^{-\kappa(x+y)}}{\kappa}.
\]

对正文两个核积分并用有界Fubini，反射得到rᴿ积分。吸收还有边界质量的Laplace积分。x>0首次命中密度是xgₜ(x)/t，这是对第26章反射所得命中分布求导；其Laplace积分为−H′(x)=e⁻κx，因此边界项是f(0)e⁻κx/λ。x=0直接代入保持边界值。

\[
R_\lambda^r f(x)=\int_0^\infty r_\lambda^R(x,y)f(y)\,dy,\qquad R_\lambda^a f(x)=\int_0^\infty r_\lambda^D(x,y)f(y)\,dy+\frac{f(0)}\lambda e^{-\kappa x}.
\]

将|x−y|积分分成y<x与y>x两段，逐段微分。端点项第一次抵消、第二次留下−2f(x)，所以u″=2λu−2f。显式核给u在C₀，等式给u″在C₀，单侧导数也连续。反射核在x=0一阶导数为0；吸收核在0为0，加上边界项使u(0)=f(0)/λ，故u″(0)=0。

反向取正文任一候选域中的u，令f=λu−u″/2。反射时它在C₀；吸收时u″(0)=0使f(0)=λu(0)。与相应resolvent解相减，差w满足w″=2λw，且w在C₀，并满足同一边界条件。一般解为ce⁻κx+deκx；无穷远消失去掉d，任一边界条件再去掉c。因此u在resolvent值域中。T-OPERATORS的值域等于定义域结论，证明正文两条精确定义域。

## E.3 一个稠密公共测试域，却不是core

令D₀为半轴上光滑紧支撑且在0附近恒定的函数。它一致稠密：先由连续性把任意C₀函数在小邻域展平，再在远端截断并在中间光滑逼近。D₀同时包含于两个域，两个生成元在其上相同。

反射情形D₀总有Af(0)=0，图收敛保留这一条件，不能逼近f=e⁻ˣ²，因为Aᵣf(0)=−1。吸收情形D₀总有f′(0)=0，图收敛也保留导数迹：Taylor积分式给下式中的连续控制。函数xe⁻ˣ²在吸收域内却有导数1，不能被图逼近。

\[
|u^{\prime}(0)|\le |u(1)-u(0)|+\int_0^1(1-s)|u^{\prime\prime}(s)|\,ds\le2\|u\|_\infty+\tfrac12\|u^{\prime\prime}\|_\infty.
\]

故上确界范数稠密不足以决定边界。若改成到0就杀死，通常应在C₀((0,∞))等相应空间处理Dirichlet条件；把它放在完整C₀([0,∞))上又允许f(0)非0，将破坏起点0的强连续。

## E.4 截断Lévy运动的生成元

<a id="t-feller-levy-generator"></a>

先在第27章Gaussian与Poisson构成的模型上计算，截断ε<1；下面的跳跃记号指这个模型的跳。任意具有相同三元组的Lévy过程，由第27章特征函数的边缘唯一性得到同一转移半群，无需在该原空间重做分解。小于等于ε的补偿跳去掉后，其余为Gaussian、漂移与有限复合Poisson和。记截断ν为限制到|y|>ε，漂移为下式。每个ε下该积分有限，不能在ε趋0时把它单独当成收敛漂移。

\[
b_\varepsilon=b-\int_{\varepsilon<|y|\le1}y\,\nu(dy),\qquad X_t^\varepsilon=b_\varepsilon t+Q^{1/2}B_t+\sum_{s\le t,\ |\Delta X_s|>\varepsilon}\Delta X_s.
\]

对f在C紧支撑无穷光滑类，平移的一致Taylor给bε梯度。Gaussian二阶Taylor给协方差Hessian的一半：将增量除以平方根时间后固定分布，三阶有界余项期望为O(t³ᐟ²)，一阶均值0。复合Poisson级数中0次与1次项给积分f(x+y)−f(x)，至少2次概率为O(t²)，其作用误差由2范数f控制。

三个独立位移的卷积算子交换。将乘积差拆成三个差，用各自强连续及上述一致导数，得到截断生成元Lε，并将漂移项与中等跳一阶项合并，得到下式。

\[
L_\varepsilon f=b\cdot\nabla f+\tfrac12\operatorname{tr}(Q\nabla^2f)+\int_{|y|>\varepsilon}[f(\cdot+y)-f-\mathbf1_{\{|y|\le1\}}y\cdot\nabla f]\,\nu(dy).
\]

## E.5 小跳极限真正给出定义域元素

以下Hessian范数取各点矩阵算子范数的上确界。小跳二阶Taylor与大跳有限质量给Lf绝对积分，且Lf在C₀：空间连续用支配收敛，小跳由Hessian范数乘|y|²支配，大跳由2范数f支配；出发位置趋无穷时，对固定y各项都趋0，同一支配再给无穷远消失。还得到统一误差。

\[
\|L_\varepsilon f-Lf\|_\infty\le\tfrac12\|\nabla^2 f\|_\infty\int_{|y|\le\varepsilon}|y|^2\nu(dy)\longrightarrow0.
\]

第27章补偿构造的L²最大估计，在d维各坐标相加得到下面的界。只使用小跳构造及正交性，不使用稳定分类、一般吸引域或原空间分解的未经独立终审部分。

\[
E\sup_{s\le T}|X_s-X_s^\varepsilon|^2\le4T\int_{|y|\le\varepsilon}|y|^2\nu(dy).
\]

因此对任意g在C₀，共同位移与一致连续性给supₛ≤T范数(Tₛεg−Tₛg)趋0：在位移差≤δ事件用连续模，补集用Chebyshev及2范数g。先ε趋0，再δ趋0。截断生成元已给Tₜεf−f=∫TₛεLεf，右边先换Lεf为Lf再换半群，误差由上面两项乘T控制。故极限满足Tₜf−f=∫TₛLf。除以t并用Lf在C₀的强连续，证明f在D(A)且Af=Lf。

这证明了所用测试类的域成员关系与公式，没有未经额外逼近就宣称它是所有Lévy生成元的core。改变截断函数会同时改变漂移参数；不能只改积分中的减项而保留同一个b。
