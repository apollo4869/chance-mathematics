# T-LEVY-DOMAINS：稳定分类、吸引域与离散梯级分解

这里完成[第27章](../chapters/27-levy-processes.md#levy-stable)所用的实值极限理论。第14章已经证明构造出的稳定族及重尾充分性；本专题补穷尽分类、吸引域必要性、无限方差Gaussian边界，并兑现离散严格/弱梯级的Wiener–Hopf乘积。所用LK与无穷小阵判别见[T-LEVY-CHARACTERISTICS](t-levy-characteristics.md#t-levy-arrays)。

## 1. 尺度不能任意改变：收敛类型引理

<a id="t-levy-types"></a>

\[
V_n\Rightarrow V,\quad a_nV_n+b_n\Rightarrow W,\quad a_n>0,\quad
V,W\text{ nonconstant}
\ \Longrightarrow\
a_n\to a>0,\quad b_n\to b,\quad W\overset d=aV+b.
\]

证明先选V分布中两个相隔正距离、各有固定正概率的区域。若尺度无界，两块像不可能同时落在W的一个共同紧窗口内，与紧性矛盾。因此尺度有界；V族紧，继而平移也有界。尺度若沿子列趋0，像分布会退化，故尺度还远离0。抽取参数极限，再用Slutsky得到所示仿射关系。

极限参数唯一：若同一非退化概率在正的仿射伸缩下不变，尺度小于1时迭代会收缩成点；尺度大于1时先求逆；尺度为1而平移非零时，反复平移违反紧性。因此只有恒等变换。所有参数子列遂有相同极限，完成整列结论。

还有一个以后反复使用的后果。非退化i.i.d.总和若经过正尺度及确定中心趋于非退化极限，则尺度必趋于无穷。第14章的对称截断预算给n乘独立差除尺度后的截断平方期望有界；有界尺度子列会迫使这个独立差恒为0，原变量便退化。加入一个新项除以尺度依概率趋0，所以对相邻两个归一化使用类型引理，得到相邻尺度比趋1。

\[
\frac{S_n-c_n}{a_n}\Rightarrow V
\quad\Longrightarrow\quad
a_n\to\infty,\qquad \frac{a_{n+1}}{a_n}\to1,\qquad
\frac{c_{n+1}-c_n}{a_n}\to0.
\]

上述尺度结论并不预先假定无穷小性。第14章预算证明的第一半只用行和紧性及独立乘积：对归一化和的独立差，在某个固定频率区间有下面的共同下界；sinc平均再给最后一项。

\[
\begin{gathered}
D=Z-Z',\qquad
|\phi_Z(t/a_n)|^{2n}\ge1/4\quad(|t|\le\delta),\\
n\bigl(1-|\phi_Z(t/a_n)|^2\bigr)\le\log4,\qquad
nE\!\left[1\wedge(D/a_n)^2\right]\le C_\delta.
\end{gathered}
\]

若尺度有aₙ≤M的子列，则E[1∧(D/M)²]≤Cδ/n趋0，强迫D恒0，原变量退化，矛盾。因此尺度确实趋无穷，加入一个新项除尺度才依概率趋0。将两个相邻归一化用收敛类型比较，同一个非退化极限只容许尺度比1、位置差0，得第1节的相邻结论。预算有界在前，无穷小性在后，没有循环。

## 2. 稳定分布的全部可能参数

<a id="t-levy-stable-classification"></a>

稳定性采用14章的完整定义：任意两个独立副本经任意正系数相加，仍是同一分布的正尺度和平移。非退化稳定律无限可分已在14章证明。由LK把其参数除以t的倒数，得到连续卷积族μ_t。整数稳定关系给每个有理t的μ_t都是μ的尺度和平移；所选卷积根必须是这个根，因为连续的特征指数唯一。

对任意实t>0，以有理时间逼近。μ_t非退化，否则LK唯一性会迫使原律也退化。类型引理使尺度和平移有唯一极限，所以同一关系扩到实时间。把时间先乘s再乘t，尺度唯一性给乘法关系；时间连续性给尺度函数连续。时间趋0时分布趋0点质量，非退化性迫使尺度趋0。连续正乘法函数于是是一项正幂。

\[
\mu_t=\mathcal L(a(t)Z+b(t)),\qquad
a(st)=a(s)a(t),\qquad a(t)=t^{1/\alpha},\quad\alpha>0.
\]

LK唯一性现在比直接解特征函数方程更有用：Gaussian方差必须同时按时间一次幂与尺度平方变换；跳测度必须齐次。

\[
t\sigma^2=t^{2/\alpha}\sigma^2,\qquad
\nu(rA)=r^{-\alpha}\nu(A)\quad(r>0).
\]

非零Gaussian部分强迫α=2。非零跳测度的两条半轴尾函数因此为常数乘x的−α次幂；对区间作差便得到密度，不假定它原来有密度。Lévy小跳条件强迫0<α<2，故此时Gaussian部分为0。若两部分都为0，只剩退化平移，已经排除。

\[
\begin{gathered}
0<\alpha<2:\quad
\nu(dx)=\bigl(c_+\mathbf1_{\{x>0\}}+c_-\mathbf1_{\{x<0\}}\bigr)|x|^{-1-\alpha}\,dx,
\quad c_\pm\ge0,\quad c_++c_->0,\quad\sigma^2=0,\\
\nu((x,\infty))=\frac{c_+}{\alpha}x^{-\alpha},\qquad
\nu((-\infty,-x))=\frac{c_-}{\alpha}x^{-\alpha}\quad(x>0),\\
\alpha=2:\quad \nu=0,\quad\sigma^2>0.
\end{gathered}
\]

这些条件也充分：14.14–14.15已由同一密度的截断构造及换元证明稳定性；任意确定平移不破坏稳定性。因此这是全部非退化实稳定律的穷尽分类，参数c保持14章的密度常数约定，不能误把它当成尾常数。

这里的时间乘法值得单独核查，因为卷积本身对应时间相加。整数稳定关系先显式给出q次根的仿射表达，连续指数唯一性识别这份根；再取p个副本，得到有理时间p/q的表达。扩到实时间以后，在指数恒等式中先乘s、再代入尺度a(t)，得到

\[
\begin{gathered}
Z_1+\cdots+Z_q\overset d=A_qZ+B_q
\quad\Longrightarrow\quad
\mu_{1/q}=\mathcal L\!\left(Z/A_q-B_q/(qA_q)\right),\\
t\Psi(u)=\Psi(a(t)u)+iu b(t),\\
st\Psi(u)=\Psi(a(s)a(t)u)+iu\{a(t)b(s)+s b(t)\}.
\end{gathered}
\]

最后一行和μ_{st}的既有正仿射表达描述同一非退化律，所以类型唯一性给a(st)=a(s)a(t)。时间连续性与类型引理给a、b连续；μ_t趋δ₀时，原律中两块相隔且有正质量的区域，不可能在a(t)有正下界时同时挤进任意小窗口，因此a(t)趋0。令v=log t，log a(e^v)为连续可加函数，故等于κv，且κ>0。取α=1/κ，才得到幂尺度。

## 3. α等于1时的中心不能略去

<a id="t-levy-stable-centering"></a>

按单位球截断，先取漂移0的标准积分指数Ψ₀，令Δ为两个密度常数之差。保留换元后截断边界的线性项，14章的直接积分给下式；它也固定了本书不依赖三角函数参数化的约定。

\[
\begin{gathered}
\Psi_0(ru)=r^\alpha\Psi_0(u)+iuD_\alpha(r),\qquad
D_\alpha(r)=
\begin{cases}
(c_+-c_-)(r^\alpha-r)/(1-\alpha),&\alpha\ne1,\\
-(c_+-c_-)r\log r,&\alpha=1.
\end{cases}
\end{gathered}
\]

任意漂移b再加上ibu。α≠1时选b=Δ/(1−α)，即可消除所有缩放差额，得到严格稳定中心。α=1且Δ非零时，漂移按同一次幂缩放，任何固定平移都消不掉对数；n个副本必须保留下面的平移。对称时Δ为0，对数项才消失。Gaussian情形则是通常的均值中心与平方根尺度。

\[
\alpha=1:\qquad Z_1+\cdots+Z_n
\overset d=nZ+n(c_+-c_-)\log n.
\]

中心符号还可直接用截断环带核对。对r>0，在Ψ₀(ru)中换元y=rx；两个线性截断的差只在r与1之间的有限环带上出现，约定r>1时积分取负向。

\[
\begin{gathered}
\Psi_0(ru)-r^\alpha\Psi_0(u)
=iu\,r^\alpha\!\int y
\bigl(\mathbf1_{\{|y|\le1\}}-\mathbf1_{\{|y|\le r\}}\bigr)\nu_\alpha(dy),\\
r^\alpha(c_+-c_-)\int_r^1 y^{-\alpha}dy
=D_\alpha(r).
\end{gathered}
\]

α=1时环带积分为−log r，故D₁(r)=−Δr log r。在n个副本的指数nΨ(u)中，把Ψ(nu)移到另一边，就变成正的Δn log n位置项。这个正号来自等式移项，并未改变下降/上升跳的密度约定。

## 4. 重尾吸引域：条件怎样真正给出极限

<a id="t-levy-stable-domain-sufficient"></a>

设非退化实随机变量的绝对尾F正则变化，指数为−α，0<α<2；正负尾占比分别趋于p₊、p₋，和为1。选C>0，并用14章的广义尾分位数取正尺度，使nF(aₙ)趋于C。单调性与正则变化保证大点的相对跳跃趋0，所以这个分位数选择确实满足所需极限。目标跳密度常数为αCp₊与αCp₋。

\[
\begin{gathered}
F(x)=P(|Z|>x),\qquad
nF(a_n)\to C,\qquad c_\pm=\alpha C p_\pm,\\
c_n=a_n\left[nE h(Z/a_n)-\gamma\right],\qquad h(x)=\frac{x}{1+x^2},\\
\frac{S_n-c_n}{a_n}\Rightarrow\mathrm{ID}(\gamma,0,\nu_\alpha).
\end{gathered}
\]

这个中心只积分有界函数，α=1或均值不存在时也有定义。下面证明并非只靠“由三元组可得”一句话。离零尾极限先识别ν；14.13的二进尺度界，对任意α<β<2给小球估计，对任意0<η<α给远尾估计。固定小区间的贡献用n/aₙ²趋0消除；该事实由2大于α及同一幂界得到。

\[
\begin{gathered}
\limsup_n nE[(Z/a_n)^2\mathbf1_{\{|Z|\le\varepsilon a_n\}}]
\le C_\beta\varepsilon^{2-\beta},\\
\limsup_n nP(|Z|>R a_n)\le C_\eta R^{-\eta}.
\end{gathered}
\]

第一式由截断二阶矩至多2乘尾积分，再代入二进上界得到。它证明零点没有Gaussian质量；第二式排除无穷远逃逸。于是w乘原项行测度弱收敛到wν。此处仍不能随意将原项泊松化：必须证明对数误差消失。取α/2<q<min(α,1)，尾积分保证q阶矩有限，且尺度幂界给n/aₙ^{2q}趋0。

\[
n|\phi_Z(u/a_n)-1|^2
\le C_{u,q}n a_n^{-2q}(E|Z|^q)^2\to0.
\]

因此原行特征函数与原项伴随复合Poisson特征函数有相同极限。所选中心使后者的连续截断漂移恰为γ，第1专题的实canonical判别完成证明。指定别的中心时，充要条件就是所示漂移差仍趋γ；不能在α=1擅自替换成不存在的均值。

具体核对上面的泊松化误差：正则变化的二进幂界给每个η<α的尾上界Ct^{−η}。在q与α间选η，尾积分便给q阶矩有限；另一方面在α与2q间选β，nF(aₙ)趋正常数与同一幂界给n/aₙ^{2q}趋0。对固定u，单项特征函数趋1，可以在1附近取同一log支。

\[
\begin{gathered}
E|Z|^q=q\int_0^\infty t^{q-1}F(t)\,dt<\infty,\qquad
\alpha/2<q<\min(\alpha,1),\\
|\log(1+z)-z|\le C|z|^2\quad(|z|\le1/2),\\
n\left|\log\phi_Z(u/a_n)-(\phi_Z(u/a_n)-1)\right|\to0 .
\end{gathered}
\]

减去确定中心只乘模1的相位，伴随复合Poisson指数的实部非正；故对数差趋0确实推出两个特征函数之差趋0。小球与远尾界先建立有限canonical测度的弱收敛，再通过此误差把极限传给原和，步骤没有互相假设。

## 5. 必要性：从极限反读出真实尾部

<a id="t-levy-stable-domain-necessary"></a>

反过来，假定完整n序列的归一化i.i.d.和趋于某个非Gaussian α稳定律。第1节给尺度趋无穷且相邻比趋1。先用正确的中位数及sin中心阵列判别，不能在尚未知道尾部时直接使用原项泊松化。每项中心化仅把Z/aₙ平移一个趋0的确定数；极限跳测度在非零点无原子，移动阈值的夹逼因而给下面的原始尾极限。

\[
nP(Z>a_n x)\to\frac{c_+}{\alpha}x^{-\alpha},\qquad
nP(Z<-a_n x)\to\frac{c_-}{\alpha}x^{-\alpha}\quad(x>0).
\]

为何这不只是沿某条稀疏尺度成立？给任意大y，取aₙ首次越过y的指标；相邻尺度比趋1，使aₙ/y趋1。尾函数单调，在(1±ε)aₙ处夹逼，再令ε下降到0，就把上述极限扩成所有实y趋于无穷的正则变化及尾平衡。相同方法不需要尺度序列本身单调。

现在才可用第4节的q阶矩与对数误差估计，回到未中心化原项的canonical漂移，得到中心条件也必要。因此重尾正则变化、正负尾平衡、正确尺度与有界截断中心共同构成完整充要判别，不只是一个构造例子。

\[
nE h(Z/a_n)-c_n/a_n\longrightarrow\gamma .
\]

把尾部必要性的夹逼也写出来。尺度趋无穷，故首次跨越指标存在并趋无穷；虽然aₙ可能不单调，首次跨越仍保证它前一项小于y。相邻比趋1遂保证跨越没有固定比例的缺口。

\[
\begin{gathered}
n(y)=\min\{n:a_n\ge y\},\qquad
a_{n(y)-1}<y\le a_{n(y)},\qquad a_{n(y)}/y\to1,\\
F((r+\eta)a_{n(y)})\le F(ry)\le F((r-\eta)a_{n(y)})
\quad(0<\eta<r,\ y\text{ sufficiently large}),\\
n(y)F(y)\to C,\qquad
\frac{F(ry)}{F(y)}\to r^{-\alpha},\qquad
C=(c_++c_-)/\alpha .
\end{gathered}
\]

固定r、η，先沿y趋无穷，用已得的各固定阈值尾极限；再η下降到0，得到最后一行。正负尾分别用相同夹逼，尾比例为c₊/(c₊+c₋)、c₋/(c₊+c₋)。每项的中位数/sin平移虽随n变化，却趋0；在非零阈值x处，用x±η夹住移动阈值，因稳定跳测度无此处原子，最后η下降到0。因此没有把中心化后的尾未经论证地当成原始尾。

## 6. 慢变截断方差的三个基本估计

<a id="t-levy-normal-tail"></a>

\[
H(x)=E[U^2\mathbf1_{\{|U|\le x\}}],\qquad F(x)=P(|U|>x).
\]

设H最终为正且慢变。它可以趋于有限正常数，也可以无界。二进迭代给H的任意小正幂上界。按二进环带分解尾概率，得到下面的可求和控制；每个固定环带的方差增量相对H趋0，所有环带又由任意小幂界支配。因此DCT作用于级数给出尾部可忽略。

\[
\begin{gathered}
\frac{x^2F(x)}{H(x)}
\le\sum_{j\ge0}4^{-j}
\frac{H(2^{j+1}x)-H(2^jx)}{H(x)}
\longrightarrow0,\\
H(x)=o(x^\eta)\quad(\eta>0),\qquad
\frac{x\,E[|U|\mathbf1_{\{|U|>x\}}]}{H(x)}\to0 .
\end{gathered}
\]

最后一式由尾积分得到：在全部t≥x上用t²F(t)/H(t)最终任意小，再以H(xu)/H(x)≤Cu^η、η<1支配积分。它也证明一阶绝对矩存在。反方向，若x²F(x)/H(x)趋0，则对r>1，H(rx)−H(x)≤r²x²F(x)=o(H(x))；r<1用倒数。因此慢变与这项尾部条件等价。

另一个所需估计来自cos展开。在|U|≤ε/|u|上，二阶展开的误差至多常数乘ε²u²截断二阶矩；外面的概率由刚才尾界控制。先u趋0，再ε趋0，得到

\[
1-E\cos(uU)\sim\frac{u^2}{2}H(1/|u|).
\]

## 7. Gaussian吸引域：充分性及尺度的实际选择

<a id="t-levy-normal-sufficient"></a>

设Z非退化，均值μ存在，令Y=Z−μ。如果V(x)=E[Y²;|Y|≤x]慢变，取趋于无穷的正尺度使nV(aₙ)/aₙ²趋于1，就有中心化总和趋于标准Gaussian。这包括有限正方差，也包括无穷方差。下面核对所有三元组条件。

\[
\begin{gathered}
nP(|Y|>\varepsilon a_n)\to0,\qquad
\frac n{a_n^2}V(\varepsilon a_n)\to1\quad(\varepsilon>0),\\
\gamma_n=nE h(Y/a_n)\to0,\qquad
n\,w(x)\mathcal L(Y/a_n)(dx)\Rightarrow\delta_0 .
\end{gathered}
\]

前两式是第6节尾界与慢变的直接代入。漂移不可省略：因EY=0，h减去恒等函数的小球误差至多ε乘截断二阶矩；球外误差至多|Y|/aₙ，用第6节尾一阶矩估计消去。先n趋无穷，再ε趋0，给γ趋0。加权有限测度的质量遂全部聚于零点，质量为1。

原项直接泊松化在这里也须合法。均值0及一阶可积性给φ_Y(u/aₙ)−1=o(1/aₙ)；而n/aₙ²有界，因为V最终有正常数下界。因此n乘对数平方误差趋0，canonical判别给所述Gaussian极限。

尺度不是一句“选合适的归一化”。选x₀使V在其后为正，定义下面连续严格递增的函数。变量替换、慢变的二进界及DCT给其渐近式；取它的反函数便实际得到尺度。固定下端部分的贡献为有限常数，除以x²/V(x)后消失。

\[
\begin{gathered}
Q(x)=\int_{x_0}^x\frac{2t}{V(t)}\,dt
\sim\frac{x^2}{V(x)},\qquad Q(a_n)=n,\\
\frac{S_n-n\mu}{a_n}\Rightarrow N(0,1).
\end{gathered}
\]

换元后的支配函数可取常数乘u^{1−η}，0<η<2，因而在0可积。例子是对称密度|y|⁻³、|y|≥1：它已归一化，均值0，方差无穷，V(x)=2log x；尺度可取√(n log n)。大跳在这个尺度消失，但留下的截断二阶质量为1。

## 8. Gaussian必要性不能暗自假定均值

<a id="t-levy-normal-necessary"></a>

假设某组中心与正尺度使总和趋于方差σ²>0的Gaussian，先不假定Z可积。取独立副本，令D=Z−Z′。对称化总和的极限方差为2σ²。D的中位数可取0，sin中心和连续截断漂移都为0。此时canonical测度为n乘w加权的D/aₙ分布，弱趋于2σ²乘原点质量。对固定ε，用有界函数(1+x²)乘{|x|≤ε}的指标测试；它的边界不被极限赋质量，因此确实得到截断二阶矩而非只是一份vague极限：

\[
\begin{gathered}
H_D(x)=E[D^2\mathbf1_{\{|D|\le x\}}],\qquad
\frac n{a_n^2}H_D(\varepsilon a_n)\to2\sigma^2\quad(\varepsilon>0),\\
\frac{H_D(\varepsilon a_n)}{H_D(a_n)}\to1 .
\end{gathered}
\]

第1节的相邻尺度比趋1，配合H的单调性与首次跨越指标，把这条尺度序列上的比值扩到全部实x：H_D慢变。具体地，首次aₙ≥x时有aₙ₋₁<x≤aₙ及aₙ/x趋1；以固定(r−η)aₙ、(r+η)aₙ夹住rx，并对x作同样夹逼，得到每个r>0的慢变比值。第6节因而给ED的绝对一阶矩有限。中位数尾界P(|Z−m|>x)≤2P(|D|>x)使Z也可积，至此才合法定义μ=EZ及Y=Z−μ。

还需证明V∼H_D/2。取Z的中位数m，先积分中位数尾界，再控制固定平移μ−m，得到

\[
\begin{gathered}
E[1\wedge((Z-m)/x)^2]\le2E[1\wedge(D/x)^2],\\
E\min((Z-m)^2,x^2)
\le2[H_D(x)+x^2P(|D|>x)]=O(H_D(x)),\\
\min((a+b)^2,x^2)\le2\min(a^2,x^2)+2b^2,\\
E\min(Y^2,x^2)=O(H_D(x)),\qquad
P(|Y|>x)\le2P(|D|>x/2)=o(H_D(x)/x^2)
\quad(x>2|\mu-m|).
\end{gathered}
\]

H_D最终有正常数下界，所以固定平移产生的常数可吸入O(H_D)。尾界使用x−|μ−m|≥x/2及H_D慢变。这两条估计控制Taylor余项与球外概率，不能仅由“平移不重要”代替。另一方面，EY=0及一阶可积性给φ_Y(u)−1=o(u)，于是

\[
\begin{gathered}
1-|\phi_Y(u)|^2
=2(1-\operatorname{Re}\phi_Y(u))-|\phi_Y(u)-1|^2
\sim\frac{u^2}{2}H_D(1/|u|),\\
1-\operatorname{Re}\phi_Y(u)\sim\frac{u^2}{4}H_D(1/|u|).
\end{gathered}
\]

对0<ε≤1，cos的四阶余项给

\[
\begin{gathered}
\left|E[(1-\cos(uY))\mathbf1_{\{|Y|\le\varepsilon/|u|\}}]
-\frac{u^2}{2}V(\varepsilon/|u|)\right|
\le \frac{\varepsilon^2u^2}{24}V(\varepsilon/|u|)
\le C\varepsilon^2u^2H_D(1/|u|),\\
E[(1-\cos(uY))\mathbf1_{\{|Y|>\varepsilon/|u|\}}]
\le2P(|Y|>\varepsilon/|u|)
=o(u^2H_D(1/|u|))
\quad(\varepsilon>0\text{ fixed}).
\end{gathered}
\]

先固定ε，再u趋0，将这两界与上一式实部渐近比较，得到V(ε/|u|)/H_D(1/|u|)离1/2的上极限至多Cε²。令|u|=ε/x，慢变性在固定ε下允许把H_D(x/ε)换成H_D(x)；最后令ε下降到0。于是V(x)∼H_D(x)/2，V慢变及nV(aₙ)/aₙ²趋σ²全部得到。这里没有交换两个极限，也未先假定Z有方差。

第7节已证明按nμ中心的同尺度极限为N(0,σ²)。再用类型引理，原中心的差必须趋于指定极限均值ℓ。这给完整中心、尺度及必要条件，而不是仅指出“可能出现无穷方差CLT”。

\[
\frac{S_n-c_n}{a_n}\Rightarrow N(\ell,\sigma^2)
\quad\Longleftrightarrow\quad
\begin{cases}
E|Z|<\infty,\quad V\text{ slowly varying},\quad a_n\to\infty,\\
nV(a_n)/a_n^2\to\sigma^2,\quad
(n\mu-c_n)/a_n\to\ell .
\end{cases}
\]

## 9. 第一次全局最大值把路径拆成两份

<a id="t-levy-wiener-hopf"></a>

先固定符号：R是末点相对最大值的有符号位移，D才是通常非负的回落量（drawdown）。

\[
M_n=\max_{0\le j\le n}S_j,\qquad
R_n=S_n-M_n\le0,\qquad D_n=M_n-S_n=-R_n\ge0.
\]

最后处理18章留下的离散梯级责任。令实随机游走从0出发，增量独立同分布，不要求矩、对称性或非格点性；取独立几何N，P(N=n)=(1−z)zⁿ，0<z<1。对一条有限路径，第一次全局最大值位置k唯一确定。此前终点必须是严格新记录，此后相对该点的全部部分和必须不正。即使路径有平手，这个“严格过去、弱未来”分解仍唯一。

\[
\begin{gathered}
A_z(f)=\sum_{k\ge0}z^kE[f(S_k);
S_k>\max_{j<k}S_j],\\
B_z(g)=\sum_{l\ge0}z^lE[g(S_l);
\max_{1\le j\le l}S_j\le0],\\
E[f(M_N)g(R_N)]=(1-z)A_z(f)B_z(g).
\end{gathered}
\]

k=0与l=0的事件约定为真。对给定k、l，前后增量独立；几何权重正好分解为(1−z)zᵏzˡ。先对非负函数Tonelli，再扩到有界复函数，便得公式。取f=g=1，右边归一化为1，所以\(M_N\)与有符号位移\(R_N\)独立，也与非负回落\(D_N\)独立。固定时刻没有这个结论：一步对称游走的(M₁,R₁)两种结果分别是(1,0)与(0,−1)，并不独立。

严格上升梯级从0开始，第一次越过当前记录时开下一周期；弱下降梯级在第一次低于或等于当前低点时开下一周期。离散停止后独立性使这些周期独立重启，允许首次梯级时间为无穷。A的严格记录恰由上升梯级枚举；把l个增量反向，B的“不正前缀”事件变成末点为弱新低，故由弱下降梯级枚举。

\[
\begin{gathered}
T^+=\inf\{n\ge1:S_n>0\},\quad H^+=S_{T^+},\\
T^-=\inf\{n\ge1:S_n\le0\},\quad H^-=S_{T^-},\\
F_\pm(z,u)=E[z^{T^\pm}e^{iuH^\pm};T^\pm<\infty],\qquad
A_z(e^{iu\cdot})=\frac1{1-F_+(z,u)},\quad
B_z(e^{iu\cdot})=\frac1{1-F_-(z,u)},\\
1-z\phi_Z(u)=(1-F_+(z,u))(1-F_-(z,u)).
\end{gathered}
\]

反转增量保持联合分布，因为增量独立同分布；精确事件等价如下。弱下降记录包含平手，严格上升记录排除平手，两种更新枚举因而与第一次全局最大值分片相配。梯级时间无穷时将高度赋0，变换只在时间有限的事件上积分；这不添加任何概率质量。

\[
\begin{gathered}
\widehat S_j=S_l-S_{l-j}\quad(0\le j\le l),\\
\{\widehat S_l\le\widehat S_j\text{ for }0\le j<l\}
=\{S_k\le0\text{ for }1\le k\le l\},\\
E f(M_N)=A_z(f)/A_z(1),\qquad
E g(R_N)=B_z(g)/B_z(1).
\end{gathered}
\]

最后两式由联合式分别取g=1或f=1及(1−z)A_z(1)B_z(1)=1得到，再相乘便是完整独立性。A_z(1)、B_z(1)均至少1且至多1/(1−z)，归一化合法；两个梯级的时间—高度更新级数可含缺陷质量。

因为每个有限梯级时间至少1，变换模至多z，几何更新级数绝对收敛。另一方面几何时刻末点的变换为(1−z)/(1−zφ)，代入前后分解便得到最后一行。这是完整的离散Wiener–Hopf严格/弱乘积，包含平手情况；若把两边都写严格，零增量恒定游走给F₊=F₋=0，右边为1却左边为1−z。正确的弱下降时间为1，F₋=z，恰好恢复1−z。这里不把z直接取1，也不宣称已经建立连续时间全部涨落分解。
