# Alpha Decay in the Complex Energy Shell Model

R. Id Betan ${ } ^ { 1 , 2 , 3 }$ and W. Nazarewicz $1 , 2 , 4$

$^ { 1 }$ Department of Physics and Astronomy, University of Tennessee, Knoxville, Tennessee 37996, USA

2Physics Division, Oak Ridge National Laboratory,

P.O. Box 2008, Oak Ridge, Tennessee 37831, USA

$^ 3$ Departamento de Qu´ımica y F´ısica, FCEIA(UNR) - Instituto de F´ısica

Rosario (CONICET), Av. Pellegrini 250, 2000 Rosario, Argentina

4Institute of Theoretical Physics, University of Warsaw, ul. Ho˙za 69, 00-681 Warsaw, Poland

(Dated: November 27, 2024)

Background: Alpha emission from a nucleus is a fundamental decay process in which the alpha particle formed inside the nucleus tunnels out through the potential barrier.

Purpose: We describe alpha decay of $^ { 2 1 2 }$ Po and $^ \mathrm { 1 0 4 }$ Te by means of the configuration interaction approach.

Method: To compute the preformation factor and penetrability, we use the complex-energy shell model with a separable $T { = } 1$ interaction. The single-particle space is expanded in a Woods-Saxon basis that consists of bound and unbound resonant states. Special attention is paid to the treatment of the norm kernel appearing in the definition of the formation amplitude that guarantees the normalization of the channel function.

Results: Without explicitly considering the alpha-cluster component in the wave function of the parent nucleus, we reproduce the experimental alpha-decay width of $^ { 2 1 2 }$ Po and predict an upper limit of $T _ { 1 / 2 } = 5 . 5 \times 1 0 ^ { - 7 }$ sec for the half-life of $^ \mathrm { 1 0 4 }$ Te.

Conclusions: The complex-energy shell model in a large valence configuration space is capable of providing a microscopic description of the alpha decay of heavy nuclei having two valence protons and two valence neutrons outside the doubly magic core. The inclusion of proton-neutron interaction between the valence nucleons is likely to shorten the predicted half-live of $^ \mathrm { 1 0 4 }$ Te.

PACS numbers: 23.60.+e,21.60.Cs,21.10.Tg,27.60.+j,27.80.+w

# I. INTRODUCTION

According to Gamow theory of alpha decay [1, 2], this fundamental radioactive decay can be considered as a two-step process [3–5]. In the first step, an alpha cluster is formed inside the parent nucleus. The resulting alpha particle resides in a metastable state of an average potential of the daughter system. In the second step, the particle tunnels through the potential barrier. Each step requires different theoretical treatment. To compute the preformation factor that describes the alpha formation probability, one needs to evaluate the overlap integral involving wave functions of the parent and daughter nuclei, and that of the alpha particle. The estimate of the penetration probability requires a careful treatment of the resonance state.

The commonly used formulation of the alpha-decay problem employs the R-matrix expression [6, 7]

$$
\Gamma_ {L} = 2 P _ {L} \gamma_ {L} ^ {2} \tag {1}
$$

for the absolute width. In this formalism, the first stage (formation of alpha particle with angular momentum $L$ ) is given by the reduced width $\gamma _ { L } ^ { 2 }$ , while the second stage (decay) is expressed by means of the penetrability $P _ { L }$ . Alternatively, the absolute width can be obtained from the general reaction-theory expression [8–11]

$$
\Gamma_ {L} = S _ {L} \Gamma_ {L} ^ {\mathrm {s p}}, \tag {2}
$$

where $S _ { L }$ is the alpha-spectroscopic factor and $\Gamma _ { L } ^ { \mathrm { s p } }$ is the single-particle (s.p.) decay width.

Historically, expression (1) was derived in 1954 by Thomas [6] using the time-independent R-matrix theory of nuclear reactions. In 1957, Mang [7] developed the alpha-decay formalism based on the time-dependent perturbation theory. He made the connection with the shell model and succeeded in expressing the alpha-decay formation amplitude in a basis of s.p. states. As shown in Refs. [12, 13] formulations of Thomas and Mang are formally equivalent; there are, however, many differences when it comes to practical implementations.

The reduced width calculated in a shell-model configuration expressed in the harmonic oscillator (h.o.) basis is too small. This can be partly cured by means of configuration mixing involving extended shell-model spaces [14, 15] as each admixed configuration contributes coherently to $\gamma _ { L } ^ { 2 }$ . To improve asymptotic properties of s.p. wave functions, the particle continuum was taken into account [16] by considering h.o. expansion [17] or within a Woods-Saxon (WS) basis consisting of bound and outgoing single-particle resonant (Gamow) states [18, 19]. The configuration mixing calculations of Refs. [15, 18] in the valence space of $2 1 2$ Po assumed the seniority-zero (pairing vibrational) wave functions obtained by considering the monopole pairing interaction between like nucleons. However, all these improvements were not sufficient to reproduce the experimental alpha decay in ${ } ^ { 2 1 2 } \mathrm { P o }$ . It is only after the valence proton-neutron interaction had been considered together with a generalized wave function expressed as a combination of cluster and shell model components [20] that theoretical and experimental

widths could be reconciled [21].

The R-matrix expression for the width (1) depends on the channel radius $R$ . This radius should be chosen large enough so that the alpha-daughter interaction in the external region is given by the Coulomb force alone [22]. The infinite range of the Coulomb force implies, however, that the asymptotic behavior of the R-matrix expression is reached only at large values of $R$ , at which the asymptotic behavior of the shell-model s.p. basis (h.o. basis in most applications) used to calculate $\gamma _ { L } ^ { 2 } ( R )$ , does matter. Due to the mismatch between the internal part of the s.p. wave function (well described in the h.o. basis) and the asymptotic part (poorly or not described in the h.o. basis), rather small changes in $R$ may produce appreciable variations in penetrability. Physically, the reason for this sensitivity is the fact that the alpha cluster is formed in the surface region of the nucleus in which the coupling to the alpha continuum that impacts the radial behavior of the formation amplitude is important [16]. Consequently, the absolute R-matrix width depends in general on the channel radius [5, 23], and this is an obvious drawback of the method [22].

Our renewed interest in the alpha-decay problem is stimulated by the recent experimental data above the doubly-magic $^ \mathrm { 1 0 0 }$ Sn [24, 25] that demonstrate the presence of very fast alpha decays. Indeed, the observed enhancement of the reduced widths of 105,106Te relative to 213,212Po is two-to-three, thus confirming earlier expectations [26] of “superallowed” alpha decays in this region due to the large overlaps of valence s.p. shell model proton and neutron wave functions. Our long-term goal is to estimate alpha preformation factors in nuclei above $^ { 2 0 8 }$ Pb and $^ \mathrm { 1 0 0 }$ Sn by using large valence s.p. spaces, including positive-energy Gamow states of a finite-depth WS potential [18, 19]. In this study, we focus on $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ and $^ \mathrm { 1 0 4 }$ Te nuclei having two valence protons and two valence neutrons outside doubly-magic cores.

Our paper is organized as follows. Section II briefly describes the alpha-decay formalism used in this work, with special emphasis on approximations used to describe wave functions of parent and daughter nuclei. Section III deals with the approximations employed and parameters used. In particular, we discuss the sensitivity of the calculated spectroscopic factor to the parameters defining the shifted Gaussian basis that is used to compute the normalization of the channel function. In Sec. IV we study the sensitivity of the reduced alpha width in ${ } ^ { 2 1 2 } \mathrm { P o }$ on the choice of s.p. basis used. In Section V we discuss the absolute alpha-decay width of $^ { 2 1 2 }$ Po and in Sec. VI we compare it with the absolute width of the superallowed alpha emitter $^ \mathrm { 1 0 4 }$ Te. Finally, the main conclusions of this work are summarized in Sec. VII.

# II. FORMALISM

In this section, we discuss the R-matrix (1) and spectroscopic factor (2) expressions for the decay width.

The connection between the two formulations is given in Ref. [8]. We also discuss the so-called deltaapproximation for the formation amplitude.

# A. R-matrix expression for the decay width

Within the R-matrix theory [6, 7, 12], the absolute width is given by Eq. (1) with $P _ { L } ( R )$ being the barrier penetrability and $\gamma _ { L } ( R )$ – the reduced width amplitude [27]. While both quantities strongly depend on the value of the channel radius $R$ , the absolute width should be $R$ -independent.

For $P _ { L } ( R )$ we use the standard expression [6]:

$$
P _ {L} (R) = \frac {k R}{\left| H _ {L} ^ {+} (\eta , k R) \right| ^ {2}}, \tag {3}
$$

where $k$ is given by the alpha energy $\begin{array} { r } { E _ { \alpha } = \frac { \hbar ^ { 2 } k ^ { 2 } } { 2 \mu } } \end{array}$ = , obtained from the experimental $Q _ { \alpha }$ value by correcting for electron screening; $\begin{array} { r } { \mu = \frac { m _ { d } m _ { \alpha } } { m _ { d } + m _ { \alpha } } } \end{array}$ is the reduced mass of alpha particle with $m _ { d }$ being the mass of the daughter nucleus; $H _ { L } ^ { + } ( \eta , k R )$ is the outgoing spherical Coulomb-Hankel function; and $\begin{array} { r } { \eta \ = \ \frac { 2 Z _ { d } \mu e ^ { 2 } } { \hbar ^ { 2 } k } } \end{array}$ is the Sommerfeld Coulomb parameter.

The reduced width amplitude $\gamma _ { L } ( R )$ may be written in terms of the formation amplitude $g _ { L } ( R )$ [5, 14]:

$$
\gamma_ {L} = \sqrt {\frac {\hbar^ {2} R}{2 \mu}} g _ {L} (R), \tag {4}
$$

with

$$
\begin{array}{l} g _ {L} (R) = \int d \Omega_ {R} \int d \xi_ {\alpha} \int d \xi_ {D} \\ \Phi_ {J M} ^ {P} \mathcal {A} \left[ \phi_ {\alpha} (\xi_ {\alpha}) \Psi_ {j} ^ {D} (\xi_ {D}) Y _ {L} (\hat {R}) \right] _ {J M} ^ {*}, \quad (5) \\ \end{array}
$$

where $\phi _ { \alpha }$ is the normalized wave function of the alpha particle with zero angular momentum, $Y _ { L M _ { L } }$ is the angular part of the center-of-mass (c.o.m.) motion of the alpha particle,ter nucleus, an ΨD $\Psi _ { j m _ { j } } ^ { D }$ is the wave function of the daugh-is the wave function of the parent $\Phi _ { J M } ^ { P }$ nucleus. The coordinates $\xi _ { \alpha }$ and $\xi _ { D }$ are the intrinsic coordinates of the alpha particle and daughter nucleus, respectively. All wave functions are normalized in terms of the internal and c.o.m. coordinates [27]. By construction, the parent and daughter wave functions are antisymmetric. The antisymmetrization with respect to inter-fragment nucleons is done by means of the operator $\mathcal { A }$ . Its action can be approximated by means of a factor $\left[ \binom { N _ { v } } { 2 } \binom { Z _ { v } } { 2 } \right] ^ { 1 / 2 }$ [14, 27, 28], with $N _ { v }$ and $Z _ { v }$ being, respectively, the numbers of valence neutrons and protons in the parent nucleus.

For the internal alpha-particle wave function we take

the standard Gaussian ansatz [18, 29]:

$$
\phi_ {\alpha} \left(\rho_ {1} \rho_ {2} \rho_ {3}, \sigma_ {1} \sigma_ {2} \sigma_ {3} \sigma_ {4}\right) = \phi \left(\rho_ {1} \rho_ {2} \rho_ {3}\right) \chi_ {0 0} \left(\sigma_ {1} \sigma_ {2}\right) \chi_ {0 0} \left(\sigma_ {3} \sigma_ {4}\right),
$$

$$
\chi_ {0 0} \left(\sigma_ {1} \sigma_ {2}\right) = \left[ \chi_ {1 / 2} \left(\sigma_ {1}\right) \chi_ {1 / 2} \left(\sigma_ {2}\right) \right] _ {0 0},
$$

$$
\phi \left(\rho_ {1} \rho_ {2} \rho_ {3}\right) = \left(\frac {8 \beta}{\pi}\right) ^ {9 / 4} e ^ {- 4 \beta \left(\rho_ {1} ^ {2} + \rho_ {2} ^ {2} + \rho_ {3} ^ {2}\right)}. \tag {6}
$$

The parameter $\beta ~ = ~ { \textstyle { \frac { 9 } { 6 4 r _ { \alpha } ^ { 2 } } } } { = } 0 . 0 5 7 \mathrm { f m ^ { - 2 } }$ depends on the root-mean-square alpha radius $r _ { \alpha }$ =1.57 fm [29].

The transformation between the intrinsic $\begin{array} { r l } { \xi _ { \alpha } } & { { } = } \end{array}$ $\{ \rho _ { 1 } , \rho _ { 2 } , \rho _ { 3 } \}$ and nucleonic $\{ r _ { i } \}$ ( $\imath$ =1,2,3,4) coordinates reads:

$$
\rho_ {1} = \frac {\boldsymbol {r} _ {1} - \boldsymbol {r} _ {2}}{\sqrt {2}},
$$

$$
\rho_ {2} = \frac {\boldsymbol {r} _ {3} - \boldsymbol {r} _ {4}}{\sqrt {2}}, \tag {7}
$$

$$
\rho_ {3} = \frac {\left(\boldsymbol {r} _ {1} + \boldsymbol {r} _ {2}\right) - \left(\boldsymbol {r} _ {3} + \boldsymbol {r} _ {4}\right)}{2},
$$

and

$$
\boldsymbol {R} = \frac {\boldsymbol {r} _ {1} + \boldsymbol {r} _ {2} + \boldsymbol {r} _ {3} + \boldsymbol {r} _ {4}}{4} \tag {8}
$$

is the c.o.m. coordinate of alpha particle. Let us denote the spherical components of intrinsic coordinates by $\pmb { \rho } _ { i } = ( \rho _ { i } , \theta _ { i } , \tilde { \varphi } _ { i } )$ . Assuming ${ \theta _ { R } } = { \varphi _ { R } } = 0$ , the nucleonic coordinates can be written as:

$$
\begin{array}{l} 4 r _ {1, 2} ^ {2} = 4 R ^ {2} + \rho_ {3} ^ {2} + 2 \rho_ {1} ^ {2} \pm 2 \sqrt {2} \rho_ {3} \rho_ {1} \cos \tilde {\theta} _ {3 1} \\ + 4 R \left(\rho_ {3} \cos \tilde {\theta} _ {3} \pm \sqrt {2} \rho_ {1} \cos \tilde {\theta} _ {1}\right), \\ \end{array}
$$

$$
\begin{array}{l} 4 r _ {3, 4} ^ {2} = 4 R ^ {2} + \rho_ {3} ^ {2} + 2 \rho_ {2} ^ {2} \mp 2 \sqrt {2} \rho_ {3} \rho_ {2} \cos \tilde {\theta} _ {3 2} \\ - 4 R \left(\rho_ {3} \cos \tilde {\theta} _ {3} \pm \sqrt {2} \rho_ {2} \cos \tilde {\theta} _ {2}\right), \tag {9} \\ \end{array}
$$

where $\ddot { \theta } _ { i j } = \ddot { \theta } _ { j } - \ddot { \theta } _ { i }$ , and

$$
\cos \theta_ {1, 2} = \frac {2 R + \rho_ {3} \cos \tilde {\theta} _ {3} \pm \sqrt {2} \rho_ {1} \cos \tilde {\theta} _ {1}}{2 r _ {1 , 2}},
$$

$$
\cos \theta_ {3, 4} = \frac {2 R - \rho_ {3} \cos \tilde {\theta} _ {3} \pm \sqrt {2} \rho_ {2} \cos \tilde {\theta} _ {2}}{2 r _ {3 , 4}}. \tag {10}
$$

This paper deals with g.s.→g.s. alpha decays to the magic daughter nucleus. Assuming the seniority-zero wave function, the corresponding formation amplitude is [13, 14]

$$
F _ {0} (R) = \frac {\sqrt {8}}{1 6 \pi^ {3 / 2}} \sum_ {\nu_ {n}, \nu_ {p}} (-) ^ {l _ {n} + l _ {p}} b _ {\nu_ {n}, \nu_ {p}} \hat {j} _ {n} \hat {j} _ {p} I _ {v _ {n}, \nu_ {p}} (R), \tag {11}
$$

where

$$
\begin{array}{l} I _ {\nu_ {n}, \nu_ {p}} (R) = \int d \boldsymbol {\rho} _ {1} d \boldsymbol {\rho} _ {2} d \boldsymbol {\rho} _ {3} \phi (\rho_ {1} \rho_ {2} \rho_ {3}) \\ \times \frac {u _ {\nu_ {n}} (r _ {1})}{r _ {1}} \frac {u _ {\nu_ {n}} (r _ {2})}{r _ {2}} P _ {l _ {n}} (\cos \theta_ {1 2}) \tag {12} \\ \times \frac {u _ {\nu_ {p}} (r _ {3})}{r _ {3}} \frac {u _ {\nu_ {p}} (r _ {4})}{r _ {4}} P _ {l _ {p}} (\cos \theta_ {3 4}), \\ \end{array}
$$

with $\theta _ { i j } = \theta _ { j } - \theta _ { i }$ , $\nu = \{ n , l , j \}$ , and $u _ { \nu } ( r )$ being s.p. radial wave functions. The factor $\sqrt { 8 }$ comes from the Jacobian of the transformation between the nucleonic coordinates $\{ r _ { i } \}$ and the internal and c.o.m. coordinates [5, 30]. In Eq. (12) and in the following, the s.p. indices $1 , 2$ refer to neutrons while $3 , 4$ refer to protons. The coefficients $b _ { \nu _ { n } , \nu _ { p } }$ are the shell-model four-particle wave function amplitudes.

# B. Delta-function approximation

In the calculation of alpha-decay rates based on h.o. wave functions, it was noticed [28] that the relative rates change little with the oscillator length $b _ { \mathbf { h . o . } }$ . of the basis. Using this argument, Mang proposed to take $\beta \gg 1 / b _ { \mathrm { h . o . } } ^ { 2 }$ . In this limit, the expression for the formation amplitude can be simplified (see also Ref. [31]). In the literature, this is known as delta-function approximation [32].

In practice, one assumes that the alpha particle wave function is constant inside a small volume of radius $s _ { \alpha } =$ 2.34 fm [32] and zero outside. Within this approximation $\rho _ { i } = 0$ ; hence, it immediately follows from Eqs. (9) that $r _ { 1 } = r _ { 2 } = r _ { 3 } = r _ { 4 } = R$ [32, 33], and the formation amplitude reduces to

$$
F _ {0} ^ {\delta} (R) = \frac {\sqrt {8}}{1 6 \pi^ {3 / 2}} \left(\frac {4 \pi s _ {\alpha} ^ {3}}{3}\right) ^ {3 / 2} \left(\sum_ {\nu_ {n}} I _ {\nu_ {n}} ^ {n}\right) \left(\sum_ {\nu_ {p}} I _ {\nu_ {p}} ^ {p}\right), \tag {13}
$$

with

$$
I _ {\nu} ^ {\tau} = (-) ^ {l _ {\nu}} b _ {\nu} ^ {\tau} \hat {j} _ {\nu} B _ {\nu} \frac {u _ {\nu \tau} ^ {2} (R)}{R ^ {2}}, \tag {14}
$$

where $\tau = n , p$ . The correction factor $B _ { \nu }$ depends on the relative angular momentum [32]:

$$
B _ {\nu} = 1 - 0. 0 1 3 l _ {\nu} \left(l _ {\nu} + 1\right). \tag {15}
$$

# C. Four-particle amplitudes

For the g.s. alpha decay of $2 1 2$ Po and $^ \mathrm { 1 0 4 }$ Te, we are going to assume that the four valence nucleons move around the rigid, doubly-magic core. The parent-nucleus wave function is approximated by a product of two-neutron and two-proton seniority-zero states:

$$
\left| \Phi_ {J = 0, M = 0} ^ {P} \right\rangle = \left| \Psi_ {2 n, 0 0} \right\rangle \otimes \left| \Psi_ {2 p, 0 0} \right\rangle , \tag {16}
$$

where

$$
\left| \Psi_ {2 \tau , 0} \right\rangle = \sum_ {\nu} X _ {\nu} ^ {\tau} | \nu \nu , 0 0 \rangle , \tag {17}
$$

$\begin{array} { r } { | \nu \nu , 0 0 \rangle = \frac { [ a _ { \nu } ^ { \dagger } a _ { \bar { \nu } } ^ { \dagger } ] _ { 0 0 } } { \sqrt { 2 } } | 0 _ { \tau } \rangle } \end{array}$ , and $| 0 \rangle = | 0 _ { n } \rangle \otimes | 0 _ { p } \rangle$ is the shellmodel vacuum representing the $^ \mathrm { 2 0 8 }$ Pb or $^ \mathrm { 1 0 0 }$ Sn g.s. wave function. The four-particle amplitudes $b _ { \nu _ { n } , \nu _ { p } }$ in (11) can thus be written in a separable form:

$$
b _ {\nu_ {n}, \nu_ {p}} = X _ {\nu_ {n}} ^ {n} X _ {\nu_ {p}} ^ {p}. \tag {18}
$$

# D. Alpha decay spectroscopic factor

Based on the general theoretical arguments [8–11], the absolute width can be expressed as a product of the alpha-particle spectroscopic factor and the single particle width, see Eq. (2). The spectroscopic factor $S _ { L }$ contains information about the probability of forming an alpha cluster in the parent system. Since the alpha particle, when formed, occupies the resonant state, the s.p. width can be obtained from the so-called current expression [5, 34, 35]:

$$
\Gamma_ {L} ^ {\mathrm {s p}} = i \frac {\hbar^ {2}}{2 \mu} \frac {u _ {L} ^ {\prime *} (R) u _ {L} (R) - u _ {L} ^ {\prime} (R) u _ {L} ^ {*} (R)}{\int | u _ {L} (R) | ^ {2} d R}, \tag {19}
$$

where the Gamow function $u _ { L } ( R )$ is obtained as a solution of the Schr¨odinger equation with outgoing boundary condition. When the imaginary part of the complex energy eigenvalue $\begin{array} { r } { \mathcal { E } _ { \alpha } = \frac { \hbar ^ { 2 } ~ k ^ { 2 } } { 2 ~ \mu } } \end{array}$ is small, which is always the case for the considered g.s. alpha emitters, one can approximate (19) with [36]:

