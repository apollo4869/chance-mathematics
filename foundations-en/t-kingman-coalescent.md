# T-KINGMAN-COALESCENT: Finite Mergers, Infinite Paths and Coming Down

Every pair of current blocks merges at rate one, with time increasing toward common ancestry. This is the dedicated Kingman construction, not an invocation of Chapter 56’s general coalescent theory. Return to [Chapter 47](../chapters/47-partitions.md#partitions-infinite-process).

## 1. Finite-sample paths and their generator

<a id="kingman-proof-finite"></a>

From π∈Pₙ with b blocks, wait Exp(\(q_b\)), \(q_b\)=b(b−1)/2, then merge a uniformly chosen unordered pair; b=1 is absorbing. Use fresh independent exponentials and choices at each step. There are at most n−1 jumps, so no explosion. Exponential competition from Chapter 21, or the direct holding density, gives rate one per specified pair and the generator below. Relabeling preserves the pair set, so the entire path law is exchangeable.

\[ L_n f(\pi)=\sum_{\{B,C\}\subseteq\pi}\big[f(\operatorname{merge}_{B,C}\pi)-f(\pi)\big],\qquad q_b=\binom b2. \]

The next jump choice is independent of its holding time, and \(q_b\) depends only on block count, not masses or sizes. Indexing the fresh exponentials by the successive counts shows that the time from n blocks to b has the law of a sum of independent variables. These auxiliary exponentials for different n need not be identified with the actual holding times in a previously chosen restriction coupling.

## 2. Deleting samples preserves visible merger rates

<a id="kingman-proof-consistency"></a>

For N≥n let R restrict \(\mathcal P_N\) to [n]. Every restricted block corresponds to one full block. Two visible blocks merge only when their two full blocks merge, still at rate one. A merger involving an empty projected block does not change the restriction. This gives the pointwise identity below for every f.

\[ L_N(f\circ R)=(L_nf)\circ R,\qquad P_t^N(f\circ R)=(P_t^nf)\circ R. \]

The second identity follows, rather than being assumed: induct on matrix powers and sum the absolutely convergent exponential series. Conditional on the full past, a future restricted observation has conditional expectation \(P_t^nf\) of the current restriction. The tower property gives the restricted Markov property. Iterated conditioning proves consistency of all finite-time laws, and thus rational-time path laws, not merely one-time marginals.

## 3. One infinite probability space from rational times

<a id="kingman-proof-path"></a>

Record the nth finite chain at nonnegative rational times, a standard Borel countable product of finite spaces. The preceding section gives consistency in n. Chapter 8 constructs all (n,q) records on one countable product probability space. The restriction identities hold simultaneously for countably many n,q. Path properties must still be checked; finite-dimensional distributions do not replace that step.

For fixed n, good records satisfy three countable Borel conditions: partitions only coarsen as rational time increases; time zero is the singleton partition; and each rational q has a rational r>q on which all rational values in [q,r) equal the value at q. The finite chain satisfies them almost surely. Coarsening allows at most n−1 genuine changes on the whole time axis. On the common good set for every n, define the value at real t as the eventual value along rationals decreasing to t. Finitely many states and changes give existence; rational right continuity recovers the recorded values. Left limits also exist. Complete bad records by a fixed constant path.

The rational restriction identities extend to every real t by right limits. They determine a unique Π(t)∈P∞. Use the metric d(π,ρ)=Σ2⁻ⁿ1{rₙπ≠rₙρ}. Control right continuity or left limits in a finite head, then make the tail sum smaller than any ε. Thus Π is càdlàg in this compact metrizable space, starting from the singleton partition. Measurability follows from finite coordinates and rational right limits.

## 4. The infinite Markov kernel and coagulation

<a id="kingman-proof-markov"></a>

Enumerate the blocks of π by least member. Independently take a Kingman partition Ξ(t) starting from singletons, and merge π blocks whose indices lie in one Ξ block, writing Coag(π,Ξ(t)). To test connectivity of two labels, only a finite prefix of π is needed to determine their block indices, followed by a finite restriction of Ξ. Hence Coag is measurable and its law \(K_t(\pi,\cdot)\) is a kernel. Its nth restriction is exactly the finite coalescent started from rₙπ.

The finite semigroup identity extends on cylinders to \(K_sK_t=K_{s+t}\). For the constructed Π, Markov identities against finite past cylinders follow from finite chains and extend by monotone classes to the whole past field and all bounded Borel tests. Thus \(K_t\) really is the transition kernel. Finite relabeling invariance likewise extends to the entire path law. No undefined total exponential clock is installed on infinitely many blocks.

## 5. The exact time calculation for coming down

<a id="kingman-proof-coming-down"></a>

Let Nₙ(t) count blocks among the first n labels, N(t)=supₙNₙ(t), and \(T_b^{(n)}\) be the first time with at most b blocks. Restriction coupling makes both Nₙ and \(T_b^{(n)}\) increasing in n; define \(T_b\) by their limit. The finite construction gives the following law and expectation. Here b≥1 and the independent Eⱼ have rates qⱼ.

\[ T_b^{(n)}\stackrel d=\sum_{j=b+1}^n E_j,\quad E_j\sim\operatorname{Exp}\!\binom j2,\qquad \mathbb ET_b^{(n)}=2\left(\frac1b-\frac1n\right),\quad \mathbb ET_b=\frac2b. \]

The final step is nonnegative monotone convergence, not an assumption that an infinite jump chain already exists. Since {N(t)>b}={\(T_b\)>t}, Markov’s inequality gives P(N(t)>b)≤2/(bt). Let b increase to obtain finitely many blocks at each fixed positive time. Intersect first over positive rational times, then use coarsening for all t>0 simultaneously. Also T₁ has mean two, so all lineages eventually merge into one at a finite time.

For the variance, construct the partial sums using one independent sequence Eⱼ on an auxiliary space. The tail has finite mean and summable variances, giving L² convergence. Its limiting law is uniquely the distributional limit of \(T_b^{(n)}\). Thus \(T_b\) has this tail-sum law and the stated mean and variance, without assuming independence across n of actual holding times in the restriction coupling.

## 6. The speed constant two and the direction of the limit

<a id="kingman-proof-speed"></a>

\[ \operatorname{Var}(T_b)=\sum_{j>b}\frac4{j^2(j-1)^2}\le\frac C{b^3},\qquad bT_b\longrightarrow2\quad\text{a.s.},\qquad T_{N(t)}\le t<T_{N(t)-1},\qquad tN(t)\longrightarrow2\quad(t\downarrow0)\ \text{a.s.} \]

The variance bound gives P(|\(bT_b\)−2|>ε)≤C/(ε²b). Along b=m² this is summable, so Borel–Cantelli gives convergence. Monotonicity of \(T_b\) and the ratio of consecutive squares tending to one extend it to every integer b. As t decreases to zero, N(t) tends to infinity: each finite restriction has not yet made its first jump sufficiently near zero, so N(t)≥n for any fixed n. The inequalities \(T_{N(t)}\le t<T_{N(t)-1}\), with the right subscript meaning N(t) minus one, then squeeze tN(t) to two.

Coming down does not mean a single jump at zero merging infinitely many blocks. Every finite restriction is right-continuous at zero; mergers on successively finer finite scales make the block count finite at positive times. If each pair’s rate is c>0, times are divided by c and the speed is tN(t)→2/c. The constant two must not be copied across rate conventions.

## 7. Frequencies simultaneously at every positive time

<a id="kingman-proof-frequencies"></a>

At each fixed positive rational q, Π(q) is exchangeable with finitely many blocks. T-PAINTBOX says zero-frequency blocks are singleton; positive dust mass would produce infinitely many such singletons by conditional independent sampling, a contradiction. Thus there is no dust, all block frequencies are positive and sum to one. Intersect over positive rational q.

For any t>0 choose rational q<t. There are finitely many blocks at q, and every later block is a finite union of them, so its frequency exists as the corresponding finite sum. This works for every t on the same set, without an uncountable intersection. Ranked S(t) is an ℓ¹-valued càdlàg step path with finitely many mergers on each [ε,∞). At zero all frequencies are zero and dust mass is one.

\[ \mathbb E\sum_i S_i(t)^2=\mathbb P\{1\sim_{\Pi(t)}2\}=1-e^{-t}. \]

The first identity is paintbox sampling; the second is the two-label Exp(1) merger time. The square of the largest frequency is at most ΣSᵢ², and the largest frequency increases under mergers. Its monotone limit as t decreases to zero is almost surely zero, since its expected square is bounded by 1−e⁻ᵗ. Thus S(t) tends coordinatewise to zero while its ℓ¹ norm stays one. Instantaneous dust loss and right continuity of finite restrictions concern different observation scales.

## 8. Mass-merger rules and actual scope

<a id="kingman-proof-scope"></a>

At positive times there are finitely many lineages, and each pair merges at rate one, replacing its masses by their sum before reranking. Sampling two individuals instead produces weights involving SᵢSⱼ, a different rule. The independent Coag kernel shows that future masses depend only on current masses: each pair uses the same rate, with no reference to old block names or contents. This generator description is asserted on the finite-block positive-time states.

This proves the binary, per-pair-rate-one Kingman model and its dedicated limits. It does not classify Λ/Ξ multiple or simultaneous mergers, general fragmentation dualities, CRT genealogical limits or nonexchangeable mechanisms. Those changes require more than replacing a symbol in these formulas; Chapter 56 carries their additional consistency and construction requirements.
