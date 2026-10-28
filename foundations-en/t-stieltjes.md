# T-STIELTJES: Selecting a Measure from Local Mass Budgets

Chapter 19 needs a real-line selection lemma, not a general topology of random measures. Suppose positive Borel measures \(\mu_n\) have uniformly bounded mass on every compact interval. A subsequence and a locally finite positive Borel measure \(\mu\) then satisfy \(\int g\,d\mu_n\to\int g\,d\mu\) for every continuous compactly supported \(g\). We prove the needed result rather than treating Helly or Stieltjes as a black box.

<a id="t-stieltjes-selection"></a>

## Keeping interval masses in a monotone function

Put \(F_n(x)=\mu_n((0,x])\) for \(x\ge0\), and \(F_n(x)=-\mu_n((x,0])\) for \(x<0\). These functions are nondecreasing, right-continuous and uniformly bounded on each compact interval. Extract successively at rational points and diagonalize to obtain \(F_n(q)\to f(q)\) simultaneously for all rational \(q\). Define

\[
F(x)=\inf_{q\in\mathbb Q,\ q>x} f(q).
\]

This is finite, nondecreasing and right-continuous. To verify the last assertion, for any positive epsilon choose \(q>x\) with \(f(q)<F(x)+\varepsilon\); the bound persists as \(y\downarrow x\) with \(y<q\). At a continuity point \(x\) of \(F\), squeezing \(F_n(x)\) between rational bounds on both sides gives \(F_n(x)\to F(x)\). A monotone function has at most countably many jumps on a compact interval: jumps larger than \(1/m\) are finite in number, and one takes the union over integer intervals and \(m\).

## Constructing the Stieltjes measure without a representation theorem

Write the extended endpoint values \(a=F(-\infty)\), \(b=F(\infty)\). Use Lebesgue length on the level axis \((a,b)\) and, for \(u\in(a,b)\), define \(Q(u)=\inf\{x:F(x)\ge u\}\). The endpoints make this infimum finite, and right-continuity ensures that the level is reached at it. Moreover,

\[
\{u:Q(u)\le x\}=\{u\in(a,b):u\le F(x)\}.
\]

Thus \(Q\) is measurable. Push forward level-axis length by setting \(\mu(B)=\operatorname{Leb}\{u\in(a,b):Q(u)\in B\}\). Pushforward and nonnegative countable additivity directly give a Borel measure with

\[
\mu((c,d])=F(d)-F(c).
\]

Infinite endpoint values do not affect this formula on finite intervals. If \(a=b\), take the zero measure. Local finiteness of \(F\) makes the measure locally finite and sigma-finite. No Riesz representation theorem or later general theory of random measures is required.

## From intervals to continuous functions

At continuity points \(c,d\) of \(F\), increments give \(\mu_n((c,d])\to\mu((c,d])\). For continuous compactly supported \(g\), choose a fine partition with continuity-point endpoints on an interval containing its support. The difference of upper and lower step approximations is bounded by the uniform-continuity error of \(g\); their integral difference is controlled by the common local mass bound. Pass to the subsequence limit first, then let the mesh error vanish, proving convergence for the required test functions.

Chapter 19 only needs an extension to bounded, compactly supported Riemann-integrable test functions after the candidate limit has been identified as a constant multiple of Lebesgue length. Every interval endpoint is then a continuity point of the limiting measure. For any endpoint \(a\) and \(\varepsilon>0\), the established interval convergence gives \(\limsup_n\mu_n(\{a\})\le\lim_n\mu_n((a-\varepsilon,a+\varepsilon])=2c\varepsilon\). Let \(\varepsilon\downarrow0\); endpoint atoms vanish. Open or closed endpoints in the Riemann step bounds therefore do not affect the limit, and uniform local mass control completes the argument. No general-space Portmanteau theorem is asserted here.

## Extending a sigma-finite premeasure by finite pieces

First extend the finite-premeasure construction to a sigma-finite cover. Let a premeasure \(q\) on an algebra have an increasing algebra cover \(E_n\uparrow E\) with \(q(E_n)<\infty\). Put \(D_n=E_n\setminus E_{n-1}\), taking the initial preceding set empty. These are disjoint algebra sets. Each finite premeasure \(q_n(A)=q(A\cap D_n)\) extends by normalizing its nonzero mass and using Chapter 8's proved probability extension; use the zero measure for zero mass. This gives a finite measure \(\mu_n\) supported on \(D_n\).

Define \(\mu=\sum_n\mu_n\). Nonnegative countable summation gives a measure. For an algebra event \(A\), the premeasure's countable additivity on its disjoint decomposition yields \(q(A)=\sum_nq(A\cap D_n)=\mu(A)\), also when the value is infinite. Any other extension of \(q\) agrees with \(\mu\) on every finite restriction to \(E_n\) by pi–lambda uniqueness, then agrees on the whole space by monotone convergence along the cover. Thus a sigma-finite premeasure has a unique extension. The algebra cover is a hypothesis of this uniqueness statement, not something removable because total mass is infinite.

Selection supplies only a subsequence and a candidate measure. Identifying its form and normalizing its mass remain separate tasks, handled by Chapter 19's harmonic argument and cycle identity. Local convergence alone cannot prevent mass from escaping to infinity.
