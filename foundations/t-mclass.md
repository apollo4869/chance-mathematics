# 生成类为什么足以决定整个可测世界？

本篇从第五章的可测集合出发，补足第六章乘积积分、第八章无限实验和第十章概率核所需的集合与函数推广工具。下面的论证只使用集合运算、可数可加性和实数极限，不把待建立的积分交换结论当作前提。

<a id="t-mclass-pi-lambda"></a>

## T-MCLASS.1 从矩形或柱集走向所有事件

设 \(\Omega\) 是集合。一个集合族 \(\mathcal P\) 若对有限交封闭，称为 \(\pi\)-系统；允许包含空集。一个集合族 \(\mathcal D\) 若包含 \(\Omega\)，对补集及可数不交并封闭，称为 \(\lambda\)-系统。后一条件比 \(\sigma\)-代数弱，因为暂时不能把有重叠的事件任意相并。

先记录一个小事实：若 \(A\subseteq B\) 且二者属于 \(\mathcal D\)，则 \(B\setminus A\in\mathcal D\)。因为 \(B^c\) 与 \(A\) 不交，先取它们的并再取补集即可。若 \(A_n\uparrow A\)，各差集 \(A_n\setminus A_{n-1}\) 因而属于 \(\mathcal D\)，不交并给出 \(A\in\mathcal D\)。

**π–λ 定理。** 包含一个 \(\pi\)-系统 \(\mathcal P\) 的任意 \(\lambda\)-系统，都包含 \(\sigma(\mathcal P)\)。

取所有包含 \(\mathcal P\) 的 \(\lambda\)-系统之交，记为 \(\mathcal L\)。交仍满足三个条件。我们要证明，交运算这个原本缺失的能力，会由 \(\mathcal P\) 传给整个 \(\mathcal L\)。不妨先把 \(\Omega\) 加入 \(\mathcal P\)，这不改变生成的 \(\sigma\)-代数，也不破坏有限交。

固定 \(A\in\mathcal P\)，令 \(\mathcal L_A=\{B:A\cap B\in\mathcal L\}\)。它包含全集；对于补集，使用 \(A\cap B^c=A\setminus(A\cap B)\) 和刚才的嵌套差集性质；对于不交并，交集仍不交。因此它是 \(\lambda\)-系统。它又包含 \(\mathcal P\)，故 \(\mathcal L\subseteq\mathcal L_A\)。我们得到一边属于 \(\mathcal P\)、另一边属于 \(\mathcal L\) 时的交闭合性。

再固定 \(B\in\mathcal L\)，对 \(\{A:A\cap B\in\mathcal L\}\) 重复同一个检验。上一段保证这个 \(\lambda\)-系统包含 \(\mathcal P\)，所以它包含 \(\mathcal L\)。这一次两边都可以属于 \(\mathcal L\)。于是 \(\mathcal L\) 对有限交、补集及有限并封闭。任意可数并可先改写为逐项去掉前项后的不交并，故 \(\mathcal L\) 是 \(\sigma\)-代数。它必然包含 \(\sigma(\mathcal P)\)，定理得证。

<a id="t-mclass-set"></a>

## T-MCLASS.2 集合单调类：极限运算怎样补出 σ-代数

称集合族为单调类，如果它对递增可数并与递减可数交封闭。**集合单调类定理**说：包含代数 \(\mathcal A\) 的最小单调类正是 \(\sigma(\mathcal A)\)。这里代数包含全集，对补集与有限并封闭；只含一个 \(\pi\)-系统还不够，不能把两种定理的假设混用。

设最小单调类为 \(\mathcal M\)。类 \(\{E:E^c\in\mathcal M\}\) 仍是单调类并包含 \(\mathcal A\)，所以 \(\mathcal M\) 对补集封闭。固定 \(A\in\mathcal A\)，类 \(\{E:A\cap E\in\mathcal M\}\) 是包含 \(\mathcal A\) 的单调类，故包含 \(\mathcal M\)。再固定 \(E\in\mathcal M\)，重复这一检验，把另一边也从 \(\mathcal A\) 推广到 \(\mathcal M\)。因此 \(\mathcal M\) 对有限交、补集和有限并封闭。

任意 \(E_n\in\mathcal M\) 的有限并递增趋于其可数并，故后者仍属于 \(\mathcal M\)。这证明 \(\mathcal M\) 是 \(\sigma\)-代数，因而包含 \(\sigma(\mathcal A)\)。反向包含成立，因为任何 \(\sigma\)-代数本身就是单调类。

<a id="t-mclass-function"></a>

## T-MCLASS.3 函数单调类：从指标到所有有界观察

设 \(\mathcal H\) 是有界实函数的向量空间，包含常数1；若 \(f_n\in\mathcal H\) 一致有界且逐点非降趋于 \(f\)，则 \(f\in\mathcal H\)。若它还包含一个 \(\pi\)-系统 \(\mathcal P\) 的全部指标函数，那么它包含所有有界 \(\sigma(\mathcal P)\)-可测实函数。

证明只需把集合论工具装进指标。令 \(\mathcal D=\{A:\mathbf1_A\in\mathcal H\}\)。全集和补集由1与向量空间性质处理；不交并的指标是有限部分和的有界递增极限。因此 \(\mathcal D\) 是包含 \(\mathcal P\) 的 \(\lambda\)-系统，π–λ 定理给出全部生成事件。非负有界可测函数由逐点递增的有界简单函数逼近；一般有界实函数加上一个足够大的常数后变成非负函数。每一步都留在 \(\mathcal H\)，证明完成。复函数分别处理实部与虚部。

