# T-REVUZ: Continuous Bounded-Potential Correspondence for Symmetric Hunt Processes

Companion to [Chapter 38](../chapters/38-feynman-kac.md#revuz-class). This page proves an actual two-way theorem beyond a Brownian-only formula, without claiming the broadest right-process theory. A Hunt process is right-continuous strong Markov and quasi-left-continuous: X_{Tₙ}→X_T on T<ζ when Tₙ↑T with Tₙ<T. The proof uses its càdlàg realization, Markov property and the kernel assumptions below, not an unproved Dirichlet-form process-existence theorem.

## 1. The Exact Process, Measure and Equivalence Classes

<a id="revuz-proof-class"></a>

Assume E compact metric, m finite full-support Borel and X a conservative m-symmetric Feller Hunt process on canonical paths with usual filtrations. Conservativeness and symmetry make m invariant. For every λ>0 assume the resolvent has a finite nonnegative symmetric jointly continuous kernel rλ on E×E, with Rλf(x)=∫\(r_\lambda(x,y)\)f(y)m(dy). Compactness makes it bounded. This is a genuine restriction: diagonal Green singularities exclude Brownian motion in dimension two and higher. It cannot be omitted.

\[ U_1^A(x)=E_x\int_0^\infty e^{-s}dA_s,\quad R_1\mu(x)=\int_Er_1(x,y)\mu(dy),\quad \mu\in\mathcal M_+(E),\ \mu(E)<\infty. \]

A PCAF is adapted, continuous increasing from zero, finite on finite time intervals, with \(A_{s+t}\)=A_s+A_t∘θ_s on a shift-invariant set of probability one for every starting point. The functional class in this theorem explicitly requires a bounded continuous version of U₁ᴬ defined at every start. Identify functionals indistinguishable under every Pₓ. Then finite positive μ correspond bijectively to this class, with U₁ᴬ=R₁μ. The correspondence satisfies all test identities below, not merely one small-time limit.

Reflecting Brownian motion on a compact interval is a nonempty example: its cosine expansion is \(r_\lambda(x,y)\)=1/(λl)+(2/l)∑ₖ≥₁ cos(kπx/l)cos(kπy/l)/(λ+(kπ/l)²/2), uniformly absolutely convergent. Folding Brownian motion or the earlier semigroup construction supplies the process. Finite reversible continuous-time chains also qualify. Infinite-state, nonsymmetric, merely quasi-continuous-potential and all-smooth-measure versions do not follow automatically.

## 2. Actually Constructing an Accumulation from a Measure

<a id="revuz-proof-construction"></a>

Put u=R₁μ∈C(E). For integers n≥2 let \(f_n=nR_n\mu\) and uₙ=R₁fₙ=\(nR_nu\). The interchange follows from semigroup integrals and Tonelli: first verify the operator identity against densities f m, then use joint kernel continuity and full support to extend the almost-everywhere kernel identity to every y before integrating a singular μ. Feller strong continuity gives uniform uₙ→u. Each nonnegative bounded continuous fₙ gives a canonical PCAF Aₙ(t)=∫₀ᵗfₙ(Xₛ)ds.

\[ E_x\left(\int_0^\infty e^{-s}f(X_s)ds\right)^2=2R_2(fR_1f)(x),\quad |R_1f|\le\varepsilon\ \Longrightarrow\ E_x\left|\int_0^\infty e^{-s}f(X_s)ds\right|^2\le2\varepsilon R_2|f|(x). \]

For bounded signed f, split the square into s<t and t<s and condition at s; the diagonal has zero Lebesgue measure. This gives the first identity. With f=fₙ−fₖ, R₂|f|≤R₁(fₙ+fₖ)≤2‖u‖∞, so the bound tends to zero with ‖uₙ−uₖ‖∞. The closed martingale is Mₜ=∫₀ᵗ\(e^{-s}\)f(Xₛ)ds+\(e^{-t}\)R₁f(Xₜ). Doob L² makes the discounted integrals Cauchy in maximal norm. Ordinary integration by parts removes the discount at a cost at most 2eᵀ on [0,T]. Thus Aₙ converge in L² maximal norm on finite horizons, uniformly over starts.

Choose one subsequence with maximal squared errors on [0,j] bounded in expectation by 2^{-j}, uniformly in x. Borel–Cantelli gives a canonical locally uniform limit A for every start. Let Λ be the Borel set on which this subsequence is uniformly Cauchy on every integer horizon; PₓΛ=1. Exact additivity of every Aₙ implies ω∈Λ entails θ_sω∈Λ for all real s≥0. The limit therefore has one shift-invariant version, not incompatible exceptional sets chosen separately for each start. It is continuous increasing, adapted and finite. The complement of Λ is null for every start and is included in the initial sigma-field by the usual universal augmentation; setting A=0 there preserves adaptation.

The discounted tail satisfies Eₓ∫ₜ∞\(e^{-s}\)dAₙ=\(e^{-t}\)Pₜuₙ≤\(e^{-t}\)‖u‖∞. Finite-horizon L² convergence and this uniform bound give U₁ᴬ=u. For continuous nonnegative f,g, the Stieltjes integrals ∫f(X)dAₙ converge to ∫f(X)dA. A càdlàg X has at most countably many jumps, and continuous A charges none; the weak-measure convergence criterion for bounded tests with null discontinuity set applies. The L² bound on Aₙ(t) gives UI of expectations.

\[ \int_Eg(x)E_x\int_0^t f(X_s)dA_s\,m(dx)=\int_0^t\int_E(P_sg)(y)f(y)\mu(dy)ds. \]

The identity holds directly for the approximants by m-symmetry. Measures fₙm=nRₙ*μ converge weakly to μ because ∫h fₙdm=∫nRₙh dμ and nRₙh→h uniformly; their masses equal μ(E). Pass to the limit against fPₛg at each s and use the mass bound for time DCT. Monotone classes extend f,g to nonnegative Borel functions. Uniform Pₛg→g for continuous g then gives the small-time Revuz limit.

## 3. Recovering a Measure from an Existing PCAF

<a id="revuz-proof-reverse"></a>

Now let A belong to the class declared in Section 1, with bounded continuous \(u_A\)=U₁ᴬ. Then E_mA₁≤e∫\(u_A\) dm<∞. Starting from m gives stationarity, and additivity makes the expected charge measure f(Xₛ)dAₛ translation invariant in time. Consequently E_m∫₀ᵗf(Xₛ)dAₛ=t\(\mu_A\)(f), with \(\mu_A\)(f)=E_m∫₀¹f(Xₛ)dAₛ. MCT on indicators makes \(\mu_A\) a finite Borel measure. Finite Borel measures on compact metric spaces are Radon by the tight-regularity result of Chapter 8.

To recover a potential for each start, do not assume dA independent of the past. Put \(\nu_h\)(dx)=h^{-1}EₓA_h m(dx); its mass is \(\mu_A\)(E). Partition [0,T] into h-cells and replace ∫f(Xₛ)dAₛ by left-endpoint f(\(X_{kh}\)) times the A-increment. Càdlàg paths and atomless A give pathwise convergence, dominated by 2‖f‖∞A_T. Stationarity makes the expected sum Nh\(\nu_h\)(f), with a remainder bounded by h‖f‖∞\(\mu_A\)(E). Thus \(\nu_h\) converges weakly to \(\mu_A\). This time-averaged argument avoids an unjustified UI assertion for A_h/h.

Multiply the same grid sum by g(X₀). Given \(X_{kh}\), Markov and additivity identify the future A-increment; m-symmetry moves the initial g to \(P_{kh}g\). The expected sum is h∑ν_h(f\(P_{kh}g\)). For continuous f,g, Feller strong continuity makes s↦fPₛg continuous in C(E). Bounded masses and weak convergence therefore give ∫₀ᵀ\(\mu_A\)(fPₛg)ds. To justify the moving tests, first approximate s by a fixed coarse grid uniformly, then take weak limits for finitely many tests. The left side converges by the preceding Stieltjes/DCT argument, proving the two-variable identity of Section 2.

\[ \int_Eg\,u_A\,dm=\int_E R_1g\,d\mu_A=\int_Eg\,R_1\mu_A\,dm,\qquad u_A=R_1\mu_A. \]

Take the time Laplace transform with f=1 and use Tonelli. Full support and continuity extend the m-almost-everywhere potential equality to all starts. If A,B have the same potential u, then Dₜᴬ=∫₀ᵗ\(e^{-s}\)dAₛ satisfies Dₜᴬ+\(e^{-t}\)u(Xₜ)=E[∫₀∞\(e^{-s}\)dAₛ|Fₜ], and likewise for B. Their difference Dᴬ−Dᴮ is a continuous finite-variation true martingale, hence zero by Chapter 31. The functionals are indistinguishable. This also proves that constructing from μ and recovering a measure returns μ itself, not just its total mass.

## 4. Normalization, Singular Measures and the Broader Open Range

<a id="revuz-proof-boundary"></a>

If m is replaced by cm without changing X, the kernel becomes rλ/c and the same A has Revuz measure cμ. One-dimensional Brownian Lᵃ corresponds to δₐ relative to dx and 2δₐ relative to speed 2dx. For reflecting Brownian motion the regulator is K=½L^{0,+}; boundary one-sided band densities and interior symmetric L require separate calculations. An unchecked boundary δ normalization is not used to prove the theorem.

The broad standard formulation allows locally compact state spaces, m-symmetric Hunt processes and capacity associated with a regular Dirichlet form. A smooth μ charges no zero-capacity set and admits a closed nest Fₙ with μ(Fₙ)<∞ whose complements have capacity tending to zero locally on compact sets. PCAFs need only be defined outside a suitable exceptional set of starts, modulo common indistinguishable versions. Here “smooth” means a capacity/nest condition, not a smooth density. General nonsymmetric right processes additionally require an excessive reference measure and the corresponding exceptional-set theory.

This page does not complete approximation of arbitrary such smooth μ by finite-energy nests, common quasi-continuous potential versions and pasting, or show every PCAF automatically has the continuous bounded potential used here. These are substantive remaining proof gaps, recorded separately in T-REVUZ’s scope; they are not merely pending independent review. The theorem actually proved is the two-way correspondence in the exact class of Section 1, with construction, uniqueness and test identities written out. The chapter uses only that scope. Chapter 37 separately supplies the explicit full-line Brownian Radon construction, not a hidden extension of the compact-space theorem.

For terminology and the broader formulation compare the process assumptions, exceptional sets and two-variable identity in §3 of the [author’s public paper](https://www.kurims.kyoto-u.ac.jp/~nkajino/preprints/HTCRBM32a.pdf). Its citation of the general correspondence does not replace the broader proof still missing here. Return to [the correspondence in the chapter](../chapters/38-feynman-kac.md#revuz-correspondence).
