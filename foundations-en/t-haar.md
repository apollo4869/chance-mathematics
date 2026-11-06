# T-HAAR: The Existence of Averaging, Local Measurement and Left versus Right

We prove Haar probability for compact metrizable groups and existence and uniqueness up to scale of left Haar measure for locally compact Polish groups. All groups are Hausdorff topological groups; the nonmetrizable version is outside this proof. The measure tools are Chapter6 integration, Chapter24 compactness and bounded positive functional representation in T-FELLER-PATHS; a locally finite version is also proved below. Return to [Chapter45](../chapters/45-invariance.md#haar-question).

## 1. On a compact group, one average yields every translation

<a id="haar-compact"></a>

Let G be compact and metrizable. Put positive masses on a countable dense sequence and normalize to obtain a probability ρ with full support. Its zeroth convolution power is the unit point mass. Convolution is the law of the ordered product of independent group elements; associativity follows from associativity in G and Fubini.

\[ \nu_N=N^{-1}\sum_{j=0}^{N-1}\rho^{*j},\qquad \rho*\nu_N-\nu_N=N^{-1}(\rho^{*N}-\delta_e). \]

Compactness and Chapter24 give a weakly convergent subsequence with limit ν. For continuous f, the function y↦∫f(hy)ρ(dh) is continuous by dominated convergence. Hence ρ*ν=ν. For continuous real f set u(x)=∫f(xy)ν(dy). Joint continuity and compactness make u continuous, and stationarity gives

\[ u(x)=\int u(xh)\,\rho(dh). \]

The function u attains its maximum. At a maximum point the right side averages numbers no larger than that maximum, so equality holds for ρ-almost every h. Continuity and full support upgrade this to every h; since xG=G, u is constant. Thus ν is invariant under every left translation, first on continuous tests and then on Borel sets because continuous functions determine finite Borel measures. No uniform distribution on G was assumed in this argument.

Push ν forward by inversion to obtain a right invariant probability r. For any left invariant probability m, integrate f(xy) against r(dx)m(dy), for bounded Borel f. Integrating y first gives mf; integrating x first gives rf. Thus m=r. Taking m=ν proves that ν is also right invariant; every other left invariant probability equals this same r. This proves existence, uniqueness, two-sided invariance and normalization to total mass one.

## 2. Comparing local sizes before having an integral

<a id="haar-covering"></a>

Now let G be locally compact Polish. Fix a nonzero nonnegative compactly supported continuous function f₀. Such functions exist by continuous distance cutoffs inside a relatively compact open neighborhood. For nonnegative f and nonzero nonnegative g define a covering cost. Here Lₐg is x↦g(a⁻¹x).

\[ (f:g)=\inf\left\{\sum_{i=1}^k c_i:f\le\sum_{i=1}^k c_i L_{a_i}g,\ c_i\ge0\right\},\qquad I_g(f)=\frac{(f:g)}{(f_0:g)}. \]

The function g is bounded below by a positive constant on some nonempty open set. Finitely many left translates cover the compact support of f, so the cost is finite. For nonzero f it is at least the supremum of f divided by that of g, and is positive. Moving covering centers proves left invariance; combining covers proves subadditivity; scaling proves positive homogeneity; substituting one cover into another proves the multiplicative comparison.

\[ (f:h)\le(f:g)(g:h),\qquad (f_0:f)^{-1}\le I_g(f)\le(f:f_0)\quad(f\ne0). \]

These bounds do not depend on the small function g. Additivity is the remaining difficulty: one cover may help two functions at once, so adding their separate costs need not equal the cost of their sum. We must show that this discrepancy disappears when the support of g shrinks to the identity.

## 3. Why the covering costs become additive

<a id="haar-additivity"></a>

Fix nonnegative f₁,f₂ and choose nonnegative h at least one on the union of their supports. Given ε>0 put F=f₁+f₂+εh, and set rᵢ=fᵢ/F, with value zero where F=0. These ratios are compactly supported continuous functions: on the compact set where a numerator can be nonzero the denominator is at least ε, while the numerator vanishes outside it. Their sum is at most one.

Compactly supported continuous functions are uniformly continuous under small right translations. To prove this, restrict the relevant points to the support times a fixed compact neighborhood and use a finite cover for joint continuity; elsewhere both values vanish. Thus for δ>0 choose an identity neighborhood U such that |rᵢ(au)−rᵢ(a)|≤δ for every a and u∈U. If g is supported in U and F≤ΣcⱼLₐⱼg, multiply the cover by rᵢ and freeze its ratio on each small piece. This gives

\[ f_i\le\sum_j(r_i(a_j)+\delta)c_jL_{a_j}g,\qquad (f_1:g)+(f_2:g)\le(1+2\delta)(F:g). \]

Take the infimum of covering costs, bound (F:g) by subadditivity and divide by (f₀:g). The defect is bounded by \(2\delta I_g(f_1+f_2)+(1+2\delta)\varepsilon I_g(h)\). The preceding upper bounds are uniform in g. Shrink the support to make δ arbitrarily small, then send ε to zero. This proves asymptotic additivity, rather than mistaking subadditivity for additivity.

## 4. From the small-piece limit to an actual measure

<a id="haar-radon"></a>

Choose a nested compact exhaustion whose interiors cover G, and nonnegative cutoffs χₙ equal to one on its nth compact set. Each fixed-support continuous function space is separable in the uniform norm, being a subspace of continuous functions on a compact metric space. Choose countable dense families in their positive cones. Choose nonzero nonnegative gₙ supported in shrinking identity neighborhoods. Successive subsequences and a diagonal choice make \(I_{g_n}\) converge on every dense test.

\[ |I_g(f)-I_g(k)|\le I_g(|f-k|)\le\|f-k\|_\infty(\chi_n:f_0)\quad(\operatorname{supp}f\cup\operatorname{supp}k\subset K_n). \]

Consequently the limit L(f) exists for every nonnegative compactly supported continuous f. Asymptotic additivity gives additivity and the exact covering translation identity gives left invariance; L(f₀)=1. Positive and negative parts extend it to a positive linear functional on real Cc. Turning that functional into a measure still requires a representation argument, which we supply.

Choose the cutoffs χₙ between zero and one and eventually equal to one at every point. Choose positive εₙ with Σ εₙ(1+Lχₙ)<∞ and set w=Σεₙχₙ. Then w is strictly positive and in C₀, while its partial sums \(w_N\) lie in Cc. For f∈C₀ the sequence \(L(fw_N)\) is Cauchy: a tail difference is bounded by ||f|| times the tail of Σ εₙLχₙ. Its limit J is a bounded positive functional. The [proved bounded representation](t-feller-paths.md#t-feller-riesz) gives a finite Radon measure ν.

\[ \mu(dx)=w(x)^{-1}\nu(dx),\qquad \int f\,d\mu=J(f/w)=L(f)\quad(f\in C_c(G)). \]

The equality holds because \(w_N/w\) tends uniformly to one on the compact support of f and L is bounded there. The measure μ is finite on compact sets; local regularity follows from finite ν and its positive continuous weight, and compact exhaustion gives global Radon regularity. Left invariance on continuous tests extends by local cutoffs to Borel sets. Every nonempty open set contains a nonzero nonnegative continuous test, whose integral is positive by the covering lower bound. Thus μ is a nonzero left Haar measure, with its scale fixed explicitly by L(f₀)=1.

## 5. Uniqueness up to scale does not assume a modular function

<a id="haar-uniqueness"></a>

Let μ be left Haar and r right Haar; the latter is obtained by inverting any left Haar measure. For nonzero nonnegative f∈Cc and g∈Cc, Fubini and two legitimate translations give the following identity. All relevant integrals are confined to compact products, so no subtraction of infinities occurs.

\[ \mu(f)r(g)=\iint f(x)g(yx)\,\mu(dx)r(dy)=\int g(z)\left[\int f(y^{-1}z)\,r(dy)\right]\mu(dz). \]

The bracket divided by μ(f) defines a continuous \(D_f\)(z): as z varies over a compact neighborhood, the relevant y stay in a fixed compact set, so dominated convergence applies. The identity says r=\(D_f\) μ. Different f give the same measure, hence equal \(D_f\) almost everywhere for μ; continuity and positive mass on open sets make them equal everywhere. Denote the common function by D. At the identity the inverse image measure of r equals D(e)μ. Taking r to be the inverted image of any second left Haar λ gives λ=D(e)μ. This proves uniqueness without circularly assuming a right-translation factor.

## 6. The modular function, relative invariance and failure of finite mass

<a id="haar-modular"></a>

A right translate of a left Haar measure is again left Haar, so uniqueness gives a positive factor. We use the following convention explicitly; books defining its reciprocal require a consistent change throughout.

\[ \mu(Ag)=\Delta(g)\mu(A),\qquad \int f(xg)\,\mu(dx)=\Delta(g)^{-1}\mu(f),\qquad \Delta(gh)=\Delta(g)\Delta(h). \]

Composing right translations proves multiplicativity. For nonzero nonnegative f∈Cc the factor is expressed by a continuous integral ratio, again with a common compact support locally, so Δ is continuous. Left Haar is two-sided exactly when Δ is identically one. For a compact group Δ(G) is a compact subgroup of the positive multiplicative reals; taking logarithms forces it to be {0}, giving two-sided invariance again. For a general action relative invariance means μ(gA)=χ(g)μ(A) for a continuous positive character χ. Merely preserving null sets, or quasi-invariance, is weaker and must not be conflated with it.

For the affine group (a,b)(c,d)=(ac,b+ad), with a,c>0, direct Jacobian calculation gives left Haar da db/a² and right Haar da db/a. Our convention gives Δ(c,d)=1/c. Left multiplication has Jacobian a² and right multiplication Jacobian c; the two densities give exactly the stated transformation laws. This computes the failure of equivalence of left and right rather than merely naming a noncommutative group.

Finally a noncompact G has no finite nonzero Haar measure. Choose a nonempty relatively compact open U, with positive finite mass. Given finitely many disjoint gᵢU, choose the next center outside the finite union of the compact closures of gᵢUU⁻¹; noncompactness permits this. There are arbitrarily many disjoint open sets of the same positive mass, contradicting finite total mass. Conversely a locally finite measure on compact G has finite total mass and is normalized by dividing by μ(G). Integer translates of an interval on the real line are the simplest instance.
