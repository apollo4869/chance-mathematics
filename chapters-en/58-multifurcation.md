# Chapter 58: From Binary Trees to Multifurcating Random Geometry

A finite tree whose internal vertices each have three children seems destined to leave a ternary continuum tree. A picture readily supports that judgment: draw thinner branches, and the three children still appear to be there.

A scaling limit, however, compares distances, roots and mass rather than branching symbols on paper. Three children may exist without all three directions retaining distinguishable length at the chosen scale. To determine what survives, we need the probability law of the tree, not just its offspring count.

## 58.1 Ternary discrete trees, binary continuum limits

<a id="mf-counter"></a>

Take a concrete reproduction rule: no children with probability 2/3, and exactly three with probability 1/3. The mean is 1 and the variance 2. This is not an infinite regular ternary tree, but a critical GW tree that becomes extinct. Retain only realizations with exactly n vertices.

If I vertices are internal, the number of edges is both 3I and n−1, hence n=3I+1. For feasible n, all full ternary plane trees have equal conditional probability. Chapter 55 now applies: rescaling distances by \(\sqrt2/(2\sqrt n)\) and using uniform vertex mass gives the standard Brownian CRT. Every nonroot branch point in that limit has only two descendant directions.

This is a direct consequence of a spatial limit theorem, not an appeal to an imprecise drawing. Fixed finite offspring degree does not determine continuum branching. The relevant object is therefore no longer an integer alone, but a collection of choices: the tree law, conditioning, rescaling and sampling rule.

## 58.2 A rigorous counterexample for every fixed k

<a id="mf-gw"></a>

\[ P(\xi=0)=1-\frac1k,\quad P(\xi=k)=\frac1k,\quad E\xi=1,\quad \sigma^2=k-1,\qquad k\ge2. \]

Conditional on total size n, along \(n=1+kI\to\infty\),

\[ \left(T_n,\frac{\sqrt{k-1}}{2\sqrt n}d,\rho,\frac1n\sum_{v\in T_n}\delta_v\right)
\Rightarrow(\mathcal T_e,d_e,\rho_e,\mu_e). \]

Here k is fixed; the statement does not include a triangular array with k growing with n. Every conditioning event has positive probability, the lattice span k is reflected in feasible sizes, and uniform vertex mass is not uniform internal-vertex mass. [T-KARY-UNIVERSALITY](../foundations/t-kary-universality.md), Sections 1–2, verifies the hypotheses. Its actual inputs are Chapters 53–55’s finite-variance conditioned-tree results, whose independent final review remains open.

The common limit does not make the finite models identical. Variance enters the scale, feasible sizes differ, and combinatorial probabilities differ. Universality says that under these hypotheses and scales, certain differences disappear from the limiting distance–mass law.

## 58.3 How many directions does a branch point have?

<a id="mf-degree"></a>

For a point b in a real tree, count the connected components after deleting b; call this \(\deg(b)\). Away from the root, one direction points towards the root, while the others are descendant directions. Thus binary branching in the Brownian CRT means unrooted degree 3.

Finite sampling omits directions containing no sampled point. An infinite-degree branch point can display at most three directions in a three-leaf reduced tree. A ternary-looking reduced picture cannot determine the degree in the full tree.

Conversely, with fully supported mass an infinite iid sample is dense. If a point has four open directions, some sample occurs in each and a finite reduced tree must display four directions. Chapter 54’s binary reduced-tree laws therefore exclude such a point. This countable dense-sample argument upgrades a finite-sampling assertion to a property of the whole tree.

## 58.4 Degree does not determine mass proportions

<a id="mf-mass"></a>

A three-direction junction can divide mass near \((1/3,1/3,1/3)\), or near \((0.98,0.01,0.01)\). The number of directions does not determine which is more likely; we must also specify how the junction is selected.

In the standard Brownian CRT take the root and two independent mass samples. Their unique junction b is selected by a precise rule. Orient its three components by those labels. Their masses satisfy

