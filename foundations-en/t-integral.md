# Where Does Linearity of the Integral Come From?—Null Sets, Limits and Arbitrary Measure Spaces

Throughout, \((S,\mathcal F,\mu)\) is an arbitrary measure space: finiteness, σ-finiteness and completeness are not assumed. We start with the algebra of nonnegative simple integrals and then prove the limiting principles. This supplies an independent basis for splitting sums inside the integrals of Chapter 6.

<a id="t-integral-simple"></a>

## T-INTEGRAL.1 Simple functions and the nonnegative integral

For a finite-valued nonnegative simple function \(s=\sum_{j=1}^ra_j\mathbf1_{A_j}\), with disjoint \(A_j\) and \(a_j\ge0\), define \(I(s)=\sum_ja_j\mu(A_j)\), using \(0\cdot\infty=0\). Refine two representations by finite intersections to a common partition. Finite additivity makes the definition independent of representation. The same refinement proves nonnegative linearity and order preservation for simple functions; no infinite quantities are subtracted.

For measurable \(f:S\to[0,\infty]\), define \(I(f)=\sup\{I(s):0\le s\le f,\ s\text{ simple}\}\). Hence \(f\le g\) implies \(I(f)\le I(g)\), and \(I\) agrees with the simple integral. Every such \(f\) admits the following nonnegative simple approximation:

\[
s_n=2^{-n}\left\lfloor2^n\min(f,n)\right\rfloor,\qquad 0\le s_n\uparrow f.
\]

Each \(s_n\) has finitely many values and measurable level sets. Refining the dyadic grid and increasing the cap make the sequence nondecreasing. At finite values of \(f\), the error is eventually less than \(2^{-n}\); where \(f=\infty\), we have \(s_n=n\). This also proves the measurable simple-approximation tool used below.

<a id="t-integral-mct"></a>

## T-INTEGRAL.2 Monotone convergence without assuming general linearity

If \(0\le f_n\uparrow f\), order preservation gives \(L:=\lim_nI(f_n)\le I(f)\). Fix a simple \(0\le s\le f\) and \(0<c<1\), and let \(E_n=\{f_n\ge cs\}\). At every point where \(s>0\), the inequalities \(f_n\uparrow f\ge s>cs\) put the point in \(E_n\) eventually. Thus \(E_n\) increase and their union contains \(\{s>0\}\).

Write \(s\) as a finite sum over disjoint level sets. Continuity from below of the measure gives \(I(s\mathbf1_{E_n})\uparrow I(s)\). Since \(f_n\ge cs\mathbf1_{E_n}\), we have \(L\ge cI(s)\). If \(I(s)=\infty\), this already gives \(L=\infty\); otherwise let \(c\uparrow1\), then take the supremum over all \(s\). This proves \(L\ge I(f)\), and hence MCT on any measure space.

<a id="t-integral-linearity"></a>

## T-INTEGRAL.3 Nonnegative linearity, countable sums and zero integrals

For nonnegative measurable \(f,g\), take the approximations \(s_n\uparrow f\), \(t_n\uparrow g\). Simple-function linearity and the MCT just proved yield

\[
\int(f+g)\,d\mu=\lim_n\int(s_n+t_n)\,d\mu=\int f\,d\mu+\int g\,d\mu.
\]

Likewise, \(\int cf=c\int f\) for finite \(c>0\); at \(c=0\), use \(0\cdot\infty=0\). After finite sums, apply MCT to the partial sums to obtain the countable-sum formula for nonnegative functions. Pointwise finiteness of the series is not required; both sides may be \(\infty\).

\[
\int\sum_{n=1}^\infty f_n\,d\mu=\sum_{n=1}^\infty\int f_n\,d\mu,\qquad f_n\ge0.
\]

For \(f\ge0\), we have \(\int f=0\) if and only if \(f=0\) almost everywhere. Indeed, \(\mu\{f\ge1/k\}\le k\int f=0\), and a countable union gives \(\mu\{f>0\}=0\). Conversely, if \(f\) vanishes off a measurable null set, every simple minorant has null positive level sets, so its integral and their supremum are zero. This includes infinite values of \(f\) on the null set.

<a id="t-integral-null"></a>

## T-INTEGRAL.4 When are changes on null sets legitimate?

