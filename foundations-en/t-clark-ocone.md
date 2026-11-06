# T-CLARK-OCONE: Predictable Projection Identifies the Martingale Integrand

Companion to [Chapter 39](../chapters/39-malliavin.md#noise-clark). Fix finite T>0, H=L²[0,T], W(h)=∫h dB, the usual Brownian natural filtration, and \(F_T\)-measurable terminals. Chapter 33 already proves L² martingale representation and right-continuity; this formula is not used circularly to establish them.

## 1. Divergence of Adapted Processes Really Is the Itô Integral

<a id="clark-proof-adapted"></a>

Take U=G1_(a,b] with smooth \(\mathcal F_a\)-measurable cylinder G, whose Gaussian directions are supported on [0,a]. Adjointness gives δU=G(B_b−B_a)−〈DG,1_(a,b]〉, with zero correction. Sum finitely. Approximate general G∈L²(\(\mathcal F_a\)) by earlier Gaussian cylinders; independence and Itô isometry make both U and δU converge in L², and closedness extends the identity.

\[ U\ \hbox{predictable},\quad E\int_0^T U_t^2dt<\infty\quad\Longrightarrow\quad U\in\operatorname{Dom}\delta,\quad\delta U=\int_0^T U_t\,dB_t. \]

Chapter 31 gives density of simple predictable processes in this energy space; isometry and closedness prove the display. For F∈\(\mathbb D^{1,2}\), test first on the smooth core then pass in graph norm: E[F∫U dB]=E∫DₜF Uₜdt. An adapted U need not itself have a Malliavin derivative.

## 2. Timewise Conditional Means Need a Predictable Version

<a id="clark-proof-projection"></a>

First let F=f(W(h₁),…,W(hₙ)). Put Mᵢ(t)=∫₀ᵗhᵢdB and Qᵢⱼ(t)=∫ₜᵀhᵢhⱼds. Given \(\mathcal F_t\), future readings are independent centered Gaussian with covariance Q(t). Thus E[DₜF|\(\mathcal F_t\)]=Σᵢhᵢ(t)E_Z[∂ᵢf(M(t)+Q(t)^{1/2}Z)]. Q and its positive square root are continuous; Gaussian moments and polynomial growth make the bracket a continuous adapted process. Multiplication by deterministic Borel hᵢ(t) preserves predictability.

Conditional Jensen and Fubini give ‖K‖_{L²(dt⊗P)}≤‖DF‖_{L²(H)}. For \(F_n\)→F in \(\mathbb D^{1,2}\), K_n converge in the closed predictable L² subspace to K. A subsequence makes D\(F_n\)(t) and K_n(t) converge in L²(P) for almost every t; conditional contraction gives \(K_t\)=E[\(D_tF\)|\(\mathcal F_t\)] there. Thus the notation denotes a predictable dt⊗P equivalence class, not incompatible conditional versions chosen separately at every time.

## 3. Duality Uniquely Identifies the Representation Coefficient

<a id="clark-proof-formula"></a>

\[ F\in\mathbb D^{1,2}\quad\Longrightarrow\quad F=EF+\int_0^T E[D_tF\mid\mathcal F_t]\,dB_t. \]

Chapter 33 gives F−EF=∫H dB with predictable square-integrable H. For all such U, Section 1 and projection give E∫HU dt=E[F∫U dB]=E∫DF U dt=E∫KU dt. Set U=H−K to identify them dt⊗P-almost everywhere; isometry and Doob identify process versions. This adds to mere existence of representation: the coefficient is the noise sensitivity available before the next increment, not an arbitrary hindsight derivative.

For F=B_T², DₜF=2B_T while Kₜ=2Bₜ, giving F=T+∫2BₜdBₜ. This does not repeat Chapter 31’s quadratic-variation proof; it explains the projection of future sensitivity. If an independent coin Z is revealed only at T, its terminal conditional-mean martingale jumps there, whereas Brownian Itô integrals are continuous and cannot represent it. Z is also outside this page’s σ(W) terminal class. Information structure is a theorem assumption, not incidental wording. [Return to the chapter](../chapters/39-malliavin.md#noise-information).
