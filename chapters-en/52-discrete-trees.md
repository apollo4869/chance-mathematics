# Chapter 52: From Family Genealogies to Random Trees

A family record says: one person initially, two in the next generation, two again in the following generation, and no descendants afterwards. It determines total population and the number of generations, but not whose children the final two people are.

They could be siblings with one parent, or come from the two different families in the preceding generation. The population curves coincide while the genealogies differ. To calculate the distance between descendants along family relationships, or cut out an ancestor’s entire family branch, the population curve is insufficient. What must be retained is not merely how many vertices lie in each layer, but how they connect.

## 52.1 The same population of five can form different families

<a id="trees-two-families"></a>

Write the ancestor as the empty word, temporarily order its children as 1 and 2, and append further labels for their children. Both address lists below record five people, with generation sizes one, two, two:

\[ T_A=\{\varnothing,1,11,12,2\},\qquad T_B=\{\varnothing,1,11,2,21\}. \]

The final-generation members are siblings in the first tree and have different parents in the second. Moving between them takes two edges in the first tree, but four in the second: return to the common ancestor, then enter the other branch. This is not a difference in drawing style; the parental relationships differ.

The generation populations of Chapter 20 are a projection of the full family, suited to extinction, growth, and population martingales. Here we study the relations they cannot recover. A probability law on closed shapes from Chapter 51 likewise does not automatically specify a root, ancestral direction, or edge lengths. Parentage must first become part of the object itself.

## 52.2 Why addresses are more reliable than a drawing

<a id="trees-addresses"></a>

\[ \mathcal U=\bigcup_{h\ge0}\mathbb N_+^h,\qquad \mathbb N_+^0=\{\varnothing\}. \]

This countable set holds all potential vertices. A finite word records which child is chosen at each step from the ancestor; the empty word is the root and word length is generation. A rooted plane tree is a subset containing the root, closed under prefixes, and having at each retained vertex exactly an initial consecutive list of children:

\[ uj\in T\quad\Longleftrightarrow\quad 1\le j\le k_T(u),\qquad u\in T,\quad k_T(u)\in\mathbb N_0. \]

Here “plane” means that siblings are ordered, not that the tree must physically live in a two-dimensional plane. Child labels will specify which branch to explore first. This is added recording structure, not an intrinsic order inferred from population counts. It can be forgotten afterwards when only unordered genealogy matters, but must not be retained in one counting argument and silently discarded in another.

