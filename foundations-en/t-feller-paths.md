# T-FELLER-PATHS: From Positive Operators to Paths and Strong Markov

Let E be a nonempty locally compact Polish space. We first construct subprobability kernels from a positive contraction C₀ semigroup. The path and strong Markov theorem explicitly assumes conservativity. The proof uses established measure tools, Chapter 8 extension, Chapter 15 discrete martingales and reverse conditional expectations, Chapter 24 Polish tightness, and T-OPERATORS.

## P.1 Cutoffs, Compactification and Countable Observables

<a id="t-feller-topology"></a>

Local compactness and a countable base give a countable relatively compact open cover. Closures of finite unions give a compact exhaustion whose interiors cover E. For compact F inside relatively compact open U, the following continuous compactly supported function equals one on F and zero outside U. Finite maxima over the exhaustion give increasing 0≤χₘ≤1 tending to one and eventually equal to one on each compact set.

\[
\chi_{F,U}(x)=\frac{d(x,E\setminus U)}{d(x,E\setminus U)+d(x,F)}.
\]

The denominator is nonzero; if E is compact and U=E use the constant one. Adjoin Δ with complements of compact sets as its neighborhoods, obtaining compact Hausdorff K. An open cover’s member containing Δ leaves a compact remainder, proving compactness; relatively compact neighborhoods separate Δ from other points. Countably many pairs of basis sets with compact closure inside a relatively compact basis set provide separating cutoffs, also separating Δ, where they vanish. The resulting map into a countable cube is continuous and injective; a compact-to-Hausdorff inverse is continuous. Thus K is compact metrizable.

C₀(E) identifies with the closed subspace of C(K) vanishing at Δ. C(K) is separable: use finite minima of functions qᵢ+L d(x,xᵢ), with rational heights, positive integer L and centers from a countable dense set. Uniform continuity first gives approximation by the lower envelope for large L; then finite dense nets and rational heights suffice. This is a countable approximating family. Subspaces are separable, and taking positive parts gives a countable dense family (fⱼ) in the positive cone of C₀.

## P.2 The Bounded Positive Representation Actually Needed

<a id="t-feller-riesz"></a>

On compact metric K take a positive functional ℓ and M=ℓ(1). Positivity gives ‖ℓ‖=M; M=0 is trivial. Cover K by finitely many balls with radii tending to zero and form a continuous partition of unity ψᵢ supported there, choosing anchors xᵢ in the balls. Distances to ball complements, normalized by their positive sum, construct the partition explicitly. Define discrete probabilities as follows.

\[
\mu_n=M^{-1}\sum_i\ell(\psi_i)\delta_{x_i},\qquad\left|\int f\,d\mu_n-M^{-1}\ell(f)\right|\le\omega_f(2/n).
\]

Compactness and Chapter 24’s Prokhorov theorem give a weakly convergent subsequence with limit μ. The estimate identifies its integral for every continuous f, yielding ℓ(f)=M∫f dμ. For uniqueness, approximate a closed-set indicator by max(0,1−n d(x,F)) decreasingly. Dominated convergence identifies closed-set masses; π–λ gives equality on all Borel sets.

For general E let L be bounded positive on C₀ with M=‖L‖. Extend to C(K) by ℓ(f+c)=Lf+cM, where f(Δ)=0. If f+c≥0 then c≥0 and f⁻≤c, so Lf≥−cM and the extension is positive. Let μ be its representing finite measure. The cutoffs satisfy Lχₘ↑M: for 0≤f≤1, fχₘ→f uniformly and L(fχₘ)≤Lχₘ; take the supremum over f. Hence μ(E)=M=μ(K), leaving no atom at Δ. Its restriction is the unique representation on E.

This is the bounded finite-measure version. Distance cutoffs give closed inner approximation of open sets; complements give open outer approximation of closed sets. Sets admitting both approximations form a σ-algebra: complements interchange them; for countable unions distribute outer errors as ε times 2 to the negative n, and truncate to a finite union before inner approximation, controlling the remainder by finite total mass. Thus all Borel sets are regular. Intersect closed inner approximations with the fixed compact exhaustion and control the tail by finite mass to obtain compact inner approximation, hence Radon regularity. General locally finite functionals or random-measure theory are not claimed here.

## P.3 Kernel Measurability and Chapman–Kolmogorov

<a id="t-feller-kernel-proof"></a>

Apply the representation to Tₜ and x to get a unique Pₜ(x,·) of mass at most one. For open U, multiply χₘ by min(1,m d(x,Uᶜ)) to approximate its indicator increasingly; for U=E use χₘ. Thus Pₜ(x,U) is a limit of continuous Tₜfₘ(x). The measurable-set class is closed under complements and disjoint countable unions, the latter by countable additivity and measurable sums, so it is a λ-system. Complements use Pₜ(x,E) without assuming it is one. Open sets form a π-system, hence π–λ gives all Borel sets.

