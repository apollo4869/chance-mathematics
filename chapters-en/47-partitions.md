# Chapter 47: How Do Random Partitions Grow, Merge and Evolve?

Two people in a relation table are recorded as belonging to the same class. A third belongs to the class of one of them. If the table really records classification, its remaining entry can no longer be a fresh coin toss: it too must say same class.

This small transitivity requirement changes the problem of the whole random table. We no longer ask how each edge is generated, but whether these mutually consistent relations arise from class masses that can gradually be identified.

## 47.1 Three edges can no longer decide separately

<a id="partitions-transitivity"></a>

The independent fair-edge model of Chapter 46 allows 12 and 23 to be connected while 13 is not, an event of probability 1/8. It is legitimate as a general relation and impossible as classification. Renaming variables in an array representation does not represent random classes; the law must be concentrated on equivalence relations.

Partition N into disjoint nonempty blocks covering N, and call the partition Π. Blocks have no intrinsic names; for now the first block means the one discovered by its least member. Exchangeability requires every finite relabeling to preserve the law. It permits two specified individuals to share a class without assigning that class an external name.

This uses additional structure rather than weakening the previous chapter. A general array requires analysis of pair noise; transitivity may organize that information into shared classes. Recovering the sizes of those classes from observed equality relations requires a new proof.

## 47.2 A finite exchangeable classification may not extend

<a id="partitions-finite"></a>

Choose uniformly a pair among three people to share a class, leaving the third alone. This is a fully exchangeable finite partition. In any infinite extension, every triple would have exactly one pair and a singleton. Every class would then have at most two members, and there would be at most two classes. At most four people could exist, contradicting an extension to N.

Infinitude is therefore a genuine hypothesis. We need finite restrictions Πₙ whose laws agree after deleting the last label and are exchangeable at every level. Sampling consistency is what permits the construction of Chapter 8. A realized infinite partition has coherent restrictions on the same sample, not merely similar-looking formulas.

## 47.3 Names can be forgotten, proportions cannot be assumed

<a id="partitions-frequency-question"></a>

The natural reading of a class is its count among the first n people divided by n. For an arbitrary deterministic partition that proportion need not converge; even an infinite block can have zero density, as with the squares. Whether exchangeability rules out these possibilities is a difficulty to solve, not an assumption to hide in the definition of frequency.

Infinitely many positive frequencies may sum to one or to less than one. The remainder is not simply another small class: if each individual there appears only once, it is the aggregate proportion of singleton blocks. We must identify both block frequencies and mass not carried by positive-frequency classes.

## 47.4 Attach colors first, then forget them

<a id="partitions-labels"></a>

An apparent detour makes an existing theorem applicable. Independently attach a continuous uniform label to each block. Members of a block read the same label; different blocks use independent labels. The countably many labels are almost surely distinct, so checking Xᵢ=Xⱼ recovers Π exactly, with no loss of classification information.

Relabeling changes discovery order, but iid labels do not depend on that order. The finite conditional labeling kernel depends only on the equivalence relation; integrating over Π makes X an infinite exchangeable sequence. Chapter 43 now applies legitimately: conditional on a random probability μ, X is iid. Unlike applying de Finetti row by row to a general array, we have proved that the entire object to be represented is a sequence of labels.

\[ \Pi=\operatorname{Eq}(X),\qquad \mathcal L(X\mid\mu)=\mu^{\otimes\mathbb N}. \]

We have not posited μ as a population parameter in advance. It is obtained in reverse from the exchangeable law. The auxiliary colors will be integrated out; only the part of μ identifiable from equality relations remains.

## 47.5 How atomic masses become class frequencies

<a id="partitions-frequencies"></a>

Given μ and Xᵢ=x, the other indicators of belonging to i’s class are independent with success probability μ({x}). The conditional strong law gives the following limit. Countably many i allow one common probability-one set. Every positive atom is eventually sampled almost surely, so infinite observation misses no positive-mass class forever.

