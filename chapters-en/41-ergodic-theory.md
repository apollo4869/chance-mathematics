# Chapter 41: Why Can a Random World Exhibit Long-Term Stability? — Stationarity and Ergodic Theory

An instrument produces a continuing record of zeros and ones. After a long time the proportion of ones seems to settle; another instrument built in the same way settles at a different proportion. More observations do not remove the difference. Perhaps the records are still too short, or perhaps each instrument selected a different environment before recording began. A settling average alone cannot distinguish these explanations.

The independent strong law explains repeated sampling under a fixed law. Our task is not another calculation of sampling error. It is to retain the dependence between records and ask what random variable a long-term average can become, and what it identifies in the whole record.

## 41.1 A coin bias persists through all future observations

<a id="ergodic-mixture"></a>

Construct the entire experiment first. Choose Θ equal to 1/4 or 3/4 with equal probabilities, take independent uniform variables U₀,U₁,… independently of Θ, and put Xₖ=1{Uₖ≤Θ}. The product space of Chapter 8 accommodates them all. Conditional on Θ the records are independent; without conditioning they share the same bias.

\[ EX_k=\frac12,\qquad \operatorname{Cov}(X_0,X_1)=\operatorname{Var}(\Theta)=\frac1{16},\qquad \frac1n\sum_{k=0}^{n-1}X_k\longrightarrow\Theta\quad\text{a.s.} \]

The last assertion follows from the Chapter 12 strong law under each of the two conditional probabilities and then from their finite mixture. It does not apply an independent theorem directly to dependent X. The average settles, but not to the unconditional mean 1/2. The effect of choosing Θ does not decay with time.

Chapter 2 treated an unknown bias as an object of inference. The new question is how dependence enters a limit theorem. We need more than a parameter appended to the answer: the probability space itself should identify the information that averaging never removes.

## 41.2 Equal daily distributions are not enough

<a id="ergodic-stationarity"></a>

The preceding experiment is indifferent to the observation's starting index: shifting any finite collection of times preserves its joint law. This is strict stationarity. It concerns all finite-dimensional distributions, rather than merely equal marginals or even invariant means and covariances.

\[ (X_{k_1+h},\ldots,X_{k_m+h})\ \overset d=\ (X_{k_1},\ldots,X_{k_m}),\qquad h\ge0,\quad k_j\ge0. \]

For example, let X₀=X₁=Z for a fair sign Z, and let X₂,X₃,… be independent fair signs independent of Z. All marginals agree, but the first pair is always equal and the next pair is equal only with probability 1/2. The process is not stationary. Shifting an experiment must preserve its dependence as well.

Stationarity is not yet a convergence proof. It supplies a global structure that can be reused. We next turn a change of observation origin into an operation on events and readings.

## 41.3 Moving the record without changing its probability law

<a id="ergodic-preserving"></a>

On the canonical record space Eᴺ⁰ with path law P, let T(x₀,x₁,… )=(x₁,x₂,… ). Finite cylinders generate its sigma algebra, so the uniqueness results of Chapters 5 and 8 show that strict stationarity is equivalent to P(T⁻¹A)=P(A) for every measurable A. We take E standard Borel, giving record spaces and later conditional kernels a precise measurable structure.

More generally a measurable T on a probability space is measure preserving when it satisfies that identity. It need not be invertible. Preimages remain legitimate and preserve set operations even when discarding the first record cannot be reversed. A reading f generates the stationary process f,f∘T,f∘T²,… .

\[ A_nf=\frac1n\sum_{k=0}^{n-1}f\circ T^k,\qquad \|f\circ T\|_p=\|f\|_p\quad(1\le p<\infty). \]

T need not be a known deterministic rule predicting a physical motion. It may simply move the origin within a space of complete random records. Expressing a probability problem by iteration of a map does not remove randomness; it makes shift invariance usable in equations.

## 41.4 Information that remains the same after a shift

<a id="ergodic-invariant"></a>

The environment chosen by the instrument does not change when the first ten records are deleted. For a general process we collect every event with this property, allowing null differences between versions. They form the invariant sigma algebra I.

\[ \mathcal I=\{A\in\mathcal F:P(T^{-1}A\triangle A)=0\},\qquad f\circ T=f\ \text{a.s.}\ \Longleftrightarrow\ f\text{ has an }\mathcal I\text{-measurable version}. \]

