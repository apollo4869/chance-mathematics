# Chapter 15: What Becomes of a Game That Remains Fair Forever?

A player stakes one unit on a fair coin. Heads doubles the capital; tails wipes it out and ends the game. As long as any money remains on the table, the player stakes it again.

There is no commission and no hidden change in the odds. However long the winning streak, the expected capital after the next round equals the capital now held. Yet almost every player who keeps going eventually loses that initial unit.

There is no arithmetic mistake. Fairness at a finite time and the eventual outcome of a path are different assertions. We need to find the connection that really holds between them.

## 15.1 Always fair, yet almost certain to vanish

On the infinite fair-coin space constructed in Chapter 8, let ξ_n record the nth toss, with heads represented by 1 and tails by 0. Set

\[
M_0=1,\qquad M_n=2^n\prod_{j=1}^n\xi_j,\qquad
\mathcal F_n=\sigma(\xi_1,\ldots,\xi_n).
\]

Information grows with the game. Once the first n tosses are known, M_n is determined; the next coin remains independent of that information. Thus

\[
\mathbb E[M_{n+1}\mid\mathcal F_n]
=2M_n\mathbb E[\xi_{n+1}\mid\mathcal F_n]=M_n.
\]

In particular, the expectation is 1 at every finite n. But the probability that the first n tosses are all heads is only \(2^{-n}\). These events decrease, so the probability of never seeing tails is 0. Almost every record has a first tail, after which the capital stays at 0. Consequently,

\[
M_n\longrightarrow0\quad\text{a.s.},\qquad
\mathbb E M_n=1\not\longrightarrow0.
\]

The spike from Chapter 6 has acquired a time dimension. The opportunities carrying the expectation become smaller, while the capital on those opportunities becomes larger. There is also an additional constraint: these spikes are not arranged arbitrarily. At every step they obey the same conditional fairness relation.

How much does that relation restrict? It plainly cannot preserve the expectation at the eventual endpoint. But neither does it allow paths to oscillate without restraint. To uncover that restriction, fairness must first be attached to the right information.

## 15.2 Fairness is relative to what has already been seen

On a fixed probability space, an increasing sequence of σ-fields \(\mathcal F_0\subseteq\mathcal F_1\subseteq\cdots\) is a filtration. It describes the information available at successive times without presuming that the future is already known.

A sequence of real random variables X_n is a martingale relative to this filtration if each term is integrable and \(\mathcal F_n\)-measurable, and

\[
\mathbb E[X_{n+1}\mid\mathcal F_n]=X_n,
\]

Replacing equality by ≥ gives a submartingale; replacing it by ≤ gives a supermartingale. This chapter concerns discrete time only. All such relations hold almost surely. Since the time index is countable, a single null set can be removed to make the required time-by-time relations hold simultaneously.

The names should not mislead: a submartingale permits its conditional average to increase; a supermartingale permits it to decrease. A martingale belongs to both classes. Iterating the tower property from Chapter 9 gives, for m≤n,

\[
\mathbb E[X_n\mid\mathcal F_m]\ge X_m
\]

for a submartingale, with equality or the reversed inequality for the other two classes. The proof successively conditions from n down to m, using monotonicity. No result about observation at random times is needed.

The same numerical process can lose its fairness when the filtration changes. For a simple symmetric random walk, if the first increment is revealed at time 0, that increment no longer has conditional mean 0. The filtration is not an accessory to the definition: it specifies exactly what a player can use in making a decision.

Conditional Jensen from Chapter 9 supplies a useful bridge. If M is a martingale, |M_n| is a nonnegative submartingale. If p≥1 and each pth moment is finite, \(|M_n|^p\) is also a submartingale. For a submartingale X, \((X_n-a)^+\) is a submartingale because the positive-part function is both convex and increasing. These transformations will let us study an entire path rather than only its distribution at one fixed time.

## 15.3 How likely is an exceptionally large win?

Let Y be a nonnegative submartingale, observed at the finitely many times 0 through N, and write

\[
Y_N^*=\max_{0\le k\le N}Y_k.
\]

If the player crosses height λ, the information available at the first crossing already identifies that occurrence. For now, rather than invoke a new theorem about the crossing time, separate the possible records in a finite ledger.

For λ>0, let A_k be the event that all earlier observations were below λ while Y_k≥λ. Then \(A_k\in\mathcal F_k\); these events are disjoint and their union is \(\{Y_N^*\ge\lambda\}\). The multistep submartingale relation gives

