# T-JUMP-CALCULUS: Companion Proofs for Semimartingales, Compensation and Jump Calculus

This page links to [Chapter 34](../chapters/34-semimartingales.md). Unless stated otherwise the filtration is usual, T is finite, paths are càdlàg and initial values are recorded separately. M denotes a local martingale and FV means pathwise finite variation. Inputs are Chapter 27’s rational-coordinate measurability of jump functionals, Chapter 30’s Doob–Meyer and dual predictable projection, Chapters 31–32’s continuous integration and Chapter 33’s Lévy characterization. Jump integrals and brackets are constructed here without assuming general BDG or future SDE theory. Section 13 distinguishes the proved Rao version from the outstanding general good-integrator converse.

## 1. Localization and Bounded-Jump Decomposition

<a id="t-jump-localization"></a>

The jump-measurability lemma in Chapter 27’s T-LEVY-PATHS uses only finite step approximation of a càdlàg function. Away from zero there are finitely many jumps; grid sums of continuous compactly supported mark tests converge pathwise, and π–λ extends to Borel counts. For adapted càdlàg X, the count through t therefore depends only on coordinates through t and is adapted, càdlàg and increasing. Its k-th arrival is a stopping time because arrival by t is equivalent to a count of at least k. Size bands and k-th arrivals enumerate all jumps countably, without a general début theorem. These facts justify the measurability, count stops and variations of all jump sums below.

The running maximum of a local martingale is locally integrable. First stop to a closed martingale on finite T, then stop at κ, its first crossing of amplitude n. The maximum through κ is at most n+|Mκ|, and closed-martingale sampling gives E|Mκ|≤E|MT|. Combine integer T and the original localizers. This is L¹ control, not a false boundedness or L² claim at an overshooting jump.

Let J be the sum of jumps of M whose absolute size exceeds one. Up to the n-th such jump, VarJ≤2nM∗. Common localization with the preceding paragraph makes J locally of integrable variation. Chapter 30’s signed FV dual projection constructs predictable Jᵖ with J−Jᵖ a local martingale. Testing predictable rules on the graph of a predictable time S gives ∆Jᵖ_S=E[∆J<sub>S</sub>|F<sub>S-</sub>]. Chapter 30 also covers nonzero jumps of predictable càdlàg FV processes by countably many announceable times. The following jump identities use that countable common exceptional set.

\[ \Delta J^p_S=E[\Delta M_S\mathbf1_{\{|\Delta M_S|>1\}}\mid\mathcal F_{S-}]=-E[\Delta M_S\mathbf1_{\{|\Delta M_S|\le1\}}\mid\mathcal F_{S-}],\qquad |\Delta J^p_S|\le1. \]

For the second equality first use conditional fairness at announceable times under common UI localization, then remove the stops. No conditional expectation of an unlocalized nonintegrable jump is taken. Put L=M−J+Jᵖ. Its jumps have size at most two, and D=J−Jᵖ is an FV local martingale of locally integrable variation. Stopping L at amplitude n bounds it by n+2, making it a bounded, hence L² martingale. Thus L is locally square-integrable and M=L+D is the required fundamental decomposition.

A second localization fact will control random energy. A predictable increasing càdlàg A starting at zero and finite on compact paths can be localized to bounded processes. Its first attainment τ_n of a positive level n is predictable: continuous attainment is announced by first attainments of lower levels; attainment by a jump is covered by the predictable jump graphs just described, restricted by F<sub>S-</sub> events. These two cases cover the first attainment. For announcers σⁿ_k<τ_n increasing to τ_n, choose k(n) with P(σⁿ_k<τ_n∧n−1/n)≤2⁻ⁿ. A is below n through σⁿ_k. These stops tend almost surely to infinity; tail infima make them increasing and remain stopping times by right continuity. This provides bounded-clock localization.

## 2. L² Integration, Jumps and Random Energy

<a id="t-jump-l2"></a>

On finite T first take a closed L²-martingale M starting at zero. M² is class D: Mσ²≤E[M<sub>T</sub>²|Fσ], a UI family, so positive domination gives UI. Chapter 30 provides unique predictable increasing A=⟨M⟩ with M²−A a martingale. Orthogonal increments give E(H·M)²_T=E∫H²dA for simple predictable H. First use bounded coefficients and intervals (s,t], including the terminal jump.

Define the finite measure ρ(G)=E∫1_G dA on the predictable sigma-algebra. Finite Boolean combinations of predictable rectangles are dense in ρ: approximable sets form a monotone class, and simple functions then approximate every L² function. Refining their finitely many time endpoints gives simple predictable processes. Isometry extends the integral to L²(ρ). Doob gives E sup|Iⁿ−Iᵐ|²≤4||Hⁿ−Hᵐ||²_ρ. A summable subsequence converges uniformly almost surely on [0,T], giving an adapted càdlàg L²-martingale. Conditional expectations pass at each time in L²; dense times and right continuity give uniqueness of process versions.

Stopping holds first for rectangles. A stopped simple function need not have a deterministic partition form, but it is predictable and can be approximated in the same ρ. Isometry and Doob pass the identity to the limit. For a locally L² martingale construct on common L² localizers and glue by uniqueness. The energy process ∫H²dA is predictable and increasing; when locally finite, Section 1’s advance localization first makes its expectation finite. Convergence is maximal L² or localized ucp, not almost sure convergence along every grid. The jump identity for general H is completed in Section 4 after constructing the bracket measure, rather than assumed in proving isometry.

