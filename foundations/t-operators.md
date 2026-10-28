# T-OPERATORS：从短时间变化率到正压缩半群

这里建立第28章所用的算子工具。首先X为实Banach空间；涉及正性和最大值时，X取局部紧Polish空间上的C₀(E)。所有算子极限若未说明，均逐个向量在范数中理解。

## O.1 连续向量积分，不借用未建的积分理论

<a id="t-operators-integrals"></a>

连续v:[a,b]→X一致连续。两个带标记分割的Riemann和，取共同细分后差的范数不超过区间长度乘相应连续模；故网格趋0时构成Cauchy族。完备性给唯一极限，称为积分。加法、线性与有界线性算子移入积分，由有限和通过极限得到。

\[
\left\|\int_a^b v(s)\,ds\right\|\le\int_a^b\|v(s)\|\,ds,\qquad \frac{d}{dt}\int_a^t v(s)\,ds=v(t).
\]

范数界先对和成立再取极限；基本定理由差商与v(t)之差不超过小区间上的连续模得到。连续导数的向量函数F也满足积分基本定理：令H(t)=F(t)−∫从a到t的F′，已证的积分导数给H′=0。对固定a，实函数范数(H(t)−H(a))的增量绝对值不超过范数(H(t+h)−H(t))，故其导数为0；实变量中值定理使该范数恒0。这避免在向量空间偷用标量中值等式。若v在无穷区间的范数有可积上界，有限区间积分的尾差使其Cauchy，定义广义积分。半群Laplace积分正属于此情形。

## O.2 生成元稠密、闭合及时间微分

<a id="t-operators-generator"></a>

设T为强连续压缩半群。强连续在每个时刻成立：右差用Tₜ(Tₕ−I)，左差用Tₜ₋ₕ(Tₕ−I)，压缩性控制它们。对f在D(A)，相同差商给Tₜf在域中和下面的恒等式。

\[
AT_tf=T_tAf,\qquad \frac{d}{dt}T_tf=T_tAf,\qquad T_tf-f=\int_0^tT_sAf\,ds.
\]

对于任意f，设uₜ为时间平均。直接将Tₕ作用后换积分端点，除h并利用连续性，得到生成元值。平均又一致趋于f，所以域稠密。

\[
u_t=\frac1t\int_0^tT_sf\,ds,\qquad Au_t=\frac{T_tf-f}{t}.
\]

若fₙ→f且Afₙ→g，压缩性允许把积分恒等式传到极限，得Tₜf−f=∫Tₛg。除以t后强连续给Af=g。这证明A闭。

## O.3 resolvent的两个逆关系与一致性

<a id="t-operators-resolvent"></a>

\[
R_\lambda f=\int_0^\infty e^{-\lambda t}T_tf\,dt,\qquad\|R_\lambda\|\le1/\lambda.
\]

若半群正，对非负f的Riemann和及其范数极限都非负，故Rλ正。令h为正，把Tₕ作用后换元。下式的差商在X中趋于λRλf−f，故Rλf属于域且(λ−A)Rλf=f。

\[
T_hR_\lambda f=e^{\lambda h}\left(R_\lambda f-\int_0^h e^{-\lambda s}T_sf\,ds\right).
\]

对f在域中，指数乘Tₜf的导数为指数乘Tₜ(A−λ)f。积分到N，再令N趋无穷，得到Rλ(λ−A)f=f。因此λ−A为双射，逆正是Rλ。用该双射作用于两个resolvent之差，算得下面公式；交换λ、μ后也证明交换性。

\[
(\lambda-A)(R_\lambda-R_\mu)f=(\mu-\lambda)R_\mu f,\qquad R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu.
\]

最后，λRλf−f是对Tₜf−f的指数平均。给定δ，将0到δ的部分用强连续界住，δ以后的部分用2范数乘指数尾界住，先λ趋无穷再δ趋0，得到λRλf→f。

## O.4 由正最大值原理得到可闭性和全部逆

<a id="t-operators-maximum"></a>

A稠密定义于实C₀，满足正最大值原理。若范数在正极值取得，直接用原理；若在负极值取得，对−f用原理。负部估计在f最负的点应用−f。得到所有正λ的两条界。

\[
\lambda\|f\|\le\|(\lambda-A)f\|,\qquad\lambda\|f^-\|\le\|((\lambda-A)f)^-\|.
\]

可闭性不能从第一条界直接跳出。若fₙ→0、Afₙ→g，固定u在域中，对u+λfₙ应用参数λ的第一条界，然后令n趋无穷，得到下式。再让λ趋无穷，有范数u−g至少为范数u；域稠密，令u趋g，便得g=0。