\[
\mathbb E[Y_N\mathbf1_{A_k}]
=\mathbb E[\mathbb E(Y_N\mid\mathcal F_k)\mathbf1_{A_k}]
\ge\mathbb E[Y_k\mathbf1_{A_k}]
\ge\lambda P(A_k).
\]

Adding these finitely many inequalities yields the refined form of Doob's maximal inequality:

\[
\lambda P(Y_N^*\ge\lambda)
\le\mathbb E[Y_N\mathbf1_{\{Y_N^*\ge\lambda\}}]
\le\mathbb E Y_N.
\]

The endpoint does not record every fluctuation, but conditional averaging reconnects that endpoint to each crossing event. This is the additional structure needed to control a whole path. Applying the result to Y=|M| gives, for a martingale M,

\[
P\!\left(\max_{k\le N}|M_k|\ge\lambda\right)
\le\frac{\mathbb E|M_N|}{\lambda}.
\]

A nonnegative supermartingale has a maximal estimate in the other direction: \(P(\max_{k\le N}X_k\ge\lambda)\le\mathbb E X_0/\lambda\). It does not follow by merely substituting the word “supermartingale” into the preceding proof. Here is a finite-increment argument.

Keep the capital active until it crosses the threshold, then freeze it. Let H_k indicate that none of times 0 through k−1 has yet crossed. It is \(\mathcal F_{k-1}\)-measurable and takes values 0 or 1. Define

\[
W_N=X_0+\sum_{k=1}^NH_k(X_k-X_{k-1}).
\]

Path by path, W_N is the capital at the first crossing if a crossing has occurred; otherwise W_N=X_N. Hence it is nonnegative and is at least λ on the crossing event. Each expected increment is nonpositive, since H_k is nonnegative and known before the bet. Thus \(\lambda P(\max_{k\le N}X_k\ge\lambda)\le\mathbb E W_N\le\mathbb E X_0\). This uses only finite sums and conditional averaging, not the optional sampling theorem of the next chapter.

In the opening game, the chance of reaching \(2^j\) is exactly \(2^{-j}\), provided N≥j. The weak estimate is an equality at those heights. Rare large winners do exist; the inequality states the cost their probabilities must pay.

## 15.4 Controlling the highest point does not control repeated returns

A bounded sequence need not converge: it can jump forever between two values. Controlling the maximum height is therefore insufficient. We must count how often a path can travel between two fixed levels.

Fix a<b. Start at the first observation at or below a and wait for the first subsequent observation at or above b; that completes one upcrossing. Restart at the next observation at or below a and repeat. Let U_N(a,b) count the upcrossings completed by time N. If no suitable entry point appears, the count is 0. A final journey that has not reached b does not count as completed.

Equivalently, describe a time-by-time strategy. When not holding a unit, buy if the current value is at most a. When holding one, sell if the current value is at least b. Before the kth price change, the holding decision is already determined by the first k−1 steps. The holding indicator H_k is therefore a \(\mathcal F_{k-1}\)-measurable 0–1 variable.

For a supermartingale X, the finite-increment gain is

\[
G_N=\sum_{k=1}^NH_k(X_k-X_{k-1}),\qquad \mathbb E G_N\le0.
\]

The expectation inequality uses only the supermartingale relation. X may be any record with that conditional-average property. Buying and selling provide a mathematical ledger, not an additional assumption about arbitrage in a market.

Every completed upcrossing earns at least b−a. If a position remains unsold, it was bought at a value at most a, so its current loss is at most \((X_N-a)^-\). Path by path,

\[
G_N\ge(b-a)U_N(a,b)-(X_N-a)^-.
\]

Taking expectations gives the supermartingale upcrossing inequality:

\[
(b-a)\mathbb E U_N(a,b)\le\mathbb E(X_N-a)^-.
\]

Here \(x^-=\max(-x,0)\). The negative part occurs because the one unfinished purchase may have an unrealized loss, not because a symmetric formula was desired. Ignoring that loss would invalidate the pathwise inequality.

For a submartingale, the expected gain has the opposite sign, and we cannot continue to assert \(\mathbb E G_N\le0\). However, the complementary finite strategy, holding exactly when H_k=0, has nonnegative expected gain. Therefore

\[
\mathbb E G_N\le\mathbb E(X_N-X_0).
\]

Combining this with the same pathwise inequality gives the valid submartingale version:

\[
(b-a)\mathbb E U_N(a,b)
\le\mathbb E(X_N-a)^+-\mathbb E(X_0-a).
\]

All terms are integrable; there is no undefined subtraction of infinities. Both versions compare the profit required by infinitely many oscillations with a finite expected ledger.

## 15.5 The bill for repeated crossings forces a path to choose a limit

