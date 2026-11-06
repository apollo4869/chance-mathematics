# Chapter 54: How Does a Brownian Excursion Become a Tree?

After exploring a left branch and before entering a right branch, a walker passes the same junction twice. The contour curve assigns different times to those passages without creating two junctions. Recovering the tree must therefore allow different times to represent the same position.

Chapter 53 scaled conditioned-tree contours into a continuous excursion. Vertex addresses and integer heights have disappeared. What remains is height and how far the traversal descended between visits. The task is not to judge how tree-like a curve looks, but to test whether those readings can support the full rules for positions, distances and ancestry.

## 54.1 Equal height does not mean equal position

<a id="crt-height-not-position"></a>

Start with a piecewise linear curve: rise from 0 to 2, descend to 1, rise to 2 again, then return to 0. The peaks have equal heights, but the descent to 1 means that each must travel down one unit to meet the other. Their distance should be 2, not 0. Height difference alone collapses their tips.

Conversely, the descent to height 1 and a later passage through that same junction should represent one ancestor. The needed information is the minimum over the intervening interval, not merely endpoint heights. Chapter 52 proved this distance calculation on finite trees. The new task is to construct a tree from the calculation when no tree has yet been supplied.

## 54.2 A candidate distance before assuming a tree exists

<a id="crt-pseudo"></a>

\[ h\in C([0,1],\mathbb R_+),\quad h(0)=h(1)=0,\qquad
m_h(s,t)=\min_{s\wedge t\le u\le s\vee t}h(u),\qquad
d_h(s,t)=h(s)+h(t)-2m_h(s,t). \]

For now h is any such continuous function, not necessarily Brownian, and may return to zero internally. The candidate distance adds the descent from h(s) to the interval minimum and the ascent to h(t). This motivates the formula but does not prove it: without a triangle inequality, the interpretation cannot create a metric space.

## 54.3 How minima produce the triangle inequality

<a id="crt-triangle"></a>

The two intervals through a third time u cover the interval between s and t. The original minimum is therefore at least the smaller of the two new minima, while h(u) is at least their larger value. These two small facts fit the proposed distance exactly.

\[ m_h(s,u)+m_h(u,t)-h(u)
\le\min\{m_h(s,u),m_h(u,t)\}\le m_h(s,t),\qquad
d_h(s,t)\le d_h(s,u)+d_h(u,t). \]

Nonnegativity, symmetry and zero self-distance hold too. Thus this is a pseudometric: “pseudo” permits distinct times at zero distance, without weakening the other metric axioms. Zero distance says precisely that the endpoints have equal height and the intervening curve never falls below it.

## 54.4 Identifying repeated visits

<a id="crt-quotient"></a>

\[ s\sim_h t\iff d_h(s,t)=0,\qquad
\mathcal T_h=[0,1]/\!\sim_h,\qquad p_h(t)=[t],\qquad \rho_h=p_h(0)=p_h(1). \]

Transitivity follows from the triangle inequality. Replacing one time by a zero-distance representative does not change its distance to another time: two triangle inequalities give both bounds. The formula therefore descends to a genuine metric on the quotient, still denoted dₕ. The root is the common class of the starting and finishing times, and its distance to pₕ(t) is h(t).

Uniform continuity gives dₕ(pₕ(s),pₕ(t))≤2ωₕ(|s−t|), so projection is continuous. The continuous image of a compact interval is compact, hence complete and connected. We now have a legitimate compact metric space. It has not yet been proved to be a tree.

## 54.5 Recovering the ancestral line to a point

<a id="crt-ancestors"></a>

To walk from the root to x=pₕ(t), we should select its ancestor at each height a. The curve supplies a representative: the last time at or before t when it reaches a. It never falls below a afterward before t, or it would have to cross a again.

\[ r_t(a)=\max\{u\le t:h(u)=a\},\quad x(a)=p_h(r_t(a)),\quad
0\le a\le h(t),\qquad d_h(x(a),x(b))=|a-b|. \]

The intermediate value theorem and closedness guarantee that the last time exists. The minimum between two selected heights is the lower height, proving the isometry. For another representative of the same point, the intervening curve never falls below the endpoint height. Last visits at lower heights consequently agree, and the top representatives are equivalent. The ancestral line belongs to the point, not to an accidental choice of time.

## 54.6 The interval minimum becomes the common ancestor

