# T-RIESZ: From Continuous Tests to Locally Finite Measures

This proof supplies the positive-functional representation used in [Chapter48](../chapters/48-point-processes.md#points-tests), without assuming the random-measure topology of Chapter49.

## 1. The space and local tools

<a id="riesz-space"></a>

Throughout, E is a locally compact second-countable metric space with a fixed compatible metric. Starting from a countable relatively compact open cover, cover each preceding compact closure by finitely many such opens and take the closure of their union. This gives Kₘ⊂int Kₘ₊₁ exhausting E. Cutoffs can be constructed directly: for compact K inside open U, finitely many small balls give open V with K⊂V⊂cl V⊂U and cl V compact. Set χ(x)=d(x,E∖V)/(d(x,E∖V)+d(x,K)). Then χ=1 on K, 0≤χ≤1 and its support is in cl V. For empty K take zero; if V=E, which is then compact, take one. No further representation or general-topology theorem is being assumed.

A compactly supported partition under a finite open cover follows directly. Choose nonnegative bumps supported in cover members and positive at each point of the compact set; retain finitely many ψᵢ. Their sum is positive near the compact set. Multiply ψᵢ/Σψⱼ by a cutoff equal to one on that set. Consequently any f∈\(C_c^+\) whose support is covered can be decomposed into finitely many nonnegative functions supported in individual cover members.


We also need a measure-regularity fact. Every locally finite Borel measure ν on this space is Radon. An open U is the increasing union of compact sets Kₘ∩{d(x,E∖U)≥1/m}, using Kₘ when U=E, so opens are inner regular. In a relatively compact open window V, ν is finite. Closed inner approximations of relative opens give open outer approximations of their complements. For a finite measure the sets admitting both closed inner and open outer approximations form a sigma-field: complements interchange the properties; for countable unions first keep finitely many inner approximations to control the tail and choose summable outer errors. This class contains the opens and hence all Borel sets. Intersect closed inner approximations with a compact exhaustion inside V to make them compact. Finally partition a countable relatively compact open cover into disjoint Borel pieces, approximate each part of A inside its open window with summable errors, and unite the resulting open sets. This gives global outer regularity. This also proves regularity of locally finite Borel image intensities.


The cutoffs also give a compatible complete metric. Choose χₘ=1 on Kₘ with support in int Kₘ₊₁ and values in [0,1], and let φ=Σₘ(1−χₘ). Only finitely many terms are nonzero locally, so φ is continuous. Outside Kₙ at least its first n−1 terms equal one, making bounded sublevel sets compact. The compatible metric d′(x,y)=d(x,y)+|φ(x)−φ(y)| is complete: a Cauchy sequence has bounded φ and remains in a compact set, where a convergent subsequence and the Cauchy property give convergence of the whole sequence. Separability follows from the original countable base. Thus E is indeed Polish and standard Borel, verifying the state-space hypothesis for kernel randomisation.

## 2. Positivity gives local boundedness

<a id="riesz-bound"></a>

Let L:\(C_c(E)\)→R be positive and linear. If f is supported in compact K and χ≥1 on K, then |L(f)|≤‖f‖∞L(χ). No further continuity assumption on the functional is needed. The desired unique Radon measure μ should satisfy L(f)=∫f dμ. Start by assigning the following candidate mass to open U.

\[ m(U)=\sup\{L(f):f\in C_c(E),\ 0\le f\le1,\ \operatorname{supp}f\subset U\}. \]

The function m is monotone. It is finitely additive on disjoint opens, and for any open cover U⊂∪Uᵢ it satisfies m(U)≤Σm(Uᵢ): the compact support of each test has a finite subcover, and the partition just constructed decomposes that test. For the reverse inequality on disjoint opens, add finitely many nearly optimal tests. Their sum is still at most one. Increasing the number of terms gives the countable disjoint-open comparison.

## 3. Outer measure and Borel measurability

<a id="riesz-outer"></a>

\[ \mu^*(A)=\inf\{m(U): A\subset U,\ U\text{ open}\}. \]

The open-cover comparison proves that μ* is an outer measure and μ*(U)=m(U). If A and B have positive distance, split any open neighbourhood of their union into disjoint open neighbourhoods containing them, and use additivity on disjoint opens to obtain μ*(A∪B)≥μ*(A)+μ*(B). Thus μ* is a metric outer measure. We spell out the key measurability step rather than assuming another representation theorem.

For closed F and any A first suppose μ*(A)<∞. Put Aₖ={x∈A:d(x,F)≥1/k}. Separation gives μ*(A)≥μ*(A∩F)+μ*(Aₖ). We also need μ*(A∖F)≤lim μ*(Aₖ). Partition positive distances into shells with decreasing thresholds. Any finite collection of odd shells is mutually separated, as is any finite collection of even shells. Each sum of outer masses is bounded by μ*(A), so the shell tails have mass tending to zero; what lies outside Aₖ is bounded by such a tail. This gives the Carathéodory equality. If μ*(A)=∞, finite total mass of the two pieces would contradict subadditivity; otherwise the equality is automatic. Closed, and hence Borel, sets are measurable. Restrict μ* to Borel sets to obtain μ.

The mass of relatively compact open U is bounded by L(χ) for a cutoff χ≥1 on its closure, so μ is locally finite. Outer regularity is built into the definition. For inner regularity of opens, if f is an admissible test supported in U, then K=supp f satisfies μ(K)≥L(f), since every open V containing K has m(V)≥L(f). Taking suprema gives \(\mu(U)=\sup_{K\subset U,\ K\ \mathrm{compact}}\mu(K)\). For arbitrary Borel A, approximate its complement from outside in a finite-mass window to obtain compact inner approximations to A; then use the compact exhaustion. Thus μ is Radon.

## 4. Recovering integrals, not only open sets

<a id="riesz-integral"></a>

For nonnegative f∈\(C_c\) and step δ>0 take the finitely many level opens Uⱼ={f>jδ}. In each choose compactly supported 0≤gⱼ≤1. Pointwise δ\(\sum_{j\ge1}\)gⱼ≤f, so L(f)≥δ\(\sum_{j\ge1}\)m(Uⱼ), by approaching each supremum before summing. As δ↓0 this gives L(f)≥∫₀∞μ{f>t}dt=∫f dμ. In the other direction use continuous layers hⱼ=min(1,(f−jδ)₊/δ). For j≥1 their support lies in {f>(j−1)δ}, so L(hⱼ)≤m({f>(j−1)δ}). Bound the j=0 layer by a fixed cutoff χ near the support: L(h₀)≤L(χ). The identity f=δ\(\sum_{j\ge0}\)hⱼ, including the truncated last layer, gives L(f)≤δL(χ)+δ\(\sum_{j\ge1}\)m({f>(j−1)δ}). The two Riemann sums have the same limit, since μ(supp f)<∞. This proves equality. Positive and negative parts give general f.

Any representing Radon measure has mass m(U) on each open U, by compact inner approximation and cutoffs. Opens determine the Borel measure: use finite-measure π–λ uniqueness in relatively compact windows and exhaust E. Representation is unique. The argument uses the outer-measure, monotone-class and nonnegative-integration tools of Chapters5–6, not Chapter49.