Strong continuity and spatial continuity give joint continuity of (t,x)↦Tₜf(x). The same approximation makes Pₜ(x,B) jointly Borel. The composed subprobability PₛPₜ integrates C₀ functions to TₛTₜf=Tₛ₊ₜf. Uniqueness gives the kernel Chapman–Kolmogorov law, including the identity kernel at zero.

## P.4 Rational Supermartingales and Common Side Limits

<a id="t-feller-regularization"></a>

Assume now Pₜ(x,E)=1. Chapter 8 extension gives a raw coordinate process X for every initial law π. From the countable positive dense family use all Rₙfⱼ for positive integer n. Since nRₙf→f uniformly, these observations separate points of K. For h=Rₙfⱼ, the bounded nonnegative process e⁻ⁿᵗh(Xₜ) is a supermartingale: its semigroup action removes an initial nonnegative integral.

\[
e^{-ns}T_sR_nf=R_nf-\int_0^s e^{-nr}T_rf\,dr\le R_nf.
\]

Fix an integer window [0,N] and nested finite grids exhausting its rational times. Apply Chapter 15’s crossing bounds to the negative supermartingale for upcrossings and to the supermartingale for downcrossings. Boundedness bounds expected crossings of any rational threshold interval independently of the grid. Monotone convergence makes the total finite. Intersect over observations, rational thresholds and N to obtain one event of probability one.

If a rational side limit failed at any real t, distinct upper and lower cluster values would force infinitely many crossings of a rational interval between them, a contradiction. Continuous exponential factors do not affect side-limit existence. Compact K provides state cluster points, and separation makes them unique. We have not intersected uncountably many probability-one events; finite crossings control all t simultaneously.

## P.5 Compact Containment Excludes Infinity

We must still exclude Δ at random times. For positive α and cutoffs χₘ put gₘ=αRαχₘ. It belongs to C₀, lies between zero and one, and by conservativity increases pointwise to one. Uq=1−e⁻ᵅqgₘ(Xq) is a nonnegative submartingale. Add T to each finite rational grid and apply the maximal inequality. Take 0<δ<1. A value gₘ<δ implies U>1−δ, giving the upper bound below.

\[
P_\pi\!\left(\inf_{q\in\mathbb Q\cap[0,T]}g_m(X_q)<\delta\right)\le\frac{1-e^{-\alpha T}E_\pi g_m(X_T)}{1-\delta}.
\]

Choose α small and then m large, making the bound arbitrarily small; Kₘ={gₘ≥δ} is compact. Choose compact sets for errors tending to zero and take finite unions Hⱼ increasing. The probability that the whole rational path is not contained in Hⱼ tends to zero, so almost surely some Hⱼ contains it. All side cluster points remain inside, excluding both values and left limits escaping to Δ and returning. Intersect over integer T. The deterministic compact sets may depend on π and T, not on the sample; the eventual containing index j depends on the path. The assertion is almost-sure finite-time compact containment for each π.

## P.6 An Actual Càdlàg Modification and a Measurable Family

Enumerate the separating observations hⱼ. The metric below is compatible with the compactification topology: the continuous injection into a countable product has a compact image and continuous inverse. Taking rational right limits of each scalar function gives a right-continuous function with left limits. If right continuity failed, choose tₖ decreasing to t and nearby rational qₖ approximating those right-limit values; this contradicts the existing rational right limit at t. Left limits follow similarly. Finite-coordinate control plus the series tail transfers the result to the state metric.

\[
d_H(x,y)=\sum_{j\ge1}2^{-j}\min(1,|h_j(x)-h_j(y)|),\qquad Y_t=\lim_{q\downarrow t,\ q\in\mathbb Q}X_q.
\]

The preceding section keeps every Y-value and left limit in E. For fixed t and any h in C₀, the Markov property gives the following expression, which tends to zero by strong continuity. Hence h(Xq) converges in probability to h(Xₜ) and almost surely to h(Yₜ). Apply this to the countable separating family to get Yₜ=Xₜ almost surely: it is a modification.

\[
E_\pi|h(X_{t+s})-h(X_t)|^2=E_\pi[T_sh^2(X_t)-2h(X_t)T_sh(X_t)+h(X_t)^2]\longrightarrow0.
\]

For one measurable modification common to all starting points, fix the increasing compact exhaustion Kₘ from P.1 whose interiors cover E. Define the good event by all countable crossing conditions and the requirement that for every integer N some Kₘ contains Xq for every rational q in [0,N]. This is a countable Borel condition independent of π. Every random compact set in P.5 is contained in some Kₘ: its cover by the exhaustion interiors has a finite subcover, and the sets increase. This fixed good event therefore has probability one for every initial law; use the same fixed constant path outside it. Each Yₜ is a measurable function of rational coordinates, and càdlàg paths give joint measurability. Raw finite-dimensional laws are measurable in x, and π–λ extends this to the rational-coordinate σ-algebra. The regularization map depends only on these coordinates, so x↦the path law of Y is measurable. Fixed-time modification preserves finite-dimensional laws; cylinder conditional expectations and a monotone class retain deterministic-time Markov. Rational times uniquely determine the law on the path coordinate σ-algebra.

