# T-PALM-INVERSION：反演、质量输送与时间—周期对偶

返回[第50章](../chapters/50-palm-gibbs.md#palm-inversion)。先在\(\mathbb R^d\)的平稳随机Radon测度中工作，强度\(0<\lambda<\infty\)，Palm律P⁰由T-PALM构造。后半周期定理专限实线简单非空点配置；不将它推广到有重数或一般群。

## 1. 含空配置时也合法的加权反演

<a id="palm-inversion-weighted"></a>

选处处正、连续、有界、可积h，\(\int hdx=1\)。平均强度给EΞh=λ，故Ξh有限a.s.，且Ξh>0当且仅当Ξ≠0。对非负F，用非中心化Campbell于测试\(F(\xi)h(x)/(\xi h)\)，在ξh=0或∞时取0，得

\[ \mathbb E[F(\Xi)\mathbf1_{\{\Xi\ne0\}}]=\lambda\int_{\mathbb R^d}\mathbb E^0\left[\frac{h(x)F(\theta_{-x}\eta)}{(\theta_{-x}\eta)h}\right]dx. \]

所有映射由联合核积分可测。分母对dx×P⁰几乎处处正有限：原Campbell测度不给Ξh异常事件质量，中心化恒等式把这个零测集传给乘积；P⁰也不见零测度，因为Campbell积分对零实现恒为0。公式先对非负量使用Tonelli，不要求F可积。它恢复P在非零配置上的部分；空配置质量要另加，不能从只观察出现的Palm概率中直接读出。给定λ与P⁰，取F=1也可计算非零总概率。

## 2. 实线上的下一点与质量输送

<a id="palm-cycle-transport"></a>

现在Ξ为平稳简单点过程、非空a.s.、有限正强度。其点集两侧无界a.s.：若非空且右有界，局部有限闭点集有最大点R；这个事件平移不变，条件于它R的概率律需对所有平移不变，不可能是实线上的概率。左端同理。条件事件概率若正，归一化合法，故各自必须概率0。此路径性质由Campbell传给P⁰。

在根配置η中以\(\cdots<T_{-1}<T_0=0<T_1<\cdots\)枚举点，τ η=θT₁η。位置由局部计数与可测枚举恢复，T₁>0有限，τ可测且逆为移到前一点。对非负可测k(η,u)，定义根向位移u的点输送质量k；不含不存在点的贡献。取非负h积分1，对同一个双和按发送点或接收点使用Campbell与Tonelli，得到

\[ \mathbb E^0\sum_{u\in\eta}k(\eta,u)=\mathbb E^0\sum_{u\in\eta}k(\theta_u\eta,-u). \]

细节是对\(\mathbb E\sum_{x,y\in\Xi}h(y)k(\theta_x\Xi,y-x)\)先以x作Campbell：写u=y−x，积分\(\int h(x+u)dx=1\)，得到λ倍左侧；先以y作Campbell，得到λ倍右侧。允许两边无穷，不作无穷减法。令\(k(\eta,u)=\mathbf1_{\{u=T_1\}}G(\theta_u\eta)\)，每点只有一个前驱与后继，身份给E⁰G∘τ=E⁰G。P⁰因而对换到下一点不变。这不是全实时间的平移平稳性。

## 3. 从周期回到时间的积分

<a id="palm-cycle-inversion"></a>

每个实数y属于唯一半开周期[x,x+gapₓ)。把\(\int h(y)F(\theta_y\Xi)dy\)按这些周期分割，对每个发送点x应用Campbell，得到

\[ \mathbb EF(\Xi)=\lambda\mathbb E^0\int_0^{T_1}F(\theta_t\eta)dt,\qquad \lambda\mathbb E^0T_1=1. \]

左侧来自平稳性与∫h=1；右侧的空间积分∫h(x+t)dx=1。F非负时Tonelli足够，F有界有符号时由F=1先得平均周期有限再分正负。若允许空配置，左侧应改成E[F1非空]，相应λE⁰T₁=P(非空)。因此书中简单版始终明确非空a.s.。

## 4. 反方向也必须构造：周期律的悬挂

<a id="palm-cycle-suspension"></a>

设Q为双侧无界、简单、根在0的配置概率，τ不变，\(m=E_QT_1\in(0,\infty)\)。定义\(PF=m^{-1}E_Q\int_0^{T_1}F(\theta_t\eta)dt\)。这是概率：非负可加由MCT，总量由m归一。也可先按T₁/m偏置Q，再在周期内均匀选t，给实际可测构造。

对有界F及a>0，周期积分平移差是\(G_a(\tau\eta)-G_a(\eta)\)，其中\(G_a(\eta)=\int_0^aF(\theta_t\eta)dt\)。这两个量有界于a‖F‖，τ不变使期望差0，所以P对正平移不变，负平移由逆作用得到。接着验证Palm，不能只验平稳：

\[ \mathbb E_P\sum_{x\in\Xi}h(x)G(\theta_x\Xi)=\frac1m\mathbb E_Q\int_0^{T_1}\sum_{k\in\mathbb Z}h(T_k-t)G(\theta_{T_k}\eta)dt=\frac1m\left(\int h\right)E_QG. \]

最后等号逐项令η′=τᵏη；Q对全部整数幂不变。变量u=t−Tₖ把该项区间变成η′的[T₋ₖ,T₁₋ₖ)，这些区间对k分割全实线，所以各项相加的h(−u)积分就是∫h。非负Tonelli保证交换，τ可逆保证负整数幂也保律。因此强度1/m，Palm恰为Q；时间—周期两种构造确实互逆。

## 5. 更新例子的新增结论与无限均值边界

<a id="palm-renewal"></a>

取严格正iid双向间隔Lₖ，0<m=EL₁<∞。12章强律使两侧部分和趋无穷，根配置局部有限；换根只平移iid下标，Q对τ不变。悬挂得到强度1/m的平稳更新过程，而且证明其Palm律就是原来的iid点根记录。19章给出了构造，本页新增的是一般Palm识别和互逆性。对年龄A与余寿命R，

\[ \mathbb E_P\varphi(A,R)=\frac1m\mathbb E\int_0^{L_1}\varphi(t,L_1-t)dt. \]

这推出含观察时刻的总间隔按长度偏置、内部位置均匀，并适用于算术间隔：实时间平稳性随机化相位，不要求非算术。若EL₁=∞，Q仍可能合法，但周期公式不能归一为有限正强度的非空平稳概率；若λ=0且局部有限，则每个有理窗口计数期望0，过程空a.s.。此结论只排除所声明平稳概率构造，不宣称所有无限均值极限都不存在。
