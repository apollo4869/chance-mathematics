# T-SDE-WELLPOSEDNESS: From Approximations to Actual Solutions

A companion to [Chapter 35](../chapters/35-sde-wellposedness.md). Brownian integration uses Chapter 31’s isometry, Doob estimate and stopping; Chapter 32 supplies continuous Itô, and Chapter 34 supplies predictable L² integration against Poisson measures with deterministic compensator. Filtrations are usual and Brownian motion is Brownian relative to the full filtration used. The finite horizon T is arbitrary, the initial variable is independent of future drivers, and deterministic coefficients are Borel. No general good-integrator converse, local time, future scale-speed theorem or general SDE theorem is assumed.

## 1. Picard, Stability and the Complete Limit Argument

<a id="sde-proof-picard"></a>

Assume the global Lipschitz and linear-growth bounds of the chapter for 0≤t≤T and all x,y. Start with E|ξ|² finite. If Y is continuous and adapted with finite E sup|Y|², coefficient compositions are predictable; growth makes both integrals exist and Γ(Y) belongs to the same space. The squared drift maximum is bounded by T∫|b|²; Doob and isometry bound the noise maximum by 4∫||σ||². The three-term square bound gives

\[ E\sup_{u\le t}|\Gamma(Y)_u|^2\le3E|\xi|^2+3(T+4)K\int_0^t(1+E|Y_s|^2)ds. \]

A uniform iteration moment bound is not yet necessary: the displayed inequality makes every iterate legitimate. Let Dₙ(t)=E supᵤ≤ₜ|Xⁿᵤ−Xⁿ⁻¹ᵤ|². A two-term square bound gives C=2L²(T+4) and Dₙ₊₁(t)≤C∫Dₙ. The first term D₁(T)≤A=C′T(1+E|ξ|²) is finite. Induction gives Dₙ₊₁(t)≤A(Ct)ⁿ/n!. Therefore

\[ \sum_{n\ge0}\bigl(E\|X^{n+1}-X^n\|_T^2\bigr)^{1/2}<\infty,\qquad E\sum_n\|X^{n+1}-X^n\|_T<\infty. \]

The first assertion, Minkowski and L² completeness established with Chapter 15 give an L² maximal-norm limit. The second gives absolutely uniform convergence almost surely by Tonelli. The uniform limit is continuous and adapted; completion accommodates the common null set. Drift and noise differences are bounded by T L²∫E|Xⁿ−X|² and 4L²∫E|Xⁿ−X|², respectively, and vanish. Thus Γ(X)=X in the L² maximal norm, hence indistinguishably by continuity.

Applying the mapping bound to X and iterating the integral inequality gives E||X||²_T≤C_T(1+E|ξ|²). Two solutions with the same driver satisfy f(t)≤3E|ξ−η|²+C∫f, so f(T)≤3eᶜᵀE|ξ−η|². Equal initial values give uniqueness. General candidates are first stopped at common levels of state amplitude and integral energy, making expectations legitimate. Gronwall gives zero discrepancy. Releasing the common stops removes any prior global second-moment requirement on candidates.

For arbitrary finite ξ use ξⁿ equal to ξ on |ξ|≤n and zero otherwise. On Aₙ={|ξ|≤n}∈F₀, the difference estimate multiplied by 1_Aₙ identifies Xⁿ and Xᵐ for m≥n without changing probability. Glue along Aₙ. Measurability, adaptation, continuity and the integral identity hold on their union. Integer horizons glue by uniqueness to give a solution on the half-line.

The estimate also gives coefficient stability. If bₙ,σₙ share L,K and converge locally uniformly on bounded state sets, stopped errors are controlled by the initial error and ∫(|bₙ−b|²+||σₙ−σ||²)(s,Xₛ)ds. DCT and Gronwall give stopped maximal L² convergence, and uniform moment bounds remove stopping to yield ucp. Convergence in probability is not automatically upgraded to almost-sure convergence of the full sequence.

<a id="sde-proof-continuous-moments"></a>

The higher-moment upper bound needed later follows directly here, without relying on Chapter 34’s general jump BDG pending final review. Let N be a continuous vector local martingale from zero, A=tr[N], and p>2. Stop N and A boundedly. Itô for |N|ᵖ and its Hessian bound give E|N_T|ᵖ≤C_p E[(N*ₜ)ᵖ⁻²A_T]. Doob’s pth inequality gives E(N*ₜ)ᵖ≤D_p C_p E[(N*ₜ)ᵖ⁻²A_T]. Young with a sufficiently small coefficient absorbs half the maximal moment, leaving C′_p E A_Tᵖᐟ². Release stopping by Fatou. For p=2 use Doob and isometry directly. Thus E sup|∫H dW|ᵖ≤C_p E(∫||H||²ds)ᵖᐟ². This short independent proof supplies fourth moments for weak existence and arbitrary high moments for the flow; neither two-sided nor jump BDG is needed.