$$
\Gamma_ {L} ^ {s p} = \frac {\hbar^ {2} \Re (k)}{\mu} \frac {| u _ {L} (R) | ^ {2}}{| H _ {L} ^ {+} (\eta , k R) | ^ {2}}. \tag {20}
$$

The s.p. width obtained in this way should be identical to the value $- 2 \mathrm { I m } ( { \mathcal { E } _ { \alpha } } )$ given by the imaginary part of the Gamow resonance energy, if the latter is computed with a sufficient precision.

The conventional alpha spectroscopic factor as introduced in Ref. [8] is defined by

$$
S _ {L} = | \langle \mathcal {A} [ \phi_ {\alpha} (\xi_ {\alpha}) \Psi_ {j} ^ {D} (\xi_ {D}) \psi_ {L} (\boldsymbol {R}) ] _ {J M} | \Phi_ {J M} ^ {P} \rangle | ^ {2}, \quad (2 1)
$$

where $\begin{array} { r } { \psi _ { L M } ( { \bf R } ) = \frac { u _ { L } ( R ) } { R } Y _ { L M } ( \hat { R } ) } \end{array}$ represents the relative motion alpha particle with respect to the daughter. In terms of the formation amplitude, $S _ { L }$ reads [3, 5, 37]:

$$
S _ {L} = \int_ {0} ^ {\infty} g _ {L} ^ {2} (R) R ^ {2} d R. \tag {22}
$$

# E. Modified spectroscopic factor

Since the formation amplitude Eq. (5) represents the overlap of the parent wave function with the daughteralpha product state, one would be tempted to associate it with the probability amplitude that in the parent wave functicleus $\Phi _ { J M } ^ { P }$ an alpha partie at a distance e . $\phi _ { \alpha }$ and a daue value of ter nu-would $\Psi _ { j m _ { j } } ^ { D }$ $R$ $S _ { L }$ then be associated with the total probability of formation of an alpha particle. However, the fundamental problem with this interpretation is that the channel function ${ \cal A } \left. \phi _ { \alpha } ( \xi _ { \alpha } ) \Psi _ { j } ^ { D } ( \xi _ { D } ) \psi _ { L } ( { \pmb R } ) \right. _ { J M }$ is not properly normalized [3, 10, 11, 38–41].

The properly defined spectroscopic factor (sometimes referred to as “the amount of clustering”) [21, 38, 42–45] is given by

$$
\mathcal {S} _ {L} = \int_ {0} ^ {\infty} G _ {L} ^ {2} (R) R ^ {2} d R, \tag {23}
$$

where

$$
G _ {L} (R) = \int \mathcal {N} _ {L} ^ {- 1 / 2} \left(R, R ^ {\prime}\right) g _ {L} \left(R ^ {\prime}\right) R ^ {\prime 2} d R ^ {\prime} \tag {24}
$$

is the modified formation amplitude. The norm kernel $\mathcal { N } _ { L }$ appearing in Eq. (24) is [43]

$$
\mathcal {N} _ {L} \left(R, R ^ {\prime}\right) = \tag {25}
$$

$$
\langle \mathcal {A} \frac {\delta (R _ {\alpha} - R)}{R ^ {2}} \phi_ {\alpha} [ Y _ {L} \Psi_ {j} ^ {D} ] _ {J} | \mathcal {A} \frac {\delta (R _ {\alpha} - R ^ {\prime})}{R ^ {\prime 2}} \phi_ {\alpha} [ Y _ {L} \Psi_ {j} ^ {D} ] _ {J} \rangle .
$$

The presence of the norm kernel $\mathcal { N }$ effectively enhances the spectroscopic factor by one-to-two orders of magnitude [21, 40, 41, 45, 46].

To compute $\mathcal { N } _ { L } ^ { - 1 / 2 } ( R , R ^ { \prime } )$ , we expand the eigenfunctions of the norm kernel in an orthonormalized shifted Gaussian basis (SGB) [43],

$$
\tilde {F} _ {L} (R, R _ {k}) = \sum_ {k ^ {\prime}} \left(N _ {F} ^ {- 1 / 2}\right) _ {k k ^ {\prime}} F _ {L} (R, R _ {k ^ {\prime}}), \tag {26}
$$

with $R _ { k }$ equidistant mesh points in the interval $\left( 0 , R _ { \operatorname* { m a x } } \right)$ and $k = 1 , \dots , M$ , where $M$ is the dimension of the basis. The SGB is given by

$$
F _ {L} \left(R, R _ {k}\right) = 4 \pi \left(\frac {8 \beta^ {\prime}}{\pi}\right) ^ {3 / 4} e ^ {- 4 \beta^ {\prime} \left(R ^ {2} + R _ {k} ^ {2}\right)} i ^ {L} j _ {L} \left(- i 8 \beta^ {\prime} R R _ {k}\right), \tag {27}
$$

while the SGB overlap $( N _ { F } ) _ { k k ^ { \prime } }$ is given by

$$
\begin{array}{l} \left(N _ {F}\right) _ {k k ^ {\prime}} = \int F _ {L} ^ {*} (R, R _ {k}) F _ {L} (R, R _ {k ^ {\prime}}) R ^ {2} d R \tag {28} \\ = 4 \pi e ^ {- 2 \beta^ {\prime} (R _ {k} ^ {2} + R _ {k ^ {\prime}} ^ {2})} i ^ {L} j _ {L} (- i 4 \beta^ {\prime} R _ {k} R _ {k ^ {\prime}}). \\ \end{array}
$$

Using the SGB overlaps, the eigenvalue equation for the norm matrix can be expressed in the form:

$$
\sum_ {k ^ {\prime}} ^ {M} \mathcal {N} _ {k k ^ {\prime}} ^ {\tilde {F}} c _ {k ^ {\prime}} ^ {\nu} = n _ {\nu} c _ {k} ^ {\nu}, \tag {29}
$$

where

$$
\mathcal {N} _ {k k ^ {\prime}} ^ {\tilde {F}} = \sum_ {n n ^ {\prime}} ^ {M} \left(N _ {F} ^ {- 1 / 2}\right) _ {k n} \mathcal {N} _ {n n ^ {\prime}} ^ {F} \left(N _ {F} ^ {- 1 / 2}\right) _ {n ^ {\prime} k ^ {\prime}} \tag {30}
$$

For $\beta ^ { \prime } = 4 \beta$ , the core-projected norm $\mathcal { N } ^ { F }$ in Eq. (30) reduces to a simple expression [21, 43, 47]:

$$
\mathcal {N} _ {k k ^ {\prime}} ^ {F} = \left(\langle \psi_ {k} ^ {(\nu), L} | \psi_ {k ^ {\prime}} ^ {(\nu), L} \rangle\right) ^ {2} \left(\langle \psi_ {k} ^ {(\pi), L} | \psi_ {k ^ {\prime}} ^ {(\pi), L} \rangle\right) ^ {2} \tag {31}
$$

where

$$
\begin{array}{l} \langle \psi_ {k} ^ {(\mu), L} | \psi_ {k ^ {\prime}} ^ {(\mu), L} \rangle = \langle \phi_ {k} ^ {L} | \phi_ {k ^ {\prime}} ^ {L} \rangle \\ - \sum_ {n l j \tau \in \text {c o r e}} \delta_ {l L} \left\langle \phi_ {k} ^ {l} \mid R _ {n l j} \right\rangle \left\langle R _ {n l j} \mid \phi_ {k ^ {\prime}} ^ {l} \right\rangle (3 2) \\ \end{array}
$$

with $\phi _ { k } ^ { L } ( R ) = F _ { L } ( R , R _ { k } ) ( \beta ^ { \prime } \to \beta )$ and $R _ { n l j } ( R ) = u _ { n l j } / R$ are the radial s.p. wave functions of the core.

In terms of eigenstates $c _ { k } ^ { \nu }$ of (29), the spectral representation of the norm kernel can be written as:

$$
\mathcal {N} _ {L} ^ {- 1 / 2} \left(R, R ^ {\prime}\right) = \sum_ {\substack {\nu \\ \left(n _ {\nu} > n _ {\min }\right)}} n _ {\nu} ^ {- 1 / 2} u _ {\nu} ^ {L *} \left(R\right) u _ {\nu} ^ {L} \left(R ^ {\prime}\right), \tag{33}
$$

where the eigenfunctions $u _ { \nu } ^ { L } ( R )$ of the norm kernel are

$$
u _ {\nu} ^ {L} (R) = \sum_ {k} ^ {M} c _ {k} ^ {\nu} \tilde {F} _ {L} (R, R _ {k}), \tag {34}
$$

and $n _ { \mathrm { m i n } }$ represents the usual cutoff on the eigenvalue of the norm kernel. The final expression for the modified formation amplitude in the normalized SGB becomes [43]:

$$
G _ {L} (R) = \sum_ {\substack {\nu \\ \left(n _ {\nu} > n _ {\min}\right)}} n _ {\nu} ^ {- 1 / 2} u _ {\nu} ^ {L} (R) g _ {\nu} ^ {L} \tag{35}
$$

with

$$
g _ {\nu} ^ {L} = \int u _ {\nu} ^ {L} (R) g _ {L} (R) R ^ {2} d R. \tag {36}
$$

# III. THE MODEL

# A. Single-particle space

The s.p. space is spanned on resonant states of a WS $^ +$ Coulomb average potential. The parameters of the s.p. Hamiltonian, namely the WS potential depth $V _ { 0 }$ , spin-orbit potential depth $V _ { \mathrm { s o } }$ , diffuseness $a$ ( $= a _ { \mathrm { s o } }$ ), radius $r _ { 0 }$ ( $\equiv r _ { 0 , \mathrm { s o } }$ ), and the radius of the uniform charge distribution $r _ { c }$ defining the Coulomb potential are listed in Table I. The resulting neutron and proton s.p. ener-

TABLE I. Parameters of the average WS Hamiltonian used in this work to compute s.p. neutron and proton states of ${ } ^ { 2 0 8 } \mathrm { P b }$ and $^ \mathrm { 1 0 0 }$ Sn cores.   

<table><tr><td>Core</td><td>τ</td><td>V0(MeV)</td><td>Vso(MeV)</td><td>a(fm)</td><td>r0(fm)</td><td>rc(fm)</td></tr><tr><td rowspan="2">208Pb</td><td>n</td><td>44.40</td><td>16.5</td><td>0.70</td><td>1.27</td><td></td></tr><tr><td>p</td><td>66.04</td><td>19.0</td><td>0.75</td><td>1.19</td><td>1.27</td></tr><tr><td rowspan="2">100Sn</td><td>n</td><td>51.60</td><td>11.3</td><td>0.70</td><td>1.27</td><td></td></tr><tr><td>p</td><td>52.20</td><td>10.5</td><td>0.70</td><td>1.27</td><td>1.27</td></tr></table>

gies for 208Pb and $^ \mathrm { 1 0 0 }$ Sn are given in Tables II and III, respectively. The nucleus $^ \mathrm { 1 0 1 }$ Sb is proton-unbound; the values in Table III are generally consistent with systematics [48]. In particular, we predict a very small splitting between the $0 g _ { 7 / 2 }$ and $1 d _ { 5 / 2 }$ neutron shells outside $_ \mathrm { 1 0 0 }$ Sn, and a $\boldsymbol { 0 } \boldsymbol { g } _ { 7 / 2 }$ g.s. in $^ \mathrm { 1 0 1 }$ Sn as suggested by recent experiment [49].

