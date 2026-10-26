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
