# 有限对称、无放回抽样与Bernoulli表示

## 1. 先把置换怎样作用写清

<a id="exchange-proof-average"></a>

在非空标准Borel空间E上，取记录空间Ω=E的可数乘积及坐标变量X。有限置换π只改变有限多个正整数，令Sπ将记录的第i项替换成原第π(i)项。交换律P满足每个Sπ保P。所有有限置换构成可数群；只置换1到N的子群记为Sₙ。这里N只是一个正整数，不是一个停止时刻。

\[ \mathcal G_N=\{A:S_\pi^{-1}A=A\text{ for every }\pi\in S_N\},\quad \mathcal J=\bigcap_{N\ge1}\mathcal G_N,\quad A_NF=\frac1{N!}\sum_{\pi\in S_N}F\circ S_\pi. \]

这些都是原始记录σ代数的子σ代数。有限群平均AₙF对该群不变，因而Gₙ可测。对任意A∈Gₙ，每个保测变换都给积分恒等式，故有限平均确实是条件期望，不只是一个形式上的对称化。对非负F用单调收敛，从有界情形扩张。

\[ \int_A A_NF\,dP=\frac1{N!}\sum_{\pi\in S_N}\int_A F\circ S_\pi\,dP=\int_A F\,dP,\qquad E[F\mid\mathcal G_N]=A_NF. \]

群越大，不变事件越少，所以Gₙ递减。第15章反向鞅定理给有界F的条件期望几乎必然且L¹收敛到E[F|J]。这里只在原始子σ代数上先取交，再按P完成化比较事件；没有把不同零集或未证的群不变理论藏进记号。

## 2. 有限总体给出的准确分布

<a id="exchange-proof-urn"></a>

对长度N的Bernoulli交换向量，令K为1的总数。每个含K个1的字具有相同概率；当P(K=j)>0时，给定K=j，这些字均匀分布。反过来，任取K的概率，再在相应的字中均匀抽样，就产生有限交换律。零概率的K值上条件版本任取。

\[ P(X_1=x_1,\ldots,X_k=x_k\mid K=j)=\frac{(j)_r(N-j)_{k-r}}{(N)_k},\quad r=\sum_{\ell=1}^k x_\ell,\quad (a)_r=a(a-1)\cdots(a-r+1). \]

这是按顺序无放回抽取位置的概率，k≤N，约定零阶下降阶乘为1；不可行的字给概率0。它不是把p=j/N代入独立Bernoulli公式。两次取样之间，剩余组成真的会改变。

## 3. 有放回与无放回之间的误差

<a id="exchange-proof-replacement"></a>

\[ L_N=\frac1N\sum_{i=1}^N\delta_{X_i},\qquad c_{k,N}=\min\left(1,\frac{k(k-1)}{2N}\right). \]

固定1≤k≤N及一份记录，独立均匀抽k个位置I。出现重复的概率不超过所有位置对相等概率之和，即c。若没有重复，这组位置均匀分布于有序不同位置。构造另一组位置J：I无重复时令J=I；有重复时另抽一组均匀不同位置。于是J始终服从无放回律，而I与J不一致的概率至多c。这一步完全不假设记录本身独立。

\[ \left|\frac1{(N)_k}\sum_{\substack{i_1,\ldots,i_k\le N\\\text{all distinct}}}\prod_{\ell=1}^k f_\ell(X_{i_\ell})-\prod_{\ell=1}^k L_N f_\ell\right|\le c_{k,N}\qquad(0\le f_\ell\le1). \]

对任意可测事件而非仅乘积函数使用同一位置耦合，得到E上向量的总变差界。位置取样与原记录独立，交换性使无放回向量的无条件律等于前k项；有放回的条件律是经验概率的k重积。

\[ d_{\rm TV}\left(\mathcal L(X_1,\ldots,X_k),\,E[L_N^{\otimes k}]\right)\le c_{k,N}. \]

这个上界也适用于只有N项的有限交换向量。它是一份定量近似，不把有限律变成精确无限表示。若允许被积函数有正负号而只满足绝对值≤1，则上面的乘积误差界应乘2；本章主证使用0到1的指标函数，故无需偷换这个常数。

## 4. Bernoulli逆向表示的全部步骤

<a id="exchange-proof-bernoulli"></a>

现在给定一条无限Bernoulli交换记录。有限平均恒等式给经验频率等于E[X₁|Gₙ]。反向鞅使其收敛到一个[0,1]值变量Θ。将不收敛记录上的Θ置0；有限置换或删去有限前缀都不改变频率极限的存在和值，因此Θ可以取为原始J可测且尾可测的函数。

\[ \frac{K_N}{N}=E[X_1\mid\mathcal G_N]\longrightarrow\Theta\quad\text{a.s. and in }L^1. \]

固定一个长度k的字x，其中r个1。有限群平均给其条件概率gₙ。上节位置耦合给gₙ与(Kₙ/N)ʳ(1−Kₙ/N)ᵏ⁻ʳ的差至多c，所以gₙ逐点趋Θʳ(1−Θ)ᵏ⁻ʳ。在任意有界Borel函数h(Θ)前乘上这个恒等式；它对每个Gₙ可测。由DCT取极限，得到真正的条件iid关系。

\[ E[h(\Theta)\mathbf1_{\{X_{1:k}=x\}}]=E[h(\Theta)\Theta^r(1-\Theta)^{k-r}],\quad P(X_{1:k}=x\mid\Theta)=\Theta^r(1-\Theta)^{k-r}. \]

对字长和二进制字取可数共同零集；积核的π–λ唯一性给整条记录的条件律。令M为Θ的律，就有全部有限维的de Finetti混合表示。反方向由积律在有限置换下不变，再对M积分，立即给交换性。

\[ P(X_{1:k}=x)=\int_0^1 p^r(1-p)^{k-r}M(dp). \]

若另一混合M′也给同一记录律，在联合空间先选p再按Bernoulli(p)生成记录。第12章强律对每个固定p给频率极限p，事件是联合可测的，所以对M′积分后仍几乎必然成立。频率极限的分布于是既是M′，又由原记录律确定为M，故M′=M。不用未证的矩问题来填补唯一性。

## 5. 有限反例与主要依赖

<a id="exchange-proof-boundaries"></a>

长度2取01与10各半，交换但协方差为−1/4。任何长度n的交换Bernoulli延拓都使其和的方差为n(2−n)/4；n=3已经矛盾。即使两两独立仍可能不可无限延拓：长度3取000、011、101、110各1/4，是交换且两两独立。若无限延拓存在，表示中VarΘ=Cov(X₁,X₂)=0，Θ=1/2，故P(111)=1/8，与原来的0矛盾。

依赖为第9章条件平均、第15章反向鞅、第12章强律，以及有限群逐项积分与第42章已证的耦合不等式。有限群平均在本页自证，不借第45章。回到[第43章频率的逆向意义](../chapters/43-exchangeability.md#exchange-bernoulli)。
