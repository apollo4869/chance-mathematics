# T-LIE-LEVY: An Actual Construction on Compact Matrix Lie Groups

Companion to [Chapter 40](../chapters/40-stochastic-geometry.md#geometry-lie-jumps). We prove a general small-jump triplet construction, its generator and fixed-truncation triplet uniqueness on a given compact smooth matrix Lie group G⊂O(N). This is not Hunt’s necessity classification for all Lévy processes on arbitrary Lie groups. Neither Chapter 48 general point-process theory nor Peter–Weyl theory is used.

## 1. Matrix Multiplication Gives the Correct Local Rule

<a id="lie-proof-geometry"></a>

Assume G is already a smooth embedded submanifold of O(N), with smooth multiplication and inversion; no unproved closed-subgroup smoothness theorem is invoked. Its Lie algebra is the tangent space at I, consisting of skew matrices. The left-invariant field is \(X_A(g)=gA\). The ODE g′=gA has unique solution g exp(tA), stays in G by tangency and exists globally by compactness. The exponential series has identity differential at zero, so the local inverse argument of T-GEOMETRY gives an exponential chart.

Choose a basis Aᵢ of the Lie algebra, write h=exp(ηⁱ(h)Aᵢ) near I and choose a smooth cutoff ρ equal to one on a smaller neighborhood. Let χⁱ=ρηⁱ and zero outside its support. Finite-dimensional Taylor estimates give h−I−χⁱ(h)Aᵢ=O(‖h−I‖²). This remainder permits convergent drift compensation; the integral of χ alone may diverge.

\[ b\in\mathbb R^d,\quad q=\sigma\sigma^{\mathsf T}\ge0,\quad A_\alpha=\sigma_{i\alpha}A_i,\qquad
\nu(\{I\})=0,\quad \int_G\|h-I\|^2\,\nu(dh)<\infty. \]

Let ν be Radon on G\{I}. Compactness makes the condition equivalent to local second-order integrability and finite mass away from I. Decompose into finite-measure annuli. Independent Poisson clocks and marks from Chapter 21, on a countable product space from Chapter 8, construct the random measure of intensity dtν(dh), independently of Brownian input. Chapter 34 predictable compensated L² integration applies componentwise to finite matrices.

## 2. How Infinite Small Products Become a Group-Valued Process

<a id="lie-proof-construction"></a>

\[ C=b^iA_i+\frac12\sum_\alpha A_\alpha^2+\int_G(h-I-\chi^i(h)A_i)\nu(dh),\qquad
dY_t=Y_{t-}C\,dt+\sum_\alpha Y_{t-}A_\alpha\,dW_t^\alpha+\int_GY_{t-}(h-I)\,\widetilde N(dt,dh),\quad Y_0=I. \]

First keep only ‖h−I‖>ε. The jump measure is finite. Between jumps use the left-invariant Stratonovich drift (bⁱ−∫χⁱdν)Aᵢ and Gaussian fields Aα; at a jump right-multiply the current state by h. Continuous segments on compact G do not explode, and each finite time interval has finitely many jumps, so Yε is an actual G-valued process. Rewriting jumps as compensated integrals gives the displayed equation with Cε integrated only over the retained set. An unrenormalized drift need not converge.

The second-order remainder gives Cε→C with uniformly bounded Cε. Every Yε has Frobenius norm √N. Subtract two cutoff equations and apply continuous and compensated-jump Doob–L² estimates, drift Cauchy–Schwarz and matrix multiplication bounds. This gives the inequality below with constants depending on T and uniform second-order coefficients, not the possibly divergent integral of χ. Gronwall gives maximal-L² Cauchy convergence. Summable subsequences converge almost surely uniformly, then diagonalize over integer T.

\[ E\sup_{s\le T}\|Y^\varepsilon_s-Y^\delta_s\|^2
\le K_T\left(\|C_\varepsilon-C_\delta\|^2+
 \int_{\{\|h-I\|\le\max(\varepsilon,\delta)\}}\|h-I\|^2\nu(dh)\right). \]

The uniform limit is càdlàg; G is closed in matrix space, so Y stays in G and cannot explode. Isometry and drift bounds pass every integral to the limit. Differences of any two solutions satisfy the error-free Gronwall estimate after state localization, proving pathwise uniqueness. Chapter 35 linear Picard could construct an ambient matrix solution, but the cutoff argument additionally proves the group constraint.

For deterministic s, Yₛ⁻¹Yₛ₊ₜ solves the same equation from I with future Brownian and Poisson increments. Those are independent of the whole past and have the original laws; pathwise uniqueness identifies the same measurable solution map. Hence left increments are independent and stationary. L² estimates give stochastic continuity. Together with constructed càdlàg paths, this is a genuine group Lévy process, not merely a collection of marginal laws.

## 3. Generator, Truncation and the Uniqueness Actually Proved

<a id="lie-proof-generator"></a>

\[ Af(g)=b^iX_if(g)+\frac12q^{ij}X_iX_jf(g)
+\int_G\big(f(gh)-f(g)-\chi^i(h)X_if(g)\big)\nu(dh). \]

Extend smooth f locally to ambient space as in T-GEOMETRY and apply Chapter 34 jump Itô. The continuous Gaussian term and the ½ΣAα² drift combine into ½qⁱʲXᵢXⱼ. The compensator part of C cancels the jump correction’s linear term, leaving the displayed integral. Its remainder is uniformly O(‖h−I‖²) near I, with finite ν away, justifying measurability, integrability and DCT. On compact G, Af is bounded continuous; the expectation identity and stochastic continuity identify the actual infinitesimal generator.

For fixed χ, the generator identifies this triplet uniquely. Smooth tests vanishing near I determine ν on compact sets away from I; smooth approximation and Radon uniqueness identify the measure. After subtracting the known jump integral, local tests with zero value and first jet but arbitrary symmetric second jet identify q. Arbitrary first jets then identify b. Replacing χ by χ′ changes b to b+∫(χ′−χ)dν, a finite second-order correction; it need not change the process.

The constructed L² equation class also has process uniqueness. We have not proved that every group-valued Lévy process necessarily has Hunt form, nor abstract martingale-problem uniqueness for every degenerate group generator. Those necessity and broad characterization statements remain open here, rather than being hidden behind a familiar formula.

## 4. Noncommutativity and Metric Brownian Motion

<a id="lie-proof-structure"></a>

Noncommutativity is visible directly in the Heisenberg group, whose product adds xy′ to the third coordinate. For a=(1,0,0) and b=(0,1,0), ab=(1,1,1) but ba=(1,1,0). This group is outside the compact-matrix theorem, but the finite calculation needs no limit theorem. A compound Poisson process multiplying independent marks in arrival order already retains information lost by Euclidean addition. Exponentiating one sum from Chapter 27 is not a general group-process construction.

On compact G⊂O(N), the Frobenius inner product is invariant under conjugation, so its left-translated metric is also right invariant. On left-invariant fields, ∇X Y=½[X,Y] is torsion-free; cyclicity of trace gives 〈[X,Y],Z〉+〈Y,[X,Z]〉=0, proving metric compatibility. Levi–Civita uniqueness identifies the connection. For an orthonormal left-invariant basis, ∇XᵢXᵢ=0; b=0, q=I and ν=0 therefore give Riemannian Brownian motion for this bi-invariant metric. An arbitrary left-invariant metric need not be bi-invariant.

The construction permits infinitely many small jumps but remains within given compact matrix Lie groups. Recovering local characteristics from an arbitrary group-valued Lévy process requires a separate necessity argument, not supplied by constructing a prescribed triplet. Return to the [chapter](../chapters/40-stochastic-geometry.md#geometry-lie-jumps).
