# T-PREDICTABLE-SYMMETRY: Sampling, Spreadability and Information Order

We prove equivalence of deterministic subsequence invariance and exchangeability for infinite sequences, and law preservation under explicitly predictable sampling and transformations. State spaces are nonempty standard Borel and group actions jointly measurable. The only tools are Chapter10 conditional kernels, Chapter41 Birkhoff, Chapter43 de Finetti and earlier discrete filtration theory. Return to [Chapter45](../chapters/45-invariance.md#sampling-question).

## 1. Why subsequence invariance is already strong

<a id="sampling-spreadable"></a>

Call an infinite sequence spreadable, also called contractable here, if every deterministic strictly increasing integer subsequence has the same finite-dimensional laws as the original. Exchangeability implies this immediately: any finite increasing set of indices can be mapped from the initial indices by a finite permutation. The converse uses infinitude.

On record space, spreadability first gives left-shift invariance, hence stationarity. Let 𝓘 be the invariant σ-field of that shift. Take any finitely many bounded Borel functions f₁,…,fₖ. Split the first kN positions into k successive blocks of length N. Every term in the expanded product of block averages is a mixed moment at increasing indices, so its expectation is independent of N.

\[ \mathbb E\prod_{j=1}^k f_j(X_j)=\mathbb E\prod_{j=1}^k\left[\frac1N\sum_{i=(j-1)N+1}^{jN}f_j(X_i)\right]. \]

Chapter41 Birkhoff implies that each block average tends to E[fⱼ(X₁)|𝓘]: block j is j times the average through jN minus j−1 times that through (j−1)N. Boundedness permits dominated convergence for the product. The limit is the expectation of the product of these conditional expectations, unchanged by permuting the fⱼ. Rectangle indicators and π–λ give exchangeability. Stationarity alone was not confused with exchangeability: equality of every increasing-index mixed moment supplies the block-product identity.

Chapter43 now gives its unique directing random probability ν and conditional iid structure. Moreover ν(A)=E[\(\mathbf1_A\)(X₁)|𝓘] almost surely: compare the ergodic and Chapter43 empirical limits for the same A, unify null sets on a countable determining class and use measure uniqueness. Use ν as an actual probability-valued random element, rather than assembling arbitrary versions separately for each A. A finite sequence has no arbitrarily long blocks, so the converse cannot be transferred to it.

## 2. Legitimate skipping rather than selecting desired answers

<a id="sampling-skipping"></a>

Let Xₙ be adapted to 𝓕ₙ and have fixed conditional law μ given 𝓕ₙ₋₁ for every n. The filtration may contain prior auxiliary randomness, but that condition must remain true. Take strictly increasing, almost surely finite integer times τⱼ such that {τⱼ=n}∈𝓕ₙ₋₁. This is stronger than being a stopping time: deciding to keep observation n must precede seeing its value.

\[ \mathbb E\prod_{j=1}^k f_j(X_{\tau_j})=\prod_{j=1}^k\mu(f_j)\quad(f_j\text{ bounded Borel}). \]

Expand the final selected term. On {τₖ=n}, all earlier selected values occurred before n; their product times this event indicator is 𝓕ₙ₋₁-measurable. Conditional expectation replaces fₖ by μ(fₖ). Sum over n and use finiteness of τₖ to make the event indicators sum to one. Induct backward in k. For signed tests bounded products justify the countable sum. This proof also explains why simply saying random times is insufficient.

For a fair coin, the first occurrence of one is an almost surely finite stopping time, but not a predictable selection as above; its selected value is always one. If τ can be infinite with positive probability, conditioning on successful selection can also change the directing law. For a mixed exchangeable coin, inspect X₁ and keep subsequent records only when X₁=1. Conditioning on success multiplies the hidden parameter law by that parameter and renormalizes it. A well-defined local rule does not guarantee preservation after such conditioning.

## 3. Conditional iid extends the argument to exchangeable sequences

<a id="sampling-exchangeable"></a>

Let ν direct the sequence, and suppose the conditional law of fresh Xₙ given the enlarged field σ(ν)∨𝓕ₙ₋₁ is ν. Take increasing, finite selection times predictable for this filtration; rules using only past observations and independent auxiliary randomness satisfy the information requirement. Replace the constant μ(f) in the previous proof by σ(ν)-measurable ν(f), and include an arbitrary bounded σ(ν) test at each step. The selected records remain iid ν conditional on ν. Thus their infinite sequence has the original exchangeable law, without changing the directing law.

This does not permit an arbitrary enlargement containing future information. Revealing the next result in advance destroys the conditional iid premise. Reverse-martingale identification of the directing law and the present predictable selection argument solve different problems; the word exchangeability cannot replace the sampling hypotheses.

## 4. Group transformations allowed to depend on the past

<a id="sampling-transform"></a>

Let G be a standard Borel group acting jointly measurably on E, and let μ be invariant under every g. If fresh Xₙ has law μ given 𝓕ₙ₋₁ and gₙ is an 𝓕ₙ₋₁-measurable G-valued random element, then Yₙ=gₙXₙ still has conditional law μ and the entire Y sequence is iid μ. For the kernel proof first test rectangular functions a(ω)b(x), extend by the function monotone-class theorem to bounded 𝓕ₙ₋₁⊗B(E)-measurable functions, then substitute f(gₙ(ω)x).

\[ \mathbb E[f(g_nX_n)\mid\mathcal F_{n-1}]=\int f(g_nx)\,\mu(dx)=\mu(f). \]

This substitutes into one jointly measurable kernel; it does not substitute a random g into separately almost sure identities for each fixed g. Conditional on ν, if ν itself is G-invariant almost surely, the same argument gives predictable transformations of exchangeable sequences. Prior rotations of uniform spherical noise and prior orthogonal transformations of Gaussian vector noise are examples; rotating the current noise into a fixed hemisphere is not. For a mixed normal sequence the conditional variance may be random: a prior rotation preserves its conditional law at that variance, rather than forcing unconditional independence.
