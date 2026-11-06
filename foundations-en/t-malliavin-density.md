# T-MALLIAVIN-DENSITY: Absolute Continuity, Smoothness and an SDE Application

Companion to [Chapter 39](../chapters/39-malliavin.md#noise-covariance). We first prove a scalar \(\mathbb D^{1,2}\) absolute-continuity criterion, then a higher-Sobolev vector criterion and smooth densities under inverse-moment assumptions. These are different theorems: the stronger vector assumption is not presented as the weakest \(\mathbb D^{1,2}\) version, and no general Hörmander theorem is claimed.

## 1. How a Scalar First Derivative Excludes Singular Mass

<a id="density-proof-scalar"></a>

First consider f=c+∫g with integrable g. It is absolutely continuous and differentiable almost everywhere by Chapter 38’s Lebesgue differentiation theorem. For a Lebesgue-null N⊂R, f′=0 almost everywhere on f^{-1}(N). At points where f is differentiable and |f′|>1/k, some n ensures |f(y)−f(x)|≥|y−x|/(2k) whenever |y−x|<1/n. Restrict these points further to intervals shorter than 1/n. The inverse map is 2k-Lipschitz there. Lipschitz maps preserve null sets, by interval coverings of arbitrarily small total length. Thus the relevant preimage is null. A countable union over k,n and intervals leaves only zero-derivative or nondifferentiability points; the latter are null for absolutely continuous f.

Let F∈\(\mathbb D^{1,2}\). Fix Gaussian coordinate ξⱼ and call the remaining coordinates z. Choose cylinder approximants with summable squared L² errors for Fₙ and DⱼFₙ. Fubini gives convergence in L²(γ₁) for almost every z. On compact intervals Gaussian density is bounded below, so the sections converge in ordinary W^{1,2}. The limit has an absolutely continuous representative with weak derivative DⱼF, by the fundamental theorem and interval Poincaré, not a density theorem. Apply the preceding argument to any null N: E[1_{F∈N}|DⱼF|²]=0.

\[ F\in\mathbb D^{1,2},\quad \|DF\|_H>0\ \hbox{a.s.}\quad\Longrightarrow\quad\mathcal L(F)\ll dx. \]

Sum over countable j by Tonelli to obtain E[1_{F∈N}‖DF‖²]=0. Strict positivity implies P(F∈N)=0. No inverse-gradient moments are needed for this scalar result, and no continuity of the density has been proved.

## 2. Vector Full Rank Must Come from Actual Directions

<a id="density-proof-vector"></a>

\[ \gamma_F=(\langle DF_i,DF_j\rangle_H)_{i,j\le m},\qquad F_i\in\bigcap_{k\ge1}\mathbb D^{k,2},\quad\det\gamma_F>0\ \hbox{a.s.}\ \Longrightarrow\ \mathcal L(F)\ll dx\ \hbox{on }\mathbb R^m. \]

First establish C¹ finite-coordinate sections. Fix the first n coordinates y and the rest z; use summably accurate cylinder approximations in \(\mathbb D^{n+1,2}\). Fubini and the compact Gaussian lower bound give local W^{n+1,2} convergence for almost every z. For smooth v supported in a fixed rectangle, iterated fundamental theorem gives v(x)=\((-1)^n\)\(\int_{x_1}^{\infty}\cdots\int_{x_n}^{\infty}\partial_1\cdots\partial_n v(y)\,dy\), so sup|v|≤‖∂₁…∂ₙv‖₁. The same applies to first derivatives, using at most n+1 derivatives. With a cutoff and L²-to-L¹, functions and gradients are uniformly Cauchy. Thus sections are C¹ and their ordinary gradients agree with Gaussian weak directional derivatives.

At a rank-m point of the C¹ section y↦F(y,z), select a nonzero m-minor and combine F with the remaining n−m coordinates into a square map Ψ. Its derivative is invertible. On a small neighborhood derivatives stay close to that fixed matrix; integrating differences gives an inverse Lipschitz bound, while contraction gives an open local image. Thus Ψ is locally bi-Lipschitz. For a null N⊂Rᵐ, N×R^{n−m} is null in Rⁿ, and the local Lipschitz inverse preserves nullity. Cover rank-m points countably and integrate over z.

Finite-direction matrices γ⁽ⁿ⁾=Σⱼ≤ₙ(DⱼF)(DⱼF)ᵀ converge pointwise to γ. If γ is positive definite, some finite γ⁽ⁿ⁾ is already positive definite. The union of the preceding full-rank events therefore covers detγ>0, proving the statement. This fully proves the declared higher-Sobolev vector version; the stronger vector Bouleau–Hirsch result with only \(\mathbb D^{1,2}\) is not claimed here.

## 3. Turning Nondegenerate Directions into Output Derivatives

<a id="density-proof-weights"></a>

Now assume F_i∈D∞, detγ>0 almost surely and E(detγ)^{-p}<∞ for every p>1. Entries, determinant and cofactors of γ belong to D∞. Apply smooth reciprocal cutoffs that vanish below 1/n and equal 1/x above 2/n, with k-th derivatives bounded by C_k x^{-k−1} on x>0. Iterated chain rules, Hölder and inverse moments give derivative Lᵖ bounds and DCT convergence; closability yields \(\gamma^{-1}\)∈D∞ entrywise.

\[ U_i=\sum_j(\gamma_F^{-1})_{ij}DF_j,\qquad \langle DF_k,U_i\rangle=\delta_{ik},\quad H_i(G)=\delta(GU_i),\qquad E[(\partial_i\varphi)(F)G]=E[\varphi(F)H_i(G)]. \]

For G∈D∞, Uᵢ and GUᵢ belong to D∞(H). The actual higher-divergence estimate in T-MALLIAVIN gives Hᵢ(G)∈D∞, so δ is not merely formal notation. Start with compactly supported smooth φ and apply the chain rule and adjoint identity. Recursively \(H_{i_1\ldots i_k}(G)=H_{i_k}(H_{i_1\ldots i_{k-1}}(G))\) gives every integration-by-parts order, with integrable weights having all positive moments.

## 4. Actually Obtaining a Smooth Density from Integration by Parts

<a id="density-proof-smooth"></a>

Use φ(x)=exp(i〈θ,x〉), initially with expanding smooth cutoffs; integrable weights and moments of F remove them. Then (iθⱼ)ᵏϕ_F(θ)=E[e^{i〈θ,F〉}H_{j…j}(1)]. Choose |θⱼ|≥|θ|/√m to get |ϕ_F(θ)|≤C_k(1+|θ|)^{-k} for every k. Fourier inversion and every derivative are therefore absolutely integrable.

\[ p_F(x)=\frac1{(2\pi)^m}\int_{\mathbb R^m}e^{-i\langle\theta,x\rangle}\varphi_F(\theta)d\theta,\qquad \partial^\beta p_F(x)=\frac1{(2\pi)^m}\int(-i\theta)^\beta e^{-i\langle\theta,x\rangle}\varphi_F(\theta)d\theta. \]

To avoid assuming F already has a density, add independent √ε standard Gaussian noise. Chapter 14 smoothing gives its density, with characteristic function ϕ_F exp(−ε|θ|²/2). DCT makes these densities and every derivative converge uniformly to the display, so p≥0 and C∞. Meanwhile F+√εZ→F almost surely; compact continuous tests identify p dx with its law, and increasing tests to one give ∫p=1. All density derivatives are bounded. More generally, N integrable integration-by-parts weights with N>m+r give a Cʳ density by the same proof; infinite-order assumptions are sufficient, not necessary.

Separate counterexamples test separate assumptions. F=Z² belongs to D∞ and has γ=4Z²>0 almost surely, hence is absolutely continuous, but its density \(\mathbf1_{\{x>0\}}e^{-x/2}/\sqrt{2\pi x}\) diverges at zero: inverse moments really fail. Conversely φ(x)=0 for x≤0 and exp(−1/x²) for x>0 is smooth with bounded derivatives, so φ(Z)∈D∞ but has a zero atom of mass one half; γ vanishes on half the samples. Differentiability, nondegeneracy and inverse moments have distinct roles.

## 5. Proving a Smooth Density without an Explicit Solution

<a id="density-proof-sde"></a>

Fix T>0, deterministic x and constant σ≠0. Consider Xₜ=x+σBₜ+∫₀ᵗb(Xᵣ)dr. Assume b smooth with all positive-order derivatives bounded; b itself may grow linearly. Chapter 35’s global Lipschitz existence/uniqueness applies. We must establish noise differentiability of the output, not formally differentiate an equation merely because it has a solution.

Let Bⁿ be dyadic Brownian interpolation and drive the corresponding ordinary integral equation Xⁿ. This is a smooth function of finitely many Gaussian coordinates. Interpolants are used as Gaussian cylinder approximations, not claimed adapted in the original filtration or used as Itô strategies. Gronwall bounds sup|Xⁿ−X| by |σ|e^{LT}sup|Bⁿ−B|. Brownian continuity and Doob’s maximal moment bounds give convergence in every Lᵖ. In H=L²[0,T], DBⁿₜ=\(P_n\mathbf1_{[0,t]}\), with Pₙ the dyadic-step orthogonal projection, and supₜ‖\(P_n\mathbf1_{[0,t]}\)−\(\mathbf1_{[0,t]}\)‖≤√(mesh).

Finite-dimensional differentiation gives Y₁ⁿ(t)=σ\(P_n\mathbf1_{[0,t]}\)+∫b′(Xᵣⁿ)Y₁ⁿ(r)dr. Higher Yₖⁿ equations are indexed by partitions of {1,…,k}: the single block gives b′Yₖⁿ, and each other partition π contributes b^{(|π|)}(Xⁿ) times the \(Y^n_{|A|}\) for its blocks, with tensor indices assigned accordingly. Bounded coefficients and Gronwall inductively give deterministic H-tensor bounds \(C_{k,T}\) on [0,T].

Convergence follows by the same induction: the next bounded derivative controls the Lipschitz constant of each b^{(j)}. Expand product differences one factor at a time; lower-order convergence and deterministic bounds make integral errors vanish in Lᵖ maximal norm, then apply Gronwall. Thus all Yₖⁿ converge and closability gives Xₜ∈D∞. Linear growth and Brownian maximal moments control values of Xⁿ; the finite Gaussian derivatives have polynomial growth, so the approximants really belong to the cylinder core.

\[ D_sX_t=\sigma\exp\!\left(\int_s^t b^\prime(X_r)dr\right)\mathbf1_{\{s\le t\}},\qquad \gamma_{X_t}\ge\sigma^2 t e^{-2Lt}>0,\quad L=\|b^\prime\|_\infty,\quad t>0. \]

Solve the limiting Y₁ linear equation at each s; the formula holds ds⊗P-almost everywhere. Its deterministic covariance lower bound gives all inverse moments, so each fixed t>0 has a C∞ density. For b=−tanh no explicit transition kernel is needed. OU is a linear special case, but the new result is noise sensitivity and nondegeneracy for nonlinear outputs. General multiplicative noise, degenerate multidimensional diffusions and Hörmander’s bracket theorem are not proved, nor is the point mass at t=0 called a density. Return to [the application](../chapters/39-malliavin.md#noise-sde).
