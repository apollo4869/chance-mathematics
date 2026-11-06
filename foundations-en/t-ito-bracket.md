# T-ITO-BRACKET: Squares, Compensation and Integration for Continuous Martingales

This page supplies the longer proofs for Chapter 31. The filtration satisfies the usual conditions, and martingales start at zero except in the final initial-value discussion. Prerequisites are only Doob inequalities from Chapter 15, bounded sampling from Chapter 16, the class D decomposition and predictable finite-variation uniqueness from Chapter 30, and completeness from T-LP. Discrete identities are not applications of the Itô formula of Chapter 32.

<a id="t-ito-bounded"></a>

## 1. Bounded Continuous Martingales: Constructing Variation from Finite Sums

Fix finite T and a continuous martingale M with |M|≤c. For a deterministic partition π, multiply each increment, stopped at the current time, by the left endpoint value of M to obtain a continuous martingale Jᵖ. Include the unfinished current interval in Qᵖ. Finite algebra gives the exact identity.

\[ J^\pi_t=\sum_i M_{t_i}(M_{t\wedge t_{i+1}}-M_{t\wedge t_i}),\qquad Q^\pi_t=\sum_i(M_{t\wedge t_{i+1}}-M_{t\wedge t_i})^2=M_t^2-2J^\pi_t. \]

Bounded sampling and conditional orthogonality make Jᵖ a genuine martingale and give the terminal estimates below. No general continuous-martingale integral is being used: we only cancel cross terms in finite sums.

\[ E(J^\pi_T)^2=E\sum_i M_{t_i}^2(\Delta_iM)^2\le c^2 E M_T^2\le c^4,\qquad \|Q^\pi_T\|_2\le \|M_T^2\|_2+2\|J^\pi_T\|_2\le3c^2. \]

Compare π and η on their common refinement r. The difference of their left endpoint coefficients is bounded by the oscillation \(\omega_M(\delta)\), where δ=max(|π|,|η|). Discrete orthogonality followed by Cauchy–Schwarz gives

\[ E|J^\pi_T-J^\eta_T|^2\le E[\omega_M(\delta)^2 Q^r_T]\le3c^2\bigl(E\omega_M(\delta)^4\bigr)^{1/2}\longrightarrow0. \]

Continuity makes the oscillation vanish pathwise, and boundedness permits dominated convergence. Doob’s L² maximal inequality upgrades terminal Cauchy convergence to Cauchy convergence in the L² maximal norm over the interval. The limit J has a continuous adapted martingale version: take a subsequence with summable maximal-norm errors for almost sure uniform convergence, then pass conditional expectations through L² limits. The whole sequence converges to the same J, not merely an unidentified subsequential limit.

Consequently Q=M²−2J is continuous and Qᵖ converges to Q in the L² maximal norm. Qᵖ need not increase at every time because the square on the unfinished interval can decrease. Removing that interval gives an increasing step function differing by at most \(\omega_M(|\pi|)^2\). Passing to the uniformly convergent subsequence proves that Q increases. It starts at zero, is adapted and continuous, hence predictable, and has integrable terminal value.

Independently define A as the predictable compensator of the bounded submartingale M² using Chapter 30. Since M²=2J+Q is another decomposition satisfying all the conditions, uniqueness gives indistinguishability of A and Q. This proves continuity of A and convergence of square sums to it. We never assumed an enumeration of jumps of A by predictable stopping times.

<a id="t-ito-local-bracket"></a>

## 2. Removing Boundedness and Specifying Partitions and Convergence

For a square-integrable M on [0,T], first verify that M² is class D: conditional Jensen and closed-martingale sampling give Mτ²≤\(E[M_T^2\mid\mathcal F_\tau]\) at every bounded stop τ. The right side consists of conditional averages of one integrable terminal value and is uniformly integrable. Chapter 30 therefore really applies, defining A=⟨M⟩.

