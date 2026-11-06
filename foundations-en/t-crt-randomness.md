# T-CRT-RANDOMNESS: Mass, Randomness and Finite Distance Readings

This companion completes the treatment of pushforward mass, measurable random real trees and Brownian mass properties in [Chapter 54](../chapters/54-brownian-crt.md#crt-mass). The deterministic real-tree theorem is proved in [T-REAL-TREE-CODE](t-real-tree-code.md), and finite sampling densities are calculated in [T-CRT-SAMPLING](t-crt-sampling.md). No GH, GP or GHP topology from Chapter 55 is assumed.

## 1. Pushforward mass and full support

<a id="crt-random-mass"></a>

\[ \mu_h=(p_h)_*\operatorname{Leb}_{[0,1]},\qquad
\int_{T_h}f(x)\,\mu_h(dx)=\int_0^1 f(p_h(t))\,dt. \]

Since pₕ is continuous, this is a Borel probability on the quotient; finite Borel measures on compact metric spaces are Radon by the regularity proved in Chapter 49. A nonempty open O has nonempty relatively open inverse image in [0,1], hence positive Lebesgue mass, so μₕ has full support. This does not imply diffuseness: a triangular code that pauses for positive time at its tip gives that point an atom.

Given h, the images of independent uniform times Uᵢ are iid μₕ samples. Mass is traversal time pushed forward, not an automatic assignment of uniform length to each edge. Uniform-speed ascent and descent of a segment, or ascent and descent with a pause, can code the same rooted metric segment with different mass. Metric and mass must both be retained.

## 2. Measurability without borrowing a spatial topology

<a id="crt-random-measurable"></a>

Let E₀ be the continuous nonnegative codes vanishing at both endpoints, equipped with the Borel field of the uniform norm. Interval minima are 1-Lipschitz in that norm, so distance readings for two codes differ by at most four times their uniform error, simultaneously in s,t.

\[ \sup_{s,t}|d_h(s,t)-d_g(s,t)|\le4\|h-g\|_\infty,\qquad
\Phi_{k,F}(T_h,\rho_h,\mu_h)
=\int_{[0,1]^k}F\!\left((h(t_i))_i,(d_h(t_i,t_j))_{i<j}\right)\,dt_1\cdots dt_k. \]

Here F is bounded continuous on finitely many coordinates. If hₙ converges uniformly to h, all coordinates converge and remain in one bounded range, so bounded convergence makes Φ continuous. Take root-preserving measure-preserving isometry classes of compact rooted full-support measured real trees, and generate a sigma field by these sampling readings. Then h↦(Tₕ,ρₕ,μₕ) is measurable. The C([0,1])-valued random excursion e therefore gives a genuine random rooted measured real tree by the samplewise quotient construction. This asserts measurability in that sigma field, not completeness or separability of a spatial metric not yet established.

Conditional sampling and common null sets can also be handled with a fixed countable record. For each h, use images pₕ(q) of rational times as dense centers and positive rational radii for a ball base. Their masses integrate over t the indicator of \(d_h(q,t)<r\). Distances are continuous in (h,q,t), so these masses and finite-sample hitting events are jointly measurable. One common good event for this fixed countable indexed family legitimizes the density and leaf arguments below when h is random.

## 3. Finite sampling readings identify the measured tree

<a id="crt-random-identification"></a>

We must prove that these observations do not identify distinct full-support trees. More generally, let two compact rooted metric probability spaces have full support and identical root-and-iid-sample distance laws for every k. Countable product uniqueness makes their infinite array laws identical. Disintegrate each infinite iid sample sequence over its distance array in its own fixed compact Polish space. Chapter 10 then couples the two sequences conditionally on one common array, making all distances equal coordinate by coordinate. Explicitly, for every array coordinate and rational threshold, the conditional indicator mean is the corresponding zero-or-one reading of the conditioning array. A common null set for these countably many tests makes each conditional kernel concentrate on sample sequences realizing that array.

Each iid sequence is almost surely dense: for every nonempty set in a countable base, the probability of never hitting it is lim(1−μO)ⁿ=0. Remove their countable union of null sets. Equal distance arrays give a root-preserving isometry of the two dense sampled sets. Repeated points coincide on both sides by zero distance, so the map is well-defined. Completeness extends it uniquely to a surjective rooted isometry.

The isometry also preserves mass. Continuous functions on a compact metric space have a countable uniformly dense family. An explicit construction first approximates continuous f uniformly by \(f_L(x)=\inf_y\{f(y)+Ld(x,y)\}\): uniform continuity controls nearby errors, and boundedness excludes lower values from distant points as L increases. These functions are L-Lipschitz. Finite nets from a countable dense set, rational heights and rational slopes then give uniform approximations by minima of finitely many functions of the form rational height plus rational slope times distance. This is a countable family. Apply the strong law of Chapter 12 to that family and extend by uniform approximation: empirical measures converge weakly to μ almost surely. The extended isometry pushes each empirical measure to its counterpart, so continuous tests show it pushes their limiting measures too. The spaces are root-preserving measure-preserving isometric. This uses ordinary weak convergence on fixed compact spaces, not a reconstruction theorem for GP spaces from Chapter 55.

For random trees, unconditional sampling laws must also recover the joint laws of the readings themselves. The product of two readings is one larger reading using the product test on two disjoint iid sample groups; the same holds for any finite product. All finite distance-array laws therefore give every mixed moment of any finite vector of readings. The readings are bounded, so polynomial approximation on a compact box, using the product Bernstein proof of Chapter 13, identifies their joint distribution. Cylinder-set uniqueness then identifies the random-tree law on the sigma field generated by readings, not just their separate means.

## 4. Diffuse mass concentrated on leaves

<a id="crt-random-leaves"></a>

Now h=e. The finite reduced-subtree theorem gives strictly positive distance between two independent mass samples almost surely. The expected conditional collision probability ∫μₑ({x})μₑ(dx) is therefore zero. Nonnegativity makes it zero almost surely, excluding every atom, including the root. This follows from the sampling density, not merely from e having a density at each fixed time.

A nonroot x is a leaf when it has no strict descendant, equivalently its removal leaves one connected component. The leaf set is measurable: for a fixed countable dense D, x is a nonleaf exactly when some z∈D satisfies |z|=|x|+d(x,z) and d(x,z)>0. A strict descendant direction contains a nonempty open set and hence meets D, proving one implication; ancestral lines prove the other. The conditions are countably Borel.

Take one conditionally iid mass-sample sequence. Almost surely every sampled point is a leaf of every finite Rₖ containing it, by the strictly positive edge-length density; countably many k permit a common event. If the first sample were a nonleaf of the whole tree, a strict-descendant direction would be nonempty open and have positive mass by full support. A later sample would almost surely enter it. The first sample would then lie inside a root-to-sample path and be a nonleaf of some Rₖ, a contradiction. Conditional integration gives μₑ(leaves)=1.

## 5. Binary branching, length and mass

<a id="crt-random-branches"></a>

The same samples are almost surely dense and all finite reduced trees are binary. Components of a real tree with one point removed are open: a sufficiently small ball about any other point remains in its component. If any point of the whole tree had at least four components, choose dense samples in four of them. Some finite Rₖ would then have degree at least four, a contradiction. Hence every branch point has degree exactly three. The root has degree one: e is strictly positive on (0,1), so the interval between representatives of any two nonroot points has positive minimum, and their connecting segment avoids the root.

This does not take a separate null set for uncountably many points. One common good event for a dense sequence and its finite spans excludes all higher-degree branch points at once. Every degree-three branch point is recovered by connecting three dense samples, so branch points are at most countable. The entire tree is not thereby countable.

The interior of any nondegenerate tree arc consists of nonleaves, and its endpoints have no atoms. Thus each arc has μₑ-mass zero despite positive metric length. Each finite Rₖ also has mass zero, although their union is dense because it contains all the samples. Total length tends to infinity almost surely by the independent exponential increments of 2Lₖ² in the sampling kernel and the strong law. Finite-edge length and whole-tree probability mass are genuinely different. Uniform time sampling has not been mistaken for normalizing an infinite skeleton length.

## 6. Rerooted readings and spatial limits not claimed here

<a id="crt-random-root"></a>

The finite sampling density depends only on the sum of edge lengths and, viewing the root as the extra leaf label 0, is symmetric in labels 0,…,k. Swapping the root with a uniform sample preserves the finite distance-array law. To compare k fresh samples after rerooting, first take k+1 old samples, interchange labels 0 and 1 in the array with k+2 labels, and discard label 1. Thus the CRT rerooted at a uniform mass point has the same sampling-reading law as the original CRT. This does not assume the original root was μ-sampled; it follows from label symmetry.

All these assertions concern actual construction and identification: a compact real tree, root, mass, finite sampling and a random law. They do not establish GH/GP/GHP metrics, Polishness of spaces of trees or spatial convergence of conditioned GW trees; these belong to Chapter 55. Complete infinite line-breaking remains for Chapter 57 and general Lévy trees for Chapter 58. [Return to the mathematical insight in Chapter 54](../chapters/54-brownian-crt.md#crt-insight).
