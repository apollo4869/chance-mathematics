# T-COALESCENT-MUTATION: How a Mutation Model Actually Produces Ewens

Fix rate one per pair of active Kingman lineages, and mutation rate θ/2 per active lineage, with θ>0. Infinitely many alleles means distinct mutations create distinct types, not labels that can collide in a finite type set. Return to [Chapter 47](../chapters/47-partitions.md#partitions-mutation).

## 1. An unmutated fixed-time coalescent is not Ewens

<a id="mutation-proof-counterexample"></a>

Without mutation, the probabilities that two labels are still distinct at t and that three are all distinct are e⁻ᵗ and e⁻³ᵗ. Under Ewens(θ) they are θ/(θ+1) and θ²/[(θ+1)(θ+2)]. Matching the two-label probabilities forces e⁻ᵗ=θ/(θ+1), but matching three would then require θ(θ+2)=(θ+1)², an impossibility differing by one.

Thus no deterministic time turns all finite restrictions of the unmutated Kingman process into one Ewens family. We now add an explicit random mechanism and prove that its terminal allelic partition does have Ewens law.

## 2. Freeze a lineage at its first backward mutation

<a id="mutation-proof-construction"></a>

A finite-sample state consists of disjoint active blocks and frozen allelic blocks, together partitioning [n]. Each active pair merges at rate one; each active block freezes at rate θ/2 and receives a previously unused type. Frozen blocks do not participate in active mergers or merge with one another. Independent exponentials construct all holding times and choices.

\[ q_b^{(\theta)}=\binom b2+\frac{b\theta}{2}=\frac{b(b-1+\theta)}2,\qquad b\ge1. \]

Each event reduces the active count by one, so after exactly n events no active blocks remain. Every holding time is finite, including the final rate θ/2 at b=1, and the terminal partition exists at a finite time. For θ=0 the last lineage never freezes; that degenerate case is not inserted into this θ>0 argument.

The same model has an explicit realization on a finite Kingman genealogy. Put independent rate θ/2 Poisson clocks on its finitely many branches, and append an infinite ancestral root branch beyond the last common ancestor. Chapter 21 makes the first mutation on that branch finite. A sampled lineage’s first backward mutation determines its type; different mutation points have different types.

More precisely augment the state to an ancestral partition R, active groups A of not-yet-typed samples, and frozen groups D. Each R block contains at most one A block. Each pair of R blocks merges at rate one: merge their two A blocks if both are present, or retain the single A block if only one is present, leaving D unchanged. Each R block containing an A block freezes that A block into D at rate θ/2 without changing R. This is a finite state space, so independent exponentials construct its chain. Under projection (R,A,D) to (A,D), each active pair corresponds to exactly one R pair and has rate one; each active group freezes at rate θ/2; other R mergers are invisible. Thus generator intertwining holds state by state, and finite matrix exponentiation proves the full projected Markov law. This justifies discarding already typed ancestral groups.

Why may typed lineages be discarded? Mark as active those sample groups whose first mutation has not yet been found. Active-active pairs still merge at rate one. A merger with an inactive lineage changes no active sample set, merely continuing its unresolved ancestral line; independent increments and exponential memorylessness leave mutation along the continuation at rate θ/2. Ignoring invisible events gives exactly the stated finite generator. The generator-intertwining and exponential-series argument of T-KINGMAN-COALESCENT Section 2 proves equality of the whole projected process. Freezing does not identify an allele across an intervening mutation with its older ancestral type.

## 3. Restriction consistency of paths and terminal partitions

<a id="mutation-proof-consistency"></a>

Restrict active and frozen blocks to [n] and discard empty blocks. Each visible active block corresponds to one full active block and still mutates at rate θ/2; each visible active pair still merges at rate one. Mergers with invisible active blocks and mutations of invisible blocks add no visible transition. Hence generators intertwine under restriction, and the finite-matrix argument gives consistency of all finite-time laws.

Each finite system reaches an absorbing terminal state at a finite time. Bounded convergence of finite-state indicators as deterministic t tends to infinity extends restriction consistency to terminal laws. These are therefore sampling-consistent for all n, and the countable restriction construction gives a unique infinite exchangeable terminal partition. This does not require all infinitely many sampled lineages to freeze by one common finite time; the proof concerns every finite restriction and their consistency.

## 4. The first-event recursion and what each term means

<a id="mutation-proof-recursion"></a>

Let u(π) be the probability of a specified terminal allelic partition π starting from n active singleton lineages. If i freezes first, it must be singleton in π, since that type cannot reappear; deletion leaves the same model with n−1 lineages. If i,j merge first, they must share a block in π; collapsing them to a composite label again leaves n−1 lineages. Rates depend on lineages, not on how many original samples a composite label contains.

\[ q_n^{(\theta)}u(\pi)=\frac\theta2\sum_{i:\{i\}\in\pi}u(\pi\setminus i)+\sum_{\substack{i<j\\i\sim_\pi j}}u(\pi^{ij}),\qquad u(\{\{1\}\})=1. \]

Every term on the right has fewer labels, so the recursion uniquely determines u. A pair merged at the first event cannot later be assigned different terminal alleles: after merging they share the same unresolved lineage and therefore the same nearest mutation.

## 5. Checking Ewens factor by factor

<a id="mutation-proof-ewens"></a>

Substitute the candidate u=θᵏ∏(nⱼ−1)! divided by the nth rising factorial of θ. Deleting a singleton gives ratio (θ+n−1)/θ; collapsing a pair in a block of size m≥2 gives ratio (θ+n−1)/(m−1). In the recursion each singleton contributes u times (θ+n−1)/2. A block of size m has m(m−1)/2 pairs, contributing u times m(θ+n−1)/2.

\[ \frac{\theta+n-1}{2}\left(\#\{\text{singleton blocks}\}+\sum_{j:n_j\ge2}n_j\right)=\frac{n(\theta+n-1)}2=q_n^{(\theta)}. \]

The n=1 initial value agrees, so induction proves the candidate is the terminal probability. Counting partitions by size then gives the Ewens sampling formula in T-PARTITION-PREDICTION Section 2. Thus CRP growth and backward coalescence with mutation yield the same static terminal law, not the same time-parameterized path process: their path spaces and transition mechanisms differ.

## 6. Scope and rate conventions

<a id="mutation-proof-scope"></a>

With pair rate c>0 and lineage mutation rate μ>0, rescale time by c to obtain θ=2μ/c. The Ewens parameter is a ratio of rates, not an arbitrary observation time. No mutation and the finite-sampling limit θ decreasing to zero both lead to one eventual type, but neither is literally the θ>0 first-mutation construction.

This does not prove a finite-population scaling limit to Kingman, nor include selection, recombination, finite-type collisions or multiple mergers. Those changes alter states, rates or identification rules; Ewens cannot be used to infer that they preserve the law. The mathematics applies to the declared neutral binary-merger model with independent infinitely-many-alleles mutations.
