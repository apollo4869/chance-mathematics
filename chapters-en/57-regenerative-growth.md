# Chapter 57: How Does a Tree Form Through Random Growth?

A new branch can be grafted without changing any old distance. Yet a different question remains: if birth order is hidden and a few leaves are sampled from the large tree, do they still have the probability law prescribed for the small tree? Growth records an order that sampling may conceal. These operations must agree if local rules are to generate one infinite random geometry.

We know how an excursion encodes a Brownian tree and how cuts may be placed on it. Now start without the completed tree, using only a clock for new lengths and a rule for graft locations. Running finite steps is not the whole task. Compactness after infinitely many branches and the emergence of probability mass from birth records require separate proofs.

## 57.1 Retaining old leaves is not automatically sampling consistency

<a id="growth-consistency"></a>

Grafting near the newest leaf can plainly preserve the old shape when the newest label is deleted. But early leaves may remain near the root while later leaves are pushed farther away, so exchanging labels changes the law. A valid sequential extension does not itself provide a sampling law independent of birth order.

We retain two requirements. A nested construction restricts pathwise to its earlier model on the first m labels; exchangeability makes every m-label restriction have the same law. The first joins stages together; the second prevents initial labels from being privileged. Reducing metric trees also suppresses degree-two vertices by adding lengths, rather than resetting surviving edges to length one.

## 57.2 The same root split can conceal different dependence

<a id="growth-markov-branching"></a>

Temporarily omit lengths. Once root label blocks are given, can each block restart as an independent tree? A common hidden environment can preserve every child’s marginal law while correlating the children. Markov branching excludes that extra dependence: conditional on the root split, children are independent and each uses the same family indexed by its own label count.

Take an exchangeable splitting law qₙ on nontrivial partitions of [n], recursively generate a family member on every block and terminate at singletons. Strictly decreasing sizes give existence and uniqueness of each finite model. Compatibility between different n is an additional claim.

## 57.3 Deleting a leaf can collapse the root split

<a id="growth-root-collapse"></a>

\[ p_n=q_n(\{\{n\},[n-1]\}),\qquad (r_{n-1})_*q_n\big|_{\pi\ne\mathbf1}=(1-p_n)q_{n-1},\quad n\ge3. \]

If one side consists only of the deleted label n, the root branch disappears and the remaining whole tree is already an (n−1)-leaf family member. Only noncollapse is described by a projected nontrivial root split. Thus consistency requires the factor 1−pₙ. Conditional independence and induction preserve children in the noncollapse case; collapse already yields Pₙ₋₁. Adding both contributions proves necessity and sufficiency, tree by tree.

