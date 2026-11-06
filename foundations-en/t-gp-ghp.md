# T-GP-GHP: Identification, Sampling, Polish Spaces and Tightness

This page proves the metric-measure structure in [Chapter 55](../chapters/55-metric-measure-limits.md#geometry-ghp). Prerequisites are this chapter’s T-GH and T-PROKHOROV-COUPLING and the countable constructions, conditional kernels, strong law and weak-convergence tools of Chapters 8,10,12,24. No later tree limit is used to prove completeness.

## 1. Two equivalence conventions and three simultaneous comparisons

<a id="mm-categories"></a>

Let Kʳ denote rooted nonempty compact metric probability spaces modulo root-preserving, measure-preserving isometry of the whole space; measures need not have full support. Let Mʳ identify complete separable metric probability spaces by rooted measure-preserving isometry on the support together with the root. Use suppμ∪{ρ} as representative; the root may lie outside the support. These conventions must not be interchanged. These classes form sets: every complete separable rooted space is determined up to isometry by the matrix of a countable dense sequence containing its root; a probability is specified by its values on a countable ball basis and its finite unions. Thus countable real records suffice to represent all the classes. Ambient spaces in the definitions may be Polish: the union of the two separable spaces is separable, and its metric completion preserves both embeddings.

\[ \begin{aligned}
d_{rGP}(\mathsf X,\mathsf Y)
&=\inf_{Z,\phi,\psi}\max\{
d_Z(\phi\rho_X,\psi\rho_Y),d_P^Z(\phi_*\mu,\psi_*\nu)\},\\
d_{rGHP}(\mathsf X,\mathsf Y)
&=\inf_{Z,\phi,\psi}\max\{
d_H^Z(\phi X,\psi Y),
d_Z(\phi\rho_X,\psi\rho_Y),
d_P^Z(\phi_*\mu,\psi_*\nu)\}.
\end{aligned} \]

GP is defined on Mʳ and GHP on Kʳ. All three terms in the second maximum use the same embeddings. Removing root terms gives unrooted versions with identical proofs. Triangle inequalities follow by gluing from T-GH and by the ambient Prokhorov triangle inequality. GP is at most1: identify the roots, making root distance zero, while dP≤1. GHP has no such diameter-independent bound.

## 2. Reconstruction from rooted distance arrays

<a id="mm-reconstruct"></a>

In a fixed space take iid samples ξᵢ and set ξ₀=ρ. Record all d(ξᵢ,ξⱼ). If every finite array law agrees for two spaces, the countable infinite array laws agree by cylinder uniqueness from Chapter 8. Disintegrate each Polish sample-sequence space over its array and pair the two sequences conditionally independently over the common array. Their arrays agree coordinate by coordinate. Distances are measurable by continuity; conditional kernels come from Chapter 10. Only countably many coordinates require a common null set.

An iid sequence is almost surely dense in the support: every positive-mass basic open set is eventually hit, and there are only countably many. Matching samples preserves all distances; including the root extends this to an onto isometry of the complete supports plus roots. It preserves measures as well. To check this, choose a countable ball basis with μ-null spheres; all finite unions are continuity sets. The strong law holds simultaneously on this countable family. Every open set is approximated from below by its finite unions, giving the open-set Portmanteau bound for empirical measures and hence weak convergence to μ. Apply the same argument on the other side. The isometry pushes the empirical measures exactly onto one another, so it also pushes their limits onto one another.

## 3. GP nondegeneracy and continuity of sampling

<a id="mm-sampling-forward"></a>

If the ambient root distance and dP are below ε, Strassen couples a sample pair with probability at most ε of distance exceeding ε. For k independent pairs, all matches are good with probability at least1−kε; every root-distance and sample-distance discrepancy is then at most2ε. Thus GP convergence implies weak convergence of every finite array. If GP=0, both arrays have identical laws and reconstruction identifies the classes. GP is therefore a metric on Mʳ but only a pseudometric on classes retaining arbitrary zero-mass geometry.

## 4. GHP nondegeneracy and a joint criterion

<a id="mm-joint"></a>

Zero GHP distance first gives a rooted whole-space isometry f by GH nondegeneracy, but measure preservation still requires proof. In the dense-point diagonal construction of T-GH, use finer finite nets of X and map x to the Y point paired with its nearest net point, breaking ties by the least index. These maps fₙ are Borel and converge uniformly to f along the chosen subsequence. More explicitly, after diagonal convergence of each fixed net, let its fineness increase sufficiently slowly that all its finitely many paired images are within its mesh size of their f-images. For any x the nearest net point is within that mesh, and its image under f is equally close to f(x); hence the maximum error of fₙ tends to zero. In the witnessing ambient space, x is within the net radius plus embedding error of fₙ(x), so their pushforward measures approach ν in dP. Uniform convergence and compactness of Y also imply (fₙ)₊μ⇒f₊μ. Hence f₊μ=ν, completing the mass identification.

\[ \left.
\begin{gathered}
R\subset X\times Y\ \text{closed rooted correspondence},\\
\operatorname{dis}R\le2r,\qquad
q\in\operatorname{Cpl}(\mu,\nu),\quad q(R)\ge1-r
\end{gathered}\right\}
\quad\Longrightarrow\quad d_{rGHP}(\mathsf X,\mathsf Y)\le r . \]

