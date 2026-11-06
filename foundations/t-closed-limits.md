# T-CLOSED-LIMITS：容量与随机闭集的弱收敛

返回[第51章](../chapters/51-random-closed-sets.md#sets-convergence)。E采用T-FELL的LCSC度量假设及proper度量ρ；所有随机闭集允许空集。弱收敛是在该专题实际证明的紧Polish Fell空间上，不是所有紧命中读数逐点收敛的别名。

## 1. Portmanteau能说什么

<a id="closed-portmanteau"></a>

记\(T^\circ(U)=P(F\cap U\ne\varnothing)\)于开U。可数紧邻域内逼近给\(T^\circ(U)=\sup_{K\subset U,\ K\text{ compact}}T(K)\)，可取一条递增紧列：用紧穷竭与距离E∖U的下界即可。T-FELL中\(H_U\)开、\(H_K\)闭，因此24章给

\[ F_n\Rightarrow F\quad\Longrightarrow\quad\liminf_nT_n^\circ(U)\ge T^\circ(U),\qquad\limsup_nT_n(K)\le T(K). \]

若紧K满足\(T(K)=T^\circ(\operatorname{int}K)\)，开命中下界与闭命中上界夹出Tₙ(K)→T(K)。这里边界例外是“F命中K却不命中其内部”的概率，不应误写成仅看某个预选位置的归属。一般紧K没有此条件；Fₙ={1/n}→{0}时，在K={0}上Tₙ=0、T=1。

## 2. 容量连续测试足以决定弱极限

<a id="closed-capacity-convergence"></a>

定理：对已给定的随机闭集F，Fₙ⇒F，当且仅当对全部满足上节容量连续条件的紧K有Tₙ(K)→T(K)。必要性已证；充分性不能只说“容量唯一”。先用Fell空间紧性与24章Prokhorov，从任意子列抽取弱收敛子列，其极限律记Q。下面识别Q。

任取非空紧K，令\(K^r=\{x:\rho(x,K)\le r\}\)，r>0，它紧。随机距离D=inf{ρ(x,y):x∈F,y∈K}在F空时取∞。proper性保证距离有限时在相关有界区域取到，故{D≤r}=H(Kʳ)。这也证明D可测。若F命中Kʳ却不命中int Kʳ，则D=r；因为{ρ(x,K)<r}包含在该内部。D的有限分布至多有可数个原子，故除可数r外，Kʳ都是所需连续测试。可选rⱼ↓0且全部合法。

对子列弱极限Q，Portmanteau及测试收敛给\(Q(H_{K^r})\ge T(K^r)\)，并且\(Q(H_{\operatorname{int}K^r})\le\liminf_nP(F_n\cap\operatorname{int}K^r\ne\varnothing)\le T(K^r)\)。所以Q(\(H_K\))≤T(Kʳ)；让rⱼ↓0得Q(\(H_K\))≤T(K)。另一方面闭命中不等式与两份闭集律的递减紧连续性给Q(\(H_K\))≥T(K)。空K两边均0。因此Q容量等于T，T-CHOQUET唯一性给Q=Law(F)。任意子列均有相同极限，故全列弱收敛。

## 3. 给定候选容量时不能忘记存在性

<a id="closed-candidate"></a>

若只给候选T而尚无F，必须先验证T-CHOQUET的归一、完全交替与递减连续；之后才可应用上一节。若Tₙ在所有紧集上趋一个满足这些条件的T，这当然是充分条件，却不是必要条件。例：Fₙ={n}在实线Fell趋∅，虽每份非空；闭集空间的紧性允许全部形状逃向无穷远，而不保证P(Fₙ≠∅)趋P(F≠∅)。非空事件在非紧E的Fell空间不是自动的连续事件。

## 4. 连续映射必须检查具体运算

<a id="closed-mappings"></a>

24章连续映射定理可直接用于T-FELL已证的有限并、proper连续空间映射及平移。两份随机集合合并须先有二者的联合弱收敛，不能只以两个边缘收敛替代。交、补集、支撑和无限时间范围均不能凭名称套用：交的确定性反例已在T-FELL；支撑与路径范围的精确边界见T-RANDOM-SHAPES。补集一般为开集，本来就不是同一状态空间。