## 3. FV Agreement, Decomposition Independence and Associativity

<a id="t-jump-independence"></a>

For an FV path A and bounded predictable H the Stieltjes integral exists pathwise. It is measurable and adapted: verify rectangles, then use the function monotone class for the finite-variation random measure. Its jump is Hₜ∆Aₜ. Localize locally bounded H; for unbounded H use truncation only on the declared domain ∫|H|dVarA locally finite, with dominated convergence against path variation.

Suppose X=M¹+A¹=M²+A² with locally L² martingales, and stop jointly to true L²-martingales. On the predictable sigma-algebra use ρ=E d⟨M¹⟩+E d⟨M²⟩+E[w dVarA¹]+E[w dVarA²], where w=1/(1+VarA¹_T+VarA²_T)>0. The weight need not be predictable: it only defines a finite averaged measure, not a trading rule. Approximate bounded H by the same bounded rectangle-simple Hⁿ in L²(ρ); a subsequence converges almost everywhere for both weighted variation measures. Strict positivity of w and pathwise dominated convergence give uniform convergence of both FV integrals. Isometry gives ucp convergence for both martingale integrals. The total simple integrals agree, so the limits agree indistinguishably.

Stopping follows by the same approximation and the predictable indicator 1_(0,τ]. Associativity holds first for two rectangular H and K. For bounded predictable processes approximate H first, using energy and variation bounds, then K. The required identity ⟨H·M⟩=H²·⟨M⟩ follows for rectangles from conditional squares and for limits from UI and Chapter 30’s uniqueness of predictable decomposition; localize jointly when necessary. Extend unbounded processes only when every integral satisfies its stated energy/variation conditions. In particular this does not assert that every semimartingale-integrable H preserves the local-martingale property of a local-martingale driver. The basic guaranteed domain here is locally bounded predictable H, and the explicitly declared local-martingale energy domain.

The martingale property for integrals of an FV local martingale deserves its own justification. Write D=J−Jᵖ with J of locally integrable variation and stop so E VarJ and E VarJᵖ are finite. For bounded predictable H, dual projection gives E∫1_A1_(s,t]H dD=0 for A∈Fₛ. Integrability follows from total variation, so the integral is a true martingale. Remove the stops and then localize locally bounded H. This proves the needed property without inferring it from the definition of general semimartingale integration.

## 4. Square Sums, Covariation and Jump Identities

<a id="t-jump-quadratic"></a>

First take a bounded martingale M. For any deterministic partition π, M^π equals M at tᵢ on (tᵢ,tᵢ₊₁]. As mesh tends to zero it converges pathwise at every s>0 to Mₛ₋, using strictly past values even when s repeatedly is an endpoint. Constant domination in the finite measure ρ=E d⟨M⟩ gives maximal-L² convergence of the integrals to M₋·M. Squared-increment sums therefore converge ucp to Q=M²−M₀²−2M₋·M. For general L² M stop at amplitude n: left values before the stop remain bounded by n and the integrator is constant afterwards. Apply that bound to the step rules multiplied by 1_(0,τ_n], without treating the terminal overshoot as bounded. Glue for locally L² drivers.

For rational r<s choose partitions containing both endpoints. Then Qₛ−Qᵣ is a probability limit of nonnegative square sums. Countably many exceptional sets and càdlàg paths make Q increasing. For jumps choose an almost surely uniformly convergent subsequence of the integrals. Each simple integral jumps by M^πₜ∆Mₜ; on the same càdlàg path the strictly left-step values tend to Mₜ₋ at every t. Thus the limiting jump is Mₜ₋∆Mₜ and ∆Q=(∆M)². This constructs [M] instead of guessing it from a martingale compensation identity.

For a closed L² martingale, [M]_T is integrable and E[M]_T=E M<sub>T</sub>². First take expectations under the preceding localization and use Fatou for ≤. The local martingale M²−[M] is class D because its bounded stopping values are controlled by the class-D family of M² and integrable [M]_T. It is a true martingale, giving equality. Hence [M]−⟨M⟩ is a martingale of integrable variation. Chapter 30’s duality gives E∫G d[M]=E∫G d⟨M⟩ for every nonnegative predictable G, first bounded and then by monotone convergence.

Now complete the jump identity for any square-energy H. For simple Hⁿ→H, E∑|Hⁿ−H|²(∆M)²≤E∫|Hⁿ−H|²d[M]→0. A summable subsequence makes the weighted square error vanish simultaneously over all jumps, while the integrals converge uniformly almost surely. Thus ∆(H·M)=H∆M simultaneously. The FV case was proved in Section 3.

For an FV process A the bracket is ∑(∆A)²: separate continuous variation and finitely many large jumps. The continuous square sums are bounded by maximal increment times total variation and vanish; small-jump tails are controlled likewise. Mixed sums for N and A converge to ∑∆N∆A: read each large jump and control the rest by dominated convergence in variation, equivalently pass the two left integrals in the discrete product identity using Sections 2–3. Polarize two locally L² martingales and add FV terms to obtain [X,Y] and the product formula. Every limit is ucp, the limit is càdlàg, and its jump is ∆X∆Y.

## 5. Continuous and Purely Discontinuous Martingale Parts

<a id="t-jump-continuous-part"></a>

