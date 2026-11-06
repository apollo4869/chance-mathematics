# T-PROKHOROV-COUPLING: From Set Inequalities to Mass Couplings

This page proves the probability-distance tools for [Chapter 55](../chapters/55-metric-measure-limits.md#geometry-prokhorov). S is Polish with a compatible complete metric and all measures are Borel probabilities. Prerequisites are Portmanteau and Prokhorov tightness from Chapter 24, conditional kernels on fixed Polish spaces from Chapter 10 and countable kernel construction from Chapter 8. The Strassen argument is proved here without using GP completeness.

## 1. Definition and the easier implication

<a id="prok-definition"></a>

\[ \begin{aligned}
A^\varepsilon&=\{x:d(x,A)<\varepsilon\},\\
d_P(\mu,\nu)&=\inf\{\varepsilon>0:\,
\mu(A)\le\nu(A^\varepsilon)+\varepsilon,\
\nu(A)\le\mu(A^\varepsilon)+\varepsilon
\ \text{for every Borel }A\}.
\end{aligned} \]

Neighborhoods are open. The distance is at most 1. Continuity from above and approximation by closed sets show that dP=0 forces equality on closed sets and hence equality of measures. If a coupling q assigns mass at most ε to pairs at distance greater than ε, then for any δ>ε, a first coordinate in A has its second coordinate in the δ-neighborhood of A except on bad pairs. Thus dP≤ε. Iterating neighborhoods and adding their radii proves the triangle inequality directly; symmetry is built into the definition.

## 2. Proof of a finite weighted matching lemma

<a id="prok-hall"></a>

Let finitely many row masses aᵢ and column masses bⱼ each sum to 1, with transport allowed on specified cells. Write N(I) for the columns accessible from rows I. If a(I)≤b(N(I))+α for every I, at least 1−α mass can be transported through allowed cells. There is no need to pretend real masses are integers: maximize total transported mass over the finite compact polytope of admissible flows to obtain f.

Start from all unsaturated rows. Move from rows to columns along allowed edges and backwards from columns along edges carrying positive flow. Reaching an unsaturated column would give a finite simple augmenting path with strictly positive residual capacity, contradicting maximality. Hence reachable columns are saturated and are exactly N(I), where I is the set of reachable rows. No external row sends positive flow into N(I), since it would then be reachable. All rows outside I are saturated. Thus unmatched mass equals a(I)−b(N(I))≤α. The remaining equal masses on the two sides can be paired by their normalized product, completing a probability coupling.

## 3. From finite matching to a Strassen coupling

<a id="prok-strassen"></a>

\[ d_P(\mu,\nu)\le\varepsilon
\quad\Longleftrightarrow\quad
\exists q\in\operatorname{Cpl}(\mu,\nu):
q\{(x,y):d(x,y)>\varepsilon\}\le\varepsilon . \]

It suffices to construct a coupling for ε<1. Choose α>dP and compact sets each carrying at least 1−δ mass. Partition each into finitely many Borel cells of diameter at most 2δ and choose centers; the remainder is tail cell 0. Allow every cell involving a tail. Allow other pairs when their centers are at distance at most α+4δ. For a row subset I, let A be its union. If I includes the tail, all columns are neighbors. Otherwise A enlarged by α meets only neighboring columns: two cells with points less than α apart have centers at distance at most α+4δ. The set inequality therefore gives the weighted matching condition.

At least 1−α mass is matched. Spread each cell transport using the product of the normalized restrictions of its marginal measures; zero-mass cells require no normalization. Matched non-tail pairs are at distance at most α+8δ, while pairs involving tails have mass at most 2δ. The completed coupling thus has mass at most α+2δ beyond distance α+8δ. Let α decrease to ε and δ to zero. These couplings are uniformly tight because their marginals are fixed: outside compact K×L their mass is at most μ(Kᶜ)+ν(Lᶜ). Chapter 24 gives a weakly convergent subsequence q. Its marginals remain μ and ν by continuity of projections.

For each η>0, the closed set {d≤ε+η} eventually carries mass at least 1−α−2δ. The closed-set Portmanteau inequality yields q{d≤ε+η}≥1−ε; let η decrease to zero. This obtains the exact threshold even if the defining infimum was not initially attained. The other implication was proved in Section 1.

## 4. It metrizes weak convergence

<a id="prok-weak"></a>

If dP(μₙ,μ)→0, apply the definition to a closed F and let neighborhood radii decrease to zero. This gives limsup μₙ(F)≤μ(F), hence weak convergence by Portmanteau. Conversely suppose μₙ⇒μ. Choose a compact K carrying mass 1−η and cover it by finitely many balls of radius below η with μ-null boundaries. Such radii exist because only countably many disjoint spheres at a fixed center can have positive μ-mass. Taking successive differences yields finite cells of diameter below 2η and a residual cell of μ-mass at most η, all with μ-null boundaries.

Cell masses converge. Match the smaller of the two masses within each identically named cell. Total unmatched mass is half the sum of the finitely many absolute cell-mass differences and tends to zero. Bad mass in the residual cell is at most η+o(1), and other matched pairs are less than 2η apart. The easy coupling implication gives limsup dP≤2η; let η tend to zero. Thus coupling was not adopted as an unproved definition of weak convergence.

## 5. Gluing couplings and completeness

<a id="prok-complete"></a>

Given q₁ coupling μ,ν and q₂ coupling ν,ζ, disintegrate over their common middle coordinate y into K₁(y,dx), K₂(y,dz). The measure ν(dy)K₁K₂ is a triple coupling. This uses Chapter 10 conditional kernels on Polish spaces, not arbitrary measurable spaces. Adding the two bad events bounds the endpoint coupling error.

Take a subsequence of a dP-Cauchy sequence with successive distances below 2⁻ⁱ. Choose adjacent Strassen couplings and use conditional kernels and Chapter 8 to realize a chain Yᵢ. The probability of a step longer than 2⁻ⁱ is at most 2⁻ⁱ. Borel–Cantelli leaves only finitely many bad steps. Subsequent distances have finite sum, so completeness of S gives Yᵢ→Y almost surely; the limit of measurable maps is measurable. If no bad step occurs after N, then d(Y(N),Y)≤Σᵢ≥N2⁻ⁱ; the probability of any such bad step is also at most this tail sum. The easy implication gives convergence in dP to LawY, and the full Cauchy sequence converges.

Finally project a compact set carrying most mass onto a finite net in a fixed countable dense set and approximate weights rationally. This gives a countable dense set of finite atomic probabilities. The probability-measure space is complete and separable under dP. This applies after different geometries have been glued into a common background, which need not be compact. Return to [Chapter 55](../chapters/55-metric-measure-limits.md#geometry-strassen).
