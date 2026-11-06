# Chapter 46: When Exchangeable Objects No Longer Form a Sequence

Suppose a survey records a zero or one for the relation between every pair of people. Names are irrelevant: relabeling leaves the law unchanged. Read one person’s record at a time and each row may look like independent fair coin tosses. Put three people’s records together, however, and the relations may reveal an entirely different structure.

What we must identify is no longer just the random probability governing one observation. It is how the same person, appearing in different relations, carries shared random information into each of them.

## 46.1 Identical rows can conceal different three-person worlds

<a id="arrays-row-failure"></a>

Construct two infinite relation tables. In the first, put an independent fair binary outcome on each unordered pair, copy it to the reverse cell and put zero on the diagonal. In the second, independently give each person one of two hidden colors with equal chances; record one between different colors and zero within a color.

Fix a person. In the second model the other people’s colors are independent, and whatever the fixed person’s color, each relation is one with probability one half. Thus each row, excluding its own diagonal, is exactly iid Bernoulli(1/2) in both tables. Applying Chapter43 row by row gives the very same deterministic directing probability.

\[ \mathbb P\{X_{12}=X_{23}=X_{31}=1\}=\begin{cases}1/8,&\text{independent pairs},\\0,&\text{two-color model}.\end{cases} \]

Three people cannot all have different binary colors, so the second probability is zero. Each row representation was correct but did not specify how rows align through the same vertices. The missing object is not more observations in one row but the organization of information shared across rows.

Another legitimate approach remains available: under separate exchangeability whole rows, as random elements of a countable product of E, form an exchangeable sequence. But the way their directing probability responds to every column permutation still needs analysis. A sequence representation does not automatically perform that shared-structure analysis.

## 46.2 Are we relabeling one population or two?

<a id="arrays-actions"></a>

\[ (X_{ij})\stackrel d=(X_{\pi(i)\pi(j)})\quad\text{joint exchangeability},\qquad (X_{ij})\stackrel d=(X_{\pi(i)\sigma(j)})\quad\text{separate exchangeability}. \]

All permutations are arbitrary finite permutations, and equality in law means equality of every finite joint distribution. In the first formula both indices belong to one population, as in personal relations. In the second rows and columns are different populations, such as participants and questions or students and courses. Separate exchangeability implies joint exchangeability, not conversely: an identity matrix survives common relabeling but changes when two rows alone are swapped.

This choice determines which inputs must be shared. Under joint relabeling (i,j) and (j,i) are two directions of one object pair; under separate relabeling they are generally different cross-population relations. A cell (i,i) is a self-relation in the first setting but an ordinary cell with coincident integer labels in the second.

## 46.3 Why a relation needs more than one level of randomness

<a id="arrays-layers"></a>

For a binary relation table, the whole population may share an environment, each person may have an individual attribute and a pair may retain randomness specific to that pair after the other information is fixed. A computable candidate is therefore to take independent global, vertex and unordered-pair uniforms and generate relations with a Borel function.

\[ X_{ij}=F(U_0,U_i,U_j,W_{\{i,j\}}),\qquad i\ne j. \]

The two-color example uses only vertex input; independent edges use only pair input; choosing a random edge probability before generating the entire graph uses global and pair input. Exchangeability of these constructions is easy: relabeling permutes independent random variables. This is far from proving that every exchangeable array arises this way. The difficult direction is extracting these levels from an existing joint law.

## 46.4 Reserving some vertices as an observation background

<a id="arrays-background"></a>

Begin with symmetric arrays without self-relations. Infinitude allows vertices to be split into targets N and an infinite background R; the target subarray still has the original law. Let B record all relations inside R. For target i also record all its relations to background vertices, giving Yᵢ=(B,(Xᵢr)r∈R).

This is not the earlier row directing probability. Each Y retains the same labeled background, allowing different people’s records to be compared against one reference. It is countable standard Borel data, not an assumed true attribute. We must now prove whether the remaining target pairs retain inseparable dependence after these records are given.

In the two-color table, if the background color string is c, a person’s relation string is either c or its complement. Without knowing which color is called zero, equality of two records determines whether those people have the same color. A row’s Bernoulli director retained only one half; records using the same background coordinates retain this alignment.