Suppose X is a nonnegative supermartingale. Since \((X_N-a)^-\le a^+\), the upcrossing estimate and monotone convergence imply

\[
\mathbb E U_\infty(a,b)\le\frac{a^+}{b-a}<\infty.
\]

Thus, for every rational pair a<b, infinitely many upcrossings have probability 0. There are only countably many rational pairs, so their exceptional sets can be removed simultaneously. If a remaining path had a lower limit strictly below its upper limit—initially allowing extended real values—we could insert two finite rationals between them. The path would have to upcross that interval infinitely often, a contradiction.

Hence X_n has an extended real limit X_∞. Nonnegativity excludes −∞, while the supermartingale property gives \(\mathbb E X_n\le\mathbb E X_0\). Fatou's lemma yields

\[
\mathbb E X_\infty\le\liminf_n\mathbb E X_n
\le\mathbb E X_0<\infty.
\]

Therefore +∞ can occur only on a null set. We have proved that **every nonnegative discrete-time supermartingale converges almost surely to a finite integrable random variable**. Neither independent increments nor a uniform second-moment bound is required.

When capital may be negative, an appropriate budget is the average positive part. Let X be a submartingale with

\[
C=\sup_n\mathbb E X_n^+<\infty.
\]

The right side of the submartingale upcrossing inequality is at most \(C+|a|+|\mathbb E(X_0-a)|\), so the same rational-interval argument excludes oscillation. We must still exclude infinite limits. Since \(\mathbb E X_n\ge\mathbb E X_0\),

\[
\mathbb E X_n^-\le C-\mathbb E X_0,\qquad
\sup_n\mathbb E|X_n|\le2C-\mathbb E X_0<\infty.
\]

Applying Fatou to the absolute values shows that the limit is finite and integrable. This proves the **submartingale convergence theorem under an L¹ bound on the positive parts**. In particular, every L¹-bounded martingale converges almost surely.

The positive-part budget cannot simply be omitted. A simple symmetric random walk S_n is a martingale but cannot converge almost surely to a finite limit. Its increments have absolute value 1, whereas successive differences of any convergent real sequence must tend to 0. This already disproves “fairness alone implies convergence”; the full recurrence theory of random walks is unnecessary.

## 15.6 The path has settled, but the expectation may still escape

Return to the opening game. Being a nonnegative martingale, it falls within the convergence theorem just proved. But that theorem only says that a path eventually chooses a finite value. It does not permit an average to pass through the infinite-time limit.

More precisely, for every fixed K, whenever \(2^n>K\),

\[
\mathbb E[M_n\mathbf1_{\{M_n>K\}}]=1.
\]

The family of capitals is therefore not uniformly integrable. Chapter 7's Vitali criterion explains how almost sure convergence together with uniform integrability can be upgraded to L¹ convergence. What fails here is exactly the condition preventing expected mass from escaping into increasingly high tails.

The expected highest capital reveals another boundary. If the first tail occurs at round j≤N, the maximum previously reached is \(2^{j−1}\), and that event has probability \(2^{-j}\). If the first N tosses are all heads, the maximum is \(2^N\) and the probability is \(2^{-N}\). Hence

\[
\mathbb E\max_{0\le k\le N}M_k
=\sum_{j=1}^N2^{j-1}2^{-j}+2^N2^{-N}
=1+\frac N2.
\]

The expected endpoint remains 1, but the expected maximum of the entire path has no uniform bound. The weak maximal tail estimate cannot therefore be strengthened indiscriminately to \(\mathbb E\max_{k\le N}|M_k|\le C\mathbb E|M_N|\) with C independent of both the martingale and N.

This does not rule out every integrable bound on the maximum. It identifies L¹ as a genuine boundary: controlling the average size of a whole maximum requires more tail information than a first moment alone. Extending fairness from finite times to an endpoint likewise requires understanding the integrable final ledger from which those successive capitals might arise.

Pathwise convergence, convergence of averages and the gradual revelation of information have become three related questions that cannot be identified with one another.

## 15.7 What escapes is the expected mass in the tail

Nonnegativity makes this loss exactly calculable. Suppose a nonnegative martingale M\_n converges almost surely to M\_∞, and write c=E M\_0. The upcrossing theorem and Fatou already ensure that M\_∞ is integrable with E M\_∞≤c. Since min(M\_n,M\_∞) converges to M\_∞ and is dominated by the integrable M\_∞, Chapter 6's dominated convergence theorem gives

\[
\mathbb E|M_n-M_\infty|
=c+\mathbb E M_\infty-2\mathbb E\min(M_n,M_\infty)
\longrightarrow c-\mathbb E M_\infty.
\]