\[ (M_0,M_1,M_2)\sim\operatorname{Dirichlet}(1/2,1/2,1/2). \]

The proof does not assume an unknown uniform distribution on branch points. A new label in a reduced tree is inserted uniformly among edges. A direction with a labeled leaves has 2a−1 edges and gains two upon insertion. The directions form a Pólya urn with initial weights 1 and reinforcement 2. Chapter 44 gives a Dirichlet limit, and the conditional strong law on the actual tree identifies it with component mass. Section 4 of the companion gives the full argument.

Mass splits can therefore be identified rigorously, but the answer depends on sampling. Two formulas called “branch-point mass distributions” need not refer to the same experiment.

## 58.5 Another k-ary tree is a different model

<a id="mf-growth"></a>

Replace independent reproduction conditioned on total size by sequential growth. Start from one root edge. At each step choose an edge uniformly, insert a vertex and attach k−1 new edges. The new vertex has k descendant directions. After n steps there are kn+1 edges and \((k-1)n+1\) leaves.

This is the published Haas–Stephenson k-ary growth model. It has the same internal offspring count as the conditioned GW example, without thereby having the same probability law. Growth repeatedly subdivides old paths; with unit edge lengths this changes distances between old endpoints. These finite trees are not nested isometric subtrees.

Theorem 1.1 of the [published 2015 paper](https://archive.numdam.org/articles/10.1214/14-AIHP622/) gives a k-ary fragmentation-tree limit on scale \(n^{-1/k}\), different from the square-root scale of finite-variance GW trees. We introduce that whole-tree theorem as a sourced external result; a complete book proof of its spatial tightness is still missing. We first prove a mass statement that distinguishes the models without using the full scaling theorem.

## 58.6 Following a persistent vertex reveals reinforcement

<a id="mf-urn"></a>

Fix the first inserted vertex v. It has k+1 unrooted directions, including the root direction, each initially containing one edge. An operation in one direction adds k edges there. If it has been selected \(N_i\) times, its next-selection probability is

\[ \frac{1+kN_i}{\sum_{j=0}^k(1+kN_j)}. \]

The prediction rule reduces one statistic of the tree to a solvable urn. Dividing weights by k gives a Dirichlet mixture with initial parameter 1/k. Hence the asymptotic leaf proportions are

\[ (D_0,\ldots,D_k)\sim\operatorname{Dirichlet}(\underbrace{1/k,\ldots,1/k}_{k+1}). \]

The root direction initially has no leaf and each other direction one; counting leaves separately gives the same limiting proportions. [T-PUBLIC-KARY-GROWTH](../foundations/t-public-kary-growth.md) gives the exact Gamma probability of a direction word, conditional kernels and strong-law proof.

At k=2 the three parameters are 1/2, connecting with the Brownian split. At k≥3 this remains an empirical mass limit at a specified persistent discrete vertex. It is not a universal formula for every continuum k-ary tree, and does not alone identify that vertex in a GHP limit.

## 58.7 When the square-root scale ceases to apply

<a id="mf-tail"></a>

The fixed-k GW counterexample has bounded offspring, hence finite variance however large k looks. Changing three possible children to four may leave the decisive hypothesis untouched. Changing the tail can alter it.

Chapter 14 separated finite-variance sums from stable domains of attraction. In a genealogy, a heavy tail allows a few individuals to produce very large families. Population counts may scale to continuous mass, but a new one-dimensional limit law is insufficient: we must still construct the ancestry of that mass.

We separate population from genealogy. Independent families of initial masses x and y should together have the same future law as a family of mass x+y. This branching requirement suggests an exponential Laplace transform, but a formal expression is not yet a probability kernel.

## 58.8 Constructing continuous-state population from reproduction

<a id="mf-csbp"></a>

\[ \psi(q)=a q+\beta q^2+\int_0^\infty(e^{-qr}-1+qr)\pi(dr),\qquad
\int(r^2\wedge r)\pi(dr)<\infty,\quad a,\beta\ge0. \]

We use nonlinear finite-mean critical/subcritical mechanisms satisfying \(\int_1^\infty dq/\psi(q)<\infty\). This condition first controls extinction height, and later genealogical compactness. Put \(v_\lambda=\psi^{-1}(\lambda)\), \(c_\lambda=\psi'(v_\lambda)\). The following pgf is chosen to align the discrete population’s Laplace evolution with one ODE.

\[ g_\lambda(s)=s+\frac{\psi(v_\lambda(1-s))}{v_\lambda c_\lambda},\qquad
\partial_tu_t(q)=-\psi(u_t(q)),\quad u_0(q)=q. \]

Expansion gives a positive constant coefficient, zero linear coefficient and nonnegative remaining coefficients from Lévy integrals, summing to one. Individuals reproduce at the end of rate-cλ exponential lifetimes. Starting with \(\lfloor x v_\lambda\rfloor\) ancestors and dividing population by vλ gives limiting single-time transform

\[ E_xe^{-qZ_t}=\exp[-x u_t(q)]. \]

[T-CSBP-SEMIGROUPS](../foundations/t-csbp-semigroups.md) proves that the probability kernels exist, are measurable, satisfy Chapman–Kolmogorov and branching, and act strongly continuously on \(C_0\). Chapter 28 then realizes càdlàg paths. Random paths are not inferred from the ODE alone.

## 58.9 Extinction height and stable population scaling

<a id="mf-extinction"></a>

\[ P_x(Z_t=0)=e^{-x v(t)},\qquad
\int_{v(t)}^\infty\frac{dq}{\psi(q)}=t. \]

Taking the Laplace parameter to infinity gives the probability of being exactly zero at time t. Grey integrability makes v(t) finite for each positive t. This is stronger than decreasing mean: \(\psi(q)=aq\) yields deterministic decay \(Z_t=xe^{-at}\), with no finite-time extinction.

For the stable mechanism \(\psi(q)=q^\alpha,1<\alpha\le2\),

\[ u_t(q)=\left(q^{1-\alpha}+(\alpha-1)t\right)^{-1/(\alpha-1)},\quad
v(t)=((\alpha-1)t)^{-1/(\alpha-1)}. \]

Population scaling follows directly. Yet population alone does not record which masses share ancestors. A tree requires complete reduced genealogies consistent across sampling intensities.

## 58.10 Why colour terminal leaves?

<a id="mf-colouring"></a>

Treat the exponential lifetimes as actual edge lengths. Take Poisson\((b v_\lambda)\) ancestors, generate independent finite GW real trees and join them at one root. Retain each terminal leaf independently with probability μ/λ and keep its paths to the root. We want the smaller forest to have exactly the same type of law at parameter μ.

This is much stronger than matching average population. Every ancestral path seen by a coarse sample must preserve its distances inside the finer tree. Deleted side branches disappear, while suppressed unary chains must retain the sum of their lengths.

The chosen \(g_\lambda,c_\lambda\) satisfy precisely this requirement. A family retains a leaf with probability \(v_\mu/v_\lambda\). Unary suppression changes lifetime rate cλ to cμ and pgf gλ to gμ. Sections 1–2 of [T-LEVY-HEIGHT](../foundations/t-levy-height.md) calculate the conditional kernels, geometric sums of exponential lifetimes and Poisson ancestral thinning. This is the core consistency of Duquesne–Winkel’s published construction, not a new model proposed for this chapter.

## 58.11 From finite genealogies to a compact real tree

<a id="mf-compact"></a>

Consistent colouring constructs nested finite real forests on one probability space. Their union and completion still require a compactness argument: bounded height does not exclude infinitely many branches of fixed positive length. An infinite star can have height 1 and fail compactness.

Fix ε, divide height into ε-grid levels, and count points with descendants at least ε farther away. Their expected number is at most

\[ b e^{-a j\varepsilon}v(\varepsilon)\quad\text{at level }j\varepsilon. \]

The bound and monotonicity make the limiting count finite at each level. The forest height is finite almost surely, so finitely many such levels give a finite 2ε-net. Total boundedness followed by completion yields a compact real tree. Section 3 handles common null sets, preservation of arcs and Hausdorff convergence.

Compactness comes from controlling extinction height and long branches together, not merely from compactness of each finite tree.

## 58.12 Limiting leaf mass is not skeleton length

<a id="mf-leafmass"></a>

Put one unit at each terminal leaf to form ξλ. As sampling intensifies, the mass normalization is ξλ/λ, rather than division by a predetermined leaf count. Its total-mass transform satisfies

\[ E\exp[-q\,\xi_\lambda(\mathcal F)/\lambda]
\longrightarrow \exp[-b\,\psi^{-1}(q)]. \]

This controls total mass, not its location. The companion divides intensity marks into unit bins, uses exchangeability of future bins, projects points onto each coarse tree and applies conditional strong laws to countably many continuous tests. Uniform projection errors then assemble a finite random measure m on the whole tree. Total mass can have infinite expectation in the critical case; no L¹-bounded martingale is used.

Changing sampling intensity again, retained leaves are conditionally Poisson with intensity tm. This kernel identifies m as diffuse, carried by leaves and fully supported. An arc can have positive geometric length but zero m-mass. Distance and mass retain different structures.

## 58.13 Why stable mechanisms produce infinite branching

<a id="mf-stable"></a>

For \(\psi(q)=q^\alpha\), the pgf becomes \(s+(1-s)^\alpha/\alpha\). At α=2 only 0 or 2 offspring are possible. For 1<α<2 every offspring count at least 2 is possible. Unbounded support alone does not prove infinite degree in the limit; every finite tree still has finite degrees.

Follow the same branch point while refining the sample. If a coarse tree has d≥2 retained descendant directions there, the actual fine-tree count D has conditional pgf

\[ E[z^{D-d}\mid d]
=\left(\frac{q}{1-(1-q)z}\right)^{d-\alpha},
\qquad q=(\mu/\lambda)^{1/\alpha},\quad1<\alpha<2. \]

For fixed z<1 the right side tends to zero as λ→∞, so D diverges. Monotonicity under inclusion upgrades convergence in probability to almost sure divergence. Density ensures every nonroot branch point already appears at some finite level. Thus the stable mechanism α<2 gives countably infinite degree at every nonroot branch point, while α=2 stays binary. Section 6 supplies factorial tilting and the common-null-set argument.

This is a genuinely different branching mechanism, not a rule assigning a fixed k to α. Infinite continuum branching and fixed discrete k-arity are different classifications.

## 58.14 Stable scaling includes mass

<a id="mf-scaling"></a>

The stable finite-reduction kernels determine joint length and mass scaling. Multiplying lengths by r requires multiplying mass by \(r^{\alpha/(\alpha-1)}\), with ancestral parameter \(b r^{1/(\alpha-1)}\). Changing mark intensity and checking lifetime rates and Poisson ancestor counts proves the law of the whole compact measured forest, not just its height.

This forest has random total mass with transform \(e^{-b q^{1/\alpha}}\). It is not automatically a single mass-one stable CRT. Excursion measures and disintegration by duration require separate proofs, particularly when comparing conventions with standard e.

## 58.15 Lévy jumps are not tree height

<a id="mf-height"></a>

Chapter 52 distinguished the Łukasiewicz path from height: one records pending offspring, the other ancestral-chain length. The distinction survives the limit.

Using a spectrally positive Lévy path X directly as tree height would mistake a batch of pending offspring for a vertical ancestral distance. Classical Lévy-height theory instead asks which earlier times remain on the ancestry of the individual explored at time t. This involves backward interval infima, not Xₜ itself.

\[ \frac1\varepsilon\int_0^t
\mathbf1_{\{X_s-\inf_{s\le r\le t}X_r<\varepsilon\}}\,ds. \]

Under precise hypotheses and local-time normalization, this approximation produces classical height H; Grey’s condition controls its continuous version. Sections 1.2–1.4 of [Duquesne–Le Gall’s 2002 monograph](https://arxiv.org/pdf/math/0509558) give the classical theory. It is not a consequence of the population ODE, and Chapter 37’s continuous-semimartingale Tanaka formula cannot simply be transferred.

The book’s boundary must remain explicit: we have reconstructed reduced Lévy forests with mass, stable degrees and scaling. Full identification from X’s reversed record local time, Ray–Knight and heavy-tailed conditioned-tree functional limits are not all written out. The companion’s final section lists the missing steps. These are unclosed proofs, not only proved results awaiting expert signatures.

## 58.16 Another infinite degree comes from repeated grafts

<a id="mf-icrt"></a>

Infinite degree does not uniquely specify a stable tree. Some joinpoints can instead be chosen repeatedly with positive weight. A public ICRT construction separates diffuse grafting from persistent hubs.

Take nonnegative parameters \(\theta_0^2+\sum_{i\ge1}\theta_i^2=1\), with positive-index parameters arranged in nonincreasing order if desired. The standard ICRT domain additionally requires \(\theta_0>0\) or \(\sum_{i\ge1}\theta_i=\infty\). A Poisson process of intensity \(\theta_0^2 dx\,dy\) on \(0<y<x\) supplies cutpoints x and joinpoints y. For each θᵢ>0, an independent rate-θᵢ Poisson clock uses its first arrival to locate a hub; every later arrival cuts a new branch and joins it at that same hub.

Section 2 of [Aldous–Pitman, PTRF118(2000),455–482](https://www.stat.berkeley.edu/~pitman/525.pdf) gives this model. Repeatedly selecting a persistent hub is not automatically equivalent to a stable branch point revealing infinitely many directions under finer sampling. Their parameters, reduced-tree laws and mass theories require separate constructions.

## 58.17 Why infinitely many clocks still allow sequential grafting

<a id="mf-localfinite"></a>

The following clock and local-finiteness calculations only require square summability, so they also make sense beyond the standard ICRT domain; they do not remove its additional restriction. Square summability has a precise role. The number of type-i cuts in [0,R] is the number of arrivals minus the first, with mean at most \(\theta_i^2R^2/2\). The total number of cuts in every bounded window is finite, so they can be ordered. Each joinpoint precedes its cutpoint and is already represented when the branch is attached.

\[ P(\eta_1>t)=e^{-\theta_0^2t^2/2}\prod_{i\ge1}(1+\theta_i t)e^{-\theta_i t}. \]

The first-cut formula expresses at most one arrival from each clock; square summability controls the infinite product’s logarithm. [T-ICRT-POISSON](../foundations/t-icrt-poisson.md) proves local finiteness, finite grafting, real-tree completion and infinite-degree hubs.

When θ₀=1 alone, cut intensity is rdr, the common 2e convention of Chapter 57. Standard e has half the edge lengths and clock 4rdr. The same name “Brownian CRT” does not remove that factor of two.

## 58.18 Valid infinite grafting may still be noncompact

<a id="mf-star"></a>

Deliberately relax the standard domain and take θ₁=1 with all other parameters zero. This violates both alternatives of the standard-domain condition and is not a standard ICRT parameter. Under the same grafting algorithm, every new branch joins one hub, with independent exponential lengths. Almost surely infinitely many exceed 1. Points at distance 1 from the hub are pairwise distance 2 and cannot be covered by finitely many small balls.

This is a legitimate complete grafting tree under the relaxed parameters, but not a compact one; it is not a noncompact example inside the standard ICRT family. Published ICRT parameter restrictions and mass construction cannot be omitted. Constructing the clocks does not automatically produce a random probability tree in compact GHP space. The companion distinguishes proved grafting results from general ICRT mass and compactness classifications.

## 58.19 Comparing models without erasing their differences

<a id="mf-compare"></a>

Four routes can now be compared precisely. Conditioned GW trees with fixed finite k fall into the Brownian limit through finite variance and size conditioning. Published uniform-edge k-ary growth has a different Markov rule, with height scale \(n^{1/k}\) and a k-ary fragmentation limit. Stable Lévy mechanisms reveal infinite branching under refinement; α describes tails and scaling rather than offspring count. ICRT separates diffuse randomness from persistent hubs.

Trees may share a statistic, even infinite degrees, without sharing a law. Conversely, different discrete offspring counts can share the same Brownian spatial limit. Equality of models requires determining reduced-tree distributions, consistency and reconstruction of the same infinite measured object. A Dirichlet marginal alone cannot establish it.

## 58.20 Where changing assumptions changes the conclusion

<a id="mf-boundaries"></a>

Letting k vary with size leaves the fixed-offspring theorem. Replacing size conditioning by height or leaf-count conditioning requires new conditional path estimates. Infinite variance does not automatically place a law in a stable domain of attraction. Mass proportions without control of thin branches may give GP information without GH tightness. Consistent reduced-tree laws alone do not ensure a compact completion.

These restrictions do not forbid extensions. They identify concrete tasks: for a chosen new model, establish the needed path limit, length control, mass construction and determining finite observations. Classical answers and book proofs still missing must be recorded separately. “Not proved here” does not mean an open mathematical problem.

## 58.21 Public sources and proof entrances

<a id="mf-sources"></a>

Every model and result in this chapter comes from public classical theory. Aldous’s [CRT III (1993)](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf) supports Brownian reduced trees. Haas–Stephenson’s [published 2015 article](https://archive.numdam.org/articles/10.1214/14-AIHP622/) specifies the k-ary edge-growth model. Duquesne–Winkel’s [published 2007 paper](https://perso.lpsm.paris/~tduquesne/Documents/Duquesne_Winkel_PTRF_2007.pdf) specifies colouring-consistent Lévy forests. Duquesne–Le Gall’s [Astérisque281 (2002)](https://arxiv.org/pdf/math/0509558) and [2005 paper](https://www.imo.universite-paris-saclay.fr/~jean-francois.le-gall/Levy-final.pdf) provide classical height and Lévy-tree theory. Aldous–Pitman’s [2000 paper](https://www.stat.berkeley.edu/~pitman/525.pdf) specifies ICRT. The 2002 monograph’s preprint was uploaded in 2005; upload year is not first publication year.

Book proofs are in [T-KARY-UNIVERSALITY](../foundations/t-kary-universality.md), [T-PUBLIC-KARY-GROWTH](../foundations/t-public-kary-growth.md), [T-CSBP-SEMIGROUPS](../foundations/t-csbp-semigroups.md), [T-LEVY-HEIGHT](../foundations/t-levy-height.md) and [T-ICRT-POISSON](../foundations/t-icrt-poisson.md). The main text retains the mechanisms; companions handle kernels, colouring, compactness, mass and common null sets. External theorems without complete book proofs are explicitly marked there. No unpublished author papers or original research supply chapter material.

## 58.22 A limit preserves more than a branching symbol

<a id="mf-understanding"></a>

The opening ternary tree has not disappeared behind a slogan about scales. We specified its law, feasible sizes, variance and distance normalization, and obtained a binary Brownian limit. A different published growth rule gave a different reinforcement and mass law. Consistent finite genealogies then showed that continuum branching must pass separate tests of distance, compactness and mass; drawing a jump path is insufficient.

There is no word-for-word translation from microscopic branching to continuum geometry. Some differences disappear at the chosen scale; others remain through tails, persistent hubs or splitting kernels. These judgments depend on finite probabilities, path estimates and consistency that jointly establish a genuine random geometric object.

For a proposed growth rule, the first task is therefore not to give it a new CRT name. Compute its reduced laws, test its sampling rules, control the lengths of thin branches and prove where mass comes from. Only then does a new continuous shape become a mathematical object that can be compared, identified and used to formulate further precise questions.
