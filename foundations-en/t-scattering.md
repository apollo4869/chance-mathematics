# T-SCATTERING: Independent Displacements, Dissipation, and Cox Limits

Return to [Chapter 49](../chapters/49-random-measures.md#mass-scattering). Input E and target F are LCSC metric spaces. Ξₙ are locally finite integer point measures, and Kₙ are deterministic subprobability kernels from E to F; missing mass is sent to a cemetery point. Probability kernels are a special case, while the subprobability version also includes thinning. Points move independently conditional on the input; input points need not be independent. No Palm or Mecke formula is used.

## 1. Measurable Conditional Construction and Infinite Products

<a id="scattering-construction"></a>

T-POINT-MEASURES enumerates every occurrence of Ξ, including multiplicities. A measurable randomization function from Chapter 10 and countably many independent uniforms generate the Yᵢ, with cemetery draws omitted. Each evaluation η(A) is a measurable countable sum of indicators. If \(\Lambda(B)=\sum_iK(x_i,B)<\infty\) for a target compact exhaustion, finite conditional expectation makes η(B) finite almost surely. Countably many B unify the null sets and give a random Radon point measure. T-MASS-KERNELS makes Λ itself a measurable random measure.

Conditional on the input, the first r terms have Laplace functional \(\prod_{i\le r}(1-a_i)\), where \(a_i=K(1-e^{-f})(x_i)\). Partial counts increase, and their exponentials decrease boundedly, so conditional dominated convergence gives the infinite product formula. If f is supported in B, then \(\sum_i a_i\le\Lambda(B)<\infty\). A logarithmic expansion of an infinite product has not been assumed without justification.

## 2. A Total Variation Coupling for a Whole Window

<a id="scattering-coupling"></a>

Fix B with m=Λ(B)<∞. Source i has a Bernoulli(qᵢ) window count, \(q_i=K(x_i,B)\). Maximally couple it to Poisson(qᵢ), using \(d_{TV}(\operatorname{Bern}(q_i),\operatorname{Poi}(q_i))=q_i(1-e^{-q_i})\le q_i^2\). If both counts are one, share a point drawn from K(xᵢ,·∩B)/qᵢ; the remaining Poisson-side points are independent draws from the same conditional law. For qᵢ=0 both are empty. The same error bound therefore holds for the whole one-source point measure.

Couple sources independently. The mismatch probability for the first r superposed sources is at most \(\sum_{i\le r}q_i^2\). The Poisson side has intensity \(\sum_{i\le r}K(x_i,\cdot\cap B)\) by the independent superposition theorem of Chapter 48. The probability of any omitted tail point on either side is at most \(\sum_{i>r}q_i\to0\), so passage to r→∞ is legitimate and gives

\[ d_{\rm TV}(\mathcal L(\eta|_B\mid\Xi),\operatorname{PRM}(\Lambda|_B))\le1\wedge\sum_iq_i^2\le1\wedge\{(\sup_iq_i)\Lambda(B)\}. \]

Total variation here is the supremum of event-probability differences, without an extra factor of two. The conditional kernels are measurable, so integrating bounds every unconditional event difference by the expected right side. No common maximal coupling across n is required, and coupling is not asserted to be the original systems’ actual common driver.

A measurable parameter coupling can be constructed explicitly. At count k take the minimum of the two probability masses as overlap. Select a shared count with the total overlap probability; otherwise draw from the two residual distributions, using fixed conventions when overlap is zero or one. All masses are continuous or measurable functions of q, making inverse-CDF sampling jointly measurable. Divide the conditional location kernel by q, assign a cemetery value at q=0, and use Chapter 10 kernel randomization. The countable product of Chapter 8 handles all sources. Thus the conditional comparison genuinely uses measurable probability kernels.

## 3. Equivalence of Smoothing and Scattering Tightness

<a id="scattering-tightness"></a>

For any family, assume every Λₙ is locally finite. Conditional on the input, ηₙ(B) is a summable independent Bernoulli sum with mean mₙ=Λₙ(B) and variance at most mₙ. L² convergence of finite centered partial sums establishes the variance formula rather than bypassing an infinite-sum exchange. If mₙ are uniformly tight, then \(\mathbb P\{\eta_n(B)>R\}\le\mathbb P\{m_n>A\}+A/R\). Choosing A and then R gives tight window counts.

Conversely, if mₙ>max(2R,8), Chebyshev gives \(\mathbb P\{\eta_n(B)\le R\mid\Xi_n\}\le4/m_n<1/2\). Hence \(\mathbb P\{m_n>\max(2R,8)\}\le2\mathbb P\{\eta_n(B)>R\}\). Tight scattered window counts imply tight smoothed window masses. T-RANDOM-MEASURE-LIMITS and its point version in Chapter 48 convert compact-window conditions into tightness of laws. This equivalence does not require dissipativity; dissipativity is needed for the Poisson approximation.

## 4. The Dissipative Cox Criterion and Both Limit Directions

<a id="scattering-cox"></a>

Assume further that \(\epsilon_n(B)=\sup_xK_n(x,B)\to0\) for every compact B. If the Λₙ laws are tight, the expected coupling bound tends to zero: on mₙ≤A it is at most εₙA, and on the complement at most P(mₙ>A). Choose A and then n. Thus ηₙ and Cox(Λₙ) have asymptotically equal laws in total variation on every compact window. Their Laplace functionals consequently differ by a vanishing amount for f supported in B.

If \(\Lambda_n\Rightarrow\Lambda\), Cox continuity from T-MASS-KERNELS and the comparison give ηₙ⇒Cox(Λ). Conversely, if ηₙ⇒η, the preceding section first gives tightness of Λₙ. Along any convergent subsequence Λₙⱼ⇒Λ′, the forward result forces η to have law Cox(Λ′). T-MASS-KERNELS fully proves injectivity of the Cox map on directing-measure laws, so all subsequential directing limits agree. Prokhorov gives convergence of the whole Λₙ sequence, and η must be Cox. Injectivity also shows that the limit η is PRM(μ) exactly when its directing limit is the deterministic measure μ.

The hypotheses are locally finite output intensities, conditional independence, dissipativity in target windows, and tight smoothed laws. Inputs need not be simple, uniform, Poisson, or of finite mean. Without dissipativity, the identity kernel preserves a deterministic lattice on both sides and produces no Poisson approximation. Without conditional independence, a common large displacement of the entire lattice retains rigidity.

## 5. Arbitrary Thinning Divisibility Identifies Cox Laws

<a id="scattering-thinning"></a>

A direct characterization follows: a locally finite point process η is Cox exactly when, for every positive integer n, some locally finite point process Ξₙ has an independent 1/n-thinning with law η. Different n need not share a space. For sufficiency use Kₙ(x,dy)=δₓ(dy)/n, so εₙ(B)≤1/n and Λₙ=Ξₙ/n. Output laws are constantly η and hence tight. The preceding section supplies a directing limit and makes η Cox. For necessity, if η=Cox(Λ), choose Ξₙ=Cox(nΛ) and apply the independent thinning theorem of Chapter 48 conditional on Λ; the output is Cox(Λ).

The criterion requires existence of a larger process to thin; it does not say that thinning a fixed process preserves its law. The latter typically fails for positive finite-window counts. Nor does this criterion classify every reinforced or clustered process as Cox.

## 6. A Complete Stationary Averaging Proof on the Line

<a id="scattering-averaging"></a>

Let Ξ be a stationary random Radon measure on the line with \(c=\mathbb E\Xi[0,1)<\infty\). On the canonical measure space the action \(\theta_h\mu(A)=\mu(A+h)\) is jointly measurable. For f∈Cc, \((h,x)\mapsto f(x-h)\) is jointly continuous, T-MASS-KERNELS gives joint integrals, and countable coordinates determine the σ-algebra. The mean measure is translation invariant and locally finite. Additivity on intervals and monotone approximation from rational lengths give \(\mathbb E\Xi(dx)=c\,dx\). Fixed locations therefore have no mean atom and no atom almost surely; fixed endpoint conventions do not affect the following statements.

Put Y(μ)=μ[0,1) and T=θ₁. Birkhoff and its L¹ convergence in Chapter 41 make forward averages converge to \(C=\mathbb E[Y\mid\mathcal I_T]\) in L¹ and almost surely. T is invertible; backward averages have the same conditional expectation because \(\mathcal I_{T^{-1}}=\mathcal I_T\). Combining them gives \(\Xi[-N,N)/(2N)\to C\) in L¹. For real R put N=⌊R⌋. The boundary difference has expectation at most 2c, and the denominator correction vanishes, so the same L¹ limit holds.

For every fixed h, the symmetric difference of the two length-2R windows has length at most 2|h|, giving \(\|C\circ\theta_h-C\|_1=0\). This is invariance modulo P for each h; no single exceptional set is claimed to give pointwise equality for uncountably many h. Let \(\mathcal I\) contain events invariant modulo P under every h. Then C has an \(\mathcal I\)-measurable version. For A∈I, measure preservation and invariance yield \(\mathbb E[\mathbf1_AC]=\mathbb E[\mathbf1_AY]\), hence \(C=\mathbb E[Y\mid\mathcal I]\). Under ergodicity for all translations, I is trivial and C=c.

Let \(K_R(x,dy)=\mathbf1_{\{|y-x|\le R\}}dy/(2R)\). Tonelli gives \(\Xi K_R(dy)=q_R(y)dy\), and the translated-window bound gives \(q_R(y)\to C\) in L¹ for fixed y. For f∈Cc, \(\mathbb E|\Xi K_Rf-C\int f|\le\int|f(y)|\mathbb E|q_R(y)-C|dy\to0\), dominated by 2c|f|. Countable tests and the metric tail yield \(\Xi K_R\to Cdy\) vaguely in probability. If Ξ is a point process, \(\sup_xK_R(x,B)\le|B|/(2R)\), and the dissipative criterion gives independent scattering⇒Cox(Cdy). The smoothed limit lives on the original canonical space, but only a distributional limit is claimed for scattering.

## 7. Lattice Examples and the Boundary of Independence

<a id="scattering-examples"></a>

For \(\Xi=\sum_{k\in\mathbb Z}\delta_{k+U}\), every [y−R,y+R] window count differs from 2R by at most two. Thus qR converges uniformly in y to one. Dissipative scattering converges to PRM(dy), without an extra ergodicity argument. If spacing is randomly a∈{1,1/2}, with phase conditionally uniform on [0,a), the window density tends to 1/a and the limit is Cox((1/a)dy). Its disjoint-window count covariance, when second moments are finite, is Var(1/a) times the two lengths, rather than Poisson independence.

If all lattice points share one displacement, however broad its distribution, the phase modulo one remains uniform and the configuration law remains a random-phase lattice. A window of length less than one contains at most one point, whereas a Poisson limit has positive probability of at least two. The laws differ. This identifies the missing conditional independence without relying on a visual impression of regularity.
