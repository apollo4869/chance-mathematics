# Empirical Probability Limits, Weak Topology and Quantifier Boundaries

## 1. Limits for fixed observations

<a id="exchange-empirical-fixed"></a>

For the standard Borel exchangeable sequence and its constructed ν, let f be a fixed Borel real function with E|f(X₁)|<∞. Finite-group averaging identifies its empirical mean with E[f(X₁)|Gₙ]. Reverse martingale convergence gives the almost sure and L¹ limit below. The conditional law identifies νf=E[f(X₁)|J] and ensures finite absolute integral almost surely. Indicators identify every fixed Borel-set evaluation.

\[ L_N f=\frac1N\sum_{i=1}^N f(X_i)\longrightarrow\nu f\quad\text{a.s. and in }L^1\qquad(E|f(X_1)|<\infty). \]

Set νf to zero on parameters with ν|f|=∞; the following assertion only uses the event of finite absolute integral. If ν|f| is almost surely finite but its unconditional expectation may be infinite, the iid strong law under each fixed μ and integration of its jointly measurable event still give almost sure convergence, without an L¹ assertion. Each statement is first for fixed f; a countable class permits a common null set.

## 2. A weak distance from countably many observations

<a id="exchange-empirical-metric"></a>

For the weak convergence corollary assume E is Polish with a fixed complete separable metric d. For a bare standard Borel space first choose a Borel encoding into a Polish S and discuss the pushed probabilities in S. There is no canonical weak topology on a bare measurable space.

\[ D(\mu,\eta)=\sup_{\substack{|f|\le1\\\operatorname{Lip}(f)\le1}}|\mu f-\eta f|. \]

The supremum can be replaced by a fixed countable class. From a countable dense set of points and rational q form finite minima min(qᵢ+d(x,xᵢ)), clipped to [−1,1]. This countable class F approximates every bounded one-Lipschitz f uniformly on a compact K: use a finite δ-net of dense points and choose qᵢ within δ of f(xᵢ). The lower envelope lies between f−δ and f+3δ on K, and clipping does not increase the error.

For fixed μ,η, tightness provides a common high-probability compact set. Approximate there and bound errors outside by one to identify D with the supremum over F. Integrals μf are evaluation-measurable by simple functions and monotone convergence. Hence D is measurable in the two probability parameters, and the event D(Lₙ,μ)→0 is jointly measurable in (μ,record).

If D(μₙ,μ)→0, approximate a closed-set indicator by max(0,1−m d(x,C)). For each fixed m divide by max(1,m) to obtain a test in the defining class. First let n tend to infinity, then increase m. Portmanteau in Chapter24 gives weak convergence. This distance is not total variation.

## 3. From conditional strong laws to an empirical probability limit

<a id="exchange-empirical-weak"></a>

Fix μ and iid(μ). For ε>0 choose compact K with μ(Kᶜ)<ε. Arzelà–Ascoli in Chapter24 makes the restrictions of bounded one-Lipschitz functions totally bounded on K, so choose a finite ε-net centered in this family. Apply the strong law to the net functions and 1K. Approximate any f by a nearest g on K to get the following uniform estimate.

\[ D(L_N,\mu)\le\max_{g\in\mathcal F_{\varepsilon,K}}|L_Ng-\mu g|+2\varepsilon+2L_N(K^c)+2\mu(K^c),\qquad \limsup_N D(L_N,\mu)\le6\varepsilon. \]

Repeat for ε=2⁻ʲ, using countably many compacts and finite nets. Thus D(Lₙ,μ)→0 almost surely under the μ-product law. The compacts and nets may depend on μ; no family uniformly tight over all μ is assumed. Since the final convergence event is jointly measurable, integrate it using K(μ,·) and M to obtain D(Lₙ,ν)→0 for the exchangeable record.

\[ L_N\Rightarrow\nu\quad\text{a.s. on a Polish state space, or after a specified Borel encoding into a Polish space}. \]

This identifies a random weak limit pathwise. It does not assert total variation convergence or interchange separate almost sure assertions for every test with a simultaneous assertion. A countable measurable distance, conditional integration and finite nets on compacts supply the missing steps.

## 4. Why all Borel sets cannot share a universal null set

<a id="exchange-empirical-boundary"></a>

For iid uniform[0,1], the strong law gives Lₙ(A)→Leb(A) for every fixed Borel A. But for any realized record, its countable set D of observed values is Borel with Leb(D)=0 and Lₙ(D)=1 for every n. No probability-one set can make every Borel-set evaluation converge simultaneously for each of its records.

\[ d_{\rm TV}(L_N,\operatorname{Leb}_{[0,1]})=1\quad\text{for every }N,\qquad L_N\Rightarrow\operatorname{Leb}_{[0,1]}\quad\text{a.s.} \]

For the first equality choose the finite set of the first N observations. Empirical identification means convergence on a countable determining class, each fixed integrable test, and weakly in a specified Polish topology. It does not say that finite records reproduce a continuous probability on every measurable event. Return to [Chapter43](../chapters/43-exchangeability.md#exchange-empirical).