For a nonnegative martingale, preserving the expectation is therefore equivalent to L¹ convergence. The unit lost at the limit in the opening game is exactly the unit left in the limiting L¹ distance. Probability mass has not disappeared: total probability is still 1 at each time. What fails to survive the limit is the expected capital.

For martingales of either sign, the numerical expectation alone is insufficient, because positive and negative tails can cancel. Uniform integrability from Chapter 7 gives the precise condition. A family of integrable variables Z\_i is uniformly integrable if

\[
\lim_{K\to\infty}\sup_i\mathbb E[|Z_i|\mathbf1_{\{|Z_i|>K\}}]=0.
\]

This first gives a uniform first-moment budget: split |Z\_i| at K to obtain sup\_i E|Z\_i|<∞. More importantly, it controls where that budget can hide, preventing it from escaping entirely into increasingly high and rare tails.

A uniformly integrable martingale consequently has an almost sure limit by 15.5 and converges in L¹ by Chapter 7's Vitali criterion. We must still understand why this tail condition should be related to repeatedly updating the same final judgment.

## 15.8 Every valuation comes from the same final ledger

Let Z∈L¹ and put M\_n=E[Z|F\_n]. The tower property makes M a martingale. It is said to be closed by Z: the available information changes from one valuation to the next, but the integrable terminal quantity being valued remains the same.

Why does closure prevent expected mass from escaping? Put A\_n={|M\_n|>K} and truncate Z at K/2. The conditional absolute-value inequality gives

\[
|M_n|\le K/2+\mathbb E[|Z|\mathbf1_{\{|Z|>K/2\}}\mid\mathcal F_n].
\]

On A\_n, K/2<|M\_n|/2. Move that term to the left and integrate to obtain

\[
\mathbb E[|M_n|\mathbf1_{A_n}]
\le2\mathbb E[|Z|\mathbf1_{\{|Z|>K/2\}}].
\]

The right side is independent of n and tends to zero as K increases. All these conditional averages are uniformly integrable. The argument does not even require their σ-fields to be increasing. We will use the same tail budget when studying decreasing information.

Conversely, suppose a martingale is uniformly integrable. Section 15.7 gives almost sure and L¹ convergence to M\_∞. Fix n and A∈F\_n. For k≥n, multistep fairness gives E[M\_k1\_A]=E[M\_n1\_A]. Let k tend to infinity; L¹ convergence permits the limit in this event integral. Thus

\[
\mathbb E[M_\infty\mathbf1_A]=\mathbb E[M_n\mathbf1_A],
\qquad M_n=\mathbb E[M_\infty\mid\mathcal F_n].
\]

We have proved that **a martingale is uniformly integrable if and only if it can be closed by an integrable random variable, and if and only if it converges in L¹**. The last implication is fully justified as well: if L¹ convergence to Z is known first, the same event-integral argument gives M\_n=E[Z|F\_n], after which the tail estimate proves uniform integrability.

A uniformly integrable submartingale also has almost sure and L¹ limits by 15.5 and Vitali. But passing to the limit in its multistep event integrals for fixed A∈F\_n only gives \(X_n\le\mathbb E[X_\infty\mid\mathcal F_n]\). For example, the deterministic \(X_n=1-2^{-n}\) has upward drift and limit 1, different from its current value at every step. The closure equivalence is therefore explicitly a theorem about martingales.

Closure does not say that the player already knows the terminal value. It says that every unfinished valuation can be explained by the same integrable ledger. The doubling game cannot be closed in this sense: its L¹ limit would have to be both zero and of expectation 1, a contradiction.

## 15.9 When all the available information has arrived

There is an easily misstated detail. If M\_n=E[Z|F\_n], its limit need not be Z: the observations may never reveal everything about Z. Define

\[
\mathcal F_\infty=\sigma\!\left(\bigcup_n\mathcal F_n\right).
\]

Section 15.8 provides an almost sure and L¹ limit V. Setting it to zero where a finite limit does not exist gives an F\_∞-measurable version. For any event A in the union, first choose F\_m containing it, then let n≥m tend to infinity to obtain E[V1\_A]=E[Z1\_A].

