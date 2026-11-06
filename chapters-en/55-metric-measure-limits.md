# Chapter 55: How Can Two Random Geometric Spaces Be Close?

A family tree with ten thousand members can be drawn broadly or squeezed into a narrow strip of paper. Pixel distances between those drawings have no genealogical meaning. What must survive a change of drawing is the distance traveled through ancestors from one member to another, and the chances of sampling members from different parts of the family.

We have contour curves for discrete trees and real trees constructed from continuous excursions. A mathematical bridge is still missing between “the curves approach one another” and “the trees approach one another.” Functions share a time interval; points in different trees need not even have common names. A convenient common drawing cannot stand in for the trees themselves.

## 55.1 A long branch can be sampled very rarely

<a id="geometry-branch"></a>

Separate two requirements first. Let X=[0,1] be rooted at0 with uniform mass. Attach an edge of length2 to the left of its root, giving Y=[−2,1]. Put mass1−ε uniformly on the original interval and ε uniformly on the new branch, writing \(μ_ε\). Among k independent samples, the probability of seeing the added branch is at most kε. If it is not sampled, all distances among the samples and the root agree with those from the original interval.

\[ \mu_\varepsilon=(1-\varepsilon)\,\mathrm{Unif}[0,1]
+\varepsilon\,\mathrm{Unif}[-2,0],
\qquad \operatorname{diam}Y=3,\quad\operatorname{diam}X=1. \]

Yet the branch has not shortened. A distance observing the whole geometry cannot erase it merely because it is rarely sampled. Neither observation is mistaken. We have asked two different questions: to preserve the entire shape and to preserve the mass structure visible to random sampling. We need distances answering each question and then answering both together.

## 55.2 No shared coordinates, but a possible shared space

<a id="geometry-common"></a>

For compact sets A,B already inside a metric space Z, Hausdorff distance measures how far each point is from the other set. Both directions matter: proximity from A to B alone does not exclude an extra long branch in B.

\[ d_H^Z(A,B)=\max\left\{
\sup_{a\in A}\inf_{b\in B}d_Z(a,b),
\sup_{b\in B}\inf_{a\in A}d_Z(a,b)\right\}. \]

Now allow isometric embeddings: relative positions may change, but no internal distance may change. Minimize the Hausdorff distance over all common spaces and such embeddings. This gives Gromov–Hausdorff distance. We are not optimizing a drawing in a predetermined Euclidean space; the common metric background itself may vary.

\[ d_{GH}(X,Y)=\inf_{Z,\phi,\psi}
d_H^Z(\phi(X),\psi(Y)),
\qquad \phi,\psi\ \text{isometric}. \]

The definition appears to allow enormous freedom. Could clever placement make two different spaces have distance zero? Answering that requires a comparison using only their internal distances.

## 55.3 A correspondence need not be a bijection

<a id="geometry-correspondence"></a>

A finite vertex tree and a continuous tree usually have different cardinalities, so bijection is the wrong requirement. Use a relation R⊂X×Y assigning at least one partner to every point on both sides. Such a relation is a correspondence. It allows a small cluster to represent one region of the other space while demanding approximate agreement of internal distances. Its distortion is

\[ \operatorname{dis}R
=\sup_{(x,y),(x',y')\in R}
|d_X(x,x')-d_Y(y,y')|. \]

If corresponding points are within r in a common background, two triangle inequalities give distortion at most2r. The important converse is that small internal distortion allows construction of an ambient metric preserving both internal metrics. External placement becomes a computable intrinsic condition.

## 55.4 Why distortion carries a factor one-half

<a id="geometry-bridge"></a>

\[ \rho_c(x,y)=
\inf_{(a,b)\in R}\{d_X(x,a)+c+d_Y(b,y)\},
\qquad c>\tfrac12\operatorname{dis}R. \]

Connect each corresponding pair by a bridge of length c. The formula permits travel inside X, across a bridge and then inside Y. An internal shortcut using two bridges is ruled out precisely when2c covers the distance distortion. For example, a route crossing into Y and back has length at least dX(x,a)+2c+dY(b,b′)+dX(a′,x′), while2c+dY(b,b′)≥dX(a,a′). It cannot shorten dX(x,x′). The other mixed triangle inequalities follow by concatenating routes.

\[ d_{GH}(X,Y)=\frac12\inf_R\operatorname{dis}R. \]