TABLE II. The eigenstates (in MeV) of the s.p. Hamiltonian of Table I for $\mathrm { \dot { 2 } 0 8 _ { P b } }$ calculated with the Gamow solver anti [50]. The positive-energy eigenvalues represent Gamow resonances; their imaginary energies reflect nonzero particle width.   

<table><tr><td>Orbit</td><td>Neutrons</td><td>Orbit</td><td>Protons</td></tr><tr><td>1g9/2</td><td>-3.926</td><td>0h9/2</td><td>-3.784</td></tr><tr><td>0i11/2</td><td>-2.797</td><td>1f7/2</td><td>-3.542</td></tr><tr><td>2d5/2</td><td>-2.072</td><td>0i13/2</td><td>-1.844</td></tr><tr><td>0j15/2</td><td>-1.883</td><td>2p3/2</td><td>-0.690</td></tr><tr><td>3s1/2</td><td>-1.438</td><td>1f5/2</td><td>-0.518</td></tr><tr><td>2d3/2</td><td>-0.781</td><td>2p1/2</td><td>0.491 - i0.200 × 10-11</td></tr><tr><td>1g7/2</td><td>-0.768</td><td>1g9/2</td><td>4.028 - i0.130 × 10-7</td></tr><tr><td>1h11/2</td><td>2.251 - i0.026</td><td>0i11/2</td><td>5.434 - i0.992 × 10-8</td></tr><tr><td>0j13/2</td><td>5.411 - i0.009</td><td>0j15/2</td><td>5.960 - i0.115 × 10-7</td></tr><tr><td></td><td></td><td>2d5/2</td><td>6.748 - i0.184 × 10-2</td></tr><tr><td></td><td></td><td>3s1/2</td><td>7.843 - i0.367 × 10-1</td></tr><tr><td></td><td></td><td>1g7/2</td><td>8.087 - i0.898 × 10-3</td></tr><tr><td></td><td></td><td>2d3/2</td><td>8.530 - i0.284 × 10-1</td></tr><tr><td></td><td></td><td>1h11/2</td><td>11.390 - i0.215 × 10-1</td></tr><tr><td></td><td></td><td>0j13/2</td><td>15.086 - i0.493 × 10-2</td></tr><tr><td></td><td></td><td>1h9/2</td><td>15.964 - i0.393</td></tr></table>

TABLE III. Similar as in Table II except for $^ { 1 0 0 } \mathrm { S n }$   

<table><tr><td>Orbit</td><td>Neutrons</td><td>Protons</td></tr><tr><td>0g7/2</td><td>-10.830</td><td>2.669 - i0.207 × 10-7</td></tr><tr><td>1d5/2</td><td>-10.674</td><td>2.869 - i0.963 × 10-5</td></tr><tr><td>2s1/2</td><td>-9.074</td><td>4.150 - i0595 × 10-2</td></tr><tr><td>1d3/2</td><td>-8.927</td><td>4.393 - i0.166 × 10-2</td></tr><tr><td>0h11/2</td><td>-5.793</td><td>7.280 - i0.110 × 10-2</td></tr><tr><td>1f7/2</td><td>-2.346</td><td>9.649 - i0.452</td></tr><tr><td>2p3/2</td><td>-1.531</td><td></td></tr><tr><td>2p1/2</td><td>-0.912</td><td></td></tr><tr><td>0h9/2</td><td>-0.641</td><td>12.012 - i0.0736</td></tr><tr><td>1f5/2</td><td>-0.171</td><td></td></tr><tr><td>0i13/2</td><td>3.254 - i0.132 × 10-2</td><td>15.572 - i0.185</td></tr></table>

# B. Two-particle interaction

The correlated two particle wave functions $| \Psi _ { 2 \tau , 0 } \rangle$ (17) have been obtained using a separable two-body $T = 1$ pairing interaction [51]:

$$
\langle \nu \nu , 0 0 | V | \nu^ {\prime} \nu^ {\prime}, 0 0 \rangle = - G _ {\tau} f (\nu , \tau) f (\nu^ {\prime}, \tau), \tag {37}
$$

where

$$
f (\nu , \tau) = \frac {(-) ^ {l _ {\nu}}}{\sqrt {2}} \langle j _ {\nu} | | Y _ {0} | | j _ {\nu} \rangle I (\nu , \tau). \tag {38}
$$

In Eq. (38) we used the Condon-Shortley phase convention for $\left. j _ { \nu } | | Y _ { 0 } | | j _ { \nu } \right.$ and

$$
I (\nu , \tau) = \int u _ {\nu \tau} ^ {2} (r) f _ {\tau} (r) d r. \tag {39}
$$

For the radial form factor $f _ { \tau } ( r )$ we took the derivative of the WS potential multiplied by $r$ :

$$
f _ {\tau} (r) = \frac {r}{a _ {v \tau}} \frac {e ^ {\frac {r - R _ {v \tau}}{a _ {v \tau}}}}{\left(1 + e ^ {\frac {r - R _ {v \tau}}{a _ {v \tau}}}\right) ^ {2}}. \tag {40}
$$

In the case of $2 1 2$ Po and $^ \mathrm { 1 0 4 }$ Te the two-particle amplitudes of Eq. (17) were obtained exactly in the Tamm-Dancoff approximation [52, 53]:

$$
X _ {\nu} ^ {\tau} = N _ {0} \frac {f (\nu , \tau)}{2 \epsilon_ {\nu} ^ {\tau} - E _ {0} ^ {\tau}}, \tag {41}
$$

where $\epsilon _ { \nu } ^ { \prime }$ are s.p. energies, $E _ { 0 } ^ { \tau }$ is the correlated twoparticle energy and $N _ { 0 }$ is the normalization constant fixed by the condition $\begin{array} { r } { \sum _ { \nu } \left( X _ { \nu } ^ { \tau } \right) ^ { 2 } = 1 } \end{array}$ .

The parameters $R _ { v \tau }$ and $a _ { v \tau }$ defining the radial form factor (40) for $^ { 2 1 0 } \mathrm { { P b } }$ and ${ } ^ { 2 1 0 } \mathrm { P o }$ were chosen to reproduce the wave functions used by Harada [14]. Since such data are not available for 102Sn and $^ \mathrm { 1 0 2 }$ Te, in this case we adopted the values of the WS potential for $\scriptstyle 1 0 0$ Sn shown in Table I. The pairing strength $G _ { \tau }$ was adjusted to fit the experimental two-nucleon separation energies $S _ { 2 \tau }$ through the dispersion relation

$$
\frac {1}{G _ {\tau}} = \sum_ {\nu} \frac {f ^ {2} (\nu , \tau)}{2 \epsilon_ {\nu} ^ {\tau} - E _ {0} ^ {\tau}}. \tag {42}
$$

Since the proton-unbound nucleus 102Te is not known experimentally, for this system we adopted the value of $S _ { 2 p } = - 2 . 1 4 \mathrm { M e V }$ obtained by extrapolating down from the heavier Te isotopes [54]. This value is in reasonable agreement with recent phenomenological estimates [48]. Table IV lists the parameters of the residual interaction used in our study.

TABLE IV. Parameters $R _ { v \tau }$ and $a _ { v \tau }$ of the residual interaction (37). The last column lists the value of $S _ { 2 \tau }$ that has been used to constrain the pairing strength $G _ { \tau }$ for various configuration spaces considered.

<table><tr><td>nucleus</td><td>Rv (fm)</td><td>av (fm)</td><td>S2τ (MeV)</td></tr><tr><td>210Pb</td><td>7.525</td><td>0.70</td><td>9.123</td></tr><tr><td>210Po</td><td>5.451</td><td>0.75</td><td>8.783</td></tr><tr><td>102Sn</td><td>5.895</td><td>0.70</td><td>24.3</td></tr><tr><td>102Te</td><td>5.895</td><td>0.70</td><td>-2.14</td></tr></table>

# C. Configuration space

To study the dependence of the formation amplitude on the size of valence space, and to compare with previous work, we considered several model spaces. Those used in the description of the alpha decay of $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ are given in Table V. The model space M0 contains only one valence shell. The space M1 contains one major shell, including

the unusual-parity intruder orbit. The model space M2 is that used by Harada [14]. The model space M3 is that of Glendenning and Harada [55]. Finally, M4 is the extended shell model space employed by Tonozuka and Arima. The model spaces used to describe $^ \mathrm { 1 0 4 }$ Te alpha

TABLE V. Model spaces used in this work to describe $^ { 2 1 2 }$ Po alpha decay.   

<table><tr><td>Model</td><td>Neutron States</td><td>Proton States</td></tr><tr><td>M0</td><td>1g9/2</td><td>0h9/2</td></tr><tr><td>M1</td><td>1g9/2, 0i11/2, 2d5/2, 0j15/23s1/2, 2d3/2, 1g7/2</td><td>0h9/2, 1f7/2, 0i13/2, 2p3/21f5/2, 2p1/2</td></tr><tr><td>M2</td><td>1g9/2, 0i11/2, 2d5/2</td><td>0h9/2, 1f7/2, 0i13/2</td></tr><tr><td>M3</td><td>1g9/2, 0i11/2, 2d5/2, 0j15/2</td><td>0h9/2, 1f7/2, 0i13/2</td></tr><tr><td>M4</td><td>1g9/2, 0i11/2, 2d5/2, 0j15/23s1/2, 2d3/2, 1g7/2, 1h11/20j13/2</td><td>0h9/2, 1f7/2, 0i13/2, 2p3/21f5/2, 2p1/2, 1g9/2, 0i11/20j15/2, 2d5/2, 3s1/2, 1g7/22d3/2, 1h11/2, 0j13/2, 1h9/2</td></tr></table>

decay are shown in Table VI; M1 consists of one major shell, including the unusual-parity intruder orbit, while M4 consists of states with width less than 1 MeV.

TABLE VI. Model spaces used in this work to describe $^ \mathrm { 1 0 4 }$ Te alpha decay.   

<table><tr><td>Model</td><td>Neutron States</td><td>Proton States</td></tr><tr><td>M1</td><td>0g7/2, 1d5/2, 2s1/2, 1d3/2
0h11/2</td><td>0g7/2, 1d5/2, 2s1/2, 1d3/2
0h11/2</td></tr><tr><td>M4</td><td>0g7/2, 1d5/2, 2s1/2, 1d3/2
0h11/2, 1f7/2, 2p3/2, 2p1/2
0h9/2, 1f5/2, 0i13/2</td><td>0g7/2, 1d5/2, 2s1/2, 1d3/2
0h11/2, 1f7/2, 0h9/2, 0i13/2</td></tr></table>

# D. Wave functions

For the alpha formation amplitude in $2 1 2$ Po discussed in Sec. IV we considered the model spaces M2, M3 and M4. The wave function amplitudes in M2 were taken from Refs. [14, 56]. For calculations in M3, we took the T =1 seniority-zero amplitudes of Ref. [55] and renormalized them accordingly. For calculations in the extended space M4, we used the renormalized amplitudes of Ref. [15]; here we retained only configurations having width smaller than 1 MeV. The comparison between 212Po and $^ \mathrm { 1 0 4 }$ Te discussed in Sec. VI was carried out in the model spaces M1 and M4. The corresponding wave functions were calculated in the two-particle approximation described in Sec. III B, except for $2 1 2$ Po in the M4 model space, where Ref. [55] was used instead.

# E. Penetration factor

The s.p. alpha width $\Gamma _ { 0 } ^ { s p }$ has been obtained from the current expression (20). The alpha-core potential was

