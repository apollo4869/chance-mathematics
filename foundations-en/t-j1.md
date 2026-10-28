# T-J1: Topology, Measurability and Tightness of Jump Paths

This companion supplies the proofs for real jump paths used in Chapter 24. Begin with D=D([0,1],ℝ): paths are right-continuous and have finite left limits at positive times. The recorded terminal value x(1) is distinct from x(1−). A local J₁ space on the half-line is constructed separately at the end. Only the stated strong stopping-pair sufficient criterion is proved; no equivalence of all Aldous formulations is claimed.

<a id="t-j1-regulated"></a>

## 1. Why a single path admits a finite step description

For ε>0 start at t₀=0 and take the next point to be the first time at which |x(t)−x(tᵢ)|>ε, using 1 if there is no such time and stopping there. Right continuity puts each genuine new point strictly to the right. At the exit the displacement can equal ε; right continuity guarantees at least ε, not necessarily a strict inequality.

There cannot be infinitely many exits. Otherwise they increase to t*≤1; successive anchor values differ by at least ε but both approach the left limit at t*, a contradiction. Thus a finite partition results. On each half-open cell [tᵢ,tᵢ₊₁), values are within ε of x(tᵢ), so the oscillation is at most 2ε. Assign the original value separately at 1. The resulting step function s satisfies ‖s−x‖∞≤ε. Consequently x is bounded and has at most countably many discontinuities: jumps larger than 2ε can occur only at the finitely many partition boundaries, and then take the union over ε=1/m.

<a id="t-j1-polish"></a>

## 2. Time alignment and a genuinely complete metric

Let Λ consist of increasing endpoint-fixing homeomorphisms of [0,1]. Ordinary J₁ convergence means that some λₙ∈Λ make both the time error and the aligned value error vanish. Its direct infimum metric is not complete: 1_[1/n,1] approaches an object that is not right-continuous at 0. Control of the relative stretching of intervals, rather than displacement alone, repairs this. Let Λ₀ consist of clocks with finite logarithmic distortion and define d₀ below.

\[
L(\lambda)=\sup_{s<t}\left|\log\frac{\lambda(t)-\lambda(s)}{t-s}\right|,
\qquad
d_0(x,y)=1\wedge\inf_{\lambda\in\Lambda_0}
\max\{L(\lambda),\|x-y\circ\lambda\|_\infty\}.
\]

An inverse clock has the same L, and distortion is subadditive under composition, giving symmetry and the triangle inequality. Also L(λ)≤r implies ‖λ−id‖∞≤eʳ−1. At distance zero, alignment gives x(t)=y(t) at every continuity point of y. Such points are dense; right continuity supplies all interior values and the fixed endpoint supplies 1. Thus d₀ is a metric.

The metric has the same convergent sequences as ordinary J₁. One direction follows from the displacement bound. For the other write ‖xₙ∘λₙ−x‖∞→0. Choose a finite half-open partition on which x oscillates by less than 2ε, and replace λₙ by the piecewise-linear clock through the images of its endpoints. The finitely many interval lengths are positive, so its slopes approach 1 and its L tends to zero. Inside a cell the old and new clocks, after conversion, stay in that same cell; the value error is at most the original error plus 2ε. At boundaries and at 1 the clocks agree. Taking n to infinity and then ε to zero gives d₀→0.

For completeness choose a Cauchy subsequence, still denoted xₙ, with clocks λₙ realizing adjacent errors εₙ where Σεₙ<∞. Set φ₁=id and φₙ₊₁=λₙ∘φₙ. The aligned hₙ=xₙ∘φₙ are uniformly Cauchy and converge uniformly to a càdlàg g: right continuity and left limits survive by the uniform-error triangle estimate. The displacement increments of φₙ are summable and the clocks have common bi-Lipschitz bounds e^{±Σεₙ}; hence they converge uniformly to a homeomorphism φ. Tail compositions also satisfy the following bound.