R is closed from the outset, hence Borel in X×Y and q(R) is defined. A given Borel correspondence may be replaced by its closure, preserving surjectivity, not increasing distortion and not decreasing coupled mass. A bridge of length r+η puts every paired point at distance at most r+η and controls Hausdorff and root distances. Bad coupling mass is at most r, so dP≤r+η. Let η decrease to zero. Conversely, for any r>dGHP choose a common embedding with errors below r. All cross-pairs at distance at most r form a closed rooted correspondence of distortion at most2r, and Strassen provides a coupling giving it mass at least1−r. This equivalent criterion, with slack at the infimum, will be used for coded trees.

## 5. Completeness and separability of GHP and GP

<a id="mm-polish"></a>

For a GHP-Cauchy sequence choose a subsequence with summable successive errors and glue realizations in one complete ambient space. T-GH makes the union of geometries have a compact closure K; roots and compact subsets converge there. Measures are dP-Cauchy on K and converge by T-PROKHOROV-COUPLING. Their limit μ is supported by the Hausdorff limit X: the μᵢ integral of min(1,d(·,X)) is at most dH(Xᵢ,X), so the limiting integral vanishes. The limiting root is also in X. All three errors tend to zero, proving completeness of Kʳ.

For GP the same gluing controls no Hausdorff distance, so the common space is complete and separable but need not be compact. Nevertheless roots and measures are Cauchy and converge to ρ and μ. The closed subspace suppμ∪{ρ} gives a limit in Mʳ. Original spaces and this subspace are compared in the same background, so GP is complete. Allowing noncompact supports here is essential.

For separability, take a finite ε-net including the root in a compact object. Project by the least index and couple the pushed mass within distance ε. Round net distances upwards to a rational mesh, then approximate weights rationally. The joint criterion makes the GHP error arbitrarily small. For a general GP object first choose a compact set carrying mass1−ε, take a finite net together with the root, and send residual mass to the root. Bad pairs have mass at most ε and good distances are at most ε. Rationalize as before. Finite rational models are countable. Thus Kʳ under GHP and Mʳ under GP are Polish metric spaces.

## 6. Different compactness criteria for geometry and mass

<a id="mm-tightness"></a>

A family in Kʳ is relatively compact exactly when diameters and, for every r, whole-space covering numbers are uniformly bounded. Necessity follows by the GH projection. For sufficiency take a GH-convergent subsequence and realize a further summable-error subsequence in one compact background using the gluing and total-boundedness proof of T-GH. Extract convergent roots and, by Prokhorov on the compact background, weakly convergent probability measures. The limiting measure is supported by the geometric limit. All three components converge together. Fixing total mass at1 matters here.

\[ \begin{gathered}
\text{A family }\mathcal A\subset M^r\text{ is relatively compact iff}\\
\forall\varepsilon>0\ \exists R<\infty:
\inf_{\mathsf X\in\mathcal A}\mu(B(\rho,R))\ge1-\varepsilon,\\
\forall\varepsilon>0\ \exists N<\infty\
\forall\mathsf X\in\mathcal A\ \exists x_1,\ldots,x_N:
\mu\!\left(\bigcup_{i\le N}B(x_i,\varepsilon)\right)\ge1-\varepsilon.
\end{gathered} \]

For sufficiency of the GP criterion, intersect the high-mass ball cover with a root ball of radius R. Retain intersecting balls and move each center to a point in the intersection, doubling their radius. The centers are within R of the root and at most2ε mass is missed. Send covered points to the first eligible center and residual mass to the root. This produces finite models of bounded size and diameter with GP error at most2ε. Rational quantization leaves finitely many models. The family is totally bounded, hence relatively compact by GP completeness.

