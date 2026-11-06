# Chapter 51: How Can a Random Set Have a Probability Law?

Choose a height uniformly in the unit square and draw a horizontal line from its left side to its right. Every point fixed before the experiment has probability zero of lying on the line. Yet every experimental record contains an entire line.

A table of membership probabilities at all locations contains only zeros. It cannot even distinguish drawing a line from drawing nothing. What is missing is not a more accurate decimal, but the way different locations jointly form one shape in an experiment.

## 51.1 No Point Is Preselected, Yet a Whole Line Exists

<a id="sets-stroke"></a>

Let U be uniform on [0,1] and put \(F_U=[0,1]\times\{U\}\). For fixed (x,y), P((x,y)∈Fᵤ)=0, but P(Fᵤ≠∅)=1. An uncountable union of null events need not be null. A window whose vertical extent is [a,b] instead has hit probability b−a. Windows retain information absent from pointwise observations.

We need not first decide the line’s length measure, its mass allocation, or a number of constituent points. Ask a question making fewer commitments: does this realization meet a region? If that suffices, a probability theory of shape can precede any choice of mass on the shape.

## 51.2 Why Open Windows Cannot Detect Missing Limit Points

<a id="sets-closedness"></a>

This observation scheme does not distinguish arbitrary subsets. The rationals and the whole real line hit exactly the same nonempty open sets, but are different sets. Open windows cannot decide whether a limit point has been included; they see closure. Closedness is thus not a decorative convenience for proofs, but a boundary of what these observations identify.

For closed F, every x outside F has an open neighborhood disjoint from F, and one may choose it from a countable base. Their union is exactly its complement, so open-hit records recover a closed set. Random records must additionally be compatible and measurable and determine joint probabilities. Deterministic distinguishability is only the first step.

## 51.3 Give Possible Shapes a Common Space

<a id="sets-state"></a>

Let E be a locally compact second-countable metric space, and let \(\mathcal F(E)\) contain all closed subsets, including ∅. These are the space hypotheses of Chapters 48–49, but objects are sets rather than masses. For open U and compact K write

\[ H_U=\{F:F\cap U\ne\varnothing\},\qquad M_K=\{F:F\cap K=\varnothing\}. \]

A random closed set is a map into this space for which every open-hit event is measurable: the Effros measurable structure. The original experiment’s probability space need not be standard Borel. We will prove that the shape space itself has a suitable Borel structure before studying laws and limits. The empty set preserves experiments leaving no shape; it must not be silently discarded.

## 51.4 Why Avoid Compact Sets Rather Than All Open Sets?

<a id="sets-fell"></a>

The singleton {n} leaves every bounded observation region, so its local record should tend to the empty set; requiring eventual avoidance of the whole line would forbid that limit. Conversely {1/n} should tend to {0}, retaining approximation of a limiting point by nearby points. We need both approximation of points that should exist and absence of spurious points remaining in finite regions.

Taking open hits \(H_U\) and compact misses \(M_K\) as subbasic opens gives Fell topology. Open hits alone do not control extra locations; excessive avoidance conditions would prohibit escape to infinity. This resembles the locality of Chapter 49 vague topology, but is not inherited automatically from it: no measure has been specified.

## 51.5 Add Infinity to Obtain a Compact Shape Space

<a id="sets-hyperspace"></a>

Compactify E to \(X=E\cup\{\infty\}\), and record F by \(F\cup\{\infty\}\). This is always a nonempty compact subset of X, even for empty F. Give X a compact metric r and use the Hausdorff distance

\[ d_H(A,B)=\max\left\{\sup_{a\in A}r(a,B),\sup_{b\in B}r(b,A)\right\}. \]