\[
L(\varphi\circ\varphi_n^{-1})\le\sum_{j\ge n}\varepsilon_j,
\qquad x=g\circ\varphi^{-1},\qquad d_0(x_n,x)\longrightarrow0.
\]

The last convergence follows directly from xₙ(t)=hₙ(φₙ⁻¹(t)) and x(φ∘φₙ⁻¹(t))=g(φₙ⁻¹(t)). The Cauchy property recovers the whole sequence. Separability is not an additional assumption: first approximate uniformly by a finite step function, then approximate its finitely many jump times and heights by rationals, independently including the terminal value. Piecewise-linear clocks align adjacent jump times with L tending to zero. These rational step functions form a countable dense set. Hence (D,d₀) is Polish.

<a id="t-j1-borel"></a>

## 3. Why coordinates still generate every Borel event

If xₙ→x in J₁, then xₙ(t)→x(t) at every continuity point of x and the uniform norms share a bound. The endpoint evaluations e₀ and e₁ are always continuous. For t<1 choose h>0 with t+h≤1. The following average is J₁-continuous: pointwise convergence holds outside countably many jumps and a common bound dominates the integral. Let h decrease to zero; right continuity yields e_t, so every evaluation is Borel.

\[
A_{t,h}(x)=\frac1h\int_t^{t+h}x(s)\,ds\longrightarrow x(t).
\]

Conversely let Pₖx sample the left endpoint of each dyadic half-open cell and retain x(1) at 1. This map uses only finitely many coordinates, and fixed-step interpolation is continuous in its heights under the uniform norm. Moreover Pₖx→x in J₁. For a finite step function s, sampling moves each jump right by at most 2⁻ᵏ; a sufficiently fine grid does not merge distinct jumps and clocks align them. For general x first make ‖x−s‖∞ small, use the contraction of Pₖ in uniform norm and d₀≤1∧‖·‖∞, then apply the triangle inequality.

For fixed y, d₀(x,y)=limₖd₀(Pₖx,y) is measurable for the coordinate σ-algebra. Separability makes every open set a union of a countable base of balls, so the Borel σ-algebra is exactly coordinate-generated. Any countable dense time set containing 1 suffices: approach each t<1 from the right to recover x(t). The terminal time 1 must explicitly be included.

<a id="t-j1-compact"></a>

## 4. Oscillation partitions and the full compactness criterion

Every partition gap below is strictly larger than δ. Cells exclude their right endpoint, in particular 1 in the last cell; the terminal value is separately controlled by the uniform norm. This convention permits a genuine terminal jump without hiding two opposing jumps near an endpoint.

\[
w'(x,\delta)=\inf_{\substack{0=t_0<\cdots<t_m=1\\
                         \min_i(t_i-t_{i-1})>\delta}}
\max_i\sup_{s,t\in[t_{i-1},t_i)}|x(s)-x(t)|.
\]

A set K is relatively compact if and only if its uniform norms are bounded and sup_{x∈K}w′(x,δ) tends to zero. For sufficiency, fix ε and choose a common δ giving each path a partition with oscillation less than ε. Replace each cell by its left value and keep the endpoint, with uniform error below ε. The number of cells is at most 1/δ, gaps are at least δ, and heights lie in a common compact interval. For a fixed number of cells the time and height parameters form a finite-dimensional compact set, mapped continuously into D: linear clocks align corresponding times and the gap bound makes slopes continuous in the parameters. The union over finitely many cell counts is compact. Thus K has a finite ε-net; completeness converts total boundedness into compact closure.

For necessity take a good partition for a single x with minimum gap g>0. If y is within d₀-distance r, an aligning clock transports it to a partition for y with gaps at least e⁻ʳg and oscillations at most the original ones plus 2r. The uniform norm is J₁-continuous. A finite neighborhood cover of a compact set supplies common norm bounds and a common δ. Apply this to the compact closure for a relatively compact set.

