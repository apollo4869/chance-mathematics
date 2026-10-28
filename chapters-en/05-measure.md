# The Mathematics of Chance
Volume II · Probability in an Infinite World

# Chapter 5: The Price of an Infinite World—Why Does Probability Need Measure Theory?

When people tried to measure every set, they eventually discovered that not every set can possess the kind of size we would like it to have.

In the first four chapters, we traveled a long road.

At the very beginning, we had only an unfinished game of chance.

To divide the stakes fairly, we began calculating futures that had not yet happened, gradually uncovering the ideas of probability, independence, and expectation.

We then tried to learn unknown probabilities through observation, and discovered that repeated experiments can produce stable statistical laws.

Next, the normal distribution emerged from the binomial formula and the limits of sums of independent random variables.

Finally, following discrete random walks, we identified the structure that continuous Brownian motion should have, and encountered questions about paths that remained to be resolved.

Randomness now lives not only in the finitely many outcomes of a game, but also among real numbers, continuous functions, and even in infinite-dimensional spaces.

Yet there is one question we have never seriously answered.

When we write

\[
P(A)
\]

what, exactly, does this symbol mean?

For a fair die, we can say:

\[
P(A)=\frac{|A|}{6}.
\]

There are only six equally likely outcomes.

For Brownian motion, however, we can ask about an event such as

\[
A=
\left\{
\omega:
\sup_{0\le t\le1}B_t(\omega)>1
\right\}.
\]

Here \(\omega\) is no longer simply a number.

It represents one possible realization of the entire random motion.

And \(A\) contains all random paths that have crossed height 1 at some point.

Such a set is neither finite nor something we can measure by simple counting.

Yet we still want to calculate its probability.

A seemingly natural idea therefore suggests itself:

> Since probability measures the size of a set, why not first build a mathematical theory capable of measuring the size of any set, and then apply it to random phenomena?

This looks like a purely technical problem.

As we shall discover, however, it conceals a mathematical impossibility.

---

## 5.1 A Random Experiment That Seems as Simple as Possible

Suppose we choose a real number at random from the interval \([0,1]\).

To avoid using probabilistic language before defining it, let us provisionally call this experiment a “uniform choice.”

By this we mean that the chance of the number falling in an interval should be proportional to that interval’s length.

For example:

\[
P\left(X\in\left[0,\frac12\right]\right)=\frac12,
\]

\[
P\left(X\in\left[\frac14,\frac34\right]\right)=\frac12.
\]

More generally, for

\[
0\le a<b\le1,
\]

we want

\[
\boxed{P(X\in[a,b])=b-a.}
\]

Whether the endpoints are included should not affect the result we seek.

This requirement seems entirely reasonable.

After all, “uniform” means that an interval’s position should not affect its chance of being selected; only the length it occupies should matter.

But an interval is only one particular kind of set of real numbers.

We might also ask:

What is the probability that the number belongs to the rationals?

What is the probability that it belongs to the Cantor set?

And what is the probability that it belongs to a very complicated set that is neither an interval nor a finite union of intervals?

If probability theory is to handle all these questions, we must extend our definition from intervals to more general sets.

We therefore try to find a function

\[
m:\mathcal P(\mathbb R)\longrightarrow[0,\infty],
\]

where \(\mathcal P(\mathbb R)\) denotes the power set consisting of all subsets of the real numbers.

We would like it to have the following properties:

First, intervals should have their usual lengths:

\[
m([a,b])=b-a.
\]

Second, translation must not change a set’s size:

\[
m(A+x)=m(A),
\]

where

\[
A+x=\{a+x:a\in A\}.
\]

Finally, if a collection of sets does not overlap, its combined size should equal the sum of the sizes of its parts.

We would even like this to hold for infinitely many disjoint sets:

\[
\boxed{
m\left(\bigcup_{n=1}^{\infty}A_n\right)
=
\sum_{n=1}^{\infty}m(A_n).
}
\]

This is countable additivity.

All three requirements seem perfectly natural.

But can they really hold simultaneously?

Before answering, let us see how infinite sets changed our understanding of “size.”

## 5.2 Why Can the Number of Elements No Longer Represent a Set’s Size?

For a finite set, the most natural notion of size is its number of elements.

For example, let

\[
A=\{1,2,3\},\qquad B=\{1,2,3,4,5\}.
\]

We plainly regard \(B\) as larger than \(A\).

Indeed,

\[
|A|=3,\qquad |B|=5.
\]

But with infinite sets, things begin to look strange.

For example, the natural numbers

\[
\mathbb N=\{1,2,3,\ldots\}
\]

and the even numbers

\[
2\mathbb N=\{2,4,6,\ldots\}
\]

are related by a bijection:

\[
n\longmapsto2n.
\]

They therefore have the same cardinality.

Although the even numbers are only part of the natural numbers, Cantor’s theory of cardinality still regards them as equally large.

For infinite sets, there is no contradiction here.

It simply shows that our intuition about counting finite sets no longer describes infinite sets completely.

Now consider the continuous intervals that really interest us.

The map

\[
f:[0,1]\longrightarrow[0,1/2],
\qquad
f(x)=\frac x2
\]

is a bijection.

Thus

\[
\left|[0,1]\right|
=
\left|[0,1/2]\right|.
\]

But in terms of ordinary length,

\[
m([0,1])=1,
\]

whereas

\[
m([0,1/2])=\frac12.
\]

Again, there is no contradiction.

Cardinality and length are two different mathematical concepts.

The real question is:

**Can we create a new notion of size for infinite sets that extends interval length while retaining the reasonable additive properties of finite counting?**

### 5.2.1 A Dense Set Can Have Length Zero

Consider

\[
A=\mathbb Q\cap[0,1].
\]

The rational numbers are dense in \([0,1]\).

This means that every nonempty open interval contained in \([0,1]\), however small, contains a rational number.

Geometrically, this set seems to be “everywhere” throughout the interval.

Yet if we want each individual point to have length zero,

\[
m(\{x\})=0,
\]

and if \(m\) is countably additive, then because the rationals are countable we can list them:

\[
A=\{q_1,q_2,\ldots\}.
\]

Hence

\[
\begin{aligned}
m(A)
&=m\left(\bigcup_{n=1}^{\infty}\{q_n\}\right)\\
&=\sum_{n=1}^{\infty}m(\{q_n\})\\
&=0.
\end{aligned}
\]

Therefore

\[
\boxed{m(\mathbb Q\cap[0,1])=0.}
\]

