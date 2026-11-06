# T-PALM: Constructing Campbell Measures and Palm Kernels

Return to [Chapter 50](../chapters/50-palm-gibbs.md#palm-disintegration). E is LCSC metric, \(\Xi\) is a nonnegative random Radon measure, and Z is an environment mark in a standard Borel space S. One may take Z=Ξ; the original probability space need not be standard Borel. We use Chapter 10 disintegration, joint integration from T-MASS-KERNELS, and the evaluation structure of T-RADON-SPACE.

## 1. First Construct a Joint Measure

<a id="palm-campbell-construction"></a>

For nonnegative jointly measurable g define \(Cg=\mathbb E\int g(x,Z)\Xi(dx)\). T-MASS-KERNELS, first on finite compact windows and rectangles and then by monotone classes, makes the integral a random variable. MCT gives countable additivity in g. Thus C is a measure on E×S without a prior Palm kernel. Its first marginal is \(\nu(A)=\mathbb E\Xi(A)\). If ν is σ-finite, partition E into Aⱼ with ν(Aⱼ)<∞; then C(Aⱼ×S)<∞, so C is σ-finite.

Local finiteness of realizations cannot replace σ-finiteness of the marginal. For example, let Ξ=Zdx on the line, with Z finite almost surely and EZ=∞. Then ν is infinite on every positive-length set and is not σ-finite. The full Campbell measure can nevertheless be σ-finite on compact windows crossed with {Z≤n}. A σ-finite joint measure need not have a σ-finite marginal or admit probability disintegration relative to that marginal. The existence theorem below explicitly assumes σ-finite ν.

## 2. Disintegrate After Finite Weighting

<a id="palm-kernel-construction"></a>

For nonzero σ-finite ν choose positive finite w with \(0<c=\nu w<\infty\), for example \(w=2^{-j}/(1+\nu A_j)\) on Aⱼ. Then \(\widetilde C(dx,dz)=w(x)C(dx,dz)/c\) is a probability with first marginal wν/c. Chapter 10 gives a probability kernel Qₓ with \(\widetilde C=(w\nu/c)Q\). Multiplying a nonnegative g by c/w and using MCT gives

\[ \mathbb E\int g(x,Z)\Xi(dx)=\int_E\int_Sg(x,z)Q_x(dz)\nu(dx). \]

This is the Palm probability kernel of the environment Z. If ν=0, every compact-exhaustion mass has expectation zero; a common null set gives Ξ=0 almost surely. Any fixed probability kernel then satisfies the vacuous identity. For two kernels satisfying the identity, compare event integrals on finite ν-pieces, combine the exceptional sets for a countable generating π-class of S, and use uniqueness of probabilities for every Borel event. Outside one common ν-null set, the kernels agree as whole probabilities. They are not uniquely prescribed at every x.

## 3. Deleting Exactly One Occurrence

<a id="palm-delete-one"></a>

Now let Ξ be an integer point measure, with S=\(\mathcal M_p(E)\) and Z=Ξ. Addition \((x,\eta)\mapsto\eta+\delta_x\) is evaluation-measurable. Deletion is defined only on \(D=\{(x,\eta):\eta\{x\}\ge1\}\). Using the compatible proper metric from Chapter 48, \(\eta\{x\}=\lim_n\eta(B(x,1/n))\), and joint kernel integration makes D measurable. On D, compact-window evaluations after deletion are \(\eta(A)-\mathbf1_A(x)\), making deletion measurable. Infinite evaluations use ∞−1=∞; outside D assign the zero configuration.

The Campbell measure is concentrated on D, since every occurrence is present at its own location. Finite ν-pieces and disintegration give \(Q_x\{\eta:\eta\{x\}\ge1\}=1\) for ν-almost every x; joint measurability legitimizes this x-dependent event. Define the reduced kernel \(Q_x^!=Q_x\circ(\eta\mapsto\eta-\delta_x)^{-1}\), fixing a common version at exceptional x. Then \(C^!(dx,d\eta)=\nu(dx)Q_x^!(d\eta)\), and

\[ \mathbb E\int g(x,\Xi-\delta_x)\Xi(dx)=\int_E Q_x^!g(x,\cdot)\,\nu(dx). \]

If η has multiplicity k at x, deletion leaves k−1. Restricting η to E∖{x} removes all k units and is a different operation. General random mass still has the Palm kernel of the preceding section, but unit deletion is not defined without integer occurrence structure.

## 4. Translations, Stationarity, and a Palm Distribution

<a id="palm-stationary"></a>

On \(\mathbb R^d\) define \(\theta_x\eta(A)=\eta(A+x)\). For \(f\in C_c\), \((\theta_x\eta)f=\int f(y-x)\eta(dy)\). If xₙ→x and ηₙ converges vaguely to η, the shifted tests have a common compact support and converge uniformly. Local mass bounds give convergence of their integrals. The translation action is jointly continuous and hence jointly measurable.

Let Ξ be stationary with \(\nu=\lambda dx\), \(0<\lambda<\infty\), and define the centered Campbell measure by \(C^0g=\mathbb E\int g(x,\theta_x\Xi)\Xi(dx)\). For a fixed environment event D, the measure \(A\mapsto C^0(A\times D)\) is translation invariant by stationarity and bounded by λ|A|. Haar uniqueness from Chapter 45 makes it a constant multiple of dx. For any bounded Borel B with 0<|B|<∞, \(P^0(D)=C^0(B\times D)/(\lambda|B|)\) is a probability independent of B. Rectangular π–λ and MCT give

\[ \mathbb E\int g(x,\theta_x\Xi)\Xi(dx)=\lambda\int_{\mathbb R^d}\int g(x,\eta)P^0(d\eta)\,dx. \]

This also gives the noncentered kernel \(Q_x=\mathcal L(\theta_{-x}\eta),\ \eta\sim P^0\), a measurable version defined for every x. For a point process, P⁰ gives η{0}≥1 almost surely, and η{0}=1 if the process is simple. For general random mass, P⁰ need not have an atom at zero: deterministic length measure has the same length measure as its Palm version. Finite positive intensity permits probability normalization. At λ=0 the process is empty; at λ=∞ the formula cannot be normalized in this way.
