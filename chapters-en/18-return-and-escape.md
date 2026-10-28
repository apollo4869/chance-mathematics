# Chapter 18: Why Do Some Random Walks Return While Others Escape?

A step left and a step right leave no preferred direction on average. Yet on a three-dimensional lattice, a walker with no directional preference at any step has positive probability of never revisiting its starting point.

Chapter 4's scaling picture does not answer this question. There, many tiny steps were compressed into a finite time window. Here step size stays fixed while time extends indefinitely. We count not the final position, but how often the same place will be seen again.

## 18.1 Being able to return is not returning

For a countable-state Markov chain started at \(i\), define the first positive-time return

\[
T_i=\inf\{n\ge1:X_n=i\},\qquad f_i=P_i(T_i<\infty).
\]

The state \(i\) is recurrent if \(f_i=1\), and transient if \(f_i<1\). Starting the return rule at 1 matters: otherwise the initial visit would make the probability identically one and erase the question.

Let \(N_i=\sum_{n\ge0}\mathbf1_{\{X_n=i\}}\), counting the initial visit. The discrete strong Markov property of Chapter 17 makes the probability of another return after each return equal to \(f_i\). Induction at successive returns gives

\[
P_i(N_i\ge k)=f_i^{k-1},\qquad
E_iN_i=\sum_{k\ge1}f_i^{k-1}.
\]

A recurrent state is therefore visited infinitely often almost surely. A transient state has finitely many visits almost surely, with mean \(1/(1-f_i)\). For a general random variable infinite mean need not imply an almost surely infinite value; the geometric restart structure makes them equivalent here.

## 18.2 An infinite series records the fate of one place

Define the Green kernel

\[
G(i,j)=\sum_{n=0}^\infty p^{(n)}_{ij}=E_i\sum_{n\ge0}\mathbf1_{\{X_n=j\}}.
\]

Tonelli for nonnegative integrals gives the last equality. Consequently

\[
G(i,i)=\infty\ \Longleftrightarrow\ f_i=1,\qquad
G(i,i)=\frac1{1-f_i}\quad(f_i<1).
\]

If \(H_j\) is the first hit of \(j\), including time zero, strong Markov also gives \(G(i,j)=P_i(H_j<\infty)G(j,j)\) as a nonnegative extended integral. When the probability is zero, interpret the right side as zero, not an undefined \(0\cdot\infty\). Split over the hitting event and then accumulate future visits by monotone convergence to prove the identity.

Thus probabilities at fixed times can together answer a question about an infinite path. We use more than one marginal: the renewal relation after returns supplies the extra structure.

## 18.3 First returns split all returns into cycles

Put \(u_n=P_i(X_n=i)\) and \(a_k=P_i(T_i=k)\). Splitting according to first return gives

\[
u_0=1,\qquad u_n=\sum_{k=1}^na_ku_{n-k}\quad(n\ge1).
\]

For \(0\le z<1\) the series converge absolutely. Their generating functions satisfy \(U(z)=1+A(z)U(z)\), hence \(U(z)=1/(1-A(z))\). Letting \(z\uparrow1\) recovers the Green criterion. The first-return law may be defective: total mass below one records paths with no next cycle.

This renewal equation will begin the next chapter. For now, another readout of \(u_n\) will show how dimension changes the series.

## 18.4 How a Fourier readout selects the origin

Consider simple symmetric nearest-neighbor walk on \(\mathbb Z^d\). Each independent step chooses uniformly among \(2d\) directions. Its characteristic function is

\[
\phi(\theta)=\frac1d\sum_{j=1}^d\cos\theta_j,
\qquad\theta\in[-\pi,\pi]^d.
\]

For every integer vector \(k\), multiplying the coordinate exponential integrals yields

\[
(2\pi)^{-d}\int_{[-\pi,\pi]^d}e^{i\theta\cdot k}\,d\theta
=\mathbf1_{\{k=0\}}.
\]

Take expectation at the random position and use bounded Fubini to obtain \(u_n=(2\pi)^{-d}\int\phi(\theta)^n\,d\theta\). No general local CLT is required, and weak convergence has not been substituted for a point-probability estimate.

## 18.5 Discount infinite time before summing it

The powers \(\phi^n\) may have either sign, so summing them under an integral needs justification. First take \(0<r<1\). The absolute sum is bounded by \(1/(1-r)\), giving

\[
G_r(0,0)=\sum_{n\ge0}r^nu_n
=(2\pi)^{-d}\int_{[-\pi,\pi]^d}\frac{d\theta}{1-r\phi(\theta)}.
\]