\[
\|u\|\le\|u-\lambda^{-1}Au-g\|.
\]

设B为图闭包。两条界通过图收敛保留。对任意正λ，(λ−B)值域闭：若输出为Cauchy，第一条界使输入Cauchy，且B输入也Cauchy，闭性给极限输入。若某λ₀下原A值域稠密，则B在该λ₀下满射且单射，逆范数不超过1/λ₀。

\[
R_\mu=R_\lambda[I+(\mu-\lambda)R_\lambda]^{-1}\quad\text{if }|\mu-\lambda|<\lambda.
\]

Neumann级数给相邻参数的逆。从λ₀开始可覆盖(0,2λ₀)，再以3λ₀/2、其后不断乘3/2推进，覆盖全部正轴。每个新逆的压缩界都由B的第一条界重新得到。正性不从交错Neumann级数猜测，而是第二条界：若(μ−B)f≥0，则f⁻=0。因此所有Rμ正，且范数不超过1/μ。

## O.5 真正构造半群：Yosida极限

<a id="t-operators-generation"></a>

现在假设A已闭、域稠密，所有正λ下双射逆Rλ满足压缩界；在C₀情形再假设Rλ正。先不使用任何半群。由逆关系代数得到resolvent恒等式和交换性。对f在域中，有λRλf−f=RλAf趋0；范数界和稠密性将此扩到所有f。定义以下有界算子。

\[
A_\lambda=\lambda^2R_\lambda-\lambda I,\qquad S_\lambda(t)=e^{-\lambda t}\sum_{k\ge0}\frac{(\lambda t)^k}{k!}(\lambda R_\lambda)^k.
\]

级数在算子范数中绝对收敛，项估计使Sλ为压缩半群，正性逐项保留。对域元素，Aλf=λRλAf趋Af。不同Aλ交换，故对Sλ(t−s)Sμ(s)逐项求导积分，有下式；两个半群都压缩，因而右边只涉及同一个固定f。

\[
S_\mu(t)f-S_\lambda(t)f=\int_0^tS_\lambda(t-s)S_\mu(s)(A_\mu-A_\lambda)f\,ds,\quad\sup_{t\le T}\|S_\mu(t)f-S_\lambda(t)f\|\le T\|(A_\mu-A_\lambda)f\|.
\]

在稠密域上这是紧时间窗中的Cauchy族，对任意f再选近似域元素，用两次压缩界扩张。极限Tₜ保持压缩与正性。乘积极限给半群关系；每个Sλ强连续且紧时间窗一致逼近T，给T的强连续。

设G为T的生成元。对f在D(A)，有界算子的积分式通过极限得到Tₜf−f=∫TₛAf，所以A包含于G。要证明相等，取g在D(G)，令f=Rλ(λ−G)g。则f在D(A)，且(λ−G)(g−f)=0。第二节与第三节已证明每个压缩半群的λ−G单射，故g=f。这排除了多余定义域，G=A。

若T和S具有同一生成元，对f在域中，s↦Sₜ₋ₛTₛf的导数为0：域不变性和两个时间导数相消。故Tₜf=Sₜf，稠密性给全空间相等。结合上一节，概率Hille–Yosida定理已经完整建立。反向若半群正压缩，非负最大值为M时，正性给Tₜf≤Tₜf⁺≤范数f⁺=M，差商便给正最大值原理；第三节给所有满值域。

## O.6 core的判别及一个可用的充分条件

<a id="t-operators-core"></a>

D₀为D(A)的线性子空间。若(λ−A)D₀稠密，对f在D(A)选fₙ在D₀使输出趋(λ−A)f。Rλ有界给fₙ趋f，Afₙ=λfₙ−输出趋Af。反之图稠密立即给值域稠密。这证明正文的core等价式。

一个常用充分条件是D₀在X稠密且被所有Tₜ保持。对g在D₀，Rλg的有限时间Riemann和位于D₀，同时A作用后的和趋∫指数TₜAg；两条尾均指数可控，故图收敛到Rλg。再对任意g用D₀中的近似，利用ARλ=λRλ−I得到图收敛。Rλ值域为全域，故D₀是core。没有不变性或值域控制时，仅有上确界范数稠密不够。

本专题仅证明压缩情形及C₀上的正性版本。满足范数Tₜ不超过e的ωt次方（前置常数恰为1）的半群，可将生成元平移ω后化为压缩情形。一般带前置常数M>1的增长半群不能仅凭此操作成为压缩半群，其Hille–Yosida幂次界版本不在这里的已证范围。
