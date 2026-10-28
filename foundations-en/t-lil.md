# T-LIL: Uniform Oscillation and the Brownian Functional Iterated-Logarithm Law

This supplies the full technical proofs used in [Chapter 26](../chapters/26-brownian-properties.md#brownian-functional-lil). B is the constructed real standard Brownian motion. Only finite-dimensional Gaussian structure, the reflection maximum bound, Borel–Cantelli, L² completeness and C-space compactness are used. Schilder, general large deviations, Cameron–Martin and strong approximation are not invoked. Normalize only for T≥eᵉ, avoiding degeneration of log log T at the lower endpoint.

## 1. Why the energy ball is a compact set of paths

<a id="t-lil-energy"></a>

\[
\begin{gathered}
I(g)=\int_0^1|v_g(s)|^2\,ds\quad
 \left(g(t)=\int_0^t v_g(s)\,ds,\ v_g\in L^2([0,1])\right),\\
I(g)=\infty\quad\text{if no such }v_g\text{ exists},\qquad
K=\{g\in C([0,1]):I(g)\le1\}.
\end{gathered}
\]

First check that the definition is unambiguous. If v,w give the same integral path, ∫(v−w)u=0 for every step u. Density of steps in L² yields v=w almost everywhere. The representation also makes g absolutely continuous: on disjoint intervals of small total length, the sum of absolute increments is bounded by the integral of |v| over their union; use T-INTEGRAL’s absolute continuity of the integral. Only integral velocities are used, without invoking Lebesgue differentiation for pointwise derivatives.

For a finite partition π write Eπ(g)=\(\sum(\Delta g)^2/\Delta t\). An L² integral representation gives Eπ(g)≤I(g) by Cauchy–Schwarz on each cell. The converse needs proof. Suppose g is continuous, g(0)=0 and all partition energies are at most C. For a step function u=Σcᵢ1_(tᵢ₋₁,tᵢ] define ℓ(u)=Σcᵢ(g(tᵢ)−g(tᵢ₋₁)). Common refinement makes this independent of representation, and weighted Cauchy–Schwarz gives |ℓ(u)|≤√C‖u‖₂.

Steps are dense in L², so ℓ extends uniquely and continuously. Use the orthonormal basis eⱼ constructed from a countable dense family of steps in Chapter 23, and put aⱼ=ℓ(eⱼ). Testing Σⱼ≤ₙaⱼeⱼ gives Σⱼ≤ₙaⱼ²≤C. T-LP completeness supplies v=Σaⱼeⱼ∈L² and ℓ(u)=∫uv. Taking u=1_(0,t] yields g(t)=∫₀ᵗv, so g has the required integral representation and I(g)≤C. Thus bounded partition energy cannot hide a singular continuous component.

Consequently K is exactly characterized by g(0)=0 and all Eπ(g)≤1, hence is closed in C. Its elements satisfy |g(t)−g(s)|≤√|t−s| and ‖g‖∞≤1; Arzelà–Ascoli gives compactness. If Pₘg is the equal-mesh polygon, I(Pₘg)≤I(g) and its uniform error is at most 2/√m. First multiply by 1−η and then approximate finitely many vertex values by rationals, preserving energy strictly below one. This gives a countable dense rational polygon family 𝒟 in K, every member having energy<1.

## 2. The exact scale of the uniform modulus

<a id="t-lil-uniform-modulus"></a>

Fix 0<T<∞ and write w(B,δ)=sup_{s,t∈[0,T],|t−s|≤δ}|\(B_t\)−\(B_s\)|. Chapter 26 proves the reflection bound P(sup_{u≤h}|B_u|>x)≤4exp(−x²/(2h)). Also a standard normal Z satisfies P(Z>x)≥c x⁻¹e⁻ˣ²ᐟ² for x≥1: integrate its density only over [x,x+1/x] to obtain an absolute c>0.

Take geometric scales δₙ=q⁻ⁿ for fixed q>1, and a finer mesh a=δ/m, with m fixed afterward. For two points at distance≤δ, their left mesh points are at distance≤δ+2a. There are at most C_Tm²/δ relevant mesh pairs. Gaussian tails and a union bound at level (1+ε)√(2δlog(1/δ)) give the first term below. Moving each original time to its left mesh point adds two short-segment remainders; allow ε√(2δlog(1/δ))/2 for each. Reflection and a union bound give the second term.

\[
\begin{gathered}
P\!\left(w(B,\delta)>(1+2\varepsilon)\sqrt{2\delta\log(1/\delta)}\right)\\
\le C_{T,m}\delta^{(1+\varepsilon)^2/(1+2/m)-1}
   +C_{T,m}\delta^{m\varepsilon^2/4-1}.
\end{gathered}
\]

Choose m large enough that both powers are positive, sum along δₙ and apply the first Borel–Cantelli lemma. For δₙ₊₁<δ≤δₙ the modulus is monotone and the normalizing scale is increasing for small δ, giving an upper limit at most (1+2ε)√q. Intersect only over countable q↓1 and ε↓0 to obtain the bound one.

For the lower bound use ⌊T/δ⌋ disjoint increments of length δ. Divided by √δ they are independent standard normals. The probability that all absolute values stay below (1−ε)√(2log(1/δ)) is at most exp(−⌊T/δ⌋\(p_\delta\)), with \(p_\delta\)≥c[log(1/δ)]⁻¹ᐟ²δ^{(1−ε)²}. The exponent grows as a positive power when δ decreases, so failure probabilities are summable on geometric scales. Borel–Cantelli gives the eventual lower bound; adjacent scales and q↓1 give the full limit, not just a subsequence.

\[
\lim_{\delta\downarrow0}
\frac{w(B,\delta)}{\sqrt{2\delta\log(1/\delta)}}=1
\quad\text{almost surely, for each fixed }T>0.
\]

A countable intersection over positive rational T makes the property simultaneous on finite windows: for arbitrary positive T use a smaller rational window for the lower bound and a larger rational window for the upper bound. The log(1/δ) reflects a search among about 1/δ locations, unlike the log log(1/δ) for the fixed-origin LIL.

## 3. The path-energy upper bound at geometric times

<a id="t-lil-upper"></a>

\[
\begin{gathered}
Y_T(t)=\frac{B(Tt)}{\sqrt{2T\log\log T}},\quad 0\le t\le1,\ T\ge e^e,\\
T_n=q^n,\quad L_n=\log\log T_n=\log(n\log q).
\end{gathered}
\]

Fix ε>0 and choose δ>0 with √(1+δ)−1<ε/2. Let Pₘ be the m-cell polygon. If I(PₘY)≤1+δ and ‖Y−PₘY‖∞≤ε/2, divide PₘY by √(1+δ) to enter K, giving dist(Y,K)≤ε. The uniform change under this rescaling is at most √(1+δ)−1; this turns energy control into path-distance control.

Brownian scaling identifies \(Y_{T_n}\) in law with W/√(2Lₙ), where W is standard Brownian on [0,1]. The m standardized mesh increments are independent N(0,1), so I(PₘW) has the \(\chi_m^2\) law. A one-dimensional Gaussian integral gives E exp(θ\(\chi_m^2\)/2)=(1−θ)⁻ᵐᐟ². Choose 1/(1+δ)<θ<1; Markov yields a summable exponent for excessive energy.

\[
P\!\left(I(P_mY_{T_n})>1+\delta\right)
\le (1-\theta)^{-m/2}e^{-\theta(1+\delta)L_n}.
\]

The polygon error is at most twice the largest fluctuation from a cell’s left endpoint. Reflection and a union bound give the next estimate. Choose m with mε²/16>1. Both terms have the form C exp(−cLₙ), c>1, summable in n because Lₙ=log(nlog q). First Borel–Cantelli and a countable intersection over precisions give dist(\(Y_{T_n}\),K)→0 almost surely. The parameters δ, θ and m are fixed before taking the n limit.

\[
P\!\left(\|Y_{T_n}-P_mY_{T_n}\|_\infty>\varepsilon/2\right)
\le4m\exp\{-m\varepsilon^2L_n/16\}.
\]

## 4. Why geometric times alone are not enough

<a id="t-lil-all-times"></a>

Take T∈[\(T_{n-1}\),Tₙ] and a=T/Tₙ∈[1/q,1]. The following is an exact identity on the same path. Rather than crudely subtracting paths, use the stability of K under restriction and square-root rescaling.

\[
\begin{gathered}
Y_T(t)=\kappa_n(T)\frac{Y_{T_n}(at)}{\sqrt a},
\qquad \kappa_n(T)=\sqrt{\frac{L_n}{\log\log T}}\longrightarrow1
\quad\text{uniformly for }T\in[T_{n-1},T_n],\\
g\in K\quad\Longrightarrow\quad
I\!\left(\frac{g(a\,\cdot)}{\sqrt a}\right)
=\int_0^a|v_g(u)|^2\,du\le1.
\end{gathered}
\]

The transformed velocity can be checked directly: g(at)/√a has integral velocity √a v_g(at). Affine substitution gives the displayed identity, without first proving pointwise differentiability of g.

Choose gₙ∈K approximating \(Y_{T_n}\). The new distance to K is at most κₙ√q‖\(Y_{T_n}\)−gₙ‖∞+|κₙ−1|, uniformly tending to zero. Thus dist(\(Y_T\),K)→0 for all T→∞. Compactness of K gives asymptotic relative compactness. The family for T∈[eᵉ,M] is compact too because T↦\(Y_T\) is continuous in uniform norm. The whole stated family is relatively compact, and every cluster point as T→∞ belongs to K.

## 5. The probability of a prescribed polygonal shape

<a id="t-lil-tube"></a>

We need a direct Gaussian tube lower bound. Fix a polygon h starting at zero and a partition containing every corner. Let cₙ=√((1−a)/(2Lₙ)) with fixed 0<a<1. Require each mesh increment of W to lie within one of Δh/cₙ. Multiplying lower bounds for Gaussian densities on these boxes gives leading exponent I(h)/(2cₙ²), plus an error at most C/cₙ+C.

\[
P(\text{all increment boxes})
\ge C_0\exp\!\left\{-\frac{L_n I(h)}{1-a}-C_1\sqrt{L_n}-C_2\right\}.
\]

Endpoints alone do not suffice. Subtracting the line between endpoints in each cell gives a continuous Gaussian bridge, uncorrelated with every mesh increment and hence independent. Gaussian independence at dense coordinates extends to path independence through C’s coordinate Borel structure. Finitely many bridge norms are almost surely finite, so after multiplication by cₙ all bridge errors are below ε/2 with probability tending to one, independently of the increment-box event. Endpoint errors inside the boxes are at most mcₙ, eventually below ε/2. Hence

\[
P(\|c_nW-h\|_\infty<\varepsilon)
\ge C\exp\!\left\{-\frac{L_n I(h)}{1-a}-C'\sqrt{L_n}\right\}
\quad\text{for all sufficiently large }n.
\]

This is an explicit density estimate for one finite polygon and one fixed tube, not an unproved general path large-deviation principle. If I(h)/(1−a)<p<1, the right side is eventually bounded below by a constant times \(n^{-p}\). The strict gap absorbs the √Lₙ error.

## 6. How independent time blocks recover the energy ball

<a id="t-lil-lower"></a>

Take g from the countable family in Section 1, with I(g)<1. Let q be an integer and a=1/q. Standardized increments on [\(T_{n-1}\),Tₙ] give independent Brownian paths Wₙ on [0,1]. This uses only deterministic disjoint intervals, not a stopping-time theorem. Replace the original path by zero on [0,a] and retain only this block’s motion from zero afterward, obtaining Zₙ.

\[
\begin{gathered}
Z_n(t)=0\quad(t\le a),\qquad
Z_n(t)=c_nW_n\!\left(\frac{t-a}{1-a}\right)\quad(t\ge a),\\
h_a(u)=g(a+(1-a)u)-g(a),\qquad
\frac{I(h_a)}{1-a}=\int_a^1|v_g(s)|^2\,ds\le I(g)<1.
\end{gathered}
\]

The tube lower bound makes the sum of probabilities of ‖cₙWₙ−\(h_a\)‖∞<ε diverge. The events are independent, so the second Borel–Cantelli lemma makes them occur infinitely often. On them Zₙ differs from g by g(a) plus ε on the later segment, and by at most √a initially. Thus ‖Zₙ−g‖∞≤√a+ε.

The deleted past cannot simply be ignored. Section 4 and ‖K‖∞≤1 give sup_{u≤\(T_{n-1}\)}|B_u|≤(1+o(1))√(2\(T_{n-1}\)log log \(T_{n-1}\)). After the current normalization this is at most (1+o(1))√a, controlling both the old initial segment and the original starting value of the new block. Infinitely often, therefore, ‖\(Y_{T_n}\)−g‖∞≤2√a+ε+o(1).

Intersect only over g∈𝒟, integer q≥2 and rational ε>0. For any desired accuracy choose q large and ε small, then select increasing suitable n from the infinitely many occurrences. Every g∈𝒟 is a cluster point. The cluster set is closed: if cluster points gⱼ→g, choose Tⱼ>j with ‖\(Y_{T_j}\)−gⱼ‖<1/j. Hence it contains the closure K and, by the upper bound, equals K. No uncountable union of exceptional null sets was taken.

## 7. The result and its relation to the scalar LIL

<a id="t-lil-statement"></a>

\[
\text{Almost surely, }\{Y_T:T\ge e^e\}
\text{ is relatively compact in }C([0,1]),
\quad\operatorname{Cluster}_{T\to\infty}Y_T=K.
\]

Evaluation g↦g(1) maps K onto [−1,1], with endpoints realized by g(t)=±t; the result therefore contains the scalar LIL. The main chapter first proves the scalar version by shorter maximum and independent-block estimates to expose the log log scale. This companion identifies the energy constraint on the entire normalized shape. It is the real Brownian large-time functional LIL, not a general strong invariance principle for independent sums, a multivariate version or a near-zero functional theorem.

K contains absolutely continuous curves, but the original Brownian path has not become differentiable. These are cluster shapes from expanding time windows after additional iterated-logarithm compression. Nowhere differentiability on fixed windows and smooth possible macroscopic cluster shapes concern different questions.