assumed to be of a WS+Coulomb form with the parameters of Ref. [57]: $r _ { 0 } = R _ { c } = 1 . 3 1 5 \mathrm { f m }$ , $a = 0 . 6 5 \mathrm { f m }$ . The strength of the WS potential has been adjusted to reproduce the measured $Q _ { \alpha }$ value corrected by the electron screening term [6, 13, 58–60]:

$$
Q _ {\alpha} = E _ {\alpha} \frac {A _ {P}}{A _ {D}} + \Delta E _ {\mathrm {s c}} \tag {43}
$$

where

$$
\Delta E _ {\mathrm {s c}} = 6 5. 3 Z _ {P} ^ {1. 4} - 8 0 Z _ {P} ^ {0. 4} (\mathrm {e V}). \tag {44}
$$

For 212Po, $E _ { \alpha } = 8 . 7 8 5$ MeV [54] and $\Delta E _ { \mathrm { s c } } = 3 1 . 8 \mathrm { k e V }$ ; hence, $Q _ { \alpha } = 8 . 9 8 6 \mathrm { M e V }$ . The g.s. alpha decay of 104Te has not been observed. For that reason, we took the value QBEα =5.135 MeV extrapolated down from the bind-ing energy differences in 108Te (3.445 MeV) and 106Te (4.290 MeV) [61]. By adding the screening correction $\Delta E _ { \mathrm { s c } } = 1 6 . 1 \mathrm { k e V }$ , we arrived at $Q _ { \alpha } = 5 . 1 5 1 \mathrm { M e V }$ . The resulting WS potential strength is $V _ { 0 } = 1 4 3 . 4 9 \mathrm { M e V }$ for 212Po and 149.64 MeV for $^ \mathrm { 1 0 4 }$ Te.

The Gamow wave functions were obtained by means of the code anti [50]. The complex energy of the metastable alpha state is $\mathcal { E } _ { \alpha } = ( 8 . 9 8 6 - i 0 . 6 3 2 \times 1 0 ^ { - 1 3 }$ ) MeV for $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ and $\mathcal { E } _ { \alpha } = ( 5 . 1 5 1 - i 0 . 8 1 4 \times 1 0 ^ { - 1 3 } )$ ) MeV for $^ \mathrm { 1 0 4 }$ Te. The outgoing spherical Coulomb-Hankel function $H ^ { + }$ was calculated using the code [62].

# F. Calculation of the spectroscopic factor

The radial integration in the expressions for the spectroscopic factor (23) and the formation amplitude in the normalized SGB (36) have been carried out using 200 Gauss-Legendre mesh-points with the maximum radius of 20 fm.

The s.p. core wave functions entering Eq. (32) are those of the s.p. Hamiltonian of Table I. The radial mesh $R _ { k }$ defining the normalized SGB (26) was taken at equidistant points $R _ { k } = k \Delta R$ . In order to determine the malized SGB: step $\Delta R$ we expanded the s.p. core states $\begin{array} { r } { \tilde { \boldsymbol { u } } ( \boldsymbol { r } ) \equiv \sum _ { k = 1 } ^ { M } a _ { k } \left[ r \tilde { F } _ { 0 } ( r , R _ { k } ) \right] } \end{array}$ $u ( r )$ . Under the in the norcondition that $u _ { \mathrm { d i f f } } ( r ) = | u ( r ) - \tilde { u } ( r ) | | < 0 . 0 0 5 \mathrm { f m ^ { - 1 / 2 } }$ we found that $0 . 4 4 \mathrm { f m } \lesssim \Delta \mathrm { R } \lesssim 0 . 5 7 \mathrm { f m }$ and $R _ { \mathrm { m a x } } \gtrsim 1 4 \mathrm { f m }$ . For this range of $\Delta R$ and $R _ { \mathrm { m a x } }$ the normalized SGB is orthonormal with an accuracy better than $1 0 ^ { - 9 }$ . To illustrate the quality of the resulting expansion, Fig. 1 shows $u _ { \mathrm { d i f f } } ( r )$ for the neutron core states in $^ { 2 0 8 } \mathrm { { P b } }$ .

To calculate the modified formation amplitude $G ( R )$ , one needs to determine the eigenvalue cutoff $n _ { \mathrm { m i n } }$ . To this end, we show in Figs. 2 and 3 typical distribution of the eigenvalues $n _ { \nu }$ of the norm kernel (25) for 212Po and $^ \mathrm { 1 0 4 }$ Te, respectively, for different values of $\Delta R$ . One may observe that a significant fraction of them accumulate at zero [53, 63]. To eliminate these spurious eigenvectors, we define the cutoff at the value where the eigenvalue distribution changes slope. For $2 1 2$ Po and $^ \mathrm { 1 0 4 }$ Te this happens

![](images/9df0402abd178a51d365ab2a311795f6d07db55cde5815b681f4d12e94f8f5c1.jpg)  
FIG. 1. $u _ { \mathrm { d i f f } } ( r ) = | u ( r ) - \tilde { u } ( r ) |$ for the neutron core states in $^ { 2 0 8 }$ Pb for $\Delta R = 0 . 5 \mathrm { f m }$ , $M = 3 0$ , and $R _ { \mathrm { m a x } } = 1 5 \mathrm { f m }$ .

![](images/0f2e7d9b472a49de2930e65575b57f7be0a9c6cfb7266f334af35e20feb10662.jpg)  
FIG. 2. Eigenvalues of the norm kernel (25) for ${ } ^ { 2 1 2 } \mathrm { P o }$ for $R _ { \mathrm { m a x } } = 1 3$ fm for different values of $\Delta R$ .

at $n _ { \nu }$ around $1 0 ^ { - 3 }$ . Consequently, in our calculations, we adopt the cutoff value of $n _ { \mathrm { m i n } } = 0 . 0 0 1$ .

The eigenfunctions $u _ { \nu } ^ { L } ( R )$ of the norm kernel (34) are orthonormal with an accuracy of $1 0 ^ { - 1 0 }$ for all eigenvalues. The eigenfunctions with $n _ { \nu } < n _ { \mathrm { m i n } }$ oscillate inside the nuclear volume and vanish outside the surface region. To further check the quality of $u _ { \nu } ^ { L } ( R )$ we compute expression (35) by assuming $n _ { \mathrm { m i n } } = 0$ and $n _ { \nu } = 1$ for all $\nu$ . In this case, Eq. (35) formally reduces to $g ( R )$ . Figure 4 shows $g ( R )$ for $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ calculated in this way. The agreement with the original formation amplitude is excellent, except for a small deviation close to $R = 0$ and a small oscillation around and beyond the nuclear surface, which is not visible in the scale of Fig. 4.

Next we study the sensitivity of $\boldsymbol { S }$ to the choice of $R _ { \mathrm { m a x } }$ , $\Delta R$ , and $n _ { \mathrm { m i n } }$ . For this analysis we relax the condition for $u _ { \mathrm { d i f f } } ( r )$ in order to access a wider range of $\Delta R$ . First, we study the sensitivity of $\boldsymbol { S }$ as a function of $R _ { \mathrm { m a x } }$ for various values of $\Delta R$ . Figure 5 shows the result for $0 . 5 3 \mathrm { f m } \le \Delta \mathrm { R } \le 0 . 5 9$ fm for 212Po in the model

![](images/49a4790ef58d2911bc3b234ce735bd66f5761a692f53fd803040bddf38ba0013.jpg)  
FIG. 3. Similar as in Fig. 2 except for $^ \mathrm { 1 0 4 }$ Te and $R _ { \mathrm { m a x } } = 1 0$ fm.

![](images/8c43f1f09a81fa4bff4f36723bec26be43de00c2514940f2c423e41ebcaa9bc2.jpg)  
FIG. 4. Formation amplitude $g ( R )$ for $\mathrm { ^ { 2 1 2 } P o }$ in the M4 model space expanded in eigenfunctions of the norm kernel for $\Delta R = 0 . 5 0 0$ fm and $R _ { \mathrm { m a x } } = 1 3$ fm.

space M4 and $n _ { \mathrm { m i n } } = 0 . 0 0 1$ . Except for a small value of $\Delta R = 0 . 5 3 \mathrm { f m }$ , which does not produce stable results, a plateau in $R _ { \mathrm { m a x } }$ is reached around 14 fm.

The dependence of $\boldsymbol { S }$ on $\Delta R$ displayed in Fig. 5 reflects the fact that for too small values of the step the basis functions become numerically linearly dependent, while for too large $\Delta R$ ’s the basis cannot capture high Fourier components [43, 53, 63]. Figure 6 shows $\boldsymbol { S }$ for $2 1 2$ Po in the model space M4 and $n _ { \mathrm { m i n } } = 0 . 0 0 1$ as a function of $\Delta R$ . In general, appreciable oscillations of $\boldsymbol { S }$ can be seen except for the “safe” region $0 . 5 4 \mathrm { f m } \le \Delta \mathrm { R } \le 0 . 5 9$ fm, where results weakly depend on $R _ { \mathrm { m a x } }$ .

Finally, Fig. 7 shows the behavior of $\boldsymbol { S }$ as a function of the eigenvalue cutoff $n _ { \mathrm { m i n } }$ for $\Delta R \ : = \ : 0 . 5 7 \mathrm { f m }$ . The cutoff used in Figs. 5 and 6 corresponds to n−1/2min $n _ { \mathrm { m i n } } ^ { - 1 / 2 } =$ -1/2 $( 0 . 0 0 1 ) ^ { - 1 / 2 } \approx 3 1 . 5$ .

![](images/835fe195e6923b1a45327dcfacc780fefb131b654daf30662c7b247b7a03dd45.jpg)  
FIG. 5. Convergence of $s$ for ${ } ^ { 2 1 2 } \mathrm { P o }$ (model space M4) as a function of $R _ { \mathrm { m a x } }$ of the normalized SGB for different values of $\Delta R$ (with $n _ { \mathrm { m i n } } = 0 . 0 0 1$ .)

![](images/90c75a7dda8dfa288ca032bb383c42856f769e79a37b94968f949c742e137353.jpg)  
FIG. 6. Similar as in Fig. 5 but as a function of the step size $\Delta R$ for different values of $R _ { \mathrm { m a x } }$ .

# G. Integral over intrinsic coordinates

The multidimensional integral (12) depends on the nucleonic coordinates, which are parametrized in terms of intrinsic variables through Eqs. (9) and (10). The integration over $\tilde { \varphi } _ { i }$ can easily be done analytically. Since the coordinates of particles 1 and 2 depend only on the relative coordinates 1 and 3, and the particle coordinates 3 and 4 depend only on the relative coordinates 2 and 3, one can greatly simplify the remaining six-dimensional integral by making first the integration over the relative coordinates 1 and 2 and then the integration over the coordinate 3:

$$
\int d \boldsymbol {\rho} _ {3} \left[ \dots \left(\int \dots d \boldsymbol {\rho} _ {1}\right) \left(\int \dots d \boldsymbol {\rho} _ {2}\right) \right]. \tag {45}
$$

The integration has been carried out using the Gauss-Legendre quadrature using 10 points for the radial integrals and 8 points for the the angular coordinates. This

![](images/5578096870eed4855842c7691db14a525219951f33bc21e9ae531dd556860b34.jpg)  
FIG. 7. Similar as in Fig. 5 but as a function of $n _ { \mathrm { m i n } }$ for different values of $R _ { \mathrm { m a x } }$ and $\Delta R = 0 . 5 7$ .

guarantees the convergence up to the fourth significant digit.

