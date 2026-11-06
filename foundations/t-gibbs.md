# T-GIBBS：Papangelou密度、有限体积核与一种无限体积存在定理

返回[第50章](../chapters/50-palm-gibbs.md#palm-papangelou)。一般密度部分用LCSC点空间、σ有限参考测度m和σ有限平均强度ν。有限体积部分明确m(B)<∞；无限体积存在定理专限欧氏空间中有界连续、非负、有限作用范围的对称两体势及常活动度，不宣称任意Gibbs相互作用均存在或唯一。

## 1. Papangelou是一个绝对连续性命题

<a id="gibbs-papangelou"></a>

给Ξ的律P，T-PALM给约化Campbell\(C^!(dx,d\eta)\)。存在可测非负c使

\[ \mathbb E\int F(x,\Xi-\delta_x)\Xi(dx)=\int m(dx)\int F(x,\eta)c(x,\eta)P(d\eta) \]

对全部非负F成立，当且仅当\(C^!\ll m\otimes P\)。这是10章Radon–Nikodym定理的直接应用，两个测度均σ有限；c取m×P-a.e.有限版本。这个c叫Papangelou条件强度，显示身份叫GNZ身份。它不是时间滤过下的预测强度，也不是任意点过程都拥有的密度。

若\(\nu(dx)=\rho(x)m(dx)\)，则\(\rho(x)=E_Pc(x,\Xi)\)，且在0<ρ(x)<∞的共同m满测度部分有

\[ Q_x^!(d\eta)=\frac{c(x,\eta)}{\rho(x)}P(d\eta). \]

证明先对F=1A(x)得到强度密度，再对环境可数生成类合并零集，利用T-PALM的概率核唯一性。ρ=0处核不由身份决定，选固定版本。若Ξ=\(\delta_U\)、U在[0,1]均匀，其平均有长度密度，但约化Palm恒为空配置，原P却只见单点配置。取F为余配置为空的示性，GNZ左侧1、右侧0，说明Papangelou绝对连续性失败。

## 2. 有限Poisson参考与遗传密度

<a id="gibbs-finite-density"></a>

令πₘ为B上有限强度m的Poisson律。取可测p≥0、\(\int p\,d\pi_m=1\)，并要求遗传性：若p(η)=0，则p(η+δₓ)=0。定义P=pπₘ。Mecke给\(C^!(dx,d\eta)=m(dx)p(\eta+\delta_x)\pi_m(d\eta)\)。遗传性消除p=0处的奇异余项，故可取c=p(η+δₓ)/p(η)于p>0，p=0处取0，GNZ成立。

只说P相对于Poisson有密度还不够：将π条件在总数1上，密度不具上述遗传性，正是前节反例。遗传性在此是明确的充分条件，不能假定一切约束都满足它。

具体取0≤z(x)≤z̄<∞，对称可测两体势φ≥0，允许φ=∞表示硬排斥。给外部局部有限配置ξ，定义

\[ w_B(\eta\mid\xi)=\prod_{x\in\eta}z(x)\exp\left\{-\sum_{\{x,y\}\subset\eta}\phi(x,y)-\int_B\int_{B^c}\phi(x,y)\xi(dy)\eta(dx)\right\}. \]

内和按不同出现组成的无序对，强度m弥散时配置简单a.s.。空积为1，\(e^{-\infty}=0\)，全部能量由非负可测积分/和定义。总质量\(Z_B(\xi)=\int w_B(\eta\mid\xi)\pi_{m|B}(d\eta)\)满足\(e^{-m(B)}\le Z_B(\xi)\le\exp\{(\bar z-1)m(B)\}\)，所以正且有限；上界由Poisson的总数母函数。归一密度遗传，Papangelou可取

\[ c_B(x,\eta\mid\xi)=\mathbf1_B(x)z(x)\exp\left\{-\int\phi(x,y)(\eta+\xi|_{B^c})(dy)\right\}\le\bar z. \]

此表达式在零密度配置上可有不同值，不影响P下身份；在正密度配置上由增加一点的能量精确相消得到。没有作∞−∞，而是直接用权重的乘法分解；被禁止的加入给权重0。

## 3. GNZ如何反推有限体积概率律

<a id="gibbs-janossy"></a>

固定B及ξ，设另一份有限配置概率P满足上述\(c_B\)的GNZ。定义\(J_n\)为在总数n事件上对全部有序n个不同出现的期望阶乘测度，J₀=P(N=0)。Jₙ总质量n!P(N=n)，有限。取GNZ测试为“余配置总数n−1，再枚举余下n−1次出现”，Tonelli给递推

\[ J_n(dx_1\cdots dx_n)=J_{n-1}(dx_1\cdots dx_{n-1})c_B\!\left(x_n,\sum_{i<n}\delta_{x_i}\mid\xi\right)m(dx_n). \]

依次代入得\(J_n=q_0w_B(\sum_i\delta_{x_i}\mid\xi)m^n\)。若q₀=0，所有Jₙ为0，与P有限配置总概率1矛盾，故q₀>0。任意非负配置函数F可由\(E_PF=\sum_n(n!)^{-1}\int F(\sum_i\delta_{x_i})dJ_n\)重建。总量归一唯一决定q₀，再与上一节Poisson密度级数比较，得到同一Gibbs律。这个证明不先假设另一份P相对Poisson有密度，也没有从GNZ名称直接宣布唯一。

对两体势，连续加入x、y的权重相乘，与反过来加入相同，因为φ对称。这给cocycle乘法相容性，也说明任意一个依赖配置的非负函数c，未必都能积成相容Gibbs权重。这里证明的是明示势给出的版本，不声称任意模零Papangelou代表在所有配置上自动满足点态关系。

## 4. 外部条件核及内外一致性

<a id="gibbs-specification"></a>

定义\(\Gamma_B\)(ξ,·)：保留ξ在B外的配置，在B内按上一节的归一Poisson密度重新抽取。外部积分联合可测由49章核积分给出；有限Poisson参考把其期望变成可测参数积分，\(Z_B\)正有限，所以得到概率核。加上外部限制的映射由评价可测，输出仍局部有限。

若A⊂B，参考Poisson在A、B∖A上独立，且权重恰分解为\(w_B(\eta_A+\eta_{B\setminus A}\mid\xi)=w_{B\setminus A}(\eta_{B\setminus A}\mid\xi|_{B^c})w_A(\eta_A\mid\eta_{B\setminus A}+\xi|_{B^c})\)。对各片非负F作Fubini，内部归一化说明给定B∖A及外部以后，A内条件律就是\(\Gamma_A\)。因此

\[ \Gamma_B\Gamma_A=\Gamma_B,\qquad P\Gamma_B=P\quad\hbox{for a Gibbs probability }P. \]

后一身份是DLR要求，不是有限核相容性自动保证已有无限P。反过来，若一份局部有限P满足全局GNZ与此势的c，先以F乘任意外部事件，对固定B析取给定外部的内部条件律。对可数生成测试类统一零集，条件核满足有限体积GNZ；上一节唯一性迫使它等于\(\Gamma_B\)。反方向DLR条件下逐窗口应用有限体积GNZ，再用可数窗口穷竭，恢复全局GNZ。所述等价对每个固定B为外部边缘a.s.，不擅自宣称一个版本同时覆盖任意不可数边界族。

## 5. 一种实际完成的无限体积存在证明

<a id="gibbs-infinite-existence"></a>

现专取\(E=\mathbb R^d\)、m=dx、常数z>0，以及\(\phi(x,y)=\psi(x-y)\)，ψ非负、连续、对称、紧支撑。取递增有界盒Bₙ穷竭空间，Pn=\(\Gamma_{B_n}\)(空配置)，盒外为空。它满足全局GNZ，cₙ为c乘1Bₙ。记\((n)_r=n(n-1)\cdots(n-r+1)\)，n<r时为0，\((n)_0=1\)。反复GNZ给每个紧K及r≥1的下降阶乘矩界\(E_{P_n}(\Xi K)_r\le(z|K|)^r\)，具体以\(F(x,\eta)=\mathbf1_K(x)(\eta K)_{r-1}\)代入GNZ，给\(E(\Xi K)_r\le z|K|E(\Xi K)_{r-1}\)，从r=1归纳；每个非负积分合法。特别地，局部一阶界与49章紧性给vague弱子列极限P，整数空间闭保证它仍为点配置。

须让GNZ真正传到极限。先取F(x,η)=h(x)H(η)，h∈Cc、H有界连续。函数\(c(x,\eta)=z\exp\{-\eta\psi(x-\cdot)\}\)联合连续：x在紧窗口时，平移ψ有共同紧支撑且一致连续，使用局部质量界。右侧积分于是有界连续，支配常数z‖H‖∫|h|。左侧\(\sum_{x\in\eta}h(x)H(\eta-\delta_x)\)也连续：在包含supp h内部的η连续性窗口，vague点收敛可把有限次出现逐个匹配；移点与删一次后仍vague收敛。窗口存在因球面质量至多可数例外；匹配来自小不交球的整数计数稳定，再缩球。

左函数未必有界，但绝对值≤‖h‖‖H‖Ξ(K)。二阶阶乘界给统一二阶矩，故一致可积；对极限，取连续截断χ≥1K，Portmanteau给同样有限二阶上界。将左函数截成有界连续函数再去截断，期望收敛。于是产品测试的GNZ在P下成立。两侧在每个空间紧窗口均有限，Cc空间测试与Cb配置测试各自生成Borel域，有限测度唯一性及单调类把身份推广到全部非负联合F。没有未经证明地交换弱极限与无界计数。

弥散参考还迫使P简单。GNZ取F(x,η)=1{η{x}≥1}，右侧对每个η的可数原子集积分为0，左侧正是重复位置中所有仍可删一次的出现总数，故无重数a.s.。用上一节条件化与有限体积唯一性，P满足DLR。因此我们已经构造出一份无限体积Gibbs概率，而不是只写相容核的名称。

## 6. 平稳版本与本证明没有覆盖的情形

<a id="gibbs-stationary-scope"></a>

常活动度与差分势使c平移协变，所以任何平移后的P仍满足同一GNZ及相同阶乘矩界。对大盒中的平移概率作均匀平均，仍满足GNZ并且律紧。取弱极限，上一节的连续性与一致可积论证再次保留GNZ。对任意固定平移a，两个平均盒的对称差体积除以盒体积趋0，故对有界连续测试期望差趋0；平移作用连续，使弱极限平稳。这给一份平稳无限体积Gibbs律。

没有证明无限体积唯一性，也没有把硬核不连续势、吸引且不稳定的势、任意长程能量或所有群空间纳入这个极限论证。有限体积非负可测势与硬排斥核已在前面证明存在及相容；其最广无限体积存在、相变与唯一性需要额外紧性或连续性工具。所有此类范围在覆盖矩阵独立记录，不计入本页已证。
