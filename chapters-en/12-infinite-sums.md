# The Mathematics of Chance

Volume II · Probability in an Infinite World

# Chapter 12: When Can Infinitely Many Additions Still Have an Answer?

The ledger on the table is still open.

The previous chapter let us hear a Gaussian outline in the distribution of an endpoint as the number of experiments grows. But an experimenter who keeps going does not inhabit a fresh world each time. There is one lengthening record: yesterday’s error is not erased when today’s distribution is recalculated, and an occasional enormous loss does not disappear merely because it was unlikely.

Chapter 7 proved that the frequency of a fair coin stabilizes along almost every record. That was a genuine infinite-time result, but not the final answer. Coin payoffs are bounded and identically distributed; their tails cannot conceal an unaffordable entry. What if the payoffs change, if errors shrink but are not absolutely summable, or if the mean exists while the variance does not?

We must turn from the endpoint to the journey, from one deviation to every future deviation. Eventually, the difficulties of random addition will separate into three mechanisms that cannot replace one another: exceptional large jumps, persistent drift, and the fluctuations accumulating after centering.

## 12.1 A controlled endpoint does not control the journey

Let the independent real random variables \(X_k\) be centered, \(\mathbb EX_k=0\), with finite variances. Write \(S_n=X_1+\cdots+X_n\). Chapter 11 studied the law of \(S_n\); the second-moment estimate of Chapter 6 gives Chebyshev’s inequality:

\[
P(|S_n|\ge u)\le\frac{\mathbb ES_n^2}{u^2}=\frac1{u^2}\sum_{k=1}^n\operatorname{Var}(X_k),\qquad u>0.
\]

We instead want to know whether \(\max_{1\le k\le n}|S_k|\) exceeds \(u\). A record may wander far away and return by the endpoint. Applying Chebyshev separately at every time and adding the probabilities counts the same variance repeatedly, potentially making the bound useless as time grows.

How can a crossing be counted only once? Instead of guessing the most dangerous time, assign each crossing record to the first time it crosses. The later errors have not yet occurred. Independence prevents them from systematically canceling the deviation already made.

