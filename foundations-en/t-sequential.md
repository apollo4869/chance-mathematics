# T-SEQUENTIAL: Sequential Experiments on Arbitrary Measurable Spaces

This proof concerns countably many arbitrary nonempty measurable spaces \((E_n,\mathcal E_n)\); it does not misuse the randomization representation for standard Borel spaces. Given an initial probability \(\nu\) and probability kernels \(K_{n+1}\) from the prefix \(E_0\times\cdots\times E_n\) to \(E_{n+1}\), there is a unique probability on the coordinate product sigma-field with finite-prefix integrals given by successive kernel integration. No arbitrary uncountable-index extension or existence of regular conditional distributions on general spaces is asserted.

<a id="t-sequential-extension"></a>

## Finite integration and consistency

Chapter 10 proved through indicators, simple functions and monotone convergence that kernel integration preserves measurability and composes into finite product measures. Thus each prefix has a probability \(P_n\). Integrating out its final coordinate uses kernel mass one, so these probabilities are consistent. Initial cylinders form an algebra: any finite-coordinate event can be padded to an initial prefix, and finitely many Boolean operations still use a common prefix. Define \(q(A)=P_n(A_n)\) on this algebra; consistency removes dependence on the chosen prefix length.

Finite additivity is not yet countable additivity. The finite products used here are those of Chapter 10.9 on arbitrary measurable spaces, not the standard Borel randomization of 10.18; countable additivity on disjoint events is preserved successively by that of the kernels and monotone convergence. We now prove empty-intersection continuity on the cylinder algebra without compactness of the state spaces. Each input kernel is defined at every prefix and has mass one; these pointwise data are essential for the recursion.

## Positive remaining probability allows one record to be chosen

Suppose cylinders \(A_j\downarrow\varnothing\), but \(q(A_j)\downarrow c>0\). Let \(d_j\) be the highest coordinate index needed for the \(j\)th event, enlarged so that \(d_j\uparrow\infty\). For each fixed prefix \(x_{0:m}\), integrate the indicator of \(A_j\) over its remaining coordinates with the successive kernels. If \(d_j\le m\), simply use its already determined indicator. Denote the resulting function by \(f_{m,j}(x_{0:m})\).

Event inclusion and positivity of the kernels make these functions decreasing in \(j\), between zero and one. Put \(f_m=\lim_j f_{m,j}\). For every prefix there is the exact identity

\[
f_m(x_{0:m})=\int f_{m+1}(x_{0:m},y)K_{m+1}(x_{0:m},dy).
\]

This follows by bounded convergence; if the event already uses a shorter prefix, integrating its constant indicator leaves it unchanged. The identity therefore holds at every prefix, rather than almost everywhere for some marginal measure. The same argument gives \(\int f_0\,d\nu=c>0\).

Choose a point with \(f_0(x_0)>0\). Once \(f_m(x_{0:m})>0\) has been chosen, the identity supplies some \(y\) with \(f_{m+1}(x_{0:m},y)>0\). Successive choices produce an infinite record \(x\). Only countable dependent choice is used: no measurable selection of a point as a function of its prefix is required.

For any \(j\), choose \(m\ge d_j\). Decrease in the events gives \(f_m(x_{0:m})\le\mathbf1_{A_j}(x)\). The left side is positive, so \(x\in A_j\). This holds for every \(j\), contradicting the empty intersection. Hence \(q(A_j)\downarrow0\).

## An actual infinite space

For a finitely additive probability on an algebra, this continuity implies the premeasure property. If disjoint \(B_j\) have union \(B\) in the algebra, the remainders \(B\setminus\bigcup_{j\le n}B_j\) decrease to the empty set and have vanishing mass. Chapter 8's outer-measure extension therefore extends \(q\) to the coordinate sigma-field. The pi–lambda uniqueness theorem for finite measures makes the extension unique.

Under this probability the kernels really do specify next-step conditional averages. For bounded measurable \(g\), the function \(\int g(y)K_{n+1}(X_{0:n},dy)\) is measurable and has the same integral as \(g(X_{n+1})\) on every prefix event. Check cylinders first, then extend by a monotone class. This completes the countable Ionescu–Tulcea sequential construction on general measurable spaces. We have not inferred an unproved regular conditional kernel from mere existence of conditional expectation.
