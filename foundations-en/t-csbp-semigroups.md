# T-CSBP-SEMIGROUPS: Continuous-State Branching from Reproduction Approximations

Return to [Chapter 58](../chapters/58-multifurcation.md). We establish transition semigroups, Feller processes and extinction for finite-mean critical/subcritical mechanisms, without equating population semigroups with full genealogy.

## 1. Mechanisms and discrete offspring laws

<a id="cb-mechanism"></a>

\[ \psi(q)=a q+\beta q^2+\int_0^\infty(e^{-qr}-1+qr)\,\pi(dr),\quad a,\beta\ge0,\quad \int_0^\infty(r^2\wedge r)\,\pi(dr)<\infty. \]

Assume \(\psi\) is nonlinear and satisfies Grey’s condition \(\int_1^\infty dq/\psi(q)<\infty\). Then \(\psi\) increases strictly to infinity and \(\psi(q)/q\to\infty\). Put \(\phi=\psi^{-1}\), \(v_\lambda=\phi(\lambda)\) and \(c_\lambda=\psi'(v_\lambda)>0\), and define

\[ g_\lambda(s)=s+\frac{\psi(v_\lambda(1-s))}{v_\lambda c_\lambda},\quad 0\le s\le1. \]

This is a genuine offspring pgf. Its constant term is \(p_0=\lambda/(v_\lambda c_\lambda)>0\), its linear term is \(p_1=0\), its quadratic term is \(\beta v_\lambda/c_\lambda+(v_\lambda/(2c_\lambda))\int r^2e^{-v_\lambda r}\pi(dr)\), and for j≥3 its coefficient is \((v_\lambda^{j-1}/(c_\lambda j!))\int r^j e^{-v_\lambda r}\pi(dr)\). All are nonnegative; taking s↑1 gives sum 1. The mean is \(1-a/c_\lambda\le1\). Tonelli justifies the nonnegative series; the stated moments ensure finite integrals.

Let each individual die at rate \(c_\lambda\) and reproduce with pgf \(g_\lambda\). Construct the GW tree by generations first. Its mean is at most one, with \(p_0>0,p_1=0\), so Chapter 20 gives a finite tree almost surely. Independent exponential lifetimes therefore cause no finite-time explosion. We use finitely many ancestors; this is not a blanket inference from finite expected population to nonexplosion.

## 2. Existence of the Laplace kernel

<a id="cb-kernel"></a>

For one ancestor let \(F_t^\lambda(s)\) be the population pgf at time t. Conditioning on its first lifetime gives a bounded renewal equation and hence \(\partial_tF=c_\lambda(g_\lambda(F)-F)\), \(F_0=s\). Direct substitution gives the exact identity

\[ v_\lambda(1-F_t^\lambda(e^{-q/v_\lambda}))=u_t(v_\lambda(1-e^{-q/v_\lambda})),\qquad \partial_tu_t(q)=-\psi(u_t(q)),\quad u_0(q)=q. \]

The ODE has a unique global solution in \([0,q]\): \(\psi\) is locally Lipschitz, and the solution decreases without crossing zero. Starting with \(\lfloor xv_\lambda\rfloor\) ancestors, the Laplace transform \(F_t^\lambda(e^{-q/v_\lambda})^{\lfloor xv_\lambda\rfloor}\) of population divided by \(v_\lambda\) converges to \(e^{-xu_t(q)}\). The discrete laws on \([0,\infty)\) are tight by their mean bound x and Markov’s inequality. The limiting Laplace transform tends to 1 as q↓0, excluding escape to infinity. Laplace uniqueness gives a unique probability kernel \(P_t(x,\cdot)\). The same argument proves weak continuity in x and t, hence kernel measurability.

\[ \int e^{-qy}P_t(x,dy)=e^{-xu_t(q)},\qquad P_{s+t}=P_sP_t,\qquad P_t(x+x',\cdot)=P_t(x,\cdot)*P_t(x',\cdot). \]

The last two identities follow from composition of the ODE flow and uniqueness of products of Laplace transforms. They establish Chapman–Kolmogorov and branching. A formal Laplace expression without an established probability kernel would not suffice.

## 3. Feller realization and generator

<a id="cb-feller"></a>

On \(C_0([0,\infty))\), finite linear combinations of \(e^{-qx},q>0\), are dense: put y=e^{-x} and approximate functions on [0,1] by polynomials vanishing at y=0. For exponentials, \(P_te^{-qx}=e^{-xu_t(q)}\in C_0\), and convergence to \(e^{-qx}\) as t↓0 is uniform since u→q>0 and \(\sup_x x e^{-cx}<\infty\). Positive contraction extends these assertions to all \(C_0\). Chapter 28’s Feller realization theorem supplies nonnegative càdlàg strong Markov paths. Its independent final review remains open; here its strong continuity, conservation and locally compact Polish-state hypotheses have been verified.

\[ \mathcal A e^{-qx}=x\psi(q)e^{-qx}. \]

The generator derivative holds in \(C_0\)-norm: the ODE has a second-order time error \(O(t^2)\), while \(x^2e^{-cx}\) is bounded. The explicit Laplace flow uniquely determines all transition kernels. This does not say that a formal operator without a domain always determines a process. Zero is absorbing because \(P_t(0)=\delta_0\).

## 4. Extinction, stable mechanisms and scaling

<a id="cb-extinction"></a>

Bounded convergence from \(e^{-qZ_t}\downarrow\mathbf1_{\{Z_t=0\}}\) gives \(P_x(Z_t=0)=e^{-xv(t)}\), with \(v(t)=u_t(\infty)\) and \(\int_{v(t)}^\infty dq/\psi(q)=t\). Grey’s condition makes v finite for every t>0. In the critical/subcritical case v(t)↓0, so absorption at some finite time has probability one. Without Grey, interpret \(v(t)=\infty\): for \(\psi(q)=aq\), \(Z_t=xe^{-at}>0\) only approaches zero.

\[ \psi(q)=q^\alpha,\quad1<\alpha\le2:\quad
u_t(q)=\big(q^{1-\alpha}+(\alpha-1)t\big)^{-1/(\alpha-1)},\quad
v(t)=((\alpha-1)t)^{-1/(\alpha-1)}. \]

For c>0, \(cZ_{c^{1-\alpha}t}\) has the same transition law started at cx, as verified in every finite-dimensional kernel by the Laplace formula. At α=2 the generator is \(\mathcal A f=xf''\) on smooth compactly supported tests, from discrete generators or the Laplace determining class. For α<2 the Lévy measure is \(\pi(dr)=\alpha(\alpha-1)r^{-1-\alpha}dr/\Gamma(2-\alpha)\). Two integrations by parts yield \(\int(e^{-qr}-1+qr)r^{-1-\alpha}dr=\Gamma(2-\alpha)q^\alpha/(\alpha(\alpha-1))\); endpoint terms vanish for 1<α<2.

Public basis: [Duquesne–Winkel, Growth of Lévy trees](https://perso.lpsm.paris/~tduquesne/Documents/Duquesne_Winkel_PTRF_2007.pdf), PTRF139(2007),313–371, Sections 1 and 4. We reconstruct the argument using the book’s Feller realization; this is not claimed to reproduce their entire proof route. Supercritical, infinite-mean and complete CSBP classification results are outside the proved scope.