\[ \frac1n\#\{j\le n:j\sim i\}\longrightarrow F_i=\mu(\{X_i\})\quad\text{a.s. for all }i. \]

This answers the existence question rather than merely naming a frequency. The left side is computed from the partition alone; the right side explains its existence through atomic masses under conditional independent sampling. Members of the same block have the same frequency, which must not be counted repeatedly in the total mass.

## 47.6 Dust is not one common infinitesimal class

<a id="partitions-dust"></a>

Two independent μ draws coincide at a zero-mass point with probability zero. Intersect over all countably many pairs: every zero-frequency block is singleton. This is a genuine consequence of infinite exchangeability; the earlier square-number block is not exchangeable and does not contradict it.

Rank distinct positive block frequencies as S₁≥S₂≥…, with sum at most one. The remainder d=1−ΣSⱼ is dust mass. Draws from the nonatomic part of μ are all distinct, yet their aggregate density is d by the strong law. A zero frequency for each singleton and density d for their union concern sums and limits that cannot be interchanged.

For example, masses 2⁻ʲ give infinitely many blocks without dust. If everyone is singleton, all S are zero and dust mass is one. Block count and total positive frequency distinguish these extremes.

## 47.7 Paintbox: reconstruct the entire classification from masses

<a id="partitions-paintbox"></a>

Now reverse the experiment. Given decreasing nonnegative s with total at most one, draw consecutive intervals of lengths sⱼ in [0,1]. Each individual samples an independent uniform point. Draws in the same positive-length interval share a class; every draw in the remainder is singleton. Painting the remainder one common color would incorrectly create another positive-mass block.

This is a paintbox. Kingman’s representation says precisely that every infinite exchangeable partition is uniquely a mixture of these laws over its ranked masses S, and that conditional on S its entire law is the corresponding paintbox. Existence follows from the random labeling and de Finetti argument, not merely from verifying that the candidate construction is exchangeable.

\[ \mathcal L(\Pi\mid S)=Q_S,\qquad \mathcal L(\Pi)=\int Q_s\,\nu(ds),\quad \nu=\mathcal L(S). \]

Ranking, atomic masses and Qₛ must also be measurable. No mysterious measurable choice of atoms is needed: integrate the jth largest sample-partition frequency under the iid product kernel of μ. This is Borel and equals its jth largest atomic mass by the strong law. [T-PAINTBOX](../foundations/t-paintbox.md#paintbox-proof-representation) establishes this step and common null sets, then identifies the whole conditional law by cylinder uniqueness.

## 47.8 Why the ranked mixture is unique and discovery is size-biased

<a id="partitions-order"></a>

The strong law recovers every positive interval length in a fixed-s paintbox, so its ranked frequencies are s. Any mixture producing the same infinite partition law must therefore give the same distribution under the measurable ranked-frequency map. This proves uniqueness of the mixture, not of color names or interval locations.

The first individual enters block j with probability sⱼ, not uniformly among blocks. Without dust, successive new discoveries are likewise selected in proportion to remaining masses. This explains the difference between Chapter 44’s GEM discovery order and ranked masses: large blocks tend to appear early, but the first need not be largest. Ranking does not preserve independence of the original Beta stick fractions.

## 47.9 What the probability of a specified partition counts

<a id="partitions-eppf"></a>

For a specified partition of [n], exchangeability makes its probability depend symmetrically only on block sizes n₁,…,nₖ; call it p(n₁,…,nₖ), the EPPF. This is not the total probability of observing those sizes. Two specified partitions with identical sizes are still disjoint events, both of which must be counted for size-count distributions.

\[ p(n_1,\ldots,n_k)=\sum_{j=1}^k p(n_1,\ldots,n_j+1,\ldots,n_k)+p(n_1,\ldots,n_k,1). \]

The new label joins one old block or creates a new block, giving this recursion. Conversely a nonnegative symmetric p with p(1)=1 satisfying the recursion yields normalized consistent finite laws and hence an infinite exchangeable partition. An EPPF is both a probability reading and a consistency condition, not an arbitrary symmetric function.

## 47.10 How frequencies determine every finite sampling probability

<a id="partitions-sampling"></a>

Without dust, assign the k specified blocks to distinct positive-mass classes to obtain the formula below. The countable sum is nonnegative, justified by Tonelli or disjoint sampling events. Equality probabilities are powers and cross-powers of population masses, not functions of mean class count alone.

\[ p_s(n_1,\ldots,n_k)=\sum_{j_1,\ldots,j_k\ \mathrm{distinct}}s_{j_1}^{n_1}\cdots s_{j_k}^{n_k}\qquad\left(\sum_j s_j=1\right). \]

With dust, only specified singleton blocks can come from the remainder. Choose which singletons do so, contributing d each; the others still use distinct positive intervals. The [full formula](../foundations/t-paintbox.md#paintbox-proof-eppf) sums these finite choices. In particular, the probability that two individuals agree is always EΣSⱼ²: dust contributes no collision.

## 47.11 What the Ewens formula adds to the interpretation

<a id="partitions-ewens"></a>

Use θ>0 for Chapter 44’s concentration, keeping it distinct from the discount α below. That chapter proved the specified-partition probability θᵏ∏(nⱼ−1)! divided by the nth rising factorial of θ. We do not retell the restaurant story, but ask how the formula changes when only counts of each class size are retained.

Let Aⱼ count blocks of size j. For prescribed aⱼ, the number of label partitions is n! divided by the product of (j!) to power aⱼ and aⱼ!. These forget within-block order and the ordering of equal-sized blocks. Multiplying by the EPPF and canceling factorials gives the Ewens sampling formula.

\[ \mathbb P(A_j=a_j,1\le j\le n)=\frac{n!}{\theta^{\uparrow n}}\prod_{j=1}^n\frac{\theta^{a_j}}{j^{a_j}a_j!},\qquad \sum_j j a_j=n. \]

Paintbox gives this finite combinatorial formula a reverse interpretation as sampling from random masses. Rank Chapter 44’s GEM masses to obtain PD(0,θ), whose sum is one. Representation and uniqueness show that these ranked masses can be recovered from the infinite CRP partition, rather than being an extra guess. With atomic labels, different tables can share a name, and their observed equality partition need not obey this formula.

## 47.12 Which modified reinforcement rules remain exchangeable

<a id="partitions-two-parameter"></a>

Ordinary CRP weights an old block by its full size. Subtract the same α from each old block and transfer the total subtraction to the new-block weight: old weights nⱼ−α and new weight θ+αk still normalize. The real question is whether the probability of a complete history survives a change in customer order.

For 0≤α<1, with θ>0 when α=0 and θ>−α when α>0, the probabilities are legitimate. Multiplying a history, new-block factors depend only on the number of discovered blocks and old-block factors only on final sizes. The symmetric formula proves exchangeability; normalization alone cannot replace this step.

\[ p_{\alpha,\theta}(n_1,\ldots,n_k)=\frac{\prod_{i=1}^{k-1}(\theta+i\alpha)\prod_{j=1}^k(1-\alpha)^{\uparrow(n_j-1)}}{(\theta+1)^{\uparrow(n-1)}}. \]

This is a computable predictive family within the general paintbox structure, not a classification of every exchangeable partition. A legitimate but nonexchangeable sequential kernel appears in [T-PARTITION-PREDICTION](../foundations/t-partition-prediction.md#partition-proof-boundaries): making the third customer follow the first whenever the first two differ secretly retains names in the model.

## 47.13 Deleting a class changes the residual parameter

<a id="partitions-stick"></a>

With n₁ in the first block and r outside, avoiding it has weight θ+α+r. Conditional on avoidance, the residual restaurant has parameters (α,θ+α). Generate a two-color Pólya scheme with initial masses (1−α,θ+α), independently generate that residual restaurant, and interleave it at the blue positions. Equality of every finite path kernel proves the independence decomposition, rather than guessing it from marginals.

\[ V_j\sim\operatorname{Beta}(1-\alpha,\theta+j\alpha)\ \text{independently},\qquad P_j=V_j\prod_{i<j}(1-V_i),\quad \sum_jP_j=1\quad\text{a.s.} \]

Residual densities multiply by 1−Vⱼ, giving discovery-order masses. Total mass one still needs proof: for α>0, the means have divergent sum and second moments summable sum. Chapter 12’s centered-series criterion makes ΣVⱼ diverge; the residual product is bounded by exp(−ΣVⱼ) and vanishes. For α=0 use the strong law. The [companion proof](../foundations/t-partition-prediction.md#partition-proof-total-mass) gives the Beta calculations and parameter conditions. Ranking gives PD(α,θ), not independent Beta ranked coordinates.

## 47.14 The same symmetry does not specify the passage of time

<a id="partitions-dynamics"></a>

A static paintbox can remain unchanged forever, or its classes can begin to merge. Both processes start from the same exchangeable partition and have different futures. Even after choosing a merger rule, multiplying every rate by two preserves exchangeability while changing all waiting times. A static representation cannot determine these clocks.

We therefore propose an additional dynamics: each pair of current ancestral lineages merges at rate one. Time runs backward, and a class contains samples already sharing an ancestor at that depth. This is a mathematical model to study; exchangeability alone does not prove that real populations must follow it.

## 47.15 Finite samples allow an actual clock construction

<a id="partitions-finite-coalescent"></a>

Start from n singleton blocks. With b blocks, wait an exponential time of rate b(b−1)/2, then merge a uniformly selected pair. Use fresh independent variables; at most n−1 jumps prevent explosion. Exponential competition gives rate one per pair. We select current lineage blocks, not individuals weighted by the number of sample members in a block.

\[ L_nf(\pi)=\sum_{\{B,C\}\subseteq\pi}\left[f(\operatorname{merge}_{B,C}\pi)-f(\pi)\right]. \]

This defines the finite Kingman coalescent, whose relabeling invariance follows directly from construction. We still need to know whether chains for different n can be finite records of one infinite process. Invisible mergers are the obstacle to check.

## 47.16 Why deleting an individual does not spoil the clock

<a id="partitions-projection"></a>

Restrict a larger sample to [n]. Each visible block comes from one full block, so its merger with another visible block corresponds to exactly one full pair of rate one. A full block with no retained members can merge with visible blocks without changing the restriction. These invisible events must not be counted as extra restricted jumps.

\[ L_N(f\circ r_n)=(L_nf)\circ r_n,\qquad P_t^N(f\circ r_n)=(P_t^nf)\circ r_n. \]

The second finite-matrix identity follows by summing powers of the first. Conditioning on the full past and applying the tower property shows that the restriction itself is Markov with generator Lₙ, giving consistency at every set of times. Matching block counts at one time would not suffice. The [complete proof](../foundations/t-kingman-coalescent.md#kingman-proof-consistency) includes this step.

## 47.17 Infinite lineages without an infinitely fast total clock

<a id="partitions-infinite-process"></a>

Putting rate-one clocks on all pairs of infinitely many blocks gives infinite total rate and no ordinary next-jump waiting time at zero. Instead retain every finite restriction at rational times. These are countably many finite-valued random variables whose consistent records can be constructed on one space by Chapter 8.

Each finite record almost surely only coarsens, changes finitely many times and is right-continuous at rational points, all countable measurable conditions. On the common good set for all n, right rational limits recover restrictions at every real time. Coherence determines Π(t). The finite-restriction metric controls a finite head and then its tail, proving a càdlàg infinite-partition path starting from singletons.

This proves path existence, not just a naming of finite-dimensional distributions. [T-KINGMAN-COALESCENT](../foundations/t-kingman-coalescent.md#kingman-proof-path) specifies the good-record set, measurable extension, left limits and unique law, giving the dedicated path construction needed here.

## 47.18 Future coalescence acts on present blocks

<a id="partitions-coagulation"></a>

Enumerate the current blocks of π by least members. Independently draw a Kingman partition Ξ(t), and merge old blocks whose indices share a Ξ block. This is Coag(π,Ξ(t)). Testing finitely many original labels uses only finitely many block indices, so the operation is measurable and defines an infinite-state transition kernel.

Each finite restriction of this kernel is the finite chain already constructed. Finite semigroup identities and conditional expectations extend on cylinders to prove the Markov property. Remembering only the present means the present partition, not just its block count. Count alone is insufficient if we want to know who shares an ancestor with whom.

## 47.19 How infinitely many ancestors become finite at positive time

<a id="partitions-coming-down"></a>

Let Nₙ(t) count blocks among the first n labels and N(t)=supₙNₙ(t). The first time \(T_b^{(n)}\) with at most b blocks increases in n. Finite holding times at j blocks are independent Exp(j(j−1)/2), and the mean time from n to b telescopes.

\[ \mathbb ET_b^{(n)}=\sum_{j=b+1}^n\frac2{j(j-1)}=2\left(\frac1b-\frac1n\right),\qquad \mathbb ET_b=\frac2b. \]

Increase n and use monotone convergence to obtain \(T_b\), without first assuming an infinite jump chain. Since {N(t)>b}={\(T_b\)>t}, its probability is at most 2/(bt); letting b increase makes the block count finite at any t>0. Establish this simultaneously at rational times and extend to all positive times by monotone coalescence.

There are still infinitely many singletons at zero. Every fixed finite sample has a positive first waiting time, while larger samples reveal mergers at progressively finer early-time scales.

## 47.20 Why the descent speed is two divided by time

<a id="partitions-speed"></a>

Finiteness at positive time does not quantify the sharp initial descent. \(T_b\) has the law of an independent exponential tail, with variance at most C/b³ and mean 2/b. Deviations of \(bT_b\) along b=m² have summable probabilities. Borel–Cantelli gives limit two, and monotonicity fills the gaps between squares.

\[ bT_b\to2\quad\text{a.s.},\qquad T_{N(t)}\le t<T_{N(t)-1},\qquad tN(t)\to2\quad(t\downarrow0)\ \text{a.s.} \]

Right continuity at zero of every finite restriction makes N(t) tend to infinity as t decreases to zero, justifying the inversion. The constant depends on convention: pair rate c gives 2/c. This counts lineages near the time boundary, not categories as sample size grows in an Ewens model.

## 47.21 How dust can vanish without violating right continuity

<a id="partitions-time-frequencies"></a>

At each positive rational time, an exchangeable partition with finitely many blocks cannot have dust: its paintbox would otherwise generate infinitely many singletons. All frequencies are positive and sum to one. On one common good set at rational times, every later block is a finite union of old blocks, giving frequencies simultaneously at all positive times without intersecting uncountably many null sets.

\[ \sum_iS_i(t)=1\quad(t>0),\qquad \mathbb E\sum_iS_i(t)^2=1-e^{-t}. \]

The second identity uses only the two-label restriction, which merges at an Exp(1) time. The square of the largest mass is bounded by ΣSᵢ² and is monotone under mergers, so the largest mass tends to zero almost surely as t decreases to zero. Ranked frequencies tend coordinatewise to zero while their ℓ¹ total stays one. Finite samples, coordinatewise frequencies and total mass are different observations; conflating them creates the apparent paradox.

## 47.22 Merging masses is not sampling two individuals

<a id="partitions-mass-rates"></a>

The finitely many blocks at positive time can be described by masses. Merging sᵢ and sⱼ replaces them by sᵢ+sⱼ before reranking. Its rate remains one, not sᵢsⱼ. That latter factor arises from sampling individuals by population mass, a different experiment from choosing lineage pairs equally.

The independent Coag kernel shows that future mass mergers do not depend on old block names. On finite-block positive-time states, the mass process has the corresponding merger mechanism. This is a proved structural connection between static frequencies and dynamic partitions, not a proof that every mass-merger model is consistent under the same rate family.

## 47.23 Two matching probabilities can fail at three samples

<a id="partitions-not-ewens"></a>

In an unmutated Kingman process, the probabilities that two people remain different and three are all different at time t are e⁻ᵗ and e⁻³ᵗ. Under Ewens(θ), they are θ/(θ+1) and θ²/[(θ+1)(θ+2)]. Matching only two people might suggest a simple equivalence between t and θ.

Substituting e⁻ᵗ=θ/(θ+1), the three-person identity would require θ(θ+2)=(θ+1)², which is impossible. Exchangeability of both objects does not make them the same probability family. A connection between Ewens and genealogy requires an additional mechanism and proof.

## 47.24 Finding the first mutation along ancestral lines

<a id="partitions-mutation"></a>

Keep pair merger rate one and add an independent mutation clock of rate θ/2 to each active ancestral lineage. Tracing backward, freeze a lineage at its first mutation and assign its samples a new type; distinct mutations receive distinct types. These classes record nearest mutation, not common ancestry at an arbitrary time depth.

\[ q_b^{(\theta)}=\binom b2+\frac{b\theta}{2}=\frac{b(b-1+\theta)}2. \]

The next event among b active lineages is a merger or freezing. Each reduces the active count by one, so all n lineages are typed after n events. Equivalently place independent Poisson mutations on a finite Kingman tree, including an ancestral root branch beyond the last common ancestor; θ>0 guarantees a first backward mutation. Ignoring invisible events of already typed lineages yields the same finite generator. The [companion proof](../foundations/t-coalescent-mutation.md#mutation-proof-construction) checks this projection rather than relying on a biological picture.

## 47.25 How the first event forces the Ewens formula

<a id="partitions-mutation-proof"></a>

Fix a terminal allelic partition π. If i mutates first, it must be singleton in π; if i,j merge first, they must share a block in π. Deleting the frozen singleton or collapsing the pair leaves the same problem with n−1 lineages. For terminal probability u(π), event rates give the exact recursion.

\[ q_n^{(\theta)}u(\pi)=\frac\theta2\sum_{i:\{i\}\in\pi}u(\pi\setminus i)+\sum_{i<j:\ i\sim_\pi j}u(\pi^{ij}). \]

Insert the CRP Ewens candidate. Deleting a singleton gives probability ratio (θ+n−1)/θ; collapsing a pair in a block of size m gives (θ+n−1)/(m−1), with m(m−1)/2 choices. Singleton and nonsingleton member counts sum to n, so the total factor is n(θ+n−1)/2, exactly the left-side rate. The n=1 initial value agrees; induction identifies u with the Ewens EPPF.

Active/frozen generators are also consistent under restriction. Bounded convergence to finite terminal states gives a consistent infinite allelic partition. The same formula therefore means that two different constructions provably yield one static law, not that adding customers forward and merging ancestors backward have identical transition processes. With pair rate c and mutation rate μ per lineage, θ=2μ/c.

## 47.26 What finite samples can and cannot identify

<a id="partitions-information"></a>

Increasing observation recovers paintbox frequencies almost surely, but one fixed finite sample gives only one finite-pattern realization. All singletons do not prove pure dust, and a few large classes do not prove zero remaining mass. Different mass mixtures can agree on finite-order tests; all finite restrictions together determine the infinite law.

Likewise, an exchangeable partition at one time does not determine its future merger mechanism. Kingman specifies pair rates; mutation specifies additional type barriers. Multiple mergers, fragmentation and nested hierarchies require new consistency and path-construction proofs. Chapter 56 studies these more general merger, fragmentation and hierarchy constructions; they do not follow automatically from the binary-rate rule here.

## 47.27 Irrelevance of names does not eliminate structure

<a id="partitions-insight"></a>

Transitivity first forbade three relation entries from deciding independently, yet led from general relational representation to a unique mixture over ranked masses. Dust shows that aggregate mass cannot be imagined only class by class: mutually distinct singletons can occupy a positive proportion. Mathematics removes arbitrary naming, not classification itself.

When classes begin to merge, additional rate rules give time its meaning. Static representation, sample growth and backward genealogy can meet, but equality in law requires explicit mechanisms and proof. We can now ask not only whether a law is symmetric, but what it acts on, which information is shared, which observation scales recover it, and which separate rules are needed for evolution.

If the observed objects are instead random locations that actually appear in space, both how many and where become random outcomes. The partition theory suggests first identifying the object and its measurable observations before seeking a representation. The interaction between count and location requires another space.

## 47.28 Sources, complete proofs and scope

<a id="partitions-sources"></a>

Kingman’s [1978 paper](https://doi.org/10.1112/jlms/s2-18.2.374) studies representation of partition structures; the [1982 original The coalescent](https://www.ccg.unam.mx/~vinuesa/tlem/pdfs/Kingman_1982_Coalescent.pdf) starts from finite-sample merger chains and their infinite embedding. Ewens’s [1972 original](https://doi.org/10.1016/0040-5809(72)90035-4) studies neutral allelic sampling. These are not three names for one discovery at one time. Organizing them through equivalence relations is a modern reconstruction.

Pitman’s [author-hosted lectures](https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/pitman_CSP.pdf) provide a reference for predictive and two-parameter structures. This chapter supplies its own deletion, Beta-factor and residual-mass arguments rather than treating a link as proof. Full companions are [T-PAINTBOX](../foundations/t-paintbox.md), [T-PARTITION-PREDICTION](../foundations/t-partition-prediction.md), [T-KINGMAN-COALESCENT](../foundations/t-kingman-coalescent.md) and [T-COALESCENT-MUTATION](../foundations/t-coalescent-mutation.md).

The actual scope is infinite exchangeable partitions of N, the stated one- and two-parameter predictive families, binary Kingman coalescence and independent infinitely-many-alleles mutation. General Λ/Ξ mergers, fragmentation hierarchies and finite-population limits are not proved by these results. Equality partitions with atomic labels, ranking versus discovery order, dust versus positive-frequency blocks, and static law versus time evolution remain distinct.