## 2. Local Gluing, Explosion and Lyapunov Control

<a id="sde-proof-local"></a>

Assume boundedness and uniform local Lipschitz dependence on x on compact time-state regions. Choose smooth χ_R equal to one on the radius-R ball and zero outside radius R+1. The cutoffs χ_Rb,χ_Rσ are globally Lipschitz with linear growth. Xᴿ and Xˢ satisfy the same stopped equation until either leaves the radius-R ball, hence coincide by uniqueness, including the exit value by continuity. Their exit times agree.

Define X for t<ζ=limτ_R using these consistent exit times. This countable gluing gives a measurable continuous adapted process. If ζ≤T while limsupₜ↑ζ|Xₜ| were finite, a larger cutoff solution would extend it beyond ζ, a contradiction. The same stopped comparison gives local uniqueness.

Take nonnegative coercive C² V with LₜV≤C_T(1+V). Start with bounded initial values. Stop Itô at τ_R and an L² localization. Coefficients and derivatives are bounded inside the ball, so the martingale has mean zero. Thus E V(Xₜ∧τ_R)≤EV(ξ)+C∫₀ᵗ(1+E V(Xₛ∧τ_R))ds; nonnegativity bounds the stopping indicators and permits Gronwall. At exit V is at least its infimum on the sphere, giving the chapter’s probability bound. Let R increase and take integer T to obtain ζ=∞ almost surely. General initial values are handled on F₀ events, or directly when EV(ξ)<∞.

## 3. Joint Brownian and Poisson Driving Noise

<a id="sde-proof-jump"></a>

Assume N has compensator dtν, with σ-finite ν on a standard Borel mark space. W and N are independent and retain their Brownian/Poisson independent increments relative to the joint filtration; ξ is F₀-measurable. On E₀ impose the chapter’s joint squared Lipschitz bound and |b(t,0)|²+||σ(t,0)||²+∫|g(t,0,z)|²ν(dz)≤K_T. Picard has a third martingale integral. The three-term square bound, Poisson isometry and Doob give

\[ E\sup_{u\le t}|X^{n+1}_u-X^n_u|^2\le3(T+8)L^2\int_0^tE\sup_{v\le s}|X^n_v-X^{n-1}_v|^2ds. \]

No optimal constant is needed; factorial convergence follows as in section 1. Iterates are càdlàg adapted and left limits predictable. Maximal L² convergence has an almost-sure uniform subsequence, whose limit is càdlàg; left-limit energy errors vanish as well. Isometry passes the equation to the limit. Use the integral convention (0,t] at jumps, not Xₜ as a predictable input. The difference estimate gives uniqueness, moment bounds and nonexplosion.

Now suppose ν(E₁)<∞ and h is jointly Borel and finite for every input. E₁ arrival times Sₖ are finite in number on compact intervals and have no simultaneous arrivals. Restrictions to E₀ and E₁ are independent and almost surely have no common jump time, first on finite mark bands by conditioning and then by countable covering. At Sₖ update x to x+h and solve the next small-jump equation.

Picard after a random time needs no unproved general strong Markov theorem. For finite F_S-measurable U use U1_{S≤t} as the base process and integrate only over (S,t]. Every iterate is adapted with predictable left inputs; the same estimates apply on the F_S events |U|≤n. Multiplication after S uses the predictable rule 1_A1_(S,∞), so the constructions glue. This constructs each restart on the original space. The small-jump equation holds after restart; its artificial initialization jump at S is not counted in the integral.

Finitely many jumps map finite states to finite states, and each intervening global small-jump solution is nonexplosive. The interlaced solution is therefore nonexplosive on every finite horizon. Without a ν-second moment for h, E sup|X|² may be infinite; statewise localization still constructs paths. Locally Lipschitz small-jump coefficients give a maximal solution until exit. A large jump can overshoot a ball, so the exit value must not be called bounded.

## 4. The Complete Smoothing Argument for a One-Dimensional Modulus

<a id="sde-proof-modulus"></a>

Suppose b is locally Lipschitz and |σ(t,x)−σ(t,y)|≤ρ(|x−y|), where ρ is continuous nondecreasing, positive away from zero, vanishes at zero and has divergent ∫₀₊ρ⁻². Choose a₀=1 and aₙ↓0 with ∫ₐₙ^ₐₙ₋₁ρ⁻²=n. A smooth ψₙ supported in (aₙ,aₙ₋₁), with integral one and 0≤ψₙ(u)≤2/(nρ(u)²), is obtained by deleting short endpoint intervals retaining integral greater than n/2, smoothly approximating from below and normalizing. Define the even C² function

\[ \phi_n(z)=\int_0^{|z|}\!\int_0^y\psi_n(u)\,du\,dy,\quad |\phi_n^\prime|\le1,\quad |z|-a_{n-1}\le\phi_n(z)\le|z|,\quad\phi_n^{\prime\prime}(z)\rho(|z|)^2\le2/n. \]

