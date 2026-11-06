# Pólya预测、Gamma归一化与有限Dirichlet理论

## 1. 局部预测为什么还不等于顺序对称

<a id="polya-proof-rule"></a>

设颜色集合为1到d，aⱼ≥0且α=Σaⱼ>0。n次以后颜色j出现Nⱼ(n)次，下一项为j的核取(aⱼ+Nⱼ(n))/(α+n)，n=0也使用此式。分母为所有分子的和，有限状态核可测；第8、10章的顺序构造给唯一无限记录律。aⱼ=0的颜色初始概率0且永远不出现。

\[ P(X_1=x_1,\ldots,X_n=x_n)=\frac{\prod_{j=1}^d(a_j)^{\uparrow n_j}}{(\alpha)^{\uparrow n}},\qquad (a)^{\uparrow r}=\prod_{i=0}^{r-1}(a+i),\quad (a)^{\uparrow0}=1. \]

证明是逐项乘预测概率：颜色j每再出现一次，其分子依次为aⱼ、aⱼ+1、…；分母只看实验长度。故字概率只看各颜色计数，所有有限置换保律，柱集唯一性给无限交换性。相容性也直接来自每个核求和为1。若初始红蓝各1，红后加2红、蓝后加1蓝，则P(红蓝)=1/8而P(蓝红)=1/6；这些仍是合法无限预测核，却不交换。

## 2. Gamma变量为何能产生一个概率向量

<a id="polya-proof-gamma"></a>

对a>0定义Γ(a)=∫₀∞xᵃ⁻¹e⁻ˣdx：0附近a>0保证可积，无穷处指数压过幂。分部积分给Γ(a+1)=aΓ(a)，边界项为0。Gamma(a,1)的密度是xᵃ⁻¹e⁻ˣ/Γ(a)；参数为0时另约定变量恒0。以下速率固定1，不把形状参数与尺度混同。

先取所有aⱼ>0的坐标，令独立Yⱼ服从这些Gamma律，S=ΣYⱼ，Dⱼ=Yⱼ/S。S>0几乎必然。变换yⱼ=suⱼ、\(u_d\)=1−Σⱼ<d uⱼ，其Jacobian为sᵈ⁻¹。把联合密度代入，得下面分解。d=1时D₁=1，单独处理，不使用零维密度。

\[ \frac{e^{-s}s^{\alpha-1}}{\Gamma(\alpha)}\,ds\;\frac{\Gamma(\alpha)}{\prod_j\Gamma(a_j)}\prod_j u_j^{a_j-1}\,du_1\cdots du_{d-1},\qquad u_j>0,\quad\sum_j u_j=1. \]

原联合密度积分为1，第一因子积分为1，Tonelli因此证明第二因子也归一化，并证明S与D独立、S为Gamma(α,1)。定义D的律为\(\operatorname{Dir}(a_1,\ldots,a_d)\)。零参数坐标恢复为0，余下坐标按上述构造；至少一个参数正。两个正坐标的第一坐标就是Beta(a,b)，故第二章Beta是本构造的一维边缘，不需要重做其旧例。

## 3. 矩公式、合并与零参数边界

<a id="polya-proof-aggregate"></a>

对非负整数rⱼ，把uⱼʳʲ乘入密度，参数改成aⱼ+rⱼ；用刚证明的归一化常数得到矩公式。若aⱼ=0，rⱼ>0则矩为0；rⱼ=0的因子按1处理，不能写Γ(0)/Γ(0)。

\[ E\prod_j D_j^{r_j}=\frac{\prod_j(a_j)^{\uparrow r_j}}{(\alpha)^{\uparrow\sum_jr_j}},\quad ED_j=\frac{a_j}{\alpha},\quad \operatorname{Cov}(D_i,D_j)=\frac{\mathbf1_{\{i=j\}}a_i/\alpha-a_i a_j/\alpha^2}{\alpha+1}. \]

独立Gamma的和具有参数相加的Gamma律，已经由上一节S的密度证明。把坐标分成不交组，在每组内相加，组间仍独立Gamma；同除总和得到Dirichlet参数也按组相加。这证明任意有限分区细化后再合并，与直接粗分区的律一致，包含总参数为0的组。两个粗分区先取共同细化，便得到彼此相容，而不是仅核对一条特定分区链。

## 4. 有限维后验与预测是同一组计算

<a id="polya-proof-posterior"></a>

先抽D∼Dir(a)，再给定D独立抽颜色。一个具体长度n的字的似然为∏Dⱼⁿʲ。与Dirichlet密度相乘并归一化，给Dir(a+n)后验；零初始参数的颜色出现时该字原概率0，条件版本任取。不含排列组合系数，因为条件的是具体有序字，不是只给计数。

\[ \mathcal L(D\mid X_{1:n}=x)=\operatorname{Dir}(a_1+n_1,\ldots,a_d+n_d),\qquad P(X_{n+1}=j\mid X_{1:n})=\frac{a_j+n_j}{\alpha+n}. \]

积分字似然所得概率正是第一节上升阶乘公式。因此从预测核向前生成，与先抽Dirichlet向量再条件iid，是同一份记录律。第二个模型用第12章强律说明经验颜色比例趋D；第43章指导律唯一性遂识别第一个模型中的随机极限。这里不是先假设强化抽取本来独立。

## 5. 不同强化尺度与本页证明责任

<a id="polya-proof-scope"></a>

若每次加入相同质量c>0，只须把初始质量全部除以c，形状参数成为aⱼ/c。c=0时没有强化，得到固定概率的iid，而非将上式直接代入c=0。α必须正；本页没有把全零Gamma向量归一化。所有构造只用有限维变换、非负积分、顺序核、可积强律及43章唯一性。

回到[第44章有限预测](../chapters/44-dirichlet-process.md#dirichlet-finite)。
