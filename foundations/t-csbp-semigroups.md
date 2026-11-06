# T-CSBP-SEMIGROUPS：由繁殖近似建立连续状态分枝

回到[第58章](../chapters/58-multifurcation.md)。下文完整建立临界/次临界有限均值机制的转移半群、Feller过程及灭绝判据；不把人口半群等同于完整谱系。

## 1. 机制及离散后代分布

<a id="cb-mechanism"></a>

\[ \psi(q)=a q+\beta q^2+\int_0^\infty(e^{-qr}-1+qr)\,\pi(dr),\quad a,\beta\ge0,\quad \int_0^\infty(r^2\wedge r)\,\pi(dr)<\infty. \]

假设\(\psi\)非线性且满足Grey条件\(\int_1^\infty dq/\psi(q)<\infty\)。这保证\(\psi\)严格递增至无穷、\(\psi(q)/q\to\infty\)。令\(\phi=\psi^{-1}\)、\(v_\lambda=\phi(\lambda)\)、\(c_\lambda=\psi'(v_\lambda)>0\)，定义

\[ g_\lambda(s)=s+\frac{\psi(v_\lambda(1-s))}{v_\lambda c_\lambda},\quad 0\le s\le1. \]

它确为后代母函数：常数项\(p_0=\lambda/(v_\lambda c_\lambda)>0\)，一次项\(p_1=0\)，二次项为\(\beta v_\lambda/c_\lambda+(v_\lambda/(2c_\lambda))\int r^2e^{-v_\lambda r}\pi(dr)\)，j≥3次项为\((v_\lambda^{j-1}/(c_\lambda j!))\int r^j e^{-v_\lambda r}\pi(dr)\)。各项非负，令s↑1得和为1；导数在1为\(1-a/c_\lambda\le1\)。积分级数交换用非负项Tonelli；远端一次矩与近端二次矩保证所列积分有限。

令每个个体以速率\(c_\lambda\)死亡并按\(g_\lambda\)繁殖。先按代数构造GW树；因均值不大于1、\(p_0>0,p_1=0\)，第20章灭绝定理保证整树有限几乎必然，因而赋予独立指数寿命后无有限时爆炸。以下使用的是有限个祖先；并不从有限期望人口直接臆断任意过程无爆炸。

## 2. Laplace核的存在而非形式猜测

<a id="cb-kernel"></a>

若一个祖先在时间t的人口母函数为\(F_t^\lambda(s)\)，按首个寿命分片并解有界更新方程，得到\(\partial_tF=c_\lambda(g_\lambda(F)-F)\)、\(F_0=s\)。直接代入可得精确恒等式

\[ v_\lambda(1-F_t^\lambda(e^{-q/v_\lambda}))=u_t(v_\lambda(1-e^{-q/v_\lambda})),\qquad \partial_tu_t(q)=-\psi(u_t(q)),\quad u_0(q)=q. \]

这个ODE在\([0,q]\)有唯一全局解：\(\psi\)局部Lipschitz，解递减、不穿越0。以\(\lfloor xv_\lambda\rfloor\)个祖先出发，人口除以\(v_\lambda\)后的Laplace变换为\(F_t^\lambda(e^{-q/v_\lambda})^{\lfloor xv_\lambda\rfloor}\)，趋于\(e^{-xu_t(q)}\)。这些离散概率在\([0,\infty)\)紧：均值不超过x，用Markov不等式；极限Laplace在q↓0趋1，排除无穷质量。第14章唯一性因此给出唯一概率核\(P_t(x,\cdot)\)。x或t连续变化时同一Laplace与紧性论证给出弱连续性，故评价核可测。

\[ \int e^{-qy}P_t(x,dy)=e^{-xu_t(q)},\qquad P_{s+t}=P_sP_t,\qquad P_t(x+x',\cdot)=P_t(x,\cdot)*P_t(x',\cdot). \]

后两式分别由ODE流的复合性和Laplace乘积唯一性得到，因而是已建立的Chapman–Kolmogorov与分枝性质。反过来，单个Laplace公式若尚未证明为概率核，就不能如此使用。

## 3. Feller路径实现及生成元

<a id="cb-feller"></a>

在\(C_0([0,\infty))\)上，指数函数\(e^{-qx},q>0\)的有限线性组合稠密：其代数分离点、无共同零点，或令y=e^{-x}用[0,1]上的多项式逼近且在y=0取零。对这些函数，\(P_te^{-qx}=e^{-xu_t(q)}\in C_0\)，t↓0时一致收敛到\(e^{-qx}\)：参数u趋q>0，利用\(\sup_x x e^{-cx}<\infty\)。正收缩性将两结论延至全部\(C_0\)。故第28章实际Feller路径实现定理给出非负càdlàg强Markov版本。该上游专题仍待专家终审，但本节已验证其强连续、保守及Polish局部紧状态空间条件。

\[ \mathcal A e^{-qx}=x\psi(q)e^{-qx}. \]

生成元导数在\(C_0\)范数下成立，因为u的二阶时间误差为\(O(t^2)\)，而\(x^2e^{-cx}\)有界。它确定上述半群：Laplace流已唯一识别全部转移核。这里不宣称任意未指定定义域的形式算子都唯一确定过程。零吸收由\(P_t(0)=\delta_0\)得到。

## 4. 灭绝、稳定机制与尺度

<a id="cb-extinction"></a>

由\(e^{-qZ_t}\downarrow\mathbf1_{\{Z_t=0\}}\)及有界收敛，\(P_x(Z_t=0)=e^{-xv(t)}\)，其中\(v(t)=u_t(\infty)\)，并且\(\int_{v(t)}^\infty dq/\psi(q)=t\)。Grey条件保证每个t>0的v有限；临界/次临界下v(t)↓0，故有限时刻最终吸收的概率为1。没有Grey条件时，以\(v(t)=\infty\)解释；例如\(\psi(q)=aq\)给\(Z_t=xe^{-at}>0\)，仅趋零而不有限时灭绝。

\[ \psi(q)=q^\alpha,\quad1<\alpha\le2:\quad
u_t(q)=\big(q^{1-\alpha}+(\alpha-1)t\big)^{-1/(\alpha-1)},\quad
v(t)=((\alpha-1)t)^{-1/(\alpha-1)}. \]

对c>0，\(cZ_{c^{1-\alpha}t}\)在初值cx下具有同一转移律，直接代入Laplace公式即可逐个有限维核验证。α=2时\(\mathcal A f=xf''\)在光滑紧支撑测试函数上可由离散生成元或Laplace决定类验证；这是Feller分枝的方差规范。α<2的Lévy测度为\(\pi(dr)=\alpha(\alpha-1)r^{-1-\alpha}dr/\Gamma(2-\alpha)\)：两次分部积分给\(\int(e^{-qr}-1+qr)r^{-1-\alpha}dr=\Gamma(2-\alpha)q^\alpha/(\alpha(\alpha-1))\)，端点项因1<α<2消失。

公开依据：[Duquesne–Winkel《Growth of Lévy trees》](https://perso.lpsm.paris/~tduquesne/Documents/Duquesne_Winkel_PTRF_2007.pdf)，PTRF139(2007),313–371，第1、4节。以上是用本书既有Feller实现重建的证明，不声称沿用了原文全部证明路线。超临界、无限均值及所有CSBP分类不在本专题已证范围。