Conversely,

\[
m\bigl([0,1]\setminus\mathbb Q\bigr)=1.
\]

In the uniform probability model we hope to construct, this means:

\[
\boxed{P(X\text{ is rational})=0.}
\]

while

\[
\boxed{P(X\text{ is irrational})=1.}
\]

This is already very different from probabilistic intuition in a finite space.

In a finite space of equally likely outcomes, a nonempty event always has positive probability.

In a continuous space, however, an event can contain infinitely many outcomes and still have probability zero.

An event can even be topologically dense while having measure zero.

Here, for the first time, we encounter three different kinds of “size”:

- Cardinality: how many elements does a set contain?
- Topological properties: how is the set distributed through the space?
- Measure: how much measurable size does the set occupy?

These are different questions.

And it is the third notion that probability theory will need.

So far, though, our difficulties still seem merely technical.

Strange as infinite sets may be, we can still assign reasonable sizes to the rationals, the irrationals, intervals, and similar sets.

The real crisis has yet to arrive.

---

## 5.3 An Attempt That Fails: Can We Really Measure Every Set?

![Historical illustration from the source manuscript](../assets/images/04-01.img)

[Original image source](https://www.futura-sciences.com/sciences/personnalites/mathematiques-emile-borel-319/?utm_source=chatgpt.com)

**Émile Borel（1871—1956）**

A French mathematician. In 1898, he studied the sets and measure structures obtainable from intervals through countable set operations.

![Historical illustration from the source manuscript](../assets/images/05-01.img)

[Original image source](https://snl.no/Henri_L%C3%A9on_Lebesgue?utm_source=chatgpt.com)

**Henri Lebesgue（1875—1941）**

A French mathematician. In his 1902 doctoral dissertation, he developed a new theory of length, area, and integration, enabling systematic study of sets and functions far more complicated than intervals.

At the turn of the twentieth century, Cantor’s set theory, Borel’s study of sets, and Lebesgue’s theories of measure and integration allowed mathematicians to handle increasingly complicated infinite sets.

Yet one very natural question remained:

If we can already measure so many sets, why not simply measure them all?

In 1905, the Italian mathematician Giuseppe Vitali gave a startling answer.

**Under the usual axiom of choice, it is impossible to assign all subsets of the real numbers a measure that is translation invariant, countably additive, and agrees with interval length.**

This was not because mathematicians had yet to find a suitable construction.

It was because such a measure cannot exist at all.〔[47](#ref-turn701804search1), [48](#ref-turn701804search0), [49](#ref-turn701804search4)〕

Let us prove this for ourselves.

### 5.3.1 First, Divide the Real Numbers into Equivalence Classes

On the interval \([0,1]\), define the relation

\[
x\sim y
\quad\Longleftrightarrow\quad
x-y\in\mathbb Q.
\]

In other words, two real numbers are equivalent when their difference is rational.

This relation does satisfy the three requirements for an equivalence relation.

Reflexivity:

\[
x-x=0\in\mathbb Q.
\]

Symmetry:

\[
x-y\in\mathbb Q
\implies y-x\in\mathbb Q.
\]

Transitivity:

\[
x-y\in\mathbb Q,\quad y-z\in\mathbb Q
\implies x-z\in\mathbb Q.
\]

Thus the relation partitions \([0,1]\) into disjoint equivalence classes.

Each equivalence class is countable, since it is contained in a set of the form

\[
x+\mathbb Q
\]

for some real number x.

But the entire interval \([0,1]\) is uncountable.

There must therefore be uncountably many equivalence classes.

So far, everything seems in order.

Next, we do something that appears entirely harmless:

**Choose exactly one representative from each equivalence class.**

Write \(V\) for the set of these representatives.

Then

\[
V\subseteq[0,1],
\]

and \(V\) meets each equivalence class exactly once.

This is a Vitali set.

Here we need the axiom of choice: we simultaneously choose one representative from each of uncountably many equivalence classes.

We do not give an explicit formula for these representatives; the set-theoretic principle of choice asserts that such a set exists.

### 5.3.2 Translate This Set Infinitely Many Times

Now consider the set of rational numbers

\[
Q_0=\mathbb Q\cap[-1,1].
\]

For each \(q\in Q_0\), define the translate

\[
V_q=V+q.
\]

We first prove that

for distinct \(q,r\in Q_0\),

\[
V_q\cap V_r=\varnothing.
\]

Suppose otherwise.

Then there exist \(v,w\in V\) such that

\[
v+q=w+r.
\]

Hence

\[
v-w=r-q\in\mathbb Q.
\]

so

\[
v\sim w.
\]

But \(V\) has only one representative from each equivalence class, so

\[
v=w.
\]

Substituting this into the original equality gives

\[
q=r,
\]

contrary to our assumption.

The translated sets are therefore pairwise disjoint.

For the second step, we prove:

\[
\boxed{
[0,1]\subseteq
\bigcup_{q\in Q_0}(V+q).
}
\]

Take any \(x\in[0,1]\).

Since \(V\) contains the representative of the equivalence class containing \(x\), there exists \(v\in V\) such that

\[
x-v\in\mathbb Q.
\]

Moreover, because \(x,v\in[0,1]\),

\[
-1\le x-v\le1.
\]

Thus, setting

\[
q=x-v\in Q_0,
\]

gives

\[
x=v+q\in V+q.
\]

The interval \([0,1]\) is indeed covered by these translates.

On the other hand, the interval

\[
[-1,2]
\]

contains all these sets.

We therefore obtain:

\[
\boxed{
[0,1]
\subseteq
\bigcup_{q\in Q_0}(V+q)
\subseteq[-1,2].
}
\]

Up to this point, we have used no assumptions about measure.

The entire construction comes from set theory.

### 5.3.3 Now Let Measure Decide the Size of the Set

Suppose we could indeed construct a measure \(m\) on all subsets of the real numbers satisfying the three requirements stated at the beginning of the chapter.

In particular, it is translation invariant:

\[
m(V+q)=m(V).
\]

Let

\[
c=m(V).
\]

Since \(V\subseteq[0,1]\), monotonicity gives

\[
0\le c\le1.
\]

Because \(Q_0\) is countably infinite and the sets \(V+q\) are pairwise disjoint, countable additivity gives

\[
\begin{aligned}
m\left(\bigcup_{q\in Q_0}(V+q)\right)
&=\sum_{q\in Q_0}m(V+q)\\
&=\sum_{q\in Q_0}c.
\end{aligned}
\]

There are now only two possibilities.

**Case one: \(c=0\).**

Then

\[
m\left(\bigcup_{q\in Q_0}(V+q)\right)=0.
\]

But this union contains \([0,1]\), so its measure is at least 1.

Thus

\[
1\le0.
\]

A contradiction.

**Case two: \(c>0\).**

Since we add the same positive number countably infinitely many times,

\[
\sum_{q\in Q_0}c=\infty.
\]

Therefore

\[
m\left(\bigcup_{q\in Q_0}(V+q)\right)=\infty.
\]

But this union is also contained in \([-1,2]\).

By interval length,

\[
m([-1,2])=3.
\]

so its measure can be at most 3.

Thus

\[
\infty\le3.
\]

Again, a contradiction.

Whether \(m(V)=0\) or \(m(V)>0\), we reach a contradiction.

We have therefore proved:

\[
\boxed{
\begin{gathered}
\text{There is no measure defined on }\mathcal P(\mathbb R)\text{ that is}\\
\text{translation invariant、countably additive、}\\
\text{and agrees with interval length。}
\end{gathered}
}
\]

This is the core of the Vitali nonmeasurable-set argument.〔[50](#ref-turn701804search35), [51](#ref-turn701804search39)〕

### 5.3.4 Where, Exactly, Did We Fail?

What makes this proof especially striking is that it involves no particularly complicated calculation.

We performed only three operations:

Choosing representatives.

Translating sets.

Adding the sizes of disjoint sets.

Each step seems natural.

Together, however, they produce an unavoidable contradiction.

This means that some of our original wishes cannot all be fulfilled.

If we insist on interval length, translation invariance, and countable additivity, we must surrender one requirement:

**We must not require every subset of the real numbers to be assigned a measure.**

Of course, we must understand this conclusion precisely.

It does not mean that no probability space can assign probabilities to all subsets. For example, a Dirac measure concentrating all probability at a single point can perfectly well be defined on \(\mathcal P(\mathbb R)\).

What is impossible is to define on all subsets the particular kind of measure we seek, compatible with uniform length.

This distinction matters, because it tells us:

**Measurability is not an absolute property of a set, independent of a system of measure. It is closely tied to the measure structure we choose.**

We now face a new question.

If we cannot measure every set, which sets should we measure?

This leads us to \(\sigma\)-algebras.

---

## 5.4 Why Did Mathematicians Need to Invent \(\sigma\)-Algebras?

Suppose we decide to abandon the demand to measure every subset.

We select only some sets and assign probabilities to them.

Collect these sets that we permit ourselves to measure into a family, denoted by

\[
\mathcal F\subseteq\mathcal P(\Omega).
\]

What properties should \(\mathcal F\) have?

Let us not rush to a definition.

Instead, reconsider the most basic logical relationships among probabilistic events.

If an event \(A\) can be assigned a probability, then “\(A\) does not occur” should also be an event we can discuss.

Thus

\[
A\in\mathcal F
\implies A^c\in\mathcal F.
\]

If two events \(A,B\) can both be measured, then “\(A\) or \(B\) occurs” should also be measurable.

We therefore want

\[
A,B\in\mathcal F
\implies A\cup B\in\mathcal F.
\]

But in infinite random experiments, taking the union of just two events is insufficient.

For example:

Will a random walk return to the origin at some future time?

Let

\[
A_n=\{S_n=0\}.
\]

Then “returning to the origin at least once” is

\[
\bigcup_{n=1}^{\infty}A_n.
\]

while “returning to the origin infinitely often” is

\[
\bigcap_{m=1}^{\infty}
\bigcup_{n=m}^{\infty}A_n.
\]

Both events involve infinitely many set operations.

If our system of measurable events cannot handle them, studying the long-term behavior of random processes becomes difficult.

It is therefore natural to ask:

Whenever each \(A_n\) is a measurable event,

\[
\bigcup_{n=1}^{\infty}A_n
\]

should also be measurable.

This gives us the definition of a \(\sigma\)-algebra.

### Definition 5.1: \(\sigma\)-Algebra

Let \(\Omega\) be a nonempty set.

If a family of sets

\[
\mathcal F\subseteq\mathcal P(\Omega)
\]

satisfies:

1. \(\Omega\in\mathcal F\)；
2. If \(A\in\mathcal F\), then \(A^c\in\mathcal F\);
3. If \(A_1,A_2,\ldots\in\mathcal F\), then
\[
\bigcup_{n=1}^{\infty}A_n\in\mathcal F,
\]

then \(\mathcal F\) is called, on \(\Omega\), a \(\sigma\)-algebra.

Its elements are called measurable sets.

That is the definition.

But we should now understand why it takes this form.

These are not three unrelated formal requirements.

They correspond, respectively, to:

The certainty that the experiment has some outcome.

The negation of an event.

Logical combinations of countably many events.

Furthermore, De Morgan’s law,

\[
\left(\bigcup_{n=1}^{\infty}A_n\right)^c
=
\bigcap_{n=1}^{\infty}A_n^c,
\]

immediately gives

\[
A_n\in\mathcal F\ (\forall n)
\implies
\bigcap_{n=1}^{\infty}A_n\in\mathcal F.
\]

A \(\sigma\)-algebra can therefore handle both countable unions and countable intersections.

### 5.4.1 Why Countably Many Rather Than Arbitrarily Many?

This question deserves consideration in its own right.

If finite unions are insufficient, why not simply require closure under arbitrary unions?

Suppose \(\mathcal F\) contains every singleton on the real line:

\[
\{x\}\in\mathcal F,
\qquad x\in\mathbb R.
\]

If \(\mathcal F\) is closed under arbitrary unions, then every set \(A\subseteq\mathbb R\) satisfies

\[
A=\bigcup_{x\in A}\{x\}\in\mathcal F.
\]

Hence

\[
\mathcal F=\mathcal P(\mathbb R).
\]

We have returned to the starting point that failed in Vitali’s proof.

The distinction between countable and arbitrary unions is therefore no arbitrary technical restriction invented by mathematicians.

It allows us to retain powerful limiting operations without including every subset in our measurable structure.

This is especially important in probability theory.

Random sequences indexed by the natural numbers, limiting unions and intersections, and many events concerning paths of stochastic processes can all be expressed through countably many operations.

An arbitrary uncountable union, however, need not be measurable.

This will influence our methods when we later handle continuous-time stochastic processes.

---

## 5.5 Is Having More Measurable Events Always Better?

Now imagine two \(\sigma\)-algebras

\[
\mathcal F_1\subseteq\mathcal F_2.
\]

If we regard them as collections of distinguishable events, \(\mathcal F_2\) allows us to distinguish more possibilities.

This suggests an interpretation of great importance in modern probability:

**A \(\sigma\)-algebra can be viewed as a structure of information.**

For example, before tossing a coin, we consider only the certain event and the impossible event:

\[
\mathcal F_0=\{\varnothing,\Omega\}.
\]

After the toss, if the outcome space is

\[
\Omega=\{H,T\},
\]

we can distinguish heads from tails:

\[
\mathcal F_1=\mathcal P(\Omega).
\]

Thus

\[
\mathcal F_0\subseteq\mathcal F_1.
\]

The latter contains more distinguishable events.

Of course, “measurable events” cannot in every setting be directly identified with “what an observer actually knows.” This is a mathematical interpretation, which we will later make precise through conditional expectation and filtrations.

Yet it already anticipates an important idea:

When studying a stochastic process, we must ask not only what happened, but also **how much information about the random world we have acquired at a given time**.

This gives rise to increasing families of \(\sigma\)-algebras:

\[
\mathcal F_s\subseteq\mathcal F_t,
\qquad s\le t.
\]

These will form the foundation of martingale theory.

The abstract families of sets introduced here will therefore do more than ensure that probability is rigorously defined: they will directly describe how information grows over time.

This will become especially important in the chapter on conditional expectation.

---

## 5.6 Borel Sets: How Can the Simplest Sets Generate a Rich Enough Measurable World?

We can now finally answer:

If we cannot measure every subset of the real numbers, which sets should we at least measure?

Intervals remain the most natural starting point.

They have clear geometric lengths.

We therefore first require every open interval to be measurable.

Then, as discussed in the previous section, whenever sets are measurable, their complements, countable unions, and countable intersections should also be measurable.

A construction problem emerges:

**Starting from all open intervals and repeatedly performing these permitted set operations, what can we obtain?**

To express this rigorously, first introduce the notion of generation.

Given a family of sets \(\mathcal C\subseteq\mathcal P(\Omega)\), define

\[
\boxed{
\sigma(\mathcal C)
=
\bigcap\left\{
\mathcal F:
\mathcal F\text{ is a }\sigma\text{-algebra},
\ \mathcal C\subseteq\mathcal F
\right\}.
}
\]

Because an arbitrary intersection of \(\sigma\)-algebras remains a \(\sigma\)-algebra, this definition does indeed produce, among the families containing \(\mathcal C\), the smallest \(\sigma\)-algebra.

We say that \(\mathcal C\) generates this \(\sigma\)-algebra.

Now let \(\mathcal O\) be the family of all open sets in \(\mathbb R\).

Define

\[
\boxed{
\mathcal B(\mathbb R)=\sigma(\mathcal O).
}
\]

This is the Borel \(\sigma\)-algebra on the real line.

It contains open sets, closed sets, and every set obtainable through countable unions, intersections, and complementation.

One very useful fact is:

\[
\boxed{
\mathcal B(\mathbb R)
=
\sigma\bigl(\{(a,b):a,b\in\mathbb Q,\ a<b\}\bigr).
}
\]

Why are intervals with rational endpoints sufficient?

Because any open set \(U\subseteq\mathbb R\) can be written as

\[
U=
\bigcup_{\substack{a,b\in\mathbb Q\\(a,b)\subseteq U}}
(a,b).
\]

and there are only countably many intervals with rational endpoints.

Thus, however complicated an open set may be, we can reconstruct it from countably many simple intervals.

This connects with the idea of countability that we have repeatedly encountered.

**Although a continuous space contains uncountably many points, many important topological and measure structures can still be generated by countably many basic objects.**

This property will repeatedly play a role in separable metric spaces, the measurability of stochastic processes, and the weak convergence of probability measures.

For now, however, we have answered only “which sets are permitted to be measured.”

We have not yet answered:

What should their measures actually be?

We need to construct an actual function

\[
m:\mathcal B(\mathbb R)\to[0,\infty].
\]

which must satisfy our original requirements of interval length and countable additivity.

That is our next step.

---

## 5.7 Lebesgue’s Idea: Can We Measure a Set by Covering It from Outside?

Imagine a set \(A\subseteq\mathbb R\).

It may be so complicated that it cannot be directly expressed as a few intervals.

But we can try covering it with a sequence of open intervals.

Suppose

\[
A\subseteq\bigcup_{n=1}^{\infty}I_n,
\]

where each \(I_n\) is an open interval.

Since the total length of the intervals used in the cover is

\[
\sum_{n=1}^{\infty}|I_n|,
\]

the length of \(A\) itself should be no greater than this number.

Different covers, however, can have entirely different total lengths.

Naturally, we want the most economical cover.

We therefore define

\[
\boxed{
m^*(A)
=
\inf\left\{
\sum_{n=1}^{\infty}|I_n|:
A\subseteq\bigcup_{n=1}^{\infty}I_n,
\ I_n\text{ is an open interval}
\right\}.
}
\]

Here \(m^*\) is called Lebesgue outer measure.

This is a beautiful construction.

We no longer try to measure an arbitrarily complicated set directly.

Instead, we approximate it from outside using intervals we already know how to measure.

For intervals, this construction gives the usual length.

For example,

\[
m^*([a,b])=b-a.
\]

The upper bound follows by covering the interval with an open interval whose length is arbitrarily close to \(b-a\).

The lower bound follows from compactness: every open-interval cover of \([a,b]\) has a finite subcover, and the total length of finitely many intervals covering the entire interval cannot be less than \(b-a\).

This step incorporates ordinary geometric length into a more general notion of set size.

### 5.7.1 What Properties Does Outer Measure Have?

First,

\[
m^*(\varnothing)=0.
\]

Second, if

\[
A\subseteq B,
\]

then any family of open intervals covering \(B\) also covers \(A\).

Therefore

\[
\boxed{m^*(A)\le m^*(B).}
\]

In other words, outer measure is monotone.

Now consider any sequence of sets

\[
A_1,A_2,\ldots.
\]

For any \(\varepsilon>0\), we can choose for each \(A_k\) an open-interval cover whose total length does not exceed

\[
m^*(A_k)+\frac{\varepsilon}{2^k},
\]

Here we first suppose that the relevant outer measures are finite; if any term is infinite, the desired inequality holds immediately.

Combining all these covers gives an open-interval cover of \(\bigcup_kA_k\).

Hence

\[
m^*\left(\bigcup_{k=1}^{\infty}A_k\right)
\le
\sum_{k=1}^{\infty}m^*(A_k)+\varepsilon.
\]

Letting \(\varepsilon\downarrow0\) gives

\[
\boxed{
m^*\left(\bigcup_{k=1}^{\infty}A_k\right)
\le
\sum_{k=1}^{\infty}m^*(A_k).
}
\]

This is the upper bound for countable additivity, or **countable subadditivity**.

Notice that we obtain an inequality, not an equality.

Outer measure therefore already assigns some nonnegative generalized size to **every subset of the real numbers**.

But it does not guarantee countable additivity for all disjoint sets.

This is unsurprising.

Vitali’s theorem has already told us that if outer measure preserves translation invariance and interval length, it cannot be countably additive on all subsets.

The problem has therefore changed.

We already have an outer measure defined on every subset.

Now we must find the sets on which outer measure behaves like a genuine measure.

This gives another natural origin for measurability.

## 5.8 Carathéodory: Which Sets Should We Permit Ourselves to Measure?

> Editorial supplement: Appendix A gives expanded proofs of closure under finite unions, closure under countable unions, and countable additivity; Appendix B treats the cut points in open covers.

Consider an arbitrary set \(A\subseteq\mathbb R\).

Suppose we divide another set \(E\) into two parts:

\[
E\cap A
\]

and

\[
E\setminus A.
\]

These are plainly disjoint, and

\[
E=(E\cap A)\cup(E\setminus A).
\]

By subadditivity of outer measure, we always have

\[
m^*(E)
\le
m^*(E\cap A)+m^*(E\setminus A).
\]

But if \(A\) is truly compatible with the notion of length, we seem entitled to expect more:

Dividing any set \(E\) according to membership in \(A\) should not change the total outer measure out of nowhere.

In other words, we want

\[
m^*(E)
=
m^*(E\cap A)+m^*(E\setminus A).
\]

Notice a crucial detail here.

**We do not ask merely that this equality hold when \(E=\mathbb R\) or \(E=A\); we require it for every set \(E\).**

This is the idea behind Carathéodory’s criterion for measurability.

### Definition 5.2: Carathéodory Measurable Set

Given the outer measure \(m^*\), if a set \(A\subseteq\mathbb R\) satisfies:

For every \(E\subseteq\mathbb R\),

\[
\boxed{
m^*(E)
=
m^*(E\cap A)+m^*(E\setminus A),
}
\]

then \(A\) is called Lebesgue measurable.

Denote the family of all such sets by

\[
\mathcal L.
\]

At first sight, this definition looks more abstract than the definition of a \(\sigma\)-algebra.

But we already understand where it comes from.

Outer measure can measure any set, yet may fail to be additive.

We therefore seek sets that preserve the desired additive property whenever they are used to cut any other set.

In the early twentieth century, Carathéodory developed this idea into an important construction tool in the general theory of outer measure.〔[52](#ref-turn701804search6), [53](#ref-turn701804search37)〕

Now let us see where its real power lies.

### 5.8.1 Why Do These Measurable Sets Automatically Form a \(\sigma\)-Algebra?

We begin with closure properties.

Since the definition is entirely symmetric in \(A\) and \(A^c\),

\[
A\in\mathcal L
\implies A^c\in\mathcal L.
\]

Repeatedly applying the measurability equality to sets also shows that if \(A,B\in\mathcal L\), then

\[
A\cup B\in\mathcal L.
\]

More generally, let \(A_1,A_2,\ldots\in\mathcal L\).

Turn them into pairwise disjoint sets:

\[
B_1=A_1,
\]

\[
B_n=A_n\setminus\bigcup_{k=1}^{n-1}A_k,\qquad n\ge2.
\]

Each of these \(B_n\) is measurable.

Moreover,

\[
\bigcup_{n=1}^{\infty}A_n
=
\bigsqcup_{n=1}^{\infty}B_n.
\]

For any \(E\subseteq\mathbb R\), repeated finite measurable partitions give

\[
m^*(E)
\ge
\sum_{k=1}^{N}m^*(E\cap B_k)
+
m^*\left(E\setminus\bigcup_{k=1}^{\infty}B_k\right).
\]

Letting \(N\to\infty\) and using subadditivity of outer measure,

\[
m^*\left(E\cap\bigcup_{k=1}^{\infty}B_k\right)
\le
\sum_{k=1}^{\infty}m^*(E\cap B_k),
\]

we obtain

\[
m^*(E)
\ge
m^*\left(E\cap\bigcup_{k=1}^{\infty}B_k\right)
+
m^*\left(E\setminus\bigcup_{k=1}^{\infty}B_k\right).
\]

The reverse inequality already follows from subadditivity.

The two sides are therefore equal.

This proves that a countable union is still measurable.

Thus

\[
\boxed{\mathcal L\text{ is a }\sigma\text{-algebra}.}
\]

Furthermore, similar finite-partition and limiting arguments show:

If \(A_1,A_2,\ldots\in\mathcal L\) are pairwise disjoint, then

\[
\boxed{
m^*\left(\bigcup_{n=1}^{\infty}A_n\right)
=
\sum_{n=1}^{\infty}m^*(A_n).
}
\]

Consequently, restricting outer measure to \(\mathcal L\),

\[
m=m^*|_{\mathcal L},
\]

gives a genuine measure.

This is exactly what we have been seeking.

### 5.8.2 Why Are All Borel Sets Included?

One important question remains.

Can this construction at least measure intervals?

The answer is yes.

For example, consider the half-line

\[
A=(-\infty,a).
\]

For any \(E\subseteq\mathbb R\), cover \(E\) by a family of open intervals, and then split each covering interval into left and right parts at \(a\).

The lengths of the two parts still add up to the original interval’s length.

Taking the infimum over the total lengths of these covers proves

\[
m^*(E\cap A)+m^*(E\setminus A)\le m^*(E).
\]

The other direction follows from subadditivity.

Thus \(A\) is measurable.

Similarly, every open interval is measurable.

And because \(\mathcal L\) is a \(\sigma\)-algebra,

\[
\boxed{
\mathcal B(\mathbb R)\subseteq\mathcal L.
}
\]

We have thereby accomplished something very important:

Starting from interval length, we have constructed a translation-invariant, countably additive measure on a sufficiently rich family of sets.

It is Lebesgue measure.

### 5.8.3 Are Borel Sets and Lebesgue Measurable Sets the Same?

One further point is easily overlooked.

\[
\mathcal B(\mathbb R)
\subsetneq
\mathcal L.
\]

In other words, there are strictly more Lebesgue measurable sets than Borel sets.

Why?

Consider the classical middle-thirds Cantor set \(C\).

It is closed, hence Borel.

It is uncountable, but

\[
m(C)=0.
\]

because at step \(n\), the \(2^n\) remaining intervals have total length

\[
\left(\frac23\right)^n,
\]

and this length tends to zero.

More importantly, under Lebesgue measure, every subset of a null set is still measurable and has measure zero.

Indeed, if \(A\subseteq C\), then

\[
0\le m^*(A)\le m^*(C)=0.
\]

Thus \(m^*(A)=0\), and any set of outer measure zero automatically satisfies Carathéodory’s measurability criterion.

Hence

\[
\boxed{
A\subseteq C\implies A\in\mathcal L.
}
\]

But the Cantor set has the same cardinality as the reals, and its power set has strictly greater cardinality than the family of Borel sets. For the full well-founded Borel coding and cardinal comparison, see the [measure foundations](../foundations/t-measure.md#t-measure-borel-code).

There must therefore be subsets of the Cantor set that are not Borel, yet are Lebesgue measurable.

This shows that Borel measure can be completed by adjoining all subsets of null sets to the measurable structure. The [companion proof](../foundations/t-measure.md#t-measure-completion) constructs completion for an arbitrary measure and proves minimality and uniqueness.

We finally have a rigorous continuous uniform probability model:

\[
\boxed{
\begin{aligned}
\Omega&=[0,1],\\
\mathcal F&=\mathcal L|_{[0,1]},\\
P(A)&=m(A).
\end{aligned}
}
\]

where

\[
\mathcal L|_{[0,1]}
=
\{A\subseteq[0,1]:A\in\mathcal L\}.
\]

For every \(0\le a<b\le1\),

\[
P([a,b])=b-a.
\]

The continuous uniform probability we wanted from the outset finally has a rigorous mathematical foundation.

But the price is:

\[
\boxed{\mathcal F\ne\mathcal P([0,1]).}
\]

We retained natural length, translation invariance, and countable additivity, while giving up the wish that every set be measurable.

This is no failure.

It is the discovery of the right mathematical structure.

---

## 5.9 Why Must Probability Be Countably Additive?

So far, we have met \(\sigma\)-algebras and Lebesgue measure.

But one important question remains unanswered.

If finite additivity suffices for finite games of chance, why go further and require countable additivity?

In other words, why is it insufficient merely to require

\[
P(A\cup B)=P(A)+P(B)
\]

for mutually exclusive \(A,B\)?

This time, instead of starting from history, we examine the relationship between probability and limits.

### 5.9.1 How Should Probability Change as Events Grow Larger?

Let

\[
A_1\subseteq A_2\subseteq\cdots
\]

be an increasing sequence of events.

Set

\[
A=\bigcup_{n=1}^{\infty}A_n.
\]

We write

\[
A_n\uparrow A.
\]

Suppose \(A_n\) means that a random event has occurred at least once in the first \(n\) trials.

Then \(A\) means that it has occurred at least once over the entire infinite sequence of trials.

As the first \(n\) trials cover more and more time, we naturally want:

\[
\boxed{
P(A_n)\longrightarrow P(A).
}
\]

Finite additivity alone does not guarantee this conclusion.

Let us prove why countable additivity does.

Define

\[
B_1=A_1,
\]

\[
B_n=A_n\setminus A_{n-1},
\qquad n\ge2.
\]

The sets \(B_n\) are pairwise disjoint.

Moreover,

\[
A=\bigsqcup_{n=1}^{\infty}B_n.
\]

Countable additivity therefore gives

\[
P(A)=\sum_{n=1}^{\infty}P(B_n).
\]

On the other hand, finite additivity gives

\[
P(A_n)=\sum_{k=1}^{n}P(B_k).
\]

Letting \(n\to\infty\) yields

\[
\boxed{
A_n\uparrow A
\quad\Longrightarrow\quad
P(A_n)\uparrow P(A).
}
\]

This is called continuity of measure from below, or continuity along increasing sequences of sets.

For a decreasing sequence of events,

\[
A_1\supseteq A_2\supseteq\cdots,
\]

if

\[
A=\bigcap_{n=1}^{\infty}A_n,
\]

then, since a probability space has finite total measure, we can apply the preceding result to complements to obtain

\[
\boxed{
A_n\downarrow A
\quad\Longrightarrow\quad
P(A_n)\downarrow P(A).
}
\]

This is called continuity of measure from above.

We finally see one of the real meanings of countable additivity.

**It ensures that when events approach a limiting event through countable set operations, probability remains compatible with that limit.**

Indeed, for a finite measure, finite additivity together with continuity along increasing sequences already implies countable additivity.

These are therefore not entirely unrelated mathematical requirements.

Countable additivity can be understood as a principle that makes probability compatible with limiting operations.

### 5.9.2 An “Infinite Fair Lottery” That Cannot Exist

Now imagine a lottery.

Every natural number,

\[
1,2,3,\ldots
\]

can be the winning number.

And we want every number to be treated completely fairly, with the same probability.

Suppose

\[
P(\{n\})=c
\]

for every \(n\).

If \(c>0\), then

\[
P(\mathbb N)
=
\sum_{n=1}^{\infty}c
=\infty.
\]

But we require

\[
P(\mathbb N)=1.
\]

Thus \(c>0\) is impossible.

If \(c=0\), then

\[
P(\mathbb N)
=
\sum_{n=1}^{\infty}0
=0.
\]

Again, a contradiction.

Therefore:

\[
\boxed{
\text{There is no measure defined on }\mathbb N\text{ 、}\\
\text{that is a countably additive probability measure giving equal mass to every singleton。}
}
\]

The real problem is not that there are too many natural numbers.

It is that we require all singletons to have equal probabilities while also requiring all the natural numbers together to have probability 1.

If probabilities may vary with the number, there is no difficulty.

For example:

\[
P(\{n\})=2^{-n},
\qquad n=1,2,\ldots
\]

because

\[
\sum_{n=1}^{\infty}2^{-n}=1.
\]

This deserves some reflection.

In Chapter 1, symmetry led us to uniform probabilities.

Now, however, symmetry may conflict with countable additivity.

**Not every symmetry requirement that feels fair can be realized in an infinite probability space.**

Probability theory must distinguish clearly between symmetries that produce valid probability distributions and those expressible only in other mathematical frameworks.

---

## 5.10 Kolmogorov: Probability Finally Becomes a Special Case of Measure

We now have the main mathematical structures needed to establish modern probability theory.

A space of outcomes \(\Omega\).

A family of events \(\mathcal F\) to which probabilities may be assigned.

And a function \(P\) that assigns numerical values to these events.

We can therefore finally state formally:

### Definition 5.3: Probability Space

A probability space is a triple

\[
\boxed{(\Omega,\mathcal F,P)}
\]

where:

\(\Omega\) is a nonempty sample space;

\(\mathcal F\) is, on \(\Omega\), a \(\sigma\)-algebra;

\(P:\mathcal F\to[0,1]\) satisfies

\[
P(\Omega)=1,
\]

and for any pairwise disjoint events \(A_1,A_2,\ldots\in\mathcal F\),

\[
\boxed{
P\left(\bigcup_{n=1}^{\infty}A_n\right)
=
\sum_{n=1}^{\infty}P(A_n).
}
\]

This gives the modern Kolmogorov axiomatic framework for probability.

![Andrey Nikolaevich Kolmogorov mathematician black and white portrait](../assets/images/06-01.img)

[Original image source](https://valeman.medium.com/andrey-kolmogorov-master-of-uncertainty-and-order-1080618e1afe)

**Andrey Kolmogorov（1903—1987）**

In 1933 he published *Grundbegriffe der Wahrscheinlichkeitsrechnung* (*Foundations of the Theory of Probability*), systematically establishing probability theory within the axiomatic framework of measure theory.

Here, too, we must respect history.

Kolmogorov did not first discover the connection between probability and measure in 1933. Earlier work by Borel, Lebesgue, and other mathematicians had already laid its foundations.

But Kolmogorov gave this framework a clear, systematic expression that became the basic language of modern probability.〔[48](#ref-turn701804search0), [54](#ref-turn701804search40)〕

We can finally return to the classical probability of Chapter 1 with a new understanding.

Suppose

\[
\Omega=\{\omega_1,\ldots,\omega_n\},
\]

Take

\[
\mathcal F=\mathcal P(\Omega).
\]

Define

\[
P(A)=\frac{|A|}{n}.
\]

Then all the probability axioms are satisfied.

Classical probability is therefore simply a particular example of a modern probability measure.

For a finite outcome space with unequal probabilities, we can likewise choose

\[
p_i\ge0,\qquad\sum_{i=1}^{n}p_i=1,
\]

and then define

\[
P(A)=\sum_{\omega_i\in A}p_i.
\]

For a countably infinite space, we can use a summable sequence of weights.

For a continuous space, we can use Lebesgue measure or other probability measures constructed from it.

We suddenly see:

\[
\boxed{
\begin{gathered}
\text{classical equally likely counting}\\
\text{discrete probabilities with unequal weights}\\
\text{continuous uniform probability}\\
\text{more general probability distributions}
\end{gathered}
\quad
\begin{gathered}
\\[-1.5em]
\Bigg\}\\
\\[-0.5em]
\text{probability measures}
\end{gathered}
}
\]

These mathematical objects, once handled separately, have finally been unified.

But this unification does not arise because every probability can be reduced to counting.

Quite the reverse.

**Counting is only one special form of measure.**

That is the theoretical expansion we have achieved since Chapter 1.

---

## 5.11 Why Must Random Variables Be Measurable Functions?

We now have a probability space

\[
(\Omega,\mathcal F,P).
\]

But probability theory studies more than events.

We also need random variables.

For example, when rolling three dice, we may care only about the sum of their scores:

\[
X(\omega)=\text{sum of the scores on three dice}.
\]

In a finite space, any such function can be handled directly.

In a general probability space, however, we must be more careful.

Suppose

\[
X:\Omega\to\mathbb R
\]

is a function.

If we want to study the event

\[
\{X\le a\},
\]

it is actually

\[
X^{-1}((-\infty,a]).
\]

To calculate its probability, we must require

\[
X^{-1}((-\infty,a])\in\mathcal F.
\]

Nor should we handle only interval events of this kind.

For every Borel set \(B\), we want to calculate

\[
P(X\in B).
\]

We must therefore require:

\[
X^{-1}(B)\in\mathcal F,
\qquad B\in\mathcal B(\mathbb R).
\]

This is where the measurability requirement for random variables comes from.

### Definition 5.4: Random Variable

Let \((\Omega,\mathcal F,P)\) be a probability space.

If a function

\[
X:\Omega\to\mathbb R
\]

satisfies

\[
\boxed{
X^{-1}(B)\in\mathcal F
\quad
\text{for all }B\in\mathcal B(\mathbb R),
}
\]

then \(X\) is called a real-valued random variable.

Notice that this definition makes no demand whatsoever that the values of \(X\) themselves have some special random form.

Its only requirement is:

**Borel events formulated through \(X\) must correspond to events that are permitted to be measured in the original probability space.**

Only then can we rigorously define the distribution of \(X\):

\[
\boxed{
P_X(B)=P(X^{-1}(B)).
}
\]

This is exactly the pushforward-measure structure foreshadowed by the sum of three dice in Chapter 1.

There, we merely grouped the 216 ordered outcomes according to their sums.

Now we find that the same mathematical idea works in general probability spaces.

The distribution of a random variable is the new measure produced from the original probability measure by a measurable map.

### 5.11.1 Back to Brownian Motion: Why Is the Maximum of a Continuous Path Measurable?

Do you remember the event we studied in Chapter 4?

\[
A=\left\{
\omega:
\sup_{0\le t\le1}B_t(\omega)>1
\right\}.
\]

We can finally explain rigorously why it is measurable.

Suppose Brownian motion has already been constructed as a random element taking values in \(C([0,1])\).

For every continuous function \(f\),

\[
\boxed{
\sup_{0\le t\le1}f(t)
=
\sup_{t\in\mathbb Q\cap[0,1]}f(t).
}
\]

Why?

Because the rationals are dense in \([0,1]\) and \(f\) is continuous.

Thus, although we originally take a supremum over uncountably many times, for continuous paths it suffices to take the supremum over countably many rational times.

Hence

\[
A=
\bigcup_{q\in\mathbb Q\cap[0,1]}
\{B_q>1\}.
\]

Here we use the fact that if the supremum of a collection of real numbers exceeds 1, at least one member of that collection exceeds 1.

For each rational number \(q\), the event

\[
\{B_q>1\}
\]

is measurable.

Since \(\mathbb Q\cap[0,1]\) is countable,

\[
A\in\mathcal F.
\]

We finally see:

**Closure of a \(\sigma\)-algebra under countable unions, a countable dense subset of the reals, and continuity of paths together ensure the measurability of certain complicated path events.**

Properties that seem to come from different areas of mathematics fit together very naturally here.

This also explains why, when constructing Brownian motion in Chapter 4, we could not simply specify normal distributions at each time and declare that we had a complete theory of random paths.

We also need measurability, the structure of a function space, and appropriate path regularity.

---

## 5.12 What, Exactly, Does Probability 1 Mean?

There is another term we have used repeatedly without ever explaining it carefully.

Almost surely.

For example, in Chapter 4 we said:

Brownian paths are almost surely continuous.

We also said:

Brownian paths are almost surely nowhere differentiable.

What does this mean?

We can now give a rigorous definition.

If an event \(A\in\mathcal F\) satisfies

\[
P(A)=1,
\]

we say that \(A\) occurs almost surely.

If

\[
P(A)=0,
\]

we call \(A\) a probability-zero event.

Notice that

\[
P(A)=1
\]

does not mean

\[
A=\Omega.
\]

Likewise,

\[
P(A)=0
\]

does not mean

\[
A=\varnothing.
\]

For example, in the uniform probability space on \([0,1]\),

\[
P(X\in\mathbb Q)=0.
\]

Yet the interval certainly contains many rational numbers.

Probability zero therefore does not mean logical impossibility.

And probability 1 does not mean the absence of exceptions.

This distinction will become a very important idea in modern probability.

Often, we do not need a property to hold for every sample path.

We need only prove that it holds for all outcomes outside a set of probability zero.

Thus:

\[
X_n\xrightarrow{\mathrm{a.s.}}X
\]

means

\[
P\left(
\left\{\omega:
\lim_{n\to\infty}X_n(\omega)=X(\omega)
\right\}
\right)=1.
\]

Here we encounter measurability again.

For this probability expression to be valid, the set

\[
\left\{
\omega:
\lim_{n\to\infty}X_n(\omega)=X(\omega)
\right\}
\]

must belong to \(\mathcal F\).

For measurable real-valued random variables, this is indeed true, because the convergence event can be expressed through countable unions and intersections and conditions involving rational thresholds.

Therefore, **almost sure convergence is more than a notion of limits alone: it combines pointwise convergence from analysis with the measure-theoretic idea of null sets.**

When we systematically study the various modes of convergence, this will underpin our understanding of their differences.

---

# Chapter 5 Conclusion: Why Must Mathematics Learn to Let Go?

We began with a perfectly reasonable wish.

We wanted to select a number uniformly at random from \([0,1]\) and calculate the probability of every possible event.

To do so, we tried to construct a way of measuring the size of every set.

But infinite sets forced us to reconsider the meaning of “size.”

First, cardinality cannot represent interval length.

Then we discovered that a dense set can have measure zero.

More importantly, Vitali’s construction told us:

Under the usual foundations of set theory, we cannot retain all the properties we originally wanted at once.

We therefore had to abandon the requirement that every subset be measurable.

But this restriction did not impoverish the theory.

Quite the opposite.

Through \(\sigma\)-algebras, we found a measurable structure that accommodates infinite operations on events while remaining compatible with countable additivity.

Through outer measure and Carathéodory measurability, we constructed Lebesgue measure from interval length.

Finally, Kolmogorov’s axiomatic framework unified classical probability, discrete distributions, and continuous probability.

Looking back over the entire journey:

**Counting finite outcomes**

\[
P(A)=\frac{|A|}{|\Omega|}
\]

**The problem of size in infinite sets**
Cardinality no longer coincides with length

**Vitali’s impossibility**
The required properties cannot hold simultaneously on all subsets

**Measurability and \(\sigma\)-algebras**

\[
\mathcal F\subseteq\mathcal P(\Omega)
\]

**The modern probability space**

\[
(\Omega,\mathcal F,P)
\]

Counting becomes a special case of measure

I believe what we should remember most from this chapter is more than the three axioms of a probability space.

It is a deeper idea:

**A mathematical theory sometimes matures not by granting us more and more freedom, but by revealing which freedoms must be restricted.**

We gave up the requirement to measure every set in exchange for a rigorous theory capable of handling infinity, limits, and complicated random objects.

Yet although we now possess probability measures, one central question remains unresolved.

We can calculate the probabilities of events:

\[
P(A).
\]

But given a random variable

\[
X:\Omega\to\mathbb R,
\]

how should we calculate its average?

In a finite space, this is simple:

\[
\mathbb E[X]
=
\sum_{\omega\in\Omega}X(\omega)P(\{\omega\}).
\]

For continuous distributions, we are accustomed to writing:

\[
\mathbb E[X]
=
\int_{\mathbb R}x f_X(x)\,dx.
\]

But what if a random variable has neither a discrete distribution nor a probability density?

What if its distribution mixes discrete and continuous parts?

Or what if we study a singular distribution with no density?

Must we invent a new formula for expectation for every type of distribution?

We already know that probability is measure.

Does expectation, too, have a unified mathematical form?

The answer is:

\[
\boxed{
\mathbb E[X]=\int_\Omega X\,dP.
}
\]

For now, however, this formula is only a promise waiting to be explained.

We must answer:

Why can integration unify all these averages?

How can general integrals be constructed from simple functions?

Why do some random variables lack finite expectations?

When may we move a limit inside an expectation?

These questions will lead us into the next chapter.

# Chapter 6: The Rebirth of the Average—From Weighted Sums to the Lebesgue Integral

We shall return to the fair stakes of Chapter 1.

This time, however, we will regard expectation as more than a way of calculating winnings.

We will discover:

**Why integration is the most natural extension of weighted averaging, and why measure theory ultimately needs an integral different from Riemann’s.**

The monotone convergence theorem, Fatou’s lemma, the dominated convergence theorem, and the Fubini–Tonelli theorem will gradually emerge along the way.

We will also prepare for a rigorous study of conditional expectation, martingales, and the various modes of convergence.

The Mathematics of Chance · Volume II, Chapter 5 · Working draft v0.1