The sigma-algebra property follows from preimages, countable unions, complements and null sets. The assertion for functions is checked on rational level sets; the reverse direction starts with indicators, then simple functions and limits. For Lᵖ variables invariance is a statement about equivalence classes, not every arbitrary representative at every point.

If A belongs to I, averaging does not spread its indicator elsewhere: Aₙ1_A=1_A almost surely. Any universal limit formula must retain this randomness. Conditional expectation from Chapter 9 can express retaining this information and averaging the rest, but that observation alone does not prove the proposed limit.

## 41.5 First identify what cancels

<a id="ergodic-coboundary"></a>

Some averages require no independence to evaluate. If f=g−g∘T with bounded g, consecutive terms cancel, leaving only the ends of the record. Such functions are called coboundaries. The important fact is that the endpoint error does not accumulate with the number of observations.

\[ A_n(g-g\circ T)=\frac{g-g\circ T^n}{n}\longrightarrow0,\qquad \|A_n(g-g\circ T)\|_\infty\le\frac{2\|g\|_\infty}{n}. \]

Invariant readings remain intact and coboundaries disappear. Approximating a general f by these two kinds of readings could identify its average. But approximation in mean square does not control all observation lengths along an infinite record. We first settle the geometry of the space, then obtain that pathwise control.

## 41.6 Long-term projection in Hilbert space

<a id="ergodic-mean"></a>

On L² put Uf=f∘T. Measure preservation makes U a linear isometry, with a closed fixed space. More precisely, the orthogonal complement of the closure of the coboundaries (I−U)g is Fix U. This remains true for noninvertible T; we must not silently assume that U is unitary.

The orthogonal complement is initially ker(I−\(U^*\)). If \(U^*\)h=h, then 〈Uh,h〉=‖h‖² and the isometry gives ‖Uh−h‖²=0. Conversely use \(U^*\)U=I. The endpoint identity makes averages of coboundaries vanish in L², whereas fixed vectors remain unchanged. Since the norm of Aₙ is at most one, approximation in the closure completes the argument.

\[ L^2=\operatorname{Fix}U\ \oplus\ \overline{\operatorname{ran}(I-U)},\qquad A_nf\xrightarrow{L^2}E[f\mid\mathcal I]\quad(f\in L^2). \]

Chapter 9 identifies conditional expectation as orthogonal projection onto L²(I). The von Neumann mean ergodic theorem is thus a projection forced by isometry and cancellation, not a new guess about averaging. It still gives convergence only in mean square, not yet along almost every record.

## 41.7 On which paths can an average become large?

<a id="ergodic-maximal"></a>

To pass from manageable readings to every integrable reading, we need control over all n rather than a convenient subsequence. Record a path whenever one of its first partial sums Sₖf is positive. Their positive maximum F_N has an exact finite recursion.

\[ F_N=\max(0,S_1f,\ldots,S_Nf)=(f+UF_{N-1})^+,\qquad E_N=\{F_N>0\},\qquad f\mathbf1_{E_N}\ge F_N-UF_{N-1}. \]

On E_N the recursion gives equality; outside it the right side is nonpositive. Integration uses measure preservation and F_N≥F_{N−1}, giving ∫_{E_N}f≥0. Letting N increase and using integrability proves Hopf’s maximal ergodic lemma. No independence is required, and ever exceeding a level has not been replaced by exceeding it at the final time.

\[ \int_{\{\sup_{k\ge1}S_kf>0\}}f\,dP\ge0,\qquad P\!\left(\sup_{n\ge1}A_n|r|>\lambda\right)\le\frac{\|r\|_1}{\lambda}\quad(\lambda>0). \]

