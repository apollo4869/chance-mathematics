# Regeneration Clocks, Successful Coupling and Total Variation Limits

## 1. A countable-chain lemma without a mixing theorem

<a id="convergence-countable"></a>

Let Q be an irreducible countable chain with invariant probability ρ. Every \(\rho _i\)>0, since a positive-probability path from a positive-mass state transmits positive mass by invariance. On stationary paths, Poincaré recurrence of {X₀=i} gives infinitely many returns under \(P_i\). Repeatedly trying a fixed path from i to j at returns to i, using strong Markov and a geometric failure bound, gives hitting probability one. Thus every state is recurrent.

The mean return time can also be identified without convergence. Construct the two-sided stationary chain by consistent finite-dimensional laws. Its reverse kernel \(\rho _j\)\(Q_{ji}\)/\(\rho _i\) is irreducible and preserves ρ. Applying the same argument backwards ensures a most recent visit to i. Partition by that visit occurring at −n. Nonnegative summation gives the following identity, and summing over j yields \(E_i\)\(\tau _i\)⁺=1/\(\rho _i\).

\[ \rho_j=\rho_i E_i\sum_{n=0}^{\tau_i^+-1}\mathbf1_{\{X_n=j\}},\qquad E_i\tau_i^+=\frac1{\rho_i}. \]

Without irreducibility this conclusion cannot cross closed classes. The lemma will be used only for the explicitly countable clock chain below; it does not assume general Harris convergence.

## 2. How two regeneration clocks meet

<a id="convergence-clocks"></a>

Let L be a positive integer cycle length with μ=EL<∞ and gcd{l:P(L=l)>0}=1. Define the residual clock Z: from j≥1 move to j−1, and at zero independently draw L and move to L−1. Its state space is S={j≥0:P(L>j)>0}. Coordinate calculation gives the invariant probability \(\rho _j\)=P(L>j)/μ. The entries sum to one, every j reaches zero, and zero reaches every j.

The product of two independent clocks preserves ρ⊗ρ. Its irreducibility requires aperiodicity. Loops at zero have lengths given by sums of support values of L. A finite subset already has gcd one. Modulo one such value a, nonnegative combinations form a subgroup of the finite residue group and reach every residue. Choose a nonnegative representative of each residue and add multiples of a; all sufficiently large integers are loop lengths. Adding fixed entrance and exit paths gives positive transition probabilities for every sufficiently large time between each pair of states. Thus the product is irreducible.

By the preceding lemma the product hits (0,0) almost surely from every residual pair. For random initial delays, condition on each pair and integrate; finite expected delay is unnecessary. This argument uses neither the desired total variation theorem nor an unproved renewal theorem.

## 3. Turning clock coupling into path coupling

<a id="convergence-marks"></a>

First draw the two initial delays. Run the two residual clocks independently until their first common regeneration T, then use shared cycles. A preselected cycle length must not be declared independent of its starting state. Instead, for each completed length l sample its entire half-open mark from the conditional mark kernel given that length. The mark includes its start but excludes its endpoint, so adjoining marks do not impose conflicting values on an overlapping coordinate.

Clock generation before T uses only previously drawn lengths, and T is a stopping time for these clocks. No cycle beginning at T has been drawn. Its new state can therefore be an independent ν-state shared by both paths, followed by common P-randomization. In either marginal, the lengths and conditional marks reassemble exactly the original iid cycle law. The initial prefix is sampled from its conditional law given its delay. Standard Borel disintegration supplies measurable kernels.

This couples full path laws; it need not be Markovian in the pair of current states. After T the paths agree at equal times. Apply it to an x-start and a π-start, whose regeneration delays are both finite, to obtain the main conclusion.

\[ d_{\rm TV}(P^n(x,\cdot),\pi)\le \mathbb P_{x,\pi}(T>n)\longrightarrow0. \]

If cycle span is d>1 the clock phases may never meet, so the condition is essential. For any initial probability η, pointwise convergence and bounded convergence imply ηPⁿ→π, without a moment assumption on η.

## 4. From marginal forgetting to mixing of stationary records

<a id="convergence-mixing"></a>

On the two-sided π-stationary P-chain, the conditional future given the past through zero depends only on X₀. The entire path from n onwards is a probability kernel from \(X_n\). Kernel contraction gives the bound below. Prove the Markov conditional identity first for finite cylinders and extend by a monotone class. Countable generation represents the total variation supremum by a countable determining algebra, ensuring measurability.

\[ \sup_{\substack{A\in\sigma(X_j:j\le0)\\B\in\sigma(X_j:j\ge n)}}|\mathbb P_\pi(A\cap B)-\mathbb P_\pi(A)\mathbb P_\pi(B)|\le\int \pi(dx)\,d_{\rm TV}(P^n(x,\cdot),\pi)\longrightarrow0. \]

This gives strong mixing and ergodicity, without a uniform rate. Approximate a shift-invariant event A by a finite cylinder D in L¹ and translate D far away. Mixing then yields P(A)=P(A)². This is the actual implication to a trivial invariant σ-field. Its converse fails, as the two-point exchange in Chapter41 shows.

## 5. Multistep small sets and scope

<a id="convergence-skeleton"></a>

If a specified m≥1 makes Q=Pᵐ satisfy all regenerative assumptions, finite mean cycles and span one, then Q has a unique invariant probability π. Since πP is also Q-invariant, uniqueness gives πP=π. Write n=mk+r; contraction gives Pⁿ(x,·)→π. A Q-cycle lasts mL original steps, but that does not mean P has period m; the residual r is handled by πP=π.

To restore the intermediate m−1 states, disintegrate the finite P-bridge given its endpoints using Chapter10, then fill it in. After matching endpoints use shared P evolution. This disintegrates paths and skeleton records under a specified initial law, without assuming a common version for arbitrary bridge parameters. Multistep minorization does not license ignoring intermediate paths.

This proves Harris convergence under explicit regenerative conditions and the specified skeleton extension. It does not count the general reduction of an arbitrary abstract aperiodic Harris kernel to the all-start recurrent skeleton needed here as proved. That is a separate measurable-space structure theorem, not a consequence of a definition or a link. Return to [Chapter42](../chapters/42-harris-coupling.md#harris-convergence).