<a id="crt-common-ancestor"></a>

Let s≤t. The two ancestral lines agree below mₕ(s,t) and still represent the same point at that minimum height. If they agreed higher up, the curve between s and t could not pass through its lower minimum. Their common initial segment therefore ends exactly there. Denote its endpoint by x∧y.

\[ |x|=d_h(\rho_h,x),\qquad
|x\wedge y|=\frac{|x|+|y|-d_h(x,y)}2=m_h(s,t),\qquad
d_h(x,y)=|x|-|x\wedge y|+|y|-|x\wedge y|. \]

Descending from x to the common ancestor and ascending to y gives an isometric segment of the stated length. Intermediate points on different branches share the same ancestor, so their distances are correct too, not just the total length. The idea that a minimum resembles an ancestor has become a theorem about the quotient.

## 54.7 What remains to rule out loops

<a id="crt-no-loops"></a>

It may sound sufficient to say that the shortest path is unique. Yet the plane also has a unique straight segment between two points while allowing other curved arcs. A real tree requires more: every injective continuous arc between the endpoints must have exactly the constructed segment as its image.

The key is separation by points. Choose an interior point z at height a on one branch of the segment. Consider points sharing an ancestor above a with that branch’s endpoint. Common-ancestor height is continuous in the distances, so this set is open. Every point outside it other than z is separated from it by at least its positive distance to z, making the set closed in the space with z removed. The endpoints lie on different sides; every continuous connection must pass through z.

