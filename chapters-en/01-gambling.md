## Chapter 1: A Game of Chance Left Unfinished

Why should dividing a stake fairly require an entirely new kind of mathematics?

### 1.1 Before Probability Became Mathematics

Imagine that we live in seventeenth-century Europe.

Mathematicians can already solve complex geometric problems, algebra is developing, and astronomers can use mathematics to predict the motions of celestial bodies.

Yet a seemingly simple question has troubled many people:

**If a game of chance must end halfway through, how should the money on the table be divided?**

In the fifteenth and sixteenth centuries, this so-called *Problem of Points*, or the division of stakes, had already appeared in mathematical writings. Pacioli, Cardano, and others studied related questions.

In 1654, correspondence between Pascal and Fermat advanced its solution toward more systematic and general mathematical methods, becoming a celebrated milestone in the history of probability. In 1657, Huygens published another important work on calculations in games of chance.

But we must be careful: **1654 was not the first time people used mathematics to study randomness**. These ideas developed over hundreds of years; they were not invented suddenly on a single day. 〔[1](#ref-turn673477search0), [2](#ref-turn673477search2), [3](#ref-turn673477search4), [4](#ref-turn673477search7)〕

For now, let us leave the historical sources and construct a simple modern teaching example.

### 1.2 What Does Fairness Mean?

Two players, A and B, enter a match:

- Each round is won by either A or B, with equal chances of winning.
- The first player to win four rounds receives all 64 gold coins.
- A has won three rounds and B has won two.
- External circumstances force the match to stop.

How should the 64 gold coins be divided?

Our first thought is to divide them in proportion to the rounds already won:

\[
A:B=3:2.
\]

A therefore receives

\[
64\cdot\frac35=38.4,
\]

and B receives

\[
64\cdot\frac25=25.6.
\]

This seems fair because it respects the rounds the players have already completed.

But there is a problem.

**Can past victories really measure the chances of winning that each player currently holds?**

If A needs only one more win while B must win twice in succession, the previous score alone seems insufficient to assess their present positions.

A new way of thinking therefore emerges:

> To divide the money, we should examine not only what happened in the past, but also what might happen in the future, starting from the current state.

This shift in thinking matters more than the particular calculation.

The record of past rounds is known.

The results of future rounds are unknown.

For the first time, we are trying to use mathematics to value an **outcome that has not yet occurred**.

### 1.3 How Can We Calculate a Future That Has Not Happened?

We will not begin with definitions of probability spaces, random variables, or expectation.

We make just one assumption: A and B have equal chances of winning the next round, and the result of each round is unaffected by previous results.

Consider the next round.

**Case one: A wins.**

The match ends immediately, and A receives 64 gold coins.

**Case two: B wins.**

The score becomes 3:3.

Each player is one win away from victory, so their positions are perfectly symmetric.

If we accept that both players have equal claims in a symmetric position, A and B now each hold a chance of winning worth 32 gold coins.

Now return to the moment when the match was interrupted.

The next round has only two equally likely outcomes:

- A wins and receives 64.
- B wins, bringing the match to a position in which each player's claim is worth 32.

Thus the fair value of A's position is

\[
V_A=\frac12(64)+\frac12(32)=48.
\]

while the fair value of B's position is

\[
V_B=64-48=16.
\]

This gives

\[
\boxed{V_A:V_B=3:1}.
\]

Arithmetic alone does not determine this answer. It rests on assumptions of **equal chances, independent outcomes, and the use of a weighted average of future payoffs to measure fair value**.

Later we will ask why “fair value” should take this weighted-average form rather than some other form.

### 1.4 A Mathematical Object Quietly Appears

In that calculation, we did something very important.

We expressed the value of the current position in terms of the values of the positions it might lead to:

\[
\boxed{
V(\text{current state})
=
\frac12V(\text{A wins the next round})
+
\frac12V(\text{B wins the next round})
}
\]

We have not formally defined expectation, but this equation already has its basic structure.

More intriguingly, it contains another idea:

**The value of a present position can be determined backward from the average value of future states.**

We can generalize the state of the match.

Let \(V(a,b)\) denote A's fair share of the total prize when A still needs \(a\) wins and B still needs \(b\) wins, taking the whole prize as one unit.

Then, when \(a,b\ge1\),

\[
\boxed{
V(a,b)
=
\frac12V(a-1,b)
+
\frac12V(a,b-1)
}
\]

The boundary conditions are

\[
V(0,b)=1 \quad(b\ge1),
\]

and

\[
V(a,0)=0 \quad(a\ge1).
\]

We are no longer studying only one particular game of chance.

We have obtained a function on integer lattice points whose interior values are determined by neighboring states.

This is a recursive boundary-value problem.

From a modern perspective, it also foreshadows connections among harmonic functions, dynamic programming, and martingales.

These are, of course, interpretations made from the vantage point of modern mathematics. We are not claiming that seventeenth-century mathematicians had already established these theories.

### 1.5 A Question Worth Pursuing

We solved the problem by setting the present value equal to the average of future values.

But why is this the only reasonable method?

We were relying on a principle of fairness.

For example, suppose someone can choose between:

- receiving 48 gold coins immediately;
- or continuing the match, with equal chances of outcomes worth 64 or 32.

We regard the two choices as having the same fair value.

This implies a more general principle:

\[
\text{fair value}
=
\text{weighted average of all possible payoffs}.
\]

But why should the weights be probabilities? Why should the average be linear? If someone strongly dislikes risk, does this calculation still give their subjective value?

These questions will lead us to distinguish expectation and probability from theories of decisions under risk.

Notice especially that, while making this calculation, we had not even formally defined probability.

We began with a requirement for fair exchange, then gradually discovered that we needed a mathematical language to measure the different possibilities the future holds.

Perhaps this is the most compelling feature of the story of probability's beginnings.

---

# The Mathematics of Chance
Volume I · Can Chance Be Calculated?

# Chapter 1: A Game of Chance Left Unfinished (Continued)

## 1.6 Can We Really Calculate Probability by Counting?

In the previous section, an interrupted game of chance revealed a surprising mathematical idea:

A person's current fair value can be calculated from future outcomes that have not yet occurred.

But our argument contained an assumption that almost escaped notice.

We said that A and B had equal chances of winning the next round, so each could be assigned weight \(1/2\).

Where does this \(1/2\) actually come from?

Suppose someone answers:

“There are only two possible outcomes, so the probability of each is \(1/2\).”

This explanation sounds very natural.

But we must ask: **Why must two possible outcomes each have probability one half?**

A coin can land heads or tails, but a specially altered coin may well be more likely to land heads.

A football match can be described simply as a win, a draw, or a loss. Yet we would certainly not conclude that all three have probability \(1/3\).

“Can happen” and “has the same chance of happening” are different things.

We seem to lack a mathematical language for what it means for two outcomes to have equal chances.

Before pursuing that question, however, I would like us to return to a historical episode earlier than the correspondence between Pascal and Fermat.

---

## 1.7 Galileo and Three Dice: Why Do Two Ways of Counting Give Different Answers?

![Galileo Galilei portrait Justus Sustermans historical painting](../assets/images/14-01.img)

[Original image source](https://www.talmudology.com/jeremybrownmdgmailcom/2021/2/15/happy-birthday-galileo)

**Galileo Galilei（1564—1642）**

Galileo studied not only motion, astronomy, and physics, but also mathematical questions arising from dice games.

In a manuscript usually dated between 1613 and 1623, he discussed a seemingly contradictory phenomenon involving the sum of three dice.

The historical question was:

When three six-sided dice are thrown together, why is a sum of 10 more likely than a sum of 9?

At first, this hardly seems to be a question at all.

We can easily find six different combinations of three dice that sum to 9:

\[
\begin{aligned}
9={}&1+2+6\\
={}&1+3+5\\
={}&1+4+4\\
={}&2+2+5\\
={}&2+3+4\\
={}&3+3+3.
\end{aligned}
\]

For 10, there are also exactly six:

\[
\begin{aligned}
10={}&1+3+6\\
={}&1+4+5\\
={}&2+2+6\\
={}&2+3+5\\
={}&2+4+4\\
={}&3+3+4.
\end{aligned}
\]

If each sum has six combinations, why should their frequencies differ?

Galileo's crucial insight was: **we were counting the wrong objects.**

For example, the combination

\[
1+2+6=9
\]

can actually arise from six ordered outcomes:

\[
(1,2,6),(1,6,2),(2,1,6),
\]

\[
(2,6,1),(6,1,2),(6,2,1).
\]

But

\[
3+3+3=9
\]

has only one permutation.

Although both count as “one combination of face values,” they contain completely different numbers of actual dice outcomes.

Let us carry out the full calculation.

Three dice: all combinations with sums of 9 and 10

**Sum = 9**

| Combination | Permutations |
|---|---:|
| 1,2,6 | 6 |
| 1,3,5 | 6 |
| 1,4,4 | 3 |
| 2,2,5 | 3 |
| 2,3,4 | 6 |
| 3,3,3 | 1 |
| **Total** | **25** |

**Sum = 10**

| Combination | Permutations |
|---|---:|
| 1,3,6 | 6 |
| 1,4,5 | 6 |
| 2,2,6 | 3 |
| 2,3,5 | 6 |
| 2,4,4 | 3 |
| 3,3,4 | 3 |
| **Total** | **27** |

Probability of a sum of 9
25/216

Approximately 11.57%

Probability of a sum of 10
27/216

12.50%

Under a model of three fair, mutually independent dice, we obtain

\[
\boxed{
P(S=10)-P(S=9)=\frac{2}{216}=\frac1{108}.
}
\]

This agrees with the phenomenon Galileo explained. For the manuscript's dating, the problem's background, and the calculation, see Hald's history of probability and the English translation of Galileo's text. 〔[5](#ref-turn689420search25), [6](#ref-turn689420search2), [7](#ref-turn689420search26)〕

What really matters here, however, is not yet the numbers \(25\) and \(27\).

We must instead answer:

**Why can ordered triples be counted with equal weights, while unordered combinations of three face values cannot?**

We cannot merely say that ordered triples give the correct answer.

That would use the answer to justify the method after the fact.

We need a mathematical principle independent of the answer to this particular problem.

That principle is symmetry.

## 1.8 Symmetry: Why Should Certain Outcomes Have the Same Probability?

Imagine an ideal, perfectly symmetric six-sided die.

Its six faces are labeled \(1,2,\ldots,6\).

If its material is distributed uniformly, its shape is perfectly symmetric, and the throwing mechanism favors no face, we have reason to believe that no difference among the faces affects their chances.

Notice that we did not begin by saying

\[
P(1)=\cdots=P(6)=\frac16.
\]

Our starting claim was:

**If two outcomes can be exchanged by a symmetry transformation that leaves the random mechanism unchanged, those outcomes should have the same probability.**

A very general mathematical idea now comes into play:

> The symmetries of an object should constrain the mathematical quantities that describe it.

Let us try to express this rigorously.

Let

\[
\Omega=\{\omega_1,\ldots,\omega_n\}
\]

be a finite outcome space.

Consider transformations acting on \(\Omega\) that form a group \(G\).

Assume:

1. The action of \(G\) on \(\Omega\) is transitive: any two outcomes can be transformed into one another by some group element;
2. The probability assignment under study is invariant under these transformations;
3. The total probability of all outcomes is 1, and the probabilities of mutually exclusive outcomes can be added.

In mathematical language, the second condition is

\[
P(gA)=P(A),
\qquad g\in G,\quad A\subseteq\Omega.
\]

By transitivity, for any \(\omega_i,\omega_j\), there is a \(g\in G\) such that

\[
g\omega_i=\omega_j.
\]

Therefore

\[
P(\{\omega_i\})
=
P(\{\omega_j\}).
\]

All singleton events thus have a common probability \(p\).

By normalization and additivity,

\[
1=P(\Omega)
=\sum_{i=1}^{n}P(\{\omega_i\})
=np.
\]

Hence

\[
\boxed{p=\frac1n}.
\]

For any event \(A\subseteq\Omega\), finite additivity gives

\[
\begin{aligned}
P(A)
&=\sum_{\omega\in A}P(\{\omega\})\\
&=\sum_{\omega\in A}\frac1n\\
&=\frac{|A|}{n}.
\end{aligned}
\]

We finally obtain the very familiar formula:

\[
\boxed{
P(A)=\frac{|A|}{|\Omega|}.
}
\]

But it now has a completely different meaning.

It is no longer a calculation rule that we have simply declared.

**On a finite space, it follows jointly from symmetry, normalization, and additivity.**

There is also a logical distinction that must be emphasized:

We have proved that if a probability assignment satisfies the relevant symmetry, it must be uniform.

We have not proved that real dice necessarily have this probabilistic symmetry.

Mathematics reveals the necessary consequences of symmetry. A symbolic model alone cannot guarantee that reality satisfies the model's assumptions.

### 1.8.1 A Deeper Question: Is Symmetry Objective, or Do We Choose It?

If someone alters a die's center of mass, it still has six labels, but we can no longer assume that its six outcomes are equally likely.

Symmetry therefore does not follow directly from the fact that “there are six outcomes.”

It comes from our judgment about the mechanism that generates the outcomes.

There is, however, another, subtler possibility.

Suppose I know nothing about a die's construction and have never observed any of its throws.

Can I assign equal probabilities to its six faces simply because I lack information?

This concerns what later came to be called the *Principle of Indifference*.

This idea has an important place in classical interpretations of probability, but it has also long been challenged: does not knowing how outcomes differ mean that they do not actually differ? 〔[8](#ref-turn561005search0), [9](#ref-turn561005search3)〕

There are two distinct propositions here:

\[
\text{the mechanism is symmetric}
\]

and

\[
\text{we do not know of any asymmetry in the mechanism}.
\]

The first is a statement about the world.

The second is a statement about our knowledge.

They are not equivalent.

This becomes an enduring disagreement in the history of probability: **does probability describe the objective world, or our uncertain knowledge of it?**

Before settling this philosophical question, however, we face a more immediate mathematical difficulty.

---

## 1.9 Why Does a Correct Probability Calculation Depend on How We Describe Outcomes?

Return to Galileo's three dice.

We originally represented the experimental outcomes as

\[
\Omega=\{1,\ldots,6\}^3.
\]

This is a finite space with

\[
|\Omega|=6^3=216
\]

elements.

Under the model of independent fair dice, each ordered triple has probability

\[
\frac1{216}.
\]

But adding the three face values gives only an integer.

Define the function

\[
S:\Omega\longrightarrow\{3,4,\ldots,18\}
\]

where

\[
S(i,j,k)=i+j+k.
\]

The event we actually care about is

\[
\{S=10\}.
\]

In other words, we are observing not the complete outcome of the three dice, but the information produced by applying a function to it.

Thus

\[
\{S=10\}
=
S^{-1}(\{10\}).
\]

Here \(S^{-1}\) denotes a preimage, not an inverse function.

Therefore

\[
P(S=10)
=
P(S^{-1}(\{10\}))
=
\frac{|S^{-1}(\{10\})|}{216}.
\]

This is why we must count 27 ordered triples rather than just six unordered combinations.

Two levels of description of the same random experiment

<svg viewBox="0 0 340 185" role="img" aria-label="216 ordered outcomes mapped to 16 possible sums"><rect x="13" y="24" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="32" y="24" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="51" y="24" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="70" y="24" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="89" y="24" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="13" y="43" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="32" y="43" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="51" y="43" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="70" y="43" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="89" y="43" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="13" y="62" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="32" y="62" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="51" y="62" width="13" height="13" rx="3" fill="#168782" opacity="0.85"/><rect x="70" y="62" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><rect x="89" y="62" width="13" height="13" rx="3" fill="#95A4BA" opacity="0.55"/><text x="56" y="107" fill="currentColor" font-size="12" text-anchor="middle">Ordered outcomes</text><text x="56" y="123" fill="currentColor" font-size="11" text-anchor="middle">216 outcomes</text><path d="M118 61H198m-8-7 8 7-8 7" stroke="#168782" stroke-width="2" fill="none"/><text x="158" y="48" text-anchor="middle" fill="currentColor" font-size="13">S</text><rect x="216" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="227" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="238" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="249" y="52" width="7" height="18" rx="2" fill="#168782" opacity="0.95"/><rect x="260" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="271" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="282" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="293" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><rect x="304" y="52" width="7" height="18" rx="2" fill="#95A4BA" opacity="0.55"/><text x="268" y="107" fill="currentColor" font-size="12" text-anchor="middle">Sum</text><text x="268" y="123" fill="currentColor" font-size="11" text-anchor="middle">16 values</text><text x="170" y="156" fill="currentColor" font-size="11" text-anchor="middle">Different original outcomes can have the same sum</text><text x="170" y="174" fill="currentColor" font-size="11" text-anchor="middle">The sum therefore need not be uniformly distributed</text></svg>

Schematic: a mapping merges outcomes, but need not preserve uniformity. The blocks are conceptual illustrations and do not represent the actual numbers of outcomes in the events.

We have uncovered an extremely important mathematical principle:

**A random object having a uniform distribution does not imply that a function of it also has a uniform distribution.**

In modern mathematical language, we have constructed a new probability distribution:

\[
P_S(B)=P(S^{-1}(B)).
\]

Here \(P_S\) is the pushforward measure of the original probability distribution under the map \(S\).

This formula deserves a pause.

On a finite space, it merely says “count how many dice outcomes correspond to each sum.”

Its structure, however, no longer depends on counting itself.

More generally, let

\[
X:(\Omega,\mathcal F,P)\longrightarrow(E,\mathcal E)
\]

be a measurable mapping.

Then the distribution of \(X\) is defined by

\[
\boxed{
P_X(B)=P(X^{-1}(B)),
\qquad B\in\mathcal E.
}
\]

This is the basic construction of the distribution of a random variable in modern probability theory.

We could follow it further, from discrete distributions to continuous distributions, stochastic processes, and random geometric objects.

But we do not need those theories yet.

We need only recognize one fact:

**Probability does more than assign a weight to a number: a mapping transfers the weights originally attached to the outcomes of a random experiment to the object we observe.**

Viewed through modern mathematics, Galileo's three-dice calculation already contains a finite instance of this idea.

---

## 1.10 Back to the Game: We Had Quietly Used Independence Too

Return now to our original game.

A has won three rounds and B has won two. A needs one more win, while B needs two.

To analyze the match, we can imagine the potential results of the next two rounds in advance, even though the actual match may end after the first.

There are four ordered potential outcomes:

\[
AA,\quad AB,\quad BA,\quad BB.
\]

If A wins at least one of the first two rounds, A receives the entire prize.

Thus A's eventual victory corresponds to

\[
\{AA,AB,BA\},
\]

while B's victory corresponds to

\[
\{BB\}.
\]

If each round is fair and the two rounds are independent, then

\[
P(AA)=P(AB)=P(BA)=P(BB)=\frac14.
\]

It follows that

\[
P(\text{A ultimately wins})=\frac34.
\]

This explains why we initially obtained a fair value of 48 gold coins:

\[
64\cdot\frac34=48.
\]

But a deeper question now arises.

If we know only that A and B each have probability \(1/2\) of winning each round, can we conclude that the four outcomes above are equally likely?

We cannot.

### 1.10.1 An Unexpected Counterexample

Let the potential outcomes of the next two rounds be random variables \(X_1,X_2\), taking values in \(\{A,B\}\).

We require only

\[
P(X_1=A)=P(X_1=B)=\frac12
\]

and

\[
P(X_2=A)=P(X_2=B)=\frac12.
\]

That is, each round considered on its own is fair.

This does not mean that the rounds are independent.

In fact, all three models below satisfy these marginal probability conditions.

| Model | \(P(AA)\) | \(P(AB)\) | \(P(BA)\) | \(P(BB)\) |
|---|---:|---:|---:|---:|
| Independent | 1/4 | 1/4 | 1/4 | 1/4 |
| Perfect positive correlation | 1/2 | 0 | 0 | 1/2 |
| Perfect negative correlation | 0 | 1/2 | 1/2 | 0 |

They give exactly the same answer to “Is each round fair?”

Yet they give completely different answers to “Who eventually wins the prize?”

<div class="experiment" data-widget="dependence"></div>

The probability that A eventually wins the prize. Choose independence, perfect positive correlation, or perfect negative correlation, and compare the probabilities of AA, AB, BA, and BB and A's fair share.

This shows that the fairness of each round alone does not determine the eventual winning probability.

We can, in fact, go further.

Let

\[
P(AA)=x.
\]

Since both marginal distributions equal \((1/2,1/2)\), we must have

\[
P(AB)=P(BA)=\frac12-x,
\]

and

\[
P(BB)=x.
\]

where

\[
0\le x\le\frac12.
\]

Thus A's eventual winning probability is

\[
\begin{aligned}
P(\text{A wins})
&=1-P(BB)\\
&=1-x.
\end{aligned}
\]

Without assuming independence, therefore,

\[
\boxed{
\frac12\le P(\text{A wins})\le1.
}
\]

The \(3/4\) we originally calculated is only one particular value in this entire range of possibilities.

Only with the independence assumption,

\[
P(AA)
=
P(X_1=A)P(X_2=A)
=
\frac14,
\]

can we conclude

\[
P(\text{A wins})=\frac34.
\]

For the first time, we have discovered that:

**Knowing the law of each random outcome separately does not mean knowing their joint law.**

This is one way in which probability theory goes deeper than counting alone.

It studies not only how likely an outcome is, but also the relationships among different outcomes.

More importantly, the original recurrence \(V(a,b)\), which expressed value using only the current score, also implicitly assumed that the score contained all relevant information needed to determine the future distribution.

If future outcomes are dependent, and that dependence also depends on the particular past outcomes, the current score alone may be insufficient to calculate future value correctly.

We are already approaching the heart of the later Markov property and the concept of a “state.”

---

## 1.11 Why Should the Probabilities of Mutually Exclusive Events Add?

We have introduced three important ideas:

symmetry, independence, and additivity.

Symmetry tells us when different outcomes should have the same probability.

Independence tells us when a joint probability can be factored into a product of individual probabilities.

But additivity seems to leave a question unanswered:

Why should the probabilities of two mutually exclusive events add?

For example, if \(A\cap B=\varnothing\), why require

\[
P(A\cup B)=P(A)+P(B)?
\]

Is this another rule introduced out of nowhere?

Let us return once more to gambling.

Suppose someone can buy a contract:

it pays one gold coin if event \(A\) occurs, and nothing otherwise.

We write

\[
\mathbf 1_A
\]

for the contract's payoff.

Now consider two contracts:

the first pays one gold coin if event \(A\) occurs.

The second pays one gold coin if event \(B\) occurs.

Assume \(A\) and \(B\) are mutually exclusive.

The total payoff from holding both contracts is

\[
\mathbf1_A+\mathbf1_B.
\]

But since \(A\cap B=\varnothing\),

\[
\boxed{
\mathbf1_A+\mathbf1_B=\mathbf1_{A\cup B}.
}
\]

Notice that this is, first of all, an entirely deterministic algebraic identity.

No probability calculation is involved.

It simply says that when two events cannot happen together, receiving one coin if either event occurs produces exactly the same payoff as separately holding the two corresponding contracts.

Now introduce an idealized principle of pricing without arbitrage:

if two portfolios produce identical payoffs in every possible situation, they should have the same price.

Let

\[
\pi(X)
\]

denote the price of payoff \(X\).

If these contracts can all be freely bought and sold, and the price system must rule out arbitrage opportunities in finite portfolios, consistent pricing must satisfy linear relationships.

In particular,

\[
\pi(\mathbf1_A+\mathbf1_B)
=
\pi(\mathbf1_A)+\pi(\mathbf1_B).
\]

We can therefore define

\[
P(A)=\pi(\mathbf1_A),
\]

normalizing the price of a contract guaranteed to pay one gold coin to 1.

We obtain

\[
\boxed{
P(A\cup B)=P(A)+P(B)
}
\]

whenever \(A\cap B=\varnothing\).

We also obtain

\[
P(\Omega)=1,
\qquad
P(A)\ge0,
\]

where nonnegativity follows from the no-arbitrage requirement that a nonnegative payoff cannot have a negative price.

Thus, in this idealized finite trading model, consistent prices for event contracts yield a finitely additive probability assignment.

This does not mean that probability theory historically arose entirely from financial pricing, or that actual market prices necessarily equal true probabilities.

We have simply discovered, from a modern mathematical perspective, a surprising unity:

**The additivity of probability can be connected to consistent pricing across different bets.**

In this sense, probability can both describe chance and provide a mathematical tool for valuing uncertain payoffs.

This also helps us understand the starting point of Chapter 1 anew.

We originally wanted only to divide 64 gold coins fairly.

Yet to understand “fairly,” we gradually introduced states, symmetry, independence, events, and additivity.

A mathematical structure is emerging from a concrete problem.

---

## 1.12 Counting Eventually Fails

We can now calculate probabilities on finite sample spaces with equally likely outcomes.

But can every probability problem be reduced to some kind of counting?

Suppose someone chooses a real number at random from the interval \([0,1]\).

Consider the interval

\[
\left[0,\frac12\right]
\]

What is the probability that the chosen number lies in it?

Following our earlier formula, we seem to need

\[
\frac{
|\{x:0\le x\le1/2\}|
}{
|\{x:0\le x\le1\}|
}.
\]

But the two intervals have the same cardinality.

Indeed, the mapping

\[
f:[0,1]\longrightarrow\left[0,\frac12\right],
\qquad f(x)=\frac x2
\]

is a bijection.

Thus

\[
\left|\left[0,\frac12\right]\right|
=
|[0,1]|.
\]

Comparing only the numbers of elements in these sets cannot distinguish the intervals at all.

Yet our intuitive understanding of “choosing uniformly from \([0,1]\)” calls for

\[
P\left(X\in\left[0,\frac12\right]\right)=\frac12.
\]

This reveals a fundamental difficulty:

**On infinite sets, the number of elements can no longer play the role of probability directly.**

More precisely, cardinality cannot capture the relative size expressed by interval length.

We need a concept more general than counting:

a tool that assigns a mathematical “size” to sets while retaining the necessary additive properties.

This is one of the problems that measure theory would eventually solve.

We are not ready to construct Lebesgue measure here, because many foundational questions remain to be explored.

But the direction of the story is becoming clear.

Starting from finitely many equally likely outcomes, probability theory must eventually reach a language independent of counting.

Along the way, we will discover a profound fact in the opposite direction:

\[
\text{counting}
\subset
\text{measure}.
\]

Uniform probability on a finite set is merely a special case of a more general measure structure.

---

## What Have We Discovered in This Chapter?

Looking back, we began simply by asking how to divide the prize in an interrupted game.

To obtain a mathematically meaningful answer, however, we discovered:

\[
\boxed{
\text{fair division}
\longrightarrow
\text{future outcomes}
\longrightarrow
\text{symmetry}
\longrightarrow
\text{probability assignment}
}
\]

Studying combinations of outcomes then forced us to introduce independence, additivity, and random mappings.

Most intriguingly, the classical probability formula, which initially seemed so natural,

\[
P(A)=\frac{|A|}{|\Omega|}
\]

does not actually tell us what probability is.

It tells us only how to calculate probability in a particular finite model with an equal-weight structure.

As Laplace's later classical formulation illustrates, the classical approach depends on the crucial premise of “equally possible cases.” What makes those cases equally possible itself still requires explanation. 〔[8](#ref-turn561005search0), [10](#ref-turn561005search25)〕

We have gained some mathematical tools, yet the most fundamental question remains:

**What should we do when outcomes lack symmetry, or when we do not know their probabilities at all?**

This leads us naturally to the next chapter.

# Chapter 2: From Chance to Belief—When Outcomes Are No Longer Equally Likely

In the next chapter, we will begin with an unfair die.

This time we cannot count directly or assume a uniform distribution in advance.

We will ask whether observing random phenomena can gradually reveal their underlying probabilities. If so, how can finite experience support predictions about the future?

There we will encounter two important and distinct directions in early probability theory: studying stable frequencies through repeated trials, and using available information to infer unknown outcomes.

These explorations will eventually lead us to Bernoulli's law of large numbers and the ideas of probabilistic inference advanced by Bayes and Laplace.

The Mathematics of Chance · Volume I, Chapter 1, draft v0.2 · End of chapter
