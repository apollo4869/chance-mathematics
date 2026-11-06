# T-CHOQUET: Constructing Random Closed Sets from Consistent Hits

Return to [Chapter 51](../chapters/51-random-closed-sets.md#sets-choquet). Use E and the closed-set space including ∅ from T-FELL. We prove the LCSC metric version with Chapter 8 countable consistent-distribution extension, π–λ, and countable compact neighborhoods, not the name Choquet as a construction tool.

## 1. Conditions and Finite Observation Tables

<a id="choquet-finite"></a>

Theorem: T on compact sets is a random closed-set capacity exactly when \(0\le T\le1,\ T(\varnothing)=0\), the following complete-alternation inequality holds for every r≥1 and compact A,K₁,…,Kᵣ, and T(Kₙ) decreases to T(K) for every decreasing compact sequence Kₙ with intersection K. Empty realizations are allowed; T(E)=1 is not required, and noncompact E is outside the domain.

\[ D_{K_1}\cdots D_{K_r}T(A):=\sum_{I\subset\{1,\ldots,r\}}(-1)^{|I|}T\!\left(A\cup\bigcup_{i\in I}K_i\right)\le0. \]

Necessity: the sum equals \(-P(F\cap A=\varnothing,\ F\cap K_i\ne\varnothing\text{ for every }i)\), by expanding the finite product of hit indicators. Decreasing continuity uses the nested compact sets F∩Kₙ: if all are nonempty, they have a common point, so their hit indicators decrease to the intersection-hit indicator.

For sufficiency, do not guess a closed set first. Put q(K)=1−T(K), and let H(K) denote a hit bit not yet constructed. Avoiding A and hitting every Kᵢ must have probability

\[ p(A;K_1,\ldots,K_r)=\sum_{I\subset\{1,\ldots,r\}}(-1)^{|I|}q\!\left(A\cup\bigcup_{i\in I}K_i\right). \]

For r≥1 this is −D…DT(A), hence nonnegative; for r=0 it is q(A)≥0. For any finite binary pattern, unite its zero-required sets into A and use the remaining sets as Kᵢ. Sum the two possibilities for one bit: the new-set terms cancel. Repetition leaves q(∅)=1; the same cancellation proves marginal consistency when deleting coordinates. We have actual consistent finite-dimensional probabilities, not merely some nonnegative numbers.

## 2. Extend Only Countable Records

<a id="choquet-countable"></a>

Take the countable union-closed compact family R of T-FELL. Chapter 8 gives a probability on {0,1}ᴿ and coordinates H(K). Its finite tables yield H(∅)=0, H(L)≤H(K) for L⊂K, and H(K∪L)=max(H(K),H(L)), each almost surely. For the last identity, monotonicity gives one side; avoiding both but hitting the union has probability q(K∪L)−q(K∪L)=0. Countably many indices and pairs give all relations on one full-probability set.

For each K∈R use its fixed outer approximations Lₙ∈R, with K⊂int Lₙ and Lₙ decreasing to K. Monotonicity gives H(Lₙ) decreasing to H*≥H(K), but EH*=lim T(Lₙ)=T(K)=EH(K), hence H*=H(K) almost surely. There are only countably many chosen sequences, so unify these null sets too. The good-record set is measurable because it uses countably many coordinate conditions; on bad records assign the empty set.

## 3. Realize a Closed Set, Not an Arbitrary Subset

<a id="choquet-realization"></a>

\[ F=E\setminus\bigcup_{\substack{L\in R\\H(L)=0}}\operatorname{int}L. \]

This is closed. For each K∈R prove that H(K)=1 exactly when F hits K. If H(K)=0, outer continuity gives some H(Lₙ)=0 with K⊂int Lₙ, so F misses K. Conversely, if F misses K, each x∈K lies in int L for some H(L)=0; compactness gives a finite subcover. Their union has hit bit zero and contains K, so monotonicity gives H(K)=0. Omitting this direction would merely close an arbitrary record without proving that it was preserved.

For open U, F hits U exactly when it hits some K∈R contained in U, so the event is a countable union of coordinate events. Together with the empty-set convention on measurable bad records, all open hits are measurable. T-FELL makes F a random element of the Polish closed-set space, not merely a pointwise-measurable membership field.

## 4. Arbitrary Compact Tests and the Unique Law

<a id="choquet-uniqueness"></a>

Take any compact K, not necessarily in R, and outer approximations Lₙ∈R decreasing to K. Closedness makes their hit indicators decrease to the hit indicator of K. Thus P(F hits K)=lim T(Lₙ)=T(K), recovering the whole domain. Equal capacities give identical finite joint R-hit laws by the finite-table formula. Their cylinders form a π-class generating Fell Borel, so π–λ gives identical closed-set laws.

For an increasing compact exhaustion Kₘ, nonemptiness is hitting some Kₘ, hence P(F=∅)=1−lim T(Kₘ). Almost-sure nonemptiness requires this limit to be one; it must not be silently included in normalization. Capacity identifies not only shapes but the probability of no shape at all.

## 5. Two Missing-Condition Counterexamples

<a id="choquet-counterexamples"></a>

On a three-point space let T(singleton)=1/2, T(two or three points)=1, T(∅)=0. Monotonicity, subadditivity, and decreasing continuity hold, but the finite table assigns −1/2 to hitting all three points; the third alternating difference is +1/2. Pairwise hits would be mutually exclusive while singleton probabilities sum to 3/2, which is impossible.

On [0,1] put T(K)=1 for infinite K, zero otherwise. A finite union is infinite exactly when some member is infinite, so alternating differences are zero or −1. Yet Kₙ={0}∪{1/k:k≥n} decreases to {0}, with capacities staying one instead of tending to zero. In any representation every singleton would have hit probability zero, so the countable K₁ would too, contradicting T(K₁)=1. Decreasing continuity genuinely excludes unrealizable records.
