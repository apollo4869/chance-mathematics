# The Mathematics of Chance
Volume II · Probability in Infinite Worlds

# Chapter 13: Why Do Rare Events Produce New Stable Laws?

Beside the ledger lies another sheet, recording only accidents.

An exceptional payoff may prevent an infinite series from converging. But the observer might simply draw a short stroke whenever an exception occurs. Rather than demand a finite total loss, the observer wants to know how many strokes remain in experiments that grow longer while each individual chance grows smaller.

These observations do not conflict. Tail events may recur along one fixed infinite record; in successive batches whose scale is redesigned, the chance per trial can change with the number of trials. The scale between them must be chosen. Shrink every chance too far and nothing remains; increase the number of trials without reducing the chances and the count grows without bound. We seek the boundary at which rarity and accumulation are both visible.

## 13.1 Almost nothing each time need not mean nothing altogether

Set aside the size of an accident. A trial records only occurrence, with value 0 or 1. In batch \(n\), perform \(n\) independent trials with occurrence probability \(p_n\), and call the total \(N_n\). This is a sequence of experimental designs of different sizes, not an extension of a single fixed-parameter record. Independence is required within each batch, not between batches.

The statement \(p_n\to0\) says little about the count. If \(p_n=n^{-2}\), Markov's inequality gives \(P(N_n>0)\le np_n\to0\). If \(p_n=n^{-1/2}\), the mean count is \(\sqrt n\), and the count concentrates around this growing quantity: Chebyshev gives \(P(|N_n-np_n|>np_n/2)\le4/(np_n)\to0\).

Between these cases, the scale worth examining is

\[
p_n\longrightarrow0,\qquad np_n\longrightarrow\lambda\in(0,\infty).
\]

Each individual chance disappears, but their total budget leaves a finite number. That number is not the count that must occur; it specifies the mean of the eventual count. A budget of 3 does not force exactly three strokes on the sheet.

Fix a nonnegative integer \(k\). For \(n\ge k\), the binomial formula becomes

\[
P(N_n=k)=\frac{n(n-1)\cdots(n-k+1)}{k!}\,p_n^k(1-p_n)^{n-k}
\longrightarrow e^{-\lambda}\frac{\lambda^k}{k!}.
\]

The finite product contributes \(\lambda^k/k!\). Since \(\log(1-p_n)=-p_n+O(p_n^2)\) and \(np_n^2=(np_n)p_n\to0\), we also have \((1-p_n)^n\to e^{-\lambda}\). In particular, the chance of no accident does not vanish: it tends to \(e^{-\lambda}\).

The limiting masses form a probability distribution because the exponential series sums them to 1. Denote it by \(\operatorname{Pois}(\lambda)\); for \(\lambda=0\), use the mass concentrated at 0. Summing the series also gives

\[
\mathbb EN=\lambda,\qquad \mathbb E[N(N-1)]=\lambda^2,\qquad \operatorname{Var}(N)=\lambda.
\]

A fixed-\(k\) limit is not permission to ignore tails. Here, however, the limiting masses already sum to 1. Choose a finite \(K\) so that \(0,\ldots,K\) captures nearly all their mass; convergence of finitely many terms then controls both tails. This gives convergence in distribution and, as the next section makes precise, convergence in a stronger distance.

