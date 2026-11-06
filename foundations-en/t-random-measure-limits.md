# T-RANDOM-MEASURE-LIMITS: Identification and Convergence of Random Mass

Return to [Chapter 49](../chapters/49-random-measures.md#mass-law-limits). Use the LCSC space, compact exhaustion, countable tests, and Polish conclusions of [T-RADON-SPACE](t-radon-space.md). Distribution convergence means weak convergence of the outer laws of random elements. The inner measure topology, vague or finite-measure weak, is specified separately.

## 1. Laplace Functionals and Uniqueness of Joint Readings

<a id="mass-transform-unique"></a>

Let Ξ and η be random nonnegative Radon measures with \(\mathbb E e^{-\Xi f}=\mathbb E e^{-\eta f}\) for all \(f\in C_c^+\). For finitely many tests f₁,…,fᵣ and nonnegative a, substituting \(f=\sum a_jf_j\) gives identical joint Laplace transforms for vectors Y and Z. Their coordinates are finite almost surely because the tests have compact support. Put \(V_j=e^{-Y_j}\), \(W_j=e^{-Z_j}\). Integer a gives all mixed moments on [0,1]ʳ.

Apply the Bernstein approximation from Chapter 13 successively in each coordinate to approximate every continuous function on the compact cube uniformly. Equivalently, write the multivariate polynomial as the expectation of a function of independent binomial coordinates and control error by uniform continuity and the coordinate variance bounds. Thus V and W have the same law. The measurable inverse exponential gives equal laws of Y and Z. All finite-dimensional laws of the countable readings agree; the cylinder π–λ theorem gives equal sequence laws, and evaluation generation gives equal laws of Ξ and η. No moment assumption on Ξ is used.

## 2. A Necessary and Sufficient Tightness Criterion

<a id="mass-random-tightness"></a>

The laws of a family \(\Xi_\alpha\) on \(\mathcal M_+\) are tight exactly when \(\Xi_\alpha(K)\) are uniformly tight for every compact K. For necessity, choose a compact set C of measures with probability at least 1−ε for every law. A continuous reading μχ with χ≥1 on K is bounded on C, so the window-mass tail is at most ε.

For sufficiency, choose aₘ with \(\sup_\alpha\mathbb P\{\Xi_\alpha(K_m)>a_m\}<\varepsilon2^{-m}\). The set \(D=\{\mu:\mu(K_m)\le a_m,\ \forall m\}\) is relatively compact by T-RADON-SPACE, so its closure C is compact. The union bound gives \(\inf_\alpha\mathbb P\{\Xi_\alpha\in C\}\ge1-\varepsilon\). D is Borel, so this is a legitimate probability statement. D itself need not be closed, and the bounds need not come from finite means. A Markov bound using means is only an additional sufficient method.

## 3. From Laplace Convergence to Measure-Law Convergence

<a id="mass-law-convergence"></a>

Theorem: if Ξₙ and Ξ are already random Radon measures, then \(\Xi_n\Rightarrow\Xi\) in the vague space exactly when \(L_n(f)\to L(f)\) for every \(C_c^+\) test. Necessity uses the bounded continuous function \(\mu\mapsto e^{-\mu f}\). For sufficiency, take χ≥1 on K and a,R>0. On \(\{\Xi_nK>R\}\), one has \(1-e^{-a\Xi_n\chi}\ge1-e^{-aR}\), yielding the tail bound in the chapter.

Given ε, finiteness of Ξχ and dominated convergence first permit choosing a with 1−L(aχ)<ε/4. Choose N so that the numerator is below ε/2 for n≥N, then choose R so the denominator is at least one-half, reducing the initial ε constants if necessary. Enlarge R to handle finitely many n<N. The preceding section gives tightness, and the Polish Prokhorov theorem of Chapter 24 gives a weakly convergent further subsequence of every subsequence. Continuous readings identify its Laplace functional as L, and the first section gives uniqueness. Hence the full sequence converges. This is convergence of outer laws, not convergence of individual paths.

If B is relatively compact and \(\mu(\partial B)=0\), continuous inner and outer approximations give \(\mu_n(B)\to\mu(B)\) under deterministic vague convergence. Radon regularity first makes a boundary neighborhood have small mass, then continuous functions squeeze the indicator. Local finiteness suffices. The random version follows from the continuous mapping theorem when \(\mathbb P\{\Xi(\partial B)=0\}=1\). A countable base of balls can avoid random boundaries simultaneously: within a fixed large window, restrict to \(\{\Xi K\le l\}\); expected masses of disjoint spheres sum to at most l, so only countably many radii have positive probability of positive mass. Take a countable union over windows and l.

## 4. Weak and Vague Topologies for Finite Mass

<a id="mass-finite-weak"></a>

Let μₙ and μ be finite nonnegative Radon measures. Convergence against all \(C_b\) tests plainly implies vague convergence and convergence of total masses. Conversely, choose a compactly supported \(0\le\chi\le1\) with \(\mu(1-\chi)<\varepsilon\). If total masses converge too, then \(\mu_n(1-\chi)=\mu_nE-\mu_n\chi\to\mu E-\mu\chi\). For any \(f\in C_b\),

\[ |\mu_nf-\mu f|\le|\mu_n(\chi f)-\mu(\chi f)|+\|f\|_\infty\{\mu_n(1-\chi)+\mu(1-\chi)\}. \]

Let n tend to infinity and then ε decrease to zero. In particular, weak and vague subspace topologies agree on \(\mathcal P(E)\). The former cannot lose probability, while the latter allows loss in the larger \(\mathcal M_+\): δₙ converges vaguely to zero on the real line, but zero is not in \(\mathcal P(E)\). On a fixed compact E the two topologies agree for all finite measures, since the constant one is compactly supported.

If \(P_n\Rightarrow P\) is outer vague distributional convergence and both Pₙ and P lie almost surely in \(\mathcal P(E)\), it is also outer convergence in the weak probability space. Use the Skorokhod representation of Chapter 24 on Polish \(\mathcal M_+\). The represented copies converge vaguely almost surely; on one common full-probability set their masses are all one. The deterministic result gives weak convergence almost surely, hence distributional convergence. This keeps the subspace topology separate from the requirement that the limit stay within the subspace.

## 5. Random Normalization and Tail Control

<a id="mass-random-normalize"></a>

Let Ξₙ and Ξ be finite with positive total masses almost surely, and assume \((\Xi_n,\Xi_nE)\Rightarrow(\Xi,\Xi E)\) in \(\mathcal M_+\times\mathbb R_+\). Skorokhod representation and the deterministic argument first give almost-sure weak convergence of finite measures. The denominator converges to a positive number, so division gives almost-sure weak convergence of normalized probabilities, hence convergence of the original outer laws. If Ξ can be zero, normalization has no continuous extension there. If its mass is infinite, division is not a legitimate normalization.

A usable no-escape condition is: for every ε>0 there is a compactly supported \(0\le\chi\le1\) with \(\sup_n\mathbb P\{\Xi_n(1-\chi)>\varepsilon\}<\varepsilon\), and Ξ is finite. Together with vague distributional convergence this gives \((\Xi_n,\Xi_nE)\Rightarrow(\Xi,\Xi E)\). First use the continuous coordinate for fixed χ, then exhaust χ using the probability tail bounds; Ξ’s own tails vanish by finiteness. The approximation lemma of Chapter 24, or a triangle bound for bounded Lipschitz tests, gives the joint conclusion. Bounded expected total mass without spatial tail control is insufficient, as δₙ demonstrates.