Discounting addresses two different difficulties. To exchange summation and integration we use

\[
\sum_{n\ge0}\int_{[-\pi,\pi]^d}|r^n\phi(\theta)^n|\,d\theta
\le\frac{(2\pi)^d}{1-r}<\infty.
\]

When removing the discount, the integrand is not increasing with \(r\) everywhere: it decreases on the negative-readout region. Separating the two signs lets monotone convergence handle a possibly infinite singularity and dominated convergence handle the remainder with a common finite budget.

The left side increases to the Green sum as \(r\uparrow1\). On the region \(\phi\ge0\) use monotone convergence; on \(\phi<0\) the integrand is bounded by 1, so use DCT. As an equality allowing infinity,

\[
G(0,0)=(2\pi)^{-d}\int_{[-\pi,\pi]^d}\frac{d\theta}{1-\phi(\theta)}.
\]

Discounting leaves the eventual question unchanged while justifying every interchange. The problem is now whether a deterministic integral is finite.

## 18.6 Dimension changes the budget near the origin

In this periodic domain, \(\phi=1\) requires all coordinates to vanish. The two-sided comparison of \(1-\cos t\) with \(t^2\) near zero gives positive \(c,C,\delta\) such that

\[
c|\theta|^2\le1-\phi(\theta)\le C|\theta|^2
\qquad(|\theta|<\delta).
\]

Away from a small ball, continuity gives a positive lower bound for \(1-\phi\). Inside it, integrability is equivalent to that of \(\int_0^\delta \rho^{d-3}\,d\rho\). Alternatively, decompose into annuli of scale \(2^{-k}\): their volumes are comparable to \(2^{-kd}\) and the integrand to \(2^{2k}\), producing the same geometric-series test without polar coordinates.

The dimension test can be written entirely as a scale sum. The bounds

\[
\frac{2t^2}{\pi^2}\le1-\cos t\le\frac{t^2}{2}
\quad(|t|\le\pi)
\]

give the quadratic comparison; the lower bound follows from \(1-\cos t=2\sin^2(t/2)\) and the chord lower bound for sine on a half-period. For sufficiently large \(k\), the cubic annuli

\[
C_k=\{\theta:2^{-k-1}<\|\theta\|_\infty\le2^{-k}\}
\]

lie inside the small ball. Their volumes are \(2^d(1-2^{-d})2^{-kd}\), while Euclidean norm lies between \(2^{-k-1}\) and \(\sqrt d\,2^{-k}\). There are thus positive constants \(a_d,b_d\), independent of \(k\), such that

\[
a_d\,2^{-k(d-2)}
\le\int_{C_k}\frac{d\theta}{1-\phi(\theta)}
\le b_d\,2^{-k(d-2)}.
\]

In two dimensions each smaller scale contributes the same order of budget, giving an infinite total; from three dimensions onward, halving the scale reduces that budget geometrically. The boundary neither substitutes Gaussian weak convergence for local probabilities nor requires a precise return-probability asymptotic.

The integral diverges in dimensions one and two, and is finite from dimension three onward. Combined with 18.2, this proves Pólya's criterion:

\[
P_0(T_0<\infty)=1\quad(d=1,2),\qquad
P_0(T_0<\infty)<1\quad(d\ge3).
\]

Zero average drift in every coordinate does not decide return. More dimensions supply more routes of escape; analytically, the same quadratic singularity must be supported by different amounts of surrounding volume.

## 18.7 Parity remains, but does not decide recurrence

Each nearest-neighbor step changes the parity of the coordinate sum, so odd-time return is impossible. Chapter 13 explained why a pointwise Gaussian approximation must account for allowed lattice sites and span.

Here a corner with \(\phi=-1\) creates no singularity in \(1-\phi\), so the Green test is governed by \(\phi=1\). That does not license ignoring the other corner when estimating \(u_{2n}\) itself: both positive and negative peaks contribute there. An accumulated-visit test and a fixed-time local approximation are different calculations.

Add an independent holding probability \(h\in(0,1)\). The new readout is \(h+(1-h)\phi\), so the Green integral is multiplied by \(1/(1-h)\). Period becomes one, but recurrence or transience does not change. Holding changes the clock without adding spatial routes of escape.

## 18.8 A small drift changes the one-dimensional answer

Retain independent nearest-neighbor steps, explicitly writing \(p=P(\Delta S=1)\) and \(q=P(\Delta S=-1)=1-p\). Only the left-right probabilities change, not step size, state space or clock.