Measurability of w′ also needs proof. If w′(x,δ)<a, choose a strictly good partition; its gaps have positive margin above δ. A small J₁ perturbation transports it to gaps still greater than δ with oscillations still less than a. Thus {w′(·,δ)<a} is open and w′ is upper semicontinuous. The probability criterion follows: D-valued laws are uniformly tight exactly when their uniform norms have compact containment and supₙP(w′(Xₙ,δ)>ε) tends to zero for every ε>0. For sufficiency choose summable bad-event probabilities, intersect the good constraints and take the closure, using the relative compactness just proved. Necessity uses the uniform criterion on a common compact set. Replacing supₙ by limsupₙ changes nothing: finitely many laws are tight and each càdlàg path has w′ tending to zero.

<a id="t-j1-fixed-times"></a>

## 5. Only countably many fixed times have positive jump probability

On equivalence classes of real random variables on the same probability space put ρ(V,W)=E[min(1,|V−W|)]. Dominated convergence transfers pathwise right continuity and left limits to t↦[X_t], making it a càdlàg curve in this metric space. The variable X_{t−} is measurable by deterministic increasing-time sampling. The finite oscillation partition proof in Section 1 uses only metric triangle inequalities and applies to this curve. It therefore has at most countably many discontinuities. But ρ(X_t,X_{t−})>0 holds exactly when P(X_t≠X_{t−})>0. No completeness of the random-variable space or process regularization theorem is used.

<a id="t-j1-aldous"></a>

## 6. Why the strong stopping-pair condition yields tightness

Suppose Xₙ is adapted to a right-continuous filtration, has càdlàg paths and compact containment of uniform norms, and satisfies the aₙ(δ,ε) condition in Chapter 24. All stopping times take values in [0,1]. First verify the exit times without using future continuous-time sampling results. Approximate a stopping time S from above by dyadic S_m↓S. The variable X_{t∧S_m} is F_t-measurable: its finite pieces use observations no later than t. Right continuity gives X_{t∧S_m}→X_{t∧S}, so the stopped process is adapted. The difference Z_t=X_t−X_{t∧S} is also adapted and càdlàg.

For the open crossing σ=inf{t:|Z_t|>ε}, the event {σ<t} is generated by rational observations before t. Right continuity of the filtration then gives {σ≤t}=∩_m{σ<t+1/m}∈F_t. Capping at 1 preserves the stopping property. The displacement at the crossing may only equal ε, which explains the use of ε/2 in the estimates.

Starting at τ₀=0, repeat exits of scale ε and let N count genuine exits before 1. It is pathwise finite. If the kth gap is at most δ and the next exit precedes 1, the pair S=τ_k and U=τ_{k+1}∧(τ_k+δ)∧1 has displacement at least ε. Its probability is at most aₙ(δ,ε/2). On N≥K at least K/2 of the first K gaps have length at most 2/K. Taking expectations of their indicators, without falsely requiring independence, gives the bound below.

\[
P(N\ge K)\le 2a_n(2/K,\varepsilon/2).
\]

For fixed K, the probability that one of the first K genuine exit gaps is at most δ with τ_{k+1}<1 is at most K aₙ(δ,ε/2). A further open crossing starting at the deterministic time 1−2δ bounds the probability of the explicit bad event sup_{t∈[1−2δ,1]}|Xₙ(t)−Xₙ(1−2δ)|>ε by aₙ(2δ,ε/2). Outside these bad events retain all exit times before 1−δ and append 1. Every gap exceeds δ. Ordinary cells have oscillation at most 2ε and the last has oscillation at most 4ε: if its anchor precedes 1−2δ, the path stays within ε of it until the terminal segment and that segment stays within ε of X(1−2δ); if the anchor is already in that segment, the terminal bound suffices. Consequently