# IV. REDUCED WIDTH FOR 212Po

# A. Single- $j$ configuration

Following Rasmussen [32], it is instructive to compute relative reduced widths assuming a pure single- $j _ { n }$ shell model orbital assignment for the neutron pair, while the proton pair fills the $0 h _ { 9 / 2 }$ shell. For simplicity, the results are expressed relative to the $^ { 2 1 0 }$ Po reference (a neutron pair in $2 p _ { 1 / 2 }$ ).

In the delta-function approximation of Sec. II B, the ratio $r _ { \delta }$ of the reduced widths is given by a simple expression [32]:

$$
r _ {\delta} = \frac {\gamma_ {j _ {n}} ^ {2}}{\gamma_ {2 p _ {1 / 2}} ^ {2}} = \frac {2 j _ {n} + 1}{2} \left(\frac {u _ {j _ {n}} (R)}{u _ {2 p _ {1 / 2}} (R)}\right) ^ {4}. \tag {46}
$$

In a more general case expressed by Eq. (11), the ratio $r$ depends on the proton wave function:

$$
r = \frac {\gamma_ {j _ {n} , 0 h _ {9 / 2}} ^ {2}}{\gamma_ {2 p _ {1 / 2} , 0 h _ {9 / 2}} ^ {2}} = \frac {2 j _ {n} + 1}{2} \left(\frac {I _ {j _ {n} , 0 h _ {9 / 2}} (R)}{I _ {2 p _ {1 / 2} , 0 h _ {9 / 2}} (R)}\right) ^ {2}. \quad (4 7)
$$

Table VII compares the ratio $r _ { \delta }$ given by Eq. (46) using the WS wave functions with that of Table I of Rasmussen [32] based on the rounded square well potential of Blomqvist and Wahlborn [64] for several neutron configurations at $R = 9 . 5 \mathrm { f m }$ . We find excellent agreement between these two calculations, and we checked that this agreement also holds for $R = 9 . 0 \mathrm { f m }$ . This is not surprising as both calculations employ finite-depth potentials. The fourth column of Table VII displays the ratio $r$ given by Eq. (47) using the WS wave functions; they are compared with the h.o. values of Ref. [65] (last column). It

TABLE VII. Single- $j$ alpha reduced width ratios at $R = 9 . 5$ fm. Shown are: $r \delta$ of Ref. [32], $r \delta$ of Eq. (46), $r$ of Eq. (47), and $r$ of Ref. [65].   

<table><tr><td>Orbital jn</td><td>rδ [32]</td><td>rδ</td><td>r</td><td>r [65]</td></tr><tr><td>0i13/2</td><td>0.44</td><td>0.46</td><td>0.20</td><td>0.10</td></tr><tr><td>0i11/2</td><td>0.32</td><td>0.34</td><td>0.21</td><td>0.08</td></tr><tr><td>1g9/2</td><td>7.50</td><td>7.50</td><td>6.50</td><td>3.73</td></tr><tr><td>1f5/2</td><td>0.73</td><td>0.74</td><td>0.58</td><td>0.55</td></tr><tr><td>2p3/2</td><td>1.89</td><td>1.89</td><td>1.73</td><td>1.89</td></tr></table>

is seen that h.o. calculations underestimate WS values for high- $j$ orbits by a factor two-to-three.

It has been early recognized [28, 32] that the deltafunction approximation overestimates the contributions of high- $j$ orbitals. One can see it clearly by comparing the values of $r _ { \delta }$ of Eq. (46) with those of $r$ (47), i.e., the third and fourth columns of Table VII. To cure this deficiency, a correction factor $B _ { \nu }$ (15) was introduced [32] in Eq. (14) that depends on the relative angular momentum.

# B. Enhancement due to configuration mixing

As was first shown by Harada [14], the reduced width at the surface region is strongly enhanced by the configuration mixing because contributions from various shell model orbits add coherently. To assess the effect of collective enhancement due to the configuration mixing, we carried out calculations in the M2 space. For $R = 8 \mathrm { f m }$ , our WS calculations yield the enhancement factor of $\zeta = 8 . 5$ with respect to the valence-shell configuration M0. This is to be compared with $\zeta = 1 1$ obtained in the delta-function approximation; $\zeta = 1 0$ obtained by Rasmussen [32]; and $\zeta = 5 . 5$ of Harada [14] using h.o. wave functions.

For the model space M3 of Glendenning and Harada [55], obtained by adding the intruder neutron state $0 j _ { 1 5 / 2 }$ to M2, we obtain $\zeta ~ = ~ 2 1$ . This should be compared with $\zeta = 2 4$ obtained in the delta-function approximation and $\zeta = 3 0$ obtained in Ref. [55] (also within the delta-function approximation) using a fairly rich wave function that also includes proton-neutron correlations and $J > 0$ two-particle couplings. It is worth noting that our enhancement is around 80% of that by Glendenning and Harada, and that the seniority-zero component in their wave function is also 80%.

# C. Extended shell model space

Due to the strong collective enhancement of the reduced width due to configuration mixing, it is important to consider extended shell-model space by taking into account higher-lying orbitals [15]. For finite-depth shellmodel potentials, such as the WS potential used in this study, this necessitates a proper treatment of the particle

continuum. An appropriate representation to deal with the continuum space is the complex Berggren ensemble representing bound and unbound s.p. states [66, 67].

Here we consider the large configuration space M4 of Tonozuka and Arima [15], i.e., all s.p. orbits up to $N = 7$ harmonic oscillator shell except for broad resonances with widths greater than 1 MeV. The shell-model amplitudes were taken from Ref. [15] and renormalized to the reduced model space. For the sake of comparison with Ref. [15], we consider the relative reduced width

$$
\theta^ {2} (R) = \frac {\gamma^ {2} (R)}{\gamma_ {W} ^ {2} (R)}, \tag {48}
$$

where $\begin{array} { r } { \gamma _ { W } ^ { 2 } ( R ) = \frac { 3 \hbar ^ { 2 } } { 2 \mu R ^ { 2 } } } \end{array}$ is the Wigner limit [68].

Table VIII compares our WS results for $\theta ^ { 2 } ( R )$ with those of Ref. [15] obtained in the h.o. basis for several values of $R$ . Generally, the reduced width obtained in

TABLE VIII. The relative reduced width $\theta ^ { 2 }$ (48) obtained in Ref. [15] and this work.   

<table><tr><td>Model space</td><td>R (fm)</td><td>Ref. [15]</td><td>This work</td></tr><tr><td>M0</td><td>8.4</td><td>6.3 × 10-6</td><td>0.60 × 10-6</td></tr><tr><td>M3</td><td>8.5</td><td>4.4 × 10-5</td><td>0.48 × 10-5</td></tr><tr><td>M4</td><td>9.0</td><td>2.9 × 10-4</td><td>0.41 × 10-4</td></tr></table>

the WS model is about one order of magnitude smaller than that in the h.o. basis. This is because the h.o. basis knows nothing about the particle thresholds, and the radial behavior at large distances is solely determined by the oscillator length. For that reason, calculations based on the h.o. wave functions show large sensitivity to this parameter [69].

![](images/de4ed71505a1c83729c557801451b87ae8939ea8a2818a292169c4d087cf6244.jpg)  
FIG. 8. Formation amplitude $g ( R )$ for 212Po obtained in this work in the model spaces M0 to M4 as defined in table V. The imaginary part of the formation amplitude in M4 (dotted line) is also shown.

The formation amplitude obtained in this work is shown in Fig. 8 for the configuration spaces M0, M1,

M2, M3, and M4. Compared with the formation amplitudes of Ref. [15], the maximum of the formation amplitudes obtained in the WS model are significantly larger, and appear at lower values of $R$ , than in the h.o. model. Also the overall shape of the formation amplitude is very different in the two cases. A characteristic two-humped shape of $g ( R )$ calculated in M4 resembles the formation amplitude $G ( R )$ obtained in Refs. [15, 42]. A similar result was also obtained in Refs. [20, 21]. It is indeed interesting to see that a two-humped behavior of the formation amplitude for $^ { 2 1 2 }$ Po has been obtained by considering large configuration space and the Berggren ensemble of the WS potential.

Figure 8 also shows that the formation amplitude in the M4 model space has a small imaginary part. This is because our calculations are carried out in the pole approximation that ignores the non-resonant continuum [67, 70–72]. This spurious component of $g ( R )$ results in a very small imaginary contribution to the reduced width, which can be safely neglected considering the expected accuracy of our model.

# V. ABSOLUTE ALPHA-DECAY WIDTH OF 212Po

The g.s. alpha-decay width of $^ { 2 1 2 }$ Po has been determined in the seniority-zero approximation using three different models spaces listed in Table V: M0, M3, and M4. The corresponding four-particle shell-model wave function contains one configuration in the M0 space, 12 configurations in M3, and 144 seniority zero configurations in M4.

The absolute width from Eq. (1) should not depend on the channel radius $R$ . However, in R-matrix studies involving approximations, such as the one-channel R-matrix treatment, this condition cannot be met [22]. Therefore, in practical calculations, in which the dependence of $\Gamma _ { L }$ on $R$ around the nuclear surface is small relative to the appreciable $R$ -dependence of the formation amplitude, one is trying to meet the plateau condition for $\Gamma _ { L } ( R )$ in which the absolute width varies weakly around the nuclear surface [73]. Figure 9 shows the dependence of the R-matrix width (1) on the channel radius. It is seen that the plateau condition is met only in the case of the extended configuration space M4 involving particle continuum. Here, we find a fairly weak variation of $\Gamma ( R )$ between 7 fm and 11 fm.

As seen in Fig. 9, and discussed in Sec. IV B and Refs. [15, 69, 74], the width strongly increases with the size of the shell-model space. Indeed, in the surface region, $\Gamma ( R )$ obtained in M3 shows an enhancement ${ \sim } 1 5$ with respect to M0, and in the extended space M4 the enhancement is ${ \sim } 2 6 0$ . Compared to experimental value, however, the width obtained in M4 is still 600 times smaller than the experimental value $\Gamma _ { \mathrm { e x p } } = 0 . 1 5 3 \times 1 0 ^ { - 1 4 }$ MeV [54].

A further enhancement in the reduced width is due to

![](images/0ce6b7900bad2d07efd8f5533dc53713bfab30ab76fd8fe8d53706859d1328fb.jpg)  
FIG. 9. Dependence of the absolute alpha-decay width (1) of $^ { 2 1 2 }$ Po on the R-matrix channel radius $R$ for three different model spaces M0, M3 and M4.

the antisymmetrization and normalization of the channel decay [38, 42]. This is achieved by replacing the standard formation amplitude $g ( R )$ with the modified formation amplitude $G ( R )$ of Eq. (24). Figure 10 shows $G ( R )$ calculated in the M4 model space with $\Delta R = 0 . 5 6$ fm, $R _ { \mathrm { m a x } } = 1 1 . 7 6$ fm ( $M = 2 1$ ) and $n _ { \mathrm { m i n } } = 0 . 0 0 1$ . A small oscillation at the tail of $G ( R )$ can be seen. The amplitude of this oscillation, around the asymptotic behavior given by $H _ { 0 } ^ { + } ( \eta , k R )$ , varies very little with $R _ { \mathrm { m a x } }$ for this value of $\Delta R$ . As discussed in, e.g., [3, 42, 45], the behavior of $g ( R )$ and $G ( R )$ is generally very different. This can be seen by comparing Figs. 8 and 10.