Kolmogorov’s 1928 paper bears the title “On sums of independent random quantities,” directly identifying this subject: [original publication record](https://link.springer.com/article/10.1007/BF01459098). This bibliographic fact identifies the research topic. The proofs below are organized in the measure and integral language now available to us; they are not presented as a reconstruction of that paper’s original exposition or exact theorem versions.

## 12.2 Assigning each record to its first crossing

Define the disjoint events \(A_k=\{|S_j|<u\ (j<k),\ |S_k|\ge u\}\). Each is determined by the first \(k\) experiments, hence is independent of the future sum \(S_n-S_k\). The passage from finite independent coordinates to their generated events is justified by the [π–λ theorem](../foundations/t-mclass.md#t-mclass-pi-lambda). No optional stopping theorem is needed.

Expand the square. The mixed term has expectation zero: \(S_k\mathbf1_{A_k}\) is integrable, the future sum is independent and integrable with mean zero, and expectations factor. The remaining future-square term is nonnegative. Hence

\[
\mathbb E[S_n^2\mathbf1_{A_k}]=\mathbb E[S_k^2\mathbf1_{A_k}]+\mathbb E[(S_n-S_k)^2\mathbf1_{A_k}]\ge u^2P(A_k).
\]

Add the disjoint first-crossing events. They use at most the full second moment at the endpoint. This gives **Kolmogorov’s maximal inequality**:

\[
P\left(\max_{1\le k\le n}|S_k|\ge u\right)\le\frac{1}{u^2}\sum_{k=1}^n\operatorname{Var}(X_k).
\]

The right side is the same as the bound for the endpoint alone. There is no extra charge for every observation time. Paths still pose an additional problem, but independent centered future increments cannot undo the second-moment cost of the first crossing in expectation.

Shift the starting point to \(m\), then let the final time \(N\) increase to infinity. Continuity from below gives

\[
P\left(\sup_{n\ge m}\left|\sum_{k=m}^nX_k\right|>u\right)\le\frac{1}{u^2}\sum_{k=m}^\infty\operatorname{Var}(X_k).
\]

This inequality controls every partial sum from now into the infinite future at once. We finally have events suitable for the Borel–Cantelli lemma established in Chapter 7.

## 12.3 A finite total variance budget lets the errors finish adding

Assume the \(X_n\) are independent and centered, with \(\sum_n\operatorname{Var}(X_n)<\infty\). Choose increasing deterministic integers \(m_j\) so that the variance tail from \(m_j\) onward is at most \(2^{-3j}\). Taking \(u=2^{-j}\) above gives

\[
P\left(\sup_{n\ge m_j}|S_n-S_{m_j-1}|>2^{-j}\right)\le2^{-j}.
\]

These probabilities are summable. By the first Borel–Cantelli lemma, almost every record has no such crossing for all sufficiently large \(j\). Thus every \(n,l\ge m_j\) satisfies \(|S_n-S_l|\le2^{1-j}\). This is the Cauchy condition for the entire sequence, not merely convergence of a selected subsequence. Completeness of the reals gives a finite limit \(S\); set \(S\) to zero on the measurable exceptional null set to obtain a measurable version.

The convergence also holds in mean square. Fix the starting point and apply Fatou as the future endpoint tends to infinity, rather than passing a limit through a square integral without justification:

\[
\mathbb E|S-S_n|^2\le\liminf_{N\to\infty}\mathbb E|S_N-S_n|^2=\sum_{k>n}\operatorname{Var}(X_k)\longrightarrow0.
\]

Thus an independent centered series with summable variances converges almost surely and in \(L^2\). Each term has a second moment and the total budget is finite; identical distributions are unnecessary. Centering independent variables with means gives the same conclusion for \(\sum_n(X_n-\mathbb EX_n)\).

Independent fair signs \(\varepsilon_n=\pm1\) produce the random harmonic series \(\sum_n\varepsilon_n/n\). Its absolute series is the divergent harmonic series, but its variance sum \(\sum_n n^{-2}<\infty\) is finite, so it converges almost surely. Random cancellation is not simply a synonym for small terms: if every sign is the same fair sign \(Z\), then \(X_n=Z/n\) has the same summable variances but diverges on every record. Independence is indispensable in the maximal inequality.

Summable variances are only sufficient. Let independent \(X_n\) take \(n\) and \(-n\) with probability \(1/(2n^2)\) each, and zero otherwise. The nonzero-event probabilities are summable, so almost every record has only finitely many nonzero terms and the series converges. Yet every variance equals 1. A useful estimate is not the final convergence criterion.

## 12.4 What information remains beyond every finite beginning?

The rare-jump example suggests a distinction: finitely many occurrences may change the value of a series, but not whether it converges. This separates what happened near the beginning from what remains true beyond every finite beginning.

Put \(\mathcal F_m=\sigma(X_1,\ldots,X_m)\), \(\mathcal F_\infty=\sigma(X_1,X_2,\ldots)\), and define the tail \(\sigma\)-algebra

\[
\mathcal T=\bigcap_{m\ge1}\sigma(X_{m+1},X_{m+2},\ldots).
\]

This extension of independence can be checked in two steps. Fix \(m\). Start with rectangles in the first \(m\) coordinates and cylinders involving finitely many coordinates after \(m\); finite independence factors their intersection probabilities. Fix a latter cylinder and apply π–λ to extend the former class to all of \(\mathcal F_m\). Then fix such an extended initial event and apply the same theorem to the later cylinders, extending to \(\sigma(X_{m+1},X_{m+2},\ldots)\). These two bodies of information are therefore independent; infinite independence has not been added as a new assumption.

The series-convergence event \(C\) really belongs to this class; this requires more than the intuition that deleting finitely many terms does no harm. For any \(m\), write the Cauchy condition as

\[
C=\bigcap_{r\ge1}\ \bigcup_{N\ge m+1}\ \bigcap_{q\ge p\ge N}\left\{\left|\sum_{k=p}^qX_k\right|\le\frac1r\right\}.
\]

These are countable set operations involving only coordinates after \(m\), so \(C\in\mathcal T\). For \(A\in\mathcal T\), independence and the π–λ extension make \(A\) independent of each \(\mathcal F_m\). For fixed \(A\), the class \(\{B:P(A\cap B)=P(A)P(B)\}\) is a \(\lambda\)-system containing \(\bigcup_m\mathcal F_m\). This union is an algebra generating \(\mathcal F_\infty\). Thus \(A\) is independent of all of \(\mathcal F_\infty\), and in particular of itself.

\[
P(A)=P(A\cap A)=P(A)^2,\qquad P(A)\in\{0,1\}.
\]

This is **Kolmogorov’s 0–1 law**. The infinite experiment has not become deterministic; its first coin is still random. Only tail events, beyond the deciding power of every finite beginning, must have probability zero or one. An independent series therefore converges with probability either zero or one. The law does not say which.

A finite real tail-measurable random variable is almost surely constant: each rational-threshold event has probability zero or one, and monotonicity together with finiteness forces a single dividing point. The sum of a convergent series is generally not a tail variable, however, because changing its first term changes the sum. Tail-measurability of convergence does not mean that its limit is nonrandom.

## 12.5 Separating an infinite ledger into three accounts

Fix a cutoff \(a>0\), temporarily set the large jumps aside, and write

\[
Y_n=X_n\mathbf1_{\{|X_n|\le a\}},\qquad b_n=\mathbb EY_n,\qquad v_n=\operatorname{Var}(Y_n).
\]

The original \(X_n\) need not have means, but the bounded \(Y_n\) always have these two readings. If large jumps occur only finitely often, the original and truncated series have the same convergence behavior. The truncated series separates into deterministic drift and centered fluctuation. This suggests three questions:

\[
\sum_nP(|X_n|>a)<\infty,\qquad\sum_nb_n\ \text{converges in }\mathbb R,\qquad\sum_nv_n<\infty.
\]

**Kolmogorov’s three-series theorem.** For independent real random variables \(X_n\), the series \(\sum_nX_n\) converges almost surely if and only if these three conditions hold for some \(a>0\). If the series converges, they hold for every \(a>0\). The mean series in the middle needs ordinary real convergence, not absolute convergence.

Sufficiency is already available. The first condition and the first Borel–Cantelli lemma make \(X_n=Y_n\) eventually. The third condition and Section 12.3 give almost-sure convergence of \(\sum_n(Y_n-b_n)\). Adding the second condition gives convergence of \(\sum_nY_n\); putting back finitely many large jumps completes the argument.

Necessity is the substantial direction. We just saw convergence with an infinite variance sum. Why should variance summability become necessary after truncation? The answer is not to forget the counterexample: all of its second-moment cost was hidden in the large jumps now removed. Uniformly bounded errors behave differently.

## 12.6 Bounded fluctuations cannot accumulate forever unseen

We need a precise lemma: if independent centered \(Z_n\) satisfy \(|Z_n|\le B<\infty\) and their partial sums are Cauchy in probability, then \(\sum_n\mathbb EZ_n^2<\infty\). Cauchy in probability means that, for every \(u>0\), the probability that the difference between any two sufficiently late partial sums exceeds \(u\) tends uniformly to zero. Almost-sure convergence implies this condition.

The last assertion follows from countable events. For almost-surely convergent partial sums \(R_n\), the events \(\{\sup_{n,l\ge m}|R_n-R_l|>u\}\) decrease with \(m\), and their intersection lies in the null event where the Cauchy condition fails. Continuity from above makes their probabilities tend to zero, uniformly controlling every pair of late endpoints.

Take a sum \(T\) over any finite consecutive block and write \(V=\mathbb ET^2=\sum\mathbb EZ_k^2\). In the fourth-power expansion, any index appearing just once contributes zero by independence and centering. Only single fourth powers and paired squares remain:

\[
\mathbb ET^4=\sum_k\mathbb EZ_k^4+6\sum_{i<j}\mathbb EZ_i^2\,\mathbb EZ_j^2\le B^2V+3V^2.
\]

No extra fourth-moment assumption is imposed: boundedness supplies it. Split the second moment according to \(T^2\le V/2\) and its complement. Cauchy–Schwarz gives, for \(V>0\),

\[
V\le\frac V2+\bigl(\mathbb ET^4\,P(T^2>V/2)\bigr)^{1/2},\qquad P(T^2>V/2)\ge\frac{V^2}{4\mathbb ET^4}\ge\frac{V}{4(B^2+3V)}.
\]

If the variance sum diverges and \(B>0\), however late a block starts, it has a finite endpoint with \(V\ge B^2\). The bound then gives \(P(|T|>B/\sqrt2)\ge1/16\), contradicting the Cauchy condition in probability. The case \(B=0\) is immediate. This proves the lemma. Bounded errors cannot hide unlimited variance forever in isolated disasters of vanishing probability and unbounded size.

## 12.7 Symmetrization: remove the unknown drift, then recover it

Assume now that \(\sum_nX_n\) converges almost surely. For each fixed \(a>0\), the necessary condition \(X_n\to0\) makes \(\{|X_n|>a\}\) occur only finitely often almost surely. The events are independent, so the contrapositive of the second Borel–Cantelli lemma gives summability of the first series. Consequently \(\sum_nY_n\) also converges almost surely.

We do not yet know whether \(\sum_nb_n\) converges, so cannot first assert convergence of the centered series. The product probability space of Chapter 8 gives an independent copy \(Y_n^\prime\) of the entire sequence \(Y_n\). Each series converges on an event of probability 1, and both events hold together on the product space. Their difference series therefore converges. Put

\[
D_n=Y_n-Y_n^\prime,\qquad\mathbb ED_n=0,\qquad|D_n|\le2a,\qquad\operatorname{Var}(D_n)=2v_n.
\]

The differences are independent, centered and uniformly bounded. The preceding lemma gives \(\sum_nv_n<\infty\). Only now may Section 12.3 be used to obtain almost-sure convergence of \(\sum_n(Y_n-b_n)\) on the original space. Subtracting it from \(\sum_nY_n\) on a common probability-one event shows that the deterministic partial sums \(\sum_{k\le n}b_k\) have a finite limit. A deterministic sequence converges once its limit exists on even one such record.

All three necessary conditions are now proved. They hold for every fixed cutoff, whereas sufficiency needs only one cutoff. Symmetrization is not decorative symmetry: it removes the drift before its convergence is known, then control of the fluctuation lets us recover that drift.

## 12.8 None of the three accounts can replace another

Let independent \(X_n\) take \(1,-1\) with probability \(1/(2n)\) each and zero otherwise. With cutoff \(a=1/2\), the truncated means and variances are all zero; only the large-jump probability series diverges. The second Borel–Cantelli lemma makes unit-sized terms occur infinitely often, so even \(X_n\to0\) fails. Vanishing probabilities cannot replace summability of the first series.

If \(X_n=1/n\) deterministically, large jumps eventually disappear and every variance is zero, but the drift is the divergent harmonic series. Replacing it by \(X_n=(-1)^{n+1}/n\) gives a conditionally convergent drift and a convergent series. Thus the second series is not required to be absolutely summable. Random-series theory retains the delicate cancellation of ordinary real series.

Now take independent fair signs and put \(X_n=\varepsilon_n/\sqrt n\). At cutoff 1 there are no large jumps and no drift, but the variance sum \(\sum_n1/n\) diverges. The three-series theorem rules out almost-sure convergence, and the 0–1 law makes its convergence probability zero. Every error tends to zero, yet their sum cannot settle at a finite answer.

For \(\alpha>0\), the series \(\sum_n\varepsilon_n/n^\alpha\) converges with probability 1 when \(\alpha>1/2\), and with probability zero when \(0<\alpha\le1/2\). Absolute convergence occurs only for \(\alpha>1\). The interval \(1/2<\alpha\le1\) measures precisely what independent random cancellation gains over absolute summation. The threshold comes from summable squares, not summable magnitudes.

Return to the rare jumps \(\pm n\) of Section 12.3. At cutoff 1, all but finitely many possible nonzero terms are removed; their jump probabilities are summable, and the remaining mean and variance series satisfy the criteria. The theorem includes this example without requiring a finite total variance of the original variables. Truncation separates disasters occurring only finitely often along a record from persistent small fluctuations.

## 12.9 A deterministic lemma turns series into averages

Series were not our only concern. The experimenter also divides total payoff by the number of trials. Why should convergence of one random series constrain another average? The bridge is entirely deterministic.

**Kronecker’s lemma.** Let \(0<b_n\uparrow\infty\). If the real series \(\sum_nx_n/b_n\) converges, then \(b_n^{-1}\sum_{k\le n}x_k\to0\). Put \(t_n=\sum_{k\le n}x_k/b_k\to t\), with \(t_0=0\). Finite summation by parts gives

\[
\frac1{b_n}\sum_{k=1}^nx_k=t_n-\frac1{b_n}\sum_{k=1}^{n-1}(b_{k+1}-b_k)t_k.
\]

The weights in the second term are nonnegative and sum to \(1-b_1/b_n\to1\). For \(\varepsilon>0\), fix \(K\) so that \(|t_k-t|<\varepsilon\) for \(k\ge K\). The finitely many earlier terms divided by \(b_n\) tend to zero, while the later weighted error is at most \(\varepsilon\). Thus the second term tends to \(t\), canceling the first. This also explains the role of monotonicity of \(b_n\).

Apply the lemma to each record in a probability-one convergence event. If independent \(X_n\) have finite variances with \(\sum_n\operatorname{Var}(X_n)/b_n^2<\infty\), apply the variance criterion to \((X_n-\mathbb EX_n)/b_n\), then Kronecker, obtaining

\[
\frac1{b_n}\sum_{k=1}^n(X_k-\mathbb EX_k)\longrightarrow0\quad\text{a.s.}
\]

Taking \(b_n=n\) gives a strong law without identical distributions. It goes beyond coin frequencies, but still assumes a second moment for every term. If a meaningful mean payoff requires only first-order integrability, why should long-run averaging demand an additional payment in variance?

## 12.10 A cutoff moving with time: keeping only the first moment

Let \(X_1,X_2,\ldots\) be independent and identically distributed, with \(\mathbb E|X_1|<\infty\). Write \(W=|X_1|\). The countable-sum identity for nonnegative integrals gives

\[
\sum_{n\ge1}P(W>n)=\mathbb E\sum_{n\ge1}\mathbf1_{\{W>n\}}\le\mathbb EW<\infty.
\]

Thus a jump larger than \(n\) at the \(n\)-th experiment occurs only finitely often. Use the moving truncation \(Y_n=X_n\mathbf1_{\{|X_n|\le n\}}\). These variables remain independent, though no longer identically distributed. The first Borel–Cantelli lemma makes \(Y_n=X_n\) eventually. The cutoff grows fast enough that the retained record differs from the original in only finitely many places.

The key question is whether the growing truncated second moments become summable after division by time squared. Move the sum into the nonnegative expectation, and the same first moment will control every time at once.

\[
\sum_{n\ge1}\frac{\operatorname{Var}(Y_n)}{n^2}\le\mathbb E\left[W^2\sum_{n\ge1}\frac{\mathbf1_{\{W\le n\}}}{n^2}\right]\le2\mathbb EW<\infty.
\]

The last bound is pointwise. For \(0\le W\le1\), the quantity is at most \(2W^2\le2W\). For \(W>1\), put \(m=\lceil W\rceil\) and use \(\sum_{n\ge m}n^{-2}\le m^{-2}+m^{-1}\le2/m\le2/W\), again obtaining \(2W\). No finiteness of \(\mathbb EX_1^2\) has been assumed.

The preceding strong-law criterion gives \(n^{-1}\sum_{k\le n}(Y_k-\mathbb EY_k)\to0\) almost surely. Identical distributions and DCT give \(\mathbb EY_n=\mathbb E[X_1\mathbf1_{\{W\le n\}}]\to\mathbb EX_1\), dominated by \(W\). Cesàro means of a convergent numerical sequence have the same limit: the finite beginning divided by \(n\) disappears, and every later term is arbitrarily close to the limit. Hence

\[
\frac1n\sum_{k=1}^nY_k\longrightarrow\mathbb EX_1\quad\text{a.s.}
\]

On the probability-one event where the original and truncated variables eventually agree, \(\sum_{k\le n}(X_k-Y_k)\) is eventually one fixed finite random number. Dividing by \(n\) makes it vanish. We have proved the **strong law for general integrable i.i.d. variables**:

\[
\boxed{\ \frac{X_1+\cdots+X_n}{n}\longrightarrow\mathbb EX_1\quad\text{a.s.},\qquad \mathbb E|X_1|<\infty.\ }
\]

This is not a repetition of the coin law in Chapter 7. The new mechanism lets the cutoff height move with the record length. Time weights reorganize a potentially infinite second moment into a finite first-order cost. The strong law does not require Gaussian fluctuations, or even an existing variance.

For example, the density \(p(x)=\alpha x^{-\alpha-1}\mathbf1_{\{x\ge1\}}\), with \(1<\alpha<2\), integrates to 1, has mean \(\alpha/(\alpha-1)\), and has infinite second moment. Independent repeated payoffs still have averages converging almost surely to that mean. The finite-variance standardization of Chapter 11’s CLT cannot simply be applied. Stable averages and Gaussian fluctuations are different questions.

## 12.11 When even the first-order cost is unaffordable

Is absolute first-order integrability merely sufficient? For a finite almost-sure limit of i.i.d. real averages, it is also necessary. If \(S_n/n\) tends almost surely to a finite value, then for \(n\ge2\),

\[
\frac{X_n}{n}=\frac{S_n}{n}-\frac{n-1}{n}\frac{S_{n-1}}{n-1}\longrightarrow0.
\]

The independent events \(\{|X_n|>n\}\) therefore occur only finitely often, and BC2 forces \(\sum_nP(W>n)<\infty\). Pointwise, \(W\le1+\sum_{n\ge1}\mathbf1_{\{W>n\}}\); integration gives \(\mathbb EW<\infty\). Integrability has been deduced from the need for a new payoff to become small relative to the elapsed time, not guessed from the plausibility of a finite mean.

If \(\mathbb EW=\infty\), the tail sum diverges, and BC2 makes \(|X_n|>n\) occur infinitely often almost surely. A finite limiting average is impossible. For nonnegative i.i.d. variables, there is a stronger conclusion. Put \(X_n^{(M)}=\min(X_n,M)\), apply the strong law for each positive integer \(M\), and work on the intersection of these countably many probability-one events:

\[
\liminf_n\frac1n\sum_{k=1}^nX_k\ge\mathbb E\min(X_1,M)\uparrow\mathbb EX_1=\infty.
\]

Thus a nonnegative infinite-mean average tends almost surely to positive infinity. If both signs defeat integrability, one cannot write a nonexistent mean and ask the law of large numbers to approach it. The Cauchy example of Chapter 11 remains a warning: the distribution of an average may stay exactly unchanged at every sample size.

## 12.12 Beyond one average: stabilization of the entire empirical distribution

Chapter 2 asked not only for a price estimate but for knowledge of an unknown distribution. The strong law now handles any fixed bounded measurable payoff. Yet correctness almost surely for every fixed payoff does not permit intersection of uncountably many probability-one events. Monotonicity of distribution functions resolves this familiar difficulty.

For i.i.d. real variables, define \(F(x)=P(X_1\le x)\) and \(F_n(x)=n^{-1}\sum_{k\le n}\mathbf1_{\{X_k\le x\}}\). For fixed \(x\), the strong law gives \(F_n(x)\to F(x)\). We will prove the stronger **Glivenko–Cantelli theorem**:

\[
\sup_{x\in\mathbb R}|F_n(x)-F(x)|\longrightarrow0\quad\text{a.s.}
\]

Fix \(r\ge2\). Take the finitely many quantiles \(q_j=\inf\{x:F(x)\ge j/r\}\), \(j=1,\ldots,r-1\), remove duplicates, sort them and add \(-\infty,+\infty\). Every open gap between adjacent distinct endpoints \(a<b\) has probability at most \(1/r\). Otherwise some \(j/r\) lies strictly between \(F(a)\) and \(F(b-)\), forcing its quantile into \((a,b)\), a contradiction. The two infinite-end gaps are treated the same way.

Apply the strong law simultaneously to the indicators \(\mathbf1_{\{X\le a\}}\) and \(\mathbf1_{\{X<a\}}\) at these finitely many endpoints. Thus \(F_n(a)\to F(a)\) and \(F_n(a-)\to F(a-)\), with values 0 or 1 at infinite endpoints. Left limits matter because an endpoint may carry a large atom. A grid using only right-side values could wrongly charge that entire atom to the gap error.

For \(a<x<b\), monotonicity sandwiches \(F_n(x)\) between \(F_n(a)\) and \(F_n(b-)\), and \(F(x)\) between the corresponding true probabilities. Their open-gap difference is at most \(1/r\). The error inside the gap is therefore bounded by the largest of the finitely many endpoint errors plus \(1/r\); endpoint errors are already controlled. Hence almost surely \(\limsup_n\sup_x|F_n-F|\le1/r\).

Intersect the probability-one events for the countably many \(r\), then let \(r\to\infty\). The supremum is itself measurable: both distribution functions are right-continuous, and every real point is approached by rationals from the right. Thus the supremum equals the countable supremum over \(\mathbb Q\). Both the event in the conclusion and the exceptional set in its proof are now justified.

The entire empirical distribution curve stabilizes, not only one threshold. No mean of the original variable is required, because the averaged observations are bounded indicators. A first moment controls payoff averages; the monotone structure of a distribution function controls all thresholds. Different objects need different finite budgets.

## 12.13 Placing an entire random law inside a set of zero length

The Cantor set in Chapter 5 showed that zero length does not mean few points. The singular distributions discussed in Chapter 6 call for an actual probability living on such a null set. Infinite coins from Chapter 8 and random series now make that construction concrete.

On the infinite independent coin space already constructed, take \(B_n\in\{0,1\}\), each value having probability \(1/2\), and define

\[
Z=\sum_{n=1}^\infty\frac{2B_n}{3^n},\qquad 0\le Z\le1.
\]

The tail after n is at most \(3^{-n}\), so every record converges and the limit is measurable. The first \(n\) digits determine one interval at stage \(n\) of the Cantor construction, hence \(Z\in C\). The [measure foundations](../foundations/t-measure.md#t-measure-cantor) prove injectivity of this 0-and-2 digit coding and \(m(C)=0\).

For fixed \(z\in C\), at most one digit sequence produces it. The probability of matching that sequence’s first \(n\) digits is \(2^{-n}\), so \(P(Z=z)\le2^{-n}\) for every \(n\), hence is zero. The law of \(Z\) has no atoms but is carried entirely by a Lebesgue-null set. Its distribution function is continuous, because each jump equals its singleton mass. It cannot have a Lebesgue density: integrating a density over a null set gives zero, not1.

Nonnegative summation and independence also give \(\mathbb EZ=1/2\) and \(\operatorname{Var}(Z)=\sum_{n\ge1}3^{-2n}=1/8\). Apply the variance formula first to finite partial sums, then pass to the \(L^2\) limit supplied by the uniform tail bound. This continuous singular probability is a law constructed from experiments, rather than a name assigned to the appearance of a curve.

## 12.14 The shape of an endpoint and stability over a lifetime are different answers

We can now place this chapter beside Chapter 11. A Gaussian endpoint limit describes the common square-root-scale shape of many errors. Almost-sure stabilization of an average describes what one experimenter sees throughout a lifetime. Neither simply replaces the other: integrable infinite-variance payoffs show that a strong law may hold when the finite-variance CLT does not apply.

The thread was more than addition. First crossings compress all intermediate events into one second-moment budget. Truncation separates large jumps from small errors. Symmetrization extracts fluctuations before the drift is understood. Kronecker turns convergent series into time averages. The tail 0–1 law excludes intermediate probabilities for convergence beyond the influence of a finite beginning. Each tool addresses a difficulty left open by the preceding tool.

The three-series theorem also points elsewhere. If large jumps do not have summable probabilities and therefore fail to disappear eventually, they may keep arriving. For a series this often means divergence. Under another mode of observation, those arrivals may form a new object worth studying.

## Chapter 12 Epilogue: Beyond the Ledger, Events That Are Rare and Still Arrive

Return to the open ledger. We can finally distinguish small errors that may keep being recorded yet leave a finite total discrepancy, and payoffs whose long-run average stabilizes even without a variance. The answer is not simply that repetition brings cancellation. Large jumps, drift and fluctuation have separate responsibilities.

The experimenter may not want to add every payoff into one finite number. A long record may instead be read for the number of accidents, extreme changes, or opportunities almost invisible in a single trial.

Each opportunity is tiny, yet the number of trials is large. The jumps set beside the ledger may not have disappeared. They may require another scale and another way of counting.

The next chapter will start from such rare events and ask why they can gather into a law with a different shape from the Gaussian.

## History and Further Reading

Kolmogoroff, *Über die Summen durch den Zufall bestimmter unabhängiger Größen*, *Mathematische Annalen* 99 (1928), 309–319: [publisher’s original record](https://link.springer.com/article/10.1007/BF01459098). The publication details are verifiable. The arrangement through first crossings, bounded fourth-moment blocks, symmetrization and moving truncation is a modern proof organization, not a claim about the original proof’s wording or sequence.

For modern treatments of independent series and laws of large numbers, see the corresponding chapters of Durrett’s [author-hosted textbook](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf). The conclusions used here have been proved independently within this chapter. The book’s breadth continues to be compared with the [official record of Kallenberg’s third edition](https://link.springer.com/book/10.1007/978-3-030-61871-1). This chapter concerns independent real sequences, not general dependent processes, martingales or stationary-sequence strong laws.
