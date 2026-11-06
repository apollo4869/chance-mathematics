# Chapter 32: Why Must the Familiar Calculus Change? — Itô Formula, Stratonovich and First SDEs

Replacing position by its square has already left us a contribution of time that does not disappear. Replace the square by a cube. What would finite sums miss if we only multiplied the derivative by changes in position? The algebra of a cube is exact enough to inspect each term before guessing an answer.

What needs to change is how a chain rule is used along a rough random path. Classical calculus remains correct under its hypotheses. We must identify the regularity that made errors disappear, and the accumulation retained by stochastic integration.

## 32.1 A Cube Leaves Two Different Remainders

<a id="ito-cubic-discovery"></a>

Let B start at zero. Retain Chapter 31’s filtration under the usual conditions, with B Brownian relative to it. Take a deterministic partition of [0,t] and write ΔᵢB for one increment. Subtracting cubes gives the following finite identity, without a general change-of-variable formula.

\[ B_t^3=3\sum_i B_{t_i}^2\Delta_iB+3\sum_i B_{t_i}(\Delta_iB)^2+\sum_i(\Delta_iB)^3. \]

The first term has the shape of Chapter 31’s left-endpoint integral sums. The third might disappear, but small individual terms are not enough when their number grows. The useful bound places the cubic sum under the largest increment times the quadratic sum.

\[ \left|\sum_i(\Delta_iB)^3\right|\le\max_i|\Delta_iB|\sum_i(\Delta_iB)^2\longrightarrow0\quad\text{in probability}. \]

Continuity sends the largest increment to zero; the quadratic sum converges in probability to t and is therefore tight. Together these facts eliminate the cubic term. The second term has no such reason to vanish: position weights quadratic variation that survives. Compared with the square, there is a new difficulty: how do weighted quadratic sums become integrals?

## 32.2 What Made Errors Vanish in the Classical Chain Rule

First examine an object for which the classical rule applies. If x is a continuous finite-variation path and f is C¹, uniform continuity of f′ on the compact range bounds the total first-order remainder by the expression below. It vanishes, yielding the classical Riemann–Stieltjes chain rule.

