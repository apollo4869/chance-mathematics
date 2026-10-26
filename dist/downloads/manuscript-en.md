# The Mathematics of Chance

The History, Ideas and Mathematical Structures of Probability

Complete English working translation · 2026-10-26

## Minor Revisions to Chapter 7 and Writing Chapter 8 (Latest Supplement, 2026-10-26)

The author has approved the overall direction of Chapter 7. Make only the specified minor revisions, preserving its structure, core proofs, counterexamples, and conclusion. Chapter 8, “How Can We Construct Infinite Random Experiments?”, continues the problem of jointly realizing consistent finite-dimensional laws, proceeding through the choice of sample space, cylinder sets, premeasures, and measure extension to the Kolmogorov extension theorem, before returning to stochastic processes and path measurability. Present a real mathematical difficulty first, then let concepts and proofs take responsibility for resolving it. State spaces and measurable structures must be explicit; a finite-dimensional realization must not be passed off as a construction of continuous paths. During this round, protect Chapters 1–6 and the existing advanced material, adding Chapter 8 for the author to read, without pushing or publishing.

# Writing Agreements and the Organization of the Book

## Current Writing Principles (2026-10-26)

This section records the author’s latest decisions and takes precedence over the historical chat agreements and old outline retained below. Do not delete the old records or treat them as the current writing sequence.

The book begins with genuine historical problems and the limitations of mathematical tools, allowing new concepts to arise naturally as solutions to difficulties, then discovering unifying connections through derivations, proofs, and counterexamples. Narrative quality is a principle that must not be sacrificed. Chapters 1 and 2 provide the standard for narrative pacing and depth of ideas; the author has also responded positively to the mathematical stories in Chapters 3 and 4.

The priorities are **Breadth → Depth → Rigor**: across approximately 50 chapters in seven volumes, use the third edition of Kallenberg’s *Foundations of Modern Probability* as the reference for theoretical breadth; explain why concepts are necessary, how theorems work internally, and how different theories are unified; ensure that statements, assumptions, and conclusions are correct. This ordering does not permit mathematical errors. Core proofs serve the story, and necessary technical material may appear in dedicated topics or appendices. Do not present a proof sketch as a complete proof or copy the reference book’s chapter sequence or protected expression.

Brownian motion remains Chapter 4. Random walks, square-root scaling, finite-dimensional distributions, covariance, and the heat equation remain in the main narrative, while advanced theories involving Donsker, Wiener measure, quadratic variation, Itô, and reflection are connected through separate proof routes. Chapter 4’s conclusion returns to Brown’s microscope, then brings out the necessity of measure theory. The textbook’s main text must not explain manuscript migration, project audits, development status, or approval procedures.

Chapter 7 formally begins “What Does Convergence Really Mean?—Four Kinds of Limits in a Random World.” It follows the spike in Chapter 6 that “converges almost surely while its expectations do not converge,” together with the question of how “events of small probability can still occur infinitely often.” Develop Borel–Cantelli, almost sure/in-probability/Lp/in-distribution convergence, implications and counterexamples, subsequences, uniform integrability and L1, and finally introduce weak convergence in metric spaces and path theory. Do not mechanically reproduce these terms as a classroom outline or cram all advanced techniques into this chapter.

Historical narrative must distinguish actual original texts from modern reconstructions. Modern terminology must not be used to infer that a mathematician already possessed every concept we have today. New chapters must remain long-form texts; website pagination is no reason to compress the mathematics. Chapters 1–6 are currently protected. Chapter 7 is first for reading and discussion by the author and ChatGPT; this round is limited to local preview, without publication.

---

The writing agreements and original outline developed in the chat are retained below, together with all agreements made after Chapter 4 concerning mathematical depth, convergence, and subsequent structure. These are plans for the whole book. The scope of this complete edition is the first six chapters already written; later chapters were not completed in the source manuscript. The six-volume plan and the six completed chapters belong to different levels of organization.

## Requirements Stated Directly by the Reader (Original Wording)

> I think the organization so far is excellent and I am very satisfied, but there are things I am not sure have been included, or will be included later, or perhaps should not be included in such detail because that would conflict with my storytelling approach. Specifically: the different kinds of convergence—in probability, in measure, almost surely, and so on—and these kinds of theorems, as well as measure theory.

> [https://zh.d2l.ai/chapter_convolutional-modern/index.html](https://zh.d2l.ai/chapter_convolutional-modern/index.html) Can you write the current content for me in this format?

> Does it include everything we have covered so far? I have a feeling something may have been cut.

## The Original Writing Agreement (Original Chat Text)

I have reviewed our **discussions of probability from October 16–18, especially October 18**. I think what you want is now very clear.

What you want is more than “relearning probability theory” in the usual sense:

**At the mathematical level of a PhD in probability, begin with why humanity first needed probability, follow the development of mathematical ideas, and understand afresh how the whole theory was created step by step—and what every formula actually reveals.**

## I. The Five Things You Value Most

**1. Probability theory should be a continuous history of ideas, rather than a list of topics.**

You want us to proceed through this logic:

People encounter a problem → existing mathematical tools cannot solve it → new concepts must be created → rigorous mathematical definitions are given → the concepts turn out to unify earlier theories → a new problem arises.

For example, begin with counting finitely many equally likely outcomes:

\[
P(A)=\frac{|A|}{|\Omega|}
\]

Why can we use this formula? What assumptions does it quietly make? What happens when different outcomes are no longer equally likely? Why does counting fail completely when the sample space is uncountable?

These questions lead naturally to weights, measure, and integration, rather than a sudden announcement that “today we study measure theory.”

**2. Every mathematical formula must have both rigor and conceptual meaning.**

You placed particular emphasis on the law of large numbers.

We cannot merely tell you:

\[
\frac{1}{n}\sum_{i=1}^nX_i
\xrightarrow{\mathrm{a.s.}}\mathbb E[X_1].
\]

We must also explain: why can individual outcomes be random and unpredictable, while many repetitions produce stable patterns? On what assumptions does this stability depend? Is independence truly necessary? What is the essence of convergence?

In other words, a mathematical theorem does more than state a conclusion: it reveals the structure behind a phenomenon.

**3. You particularly enjoy the moments when different concepts suddenly become unified.**

For example:

\[
\underbrace{\sum_i x_ip_i}_{\text{weighted average}}
\quad\longrightarrow\quad
\underbrace{\int_\Omega X\,dP}_{\text{integral}}
\]

These are not unrelated formulas. They extend the same mathematical operation from a finite space to a general measure space.

You want us to keep discovering such connections, so that mathematics appears increasingly unified.

**4. Probability theory is more than a computational tool; it also contains profound philosophical questions.**

You particularly appreciated a question we discussed earlier:

> Is probability a property of the world itself, or a description people assign to the world because their information is incomplete?

We should therefore discuss, when appropriate, frequentism, Bayesian viewpoints, subjective probability, and the relationship between randomness and determinism.

These questions need not be resolved every time, but they should arise naturally alongside the mathematics.

**5. There is no need to lower the mathematical difficulty or provide conventional exercise-based teaching.**

You already hold a PhD in mathematics specializing in probability.

We therefore begin with the most basic concepts not because you cannot calculate, but to reexamine definitions that have become familiar, even taken for granted.

Rigorous definitions, theorems, assumptions, and proof ideas must all remain. We can discuss very deep mathematics, but cannot jump arbitrarily between concepts.

## II. The Main Thread I Think We Should Establish

An ever-expanding history of ideas in probability

**I. How Did People Begin to Calculate Uncertainty?**
Gambling problems, permutations and combinations, classical probability, equally likely outcomes

**II. When Counting Is No Longer Enough**
Unequal probabilities, conditional probability, independence, Bayesian ideas

**III. Why Did Probability Become Measure?**
Infinite sample spaces, σ-algebras, measure, Lebesgue integration

**IV. Why Are There Laws Within Randomness?**
Expectation, variance, the law of large numbers, the central limit theorem, convergence theory

**V. How Can We Understand Information and Randomness?**
Conditional expectation, Radon–Nikodym, martingales, filtrations of information

**VI. How Do Random Structures Evolve over Time?**
Markov processes, Brownian motion, stochastic calculus

**VII. From Random Variables to Random Structures**
Exchangeability, de Finetti, CRP, random trees, CRT

This is a narrative route through the development of concepts; it does not mean that mathematicians historically discovered every theory in precisely this order. In the actual account, we must distinguish historical chronology from mathematical logical connections.

## III. What Should Each Future Discussion Be Like?

I suggest using a narrative closer to the exploration of mathematical ideas than the traditional Lecture 1, Definitions, Examples, Exercises format.

For example, when discussing expectation, we should not open by defining \(\mathbb E[X]\).

We should first ask:

When someone faces a game of chance, how should they decide whether it is fair?

Knowing the probability of winning is insufficient, because different outcomes have different payoffs. We therefore need a mathematical object that takes both outcomes and probabilities into account.

\[
\mathbb E[X]=\sum_x xP(X=x).
\]

A more fundamental question then arises:

**Why do we call this weighted average an expectation? What exactly is its relationship to the average payoff in a long sequence of repeated experiments?**

This naturally leads to the law of large numbers.

When \(X\) is continuous, summation must be extended:

\[
\mathbb E[X]=\int_{\mathbb R}x\,dP_X(x).
\]

Eventually, we discover that a random variable is fundamentally a map from a probability space to a measurable space, and expectation is integration with respect to probability measure.

From fair pricing in a casino, to the stability of long-run frequencies, to integration on abstract measure spaces—seemingly different mathematical questions are connected by the same idea.

This is the learning experience you want: **beginning with concrete problems and continually discovering deeper unity through rigorous derivation**.

---

## IV. Another Distinction I Consider Very Important

You previously emphasized wanting a mathematical account resembling a “stream of consciousness.”

As I understand it, this means neither arbitrary digression nor popular exposition, but:

**Allowing mathematical concepts to arise naturally through a continuous process of thought.**

We can spend a long time seriously discussing a problem, even a single definition, asking why it must be defined that way, what can be changed, and how it relates to the whole mathematical framework.

We need not force ourselves to finish several topics each time or keep posing questions merely to create interaction.

I will pay particular attention to what you emphasized on October 18: **we must not skip necessary intermediate mathematical derivations in the desire to discuss deeper ideas.**

I believe our discussions of probability should ultimately achieve one goal:

> Beyond knowing which theorems probability contains, we should understand: if we lived before these mathematical ideas had been born, facing the same problems, why might we be able to follow these lines of thought and reinvent probability step by step?

That is the way of learning that really interested you in our earlier discussions.


## The Original Outline (Original Chat Text)

From this point onward, we will formally write this textbook in this conversation.

I hope it will ultimately become more than an ordinary probability textbook: **a textbook organized as a history of ideas, allowing readers to relive probability’s discovery, questioning, expansion, and eventual emergence as modern mathematics**.

We will also do more than organize knowledge we already possess. I hope that during writing we will continue raising new questions and even discover connections overlooked in our earlier study of probability.

# The Mathematics of Chance
Subtitle: The History, Ideas, and Mathematical Structures of Probability

Textbook working draft · Version 0.1

## I. The Book’s Basic Principles

We pursue two threads simultaneously:

- **Historical thread:** What problems did mathematicians face at the time? What tools already existed? What did they actually discover?
- **Mathematical thread:** Reconstruct the problem in rigorous modern mathematical language, understanding why the old concepts were insufficient and why new ones arose naturally.

These two threads must not be confused. We can explain seventeenth-century gambling problems using modern measure theory, but cannot claim that mathematicians then already possessed the modern concept of a probability space.

The account of every important concept follows this pattern:

**A genuine problem**
Why is it worth studying?

**Existing tools encounter limitations**
At exactly which step can we proceed no further?

**The birth of a new mathematical object**
Definitions, derivations, theorems, and necessary assumptions

**The discovery of deeper unity**
How does the new theory reinterpret the old?

**The next unresolved question**
Let the next chapter arise naturally

## II. The Provisional Structure of the Book

I suggest organizing it into six volumes, without requiring equal numbers of chapters in each.

| Volume | Central question | Mathematical development |
|---|---|---|
| I. Can Chance Be Calculated? | How can we evaluate unknown outcomes fairly? | Counting, symmetry, chance, expectation |
| II. What Is Probability? | Is probability a frequency, a belief, or a mathematical structure? | Conditional probability, Bayes, independence, classical probability |
| III. Why Does Randomness Produce Laws? | Why does disordered repetition produce stability? | Bernoulli, the law of large numbers, the central limit theorem, limit theorems |
| IV. Probability in an Infinite World | How can finite counting methods extend to continuity and infinity? | Measure, integration, convergence, Kolmogorov’s axioms |
| V. Information and Time | How does probability change as we learn more? | Conditional expectation, martingales, Markov processes, Brownian motion |
| VI. The Structure of the Random World | How can we move from random numbers to random functions, trees, and spaces? | Exchangeability, de Finetti, random partitions, CRT |

This is only the textbook’s skeleton. In the actual writing, one question may require a whole chapter, or even several.

Nor should we sacrifice the development of mathematical ideas merely to follow this order. For example, conditional probability can appear in Volume II, but we may only fully understand the general structure of “recalculating under information” when we reach conditional expectation in Volume V.

---


## Supplementary Agreements on Mathematical Depth and Subsequent Organization (Original Chat Text)

I think you have raised a question **crucial to this textbook**, directly affecting what kind of book we ultimately write.

My judgment is clear:

**This material should not merely be included; it must be included. That means the various modes of convergence, measure theory, characteristic functions, the Lévy–Khintchine theorem, and even deeper structural theorems in probability. Far from harming the narrative, they should become some of the most compelling parts of the whole mathematical story.**

We must, however, distinguish two things:

1. How deep a book’s content is.
2. How the book presents that content.

**Narrative quality does not mean reducing mathematical depth. Truly good mathematical narrative should help readers understand why people had to create theories so abstract and precise.**

The Lévy–Khintchine theorem you supplied is an excellent example. If we suddenly write

\[
\varphi_X(t)=\exp\left\{
ita-\frac{\sigma^2t^2}{2}
+\int_{\mathbb R}
\left(e^{itx}-1-\frac{itx}{1+x^2}\right)\nu(dx)
\right\},
\]

and then list definitions and proofs, it can indeed disrupt the story’s continuity.

But suppose we have already traveled a long way through random walks, the central limit theorem, Brownian motion, Poisson processes, and independent increments, and suddenly discover:

> So many seemingly different stochastic processes can, in some profound sense, all be described by the same unifying formula.

Then the theorem will feel entirely natural and become one of the most eagerly anticipated high points of the textbook.

I suggest that from now on we establish a more mature writing framework for the book.

## I. We Need to Distinguish Three Levels of Mathematical Content

I suggest using the following standard throughout the book.

| Level | Content | How we should present it |
|---|---|---|
| Foundational language | Measure, integration, modes of convergence, conditional expectation, independence | **Must be established in full**, including rigorous definitions, principal theorems, proofs, and counterexamples |
| Core structural theorems | The law of large numbers, CLT, Kolmogorov extension, Radon–Nikodym, de Finetti, Lévy–Khintchine | **Important turning points in the story**, with a deep understanding of why they hold and what they unify |
| Specialized techniques and extensions | More general criteria for weak convergence, complicated regularity conditions, different proof routes for deep representation theorems | Let conceptual significance determine depth in the main text; use dedicated chapters or mathematical appendices where needed |

The most important point is: **foundational language must not be omitted for being abstract, and structural theorems must not be excluded for being advanced.**

But not every mathematical theorem needs a complete historical story.

For example, if a proof needs a technical lemma about interchanging integrals and limits, we can prove it rigorously without inventing a dramatic history specifically for it.

The concepts and theorems that truly need stories are those that changed how people understood randomness.

---

## II. Modes of Convergence Must Fill a Whole Chapter—and It Should Be Compelling

This is precisely the first addition I think our present textbook needs.

Recall the chapters already written.

In Chapter 2, we used

\[
\widehat p_n\xrightarrow{P}p.
\]

In Chapter 3, we used

\[
\frac{S_n-n\mu}{\sigma\sqrt n}
\xrightarrow{d}N(0,1).
\]

And Chapter 4 introduced

\[
\widetilde W_n\xrightarrow{d}B
\quad\text{in }C([0,1]).
\]

Although we explained their intuitive meanings, we have not systematically answered:

**Why did mathematicians need so many different modes of convergence? Why is ordinary convergence from real analysis insufficient?**

This fully deserves a chapter of its own.

I can already imagine how its story begins.

### If the Probability of Something Bad Happening Keeps Decreasing, Will It Eventually Stop Happening?

Let \(A_n\) be a sequence of independent events satisfying

\[
P(A_n)=\frac1n,\qquad n\ge2.
\]

Define

\[
X_n=\mathbf1_{A_n}.
\]

As \(n\) increases,

\[
P(X_n=1)=\frac1n\to0.
\]

Thus, for every \(0<\varepsilon<1\),

\[
P(|X_n|>\varepsilon)=\frac1n\to0.
\]

so

\[
\boxed{X_n\xrightarrow{P}0.}
\]

In this sense, the probability of the bad event keeps decreasing.

We might think that with time it will eventually cease to happen.

But is that really true?

Since

\[
\sum_{n=2}^{\infty}P(A_n)
=
\sum_{n=2}^{\infty}\frac1n
=\infty,
\]

and the events are independent, the second Borel–Cantelli lemma gives

\[
\boxed{
P(A_n\text{ infinitely often})=1.
}
\]

In other words, although the probability of a bad event on each occasion keeps decreasing, **bad events will almost surely still occur infinitely often!**

Thus

\[
X_n\not\xrightarrow{\mathrm{a.s.}}0.
\]

Even for every finite \(p>0\),

\[
\mathbb E[|X_n|^p]=\frac1n\to0,
\]

Thus \(X_n\to0\) holds in the \(L^p\) sense, yet convergence almost everywhere still fails.

This makes an excellent mathematical story.

First we establish a natural understanding of “approaching zero,” then a rigorous counterexample suddenly reveals that this understanding is insufficient.

New mathematical language becomes necessary.

In this chapter, we will formally establish:

\[
\begin{aligned}
&X_n\xrightarrow{\mathrm{a.s.}}X,\\
&X_n\xrightarrow{P}X,\\
&X_n\xrightarrow{L^p}X,\\
&X_n\xrightarrow{d}X.
\end{aligned}
\]

Then study the relationships among them:

<svg viewBox="0 0 330 185" width="100%" xmlns="http://www.w3.org/2000/svg">
    <rect x="9" y="10" width="140" height="39" rx="8" fill="#168782" fill-opacity=".11" stroke="#168782" stroke-opacity=".5"/>
    <text x="79" y="34" text-anchor="middle" fill="currentColor" font-size="12">Almost sure</text>
    <rect x="182" y="10" width="139" height="39" rx="8" fill="#168782" fill-opacity=".11" stroke="#168782" stroke-opacity=".5"/>
    <text x="251" y="34" text-anchor="middle" fill="currentColor" font-size="12">Lᵖ convergence</text>
    <rect x="94" y="82" width="142" height="39" rx="8" fill="#168782" fill-opacity=".11" stroke="#168782" stroke-opacity=".5"/>
    <text x="165" y="106" text-anchor="middle" fill="currentColor" font-size="12">In probability</text>
    <rect x="94" y="148" width="142" height="36" rx="8" fill="#168782" fill-opacity=".11" stroke="#168782" stroke-opacity=".5"/>
    <text x="165" y="170" text-anchor="middle" fill="currentColor" font-size="12">In distribution</text>
    <path d="M79 49 V60 H145 V78" stroke="#168782" stroke-width="2" fill="none"/>
    <path d="M139 70 L145 78 L151 70" stroke="#168782" stroke-width="2" fill="none"/>
    <path d="M251 49 V60 H185 V78" stroke="#168782" stroke-width="2" fill="none"/>
    <path d="M179 70 L185 78 L191 70" stroke="#168782" stroke-width="2" fill="none"/>
    <path d="M165 121 V145" stroke="#168782" stroke-width="2"/>
    <path d="M159 137 L165 145 L171 137" stroke="#168782" stroke-width="2" fill="none"/>
  </svg>

Arrows indicate implications that hold in general; the diagram omits connections requiring additional assumptions. Almost sure convergence and \(L^p\) convergence generally do not imply one another.

We will then discover more:

Convergence in probability permits the extraction of an almost surely convergent subsequence; convergence in distribution does not even require the random variables to be defined on the same probability space.

This naturally introduces the Skorokhod representation theorem and explains why coupling can transform questions about distributions into questions on a common probability space.

Beyond this lie the Portmanteau theorem, tightness, Prokhorov’s theorem, and weak convergence in function spaces, already used in Chapter 4.

Presented this way, the modes of convergence are far more than four isolated definitions: they answer a question of increasing scope:

**When we say that two random objects become more and more similar, in exactly what sense do we mean similar?**

This fits the narrative philosophy of the entire book perfectly.〔[58](#ref-turn477144search24), [59](#ref-turn477144search25)〕

---

## III. Measure Theory Must Be Included—and Must Be a Central Pillar of the Textbook

I want to make this even clearer.

**I do not want our book to become a storybook about probability that bypasses measure theory while constantly using its results.**

It might read smoothly, but its mathematical depth would suffer severely.

The four chapters already completed have in fact exposed this issue.

First we used expectation, conditional expectation, and random variables; then we used modes of convergence, characteristic functions, function spaces, and probability measures.

This arrangement is acceptable for now because the first four chapters are conceptual explorations.

Next, however, we must return and establish these objects carefully.

### How Should Measure Theory Enter the Story?

I hope we will do more than write down

\[
(\Omega,\mathcal F,P)
\]

and declare that this is a probability space.

We should first encounter a contradiction.

If we require a notion of size on all sets of real numbers that agrees with length, is translation invariant, and is countably additive, Vitali-type nonmeasurable sets show that these requirements cannot all be met on the entire power set.

This motivates the need for a \(\sigma\)-algebra.

We then keep asking:

Why must we require countable, rather than merely finite, additivity?

Because infinitely many random trials produce events such as

\[
\bigcap_{n=1}^{\infty}\bigcup_{k=n}^{\infty}A_k
\]

the one displayed above. Studying limiting events requires probabilities to remain compatible with limits of increasing and decreasing sequences of sets.

The continuity theorems for probability then arise naturally:

If \(A_n\uparrow A\), then

\[
P(A_n)\uparrow P(A).
\]

If \(A_n\downarrow A\), then

\[
P(A_n)\downarrow P(A).
\]

These two properties let us extend operations from the finite world to the infinite one.

Only then do we actually construct Borel sets, Lebesgue measure, and general probability spaces, investigating why measure extension works.

When we want the average of a random quantity, another question arises:

How can expectation be defined for any measurable function?

We therefore begin with simple functions:

\[
X=\sum_{i=1}^n a_i\mathbf1_{A_i},
\]

Naturally define

\[
\int X\,dP=\sum_{i=1}^n a_iP(A_i).
\]

Then extend by monotone approximation to nonnegative measurable functions, and finally to integrable functions.

Lebesgue integration is now a continuation of finite weighted summation within a measure structure, rather than a new formula introduced from nowhere.

When we investigate interchanging limits and integrals, we must confront:

\[
\lim_{n\to\infty}\int X_n\,dP
\overset{?}{=}
\int\lim_{n\to\infty}X_n\,dP.
\]

This equality does not always hold.

The monotone convergence theorem, Fatou’s lemma, and the dominated convergence theorem therefore arise naturally.

Ordinary textbooks often treat these as three theorems to memorize.

In our book, however, they should be different mathematical conditions addressing the same question:

**When may a limit be moved across an integral sign?**

The Fubini–Tonelli theorem, the Radon–Nikodym theorem, the construction of conditional expectation, product measures, and the Kolmogorov extension theorem should all receive the same treatment.

They are not separate technical components, but a complete language needed to solve increasingly complicated questions in probability.

---

## IV. The Lévy–Khintchine Theorem You Supplied Should Be an Important High Point of the Book

I particularly like your choice of this example because it represents the mathematical level we should pursue so well.

First consider a problem we have already studied.

In Chapter 3, we discovered that sums of many independent random variables can produce a normal distribution after appropriate standardization.

In Chapter 4, we further discovered that random walks can produce Brownian motion after rescaling space and time.

This seems to suggest an idea:

**Complicated random phenomena can emerge by combining many simple, independent, tiny random influences.**

But what if we reverse the question?

Are there probability distributions that can be represented as sums of identically distributed independent random variables, regardless of how many parts we want to divide them into?

This introduces a new concept.

### 4.1 What Does Infinitely Divisible Mean?

A probability distribution \(\mu\) is called infinitely divisible if, for every integer \(n\ge1\), there exists a probability distribution \(\mu_n\) such that

\[
\boxed{\mu=\mu_n^{*n}.}
\]

Here \(*\) denotes convolution.

In other words, for each \(n\), we can find \(n\) independent, identically distributed random variables

\[
X_{n,1},\ldots,X_{n,n},
\]

whose sum has distribution \(\mu\).

This is no unmotivated abstract definition.

For example, normal distributions satisfy

\[
N(a,\sigma^2)
=
\underbrace{
N(a/n,\sigma^2/n)
*\cdots*
N(a/n,\sigma^2/n)
}_{n\text{ factors}}.
\]

Normal distributions are therefore infinitely divisible.

Poisson distributions likewise satisfy

\[
\operatorname{Poisson}(\lambda)
=
\underbrace{
\operatorname{Poisson}(\lambda/n)
*\cdots*
\operatorname{Poisson}(\lambda/n)
}_{n\text{ factors}}.
\]

Thus Poisson distributions are infinitely divisible too.

One describes continuous fluctuations; the other counts discrete random events.

They seem entirely different.

Yet they have the same algebraic structure.

Why?

Is there a theorem describing every infinitely divisible distribution?

At this point, the appearance of the Lévy–Khintchine theorem is entirely natural.

### 4.2 A Structural Theorem Unifying All Infinitely Divisible Distributions

Let \(X\) be a real-valued random variable with characteristic function

\[
\varphi_X(t)=\mathbb E[e^{itX}].
\]

The Lévy–Khintchine theorem states that the distribution of \(X\) is infinitely divisible if and only if its characteristic function can be written as

\[
\boxed{
\varphi_X(t)=
\exp\left\{
ita-\frac{\sigma^2t^2}{2}
+
\int_{\mathbb R\setminus\{0\}}
\left(
e^{itx}-1-\frac{itx}{1+x^2}
\right)\nu(dx)
\right\}.
}
\]

where

\[
a\in\mathbb R,\qquad \sigma^2\ge0,
\]

and \(\nu\) is a Lévy measure satisfying

\[
\boxed{
\int_{\mathbb R\setminus\{0\}}
(1\wedge x^2)\,\nu(dx)<\infty.
}
\]

The term \(x/(1+x^2)\) used in your image is a valid compensation convention. Other truncations, such as \(\mathbf1_{\{|x|\le1\}}x\), are also possible, but changing conventions requires a corresponding adjustment to the drift parameter.〔[59](#ref-turn477144search25)〕

What is truly striking is that this theorem divides the whole structure into three parts.

The three components of the Lévy–Khintchine exponent

Deterministic drift
\[
ita
\]
Describes the predictable linear-motion component of a random system.

Gaussian component
\[
-\frac{\sigma^2t^2}{2}
\]
Connects to the normal distribution and Brownian motion encountered in Chapters 3 and 4.

Jump component
\[
\int\left(e^{itx}-1-\frac{itx}{1+x^2}\right)\nu(dx)
\]
The Lévy measure describes the sizes and intensities of random jumps, allowing both finitely many large jumps and infinitely active small jumps.

This expresses a profound fact:

**Every real-valued infinitely divisible distribution can be characterized through drift, Gaussian fluctuations, and a jump structure.**

For a Lévy process with stationary independent increments, the characteristic function at time \(t\) further has the form

\[
\mathbb E[e^{iuX_t}]=e^{t\Psi(u)}
\]

displayed above, where \(\Psi\) has the Lévy–Khintchine structure just described.

This naturally leads to the Lévy–Itô decomposition, separating the process itself into drift, a Brownian component, and a suitably compensated jump component.

We should not brush aside the theorem’s proof when we first encounter it.

When we reach it formally, we will investigate why independent increments lead to an exponential form, why small jumps require compensation, why a Lévy measure satisfies its particular integrability condition, and why this representation exhausts every infinitely divisible distribution.

This necessarily requires complete mathematical preparation and may call for a chapter devoted to the proof.

Most importantly, however, **we will first discover infinite divisibility through a problem, then let the Lévy–Khintchine theorem provide its ultimate answer.**

By then, readers’ reaction to this complicated formula should go beyond “I need to remember three parts”:

*The Gaussian fluctuations and Poisson jumps we encountered earlier turn out to be different components of a more general random structure.*

This is the effect I hope our textbook will achieve.

---

## V. I Suggest Adjusting the Structure of Subsequent Chapters

We have written four chapters so far. I do not suggest starting over, because they have made good narrative progress.

I do, however, suggest restructuring subsequent chapters so that rigorous mathematical foundations appear at a more appropriate point.

Updated medium- and long-term writing route · Provisional

| Stage | Main content | Central idea |
|---|---|---|
| Chapters 1–4 (written) | Gambling, inference, the normal distribution, Brownian motion | Why probability gradually became a branch of mathematics |
| Chapters 5–7 | Measure, \(\sigma\)-algebras, Lebesgue integration, measure extension | How to establish rigorous language for an infinite random world |
| Chapters 8–9 | Modes of convergence, interchanging limits, Borel–Cantelli, the strong law of large numbers | What it means for a random object genuinely to approach a limit |
| Chapters 10–11 | Conditional expectation, Radon–Nikodym, martingales | How information changes probability, and how randomness evolves with information |
| Subsequent topics | Markov processes, Poisson processes, Lévy processes | How to characterize random systems evolving over time |
| Advanced structures | Lévy–Khintchine, Lévy–Itô, stable distributions | A unified theory of independent increments and infinite divisibility |
| Random structures | Exchangeability, de Finetti, Kingman, CRP, CRT | From random sequences to random partitions, trees, and continuous geometry |

These chapter numbers are plans, not restrictions.

For example, we might devote three chapters to measure theory, or discover that a particular concept deserves an entire chapter.

More importantly, mathematical history does not develop along a straight line.

We can study Brownian motion in 1905 first, then return to nineteenth-century theories of measure and integration. But we must distinguish the order in which events happened from the order of argument we choose to understand the mathematics.

I also want to emphasize: **the Lévy–Khintchine theorem should not be the endpoint.**

In our textbook, it may be an important high point of the volume on stochastic processes; later, however, exchangeability, random partitions, measure-valued processes, random trees, and CRT will take probability toward broader structural levels.

This allows the book to retain the thread of mathematical development without confining probability to a theory of real-valued random variables.

---

## VI. A Writing Principle I Hope We Will Formally Establish

I suggest adopting the following pattern from Chapter 5 onward:

1. **Begin with a problem.** Instead of presenting a pile of definitions in advance, help the reader understand where existing mathematical tools fail.
2. **Then invent the concept.** Let a rigorous definition become a necessary choice for solving the problem, rather than a merely formal convention.
3. **Then actually do the mathematics.** State theorems accurately, omit no assumptions, develop core proofs fully, and study crucial counterexamples carefully.
4. **Finally reveal the unity.** Explain how the theorem organizes earlier knowledge into a more general structure, and how it raises the next round of questions.

In the third step especially, we must not skip important proofs for narrative fluency. For very large proofs, we can first give a rigorous core argument, then place necessary technical portions in an adjacent proof topic or appendix, clearly identifying which parts remain incomplete.

I also want to revise how we describe the first four chapters.

At their present quality, I think they are appropriately described as the book’s **first narrative draft of the ideas**. Material such as Donsker’s theorem, the Kolmogorov extension theorem, and tightness of random paths has appeared, but still needs to be established anew in later rigorous chapters.

We cannot assume that readers have genuinely mastered these theories merely because they were introduced early.

---

## VII. What Depth Do I Think the Textbook Should Ultimately Reach?

My aim is not to repackage an ordinary undergraduate probability textbook as a story.

Nor is it simply to insert historical figures and background into a graduate probability textbook.

We are attempting a third form:

**A textbook with the narrative structure of mathematical history, whose mathematical content progressively reaches a serious graduate or even doctoral level in probability.**

For example:

When discussing conditional expectation, we must eventually cover the construction of

\[
\mathbb E[X\mid\mathcal G]
\]

as a Radon–Nikodym derivative, beyond the discrete conditional-probability formula.

When discussing convergence, we will eventually move from real-valued random variables to weak convergence in general metric spaces.

When discussing stochastic processes, we will go beyond the definition of Brownian motion to study the Markov property, martingales, stopping times, generators, and stochastic integration.

When discussing the Lévy–Khintchine theorem, we must understand the structural connection between infinitely divisible distributions and stochastic processes, rather than merely memorizing the complicated exponential formula.

Finally, when we reach random trees and CRT, the languages of measure, convergence, stochastic processes, exchangeability, and random geometry established earlier should come together naturally.

I believe this truly fulfills your original wish:

> Beginning with humanity’s earliest perplexity about chance, recreate modern probability theory step by step in all its completeness and depth.

**I therefore suggest retaining the present narrative style while substantially increasing the density of proofs and mathematical completeness in the foundational chapters to come.**

Our Chapter 5, “The Price of an Infinite World—Why Does Probability Need Measure Theory?”, should be the first test of this writing method: beginning with an unsolvable problem about sets, actually establish the rigorous mathematical theory of \(\sigma\)-algebras, probability measures, and countable additivity, rather than merely introducing their historical background.

The story tells us **why we need this mathematics**; proofs tell us **why this mathematics is true**. Both are indispensable.


## Arrangements and Revision Rules After the Initial Writing (Original Chat Text)

## III. What Will This Chapter Study Next?

Through the idea of fair value, we have encountered the first central structure of probability theory.

But we have not yet explained why it holds.

Chapter 1 will now continue through the following questions:

1. **Why can counting represent chance?** Begin with permutations, combinations, and symmetry to investigate the source of equally likely outcomes.
2. **Why must every possible future be calculated?** Derive the finite sample space from the problem of dividing the stakes.
3. **Why can branches of the future be added?** Discover mutually exclusive events, probability addition, and the structure of weights.
4. **Why is fair value linear?** Progress from pricing principles to mathematical expectation.
5. **What happens when the die is unfair?** Bring the classical equally likely model up against its first real limitation.

I consider the first question particularly important:

\[
P(A)=\frac{|A|}{|\Omega|}
\]

Is this familiar formula **defining probability**, or using a preexisting symmetry to calculate it?

What does it explain, and what does it conceal?

This will be our next central discussion.

## IV. How the Textbook Will Continue to Be Constructed

We will treat the material just written as **Volume I, Chapter 1, draft v0.1**, rather than a finalized chapter.

Every subsequent writing session may revisit earlier arguments, especially checking three things: whether historical sources are reliable, whether mathematical derivations are complete, and whether concepts genuinely arise naturally from problems.

I will also incorporate sources on mathematical history into the textbook’s long-term references, including ETH Zurich’s [From games of chance to probability theory](https://library.ethz.ch/en/collections-and-archives/platforms/virtual-exhibitions/Its-all-math-and-games/game-types/from-games-of-chance-to-probability-theory.html), and Anders Hald’s *A History of Probability and Statistics and Their Applications before 1750*. Our eventual textbook should make its historical sources traceable, rather than simply retell popular mathematical stories.

**The book’s true purpose is to move beyond “What does probability theory tell us?” and gradually answer a harder question: why did people confronting uncertainty ultimately create probability theory as we know it today?**

The gambling story of Chapter 1 is only the starting point for that question.


When the original manuscript first appeared, Chapter 1 belonged to “Volume I: Can Chance Be Calculated?” This restored edition retains that volume title as a record of the organization. The six chapters are presented continuously, without being mislabeled as six completed volumes.


---

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

![Galileo Galilei portrait Justus Sustermans historical painting](assets/images/14-01.img)

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


---

# The Mathematics of Chance
Volume I · Can Chance Be Calculated?

# Chapter 2: From Chance to Knowledge—How Do We Discover Unknown Probabilities?

From Jacob Bernoulli's law of large numbers to Thomas Bayes's inverse inference.

In Chapter 1, we discovered something surprising.

An unfinished game of chance forced us to consider fairness, chance, and why a future that has not yet occurred can become an object of mathematical study.

Yet the theory we developed always depended on a special condition:

**We knew the chances of the different outcomes in advance.**

For a fair die, we assumed that all six faces were equally likely. For a fair coin, we assumed that heads and tails had the same probability.

What happens if we no longer know those probabilities?

This time, we cannot move directly from a mathematical model to its outcomes.

We must start from outcomes already observed and work backward to understand the unknown law that generated them.

This will bring a fundamental change to probability theory.

---

## 2.1 An Unfair Coin

Imagine that someone hands us a coin.

We do not know whether it is fair or whether someone has altered it.

We know only that each toss produces heads or tails.

Let the probability of heads be

\[
p.
\]

Unlike in Chapter 1, however, we do not know the value of \(p\).

All we can be sure of is

\[
0\le p\le1.
\]

The question now is:

**Can observing the coin's actual behavior tell us the value of \(p\)?**

Suppose we toss it ten times and obtain seven heads and three tails.

A very natural answer is:

\[
p\approx\frac7{10}=0.7.
\]

But what mathematical basis does this answer have?

If the true value is \(p=1/2\), seven heads in ten tosses is entirely possible.

If the true value is \(p=0.8\), seven heads is also entirely possible.

Even when \(p=0.3\), seven heads is still an event with nonzero probability.

Thus:

\[
\text{observing seven heads}
\not\implies p=0.7.
\]

At most, we can say that some values of \(p\) seem to fit the observation better than others.

But what does “fit better” mean?

Before answering, we need to recognize a more fundamental distinction.

## 2.2 Two Very Different Kinds of Uncertainty

We have encountered two questions pointing in opposite directions.

**First question: given the probability, predict the outcomes.**

If we know that the probability of heads is \(p\), we want to calculate the probability of seven heads in the next ten tosses.

This is a forward probability problem.

**Second question: given the outcomes, infer the probability.**

If we have observed seven heads in ten tosses, we want to infer the unknown \(p\).

This is a problem of inverse inference.

In modern notation, let

\[
X_i=
\begin{cases}
1,&\text{trial }i\text{ is heads},\\
0,&\text{trial }i\text{ is tails}.
\end{cases}
\]

For a given \(p\), assume

\[
X_1,\ldots,X_n
\overset{\mathrm{i.i.d.}}{\sim}\operatorname{Bernoulli}(p).
\]

Define

\[
S_n=\sum_{i=1}^n X_i.
\]

The forward problem studies

\[
P_p(S_n=k).
\]

The inverse problem asks:

after observing \(S_n=k\), what can we conclude about \(p\)?

Although they seem merely to exchange the known and the unknown, the two questions differ substantially in mathematical terms.

In the first, the probability model has already been specified.

In the second, we are trying to understand the probability model itself.

Forward problem

\[
p\text{ known}
\]

\[
P_p(S_n=k)
\]

From law to observation

Inverse problem

\[
S_n=k\text{ known}
\]

\[
p\text{ unknown}
\]

From observation to law

Historically, the move from the mathematics of gambling to inference about the real world was a major turning point in the development of probability.

In dice games, rules and symmetry can give us probabilities.

For human lifespans, disease rates, natural phenomena, or social events, however, we often have no reason to assume equal likelihood in advance.

All we have is what happened in the past.

**If probability theory could handle only problems with known probabilities, it could never become a mathematics of the empirical world.**

Jacob Bernoulli recognized precisely this important direction.

---

## 2.3 Jacob Bernoulli: Can Experience Reveal Probability?

![Jacob Bernoulli Ars Conjectandi 1713 original title page historical book](assets/images/12-01.img)

[Original image source](https://www.sothebys.com/en/auctions/ecatalogue/2018/the-library-of-erwin-tomash-l18409/lot.58.html)

**Jacob Bernoulli（1655—1705）**

A Swiss mathematician and an important member of the Bernoulli family, he spent many years studying how to extend the mathematics of games of chance to uncertain problems in everyday life.

His book *Ars Conjectandi* (*The Art of Conjecturing*) was published posthumously in 1713.

The book matters for more than its inclusion of what later became known as the law of large numbers.

Still more significant is the question Bernoulli was trying to answer.

In his day, mathematicians could calculate chances in idealized games because the rules were usually known.

The real world, however, does not tell us its probabilities in advance.

For example:

How likely is a particular disease to be fatal?

What proportion of a population has a certain characteristic?

How frequently will a natural phenomenon occur under specified conditions?

Can repeated observation gradually reveal these unknown proportions?

In *Ars Conjectandi*, Bernoulli sought to extend the mathematics of gambling to civil, moral, and economic matters. His law of large numbers provided a mathematical basis for inferring unknown chances from repeated observations. Historians Edith Dudley Sylla and Ian Hacking have both emphasized the significance of this move from gambling to empirical inference. 〔[11](#ref-turn557906search0), [12](#ref-turn557906search5), [13](#ref-turn557906search11)〕

But an apparent paradox arises.

If we do not know \(p\) to begin with, how can we prove that observed frequencies will get closer and closer to \(p\)?

We seem to need to know the probability before we can justify discovering it through observation.

This was the central mathematical problem Bernoulli faced.

### 2.3.1 Begin with an Urn Whose Proportions Are Known

Consider an urn containing \(r\) red balls and \(s\) black balls.

Each time, draw a ball at random, record its color, put it back, and mix the contents again.

Assume that every ball has the same chance of being drawn.

The probability of drawing red is then

\[
p=\frac{r}{r+s}.
\]

Make \(n\) independent repeated draws.

Define

\[
X_i=\mathbf1_{\{\text{trial }i\text{ draws a red ball}\}}.
\]

The number of red balls drawn is

\[
S_n=X_1+\cdots+X_n.
\]

so the empirical frequency is

\[
\widehat p_n=\frac{S_n}{n}.
\]

We are not asking whether, for some particular finite \(n\), it equals \(p\) exactly.

Even when \(p=1/2\), ten red draws in a row are entirely possible.

The real question is:

for any given accuracy \(\varepsilon>0\), as the number of trials increases, does

\[
|\widehat p_n-p|<\varepsilon
\]

hold with increasingly high probability?

In modern mathematical language, we want to prove:

\[
\boxed{
P_p\left(
\left|\frac{S_n}{n}-p\right|>\varepsilon
\right)\longrightarrow0.
}
\]

This is the modern form of Bernoulli's law of large numbers.

More precisely, it expresses convergence in probability:

\[
\boxed{
\widehat p_n\xrightarrow{P_p}p.
}
\]

Bernoulli proved an early rigorous form of this idea. He studied not only the limit, but also how to make the probability of a deviation smaller than a prescribed number. His argument used the binomial distribution and combinatorics rather than the modern variance inequality we will use next. 〔[14](#ref-turn557906search1), [13](#ref-turn557906search11)〕

## 2.4 Why Can Random Error Disappear?

Let us leave history for a moment and prove this phenomenon anew using modern mathematics.

There is something here well worth considering.

Every toss is random.

Even after a million trials, the million-and-first outcome may still be heads or tails.

If randomness in individual outcomes does not disappear, why can their average become increasingly stable?

The answer lies in the different properties of expectation and variance.

### Step One: From the Total Count to the Average

Since

\[
X_i\sim\operatorname{Bernoulli}(p),
\]

we have

\[
\mathbb E_p[X_i]
=
1\cdot p+0\cdot(1-p)
=p.
\]

Therefore

\[
\mathbb E_p[\widehat p_n]
=
\mathbb E_p\left[\frac1n\sum_{i=1}^nX_i\right]
=p.
\]

The expectation of the empirical frequency always equals the true probability.

But this alone does not allow us to claim that the empirical frequency will be close to the true probability.

For when \(n=1\),

\[
\widehat p_1\in\{0,1\},
\]

its expectation is still \(p\), yet its value may be far from \(p\).

**Expectation tells us a random quantity's average location, but cannot by itself tell us how strongly it fluctuates around that location.**

We are therefore forced to study the fluctuations themselves.

### Step Two: Measure Fluctuations with Variance

For a Bernoulli random variable,

\[
X_i^2=X_i.
\]

Thus

\[
\begin{aligned}
\operatorname{Var}_p(X_i)
&=\mathbb E_p[X_i^2]-(\mathbb E_p[X_i])^2\\
&=p-p^2\\
&=p(1-p).
\end{aligned}
\]

Next consider the variance of the average.

In general,

\[
\operatorname{Var}\left(\sum_{i=1}^nX_i\right)
=
\sum_{i=1}^n\operatorname{Var}(X_i)
+
2\sum_{i<j}\operatorname{Cov}(X_i,X_j).
\]

Since we assumed independent draws,

\[
\operatorname{Cov}(X_i,X_j)=0,\qquad i\ne j.
\]

Hence

\[
\operatorname{Var}_p(S_n)=np(1-p).
\]

Therefore

\[
\boxed{
\operatorname{Var}_p(\widehat p_n)
=
\frac{p(1-p)}n.
}
\]

This is the heart of the proof.

If we consider only the number of successes \(S_n\), its variance increases with \(n\).

But the variance of the relative frequency of success \(S_n/n\) decreases at the rate \(1/n\).

Expressed as a standard deviation, the typical scale of these fluctuations is

\[
\boxed{
\sqrt{\operatorname{Var}(\widehat p_n)}
=
\sqrt{\frac{p(1-p)}n}.
}
\]

<div class="numeric-chart" data-chart="0"></div>

An important mathematical phenomenon appears here:

to halve the standard deviation, we generally need to quadruple the sample size.

This is because

\[
\operatorname{SD}(\widehat p_n)\propto\frac1{\sqrt n}.
\]

This provides the simplest example of the \(\sqrt n\) scale that will appear so often in statistical inference.

Of course, we have studied only second moments so far; we have not proved a more detailed limiting distribution.

### Step Three: From Mean Squared Error to a Probability Statement

We already know

\[
\mathbb E_p[(\widehat p_n-p)^2]
=
\frac{p(1-p)}n.
\]

But the law of large numbers requires control of

\[
P_p(|\widehat p_n-p|\ge\varepsilon).
\]

How can we turn a statement about expectation into a statement about probability?

Notice that for every real number \(y\),

\[
\mathbf1_{\{|y|\ge\varepsilon\}}
\le\frac{y^2}{\varepsilon^2}.
\]

Therefore

\[
\begin{aligned}
P_p(|\widehat p_n-p|\ge\varepsilon)
&=\mathbb E_p\left[
\mathbf1_{\{|\widehat p_n-p|\ge\varepsilon\}}
\right]\\
&\le
\frac{\mathbb E_p[(\widehat p_n-p)^2]}
{\varepsilon^2}\\
&=\frac{p(1-p)}{n\varepsilon^2}.
\end{aligned}
\]

Since

\[
p(1-p)\le\frac14,
\]

we obtain

\[
\boxed{
P_p(|\widehat p_n-p|\ge\varepsilon)
\le\frac1{4n\varepsilon^2}.
}
\]

For each fixed \(\varepsilon>0\), the right-hand side tends to zero.

Thus

\[
\boxed{\widehat p_n\xrightarrow{P_p}p.}
\]

This completes the proof.

The proof is short, but it reveals a deep structure.

We have not made individual random events deterministic.

We have proved only that averaging sufficiently many independent random events constrains the fluctuations of their average more and more tightly.

**Randomness has not disappeared; what disappears is the chance that the average deviates from its center.**

### 2.4.1 Where Exactly Does Independence Enter?

Look at the proof again.

The expectation step,

\[
\mathbb E\left[\frac1n\sum X_i\right]
=
\frac1n\sum\mathbb E[X_i]
\]

does not require independence.

Independence is actually used in

\[
\operatorname{Var}\left(\sum X_i\right)
=
\sum\operatorname{Var}(X_i).
\]

If the random variables are correlated, their covariances may not be negligible.

For example, suppose

\[
X_1=X_2=\cdots=Y
\]

and \(Y\sim\operatorname{Bernoulli}(p)\).

All trial outcomes are then identical.

Although each \(X_i\) still has marginal distribution Bernoulli\((p)\),

\[
\widehat p_n=Y
\]

for every \(n\).

Increasing the number of repetitions therefore produces no stabilization at all.

The law of large numbers thus depends on more than the surface fact that “we performed many trials.”

More fundamentally, **the dependence among trials must be weak enough to control the average error.**

Independence is a particularly effective sufficient condition, but it is not the only possible hypothesis for a law of large numbers.

We will return to this question repeatedly when studying ergodic theory, martingales, and dependent stochastic processes.

---

## 2.5 What Does the Law of Large Numbers Answer, and What Does It Leave Open?

We have now proved an important conclusion:

\[
\widehat p_n\xrightarrow{P_p}p.
\]

At first sight, this seems to solve the problem of inferring an unknown probability.

If we observe enough trials, the empirical frequency will approach the true probability.

But a logical difficulty is hidden here.

The law of large numbers says:

> Assuming the true probability is \(p\), the empirical frequency is likely to be close to \(p\).

What we want to conclude is:

> I have observed an empirical frequency of \(0.7\), so the true probability should be close to \(0.7\).

These statements look similar, but they are not the same logical proposition.

One predicts observations from a model.

The other infers a model from observations.

We cannot simply reverse the direction of a conditional probability statement without proof.

### 2.5.1 How Can the Law of Large Numbers Become an Actual Method of Inference?

Fortunately, its probability inequality provides a more rigorous approach.

We proved earlier that

\[
P_p(|\widehat p_n-p|\ge\varepsilon)
\le\frac1{4n\varepsilon^2}.
\]

Notice that the inequality holds for every \(p\in[0,1]\).

Even without knowing \(p\), we can therefore prescribe an acceptable error probability \(\delta\in(0,1)\) in advance.

Set

\[
\varepsilon_n=\sqrt{\frac1{4n\delta}}.
\]

Then

\[
P_p\left(
|\widehat p_n-p|\le\varepsilon_n
\right)\ge1-\delta.
\]

Now define a random interval determined by the observed data:

\[
\boxed{
C_n=
\left[
\widehat p_n-\varepsilon_n,
\widehat p_n+\varepsilon_n
\right]\cap[0,1].
}
\]

For every true parameter \(p\), we then have

\[
\boxed{
P_p(p\in C_n)\ge1-\delta.
}
\]

This is a parameter-inference procedure with a rigorous coverage guarantee.

For example, suppose we make 100 independent tosses and observe 70 heads.

Take \(\delta=0.05\).

Then

\[
\varepsilon_{100}
=
\sqrt{\frac1{4(100)(0.05)}}
\approx0.224.
\]

giving the interval

\[
C_{100}\approx[0.476,0.924].
\]

This interval is indeed very wide.

Its advantage, however, is a coverage guarantee of at least 95%, obtained without any prior guess about the unknown \(p\).

Modern statistics can improve this substantially through sharper inequalities or exact binomial methods. This construction is intended only to make the mathematical principle clear.

### 2.5.2 A Subtle Philosophical Question

Now suppose we have indeed observed 70 heads and calculated this fixed interval.

Can we say:

“The probability that the true parameter lies in this interval is at least 95%”?

That interpretation does not follow directly within the mathematical framework just used.

The reason is that \(p\) is treated as a fixed but unknown parameter.

Before the experiment, the interval \(C_n\) is random. It may or may not contain the true parameter.

Once we observe particular data, however, the interval is determined.

Coverage means: **if we repeatedly use this construction in repeated experiments with the same true parameter, at least 95% of the intervals will contain it.**

It does not directly assign a 95% conditional probability to the already fixed parameter.

Yet from the practical human position of facing an unknown, another question is almost inevitable:

since we do not know \(p\), why can we not assign a probability to \(p\) itself?

For example:

\[
P(0.6<p<0.8\mid\text{observed data})=?
\]

This requires a mathematical structure different from the fixed-parameter model above.

The “unknown probability” itself must become an object of probabilistic inference.

Historically, Thomas Bayes took a crucial step in this direction.

---

## 2.6 Thomas Bayes: Can Probability Itself Be Uncertain?

![Thomas Bayes mathematician portrait historical engraved portrait](assets/images/13-01.img)

[Original image source](https://dun.unistra.fr/ipm/unit/bayesien/co/support_web.html)

**Thomas Bayes (c. 1701–1761)**

An English minister and mathematician.

After his death, Richard Price edited his paper *An Essay towards Solving a Problem in the Doctrine of Chances* and submitted it to the Royal Society. It appeared in the 1763 volume of the *Philosophical Transactions*.

The paper's starting point is remarkably close to our question.

Suppose an event has occurred a certain number of times and failed to occur a certain number of times.

Knowing only these observations, can we calculate the chance that its probability of occurrence lies between two given values?

Bayes studied precisely this kind of interval probability inference for an unknown success probability. 〔[15](#ref-turn557906search3), [16](#ref-turn310466search0), [17](#ref-turn310466search6)〕

A historical distinction is needed here.

The familiar Bayes formula,

\[
P(H\mid D)
=
\frac{P(D\mid H)P(H)}{P(D)},
\]

was not a conditional probability identity that first appeared in his paper wholly independently of earlier mathematical developments.

Bayes's important contribution was a concrete probabilistic analysis of the inverse problem of unknown chances.

Nor did he simply declare that “all unknown parameters should be uniformly distributed.” He constructed a physical model in which the random landing position of a ball generated an unknown probability, thereby giving his particular problem an initial probability structure. Historians have also discussed carefully the relationship between his original argument and later Bayesian thought. 〔[18](#ref-turn310466search24), [19](#ref-turn310466search26), [20](#ref-turn310466search8)〕

We now reconstruct this idea in modern probability language.

### 2.6.1 A New Experiment: First Choose the Coin's Bias at Random

Imagine that we design a device.

First, choose a number uniformly at random from \([0,1]\).

Call this number

\[
\Theta.
\]

Thus

\[
\Theta\sim\operatorname{Uniform}(0,1).
\]

Second, use the randomly chosen number to manufacture a coin whose probability of heads is exactly \(\Theta\).

Third, toss this coin many times independently.

Notice that we do not manufacture a new coin for every toss.

Once chosen, \(\Theta\) becomes the fixed bias of this coin.

We therefore obtain the following hierarchical model:

\[
\boxed{
\begin{aligned}
\Theta&\sim\operatorname{Uniform}(0,1),\\
X_i\mid\Theta=\theta
&\overset{\mathrm{i.i.d.}}{\sim}
\operatorname{Bernoulli}(\theta).
\end{aligned}
}
\]

There is an important difference between this model and the preceding section's.

Previously, \(p\) was a fixed but unknown number.

Now, \(\Theta\) is an actual random variable.

We can therefore legitimately ask:

\[
P(\Theta\in[a,b]).
\]

Before observing any data,

\[
P(\Theta\in[a,b])=b-a,
\qquad 0\le a\le b\le1.
\]

In modern terminology, this is called the prior distribution.

In our device, however, it does more than express subjective belief.

It has a clear physical interpretation: we actually generated an unknown parameter by a uniform random mechanism.

Assigning probabilities to unknown parameters therefore does not necessarily imply a subjective interpretation of probability; its meaning depends on how the model is constructed.

---

## 2.7 How Do Observations Change the Distribution of an Unknown Probability?

Now suppose we toss this coin ten times and observe seven heads.

Define

\[
S_{10}=X_1+\cdots+X_{10}.
\]

We know

\[
S_{10}=7.
\]

and want to calculate

\[
P(\Theta\in[a,b]\mid S_{10}=7).
\]

First, given \(\Theta=\theta\), the ten tosses are independent, so

\[
P(S_{10}=7\mid\Theta=\theta)
=
\binom{10}{7}\theta^7(1-\theta)^3.
\]

Now apply the idea of conditional probability.

If the prior density is \(\pi(\theta)\), then after observing data \(D\), the posterior density must satisfy

\[
\pi(\theta\mid D)
=
\frac{P(D\mid\theta)\pi(\theta)}
{\int_0^1P(D\mid u)\pi(u)\,du}.
\]

In our uniform-prior model,

\[
\pi(\theta)=1,\qquad 0<\theta<1.
\]

Hence

\[
\pi(\theta\mid S_{10}=7)
=
\frac{\theta^7(1-\theta)^3}
{\int_0^1u^7(1-u)^3\,du}.
\]

The denominator is a beta integral:

\[
\int_0^1u^7(1-u)^3\,du
=
B(8,4)
=
\frac{7!\,3!}{11!}.
\]

Therefore

\[
\boxed{
\Theta\mid S_{10}=7
\sim\operatorname{Beta}(8,4).
}
\]

This is a beautiful result.

We began without knowing the coin's bias.

After observing seven successes and three failures, we have not obtained a single definite parameter value.

Instead, we have obtained an entire probability distribution for the unknown parameter.

It describes **the conditional probability weights of different parameter values, given our prior model and the observed data.**

For the first time, we are treating probability as more than a tool for describing the outcomes of random experiments.

We are using it to describe uncertainty about the unknown law itself.

## 2.8 A Surprising Discovery: An Average over an Unknown Probability Can Predict the Future

We have obtained:

\[
\Theta\mid S_{10}=7\sim\operatorname{Beta}(8,4).
\]

What, then, is the probability of heads on the next toss?

A direct approach would use the observed frequency:

\[
\frac7{10}=0.7.
\]

But we now have the entire posterior distribution of \(\Theta\).

The conditional probability for the next toss satisfies

\[
P(X_{11}=1\mid\Theta=\theta,S_{10}=7)=\theta.
\]

By the conditional law of total probability,

\[
\begin{aligned}
P(X_{11}=1\mid S_{10}=7)
&=\int_0^1\theta\,
\pi(\theta\mid S_{10}=7)\,d\theta\\
&=\mathbb E[\Theta\mid S_{10}=7].
\end{aligned}
\]

The expectation of a beta distribution is

\[
\mathbb E[\Theta\mid S_{10}=7]
=
\frac8{8+4}.
\]

so

\[
\boxed{
P(X_{11}=1\mid S_{10}=7)=\frac23.
}
\]

This is not exactly \(0.7\).

Why?

Because we used not only the ten observations, but also the probability model for \(\Theta\) specified before observing them.

Under a uniform prior, after \(n\) trials with \(k\) successes,

\[
\Theta\mid S_n=k
\sim\operatorname{Beta}(k+1,n-k+1).
\]

Therefore

\[
\boxed{
P(X_{n+1}=1\mid S_n=k)
=
\frac{k+1}{n+2}.
}
\]

This expression is usually called Laplace's rule of succession. In modern form, it corresponds to the predictive beta–Bernoulli model with a uniform prior. Laplace further developed inverse-probability methods systematically in the late eighteenth and early nineteenth centuries. 〔[21](#ref-turn557906search12)〕

For example, if all ten tosses have been heads, the predictive probability of another head is

\[
\frac{11}{12}.
\]

rather than 1.

This is not a mathematical theorem saying that no coin can produce heads forever. It is the result of combining our chosen prior model with the observations.

We now see two different averages:

\[
\boxed{
\begin{aligned}
\text{empirical frequency：}&\quad \frac{k}{n},\\[3pt]
\text{posterior prediction：}&\quad \frac{k+1}{n+2}.
\end{aligned}
}
\]

and

\[
\frac{k+1}{n+2}-\frac{k}{n}
=
\frac{n-2k}{n(n+2)}.
\]

Thus

\[
\left|
\frac{k+1}{n+2}-\frac{k}{n}
\right|
\le\frac1{n+2}.
\]

As \(n\to\infty\), their difference tends to zero.

This seems to suggest a connection between empirical frequencies and Bayesian prediction in large samples.

Their actual relationship, however, goes deeper than this simple algebraic expression.

---

## 2.9 Why Have We Created Dependence?

We now encounter one of the chapter's most thought-provoking mathematical phenomena.

Recall our hierarchical model:

\[
\Theta\sim\operatorname{Uniform}(0,1),
\]

\[
X_i\mid\Theta
\overset{\mathrm{i.i.d.}}{\sim}
\operatorname{Bernoulli}(\Theta).
\]

Given \(\Theta\), all tosses are independent.

Without conditioning on \(\Theta\), are they still independent?

First calculate

\[
P(X_1=1).
\]

Integrating over the unknown parameter gives

\[
\begin{aligned}
P(X_1=1)
&=\int_0^1P(X_1=1\mid\Theta=\theta)\,d\theta\\
&=\int_0^1\theta\,d\theta\\
&=\frac12.
\end{aligned}
\]

Thus any single toss, considered on its own, has probability \(1/2\) of heads.

Now calculate the probability of two consecutive heads.

\[
\begin{aligned}
P(X_1=1,X_2=1)
&=\int_0^1
P(X_1=1,X_2=1\mid\Theta=\theta)\,d\theta\\
&=\int_0^1\theta^2\,d\theta\\
&=\frac13.
\end{aligned}
\]

If the tosses were independent, however, we would obtain

\[
P(X_1=1)P(X_2=1)=\frac14.
\]

In fact,

\[
\boxed{
P(X_1=1,X_2=1)=\frac13\ne\frac14.
}
\]

So they are not independent!

More surprisingly,

\[
\begin{aligned}
P(X_2=1\mid X_1=1)
&=\frac{P(X_1=1,X_2=1)}{P(X_1=1)}\\
&=\frac{1/3}{1/2}\\
&=\frac23.
\end{aligned}
\]

After observing heads on the first toss, our prediction for heads on the second rises from \(1/2\) to \(2/3\).

Why does this happen?

The first toss did not alter the physical structure of the coin.

But it changed our knowledge of the unknown \(\Theta\).

Since all tosses share the same \(\Theta\), a change in our knowledge of this common parameter changes our predictions for other tosses as well.

**Conditional independence does not imply unconditional independence.**

Covariance makes this structure clearer.

Since

\[
\mathbb E[X_i\mid\Theta]=\Theta,
\]

and, given \(\Theta\), the variables \(X_i,X_j\) are independent, for \(i\ne j\) we have

\[
\begin{aligned}
\operatorname{Cov}(X_i,X_j)
&=\mathbb E[X_iX_j]-\mathbb E[X_i]\mathbb E[X_j]\\
&=\mathbb E[\Theta^2]-(\mathbb E[\Theta])^2\\
&=\operatorname{Var}(\Theta).
\end{aligned}
\]

For the uniform distribution,

\[
\boxed{
\operatorname{Cov}(X_i,X_j)=\frac1{12}>0.
}
\]

The correlations among tosses in this model are therefore generated by their common unknown parameter.

This is an extremely important mathematical structure.

We began with simple conditionally independent trials. By mixing distributions associated with different parameters, we produced a random sequence that is dependent overall.

The sequence also has a special property.

For any positive integer \(n\) and any \(x_1,\ldots,x_n\in\{0,1\}\), let

\[
k=\sum_{i=1}^n x_i.
\]

Then

\[
\begin{aligned}
&P(X_1=x_1,\ldots,X_n=x_n)\\
&\qquad =
\int_0^1\theta^k(1-\theta)^{n-k}\,d\theta.
\end{aligned}
\]

The right-hand side depends only on the total number of successes \(k\), not on the particular order of successes and failures.

Thus, for every permutation \(\sigma\),

\[
\boxed{
(X_1,\ldots,X_n)
\overset d=
(X_{\sigma(1)},\ldots,X_{\sigma(n)}).
}
\]

We have obtained an exchangeable random sequence.

This is not independence, but it is a symmetry stronger than merely having identical marginal distributions.

We will return to this when studying de Finetti's theorem.

For infinite Bernoulli sequences, de Finetti's theorem will reveal a striking connection between exchangeability and mixtures of conditionally independent models.

For now, let us keep this discovery in mind.

It reveals a fact that was previously easy to overlook:

> **How we handle unknown structure within a random system can itself determine the dependence among the random variables we observe.**

---

## 2.10 Have We Merely Replaced “Not Knowing” with Another Assumption?

Our story seems complete.

We do not know the coin's true bias.

So we introduce a random parameter \(\Theta\).

After observing data, we calculate its posterior distribution using conditional probability.

Finally, we use the posterior to predict the future.

But what justified our initial assumption

\[
\Theta\sim\operatorname{Uniform}(0,1)
\]

in the first place?

In the earlier physical experiment, we explicitly specified a device that generated the parameter uniformly at random.

That distribution therefore had a basis in the model.

If instead we find a coin in the real world, we do not know how its bias arose.

Choosing a uniform prior then becomes a modeling decision requiring justification.

Even the word “uniform” is less simple than it seems.

Suppose that instead of \(\Theta\), we study

\[
U=\Theta^2.
\]

If \(\Theta\sim\operatorname{Uniform}(0,1)\), then for \(0\le u\le1\),

\[
\begin{aligned}
P(U\le u)
&=P(\Theta^2\le u)\\
&=P(\Theta\le\sqrt u)\\
&=\sqrt u.
\end{aligned}
\]

The density of \(U\) is therefore

\[
\boxed{
f_U(u)=\frac1{2\sqrt u},\qquad 0<u<1.
}
\]

This is clearly not uniform.

But if we had regarded \(U=\Theta^2\) as the appropriate parameter and assigned \(U\) a uniform prior, transforming back to \(\Theta\) would give a different prior distribution.

Thus:

\[
\boxed{
\text{the law of }\Theta\text{ is uniform}
\quad\not\Longleftrightarrow\quad
\text{the law of }\Theta^2\text{ is uniform}.
}
\]

This is more than a technical issue.

It reveals a deeper difficulty.

When claiming to have “no preference” about an unknown parameter, we must answer:

**With respect to which parameterization do we have no preference?**

In continuous spaces, uniformity is not a property that exists entirely independently of a measure and a coordinate description.

We intended a uniform prior to express lack of knowledge, only to discover that the expression itself depends on our chosen mathematical language.

This echoes the discussion of symmetry in Chapter 1.

When probability comes from physical symmetry, that symmetry can constrain the probability assignment.

But when probability expresses incomplete knowledge, we must ask why we should adopt a particular invariance principle.

This question will run through later objective Bayesian methods, parameter transformations, invariant measures, and statistical decision theory.

---

## 2.11 Bernoulli and Bayes: Are Their Ideas Really in Conflict?

We can finally reconsider the two questions with which this chapter began.

Bernoulli's approach assumes a fixed probability \(p\) and then asks whether repeated observations can estimate it.

In this framework, we study

\[
P_p\left(
|\widehat p_n-p|>\varepsilon
\right).
\]

A Bayesian hierarchical model instead first assigns a probability distribution to the unknown parameter, then updates it with data.

Here we study

\[
P(\Theta\in A\mid X_1,\ldots,X_n).
\]

The two approaches treat the “unknown parameter” differently in mathematical terms.

Yet they share an extremely important aim:

**Both seek to learn unknown laws gradually through observation.**

In the beta–Bernoulli model above, we can even see their connection directly.

Since, given \(\Theta=\theta\), the variables \(X_i\) are independent and identically distributed, the corresponding strong law of large numbers gives

\[
P\left(
\left.
\lim_{n\to\infty}\frac{S_n}{n}=\theta
\,\right|\,\Theta=\theta
\right)=1
\]

for prior-almost every \(\theta\).

Integrating over the distribution of \(\Theta\) yields

\[
\boxed{
\frac{S_n}{n}\xrightarrow{\mathrm{a.s.}}\Theta.
}
\]

On the other hand, we have already proved that the posterior mean satisfies

\[
\left|
\mathbb E[\Theta\mid S_n]-\frac{S_n}{n}
\right|
\le\frac1{n+2}.
\]

Therefore

\[
\boxed{
\mathbb E[\Theta\mid S_n]
\xrightarrow{\mathrm{a.s.}}\Theta.
}
\]

In this particular model, as observations accumulate, the posterior mean approaches the random parameter value that actually generated the data.

There is another structure here that was revealed systematically only later.

Since

\[
M_n=
\mathbb E[\Theta\mid X_1,\ldots,X_n],
\]

the tower property of conditional expectation gives

\[
\mathbb E[M_{n+1}\mid X_1,\ldots,X_n]=M_n.
\]

Thus \((M_n)\) is a bounded martingale.

This is a connection worth remembering.

We began by asking only how to predict the next toss.

Yet in modern probability theory, that very prediction process naturally becomes a martingale.

When we later study conditional expectation and stochastic processes, we will be able to reinterpret this chapter's calculations about learning and accumulating information.

---

# Closing Reflections: From Calculating Chance to Forming Knowledge

In Chapter 1, we asked:

**If the chances are known, how should we calculate outcomes?**

Chapter 2 took a further step:

**If the chances are unknown, can observation reveal them?**

Bernoulli found that independent repeated trials allow empirical frequencies to approach hidden probabilities in a stable way.

Bayes's inverse problem showed further that we can construct a probability model for an unknown probability and update our inferences through observation.

These two directions later developed into rich statistical traditions with long-running disagreements.

But together they reveal something.

Probability theory is more than the mathematics of chance outcomes.

It gradually becomes a mathematics of **how people acquire reliable knowledge in an uncertain world**.

“Reliable” does not mean that every inference must be correct. It means that we can state clearly which assumptions an inference depends on, what probabilistic guarantees it has, and how it might fail.

Yet one difficulty in our story remains unresolved.

We proved:

\[
\frac{S_n}{n}\xrightarrow{P}p.
\]

This says only that the probability of a deviation beyond a fixed accuracy tends to zero.

It does not tell us:

when \(n\) is large but finite, how exactly does the empirical frequency fluctuate around \(p\)?

To predict those fluctuations more precisely, we must study

\[
\sqrt n(\widehat p_n-p).
\]

Why does \(\sqrt n\) appear?

Why do so many apparently different random phenomena show nearly the same distributional shape after appropriate standardization?

This brings us to another major discovery in the history of probability:

**the normal distribution and the central limit theorem.**

Before continuing, however, we must trace an older mathematical question: why do the binomial coefficients

\[
\binom nk
\]

produce an approximately bell-shaped curve in repeated trials? And why can that curve eventually extend beyond dice, coins, and the binomial distribution to become an important tool for describing natural errors?

Next: Chapter 3, “The Birth of the Bell Curve—From the Binomial to the Normal Distribution”

The Mathematics of Chance · Volume I, Chapter 2 · Working draft v0.1


---

# The Mathematics of Chance
Volume I · Can Chance Be Calculated?

# Chapter 3: The Birth of the Bell Curve—Why Do Countless Random Phenomena Approach the Same Distribution?

From Abraham de Moivre's binomial approximation to Laplace's general limit theorem, and then to Gauss's theory of errors.

By the end of Chapter 2, we had learned something surprising:

If \(X_1,X_2,\ldots\) are independent, identically distributed Bernoulli\((p)\) random variables, then

\[
\frac1n\sum_{i=1}^nX_i\xrightarrow{P}p.
\]

In other words, a large number of repeated random experiments exhibits an increasingly stable regularity.

But a closer look reveals that this is only half the story.

The law of large numbers tells us where a random average will eventually go, but does not fully explain how it fluctuates on its way to that limit.

Suppose we know that a coin is fair.

After ten thousand tosses, five thousand heads would clearly be perfectly ordinary.

But what about five thousand one hundred heads?

Five thousand two hundred?

Five thousand five hundred?

Of course, we can calculate the exact probability of each outcome. But if the number of repetitions reaches a million, a billion, or more, calculating the binomial coefficients directly becomes extraordinarily cumbersome.

A new mathematical question therefore arises:

**Can we find a mathematical law that approximately describes the entire shape of the random fluctuations, without calculating every possible outcome separately?**

This question eventually led mathematicians to discover one of the most famous functions in probability theory:

\[
\boxed{
\varphi(x)=\frac1{\sqrt{2\pi}}e^{-x^2/2}.
}
\]

Today we call this the standard normal density.

But we will not simply introduce it as a definition.

We want to understand why calculations involving coins and binomial coefficients led mathematicians to an expression containing the exponential function and the constant pi.

In particular:

**Why should \(\pi\) ultimately appear in a random experiment that has nothing to do with circles?**

---

## 3.1 Bernoulli's Unfinished Question: Knowing That the Error Vanishes Is Not Enough

Suppose

\[
S_n=X_1+\cdots+X_n,
\qquad
X_i\overset{\mathrm{i.i.d.}}{\sim}\operatorname{Bernoulli}(1/2).
\]

We know that

\[
S_n\sim\operatorname{Binomial}(n,1/2).
\]

Thus

\[
P(S_n=k)=\binom nk2^{-n}.
\]

For even \(n\), the most likely outcome is

\[
k=\frac n2.
\]

because

\[
\frac{P(S_n=k+1)}{P(S_n=k)}
=
\frac{n-k}{k+1}.
\]

When \(k\) lies to the left of the center, successive probabilities tend to increase; after passing the center, they begin to decrease.

The shape of the binomial distribution must therefore be as follows:

It rises gradually from the left, reaches its maximum in the middle, and then falls to the right.

But this is only a qualitative description.

We still do not know precisely how fast it rises and falls.

First consider a somewhat counterintuitive fact.

As \(n\) increases, the empirical frequency

\[
\widehat p_n=\frac{S_n}{n}
\]

gets closer and closer to \(1/2\).

Yet the probability of obtaining exactly half heads,

\[
P(S_n=n/2)
\]

does not approach 1.

In fact, we will prove that it approaches 0 instead.

This means that

\[
\boxed{
\text{getting closer to the center}
\ne
\text{becoming more likely to equal the center exactly}.
}
\]

Why?

Because as the number of experiments increases, the relative error shrinks, while the absolute fluctuations in the number of successes grow.

We already know that

\[
\operatorname{Var}(S_n)=\frac n4,
\]

so

\[
\operatorname{SD}(S_n)=\frac{\sqrt n}{2}.
\]

The typical scale of fluctuations in the number of successes is \(\sqrt n\), rather than a fixed constant.

As the number of tosses grows, the probability mass therefore spreads across an increasing number of integers near the center.

The probability of any single integer may shrink, while the total probability of a suitably expanding central region can remain high.

This is precisely the structure we will study next.

---

## 3.2 Abraham de Moivre: How Can We Calculate an Almost Incalculable Binomial Expression?

![Historical illustration from the original manuscript](assets/images/09-01.img)

[Original image source](https://prints.royalsociety.org/collections/vintage-mathematics-prints-and-parabola-drawings/products/portrait-of-abraham-de-moivre-1667-1754-rs-9548?utm_source=chatgpt.com)

**Abraham de Moivre（1667—1754）**

A French-born mathematician who later spent much of his life in Britain. In addition to probability, he studied trigonometric analysis and the mathematics of annuities.

In 1733, he wrote the Latin paper *Approximatio ad Summam Terminorum Binomii* on sums of terms in high powers of a binomial. An English version appeared in the second edition of *The Doctrine of Chances* in 1738.

The problem de Moivre faced was very concrete.

In the expansion of a high power of a binomial, we can write every term exactly:

\[
(a+b)^n
=
\sum_{k=0}^n\binom nk a^kb^{n-k}.
\]

But when \(n\) is large, calculating the sum of many neighboring terms becomes very difficult.

And probability problems frequently require exactly this kind of summation.

For example, when \(p=1/2\),

\[
P(a\le S_n\le b)
=
2^{-n}\sum_{k=a}^b\binom nk.
\]

In his 1733 work, de Moivre investigated how a continuous mathematical expression could approximate these sums of binomial coefficients. His main early breakthrough concerned the symmetric binomial distribution; Laplace later extended the underlying ideas considerably. 〔[22](#ref-turn234816search0), [23](#ref-turn234816search4), [24](#ref-turn234816search30)〕

We will now follow his central idea and reconstruct the derivation using modern asymptotic analysis.

### 3.2.1 Begin with the Central Term

To simplify the notation, let

\[
n=2m.
\]

Then

\[
P(S_{2m}=m)
=
\binom{2m}{m}2^{-2m}
=
\frac{(2m)!}{(m!)^2\,4^m}.
\]

Calculating the factorials directly is inconvenient.

But we can use Stirling's formula:

\[
\boxed{
n!\sim\sqrt{2\pi n}\left(\frac ne\right)^n.
}
\]

Here the notation

\[
a_n\sim b_n
\]

means

\[
\lim_{n\to\infty}\frac{a_n}{b_n}=1.
\]

This formula has a history well worth studying in its own right. Both de Moivre and James Stirling made important contributions to factorial asymptotics, and identifying the correct constant \(\sqrt{2\pi}\) was a crucial step. 〔[25](#ref-turn234816search3)〕

Now substitute it into the central binomial coefficient.

\[
(2m)!\sim\sqrt{4\pi m}\left(\frac{2m}{e}\right)^{2m},
\]

\[
(m!)^2\sim 2\pi m\left(\frac me\right)^{2m}.
\]

Therefore

\[
\begin{aligned}
P(S_{2m}=m)
&=\frac{(2m)!}{(m!)^2\,4^m}\\
&\sim
\frac{
\sqrt{4\pi m}(2m/e)^{2m}
}{
2\pi m(m/e)^{2m}4^m
}\\
&=\frac1{\sqrt{\pi m}}.
\end{aligned}
\]

Since \(n=2m\), we can also write

\[
\boxed{
P(S_n=n/2)\sim\sqrt{\frac2{\pi n}}.
}
\]

We have at last reached an important conclusion.

The probability of obtaining exactly half heads is of order

\[
\frac1{\sqrt n}.
\]

Hence

\[
P(S_n=n/2)\longrightarrow0.
\]

This explains the apparently contradictory phenomenon raised at the beginning of the chapter.

But the probability at the center alone does not tell us the shape of the whole distribution.

We must go on to ask:

How large are the terms a certain distance from the center, compared with the central term?

### 3.2.2 Moving Away from the Center

Again let \(n=2m\).

Define

\[
p_m(j)=P(S_{2m}=m+j).
\]

By symmetry,

\[
p_m(j)=p_m(-j).
\]

so we need only consider \(j\ge0\).

The relation between binomial coefficients gives

\[
\frac{p_m(j)}{p_m(0)}
=
\frac{\binom{2m}{m+j}}{\binom{2m}{m}}.
\]

Simplifying yields

\[
\frac{p_m(j)}{p_m(0)}
=
\frac{m!\,m!}{(m+j)!(m-j)!}.
\]

Expanding this further as a product,

\[
\boxed{
\frac{p_m(j)}{p_m(0)}
=
\prod_{r=1}^j\frac{m-r+1}{m+r}.
}
\]

This expression is intriguing.

We have transformed a ratio of enormous binomial coefficients into a product of factors close to 1.

How can we analyze the product of many numbers close to 1?

Taking logarithms is a natural choice.

Logarithms turn products into sums:

\[
\log\frac{p_m(j)}{p_m(0)}
=
\sum_{r=1}^j
\log\left(\frac{m-r+1}{m+r}\right).
\]

Write each term as

\[
\log\left(1-\frac{r-1}{m}\right)
-
\log\left(1+\frac rm\right).
\]

Now use the Taylor expansion

\[
\log(1+x)=x-\frac{x^2}{2}+O(x^3),
\]

valid for \(x\) near 0.

Provided \(j\) does not grow too quickly relative to \(m\), we can control all these expansions.

For \(j=O(\sqrt m)\), the leading terms after summation are

\[
\begin{aligned}
\log\frac{p_m(j)}{p_m(0)}
&=
-\frac1m\sum_{r=1}^j(2r-1)+o(1)\\
&=-\frac{j^2}{m}+o(1).
\end{aligned}
\]

Here we have used

\[
\sum_{r=1}^j(2r-1)=j^2.
\]

Consequently,

\[
\frac{p_m(j)}{p_m(0)}
\sim e^{-j^2/m}.
\]

Combining this with the approximation to the central term,

\[
p_m(0)\sim\frac1{\sqrt{\pi m}},
\]

we finally obtain

\[
\boxed{
P(S_{2m}=m+j)
\sim
\frac1{\sqrt{\pi m}}e^{-j^2/m}
}
\]

where \(j=O(\sqrt m)\). More precisely, the approximation errors can be controlled uniformly over any fixed central window \(|j|\le C\sqrt m\).

Here a completely new functional form suddenly appears:

\[
e^{-j^2/m}.
\]

We did not assume a normal distribution.

We have not even discussed continuous probability densities.

**The squared term in the exponent arises naturally from the structure of binomial coefficients and the Taylor expansion of the logarithm.**

This is the mathematical origin of the bell curve.

## 3.3 Why Must We Standardize by \(\sqrt n\)?

We have just derived

\[
P(S_{2m}=m+j)
\approx
\frac1{\sqrt{\pi m}}e^{-j^2/m}.
\]

An important question now arises.

If we let \(m\to\infty\) while keeping \(j\) fixed, then

\[
\frac{j^2}{m}\to0.
\]

and therefore

\[
e^{-j^2/m}\to1.
\]

This means that, for fixed \(j\), the probabilities at different positions near the center gradually become almost equal.

We would then lose sight of the distribution's actual shape.

We must therefore find the right scale of observation.

Look at the exponent

\[
\frac{j^2}{m}.
\]

If it is to retain nontrivial variation as \(m\to\infty\), we should take

\[
j\asymp\sqrt m.
\]

This is why the square-root scale appears naturally.

It does not come from knowing the definition of standard deviation in advance, or from trying to force a normal distribution to appear.

It comes from the fact that only at this scale do the relative probabilities near the center of the binomial distribution have a nontrivial limiting shape.

Now define

\[
Z_n=\frac{S_n-n/2}{\sqrt n/2}.
\]

This subtracts the expected number of successes and divides by the standard deviation.

When \(n=2m\) and \(S_n=m+j\),

\[
Z_n=\frac{2j}{\sqrt n}.
\]

Let

\[
z=\frac{2j}{\sqrt n}.
\]

Then

\[
\frac{j^2}{m}=\frac{z^2}{2}.
\]

The earlier approximation therefore becomes

\[
P\left(Z_n=z\right)
\approx
\sqrt{\frac2{\pi n}}e^{-z^2/2},
\]

where \(z\) must be a lattice value that \(Z_n\) can actually take.

The distance between adjacent lattice points is

\[
\Delta z=\frac2{\sqrt n}.
\]

Thus

\[
\begin{aligned}
P(Z_n=z)
&\approx
\frac2{\sqrt n}\cdot
\frac1{\sqrt{2\pi}}e^{-z^2/2}\\
&=\Delta z\,\varphi(z).
\end{aligned}
\]

where

\[
\boxed{
\varphi(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2}.
}
\]

Now the picture becomes particularly clear.

The original binomial distribution consists of discrete probability masses.

But as \(n\to\infty\), the spacing between successive standardized values shrinks.

The probability mass at each value is approximately

\[
\text{interval width}\times\text{height of a continuous function}.
\]

We have found that continuous function:

\[
\varphi(z).
\]

This is the mathematical process by which the bell curve emerges from discrete probability.

### 3.3.1 Watching the Bell Curve Emerge

Below, the binomial probability masses for different values of \(n\) are divided by the lattice spacing and compared with the standard normal density.

<div class="numeric-chart" data-chart="1"></div>

The lines connecting discrete lattice points in the figure serve only as a visual comparison; they do not mean that the binomial distribution itself has a continuous density.

As \(n\) increases, the correctly standardized discrete probability masses approach the same continuous function.

There is another point worth noticing.

We have not changed the coin itself.

Every toss still has only two outcomes: heads and tails.

**The continuous bell curve is not the shape of an individual random experiment. It is a limiting structure that emerges when many discrete random outcomes are added and rescaled.**

---

## 3.4 From Sums of Binomial Coefficients to Integrals

We now have a local approximation:

\[
P(Z_n=z_{n,k})
\approx
\Delta z_n\,\varphi(z_{n,k}),
\]

where

\[
z_{n,k}=\frac{k-n/2}{\sqrt n/2},
\qquad
\Delta z_n=\frac2{\sqrt n}.
\]

But de Moivre's original goal was not merely to approximate a single binomial coefficient.

He was interested in sums of many terms.

Take any fixed real numbers \(a<b\).

We want to calculate

\[
P(a\le Z_n\le b).
\]

By definition,

\[
P(a\le Z_n\le b)
=
\sum_{\substack{k:\\a\le z_{n,k}\le b}}
P(Z_n=z_{n,k}).
\]

Using the approximation just obtained,

\[
P(a\le Z_n\le b)
\approx
\sum_{\substack{k:\\a\le z_{n,k}\le b}}
\varphi(z_{n,k})\Delta z_n.
\]

Now look carefully at the right-hand side.

Does it look familiar?

It is precisely a Riemann sum.

As \(n\to\infty\),

\[
\Delta z_n=\frac2{\sqrt n}\to0.
\]

We should therefore obtain

\[
\boxed{
\lim_{n\to\infty}P(a\le Z_n\le b)
=
\int_a^b
\frac1{\sqrt{2\pi}}e^{-z^2/2}\,dz.
}
\]

This is the de Moivre–Laplace limit theorem for symmetric Bernoulli random variables.

A point about rigor is necessary here.

An approximation near each fixed location does not, by itself, justify interchanging an infinite sum and a limit.

What we need is for the relative errors in the local probability approximation to tend to zero uniformly over the fixed standardized interval \([a,b]\).

The asymptotic expansion obtained earlier over the range \(|j|\le C\sqrt n\) provides exactly this control.

The limit can therefore be deduced rigorously from the Riemann sums.

### 3.4.1 Why Does the Normal Density Integrate to 1?

We have not yet explained why

\[
\frac1{\sqrt{2\pi}}
\]

is the correct normalizing constant.

For \(\varphi\) to be a probability density, it must satisfy

\[
\int_{-\infty}^{\infty}\varphi(x)\,dx=1.
\]

We therefore need to calculate

\[
I=\int_{-\infty}^{\infty}e^{-x^2/2}\,dx.
\]

This integrand has no elementary antiderivative, but the definite integral can be evaluated exactly.

Consider

\[
I^2
=
\int_{\mathbb R^2}
e^{-(x^2+y^2)/2}\,dx\,dy.
\]

We have moved from one dimension to two.

Switch to polar coordinates:

\[
x=r\cos\theta,
\qquad
y=r\sin\theta.
\]

The Jacobian is \(r\), so

\[
\begin{aligned}
I^2
&=
\int_0^{2\pi}\int_0^\infty
e^{-r^2/2}r\,dr\,d\theta\\
&=2\pi\left[-e^{-r^2/2}\right]_0^\infty\\
&=2\pi.
\end{aligned}
\]

Therefore

\[
I=\sqrt{2\pi}.
\]

and hence

\[
\boxed{
\int_{-\infty}^{\infty}
\frac1{\sqrt{2\pi}}e^{-x^2/2}\,dx=1.
}
\]

We can finally answer one of the questions from the beginning of the chapter:

Why does \(\pi\) appear in the limiting distribution of coin tosses?

Because the asymptotic structure of binomial coefficients near their center produces an exponential of a quadratic, and the normalization of this function is closely tied to circular symmetry in two-dimensional Euclidean space.

Pi is not a physical property of the coin.

It is a geometric constant of the continuous mathematical structure we ultimately encounter.

This is a beautiful unification within probability theory:

**Through limits, finite combinatorics leads to calculus; geometric symmetry within the integral then determines the normalizing constant of the probability distribution.**

---

## 3.5 Laplace: Why Should the Bell Curve Belong Only to Coins?

We have now understood a special result:

\[
\frac{S_n-n/2}{\sqrt n/2}
\xrightarrow{d}N(0,1).
\]

Here \(N(0,1)\) denotes the standard normal distribution, and \(\xrightarrow d\) denotes convergence in distribution.

But an even more exciting question arises:

**Why should we study only heads and tails?**

Suppose we roll dice instead of tossing coins.

Or observe temperature errors each day.

Or study the total error produced by the accumulation of many small disturbances.

The distributions of these individual random variables may be very different from a symmetric binomial distribution.

Will their standardized sums still approach the same bell curve?

![Pierre Simon Laplace portrait 19th century painting mathematician](assets/images/10-01.img)

[Original image source](https://www.meisterdrucke.com/kunstdrucke/Sophie-Feytaud/1632777/Portr%C3%A4t-von-Pierre-Simon%2C-Marquis-de-Laplace-%281745-1827%29.html)

**Pierre-Simon Laplace（1749—1827）**

A French mathematician and astronomer.

Laplace developed probability calculations into a more general analytical theory. In particular, in his work around 1810 and in *Théorie analytique des probabilités*, published in 1812, he studied approximations to random sums far more general than those arising from the symmetric binomial distribution.

The passage from de Moivre's special approximation to a general central limit theorem involved a long mathematical development, rather than a simple change of symbols. Laplace's work was a pivotal part of that history. 〔[26](#ref-turn234816search8), [27](#ref-turn234816search6), [28](#ref-turn523153search2)〕

We now study this extension in modern mathematical language.

Let

\[
X_1,X_2,\ldots
\]

be independent, identically distributed random variables, and assume

\[
\mathbb E[X_i]=\mu,
\]

\[
0<\operatorname{Var}(X_i)=\sigma^2<\infty.
\]

They may be discrete or continuous.

Their distribution may be symmetric or skewed.

We do not assume that they have a bell-shaped density.

Now define

\[
S_n=X_1+\cdots+X_n.
\]

By linearity of expectation,

\[
\mathbb E[S_n]=n\mu.
\]

By independence,

\[
\operatorname{Var}(S_n)=n\sigma^2.
\]

The most natural standardization is therefore

\[
Z_n=\frac{S_n-n\mu}{\sigma\sqrt n}.
\]

The same \(\sqrt n\) appears here as in the coin-tossing problem.

This already suggests a more general structure.

Under these assumptions, the modern Lindeberg–Lévy central limit theorem tells us that

\[
\boxed{
\frac{S_n-n\mu}{\sigma\sqrt n}
\xrightarrow{d}N(0,1).
}
\]

Take a moment to appreciate this conclusion.

Each \(X_i\) on the left may have any of a wide variety of distributional shapes.

Yet after independent summation, centering, and standardization, their limiting distribution is the same \(N(0,1)\).

This is universality in a substantive probabilistic sense.

In a sense, the accumulation of many random influences makes the final distribution lose much of the detail about the individual influences.

In the independent, identically distributed model with finite variance, the scale information retained by the limit is primarily determined by the mean and variance.

Why does this happen?

We must still explain the mechanism.

---

## 3.6 The Central Limit Theorem's Real Secret: Why Do the Details of a Distribution Disappear?

> Editorial supplement: Appendix D controls the remainder in the second-order expansion of the characteristic function; no third-moment assumption is added here.

We already know how to derive the normal distribution from the binomial expansion.

But if \(X_i\) have an entirely different distribution, the binomial-coefficient method no longer applies.

We need a new mathematical language.

This problem will lead us to the deep connection between probability theory and Fourier analysis.

### 3.6.1 Why Study Complex Exponentials?

Suppose the distribution of a random variable \(X\) is very complicated.

Studying the distribution of its independent sum

\[
S_n=X_1+\cdots+X_n
\]

directly usually involves repeated convolution.

For example, if \(X,Y\) are independent with densities \(f_X,f_Y\), then

\[
f_{X+Y}(z)
=
\int_{\mathbb R}f_X(x)f_Y(z-x)\,dx.
\]

For \(n\) random variables, we must convolve repeatedly.

This is a fairly complicated operation.

But mathematicians had already found in other settings that certain functional transforms turn complicated operations into simple algebra.

Define the characteristic function of a random variable \(X\) by

\[
\boxed{
\phi_X(t)=\mathbb E[e^{itX}],
\qquad t\in\mathbb R.
}
\]

The definition may seem rather unexpected.

Why introduce the imaginary unit \(i\)?

Why choose the exponential function in particular?

Because it has a very useful property:

\[
e^{it(x+y)}=e^{itx}e^{ity}.
\]

Thus, if \(X,Y\) are independent,

\[
\begin{aligned}
\phi_{X+Y}(t)
&=\mathbb E[e^{it(X+Y)}]\\
&=\mathbb E[e^{itX}e^{itY}]\\
&=\mathbb E[e^{itX}]\mathbb E[e^{itY}]\\
&=\phi_X(t)\phi_Y(t).
\end{aligned}
\]

and consequently

\[
\boxed{
\phi_{X+Y}(t)=\phi_X(t)\phi_Y(t).
}
\]

We have turned addition of random variables into multiplication of characteristic functions.

The idea resembles our earlier use of logarithms to turn products into sums:

**When faced with a complicated operation, seek a representation in which its difficult structure becomes a simple algebraic relation.**

> Dependencies on later theory: The following is a reconstruction of historical results in modern language, not de Moivre's or Laplace's original proof. Appendix D controls the remainder in the second-order expansion; Chapter 6 develops integration for complex-valued random variables; Chapters 9 and 11 systematically prove uniqueness of characteristic functions and Lévy's continuity theorem. Chapter 7 first distinguishes the relevant notions of convergence. This section continues the story through products and second-order terms, without presenting these outside results as if they had been proved here.

### 3.6.2 Proving the Central Limit Theorem Again with Characteristic Functions

Let

\[
Y_i=\frac{X_i-\mu}{\sigma}.
\]

Then

\[
\mathbb E[Y_i]=0,
\qquad
\mathbb E[Y_i^2]=1.
\]

The standardized random sum can be written as

\[
Z_n=\frac1{\sqrt n}\sum_{i=1}^nY_i.
\]

We now examine the characteristic function of \(Y_i\) near \(t=0\).

Using

\[
e^{ity}=1+ity-\frac{t^2y^2}{2}+\cdots,
\]

we expect

\[
\phi_Y(t)
=
1+it\mathbb E[Y]
-\frac{t^2}{2}\mathbb E[Y^2]
+o(t^2).
\]

Since the mean is 0 and the variance is 1,

\[
\boxed{
\phi_Y(t)=1-\frac{t^2}{2}+o(t^2).
}
\]

We do not need to assume that \(Y\) has a third moment.

A finite second moment suffices for this expansion. A rigorous proof can use

\[
\frac{e^{iu}-1-iu}{u^2}\longrightarrow-\frac12
\]

and the corresponding boundedness to control the expectation and obtain the second-order expansion.

Now, because \(Y_1,\ldots,Y_n\) are independent,

\[
\begin{aligned}
\phi_{Z_n}(t)
&=
\prod_{i=1}^n
\phi_{Y_i}\left(\frac{t}{\sqrt n}\right)\\
&=
\left[
\phi_Y\left(\frac{t}{\sqrt n}\right)
\right]^n.
\end{aligned}
\]

Using the Taylor expansion above,

\[
\phi_Y\left(\frac{t}{\sqrt n}\right)
=
1-\frac{t^2}{2n}+o\left(\frac1n\right).
\]

Therefore

\[
\phi_{Z_n}(t)
=
\left[
1-\frac{t^2}{2n}+o\left(\frac1n\right)
\right]^n.
\]

Recall the elementary limit

\[
\left(1+\frac an+o\left(\frac1n\right)\right)^n
\longrightarrow e^a.
\]

It follows that

\[
\boxed{
\lim_{n\to\infty}\phi_{Z_n}(t)
=
e^{-t^2/2}.
}
\]

But

\[
e^{-t^2/2}
\]

is precisely the characteristic function of a standard normal random variable.

The continuity theorem for characteristic functions therefore gives

\[
\boxed{Z_n\xrightarrow d N(0,1).}
\]

This completes the proof.

This modern proof differs from de Moivre's and Laplace's original derivations, but reveals the central mathematical mechanism of the central limit theorem.

### 3.6.3 Why Does Only the Second-Order Term Survive?

Look again at

\[
\phi_Y(t)=1-\frac{t^2}{2}+o(t^2).
\]

When standardizing the sum, we replace \(t\) by \(t/\sqrt n\).

The second-order term becomes

\[
\frac{t^2}{n}.
\]

Multiplying the characteristic functions of \(n\) independent random variables produces a nontrivial limit:

\[
n\cdot\frac{t^2}{n}=t^2.
\]

Under suitable moment conditions, the higher-order terms gradually disappear.

For example, if the third moment exists, the accumulated third-order contribution is of order

\[
n\left(\frac t{\sqrt n}\right)^3
=
\frac{t^3}{\sqrt n}
\to0.
\]

The fourth-order term gives

\[
n\left(\frac t{\sqrt n}\right)^4
=
\frac{t^4}{n}
\to0.
\]

Thus only the second-order structure survives in the limit.

This explains why independent sums from many different distributions have the same limit.

We do not need to know every detail of each distribution.

At this limiting scale, many higher-order details become invisible.

And the characteristic function supplied by the second-order term,

\[
e^{-t^2/2}
\]

corresponds precisely to the normal distribution.

The central limit theorem therefore does much more than happen to announce that sums of many random variables “look bell-shaped.”

It expresses the following mathematical principle:

**Independent summation and square-root standardization preserve second-order structure in the limit while diminishing other local details.**

This is a central reason for the universality of the normal distribution.

---

## 3.7 Gauss: Why Do Astronomers Also Encounter the Bell Curve?

So far, we have discovered the normal distribution by following a path through gambling, binomial expressions, and independent random sums.

Historically, another important path led to the same function.

It began not with dice,

but with measurement errors in astronomy.

![Carl Friedrich Gauss portrait 1840s painting mathematician astronomer](assets/images/11-01.img)

[Original image source](https://www.meisterdrucke.it/stampe-d-arte/Christian-Albrecht-Jensen/175614/Ritratto-di-Carl-Friedrich-Gauss%2C-1840.html)

**Carl Friedrich Gauss（1777—1855）**

A German mathematician and astronomer.

In *Theoria Motus Corporum Coelestium* (1809), he discussed celestial orbits and observational errors, and established an important connection between normally distributed errors and least-squares estimation.

Legendre had already published the method of least squares in 1805; Robert Adrain independently studied the normal law of errors in 1808. Simply attributing the discovery of the normal distribution to Gauss alone therefore misrepresents its mathematical history. 〔[27](#ref-turn234816search6), [29](#ref-turn523153search1), [30](#ref-turn234816search7)〕

Yet Gauss's argument contains an idea that deserves close attention:

Why, when repeatedly measuring the same unknown quantity, do we tend to use the arithmetic mean as an estimate?

For example, suppose we measure an unknown length \(\theta\) and obtain

\[
Y_1,\ldots,Y_n.
\]

Assume

\[
Y_i=\theta+\varepsilon_i,
\]

where \(\varepsilon_i\) are measurement errors.

The mathematician wants to recover \(\theta\) from these imperfect observations.

A natural method is to average:

\[
\widehat\theta=\frac1n\sum_{i=1}^nY_i.
\]

But why should the average be the right estimate?

Can we reverse the question?

**If we require the arithmetic mean to be the most likely estimate, what form must the probability distribution of the errors take?**

> Reading route: Returning to Gauss's problem of errors and estimation gives another historical source of the Gaussian law; it does not imply that Gauss worked after the modern characteristic-function proof. The functional-equation argument below is a modern reconstruction. The linearity of measurable additive functions remains a tool to be supplied later, and the related regularity questions are retained in the review issue register.

### 3.7.1 Recovering a Probability Distribution from an Optimal Estimate

Assume the errors \(\varepsilon_i\) are independent and identically distributed, with an everywhere positive, differentiable density \(f\).

Given observations \(y_1,\ldots,y_n\), the likelihood function for the parameter \(\theta\) is

\[
L(\theta)=\prod_{i=1}^n f(y_i-\theta).
\]

We now impose a strong assumption:

Whatever the sample and whatever its size, the arithmetic mean

\[
\overline y=\frac1n\sum_{i=1}^ny_i
\]

should be a maximum likelihood estimate.

Let us see what constraints this places on the density \(f\).

For convenience, let

\[
\psi(x)=\frac{f'(x)}{f(x)}.
\]

Differentiate the log-likelihood:

\[
\frac{d}{d\theta}\log L(\theta)
=
-\sum_{i=1}^n\psi(y_i-\theta).
\]

If the maximum occurs at \(\theta=\overline y\), the first-order condition requires

\[
\sum_{i=1}^n\psi(y_i-\overline y)=0.
\]

Let

\[
r_i=y_i-\overline y.
\]

Notice that

\[
\sum_{i=1}^nr_i=0.
\]

Our assumption therefore implies that

for every set of residuals satisfying \(\sum r_i=0\), we have

\[
\boxed{\sum_{i=1}^n\psi(r_i)=0.}
\]

First consider \(n=2\).

Taking residuals \(x,-x\) gives

\[
\psi(x)+\psi(-x)=0.
\]

Thus \(\psi\) is odd.

Next consider \(n=3\).

Take the residuals

\[
x,\quad y,\quad -(x+y).
\]

Then

\[
\psi(x)+\psi(y)+\psi(-(x+y))=0.
\]

Using oddness,

\[
\boxed{
\psi(x+y)=\psi(x)+\psi(y).
}
\]

This is Cauchy's functional equation!

Under a suitable regularity assumption, such as continuity, we have

\[
\psi(x)=cx
\]

for some constant \(c\).

But since

\[
\psi(x)=\frac{f'(x)}{f(x)},
\]

we obtain

\[
\frac{d}{dx}\log f(x)=cx.
\]

Integrating gives

\[
\log f(x)=\frac c2x^2+C.
\]

and hence

\[
f(x)=Ae^{cx^2/2}.
\]

For \(f\) to be an integrable probability density on the whole real line, we must have

\[
c<0.
\]

Let

\[
c=-\frac1{\sigma^2},
\]

Then

\[
f(x)=Ae^{-x^2/(2\sigma^2)}.
\]

Normalization gives

\[
\boxed{
f(x)=
\frac1{\sqrt{2\pi}\sigma}
e^{-x^2/(2\sigma^2)}.
}
\]

Once again, we have obtained the normal density!

This time, however, it did not arise as a limit of binomial coefficients.

It arose from a requirement on an estimation method:

**In the independent, identically distributed error model above, under the stated regularity conditions, requiring the arithmetic mean to be a maximum likelihood estimate for every sample leads to normally distributed errors.**

This is a modern reconstruction of Gauss's line of reasoning in 1809. It does not prove that all real-world observational errors are normally distributed; it shows a special relationship between a certain optimality requirement for the average and the normal model. 〔[30](#ref-turn234816search7)〕

Going further, we can understand why least squares is so closely connected with the normal distribution.

In the normal error model, apart from constants independent of \(\theta\) and a positive scaling factor, the negative log-likelihood is precisely

\[
\sum_{i=1}^n(y_i-\theta)^2.
\]

Maximizing the likelihood is the same as minimizing the squared error.

Thus

\[
\boxed{
\text{normal error model}
\Longrightarrow
\text{least squares and maximum likelihood are connected}.
}
\]

Mathematical methods that arose historically from different problems acquire a unified explanation here.

---

## 3.8 Must Every Random Phenomenon Eventually Become Normally Distributed?

By this point, the normal distribution may seem capable of everything.

The sum of coin tosses approaches a normal distribution.

Standardized sums of general independent random variables also approach a normal distribution.

The analysis of measurement errors again produces the normal density.

Should we conclude that the normal distribution is the inevitable final form of random phenomena?

No.

The central limit theorem has very specific assumptions.

When those assumptions fail, its conclusion may be entirely different.

Let us consider a particularly important example.

> Dependencies on later theory: This example still uses as known results the characteristic-function formula and the identification of distributions by characteristic functions. The calculation and uniqueness theory are scheduled for Chapter 9; presenting a counterexample here does not mean that the corresponding theory has already been established.

### 3.8.1 The Cauchy Distribution: A Random Variable That Averaging Cannot Tame

Let

\[
X_1,X_2,\ldots
\]

be independent and identically distributed, each with the standard Cauchy distribution:

\[
f(x)=\frac1{\pi(1+x^2)}.
\]

Its characteristic function is

\[
\phi_X(t)=e^{-|t|}.
\]

Now calculate the sample average

\[
\overline X_n=\frac1n\sum_{i=1}^nX_i.
\]

Using characteristic functions and independence,

\[
\begin{aligned}
\phi_{\overline X_n}(t)
&=
\prod_{i=1}^n
\phi_X\left(\frac tn\right)\\
&=
\left(e^{-|t|/n}\right)^n\\
&=e^{-|t|}.
\end{aligned}
\]

This is exactly the characteristic function of a single \(X_i\).

Consequently,

\[
\boxed{
\overline X_n\overset d=X_1
}
\]

for every \(n\ge1\).

This means that

no matter how many independent standard Cauchy random variables we average, the distribution of the average does not become more concentrated.

It remains standard Cauchy.

The usual convergence conclusion of the law of large numbers fails here, and the standard central limit theorem with finite variance certainly does not apply.

The reason is that the Cauchy distribution has neither a finite first absolute moment nor a finite variance.

We now see that

**the universality of the normal distribution is conditional.**

It depends on the tail behavior of the random variables, their dependence structure, and the scale chosen for summation.

When these conditions change, the limit may belong to a completely different family of distributions.

This leads to stable distributions, generalized central limit theorems, and modern probability theory's study of heavy tails.

It also shows that the normal distribution is the starting point of a broader theory of random limits, rather than the endpoint of randomness.

---

# Chapter 3 Conclusion: What Have We Really Discovered?

Let us retrace the chapter's line of thought.

At the outset, we had a very concrete difficulty:

calculating

\[
2^{-n}\sum_{k=a}^{b}\binom nk
\]

becomes exceedingly troublesome when \(n\) is large.

To understand it, we studied the central term and then compared neighboring binomial coefficients.

Taking logarithms and applying a Taylor expansion brought out

\[
e^{-x^2/2}.
\]

To obtain a nontrivial limiting shape, we had to introduce a scale such as \(\sqrt n\).

As the discrete lattice spacing tends to zero, sums of binomial coefficients become integrals.

The bell curve then emerges naturally.

The direction of generalization advanced by Laplace next tells us that this limiting phenomenon extends beyond binomial distributions.

Modern characteristic functions reveal the structure behind it:

\[
\left(
1-\frac{t^2}{2n}
+o\left(\frac1n\right)
\right)^n
\longrightarrow e^{-t^2/2}.
\]

After independent summation and suitable standardization, a complicated random system exhibits a universal limiting form determined by second-order structure.

Meanwhile, Gauss's analysis of measurement errors reveals connections between the normal distribution and the optimality of the arithmetic mean and least squares.

Two quite different paths of inquiry finally meet.

**Adding Many Random Events**
de Moivre → Laplace

\[
\sum X_i
\]

**Measurement Errors and Optimal Estimation**
Legendre → Gauss

\[
\min_\theta\sum(Y_i-\theta)^2
\]

**The Normal Distribution**

\[
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
\]

Probabilistic limits, analytical structure, and statistical estimation come together here.

But I believe this chapter contains an idea more important than any individual formula.

We have found two phenomena that initially seem entirely opposed:

On the one hand, random events produce unpredictable fluctuations.

On the other, after enough accumulation, those fluctuations exhibit a stable and universal mathematical regularity.

This does not mean that the world has ceased to be random.

Quite the contrary.

**By studying randomness itself carefully, mathematicians discovered the order that randomness allows.**

We can now explain why random errors from different sources may produce approximately the same bell curve.

Yet another question arises.

In our earlier study of random variables, we could often begin by explicitly writing down their probability distributions.

But many random objects in the real world vary continuously.

For example, a particle keeps moving in a liquid.

We want to know not only its position at a particular time, but also how it moves randomly over an entire time interval.

More puzzling still:

If we observe this motion on shorter and shorter time scales, what will we ultimately see?

As the time interval tends to zero, can we construct a mathematical process that is truly continuous yet remains random throughout?

This will force us to move from individual random variables to stochastic processes consisting of infinitely many random variables.

It will also bring us back to a question that first appeared in Chapter 1:

**When the possible random outcomes form an infinite and complicated space, how should we define probability?**

This prepares the way for our journey into measure theory, stochastic processes, and Brownian motion.

---

Coming Next

## Chapter 4: When Randomness Enters Time—From Random Walks to Brownian Motion

We will begin with a very simple model:

\[
S_n=X_1+\cdots+X_n,
\qquad P(X_i=1)=P(X_i=-1)=\frac12.
\]

Then we will ask:

Why, after shrinking space by \(1/\sqrt n\) and time by \(1/n\), can a random motion that jumps on an integer lattice converge to a stochastic process with continuous paths?

This will be our first real encounter with **random functions themselves**, beyond random numbers alone.

It will also provide another important foundation for our later study of random trees, the CRT, and continuous random geometry.

The Mathematics of Chance · Volume I, Chapter 3 · Working Draft v0.1


---

# The Mathematics of Chance
Volume I · Can Chance Be Calculated?

# Chapter 4: When Randomness Enters Time—From Random Walks to Brownian Motion

Can snapshots of Gaussian distributions be assembled into a genuine random path?

In Chapter 3, we discovered a profound phenomenon in probability theory.

After suitable centering and standardization, the sum of many independent random variables may converge to a normal distribution:

\[
\frac{X_1+\cdots+X_n-n\mu}{\sigma\sqrt n}
\xrightarrow{d}N(0,1).
\]

Until now, however, we have treated the random experiment as a whole.

We cared only about the final sum of the first \(n\) random variables.

Now suppose that, instead of observing only the final sum, we record the position of the random system at every step.

The single random variable

\[
S_n=X_1+\cdots+X_n
\]

then becomes an entire sequence of random variables:

\[
S_0,S_1,S_2,\ldots
\]

We begin to ask a new question:

**How does randomness develop over time?**

This question will take probability theory beyond individual random numbers into random paths, stochastic processes, and eventually spaces of random functions.

Along the way, we will encounter one of the most important objects in modern probability theory: Brownian motion.

---

## 4.1 A Botanist Discovers a Mathematical Problem

![Historical illustration from the original manuscript](assets/images/07-01.img)

[Original image source](https://commons.wikimedia.org/wiki/File%3APortrait_of_Robert_Brown_Wellcome_L0011784.jpg?utm_source=chatgpt.com)

**Robert Brown（1773—1858）**

A Scottish botanist who took part in botanical exploration in Australia and also studied the microscopic structure of plants.

In 1827, while studying tiny particles in pollen, he observed their persistent, irregular motion in a liquid.

By the early nineteenth century, microscopes already allowed people to observe many structures invisible to the naked eye.

Studying pollen, Brown noticed that very small particles kept trembling and changing position even when suspended in apparently still water.

At first, this motion seemed possibly related to life.

But Brown went on to study particles of nonliving matter and found that similar motion was not confined to living materials.

It could therefore not be attributed simply to the pollen being alive.

Brown made these observations in 1827 and published his report in 1828. Others had observed similar phenomena earlier, so his important contribution was a systematic investigation of the universality of the motion among different small particles, rather than being “the first to see particles move.” 〔[31](#ref-turn360592search6), [32](#ref-turn360592search7)〕

![Historical illustration from the original manuscript](assets/images/08-01.img)

![Historical illustration from the original manuscript](assets/images/08-02.img)

![Historical illustration from the original manuscript](assets/images/08-03.img)

![Historical illustration from the original manuscript](assets/images/08-04.img)

![Historical illustration from the original manuscript](assets/images/08-05.img)

![Historical illustration from the original manuscript](assets/images/08-06.img)

![Historical illustration from the original manuscript](assets/images/08-07.img)

[Original image source](https://masterymind.co.uk/study-guides/physics-ocr-gcse-brownian-motion)

[Original image source](https://web.mit.edu/course/10/10.50/www/diffuse2.html)

[Original image source](https://www.heurema.com/POFQ-Perrin.htm)

[Original image source](https://www.iitianacademy.com/cie-igcse-physics-0625-particle-model-study-notes/)

[Original image source](https://www.academia.edu/4000202/_Evident_atoms_visuality_in_Jean_Perrin_s_Brownian_motion_research_Studies_in_the_History_and_Philosophy_of_Science_39_2008_312_322)

[Original image source](https://www.slideserve.com/darrius/introduction-to-the-experiments-of-physics-407)

[Original image source](https://www.mvp.cufo.cz/materialy/9.html)

Let us try to think from the perspective of an observer at the time.

If the water is still and the particle cannot move under its own power, why does it keep moving?

If some invisible microscopic action continually pushes these particles, can countless tiny motions that we cannot directly observe produce statistical laws measurable at a macroscopic scale?

This question later became closely connected with the kinetic theory of molecules, evidence for the existence of atoms, and statistical physics.

In 1905, Einstein gave a quantitative theory of the diffusion of suspended particles; Smoluchowski proposed a related theory in 1906. Jean Perrin's subsequent experiments provided important support for the predictions. 〔[33](#ref-turn360592search3), [34](#ref-turn360592search4), [35](#ref-turn360592search5)〕

There is also a historical episode worth noticing.

Before the physical theory of Brownian motion had matured, the French mathematician Louis Bachelier studied a similar continuous random price model in his 1900 financial mathematics thesis *Théorie de la spéculation*.

The rigorous probabilistic foundations of this continuous stochastic process are closely associated with Norbert Wiener's work in the 1920s, particularly in 1923.

Today, mathematical standard Brownian motion is also called the Wiener process. 〔[36](#ref-turn360592search8), [37](#ref-turn360592search0)〕

But that history came later.

To understand how such a process arises, we must first set aside continuous time, continuous paths, and even the normal distribution.

We begin with the smallest possible model.

---

## 4.2 A Particle That Can Move Only Left or Right at Each Step

Imagine a particle on the integer line.

It starts at the origin.

At each unit of time, it randomly moves one unit to the right or left.

Let

\[
\xi_1,\xi_2,\ldots
\]

be independent, identically distributed random variables with

\[
P(\xi_i=1)=P(\xi_i=-1)=\frac12.
\]

Define

\[
S_0=0,\qquad
S_n=\sum_{i=1}^n\xi_i.
\]

Then

\[
S_n
\]

is the particle's position after \(n\) steps.

This is the one-dimensional simple symmetric random walk.

We already have most of the knowledge needed to study this model.

Since

\[
\mathbb E[\xi_i]=0,
\qquad
\operatorname{Var}(\xi_i)=1,
\]

we have

\[
\boxed{
\mathbb E[S_n]=0,\qquad
\operatorname{Var}(S_n)=n.
}
\]

and hence

\[
\mathbb E[S_n^2]=n.
\]

If we measure the typical distance from the origin by the root-mean-square displacement, then

\[
\boxed{
\sqrt{\mathbb E[S_n^2]}=\sqrt n.
}
\]

This is rather strange.

If the particle always moves right, its distance from the origin after \(n\) steps is \(n\).

But when independent, symmetric randomness determines its direction, its root-mean-square displacement is only \(\sqrt n\).

Displacement scales for random walks and deterministic motion

<div class="numeric-chart" data-chart="2"></div>

The displacement scale of random motion is thus quite different from that of deterministic motion at constant speed.

Motion at constant speed satisfies

\[
x(t)\propto t.
\]

In this random-walk model, however, the typical displacement satisfies

\[
|S_n|_{\mathrm{typical}}\propto\sqrt n.
\]

Of course, an individual random trajectory may deviate enormously.

\(\sqrt n\) is not a deterministic bound that holds for every sample path.

It is first of all a statistical scale supplied by the second moment.

But this scale will become the key to understanding continuous random motion.

## 4.3 What Becomes of a Random Walk as Time Is Divided More Finely?

Let us pose a thought experiment.

Suppose we no longer want the particle to move once per second.

Instead, let it move \(n\) times in one second.

Each move then takes time

\[
\Delta t=\frac1n.
\]

At the same time, shrink the spatial length of each step to

\[
\Delta x=\frac1{\sqrt n}.
\]

In time \(t\), the particle then takes approximately \(nt\) steps.

The variance of its total displacement is therefore approximately

\[
nt\cdot\frac1n=t.
\]

This means that

even as individual steps shrink and the number of steps per unit time grows, the total displacement retains a nontrivial variance.

We get neither a completely stationary particle nor a system that diverges infinitely in finite time.

Now define

\[
\boxed{
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n},
\qquad t\ge0.
}
\]

Here \(\lfloor nt\rfloor\) denotes the largest integer no greater than \(nt\).

This is the random walk after simultaneous rescaling of time and space.

Let us observe how it changes.

<div class="experiment" data-widget="walk"></div>

A scaling experiment for discrete random walks. Number of time steps: 16, 32, 64, 128, 256. Illustrative simulation: each step has length \(1/\sqrt n\) and each time interval is \(1/n\). To aid comparison, different-length prefixes of the same pregenerated sequence of random increments are used; the figure does not rigorously depict successive approximations of one and the same path.

As \(n\) increases, the original large jumps become smaller and more densely spaced.

We begin to expect that, in some limiting sense, this process will form a continuous random path.

But this immediately raises two mathematical questions.

First, does such a limit really exist?

Second, even if it exists, in what sense should we understand convergence of an entire random path?

The central limit theorem so far describes only how the distribution of a single random variable converges.

Now we want an entire function to converge:

\[
t\longmapsto W_n(t).
\]

This distinction will be crucial.

## 4.4 Why Must the Spatial Scale Be the Square Root of the Time Scale?

Let us avoid assuming that the scaling exponent is \(1/2\).

Suppose time is still shrunk by \(1/n\), but the spatial step is

\[
n^{-\alpha}
\]

where \(\alpha>0\).

Define

\[
W_n^{(\alpha)}(t)
=
n^{-\alpha}S_{\lfloor nt\rfloor}.
\]

Since

\[
\operatorname{Var}(S_{\lfloor nt\rfloor})=\lfloor nt\rfloor,
\]

we have

\[
\operatorname{Var}(W_n^{(\alpha)}(t))
=
n^{-2\alpha}\lfloor nt\rfloor.
\]

For fixed \(t>0\), the asymptotic scale is

\[
t n^{1-2\alpha}.
\]

Three quite different cases arise.

If

\[
\alpha>\frac12,
\]

then

\[
\operatorname{Var}(W_n^{(\alpha)}(t))\to0.
\]

The random displacement tends to zero in probability, giving a degenerate limit.

If

\[
\alpha=\frac12,
\]

then

\[
\operatorname{Var}(W_n^{(\alpha)}(t))\to t.
\]

the fluctuations retain a finite, nonzero scale in the limit.

If

\[
\alpha<\frac12,
\]

the variance tends to infinity. For this symmetric random walk, the central limit theorem further shows that, for any fixed \(M>0\),

\[
P(|W_n^{(\alpha)}(t)|\le M)\to0.
\]

The distributions at a fixed time therefore do not form a tight family of probability distributions on the real line.

Thus only

\[
\boxed{\alpha=\frac12}
\]

can give us the nondegenerate diffusion limit we seek.

This choice of scale is profound.

\[
\boxed{
\text{time scale}\sim\varepsilon^2,
\qquad
\text{space scale}\sim\varepsilon.
}
\]

It differs from deterministic motion at constant speed, where

\[
\text{space scale}\sim\text{time scale}.
\]

In random diffusion, time and space obey a quadratic relationship.

When we later study scaling limits of random trees, the CRT, and other continuous random geometric objects, we will encounter this idea again:

**Finding the right scaling exponent is often the first step toward discovering the limiting object.**

The actual exponent, however, depends on the random structure of the model. Not every random system must have the Brownian exponent \(1/2\).

---

## 4.5 The Central Limit Theorem Sees Only One Time

Return to

\[
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n}.
\]

First fix a time \(t>0\).

Since

\[
S_{\lfloor nt\rfloor}
=
\xi_1+\cdots+\xi_{\lfloor nt\rfloor},
\]

the central limit theorem gives

\[
\frac{S_{\lfloor nt\rfloor}}{\sqrt{\lfloor nt\rfloor}}
\xrightarrow d N(0,1).
\]

Thus

\[
W_n(t)
=
\frac{S_{\lfloor nt\rfloor}}{\sqrt{\lfloor nt\rfloor}}
\sqrt{\frac{\lfloor nt\rfloor}{n}}.
\]

Since

\[
\frac{\lfloor nt\rfloor}{n}\to t,
\]

we obtain

\[
\boxed{
W_n(t)\xrightarrow d N(0,t).
}
\]

If a continuous-time limit exists, we see that its position at each fixed time \(t\) should therefore be normally distributed with mean 0 and variance \(t\).

Its density should thus be

\[
\boxed{
p_t(x)
=
\frac1{\sqrt{2\pi t}}
\exp\left(-\frac{x^2}{2t}\right).
}
\]

But notice:

This conclusion describes only a single fixed time.

It says nothing about the relationship between the positions at \(t=1\) and \(t=2\), or where the particle travels between those times.

A stochastic process is much more than a separate probability distribution at each time.

### 4.5.1 Why Is Knowing the Distribution at Every Time Insufficient?

Consider two stochastic processes.

The first is

\[
X_t=\sqrt t\,Z,
\]

where

\[
Z\sim N(0,1).
\]

Then, for each \(t>0\),

\[
X_t\sim N(0,t).
\]

Temporarily denote the second process by \(B_t\), and require it also to satisfy

\[
B_t\sim N(0,t).
\]

The two processes therefore have the same distribution at each fixed time.

For the first process, however,

\[
X_s=\sqrt{\frac st}X_t
\qquad(0<s<t).
\]

Knowing its position at one nonzero time determines its position at every other time.

Its entire path is simply a deterministic function of the form

\[
t\longmapsto \sqrt t\,z
\]

with a random coefficient \(z\).

Consequently,

\[
\operatorname{Cov}(X_s,X_t)=\sqrt{st}.
\]

The Brownian motion we seek, however, will satisfy

\[
\operatorname{Cov}(B_s,B_t)=\min(s,t).
\]

These are clearly different.

In particular, when \(0<s<t\),

\[
\sqrt{st}\ne s.
\]

Two stochastic processes can thus have exactly the same distribution at every time while having entirely different temporal structures.

**To study a stochastic process, we must understand joint distributions across different times, beyond the marginal distribution at each time.**

### 4.5.2 From One Time to Several

Choose times

\[
0=t_0<t_1<\cdots<t_m.
\]

We study the random vector

\[
(W_n(t_1),\ldots,W_n(t_m)).
\]

The most natural way to understand it is to study the increments between adjacent times rather than each coordinate separately:

\[
\Delta_{n,j}=W_n(t_j)-W_n(t_{j-1}).
\]

For the step process defined here, these increments are exactly sums of random steps over distinct time intervals; boundary terms require control only if we switch to the linearly interpolated version (see Appendix F).

For example,

\[
\Delta_{n,j}
=
\frac1{\sqrt n}
\sum_{k=\lfloor nt_{j-1}\rfloor+1}^{\lfloor nt_j\rfloor}\xi_k.
\]

Different intervals use disjoint collections of random variables, so the increments are independent.

Each increment also satisfies the central limit theorem:

\[
\Delta_{n,j}
\xrightarrow d
N(0,t_j-t_{j-1}).
\]

The entire increment vector should therefore converge to a collection of independent normal random variables:

\[
(Z_1,\ldots,Z_m),
\]

where

\[
Z_j\sim N(0,t_j-t_{j-1}).
\]

Characteristic functions prove this joint convergence rigorously: independence factors the joint characteristic function into a product, and each factor converges to the characteristic function of the corresponding normal distribution.

Then, using

\[
W_n(t_j)=\sum_{r=1}^j\Delta_{n,r},
\]

we obtain joint convergence of the finite-dimensional distributions.

We have therefore found the structure that the continuous limit should satisfy:

\[
\boxed{
B_{t_j}-B_{t_{j-1}}
\sim N(0,t_j-t_{j-1}),
}
\]

with independent increments over disjoint time intervals.

This is far stronger than saying that the distribution at every time is normal.


> Using characteristic functions to pass from limits of increments to the joint vector limit invokes the multivariate continuity theorem for characteristic functions and preservation of convergence in distribution by continuous linear maps. These will be developed systematically in Chapters 9 and 11, with the language of convergence introduced in Chapter 7. Appendix F retains the product-factorization calculation. This section establishes the finite-dimensional limit conditional on those tools; it does not establish a path limit theorem.

### 4.5.3 The Covariance Structure Emerges Naturally

From

\[
B_t=B_s+(B_t-B_s),
\qquad s<t,
\]

and independence of increments,

\[
\begin{aligned}
\mathbb E[B_sB_t]
&=\mathbb E[B_s^2]
+\mathbb E[B_s(B_t-B_s)]\\
&=s+0\\
&=s.
\end{aligned}
\]

Thus

\[
\boxed{
\operatorname{Cov}(B_s,B_t)=\min(s,t).
}
\]

We obtain a very special covariance kernel:

\[
\boxed{
K(s,t)=\min(s,t).
}
\]

It encodes the second-order relationships between different times of the entire process in a single function.

More importantly, for a Gaussian process, this covariance kernel together with the mean function determines all finite-dimensional joint distributions.

It appears that we have found the entire finite-dimensional probability structure of Brownian motion.

But a huge logical gap remains.

---

## 4.6 Does Knowing All Finite-Dimensional Distributions Mean We Have Constructed a Random Path?

Suppose we know, for every finite collection of times

\[
t_1,\ldots,t_m,
\]

the joint distribution that the random vector

\[
(B_{t_1},\ldots,B_{t_m})
\]

should have.

Does this already imply that a continuous random path exists,

\[
t\longmapsto B_t?
\]

Not necessarily.

Later, under appropriate conditions on the state space, we will use a probability-measure extension theorem to realize consistent finite-dimensional distributions within one stochastic process. Here we first identify the problems a construction must solve, without invoking that theorem in advance to announce that the construction is complete.

Such a construction does not, by itself, automatically guarantee continuous sample paths.

Moreover, even when two processes have the same joint distributions at all finite collections of times, we cannot conclude without qualification that their path properties agree.

This is an easily overlooked trap in moving from random variables to stochastic processes.

### 4.6.1 A Simple but Decisive Counterexample

Let \(U\sim\operatorname{Uniform}(0,1)\) and define

\[
X_t=\mathbf1_{\{t=U\}},
\qquad 0\le t\le1.
\]

For every fixed \(t\),

\[
P(X_t=1)=P(U=t)=0.
\]

so

\[
X_t=0\quad\text{a.s.}
\]

For any finite collection of deterministic times \(t_1,\ldots,t_m\), we likewise have

\[
P(X_{t_1}=\cdots=X_{t_m}=0)=1.
\]

All finite-dimensional distributions of the process \((X_t)\) are therefore exactly the same as those of the identically zero process

\[
Y_t\equiv0
\]

in every case.

Yet the complete paths are dramatically different.

For every \(U\in(0,1)\), the function

\[
t\longmapsto X_t
\]

suddenly takes the value 1 at \(t=U\) and is zero everywhere else.

The path is therefore discontinuous.

The paths of \(Y_t\equiv0\), by contrast, are clearly continuous everywhere.

We even have

\[
\sup_{0\le t\le1}X_t=1
\quad\text{a.s.},
\]

but

\[
\sup_{0\le t\le1}Y_t=0.
\]

Notice how far-reaching this is:

\[
\boxed{
\text{all finite-dimensional distributions agree}
\not\implies
\text{path properties agree}.
}
\]

This does not mean finite-dimensional distributions are useless.

On the contrary, they are an essential part of describing a process.

But to study continuous paths, we must also specify the function space in which we construct our random object and explain how fluctuations between different times are controlled.

Otherwise, continuity may be merely a smooth curve drawn on paper, rather than a rigorously established mathematical property.

### 4.6.2 Another Problem: Finite-Dimensional Convergence Is Not Path Convergence

Even for a sequence of continuous functions, convergence at each fixed time need not imply convergence of the entire path.

For example, consider the functions on \([0,1]\) given by

\[
f_n(t)=\max\left\{1-2n\left|t-\frac1n\right|,0\right\}.
\]

As \(n\) increases, this triangular spike moves toward 0 and becomes narrower.

For every fixed \(t\in[0,1]\),

\[
f_n(t)\to0.
\]

But for every sufficiently large \(n\),

\[
\sup_{0\le t\le1}|f_n(t)|=1.
\]

Thus these functions do not converge uniformly to the zero function.

This is a very visual warning:

When studying paths, checking what happens at each deterministic time is insufficient. Exceptional fluctuations over increasingly short intervals, increasingly difficult to detect at fixed times, may still prevent convergence of the whole function.

We therefore need a new theory of convergence for stochastic processes. Chapter 7 will first distinguish the various forms of random convergence; later chapters will place these questions in function spaces.

---


Two obstacles must be distinguished here. Marginal distributions alone do not even describe relationships between times; after all finite-dimensional distributions are known, we must still choose a path space and establish its measurable structure and regularity.

The random spike does not mean that finite-dimensional distributions can never determine the probability law of continuous paths. Once a process is established as a Borel random element in a space of continuous functions, all its finite-dimensional distributions determine its path distribution; proving this requires the measurable structure developed later. The counterexample shows that finite-dimensional information alone cannot establish path continuity without specifying the path space and the version of the process.

**Snapshots tell us where a particle appears, but do not automatically provide a random path on which we can discuss “ever reaching” or “remaining throughout.”**

This is the chapter's real turning point. The Gaussian limit has not failed; it has brought us to questions it cannot answer on its own.

## 4.7 The Continuous Random Motion We Seek

After the preceding investigation, we are finally ready for the formal definition.

**Definition: Standard Brownian Motion**

A real-valued stochastic process

\[
B=(B_t)_{t\ge0}
\]

is called a standard Brownian motion if:


**1.** \(B_0=0\) almost surely;

**2.** For every \(0\le t_0<t_1<\cdots<t_m\), the increments
\[
B_{t_1}-B_{t_0},\ldots,B_{t_m}-B_{t_{m-1}}
\]
are independent;


**3.** For every \(0\le s<t\),
\[
B_t-B_s\sim N(0,t-s);
\]

**4.** Almost every sample path \(t\mapsto B_t(\omega)\) is continuous.

The definition no longer seems unexpected.

We discovered each requirement gradually while seeking a continuous limit of random walks.

The first specifies the initial state.

The second preserves the independence of the original random walk over different time intervals.

The third gives the Gaussian increment structure arising from the central limit theorem.

The fourth needs a proof at the level of function spaces; distributions at fixed times alone cannot guarantee it.


These four conditions are requirements on the limiting object, not yet a proof of its existence. In particular, the fourth does not follow automatically from the earlier Gaussian snapshots.

This chapter no longer compresses a rigorous construction into the text immediately after the definition. Later we will separately address how to extend consistent finite-dimensional distributions to a probability measure, how to choose a continuous version, and why entire random-walk paths approach this process. The original construction routes and technical calculations are retained in full in the [continuous versions and Wiener measure module](#advanced-wiener) and the [Donsker and path tightness module](#advanced-donsker).

---

## 4.8 From Random Walks to the Heat Equation: Why Does Random Motion Produce a Deterministic Partial Differential Equation?

Following the random-walk route, we have identified the requirements Brownian motion should satisfy; its rigorous existence remains to be established later.

Mathematical history offers another important route to the same object:

heat conduction and diffusion.

This connection deserves a careful derivation because it reveals a deep relationship between the random world and deterministic differential equations.

### 4.8.1 Starting Again from a Discrete Random Walk

Suppose a particle moves on a spatial grid, jumping left or right by \(\Delta x\), with each jump taking time \(\Delta t\).

Let

\[
p(x,t)
\]

be the probability mass of the particle at time \(t\) at grid point \(x\).

The particle can arrive at \(x\) only from its left or right neighbor, so

\[
p(x,t+\Delta t)
=
\frac12p(x-\Delta x,t)
+
\frac12p(x+\Delta x,t).
\]

Rearranging gives

\[
\begin{aligned}
&p(x,t+\Delta t)-p(x,t)\\
&=\frac12\left[
p(x-\Delta x,t)-2p(x,t)+p(x+\Delta x,t)
\right].
\end{aligned}
\]

Divide both sides by \(\Delta t\):

\[
\begin{aligned}
\frac{p(x,t+\Delta t)-p(x,t)}{\Delta t}
=
\frac{(\Delta x)^2}{2\Delta t}
\frac{
p(x-\Delta x,t)-2p(x,t)+p(x+\Delta x,t)
}{(\Delta x)^2}.
\end{aligned}
\]

Now examine this expression.

The left-hand side has the form of a difference quotient in time:

\[
\frac{\partial p}{\partial t}.
\]

The right-hand side has the form of a second difference quotient in space:

\[
\frac{\partial^2p}{\partial x^2}.
\]

If both grid spacings tend to zero while

\[
\frac{(\Delta x)^2}{2\Delta t}\to D,
\]

we formally obtain

\[
\boxed{
\frac{\partial p}{\partial t}
=
D\frac{\partial^2p}{\partial x^2}.
}
\]

This is the one-dimensional diffusion equation, also called the heat equation.

This is a formal derivation of a continuous limit. Rigorously proving that the suitably normalized limit of the discrete probability masses satisfies this partial differential equation requires a local limit theorem, semigroup theory, or other convergence methods. 〔[43](#ref-turn516523search36), [44](#ref-turn516523search1)〕

But it already reveals a mathematical connection that is difficult to overlook:

**At the level of probability distributions, a sequence of entirely random tiny movements can produce a deterministic partial differential equation.**

### 4.8.2 Why Is the Heat Equation's Solution Again a Normal Density?

For standard Brownian motion,

\[
B_t\sim N(0,t).
\]

so the position density is

\[
p_t(x)=
\frac1{\sqrt{2\pi t}}
e^{-x^2/(2t)}.
\]

Direct partial differentiation verifies that

\[
\boxed{
\frac{\partial p_t}{\partial t}
=
\frac12\frac{\partial^2p_t}{\partial x^2}.
}
\]

For a general diffusion coefficient \(D\), the density is

\[
\boxed{
p_t(x)
=
\frac1{\sqrt{4\pi Dt}}
e^{-x^2/(4Dt)}.
}
\]

Its variance is

\[
\operatorname{Var}(X_t)=2Dt.
\]

Thus

\[
\boxed{
\mathbb E[(X_t-X_0)^2]=2Dt
}
\]

holds for a one-dimensional diffusion model starting at the origin with no drift.

This is precisely the mean-square displacement law connecting Einstein's 1905 Brownian motion theory closely with experiment.

Under appropriate physical conditions, the diffusion coefficient can also be related to temperature, fluid viscosity, and particle radius, allowing macroscopically observable random displacements to reveal microscopic properties of matter. 〔[35](#ref-turn360592search5), [31](#ref-turn360592search6)〕


The density obtained from random jumps satisfies a deterministic diffusion equation. For standard Brownian motion, its coefficient is \(D=1/2\); a general \(D>0\) corresponds to the process \(\sqrt{2D}\,B_t\). This explains why we study both the particle's random trajectory and the deterministic evolution of its distribution over time.

Verifying that the Gaussian density satisfies the heat equation does not replace a proof that continuous random paths exist. A density describes the distribution at each time; how a path connects those times remains the open question. Semigroups, generators, and deeper connections to stochastic calculus have been transferred in full to the [semigroups and generators module](#advanced-semigroup), awaiting the relevant tools.

## 4.9 When “It Happened at Some Time” Becomes an Event

If a particle ends up near the origin, can we say it never traveled far?

Of course not. It might have crossed a high horizontal line and then returned. The final position gives only the last snapshot; “having crossed” requires the entire path.

Assume we already have a continuous Brownian path, and ask on \([0,1]\):

\[
A=\left\{\omega:\sup_{0\le t\le1}B_t(\omega)>1\right\}.
\]

This set contains a whole collection of functions with a particular history, rather than a sequence of possible die scores. We want to write \(P(A)\), but first must answer: which sets of paths may be assigned probabilities, and why does \(A\) belong among them?

Continuity offers a clue. If a continuous path is strictly above 1 at some time, it is also above 1 at a nearby rational time. Thus, for continuous paths,

\[
\left\{\sup_{0\le t\le1}B_t>1\right\}
=\bigcup_{q\in\mathbb Q\cap[0,1]}\{B_q>1\}.
\]

The right-hand side needs only countably many observation times. Here the equality is understood path by path in the continuous path space; if the process is only almost surely continuous, the equality holds on the same probability-one continuity event. Both continuity and the strict inequality matter; the reasoning cannot be applied unconditionally to the earlier random spike. We have not yet used the equality to calculate the probability, but it already indicates which set operations should continue to yield meaningful events when describing entire paths.

Our language must accommodate complements, countable unions, and limits; it must also explain why the maximum of a continuous function can serve as a random quantity. Chapter 5 begins with the sets we may discuss, Chapter 6 develops integration as a language for averaging functions, and Chapter 7 proceeds to different kinds of random convergence. Only then will we be ready to return to Brownian motion and complete the construction and path limits.

## Chapter 4 Conclusion: We Know Where the Particle Is, but Not Which Path It Took

Let us return to the microscope.

The particles Brown observed are still moving constantly in the water. Their positions keep changing and their directions seem patternless; even a clear view of a particle's present position cannot predict where it will move next.

To understand this motion, we began with the simplest random walk: each step goes left or right, independently and with equal probability. One step alone cannot reveal the scale of motion over a long period. But when many jumps are combined, cancellations between directions leave a stable scale. Quadrupling the number of steps only doubles the root-mean-square displacement.

As jumps become more frequent and steps become smaller, we therefore cannot rescale time and space arbitrarily. For random motion to persist while retaining a finite scale of fluctuations, we must maintain

\[
\Delta x\sim\sqrt{\Delta t}.
\]

At this scale, the Gaussian limit of Chapter 3 reappears: at a fixed time, the particle's position distribution approaches a bell curve whose variance grows with time.

But this gives us only one snapshot.

Collecting separate snapshots at every time does not tell us how the particle moves from one position to another. The same one-time distributions can arise from very different motions. We must turn to joint structure across times and to increments over adjacent time intervals, until independence and Gaussian distributions together give the special covariance kernel:

\[
K(s,t)=\min(s,t).
\]

This simple function records the connections between times: the random displacement accumulated at an earlier time becomes part of the later position, while subsequent independent increments bring fresh fluctuations.

When we turn from the trajectory of one particle to the position distribution of many particles, another regularity appears. At the standardized diffusion scale, the Gaussian density satisfies

\[
\frac{\partial p}{\partial t}
=\frac12\frac{\partial^2p}{\partial x^2}.
\]

The irregular motion seen under the microscope connects here with the deterministic heat equation. Individual trajectories are hard to predict, yet the distribution of possible positions can evolve regularly.

Just as we seem to be gradually understanding the motion, however, a more fundamental question emerges.

**We know where the particle may be at a given time, but have not yet established its entire continuous random path in a rigorous probability space.**

One-time distributions do not determine relationships across time. Even when every finite-dimensional distribution is specified, existence and measurability of continuous paths cannot be skipped. Our definition of Brownian motion describes the properties this motion should possess, but we must still prove that these requirements can be realized together.

In studying motion, we often care about more than the final snapshot. Has the particle ever reached a given height? Can it remain in a region throughout an interval? When does it first reach a given position?

All these questions depend on the entire path. Returning near the origin at the end does not erase the long journey a particle may have made.

The outcome of a random experiment can therefore be an entire function. We want to group paths with the same kind of history and assign a probability to that collection; before writing that probability, we must know why such a set of paths is an event we are allowed to discuss.

The particle brings us back to the question left open in Chapter 1. Counting gave clear answers for finite games of chance. Now the possible outcomes are entire continuous functions, and the old answer is insufficient.

**How should probability be defined?**

## Toward Chapter 5: Why Does Probability Need Measure Theory?

Let us simplify the difficulty. For now, set aside choosing a random path in function space, and ask only how to choose a real number uniformly from the interval \([0,1]\).

We want the probability of an interval to equal its length. Translating a set should preserve its probability, provided it remains within the interval. Combining countably many disjoint events should give a total probability equal to the sum of their probabilities.

These requirements look natural. But can we retain them all while assigning a probability to every subset of \([0,1]\)?

If even all the sets within an interval cannot be measured this way, we have still more reason to determine exactly which sets can be events before assigning probabilities to entire collections of random paths.

The next chapter begins with this ambition and takes us to the point where it becomes impossible. To understand the particle moving ceaselessly in the water, we must first rethink what it means for an event to be measurable.

[Continue to Chapter 5](#chapter-5)

The Mathematics of Chance · Volume I, Chapter 4 · Reading Candidate with Revised Conclusion, 2026-10-26


---

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

![Historical illustration from the source manuscript](assets/images/04-01.img)

[Original image source](https://www.futura-sciences.com/sciences/personnalites/mathematiques-emile-borel-319/?utm_source=chatgpt.com)

**Émile Borel（1871—1956）**

A French mathematician. In 1898, he studied the sets and measure structures obtainable from intervals through countable set operations.

![Historical illustration from the source manuscript](assets/images/05-01.img)

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

But the Cantor set has the same cardinality as the reals, and its power set has strictly greater cardinality than the family of Borel sets.

There must therefore be subsets of the Cantor set that are not Borel, yet are Lebesgue measurable.

This shows that Borel measure can be completed by adjoining all subsets of null sets to the measurable structure.

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

![Andrey Nikolaevich Kolmogorov mathematician black and white portrait](assets/images/06-01.img)

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


---

# The Mathematics of Chance
Volume II · Probability in an Infinite World

# Chapter 6: The Rebirth of the Average—From Weighted Sums to the Lebesgue Integral

Why should a simple average of gambling winnings ultimately require an entirely new theory of integration?

In Chapter 5, we underwent a major transformation in mathematical thought.

To define probability on infinite sets, we had to abandon a seemingly natural wish: not every set can have a measure compatible with interval length.

We therefore established the probability space

\[
(\Omega,\mathcal F,P).
\]

Probability became more than “the number of favorable outcomes divided by the total number of outcomes”: it became a countably additive measure defined on a \(\sigma\)-algebra.

This finally enabled us to study continuous distributions, infinite random sequences, and complicated random objects such as Brownian motion rigorously.

Looking back over the development of probability, however, we find another mathematical concept of almost equal importance that has accompanied us throughout.

It is expectation.

In Chapter 1, we used expectation to divide the stakes fairly in an unfinished game.

In Chapter 2, we used expectation to estimate unknown parameters.

In Chapter 3, we used means and variances to study normal limits.

In Chapter 4, we even calculated the expectation of the sum of squared increments of an entire stochastic process.

But we never really answered:

**Why should expectation be defined in the familiar way? What exactly is expectation when the sample space is no longer finite?**

We now possess measure.

Perhaps it is time to understand averages afresh, from the beginning.

---

## 6.1 It Still Begins with a Fair Game of Chance

Imagine returning once more to Chapter 1.

A gambling contract has three possible payoffs:

\[
X=
\begin{cases}
10,&\text{with probability }1/2,\\
20,&\text{with probability }1/3,\\
-5,&\text{with probability }1/6.
\end{cases}
\]

If we want a single number to represent its average payoff, the most natural calculation is

\[
\begin{aligned}
\mathbb E[X]
&=10\cdot\frac12
+20\cdot\frac13
-5\cdot\frac16\\
&=\frac{65}{6}.
\end{aligned}
\]

Here we are taking a weighted sum:

\[
\boxed{
\mathbb E[X]=\sum_i x_ip_i.
}
\]

But we should examine this expression more closely.

It actually contains two entirely different mathematical objects.

The first is the payoff:

\[
x_i.
\]

The second is the probability weight associated with each payoff:

\[
p_i.
\]

Expectation is a mathematical operation combining the two.

Now write it in another form.

Let the sample space be

\[
\Omega=\{\omega_1,\omega_2,\omega_3\},
\]

and define the random variable

\[
X(\omega_1)=10,\quad
X(\omega_2)=20,\quad
X(\omega_3)=-5.
\]

with corresponding probabilities

\[
P(\{\omega_1\})=\frac12,\quad
P(\{\omega_2\})=\frac13,\quad
P(\{\omega_3\})=\frac16.
\]

Then

\[
\mathbb E[X]
=
\sum_{\omega\in\Omega}
X(\omega)P(\{\omega\}).
\]

This formula already comes very close to the idea of integration.

What we are doing, in fact, is:

Accumulating the values of a function on the sample space, weighted according to a rule for the sizes of sets.

A new question therefore arises:

**If the sample space has infinitely many outcomes, can this weighted summation be extended to some kind of integral?**

### 6.1.1 From Finite to Continuous Outcomes

Suppose the payoff is no longer restricted to three values.

From \([0,1]\), we choose a real number \(U\) uniformly at random, then receive the payoff

\[
X=U^2.
\]

Chapter 5 has already supplied a rigorous uniform probability space:

\[
\Omega=[0,1],
\qquad P=\text{Lebesgue length measure}.
\]

We want to calculate

\[
\mathbb E[U^2].
\]

From calculus, we would naturally write:

\[
\mathbb E[U^2]
=
\int_0^1x^2\,dx
=
\frac13.
\]

But this step contains an assumption we have not yet explained:

Why should the average of a continuous random variable equal an area integral of a function over an interval?

Our usual explanation is that the interval can be divided into many small pieces.

For example:

\[
0=x_0<x_1<\cdots<x_n=1.
\]

For each small interval

\[
I_k=[x_{k-1},x_k],
\]

choose a representative point \(\xi_k\).

The expectation then appears to be approximated by

\[
\sum_{k=1}^n\xi_k^2P(U\in I_k).
\]

Since \(U\) is uniformly distributed,

\[
P(U\in I_k)=x_k-x_{k-1}.
\]

Hence

\[
\mathbb E[U^2]
\approx
\sum_{k=1}^n\xi_k^2(x_k-x_{k-1}).
\]

As the mesh becomes finer, this becomes the Riemann integral.

\[
\boxed{
\mathbb E[U^2]
=
\int_0^1x^2\,dx.
}
\]

This seems to suggest that we need no new theory of integration at all.

If calculus already provides the Riemann integral, why not simply apply it to every random variable?

The answer is that the Riemann integral depends on a particular method of approximation.

When we begin studying truly complicated random events and functions, that method encounters insurmountable difficulties.

---

## 6.2 What, Exactly, Does the Riemann Integral Do?

![Bernhard Riemann mathematician historical portrait](assets/images/01-01.img)

[Original image source](https://www.quien.net/bernhard-riemann/)

**Bernhard Riemann（1826—1866）**

A German mathematician. In his 1854 study of integration, he systematically investigated when functions more general than continuous functions could be integrated; the work was published in 1867.

Later, in 1875, Darboux developed the classical formulation of Riemann integrability in terms of upper and lower sums.

The intuitive idea behind the Riemann integral is very simple.

Given a function

\[
f:[a,b]\to\mathbb R.
\]

we want to calculate the signed area beneath its graph.

To do so, we divide the horizontal axis into small intervals and approximate the graph with rectangles.

The Riemann integral: partition the domain first

<svg viewBox="0 0 340 190" role="img" aria-label="Riemann rectangle approximation"><path d="M25 12V159H328" stroke="currentColor" fill="none"/><rect x="27.0" y="110.7143827531554" width="28.2" height="48.285617246844595" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="56.5" y="93.60983043879435" width="28.2" height="65.39016956120565" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="86.0" y="79.40231206015882" width="28.2" height="79.59768793984118" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="115.5" y="69.60979373237133" width="28.2" height="89.39020626762867" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="145.0" y="65.0871885614579" width="28.2" height="93.9128114385421" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="174.5" y="65.89796418660468" width="28.2" height="93.10203581339532" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="204.0" y="71.30461109076752" width="28.2" height="87.69538890923248" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="233.5" y="79.8794031666701" width="28.2" height="79.1205968333299" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="263.0" y="89.71881630812723" width="28.2" height="69.28118369187277" fill="#168782" fill-opacity=".19" stroke="#168782"/><rect x="292.5" y="98.72940323948023" width="28.2" height="60.270596760519766" fill="#168782" fill-opacity=".19" stroke="#168782"/><polyline points="27.0,110.7143827531554 30.3,108.92707911559825 33.6,107.15142930347153 36.9,105.38951020687368 40.2,103.64337783413175 43.5,101.91506418500911 46.8,100.20657416042557 50.099999999999994,98.51988251338953 53.4,96.85693084577939 56.7,95.21962465554134 60.0,93.60983043879435 63.3,92.02937285124939 66.6,90.48003193325987 69.9,88.96354040272332 73.19999999999999,87.48158101995163 76.5,86.03578402851687 79.8,84.62772467596524 83.1,83.25892081816907 86.4,81.9308306109608 89.69999999999999,80.64485029255889 93.0,79.40231206015882 96.3,78.20448204391788 99.6,77.05255838141527 102.89999999999999,75.94766939551586 106.19999999999999,74.89087187840859 109.5,73.88314948442934 112.8,72.9254112341122 116.1,72.01849013174461 119.39999999999999,71.16314189852832 122.69999999999999,70.36004382327316 126.0,69.60979373237133 129.3,68.91290908061872 132.6,68.26982616426585 135.89999999999998,67.68089945749554 139.2,67.1464010733358 142.5,66.66652034982852 145.8,66.24136356208273 149.1,65.87095376065076 152.39999999999998,65.55523073647267 155.7,65.29405111244262 159.0,65.0871885614579 162.29999999999998,64.93433415061884 165.6,64.83509681105603 168.9,64.78900393267085 172.2,64.79550208288421 175.5,64.85395784830092 178.79999999999998,64.96365879800926 182.1,65.1238145670511 185.39999999999998,65.33355805841461 188.7,65.59194676172174 192.0,65.89796418660468 195.29999999999998,66.25052140859188 198.6,66.64845872515215 201.89999999999998,67.09054741937877 205.2,67.57549162863083 208.5,68.10193031529072 211.79999999999998,68.66843933663988 215.1,69.27353361070524 218.39999999999998,69.9156693747828 221.7,70.59324653320294 225.0,71.30461109076752 228.29999999999998,72.04805766815775 231.6,72.82183209548738 234.89999999999998,73.6241340800569 238.2,74.4531199442517 241.5,75.30690542942023 244.79999999999998,76.18356856146832 248.1,77.08115257381121 251.39999999999998,77.99766888323815 254.7,78.93110011416434 258.0,79.8794031666701 261.29999999999995,80.84051232366218 264.6,81.81234239243108 267.9,82.79279187582716 271.2,83.77974616823288 274.5,84.7710807714701 277.79999999999995,85.7646645257523 281.1,86.75836285076794 284.4,87.7500409919653 287.7,88.73756726710293 291.0,89.71881630812723 294.3,90.6916722934476 297.59999999999997,91.65403216569314 300.9,92.60380883005757 304.2,93.53893432836801 307.5,94.45736298405077 310.8,95.35707451321099 314.09999999999997,96.23607709709509 317.4,97.09241041126295 320.7,97.92414860686368" fill="none" stroke="#168782" stroke-width="2"/><text x="320" y="180">x</text><text x="4" y="16">f(x)</text></svg>

The rectangles’ widths come from the partition of the domain, while their heights are determined by the function values on the respective intervals.

Define a partition

\[
\mathcal P=\{a=x_0<x_1<\cdots<x_n=b\}.
\]

For a bounded function \(f\), set

\[
m_k=\inf_{x\in[x_{k-1},x_k]}f(x),
\]

\[
M_k=\sup_{x\in[x_{k-1},x_k]}f(x).
\]

The lower and upper sums are, respectively,

\[
L(f,\mathcal P)=
\sum_{k=1}^nm_k(x_k-x_{k-1}),
\]

\[
U(f,\mathcal P)=
\sum_{k=1}^nM_k(x_k-x_{k-1}).
\]

If we can make

\[
U(f,\mathcal P)-L(f,\mathcal P)
\]

arbitrarily small, then \(f\) is Riemann integrable.

Behind this definition lies an important requirement:

As we divide the horizontal axis more finely, we must be able to control the function’s oscillation within the small intervals sufficiently well.

For continuous functions, this is of course no problem.

A continuous function on a compact interval is uniformly continuous.

But what about a function discontinuous everywhere?

Then things change.

### 6.2.1 A Function Entirely Natural in Probability That Cannot Be Riemann Integrated

Return to Chapter 5.

We already know that when choosing a real number uniformly on \([0,1]\),

\[
P(U\in\mathbb Q)=0.
\]

Now define

\[
f(x)=\mathbf1_{\mathbb Q\cap[0,1]}(x).
\]

In other words:

\[
f(x)=
\begin{cases}
1,&x\in\mathbb Q,\\
0,&x\notin\mathbb Q.
\end{cases}
\]

This is usually called the Dirichlet function.

From a probabilistic viewpoint, it is entirely ordinary.

It simply represents the event

\[
A=\{U\in\mathbb Q\}
\]

through its indicator function.

We want its expectation to equal the probability of that event:

\[
\mathbb E[\mathbf1_A]=P(A)=0.
\]

But what happens if we try to use the Riemann integral?

Consider any partition

\[
\mathcal P=\{0=x_0<\cdots<x_n=1\}.
\]

Since every nondegenerate subinterval contains both rational and irrational numbers,

\[
m_k=0,\qquad M_k=1.
\]

we have

\[
L(f,\mathcal P)=0,
\]

while

\[
U(f,\mathcal P)=1.
\]

However fine the mesh,

\[
\boxed{
U(f,\mathcal P)-L(f,\mathcal P)=1.
}
\]

Thus \(f\) is not Riemann integrable.

We have encountered a real problem.

Probabilistically, the expectation of this random variable could hardly be clearer:

\[
\mathbb E[f(U)]=0.
\]

Yet the traditional Riemann integral cannot assign it an integral value.

We cannot simply dismiss this function as “too irregular to be worth studying.”

Indicators of events are the most basic random variables in probability theory.

**An integration theory that cannot generally handle indicators of measurable events cannot provide a complete foundation for expectation in modern probability.**

We therefore need a new method of integration.

---

## 6.3 Lebesgue’s Change of View: Partition Values Before Positions

![Historical illustration from the source manuscript](assets/images/02-01.img)

[Original image source](https://snl.no/Henri_L%C3%A9on_Lebesgue?utm_source=chatgpt.com)

**Henri Lebesgue（1875—1941）**

A French mathematician.

In 1901, Lebesgue published a short paper on extending integration; in his 1902 doctoral dissertation, *Intégrale, longueur, aire* (*Integral, Length, Area*), he systematically developed new methods of measure and integration.

Lebesgue’s breakthrough did more than make certain previously nonintegrable functions integrable.

More fundamentally, he changed how we organize integration.〔[55](#ref-turn817174search1), [56](#ref-turn817174search26)〕

Riemann’s method can be understood as:

First divide the domain into small pieces, then examine the function values on each piece.

Lebesgue integration lets us organize the problem in the opposite direction:

First consider the values a function can take, then ask how large the sets of points having those values are.

Suppose a function \(f\) takes only three distinct values:

\[
f(x)=
\begin{cases}
1,&x\in A_1,\\
3,&x\in A_2,\\
5,&x\in A_3,
\end{cases}
\]

where

\[
[0,1]=A_1\sqcup A_2\sqcup A_3.
\]

Assume these sets are all measurable.

Instead of dividing the horizontal axis into ever more small intervals, we can ask directly:

How large is the set where the function equals 1?

Where it equals 3?

Where it equals 5?

We naturally obtain

\[
\boxed{
\int f\,dm
=
1\cdot m(A_1)
+3\cdot m(A_2)
+5\cdot m(A_3).
}
\]

Is this not the weighted average with which we began?

The weights are now the measures of the sets corresponding to each function value, rather than the probabilities of three discrete outcomes.

Now reconsider the Dirichlet function.

\[
f=\mathbf1_{\mathbb Q\cap[0,1]}.
\]

It takes only two values:

\[
0,\qquad1.
\]

The set where it equals 1 is

\[
\mathbb Q\cap[0,1],
\]

and its Lebesgue measure is 0.

The set where it equals 0 is the irrational part, whose measure is 1.

Thus:

\[
\begin{aligned}
\int_0^1f\,dm
&=
1\cdot m(\mathbb Q\cap[0,1])\\
&\quad+
0\cdot m([0,1]\setminus\mathbb Q)\\
&=0.
\end{aligned}
\]

The problem is solved.

There is a subtle distinction here.

We did not change the function itself.

Nor did we find a way to make it continuous.

We changed how we measure and accumulate its values.

**A function may fluctuate with extreme irregularity across its domain while still having a very simple structure in terms of measure.**

This is one of the most important changes of viewpoint in Lebesgue integration.

So far, however, we have handled only functions taking finitely many values.

The real difficulty is:

What should we do when a function takes infinitely many values?

---

## 6.4 Begin with the Simplest Functions: Integration Is Weighted Summation

In Chapter 5, we discovered an important method.

When we cannot directly measure arbitrarily complicated sets, we can begin with intervals and extend to more general sets through suitable limiting procedures.

We now apply a similar method to functions.

Do not try to integrate arbitrarily complicated measurable functions from the outset.

Study the simplest functions first, then gradually extend the reach of integration.

### 6.4.1 The Birth of Simple Functions

Let \((\Omega,\mathcal F,\mu)\) be a measure space.

Consider a function

\[
s:\Omega\to[0,\infty)
\]

and suppose it takes only finitely many distinct values:

\[
a_1,\ldots,a_m.
\]

If every set

\[
A_i=\{\omega:s(\omega)=a_i\}
\]

is measurable, we can write

\[
\boxed{
s=\sum_{i=1}^ma_i\mathbf1_{A_i}.
}
\]

Such a function is called a nonnegative simple function.

Notice that we have not required the sets \(A_i\) to be intervals.

They may be complicated Borel sets, measurable subsets of the Cantor set, or events in a general probability space.

Because these sets are pairwise disjoint, we can naturally define:

\[
\boxed{
\int_\Omega s\,d\mu
=
\sum_{i=1}^ma_i\mu(A_i).
}
\]

When \(a_i=0\), the corresponding term is defined to be 0, even if \(\mu(A_i)=\infty\).

This is the integral of a simple function.

If \(\mu=P\) is a probability measure, it returns exactly to the expectation formula from Chapter 1:

\[
\mathbb E[s]
=
\sum_{i=1}^ma_iP(A_i).
\]

We can see:

**Lebesgue integration begins by extending finite weighted summation to measurable sets, rather than by introducing an entirely unfamiliar operation.**

It preserves all our earlier basic intuitions about expectation.

For example, for nonnegative simple functions \(s,t\) and constants \(a,b\ge0\),

\[
\int(as+bt)\,d\mu
=
a\int s\,d\mu+b\int t\,d\mu.
\]

Why?

Using the sets on which \(s,t\) take their respective values, we can construct a common finite measurable partition.

On each part, both functions are constant, so the equality above follows simply from distributivity of finite sums and finite additivity of measure.

Likewise, if

\[
0\le s\le t,
\]

then

\[
\int s\,d\mu\le\int t\,d\mu.
\]

All these properties are natural for simple functions.

The real question is how to proceed from simple functions to general measurable functions.

### 6.4.2 Why Can Every Nonnegative Measurable Function Be Approximated by Simple Functions?

Suppose

\[
f:\Omega\to[0,\infty]
\]

is a nonnegative measurable function.

We want a sequence of simple functions

\[
s_1,s_2,\ldots
\]

such that

\[
0\le s_1\le s_2\le\cdots
\]

and

\[
s_n(\omega)\uparrow f(\omega)
\]

for every \(\omega\).

Can this be done?

A natural idea is to divide the axis of function values into increasingly small intervals.

For example, use intervals of length \(1/2\) on the first step.

Use intervals of length \(1/4\) on the second.

At step \(n\), use intervals of length \(2^{-n}\).

Then round each function value down to the nearest grid point.

To ensure finitely many values at every step, also truncate the function at \(n\).

Define

\[
\boxed{
s_n(\omega)
=
2^{-n}\left\lfloor
2^n\min\{f(\omega),n\}
\right\rfloor.
}
\]

Here \(f(\omega)=\infty\) is permitted.

The expression may look complicated, but its meaning is simple:

First, disregard function values beyond \(n\).

Then approximate the remaining part from below with precision \(2^{-n}\).

For every \(n\), \(s_n\) takes only finitely many values and is therefore simple.

Because \(f\) is measurable, each of its level sets is measurable too.

Moreover, as \(n\) increases, the truncation level rises and the mesh becomes finer, so

\[
s_n\le s_{n+1}.
\]

Finally,

\[
\boxed{s_n(\omega)\uparrow f(\omega).}
\]

We have obtained an important construction theorem:

**Every nonnegative measurable function can be approximated pointwise by a monotonically increasing sequence of nonnegative simple functions.**

This step is one of the foundations of Lebesgue integration.

It tells us that however complicated the values and variations of \(f\) may be, we can still approximate it progressively through finite weighted summation.

### 6.4.3 If We Can Approximate, Why Not Define the Integral Directly?

We now know how to integrate simple functions.

And every nonnegative measurable function can be approximated from below by simple functions.

A very natural idea therefore arises:

Collect the integrals of all simple functions lying below \(f\), then take their supremum.

Thus define

\[
\boxed{
\int_\Omega f\,d\mu
=
\sup\left\{
\int_\Omega s\,d\mu:
0\le s\le f,\ s\text{ is a simple function}
\right\}.
}
\]

This is the Lebesgue integral of a nonnegative measurable function.

Its value may at this stage be \(+\infty\).

But this is no defect in the definition.

It is an outcome the theory deliberately permits.

We do not yet require every random variable to have a finite expectation, since that would force us to exclude many natural probability models.

Now look again at this definition.

It extends the familiar finite weighted sum:

\[
\sum_{i=1}^ma_i\mu(A_i)
\]

to general measurable functions:

\[
\int f\,d\mu.
\]

It uses no continuity of the function, requires no density, and does not even require \(\Omega\) to be an interval of real numbers.

It can therefore handle random variables, random functions, and measurable objects on even more abstract spaces.

But now a truly important difficulty appears.

We know that \(s_n\uparrow f\).

May we conclude:

\[
\int s_n\,d\mu\longrightarrow\int f\,d\mu?
\]

Only if the answer is yes does our entire approach of approximating general functions by simple functions truly work.

This is the problem solved by the monotone convergence theorem.

---

## 6.5 Beppo Levi: Why Does Approximation from Below Lose No Integral?

![Beppo Levi Italian mathematician historical portrait](assets/images/03-01.img)

[Original image source](https://site.unibo.it/indam-bologna/en)

**Beppo Levi（1875—1961）**

An Italian mathematician. The important convergence result he proved in 1906 is now usually called Beppo Levi’s theorem or the monotone convergence theorem.

There is a historical detail worth noticing here.

Modern measure-theory textbooks often teach the “monotone convergence theorem, Fatou’s lemma, dominated convergence theorem” in that order.

The historical sequence was not quite the same. Lebesgue’s 1902 dissertation already contained the idea of bounded convergence, while Beppo Levi and Fatou made important contributions in 1906; more general forms of dominated convergence developed in Lebesgue’s later work.〔[57](#ref-turn817174search0)〕

We shall continue by following the natural mathematical questions.

### Theorem 6.1: Monotone Convergence Theorem

> Editorial supplement: The limit function \(f\) is also assumed nonnegative and measurable; on an incomplete space, almost everywhere convergence should be interpreted using a measurable version of the limit. See Appendix E.

Let \(f_1,f_2,\ldots\) be nonnegative measurable functions satisfying

\[
0\le f_1\le f_2\le\cdots
\]

and

\[
f_n(\omega)\uparrow f(\omega)
\]

almost everywhere.

Then

\[
\boxed{
\lim_{n\to\infty}
\int_\Omega f_n\,d\mu
=
\int_\Omega f\,d\mu.
}
\]

Both sides are permitted to equal \(+\infty\).

This theorem is exceptionally powerful.

It does not require \(\mu(\Omega)\) to be finite.

It does not require a uniform upper bound on the \(f_n\).

It does not even require their integrals to be finite.

It requires only nonnegativity and monotone increase.

Why are these two conditions so effective?

### 6.5.1 Proof: First Understand the Easy Direction

Since

\[
f_n\le f,
\]

monotonicity of the integral gives

\[
\int f_n\,d\mu\le\int f\,d\mu.
\]

Hence

\[
\lim_{n\to\infty}\int f_n\,d\mu
\le
\int f\,d\mu.
\]

This part presents no difficulty.

The real issue is the reverse direction:

\[
\int f\,d\mu
\le
\lim_{n\to\infty}\int f_n\,d\mu.
\]

We must prove:

Although the \(f_n\) always lie below \(f\), their integrals cannot permanently miss some part of \(f\).

### 6.5.2 The Key to the Proof: Compare with an Arbitrary Simple Function

Take any nonnegative simple function \(s\) satisfying

\[
s\le f.
\]

We want to prove

\[
\int s\,d\mu
\le
\lim_{n\to\infty}\int f_n\,d\mu.
\]

If this holds for every such \(s\), taking the supremum over \(s\) gives the result.

But we cannot simply assert that for some sufficiently large \(n\) we must have \(f_n\ge s\).

The functions \(f_n\) may keep approaching \(f\) from below without ever reaching portions of \(s=f\) exactly.

To get around this, introduce a slightly smaller factor.

Take any

\[
0<c<1.
\]

Define

\[
A_n=\{\omega:f_n(\omega)\ge c\,s(\omega)\}.
\]

Because \(f_n\uparrow f\) and \(s\le f\), we can show

\[
A_n\uparrow\Omega
\]

on the set where pointwise convergence holds.

Indeed, if \(s(\omega)>0\), then

\[
f(\omega)\ge s(\omega)>c\,s(\omega),
\]

Thus, for sufficiently large \(n\),

\[
f_n(\omega)\ge c\,s(\omega).
\]

If \(s(\omega)=0\), then because \(f_n\ge0\), this inequality holds for every \(n\).

Hence

\[
f_n\ge c\,s\mathbf1_{A_n}.
\]

By monotonicity of the integral,

\[
\int f_n\,d\mu
\ge
c\int s\mathbf1_{A_n}\,d\mu.
\]

Since \(s\) is simple, we can write

\[
s=\sum_{j=1}^ma_j\mathbf1_{E_j}.
\]

Thus

\[
\int s\mathbf1_{A_n}\,d\mu
=
\sum_{j=1}^ma_j\mu(E_j\cap A_n).
\]

Because

\[
E_j\cap A_n\uparrow E_j
\]

holds after removing a null set, and Chapter 5 established continuity of measure along increasing sequences of sets,

\[
\mu(E_j\cap A_n)\uparrow\mu(E_j).
\]

Therefore

\[
\lim_{n\to\infty}
\int s\mathbf1_{A_n}\,d\mu
=
\int s\,d\mu.
\]

Hence

\[
\lim_{n\to\infty}\int f_n\,d\mu
\ge c\int s\,d\mu.
\]

Letting \(c\uparrow1\) gives

\[
\lim_{n\to\infty}\int f_n\,d\mu
\ge\int s\,d\mu.
\]

This holds for every simple function satisfying \(0\le s\le f\).

Taking the supremum therefore gives:

\[
\lim_{n\to\infty}\int f_n\,d\mu
\ge
\sup_{0\le s\le f}
\int s\,d\mu
=
\int f\,d\mu.
\]

Combining the two directions,

\[
\boxed{
\int f_n\,d\mu\uparrow\int f\,d\mu.
}
\]

This completes the proof.

### 6.5.3 What Does This Theorem Really Reveal?

I believe the most memorable feature here is more than the auxiliary set \(A_n\) used in the proof.

It is a deeper principle:

**We can recover the integral of a nonnegative function by continually adding known information and improving approximations from below, without losing any positive contribution to the integral.**

In Chapter 5, we saw that probability measures satisfy

\[
A_n\uparrow A
\implies P(A_n)\uparrow P(A).
\]

Now, in Chapter 6, we find the corresponding statement for functions:

\[
f_n\uparrow f
\implies
\int f_n\,dP\uparrow\int f\,dP.
\]

The connection is entirely natural.

Indeed, choosing

\[
f_n=\mathbf1_{A_n},
\]

gives

\[
\int f_n\,dP=P(A_n).
\]

Continuity of measure from below can therefore be viewed as the monotone convergence theorem applied to indicator functions.

Conversely, the monotone convergence theorem extends this continuity from sets to general nonnegative measurable functions.

This is precisely the unity we have been seeking:

\[
\boxed{
\text{limits of sets}
\quad\longrightarrow\quad
\text{limits of functions}
}
\]

Probability and integration are no longer two unrelated theories.

Integration is the natural extension of the idea of measure to functions.

---

## 6.6 A New Difficulty: Not Every Random Variable Has a Finite Expectation

So far, we have discussed only nonnegative measurable functions.

Gambling payoffs, however, can be negative.

Random variables in the real world can also take both positive and negative values.

How should we define their integrals?

The most natural method is to separate a real-valued function into its positive and negative parts.

Define

\[
f^+=\max\{f,0\},
\]

\[
f^-=\max\{-f,0\}.
\]

Then

\[
f=f^+-f^-,
\]

and

\[
|f|=f^++f^-.
\]

Since \(f^+,f^-\) are both nonnegative measurable functions, we already know how to define their integrals.

We therefore try defining

\[
\boxed{
\int f\,d\mu
=
\int f^+\,d\mu-\int f^-\,d\mu.
}
\]

But there is a problem.

If

\[
\int f^+\,d\mu=\infty,
\qquad
\int f^-\,d\mu=\infty,
\]

we obtain

\[
\infty-\infty.
\]

This expression has no well-defined mathematical meaning.

We must therefore require at least one of the two integrals to be finite before defining their difference as an extended-real integral.

If we further require

\[
\int|f|\,d\mu<\infty,
\]

then both integrals of \(f^+,f^-\) are finite.

We say that \(f\) is integrable.

On a probability space, this corresponds to

\[
\boxed{
\mathbb E[|X|]<\infty.
}
\]

It ensures that \(\mathbb E[X]\) is a finite real number.

### 6.6.1 A Game with Finite Payoffs but Infinite Expectation

Consider a new game of chance.

A player uses some randomizing device and receives a random payoff \(X\).

Suppose

\[
P(X=2^n)=2^{-n},
\qquad n=1,2,\ldots.
\]

This is a valid probability distribution because

\[
\sum_{n=1}^{\infty}2^{-n}=1.
\]

Moreover, \(X\) takes a finite value in every actual trial.

In other words,

\[
P(X<\infty)=1.
\]

But calculating its expectation gives:

\[
\begin{aligned}
\mathbb E[X]
&=\sum_{n=1}^{\infty}2^nP(X=2^n)\\
&=\sum_{n=1}^{\infty}2^n2^{-n}\\
&=\sum_{n=1}^{\infty}1\\
&=\infty.
\end{aligned}
\]

Thus

\[
\boxed{
X<\infty\text{ a.s.},
\qquad
\mathbb E[X]=\infty.
}
\]

Every actual game pays only a finite amount, yet its theoretical average payoff is infinite.

This has the same basic structure as the famous St. Petersburg paradox.

It forces us to distinguish anew:

A random variable’s being almost surely finite and its having a finite expectation are different matters.

Furthermore, an infinite expectation does not mean that a person should be willing to pay any entrance fee, however high. Real decisions also involve wealth constraints, utility, risk, and ability to pay.

The “fair value” we used in Chapter 1 corresponds to mathematical expectation under specific pricing assumptions. It does not automatically equal everyone’s subjective valuation when facing risk.

### 6.6.2 Why Does the Cauchy Distribution Have No Expectation?

In Chapter 3, we encountered the standard Cauchy distribution:

\[
f(x)=\frac1{\pi(1+x^2)}.
\]

Because the density is symmetric about the origin, one might immediately conclude

\[
\mathbb E[X]=0.
\]

But this inference is dangerous.

We must examine the positive and negative parts separately.

For the positive part,

\[
\begin{aligned}
\mathbb E[X^+]
&=\int_0^\infty\frac{x}{\pi(1+x^2)}\,dx\\
&=\frac1{2\pi}
\lim_{R\to\infty}\log(1+R^2)\\
&=\infty.
\end{aligned}
\]

By symmetry,

\[
\mathbb E[X^-]=\infty.
\]

Thus

\[
\mathbb E[X]
=
\mathbb E[X^+]-\mathbb E[X^-]
\]

is undefined.

Although the symmetrically truncated integrals satisfy

\[
\lim_{R\to\infty}
\int_{-R}^{R}\frac{x}{\pi(1+x^2)}\,dx=0,
\]

this is only the result of symmetric truncation in the sense of a Cauchy principal value, not an expectation in the Lebesgue sense.

We thereby learn:

**Integration theory must tell us not only how to calculate an average, but also when an average does not exist at all.**

This is the value of a rigorous definition.

---

## 6.7 Why Can We Not Freely Interchange Limits and Expectations?

We are finally ready to examine another of this chapter’s central questions.

Suppose we have a sequence of random variables

\[
X_1,X_2,\ldots
\]

and

\[
X_n\longrightarrow X
\]

almost everywhere.

May we immediately conclude

\[
\mathbb E[X_n]\longrightarrow\mathbb E[X]?
\]

This seems entirely reasonable.

If the values of the random variables are converging, why should their averages not converge as well?

Reality, however, is far less simple.

### 6.7.1 A Spike That Grows Narrower and Taller

Take Lebesgue measure on the interval \([0,1]\) and define

\[
f_n(x)=n\mathbf1_{(0,1/n)}(x).
\]

This function takes only two values:

\[
f_n(x)=
\begin{cases}
n,&0<x<1/n,\\
0,&\text{elsewhere}.
\end{cases}
\]

As \(n\) increases, the region where the function is nonzero narrows, while its height increases.

<div class="experiment" data-widget="spike"></div>

Shrinking-spike experiment: \(f_n=n\mathbf1_{(0,1/n)}\). The nonzero interval has width \(1/n\) and integral 1. The vertical axis uses a fixed scale for the selected n. The spike grows narrower, but its area always remains 1.

For any fixed \(x\in[0,1]\), eventually

\[
f_n(x)=0.
\]

so

\[
\boxed{f_n(x)\longrightarrow0}
\]

at every point.

Yet

\[
\begin{aligned}
\int_0^1f_n(x)\,dx
&=
n\cdot\frac1n\\
&=1.
\end{aligned}
\]

Thus

\[
\boxed{
\lim_{n\to\infty}\int_0^1f_n(x)\,dx
=1
\ne
0
=
\int_0^1\lim_{n\to\infty}f_n(x)\,dx.
}
\]

We do not even need complicated probability distributions here.

A sequence of very simple nonnegative functions already shows that pointwise convergence does not guarantee convergence of integrals.

What happened?

As \(n\) increases, the function’s entire contribution to the integral concentrates in an ever smaller region.

The spike eventually leaves every fixed point behind.

The pointwise limit therefore sees none of this contribution.

Yet the total area of each spike remains 1.

We may call this **concentration of mass**.

There is another, similar mechanism of failure.

On the whole real line, consider

\[
g_n(x)=\mathbf1_{(n,n+1)}(x).
\]

Again,

\[
g_n(x)\to0
\]

for every fixed \(x\).

But

\[
\int_{\mathbb R}g_n(x)\,dx=1.
\]

Here the mass does not concentrate in a shrinking interval.

It simply keeps moving toward infinity.

We may call this **escape of mass**.

We have therefore identified two reasons why limits of integrals can fail:

Excessive local concentration of mass, and mass escaping to infinity.

We now need a theorem that at least gives a universally valid estimate without demanding a complete interchange of limits and integrals.

This is Fatou’s lemma.

---

## 6.8 Fatou’s Lemma: What Can We Retain Even When Limits Cannot Be Interchanged?

### Theorem 6.2: Fatou’s Lemma

Let \(f_1,f_2,\ldots\) be nonnegative measurable functions.

Then

\[
\boxed{
\int_\Omega\liminf_{n\to\infty}f_n\,d\mu
\le
\liminf_{n\to\infty}\int_\Omega f_n\,d\mu.
}
\]

We do not require \(f_n\) to be monotone.

We do not even require \(f_n\) itself to have a pointwise limit.

We use only the lower limit:

\[
\liminf_{n\to\infty}f_n.
\]

The theorem can be understood as follows:

**In a limiting sequence of nonnegative functions, contributions to the integral may disappear, but the integral of the lower-limit function cannot exceed the lower limit of the original integrals.**

The spike example shows precisely how this inequality can be strict:

\[
0<1.
\]

### 6.8.1 Why Does Fatou’s Lemma Follow from Monotone Convergence?

Define

\[
h_n(\omega)=\inf_{k\ge n}f_k(\omega).
\]

Since we take infima over progressively smaller sets,

\[
h_1\le h_2\le\cdots.
\]

and

\[
h_n\uparrow\liminf_{n\to\infty}f_n.
\]

We may therefore apply the monotone convergence theorem:

\[
\int\liminf_{n\to\infty}f_n\,d\mu
=
\lim_{n\to\infty}\int h_n\,d\mu.
\]

On the other hand, for every \(k\ge n\),

\[
h_n\le f_k.
\]

so

\[
\int h_n\,d\mu
\le
\inf_{k\ge n}\int f_k\,d\mu.
\]

Letting \(n\to\infty\) gives

\[
\begin{aligned}
\int\liminf_{n\to\infty}f_n\,d\mu
&=
\lim_n\int h_n\,d\mu\\
&\le
\lim_n\inf_{k\ge n}\int f_k\,d\mu\\
&=
\liminf_{n\to\infty}\int f_n\,d\mu.
\end{aligned}
\]

This completes the proof.

This proof illustrates an important strategy in measure theory.

When the original sequence is not monotone, we can construct a new increasing sequence by taking infima over its tails.

The monotone convergence theorem can then solve a problem that was not initially monotone.

Fatou’s lemma is no magical rule completely independent of monotone convergence.

It develops naturally from that foundational structure.

But Fatou’s lemma still gives only a one-sided inequality.

To interchange integrals and limits fully, we must control the contributions that could concentrate or escape.

This leads us to one of the most frequently used theorems of Lebesgue integration.

---

## 6.9 The Dominated Convergence Theorem: What Can Prevent Integral Mass from Disappearing?

Reconsider the earlier counterexample:

\[
f_n(x)=n\mathbf1_{(0,1/n)}(x).
\]

The problem is that although the function is nonzero only on a tiny region, its height becomes arbitrarily large as \(n\) increases.

If we could find a fixed integrable function \(g\) such that every \(f_n\) satisfies

\[
|f_n|\le g,
\]

could we prevent this loss of control?

Indeed, this is the core of the dominated convergence theorem.

### Theorem 6.3: Lebesgue’s Dominated Convergence Theorem

> Editorial supplement: The limit function \(f\) below is taken to be measurable; functions may be real or complex, with the proof interpreted componentwise as appropriate. See Appendix E.

Let \(f_n\) be a sequence of measurable functions, with

\[
f_n\longrightarrow f
\qquad\mu\text{-a.e.}
\]

Suppose there exists a nonnegative integrable function \(g\) such that

\[
|f_n|\le g
\qquad\mu\text{-a.e.}
\]

for every \(n\).

Then \(f\) is integrable, and

\[
\boxed{
\lim_{n\to\infty}\int f_n\,d\mu
=
\int f\,d\mu.
}
\]

In fact, we obtain the stronger conclusion:

\[
\boxed{
\int|f_n-f|\,d\mu\longrightarrow0.
}
\]

This second conclusion shows that dominated convergence actually gives \(L^1\) convergence, not merely convergence of the numerical integrals.

This will matter when we systematically study modes of random convergence.

### 6.9.1 Why Is an Integrable Upper Bound So Effective?

If

\[
|f_n|\le g
\]

and

\[
\int g\,d\mu<\infty,
\]

then for every measurable set \(A\),

\[
\int_A|f_n|\,d\mu
\le
\int_Ag\,d\mu.
\]

Since \(g\) is integrable, its integral is absolutely continuous:

For any \(\varepsilon>0\), there exists \(\delta>0\) such that

\[
\mu(A)<\delta
\implies
\int_Ag\,d\mu<\varepsilon.
\]

Thus, however large \(n\) becomes, \(f_n\) cannot retain a fixed contribution to the integral in a region of arbitrarily small measure.

Likewise, for the integrable function \(g\) with finite integral, we can control the tail contribution from distant parts of the space; in a general measure space, the corresponding integrability control can be expressed through a suitable exhaustion by sets of finite measure.

A fixed integrable upper bound therefore excludes exactly the uncontrolled integral mass present in our two earlier counterexamples.

This explains why dominated convergence requires an integrable dominating function, rather than simply some bound on function values.

For example, on an infinite-measure space,

\[
|f_n|\le1
\]

need not suffice.

The earlier functions

\[
g_n=\mathbf1_{(n,n+1)}
\]

all satisfy \(|g_n|\le1\), yet we still cannot interchange limit and integral, because the constant function 1 is not integrable on the whole real line.

### 6.9.2 A Rigorous Proof of the Dominated Convergence Theorem

Now that we have Fatou’s lemma, the proof is quite concise.

Since

\[
|f_n|\le g
\]

and \(f_n\to f\) almost everywhere,

\[
|f|\le g
\]

almost everywhere.

Thus \(f\) is integrable.

Also,

\[
g+f_n\ge0,
\qquad
g-f_n\ge0.
\]

First apply Fatou’s lemma to the nonnegative functions \(g+f_n\):

\[
\int(g+f)\,d\mu
\le
\liminf_{n\to\infty}
\int(g+f_n)\,d\mu.
\]

Because \(g\) is integrable, we may legitimately subtract \(\int g\,d\mu\), obtaining

\[
\boxed{
\int f\,d\mu
\le
\liminf_{n\to\infty}\int f_n\,d\mu.
}
\]

Next apply Fatou’s lemma to \(g-f_n\):

\[
\int(g-f)\,d\mu
\le
\liminf_{n\to\infty}\int(g-f_n)\,d\mu.
\]

Thus

\[
\int g\,d\mu-\int f\,d\mu
\le
\int g\,d\mu-
\limsup_{n\to\infty}\int f_n\,d\mu.
\]

Rearranging gives

\[
\boxed{
\limsup_{n\to\infty}\int f_n\,d\mu
\le
\int f\,d\mu.
}
\]

Combining the two inequalities:

\[
\int f\,d\mu
\le
\liminf_n\int f_n\,d\mu
\le
\limsup_n\int f_n\,d\mu
\le
\int f\,d\mu.
\]

Hence

\[
\boxed{
\lim_{n\to\infty}\int f_n\,d\mu
=
\int f\,d\mu.
}
\]

Finally, since

\[
|f_n-f|\longrightarrow0
\]

almost everywhere, and

\[
|f_n-f|\le2g,
\]

applying the integral-convergence conclusion just proved to the new sequence of nonnegative functions \(|f_n-f|\) gives

\[
\boxed{
\int|f_n-f|\,d\mu\longrightarrow0.
}
\]

This completes the proof.

### 6.9.3 The Relationship Among the Three Convergence Theorems

Let us review the three results we have established.

| Theorem | Essential conditions | Conclusion |
|---|---|---|
| Monotone convergence | \(0\le f_n\uparrow f\) | Integral and limit can be interchanged; infinite integrals are allowed |
| Fatou’s lemma | \(f_n\ge0\) | A one-sided inequality involving lower limits |
| Dominated convergence | \(f_n\to f\) a.e., \(|f_n|\le g\in L^1\) | Integrals converge, and \(f_n\to f\) in \(L^1\) |

We see that these three theorems are not isolated pieces of knowledge.

They all answer the same question:

\[
\boxed{
\text{When can a limit be moved inside an integral？}
}
\]

We simply have different amounts of information for different sequences of functions.

If the functions increase monotonically, we can exploit approximation from below in the structure of the nonnegative integral.

If they are not monotone but remain nonnegative, Fatou’s lemma at least supplies a lower bound.

If they share an integrable dominating function, we can obtain full convergence.

This is a mathematical language of increasing precision.

The familiar order of these proofs primarily reflects modern mathematical logic, rather than the historical order of discovery. Beppo Levi, Fatou, Lebesgue, and Vitali made interconnected contributions to limits of integrals in the early twentieth century.〔[57](#ref-turn817174search0)〕

---

## 6.10 Why Can Integration Unify the Distributions of All Random Variables?

We have now rigorously established the Lebesgue integral.

We can return to probability and resolve a question that has repeatedly arisen.

Suppose

\[
X:(\Omega,\mathcal F,P)\to(\mathbb R,\mathcal B(\mathbb R))
\]

is a random variable.

We want to calculate

\[
\mathbb E[h(X)]
\]

where \(h:\mathbb R\to\mathbb R\) is Borel measurable.

Must we know how \(X\) was constructed on the original sample space?

Not necessarily.

In fact, knowing the distribution of \(X\) suffices to calculate the expectations of all corresponding integrable functions.

### 6.10.1 Begin the Proof with Simple Functions

Recall Chapter 5:

\[
P_X(B)=P(X^{-1}(B)).
\]

First consider a simple function:

\[
h=\sum_{i=1}^ma_i\mathbf1_{B_i},
\]

where the \(B_i\) are Borel sets.

Then

\[
h(X)
=
\sum_{i=1}^ma_i\mathbf1_{\{X\in B_i\}}.
\]

Hence

\[
\begin{aligned}
\mathbb E[h(X)]
&=\sum_{i=1}^ma_iP(X\in B_i)\\
&=\sum_{i=1}^ma_iP_X(B_i)\\
&=\int_{\mathbb R}h(x)\,P_X(dx).
\end{aligned}
\]

For a nonnegative Borel measurable function \(h\), choose a sequence of simple functions

\[
h_n\uparrow h.
\]

Then apply the monotone convergence theorem to both sides to obtain

\[
\boxed{
\mathbb E[h(X)]
=
\int_{\mathbb R}h(x)\,P_X(dx).
}
\]

For general integrable \(h(X)\), extend the result using positive and negative parts.

This integral formula is often called the *law of the unconscious statistician*. Essentially, it is the change-of-variables formula for integration under a pushforward measure.

It tells us:

**If we only want the expectation of a function of a random variable, we do not need to know the construction of the entire probability space behind it.**

We need only its distribution measure \(P_X\).

This is a remarkably powerful abstraction.

### 6.10.2 Discrete and Continuous Distributions Are Merely Special Cases

If \(X\) is discrete, taking values \(x_i\) with corresponding weights \(p_i\), then

\[
P_X=\sum_i p_i\delta_{x_i}.
\]

Here \(\delta_{x_i}\) is the Dirac measure concentrated at \(x_i\).

Thus

\[
\int h(x)\,P_X(dx)
=
\sum_i h(x_i)p_i.
\]

We have returned to weighted summation.

If the distribution of \(X\) has a density \(f_X\) with respect to Lebesgue measure, then

\[
P_X(dx)=f_X(x)\,dx.
\]

so

\[
\int h(x)\,P_X(dx)
=
\int_{\mathbb R}h(x)f_X(x)\,dx.
\]

We have returned to the familiar formula for continuous random variables.

Now, however, consider a more unusual random variable.

Suppose \(X\) has the Cantor distribution.

Its distribution function is continuous and it has no point atoms, yet its distribution is concentrated on the Cantor set, which has Lebesgue measure zero.

It is therefore neither discrete nor equipped with a probability density relative to Lebesgue measure.

Nevertheless,

\[
\boxed{
\mathbb E[h(X)]
=
\int_{\mathbb R}h(x)\,P_X(dx)
}
\]

remains perfectly valid.

We finally understand why modern probability should not define expectation as

\[
\sum_xxf(x)
\]

or

\[
\int xf(x)\,dx.
\]

since these cover only particular types of distributions.

The truly general form is

\[
\boxed{
\mathbb E[X]
=
\int_\Omega X\,dP
=
\int_{\mathbb R}x\,P_X(dx),
}
\]

provided that the relevant integral is defined.

This is entirely consistent with the outlook of the whole book.

We are not inventing a new theory unrelated to the old methods.

We have found a larger mathematical structure in which the old methods become special cases.

---

## 6.11 An Unexpected Formula: Expectation Can Also Be Calculated from Tail Probabilities

We already know that the expectation of a nonnegative random variable is

\[
\mathbb E[X]=\int_\Omega X\,dP.
\]

But if we do not directly know the density of \(X\) and know only its tail probabilities

\[
P(X>t),
\]

can we still calculate its expectation?

For a nonnegative real number \(x\), there is a simple identity:

\[
\boxed{
x=\int_0^\infty\mathbf1_{\{x>t\}}\,dt.
}
\]

Why?

Because when \(x\ge0\),

\[
\mathbf1_{\{x>t\}}
=
\begin{cases}
1,&0\le t<x,\\
0,&t\ge x.
\end{cases}
\]

so the right-hand side is simply the length of an interval of length \(x\).

Replacing \(x\) with a nonnegative random variable \(X(\omega)\) gives

\[
X(\omega)
=
\int_0^\infty\mathbf1_{\{X(\omega)>t\}}\,dt.
\]

Hence

\[
\mathbb E[X]
=
\int_\Omega
\left(
\int_0^\infty
\mathbf1_{\{X(\omega)>t\}}\,dt
\right)P(d\omega).
\]

If we may interchange these two integrals, then

\[
\begin{aligned}
\mathbb E[X]
&=
\int_0^\infty
\left(
\int_\Omega
\mathbf1_{\{X(\omega)>t\}}P(d\omega)
\right)dt\\
&=
\int_0^\infty P(X>t)\,dt.
\end{aligned}
\]

Thus

\[
\boxed{
\mathbb E[X]
=
\int_0^\infty P(X>t)\,dt.
}
\]

This is sometimes called the tail integral formula or the layer-cake representation.

It reveals another interpretation of expectation:

**The expectation of a nonnegative random variable can be understood as the accumulated probabilities of all its tail events.**

For example, suppose

\[
P(X>t)=e^{-\lambda t},
\qquad t\ge0.
\]

Then

\[
\mathbb E[X]
=
\int_0^\infty e^{-\lambda t}\,dt
=
\frac1\lambda.
\]

Without first using a probability density, we obtained the expectation directly from tail probabilities.

This is especially important for heavy-tailed distributions.

If, for sufficiently large \(t\),

\[
P(X>t)\asymp t^{-\alpha},
\]

then the tail integral

\[
\int_1^\infty t^{-\alpha}\,dt
\]

is finite if and only if \(\alpha>1\).

Thus the rate of tail decay directly determines whether expectation is finite.

But our derivation left one question unresolved:

Why may we interchange the two integrals?

This leads us to the chapter’s final important theorem.

---

## 6.12 Fubini–Tonelli: When May We Change the Order of Summation and Integration?

> Editorial supplement: Appendix C gives expanded proofs concerning sections of product sets, the monotone-class step, and the construction of product measure.

Recall Chapter 1.

On finite probability spaces, we can freely change the order of finite summation:

\[
\sum_{i=1}^m\sum_{j=1}^na_{ij}
=
\sum_{j=1}^n\sum_{i=1}^ma_{ij}.
\]

This is an utterly ordinary algebraic property.

But when we study infinitely many random outcomes, may we still freely interchange sums and integrals?

Consider a random system with two components, whose outcome space is

\[
\Omega_1\times\Omega_2.
\]

We want to take a function

\[
f:\Omega_1\times\Omega_2\to\mathbb R
\]

and calculate its integral.

We could integrate first in the second variable and then in the first.

Or we could reverse the order.

The question is:

\[
\boxed{
\int_{\Omega_1}
\left(
\int_{\Omega_2}f(x,y)\,\nu(dy)
\right)\mu(dx)
\overset{?}{=}
\int_{\Omega_2}
\left(
\int_{\Omega_1}f(x,y)\,\mu(dx)
\right)\nu(dy).
}
\]

Are these two expressions really equal in general?

To answer this, we must first understand product measure.

### 6.12.1 How Can We Assign Measure to the Joint Outcomes of Two Spaces?

Suppose

\[
(\Omega_1,\mathcal F_1,\mu)
\]

and

\[
(\Omega_2,\mathcal F_2,\nu)
\]

are two measure spaces.

For a rectangle

\[
A\times B,
\]

the most natural definition is

\[
(\mu\times\nu)(A\times B)=\mu(A)\nu(B).
\]

When \(\mu,\nu\) are probability measures, this agrees exactly with the multiplication rule for independent events.

Defining measure only on rectangles, however, is insufficient.

The joint space contains many sets that cannot be written as a single rectangle.

We therefore need the following \(\sigma\)-algebra generated by measurable rectangles:

\[
\mathcal F_1\otimes\mathcal F_2
=
\sigma\{A\times B:A\in\mathcal F_1,B\in\mathcal F_2\}
\]

and must construct a measure on it.

Under the assumption of \(\sigma\)-finiteness, measure extension theory constructs the unique product measure with the required values on rectangles.

Once again, this shows that the measure extension theory of Chapter 5 is far more than an isolated technical issue.

It allows us to construct rigorously, from individual random experiments, a joint space containing several experiments.

### 6.12.2 Tonelli’s Theorem: For Nonnegative Functions, Interchanging the Order Is Always Safe

Now suppose

\[
f:\Omega_1\times\Omega_2\to[0,\infty]
\]

is a nonnegative product-measurable function, and both measure spaces are \(\sigma\)-finite.

Tonelli’s theorem tells us:

\[
\boxed{
\begin{aligned}
\int_{\Omega_1\times\Omega_2}f\,d(\mu\times\nu)
&=
\int_{\Omega_1}
\left(\int_{\Omega_2}f(x,y)\,\nu(dy)\right)\mu(dx)\\
&=
\int_{\Omega_2}
\left(\int_{\Omega_1}f(x,y)\,\mu(dx)\right)\nu(dy).
\end{aligned}
}
\]

The integrals are permitted to equal \(+\infty\).

Let us first understand why this holds.

For the indicator of a rectangle,

\[
f=\mathbf1_{A\times B},
\]

the conclusion is simply

\[
(\mu\times\nu)(A\times B)=\mu(A)\nu(B).
\]

For nonnegative simple functions, linearity gives the corresponding formula.

Extending the result to general nonnegative measurable functions also requires a step concerning product-measurable sets and measurability of their sections. Start with rectangles and use a monotone-class argument to extend the integral identity to sets in the product \(\sigma\)-algebra, then to simple functions.

Finally, for any nonnegative measurable function \(f\), choose simple functions

\[
s_n\uparrow f,
\]

and apply the monotone convergence theorem successively to the relevant integrals.

This gives Tonelli’s formula.

Notice the structure.

The multiplicative relation between measures on rectangles is the starting point.

Simple functions turn it into finite weighted summation.

The monotone convergence theorem then extends the finite structure to arbitrary nonnegative measurable functions.

**Tonelli’s theorem shows once more that Lebesgue integration draws its power from the interplay of simple objects, additivity of measure, and limiting operations.**

The tail integral formula from Section 6.11 now has a rigorous justification too.

Since

\[
(\omega,t)\longmapsto
\mathbf1_{\{X(\omega)>t\}}
\]

is nonnegative and product measurable, Tonelli’s theorem lets us interchange the integrals without knowing beforehand that \(\mathbb E[X]\) is finite.

### 6.12.3 Fubini’s Theorem: With Both Signs Present, We Need More Conditions

For general real-valued functions, however, the situation differs.

If positive and negative contributions alternate infinitely, changing the order of integration may change the result or even make an integral undefined.

To understand the danger, begin with a wholly discrete example.

Define a doubly indexed sequence

\[
a_{mn}=
\begin{cases}
1,&n=m,\\
-1,&n=m+1,\\
0,&\text{otherwise},
\end{cases}
\qquad m,n\ge1.
\]

For every fixed \(m\), the row contains exactly one \(1\) and one \(-1\).

Thus

\[
\sum_{n=1}^{\infty}a_{mn}=0.
\]

and hence

\[
\boxed{
\sum_{m=1}^{\infty}
\left(\sum_{n=1}^{\infty}a_{mn}\right)=0.
}
\]

But if we sum over \(m\) first:

The first column contains only a single \(1\), so its sum is 1.

For column \(n\ge2\), there is exactly one \(1\) and one \(-1\), so its sum is 0.

Thus

\[
\boxed{
\sum_{n=1}^{\infty}
\left(\sum_{m=1}^{\infty}a_{mn}\right)=1.
}
\]

We have obtained two different answers!

Why?

Because

\[
\sum_{m,n}|a_{mn}|=\infty.
\]

the total absolute contribution of the positive and negative terms cannot be controlled.

Changing the order of infinite summation can therefore produce different results.

This reminds us:

The interchange property of finite sums cannot be extended without conditions to infinite sums or integrals.

We therefore need a more precise theorem.

### Theorem 6.4: Fubini’s Theorem

Let \(f\) be a product-measurable real-valued function satisfying

\[
\boxed{
\int_{\Omega_1\times\Omega_2}
|f|\,d(\mu\times\nu)<\infty.
}
\]

Then the corresponding iterated integrals exist in the appropriate almost everywhere sense and satisfy

\[
\boxed{
\begin{aligned}
\int_{\Omega_1\times\Omega_2}f\,d(\mu\times\nu)
&=
\int_{\Omega_1}
\left(\int_{\Omega_2}f(x,y)\,\nu(dy)\right)\mu(dx)\\
&=
\int_{\Omega_2}
\left(\int_{\Omega_1}f(x,y)\,\mu(dx)\right)\nu(dy).
\end{aligned}
}
\]

The proof is now very natural.

Decompose \(f\) as

\[
f=f^+-f^-.
\]

Since

\[
f^+,f^-\le|f|,
\]

both of their integrals are finite.

Apply Tonelli’s theorem separately to the two nonnegative functions and subtract the results to obtain Fubini’s theorem.

We have finally found sufficient conditions for changing the order of integration.

**Nonnegativity permits Tonelli’s theorem; absolute integrability permits Fubini’s theorem to handle positive and negative contributions safely.**

These two theorems will recur throughout our later study of joint distributions, conditional expectation, stochastic integration, and stochastic processes.

---

## 6.13 From Fair Prices to Probabilistic Limits: What Have We Created?

We can now return to the gambling problem of Chapter 1.

There, expectation was simply a very elementary formula:

\[
\mathbb E[X]=\sum_i x_ip_i.
\]

After this chapter, we finally understand the entire extensible mathematical structure behind that formula.

On finite spaces, we use weighted sums.

For simple functions, we extend the weights to measures of measurable sets.

For general nonnegative functions, we define integration through monotone approximation by simple functions.

For functions with both signs, we use positive and negative parts to define integrability.

We then study the conditions for interchanging integrals with limits, and integrals with other integrals.

This allows us to use the same expression on extraordinarily complicated probability spaces:

\[
\boxed{
\mathbb E[X]=\int_\Omega X\,dP.
}
\]

But I believe the real value of this formula goes beyond unifying discrete and continuous expectations.

It gives many seemingly different questions in probability the same logical structure.

For example, the law of large numbers studies random averages:

\[
\frac1n\sum_{i=1}^nX_i.
\]

We need to know in what sense these averages converge.

Statistical inference studies sequences of estimators:

\[
\widehat\theta_n.
\]

We need to know when limits can be used to estimate their risks:

\[
\mathbb E[(\widehat\theta_n-\theta)^2].
\]

The theory of stochastic processes studies random variables evolving over time:

\[
X_t.
\]

We need to know when limits and expectations can be interchanged:

\[
\lim_{t\to t_0}\mathbb E[X_t]
\overset{?}{=}
\mathbb E\left[\lim_{t\to t_0}X_t\right].
\]

Brownian motion, encountered in Chapter 4, likewise repeatedly requires this theory of integration and limits.

Lebesgue integration therefore does more than answer how to calculate an average.

One of its more important contributions is a stable mathematical language for analyzing limiting processes.

This makes an interesting comparison with our original understanding of expectation.

Initially, expectation told us how to value random payoffs that had not yet occurred.

Now it has become an integration operation on abstract function spaces.

It handles finite games of chance, but also continuous stochastic processes, singular distributions, random geometry, and infinite-dimensional probability models.

---

# Chapter 6 Conclusion: Integration Is More Than Another Way to Calculate Area

Look back over the ideas of this chapter.

We began by wanting to extend finite weighted averages to continuous spaces.

It seemed we could simply use the Riemann integral.

But the Dirichlet function showed that this integral cannot handle certain elementary indicators of random events.

Instead of treating interval partitions of the domain as our only starting point, we therefore began with the sets corresponding to the values of measurable functions.

We defined the integral of a simple function:

\[
\int s\,d\mu=\sum_i a_i\mu(A_i).
\]

Then, through approximation from below, extended it to general nonnegative measurable functions:

\[
\int f\,d\mu
=
\sup_{0\le s\le f}
\int s\,d\mu.
\]

Finally, positive and negative parts supplied the integral of a general integrable function.

But sequences of functions presented a new difficulty:

Even if

\[
f_n\to f
\]

holds pointwise, it need not follow that

\[
\int f_n\,d\mu\to\int f\,d\mu.
\]

We therefore needed the monotone convergence theorem, Fatou’s lemma, and the dominated convergence theorem.

To interchange two integrals, we also had to establish Tonelli’s and Fubini’s theorems.

A complete theory of integration gradually emerged.

**Finite weighted averages**

\[
\sum_i a_ip_i
\]

**Integration of simple functions**

\[
\int\sum_i a_i\mathbf1_{A_i}\,d\mu
\]

**General measurable functions**

\[
\int f\,d\mu=\sup_{0\le s\le f}\int s\,d\mu
\]

**Expectation in modern probability**

\[
\mathbb E[X]=\int_\Omega X\,dP
\]

Naturally connected with limit theorems, product measures, and stochastic processes

But there is one further question that I believe deserves deeper thought.

We have proved the dominated convergence theorem:

If \(X_n\to X\) almost everywhere, and

\[
|X_n|\le Y,\qquad \mathbb E[Y]<\infty,
\]

then

\[
\mathbb E[|X_n-X|]\to0.
\]

This shows that under suitable conditions, almost sure convergence implies \(L^1\) convergence.

Yet we also saw the spike counterexample:

\[
X_n\to0\quad\text{a.s.},
\]

which satisfies

\[
\mathbb E[|X_n|]=1.
\]

Thus almost sure convergence alone does not imply \(L^1\) convergence.

On the other hand, Chapter 2 discussed:

\[
X_n\xrightarrow{P}X.
\]

Chapter 3 introduced:

\[
X_n\xrightarrow{d}X.
\]

And Chapter 4 even studied:

\[
X_n\Longrightarrow X
\quad\text{in }C([0,1]).
\]

We seem to have acquired many mathematical expressions for “approaching the same random object,” without yet establishing their full connections.

The question therefore arises.

When we say that one sequence of random variables approaches another random variable, what exactly should we require?

Should their values approach one another along each sample path?

Should the probability of a deviation beyond a given threshold become smaller?

Or should only their probability distributions become increasingly similar?

Are these requirements equivalent?

If not, why do we need so many different notions of convergence?

This will mark another exceptionally important change of perspective.

---

# Next Chapter: Chapter 7, “What Does Convergence Really Mean?—Four Kinds of Limits in a Random World”

We will begin with a seemingly counterintuitive question:

> If the probability that an event occurs on trial \(n\) tends to zero, why can it still occur infinitely often almost surely?

This question will take us back to the law of large numbers in Chapter 2 and reveal that decreasing probabilities and the eventual absence of exceptional behavior along a sample path are two different mathematical properties.

We will then gradually develop:

\[
\boxed{
\begin{aligned}
&\text{Almost sure convergence},\\
&\text{Convergence in probability},\\
&L^p\text{ convergence},\\
&\text{Convergence in distribution}.
\end{aligned}
}
\]

We will not merely state their relationships: rigorous counterexamples will show why each reverse implication can fail.

The Borel–Cantelli lemmas, the subsequence principle, uniform integrability, the Portmanteau theorem, and the idea of Skorokhod representation will gradually become natural parts of the story.

Ultimately, we hope to understand:

**Convergence is not an isolated mathematical concept. Choosing a mode of convergence means deciding which kind of information about the random world we want to preserve.**

The Mathematics of Chance · Volume II, Chapter 6 · Working draft v0.1


---

# The Mathematics of Chance
Volume II · Probability in an Infinite World

# Chapter 7: What Does Convergence Mean? Four Limits in a Random World

At the end of [Chapter 6](#chapter-6), we left a spike that was growing narrower and taller.

Choose a point \(U\) uniformly from the interval \([0,1]\), and set

\[
X_n=n\mathbf1_{\{0<U<1/n\}}.
\]

For every fixed sample point, the spike eventually leaves it behind. Thus \(X_n\to0\) holds almost surely. Yet however large we make \(n\),

\[
\mathbb E[X_n]=1.
\]

We have witnessed one limit without obtaining another.

Is the integral refusing to cooperate, or has our understanding of ‘getting closer’ been missing something all along?

Now turn the question around. Suppose the probability of an exception at observation \(n\) tends to zero. Can we guarantee that an actual record of observations eventually contains no more exceptions?

Once again, the answer can be no.

The spike reminds us that stability along individual records need not control average loss. Our next example will remind us that something rare at any particular moment may nevertheless recur throughout a lifetime.

To understand these two failures, we must return to a word we have used repeatedly since Chapter 2: convergence.

## 7.1 A Shrinking Window That Keeps Passing Everyone

Use Lebesgue probability once more on \(\Omega=[0,1)\). Think of this interval as the collection of all possible observation records; selecting a particular \(u\) selects one record.

In the first round, divide the interval in half and open the two windows in turn:

\[
[0,1/2),\qquad[1/2,1).
\]

In the second round, divide it into four pieces and again open the windows from left to right:

\[
[0,1/4),\quad[1/4,1/2),\quad[1/2,3/4),\quad[3/4,1).
\]

Round \(k\) contains \(2^k\) windows, each of width \(2^{-k}\). Only records lying in the current window register an exception at that observation.

This picture can be made precise. Write

\[
N_0=0,\qquad N_k=\sum_{r=1}^k2^r=2^{k+1}-2,
\]

and, for \(k\ge1\) and \(0\le j<2^k\), define

\[
A_{N_{k-1}+j+1}
=\left[\frac j{2^k},\frac{j+1}{2^k}\right),
\qquad Y_n=\mathbf1_{A_n}.
\]

As the observation number \(n\) increases, its round number \(k\) increases too, so

\[
P(Y_n=1)=P(A_n)=2^{-k}\longrightarrow0.
\]

But every fixed \(u\in[0,1)\) lies in exactly one window in every round. Every record therefore contains infinitely many exceptions.

Each round also contains at least one other window that misses it. Hence, for every \(u\),

\[
\limsup_{n\to\infty}Y_n(u)=1,
\qquad
\liminf_{n\to\infty}Y_n(u)=0.
\]

The sequence does not even have a pointwise limit.

Often called the ‘typewriter sequence’, this example sweeps across the interval like a cursor. Its windows shrink, but they never stop seeking new sample points. Fewer people see an exception at each observation, yet nobody is promised that it will eventually stop being their turn.

Now keep windows of the same sizes fixed at the left endpoint. If \(n\) belongs to round \(k\), set

\[
B_n=[0,2^{-k}),\qquad Z_n=\mathbf1_{B_n}.
\]

We still have

\[
P(Z_n=1)=P(Y_n=1).
\]

But for every \(u>0\), all windows lie to its left from some round onward. Thus \(Z_n(u)\to0\); only zero is exceptional, and zero has probability zero.

The two sequences have exactly the same distribution at each observation. One tends to zero almost surely; the other keeps oscillating along every record.

We encountered something similar in Chapter 1. Fairness in each of two games did not determine their joint outcome. Now the exception probability at each time likewise fails to determine the fate of an infinite record.

What is missing, once again, is the connection between different observations.

## 7.2 From the Digits of One Real Number to Infinitely Many Events

Using an entire interval as a random experiment is not merely a way to manufacture counterexamples.

Borel’s 1909 paper *Les probabilités dénombrables et leurs applications arithmétiques* connected countable probability with arithmetic questions. Along this line of inquiry, the infinite digit expansion of a real number becomes a natural entry into infinite random records. [Original publication record](https://link.springer.com/article/10.1007/BF03019651)

We reconstruct the question below in the modern language of Lebesgue probability. Neither the modern notation nor the proof that follows is presented as Borel’s original wording.

Choose \(U\) uniformly in \([0,1)\), and write its binary expansion:

\[
U=0.\xi_1\xi_2\xi_3\cdots\quad\text{（binary）}.
\]

For dyadic rationals with two expansions, consistently choose the one that is eventually zero. These points form a countable set and do not affect the probability conclusions below.

Specifying the first \(m\) digits, for example \(0101\cdots\), places the number in a half-open interval of length \(2^{-m}\). Thus every specified digit string of length \(m\) has probability \(2^{-m}\).

To specify any finite set of digit positions, go as far as the largest position and count the unspecified digits. This gives

\[
P(\xi_{i_1}=a_1,\ldots,\xi_{i_r}=a_r)=2^{-r},
\qquad a_j\in\{0,1\}.
\]

These digits are therefore independent, fair Bernoulli random variables.

Pause over what has happened: we did not begin by assuming an infinite coin-tossing space that had yet to be constructed. The length measure of Chapter 5 has already accommodated an entire sequence of independent tosses inside one random real number.

We can now ask whether the digit 1 eventually accounts for half of an infinite expansion. We can also ask whether certain increasingly rare digit patterns nevertheless keep appearing.

The first question leads toward the strong law of large numbers. The second first requires us to identify precisely the event called ‘keeps appearing’.

For a sequence of measurable events \(A_1,A_2,\ldots\), at least one occurrence from observation \(N\) onward corresponds to

\[
E_N=\bigcup_{n\ge N}A_n.
\]

No matter how far we move the starting point \(N\), there is another occurrence afterward. This corresponds to

\[
\limsup_{n\to\infty}A_n
=\bigcap_{N=1}^{\infty}\bigcup_{n\ge N}A_n.
\]

This is the event that \(A_n\) occur infinitely often, usually abbreviated as \(\{A_n\ \mathrm{i.o.}\}\). Here i.o. stands for infinitely often.

It does not mean ‘occurs at some exceptionally distant time’. It tests all arbitrarily distant starting points at once.

We can assign a probability to this statement about infinite time because Chapter 5 permits countable unions and intersections. Abstract foundations have become the grammar needed to describe an infinite record.

## 7.3 How Can All Distant Exceptions Disappear Together?

If all we know is \(P(A_n)\to0\), the moving windows of the first section have already shown that the matter is not simple.

But what if the sum of the probabilities of all distant exceptions is itself small?

Countable subadditivity immediately gives

\[
P(E_N)\le\sum_{n\ge N}P(A_n).
\]

Consequently, whenever

\[
\sum_{n=1}^{\infty}P(A_n)<\infty,
\]

the tail sum on the right tends to zero. Moreover, \(E_N\) decreases as \(N\) increases, and \(P(E_1)\le1\). Continuity from above therefore gives

\[
P(A_n\ \mathrm{i.o.})
=\lim_{N\to\infty}P(E_N)=0.
\]

This is the first direction of the Borel–Cantelli lemma: **if the exception probabilities are summable, almost every record contains only finitely many exceptions.**

The proof is short, but it changes the level of the question. A probability at one time has been replaced by an upper bound covering all future times. ‘Becoming rarer’ has thereby become ‘eventually stopping’.

No independence was used. The exceptions may depend on one another in any way; a finite total probability budget prevents them from continuing infinitely often on a set of records of positive probability.

We can see the same fact again through the integration language of Chapter 6. Let

\[
N(\omega)=\sum_{n=1}^{\infty}\mathbf1_{A_n}(\omega)
\]

count the total number of exceptions, allowing infinity. By monotone convergence,

\[
\mathbb E[N]=\sum_nP(A_n)<\infty.
\]

A nonnegative random variable with finite expectation cannot equal infinity with positive probability: for every \(M>0\), \(P(N\ge M)\le\mathbb E[N]/M\), and then let \(M\to\infty\).

For a second time, we obtain \(N<\infty\) almost surely.

The same fact has two faces. In terms of events, the probabilities of tail unions vanish; in terms of integration, a finite average count rules out an infinite count. Measure and integration meet here in the study of infinite random records.

Do not reverse the statement, however. \(\mathbb E[N]=\infty\) does not guarantee \(N=\infty\). Chapter 6 already showed that a random variable finite almost surely can have infinite expectation.

When the sum of probabilities diverges, we therefore need another condition.

## 7.4 How Does Independence Bring Rare Events Back Again?

Suppose \(A_n\) are mutually independent and \(\sum_nP(A_n)=\infty\).

The probability of no occurrence between observations \(N\) and \(M\) is

\[
P\left(\bigcap_{n=N}^MA_n^c\right)
=\prod_{n=N}^M(1-P(A_n))
\le\exp\left(-\sum_{n=N}^MP(A_n)\right).
\]

The last step uses only \(1-x\le e^{-x}\). Fix \(N\) and let \(M\to\infty\). The right side tends to zero; by continuity from above, the left side tends to \(P(\bigcap_{n\ge N}A_n^c)\).

Thus, from any given starting point, the probability of never seeing another occurrence is zero. Finally take the union over the countably many starting points to obtain

\[
\boxed{
\sum_nP(A_n)=\infty,\quad A_n\text{ are mutually independent}
\quad\Longrightarrow\quad
P(A_n\ \mathrm{i.o.})=1.
}
\]

This is the second direction. Independence turns ‘each opportunity can be missed’ into ‘infinitely many factors exhaust the chance of missing every opportunity forever’.

Independence is not the weakest possible sufficient condition, but it already makes the mechanism clear. We cannot merely replace a convergent probability sum by a divergent one and reverse the preceding lemma’s conclusion.

For example, on \((0,1)\) take \(A_n=(0,1/n)\). The probability sum is the divergent harmonic series, yet every fixed \(u>0\) eventually leaves all the \(A_n\). The probability of infinitely many occurrences is still zero.

These events keep shrinking into the same region. They do not offer most records any new opportunities.

For an **independent** example whose probabilities tend to zero while occurrences continue infinitely often, we need not invoke an infinite product measure theorem in advance. Use the independent binary digits from the second section and divide them successively into disjoint finite blocks. In round \(k\), use \(2^k\) blocks of length \(k\), each using digit positions never used before. Let one event be that every digit in a block is 1.

The events for different blocks are mutually independent. Each event in round \(k\) has probability \(2^{-k}\), and the sum of all probabilities in that round is

\[
2^k\cdot2^{-k}=1.
\]

Numbering the rounds in order, the individual probabilities tend to zero, but their sum diverges. The second lemma therefore says that these events occur infinitely often in the digit record of almost every random real number.

Becoming rarer does not mean becoming less likely to meet again. The size of one opportunity and the way opportunities accumulate throughout a lifetime are different information.

Cantelli studied the limiting relationship between probability and frequency in his 1917 paper *Sulla probabilità come limite della frequenza*; his 1935 *Considérations sur la convergence dans le Calcul des probabilités* addressed convergence in probability theory directly. These original documents remind us that today’s neatly arranged language of convergence grew from a long effort to distinguish different limiting requirements, rather than from casually giving several names to one idea. [1917 academy catalogue](https://operedigitali.lincei.it/rendicontiFMN/rol/visabs.php?fileId=5161&lang=it&type=mat); [1935 original text](https://www.numdam.org/item/AIHP_1935__5_1_3_0.pdf)

In the historical discussion of his 1935 lectures, Cantelli returned specifically to a distinction easily hidden by the language of frequencies: a frequency being close to the true probability with high probability at one late time is a different promise from all frequencies being close simultaneously from some time onward. This is precisely the difficulty we have faced on our way here from Chapter 2. Infinitely many times cannot be covered merely by a guarantee for one large sample. [Part III of the original text](https://www.numdam.org/item/AIHP_1935__5_1_3_0.pdf)

This chapter uses modern statements and proofs of Borel–Cantelli. It does not assert that the historical papers used exactly our terminology and assumptions.

## 7.5 The Coin of Chapter 2 Finally Receives an Answer for Individual Records

We can now return to empirical frequencies.

For independent fair coins, Chapter 2 proved that the probability of a fixed deviation from \(1/2\) tends to zero. Using the variance alone gives the estimate

\[
P\left(\left|\frac{S_n}{n}-\frac12\right|>\varepsilon\right)
\le\frac1{4n\varepsilon^2}.
\]

Although the right side tends to zero, it is not summable. This bound does not entitle us to announce that exceptions occur only finitely often.

That does not make the stronger conclusion false. It only means that this estimate is not sharp enough.

Set \(\eta_i=\xi_i-1/2\). Then the \(\eta_i\) are independent, take values \(\pm1/2\), and have mean zero. In the fourth-power expansion, every term containing an odd power of some variable has expectation zero. Only terms with one index appearing four times, or two distinct indices appearing twice each, remain:

\[
\begin{aligned}
\mathbb E\left(\sum_{i=1}^n\eta_i\right)^4
&=\sum_i\mathbb E\eta_i^4
+6\sum_{i<j}\mathbb E\eta_i^2\mathbb E\eta_j^2\\
&=\frac n{16}+\frac{6}{16}\binom n2
=\frac{3n^2-2n}{16}.
\end{aligned}
\]

Consequently, Markov’s inequality for nonnegative variables gives

\[
P\left(\left|\frac{S_n}{n}-\frac12\right|>\varepsilon\right)
\le\frac{3}{16\varepsilon^4n^2}.
\]

This time the probability bound is summable. For each fixed \(\varepsilon>0\), the first Borel–Cantelli lemma says that this error is exceeded only finitely often, almost surely.

To obtain convergence, however, we cannot keep just one error threshold fixed. Apply the conclusion separately to \(\varepsilon=1,1/2,1/3,\ldots\), then intersect these countably many probability-one events. On one common probability-one set, for each \(m\) we eventually have

\[
\left|\frac{S_n}{n}-\frac12\right|\le\frac1m.
\]

Only now have we truly shown that

\[
\boxed{\frac{S_n}{n}\longrightarrow\frac12\quad\text{almost surely}.}
\]

We did not require independence between deviation events at different sample sizes; in fact, they are usually highly dependent. Independence of the original coin increments was used only in calculating the fourth moment.

This distinction matters. We must follow the proof to see where independence enters, rather than use the word as a vague incantation.

The same calculation works for independent, identically distributed, bounded Bernoulli variables of mean \(p\). If \(\eta_i=\xi_i-p\), then \(|\eta_i|\le1\), and the expansion gives \(\mathbb E(\sum_i\eta_i)^4\le3n^2\). This already supplies a summable bound of the same kind. Thus, for any fixed \(p\in[0,1]\), Bernoulli frequencies converge almost surely to \(p\).

This is a complete proof of a strong law of large numbers, but it uses bounded increments. The strong law for general integrable i.i.d. variables requires further tools, including truncation; this fourth-moment calculation cannot replace that argument.

### 7.5.1 From One Digit to Every Finite Pattern of a Real Number

We can take the digit-expansion question a step further.

In any integer base \(b\ge2\), intervals of length \(b^{-m}\) show that the digits of a uniform real number are independent and uniform on \(\{0,\ldots,b-1\}\). Fix a digit string \(w\) of length \(r\). Its probability of appearing from a given position is \(b^{-r}\).

Occurrences starting at adjacent positions overlap, so they cannot simply be treated as independent coin tosses. Group the starting positions into \(r\) residue classes modulo \(r\). Within each group the digit blocks do not overlap, so their indicator variables are i.i.d.

The bounded Bernoulli strong law applies to each group. Its occurrence frequency tends to \(b^{-r}\), while the proportions of the groups among starting positions up to \(n\) tend to \(1/r\). Recombining the groups, the frequency over all starting positions therefore also tends to \(b^{-r}\).

For fixed \(b,r,w\), this happens on a probability-one set. There are only countably many choices of integer base, string length and finite digit string. Taking another countable intersection, we obtain: almost every real number has every finite digit string occurring with its expected frequency in every integer base.

This gives a modern route to the probabilistic conclusion of absolute normality. We have proved an almost-everywhere property, not thereby established the property for a particular specified real number, such as \(\sqrt2\).

From the variance of a single coin, to stable frequencies along a record, to the digit structure of almost all real numbers, we have not changed the concept of probability. We have changed how we observe an infinite experiment.

## 7.6 Two Meanings of ‘Eventually’: Fix a Record First, or Fix a Time First?

Only now is it time to give formal names to the two requirements.

In what follows, we first study real-valued measurable random variables \(X_n,X\) on one probability space \((\Omega,\mathcal F,P)\). When we reach convergence in distribution, we will explain explicitly why the variables no longer need to share that space.

**Almost sure convergence** means that there is a measurable null set \(N\) such that \(X_n(\omega)\to X(\omega)\) in the usual real-number sense for every \(\omega\notin N\). We write

\[
X_n\xrightarrow{\mathrm{a.s.}}X.
\]

It fixes a record first and then follows that record indefinitely. Different records may require entirely different waiting times; almost sure convergence supplies no common deadline that works for everyone.

**Convergence in probability**, by contrast, requires that for every \(\varepsilon>0\),

\[
P(|X_n-X|>\varepsilon)\longrightarrow0,
\qquad\text{written }X_n\xrightarrow P X.
\]

At each fixed late time, it measures the probability of the records still failing to be close enough. The membership of that group may keep changing.

The moving windows of the first section satisfy \(Y_n\xrightarrow P0\) but have no almost sure limit; the left-anchored windows \(Z_n\) tend to zero almost surely. Since the two sequences have identical distributions at each time, their difference must lie in the joint structure across time.

### 7.6.1 Why Does Stability Along Records Make the Fraction of Exceptions Vanish?

Suppose \(X_n\to X\) almost surely. Fix \(\varepsilon>0\) and set

\[
E_N(\varepsilon)=\bigcup_{n\ge N}\{|X_n-X|>\varepsilon\}.
\]

Almost every record eventually stops exceeding this error, so \(\bigcap_NE_N(\varepsilon)\) is a null event. Since \(E_N\) decreases and the probability is finite, \(P(E_N)\to0\). Moreover,

\[
P(|X_N-X|>\varepsilon)\le P(E_N(\varepsilon))\to0.
\]

We have obtained

\[
X_n\xrightarrow{\mathrm{a.s.}}X\quad\Longrightarrow\quad X_n\xrightarrow P X.
\]

From Chapter 6’s perspective, we could instead apply dominated convergence to the bounded indicator functions \(\mathbf1_{\{|X_n-X|>\varepsilon\}}\). Both proofs rely on the same fact: the entire probability space has finite total mass.

For a general infinite measure, the implication cannot be carried over unchanged. On the real line, \(\mathbf1_{(n,n+1)}\) tends pointwise to zero, yet the set where it exceeds \(1/2\) always has measure 1. Mass can keep moving toward infinity. The finite total mass of a probability space rules out this form of escape.

### 7.6.2 The Order of Quantifiers Is a Mathematical Structure Too

For fixed \(\varepsilon>0\), convergence in probability says

\[
\lim_{n\to\infty}P(|X_n-X|>\varepsilon)=0.
\]

Almost sure convergence requires, for each such threshold, that combining the exceptions at all distant times still leaves a probability that vanishes:

\[
\lim_{N\to\infty}P\left(\bigcup_{n\ge N}\{|X_n-X|>\varepsilon\}\right)=0.
\]

Checking the second formula for the countably many thresholds \(\varepsilon=1/m\) is equivalent to almost sure convergence. It coordinates future times in a way the first formula does not.

We can turn this coordination into a stronger geometric picture. Given \(\delta>0\), choose \(N_m\) for each \(m\) so that

\[
P(E_{N_m}(1/m))<\delta2^{-m}.
\]

Remove \(H=\bigcup_mE_{N_m}(1/m)\); then \(P(H)<\delta\). On \(H^c\), for every \(m\) and all \(n\ge N_m\), we have \(|X_n-X|\le1/m\). Convergence is therefore uniform on \(H^c\).

This proves the Egorov phenomenon on a finite measure space: almost-everywhere convergence becomes uniform after discarding an arbitrarily small probability set. It does not give one fixed null set outside which convergence is uniform on the entire remaining space. ‘Arbitrarily small’ cannot simply be replaced by ‘zero’.

Almost sure convergence and convergence in probability differ not because one sounds more like everyday language, but because they arrange the quantifiers over time and samples in different orders.

## 7.7 If the Whole Sequence Will Not Settle Down, Can We Choose a Sparser Timeline?

The moving window forces us to admit that convergence in probability cannot simply be upgraded to almost sure convergence.

But not every hope for individual records is lost. Convergence in probability lets us wait long enough to make the probability of a specified error arbitrarily small. Why not organize those waits?

Suppose \(X_n\xrightarrow P X\). First choose \(n_1\) so that \(P(|X_{n_1}-X|>1/2)<1/2\); then choose a larger \(n_2\) so that the probability of an error exceeding \(1/4\) is less than \(1/4\). Continuing recursively, we obtain strictly increasing \(n_j\) satisfying

\[
P(|X_{n_j}-X|>2^{-j})\le2^{-j}.
\]

Now the exception probabilities are summable. Borel–Cantelli says that, along almost every record, only finitely many \(j\) violate \(|X_{n_j}-X|\le2^{-j}\). Hence

\[
\boxed{X_{n_j}\xrightarrow{\mathrm{a.s.}}X.}
\]

The selected timeline does not depend on the sample point. We first choose \(n_j\) using the probabilities of the entire collection of records, and then the same timeline works for almost all records.

This is quite different from selecting a good subsequence separately for each record. That selection could depend on the record and would not give the common probability conclusion obtained here.

Moreover, every subsequence of the original sequence still converges in probability, so each admits a further subsequence converging almost surely. We obtain an exact criterion:

**Real-valued random variables \(X_n\) converge in probability to \(X\) if and only if every subsequence has a further subsequence converging almost surely to \(X\).**

We have proved the forward direction. The reverse direction deserves a complete look as well.

If convergence in probability fails, there are \(\varepsilon,\delta>0\) and a subsequence \(n_k\) such that, for every \(k\),

\[
P(|X_{n_k}-X|>\varepsilon)\ge\delta.
\]

By assumption, this subsequence has a further subsequence tending almost surely to \(X\). But almost sure convergence has already been shown to imply convergence in probability, so the same deviation probabilities must tend to zero, contradicting their lower bound \(\delta\).

Notice the word ‘every’ in the criterion. The existence of just one good subsequence is far from enough. For example, the deterministic sequence \(0,1,0,1,\ldots\) has an identically zero subsequence but does not converge to zero in probability.

This is an idea we will use repeatedly: rather than force the entire sequence to have a pointwise property, require that after every extraction there remains a chance to extract again and recover that property.

### 7.7.1 Why Cannot One Limit Be Two Different Random Variables?

If \(X_n\xrightarrow P X\) and \(X_n\xrightarrow P Y\), the triangle inequality gives, for every \(\varepsilon>0\),

\[
P(|X-Y|>\varepsilon)
\le P(|X-X_n|>\varepsilon/2)
+P(|X_n-Y|>\varepsilon/2).
\]

Letting \(n\to\infty\) makes the left side zero. Taking a countable union over thresholds \(1/m\) then gives \(X=Y\) almost surely.

The limit is therefore unique, but only up to a null set. This agrees with the integration language of Chapter 6: probabilities and integrals cannot distinguish variables that differ only on a measurable null set. Such resolution is not a gap in the theory; it is the scale of information the theory chose from the outset.

## 7.8 If Errors Are Rare, Why Can Average Loss Remain Large?

Return to the spike \(X_n=n\mathbf1_{\{0<U<1/n\}}\) from Chapter 6. It tends to zero almost surely, hence also in probability. But each rare hit produces an increasingly large value, leaving the average loss constantly equal to 1.

Counting only whether an error exceeds a threshold discards how serious it becomes afterward.

We can make that statement precise. For \(D_n=|X_n-X|\), first cap the loss at 1. If \(0<\varepsilon<1\), then

\[
\varepsilon P(D_n>\varepsilon)
\le\mathbb E[\min(1,D_n)]
\le\varepsilon+P(D_n>\varepsilon).
\]

The left inequality integrates over the exception set. The right follows by dividing the space into \(D_n\le\varepsilon\) and its complement.

Convergence in probability is therefore equivalent to

\[
\mathbb E[\min(1,|X_n-X|)]\longrightarrow0.
\]

So convergence in probability can also be described through average loss. But this loss has a ceiling: an error of 10 and an error of a million become indistinguishable after they reach it.

If we remove the cap and genuinely care about the average magnitude of the error, the natural requirement becomes

\[
\mathbb E|X_n-X|\longrightarrow0.
\]

This is called \(L^1\) convergence.

To penalize large errors more heavily, we can consider the \(p\)th power. For \(1\le p<\infty\), assuming finite absolute moments of order \(p\), we write

\[
\|Z\|_p=(\mathbb E|Z|^p)^{1/p},
\qquad
X_n\xrightarrow{L^p}X
\quad\Longleftrightarrow\quad
\mathbb E|X_n-X|^p\longrightarrow0.
\]

Here the space \(L^p\) consists of random variables with finite moments of order \(p\), identifying variables equal almost everywhere. The quantity \(\|\cdot\|_p\) is its usual norm. Further structure, such as completeness, is not a prerequisite for the arguments below; first we ask why this quantity measures random error appropriately.

For \(p=2\), we ask that mean square error vanish. This connects directly with Chapter 2’s variance bounds: for an unbiased estimator, mean square error equals variance. For \(p=1\), we require the average absolute error to vanish, without letting positive and negative errors cancel.

### 7.8.1 Why Does Average Error Control Exception Probabilities?

On \(\{|X_n-X|>\varepsilon\}\), we have \(|X_n-X|^p>\varepsilon^p\), so

\[
P(|X_n-X|>\varepsilon)
\le\frac{\mathbb E|X_n-X|^p}{\varepsilon^p}.
\]

Thus \(L^p\) convergence necessarily implies convergence in probability.

It still does not guarantee convergence along the entire sequence of individual records. The moving window offers a particularly vivid counterexample: for any fixed finite \(p\ge1\),

\[
\mathbb E|Y_n|^p=P(A_n)\to0,
\]

Hence \(Y_n\to0\) in every such \(L^p\) sense, although not a single record tends to zero.

Penalizing the height of an error and arranging the times at which errors occur are still different tasks.

Conversely, the spike disappears along every record without disappearing in \(L^1\). Consequently, \(L^p\) and almost sure convergence cannot simply be arranged on one line from weak to strong.

### 7.8.2 How Are Different Average Losses Related?

On a probability space, if \(1\le q\le p<\infty\), then

\[
\|Z\|_q\le\|Z\|_p.
\]

The estimate needed here can be proved without assuming the full Hölder theory. Let \(a=\mathbb E|Z|^p\). If \(a=0\), the result is immediate. If \(0<a<\infty\), take \(r=q/p\le1\) and use the tangent-line inequality \(t^r\le rt+1-r\) for nonnegative numbers to obtain

\[
\mathbb E\left(\frac{|Z|^p}{a}\right)^r
\le r\mathbb E\frac{|Z|^p}{a}+1-r=1.
\]

Rearrangement gives the desired conclusion. Thus \(L^p\) convergence implies \(L^q\) convergence.

The reverse direction generally fails. For \(q<p\), take

\[
H_n=n^{1/p}\mathbf1_{\{0<U<1/n\}},
\]

Then

\[
\mathbb E|H_n|^q=n^{q/p-1}\to0,
\qquad \mathbb E|H_n|^p=1.
\]

A large error becomes cheap under a lower power while leaving a non-negligible contribution under a higher power.

Defining \(L^\infty\) error through the essential supremum imposes a stronger requirement. Even though \(\mathbf1_{\{0<U<1/n\}}\) almost surely and in every finite \(L^p\), its essential supremum stays equal to 1. For \(0<p<1\) one can also study \(\mathbb E|X_n-X|^p\to0\), but the corresponding \((\mathbb E|Z|^p)^{1/p}\) is no longer a norm. Our main discussion uses \(p\ge1\).

### 7.8.3 What Does Dominated Convergence Now Explain?

If \(X_n\to X\) almost surely, with \(|X_n|\le G\) and \(\mathbb E G^p<\infty\), then \(|X|\le G\) holds on the same probability-one set. Consequently,

\[
|X_n-X|^p\le2^{p-1}(|X_n|^p+|X|^p)\le2^pG^p.
\]

The dominated convergence theorem of Chapter 6 immediately yields \(L^p\) convergence.

This theorem does not declare two convergence notions equivalent. It adds a common constraint across all times: no increasingly tall spike can evade the same integrable dominating function.

If we do not want to demand a common upper bound, can we find a condition that is exactly sufficient? This question will soon lead us to uniform integrability.

Before pursuing average loss, however, we should identify an earlier kind of limit. Exactly what form of approximation did Chapter 3’s bell curve describe?

## 7.9 Which Random Variable Is the Bell Curve Approaching?

[Chapter 3](#chapter-3) wrote

\[
\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow d N(0,1).
\]

The right side first specifies a distribution, not some record already present among the original coin tosses.

We can define \(S_n\) for every sample size on the same space. But the central limit theorem does not thereby specify a particular \(Z\) and guarantee that the standardized error along every record gets closer to that \(Z\).

An example requiring no asymptotic calculation brings this difference into view.

On a space with just two equally likely outcomes, take \(P(X=0)=P(X=1)=1/2\) and set

\[
X_{2n}=X,\qquad X_{2n-1}=1-X.
\]

Each \(X_n\) has the same distribution as \(X\). Their histograms have been identical from the very first day.

Yet along every record the values keep alternating between 0 and 1. In particular,

\[
P(|X_{2n-1}-X|>1/2)=1.
\]

There is therefore no convergence in probability to this \(X\).

If we retain only the individual probability distributions, all this alternation becomes invisible. **Convergence in distribution** studies limits precisely at that level.

For real-valued random variables, let

\[
F_n(x)=P(X_n\le x),\qquad F(x)=P(X\le x).
\]

We define \(X_n\xrightarrow d X\) to mean that \(F_n(x)\to F(x)\) at every continuity point \(x\) of \(F\). Another common notation is \(X_n\Rightarrow X\).

The \(X_n\) may perfectly well live on different spaces \((\Omega_n,\mathcal F_n,P_n)\): replace \(F_n\) by \(P_n(X_n\le x)\). The limiting variable may live on yet another space. We compare only distributions on the real line.

Why not require convergence at every point? Consider deterministic variables \(X_n=1/n\) and \(X=0\). Their values approach zero at every sample point, but

\[
F_n(0)=0,\qquad F(0)=1.
\]

The problem is not the approximation of values. An atom suddenly appears at the boundary of the interval \(( -\infty,0]\). Such a boundary choice should not destroy a limit that ought to hold.

The continuity-point restriction therefore distinguishes closeness of distributions from the assignment of mass at a sharp boundary.

### 7.9.1 Why Does Convergence in Probability Bring Distributions Closer?

If \(X_n\xrightarrow P X\), then on the event \(\{|X_n-X|\le\varepsilon\}\),

\[
X\le x-\varepsilon\Longrightarrow X_n\le x,
\qquad
X_n\le x\Longrightarrow X\le x+\varepsilon.
\]

and hence

\[
F(x-\varepsilon)-P(|X_n-X|>\varepsilon)
\le F_n(x)
\le F(x+\varepsilon)+P(|X_n-X|>\varepsilon).
\]

First let \(n\to\infty\), then \(\varepsilon\downarrow0\). If \(x\) is a continuity point of \(F\), both endpoints tend to \(F(x)\), giving \(F_n(x)\to F(x)\).

This proves that convergence in probability implies convergence in distribution. The alternating Bernoulli example has already disproved the reverse direction.

An important exception occurs when the limit is a constant \(c\). If \(X_n\xrightarrow d c\), then for every \(\varepsilon>0\) the points \(c-\varepsilon\) and \(c+\varepsilon\) are continuity points of the limiting distribution function, so

\[
P(|X_n-c|>\varepsilon)
\le F_n(c-\varepsilon)+1-F_n(c+\varepsilon)\to0.
\]

Thus **convergence in distribution to a constant is equivalent to convergence in probability to that constant.**

This explains a familiar experience. The weak law of large numbers has a constant limit, so concentration at the distributional level suffices. The central limit theorem has a genuinely random limit, so distributional convergence cannot simply be promoted to closeness of values in the original space.

## 7.10 Beyond Interval Endpoints: Stabilizing Every Continuous Observation

Distribution functions provide convenient coordinates on the real line, but do not look like a definition suited to random functions or random trees. What should play the role of ‘\(X\le x\)’ for a path?

First change our viewpoint on the real line itself.

Suppose an instrument reports a bounded continuous function \(f(X)\) instead of the truth or falsity of a sharp event. Compare its average readings under two distributions. A natural requirement is

\[
\mathbb E[f(X_n)]\longrightarrow\mathbb E[f(X)]
\quad\text{for every bounded continuous }f:\mathbb R\to\mathbb R.
\]

This is exactly equivalent to the distribution-function definition. We prove it so that we can be sure the new viewpoint has not lost the original limit.

### 7.10.1 How Can a Continuous Instrument Approximate an Interval?

First suppose expectations of all bounded continuous readings converge. Given \(x\) and \(\delta>0\), construct two continuous ramps. One stays at 1 before \(x-\delta\) and decreases to 0 at \(x\); the other stays at 1 before \(x\) and decreases to 0 at \(x+\delta\). Elsewhere they remain at 0 or 1.

Call them \(\ell_\delta,u_\delta\). Then

\[
\ell_\delta(t)\le\mathbf1_{\{t\le x\}}\le u_\delta(t).
\]

Take expectations under \(X_n\) and pass to limits to obtain

\[
F(x-\delta)\le\liminf_nF_n(x)
\le\limsup_nF_n(x)\le F(x+\delta).
\]

If \(F\) is continuous at \(x\), letting \(\delta\downarrow0\) gives the desired distribution-function convergence.

The ramps approach the boundary gradually rather than leaping across it. When the limiting distribution gives that boundary no mass, the gradual approach leaves no error.

### 7.10.2 How Do Interval Probabilities Control Every Continuous Reading?

Conversely, we know only interval probabilities but want to recover arbitrary continuous readings across the entire real line. The difficulty has two layers: the reading changes with position, and the line has no end. First keep almost all probability in a bounded interval, then approximate readings there using finitely many graduations. Only then can the distribution function’s information take charge of each graduation.

Suppose \(F_n\) tends to \(F\) at every continuity point of \(F\), and take bounded continuous \(f\) with \(|f|\le M\). If \(M=0\), there is nothing to prove.

First choose continuity points \(a<b\) sufficiently far apart that

\[
F(a)+1-F(b)<\eta.
\]

This is possible because a distribution function tends to 0 and 1 at the two ends of the line and has at most countably many discontinuities. The latter fact has a simple explanation: there are at most \(m\) jumps of size at least \(1/m\), and all positive jumps form a countable union of these finite sets.

Convergence at the endpoints ensures that, for large enough \(n\), \(P(X_n\notin(a,b])<2\eta\); the corresponding tail probability for the limit is less than \(\eta\). The total error in the two tail readings is thus at most \(3M\eta\).

Boundedness has controlled the distant readings. What remains is variation nearby. On the compact interval \([a,b]\), \(f\) is uniformly continuous: one sufficiently fine system of graduations works at every position. Divide the interval into finitely many sufficiently short pieces \((t_{j-1},t_j]\), with all endpoints continuity points of \(F\), so that the oscillation of \(f\) on each piece is less than \(\eta\). Choose one representative \(c_j\) per piece.

The integral over the interior can then be approximated by a finite sum:

\[
\sum_j f(c_j)\,[F_n(t_j)-F_n(t_{j-1})].
\]

Each coefficient converges to the corresponding limiting interval probability, and each of the two approximation errors is at most \(\eta\). Hence

\[
\limsup_n|\mathbb Ef(X_n)-\mathbb Ef(X)|
\le 2\eta+3M\eta.
\]

Let \(\eta\downarrow0\) to finish the proof.

Looking back, the two approximations had different responsibilities: control probability far away, then oscillation nearby. Finite partitions on the real line connect the two tasks and leave a clue for our later passage to general spaces.

‘Bounded’ and ‘continuous’ each do a particular job. Boundedness prevents rare large values from dominating the reading; continuity prevents infinitesimal movements from crossing a sharp boundary carrying mass.

Remove the first, and Chapter 6’s spike makes the expectation of \(f(x)=x\) misbehave. Remove the second: for \(X_n=1/n\to0\), the readings of \(f=\mathbf1_{\{0\}}\) remain zero, but the limiting reading is 1.

These restrictions are not arbitrary concessions to the proof. They correspond exactly to two different ways a limit can fail.

The four limits have now separated: individual records, exception probabilities, average losses and continuous readings of distributions. Yet the spike’s original question remains. Is there a more flexible condition than one common integrable bound that makes average loss obey a limit?

## 7.11 What the Spike Carries Away Is Average Loss, Not Probability

Look once more at \(X_n=n\mathbf1_{\{0<U<1/n\}}\). Its probability of being nonzero is only \(1/n\), but whenever \(n>K\),

\[
\mathbb E\bigl[|X_n|\mathbf1_{\{|X_n|>K\}}\bigr]=1.
\]

However high we place the ‘large value’ threshold \(K\), a taller spike puts the entire average loss beyond it.

The issue is therefore not merely \(\sup_n\mathbb E|X_n|<\infty\). We also need this finite average loss not to reconcentrate in regions of larger and larger values.

A family \(\mathcal X\) of integrable random variables is called **uniformly integrable** if

\[
\boxed{
\lim_{K\to\infty}\sup_{Y\in\mathcal X}
\mathbb E\bigl[|Y|\mathbf1_{\{|Y|>K\}}\bigr]=0.
}
\]

Uniform integrability is commonly abbreviated UI. When \(\mathcal X=\{X_n:n\ge1\}\), we say the sequence is uniformly integrable.

Every individual integrable variable has tail expectations tending to zero. Dominated convergence gives this immediately: \(|Y|\mathbf1_{\{|Y|>K\}}\to0\), dominated by the integrable \(|Y|\).

The new requirement is that one \(K\) work simultaneously for the entire family. Fixing one \(n\) before increasing the threshold differs from putting all \(n\) together before raising it. Once again, the order of quantifiers matters.

### 7.11.1 How Can Numerical Tails Reveal Small-Probability Sets?

For a uniformly integrable family, first choose \(K\ge1\) so that all tail expectations are less than 1. Then

\[
\sup_{Y\in\mathcal X}\mathbb E|Y|\le K+1<\infty.
\]

For any event \(A\),

\[
\mathbb E[|Y|\mathbf1_A]
\le K P(A)
+\mathbb E[|Y|\mathbf1_{\{|Y|>K\}}].
\]

Given \(\varepsilon>0\), first choose \(K\) to make the second term less than \(\varepsilon/2\) for every \(Y\), then require \(P(A)<\varepsilon/(2K)\). This gives

\[
\sup_{Y\in\mathcal X}\mathbb E[|Y|\mathbf1_A]<\varepsilon.
\]

The conclusion is closely tied to our original question: **on a set of sufficiently small probability, the average loss contributed by the entire family is uniformly small.**

Conversely, suppose this small-set property holds and \(C=\sup_{Y\in\mathcal X}\mathbb E|Y|<\infty\). If \(C=0\), the result is immediate. Otherwise, given \(\varepsilon>0\), choose \(\delta>0\) from the small-set property. Choose \(K>C/\delta\) next. Markov’s inequality gives

\[
P(|Y|>K)\le C/K<\delta
\]

for every \(Y\). Substituting \(A=\{|Y|>K\}\) into the small-set property yields uniform integrability.

Thus UI is equivalent to two requirements together: uniformly bounded absolute first moments and uniform absolute continuity of the integrals on small-probability sets.

The first-moment bound cannot be omitted. On a one-point probability space, the variables \(Y_n=n\) satisfy the small-set condition for all sufficiently small-probability events, since the only such event is empty. Yet they are plainly not uniformly integrable.

This extreme example shows that hypotheses are not decoration. On a general probability space, we must control both the total budget and its concentration in small regions.

### 7.11.2 Why Does a Higher Moment Prevent Bad Tails?

If some \(p>1\) satisfies \(\sup_n\mathbb E|X_n|^p=C<\infty\), then on \(|X_n|>K\),

\[
|X_n|\le K^{1-p}|X_n|^p.
\]

and so

\[
\sup_n\mathbb E[|X_n|\mathbf1_{\{|X_n|>K\}}]
\le C K^{1-p}\to0.
\]

A uniform higher-moment bound is therefore a convenient sufficient condition for UI. It is stronger than UI itself and must not be mistaken for its definition.

For example, use the uniform probability of density \(e\) on \((0,e^{-1})\), and set

\[
Y(u)=\frac1{u[\log(1/u)]^2}.
\]

The substitution \(t=\log(1/u)\) gives

\[
\mathbb E Y=e\int_1^\infty t^{-2}\,dt=e<\infty,
\]

but for every \(p>1\),

\[
\mathbb E Y^p=e\int_1^\infty e^{(p-1)t}t^{-2p}\,dt=\infty.
\]

The last integral diverges because exponential growth eventually exceeds every polynomial decay. The constant sequence \(X_n=Y\) is uniformly integrable but has no higher-moment bound of this kind.

A common integrable dominating function is also sufficient for UI: if \(|X_n|\le G\) and \(G\) is integrable, the tail contribution is bounded by \(\mathbb E[G\mathbf1_{\{G>K\}}]\). But UI does not require every variable to fit under one integrable ceiling. It directly constrains the tail integrals we actually care about.

## 7.12 What Happens When Closeness in Probability Loses No Average Loss?

The preceding section turned restrictions on numerical tails into uniform control of integrals on small-probability sets. Now take precisely the sets \(\{|X_n-X|>\varepsilon\}\). Convergence in probability makes them small; UI prevents spikes from hiding loss inside them. Two previously distinct convergence requirements can finally cooperate.

The exact result is: **if real-valued measurable \(X_n\) converge in probability to real-valued measurable \(X\) and every \(X_n\) is integrable, then \(X_n\to X\) in \(L^1\) if and only if \(\{X_n\}\) is uniformly integrable.** In the UI direction, integrability of \(X\) need not be assumed separately; it follows.

This is the Vitali convergence criterion on a probability space. Rather than treat it merely as a named generalization of dominated convergence, we want to see why each part is indispensable.

### 7.12.1 First Make Sure the Limit Has an Average

UI already gives \(\sup_n\mathbb E|X_n|=C<\infty\). By the subsequence principle, choose \(X_{n_j}\to X\) almost surely. Apply Fatou’s lemma to the nonnegative \(|X_{n_j}|\) to obtain

\[
\mathbb E|X|\le\liminf_j\mathbb E|X_{n_j}|\le C.
\]

The limit is therefore integrable.

We extracted just one almost surely convergent subsequence; we did not quietly assume almost sure convergence of the whole sequence. When the proof needs individual records, the subsequence principle supplies exactly the bridge required.

### 7.12.2 Split the Total Error into ‘Small’ and ‘Rare’

Given \(\varepsilon>0\), the small-set criterion for UI supplies \(\delta_1>0\) such that whenever \(P(A)<\delta_1\), every \(n\) satisfies

\[
\mathbb E[|X_n|\mathbf1_A]<\varepsilon.
\]

Likewise, the integral of the single integrable variable \(X\) is absolutely continuous on small-probability sets. First make the tail integral of \(|X|\) above a large threshold less than \(\varepsilon/2\), then bound the rest by that threshold times \(P(A)\). We can therefore choose \(\delta_2>0\) to make the corresponding integral less than \(\varepsilon\).

Set

\[
A_n=\{|X_n-X|>\varepsilon\}.
\]

Convergence in probability ensures that for sufficiently large \(n\), \(P(A_n)<\min(\delta_1,\delta_2)\). On \(A_n^c\) the error is at most \(\varepsilon\); on \(A_n\) use \(|X_n-X|\le|X_n|+|X|\). Therefore

\[
\begin{aligned}
\mathbb E|X_n-X|
&\le\varepsilon+
\mathbb E[|X_n|\mathbf1_{A_n}]
+\mathbb E[|X|\mathbf1_{A_n}]\\
&<3\varepsilon.
\end{aligned}
\]

Since \(\varepsilon\) is arbitrarily small, \(L^1\) convergence follows.

The two integrals over the exceptional region are exactly what Chapter 6’s spike disrupted. The small-set estimates have finally brought both under control.

### 7.12.3 Why Must \(L^1\) Convergence Also Leave UI Behind?

Conversely, suppose \(X_n\to X\) in \(L^1\). The inequality

\[
\mathbb E|X_n|\le\mathbb E|X_n-X|+\mathbb E|X|
\]

shows that the first moments are uniformly bounded.

Given \(\varepsilon>0\), first choose \(N\) so that \(\mathbb E|X_n-X|<\varepsilon/2\) for every \(n\ge N\). If an event \(A\) has sufficiently small probability, then \(\mathbb E[|X|\mathbf1_A]<\varepsilon/2\). Thus every \(n\ge N\) satisfies

\[
\mathbb E[|X_n|\mathbf1_A]
\le\mathbb E|X_n-X|+\mathbb E[|X|\mathbf1_A]
<\varepsilon.
\]

Only the finitely many integrable variables \(X_1,\ldots,X_{N-1}\) remain. Choose an appropriate small-set threshold for each, then take the minimum. One condition will then work for all \(n\).

The small-set criterion gives uniform integrability of \(\{X_n\}\). Since \(L^1\) convergence already implies convergence in probability, both directions of the equivalence are complete.

### 7.12.4 Dominated Convergence No Longer Requires Individual Records First

Suppose we know only \(X_n\xrightarrow P X\) but still have \(|X_n|\le G\) with integrable \(G\). UI is automatic, and the criterion gives \(L^1\) convergence.

Thus, when exchanging expectations with limits on a probability space, dominated convergence’s usual almost sure hypothesis can be weakened to convergence in probability. Pointwise reasoning has not been ignored: the subsequence principle and Fatou’s lemma have already done that work for us.

More generally, if \(|X_n|\le G\) and \(\mathbb EG^p<\infty\), we obtain \(L^p\) convergence. Indeed, every subsequence admits a further subsequence tending almost surely to \(X\). Along it, \(|X|\le G\) almost surely, and the domination estimate of Section 7.8 gives \(\mathbb E|X_{n_j}-X|^p\to0\). If the whole sequence of these nonnegative expectations did not tend to zero, we could first extract one with a positive lower bound, contradicting the extraction property just established.

We have learned a powerful proof method: solve the problem on a subsequence where individual records are available, then check that no failing subsequence can escape the conclusion.

## 7.13 Why Do Equal Expectations Not Mean the Loss Has Disappeared?

The Vitali criterion controls absolute error, but calculations often give signed expectations first. If we already know \(\mathbb EX_n\to\mathbb EX\), can this more accessible information replace UI?

For gains with both signs, the answer is no. Set

\[
Z_n=n\mathbf1_{\{0<U<1/(2n)\}}
-n\mathbf1_{\{1/(2n)\le U<1/n\}}.
\]

Then \(Z_n\to0\) almost surely, and

\[
\mathbb E Z_n=0\longrightarrow0,
\qquad
\mathbb E|Z_n|=1.
\]

The positive and negative spikes cancel exactly in expectation without making the error disappear. This is why \(L^1\) uses absolute values rather than merely comparing two signed averages.

Nonnegative variables have a sharper and more elegant exception. If \(X_n\ge0\) and \(X\ge0\) are integrable, \(X_n\to X\) almost surely, and \(\mathbb EX_n\to\mathbb EX\), then

\[
|X_n-X|=X_n+X-2\min(X_n,X).
\]

The minimum on the right tends to \(X\) and is dominated by the integrable \(X\). Dominated convergence gives

\[
\mathbb E|X_n-X|
=\mathbb EX_n+\mathbb EX-2\mathbb E\min(X_n,X)
\longrightarrow0.
\]

This is often called a Scheffé-type argument. Nonnegativity prevents cancellation, so ‘no loss of total mass’ together with pointwise closeness forces absolute error to vanish. If only convergence in probability is given, the subsequence principle again lifts the argument to the whole sequence.

### 7.13.1 If Distributions Are Already Close, Can UI Recover Average Readings?

We can weaken the assumption further. Suppose only \(X_n\xrightarrow d X\) and uniformly vanishing absolute-value tail expectations for \(\{X_n\}\). The variables need not live on the same probability space.

Section 7.10 admitted only bounded continuous instruments through the limit; now we want the unbounded reading \(f(x)=x\) back. Our two truncation ideas meet here: distributional convergence handles the reading at a fixed threshold, while UI finally lets us remove the threshold safely.

There is no difference on a common space to estimate here, so Vitali cannot be invoked directly. First establish integrability of the limit from its distribution: UI gives \(C=\sup_n\mathbb E|X_n|<\infty\). The function \(x\mapsto\min(|x|,R)\) is bounded and continuous, so

\[
\mathbb E\min(|X|,R)
=\lim_n\mathbb E\min(|X_n|,R)\le C.
\]

Let \(R\to\infty\). Monotone convergence shows that \(X\) is integrable.

Take the continuous truncation \(T_K(x)=\max(-K,\min(x,K))\). Distributional convergence gives \(\mathbb ET_K(X_n)\to\mathbb ET_K(X)\), while

\[
|\mathbb EX_n-\mathbb ET_K(X_n)|
\le\mathbb E[|X_n|\mathbf1_{\{|X_n|>K\}}].
\]

UI makes the right side tend uniformly to zero, and integrability makes the limiting variable’s corresponding tail vanish too. First let \(n\to\infty\) and then \(K\to\infty\) to obtain \(\mathbb EX_n\to\mathbb EX\).

This is still not \(L^1\) convergence of the original variables. The alternating Bernoulli variables in Section 7.9 have the same distribution and expectation and are uniformly bounded, hence uniformly integrable. Yet they do not even converge in probability to the specified \(X\).

UI restores **unbounded average readings of distributions**. It does not invent joint relationships that were never there.

## 7.14 Four Limits Preserve Four Different Kinds of Information

After these examples, bringing the relations together no longer produces a diagram of arrows to memorize blindly.

For real-valued variables on a common probability space and \(1\le q\le p<\infty\), we have proved

\[
\begin{gathered}
X_n\xrightarrow{\mathrm{a.s.}}X\ \Longrightarrow\ X_n\xrightarrow P X\ \Longrightarrow\ X_n\xrightarrow d X,\\
X_n\xrightarrow{L^p}X\ \Longrightarrow\ X_n\xrightarrow{L^q}X\ \Longrightarrow\ X_n\xrightarrow P X.
\end{gathered}
\]

To return from convergence in probability to \(L^1\), UI is exactly what is needed:

\[
X_n\xrightarrow{L^1}X
\quad\Longleftrightarrow\quad
X_n\xrightarrow P X\ \text{and }\{X_n\}\text{ is uniformly integrable},
\]

Here the \(X_n\) are integrable, and the limit \(X\) is real-valued and measurable; the right-hand conditions imply its integrability.

|Attempted reverse implication|The random phenomenon that blocks it|
|---|---|
|In probability \(\Rightarrow\) almost surely|A moving window hits few people at each time but repeatedly hits everyone|
|Every finite \(L^p\) \(\Rightarrow\) almost surely|The same bounded moving window loses all finite-order average error, yet recurrence over time remains|
|Almost surely or in probability \(\Rightarrow L^1\)|A shrinking spike hides average loss in ever rarer large values|
|\(L^q\Rightarrow L^p\), \(q<p\)|A spike of height \(n^{1/p}\) and width \(1/n\) retains mass under the higher power|
|In distribution \(\Rightarrow\) in probability|Alternating variables with identical time marginals preserve histograms while changing the pairing on the original space|

The table does not tell us to strengthen every limit as much as possible. It reminds us that different questions require different information.

Almost sure convergence naturally describes whether an actual observation record eventually stabilizes. Convergence in probability often already answers a high-probability accuracy question for a large-sample estimator. Controlling average loss or exchanging expectations requires checking the integral level. Identifying the shape of standardized fluctuations calls for convergence in distribution, which allows different microscopic models to approach the same limiting law.

Rolling all these requirements into a single ‘convergence’ would obscure the very distinctions probability theory studies.

## 7.15 If the Distributions Match, Can We Arrange a New Meeting?

In the alternating Bernoulli example, why can a sequence with identical distributions fail to display closeness of values? Because we kept the original pairing.

If we may realize those distributions again on another space, take one Bernoulli variable \(Z\) and set every new variable \(Y_n\) equal to \(Z\). Each \(Y_n\) still has the distribution of the original \(X_n\), and \(Y_n\to Z\) now holds everywhere.

We have not improved convergence of the old variables. We have preserved each individual distribution but changed the way they live together.

This is the basic idea of **coupling**: choose a joint realization of given marginal distributions.

On the real line, one arrangement is particularly natural. For a distribution function \(F\), define its generalized quantile

\[
Q(u)=\inf\{x\in\mathbb R:F(x)\ge u\},\qquad 0<u<1.
\]

Using the same uniform variable \(U\), \(Q(U)\) has distribution function \(F\). Monotonicity and right continuity give \(Q(u)\le x\) if and only if \(u\le F(x)\). Taking uniform probabilities yields \(P(Q(U)\le x)=F(x)\). The condition \(0<u<1\) ensures finite generalized quantiles; the endpoints do not affect uniform probability.

For a sequence of distribution functions \(F_n\), we can therefore place \(Q_n(U)\) and \(Q(U)\) on the same uniform scale. This preserves the original one-time distributions, not independence or other joint relationships among the original variables.

When real-valued distributions converge weakly, the quantile arrangement can produce an almost surely convergent realization. Its key is convergence of generalized quantiles at almost every uniform level. The broader Skorokhod representation theory addresses similar questions in suitable complete separable metric spaces. Proving these results requires careful control of quantile continuity points or of the space’s topology; we will develop that line of inquiry when we reach weak convergence theory.

For now, remember exactly what these conclusions allow us to change: pointwise convergence in a new space does not mean pointwise convergence along the original observation records.

The joint probabilities of Chapter 1, the finite-dimensional distributions of Chapter 4 and this chapter’s convergence in distribution meet once more. Marginal laws have never uniquely determined a joint world for us.

### 7.15.1 If Outcomes Are No Longer Real Numbers, What Remains of Continuous Readings?

For random elements of a metric space \(S\), once its Borel measurable structure and the distributions have been specified, the same question defines a direction for weak convergence: do the integrals converge for every bounded continuous \(f:S\to\mathbb R\)?

This question no longer depends on the ordering of real numbers, so it can also address continuous paths, random trees and random measures.

But which event probabilities will converge? The example \(1/n\to0\) already shows that we cannot expect every measurable set to work. Boundary mass remains an obstacle. The Portmanteau theorem in general weak convergence theory connects bounded continuous observations with one-sided estimates for open and closed sets and convergence of probabilities for sets whose boundaries have zero mass.

This is not a sudden new collection of equivalent propositions to memorize. We have just seen why they must arise: continuous instruments approximate sharp events, and boundaries determine whether the approximation can be made without loss.

There is also the question of escaping probability mass. For a real-valued limiting distribution, a sufficiently large compact interval retains almost all probability. Section 7.10 used exactly this fact to lift bounded-interval approximations to the whole space. In a general metric space, we must distinguish two requirements.

For a Borel probability measure \(\mu\) on \(S\), if

\[
\forall\varepsilon>0\ \exists K\subseteq S\text{ compact},
\qquad \mu(K)\ge1-\varepsilon,
\]

we call \(\mu\) **tight**. The compact set may depend on \(\varepsilon\) and on this particular measure.

For a family \(\mathcal P\) of Borel probability measures, if

\[
\forall\varepsilon>0\ \exists K\subseteq S\text{ compact},
\qquad \inf_{\mu\in\mathcal P}\mu(K)\ge1-\varepsilon,
\]

we call the family **uniformly tight**. Some texts simply say that such a family is ‘tight’. The important point is not the abbreviation: one compact set must retain almost all probability simultaneously for the entire family.

Every probability measure on the real line is tight, since \([-R,R]\uparrow\mathbb R\). But a family need not be uniformly tight. The measures \(\delta_n\) each put all mass at the integer \(n\). Each measure is tight, yet a fixed compact set contains only bounded integer positions and cannot control all \(n\) simultaneously. When looking for a weak limit of a sequence of distributions, this uniform constraint is what we need to examine, rather than checking tightness one measure at a time.

Do not confuse tightness with uniform integrability. For the spike \(X_n=n\mathbf1_{\{0<U<1/n\}}\), if \(R\ge1\), then

\[
\sup_nP(|X_n|>R)
\le\frac1{\lfloor R\rfloor+1}\longrightarrow0.
\]

Its family of distributions is therefore uniformly tight on the real line. But for any \(K\), taking \(n>K\) still leaves tail expectation 1, so UI fails.

Little **probability** escaping to large values does not imply a small **value-weighted contribution** there.

Chapter 4’s path question adds another difficulty. Preventing displacement from escaping at one time does not prevent an entire function from developing increasingly sharp oscillations. Compact sets will no longer be just large intervals: we must understand which collections of functions can approach one another and which path fluctuations obstruct tightness.

Borel–Cantelli, integration, distributions and function spaces thus begin to share a road. Each controls different information, but they work together when we need a fuller random limit.

## Closing Chapter 7: What Do We Want a Random World to Preserve?

Imagine walking forward once more along an infinite observation record.

A small window may sweep past us again and again even as the probability of being hit at each observation decreases. Another spike may finally leave every fixed record while retaining the same average loss in the population.

These original difficulties do not contradict one another. They tell us that ‘eventually’ can have different meanings.

Borel–Cantelli lets us consider all distant times together. It turns a summable probability budget into finitely many exceptions and lets infinitely many independent opportunities exhaust the chance of escaping forever. The law of large numbers can thereby become the long-term fate of almost every record, rather than merely a high-probability guarantee at one late time.

Yet the fate of a record cannot determine average loss. The spikes revealed by Lebesgue integration need the constraint of uniform integrability. It does not place every variable beneath the same ceiling; it requires that no region of diminishing probability conceal an average contribution that refuses to disappear.

Looking again at Chapter 3’s Gaussian curve, we discover that some limits do not track one record at all. They preserve the shape of a distribution: the average reading of every bounded continuous observation. To rearrange such distributions into pointwise-approaching variables, we must decide carefully how to realize them together.

The four convergences are not definitions competing for rank. They answer different questions: what happens to one record, how large the exceptions are, whether average loss vanishes and what shape the population distribution takes.

We need not always choose the strongest requirement. We need to know which random information our question must preserve and what further conditions must be paid for to obtain more.

The particle of [Chapter 4](#chapter-4) still awaits a genuine continuous random path. We can now say precisely why a fixed-time Gaussian limit answers only one convergence question. An entire path still requires the construction of a probability measure, measurability in path space and suitable weak convergence theory.

Next we face a question opposite to the one that began this chapter. We started with a whole probability space already given and studied infinite sequences inside it. If instead we begin only with rules for each finite experiment, can we always make them coexist in one infinite experiment?

A real number’s digit expansion already showed how a special case can succeed. What consistency is needed for arbitrary finite-dimensional laws to coexist? Where, in passing from finite to infinite, does countable additivity become decisive?

We have learned to distinguish the different promises made by limits. Now we must ask how the random objects involved in those promises are placed in one mathematical world.

## History and Further Reading

Émile Borel, *Les probabilités dénombrables et leurs applications arithmétiques*, *Rendiconti del Circolo Matematico di Palermo* 27 (1909), 247–271. [Original publication record](https://link.springer.com/article/10.1007/BF03019651). The publication page’s separate 2009 date concerns the online record, not the paper’s original publication.

Francesco Paolo Cantelli, *Sulla probabilità come limite della frequenza* (1917). [Original catalogue of the Accademia dei Lincei](https://operedigitali.lincei.it/rendicontiFMN/rol/visabs.php?fileId=5161&lang=it&type=mat). F. P. Cantelli, *Considérations sur la convergence dans le Calcul des probabilités*, *Annales de l’Institut Henri Poincaré* 5 (1935), 3–50. [Original facsimile and full text](https://www.numdam.org/item/AIHP_1935__5_1_3_0.pdf).

This chapter uses modern mathematical language for its notation, proof sequence, comparison of moving windows with spikes and organization from subsequences toward uniform integrability. These should not be read as quotations or reproductions of the original proofs in the historical documents above.

For broader theory, see the parts on integration, sequence limits and convergence of distributions in Olav Kallenberg, *Foundations of Modern Probability*, third edition (2021). [Publisher’s bibliographic record](https://link.springer.com/book/10.1007/978-3-030-61871-1). This chapter’s narrative grows from the problems of the first six chapters.


---

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

This is the **Carathéodory probability measure extension theorem** used in this chapter: a probability premeasure on an algebra has a unique probability extension to the \(\sigma\)-algebra it generates. Outer measure also gives a larger, complete measurable structure; later we will explain why retaining the generated \(\sigma\)-algebra first is usually clearer.

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

On the real line and in finite-dimensional Euclidean space, this is a manifestation of measure regularity. We will prove what we need in a slightly broader and more useful setting.

A metric space is called a **Polish space** if it is separable and its topology can be induced by a complete metric. We use such a complete metric here. Important examples include the real line, finite-dimensional Euclidean spaces, countable discrete spaces, and \(C([0,1])\) with the uniform metric. The last space is complete because uniform limits of continuous functions remain continuous; separability follows by approximation with piecewise linear functions having rational breakpoints and rational vertex values.

On a Polish space \(S\), every Borel probability \(\mu\) is tight. We can see the mechanism directly.

Fix \(\varepsilon>0\). For each \(k\), separability supplies a countable cover of \(S\) by open balls of radius \(2^{-k}\). By continuity from below, select finitely many whose union has probability greater than \(1-\varepsilon2^{-k}\). Replace these balls with closed balls and call the resulting closed set \(F_k\). Set

\[
K=\bigcap_{k\ge1}F_k.
\]

Countable subadditivity gives \(\mu(K)\ge1-\varepsilon\). The set \(K\) is closed and therefore complete; at every scale it can also be covered by finitely many sufficiently small balls, so it is totally bounded. Completeness and total boundedness make it compact: successively finer finite covers yield a Cauchy subsequence, and completeness keeps the limit inside the set.

Separability supplies finite approximations; completeness retains their limits. Probability organizes both within one high-probability set.

We still need to move one step further, into the event itself.

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

Now arrange these witnesses in a sequence.

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

At the same time, we must state the scope of uniqueness clearly. It holds on the \(\sigma\)-algebra generated by cylinders; it does not automatically give probabilities to arbitrary subsets of the record space. Completion can add all subsets of known null events and assign their probabilities by inclusion, but this is an explicit additional step. It neither makes every subset measurable nor resolves all uncountable path conditions at once.

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


---

# Corrections and Supplementary Proofs

This appendix was added to the restored edition. The six chapters have been restored from the master chat manuscript; this appendix does not replace or compress their original narrative. It expands key arguments treated briefly in the manuscript and identifies the deeper theorems still invoked as known results.

## A. From Finite to Countable Additivity: The Essential Intermediate Steps

Let \(\mu^*\) be an outer measure on a set \(\Omega\), and define

\[
\mathcal M=\{A\subseteq\Omega:\ \forall E\subseteq\Omega,\quad
\mu^*(E)=\mu^*(E\cap A)+\mu^*(E\setminus A)\}.
\]

Subadditivity of outer measure always gives the “\(\le\)” direction, so proving measurability requires establishing the reverse inequality. We complete the closure and countable-additivity arguments of Section 5.8 below without assuming beforehand that “the measurable sets form a \(\sigma\)-algebra.”

### A.1 Complements and Finite Unions

We have \(\varnothing\in\mathcal M\). The definition is symmetric in \(A\) and \(A^c\), so \(A\in\mathcal M\) implies \(A^c\in\mathcal M\).

Take \(A,B\in\mathcal M\). Use \(A\) to split \(E\), then use \(B\) to split \(E\setminus A\), obtaining

\[
\mu^*(E)=\mu^*(E\cap A)+\mu^*((E\setminus A)\cap B)
+\mu^*(E\setminus(A\cup B)).
\]

The first two pieces together are exactly \(E\cap(A\cup B)\). Subadditivity says that the sum of their outer measures is at least the outer measure of their union. Thus

\[
\mu^*(E)\ge\mu^*(E\cap(A\cup B))+\mu^*(E\setminus(A\cup B)).
\]

Combining this with the reverse inequality, which always holds, gives \(A\cup B\in\mathcal M\). Complements and finite unions then imply closure under finite intersections and differences. This argument uses only addition of nonnegative extended real numbers; it never subtracts a possibly infinite quantity.

### A.2 Countable Unions

First suppose that \(A_n\in\mathcal M\) are pairwise disjoint, and write \(A=\bigcup_nA_n\). Finitely many splittings give, for every \(N\),

\[
\mu^*(E)=\sum_{n=1}^N\mu^*(E\cap A_n)
+\mu^*\left(E\setminus\bigcup_{n=1}^NA_n\right)
\ge\sum_{n=1}^N\mu^*(E\cap A_n)+\mu^*(E\setminus A).
\]

Letting \(N\to\infty\) and then applying subadditivity gives

\[
\mu^*(E)\ge\sum_{n=1}^{\infty}\mu^*(E\cap A_n)+\mu^*(E\setminus A)
\ge\mu^*(E\cap A)+\mu^*(E\setminus A).
\]

Hence \(A\in\mathcal M\). A general countable union can be expressed, using

\[
B_1=A_1,\qquad B_n=A_n\setminus\bigcup_{k<n}A_k
\]

as a union of pairwise disjoint measurable sets. Thus \(\mathcal M\) is indeed a \(\sigma\)-algebra.

### A.3 Why the Restricted Measure Is Countably Additive

Again suppose that \(A_n\) are pairwise disjoint. Substituting \(E=A\) in the finite splitting above gives

\[
\mu^*(A)\ge\sum_{n=1}^N\mu^*(A_n).
\]

Taking the supremum gives the “\(\ge\)” direction; subadditivity gives “\(\le\).” Therefore

\[
\mu^*\left(\bigcup_nA_n\right)=\sum_n\mu^*(A_n).
\]

Thus \(\mu=\mu^*|_{\mathcal M}\) is a measure. We must distinguish “an outer measure is subadditive on all sets” from “its restriction to measurable sets is countably additive”: the latter is precisely the additional structure provided by the splitting criterion.

## B. When an Open Cover Is Split, What Happens to the Cutting Point?

Chapter 5 defines \(m^*\) through covers by open intervals. To prove that \(H=(-\infty,a]\) is measurable, we cannot simply split \((u,v)\) at \(a\) into two open intervals and ignore the cutting point.

Fix \(E\) and \(\varepsilon>0\). If \(m^*(E)=\infty\), subadditivity already forces

\[
m^*(E\cap H)+m^*(E\setminus H)=\infty,
\]

so equality holds. If \(m^*(E)<\infty\), choose an open-interval cover \(E\subseteq\bigcup_jI_j\) whose total length is less than \(m^*(E)+\varepsilon\).

Intervals that do not cross \(a\) need no splitting. For an interval \(I_j=(u_j,v_j)\) that crosses the cutting point, use

\[
(u_j,a+\delta_j),\qquad(a,v_j)
\]

to cover its portions in \(H\) and \(H^c\), respectively, where \(\delta_j>0\) and \(\sum_j\delta_j<\varepsilon\). Extending the left portion slightly to the right ensures that the cutting point itself is retained; the total length increases by at most \(\varepsilon\). Hence

\[
m^*(E\cap H)+m^*(E\setminus H)
\le\sum_j|I_j|+\sum_j\delta_j
<m^*(E)+2\varepsilon.
\]

Letting \(\varepsilon\downarrow0\) and applying subadditivity proves measurability. Intervals with an endpoint equal to \(a\) can be handled on the side to which they already belong; a left-hand piece containing \(a\) still uses the same slight enlargement.

Closure of the \(\sigma\)-algebra makes \((-\infty,a)=\bigcup_n(-\infty,a-1/n]\) measurable, and consequently all open intervals are measurable. Every open set is a countable union of open intervals with rational endpoints, so all Borel sets are measurable. This supplies the complete bridge from interval length to a Borel measure.

## C. Product Measure and Tonelli: From Rectangles to General Sets

The phrase “by a monotone-class argument” in Section 6.12 carries substantial content. We expand it here on \(\sigma\)-finite spaces \((X,\mathcal A,\mu)\) and \((Y,\mathcal B,\nu)\). We consider only the product \(\sigma\)-algebra \(\mathcal A\otimes\mathcal B\); completing it requires separate treatment of exceptions involving sections of null sets.

### C.1 Measurable Sections Before Integration

For \(E\subseteq X\times Y\), write \(E_x=\{y:(x,y)\in E\}\). The family of sets for which “every \(E_x\in\mathcal B\)” is closed under complements and countable unions and contains all rectangles; it therefore contains \(\mathcal A\otimes\mathcal B\). The same applies to sections in the other direction.

### C.2 The Set Identity for Finite Measures

First assume \(\mu(X),\nu(Y)<\infty\). Let \(\mathcal D\) consist of all product-measurable sets for which

\[
x\mapsto\nu(E_x),\quad y\mapsto\mu(E^y)
\]

are measurable and

\[
\int_X\nu(E_x)\,d\mu(x)=\int_Y\mu(E^y)\,d\nu(y)
\]

holds. A rectangle \(A\times B\) belongs to \(\mathcal D\), with both sides equal to \(\mu(A)\nu(B)\). The whole space also belongs to this family.

Finite total measure makes complements legitimate: a section's measure becomes the constant \(\nu(Y)\) minus the original function, and the integral identity follows by subtracting both sides from \(\mu(X)\nu(Y)\). For pairwise disjoint \(E_n\in\mathcal D\), the section measures are sums of nonnegative functions; the monotone convergence theorem gives measurability and the integral identity. Thus \(\mathcal D\) is a Dynkin system.

Rectangles are closed under finite intersections. By the \(\pi\)-\(\lambda\) theorem, \(\mathcal D\) contains the entire product \(\sigma\)-algebra they generate. The \(\pi\)-\(\lambda\) theorem invoked here is a set-theoretic tool, not Tonelli's theorem, so there is no circular use of the result being proved.

### C.3 The General \(\sigma\)-Finite Case and the Construction of the Measure

Choose \(X_k\uparrow X\) and \(Y_k\uparrow Y\), each with finite measure. Apply the preceding result to \(E\cap(X_k\times Y_k)\) and then use monotone convergence. This gives measurable section functions for general sets and equality of the two iterated integrals. Define

\[
\rho(E)=\int_X\nu(E_x)\,d\mu(x),\qquad E\in\mathcal A\otimes\mathcal B.
\]

We have \(\rho(\varnothing)=0\). If \(E_n\) are pairwise disjoint, their respective sections are also pairwise disjoint, so

\[
\rho\left(\bigcup_nE_n\right)
=\int_X\sum_n\nu((E_n)_x)\,d\mu
=\sum_n\rho(E_n).
\]

Thus \(\rho\) is a measure, and on rectangles \(\rho(A\times B)=\mu(A)\nu(B)\), with the convention \(0\cdot\infty=0\). Uniqueness on finite rectangles follows from \(\pi\)-\(\lambda\) uniqueness; a countable cover then gives uniqueness under \(\sigma\)-finiteness. This constructs \(\mu\otimes\nu\) without first assuming its existence and using it to prove its own properties.

### C.4 From Sets to Functions

The set identity is Tonelli's formula for indicator functions. Finite linear combinations give the formula for nonnegative simple functions. For nonnegative product-measurable \(f\), choose \(s_n\uparrow f\) and apply monotone convergence on the product space and in both section directions to obtain

\[
\int f\,d(\mu\otimes\nu)
=\int_X\left(\int_Yf(x,y)\,d\nu(y)\right)d\mu(x)
=\int_Y\left(\int_Xf(x,y)\,d\mu(x)\right)d\nu(y).
\]

Each side may equal \(+\infty\). For signed \(f\), first apply Tonelli to \(|f|\). If the product integral is finite, almost all sections are absolutely integrable. Apply the formula separately to \(f^+\) and \(f^-\) and subtract to obtain Fubini's theorem. Absolute integrability ensures that we have not silently performed \(\infty-\infty\).

## D. Why a Finite Second Moment Suffices: The Characteristic-Function Remainder

In Chapter 3's characteristic-function explanation of the central limit theorem, the crucial step is not formally expanding the exponential, but justifying taking expectations of its second-order expansion. Assume \(\mathbb EY=0\) and \(\mathbb EY^2=\sigma^2<\infty\). Set

\[
r(u)=e^{iu}-1-iu+\frac{u^2}{2}.
\]

The second-order Taylor expansion gives \(r(u)/u^2\to0\). There is also an absolute constant \(C\) such that \(|r(u)|\le Cu^2\) for all real arguments: for \(|u|\le1\), use the Taylor remainder; for \(|u|>1\), use \(2+|u|+u^2/2\le(7/2)u^2\).

For \(t\ne0\),

\[
\frac{r(tY)}{t^2}\longrightarrow0,\qquad
\left|\frac{r(tY)}{t^2}\right|\le CY^2.
\]

The dominated convergence theorem therefore gives

\[
\varphi_Y(t)=1-\frac{\sigma^2t^2}{2}+o(t^2).
\]

If \(\sigma>0\), independent and identically distributed \(Y_j\) satisfy

\[
\varphi_{(Y_1+\cdots+Y_n)/(\sigma\sqrt n)}(t)
=\left(1-\frac{t^2}{2n}+o(n^{-1})\right)^n\longrightarrow e^{-t^2/2}.
\]

Only after applying Lévy's continuity theorem do we obtain convergence in distribution. No third moment is needed: formally putting the random variable into a third-order remainder and assuming integrability would silently strengthen the theorem's hypotheses. Dominated convergence, established in Chapter 6, supplies exactly this missing logical link in Chapter 3.

## E. “Almost-Everywhere Limits” and Measurability

The main-text statements of monotone and dominated convergence include the assumption that the limiting function \(f\) is measurable. On an incomplete measure space, arbitrarily modifying a function on a subset of a null set need not leave it measurable. Merely being “equal almost everywhere to a measurable function” does not justify an unconditional assertion of measurability.

If we are given only measurable \(f_n\) converging outside a measurable null set, we can define the limit to be zero on the exceptional set and obtain a measurable version; for example, use the measurable upper limit and modify it on the measurable exceptional set. Integrals in nonnegative monotone convergence may take extended values, while an integrable dominating function in dominated convergence ensures that the limit is finite almost everywhere.

For nonnegative simple functions we consistently adopt \(0\cdot\infty=0\), so that a zero coefficient on a set of infinite measure does not create an undefined expression. For signed integrals, the positive- and negative-part integrals still cannot both be infinite.

## F. Exact Finite-Dimensional Increment Identities and Joint Limits for Random Walks

The step process defined in Chapter 4 is \(W_n(t)=S_{\lfloor nt\rfloor}/\sqrt n\), so

\[
W_n(t_j)-W_n(t_{j-1})
=\frac1{\sqrt n}\sum_{k=\lfloor nt_{j-1}\rfloor+1}^{\lfloor nt_j\rfloor}\xi_k
\]

is an exact identity, not an approximation obtained by ignoring boundary terms. An error of at most two partial steps arises only when we switch to linear interpolation; for \(\pm1\) steps, its absolute value is at most \(2/\sqrt n\).

Write \(m_{n,j}=\lfloor nt_j\rfloor-\lfloor nt_{j-1}\rfloor\); then \(m_{n,j}/n\to t_j-t_{j-1}>0\). Independence and the preceding characteristic-function expansion give, for any \(u_1,\ldots,u_m\),

\[
\mathbb E\exp\left(i\sum_{j=1}^mu_j\Delta_{n,j}\right)
=\prod_{j=1}^m\left[\varphi_\xi\left(\frac{u_j}{\sqrt n}\right)\right]^{m_{n,j}}
\longrightarrow\exp\left(-\frac12\sum_{j=1}^mu_j^2(t_j-t_{j-1})\right).
\]

This proves convergence of the joint distribution of the increment vector. Applying the continuous linear transformation that “adds up the increments” then gives finite-dimensional convergence of the vector of process values. This is still not weak convergence on the entire path space; that also requires tightness.

## G. The Limits of the Proofs of Deeper Theorems

The restored edition retains the master manuscript's proofs, explanations, and original links. Complete proofs of the following results are absent from the original six chapters; intuitive explanations must not be described as complete proofs of them.

| Location in the text | What this book actually supplies | What is still invoked as a known result |
|---|---|---|
| Chapter 2: long-run frequencies and posteriors | Finite-variance weak law of large numbers; specific beta–Bernoulli calculations | The reference to the strong law does not include a complete proof of the general strong law |
| Chapter 3: characteristic-function approach | Second-order expansion and product limit; Appendix D supplies remainder control | Lévy's continuity theorem and uniqueness of characteristic functions; the integral calculation of the Cauchy characteristic function remains a known example |
| Section 4.7 | Interpolation, path space, and the distinction between finite-dimensional convergence and tightness | The complete tightness proof for Donsker's invariance principle |
| Section 4.8 | Consistent finite-dimensional distributions and a fourth-moment continuity estimate | Complete proofs of the Kolmogorov extension and continuous-modification theorems |
| Section 4.10 | Increment scaling, quadratic variation, and its conflict with smoothness | The complete proof of almost-sure nowhere differentiability; an argument at a fixed time cannot be applied directly across uncountably many times |
| Section 4.11 | The pathwise idea of reflection and the maximum formula | Measure preservation of the reflection transformation can be established using the strong Markov property; the strong Markov theorem itself is not proved in the six chapters |
| Section 5.8 | The original proof strategy; Appendices A and B supply closure, additivity, and treatment of cover endpoints | The listed gaps have now been filled here |
| Section 6.12 | The original route through rectangles, simple functions, and convergence; Appendix C supplies the intermediate set argument | The \(\pi\)-\(\lambda\) theorem is invoked as a set-theoretic tool |

This table describes the scope of the proofs; it does not authorize abridging the text. It distinguishes the narrative's “why this should be true,” the proofs already completed, and the theory that still requires later development.


---

# Further Reading and Routes through the Proofs

Chapter 4 identified, through random walks, the structure that continuous random motion should have. To turn that structure into a rigorous probability model, we can continue along two connected routes: constructing the process and proving path limits. Each entry below develops a particular mathematical question.

## How Do Finite-Dimensional Distributions Give Continuous Random Motion?

Consistent joint distributions, measure extension, and continuous modifications connect finitely many coordinates to an entire random path. On continuous-function space, Wiener measure makes sets of paths into objects that probability theory can study.

[Continuous versions and Wiener measure](#advanced-wiener)

## Why Does an Entire Random-Walk Path Converge?

Linear interpolation places discrete paths in continuous-function space. Finite-dimensional limits must be accompanied by control of oscillations over small time intervals; path tightness addresses precisely this issue.

[Donsker's invariance principle and path tightness](#advanced-donsker)

## How Does Random Motion Connect to Deterministic Evolution Equations?

Starting with the evolution of position distributions, Markov semigroups and generators connect random motion with partial differential equations.

[Semigroups, generators, and deterministic evolution](#advanced-semigroup)

## Why Do Continuous Paths Need a New Calculus?

The square-root scaling of increments makes accumulated second-order effects impossible to ignore. Path regularity, quadratic variation, and stochastic integration will explain further the source of the additional term in Itô's formula.

[Path roughness, quadratic variation, and the motivation for Itô calculus](#advanced-quadratic)

## How Do We Calculate the Probability of “Having Reached” a Level?

Stopping times and the strong Markov property let us study paths after their first hitting time, while the reflection principle connects path events with Gaussian distributions.

[First hitting and the reflection principle](#advanced-reflection)

## How Can a Random Function Become a Tree?

The changing height of an excursion can encode branching and distance. Through pseudometrics, quotient spaces, and real trees, we move from random paths toward continuous random geometry.

[Excursions, real trees, and the Brownian CRT](#advanced-crt)


---

# Advanced Reading: Donsker and Tightness of Paths

> This module was transferred in full from Chapter 4 before its restructuring, retaining the original section numbers and all of the original text. It is a technical working draft for development in later chapters, rather than a required proof for the current Chapter 4.

**Destination chapters:** Chapter 12, “Distributions Enter Function Spaces”; Chapter 27, “Why Do Discrete Paths Approach Continuous Paths?”

**Prerequisites:** Convergence from Chapter 7, measurability in function spaces, Arzelà–Ascoli, Prokhorov, and Kolmogorov tightness criteria.

**Scope of the proof:** The interpolation, fourth-moment calculation, and all original derivations are retained. The original manuscript still invokes tightness criteria and tools for identifying weak limits; it does not provide a complete, self-contained proof of Donsker's theorem. The general case with only a finite second moment also requires a further proof.

[Return to the main reading of Chapter 4](#chapter-4) · [View the complete snapshot of the former Chapter 4](/downloads/04-brownian-before-restructure.md)

---

## 4.7 Donsker's Breakthrough: The Central Limit Theorem Should Extend Beyond Random Variables

> Editorial supplement: Appendix G lists the deeper theorems invoked in this chapter and the scope of the complete proofs; Appendix F supplies an additional proof of the joint finite-dimensional limit.

The central limit theorem in Chapter 3 tells us that

\[
\frac{S_n}{\sqrt n}\xrightarrow d N(0,1).
\]

What we now want to prove is that

\[
\left(
\frac{S_{\lfloor nt\rfloor}}{\sqrt n}
\right)_{0\le t\le1}
\]

can converge to Brownian motion as an entire stochastic process.

This is the central idea of what later became known as the functional central limit theorem.

Monroe Donsker's 1951 paper *An Invariance Principle for Certain Probability Limit Theorems* was an important milestone in this historical development.

The chronology needs to be distinguished from our earlier account: Donsker's work followed Wiener's rigorous construction of Brownian motion. We are taking the modern mathematical route of understanding Brownian motion anew through random-walk limits; we are not suggesting that Donsker's theorem historically preceded the invention of Brownian motion. 〔[38](#ref-turn288123search2), [39](#ref-turn288123search41)〕

### 4.7.1 First Turn Step Paths into Continuous Paths

The process defined earlier,

\[
W_n(t)=\frac{S_{\lfloor nt\rfloor}}{\sqrt n}
\]

is a step function.

At each grid time, it makes a jump of size \(1/\sqrt n\).

For any fixed \(n\), it is therefore not continuous.

To study it in a space of continuous functions, the most natural approach is linear interpolation.

Let

\[
k=\lfloor nt\rfloor,\qquad r=nt-k.
\]

Define

\[
\boxed{
\widetilde W_n(t)
=
\frac{(1-r)S_k+rS_{k+1}}{\sqrt n},
\quad0\le t<1,
}
\]

and set

\[
\widetilde W_n(1)=\frac{S_n}{\sqrt n}.
\]

Now every path of \(\widetilde W_n\) is continuous.

Moreover,

\[
\sup_{0\le t\le1}
|\widetilde W_n(t)-W_n(t)|
\le\frac1{\sqrt n}.
\]

The difference between the two representations therefore tends to zero in the uniform norm.

Notice, however, that linear interpolation only lets us place these processes in a continuous function space.

It does not automatically prove that a limit exists.

### 4.7.2 In Which Space Do We Want Convergence?

Consider

\[
C([0,1])
\]

the space of all real-valued continuous functions on \([0,1]\).

Equip it with the uniform norm:

\[
\|f\|_\infty
=
\sup_{0\le t\le1}|f(t)|.
\]

Each \(\widetilde W_n\) can then be regarded as a random element taking values in \(C([0,1])\).

This is fundamentally the same kind of object as the individual random variables studied earlier.

The difference is that the values now lie in an infinite-dimensional function space rather than in \(\mathbb R\).

We want to prove

\[
\boxed{
\widetilde W_n\xrightarrow d B
\quad\text{in }C([0,1]).
}
\]

Convergence in distribution here can be expressed using bounded continuous functionals:

for every bounded continuous map

\[
F:C([0,1])\longrightarrow\mathbb R,
\]

we have

\[
\mathbb E[F(\widetilde W_n)]
\longrightarrow
\mathbb E[F(B)].
\]

This goes beyond probabilistic convergence at a single time.

It allows us to discuss functions of an entire path, such as

\[
F(f)=\max_{0\le t\le1}f(t).
\]

The maximum functional is continuous in the uniform norm because

\[
|\max f-\max g|
\le\|f-g\|_\infty.
\]

Once we prove weak convergence in the function space, the continuous mapping theorem therefore yields a limit theorem for the maxima.

This is why the functional central limit theorem is so much more powerful than the ordinary central limit theorem.

### 4.7.3 What Is Missing from Finite-Dimensional Distributions?

In Section 4.5 we proved convergence of the finite-dimensional distributions.

But that alone is insufficient.

We must also exclude path fluctuations that become increasingly sharp and difficult to control.

Modern probability theory addresses this through one concept:

**Tightness.**

Intuitively, we want most of the probability mass of the random paths not to escape into increasingly irregular regions of function space where no convergent subsequence can be found.

In \(C([0,1])\), the Arzelà–Ascoli theorem tells us that relative compactness of a family of functions requires both boundedness at one point and uniform equicontinuity.

Tightness of stochastic processes can therefore be proved by controlling oscillations over small time intervals.

For example, we would like a moment estimate independent of \(n\):

\[
\mathbb E\left[
|\widetilde W_n(t)-\widetilde W_n(s)|^4
\right]
\le C|t-s|^2.
\]

For our symmetric random walk, such an estimate does hold.

We can even prove it directly.

Write the increment of the interpolated process over \([s,t]\) as

\[
\widetilde W_n(t)-\widetilde W_n(s)
=
\frac1{\sqrt n}\sum_j a_j\xi_j,
\]

where the coefficients satisfy \(a_j\in[0,1]\) and

\[
\sum_j a_j=n(t-s).
\]

Since the \(\xi_j\) are independent symmetric \(\pm1\) random variables, expansion of the fourth moment gives

\[
\mathbb E\left[
\left(\sum_j a_j\xi_j\right)^4
\right]
=
3\left(\sum_j a_j^2\right)^2
-
2\sum_j a_j^4.
\]

Hence

\[
\mathbb E\left[
\left(\sum_j a_j\xi_j\right)^4
\right]
\le
3\left(\sum_j a_j^2\right)^2.
\]

Also, since \(0\le a_j\le1\),

\[
\sum_j a_j^2
\le\sum_j a_j
=n(t-s).
\]

we obtain

\[
\boxed{
\mathbb E\left[
|\widetilde W_n(t)-\widetilde W_n(s)|^4
\right]
\le3|t-s|^2.
}
\]

This estimate holds for every \(n\).

It controls oscillations uniformly over the entire family of random paths.

Applying the corresponding Kolmogorov tightness criterion together with

\[
\widetilde W_n(0)=0,
\]

proves that the distributions of these processes are tight in \(C([0,1])\).

Finally, combining tightness with convergence of the finite-dimensional distributions yields the functional central limit theorem.

\[
\boxed{
\widetilde W_n\Longrightarrow B
\quad\text{in }C([0,1]).
}
\]

This is a concrete version of Donsker's invariance principle for our model.

Donsker's theorem also holds for more general independent, identically distributed random increments with mean 0 and variance 1. With only a finite second moment, the simple fourth-moment proof above may not apply directly; a more general tightness argument is required.

For the full theory of functional convergence and its proofs, see [Encyclopedia of Mathematics: Donsker invariance principle](https://encyclopediaofmath.org/wiki/Donsker_invariance_principle). 〔[38](#ref-turn288123search2), [40](#ref-turn288123search39), [39](#ref-turn288123search41)〕

We can finally say:

**Brownian motion is more than the normal limit of a random walk at a single time: it can arise as the limit in distribution of the entire random-walk path.**

This universality goes deeper than the central limit theorem of Chapter 3.

Under suitable scaling of space and time, different microscopic random mechanisms can have not only the same terminal distribution, but also the same continuous stochastic process as their limit.

---



---

# Advanced Reading: Continuous Versions and Wiener Measure

> This module was transferred in full from Chapter 4 before its restructuring, retaining the original section numbers and all of the original text. It is a technical working draft for development in later chapters, rather than a required proof for the current Chapter 4.

**Destination chapters:** Chapter 8, “Constructing Infinite Experiments from Local Rules”; Chapter 24, “The Rigorous Birth of Continuous Random Paths.”

**Prerequisites:** Measure extension, Gaussian vectors, consistent finite-dimensional distributions, Kolmogorov's continuous modification theorem, and measurability of the path map.

**Scope of the proof:** Statements in the original manuscript that a process is “obtained” or “constructed” are conditional conclusions after invoking the extension and continuous modification theorems; Chapter 4 has not proved those theorems. The construction route is preserved in full here, without presenting it as a completed construction of Wiener measure.

[Return to the main reading of Chapter 4](#chapter-4) · [View the complete snapshot of the former Chapter 4](/downloads/04-brownian-before-restructure.md)

---

### 4.8.1 Does Continuous Brownian Motion Really Exist?

The functional limit theorem for random walks has already suggested one route to a construction.

But there is another very important approach.

We can start with the covariance kernel

\[
K(s,t)=\min(s,t).
\]

For any finite collection of times \(t_1,\ldots,t_m\), the matrix

\[
\left(K(t_i,t_j)\right)_{i,j=1}^m
\]

is positive semidefinite.

Indeed, using

\[
K(s,t)=\int_0^\infty
\mathbf1_{\{u\le s\}}\mathbf1_{\{u\le t\}}\,du,
\]

we have

\[
\begin{aligned}
\sum_{i,j=1}^m a_ia_jK(t_i,t_j)
&=\int_0^\infty
\left(\sum_{i=1}^m a_i\mathbf1_{\{u\le t_i\}}\right)^2du\\
&\ge0.
\end{aligned}
\]

These matrices can therefore serve as covariance matrices of centered Gaussian vectors.

They also satisfy the consistency conditions required when time coordinates are deleted or reordered.

The Kolmogorov extension theorem thus allows us to construct a Gaussian process with these finite-dimensional distributions.

But one last step remains.

We must prove that it has a continuous modification.

Since

\[
B_t-B_s\sim N(0,t-s),
\]

we have

\[
\mathbb E[|B_t-B_s|^4]
=
3|t-s|^2.
\]

This satisfies a moment condition of the kind required by Kolmogorov's continuity theorem.

We can therefore construct a version with continuous sample paths.

Only at this point have we truly obtained continuous-time Brownian motion. 〔[41](#ref-turn288123search36), [42](#ref-turn288123search38)〕

This proof route also illustrates the layered structure of modern probability theory:

\[
\boxed{
\begin{gathered}
\text{consistent finite-dimensional probability distributions}\\
\Downarrow\\
\text{existence of a stochastic process}\\
\Downarrow\\
\text{moment estimates for increments}\\
\Downarrow\\
\text{existence of a version with continuous paths}
\end{gathered}
}
\]

These steps are distinct theorems, and none can simply be omitted.

### 4.8.2 Wiener Measure: An Entire Function Can Be a Random Variable

We now know that the sample paths of Brownian motion almost surely belong to

\[
C([0,1]).
\]

The most natural idea is therefore to take continuous functions themselves as the outcomes in a probability space.

Let

\[
\Omega=C_0([0,1])
=
\{f\in C([0,1]):f(0)=0\}.
\]

and equip it with the Borel \(\sigma\)-algebra generated by the uniform norm.

We want to construct a probability measure \(\mathbb W\) on this function space such that the coordinate maps

\[
B_t(\omega)=\omega(t)
\]

form a standard Brownian motion.

This measure is called Wiener measure.

We can then assign probabilities to events in the entire function space.

For example:

\[
A=\left\{
\omega:\sup_{0\le t\le1}\omega(t)\ge1
\right\}.
\]

This is no longer an event concerning a single time.

It asks whether the whole path ever reaches a given height.

We can write

\[
\mathbb W(A)
=
P\left(\sup_{0\le t\le1}B_t\ge1\right).
\]

Notice that this answers the question left open at the end of Chapter 1.

What should we do when outcomes can no longer be described by counting?

Our sample space is now not even an interval, but an infinite-dimensional function space.

Probability can still be defined because its true foundation is a measure satisfying appropriate axioms, rather than “the number of favorable outcomes divided by the total number of outcomes.”

Here a random variable can be a real number, a continuous function, or even a more complicated random geometric object.

**Modern probability theory begins to free itself from dependence on the particular form of its random outcomes.**

This is an indispensable foundation for our later study of random trees and the CRT.

---



---

# Advanced Reading: From Random Motion to Semigroups and Generators

> This module was transferred in full from Chapter 4 before its restructuring, retaining the old section numbers and all original text. It is a technical working draft for later chapters to build on, rather than a required part of the proofs in the current Chapter 4.

**Destination chapters:** Chapter 20, “Systems That Remember Only the Present”; Chapter 31, “Probabilistic Evolution and Deterministic Equations.”

**Prerequisites:** Lebesgue integration, conditional distributions, the Markov property, operator semigroups, and domains of generators.

**Scope of the proof:** The original derivations of the semigroup and generator have been moved here in full. This module assumes Brownian motion has already been constructed; it does not claim that Chapter 4 has established semigroup theory.

[Return to the main narrative of Chapter 4](#chapter-4) · [View the complete snapshot of the old Chapter 4](/downloads/04-brownian-before-restructure.md)

---

### 4.9.3 A Unification: Random Paths and Deterministic Evolution

We now have two entirely different descriptions.

The first is the random path:

\[
t\longmapsto B_t(\omega).
\]

Each \(\omega\) corresponds to a different random trajectory.

The second is the probability density:

\[
(t,x)\longmapsto p_t(x).
\]

This function is governed by the deterministic heat equation.

For a sufficiently regular function \(f\), define

\[
P_tf(x)
=
\mathbb E[f(x+B_t)].
\]

Since Brownian motion has independent, stationary increments,

\[
P_{t+s}f=P_t(P_sf).
\]

Thus \((P_t)_{t\ge0}\) forms a Markov semigroup.

Its infinitesimal generator satisfies

\[
\lim_{h\downarrow0}
\frac{P_hf(x)-f(x)}{h}
=
\frac12f''(x),
\]

for example, for \(f\in C_c^\infty(\mathbb R)\).

Therefore

\[
\boxed{
L=\frac12\frac{d^2}{dx^2}.
}
\]

The corresponding evolution equation is precisely

\[
\frac{\partial u}{\partial t}=Lu.
\]

We obtain an exceptionally important unifying relationship:

\[
\boxed{
\text{stochastic processes}
\longleftrightarrow
\text{Markov semigroups}
\longleftrightarrow
\text{partial differential equations}.
}
\]

This is more than a symbolic correspondence.

It means that random motion can explain partial differential equations, while partial differential equations can be used to study the probability distributions of stochastic processes.

In stochastic calculus, the Feynman–Kac formula, and stochastic differential equations, we will repeatedly encounter the importance of this connection.

---



---

# Advanced Reading: Path Roughness, Quadratic Variation, and the Motivation for Itô Calculus

> This module was transferred in full from Chapter 4 before its restructuring, retaining the old section numbers and all original text. It is a technical working draft for later chapters to build on, rather than a required part of the proofs in the current Chapter 4.

**Destination chapters:** Chapter 24, on path regularity; Chapter 28, “Noise That Ordinary Calculus Cannot Accumulate”; Chapter 29, “The Term Left by Second-Order Variation.”

**Prerequisites:** Existence of Brownian motion, L2 convergence, Borel–Cantelli, stochastic integration, and Itô’s formula.

**Scope of the proof:** The opening statement “We have now actually constructed” retains the context of the old chapter and applies only after the construction above has been completed. An argument about difference quotients at a fixed time cannot replace a proof of almost sure nowhere differentiability; the original quadratic-variation proof fixes T and uses dyadic grids; Itô’s formula remains a preview.

[Return to the main narrative of Chapter 4](#chapter-4) · [View the complete snapshot of the old Chapter 4](/downloads/04-brownian-before-restructure.md)

---

## 4.10 Continuous Yet Not Differentiable: Another Paradox of Brownian Motion

We have now actually constructed Brownian motion.

It has continuous sample paths:

\[
t\longmapsto B_t(\omega).
\]

At first glance, since the particle’s position changes continuously with time, it seems we should be able to define its instantaneous velocity:

\[
v(t)=\lim_{h\to0}\frac{B_{t+h}-B_t}{h}.
\]

But matters are not that simple.

By the definition of Brownian motion,

\[
B_{t+h}-B_t\sim N(0,h)
\]

for \(h>0\).

Thus

\[
\frac{B_{t+h}-B_t}{h}
\sim N\left(0,\frac1h\right).
\]

As \(h\downarrow0\), the variance of this difference quotient actually tends to infinity.

The difference quotient therefore does not become increasingly concentrated near any finite value.

Indeed, for any fixed \(M>0\),

\[
P\left(
\left|\frac{B_{t+h}-B_t}{h}\right|\le M
\right)\longrightarrow0.
\]

These difference quotients cannot therefore even converge in probability to a finite random variable.

But this is still not the strongest conclusion.

Brownian sample paths are in fact almost surely **nowhere differentiable**.

This is a surprising fact:

\[
\boxed{
\text{sample paths are continuous}
\quad\text{but almost surely nowhere differentiable}.
}
\]

In calculus, we became accustomed to an intuition:

Continuous functions represent smooth motion, and velocity should be obtained by differentiating position.

Brownian motion overturns this intuition completely.

It is continuous motion with a rigorous mathematical existence, yet its paths are too rough to describe using ordinary differentiation. For proofs and the historical development of path regularity, see modern probability texts on Brownian motion.〔[45](#ref-turn516523search41), [46](#ref-turn288123search37)〕

We can, however, understand this roughness through a more structural quantity.

### 4.10.1 How Rough Is a Path?

On the interval \([0,T]\), consider the dyadic grid

\[
t_k=\frac{kT}{2^m},
\qquad k=0,\ldots,2^m.
\]

Define the sum of squared increments:

\[
Q_m=
\sum_{k=0}^{2^m-1}
(B_{t_{k+1}}-B_{t_k})^2.
\]

Since the increments are independent and

\[
B_{t_{k+1}}-B_{t_k}
\sim N\left(0,\frac{T}{2^m}\right),
\]

we have

\[
\mathbb E[Q_m]
=
2^m\cdot\frac{T}{2^m}
=T.
\]

A normal random variable with mean 0 and variance \(v\), denoted by \(Z\), satisfies

\[
\operatorname{Var}(Z^2)=2v^2.
\]

Therefore

\[
\begin{aligned}
\operatorname{Var}(Q_m)
&=
2^m\cdot2\left(\frac{T}{2^m}\right)^2\\
&=\frac{2T^2}{2^m}.
\end{aligned}
\]

Thus

\[
Q_m\longrightarrow T
\]

in \(L^2\).

Furthermore, Chebyshev’s inequality gives

\[
P(|Q_m-T|>\varepsilon)
\le
\frac{2T^2}{\varepsilon^2 2^m}.
\]

The right-hand side is summable in \(m\).

The Borel–Cantelli lemma therefore yields

\[
\boxed{
Q_m\xrightarrow{\mathrm{a.s.}}T.
}
\]

This is a rigorous statement of Brownian motion’s quadratic variation along dyadic grids.

We usually write

\[
\boxed{[B]_T=T.}
\]

### 4.10.2 Why Is This Completely Different from Ordinary Smooth Functions?

Suppose \(f:[0,T]\to\mathbb R\) is continuously differentiable.

The mean value theorem gives

\[
|f(t_{k+1})-f(t_k)|
\le M(t_{k+1}-t_k)
\]

where

\[
M=\sup_{0\le t\le T}|f'(t)|<\infty.
\]

Hence

\[
\begin{aligned}
\sum_k(f(t_{k+1})-f(t_k))^2
&\le
M^2\sum_k(t_{k+1}-t_k)^2\\
&=M^2\frac{T^2}{2^m}\\
&\longrightarrow0.
\end{aligned}
\]

For a smooth function, the sum of squared increments along increasingly fine grids therefore tends to zero.

Brownian motion, however, satisfies

\[
\sum_k(B_{t_{k+1}}-B_{t_k})^2
\longrightarrow T.
\]

In other words:

\[
\boxed{
\begin{aligned}
\text{smooth paths：}&\quad [f]_T=0,\\
\text{Brownian paths：}&\quad [B]_T=T.
\end{aligned}
}
\]

This goes deeper than saying that “the paths are somewhat unsmooth.”

It shows that Brownian motion has a cumulative second-order effect that ordinary calculus cannot disregard.

### 4.10.3 Why Must Stochastic Calculus Be Reinvented?

In ordinary calculus, we often disregard second-order infinitesimals.

Indeed, if

\[
dx=O(dt),
\]

then

\[
(dx)^2=O(dt^2),
\]

which tends to zero after division by \(dt\).

For Brownian motion, however, typical increments have the scale

\[
dB\sim O(\sqrt{dt})
\]

shown above.

Thus

\[
(dB)^2\sim O(dt).
\]

The accumulated contribution of squared increments is therefore of the same order as the first-order time increments.

We can no longer disregard it as in ordinary calculus.

This is the fundamental reason why the formal relationship

\[
\boxed{(dB_t)^2=dt}
\]

will appear in Itô calculus.

This is not algebra that treats \(dB_t\) as an ordinary real differential; it is concise notation for the quadratic-variation structure within the theory of stochastic integration.

For example, ordinary calculus might lead us to expect

\[
d(B_t^2)=2B_t\,dB_t.
\]

whereas Itô’s formula actually gives

\[
\boxed{
d(B_t^2)=2B_t\,dB_t+dt.
}
\]

The additional \(dt\) arises precisely from Brownian motion’s nonzero quadratic variation.

We have not yet established stochastic integration rigorously, so this remains a preview of the theory to come.

But it already reveals a very important pattern in the development of probability:

**New theories of integration arise because new random objects cannot be fully described by existing calculus, rather than simply because mathematicians want more complicated formulas.**

---



---

# Advanced Reading: First Passage and the Reflection Principle

> This module was transferred in full from Chapter 4 before its restructuring, retaining the original section numbers and all of the original text. It is a technical working draft for development in later chapters, rather than a required proof for the current Chapter 4.

**Destination chapter:** Chapter 25, “Hitting, Reflection, and Path Decomposition.”

**Prerequisites:** Continuous paths, stopping times, the natural filtration, the strong Markov theorem, and the measure-preserving property of the reflection transformation.

**Scope of the proof:** The original account of reflection, its formulas, and the first-passage-time calculation are all retained. The strong Markov property and the measure-preserving property of reflection still require systematic proofs; geometric symmetry is not treated as a complete proof.

[Return to the main reading of Chapter 4](#chapter-4) · [View the complete snapshot of the former Chapter 4](/downloads/04-brownian-before-restructure.md)

---

## 4.11 Why Does a Random Path Contain More Information Than a Random Variable?

So far, we know that

\[
B_T\sim N(0,T).
\]

This tells us where the particle is at time \(T\).

But suppose we want to ask:

By time \(T\), has the particle ever reached a height \(a>0\)?

This is a completely different question.

Define the first-passage time

\[
\tau_a=\inf\{t\ge0:B_t=a\}.
\]

What we really want is

\[
P(\tau_a\le T).
\]

This event depends on the whole path, as opposed to the final position \(B_T\) alone.

For example, the particle might reach height \(a\) and then return close to the origin.

Observing only the final position cannot tell us whether this happened.

But the special symmetry of Brownian motion allows us to calculate the probability of this path event.

### 4.11.1 The Reflection Principle

Consider all paths that, by time \(T\), reach height \(a\) but finish below \(a\).

For each such path, reflect the portion after its first arrival at height \(a\) across the horizontal line \(y=a\).

By the strong Markov property of Brownian motion after the first-passage time and the symmetry of its increments, this reflection gives a probability correspondence between the relevant path events.

We obtain the reflection principle:

\[
\boxed{
P\left(\sup_{0\le t\le T}B_t\ge a\right)
=
2P(B_T\ge a).
}
\]

Since

\[
B_T\sim N(0,T),
\]

we have

\[
P(B_T\ge a)
=
1-\Phi\left(\frac a{\sqrt T}\right),
\]

where \(\Phi\) is the standard normal distribution function.

Therefore

\[
\boxed{
P(\tau_a\le T)
=
2\left[
1-\Phi\left(\frac a{\sqrt T}\right)
\right].
}
\]

This formula deserves close attention.

The central limit theorem originally gave us a Gaussian distribution at a fixed time.

Path symmetry now lets us use it to calculate the probability of a first-passage event as well.

We can even derive the density of the first-passage time:

\[
\boxed{
f_{\tau_a}(t)
=
\frac{a}{\sqrt{2\pi t^3}}
\exp\left(-\frac{a^2}{2t}\right),
\qquad t>0.
}
\]

Interestingly,

\[
P(\tau_a<\infty)=1,
\]

but

\[
\mathbb E[\tau_a]=\infty.
\]

Thus the particle almost surely eventually reaches any fixed positive height, yet the expected waiting time to reach it is infinite.

This reminds us once again:

An event occurring almost surely does not imply that its waiting time has finite expectation.

From first-passage problems for discrete random walks to the reflection principle for continuous Brownian motion, probability theory begins to develop a theory of entire random trajectories.

---



---

# Advanced Reading: From Brownian Paths to Random Trees

> This module was transferred in full from Chapter 4 before its restructuring, retaining the original section numbers and all of the original text. It is a technical working draft for development in later chapters, rather than a required proof for the current Chapter 4.

**Destination chapters:** Chapter 25, excursions and path decomposition; Chapter 43, path encoding; Chapter 45, real trees; Chapter 46, the Brownian CRT (following the locations in the existing draft).

**Prerequisites:** Excursions, pseudometrics and quotient spaces, properties of real trees, normalization, and weak convergence in function spaces.

**Scope of the proof:** The list of topics “already developed” at the start of the old section reviews the former manuscript, rather than recording what the current reading edition has completed. The tree-encoding formulas and SVG illustration are preserved; the CRT construction and limit theorems have not been proved within the six chapters.

[Return to the main reading of Chapter 4](#chapter-4) · [View the complete snapshot of the former Chapter 4](/downloads/04-brownian-before-restructure.md)

---

## 4.12 Why Is Brownian Motion So Important for the Future of Probability Theory?

Starting from a very simple random walk, we have gradually developed:

- probability measures on infinite-dimensional function spaces;
- continuous Gaussian processes;
- the functional central limit theorem;
- Markov semigroups and the heat equation;
- random paths that are continuous but nondifferentiable;
- quadratic variation and the need for stochastic calculus;
- first-passage times and path events.

These concepts seem to span probability theory, functional analysis, partial differential equations, and differential geometry.

But their appearance together is no accident.

They all center on one fundamental question:

**How can we understand an object that continually generates fresh randomness over time?**

Brownian motion provides a particularly precise and rich mathematical model for this question.

More importantly, it teaches us for the first time to treat a random function as a basic object in a probability space.

The significance of this extends far beyond Brownian motion itself.

### 4.12.1 From Brownian Paths to Random Trees

Let us glimpse a construction that will return later.

Suppose we have a nonnegative continuous function

\[
e:[0,1]\to[0,\infty)
\]

satisfying

\[
e(0)=e(1)=0.
\]

For example, \(e\) might be a Brownian excursion.

We can define

\[
m_e(s,t)
=
\inf_{u\in[s\wedge t,s\vee t]}e(u).
\]

and then set

\[
\boxed{
d_e(s,t)
=
e(s)+e(t)-2m_e(s,t).
}
\]

This expression is worth examining closely.

It is the sum of the heights at two times, minus twice the lowest common height encountered between them.

If the rises and falls of the continuous function represent a depth-first traversal of a tree, the expression has the meaning of distance in that tree.

By identifying times satisfying

\[
d_e(s,t)=0
\]

we can construct a quotient space.

For suitable excursions, this quotient space has the structure of a real tree.

When \(e\) is a suitably normalized Brownian excursion, this connects with the classical construction of the Brownian CRT; the precise scale factor depends on the normalization convention.

Illustrating the idea of passing from a continuous function to tree geometry

<svg viewBox="0 0 340 185" width="100%" xmlns="http://www.w3.org/2000/svg">
    <path d="M15 130 C34 129 38 95 55 88 S76 35 89 54 S106 109 124 96 S145 43 165 50 S185 85 201 72 S224 35 245 60 S272 106 285 99 S311 131 325 130 L325 130 L15 130 Z" fill="#168782" opacity="0.12"/>
    <path d="M15 130 C34 129 38 95 55 88 S76 35 89 54 S106 109 124 96 S145 43 165 50 S185 85 201 72 S224 35 245 60 S272 106 285 99 S311 131 325 130" fill="none" stroke="#168782" stroke-width="2.6" stroke-linecap="round"/>
    <line x1="15" y1="130" x2="325" y2="130" stroke="currentColor" opacity="0.4"/>
    <text x="170" y="158" font-size="12" fill="currentColor" text-anchor="middle">Continuous excursion function e(t)</text>
    <text x="170" y="177" font-size="11" fill="currentColor" opacity="0.7" text-anchor="middle">Height changes encode branches and distances in a tree</text>
  </svg>

Conceptual diagram: This is a schematic continuous excursion curve, not an actual simulation of a Brownian excursion.

Brownian motion therefore gives us more than a continuous stochastic process.

It also supplies important material for passing from discrete combinatorial structures to continuous random geometry.

In our future study of the CRT, we will encounter many of today's ideas again:

random walks, weak convergence in function spaces, tightness, excursions, quotient spaces, and geometric structures induced by random functions.

This is a deep unification that we can already foresee.

---



---

# References and Image Sources

Citations in the text have been restored at their original locations. Below, “original citation” means that the link was recovered from chat metadata; it does not mean that the entire content of every source was reverified in this restoration. The first four original identifiers have no recoverable URLs and are explicitly listed with supplementary sources checked during restoration; no original links have been fabricated. Images have been downloaded and embedded, so offline reading does not require loading the source websites.

<a id="ref-turn673477search0"></a>

1. The link for the original identifier `turn673477search0` could not be recovered. Supplementary sources checked during restoration: [ETH Library: From games of chance to probability theory](https://library.ethz.ch/en/collections-and-archives/platforms/virtual-exhibitions/Its-all-math-and-games/game-types/from-games-of-chance-to-probability-theory.html), [MacTutor: Pascal](https://mathshistory.st-andrews.ac.uk/Biographies/Pascal/). These two pages support the passage’s background on the early problem of points, the 1654 correspondence, and Huygens’s 1657 work; they do not establish which page each original identifier referred to.

<a id="ref-turn673477search2"></a>

2. The link for the original identifier `turn673477search2` could not be recovered. Supplementary sources checked during restoration: [ETH Library: From games of chance to probability theory](https://library.ethz.ch/en/collections-and-archives/platforms/virtual-exhibitions/Its-all-math-and-games/game-types/from-games-of-chance-to-probability-theory.html), [MacTutor: Pascal](https://mathshistory.st-andrews.ac.uk/Biographies/Pascal/). These two pages support the passage’s background on the early problem of points, the 1654 correspondence, and Huygens’s 1657 work; they do not establish which page each original identifier referred to.

<a id="ref-turn673477search4"></a>

3. The link for the original identifier `turn673477search4` could not be recovered. Supplementary sources checked during restoration: [ETH Library: From games of chance to probability theory](https://library.ethz.ch/en/collections-and-archives/platforms/virtual-exhibitions/Its-all-math-and-games/game-types/from-games-of-chance-to-probability-theory.html), [MacTutor: Pascal](https://mathshistory.st-andrews.ac.uk/Biographies/Pascal/). These two pages support the passage’s background on the early problem of points, the 1654 correspondence, and Huygens’s 1657 work; they do not establish which page each original identifier referred to.

<a id="ref-turn673477search7"></a>

4. The link for the original identifier `turn673477search7` could not be recovered. Supplementary sources checked during restoration: [ETH Library: From games of chance to probability theory](https://library.ethz.ch/en/collections-and-archives/platforms/virtual-exhibitions/Its-all-math-and-games/game-types/from-games-of-chance-to-probability-theory.html), [MacTutor: Pascal](https://mathshistory.st-andrews.ac.uk/Biographies/Pascal/). These two pages support the passage’s background on the early problem of points, the 1654 correspondence, and Huygens’s 1657 work; they do not establish which page each original identifier referred to.

<a id="ref-turn689420search25"></a>

5. [A History of Probability and](https://www.mdthinducollege.org/ebooks/statistics/A_History_of_Probability_and_Statistics.pdf). Original citation identifier: `turn689420search25`.

<a id="ref-turn689420search2"></a>

6. [turn689420search2](https://www.york.ac.uk/depts/maths/histstat/galileo.htm). Original citation identifier: `turn689420search2`.

<a id="ref-turn689420search26"></a>

7. [Studies in the History of Probability and Statistics I. Dicing and Gaming (A Note on](https://crypto.di.uoa.gr/dmath2014/Diakrita_Mathematika_2014/Anakoinose_5_files/Studies_in_the_History_of_Probability_and_Statistics_I._Dicing_and_Gaming.pdf). Original citation identifier: `turn689420search26`.

<a id="ref-turn561005search0"></a>

8. [Interpretations of Probability (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/probability-interpret/). Original citation identifier: `turn561005search0`.

<a id="ref-turn561005search3"></a>

9. [Formal Epistemology (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/formal-epistemology/). Original citation identifier: `turn561005search3`.

<a id="ref-turn561005search25"></a>

10. [Classical definition of probability](https://en.wikipedia.org/wiki/Classical_definition_of_probability). Original citation identifier: `turn561005search25`.

<a id="ref-turn557906search0"></a>

11. [Tercentenary of <i>Ars Conjectandi</i> (1713): Jacob Bernoulli and the Founding of Mathematical Probability - Sylla - 2014 - International Statistical Review - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/insr.12050). Original citation identifier: `turn557906search0`.

<a id="ref-turn557906search5"></a>

12. [The art of conjecturing (1692[?] published 1713) (Chapter 16) - The Emergence of Probability](https://www.cambridge.org/core/books/abs/emergence-of-probability/art-of-conjecturing-1692-published-1713/61B6958151D52354FBB5043742FFACC0). Original citation identifier: `turn557906search5`.

<a id="ref-turn557906search11"></a>

13. [The first limit theorem (Chapter 17) - The Emergence of Probability](https://www.cambridge.org/core/books/abs/emergence-of-probability/first-limit-theorem/EBFF13F0A03A69E20A2C23C898203A73). Original citation identifier: `turn557906search11`.

<a id="ref-turn557906search1"></a>

14. [Bernoulli theorem - Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Bernoulli_theorem). Original citation identifier: `turn557906search1`.

<a id="ref-turn557906search3"></a>

15. [An Essay towards Solving a Problem in the Doctrine of Chances. By the Late Rev. Mr. Bayes, F. R. S. Communicated by Mr. Price, in a Letter to John Canton, A. M. F. R. S. | JSTOR](https://www.jstor.org/stable/105741). Original citation identifier: `turn557906search3`.

<a id="ref-turn310466search0"></a>

16. [turn310466search0](https://www.york.ac.uk/depts/maths/histstat/essay.htm). Original citation identifier: `turn310466search0`.

<a id="ref-turn310466search6"></a>

17. [Thomas Bayes (1702 - 1761) - Biography - MacTutor History of Mathematics](https://mathshistory.st-andrews.ac.uk/Biographies/Bayes/). Original citation identifier: `turn310466search6`.

<a id="ref-turn310466search24"></a>

18. [BULLETIN (New Series) OF THE](https://www.stat.yale.edu/~pollard/Courses/241.fall2005/notes2005/ThomasBayes.pdf). Original citation identifier: `turn310466search24`.

<a id="ref-turn310466search26"></a>

19. [Bayes Biography](https://www2.isye.gatech.edu/isyebayes/bank/bayesbiog.pdf). Original citation identifier: `turn310466search26`.

<a id="ref-turn310466search8"></a>

20. [Was Bayes a Bayesian? - ScienceDirect](https://www.sciencedirect.com/science/article/pii/0315086087900656). Original citation identifier: `turn310466search8`.

<a id="ref-turn557906search12"></a>

21. [Pierre-Simon Laplace (1749 - 1827) - Biography - MacTutor History of Mathematics](https://mathshistory.st-andrews.ac.uk/Biographies/Laplace/). Original citation identifier: `turn557906search12`.

<a id="ref-turn234816search0"></a>

22. [Moivre](https://www.probabilityandfinance.com/pulskamp/Moivre/index.html). Original citation identifier: `turn234816search0`.

<a id="ref-turn234816search4"></a>

23. [De Moivre's Normal Approximation to the Binomial Distribution, 1733 - 1990 - Wiley Series in Probability and Statistics - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/0471725161.ch24). Original citation identifier: `turn234816search4`.

<a id="ref-turn234816search30"></a>

24. [JSS 18 (1) (1966)  2-15](https://www.actuaries.org.uk/system/files/documents/pdf/0002-0015.pdf). Original citation identifier: `turn234816search30`.

<a id="ref-turn234816search3"></a>

25. [Abraham de Moivre (1667 - 1754) - Biography - MacTutor History of Mathematics](https://mathshistory.st-andrews.ac.uk/Biographies//De_Moivre/). Original citation identifier: `turn234816search3`.

<a id="ref-turn234816search8"></a>

26. [A history of mathematical statistics from 1750 to 1930-Hald](https://www.york.ac.uk/depts/maths/histstat/haldcontents.htm). Original citation identifier: `turn234816search8`.

<a id="ref-turn234816search6"></a>

27. [Classic Topics on The History of Modern Mathematical Statistics: From Laplace to More Recent Times | Mathematical Association of America](https://old.maa.org/node/743958). Original citation identifier: `turn234816search6`.

<a id="ref-turn523153search2"></a>

28. [A history of mathematical statistics from 1750 to 1930-Hald](https://www.york.ac.uk/depts/maths/histstat/haldcontents.htm). Original citation identifier: `turn523153search2`.

<a id="ref-turn523153search1"></a>

29. [A short history of probability and statistics: 19th century](https://web.universiteitleiden.nl/fsw/verduin/stathist/sh_19.htm). Original citation identifier: `turn523153search1`.

<a id="ref-turn234816search7"></a>

30. [Ellis on Mathematical Statistics and Probability | Springer Nature Link](https://link.springer.com/chapter/10.1007/978-3-030-85258-0_5). Original citation identifier: `turn234816search7`.

<a id="ref-turn360592search6"></a>

31. [August 1827: Robert Brown and Molecular Motion in a Pollen-filled Puddle | American Physical Society](https://www.aps.org/apsnews/2016/08/robert-brown-molecular-motion-pollen). Original citation identifier: `turn360592search6`.

<a id="ref-turn360592search7"></a>

32. [Controlling the Unobservable: Experimental Strategies and Hypotheses in Discovering the Causal Origin of Brownian Movement | Springer Nature Link](https://link.springer.com/chapter/10.1007/978-3-031-52954-2_8). Original citation identifier: `turn360592search7`.

<a id="ref-turn360592search3"></a>

33. [The case of Brownian motion | The British Journal for the History of Science | Cambridge Core](https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/abs/case-of-brownian-motion/7E6FCB8188956D072CC83581B5645099). Original citation identifier: `turn360592search3`.

<a id="ref-turn360592search4"></a>

34. [HISTORICAL BACKGROUND | Brownian Motion: Fluctuations, Dynamics, and Applications | Oxford Academic](https://academic.oup.com/book/11539/chapter-abstract/160327134). Original citation identifier: `turn360592search4`.

<a id="ref-turn360592search5"></a>

35. [111 years of Brownian motion - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5476231/). Original citation identifier: `turn360592search5`.

<a id="ref-turn360592search8"></a>

36. [<fc>B</fc>achelier, <fc>L</fc>ouis (1870–1946) - Bru - Major Reference Works - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1002/9780470061602.eqf01001). Original citation identifier: `turn360592search8`.

<a id="ref-turn360592search0"></a>

37. [Brownian motion (Chapter 3) - Brownian Motion, Hardy Spaces and Bounded Mean Oscillation](https://www.cambridge.org/core/books/abs/brownian-motion-hardy-spaces-and-bounded-mean-oscillation/brownian-motion/3CD3E9FFEC8D67436382783C54566CFE). Original citation identifier: `turn360592search0`.

<a id="ref-turn288123search2"></a>

38. [Donsker invariance principle - Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Donsker_invariance_principle). Original citation identifier: `turn288123search2`.

<a id="ref-turn288123search41"></a>

39. [Lecture 14: Brownian Motion](https://web.ma.utexas.edu/users/gordanz/notes/brownian_motion.pdf). Original citation identifier: `turn288123search41`.

<a id="ref-turn288123search39"></a>

40. [Advanced Probability](https://www2.math.upenn.edu/~qze/notes/AP14.pdf). Original citation identifier: `turn288123search39`.

<a id="ref-turn288123search36"></a>

41. [2.5 Kolmogorov Continuity Theorem.](https://www.stt.msu.edu/Links/Research_Memoranda/RM/RM_703.pdf). Original citation identifier: `turn288123search36`.

<a id="ref-turn288123search38"></a>

42. [Theorem 2.6 (Kolmogorov Extension Theorem). Given a set of compatible finite dimensional distributions \(\{\mu_{t_1\ldots t_m}\}\) with indexing set \(T\), there exists a probability space \((\Omega,\mathcal{F},\mathbb{P})\) and a stochastic process \(\{X_t\}\) so that \(X_t\) has the required finite dimensional distributions, i.e. for all \(t_1 < \cdots < t_m \in T\) and \(A_1,\ldots,A_m \in \mathcal{B}\) we have](https://sites.math.duke.edu/~agazzi/notes_MAR31st.pdf). Original citation identifier: `turn288123search38`.

<a id="ref-turn516523search36"></a>

43. [Partial Diﬀerential Equations and Diﬀusion Processes](https://math.stanford.edu/~ryzhik/STANFORD/STANF227-11/notes227-09.pdf). Original citation identifier: `turn516523search36`.

<a id="ref-turn516523search1"></a>

44. [AMS :: Notices of the American Mathematical Society](https://doi.org/10.1090%2Fnoti2663). Original citation identifier: `turn516523search1`.

<a id="ref-turn516523search41"></a>

45. [Stochastic Processes](https://www.jacopoborga.com/wp-content/uploads/2021/12/Notes_Dembo.pdf). Original citation identifier: `turn516523search41`.

<a id="ref-turn288123search37"></a>

46. [1. LECTURE 1: APRIL 3, 2012](https://www.math.ucsd.edu/~tkemp/285.LectureNotes.pdf). Original citation identifier: `turn288123search37`.

<a id="ref-turn701804search1"></a>

47. [The Early Development of Set Theory (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/settheory-early/). Original citation identifier: `turn701804search1`.

<a id="ref-turn701804search0"></a>

48. [Studies in the history of probability and statistics XLVI. Measure into probability: from Lebesgue to Kolmogorov | Biometrika | Oxford Academic](https://academic.oup.com/biomet/article-abstract/87/1/145/221413). Original citation identifier: `turn701804search0`.

<a id="ref-turn701804search4"></a>

49. [On the problem of measuring sets of points by Giuseppe Vitali](https://jamesrmeyer.com/infinite/vitali-paper-measure-points-on-line). Original citation identifier: `turn701804search4`.

<a id="ref-turn701804search35"></a>

50. [Elementary Real Analysis](https://classicalrealanalysis.info/documents/BBT-Chapters1-4-Landscape.pdf). Original citation identifier: `turn701804search35`.

<a id="ref-turn701804search39"></a>

51. [From the beginning of set theory to Lebesgue’s measure problem](https://www.utupub.fi/server/api/core/bitstreams/a1457eec-6784-4528-bd0b-cdc5910ca876/content). Original citation identifier: `turn701804search39`.

<a id="ref-turn701804search6"></a>

52. [Lebesgue Measure · Guidebook 3A.2 · Neckpinch](https://neckpinch.com/guide/measure-integration-and-lp/lebesgue-measure/). Original citation identifier: `turn701804search6`.

<a id="ref-turn701804search37"></a>

53. [Foundations of Quantitative](https://s3-euw1-ap-pe-df-pch-content-store-p.s3.eu-west-1.amazonaws.com/9781003264576/151f38ce-a793-4aef-8b92-7d08baf495d7/preview.pdf?AWSAccessKeyId=ASIAQFVOSJ573K44BTGI&Expires=1773391788&Signature=tbfzdk9M30ykNp02V8LVoQQwyU4%3D&response-content-disposition=attachment%3B+filename%3D%2210.1201_9781003264576_previewpdf.pdf%22&x-amz-security-token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDCVRmWV1y5phjZiFDk1xKdQxEdW%2B%2BSmQ7DhlauTfoDvAIgHvyYiJwukfj9LGP39Ti6s9EKLoTr6q3jzpmDpAYfX58qlgQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAEGgwwMTIxNzcyNjQ1MTEiDDFrX6yB6rkfyQsepCrqAwMKa%2FyKYFFxq9Lm5T5JU4w51aBya2mONeGJ%2FfxP7VwboRfZMM%2BxUlTMUBA43BsgDmQJZbpPq%2FHZexkjq68aL6MJGuAkxX4iLvrummtR%2BBqhrzYINhK%2F8banqN4lbJ0ioXBSHXB8h7gfwEZCA04ulxEspwgZXgKEVc4ZJ1%2F9hC2nBcQieJO%2BHOsKa4Y0lZxx7BVpPgZ5Wagr1KagFf4CfCcfBaYNLV6Nb%2F8znCVgrcbyOSY2qMEPjsZh6dfkqqueUwX2mIGG7ZZQrC86Fc0QPrv0KSDBKKtbZbxZHoEYudWmZ%2F9q3AR8%2FFLhyfz0ZG7svO9o5xzR%2Fm9GMX3uw1Yxrh5amzaOaNBZIc5l5MKwWZcPSMngMJq%2B4BJZSSOad7hQ%2BH3qSY6HHa8dw3tv0F2dCW6X3fGY%2F8QAMbsxoJuuIoL9v6mHi6oByClEeFuw5FlRF9sxqoUI2a%2BQhDqcc4is6aUzLG9GxiC9Q7%2BkzU2DiT0Ls4nRz6U0kKjVQTbet0%2BVwjGf8dxJqHGZ1K9D75XKmczN66gDFU6O0Vo1Mr3idvJEWLSYSqmWCEbhlHaER%2FxoYvE%2FYyDsZ106LtsOpsfW8CKYLIQQyq4GkERF8zqdMF29MyZQugdFnbkap0OJkNYJM7vJhHPOnfjjMbIwtq7OzQY6pQFKBZXWDpYcEeJTS%2BsbZa%2F8vaDSWlUj1JaOK4WJKtt%2B%2F19HlagPRTHNG3eK%2FDxfFm1liUCz9kNw%2BeDfwTbVOPxgz93H4l%2FvJglcCrCuYId2rWpTT2iAYz4mcPbQT3Pjo%2Bv5jJIGeayp1KP4%2B5Ye3GsuTuYcAI8fvlwcup%2BiR1PsiQAG3KblQqQPS2nbVz7jIhUNcnR%2FQPEYFNTrIt3kJ%2FdfZZA7UB4%3D). Original citation identifier: `turn701804search37`.

<a id="ref-turn701804search40"></a>

54. [7. The 20th C and Measure Theory](https://www.ma.imperial.ac.uk/~bin06/talks/arsconjIV.pdf). Original citation identifier: `turn701804search40`.

<a id="ref-turn817174search1"></a>

55. [Henri Lebesgue (1875 - 1941) - Biography - MacTutor History of Mathematics](https://mathshistory.st-andrews.ac.uk/Biographies/Lebesgue/). Original citation identifier: `turn817174search1`.

<a id="ref-turn817174search26"></a>

56. [Henri Lebesgue and the Development of the Integral Concept*](https://old.maa.org/sites/default/files/images/upload_library/46/Barnett_TRIUMPHS_MiniPSPs/MiniPSP_Lebesgue_Integration_2023_01_01.pdf). Original citation identifier: `turn817174search26`.

<a id="ref-turn817174search0"></a>

57. [Jal Choksi - A history of the convergence theorems of (Lebesgue) integration](https://www2.cms.math.ca/Events/winter99/abstracts/node89.html). Original citation identifier: `turn817174search0`.

<a id="ref-turn477144search24"></a>

58. [Modes of Convergence](https://www-inst.cs.berkeley.edu/~ee126/sp24/notes/convergence.pdf). Original citation identifier: `turn477144search24`.

<a id="ref-turn477144search25"></a>

59. [Probability: Limit Theorems I](https://homepages.math.uic.edu/~itobasco/courses/NYU/LimitThms1.pdf). Original citation identifier: `turn477144search25`.

## Image Sources

- [01-01.img](assets/images/01-01.img); [Original source](https://www.quien.net/bernhard-riemann/)
- [02-01.img](assets/images/02-01.img); [Original source](https://snl.no/Henri_L%C3%A9on_Lebesgue?utm_source=chatgpt.com)
- [03-01.img](assets/images/03-01.img); [Original source](https://site.unibo.it/indam-bologna/en)
- [04-01.img](assets/images/04-01.img); [Original source](https://www.futura-sciences.com/sciences/personnalites/mathematiques-emile-borel-319/?utm_source=chatgpt.com)
- [05-01.img](assets/images/05-01.img); [Original source](https://snl.no/Henri_L%C3%A9on_Lebesgue?utm_source=chatgpt.com)
- [06-01.img](assets/images/06-01.img); [Original source](https://valeman.medium.com/andrey-kolmogorov-master-of-uncertainty-and-order-1080618e1afe)
- [07-01.img](assets/images/07-01.img); [Original source](https://commons.wikimedia.org/wiki/File%3APortrait_of_Robert_Brown_Wellcome_L0011784.jpg?utm_source=chatgpt.com)
- [08-01.img](assets/images/08-01.img), [08-02.img](assets/images/08-02.img), [08-03.img](assets/images/08-03.img), [08-04.img](assets/images/08-04.img), [08-05.img](assets/images/08-05.img), [08-06.img](assets/images/08-06.img), [08-07.img](assets/images/08-07.img); [Original source](https://masterymind.co.uk/study-guides/physics-ocr-gcse-brownian-motion); [Original source](https://web.mit.edu/course/10/10.50/www/diffuse2.html); [Original source](https://www.heurema.com/POFQ-Perrin.htm); [Original source](https://www.iitianacademy.com/cie-igcse-physics-0625-particle-model-study-notes/); [Original source](https://www.academia.edu/4000202/_Evident_atoms_visuality_in_Jean_Perrin_s_Brownian_motion_research_Studies_in_the_History_and_Philosophy_of_Science_39_2008_312_322); [Original source](https://www.slideserve.com/darrius/introduction-to-the-experiments-of-physics-407); [Original source](https://www.mvp.cufo.cz/materialy/9.html)
- [09-01.img](assets/images/09-01.img); [Original source](https://prints.royalsociety.org/collections/vintage-mathematics-prints-and-parabola-drawings/products/portrait-of-abraham-de-moivre-1667-1754-rs-9548?utm_source=chatgpt.com)
- [10-01.img](assets/images/10-01.img); [Original source](https://www.meisterdrucke.com/kunstdrucke/Sophie-Feytaud/1632777/Portr%C3%A4t-von-Pierre-Simon%2C-Marquis-de-Laplace-%281745-1827%29.html)
- [11-01.img](assets/images/11-01.img); [Original source](https://www.meisterdrucke.it/stampe-d-arte/Christian-Albrecht-Jensen/175614/Ritratto-di-Carl-Friedrich-Gauss%2C-1840.html)
- [12-01.img](assets/images/12-01.img); [Original source](https://www.sothebys.com/en/auctions/ecatalogue/2018/the-library-of-erwin-tomash-l18409/lot.58.html)
- [13-01.img](assets/images/13-01.img); [Original source](https://dun.unistra.fr/ipm/unit/bayesien/co/support_web.html)
- [14-01.img](assets/images/14-01.img); [Original source](https://www.talmudology.com/jeremybrownmdgmailcom/2021/2/15/happy-birthday-galileo)


## Chapter 7: Convergence and Countable Probability

- Émile Borel (1909), Les probabilités dénombrables et leurs applications arithmétiques, Rendiconti 27, 247–271. [Publication record](https://link.springer.com/article/10.1007/BF03019651).
- F. P. Cantelli (1917), Sulla probabilità come limite della frequenza. [Original academy catalog](https://operedigitali.lincei.it/rendicontiFMN/rol/visabs.php?fileId=5161&lang=it&type=mat).
- F. P. Cantelli (1935), Considérations sur la convergence dans le Calcul des probabilités, Annales IHP 5, 3–50. [Original text](https://www.numdam.org/item/AIHP_1935__5_1_3_0.pdf).
- Olav Kallenberg (2021), Foundations of Modern Probability, third edition. [Official book record](https://link.springer.com/book/10.1007/978-3-030-61871-1).


## Chapter 8: Constructing Infinite Random Experiments

- A. Kolmogoroff (1933), Grundbegriffe der Wahrscheinlichkeitsrechnung. [Publisher’s record and table of contents for the original book](https://link.springer.com/book/10.1007/978-3-642-49888-6). The original book’s year and table of contents were checked. The date of a modern online edition is not presented as its original publication date, and no claim is made to reproduce all of the original book’s proofs.
- P. J. Daniell (1919), Integrals in An Infinite Number of Dimensions, Annals of Mathematics 20(4), 281–288. [Original journal record](https://www.jstor.org/stable/1967122). Bibliographic information was checked; the chapter’s modern cylinder-set proof is not attributed to this paper as its original proof.