![](images/7d859439e0f9e984961d362d495a34a8ea57cb69676c0f1d7600128dcac39913.jpg)  
FIG. 10. Modified formation amplitude $G ( R )$ of Eq. (24) in the extended model space M4 with $n _ { \mathrm { m i n } } = 0 . 0 0 1$ , $\Delta R = 0 . 5 6$ fm and $R _ { \mathrm { m a x } } = 1 1 . 7 6$ . Unlike $g ( R )$ , $G ( R )$ properly accounts for the normalization and antisymmetrization of the decay channel. The asymptotic behavior of $G ( R )$ is given by the Coulomb-Hankel function at the alpha-decay energy $Q _ { \alpha } =$ 8.986 MeV (dashed line).

The absolute alpha-decay width obtained by using the R-matrix expression (1) with the formation amplitude

$G ( R )$ of Fig. 10 is shown in Fig. 11. There appears a small plateau in the region of nuclear surface that corresponds to $\Gamma \approx 0 . 0 0 4 2 \times 1 0 ^ { - 1 4 }$ MeV. This value is $\sim 3 6$ times smaller than $\Gamma _ { \mathrm { e x p } }$ . At larger distances $R > 9 \mathrm { f m }$ , the result is affected by spurious oscillations of $G ( R )$ around $H _ { 0 } ^ { + } ( \eta , k R )$ , i.e., it is quite unreliable.

![](images/a443cdf4b7192b7e82fc733197107ff479aeffc329767d21e054658d2dad065b.jpg)  
FIG. 11. Absolute width from R-matrix expression (1) calculated in the M4 model space using the modified formation amplitude $G ( R )$ of Fig. 10. At $R > 9 \mathrm { f m }$ , the result obtained by assuming $G ( R ) \propto H _ { 0 } ^ { + } ( \eta , k R )$ is marked by a dotted line.

The absolute width can also be obtained from expression (2), which involves the alpha-particle spectroscopic factor $\boldsymbol { S }$ and the s.p. decay width. Figure 12 shows the result of the current expression (20) for $\Gamma ^ { s p }$ as a function of the channel radius. As discussed in Ref. [36], $\Gamma ^ { s p }$ calculated this way should be independent of $R$ if $R$ is large enough. This is precisely what is seen in Fig. 12: the s.p. width converges beyond the range of the WS potential to $\Gamma ^ { s p } = 0 . 1 2 4 7 \times 1 0 ^ { - 1 2 }$ MeV, which is indeed very close to the value of $- 2 \mathrm { I m } ( \mathcal { E } _ { \alpha } ) = 0 . 1 2 6 5 \times 1 0 ^ { - 1 2 }$ MeV given by the imaginary part of the Gamow resonance.

Using the modified formation amplitude $G ( R )$ of Fig. 11, we compute the spectroscopic factor $S = 0 . 0 1 1$ , which – combined with the value of $\Gamma ^ { s p }$ above – yields $\Gamma = 0 . 1 4 \times 1 0 ^ { - 1 4 }$ MeV. Using $\Delta R = 0 . 5 5$ fm we obtain $ { \boldsymbol { S } } = 0 . 0 0 8 0$ and $\Gamma = 0 . 1 0 \times 1 0 ^ { - 1 4 }$ MeV. Both these values are close to $\Gamma _ { \mathrm { e x p } } = 0 . 1 5 3 \times 1 0 ^ { - 1 4 } \mathrm { M e V }$ .

# VI. COMPARISON BETWEEN GROUND-STATE ALPHA DECAY OF $^ { 2 1 2 }$ Po AND 104Te

To compare absolute widths of $2 1 2$ Po and $^ \mathrm { 1 0 4 }$ Te in a consistent way, we consider similar M1 and M4 model spaces for both nuclei. The norm kernel eigenvalues $n _ { \nu }$ do not depend on the model space in which $g ( R )$ is calculated, so we take the cutoff $n _ { \mathrm { m i n } } = 0 . 0 0 1$ .

Let us begin with $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ by making a convergence analysis of $\boldsymbol { S }$ in the M1 model space as a function of $\Delta R$ and $R _ { \mathrm { m a x } }$ (as in Fig. 5). For $\Delta R = 0 . 5 3$ , 0.54, 0.55, and

![](images/735fb2863dfb42b1d8dcb372bb2a15bfc7ef02a06ba6bb3b5ad143226f1e9013.jpg)  
FIG. 12. Single particle width of $^ { 2 1 2 }$ Po from current expression (20).

0.56 fm, we found $S = 0 . 0 0 4 1$ , 0.0011, 0.00030, 0.00032, respectively. The resulting converged value $S = 0 . 0 0 0 3$ is too small, as expected from Fig. 8. This deficiency is related to the poor quality of the interaction used to describe $^ { 2 1 2 }$ Po in M1. To better understand this fact, let us take a look of the spectroscopic factor in terms of the spectral representation of the norm kernel,

$$
\mathcal {S} = \sum_ {\nu} \frac {g _ {\nu} ^ {2}}{n _ {\nu}}, \tag {49}
$$

where the sum is truncated by the condition $n _ { \nu } > n _ { \mathrm { m i n } }$ . The summation range and eigenvalues $n _ { \nu }$ are the same for M1 and M4; the only difference comes from $g _ { \nu }$ . Because of the rapid oscillation of the eigenfunctions inside the nucleus, only the eigenfunctions which are peaked at and beyond the nuclear surface will contribute significantly to the sum. But – because $g ( R )$ in M1 is small in the surface region – the overlap with those eigenfunctions is small, and this gives rise to a very reduced value of $\boldsymbol { S }$ .

By making a similar analysis for $^ \mathrm { 1 0 4 }$ Te in M1, we found $S = 0 . 0 6 7$ , 0.024, 0.0066, and 0.00046 for $\Delta R =$ 0.53, 0.54, 0.55, and 0.56 fm, respectively. In the model space M4 we found $S = 0 . 2 1$ , 0.088, 0.032, and 0.0051 for the same values of $\Delta R$ . Clearly, the convergence in $\boldsymbol { S }$ has not been achieved for $^ \mathrm { 1 0 4 }$ Te. We would like to attribute this to the impact of the proton continuum on $g _ { \nu }$ , which results in increased oscillations of $G ( R )$ in the surface area. Table IX compares the values of $\boldsymbol { S }$ and the corresponding absolute widths for $2 1 2$ Po and $^ { 1 0 4 } \mathrm { T e }$ at $\Delta R = 0 . 5 6 \mathrm { f m }$ . (The single particle width for Te is $\Gamma ^ { s p } = 0 . 1 6 2 \times 1 0 ^ { - 1 2 }$ MeV.)

It is interesting to compare our current results for $^ \mathrm { 1 0 4 }$ Te with the estimates of phenomenological alpha-decay models based on semi-classical approximation [75–77]. The assumed large value of $Q _ { \alpha } = 6 . 1 2 \mathrm { M e V }$ in Ref. [75] results in a very short half-life of $7 \times 1 0 ^ { - 1 1 }$ sec. The alphadecay energies of 5.05 MeV [76] and 5.42±0.07 MeV [77] result in $T _ { 1 / 2 } \sim 1 0 ^ { - 7 } \mathrm { s }$ ec and $\sim 5 \times 1 0 ^ { - 9 }$ sec, respectively, and these estimates are not inconsistent with our

TABLE IX. Alpha decay spectroscopic factor and absolute width for $\scriptstyle { ^ { 2 1 2 } \mathrm { P o } }$ and $^ \mathrm { 1 0 4 }$ Te computed in the configuration spaces M1 and M4, with $n _ { \mathrm { m i n } } ~ = ~ 0 . 0 0 1$ , $\Delta R ~ = ~ 0 . 5 6$ and $R _ { \mathrm { m a x } } = 1 1 . 7 6 \mathrm { f m } \left( \mathrm { M } = 2 1 \right)$ .   

<table><tr><td rowspan="2">Model Space</td><td colspan="2">S</td><td colspan="2">Γ × 1014MeV</td></tr><tr><td>212Po</td><td>104Te</td><td>212Po</td><td>104Te</td></tr><tr><td>M1</td><td>0.00032</td><td>0.00046</td><td>0.0040</td><td>0.0075</td></tr><tr><td>M4</td><td>0.011</td><td>0.0051</td><td>0.14</td><td>0.083</td></tr></table>

value (M4 model space) $T _ { 1 / 2 } = 5 . 5 \times 1 0 ^ { - 7 } \mathrm { s e c }$ ( $Q _ { \alpha } =$ 5.151 MeV). As the value of $Q _ { \alpha }$ in $^ \mathrm { 1 0 4 }$ Te is very uncertain, we show in Fig. 13 the absolute width and half-life $T _ { 1 / 2 }$ as a function of $Q _ { \alpha }$ for the model space M4.

![](images/2994b0d7c65625db6e370572f8acdea37ff75995c398e4c82b19cb3faddb2695.jpg)  
FIG. 13. Ground-state alpha-decay width (left scale) and half-life (right scale) in $^ \mathrm { 1 0 4 }$ Te as functions of the decay energy.

Our predicted spectroscopic factors in M4 for $^ \mathrm { 1 0 4 }$ Te and 212Po are about 0.5% and 1%, respectively. As mentioned above, a fairly small value of $\boldsymbol { S }$ in $^ \mathrm { 1 0 4 }$ Te could be a consequence of the proximity of the proton continuum. Indeed, all the valence proton shells are resonances. The small value of $\boldsymbol { S }$ in $^ \mathrm { 1 0 4 }$ Te could also be attributed to the poor quality of the valence interaction assumed, and the neglect of the $T = 0$ force. The effect of the protonneutron interaction was examined in, e.g., Refs. [14, 78] for 212Po and was found to be minor due to the fact that neutrons and protons in $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ occupy different shells. This is no longer true in the $N = Z$ nucleus $^ \mathrm { 1 0 4 }$ Te, in which the major enhancement of $\boldsymbol { S }$ is expected due to $T = 0$ correlations. Therefore, our predictions for $\boldsymbol { S }$ and $\Gamma$ in $^ \mathrm { 1 0 4 }$ Te given in Table IX should be considered as a very conservative lower limit.

# VII. CONCLUSIONS

The g.s. alpha decay of $2 1 2$ Po has been studied within the complex-energy shell model framework with the Berggren ensemble of the average Woods-Saxon potential. We applied the pole approximation by consider-

ing s.p. resonant states only. The overlap integral involving alpha-cluster nucleons was computed exactly, without resorting to the delta-function approximation. We considered the large valence space of Tonozuka and Arima that is necessary to produce the collective enhancement of the formation amplitude.

The absolute alpha-decay width was computed using the reduced width obtained in the framework of the Rmatrix theory and also from the alpha spectroscopic factor. The latter approach yielded results consistent with experimental value, but only after considering the antisymmetrization and normalization of the decay channel wave function. The R-matrix estimate underestimates the experimental width by a factor of $\sim 3 6$ . The Rmatrix expression depends on the asymptotic value of the formation amplitude that is very sensitive to the size of the configuration space. On the other hand, the reactiontheory expression (2) involves the spectroscopic factor – an integral quantity that depends less on the size of the basis used. It is very encouraging to see that a reasonable agreement with the experimental width of $^ { 2 1 2 }$ Po has been obtained without explicitly considering the alpha-cluster component in the wave function of the parent nucleus. In this context, we believe that the improved treatment of the particle continuum has been essential.