For an L²-martingale M, terminal values of continuous martingales form a closed Hilbert subspace: Doob gives maximal-L² Cauchy convergence, and a uniformly convergent almost sure subsequence preserves continuity. Projection gives M=C+D. For A∈Fₛ and any continuous L²-martingale Z, the process 1_A times the difference between Z stopped at t and at s is still a continuous L²-martingale, with terminal value orthogonal to D<sub>T</sub>. Expand the conditional product and use the martingale property of D to get E[1_A(DₜZₜ−DₛZₛ)]=0. Thus D is strongly orthogonal to every continuous martingale, and localization covers continuous local martingales.

We must further prove that D’s quadratic variation comes entirely from jumps. For ε>0 take J^ε=∑∆M1_{|∆M|>ε}, its projection A^ε and D^ε=J^ε−A^ε. Initially this is an FV local martingale of locally integrable variation. Its mixed quadratic variation with a continuous martingale vanishes. The product formula makes D^ε strongly orthogonal: one term is a continuous martingale integral, and the other is a predictable integral of an FV martingale, whose zero mean follows from dual projection.

Expand the squared jumps of D^ε and apply projection under common integrable localization. This gives E|D^ε_T|²=E∑(∆M)²1_{|∆M|>ε}−E∑(∆A^ε)², bounded by E[M]_T. Fatou first supplies the bound; bounded expected squares and maximal estimates then make D^ε a true L²-martingale, so the expansion holds on the whole interval. For two truncations the squared L² terminal distance is bounded by the corresponding squared-jump tail, which vanishes as both cutoffs tend to zero. Thus D^ε converges in maximal L² to D⁰, still strongly orthogonal.

Conditional fairness at predictable times gives ∆A^ε=−E[∆M1_{|∆M|≤ε}|F₋]. Conditional Jensen summed over all predictable compensator jump graphs gives E∑(∆A^ε)²≤E∑(∆M)²1_{|∆M|≤ε}→0. The omitted tail of actual M jumps also vanishes. Along a summable subsequence all jumps of D^ε tend to those of M, while uniform process convergence gives ∆D⁰=∆M. Therefore M−D⁰ is continuous. Projection uniqueness identifies it as C and D⁰ as D.

Quadratic variation passes through this L² limit. If Kⁿ→K in maximal L², first stop at bounded maxima. Expand ∫Kⁿ₋dKⁿ−∫K₋dK into a bounded integrand against the driver difference and a vanishing integrand against the fixed driver. Isometry and dominated convergence under bounded clocks give ucp convergence of both. Maximal-L² convergence controls the probability of discarded stops. Hence [Kⁿ]→[K] ucp. For D^ε the FV bracket is its squared-jump sum. The preceding tail and compensator-jump L² bounds and Cauchy–Schwarz make these sums converge in L¹ total variation to ∑(∆M)². Thus [D]=∑(∆M)². Strong orthogonality makes [C,D] a continuous FV local martingale and hence zero.

Glue by stopping for locally L² processes. For general M use Section 1’s M=L+D; its FV martingale D is strongly orthogonal to continuous martingales and has a pure-jump bracket, so the continuous component is independent of the decomposition. Two candidate continuous components differ by a continuous local martingale strongly orthogonal to itself; its bracket vanishes, so it is constant. For X=N+A, finite variation contributes no continuous quadratic variation. Thus Xᶜ=Nᶜ and C=[Xᶜ] are decomposition-independent. Finite variation may alter actual jumps but cannot supply a continuous martingale component.

Stopping is compatible with this projection. If D is strongly orthogonal to every continuous local martingale, the stopped product identity gives [D stopped at τ,Z]=1_(0,τ]·[D,Z]=0. The stopped D is still strongly orthogonal and the stopped C continuous, so uniqueness makes the L² local windows agree. For locally bounded H, H·D^ε remains an FV local martingale and hence orthogonal to continuous martingales; so does its local L² limit H·D. The integral H·C is continuous. Thus (H·M)ᶜ=H·Mᶜ. Chapter 31 gives the bracket transformation on continuous components and Section 4 the simultaneous jump identity, yielding [H·X,K·Y]=HK·[X,Y]. Start bounded and then localize jointly. This transformation was not used to construct the continuous/purely discontinuous decomposition.

## 6. Existence and Atoms of a Jump Compensator

<a id="t-jump-compensator"></a>

Take marks E=Rᵈ without zero and w(x)=1∧|x|². Sections 4–5 make w∗μ finite on compact paths. Every jump is at most one, so stopping at the first total of n bounds it by n+1 and makes its expectation finite. Work first on this finite-T window and let A be Chapter 30’s dual predictable projection of w∗μ. Define m(G)=E∫1_G w(x)μ(ds,dx) on the product of the predictable sigma-algebra and Borel(E). Its time-sample marginal is λ(dω,ds)=P(dω)dAₛ.

Chapter 10’s conditional-kernel construction requires standard Borel marks, not a standard Borel predictable base. Normalize finite m, condition the mark on the base sigma-algebra of the product, and use Chapter 10’s measurable factorization to obtain K(ω,s,dx). If m has total zero choose a fixed probability kernel. Choose a fixed mark on λ-null exceptional sets too, so K is a probability at every base point. Define

\[ \nu(\omega;ds,dx)=w(x)^{-1}K(\omega,s,dx)\,dA_s(\omega),\qquad w*\nu=A. \]

