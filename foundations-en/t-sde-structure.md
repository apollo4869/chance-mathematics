# T-SDE-STRUCTURE: Laws, Inputs and a Common Random Space

A companion to [Chapter 35](../chapters/35-sde-wellposedness.md). Inputs are Chapter 10’s standard Borel disintegration, Chapter 24’s weak convergence on continuous-path space, Chapters 31–32’s continuous integration and Itô formula, Chapter 33’s Lévy characterization, and the continuous-martingale pth upper bound proved directly in T-SDE-WELLPOSEDNESS 1. Basic constructions are in [T-SDE-WELLPOSEDNESS](t-sde-wellposedness.md). No general Bichteler–Dellacherie converse or future local time is used.

## 1. Recovering a Brownian Driver from a Martingale Problem

<a id="sde-proof-mp"></a>

Let b:Rᵈ→Rᵈ and σ:Rᵈ→Rᵈˣᵐ be locally bounded Borel functions, with a=σσᵀ. A probability Q on C([0,∞),Rᵈ) solves the continuous martingale problem when the chapter’s observable for every f∈C_c∞ is a local martingale in the coordinate filtration. The initial law is prescribed and paths remain finite at every finite time. Local boundedness ensures finite local drift and energy on compact paths.

The forward implication is Itô with compact cutoffs. For the reverse choose χ_R equal to one on the radius-(R+1) ball, test χ_R xᵢ and χ_R xᵢxⱼ and stop at τ_R. These tests agree with coordinates and products inside the ball, so Mᵢ=Xᵢ−X₀ᵢ−∫bᵢ(X)ds is a continuous local martingale. Applying the continuous semimartingale product formula identifies MᵢMⱼ−∫aᵢⱼ(X)ds as a local martingale. A continuous finite-variation local martingale is constant, giving [Mᵢ,Mⱼ]=∫aᵢⱼ. Let R increase; every compact path lies in a ball, and identities agree on overlaps.

First take the usual augmentation of the coordinate filtration. Right-continuization preserves continuous local martingales: for bounded stopped M and sₙ↓s, conditional expectations on decreasing sigma-algebras give E[Mₜ|Fₛ₊]=limMₛₙ=Mₛ. Completion adds only null sets. Enlarge by an independent m-dimensional Wiener space. Original martingales remain martingales by independent rectangle tests and a monotone class. Their cross brackets with the independent Brownian motion vanish, since the products are local martingales and the product formula applies.

\[ \sigma^+(x)=\lim_{n\to\infty}\sigma(x)^\top(a(x)+n^{-1}I_d)^{-1},\quad P(x)=\sigma^+(x)\sigma(x),\quad Q(x)=\sigma(x)\sigma^+(x). \]

Pointwise singular-value decomposition proves that the limit is finite, that P,Q are the respective orthogonal range projections, and that σ⁺a(σ⁺)ᵀ=P. The formula itself proves Borel measurability without a measurable eigenvector selection. Borel compositions with continuous adapted X are predictable. Since ∫tr(σ⁺a(σ⁺)ᵀ)ds≤mT, the possibly unbounded pseudoinverse can be constructed in the vector-energy extension of Chapter 31’s random-clock method.

The vector covariance energy must be used here: finiteness of its total quadratic form does not imply separate integrability of every coordinate term. First stop M on an L² window. For bounded simple matrix H, conditional orthogonality and mixed brackets give E|∫H dM|²=E∫tr(HaHᵀ)ds. Put Hₙ=σ⁺1_{||σ⁺||≤n}; its bounded predictable integral is constructed coordinatewise by Chapter 31. Differences of truncations have joint energy ∫tr(P)1_{truncation band}ds, dominated by mT and tending to zero. Their maximal L² limit defines the full vector integral; then release stopping of M. Energy and cross brackets pass through the same limits. This handles possible cancellations among degenerate correlated coordinates. Associativity with locally bounded σ below likewise holds first for truncations and then by common covariance-energy limits.

\[ W_t=\int_0^t\sigma^+(X_s)dM_s+\int_0^t(I_m-P(X_s))d\overline W_s,\qquad [W^i,W^j]_t=\delta_{ij}t. \]

Lévy’s characterization makes W Brownian in the enlarged usual filtration, including independence of increments from F₀. Moreover ∫σdW=∫QdM since σ(I−P)=0. The bracket of M−∫QdM is ∫(I−Q)a(I−Q)ᵀds=0, so the difference vanishes. This is a weak SDE. A covariance square root is not unique; its path-law description depends on a. The construction does not claim that the coordinate filtration already contains every Brownian direction needed.

