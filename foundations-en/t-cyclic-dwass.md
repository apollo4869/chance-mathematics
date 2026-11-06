# T-CYCLIC-DWASS: Indexed Cuts, First Passage, and Total Progeny

This companion proves the cycle lemma and Dwass formula used in [Chapter 52](../chapters/52-discrete-trees.md#trees-cycle), including feasibility, enumeration, and conditional sampling. Its only preceding tree inputs are the list bijection in [T-TREE-CODING](t-tree-coding.md#coding-lukas) and iid exploration in [T-GW-TREES](t-gw-trees.md#gw-tree-forest). No conditioned-tree limit theorem is used.

## 1. The cycle lemma: exactly how many indexed cuts are legal

<a id="cycle-indexed"></a>

\[ a_i\in\{-1,0,1,\ldots\},\quad \sum_{i=1}^{n}a_i=-m,\quad 1\le m\le n. \]

Read the cyclic word starting after each indexed cut, with cut indices from zero to n minus one. A cut is legal when the new partial sums remain strictly above minus m before ending at minus m. Theorem: exactly m indexed cuts are legal. Distinct cuts of a periodic word may produce the same word; their indices are still counted separately.

\[ S_0=0,\quad S_j-S_{j-1}=a_j,\quad a_{j+n}=a_j,\quad S_{j+n}=S_j-m\qquad(j\in\mathbb Z). \]

Extend increments periodically to all integer times and cumulative sums by the displayed relation. The sums tend to positive infinity to the left and negative infinity to the right. Since a downward step has size at most one, every integer level has a first hitting time. All earlier values are strictly larger: to descend from the high values on the left to anything lower one must first pass through that level. Denote these first hitting times as follows. Periodicity also gives their translation rule.

\[ t_h=\min\{j\in\mathbb Z:S_j=h\},\qquad t_{h-m}=t_h+n. \]

Cutting at any first hitting time is legal: the level m lower is first reached one period later, so all earlier relative sums exceed minus m. Conversely, suppose a cut r is legal. For any earlier time j, choose a positive integer q translating it into the period beginning at r. Legality and periodicity give

\[ r\le j+qn<r+n,\qquad S_j=S_{j+qn}+qm>S_r+(q-1)m\ge S_r. \]

Thus r is the global first hitting time of its level. Legal cuts are exactly the residues modulo n of such times. Levels differing by m have first hitting times differing by n; conversely, congruent times have congruent levels modulo m. This is a bijection between levels modulo m and legal cuts modulo n, proving the count m. Zero increments, repeated minima, and periodic words are all allowed; distinct rotations were not assumed.

## 2. Why the one-tree cut uses the first minimum

<a id="cycle-first-min"></a>

\[ m=1,\qquad r=\min\operatorname*{arg\,min}_{0\le j<n}S_j. \]

This is the unique legal cut. A direct verification also explains the tie rule. If the minimum is zero, its first occurrence is the starting point and all preterminal sums are nonnegative. If the cut occurs later, the minimum is at most minus one. Between the cut and the old endpoint all values minus that minimum are nonnegative, including the old endpoint at minus one. After wrapping to the beginning but before reaching the cut, each old value exceeds the first minimum by at least one; subtracting that minimum and one again leaves a nonnegative sum. The terminal sum is minus one.

For increments minus one, zero, zero, the first minimum is after the first increment. Rotation gives zero, zero, minus one, a legal one-tree path. The last minimum gives zero, minus one, zero, ending the tree prematurely before another reading. If m equals n and every increment is minus one, all n cuts are legal but yield only one distinct word. A count of m cuts is therefore not a count of m distinct rotated words.

## 3. Dwass’s formula without conditioning on null events

<a id="dwass-formula"></a>

\[ \xi_1,\ldots,\xi_n\overset{\mathrm{iid}}{\sim}p,\quad S_j=\sum_{i=1}^j(\xi_i-1),\quad \tau_m=\inf\{j\ge0:m+S_j=0\}. \]

Sum over cuts the indicators that a cut is legal and the endpoint is minus m. The cycle lemma gives m times the endpoint indicator; off that endpoint event every indicator is zero. The iid product law is invariant under cyclic shifts, so every summand has expectation equal to the probability that the original walk first reaches minus m at step n. Taking expectations yields

\[ nP(\tau_m=n)=mP(S_n=-m),\qquad P(N^{(m)}=n)=\frac mn\,P\!\left(\sum_{i=1}^n\xi_i=n-m\right)\quad(n\ge m\ge1). \]

The exploration theorem identifies first passage with forest total size, completing the proof. Sizes below the number of roots have probability zero. The offspring law may be supercritical, have infinite mean, or assign zero probability to some values: the formula still computes finite total sizes, with infinite mass recorded separately. No division by endpoint probability occurred, so an impossible endpoint correctly gives zero. For one ancestor and one vertex the formula gives the probability of zero offspring.

## 4. Lattice feasibility: a residue need not suffice at small sizes

<a id="dwass-feasibility"></a>

\[ P(N=n)>0\ \Longleftrightarrow\ \exists k_1,\ldots,k_n\in\operatorname{supp}p:\ \sum_{i=1}^n k_i=n-1. \]

Necessity follows from the edge count; sufficiency follows from a legal cyclic cut of such an offspring word and its positive product weight. If zero offspring is impossible, every summand is at least one and no finite tree exists. If only zero offspring is possible, there is only the root. Otherwise take the greatest common divisor of the positive offspring support. Since zero is in the support, this is also the maximal offspring lattice span.

\[ p_0>0,\quad d=\gcd\{k\ge1:p_k>0\}\quad\Longrightarrow\quad P(N=n)>0\ \Longrightarrow\ n\equiv1\pmod d. \]

The converse holds for all sufficiently large sizes in the correct residue class. Here is the needed argument. Choose finitely many positive support values already having greatest common divisor d: successive greatest common divisors form a decreasing positive integer sequence and stabilize. Divide by d and choose one generator a. The remaining generators generate all residues in the finite group modulo a. Nonnegative combinations suffice, because each inverse in a finite group is a positive multiple of its generator. Choose one nonnegative representative combination for each residue. Any larger integer in that residue is obtained by adding copies of a. Multiplying back by d represents n minus one. The number of positive summands is at most n minus one, so zeros fill the list to n entries.

Small sizes still require an actual sum representation. For support zero, four, six, the span is two, but size three, despite being odd, would require a sum of two from those support values and is impossible. For support zero, two, exactly all odd sizes are feasible. Size-conditioned formulas are used only at genuinely positive-probability sizes.

## 5. Degree profiles, Catalan counts, and conditional profiles

<a id="dwass-profiles"></a>

\[ \sum_{k\ge0}n_k=n,\quad \sum_{k\ge0}k n_k=n-1\quad\Longrightarrow\quad \#\{t:|\{u:k_t(u)=k\}|=n_k\ \forall k\}=\frac1n\frac{n!}{\prod_k n_k!}. \]

For a fixed finitely supported profile, there are as many ordered words as the multinomial coefficient. Each word has one legal indexed cut. Each legal word has exactly n preimages as a pair consisting of an original word and a cut index: every index fixes the inverse rotation. This is indexed double counting, not an unproved division by the number of distinct rotation orbits. Dividing by n and using the coding bijection gives the formula.

\[ \#\{t:|t|=n\}=\frac1n\binom{2n-2}{n-1},\qquad
\#\{\text{full }r\text{-ary plane trees with }j\text{ internal vertices}\}
=\frac1{rj+1}\binom{rj+1}{j}\quad(r\ge2). \]

For the first formula, count all n-tuples of nonnegative integers summing to n minus one by arranging n minus one marks and n minus one separators, then apply the same indexed-cut count. For the second, allow offspring only zero or r: j internal vertices force the number of leaves to be r minus one times j plus one. Substitute into the profile formula. These count rooted ordered shapes, not trees with arbitrary distinct vertex labels.

Every tree with a given profile has the corresponding product of offspring probabilities. Multiplying by the profile count and dividing by the Dwass size probability shows that the unordered offspring profile conditional on tree size has the law of the iid profile conditional on its sum being n minus one. This does not make the ordered preorder string an ordinary iid bridge: it must also satisfy first passage.

## 6. An exact rotation from an iid bridge to a conditioned tree

<a id="dwass-conditioned"></a>

Assume the endpoint event has positive probability. Sample the iid offspring string conditional on its sum being n minus one. Rotate the increment string at the first minimum of its partial sums, then reconstruct the tree by the pending-list algorithm. The resulting law is exactly that of the original GW tree conditional on total size n.

To prove this, check the weights of rotation preimages. An integer word with total increment minus one cannot have a nontrivial period: repetition q times would make minus one divisible by q, forcing q to be one. Each legal word thus has n distinct rotated preimages, all with the same product weight and all mapped back by their unique legal cut. Their combined bridge probability is the following expression, exactly the conditioned tree weight.

\[ \frac{n\prod_{i=1}^n p_{k_i}}{P(\sum_{i=1}^n\xi_i=n-1)}
=\frac{\prod_{i=1}^n p_{k_i}}{P(N=n)}. \]

This is an exact identity at each feasible finite size, not a scaling limit. Taking large bridges, studying continuity of the minimum cut, and controlling heights and contours still require new conditional tightness and limit proofs. Those belong to Chapter 53; ordinary Donsker is not substituted for them here. Return to [Chapter 52](../chapters/52-discrete-trees.md#trees-conditioned).