Predictability of kernel integrals holds first for time-mark rectangles and then for every nonnegative rule by the function monotone class. Pathwise measures are kernel products with Stieltjes measure. Disintegration of m gives E W∗μ=E W∗ν for every nonnegative predictable W, allowing infinity. On overlapping windows, use a countable generating family of bounded mark functions g supported away from zero. The processes g∗ν and g∗ν′ are dual projections of the same FV process and agree indistinguishably by Chapter 30. Rational times and a countable mark π-system give one exceptional set; measure uniqueness and monotone convergence identify the pathwise random measures. This glues all windows and proves uniqueness.

For predictable S test U1_{t=S}g(x), with nonnegative F<sub>S-</sub>-measurable U and nonnegative Borel g. This gives ∫g(x)ν({S},dx)=E[g(∆X<sub>S</sub>)1_{∆X<sub>S</sub>≠0}|F<sub>S-</sub>]. Choose versions simultaneously on a countable mark generator and extend to all Borel sets. Thus every time atom of ν has total mass at most one. All atoms are covered by countably many predictable jump graphs of increasing w∗ν, so the bound holds at every time off one common null set. These atoms cannot be dropped in compensated integration.

## 7. Random Marked Integration with Atomic Correction

<a id="t-jump-marked-integral"></a>

First let W be a bounded simple predictable rectangle rule on finite time and a bounded mark band away from zero. Localize to finite expected ν-mass there. J=W∗μ has integrable variation, W∗ν is its dual projection, and N=J−W∗ν is an FV local martingale. Its jump is the actual mark value minus hats, where hats=∫W(s,x)ν({s},dx). Section 6’s atomic mass bound gives hats²≤∫W²ν({s},dx).

\[ E[N]_T=E(W^2*\mu)_T-2E\sum_{s\le T}W(s,\Delta X_s)\mathbf1_{\{\Delta X_s\ne0\}}\widehat W_s+E\sum_{s\le T}\widehat W_s^2=E(W^2*\nu)_T-E\sum_{s\le T}\widehat W_s^2. \]

The cross expectation uses compensation for the predictable rule W times hats; Cauchy–Schwarz and the preceding bound give absolute integrability. Compute first under localization and use Fatou for a uniform second-moment bound. N becomes a true L²-martingale, and Section 4 gives E N<sub>T</sub>²=E[N]_T. Thus the formula is exact, but not an uncorrected ν-energy isometry. Only an atomless-in-time ν removes the correction.

If E W²∗ν is finite, rectangle-simple rules are dense under a finite control measure: truncate time, marks and energy, then use Section 2’s monotone-class argument. The terminal squared error is at most E|Wⁿ−W|²∗ν; Doob yields maximal-L² convergence and a unique càdlàg integral. The hats map contracts from L²(ν) to the L² sum over time atoms. Both the atomic formula and squared errors on actual jumps converge; a summable subsequence gives the process-level jump identity. The resulting seminorm may vanish although ν-energy does not, as for W=1 at an event certain to occur at a fixed time.

The local square ν-energy process is predictable and increasing. Section 1’s advance localization makes its expectation finite; uniqueness gives stopping and gluing. The integral is a purely discontinuous local martingale: finite truncations are FV local martingales, hence strongly orthogonal to continuous martingales, and local L² limits preserve this. Large marks with locally integrable |W|∗ν may instead be integrated as actual sum minus compensation, an FV local martingale without an L² claim. If even a large-jump mean does not exist, keep only its finite actual sum. No maximal domain of every possible integrable function is constructed here.

## 8. Canonical Decomposition and Truncations

<a id="t-jump-characteristics"></a>

First prove that a locally bounded semimartingale Y is special. Write Y=M+A and stop to bounded Y and integrable M∗, then stop VarA at its first crossing of n. Its overshoot is at most |∆Y|+|∆M|, controlled by bounded Y and integrable M∗, so stopped VarA has finite expectation. Dual-project A to B. Then L=M+A−B is a local martingale and B predictable FV. Uniqueness follows because a predictable FV local martingale is constant: Section 1 first makes variation integrable, then Chapter 30 applies. Bounded-jump Y can first be amplitude-stopped to become locally bounded, so the same conclusion holds.

Take bounded h agreeing with x near zero and put Y=X−(x−h)∗μ. The large-jump remainder is a finite actual sum, and Y has bounded jumps h(∆X). Write Y=X₀+L+B. At predictable S, ∆B<sub>S</sub>=E[h(∆X<sub>S</sub>)1_{∆X<sub>S</sub>≠0}|F<sub>S-</sub>]=hat h<sub>S</sub>. Thus L has jumps bounded by 2||h||∞ and is locally L². Since h²≤K(1∧|x|²), Section 7 constructs h∗(μ−ν), purely discontinuous with exactly the jumps of L. Their difference is continuous and equals the unique Xᶜ. This proves the canonical formula without assuming a Poisson representation property.

For another truncation g, g−h is bounded and zero near zero, so its ν integral is locally finite. Expanding g∗(μ−ν)+(x−g)∗μ gives the h expression minus (g−h)∗ν; B must therefore increase by (g−h)∗ν. C and ν do not change. This is Chapter 27’s drift-sign rule, now also valid atom by atom. For a locally L²-martingale itself, C+x²∗ν is its angle bracket: square-integrable localization, compensation and the formula for M² identify the predictable compensator. At predictable times hat x=E∆M|F₋=0, so no additional squared mean remains. Polarization gives C^{ij}+xᵢxⱼ∗ν in several dimensions.

