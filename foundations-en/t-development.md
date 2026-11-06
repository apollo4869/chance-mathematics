# T-DEVELOPMENT: Stochastic Development, Invariance and Lifetime

Companion to [Chapter 40](../chapters/40-stochastic-geometry.md#geometry-development). Use the connection and horizontal fields of [T-GEOMETRY](t-geometry.md), and the independently proved continuous-driver existence theorem in [T-MANIFOLD-DIFFUSIONS](t-manifold-diffusions.md#manifold-proof-clock). M is boundaryless with smooth g; except for explicit boundary examples, processes are maximal without extra killing.

## 1. Development and Antidevelopment Are Actual Inverse Constructions

<a id="development-proof-construction"></a>

\[ dU_t=\sum_iH_i(U_t)\circ dZ_t^i,\quad X_t=\pi(U_t),\qquad Z_t^i=\int_0^t(U_s^{-1})^i_k\circ dx^k(X_s),\quad Z_0=0. \]

Given a continuous Rⁿ semimartingale Z and initial orthonormal frame u₀, smooth horizontal fields on O(M) give an actual maximal solution U by the previous theorem, hence X. Their coordinate formula shows that U is parallel along X. Conversely, given a continuous manifold semimartingale X, solve the displayed parallel-transport equation locally. It is a smooth-field equation on (x,U): the x-component is a coordinate unit vector and the frame component is the connection term, so the same theorem applies and its base is the given X.

To close a possible gap from infinitely many changing local drivers, choose the separating immersion F on a finite compact path region. Its differential has a smooth left inverse L, constructed locally as (DFᵀDF)⁻¹DFᵀ and patched with a partition while retaining L dF=Id. Stratonovich gives dX=L(X)∘dF(X). Horizontally lifting the directions of L expresses the frame equation with one fixed Euclidean semimartingale driver F(X). Its clock is finite on finite intervals; compact base image and compact fibers then genuinely permit the preceding maximal-solution theorem.

The connection transformation law identifies parallel lifts on overlaps, and pathwise uniqueness patches them. Metric compatibility preserves orthonormality. Before any T smaller than X’s lifetime, the compact image of X and compact frame fibers prevent earlier lift explosion. The antidevelopment is the Stratonovich integral of the global solder form θ=U⁻¹dπ, whose coordinate compatibility was proved on the preceding page.

Since θ(Hᵢ)=eᵢ, proved Stratonovich associativity gives antidevelopment(development Z)=Z. Conversely, the parallel lift of X satisfies dX=U∘dZ and the horizontal constraint, hence the same horizontal equation; uniqueness gives development(antidevelopment X)=X with the same initial frame. Changing u₀ to u₀q rotates antidevelopment to q⁻¹Z. Arbitrary changes of connection are not claimed to preserve it.

## 2. Brownian Projection, Frame Choice and Isometry Invariance

<a id="development-proof-brownian"></a>

\[ H_iH_j(f\circ\pi)(u)=\operatorname{Hess}f(ue_i,ue_j),\qquad \frac12\sum_iH_i^2(f\circ\pi)=\frac12(\Delta_gf)\circ\pi. \]

Apply Hᵢ to Uⱼᵏ∂ₖf. The frame derivative contributes the connection term and the base derivative the second partials, exactly the Hessian. Trace using ΣUᵢ⊗Uᵢ=g⁻¹. For standard Rⁿ Brownian Z, stopped chart Itô then makes f(X)−½∫Δf(X)ds a local martingale. The preceding page’s strictly elliptic law uniqueness identifies the unique maximal Riemannian Brownian law, without assuming a heat kernel exists.

The right-action identity makes \(R_qU\) the development from u₀q driven by q⁻¹Z, which is again standard Brownian. Thus projection law is independent of the initial orthonormal frame. A global Riemannian isometry Φ preserves the connection and horizontal fields; pushing U forward solves the target horizontal equation and couples the projected path as Φ(X). This proves isometry invariance in law. For local isometries, assert the identity only until the relevant exits, not a global extension through a nonproper map.

The preceding page gives strong Markov for the autonomous Brownian SDE U. Conditional on its frame at a stopping time, the projected future law depends only on the base point, not the frame; conditioning again proves strong Markov for X. Measurable Picard maps and countable chart choices give Borel transition kernels. Frame and base lifetimes agree because compact base sets have compact frame inverse images.

## 3. Connection Martingales Do Not Mean Every Coordinate Is a Martingale

<a id="development-proof-martingale"></a>

\[ df(X_t)=df(U_te_i)\,dZ_t^i+\frac12\operatorname{Hess}f(U_te_i,U_te_j)\,d[Z^i,Z^j]_t. \]

Convert the Stratonovich chain rule for the horizontal equation to Itô form, using the Hessian identity just proved. The first integral above is Itô; no convention is mixed. If Z is a continuous local martingale, subtracting the Hessian term gives a local martingale. This defines a connection martingale intrinsically. Conversely, cutoff coordinate tests force U dA=0 for antidevelopment Z=M+A. Integrating the invertible U⁻¹ makes A constant, so Z is a local martingale.

A connection martingale may therefore have coordinate drift; β=b+½Γ:a is the quantity that vanishes. Sphere Brownian’s normal ambient drift is compatible with this: ambient coordinates do not turn the sphere connection into Euclidean translation. Different connections can define different martingale notions. Coordinate compatibility alone does not select geometry.

## 4. A Usable Nonexplosion Condition

<a id="development-proof-lyapunov"></a>

\[ V\in C^2(M),\quad V\ge1,\quad\{V\le r\}\ \hbox{compact},\quad AV\le cV,\ c\ge0
\quad\Longrightarrow\quad P_x(\zeta=\infty)=1. \]

Let τᵣ be the first hitting time of V=r. Inside a compact sublevel set, bounded stopped Itô coefficients allow expectations. Gronwall gives EₓV(Xₜ∧τᵣ)≤\(e^{ct}\)V(x), and continuity bounds rP(τᵣ≤t) by the same quantity. Let r increase and use compact-exit lifetime; then unify over integer t. A time-dependent locally integrable upper coefficient replaces ct by its integral. No unproved general curvature criterion is used.

On compact M a maximal solution cannot leave every compact set, so smooth Brownian-field diffusions do not explode. On noncompact space metric completeness controls endpoints of finite-length curves, not the generator estimate above. For locally finite-variation input Z, orthonormal U makes the developed path length equal the Euclidean total variation of Z. On a complete metric manifold, vanishing tail length makes X Cauchy with an endpoint; bounded connection coefficients along that finite-variation curve also give a frame limit, permitting extension. Brownian infinite total variation does not meet this argument’s hypothesis.

## 5. A Geodesically Complete Surface with Brownian Explosion

<a id="development-proof-incomplete"></a>

\[ g=dr^2+f(r)^2d\theta^2,\quad f(r)=r\ (r\le1),\quad f(r)=e^{r^3}\ (r\ge2),\qquad
\frac12\Delta_{\rm radial}=\frac12\frac{d^2}{dr^2}+\frac{f'(r)}{2f(r)}\frac d{dr}. \]

Choose any positive smooth interpolation on 1<r<2. The metric is Euclidean near zero, so this is a smooth surface on all of R², not a punctured plane. Curve length bounds radial change, and radial lines realize distance r from the origin. Closed metric balls are compact, making every Cauchy sequence converge. Geodesic speed is constant, so r stays bounded in finite time; the fixed-speed tangent-bundle subset over that compact region is compact and the ODE extends. This directly proves geodesic completeness without assuming Hopf–Rinow.

Until hitting R≥2, the Brownian radius solves a one-dimensional SDE with drift 3r²/2. This follows from the proved Laplacian and local elliptic law, not a guess about radial motion. Let S and v be as displayed below; differentiation gives LS=0 and Lv=1. Stopped hitting calculations already proved in Chapter 36, or direct bounded-interval Itô, give the probability formula.

\[ S(r)=\int_R^r\frac{dy}{f(y)},\quad v(r)=2\int_R^r\frac{\int_R^y f(z)\,dz}{f(y)}\,dy,\quad
P_r(\tau_L<\tau_R)=\frac{S(r)}{S(L)}. \]

Here S(∞)<∞. Since the derivative of \(e^{y^3}\)/(3y²) is \(e^{y^3}\)(1−2/(3y³))≥½\(e^{y^3}\) for y≥2, the inner integral in v is at most 2f(y)/(3y²), hence v(∞)<∞. Stopping v gives Eᵣ(τᴿ∧τᴸ)≤v(∞)−v(r), uniformly in L. First stop at finite t and then use monotone convergence, so all expectations are legitimate.

The events {τᴸ<τᴿ} decrease with L and their intersection has probability S(r)/S(∞)>0. On that intersection τᴸ increases to a finite time, because the common stopped times have uniformly bounded expectations. The radius crosses every L: this is explosion of the maximal process. There is no finite-distance geometric hole, yet Brownian motion can escape in finite time. Geodesic completeness therefore does not imply stochastic completeness, and finite-variation length reasoning cannot be transferred to Brownian input.

## 6. Holes, Chart Poles and Boundary Rules Are Different

<a id="development-proof-boundary"></a>

Nor does the converse hold. The Euclidean punctured plane is geodesically incomplete, yet Brownian motion does not hit the origin. Chapter 38’s annulus computation gives Pᵣ(hit ε before R)=log(R/r)/log(R/ε)→0. Union over integer R excludes every hit of zero. On each finite time interval, continuity bounds the maximum radius and, since zero is not hit, gives a positive minimum radius. Thus compact-exit lifetime in the punctured plane is infinite.

In the half-line interior, both absorption at zero and reflection have generator ½∂², but they are different processes. For R=|x+B|, Chapter 37 Tanaka gives R=x+∫sgn(x+B)dB+L⁰(x+B). Ordinary time spent at zero is zero, so the integral has bracket t and is Brownian by Chapter 33. For C² tests with f′(0)=0 the local-time term vanishes, yielding the reflecting Neumann rule. Absorption has a positive zero atom at each positive time; the absolute Gaussian reflecting marginal has none.

The main theorem concerns the maximal interior process on a boundaryless manifold. General reflecting, sticky or elastic boundary classification is not supplied by one interior Laplacian. The examples separate a bad coordinate, actual departure from the state space, and a different boundary rule. [Return to the chapter](../chapters/40-stochastic-geometry.md#geometry-lifetime).
