# T-LIE-LEVY：紧矩阵Lie群上的实际构造

配套[第40章](../chapters/40-stochastic-geometry.md#geometry-lie-jumps)。本页实际证明给定紧光滑矩阵Lie群G⊂O(N)上的一般小跳三元组构造、生成元及固定截断下的三元组唯一性。没有把它冒充任意Lie群上所有Lévy过程的Hunt必要性分类，也不使用48章一般点过程或Peter–Weyl理论。

## 1. 矩阵乘积先给出正确的局部规则

<a id="lie-proof-geometry"></a>

假定G已经是O(N)的光滑嵌入子流形，乘法及逆光滑；不把任意闭子群光滑性定理当作已证。其Lie代数为恒等元I处切空间𝔤，元素A为反对称矩阵，左不变场为\(X_A(g)=gA\)。常微分方程g′=gA的唯一解为g exp(tA)，且切向ODE使它留在G；紧性保证全球存在。矩阵指数的幂级数给在0处微分为恒等，T-GEOMETRY局部逆论证提供指数图。

选𝔤的基Aᵢ，在恒等元附近写h=exp(ηⁱ(h)Aᵢ)，取等于1于更小邻域的光滑截断ρ，令χⁱ=ρηⁱ，支撑外为0。Taylor与有限维紧邻域估计给h−I−χⁱ(h)Aᵢ=O(‖h−I‖²)。这个二阶余项才允许漂移补偿收敛；单独∫χν可能发散。

\[ b\in\mathbb R^d,\quad q=\sigma\sigma^{\mathsf T}\ge0,\quad A_\alpha=\sigma_{i\alpha}A_i,\qquad
\nu(\{I\})=0,\quad \int_G\|h-I\|^2\,\nu(dh)<\infty. \]

ν为G\{I}上的Radon测度。紧性使上面的条件等价于通常邻域二阶可积且远离I处质量有限。用环带分解，每环ν有限，21章独立Poisson时钟与条件标记、8章可数乘积便实际构造强度dtν(dh)的随机测度；与Brownian驱动取独立乘积。34章可预测L²补偿积分适用于这些有限维矩阵分量。

## 2. 无限小乘积怎样成为一个群值过程

<a id="lie-proof-construction"></a>

\[ C=b^iA_i+\frac12\sum_\alpha A_\alpha^2+\int_G(h-I-\chi^i(h)A_i)\nu(dh),\qquad
dY_t=Y_{t-}C\,dt+\sum_\alpha Y_{t-}A_\alpha\,dW_t^\alpha+\int_GY_{t-}(h-I)\,\widetilde N(dt,dh),\quad Y_0=I. \]

先截断至‖h−I‖>ε。ν在此有限，连续段取左不变Stratonovich漂移(bⁱ−∫χⁱdν)Aᵢ以及Gaussian场Aα，跳到来时把当前状态右乘h。紧G上的连续段不爆炸，有限时段只有有限个跳，故这是真正群值过程Yε。把有限跳改写为补偿积分，得到上式的Cε，其中积分仅在截断集上。这一步说明为什么不能直接使用不收敛的那份未补偿漂移。

二阶余项给Cε→C，且supε‖Cε‖有限。所有Yε的Frobenius范数恒为√N。对两截断的差，连续及补偿跳积分的Doob–L²估计、漂移Cauchy–Schwarz、矩阵乘法范数界给下面的不等式，常数只依T和统一的二阶系数，不含可能发散的∫χν。Gronwall得到最大L² Cauchy；每个T取可求和子列，几乎必然一致收敛，随后对整数T对角化。

\[ E\sup_{s\le T}\|Y^\varepsilon_s-Y^\delta_s\|^2
\le K_T\left(\|C_\varepsilon-C_\delta\|^2+
 \int_{\{\|h-I\|\le\max(\varepsilon,\delta)\}}\|h-I\|^2\nu(dh)\right). \]

一致极限为càdlàg，G在矩阵空间中闭，故Y始终在G且不爆炸。等距与漂移控制让所有积分通过极限，实际满足上式。反向任意两解的差满足无误差Gronwall估计，先局部化状态幅度再放开，故路径唯一。线性系数加有限二阶跳预算也可直接作35章Picard；这里截断法额外证明了群约束，而不只构造一个环境矩阵解。

对确定s，Yₛ⁻¹Yₛ₊ₜ满足初值I的同一方程，驱动是s之后的Brownian和Poisson增量。它们独立于完整过去且同分布；路径唯一性把未来识别为这些增量的同一可测解函数。因此左增量独立且平稳。L²连续时间估计给随机连续性；加上已构造的càdlàg路径，Y确为群上的Lévy过程，而非只具有某种单时刻分布。

## 3. 生成元、截断及已证明的唯一性

<a id="lie-proof-generator"></a>

\[ Af(g)=b^iX_if(g)+\frac12q^{ij}X_iX_jf(g)
+\int_G\big(f(gh)-f(g)-\chi^i(h)X_if(g)\big)\nu(dh). \]

对光滑f用T-GEOMETRY的局部环境延拓，再用34章跳跃Itô公式。连续Gaussian二阶项与½ΣAα²的漂移合成½qⁱʲXᵢXⱼ；C中的积分与跳修正的线性项相消，剩下上式。近I的余项一致为O(‖h−I‖²)，远处ν有限，故可测、可积、DCT均合法。紧G上Af连续有界，E[f(gYₜ)−f(g)]=∫₀ᵗE Af(gYₛ)ds，再以随机连续性送t↓0得到真正生成元。

固定χ时，生成元唯一识别此三元组：在I附近为0的光滑测试先识别ν在每个远离I的紧集上的积分，光滑逼近及Radon唯一性给ν。减去这份已知积分，取零值零一阶、任意对称二阶jet的局部测试，识别q；再取任意一阶jet识别b。换χ为χ′时，b′=b+∫(χ′−χ)dν，差为二阶故有限；这与改变过程不同。

还可在本构造的L²方程类别中得到过程唯一；并未证明任意群值Lévy过程一定有该Hunt形式，也未证明一般退化群生成元的抽象martingale problem唯一性。这两项必要性/最广刻画仍开放，不用一个熟悉公式掩盖证明责任。

## 4. 非交换性与度量Brownian的联系

<a id="lie-proof-structure"></a>

非交换的必要性可以在Heisenberg群直接看见：(x,y,z)(x′,y′,z′)=(x+x′,y+y′,z+z′+xy′)。a=(1,0,0)、b=(0,1,0)满足ab=(1,1,1)、ba=(1,1,0)。这不属于前面的紧矩阵定理，但这个有限乘积计算本身不需任何概率极限定理。独立标记的复合Poisson过程按到达次序乘a、b，已经能看见欧氏普通求和遗漏的顺序信息；不能把第27章的总和取一次指数就当一般群过程。

在紧G⊂O(N)上，Frobenius内积在共轭下不变，左平移延拓的度量因而也右不变。对左不变场，∇X Y=½[X,Y]无挠；迹的循环性给〈[X,Y],Z〉+〈Y,[X,Z]〉=0，故它保持度量。Levi–Civita唯一性识别这个联络。正交左不变基的∇XᵢXᵢ=0，因此b=0、q=I、ν=0时，前面构造的过程正是该双不变度量的Riemannian Brownian。一般左不变度量未必双不变，不能删掉联络修正。

以上构造允许无限小跳，但范围仍是给定紧矩阵Lie群。反向从任意群值Lévy过程恢复局部特征，还需要新的必要性论证；它并不由给定三元组的构造自动获得。回到[正文](../chapters/40-stochastic-geometry.md#geometry-lie-jumps)。
