# T-ARRAY-VARIANTS: Directions, Diagonals and the Complete Separate-Exchangeability Construction

Let E be nonempty standard Borel. [T-ARRAYS](t-arrays.md) establishes joint exchangeability. Here we explicitly handle directions and diagonals, separately exchangeable matrices and finite multitype higher-order extensions. Return to [Chapter46](../chapters/46-arrays.md#arrays-separate-proof).

## 1. Two group actions and two kinds of pair noise

<a id="array-variants-groups"></a>

\[ (X_{ij})\stackrel d=(X_{\pi(i)\pi(j)})\quad\text{joint};\qquad (X_{ij})\stackrel d=(X_{\pi(i)\sigma(j)})\quad\text{separate}. \]

The maps π,σ range over all finite permutations of N. Separate exchangeability implies joint exchangeability, not conversely: an identity matrix is invariant under simultaneous relabeling but changes when two rows alone are swapped. Rows and columns represent different object populations; an entry (i,i) does not mean a shared vertex. Joint exchangeability allows extra dependence between Xij and Xji, two directions of the same object pair.

The marked ordered decoding in T-ARRAYS gives Borel F,D and independent uniform inputs with the following jointly exchangeable law. Each unordered pair has one W; the reverse edge must not receive a fresh independent number. The function D may also output extra standard Borel vertex marks.

\[ X_{ij}=F(U_0,U_i,U_j,W_{\{i,j\}})\quad(i\ne j),\qquad X_{ii}=D(U_0,U_i). \]

The function F need not be symmetric in the vertex inputs; it can be chosen symmetric when the original array is symmetric. For general directed arrays T-ARRAYS stores both directions in a single pair label and decodes their order using continuous vertex marks. It therefore constructs the joint directional law with shared W, rather than matching marginal edge laws separately.

## 2. Giving two populations one common label space

<a id="array-variants-color"></a>

Now suppose X is separately exchangeable. Independently take iid colors Cₐ∈{0,1} with equal probabilities; each occurs infinitely often almost surely, for example by the independent strong law. Let r(a) be a type-zero vertex’s rank in the natural enumeration, and c(a) the corresponding rank for type one. Define a directed relation H on the common label space: use \(X_{r(a),c(b)}\) only when Cₐ=0,\(C_b\)=1, and a new symbol † otherwise, retaining the vertex colors.

The disjoint union of E and {†} is standard Borel. Conditional on the entire color sequence, any finite vertex permutation induces finite separate permutations of the row and column ranks, so the corresponding joint law is unchanged. Since colors are iid, (H,C) is jointly exchangeable. T-ARRAYS supplies independent uniforms U₀,Tₐ,\(W_{\{a,b\}}\) and Borel h,d with Hₐb=h(U₀,Tₐ,\(T_b\),\(W_{\{a,b\}}\)) and Cₐ=d(U₀,Tₐ). Only a≠b relations will be extracted; diagonals are †.

Conditional on U₀=z, colors are iid with success probability p(z)=∫1{d(z,t)=0}dt. Their conditional strong law gives limiting type-zero frequency p(z), whereas the original construction has frequency one half. Equality of laws forces p(z)=1/2 almost surely. Extracting by type therefore does not inadvertently reweight the global environment; its conditional parameter has actually been checked.

## 3. Which random sources remain independent after extracting colors

<a id="array-variants-thinning"></a>

\[ Q_z^c(dt)=\frac{\mathbf1_{\{d(z,t)=c\}}\,dt}{p_c(z)},\qquad p_c(z)=\int_0^1\mathbf1_{\{d(z,t)=c\}}dt\quad(c=0,1). \]

Use a fixed probability where \(p_c\)=0. These are Borel kernels at every z, with both denominators one half at good z. Chapter10 randomization gives \(a_c(z,u)\) with law \(Q_z^c\). We now prove the two extracted families of T are not merely individually iid but conditionally independent of one another.

For fixed good z, generate the T sequence in reverse: first iid types with probabilities \(p_c(z)\), independently generate an iid \(Q_z^c\) sequence for each type, then interleave them in type order. For any finite type word and T tests, the probability is the product of \(p_c(z)Q_z^c(dt)\) over positions. Summing over types yields iid Lebesgue T. This finite product-kernel identity and countable product uniqueness prove equality with the original T sequence. Extracting types recovers the two independently generated families, proving their conditional independence.

Pair variables W are independent of all T and U₀, while type extraction depends only on those vertex data. Conditional on the types and vertex data, finitely many distinct pairs consisting of the ith type-zero and jth type-one vertex correspond to distinct unordered vertex pairs. Their W remain independent uniforms, independent of the extracted T. This follows from finite conditional product probabilities and does not permit selections depending on edge values.

## 4. Completing the separate representation at every matrix position

<a id="array-variants-separate"></a>

\[ F(z,u,v,w)=h(z,a_0(z,u),a_1(z,v),w),\qquad (X_{ij})\stackrel d=(F(U_0,U_i,V_j,W_{ij})). \]

Replace † outputs of F by fixed x₀∈E. Cross-type relations originally take E-values at good parameters, so the change concerns a total-product null set and all countably many cells can be repaired together. The variables U₀, all Uᵢ,Vⱼ,Wᵢⱼ are mutually independent uniforms. Extracting by type in the original H construction recovers original X; the preceding section proves that extracting in its representation yields exactly the conditional-independent latent law in this formula. Thus all joint laws of any original X are recovered, not merely the easy implication that the formula produces exchangeability.

The converse follows directly because finite row and column permutations preserve the independent input law. Here Wᵢⱼ and Wⱼᵢ are independent, since row i and column j belong to different populations; i=j is an ordinary cross-population cell. This differs from the shared unordered-pair noise and genuine diagonal D in the jointly exchangeable formula.

## 5. Finite multitype higher-order separate exchangeability and shared subsets

<a id="array-variants-higher"></a>

Fix d populations, each indexed by N, and a d-ary relation invariant under independent permutations within populations. Give common vertices iid types1,…,d with probabilities \(p_c\)>0. Store the original relation at the corresponding occurrence ranks only when the cth vertex of an ordered d-tuple has type c, and use † otherwise. Retain type as a singleton mark. Conditional on types, a finite common relabeling induces finite relabelings in each population, giving a jointly exchangeable marked ordered relation. The finite-order ordered result of T-ARRAYS applies.

In this representation types depend only on U₀ and singleton noise. Comparing original type-frequency strong laws with conditional strong laws in the representation gives \(p_c(U_0)\)=\(p_c\) almost surely for every type. The finite-product interleaving proof yields d conditionally independent singleton pools with laws \(Q_z^c\). Every noise attached to a subset of size at least two is independent of the type selections. Distinct typed partial-index sets correspond to distinct unordered vertex subsets, so their extracted noises are still a mutually independent uniform family.

\[ X_{i_1,\ldots,i_d}=F\left(U_\varnothing,\big(U^A_{(i_c)_{c\in A}}\big)_{\varnothing\ne A\subseteq[d]}\right). \]

Randomize singleton inputs through the measurable Q kernels and leave all other subset inputs uniform to obtain Borel F. For a finite family of tuples, extraction preserves equality and inequality of every partial-index set: a noise is shared exactly when the corresponding population subset is shared. Finite product verification followed by cylinder uniqueness gives the whole law; conversely population-wise permutations preserve all independent subset-input laws. This proves separate representation for every fixed finite d, not infinitely many types or nonstandard Borel extensions.

## 6. Permutation symmetry is not orthogonal rotation of an array

<a id="array-variants-rotations"></a>

These theorems concern relabeling, not arbitrary linear combinations. An iid Rademacher matrix is separately exchangeable but a two-row orthogonal mixture produces zero and ±√2, so it is not separately rotatable. Conversely Xᵢⱼ=ZᵢVⱼ, with independent iid standard normal sequences Z,V, is invariant under finite row and column orthogonal transformations, which separately preserve the independent normal laws of Z and V.

This matrix has single-cell second moment one and fourth moment nine, so it is not an independent standard Gaussian matrix; every2×2 determinant is also zero. If all cells are additionally assumed iid, Chapter45 two-coordinate rotational characteristic-function equation forces a common centered Gaussian cell law. This does not prove the general classification of separately rotatable arrays, which remains an open proof responsibility here; permutation representation is not that classification.
