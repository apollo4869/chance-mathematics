# T-MASS-KERNELS: Mass Kernels, Smoothing, and Poissonization

Return to [Chapter 49](../chapters/49-random-measures.md#mass-smoothing). E and F are locally compact second-countable metric spaces. The parameter space Z only needs a measurable structure; randomization of probability kernels additionally uses the standard Borel target theorem of Chapter 10. All unsigned integration exchanges first use Tonelli for nonnegative quantities, without a hidden finite-mean assumption.

## 1. Joint Integration in the Parameter and the Measure

<a id="mass-kernel-measurable"></a>

If \(h:Z\times E\to[0,\infty]\) is jointly measurable, then \((z,\mu)\mapsto\int h(z,x)\mu(dx)\) is measurable on \(Z\times\mathcal M_+(E)\). For \(h=\mathbf1_A(z)\mathbf1_B(x)\) this is measurable evaluation, and finite nonnegative simple combinations follow. First restrict x to a compact exhaustion Kₘ. Since μ(Kₘ) is finite for every μ, complement subtraction is legitimate. A rectangular π–λ or functional monotone-class argument gives bounded jointly measurable h on each window; exhaustion, truncation, and monotone approximation then treat general nonnegative h. This establishes joint, rather than merely separate, measurability.

Let K be a probability kernel from Z×E to F. The measure \((\mu K_z)(A)=\int K(z,x,A)\mu(dx)\) is countably additive realization by realization by MCT. For a compact exhaustion Dₘ of F, let G consist of parameter-measure pairs satisfying every \(\mu K_z(D_m)<\infty\). This set is measurable. On G the output is locally finite Borel and hence Radon by T-RIESZ. Assigning zero outside G preserves measurability of every evaluation, yielding a measurable map into \(\mathcal M_+(F)\). If G has probability one in an application, the revision changes only a null set.

For fixed K and every nonnegative Borel f, one has \((\mu K)f=\mu(Kf)\), proved through indicators, simple functions, and MCT. Thus the mean \(\nu=\mathbb E\Xi\) satisfies \(\mathbb E[(\Xi K)f]=\nu(Kf)\), with infinity allowed. The Laplace functional obeys \(L_{\Xi K}(f)=\mathbb E e^{-\Xi(Kf)}\). Since Kf need not be continuous or compactly supported, the right side is an extended measurable reading of the original measure; vague convergence cannot be substituted without further proof.

## 2. Continuous Kernels and Fine Smoothing

<a id="mass-kernel-continuity"></a>

A sufficient deterministic continuity condition is \(Kf\in C_c(E)\) for every \(f\in C_c(F)\). Then \(\mu_n\xrightarrow v\mu\) directly gives \(\mu_nK\xrightarrow v\mu K\), but the outputs must first be locally finite. If K is a probability kernel and for each compact B⊂F there is compact A⊂E such that \(K(x,B)=0\) for x∉A, then \((\mu K)(B)\le\mu(A)\), ensuring local finiteness. Together with Feller continuity this gives the sufficient condition. Arbitrary kernels do not have it.

On \(\mathbb R^d\), take a nonnegative continuous compactly supported ρ of integral one and \(K_\varepsilon(x,dy)=\rho_\varepsilon(y-x)dy\). If f has support B and ρ is supported in a radius-r ball, then for ε≤1 all Kεf have support in the common compact set B plus that ball. Moreover, \(\sup_x|K_\varepsilon f(x)-f(x)|\le\sup_{|z|\le\varepsilon r,x}|f(x+z)-f(x)|\to0\), since a continuous compactly supported function is uniformly continuous on the whole space. Integration against any Radon μ gives vague convergence μKε→μ.

The density \(p_\varepsilon(y)=\int\rho_\varepsilon(y-x)\mu(dx)\) is finite and continuous on every compact y-window: only a common compact x-window contributes, ρ is uniformly continuous, and μ is finite there. Joint measurability of \((y,\mu)\mapsto p_\varepsilon(y)\) follows from the preceding section, giving a genuine random continuous density for random Ξ. The measures δ₀ and ρεdy differ by one on the singleton zero, proving that total variation convergence fails in general. If μ already has an L¹ density, L¹ continuity of translations gives a further L¹ approximation, but that conclusion is not extended to singular measures.

## 3. A Conditional Poissonization Construction

<a id="mass-poisson-approximation"></a>

Given random Radon Λ, use the Poisson probability kernel for evaluation-measurable intensities actually constructed in [T-POISSON-SPACE](t-poisson-space.md). The countable kernel construction of Chapter 8 generates \((\Lambda,N_1,N_2,\ldots)\) on an enlarged space, taking Nₙ conditionally independent with intensity nΛ. No unprovided extra randomness on the original space is assumed. Countably many n and compact windows unify the local-finiteness null sets. Define \(\widehat\Lambda_n=N_n/n\).

The finite-window Poisson second-moment isometry of Chapter 48 gives, for every real \(f\in C_c\), conditional mean Λf and conditional variance Λ(f²)/n. The quantity Λ(f²) is finite almost surely, though its expectation may be infinite. For A,δ>0,

\[ \mathbb P\{|\widehat\Lambda_nf-\Lambda f|>\delta\}\le\mathbb P\{\Lambda(f^2)>A\}+\frac{A}{n\delta^2}. \]

First let n tend to infinity and then A to infinity. Every coordinate converges in probability. Given ε, choose J with \(\sum_{j>J}2^{-j}<\varepsilon/2\), and apply a union bound to the first J coordinates. Then \(d_v(\widehat\Lambda_n,\Lambda)\to0\) in probability. This is convergence on one enlarged probability space and is stronger than separate marginal-law convergence; it does not claim realizationwise convergence of arbitrary independently chosen copies.

## 4. Continuity and Identification of the Cox Map

<a id="mass-cox-map"></a>

If \(\Lambda_n\Rightarrow\Lambda\) in the Radon vague space, the conditional Poisson outputs satisfy Cox(Λₙ)⇒Cox(Λ). For \(g=1-e^{-f}\in C_c^+\), the map \(\lambda\mapsto e^{-\lambda g}\) is bounded continuous, so every output Laplace functional converges. T-RANDOM-MEASURE-LIMITS, or the point version of Chapter 48, yields convergence in law. Finite means of the random intensities are unnecessary.

The Cox map is also injective on laws of directing measures. If two Cox laws agree, take any h∈\(C_c^+\) and \(0<s<1/\|h\|_\infty\), and substitute \(f=-\log(1-sh)\). The Laplace transforms of the two random variables Λh agree on a short interval. For finite nonnegative Y its Laplace transform has a Taylor expansion at every a>0 with radius at least a: the absolute term sum is dominated by \(e^{-(a-|u|)Y}\le1\), justifying exchange of series and expectation for |u|<a. Derivatives agree within the known interval. An interior point a extends equality to (0,2a); repetition extends it to all positive s. The previous companion’s uniqueness identifies Λh, and linear combinations and the countable family identify the entire random-measure law.
