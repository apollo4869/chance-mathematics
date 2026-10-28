# Chapter 17: Does the Present Suffice to Determine the Future?

At a lattice site, the chances of moving left or right do not depend on how many streets were traversed before arrival. Standing at the same place again seems to restore the same future.

Randomness alone does not guarantee this. If a coin's bias is an unknown parameter, earlier observations alter our prediction of the next toss; current position need not record every useful piece of information. For a return to be a genuine restart, we must identify what the present summarizes and what remains hidden in the past.

## 17.1 A state is not merely the number displayed on a screen

Suppose a screen records only whether the latest toss was zero or one. Keeping this present value seems economical and reasonable: conditional on the coin's bias, tosses really are independent. Testing whether the record suffices does not require an abstract definition first. Look for two past records with the same display but different predictions for the next toss.

The unknown-bias coin makes an insufficient state into a calculable failure. First choose \(\Theta=1/4\) or \(3/4\) with equal probabilities; conditional on it, toss independently with success indicators \(B_1,B_2,\ldots\). After the record 00, the posterior probability of the larger bias is \(1/10\); after 10, it is \(1/2\). Consequently,

\[
P(B_3=1\mid B_1B_2=00)=\frac3{10},\qquad
P(B_3=1\mid B_1B_2=10)=\frac12.
\]

Both posterior numbers can be checked directly. Equal prior weights cancel in Bayes' ratios. Record 00 has smaller likelihood under the larger bias, whereas 10 has equal likelihood under both biases, giving respectively

\[
\frac{(1/4)^2}{(1/4)^2+(3/4)^2}=\frac1{10},\qquad
\frac{(3/4)(1/4)}{(3/4)(1/4)+(1/4)(3/4)}=\frac12.
\]

Both records end at 0, yet they predict different next steps. Conditional independence given the parameter has not failed. The proposed state omitted what the observations taught us about that parameter.

The failure occurred when we compressed the record, not because the coin suddenly acquired physical memory. Its hidden bias stayed fixed; the observer's inference from previous outcomes changed. The identical screen value merged two different information states. The precise question worth investigating is therefore which information about the past must enter the present for correct prediction, rather than whether an experiment vaguely has memory.

A sufficient present should mean that, even after the entire history is given, the conditional average of every bounded next-step readout can still be computed from the current state. Writing that requirement gives the following definition. It does not demand complete independence between past and future; it asks that their predictive connection already be retained by the current state.

Let an adapted process \(X_n\) take values in a measurable space \((E,\mathcal E)\). Given a probability kernel \(P(x,dy)\), the homogeneous Markov property relative to \(\mathcal F_n\) means, for every bounded measurable \(f\),

\[
E[f(X_{n+1})\mid\mathcal F_n]=Pf(X_n),\qquad Pf(x)=\int f(y)P(x,dy).
\]

Homogeneity means the same kernel applies at every time; a time-inhomogeneous system may use \(P_n\). A kernel has two separate requirements: each \(x\) specifies a probability measure, and each event's probability varies measurably with \(x\). Both are needed for the right side to be a legitimate random prediction.

The property refers to a specified filtration. Enlarging it to reveal future outcomes can destroy the Markov property. Validity for the natural filtration does not imply validity for every larger filtration.

## 17.2 Compressing the past into a sufficient present

Nor must the whole bit record always be retained. Put \(q_n=P(\Theta=3/4\mid B_1,\ldots,B_n)\). Its next success probability is \(w(q_n)\), where \(w(q)=1/4+q/2\). Bayes' formula gives the two posterior updates after success and failure:

\[
q\longmapsto T_1(q)=\frac{3q}{1+2q},\qquad
q\longmapsto T_0(q)=\frac{q}{3-2q}.
\]

The posterior state therefore has the Borel probability kernel on \([0,1]\)

\[
K(q,da)=w(q)\delta_{T_1(q)}(da)+(1-w(q))\delta_{T_0(q)}(da).
\]

The past has not been denied; it has been compressed into a quantity sufficient for next-step prediction and posterior updating. A mixture of independent experiments need not remain independent, and a projection of an observation process need not preserve the Markov property.

Can the posterior be compressed further while retaining the original prediction for the next toss? In this particular model, \(w(q)=1/4+q/2\) is strictly increasing. If a single prediction function of the compressed state must recover the original next success probability, it cannot merge two distinct reachable posterior values. The posterior is not an arbitrary extra label: the distinctions it retains already change an observable experimental probability. This does not deny that discarding predictive information may yield a coarser Markov chain, nor assert an equally simple minimal state for every model or uniqueness of a successful representation.

Take independent fair bits \(U,V\) and set \(X_0=U,X_1=V,X_2=U\). Each has the same fair marginal, and adjacent pairs are independent. Yet \(X_0,X_1\) determine \(X_2\), whereas given only \(X_1\) its two possibilities still have equal probability.

