# The Mathematics of Chance
Volume II · Probability in an Infinite World

# Chapter 10: How Can One Probability Be Decomposed in Terms of Another?—Densities, Conditional Laws and Probability Kernels

The coins on the table are still in view.

[The preceding chapter](#chapter-9) enabled us to revalue a game using the outcomes already observed. Its price used only the available information and preserved the integral of the true return on every observable event. We also proved that such an average exists without borrowing a general density theorem first.

But knowing the average price is not knowing the game.

One game always pays 32 coins; another pays 0 or 64 with equal chances. Both average 32, yet their risks differ. If observations have changed our knowledge of the outcome, we want more than a mean: we want the chances of every possible future result.

The question therefore moves forward:

**Can all the probabilities after conditioning be organized into a genuine probability distribution?**

This asks more than taking a conditional expectation separately for each event. Chapter 8 showed that reasonable finite experiments need not fit inside an arbitrarily chosen infinite world. The same difficulty now reappears within information: separate answers to every question need not already form a common world.

We begin with the density that appeared at the end of the previous chapter, then follow this difficulty toward conditional laws, disintegration and probabilities that vary with observations.

## 10.1 If every individual answer is right, why is there still no probability?

Let us first make the version problem concrete.

Take Borel events and uniform probability \(P\) on \([0,1]\). Allow the observer to distinguish only Borel events of probability zero or one:

\[
\mathcal G=\{A\in\mathcal B([0,1]):P(A)\in\{0,1\}\}.
\]

This is indeed a sub-\(\sigma\)-algebra: a countable union of null events is null, while a union containing an event of probability one has probability one. For any Borel set \(A\), the constant \(P(A)\) is a version of \(P(A\mid\mathcal G)\).

Now deliberately choose differently. For a singleton \(A=\{a\}\), set

\[
H(\omega,\{a\})=\mathbf1_{\{a\}}(\omega);
\]

For a Borel set that is not a singleton, set \(H(\omega,A)=P(A)\).

For each fixed \(A\), this is still a correct conditional-probability version. A singleton indicator is \(\mathcal G\)-measurable and differs from the constant zero at only one null point. Other sets have not been changed at all.

Yet fixing any \(\omega\) gives

\[
H(\omega,\{\omega\})=1,\qquad
H(\omega,[0,1]\setminus\{\omega\})=1,
\qquad H(\omega,[0,1])=1.
\]

The probabilities of two disjoint sets add up to 2, while their union has probability 1. Even finite additivity fails.

No answer to a fixed question was wrong. The mistake was to treat separately chosen versions as a coordinated whole. Each singleton changes only a null set, but there are uncountably many singletons; discarding all their exceptions discards the entire interval.

This does not mean that our example lacks a good conditional law. Taking \(K(\omega,A)=P(A)\) works perfectly. The example reveals an indispensable existence problem: **compatible choices must be proved possible; arbitrary choices must not be assumed compatible.**

Before solving that problem, let us understand where the weights in each conditional answer come from.

## 10.2 A density is a relation between measurements, not a curve

Chapter 6 often wrote a density as \(f(x)\,dx\). That notation can suggest that a density is simply a curve drawn relative to length.

The more basic question concerns two nonnegative measures \(\mu,\nu\) on the same measurable space \((S,\mathcal S)\). Can we find measurable \(f\ge0\) such that

\[
\nu(A)=\int_A f\,d\mu\qquad(A\in\mathcal S)?
\]

There is no requirement that \(S\) be the real line or that \(\mu\) measure length. The reference may be discrete weights, a continuous distribution or another probability already constructed.

If such \(f\) exists, \(\mu(A)=0\) must imply \(\nu(A)=0\). We write this condition as

\[
\nu\ll\mu,
\]

and say that \(\nu\) is **absolutely continuous** with respect to \(\mu\). This concerns their null sets, not continuity of a graph.

Two probabilities on finitely many states can have such a relative density: at a point with \(\mu(\{s\})>0\), it is the ratio \(\nu(\{s\})/\mu(\{s\})\). But if \(\mu\) gives a point no mass and \(\nu\) places an atom there, no weighting can create that atom from zero.

A necessary condition has appeared. The substantial result is that, under suitable finiteness assumptions, a condition concerning only null sets also guarantees the existence of an entire density.

Nikodym's 1930 paper, explicitly about generalizing Radon's integrals, advanced this direction for additive measurements on abstract sets. [Original publication](https://doi.org/10.4064/fm-15-1-131-179). We do not reproduce its proof. Instead, we use the conditional average established in the previous chapter to reveal relative weights inside a common experiment.

## 10.3 What happens when the label distinguishing two measurements is hidden?

First assume \(\mu(S),\nu(S)<\infty\). If both total masses vanish, the density problem is already settled. Otherwise put

\[
c=\mu(S)+\nu(S)>0,\qquad \lambda=\mu+\nu.
\]

Construct an experiment with labels: a state still comes from \(S\), but the record also carries 0 or 1. Specify

\[
P(A\times\{0\})=\frac{\mu(A)}c,
\qquad
P(A\times\{1\})=\frac{\nu(A)}c.
\]

This is a probability on \(S\times\{0,1\}\): every measurable set consists of two measurable sections, and countable additivity follows directly from \(\mu,\nu\). Let \(Z(s,i)=s\), revealing the state but hiding its label.

The conditional chance of label 1 is

\[
\mathbb E[\mathbf1_{\{i=1\}}\mid\sigma(Z)]=q(Z).
\]

The measurable factorization is from Section 9.16: a real \(\sigma(Z)\)-measurable function is a measurable function of \(Z\). This works for any measurable state space and does not assume a conditional-distribution kernel. Clipping \(q\) to \([0,1]\) preserves the version, so we may require \(0\le q(s)\le1\) everywhere.

Section 9.16 explained this for a real-valued observation; we must check that its argument did not depend on observation values being real numbers. Write \(H\) for a conditional-expectation representative already clipped to \([0,1]\), and approximate it pointwise by finite-valued simple functions \(H_n\). Since \(\sigma(Z)=\{Z^{-1}(A):A\in\mathcal S\}\), every level set of \(H_n\) is the preimage of a measurable state set. Successively remove the portions assigned to earlier state sets. This gives measurable simple functions \(q_n\) on the state space with \(H_n=q_n(Z)\). Disjointification preserves the preimages, because the original level sets are disjoint.

Take the limit on the measurable set where \(q_n(s)\) converges to a finite real number, and put 0 elsewhere, obtaining measurable \(q\). At every original sample point, \(q_n(Z)=H_n\to H\), so \(q(Z)=H\) pointwise. If the initial conditional-expectation representative satisfies the bounds only almost everywhere, clip it first on its measurable bad set. This is measurable factorization of a real-valued function, not an existence theorem for regular conditional distributions, so no standard Borel assumption on \((S,\mathcal S)\) is needed here.

Apply the defining event-integral identity to \(\{Z\in A\}\) and cancel the normalizing constant \(c\). This gives

\[
\nu(A)=\int_Aq\,d\lambda,
\qquad
\mu(A)=\int_A(1-q)\,d\lambda.
\]

Passing from indicators through simple functions and monotone convergence gives the corresponding change-of-weight identities for every nonnegative measurable \(h\):

\[
\int h\,d\nu=\int hq\,d\lambda,
\qquad
\int h\,d\mu=\int h(1-q)\,d\lambda.
\]

Now assume \(\nu\ll\mu\). On \(D=\{q=1\}\), the second identity gives \(\mu(D)=0\), and absolute continuity gives \(\nu(D)=0\). Hence \(\lambda(D)=0\).

At the other points define

\[
f=\frac{q}{1-q},
\]

and set it to zero on \(D\). Then

\[
\int_A f\,d\mu
=\int_A f(1-q)\,d\lambda
=\int_Aq\,d\lambda
=\nu(A).
\]

This proves the **Radon–Nikodym theorem for finite nonnegative measures**: if \(\nu\ll\mu\), the required density exists.

It is also unique up to \(\mu\)-almost-everywhere equality. If \(f,g\) are densities, both are \(\mu\)-integrable. Subtract their integrals over \(\{f>g\}\) to obtain a nonnegative difference with integral zero, then interchange them. The usual notation is therefore

\[
f=\frac{d\nu}{d\mu}.
\]

It resembles a derivative from calculus, but its definition is an integral identity on every measurable event. It does not require an infinitesimal probability ratio at every point.

The ratio in the proof has a transparent meaning too: \(q\) is the conditional share of the mixed record coming from \(\nu\), while \(1-q\) is the share coming from \(\mu\). Comparing the two measurements means comparing their hidden labels.

The previous chapter constructed conditional averages geometrically; we have now used them to construct general densities. There is no circularity. Had the previous chapter assumed this density theorem first, the present argument could not count as an independent proof.

## 10.4 Where did the probability that cannot be expressed by weights go?

Remove the absolute-continuity assumption temporarily. The label experiment still works, but \(D=\{q=1\}\) need not be null for \(\nu\).

Inspect this set: \(\mu(D)=0\), while \(\nu\) may retain some or all of its mass there. It is precisely a region invisible to one measurement but potentially visible to \(\nu\).

Set \(f=q/(1-q)\) on \(D^c\), zero on \(D\), and define

\[
\nu_a(A)=\int_A f\,d\mu,
\qquad \nu_s(A)=\nu(A\cap D).
\]

The change-of-weight formula gives, term by term,

\[
\nu_a(A)=\nu(A\cap D^c),
\qquad \nu=\nu_a+\nu_s.
\]

The first part is absolutely continuous with respect to \(\mu\). The second is concentrated on a \(\mu\)-null set; we write

\[
\nu_s\perp\mu,
\]

and call it **singular** with respect to \(\mu\). Singularity describes a relation between measures. It does not say that a supporting set must be sparse, have no topological interior or be countable.

This **Lebesgue decomposition** is unique. Given two decompositions whose singular parts are supported on \(\mu\)-null sets \(D_1,D_2\), both absolutely continuous parts agree with \(\nu\) outside \(D_1\cup D_2\) and vanish inside it. They therefore agree on every event, as do the remaining singular parts.

With length \(\ell\) on \([0,1]\) as reference,

\[
\nu=\frac12\ell+\frac12\delta_0
\]

has half its mass in a density and half in a singular point mass. A singular part need not have atoms: a continuous probability supported on a zero-length Cantor set is another example. Having no singleton masses does not imply having a length density.

The density and singular parts are not competing descriptions. They are two components of the same measurement relative to a specified reference. Changing the reference can change the decomposition.

## 10.5 Why divide an infinite-mass space into manageable pieces?

Probability has total mass one, whereas length need not be finite. We must understand how the preceding existence result extends beyond finite total mass.

Suppose both \(\mu,\nu\) are \(\sigma\)-finite: each space has a countable cover by sets of finite measure. Intersect the two covers, enumerate the intersections, then remove previously assigned pieces. This produces a countable measurable partition \(C_n\) with

\[
\mu(C_n)<\infty,\qquad \nu(C_n)<\infty.
\]

Apply the finite case on each \(C_n\), and assemble the densities into

\[
f=\sum_n f_n\mathbf1_{C_n}.
\]

For every \(A\), countable additivity of nonnegative integration gives

\[
\int_A f\,d\mu
=\sum_n\int_{A\cap C_n}f_n\,d\mu
=\sum_n\nu(A\cap C_n)=\nu(A).
\]

This proves the **\(\sigma\)-finite Radon–Nikodym theorem**. Applying the Lebesgue decomposition on each piece and taking the countable union of singular supports gives its \(\sigma\)-finite version as well. Uniqueness can likewise be checked piece by piece.

Countability again does genuine work: measurable functions can be assembled countably, and a countable union of null sets is null.

This does not mean that absolute continuity alone automatically survives the removal of finiteness assumptions. Take counting measure \(\mu\) on \([0,1]\) and length \(\nu\). The only counting-measure null set is empty, so indeed \(\nu\ll\mu\).

If a density existed, every \(x\) would satisfy

\[
0=\nu(\{x\})=\int_{\{x\}}f\,d\mu=f(x).
\]

Its integral over the entire interval would then also vanish, contradicting \(\nu([0,1])=1\). This counting measure is not \(\sigma\)-finite.

Recall also the previous chapter's infinite expectation. For \(X\ge0\), setting \(\nu(A)=\int_AX\,dP\) on \(\mathcal G\) need not give a \(\sigma\)-finite measure. If \(\mathcal G\) consists only of the empty set and the whole space, and \(\mathbb EX=\infty\), no finite-\(\nu\)-mass events cover the whole space.

Thus the \(\sigma\)-finite density theorem cannot replace every extended construction of Section 9.8.1 without checking its assumptions. Nonnegative truncation already did more direct work there. Understanding a theorem's boundaries matters more than putting its name everywhere.

## 10.6 How does a conditional average change when probability changes?

A density becomes useful by allowing integrals under one measurement to be computed under another.

If \(\nu=f\mu\), indicators, simple functions and monotone limits give

\[
\int h\,d\nu=\int hf\,d\mu\qquad(h\ge0).
\]

For absolutely integrable signed \(h\), handling positive and negative parts separately gives the same conclusion. This is the exact content of \(d\nu=f\,d\mu\).

If \(\eta\ll\nu\ll\mu\) and all three nonnegative measures are \(\sigma\)-finite, another application of the change-of-weight formula gives the chain rule

\[
\frac{d\eta}{d\mu}
=\frac{d\eta}{d\nu}\frac{d\nu}{d\mu}
\quad\mu\text{-a.e.},
\]

with measurable versions on the relevant null sets and the nonnegative-integral convention for products. The proof verifies that the product integrates to \(\eta\) on every event; it does not manipulate symbolic fractions.

Now let \(Q\ll P\) be probabilities, and write

\[
L=\frac{dQ}{dP},\qquad L\ge0,\quad\mathbb E_PL=1.
\]

For \(X\in L^1(Q)\) and the same observed information \(\mathcal G\), how should the new conditional average be calculated?

Compute two quantities under the old probability:

\[
D=\mathbb E_P[L\mid\mathcal G],\qquad
N=\mathbb E_P[LX\mid\mathcal G].
\]

Define \(Y=N/D\) on \(D>0\), and zero on \(D=0\). The latter event is \(Q\)-null because

\[
Q(D=0)=\mathbb E_P[L\mathbf1_{\{D=0\}}]
=\mathbb E_P[D\mathbf1_{\{D=0\}}]=0.
\]

The nonnegative pull-out property and \(|N|\le\mathbb E_P[L|X|\mid\mathcal G]\) ensure that

\[
\mathbb E_Q|Y|
=\mathbb E_P[D|Y|]
\le\mathbb E_P[L|X|]<\infty.
\]

For \(A\in\mathcal G\), bounded truncations followed by integral limits similarly justify the change of weight and give

\[
\int_A Y\,dQ
=\mathbb E_P[\mathbf1_A DY]
=\mathbb E_P[\mathbf1_A N]
=\mathbb E_P[\mathbf1_A LX]
=\int_A X\,dQ.
\]

Here \(N=0\) almost surely on \(D=0\): on that event \(L=0\) almost surely, so the conditional integral of \(LX\) vanishes. No numerator has been silently discarded.

Uniqueness yields

\[
\mathbb E_Q[X\mid\mathcal G]
=\frac{\mathbb E_P[LX\mid\mathcal G]}
{\mathbb E_P[L\mid\mathcal G]}
\quad Q\text{-a.s.}
\]

Chapter 2's instruction to reweight by a likelihood and then normalize has acquired a general structure. The numerator adjusts the payoff, the denominator the total weight within this information. Later stochastic-process theory will encounter changes of probability again; we now know how their basic accounts are balanced.

## 10.7 When the account contains both gains and losses

So far we have compared nonnegative measures. But the payoff in Chapter 1 can be replaced by a net payoff, making the account signed.

A zero total balance does not mean that nothing changed anywhere. One distinguishable region records a gain, another a loss. Combined, they can cancel; observed separately, they still carry quite different information. Keeping only the canceled total would conceal how this account differs from the original probability.

The density problem is therefore not quite over. We first need a total account that survives positive and negative cancellation, then a separation of gains from losses. Refining the observable regions and adding the absolute net change on each piece searches for precisely that total account. The ensuing decomposition will locate the positive and negative contributions.

For a signed measure \(\rho\) of finite variation, define

\[
|\rho|(A)=\sup_{\{A_j\}}\sum_j|\rho(A_j)|,
\]

where the supremum is over finite measurable partitions of \(A\), and assume \(|\rho|(S)<\infty\). Finite variation limits the total amount that can cancel across different regions.

This definition itself yields a nonnegative measure. For disjoint \(A_n\), combining nearly optimal partitions of finitely many \(A_n\) gives

\[
|\rho|\Bigl(\bigcup_nA_n\Bigr)\ge\sum_n|\rho|(A_n).
\]

Conversely, for any finite partition \(B_j\) of the union, countable additivity and the triangle inequality give

\[
\sum_j|\rho(B_j)|
\le\sum_n\sum_j|\rho(B_j\cap A_n)|
\le\sum_n|\rho|(A_n).
\]

Taking the supremum gives the reverse inequality. Thus \(|\rho|\) is countably additive and \(|\rho(A)|\le|\rho|(A)\).

Consequently,

\[
\rho^+=\frac{|\rho|+\rho}{2},\qquad
\rho^-=\frac{|\rho|-\rho}{2}
\]

are finite nonnegative measures with \(\rho=\rho^+-\rho^-\). If \(\rho\ll\mu\), then \(\rho\) vanishes on every measurable subset of a \(\mu\)-null set. Thus \(|\rho|\), \(\rho^+\) and \(\rho^-\) vanish on such sets too.

Apply the nonnegative density theorem for \(\sigma\)-finite \(\mu\) to obtain \(\rho^+=f_+\mu\), \(\rho^-=f_-\mu\), and hence

\[
\rho(A)=\int_A h\,d\mu,\qquad
h=f_+-f_-\in L^1(\mu).
\]

There is no infinity minus infinity: both densities have finite integrals. The signed Radon–Nikodym conclusion has therefore also been established. To prove a decomposition for any finite-variation account, no external reference need be specified: take \(\mu=|\rho|\), which is finite and automatically satisfies \(\rho\ll\mu\). The density construction above then always applies.

Comparing the partition \(\{h\ge0\}\), \(\{h<0\}\) with the triangle bound for arbitrary partitions verifies directly that

\[
|\rho|(A)=\int_A|h|\,d\mu,
\qquad \rho^+=h^+\mu,\quad \rho^-=h^-\mu.
\]

The two parts are supported on disjoint positive and negative regions. This is the Jordan decomposition of a finite-variation account. Its positive and negative contributions were not guessed from a canceled total; the measure's values on all distinguishable regions determine them together.

The density problem has now moved beyond nonnegative weights. The next distance to cross is between one weighting function and an entire probability that varies with observations.

## 10.8 What should a probability that varies with state satisfy?

For measurable spaces \((S,\mathcal S)\), \((T,\mathcal T)\), consider a map

\[
K:S\times\mathcal T\longrightarrow[0,1].
\]

Require that for each fixed \(s\), \(A\mapsto K(s,A)\) is a probability on \(T\), and for each fixed \(A\in\mathcal T\), \(s\mapsto K(s,A)\) is \(\mathcal S\)-measurable. Such \(K\) is a **probability kernel** from \(S\) to \(T\), also written \(K(s,dt)\).

The first requirement makes each state's experiment legitimate; the second lets experiments be integrated, assembled and observed when the state is itself random.

Measurability is not cosmetic. If the chance \(K(s,A)\) of an event \(A\) varies nonmeasurably with state, even averaging these chances may be undefined.

A kernel may be entirely deterministic. For measurable \(F:S\to T\),

\[
K(s,A)=\mathbf1_A(F(s))
\]

puts the next step at \(F(s)\). It may instead be Chapter 2's familiar coin rule:

\[
K(\theta,\{1\})=\theta,\qquad
K(\theta,\{0\})=1-\theta.
\]

Or it may describe Chapter 4's Gaussian displacement: for \(t>0\),

\[
K_t(x,A)=\int_A\frac1{\sqrt{2\pi t}}
\exp\!\left(-\frac{(y-x)^2}{2t}\right)\,dy.
\]

At \(t=0\), take \(K_0(x,\cdot)=\delta_x\). A position density at one time has become a rule for choosing a future position from the current one.

These examples include both densities and point masses. A kernel need not have a common length density. A conditional law must satisfy both kernel requirements, precisely what the arbitrary version choices in Section 10.1 failed to achieve.

## 10.9 Can choosing a state and then choosing an outcome form a common experiment?

Suppose we first choose \(s\) according to probability \(\mu\), then \(t\) according to \(K(s,dt)\). We want a joint probability

\[
\Gamma(ds,dt)=\mu(ds)K(s,dt).
\]

This must be more than attractive multiplication notation. For a product-measurable set \(E\subseteq S\times T\), let \(E_s=\{t:(s,t)\in E\}\). We must first prove that \(s\mapsto K(s,E_s)\) is measurable.

For a rectangle \(E=A\times B\), the function equals \(\mathbf1_A(s)K(s,B)\), so the claim holds. The class of sets with this property contains the whole space and is closed under complements because the kernel has total mass1; it is closed under countable disjoint unions by countable additivity at each state. The [\(\pi\)-\(\lambda\) theorem](../foundations/t-mclass.md#t-mclass-pi-lambda) therefore extends the property to all product events.

We can therefore define

\[
\Gamma(E)=\int_SK(s,E_s)\,\mu(ds).
\]

For disjoint \(E_n\), countable additivity at each \(s\), followed by monotone convergence, proves that \(\Gamma\) is a countably additive probability. Its values on rectangles are exactly those desired.

The same argument passes from indicators to nonnegative simple functions and then to nonnegative measurable \(h(s,t)\), giving the **kernel integration formula**:

\[
\int h\,d\Gamma
=\int_S\left[\int_T h(s,t)K(s,dt)\right]\mu(ds).
\]

The inner integral is measurable in \(s\). If \(\int|h|\,d\Gamma<\infty\), positive and negative parts can safely be subtracted. Chapter 6's Tonelli–Fubini mechanism no longer requires every state to use the same second-coordinate probability.

In particular, when a joint experiment is generated by \(\mu\) and \(K\),

\[
\mathbb E[h(S,T)\mid\sigma(S)]
=\int h(S,t)K(S,dt)
\]

holds for nonnegative or integrable \(h\). Verification remains Chapter 9's accounting test: integrating over \(\{S\in A\}\) gives equality on both sides.

Thus, once a kernel exists, all the averages acquire a common expression. We must now ask the reverse question: given only a joint experiment, can we always extract such a kernel?

## 10.10 How can rational marks repair uncountably many versions?

First let the outcome \(Y\) be real-valued, and let the observed information be an arbitrary sub-\(\sigma\)-algebra \(\mathcal G\).

For each rational number \(q\), choose a version

\[
F_q=\mathbb E[\mathbf1_{\{Y\le q\}}\mid\mathcal G].
\]

For now, instead of choosing versions separately for all Borel sets, we record only a ruler with rational marks.

Order preservation and conditional dominated convergence tell us that, outside null sets, these numbers are nondecreasing, lie in \([0,1]\), and tend to 1 and 0 as the rational marks tend to positive and negative infinity. For each rational \(q\), fix a rational sequence \(r_n\downarrow q\); then

\[
F_{r_n}\downarrow F_q\quad\text{a.s.}
\]

There are only countably many rational numbers, rational pairs and these selected approximating sequences. All bad points can therefore be included in a single \(N\in\mathcal G\), with \(P(N)=0\). On \(N\), replace every reading by that of the point mass \(\delta_0\).

Now, for every \(\omega\), rather than merely almost everywhere for one previously chosen relation, define

\[
F_\omega(t)=\inf_{q\in\mathbb Q,\ q>t}F_q(\omega).
\]

This function is nondecreasing and right-continuous, has limits 1 and 0 at positive and negative infinity, and agrees with the original \(F_q\) at rational points. Right-continuity comes from the same rational marks above a point: as \(t_n\downarrow t\), these upper sets recover the upper set for \(t\), so their infima agree in the limit.

Such a function really is the distribution function of a probability. To avoid hiding existence in a name, take uniform \(u\) on \((0,1)\) and define

\[
Q_\omega(u)=\inf\{q\in\mathbb Q:F_q(\omega)\ge u\}.
\]

The endpoint limits make it finite; monotonicity and right-continuity give

\[
Q_\omega(u)\le t\quad\Longleftrightarrow\quad u\le F_\omega(t).
\]

The image of uniform length under \(Q_\omega\) is therefore a probability with distribution function \(F_\omega\). Denote it by \(K(\omega,\cdot)\).

For half-lines, \(K(\omega,(-\infty,t])=F_\omega(t)\) is visibly measurable in \(\omega\). The Borel sets for which \(\omega\mapsto K(\omega,B)\) is measurable form a \(\lambda\)-system containing the rational half-lines that generate the Borel events. Hence \(K\) is a probability kernel from \((\Omega,\mathcal G)\) to the real line.

Finally, check that it really gives conditional probabilities. On rational half-lines this is the definition used to choose \(F_q\). The Borel sets for which

\[
\int_AK(\omega,B)\,dP(\omega)
=P(A\cap\{Y\in B\})\qquad(A\in\mathcal G)
\]

holds, denoted by \(B\), also form a \(\lambda\)-system containing the rational half-lines. Thus the identity holds for every Borel set.

We have obtained a **regular conditional distribution** of a real random variable given arbitrary \(\mathcal G\). For each fixed \(B\), it is a version of \(P(Y\in B\mid\mathcal G)\); for each fixed \(\omega\), it is an entire genuine probability.

If \(L\) is another such kernel, remove the null sets of version differences on all the countably many rational half-lines at once. At every remaining \(\omega\), the two probabilities agree. Thus there is one common null set outside which

\[
K(\omega,B)=L(\omega,B)
\quad\text{for every Borel }B
\]

holds simultaneously. We first coordinate versions with countably many marks, then recover all events by uniqueness of measures. We do not take the union of uncountably many exceptional sets.

## 10.11 If the outcome is a path, where can we find a rational ruler?

A Brownian path is not a real number, nor is a random tree. Does the preceding proof therefore offer only a narrow passage?

Chapter 8 defined a standard Borel space: a space in measurable bijection, with measurable inverse, with a Borel subset of a Polish space. The crucial fact is that each such space can be assigned **Borel addresses among the real numbers**.

The previous section succeeded not because real numbers are easy to draw, but because countably many rational questions already identify a real-valued distribution. We now seek similarly countable readings for more complicated outcomes: first ask which coarse cell contains the outcome, then which finer cell. A growing address should gradually remove uncertainty about position without listing every possible event at once.

But identifying a small cell at every stage is insufficient. The address must actually identify an outcome, reconstruction must be measurable, and false addresses lying beyond a cell's boundary must be excluded. The nested partitions, limit, and final boundary check below perform these three tasks. What we preserve is an address sufficient to reconstruct events, rather than a flattening of the object's geometry onto a line.

Let us explain how these addresses arise. In a nonempty complete separable metric space \(S\), cover the space by countably many small open balls, assign each point to the first ball that has not yet claimed it, and refine these Borel partitions successively. This gives countable partitions

\[
\mathcal P_n=\{C_{n,k}\}_k,
\qquad \operatorname{diam}(C_{n,k})\le2^{-n}.
\]

Number only nonempty cells, allowing numbering to start at 0, and choose a representative \(x_{n,k}\) in each cell. Every \(x\in S\) has an address of nonnegative integers \(a(x)=(k_1,k_2,\ldots)\), recording its cell at each level. Distinct points are eventually separated because the diameters of shared cells tend to 0.

Not every integer sequence is a valid address. First require the cells to be nested. These requirements involve only adjacent integer coordinates, so the sequences satisfying them form a Borel subset \(C\) of \(\mathbb N_0^{\mathbb N}\). For \(a\in C\), the representatives \(x_{n,k_n}\) form a Cauchy sequence; completeness supplies its limit \(L(a)\).

The limit map is measurable. For a closed set \(F\), the distance

\[
d(L(a),F)=\lim_n d(x_{n,k_n},F)
\]

is a measurable real function. Preimages of closed sets, and hence of all Borel sets, are measurable.

We must also prevent a limit from falling outside a half-open cell at its boundary. Retain only the addresses satisfying

\[
L(a)\in C_{n,k_n}\quad\text{for every }n
\]

and call their set \(D\). Each condition is a countable union over \(k\), so \(D\) is still Borel.

Now \(x\mapsto a(x)\) and \(a\mapsto L(a)\) are inverse measurable maps: \(S\) is measurably isomorphic to \(D\subseteq\mathbb N_0^{\mathbb N}\). For any Borel subset of \(S\), intersect the address set with its corresponding preimage under \(L\); the result is still Borel.

An integer address can also be encoded by a real number. Encode \((k_1,k_2,\ldots)\) as the binary symbol sequence

\[
0^{k_1}1\,0^{k_2}1\,0^{k_3}1\cdots,
\]

and replace symbols 0 and 1 by ternary digits 0 and 2. The symbol sequences with infinitely many separators 1 form a Borel set. Reading finitely many initial separators recovers finitely many initial integers, so both encoding and decoding are measurable. The ternary 0,2 encoding is a bijection onto the Cantor set; we need not use alternative expansions involving digit 1.

Consequently, between a standard Borel space \(S\) and some \(B\subseteq[0,1]\), there is a measurable bijection with measurable inverse

\[
b:S\longrightarrow B,\qquad B\text{ Borel}.
\]

In this proof, separability provides countably many questions, diameter control makes the address identify the point, completeness gives compatible addresses limits, and the final Borel condition prevents an address from pointing beyond a cell boundary. Together they explain why “standard Borel” supports conditional distributions, rather than serving as a decorative assumption.

For continuous paths, an address can retain sufficiently many readings at rational times; for finite-dimensional vectors, coordinate digits can be interlaced. We preserve event structure, without requiring a path to become a real line geometrically.

## 10.12 As the observation changes, how can an entire conditional law change with it?

Now let \(Y\) take values in a nonempty standard Borel space \(S\), and let the observation \(Z\) take values in a measurable space \(T\). Write \(\mu_Z\) for the law of \(Z\). We seek a kernel from \(T\) to \(S\) such that

\[
P(Y\in A,\ Z\in C)
=\int_C K(z,A)\,\mu_Z(dz).
\]

First encode \(Y\) as the real variable \(b(Y)\). For each rational \(q\), its conditional expectation is \(\sigma(Z)\)-measurable, so it can be written

\[
\mathbb E[\mathbf1_{\{b(Y)\le q\}}\mid\sigma(Z)]
=f_q(Z),
\]

where \(f_q:T\to[0,1]\) is measurable.

Write all the countably many conditions needed for the preceding real-valued construction directly as conditions on \(\{f_q(z)\}\). The values \(z\) violating them form a measurable \(\mu_Z\)-null set. Putting one fixed real point mass at these values gives a conditional kernel \(K_R\) from \(T\) to the real line.

But real addresses must return to \(B=b(S)\). Since \(b(Y)\in B\) almost surely,

\[
\int K_R(z,B)\,\mu_Z(dz)=1.
\]

Hence \(K_R(z,B)=1\) \(\mu_Z\)-almost everywhere. Include the measurable null set failing this requirement among the exceptions, and put \(\delta_{b(y_0)}\) there, with fixed \(y_0\in S\). We can now transport the probability back to \(S\) through \(b^{-1}\):

\[
K(z,A)=K_R(z,b(A)).
\]

The set \(b(A)\) is Borel because \(b^{-1}\) is measurable. Both kernel conditions and the conditional integral identity follow.

We have proved: **a standard Borel-valued random element has a regular conditional distribution given a measurable observation \(Z\); its version as an entire probability is unique \(\mu_Z\)-almost everywhere.** The observation space \(T\) needs no additional Polish assumption for this existence result. The outcome space whose law we describe needs the standard Borel structure.

If an arbitrary sub-\(\sigma\)-algebra \(\mathcal G\) is given directly, transporting the real construction to the address space likewise gives a conditional distribution kernel from \((\Omega,\mathcal G)\) to \(S\). We have not thereby proved that all events on an arbitrary original measurable space form a regular conditional probability: if the outcome is the original sample point itself, the original sample space must also undergo the relevant structural check.

This is stronger than Chapter 9's conclusion in a precise way. Conditional expectations do not require these countable addresses for the outcome space. Organizing countless conditional averages into a probability at each observation requires this structural bridge.

## 10.13 How can a joint probability unfold along the slices of an observation?

Suppose a joint probability \(\Gamma\) is given on \(S\times T\), where \(T\) is nonempty standard Borel. Let \(\mu\) be the marginal probability of the first coordinate.

On this joint space, regard the second coordinate as the outcome and the first as the observation. The existence theorem supplies a kernel \(K\). For each rectangle,

\[
\Gamma(A\times B)=\int_AK(s,B)\,\mu(ds).
\]

Section 10.9 proved that \(\mu(ds)K(s,dt)\) itself defines a probability. The two probabilities agree on the rectangular \(\pi\)-system, hence on the whole product \(\sigma\)-algebra:

\[
\Gamma(ds,dt)=\mu(ds)K(s,dt).
\]

This is **disintegration** of a joint probability. It separates the common experiment into where an observation appears and how an outcome is then chosen given that observation.

For every nonnegative measurable \(h\), we therefore have

\[
\int h(s,t)\,\Gamma(ds,dt)
=\int_S\int_T h(s,t)K(s,dt)\,\mu(ds).
\]

This is more than a formal identity on rectangles, and it does not require \(\Gamma\) to have a density with respect to some product length measure.

We can also slice along a general observation map. Let the original state space \(E\) be standard Borel, let \(P\) be a probability on it, and let \(T:E\to S\) be a measurable observation into a standard Borel space. Put \(\mu=T_*P\) and construct the kernel \(\kappa(s,dx)\) of the original state given the observation. Then

\[
P(A)=\int_S\kappa(s,A)\,\mu(ds).
\]

Moreover, for \(\mu\)-almost every \(s\), \(\kappa(s,\cdot)\) is actually concentrated on the slice \(T^{-1}\{s\}\).

This support statement also requires proof. Choose a countable point-separating Borel generating class \(C_n\) of \(S\). Since \(\mathbf1_{\{T\in C_n\}}\) is already readable from the observation,

\[
\kappa(s,T^{-1}C_n)=\mathbf1_{C_n}(s)
\quad\mu\text{-a.e.}
\]

Remove one common null set for all \(n\). For every remaining \(s\), at \(\kappa(s,\cdot)\)-almost every \(x\), the points \(T(x)\) and \(s\) answer all these questions identically, so \(T(x)=s\). Precisely,

\[
\kappa(s,T^{-1}\{s\})=1
\quad\mu\text{-a.e.}
\]

We cannot simply erase “almost every.” Some observation values correspond to no original state at all, and kernels on marginal null sets can still have different versions.

### 10.13.1 If the original measure is not a probability

Keep the previous section's assumptions: \(E,S\) are nonempty standard Borel spaces and \(T:E\to S\) is measurable. If \(P\) is a nonzero \(\sigma\)-finite measure on \(E\), and the marginal \(\mu=T_*P\) is also \(\sigma\)-finite, a disintegration into probability kernels relative to \(\mu\) still exists.

Choose a measurable \(w\), everywhere positive and finite, with \(\int w\,dP=1\). Partition the space into finite-measure pieces, assign sufficiently small positive weights to them, and normalize. Then \(R=wP\) is a probability. Disintegrate \(R\) as above to obtain probability kernels \(R_s\). Its marginal \(\mu_R\) is equivalent to \(\mu\), and

\[
g=\frac{d\mu_R}{d\mu}>0
\quad\mu\text{-a.e.}
\]

Choose a nonnegative measurable density representative. Since \(\mu_R\) has finite total mass, \(g\) is also finite \(\mu\)-almost everywhere. Let \(C_j\) be the countable separating generating class used above, and keep the states satisfying

\[
0<g(s)<\infty,\qquad
R_s(T^{-1}C_j)=\mathbf1_{C_j}(s)\quad\text{for every }j
\]

These states form a measurable set \(G_0\). Each condition has a \(\mu_R\)-null exceptional set; equivalence makes it \(\mu\)-null too, so \(\mu(S\setminus G_0)=0\). On \(G_0\), each \(R_s\) is concentrated on its corresponding fiber. This is one set of states valid simultaneously for all events to be integrated, rather than a fresh null set for each event.

On \(G_0\), define kernel measures temporarily permitting infinite total mass,

\[
\kappa(s,A)=g(s)\int_A\frac1{w(x)}\,R_s(dx).
\]

Outside \(G_0\), initially put the same fixed point mass \(\delta_{x_0}\), for a fixed \(x_0\in E\).

Kernel integration and the change-of-weight formula ensure measurability and give

\[
\int_C\kappa(s,A)\,\mu(ds)
=\int_{T^{-1}C}\mathbf1_A(x)\frac1{w(x)}\,R(dx)
=P(A\cap T^{-1}C).
\]

The change of weight uses fiber support on \(G_0\); the remaining states form a common marginal null set and do not affect the integral. Positivity and finiteness of \(g\) also avoid undefined multiplication of infinity by zero.

Take \(A=E\) and write \(h(s)=\kappa(s,E)\). Then \(\int_C h\,d\mu=\mu(C)\) for every measurable \(C\). To deduce normalization, cover \(S\) by countably many sets \(S_m\) of finite \(\mu\)-mass. The integral on each \(S_m\) is finite, hence \(h\) is finite almost everywhere there; uniqueness of finite densities then gives \(h=1\) almost everywhere. Combining the exceptions over all \(m\) still leaves one measurable null set.

Retain this kernel only on the measurable full-measure set \(G_0\cap\{h=1\}\), replacing the entire measure by \(\delta_{x_0}\) at every other state. We now have a probability at every state, measurable parameter dependence for every event, the reconstruction identity, and fiber support almost everywhere. Repairing bad values separately for each event would instead recreate the incompatibility of Section 10.1.

For another such disintegration, compare event integrals on pieces of finite marginal mass to obtain almost-everywhere equality for each fixed outcome event. Merge the exceptions over a countable generating \(\pi\)-system of \(E\), then use uniqueness of probability measures to recover every event. Uniqueness again means equality of the entire probability kernels off one common \(\mu\)-null set, not a unique pointwise answer at every null observation.

The two \(\sigma\)-finiteness requirements cannot be collapsed into one. For example, let \(P\) be length on the real line and let \(T\) always have the same observation value. The marginal has infinite mass at that value. A probability kernel relative to this marginal would give \([0,1]\) mass either 0 or infinity, never 1. A \(\sigma\)-finite original space need not have a \(\sigma\)-finite observed marginal.

## 10.14 Where does Bayes' formula reappear?

Suppose the joint probability has a nonnegative density \(p(s,t)\) relative to \(\alpha(ds)\beta(dt)\), with \(\sigma\)-finite reference measures \(\alpha,\beta\). Put

\[
m(s)=\int_Tp(s,t)\,\beta(dt).
\]

This is the marginal density relative to \(\alpha\). Where \(0<m(s)<\infty\),

\[
K(s,dt)=\frac{p(s,t)}{m(s)}\,\beta(dt)
\]

is a probability. The remaining values have zero marginal probability and may receive a fixed point mass. Kernel integration immediately verifies the disintegration identity. These are the conditions under which a conditional density formula applies, rather than a definition of every conditional distribution.

For example, take joint density 2 on the triangle \(0<y<x<1\). The first-coordinate marginal density is \(2x\), so for \(0<x<1\) the conditional probability of the second coordinate given the first is

\[
K(x,dy)=\frac1x\mathbf1_{(0,x)}(y)\,dy,
\qquad \mathbb E[Y\mid X]=\frac X2.
\]

After observing \(x\), the original triangle becomes a vertical slice. Dividing by the slice's total mass turns it back into a probability. We have finally given “average again over the remaining possibilities” an exact expression for continuous observations.

But this expression assumes a joint density exists. If \(Y=X\) almost surely, the joint probability lies on the diagonal and has no two-dimensional length density; its conditional kernel is nevertheless clear: \(K(x,\cdot)=\delta_x\).

Chapter 2's posterior has the same interpretation. Choose a parameter from the prior, then a record from the observation kernel; Section 10.9 has already established the joint probability. If the observation kernel has likelihood density \(\ell(\theta,z)\), reverse disintegration gives

\[
\Pi(d\theta\mid z)
=\frac{\ell(\theta,z)\Pi(d\theta)}
{\int\ell(a,z)\Pi(da)}
\]

at observation values with positive finite denominator. Forward experiment and backward inference are two unfoldings of the same joint measure, rather than unrelated probabilities.

## 10.15 How can the same diagonal leave two different conditional answers?

One interpretation of “given a zero-probability event” remains misleading: once regular conditional distributions exist, it can seem that a null event itself has a unique probability inside it.

Take uniform two-dimensional probability on the closed unit square \([0,1]^2\), with independent uniform coordinates \(X,Y\). At \(X>0\), first write two observations:

\[
D=Y-X,\qquad R=\frac{Y-X}{X}.
\]

The difference observation \(D\) is defined on the whole square; the relative difference still needs a boundary definition. Set explicitly

\[
R=\begin{cases}
(Y-X)/X,&X>0,\\
Y,&X=0.
\end{cases}
\]

Thus \(R\) is measurable and defined on the entire sample space. Choosing \(Y\) on the boundary also makes \(R=0\) and \(D=0\) exactly the same diagonal throughout the square. The boundary \(\{X=0\}\) has probability zero, so this extension changes none of the joint-density or conditional-distribution calculations below.

Since \(X>0\) almost surely, both \(D=0\) and \(R=0\) describe the same diagonal. Yet the observations organize nearby points into different slices.

For fixed \(x\), the one-dimensional substitution \(y=x+d\) gives the joint density of \((X,D)\):

\[
p_{X,D}(x,d)=\mathbf1_{\{0<x<1,\ 0<x+d<1\}}.
\]

At \(d=0\), choose the conditional version naturally specified by this formula. Then \(X\) is uniform on \((0,1)\).

Instead substitute \(y=x(1+r)\); for fixed \(x\), \(dy=x\,dr\). Thus

\[
p_{X,R}(x,r)=x\mathbf1_{\{0<x<1,\ 0<x(1+r)<1\}}.
\]

At \(r=0\), the corresponding conditional version gives \(X\) density \(2x\), with mean \(2/3\) rather than \(1/2\). Both formulas also arise as limits of conditional distributions when the respective observations fall in small intervals around 0. The denominators are nonzero near 0, and dominated convergence on a bounded region justifies the limits.

Neither probability is wrong. A narrow band of fixed differences and a narrow band of fixed relative differences retain different thicknesses at different \(x\); the latter carries the factor \(x\). Different observational experiments can yield different conditional distributions.

Even for a fixed observation, a version at one zero-probability observation value can still be changed. Kernel theory guarantees a measurable organization of the whole and uniqueness marginal-almost everywhere. It does not conjure an answer to every null event determined by that event alone.

This modern teaching example displays the mechanism commonly called Borel's conditioning paradox; it does not reproduce the particular geometry of Borel's original text. Chapter V of Kolmogorov's book also discusses conditional probability and Borel's paradox. Our square calculation directly exposes the distinction between the same null set and the same observation.

## 10.16 When can two selection rules really be joined?

Suppose \(K\) is a probability kernel from \(S\) to \(T\), and \(L\) one from \(T\) to \(U\). Define

\[
(KL)(s,A)=\int_TL(t,A)K(s,dt).
\]

Kernel integration makes this measurable in \(s\); for each \(s\), nonnegative integration and countable additivity make it a probability. This is composition of kernels.

For nonnegative functions, repeated use of Section 10.9's integral identity proves associativity. It describes a definite sequential experiment: from \(s\), choose \(t\), then choose \(u\) using only \(t\).

“Using only \(t\)” cannot be omitted. Let \(X=Z\) be a fair coin in an existing world and let \(Y\) be another independent fair coin. Both \(Y\) given \(X\) and \(Z\) given \(Y\) are uniform. Composing the two kernels remains uniform, whereas \(Z\) given \(X\) is the point mass \(\delta_X\), not uniform.

Thus we cannot join two conditional kernels for arbitrary three variables and claim to obtain the third conditional kernel. In an existing joint world, we must explain that the law of \(Z\) given \((X,Y)\) depends only on \(Y\), or that sufficient nesting of information holds. For a new sequential experiment generated by \(\mu\), \(K\) and \(L\), this property is explicitly part of the model.

Chapter 4's Gaussian motion supplies a particularly important composition law. For \(s,t>0\), completing the square gives

\[
\frac{(y-x)^2}{s}+\frac{(z-y)^2}{t}
=\frac{s+t}{st}\left(y-\frac{tx+sz}{s+t}\right)^2
+\frac{(z-x)^2}{s+t}.
\]

Multiply the two Gaussian densities and integrate in \(y\). The first term supplies the normalizing factor, leaving

\[
K_sK_t=K_{s+t}.
\]

Moving for time \(s\), then moving from the current position for time \(t\), is consistent in position distribution with moving directly for \(s+t\). The structural connection between random motion and heat propagation is now a kernel composition identity. Yet consistent position transitions do not prove continuous paths exist; a kernel symbol cannot automatically solve Chapter 4's path problem.

## 10.17 Can the same simple random source drive all these choices?

The distribution-function construction already suggests that a uniform random number, under a suitable measurable transformation, can generate any real-valued probability.

This transformation can also vary measurably with a parameter. Let \(K\) be a probability kernel from an arbitrary measurable parameter space \(S\) to the real line. Write

\[
F(s,q)=K(s,(-\infty,q]),\qquad
Q(s,u)=\inf\{q\in\mathbb Q:F(s,q)\ge u\},\quad0<u<1.
\]

For each \(s\), it has the quantile property established above. Joint measurability follows from

\[
\{(s,u):Q(s,u)<a\}
=\bigcup_{q\in\mathbb Q,\ q<a}\{(s,u):u\le F(s,q)\}.
\]

The right side is a countable union of product-measurable sets. Thus this is a jointly measurable method in the state and the random number, rather than a sampling method existing separately for each fixed parameter.

If the outcome space \(T\) is nonempty standard Borel, push the kernel through the address map \(b:T\to B\subseteq[0,1]\) of Section 10.11, form a real-valued quantile, then return through \(b^{-1}\).

For some length-zero sets of \(u\), the quantile may fall outside \(B\). Since \(B\) is Borel, the bad set \(\{(s,u):Q(s,u)\notin B\}\) is jointly measurable. Replace its values by a fixed \(t_0\). For every \(s\), the bad section has uniform probability 0, so no target probability changes.

We have proved the **randomization representation of a kernel**: there is a measurable \(\Phi:S\times(0,1)\to T\) such that, for each fixed \(s\),

\[
\operatorname{Law}(\Phi(s,U))=K(s,\cdot),
\qquad U\text{ uniform on }(0,1).
\]

Every state uses the same uniform random source. What changes is the measurable selection rule. A probability kernel therefore describes what can happen and how to realize those possibilities on a common space.

## 10.18 If the next experiment depends on the whole past, does an infinite record still exist?

Chapter 8 already allowed each coin's chances to depend on the preceding record. Replace the coins now by general nonempty standard Borel state spaces \(E_0,E_1,\ldots\).

Specify an initial probability \(\mu_0\) and probability kernels from \(E_0\times\cdots\times E_n\) to \(E_{n+1}\),

\[
K_n(x_0,\ldots,x_n;dx_{n+1}).
\]

We seek an infinite experiment that unfolds according to these rules. This standard Borel version is a form of the **Ionescu–Tulcea construction**. We shall actually construct it, without hiding existence in the words “sample successively.”

By Chapter 8, independent uniforms \(U_0,U_1,\ldots\) exist. Regard \(\mu_0\) as a kernel from a one-point parameter space, and use randomization to choose \(X_0=\Phi_0(U_0)\). Recursively define

\[
X_{n+1}=\Phi_{n+1}(X_0,\ldots,X_n,U_{n+1}),
\]

where \(\Phi_{n+1}\) realizes \(K_n\). Each \(X_n\) is a measurable function of finitely many preceding uniform coordinates, so the recursion has a common home. Finite products of standard Borel spaces are still standard Borel, as Chapter 8's Polish realizations or the countable addresses above directly verify.

Since \(U_{n+1}\) is independent of preceding uniform coordinates, Tonelli integration after fixing the past gives

\[
\mathbb E[h(X_{n+1})\mid\sigma(X_0,\ldots,X_n)]
=\int h(y)K_n(X_0,\ldots,X_n;dy)
\]

for all nonnegative or integrable \(h\). Precisely, multiply by any bounded past-measurable weight, integrate first over \(U_{n+1}\), and compare with Chapter 9's definition.

Push the whole sequence \((X_0,X_1,\ldots)\) onto the product space to obtain the required probability. Its finite windows are uniquely determined by repeated kernel integration:

\[
\mu_0(dx_0)K_0(x_0,dx_1)\cdots
K_{n-1}(x_0,\ldots,x_{n-1};dx_n).
\]

Another experiment with the same initial law and conditional rules therefore agrees on every cylinder. By \(\pi\)-\(\lambda\) uniqueness, the laws of the entire records agree. This proves existence and uniqueness in law in the standard Borel scope of this section. The Ionescu–Tulcea theorem for general measurable state spaces has a broader, dedicated extension proof; our encoding argument is not a substitute for that wider version. See the [uniqueness companion](../foundations/t-mclass.md#t-mclass-uniqueness) for finite-probability uniqueness on cylinders and the common finite cover required in σ-finite extensions.

If \(K_n\) depends only on the last state, the past can be compressed into the present, producing Markov structure. If it depends on the whole history, we still have a legitimate infinite experiment, but must not mistakenly attribute the same Markov property to it.

The fair choices of Chapter 1, the unknown parameter of Chapter 2, the position transitions of Chapter 4 and the infinite records of Chapter 8 now enter one language: specify a joint rule, then arrange each step with measurable kernels. Drawing an apparently random record is not a proof that its probability exists.

## Chapter 10 epilogue: behind an average, an entire world takes shape

At first, we only wanted to know how to divide the gold on the table.

Then we discovered that a fair price must respect the information already known. Today, the entire experiment behind that price has acquired a clear structure: densities redistribute weight between measures, singular parts locate mass invisible to a reference, conditional laws organize all events after an observation into a probability, and disintegration unfolds the joint world along observations.

The subtlest step was to make countless separately correct answers correct together. Rational marks and countable addresses allow observations that cannot be handled by direct division by their probabilities to live within a measurable, coherent system of laws.

We have not thereby learned the future. Given the present position, a Gaussian kernel is still only a law of future positions. Continuous paths, first boundary-crossing times and finer path properties await us. Kernels first make “continue the experiment according to what is currently known” legitimate mathematics.

But as distributions are repeatedly generated through kernels, a new question appears: how do we recognize these distributions? How can we tell that two apparently different constructions yield the same law? When many small independent displacements are added, what calculations explain the bell curve that repeatedly appeared in Chapter 3?

In the next chapter, we shall find new readings for a distribution. Applying an exponential function to a random variable turns probability into a function of frequency; independent addition becomes multiplication. This road will bring the earlier Gaussian limit back in rigorous modern language and prepare tools for more general limit laws.

We know how to generate a random world. Next, we must learn how to hear the distribution it leaves behind.

## History and further reading

Nikodym, *Sur une généralisation des intégrales de M. J. Radon*, *Fundamenta Mathematicae*15(1930),131–179: [original journal and DOI](https://doi.org/10.4064/fm-15-1-131-179). This chapter's tagged-mixture experiment, its route from conditional averages to densities, and all teaching examples are modern mathematical reconstructions, not attributed to the paper's original narrative or proof.

Kolmogorov, *Grundbegriffe der Wahrscheinlichkeitsrechnung*, Chapter V: [original book record](https://link.springer.com/book/10.1007/978-3-642-49888-6). We pursue the conditioning and zero-probability observation questions genuinely present there, without claiming our square example is the book's own example.

For the modern theoretical scope of kernels, conditional laws and random sequences, see the [official contents of Kallenberg's third edition](https://link.springer.com/book/10.1007/978-3-030-61871-1). A course entry into joint laws and conditional kernels is available in the [Berkeley probability course record](https://www.stat.berkeley.edu/users/aldous/205B/index.html). This chapter proves the finite and \(\sigma\)-finite density results it uses, standard Borel coding, existence of conditional kernels, disintegration and sequential construction in the stated scope, keeping conclusions for standard Borel and arbitrary measurable spaces distinct.
