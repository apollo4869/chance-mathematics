# Why Can a Generating Class Determine an Entire Measurable World?

Starting with the measurable sets of Chapter 5, this companion develops the extension tools needed for product integration, infinite experiments and probability kernels. The proofs use set operations, countable additivity and limits of real numbers; they do not assume the integration identities they will later justify.

<a id="t-mclass-pi-lambda"></a>

## T-MCLASS.1 From rectangles or cylinders to all events

Let \(\Omega\) be a set. A class \(\mathcal P\) closed under finite intersections is a \(\pi\)-system; the empty set is allowed. A class \(\mathcal D\) containing \(\Omega\) and closed under complements and countable disjoint unions is a \(\lambda\)-system. This is weaker than being a \(\sigma\)-algebra: unions with overlapping members are not yet available.

First note that if \(A\subseteq B\) and both belong to \(\mathcal D\), then \(B\setminus A\in\mathcal D\): unite the disjoint sets \(B^c\) and \(A\), then take a complement. Consequently, if \(A_n\uparrow A\), the differences \(A_n\setminus A_{n-1}\) belong to \(\mathcal D\), and their disjoint union gives \(A\in\mathcal D\).

**The π–λ theorem.** Every \(\lambda\)-system containing a \(\pi\)-system \(\mathcal P\) contains \(\sigma(\mathcal P)\).

Intersect all \(\lambda\)-systems containing \(\mathcal P\), and call the intersection \(\mathcal L\). It again has these three closure properties. We will transfer the missing intersection operation from \(\mathcal P\) to all of \(\mathcal L\). We may first adjoin \(\Omega\) to \(\mathcal P\); this changes neither its generated \(\sigma\)-algebra nor closure under intersections.

Fix \(A\in\mathcal P\), and let \(\mathcal L_A=\{B:A\cap B\in\mathcal L\}\). It contains the whole space. Complements are handled by \(A\cap B^c=A\setminus(A\cap B)\) and the nested-difference property; intersections with disjoint unions remain disjoint. Thus it is a \(\lambda\)-system. It contains \(\mathcal P\), so \(\mathcal L\subseteq\mathcal L_A\). Intersections are now allowed when one member is in \(\mathcal P\) and the other in \(\mathcal L\).

Now fix \(B\in\mathcal L\) and make the same check for \(\{A:A\cap B\in\mathcal L\}\). The preceding paragraph shows that this \(\lambda\)-system contains \(\mathcal P\), hence contains \(\mathcal L\). Both members may now lie in \(\mathcal L\). Consequently \(\mathcal L\) is closed under intersections, complements and finite unions. Disjointifying an arbitrary countable union makes it a countable disjoint union. Thus \(\mathcal L\) is a \(\sigma\)-algebra and contains \(\sigma(\mathcal P)\), as required.

<a id="t-mclass-set"></a>

## T-MCLASS.2 Set monotone classes: how limits supply a σ-algebra

A monotone class is closed under increasing countable unions and decreasing countable intersections. **The set monotone class theorem** states that the smallest monotone class containing an algebra \(\mathcal A\) is \(\sigma(\mathcal A)\). An algebra contains the whole space and is closed under complements and finite unions. Merely containing a \(\pi\)-system is not this theorem’s hypothesis.

Write the smallest monotone class as \(\mathcal M\). The class \(\{E:E^c\in\mathcal M\}\) is a monotone class containing \(\mathcal A\), so \(\mathcal M\) is closed under complements. For fixed \(A\in\mathcal A\), the class \(\{E:A\cap E\in\mathcal M\}\) is a monotone class containing \(\mathcal A\), hence containing \(\mathcal M\). Fixing \(E\in\mathcal M\) and repeating extends the other argument from \(\mathcal A\) to \(\mathcal M\). Thus \(\mathcal M\) is closed under intersections, complements and finite unions.

The finite unions of any sequence \(E_n\in\mathcal M\) increase to its countable union, which therefore belongs to \(\mathcal M\). Hence \(\mathcal M\) is a \(\sigma\)-algebra containing \(\sigma(\mathcal A)\). The reverse inclusion holds because every \(\sigma\)-algebra is itself a monotone class.

<a id="t-mclass-function"></a>

## T-MCLASS.3 Functional monotone classes: from indicators to bounded observations

Let \(\mathcal H\) be a vector space of bounded real functions containing the constant 1. Assume that whenever \(f_n\in\mathcal H\) are uniformly bounded and increase pointwise to \(f\), then \(f\in\mathcal H\). If it contains the indicators of a \(\pi\)-system \(\mathcal P\), then it contains every bounded real \(\sigma(\mathcal P)\)-measurable function.

Put \(\mathcal D=\{A:\mathbf1_A\in\mathcal H\}\). The constant 1 and the vector-space property handle the whole space and complements. An indicator of a disjoint union is the bounded increasing limit of the finite partial sums of its indicators. Thus \(\mathcal D\) is a \(\lambda\)-system containing \(\mathcal P\), and the π–λ theorem supplies every generated event. Approximate a nonnegative bounded measurable function by increasing bounded simple functions; add a sufficiently large constant to treat any bounded real function. Every step stays in \(\mathcal H\). Treat real and imaginary parts separately for complex functions.