## 9. Taylor Limits with Jumps

<a id="t-jump-ito"></a>

For one-dimensional f∈C² first localize X and the martingale, variation and square clocks in its decomposition. The first two derivatives are bounded on the required compact set and the second is uniformly continuous. Refine deterministic partitions. Taylor gives f′ at the left value times ∆X, half f″ times ∆X², and a remainder. The remainder must not be asserted to vanish on intervals containing large jumps.

Fix ε>0. There are finitely many jumps with |∆X|>ε on a compact window. Fine partitions separate them; interval endpoints converge to actual left and right values, yielding exact function differences there. Off these finitely many intervals a finite step approximation of the càdlàg path bounds oscillation by a constant times ε. The sum of absolute Taylor errors is then bounded by the modulus of continuity of f″ times the square-increment sum. Section 4 makes these sums ucp-tight, so the error vanishes when mesh tends to zero before ε does. Read large jumps individually. The small-jump tail is controlled by ∑|∆X|²<∞ and |R<sub>f</sub>|≤K|∆X|², giving absolute, compact-uniform convergence of the full jump-remainder series.

Left first-order sums converge to f′(X₋)·X by Section 3. Weighted quadratic sums require more than convergence of an unweighted terminal value. Approximate the weight by finite steps on pieces of oscillation at most ε; the error is its modulus of continuity times the quadratic sum. Such pieces come from finite step approximation of a càdlàg path, with endpoints read using deterministic grids. Each isolated large jump contributes f″(Xₛ₋)(∆Xₛ)², while the remaining jump tail is controlled by its square sum. Refine the grid first, then the finite step approximation, and let ε decrease. Section 4’s ucp convergence of cumulative square sums yields the continuous Stieltjes part plus all jump terms, namely ∫f″(X₋)d[X]. Move each jump’s half quadratic contribution into the remainder to obtain the formula using the continuous part of [X]. Choose almost surely uniform subsequences simultaneously at rational horizons; càdlàg paths make the identity indistinguishable as processes. No additional universal convergence along arbitrary random partitions is asserted.

In several dimensions use second-order multivariate Taylor off the same finite set of large jumps. The error is controlled by |∆X|² and matrix terms by polarization. For time-space f∈C¹,² change time and then space. Time increments converge against continuous dt; uniform continuity of fₜ on localized compact sets times total elapsed time controls mixed grid errors, without demanding a second time derivative. Time itself does not jump, so the remainder is exactly f(s,Xₛ)−f(s,Xₛ₋)−∇f(s,Xₛ₋)·∆Xₛ. Functions here are defined on all time-space; for an open domain stop separately where both pre- and post-jump values remain in that domain.

This localization never treats the exit overshoot as bounded. First take a smooth cutoff f<sub>K</sub> equal to f on [−K,K] with bounded derivatives, and prove the deterministic-grid identity for f<sub>K</sub>. Before exit both functions and derivatives agree; at exit read the full jump difference separately, which gives the correct terminal value of f rather than f<sub>K</sub>. Every càdlàg path is bounded on a compact window, so for sufficiently large K that window has no exit. Remove the cutoff. Use compact balls and smooth cutoffs in several dimensions.

## 10. Stochastic Exponentials, Signs and Linear Uniqueness

<a id="t-jump-exponential"></a>

Let L be a semimartingale with L₀=0. Its compact-window small jumps satisfy ∑(∆L)²<∞, and |log(1+z)−z|≤Kz² for |z|≤1/2. The logarithmic corrections therefore converge absolutely and uniformly on compact intervals; larger jumps are finite in number. Without a jump of −1 use log|1+z| for finitely many negative factors and record their signs by an FV product R. This defines the main product formula as a semimartingale: its absolute value is the ordinary exponential of a semimartingale plus FV, and R is FV. Jump Itô and products were already proved.

Substitution cancels the exponential’s continuous second-order term against −[L]ᶜ/2. Every logarithmic jump correction gives ∆Z=Z₋∆L, so dZ=Z₋dL. At a jump of −1 set Z to zero permanently; the equation still holds. Otherwise K=−L+[L]ᶜ+∑(∆L)²/(1+∆L) is a semimartingale: the small-jump series is absolutely summable, while compact windows have finitely many larger jumps with nonzero denominators. Its jump is −∆L/(1+∆L) and its continuous covariation with L is −[L]ᶜ. Hence L+K+[L,K]=0, and the product formula yields 𝓔(L)𝓔(K)=1.

The same product calculation makes any linear solution times the inverse exponential constant at its initial value, proving pathwise uniqueness on intervals without jumps of −1. Such jumps are finite in number on compact windows. Each kills a difference of solutions too; restarting the inverse argument from zero on the next interval proves uniqueness throughout. For U,V use associativity and bracket transformation, first for rectangles and then by Sections 2–4’s local limits. The product 𝓔(U)𝓔(V) solves the linear equation driven by U+V+[U,V]; uniqueness gives the exponential product identity. All identities are indistinguishable process identities. Strict positivity, zero and sign reversals are determined by 1+∆L. A general semimartingale exponential is not called a true martingale.

## 11. Complete Increment Checks for Davis Potentials

