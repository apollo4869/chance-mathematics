# T-ENTROPY：有限熵信息率、SMB与生成划分

本页完成[第41章信息率](../chapters/41-ergodic-theory.md#ergodic-information-rate)。SMB部分取可数字母双边平稳过程、H(X₀)<∞、可逆坐标移位T。结论允许非遍历，给a.s.与L¹的随机条件信息率；不是仅在平均熵层面的等式。对一般保概率变换也定义有限划分熵，生成划分定理另声明可逆性。

## 1. 链式熵、条件化与块熵极限

<a id="entropy-proof-basics"></a>

对可数分布定义H=Σ−p_a log p_a，0 log0=0。实际符号落到零概率字母的概率为0。联合概率分解使−log p(X,Y)=−log p_X(X)−log p(Y|X)，所有项非负，Tonelli给H(X,Y)=H(X)+H(Y|X)，允许∞。条件熵定义为条件分布的熵的期望；对−u log u用条件Jensen，细σ域的条件熵不大于粗σ域。可数字母由合并尾部的有限划分再取极限，或逐个非负求和得到同一结论。

在平稳过程，H_n=H(X₀,…,X_{n−1})满足H_{m+n}≤H_m+H_n且H_n≤nH(X₀)<∞。Fekete给h=lim H_n/n=inf H_n/n。这个确定极限只是块熵的平均，还不是实际词的信息率。下两节提供缺少的随机控制。

## 2. 条件概率的零值与可积对数包络

<a id="entropy-proof-envelope"></a>

\[ \mathcal G_k=\sigma(X_{-k},\ldots,X_{-1}),\quad p_k(a)=P(X_0=a\mid\mathcal G_k),\quad p_\infty(a)=P(X_0=a\mid\mathcal G_\infty),\quad I_k=-\log p_k(X_0). \]

G₀平凡。对每个a，p_k(a)是[0,1]值鞅，15章给a.s.与L¹趋p∞(a)。可数字母允许统一零集。P(X₀=a,p∞(a)=0)=E[p∞(a)1_{p∞(a)=0}]=0，所以实际符号的极限概率严格正；每个有限k亦同。I_k因而为有限非负变量且趋I∞。

对p₀(a)>0与t≥0，令τ_a首次满足p_k(a)<e⁻ᵗp₀(a)。事件{τ_a=k}属于G_k，逐项条件积分给P(X₀=a,τ_a≤N)=Σₖ≤N E[p_k(a)1_{τ_a=k}]≤e⁻ᵗp₀(a)。N增加，再对a求和，得到下面的指数尾。这里用的是明确的离散停止检验，不使用尚未建立的对数鞅不等式。

\[ R=\sup_{k\ge0}\left(\log\frac{p_0(X_0)}{p_k(X_0)}\right)^+,\qquad P(R>t)\le e^{-t},\qquad 0\le I_k,I_\infty\le I_0+R,\qquad E(I_0+R)\le H(X_0)+1. \]

因此DCT给I_k→I∞于L¹。链式与平稳性给H_n=Σⱼ<n EI_j，故h=EI∞。这个包络还会控制逐路径三角平均；只知道各EI_k≤H(X₀)不够，因为L¹有界不保证统一可积。

## 3. Maker引理及SMB的全部极限步骤

<a id="entropy-proof-smb"></a>

先给三角平均的一般引理：若f_j→f几乎必然且sup_j|f_j|≤F∈L¹，则n⁻¹Σⱼ<n f_j∘Tʲ→E[f|I]几乎必然且L¹。固定K，前K项除n逐路径趋0；其余差绝对值≤A_n g_K，g_K=sup_{j≥K}|f_j−f|≤2F。Birkhoff使其limsup≤E[g_K|I]。g_K↓0，条件单调/控制收敛使此界↓0几乎必然，证明逐点结论。L¹误差≤n⁻¹Σ‖f_j−f‖₁→0，再加A_nf的L¹收敛。

对每个长度n与每个可数词，条件概率链式成立；平稳性识别第j因子为p_j(X_j)在移位后的版本，即p_j(X₀)∘Tʲ。可数取交处理所有词、长度与移位，实际出现的零概率词删成一个零集。于是下式是几乎必然的精确身份，应用上一引理与可积包络，完成SMB。

\[ -\log P(X_0,\ldots,X_{n-1})=\sum_{j=0}^{n-1}I_j\circ T^j,\qquad -\frac1n\log P(X_0,\ldots,X_{n-1})\to E[I_\infty\mid\mathcal I]\quad\text{a.s. and in }L^1. \]

若遍历，极限h=EI∞。对δ,ε>0，充分大的n下，概率至少1−ε的实际词满足e^{-n(h+δ)}≤P(词)≤e^{-n(h−δ)}。所以这些词的数目在(1−ε)e^{n(h−δ)}与e^{n(h+δ)}之间。下界用每词概率上界，计数上界用每词概率下界和总概率≤1。它说明指数尺度的有效记录数，不宣称所有词等概率，也不是无损编码定理的完整证明。

## 4. 测度熵与生成划分定理

<a id="entropy-proof-generator"></a>

任意保概率T及有限或可数有限熵划分P，令P^n=∨ⱼ<n T⁻ʲP，h(T,P)=lim H(P^n)/n。前节的次可加论证保证存在，且不要求T可逆。定义h(T)为所有有限P的h(T,P)上确界。模零保测同构把每份划分及其全部逆像一一对应，所以保持h(T)，不需先证明某个拓扑动力学版本。

现在假定T可逆，P可数、H(P)<∞，且∨ⱼ∈Z T⁻ʲP生成F模零。取任意有限Q，R_m=∨_{j=-m}^m T⁻ʲP。给定R_m的Q条件概率由15章鞅收敛趋Q的指标；有限Q的条件熵至多log|Q|，DCT给H(Q|R_m)→0。对长度n联合划分，条件链式与增信息减熵给H(Q^n)≤H(R_m^n)+nH(Q|R_m)。

R_m^n等于P从−m到n−1+m的联合，保测可逆使它的熵为H(P^{n+2m})。除n送n到∞，得h(T,Q)≤h(T,P)+H(Q|R_m)；再送m到∞，h(T)≤h(T,P)。若P有限，反向显然。若P可数，把除前l个原子外的尾部合并成一格P_l，则H(P|P_l)=H(P)−H(P_l)→0。同一条件链式给h(T,P)≤h(T,P_l)+H(P|P_l)≤h(T)+误差。送l到∞，反向也成立，生成划分定理完整证明。

## 5. 例子、依赖与未证推广

<a id="entropy-proof-boundary"></a>

双边独立Bernoulli过程的坐标划分生成全信息，H_n=nH(p)，故系统熵为H(p)。两点交换的所有联合划分都至多两格，块熵≤log2，系统熵为0。混合两种偏向时，过去频率按条件强律恢复Θ；故p∞(1)=Θ，条件信息率为H(Θ)。选Θ=1/4或3/4，二者H相同，于是信息率常数仍不推出遍历。

依赖：第6章非负积分与DCT、第9–10章条件概率、第12章条件独立强律、第15章增加信息鞅收敛、本章已证Birkhoff。所有对数极限所需的包络已在本页证明，不借未来交换性定理或未证熵变分原理。有限熵可数SMB和可逆生成划分以外的一般相对熵、无限熵、群作用版本与拓扑变分原理不在此计为已证。概念与条件可对照[Hochman作者讲义](https://math.huji.ac.il/~mhochman/courses/dynamics2014/notes.5.pdf)，本文实际论证独立组织。[返回第41章结语](../chapters/41-ergodic-theory.md#ergodic-insight)。
