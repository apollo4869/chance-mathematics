# T-HOMOGENEOUS-FRAGMENTATION: General Dislocation Measures, Erosion, Joint Frequencies and a Tagged Block

This page constructs the homogeneous process in [Chapter 56](../chapters/56-fragmentation-hierarchies.md#fragment-dislocation). It uses Chapter 47’s Borel paintbox kernel, Chapter 48’s Poisson random measures, exponential waits from Chapter 21, finite matrices from Chapter 22 and de Finetti from Chapter 43. The tagged-block subordinator uses only the nonnegative Poisson jump sum already constructed in Chapter 27, not a later fragmentation result.

## 1. Parameters and integrability

<a id="homfrag-parameters"></a>

\[ \mathcal S^\downarrow=\{s_1\ge s_2\ge\cdots\ge0:
\sum_i s_i\le1\},\quad
\mathbf1=(1,0,\ldots),\qquad
c\ge0,\quad\nu\{\mathbf1\}=0,\quad
\int(1-s_1)\nu(ds)<\infty. \]

Let ν be a Borel measure on S↓ with its coordinate topology; it need not be finite. Let PBₛ be the dust-allowing paintbox kernel of Chapter 47, and let εᵢ isolate i while keeping all other integers together. Define the partition dislocation measure κ.

\[ \kappa(d\pi)=\int PB_s(d\pi)\nu(ds)
+c\sum_{i\ge1}\delta_{\varepsilon_i}(d\pi).
\qquad
\lambda_m=mc+\int\left(1-\sum_i s_i^m\right)\nu(ds)
\quad(m\ge2). \]

The partition space P∞ with its finite-restriction metric is compact Polish. After deleting the trivial partition 1, Bₘ={π:π|[m] is nontrivial} is an increasing compact-open exhaustion. Its κ-mass is λₘ: m samples all belong to one block with probability Σsᵢᵐ. All m visible erosion isolations count; for m=2 the same final partition has two contributions, giving 2c. For m=1 the effective rate is 0 and that formula must not be used. Since 1−Σsᵢᵐ≤1−s₁ᵐ≤m(1−s₁), λₘ is finite. Thus κ is locally finite Radon on P∞∖{1}, allowing Chapter 48’s Poisson construction.

## 2. One Poisson space supports all finite restrictions

<a id="homfrag-poisson"></a>

\[ N(dt,d\pi,dk),\qquad
E N=dt\,\kappa(d\pi)\,\#(dk),\qquad k\in\mathbb N. \]

Order blocks by least member. At an atom (t,π,k), enumerate the current k-th block increasingly, apply π to those ranks and map back, discarding empty intersections. Infinitely many ineffective atoms cannot be run by a global “next jump” algorithm. On [n], only atoms with k≤n and π∈Bₙ can matter. There are finitely many on bounded time intervals, so a chronological recursion defines the finite path. Each effective change increases block count, giving at most n−1 changes.

These recursions are pathwise compatible. Every global block meeting [n] precedes every invisible block, and its members in [n] form an initial segment of its increasing enumeration. Both block rank and internal rank agree with the finite restriction. Atoms acting only on invisible blocks do not affect visible ordering. Thus all finite paths project exactly on one good set, not merely in marginal law. They determine a unique infinite partition path. Finite restrictions are right-continuous with left limits, and so is the inverse-limit path: its tail-coordinate error is bounded by 2⁻ⁿ.

## 3. Generators, exchangeability and branching Markov structure

<a id="homfrag-generator"></a>

\[ L_n f(\eta)=
\sum_{\substack{B\in\eta\\|B|\ge2}}
\int\{f(\operatorname{Frag}_{B,\pi}\eta)-f(\eta)\}\kappa(d\pi).
\qquad L_N(f\circ r_n)=(L_nf)\circ r_n . \]

The integral is nonzero only on finite-rate effective events. κ is invariant under finite permutations, making the finite generator covariant under relabeling. The matrix-exponential power series turns generator intertwining into semigroup intertwining; repeated conditioning gives path exchangeability and consistency. Generator terms for distinct current blocks act on distinct coordinates. Uniqueness of the finite product chain proves conditional independence of their future fragmentation, each following the original rule. Extend to infinitely many blocks by finite-cylinder uniqueness. Least-member numbering introduces no physical preference.

The semigroup preserves cylinder functions and is continuous at time 0 on them by finite matrices. Cylinder functions uniformly approximate continuous functions on the compact state space, so the semigroup is Feller and strongly continuous. Approximate a finite stopping time from above by grid times. Right continuity of finite restrictions and continuity of cylinder semigroups permit bounded convergence of the deterministic-time Markov identity. Localize stopping times and extend cylinders afterwards. This proves the process’s strong Markov property without future tree theory.

## 4. Frequencies simultaneously for all times

<a id="homfrag-frequencies"></a>

Fix i and let τᵢⱼ be the first separation time of i,j, possibly infinite. Refinement gives j∈Bᵢ(t) exactly when τᵢⱼ>t. With i fixed, the other separation times form an exchangeable sequence. Chapter 43 gives a conditionally iid directing probability Mᵢ on [0,∞]. Its empirical tails converge uniformly, not just pointwise. To prove this auxiliary fact, isolate finitely many large atoms and choose a finite quantile grid in the remainder with interval masses below ε. Condition on M and apply the strong law to both open and closed tails at grid endpoints and to isolated atoms; quantiles are measurably chosen from evaluations of M. Monotonicity sandwiches any threshold between adjacent endpoints, bounding the supremum error by 2ε plus a vanishing term. Take ε=1/k for a common good set.

\[ |B_i(t)|=\lim_{n\to\infty}
\frac{\#(B_i(t)\cap[n])}{n}
=M_i((t,\infty]),\qquad \text{all }i,\ t\ge0\quad\text{a.s.} \]

Thus every tagged-block mass path is simultaneously nonincreasing, right-continuous and has left limits. Chapter 47 makes zero-frequency blocks singletons at all rational times. If a zero-frequency block contained i,j at a real time, right continuity would keep them together at a later rational time, while nonincreasing mass would still be zero, a contradiction. This holds for all times simultaneously. Frequencies are Borel limits of finite counts; no uncountable union of null sets was taken.

## 5. Process versions of ranked and total mass

<a id="homfrag-mass-paths"></a>

Enumerate blocks by least member and rank their frequencies to obtain X(t)∈S↓. Measurability follows by finite maximum sums and countable suprema. Let Aₖ(t) be the sum of the k largest masses. Any k descendant blocks have at most k ancestors, so Aₖ is nonincreasing. Select a label from each of the k largest positive blocks at t. They stay distinct to the right and their tagged masses are right-continuous, so Aₖ(t+)≥Aₖ(t); hence equality. Therefore Xₖ=Aₖ−Aₖ₋₁ has right-continuity and left limits. The process is càdlàg in the coordinate topology; ℓ¹-càdlàg behavior has not been inferred.

Total mass S(t)=ΣXⱼ(t) also has a legitimate version. Put ζᵢ=supⱼ≠ᵢτᵢⱼ, the time label i becomes a singleton. This sequence is exchangeable, and uniform empirical-tail convergence gives V(t)=limₙ n⁻¹Σᵢ≤ₙ1{ζᵢ>t}, simultaneously for all t, with V right-continuous. At rational t paintbox gives V(t)=S(t). At any t positive blocks are contained in the nonsingleton labels, so S(t)≤V(t). Conversely S is nonincreasing; rational q↓t give S(t)≥lim V(q)=V(t). Hence S=V simultaneously, with dust 1−S.

## 6. The tagged block and a killed subordinator

<a id="homfrag-tag"></a>

\[ \begin{aligned}
\Phi(q)&=c(q+1)+\int\left(1-\sum_i s_i^{q+1}\right)\nu(ds)
\quad(q>0),\\
k&=c+\int\left(1-\sum_i s_i\right)\nu(ds),\\
\Pi(dy)&=\int\sum_{i:s_i>0}s_i\,\delta_{-\log s_i}(dy)\nu(ds)
\quad(y>0).
\end{aligned} \]

The killing rate k is finite and ∫(1∧y)Π(dy)≤2∫(1−s₁)ν: the largest part satisfies −s₁log s₁≤1−s₁, while all remaining weights sum to at most 1−s₁. Chapter 27 constructs ξ with drift c, jump measure Π and an independent killing time of rate k. After killing set ξ=∞ and e⁻∞=0. The Poisson functional gives E e⁻ᑫξₜ=exp(−tΦ(q)), since k+cq+∫(1−e⁻ᑫʸ)Π=Φ(q). Erosion contributes both drift c and killing rate c; neither may be omitted.

Identify this auxiliary process with the actual tagged block rather than asserting it heuristically. For integer q≥1, E|B₁(t)|ᑫ equals the probability that q+1 specified labels have stayed together: de Finetti fixing label 1 makes the other membership indicators conditionally iid. Before separation the effective rate is λ for q+1 labels, so the probability is exp(−tΦ(q)). Together with the constant moment, Chapter 13’s Bernstein uniqueness identifies the [0,1] mass law as e⁻ξₜ. Conditional on a positive-mass block, its independent internal future has the same tagged law, and relative child frequency multiplies parent frequency by the strong law along its increasing enumeration. Repeated conditioning identifies all time joint laws. Both paths are càdlàg, so their process laws agree.

## 7. Conservation criterion and mass observables

<a id="homfrag-conservation"></a>

\[ E\sum_iX_i(t)^{q+1}=e^{-t\Phi(q)}\quad(q>0),
\qquad ES(t)=e^{-kt}.
\qquad
S(t)=1\ \text{for all }t\ge0\ \text{a.s.}
\ \Longleftrightarrow\ k=0. \]

The first identity follows from size-biased paintbox sampling. Let q decrease to zero and use monotone convergence for total mass. If k=0, every rational-time S lies in [0,1] with expectation 1 and hence equals 1; monotonicity extends to all times. The reverse follows from expectations. Nonnegativity makes k=0 equivalent to c=0 and Σsᵢ=1 for ν-almost every s. This is an exact criterion for homogeneous fragmentation, not an unproved criterion for negative-index self-similar processes.

\[ F_q(x)=\sum_i x_i^{q+1},\qquad
P_tF_q(x)=e^{-t\Phi(q)}F_q(x),\qquad
\left.\frac{d}{dt}P_tF_q(x)\right|_{t=0}
=-\Phi(q)F_q(x). \]

Independent blocks, nonnegative sums and Tonelli give the semigroup identity for any initial mass vector x. This is a pointwise generator relation for the specified observable, not a derivative assertion for arbitrary functions on the state space. Pure erosion ν=0 gives X(t)=(e⁻ᶜᵗ,0,…) and dust 1−e⁻ᶜᵗ. A tag survives with probability e⁻ᶜᵗ; conditional on survival its block has mass e⁻ᶜᵗ as well. Its q-th mass moment is e⁻ᶜ⁽ᑫ⁺¹⁾ᵗ, checking both c contributions.

## 8. Parameter identification and the unproved inverse classification

<a id="homfrag-scope"></a>

The finite effective transition rates identify κ, since they specify jump measures on finite cylinders and Bₙ exhaust the space with finite measure. Moreover c=κ{ε₁}: paintboxes from nontrivial ν almost surely do not have frequencies (1,0,…). Push ranked frequencies forward on the finite-measure event that labels 1,2 are separated. Away from the erosion atom at frequency 1, this gives (1−Σsᵢ²)ν(ds). That weight is positive for s≠1, recovering ν. This proves uniqueness of the constructed characteristics, not the inverse decomposition theorem for every abstract exchangeable splitting measure.

The full inverse classification of homogeneous fragmentations and general infinite-ν self-similar stopping-line constructions remain unproved here. Within the stated ν,c range, existence, path consistency, Markov branching, simultaneous frequencies, the tagged block and conservation criterion have actual working proofs above. Return to the [main text](../chapters/56-fragmentation-hierarchies.md#fragment-tag).