## 2. Causal Conditional Kernels and Yamada–Watanabe

<a id="sde-proof-yw"></a>

Consider a continuous Brownian SDE with deterministic Borel b(t,x),σ(t,x), a fixed initial law μ, and nonexplosive weak solutions satisfying local drift and square-energy conditions. Assume weak existence and pathwise uniqueness. The input space Y=Rᵈ×C₀([0,∞),Rᵐ) and output space S=C([0,∞),Rᵈ) are Polish. Chapter 10 supplies K(y,dx), with input law ν=μ⊗Wiener. For rational t and each output-past event A, K(y,A) has a version depending only on input up to t.

To prove the last assertion, future Brownian increments are independent of the original Fₜ, which contains A and input past. For input-past u and future-increment v, E[1_Au v]=E[1_Au]E[v]. Put kₜ=E[1_A|ξ,W≤t]; then E[kₜu v] gives the same value. Past and future input cylinders generate the full input sigma-algebra, so a monotone class gives E[1_A|Y]=kₜ. Take a common null set for a countable rational-coordinate generator and extend to all past events.

For kernels K₁,K₂ of two weak solutions define Π(dy,dx₁,dx₂)=ν(dy)K₁(y,dx₁)K₂(y,dx₂). For two output-past cylinders A₁,A₂ and input-past u, the product K₁(y,A₁)K₂(y,A₂)u depends only on input past. It factors from any future-increment function v. A monotone class gives independence from the entire enlarged past. Right-continuization and completion are handled as in section 1, preserving Brownian motion. Both initial values equal the common ξ.

The integral equation must also survive the new filtration. For H=σ(t,Xₜ), first stop at bounded energy and truncate H, then approximate by backward averages n∫_(t−1/n)₊^t Hₛds, continuous adapted processes converging in L²(dt×P). For each continuous approximation, deterministic left-step integrals converge by Doob and isometry. A diagonal sequence works simultaneously under both marginal laws and consists of Borel functionals of (X,W). On the new space the stochastic integral is defined by the same isometric approximation, so equality of marginal laws preserves the equation. The drift is an ordinary measurable integral. Releasing stopping gives two genuine weak solutions.

First set K₁=K₂=K. Pathwise uniqueness gives Π(X₁=X₂)=1, so for almost every y the product K(y)⊗K(y) is supported on the diagonal. For a countable separating algebra Bₖ, K(y,Bₖ)(1−K(y,Bₖ))=0. A probability not concentrated at one point has two support points with disjoint open neighborhoods of positive mass, contradicting this zero-one property. A Polish probability has full-measure support, directly from a countable base. Thus K(y)=δF(y).

A measurable point can be selected explicitly: use nested countable Borel partitions of S with diameter ≤2⁻ⁿ, choose the unique mass-one cell and a preset representative. Nested representatives are Cauchy and converge to F; completeness and measurability of pointwise limits apply. Choose any fixed path on the null set. For rational-t output generators, 1_{F(Y)∈A}=K(Y,A) depends only on input past. Rational coordinates are adapted; continuity and rational times decreasing to t give adaptation in the usual augmented input filtration.

The joint law of (X,Y) equals that of (F(Y),Y). Therefore on any prescribed input with law ν the same integral-functional construction makes F(Y) a strong solution. Cross-coupling K₁,K₂ and applying pathwise uniqueness gives δF₁(y)=δF₂(y) almost everywhere, so the joint law and X law are unique. This proof fixes μ; it does not assert a universal pathwise function simultaneously for every initial law without an additional measurable-parameter argument.

## 3. Countable Tests and Well-Posedness of the Martingale Problem

<a id="sde-proof-tests"></a>

The quantifier over all smooth tests reduces to a countable class. On each compact ball choose a countable dense subset in the uniform norm of functions and derivatives through order two, and unite over integer balls. Local boundedness controls generator error by that norm. Stopped at exit and a finite horizon, tests are bounded and UI, so conditional expectations pass to the dense limit. Past tests likewise reduce to a countable algebra of rational coordinates and then extend by a monotone class.