For line walk with \(p>q\), the chance of hitting 0 from 1 is \(q/p\): apply Chapter 16's ruin formula on \([0,a]\) and let \(a\to\infty\). A path that hits 0 at a finite time has a finite maximum before that hit, so the union of these finite-interval events is exactly eventual hitting.

From −1 the chance of hitting 0 is one. Enlarge the left barrier in the same way, or use Chapter 12's strong law to see the position eventually tending rightward to infinity, which a nearest-neighbor path cannot do without crossing 0. Splitting on the first step gives

\[
f_0=p(q/p)+q=2q<1.
\]

For \(p<q\), symmetry gives \(f_0=2p\). One-dimensional recurrence is sensitive to lack of bias; merely living on a line does not make every random motion return.

## 18.9 Recurrence belongs to a communication class

Suppose \(i\) is recurrent and \(i\to j\). After each return to \(i\), the same positive probability is available for following a fixed finite route to \(j\). Group attempts into nonoverlapping blocks; failure probabilities decay geometrically. Starting from \(i\), the chain therefore eventually hits \(j\) almost surely.

Nonoverlapping attempts can be arranged explicitly. Choose a positive-probability route of length \(\ell\ge1\), with success probability \(\eta>0\). On recurrent records from \(i\), put \(\tau_0=0\) and let \(\tau_{r+1}\) be the first visit to \(i\) at or after \(\tau_r+\ell\). These are finite stopping times. The whole route of attempt \(r\) is revealed before the next attempt begins. If \(A_r\) denotes failure of all the first \(r\) attempts, strong Markov gives

\[
P_i(A_r)\le(1-\eta)^r.
\]

This justifies the geometric bound. Starting a possibly overlapping long attempt at every visit to \(i\) and simply multiplying success chances would not ensure conditioning at the right times. Unconditional independence of attempts is unnecessary; each attempt needs the same conditional success probability \(\eta\) given its past.

Starting from \(j\), it must also hit \(i\) almost surely. Otherwise choose a positive-probability route from \(i\) to its first arrival at \(j\), with no intervening return to \(i\), then a positive-probability future avoiding \(i\). This would give positive probability of no return to \(i\), a contradiction. Iterating strong Markov shows infinitely many visits to \(j\). Thus \(j\) and every state communicating with a recurrent state is recurrent, and recurrent classes are closed.

From any initial state, a specified transient state is visited finitely often almost surely: upon a hit, its remaining visits have the geometric law; without a hit, their number is zero. Taking a common null set over countably many states, the path eventually leaves every fixed finite set. This is a precise sense of escape, not a claim that position has a directional limit.

## 18.10 Infinitely many returns can have infinite mean spacing

A recurrent state is positive recurrent if \(E_iT_i<\infty\), and null recurrent if \(E_iT_i=\infty\). Let the mean visits to \(j\) in one complete return cycle from \(i\) be

\[
\nu_j=E_i\sum_{n=0}^{T_i-1}\mathbf1_{\{X_n=j\}},
\]

Then \(\nu_i=1\) and \(\nu P=\nu\). Shift the occupation count by one time step: times 0 through one before the return become times 1 through \(T_i\); both endpoints are \(i\), so they cancel. All interchanges are initially nonnegative integrations.

The role of stopping in the one-step shift can also be made explicit. Since \(\{n<T_i\}\) belongs to \(\mathcal F_n\), Markov conditional averaging and Tonelli give

\[
\sum_k\nu_kp_{kj}
=E_i\sum_{n\ge0}\mathbf1_{\{n<T_i\}}p_{X_nj}
=E_i\sum_{n\ge0}\mathbf1_{\{n<T_i\}}\mathbf1_{\{X_{n+1}=j\}}
=E_i\sum_{n=1}^{T_i}\mathbf1_{\{X_n=j\}}
=\nu_j.
\]

The last step compares counts along each finite return path: it merely exchanges endpoints both equal to \(i\), without subtracting two infinite expectations. The Green sum counts visits across infinitely many cycles, whereas the cycle measure counts visits inside one cycle. Divergence of the former guarantees recurrence, not finiteness of the latter's total budget.

In an irreducible recurrent chain each \(\nu_j\) is finite. From \(j\) a positive-probability route hits \(i\) before returning to \(j\), so visits to \(j\) before hitting \(i\) are bounded by a geometric number with finite mean. If \(E_iT_i<\infty\), total mass is \(\sum_j\nu_j=E_iT_i\), which normalizes to an invariant probability.

