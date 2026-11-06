# T-GAUSSIAN: Hermite Polynomials, Wiener Chaos and Gaussian Banach Translations

Companion to [Chapter 39](../chapters/39-malliavin.md#noise-chaos). H is real separable Hilbert and W:H→L² is the isonormal family constructed in Chapter 23, with E W(h)W(k)=〈h,k〉. Our L² space is the completion of σ(W), without extra independent information. Coordinates ξⱼ=W(eⱼ) in an orthonormal basis are independent standard Gaussians, by Chapter 14’s finite-vector uniqueness.

## 1. Hermite Normalization and Orthogonality

<a id="gaussian-proof-hermite"></a>

Define probabilists’ Hₙ(x)=\((-1)^n\)e^{x²/2}(d/dx)ⁿe^{-x²/2}. Repeated Gaussian integration by parts has polynomial-times-Gaussian boundary terms vanishing at infinity and gives E[Hₙ(Z)f(Z)]=E f^{(n)}(Z), initially for polynomials and bounded smooth tests. Since the leading term is xⁿ, orthogonality is EHₙHₘ=n!1_{n=m}. Differentiate in x and t to verify the generating recurrence; Gaussian exponential moments dominate derivatives on bounded t-intervals.

\[ e^{tx-t^2/2}=\sum_{n=0}^\infty\frac{t^n}{n!}H_n(x),\quad H_n^\prime=nH_{n-1},\quad xH_n=H_{n+1}+nH_{n-1}. \]

For finite-support multi-indices α, H_α=∏H_{αⱼ}(ξⱼ) are orthogonal with squared norm α!=∏αⱼ!. The Gaussian exponential E_h=exp(W(h)−‖h‖²/2) has coefficients h^α/α!, whose squared norm sum is exp(‖h‖²)=E E_h². Its orthogonal partial sums therefore converge in L², not merely formally pointwise. Totality of finite-coordinate exponentials was actually proved by Laplace/Fourier methods in §§33.20–21. Equivalently apply that result to finite-coordinate conditional means and increase the coordinates. Thus the H_α form a complete orthogonal family in L²(σ(W)).

## 2. From Symmetric Tensors to Every Square-Integrable Output

<a id="gaussian-proof-chaos"></a>

Let \(H^{\odot n}\) be the symmetric closed subspace of the n-fold Hilbert tensor product. For |α|=n, symmetrize the basis tensor with repetitions α by averaging over n! permutations; its squared norm is α!/n!. Define Iₙ(e^{⊙α})=H_α. Orthogonality proves linear consistency and E Iₙ(f)Iₘ(g)=1_{n=m}n!〈f,g〉, extending uniquely by completeness to all symmetric tensors. The name “multiple integral” does not replace this construction.

\[ F=\sum_{n=0}^\infty I_n(f_n),\qquad E|F|^2=\sum_{n=0}^\infty n!\|f_n\|_{H^{\otimes n}}^2,\qquad I_0(f_0)=EF. \]

Group the complete Hermite expansion by total degree. Orthogonal Parseval gives the displayed L² convergence and unique fₙ. Iₙ is basis independent: on pure powers \(h^{\otimes n}\) for h≠0, the generating function gives Iₙ(\(h^{\otimes n}\))=‖h‖ⁿHₙ(W(h)/‖h‖). Polarization makes pure powers dense in symmetric tensors, so constructions from different bases agree. Orthogonal orders need not be independent: Z and Z²−1 are orthogonal but the latter is determined by the former.

## 3. The Expansion Really Contains Multiple Itô Integrals

<a id="gaussian-proof-multiple"></a>

Take H=L²[0,T], W(h)=∫h dB. Chapter 33’s exponential E_t(zh) satisfies E_t=1+z∫₀ᵗE_s h_s dB_s. Successive substitutions give ordered integrals. Repeated Chapter 31 isometry gives squared norm (∫h²)ⁿ/n! for order n, so the power series converges in L² locally uniformly in z and solves the equation. Isometry/Gronwall give uniqueness; compare coefficients with the Hermite generating function.

\[ I_n(f)=n!\int_{0<t_1<\cdots<t_n<T}f(t_1,\ldots,t_n)\,dB_{t_1}\cdots dB_{t_n},\quad f\in L^2_{\rm sym}([0,T]^n). \]

First obtain the identity for \(h^{\otimes n}\), then extend by polarization and isometry. Time diagonals have zero Lebesgue measure, so equal times require no artificial order. The tensor n! matches the ordered simplex. These are deterministic-kernel iterated Itô integrals already available, not integrals defined circularly by Malliavin divergence.

## 4. Derivative Weights and the Mehler Operator

<a id="gaussian-proof-number"></a>

Differentiate H_α directly on polynomial cylinders and apply Parseval to obtain the norm below. For general \(\mathbb D^{1,2}\) variables, Gaussian integration by parts identifies each Hermite coefficient of the derivative with a raised coefficient of F. Apply Parseval coordinatewise in H and use nonnegative Tonelli. Conversely, a finite weighted series makes derivatives of finite chaos sums Cauchy, and closability gives F∈\(\mathbb D^{1,2}\). The formula is not restricted to polynomials.

\[ E\|DF\|_H^2=\sum_{n\ge1} n\,n!\|f_n\|^2,\quad E\|D^kF\|^2=\sum_{n\ge k}\frac{n!}{(n-k)!}\,n!\|f_n\|^2. \]

The second identity follows by iteration; \(\mathbb D^{k,2}\) requires finiteness through order k. With an independent W′, define Mehler on cylinders by replacing W with \(e^{-t}\)W+√(1−\(e^{-2t}\))W′ and averaging. For 1≤p<∞, Jensen gives Lᵖ contraction and cylinder approximation gives strong continuity. The generating function yields TₜIₙ=\(e^{-nt}\)Iₙ. Its L² generator is L=-N, with N Iₙ=nIₙ and domain Σn²n!‖fₙ‖²<∞. On this domain δDF=NF by integration by parts and coefficient comparison. Here t attenuates noise coordinates, not the original Brownian motion’s physical time.

## 5. Integrability of Gaussian Banach Variables Is Not an Extra Assumption

<a id="gaussian-proof-fernique"></a>

Let B be separable Banach and X centered Radon Gaussian. A dense unit-sphere sequence and Hahn–Banach give countably many norming functionals ℓⱼ with ‖x‖=supⱼ|ℓⱼ(x)|. Closed-ball intersections with a countable positive margin, together with separability, show σ(ℓⱼ)=Borel(B). Finite linear readings therefore identify probability laws. For independent copies X,Y, (X+Y)/√2 and (X−Y)/√2 are independent copies of X, by finite Gaussian characteristic functions and this measure uniqueness.

\[ p(t)=P(\|X\|>t),\quad a=P(\|X\|\le r)>0,\quad a\,p(\sqrt2t+r)\le p(t)^2. \]

Indeed ‖X‖>√2t+r and ‖Y‖≤r force both rotated norms above t. Choose t₀ with p(t₀)<a and set tₙ₊₁=√2tₙ+r. Then p(tₙ)/a≤(p(t₀)/a)^{2ⁿ}, while tₙ≤C2^{n/2}. Comparing adjacent thresholds gives p(t)≤C₁exp(−c₁t²). Tail integration yields Eexp(η‖X‖²)<∞ for some η>0, hence all norm moments. Finite Gaussian rotation and this elementary estimate prove the Fernique version used here.

## 6. Extracting Cameron–Martin Directions in a Banach Space

<a id="gaussian-proof-banach"></a>

Let H be the closure of span{ℓ(X):ℓ∈B*} in L² and set W(h)=h. It is separable: a member orthogonal to every ℓⱼ(X) is Gaussian-independent of σ(X), yet is measurable there, so must be zero. Thus the countable readings have dense span. Define i(h)=E[XW(h)] as a Bochner integral. The preceding moments and Cauchy–Schwarz ensure existence and continuity: quantize X on countable B-grids by L²-convergent simple variables; the finite sums E[XₙW(h)] are Cauchy in B and define the integral, and ℓ(i(h))=〈ℓ(X),h〉. If i(h)=0, density gives h=0, so i embeds H in B.

\[ \frac{d\mu_{i(h)}}{d\mu}(x)=\exp\!\left(W(h)(x)-\frac12\|h\|_H^2\right),\quad \mu_{i(h)}=\mathcal L(X+i(h)),\qquad b\notin i(H)\Longrightarrow\mu_b\perp\mu. \]

For sufficiency the density has mean one and is strictly positive. Completing the square for finite linear readings shifts means by ℓ(i(h)) without changing covariance; Borel uniqueness identifies the translated law. Choose a measurable L²-limit version of W(h); equivalent measures make its null-set choice harmless. W(h) is not asserted to be a bounded continuous linear functional at every x.

For necessity try L_b(ℓ(X))=ℓ(b) on the span of the readings. If ill-defined, a zero-variance reading becomes a nonzero constant after translation and separates the laws. If well-defined and bounded, Hilbert Riesz gives h with ℓ(b)=〈ℓ(X),h〉=ℓ(i(h)) for every ℓ, hence b=i(h). Otherwise select finite linear readings gⱼ of L² norm one with L_b(gⱼ)≥2ʲ. Chebyshev and first Borel–Cantelli give gⱼ(X)/L_b(gⱼ)→0, whereas the same readings under X+b tend to one. Disjoint Borel limit events separate the laws. This proves the Banach translation criterion, not the entire equivalence theory for changed Gaussian covariances.

Derivative closability used in Section 4 is proved independently by Gaussian integration by parts in [T-MALLIAVIN](t-malliavin.md#malliavin-proof-closed), without chaos, so there is no circle. [Return to the chapter](../chapters/39-malliavin.md#noise-banach).