<a id="t-jump-davis"></a>

This section is deterministic algebra, without assuming a probabilistic inequality. For a finite real sequence starting at x₀=0, let q be the accumulated squared increments and m the running absolute maximum, so |x|≤m. An increment d gives q′=q+d² and m′=m∨|x+d|. Assign zero at a zero denominator and define

\[ h(x,m,q)=\frac{x}{\sqrt{m^2+q}},\quad F(x,m,q)=-5\sqrt q+\sqrt{m^2+q}-\frac{m^2-x^2}{2\sqrt{m^2+q}},\quad G(x,m,q)=-2m+\sqrt{m^2+q}+\frac{m^2-x^2}{2\sqrt{m^2+q}}. \]

We prove two increment bounds. Deliberately loose constants simplify boundary calculations. The method is inspired by pathwise Davis potentials, but all algebra is supplied below. The case m=0 follows by continuous extension. For m>0 normalize m=1 by homogeneity, and use simultaneous sign symmetry of x,d to assume d≥0. Write r=√(1+q).

\[ F(x+d,m^\prime,q^\prime)-F(x,m,q)\le hd+(\sqrt{q^\prime}-\sqrt q),\qquad G(x+d,m^\prime,q^\prime)-G(x,m,q)\le-hd+2(m^\prime-m). \]

First verify F. Without a new maximum, d≤2. The smallest feasible z=(x+d)² is zero for d≤1 and (d−1)² for 1≤d≤2. Let K be left side minus right side. The coefficient of (x+d)² is (1/√(r²+d²)−1/r)/2≤0, so K is bounded by its value at z. That value is exactly the integral from zero to d² of the following derivative, with y=q+s.

\[ \frac1{\sqrt{1+y}}+\frac{1-s+d^2-z}{4(1+y)^{3/2}}-\frac3{\sqrt y}\le\frac{y+2}{(1+y)^{3/2}}-\frac3{\sqrt y}\le0. \]

The first bound uses 1+d²−z≤4. The final bound holds even with 3/2 instead of 3, since squaring gives 9(1+y)³−4y(y+2)²=5y³+11y²+11y+9≥0. At y=0 use the corresponding integrable improper integral. Its starting value is zero, proving K≤0.

With a new maximum x+d≥1, the derivative of K in x is (x+d)(1/√((x+d)²+q+d²)−1/r)≤0. For d≤2 the maximum occurs at x=1−d, the preceding boundary. For d>2 it occurs at x=−1, giving K=√(r²+2d²−2d)−r+d/r−6(√(q+d²)−√q). If q≥d², concavity bounds the first part by d²/r and √(q+d²)+√q≤(√2+1)r, so K≤0. If q<d² the first part is at most (√2+1)d, while the final part is at least 6(√2−1)d. Their difference is (7−5√2)d<0. This proves F’s bound.

For G without a new maximum, left side plus hd is a convex quadratic in x. Check only x=−1 and x=1−d. The latter gives √(r²+d²)−r−d²/(2r)≤0. The former is equivalent to √(r²+d²)+(d−d²/2)/√(r²+d²)≤r+d/r for 0≤d≤2. Positive cross multiplication and squaring give the difference d³(1−d/4)+d⁴/r²≥0, proving it.

With a new maximum, left side minus right side is −4(x+d−1)+√((x+d)²+q+d²)−r−(1−x²)/(2r)+xd/r. It is convex in x, so check the feasible endpoints. At x=1 the norm triangle inequality bounds it by (√2−3)d≤0. The lower endpoint for d≤2 is x=1−d, already checked. For d≥2 it is x=−1, giving −4(d−2)+√(r²+2d²−2d)−r−d/r. This is convex in d with increasing derivative tending to −4+√2−1/r<0. It decreases for d≥2, starting nonpositive at d=2 by the preceding boundary case. This proves G’s bound.

Finally F≥m/2−5√q and G≥√q−2m, with both initially zero. Summing increments yields the pathwise Davis bounds, with |h|≤1.

\[ \sqrt{[x]_n}\le4x_n^*-(h\cdot x)_n,\qquad x_n^*\le12\sqrt{[x]_n}+2(h\cdot x)_n. \]

## 12. From Davis to BDG for Every p≥1

<a id="t-jump-bdg"></a>

Sample a continuous-time local martingale on deterministic dyadic grids. Section 4 gives the ucp square-sum limit and the grid maxima converge to the true maximum. The simple coefficients h^π approach hₛ=Mₛ₋/√([M]ₛ₋+(M∗ₛ₋)²) from the left. If the denominator is zero, every past value of M, hence every grid numerator, is zero. Elsewhere càdlàg paths and a uniform square-sum subsequence give pointwise convergence. Since |h^π|≤1, dominated convergence under Section 3’s joint control measure gives ucp convergence to h·M. The pathwise Davis bounds therefore hold for càdlàg local martingales. Localize h·M to true martingales before taking expectations; Fatou and nonnegative bounds give E√[M]≤4EM∗ and EM∗≤12E√[M], including infinite values and stopping. BDG was not used to prove integral continuity.

For σ≤T apply the bounds to 1_A1_(σ,t]·M for A∈Fσ. This yields conditional Davis bounds E[√([M]_T−[M]_σ)|Fσ]≤8E[M∗_T|Fσ] and E[M∗_T−M∗_σ|Fσ]≤12E[√[M]_T|Fσ]. The factor two in the first uses maximal displacement from a new origin at most 2M∗. Testing Fσ-events proves this without assuming regular conditional probabilities on an arbitrary sample space.

