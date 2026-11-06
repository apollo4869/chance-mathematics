# 经验概率的极限、弱拓扑与量词边界

## 1. 每个固定读数的极限

<a id="exchange-empirical-fixed"></a>

沿用标准Borel交换序列及已构造的ν。若f为固定Borel实函数且E|f(X₁)|有限，有限群平均给经验均值=E[f(X₁)|Gₙ]，反向鞅给如下几乎必然及L¹结论。条件律使νf=E[f(X₁)|J]，其绝对积分几乎必然有限。对指标函数就得到每个固定Borel集合的经验评价识别。

\[ L_N f=\frac1N\sum_{i=1}^N f(X_i)\longrightarrow\nu f\quad\text{a.s. and in }L^1\qquad(E|f(X_1)|<\infty). \]

在ν|f|=∞的参数上可将νf统一置0；后面的断言只在绝对积分有限的事件上使用。若只知道ν|f|几乎必然有限，而其无条件期望可能无限，则在每个固定μ的iid积律下应用第12章可积强律，再利用联合可测事件与混合核积分，仍得几乎必然收敛，但不声称L¹。所有这些结论先对每个固定f陈述；可数类才可直接统一零集。

## 2. 把弱距离写成可数读数

<a id="exchange-empirical-metric"></a>

以下另给E为Polish空间的弱收敛推论，使用一个固定的完备可分度量d。仅有抽象标准Borel结构时，先选一个Borel编码到Polish空间S，再讨论推送概率在S中的弱收敛；不为裸可测空间伪造一个规范拓扑。

\[ D(\mu,\eta)=\sup_{\substack{|f|\le1\\\operatorname{Lip}(f)\le1}}|\mu f-\eta f|. \]

这里的上确界可以实际换成一个固定可数类。取可数稠密点列，使用有限多个点及有理q，组成函数min(qᵢ+d(x,xᵢ))，再截到[−1,1]。这些函数构成可数类F，且在任意紧K上可以任意一致逼近每个上述Lipschitz函数：选稠密点的有限δ网，让qᵢ距f(xᵢ)小于δ，则所得下包络在K上介于f−δ与f+3δ之间。截断不增加误差。

对给定μ、η，由Polish概率的单个紧性选同一个高概率紧集。在其上作上述逼近，补集用函数界1控制，便证明D恰等于对F的上确界。μ↦μf由评价σ代数可测，因为简单函数与单调收敛可处理任意有界Borel f。因此D是两个概率参数的可测函数，事件D(Lₙ,μ)→0对(μ,记录)联合可测。

若D(μₙ,μ)→0，对闭集C用max(0,1−m d(x,C))逼近1C；每个固定m的函数可除以max(1,m)纳入上述测试类。先取n极限，再让m增大，得闭集上界，依第24章Portmanteau便有弱收敛。这里没有把总变差与弱距离混同。

## 3. 条件强律怎样给整份经验概率的极限

<a id="exchange-empirical-weak"></a>

先固定一份μ，研究iid(μ)。给ε>0，紧性给K使μ(Kᶜ)<ε。由第24章Arzelà–Ascoli，所有有界一阶Lipschitz函数在K上的限制全有界，故有一个以这些函数为中心的有限ε网。对网中函数和1K同时使用强律。对任意f取最近网点g，分开K与补集，得到下面的统一估计。

\[ D(L_N,\mu)\le\max_{g\in\mathcal F_{\varepsilon,K}}|L_Ng-\mu g|+2\varepsilon+2L_N(K^c)+2\mu(K^c),\qquad \limsup_N D(L_N,\mu)\le6\varepsilon. \]

对ε=2⁻ʲ重复，只需可数个紧集与有限网，故D(Lₙ,μ)→0在μ积律下几乎必然。每个μ可有自己的紧集与网，不需要存在一套对所有μ都统一高概率的紧集。上节已经把最终收敛事件证明为联合可测，所以可用K(μ,·)与M积分，得到交换记录上的D(Lₙ,ν)→0。

\[ L_N\Rightarrow\nu\quad\text{a.s. on a Polish state space, or after a specified Borel encoding into a Polish space}. \]

这是一份随机极限的逐路径识别，不是说Lₙ与ν必须在总变差下接近，也不是把“对每个测试分别几乎必然”未经处理地变成“所有测试同时”。可数可测距离、条件积分与紧集上的有限网，正好填上这两处逻辑间隙。

## 4. 为什么不能对所有Borel集同时取同一个零集

<a id="exchange-empirical-boundary"></a>

取iid均匀[0,1]。对每个事先固定的Borel集合A，强律给Lₙ(A)→Leb(A)。但对每条记录，所有观察值组成的可数集合D也是Borel，Leb(D)=0而所有Lₙ(D)=1。因此不可能找一个概率1集合，使里面每条记录对所有Borel A都同时评价收敛。

\[ d_{\rm TV}(L_N,\operatorname{Leb}_{[0,1]})=1\quad\text{for every }N,\qquad L_N\Rightarrow\operatorname{Leb}_{[0,1]}\quad\text{a.s.} \]

总变差的第一个等式只需选前N个观察值组成的有限集合。这个边界保护了“经验识别指导概率”的确切含义：可数决定评价、每个固定可积测试以及选定Polish拓扑下的弱极限。它不声称有限记录已经在一切可测事件上复制了连续概率。回到[第43章经验概率](../chapters/43-exchangeability.md#exchange-empirical)。