For solutions with the same driver and initial value, stop at τ_R=inf{|X|∨|Y|≥R}. Itô and localization make the martingale mean zero. Drift is bounded by L_R∫₀ᵗE[1_{s≤τ_R}|Xₛ−Yₛ|]ds, the second-order term by t/n. The functions converge to absolute value with bounded error; monotonicity is unnecessary. DCT applies since stopped differences are bounded by 2R. Thus f_R(t)=E|Xₜ∧τ_R−Yₜ∧τ_R|≤L_R∫₀ᵗf_R(s)ds. Gronwall gives zero; rational times and continuity give a common null set, and releasing R proves uniqueness up to the common lifetime.

## 5. Weak Existence for Continuous Coefficients: Beyond Tightness

<a id="sde-proof-weak"></a>

First let b,σ be bounded continuous and time-homogeneous, with deterministic X₀=x. On mesh δ define the frozen Euler solution Xᵟ=x+∫b(Xᵟ_η(s))ds+∫σ(Xᵟ_η(s))dW, where η(s)=δ⌊s/δ⌋. Explicit interval recursion constructs a continuous adapted process. The continuous-martingale p=4 estimate gives E|Xᵟₜ−Xᵟₛ|⁴≤C_T|t−s|² uniformly in δ: drift contributes order |t−s|⁴, and the noise bracket is bounded by C|t−s|. Kolmogorov tightness and Prokhorov give a continuous-path weak limit Q.

Frozen-state error satisfies E∫₀ᵀ|Xᵟₛ−Xᵟ_η(s)|²ds≤C_Tδ. Its maximal oscillation also vanishes in probability by tightness and vanishing mesh. For f∈C_c∞, Itô gives a martingale whose generator coefficients are frozen while derivatives use the current state. Uniform continuity on compact sets and the uniform moment bound control the integral difference from ∫Lf(Xᵟₛ)ds in L¹.

For rational s<t multiply a martingale increment by a bounded continuous function of finitely many past coordinates. The resulting path functional is bounded continuous because Lf is, so weak convergence passes expectations; the L¹ error vanishes. A function monotone class extends cylinder tests to coordinate Fₛ, and continuity extends rational s,t to all times. Thus Q solves the martingale problem. The next companion’s pseudoinverse construction supplies Brownian noise, yielding a weak solution without circularly using it to prove tightness.

With linear growth instead of boundedness, BDG, Hölder and Gronwall uniformly bound fourth maximal moments for deterministic initial x: E supᵤ≤ₜ|Xᵟᵤ|⁴≤C(1+|x|⁴)+C∫₀ᵗE supᵥ≤ₛ|Xᵟᵥ|⁴ds. Fourth increment moments remain ≤C_T|t−s|², so tightness follows. Compactly supported f makes Lf bounded continuous, since derivatives vanish outside a compact set. Restrict frozen errors to a large ball and control the tail by moment bounds. Identification and Brownian reconstruction are unchanged. For a random initial law use the same Euler construction with that law and truncate initial-amplitude moment bounds. This gives weak existence for the prescribed law, not an unproved measurable choice among solutions.

## 6. Three Distinct Conclusions for Tanaka’s Equation

<a id="sde-proof-tanaka"></a>

Put s(x)=1 for x≥0 and −1 for x<0. For standard Brownian B set W=∫s(B)dB. Its energy is t, so Lévy identifies W as Brownian in the same filtration. Associativity gives ∫s(B)dW=∫s(B)²dB=B, yielding weak existence. Every weak solution X has [X]=t and is Brownian, giving uniqueness in law. Pathwise uniqueness fails: on the constructed space B and −B share the driver W, because ∫1_{B=0}dt=0 by Tonelli and P(Bₜ=0)=0 for positive t, without local time.

To rule out another hidden strong construction, prove joint-law uniqueness. Choose bounded continuous sₙ→s off zero with |sₙ|≤1. Gaussian marginals and Tonelli give E∫|sₙ(X)−s(X)|²dt→0. For fixed n, deterministic left sums converge in probability to ∫sₙ(X)dX since sₙ(X) is continuous. A diagonal subsequence makes W=∫s(X)dX a Borel path functional of X on a Wiener-full set. Every weak solution has the same X law, hence the same joint law.

Brownian sign reversal preserves Wiener law and leaves the integral unchanged, so (X,W) and (−X,W) have the same law. Thus E[Xₜh(W)]=−E[Xₜh(W)]=0 for every bounded measurable h, giving E[Xₜ|W]=0. A strong solution from ξ=0 would make Xₜ measurable in past W, hence in the entire W path, forcing Xₜ=0, a contradiction. Weak existence, uniqueness in law and absence of strong solutions have all been proved.

Return to [Chapter 35’s conditional-kernel construction](../chapters/35-sde-wellposedness.md#sde-yamada). Self-checking is not independent mathematical final review. Broader weak-solution and flow scope is stated precisely in the other companion.