Before continuity of A is known, predictability of its stopped process needs justification. Pullbacks of predictable rectangles show that deterministic stopping preserves predictability. For a rectangle H=ξ1_(s,t], the pathwise Stieltjes integral is ξ times the difference of two deterministic stops of A, hence predictable. Using A as total integral, the π–λ theorem and monotone convergence extend this to all nonnegative predictable H. Since 1_(0,σ] is left-continuous and adapted, it is predictable; its integral against dA is precisely stopped A. This uses pathwise integration, not the martingale integral being constructed.

Let \(\sigma_c\) be the first time |M| reaches c, capped at T. Continuity makes the stopped process bounded. Stopping M²−A at \(\sigma_c\) preserves the martingale property, and stopped A remains predictable, increasing and terminally integrable. Uniqueness identifies it with the stopped process’s compensator. Section 1 makes each stopped compensator continuous. Each continuous path is bounded on [0,T], so eventually it is not stopped early. Thus A is continuous, and L² maximal convergence after stopping yields ucp convergence of the original square sums.

\[ P\!\left(\sup_{t\le T}|Q^{\pi_n}_t-A_t|>\varepsilon\right)\le P(\sigma_c<T)+P\!\left(\sup_{t\le T}|Q^{\pi_n}(M^{\sigma_c})_t-A^{\sigma_c}_t|>\varepsilon\right). \]

First fix c and refine the mesh, then send c to infinity. For deterministic partitions E \(Q^\pi_T\)=E \(M_T^2\)=E \(A_T\), and \(Q^\pi_T\) is nonnegative. Convergence in probability together with equality of means gives L¹ convergence: from any subsequence take an almost surely convergent subsubsequence, apply dominated convergence to min(\(Q^\pi_T\),\(A_T\)), and expand the absolute difference. A general square-integrable M thus gives ucp and fixed-terminal-time L¹ convergence, not an unproved L² maximal conclusion.

For a continuous local martingale, localize at exits from ±c. A bounded stopped local martingale is a genuine martingale by conditional dominated convergence along the original localizing times. Uniqueness makes the stopped brackets consistent, producing a continuous increasing A finite pathwise on compact intervals; square sums still converge ucp. E \(A_T\) may now be infinite.

The deterministic grids need not be nested. The stopping-partition version means 0=τ₀≤⋯≤τₘ=T, with a deterministic finite m for each partition, bounded stopping times τᵢ, and maximal gap tending to zero in probability. Repeated points are permitted; zero-length intervals contribute nothing.

For τ≤τ′ and bounded Fτ-measurable ξ, the finite process ξ(M stopped at τ′ minus M stopped at τ) really is a martingale. Given s<t, on {τ≤s} use conditional means of stopped martingales. On {τ>s}, for every C∈Fₛ the event C∩{τ>s} belongs to Fτ; apply bounded sampling between τ and η=(t∨τ)∧τ′. Both pieces have conditional increment mean zero. Thus random-interval integration has not been used to prove its own construction.

Conditional orthogonality of stopped increments gives the same 3c² estimate as in Section 1. The ordered union of two finite stopping grids consists of stopping times; its coefficients are measurable at the current stopping information, and their difference is controlled by oscillation at random δ. Convergence δ→0 in probability implies convergence of this oscillation in probability, and boundedness gives \(E\omega_M(\delta)^4\)→0. Doob then yields ucp. Future-selected nonstopping partition points are not covered.

<a id="t-ito-covariation"></a>

## 3. Bilinearity and Finite Variation of Covariation Are Not Formal Guesses

For continuous local martingales M,N, localize jointly and define cross variation from the limits of cross sums. A finite identity gives the polarization formula below. The cross sums themselves are bilinear term by term, so their ucp limits are bilinear. For square-integrable M,N, MN−C is a genuine martingale because it is a linear combination of two compensated square processes.

\[ C=[M,N]=\frac14\bigl([M+N]-[M-N]\bigr),\qquad C=\langle M,N\rangle. \]

