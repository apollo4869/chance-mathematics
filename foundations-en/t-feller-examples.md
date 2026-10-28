# T-FELLER-EXAMPLES: Boundary Domains and Lévy Generators

## E.1 Two Actual Half-Line Semigroups

<a id="t-feller-boundary-domains"></a>

Let Hₜ be Gaussian convolution on the line. Extend f evenly, convolve and restrict to the half-line for reflection. Gaussian convolution preserves evenness, proving the semigroup law. The even extension is bounded uniformly continuous, so small Gaussian increments give strong continuity; vanishing at infinity is retained. The kernel is positive and has mass one.

For absorption retaining zero, extend f−f(0) oddly as v and set Tₜᵃf=f(0)+Hₜv. The extension is continuous and uniformly continuous. Hₜ preserves oddness, keeping the boundary value f(0); extending again gives Hₜv and proves the semigroup law. Expanding yields the chapter’s kernel: its density gₜ(y−x)−gₜ(y+x) is nonnegative for y>0, and the remaining mass 2Φ(−x/√t) sits at zero.

Uniform continuity of v proves strong continuity. For vanishing at infinity use the kernel: as x increases, both the probability of landing in a fixed compact interval and the probability of hitting zero vanish; f is small outside. Both semigroups are positive, conservative and strongly continuous on the same C₀([0,∞)). For f=e⁻ˣ² the mean from zero is always one under absorption, but (1+2t)⁻¹ᐟ² under reflection, so they differ.

## E.2 The Laplace Heat Kernel and Entire Resolvent Ranges

Put κ=√(2λ). First the Laplace heat integral H(x) equals e⁻κ|x|/κ. For x>0, the heat equation and integration by parts give H″=2λH; differentiation away from zero is dominated by Gaussian small-time decay and exponential large-time discount. H vanishes at infinity by dominated convergence using gₜ(0), while H(0)=1/κ by the Gaussian integral. The constant-coefficient ODE gives the result, with evenness handling x<0.

\[
\int_0^\infty e^{-\lambda t}g_t(x)\,dt=\frac{e^{-\kappa|x|}}{\kappa},\qquad r_\lambda^{D/R}(x,y)=\frac{e^{-\kappa|x-y|}\mp e^{-\kappa(x+y)}}{\kappa}.
\]

Integrate the chapter’s kernels in time using bounded Fubini. Reflection gives the integral with rᴿ. Absorption has the Laplace transform of the boundary mass as well. For x>0 the first-hitting density is xgₜ(x)/t, obtained by differentiating Chapter 26’s reflection formula. Its Laplace transform is −H′(x)=e⁻κx, so the boundary term is f(0)e⁻κx/λ. At x=0 use the preserved boundary value directly.

\[
R_\lambda^r f(x)=\int_0^\infty r_\lambda^R(x,y)f(y)\,dy,\qquad R_\lambda^a f(x)=\int_0^\infty r_\lambda^D(x,y)f(y)\,dy+\frac{f(0)}\lambda e^{-\kappa x}.
\]

Split the integral at y=x and differentiate each part. Endpoint terms cancel on the first derivative and leave −2f(x) on the second, giving u″=2λu−2f. The explicit kernels give u∈C₀; the equation gives u″∈C₀ and continuous one-sided derivatives. The reflecting kernel has derivative zero at x=0. The Dirichlet kernel vanishes there; the added term gives u(0)=f(0)/λ, hence u″(0)=0.

Conversely take u in either candidate domain in the chapter and set f=λu−u″/2. It belongs to C₀; in the absorbing case u″(0)=0 gives f(0)=λu(0). Subtract the corresponding resolvent solution. The difference w lies in C₀, satisfies w″=2λw and the same boundary condition. Its general form ce⁻κx+deκx has d=0 by vanishing at infinity, then c=0 by either boundary condition. Thus u lies in the resolvent range. The range-domain identity in T-OPERATORS proves the exact domains.

## E.3 A Dense Common Test Domain That Is Not a Core

Let D₀ consist of smooth compactly supported half-line functions constant near zero. It is uniformly dense: flatten a C₀ function near zero using continuity, cut it off far away, and smooth the intermediate part. It belongs to both domains and both generators agree on it.

For reflection every D₀ element has Af(0)=0, retained by graph convergence, while f=e⁻ˣ² has Aᵣf(0)=−1. For absorption every D₀ element has f′(0)=0, and the derivative trace is also graph-continuous by the following Taylor bound. The function xe⁻ˣ² belongs to the absorbing domain but has derivative one, so cannot be graph-approximated.

