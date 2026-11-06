# T-SUBADDITIVE: Kingman’s Theorem and Random Products

This page completes [the subadditive proof](../chapters/41-ergodic-theory.md#ergodic-subadditive). Assume T preserves probability, X₀=0, every Xₙ is finite and integrable, X_{m+n}≤X_m+X_n∘Tᵐ for all nonnegative integer m,n almost surely, and inf EXₙ/n>−∞. Intersect countably many sets and remove all their T-preimages so every inequality can be used along the remaining orbits.

## 1. Fekete limits of expectations and a nonpositive reduction

<a id="subadditive-proof-reduction"></a>

For finite numbers a_n with a_{n+m}≤a_n+a_m, write N=qk+r with 0≤r<k. Then a_N≤q a_k+a_r. Division and increase of N give limsup a_N/N≤a_k/k, while liminf is bounded below by the infimum. Thus the limit equals inf a_n/n, allowing −∞. Expectations EX_n satisfy this relation by preservation.

\[ Y_n=X_n-\sum_{j=0}^{n-1}X_1\circ T^j\le0,\qquad Y_{m+n}\le Y_m+Y_n\circ T^m,\qquad Y_0=Y_1=0. \]

All Y_n remain integrable. After proving their unit-cost limit, Birkhoff restores the removed average. This reduction makes skipped intervals contribute nonpositive upper bounds, allowing gaps to be discarded legally in the later cover. It does not assume that the original costs are nonnegative.

## 2. The full two-sided argument in the ergodic case

<a id="subadditive-proof-ergodic"></a>

First suppose T is ergodic and let β=inf EY_n/n∈[−∞,0]. For fixed k and N≥k, decompose from every offset r=0,…,k−1 into complete k-blocks. Prefix and terminal costs are nonpositive. Discard them and sum the k inequalities: each starting point 0,…,N−k occurs once, giving kY_N≤Σ_{j=0}^{N-k}Y_k∘Tʲ. Birkhoff gives limsup Y_N/N≤EY_k/k. Intersecting over k gives the upper bound β. If β=−∞, the extended-real limit is already established.

Suppose β is finite and put G=liminf Y_n/n≤0. The inequality Y_{n+1}≤Y₁+Y_n∘T gives G≤G∘T. Apply a bounded strictly increasing function on [−∞,0]; preservation makes the integrals equal, forcing equality almost surely. Ergodicity makes G a constant, possibly −∞. If G<β, choose a finite a with G<a<β and a<0.

\[ B_K=\bigcup_{1\le k\le K}\{Y_k<ka\},\qquad P(B_K)\uparrow1. \]

Fix K and scan j=0,…,N−K. When Tʲω∈B_K choose the smallest suitable k≤K, select [j,j+k), and move to j+k; otherwise move one step. Selected intervals are disjoint within [0,N], with at most K untreated terminal positions. Their total length L covers every available starting point, whether already inside a selected interval or selected when reached. Hence L≥Σ_{j=0}^{N-K}1_{B_K}∘Tʲ. Finite subadditivity and nonpositive gap costs give Y_N≤aL≤aΣ1_{B_K}∘Tʲ.

Take expectations and divide by N. Fekete gives β≤aP(B_K), but for sufficiently large K the right side is smaller than β, a contradiction. Thus G≥β and Y_n/n→β almost surely. For finite β, −Y_n/n is nonnegative and its expectations tend to −β. Scheffé’s identity E|Z_n−Z|=EZ_n+EZ−2E min(Z_n,Z), with domination of the minimum by Z, gives L¹ convergence. Bounded expectations alone have not been mistaken for uniform integrability.

## 3. Nonergodic environments and legitimate integration of the limits

<a id="subadditive-proof-conditional"></a>

On a standard Borel system use [T-ERGODIC-DECOMPOSITION](t-ergodic-decomposition.md#decomposition-proof-ergodicity). The countably many variables and full-measure inequalities remain integrable and valid under almost every ergodic kernel. Set b_n=E[Y_n|I]≤0. Invariant test integrals give E[Z∘Tᵐ|I]=E[Z|I], so b_{n+m}≤b_n+b_m on one common set.

Pointwise Fekete gives the limit β(ω)=inf b_n(ω)/n. Along factorial indices b_{n!}/n! decreases, since the next factorial is an integer multiple of the preceding one, and has the same infimum. Monotone convergence for nonpositive variables gives Eβ=lim EY_{n!}/n!=inf EY_n/n>−∞. Hence β is finite almost surely and integrable. Concentration of the kernels on their invariant parameters fixes all b_n within an environment, so the ergodic proof gives Y_n/n→β under the original probability almost surely.

Unconditional Fekete also gives EY_n/n→Eβ. The same nonnegative Scheffé argument proves global L¹ convergence, rather than exchanging uncontrolled outer integrals of componentwise L¹ limits. Restore the Birkhoff limit of S_nX₁/n: γ=β+E[X₁|I]=inf E[X_n|I]/n, and Eγ=inf EX_n/n.

For a nonstandard original probability space, pass to the countable record factor (X_n∘Tᵏ). Pull back the proved convergence. For each fixed X_n, the original and factor Birkhoff limits are the same along the same record, so E[X_n|I_original] equals the pulled-back conditional mean. The conditional formula therefore holds without assuming a regular kernel on the original space.

## 4. Matrix applications and the boundary of the proved scope

<a id="subadditive-proof-products"></a>

For stationary invertible matrices, operator norms satisfy ‖BC‖≤‖B‖‖C‖ and ‖BC‖≥1/‖(BC)⁻¹‖. Logarithms of a product lie between −Σlog⁺‖A_j⁻¹‖ and Σlog⁺‖A_j‖. This makes each X_n integrable and bounds EX_n/n below by −E log⁺‖A₀⁻¹‖. The theorem gives the maximal norm growth rate, constant in the ergodic case. Invertibility can be replaced by any other verified linear expected lower bound.

The example X_n=−n² shows that the finite lower bound excludes −∞, rather than being optional for a finite conclusion. Continuous-time subadditivity, nonstationary arrays and the full directional Lyapunov spectrum are not proved here. Any responsibility for the full multiplicative ergodic theorem requires an actual separate proof and cannot be inferred from the norm result. Return to [the matrix example](../chapters/41-ergodic-theory.md#ergodic-matrix).
