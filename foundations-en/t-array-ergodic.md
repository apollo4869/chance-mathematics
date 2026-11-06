# T-ARRAY-ERGODIC: Dissociation, Extreme Laws and Observable Global Information

Work on a nonempty standard Borel array record space, with either joint vertex relabeling or separate row-column relabeling. Finite-order relations and vertex marks are allowed. Groups consist of finite permutations and are countable. We prove the relations between dissociation, extreme exchangeable laws, invariant information and conditional decomposition, without invoking an unproved general group ergodic-decomposition theorem. Return to [Chapter46](../chapters/46-arrays.md#arrays-dissociation).

## 1. Finite-group averages and the actual invariant information

<a id="array-ergodic-average"></a>

Let Gₙ contain all permutations of the first n vertices; for separate exchangeability use the product of the first n row and column permutation groups. Under exchangeable P let 𝓘ₙ be the σ-field of events invariant modulo P under Gₙ, and 𝓘 the information invariant under every finite permutation. The finite average Aₙf is 𝓘ₙ-measurable and integrates like f on every 𝓘ₙ event, hence is its conditional expectation.

\[ A_nf=|G_n|^{-1}\sum_{\pi\in G_n}f\circ T_\pi=\mathbb E[f\mid\mathcal I_n],\qquad A_nf\longrightarrow\mathbb E[f\mid\mathcal I]\quad\text{a.s. and in }L^2\ (f\text{ bounded}). \]

The fields decrease, so Chapter15 reverse martingales give convergence. Their intersection is exactly the completed invariant field: every group element eventually belongs to Gₙ. For an event invariant only modulo null sets, the limsup of its indicator averages is pointwise invariant under every fixed group element and still equals the indicator almost surely. Countability of the group makes the common null set legitimate.

## 2. Why disjoint index sets become conditionally independent

<a id="array-ergodic-collision"></a>

Take bounded cylinder functions f,g supported on disjoint sets of k,l vertices, and take n large enough to contain all their indices. The product Aₙf Aₙg averages over two independently sampled ordered lists without repetitions within either list; Aₙ(fg) also excludes collisions between the lists. The first sampling has collision probability at most kl/n; conditional on no collision it has precisely the second distribution. This gives the following pointwise bound for each fixed array.

\[ |A_n(fg)-A_nf\,A_ng|\le\frac{2kl}{n}\|f\|_\infty\|g\|_\infty,\qquad \mathbb E[fg\mid\mathcal I]=\mathbb E[f\mid\mathcal I]\mathbb E[g\mid\mathcal I]. \]

The second identity follows from the reverse-martingale limits, not from assuming f,g independent. For separate exchangeability, blocks with disjoint row sets and disjoint column sets have collision bound equal to the sum of the row-count product and column-count product divided by n; the same conditioned-sampling proof applies. Disjoint rows alone with shared columns do not suffice, and column latent variables can retain dependence. Avoiding previously sampled indices successively gives conditional product identities for any finite family of blocks.

Define dissociation as unconditional independence of these disjoint blocks: disjoint vertex sets for joint exchangeability, and disjoint sets in both populations for separate exchangeability. The displayed identity immediately gives dissociation when 𝓘 is trivial. Infinite block versions follow from finite cylinders and monotone classes.

## 3. Equivalence of dissociation, extremality and trivial invariant information

<a id="array-ergodic-extreme"></a>

Conversely suppose P is dissociated. Approximate \(\mathbf1_A\) for A∈𝓘 in L¹ by a finite cylinder g between zero and one, within ε. A finite permutation τ moves its indices to a disjoint copy; for separate exchangeability move both populations. Invariance of A makes g∘τ an equally good approximation of \(\mathbf1_A\), while dissociation gives E[g(g∘τ)]=(Eg)². The two approximation errors and the mean error give |P(A)−P(A)²|≤4ε. Hence 𝓘 is trivial.

If 𝓘 contains a nontrivial A, conditioning on A and its complement expresses P as a mixture of different exchangeable laws, so P is not extreme. Conversely if P=tP₁+(1−t)P₂ with 0<t<1, Radon–Nikodym gives h=dP₁/dP≤1/t. Exchangeability of both measures and a change-of-variables test yield h∘τ=h modulo P for each finite τ. Countability makes h invariant on a common version. Trivial 𝓘 makes h identically one, giving P₁=P and likewise P₂. The three properties are equivalent.

## 4. Disintegrating conditional expectations into extreme probabilities

<a id="array-ergodic-kernel"></a>

The standard Borel record space has separable L². For indicators of a countable generating algebra, the rational span of hₘ=E[\(\mathbf1_{A_m}\)|𝓘] is dense in L²(𝓘): approximate an invariant function in the full L² space, then conditionally project. Almost surely convergent subsequences show that (hₘ) generates 𝓘 modulo null sets. Each hₘ has a version in the original record Borel σ-field: approximate its completed-measurable version by simple functions, replace their countably many level sets by Borel sets equal modulo null sets, and pass to a limit. All m require only one further common null set. Thus Z=(hₘ) is a Borel-valued code whose completed σ-field equals 𝓘.

Chapter10 supplies \(P_z\)=Law(X|Z=z). Conditional-independence and invariance identities on a countable cylinder algebra, countable index blocks and countable permutations give one null set outside which \(P_z\) is both exchangeable and dissociated. The good set of z is Borel because these are countably many kernel-evaluation equalities; replace bad values by the law of a fixed constant array. This is a genuine Borel kernel of extreme probabilities, with P=∫\(P_z\) Law(Z)(dz).

Set Θ=\(P_Z\). Chapter43 proves that the probability parameter space on record space is standard Borel. Since Θ(Aₘ)=hₘ, we have 𝓘=σ(Θ) modulo null sets. The observable object is this random extreme law, not the name or full contents of a particular representing U₀, which may include independent randomness never used by the output.

## 5. The mixing law is unique, not the representing function

<a id="array-ergodic-unique"></a>

Exchangeable dissociated probabilities form a Borel subset of the probability parameter space: both properties are expressed by countably many cylinder-algebra equalities. If P has another mixture π over this set, finite-group averages Aₙ\(\mathbf1_{A_m}\) converge almost surely to μ(Aₘ) under each extreme μ. Integrating over π and taking a common set over m shows that these limits from the observed record give every determining evaluation of μ. Their distribution is fixed by P, so π is unique.

For fixed U₀, disjoint blocks in a representation use disjoint independent inputs, so the conditional law is dissociated. If P is extreme these conditional laws equal P almost everywhere: otherwise a level set of a countable determining evaluation splits the mixture into two distinct exchangeable laws. Fixing a good U₀ gives a representation with no random global input. Conversely such a representation is dissociated. Thus omitting global randomness corresponds exactly to dissociation and extremality, not independence of vertices and all pair relations.