For necessity, approximate a relatively compact family by a finite GP net and approximate its centers by finite atomic models. A small GP coupling transports all but η mass from each finite model into finitely many O(η)-balls of the original space. For each model atom participating in a good pair choose one original representative; all other good partners are within2η of it. Root errors are also controlled. Model atoms have bounded distance from their model roots, giving a uniform root ball outside O(η) mass. Maximize constants over the finitely many net centers and choose η sufficiently small.

## 7. The converse sampling-convergence theorem

<a id="mm-sampling-converse"></a>

Theorem: a deterministic sequence in Mʳ converges in GP to a specified object of Mʳ if and only if every finite rooted iid distance array converges weakly to its array law. The forward implication was proved above. For the converse, identification of laws alone is insufficient. First, convergence of the one-sample root-distance reading gives uniform tightness of root-distance distributions. Next examine the probability that k sampled balls in the target miss one further sample:

\[ \kappa_k(r)=
P\!\left(\min_{i\le k}d(\xi_{k+1},\xi_i)>r\right)
=\int(1-\mu(\overline B(x,r)))^k\,\mu(dx)
\longrightarrow0 . \]

For μ-almost every x, every positive-radius ball has positive mass, so dominated convergence applies. Given ε choose r<ε/2 with P(d(ξ₁,ξ₂)=r)=0; only countably many radii are forbidden. Finite-array convergence makes the missed probability for each fixed k converge to κₖ(r). Choose k so its expectation is below ε/4. Eventually Markov bounds the probability of missing more than ε mass by less than1/3. Choose R so the probability any of the k centers lies beyond R from the root is also below1/3. Hence some choice of k bounded-root-distance centers covers mass1−ε. Treat finitely many initial terms individually. The GP compactness criterion follows.

Every GP subsequential limit has the target array law by forward sampling continuity and equals the target by reconstruction. Relative compactness and uniqueness of subsequential limits imply convergence of the full sequence. A genuine Polish metric-measure target is essential; arbitrary consistent finite array limits need not supply one, as the equilateral example in Chapter 55 shows.

## 8. Borel structure, random objects and probabilistic tightness

<a id="mm-measurable"></a>

The GP Borel field is generated by bounded continuous finite-array readings, with a countable determining family sufficient. To prove that metric open sets are not missed, form the finite empirical space Fₖ from k iid samples and the root of a fixed object X. Empirical weak convergence and the dP characterization imply dGP(Fₖ,X)→0 almost surely. On finite distance matrices, matching labels and coupling uniform masses bound space distance by half the maximum entry error; quotienting zero-distance labels causes no difficulty. Thus the matrix-to-empirical-space map is continuous. For each A in a countable dense family of rational finite models,

\[ 1\wedge d_{rGP}(\mathsf X,A)
=\lim_{k\to\infty}E\,[1\wedge d_{rGP}(F_k(\mathsf X),A)]. \]

The right side integrates bounded continuous functions of finite arrays; the left side generates balls centered in that countable family. The reverse inclusion follows by sampling continuity. Measurability of array evaluations therefore constructs GP random elements. To identify random-space laws, products of finite readings are single readings on more independent samples. Moment uniqueness for bounded variables and a countable determining family then identify joint reading laws and the space law. Neither expected distances alone nor one fixed sample size suffices.

For GHP use distance balls centered at countably many rational finite models. The same sampling sigma field cannot replace it, since samples do not identify zero-mass geometry. The tree objects below are constructed by an explicitly proved continuous coding map and hence are measurable directly. In either Polish space a sequence of random-object laws is tight exactly when, for each η>0, there are εⱼ↓0 and finite sets Aⱼ such that the probability of being farther than εⱼ from Aⱼ is uniformly below η2⁻ʲ. Sufficiency follows because the intersection of the closed neighborhoods is closed and totally bounded, hence compact, with the union bound controlling its complement. Necessity follows by taking finite nets of compact sets carrying sufficient probability.

In particular, GHP laws are tight precisely when diameters are uniformly tight in probability and so are whole-space covering numbers for each r>0. For rⱼ↓0 choose bounds with failure probabilities η2⁻ʲ; their intersection is relatively compact by the geometric criterion, and take its closure. Measurability of covering numbers and diameter was proved in T-GH. Independent expert final review remains open; the arguments here are working proofs. Return to [Chapter 55](../chapters/55-metric-measure-limits.md#geometry-random).
