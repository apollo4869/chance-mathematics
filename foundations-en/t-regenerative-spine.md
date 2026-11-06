# T-REGENERATIVE-SPINE: CRP Growth, Brownian Spines and Regenerative Decomposition

This page proves the concrete growth and regeneration claims of [Chapter 57](../chapters/57-regenerative-growth.md#growth-spinal-crp). Write Nₖ=(2k−3)!! and N₁=1 for nonplane leaf-labeled binary shapes with a planted root edge. The CRP discount is a, distinct from Chapter 56’s self-similar time index α. No general classification of non-Brownian continuous regenerative trees is claimed.

## 1. How metric growth chooses an edge after lengths are forgotten

<a id="regen-uniform-edges"></a>

By the line-breaking density, conditional on shape and total length the 2k−1 edge proportions are Dirichlet(1,…,1), independently of both. Length-uniform attachment therefore chooses each edge with probability 1/(2k−1) after lengths are forgotten. Earlier shapes are deletions of the current labeled shape, so this is also the conditional rule given shape history. Unique deletion of the newest leaf gives probability 1/[Nₖ(2k−1)]=1/Nₖ₊₁ for every new shape.

Uniform edges describe the shape kernel, not the metric kernel conditional on actual lengths; that kernel must be length-weighted. Independently orienting the two children gives the following root-size law. Conditional on the actual label split, the two shapes are independent uniform trees, so the family satisfies the full Markov branching condition.

\[ q_n(i)=\frac{\binom ni N_iN_{n-i}}{2N_n},\qquad1\le i<n,\quad n\ge2. \]

## 2. An ordered forest along the spine to label 1

<a id="regen-forest-count"></a>

Put m=k−1. Along the root-to-leaf-1 path, list side-subtree label blocks \(B_1,\ldots,B_b\) from root toward the leaf, with sizes nⱼ partitioning {2,…,k}. An ordered label partition and a binary tree on each block reconstruct the whole shape by successive grafts along the spine and a terminal leaf 1. The decomposition is unique in both directions, giving the probability below for a specified ordered label partition.

\[ P(B_1,\ldots,B_b\text{ in spinal order})=\frac{\prod_{j=1}^bN_{n_j}}{N_{m+1}}. \]

Conditional on that partition, side shapes are independent uniform trees since every shape combination is equally likely. Forgetting spinal order gives b! orders of the distinct label blocks, hence EPPF b!∏Nₙⱼ/Nₘ₊₁. Equal block sizes do not identify different labeled blocks, so no extra factorial is divided out.

## 3. The CRP parameters follow from edge counts

<a id="regen-crp"></a>

\[ P(\text{join block }j)=\frac{2n_j-1}{2m+1}=\frac{n_j-1/2}{m+1/2},\qquad P(\text{new block})=\frac{b+1}{2m+1}. \]

Side block j, including its stem from the spine, has 2nⱼ−1 edges; the spine itself has b+1 edges. Choosing a side edge joins that block, while choosing a spinal edge creates a new block in that gap. Their sum is 2m+1, yielding CRP(1/2,1/2) from actual tree growth. At m=0 the first block opens with probability one. Uniform insertion among gaps makes geometric order uniform given the unordered partition; discovery order instead follows first observation and is different.

\[ p_{1/2,1/2}(n_1,\ldots,n_b)=\frac{b!\prod_j(2n_j-3)!!}{(2m-1)!!}. \]

Substituting a=θ=1/2 into Chapter 47’s two-parameter EPPF and converting rising factorials to double factorials gives exactly this count. The direction is from an identified tree law to prediction, not from a guessed parameter to a CRT.

## 4. After the first side block is removed, the remainder restarts

<a id="regen-decrement"></a>

\[ r(m,j)=\binom mj\frac{N_jN_{m-j+1}}{N_{m+1}},\qquad1\le j\le m. \]

Choose the j labels of the first root-side block, its Nⱼ shapes and the remaining Nₘ₋ⱼ₊₁ shapes containing label 1. The cases exhaust all trees, proving that r sums to one. Conditional on the first block’s actual labels, its tree and the remaining marked tree are independent uniform trees. Remove the block and suppress its spinal vertex; the remainder restarts with m−j other labels. Iteration gives the regenerative composition formula.

\[ P(C_m=(n_1,\ldots,n_b))=\prod_{j=1}^b r\!\left(m-\sum_{i<j}n_i,n_j\right). \]

This is finite-sample regeneration. It does not assert that an infinite CRT has a first positive-mass side branch counted from the root; branching can accumulate there and the first finite-sample block may have vanishing limiting mass. Recursion in remaining label count is not an unproved iid spacing statement in physical length.

## 5. The full finite metric spinal decomposition

<a id="regen-metric"></a>

\[ \left(\frac{A_1}{L},\ldots,\frac{A_b}{L},\frac{H}{L}\right)\ \sim\ \operatorname{Dirichlet}(2n_1-1,\ldots,2n_b-1,b+1),\qquad2L^2\sim\operatorname{Gamma}(m+1,1). \]

Aⱼ denotes finite side-tree skeleton length and H spinal length, not full-component probability mass. Conditional on the ordered partition, choose independent uniform side shapes and an independent L. Independent Exp(1) variables normalized by their sum realize all-edge Dirichlet(1,…,1). Group them into side trees and spine. The transformation Gᵢ=S pᵢ has Jacobian S^(d−1); the product exponential density factors into a Gamma group sum and independent Dirichlet proportions. Thus dimensions 2nⱼ−1 and b+1 give the displayed law.

Given group totals, within-side-tree edge proportions and the b+1 spinal proportions are independent uniform simplices. Reassemble in spinal order to recover exactly Rₘ₊₁. This is a complete finite metric disintegration and reconstruction. Group totals are dependent through their common sum, and Aⱼ/L is not the frequency Pⱼ below.

## 6. Actual mass frequencies along a continuum spine

<a id="regen-mass"></a>

In the closed Brownian construction take an independent mass leaf ξ₁ and remove the closed spine [ρ,ξ₁]. Its complementary components are open and countable by separability; every nonempty component has positive mass by full support. Chapter 54’s leaf-supported nonatomic mass gives μ([ρ,ξ₁])=0, so their masses sum to one. Conditional on the tree and ξ₁, iid mass samples identify every component frequency simultaneously by the strong law. Side blocks in finite reduced trees are exactly their restrictions, using unique arcs and Brownian binary branching.

\[ P_j=V_j\prod_{i<j}(1-V_i),\qquad V_j\sim\operatorname{Beta}\left(\tfrac12,\tfrac{j+1}2\right)\text{ independently};\qquad (P_j)^{\downarrow}\sim\operatorname{PD}(1/2,1/2). \]

The finite side partition is CRP(1/2,1/2), so Chapter 47’s proved deletion, Beta-cutting and total-mass results give discovery-order GEM and ranked PD frequencies. The first discovered component, selected by ξ₂, is size-biased; E P₁=1/3 equals the probability that two extra samples enter the same side component. This proves a concrete continuum spinal mass statement. It does not assert an unproved conditional law of independent scaled CRT geometries given all component frequencies.

## 7. A valid recursive growth family without assumed exchangeability

<a id="regen-general-growth"></a>

\[ 0<a<1,\quad\theta>0:\qquad \text{root-edge weight }a,\quad \text{off-spine subtree weight }u-a,\quad \text{marked subtree weight }v-1+\theta. \]

At a binary tree with n=u+v leaves, mark the child containing the smallest label and let the other have u leaves. Select the root edge or a child with these weights, totaling n−1+θ; recursively apply the rule inside a selected child until an edge is chosen. A singleton tree has just its unique edge. Split that edge and add the new leaf, specifying shape but no lengths. Weights are positive and recursion decreases size, so each step is a valid finite Markov kernel, and countably many uniforms construct infinite growth. Deleting the newest label recovers the previous tree pathwise, which is not yet arbitrary sampling consistency.

## 8. The recursion really induces the two-parameter CRP

<a id="regen-general-crp"></a>

\[ P(\text{join }j)=\frac{n_j-a}{m+\theta},\qquad P(\text{new})=\frac{\theta+ab}{m+\theta}. \]

Expanding the recursion along the spine to leaf 1, the weight of a marked child cancels the next level’s total denominator. Side subtree j therefore has total weight nⱼ−a, each gap before an existing branch has weight a, and the terminal gap has weight θ. Summing gap weights proves the CRP probabilities. Inside a selected side tree, independent random numbers run the same recursion; external allocation depends only on sizes, giving independent internal growth conditional on allocation history. The discount a has not been identified with any geometric scaling index.

Chapter 47’s EPPF proves exchangeability of the side partition and its GEM(a,θ) frequencies. But the whole three-leaf tree has the following cherry probabilities. Exchangeability of all labels requires equality, forcing a=θ=1/2. In that case counting root-side and subtree edges inductively shows the recursion is uniform-edge growth, returning to the first section. For other parameters, consistency under deletion of the newest label does not make birth labels iid mass samples.

\[ P(\{1,2\}\text{ cherry})=\frac a{1+\theta},\quad P(\{1,3\}\text{ cherry})=\frac\theta{1+\theta},\quad P(\{2,3\}\text{ cherry})=\frac{1-a}{1+\theta}. \]

## 9. The exact boundary of regeneration claims

<a id="regen-scope"></a>

Proved here are Brownian consistent Markov branching shapes, complete finite metric spinal disintegration and reconstruction, the regenerative decrement r, continuum PD(1/2,1/2) spinal masses, recursive CRP growth in the stated parameter range and the three-leaf exchangeability test. General non-Brownian compact CRT limits, a full conditional independent-scaling theorem for continuous side geometries and general regenerative CRT classification are not proved by GEM frequencies. Pitman–Winkel study a broader family and distinguish weak from strong sampling consistency. Failure of birth-label exchangeability here does not imply that every corresponding delabeled family fails weak consistency. [Return to the chapter](../chapters/57-regenerative-growth.md#growth-crp-boundary).
