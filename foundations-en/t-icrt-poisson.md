# T-ICRT-POISSON: Repeat Clocks, Grafting and the Compactness Boundary

Return to [Chapter 58](../chapters/58-multifurcation.md). The model is the public construction in Section 2 of [Aldous–Pitman, PTRF118(2000),455–482](https://www.stat.berkeley.edu/~pitman/525.pdf). Full ICRT mass classification and additive-coalescent entrance boundaries are not counted as proved here.

## 1. Diffuse grafting versus repeated hubs

<a id="ic-clocks"></a>

\[ \theta_i\ge0,\quad \theta_0^2+\sum_{i\ge1}\theta_i^2=1. \]

The standard ICRT family additionally requires \(\theta_0>0\) or \(\sum_{i\ge1}\theta_i=\infty\); ranking the positive-index parameters is a representation convention. We first prove clock and grafting lemmas on the relaxed normalized square-summable domain. These lemmas are not the general ICRT mass or compactness theorem. The single-hub example in Section 4 deliberately lies outside the standard domain.

Independently take a Poisson process of intensity \(\theta_0^2 dx\,dy\) on \(\{(x,y):0<y<x\}\), and Poisson arrival times \(\xi_{i,1}<\xi_{i,2}<\cdots\) of rate θᵢ for every i≥1. A triangular point has cutpoint x and joinpoint y. Type i uses only arrivals j≥2 as cutpoints, always joining at \(\xi_{i,1}\). The first arrival is not a cutpoint.

The expected number of type-i cutpoints in [0,R] is \(\theta_i R-(1-e^{-\theta_i R})\le\theta_i^2R^2/2\). Triangular points have mean \(\theta_0^2R^2/2\). The total mean is at most R²/2, hence cutpoints are locally finite almost surely. Independent continuous times and a countable union exclude ties. A positive-rate type has infinitely many cuts, as does the triangular process alone. Thus \(0<\eta_1<\eta_2<\cdots\uparrow\infty\).

## 2. Finite trees, completion and infinite degree

<a id="ic-tree"></a>

Start from [0,η₁]. At cut j attach \((\eta_j,\eta_{j+1}]\) at its joinpoint. The latter is below the cutpoint and already represented. Each step adds a positive pendant segment and preserves old distances, producing a compact finite real tree. Measurable enumeration of finite-window Poisson configurations and finite distance formulas make every step measurable. The union is separable and its completion is a real tree: Chapter 57’s completion lemma uses unique arcs and the four-point inequality; completeness and approximate midpoints give geodesics, without requiring total boundedness.

If θᵢ>0, every subsequent type-i graft uses one hub. The positive new branches occupy distinct components after its deletion; future grafting does not identify old points, nor does completion identify points at positive distance. The hub has countably infinite degree. Triangular joinpoints are distinct and avoid the hubs, giving ordinary binary insertions at finite stages. A fixed k cannot describe both mechanisms.

## 3. The first-repeat distribution

<a id="ic-repeat"></a>

\[ P(\eta_1>t)=\exp(-\theta_0^2t^2/2)
\prod_{i\ge1}(1+\theta_i t)e^{-\theta_i t}. \]

No cut means no triangular point with x≤t and at most one arrival from each Poisson clock before t. Independence gives finite products; continuity of decreasing events gives the infinite product. It converges to a positive value for finite t, because \(0\le u-\log(1+u)\le u^2/2\) and the squares are summable. This separates the diffuse Brownian part from persistent weights; equal sums of squares do not make all parameter vectors equivalent.

## 4. A counterexample exposing a parameter boundary

<a id="ic-boundary"></a>

Relax the parameters and take θ₁=1 and all others zero. This violates the standard ICRT domain, so it tests only the boundary of the grafting algorithm. Every branch joins the same hub. Consecutive cutpoint gaps are iid Exp(1); infinitely many exceed 1 almost surely. Points at distance 1 along those branches are pairwise distance 2, so the ball has no finite 1/2-net. The completion is neither locally compact nor compact.

Published ICRT theory imposes extra conditions: Aldous–Pitman use \(\theta_0>0\) or \(\sum_{i\ge1}\theta_i=\infty\), and construct mass separately. Even within that parameter domain, general objects cannot be placed in the book’s compact GHP space without checking compactness. We fully prove finite grafting, real-tree completion, hubs and the first-cut law. General mass construction, sampling consistency, compactness classification and unequal-birthday-tree limit identification do not have complete book proofs here. At θ₀=1 the diffuse clock is rdr, the 2e convention of Chapter 57. Standard e requires halving lengths, equivalently a 4rdr clock.