For example, balanced root splitting permits only 2+2 at size four, but size five has 2+3 and deletion from the smaller side leaves 1+3. Failure appears in a five-person calculation, before any infinite limit. The complete criterion is proved in [T-MARKOV-BRANCHING](../foundations/t-markov-branching.md#mb-deletion).

## 57.4 Consistent split probabilities hide a rate measure

<a id="growth-rate-representation"></a>

\[ \gamma_2=1,\qquad\gamma_n=\gamma_{n-1}/(1-p_n),\qquad K_n=\gamma_nq_n. \]

Exchangeability gives pₙ≤1/n, so these numbers are positive and finite. Multiplying by γₙ turns conditional splitting laws into consistent finite measures on nontrivial cylinders. Restrict to Bₘ, the event that the first m labels have separated, with finite mass γₘ. Normalize, use Chapter 8’s construction and paste over increasing Bₘ. This gives a unique locally finite exchangeable κ whose nontrivial [m]-projection is Kₘ.

Driving each block with dt κ(dπ) Poisson rules gives one branching history shared by all restrictions: an m-member visible block waits Exp(γₘ) and splits according to qₘ. A finite sample refines at most n−1 times, so the genealogy is an actual tree. Normalizing κ recovers q, uniquely up to total time scale. This is a general κ representation of consistent Markov branching, not the still-unproved inverse classification of every κ into ν and erosion.

## 57.5 A tree law has not yet selected lengths

<a id="growth-before-metric"></a>

The same q can be equipped with different waiting clocks or separately assigned edge lengths. It records ancestry without selecting Brownian geometry. Even nested finite metric trees can have noncompact completion: infinitely many unit root branches remain pairwise distance 2, while grafting length 1/n at distance 1/(4n) below the newest tip preserves old leaves while increasing root height by 3/(4n), giving vanishing branches but unbounded height.

A concrete growth law must constrain both shape and length. Chapter 54 computed finite sampled-subtree densities for the Brownian CRT. We now reverse the use of that calculation: which grafting kernel turns a k-leaf family member into the (k+1)-leaf law? The old formula now poses a construction problem.

## 57.6 Read a grafting rule from adjacent densities

<a id="growth-density-kernel"></a>

\[ f_k(\tau,\ell)=4^kL e^{-2L^2},\qquad L=\sum_{a\in E(\tau)}\ell_a,\quad |E(\tau)|=2k-1. \]

Here τ is a nonplane labeled binary shape with a root stem, and density is with respect to positive edge lengths. At old total s, split an edge at position a and graft a new branch b. Deleting the new leaf uniquely recovers the old tree and attachment; the edge-splitting Jacobian is one. Dividing adjacent densities gives the conditional kernel below.

\[ \frac{4(s+b)}s\exp\{-2((s+b)^2-s^2)\}\,da\,db,\qquad b>0,\quad a\in R_k. \]

Integration over a contributes old-tree length s; the b-integral is a survival derivative and equals one. Thus attachment is uniform in old skeleton length and conditionally independent of new length. Given the metric tree, edges are not equally likely: a longer edge receives more grafts.

## 57.7 The 4r clock in cumulative skeleton length

<a id="growth-linebreaking"></a>

\[ L_k=\sqrt{\frac{E_1+\cdots+E_k}{2}},\qquad E_i\overset{\mathrm{iid}}\sim\operatorname{Exp}(1),\qquad \ell_{k+1}=L_{k+1}-L_k. \]

Start with a root segment of length L₁ and graft successive segments of length ℓₖ₊₁ at the preceding length-uniform locations. Given Lₖ=s, the next total exceeds r≥s with probability exp{−2(r²−s²)}. The totals are Poisson arrivals with cumulative intensity 2r² and intensity 4r dr. Every step uses fresh exponentials and uniforms, without first sampling an excursion or completed CRT.

The familiar r dr version uses a different scale. Doubling every edge changes the cumulative intensity to r²/2 and gives the 2e convention. This book uses a standard duration-one e. The two are rescalings, not different models; failure to convert changes root distances, total lengths and later cutting rates by a factor two.

## 57.8 The finite growth theorem is more than an animation

<a id="growth-finite-theorem"></a>

Order edges by fixed descendant-label codes and use cumulative length to locate a uniform variable on a specific segment. This realizes a measurable graft kernel. Vertices have zero length mass, so all countably many grafts occur in interiors almost surely. Splitting one edge and adding another increases edge count by two and total length to Lₖ₊₁.

The density-ratio induction proves that every Rₖ has law fₖ. Label symmetry yields the correct law on every specified finite subset; keeping the first m labels recovers the earlier Rₘ pathwise. Thus both validity and genuine sampling consistency are proved, rather than inferred from a plausible picture.

## 57.9 Shorter new branches still do not suffice

<a id="growth-tightness-question"></a>

\[ \frac{L_k}{\sqrt{k/2}}\longrightarrow1\quad\text{a.s.},\qquad L_k\longrightarrow\infty. \]

The strong law gives infinite cumulative length. That does not imply escape to infinity: total skeleton length differs from maximal root distance. Nor would ℓₖ→0 suffice, as the leaf-preserving harmonic example shows. The required control concerns all future branches simultaneously, not merely the newest one.

Let T be the completion of the increasing rooted spans. Rooted convexity lets maximal distance from an old span be tested on all birth leaves. Projection distance to a root segment is determined by three pairwise distances, yielding a countable measurable compactness criterion.

\[ \Delta_n=\sup_{j\ge1}\min_{i\le n}\frac{d(\rho,x_j)+d(x_j,x_i)-d(\rho,x_i)}2;\qquad T\text{ compact}\iff\Delta_n\to0. \]

## 57.10 Why the whole countable growth record can be identified

<a id="growth-joint-identification"></a>

Sampling successive mass points in Chapter 54’s Tₑ gives another sequence of finite spans Rₖᵉ. Its conditional growth kernel is exactly the computed one. A current labeled tree determines its whole past by deletion of larger labels. Thus every finite joint sequence law agrees, not just one-time marginals. Standard Borel finite-tree spaces and countable cylinder uniqueness identify the entire sequence.

The comparison does not insert an excursion into the direct random inputs. It uses an existing realization to prove infinite properties. Compactness and full-support mass in Tₑ make iid samples dense, so Δₙᵉ→0. Whole-sequence identification transfers that measurable event and proves compactness of direct growth. The distinction between marginal and sequence laws is doing real work.

## 57.11 Why completion is still a real tree

<a id="growth-completion-tree"></a>

Every finite collection in the union lies in a finite real tree, so the four-point tree inequality holds and passes to completion. Approximate two limiting endpoints by points of the union. Projection and triangle bounds compare their parameterized segments inside a common finite tree, making them uniformly Cauchy and producing an isometric limiting segment.

For uniqueness, the four-point inequality identifies corresponding points on two segments. Removing an interior point separates the endpoints into open direction classes, so every continuous arc must pass through it. An excursion outside the segment would revisit its attachment point, violating simplicity. Thus completion is a real tree, not merely a compact metric quotient. The [full proof](../foundations/t-linebreaking-crt.md#line-completion) also establishes the Δ criterion.

## 57.12 Infinite total length cannot simply be normalized into mass

<a id="growth-mass"></a>

\[ \mu_n=\frac1n\sum_{i=1}^n\delta_{x_i}. \]

On a finite tree one may sample by length or put mass 1/n on each birth leaf. One measure is diffuse, the other discrete; they differ at every finite stage. Infinite skeleton length cannot be normalized into probability. We choose empirical leaf mass, but its definition does not prove convergence.

Prokhorov distance between empirical measures is determined by finitely many leaf distances and a finite coupling matrix. Thus the Cauchy event is measurable in the growth record. In Tₑ the conditional strong law gives convergence to μₑ. Transfer and completeness yield a unique probability limit μ on the direct compact completion. Rooted GHP limits of finite spans with μₙ provide a measurable version of the whole measured tree.

## 57.13 Direct growth closes into the standard Brownian CRT

<a id="growth-infinite-crt"></a>

\[ (R_n,d,\rho,\mu_n)\longrightarrow(T,d,\rho,\mu)\quad\text{a.s. in rooted GHP},\qquad (T,d,\rho,\mu)\overset d=(\mathcal T_e,d_e,\rho_e,\mu_e). \]

In the common completion, Δₙ controls Hausdorff error, empirical weak convergence controls measure error and roots coincide, proving rooted GHP convergence. Couple with the comparison array, extend the isometry between dense rooted spans and push every empirical measure forward. The limit preserves mass, identifying the full object rather than merely a few sampled distances.

Mass is nonatomic, full-support and leaf-supported. After growth labels and history are forgotten, intrinsic birth-leaf readings satisfy conditional iid mass-sampling identities. This does not make earliest leaves fresh independent samples after all labeled graft history is revealed. [T-LINEBREAKING-CRT](../foundations/t-linebreaking-crt.md#line-mass) proves construction, identification, compactness, mass and the sampling interpretation.

## 57.14 Uniform edge selection appears after lengths are forgotten

<a id="growth-uniform-shape"></a>

Conditional on actual edge lengths, grafting is length-weighted. Conditional only on shape, Dirichlet(1,…,1) edge proportions all have mean 1/(2k−1), yielding uniform-edge shape growth. Earlier shapes are deletions of the current shape, so this is the kernel given the whole shape history. The two rules condition on different information.

\[ N_k=(2k-3)!!,\quad N_{k+1}=(2k-1)N_k,\qquad P(\text{shape}=\tau)=1/N_k. \]

Unique deletion of the newest leaf gives uniform shapes inductively. Conditional on the actual root label split, children are independent uniform trees, a concrete consistent Markov branching family. Looking along one sampled leaf’s ancestry now exposes a new predictive structure through exact counting.

## 57.15 The spine carries an ordered side forest

<a id="growth-spinal-forest"></a>

Fix leaf 1 and list side-subtree blocks \(B_1,\ldots,B_b\) from root toward it. They partition the other m=k−1 leaves. Their internal trees and order uniquely reconstruct the full shape, giving the displayed probability and independent uniform conditional side shapes.

\[ P(B_1,\ldots,B_b\text{ in spinal order})=\frac{\prod_{j=1}^bN_{|B_j|}}{N_{m+1}}. \]

This is not a redrawing of Chapter 20’s population-biased spine. Here a sampled mass leaf in an already identified tree organizes the ancestry. Bias must be calculated from the sampling probabilities, not inferred merely because one path is highlighted.

## 57.16 Counting edges produces a restaurant

<a id="growth-spinal-crp"></a>

\[ P(\text{join }j)=\frac{2n_j-1}{2m+1}=\frac{n_j-1/2}{m+1/2},\qquad P(\text{new})=\frac{b+1}{2m+1}. \]

A side tree with nⱼ leaves, including its stem to the spine, has 2nⱼ−1 edges. The spine has b+1 gaps. A uniform side edge joins that block; a spinal edge starts a new side tree. Total edge count is 2m+1, producing CRP(1/2,1/2), not Chapter 44’s one-parameter Dirichlet-process CRP(0,θ).

At m=0 the first table opens. Each subsequent new table is inserted uniformly among the b+1 gaps. Conditional on the unordered partition, spinal order is uniform. Discovery order numbers tables by first observation; geometric order sorts attachment positions. They are not interchangeable.

## 57.17 Finite regeneration is not an assumption of iid spinal spacings

<a id="growth-decrement"></a>

\[ r(m,j)=\binom mj\frac{N_jN_{m-j+1}}{N_{m+1}},\qquad 1\le j\le m. \]

To obtain the first root-side block of size j, choose its labels, its internal tree and the remaining tree containing leaf 1. Conditional on the first block’s labels the two trees are independent family members. Delete that block and suppress its spinal vertex; the remaining composition restarts at m−j. This gives the full regenerative decrement r, normalized by exhaustive disjoint counting.

The restart is indexed by remaining sample count. Actual Brownian branches can accumulate toward the root; finite r does not imply an ordered list of positive-mass subtrees at iid spacings. Chapter 19 taught us to identify what restarts. Here it is a conditional tree, not an unspecified physical waiting time.

## 57.18 Separate side lengths, spinal length and probability mass

<a id="growth-spinal-metric"></a>

\[ \left(\frac{A_1}{L},\ldots,\frac{A_b}{L},\frac HL\right)\sim\operatorname{Dirichlet}(2n_1-1,\ldots,2n_b-1,b+1),\qquad2L^2\sim\operatorname{Gamma}(m+1,1). \]

Given ordered side blocks, internal shapes are independent uniform trees and L is independent of them. Grouping independent exponential variables representing all-edge Dirichlet(1,…,1) gives the displayed side skeleton totals Aⱼ and spinal length H. Conditional on group totals, internal edge proportions are independent uniform simplices, reconstructing the full finite metric tree.

The common total makes group lengths dependent, and Aⱼ/L is not a full CRT component mass. [T-REGENERATIVE-SPINE](../foundations/t-regenerative-spine.md#regen-metric) proves the Gamma transformation and Jacobian. A regenerative decomposition must specify its conditioning rather than hide dependencies inside an unconditional independence claim.

## 57.19 Continuum spinal frequencies and a new size bias

<a id="growth-spinal-masses"></a>

Remove [ρ,ξ₁] from the completed CRT. Complementary components are open and countable, each with positive mass by full support. The spine has mass zero, so component masses sum to one. The other iid mass samples induce exactly the finite side partition. Strong laws identify frequencies, and Chapter 47’s two-parameter deletion theorem gives independent Beta cuts in discovery order.

\[ V_j\sim\operatorname{Beta}\left(\tfrac12,\tfrac{j+1}2\right)\text{ independently},\quad P_j=V_j\prod_{i<j}(1-V_i),\quad P^\downarrow\sim\operatorname{PD}(1/2,1/2). \]

The first component discovered by ξ₂ is size-biased and has mean mass E P₁=1/3, also the probability that ξ₂ and ξ₃ share a side component. This makes typical branch precise. We have proved continuum spinal masses and finite metric disintegration, not an unproved conditional independent-scaling law for all continuous side geometries.

## 57.20 Turn a general CRP into an actual tree-growth kernel

<a id="growth-general-crp"></a>

Change the rule more broadly, initially for unweighted binary shapes. Take 0<a<1 and θ>0. Mark the root child containing the smallest label. If the other child has u leaves and the marked child v, give the root stem weight a, the other child u−a and the marked child v−1+θ, totaling u+v−1+θ. Recurse inside a selected child; a singleton chooses its unique edge. Finally split the selected edge and add the new leaf.

Positive weights and decreasing recursion give actual finite Markov kernels, realized by countably many uniforms. Expanding along leaf 1 cancels marked-child weights against subsequent denominators. Side block j has total weight nⱼ−a; each gap before an existing branch has weight a and the terminal gap θ. The side partition therefore really follows CRP(a,θ).

## 57.21 Prediction may be exchangeable while whole-tree labels are not

<a id="growth-crp-boundary"></a>

\[ P(12\text{ cherry})=\frac a{1+\theta},\qquad P(13\text{ cherry})=\frac\theta{1+\theta},\qquad P(23\text{ cherry})=\frac{1-a}{1+\theta}. \]

Three leaves separate the claims. Exchangeability of the whole labeled tree requires all three cherry pairs to be equally likely, forcing a=θ=1/2. At that point the recursion reduces to uniform-edge growth. Other parameters yield valid restaurants and valid birth-labeled growth but not automatically exchangeable sampled trees.

Uniform deletion after removing labels asks only for matching marginal shapes, a weaker consistency; matching the joint law with the larger tree is stronger. Failure of label exchangeability does not imply failure of every delabeled model. Nor do GEM(a,θ) frequencies construct a particular non-Brownian compact CRT. The discount a is not Chapter 56’s time-scaling index.

## 57.22 A different typical individual changes spinal weights

<a id="growth-pointed-spine"></a>

Consider a subcritical GW family with 0<m<1. Sampling an original tree and then a uniform member does not make larger trees more frequent in the first stage. Sampling from all individual occurrences does: a tree of size |t| receives weight |t|. This is a concrete genealogical Campbell experiment, different from Chapter 20’s fixed-generation population bias.

\[ E|T|=\frac1{1-m},\qquad \widehat P(T=t,V=v)=(1-m)P(T=t),\quad v\in t. \]

Tonelli gives expected total population Σmʰ, so the probability is normalized. Typical depth H has law (1−m)mʰ. To construct its ancestry, use offspring counts ℓpℓ/m and choose a continuing child uniformly among ℓ possibilities. The bias comes from the requirement of reaching the selected individual.

## 57.23 A product density identifies exactly what regenerates

<a id="growth-spine-density"></a>

\[ \frac{\ell p_\ell}{m}\frac1\ell=\frac{p_\ell}{m},\qquad Q_h(t,v)=m^{-h}P(t)\mathbf1_{|v|=h},\qquad \widehat P=\sum_{h\ge0}(1-m)m^hQ_h. \]

The 1/ℓ factor is essential. Multiplying h ancestral factors while keeping ordinary p at all other nodes gives the actual Qₕ density. Attach independent original GW trees to other children and below the marked vertex. Geometric mixing cancels the m⁻ʰ factor and recovers typical-individual sampling. Given the spine environment, side trees are independent and ancestral environments are iid; the residual geometric depth restarts before termination.

The marked individual’s own offspring retain law p; not every vertex is size-biased. Normalization and conditional independence support and delimit the ancestral interpretation. The [complete proof](../foundations/t-pointed-gw-trees.md#pointed-geometric-spine) requires finite mean, without adding a second moment.

## 57.24 The local tree of a critical family surviving far ahead

<a id="growth-kesten-local"></a>

\[ m=1,\quad0<\sigma^2<\infty,\qquad \frac{1-(1-a_{N-h})^{Z_h}}{a_N}\longrightarrow Z_h\quad\text{in }L^1,\qquad a_N=P(Z_N>0). \]

Critical expected total population is infinite, so the previous bias cannot be normalized. Instead condition on survival to generation N and observe a fixed first h generations. Independence of later descendant families gives the displayed density. Chapter 20’s aₙ∼2/(σ²n) gives pointwise limit Zₕ. The bound 1−(1−a)ᶻ≤za dominates by CZₕ with E Zₕ=1, proving L¹ and total variation convergence of the finite-height law.

Generate the limit directly: along an infinite spine use counts ℓpℓ and a uniform continuing child, attaching independent original critical GW side trees. All side trees are finite on one common good set, leaving a unique infinite ancestral line. This constructs and identifies the Kesten local tree without claiming the infinite-variance extension.

## 57.25 Regeneration and limits must state the retained scale

<a id="growth-local-global"></a>

Unit edges, fixed observed height and survival far ahead give an infinite local tree. Conditioning total size n and scaling by σ/(2√n) gives Chapter 55’s compact CRT. One retains the neighborhood of a long-surviving lineage; the other records macroscopic distances of the whole family. They are not two drawings of one limit theorem.

Likewise finite Markov branching, spinal composition regeneration, subcritical geometric termination and Brownian continuum masses restart different objects under different conditioning. Recognizing those differences determines where a growth argument can be transferred. A shared word does not transfer iid physical waits, mass self-similarity or arbitrary CRT representation.

## 57.26 Sources, proved scope and remaining mathematics

<a id="growth-sources"></a>

[Aldous’s 1993 paper, §4.3](https://www.stat.berkeley.edu/~aldous/Papers/CRT3.pdf), gives inhomogeneous Poisson line-breaking and sampling densities in the r dr, 2e convention. Here the standard-e density yields 4r, and whole-sequence identification, measurable compactness and empirical mass close the construction using this book’s earlier results, in a modern proof organization.

[Pitman–Winkel’s 2009 paper](https://arxiv.org/pdf/0803.3098) distinguishes birth labels, weak and strong sampling consistency for broader recursive growth. We prove the stated finite rules, Brownian case and spinal decompositions. The [Lyons–Pemantle–Peres author manuscript](https://arxiv.org/html/math/0404083v1) is a source for size-biased spines. Our subcritical total-population Palm and finite-variance critical local limit use explicit product densities and Chapter 20, without invoking its infinite-variance conditional-limit argument.

Four companions contain the actual working proofs: T-MARKOV-BRANCHING, T-LINEBREAKING-CRT, T-REGENERATIVE-SPINE and T-POINTED-GW-TREES. General non-Brownian continuous regenerative-tree classification, all two-parameter compact limits and the broad conditional independent-scaling law of continuous side geometries are not proved. Chapter 56’s general hierarchy, infinite-ν and broader-coalescence gaps remain. Successful binary growth determines no general multifurcating CRT and makes no claim about the author’s particular k-ary models or conjectures.

## 57.27 Local growth can form geometry without replacing its conditions

<a id="growth-ending"></a>

The Brownian tree now has another rigorous origin: add its skeleton segment by segment and recover mass from long-run leaf frequencies, rather than first quotienting an excursion or rescaling a conditioned large family. The routes meet through densities, deletion kernels, whole-sequence identification, compactness and mass coupling, not through their shared name.

The spine exposes another hidden condition. Looking backward from a sampled descendant weights ancestors through the sampling mechanism; the same CRP frequencies need not give the same whole-tree exchangeability or geometry. Local rules can create a complex object, but must specify compatible observations and retained scales. If offspring counts change or more branches meet at a point, is continuum branching determined by the superficial count or by the full splitting, scaling and consistency structure? Those relations need fresh tests rather than extrapolation from today’s binary picture.
