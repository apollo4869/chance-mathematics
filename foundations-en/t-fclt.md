# T-FCLT: Empirical Curves, Inverse Time and Functional Limits

This companion starts from the finite-second-moment iid polygonal Donsker theorem proved in [Chapter 25](../chapters/25-donsker.md#donsker-theorem). It establishes the uniform empirical process, its general-CDF version on compact intervals, and a finite-variance renewal functional limit for positive waits. No unproved general empirical-class theory, Brownian embedding or Palm theory is used.

## 1. An exact finite-sample identity for exponential spacings

<a id="t-fclt-spacings"></a>

Let N=n+1 and let E₁,…,E_N be independent with density e⁻ˣ1_{x>0}, and partial sums Rₖ. On the positive orthant use the smooth bijection r=R_N and uᵢ=Rᵢ/r, i=1,…,n. The new domain is r>0 and 0<u₁<⋯<uₙ<1. With u₀=0 and u_N=1 the inverse is Eᵢ=r(uᵢ−uᵢ₋₁).

Check the Jacobian in two stages. From (r,u₁,…,uₙ) to (r,E₁,…,Eₙ), the difference matrix at fixed r is lower triangular with diagonal r, giving determinant rⁿ. Replacing r by E_N=r−Σᵢ≤ₙEᵢ has absolute determinant one. The joint density is therefore e⁻ʳrⁿ. Tonelli permits integration in r first. Integration by parts inductively gives ∫₀∞e⁻ʳrⁿdr=n!; the boundary term vanishes because exponential decay dominates every fixed polynomial.

\[
f_{u_1,\ldots,u_n}(u_1,\ldots,u_n)
 =n!\,\mathbf1_{\{0<u_1<\cdots<u_n<1\}}.
\]

An unordered iid uniform vector has joint density one and no ties. Each strict ordering corresponds to a coordinate permutation, so the ordered density is n!. This proves the joint distributional identity, not just a marginal spacing formula. Each n may be represented on one exponential sequence, without claiming to preserve the original uniform samples’ dependence across n.

## 2. Why normalization of total length produces a bridge

<a id="t-fclt-bridge"></a>

Let H_N be the √N-normalized polygon for Eᵢ−1, and let q_N interpolate (k/N,Rₖ/R_N). Every Eᵢ is positive almost surely; a countable intersection makes all q_N increasing homeomorphisms of [0,1] simultaneously. Set q_N=id on the null exception. Finite-vector interpolation is measurable, and so is its inverse: on the positive-spacing domain the nodes and piecewise-linear inverses vary continuously with the parameters.

\[
q_N(t)=\frac{Nt+\sqrt N\,H_N(t)}{N+\sqrt N\,H_N(1)},\qquad
 v_N(t):=\sqrt N(q_N(t)-t)
 =\frac{H_N(t)-tH_N(1)}{1+H_N(1)/\sqrt N}.
\]

Exponential variables have mean and variance one, so Donsker gives H_N⇒B in C([0,1]). Their uniform norms are tight and the denominator tends to one in probability. Set G_N=H_N−tH_N(1). A fixed continuous linear map gives G_N⇒B°, and ‖v_N−G_N‖∞≤2‖H_N‖∞|d_N−1|/|d_N|, where d_N is the denominator. Restricting first to a high-probability bounded-norm event and |d_N|≥1/2 proves that the difference vanishes in probability. This checks the N-dependent denominator rather than silently applying a changing-map theorem.

Thus v_N⇒B° and is C-tight. The process B°(t)=B(t)−tB(1), with covariance min(s,t)−st, is the bridge already constructed in Chapter 23, not a candidate defined only at finitely many times.

## 3. Inverse fluctuations require more than a continuity slogan

<a id="t-fclt-inverse"></a>

For any increasing continuous homeomorphism q with inverse r, substituting u=q(t) gives ‖r−id‖∞=‖q−id‖∞. In the random setting above, the right side is ‖v_N‖∞/√N and tends to zero in probability by C-tightness. Substituting into q_N(r_N(t))=t gives the exact relation:

\[
\sqrt N(r_N(t)-t)=-v_N(r_N(t)),\qquad
 \|\sqrt N(r_N-\mathrm{id})+v_N\|_\infty
 \le w(v_N,\|r_N-\mathrm{id}\|_\infty).
\]

The random modulus on the right really vanishes. For fixed δ>0, its probability of exceeding ε is at most P(‖r_N−id‖∞>δ)+P(w(v_N,δ)>ε). First take the upper limit in N, removing the first term, and then let δ decrease to zero; C-tightness removes the second. No independence between r_N and v_N is required; they come from the same data. The stability result yields √N(r_N−id)⇒−B° in C.

## 4. Every endpoint and error for the empirical CDF

<a id="t-fclt-empirical"></a>

In the exponential realization let Gₙ be the empirical CDF of R₁/R_N,…,Rₙ/R_N. For t∈[Rₖ/R_N,Rₖ₊₁/R_N), k=0,…,n, one has Gₙ(t)=k/n and r_N(t) between k/N and (k+1)/N. The endpoint errors are k/(nN) and (n−k)/(nN), both at most 1/N; at t=1 both values are one. This gives a deterministic uniform bound.

\[
\|G_n-r_N\|_\infty\le\frac1N,\qquad
 \left\|\sqrt n(G_n-\mathrm{id})-\sqrt n(r_N-\mathrm{id})\right\|_\infty
 \le\frac{\sqrt n}{n+1}\longrightarrow0.
\]

Since √(n/N)→1, the previous section and tight norms give √n(r_N−id)⇒−B° in C. The continuous inclusion C→D, the uniform error and Chapter 24’s stability result yield αₙ⇒−B° in D with J₁. Centered Gaussian symmetry identifies −B° in law with B°. The empirical CDF is a D-valued random element: each threshold count is measurable, D’s Borel σ-algebra is coordinate-generated, and its paths are right-continuous finite steps.

The joint distributional identity in Section 1 passes through the Borel map from ordered points to the CDF, so the entire D-valued laws agree and the conclusion applies to the original iid uniform sample. The maximum absolute error follows directly from the continuous approximation: the difference of suprema is bounded by the uniform error, giving √n‖Gₙ−id‖∞⇒‖B°‖∞. No unverified measurability assertion in nonseparable ℓ∞ is needed.

## 5. A general CDF, including atoms

<a id="t-fclt-general-cdf"></a>

Let F be any real CDF. For u∈(0,1), Q_F(u)=inf{x:F(x)≥u} is finite and right continuity gives F(Q_F(u))≥u by approaching the infimum from above through points with F≥u. Hence Q_F(u)≤x if and only if u≤F(x). Setting Yᵢ=Q_F(Uᵢ) gives an iid F-sample and the exact indicator identity.

Fix finite a<b. The map Φ_F:C([0,1])→D([a,b]), Φ_F(g)(x)=g(F(x)), produces right-continuous paths with left limit g(F(x−)). Moreover ‖Φ_F(g)−Φ_F(h)‖∞≤‖g−h‖∞, so the map is continuous into J₁ and Borel. Apply Φ_F to the continuous approximating processes from Section 4; their error remains bounded by the original uniform error, proving:

\[
\begin{gathered}
\sqrt n(F_n-F)\Rightarrow B^\circ\circ F\quad\text{in }D([a,b]),\\
 \operatorname{Cov}(B^\circ(F(x)),B^\circ(F(y)))
 =F(\min(x,y))-F(x)F(y).
\end{gathered}
\]

Atoms of F produce jumps at fixed locations. They do not obstruct this proof: continuity is needed in the input g, not imposed on F. Weighted uniform norms on the entire real line, general index classes and multivariate empirical processes are outside the proved scope.

## 6. The inverse limit for renewal counts

<a id="t-fclt-renewal"></a>

Let τᵢ>0 be iid with mean μ>0 and variance σ²∈(0,∞). Set R₀=0, Rₖ=Σᵢ≤ₖτᵢ and N(t)=max{k:Rₖ≤t}. The integrable strong law of Chapter 12 gives Rₖ/k→μ almost surely, hence Rₖ→∞ and N(t) is finite: the construction is nonexplosive. The count is a right-continuous staircase and {N(t)≥k}={Rₖ≤t} is measurable, so it is D-valued.

First prove the inverse strong law. For fixed t>0 and 0<ε<t/μ take kₙ±=⌊n(t/μ±ε)⌋. The strong law gives R_{kₙ±}/n→t±με. Eventually kₙ⁻≤N(nt)<kₙ⁺, and letting ε decrease to zero gives N(nt)/n→t/μ. At t=0 positivity gives N(0)=0. On the same probability-one strong-law event, these conclusions can first be made simultaneous over countably many grid times and rational ε. Apply this at finitely many grid times; monotonicity of N traps values between grid points while the continuous linear limit changes by at most the mesh divided by μ. Refining the mesh gives uniform convergence on compact windows.

\[
\sup_{0\le t\le T}\left|\frac{N(nt)}n-\frac t\mu\right|\longrightarrow0
 \quad\text{almost surely}.
\]

Next control the random index. Choose C>T/μ. If R_⌊Cn⌋>nT then N(nT)+1≤⌊Cn⌋; the complementary probability vanishes by the strong law. On this high-probability event, both age A(nt)=nt−R_{N(nt)} and residual life V(nt)=R_{N(nt)+1}−nt are bounded by the largest of the first ⌊Cn⌋ waits. A finite second moment gives:

\[
P\!\left(\max_{j\le\lfloor Cn\rfloor}\tau_j>\varepsilon\sqrt n\right)
 \le\frac C{\varepsilon^2}E[\tau_1^2\mathbf1_{\{\tau_1>\varepsilon\sqrt n\}}]\longrightarrow0,
 \qquad
 \frac1{\sqrt n}\sup_{t\le T}\{A(nt)\vee V(nt)\}\xrightarrow P0.
\]

Put Hₙ(s)=(R_⌊ns⌋−μ⌊ns⌋)/√n and let Ḣₙ be its polygon. The main chapter gives Ḣₙ⇒σB in C([0,C]) and ‖Hₙ−Ḣₙ‖_[0,C]→0 in probability. Substituting k=N(nt) into the arrival-time definition gives the exact identity below. The remainder is the age just controlled, not an arbitrarily discarded rounding term.

\[
Z_n(t)=\frac{N(nt)-nt/\mu}{\sqrt n},\qquad
 \mu Z_n(t)=-H_n\!\left(\frac{N(nt)}n\right)-\frac{A(nt)}{\sqrt n}.
\]

On the high-probability event where random times stay in [0,C], the difference of the two readings is bounded by the step/polygon error plus w(Ḣₙ, sup_{t≤T}|N(nt)/n−t/μ|). For fixed δ, its probability is bounded by the inverse-law bad event and the common-modulus bad event. Taking n to infinity and then δ to zero removes both. No independence between counts and waiting sums is required.

\[
\left\|Z_n+\frac1\mu\bar H_n(\,\cdot\,/\mu)\right\|_{[0,T]}
 \xrightarrow P0,\qquad
 Z_n\Rightarrow-\frac{\sigma}{\mu}B(\,\cdot\,/\mu)
 \quad\text{in }D([0,T]).
\]

Fixed time rescaling and scalar multiplication are continuous on C; stability from uniform error to J₁ gives the conclusion. Jointly with the waiting sums the construction retains their negatively related limit. For the count path alone, √μ B(t/μ) is standard Brownian motion and its negative has the same law, so the limit may be written as σμ⁻³ᐟ² times another standard Brownian motion. This is a distributional identity, not a samplewise identity with the original waiting-sum limit.

This proof needs no nonarithmetic assumption, Blackwell theorem or key renewal theorem: positive waits, the integrable strong law and finite variance suffice. The argument needs no local renewal-measure selection or key renewal limit, only independent sums, inverse clocks and a common modulus. With variance zero, waits equal μ, the count error is at most one and √n-fluctuations vanish. Heavy-tailed renewal, unscaled age and residual life, and stationary observation remain distinct theories.
