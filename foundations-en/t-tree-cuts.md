# T-TREE-CUTS: Length-Poisson Cutting, Finite-Sample Consistency and Model Boundaries

This page proves the geometric cutting used in [Chapter 56](../chapters/56-fragmentation-hierarchies.md#fragment-geometric-cuts). It first treats fixed compact real trees, then gives a measurable conditional construction for Chapter 54’s continuously coded random trees. The special self-similar law of Brownian CRT cutting and its additive-coalescent duality are not proved here.

## 1. Cuts exist even with infinite total length

<a id="cuts-length"></a>

Take a compact rooted real tree (T,d,ρ), Borel probability μ and a countable dense sequence vᵢ. Let Rᵢ=∪ⱼ≤ᵢ[ρ,vⱼ]. Each newly added part is a half-open segment from its unique attachment point to vᵢ, with finite length. Assign arc length on these disjoint new pieces and sum, obtaining a sigma-finite length measure ℓ. These pieces cover the nonleaf skeleton: an open branch above any point with a strict descendant contains a dense vᵢ. Any omitted dense endpoints and the root are ℓ-null. Each finite arc has ℓ-length equal to its distance, as follows by approximating endpoints inside Rᵢ.

Place Poisson points with intensity dt da on time times the countable segment parameters and map them into T, giving intensity dt ℓ(dz). There may be infinitely many cuts in the whole tree in finite time. A finite sampled root span R(x₁,…,xₙ) has finite total length, so its cuts are locally finite. That is why finite observations are legitimate. Compactness of a CRT does not imply finite length.

## 2. Avoidance on arcs defines a partition

<a id="cuts-partitions"></a>

\[ i\sim_{\Pi_t}j
\quad\Longleftrightarrow\quad
N([0,t]\times[x_i,x_j])=0,\qquad
P(i\sim_{\Pi_t}j\mid T,x_i,x_j)=e^{-t\,d(x_i,x_j)}. \]

Draw iid μ samples independently of cuts. Length measure is atomless, so conditional on the countably many samples no cut ever hits a sampled point, giving reflexivity. The real-tree inclusion [x,z]⊂[x,y]∪[y,z] gives transitivity. Relabeling iid samples preserves the path law, so the partition process is exchangeable. Finite samples see only finitely many cuts in a finite span and at most n−1 effective changes, and restrictions use exactly the same samples and cuts. This establishes measurability, right-continuous paths and sampling consistency.

Measurability follows directly from the arc criterion: z∈[x,y] iff d(x,z)+d(z,y)=d(x,y), a closed condition. A countable sum over Poisson points gives measurable counts. Separation events are determined by cut times, with no future stochastic integral.

## 3. Measurable conditional construction on coded random trees

<a id="cuts-random"></a>

For Chapter 54’s code h choose fixed dense rational times qᵢ and vᵢ=pₕ(qᵢ). Attachment height is aᵢ=maxⱼ<ᵢ mₕ(qᵢ,qⱼ), with the first maximum 0. Parameterize the added arc by height u∈(aᵢ,h(qᵢ)]. These endpoints are continuous in h. Its height-u ancestor can be represented by the last time before qᵢ with height u. This is Borel in (h,u): “last time>r” is a countable union of zero-minimum conditions for |h−u| on compact intervals. Chapter 54’s minimum formula makes projected ancestor distances measurable.

On the fixed space time×N×nonnegative height first put a Poisson measure of intensity dt #di du, keeping points with aᵢ(h)<u≤h(qᵢ). The measurable-kernel thinning construction of Chapter 48 allows this conditional choice. The ancestor map then gives cut points. Take pₕ(Uⱼ) at independent uniform times as mass samples. Everything is built on fixed measurable spaces, so random e gives a legitimate process, rather than separately chosen versions for each tree.

## 4. The unit interval gives a genuinely self-similar cutting model

<a id="cuts-interval"></a>

Take T=[0,1], μ Lebesgue and cut intensity dt dz. A current interval of mass x is cut at rate x and its conditional cut position is uniform. Future Poisson restrictions on different intervals are independent. Their length masses therefore follow the finite-ν, c=0, α=1 fragmentation with ν the law of ranked (U,1−U). Since total length is 1, bounded time contains finitely many cuts and interval masses always sum to 1. This is a constructed model with identified parameters, not a universal property of real trees.

On a general tree the full remaining component geometries have independent Poisson futures. Recording only sampled partitions or masses may discard geometry controlling future rates, so they are not automatically assigned a universal Markov branching law. On the same CRT use bounded Borel weighted cut intensity w(z)ℓ(dz), or no cuts at all. Pairwise separation rates become ∫[x,y]w dℓ or 0. Existence of the geometry does not specify its evolution.

The special index, conditional component laws and additive-coalescent time reversal of Brownian CRT cutting require separate proofs and remain unproved here; Chapters 57–58 are not borrowed to fill the gap. Return to the [main text](../chapters/56-fragmentation-hierarchies.md#fragment-geometric-cuts).