\[
|u^{\prime}(0)|\le |u(1)-u(0)|+\int_0^1(1-s)|u^{\prime\prime}(s)|\,ds\le2\|u\|_\infty+\tfrac12\|u^{\prime\prime}\|_\infty.
\]

Thus supremum-norm density does not determine boundary behavior. Killing at zero instead requires a suitable space such as C₀((0,∞)) with its Dirichlet interpretation. Allowing arbitrary f(0) on full C₀([0,∞)) while killing immediately from zero would destroy strong continuity there.

## E.4 Generators of Truncated Lévy Motions

<a id="t-feller-levy-generator"></a>

First compute in Chapter 27’s constructed Gaussian–Poisson model and truncate at ε<1; the jump notation below refers to that model. Any Lévy process with the same triplet has the same transition semigroup by the marginal characteristic-function uniqueness in Chapter 27, without an original-space decomposition. Remove compensated jumps of size at most ε; the rest is Gaussian motion, drift and a finite compound Poisson sum. Restrict ν to |y|>ε and use the following drift. Its integral is finite for each ε; it must not be treated as a separately convergent drift as ε decreases.

\[
b_\varepsilon=b-\int_{\varepsilon<|y|\le1}y\,\nu(dy),\qquad X_t^\varepsilon=b_\varepsilon t+Q^{1/2}B_t+\sum_{s\le t,\ |\Delta X_s|>\varepsilon}\Delta X_s.
\]

For smooth compactly supported f, uniform Taylor expansion of translation gives bε·∇f. Gaussian second-order Taylor gives one half of covariance contracted with the Hessian: after scaling the increment by √t its law is fixed, the bounded third-order remainder has mean O(t³ᐟ²), and the linear term has mean zero. In the compound Poisson series, zero and one jumps give the integral of f(x+y)−f(x); two or more jumps have probability O(t²), with payoff error bounded by 2‖f‖.

The three independent convolution operators commute. Split the product difference into three pieces and use strong continuity with the uniform derivatives to obtain Lε. Combine the drift with the intermediate-jump first-order term to get the next expression.

\[
L_\varepsilon f=b\cdot\nabla f+\tfrac12\operatorname{tr}(Q\nabla^2f)+\int_{|y|>\varepsilon}[f(\cdot+y)-f-\mathbf1_{\{|y|\le1\}}y\cdot\nabla f]\,\nu(dy).
\]

## E.5 The Small-Jump Limit Gives Actual Domain Membership

Here the Hessian norm is the supremum of its matrix operator norm. Small-jump second-order Taylor and finite large-jump mass make Lf absolutely integrable and in C₀. For continuity use dominated convergence with the Hessian norm times |y|² for small jumps and 2‖f‖ for large jumps. As the starting point goes to infinity every fixed-y term vanishes, and the same bounds prove vanishing at infinity. They also give the uniform error estimate.

\[
\|L_\varepsilon f-Lf\|_\infty\le\tfrac12\|\nabla^2 f\|_\infty\int_{|y|\le\varepsilon}|y|^2\nu(dy)\longrightarrow0.
\]

Chapter 27’s compensated construction gives the following L² maximal bound, summing coordinate estimates in dimension d. Only the small-jump construction and orthogonality are used, not stable classifications, general attraction domains or independently unfinalized original-space decomposition results.

\[
E\sup_{s\le T}|X_s-X_s^\varepsilon|^2\le4T\int_{|y|\le\varepsilon}|y|^2\nu(dy).
\]

Consequently for every g in C₀ the common displacement coupling and uniform continuity give supₛ≤T‖Tₛεg−Tₛg‖→0. On displacement difference ≤δ use the modulus; on its complement use Chebyshev and 2‖g‖. Let ε decrease first, then δ. The truncated generator gives Tₜεf−f=∫TₛεLεf. Replace Lεf by Lf and then the semigroup; the preceding errors times T tend to zero. Thus Tₜf−f=∫TₛLf. Divide by t and use strong continuity for Lf∈C₀ to prove f∈D(A), Af=Lf.

This proves domain membership and the formula on the stated tests, without an additional unproved assertion that they form a core for all Lévy generators. Changing truncation also changes the drift parameter; the subtraction in the integral cannot be altered while retaining the same b.