\[
P(w'(X_n,\delta)>4\varepsilon)
\le P(N>K)+K a_n(\delta,\varepsilon/2)
+             a_n(2\delta,\varepsilon/2).
\]

Take the upper limit in n, then let δ decrease to zero and finally K increase to infinity. The displayed bounds force the right side to zero, and Section 4 gives tightness after adding the finite prefix through tightness of its individual laws; that prefix need not satisfy the asymptotic stopping-pair condition. A single deterministic jump at a known time fails this stopping-pair condition but forms a compact set by itself, so the criterion is sufficient only.

<a id="t-j1-local"></a>

## 7. Local J₁ on the half-line: truncation endpoints cannot all be fixed

Write D∞=D([0,∞),ℝ) and R_Tx(s)=x(Ts), 0≤s≤1. The integral below gives a useful complete metric, rather than a sum over integer restrictions. For a fixed path, T↦R_Tx is Borel: finite-interval Borel sets are coordinate-generated and x(Ts) is Borel. The integral is therefore defined.

\[
d_\infty(x,y)=\int_0^\infty e^{-T}d_0(R_Tx,R_Ty)\,dT.
\]

Symmetry and the triangle inequality follow by integration. If x≠y, right continuity preserves a difference on a short interval to the right of some time. Restrictions are then distinct for all sufficiently large T, making the integral positive. This proves separation.

First prove the restriction lemma: if xₙ→x in J₁ on [0,H] and T<H is a continuity point of x, restrictions to [0,T] still converge in J₁. Take the aligning clocks and adjust linearly in a shrinking neighborhood before T to make the new clock fix T, leaving it unchanged earlier. Twice the square root of the original maximum time error can serve as the neighborhood width, ensuring strictly increasing interpolation and vanishing time error. Beyond the original error, the new value error involves only the oscillation of x near T, which vanishes by continuity. Equivalence of the finite-interval metrics gives the result.

For completeness extract from a d∞-Cauchy sequence a subsequence with summable adjacent distances. Tonelli gives, for almost every T, a Cauchy sequence of restrictions in the complete metric d₀, with its limit rescaled from [0,1] back to [0,T] and denoted y_T. Choose good windows T_j tending to infinity. On the common interior of any two windows, the limits agree at their common continuity times by pointwise convergence, and then everywhere by right continuity. No agreement at the shorter terminal point is asserted in advance. Define each finite-time value using a larger window to obtain a global càdlàg path x.

Now take any good window T at which x is continuous. On [0,T), y_T already equals x. A larger good window and the restriction lemma give terminal limit x(T), while continuity of the short-window endpoint evaluation gives y_T(T). Both are limits of the original subsequence values at T and hence agree. The jumps of x are countable, so restrictions converge to R_Tx for almost every T. Distances are bounded by 1; dominated convergence gives d∞ convergence, and the Cauchy property recovers the full sequence.

Rational finite step functions, constant after some integer, form a countable dense set. First choose M with small tail integral e⁻ᴹ, approximate uniformly by a finite step function on [0,M], then approximate heights and jump times by rationals. Every smaller restriction except at finitely many jump endpoints converges in J₁; dominated convergence handles the integral. Thus D∞ is Polish as well.

Convergence in this metric is exactly convergence R_Txₙ→R_Tx at every continuity horizon T of the limit x. One direction follows by integration. For the other, from any subsequence extract a further subsequence converging on almost every window; for a given continuous horizon choose a larger good window and use the restriction lemma. A bad-subsequence contradiction recovers convergence of the full sequence at T. The moving jump 1_[1+1/n,∞) converges to 1_[1,∞) in this topology although terminal values in the integer window 1 do not converge.

Finally verify measurability. Let Σ be generated by all coordinates. The joint map (t,x)↦x(t) is B(ℝ₊)⊗Σ-measurable: right dyadic rounding gives measurable approximations on countably many rectangular pieces and converges pointwise. Finite-interval coordinate generation makes (T,x)↦R_Tx jointly measurable. Integral distances are consequently Σ-measurable and separability gives B(D∞)⊂Σ. Conversely, right-side short averages are continuous by restriction convergence at continuous horizons and dominated convergence; their limits give Borel evaluations. Thus B(D∞)=Σ.

The paths here are real-valued. Arbitrary Polish-valued paths, the weaker M₁ topology and equivalences with weaker Aldous formulations do not follow automatically. The finite-interval compactness criterion, half-line Polish and Borel structures, and the strong stopping-pair sufficient criterion above have actual proofs.
