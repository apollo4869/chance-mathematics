# T-MULTIPARAMETER：交换保测变换的长方体平均

本页完成[第41章多参数结果](../chapters/41-ergodic-theory.md#ergodic-multiparameter)。固定有限d，T₁,…,T_d两两交换且各保概率，不必可逆；1<p<∞，f∈Lᵖ。长方体的所有整数边长都允许独立变化，极限指min n_i→∞。

## 1. 交换投影及其精确识别

<a id="multiparameter-proof-projections"></a>

令U_i f=f∘T_i，A^i_n为对应一维平均，P_i=E[·|I_i]。T-ERGODIC已证各A^i_n在Lᵖ强收敛P_i，且两类算子范数≤1。U_i与U_j交换，所以A^i_n与A^j_m交换。先固定m送n到∞，再送m到∞，强收敛与统一有界性使P_iP_j=P_jP_i；同样P_i与U_j交换。

在L²上，P_i为交换正交投影，P=P₁…P_d的范围恰为共同固定子空间：P的值被各P_i固定；任何共同固定向量又被P保留。P自伴且幂等，故是到L²(J)的正交投影，J=∩I_i。对有界函数及其Lᵖ逼近，得到P=E[·|J]在每个Lᵖ上成立。交换条件在此有实质作用，不能对任意两个条件期望直接把乘积称为到σ域交集的投影。

## 2. 同时控制全部长方体

<a id="multiparameter-proof-maximal"></a>

\[ M_i g=\sup_{n\ge1}A_n^i|g|,\qquad |A_{\mathbf n}f|\le M_1M_2\cdots M_d|f|,\qquad \|M_1\cdots M_d|f|\|_p\le\left(\frac p{p-1}\right)^d\|f\|_p. \]

第一份不等式只使用平均的正性：对固定外层平均，把内层每个长度的平均依次换成上确界。逐次应用一维强型估计得到后式。这里M_i非线性，不曾把它们当成可交换线性投影；只需要按固定顺序复合。因多重指标可数，最大函数可测且有限几乎必然。

## 3. 稠密类、共同极限与Lᵖ收敛

<a id="multiparameter-proof-limit"></a>

先令f有界。恒等式f−Pf=Σ_i P₁…P_{i−1}(I−P_i)f把它分成各方向残差。一维均值收敛使(I−P_i)f由f−A^i_nf逼近；有限代数给f−A^i_nf=(I−U_i)g_{i,n}，其中g_{i,n}=Σ_{k=0}^{n−2}(n−1−k)U_i^k f/n有界。前置投影与U_i交换且保有界，故f由有界共同固定函数加Σ_i(I−U_i)g_i在Lᵖ逼近。再截断任意f，得到此类在全部Lᵖ稠密；这里不把L²稠密误当成p>2的自动稠密。

对一个这样的余边界，交换使第i方向平均望远镜消去，其余方向平均不增加上界，故全部长方体的绝对平均≤2‖g_i‖∞/n_i。对稠密类已有共同几乎必然极限。一般f的长方体尾部振荡被2M₁…M_d|f−h|控制，Markov与上一节使超出ε的概率至多常数ε^{-p}‖f−h‖ₚ^p。取逼近并对可数ε取交，所有min n_i→∞长方体同趋一个有限极限。

Lᵖ极限可直接识别。把∏A^i_{n_i}−∏P_i望远镜拆开，利用交换与收缩，范数至多Σ_i‖(A^i_{n_i}−P_i)f‖ₚ→0。所以极限是Pf=E[f|J]；依概率极限唯一使它与刚才逐点极限相同。没有用迭代极限代替共同极限。任意长方体L¹端点、一般群Følner序列及比遍历不在本页范围。[返回正文](../chapters/41-ergodic-theory.md#ergodic-entropy)。
