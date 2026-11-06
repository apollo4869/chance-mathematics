# T-PUBLIC-KARY-GROWTH: A Published Edge-Growth Model and Persistent-Vertex Mass

Return to [Chapter 58](../chapters/58-multifurcation.md). We reconstruct the finite Haas–Stephenson model and its urn consequences; the boundary concerning its whole-tree scaling proof is explicit below.

## 1. The operation at each step

<a id="kg-rule"></a>

Fix \(k\ge2\). Start with one root edge \(G_0\). Given \(G_n\), choose one of its edges uniformly, insert a vertex to replace it by two edges, and attach \(k-1\) new edges there. Each combinatorial edge has length 1: splitting does not preserve the old real edge length isometrically. A fixed insertion convention can retain plane order; the undirected counts below do not depend on it. Finite measurable transition kernels and independent uniforms construct all steps.

\[ |E(G_n)|=kn+1,\qquad |\mathrm{Leaves}(G_n)|=(k-1)n+1,\qquad |\mathrm{Internal}(G_n)|=n. \]

Inductively, one step adds k edges, k−1 leaves and one internal vertex. The root endpoint is not counted as a leaf. At k=2 this is Rémy-type binary edge growth. For k≥3 leaves arrive in batches; birth labels are not iid mass-sampling labels. Deleting the newest batch and suppressing its new vertex recovers the preceding tree, which is birth-order consistency rather than arbitrary uniform-leaf deletion consistency.

## 2. All directions at the first branch point

<a id="kg-urn"></a>

Fix the first inserted vertex v. Its removal leaves \(k+1\) directions numbered \(0,\ldots,k\), with direction 0 towards the root. Each initially has one edge in \(G_1\). Let \(N_i(n)\) count operations in direction i during steps 2 through n. Then \(E_i(n)=1+kN_i(n)\), and \(\sum_iN_i(n)=n-1\). Edges adjacent to v retain their direction under subsequent splitting.

\[ P(\text{next direction}=i\mid G_n)=\frac{1+kN_i(n)}{kn+1}. \]

This is an urn with initial weights 1 and reinforcement k. For a direction word of length m containing \(m_i\) occurrences of each direction, its probability is exactly

\[ \frac{\prod_{i=0}^{k}\prod_{j=0}^{m_i-1}(1+kj)}{\prod_{j=0}^{m-1}(k+1+kj)}
=\frac{\Gamma((k+1)/k)}{\Gamma((k+1)/k+m)}
\prod_{i=0}^{k}\frac{\Gamma(1/k+m_i)}{\Gamma(1/k)}. \]

The right side is the integral of iid direction words against a Dirichlet\((1/k,\ldots,1/k)\) law, by the Dirichlet integral proved in Chapter 44. Finite-dimensional uniqueness and the conditional strong law give an almost sure limit on the original growth space:

\[ \frac{N_i(n)}n\longrightarrow D_i,\qquad (D_0,\ldots,D_k)\sim\operatorname{Dirichlet}(\underbrace{1/k,\ldots,1/k}_{k+1}). \]

## 3. Leaf mass, conditional structure and invalid extrapolations

<a id="kg-leaves"></a>

For \(i\ge1\), the number of leaves in direction i is \(1+(k-1)N_i(n)\); towards the root it is \((k-1)N_0(n)\). Division by \((k-1)n+1\) gives the same limits \(D_i\). Edge and leaf counts were calculated separately, not equated at finite n. Conditional on the full sequence of chosen directions, the edge is uniform within the chosen component. Independent internal uniforms realize the resulting product of component transition kernels.

This Dirichlet result concerns empirical leaf mass at a persistent discrete vertex. It does not prove the scale of the diameter, GHP tightness, or identification of that vertex in a continuum limit. An urn calculation cannot supply those conclusions. Haas–Stephenson prove a distinct whole-tree continuum limit; our finite argument is an independently checkable part of that model.

## 4. The published theorem and the remaining proof obligation

<a id="kg-public"></a>

[Haas–Stephenson, Ann. IHP 51 (2015), 1314–1341](https://archive.numdam.org/articles/10.1214/14-AIHP622/), [public full text](https://www.math.univ-paris13.fr/~haas/AIHPB2015514.pdf), Theorem 1.1, prove GHP convergence in probability of unit-edge \(n^{-1/k}G_n\), with uniform leaf mass, to a k-ary self-similar fragmentation tree under the natural growth coupling. Here n counts inserted internal vertices, not the total vertex count used for conditioned GW trees.

This whole-tree scaling theorem is presented as a sourced external theorem, not counted as fully reproved here. The splitting-measure limit, spatial tightness for Markov branching trees and control of the full tree by finite retained trees still lack complete book proofs. Even k=2 requires an explicit normalization comparison with standard e. These are substantive coverage limits, not merely unsigned expert reviews.