## 46.5 Projection norms test whether extra data improve prediction

<a id="arrays-proof-mechanism"></a>

Fix a target edge ij and bounded f. Let 𝓖=σ(Yᵢ,Yⱼ) be the local information and 𝓗 include all Y records and any finitely many other target edges. If 𝓗 predicts f(Xᵢⱼ) no better than 𝓖, we can peel off other edges to obtain conditional independence. Chapter9 orthogonal projection gives the exact test.

\[ \|\mathbb E[V\mid\mathcal H]-\mathbb E[V\mid\mathcal G]\|_2^2=\|\mathbb E[V\mid\mathcal H]\|_2^2-\|\mathbb E[V\mid\mathcal G]\|_2^2,\qquad V=f(X_{ij}). \]

The problem becomes equality of two norms. Each depends only on the joint law of the target and the observed data, so exchangeability can act on this comparison without first guessing a latent distribution.

## 46.6 How one relabeling eliminates remaining dependence

<a id="arrays-sandwich"></a>

Split R into two infinite parts. Fix i,j, inject the old background into one half and every other target vertex into the other. Injections preserve finite joint laws and hence the L² prediction norm from 𝓗. After this map every other edge lies within the background or joins i or j to a background point; no other edge becomes ij itself.

Thus the transformed information field 𝓙 is contained in 𝓖. On one side 𝓖⊂𝓗; on the other an equally predictive 𝓙 is contained in 𝓖. Projection norms are sandwiched.

\[ \|\mathbb E[V\mid\mathcal G]\|_2\le\|\mathbb E[V\mid\mathcal H]\|_2=\|\mathbb E[V\mid\mathcal J]\|_2\le\|\mathbb E[V\mid\mathcal G]\|_2. \]

