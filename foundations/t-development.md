# T-DEVELOPMENT：随机发展、几何不变性与寿命

配套[第40章](../chapters/40-stochastic-geometry.md#geometry-development)。使用[T-GEOMETRY](t-geometry.md)的联络与水平场，以及[T-MANIFOLD-DIFFUSIONS](t-manifold-diffusions.md#manifold-proof-clock)已经独立证明的连续半鞅驱动存在唯一性。M无边界、g光滑；除边界例子外，均取无额外杀死的最大过程。

## 1. 发展与反发展是真正互逆的构造

<a id="development-proof-construction"></a>

\[ dU_t=\sum_iH_i(U_t)\circ dZ_t^i,\quad X_t=\pi(U_t),\qquad Z_t^i=\int_0^t(U_s^{-1})^i_k\circ dx^k(X_s),\quad Z_0=0. \]

给定Rⁿ连续半鞅Z及初始正交标架u₀，水平场在O(M)光滑，前页定理实际构造最大U，故X存在。T-GEOMETRY的水平场公式说明U沿X平行移动。反过来，给定连续流形半鞅X，在一个图中解dUⱼᵏ=−Γᵏₗₘ(X)Uⱼᵐ∘dxˡ(X)。可以把它看作(x,U)上的光滑场：x方向是坐标单位向量，标架方向由右式给出，故同一定理适用且x分量正好是已给X。

为排除“局部驱动换图无穷次”留下的漏洞，可在X的一个有限紧路径区域取T-GEOMETRY的分离浸入F。其微分有光滑左逆L，可在各图以(DFᵀDF)⁻¹DFᵀ构造，再用单位分解拼合，始终满足L dF=Id。Stratonovich链式给dX=L(X)∘dF(X)。把L的各方向水平提升后，平行标架成为由一个固定欧氏半鞅F(X)驱动的方程。其时钟在有限时段有限；紧基像与紧纤维遂使前页最大解定理真正适用。

Γ的坐标变换保证局部平行提升在重叠图一致；路径唯一性使其可拼合。度量相容保持U正交。任何T小于X寿命时，X在[0,T]的像紧，其上O(M)的纤维紧，故提升不会先行爆炸。上式右侧是全局solder一形式θ=U⁻¹dπ的Stratonovich积分，坐标相容已在前页证明，因而Z定义无歧义。

θ(Hᵢ)=eᵢ，加上已证Stratonovich结合律，使反发展(发展Z)=Z。另一个方向，X的平行提升满足dX=U∘dZ，由水平约束推出同一水平方程，唯一性使发展(反发展X)=X，初始标架相同。若改变初始标架为u₀q，反发展变为q⁻¹Z；这不声称任意改变联络也保持同一个反发展。

## 2. Brownian投影、标架选择与等距不变性

<a id="development-proof-brownian"></a>

\[ H_iH_j(f\circ\pi)(u)=\operatorname{Hess}f(ue_i,ue_j),\qquad \frac12\sum_iH_i^2(f\circ\pi)=\frac12(\Delta_gf)\circ\pi. \]

把Hᵢ作用于Uⱼᵏ∂ₖf：标架导数给−ΓᵏₗₘUᵢˡUⱼᵐ∂ₖf，基点导数给UᵢˡUⱼᵏ∂ₗₖf，正是Hessian。取迹用ΣUᵢ⊗Uᵢ=g⁻¹得第二式。对Z为标准Rⁿ Brownian，32章在每个图的停止版本遂证明f(X)−½∫Δf(X)ds为局部鞅。前页的严格椭圆律唯一性识别它为唯一最大Riemannian Brownian律；构造没有预设热核存在。

常正交q下水平场的右作用公式，使\(R_qU\)等于从u₀q、由q⁻¹Z驱动的发展；q⁻¹Z仍为标准Brownian。因此投影律不依赖初始正交标架。对全局Riemannian等距同胚Φ，联络唯一性保持水平场，推前U直接解目标水平方程；路径在共同驱动下即有Φ(X)的耦合身份，特别概率律等距不变。局部等距只声明到相应退出寿命，不把非proper映射当全局延长。

U为自治Brownian SDE的最大解，前页已证明强Markov。给定停止时刻后的初始U，投影未来律只依赖其基点而不依赖标架，故对条件期望再次积分得到X的强Markov性。转移核可测性来自Picard及可数图选择的可测解函数。标架寿命与基点寿命相同，因为紧基集上方的纤维紧。

## 3. 联络鞅并非“每个坐标都是鞅”

<a id="development-proof-martingale"></a>

\[ df(X_t)=df(U_te_i)\,dZ_t^i+\frac12\operatorname{Hess}f(U_te_i,U_te_j)\,d[Z^i,Z^j]_t. \]

先用Stratonovich链式与结合律，再把水平方程整体转成Itô形式。HᵢHⱼ的已证Hessian身份给上式，一阶项是Itô积分，未把两种积分约定混写。若Z为连续局部鞅，减去Hessian二阶项后是局部鞅；把这作为∇鞅的内在定义。反向在一图取截断坐标测试，其有限变差部分给U dA=0，其中Z=M+A是反发展的分解。U可逆，积分U⁻¹使A为常数，因此Z是局部鞅。

因而一个∇鞅在普通坐标里可以有漂移，β=b+½Γ:a才是应为零的量。球面Brownian在环境空间的法向漂移与这一点相容：环境坐标并不把球面的联络变成欧氏平移。不同联络可能给不同的鞅概念；坐标相容本身并不替我们选择几何。

## 4. 真正可用的非爆炸条件

<a id="development-proof-lyapunov"></a>

\[ V\in C^2(M),\quad V\ge1,\quad\{V\le r\}\ \hbox{compact},\quad AV\le cV,\ c\ge0
\quad\Longrightarrow\quad P_x(\zeta=\infty)=1. \]

令τᵣ为首次达到V=r。停止在紧子水平集内，Itô鞅系数有界，故可取期望；Gronwall给EₓV(Xₜ∧τᵣ)≤\(e^{ct}\)V(x)。连续性给rP(τᵣ≤t)≤此上界。令r趋∞，寿命的紧退出定义给P(ζ≤t)=0，再对整数t统一。若c为局部时间上界，有限T以其积分取代ct，同一证明成立。本页没有由任意形式曲率条件直接宣称非爆炸。

若M紧，最大解根本不可能离开所有紧集，故所有光滑Brownian向量场扩散均非爆炸。非紧空间上，度量完备只控制有限长度曲线的端点；它不自动给上述生成元估计。对局部有限变差Z的发展，正交U使X的Riemannian长度等于Z的欧氏总变差。若度量完备，有限时段尾部长度趋0，X为Cauchy并有端点；连接方程沿有限变差曲线的有界系数又给U极限，故可以延长。Brownian无限总变差不满足这条论证的前提。

## 5. 一张测地完备但Brownian会爆炸的曲面

<a id="development-proof-incomplete"></a>

\[ g=dr^2+f(r)^2d\theta^2,\quad f(r)=r\ (r\le1),\quad f(r)=e^{r^3}\ (r\ge2),\qquad
\frac12\Delta_{\rm radial}=\frac12\frac{d^2}{dr^2}+\frac{f'(r)}{2f(r)}\frac d{dr}. \]

在1<r<2选任意正的光滑插值，近0的度量正好欧氏，故这是整个R²上的光滑曲面，不是在原点留洞。任何曲线长度至少是其径向变化，且径向线实现从原点到r的距离r。因此闭度量球紧，Cauchy列有收敛子列并整体收敛。测地线速度恒定，在有限时间r有界；紧基集上固定长度速度的切丛子集紧，ODE延长又直接证明测地完备，不需要把Hopf–Rinow当未证前提。

Brownian半径在r>R≥2、到达R以前满足一维SDE，漂移为3r²/2。其构造来自已证Δ生成元与局部椭圆律，不猜测径向过程。记S(r)=∫ᴿʳ1/f(y)dy、v(r)=2∫ᴿʳ[∫ᴿʸf(z)dz]/f(y)dy。直接微分得LS=0、Lv=1。对R<L，用36章已经证明的停止命中计算可得下式；也可对有界区间直接Itô取期望得到。

\[ S(r)=\int_R^r\frac{dy}{f(y)},\quad v(r)=2\int_R^r\frac{\int_R^y f(z)\,dz}{f(y)}\,dy,\quad
P_r(\tau_L<\tau_R)=\frac{S(r)}{S(L)}. \]

这里S(∞)<∞。而d[\(e^{y^3}\)/(3y²)]/dy=\(e^{y^3}\)(1−2/(3y³))≥½\(e^{y^3}\)于y≥2，故∫ᴿʸf≤2f(y)/(3y²)，v(∞)<∞。停止v给Eᵣ(τᴿ∧τᴸ)≤v(∞)−v(r)，统一于L；先停有限t再以单调收敛放开，所有期望合法。

事件{τᴸ<τᴿ}随L增加而递减，其交的概率为S(r)/S(∞)>0。在这个交上，τᴸ递增到一个有限时刻，因为其共同停止时间有统一有限期望；半径越过所有L，正是最大过程的爆炸。几何没有有限距离的缺口，概率过程仍会在有限时间逃向无穷。这同时说明测地完备不能替代随机完备，也不能用有限变差发展的长度证明处理Brownian。

## 6. 缺口、坐标极点与边界规则并不相同

<a id="development-proof-boundary"></a>

另一方向也不能反推。欧氏穿孔平面R²\{0}不是测地完备，但Brownian不会命中原点。38章已证的环域计算给Pᵣ(先达ε再达R)=log(R/r)/log(R/ε)→0。对整数R取并，原点从未命中；在每个有限时段，普通平面Brownian连续，既有有限最大半径，也因不命中0而有正最小半径。因此其在穿孔平面中的紧退出寿命仍无限。

在半直线内点同有生成元½∂²，停止在0并吸收与在0反射却不是同一过程。取R=|x+B|，37章Tanaka给R=x+∫sgn(x+B)dB+L⁰(x+B)。普通时间在0的占用为0，故积分括号为t，33章刻画使它为Brownian。对满足f′(0)=0的C²测试，局部时间项消失，给反射的Neumann规则。吸收过程在任何固定正时刻有正的0点质量，反射过程的固定时刻绝对值Gaussian无原子；两律确实不同。

主定理对无边界流形的最大内点过程负责；反射、粘滞、弹性边界的一般分类并未由一个内部Laplace算子完成。源头清楚以后，读者可以分别追问：坐标是否换坏了，是否真正离开状态空间，以及是否另选了边界物理规则。[回正文](../chapters/40-stochastic-geometry.md#geometry-lifetime)。