There is also an algebra version: if \(\mathcal H\) contains an algebra \(\mathcal A\) of bounded real functions, including 1 and closed under multiplication, it contains all bounded \(\sigma(\mathcal A)\)-measurable functions. The passage from a function algebra to indicators requires a proof.

First, \(\mathcal H\) is closed under uniform limits. If \(f_n\in\mathcal H\) converge uniformly to \(f\), take a subsequence with \(\|f_n-f\|_\infty\le4^{-n}\), put \(d_n=2\cdot4^{-n}\) and \(r_n=\sum_{k\ge n}d_k\). Since \(\|f_{n+1}-f_n\|_\infty\le d_n\), the functions \(f_n-r_n\) are uniformly bounded, increase pointwise and converge to \(f\). Thus \(f\in\mathcal H\).

For a continuous function \(u\) on \([0,1]\), the Bernstein polynomial \(B_nu(x)=\sum_{k=0}^nu(k/n)\binom nk x^k(1-x)^{n-k}\) converges uniformly to \(u\). Indeed, if \(K\) has the binomial distribution with parameters \((n,x)\), this polynomial is \(\mathbb Eu(K/n)\), and \(\operatorname{Var}(K/n)\le1/(4n)\). Split according to \(|K/n-x|\le\delta\) and its complement, and use uniform continuity and Chebyshev’s inequality:

\[
\sup_{0\le x\le1}|B_nu(x)-u(x)|\le\omega_u(\delta)+\frac{2\|u\|_\infty}{4n\delta^2}.
\]

Let \(n\to\infty\), then \(\delta\downarrow0\). An affine change of variables gives the same result on any compact interval. Thus for \(f\in\mathcal A\) and continuous \(u\) on its range, polynomial approximation yields \(u(f)\in\mathcal H\). For finitely many \(f_i\in\mathcal A\), a product of continuous functions of these variables is uniformly approximated by products of polynomial approximations to the respective functions. Those products lie in \(\mathcal A\), so their limit lies in \(\mathcal H\).

Take the continuous ramps \(u_{i,k}(x)=\min(1,k(x-a_i)_+)\). The product \(\prod_i u_{i,k}(f_i)\) increases to \(\mathbf1_{\cap_i\{f_i>a_i\}}\), so all such intersection indicators lie in \(\mathcal H\). These finite intersections form a \(\pi\)-system generating \(\sigma(\mathcal A)\). Apply the indicator version already proved. This makes the passage to all measurable functions explicit.

<a id="t-mclass-uniqueness"></a>

## T-MCLASS.4 Measure uniqueness and its finiteness boundary

Let \(\mu,\nu\) be finite measures on the same measurable space, with equal total mass, agreeing on a \(\pi\)-system generating the \(\sigma\)-algebra \(\mathcal P\). Then \(\mu=\nu\). Indeed, \(\mathcal D=\{A:\mu(A)=\nu(A)\}\) contains the whole space. Complements use subtraction from the equal finite total masses, and disjoint unions use countable additivity. Thus \(\mathcal D\) is a \(\lambda\)-system, and the theorem applies.

The σ-finite version needs a common finite cover: sets \(E_n\in\mathcal P\) with \(\bigcup_nE_n=\Omega\) and \(\mu(E_n)=\nu(E_n)<\infty\). Fix \(n\). The finite measures \(A\mapsto\mu(A\cap E_n)\) and its \(\nu\) counterpart agree on \(\mathcal P\), hence on the whole generated \(\sigma\)-algebra. Put \(D_n=E_n\setminus\bigcup_{j<n}E_j\). These sets are measurable and disjoint. Equality on each \(D_n\), followed by countable summation, proves equality on every event.

Without finiteness, equal generating readings need not determine a measure. On the real line, counting measure and the measure assigning \(\infty\) to every nonempty set both assign \(\infty\) to every nonempty open interval with rational endpoints, yet assign 1 and \(\infty\) to a singleton. Adjoin the empty set to these intervals to obtain a generating Borel \(\pi\)-system. Subtracting \(\infty-\infty\) cannot replace the finite-measure complement argument.

<a id="t-mclass-applications"></a>

## T-MCLASS.5 The applications actually needed in this book

A probability on the real line is determined by the probabilities of \(( -\infty,q]\), \(q\in\mathbb Q\). These half-lines together with the whole space form a \(\pi\)-system; rational thresholds approximate any real threshold from above, and the half-lines generate the Borel sets. This is the set-theoretic basis of distribution-function uniqueness. Chapter 11 first recovers the half-line probabilities by continuous ramps, then recovers the entire law by this result.

Product rectangles and finite-coordinate cylinders are also closed under finite intersections. Probabilities agreeing on all cylinders agree on the product \(\sigma\)-algebra they generate, even for an uncountable index set. This does not make arbitrary path subsets measurable. For uniqueness of σ-finite product measures, first use the common countable cover by finite-measure rectangles; the localization in the preceding section cannot be omitted.

For a probability kernel in Chapter 10, one checks that the event class having the desired property is a \(\lambda\)-system, then extends from rectangles. A property valid separately at each state does not by itself settle a common exceptional null set for uncountably many states. Countable determining classes and version choices still require their own argument.

Related foundations: [integration, null sets and DCT](t-integral.md#t-integral-dct); [completion and Borel coding](t-measure.md#t-measure-completion).