The two predictions are equal. Iterating conditional expectation shows that a test product over finitely many distinct target edges, conditional on all Y, factors into tests conditioned only on the two endpoint records of each edge. The full injection, σ-field and common-null-set argument is in [T-ARRAYS](../foundations/t-arrays.md#arrays-proof-independence). This is the core of representation, not an assumption inferred backward from its formula.

## 46.7 Conditional kernels must use one consistent family of versions

<a id="arrays-common-kernel"></a>

Take a regular conditional kernel K for X₁₂ given (Y₁,Y₂). Symmetry says swapping endpoints preserves the conditional probability. Average over this two-element group to avoid separate exceptional versions and obtain a probability kernel symmetric everywhere. It is defined at every parameter and remains a conditional-law version.

Use the same kernel for every target edge. Standard Borel state spaces have countable generating algebras. All edges, finite edge families and these tests require removal of only a countable union of null sets, after which monotone classes extend the identities. Chapter10 kernel randomization then supplies independent uniforms for the remaining pair choices.

\[ \mathbb P\{X_{ij}\in A\mid(Y_k)_{k\ge1}\}=K(Y_i,Y_j,A),\qquad X_{ij}\ \stackrel d=\ \Gamma(K(Y_i,Y_j),W_{\{i,j\}}). \]

Identical individual conditional marginals are not the same as one conditional product law. The latter is what makes this randomization recover the full array, not merely each edge.

## 46.8 Why de Finetti now applies legitimately

<a id="arrays-profile-director"></a>

Keeping the background fixed while relabeling targets makes (Yᵢ) an exchangeable sequence of standard Borel random elements. Chapter43 gives a random director ν making them conditionally iid. Generate ν from U₀, each record from an independent Uᵢ, then use pair uniforms for kernel randomization.

\[ Y_i=h(U_0,U_i),\qquad X_{ij}\stackrel d=F(U_0,U_i,U_j,W_{\{i,j\}}). \]

The row-by-row attempt failed because row directors did not retain relational alignment. Here conditional independence of edges given common records was established before applying sequence representation to those records. The same theorem is used only after a different prerequisite has been solved. The global input carries a random law of records, not automatically an observable demographic characteristic.

## 46.9 Directions and diagonals cannot be hidden in a similar-case claim

<a id="arrays-directions-diagonal"></a>

For a directed array treat (Xᵢⱼ,Xⱼᵢ) as the full information attached to one unordered pair, then establish independence across distinct pairs, not between its two directions. Put Xᵢᵢ into the vertex record. The rigorous construction uses independent continuous vertex marks to order the pair record internally and decode the original directions, yielding

\[ X_{ij}=F(U_0,U_i,U_j,W_{\{i,j\}})\quad(i\ne j),\qquad X_{ii}=D(U_0,U_i). \]

The [ordered-decoding proof](../foundations/t-arrays.md#arrays-proof-ordered) handles both features by explicitly encoding every equality pattern. Reverse edges retain the same W conditional on latent variables. A random tournament may have exactly one direction equal to one for every pair; using two independent directional coins immediately loses this probability-one constraint.

## 46.10 How two populations obtain two independent vertex pools

<a id="arrays-separate-proof"></a>

Separate exchangeability does not mean taking a common vertex pool and duplicating it. To prove the correct form, independently color common vertices into two types, retain the original matrix relations only from type zero to type one, put † elsewhere and retain colors as marks. This marked relation is jointly exchangeable, so the theorem just proved applies.

In the representation colors depend only on U₀ and singleton inputs. Compare the original type-frequency strong law with its conditional version in the representation to find conditional probabilities one half for each type. Extracting each type gives its conditional kernel. A finite-product calculation, generating types first, then independent type-specific sequences and interleaving them, proves independence of the two pools conditional on U₀. Pair noise does not enter color selection and remains independent.

\[ (X_{ij})\stackrel d=\big(F(U_0,U_i,V_j,W_{ij})\big). \]

All inputs here are mutually independent uniforms. Reverse and diagonal positions do not share a vertex identity, and Wᵢⱼ are independent by ordered row-column position. The complete kernel, extraction and higher-type proof is in [T-ARRAY-VARIANTS](../foundations/t-array-variants.md#array-variants-color). Conditional type probabilities and infinite occurrence have been verified, not assumed from the displayed formula.

## 46.11 A shared column can still connect different rows

<a id="arrays-sharing-example"></a>

Let Uᵢ,Vⱼ be independent fair ±1 variables and set Xᵢⱼ=UᵢVⱼ. The array is separately exchangeable and every cell is fair ±1, but the product around every2×2 rectangle is identically one. Independent cell draws give that product one with probability only one half. Shared row and column information leaves constraints invisible to single cells and even some pairwise comparisons.

In a general model, cells in a column can be dependent through its column latent variable, for example Xᵢⱼ=Vⱼ; the preceding product example retains a rectangular constraint even with pairwise independence. The precise conditional independence says that, given the global, row and column inputs, the remaining cell-specific choices are independent. It never means unconditional independence of every row and column.

## 46.12 Must blocks with no shared vertices be independent?

<a id="arrays-dissociation"></a>

If we first choose a nondegenerate random p in [0,1] and then independently generate a whole graph at that p, even disjoint vertex blocks share dependence through p. Disjoint vertices do not mean absence of global information. A jointly exchangeable array is dissociated when subarrays on disjoint vertex sets are independent; under separate exchangeability both their row sets and their column sets must be disjoint.

This does not require adjacent edges to be independent. The two-color table is dissociated because disjoint populations use independent colors; shared vertices still create triangle constraints. The definition concerns independent sampling of disjoint object blocks, not decomposition into independent cells.

## 46.13 What random law survives finite relabeling averages?

<a id="arrays-invariant-average"></a>

Average a bounded finite-pattern test f over permutations of the first n objects to get Aₙf. Chapter45 finite-group conditional-expectation identity applies at every n: Aₙf conditions on Gₙ-invariant information. These information fields decrease with n, and Chapter15 reverse martingales give the limit.

\[ A_nf=\frac1{|G_n|}\sum_{\pi\in G_n}f\circ T_\pi\longrightarrow\mathbb E[f\mid\mathcal I]\quad\text{a.s. and in }L^2. \]

The field 𝓘 contains information no finite relabeling removes. This is a limit of finite-group averages, not an assumed Haar probability on the infinite group of finite permutations. For f,g on disjoint sets of k,l objects, two independent label lists collide with probability at most kl/n; conditional on no collision they have the jointly sampled law. The averaging discrepancy tends to zero, proving block independence conditional on 𝓘.

## 46.14 What exactly an extreme law excludes

<a id="arrays-extreme"></a>

A nontrivial event in 𝓘 splits the law, by conditioning on it and its complement, into two different exchangeable laws. If 𝓘 is trivial, the Radon–Nikodym density in any convex decomposition must be invariant under relabeling and hence identically one, making the law extreme.

Dissociation is equivalent too. One direction follows from conditional block independence above. For the converse approximate an invariant event by a finite cylinder, then move its objects to a disjoint copy. Dissociation makes the copies independent, while invariance makes them approximate the same event, forcing probability zero or one. The [full proof](../foundations/t-array-ergodic.md#array-ergodic-extreme) handles the need to move both rows and columns in the separate case.

## 46.15 Observable global information is not a latent variable’s name

<a id="arrays-canonical-global"></a>

The standard Borel record space has separable L². Invariant conditional expectations of a countable cylinder algebra encode 𝓘 by a standard Borel random element, allowing actual disintegration into a random exchangeable law Θ. The preceding argument makes that conditional law dissociated and extreme; limits of finite-pattern averages recover its determining evaluations.

\[ \mathcal I=\sigma(\Theta)\quad\bmod P,\qquad P=\int\mu\,\mathcal L(\Theta)(d\mu). \]

The distribution of this extreme-law mixture is unique, as proved in [T-ARRAY-ERGODIC](../foundations/t-array-ergodic.md#array-ergodic-unique). A particular U₀ can contain unused randomness, so observations do not necessarily recover U₀. What the record identifies is the conditional probability law, not every coordinate of an artificial encoding.

## 46.16 Removing global input does not make all relations independent

<a id="arrays-no-global"></a>

For a fixed U₀, disjoint blocks use disjoint independent inputs, so the conditional law is dissociated. If the original law is extreme, these conditional laws must equal it almost everywhere. Fix a good U₀ to obtain a representation without global randomness. Conversely a representation without global input is dissociated.

The two-color graph needs no global input but still has dependent edges; a row-column product array can lack global input while every rectangular product equals one. Extremality removes mixing between different overall laws, not dependence caused by shared objects.

## 46.17 How to compare two representing formulas

<a id="arrays-law-criterion"></a>

A representation is not a unique coordinate system. Choose a countable generating algebra 𝓐 of standard Borel E and test every cell on a finite rectangle or common vertex set. Put an event of 𝓐 in each cell and integrate over the independent inputs, sharing them exactly as the formula requires. These are the finite-cylinder probabilities.

\[ \int\prod_{i,j}\mathbf1_{A_{ij}}\big(F(z,u_i,v_j,w_{ij})\big)\,d(z,\mathbf u,\mathbf v,\mathbf w). \]

Two representations have the same law exactly when all these countably many tests agree, by π–λ and countable product uniqueness. Jointly exchangeable integrals must share W between reverse directions and test diagonal D separately. Single cells, rows or a few moments are insufficient, while pointwise equality of representing functions is unnecessary. [T-GRAPHONS](../foundations/t-graphons.md#graphon-proof-cylinders) proves this complete applicable criterion.

## 46.18 Integrating out the final randomization of a binary edge

<a id="arrays-graphon"></a>

Return to symmetric loopless binary graphs. Given global z and vertex inputs u,v, only pair randomness remains. Integrating it out leaves the edge probability W(z,u,v), a symmetric Borel [0,1]-valued function. Comparing independent pair uniforms with those probabilities restores the same whole-graph law.

\[ W(z,u,v)=\int_0^1\mathbf1_{\{F(z,u,v,w)=1\}}dw,\qquad X_{ij}=\mathbf1\{W(U_0,U_i,U_j)>W_{\{i,j\}}\}. \]

For fixed z this W is a graphon. A dissociated graph can use deterministic W, while a general law can mix them. A graphon is neither one realized adjacency matrix nor a unique naming of unobserved attributes. It expresses a sampling law; directed, multivalued and weighted relations require the corresponding probability kernels rather than a single binary success rate.

## 46.19 Why subgraph probabilities contain more than degrees

<a id="arrays-patterns"></a>

\[ t(H,W)=\int\prod_{ab\in E(H)}W(x_a,x_b)\,d\mathbf x. \]

This does not require exactly H; it requires only that its specified edges occur. To exclude other edges multiply by the appropriate factors (1−W) and expand their finite product. Thus all t(H,W) recover every induced graph probability and determine the infinite graph law. The two models in Section46.1 agree on row information but differ on the triangle test, a minimal computable instance of this criterion.

With random global W the graph law first determines E t(H,W). Disjoint graph unions give products of these densities and identify the distribution of the countable density vector; the [companion proof](../foundations/t-graphons.md#graphon-proof-patterns) completes moment uniqueness using Bernstein approximation on compact cubes. The identified object remains the sampling law, not original coordinates of a particular function.

## 46.20 Equal laws need not differ by invertible renaming

<a id="arrays-nonunique"></a>

On [0,1] take the measure-preserving but noninvertible T(x)=2x modulo one. The graphons W(x,y)=xy and V(x,y)=T(x)T(y) generate exactly the same law because T(Uᵢ) remain iid uniforms. If an invertible modulo null sets, measure-preserving S satisfied V(x,y)=W(Sx,Sy), integration in y would give S(x)=T(x) almost everywhere.

Every full-measure set contains almost every pair x,x+1/2, which T identifies, so it cannot be injective there. This is stronger than exchanging two color names: equality of functions, invertible coordinate equivalence and equality of sampling laws are genuinely different claims. A stronger general Hoover coordinate classification is not proved here and is not conflated with the complete finite-cylinder equality criterion.

## 46.21 Exchangeability on three people is not enough

<a id="arrays-finite-boundary"></a>

Choosing one edge uniformly on three vertices gives a legitimate finite exchangeable graph. An infinite extension would require exactly one edge on every triple. On X₁₂=1, no k≥3 could connect to1 or2. Triples {1,k,l} would then force every pair k,l≥3 to connect, making three edges on {3,4,5}, a contradiction.

This recalls finite extension for sequences, with the new obstruction that overlapping relations must obey common constraints. The background and injection proof genuinely uses infinitude; it cannot assign its conclusion to every finite relation table without qualification.

## 46.22 Three indices have an intermediate layer of shared pairs

<a id="arrays-higher-example"></a>

A relation involving three people may need more structure than one attribute per person and one independent variable per triple. Give every unordered pair an independent fair sign ξᵢⱼ and define each triple relation as their product.

\[ X_{ijk}=\xi_{ij}\xi_{ik}\xi_{jk},\qquad X_{123}X_{124}X_{134}X_{234}=1. \]

A single triple is a fair sign, but four tetrahedral faces share six pairs, each pair appearing twice in their product. This exhibits a legitimate intermediate random layer; the calculation alone does not prove that a layer is indispensable in every equal-law representation. Representation supplies a structure covering all laws, not a unique naming of each latent level.

## 46.23 What the finite-order induction actually does

<a id="arrays-higher-proof"></a>

For an unordered r-person relation, attach one \(U_b\) to each subset b, including the empty subset. To prove this is not mere imagination, T-ARRAYS handles all lower-order labels simultaneously: record everything a proper subset can see together with the infinite background, then use the projection sandwich to establish conditional independence of top-level relations given those records.

\[ X_a=f_r\big((U_b)_{b\subseteq a}\big),\qquad |a|=r. \]

The substantive bookkeeping concerns internal ordering of records. The companion adds independent continuous vertex marks and sorts by them rather than external integers, making lower records an ordinary exchangeable subset family. Represent them inductively, then generate the top layer through a common measurable kernel. Ordered r-tuples store all surjection coordinates on their support and decode using singleton marks, proving repetition cases too. The [complete finite-order induction](../foundations/t-arrays.md#arrays-proof-reservoir) checks these inclusions explicitly rather than calling them similar to two dimensions.

## 46.24 Which subset is shared in a multitype higher relation

<a id="arrays-multitype"></a>

When r indices come from r populations with separate relabeling, each nonempty coordinate subset still has its own random input, beyond a row, column and final-noise picture. The companion embeds the relation into commonly labeled objects using finitely many independent colors, then extracts each type conditionally.

\[ X_{i_1,\ldots,i_r}=F\left(U_0,\big(U^A_{(i_c)_{c\in A}}\big)_{\varnothing\ne A\subseteq[r]}\right). \]

Extraction uses only singleton color data, not higher-order noise. The same partial-index set therefore shares exactly one random variable and different such sets retain independence. [T-ARRAY-VARIANTS](../foundations/t-array-variants.md#array-variants-higher) proves conditional type probabilities, infinite occurrence, kernel randomization and the finite-product identities. Scope is fixed finite order, finitely many types and standard Borel values, not arbitrary infinitary relations or partial group actions.

## 46.25 Permutation invariance remains distinct from orthogonal mixing

<a id="arrays-rotation-boundary"></a>

Chapter45 rotatable-sequence result cannot be copied cellwise into an array classification. Let Xᵢⱼ=ZᵢVⱼ with independent standard Gaussian sequences. Finite row and column orthogonal transformations preserve its law, but a cell has fourth moment nine and second moment one, while every2×2 determinant is zero. It is not an independent standard Gaussian matrix, nor need its cells be normal.

Only with the additional assumption that all cells are iid does Chapter45 two-coordinate rotational characteristic-function equation force Gaussianity. General rotatable-array classification remains a recorded open proof responsibility. The Aldous–Hoover theorem established here is a permutation representation, not completion of a different symmetry classification.

## 46.26 Relational symmetry determines how information is shared

<a id="arrays-insight"></a>

Our initial survey tables were indistinguishable row by row but separated by triangles. Representation turns that gap into a rigorous structure: environment is shared globally, individual data across relations involving that person, pair data within that object pair and higher-order data according to every shared subset.

This neither asserts independence of all relations nor identifies unique hidden real-world causes. Dissociation and extremality determine when global mixing can be removed; finite-pattern criteria and noninvertible-coordinate examples distinguish identifiable laws from unidentifiable names. Mathematics changes the question we can ask: not merely the probability of one cell but which information several relations reuse.

If a relation must also be transitive as belonging to the same class, an arbitrary exchangeable graph is no longer suitable: triples must obey further constraints. What random mass structure remains when only class membership is retained? Representation indicates where to investigate: identify exactly which shared-information layer the extra constraints restrict in the joint law.

## 46.27 Historical sources, proof routes and actual boundaries

<a id="arrays-sources"></a>

Aldous’s [1981 paper](https://doi.org/10.1016/0047-259X(81)90099-3), Representations for partially exchangeable arrays of random variables, appeared in Journal of Multivariate Analysis11,581–598. Hoover’s [original research manuscript](https://www.stat.berkeley.edu/users/aldous/Research/hoover.pdf), Relations on Probability Spaces and Arrays of Random Variables, provides another representation route. Kallenberg’s [1989 paper](https://doi.org/10.1016/0047-259X(89)90092-4) concerns representation and equivalence criteria. Independent contributions are not compressed into one person’s continuous discovery story.

An instructional reference for background records and conditional projections is Austin’s [author notes](https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/austin_arrays.pdf). Our complete argument organizes finite-order multilevel records, auxiliary-mark sorting, ordered decoding and multitype extraction, distinguishing modern reconstruction from historical discovery. Diaconis–Janson’s [research paper](https://arxiv.org/abs/0712.2749) is a further graph-sampling reference, not a substitute for proofs here.

The four complete companions are [T-ARRAYS](../foundations/t-arrays.md), [T-ARRAY-VARIANTS](../foundations/t-array-variants.md), [T-ARRAY-ERGODIC](../foundations/t-array-ergodic.md) and [T-GRAPHONS](../foundations/t-graphons.md). They prove fixed finite-order standard Borel joint and separate representations, repetition cases, dissociated/extreme decomposition and finite-pattern equality criteria. General rotational classification, general Hoover coordinate classification and nonstandard Borel extensions are not claimed.