\[ \sum_i|r_i|\le\omega_{f'}\!\left(\max_i|\Delta_ix|\right)\operatorname{Var}(x)_{[0,t]}\longrightarrow0. \]

Brownian paths do not satisfy this finite-variation hypothesis, as established in Chapter 31. An infinite total variation cannot be treated as a fixed constant in that estimate. Meanwhile their quadratic sums have finite nonzero limits. This suggests retaining a second-order expansion, not declaring Taylor theory invalid.

Nor does surviving quadratic variation mean that every squared random increment equals its time interval. Such equality arises only through specified sums and limits. Differential notation below abbreviates integral identities; it does not prescribe algebra for individual random numbers.

## 32.3 From Total Quadratic Growth to Weighted Growth

<a id="ito-weighted-variation"></a>

Let M be a continuous local martingale starting at zero, with A=[M]=⟨M⟩. Chapter 31 gives ucp convergence of quadratic sums along deterministic vanishing meshes, without nesting. For a continuous random weight g we need the following result, including the unfinished cell up to t. Its right side is a pathwise Stieltjes integral against continuous increasing A.

\[ \sum_i g_{t_i}(M_{t\wedge t_{i+1}}-M_{t\wedge t_i})^2\xrightarrow{\mathrm{ucp}}\int_0^t g_s\,dA_s. \]

Continuity of the weight does not permit termwise multiplication of an unweighted limit. First remove the unfinished cell, with error bounded by squared path oscillation; the remainder is increasing. Approximate g on a fixed coarse grid. On that grid the uniform unweighted error is added only finitely many times. The weight approximation costs its oscillation times the two total masses. Refine the original grid first, then the coarse grid, to obtain the result.

The mechanism is stability of continuous weights under controlled total mass, not a new independence assumption. Full estimates and the polarized cross version are in [companion Section 1](../foundations/t-ito-formula.md#t-ito-weighted). Apply it to g=B, pass the first term by Chapter 31’s isometry and localization, and the cubic calculation closes.

\[ B_t^3=3\int_0^t B_s^2\,dB_s+3\int_0^t B_s\,ds. \]

## 32.4 Controlling Remainders with Only Two Continuous Derivatives

<a id="ito-taylor-remainder"></a>

A cubic expansion is exact but does not cover general functions. Take f∈C²(R). On a compact interval, Taylor’s integral remainder has the exact form below. The relevant quantity is oscillation of the second derivative, not a potentially nonexistent bound on a third derivative.

\[ f(x+h)-f(x)=f'(x)h+\frac12f''(x)h^2+r(x,h),\qquad r(x,h)=h^2\int_0^1(1-u)\{f''(x+uh)-f''(x)\}\,du. \]

Thus the sum of absolute remainders is at most half the modulus of continuity of f′′ at the largest path increment, multiplied by the quadratic sum. The increment vanishes and the sum is tight, so the product vanishes in probability. This explains why the second-order term survives while the remainder does not: their controls differ.

\[ \sum_i|r_i|\le\frac12\omega_{f''}(\omega_B(|\pi|))\sum_i(\Delta_iB)^2\longrightarrow0\quad\text{in probability}. \]

Compact intervals cannot silently stand in for the entire sample space. Stop before the path exits a fixed bound, making derivatives bounded. Chapter 31’s stopping identity makes these proofs consistent as the bound is removed. The function and its derivatives need not be globally bounded.

## 32.5 The General Formula Has Now Been Forced by Finite Sums

<a id="ito-brownian-formula"></a>

Now pass each term to its limit: the first-order sums become predictable integrals by isometry; the second-order sums become time integrals by weighted quadratic variation; the remainder vanishes by the preceding section. For every f∈C²(R) we obtain the Brownian Itô formula.

\[ f(B_t)=f(B_0)+\int_0^t f'(B_s)\,dB_s+\frac12\int_0^t f''(B_s)\,ds. \]

A complete statement also needs process versions. Every term has a continuous version, and the finite-sum error tends to zero ucp on compact intervals. Equality therefore holds for all t outside one null set. Approximation along general meshes is still only asserted ucp, not automatically pathwise. The first term converges in L² maximal norm after localization, becoming local ucp when bounds are removed.

The square and cube are now two checks of one mechanism. The second derivative is not an accidental correction: it is the Taylor coefficient multiplied by nonvanishing quadratic variation. The factor 1/2 comes from the same expansion, not an extra rule attached to noise.

## 32.6 A Path with Both Drift and Martingale Fluctuation

<a id="ito-continuous-semimartingale"></a>

Brownian time is t, but Chapter 31 supplies random clocks for general continuous martingales. A path may also contain finite-variation accumulation. Introduce precisely the object needed here: a continuous adapted X with the decomposition below is a continuous semimartingale in this chapter; M is a continuous local martingale starting at zero, V is continuous adapted locally finite variation starting at zero, and X₀ is finite and F₀-measurable.

\[ X_t=X_0+M_t+V_t,\qquad \int_0^t H_s\,dX_s:=\int_0^t H_s\,dM_s+\int_0^t H_s\,dV_s. \]

For continuous adapted H, compact-time pathwise boundedness makes both integrals available: local square energy controls the first, and pathwise Stieltjes integration the second. More general predictable H must separately satisfy local finiteness of ∫H²d[M] and ∫|H|dVar(V), rather than one vague integrability condition. Coefficients arising from the smooth functions used here are continuous and adapted.

The decomposition is unambiguous: the difference of its martingale parts is a continuous finite-variation local martingale, hence zero by Chapter 31. Squares of V increments vanish; their cross sums with M vanish by Cauchy–Schwarz. Thus [X]=[M]. Linear finite-variation accumulation enters the first-order term without a new second-order correction.

## 32.7 Giving the Same Proof to a Random Clock

<a id="ito-continuous-formula"></a>

For this X and every f∈C²(R), the Taylor argument is unchanged, except that weighted quadratic sums now integrate against [M]. Every equality remains an indistinguishable identity between continuous process versions.

\[ f(X_t)=f(X_0)+\int_0^t f'(X_s)\,dM_s+\int_0^t f'(X_s)\,dV_s+\frac12\int_0^t f''(X_s)\,d[M]_s. \]

The first-order martingale term uses random-clock isometry; the finite-variation term uses uniform pathwise approximation; the second-order term uses Section 3; the remainder uses path oscillation times tight quadratic sums. A general continuous martingale clock cannot first be assumed to have the form σ²dt, as Chapter 31’s Cantor example already shows.

When M=0, the formula restores the classical chain rule for continuous finite-variation paths. When V=0 and [M]=t, it has the Brownian form just proved. We have not yet inferred that M must be Brownian from [M]=t; identifying the entire process requires another theorem.

## 32.8 What Localization Actually Protects

Saying only “obvious after localization” hides integrability. Fix T. On the F₀ event {|X₀|≤R}, stop when |M| or Var(V) reaches R. The stopped martingale is bounded with E[M]ₜ≤R²; V has bounded total variation and X stays in a fixed compact set. Outside the initial event stop at zero and multiply integrands by its indicator, then increase R.

For Hⁿ=f′ at left grid values of X, energy error is controlled by uniform path error. On the stopped interval derivatives are bounded and the terminal bracket is integrable, so dominated convergence and Doob give L² maximal convergence. The remaining terms use their finite path measures. Common null sets, weighted cross sums and C¹,² time expansions are detailed in the [companion proof](../foundations/t-ito-formula.md#t-ito-general).

\[ E\sup_{t\le T}\left|\int_0^t(H_s^n-H_s)\,dM_s\right|^2\le4E\int_0^T|H_s^n-H_s|^2\,d[M]_s\longrightarrow0. \]

Remove stopping in the order mesh first, R second. The general conclusion is ucp, not an unproved L² or almost sure convergence. Chapter 31 makes the stopped identities consistent, so the local formulas really assemble into a formula for the original process.

## 32.9 What a Product Remembers of Two Changing Coordinates

<a id="ito-product"></a>

Let X and Y be continuous semimartingales. Knowing each quadratic variation does not yet determine the calculus of XY. Finite multiplication leaves a cross term whose accumulated limit is Chapter 31’s covariation. Start with finite algebra, then pass to the established integrals and ucp limits.

\[ \Delta_i(XY)=X_{t_i}\Delta_iY+Y_{t_i}\Delta_iX+\Delta_iX\Delta_iY,\qquad X_tY_t=X_0Y_0+\int_0^t X_s\,dY_s+\int_0^t Y_s\,dX_s+[X,Y]_t. \]

If X and Y are both B, then [X,Y]=t. For independent Brownian coordinates the cross bracket is zero. Individual variances can agree while product drifts differ. The correction records shared fluctuation structure, not merely two separate fluctuation intensities.

Thus d[X,Y] in differential notation has a precise source: it abbreviates this integral identity. A finite-variation coordinate has zero cross variation with any continuous semimartingale, restoring the classical product rule in that case.

## 32.10 How the Hessian Reads Shared Fluctuations

<a id="ito-multidimensional"></a>

For a d-dimensional continuous semimartingale X, decompose each coordinate as X₀+M+V. A second-order Taylor expansion contains every pair of increments, so curvature must be paired with the full covariation matrix. Suppose F is C¹ in time and C² in space, with all these derivatives jointly continuous: F∈C¹,². The time-space formula is

\[ \begin{aligned}F(t,X_t)-F(0,X_0)={}&\int_0^t F_t(s,X_s)\,ds+\sum_{i=1}^d\int_0^t F_{x_i}(s,X_s)\,dX_s^i\\&+\frac12\sum_{i,j=1}^d\int_0^t F_{x_ix_j}(s,X_s)\,d[M^i,M^j]_s.\end{aligned} \]

The proof does not secretly demand two time derivatives. In each cell, first take the time difference at its final spatial position and integrate Fₜ by the fundamental theorem of calculus. Then expand in space at the left time. Uniform continuity of Fₜ and oscillation of X control the time error; the Hessian modulus times Σ|ΔX|² controls the spatial remainder. Diagonal and off-diagonal sums use weighted convergence and polarization.

Each covariation is a signed locally finite-variation measure, without a required dt density. Coordinate quadratic sums bound the absolute cross sums, so the same localization suffices. Only when a representation M=∫σdW is given does the matrix clock become a=σσᵀ times dt. This is not a hypothesis of the general formula.

## 32.11 Another Integral Convention for the Same Cross Term

<a id="ito-stratonovich"></a>

The product formula makes another way of accumulating terms worth studying. Averaging the two endpoint values in each cell gives exactly the left sum plus half the cross-increment sum. For continuous semimartingales H and X both limits already exist, defining the Stratonovich integral. The convergence below is ucp.

\[ \sum_i\frac{H_{t_i}+H_{t_{i+1}}}{2}\Delta_iX\longrightarrow\int_0^t H_s\circ dX_s:=\int_0^t H_s\,dX_s+\frac12[H,X]_t. \]

When t is not a grid point, use t as the right endpoint of its unfinished cell. This specifies the full process limit. Quadratic variation has not changed: half the shared fluctuation is absorbed into a new integral notation. Taking H=X gives precisely \(\int_0^t X_s\circ dX_s=(X_t^2-X_0^2)/2\), without requiring a zero initial value; for different coordinates the product rule also has its familiar shape.

\[ d(XY)=X\circ dY+Y\circ dX. \]

This does not turn future information into a legal Itô trading rule. The Stratonovich integral is defined by a different limit and an identified finite-variation correction; it generally does not preserve the martingale property of Itô integration. They can be converted, but an equation cannot simply switch integral symbols while retaining every other term.

## 32.12 The Domain Needed to Restore a Chain Rule

<a id="ito-stratonovich-domain"></a>

If f∈C³, the Itô formula just proved makes f′(X) a continuous semimartingale, so the preceding definition applies immediately. But Itô formula only requires C². It is not legitimate to assume that the derivative of every C² function, applied to a semimartingale, is still a semimartingale. To retain the C² range, examine the needed cross sums directly.

For a spatial C¹ function g, its first-order Taylor error is bounded by \(\omega_{g'}(|\Delta X|)|\Delta X|\). Multiplying by ΔX and summing again removes the error through oscillation times quadratic sums. Thus the cross-sum limit [g(X),X] exists and equals ∫g′(X)d[X]. Endpoint-symmetric sums have a limit even without first asserting that g(X) is a semimartingale. We use the same notation on this explicitly proved extension domain.

\[ [g(X),X]_t=\int_0^t g'(X_s)\,d[X]_s,\qquad f(X_t)-f(X_0)=\int_0^t f'(X_s)\circ dX_s,\quad f\in C^2. \]

The multidimensional and time-dependent statements are proved in [companion Section 4](../foundations/t-ito-formula.md#t-ito-stratonovich), including the fact that C¹,² does not supply mixed time derivatives. Restoring the classical shape does not remove the Hessian: it is placed precisely inside covariation of the integrand and integrator.

## 32.13 A Time Midpoint Need Not Halve Quadratic Growth

<a id="ito-midpoint-clock"></a>

“Midpoint” can mean averaging H’s two endpoint values or reading H at the temporal midpoint. The former is the definition above. For a general continuous semimartingale the latter need not give the same integral. Chapter 31’s singular clock makes the distinction exactly calculable.

Use the Cantor ternary coding again, now with left-child probability p∈(0,1), right-child probability 1−p, and p≠1/2. Write cₚ for its atomless CDF and Mₜ=\(B_{c_p(t)}\), with the corresponding usual time-changed filtration. Chapter 31’s deterministic-clock construction gives its bracket cₚ; the question now concerns the two portions of clock mass within one interval.

Partition [0,1] into 3ⁿ equal cells and let uᵢ be each temporal midpoint. An active cell has clock mass qᵢ. Its midpoint lies in the deleted middle third, so the first half has already received pqᵢ and the second receives (1−p)qᵢ. Write the two martingale increments as aᵢ,bᵢ. The temporal-midpoint sum minus the left sum is exactly Σ(aᵢ²+aᵢbᵢ).

\[ E\sum_i(a_i^2+a_ib_i)=p,\qquad \operatorname{Var}\!\left(\sum_i(a_i^2+a_ib_i)\right)=\sum_i\{2p^2q_i^2+p(1-p)q_i^2\}\le2\max_iq_i\longrightarrow0. \]

Brownian-clock increments in different cells and in each cell’s two pieces are independent. Also Σqᵢ=1 and max qᵢ≤max(p,1−p)ⁿ, proving the variance bound. At the fixed endpoint one, temporal-midpoint sums therefore converge in L² to the first expression below, whereas symmetric-endpoint sums equal the second exactly.

\[ \sum_i M_{u_i}(M_{t_{i+1}}-M_{t_i})\xrightarrow{L^2}\frac12(M_1^2-1)+p,\qquad\sum_i\frac{M_{t_i}+M_{t_{i+1}}}{2}(M_{t_{i+1}}-M_{t_i})=\frac12M_1^2. \]

This does not reject every midpoint method. Standard Brownian time assigns half the variance to each half of an equal cell, and the same calculation leaves 1/2. The counterexample says that halving time need not halve the second-order clock. A general definition cannot follow from one example with a uniform clock.

## 32.14 What an Equation Containing dB Asks Us to Construct

<a id="ito-sde-meaning"></a>

Change of variables constructs new paths from existing ones and gives a testable meaning to evolution by local rules. Writing dX=b dt+σ dB does not create an ordinary derivative of B. On a given filtration and Brownian motion it asks for a continuous adapted X satisfying the integral identity simultaneously for all t.

\[ X_t=X_0+\int_0^t b(s,X_s)\,ds+\int_0^t\sigma(s,X_s)\,dB_s,\qquad\int_0^T|b(s,X_s)|\,ds<\infty,\quad\int_0^T\sigma(s,X_s)^2\,ds<\infty\quad\text{a.s.} \]

The integration rules must lie in Chapter 31’s domain. Model coefficients below are continuous, producing predictable processes on continuous adapted solutions. Square energy is only required locally almost surely; the resulting integral is not automatically a true martingale. The initial value is finite and F₀-measurable. We will construct solutions and prove uniqueness for specific models, not infer general existence from the definition.

This imposes an information-order requirement beyond specifying a random variable’s law: the solution must be compatible with the same driver and filtration. General existence, pathwise uniqueness, uniqueness in law and weak solutions require distinct theorems, assigned to Chapter 35.

## 32.15 How an Exponential Cancels Its Own Quadratic Growth

<a id="ito-stochastic-exponential"></a>

An ordinary linear equation suggests an exponential. Given a continuous local martingale M starting at zero and continuous adapted finite-variation V, seek dZ=Z dM+Z dV with Z₀=1. Trying exp(M+V) produces an extra half of quadratic growth by Itô formula. Subtracting half of [M] in the exponent cancels that term.

\[ Z_t=\exp\!\left(M_t+V_t-\frac12[M]_t\right),\qquad dZ_t=Z_t\,dM_t+Z_t\,dV_t. \]

For the proof put U=M+V−[M]/2 into the exponential: d[U]=d[M], so the first-order −d[M]/2 cancels the second-order +d[M]/2. Coefficients are pathwise bounded on compact intervals, making the local integrals legitimate. This is not a guessed solution assembled from formal differentials.

Uniqueness can be checked directly. Applying the formula to Z⁻¹ gives the identity below. If X solves the same linear equation with initial value X₀, the product term [X,Z⁻¹]=−∫XZ⁻¹d[M] cancels the remaining drift, giving XZ⁻¹=X₀. This includes zero and negative initial values without an illicit use of log X.

\[ d(Z^{-1})=-Z^{-1}\,dM-Z^{-1}\,dV+Z^{-1}\,d[M],\qquad X_t=X_0Z_t. \]

When V=0 this positive exponential is a continuous local martingale. Nonnegativity and conditional Fatou make it a supermartingale with expectation at most one. Equality requires additional conditions. We have constructed an equation’s solution, not proved that it can always be used to change probability measure.

## 32.16 Which Term Changes When a Multiplicative Model Changes Convention

<a id="ito-geometric-brownian"></a>

For real constants μ,σ put M=σB and V=μt. The preceding section gives the unique continuous adapted solution of the geometric Brownian equation. X₀ is finite and F₀-measurable without a required second moment. Expectation conclusions require their own integrability assumptions.

\[ dX_t=\mu X_t\,dt+\sigma X_t\,dB_t,\qquad X_t=X_0\exp\!\left((\mu-\tfrac12\sigma^2)t+\sigma B_t\right). \]

If X₀ is integrable, independence of Brownian increments from F₀ and the Gaussian exponential mean give E[Xₜ|F₀]=X₀e^{μt}. For deterministic positive initial value, log X instead has drift μ−σ²/2. The two growth readings follow from the constructed solution and quadratic correction.

Writing the same solution in Stratonovich form must change its drift as well, since [σX,B]=σ²∫Xds. Retaining the same μ in both conventions does not describe the same process.

\[ dX_t=(\mu-\tfrac12\sigma^2)X_t\,dt+\sigma X_t\circ dB_t. \]

More generally, for an already given d-dimensional solution driven by an m-dimensional standard Brownian motion, with spatially C¹ σ and continuous derivatives, conversion subtracts the expression below from the i-th Itô drift. The covariation needed for C¹ compositions is supplied by Section 12’s extension, without assuming general existence or uniqueness.

\[ b^i_{\mathrm{Strat}}=b^i_{\mathrm{Ito}}-\frac12\sum_{j=1}^m\sum_{k=1}^d\sigma^{kj}\,\partial_{x_k}\sigma^{ij}. \]

## 32.17 Returning to a Restoring Force: A Process and Its Equation

<a id="ito-ou-equation"></a>

Chapter 23 constructed OU processes through Gaussian structure. The question now is different: how can paths be built from a rule with stronger deterministic restoration farther from m and constant Brownian forcing? Take θ>0 and real m,σ, with finite F₀-measurable U₀. The deterministic integrating factor e^{θt} has finite variation and produces no covariation correction.

\[ dU_t=-\theta(U_t-m)\,dt+\sigma\,dB_t,\qquad U_t=m+e^{-\theta t}(U_0-m)+\sigma e^{-\theta t}\int_0^t e^{\theta s}\,dB_s. \]

The integral is constructed in Chapter 31, with a deterministic coefficient square-integrable on every finite horizon, giving a continuous version. The product formula directly verifies the equation. The difference D of two solutions satisfies Dₜ=−θ∫₀ᵗDₛds; pathwise multiplication by e^{θt} makes it identically zero, proving pathwise uniqueness for this model.

For s<t split the integral at s. Its latter part is a Gaussian integral independent of Fₛ: first use independent Gaussian increments for deterministic elementary coefficients, then pass by isometry and characteristic functions. Isometry computes its variance, yielding a conditional transition law rather than only one-time marginals.

\[ \mathcal L(U_t\mid\mathcal F_s)=N\!\left(m+e^{-\theta(t-s)}(U_s-m),\ \frac{\sigma^2}{2\theta}(1-e^{-2\theta(t-s)})\right). \]

If U₀ is independent of future Brownian motion and Gaussian with mean m and variance σ²/(2θ), the transition preserves this law. Joint Gaussian covariance is σ²e^{−θ|t−s|}/(2θ), so all finite-dimensional distributions are stationary. The process constructed in [Chapter 23](23-gaussian-paths.md) is now also characterized by an integral equation with a unique solution.

## 32.18 Why Future Averages Produce a Second-Order Operator

First restrict to time-homogeneous coefficients b(x),σ(x). For a given solution dX=b(X)dt+σ(X)dW, the finite-variation part of a smooth test function is b·∇f plus the pairing of second-order covariance with its Hessian. Chapter 28’s operator form now has a pathwise source.

\[ Lf(x)=\sum_i b^i(x)\partial_i f(x)+\frac12\sum_{i,k}(\sigma\sigma^{\mathsf T})^{ik}(x)\partial_{ik}f(x). \]

For time-dependent coefficients write \(L_t f(x)=\sum_i b^i(t,x)\partial_i f(x)+\tfrac12\sum_{i,k}(\sigma\sigma^{\mathsf T})^{ik}(t,x)\partial_{ik}f(x)\). This is the time-dependent local drift operator in Itô formula. If the Markov property has separately been established, transitions generally carry two time indices; it must not simply be treated as Chapter 28’s one-parameter semigroup generator. The OU model below has time-independent parameters, so we retain L and P_t.

This is first a local drift expression for a given solution. By itself it proves neither existence, the Markov property nor a well-posed generator. For the OU process already constructed, take compactly supported C² f. Both Lf and σf′ are bounded, so the integral martingale is true. Expectations, continuous paths and dominated convergence give a pointwise short-time rate of change of averages.

\[ P_t f(x)-f(x)=\int_0^t E_x Lf(U_s)\,ds,\qquad\lim_{t\downarrow0}\frac{P_tf(x)-f(x)}t=-\theta(x-m)f'(x)+\frac12\sigma^2f''(x). \]

The pointwise limit has not been promoted to a generator derivative in the C₀ norm; domains and boundary conditions still require [Chapter 28](28-semigroups.md). What we have is a proved connection between random paths, integral equations and deterministic operators.

## 32.19 Smoothness Cannot Be Removed by Formal Calculation

<a id="ito-nonsmooth-boundary"></a>

A short test reveals the role of the hypotheses. Substituting f(x)=|x| and discarding the correction because its second derivative vanishes away from zero would give the impossible identity below. Set sgn(0)=0. The right integrand is bounded and predictable, giving a mean-zero square-integrable martingale, whereas the left expectation is √(2t/π)>0.

\[ |B_t|\ne\int_0^t\operatorname{sgn}(B_s)\,dB_s,\qquad E|B_t|=\sqrt{2t/\pi}>0\quad(t>0). \]

The stochastic integral exists. The error is that absolute value is outside the proved C² class and its corner contribution has been omitted. A new path accumulation must be studied; local time and the associated nonsmooth formula belong to Chapter 37. The contradiction identifies a boundary without pretending to prove the more general formula.

## 32.20 Why One Path Can Have Different Chain Rules

<a id="ito-chapter-insight"></a>

The first-order sum, weighted quadratic sum and cubic remainder left by the initial cube have reached different limits. We can now give the same account for general smooth functions, and explain exactly why the classical rule still holds on continuous finite-variation paths. What matters is the path’s second-order structure and how its integral accumulates changes.

The Hessian reads shared fluctuations. Itô integration leaves this contribution explicit outside the integral; endpoint-symmetric integration absorbs part of it into the definition. The singular clock further shows why “middle” cannot be judged from time length alone. A chain rule’s form is not a universal pronouncement about randomness, but a mathematical consequence of paths, limits and accumulation conventions.

Explicit equations now have verifiable solutions rather than attractive differential symbols. Conversely, given a continuous martingale with its own quadratic clock but no prescribed Brownian driver, could smooth functions and exponential tests help identify its motion? The next worthwhile question is whether the change-of-variable tools can read the noise in reverse.

### Sources and Scope of Proof

Conditions for Itô formula and continuous semimartingales can be checked against [Tehranchi’s author notes](https://www.statslab.cam.ac.uk/~mike/StoCal/notes.pdf). This chapter supplies a modern reconstruction by Taylor remainders, weighted quadratic sums and localization, not a paragraph-by-paragraph translation. Stratonovich’s paper A New Representation for Stochastic Integrals and Equations appeared in SIAM Journal on Control 4(2), 362–371 (1966); see the [journal record](https://epubs.siam.org/doi/10.1137/0304028). Publication year must not be confused with the later online date. Our discovery sequence is a teaching reconstruction, not a claim to reproduce the author’s historical thoughts.

The proved scope is one-dimensional, multidimensional and C¹,² time-space Itô formula for continuous semimartingales, products and bracket transformations, endpoint-symmetric integration with an explicit C¹-composition extension, and construction and pathwise uniqueness for specific linear SDEs. General SDE well-posedness belongs to Chapter 35, jump Itô to 34, measure change and representation to 33, and nonsmooth local-time theory to 37. Full technical arguments are in [T-ITO-FORMULA](../foundations/t-ito-formula.md), whose name cannot substitute for its actual proofs.