Outside a common null set, increments of A(M+aN) are nonnegative for every rational a and rational interval. Bilinearity, continuity and rational density make the quadratic expression below nonnegative for every real a and every interval. This gives interval Cauchy–Schwarz; applying finite-sum Cauchy–Schwarz over partitions gives the pathwise total-variation bound.

\[ \Delta A(M)+2a\,\Delta C+a^2\Delta A(N)\ge0,\qquad |\Delta C|^2\le\Delta A(M)\Delta A(N),\qquad \operatorname{Var}(C)_T\le\sqrt{A(M)_T A(N)_T}. \]

The integral version also requires proof. On each path use dD=dA(M)+dA(N) as a dominating measure. Positivity of the interval quadratic expression extends to Borel sets, and its Radon–Nikodym densities a,b,c satisfy c²≤ab. For measurable H,K, the density bound followed by integral Cauchy–Schwarz yields

\[ \int_0^T|HK|\,|dC|\le\left(\int_0^T H^2\,dA(M)\right)^{1/2}\left(\int_0^T K^2\,dA(N)\right)^{1/2}. \]

Only pathwise densities are needed to prove the inequality; no unproved joint choice of a random density is assumed. Taking expectations uses ordinary Cauchy–Schwarz. In particular brackets are stable under terminal L² convergence: write A(X)−A(Y)=⟨X−Y,X+Y⟩ to obtain

\[ E\sup_{t\le T}|A(X)_t-A(Y)_t|\le\|X_T-Y_T\|_2\,\|X_T+Y_T\|_2. \]

<a id="t-ito-clock-integral"></a>

## 4. Complete Extension of Integration on a Random Clock

For continuous square-integrable M with A=⟨M⟩, define the finite measure \(m_M(E)=E\int_0^T\mathbf1_E\,dA\) on the predictable σ-algebra. Measurability of path integrals is checked on rectangles and extended by the nonnegative functional monotone class theorem. Its total mass is E \(A_T\)=E \(M_T^2\).

Bounded elementary predictable processes are dense in \(L^2(m_M)\). The algebra obtained by finite set operations on deterministic rectangles generates P. Let D consist of sets whose indicators belong to the L² closure of these simple functions. It contains the full space and is closed under complements. For disjoint unions use finite partial sums and L² tail convergence under the finite measure. Thus D is a λ-system containing the generating rectangle π-system, and the π–λ theorem of T-MCLASS gives D=P. Truncate a general L² function and approximate it by steps. Every algebra-simple function can be expressed on a common deterministic grid with bounded coefficients measurable at left endpoints. Time zero has no mass, since A₀=0 and A is continuous.

Define I(H) by finite sums for elementary H. Conditional orthogonality and the martingale identity for M²−A give the isometry. The same argument applies at non-grid terminal times by cutting the current interval.

\[ E I_T(H)^2=E\sum_i H_i^2(\Delta_iM)^2=E\sum_i H_i^2\Delta_iA=E\int_0^T H^2\,dA. \]

Approximate in \(L^2(m_M)\). Doob’s L² estimate gives a limit in the L² maximal norm of continuous martingales. It is adapted, continuous and a genuine martingale; it is independent of the approximations and preserves the isometry. Completeness of this process space uses the summable-maximal-norm subsequence argument already proved in the Brownian construction in Chapter 31, not a future integration theorem.

<a id="t-ito-stopping"></a>

## 5. Stopping and Localization Must Commute with Extension

First take elementary H and a stopping time τ with values in a deterministic finite grid, refining to a common grid. Multiplying a coefficient by 1{τ>left endpoint} still uses left-endpoint information, and finite sums give the stopping identity below. Energy approximation extends it to general H because stopping decreases the energy error. The process 1_(0,τ] is left-continuous and adapted, hence remains in the predictable integration domain. For arbitrary τ≤T, replace it by finite-grid stopping times τₙ decreasing from the right. The left side converges pathwise uniformly by continuity of the integral. On the right, integrability of H² for m_M, decreasing indicators 1{s≤τₙ}, and the isometry give L² maximal convergence. The identity therefore holds for general τ.

