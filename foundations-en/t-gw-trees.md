# T-GW-TREES: Complete Genealogies, Exploration, and Total Size

This companion completes the probabilistic constructions in [Chapter 52](../chapters/52-discrete-trees.md#trees-gw). Initially the offspring law is any probability on nonnegative integers; neither finite mean nor a finite tree is assumed. For coding bijections see [T-TREE-CODING](t-tree-coding.md), and for the counting argument see [T-CYCLIC-DWASS](t-cyclic-dwass.md).

## 1. The complete family on countably many potential addresses

<a id="gw-tree-space"></a>

\[ p=(p_k)_{k\ge0},\qquad \xi_u\overset{\mathrm{iid}}{\sim}p\quad(u\in\mathcal U),\qquad \mathcal U=\bigcup_{h\ge0}\mathbb N_+^h. \]

The countable product construction of Chapter 8 supports all experiments on its product σ-algebra; no normalization over finite trees is needed. The root is born. A word is born exactly when each successive child label is no larger than its prefix vertex’s offspring count. This is a finite set of coordinate inequalities, making each birth indicator measurable and hence the full binary family measurable. Every coordinate is finite almost surely; their countable intersection gives local finiteness of the entire tree.

\[ P(\mathcal T=t)=\prod_{u\in t}p_{k_t(u)}\qquad(t\text{ a finite plane tree}). \]

Indeed, equality to a specified finite tree means precisely that every address in that tree has its prescribed offspring count. Zero offspring at its leaves already prevent outside addresses from being born; no conditions on infinitely many unborn coordinates are required. Independence gives the product. A zero factor makes the tree probability zero, and summing over finite trees gives the extinction probability, which need not equal one.

Given k children at the root, stripping each child prefix leaves mutually disjoint coordinate families, independent of the root coordinate. The k complete subtrees are therefore independent copies of the original tree. This tree-valued branching property is stronger than knowing only the next generation’s conditional population law. Taking generation sizes gives exactly the Galton–Watson process of Chapter 20, while the tree retains all parental relationships discarded by that projection.

## 2. Why adaptive exploration still reveals independent offspring

<a id="gw-tree-exploration"></a>

Reveal offspring successively using the preorder pending list. The next address depends on previous readings, so independence at random indices needs proof. Fix a finite exploration history specifying all previously read addresses and values. These finite data determine the pending list. If it is nonempty, its next address is unexamined; on this history event that coordinate still has the original law and is independent of the finitely many examined coordinates.

There are countably many finite histories. On each history event multiply a bounded past-measurable function by a bounded function of the next reading, integrate using coordinate independence, then sum over histories. The next reading thus has conditional law p given the past. After exploration ends append fresh independent experiments, giving an infinite iid sequence whose initial readings are the actual exploration. This extension does not change the completed tree.

\[ S_j=\sum_{\ell=1}^{j}(\xi_\ell-1),\qquad N=|\mathcal T|\ \overset d=\ \tau_1:=\inf\{j\ge0:1+S_j=0\},\quad \inf\varnothing=\infty. \]

The equality includes infinity. A finite tree empties the list after all its vertices are visited. Conversely, if the list empties after finitely many steps, the algorithm has already constructed a complete finite tree, leaving no unseen branch. Failure ever to empty thus corresponds to an infinite tree. Only finite histories were used; ordinary preorder was not claimed to reach every vertex of an infinite tree.

## 3. Forests, fresh experiments after stopping, and the infinite boundary

<a id="gw-tree-forest"></a>

\[ N^{(m)}=\sum_{a=1}^{m}|\mathcal T^{(a)}|,\qquad \tau_m=\inf\{j\ge0:m+S_j=0\},\qquad N^{(m)}\overset d=\tau_m. \]

For m independent ordered trees start with m root slots. Complete the first tree before exploring the next. The same exploration argument gives the displayed distributional identity. Legal finite forest paths end at minus m, remain strictly above minus m beforehand, and have increments at least minus one. The inverse list construction starts with m roots, with a different initial slot count from the one-tree case. Such a forest with n vertices has n minus m edges.

After a finite first-passage time, iid readings restart. On the event that a stopping time equals a finite integer r, the stopped past uses only the first r coordinates and is independent of any subsequent finite string. Summing over r proves that subsequent finite strings have the product law and are independent of the stopped information. This is the required discrete stopping partition argument, not an appeal to continuous-time strong Markov. No first reading after an infinite stopping time is defined.

The infinite-tree warning is substantive. Let the root have two children, its first child continue along an infinite single-child chain, and its second child be a leaf. Recursive preorder follows the first chain forever and never reaches the second child at any finite index. The complete address tree is nevertheless well defined and has infinite total size. It is outside the finite coding bijection; the exploration obstruction is not dismissed as an analogous extension.

## 4. Finite total size, the minimal generating function, and conditional subtrees

<a id="gw-tree-size-pgf"></a>

\[ f(z)=\sum_{k\ge0}p_kz^k,\qquad q_n=P(N=n),\qquad G(s)=E[s^N;N<\infty]=\sum_{n\ge1}q_ns^n,\quad 0\le s\le1. \]

Only finite sizes are summed, avoiding ambiguous powers at an infinite tree size. Root decomposition, nonnegative summation, and independent subtrees give the equation below. To identify the solution, start at zero and iterate its right-hand side. The dth iterate sums precisely the weighted finite trees of height less than d. A locally finite tree of finite height has finitely many vertices, so monotone convergence gives all finite trees. Every nonnegative fixed point bounds each iterate, making the limit the smallest solution.

\[ G(s)=s f(G(s)),\qquad G(s)=\min\{z\in[0,1]:z=s f(z)\},\qquad G(1)=P(N<\infty). \]

Conditioning can also be calculated exactly. For k root children and specified positive subtree sizes, the joint probability is

\[ P\bigl(k_{\mathcal T}(\varnothing)=k,\ |\mathcal T_1|=n_1,\ldots,|\mathcal T_k|=n_k\bigr)=p_k\prod_{a=1}^{k}q_{n_a}. \]

Conditioning further on total size n retains only tuples summing to n minus one and divides by its positive size probability. Given feasible root degree and subtree sizes, shapes remain independent, each with the corresponding size-conditioned GW law: divide each finite-tree product probability by its size probability. If only total size is specified, subtree sizes share a sum constraint and are generally dependent. This division does not define a model on a zero-probability conditioning event.

## 5. Computable models and different uniform tree laws

<a id="gw-tree-examples"></a>

The following applications use the independently proved formula in [T-CYCLIC-DWASS](t-cyclic-dwass.md#dwass-formula), not the reverse. For geometric offspring the finite-tree product has a useful consequence:

\[ p_k=(1-a)a^k\ (0<a<1)\quad\Longrightarrow\quad P(\mathcal T=t)=(1-a)^n a^{n-1}\quad(|t|=n). \]

Conditionally on size n, all plane trees are thus equally likely, throughout this parameter interval, even when the unconditioned tree can be infinite. This is neither uniformity over all distinctly labeled trees nor uniformity over unordered shapes: forgetting sibling order identifies different numbers of plane realizations for different shapes.

\[ p_0=1-b,\ p_2=b\ (0<b<1):\quad P(N=2j+1)=\frac{1}{2j+1}\binom{2j+1}{j}b^j(1-b)^{j+1},\quad P(N=2j)=0. \]

Every internal vertex of a full binary tree has two children, so total size is odd. The formula asks that the iid offspring sum be one less than the vertex count; its coefficient is the jth Catalan number. Poisson offspring with parameter λ have a Poisson sum, yielding

\[ p_k=e^{-\lambda}\frac{\lambda^k}{k!},\quad \lambda>0:\qquad P(N=n)=\frac{e^{-\lambda n}(\lambda n)^{n-1}}{n!}. \]

In the supercritical case these finite-size probabilities sum to less than one, with the remainder on infinite trees; they must not be silently renormalized. At parameter zero the tree consists only of its root.

## 6. Lattice constants and the critical total-size tail

<a id="gw-tree-critical-tail"></a>

\[ E\xi=1,\quad 0<\sigma^2=\operatorname{Var}\xi<\infty,\qquad d=\gcd\{k\ge1:p_k>0\}. \]

These conditions exclude deterministic single offspring and force positive probability of zero offspring. The maximal offspring lattice span is therefore the displayed integer. Feasibility is proved in the cyclic companion; take sizes of positive probability. The lattice local CLT of Chapter 13 at a point next to the mean gives

\[ P\!\left(\sum_{i=1}^n\xi_i=n-1\right)\sim\frac{d}{\sigma\sqrt{2\pi n}},\qquad q_n\sim\frac{d}{\sigma\sqrt{2\pi}}\,n^{-3/2}\quad(n\equiv1\!\!\!\pmod d). \]

The displacement from the mean is only minus one, which vanishes after normalization, so the Gaussian exponential tends to one. Dividing by the vertex count in Dwass yields the second formula. The cyclic companion proves that all sufficiently large sizes in the correct residue class are feasible, while other residues have zero probability. The nondegenerate critical extinction theorem of Chapter 20 makes the tree finite almost surely, so its tail is the sum of these finite-size probabilities.

\[ P(N\ge n)\sim\frac{\sqrt{2/\pi}}{\sigma}\,n^{-1/2}. \]

Explicitly, bound the second asymptotic above and below with an arbitrarily small relative error at all large feasible sizes. Left and right integral bounds for the decreasing function along an arithmetic progression of spacing d give a tail asymptotic of two divided by d times the threshold to power minus one half. The local factor d cancels. Finitely many initial exceptions do not affect the tail. Parity is retained in local probabilities before it disappears in the tail sum.

By nonnegative summation, expected total size is the sum of expected generation sizes. For finite mean μ below one this is a convergent geometric series; for μ at least one it diverges. A critical tree can therefore be finite almost surely yet have infinite expected total size. These results concern size alone, not the contour limit of a conditioned tree. Return to [Chapter 52](../chapters/52-discrete-trees.md#trees-critical-size).

\[ EN=\sum_{h\ge0}EZ_h=\sum_{h\ge0}\mu^h=\begin{cases}(1-\mu)^{-1},&0\le\mu<1,\\ \infty,&1\le\mu<\infty.\end{cases} \]
