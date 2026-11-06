# T-TREE-GHP：编码稳定性、节点质量与CRT空间极限

本页完成[第55章最终定理](../chapters/55-metric-measure-limits.md#geometry-crt-limit)所需的全部几何与质量比较。输入是第53章已建立的有限方差条件树联合函数极限，及第54章的确定性实树构造。不会以结论的空间收敛倒证输入函数极限。T-CONDITIONED-HEIGHT的独立专家终审保持开放。

## 1. 同一时间关系的失真

<a id="treeghp-stability"></a>

令E₀为[0,1]上连续非负、两端为0的函数空间，使用一致范数。54章构造pₕ:[0,1]→Tₕ、根pₕ(0)以及μₕ=(pₕ)₊Leb。给h、g∈E₀，令δ为它们的一致距离。区间最小值的差至多δ，故

\[ \begin{aligned}
m_h(s,t)&=\inf_{u\in[s\wedge t,s\vee t]}h(u),\\
d_h(s,t)&=h(s)+h(t)-2m_h(s,t),\\
|d_h(s,t)-d_g(s,t)|&\le4\delta .
\end{aligned} \]

\(R=\{(p_h(t),p_g(t)):0\le t\le1\}\)是紧带根对应，因为两投影连续满射。其失真≤4δ。取同一个U∼Uniform[0,1]，其两投影的联合律q为两质量的耦合，且q(R)=1。由T-GP-GHP的同场联合判据，以r=2δ（δ=0时取任意正松弛）得到

\[ d_{rGHP}(\Phi(h),\Phi(g))\le2\|h-g\|_\infty,\qquad
\Phi(h)=(T_h,d_h,p_h(0),(p_h)_*\mathrm{Leb}). \]

这是采用最大值规范的常数；若把三项误差相加，不能原样搬用常数2。Φ为到紧带根GHP空间的Lipschitz映射，因而Borel可测。证明用了具体共同对应及耦合，不是仅凭商映射逐点存在。

## 2. 轮廓商等距于补全边的有限树

<a id="treeghp-realization"></a>

给含n≥2节点的有根平面树，每条边长a>0。把边补成闭线段得紧实树T̄，按深度优先轮廓走过每条边的两个方向，各用一个单位时间。轮廓访问位置记q(u)，高度C(u)=d(ρ,q(u))，0≤u≤2(n−1)。要证明其编码商正好是T̄，必须对边内部时刻也验证最低值公式，而非只验证整数顶点。

对任意树上点z，在删去z后的每一个上方分枝中，轮廓恰连续完成一次深度优先访问。对x=q(u)、y=q(v)，u≤v，轮廓从x到y的连续路径必过它们的最近共同祖先w，所以区间最低高度不超过|w|。若z为w以下任意严格祖先，x、y在z上方同一分枝，两个时刻同属于该分枝的一次访问区间，期间不能下到z以下。因此最低高度至少|z|；沿祖先线令z升到w，得到最低高度等于|w|。当w为根，非负性给同一结论。

\[ d_{\overline T}(q(u),q(v))
=C(u)+C(v)-2\inf_{u\le r\le v}C(r). \]

轮廓连续满射，因此该等式恰使零伪距离等价于同一访问点；因子化后得到商树到补边树的保根满射等距。标准化时钟后，游程Leb推前是归一化边长测度：每条边两次等速访问，故每单位边长得到相同质量。它不是均匀节点测度，二者在n≥2时甚至互相奇异。

## 3. 节点先序时钟与轮廓时钟

<a id="treeghp-clock"></a>

按先序记节点v₀,…,vₙ₋₁，高度Hⱼ以边数计。第52章的访问恒等式给首次轮廓到达vⱼ的时刻bⱼ=2j−Hⱼ。其原因也可直接计数：到该时刻已向下到达j个非根节点；未返的向下边正是祖先链上的Hⱼ条，所以向上次数为j−Hⱼ。记相对时刻tⱼ，并把U均匀时间分配给J=⌊nU⌋，则vⱼ的选择恰为均匀节点。

\[ \begin{aligned}
t_j&=\frac{2j-H_j}{2(n-1)},\quad 0\le j<n,\\
\eta_n&=\frac1n+\max_{j<n}|t_j-j/n|\\
&\le\frac1n+\frac1{n-1}
+\frac{H_{\max}}{2(n-1)},\qquad |U-t_J|\le\eta_n .
\end{aligned} \]

令h(t)=aC₀(2(n−1)t)，其中C₀为单位边轮廓。识别Tₕ与补边树后，pₕ(tⱼ)=vⱼ。对任意两个编码时刻，距离至多两倍这段上的高度振幅；因此同一U给节点质量ν与轮廓质量λ的一份耦合，具有确定界

\[ \begin{aligned}
d(p_h(U),v_J)&\le2\omega(h,\eta_n),\\
\omega(h,\delta)&=\sup_{|s-t|\le\delta}|h(s)-h(t)|,\\
d_P(\nu,\lambda)&\le2\omega(h,\eta_n).
\end{aligned} \]

无需声称遍历时钟完全等速地抽取节点。两份质量的TV距离仍为1，但它们的弱距离可以很小，因为耦合点在树的距离上接近。节点子空间到补边树的Hausdorff距至多a/2，根完全一致，遂在同一补边背景中得到

\[ d_{rGHP}\big((V(T),ad_{\rm graph},\rho,\nu),\Phi(h)\big)
\le\max\{a/2,\ 2\omega(h,\eta_n)\}. \]

## 4. 有限方差条件GW树的带根GHP极限

<a id="treeghp-limit"></a>

假设后代律p满足Eξ=1、0<Varξ=σ²<∞。沿P(|T|=n)>0的实际可行n趋无穷，取条件树Tₙ。最大格点跨度及可行规模按第53章，不把零概率规模强行条件化。n=1不影响极限。设aₙ=σ/(2√n)，μₙ为n个节点各给质量1/n。第53章T-CONDITIONED-HEIGHT已经实际给出同一条件树的轮廓与高度联合收敛，尤其

\[ h_n(t)=\frac{\sigma}{2\sqrt n}
C^{(n)}(2(n-1)t)\ \Rightarrow\ e(t)
\quad\text{in }C([0,1]),\qquad H_{\max}/\sqrt n=O_P(1). \]

因此ηₙ→0依概率。由连续函数空间紧性，当ε>0时，先选择小δ再让n趋无穷，以下上界趋0；这一步避免了把随机时钟误差小误当成振幅误差自动小。

\[ P(\omega(h_n,\eta_n)>\varepsilon)
\le P(\eta_n>\delta)+P(\omega(h_n,\delta)>\varepsilon),\qquad
\lim_{\delta\downarrow0}\limsup_nP(\omega(h_n,\delta)>\varepsilon)=0. \]

上一节的同场界于是趋0依概率。另一方面Φ的2-Lipschitz性质与第24章连续映射定理给Φ(hₙ)⇒Φ(e)。用以下度量版本的概率小扰动引理即可转回节点树：若d(Xₙ,Yₙ)→0依概率且Yₙ⇒Y，则对任意有界Lipschitz f，期望差的绝对值至多Lip(f)ε+2‖f‖∞P(d>ε)，先n后ε得0；Polish空间中有界Lipschitz测试刻画弱收敛，见第24章。

\[ \boxed{\left(T_n,\frac{\sigma}{2\sqrt n}d_{T_n},
\rho_n,\frac1n\sum_{v\in T_n}\delta_v\right)
\ \Rightarrow\
(\mathcal T_e,d_e,\rho_e,\mu_e)
\quad\text{in }(K^r,d_{rGHP}).} \]

根、全空间距离和原始均匀节点质量在同一比较中同时得到控制。此处e是第37、53、54章时长1、标准Brownian运动规范的游程，未改为2e。n−1只出现在轮廓边时钟；空间比例使用√n。没有在原概率空间宣称几乎必然树收敛。

## 5. 依赖闭合与未证的一般化

<a id="treeghp-boundary"></a>

证明链是53条件桥/切口/高度联合极限→本页时钟耦合，54实树→编码稳定性，本章GH/Prokhorov/GHP→共同拓扑及可测性，24→连续映射与小扰动。所用53高度证明的祖先链重权、局部紧性及一致误差已针对这些输入实际阅读，未发现本轮阻塞性缺口；这不是外部专家终审。无限方差条件树、一般Lévy高度、非紧局部GHP及动态树过程没有在本页证明。

正文的[节点质量比较](../chapters/55-metric-measure-limits.md#geometry-vertex-mass)给出主机制；本页保留所有时钟和误差步骤，避免用“编码收敛显然给树收敛”代替证明。