The last estimate applies the lemma to |r|−λ. An error small in L¹ cannot produce a large average of any length on many paths. This is precisely the control missing from mean convergence. The [complete finite recursion and maximal estimates](../foundations/t-ergodic.md#ergodic-proof-maximal) also establish the strong Lᵖ bound needed later for several parameters.

## 41.8 From cancelling readings to almost every record

<a id="ergodic-birkhoff"></a>

Linear sums of bounded invariant functions and bounded coboundaries are dense in L¹. The Hilbert decomposition first gives L² density, truncation makes both types bounded, and bounded functions are dense in L¹. Call this class D. Averages of h∈D converge pathwise, with a known limit.

Approximate integrable f by h_j∈D. The difference between the upper and lower limits of Aₙf is at most 2supₙAₙ|f−h_j|. The maximal estimate bounds the probability of oscillation greater than ε by 2‖f−h_j‖₁/ε. Let j increase. Oscillation vanishes, and the same estimate excludes infinite limits. We have a finite almost-sure limit \(f^*\), not merely a convergent subsequence.

Integrability gives ΣₙP(|f|>εn)<∞. Measure preservation and Borel–Cantelli imply f∘Tⁿ/n→0, so \(f^*\) is invariant. For A∈I, ∫_A Aₙf=∫_A f for every n. To pass to the limit, approximation by D and L¹ contraction show L¹ convergence to \(f^*\) as well: Fatou makes the limiting operator an L¹ contraction, so both approximation errors are controlled by ‖f−h_j‖₁. The integral identities therefore survive and identify conditional expectation uniquely.

\[ f\in L^1,\quad P\circ T^{-1}=P\quad\Longrightarrow\quad A_nf\longrightarrow E[f\mid\mathcal I]\quad\text{a.s. and in }L^1. \]

This is the Birkhoff pointwise ergodic theorem used here. The [complete density, null-set and identification argument](../foundations/t-ergodic.md#ergodic-proof-pointwise) supplies every step. L² readings also converge in L² by the earlier theorem; that does not give L² convergence for an arbitrary L¹ reading.

## 41.9 When does the random limit become a constant?

<a id="ergodic-ergodicity"></a>

T is ergodic when every invariant event has probability zero or one. Then every integrable I-measurable variable is constant, making the Birkhoff limit Ef. Conversely, if every indicator average converges to its unconditional mean, an invariant event A satisfies 1_A=P(A), forcing probability zero or one. Ergodicity excludes positive-probability pieces separated by different invariant environments.

Return to the opening model. On the enlarged space T shifts the U sequence while leaving Θ unchanged. Each fixed-Θ Bernoulli shift is ergodic; we shortly prove the stronger mixing property. An invariant event consequently has conditional probability zero or one given Θ, and its indicator equals that conditional probability. Thus I is precisely σ(Θ), modulo null sets. Observing only X does not lose Θ, since the long-run proportion recovers it.

\[ E[X_0\mid\mathcal I]=\Theta,\qquad A_nX_0\to\Theta,\qquad \operatorname{Var}(\Theta)=1/16>0. \]

The long record removes sampling fluctuations within an environment without removing the randomness of selecting that environment. The theorem does not equate stability with determinism. It identifies the information in which the remaining random variable lives.

## 41.10 No invariant environment need not mean forgotten phase

<a id="ergodic-mixing"></a>

Let Ω consist of two equally likely points, 0 and 1, and let T swap them. With f(ω)=ω the system is ergodic: its only invariant events are trivial. Each record alternates zeros and ones, with average tending to 1/2. Yet the present determines the phase at every future time. Ergodicity therefore does not mean eventually forgetting the past.

\[ P(A\cap T^{-n}B)\longrightarrow P(A)P(B)\quad(A,B\in\mathcal F) \]

If this decay holds for every A and B, the transformation is strongly mixing. Taking an invariant A shows that mixing implies ergodicity. In the two-point example, A=B={0} gives 1/2 at even n and zero at odd n, so mixing fails.

An independent shift is mixing: finite-coordinate cylinders become independent at large separation, and arbitrary events are approximated in probability by their algebra. Intersection errors are bounded by the two approximation errors. First increase separation, then remove the errors. This also proves the Bernoulli ergodicity used above. Chapter 42 has separate responsibilities for stationary Markov chains, more general mixing and coupling; these do not follow automatically from the definition here.

## 41.11 What integrability and measure preservation prevent

<a id="ergodic-boundaries"></a>

Stationarity does not permit dropping integrability. Independent standard Cauchy observations are stationary and ergodic, but every average is still standard Cauchy. If the averages had an almost-sure finite limit, we must not assert that (Xₙ−X₀)/n vanishes in this nonintegrable example. Instead delete any fixed finite prefix: it cannot affect an existing finite limit. That limit is tail measurable, hence constant by the Chapter 12 zero–one law. Its constant limit contradicts the unchanged Cauchy distribution of each average.

Conversely, bounded readings do not replace measure preservation. In a deterministic zero–one record with alternating constant blocks of lengths 2^{2^j}, each new block overwhelms the old record, and averages at block endpoints oscillate between zero and one. The point mass on this record is not shift invariant. Birkhoff is not a theorem about an arbitrary sufficiently long sequence.

A further quantifier matters: each f has its own probability-one set. Separate assertions for all fixed Borel readings do not automatically give one sample on which uncountably many arbitrary readings all work. A simultaneous assertion requires a countable determining class and another argument, as the coming decomposition construction will show.

## 41.12 Returns and continuous time need no new independence assumption

<a id="ergodic-return-flow"></a>

Measure preservation alone gives infinitely many returns to A for almost every point starting in a positive-probability event A. If B⊂A consists of points never returning, the sets T⁻ⁿB are disjoint with equal probabilities, so P(B)=0. Points returning only finitely often eventually enter B and are also null. Birkhoff adds the frequency E[1_A|I], rather than merely return.

Continuous time also requires a specified structure. Let (θ_t) be a jointly measurable, measure-preserving semiflow with θ₀=id and θ_{s+t}=θ_sθ_t, and let f∈L¹. Use F=∫₀¹f∘θ_s ds as the unit-block reading. The discrete theorem handles integer blocks; stationary integrable tails of the absolute block integral control the final incomplete block. Each fixed shift alters only the two ends. The limit is invariant under every fixed θ_r, and testing integrals identifies it.

\[ \frac1t\int_0^t f\circ\theta_s\,ds\longrightarrow E[f\mid\mathcal I_{\rm flow}]\quad\text{a.s. and in }L^1,\qquad \mathcal I_{\rm flow}=\bigcap_{r\ge0}\mathcal I_{\theta_r}. \]

The intersection concerns invariant-event sigma algebras modulo null sets, not an uncountable intersection of probability-one sets. The [continuous-time proof](../foundations/t-ergodic.md#ergodic-proof-flow) handles tails, time parameters and L¹ limits. An invariant probability must already exist. Brownian motion on the whole line has no finite stationary probability to insert into this probability-preserving statement.

## 41.13 Can a general hidden environment be separated by conditional probabilities?

<a id="ergodic-decomposition"></a>

The opening had only two environments, so conditioning could be done one at a time. A general I may have no preassigned parameter. If a kernel P_ω decomposes P and almost every P_ω is measure preserving and ergodic, random conditional averages become ordinary means within each environment. This is the concrete task of ergodic decomposition.

\[ P(A)=\int P_\omega(A)P(d\omega),\qquad P_\omega(f)=E[f\mid\mathcal I](\omega),\qquad P_\omega\text{ is }T\text{-invariant and ergodic for a.e. }\omega. \]

Here E is standard Borel and T is a Borel probability-preserving map; completions are handled afterward through equivalence classes. An arbitrary measurable space does not automatically admit this regular kernel. Nor is the proof just the instruction to condition on I. Conditional means h_j of a countable generating algebra first produce a countably generated G equal to I modulo P; Chapter 10 then supplies its conditional kernel.

For countably many tests, the measure-preserving integral identity makes the kernel invariant almost everywhere. The same countable family of Birkhoff limits becomes constant after conditioning on G. These tests are dense in each L²(P_ω), so invariant functions there must be constants: the kernel really is ergodic. The [complete decomposition proof](../foundations/t-ergodic-decomposition.md) handles common null sets, parameter concentration and uniqueness. It promises neither an exception-free unique environment at every individual point nor an application of future Harris theory.

## 41.14 When the cost of a block is not a sum of individual rewards

<a id="ergodic-subadditive"></a>

So far a block's reading has been a sum of individual rewards. Magnifications of successive random matrices do not add. Even after taking logarithms, we generally obtain only an inequality. Estimating blocks separately lets each choose its most amplified direction; the first block's output need not point along the second block's preferred input.

\[ X_n=\log\|A_{n-1}\cdots A_0\|,\qquad X_{m+n}\le X_m+X_n\circ T^m. \]

We therefore study subadditive accumulations. Independence is unnecessary for this example: a stationary matrix sequence gives such X. The precise Kingman version proved here assumes finite integrable Xₙ, the displayed subadditivity for all m,n almost surely, and infₙEXₙ/n>−∞. Then Xₙ/n converges almost surely and in L¹ to an integrable invariant variable γ.

\[ \gamma=\inf_{n\ge1}\frac1nE[X_n\mid\mathcal I]\quad\text{a.s.},\qquad E\gamma=\inf_{n\ge1}\frac{EX_n}{n}. \]

The random limit is still organized by invariant information, but it is not generally the conditional mean of a chosen single-step X₁. The infimum retains additional cancellation available in long blocks. Subadditivity has not silently been turned back into additivity.

## 41.15 Why subadditive limits need two different block arguments

<a id="ergodic-kingman-mechanism"></a>

Start in the ergodic case. Put Yₙ=Xₙ−SₙX₁≤0. It remains subadditive, and Birkhoff restores the subtracted part at the end. For a fixed block length k, split from each of the k possible offsets and average the inequalities. This counts each complete k-block once. Using ergodicity along Tᵏ alone would be wrong: ergodicity of T need not pass to Tᵏ, as the two-point swap shows.

\[ kY_N\le\sum_{j=0}^{N-k}Y_k\circ T^j,\qquad \limsup_N\frac{Y_N}{N}\le\inf_k\frac{EY_k}{k}=:\beta. \]

A fixed block does not give the lower bound. G=liminf Yₙ/n satisfies G≤G∘T; equal distributions force equality and ergodicity makes it constant. If G<β, choose G<a<β≤0. Almost every record eventually offers a block with unit cost below a. Restrict its length to at most K; the probability of an available starting point tends to one as K increases.

Scan from left to right, selecting an available short block and otherwise skipping one position. Since Y≤0, skipped pieces cannot increase the upper bound. Selected blocks cover at least all available starting points. Their inequality forces the expected unit cost of a long segment close to a, below β, contradicting its definition. The greedy cover resolves the real difficulty: very low local ratios cannot occur at path-dependent lengths everywhere while leaving all expected unit costs above them.

For a nonergodic law, apply the result to the ergodic kernels actually constructed above. Conditional subadditivity and monotonicity along factorial indices identify γ, while Scheffé’s argument for the nonpositive version gives L¹ convergence. [T-SUBADDITIVE](../foundations/t-subadditive.md) supplies the cover, expectations, conditional lower bound and countable record factor for an arbitrary probability space; it does not leave the general case to an analogy.

## 41.16 A growth rate does not yet decompose all directions

<a id="ergodic-matrix"></a>

For stationary invertible d×d random matrices, assume integrability of log⁺‖A₀‖ and log⁺‖A₀⁻¹‖. Product norm bounds above, and inverse norms below, make Xₙ integrable with a linear expected lower bound. The preceding theorem genuinely applies.

\[ -\sum_{j<n}\log^+\|A_j^{-1}\|\le\log\|A_{n-1}\cdots A_0\|\le\sum_{j<n}\log^+\|A_j\|,\qquad \frac1n\log\|A_{n-1}\cdots A_0\|\to\gamma. \]

This gives the exponential scale of maximal amplification. It does not establish a limit for every vector or construct all Lyapunov subspaces; a norm limit is not the complete multiplicative ergodic theorem. Without the lower bound, the subadditive example Xₙ=−n² has unit cost tending to −∞. If matrices can vanish, infinite logarithms likewise need explicit treatment.

## 41.17 Why observing in two directions needs another estimate

<a id="ergodic-multiparameter"></a>

Spatial records need not form a single sequence. Let T₁,…,T_d commute and each preserve probability, and average f over rectangles. Taking one directional limit and then another gives an iterated limit, not automatically the limit when all sides grow together. Very thin rectangles cannot simply be replaced by a sequence of cubes.

\[ A_{\mathbf n}f=\frac1{n_1\cdots n_d}\sum_{0\le k_i<n_i}f\circ T_1^{k_1}\cdots T_d^{k_d},\qquad \mathcal J=\bigcap_{i=1}^d\mathcal I_{T_i}. \]

We prove that for 1<p<∞ and f∈Lᵖ, Aₙf converges almost surely and in Lᵖ to E[f|J] as minᵢnᵢ→∞. Iterating the one-dimensional strong maximal bound controls all rectangles at once. Bounded jointly invariant functions and bounded coboundaries in each direction form a dense Lᵖ class, on which each coboundary vanishes with its corresponding side length.

\[ \left\|\sup_{\mathbf n}|A_{\mathbf n}f|\right\|_p\le\left(\frac p{p-1}\right)^d\|f\|_p. \]

The product estimate explains the stated p>1 range: the one-dimensional L¹ theorem cannot simply be copied to all multiparameter rectangles. The [complete multiparameter proof](../foundations/t-multiparameter.md) establishes commuting projections, density and a common null set for every rectangle tending to infinity. General-group Følner averages, endpoint L¹ results and ratio ergodic theory are not claimed here; Markov ratio limits belong to Chapter 42.

## 41.18 Beyond frequencies, how much information is in a whole block?

<a id="ergodic-entropy"></a>

Two stationary records can have the same zero–one frequencies yet very different predictive structures. Both alternating records and fair independent coins spend half their time at each symbol. But once its phase is known, the alternating record has no further choices. Single-symbol frequencies miss this difference.

The smaller the probability of an observed word w, the larger the reading needed to identify it. Probabilities multiply for independent concatenations, whereas information should add, motivating −log P(w). Its average for a discrete law p is Shannon entropy. We use natural logarithms, with information measured in nats.

\[ H(p)=-\sum_a p_a\log p_a,\quad 0\log0=0,\qquad H(X,Y)=H(X)+H(Y\mid X). \]

The chain identity expands p(x,y)=p(x)p(y|x). Concavity of −u log u shows that additional conditioning cannot increase mean conditional entropy. It does not say that the surprise of each actual record decreases. Individual readings and mean information must be distinguished. The [entropy foundations](../foundations/t-entropy.md#entropy-proof-basics) handle zero-probability words and countable sums as well.

## 41.19 Using an increasingly long past as a condition

<a id="ergodic-information-rate"></a>

Take a two-sided stationary process (Xₖ)ₖ∈Z on a countable alphabet, assuming H(X₀)<∞; finite alphabets are included. Let p_k(a) be the probability conditional on the previous k symbols and p_∞(a) the probability conditional on the entire past. Conditional-expectation martingale convergence from Chapter 15 gives convergence of each p_k(a), but cannot by itself move −log through expectations: logarithms magnify small probabilities.

\[ I_k=-\log p_k(X_0),\qquad I_k\to I_\infty\ \text{a.s.},\qquad H(X_0,\ldots,X_{n-1})=\sum_{j=0}^{n-1}EI_j. \]

A stopping test for conditional probabilities provides the missing control. For each a, wait until p_k(a) first falls below e⁻ᵗp₀(a). The probability that the actual symbol is still a at that time is at most e⁻ᵗp₀(a). Summing over a gives an integrable envelope for supₖIₖ: it is at most I₀ plus a nonnegative variable with tail bounded by e⁻ᵗ. This is where finite entropy is used, rather than as a customary decoration on the theorem.

Consequently Iₖ→I∞ in L¹. Dividing block entropy by n gives the mean information rate h=EI∞. This is still an average over experiments. Reading a single long record requires a pathwise result for the logarithm of its word probability.

## 41.20 How word probabilities yield a pathwise information rate

<a id="ergodic-smb"></a>

Successive conditioning of the actual word writes −log P(X₀,…,Xₙ₋₁) as \(\sum_{j=0}^{n-1}I_j\circ T^j\). The function changes with j, so this is not immediately a Birkhoff average of a fixed f. The new difficulty is a triangular array of readings, not another independent strong law.

If f_j→f almost surely and all |f_j| are bounded by one integrable F, then Σf_j∘Tʲ/n has the same limit as Aₙf. For fixed K the initial K terms vanish after division by n. The rest is bounded by Aₙg_K, where g_K=supⱼ≥K|f_j−f| decreases to zero and is integrable. Birkhoff gives E[g_K|I], then K increases. This proves the required Maker triangular-average lemma without an unjustified interchange of limits.

\[ -\frac1n\log P(X_0,\ldots,X_{n-1})\longrightarrow h_{\mathcal I}:=E[I_\infty\mid\mathcal I]\quad\text{a.s. and in }L^1. \]

This is the Shannon–McMillan–Breiman version proved here. In the ergodic case h_I=h is constant, and an actual typical word has probability like e⁻ⁿʰ on the exponential scale. In a nonergodic system the information rate can retain its environment. P(X₀,…,Xₙ₋₁) means the unconditional cylinder probability of the observed word, not an unspecified conditional probability. The [complete information-rate proof](../foundations/t-entropy.md#entropy-proof-smb) includes envelopes, chain-rule versions and L¹ convergence.

## 41.21 Does information rate belong to a reading or to the system?

<a id="ergodic-ks"></a>

A finite measurable partition P turns the system into a finite-symbol record; h(T,P) measures its mean new information per unit time. A different reading can give a different value. Taking the supremum over all finite partitions defines Kolmogorov–Sinai measure entropy h(T). A measure-preserving isomorphism transports partitions, word probabilities and refinements together, so preserves this entropy.

\[ h(T,\mathcal P)=\lim_n\frac1nH\!\left(\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\right),\qquad h(T)=\sup_{\mathcal P\ {\rm finite}}h(T,\mathcal P). \]

If T is invertible and the translates at all positive and negative times of a countable finite-entropy partition P generate F modulo null sets, then h(T)=h(T,P). This generator assertion needs proof: larger finite observation windows drive the remaining conditional entropy of any finite Q to zero. The chain inequality bounds h(T,Q) by h(T,P) plus that error. Window edges add only a fixed number of copies of P and do not affect the rate. The [complete proof](../foundations/t-entropy.md#entropy-proof-generator) retains invertibility, generation and finite entropy.

An independent Bernoulli record has entropy rate −p log p−(1−p)log(1−p), whereas the two-point alternating system has entropy zero, although both are ergodic. Even the opening mixture of p=1/4 and 3/4 has equal conditional entropy rates but is not ergodic. A stable average, an information-rate number and mixing are different readings. None substitutes for the full remaining structure.

## 41.22 What randomness survives stability?

<a id="ergodic-insight"></a>

The two instruments now have a precise explanation. Their long-term averages differ because time shifts preserve information that averaging does not erase. Measure preservation provides one law for comparing origins, the maximal ergodic lemma controls the whole sequence of averages, and the invariant sigma algebra identifies the structure carrying the limit. Ergodicity is the case where that structure is trivial, not a synonym for every kind of stability.

Subadditivity takes us from additive rewards to growth of multiplicative structures. Several parameters distinguish iterated limits from a joint limit. Information rates move beyond frequencies to the difficulty of identifying an entire record. Each advance has its own assumptions and proof. Shift symmetry can replace some uses of independence without making dependent blocks independent or guaranteeing forgotten phase.

The questions for a motion with transition kernels can now be more precise. Beyond an invariant probability and stable averages, what makes future laws from different starting points approach one another? Which obstructions come from periods, which from distinct long-term regions, and which can be identified by comparing two legally coupled motions? These are new questions about evolution, not answers supplied by convergence of an average.

### Sources and scope

Birkhoff’s [1931 paper](https://doi.org/10.1073/pnas.17.2.656) and von Neumann’s [1932 paper](https://doi.org/10.1073/pnas.18.1.70) give historical entry points for pointwise and mean results. Their dynamical formulations are not verbatim statements of this chapter’s abstract L¹ theorem. Kingman’s [1968 paper](https://doi.org/10.1111/j.2517-6161.1968.tb00749.x) is an original source for subadditivity. Our finite maximal recursion, conditional-kernel organization and information-rate development are modern mathematical reconstructions, not reconstructions of the authors’ private thoughts.

The complete longer proofs are [T-ERGODIC](../foundations/t-ergodic.md), [T-ERGODIC-DECOMPOSITION](../foundations/t-ergodic-decomposition.md), [T-SUBADDITIVE](../foundations/t-subadditive.md), [T-MULTIPARAMETER](../foundations/t-multiparameter.md) and [T-ENTROPY](../foundations/t-entropy.md). They do not automatically establish nonsingular transformations, infinite-measure ratio theorems, general-group averages, the full Oseledets decomposition, relative entropy or information-rate theorems without finite-entropy assumptions. Markov long-term convergence and Harris regeneration remain Chapter 42 responsibilities.
