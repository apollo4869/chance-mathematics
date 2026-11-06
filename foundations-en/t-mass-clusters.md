# T-MASS-CLUSTERS: Poisson Clusters, Random Line Mass, and Gamma Measures

Return to [Chapter 49](../chapters/49-random-measures.md#mass-clusters). Target E is LCSC metric; parent space S is standard Borel with σ-finite measure a; Q is a probability kernel from S to the Polish space of nonnegative Radon measures. Parents may have multiplicities, and daughter measures are conditionally independent for each occurrence. This page proves this precise scope without future Palm-tree criteria.

## 1. Marking into the Space of Measures

<a id="cluster-construction"></a>

The marking theorem of Chapter 48 gives a PRM N on S×\(\mathcal M_+(E)\) with intensity \(\lambda(dx,d\zeta)=a(dx)Q(x,d\zeta)\). Partition S into Borel pieces of finite a-mass, generate finitely many Poisson parents on each, mark each by a whole Radon realization, and concatenate countably many independent pieces. The evaluation structure uses the standard Borel space and does not require local compactness of S. Define the extended measure \(\Psi(A)=\int\zeta(A)N(dx,d\zeta)\), allowing infinity in this nonnegative integral.

The map ζ↦ζ(A) is measurable. For a fixed countable realization N, MCT preserves countable additivity in A when forming Ψ. T-MASS-KERNELS, or simple approximation, makes every Ψ(A) a random variable. For \(f\ge0\), Tonelli gives \(\Psi f=\int\zeta f\,dN\). The Poisson functional for all nonnegative measurable tests yields the formula in the chapter. Truncating parent pieces and ζf and then using MCT gives the same expression. Local finiteness has not been assumed.

## 2. Finiteness and the 0–∞ Criterion for Positive Poisson Integrals

<a id="cluster-finiteness"></a>

First prove a general lemma. Let λ be σ-finite, h≥0 measurable and finite λ-almost everywhere, and N be PRM(λ). Then \(Nh<\infty\) almost surely exactly when \(\lambda(1\wedge h)<\infty\); if this integral is infinite, Nh=∞ almost surely. If it is finite, \(\lambda\{h>1\}<\infty\), so this region contains finitely many N points, each with finite h. Also \(\mathbb E N(h\mathbf1_{h\le1})=\lambda(h\mathbf1_{h\le1})<\infty\), making the small-term sum finite almost surely. A λ-null set contains no points by the zero-intensity Poisson count.

Conversely use \((1-e^{-1})(1\wedge h)\le1-e^{-h}\le1\wedge h\). If the truncated integral diverges, the Poisson functional gives \(\mathbb E e^{-Nh}=e^{-\lambda(1-e^{-h})}=0\). The nonnegative exponential has zero expectation, so Nh=∞ almost surely. The assumption that h is finite almost everywhere matters: if h=∞ on a finite positive-intensity set, the probability of at least one such point lies strictly between zero and one, and the same 0–∞ conclusion fails.

For fixed compact B take \(h(x,\zeta)=\zeta(B)\), which is finite everywhere, obtaining the chapter’s criterion. If it holds for a compact exhaustion Bₘ, Ψ is locally finite on one common full-probability set, and T-RIESZ gives regularity, so it is a random Radon measure. Failure in any window forces Ψ(Bₘ)=∞ almost surely and excludes that state space. This is a Poisson-structure criterion for specified compact windows, not a universal zero–one law for every random Radon measure.

## 3. Means, Truncation Limits, and a Non-Cox Example

<a id="cluster-laws"></a>

Campbell and Tonelli give \(\mathbb E\Psi f=\int\!\int\zeta f\,Q(x,d\zeta)a(dx)\), without a finiteness requirement. Restricting parents to increasing finite-intensity pieces gives sums Ψₙ increasing setwise to Ψ. Under the local-finiteness criterion, Ψₙf↑Ψf<∞ for every nonnegative compactly supported f. Splitting real f into positive and negative parts gives realizationwise vague convergence. One may also truncate each ζ to increasing compact windows; MCT and common countable tests give the same conclusion. This argument does not cover arbitrary signed or nonmonotone truncations.

Finite mean is stronger than almost-sure finiteness. For example, take a Poisson(1) total parent count and daughter Zδ₀, where Z is positive and finite almost surely with infinite mean. The criterion’s integral is at most one, so the output is Radon while its mean singleton mass is infinite. If every daughter is instead 2δ₀, the count is 2N. Were it Cox, its singleton count would be mixed Poisson. A positive probability of nonzero count would force positive directing singleton intensity Λ₀ with positive probability, yielding P{count 1}=E[Λ₀exp(−Λ₀)]>0, a contradiction. Local finiteness makes Λ₀ finite almost surely.

There is a precise sufficient condition in the other direction. Suppose each daughter point measure is conditionally PRM(Λᵢ) given its random Radon intensity, daughter point measures are independent conditional on all parent information and intensities, and Λ=ΣΛᵢ is locally finite almost surely. Multiplying conditional Laplace functionals gives PRM(Λ), so the output is Cox. Multiply finitely first, then take monotone limits; the tower property permits conditioning only on Λ. The parent process itself need not be the directing measure.

## 4. Measurability, Local Finiteness, and Mean of Line Mass

<a id="cluster-lines"></a>

Take S=[0,π)×R and \(a(d\vartheta,dr)=(c/\pi)d\vartheta dr\), c>0. Put \(n_\vartheta=(\cos\vartheta,\sin\vartheta)\), \(v_\vartheta=(-\sin\vartheta,\cos\vartheta)\), and define \(\zeta_{\vartheta,r}f=\int_{\mathbb R}f(rn_\vartheta+tv_\vartheta)dt\). Joint continuity in the parameters and t, followed by nonnegative Tonelli, gives measurable Borel evaluations; continuous tests can also be integrated directly. For a compact window inside a radius-R disk, only lines with |r|≤R contribute. This parameter set has a-mass 2cR, and each line contributes at most 2R length. The cluster finiteness criterion holds.

For fixed ϑ, the map \((r,t)\mapsto rn_\vartheta+tv_\vartheta\) is orthogonal with absolute Jacobian one. Hence \(\mathbb E\Lambda f=c\int f(x)dx\) for every nonnegative f. The PRM on the σ-finite parameter space is countable almost surely. Each line has zero planar Lebesgue measure, and their countable union still does; every Λ realization is supported there. Λ is nonzero almost surely: the parameter space has infinite intensity, so N is nonempty almost surely, and every line has nonzero local length. Singular realizations with a diffuse mean are a rigorous distinction, independent of a picture.

Conditional on Λ, construct PRM(ρΛ), ρ>0. Local finiteness follows from Λ. With \(h(\vartheta,r)=\rho\int_{\ell_{\vartheta,r}}(1-e^{-f})d\mathcal H^1\), conditional Poissonization followed by the parent-line Poisson functional gives \(L(f)=\exp\{-\int(1-e^{-h(\vartheta,r)})a(d\vartheta,dr)\}\). For nonzero f this generally differs from the Poisson functional with mean intensity ρc dx: since 1−e⁻ʰ<h for h>0, the exponent has strictly smaller absolute value. This directly proves that the line-based Cox process is not ordinary planar Poisson.

## 5. Gamma Mass and Dirichlet Normalization

<a id="cluster-gamma"></a>

Let H be a Radon probability on E and θ>0. On E×(0,∞) take the σ-finite intensity \(\lambda(dx,ds)=\theta H(dx)s^{-1}e^{-s}ds\). Countably many small-s strips each have finite intensity, so the construction of Chapter 48 applies. Use the deterministic mark \(\zeta_{x,s}=s\delta_x\), jointly measurable through evaluations \(s\mathbf1_A(x)\), and define \(\Gamma=\int s\delta_xN(dx,ds)\). The total-mass criterion is

\[ \int(1\wedge s)\lambda(dx,ds)=\theta\left(\int_0^1e^{-s}ds+\int_1^\infty s^{-1}e^{-s}ds\right)<\infty. \]

Thus Γ(E)<∞ almost surely. For a≥0, use \(1-e^{-as}=\int_0^a s e^{-us}du\) and Tonelli to obtain \(\int_0^\infty(1-e^{-as})s^{-1}e^{-s}ds=\int_0^a(1+u)^{-1}du=\log(1+a)\). The Poisson functional gives the Gamma functional in the chapter. For simple tests \(\sum_jt_j\mathbf1_{A_j}\) with disjoint Aⱼ, the functional factors, so Γ(Aⱼ) are independent with transforms \((1+t_j)^{-\theta H(A_j)}\). Integrating the Gamma density for positive shape gives this transform, and Chapter 13’s uniqueness identifies the law; zero shape means identically zero.

Taking A=E gives \(\mathbb P\{\Gamma(E)=0\}=\lim_{t\to\infty}(1+t)^{-\theta}=0\), so normalization is legitimate and evaluation-measurable. On each finite partition, the positive-shape Gamma masses are independent. The Gamma normalization Jacobian proved in Chapter 44 makes \((\Gamma(A_j)/\Gamma(E))_j\) Dirichlet(θH(Aⱼ)); delete zero-shape coordinates and restore them as zeros afterward. Consistency and evaluation uniqueness identify the Dirichlet-process law of the random probability. No normalization claim is made for infinite total base mass; total-mass conditions would need rechecking.