\[ (H\mathbin{\cdot}M)_{t\wedge\tau}=\bigl(H\mathbf1_{(0,\tau]}\mathbin{\cdot}M\bigr)_t,\qquad \langle M^\tau\rangle=\langle M\rangle^\tau. \]

The bracket identity follows from preservation of predictability under stopping and uniqueness of the Chapter 30 decomposition; it is not merely a symbolic rule. Using the stopped integrator and stopping the integrand consequently agree: first check finite sums for elementary H, then extend with the same energy norm on both sides.

Let M be a continuous local martingale and H predictable, with ∫H²dA finite almost surely on each finite T. Its accumulated energy Cₜ=∫₀ᵗH²dA is continuous, adapted and increasing: on [0,t], first check Fₜ measurability of integrals for predictable rectangles and then extend by the nonnegative functional monotone class theorem. Continuity of A makes its measure atomless, and locally finite total energy gives continuity of C. Let ρₙ be the minimum of time n, the first time |M| reaches n, and the first time C reaches n. These are stopping times and ρₙ↑∞ almost surely.

After stopping, M is bounded and energy is at most n, so every localized integral belongs to the established L² theory. The stopping identity makes them agree on overlaps, giving a unique continuous local martingale up to indistinguishability. A common refinement and the same stopping identity give independence of the localization sequence. Almost surely finite energy has not been confused with finite expected energy.

<a id="t-ito-transform"></a>

## 6. How Integration Changes Brackets and Covariation

For elementary H, check interval by interval. The integral starts from its past value, and its next increment is \(H_i\) times the increment of M. In a square expansion the linear term has conditional mean zero, while M²−A compensates the squared term. Thus I(H)²−∫H²dA is a martingale, and the accumulated integral is continuous, increasing and predictable. Doob–Meyer uniqueness gives the bracket formula, without using Itô formula.

The elementary conditional calculation can be made explicit. Within a cell Iᵤ=Iₐ+ξ(Mᵤ−Mₐ); the linear term has conditional mean zero and M²−A compensates the square. Integrability follows from L² integrability of Iₐ and Mᵤ and bounded ξ. Repeating the calculation for arbitrary endpoints within a cell and concatenating gives a process martingale identity.

\[ E[I_b^2-I_a^2\mid\mathcal F_a]=E[\xi^2(A_b-A_a)\mid\mathcal F_a]. \]

For general H, approximate by elementary Hⁿ in the energy L² norm. Bracket stability from Section 3 gives convergence of the left side in the L¹ maximal norm; Cauchy–Schwarz sends E∫|(Hⁿ)²−H²|dA to zero. The identity survives the limit. For different integrators, check elementary processes using MN−⟨M,N⟩, then control errors on both sides with the integral inequality from Section 3.

\[ \langle H\mathbin{\cdot}M\rangle_t=\int_0^t H^2\,d\langle M\rangle,\qquad \langle H\mathbin{\cdot}M,K\mathbin{\cdot}N\rangle_t=\int_0^t HK\,d\langle M,N\rangle. \]

Apply the proved formulas up to ρₙ and patch for the local case. Integration is also associative: K·(H·M)=(KH)·M whenever the corresponding local energy conditions hold. For elementary K this follows by calculating interval increments. The displayed bracket identity makes the approximation errors for general K have exactly the same energy norm on both sides, so isometry and localization extend the identity. This is consistency of the construction, not ordinary algebra with stochastic differentials.

<a id="t-ito-progressive"></a>

## 7. Predictable Representatives of Progressive Rules for the Brownian Clock

The Brownian integral depends only on the dt·P equivalence class of the integrand; it does not require a continuous version with matching point values everywhere. If H is progressive and E∫H²dt is finite, extend it by zero to negative times and average only past values. Fubini gives locally integrable H paths almost surely. The averages are continuous and adapted, hence predictable.

\[ H^{(n)}_t=n\int_{(t-1/n)^+}^t H_s\,ds,\qquad \|H^{(n)}-H\|_{L^2(P\,dt)}\longrightarrow0. \]

