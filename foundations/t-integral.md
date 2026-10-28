# 积分从哪里获得线性？——零集、极限与任意测度空间

本篇在任意测度空间 \((S,\mathcal F,\mu)\) 上工作，不预设有限性、σ-有限性或完备性。我们先从非负简单函数建立积分的代数，再证明极限原则。这样，第六章里看似自然的“把和拆开”，才有不依赖所求结论的根据。

<a id="t-integral-simple"></a>

## T-INTEGRAL.1 简单函数与非负积分

对有限值非负简单函数 \(s=\sum_{j=1}^ra_j\mathbf1_{A_j}\)，其中 \(A_j\) 两两不交、\(a_j\ge0\)，定义 \(I(s)=\sum_ja_j\mu(A_j)\)，约定 \(0\cdot\infty=0\)。不同表示可用全部集合的有限交细分为共同分区，有限可加性保证定义与表示无关。相同细分还给出简单函数的非负线性性与保序性；即使某项测度为无穷，也没有做无穷量的相减。

对可测 \(f:S\to[0,\infty]\)，定义 \(I(f)=\sup\{I(s):0\le s\le f,\ s\text{ simple}\}\)。因此 \(f\le g\) 蕴含 \(I(f)\le I(g)\)，而 \(I\) 在简单函数上与刚才的定义一致。每个这样的 \(f\) 有非负简单函数逼近：

\[
s_n=2^{-n}\left\lfloor2^n\min(f,n)\right\rfloor,\qquad 0\le s_n\uparrow f.
\]

每个 \(s_n\) 只有有限多个值，且其水平集可测；二进网格细化与上限增大保证非降。有限 \(f\) 处的误差最终小于 \(2^{-n}\)，而 \(f=\infty\) 处有 \(s_n=n\)。这一步同时给出了后面反复使用的可测简单逼近。

<a id="t-integral-mct"></a>

## T-INTEGRAL.2 不借线性性证明单调收敛

若 \(0\le f_n\uparrow f\)，保序性先给 \(L:=\lim_nI(f_n)\le I(f)\)。固定简单函数 \(0\le s\le f\) 及 \(0<c<1\)，令 \(E_n=\{f_n\ge cs\}\)。在 \(s>0\) 的每一点，因 \(f_n\uparrow f\ge s>cs\)，该点最终进入 \(E_n\)。因此 \(E_n\) 递增，且其并包含 \(\{s>0\}\)。

把 \(s\) 写成不交水平集的有限和，测度从下连续性逐项给出 \(I(s\mathbf1_{E_n})\uparrow I(s)\)。由 \(f_n\ge cs\mathbf1_{E_n}\) 得 \(L\ge cI(s)\)。若 \(I(s)=\infty\)，已得 \(L=\infty\)；否则令 \(c\uparrow1\)，再对全部 \(s\) 取上确界，得到 \(L\ge I(f)\)。这证明 MCT，且对任意测度空间成立。

<a id="t-integral-linearity"></a>

## T-INTEGRAL.3 非负线性性、可数求和与积分为零

为非负可测 \(f,g\) 分别取上述 \(s_n\uparrow f\)、\(t_n\uparrow g\)。简单函数的线性性和刚证明的 MCT 给出

\[
\int(f+g)\,d\mu=\lim_n\int(s_n+t_n)\,d\mu=\int f\,d\mu+\int g\,d\mu.
\]

同理，对有限常数 \(c>0\) 有 \(\int cf=c\int f\)；\(c=0\) 时按 \(0\cdot\infty=0\) 处理。有限和以后，MCT 作用于部分和，得到非负函数的可数求和公式。这不是要求函数在每一点都可求和的额外假设，允许两边为 \(\infty\)。

\[
\int\sum_{n=1}^\infty f_n\,d\mu=\sum_{n=1}^\infty\int f_n\,d\mu,\qquad f_n\ge0.
\]

若 \(f\ge0\)，则 \(\int f=0\) 当且仅当 \(f=0\) 几乎处处。一方面，\(\mu\{f\ge1/k\}\le k\int f=0\)，可数并给出 \(\mu\{f>0\}=0\)。另一方面，若 \(f\) 只在可测零集上非零，则其下每个简单函数的正水平集都为零测，故积分上确界为零。这也覆盖 \(f\) 在零集上取无穷大的情形。

<a id="t-integral-null"></a>

## T-INTEGRAL.4 零集修改什么时候合法？