The following threshold lemma handles overshoots. Let A be increasing càdlàg with A₀=0, J≥sup∆A, and E[A<sub>T</sub>−Aσ|Fσ]≤E[B|Fσ] at every σ≤T, where B,J≥0. At the first τλ with A>λ, Aτλ≤λ+J. Condition on {τλ≤T}, multiply by λ^{p−2} and integrate. Tonelli and the tail-integral identity give

\[ EA_T^p=p(p-1)\int_0^\infty\lambda^{p-2}E(A_T-\lambda)^+d\lambda\le pE[(B+J)A_T^{p-1}],\qquad\|A_T\|_p\le p\|B+J\|_p\quad(p>1). \]

Apply first to A∧n so the left side is finite, use Hölder and let n increase. The boundary A<sub>T</sub>=λ is irrelevant under λ integration; monotonicity and adapted paths verify stopping of the first passage. For A=√[M], the largest jump is at most 2M∗, and B=8M∗ gives ||√[M]||p≤10p||M∗||p. For A=M∗, the largest jump is at most √[M], and B=12√[M] gives ||M∗||p≤13p||√[M]||p. The preceding paragraph gives p=1 directly, so the main constants can uniformly be c<sub>p</sub>=(10p)⁻ᵖ and C<sub>p</sub>=(13p)ᵖ. For an unbounded endpoint take T∧n and use monotone convergence.

For 0<p<1 the general upper bound fails. For unit Poisson M=N−t on [0,ε], no arrival gives E(M∗)ᵖ≥e⁻ᵋεᵖ. But E Nε^{p/2}≤E Nε=ε because k^{p/2}≤k for integers k≥1. The ratio diverges. Applying BDG to an integral requires a local-martingale integral and the established bracket transformation; FV drift of a general semimartingale cannot simply be included on BDG’s martingale side.

## 13. Good Integrators: The Forward Direction and Rao’s Converse Version

<a id="t-jump-good-integrator"></a>

The good-integrator test asks that for simple predictable Hⁿ bounded on [0,T] by deterministic ε_n→0, the maximum of Hⁿ·X tends to zero in probability. For X=N+A first stop N to L². Doob gives P((Hⁿ·N)∗>η)≤4ε_n²E⟨N⟩_T/η², while the FV part is bounded pathwise by ε_nVarA_T. Fix localization before removing it to prove the property. Stopping and grid insertion also equate terminal and ucp tests: stop at a first excessive amplitude and approximate its predictable stochastic interval by simple rules.

The general Bichteler–Dellacherie theorem says that an adapted càdlàg process passes this test exactly when it is a semimartingale. The difficult converse is not hidden in a definition: constructing suitable local conditional-variation control from probability-bounded simple integrals requires an additional long proof. That classical characterization is cited here but not used in any construction or deduction. What is actually proved below is the finite-conditional-variation version, not the general converse.

Let X be integrable at every time and càdlàg, with the main text’s finite total conditional variation V. On a countable dense time set in [0,T], define Vₜ as the essential supremum, over finite partitions from t to T, of the conditional expectation of the absolute conditional-mean increments plus |X<sub>T</sub>|. Common refinement directs this family upwards because conditional Jensen increases expected variation. Finite total variation gives E Vₜ≤V. An increasing sequence of partitions realizes the essential supremum: select expectations approaching their supremum, take common refinements and apply monotone convergence to obtain the least upper bound.

\[ V_t\ge|X_t|,\qquad V_s\ge E[V_t\mid\mathcal F_s]+|E[X_t-X_s\mid\mathcal F_s]|\quad(s<t). \]

The first bound follows by telescoping conditional means and Jensen. For the second prepend [s,t] to later partitions and let them attain the supremum. Hence V±X are nonnegative supermartingales on the dense time set. Chapter 15’s upcrossing argument and bounded means give all one-sided limits; take right limits. Usual conditions give adaptation, conditional Fatou preserves supermartingale inequalities, and càdlàg X keeps their difference equal to 2X. Retain the specified endpoint T; the dense-time left limit gives càdlàg paths. We obtain nonnegative càdlàg supermartingales S⁺,S⁻ with X=(S⁺−S⁻)/2.

A nonnegative càdlàg supermartingale is locally class D. Stop at its first crossing κ of amplitude n. Stopping values are dominated by n+Sκ+S₀; discrete sampling and Fatou give E Sκ≤E S₀, a genuine integrable domination. The crossings tend to infinity; on finite horizons localize within the terminal interval or combine integer extensions. Apply Chapter 30’s local Doob–Meyer to −S⁺ and −S⁻. Their difference gives X as a local martingale plus predictable FV. Uniqueness of predictable FV decomposition glues localizers. This proves the stated Rao version, not the general good-integrator converse or an arbitrary sigma-martingale theory.

## 14. A Brownian Functional Limit for Martingales with Jumps

<a id="t-jump-fclt"></a>

