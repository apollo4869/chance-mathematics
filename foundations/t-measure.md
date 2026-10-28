# 零集的全部子集，为什么改变了可测世界？

第五章把长度推广为测度，却留下两个需要完整回答的问题：为什么 Lebesgue 可测集真的比 Borel 集多，以及任意测度如何补进尚未可测的零集子集。本篇给出构造与集合论证明，不把“集合很多”当成严格包含的论证。

<a id="t-measure-completion"></a>

## T-MEASURE.1 任意测度的完备化

设 \((S,\mathcal F,\mu)\) 是任意测度空间。令 \(\mathcal N=\{N:N\subseteq Z\in\mathcal F,\ \mu(Z)=0\}\)，并定义 \(\overline{\mathcal F}=\{A\triangle N:A\in\mathcal F,N\in\mathcal N\}\)。这里 \(\triangle\) 是对称差；\(N\) 自己暂时不必属于 \(\mathcal F\)。等价地，\(E\in\overline{\mathcal F}\) 当且仅当存在旧可测集合 \(A\subseteq E\subseteq B\)，且 \(\mu(B\setminus A)=0\)。

两种形式相同：若 \(E=A_0\triangle N\)、\(N\subseteq Z\) 且 \(\mu Z=0\)，取下夹集 \(A_0\setminus Z\) 与上夹集 \(A_0\cup Z\)；反过来，夹在 \(A,B\) 之间的集合只比 \(A\) 多出 \(B\setminus A\) 的一个子集。补集满足 \(E^c=A_0^c\triangle N\)；可数并与旧可测并的对称差包含在 \(\bigcup_nN_n\subseteq\bigcup_nZ_n\) 内。因此 \(\overline{\mathcal F}\) 是包含 \(\mathcal F\) 的 \(\sigma\)-代数。

定义 \(\overline\mu(A_0\triangle N)=\mu(A_0)\)。若还有另一表示 \(B_0\triangle M\)，则 \(A_0\triangle B_0\) 包含在一个旧可测零集内。删去该零集后，\(A_0,B_0\) 相同；由测度可加性，给集合加减零集不改变其测度。因此定义无关表示，即使 \(\mu(A_0)=\infty\) 也成立，没有使用无穷减无穷。

还要证明可数可加性。若 \(E_i=A_i\triangle N_i\) 两两不交，取旧零集 \(Z_i\supseteq N_i\)。旧可测核心 \(C_i=A_i\setminus Z_i\) 包含在 \(E_i\) 内，因而两两不交，且 \(\mu C_i=\mu A_i\)。\(\bigcup_iE_i\) 与 \(\bigcup_iC_i\) 的差包含在旧零集 \(\bigcup_iZ_i\) 中，所以

\[
\overline\mu\Bigl(\bigcup_iE_i\Bigr)=\mu\Bigl(\bigcup_iC_i\Bigr)=\sum_i\mu(C_i)=\sum_i\overline\mu(E_i).
\]

若 \(\overline\mu(E)=0\)，上面的表示把 \(E\) 放在旧可测零集 \(A_0\cup Z\) 内。因此 \(E\) 的任意子集都属于 \(\overline{\mathcal F}\) 且测度为零。这证明完备性。任何包含旧空间的完备测度扩张都必须容纳这些零集子集，故必须包含 \(\overline{\mathcal F}\)；夹集的上下界又迫使其在这里取值为 \(\overline\mu\)。完备化因此是最小的完备扩张，且在这个最小定义域上唯一。没有用 σ-有限性。

<a id="t-measure-cantor"></a>

## T-MEASURE.2 一个长度为零、却装得下连续统的集合

从 \([0,1]\) 逐次删去每个剩余区间的开中间三分之一。第 \(n\) 层剩余 \(2^n\) 个长 \(3^{-n}\) 的闭区间，记其并为 \(C_n\)，令 \(C=\bigcap_nC_n\)。它是闭集，且 \(m(C)\le(2/3)^n\) 对每个 \(n\) 成立，所以 \(m(C)=0\)。

每个二进序列 \(b=(b_1,b_2,\ldots)\in\{0,1\}^{\mathbb N}\) 给出 \(x(b)=\sum_{n\ge1}2b_n3^{-n}\in C\)。若两序列首次在 \(k\) 处不同，首个差值为 \(2\cdot3^{-k}\)，余下尾部至多抵消 \(3^{-k}\)，故得到不同的点。因此这个映射单射；不受一般三进表示端点二义性的影响。

二进序列的集合就是 \(\mathcal P(\mathbb N)\)，其基数记为 \(\mathfrak c\)。实数可由有理数的下截集编码，所以 \(|\mathbb R|\le\mathfrak c\)；刚才的单射给出反向不等式。于是 \(|C|=|\mathbb R|=\mathfrak c\)。这里没有采用连续统假设。

这里使用的基数比较也可直接证明。设单射 \(f:A\to B\)、\(g:B\to A\)。令 \(A_0=A\setminus g(B)\)、\(A_{n+1}=g(f(A_n))\)、\(U=\bigcup_{n\ge0}A_n\)。在 \(U\) 上取 \(h=f\)，其余点取 \(h=g^{-1}\)；后者有定义，因为它们不在 \(A_0\)。两部分各单射，像不交：若 \(b=f(x)\)、\(x\in U\)，则 \(g(b)\in U\)，不能同时来自另一部分。若 \(b\notin f(U)\)，则 \(g(b)\notin U\)，所以由后一部分映到 \(b\)。因此 \(h:A\to B\) 双射。这证明了 Cantor–Bernstein 原理。