Poisson's name takes us to his 1837 *Researches into the Probabilities of Judgements in Criminal and Civil Cases*. The book treats much more than verdicts, including approximation of Bernoulli experiments in a rare-event regime. Historical questions must be distinguished from present definitions: the arrays, couplings and distance estimates below are modern mathematical reconstructions, not a claim that the original book expressed the entire theory in this form. The [English translation and translator's discussion](https://arxiv.org/abs/1902.02782) help check that distinction.

## 13.2 What calculations does a close approximation justify?

For a fixed threshold, a distribution function suffices. But the observer might ask whether the count is even, or belongs to a chosen collection of integers. An approximation remains incomplete if every new event requires a separate argument about its validity.

For two probabilities on the same measurable space, define their **total variation distance** by

\[
d_{\mathrm{TV}}(\mu,\nu)=\sup_{A}|\mu(A)-\nu(A)|.
\]

It controls all measurable events simultaneously. This chapter uses the normalization between 0 and 1. Some references use a total variation norm twice as large; constants must be read with the convention in view.

If both probabilities live on a countable set \(E\), write \(a_x=\mu\{x\}-\nu\{x\}\). Since \(\sum_xa_x=0\), the positive terms sum to the absolute sum of the negative terms. Every event difference is bounded by the positive sum, and the set of positive terms attains it. Hence

\[
d_{\mathrm{TV}}(\mu,\nu)=\frac12\sum_{x\in E}|\mu\{x\}-\nu\{x\}|=1-\sum_{x\in E}\min(\mu\{x\},\nu\{x\}).
\]

This completes the preceding tail argument: the absolute difference on a finite set tends to zero, while the remaining difference is bounded by the sum of the two tail probabilities. Enlarge the finite set afterward. Generally, pointwise convergence of masses on a common countable set to a probability of total mass 1 implies total variation convergence.

Total variation has a concrete experimental meaning. Place \(U,V\) in one joint experiment. Whenever they agree, every event receives the same answer. Thus

\[
|P(U\in A)-P(V\in A)|\le P(U\ne V),\qquad d_{\mathrm{TV}}(\mathcal L(U),\mathcal L(V))\le P(U\ne V).
\]

On a countable space, equality with the supremum can be achieved. Put \(r_x=\min(\mu\{x\},\nu\{x\})\) and \(r=\sum_xr_x\). With probability \(r\), choose one common outcome according to \(r_x/r\). On the remaining part, draw from the two normalized residual probabilities after removing the common masses. Their supports are disjoint, so the outcomes necessarily differ there. If \(r=0\) or 1, omit the corresponding empty step. This constructs the coupling completely, rather than merely suggesting that the variables be made as similar as possible.

Estimating a distance between laws has become a question about experiments: can the actual experiment and an easier one be arranged so that their records rarely disagree?

## 13.3 Matching one chance with a small Poisson count

Compare just one cell of the record. Let \(B\) have law \(\operatorname{Bern}(p)\) and \(Z\) law \(\operatorname{Pois}(p)\), with \(0\le p\le1\). At 0, \(e^{-p}\ge1-p\); at 1, \(p\ge pe^{-p}\); at 2 and above, only the Poisson law has mass. The Bernoulli law's only excess is at 1, giving

\[
d_{\mathrm{TV}}(\operatorname{Bern}(p),\operatorname{Pois}(p))=p(1-e^{-p})\le p^2.
\]

The quadratic error has a mechanism. One chance can record at most one stroke; the small Poisson count permits two or more in the same cell. First-order occurrence has been matched, leaving discrepancies at a smaller, quadratic scale. The precise distance follows from the mass comparison, not from this interpretation alone.

Now let \(B_1,\ldots,B_m\) be independent, with possibly different success probabilities, and write

\[
N=\sum_{i=1}^mB_i,\qquad \lambda=\sum_{i=1}^mp_i.
\]

For each \(i\), use the common-mass construction to couple \(B_i\) with \(Z_i\sim\operatorname{Pois}(p_i)\), then make these **paired experiments independent of one another**. Chapter 8's finite product construction permits this. Each coordinate sequence has the required independence, and

\[
P\left(\sum_iB_i\ne\sum_iZ_i\right)\le P(\exists i:B_i\ne Z_i)\le\sum_i p_i(1-e^{-p_i})\le\sum_i p_i^2.
\]

Independent Poisson counts add to a Poisson count. For two parameters, convolution at \(k\) gives \(e^{-(a+b)}\sum_{j=0}^k a^jb^{k-j}/(j!(k-j)!)=e^{-(a+b)}(a+b)^k/k!\). Finite induction yields \(\sum_iZ_i\sim\operatorname{Pois}(\lambda)\). Consequently,

\[
\boxed{\ d_{\mathrm{TV}}(\mathcal L(N),\operatorname{Pois}(\lambda))\le\sum_i p_i(1-e^{-p_i})\le\sum_i p_i^2.\ }
\]

This is the **Le Cam type bound** used here. For the sum of absolute mass differences, multiply the right side by 2. The probabilities need not be equal, and no limit is required: every finite experiment satisfying the independent Bernoulli assumptions has this explicit bound. A bound above 1 remains true but supplies no useful precision.

Le Cam's 1960 paper concerns approximation of the Poisson binomial distribution, explicitly treating independent Bernoulli sums with unequal probabilities and a specified measure distance. Our coupling proof establishes the bound and constant stated above; it does not reproduce all the paper's sharper estimates or its original proof. The [original journal article](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p11-p.pdf) also makes clear why a theorem's name cannot replace its metric and normalization.

## 13.4 Why unequal small chances forget their differences

Write a batch as independent indicators \(B_{n1},\ldots,B_{nm_n}\), with \(p_{ni}=P(B_{ni}=1)\). Only within-row independence is required. Put \(N_n=\sum_iB_{ni}\) and \(\lambda_n=\sum_i p_{ni}\). Suppose

\[
\max_{1\le i\le m_n}p_{ni}\longrightarrow0,\qquad \lambda_n\longrightarrow\lambda<\infty,
\]

The sum of probability squares is bounded by \(\lambda_n\max_i p_{ni}\), so it tends to zero. Unequal small chances lose their separate identities within the same quadratic error budget.

The parameter \(\lambda_n\) must also be replaced by \(\lambda\). If \(a\le b\), take independent \(U\sim\operatorname{Pois}(a)\) and \(D\sim\operatorname{Pois}(b-a)\). Then \(U+D\sim\operatorname{Pois}(b)\), and disagreement requires \(D>0\). Thus

\[
d_{\mathrm{TV}}(\operatorname{Pois}(a),\operatorname{Pois}(b))\le1-e^{-|a-b|}\le|a-b|.
\]

The triangle inequality for event differences gives the quantitative non-identically distributed rare-event limit:

\[
d_{\mathrm{TV}}(\mathcal L(N_n),\operatorname{Pois}(\lambda))\le\sum_i p_{ni}^2+|\lambda_n-\lambda|\longrightarrow0.
\]

For example, take \(p_{ni}=2\lambda i/[n(n+1)]\), \(1\le i\le n\), which are legal probabilities for sufficiently large \(n\). Their unequal values sum exactly to \(\lambda\), and their maximum is \(2\lambda/(n+1)\). The error is at most \(2\lambda^2/(n+1)\). Equal chances do not determine the limit; what matters is that no cell retains a finite share and that the total chance budget converges.

The absence of a large cell is even necessary in a precise sense. Still assume \(\lambda_n\to\lambda<\infty\). If \(N_n\) converges in distribution to \(\operatorname{Pois}(\lambda)\), subtract distribution functions at the continuity points \(-1/2,1/2\) to obtain \(P(N_n=0)\to e^{-\lambda}>0\). Eventually no \(p_{ni}=1\), and

\[
0\le\frac12\sum_i p_{ni}^2\le\sum_i[-\log(1-p_{ni})-p_{ni}]=-\log P(N_n=0)-\lambda_n\longrightarrow0.
\]

The inequality follows from \(-\log(1-p)-p=\int_0^p u/(1-u)\,du\ge p^2/2\). Hence \(\max_i p_{ni}\to0\). Under convergence of the total budget, sparsity is not a decorative hypothesis.

## 13.5 The same budget can still describe another world

Keep one ordinary coin with success probability \(q\in(0,1)\), then add independent small chances with total budget \(\lambda-q\), where \(\lambda>q\). The ordinary coin does not disappear. The count tends to an independent sum \(\operatorname{Bern}(q)+\operatorname{Pois}(\lambda-q)\), rather than \(\operatorname{Pois}(\lambda)\): its zero-count probability is \((1-q)e^{-(\lambda-q)}\), different from \(e^{-\lambda}\). Equal means do not erase a visible structure within one cell.

Independence cannot remain an unexamined background word. Take one uniform variable \(U\), and in row \(n\) make all \(n\) indicators equal to \(\mathbf1_{\{U\le\lambda/n\}}\), with \(n\ge\lambda\). Each probability vanishes and the budget is \(\lambda\), but the result is one enormous simultaneous cluster rather than scattered small events:

\[
N_n=n\mathbf1_{\{U\le\lambda/n\}},\qquad N_n\longrightarrow0\ \text{in probability},\qquad \mathbb EN_n=\lambda.
\]

This recreates Chapter 7's spike. A diminishing probability carries an increasing count, and the mean does not follow convergence in probability. The Poisson conclusion fails because the opportunities do not disperse independently, not because their probabilities are insufficiently small.

A milder failure points toward the next theory. Divide \(2n\) positions into \(n\) pairs. Each pair occurs together with probability \(\lambda/(2n)\), independently between pairs. Every position is rare and the total budget remains \(\lambda\), but the count tends to \(2Z\), where \(Z\sim\operatorname{Pois}(\lambda/2)\). Odd counts never have mass. What arrives independently is a cluster of two events, not a single event.

The three-series theorem separates large jumps from small fluctuations; here we must also separate single chances from clustered chances. A small marginal probability specifies neither the dependence nor what one occurrence brings with it.

## 13.6 Recording an entire count distribution in one function

For a nonnegative integer-valued \(N\), take \(0\le z\le1\) and write

\[
G_N(z)=\mathbb E z^N=\sum_{k=0}^\infty P(N=k)z^k,
\]

with \(0^0=1\). This is the **probability generating function**. It always exists on this interval, since \(0\le z^N\le1\), without any finite-moment assumption. Independence turns sums into products, by Chapter 11's independent integration, now using decay instead of rotation.

The function identifies the count law. Letting \(z\downarrow0\) first recovers the mass at 0. Once the preceding \(k\) terms are known, subtract them and divide by \(z^k\). The first remaining term is the coefficient at \(k\); the subsequent tail is bounded by \(z\sum_{j>k}P(N=j)\le z\). Letting \(z\downarrow0\) again recovers that coefficient, and induction recovers every mass. No complex-analytic uniqueness theorem for power series is needed.

The Poisson and Bernoulli generating functions are

\[
G_{\operatorname{Pois}(\lambda)}(z)=e^{\lambda(z-1)},\qquad G_{\operatorname{Bern}(p)}(z)=1+p(z-1).
\]

Independent rare chances give a product; Poisson gives an exponential. Put \(w=1-z\). As the maximum probability vanishes, \(\log(1-p_{ni}w)=-p_{ni}w+O(p_{ni}^2w^2)\), with the total remainder controlled by the square budget. The product leaves only \(e^{-\lambda w}\). This expresses the coupling mechanism in another language: first-order contributions accumulate, while second-order collisions disappear.

But convergence of function values needs a limit theorem that prevents lost mass. If \(N_n=n\), then \(G_{N_n}(z)\to0\) for every \(z<1\), while the value at 1 remains 1. No finite integer-valued random variable has this generating function. Probability has escaped to infinity; pointwise limits inside the interval miss all of it.

To handle losses of different sizes, we extend the decaying reading to all nonnegative real variables. Generating functions are not an isolated trick; they already stand at the entrance to another transform.

## 13.7 Another reading that does not explode at large values

An accident may carry a nonnegative loss in addition to its count. Positive exponentials magnify distant outcomes; Chapter 11 explained why their expectations may fail. Reversing the direction gives a nonnegative variable's **Laplace transform**:

\[
L_X(s)=\mathbb E e^{-sX},\qquad s\ge0,\quad 0\le X<\infty\ \text{a.s.}
\]

It lies between 0 and 1, and DCT gives \(L_X(s)\to1\) as \(s\downarrow0\). Independent nonnegative sums turn transforms into products. For integer counts, \(L_N(s)=G_N(e^{-s})\). None of these statements assumes a mean or exchanges integration with an unjustified moment expansion.

Why can decaying readings identify a whole law? Put \(Y=e^{-X}\in(0,1]\). Knowing all \(L_X(s)\), in particular their values at integers \(s=k\), supplies all integer moments of \(Y\) on a compact interval. Chapter 11 warned that even all moments need not identify a distribution. The common compact support is the crucial change here.

We now need to connect a sequence of moment readings to arbitrary continuous observations. The moments already determine the integral of every polynomial. If polynomials approximate continuous functions uniformly, equal moments force equal averages for all continuous observations. Bernstein polynomials make this bridge a binomial average: sampling locations concentrate near the specified point, so the average reading approaches the function value there.

We prove the approximation tool, rather than borrowing the compact moment problem as a black box. For continuous \(g\) on \([0,1]^d\), define the Bernstein polynomial

\[
B_mg(y)=\sum_{k_1,\ldots,k_d=0}^m g(k_1/m,\ldots,k_d/m)\prod_{j=1}^d\binom m{k_j}y_j^{k_j}(1-y_j)^{m-k_j}.
\]

For fixed \(y\), this is the expectation of \(g(K_1/m,\ldots,K_d/m)\), with independent binomial variables \(K_j\) of parameters \((m,y_j)\). A continuous function on the compact cube is uniformly continuous. Given \(\varepsilon>0\), choose \(\delta>0\) so that coordinatewise maximum distance at most \(\delta\) gives function-value difference at most \(\varepsilon\). Chebyshev and the union bound yield

\[
\sup_y|B_mg(y)-g(y)|\le\varepsilon+2\|g\|_\infty\frac{d}{4m\delta^2}\longrightarrow\varepsilon.
\]

Letting \(\varepsilon\downarrow0\) proves uniform polynomial approximation. Two cube probabilities with the same mixed moments integrate polynomials, and hence all continuous functions, equally. Approximate indicators of closed lower rectangles by continuous decreasing ramps and apply DCT. These rectangles form a generating Borel \(\pi\)-class, so the [\(\pi\)–\(\lambda\) theorem](../foundations/t-mclass.md#t-mclass-uniqueness) identifies the probabilities.

Explicit ramps are \(\prod_j[1-m(y_j-a_j)_+]_+\), converging to \(\mathbf1_{\{y_j\le a_j,\ \forall j\}}\) on the cube. Boundary atoms are therefore included. Pulling the identical law back through the measurable inverse \(x_j=-\log y_j\) proves Laplace uniqueness for finite nonnegative vectors:

\[
\mathbb E e^{-\sum_{j=1}^d s_jX_j}=\mathbb E e^{-\sum_{j=1}^d s_j\widetilde X_j}\quad(\forall s_j\ge0)
\quad\Longrightarrow\quad \mathcal L(X)=\mathcal L(\widetilde X).
\]

These are finite-dimensional vectors with finitely many coordinates in the transform. This does not establish a general point process Laplace-functional theory in advance.

## 13.8 How limiting readings prevent escaping probability

Uniqueness asks whether an answer, if present, is unique. A limit argument must also ensure existence and stop decay from concealing mass escaping to infinity. For nonnegative real variables, a direct tail estimate is

\[
P(X>M)\le\frac{1-L_X(s)}{1-e^{-sM}},\qquad s>0,\ M>0.
\]

Indeed, on \(X>M\), we have \(1-e^{-sX}\ge1-e^{-sM}\). Like Chapter 11's low-frequency tightness estimate, readings near the origin control mass far away.

There are now two separate obstacles. Bernstein approximation takes us from converging moments to converging continuous observations on the compact cube. But recovering the original values from the decaying readings magnifies the region near zero into a distant tail. The preceding tail bound guards precisely this exit. The proof below joins these two mechanisms instead of declaring convergence of laws from converging transforms alone.

First state a finite-dimensional conclusion with no ambiguity about existence. If \(X_n,X\) are almost surely finite nonnegative \(d\)-vectors, then

\[
X_n\Rightarrow X\quad\Longleftrightarrow\quad L_{X_n}(s)\longrightarrow L_X(s)\quad(\forall s\in[0,\infty)^d).
\]

Convergence in distribution here means convergence of expectations of all bounded continuous functions. The forward implication uses bounded continuity of exponentials. Conversely, put \(Y_{nj}=e^{-X_{nj}}\), \(Y_j=e^{-X_j}\). Mixed-moment convergence gives convergence of polynomial expectations, and uniform approximation then gives convergence for every continuous function on the cube.

We cannot immediately apply the same argument to \(-\log\), which is unbounded at 0. Apply the tail estimate to each coordinate. First take small \(s>0\), using \(L_X(se_j)\to1\), then large \(M\) so that the denominator approaches 1. This makes \(\limsup_nP(\max_jX_{nj}>M)\) arbitrarily small; the corresponding tail of \(X\) is also small. A finite union bound suffices, with no infinite-dimensional tightness theorem.

For bounded continuous \(f\), use \(f(-\log y_1,\ldots,-\log y_d)\) where \(y_j\ge e^{-M}\), then extend it continuously to the cube: replace each \(y_j\) by \(\max(y_j,e^{-(M+1)})\), and multiply by continuous ramps that are 0 for \(y_j\le e^{-(M+1)}\) and 1 for \(y_j\ge e^{-M}\). The resulting function is bounded continuous and agrees with \(f(X)\) when every \(X_j\le M\). Each truncation error in expectation is at most \(2\|f\|_\infty\) times the corresponding tail probability. Let \(n\to\infty\), then reduce the tails to zero. This proves the reverse implication.

For real variables, a candidate variable need not be supplied. If \(L_{X_n}(s)\to L(s)\) for all \(s\ge0\), with \(L(0)=1\) and right continuity of \(L\) at 0, there is a unique finite nonnegative limiting law. The tail bound first gives uniform tightness of \(\{\mathcal L(X_n)\}\): the limiting readings control all sufficiently late \(n\), and finitely many initial tails are handled by enlarging the window. The [real-line selection argument of Chapter 11](11-characteristic-functions.md) supplies a weakly convergent subsequence of every subsequence.

These limits remain nonnegative: the bounded continuous function \(\min(1,(-x)_+)\) must have integral 0. Testing with the bounded continuous extension \(e^{-s\max(x,0)}\) gives limiting Laplace transform \(L\). Uniqueness identifies every subsequential limit. If an expectation of a bounded continuous test failed to converge, take a subsequence separated from that limit and then a convergent subsubsequence, a contradiction. Thus the whole sequence converges, without using general Prokhorov theory.

Consequently, a pointwise limit of probability generating functions that is continuous at 1 and equals 1 there gives a finite integer-valued limit. Use \(s=-\log z\) and the real-line conclusion, then test with \(\min(1,\operatorname{dist}(x,\mathbb N_0))\) to see that the limit stays on \(\mathbb N_0\). Pointwise masses then upgrade to total variation convergence. Continuity near the origin or endpoint prevents the complete escape exhibited by \(N_n=n\).

## 13.9 A short stroke may carry a loss of a different size

Attach a mark \(J\) to each accident. Initially let its possible values be a finite or countable set of real numbers, with law \(Q\). The mark may describe a loss size or an accident type. Its probabilities must be specified by the model; rarity alone does not determine them.

Take \(N\sim\operatorname{Pois}(\lambda)\), independent of i.i.d. marks \(J_1,J_2,\ldots\), and define

\[
S=\sum_{r=1}^N J_r,\qquad \sum_{r=1}^0J_r=0.
\]

Chapter 8 supplies the product space. Since \(N\) is almost surely finite, no random-series convergence theorem is needed for this sum. Its law is **compound Poisson**. A random number is selected first, then each occurrence receives an independent mark; the two random layers must remain distinct.

Write \(\phi_Q(t)=\mathbb E e^{itJ}\). Grouping by \(N\), with modulus bounded by 1 to justify the integrations, gives

\[
\mathbb E e^{itS}=\sum_{k=0}^\infty e^{-\lambda}\frac{\lambda^k}{k!}\phi_Q(t)^k
=\exp\{\lambda(\phi_Q(t)-1)\}.
\]

For nonnegative marks, likewise \(L_S(s)=\exp\{\lambda(L_J(s)-1)\}\). For nonnegative integer marks, \(G_S(z)=\exp\{\lambda(G_J(z)-1)\}\). These are three readings of one construction, not three independently guessed definitions.

If \(\mathbb E|J|<\infty\), conditional expectation gives \(\mathbb ES=\lambda\mathbb EJ\). If \(\mathbb EJ^2<\infty\), conditional variance decomposition gives

\[
\operatorname{Var}(S)=\lambda\operatorname{Var}(J)+\lambda(\mathbb EJ)^2=\lambda\mathbb EJ^2.
\]

Marks constantly equal to 1 recover ordinary Poisson; marks constantly equal to 2 recover the independent pair-cluster limit. Random loss size and random accident count both contribute to variance, which is not merely \(\lambda\operatorname{Var}(J)\). Without these moments, the law and bounded transforms still exist, but the moment formulas cannot be used unconditionally.

Suppose each independent Bernoulli occurrence receives a mark independent of its indicator, with common law \(Q\). Given the count, the selected marks are still independent \(Q\) samples. Couple the count to its Poisson counterpart as before, and use the same independent mark sequence for both. Equal counts then give equal sums. Hence

\[
d_{\mathrm{TV}}\left(\mathcal L\left(\sum_iB_iJ_i\right),\mathcal L\left(\sum_{r=1}^{N}J_r\right)\right)\le\sum_i p_i^2,\qquad N\sim\operatorname{Pois}\left(\sum_i p_i\right).
\]

No mean or variance assumption on the marks is needed. The estimate controls disagreement between total-loss experiments, rather than beginning with a comparison of means that may not exist.

## 13.10 Why independent colour counts survive random classification

Give every occurrence an independent colour, with probabilities \(q_1,\ldots,q_r\), grouping the rest into probability \(q_0=1-\sum_{j=1}^r q_j\). Let \(C_j\) count colour \(j\). Given \(N\), these counts are constrained by their sum and are not independent. Averaging over the random total surprisingly removes the constraint.

Fix \(k_1,\ldots,k_r\) and sum over the remaining count \(k_0\). Conditional multinomial counting yields

\[
P(C_1=k_1,\ldots,C_r=k_r)
=e^{-\lambda}\prod_{j=1}^r\frac{(\lambda q_j)^{k_j}}{k_j!}\sum_{k_0=0}^\infty\frac{(\lambda q_0)^{k_0}}{k_0!}
=\prod_{j=1}^r e^{-\lambda q_j}\frac{(\lambda q_j)^{k_j}}{k_j!}.
\]

Thus the colour counts are independent, with laws \(\operatorname{Pois}(\lambda q_j)\). Zero colour probabilities use \(0^0=1\). For countably many colours, select any finite group, merge the others, and repeat the calculation. This proves independence of every finite collection; only finitely many colours can actually occur because the total count is finite.

This is the splitting property of independent marking. A Poisson total alone does not automatically give independent category counts. If all accidents share one random colour coin, the red and blue counts cannot both be positive, even though the total is Poisson. The independent-mark assumption has failed.

For the original rare experiments, couple each Bernoulli cell with a small Poisson count and prepare independent marks within each cell, sharing them whenever counts agree. If every cell matches, all colour counts match simultaneously. The same square budget therefore bounds total variation error for the **whole classified record**, not merely each marginal count. Independent Poisson limits for finitely many colours do not follow from Poisson marginal limits alone; the common coupling supplies the joint argument.

## 13.11 When marks also change, what must remain?

Different opportunities may bring different losses. Cell \(i\) of row \(n\) has occurrence probability \(p_{ni}\) and mark law \(Q_{ni}\). Within each cell the indicator and mark are independent, and whole paired experiments are independent across cells. Keep marks in one fixed countable real set \(E\), and define the finite intensity account

\[
\nu_n\{a\}=\sum_i p_{ni}Q_{ni}\{a\},\qquad a\in E,\qquad \nu_n(E)=\lambda_n.
\]

Replace each Bernoulli cell by a Poisson count of parameter \(p_{ni}\), retaining its mark law. Cellwise coupling bounds the total-loss error by \(\sum_i p_{ni}^2\). The replacement has characteristic function

\[
\exp\left\{\sum_i p_{ni}(\phi_{Q_{ni}}(t)-1)\right\}
=\exp\left\{\sum_{a\in E}(e^{ita}-1)\nu_n\{a\}\right\}.
\]

For \(\lambda_n>0\), this is the compound Poisson reading with total count parameter \(\lambda_n\) and mark law \(\nu_n/\lambda_n\); Chapter 11's real-line uniqueness identifies the sum laws. If \(\lambda_n=0\), the sum is 0. Finite intensity makes the series absolutely convergent, without a general Poisson random measure.

Suppose a finite measure \(\nu\) satisfies \(\nu_n\{a\}\to\nu\{a\}\) for every \(a\in E\), and \(\lambda_n\to\nu(E)<\infty\). Choose a finite mark set leaving little \(\nu\)-mass outside. On that set there is termwise convergence; total masses converge as well, so both remaining masses are small. This proves

\[
\|\nu_n-\nu\|_1:=\sum_{a\in E}|\nu_n\{a\}-\nu\{a\}|\longrightarrow0.
\]

Split the two finite intensities into their common masses \(\min(\nu_n\{a\},\nu\{a\})\) and two residuals, constructing independent compound Poisson sums. Share the common experiment. The residual total intensities add to \(\|\nu_n-\nu\|_1\). If neither residual occurs, the sums agree, so their distance is at most \(1-e^{-\|\nu_n-\nu\|_1}\). Adding intensities restores the required laws, directly by their characteristic exponents and uniqueness. Combined with the cellwise error,

\[
d_{\mathrm{TV}}\left(\mathcal L\left(\sum_iB_{ni}J_{ni}\right),\operatorname{CP}(\nu)\right)
\le\sum_i p_{ni}^2+\|\nu_n-\nu\|_1.
\]

Here \(\operatorname{CP}(\nu)\) denotes the law constructed from total intensity and normalized marks. The condition \(\max_i p_{ni}\to0\) with a bounded total budget sends the first term to zero; no escape in the mark account sends the second to zero. The terms have separate responsibilities.

If each mark instead equals \(n\), while the count parameter stays \(\lambda>0\), the loss is \(S_n=nN\). For any fixed \(M\), whenever \(n>M\), \(P(S_n>M)=1-e^{-\lambda}\), so these laws are not uniformly tight. Their Laplace transforms tend to \(e^{-\lambda}\) for each \(s>0\), but equal 1 at 0. The count remained while the size escaped. Checking total intensity alone cannot establish a finite loss limit.

## 13.12 When accidents are no longer few, the bell curve returns

Poisson and Gaussian are not disconnected worlds. For \(N_\lambda\sim\operatorname{Pois}(\lambda)\), as \(\lambda\to\infty\), the centered and standardized characteristic function is

\[
\mathbb E\exp\left\{it\frac{N_\lambda-\lambda}{\sqrt\lambda}\right\}
=\exp\left\{\lambda\left(e^{it/\sqrt\lambda}-1-\frac{it}{\sqrt\lambda}\right)\right\}
\longrightarrow e^{-t^2/2}.
\]

For fixed \(t\), the exponent remainder is \(O(|t|^3/\sqrt\lambda)\); Chapter 11's Lévy continuity theorem gives the standard Gaussian limit. First retain a finite total count across small cells to obtain Poisson; then increase that count budget and observe centered fluctuations to see the bell shape again.

For binomial experiments, if \(np_n\to\infty\) and \(np_n^2\to0\), Le Cam's bound first replaces the count in total variation by Poisson of parameter \(np_n\). Subtracting \(np_n\) and dividing by \(\sqrt{np_n}\) then gives the Gaussian weak limit. The square condition is sufficient for this two-step proof, **not** necessary for a binomial CLT: fixed \(p\in(0,1)\) already demonstrates that. A method's limitation must not become a false boundary for the limit itself.

Yet a stroke on the sheet always gives an integer. The question of exactly \(k\) occurrences is not answered by Gaussian weak convergence. That controls fixed standardized intervals; one integer point occupies a cell of width about \(1/\sqrt n\) after scaling. The cell shrinks with the experiment, so a fixed-test limit cannot simply be substituted.

## 13.13 Empty cells the limiting curve cannot see

Take the simplest symmetric random walk, with steps \(-1\) and 1. Chapter 11 proves that position divided by \(\sqrt n\) tends to standard Gaussian. But at step \(n\), position has the same parity as \(n\): at odd times it cannot be 0, and at even times it cannot be 1.

The Gaussian density is positive near all these points. Multiplying density by an integer-cell width and calling it a point probability immediately fails on half the cells. Weak convergence sees the large-scale bell shape; it does not fill cells that were never available.

There is a stronger distinction. Let \(\mu_n\) be any such standardized lattice-sum law and \(\gamma\) standard Gaussian probability. The countable support \(A_n\) of \(\mu_n\) has \(\mu_n\)-probability 1 and \(\gamma\)-probability 0. Even with weak convergence,

\[
d_{\mathrm{TV}}(\mu_n,\gamma)=1\qquad(n\ge1).
\]

This does not contradict Le Cam's bound, whose two laws share an integer counting space. Here one is discrete and the other continuous. We need a local approximation respecting cell width before discussing total variation after a suitable discretization.

## 13.14 Where the true lattice spacing is hidden in frequency

In 1948, Gnedenko published “On a local limit theorem of the theory of probability” in Uspekhi Matematicheskikh Nauk, volume 3, issue 3(25), pages 187–194; see the [original publication record](https://www.mathnet.ru/eng/rm8713). A local limit asks how much mass each allowed lattice site receives beneath the overall bell-shaped profile. Below we establish this conclusion anew from lattice span and Fourier inversion. This is a modern reconstruction for this book, not a reproduction of the 1948 proof.

Suppose \(X\) is supported on \(a+h\mathbb Z\), with \(h>0\). Call \(h\) the **maximal lattice span** if no larger positive spacing contains the same support, even after changing the offset. We consider nondegenerate laws; a constant variable has neither the finite maximal span nor the positive variance required here.

Put \(Y=(X-a)/h\), so \(Y\) is integer-valued. Maximality means that the greatest common divisor of integer support differences is 1; otherwise the support lies in a sparser residue class and the span of \(X\) can be enlarged. Finitely many such differences have an integer linear combination equal to 1: the positive gcd obtained by adding differences can decrease only finitely often, after which Euclid's algorithm applies.

The characteristic function is \(\phi_Y(t)=\mathbb E e^{itY}\). A unit-modulus random variable has a unit-modulus mean exactly when it is almost surely constant, since \(\mathbb E|Z-\mathbb EZ|^2=1-|\mathbb EZ|^2\). Thus \(|\phi_Y(t)|=1\) forces every support difference \(d\) to satisfy \(td\in2\pi\mathbb Z\). Taking the finite integer linear combination gives \(t\in2\pi\mathbb Z\). Therefore

\[
|\phi_Y(t)|<1\quad(0<|t|\le\pi),\qquad
\sup_{\delta\le|t|\le\pi}|\phi_Y(t)|=\rho_\delta<1\quad(0<\delta<\pi).
\]

The last step uses continuity and a maximum on a compact set. This does not assume 0 is in the support. For example, the original \(\{-1,1\}\) variable has span 2; only after changing to \(Y=(X+1)/2\in\{0,1\}\) does it have span 1. The sum's lattice also shifts with \(n\).

Integer probabilities have an exact inversion formula. For integer-valued \(T\), bounded integration over a finite interval and Fubini give

\[
P(T=k)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-itk}\phi_T(t)\,dt,
\]

because for every integer \(j\), \((2\pi)^{-1}\int_{-\pi}^{\pi}e^{it(j-k)}\,dt\) is 1 at \(j=k\) and 0 otherwise. A finite frequency interval suffices. Maximal span ensures that, except at the origin, this interval has no further unit-modulus reading that survives repeated multiplication.

## 13.15 Recovering one cell from the whole frequency interval

We can now state the finite-variance lattice local central limit theorem precisely. Let \(X_1,X_2,\ldots\) be i.i.d., with mean \(\mu\), variance \(0<\sigma^2<\infty\), and support on \(a+h\mathbb Z\), where \(h\) is maximal. Write \(S_n=\sum_{j=1}^nX_j\), and put

\[
x_{nk}=\frac{na+hk-n\mu}{\sigma\sqrt n},\qquad
\varphi(x)=\frac1{\sqrt{2\pi}}e^{-x^2/2}.
\]

Then, uniformly over all integers \(k\),

\[
\boxed{\ \sup_{k\in\mathbb Z}\left|\frac{\sigma\sqrt n}{h}P(S_n=na+hk)-\varphi(x_{nk})\right|\longrightarrow0.\ }
\]

No third moment, finite support or positive mass at every lattice point is required. Maximal span removes a genuine periodicity obstruction; finite variance controls the quadratic shape near the origin. They solve different problems.

For the proof, change to integer units. Put \(Y_j=(X_j-a)/h\), with mean \(b=(\mu-a)/h\), standard deviation \(v=\sigma/h>0\), and centered characteristic function \(\chi(t)=\mathbb E e^{it(Y_1-b)}\). Chapter 11 established under a finite second moment that

\[
\chi(t)=1-\frac{v^2t^2}{2}+o(t^2),\qquad
\chi\left(\frac{u}{v\sqrt n}\right)^n\longrightarrow e^{-u^2/2}\quad(u\in\mathbb R).
\]

Apply the preceding inversion to \(Y_1+\cdots+Y_n\), then change variables \(u=v\sqrt n\,t\). This gives

\[
v\sqrt n\,P(S_n=na+hk)=\frac1{2\pi}\int_{-\pi v\sqrt n}^{\pi v\sqrt n}e^{-iux_{nk}}\chi\left(\frac{u}{v\sqrt n}\right)^n\,du.
\]

Chapter 11's Gaussian inversion uses the normalization

\[
\varphi(x)=\frac1{2\pi}\int_{\mathbb R}e^{-iux}e^{-u^2/2}\,du.
\]

Only the amplitudes differ; the oscillating factor always has modulus 1. Convergence of the two amplitudes in \(L^1\) over the whole line would control every cell simultaneously, instead of taking a separate limit for each \(k\). This full-frequency integral control is the additional mathematical cost of a local theorem.

## 13.16 Shape survives near zero; distant frequencies are multiplied away

The second-order expansion gives \(|\chi(t)|^2=1-v^2t^2+o(t^2)\). Choose \(\delta\in(0,\pi)\) so that for \(|t|\le\delta\),

\[
|\chi(t)|\le e^{-v^2t^2/4},\qquad
\left|\chi\left(\frac{u}{v\sqrt n}\right)^n\right|\le e^{-u^2/4}\quad(|u|\le\delta v\sqrt n).
\]

For instance, first bound the squared modulus by \(1-v^2t^2/2\), then use \(1-r\le e^{-r}\) and take square roots. The near-origin amplitude is controlled by one integrable function, not just by 1. The latter would not suffice on an expanding integration interval.

For each fixed \(u\), the near-origin region eventually contains it and the amplitude tends to \(e^{-u^2/2}\). DCT gives

\[
\int_{\mathbb R}\left|\mathbf1_{\{|u|\le\delta v\sqrt n\}}\chi\left(\frac{u}{v\sqrt n}\right)^n-e^{-u^2/2}\right|\,du\longrightarrow0.
\]

The integrable control is \(e^{-u^2/4}+e^{-u^2/2}\). The [general integration and DCT supplement](../foundations/t-integral.md#t-integral-dct) shows why this does not require finite Lebesgue measure of the whole line.

The remaining frequencies satisfy \(\delta v\sqrt n<|u|\le\pi v\sqrt n\). Maximal span gives \(\rho_\delta<1\), and centering does not change modulus, so

\[
\int_{\delta v\sqrt n<|u|\le\pi v\sqrt n}\left|\chi\left(\frac{u}{v\sqrt n}\right)\right|^n\,du
\le2\pi v\sqrt n\,\rho_\delta^n\longrightarrow0.
\]

Combining the distant-frequency estimate with near-origin \(L^1\) convergence gives \(L^1\) convergence of the entire truncated amplitude to the Gaussian amplitude. The inversion difference is bounded by that distance divided by \(2\pi\), independently of \(x_{nk}\). Taking the supremum over all integers \(k\) completes the local CLT proof.

Neither part can replace the other. The weak CLT uses fixed frequencies after scaling; the local CLT must also suppress the rest of the inversion interval. Periodicity leaves distant unit-modulus points and defeats precisely that suppression.

## 13.17 Why a normal curve cannot fill the odd cells

For independent Bernoulli sums with fixed \(p\in(0,1)\), maximal span is 1, and the local CLT gives

\[
P(\operatorname{Bin}(n,p)=k)=\frac1{\sqrt{np(1-p)}}\varphi\left(\frac{k-np}{\sqrt{np(1-p)}}\right)+o(n^{-1/2}),
\]

with remainder uniform over all integers \(k\). This supplies a modern finite-variance framework for Chapter 3's local binomial bell approximation, without retelling its history or promising every error rate discussed there. Here \(p\) is fixed; the theorem cannot be applied without qualification to a rare parameter changing with \(n\).

For the symmetric walk \(X_j=\pm1\), take \(a=-1\), \(h=2\), \(\sigma=1\). Only at positions \(k\equiv n\pmod2\) do we have

\[
P(S_n=k)=\frac2{\sqrt n}\varphi\left(\frac{k}{\sqrt n}\right)+o(n^{-1/2}).
\]

The wrong-parity cells have probability exactly 0. In particular, for even \(n\), \(\sqrt nP(S_n=0)\to2\varphi(0)\); for odd \(n\) it is always 0. Using maximal span 1 by mistake gives the wrong constant even at the center. The missing half of the positions has not lost probability; it doubles the mass on available positions.

This also explains why subtracting two distribution functions after a weak CLT does not finish a local proof. Point probabilities require precision of order \(n^{-1/2}\). A distribution-function error without a rate may tend to zero while exceeding the point mass itself. Full-interval Fourier control supplies the missing information.

## 13.18 For total variation, first put both laws on the same grid

Assign Gaussian probability to the same grid to remove the continuous–discrete obstruction. Let \(d_n=h/(\sigma\sqrt n)\), and define a probability on integer labels by

\[
q_n(k)=\int_{x_{nk}-d_n/2}^{x_{nk}+d_n/2}\varphi(u)\,du.
\]

Taking all cells left-closed and right-open makes them disjoint and covers the line, so \(\sum_kq_n(k)=1\). No Gaussian point is being given positive mass; an interval's entire mass is assigned to one grid point.

Write \(p_n(k)=P(S_n=na+hk)\). Uniform continuity of the Gaussian density gives \(\sup_k|q_n(k)/d_n-\varphi(x_{nk})|\to0\). Together with the local CLT, \(\sup_k|p_n(k)-q_n(k)|/d_n\to0\). We still cannot sum infinitely many uniformly small errors without further control.

Fix \(R>0\). The central region \(|x_{nk}|\le R\) has at most \(2R/d_n+2\) cells, so its sum of absolute differences tends to zero. Outside, Chebyshev gives \(\sum_{|x_{nk}|>R}p_n(k)\le R^{-2}\). The corresponding Gaussian cells lie within \(|u|>R-d_n/2\), bounding the \(q_n\) tail by that Gaussian tail. Consequently,

\[
\limsup_n d_{\mathrm{TV}}(p_n,q_n)\le\frac12\left(R^{-2}+\int_{|u|\ge R}\varphi(u)\,du\right).
\]

Letting \(R\to\infty\) proves total variation convergence between the discrete sum and the **discretized Gaussian**. Local precision controls the center and a tail budget controls the outside. Without both, pointwise or local estimates cannot be upgraded to total variation.

Three conclusions can now be separated accurately. Weak convergence compares bounded continuous observations; the local CLT compares a single cell's mass to density times cell width; total variation compares all events within a common space. They are connected but are not interchangeable formulations of one statement.

## 13.19 Conditions that cannot quietly be removed

Finite variance provides integrable Gaussian control in the local proof; it is not merely a computational convenience. Consider a symmetric integer law with \(P(X=k)=P(X=-k)=c k^{-5/2}\), \(k\ge1\), normalized by \(c\). It has a finite first absolute moment and mean 0, but infinite second moment. The gcd of support differences is still 1.

Its characteristic function is real. For small \(|t|>0\), keep just \(1/|t|\le k\le2/|t|\). On that range \(1-\cos(kt)\) has a positive common lower bound, and there are order \(1/|t|\) integers. Hence for some \(C>0\),

\[
1-\phi_X(t)=2c\sum_{k\ge1}\frac{1-\cos(kt)}{k^{5/2}}\ge C|t|^{3/2}.
\]

Continuity makes \(\phi_X(t)\) positive near the origin. For fixed nonzero \(u\), the independent sum at square-root scale therefore satisfies

\[
0\le\phi_X(u/\sqrt n)^n\le\exp\{-C|u|^{3/2}n^{1/4}\}\longrightarrow0.
\]

At 0 the value remains 1. This cannot be the continuous characteristic function of any finite weak limit. The square-root standardized sums have no finite weak limit, let alone the stated Gaussian local limit. Chapter 12's first-moment strong law still applies. Stable averages and the correct fluctuation scale again have different responsibilities.

Besides maximal span, the **lattice** assumption itself specifies the scope of this local statement. If \(X\) takes \(0,1,\sqrt2\) with equal probabilities, it is nonlattice, bounded and has positive variance, so the finite-variance weak CLT holds. Every finite sum nevertheless consists of finitely many atoms and has no Lebesgue density. One cannot assert pointwise convergence of its density to Gaussian. Nonlattice small-interval and density local theorems have different statements and additional conditions; they are not obtained by erasing \(h\) from this formula.

The local CLT here also supplies absolute error, not relative error throughout remote tails, nor a universal convergence rate based solely on finite variance. Outside a binomial sum's support, its mass is exactly 0 while Gaussian density remains positive. That already prevents reading a uniform absolute approximation as an everywhere valid relative approximation.

## Chapter 13 Epilogue: Rare events have not been averaged away

The strokes on the sheet are no longer merely exceptions beside the ledger. Vanishing individual chances need not disappear from a long record. If the total budget stays finite and no cell or dependent cluster secretly retains an excessive share, the final count preserves an identifiable random law.

If a stroke also carries a loss size, counting strokes alone is insufficient. Marks separate occurrence from consequence; common-part couplings show which small differences disappear. Decaying readings near the origin remind us that even when counts remain, their sizes can still escape to infinity.

The bell curve has not departed either. As the budget grows, centered Poisson fluctuations return to Gaussian scale. But a smooth curve cannot see parity or empty grid cells. To calculate exactly one count, every part of the inversion interval must be controlled, beyond limits at fixed frequencies.

Many independent summands may leave continuous small fluctuations, sparse jumps, or no finite limit at square-root scale. Put them into experiments changing row by row, allowing sizes, tails and chances to vary together, and a broader question becomes unavoidable: which structures determine the limiting shape, and which conditions prevent one term from owning the entire answer?

## History and further reading

For Poisson's title and historical context, consult Oscar Sheynin's [translation and commentary](https://arxiv.org/abs/1902.02782). This chapter does not attribute the entire modern system of Poisson masses, coupling distances and triangular arrays to the historical text. The accident sheet and loss ledger are modern teaching models, not undocumented historical experiments.

Le Cam, *An approximation theorem for the Poisson binomial distribution*, *Pacific Journal of Mathematics* 10 (1960), 1181–1197: [original publisher article](https://msp.org/pjm/1960/10-4/pjm-v10-n4-p11-p.pdf). This chapter independently proves its stated \(d_{\mathrm{TV}}\le\sum p_i^2\) bound. The reference's measure norm and sharper estimates are distinguished from our normalization.

For modern Poisson and local limit theory, see Durrett's [author-hosted textbook](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf). The finite-variance lattice proof here uses established integration, characteristic functions, real-line selection and \(\pi\)–\(\lambda\) tools, without borrowing later Poisson process or general point process existence theorems.

The book's breadth continues to be compared with the [official record of Kallenberg's third edition](https://link.springer.com/book/10.1007/978-3-030-61871-1). This chapter's models, order of argument and narrative follow its counting problem. A Poisson rare-count limit is not a classification of all infinitesimal arrays, and independent marking at finite intensity is not general random measure theory.