These equalities cover all of F\_∞. The union of increasing σ-fields is an algebra, hence a π-system. The events satisfying E[(V−Z)1\_A]=0 form a λ-system: the whole space, complements and countable disjoint unions follow from zero total integral and integrability. The [π–λ theorem](../foundations/t-mclass.md#t-mclass-pi-lambda) accompanying Chapter 5 extends the equality to F\_∞. Therefore

\[
\mathbb E[Z\mid\mathcal F_n]\longrightarrow
\mathbb E[Z\mid\mathcal F_\infty]
\quad\text{a.s. and in }L^1.
\]

This is often called the upward convergence theorem for conditional expectations, or Lévy's upward theorem. We have proved its precise increasing-information version. The right side simplifies to Z only when Z has an F\_∞-measurable version. A variable independent of every available observation, and never revealed by them, retains its unconditional average.

Chapter 9's L² projection picture has acquired a time direction. Increasing information subspaces provide increasingly refined predictions, but the final prediction belongs to the information they generate; it does not acquire every fact about the world by magic.

## 15.10 The size of the maximum requires more than a first moment

Section 15.6 showed that no constant independent of N bounds the L¹ norm of the maximum by that of the endpoint. Controlling a pth moment, p>1, charges high tails a greater price and changes the situation.

Before these tools are first used, the [T-LP supplement](../foundations/t-lp.md#t-lp-holder) proves general Hölder and Minkowski inequalities, [completeness for every 1≤p≤∞](../foundations/t-lp.md#t-lp-complete), and the required probability-space approximation, conditional contraction and norm duality. Chapter 9's L² completeness is not being mistaken for general Lᵖ completeness.

Let Y be a nonnegative submartingale with Y\_N∈L^p, 1<p<∞, and again put \(Z=Y_N^*\). Integrate the refined tail bound of 15.3 over λ from 0 to R. Tonelli applies to the nonnegative integrands. Truncation at R avoids assuming in advance that Z has a pth moment:

\[
\mathbb E(Z\wedge R)^p
=\int_0^R p\lambda^{p-1}P(Z>\lambda)\,d\lambda
\le\frac p{p-1}\mathbb E[Y_N(Z\wedge R)^{p-1}].
\]

Only now apply Hölder with conjugate exponents p and q=p/(p−1). Because Z∧R is bounded, its norm is finite, and its nonzero (p−1)st power may safely be cancelled; a zero norm is immediate. Hence

\[
\|Z\wedge R\|_p\le\frac p{p-1}\|Y_N\|_p.
\]

Let R increase to infinity and use monotone convergence. This proves Doob's Lᵖ maximal inequality:

\[
\left\|\max_{k\le N}Y_k\right\|_p
\le\frac p{p-1}\|Y_N\|_p,\qquad1<p<\infty.
\]

At the endpoint p=∞, the multistep submartingale relation gives Y\_k≤E[Y\_N|F\_k]≤‖Y\_N‖\_∞. The L∞ norm of the maximum is therefore bounded by that of the endpoint with constant 1. This maximal bound does not itself ensure L∞ norm convergence, as the following section will show.

For a martingale use Y=|M|. Truncation is essential: writing a possibly infinite E Z^p and cancelling a power of it cannot establish its finiteness. The constant diverges as p decreases to 1, consistently with the first-moment boundary exposed by the opening game.

## 15.11 A common moment budget steadies the entire remaining journey

Let M be a martingale, 1<p<∞, with \(C=\sup_n\|M_n\|_p<\infty\). Hölder first gives L¹ boundedness, so 15.5 gives an almost surely finite limit M\_∞. Apply the maximal inequality for each N and let N increase to infinity:

\[
M^*=\sup_{n\ge0}|M_n|\in L^p,
\qquad\|M^*\|_p\le\frac p{p-1}C.
\]

In particular \(|M_\infty|\le M^*\). Now \(|M_n-M_\infty|^p\le2^p(M^*)^p\). Only after obtaining this integrable domination may DCT establish L^p convergence. Section 15.8 also gives \(M_n=\mathbb E[M_\infty\mid\mathcal F_n]\). A pth-moment budget therefore controls both the maximum and the average error on the way to the terminal value.

Even the entire future deviation from the present judgment is controlled. For k≥n, regard M\_k−M\_n as a martingale starting at n, apply the finite-horizon maximal inequality, and then use the established L^p convergence and monotone convergence:

\[
\left\|\sup_{k\ge n}|M_k-M_n|\right\|_p
\le\frac p{p-1}\|M_\infty-M_n\|_p\longrightarrow0.
\]

No continuous-time path regularization has been introduced. These are countably many discrete times, and measurability of their supremum is already available.

The endpoint ∞ cannot inherit this norm-convergence assertion. Let U be uniform on [0,1], let F\_n be generated by the dyadic interval partition, and put \(Z=\mathbf1_{\{U<1/3\}}\), M\_n=E[Z|F\_n]. These capitals remain between 0 and 1. Since F\_∞ generates the Borel information, M\_n→Z almost surely and in every finite L^p. But a positive-length dyadic interval always straddles 1/3. On it M\_n is a constant 0<r<1, while Z takes values 0 and 1 on two positive-measure parts. Thus

\[
\|M_n-Z\|_\infty\ge\max(r,1-r)\ge1/2.
\]

Essential boundedness does not ensure L∞ norm convergence. Conversely, uniform integrability does not create higher moments: for p>1 let \(Z=U^{-1/p}\), setting it to zero at U=0. It is integrable but not in L^p. The constant martingale M\_n=Z is uniformly integrable, yet is not even a convergence problem inside L^p. Each condition has its own role.

## 15.12 When observations are gradually forgotten

Some problems ask us to discard early details: retain only increasingly remote records, or forget more and more labels in a symmetry problem. This produces decreasing σ-fields

\[
\mathcal G_0\supseteq\mathcal G_1\supseteq\cdots,
\qquad Y_n=\mathbb E[Z\mid\mathcal G_n],\quad Z\in L^1.
\]

The tower property becomes \(\mathbb E[Y_n\mid\mathcal G_{n+1}]=Y_{n+1}\), a reverse martingale relation. Physical time has not been reversed: we are projecting onto coarser information. Section 15.8 already guarantees uniform integrability of this whole family.

The general definition only requires Y\_n to be adapted to the decreasing G\_n, integrable at each time, and to satisfy the same reverse conditional-average relation. Iterating the tower property gives Y\_n=E[Y\_0|G\_n], so the conditional-average form does not restrict generality.

Uniform integrability alone does not force a random sequence to converge. We must also prove that these decreasing-information projections cannot oscillate forever. Calling them an ordinary martingale would use the filtration in the wrong direction. What works is reversing each finite observation window.

## 15.13 A finite window can be reversed; the infinite limit needs proof

Fix N and put \(W_j=Y_{N-j}\), \(\mathcal H_j=\mathcal G_{N-j}\), 0≤j≤N. H\_j increases with j, and the tower property gives \(\mathbb E[W_{j+1}\mid\mathcal H_j]=W_j\). This really is a finite-horizon martingale, so the proved upcrossing inequality applies.

Let D\_N(a,b) count completed downcrossings of Y from at least b to at most a. In a finite record, omit observations inside (a,b) and compress consecutive observations on the same side into one run. The remaining low and high runs alternate. Upcrossing and downcrossing counts therefore differ by at most 1, and reversing a record turns downcrossings into upcrossings. This also verifies that the greedy rule of 15.4 attains the greatest possible number of completed crossings: completing one earlier cannot obstruct later ones.

Apply the supermartingale version of 15.4 to the reversed martingale, whose terminal value is Y\_0:

\[
\mathbb E U_N^Y(a,b)
\le\mathbb E D_N^Y(a,b)+1
=\mathbb E U_N^W(a,b)+1
\le\frac{\mathbb E(Y_0-a)^-}{b-a}+1
\le\frac{\mathbb E|Z|+|a|}{b-a}+1.
\]

The bound is independent of N. Monotone convergence for each rational interval, followed by the path argument of 15.5, rules out infinite oscillation. The bound sup\_n E|Y\_n|≤E|Z| and Fatou exclude infinite limits. Hence Y\_n converges almost surely to an integrable V. Uniform integrability and Vitali now give L¹ convergence.

We must still identify the surviving information. Put \(\mathcal G_\infty=\bigcap_n\mathcal G_n\). Choose V as limsup Y\_n wherever that is finite, and zero otherwise. For any fixed m this limsup uses only the tail n≥m, all of whose variables are G\_m-measurable. The same version V is thus measurable for every G\_m, hence for their actual intersection G\_∞. No tacit completeness assumption on the σ-fields is needed.

For A∈G\_∞, all n satisfy E[Y\_n1\_A]=E[Z1\_A]. Passing to the L¹ limit gives E[V1\_A]=E[Z1\_A]. This completes the reverse conditional-expectation limit theorem:

\[
\mathbb E[Z\mid\mathcal G_n]\longrightarrow
\mathbb E[Z\mid\mathcal G_\infty]
\quad\text{a.s. and in }L^1.
\]

We neither presumed that the projection limit existed nor invoked optional sampling. Finite reversal only supplied a uniform crossing budget. The infinite result still came from countably many crossings and tail control.

## 15.14 The information left at the end is not the information held at the start

If Z∈L^p, 1≤p<∞, the reverse conclusion also holds in L^p. Avoid guessing a new higher-order tail condition by first truncating Z to bounded \(Z^{(K)}\). Its conditional averages and limit are bounded by K, so almost sure convergence and DCT give L^p convergence. Conditional contraction and Minkowski from T-LP then yield

\[
\limsup_{n\to\infty}
\|\mathbb E[Z\mid\mathcal G_n]-\mathbb E[Z\mid\mathcal G_\infty]\|_p
\le2\|Z-Z^{(K)}\|_p\longrightarrow0.
\]

The upward and downward theorems look similar but end in different information: one uses the σ-field generated by a union, the other an intersection. Writing “converges to Z” indiscriminately would erase the substance of the problem.

For example, Chapter 12's tail σ-field of an independent sequence is the decreasing limit of \(\mathcal G_n=\sigma(\xi_n,\xi_{n+1},\ldots)\). Kolmogorov's 0–1 law was proved there without martingale theory. It makes every event in the intersection have probability 0 or 1. Thus E[Z|G\_∞]=E Z almost surely for every integrable Z, and reverse averages eventually retain only a constant. Z need not be independent of each G\_n: the conclusion comes from the triviality of the information that finally remains.

This does not prove continuous-time regularization. Selecting versions at uncountably many times, right continuity and Doob–Meyer decomposition require their own hypotheses and arguments. A countable discrete limit cannot replace them.

## 15.15 Fair increments may be dependent and still orthogonal

In Chapter 12, independence allowed variances of a random series to add. We can now see the property directly responsible for that calculation: conditional mean zero given the past.

Let D\_n be F\_n-measurable, belong to L² and satisfy \(\mathbb E[D_n\mid\mathcal F_{n-1}]=0\). Such a sequence consists of martingale differences. Put \(S_n=\sum_{k=1}^nD_k\). Then S is a martingale, and for i<j the variable D\_i is already \(\mathcal F_{j-1}\)-measurable, giving

\[
\mathbb E[D_iD_j]=0,\qquad
\mathbb E S_n^2=\sum_{k=1}^n\mathbb E D_k^2.
\]

The first identity is justified even for unbounded D\_i: truncate it, pull the bounded past factor through the conditional average, and let the truncation level increase, using Cauchy–Schwarz to control the product error. We have not applied a bounded-factor identity to an unbounded factor without justification.

If Σ\_n E D\_n²<∞, the sums are uniformly bounded in L², and 15.11 gives almost sure and L² convergence. Chapter 12's square-moment criterion for independent centered series becomes a special case. The new point is that amplitudes may depend on the past: as long as conditional fairness survives, the orthogonal variance budget still works.

## 15.16 When information permits the order of averaging to be exchanged

Information inside a filtration is nested, so the tower property already fixes the order of projections. Conditional averages onto two nonnested observations cannot simply be interchanged. The extra structure needed is conditional independence, with the conditioning information explicitly named.

For σ-fields A, B and G, say that A and B are conditionally independent given G if, for every bounded A-measurable U and bounded B-measurable V,

\[
\mathbb E[UV\mid\mathcal G]
=\mathbb E[U\mid\mathcal G]\mathbb E[V\mid\mathcal G].
\]

It suffices to check indicators of events in the two classes: extend linearly to simple functions, then apply the bounded function monotone-class argument separately in each variable. T-MCLASS supplies that tool. An equivalent formulation, better suited to information flow, is that every bounded A-measurable U satisfies

\[
\mathbb E[U\mid\mathcal G\vee\mathcal B]=\mathbb E[U\mid\mathcal G].
\]

No conditional density is needed for the proof. Product factorization makes the integrals of U and E[U|G] agree on C∩B for C∈G and B∈B. These intersections form a π-system generating G∨B; π–λ extends the equality and gives the definition of the conditional average. Conversely, pull V through conditioning on G∨B and then condition on G to recover the product formula.

The equivalent formulation proves three useful rules precisely. Forgetting part of B preserves independence. If A is independent of B∨C given G, then A is independent of B given G∨C, since both conditional averages of U equal E[U|G]. If A is independent of B given G and independent of C given G∨B, then

\[
\mathbb E[U\mid\mathcal G\vee\mathcal B\vee\mathcal C]
=\mathbb E[U\mid\mathcal G\vee\mathcal B]
=\mathbb E[U\mid\mathcal G],
\]

so A is independent of B∨C given G. These are decomposition, weak union and contraction. Each rests on a stated conditional-average identity rather than an unexamined transfer of ordinary independence intuition.

If additionally G⊂A∩B, truncation and L¹ contraction extend the equivalent formulation to integrable A-measurable variables. For every X∈L¹ it follows that

\[
\mathbb E[\mathbb E[X\mid\mathcal A]\mid\mathcal B]
=\mathbb E[X\mid\mathcal G]
=\mathbb E[\mathbb E[X\mid\mathcal B]\mid\mathcal A].
\]

The symmetric identity also uses symmetry of conditional independence. Without independence or inclusion, conditional projections cannot be presumed to commute this way. Nor may an intersection rule be added unconditionally: take A=B=C to be the same nontrivial coin σ-field. Given C, A and B are conditionally independent; given B, A and C are conditionally independent. Yet A is certainly not unconditionally independent of B∨C. Stronger independence calculi may require additional positivity assumptions.

## 15.17 Can a posterior judgment finally recognize the truth?

Chapter 2 inferred unknown chances through repetition, and Chapter 9 expressed posterior judgments as conditional averages. We can now separate two assertions that were easily confused: a posterior valuation settling down does not automatically mean it identifies the true parameter.

For example, on the kernel-based sequential experiment space of Chapter 10, first choose θ∈[0,1] from any prior π and then, conditionally on θ, generate independent Bernoulli(θ) observations ξ\_n. For a fixed Borel set B put \(Z=\mathbf1_{\{\theta\in B\}}\) and \(\mathcal F_n=\sigma(\xi_1,\ldots,\xi_n)\). The posterior probability M\_n=E[Z|F\_n] is a bounded closed martingale. Hence

\[
M_n\longrightarrow\mathbb E[\mathbf1_{\{\theta\in B\}}\mid\mathcal F_\infty]
\quad\text{a.s. and in every finite }L^p.
\]

In this model the right side really equals \(\mathbf1_{\{\theta\in B\}}\), but that needs a separate argument. For every fixed θ, Chapter 12's strong law makes the sample frequency converge almost surely to θ. Integrating the conditional probability of this measurable event against π proves the same assertion on the joint space. Set the frequency limit to zero on nonconvergent records: this gives an F\_∞-measurable estimator equal to θ almost surely. Thus Z has an F\_∞-measurable version, and only then does the limit in 15.9 equal Z. The null set here concerns a fixed B. A simultaneous assertion for a family should first restrict to a countable class, not take an uncountable union of exceptions. This is an almost sure result under the joint prior model, not automatically posterior consistency for every externally fixed true parameter.

If the observations are entirely independent of θ, every posterior remains π(B). It is still a bounded, convergent, expectation-preserving fair judgment, but it cannot identify the truth from records containing no information. Probability maintains a useful distinction: convergence theory governs how valuations stabilize; identification depends on what the observations can actually reveal.

## Chapter 15 Conclusion: Fairness is a time-by-time constraint

The game whose initial unit finally vanishes has not disproved fairness. It shows that the average relation at finite times, the settling of an entire path and the expected capital at the endpoint require different conditions to connect them.

The upcrossing ledger explains why infinite oscillation cannot occur without a cost. A tail budget explains why a settled outcome may still lose expected mass. When valuations come from the same integrable terminal quantity, fairness survives the L¹ limit. Whether information grows or shrinks, the final judgment belongs to the σ-field that genuinely remains.

In the finite ledger behind the maximal estimate, we already tried freezing capital at a crossing. Observation still ended at a prescribed step N. If a player may keep waiting and choose when to leave from the record already seen, with no common finite upper bound on that time, what conditions preserve the original average relation? The boundary of fairness moves from how to take a limit to when to stop.

## Historical sources and scope of the proofs

Ville's 1939 book used gambling strategies to examine randomness. In his interview with Snell, Doob recalled inspiration from the book's maximal inequality and Bernoulli strong-law argument while reviewing it. The [Ville archive](https://numdam.org/item/THESE_1939__218__1_0/) and [Doob interview](https://chance.dartmouth.edu/Doob/conversation.html) provide the original book and a participant's recollection. We do not attribute the modern filtration language, every upcrossing argument or this chapter's unified proofs to an identical original formulation by one author. The doubling ledger, truncation arguments and narrative connections here are modern mathematical reconstructions.

The proved scope is discrete time: maximal estimates, upcrossings, almost sure and L¹/L^p convergence, closed martingales, conditional-expectation limits for increasing and decreasing information, and the stated conditional-independence rules. General continuous-time regularization, Doob–Meyer and stochastic integration are not included in these conclusions. [T-LP](../foundations/t-lp.md) supplies the general integral-norm tools used here; [Chapter 7](07-convergence.md), [Chapter 9](09-conditional-expectation.md) and [Chapter 12](12-infinite-sums.md) supply Vitali, conditional averaging and the independent-sequence prerequisites.
