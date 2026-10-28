# T-LP: Integration Tools for Sums, Products and Limits

This page supplies the analysis required for Chapter 15's maximal inequalities. The first three sections hold on arbitrary measure spaces; the last explicitly concerns probability spaces. Functions here are real-valued; completeness of the measure is not assumed, and functions are identified almost everywhere. These full written proofs remain subject to mathematical revision.

<a id="t-lp-holder"></a>

## Why two different moments control a product

Let 1<p<∞ and q=p/(p−1). For a,b≥0, maximizing ab−a^p/p gives the maximizer \(a=b^{q-1}\), hence

\[
ab\le a^p/p+b^q/q.
\]

If f∈L^p and g∈L^q have nonzero norms, substitute a=|f|/‖f‖\_p and b=|g|/‖g‖\_q and integrate. The two terms sum to 1, giving

\[
\int|fg|\,d\mu\le\|f\|_p\|g\|_q.
\]

If either norm is zero, its function vanishes almost everywhere and the conclusion still holds. For p=1 and q=∞, integrate the almost everywhere bound |g|≤‖g‖\_∞ directly; exchange f and g for the other endpoint. This proves the required Hölder inequality on arbitrary measure spaces.

<a id="t-lp-minkowski"></a>

## From a product estimate to the triangle inequality

For 1<p<∞, convexity first gives \(|f+g|^p\le2^{p-1}(|f|^p+|g|^p)\), so f+g belongs to L^p whenever f and g do. This first ensures that the following integrals make sense: we must not divide by a potentially infinite norm before establishing integrability. Set S=|f+g|. Hölder gives

\[
\int S^p\,d\mu\le\int(|f|+|g|)S^{p-1}\,d\mu
\le(\|f\|_p+\|g\|_p)\|S\|_p^{p-1}.
\]

If ‖S‖\_p>0, divide by the finite quantity \(\|S\|_p^{p-1}\) to obtain \(\|f+g\|_p\le\|f\|_p+\|g\|_p\); a zero norm is immediate. For p=1 use the pointwise triangle inequality, and for p=∞ use essential bounds. This proves Minkowski for all 1≤p≤∞.

<a id="t-lp-complete"></a>

## How a Cauchy sequence actually finds a measurable limit

Let 1≤p<∞ and let f\_n be Cauchy in L^p. Extract a subsequence \(f_{n_j}\) with consecutive differences of L^p norm at most \(2^{-j}\). Finite applications of Minkowski followed by monotone convergence for the nonnegative integral give

\[
\left\|\sum_{j=1}^m|f_{n_{j+1}}-f_{n_j}|\right\|_p
\le\sum_{j=1}^m2^{-j}\le1,
\qquad
\int\left(\sum_{j=1}^\infty|f_{n_{j+1}}-f_{n_j}|\right)^p d\mu\le1.
\]

Thus the absolute difference series is finite almost everywhere. Define f as \(f_{n_1}\) plus the sum of those consecutive differences, setting it to zero on the measurable exceptional null set. This is measurable; the same estimate and Minkowski show that f∈L^p. Apply Minkowski to finite tail sums and then Fatou to obtain

\[
\|f-f_{n_j}\|_p\le\sum_{k=j}^\infty2^{-k}\longrightarrow0.
\]

Because the original sequence is Cauchy, for any ε>0 first choose j with subsequence error below ε/2, then use the Cauchy property to control \(f_n-f_{n_j}\). The whole sequence converges to f. This proves Riesz–Fischer completeness for 1≤p<∞, rather than merely convergence of an extracted subsequence.

For p=∞, again extract a subsequence whose consecutive L∞ differences are at most \(2^{-j}\). Outside the union of their exceptional null sets, also removing the set where the first term exceeds its finite essential bound, all differences obey a uniformly summable bound, so the subsequence converges uniformly to a bounded function. Set it to zero on the measurable exceptional set to obtain a measurable essentially bounded representative. The tail estimate gives L∞ convergence, and the original Cauchy property gives convergence of the whole sequence. Thus L^p is complete for every 1≤p≤∞.

<a id="t-lp-probability"></a>

## Approximation, conditional averaging and norm identification on a probability space

Here μ=P. For f∈L^p, 1≤p<∞, truncation \(f^{(K)}=f\mathbf1_{\{|f|\le K\}}\) satisfies \(\|f-f^{(K)}\|_p\to0\), since its pth tail integral tends to zero. Approximate each bounded real measurable function by step functions of mesh \(2^{-m}\), with pointwise error at most \(2^{-m}\). Total probability 1 makes their L^p errors at most \(2^{-m}\) as well. Bounded simple functions are therefore dense in these L^p spaces.

Hölder also gives L^p⊂L¹. Conditional Jensen from Chapter 9 and the order property of conditional averages consequently give contraction for every 1≤p≤∞:

\[
\|\mathbb E[f\mid\mathcal G]\|_p\le\|f\|_p.
\]

For finite p, integrate \(|\mathbb E[f\mid\mathcal G]|^p\le\mathbb E[|f|^p\mid\mathcal G]\). For p=∞, condition the bounds \(-\|f\|_\infty\le f\le\|f\|_\infty\). At p=1 the conditional Jensen step is just the conditional absolute-value inequality.

Let q be the conjugate exponent, with 1 and ∞ conjugate. On this finite measure space, the norm-duality formula needed here is

\[
\|f\|_p=\sup_{\|g\|_q\le1}\left|\mathbb E[fg]\right|.
\]

Hölder gives the upper bound. For 1<p<∞ and nonzero f, choose \(g=\operatorname{sgn}(f)|f|^{p-1}/\|f\|_p^{p-1}\) to attain equality; for p=1 use g=sgn(f). For p=∞ with \(\|f\|_\infty\)>0, take 0<ε<\(\|f\|_\infty\) and the positive-probability set A\_ε={|f|>\(\|f\|_\infty\)−ε}. The choice \(g=\operatorname{sgn}(f)\mathbf1_{A_\varepsilon}/P(A_\varepsilon)\) reads at least \(\|f\|_\infty\)−ε; let ε decrease to zero. The zero function is immediate. This section identifies the norm only; it does not assert that every continuous linear functional on L∞ is represented by an L¹ function.
