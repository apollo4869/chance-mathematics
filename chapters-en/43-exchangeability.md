# Chapter 43: If We Reorder Observations, Does Probability Stay the Same?

Place two cards in a box, marked zero and one, shuffle, and draw them without replacement. The records01 and10 are equally likely. Yet after seeing the first card, the second is certain. Reordering does not change the probability of the complete record, although one observation completely changes the next prediction.

## 43.1 Two cards already distinguish two random structures

<a id="exchange-cards"></a>

Each card separately has probability one half of being one. Mistaking equal marginals for independence assigns probability one quarter to00 and11, although neither is possible. The error is a hidden assumption that drawing leaves the population unchanged.

Swapping the two labels really does preserve their joint probabilities. We need language that retains this symmetry without overstating it. The question is not whether the next draw is independent, but which records remain probabilistically equivalent after relabeling.

## 43.2 Finite symmetry and symmetry that can continue indefinitely

<a id="exchange-definition"></a>

An N-vector in a nonempty measurable E is finitely exchangeable when every permutation of1,…,N preserves its joint law. An infinite record is exchangeable when every permutation fixing all but finitely many indices preserves its law. Its symmetric prefixes must belong to one consistent infinite experiment.

\[ (X_1,\ldots,X_N)\overset d=(X_{\pi(1)},\ldots,X_{\pi(N)}),\qquad \pi\in S_N. \]

An iid record is exchangeable because reordering finite product factors changes nothing. This proves one direction, not its converse. Independence with unequal marginals need not give exchangeability: swapping a deterministic zero and a fair coin changes even the first marginal.

## 43.3 What a total count says about an initial word

<a id="exchange-finite"></a>

For a Bernoulli record of length N, words with j ones can all be permuted into each other. Conditional on that count they are uniform. Exchangeability has not made draws independent; it has made them equivalent to sampling a finite population of known composition without replacement.

\[ P(X_1=x_1,\ldots,X_k=x_k\mid K_N=j)=\frac{(j)_r(N-j)_{k-r}}{(N)_k},\quad r=x_1+\cdots+x_k,\quad k\le N. \]

Each falling factorial records that a used one or zero removes an available choice. The order-zero product is one and impossible words have probability zero. Choosing any distribution of the total count and then a uniform word of that composition gives every finite Bernoulli exchangeable law.

## 43.4 Why a third card cannot preserve the original rule

<a id="exchange-nonextendible"></a>

The two opposite cards cannot be the first two terms of an infinite exchangeable record. Every pair would have to be opposite. Three terms make that impossible: if the first differs from both others, the other two agree.

Variance expresses the obstruction in a reusable form. Each marginal variance is1/4 and the covariance is−1/4. An exchangeable n-extension would have the following sum variance, negative already at n=3.

\[ \operatorname{Var}\!\left(\sum_{i=1}^n X_i\right)=\frac n4-\frac{n(n-1)}4=\frac{n(2-n)}4. \]

Thus infinite symmetry is not merely adding more coordinates. Compatibility at arbitrary length imposes new constraints on dependence. Any representation theorem must preserve this infinite hypothesis; it cannot be inferred from one finite urn.

## 43.5 Reversing the construction in Chapter2

<a id="exchange-converse"></a>

Chapter2 first selected an unknown chance Θ and then tossed coins independently given Θ. Unconditionally they share Θ and may depend; a word probability depends only on its number of ones, so the record is exchangeable. That construction moves from parameter to record.

\[ P(X_1=x_1,\ldots,X_k=x_k)=E[\Theta^r(1-\Theta)^{k-r}]. \]

Now only the infinite exchangeable law is given, with no supplied Θ. Does symmetry itself force such a representation, and can its random chance be recovered from the record? More examples of mixed coins would not answer this converse question.

## 43.6 How a growing population approximates independent sampling

<a id="exchange-replacement"></a>

Fix a short length k inside a much larger first N observations. Sampling positions without replacement differs from independent replacement sampling only when the latter repeats a position. Each pair collides with probability1/N, so the collision probability is at most k(k−1)/(2N).

\[ L_N=\frac1N\sum_{i=1}^N\delta_{X_i},\qquad d_{\rm TV}\!\left(\mathcal L(X_1,\ldots,X_k),E[L_N^{\otimes k}]\right)\le\min\left(1,\frac{k(k-1)}{2N}\right). \]