Let \(f,g\ge0\) be measurable and equal off a measurable null set \(N\). Split over \(N\) and \(N^c\); linearity and the preceding result give \(\int f=\int g\). Thus measurable changes on null sets do not affect the integral. **Both functions must be measurable**: in an incomplete space, an arbitrary subset of a null set need not be an event, nor its indicator measurable. See the full [completion construction](t-measure.md#t-measure-completion).

If measurable \(f_n\) have a limit off a measurable null set, first set every \(f_n\) to zero there, then take the limsup to obtain a measurable limit version. Measurability follows from the countable operations in \(\limsup f_n=\inf_m\sup_{n\ge m}f_n\). Almost-everywhere equality alone does not make an arbitrarily prescribed version measurable.

<a id="t-integral-signed"></a>

## T-INTEGRAL.5 Integrable real and complex functions

For real measurable \(f\) with \(\int|f|<\infty\), define \(\int f=\int f^+-\int f^-\). Both terms are finite, so subtraction is legitimate. Nonnegative linearity and the pointwise identity \((f+g)^++f^-+g^-=(f+g)^-+f^++g^+\) give real linearity after integration and rearrangement. The inequality \(|f+g|\le|f|+|g|\) first guarantees integrability of the sum.

The inequalities \(-|f|\le f\le|f|\) give \(|\int f|\le\int|f|\). Define a complex integral through real and imaginary parts. Choose a unit complex number \(z\) so that \(z\int f\) is nonnegative real, and integrate \(\operatorname{Re}(zf)\le|f|\) to obtain the complex triangle inequality. If the integral is zero, no direction is needed. Nonnegative extended integrals allow infinity, but signed integrals must never contain an undefined \(\infty-\infty\).

<a id="t-integral-dct"></a>

## T-INTEGRAL.6 Fatou and DCT: proofs without σ-finiteness

For nonnegative measurable \(f_n\), put \(g_m=\inf_{n\ge m}f_n\). Then \(g_m\uparrow\liminf_n f_n\), while \(\int g_m\le\inf_{n\ge m}\int f_n\). MCT gives Fatou’s lemma. If inequalities or convergence hold only almost everywhere, first change versions on the common measurable null set as above.

Now suppose \(f_n\to f\) almost everywhere, the real or complex functions \(f_n,f\) are measurable, and \(|f_n|\le g\) almost everywhere for every \(n\), where \(g\ge0\) and \(\int g<\infty\). The set where \(g=\infty\) is null. Unite it with the countably many exceptional sets and use zero versions there. Then \(|f|\le g\) and \(0\le|f_n-f|\le2g\) hold everywhere. Apply Fatou to the nonnegative functions \(2g-|f_n-f|\):

\[
2\int g\,d\mu\le\liminf_n\int(2g-|f_n-f|)\,d\mu=2\int g\,d\mu-\limsup_n\int|f_n-f|\,d\mu.
\]

Every integral being subtracted is finite. Hence \(\int|f_n-f|\to0\), and the integral triangle inequality gives \(\int f_n\to\int f\). This proves DCT together with \(L^1\) convergence. No finite-measure exhaustion of the whole space, topology or σ-finiteness has been used.

<a id="t-integral-support"></a>

## T-INTEGRAL.7 What can be exhausted is the effective support of the dominator

The intuition about tail control in Chapter 6 remains valid once its scope is stated correctly. For \(g\in L^1_+(\mu)\), put \(E_m=\{g\ge1/m\}\). A Markov-type estimate gives

\[
\mu(E_m)\le m\int g\,d\mu<\infty,\qquad E_m\uparrow\{g>0\},\qquad\int_{E_m^c}g\,d\mu\longrightarrow0.
\]

The last limit follows by applying MCT to \(g\mathbf1_{E_m}\) and subtracting from the finite integral \(\int g\). The sets \(E_m\) exhaust \(\{g>0\}\), not the entire possibly non-σ-finite space \(S\). For instance, counting measure on an uncountable set admits no countable finite-measure cover of the whole space. Nevertheless, every integrable dominator has the effective-support exhaustion above, and DCT still holds.

Equivalently, organize the control with the finite measure \(\nu(A)=\int_Ag\,d\mu\). The nonnegative countable-sum formula proves countable additivity of \(\nu\), and its total mass is \(\int g\). To control contributions of small sets, first choose \(M\) so that \(\int g\mathbf1_{\{g>M\}}<\varepsilon/2\), then use

\[
\int_Ag\,d\mu\le M\mu(A)+\int g\mathbf1_{\{g>M\}}\,d\mu.
\]

Choose \(\mu(A)<\varepsilon/(2M)\), taking \(M\) positive. This is absolute continuity of the integral with respect to the underlying measure. It comes from the tail of an integrable function, not from the entire space having finite volume. These null-set and integral foundations can now support extension in Chapter 8, densities in Chapter 10 and Gaussian smoothing in Chapter 11.