For the convergence, prove L² continuity of time translation first for finite rectangular simple functions, then extend by density and contraction of zero-extended translations; apply Minkowski to the past averages. Completeness of predictable L² gives a predictable representative equal to H dt·P-almost everywhere. This proof does not invoke general measurable projection and cannot be transferred without proof to an atomic random clock.

Finally, for square-integrable M with nonzero initial value, subtract the F₀-measurable M₀. The two square processes differ by 2M₀(M−M₀)+M₀². Truncate M₀ and use L² Cauchy–Schwarz for L¹ passage to prove this is a martingale. The bracket is unchanged, and integration uses only increments. The statements starting from zero therefore cover general square-integrable initial values.

<a id="t-ito-singular-clock"></a>

## 8. How a Null Set of Ordinary Time Can Carry All Integral Energy

Take independent fair Bernoulli variables ξₖ and let Y be the series below, with law ν. It is supported on the standard Cantor set C, which has length zero; see the [measure proof](t-measure.md). Each n-digit prefix corresponds to a closed interval of mass 2⁻ⁿ, and these intervals are separated. The mass of any point is at most 2⁻ⁿ for every n, hence zero. Thus ν is atomless, its CDF c is continuous, and c(0)=0, c(1)=1.

\[ Y=\sum_{k\ge1}2\xi_k3^{-k},\qquad c(t)=\nu([0,t]),\qquad \nu(C)=1,\quad |C|=0. \]

Extend c constantly as one after time one. Use the usual augmentation of the Brownian natural filtration and set Gₜ=\(\mathcal F^B_{c(t)}\). It contains all original null sets and their subsets, so it is complete. If c is locally constant to the right of t, right continuity of G is immediate. Otherwise choose uₙ↓t with c(uₙ)>c(t); continuity of c and right continuity of the original filtration identify the intersection of F^B_{c(uₙ)} with F^B_{c(t)}. Thus G is right-continuous as well. The deterministic c has not been mistaken for a random stopping time.

The process Mₜ=\(B_{c(t)}\) is continuous and G-adapted. Brownian increments at deterministic times remain independent of the past after usual augmentation. Both conditional identities below hold, and E Mₜ²=c(t)≤1. The process c is deterministic, continuous, increasing, starts at zero and is G-predictable. On finite horizons M² is class D, so Doob–Meyer uniqueness gives ⟨M⟩=c, rather than assuming a formal time-change rule.

\[ E[M_t\mid\mathcal G_s]=M_s,\qquad E[M_t^2\mid\mathcal G_s]=M_s^2+c(t)-c(s),\qquad s\le t. \]

The deterministic Borel process H=\(\mathbf1_C\) is predictable: choose Ω as the event in predictable rectangles, and use that (a,b] and {0} generate all time Borel sets. The measure dc is atomless and zero off C; there is no atom at zero either, so integrating over (0,t] leaves the conclusion unchanged. Thus H equals one dc-almost everywhere, whereas it equals zero dt-almost everywhere. Null sets for the two measures cannot be interchanged.

For every finite integer T, isometry and Doob's maximal estimate give the zero error below. Take the countable union of these null sets and use continuous integral versions. Then H·M and 1·M=M are indistinguishable: outside one null set equality holds for every t. Since M₁ has variance one, this is genuinely a nonzero process.

\[ E\sup_{t\le T}|((H-1)\mathbin{\cdot}M)_t|^2\le4E\int_0^T|H_s-1|^2\,dc(s)=0. \]

\[ \int_0^1 H_s^2\,ds=0,\qquad \int_0^1 H_s^2\,dc(s)=1,\qquad (H\mathbin{\cdot}M)_t=(1\mathbin{\cdot}M)_t=M_t. \]

Return to [Chapter 31](../chapters/31-ito-integral.md#martingale-bracket). The proved scope is continuous (local) martingales. General jump semimartingales, the full BDG range and Itô formula are not being claimed here.
