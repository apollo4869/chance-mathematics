# Chapter 44: Why Do Dependent Samples Look Like Repeated Predictions? — Pólya Urns, Dirichlet Processes and Tables

A bag initially contains equal numbers of red and blue balls. After each draw, return the ball and add another of its color. A first red makes another red more likely; a run of reds changes the bag further. The rule remembers the past, yet it may assign exactly the same probability to every record with the same color totals. Checking that next-step probabilities sum to one will not settle this symmetry.

## 44.1 Every draw changes the bag, yet the full record may ignore order

<a id="dirichlet-opening"></a>

Start with one red and one blue. Red-blue-red has probability (1/2)(1/3)(2/4)=1/12, and red-red-blue has probability (1/2)(2/3)(1/4)=1/12. The intermediate bags differ but the products agree. Draws are not independent: after a first red, the chance of a second red rises from 1/2 to 2/3.

The calculation puts two apparently conflicting descriptions together: the rule depends on past results, but the joint law may depend only on totals. If this persists at every length, [Chapter 43](43-exchangeability.md#exchange-general) guarantees a common random probability. We now start from the rule, prove or disprove its infinite symmetry, and construct the probability it determines.

## 44.2 Infinite generation does not yet prove exchangeability

<a id="dirichlet-failure"></a>

Change the rule: a red draw adds two reds, whereas a blue draw adds only one blue. Starting from one of each, red-blue has probability 1/8 and blue-red 1/6. Next-step probabilities are always nonnegative and normalized, so the experiment can continue indefinitely, but swapping two observations changes the joint probability.

Measurable normalized predictive kernels already define an infinite process by the sequential construction in Chapter 10. Exchangeability requires the additional consistency between different orders. Not all reinforcement fails, and not every legitimate process must be exchangeable. We study a structure that satisfies both requirements.

## 44.3 How same-color factors rearrange along different histories

<a id="dirichlet-finite"></a>

Allow d colors with nonnegative initial masses \(a_1,\ldots,a_d\) and positive total α. Each occurrence adds unit mass of its color. Masses need not be integers; in that case the bag describes a probability rule rather than fractional physical balls. After n draws, with counts Nⱼ(n), prediction uses relative masses.

\[ P(X_{n+1}=j\mid X_{1:n})=\frac{a_j+N_j(n)}{\alpha+n},\qquad \alpha=\sum_{j=1}^d a_j>0. \]

Multiplying probabilities for a particular ordered word, each color contributes aⱼ,aⱼ+1,… regardless of how its occurrences interleave with other colors. Rising factorials record precisely these factors.

\[ P(X_1=x_1,\ldots,X_n=x_n)=\frac{\prod_j(a_j)^{\uparrow n_j}}{(\alpha)^{\uparrow n}},\qquad (a)^{\uparrow r}=a(a+1)\cdots(a+r-1),\quad(a)^{\uparrow0}=1. \]

This proves finite-dimensional exchangeability, while the sequential kernels give one compatible infinite experiment. A zero-mass color cannot appear: its first occurrence has probability zero. A common reinforcement mass c>0 rescales shapes to aⱼ/c. Color-dependent reinforcement generally destroys the shared denominator structure. See [T-POLYA-DIRICHLET](../foundations/t-polya-dirichlet.md#polya-proof-rule) for the exact scope.

## 44.4 The frequency limit should be identified, not merely named

<a id="dirichlet-hidden"></a>

Chapter 43 makes this exchangeable color record iid given a random vector D. We still need its law. Two colors return to the [Beta posterior in Chapter 2](02-inference.md), but independently drawing several Beta variables will not handle many colors: coordinates must be nonnegative, sum to one, and cannot fluctuate independently.

Try first generating independent positive masses and dividing by their total. Normalization turns independent masses into constrained probabilities. The positive variables should also preserve their family under aggregation; otherwise refining and coarsening colors would produce incompatible models. Gamma additivity supplies this structure.

## 44.5 From positive masses to a Dirichlet vector

<a id="dirichlet-gamma"></a>

Take independent Yⱼ∼Gamma(aⱼ,1), with positive shape and unit rate, and put Dⱼ=Yⱼ/ΣYᵢ. Zero shapes are separately set to zero, with at least one positive shape. For positive coordinates use yⱼ=suⱼ and Jacobian sᵈ⁻¹. The joint density separates into a Gamma total-mass density and a simplex density.

\[ f_a(u)=\frac{\Gamma(\alpha)}{\prod_j\Gamma(a_j)}\prod_j u_j^{a_j-1},\qquad u_j>0,\quad\sum_j u_j=1. \]

The density uses Lebesgue measure on the first d−1 coordinates; the last is fixed by the sum. With only one positive coordinate the probability is concentrated at one. This is the Dirichlet law. The transformation proves both normalization and independence of total mass S from relative probabilities D. The [finite-dimensional companion](../foundations/t-polya-dirichlet.md#polya-proof-gamma) proves the Gamma identities, zero-parameter convention and change of variables.

## 44.6 Aggregation and observation use the same algebra

<a id="dirichlet-conjugacy"></a>

Merging colors sums their independent Gamma masses and hence their shapes. Multiplying the Dirichlet density by the likelihood ∏Dⱼⁿʲ of a specific observed word changes shapes to aⱼ+nⱼ. Aggregation and updating thus establish consistency across spatial partitions and the posterior after observations.

\[ E\prod_jD_j^{n_j}=\frac{\prod_j(a_j)^{\uparrow n_j}}{(\alpha)^{\uparrow n}},\qquad \mathcal L(D\mid X_{1:n})=\operatorname{Dir}(a_1+n_1,\ldots,a_d+n_d). \]

Integrating the word likelihood reproduces the urn law exactly. Sampling a probability first and reinforcing relative masses sequentially give the same complete record law. Conditional independence comes from the former representation; the latter does not require unconditional independence. Their equivalence is a proved statement, not a verbal analogy.

## 44.7 How an unseen color can retain positive probability

<a id="dirichlet-unseen"></a>

A color with zero initial mass never appears in a finite urn. If observations are real locations or belong to an open-ended category space, adding mass only to observed colors permanently rules out unseen results. We need initial mass whose location is not specified by the sample and which can still produce future observations.

On a nonempty standard Borel space E choose a probability H and initial mass β=αH with α>0. Add one unit point mass at each observed value to obtain the prediction below. H does not guarantee a new value on every innovation; an atomic H may generate an old value again.

\[ P(X_{n+1}\in A\mid X_{1:n})=\frac{\alpha H(A)+\sum_{i=1}^n\mathbf1_A(X_i)}{\alpha+n}. \]

Ferguson’s [1973 paper](https://users.wpi.edu/~balnan/Ferguson1973.pdf) studies priors on probability distributions with tractable posteriors. The same-year [paper of Blackwell and MacQueen](https://people.eecs.berkeley.edu/~jordan/courses/281B-spring04/readings/blackwell-macqueen.pdf) extends Pólya sampling to a general color space. Our order-consistency route is a modern reconstruction, not an invented single discovery sequence joining those papers.

## 44.8 Every finite partition must refer to the same random probability

<a id="dirichlet-consistency"></a>

Partition E into measurable cells \(A_1,\ldots,A_d\) and record only the cell of each observation. The predictive formula becomes a finite Pólya rule with shapes αH(Aⱼ), so every color word is exchangeable. For overlapping test sets refine them into Boolean cells and write each event as a finite union of color words. This proves exchangeability of the actual observations; sequential kernels already supply the infinite experiment.

A random probability G should have Dirichlet masses on every finite partition. Gamma aggregation proves consistency of these vectors under refinement. But a consistent array of numbers is not yet a countably additive random probability. Extending over an uncountable set index would still require checking that sample functions are measures. Chapter 43 gives a route that completes this step.

## 44.9 The Dirichlet process emerges as an actual director

<a id="dirichlet-process"></a>

Apply de Finetti to the constructed infinite exchangeable record to obtain a genuine P(E)-valued G. Push it through any finite partition. Its color director gives the same Pólya record law as the finite Dirichlet mixture already constructed. Uniqueness of the directing law identifies them.

\[ (G(A_1),\ldots,G(A_d))\sim\operatorname{Dir}(\alpha H(A_1),\ldots,\alpha H(A_d)),\qquad G\sim\operatorname{DP}(\alpha,H). \]

This is the Dirichlet process: a random probability, not a motion indexed by time. Write its law also as Dβ for β=αH, allowing the entire initial measure to be updated. A zero-parameter cell has zero mass; total parameter stays positive. Countable additivity is secured before identifying finite-dimensional laws; see [T-DIRICHLET-PROCESS](../foundations/t-dirichlet-process.md#dp-proof-director).

## 44.10 Uniqueness uses measurable evaluations, not a process name

<a id="dirichlet-measurable"></a>

We observe G through evaluations G(A), generating the σ-field on P(E). On a standard Borel space a countable generating algebra determines a probability. Every finite collection of evaluations has a common partition refinement, so Dirichlet partition laws determine all joint evaluations and uniquely determine Dβ.

When β later depends on data, separate existence for each β is insufficient; its law must vary measurably. The companion pushes each parameterized predictive record law through the same empirical-CDF decoding map, constructing the kernel β↦Dβ. The [parameter-kernel proof](../foundations/t-dirichlet-process.md#dp-proof-kernel) uses the evaluation structure established in Chapter 43, without a Chapter 49 random-measure topology.

## 44.11 After existence, we want to see what the probability consists of

<a id="dirichlet-explicit"></a>

De Finetti proves existence without listing where the masses lie. Finite Dirichlet vectors normalize Gamma masses. Normalizing an arbitrary infinite list of positive variables may instead face an infinite sum. We need to control total mass from the beginning without silently discarding a remainder.

Try cutting a unit mass: take proportion V₁, then proportion V₂ of the remainder, and continue. Assign independent H-distributed labels Zⱼ to the pieces. This becomes a DP construction only after proving both that the pieces sum to one and that their partition masses are Dirichlet. One observation adds one to a finite Dirichlet shape. Comparing an independent Gamma(1,1) mass with a Gamma mass of total shape α gives an added fraction with law Beta(1,α). This suggests a candidate break to test, without already proving the infinite construction.

## 44.12 The remainder must actually vanish

<a id="dirichlet-stick"></a>

Take iid Vⱼ∼Beta(1,α), independent of iid H labels, and define Pⱼ and Rₘ below. The finite telescoping identity gives only ΣPⱼ≤1, not equality.

\[ P_j=V_j\prod_{i<j}(1-V_i),\qquad R_m=\prod_{i=1}^m(1-V_i),\qquad \sum_{j=1}^mP_j=1-R_m. \]

The Beta integral gives E(1−V)=α/(α+1), hence ERₘ=(α/(α+1))ᵐ→0. The decreasing nonnegative remainder has a limit of expectation zero, so vanishes almost surely. Thus ΣPⱼ=1 and G*=ΣPⱼδZⱼ is a probability at each good path. Interchanging nonnegative double series proves countable additivity; evaluations are measurable series limits.

\[ G^*=\sum_{j\ge1}P_j\delta_{Z_j},\qquad E G^*(A)=H(A). \]

Use a fixed point mass on the null set of bad weights so the map is everywhere probability-valued. [T-STICK-BREAKING](../foundations/t-stick-breaking.md#stick-proof-mass) supplies null-set and integration details. We must still identify its partition laws.

## 44.13 Why Gamma normalization reappears in the infinite construction

<a id="dirichlet-fixedpoint"></a>

For a finite partition let Y be the mass vector of G* and h the base probabilities. Delete the first piece and renormalize the remainder; the tail is an independent copy. Thus Y is a fixed point of the following transformation, with J distributed as h, V∼Beta(1,α), and Y′ an independent copy.

\[ Y\overset d=Ve_J+(1-V)Y^\prime. \]

Dir(αh) is a fixed point. Start with independent Gamma(αhⱼ,1) masses and add an independent Gamma(1,1) mass at the random coordinate J. Independence of original total and relative masses makes the added fraction Beta(1,α). Given J=j, the normalized law is Dir(αh+eⱼ). Mixing these densities with weights hⱼ recovers the original density because Σyⱼ=1.

Other fixed points must be excluded. Couple two possible tail vectors with the same first m breaks and labels; their ℓ¹ difference is at most 2Rₘ. Vanishing remainder equates every continuous expectation on the simplex and hence the laws. Thus Y is Dir(αh) for every partition, and uniqueness gives G*∼DP(α,H). The [complete identification proof](../foundations/t-stick-breaking.md#stick-proof-fixedpoint) does not assume the stick-breaking theorem it proves.

## 44.14 Each probability is discrete, although its average may be continuous

<a id="dirichlet-discrete"></a>

For uniform H on [0,1], EG(A)=H(A) for every A, yet each G is concentrated on the at most countably many locations Z₁,Z₂,…. Continuity of the average law is not continuity of each realization. Finite Dirichlet moments also compute joint fluctuations across regions.

\[ \operatorname{Cov}(G(A),G(B))=\frac{H(A\cap B)-H(A)H(B)}{\alpha+1}. \]

Larger α reduces fluctuations of each fixed regional mass around H. This is a second-moment statement, not a claim that finite α makes G deterministic. Nor is α the number of atoms. Atomic H allows repeated Zⱼ whose weights must be merged. Break order is not size ranking; its relation to table-creation order still needs proof.

## 44.15 The posterior cannot be obtained by dividing point probabilities

<a id="dirichlet-posterior"></a>

Draw G∼DP(α,H), then sample iid conditionally on G. Finite colors admit a density calculation, but under diffuse H a specified exact value x usually has marginal probability zero. Each G is discrete, so an ordinary density with respect to H cannot simply be assumed. To obtain the posterior of the whole G we return to the defining conditional-integral identity.

\[ \mathcal L(G\mid X_{1:n})=\operatorname{DP}\!\left(\alpha+n,\frac{\alpha H+\sum_{i=1}^n\delta_{X_i}}{\alpha+n}\right)=\mathsf D_{\beta+\sum_i\delta_{X_i}}. \]

Test a bounded function of a finite partition evaluation of G together with a sample rectangle. Refine both partition and sample tests, apply finite Dirichlet conjugacy, then aggregate back. This proves the posterior integral identity. Two monotone-class arguments extend it to every sample event and the full evaluation σ-field of G. The data-dependent Dβ+Σδx is already a measurable kernel, not an arbitrary pointwise posterior choice.

See the [posterior proof](../foundations/t-dirichlet-process.md#dp-proof-posterior) for common null sets, zero-mass cells and versions at all data points. We have not mistaken sufficiency of counts for one partition for the claim that exact observations carry no finer information.

## 44.16 Prediction and probability models now determine each other

<a id="dirichlet-predictive"></a>

The Dirichlet mean and tower property give posterior prediction, combining α units of initial mass with n sample units. Generate forward from prediction and recover G by exchangeability, or draw G first and compute its posterior prediction: the two routes produce the same record law.

\[ P(X_{n+1}\in A\mid X_{1:n})=E[G(A)\mid X_{1:n}]=\frac{\alpha H(A)+\sum_{i=1}^n\mathbf1_A(X_i)}{\alpha+n}. \]

This equivalence does not require a literal hidden parameter in reality and does not validate arbitrary subjective updating. It proves that this specific rule is compatible, at every finite length, with a unique random-probability model. Updating changes conditional beliefs about G; in the G-first representation the director is not redrawn after every observation.

## 44.17 Copying a previous customer rather than choosing a color uniformly

<a id="dirichlet-copy"></a>

The predictive formula has an executable form: with probability α/(α+n) draw a fresh independent H label; otherwise choose one of the previous n observations uniformly and copy its value. Selection is proportional to occurrence count, not uniform among distinct seen colors. The latter would be a different rule whose exchangeability must be checked anew.

Also record the copying ancestry: innovation begins a group and copying inherits the selected customer’s group. Calling groups tables gives a partition that does not depend on color names. This ancestry is a copying record, not the independent reproduction mechanism of the Galton–Watson process in Chapter 20.

## 44.18 How the table rule produces an exchangeable partition

<a id="dirichlet-tables"></a>

With k tables of sizes n₁,…,nₖ and n customers, the next joins table j with probability nⱼ/(α+n), or opens a table with probability α/(α+n). The first customer starts the first table. Indexing tables by creation order is bookkeeping; the symmetry concerns the unnumbered blocks under permutations of customer labels.

\[ P(\Pi_n=\pi)=\frac{\alpha^{k}}{(\alpha)^{\uparrow n}}\prod_{j=1}^k(n_j-1)!. \]

Multiply kernels for a specified partition: each table contributes α when founded, then 1,…,nⱼ−1 for joins. The formula depends only on sizes, proving exchangeability. It is the EPPF of the one-parameter Chinese Restaurant Process, giving a particular partition’s probability rather than the total probability of a size pattern. Extension probabilities summing to one prove deletion consistency; see [T-CRP](../foundations/t-crp.md#crp-proof-eppf).

## 44.19 A new table need not produce a new value

<a id="dirichlet-atoms"></a>

Give tables independent H labels Zⱼ and let customers receive their table label. This recovers the same Pólya predictive kernel. For diffuse H the countably many labels are almost surely distinct, so seating and equal-value partitions agree. With atoms, different tables may share a label; the equal-value partition is a coarsening.

\[ P(X_1=X_2)=\frac1{\alpha+1}+\frac{\alpha}{\alpha+1}\int H(\{z\})H(dz),\qquad P(1\sim_{\Pi}2)=\frac1{\alpha+1}. \]

The extra term is the chance of a label collision between different tables. At the extreme H=δz, every value equals z although many tables may open. After general data, a new value has probability αH(E minus {X₁,…,Xₙ})/(α+n), whereas a new table always has probability α/(α+n). The EPPF therefore cannot be applied directly to equal-value blocks for atomic bases. The [label proof](../foundations/t-crp.md#crp-proof-labels) also gives the full sample-rectangle expansion over partitions.

## 44.20 Why residual allocation appears in table-creation order

<a id="dirichlet-frequencies"></a>

Stick-breaking indexes weights first, whereas tables are indexed as they appear. Their relation cannot be inferred from the name DP. Separate the first table from everyone else. First-table membership follows a two-color Pólya rule with initial masses (1,α); given avoidance, the compressed residual seating follows the original CRP again.

Generate that two-color indicator sequence independently of a residual CRP, then interleave them back on the time axis. Matching conditional kernels proves independence of the two components. The first-table frequency is V₁∼Beta(1,α), leaving positive residual proportion 1−V₁. Repeat on the residual problem to obtain independent V₂,V₃,… and frequencies in table-creation order.

\[ \frac{N_j(n)}n\longrightarrow P_j=V_j\prod_{i<j}(1-V_i),\qquad V_j\ \text{iid }\operatorname{Beta}(1,\alpha). \]

Multiply relative frequencies by residual population densities to obtain absolute frequencies. The Vⱼ, not the Pⱼ, are independent. This creation-order residual-allocation law is also called GEM; here α is the concentration and discount is zero. The [frequency proof](../foundations/t-crp.md#crp-proof-deletion) handles decomposition, infinite compression and common null sets.

## 44.21 Why empirical probabilities here can converge in total variation

<a id="dirichlet-empirical"></a>

Existence of every table frequency does not by itself rule out mass moving to ever-later tables. Here ΣPⱼ=1 has been proved. A finite head and the two residual tails upgrade coordinate convergence to ℓ¹ convergence. Mapping tables to labels only merges coordinates.

\[ d_{\rm TV}\!\left(L_n,\sum_jP_j\delta_{Z_j}\right)\le\frac12\sum_j\left|\frac{N_j(n)}n-P_j\right|\longrightarrow0\quad\text{a.s.} \]

This differs from the continuous-uniform director example in Chapter 43, where total variation remains one. Here the director itself is discrete and a finite head captures arbitrarily much mass. A countable ℓ¹ bound controls every set without intersecting uncountably many strong-law full sets. Empirical limits identify ΣPⱼδZⱼ with the unique director. Label collisions leave only the coarsened probability identifiable, not each latent table.

## 44.22 Innovation becomes rarer, yet tables keep accumulating

<a id="dirichlet-count"></a>

Each innovation can be decided by a fresh independent uniform variable, with probability α/(α+n). These probabilities tend to zero but have a divergent sum, so Borel–Cantelli gives infinitely many tables. Their number Kₙ has a precise long-term scale.

\[ EK_n=\sum_{i=1}^n\frac{\alpha}{\alpha+i-1}=\alpha\log n+O(1),\qquad \frac{K_n}{\log n}\longrightarrow\alpha\quad\text{a.s.} \]

Variance is at most the mean. Along nₘ=⌊exp(m²)⌋, Chebyshev errors are summable. Borel–Cantelli gives the subsequence limit, and monotonicity plus consecutive log-scale ratios tending to one fills the gaps; see the [table-count proof](../foundations/t-crp.md#crp-proof-count). For diffuse H this also counts distinct values; for H=δz there is always only one distinct value.

## 44.23 Parameter limits and assumptions that remain in force

<a id="dirichlet-boundaries"></a>

Throughout α>0. The initial predictive rule at α=0 would be 0/0. For fixed record length n, however, the chance all customers share the first table is ∏ᵢ₌₁ⁿ⁻¹i/(α+i)→1 as α decreases to zero. The finite record law thus tends to a model drawing Z∼H and repeating it forever. This is a limit model, not a direct definition by the singular formula.

As α grows, the chance of any copy among a fixed n observations is at most Σᵢ₌₁ⁿ⁻¹i/(α+i)→0. Coupling gives total variation convergence of the finite record law to H to the nth product. Length is fixed; this does not turn an entire infinite record into independent coordinates at a finite parameter. Nonzero-discount Pitman–Yor and two-parameter CRPs require their own admissible parameters, weights and representation proofs in associated Chapter 47 work; they are not established here.

## 44.24 A predictive rule creates a model only with its actual joint structure

<a id="dirichlet-insight"></a>

The changing bag has produced three mutually checkable descriptions: sequential prediction, conditional iid under a random probability, and a table partition with independent labels. They are connected by order-invariant rising factorials, finite Dirichlet partitions, vanishing residual mass, posterior kernel identities and unique empirical identification, rather than analogy.

Observation can be described either as updating beliefs about G or as generating the next result from a prediction rule. These descriptions have the same law here, without automatically carrying the same real-world causal interpretation. Order, value labels and latent seating remain distinct information. With atomic bases, even the full value record need not recover the seating.

Local normalization gives a process; order consistency gives exchangeability; representation and construction reveal what the symmetry retains. If only transformations compatible with some spatial structure are preserved instead of all finite reorderings, what information remains identifiable? The method tells us where to start: specify the object transformed and the joint probabilities actually preserved.

## 44.25 Sources, complete proofs and scope

<a id="dirichlet-sources"></a>

Ferguson’s A Bayesian Analysis of Some Nonparametric Problems appeared in Annals of Statistics 1(2), 1973, 209–230; Blackwell and MacQueen’s Ferguson Distributions Via Pólya Urn Schemes in the same volume and issue, 353–355. Sethuraman’s [1994 journal paper](https://www3.stat.sinica.edu.tw/statistica/j4n2/j4n216/j4n216.htm), A Constructive Definition of Dirichlet Priors, appeared in Statistica Sinica 4, 639–650. These distinct routes are not presented as one person’s continuous discovery.

For tables and residual allocation see [Pitman’s author lectures](https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/pitman_CSP.pdf). This chapter develops its own proofs for the one-parameter standard Borel setting, using α as concentration, distinct from the discount often called α in two-parameter notation. Nonzero discount, general paintboxes and broader random-measure theory are not counted as proved here.

The complete companions are [T-POLYA-DIRICHLET](../foundations/t-polya-dirichlet.md), [T-DIRICHLET-PROCESS](../foundations/t-dirichlet-process.md), [T-STICK-BREAKING](../foundations/t-stick-breaking.md), and [T-CRP](../foundations/t-crp.md).
