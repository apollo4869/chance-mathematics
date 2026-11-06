# T-GEOMETRY：坐标、度量、联络与标架的实际基础

配套[第40章](../chapters/40-stochastic-geometry.md#geometry-atlas)。固定有限维、Hausdorff、第二可数、无边界的光滑流形M。一般带边界的延拓另作问题，不藏进坐标定义。这里先完成本章实际使用的确定性工具，不调用Nash嵌入或一般曲率比较。

## 1. 图册为什么能容纳全局拼接

<a id="geometry-proof-atlas"></a>

坐标图是开集U到Rⁿ开集的同胚x；重叠上的变换光滑且逆光滑。第二可数使相对紧坐标小球有可数子覆盖。可取紧集Kₘ⊂int Kₘ₊₁耗尽M：先用可数相对紧球的有限并递增，再在每一步把前一紧集包含进有限个更大的相对紧球并取闭包。每个紧环Kₘ₊₁∖int Kₘ₋₁有有限个坐标球，所取小球的闭包落在较大坐标球内；只让这些球出现在相邻几个环中，便得到局部有限的较小球覆盖Pⱼ及较大图域Qⱼ。

欧氏球内用exp(−1/(1−|z|²))的缩放、平移及有限和构造光滑非负函数ρⱼ，支撑紧含Qⱼ、在闭Pⱼ上正。局部有限性使ρ=Σρⱼ光滑且处处正，φⱼ=ρⱼ/ρ遂为光滑单位分解。对给定开覆盖，先把Qⱼ缩进某个覆盖成员，即得到从属分解。特别地，紧集K含于开集U时，可用有限个这样的函数及光滑截断做出等于1于K附近、紧支撑在U内的函数。

本页所用欧氏局部逆定理也可直接核验：若DF(a)=A可逆，在小球使‖I−A⁻¹DF‖<1/2，则x↦x+A⁻¹(y−F(x))为收缩，并把适当闭小球映入自身。迭代得到唯一逆，差分积分给逆Lipschitz界；对身份F(F⁻¹(y))=y求差商，再递归求导，得到与F相同阶的光滑逆。这足以处理后面的局部嵌入与指数图，不以一个未证的几何定理代替。

## 2. 切向量不是一组固定的分量

<a id="geometry-proof-tangent"></a>

在p处把切向量定义为光滑函数芽上的线性导子v，满足v(fh)=f(p)v(h)+h(p)v(f)。局部Taylor积分公式f(x)−f(p)=Σ(xⁱ−pⁱ)∫₀¹∂ᵢf(p+s(x−p))ds说明v=Σv(xⁱ)∂ᵢ，所以切空间恰为n维。常数导数为0；二阶余项被Leibniz消去。坐标改变后的分量遂由一阶Jacobian给出，而不是额外约定。

\[ v_y^a=\frac{\partial y^a}{\partial x^i}v_x^i,\qquad \alpha_x=\alpha_i\,dx^i,\qquad \alpha(v)=\alpha_i v^i. \]

余切空间是切空间的对偶；一形式以此保持配对。光滑向量场是坐标分量光滑的切向量选择，作为一阶微分算子作用于函数。其括号[V,W]f=V(Wf)−W(Vf)仍满足Leibniz，故也是向量场。局部常微分方程的唯一性来自35章Picard的确定性特例；坐标链式法则使它们在重叠区相同，得到最大流曲线。

## 3. 度量怎样决定一种联络

<a id="geometry-proof-connection"></a>

Riemannian度量是每个切空间上的正定内积，坐标矩阵g光滑；单位分解把局部欧氏度量拼成全局度量。它测量曲线长度，但还没有直接规定怎样比较不同点的切向量。联络∇给出沿V微分W的规则：对第一变量函数线性，对第二变量满足∇ᵥ(fW)=V(f)W+f∇ᵥW。局部写∇ᵢ∂ⱼ=Γᵏᵢⱼ∂ₖ，所有其他值由这两条规则决定。

\[ \Gamma^k_{ij}=\frac12g^{k\ell}(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij}),\qquad \nabla_VW=V^i(\partial_iW^k+\Gamma^k_{ij}W^j)\partial_k. \]

要求无挠∇ᵥW−∇𝑤V=[V,W]，并保持度量Vg(W,Z)=g(∇ᵥW,Z)+g(W,∇ᵥZ)。在坐标基上得到Γ下标对称及下面的度量微分身份。交换三个指标，加两式减一式并乘逆度量，就唯一得到上面的Christoffel式；代回又验证两项要求，故存在且唯一。