For globally bounded continuous coefficients, Euler weak existence is already proved. Pathwise uniqueness, section 2 and the two-way realization in section 1 imply uniqueness of the martingale problem. If xₙ→x, uniform fourth increment bounds and bounded initial values give tightness. Every limit passes the same bounded continuous martingale tests used in the basic companion and solves the problem from x. Uniqueness forces Qₓₙ⇒Qₓ. Thus x↦Qₓ is weakly continuous and in particular a Borel kernel. The argument also works for globally Lipschitz linear-growth coefficients with uniform moment localization.

## 4. The Same Local Rule after Stopping

<a id="sde-proof-markov"></a>

Start with time-homogeneous globally Lipschitz coefficients. Simple-integral approximations in Picard give a jointly Borel solution functional of initial state and Wiener input. Approximate random initial states by finite-valued variables and transfer the relation by stability. After deterministic s, Brownian increments are independent of the past and the stopping identity makes the continuation solve the same SDE from Xₛ. Pathwise uniqueness and the independent input kernel give the chapter’s Markov identity.

Pₜf is continuous for bounded continuous f: maximal L² stability gives Xˣⁿₜ→Xˣₜ in probability when xₙ→x, and boundedness passes expectations. Preservation of C₀ would require additional control of entry from infinity; C_b-Feller is not declared full C₀-Feller here. For bounded S let Sₙ=2⁻ⁿ(⌊2ⁿS⌋+1). Grid slicing gives E[f(Xₛₙ₊ₜ)|Fₛₙ]=Pₜf(Xₛₙ). Test against A∈F_S⊂Fₛₙ; continuity of paths and Pₜf lets DCT pass the limit. Extend from C_b to B_b by a function monotone class. Truncate finite S at integers. Conditional iteration yields future finite-dimensional laws, establishing strong Markov.

One can also prove the result directly for the preceding well-posed martingale problem without a strong-solution functional. Restrict to globally bounded continuous coefficients, or the globally Lipschitz linear-growth case with uniform localized moment control. Given bounded S, disintegrate the post-S continuous path conditional on the stopped past, first on the uncompleted standard Borel coordinate space; completion changes only null sets. Countable martingale tests and bounded sampling show that this conditional law solves the same problem from X_S: test at S+r,S+t, approximate S discretely and use continuity with bounded or stopped domination. Past cylinders provide conditional-law tests. Countability gives one exceptional null set; density restores all f. Uniqueness identifies the kernel with Q_{X_S}. Borel measurability of x↦Q_x was proved above, without an unmentioned measurable selection. This establishes strong Markov in the stated scope.

## 5. A Jointly Continuous C¹ Forward Flow and Its Jacobian

<a id="sde-proof-flow"></a>

Assume time-homogeneous b,σ∈Cᵦ³(Rᵈ), with columns σₖ. Define Φₛ,ₜ(x) for 0≤s≤t≤T and extend by x for t<s. For any p≥2, continuous BDG and Hölder give a useful estimate: Lipschitz coefficient differences yield E sup|U−V|ᵖ≤C times the initial pth difference plus the corresponding pth residual integrals. In detail drift uses Tᵖ⁻¹∫|difference|ᵖ, noise uses C_p Tᵖᐟ²⁻¹∫||difference||ᵖ, and Gronwall closes the bound.

\[ E\sup_{t\le T}|\Phi_{s,t}(x)-\Phi_{r,t}(y)|^p\le C_{T,p,K}\bigl(|x-y|^p+|s-r|^{p/2}\bigr),\qquad |x|,|y|\le K. \]

For different start times, bound the short increment between them by C|s−r|ᵖᐟ², then use the difference estimate on the common continuation. The same short-increment bound applies between the starts. Choose arbitrarily large p and apply the Kolmogorov grid proof in parameters (s,x), with values in the maximal-norm space C([0,T]). Its dimension is d+1, neighbor differences have pth moment ≤Cδᵖᐟ², and p/2>d+1 makes the Markov bad-edge bounds summable for a suitable Hölder exponent. Borel–Cantelli gives a locally Hölder C-path-valued version and thus joint continuity in (s,t,x). Glue over integer T,K.

Construct the linear matrix SDE J=I+∫Db(Φ)Jdu+∑∫Dσₖ(Φ)JdWₖ. Its random coefficients are bounded and adapted; Picard estimates never required deterministic coefficients, so they give a unique continuous J with locally uniform moments of every order. Parameter differences of J contain Db(Φˣ)−Db(Φʸ), controlled by bounded second derivatives. Hölder with 2p moments gives the same parameter bound, and hence a jointly continuous version of J.

