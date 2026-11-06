# T-POINT-TRANSFORMS：标记、映射与均值

返回[第48章](../chapters/48-point-processes.md#points-marking)。使用[T-POINT-MEASURES](t-point-measures.md#point-space-measurable)的带重数可测枚举和[T-POISSON-SPACE](t-poisson-space.md)的完整可测非负测试泛函。

## 1. 每次出现分别得到标记

<a id="point-transform-mark"></a>

设N是E上局部有限点过程，F为标准Borel标记空间，κ为E到F的概率核。按枚举给每次出现独立均匀数，通过第10章核随机化取标记，构成M=\(\sum_i\delta_{(x_i,y_i)}\)。同一位置的不同出现必须各取独立标记，不能共用一枚数。M在地面相对紧窗口A×F上有限。若F也是局部紧第二可数，则乘积空间每个紧集的地面投影紧，因此M为乘积空间的局部有限点过程。一般标准Borel F时只使用评价σ域和地面局部有限性，不虚构F上的vague拓扑。

\[ \mathbb E[e^{-Mf}\mid N]=\prod_{x\text{ occurrence in }N}\kappa(x,e^{-f(x,\cdot)})=\exp\{-N h\},\qquad h(x)=-\log\kappa(x,e^{-f(x,\cdot)}). \]

对无限乘积先在有限枚举前缀计算，再用有界收敛；h可取∞。若N为Poisson(μ)，代入其泛函，得到exp{−∫∫(1−e⁻ᶠ)κ(x,dy)μ(dx)}。因而M是强度μ(dx)κ(x,dy)的PRM：不交有限强度集合的独立Poisson计数由该泛函证明，不是从单个标记边缘推断。

## 2. 映射定理必须检查目标窗口

<a id="point-transform-map"></a>

设T:E→F为可测映射，F局部紧第二可数。\(T_*N(A)=N(T^{-1}A)\)评价可测，但未必局部有限。对Poisson(μ)，若ν=\(T_*\mu\)在所有紧集上有限，则它是Radon（局部紧第二可数空间上局部有限Borel测度的正则性，由T-RIESZ的同样开集/紧逼近论证得到），且\(T_*N\)∈Mₚ(F)几乎必然。将f换为f∘T，泛函立即给Poisson(ν)。若有紧K使ν(K)=∞，计数在K上几乎必然无穷，不能称局部有限点过程。

对任意而非Poisson的N，一个充分条件是T连续且proper，即紧集原像紧；这时逐样本直接验证。对Poisson过程可以用较弱的强度原像条件。映射不保证简单性：有限强度区间全部映到0，得到一个Poisson数目的重合点；实线Lebesgue强度全部映到0，则在0堆积无穷点。随机位移是先标记再映射，仍须检查所得强度局部有限。

## 3. 独立稀释与叠加

<a id="point-transform-thin"></a>

给每次出现独立Bernoulli(q(x))标记，分别保留标记1、0的点为N₁、N₀。对两个非负测试f,g，将乘积空间测试写为f(x)\(\mathbf1_{\{1\}}\)+g(x)\(\mathbf1_{\{0\}}\)。标记泛函分解为exp{−μ(q(1−e⁻ᶠ))}exp{−μ((1−q)(1−e⁻ᵍ))}，以联合Laplace唯一性证明N₁、N₀是独立PRM，而非只各自Poisson。

可数个独立Poisson(μⱼ)叠加，在Σμⱼ局部有限时由有限乘积、单调收敛得Poisson(Σμⱼ)。无局部有限条件可能失败。依赖删点也不享有稀释结论：在有限窗口只保留最左一点（若有），计数仅取0或1，一般不为Poisson。若点有原子，最左并列还必须明确选择出现的规则。

## 4. Campbell均值与补偿二阶计算

<a id="point-transform-campbell"></a>

任意评价可测点过程Ξ都有强度测度ν(A)=EΞ(A)，可数可加由Tonelli给出；ν未必局部有限，甚至未必σ有限。对非负简单函数逐项线性，再用单调收敛，证明Campbell均值公式。带符号f要求∫|f|dν<∞。这里f确定；若f依赖整个配置，不能直接把它移到ν下积分，第50章才承担Palm及Mecke结构。

\[ \mathbb E\int f\,d\Xi=\int f\,d\nu.\qquad \mathbb E\left[\left(\int f\,d(N-\mu)\right)\left(\int g\,d(N-\mu)\right)\right]=\int fg\,d\mu. \]

第二式先对有限强度不交单元上的简单f,g成立：独立计数的中心乘积消去交叉项，Var N(A)=μ(A)。一般L²(μ)函数用有限窗口简单函数逼近，等距使积分在L²(P)中唯一延拓。其均值0且协方差如式；若f还在L¹，延拓与通常有符号随机测度积分相同，因Campbell使L¹逼近成立。仅L²时不得将两个可能无穷的普通积分相减。