\[ \partial_i g_{jk}=\Gamma^\ell_{ij}g_{\ell k}+\Gamma^\ell_{ik}g_{j\ell},\qquad \Gamma'^a_{bc}=\frac{\partial y^a}{\partial x^k}\Gamma^k_{ij}\frac{\partial x^i}{\partial y^b}\frac{\partial x^j}{\partial y^c}+\frac{\partial y^a}{\partial x^k}\frac{\partial^2x^k}{\partial y^b\partial y^c}. \]

后一变换式由对W的坐标链式法则直接得到；它的二阶项使∇ᵥW真正按切向量变换。无挠和度量相容本身与坐标无关，故唯一性也证明各图的Christoffel公式拼成同一个Levi–Civita联络。不能把Γ本身当成张量。

## 4. Hessian与Laplace–Beltrami

<a id="geometry-proof-laplacian"></a>

\[ \operatorname{Hess}f(V,W)=V(Wf)-(\nabla_VW)f,\qquad \Delta_g f=g^{ij}(\partial_{ij}f-\Gamma^k_{ij}\partial_kf)=\frac1{\sqrt{|g|}}\partial_i(\sqrt{|g|}\,g^{ij}\partial_jf). \]

Leibniz使Hessian对V、W均为函数线性；无挠使它对称，因此度量迹不依赖坐标。散度形式不是另一种未经核验的定义：对行列式的Leibniz展开求导给∂log|g|=tr(g⁻¹∂g)，对g⁻¹g=I求导给∂g⁻¹=−g⁻¹(∂g)g⁻¹。将它们与前节Christoffel式代入，得到∂ᵢgⁱʲ+½gⁱʲ∂ᵢlog|g|=−gⁱᵏΓʲᵢₖ，恰为两式一阶项相同。

若E₁,…,Eₙ是局部正交标架，按Hessian的定义逐项取迹得Δf=Σ(Eᵢ²f−(∇Eᵢ Eᵢ)f)。因此仅把ΣEᵢ²称为Laplace算子会漏掉一个向量场。光滑紧支撑测试的分部积分可在单图用散度式证明，再以单位分解求和；这给形式对称的能量身份，不单独证明全局热核或长期不变分布。

## 5. 紧区域中的可核验嵌入

<a id="geometry-proof-local-embedding"></a>

给定紧K，取有限图域及支撑在其中的ρⱼ，使每点至少一个ρⱼ>0。把所有ρⱼ和ρⱼxⱼⁱ作为全局光滑函数（支撑外延0），合成F。若F(p)=F(q)且p∈K，取ρⱼ(p)>0，便有同一图中的xⱼ(p)=xⱼ(q)，故p=q。若dF(v)=0，同样先由dρⱼ(v)=0再得ρⱼdxⱼ(v)=0，故v=0。缩小K的邻域可得局部浸入；F在K上为连续单射，紧性和Hausdorff性使其逆连续。

对一个已给定的光滑嵌入i:M→Rᴺ，满秩子式与第1节逆函数论证给局部环境坐标，把i(M)写成{z″=0}。光滑f或向量场的各分量先保持不随z″变化，再乘环境小球截断；有限单位分解在紧区域拼合，给光滑环境延拓。这个局部延拓足够核对投影SDE。我们没有从这里推出所有Riemannian流形都存在全局等距嵌入；Brownian的一般构造不依赖那条定理。

## 6. 正交标架本身构成一个流形

<a id="geometry-proof-frames"></a>

O(M)的点u是Rⁿ到TₓM的线性等距映射。用度量Gram–Schmidt把坐标基变成光滑局部正交基E(x)，则u=E(x)q、q∈O(n)。O(n)的局部图可在恒等元附近用反对称矩阵A的Cayley变换(I−A)⁻¹(I+A)，逆为(q−I)(q+I)⁻¹；平移这些图覆盖O(n)。因此O(M)有明确的光滑局部乘积图，不是抽象符号。其在任一紧基集之上的逆像紧，因为有限个局部平凡化和紧纤维O(n)覆盖它。

\[ H_i=u_i^k\frac{\partial}{\partial x^k}-\Gamma^k_{\ell m}u_i^\ell u_j^m\frac{\partial}{\partial u_j^k},\qquad H_i\big(g_{k\ell}u_j^ku_r^\ell\big)=0. \]

上式规定沿uᵢ前进时同时平行移动全部标架向量。后一身份由第3节度量相容式逐项相消，证明Hᵢ切于O(M)；Γ的变换式证明各图表达相同。对常正交矩阵q，右作用R_q(u)=uq满足Hᵢ(uq)=(R_q)₊ΣⱼqⱼᵢHⱼ(u)。这里推前符号只表示微分作用；它将给Brownian初始标架选择的旋转等价。

\[ H_i(uq)=(R_q)_*\sum_jq_{ji}H_j(u). \]

## 7. 平行移动、测地线与等距映射

<a id="geometry-proof-transport"></a>

\[ \dot u_j^k=-\Gamma^k_{\ell m}(x)\dot x^\ell u_j^m,\qquad \ddot x^k+\Gamma^k_{ij}(x)\dot x^i\dot x^j=0. \]

第一式是给定C¹曲线上的线性ODE，局部存在唯一；度量相容保持所有内积，有限区间沿曲线的紧像使标架有界并可拼接。第二式定义测地线；度量相容使其速度范数恒定。因而在紧流形上，有限时间内基点与固定长度速度都留在紧的切丛子集，ODE可延长。对非紧流形不能只由局部方程推出同样结论。

若Φ是全局光滑Riemannian等距同胚，把联络推前仍无挠且保持目标度量，唯一性使其等于目标Levi–Civita联络。因此Φ保持Hessian迹、平行移动和水平向量场。单纯改变坐标时度量分量也必须随之变换；固定一套欧氏度量再改变方程则可能真的改变运动。[回正文](../chapters/40-stochastic-geometry.md#geometry-isometry)。
