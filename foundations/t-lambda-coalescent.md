# T-LAMBDA-COALESCENT：一致率、Poisson构造、dust与反演边界

本页补全[第56章](../chapters/56-fragmentation-hierarchies.md#coalescent-rates)的单组多重合并，不重证47章Kingman专用主线。Λ为[0,1]上的有限非负测度；每次跳只合并一组块，允许组内任意多个块，同时多组Ξ型跳跃不在本页范围。

## 1. 删除一个块所迫使的递推

<a id="lambda-recursion"></a>

\[ \lambda_{b,k}=\lambda_{b+1,k}+\lambda_{b+1,k+1},
\qquad 2\le k\le b. \]

各λ均为非负有限数。λ是某个指定k块组的速率，不是全部这类跳的总速率。加入一个不可见块后，原k组可以恰好合并，也可以连同新块一起合并，两事件互斥且给同一限制跳，故一致性强迫递推。反向，只要非负率满足它，逐个删除额外块就给有限生成矩阵的投影身份；有限矩阵指数及迭代条件期望给路径一致性。

## 2. 不用未证矩问题名称代替Λ表示

<a id="lambda-moment"></a>

设aₙ=λₙ₊₂,₂，E为序列前移算子。递推给λ(b,k)=E^(b−k)(1−E)^(k−2)a₀，故所有这些差分非负。对m≥1定义有限测度Mₘ。

\[ w_{m,j}=\binom mj\lambda_{m+2,m-j+2},\qquad
M_m=\sum_{j=0}^m w_{m,j}\delta_{j/m},\qquad
\sum_jw_{m,j}=a_0. \]

最后一式是[E+(1−E)]ᵐa₀=a₀。类似地，写(j)ᵣ=j(j−1)…(j−r+1)，组合恒等式给Σ(j)ᵣ/(m)ᵣ wₘ,ⱼ=aᵣ。因为(j/m)ʳ与这个阶乘比在0≤j≤m上一致相差Oᵣ(1/m)，Mₘ的r阶矩趋aᵣ。总质量a₀固定，紧区间上的测度紧性给弱极限M，拥有这些矩；a₀=0时全率0，取零测度。

\[ \sum_{j=r}^m
\frac{(j)_r}{(m)_r}\binom mj
E^j(1-E)^{m-j}a_0
=E^r[E+(1-E)]^{m-r}a_0=a_r. \]

13章Bernstein多项式逼近使紧区间上相同全部矩的有限测度相同，故M唯一。把y映成x=1−y，得唯一Λ。差分恒等式遂给完整率表示；没有未经证明调用Hausdorff矩定理。

\[ \lambda_{b,k}=\int_{[0,1]}
x^{k-2}(1-x)^{b-k}\Lambda(dx),\qquad
q_b=\sum_{k=2}^b\binom bk\lambda_{b,k}.
\quad 0^0=1. \]

## 3. 同一随机空间上的全部有限链

<a id="lambda-construction"></a>

记a=Λ{0}。对正x取Poisson测度，强度dt x⁻²Λ(dx) du，其中u∈[0,1]ᴺ有积均匀律。原子到达时，将当前块B标为活跃，当且仅当\(u_{\min B}\)≤x；合并所有活跃块，少于两个则不变。对[n]，能改变状态的事件包含于前n个u至少两个≤x，其概率至多binom(n,2)x²，故有效Poisson率至多binom(n,2)Λ((0,1])。每指定k个当前块活跃、其余不活跃的率恰为上式的正x部分。

另对每个整数对i<j放独立率a Poisson时钟，仅当i、j都是当前块最小代表时才合并两块。对[n]只需i、j≤n的有限时钟，产生Kingman原子0部分。给全部n使用同一噪声：任何遇到[n]的块，其最小值也在[n]，故两个构造都与限制逐样本相容。有限链至多n−1跳，所有n在一个共同好集定义，得到紧划分空间中的càdlàg路径。

生成矩阵的置换协变给路径交换性；柱半群仍是有限矩阵半群，给Feller、强连续和格点逼近的专用强Markov证明，步骤与T-HOMOGENEOUS-FRAGMENTATION的有限柱论证完全相同：先柱函数、再一致逼近连续函数、再对停止时刻向上格点取有界极限。这里的必要差别是合并会减少块数，但有限投影仍非爆炸。

## 4. Kingman原子保证从无穷下降

<a id="lambda-cdi"></a>

若a>0，记Nₙ(t)为[n]块数、τₘ为首次≤m。取f(b)=Σⱼ₌ₘ₊₁ᵇ1/[a binom(j,2)]，b≤m时为0。对b>m，二元Kingman项给Lf≤−1，额外多重跳只让f更小。有限链Dynkin及停止给Eτₘ≤f(n)≤2/(am)。由Markov界和Nₙ随n非减，

\[ P(N(t)>m)
=\lim_nP(N_n(t)>m)\le\frac{2}{amt},\qquad t>0. \]

令m趋无穷，正时间块数有限几乎必然；对有理时间统一后，由块数非增推广到所有正时间。若Λ=δ₁，第一次率1时钟以前全是单点，之后合成一块。因此P(N(t)=∞)=e⁻ᵗ，说明一般Λ过程并不自动从无穷下降。最广积分判据没有在此证明。

## 5. 有限标记强度下的dust公式

<a id="lambda-dust"></a>

\[ a=0,\qquad
\beta=\int_{(0,1]}x^{-1}\Lambda(dx)<\infty
\quad\Longrightarrow\quad
D(t)=\prod_{(u,x):\,u\le t}(1-x),\qquad ED(t)=e^{-\beta t}. \]

条件于Poisson时刻和x，每个原始单点i在被第一次标记以前使用自己的uᵢ；“截至t从未被标记”的事件跨i独立，概率为上述乘积。Poisson∑x在有界时间内有限几乎必然；无x=1事件前乘积严格正。一旦i首次标记，其他从未标记的标签中被同时标记者具有正频率xD(u−)，故i加入非单点正频率块。x=1事件使全部剩余单点合入。因此dust恰是未被标记标签的频率，条件强律给乘积公式；Poisson泛函给其期望。

例如\(\Lambda=\delta_{1/2}\)时，D(t)=2⁻ᴷ⁽ᵗ⁾，K为率4 Poisson计数。零频率单点可以组成正dust总量；合并使它们进入正质量块。没有把每个零频率单点的“质量0”当作可数可加测度在N上相加。β无穷的一般dust必要充分条件没有由此特殊可积公式自动推出。

## 6. 反演两标签就已暴露新的条件

<a id="lambda-reversal"></a>

从两个单点出发，每对率1，合并时刻E∼Exp(1)。固定T>0，把路径在[0,T]反看。给反向时刻u当前已合并，下一小段反向分裂率由前向时刻s=T−u的质量比给出。

\[ r_{\rm rev}(u)=
\lim_{h\downarrow0}
\frac{P(s-h<E\le s)}{hP(E\le s)}
=\frac{e^{-(T-u)}}{1-e^{-(T-u)}},\qquad 0\le u<T. \]

该率依时间并在终端发散，绝不是自动得到一份固定率齐次碎裂。这里指定了观察区间与起始律；若另选平稳律或模型、做时间变换，可能有真正对偶，但必须另外证明。一般Ξ分类、CRT切割与加性合并对偶及人口缩放没有计入本页。返回[正文](../chapters/56-fragmentation-hierarchies.md#fragment-reversal)。