This hyperspace is genuinely compact: finite ε-nets of X provide finite ε-nets for compact subsets; distance functions of a Hausdorff-Cauchy sequence converge uniformly to distance from a nonempty compact set. Thus it is complete and totally bounded. Compacts containing ∞ form a closed subspace, also compact and Polish. Pulling back gives exactly the preceding open-hit and compact-miss conditions. [T-FELL](../foundations/t-fell.md#fell-polish) supplies the compactification and metric details.

## 51.6 Why Compact-Window Hits Are Measurable Too

<a id="sets-measurability"></a>

For compact K take shrinking open neighborhoods Uₙ whose closures lie in one compact neighborhood and whose intersection is K. If closed F hits each Uₙ, a convergent subsequence of hit points has its limit in F∩K. Consequently

\[ H_K=\bigcap_nH_{U_n},\qquad H_K=M_K^c. \]

Compact hits are therefore Effros-measurable and Fell-closed. Every Fell subbasic set is Effros-measurable; second countability makes each open a countable union of finite subbasic intersections. Hence Effros equals Fell Borel. A countable union-closed family of compact neighborhoods already generates it. To identify laws we can use one countable record, rather than choosing null sets separately at uncountably many positions.

## 51.7 Capacity Records Hits, Not Spatial Mass

<a id="sets-capacity"></a>

Define its capacity functional by \(T(K)=P(F\cap K\ne\varnothing)\) for compact K, with T(∅)=0. For the horizontal-line example, take E to be the unit square and K a compact subset of that square. Then

\[ T(K)=\operatorname{Leb}\bigl(\pi_yK\bigr),\qquad F=[0,1]\times\{U\}. \]

The projection \(\pi_yK\) is compact, so the formula is well-defined. Two disjoint vertical segments at different horizontal positions but with the same height interval are always hit together. Their union has the same capacity as either segment, not twice it. T is not an additive spatial probability measure; it gives probabilities of events in shape space. Confusing the two spaces would obscure the representation conditions.

## 51.8 Can Union Hits Recover Joint Hits?

<a id="sets-identification"></a>

Marginal event probabilities usually do not determine a joint law. But a union of compact windows is another compact window, and capacity includes that reading too. Thus two-window joint hits satisfy

\[ P(H_{K_1}\cap H_{K_2})=T(K_1)+T(K_2)-T(K_1\cup K_2). \]

Inclusion–exclusion similarly recovers every finite combination of hits and misses. Hence T determines all finite joint laws on the countable compact determining family. These generate Fell Borel, so π–λ identifies the entire closed-set law. Capacity is therefore much more than a first-order average. This also explains why singleton capacities alone are insufficient.

## 51.9 Observation Tables Must Not Have Negative Probabilities

<a id="sets-alternation"></a>

Suppose we require avoidance of A and hits of K₁,…,Kᵣ. Expanding its event gives a constraint required for every r:

\[ \sum_{I\subset\{1,\ldots,r\}}(-1)^{|I|}T\!\left(A\cup\bigcup_{i\in I}K_i\right)=-P\left(H_A^c\cap\bigcap_{i=1}^rH_{K_i}\right)\le0. \]

This is complete alternation. First differences give monotonicity; second differences constrain two-hit dependence; higher differences cannot be omitted. On a three-point space, singleton capacities 1/2 and capacities one for every pair or triple give a monotone subadditive T, but assign probability −1/2 to hitting all three. A plausible numerical table need not be the law of any experiment.

## 51.10 Finite Compatibility Must Also Respect Limit Points

<a id="sets-continuity"></a>

If compact Kₙ decreases to K and F hits every Kₙ, closedness and compactness force a hit of K. Thus T(Kₙ) must decrease to T(K). Without this condition finite tables may be consistent while the limiting record cannot be a closed set.

For example, on [0,1] give infinite compact sets capacity one and finite ones zero. It is completely alternating, because a finite union is infinite exactly when some member is infinite. Yet {0}∪{1/k:k≥n} decreases to {0}, with capacities staying one while the limiting singleton has capacity zero. In any representation its countable points would all have zero hit probability, forcing zero for their union. Continuity is no dispensable technical addendum.

## 51.11 Exactly Which Capacities Come from Closed Sets?

<a id="sets-choquet"></a>

We now have reason to formulate representation. On LCSC metric E, a compact-set functional T is the capacity of a unique random closed-set law exactly when it takes values in [0,1], is zero at ∅, is completely alternating, and is continuous along decreasing compact sequences. Random empty sets are allowed; realizations need not always be nonempty. This is the chapter’s Choquet random closed-set representation theorem.

Actual hit events proved necessity. Sufficiency requires converting consistent finite binary tables into a spatial object. Chapter 8 first gives infinite records, not automatically records drawable as a closed set. We now make that conversion; [T-CHOQUET](../foundations/t-choquet.md) retains all common-null-set and arbitrary-compact extension details.

## 51.12 First Construct a Countable Hit Record

<a id="sets-records"></a>

Take compact closed balls with countably dense centers and rational radii, and their finite unions, forming R. They detect all opens from inside and approximate every compact from outside. For a finite record unite the missed windows into A and label required hits Kᵢ. With q=1−T its probability must be

\[ p(A;K_1,\ldots,K_r)=\sum_{I\subset\{1,\ldots,r\}}(-1)^{|I|}q\!\left(A\cup\bigcup_{i\in I}K_i\right). \]

Complete alternation makes these weights nonnegative. Adding the hit and miss possibilities for one bit cancels the new terms, giving the smaller table; summing every bit leaves q(∅)=1. The tables are consistent, so Chapter 8 gives a probability on {0,1}ᴿ with hit bits H(K). They also enforce monotonicity and the maximum rule for unions. Countably many indices let us impose all these relations on one full-probability set.

## 51.13 Build the Open Complement from Zero Records

<a id="sets-realization"></a>

If a compact neighborhood is recorded as missed, its interior should contain no part of the shape. Remove all such interiors and define

\[ F=E\setminus\bigcup_{\substack{L\in R\\H(L)=0}}\operatorname{int}L. \]

This gives a closed set, but its records must still be verified. If H(K)=0, choose outer Lₙ∈R decreasing to K with K⊂int Lₙ. Decreasing capacity continuity and monotone bits force H(Lₙ) eventually to be zero, removing all of K. Conversely, if F misses K, the zero-record interiors cover K. A finite subcover exists; its union bit is zero, and monotonicity forces H(K)=0. Thus every R-record is realized exactly on one full-probability set.

Every open hit is a countable union of appropriate R-hits, making F measurable. For arbitrary compact K, outer approximation from R and decreasing continuity recover P(F hits K)=T(K). Existence is complete, and inclusion–exclusion gives uniqueness. Consistency of finite probabilities, spatial closedness, and probability continuity solve different construction problems.

## 51.14 Capacity Includes the Probability of No Shape

<a id="sets-empty"></a>

For an increasing compact exhaustion Kₘ, every nonempty closed F hits some Kₘ, so

\[ P(F=\varnothing)=1-\lim_{m\to\infty}T(K_m). \]

One cannot casually impose a spatial “total mass one” condition to exclude empty shapes. Capacity is not spatial mass. It already defines total probability one on shape space and separately computes the nonempty part.

## 51.15 What Does This Have to Do with Potential-Theoretic Capacity?

<a id="sets-history"></a>

Choquet’s 1954 Theory of capacities developed set functions, infinite-order alternation, and integral representations. Fell’s 1962 paper studied a Hausdorff topology on closed subsets of locally compact spaces. These are documented historical landmarks. Our organization through countable hit tables is a modern reconstruction, not a claim that the two authors followed one shared discovery route.

Chapter 38 potential-theoretic capacities are related but are not automatically interchangeable with these hitting capacities. Our theorem identifies closed-set hit probabilities satisfying explicit conditions and bounded by one. An analytic capacity may lack that normalization or require separate continuity and representation proofs. A shared name does not substitute for mathematical comparison.

## 51.16 Which Points Must a Converging Shape Keep or Exclude?

<a id="sets-sequences"></a>

Fell convergence has a checkable criterion: every point of limiting F is approximated by points of Fₙ; every convergent selection from a subsequence of Fₙ has its limit in F. The first prevents unapproximated points from appearing in the limit; the second rules out residual finite locations absent from it.

The proof comes directly from open hits and compact misses. If the second condition fails, a compact neighborhood of the extraneous limit separates it from F. If a compact that should be missed is hit infinitely often, compactness produces just such a violating subsequence. Both {n} tending to ∅ and {1/n} tending to {0} are legitimate; escape must be understood with the state space’s treatment of infinity.

## 51.17 Random Convergence Does Not Require Every Compact Reading to Converge

<a id="sets-convergence"></a>

For random closed sets Fₙ and F, distributional convergence means weak convergence on Fell space. Chapter 24 Portmanteau gives different inequalities for open hits and closed hits:

\[ \liminf_nP(F_n\cap U\ne\varnothing)\ge P(F\cap U\ne\varnothing),\qquad\limsup_nT_n(K)\le T(K). \]

If the probability of hitting K without hitting its interior is zero, these bounds imply Tₙ(K)→T(K). General compacts do not qualify: deterministic Fₙ={1/n} already tends to {0}, while its hit probability at K={0} is never one. Exact boundary contact can make a binary reading discontinuous while the sets converge perfectly well.

## 51.18 Enough Continuity Windows Still Determine the Whole Limit

<a id="sets-capacity-limit"></a>

The precise criterion is: for given F, convergence Tₙ(K)→T(K) on every compact with \(T(K)=P(F\cap\operatorname{int}K\ne\varnothing)\) is equivalent to Fₙ⇒F. Capacity uniqueness alone is not a proof. Fell compactness provides a weak further limit Q from every subsequence; we must identify its capacity.

Enlarge arbitrary compact K to a compact distance-neighborhood Kʳ. Except at countably many radii, the random distance from F to K has no atom at r, making Kʳ a valid continuity window. Apply Portmanteau to the subsequential limit using Kʳ and its interior to bound Q’s reading at K. Let valid radii decrease to zero; compact decreasing continuity gives Q(\(H_K\))=T(K). Only then does capacity uniqueness identify the limit. [T-CLOSED-LIMITS](../foundations/t-closed-limits.md#closed-capacity-convergence) proves every inequality direction and the exceptional-radius assertion.

## 51.19 Union Can Be Continuous While Intersection Is Not

<a id="sets-operations"></a>

Finite union is Fell-continuous, so jointly converging random shapes can be united by continuous mapping. Marginal convergences alone do not specify their joint dependence. Intersection can fail even deterministically: {0} and {1/n} both tend to {0}, but their intersections remain empty instead of tending to the intersection of their limits.

A continuous proper spatial map a sends closed sets to closed sets and induces a continuous shape map. Properness makes preimages of points remaining in a compact region have compact subsequences. Without it, even the image of a closed set need not be closed. Before transforming a shape, check that the output remains in the state space.

## 51.20 Support Is Measurable but Can Retain Ghost Locations

<a id="sets-examples"></a>

For Radon μ take its support. For open U, \(\operatorname{supp}\mu\cap U\ne\varnothing\Longleftrightarrow\mu(U)>0\); the complement of support is a countable union of zero-mass base opens, proving the nontrivial direction. Chapter 49 evaluation measurability thus makes random support Effros-measurable.

\[ \mu_n=(1-1/n)\delta_0+(1/n)\delta_1\Rightarrow\delta_0,\qquad\operatorname{supp}\mu_n=\{0,1\}\quad(n\ge2). \]

The supports do not tend to {0}. Even with total mass one and no escape to infinity, a vanishing mass can retain an ever-present location. Measure convergence tests integral readings; support convergence tests existence. One is not obtained by renaming the other.

## 51.21 Why Integer Points Exclude the Small-Mass Counterexample

<a id="sets-point-support"></a>

For locally finite integer point measures, support is continuous from vague to Fell. A limiting point has a positive continuous test reading, forcing eventual points in each neighborhood. A compact K to be avoided has a continuous cutoff at least one on K with limiting integral zero; once the preceding reading is below one, integer counts force no points in K. Arbitrarily small ghost weights cannot occur.

Thus Chapter 48 Poisson support has capacity \(T(K)=1-e^{-\mu(K)}\), and Cox support has \(T(K)=1-Ee^{-\Lambda(K)}\). Closed shape still forgets multiplicities: \(\delta_U\) and 2\(\delta_U\) give exactly the same shape. We have both a legitimate passage from measure to shape and a precise account of information it loses.

## 51.22 How Long Do We Observe a Path’s Range?

<a id="sets-paths"></a>

A continuous path has compact range on [0,t], with \(d_H^\rho(\gamma_n[0,t],\gamma[0,t])\le\sup_{s\le t}\rho(\gamma_n(s),\gamma(s))\). Thus finite-time uniform path convergence gives Fell convergence of ranges, and continuous mapping gives the random version.

Infinite time differs. The path 1/(1+s) has range (0,1], requiring closure to enter our state space. Its closed range hits open U exactly when the path visits U at some rational time, proving measurability. But local uniform convergence does not control infinite ranges. Let γₙ stay at zero until n, rise to one in the next time unit, then remain there. All closed ranges are [0,1], while paths converge locally uniformly to zero. Chapter 24 path topology controls finite windows, not all future times automatically.

## 51.23 When Is a Random Union of Grains Really Closed?

<a id="sets-coverage"></a>

Let Poisson parents carry compact grains and unite their translates. This is not a new icon for a point measure: grains overlap and the result does not retain coverage multiplicity. First ensure that every compact window meets only finitely many grains. For σ-finite parent intensity a and independent grain law Q, assume

\[ I_K=\int a(dx)\int\mathbf1_{\{(x+G)\cap K\ne\varnothing\}}Q(dG)<\infty. \]

Marked Poisson construction makes the number of hit grains have mean \(I_K\), hence finite almost surely. A countable exhaustion gives local finite unions and therefore closedness. The Poisson probability of no hit gives \(T(K)=1-e^{-I_K}\). On the line, grain [−r,r] and homogeneous parent rate κ give I=κ(b−a+2r) on [a,b]. [T-RANDOM-SHAPES](../foundations/t-random-shapes.md#shapes-boolean) proves grain-space measurability, closedness of the union, and the calculation.

One cannot simply delete the condition: place independent Poisson(1) numbers of zero-radius grains at positions 1/n. Infinitely many labels occur almost surely; the union omits zero but accumulates there. Closing it defines a different object that adds a location. Infinite union, closure, and the original occurrence record are different operations.

## 51.24 Local Compactness Is Not Disposable Background

<a id="sets-space-boundary"></a>

Compact Polishness of our closed-set space uses local compactness and second countability of E. In infinite-dimensional Hilbert space, the same open-hit/compact-miss topology cannot even separate ∅ and {0}: finitely many compact sets cannot fill a small ball at zero, leaving a singleton satisfying both finite observation requirements. See [T-FELL](../foundations/t-fell.md#fell-nonlocal).

This does not prohibit random closed sets on general Polish spaces; it limits the unconditional reach of this topology and representation. Changing space requires rechecking compact neighborhoods, countable determining families, boundaries, and convergence.

## 51.25 From Zero Readings to a Full Probability of Shape

<a id="sets-insight"></a>

The zero membership probability at every fixed point remains correct. The mistake was treating it as the whole shape law. Joint window-hit records not only distinguish the line from ∅; under complete alternation and decreasing continuity they construct a unique closed-set law from scratch. Each condition has a task: finite tables cannot contain negative probabilities, limiting hits must retain required contact, and all records must be realized by one spatial object.

Capacity does not manufacture spatial mass; it organizes compatible shape-space events into a probability law. Support, path-range, and coverage examples distinguish existence, mass size, time horizon, and closure as different limit operations. We can now ask probabilistic questions of shapes without predetermined unit mass and know which answers define a legitimate random world.

## 51.26 What Has Not Been Recorded by Shape?

<a id="sets-sources"></a>

A drawn tree can be viewed as a closed set, but its outline alone does not specify ancestry, edge lengths, or movement along genealogical relations. The same external shape can carry different structures. The next problem is not another window-hit number, but a random object preserving genealogy itself.

Complete proofs are in [T-FELL](../foundations/t-fell.md), [T-CHOQUET](../foundations/t-choquet.md), [T-CLOSED-LIMITS](../foundations/t-closed-limits.md), and [T-RANDOM-SHAPES](../foundations/t-random-shapes.md). Historical sources are Choquet’s [1954 paper](https://numdam.org/articles/10.5802/aif.53/) and Fell’s [1962 paper](https://doi.org/10.1090/S0002-9939-1962-0139135-6). We prove the LCSC metric version; other hyperspace topologies and broader representations on non-locally-compact spaces are not automatic consequences.