First consider finite trees. The probabilistic construction will also allow infinite trees with finitely many children per vertex and hence finitely many vertices in every generation. Address indicators have a countable product measurable structure, and the tree conditions are countable conditions. This gives a valid space of random objects, not merely a drawing convention. See [T-TREE-CODING](../foundations/t-tree-coding.md#coding-addresses) for measurability.

## 52.3 Ancestors and distances: relations become geometry

<a id="trees-ancestry"></a>

An address is a prefix of another exactly when it is its ancestor. Their longest common prefix is their most recent common ancestor. Give every parent–child edge length one. A connection without repeated edges must first return to that prefix and then descend along the other branch, so

\[ d_T(u,v)=|u|+|v|-2|u\wedge v|,\qquad T_u=\{w:uw\in T\}. \]

The second set cuts out a vertex and all its descendants, then removes the common address prefix, giving a tree rooted again at the empty word. Cutting out a subfamily and measuring genealogical distance are now precise operations. Tree geometry does not come from straight-line distances in a picture: nearby drawn branches may remain far apart along the tree.

## 52.4 The same offspring rule now generates the entire tree

<a id="trees-gw"></a>

Take an offspring distribution on nonnegative integers and place an independent experiment at every potential address. The root is born. A child is born only if its parent was born and its label does not exceed the parent’s experiment result. The countable product of Chapter 8 supports this construction. Results at unborn addresses do not enter the actual observation, but allow the entire experiment to be defined at once.

\[ \xi_u\overset{\mathrm{iid}}{\sim}p=(p_k)_{k\ge0},\qquad P(\mathcal T=t)=\prod_{u\in t}p_{k_t(u)}\quad(t\text{ finite}). \]

The finite-tree product requires only the specified offspring counts inside the tree. Zero offspring at leaves already prevent outside births, so no infinite list of external constraints is missing. Given the root’s offspring count, its child subtrees use disjoint independent coordinates and are independent copies of the original tree. This tree-valued branching property will justify the probabilistic decomposition of paths.

Offspring counts are finite, but their mean and the total tree size may be infinite. Chapter 20 studied generation populations and extinction. The new step is to retain all addresses and turn their relational structure into a computable path. See [T-GW-TREES](../foundations/t-gw-trees.md#gw-tree-space) for the construction and its measurability.

## 52.5 Instead of viewing everything at once, choose a traversal

<a id="trees-preorder"></a>

To compress a tree into a sequence, the first step is to choose an order rather than a formula. Visit a parent, then its first child’s entire family, then the second child’s family, and continue. This is depth-first preorder: prefixes precede their extensions and sibling labels determine their order.

\[ v_0=\varnothing,v_1,\ldots,v_{n-1},\qquad k_j=k_T(v_j),\qquad H_j=|v_j|. \]

Listing people generation by generation gives a different order, suitable for generation counts but not for making each family a consecutive interval. Preorder makes a vertex’s descendants follow it consecutively before the next family begins. This interval structure will turn ancestry into first passage along a path.

## 52.6 The path records unfinished exploration

<a id="trees-lukas"></a>

Initially there is one pending visit, the root. Visiting a vertex uses one slot and adds all its children. Keep pending addresses in order and insert new children at the front, so the current subtree is completed first. The list length changes by the offspring count minus one.

\[ S_0=0,\qquad S_{j+1}=S_j+k_j-1,\qquad Q_j=1+S_j. \]

The path value is neither generation population nor vertex depth. Adding one gives the pending count before visit j. Before the tree is finished this count cannot be zero, and afterwards no slot can remain. Thus a tree with n vertices gives

\[ S_j\ge0\ (0\le j<n),\qquad S_n=-1,\qquad S_{j+1}-S_j\ge-1. \]

This is the Łukasiewicz path. Its terminal value minus one is not a negative vertex; it results from subtracting one from the pending count. The opening examples have paths

\[ S^A=(0,1,2,1,0,-1),\qquad S^B=(0,1,1,0,0,-1). \]

## 52.7 How a legal path reconstructs a tree

<a id="trees-inverse"></a>

Now discard the original tree and retain only such an integer path. Each increment plus one is nonnegative and can be an offspring count. The correct total alone does not guarantee that all vertices can connect: the path must stay nonnegative until the end.

The inverse starts with a list containing only the root. Remove its first pending address, create as many children as the increment plus one, and insert them at the front in order. Inductively the list length before each visit is one plus the current path value. Nonnegativity prevents premature termination; the terminal value minus one empties the list exactly at the end. Every new address has one parent, so this is a plane tree. The list rule gives preorder, and every step is forced, proving uniqueness.

This is a bijection, not merely a way to describe trees. There are n increments for n vertices but n minus one edges; the path has n plus one endpoint readings. A single step from zero to minus one codes the root-only tree. See [T-TREE-CODING](../foundations/t-tree-coding.md#coding-lukas).

## 52.8 The end of a family becomes a first descent

<a id="trees-subtree"></a>

\[ r_i=\inf\{j>i:S_j=S_i-1\},\qquad |T_{v_i}|=r_i-i. \]

Just before visiting a vertex, track only pending slots belonging to its family. There is initially one, and preorder keeps this family ahead of other branches. Until its completion the local pending count is one plus the path change from the starting level. The first descent one level below that start is exactly when the family finishes. Its vertices occupy the consecutive indices before that descent.

Thus a later vertex is its descendant exactly when the path has not fallen below its starting level between the two indices:

\[ v_i\preceq v_j\ (i<j)\quad\Longleftrightarrow\quad S_i=\min_{i\le k\le j}S_k. \]

The whole ancestral partial order is contained in this one-dimensional path, not merely total size. Cutting out a subtree means taking a first-descent segment and shifting its starting level to zero. The result is another legal one-tree path.

## 52.9 Height counts earlier ancestors rather than the path value

<a id="trees-height"></a>

Depth can now be recomputed from the path. It is the number of strict ancestors, and each candidate ancestor is tested by the interval minimum just obtained. Hence

\[ H_j=\sum_{i=0}^{j-1}\mathbf1\!\left\{S_i=\min_{i\le k\le j}S_k\right\}. \]

Reading backwards from the jth path value turns these conditions into record conditions allowing ties. Ties are essential: a single-child chain has path value zero until its final leaf while depth keeps increasing. Strict records would erase the ancestral chain.

The paths serve different purposes. The Łukasiewicz path records pending visits; the height process records the current vertex’s distance from the root. Here height means discrete generation depth. General Lévy height processes require additional theory and are not established by this terminology.

## 52.10 Why heights alone still retain parentage

<a id="trees-height-inverse"></a>

\[ H_0=0,\qquad 1\le H_j\le H_{j-1}+1\quad(1\le j<n). \]

These conditions characterize finite-tree preorder heights. The next visit may enter a child, so height increases by at most one. It may return to an ancestor and enter another branch, allowing larger decreases, but cannot list the root again as a new vertex.

To reconstruct the tree keep the ancestor stack from the root to the current vertex. On reading a new height, remove vertices of at least that depth. The remaining final vertex lies one level lower; attach the new vertex as its next child. This recovers both parents and sibling order. The upper bound ensures a parent exists, positivity retains the root, and popped vertices never receive further children, making the list preorder. Each step is unique, proving sufficiency and uniqueness; see [T-TREE-CODING](../foundations/t-tree-coding.md#coding-height-inverse).

\[ H^A=(0,1,2,2,1),\qquad H^B=(0,1,2,1,2). \]

Each height occurs equally often in these two sequences, but the order and tree differ. The population curve is not the height process: it is its frequency table after order has been erased.

## 52.11 Recording returns gives the contour

<a id="trees-contour"></a>

Preorder records a vertex only on its first visit, omitting return travel. Let a walker start at the root, move at unit speed along an edge to the first child, return after completing that family, then enter the next. Each edge is traversed once in each direction. Recording distance to the root gives the contour process.

\[ C_0=C_{2(n-1)}=0,\quad C_\ell\ge0,\quad C_{\ell+1}-C_\ell\in\{-1,1\}. \]

Interpolate linearly between integers; for the root-only tree the time domain is the single point zero. This is a Dyck path of duration twice the edge count, not the n-step Łukasiewicz path. Conversely, each up-step creates the current vertex’s next new child and each down-step returns to its parent. Nonnegativity prevents a return above the root; the zero endpoint finishes every branch. Each such Dyck path therefore reconstructs a unique plane tree, as proved in [T-TREE-CODING](../foundations/t-tree-coding.md#coding-contour).

\[ C^A=(0,1,2,1,2,1,0,1,0),\qquad C^B=(0,1,2,1,0,1,2,1,0). \]

Equal maximum heights do not imply equal contours. Visiting siblings and returning to a common ancestor before entering another branch leave different return records.

## 52.12 Three clocks must be converted before comparison

<a id="trees-clocks"></a>

\[ b_j=2j-H_j,\qquad C_{b_j}=H_j\quad(0\le j<n). \]

At the contour walker’s first visit to vertex j, exactly j new edges have been discovered, giving j up-steps. Current depth is the vertex height, so down-steps number j minus that height. Adding gives the first-visit time. Between consecutive first visits the contour returns to the next vertex’s parent, then makes one up-step; after the last new vertex it returns to the root. Thus heights determine the whole contour, not merely some sampled values.

The Łukasiewicz path processes one vertex per step, the height sequence records one new vertex per entry, and the contour traverses one directed edge per step. Vertex count, edge count, and traversal duration therefore enter different formulas. The clock conversion will also affect scaling constants for large trees; plotting the curves on one horizontal axis does not make their times identical.

## 52.13 How a path minimum recovers a common ancestor

<a id="trees-distance"></a>

\[ d_T(v_i,v_j)=H_i+H_j-2\min_{b_i\le t\le b_j}C_t\qquad(i\le j). \]

Between these first visits the contour passes through the most recent common ancestor and does not move above it before the later vertex is discovered. The interval minimum is exactly its depth. The address distance formula gives the result. An ordered height curve now recovers not only branching but every distance between vertices.

Using preorder heights directly requires an essential adjustment:

\[ |v_i\wedge v_j|=\min_{i<k\le j}H_k-1\qquad(i<j). \]

The shallowest first-visited vertex in this interval is a child of the common ancestor, requiring the excluded left endpoint and subtraction of one. In the opening first tree, consecutive sibling leaves both have height two. Taking the minimum over both endpoint heights would place their common ancestor at depth two and make their distance zero. The contour is better suited to distances because it records the returns between discoveries. Both formulas are proved in [T-TREE-CODING](../foundations/t-tree-coding.md#coding-clocks-distance).

## 52.14 Tree randomness becomes independent increments until the list empties

<a id="trees-iid"></a>

Apply the same exploration to a GW tree. Offspring counts already seen determine the next address, but that address’s experiment has not been revealed. Its reading therefore still has the original offspring law. The information condition matters: the adaptively selected address must be unexamined, not chosen using its unrevealed value.

Fix a finite exploration history. Its next address is determined and has not appeared before, so coordinate independence gives its conditional law. There are countably many possible finite histories; combining them proves independence of successive readings. If the tree ends, append fresh independent readings to place its finite exploration inside a complete iid sequence. Consequently

\[ S_j=\sum_{\ell=1}^{j}(\xi_\ell-1),\qquad \xi_\ell\overset{\mathrm{iid}}{\sim}p,\qquad
|\mathcal T|\overset d=\inf\{j\ge0:S_j=-1\}. \]

This is not an approximation of a tree by a random walk. Total size is identified exactly with a first hitting time, and subtrees with consecutive first-descent segments. See [T-GW-TREES](../foundations/t-gw-trees.md#gw-tree-exploration).

## 52.15 An infinite family cannot automatically be exhausted in preorder

<a id="trees-infinite"></a>

Suppose the root has two children, with an endless single-child chain below the first and a leaf as the second. A rule that completes the first family before entering the second reaches the second child at no finite visit index.

This does not prevent the address space from defining the whole infinite tree, nor invalidate the total-size identity: an empty list at a finite time completes a finite tree; otherwise total size is infinite. What fails is the additional assertion that ordinary preorder lists every vertex in succession. The finite-tree bijection cannot be extended unchanged in this way.

The finite-size conditioning, cyclic counting, and path reconstruction below concern finite trees. The complete GW construction always allows infinite trees; finite-tree probabilities sum only to extinction probability. Keeping these levels separate prevents the survival event from being silently removed in a supercritical model.

## 52.16 Several ancestors change the initial pending count

<a id="trees-forest"></a>

\[ N^{(m)}=\sum_{a=1}^{m}|\mathcal T^{(a)}|\overset d=\tau_m,\qquad
\tau_m=\inf\{j\ge0:m+S_j=0\},\quad m\ge1. \]

Place the roots of m independent ordered GW trees in the initial pending list. Each step still uses one slot and adds offspring, but starts with m slots rather than one. The inverse algorithm gives legal finite forest paths: increments at least minus one, first reaching minus m at the terminal step and remaining strictly above it before then. A forest of n vertices has n minus m edges, not n minus one.

Each finite tree ends when the path first reaches the next lower integer level. The iid experiments restart after such a finite stopping time: on each event specifying its integer value, subsequent coordinates are independent of previous coordinates, and summing proves the claim. No unexplained strong Markov hypothesis is needed. See [T-GW-TREES](../foundations/t-gw-trees.md#gw-tree-forest).

## 52.17 Why the correct endpoint does not yet give a tree

<a id="trees-first-minimum"></a>

Sums of iid offspring are easy to calculate, but a tree must not exhaust its slots prematurely. Offspring counts zero, one, one sum to two, the correct total for three vertices. In that order the root has no children, leaving nowhere to attach the remaining readings. Rotating to one, one, zero gives a three-vertex chain.

\[ S_n=-1,\qquad r=\min\operatorname*{arg\,min}_{0\le j<n}S_j. \]

For increments at least minus one with total minus one, cut at the first minimum of the preterminal sums and move the latter part to the front. This gives a legal one-tree path. Values after the cut minus the minimum are nonnegative. After wrapping, earlier values exceed the first minimum by at least one, canceling the total minus one. The first occurrence is essential: cutting minus one, zero, zero at its last minimum gives zero, minus one, zero and still ends prematurely.

This finds a legal cut. Counting also needs its uniqueness and the number of legal cuts for several ancestors. The answer comes from downward movement crossing integer levels one at a time, not from every ordering being a tree.

## 52.18 The cycle lemma counts cuts rather than distinct words

<a id="trees-cycle"></a>

\[ a_i\ge-1,\quad a_i\in\mathbb Z,\quad\sum_{i=1}^{n}a_i=-m,\quad1\le m\le n
\quad\Longrightarrow\quad\#\{\text{legal indexed cuts}\}=m. \]

Legality means that rotated partial sums stay strictly above minus m before the end. The mechanism is visible on a two-sided extension: repeat increments periodically, so cumulative sums decrease by m every n steps. They tend to positive infinity to the left and negative infinity to the right. Each integer level has a global first hitting time. Cutting there is legal because the level m lower is first hit exactly one period later.

\[ S_{j+n}=S_j-m,\qquad t_h=\min\{j\in\mathbb Z:S_j=h\},\qquad t_{h-m}=t_h+n. \]

Conversely, translate any time preceding a legal cut into the current period. Adding back the corresponding multiples of m shows that its old value was strictly higher than the cut value. Legal cuts are therefore precisely global first hits. Levels modulo m correspond bijectively to cuts modulo n, giving exactly m. The full reverse inequality is proved in [T-CYCLIC-DWASS](../foundations/t-cyclic-dwass.md#cycle-indexed).

If every increment is minus one and m equals n, all indexed cuts are legal but produce only one distinct word. The integer factor comes from indexed cyclic operations; it cannot be retained unchanged after ignoring periodic repetitions.

## 52.19 Dwass’s formula turns total family size into an iid sum

<a id="trees-dwass"></a>

Apply the lemma to an iid offspring string. A string ending at minus m has m legal cuts. Every indexed rotation has the same law, so the probability of each legal cut with this endpoint equals the original walk’s probability of first reaching minus m at step n. Therefore

\[ nP(\tau_m=n)=mP(S_n=-m),\qquad
P(N^{(m)}=n)=\frac mn P\!\left(\sum_{i=1}^{n}\xi_i=n-m\right),\quad n\ge m\ge1. \]

This is the Dwass total-progeny formula. A forest probability is reduced to an ordinary iid sum. No finite mean or almost-sure extinction is required; infinite total size is kept separately. The proof never divides by endpoint probability, so an impossible endpoint correctly gives zero rather than forcing a conditional tree onto a null event.

Dwass’s 1969 paper studied total progeny and a related random walk. Here the proof is reconstructed through indexed cyclic cuts; the whole modern tree-coding narrative is not attributed retrospectively to that paper. See the [original publication record](https://doi.org/10.2307/3212112) and the complete argument in [T-CYCLIC-DWASS](../foundations/t-cyclic-dwass.md#dwass-formula).

## 52.20 Some sizes admit no tree at all

<a id="trees-feasibility"></a>

\[ P(N=n)>0\quad\Longleftrightarrow\quad
\exists k_1,\ldots,k_n\in\operatorname{supp}p:\ \sum_{i=1}^{n}k_i=n-1. \]

Necessity is the edge count; sufficiency is the unique legal cut of a positive-weight offspring word. If zero offspring is impossible, each vertex has a child and the tree cannot be finite. If only zero offspring is possible, there is only the root. Otherwise zero is in the support. The greatest common divisor of positive support values gives the required residue:

\[ d=\gcd\{k\ge1:p_k>0\},\qquad n\equiv1\pmod d. \]

This is also the maximal offspring lattice span. The correct residue need not suffice at small sizes: with support zero, four, six, size three is odd but its required offspring sum two is impossible. All sufficiently large sizes in the correct residue are feasible: finitely many support values already have that greatest common divisor, and their nonnegative combinations eventually fill the residue class; zeros fill the remaining entries. The integer-semigroup argument is proved in [T-CYCLIC-DWASS](../foundations/t-cyclic-dwass.md#dwass-feasibility).

Full binary families have odd total size; a deterministic single-child chain has no finite total size. These are not exceptions to the formula but feasibility information recorded by its iid sum. Conditional models and later local limits must use genuinely feasible sizes.

## 52.21 The same cut argument counts tree shapes

<a id="trees-profiles"></a>

\[ \sum_k n_k=n,\qquad\sum_k k n_k=n-1,\qquad
\#\{\text{plane trees with degree profile }(n_k)\}=\frac1n\frac{n!}{\prod_k n_k!}. \]

Fix how often each offspring count occurs. There are multinomially many orderings. Every ordering has one legal indexed cut, while every legal word corresponds to n pairs of an original ordering and a cut. Divide by n. This is double counting, not an assumption about equal rotation-orbit sizes. The coding bijection converts words into trees.

\[ \#\{t:|t|=n\}=\frac1n\binom{2n-2}{n-1}. \]

Combining all nonnegative offspring words with total n minus one, stars-and-bars gives the binomial coefficient; dividing by n yields a Catalan number. If every internal vertex has r children and there are j internal vertices, total size is r times j plus one, giving full multiway-tree counts by substitution. See [T-CYCLIC-DWASS](../foundations/t-cyclic-dwass.md#dwass-profiles), including conditional degree-profile laws.

These counts retain the root and sibling order throughout. An unordered shape can have multiple plane realizations, so uniform plane trees and uniform unordered trees are different random models.

## 52.22 A conditioned tree is not a walk bridge, but is an exact rotation of one

<a id="trees-conditioned"></a>

Conditional on total size n, a preorder offspring string must have the correct sum and exhaust its slots only at the last step. An iid string conditioned merely on sum n minus one need not satisfy the latter. The first-minimum cut supplies exactly what is missing.

When the endpoint event has positive probability, sample the conditioned iid string, rotate its increment path at the first minimum, and reconstruct the tree. This gives the size-conditioned GW law. To check the bias, an integer word of total minus one cannot repeat periodically, since the repetition count would divide minus one. Every legal word has n distinct rotated preimages with identical product weights, giving probability

\[ \frac{n\prod_i p_{k_i}}{P(\sum_{i=1}^n\xi_i=n-1)}
=\frac{\prod_i p_{k_i}}{P(N=n)}. \]

This finite-size identity genuinely links conditioned random trees and conditioned random walks. It does not prove a large-tree path limit: the conditioning event changes with size, its probability becomes small, and the minimum cut, heights, and contours still need control. See [T-CYCLIC-DWASS](../foundations/t-cyclic-dwass.md#dwass-conditioned).

## 52.23 Conditioning retains the branching rule but changes subtree dependence

<a id="trees-conditioned-branching"></a>

\[ P(k_{\mathcal T}(\varnothing)=k,\ |\mathcal T_1|=n_1,\ldots,|\mathcal T_k|=n_k)
=p_k\prod_{a=1}^{k}q_{n_a},\qquad q_n=P(N=n). \]

Root subtrees are independent without conditioning. Given total size n, their sizes must sum to n minus one and are generally dependent. Given a feasible root offspring count and all subtree sizes as well, their shapes become independent, each with its own size-conditioned GW law. This follows from the displayed probabilities and finite-tree product weights, rather than carrying the unconditioned branching property unchanged into a conditional model.

Generating a tree from independent coordinates and imposing a global restriction on that tree are different operations. Coding makes the distinction visible: previously independent experiments must jointly satisfy a first-passage constraint after total size is fixed.

## 52.24 When a conditioned tree is exactly uniform

<a id="trees-models"></a>

\[ p_k=(1-a)a^k,\quad0<a<1
\quad\Longrightarrow\quad P(\mathcal T=t)=(1-a)^n a^{n-1}\quad(|t|=n). \]

For geometric offspring, the finite-tree product weight depends only on total offspring, already determined by vertex count. Conditional on size, all plane trees are equally likely. This remains true when the geometric mean exceeds one and the unconditioned tree can be infinite. Offspring experiments thus produce uniform combinatorial plane trees, but the uniformity depends on the weights and is not shared by every GW model.

\[ \xi\sim\operatorname{Poisson}(\lambda),\quad\lambda>0
\quad\Longrightarrow\quad q_n=\frac{e^{-\lambda n}(\lambda n)^{n-1}}{n!}. \]

For Poisson offspring, substitute a Poisson variable with parameter equal to vertex count times λ into Dwass’s formula. In the supercritical case finite-size probabilities do not sum to one, the remainder representing infinite families. At zero parameter there is only the root. Full binary models and lattice zeros are similarly explicit in [T-GW-TREES](../foundations/t-gw-trees.md#gw-tree-examples).

## 52.25 A total-size equation still needs its smallest solution

<a id="trees-size-pgf"></a>

\[ f(z)=\sum_{k\ge0}p_kz^k,\qquad G(s)=\sum_{n\ge1}q_ns^n,\qquad G(s)=s f(G(s)),\quad0\le s\le1. \]

The root contributes one vertex and each child an independent tree, giving this equation. The equation alone does not select its solution. Starting at zero and iterating the right-hand side retains trees of height less than d at iteration d. Every finite tree is eventually included, and local finiteness plus bounded height implies finiteness. Monotone convergence gives all finite trees, while every fixed point bounds the iterates, selecting the smallest nonnegative solution.

At argument one this is extinction probability, not necessarily one. The smallest fixed point from Chapter 20 now has another concrete interpretation: the sum of product weights of all finite trees. The same generating function is revisited, but the new result connects total tree size, finite-tree conditioning, and path enumeration. See [T-GW-TREES](../foundations/t-gw-trees.md#gw-tree-size-pgf).

## 52.26 Why critical total-size probabilities have exponent three halves

<a id="trees-critical-size"></a>

Now take critical, nondegenerate offspring with finite variance. Zero offspring has positive probability and the tree is finite almost surely, but expected total size need not be finite. Dwass gives the local CLT a new role:

\[ E\xi=1,\quad0<\sigma^2=\operatorname{Var}\xi<\infty,\qquad
q_n=\frac1n P\!\left(\sum_{i=1}^n\xi_i=n-1\right)
\sim\frac{d}{\sigma\sqrt{2\pi}}\,n^{-3/2}\quad(n\equiv1\!\!\!\pmod d). \]

An iid sum lands near its mean at one allowed lattice point with probability of order vertex count to power minus one half. The cyclic constraint contributes another inverse vertex count, producing minus three halves. The span factor matters: full binary trees have only odd sizes, and allowed local probabilities compensate for that sparsity. The local CLT of Chapter 13 supplies the factor, while the displacement minus one from the mean makes the Gaussian exponential tend to one.

\[ P(N\ge n)\sim\frac{\sqrt{2/\pi}}{\sigma}\,n^{-1/2},\qquad EN=\infty. \]

Summing local probabilities along the allowed residue class cancels the span factor through lattice spacing, giving the tail. Full integral bounds are in [T-GW-TREES](../foundations/t-gw-trees.md#gw-tree-critical-tail). Almost-sure finiteness with infinite mean is a consequence of this calculable heavy tail; no continuous limit for tree height or contour has yet been asserted.

## 52.27 What the path preserves and what remains

<a id="trees-insight"></a>

The opening population records still coincide, but we can now identify what they omit: parents, subtree boundaries, common ancestors, and tree distances. A complete legal encoding recovers them all. Writing a tree as a one-dimensional path does not remove branching; it translates branching into visit order, first descents, weak records, and return minima.

The translation also gives new probabilistic tools. Total size becomes first passage for an iid sum; the cycle lemma supplies exact probabilities and conditional sampling; branching becomes decomposition into path segments. Legality conditions are substantive: removing first passage leaves unattached offspring, strict records lose ancestors, and mixing clocks gives wrong distances.

The large-tree problem can now be posed precisely. A finite tree conditioned on a large feasible size is exactly a particular conditioned path. Ordinary walk limits do not handle this increasingly rare restriction or control heights and returns. The next task is a whole-path conditioned limit, not a drawing of a bigger tree. Only afterwards can a continuous curve legitimately be used to construct tree geometry.

Complete discrete proofs are in [T-TREE-CODING](../foundations/t-tree-coding.md), [T-GW-TREES](../foundations/t-gw-trees.md), and [T-CYCLIC-DWASS](../foundations/t-cyclic-dwass.md). Source checks use [Dwass’s original 1969 publication record](https://doi.org/10.2307/3212112) and [Le Gall’s 2005 author survey](https://arxiv.org/abs/math/0511515). Addresses, inverse list algorithms, indexed cuts, and distance counterexamples are organized here as a modern proof for this book’s problem sequence. Continuous scaling limits and general Lévy height processes are not counted as established in this chapter.