还有常用的代数版本：若 \(\mathcal H\) 包含一个有界实函数代数 \(\mathcal A\)，其中有1且对乘法封闭，那么它包含全部有界 \(\sigma(\mathcal A)\)-可测函数。为免把函数代数的假设悄悄换成指标假设，我们补出这一步。

先证 \(\mathcal H\) 对一致极限封闭。若 \(f_n\in\mathcal H\) 一致趋于 \(f\)，取子列使 \(\|f_n-f\|_\infty\le4^{-n}\)，记 \(d_n=2\cdot4^{-n}\)、\(r_n=\sum_{k\ge n}d_k\)。于是 \(f_n-r_n\) 一致有界、逐点非降并趋于 \(f\)，因为 \(\|f_{n+1}-f_n\|_\infty\le d_n\)。故 \(f\in\mathcal H\)。

对区间 \([0,1]\) 上的连续函数 \(u\)，Bernstein 多项式 \(B_nu(x)=\sum_{k=0}^nu(k/n)\binom nk x^k(1-x)^{n-k}\) 一致逼近 \(u\)：若 \(K\) 服从参数 \((n,x)\) 的二项分布，则该多项式是 \(\mathbb Eu(K/n)\)，而 \(\operatorname{Var}(K/n)\le1/(4n)\)。把差分成 \(|K/n-x|\le\delta\) 与其补集，用一致连续性和 Chebyshev 不等式，得到下式。

\[
\sup_{0\le x\le1}|B_nu(x)-u(x)|\le\omega_u(\delta)+\frac{2\|u\|_\infty}{4n\delta^2}.
\]

先令 \(n\to\infty\)，再令 \(\delta\downarrow0\)。经仿射换元，同样结论适用于任意紧区间。于是对 \(f\in\mathcal A\) 及其值域上的连续 \(u\)，多项式逼近给出 \(u(f)\in\mathcal H\)。对有限个 \(f_i\in\mathcal A\)，各个连续函数的乘积也能由对应多项式的乘积一致逼近；这些乘积属于 \(\mathcal A\)，所以极限属于 \(\mathcal H\)。

取连续斜坡 \(u_{i,k}(x)=\min(1,k(x-a_i)_+)\)。乘积 \(\prod_i u_{i,k}(f_i)\) 非降趋于 \(\mathbf1_{\cap_i\{f_i>a_i\}}\)，故这些有限交的指标都在 \(\mathcal H\)。它们构成生成 \(\sigma(\mathcal A)\) 的 \(\pi\)-系统；应用已经证明的指标版本即可。这也说明，函数单调类不是把“所有可测函数”当作一个没有说明的极限步骤。

<a id="t-mclass-uniqueness"></a>

## T-MCLASS.4 测度唯一性及其有限性边界

设 \(\mu,\nu\) 是同一可测空间上的有限测度，总质量相同，并在生成 \(\sigma\)-代数的 \(\pi\)-系统 \(\mathcal P\) 上相同。则 \(\mu=\nu\)。事实上，\(\mathcal D=\{A:\mu(A)=\nu(A)\}\) 包含全集；补集等式来自有限总质量相减，不交并等式来自可数可加性。因此 \(\mathcal D\) 是 \(\lambda\)-系统，应用前面的定理即可。

σ-有限版本需要一份共同的有限覆盖：存在 \(E_n\in\mathcal P\)，使 \(\bigcup_nE_n=\Omega\) 且 \(\mu(E_n)=\nu(E_n)<\infty\)。固定 \(n\)，有限测度 \(A\mapsto\mu(A\cap E_n)\) 与相应的 \(\nu\) 在 \(\mathcal P\) 上相同，故在整个生成的 \(\sigma\)-代数上相同。令 \(D_n=E_n\setminus\bigcup_{j<n}E_j\)；它们可测且不交。分别在 \(D_n\) 上相等，再可数求和，得到一般事件上的相等。

缺少有限性时，相同的生成读数未必唯一。实线上计数测度与“每个非空集合都赋值 \(\infty\)”的测度，在全部非空有理端点开区间上都取 \(\infty\)，却在单点上分别取1与 \(\infty\)。把空集加入这族区间便得到生成 Borel 集的 \(\pi\)-系统。不能在 \(\infty-\infty\) 上重演有限测度的补集证明。

<a id="t-mclass-applications"></a>

## T-MCLASS.5 本书中真正需要的几种用法

实线概率由全部半直线 \(( -\infty,q]\)、\(q\in\mathbb Q\) 的概率唯一决定：它们加上全集构成 \(\pi\)-系统；任意实阈值可由有理阈值递降逼近，而这些半直线生成 Borel 集。这就是分布函数唯一性的集合论根据。第十一章的连续斜坡先恢复这些概率，再由本结论得到整份分布。

乘积矩形与有限坐标柱集也对有限交封闭。概率测度在所有柱集上一致，就在柱集生成的乘积 \(\sigma\)-代数上一致，无论指标集是否可数。这个结论不把任意路径子集自动变成可测事件。若谈 σ-有限乘积测度的唯一性，必须先使用有限测度矩形的共同可数覆盖，不能省掉上一节的定位。

第十章概率核的推广则固定一个状态，检查某性质成立的事件类是否为 \(\lambda\)-系统，再从矩形推广。不同状态各自成立的性质，不等于已经处理了不可数多个状态的共同零集；共同零集仍须用可数生成类和版本选择另作论证。

相关基础：[积分、零集与DCT](t-integral.md#t-integral-dct)；[完备化与Borel编码](t-measure.md#t-measure-completion)。
