# T-DIFFERENTIATION：由覆盖估计恢复局部密度

配套[第38章](../chapters/38-feynman-kac.md#potential-differentiation)。空间为Rᵈ，球用欧氏开球，|·|为Lebesgue测度。只证明本章实际需要的Lebesgue微分与有限测度密度恢复，不混淆RN抽象密度与已证明的点态极限。

## 1. 五倍球覆盖与弱型估计

<a id="differentiation-proof-cover"></a>

给定有界集合中一族半径有共同上界的球，按半径从大到小选不相交球：先选半径大于现有上确界一半的球，删去与它相交者，反复进行。未被选的球若半径r，就必与某个所选半径rⱼ≥r/2的球相交，否则会在半径降至r/2以前被选；原球包含在该球五倍放大内。可数性由所选不相交开球各含不同有理点给出。对紧集只需有限子覆盖后做有限贪心选择，因而不依赖无限选择细节。

\[ M\nu(x)=\sup_{r>0}\frac{|\nu|(B(x,r))}{|B(x,r)|},\qquad |\{M\nu>\lambda\}|\le\frac{5^d}{\lambda}|\nu|(\mathbb R^d),\quad\lambda>0. \]

对{Mν>λ}的任意紧子集，为每个点选一颗满足质量>λ体积的球。所选不相交球的总体积至多|ν|/λ，五倍覆盖使紧集体积至多5ᵈ|ν|/λ。超水平集可测：球积分对中心和半径Borel，半径可取有理并从下方增加到所给半径，由测度下连续性恢复开球积分，不把可能带质量的球面错误地纳入。Lebesgue内正则性及有界区域耗尽给全结论。对f∈L¹取ν=f dx即得最大平均弱(1,1)界。

## 2. 先对连续函数，再用弱型控制误差

<a id="differentiation-proof-functions"></a>

连续紧支撑g的局部振幅平均当然趋0。任意f∈L¹可在L¹逼近这样的g：先截断f及空间，简单函数逼近，再用Radon内外正则性以紧K⊂A⊂开U、|\(U\setminus K\)|小的连续夹逼函数替代指示；函数可显式取dist(x,K)/(dist(x,K)+dist(x,Uᶜ))的补值。故不使用尚未证明的Lusin定理。

\[ Df(x):=\limsup_{r\downarrow0}\frac1{|B(x,r)|}\int_{B(x,r)}|f(y)-f(x)|dy\le M(f-g)(x)+|f(x)-g(x)|. \]

对ε>0，{Df>2ε}的测度≤(5ᵈ+1)‖f−g‖₁/ε，来自上一节及Markov不等式。令逼近误差趋0，再对有理ε取交，得Df=0几乎处处。局部L¹函数乘每个大球的截断后，在较小球内足够小的平均相同，可数耗尽给L¹_loc版本。改变f于零集不影响结论，但极限只在共同满测度集合上成立，不是每一点成立。

## 3. 奇异测度不可能由普通密度恢复

<a id="differentiation-proof-measures"></a>

令有限正ν=f dx+ν_s为10章的Lebesgue分解。ν_s集中于零测集N。选紧K⊂N使ν_s(\(\mathbb R^d\setminus K\))<δ。x∉K时，小到一定程度的球不见K，因此ν_s的上密度等于剩余ν_s|Kᶜ的上密度。上一节弱型估计给上密度>ε的Lebesgue测度≤5ᵈδ/ε；K本身零测。δ↓0、ε取可数有理值得奇异部分密度为0几乎处处。带符号ν用总变差支配其奇异部分；局部有限情形截断空间。

\[ \lim_{r\downarrow0}\frac{\nu(B(x,r))}{|B(x,r)|}=f(x)\quad\hbox{for Lebesgue-a.e. }x,\qquad \nu_s\ne0\ \hbox{is still possible}. \]

这解释了为何把局部时收费压成一个几乎处处的函数q会丢失信息。对ν=δ_c，上式右侧f=0几乎处处，却并不意味着ν=0。占用测度、二阶分布导数与Revuz测度需要保留它们的奇异部分。[回正文](../chapters/38-feynman-kac.md#potential-differentiation)。