Thus identical distributions at each time are far from saying the past supplies no further prediction. Even adjacent joint laws may be insufficient. Enlarging the state can preserve discarded memory: recording the relevant history as part of the state often produces a larger Markov system. This is a modeling choice, not a theorem that arbitrary projections preserve the Markov property.

Chapter 15's conditional independence gives precise language. Since \(\sigma(X_n)\subseteq\mathcal F_n\), the defining equality says that \(\sigma(X_{n+1})\) and \(\mathcal F_n\) are conditionally independent given \(\sigma(X_n)\). Conversely, that conditional independence recovers the Markov equality provided the specified kernel really is a conditional law of the next state given \(X_n\). On general measurable spaces, existence of conditional expectations does not itself supply such a kernel; here the kernel is data or is explicitly constructed.

Expanding the conditional-independence equivalence reveals exactly what “no additional predictive information” means. Write \(\mathcal G=\sigma(X_n)\), and let \(Y\) be bounded and \(\mathcal F_n\)-measurable. The Markov equality and tower property give

\[
E[Yf(X_{n+1})\mid\mathcal G]
=Pf(X_n)E[Y\mid\mathcal G],\qquad
E[f(X_{n+1})\mid\mathcal G]=Pf(X_n).
\]

This is the required conditional product factorization. Conversely, suppose that factorization holds and that \(P\) represents the conditional next-state law given the present. Taking expectations gives

\[
E[Yf(X_{n+1})]=E[YPf(X_n)].
\]

For every such \(Y\), this is precisely the defining test for conditional expectation given all of \(\mathcal F_n\). Conditional independence does not say past and future are unrelated. They may remain related through the present; only after that state is known does the past cease to improve prediction.

Markov property is thus a statement about a model, a state and available information. It says neither that reality has no past nor that recording less necessarily gets closer to its essence. Choosing a state means discovering which distinctions affect later experiments. Discarding irrelevant detail and discarding information that still predicts the future are opposite operations.

## 17.3 Multiplying transition rules across several steps

Define \(P^0(x,A)=\mathbf1_A(x)\), and put

\[
P^{n+1}(x,A)=\int P^n(y,A)P(x,dy).
\]

Measurability of kernel integrals was proved in Chapter 10. The tower property and induction yield \(E[f(X_{n+r})\mid\mathcal F_n]=P^rf(X_n)\). Associativity of iterated integration then gives the Chapman–Kolmogorov equation

\[
P^{r+s}(x,A)=\int P^s(y,A)P^r(x,dy).
\]

Prove associativity for nonnegative functions with Tonelli, then split bounded signed functions into positive and negative parts. This supplies the justification for extending matrix multiplication to general spaces.

The two-step calculation displays the logic rather than merely introducing powers of a kernel. For bounded measurable \(f\),

\[
E[f(X_{n+2})\mid\mathcal F_n]
=E[Pf(X_{n+1})\mid\mathcal F_n]
=P(Pf)(X_n).
\]

The second use of the Markov property is legitimate because kernel integration keeps \(Pf\) bounded and measurable. Repeated use of a one-step rule depends on this closure, not just on intuition about independence. Chapman–Kolmogorov says that splitting the same future into different time blocks cannot change its probability.

Successive conditional averaging also treats finite future blocks. For bounded measurable \(H\) of the next \(r\) states, let \(Q_rH(x)\) be its \(r\)-fold kernel integral starting from \(x\). Then

\[
E[H(X_{n+1},\ldots,X_{n+r})\mid\mathcal F_n]=Q_rH(X_n).
\]

For two bounded measurable functions \(g_1,g_2\), eliminate the most distant time first:

\[
E[g_1(X_{n+1})g_2(X_{n+2})\mid\mathcal F_n]
=P(g_1\,Pg_2)(X_n).
\]

Products supply all rectangular events, which generate the future block's product sigma-field. Closure under bounded monotone limits therefore reaches every bounded measurable readout. This step upgrades coordinate statements to statements about a whole finite block without pretending every measurable function is a finite sum of products.

First verify products of indicators, then finite linear combinations, then a functional monotone class. The present therefore summarizes every finite future experiment, rather than only its next step.

## 17.4 Transition rules need an actual common space

Given initial probability \(\nu\) and kernel \(P\), finite paths should have law

\[
\nu(dx_0)P(x_0,dx_1)\cdots P(x_{n-1},dx_n).
\]

