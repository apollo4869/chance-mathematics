# The Mathematics of Chance
Volume II · Probability in an Infinite World

# Chapter 8: How Can We Construct an Infinite Random Experiment?

By the end of [the preceding chapter](#chapter-7), we could already follow an infinite observation record forward.

We knew that small-probability events might recur, how to extract an almost surely convergent subsequence from convergence in probability, and how a spike can escape the limit of expectations. But all those discussions began in the same place: a probability space already existed, and every random variable already lived there.

For a moment, let us put that premise aside.

There is just one coin on the table. Toss it once and we can write down the probabilities of two outcomes; twice, and we can write down four. For any finite number of tosses specified beforehand, we can state the rules perfectly clearly.

But is ‘we can do this for every finite number’ the same as ‘there is one place that accommodates all those numbers’?

We are not asking whether we can actually sit at the table tossing forever. Mathematics requires another kind of existence: a sample space whose individual outcomes are complete infinite records, with a countably additive probability agreeing with our original rules on every finite part of a record.

Without such a space, the preceding chapter’s claims about infinitely many exceptions and long-term frequencies would have no common object to describe.

We must therefore examine a move we have repeatedly passed over lightly: when we write ‘let \(X_1,X_2,\ldots\) be a sequence of random variables’, what exactly have we promised?

## 8.1 Every Finite Record Can Be Correct While the Whole World Is Wrong

First try to build a world that looks economical.

Use 1 for heads and 0 for tails, and allow only infinite records that are eventually all zero:

\[
\Omega_{\mathrm{fin}}
=\{\omega\in\{0,1\}^{\mathbb N}:
\omega_n=0\text{ for all sufficiently large }n\}.
\]

This space obstructs no finite experiment. Any prescribed finite string of zeros and ones can be placed at the beginning and followed forever by zeros. We can even prescribe outcomes at any finite set of positions and still find a realization here.

It is therefore tempting to assign each prefix of length \(m\) probability \(2^{-m}\), just as for independent fair tosses.

A difficulty appears immediately.

Fix one record \(\omega\). Its singleton event lies inside every finite prefix event agreeing with it. Any probability with those finite rules must therefore satisfy

\[
0\le P(\{\omega\})\le2^{-m}
\quad\text{for every }m,
\]

Hence \(P(\{\omega\})=0\). The singleton is indeed measurable: it is the countable intersection of events fixing the coordinates one by one.

But \(\Omega_{\mathrm{fin}}\) is countable. It is the countable union, as \(m\) increases, of the finite sets of records that are all zero after step \(m\). Countable additivity therefore requires

\[
P(\Omega_{\mathrm{fin}})
=\sum_{\omega\in\Omega_{\mathrm{fin}}}P(\{\omega\})=0,
\]

which must also equal 1.

No calculation for an individual toss caused the contradiction. Every finite window fails to detect what is missing from this world; the omission appears only when the windows are combined.

This is more specific than saying that infinity is complicated. It tells us: **realizing finite experiments one at a time does not guarantee that a casually chosen sample space can support their probabilities simultaneously.**

[Chapter 5](#chapter-5) taught us not to abandon countable additivity in order to measure every set. We must not abandon it now to preserve a sample space that is too small.

We need a space that genuinely accommodates every infinite record, and a proof that probability can be established there.

## 8.2 An Infinite Record Is a Whole Sequence of Coordinates, Not One Large Number

The most natural choice initially excludes no records:

\[
\Omega=\{0,1\}^{\mathbb N}.
\]

A point of this space is \(\omega=(\omega_1,\omega_2,\ldots)\). The outcome of experiment \(n\) becomes a coordinate function:

\[
X_n(\omega)=\omega_n.
\]

First comes the record, then the coordinates that read it. We need not search for random variables in some mysterious background space. Make the complete record itself a sample point, and the variables arise by reading it.

Yet \(\Omega\) is so far only a set. Writing it down has specified neither events nor probabilities.

The events a finite experiment can first answer are requirements such as

\[
\{X_1=1,\ X_3=0,\ X_{10}=1\}
\]

It observes only finitely many coordinates, leaving every other coordinate free. Such a set is called a **cylinder set**.

The name has a geometric interpretation: specify a cross-section in certain directions and extend freely in the others. There may now be infinitely many freely extending directions.

For general nonempty measurable state spaces \((E_n,\mathcal E_n)\), we can likewise take

\[
\Omega=\prod_{n\ge1}E_n,
\qquad \pi_n(\omega)=\omega_n.
\]

The smallest event system should make every coordinate reading measurable. We therefore define

\[
\bigotimes_{n\ge1}\mathcal E_n
=\sigma\{\pi_n^{-1}(A):n\ge1,\ A\in\mathcal E_n\}.
\]

This is the **product \(\sigma\)-algebra**. It is also generated by all finite-dimensional cylinder sets.

Notice that we have defined a product measurable structure, not obtained a product probability. Writing \(\bigotimes\) between \(\sigma\)-algebras cannot replace an existence proof for a probability measure.

This event system nevertheless includes much more than finite observations. Repeated countable unions, intersections and complements express infinite requirements. In the coin space, for example,

\[
\{X_n=1\text{ infinitely often}\}
=\bigcap_{m\ge1}\bigcup_{n\ge m}\{X_n=1\}.
\]

‘The frequency of heads tends to \(1/2\)’ can also be written

\[
\bigcap_{r\ge1}\bigcup_{N\ge1}\bigcap_{n\ge N}
\left\{\left|\frac1n\sum_{j=1}^nX_j-\frac12\right|<\frac1r\right\}.
\]

The long-term fate of an infinite record has thus entered the \(\sigma\)-algebra generated by finite observations.

We know which questions we can ask. Next we must give them mutually compatible probability answers.

## 8.3 Overlapping Experimental Records Must Tell the Same Story

Suppose someone gives us a joint probability \(\mu_n\) for the first \(n\) experiments, separately for each length. The legality of each probability alone is not enough.

If the two-experiment distribution says ‘the first result must be 0’, but the one-experiment distribution says ‘the first must be 1’, they cannot come from one record. Deleting the second observation must not change the law of the first.

We must therefore have

\[
\mu_{n+1}(A\times E_{n+1})=\mu_n(A),
\qquad A\in\bigotimes_{j=1}^n\mathcal E_j.
\]

This is **consistency**. It does not require independence between variables; it requires observation windows of different sizes not to contradict one another.

The individual distributions of the coordinates do not provide this information. Suppose \(X_1,X_2\) both take 0 or 1 with equal probabilities. They may always agree, always disagree or be independent. All three worlds have the same individual coordinate distributions but different two-experiment records.

This is the issue recurring in Chapters 1, 4 and 7: marginal laws do not determine how variables live together. An extension theorem will not choose dependence for us. We must supply the finite-dimensional joint relationships we want.

Even ‘every pair of experiments has a valid joint distribution’ may be insufficient. Require every pair among three 0–1 variables to disagree with probability 1, while each individual distribution is fair. Every two-dimensional distribution is valid and their one-dimensional marginals agree. But if the first disagrees with the second, and the second with the third, the first must agree with the third, violating the third requirement.

We cannot merely tick off neighboring windows independently. We need a consistent family containing all finite windows, each larger window genuinely accommodating all its smaller ones.

If observation times form a general index set \(T\) rather than \(1,2,\ldots\), the clearest notation is to assign, for every nonempty finite subset \(J\subseteq T\), a probability measure on

\[
E_J=\prod_{t\in J}E_t
\]

denoted by \(\mu_J\). If \(J\subseteq K\), project from the larger window onto the coordinates in \(J\), writing the projection as \(\pi_{K,J}\). We require

\[
\mu_K\circ\pi_{K,J}^{-1}=\mu_J.
\]

Indexing coordinates by finite sets already incorporates the compatibility needed for changing their order. If distributions are instead indexed by ordered time lists, we must also specify that jointly permuting times and coordinates does not change the probability’s meaning.

The question is now precise: **can a consistent family of finite-dimensional probabilities become all the finite-dimensional distributions of one infinite record space?**

## 8.4 We Can Balance Finite Accounts, but Have Not Crossed the Countable Threshold

Return for now to countably many experiments. Let \(\pi_{1:m}\) project onto the first \(m\) coordinates. All sets of the form

\[
C=\pi_{1:m}^{-1}(B),
\qquad B\in\bigotimes_{j=1}^m\mathcal E_j
\]

form an algebra \(\mathcal A\): combine two finite observations in a common longer prefix, and their union, intersection or complement remains a finite observation.

Naturally, we want to define

\[
p_0(C)=\mu_m(B).
\]

First check that the number does not depend on the cylinder’s representation. If different prefix lengths represent the same set, lift both to the longer prefix. Coordinate projections are surjective, and consistency ensures that deleting extra coordinates leaves probability unchanged. The two computations therefore agree.

Likewise, lifting finitely many disjoint cylinders to one common window gives finite additivity directly from that finite-dimensional probability.

At this point, \(p_0\) is an account with no finite contradiction.

But we want countable additivity, not just finite additivity.

If \(A_1,A_2,\ldots\in\mathcal A\) are pairwise disjoint and their union \(A\) still belongs to \(\mathcal A\), we also need

\[
p_0(A)=\sum_{n\ge1}p_0(A_n).
\]

A nonnegative additive function satisfying this requirement is called a **premeasure**. The algebra itself need not be closed under arbitrary countable unions; the requirement applies whenever the union stays in its domain. Extending to \(\sigma(\mathcal A)\) will complete the event system.

How can we test this step? For a nonnegative finitely additive function of finite total mass, the answer is closely connected to the preceding chapter: test the limit of decreasing events.

\[
C_n\in\mathcal A,\quad C_n\downarrow\varnothing
\qquad\Longrightarrow\qquad p_0(C_n)\longrightarrow0.
\]

Why is this condition sufficient? Truncate the countable decomposition of \(A\) after its first \(m\) terms. The remainder

\[
R_m=A\setminus\bigcup_{n=1}^mA_n
\]

still belongs to the algebra and decreases to the empty set. Finite additivity gives

\[
p_0(A)=\sum_{n=1}^m p_0(A_n)+p_0(R_m).
\]

Let \(m\to\infty\). The remaining mass vanishes, giving countable additivity.

Conversely, if \(C_n\downarrow\varnothing\), the differences \(C_n\setminus C_{n+1}\) are pairwise disjoint and their union is \(C_1\). A premeasure’s countable additivity splits that finite total mass into a convergent series. The value \(p_0(C_m)\) is precisely the tail beginning at term \(m\), so it tends to zero.

The difficulty of infinite extension has thus become one question: **when finite observations tighten until no complete record can satisfy them, must their probabilities disappear too?**

The too-small coin world at the beginning fails exactly here.

Enumerate the records in \(\Omega_{\mathrm{fin}}\) as \(\omega^{(1)},\omega^{(2)},\ldots\). Given \(0<\varepsilon<1\), choose a sufficiently long prefix cylinder \(H_j\) around the \(j\)th record, such that

\[
\omega^{(j)}\in H_j,
\qquad p_0(H_j)<\varepsilon2^{-j}.
\]

Their countable union covers all of \(\Omega_{\mathrm{fin}}\). Yet

\[
D_m=\Omega_{\mathrm{fin}}\setminus\bigcup_{j=1}^mH_j
\downarrow\varnothing,
\qquad p_0(D_m)>1-\varepsilon.
\]

Here \(p_0\) is the finitely additive function defined by the fair finite-prefix rules; the probability bound for finite unions follows from finite additivity. Every finite account balances, yet the remaining mass has nowhere to settle in the end.

Thus, ‘apply the measure extension theorem’ must never be a phrase that skips the difficulty. We must first prove that our cylinder probabilities really form a premeasure before we are entitled to use it.

## 8.5 If the Finite Ledger Is Reliable Enough, How Does Outer Measure Extend It?

First let us clarify the extension tool itself. Let \(\mathcal A\) be an algebra on \(\Omega\), and let \(p_0\) be a premeasure on it, with \(p_0(\Omega)=1\).

In [Chapter 5](#chapter-5), we used interval covers to measure sets of real numbers whose measurability was not yet known. Now we replace intervals with algebra events that already have probabilities; the rest of the idea still applies:

\[
p^*(H)=\inf\left\{
\sum_{n\ge1}p_0(A_n):
H\subseteq\bigcup_{n\ge1}A_n,\ A_n\in\mathcal A
\right\}.
\]

This number is defined for every \(H\subseteq\Omega\). Since \(\Omega\in\mathcal A\), there is at least one cover with total cost 1.

The empty set has size 0, and covering a larger set cannot cost less. For each set choose a cover within \(\varepsilon2^{-n}\) of its optimal cost, then combine these covers to obtain countable subadditivity. Thus \(p^*\) is an outer measure.

Does it really preserve the old accounts? For \(A\in\mathcal A\), covering the set by itself gives \(p^*(A)\le p_0(A)\). Conversely, if \(A\subseteq\bigcup_nA_n\), put

\[
B_n=A\cap\left(A_n\setminus\bigcup_{j<n}A_j\right).
\]

These sets belong to the algebra, are pairwise disjoint, and have union \(A\). The premeasure property therefore gives

\[
p_0(A)=\sum_n p_0(B_n)\le\sum_n p_0(A_n).
\]

Taking the infimum over all covers yields \(p^*(A)\ge p_0(A)\). Combining the two directions, not a single old event has changed its probability.

This argument also makes the importance of the premeasure hypothesis explicit: finite additivity alone gives no reason why the probabilities of this countable decomposition of \(A\) should add back to its original probability. In the flawed world at the start, even a space of total mass 1 can be swallowed by countable covers of arbitrarily small cost.

Now use Carathéodory's splitting criterion to select events:

\[
H\in\mathcal M
\quad\Longleftrightarrow\quad
p^*(Q)=p^*(Q\cap H)+p^*(Q\setminus H)
\quad\text{for all }Q\subseteq\Omega.
\]

Every \(A\in\mathcal A\) passes this test. Indeed, intersect each set in an arbitrary cover with \(A\) and its complement. Finite additivity splits the original covering cost into two parts; taking infima gives one required inequality, while the reverse inequality follows from subadditivity of outer measure.

The proof of this criterion in Chapter 5 and [Supplementary Proof A](#supplement) used only the properties of outer measure, without relying on the real line: \(\mathcal M\) is a \(\sigma\)-algebra, and the restriction of \(p^*\) to it is a countably additive measure. Thus

\[
\mathcal A\subseteq\sigma(\mathcal A)\subseteq\mathcal M,
\qquad P=p^*|_{\sigma(\mathcal A)}
\]

gives the probability extension we wanted.

This extension is also unique on \(\sigma(\mathcal A)\). If \(Q\) is another probability preserving \(p_0\), then for any measurable \(H\), any algebra cover gives \(Q(H)\le\sum_n p_0(A_n)\), so

\[
Q(H)\le p^*(H)=P(H).
\]

Apply the same inequality to complements and use the fact that both measures have total mass 1 to obtain the reverse inequality. Hence \(Q(H)=P(H)\).

This is the **Carathéodory probability measure extension theorem** used in this chapter: a probability premeasure on an algebra has a unique probability extension to the \(\sigma\)-algebra it generates. Outer measure also gives a larger, complete measurable structure; later we will explain why retaining the generated \(\sigma\)-algebra first is usually clearer. For probabilities and measures with a common finite cover, the [generating-class uniqueness theorem](../foundations/t-mclass.md#t-mclass-uniqueness) gives another uniqueness route; it does not replace the existence construction here.

The tool is ready. The unfinished task is to prove that the cylinder ledger supplied by consistent finite-dimensional laws remains trustworthy at countable limits.

## 8.6 In the Coin World, How Does Compactness Prevent a Record from Disappearing?

On the full coin space \(\{0,1\}^{\mathbb N}\), we can first see a particularly transparent proof.

Give each coordinate the discrete topology. Regard two records as closer when their first disagreement occurs later; for example, use the metric

\[
d(\omega,\eta)=\sum_{j\ge1}2^{-j}|\omega_j-\eta_j|.
\]

This space is compact. Given any sequence of records, first select an infinite subsequence with the same first entry, then one with the same second entry, and continue. The diagonal subsequence eventually stabilizes in each coordinate and therefore converges in the metric above.

A cylinder observing only the first \(m\) entries is closed, and indeed open, since these coordinates have only finitely many possible states. If \(C_n\) is a decreasing sequence of nonempty cylinders, choose a record from each \(C_n\). Diagonal selection and closedness produce a record belonging to every \(C_n\).

Consequently, if \(C_n\downarrow\varnothing\), one of these sets must already be empty; all subsequent probabilities are then zero. The fair cylinder probability thus satisfies continuity from above and is a premeasure. The extension theorem finally supplies the probability for infinitely many fair coin tosses.

Compared with \(\Omega_{\mathrm{fin}}\), the difference lies in none of the finite accounts. As finite records become longer, the full space retains their limiting records, while the undersized space excludes some of those limits.

Compactness has not calculated any probabilities for us. It prevents a situation in which every finite requirement can be met, yet the infinite collection suddenly has nowhere to be realized.

The states of real random variables are not limited to 0 and 1. The real line is not compact, and Borel sets need not be closed. How much of this proof can survive?

The answer is not to demand that all state spaces be compact from the outset, but to use probability: we can discard arbitrarily little mass and keep the essential part inside a compact set.

## 8.7 Real Numbers Can Escape to Infinity—Why Can Probability Still Find Compact Ground?

First look at the real line. For any Borel probability \(\mu\),

\[
\mu([-R,R])\uparrow1.
\]

It is therefore tight: precisely the tightness of a single measure distinguished in Section 7.15.1.

For our construction, however, we also need to approximate a particular Borel event from within by a compact set; approximating the whole space is not enough.

Think about what the next step will require. An event in a finite window may have holes, with no obvious boundary to follow. Knowing that most mass lies in a compact set does not make its intersection with that event closed: a limiting record might still slip through a hole. We need the compact set inside the event, not merely near it.

On the real line and in finite-dimensional Euclidean space, this is a manifestation of measure regularity. We will prove what we need in a slightly broader and more useful setting.

A metric space is called a **Polish space** if it is separable and its topology can be induced by a complete metric. We use such a complete metric here. Important examples include the real line, finite-dimensional Euclidean spaces, countable discrete spaces, and \(C([0,1])\) with the uniform metric. The last space is complete because uniform limits of continuous functions remain continuous; separability follows by approximation with piecewise linear functions having rational breakpoints and rational vertex values.

On a Polish space \(S\), every Borel probability \(\mu\) is tight. We can see the mechanism directly.

Fix \(\varepsilon>0\). For each \(k\), separability supplies a countable cover of \(S\) by open balls of radius \(2^{-k}\). By continuity from below, select finitely many whose union has probability greater than \(1-\varepsilon2^{-k}\). Replace these balls with closed balls and call the resulting closed set \(F_k\). Set

\[
K=\bigcap_{k\ge1}F_k.
\]

Countable subadditivity gives \(\mu(K)\ge1-\varepsilon\). The set \(K\) is closed and therefore complete; at every scale it can also be covered by finitely many sufficiently small balls, so it is totally bounded. Completeness and total boundedness make it compact: successively finer finite covers yield a Cauchy subsequence, and completeness keeps the limit inside the set.

Separability supplies finite approximations; completeness retains their limits. Probability organizes both within one high-probability set.

The compact ground just found for the whole space does not yet explain how a particular event can retain its own mass. To enter the event, we first find a closed inner approximation, then keep it within that compact ground.

For a finite Borel measure, any Borel set \(A\) and any \(\eta>0\) admit a closed set \(F\) and an open set \(G\) such that

\[
F\subseteq A\subseteq G,
\qquad \mu(G\setminus F)<\eta.
\]

We need not introduce regularity as an unexplained black box. A closed set \(F\) can be approximated from outside by the open neighborhoods \(\{x:d(x,F)<1/m\}\); continuity from above for a finite measure makes the error tend to zero. The sets that can be enclosed arbitrarily closely between an inner closed set and an outer open set are closed under complements. They are also closed under countable unions: assign each term a small error with summable total, cover from outside by the union of the open sets, then approximate the first finitely many terms from within by the union of their closed sets. Continuity from below controls the mass beyond these finite terms. This class is therefore a \(\sigma\)-algebra containing the closed sets, and hence contains every Borel set.

More explicitly, for a union \(A=\bigcup_nA_n\), first make the sum of the individual enclosure errors less than \(\eta/4\), then choose \(N\) so that \(\mu(A\setminus\bigcup_{n\le N}A_n)<\eta/2\). Take \(G=\bigcup_nG_n\) and \(F=\bigcup_{n\le N}F_n\); the sum of the two errors is less than \(\eta\). This completes the countable-union step.

Finally, intersect the inner closed set with a global compact set of sufficiently large mass to obtain

\[
\forall A\in\mathcal B(S),\ \forall\varepsilon>0,
\quad\exists L\subseteq A\text{ compact},
\qquad\mu(A\setminus L)<\varepsilon.
\]

This is called **inner regularity by compact sets** for Borel probabilities. It goes one step beyond finding a high-probability compact set for the whole space, and this extra step allows finite-dimensional events of arbitrary shape to enter our compactness argument.

A finite product of Polish spaces is again Polish: the complete coordinate metrics combine into a complete metric, and the finite product of countable dense sets preserves separability. Its Borel \(\sigma\)-algebra also equals the finite product \(\sigma\)-algebra, because rectangles from countable topological bases generate every open set. The preceding result therefore applies to the joint probability in each finite window.

We can now replace ‘cylinders are already closed’ in the coin proof with ‘the finite-dimensional base of a cylinder can be approximated from within by compact sets.’

## 8.8 How Can One Record Be Found among Infinitely Many Finite Requirements?

We can finally confront the core construction.

In the coin space, the proof combined two jobs: restrictions could not drive records to infinity, and limits could not destroy restrictions already satisfied. Compact approximation now takes over both jobs. Probability ensures that finite-stage witnesses survive the approximation; topology then finds a common record. This division of work is what allows the proof to cross into the infinite.

Let each \(E_j\) be a nonempty Polish space equipped with its Borel \(\sigma\)-algebra. Suppose the probabilities \(\mu_m\) on the first \(m\) coordinates are consistent. We have already defined the finitely additive \(p_0\) on the cylinder algebra.

It remains only to prove that if \(C_n\downarrow\varnothing\), then \(p_0(C_n)\to0\).

If this fails, monotonicity implies that the probabilities of these decreasing sets are all at least some \(\delta>0\). We may write each cylinder as

\[
C_n=\pi_{1:m_n}^{-1}(B_n),
\qquad m_n\ge n,
\qquad m_{n+1}\ge m_n.
\]

This merely permits us to observe more coordinates at each stage, without changing the event. By compact inner regularity of finite-dimensional probabilities, choose a compact set \(K_n\) inside \(B_n\) such that

\[
\mu_{m_n}(B_n\setminus K_n)<\delta2^{-n-2}.
\]

Write the corresponding closed cylinder as

\[
D_n=\pi_{1:m_n}^{-1}(K_n)\subseteq C_n.
\]

These \(D_n\) need not be decreasing, but any finite number still share a record. Indeed, for \(N\ge1\),

\[
C_N\setminus\bigcap_{n=1}^ND_n
\subseteq\bigcup_{n=1}^N(C_n\setminus D_n),
\]

Finite additivity gives

\[
\begin{aligned}
p_0\left(\bigcap_{n=1}^ND_n\right)
&\ge p_0(C_N)-\sum_{n=1}^Np_0(C_n\setminus D_n)\\
&>\delta-\sum_{n=1}^N\delta2^{-n-2}
>\frac{3\delta}{4}>0.
\end{aligned}
\]

All these remain finite operations in the algebra; we have not prematurely used an infinite-dimensional measure that has yet to be constructed.

We may therefore choose a record \(\omega^{(N)}\in\bigcap_{n=1}^ND_n\). We have not made it satisfy infinitely many requirements simultaneously; so far we have selected only one witness for each finite stage.

Arranging these witnesses in a sequence does not yet give them a common limit. A good subsequence for the first coordinate need not be good for the second. At each stage we retain the convergence already obtained and choose a further subsequence for the next coordinate. The diagonal then collects only promises already secured at every finite stage.

When \(N\ge j\), we have \(\omega^{(N)}\in D_j\), while \(m_j\ge j\). Thus the \(j\)th coordinate \(\omega_j^{(N)}\) lies in the projection of the compact set \(K_j\) onto coordinate \(j\). This is a compact subset of \(E_j\).

First select a subsequence converging in the first coordinate, then from it a subsequence converging in the second, and continue. Diagonal selection gives a single sequence of indices \(N_r\to\infty\) such that, for each fixed \(j\),

\[
\omega_j^{(N_r)}\longrightarrow\omega_j\in E_j.
\]

These coordinates form a complete record \(\omega=(\omega_1,\omega_2,\ldots)\).

For any fixed \(n\), once \(r\) is sufficiently large, \(N_r\ge n\), so the first \(m_n\) coordinates of \(\omega^{(N_r)}\) belong to \(K_n\). These finitely many coordinates converge jointly, and \(K_n\) is closed, so the first \(m_n\) coordinates of the limit still belong to \(K_n\). Hence

\[
\omega\in D_n\subseteq C_n
\quad\text{for every }n.
\]

This contradicts \(\bigcap_n C_n=\varnothing\).

Thus \(p_0\) on cylinders is continuous from above and is a premeasure. The extension theorem of Section 8.5 gives a unique probability \(P\) on

\[
\left(\prod_{j\ge1}E_j,\ \bigotimes_{j\ge1}\mathcal B(E_j)\right)
\]

satisfying

\[
P\circ\pi_{1:m}^{-1}=\mu_m
\quad\text{for every }m.
\]

This is the **Kolmogorov extension theorem for countably many Polish state spaces**.

Looking again at the heart of the proof, we see that we did not calculate ‘infinity’ itself. First, a summable error budget replaced every finite requirement with a sufficiently reliable compact requirement. Then diagonal selection compressed arbitrarily long finite witnesses into one common witness. This mechanism preserves exactly the continuity needed for countable additivity.

The preceding chapter's Borel–Cantelli argument also used summably small errors to control infinitely many times. There, however, a probability already existed and the task was to study long-term behavior of records. Here, the infinite-dimensional probability does not yet exist; the task is to prove that it can come into being. Similar error ideas occupy different places in the logical chain.

## 8.9 The 1933 Framework Accommodates More Than Independent Coin Tosses

We encountered Kolmogorov's probability axioms in Chapter 5. Only now does their connection with stochastic processes reveal its full force.

Kolmogorov's *Grundbegriffe der Wahrscheinlichkeitsrechnung* was published in 1933. Its table of contents moves from elementary probability into ‘infinite probability fields,’ then discusses random quantities and expectation. This arrangement makes the existence of infinite experiments a question internal to the foundations, rather than an incidental assumption made when using a particular process. [Publisher's record and table of contents for the original book](https://link.springer.com/book/10.1007/978-3-642-49888-6)

This does not mean that nobody studied infinite-dimensional objects before 1933. Daniell had already published *Integrals in An Infinite Number of Dimensions* in 1919. The title alone reminds us that extending finite-dimensional integration to infinitely many dimensions was an explicit question before probability's axioms were systematized. [Original journal publication record](https://www.jstor.org/stable/1967122)

Our construction uses modern measurable-space and topological language; we do not present the proof above as a verbatim reproduction of these historical sources. Historical approaches also started from other ideas, including integral functionals. Having developed measure and integration in Chapters 5 and 6, this book instead chooses to place cylinders, premeasures, and compactness along one main route.

Above all, notice that the extension theorem does not require independence.

It allows complex dependence within finite windows, requiring only that the windows be consistent with one another. Independence is merely one mechanism making consistency particularly easy to check. Markov transitions, Gaussian covariances, and many more complex structures can also supply consistent ledgers.

This is why the extension theorem reaches beyond any particular construction of infinite coin tossing: it separates designing a dependence structure from proving that the structure has a common realization, while connecting the two tasks.

### 8.9.1 What If a State Space Retains Only Its Measurable Structure?

The proof used completeness and compact sets. Sometimes, however, probability theory needs to know only which sets are measurable, without attaching a physical distance to every state.

A measurable space is called a **standard Borel space** if it admits a bijection to a Borel subset of a Polish space that is measurable in both directions. This bijection preserves the structure of events; it need not preserve any particular preassigned distance.

The countable extension theorem also applies to nonempty standard Borel state spaces. The reason can be made explicit: realize each \(E_j\) as a Borel subset \(B_j\) of a Polish space \(S_j\), push the finite-dimensional probabilities onto the corresponding \(S_j\), and first apply the version already proved. Every coordinate lies in \(B_j\) with probability 1. Since there are only countably many coordinates,

\[
P\left(\bigcap_{j\ge1}\{\pi_j\in B_j\}\right)=1.
\]

Restrict the probability to this measurable set of full probability, then transport it back to the original state spaces through the measurable correspondences to obtain the desired realization. The generated event structure and all cylinder probabilities are preserved.

The standard Borel assumption is not a qualifier that can quietly be dropped. These are the state spaces on which this chapter's general extension of consistent distributions is guaranteed. For arbitrary measurable spaces, we cannot simply copy the same existence conclusion. The proof's step of retaining finite-dimensional events within compact sets requires supporting structure.

## 8.10 Time Can Be Uncountable—Why Does Extension Still Encounter Only Countable Difficulties?

Brown's particles move at more than integer times. We want \(X_t\) to exist simultaneously for every \(t\ge0\).

Take a general index set \(T\) and a nonempty standard Borel space \((E_t,\mathcal E_t)\) at each time. For every finite \(J\subseteq T\), specify consistent probabilities \(\mu_J\).

Again use the full record space and the product \(\sigma\)-algebra:

\[
\Omega=\prod_{t\in T}E_t,
\qquad\mathcal F=\bigotimes_{t\in T}\mathcal E_t.
\]

On a finite-dimensional cylinder \(\pi_J^{-1}(B)\), define \(p_0=\mu_J(B)\). Well-definedness and finite additivity again follow by placing everything in a common finite window.

Checking continuity from above involves a sequence of cylinders \(C_n\downarrow\varnothing\). If the \(n\)th uses only the finite index set \(J_n\), then

\[
J=\bigcup_{n\ge1}J_n
\]

is at most countable.

The countable version has already supplied a probability on the record space over \(J\). Write \(C_n\) as the preimage of an event \(C_n'\) in that space. If \(\bigcap_n C_n'\) were nonempty, one of its records over \(J\) could be extended to a complete record over \(T\), contradicting \(\bigcap_n C_n=\varnothing\). Thus \(C_n'\downarrow\varnothing\), and the probability already constructed on countably many coordinates gives

\[
p_0(C_n)=P_J(C_n')\longrightarrow0.
\]

If \(J\) is finite, simply use the corresponding finite-dimensional measure; the conclusion is the same. To fill in unobserved coordinates, we fix a reference point in each nonempty state space, as in the usual construction of a product space.

The cylinder probability is therefore again a premeasure, and outer-measure extension completes the task once more.

We obtain the **Kolmogorov extension theorem for standard Borel spaces**: for any index set \(T\), a consistent family of probabilities \(\{\mu_J\}\) on finite products of nonempty standard Borel state spaces has a unique probability \(P\) on the product \(\sigma\)-algebra such that

\[
P\circ\pi_J^{-1}=\mu_J
\quad\text{for every finite }J\subseteq T.
\]

The coordinate functions \(X_t=\pi_t\) then form a stochastic process with the prescribed finite-dimensional distributions.

Moving from countable to uncountable indices involved no summation of uncountably many probabilities. The crucial point is precisely the opposite: **countable additivity still asks us to check only a sequence of events at a time, and a sequence of finite observations uses only countably many coordinates in total.**

This also explains why Section 8.9.1 first carried out the standard Borel reduction on countably many coordinates. We cannot intersect uncountably many probability-one events and simply claim that their intersection still has probability 1. The general-index conclusion follows from the cylinder argument and countable reduction just given, not from an unauthorized uncountable intersection.

## 8.11 Product Probability: How Does Independence Supply a Consistent Ledger?

Pick up the coin again. If the probability of heads on toss \(j\) is \(p_j\) and the tosses are required to be independent, prescribe for every finite prefix

\[
\mu_m(\{(a_1,\ldots,a_m)\})
=\prod_{j=1}^m p_j^{a_j}(1-p_j)^{1-a_j},
\qquad a_j\in\{0,1\},
\]

where each factor is interpreted as the probability of that toss taking the value 0 or 1. Interpret it this way even when a parameter is 0 or 1, without relying on the undefined \(0^0\).

Summing over the last entry yields the factor \(p_{m+1}+(1-p_{m+1})=1\), so these finite-dimensional probabilities are consistent. The extension theorem supplies a probability on full infinite records.

More generally, give each coordinate in a nonempty standard Borel space \(E_t\) a probability \(\nu_t\). Using Chapter 6's finite product measures, define

\[
\mu_J=\bigotimes_{t\in J}\nu_t
\quad\text{for every finite }J.
\]

Deleting a coordinate integrates out a factor of total mass 1, so consistency holds. Denote the extended probability by

\[
P=\bigotimes_{t\in T}\nu_t.
\]

This is the corresponding **product probability space**. This section completes the infinite construction within the standard Borel setting just established; it does not conflate general extension of consistent distributions with the specialized construction of independent products.

Its coordinate variables are mutually independent, since for any finite \(J\) and measurable \(A_t\subseteq E_t\),

\[
P\left(\bigcap_{t\in J}\{X_t\in A_t\}\right)
=\prod_{t\in J}\nu_t(A_t).
\]

Requiring infinitely many variables to be mutually independent means exactly that every finite subfamily satisfies this product formula. It does not mean taking an infinite or uncountable numerical product directly as the probability of an arbitrary event.

An independent sequence is finally more than an assumption written before a theorem. We now know that, at least for the real-valued, discrete-valued, and other principal cases used in this book, a probability space accommodating this assumption really exists.

### 8.11.1 If Every Individual Record Has Probability Zero, How Can Any Record Be Chosen?

In the full fair-coin product space, every specified record still has probability 0. In this respect, nothing has changed from the beginning.

The difference is that the full space is not a union of countably many records. Countable additivity does not require us to add uncountably many zeros to obtain the total mass.

The initial \(\Omega_{\mathrm{fin}}\) is now a measurable probability-zero subset of the full space. We can also see this by direct calculation: for fixed \(m\),

\[
\begin{aligned}
P(X_n=0\text{ for all }n\ge m)
&=\lim_{N\to\infty}
P(X_m=\cdots=X_N=0)\\
&=\lim_{N\to\infty}2^{-(N-m+1)}=0.
\end{aligned}
\]

Taking the countable union over \(m\) gives \(P(\Omega_{\mathrm{fin}})=0\).

It was not that every individual record in this set was forbidden to occur; the set was simply too small to carry all the probability by itself.

The preceding chapter's Bernoulli strong law finally has a common realization independent of digit expansions: on this product space, the finite independent-moment calculations hold, and Borel–Cantelli applies to frequency-deviation events, so the frequency of heads converges almost surely to \(1/2\). Section 8.2's countable expression has already guaranteed the measurability of this long-term event.

Digit expansions supplied a concrete model; the extension theorem shows that the finite rules themselves suffice to produce its canonical distribution. We have retained the same finite experiments without depending on a particularly clever encoding.

## 8.12 Dependent Experiments Can Also Have a Complete Future

In the real world, the next outcome often depends on what just happened.

Let the state space be a finite set \(E\), with initial probability \(\alpha\) and a transition matrix \(Q\):

\[
Q(i,j)\ge0,\qquad\sum_{j\in E}Q(i,j)=1.
\]

For a record segment \((i_0,\ldots,i_n)\), prescribe

\[
\mu_{0:n}(i_0,\ldots,i_n)
=\alpha(i_0)\prod_{k=1}^nQ(i_{k-1},i_k).
\]

This formula does more than list numbers. Successively summing over the last state, the row sums of 1 ensure both total mass 1 and recovery of the preceding segment's distribution when the last observation is removed.

To observe only selected times, take a sufficiently long prefix distribution and sum over the unobserved coordinates. Prefix consistency makes the result independent of the chosen prefix length. Thus all finite windows form a consistent family.

Kolmogorov extension then supplies a probability on \(E^{\{0,1,2,\ldots\}}\) under which every finite record follows the original transition formula. For histories of positive probability, division using finite-event conditional probabilities gives

\[
P(X_{n+1}=j\mid X_0=i_0,\ldots,X_n=i_n)=Q(i_n,j).
\]

Conditional values for zero-probability histories cannot be defined by this ratio. We will return to this in the systematic theory of conditional probabilities as random objects.

For example, take \(E=\{0,1\}\), use a uniform initial distribution, and set

\[
Q=\begin{pmatrix}0.9&0.1\\0.1&0.9\end{pmatrix}.
\]

The individual distribution at every time remains uniform, but consecutive outcomes have a strong tendency to persist:

\[
P(X_0=1,X_1=1)=0.45\ne0.25
=P(X_0=1)P(X_1=1).
\]

Independence has disappeared; consistency has not.

If we skip an intermediate time, the transition probability becomes

\[
Q^2(i,j)=\sum_{k\in E}Q(i,k)Q(k,j).
\]

Summing over all possible intermediate states makes a coarser time observation agree with a finer one. Later, the Chapman–Kolmogorov relation in continuous time will express this same requirement: inserting or removing an unobserved time must not change the probabilities of what is observed.

The extension theorem does not predict what will happen at every future step. It confirms that these conditional rules for the future can belong to one infinite random experiment.

## 8.13 Back to Brown's Particles: Can Gaussian Windows Form a Single Motion?

Return now to [Chapter 4](#chapter-4). There, square-root scaling of random walks led us to Gaussian distributions and suggested that the covariance between different times should be \(\min(s,t)\).

An elegant covariance formula, however, is not yet a proof that the entire process exists.

First construct each finite window explicitly. Write

\[
p_t(x)=\frac1{\sqrt{2\pi t}}
\exp\left(-\frac{x^2}{2t}\right),\qquad t>0.
\]

At times \(0<t_1<\cdots<t_n\), we want the position vector to have joint density

\[
f_{t_1,\ldots,t_n}(x_1,\ldots,x_n)
=p_{t_1}(x_1)
\prod_{j=2}^n p_{t_j-t_{j-1}}(x_j-x_{j-1}).
\]

This density comes from adding finitely many independent Gaussian increments. Its total integral is 1: integrate one position at a time, starting with the last, and each step removes a normalized Gaussian density. The coordinate at time 0 is fixed directly at 0; we do not treat \(p_0\) as an ordinary density.

Rather than immediately giving this a process name, we must check that these windows agree where they overlap.

Removing the last time is straightforward. Removing an intermediate time requires two consecutive increments to combine into a single increment across a longer interval. This calls for exactly the Gaussian convolution identity:

\[
\int_{\mathbb R}p_s(z-x)p_t(y-z)\,dz
=p_{s+t}(y-x),\qquad s,t>0.
\]

It follows directly by completing the square. The squares in the exponent satisfy

\[
\frac{(z-x)^2}{2s}+\frac{(y-z)^2}{2t}
=\frac{s+t}{2st}
\left(z-\frac{tx+sy}{s+t}\right)^2
+\frac{(y-x)^2}{2(s+t)}.
\]

The Gaussian integral of the first square contributes \(\sqrt{2\pi st/(s+t)}\). Multiplying by the constants in the two densities leaves exactly the constant for \(p_{s+t}(y-x)\). Removing the earliest positive time uses the same convolution. Repeated deletion gives the same formula for any smaller window.

These are therefore consistent finite-dimensional distributions. Each is more than plausible on its own: together they have passed the compatibility test between windows.

The Kolmogorov extension theorem now supplies a probability on

\[
\left(\mathbb R^{[0,\infty)},\quad
\bigotimes_{t\ge0}\mathcal B(\mathbb R)\right)
\]

The coordinate process \(B_t(\omega)=\omega(t)\) satisfies \(B_0=0\) almost surely, has the specified Gaussian finite-dimensional distributions, and has independent, stationary increments.

If \(s\le t\), write \(B_t=B_s+(B_t-B_s)\). Independence and zero means of the increments give

\[
\mathbb E[B_sB_t]
=\mathbb E[B_s^2]=s,
\qquad
\operatorname{Cov}(B_s,B_t)=\min(s,t).
\]

The covariance is now more than a formula we hope will hold. It belongs to one Gaussian process that already exists.

We still cannot say that Chapter 4's Brownian motion has been completely constructed.

Extension guarantees all time coordinates and their joint probabilities. Brownian motion also requires continuous sample paths, and we must now even reexamine whether ‘the function formed by all the coordinates is continuous’ is an event in this event system.

This apparently technical question reveals one of the most easily misunderstood boundaries of infinite products.

## 8.14 How Many Coordinates Can One Measurable Question See?

For countably many coordinates, the product structure is quite natural. If each \(E_j\) is Polish, with a corresponding complete metric \(d_j\), define

\[
d(x,y)=\sum_{j\ge1}2^{-j}\min\{1,d_j(x_j,y_j)\}.
\]

Convergence in this metric is exactly convergence in every coordinate: one direction follows because the sum controls each term; the other follows by first cutting off a small series tail and then controlling finitely many coordinates.

The metric is complete as well. A Cauchy sequence has a limit in each coordinate, and the same truncation estimate gives convergence of the entire record. From countable dense coordinate sets, choose freely in finitely many positions and fix reference points elsewhere; these choices give a countable dense set of records. Thus a countable product is again Polish.

Here the product \(\sigma\)-algebra equals the Borel \(\sigma\)-algebra of the product topology. Continuity of the coordinate projections gives inclusion of the former in the latter. Conversely, open rectangles using finitely many coordinates from countable bases form a countable base for the product, and every open set is a countable union of these basic open sets.

We cannot copy this argument unchanged for an uncountable index set. In particular, we cannot automatically identify the product \(\sigma\)-algebra with whatever function-space Borel structure we wish to use.

In fact, every event in the uncompleted product \(\sigma\)-algebra depends on at most countably many coordinates. More precisely, for every \(A\in\mathcal F\) there are an at most countable \(J\subseteq T\) and an event \(A_J\) in its product \(\sigma\)-algebra such that

\[
A=\pi_J^{-1}(A_J).
\]

The proof is straightforward. The class of sets with such a representation contains every finite-dimensional cylinder and is closed under complements. For countable unions, combine the at most countably many coordinates used by each event; they remain at most countable, and each event can be pulled back to this common space. Thus the class itself is a \(\sigma\)-algebra containing the cylinders.

A product-measurable event therefore permits infinitely many observations, but its generation cannot suddenly invoke uncountably many separate new coordinates.

This does not make the event system impoverished. Convergence, occurrence infinitely often, and sums of countable records are all deep questions it can express. But when a state is itself a function of continuous time, we must identify which questions are actually determined by countable observations.

Consider the subset \(\mathcal C\) of all continuous functions in \(\mathbb R^{[0,1]}\). It does not belong to the original product \(\sigma\)-algebra.

If it did, it would depend only on some at most countable set of times \(J\). The zero function belongs to \(\mathcal C\). Choose \(t_0\in(0,1)\setminus J\) and change its value only at \(t_0\) to 1. This new function agrees exactly with the zero function on \(J\) and would therefore also have to belong to \(\mathcal C\). Yet it is plainly discontinuous, a contradiction.

Between ‘giving all time coordinates one common probability’ and ‘giving continuous paths a probability,’ there remains the structure of events itself.

## 8.15 Every Finite Window Can Agree While Paths Differ Completely

This distinction does not occur only in the depths of an abstract space. A concrete example makes it visible.

Choose \(U\) uniformly on \([0,1]\) and, for each \(t\in[0,1]\), define

\[
Y_t=\mathbf1_{\{U=t\}}.
\]

For any fixed \(t\), the event \(U=t\) has probability 0, so \(Y_t=0\) almost surely. For any finite collection \(t_1,\ldots,t_n\), the probability that all these coordinates are 0 is still 1. Thus \(Y\) has exactly the same finite-dimensional distributions as the identically zero process.

Yet for every actual choice of \(U=u\), the function \(t\mapsto Y_t(u)\) takes the value 1 exactly at \(u\) and is 0 elsewhere. Every path is discontinuous, whereas every path of the identically zero process is continuous.

Where has the extension theorem's uniqueness been violated?

It has not. The two processes have the same distribution on the original product \(\sigma\)-algebra, while ‘the path is continuous’ is not a measurable event in that space. Uniqueness does not compare a question outside its domain.

Moreover, in ‘for every fixed \(t\), \(Y_t=0\) almost surely,’ the exceptional null set is \(\{U=t\}\), which varies with \(t\). The uncountable union of these null sets is exactly the entire sample space. Once again, rules for probabilities of countable collections cannot simply be extended to uncountable ones.

If two processes are almost surely equal at each fixed time, one is called a **modification** of the other. If there is a single exceptional null set outside which they agree at every time, they are called **indistinguishable**. The example above satisfies the first condition, but not the second.

When both processes have continuous paths, the situation changes. Take the probability-one equality events at rational times and intersect them countably to obtain a single set of full probability. On this set, equality at the dense rational times implies equality at every time by continuity. Thus two continuous modifications are indistinguishable.

Continuity does more than smooth a graph. It places uncountably many time constraints back under the control of observations at a countable dense set.

### 8.15.1 What Path Space Do We Ultimately Want to Inhabit?

Take the actual continuous-function space \(C([0,1])\) with the uniform metric

\[
\|f-g\|_\infty=\sup_{t\in[0,1]}|f(t)-g(t)|.
\]

This does not casually declare a subset of \(\mathbb R^{[0,1]}\) to have ‘probability 1.’ It explicitly chooses a new state space and its Borel event system.

Within this space, the Borel \(\sigma\)-algebra is indeed generated by evaluations at rational times.

One direction is immediate: every evaluation map \(f\mapsto f(q)\) is continuous and hence measurable. The other follows from the identity for continuous functions

\[
\|f-g\|_\infty
=\sup_{q\in\mathbb Q\cap[0,1]}|f(q)-g(q)|.
\]

For example, for \(r>0\), an open ball centered at a fixed \(g\) can be written as

\[
\{f:\|f-g\|_\infty<r\}
=\bigcup_{\substack{m\ge1\\1/m<r}}
\bigcap_{q\in\mathbb Q\cap[0,1]}
\{f:|f(q)-g(q)|\le r-1/m\}.
\]

These are all measurable sets generated by rational-time evaluations. Separability of \(C([0,1])\) then expresses every open set as a union of balls from a countable base, giving the reverse inclusion.

Thus, if a continuous process has already been established, its distribution as a \(C([0,1])\)-valued random element is uniquely determined by all finite-dimensional distributions at rational times. But ‘has already been established’ still calls for an existence argument.

For the Gaussian process above,

\[
\mathbb E|B_t-B_s|^4=3|t-s|^2.
\]

This follows from the fourth moment of a centered Gaussian variable. It gives strong probabilistic control of excessively large increments over short times. A continuous-modification theorem will turn precisely such moment estimates into existence of continuous paths. Its proof requires controlling all adjacent increments along increasingly fine time grids, naturally joining the proof route for continuous versions and Wiener measure retained in Chapter 4.

The fourth-moment constant can also be checked directly. For the standard Gaussian density \(\varphi\), we have \(\varphi'(x)=-x\varphi(x)\). One integration by parts gives \(\int_{\mathbb R}x^4\varphi(x)\,dx=3\int_{\mathbb R}x^2\varphi(x)\,dx=3\), with the boundary term vanishing by Gaussian decay. Scaling by the increment's standard deviation \(\sqrt{|t-s|}\) gives the displayed formula.

This chapter has established a common realization of consistent finite-dimensional probabilities and located precisely the gap between that realization and a construction of continuous paths. The continuous-modification theorem and its grid proof should be developed through the problem of path regularity. Possessing \(\min(s,t)\) does not allow us to conjure up a continuous path without proof.

## 8.16 What Is Unique Is a Distribution, Not the Material of a Universe

One final question is easily confused.

If the extension theorem says the probability is unique, must every space realizing these experiments have the form \(\prod_tE_t\)?

No. Digit expansions can realize independent coins on an interval of real numbers; another construction can begin with other sources of randomness. Different sample points may even represent the same coordinate record.

Suppose that on a probability space \((\Omega',\mathcal F',P')\) we already have measurable random variables \(X_t'\) whose finite-dimensional distributions are \(\mu_J\). Send each sample point to the full record it generates:

\[
\Phi(\omega')=(X_t'(\omega'))_{t\in T}.
\]

The map \(\Phi\) is measurable for the product \(\sigma\)-algebra, because the preimage of every finite-coordinate event is measurable in the original space. Thus \(P'\circ\Phi^{-1}\) is a probability on the record space with all the specified finite-dimensional distributions. By uniqueness, it equals the \(P\) we constructed.

This is the meaning of the canonical record space: whatever material underlies the experiment, the same finite joint rules tell the same story within the product event system.

At the same time, we must state the scope of uniqueness clearly. It holds on the \(\sigma\)-algebra generated by cylinders; it does not automatically give probabilities to arbitrary subsets of the record space. Completion can add all subsets of known null events and assign their probabilities by inclusion, but this is an explicit additional step. It neither makes every subset measurable nor resolves all uncountable path conditions at once. The rigorous construction of that extra step for an arbitrary measure is in the [completion companion](../foundations/t-measure.md#t-measure-completion).

Coupling in Chapter 7 offers a reminder from another direction: specifying each variable's individual distribution does not specify every finite-dimensional joint distribution. Different common realizations can still be chosen. Uniqueness of extension and freedom of coupling do not conflict; they fix different amounts of information.

Once the finite-dimensional joint laws are specified, consistency joins the windows, extension carries probability beyond finite observation, and uniqueness makes different constructions yield the same canonical distribution. Further control of paths, conditional information, or limits still requires building the corresponding structures.

This does not diminish the existence theorem. It finally tells us exactly what each promise of existence has accomplished.

## Closing Reflections on Chapter 8: Infinity Is Not the Last Toss

Return once more to the coin on the table.

No ‘last toss’ awaits completion. Every record actually written down is finite, as is every specified observation window.

Yet a mathematics of laws of large numbers, infinitely many exceptions, and random paths cannot retain only finite stages erected afresh for each occasion. It needs a common world in which all these windows can be read from the same record.

The world of eventually all-zero records at the beginning allowed every finite record, yet could not carry the probability those records required. It showed us that the question is not whether a record is long enough, but whether finite rules still have somewhere to settle at infinite limits.

Measure extension supplied a route from existing events to new ones; compact approximation retained probability mass that had not yet found its place; diagonal selection turned arbitrarily long finite requirements into one complete record. Finally, consistent finite-dimensional distributions held together on a countably additive probability space.

The preceding chapter's law of large numbers therefore no longer hangs on the phrase ‘suppose an infinite independent sequence exists.’ We have constructed such a sequence and know why its long-run frequency is a measurable event.

Brown's particles push the question further. We can make Gaussian positions and increments at all times exist together, but we still have to connect them into genuinely continuous paths. Finite windows, product events, and path spaces answer questions at different levels; distinguishing them makes their eventual unification possible.

We will also encounter another difficulty: although the experiments now coexist, observers usually know only part of them. After seeing some of the past, how do future probabilities change? If we retain only certain information, how should expectation be recalculated?

These questions bring probability kernels, conditional distributions, and conditional expectation before us. They do not overturn the world just constructed; they explain how information organizes randomness within it.

Path continuity, weak convergence, and deeper theories of random motion now also have a common foundation on which to grow.

Infinity is no longer merely a finite experiment prolonged far enough. It is a mathematical object to be constructed, measured, and questioned carefully.

## History and Further Reading

A. Kolmogoroff, *Grundbegriffe der Wahrscheinlichkeitsrechnung*, Springer, 1933. [Publisher's record and original table of contents](https://link.springer.com/book/10.1007/978-3-642-49888-6). The release date of a modern online edition must not be confused with the original book's year. This chapter uses a modern Polish/standard Borel formulation and does not claim to reproduce all of the original assumptions, language, or proofs.

P. J. Daniell, *Integrals in An Infinite Number of Dimensions*, *Annals of Mathematics* 20(4) (1919), 281–288. [Original journal archive and DOI](https://www.jstor.org/stable/1967122). The original publication record supplies a historical entry point to the problem of infinite-dimensional integration; this chapter's cylinder proof is not attributed to that paper.

Olav Kallenberg's *Foundations of Modern Probability*, third edition (2021), remains the reference for the theoretical coverage of modern probability throughout this book. [Publisher's bibliographic information](https://link.springer.com/book/10.1007/978-3-030-61871-1). This chapter organizes its construction around the preceding questions of measure, integration, convergence, and Brownian paths rather than following the reference book's chapter narrative.

This chapter develops the undersized coin space, the premeasure continuity test, compact inner regularity, the diagonal construction, and path counterexamples in modern language. Historical sources trace the development of the questions; the proofs here bear their own mathematical responsibility through explicitly stated assumptions and arguments.