Letting the bridge length decrease to half the distortion proves one direction; near pairs in an ambient embedding prove the other. [T-GH](../foundations/t-gh.md#gh-equivalence) also proves that zero distance gives an onto isometry: take a compactness diagonal limit of approximate partners of countably many dense points, extend the map and use surjectivity to exclude missing points. Thus the metric is on compact isometry classes. Coordinates and names disappear, but internal distances are retained.

## 55.5 The root is part of the object

<a id="geometry-root"></a>

For a genealogical tree the root determines ancestry. Even identical unrooted shapes give different ancestral distances if rooted at a midpoint or endpoint. Rooted GH additionally controls the roots in the same ambient embedding, using a maximum. Equivalently minimize half the distortion over correspondences containing the root pair.

\[ d_{rGH}(\mathsf X,\mathsf Y)=
\inf_{Z,\phi,\psi}\max\{d_H^Z(\phi X,\psi Y),
d_Z(\phi\rho_X,\psi\rho_Y)\}. \]

The phrase “same embedding” will matter even more shortly: separate placements for shape, root and mass may give incompatible small errors. We have not yet incorporated all the structure of measured spaces.

## 55.6 Finite nets and completeness give random geometry a state space

<a id="geometry-polish"></a>

For compact X choose a finite ε-net and retain pairwise distances. Its Hausdorff distance to X is at most ε. Rounding each distance upwards to a small rational mesh preserves triangle inequalities. These finite rational models form a countable dense family. Separability comes from finite approximation, not visual simplicity in a drawing.

The key to completeness is also worth seeing. Take a subsequence with summable successive errors and glue its witnessing spaces along shared objects. All spaces then live in one complete background. The tail stays close to a fixed compact space, so their union is totally bounded. Its closure is compact; the Hausdorff-Cauchy sets have a nonempty compact limit and roots converge at the same time. Details are in [T-GH](../foundations/t-gh.md#gh-complete). Compact and rooted compact isometry classes are therefore Polish spaces, on which probability laws and weak convergence make sense.

\[ \mathcal A\text{ is relatively compact in }rGH
\ \Longleftrightarrow\
\begin{cases}
\sup_{\mathsf X\in\mathcal A}\operatorname{diam}X<\infty,\\
\sup_{\mathsf X\in\mathcal A}N_X(r)<\infty\quad\text{for each }r>0 .
\end{cases} \]

Here N is the number of open balls needed to cover the whole space. Sufficiency follows by finite quantization of nets at every scale; necessity by transferring nets from nearby limits. A diameter bound alone is insufficient: an n-point equilateral space of distance1 needs n small-radius balls and is not GH-precompact.

## 55.7 Comparing mass allows a small exceptional portion

<a id="geometry-prokhorov"></a>

On a common Polish space Z, most probability mass may be close while a small amount lies far away. Requiring every bit of mass to move only a short distance is too restrictive; ignoring exceptional mass entirely loses probabilistic control. Prokhorov distance limits both transport distance and the amount allowed to fail. It is first defined by set inequalities:

\[ \begin{aligned}
d_P(\mu,\nu)=\inf\{\varepsilon>0:\,
&\mu(A)\le\nu(A^\varepsilon)+\varepsilon,\\
&\nu(A)\le\mu(A^\varepsilon)+\varepsilon\
\text{for all Borel }A\}.
\end{aligned} \]

The ε-neighborhood uses strict distance less than ε. This metric characterizes weak convergence, not total variation: moving an atom slightly can make dP small even when the two atomic measures are mutually singular. We need an exact metric compatible with sampling and common embeddings, not an informal relaxation of accuracy.

## 55.8 Finding a coupling from set inequalities

<a id="geometry-strassen"></a>

\[ d_P(\mu,\nu)\le\varepsilon
\quad\Longleftrightarrow\quad
\exists q\in\operatorname{Cpl}(\mu,\nu):
q\{d(x,y)>\varepsilon\}\le\varepsilon. \]

From right to left, mass in A can only move into a slightly enlarged neighborhood except on bad pairs; then remove the slack. The reverse is substantive. Partition high-mass compact sets into finitely many small cells and connect cells at allowed distances. The set inequality says that mass in any group of row cells is at most its reachable column mass plus ε. Why is this enough? If a maximum transport leaves too much unmatched, follow allowed edges forwards and existing positive flows backwards from unsaturated rows. The reachable columns are saturated with no external inflow. The unmatched amount is exactly the excess of reachable row mass over its neighboring column mass, contradicting the condition.

Spread cell masses by conditional products and let cell diameters and tail masses vanish. Fixed marginals make the couplings uniformly tight; closed distance events preserve the inequalities in a weak limit. [T-PROKHOROV-COUPLING](../foundations/t-prokhorov-coupling.md#prok-strassen) gives the full weighted matching, limiting and exact-threshold argument, and proves the weak-convergence characterization and completeness of dP. Coupling existence was not smuggled into the definition.

## 55.9 GP compares what mass can see

<a id="geometry-gp"></a>

\[ d_{rGP}(\mathsf X,\mathsf Y)
=\inf_{Z,\phi,\psi}
\max\{d_Z(\phi\rho_X,\psi\rho_Y),
d_P^Z(\phi_*\mu,\psi_*\nu)\}. \]

GP does not require the whole-space Hausdorff distance to be small. It is consequently a genuine metric only after identifying rooted measured spaces by isometry on the measure support together with the root. An entirely massless extra branch is invisible to GP. Its natural complete state space Mʳ permits complete separable, noncompact supports, rather than compact trees alone.

The opening example gives GP≤ε in the same interval background: with probability1−ε couple the same original position, allowing the residual mass to fail. Yet the diameter difference is2, so every correspondence has distortion at least2 and GH≥1. This distinguishes negligible sampling mass from negligible geometry. Requiring full support for each measure does not remove the example: the added branch has positive but vanishing mass.

## 55.10 What finite sampling can reconstruct

<a id="geometry-sampling"></a>

Take iid mass samples ξ₁,…,ξₖ conditional on the space and let ξ₀ be its root. A GP coupling of error ε makes all coordinate pairs good with probability at least1−kε, giving distance errors at most2ε. GP convergence therefore implies convergence of every finite distance-array law. Conversely these laws identify the support plus root: disintegrate two sample sequences over a common infinite array. Samples are almost surely dense in their supports, so the distance-preserving matching extends by completeness, and the empirical strong law makes it measure-preserving.

\[ D_k(\mathsf X)=
\mathcal L\big((d(\xi_i,\xi_j))_{0\le i,j\le k}\big). \]

For a deterministic sequence, convergence of all Dₖ to readings of an actual object of Mʳ implies GP convergence. Tightness is needed in addition to identification. In the target, k random small balls miss one further sample with probability tending to zero. Array convergence transfers this to approximating spaces, so a uniformly bounded number of small balls covers most mass. Root-distance readings control mass escaping far away. GP relative compactness follows, and reconstruction identifies every subsequential limit. [T-GP-GHP](../foundations/t-gp-ghp.md#mm-sampling-converse) gives the converse argument.

## 55.11 Consistent sampled limits may lack a separable realization

<a id="geometry-sampling-boundary"></a>

Consider n equilateral points at pairwise distance1, with uniform mass and one distinguished root. For fixed k the probability of repeated samples or sampling the root tends to zero. The limiting array has distance1 between every distinct label. These finite arrays are consistent, but cannot be iid distances from a separable metric probability space.

The obstruction is not drawing size. In a separable probability space almost every sample lies in the support, where every positive-radius ball has positive mass. Hence ∫μ(B(x,1/2))μ(dx)>0, so two samples have positive probability of distance below1/2, contradicting that array. Here N balls of radius below1/2 cover at most N/n mass, precisely violating GP tightness. Consistency of finite readings and existence of the desired target space are different requirements.

## 55.12 Why GHP needs three controls in one placement

<a id="geometry-ghp"></a>

\[ \begin{aligned}
d_{rGHP}(\mathsf X,\mathsf Y)=
\inf_{Z,\phi,\psi}\max\{&
d_H^Z(\phi X,\psi Y),\\
&d_Z(\phi\rho_X,\psi\rho_Y),
d_P^Z(\phi_*\mu,\psi_*\nu)\}.
\end{aligned} \]

Use Kʳ, the whole-space isometry classes of nonempty rooted compact metric spaces with Borel probability measures, allowing non-full support. GHP preserves geometry, root and mass simultaneously. It controls rGH and the support-reduced rGP, but generally is not the maximum of these two separately optimized distances.

For an exact example use the same interval [−1,2], rooted at0, with masses δ₁ and δ₋₁. Geometry agrees, so rGH=0. Each support plus root consists of two points at distance1, so rGP=0. But the only whole-interval isometry preserving0 is the identity; it cannot map the interior point1 to the endpoint−1. Hence rGHP>0. A matching chosen for mass need not respect the whole geometry. The simultaneous requirement is substantive.

## 55.13 The correspondence and mass coupling must agree

<a id="geometry-joint"></a>

We can now package all three controls into a usable criterion. If a closed rooted correspondence R has distortion at most2r and a mass coupling q puts at least1−r mass on R, then rGHP≤r. Bridges of length r plus arbitrary slack bring every paired point close, controlling Hausdorff, roots and the coupling in one metric. Conversely a common embedding of error below r yields the near-pair correspondence and a Strassen coupling satisfying those conditions.

\[ R\ \text{closed},\quad\operatorname{dis}R\le2r,\quad
(\rho_X,\rho_Y)\in R,\quad
q(R)\ge1-r
\quad\Longrightarrow\quad d_{rGHP}(\mathsf X,\mathsf Y)\le r. \]

This does not require every point to be sampled by the coupling. R covers the whole space, while q controls probability mass. A zero-mass branch must still find geometric partners in R. For coded trees we will put all coupled mass on the correspondence, a stronger property than the general criterion requires.

## 55.14 Tightness belongs to a specified state-space category

<a id="geometry-random"></a>

Kʳ is complete and separable under GHP. Relative compactness is equivalent to uniform bounds on diameters and whole-space covering numbers at each scale. The proof puts a geometric Cauchy subsequence in one compact background, then takes root and probability-measure limits. Non-full support must be allowed: on a fixed interval the measures (1−1/n)δ₀+(1/n)Leb all have full support, yet the GHP limit retains the entire interval while only its root has mass.

Mʳ is complete and separable under GP. Relative compactness requires uniform tightness of root-distance distributions and a uniformly finite number of balls at each scale covering all but arbitrarily small mass. Zero-mass regions need not be covered. The subclass of compact GP objects is not complete in this metric: put masses1/2,1/4,1/8,… on a countable equilateral space. Its finite truncations, with tail mass moved to the root, converge in GP to that noncompact support.

Measurability of random spaces also requires proof. GHP Borel sets are generated by distance balls centered at countably many finite rational models; GP Borel sets are also generated by finite sampling readings. The latter uses almost sure GP approximation by empirical finite spaces and cannot identify massless GHP branches. Full completeness, tightness and Borel proofs appear in [T-GP-GHP](../foundations/t-gp-ghp.md#mm-polish). Only after this work can Chapter 24’s weak-convergence tools be applied.

## 55.15 Back to excursions: the same time need not be the same tree point

<a id="geometry-code"></a>

Chapter 54 showed that different excursion times may represent the same ancestral point. Given two continuous nonnegative closed codes h,g, their zero-distance classes need not coincide, so one cannot simply send a quotient point to “the same equivalence class.” A relation remains available: pair the two tree points produced by the same parameter time.

\[ R_{h,g}=\{(p_h(t),p_g(t)):0\le t\le1\}. \]

This explains again why correspondence, rather than a map, is needed. Continuous surjective projections make R a compact rooted correspondence. Distance error is now computable directly, rather than guessed from tree drawings.

## 55.16 Four times the distance error, twice the GHP error

<a id="geometry-code-bound"></a>

\[ \begin{aligned}
|m_h(s,t)-m_g(s,t)|&\le\|h-g\|_\infty,\\
|d_h(s,t)-d_g(s,t)|
&\le4\|h-g\|_\infty .
\end{aligned} \]

The two endpoint heights contribute one error each, and the coefficient2 on the interval minimum contributes two more. The root pair is already in R. Couple the masses with the same uniform U: \(p_h(U)\),\(p_g(U)\) have exactly the excursion-time pushforward marginals, and all coupled mass lies on R. The joint criterion gives the actual stability theorem:

\[ d_{rGHP}(\Phi(h),\Phi(g))
\le2\|h-g\|_\infty,\qquad
\Phi(h)=(T_h,d_h,\rho_h,(p_h)_*\mathrm{Leb}). \]

The coding map into rooted metric-measure trees is Lipschitz and measurable. This is the continuity required to transport a functional limit into a spatial limit. Without its proof, saying “by the continuous mapping theorem” establishes no continuity of any map. [T-TREE-GHP](../foundations/t-tree-ghp.md#treeghp-stability) records the constants and convention.

## 55.17 Does the contour encode vertices or whole edges?

<a id="geometry-edge"></a>

A finite tree’s contour is a continuous polygonal curve and visits more than vertices. Fill every edge with an interval; the contour maps continuously onto this edge-filled tree. The minimum height between two visits equals the height of their most recent common ancestor. The visit segment must pass that ancestor, while the subtree above each strict lower ancestor is visited in one uninterrupted depth-first block and cannot be left between the visits. This argument includes edge-interior points.

\[ d(q(s),q(t))
=C(s)+C(t)-2\inf_{u\in[s,t]}C(u),\qquad s\le t. \]

The quotient is therefore rooted-isometric to the edge-filled tree, not merely distance-correct at integer times. If edges have length a, the Hausdorff distance from the vertex subspace to the filled tree is at most a/2 and roots agree. This error disappears under scaling, but the two spaces are not literally equal for a finite tree.

## 55.18 Two kinds of uniformity differ on a finite tree

<a id="geometry-vertex-mass"></a>

Uniform contour time traverses every edge twice at constant speed and pushes forward to normalized edge length. Uniform vertex mass lives on finitely many points. For n≥2 the two measures are mutually singular, with total variation distance1. Calling both “uniform” does not permit substitution. We need a coupling close in tree distance, not equality on every measurable set.

\[ b_j=2j-H_j,\qquad
t_j=\frac{b_j}{2(n-1)},\qquad
J=\lfloor nU\rfloor,\quad U\sim\mathrm{Unif}[0,1]. \]

Number preorder vertices vⱼ and let Hⱼ be edge-count height. Before the first contour visit to vⱼ there have been j downward visits to new vertices and j−Hⱼ returns, giving the formula. J is exactly uniform on vertex labels, while q(U) has uniform contour-time mass. Vertex vⱼ is the contour position at relative time tⱼ.

\[ \begin{aligned}
|U-t_J|&\le\eta_n,\qquad
\eta_n=\frac1n+\max_{j<n}|t_j-j/n|\\
&\le\frac1n+\frac1{n-1}
+\frac{H_{\max}}{2(n-1)} .
\end{aligned} \]

For the scaled unit-time contour h, two visits in a short interval are at tree distance at most twice its height oscillation. The same-U pairing therefore bounds the Prokhorov distance between vertex and contour masses by2ω(h,ηₙ). This converts clock discrepancy into spatial discrepancy and shows exactly why common oscillation control is needed.

## 55.19 What the conditioned functional theorem contributes

<a id="geometry-input"></a>

Take a critical nondegenerate offspring law with Eξ=1 and Varξ=σ²∈(0,∞), along sizes with P(|T|=n)>0. Chapter 53’s conditioned bridge, cut, ancestral-height and joint contour estimates give

\[ \begin{aligned}
a_n&=\frac{\sigma}{2\sqrt n},\\
h_n(t)&=a_n C^{(n)}(2(n-1)t)\Rightarrow e(t)
\quad\text{in }C([0,1]),\\
H_{\max}/\sqrt n&=O_P(1).
\end{aligned} \]

The input is the conditioned-tree functional theorem, not unconditioned Donsker applied directly to a rare size event. Maximal lattice span and admissible sizes remain as in Chapter 53; impossible conditions are excluded. The working proof is in [T-CONDITIONED-HEIGHT](../foundations/t-conditioned-height.md#height53-joint).

The height bound makes ηₙ tend to zero in probability. Crucially, tightness of hₙ in continuous-function space makes ω(hₙ,ηₙ) tend to zero in probability. First control oscillation at deterministic δ, exclude ηₙ>δ, and only then let δ decrease. This is not an unproved pathwise assertion.

\[ \lim_{\delta\downarrow0}\limsup_n
P(\omega(h_n,\delta)>\varepsilon)=0,\qquad
P(\omega(h_n,\eta_n)>\varepsilon)
\le P(\eta_n>\delta)+P(\omega(h_n,\delta)>\varepsilon). \]

## 55.20 Conditioned GW trees finally converge as spaces

<a id="geometry-crt-limit"></a>

\[ \boxed{\left(T_n,\frac{\sigma}{2\sqrt n}d_{T_n},
\rho_n,\mu_n\right)
\Rightarrow(\mathcal T_e,d_e,\rho_e,\mu_e)
\quad\text{in }(K^r,d_{rGHP}),\qquad
\mu_n=\frac1n\sum_{v\in T_n}\delta_v.} \]

The proof now forms a substantive chain. The2-Lipschitz stability of Φ takes hₙ⇒e to Φ(hₙ)⇒Φ(e). Place the original vertex tree and Φ(hₙ) in the same edge-filled tree. Hausdorff error is at most aₙ/2, root error is zero and mass error is at most2ω(hₙ,ηₙ). Thus

\[ d_{rGHP}\big((T_n,a_nd_{T_n},\rho_n,\mu_n),\Phi(h_n)\big)
\le\max\{a_n/2,2\omega(h_n,\eta_n)\}
\xrightarrow{P}0. \]

Bounded Lipschitz tests show that random elements at distance tending to zero in probability have asymptotically equal expected readings, proving the boxed theorem; see [T-TREE-GHP](../foundations/t-tree-ghp.md#treeghp-limit). The factor σ/(2√n) gives Chapter 54’s Tₑ, not T₂ₑ. Contour duration2(n−1) and vertex count n retain their distinct roles; no “asymptotically the same” substitutes for constructing the mass coupling. One witness simultaneously controls root, all distances and the original vertex measure.

## 55.21 What the spatial limit actually preserves

<a id="geometry-limit-meaning"></a>

Chapter 52’s coding was an exact relation between finite objects. Chapter 53’s limit lived in function space. Chapter 54 turned each continuous code into a genuine real tree. This chapter does not rename the same conclusion. It proves compatibility in rooted GHP: point names disappear, while distances, root and mass survive together with verifiable errors.

The limit retains neither a sampled vertex’s original label nor each individual edge; scaled edges become short. But it controls the whole tree, not merely finitely sampled points, so a fixed extra long branch cannot be hidden. A sampling-distance proof alone would still permit the opening counterexample.

## 55.22 Universality not proved here

<a id="geometry-boundary"></a>

Finite variance and criticality do not disappear when we switch to geometric language. Changing offspring tails, conditioning or allowing a few long edges to introduce a new scale requires new functional control and mass comparisons. General stable trees, noncompact local GHP and dynamic fragmentation-coalescence are not established here; arbitrary models outside the coding construction still need their own tightness estimates. They do not follow by replacing σ with another constant.

Other boundaries matter too. Consistent sampling laws need not already have a Polish geometric realization. A GHP limit of full-support compact objects need not retain full support. A GP-Cauchy sequence of compact-support objects may leave that subclass. Choosing the right state space is part of the limit theorem itself.

## 55.23 Sources and the proof responsibilities of this chapter

<a id="geometry-sources"></a>

For modern measured-space topology, the [original paper](https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/greven.pdf) of Greven, Pfaffelhuber and Winter appeared in 2009 and studies sampling topology and GP on complete separable metric probability spaces. The [original paper](https://cermics.enpc.fr/~delmas/Publi/GHP.pdf) of Abraham, Delmas and Hoscheit appeared in 2013 and treats compact and suitable locally compact rooted measured spaces. Here we use a maximum of errors on compact probability objects; some literature uses their sum. The topologies agree, but constants cannot be transferred unchanged.

The discovery order and bridge, weighted-matching, empirical-sampling and vertex-clock arguments here are a modern mathematical reconstruction, not a claim about those authors’ historical thought processes. Four bilingual companions contain actual proofs of deterministic GH, Prokhorov coupling, GP/GHP state spaces and the tree-space limit. The proof dependencies retain their stated hypotheses throughout.

## 55.24 Closeness becomes a provable relation

<a id="geometry-ending"></a>

“Two random trees look similar” no longer depends on overlapping drawings. We can exhibit the pairing relation, bound its distance distortion, specify a mass coupling and check whether the root is preserved in the same comparison. The long-branch example shows what sampling cannot replace; coding stability turns curve error into an error for the whole geometry and its mass.

This completes the present passage from a discrete family to a continuous tree. It is not that a picture becomes smoother: finite-variance microscopic reproduction, under precise conditions and scaling, produces a common rooted metric-measure limit. Cutting this tree or allowing branches to grow or merge requires new random rules acting on geometric objects. Existence of a static space does not itself specify how it evolves.