<a id="t-measure-borel-code"></a>

## T-MEASURE.3 为什么 Borel 集至多只有连续统多个

“从可数区间做可数运算”本身不是基数证明，因为可数层之后还可继续迭代。正确的编码要容纳所有有限或可数的良基运算树。先枚举有理端点开区间。一个编码是一棵以有限整数序列为节点的可数树：叶子标记这些基本区间，内部节点标记补集或可数并；树不允许无限下降分支。

每棵这样的良基树可从叶子向上赋值。形式上，叶子秩为0，父节点的秩为各子节点秩加1后的上确界；按秩递归解释集合。这里的秩均为可数序数：每个节点只有可数个子节点，整树也可数。若逐次移去已赋秩节点仍有剩余，则每个剩余节点都有剩余子节点；依次选择便产生无限分支，矛盾。因此递归确实覆盖全树。我们在通常的 ZFC 集合论中使用可数选择与良基递归。

有编码的集合族包含基本区间，对补集与可数并封闭：添加一个根节点，下面接一棵树或可数棵已有树即可；任何无限分支都会在其中某棵子树中留下无限分支，所以新树仍良基。因此全部 Borel 集都有这种编码；反过来，按秩递归可知每个编码的值是 Borel 集。

有限整数序列的集合可数；一棵树及其节点标签可编码为一个可数集合的子集。因此编码总数至多为 \(2^{\aleph_0}=\mathfrak c\)，Borel 集总数也至多为 \(\mathfrak c\)。另一方面，每个单点都是闭集，所以 Borel 集至少有 \(\mathfrak c\) 个。我们得到精确基数，而不是只数有限层生成的集合。

<a id="t-measure-strict"></a>

## T-MEASURE.4 严格包含的最后一步

Cantor 的对角论证说明，对于任何集合 \(E\)，不存在从 \(E\) 到 \(\mathcal P(E)\) 的满射：若 \(F\) 是这样的映射，取 \(D=\{x\in E:x\notin F(x)\}\)，则 \(D=F(d)\) 会给出 \(d\in D\) 当且仅当 \(d\notin D\)。因此 \(|\mathcal P(C)|>\mathfrak c\)。

零外测度集合 \(N\) 的每个子集 \(A\) 都有零外测度。对任意 \(E\)，外测度的单调性和次可加性给出 \(m^*(E)=m^*(E\setminus A)\) 及 \(m^*(E\cap A)=0\)，所以 Carathéodory 分割等式成立，\(A\) 是 Lebesgue 可测的。于是 \(C\) 的所有子集可测，但其中至多 \(\mathfrak c\) 个可能是 Borel 集。故

\[
\mathcal B(\mathbb R)\subsetneq\mathcal L(\mathbb R).
\]

这是一份存在性证明，并没有假装写出某个非 Borel 子集的显式公式。它依靠的是零集容纳的全部子集与 Borel 运算编码之间的严格基数差，而不是“不可数”与“可数”之间的混淆。

<a id="t-measure-lebesgue-completion"></a>

## T-MEASURE.5 Lebesgue 测度正是 Borel 长度测度的完备化

还需证明“补进零集”没有漏掉其他 Lebesgue 可测集。设 \(E\) 是有限测度的 Lebesgue 可测集。由区间覆盖定义，先选总长度小于 \(m(E)+\varepsilon/2\) 的可数覆盖，再把第 \(k\) 个区间稍微放大为开区间，新增长度之和小于 \(\varepsilon/2\)。于是有开集 \(O\supseteq E\)，\(m(O)\le m(E)+\varepsilon\)。这一步直接由外测度定义得到，没有预用测度的正则性定理。

对 \(\varepsilon=2^{-n}\) 取开集 \(O_n\)，令 \(B=\bigcap_nO_n\)。则 \(B\) 是 Borel 集，\(E\subseteq B\)，且 \(m(B)=m(E)<\infty\)，所以 \(m(B\setminus E)=0\)。再给零集 \(B\setminus E\) 作同样的开覆盖，得到包含它的 Borel 零集 \(Z\)。于是 \(E=B\setminus N\)，其中 \(N\subseteq Z\)，正属于 Borel 测度的完备化。

一般 Lebesgue 可测 \(E\) 可分成与 \([-n,n]\) 相交的有限测度部分；每部分属于完备化，故其可数并也属于。反向包含来自 Borel 集的 Lebesgue 可测性及 Lebesgue 测度的完备性。两种测度在旧 Borel 集上一致，所以上一节的一般构造也确定了取值。

因此，不完备概率空间不是自相矛盾，而是尚未选择把全部零集子集加入。第八章先在柱集生成的结构上构造概率，第十章在标准 Borel 状态空间处理条件核，都有明确理由；若随后完备化，必须重新说明定义域和可测版本，而不能把“相差一个零集”当作任意函数自动可测的许可。积分中的准确边界见[零集修改定理](t-integral.md#t-integral-null)。
