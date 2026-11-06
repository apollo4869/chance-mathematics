# T-SUBADDITIVE：Kingman定理与随机乘积

本页完成[第41章次可加主证](../chapters/41-ergodic-theory.md#ergodic-subadditive)。假设T保概率，X₀=0，每个Xₙ为有限L¹变量，X_{m+n}≤X_m+X_n∘Tᵐ对所有整数m,n≥0几乎必然，且inf EXₙ/n>−∞。可数取交并删去其全部T逆像，保证沿余下轨道同时使用全部不等式。

## 1. 期望的Fekete极限与非正还原

<a id="subadditive-proof-reduction"></a>

若有限数列a_n满足a_{n+m}≤a_n+a_m，写N=qk+r，0≤r<k，得a_N≤q a_k+a_r。除N并令N增加，limsup a_N/N≤a_k/k，而liminf≥inf a_n/n，故极限等于该inf，允许−∞。期望EX_n满足此关系，因为T保测。

\[ Y_n=X_n-\sum_{j=0}^{n-1}X_1\circ T^j\le0,\qquad Y_{m+n}\le Y_m+Y_n\circ T^m,\qquad Y_0=Y_1=0. \]

所有Y_n仍可积。证明Y_n/n的极限以后，用已证Birkhoff恢复被减去的平均。这个还原使任意被跳过的区间都贡献非正上界，因此后面的覆盖可以合法丢弃空白；并不是假定原始代价非负。

## 2. 遍历情形的完整双向证明

<a id="subadditive-proof-ergodic"></a>

先设T遍历，令β=inf EY_n/n∈[−∞,0]。固定k与N≥k，从每个偏移r=0,…,k−1作完整k块分解。前缀和末段的Y均≤0，去掉这些项并把k条不等式相加，所有完整块起点0,…,N−k恰出现一次，得kY_N≤Σ_{j=0}^{N-k}Y_k∘Tʲ。Birkhoff给limsup Y_N/N≤EY_k/k，对可数k取交得≤β。如果β=−∞，已经证明扩展实值极限为−∞。

设β有限，G=liminf Y_n/n≤0。由Y_{n+1}≤Y₁+Y_n∘T得G≤G∘T；对扩展区间[−∞,0]用有界严格递增函数，保测使两边积分相等，故G=G∘T几乎必然。遍历性使G为确定常数，允许−∞。假设G<β，取有限a满足G<a<β且a<0。

\[ B_K=\bigcup_{1\le k\le K}\{Y_k<ka\},\qquad P(B_K)\uparrow1. \]

固定K，扫描整数位置j=0,…,N−K。若Tʲω∈B_K，取最小合适k≤K，选区间[j,j+k)并把j跳到j+k；否则只前进1。选中区间两两不交，全部落在[0,N]，末尾未处理区间不超过K项。令总长度L。每个可用起点不是被一个已选区间覆盖，就是会成为下一选中块的起点，所以L≥Σ_{j=0}^{N-K}1_{B_K}∘Tʲ。有限次次可加，空白项非正，故Y_N≤aL≤aΣ1_{B_K}∘Tʲ。

取期望并除N，Fekete给β≤aP(B_K)。K充分大时aP(B_K)<β，矛盾。故G≥β，与上界合并，Y_n/n→β几乎必然。若β有限，−Y_n/n非负、期望由Fekete趋−β；Scheffé的恒等式E|Z_n−Z|=EZ_n+EZ−2E min(Z_n,Z)，配合DCT处理min≤Z，给L¹收敛。这里不从有界期望直接偷换成一致可积。

## 3. 非遍历环境与全部期望的合法拼合

<a id="subadditive-proof-conditional"></a>

先在标准Borel系统使用[T-ERGODIC-DECOMPOSITION](t-ergodic-decomposition.md#decomposition-proof-ergodicity)。可数个X_n及其不等式的满测集，在几乎每份遍历核下仍满测且可积。令b_n=E[Y_n|I]≤0；不变测试积分给E[Z∘Tᵐ|I]=E[Z|I]，所以b_{n+m}≤b_n+b_m共同几乎必然。

对每个ω用Fekete，β(ω)=inf b_n(ω)/n是该序列的极限。阶乘子列b_{n!}/n!递减，因为(n+1)!是n!的整数倍；它趋同一个inf。非正单调收敛遂给Eβ=lim E Y_{n!}/n!=inf EY_n/n>−∞。因此β有限几乎必然且可积。核关于I的参数集中性，使核内每个b_n都等于所固定环境的值，上一节遍历证明于是给Y_n/n→β于原概率几乎必然。

无条件Fekete又使E Y_n/n→Eβ，前节的非负Scheffé论证给全局L¹收敛，不需从“每份核内L¹”直接交换不可控的外层积分。加回S_nX₁/n的Birkhoff极限，γ=β+E[X₁|I]=inf E[X_n|I]/n，并且Eγ=inf EX_n/n。

原概率空间不标准Borel时，用可数读数(X_n∘Tᵏ)的记录因子。该因子中的主证拉回给收敛。对每个固定X_n，原空间Birkhoff极限与因子Birkhoff极限沿同一记录相同，故E[X_n|I_original]也等于所拉回的条件平均，条件公式仍成立。没有调用原空间未必存在的正则条件核。

## 4. 矩阵应用与已证范围的边界

<a id="subadditive-proof-products"></a>

对平稳可逆矩阵A_k，算子范数满足‖BC‖≤‖B‖‖C‖，且‖BC‖≥1/‖(BC)⁻¹‖。对乘积取对数，分别用Σlog⁺‖A_j‖和−Σlog⁺‖A_j⁻¹‖夹逼，保证每个X_n可积、EX_n/n≥−E log⁺‖A₀⁻¹‖。全定理遂给最大范数增长率；遍历时为常数。若无需可逆性但能另证线性期望下界，也同样适用。

X_n=−n²说明有限下界负责排除−∞，不是保证任何无下界次可加族都有限收敛。连续时间次可加、非平稳阵列和完整方向Lyapunov谱并未在本页证明；一般乘法遍历若需要承担，须另立实际证明责任，不能从本范数结论推定。回到[正文矩阵例子](../chapters/41-ergodic-theory.md#ergodic-matrix)。
