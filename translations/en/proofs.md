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