For direction v put Dʰ=(Φ(x+hv)−Φ(x))/h. The integral mean-value theorem makes its coefficients averages of Db,Dσ along the two-state segment. Comparing with Jv, bounded second derivatives bound coefficient error by C|Φ(x+hv)−Φ(x)|. The preceding 2p estimates give E||Dʰ−Jv||ᵖ_T≤C|h|ᵖ|v|²ᵖ. To turn mean differentiability into pathwise differentiability, partition a finite line segment in Lᵖ(C-path). Each segment has error norm ≤C times its squared length, so the summed error vanishes. Continuity of J gives the Riemann-sum limit. Hence

\[ \Phi_{s,t}(y)-\Phi_{s,t}(x)=\int_0^1J_{s,t}(x+\theta(y-x))(y-x)d\theta. \]

First use a common null set for rational s,x,y and extend by joint continuity. The identity proves classical C¹ dependence with derivative J; fixed-x Lᵖ difference-quotient convergence alone was not passed off as pathwise C¹. The flow relation first follows by pathwise uniqueness for rational s≤u and rational x, since the continuations share initial state and equation. Joint continuity extends to all s≤u≤t and x.

\[ dK=K\left(-A+\sum_kB_k^2\right)dt-\sum_kKB_kdW^k,\quad K_{s,s}=I,\quad A=Db(\Phi),\quad B_k=D\sigma_k(\Phi),\quad d(KJ)=0. \]

The linear equation for K is constructed in the same way, and bounded derivatives with moment estimates give parameter continuity. The product cross term −∑KBₖ²J cancels the extra drift, so KJ=I, first for countably many parameters and then simultaneously. The finite-dimensional inverse function theorem gives a local C¹ diffeomorphism for each Φ. Local nonsingularity alone does not give global bijectivity: states from infinity must be prevented from entering a bounded region.

Under Cᵦ³ this step can also be completed. Put D(s,t,x)=Φₛ,ₜ(x)−x. Bounded coefficients give E||D(s,·,k)||ᵖ_T≤C_T,p uniformly over integer lattice points k. The preceding spatial and starting-time bounds are also uniform in k. On each unit cube k+[0,1]ᵈ use dyadic grids in (s,x). Level j has at most C2ʲ⁽ᵈ⁺¹⁾ edges, each with Lᵖ(C-path) difference norm ≤C2⁻ʲᐟ². The level’s maximum edge norm is at most C2⁻ʲ⁽¹ᐟ²⁻⁽ᵈ⁺¹⁾ᐟᵖ⁾. Choose p>2(d+1), sum levels by Minkowski and extend by continuity. This gives E sup_{s≤t≤T,x∈k+[0,1]ᵈ}|D|ᵖ≤C_T,p uniformly in k.

Markov’s inequality bounds the chance that the cube’s maximal displacement exceeds |k|/2 by C|k|⁻ᵖ. This is summable over lattice points. Borel–Cantelli leaves only finitely many bad cubes. On one probability-one set, inf_{s≤t≤T}|Φₛ,ₜ(x)|→∞ as |x|→∞. Every map is proper, meaning compact sets have compact preimages, uniformly over time parameters.

For completeness verify the local-to-global topological step. For fixed s,t the image is open by local inverses. If image points yₙ→y, properness gives a convergent subsequence of their preimages, so the image is closed and hence all of Rᵈ. Each fiber is discrete and compact, therefore finite. Each local inverse varies continuously with (s,t,y): use the inverse Jacobian at a base point to rewrite Φₛ,ₜ(x)=y as a contraction on a small ball; joint derivative continuity preserves the contraction nearby. Properness prevents new distant preimages from appearing at neighboring parameters, so fiber cardinality is locally constant. Along t starting at s it remains the value one of the identity map. Thus every Φ is globally bijective; its local C¹ inverses glue to a global C¹ inverse, jointly continuous in parameters with inverse derivative. This establishes a C¹ stochastic diffeomorphism flow under Cᵦ³ without invoking future reverse-time stochastic calculus.

Return to the [Chapter 35 ending](../chapters/35-sde-wellposedness.md#sde-insight). Actual dependencies are continuous integration, Itô, conditional kernels, tightness and Brownian characterization. Their independent mathematical final reviews remain open; citation and build status do not close them.
