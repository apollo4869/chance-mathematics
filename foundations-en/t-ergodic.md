# T-ERGODIC: Measure-Preserving Averages, the Maximal Lemma and Pointwise Limits

This page completes the probability-preserving results in [Chapter 41](../chapters/41-ergodic-theory.md#ergodic-birkhoff). T is measurable with P∘T⁻¹=P and need not be invertible. Functions are real; complex functions are treated through their real and imaginary parts. I consists of invariant events modulo P. Null sets may be shared by a specified countable test family, not automatically by all of L¹.

## 1. Space decomposition, conditional projection and a bounded dense class

<a id="ergodic-proof-mean"></a>

The integral identity for indicators extends through simple functions and monotone convergence to Eφ∘T=Eφ, with positive and negative parts for integrable signed functions. Thus U is an isometry on L² and \(U^*\)U=I. The orthogonal complement of ran(I−U) is ker(I−\(U^*\)). If \(U^*\)h=h, then ‖Uh−h‖²=2‖h‖²−2〈Uh,h〉=0; if Uh=h, then \(U^*\)h=\(U^*\)Uh=h. Hence the closed range of I−U is exactly the orthogonal complement of Fix U.

For a coboundary, Aₙ(I−U)g=(g−Uⁿg)/n has L² norm at most 2‖g‖₂/n. Fixed functions remain fixed. Since Aₙ is a contraction, the orthogonal decomposition gives L² convergence to the projection P. Fix U=L²(I), and Chapter 9 identifies P with E[·|I]. Truncating an invariant h retains invariance; truncating g approximates its coboundary in L². Thus sums of bounded invariant functions and bounded coboundaries form a dense class D in L². L² approximation implies L¹ approximation, and truncation of an arbitrary L¹ function makes D dense there as well. Each element of D has pathwise and L¹ convergence of its averages.

## 2. The finite maximal recursion and all observation lengths

<a id="ergodic-proof-maximal"></a>

\[ S_kf=\sum_{j=0}^{k-1}U^jf,\quad F_0=0,\quad F_N=\max(0,S_1f,\ldots,S_Nf)=(f+UF_{N-1})^+. \]

F_N is integrable since F_N≤Σⱼ<N Uʲ|f|. On E_N={F_N>0}, f=F_N−UF_{N−1}; off E_N, zero is at least −UF_{N−1}. Integration gives ∫_{E_N}f≥EF_N−EF_{N−1}≥0. The events increase and |f| dominates, giving the infinite maximal lemma. Apply it to f=|r|−λ: E_N={maxₖ≤N Aₖ|r|>λ}, and λP(E_N)≤∫_{E_N}|r|. Increasing N gives weak type (1,1).

For the strong bound, first take bounded r and M_N=maxₖ≤N Aₖ|r|. Multiply the localized event inequality by pλ^{p−2} and integrate over λ>0. Nonnegative Tonelli and Hölder give the inequality below. Every term is finite since M_N is bounded. Cancel its norm to the power p−1, then remove truncation and increase N by monotone convergence, obtaining the constant p/(p−1).

\[ EM_N^p\le\frac p{p-1}E(|r|M_N^{p-1})\le\frac p{p-1}\|r\|_p\|M_N\|_p^{p-1},\qquad \left\|\sup_n A_n|r|\right\|_p\le\frac p{p-1}\|r\|_p. \]

## 3. The complete L¹ pointwise theorem and identification

<a id="ergodic-proof-pointwise"></a>

The weak estimate gives supₙAₙ|f|<∞ almost surely, since its probability of exceeding K is at most ‖f‖₁/K. For h_j∈D tending to f in L¹, the oscillation O(f)=limsup Aₙf−liminf Aₙf is bounded by 2supₙAₙ|f−h_j|. The probability that it exceeds ε tends to zero with j. Countably many ε give a finite limit L(f). Fatou and contraction give ‖L(f)−L(g)‖₁≤‖f−g‖₁. Approximation on both sides by h_j yields limsupₙ‖Aₙf−L(f)‖₁≤2‖f−h_j‖₁ and hence L¹ convergence.

Since ΣₙP(|f|>εn)≤E|f|/ε, preservation and the first Borel–Cantelli lemma give Uⁿf/n→0 almost surely. T⁻¹ preserves null sets, so on the convergence set and its preimage compare UAₙf−Aₙf=(Uⁿf−f)/n to obtain UL(f)=L(f). The limit is I-measurable. For A∈I, 1_AUᵏf=Uᵏ(1_Af) modulo null sets and has integral ∫_A f. L¹ convergence gives the defining integral identity for conditional expectation, proving L(f)=E[f|I].

For p≥2, L² convergence of bounded f and its deterministic uniform bound imply Lᵖ convergence; for 1≤p<2 use norm inclusion on a probability space. Density of bounded functions and contraction on both sides extend this to every 1≤p<∞. This establishes the Lᵖ mean theorem used later, without asserting norm convergence for p=∞.

## 4. Quantifiers for ergodicity, mixing and return

<a id="ergodic-proof-examples"></a>

If I is trivial, every rational level event of an I-measurable real variable has probability zero or one, so its law concentrates at a point; integration identifies that point as Ef. Indicators prove the converse. For an independent shift, finite cylinders become independent under sufficiently large shifts. Approximation of arbitrary A and B by cylinders with error ε bounds the total error in the mixing identity by 4ε. Taking an invariant A and B=A gives P(A)=P(A)². The even–odd calculation for a two-point swap disproves the converse.

Let B=A∩∩ₙ≥1T⁻ⁿ(Aᶜ), the points in A with no return. Its preimages T⁻ʲB are disjoint, since a second occurrence would revisit A after an occurrence in B. Thus P(B)=0. Points visiting A only finitely often eventually enter B and belong to its countable union of preimages. The pointwise theorem identifies the frequency as q=E[1_A|I]. On A, q>0 almost surely, since P(A∩{q=0})=E[q1_{q=0}]=0. No simultaneous assertion over uncountably many positive-probability sets is needed.

## 5. The continuous-time version for a jointly measurable preserving semiflow

<a id="ergodic-proof-flow"></a>

Let θ be a jointly measurable probability-preserving semiflow and f∈L¹. Tonelli gives finite absolute integrals on finite intervals, first on one common set for integer endpoints. Both F=∫₀¹f∘θ_s ds and G=∫₀¹|f∘θ_s|ds are integrable. Apply the discrete theorem to θ₁ and F to obtain a limit L at integer times. Integrable tail sums and preservation give G∘θ_n/n→0 almost surely. For n≤t<n+1 the remaining integral is bounded by G∘θ_n, and the changed denominator is controlled by the convergent integer averages. Thus all real t have the same finite limit.

Fix any r≥0. Shifting by r changes only the initial and terminal intervals of length r. For t∈[n,n+1], the terminal contribution is bounded by H_r∘θ_n with H_r=∫₀^{r+1}|f∘θ_s|ds integrable, so H_r∘θ_n/n→0. Comparing the convergence set with its θ_r preimage gives L∘θ_r=L modulo null sets. This separate assertion for each r suffices for I_flow-measurability. For A∈I_flow, Fubini and preservation make the integral of every continuous-time average over A equal ∫_A f.

For L¹ convergence, continuous averages are L¹ contractions, and Fatou makes their limiting operator a contraction. Bounded f has L¹ convergence by domination; truncate a general f, controlling the two errors by ‖f−f_K‖₁. The integral identity then passes to the limit and L=E[f|I_flow]. We do not require θ₁ to be ergodic and do not confuse its invariant sigma algebra with the full flow's.

Dependencies are integration from Chapter 6, projection from Chapter 9, tail sums and the zero–one law from Chapter 12, and elementary maximal and convergence tools from Chapter 15. The maximal ergodic lemma itself was proved here. Return to [the chapter's concluding insight](../chapters/41-ergodic-theory.md#ergodic-insight).