设 \(f,g\ge0\) 都可测，并在可测零集 \(N\) 外相同。分成 \(N\) 与 \(N^c\)，由线性性和上一节知 \(\int f=\int g\)。所以积分不受可测的零集修改影响。**两个函数都可测**不可略去：在未完备空间中，零集的任意子集未必是事件，其指标也未必可测。一般完备化的完整构造见[测度基础](t-measure.md#t-measure-completion)。

若可测 \(f_n\) 在某个可测零集之外有极限，先把该零集上所有 \(f_n\) 定义成0，再取上极限，就得到可测极限版本。可测性来自 \(\limsup f_n=\inf_m\sup_{n\ge m}f_n\) 的可数运算；不能从“存在一个几乎处处相等的函数”无条件推出任意指定版本可测。

<a id="t-integral-signed"></a>

## T-INTEGRAL.5 可积实函数与复函数

若 \(f\) 实值可测且 \(\int|f|<\infty\)，定义 \(\int f=\int f^+-\int f^-\)。两个量都有限，因而相减合法。由非负线性性及逐点恒等式 \((f+g)^++f^-+g^-=(f+g)^-+f^++g^+\)，积分后整理得可积实函数的线性性；\(|f+g|\le|f|+|g|\) 先保证和可积。

由 \(-|f|\le f\le|f|\) 得 \(|\int f|\le\int|f|\)。复函数按实部、虚部分别定义积分。取单位复数 \(z\) 使 \(z\int f\) 为非负实数，对 \(\operatorname{Re}(zf)\le|f|\) 积分，同样得到复数三角不等式。若积分为0，无需选方向。非负扩展积分允许无穷大，但有符号积分不得写出未定义的 \(\infty-\infty\)。

<a id="t-integral-dct"></a>

## T-INTEGRAL.6 Fatou 与 DCT：不需要 σ-有限的证明

对非负可测 \(f_n\)，令 \(g_m=\inf_{n\ge m}f_n\)。则 \(g_m\uparrow\liminf_n f_n\)，而 \(\int g_m\le\inf_{n\ge m}\int f_n\)。MCT 给出 Fatou 引理。若不等式或收敛只在几乎处处成立，先按上一节在共同的可测零集上修改版本。

现在设 \(f_n\to f\) 几乎处处，\(f_n,f\) 为可测实函数或复函数，且对所有 \(n\) 有 \(|f_n|\le g\) 几乎处处，其中 \(g\ge0\)、\(\int g<\infty\)。\(g=\infty\) 的集合为零测；将它与可数个例外集合并并取零版本后，可以在每一点使用 \(|f|\le g\) 与 \(0\le|f_n-f|\le2g\)。对非负函数 \(2g-|f_n-f|\) 使用 Fatou：

\[
2\int g\,d\mu\le\liminf_n\int(2g-|f_n-f|)\,d\mu=2\int g\,d\mu-\limsup_n\int|f_n-f|\,d\mu.
\]

这里所有被减的积分都有限。因此 \(\int|f_n-f|\to0\)，再由积分三角不等式得到 \(\int f_n\to\int f\)。这既证明 DCT，也给出 \(L^1\) 收敛。证明没有为整个空间寻找有限测度穷尽，没有用拓扑，也没有用 σ-有限性。

<a id="t-integral-support"></a>

## T-INTEGRAL.7 能穷尽的是控制函数的有效支集

第六章关于尾部控制的直觉可以严格保留，但范围必须说准。对于 \(g\in L^1_+(\mu)\)，令 \(E_m=\{g\ge1/m\}\)。Markov 型估计给出

\[
\mu(E_m)\le m\int g\,d\mu<\infty,\qquad E_m\uparrow\{g>0\},\qquad\int_{E_m^c}g\,d\mu\longrightarrow0.
\]

最后的极限由 MCT 作用于 \(g\mathbf1_{E_m}\) 再从有限的 \(\int g\) 相减得到。\(E_m\) 穷尽的是 \(\{g>0\}\)，不是未必 σ-有限的整个 \(S\)。例如，不可数集合上的计数测度没有可数个有限测度集覆盖全空间；但任意可积控制函数仍有上面的有效支集穷尽，DCT 仍成立。

另一种等价的组织方式是有限测度 \(\nu(A)=\int_Ag\,d\mu\)。非负可数求和公式保证 \(\nu\) 可数可加，总质量为 \(\int g\)。如果要控制小集合的贡献，先取 \(M\) 使 \(\int g\mathbf1_{\{g>M\}}<\varepsilon/2\)，再用

\[
\int_Ag\,d\mu\le M\mu(A)+\int g\mathbf1_{\{g>M\}}\,d\mu.
\]

取 \(\mu(A)<\varepsilon/(2M)\) 即可，必要时把 \(M\) 选成正数。这就是积分关于底层测度的绝对连续性。它来自一个可积函数的尾部，而不是来自整个空间具有有限体积。第五、六章的零集与积分基础，由此能够可靠地支撑第八章的扩张、第十章的密度及第十一章的 Gaussian 平滑。
