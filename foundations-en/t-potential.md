# T-POTENTIAL: Harmonicity, Excessiveness, Green Potentials, Capacity and Sweeping

Companion to [Chapter 38](../chapters/38-feynman-kac.md#potential-excessive). The general Markov part uses the stated bounded continuous versions. Full Riesz decomposition, equilibrium measures and sweeping are proved for killed Brownian motion on bounded intervals. Higher-dimensional Dirichlet theory and polarity examples are in T-FEYNMAN-KAC; a one-dimensional curvature argument is not claimed as Riesz theory for all Hunt processes.

## 1. Why Future Reward Is Smaller than the Whole Reward

<a id="potential-proof-excessive"></a>

Let X be strong Markov with lifetime ζ and A a continuous increasing additive functional starting at zero. Suppose u(x)=Eₓ∫₀ζe^{-αs}dAₛ<∞. Splitting the integral and conditioning gives u−\(e^{-\alpha t}\)Pₜu=Eₓ∫₀^{t∧ζ}e^{-αs}dAₛ≥0. As t↓0, monotone convergence sends the right side to zero. Thus u is α-excessive: \(e^{-\alpha t}\)Pₜu≤u, with limit u. The limit condition excludes arbitrary bad versions; it is not decorative.

\[ u\ge e^{-\alpha t}P_tu,\qquad \lim_{t\downarrow0}e^{-\alpha t}P_tu=u,\qquad e^{-\alpha t}u(X_t)\ \hbox{is a supermartingale when integrable}. \]

At deterministic times the supermartingale assertion follows directly from conditional Markov. For continuous locally bounded u and continuous X, stop on compact sets and apply Chapters 16/30 before delocalizing. Fine right-continuity of arbitrary Borel excessive functions along Hunt paths is an additional theorem not silently used here. Harmonic functions give equality before local exits. Preservation of averages and possible decrease of averages are different structures.

## 2. The Interval Green Kernel and Riesz Decomposition

<a id="potential-proof-riesz"></a>

Let I=(a,b), kill Brownian motion at exit τ and use reference dx. Chapters 36–37 already yield G from stopping and occupation. Alternatively verify zero endpoints, piecewise linearity in x and derivative jump −2 at y, then apply generalized Itô and take expectations. This is the occupation kernel relative to dx, not its half-sized version relative to speed 2dx.

\[ G_I(x,y)=2\frac{(x\wedge y-a)(b-(x\vee y))}{b-a},\qquad E_x\int_0^\tau f(B_s)ds=\int_IG_I(x,y)f(y)dy. \]

In this section fix α=0. Suppose u is finite, continuous, nonnegative and 0-excessive for killed Brownian motion on I. Optional sampling at exit from (c,d)⊂⊂I gives u(x)≥[(d−x)u(c)+(x−c)u(d)]/(d−c), hence concavity. Conversely, stop a nonnegative concave u on compact intervals and use generalized Itô; Fatou removes the stops, while continuity gives the time-zero limit. Its endpoint limits are finite nonnegative: an infinite endpoint limit would force infinite chord values at another interior point.

\[ \mu=-\frac12u^{\prime\prime}\ge0,\qquad u(x)=h(x)+\int_IG_I(x,y)\mu(dy),\qquad h(x)=\frac{b-x}{b-a}u(a+)+\frac{x-a}{b-a}u(b-). \]

The second derivative is distributional. A concave u has monotone one-sided derivatives, whose Stieltjes measure defines locally finite μ. On Iₙ=(aₙ,bₙ)⊂⊂I, u−hₙ and G_{Iₙ}μ have the same second derivative and zero endpoints, hence coincide. Let aₙ↓a and bₙ↑b. The Green kernels increase to G_I, while hₙ→h; MCT gives the decomposition and finite potential. Second derivatives and endpoint limits identify μ and h uniquely. Every nonnegative harmonic minorant is affine with endpoint limits bounded by those of u, hence lies below h. Thus h is the greatest nonnegative harmonic minorant.

The measure may have infinite total mass near the endpoints, provided Gμ is finite inside; it remains Radon. Chapter 37 local time defines Aₜ=∫L_{t∧τ}ʸμ(dy), finite for t<τ because the path range is compact inside I. Also EₓAτ=Gμ(x)<∞ rules out infinite terminal accumulation. The Riesz potential is therefore genuinely an expected path accumulation. Its harmonic remainder is not an interior source: it retains terminal information not consumed inside.

## 3. Capacity Does Not Measure Length

<a id="potential-proof-capacity"></a>

On I let H₀¹ contain absolutely continuous zero-endpoint functions with square-integrable derivative, energy E(v)=½∫|v′|²dx. For nonempty compact K⊂I define cap_I(K)=inf{E(v):v∈H₀¹,v≥1 on K}. The pointwise constraint makes sense because one-dimensional H₀¹ has continuous versions; no unproved higher-dimensional quasi-continuity is used. Let p=minK and q=maxK. The candidate e rises linearly from zero to one on (a,p), equals one on [p,q], and falls linearly to zero on (q,b).

\[ e_K(x)=P_x(T_K<\tau),\qquad \operatorname{cap}_I(K)=\frac1{2(p-a)}+\frac1{2(b-q)},\qquad \eta_K=-\frac12e_K^{\prime\prime}=\frac{\delta_p}{2(p-a)}+\frac{\delta_q}{2(b-q)}. \]

Clamp any admissible v to [0,1] without increasing energy. Cauchy–Schwarz gives ∫ₐᵖ|v′|²≥1/(p−a), and similarly on the right; the middle energy is nonnegative. The candidate attains the bound, proving optimality and uniqueness. From between the extremes of K, continuity prevents exit from I before hitting K; interval hitting probabilities identify e with the stated probability. Derivative jumps give η, whose mass equals the energy, and Riesz gives e=Gη. A singleton c has capacity (b−a)/(2(c−a)(b−c))>0 despite zero length.

In \(d\ge2\) a point can instead be polar, as the radial calculation in T-FEYNMAN-KAC shows. Reference-measure nullity and pathwise inaccessibility are not synonymous. Smooth measures in general Revuz theory cannot charge polar sets. Transplanting the legal one-dimensional δ_c directly to two dimensions is a dimension-sensitive error.

## 4. Sweeping an Interior Source onto a Hittable Set

<a id="potential-proof-balayage"></a>

Keep I, compact K and finite positive μ, and write T=\(T_K\). Mix the distributions of hitting K before exit, starting at y, against μ to obtain μᴷ. Strong Markov splits occupation before and after T, giving a Green decomposition. Before T the process is killed in \(I\setminus K\); its Green kernel is symmetric, using the interval kernel on each component and zero across components. Thus the remainder is symmetric in x,y too.

\[ \mu^K(C)=\int_I P_y(B_T\in C,T<\tau)\mu(dy),\quad G_I\mu^K(x)=E_x[G_I\mu(B_T);T<\tau]\le G_I\mu(x). \]

Integrate the remainder against μ and use symmetry to move the hitting integral from x to y; this gives the formula. All exchanges are nonnegative Tonelli. The swept potential equals the original on K, is harmonic off K and never exceeds it. It retains observations on K while removing other interior sources. Signed finite measures require applying the argument to both parts where their absolute Green potential is finite; no unconditional global boundedness is asserted. Return to [sweeping in the chapter](../chapters/38-feynman-kac.md#potential-sweeping).