We have also provided an estimate of the alpha-decay rate in $^ \mathrm { 1 0 4 }$ Te. Unfortunately, due to the fact that the valence proton shells in this nucleus lie in the continuum, no fully convergent result has been achieved. We hope to improve the situation in the future by inclusion of the non-resonant continuum space that will remove some of the undesired oscillations in $G ( R )$ at large distances. In addition, since the residual interaction employed in our work neglects the proton-neutron components, and

the wave function has a seniority-zero character based on $T = 1$ nucleonic pairs, the predicted alpha width in this $N = Z$ nucleus should be viewed as a conservative low limit. Indeed, the inclusion of $T = 0$ correlations is expected to increase the value of $\Gamma$ significantly.

The calculations presented in this study should be considered as an important step towards an improved microscopic understanding of the alpha-decay process. Still, as this work demonstrates, further improvements are needed. The neglect of the non-resonant continuum, i.e., complex-energy scattering states in the Berggren ensemble, slightly violates the completeness relation at a one-body level. This results in small imaginary contributions to spectroscopic factors and reduced widths, and – most importantly – can affect the behavior of formation amplitudes at very large distances. The second crucial development will be the use of large-scale shell model calculations, including realistic $T = 0$ and $T = 1$ interactions, to compute wave function amplitudes. This will enable us to provide a more meaningful estimate of $^ \mathrm { 1 0 4 }$ Te alpha decay rate. The work in both directions is underway.

# ACKNOWLEDGMENTS

Useful discussions with Doru Delion, Torsten Fliessbach, Robert Grzywacz, Kiyoshi Kato, and Krzysztof Rykaczewski are gratefully acknowledged. Special thanks to Rezso Lovas for his insights on the norm kernel and his patience in explaining the underlying physics. This work was supported by the Office of Nuclear Physics, U.S. Department of Energy under Contract No. DE-FG02-96ER40963 and by the National Council of Research PIP-77 (CONICET, Argentina).

[1] G. Gamow, Z. Physik 51, 204 (1928).   
[2] E. U. Condon and R. W. Gurney, Nature 122, 439 (1928).   
[3] R. G. Lovas, R. J. Liotta, K. Insolia, K. Varga, and D. Delion, Phys. Rep. 294, 265 (1998).   
[4] P. E. Hodgson and E. Bˇet´ak, Phys. Rep. 374, 1 (2003).   
[5] D. S. Delion, Theory of Particle and Cluster Emission, Lecture Notes in Physics, Vol. 819 (Springer Heidelberg, 2010).   
[6] R. G. Thomas, Prog. Theor. Phys. 12, 253 (1954).   
[7] H. J. Mang, Z. Phys. 148, 582 (1957).   
[8] A. Arima and S. Yoshida, Phys. Lett. B 40, 15 (1972).   
[9] A. Arima and S. Yoshida, Nucl. Phys. A 219, 475 (1974).   
[10] T. Fliessbach, J. Phys. G 2, 531 (1976).   
[11] T. Fliessbach and P. Manakos, J. Phys. G 3, 643 (1977).   
[12] H. D. Zeh, Z. Phys. 175, 490 (1963).   
[13] H. J. Mang, Ann. Rev. Nucl. Sci. 14, 1 (1964).   
[14] K. Harada, Prog. Theor. Phys. 26, 667 (1961).   
[15] I. Tonozuka and A. Arima, Nucl. Phys. A 323, 45 (1979).   
[16] F. A. Janouch and R. J. Liotta, Phys. Rev. C 27, 896 (1983).   
[17] G. Dodig-Crnkovic, F. A. Janouch, R. J. Liotta, and Z. Xiaolin, Phys. Scr. 37, 523 (1988).

[18] S. M. Lenzi, O. Drag´un, E. E. Maqueda, R. J. Liotta, and T. Vertse, Phys. Rev. C 48, 1463 (1993).   
[19] D. S. Delion and J. Suhonen, Phys. Rev. C 61, 024304 (2000).   
[20] S. Okabe, J. Phys. Soc. Jpn. Suppl. 58, 516 (1989).   
[21] K. Varga, R. G. Lovas, and R. J. Liotta, Nucl. Phys. A 550, 421 (1992).   
[22] P. Descouvemont and D. Baye, Rep. Prog. Phys. 73, 036301 (2010).   
[23] A. Insolia, P. Curutchet, R. J. Liotta, and D. S. Delion, Phys. Rev. C 44, 545 (1991).   
[24] Z. Janas, C. Mazzocchi, L. Batist, A. Blazhev, M. G´orska, M. Kavatsyuk, O. Kavatsyuk, R. Kirchner, A. Korgul, M. La Commara, K. Miernik, I. Mukha, A. Plochocki, E. Roeckl, and K. Schmidt, Eur. Phys. J. A 23, 197 (2005).   
[25] S. N. Liddick, R. Grzywacz, C. Mazzocchi, R. D. Page, K. P. Rykaczewski, J. C. Batchelder, C. R. Bingham, I. G. Darby, G. Drafta, C. Goodin, C. J. Gross, J. H. Hamilton, A. A. Hecht, J. K. Hwang, S. Ilyushkin, D. T. Joss, A. Korgul, W. Kr´olas, K. Lagergren, K. Li, M. N. Tantawy, J. Thomson, and J. A. Winger, Phys. Rev.

Lett. 97, 082501 (2006).   
[26] R. D. Macfarlane and A. Siivola, Phys. Rev. Lett. 14, 114 (1965).   
[27] A. M. Lane, Rev.Mod. Phys. 32, 519 (1960).   
[28] H. J. Mang, Phys. Rev. 119, 1069 (1960).   
[29] B. F. Bayman, S. M. Lenzi, and E. E. Maqueda, Phys. Rev. C 41, 109 (1990).   
[30] J. Eichler and H. J. Mang, Zeitschrift f¨ur Physik 183, 321 (1965).   
[31] P. J. Brussaard and H. A. Tlohoek, Physica 24, 263 (1958).   
[32] J. O. Rasmussen, Nucl. Phys. 44, 93 (1963).   
[33] S. Devons and L. J. B. Goldfanb, (1957).   
[34] J. Humblet and L. Rosenfel, Nucl. Phys. C 26, 529 (1961).   
[35] B. Barmore, A. T. Kruppa, W. Nazarewicz, and T. Vertse, Phys. Rev. C 62, 054315 (2000).   
[36] A. T. Kruppa and W. Nazarewicz, Phys. Rev. C 69, 054311 (2004).   
[37] T. Fliessbach, H. J. Mang, and J. O. Rasmussen, Phys. Rev. C 13, 1318 (1976).   
[38] T. Fliessbach, Z. Physik A 272, 39 (1975).   
[39] T. Fliessbach and H. J. Mang, J. Phys. G 4, 1451 (1978).   
[40] A. Watt, D. Kelvin, and R. R. Whitehead, J. Phys. G 6, 31 (1980).   
[41] R. Blendowske, T. Fliessbach, and H. Walliser, Nucl. Phys. A 464, 75 (1987).   
[42] T. Fliessbach and H. J. Mang, Nucl. Phys. A 263, 75 (1976).   
[43] T. Fliessbach, Z. Physik A 277, 151 (1976).   
[44] R. Beck, F. Dickmann, and R. G. Lovas, Ann. Phys. 173, 1 (1987).   
[45] K. Varga, R. G. Lovas, and R. J. Liotta, Phys. Rev. Lett. 69, 37 (1992).   
[46] M. Conze and P. Manakos, J. Phys. G 5, 671 (1979).   
[47] D. Brink, Proc. Int. School of Physics, Enrico Fermi, Course XXXVI. Ed. C. Bloch, Vol. 819 (Varenna, Academic Press, New York, 1966).   
[48] V. Isakov and K. Erokhina, Phys. At. Nucl. 65, 1431 (2002).   
[49] I. G. Darby, R. K. Grzywacz, J. C. Batchelder, C. R. Bingham, L. Cartegni, C. J. Gross, M. Hjorth-Jensen, D. T. Joss, S. N. Liddick, W. Nazarewicz, S. Padgett, R. D. Page, T. Papenbrock, M. M. Rajabali, J. Rotureau, and K. P. Rykaczewski, Phys. Rev. Lett. 105, 162502 (2010).   
[50] L. Gr. Ixaru, M. Rizea, and T. Vertse, Comput. Phys.

Comm. 85, 217 (1995).   
[51] D. R. Bes and R. A. Broglia, Phys. Rev. C 3, 2349 (1971).   
[52] A. Lane, Nuclear Theory (Benjamin, New York, 1964).   
[53] P. Ring and P. Schuck, The Nuclear Many-Body Problem (Springer, 2000).   
[54] National Nuclear Data Center, http://www.nndc.gov.   
[55] N. K. Glendenning and K. Harada, Nucl. Phys. C 72, 481 (1965).   
[56] P. Banerjee and H. Zeh, Z. Phys. 159, 170 (1960).   
[57] R. M. DeVries, J. S. Lilley, and M. A. Franey, Phys. Rev. Lett. 37, 481 (1976).   
[58] K. Toth and J. Rasmussen, Nucl. Phys. 16, 474 (1960).   
[59] J. Rasmussen, Alpha-, Beta-, and Gamma-ray spectroscopy, edited by K. Siegbahn, Lecture Notes in Physics, Vol. 1 (North-Holland, Amsterdam, 1974).   
[60] Y. Hatsukawa, H. Nakahara, and D. Hoffman, Phys. Rev. C 42, 674 (1990).   
[61] K. Rykaczewski and R. Grzywacz, Private communication.   
[62] I. J. Thompson and A. R. Barnett, Comput. Phys. Comm. 36, 363 (1985).   
[63] P. Bonche, J. Dobaczewski, H. Flocard, P.-H. Heenen, and J. Meyer, Nucl. Phys. A 510, 466 (1990).   
[64] J. Blomqvist and S. Wahlborn, Ark. Fys. N 46 16 (1960).   
[65] H. D. Zeh, dissertation Univ. of Heidelberg (unpublished) (1962).   
[66] T. Berggren, Nucl. Phys. A 109, 265 (1968).   
[67] N. Michel, W. Nazarewicz, P loszajczak, and T. Vertse, J. Phys. G 36, 013101 (2009).   
[68] A. M. Lane and R. G. Thomas, Rev. Mod. Phys. 30, 257 (1958).   
[69] K. Harada, Prog. Theor. Phys. 27, 430 (1962).   
[70] T. Berggren and P. Lind, Phys. Rev. C 47, 768 (1993).   
[71] R. Id Betan, R. J. Liotta, N. Sandulescu, and T. Vertse, Phys. Rev. C 67, 014322 (2003).   
[72] N. Michel, W. Nazarewicz, M. P loszajczak, and J. Oko lowicz, Phys. Rev. C 67, 054311 (2003).   
[73] A. Insolia, R. J. Liotta, and E. Maglione, Europhys. Lett. 7, 209 (1988).   
[74] C. Qi, A. N. Andreyev, M. Huyse, R. J. Liotta, P. Van Duppen, and R. A. Wyss, Phys. Rev. C 81, 064319 (2010).   
[75] F. Xu and J. Pei, Phys. Lett. B 642, 322 (2006).   
[76] C. Xu and Z. Ren, Phys. Rev. C 74, 037302 (2006).   
[77] P. Mohr, Eur. Phys. J. A 31, 23 (2007).   
[78] K. Sasaki, S. Suekane, and I. Tonozuka, Nucl. Phys. A 147, 45 (1970).