## P.7 Right Continuity of the Completed Natural Filtration

<a id="t-feller-filtration"></a>

Rename Y as X and fix π. Let Gₜ be the natural filtration augmented by all Pπ-null terminal path events and their subsets. For sₙ decreasing to t prove ∩Gₛₙ=Gₜ. Start with a finite cylinder product Z whose factors belong to C₀ plus constants. For large n, sₙ lies before its first future observation r. Markov recursion makes its conditional mean the past product times Tᵣ₋ₛₙg(Xₛₙ), for g in C₀ plus constants.

Conservativity preserves constants, and C₀ plus constants is an algebra. Strong continuity and right-continuous paths make these conditional means converge boundedly to E(Z|Gₜ). The reverse conditional-expectation theorem identifies the same limit with E(Z|∩Gₛₙ). These cylinder functions generate the path σ-algebra; the functional monotone class extends equality to all bounded path variables, and completion changes no conditional means. Taking indicators of events in the intersection gives membership in Gₜ. Denote this right-continuous completed filtration by Fₜ.

This is completion for the fixed π. A measurable raw Markov family does not mean all Pₓ have the same null sets; no such assertion is made.

## P.8 Stopped States, Open Entrances and Strong Markov

<a id="t-feller-strong-markov-proof"></a>

On [0,t], use rightward grids capped at t. Right continuity makes Xₛ measurable for B([0,t])×Fₜ. Substitute the Fₜ-measurable τ∧t to obtain measurable Xτ∧t. Thus {Xτ∈B}∩{τ≤t} belongs to Fₜ, proving Fτ-measurability on finite τ. For open U its entrance time satisfies {τU<t}=∪q<t{Xq∈U}. Right continuity of the filtration gives {τU≤t}=∩n{τU<t+1/n} in Fₜ.

For bounded τ take τₙ=2⁻ⁿceil(2ⁿτ). It is a stopping time, and for A in Fτ each intersection A∩{τₙ=k2⁻ⁿ} is measurable at that grid time. Apply deterministic Markov on each slice to get the chapter’s identity for f in C₀. Both τₙ and τₙ+s approach from the right; right-continuous paths, continuous Tₛf and boundedness permit dominated convergence. Constants and a monotone class extend the conditional identity to all bounded Borel f.

For general τ use A∩{τ≤m} and τ∧m. This event belongs to Fτ∧m: intersecting with {τ∧m≤t} gives A∩{τ≤t} for t<m, and A∩{τ≤m} for t≥m. Let m increase to get the result on finite τ. Iterate conditional expectations at τ+tᵢ for future products; rational coordinates generate the future càdlàg path σ-algebra, so π–λ gives the full future strong Markov formula. Terminal expressions on infinite τ always carry the finite-τ indicator; X∞ is not silently defined.

Closed-set entrance cannot be proved merely by taking open-neighborhood limits. The càdlàg path equal to 1−s for s<1 and to 1 afterward never hits zero, but its entrance times into open neighborhoods of zero tend to one. No unproved debut theorem is used here.

## P.9 Dynkin’s Formula and Discounted Stopping

<a id="t-feller-dynkin"></a>

For f in D(A), Af is bounded. Joint measurability supplies the time integral, and Markov plus bounded conditional Fubini prove the martingale M in the chapter. If τ≤T use the dyadic approximations and the finite-grid expansion below. Each indicator is measurable at the beginning of its increment, giving mean zero term by term.

\[
M_{\tau_n}=M_0+\sum_{k=0}^{\lceil2^n(T+1)\rceil}\mathbf1_{\{\tau_n>k2^{-n}\}}(M_{(k+1)2^{-n}}-M_{k2^{-n}}),\qquad |M_{\tau_n}|\le2\|f\|+(T+1)\|Af\|.
\]

Right continuity and the deterministic bound give EMτ=0, the bounded Dynkin formula. If Eτ is finite, apply it to τ∧n. The integral is dominated by τ‖Af‖ and the terminal value is bounded, giving the stated extension.

For u=Rλf one has (A−λ)u=−f. The discounted semigroup integral identity on deterministic intervals and conditional Fubini directly prove that the following is a martingale; no stochastic integral or unproved product formula is required.

\[
N_t=e^{-\lambda t}u(X_t)-u(X_0)+\int_0^t e^{-\lambda s}f(X_s)\,ds.
\]

Finite-grid stopping is identical, with a bound 2‖u‖+‖f‖/λ independent even of T. Stop at τ∧n and let n increase. An exponential tail dominates the integral; the terminal value tends to zero on infinite τ and is eventually the desired value on finite τ. This proves the chapter’s resolvent decomposition at arbitrary stopping times.

The kernel, path and strong Markov proof handles conservative C₀-Feller families. Kernel representation also covers nonconservative semigroups, but general lifetimes, absorbing cemetery constructions and broader right-process theory are not claimed through undeveloped steps here.