Every arc thus contains the entire constructed segment. An injective arc is homeomorphic to its parameter interval; the inverse image of the segment is connected and contains both endpoints, so fills the interval. No alternative arc remains. Full separation and representative arguments appear in [T-REAL-TREE-CODE](../foundations/t-real-tree-code.md#real-code-arcs).

## 54.8 What the continuous coding theorem proves

<a id="crt-real-tree"></a>

A metric space is a real tree when every pair is joined by an isometric real interval and every injective continuous connection has that same image. We have proved that every continuous nonnegative h vanishing at both endpoints produces a compact rooted real tree (𝒯ₕ,dₕ,ρₕ). Binary branching, strict interior positivity and randomness are not required.

Several peaks may produce multiple branching, and returns to zero may split branches at the root. The zero function gives one point. A tree need not have finitely many vertices or edges: every position along a segment is a point, branching may be infinite, but there is no loop offering a detour.

## 54.9 Traversal time becomes mass

<a id="crt-mass"></a>

\[ \mu_h(A)=\operatorname{Leb}\{t\in[0,1]:p_h(t)\in A\},\qquad
\int f\,d\mu_h=\int_0^1f(p_h(t))\,dt. \]

Once time is no longer position, where does duration go? It supplies sampling weights. Select a uniform time in [0,1] and take the tree point it represents: its law is μₕ. Continuous projection makes this a Borel measure, and on the compact space it is Radon. Every nonempty open set has a relatively open inverse image of positive duration, so μₕ has full support.

Mass is not automatically edge length. A code may pause at the tip of a segment without changing its quotient metric, while giving the tip an atom. Root, distance and mass are data to preserve separately. Diffuseness in the Brownian case still needs proof; it cannot be read off a drawing of thin branches.

## 54.10 Not every curve or record has the required properties

<a id="crt-boundaries"></a>

Delete continuity and take h equal to 1 on [1/3,2/3) and zero elsewhere. The quotient has two points at distance 1, without intermediate points or a segment. The pseudometric formula still makes sense, but the real-tree conclusion fails. Replacing the interval minimum by the smaller endpoint height gives absolute height difference: it may define a segment, yet loses the branching between the two initial peaks.

Interior zeros and plateaux are not forbidden; they may change root branching or mass. Some continuous functions outside this chapter’s class also code trees. We have not proved that every nonclosed or sign-changing function fails. Our stated conditions suffice for a closed traversal, root heights, a compact real tree and probability mass together.

## 54.11 Applying the deterministic construction to a random excursion

<a id="crt-random-construction"></a>

Now take the duration-one standard Brownian excursion e from Chapters 37 and 53, with variance units inherited from standard Brownian motion. Applying the deterministic theorem samplewise gives (𝒯ₑ,dₑ,ρₑ,μₑ), a rigorous construction of the Brownian continuum random tree, or Brownian CRT. It is not defined through a spatial limit of conditioned trees, so creates no circularity with Chapter 55.

Randomness needs an explanation beyond saying that a formula contains a random function. Select k independent mass samples, evaluate a bounded continuous function of their root distances and pairwise distances, and average over them. All these readings are integrals over [0,1]ᵏ. A uniform change δ in h changes every distance by at most 4δ, so the readings depend continuously on h. Measurability of e passes to the tree readings.

Use the sigma field generated by these readings on root-preserving measure-preserving isometry classes. They identify each compact full-support measured space: infinite iid samples are almost surely dense, their distance array identifies the dense sets isometrically, completeness extends the isometry, and the empirical-measure strong law recovers mass. The actual reconstruction proof is in [T-CRT-RANDOMNESS](../foundations/t-crt-randomness.md#crt-random-identification). GH/GP/GHP topologies for comparing spaces remain for Chapter 55.

## 54.12 The same name requires matched length units

<a id="crt-normalization"></a>

\[ \mathcal T=\mathcal T_e,\qquad
d_{2e}=2d_e,\qquad \mu_{2e}\ \text{corresponds to }\mu_e
\ \text{under the natural identification of quotient points}. \]

We use the e-coded version, matching the σ/(2√n) contour normalization of Chapter 53. Another common Aldous normalization uses 2e: all edge lengths double and mass stays the same. Both are scale versions of the Brownian CRT. Densities must specify which is used; a different Rayleigh parameter cannot silently enter a root-height formula.

## 54.13 First examine a few randomly sampled descendants

<a id="crt-reduced"></a>

The whole tree may have infinitely many branches. Choose finitely many independent uniform times U₁,…,Uₖ, put Xᵢ=pₑ(Uᵢ), and retain the union Rₖ of their paths to the root. This is a finite reduced subtree. Each additional ancestral line meets the existing span in a closed initial segment and adds at most one segment at one attachment point. Thus Rₖ genuinely consists of finitely many segments.

Order the sample times t₁<⋯<tₖ. Only xᵢ=e(tᵢ) and adjacent minima yᵢ are needed; a nonadjacent minimum is the smallest intervening y. Recursively splitting at the smallest y recovers the reduced tree. Its total edge length is L=Σxᵢ−Σyᵢ: the first point contributes x₁, and each subsequent one adds xᵢ−yᵢ₋₁ above its common ancestor with the preceding point.

## 54.14 To calculate branching, calculate minimum probabilities

<a id="crt-minimum-density"></a>

Excursion heights alone cannot determine the law of Rₖ: they omit how far two visits descend together. A moving barrier supplies the missing joint information. For positive endpoints x,z, the transition kernel for a segment staying above y is below, obtained by shifting the reflection formula of Chapter 26 to height y.

\[ \begin{aligned}
g_t(z)&=\frac{e^{-z^2/(2t)}}{\sqrt{2\pi t}},\qquad
q_t^{(y)}(x,z)=g_t(z-x)-g_t(x+z-2y),\\
-\partial_yq_t^{(y)}(x,z)&=2h_t(x+z-2y),\qquad
h_t(a)=\frac{a\,e^{-a^2/(2t)}}{\sqrt{2\pi}t^{3/2}}.
\end{aligned} \]

The excursion density in §53.11 uses q⁽⁰⁾ on each intervening segment. Given endpoints, the segments are independent killed bridges. Replacing q⁽⁰⁾ by q⁽ʸ⁾ and differentiating the barrier gives the minimum density. The function hₜ(a) is precisely a first-passage time density, linking spatial descent distances to Brownian hitting times in a calculable way.

## 54.15 Why only total length remains in the density

<a id="crt-total-length"></a>

\[ r_0=x_1,\quad r_i=x_i+x_{i+1}-2y_i\ (1\le i<k),\quad r_k=x_k,\qquad
\sum_{i=0}^{k}r_i=2L,\qquad h_\cdot(a)*h_\cdot(b)=h_\cdot(a+b). \]

The distances traveled from the root to the first sample, through the samples and back to the root are r₀,…,rₖ. First-passage convolution comes from the strong Markov decomposition at successive levels a and b. Integrating out the sample times convolves over positive time intervals summing to 1, combining the k+1 distances into 2L.

Including the order-statistic density k!, the joint density of heights and minima is 2ᵏ⁺¹k! L exp(−2L²). A total-length formula has not simply been guessed from symmetry: first-passage convolution actually eliminates the individual segment times. Edge coordinates and labels determine the remaining coefficient.

## 54.16 The complete finite reduced-subtree law

<a id="crt-sampling-law"></a>

Theorem. For each k≥1, Rₖ almost surely has a degree-one root, k distinct labeled leaves and k−1 degree-three branch points. Suppressing unmarked degree-two points leaves 2k−1 positive-length edges. Forget the plane order and fix any such labeled binary shape τ. Its joint edge-length density is

\[ \boxed{
P\{\operatorname{shape}(R_k)=\tau,\ (\ell_a)\in d\ell\}
=4^kL e^{-2L^2}\prod_{a\in E(\tau)}d\ell_a,\qquad
L=\sum_{a\in E(\tau)}\ell_a,\quad\ell_a>0.\ } \]

The final proof steps can be seen directly. Jointly continuous minima exclude tied branching heights and zero edges, yielding a binary shape. For a fixed plane shape, x,y are the absolute heights of all nonroot vertices. Passing to parent–child height differences has Jacobian 1. Original sample labels are uniformly permuted among the ordered times, dividing by k!; forgetting the left–right choices at k−1 branches multiplies by 2ᵏ⁻¹. Thus 2ᵏ⁺¹k! becomes 4ᵏ.

The full arguments for barrier conditional kernels, first-passage convolution, coordinate regions and all constants are in [T-CRT-SAMPLING](../foundations/t-crt-sampling.md), including verification that the density accounts for all probability and misses no degenerate boundary.

## 54.17 Shape, total length and edge proportions

<a id="crt-shape-length"></a>

The number of nonplane labeled shapes is (2k−3)!!, equal to 1 for k=1. Adding a new leaf selects one of the 2k−1 old edges to subdivide and attach the leaf; deleting the last label and suppressing a degree-two vertex reverses the operation. Since the density is the same for every shape, shape is uniform.

\[ 2L_k^2\sim\operatorname{Gamma}(k,1),\qquad
(\ell_a/L_k)_{a\in E(\tau)}\sim\operatorname{Dirichlet}(1,\ldots,1). \]

At fixed total length the density is constant on the positive-edge simplex, so proportions are uniform; shape, total length and proportions are independent. Multiply by simplex volume L²ᵏ⁻²/(2k−2)! and substitute z=2L² to obtain the Gamma law and check probability 1/(2k−3)!! for each shape. Uniform proportions do not mean equal edge lengths; they remain random simplex coordinates.

\[ P\{d_e(\rho_e,X_1)\in dr\}=4r e^{-2r^2}\,dr,\quad r>0;\qquad
P\{2d_e(\rho_e,X_1)\in dr\}=r e^{-r^2/2}\,dr. \]

One sample is already a sensitive normalization check. It distinguishes the Rayleigh densities of our e version and the common 2e version, in agreement with the σ/(2√n) height factor in Chapter 53.

## 54.18 How one more sample adds a branch

<a id="crt-add-sample"></a>

Adding an independent sample in the same CRT cannot mean resampling the old finite tree. Deleting the final leaf must recover the previous span. With old total length s, new branch length b and attachment length-coordinate a, the density ratio gives

\[ \frac{4(s+b)}s e^{-2((s+b)^2-s^2)}\,da\,db,\qquad
2L_{k+1}^2-2L_k^2\mid R_k\sim\operatorname{Exp}(1). \]

Attachment is uniform in old total edge length; the conditional density of the new length is 4(s+b)exp{−2((s+b)²−s²)}, integrating to 1. This verifies deletion consistency and suggests segment-by-segment growth. Starting from these finite kernels to construct a separate complete infinite tree still requires proving that its completion and mass exist. Consistency of finite samples has not yet solved that growth-construction problem.

## 54.19 Why mass lies on leaves yet sees the whole tree

<a id="crt-leaf-mass"></a>

Two independent mass samples almost surely have strictly positive distance. Their expected conditional collision probability is zero, excluding all atoms of μₑ by nonnegativity. Now take a conditionally iid sequence: every sample is a leaf in every finite reduced span. If the first sample had a strict descendant in the whole tree, full support would give that descendant direction positive mass, and a later sample would enter it. The first would become internal to some finite span, a contradiction. Thus μₑ is concentrated on leaves.

This does not contradict full support. Every open ball has positive leaf mass without giving positive mass to each arc inside it. Indeed, the interior of a nondegenerate arc contains no leaves and the endpoints have no atoms, so the entire arc has mass zero. The union of finite reduced spans can be dense while having zero mass. Mass specifies sampling, not a length inventory of all possible positions.

## 54.20 How finite samples constrain all branching

<a id="crt-binary-reroot"></a>

Conditionally iid samples are almost surely dense, since the probability of missing a positive-mass basic open set forever is zero. If the whole tree had a point of degree four or more, dense samples would hit four of its open components. Some finite reduced span would then have a degree-four point, contradicting the sampling density. Brownian CRT branch points therefore all have degree three, unlike general continuous codes. One common good event excludes all higher branching; no uncountable collection of pointwise null sets is being combined.

Viewing the root as an extra leaf label 0, the finite density is symmetric in the root and sample labels. Rerooting at a uniform mass point thus preserves every finite distance-reading law. This does not make the root indistinguishable from all positions in each fixed realization. It is an equality of rooted probability laws after random rerooting. Full proofs of measurability, leaf mass, binary branching and rerooted readings are in [T-CRT-RANDOMNESS](../foundations/t-crt-randomness.md).

## 54.21 Limits of what the code and samples identify

<a id="crt-information"></a>

Changing traversal speed may preserve the metric tree but change mass. Changing left–right visiting order may preserve the same rooted measured tree. Thus the construction does not produce an object forever retaining its original time coordinates. Quotienting forgets repeated-visit labels, minima retain ancestry, and pushforward mass retains the chosen time-sampling weights.

All finite sample-distance laws identify a compact full-support measured tree, but one fixed small sampled subtree cannot recover an entire realization. The former uses the probability structure at every sample size; the latter supplies only finitely many observations. These meanings of identification must remain distinct, just as writing a code is not proving a real-tree theorem.

## 54.22 The excursion has now become geometry

<a id="crt-insight"></a>

The two passages through the initial junction are now literally one quotient point. Equal-height peaks separated by a lower descent remain on different branches. The triangle inequality ensures consistent distances, ancestral lines and cut points ensure unique arcs, and continuity ensures compactness. A tree-like picture has been replaced by the conditions proving a tree exists.

The random excursion gives more than existence. Reduced shapes and edge lengths between uniform mass samples can be calculated exactly; mass lies almost entirely on leaves, while skeleton length cannot replace that probability. Time has not become a literal ancestral axis. It is first quotiented, then pushed forward into sampling mass. Distance construction and the sampling theorem jointly support that distinction.

One concrete question remains. Chapter 53 made discrete contours approach e, and we have now constructed 𝒯ₑ. But what does approaching mean for trees without common coordinates? How should a function error control tree distances, and how can mass be compared as well? Tools for comparing spaces themselves are needed before a curve limit becomes a random geometric limit.

## 54.23 Proof entries and historical boundaries

<a id="crt-sources"></a>

Complete proofs are in [T-REAL-TREE-CODE](../foundations/t-real-tree-code.md), [T-CRT-SAMPLING](../foundations/t-crt-sampling.md), and [T-CRT-RANDOMNESS](../foundations/t-crt-randomness.md). They establish deterministic unique arcs, finite sampling densities and random-mass identification. The chapter retains the obstacles, central calculations and proof mechanisms. GH/GP/GHP and spatial convergence in Chapter 55, complete growth constructions in Chapter 57 and general Lévy trees in Chapter 58 are not proved here.

Aldous developed continuum random trees and their finite sampling structure in his 1991 papers and the third paper in 1993; the [1993 author paper](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf) also treats continuous limits of general finite-variance conditioned families. Le Gall’s [2005 author survey, §2](https://arxiv.org/pdf/math/0511515), develops real-tree coding and excursion marginal calculations. Our sequence of identification, unique arcs, mass and barrier-based sampling is a modern reconstruction, not an invented shared historical discovery.

The earlier [CRT introduction](../advanced/crt.md) supplied a pseudometric and conceptual diagram. We now have mathematical arguments for how interval minima retain ancestry, how the quotient excludes loops and how traversal mass enters sampling. A schematic curve helps reveal the construction but cannot replace these arguments, and is not a Brownian sample.
