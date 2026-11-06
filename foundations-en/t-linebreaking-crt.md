# T-LINEBREAKING-CRT: The 4r Clock, Infinite Compact Tree and Empirical Mass

This page closes the direct Brownian construction in [Chapter 57](../chapters/57-regenerative-growth.md#growth-linebreaking). Inputs are Chapter 54’s actual sampling density, compactness, full support and sample strong law, and Chapter 55’s measurable metric-space framework. No excursion is used as random input to growth. Identification with the excursion tree is a proof tool, not a substitute for constructing the growth kernel.

## 1. Construct lengths and measurable grafts first

<a id="line-clock"></a>

\[ E_i\overset{\mathrm{iid}}\sim\operatorname{Exp}(1),\qquad S_k=\sum_{i=1}^k E_i,\qquad L_k=\sqrt{S_k/2},\quad L_0=0,\qquad \ell_{k+1}=L_{k+1}-L_k. \]

Start with a segment of length L₁, rooted at one endpoint and with the other labeled 1. The finite tree Rₖ has total length Lₖ. An independent uniform Vₖ selects a point from its length interval [0,Lₖ): order edges measurably, for example by descendant-label codes, locate the cumulative-length interval and then the position within the edge. Graft a new segment of length ℓₖ₊₁ and label its endpoint k+1. Old distances stay unchanged. Vertices have zero length mass; a countable union excludes grafts at vertices. Each tree is binary with strictly positive edges.

\[ P(L_{k+1}>r\mid L_k=s)=e^{-2(r^2-s^2)},\quad r\ge s;\qquad f(r\mid s)=4r e^{-2(r^2-s^2)}\mathbf1_{r>s}. \]

Independent exponential increments identify the Lₖ as arrival locations of an inhomogeneous Poisson process with cumulative intensity 2r² and intensity measure 4r dr, also obtainable by Chapter 21’s exponential time change. The strong law gives Sₖ/k→1 and Lₖ→∞, so bounded length windows contain finitely many arrivals. Here k counts added leaves and r denotes cumulative skeleton length, not physical time.

## 2. Induction for the finite density and deletion consistency

<a id="line-density"></a>

\[ f_k(\tau,\ell)=4^kL e^{-2L^2},\qquad \ell\in(0,\infty)^{2k-1},\quad L=\sum_a\ell_a. \]

Density is with respect to counting measure on nonplane labeled binary rooted shapes and Lebesgue edge lengths. The base case is the density of L₁. Given old total s, graft location a and new branch b have density 4(s+b)exp{−2((s+b)²−s²)} da db/s. Splitting an edge has Jacobian 1. Deleting leaf k+1 and suppressing its degree-two vertex uniquely recovers the old tree and a,b. Multiplication proves fₖ₊₁. The kernel integrates to one: old-tree length integration gives s and the remaining b-integral is a survival derivative.

This independently verifies that growth preserves Chapter 54’s density. Symmetry of fₖ in leaf labels gives the Rₖ₋₁ law after deleting any specified leaf and relabeling, hence consistency for every finite subset. Restrictions to initial labels equal the earlier Rₘ pathwise. The former is distributional sampling consistency; the latter alone is merely a property of the grafting construction.

## 3. Identify the whole growth sequence, not just its marginals

<a id="line-sequence"></a>

In the already constructed Tₑ, take conditionally iid mass samples ξ₁,ξ₂,… and their rooted spans Rₖᵉ. Chapter 54’s density ratio gives exactly the preceding graft kernel. It is conditional on the entire past: deleting larger labels from Rₖᵉ recovers every earlier Rⱼᵉ, so that past is a measurable function of the current labeled tree. The same initial law and conditional kernels therefore give identical joint tree-sequence laws for every finite N.

Finite labeled length-tree spaces are countable unions of finite-shape positive orthants, hence standard Borel. Countable-product uniqueness promotes the joint identities to equality of entire sequence laws, equivalently all rooted leaf-distance arrays. Compactness and mass below are measurable properties of that countable record, and can therefore be transferred. Equality of one-time marginals alone would not justify this step.

## 4. Completion and a compactness criterion for nested finite trees

<a id="line-completion"></a>

Include Rₖ isometrically using its actual grafts. Let R° be the increasing union and T its metric completion. Every finite collection in the union lies in a finite real tree, so the four-point tree inequality holds and passes to completion. To construct a segment from x to y, approximate endpoints by xₙ,yₙ in the union and parameterize their segments by fraction u. Put δ=d(xₙ,xₘ)+d(yₙ,yₘ), let I=[xₙ,yₙ], and project a fraction-u point z′ of the other segment onto I at p. In a finite tree distance to a convex segment decreases toward an attachment and then increases, so d(z′,p)≤δ. Also |d(xₙ,p)−d(xₘ,z′)|≤d(xₙ,xₘ)+δ and the two segment lengths differ by at most δ. Thus p is within 3δ of the fraction-u point of I, giving total error at most 4δ. All comparisons occur in a finite tree. The segments are uniformly Cauchy and their limit is an isometric segment from x to y.

\[ d(x,y)+d(z,w)\le\max\{d(x,z)+d(y,w),d(x,w)+d(y,z)\}. \]

The four-point inequality identifies points at the same distance from x on any two x-to-y segments, giving geodesic uniqueness. For uniqueness among all simple arcs, remove an interior point z. The relation d(a,b)<d(a,z)+d(z,b) defines direction classes; the four-point inequality gives transitivity and small balls make them open. The endpoints lie in distinct classes, so every continuous arc passes through z. An excursion of a simple arc outside the segment must return through the same attachment point, contradicting injectivity. Thus T is a real tree.

\[ \Delta_n=\sup_{j\ge1}d(x_j,R_n)=\sup_{j\ge1}\min_{1\le i\le n}\frac{d(\rho,x_j)+d(x_j,x_i)-d(\rho,x_i)}2.\qquad T\text{ compact}\ \Longleftrightarrow\ \Delta_n\to0. \]

The formula is projection distance to a root segment, and Rₙ is their union. Rooted convexity makes distance from Rₙ nondecreasing along a root-to-leaf path, so the supremum over the whole union equals the supremum over leaf endpoints. If Δₙ→0, a finite ε-net in Rₙ becomes a 2ε-net for the union; its completion is totally bounded and compact. Conversely density of the union in compact T gives a finite cover with centers approximated in some Rₙ; nesting then gives Δₙ→0. The criterion is Borel in the countable distance array.

## 5. Compactness actually holds

<a id="line-compactness"></a>

The comparison model Tₑ is compact with full-support mass. Conditional on the tree, iid samples eventually hit every positive-mass ball of a countable base, so they are dense on one common good set. Hence their finite spans approach the whole tree in Hausdorff distance: Δₙᵉ→0. Equality of whole-sequence laws and the Borel criterion transfer this probability-one event to direct growth, proving its completion compact. Compactness is not assumed in identification: the direct model uses only E,V, and the property is proved using a verified comparison realization.

Vanishing new-branch lengths would not suffice. At step n graft length 1/n at distance 1/(4n) below the newest tip, preserving every old leaf. The new tip gains root height 3/(4n), so heights are unbounded despite vanishing new lengths, while infinitely many unit branches at the root have bounded diameter but fail compactness. Brownian Lₙ→∞ is compatible with compact T: total skeleton length and maximum distance from a finite span control different quantities.

## 6. Mass must be constructed separately

<a id="line-mass"></a>

\[ \mu_n=\frac1n\sum_{i=1}^n\delta_{x_i},\qquad \mu_n\Longrightarrow\mu\ \text{a.s. on the completed }T. \]

First test whether μₙ is Cauchy in Prokhorov distance on T. The distance between two finite empirical measures depends only on their finite distance matrix: Chapter 55’s Strassen criterion asks whether a finite coupling matrix places at least 1−ε mass on pairs at distance at most ε. Rational ε and finite linear constraints give Borel readings, and the Cauchy event is countable. In Tₑ the countable continuous-test strong law gives empirical convergence to μₑ. The Cauchy event thus has probability one and transfers to direct growth. Completeness of probabilities on compact T gives a unique limit μ.

Finite Rₙ with μₙ are measurable rooted GHP elements by their coordinates and finite couplings. Hausdorff and measure convergence in the common completion give rooted GHP convergence to (T,ρ,μ), hence a measurable random measured tree. Couple its full distance array with the comparison array, identify the dense rooted spans isometrically and extend to completion. The isometry pushes every empirical μₙ forward and therefore pushes μ to μₑ. Thus the full rooted measured-tree law is identified, not just finite shapes.

The nonatomic, full-support, leaf-supported mass properties transfer from Tₑ. After forgetting growth labels, intrinsic sampling readings satisfy the conditional iid μ identities: test jointly against a bounded measurable function of the limiting tree and a finite distance test, use the comparison model and transfer through whole-sequence and GHP-limit identification. This does not say the earliest leaves remain fresh independent samples after revealing the entire labeled growth history. Finite empirical mass is discrete and normalized finite-tree length is diffuse; they are not equal. Infinite total skeleton length is not normalized to define μ.

## 7. Scale check and scope

<a id="line-scale"></a>

\[ 2L_k^2\sim\operatorname{Gamma}(k,1),\qquad \widetilde L_k=2L_k:\quad \frac{\widetilde L_k^2}{2}\sim\operatorname{Gamma}(k,1),\quad\text{intensity }r\,dr. \]

Thus 4r dr belongs to standard e and r dr to 2e. Doubling every branch transforms one into the other; changing the clock density without changing geometry loses a factor two. The argument closes Brownian direct growth, compact completion, mass and equivalence with Chapter 54. It does not construct non-Brownian regenerative CRTs from arbitrary Markov branching or CRP rules, nor establish stable trees, ICRTs or multifurcating models. Independent expert review remains open. [Return to the chapter](../chapters/57-regenerative-growth.md#growth-infinite-crt).
