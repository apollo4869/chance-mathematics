# T-MASS-CLUSTERS：Poisson簇、随机线质量与Gamma测度

返回[第49章](../chapters/49-random-measures.md#mass-clusters)。目标E为LCSC度量空间；父空间S为标准Borel，a为σ有限测度；Q是S到非负Radon测度Polish空间的概率核。父出现可以重合，各次子测度条件独立。本页证明这个准确范围，不引用未来Palm树准则。

## 1. 标记到随机测度空间

<a id="cluster-construction"></a>

第48章标记Poisson定理给S×\(\mathcal M_+(E)\)上的PRM N，强度\(\lambda(dx,d\zeta)=a(dx)Q(x,d\zeta)\)。先把S分为有限a质量Borel片，各片有限Poisson父数，每个标记取完整Radon实现；可数独立拼接给N。其评价域由标准Borel结构生成，不要求父空间局部紧。定义扩展测度\(\Psi(A)=\int\zeta(A)N(dx,d\zeta)\)，以非负积分允许无穷。

ζ↦ζ(A)可测；对固定可数实现N，MCT把A的可数可加性保留为Ψ的可数可加性。T-MASS-KERNELS或简单函数逼近给每个Ψ(A)随机可测。对\(f\ge0\)，Tonelli给\(\Psi f=\int\zeta f\,dN\)。Poisson全非负可测泛函因此给出正文公式；先截断父片和ζf再MCT也得到同一表达式。未假定Ψ已经局部有限。

## 2. Poisson正积分的有限性与0–∞判据

<a id="cluster-finiteness"></a>

先证明一般引理。λ为σ有限强度，h≥0可测且λ-a.e.有限，N为PRM(λ)。则\(Nh<\infty\)a.s.当且仅当\(\lambda(1\wedge h)<\infty\)；若后式无穷，Nh=∞a.s.。若有限，\(\lambda\{h>1\}<\infty\)，故此区域只有有限N点，每个h值有限；而\(\mathbb E N(h\mathbf1_{h\le1})=\lambda(h\mathbf1_{h\le1})<\infty\)，故小项和有限a.s.。λ零集无点由零强度Poisson计数保证。

反向用\((1-e^{-1})(1\wedge h)\le1-e^{-h}\le1\wedge h\)。若截断积分发散，Poisson泛函给\(\mathbb E e^{-Nh}=e^{-\lambda(1-e^{-h})}=0\)。非负变量e⁻ᴺʰ的期望0，故Nh=∞a.s.。h有限a.e.不可删：若h在有限正强度集上为∞，出现至少一个点的概率严格介于0和1，不再有同样的0–∞结论。

对固定紧B取\(h(x,\zeta)=\zeta(B)\)，它处处有限，正好得到正文条件。对紧穷竭Bₘ，所有条件有限则在共同满概率集上Ψ局部有限，由T-RIESZ正则，故是随机Radon测度。任一个条件失败则Ψ(Bₘ)=∞a.s.，不属于这个空间。注意这是每个指定紧窗口的Poisson结构判据，不是给任意随机Radon测度套上的普遍零一律。

## 3. 均值、截断收敛及非Cox反例

<a id="cluster-laws"></a>

Campbell与Tonelli给\(\mathbb E\Psi f=\int\!\int\zeta f\,Q(x,d\zeta)a(dx)\)，不要求有限。父空间截到递增有限强度片，其子测度和Ψₙ逐集合递增到Ψ。在局部有限判据成立时，每个紧支撑f≥0有Ψₙf↑Ψf<∞；任意实f分正负部分，遂Ψₙ vague→Ψ逐实现。还可在每份ζ上用递增紧窗口截断；同样的MCT与共同可数测试给结论。不能把有符号、非单调截断直接归入这个证明。

平均有限比a.s.有限强。例如父总数Poisson(1)，每份子测度Zδ₀，其中Z为有限a.s.、均值无穷的正变量。判据的积分≤1，所以输出Radon，而平均单点质量无穷。若每份子测度改为2δ₀，输出计数2N。假如它是Cox，单点计数为混合Poisson，且其正概率非零迫使指导单点强度Λ₀以正概率正；于是P{计数1}=E[Λ₀exp(−Λ₀)]>0，矛盾。局部有限保证Λ₀有限a.s.。

另一方向有准确充分条件：若每份子点测度条件于随机Radon强度Λᵢ为PRM(Λᵢ)，且给全部父信息和强度以后各子点条件独立，强度和Λ=ΣΛᵢ局部有限a.s.，则条件Laplace泛函相乘给PRM(Λ)，所以输出Cox。先有限相乘再单调取极限；随后由塔式法则可只条件于Λ。不需要把父过程本身误当成指导测度。

## 4. 线测度的可测性、局部有限与平均

<a id="cluster-lines"></a>

取S=[0,π)×R、\(a(d\vartheta,dr)=(c/\pi)d\vartheta dr\)，c>0。令\(n_\vartheta=(\cos\vartheta,\sin\vartheta)\)、\(v_\vartheta=(-\sin\vartheta,\cos\vartheta)\)，定义\(\zeta_{\vartheta,r}f=\int_{\mathbb R}f(rn_\vartheta+tv_\vartheta)dt\)。参数与t的联合连续映射及非负Tonelli给所有Borel评价可测；对Cc测试也可直接积分。紧窗口位于半径R圆盘内时，只有|r|≤R的直线可贡献，该参数集a质量2cR，且单线窗口长度≤2R。故簇判据有限。

固定ϑ时，\((r,t)\mapsto rn_\vartheta+tv_\vartheta\)为正交坐标变换，绝对Jacobian1。因此\(\mathbb E\Lambda f=c\int f(x)dx\)对所有非负f成立。N在σ有限参数空间上可数a.s.，每条线的平面Lebesgue质量0，可数并仍0；每个实现Λ集中其上。Λ不是零测度a.s.：参数空间强度无穷，N非空a.s.，每条线有非零局部长度。于是每份实现奇异而平均弥散。这一差别严格成立，不依赖图像。

条件于Λ，构造PRM(ρΛ)，ρ>0。局部有限由Λ保证。以\(h(\vartheta,r)=\rho\int_{\ell_{\vartheta,r}}(1-e^{-f})d\mathcal H^1\)，先条件Poisson再对父直线用Poisson泛函，得\(L(f)=\exp\{-\int(1-e^{-h(\vartheta,r)})a(d\vartheta,dr)\}\)。对非零f，这一般不同于平均强度ρc dx对应的Poisson泛函：由于1−e⁻ʰ<h于h>0，指数的绝对值严格更小。这也直接证明沿线Cox不是普通平面Poisson。

## 5. Gamma质量及Dirichlet归一化

<a id="cluster-gamma"></a>

设H为E上的Radon概率，θ>0，在E×(0,∞)取σ有限强度\(\lambda(dx,ds)=\theta H(dx)s^{-1}e^{-s}ds\)。可数小s条带各有限强度，故第48章构造适用。以\(\zeta_{x,s}=s\delta_x\)为确定标记，联合可测由评价\(s\mathbf1_A(x)\)得到。定义\(\Gamma=\int s\delta_xN(dx,ds)\)。全空间质量判据

\[ \int(1\wedge s)\lambda(dx,ds)=\theta\left(\int_0^1e^{-s}ds+\int_1^\infty s^{-1}e^{-s}ds\right)<\infty. \]

故Γ(E)<∞a.s.。对a≥0，以\(1-e^{-as}=\int_0^a s e^{-us}du\)并用Tonelli，有\(\int_0^\infty(1-e^{-as})s^{-1}e^{-s}ds=\int_0^a(1+u)^{-1}du=\log(1+a)\)。代入Poisson泛函给正文Gamma泛函。对简单测试\(\sum_jt_j\mathbf1_{A_j}\)、不交Aⱼ，泛函分解，故Γ(Aⱼ)独立，且Laplace变换\((1+t_j)^{-\theta H(A_j)}\)。正形参数的Gamma密度积分给此变换，再用第13章唯一性识别；形参数0是恒0。

取A=E，\(\mathbb P\{\Gamma(E)=0\}=\lim_{t\to\infty}(1+t)^{-\theta}=0\)，故归一化合法、评价可测。每个有限分割的正形参数Gamma独立，使用第44章已证明的Gamma归一化Jacobian，\((\Gamma(A_j)/\Gamma(E))_j\)服从Dirichlet(θH(Aⱼ))；零形参数坐标删去后再补0。有限分割一致及评价域唯一性给该随机概率的Dirichlet过程律。这里不宣称无穷总基质量也能归一化；那需要另查总质量条件。