These are still only finite experiments. Chapter 10 constructed sequential experiments on standard Borel spaces through randomization; arbitrary measurable spaces cannot silently inherit that encoding. General finite kernel products are available from [10.9](10-densities-and-kernels.md#section-10-9), but they do not yet give a countably infinite construction. Here the input must be a probability kernel at every prefix, not merely a collection of almost-everywhere conditional-expectation versions.

[T-SEQUENTIAL](../foundations/t-sequential.md#t-sequential-extension) proves the countable construction on general measurable spaces. It defines finite integrals on the cylinder algebra and proves continuity at an empty decreasing intersection. The mechanism is concrete: if the probabilities of decreasing cylinders stay positive, conditional future success probabilities allow coordinates to be chosen successively, producing a record in every cylinder, contradicting the empty intersection. The choices need not be measurable functions of their prefixes, so no unjustified measurable-selection theorem is needed.

This is a different direction from extracting conditional laws from an existing process. Here kernels are already specified at every state; finite integration and continuity at empty intersections realize them as a process. Starting instead with a process on a general space, conditional expectations give eventwise versions, which need not assemble into pointwise countably additive kernels. Standard Borel structure addresses an important existence difficulty in that latter direction; sequential construction does not require it as an extra assumption in the former.

The quantifiers matter too. Each fixed bounded measurable test function has its own almost sure identity. Without a countable determining class on a general space, we do not assert a common null set for all tests. The kernel defined by finite integration, in contrast, is a probability measure at every input point.

After extension, the kernel-integral identities on all prefix events verify Markov conditional averaging itself. Both existence and the property have been established, using only countable sequential experiments rather than future continuous-process theory or an uncountable extension.

## 17.5 Does the future recognize the present after a random stop?

Let \(T\) be an almost surely finite stopping time. Split \(A\in\mathcal F_T\) according to \(T=n\); each slice belongs to \(\mathcal F_n\). The fixed-time future formula gives

\[
E[\mathbf1_{A\cap\{T=n\}}H(X_{T+1},\ldots,X_{T+r})]
=E[\mathbf1_{A\cap\{T=n\}}Q_rH(X_T)].
\]

Boundedness permits summation over every \(n\), yielding

\[
E[H(X_{T+1},\ldots,X_{T+r})\mid\mathcal F_T]=Q_rH(X_T).
\]

This is the discrete strong Markov property. If \(T\) can be infinite, understand it only on \(T<\infty\): sum on \(A\cap\{T<\infty\}\), without inventing steps after \(X_\infty\). For the entire countable future, extend from cylinders by a monotone class.

The stopped position itself must be measurable. For \(B\in\mathcal E\), on \(\{T<\infty\}\),

\[
\{X_T\in B,T<\infty\}
=\bigcup_{n\ge0}\{T=n,X_n\in B\}.
\]

Intersecting the union with \(\{T\le m\}\) leaves only finitely many \(\mathcal F_m\) events with \(n\le m\), proving stopped-sigma-field measurability. In summing the identities, the total absolute-integral budget on either side is at most \(\|H\|_\infty P(A\cap\{T<\infty\})\). Slicing is a legitimate countable integral decomposition, not a formal substitution.

Even the entire infinite future has a precise kernel. For every \(x\), T-SEQUENTIAL gives a future-sequence law \(R_x\) starting at \(x\). Path events \(C\) for which \(x\mapsto R_x(C)\) is measurable form a lambda-system containing all finite cylinders. The pi–lambda theorem extends measurability to the full path product sigma-field. Applying a monotone class to the conditional-average identity then permits any bounded measurable future-path readout at the stopping time. This remains countable-coordinate information, without silently adding a larger collection of path events.

This proof does not infer independence from optional sampling. It uses slices of the stopped sigma-field and the original Markov kernel. Continuous time has no such countable partition covering every real stopping value; general strong Markov properties there need additional regular structure.

## 17.6 A possible route is not an inevitable arrival

<a id="mc-communication"></a>

Knowing the next-step rule does not yet tell us where a long journey will lead. We now restrict to a finite or countable state space with its discrete sigma-algebra, writing the transition matrix as \(p_{ij}\). A kernel can then be drawn as a directed graph, retaining precisely the transitions with positive probability.

The probability of a finite path is the product of its edge probabilities. Thus a positive-probability route from \(i\) to \(j\) exists exactly when \(p^{(n)}_{ij}>0\) for some \(n\ge0\). Write \(i\to j\), allowing a zero-step path. Chapman–Kolmogorov makes accessibility transitive by concatenation. If both \(i\to j\) and \(j\to i\), write \(i\leftrightarrow j\). Reflexivity, symmetry and transitivity partition the states into communication classes. A chain with just one class is irreducible.

These definitions first distinguish an irreversible departure. A communication class is closed if it has no positive-probability transition out of the class: once entered, it cannot be left. Collapse each class to a vertex. The resulting graph has no directed cycle, since classes on a cycle would communicate and should have been merged. Following outward edges in a finite graph must end. Every finite chain therefore has a closed class, and every state has a route to one.

A route is not yet almost-sure entry. Finiteness supplies the missing step. Let \(B\) be the union of all closed classes and \(H=\inf\{n\ge0:X_n\in B\}\). If there are states outside, choose from each one a positive-probability path into \(B\). There are finitely many such states, so all selected path lengths are bounded by some \(L\ge1\), and all their probabilities are at least some \(\eta>0\). Arrival need not occur exactly at step \(L\); following a chosen path and entering earlier already counts.

\[
P_\mu(H>(r+1)L)\le(1-\eta)P_\mu(H>rL)
\le(1-\eta)^{r+1}.
\]

For the first inequality, condition on \(\mathcal F_{rL}\) on \(\{H>rL\}\) and use the selected path from the current state; induction gives the second. Hence \(H<\infty\) almost surely, and summing the tail gives \(E_\mu H\le L/\eta\). If every state already lies in \(B\), then \(H=0\) and no estimate is needed. Accessibility in a graph was not silently replaced by probability one: finitely many starting points supplied a uniform chance.

On an infinite space that uniform chance may disappear. Even mutual accessibility is not recurrence: a route back can exist while the chain avoids returning forever with positive probability. The return questions ahead cannot be settled merely by drawing arrows.

## 17.7 If a law settles, what can it settle to?

<a id="mc-invariant"></a>

Do not assume that settling occurs. If the laws \(\mu P^n\) of a finite chain do converge to a probability vector \(\pi\), the next step still uses the same matrix. Passing a finite sum through the limit forces \(\pi P=\pi\). We therefore first seek a distribution preserved by one step, called an invariant distribution. This is an equation any possible limit must satisfy, not a proof that a limit exists.

Starting from an invariant distribution gives the same law to every time-shifted finite path. Indeed, the probability of \(i_0,\ldots,i_r\) is \(\pi_{i_0}\prod_{k<r}p_{i_ki_{k+1}}\). Sum out the extra earliest state before a shift and use \(\sum_j\pi_jp_{ji_0}=\pi_{i_0}\) to recover the same product. The process is stationary, although individual paths can keep moving indefinitely.

A finite chain always has an invariant distribution, even if its successive laws do not converge. Start with any law \(\nu\) and average the first \(N\) time marginals:

\[
\mu_N=\frac1N\sum_{k=0}^{N-1}\nu P^k,\qquad
\mu_NP-\mu_N=\frac{\nu P^N-\nu}{N}.
\]

Every coordinate on the right tends to zero. The vectors \(\mu_N\) lie in a finite-dimensional probability simplex: successive coordinatewise extraction gives a convergent subsequence whose nonnegative coordinates still sum to one. Passing through finite matrix multiplication produces an invariant probability. Averaging removed the endpoint difference, but it did not identify convergence of averaged laws with convergence of each time marginal. Nor have we proved a sample-path empirical-frequency theorem.

Irreducibility makes every coordinate positive: if \(\pi_i>0\) and \(p^{(n)}_{ij}>0\), then \(\pi_j=(\pi P^n)_j\ge\pi_ip^{(n)}_{ij}>0\). Any other invariant probability \(\rho\) is positive everywhere too. To prove equality, compare the ratios \(r_i=\pi_i/\rho_i\). Invariance gives

\[
r_i=\sum_j\frac{\rho_jp_{ji}}{\rho_i}\,r_j,\qquad
\sum_j\frac{\rho_jp_{ji}}{\rho_i}=1.
\]

Each ratio is a weighted average of other ratios. Finiteness ensures that a maximum is attained; equality of an average with that maximum forces every positively weighted term to attain it too. The positive weight edges reverse the original graph, whose reversal is still irreducible. The maximum propagates along reversed paths to every state. The ratio is constant, and total mass one makes the constant one. This proves uniqueness for a finite irreducible chain. The reversed weights will later acquire an interpretation through reversed time.

The proof cannot be transferred unchanged to an infinite space. For deterministic right shift \(i\mapsto i+1\) on the nonnegative integers, the averaged law from zero is uniform on the first \(N\) points. Each coordinate tends to zero, but the coordinate limit is no longer a probability. The invariant equations likewise force zero mass at zero and then at every successive point. For symmetric walk on the integer line, an invariant vector satisfies \(2\pi_j=\pi_{j-1}+\pi_{j+1}\); adjacent differences are constant, nonnegativity on all integers forces a constant sequence, and a nonzero constant is not summable. These exhibit mass leaving finite windows and an invariant measure that cannot be normalized.

## 17.8 Invariant weights may still carry a periodic clock

<a id="mc-period"></a>

A chain that switches between two states at every step is irreducible and has the unique invariant distribution \((1/2,1/2)\). Yet from a fixed state its laws alternate forever between two point masses. The obstruction concerns permitted return times, not communication in space.

For a state \(i\) with a possible positive-time return, define the greatest common divisor of all its possible return lengths:

\[
d(i)=\gcd\{n\ge1:p^{(n)}_{ii}>0\}.
\]

This is its period; \(d(i)=1\) means aperiodic. The greatest common divisor retains the temporal lattice that concatenation cannot break, rather than merely the shortest possible return. If positive paths \(i\to j\) and \(j\to i\) have lengths \(a,b\), any return length \(n\) at \(j\) makes both \(a+n+b\) and \(a+b\) return lengths at \(i\). Hence \(d(i)\) divides \(n\). Interchanging states proves equality of periods throughout a communication class. The same-state comparison is immediate; for distinct states the lengths \(a,b\) can be positive.

Every state of a finite irreducible chain has a positive-time return. Fix a base \(o\), and let \(r(j)\) be the length modulo the common period \(d\) of any positive-probability path from \(o\) to \(j\), allowing the zero-step path at the base. The residue is well defined: append the same path \(j\to o\) to two choices, and their return-length difference is divisible by \(d\). Thus

\[
C_\ell=\{j:r(j)=\ell\},\qquad
p_{ij}>0\ \Longrightarrow\ r(j)=r(i)+1\pmod d.
\]

Every residue class is nonempty: traverse the first \(d\) times of a positive-probability return circuit at \(o\). Each step goes only from \(C_\ell\) to \(C_{\ell+1}\). Invariance gives these sets equal \(\pi\)-mass, hence mass \(1/d\) each. From a fixed state, however, all mass at time \(n\) lies in a single current phase. For \(d>1\), this event has probability one now and stationary probability \(1/d\), a discrepancy at least \(1-1/d\) that cannot disappear.

Waiting in place is one way to break periodicity: a positive self-loop anywhere in an irreducible class forces common period one. It is not necessary. The following three-state chain has no self-loops, but zero can return in both two and three steps:

\[
P=\begin{pmatrix}
0&1&0\\[2pt]
\tfrac12&0&\tfrac12\\[2pt]
1&0&0
\end{pmatrix},\qquad \pi=(\tfrac25,\tfrac25,\tfrac15).
\]

The graph is irreducible, and two and three have greatest common divisor one. The displayed invariant law follows directly from the incoming-flow equations and normalization. What matters is not whether every step allows a pause, but whether concatenable circuits remain constrained by a coarser common clock.

## 17.9 From no common period to routes at every sufficiently late time

<a id="mc-positive-power"></a>

Aperiodicity removes an obstruction, but we need a positive conclusion. Knowing one route between each pair of states does not make those routes equally long. To compare distributions at a common observation time, we must be able to extend different routes to a common duration.

First study returns to one state \(o\). Return lengths are closed under addition because circuits concatenate. If their greatest common divisor is one, finitely many of them, \(a_1,\ldots,a_q\), already have greatest common divisor one: as lengths are added, the gcd descends through positive integers and eventually reaches the gcd of the full set. We now prove that their nonnegative integer combinations contain every sufficiently large integer.

Work modulo \(a_1\). The residues of nonnegative combinations contain zero and are closed under addition. In a finite group such a set contains inverses too, since a positive multiple of each element is zero. It is a subgroup. Gcd one makes it the whole residue group: the least positive integer linear combination divides every \(a_j\), hence is one, so the subgroup contains one. For each residue \(\ell\), choose an actual nonnegative combination \(b_\ell\) representing it. If \(M=\max_\ell b_\ell\), any \(n\ge M\), with \(b_\ell\) congruent to \(n\), has

\[
n=b_\ell+k a_1,\qquad k\in\{0,1,2,\ldots\}.
\]

Concatenating the corresponding circuits gives positive path probability, so \(p^{(n)}_{oo}>0\) for every sufficiently large positive integer \(n\). The gcd definition has become a usable probability statement about actual paths, without concealing the arithmetic in an unnamed standard lemma.

For every pair \(i,j\), choose positive-probability paths \(i\to o\) and \(o\to j\), of lengths \(u_i,v_j\), allowing zero steps where appropriate. Finitely many states allow a single \(N\ge1\) such that \(n-u_i-v_j\) is an allowed return length whenever \(n\ge N\), for every pair \(i,j\). Chapman–Kolmogorov yields

\[
p^{(n)}_{ij}\ge
p^{(u_i)}_{io}\,p^{(n-u_i-v_j)}_{oo}\,p^{(v_j)}_{oj}>0
\qquad(n\ge N).
\]

Thus some power \(P^N\) of a finite irreducible aperiodic chain has all entries strictly positive. Conversely, if \(P^N\) is strictly positive, all states communicate, and \(P^{N+1}=PP^N\) is strictly positive because each row sums to one. Consecutive return lengths \(N,N+1\) force period one. These conditions are equivalent in the finite setting; on an infinite space positive routes for individual pairs do not supply a uniform positive lower bound.

## 17.10 How shared probability mass removes the starting point

<a id="mc-finite-convergence"></a>

We can now reach every state at a common time, but that alone is not yet convergence of laws. The key is that finitely many positive numbers have a common positive lower bound. Distributions arriving from different starting points then contain an identical probability component. Their remaining difference contracts after each block of the same duration.

We use the total-variation convention from Chapter 13. On a finite set \(E\),

\[
\|\mu-\nu\|_{\mathrm{TV}}
=\sup_{A\subseteq E}|\mu(A)-\nu(A)|
=\frac12\sum_{j\in E}|\mu_j-\nu_j|.
\]

The coordinates satisfying \(\mu_j-\nu_j>0\) attain the supremum; equality of total positive and negative mass explains the factor \(1/2\). This measures the largest probability discrepancy over events, rather than a chosen coordinate. For any transition matrix \(R\), the triangle inequality and row sums one give

\[
\begin{aligned}
2\|\mu R-\nu R\|_{\mathrm{TV}}
&=\sum_j\left|\sum_i(\mu_i-\nu_i)R_{ij}\right|\\
&\le\sum_i|\mu_i-\nu_i|\sum_jR_{ij}
=2\|\mu-\nu\|_{\mathrm{TV}}.
\end{aligned}
\]

Evolution cannot enlarge this discrepancy, but two-state alternation can preserve it completely. Let \(s=|E|\), take \(K=P^N\) from the preceding section, and set

\[
\delta=\min_{i,j}K_{ij}>0,\qquad
\varepsilon=s\delta\in(0,1],\qquad u_j=\frac1s.
\]

If \(\varepsilon<1\), subtract the uniform mass common to every row and normalize what remains:

\[
R_{ij}=\frac{K_{ij}-\varepsilon u_j}{1-\varepsilon},
\qquad K_{ij}=\varepsilon u_j+(1-\varepsilon)R_{ij}.
\]

The numerators are nonnegative and each row sums to \(1-\varepsilon\), so \(R\) really is a transition matrix. Multiplying any two initial laws by \(K\) makes their common \(\varepsilon u\) cancel. Nonexpansion becomes strict contraction:

\[
\|\mu K-\nu K\|_{\mathrm{TV}}
\le(1-\varepsilon)\|\mu-\nu\|_{\mathrm{TV}}.
\]

**Finite-chain convergence theorem.** If \(P\) is a finite-state irreducible aperiodic transition matrix, it has a unique invariant probability \(\pi\), and \(\mu P^n\to\pi\) in total variation for every initial law \(\mu\). More precisely, for \(0<\varepsilon<1\), the \(N,\varepsilon\) above satisfy

\[
\|\mu P^n-\pi\|_{\mathrm{TV}}
\le(1-\varepsilon)^{\lfloor n/N\rfloor}\|\mu-\pi\|_{\mathrm{TV}}.
\]

Existence, positivity and uniqueness were proved in 17.7; section 17.9 supplies \(N\); this section supplies contraction per block. Write \(n=kN+r\), \(0\le r<N\). Apply the contraction \(k\) times to \(K\), then nonexpansion for the remaining \(P^r\), to obtain the bound. If \(\varepsilon=1\), every row of \(K\) equals \(u\), erasing the initial difference after one block. Invariance \(\pi K=\pi\) forces \(\pi=u\), so equality with \(\pi\) holds for all \(n\ge N\). This case does not require inserting \(0^0\) into a formula.

All bounded observables are controlled too: \(|\mu P^ng-\pi g|\le2\|g\|_\infty\|\mu P^n-\pi\|_{\mathrm{TV}}\). To observe the next fixed \(r\) steps, push the current law through the future kernel of 17.3; the same finite-sum estimate cannot increase total variation. Initial-state effects disappear not only in single coordinates but in every fixed-length future experiment.

Each assumption has a role: finiteness supplies a common time and positive lower bound; irreducibility prevents separate closed components from retaining separate futures; aperiodicity removes clocks that cannot align. The bound is not claimed optimal, nor is it general Harris or mixing theory. Finding appropriate small sets, returns and contraction conditions on general spaces remains the responsibility of Chapter 42. The finite-chain version needed here has been proved in full.

This convergence changes how distinguishable the initial laws remain; it does not guarantee that a single path settles down. A particularly clear example forgets its initial law completely after just one step:

\[
P=\begin{pmatrix}\tfrac12&\tfrac12\\[2pt]\tfrac12&\tfrac12\end{pmatrix},
\qquad \mu P=(\tfrac12,\tfrac12)\quad\text{for every }\mu.
\]

From step one onward, the finite-path product formula gives independent fair bits. For \(k\ge1\), the events \(X_{2k}\ne X_{2k+1}\) use disjoint pairs and are independent, each with probability \(1/2\). Borel–Cantelli makes them occur infinitely often almost surely. A path is therefore not eventually constant and cannot converge as a real sequence. The tail process from step one is exactly stationary while almost every path keeps changing; for a nonuniform initial law this does not assert stationarity of the entire process from time zero. The total-variation theorem concerns later observational probabilities ceasing to distinguish initial laws; it cannot be read as individual motion coming to rest.

The proof also identifies a next question more precise than generalization to infinite space. Contraction was driven by common positive mass. If that component exists only within one region, evolution outside it and the time needed to return become unavoidable issues. Transferring the present mechanism requires connecting return estimates to local common mass. Later Harris theory will systematically connect these two ingredients; the present proof has identified the concrete components needed for that extension.

## 17.11 What still converges when a periodic clock remains?

<a id="mc-periodic-limits"></a>

Two-state alternation is not absence of order; it is excessive stability demanded on the wrong clock. Even with periodicity, the averaged laws of a finite irreducible chain converge to its unique \(\pi\): every subsequential limit from 17.7 is invariant and hence identical. If the full sequence failed to converge, a subsequence bounded away from \(\pi\) would have a further convergent subsequence in the finite simplex, a contradiction. Thus for every initial \(\mu\),

\[
\frac1N\sum_{n=0}^{N-1}\mu P^n\longrightarrow\pi
\quad\text{in total variation}.
\]

Without averaging, individual phases have limits too. At common period \(d\), observing every \(d\) steps makes \(P^d\) stay within each \(C_\ell\). Its restriction is irreducible, since a positive path between states in the same phase has length divisible by \(d\). It is aperiodic because dividing all original return lengths by \(d\) leaves gcd one. Its invariant law is the normalized restriction of \(\pi\), namely \(d\pi_j\) on that class.

The normalized restriction is invariant because \(\pi P^d=\pi\) and \(P^d\) has no transitions between these classes, so its invariant equations restrict to each class. We may now apply the finite-chain theorem just proved, rather than assume a separate periodic convergence result. Starting at \(i\in C_a\), for \(0\le r<d\),

\[
p^{(kd+r)}_{ij}\longrightarrow
\begin{cases}
d\pi_j,&j\in C_{a+r\ {\rm mod}\ d},\\
0,&j\notin C_{a+r\ {\rm mod}\ d}.
\end{cases}
\]

To verify the formula, first take \(r\) steps, placing all mass in \(C_{a+r}\). After a further \(kd\) steps, the law from each intermediate state tends to \(d\pi\) on that class. A finite sum permits the limit. Two-state alternation is the case of one state per phase. Averaged convergence, phasewise convergence and convergence at every time now have distinct conclusions, rather than sharing an ambiguous label of equilibrium.

## 17.12 When there are several worlds that cannot be left

<a id="mc-closed-limits"></a>

Irreducibility is not merely a label next to a theorem. Two disjoint absorbing states already give every mixture as an invariant law; no mechanism can erase which closed world the chain eventually enters. Long-term laws of a finite reducible chain must record that choice before studying stability inside each class.

Let the closed communication classes be \(D_1,\ldots,D_b\), with their unique invariant probabilities \(\pi^{(a)}\), extended by zero outside the class. Section 17.6 proved entry into their union at a finite time \(H\). The mass outside is at most \(P_\mu(H>n)\), tending to zero. For an invariant law \(\rho\), starting from \(\rho\) keeps that outside mass constant and must therefore vanish. Restricting the invariant equations to each class and using uniqueness shows that all invariant probabilities are exactly

\[
\rho=\sum_{a=1}^b c_a\pi^{(a)},\qquad
c_a\ge0,\quad\sum_a c_a=1.
\]

If every closed class is also aperiodic, the time marginals do converge, but their mixture weights depend on the initial experiment. With \(\alpha_a=P_\mu(X_H\in D_a)\),

\[
\mu P^n\longrightarrow\sum_{a=1}^b\alpha_a\pi^{(a)}
\quad\text{in total variation}.
\]

One cannot simply substitute a random entry time into a deterministic-time limit. Fix \(M\) and first restrict to \(H\le M\). Partition by \(H=h\) and \(X_H=i\). Strong Markov from 17.5 gives the subsequent law \(P^{n-h}(i,\cdot)\). Finitely many \(h\le M,i\) allow simultaneous use of within-class convergence. The actual remainder on \(H>M\) and the corresponding target mixture have the same total mass, so their total variation is at most \(P_\mu(H>M)\). Let \(n\to\infty\) first and then \(M\to\infty\) to prove the limit.

Periodic closed classes can prevent convergence at every time; retain the preceding phases or average the laws over time. The averaged version needs no aperiodicity, but still distinguishes times before and after entry. On \(H=h\le M\), \(X_H=i\in D_a\), apply strong Markov only to the terms after entry:

\[
\frac1N\sum_{n=h}^{N-1}P^{n-h}(i,\cdot)
=\frac{N-h}{N}
\left(\frac1{N-h}\sum_{k=0}^{N-h-1}P^k(i,\cdot)\right)
\longrightarrow\pi^{(a)}\qquad(N>M).
\]

There are at most \(M\) terms with \(n<h\), contributing total averaged mass at most \(M/N\). Use the within-class averaged limit of 17.11 for finitely many \(h,i\); the remaining records with \(H>M\) contribute at most \(P(H>M)\) discrepancy. Let \(N\to\infty\) and then \(M\to\infty\) to obtain the same mixture \(\sum_a\alpha_a\pi^{(a)}\). No negative-time matrix power is used, and a random shift is not silently treated as deterministic. This remains a long-term statement about laws, not a sample-path ergodic theorem.

## 17.13 After stationarity, does reversed time give the same experiment?

<a id="mc-reversal"></a>

An unchanging long-term distribution does not remove the direction of time. Reversed weights appeared in the uniqueness proof of 17.7; now read them from a stationary record. At a state with \(\pi_i>0\), the conditional probability that the preceding state was \(j\), given the current state \(i\), is

\[
\widehat p_{ij}=\frac{\pi_jp_{ji}}{\pi_i}.
\]

Invariance makes each row sum to one and gives \(\pi\widehat P=\pi\). These identities hold on countable chains as well, by summing nonnegative terms. If \(\pi_j=0\), the nonnegative terms in its invariant equation show that the positive-mass support cannot transition to \(j\). Use the formula on that support; arbitrary reversed rows at zero-mass states do not change the stationary path law.

The description extends beyond two adjacent times. For a finite path in the support, the reversed transition product telescopes:

\[
\begin{aligned}
\pi_{i_n}\prod_{k=0}^{n-1}\widehat p_{i_{k+1}i_k}
&=\pi_{i_n}\prod_{k=0}^{n-1}
\frac{\pi_{i_k}p_{i_ki_{k+1}}}{\pi_{i_{k+1}}}\\
&=\pi_{i_0}\prod_{k=0}^{n-1}p_{i_ki_{k+1}}.
\end{aligned}
\]

Thus the reversed record is Markov, but usually with the different kernel \(\widehat P\). If forward and backward records are to have the same stationary law, paths of length one force detailed balance for every pair of states:

\[
\pi_ip_{ij}=\pi_jp_{ji}.
\]

Conversely, summing detailed balance gives invariance, and multiplying along finite paths gives equal probabilities to forward and backward records. It is therefore equivalent to reversibility here. It is stronger than invariance: invariance balances total incoming and outgoing flow at each state, while detailed balance balances each pair separately.

Deterministic rotation around a directed three-cycle has invariant uniform law but no reverse edges, so it is not reversible. If each step instead waits with probability one half and moves forward with probability one half, the chain remains nonreversible but becomes finite, irreducible and aperiodic. It converges to the uniform law from every start. Conversely, deterministic two-state alternation satisfies detailed balance but fails to converge at every time because its period is two. Reversibility cannot replace aperiodicity, and convergence does not require reversibility: these notions answer different experimental questions.

## Chapter 17 Epilogue: The next-step rule and the long future

The posterior state stores the information left by successive observations; given it, the old record adds nothing to predicting the future. Markov property is therefore not a slogan about forgetting, but a test of whether the present state retains enough information. Sequential construction and stopping-time partitions give that claim an actual infinite record and preserve it after a legitimate stop.

If finding a unique invariant law had been treated as the endpoint, two-state alternation could easily have been dismissed as a minor exception. Taking it seriously separates two questions previously conflated: which law can remain invariant, and whether different initial laws approach it. The next distinction concerns permitted path durations rather than more coordinates. These distinctions exposed by counterexamples advance the question; a common positive power and common probability mass then become tools precisely suited to resolving it.

Finite space ultimately confines the chain to a closed component, making these uniform estimates possible. On an infinite lattice, arrows can still point back toward the start while a path keeps travelling away. After finding a route back, we must compute whether it will actually be taken and how many returns occur. That difference leads random walk toward visit counts and spatial dimension.

## Sources and proof scope

The unknown-bias coin, bit counterexample, cycles and finite-matrix arguments are modern mathematical reconstructions, not invented episodes from Markov's own discovery. General measurable-space existence is actually supported by [T-SEQUENTIAL](../foundations/t-sequential.md#t-sequential-extension); an original reference is Ionescu–Tulcea's 1949 [Mesures dans les espaces produits](https://cs.uwaterloo.ca/~y328yu/classics/IonescuTulcea49.pdf). Pointwise sequential-kernel data remain distinct from arbitrary finite-dimensional extension on general spaces.

The periodic arithmetic and convergence scope were checked against Cambridge's public [Markov Chains notes, sections 9.2–9.3](https://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf). Here nonnegative integer combinations are proved explicitly and contraction follows from common mass in finite matrices, without a general coupling or Harris theorem. Chapter 18 develops returns and Green kernels; Chapter 42 retains general-state Harris and mixing theory. The finite results here are not counted as proofs of those general theorems.