An invariant probability is thus more than a formal matrix eigenvector. It can be an actual return cycle's occupation budget divided by the cycle's mean length.

## 18.11 Why invariant probability requires a finite mean cycle

Conversely, suppose an irreducible countable chain has invariant probability \(\pi\). Start from a state of positive mass and propagate positivity along positive-probability paths using invariance; every \(\pi_i>0\). Under the stationary initial law, the events “at \(i\) at time \(n\), with no later visit” are disjoint for different \(n\). Finite-block stationarity followed by a decreasing limit gives each probability \(\pi_i(1-f_i)\). Their infinite sum is at most one, forcing \(f_i=1\) for every state. No general ergodic theorem has been used.

The remainder must actually vanish. By 18.9, every state \(k\) hits \(i\) almost surely: a positive-probability hitting path with no intermediate return to \(k\) can be tried again at successive returns to \(k\), and repeated failure has a geometric bound. Put \(H_i=\inf\{n\ge0:X_n=i\}\) and \(D=E\setminus\{i\}\); let \(K=(p_{k\ell})_{k,\ell\in D}\) be the substochastic matrix killed at \(i\), and \(b=(p_{ij})_{j\in D}\). The invariant equation on \(D\) gives

\[
\pi_D=\pi_i b+\pi_DK
=\pi_i\sum_{r=0}^{N-1}bK^r+\pi_DK^N.
\]

For \(j\in D\), \(\sum_{r\ge0}(bK^r)_j=\nu_j\): these are precisely the probabilities of visits after departure from \(i\) and before its first return. The remainder has total mass

\[
\sum_{j\in D}(\pi_DK^N)_j
=\sum_{k\in D}\pi_kP_k(H_i>N)\longrightarrow0.
\]

Every hitting tail tends to zero, dominated by the summable \(\pi_k\), so dominated convergence is justified. The first term tends to \(\pi_i\nu_j\) by nonnegative monotone convergence. Include \(\nu_i=1\) and sum over all states to obtain

\[
\pi_j=\pi_i\nu_j,\qquad E_iT_i=1/\pi_i.
\]

Cycle budgets uniquely determine the invariant probability. Symmetric line walk is recurrent but, as Chapter 17 showed, has no invariant probability; it is null recurrent. Finite irreducible chains have invariant probabilities, hence positive recurrent states, though periodicity may still prevent stepwise convergence.

## 18.12 New upward records give another restart

For a real random walk \(S_n\) with independent identically distributed increments, let \(L\) be the first strict ascent above the initial value and \(H=S_L\). Their joint law may be defective: some paths never set a new high. Independent increments and stopping-time slices make the time and height increments between successive records have this same joint law.

If \(q(z,\theta)=E[z^Le^{i\theta H};L<\infty]\), with \(0\le z<1\), the sum of the joint transforms of all strict ascending records is \(\sum_{k\ge0}q(z,\theta)^k=1/(1-q(z,\theta))\). Since \(|q(z,\theta)|\le z<1\), absolute control justifies the summation. This proves the ladder renewal structure itself.

It is not yet the complete Wiener–Hopf factorization splitting the whole walk into ascending and descending parts. Strict-versus-weak boundary conventions and the full product identity still need a separate proof. This precise boundary is retained rather than declaring the entire discrete or Lévy factorization proved by naming it.

## Chapter 18 Epilogue: Revisited places divide time into cycles

Unbiased steps cross a genuine boundary between dimensions two and three. The difference is not in one jump, but in the total budget for infinitely many possible returns. The Green sum records that budget; Fourier integration turns it into competition between singularity and volume near the origin.

Whenever a return occurs, the future begins from the same state again. A record is divided into cycles. Some never finish; others finish almost surely but have infinite mean. Combining these restarts to calculate long-term waiting requires more than deciding whether a return happens: it requires understanding how cycles fill time.

## Historical sources and scope

Pólya's paper, “Über eine Aufgabe der Wahrscheinlichkeitsrechnung betreffend die Irrfahrt im Straßennetz,” appeared in volume 84 of Mathematische Annalen in 1921, pages 149–160. The discounted Fourier argument here is a modern reconstruction using our established characteristic functions and integration tools, not a claim to reproduce his original proof. See the [original publication record](https://doi.org/10.1007/BF01458701). The complete classification here concerns simple symmetric nearest-neighbor lattice walk; arbitrary jumps, dependent steps or general groups require proofs beyond a slogan about dimension.
