# T-MARKOV-BRANCHING: Leaf Deletion, Splitting Laws and Regenerative Representation

This page proves the finite and infinite representations used in [Chapter 57](../chapters/57-regenerative-growth.md#growth-markov-branching). Initially trees are nonplane labeled hierarchies without edge lengths; a planted root edge may be added but is not a split. Regeneration here means conditional independence and reuse of a family of subtree laws after the first split, not renewal in physical time.

## 1. Make subtree independence a testable recursion

<a id="mb-recursion"></a>

For n≥2 let qₙ be an exchangeable probability on nontrivial partitions of [n]. Conditional on the root partition π, generate independent copies T(B) from the same family on its blocks, relabel by increasing order and attach them to the root. A one-label tree is deterministic. Every block is smaller than n, so recursion terminates and defines a unique Markov branching law Pₙ. All state spaces are finite, making every kernel measurable. Conversely, the root laws q determine any family with this conditional subtree independence.

## 2. Deleting a label can suppress the root

<a id="mb-deletion"></a>

For n≥3 put pₙ=qₙ({{n},[n−1]}). If deleting n removes a singleton side of a binary root split, that root branch is suppressed and the remaining whole tree has law Pₙ₋₁. Otherwise the projected root partition stays nontrivial. The n singleton-isolation root events are disjoint and equally likely, so pₙ≤1/n<1. Suppression removes an unbranched vertex, not the distinguished root; lengths of any planted edges require their own rule.

\[ (r_{n-1})_*q_n\big|_{\mathcal P_{n-1}\setminus\{\mathbf1\}}=(1-p_n)q_{n-1},\qquad n\ge3. \]

The displayed identity is necessary and sufficient for sampling consistency. For necessity, split the deleted tree’s root law into noncollapse and collapse, the latter contributing pₙqₙ₋₁, and rearrange. For sufficiency use induction on n. Deletion within a nonsingleton child preserves its law by induction and leaves the other children independent; deletion of a singleton removes that child. Except when the root collapses, the resulting children are independent family members on the projected blocks. In the collapse case the remaining tree already has law Pₙ₋₁. The identity gives qₙ₋₁ also in the noncollapse case, proving the whole-tree claim. Exchangeability extends it to every label and finite restriction.

## 3. Recover a locally finite rate measure from finite probabilities

<a id="mb-rate-representation"></a>

\[ \gamma_2=1,\qquad\gamma_n=\frac{\gamma_{n-1}}{1-p_n},\qquad K_n=\gamma_nq_n\quad(n\ge2). \]

Extend Kₙ by zero at the trivial partition. The preceding identity makes its nontrivial projections consistent: for m<n, projection onto nontrivial [m]-partitions gives Kₘ. Let Bₘ be the event that an infinite partition is nontrivial on [m]. For fixed m restrict Kₙ, n≥m, to finite states whose [m]-restriction is nontrivial. Their common mass is γₘ, and normalization gives consistent probabilities. Chapter 8 supplies a finite measure κᵐ on Bₘ. Cylinder uniqueness makes these measures agree on smaller Bₘ. The Bₘ increase to the entire nontrivial partition space.

\[ \kappa(A)=\lim_{m\to\infty}\kappa^m(A\cap B_m),\qquad \kappa(B_m)=\gamma_m<\infty,\qquad (r_m)_*\kappa\big|_{\mathcal P_m\setminus\{\mathbf1\}}=K_m. \]

The increasing pasting is a measure: countable additivity follows by exchanging two nonnegative increasing limits after finite-measure additivity. Values on finite nontrivial cylinders are determined by the exchangeable Kₙ. Local finiteness on Bₘ and a π–λ argument extend invariance to all measurable sets and prove uniqueness. Without γ₂=1 uniqueness is up to positive time scale. Conversely any nonzero exchangeable κ, finite on every Bₘ and charging no trivial partition, gives γₘ=κ(Bₘ)>0 and normalized qₘ. If γ₂ were zero, every specified pair-separation event would have zero κ-mass; their countable union is the nontrivial space, forcing κ=0. Projection recovers the recursion.

## 4. An infinite branching history really exists

<a id="mb-process"></a>

The nontrivial partition space is the compact partition space with one point removed, standard Borel and locally compact; the Bₘ form an increasing compact-open cover. Chapter 48 constructs Poisson atoms of intensity dt κ(dπ) #dk. Use Chapter 56’s internal increasing enumeration to refine current block k. On [n], only k≤n and π∈Bₙ can matter, at rate at most nγₙ. Finite paths are nonexplosive, and shared atoms give consistency. No prior decomposition of a general κ into ν and erosion is needed.

A block with m≥2 visible members waits Exp(γₘ) for its next effective split and then uses qₘ. Separated block terms in the finite generator give independent futures. At most n−1 effective refinements yield singletons; every intervening wait has positive finite rate, so this happens in finite time almost surely. The resulting finite genealogy has law Pₙ. Common paths for all n give an exchangeable infinite hierarchy. Alternatively apply Chapter 56’s compact inverse-limit construction directly to the Pₙ; finite-restriction uniqueness identifies the two laws.

## 5. A broad concrete splitting family and a failure

<a id="mb-examples"></a>

\[ q_n(\pi)=\frac{\int PB_s\{r_n\Pi=\pi\}\nu(ds)}{\int(1-\sum_i s_i^n)\nu(ds)},\quad \pi\ne\mathbf1,\quad c=0. \]

For a nonzero integrable ν from Chapter 56 with positive denominator, the formula is a special case of the κ representation and therefore defines a sampling-consistent Markov branching family; erosion may also be included in κ. By contrast suppose every root splits its current sample as evenly as possible. Sizes three and four give 1+2 and 2+2, so deletion at four looks harmless. But size five gives 2+3; deletion in the smaller child produces 1+3, forbidden at size four. Independent children and locally normalized rules do not repair this conflict.

## 6. The binary formula exposes the collapse factor

<a id="mb-binary"></a>

\[ \left(1-\frac{q_n(1)+q_n(n-1)}n\right)q_{n-1}(i)=\frac{i+1}{n}q_n(i+1)+\frac{n-i}{n}q_n(i),\quad1\le i\le n-2. \]

Here qₙ(i) is the size probability on the left after independently orienting a binary root; qₙ(i)=qₙ(n−i), and label subsets are uniform given size. This is a different coordinate from qₙ(π) for a particular partition. The two terms correspond to deletion on the left or right. The prefactor removes collapse after deleting a singleton side. Necessity follows from whole-tree consistency and sufficiency from independent-subtree induction. Omitting collapse often misclassifies a correct conditional splitting law.

## 7. What the representation identifies, and what it does not

<a id="mb-scope"></a>

The complete representation here concerns exchangeable unweighted finite Markov branching families and a locally finite exchangeable κ, with a consistent infinite hierarchy. Choosing γ₂ adds a clock; mass-dependent clock changes can also preserve an unclocked genealogy. General inverse ν/c classification is not proved, so Chapter 56’s gap remains open. A hierarchy need not be compact: equal-length finite stars are consistent while infinitely many leaves stay distance 2 apart. The next companion proves compactness and mass for Brownian line-breaking separately. [Return to the chapter](../chapters/57-regenerative-growth.md#growth-consistency).