The theorem uses the sufficient conditions stated in the main text. Mⁿ starts at zero and is a d-dimensional locally L²-martingale. On every finite T its angle-bracket matrix tends ucp to Σt for fixed symmetric nonnegative Σ, and E∫|x|²1_{|x|>ε}νⁿ→0 for every ε>0. Here νⁿ is this chapter’s compensator of Mⁿ’s jumps, not a guessed intensity. The conclusion holds in finite-window J₁ and half-axis local J₁. T-J1’s established topology and tightness results are inputs; their independent human final-review status is not upgraded by this use.

First remove large jumps. Choose ε_n↓0 diagonally so b<sub>n</sub>=E∫|x|²1_{|x|>ε_n}νⁿ→0 and put Rⁿ=x1_{|x|>ε_n}∗(μⁿ−νⁿ). Section 7 and Doob give E(Rⁿ∗)²≤4b_n. At predictable atoms the local martingale has conditional mean zero, so the conditional large-jump mean is the negative small-jump mean and has norm at most ε_n. Thus Yⁿ=Mⁿ−Rⁿ has jumps bounded by 2ε_n and unchanged continuous component.

Check angle brackets rather than formally subtracting ucp limits. Let Aⁿ be the trace angle bracket of Mⁿ and Bⁿ its large-jump square ν-energy. Each atom satisfies ∆Aⁿ≤ε_n²+∆Bⁿ because ν’s atomic mass is at most one. Stop when Aⁿ first reaches K; then E Aⁿ_stopped(T)≤K+ε_n²+b<sub>n</sub>. The stopped angle bracket of R has expectation at most b<sub>n</sub>. Cauchy–Schwarz for covariation measures bounds the expected cross total variation by √((K+ε_n²+b<sub>n</sub>)b<sub>n</sub>). The identity ⟨Y⟩=⟨M⟩−⟨M,R⟩−⟨R,M⟩+⟨R⟩ now makes the matrix difference vanish ucp. For K>traceΣ·T the original stop is used with probability tending to zero. Thus ⟨Yⁿ⟩→Σt without stopping as well.

Next stop Y when its own trace angle bracket first reaches K>traceΣ·T+1. Since jumps are at most 2ε_n, bracket atoms are at most 4ε_n² and the whole stopped trace is bounded by K+4ε_n². Y is a true L²-martingale with E(Y∗)²≤4(K+4ε_n²), and this stop has vanishing probability. For stopping times σ≤τ≤σ+δ≤T, closed-martingale sampling and square compensation give E|Yτ−Yσ|²=E(Aτ−Aσ). Bounded ucp convergence of the brackets to deterministic Σt also gives L¹ convergence of their maximal difference. Thus the bound is traceΣ·δ+o(1). Aldous gives tightness, and vanishing maximum jumps make every limit continuous. Apply coordinatewise and use compact sets of continuous paths for vector C-tightness, without identifying coordinate J₁ with a common vector time change at discontinuous limits.

Identify a subsequential limit Z. For f(y)=exp(iu·y), jump Itô and compensation show that f(Yₜ)−1 minus one half ∑∫fᵢⱼ(Yₛ₋)d⟨Yⁱ,Yʲ⟩ₛ is a martingale plus an error whose expected total variation vanishes. Its bound is K<sub>u</sub> ω_u(2ε_n)(K+4ε_n²), from the exact jump difference minus the quadratic term. The compensated remainder is a true martingale because its square ν-energy is bounded by a constant times ε_n² times total square energy. The first-order integral is also true, with bounded integrand and bracket. Bounded derivatives of f avoid any unproved higher-moment UI assumption.

The joint bracket limit is deterministic and continuous. Chapter 24’s common representation is used only to verify continuity of the limiting integral. Paths converge uniformly there, brackets converge uniformly and total variation is controlled by the trace. Approximate continuous fᵢⱼ(Z) by finite step functions, then use uniform convergence to pass the Stieltjes integrals. Deterministic bounds allow multiplication by bounded continuous functions of finitely many past coordinates and passage of expectations. π–λ extends to all past information. The limit satisfies the martingale identity below.

\[ e^{iu\cdot Z_t}-1+\frac{u^\top\Sigma u}{2}\int_0^t e^{iu\cdot Z_s}\,ds\quad\text{is a martingale}. \]

Conditioning on Fₛ and using Fubini gives a bounded Volterra equation. Its unique solution is E[e^{iu·Zₜ}|Fₛ]=e^{iu·Zₛ}exp(−uᵀΣu(t−s)/2): integral iteration makes the difference of two solutions zero, or solve with a deterministic exponential factor. Chapter 14’s uniqueness of characteristic functions gives successive independent Gaussian increments. Continuity gives Brownian motion of covariance Σ. No general martingale-problem uniqueness theorem is used. All subsequences have the same limit; removal and stopping errors vanish ucp, so Mⁿ converges. Diagonal tightness over integer T, compatible continuous finite-window limits and Chapter 24’s local J₁ structure yield the half-axis result.

### References and Scope

For the idea of Davis potentials see the [Beiglböck–Siorpaes author paper](https://arxiv.org/abs/1305.6188); this page changes constants and supplies the boundary calculations. For general good-integrator characterization see [the modern author proof of Beiglböck–Schachermayer–Veliyev](https://arxiv.org/abs/1004.5559). Its general converse is not reproduced here. Compare functional martingale limits with [Whitt’s author paper](https://arxiv.org/abs/0712.1929); Section 14 actually proves the stated sufficient conditions, truncation and exponential identification. Mathematical facts, modern teaching reconstructions and original historical contributions are kept distinct.