This uses Chapter42 coupling for a new finite-symmetry approximation: fix the record and couple the indices, without assuming independent observations. Given the record, replacement sampling has the empirical product law. The full index construction is in [T-EXCHANGEABILITY](../foundations/t-exchangeability.md#exchange-proof-replacement).

For fixed k the error disappears as N grows. This is not yet a representation: the empirical probability changes with N, and its limit must be established. Approximate products alone do not create a limiting random parameter.

## 43.7 Why more observations lead to decreasing information in the proof

<a id="exchange-reverse"></a>

Imagine possessing the complete record but erasing the labels of its first N entries. Their composition and the later record remain, while the identity of the first entry is lost. Let Gₙ contain events unaffected by those permutations. Erasing more labels decreases this information. This is different from the increasing information Fₙ of observations arriving in time.

Under an exchangeable law all first N positions have equal status given this information. Averaging over the finite group really is conditional expectation: integration over any invariant event is preserved by every permutation. Thus for Bernoulli records,

\[ E[X_1\mid\mathcal G_N]=\frac1N\sum_{i=1}^N X_i,\qquad \mathcal G_N\downarrow\mathcal J. \]

J contains the information invariant under all finite permutations. Chapter15 now gives an almost sure and L¹ frequency limit. We have not pretended the record is iid; symmetry creates another route through conditional averages.

## 43.8 A random chance emerges from the record

<a id="exchange-bernoulli"></a>

\[ \frac{K_N}{N}\longrightarrow\Theta\in[0,1]\quad\text{a.s. and in }L^1. \]

For a k-word with r ones, its conditional probability given Gₙ is a without-replacement average. The index comparison makes its difference from the empirical independent word probability vanish, so it tends to Θʳ(1−Θ)ᵏ⁻ʳ. To obtain conditioning on Θ rather than just an unconditional integral, multiply by arbitrary bounded h(Θ) and use bounded convergence. A frequency limit is permutation invariant, so h(Θ) is measurable for every Gₙ.

\[ E[h(\Theta)\mathbf1_{\{X_{1:k}=x\}}]=E[h(\Theta)\Theta^r(1-\Theta)^{k-r}],\qquad P(X_{1:k}=x\mid\Theta)=\Theta^r(1-\Theta)^{k-r}. \]

Given the chance extracted from the record, the observations really are iid Bernoulli. Its law M gives the Bernoulli de Finetti representation. Independence has not been read directly from the unconditional record; it appears after conditioning on the correct shared random probability.

\[ P(X_{1:k}=x)=\int_0^1 p^r(1-p)^{k-r}M(dp). \]

## 43.9 The hidden probability is not an arbitrary explanation

<a id="exchange-bernoulli-unique"></a>

If M′ gives the same record law, first sample p from M′ and then iid Bernoulli(p). For every p, the strong law makes the frequency limit p. The event is jointly measurable, so integration preserves probability one. Thus M′ is the distribution of a frequency limit that the record law already fixes as M.

Two terms of an infinite exchangeable Bernoulli record have covariance VarΘ, hence nonnegative. If it is zero, Θ is constant and the entire record is iid. Finite pairwise independence does not suffice: the three-term law uniform on000,011,101,110 is exchangeable and pairwise independent, but an infinite extension would force Θ=1/2 and probability1/8 rather than zero for111.

Infinite compatibility controls all word probabilities, not merely pairs. The [complete scalar proof](../foundations/t-exchangeability.md#exchange-proof-bernoulli) retains the conditional tests, null sets and uniqueness argument.

## 43.10 A general record needs more than a hidden mean

<a id="exchange-random-law"></a>

For observations beyond zero and one, one number cannot describe every chance. Choose equally between the law uniform on±1 and the law uniform on±2, then sample iid from the selected law. Both conditional means are zero and the ordinary covariance of two observations is zero. Yet one observed magnitude determines every later magnitude.

What is shared is a whole probability ν, not just its mean. It assigns a chance ν(A) to each measurable region. Different tests can reveal different hidden information; one low-order moment can miss the dependence.

## 43.11 Why limiting frequencies alone do not yet define a probability

<a id="exchange-additivity"></a>

Finite averaging yields a Bernoulli-type empirical limit for each set A. But assigning these limits individually as ν(A) leaves countable additivity unproved. A probability is not a table of unrelated values; it must respect infinite disjoint unions.

A nonexchangeable warning is the deterministic record Xᵢ=i. On the natural numbers each finite set has limiting empirical mass zero, while the whole space always has mass one. The limits on the finite-cofinite algebra form a finitely additive probability with no countably additive extension having those values. This does not refute exchangeability; it exposes the missing step in taking limits separately.

Chapter10 provides a safer tool: a conditional probability kernel first constructs a whole probability, which frequencies can then identify. We must explain how a probability itself becomes a random object.

## 43.12 Observing a probability as a random object

<a id="exchange-measure-space"></a>

Let P(E) be the countably additive probabilities on E, equipped with the evaluation σ-field. For each A we may observe μ↦μ(A). On standard Borel E, a countable generating algebra both determines probabilities and generates this σ-field. A random directing probability has measurable evaluations and is an actual probability at each sample point.

This is substantive. Encode E as Borel B⊂[0,1] and a probability by its rational CDF values. Monotonicity, right continuity, boundary values and mass concentrated on B are Borel conditions. Quantile decoding proves that P(E) itself is standard Borel. [T-DIRECTING-MEASURE](../foundations/t-directing-measure.md#directing-proof-space) supplies every condition, measurable integral and inverse map without later random-measure theory.

## 43.13 Construct a probability first, then identify it by frequencies

<a id="exchange-conditional-law"></a>

Return to J. We need not list all its events to ask for the conditional law of X₁ given this information. Standard Borel E guarantees a kernel; J need not be treated as an already known standard Borel quotient. Let ν be this conditional law. Kernel construction has already supplied its countable additivity.

\[ \nu(\omega,A)=P(X_1\in A\mid\mathcal J)(\omega),\qquad L_N(A)=E[\mathbf1_A(X_1)\mid\mathcal G_N]\longrightarrow\nu(A). \]

Versions cannot be selected arbitrarily set by set. Chapter10 first unifies rational CDF readings outside a countable null set, repairs them into a probability kernel, and then verifies conditional identities by a monotone class. Simultaneous empirical limits on a countable determining algebra identify that existing probability.

## 43.14 How symmetry averaging separates several coordinates

<a id="exchange-general"></a>

A conditional law for one coordinate is not independence; joint events must factor. Fix k sets and erase labels within the first N entries. Every ordered distinct k-tuple of positions occurs equally often, so the conditional rectangle probability is a without-replacement average.

\[ E\!\left[\prod_{\ell=1}^k\mathbf1_{A_\ell}(X_\ell)\,\middle|\,\mathcal G_N\right]=\frac1{(N)_k}\sum_{\substack{i_1,\ldots,i_k\le N\\\text{all distinct}}}\prod_{\ell=1}^k\mathbf1_{A_\ell}(X_{i_\ell}). \]

The collision bound makes the right side approach the product of empirical evaluations, each of which converges to its ν-evaluation. Reverse martingale convergence identifies the left limit, yielding the product. Conditional independence was not smuggled into finite sampling; finite sampling is dependent, and the infinite limit removes collisions for fixed k.

\[ E\!\left[\prod_{\ell=1}^k\mathbf1_{A_\ell}(X_\ell)\,\middle|\,\mathcal J\right]=\prod_{\ell=1}^k\nu(A_\ell). \]

First establish this simultaneously on the countable algebra for all k, then extend by uniqueness of probability kernels. This is the core of the general de Finetti representation: an infinite exchangeable law on a nonempty standard Borel space is a conditional iid law directed by a random probability. Uniqueness of that directing law remains to be justified below.

## 43.15 From finite rectangles to the whole record

<a id="exchange-path-law"></a>

Chapter8 constructs the infinite product for each μ. Cylinder evaluations are products of μ-evaluations, and a monotone class makes these products a kernel K(μ,·). Also take the regular conditional law R of the whole record given J. The preceding identities make R and K(ν,·) agree simultaneously on countable determining cylinders. Off their common null set they are probabilities agreeing as whole path measures by π–λ.

\[ P(X\in D\mid\mathcal J)=\nu^{\otimes\mathbb N}(D),\qquad P(X\in D\mid\sigma(\nu))=\nu^{\otimes\mathbb N}(D). \]

The second identity is the tower property, not another hypothesis. Let M be the law of ν on P(E); integration gives the mixture below. [T-DIRECTING-MEASURE](../foundations/t-directing-measure.md#directing-proof-path) completes the space, kernel and null-set arguments.

\[ P(X\in D)=\int_{\mathcal P(E)}\mu^{\otimes\mathbb N}(D)\,M(d\mu). \]

For a sequence on any original sample space, construct on its canonical record law and pull ν back as a measurable function of the record. The theorem identifies information in the record, not arbitrary external variables on the original space.

## 43.16 In what sense does the empirical probability identify its director?

<a id="exchange-empirical"></a>

For each fixed integrable reading f, group averaging remains conditional expectation, so Lₙf→νf almost surely and in L¹. Every fixed Borel-set evaluation converges too, but separate almost sure assertions for each fixed set do not imply a single null set valid for all sets.

If E carries a Polish topology, the whole empirical probability converges weakly to ν almost surely. For fixed μ, Lipschitz functions on a compact set have finite nets. Strong laws control the net readings and mass outside the compact. A countable determining class makes the resulting event jointly measurable before it is integrated over random μ.

\[ L_N\Rightarrow\nu\quad\text{a.s. in a specified Polish realization}. \]

This is not total variation convergence. For iid uniform[0,1], the finite set of the first N observations has empirical mass one and Lebesgue mass zero, so distance stays one. Weak convergence and strong laws for fixed sets hold without reproducing every event from finite data. [T-EXCHANGEABLE-EMPIRICAL](../foundations/t-exchangeable-empirical.md) proves the weak-distance, measurability, compact-net and quantifier steps.

## 43.17 Why a different directing probability cannot give the same record

<a id="exchange-unique"></a>

Suppose Λ is another random probability making the whole record conditionally iid. The iid strong law holds simultaneously on the countable determining class under every fixed μ. Conditional integration makes empirical evaluations converge to Λ-evaluations on the original space. They already converge to ν, so the two probabilities agree almost surely on a determining class and hence everywhere as measures.

For an alternative mixing distribution M′, sample μ from it and generate a product record. Its empirical director is μ. Since the record law is the same, the extracted directing law has the same distribution, giving M′=M. Uniqueness concerns the probability identifiable from an infinite record, not a preferred story about hidden causes.

## 43.18 Deleting finite prefixes and finite labels leaves the same information

<a id="exchange-tail"></a>

Tail information T ignores every finite prefix, so finite permutations preserve it and T⊂J. The directing probability has a tail-measurable version: take empirical limsup rational CDF readings and repair invalid probability codes uniformly. It equals the original ν almost surely, placing σ(ν) inside T.

Conversely, for each fixed A∈J the conditional path kernel gives ν-product probability of A equal to1A. The left side depends only on ν, so A does too modulo null sets. This yields equality of completions, not a pointwise identification of the raw event collections.

\[ \overline{\sigma(\nu)}^{\,P}=\overline{\mathcal T}^{\,P}=\overline{\mathcal J}^{\,P}. \]

The two ways of reducing information are different, but exchangeability makes their eventual contents agree: what is determined by the shared random probability. This cannot be transferred to arbitrary nonexchangeable records, where permutations need not preserve the law and group averaging need not be conditional expectation.

## 43.19 Why Hewitt–Savage must say iid

<a id="exchange-hs"></a>

For an iid record the director is deterministic, suggesting that permutation-invariant information is trivial. A direct proof independent of the representation theorem is still revealing: it shows separately what independence and identical distribution contribute.

Approximate invariant A by an event B depending only on the first n coordinates, with error below ε. Swap this block with the next n to obtain B′. Identical distribution and invariance of A make B′ another ε-approximation; independence makes B,B′ independent. Thus A is approximated by two independent copies of its approximation, forcing PA close to its square.

\[ |P(A)-P(A)^2|\le4\varepsilon,\qquad P(A)\in\{0,1\}. \]

This is the Hewitt–Savage zero-one law. A general exchangeable mixture fails its unconditional conclusion: for Θ=1/4 or3/4, the event that frequency exceeds one half has probability one half. Independence without identical distribution also fails: let the first term be a fair coin and the rest zero; exactly one one is invariant and has probability one half. The [full proof](../foundations/t-exchangeable-information.md#exchange-info-hs) handles prefix approximation, the four-ε estimate and modulo-null representatives.

## 43.20 Stronger order symmetry does not imply stronger forgetting

<a id="exchange-stationary"></a>

Infinite exchangeability implies strict stationarity: a finite index translation can be completed to a finite permutation. The converse fails: Chapter41’s random-phase alternating record supports010 and101, not001. Independence, shift invariance and finite-permutation invariance have distinct conditions.

If the director is nondegenerate, some determining A has nonconstant ν(A). Conditional iid gives a positive covariance between its indicators at any two distinct positions, regardless of separation. Unlike Chapter42 mixing, this dependence does not decay.

\[ \operatorname{Cov}(\mathbf1_A(X_i),\mathbf1_A(X_j))=\operatorname{Var}(\nu(A))>0\quad(i\ne j). \]

Indeed the shift-invariant information of an exchangeable law is also σ(ν) modulo null sets. It is shift-ergodic exactly when ν is deterministic, equivalently when the record is iid. The extreme exchangeable laws are the same products: split a nondegenerate mixture by a parameter event; a nontrivial decomposition of a product would contradict unique mixing. See the [information companion](../foundations/t-exchangeable-information.md#exchange-info-extreme).

## 43.21 Order symmetry does not prevent learning

<a id="exchange-prediction"></a>

Let Fₙ contain only the first n observations actually seen. Given ν and the past, the next observation has law ν. Given the past alone, ν is not fully identified and prediction takes its posterior mean. This is a different information problem from the decreasing Gₙ used to erase labels in the proof.

\[ E[f(X_{n+1})\mid\mathcal F_n]=E[\nu f\mid\mathcal F_n]\longrightarrow\nu f\quad\text{a.s. and in }L^1\qquad(f\text{ bounded Borel}). \]

Conditional independence first justifies νf given both ν and the past; the tower then yields the equality. Since ν is measurable from the whole record, upward martingale convergence in Chapter15 identifies the posterior limit as νf. See the [prediction proof](../foundations/t-exchangeable-information.md#exchange-info-prediction) for the tests and null sets.

For a Bernoulli mixture an n-word with k ones reweights M by pᵏ(1−p)ⁿ⁻ᵏ. A Beta prior gives the Chapter2 prediction (k+a)/(n+a+b). The new result is not that integral again, but existence and uniqueness of M for every infinite exchangeable law. Zero-denominator words are impossible under the model and admit arbitrary conditional versions.

## 43.22 The probability is unique, not every hidden parameter label

<a id="exchange-identifiability"></a>

In a model that samples θ and then iid from μθ, de Finetti identifies μθ. Different θ can produce the same probability. For example take θ=±a,0<a<1, then iid Bernoulli(θ²). The director is the fixed Bernoulli(a²), while the record contains no information about the sign.

The definition also concerns each fixed finite permutation, not every data-dependent rearrangement. Sorting two iid continuous observations makes the first smaller with probability one instead of one half. The transformations constrained by symmetry and the ways an observer uses data are different conditions. Arbitrary adaptive selection has not been declared exchangeable here.

## 43.23 Symmetry makes dependence identifiable rather than removing it

<a id="exchange-insight"></a>

The two cards showed dependence without a preferred order. The impossible third card made infinite continuation a substantive mathematical requirement. The collision error between replacement and nonreplacement then explained why products emerge from infinite symmetry, while reverse martingales and conditional kernels made the limit more than a guessed formula.

The conclusion is not that exchangeability equals independence. A shared random probability can retain genuine long-term random information and create unconditional dependence; products arise after conditioning on it. The director is uniquely identified by empirical behavior, so it is not arbitrary, yet not every external parameter becomes identifiable.

Observation preserves symmetry under fixed relabeling while changing our knowledge of the directing law. A concrete new question follows: rather than specifying M first, which rules for updating the next prediction after each observation are compatible with an infinite exchangeable law? Arbitrary reinforcement need not be; compatibility must be checked from the predictive rule itself.

## 43.24 Sources and exact proof scope

<a id="exchange-sources"></a>

The [1937 paper of de Finetti](https://numdam.org/item/AIHP_1937__7_1_1_0/) appeared in Annales de l’Institut Henri Poincaré7(1),1–68. Hewitt and Savage published [Symmetric measures on Cartesian products](https://doi.org/10.1090/S0002-9947-1955-0076206-8) in Transactions of the AMS80 (1955),470–501. Our cards, collision comparison and conditional-kernel sequence are a modern reconstruction, not a claim that either original followed this discovery route.

Further reading on exchangeable representations is available in the [author lectures of Aldous](https://www.stat.berkeley.edu/~aldous/Papers/me22.pdf). Proofs and exposition are developed independently here. The four complete companions are [T-EXCHANGEABILITY](../foundations/t-exchangeability.md), [T-DIRECTING-MEASURE](../foundations/t-directing-measure.md), [T-EXCHANGEABLE-INFORMATION](../foundations/t-exchangeable-information.md), and [T-EXCHANGEABLE-EMPIRICAL](../foundations/t-exchangeable-empirical.md).

The complete main theorem concerns infinite standard Borel sequences. Standard Borelness is a sufficient condition used by this proof, not a classification of every possible state space. Finite approximation is not infinite extendibility; Hewitt–Savage assumes iid; weak limits require a specified Polish realization. General group actions, arrays and partitions are not established by a sequence representation alone.
