# Statistical Hauser-Feshbach theory with width fluctuation correction including direct reaction channels for neutron induced reaction at low energies

T. Kawano∗

Theoretical Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA

R. Capote

NAPC–Nuclear Data Section, International Atomic Energy Agency, Vienna A-1400, Austria

S. Hilaire

CEA/DIF, Service de Physique Nucl´eaire, F-91680 Bruy`eres-le-Chˆatel, France

(Dated: May 2, 2016)

A model to calculate particle-induced reaction cross sections with statistical Hauser-Feshbach theory including direct reactions is given. The energy average of scattering matrix from the coupledchannels optical model is diagonalized by the transformation proposed by Engelbrecht and Weidenm¨uller. The ensemble average of $S$ -matrix elements in the diagonalized channel space is approximated by a model of Moldauer [Phys.Rev.C 12, 744 (1975)] using newly parametrized channel degree-of-freedom $\nu _ { a }$ to better describe the Gaussian Orthogonal Ensemble (GOE) reference calculations. Moldauer approximation is confirmed by a Monte Carlo study using randomly generated $S$ -matrix, as well as the GOE three-fold integration formula. The method proposed is applied to the 238U(n,n’) cross section calculation in the fast energy range, showing an enhancement in the inelastic scattering cross sections.

PACS numbers: 24.60.-k,24.60.Dr,24.60.Ky

# I. INTRODUCTION

Neutron scattering in the keV to MeV energy range is one of the most important processes in many fields, for which better understanding of nuclear reaction mechanisms is always crucial. In particular, accurate neutron reaction cross sections are needed for applications such as radiation transport simulations for nuclear technology, particle detector response, nuclear reaction rate calculation for nuclear astrophysics, and so forth. When we calculate the nuclear reaction cross section for a system where the dynamical or static nuclear deformation is involved, the simple regime of the spherical optical model plus the Hauser-Feshbach theory [1] has to be extended to the coupled-channels scheme (e.g. Ref. [2]). Rotational bands built on intrinsic or vibrational levels dominate the low-lying excitation spectra for statically deformed nuclei, and it is well known that these excited rotational states are strongly populated by the collective motion of target nucleus.

Typically, the direct reaction channels in the statistical model have been considered in a perturbed way, in which a flux going into the direct channels is subtracted from the total compound nucleus formation cross section [3], i.e., the direct and compound cross sections are assumed to be independent. Such approximation has a great advantage to reduce computational burden, and therefore, many Hauser-Feshbach codes, such as Empire [4], TALYS [5], CCONE [6], CoH $^ { 3 }$ [7, 8], etc., employ this approxi-

mation to calculate nuclear reaction cross sections. However,it was shown that the existence of direct reaction channels changes the compound reaction cross sections [9]. Therefore it is important to assess the independence of the direct and compound reaction mechanisms quantitatively, which exists implicitly in the approximation aforementioned.

Statistical models for the compound nuclear reaction connect energy average $S$ -matrix elements (or transmission coefficients) to energy average cross sections. While the statistical Hauser-Feshbach theory provides such a link, it has to be modified by the width fluctuation correction that accounts for statistical properties in the resonances. The width fluctuation correction enhances the cross section in the elastic channel, and reduces all other channels to fulfill the unitarity condition. When strongly coupled channels exist, the energy average $S$ -matrix, $\langle S \rangle$ is no-longer diagonal. The imposed unitarity condition yields additional correlations between the elastic and other channels, hence the cross sections will be further modified [10].

Kawai, Kerman, and McVoy (KKM) [10] obtained a formula for the compound nuclear reaction including the direct channels at the strong absorption limit. The actual calculations of KKM are, unfortunately, very limited [11, 12]. In parallel to KKM, inclusion of the direct reaction in the statistical theory was proposed by Engelbrecht and Weidenm¨uller [13], in which $\langle S \rangle$ is diagonalized by a unitary transformation. The statistical model calculation is performed in the diagonalized space, just like the no-direct reaction cases. Hofmann et al. [14] and Moldauer [15] performed the Engelbrecht-Weidenm¨uller (EW) transformation to examine the effects of the di-

rect channels on the compound nuclear reaction. A more general and rigorous theory was proposed by Nishioka, Weidenm¨uller, and Yoshida (NWY) [16] based on the so-called Gaussian Orthogonal Ensemble (GOE) [17] together with the EW transformation. However, the NWY equation obtained is almost impossible to calculate. The most recent study on this subject is by Capote et al. [18], who studied the impact of the EW transformation on a realistic calculation of inelastic scattering on $^ { 2 3 8 }$ U using the coupled-channels optical model code ECIS [19]. An enhancement of the inelastic scattering cross section was found [18], yet the compound reaction model implemented in ECIS is limited and further investigation was needed.

In the case of a spherical nucleus, we obtained a simple relationship between the channel degree-of-freedom $\nu _ { a }$ and the optical model transmission coefficients $T _ { a }$ by applying the Monte Carlo technique to GOE [20], which yields an almost equivalent compound nucleus cross sections to the GOE three-fold integration formula [17]. Such an empirical approach facilitates computations of the Hauser-Feshbach theory in the fast energy range, where the number of open channels tends to be too large to handle. Starting with the approach by Moldauer [15], and adding the idea of GOE three-fold integration, we extend Moldauer’s approach to the actual cross section calculation for deformed nuclei. Since we will show in this paper that our model produces almost identical results to the NWY theory, the calculated nuclear reaction cross sections should be within reasonable uncertainties for many realistic cases. This could be particularly im-

portant to calculate nuclear reaction cross sections for actinides or in the rare earth region, where the static nuclear deformation is large.

# II. THEORY

# A. Hauser-Feshbach theory with width fluctuation correction

In the case of nuclear reaction without direct channels, the Hauser-Feshbach theory with the width fluctuation correction reads

$$
\sigma_ {a b} = \frac {\pi}{k _ {a} ^ {2}} \frac {T _ {a} T _ {b}}{\sum_ {c} T _ {c}} W _ {a b} = \sigma_ {a b} ^ {\mathrm {H F}} W _ {a b}, \tag {1}
$$

where $\sigma _ { a b }$ is the energy average cross section from channel a to b, σHFab $a$ $b$ $\sigma _ { a b } ^ { \mathrm { H F } }$ is the Hauser-Feshbach cross section, $k _ { a }$ is the wave-number of projectile, $W _ { a b }$ is the width fluctuation correction factor, and $T _ { c }$ is the transmission coefficient in channel $c$ calculated with the optical model $S$ -matrix element $T _ { c } = 1 - \vert \left. { S _ { c c } } \right. \vert ^ { 2 }$ . Hereafter we omit the kinematic factor of $\pi / k _ { a } ^ { 2 }$ , unless otherwise specified.

The width fluctuation correction factor is given by the Gaussian Orthogonal Ensemble (GOE) model of Verbaarschot, Weidenm¨uller, and Zirnbauer [17]. This model gives an ensemble average of the fluctuation part, ab cdbe calculated as a ratio to $S _ { a b } S _ { c d } ^ { * }$ , and the width fluctuation correction factor can $\sigma _ { a b } ^ { \mathrm { H F } }$ . The so-called GOE tripleintegral formula is [17]

$$
\overline {{S _ {a b} S _ {c d} ^ {*}}} = \frac {1}{8} \int_ {0} ^ {\infty} d \lambda_ {1} \int_ {0} ^ {\infty} d \lambda_ {2} \int_ {0} ^ {1} d \lambda \mu (\lambda , \lambda_ {1}, \lambda_ {2}) \prod_ {c} \frac {1 - T _ {c} \lambda}{\sqrt {(1 + T _ {c} \lambda_ {1}) (1 + T _ {c} \lambda_ {2})}} J (\lambda , \lambda_ {1}, \lambda_ {2}), \tag {2}
$$

where

$$
\mu (\lambda , \lambda_ {1}, \lambda_ {2}) = \frac {\lambda (1 - \lambda) | \lambda_ {1} - \lambda_ {2} |}{\sqrt {\lambda_ {1} (1 + \lambda_ {1})} \sqrt {\lambda_ {2} (1 + \lambda_ {2})} (\lambda + \lambda_ {1}) ^ {2} (\lambda + \lambda_ {2}) ^ {2}}, \tag {3}
$$

$$
\begin{array}{l} J (\lambda , \lambda_ {1}, \lambda_ {2}) = \delta_ {a b} \delta_ {c d} \overline {{S}} _ {a a} \overline {{S}} _ {c c} ^ {*} T _ {a} T _ {c} \left(\frac {\lambda_ {1}}{1 + T _ {a} \lambda_ {1}} + \frac {\lambda_ {2}}{1 + T _ {a} \lambda_ {2}} + \frac {2 \lambda}{1 - T _ {a} \lambda}\right) \left(\frac {\lambda_ {1}}{1 + T _ {c} \lambda_ {1}} + \frac {\lambda_ {2}}{1 + T _ {c} \lambda_ {2}} + \frac {2 \lambda}{1 - T _ {c} \lambda}\right) \\ + (\delta_ {a c} \delta_ {b d} + \delta_ {a d} \delta_ {b c}) T _ {a} T _ {b} \left\{\frac {\lambda_ {1} (1 + \lambda_ {1})}{(1 + T _ {a} \lambda_ {1}) (1 + T _ {b} \lambda_ {1})} + \frac {\lambda_ {2} (1 + \lambda_ {2})}{(1 + T _ {a} \lambda_ {2}) (1 + T _ {b} \lambda_ {2})} + \frac {2 \lambda (1 - \lambda)}{(1 - T _ {a} \lambda) (1 - T _ {b} \lambda)} \right\}. (4) \\ \end{array}
$$

The compound cross section is readily calculated as $\overline { { S _ { a b } S _ { a b } ^ { * } } } = | S _ { a b } | ^ { 2 } = \sigma _ { a b }$ when $\langle S \rangle$ is provided, beside the time-consuming three-fold integration [21]. The GOE model is believed to be a correct answer to the calculation of the compound cross section. However, it is not so practical to apply Eq. (2) to realistic cases. For example, a compound nucleus after a particle or photon emission is often left in the continuum state, where the decay channel is not well defined. Even if we approximate the transition to one of the continuum bins by a pseudo-single

level, the calculation time will be enormous when there are many open channels. Alternatively, there are several models to evaluate $W _ { a b }$ . We adopt Moldauer’s model [15, 22–24], since Hilaire, Lagrange, and Koning [25] reported that this model is practically accurate enough. The width fluctuation correction factor can be evaluated numerically as

$$
W _ {a b} = \left(1 + \frac {2 \delta_ {a b}}{\nu_ {a}}\right) \int_ {0} ^ {\infty} \frac {d t}{F _ {a} (t) F _ {b} (t) \prod_ {k} F _ {k} (t) ^ {\nu_ {k} / 2}}, (5)
$$

$$
F _ {k} (t) = 1 + \frac {2}{\nu_ {k}} \frac {T _ {k}}{\sum_ {c} T _ {c}} t, \tag {6}
$$

where $\nu _ { a }$ is the channel degree-of-freedom, which is related to the channel transmission coefficient $T _ { a }$ . There are, again, several models to express $\nu _ { a }$ by $T _ { a }$ , which were derived by a Monte Carlo study, such as that of Moldauer [26], Ernebjerg and Herman [27], or of LANL [20]. We here employ the most recent model from LANL [20], because it produces almost identical $W _ { a b }$ compared to the GOE triple-integral calculation [9].

# B. Generalized transmission coefficient

When direct reaction channels exist, in other words, the optical model $S$ -matrix is not diagonal, the Hauser-Feshbach cross section in Eq. (1) should be further modified. In this case the energy average $S$ -matrix is given by the coupled-channels calculation. When combining the coupled-channels method with the Hauser-Feshbach theory, the existing cross section calculation codes, such as Empire [4], TALYS [5], CCONE [6], and CoH3 [7], adopt a “direct cross section eliminated” transmission coefficient. This is defined as the probability of formation of compound nucleus on the $n$ -th state by a nucleon having the orbital angular momentum and spin of $i , j$ :

$$
T _ {l j} ^ {(n)} = \sum_ {J \Pi} \sum_ {c} g _ {J c} \left(1 - \sum_ {c ^ {\prime}} | \langle S _ {c c ^ {\prime}} ^ {J \Pi} \rangle | ^ {2}\right) \delta_ {n _ {c}, n} \delta_ {l _ {c}, l} \delta_ {j _ {c}, j}, \tag {7}
$$

where the suffix $c$ indicates the quantum number in the channel, $J \Pi$ is the total spin and parity, and $g _ { J c }$ is the spin factor

$$
g _ {J c} = \frac {2 J + 1}{\left(2 j _ {c} + 1\right) \left(2 I _ {c} + 1\right)}. \tag {8}
$$

$I _ { c }$ is the spin of the nucleus state. Equation (7) gives a partial-wave contribution to the total compound formation cross section when the target is in its $n$ -th state

$$
\sigma^ {\mathrm {C N} (n)} = \frac {\pi}{k _ {n} ^ {2}} \sum_ {l j} \frac {2 j + 1}{2 s + 1} T _ {l j} ^ {(n)}, \tag {9}
$$

where $s$ is the intrinsic spin of incoming particle. Because we eliminate the off-diagonal elements in $\langle S \rangle$ by Eq. (7), the meaning of the transmission coefficient is different from the no-direct reaction case. We call this a generalized transmission coefficient.

The statistical model calculation is performed in the direct cross section eliminated space, assuming the channels are diagonal. Such assumption implies that the direct and compound cross sections are independent, and the unitarity condition is fulfilled only for the total reaction cross section. Therefore the scattering cross sections are given by an incoherent sum of the direct and compound components. For example, the inelastic scattering

cross section is written as

$$
\sigma_ {a b} = \sigma_ {a b} ^ {\mathrm {D I}} + \frac {T _ {a} ^ {\prime} T _ {b} ^ {\prime}}{\sum_ {c} T _ {c} ^ {\prime}} W _ {a b}, \tag {10}
$$

where the direct cross section $\sigma _ { a b } ^ { \mathrm { { D I } } }$ is usually given by the coupled-channels calculation, and we denote the generalized transmission coefficients by $T ^ { \prime }$ . Often another approximation is made in addition to Eq. (7), which consists in replacing the decay channel transmission coefficients T (n) $T _ { l j } ^ { ( n ) }$ lj $T _ { l j } ^ { ( 0 ) }$ alculate, where shifted energy, T (n)lj ( $T _ { l j } ^ { ( n ) } ( E ) = T _ { l j } ^ { ( 0 ) } ( E - E _ { x } ^ { ( n ) } )$ $E _ { x } ^ { ( 0 ) }$ the excitation energy of $n$ -th level. This is not the case in our study. Making use of the time-reversal property of $S$ -matrix, the transmission coefficients for each $n$ -th state can be calculated automatically by Eq. (7). Note that the impact of this approximation is small when the optical potential depends weakly on the incident energy.

# C. Engelbrecht-Weidenm¨uller transformation

A rigorous treatment of off-diagonal elements in $\langle S \rangle$ is to perform the Engelbrecht-Weidenm¨uller (EW) transformation [13]. The particle penetration is expressed in terms of Satchler’s transmission matrix [28]

$$
P _ {a b} = \delta_ {a b} - \sum_ {c} \left\langle S _ {a c} \right\rangle \left\langle S _ {b c} ^ {*} \right\rangle , \tag {11}
$$

where the $S$ -matrix elements $\langle S _ { a b } \rangle$ are usually given by the coupled-channels calculation. Since $P$ is Hermitian, this can be diagonalized by a unitary transformation [13]

$$
\left(U P U ^ {\dagger}\right) _ {\alpha \beta} = \delta_ {\alpha \beta} p _ {\alpha}, \quad 0 \leq p _ {\alpha} \leq 1, \tag {12}
$$

and the same matrix $U$ diagonalizes the scattering matrix, i.e.,

$$
\left\langle \tilde {S} \right\rangle = U \langle S \rangle U ^ {T}. \tag {13}
$$

We use Greek subscripts for channel indices in the diagonalized space, and Latin subscripts for the normal space.

Since $\left. \tilde { S } \right.$ is diagonal, a new transmission coefficient in the diagonal channel space is defined as

$$
\left. T _ {\alpha} = 1 - \left| \left\langle \tilde {S} _ {\alpha \alpha} \right\rangle \right| ^ {2} = p _ {\alpha}, \right. \tag {14}
$$

and the statistical model calculation is performed in the diagonal channel space to evaluate the fluctuating part $\left. { \tilde { S } } _ { \alpha \beta } { \tilde { S } } _ { \gamma \delta } ^ { * } \right.$ . Finally a back-transformation from the channel space to the cross-section space reads

$$
\sigma_ {a b} = \sum_ {\alpha \beta \gamma \delta} U _ {\alpha a} ^ {*} U _ {\beta b} ^ {*} U _ {\gamma a} U _ {\delta b} \left\langle \tilde {S} _ {\alpha \beta} \tilde {S} _ {\gamma \delta} ^ {*} \right\rangle . \tag {15}
$$

Nishioka, Weidenm¨uller, and Yoshida (NWY) [16] obtained an equivalent formula for the fluctuation cross section, which expressed in terms of the non-diagonal $\langle S \rangle$ .

Although NWY does not require the $P$ -matrix diagonalization, a hefty computational burden is still involved. Instead of calculating NWY, we follow the procedure given above: the EW transformation is applied to nondiagonal $\langle S \rangle$ , and the GOE triple-integral of Eq. (2) is applied to the diagonalized channel space. This is the most accurate procedure to calculate the cross sections when $\langle S \rangle$ is not diagonal, and we consider this is the reference GOE cross section, as this is equivalent to NWY. Based on this, we further develop a technique, which is feasible in realistic cross section calculation cases, yet yields practically the same results to the reference GOE. We follow Moldauer’s prescription [15], in which the Engelbrecht-Weidenm¨uller (EW) transformation [13] is invoked, although an approximation — the decay amplitudes are normally distributed and their real and imaginary parts are uncorrelated — was made to cross sections in the diagonalized space.

The back-transformation can be re-written as [14],

$$
\begin{array}{l} \sigma_ {a b} = \sum_ {\alpha} | U _ {\alpha a} | ^ {2} | U _ {\alpha b} | ^ {2} \sigma_ {\alpha \alpha} \\ + \sum_ {\alpha \neq \beta} U _ {\alpha a} ^ {*} U _ {\beta b} ^ {*} \left(U _ {\alpha a} U _ {\beta b} + U _ {\beta a} U _ {\alpha b}\right) \sigma_ {\alpha \beta} \\ + \sum_ {\alpha \neq \beta} U _ {\alpha a} ^ {*} U _ {\alpha b} ^ {*} U _ {\beta a} U _ {\beta b} \left\langle \tilde {S} _ {\alpha \alpha} \tilde {S} _ {\beta \beta} ^ {*} \right\rangle , \tag {16} \\ \end{array}
$$

where $\sigma _ { \alpha \beta }$ is a width fluctuation corrected cross section in the diagonalized channel space,

$$
\sigma_ {\alpha \beta} = \frac {p _ {\alpha} p _ {\beta}}{\sum_ {\gamma} p _ {\gamma}} W _ {\alpha \beta}. \tag {17}
$$

Replacing the energy average (angle-bracket) by the ensemble average (overline), the GOE triple-integral formula gives a new term of $\left. { \tilde { S } } _ { \alpha \alpha } { \tilde { S } } _ { \beta \beta } ^ { * } \right.$ in Eq. (16) by setting $a = b = \alpha$ and $c = d = \beta$ . Moldauer [15] estimated this in terms of the channel degree-of-freedom $\nu _ { a }$ and the width fluctuation corrected cross section $\sigma _ { \alpha \beta }$ as

$$
\overline {{\tilde {S} _ {\alpha \alpha} \tilde {S} _ {\beta \beta} ^ {*}}} \simeq \left(\frac {2}{\nu_ {\alpha}} - 1\right) ^ {1 / 2} \left(\frac {2}{\nu_ {\beta}} - 1\right) ^ {1 / 2} \sigma_ {\alpha \beta}. \tag {18}
$$

This estimation was partially confirmed by a GOE Monte Carlo study [29], when $\tilde { S } _ { \alpha \alpha } \tilde { S } _ { \beta \beta } ^ { * }$ is real. We generalize this expression by expanding to the case of complex $\tilde { S } _ { \alpha \alpha } \tilde { S } _ { \beta \beta } ^ { * }$ The Jacobian of Eq. (4) for $a = b = \alpha$ and $c = d = \beta$ ,

$$
J \propto \bar {S} _ {\alpha \alpha} \bar {S} _ {\beta \beta} ^ {*} T _ {\alpha} T _ {\beta}, \tag {19}
$$

is real when $\mathrm { I m } ( \overline { { S } } _ { \alpha \alpha } \overline { { S } } _ { \beta \beta } ) = 0$ . This requires an extra phase factor as

$$
\overline {{\tilde {S} _ {\alpha \alpha} \tilde {S} _ {\beta \beta} ^ {*}}} \simeq e ^ {i (\phi_ {\alpha} - \phi_ {\beta})} \left(\frac {2}{\nu_ {\alpha}} - 1\right) ^ {1 / 2} \left(\frac {2}{\nu_ {\beta}} - 1\right) ^ {1 / 2} \sigma_ {\alpha \beta}, \tag {20}
$$

where $\phi _ { \alpha } = \tan ^ { - 1 } \bar { S } _ { \alpha \alpha }$

# D. Decay to uncoupled states

Actual cross section calculations involve many uncoupled or very weakly coupled states, such as the neutron emission to the continuum, the photon emission in the neutron radiative capture process, and nuclear fission. In the generalized transmission calculation scheme, inclusion of these channels is straightforward; the denominator of Eq. (10), $\sum _ { c } T _ { c } ^ { \prime }$ , includes the transmission coefficients for all uncoupled channels. The particle emission transmission coefficients may be given by the optical model, the photon channel is calculated with the Giant Dipole Resonance (GDR) model, etc.

In the case of EW transformation, the penetration matrix may have two blocks

$$
P = \left( \begin{array}{c c} P _ {1} & \\ & P _ {2} \end{array} \right), \tag {21}
$$

where $P _ { 1 }$ is the coupled channels $P$ matrix, and $P _ { 2 }$ is the diagonal part that accounts for decaying into the uncoupled states. The unitary transformation is performed to $P _ { 1 }$ only, and the summation in the denominator of $\sigma _ { \alpha \beta }$ in Eq. (17) runs over both the eigenvalues of $P _ { 1 }$ and the diagonal elements of $P _ { 2 }$ . Finally the uncoupled cross section is calculated by

$$
\sigma_ {a b} = \sum_ {\alpha} \left| U _ {\alpha a} \right| ^ {2} \sigma_ {\alpha \beta} \delta_ {\beta b}. \tag {22}
$$

# E. Monte Carlo technique for sampling $S$ -matrix

The aim of this paper is twofold; (a) understanding the limitation of generalized transmission coefficient in Eq. (7), in which no diagonalization procedure is required, and (b) when the diagonalization is essential, how accurate the approximation of Eq. (20) will be. To this end, we have to explore a large parameter space spanning over various $S$ -matrix elements and the number of channels $\Lambda$ . A natural approach is to employ the Monte Carlo technique, which facilitates model comparisons in a large multi-parametric space. We draw a diagonal element of $S$ -matrix from a uniform distribution inside the unit circle on the complex plane. The diagonal elements are generated by

$$
\langle S _ {a a} \rangle = e ^ {i \phi} \sqrt {1 - T _ {a}}, \quad 1 \leq a \leq \Lambda , \tag {23}
$$

where $0 \leq \phi < 2 \pi$ and $0 < \sqrt { 1 - T _ { a } } < 1$ are the sampled phase and transmission coefficient from the uniform distribution. For the off-diagonal elements, we impose another condition of $| \left. S _ { a b } \right. | ^ { 2 } < 0 . 5 | \left. S _ { a a } \right. | | \left. S _ { b b } \right. |$ . The sampled $S$ -matrix is converted into $P$ , and the matrix is diagonalized to obtain its eigenvalues. If negative eigenvalues emerge, we discard this $S$ , and re-sample. The constructed matrix has a dimension of $\Lambda \times \Lambda$ .

With the generated $S$ -matrix, dimensionless cross sections — total cross section of $\sigma ^ { \mathrm { T } }$ , shape elastic scattering

σSE $\sigma ^ { \mathrm { S E } }$ , direct inelastic scattering $\sigma _ { a b } ^ { \mathrm { { D I } } }$ , compound formation σCN — $\sigma ^ { \mathrm { C N } }$ are calculated in a common way,

$$
\sigma^ {\mathrm {T}} = 2 \left(1 - \Re \langle S _ {a a} \rangle\right), \tag {24}
$$

$$
\sigma^ {\mathrm {S E}} = | 1 - \langle S _ {a a} \rangle | ^ {2}, \tag {25}
$$

$$
\sigma_ {a b} ^ {\mathrm {D I}} = \left| \langle S _ {a b} \rangle \right| ^ {2}, \tag {26}
$$

$$
\sigma^ {\mathrm {C N}} = 1 - \left| \left\langle S _ {a a} \right\rangle \right| ^ {2} = T _ {a}, \tag {27}
$$

and the reaction cross section rea $\begin{array} { r } { \sigma ^ { \mathrm { R } } = \sigma ^ { \mathrm { C N } } + \sum _ { b } \sigma _ { a b } ^ { \mathrm { D I } } } \end{array}$ $a$ ing channel. Since $\mid \left. S \right. \mid ^ { 2 } \leq 1$ , clearly $0 \le \sigma _ { T } \le 4$ . We generate several hundred of $S$ -matrices for each $\Lambda = 2 \sim$ 7 case.

# III. SIMULATION USING RANDOM $S$ -MATRIX

# A. Simulation for Engelbrecht-Weidenm¨uller transformation

Here we compare two methods to calculate the compound cross sections. The first method is to employ the generalized transmission coefficients in Eq. (7). Using the randomly generated $S$ -matrix this is written simply as

$$
T _ {a} ^ {\prime} = 1 - \sum_ {c} | \langle S _ {a c} \rangle | ^ {2}. \tag {28}
$$

The compound reaction cross sections are defined in the direct cross section eliminated space,

$$
\sigma_ {a b} ^ {\prime} = \frac {T _ {a} ^ {\prime} T _ {b} ^ {\prime}}{\sum_ {c} T _ {c} ^ {\prime}} W _ {a b} ^ {\prime}, \tag {29}
$$

where we use Eq. (2) to calculate $W _ { a b } ^ { \prime }$ . The second method is to perform the EW transformation. The cross section is given by Eq. (15), with $\tilde { S } _ { \alpha \beta } \tilde { S } _ { \gamma \delta } ^ { * }$ by Eq. (2). This procedure yields the correct results, and is thus our reference GOE cross section.

The calculated cross sections with the generalized transmission coefficients are shown in Fig. 1 by the ratio to the reference GOE cross sections, as a function of the strength of direct channels $\textstyle \sum _ { b } \sigma _ { a b } ^ { \mathrm { D I } } / \sigma ^ { \mathrm { R } }$ for $\Lambda = 2 \sim 7$ . In the case of $\Lambda > 2$ , the inelastic scattering are summed

$$
\sigma^ {\text {I N L}} = \sum_ {b (a \neq b)} \sigma_ {a b}. \tag {30}
$$

Because we generated the $S$ -matrix from the uniform distribution, such comparisons tend to produce extreme cases where the coupling of direct channels is too strong. Nevertheless a general tendency can be clearly seen; when the generalized transmission coefficient is used, the elastic channel is overestimated and the inelastic channel is underestimated. The impact of EW transformation is large, when there are a few channels open (e.g. Fig. 1 (a)), and the direct cross sections are large. Under such circumstances the approximated method to calculate the

cross section by employing the generalized transmission coefficients leads to incorrect answers.

The underestimation in the inelastic channels decreases as the number of channels $\Lambda$ increases. That said, we expect that the approximation with the generalized transmission coefficients works well at the strong absorption limit, where the elastic enhancement factor $W _ { a }$ is 2 [9]. In our Monte Carlo technique, $W _ { a }$ is approximately given by

$$
W _ {a} \simeq \sigma_ {a a} / \frac {T _ {a} ^ {\prime}}{\sum_ {c} T _ {c} ^ {\prime}}, \tag {31}
$$

where $\sigma _ { a a }$ is the compound elastic scattering cross section. Figure 2 shows the inelastic channel underestimation as a function of the elastic enhancement. The underestimation will be very small at the strong absorption limit ( $W _ { a } = 2$ ), where the width fluctuation correction to the inelastic channels fades out due to a large number of open channels. In other words, the EW transformation is essential when the elastic enhancement largely changes the inelastic channels.

# B. Uncoupled states

To investigate the uncoupled channel in the EW transformation, we construct $S$ with $\Lambda = 3$ as in

$$
S = \left( \begin{array}{c c c} S _ {a a} & S _ {b a} & \\ S _ {a b} & S _ {b b} & \\ & & S _ {c c} \end{array} \right), \tag {32}
$$

where the channel $c$ is uncoupled to the channels $a$ and $b$ . The calculated cross sections with the generalized transmission coefficients are shown by the ratio to the EW transformation in Fig. 3. As opposed to the coupled inelastic scattering channel, the cross section to the uncoupled channel increases very slightly, but is almost not influenced by the channel coupling. This suggests, in the case of neutron-induced reactions on deformed nuclei, that the inelastic scattering cross sections will be enhanced mainly at the expense of the elastic channel, while the neutron capture and fission cross sections will practically not change.

# C. Simulation for Moldauer’s estimation

Because the term of $\tilde { S } _ { \alpha \alpha } \tilde { S } _ { \beta \beta } ^ { * }$ in Eq. (16) is a quantity in the diagonalized channel space, we can evaluate this with the GOE triple-integral of Eq. (2) whenever $\langle S \rangle$ is diagonal. We replace $\bar { S } _ { \alpha \alpha }$ by $\langle S _ { a a } \rangle$ , and apply the Monte Carlo technique to calculate $S _ { a a } S _ { b b } ^ { * }$ by sampling the diagonal $S$ -matrix, as well as the number of channels $\Lambda$ that is randomly varied from 2 to 200. We generated 500 such random $S$ -matrices, and the calculated $| \overline { { S _ { a a } S _ { b b } ^ { * } } } |$ is shown by the symbols in Fig. 4. When there are many open channels, $\textstyle \sum _ { c } T _ { c } \gg 1$ , this term will be negligible.

![](images/53795ede69d0008181f861049a4814eaf9d262f245fd494ceda2ba833e777059.jpg)

![](images/0aeff140cadfdad0e85eda7ea90bee29670eb8fe3e138a217a7e33224a1f2010.jpg)

![](images/0255dbbd7be34f0902c1cbd273d6034e164149e6aa453f6cbb0c8be2af199ea0.jpg)  
FIG. 1. Ratio of calculated cross sections using randomly generated $S$ -matrix, as a function of the direct reaction strength. The ratio is that of generalized transmission coefficient calculations to the EW transformation case. The top panel (a) is for a number of channels of $\Lambda = 2$ and 3, the middle panel (b) is for $\Lambda = 4$ and 5, and the bottom panel (c) is for $\Lambda = 6$ and 7.

![](images/b54d4791e514e4e59bc1297fc90352486d6540f5804e7c8f2fa2a6a89de1d5b1.jpg)  
FIG. 2. Ratio of calculated inelastic scattering cross section with the generalized transmission coefficient calculations to the EW transformation case, as a function of the elastic enhancement factor $W _ { a }$ .

![](images/2fadc71061f7835b39e6f9bb375bfdb3798222571695217f07eb76676f173ea7.jpg)  
FIG. 3. Ratio of the cross sections calculated with the generalized transmission coefficient calculations to the cross sections calculated with EW transformation case, for $\Lambda = 3$ and the third channel is uncoupled.

Applying two different estimates for $\nu _ { a }$ obtained by Moldauer [26] and at LANL [20], Eq. (20) can be evaluated very easily. Figure 5 shows the ratio of Eq. (20) to the GOE results, using two functional forms for $\nu _ { a }$ . Since $\overline { { S _ { a a } S _ { b b } ^ { * } } }$ is complex due to the factor of $S _ { a a } S _ { b b } ^ { * }$ in Eq. (2), the ratio is taken for the absolute value (the module). It can be seen clearly that the updated systematics of $\nu _ { a }$ at LANL produces an excellent agreement with GOE, except for in the very small $\Sigma _ { c } T _ { c }$ region, where all statistical models tend to fail [20].

![](images/5827cb534ba5052e0ee2e8e93c8fe8240a622aae31b97b48be97b643c8aac409.jpg)  
FIG. 4. Calculated $| S _ { a a } S _ { b b } ^ { * } |$ with the GOE triple-integral formula for randomly generated $S$ -matrix and number of channels. The results are shown as a function of $\sum _ { c } T _ { c }$ .

# D. Simulation for cross section

Our next step is to confirm whether Eq. (16) with the estimation for $\overline { { { \tilde { S } } _ { \alpha \alpha } { \tilde { S } } _ { \beta \beta } ^ { * } } }$ in Eq. (20) is a good approximawe calculate the cross sections using the randomly generated non-diagonal $S$ -matrix again, and compare with the reference GOE cross sections.

The calculated cross sections for the compound elastic and inelastic channels are shown by the deviation from GOE in Fig. 6, as a function of total cross section $\sigma ^ { \mathrm { T } }$ . The standard deviation is 0.83% for the $\Lambda = 2$ case, and 0.29% for $\Lambda = 5$ . From this comparison, we conclude that Moldauer’s model of Eq. (18) with the additional phase factor provides a very good approximation to the GOE triple-integral formula when the off-diagonal elements in the $S$ -matrix exist. In reality, because the actual direct channel coupling is much weaker than our randomly generated $S$ -matrix, and the number of channels tends to be larger, Eqs (16) and (20) should provide an excellent alternative procedure to calculate compound reaction cross sections, leading to almost identical cross sections as the rigorous GOE formula [16].

# IV. COUPLED-CHANNELS AND HAUSER-FESHBACH MODEL IN A REALISTIC CASE

We now calculated compound cross sections for neutron induced reactions on 238U in the fast energy range with the coupled-channels Hauser-Feshbach code CoH $^ 3$ , and implement the EW transformation as well as all the necessary formulae given previously. Note that the intention here is not to provide the best evaluated cross

![](images/70e91731f5bf4e4219dcfa3a06ed6e744d3bbe02cebdae58f698a116b74d32e5.jpg)

![](images/caf19026e490ab9c8029c65d558092079e996da6752ed0d7e7cc65c36b258a6b.jpg)  
FIG. 5. Comparison of Moldauer’s estimate for $| \overline { { S _ { a a } S _ { b b } ^ { * } } } |$ given by Eq. (18) for various $T _ { a }$ values and channels, shown by the ratios to the GOE calculation. Two different estimates for the channel degree-of-freedom $\nu$ , Refs. [26] and [20], are used; the top panel (a) is for smaller $\sum _ { c } T _ { c }$ case, and the bottom panel (b) is for larger $\sum _ { c } T _ { c }$ case.

section, but to study how large the impact of the EW transformation on actual cross section calculations will be. Albeit it is redundant, we summarize here the procedure of cross section calculation including the EW transformation as a practical recipe for applications.

• For a given total spin and parity $J \Pi$ , solve the coupled-channels equation. The coupled-channels $S$ -matrix is converted into $P$ -matrix by Eq. (11), then diagonalized by $U P U ^ { \dagger }$ to obtain the eigenvalues $p _ { \alpha }$ and the eigenvector $U$ . We also need the diagonalized $S$ -matrix, $\tilde { S } = U S U ^ { T }$ .   
• Calculate the transmission sum for all open channels as

$$
T = \sum_ {\alpha} p _ {\alpha} + \sum_ {k} T _ {k} (\text {u n c o u p l e d}). \tag {33}
$$

![](images/9f614fef3c05cc6a04954ce63ec505e97de459828a6571a488dca86c7a08d9b0.jpg)

![](images/b342514d1ce86a66c2828bef19964d92f54071190025c16d089cab467096e861.jpg)  
FIG. 6. Compound elastic and inelastic cross sections calculated with randomly sampled $S$ -matrix as well as using Moldauer’s estimate for $| \tilde { S } _ { \alpha \alpha } \tilde { S } _ { \beta \beta } ^ { * } |$ , as a function of the dimensionless total cross section. The results are shown by the deviation from the GOE results. The top panels are for the two channels case, and the bottom panels are for the five channels.

• Calculate the channel cross section matrix in the transformed space

$$
\sigma_ {\alpha \beta} = \frac {p _ {\alpha} p _ {\beta}}{T} W _ {\alpha \beta}, \tag {34}
$$

where the width fluctuation factor $W _ { \alpha \beta }$ is given by Eq. (5).

• For a set of coupled levels, given a fixed set of incoming (a) and outgoing (b) channels, sum over $a$ and $b$ when $a \in$ (ground state), and $b \in$ (ground or excited state). Summation $\alpha$ and $\beta$ runs over all the diagonal space, and calculate the cross section as in Eq .(16) with Eqs. (17) and (20).   
• For uncoupled levels, run $a$ over the channels that belong to the ground state. The cross section is given by Eq. (22).

We employed the dispersive coupled-channels optical potential by Soukhovitskii et al. [30], with the deformation parameters of $\beta _ { 2 } ~ = ~ 0 . 2 1 4$ , $\beta _ { 4 } ~ = ~ 0 . 0 0 9 3 1$ , and $\beta _ { 6 } ~ = ~ - 0 . 0 1 4 8$ taken from the Finite Range Droplet Model [31]. We coupled five levels in the ground state rotational band, $0 ^ { + }$ , $2 ^ { + }$ , $4 ^ { + }$ , $6 ^ { + }$ , and $8 ^ { + }$ . Although direct inelastic scattering to the vibrational bands can be

observed, we consider them as uncoupled levels to simplify the calculations, otherwise a different optical model would be needed.

The photon strength function is calculated with the Giant Dipole Resonance (GDR) model with the parameters of Ullmann et al. [32]. The level density of $^ { 2 3 9 }$ U is calculated with Gilbert and Cameron’s composite formula [33, 34], and the level density parameter is slightly adjusted to reproduce the average resonance spacing of $D _ { 0 } = 2 0 . 2 6 \pm 0 . 7 2 ~ \mathrm { e V }$ [35]. The fission barrier parameters are taken from Iwamoto’s study [6], and adjusted to roughly reproduce the evaluated fission cross section at 1 MeV in ENDF/B-VII [36]. Note that the fission channel is not important, since we are mainly interested in the cross sections in the sub-threshold fission region.

Figure 7 shows the comparison of calculated inelastic scattering cross sections for the $2 ^ { + }$ , $4 ^ { + }$ , $6 ^ { + }$ , and $8 ^ { + }$ states. The dashed curves are calculated with the generalized transmission coefficients as in Eq. (10). We also depict the evaluated cross sections in JENDL-4 [6, 37] for comparison, since these cross sections were calculated with a similar optical model with the coupled-channels Hauser-Feshbach code, CCONE [6], in which the generalized transmission coefficients are adopted. The solid curves are the result of EW transformation. The transformation always increases the inelastic scattering cross section to the level that has the direct component, which we already observed in Fig. 1 in the randomly generated $S$ -matrix model. Because the compound formation cross section $\sigma ^ { \mathrm { C N } }$ remains the same, the increase in the inelastic channels reduces the enhancement in the compound elastic channel. However, the reduction in the elastic scattering cross section is not so visible, since the shape elastic scattering $\sigma _ { \mathrm { S E } }$ dominates the elastic channel in this energy range.

The calculated capture, total inelastic, and fission cross sections are shown in Fig. 8, as a ratio of the EW transformation case to the generalized transmission case. The total inelastic scattering includes both the coupled and uncoupled levels. As we already saw in Fig. 3, the generalized transmission calculation gives slightly larger cross sections for the uncoupled capture and fission channels. However, the change in these cross sections are less than 2%, while uncertainties in the calculated capture and fission cross sections are much larger in general.

The ratios approach to unity as the neutron incident energy increases, and the impact of the EW transformation disappears above a few MeV. Above that energy, the compound elastic scattering cross section can be basically ignored, because there are many open channels. Under such circumstances the Hauser-Feshbach theory is justified, and the cross sections can be calculated without the EW transformation.

![](images/ad9e963041999f78fc6306f83bb2b4131560f5157e33015fd1ce26f770300b2a.jpg)

![](images/b3c576cfe079a35e09f5228cb03d5fd05a53fbfa7d20f230871cf653b9ddffb4.jpg)

![](images/830e4ef72babdf0e527824c1d9d823e17599b48a79b312e04b4e85a15d75d217.jpg)

![](images/03ec65fdb596a7f372e5820b93fdad4daca944be22ff2b1a832517f0ba124bb7.jpg)  
FIG. 7. Calculated $^ { 2 3 8 }$ U(n,n’) reaction cross sections with the EW transformation (solid curves) compared with the modified transmission calculation (dashed curves), as well as with the evaluated cross sections in JENDL-4 (dot-dashed curves).

# V. CONCLUSION

An exact formula for the width fluctuation corrected Hauser-Feshbach cross section, in which directly coupled channels are involved, is used to perform the statistical model calculation based on Gaussian Orthogonal Ensemble (GOE) in the diagonalized space — the so-called Engelbrecht-Weidenm¨uller (EW) transformation. Nishioka, Weidenm¨uller, and Yoshida [16] obtained an equivalent expression of the fluctuation cross section without the diagonalization procedure. Nevertheless, the latter has not been employed in practical cross section calculations, due to the complexity both in the formula itself and technical difficulties in applying actual cases. To overcome this problem, we have developed an approximated method, which produces almost identical cross sections as the theory of Nishioka et al., and is feasible to compute cross sections in realistic cases without any of the difficulties the GOE inherently possesses. The method

combines Moldauer’s approximation [15] with a simple relation between the channel degree-of-freedom and the optical model transmission coefficient, recently obtained by a GOE numerical study at LANL [20].

We have confirmed the Moldauer’s approximation for the first time by our Monte Carlo approach, and found that an extra phase factor should be included when $\mathrm { I m } ( S _ { \alpha \alpha } S _ { \beta \beta } ) \neq 0$ . The method was applied to the description of neutron induced reactions on $^ { 2 3 8 }$ U target in the fast energy range, where the elastic and inelastic scattering, the radiative neutron capture and the fission channels are relevant. We demonstrated that the EW transformation indeed increases the calculated inelastic scattering cross sections, while modest changes were seen in the uncoupled channels, including the fission and capture cross sections. We concluded that conventional methods calculating the Hauser-Feshbach theory by adopting the generalized (direct cross section eliminated) transmission coefficients lead to underestimation

![](images/db4e10588715c041a0308f01f763a1b699b880ef0927b309b2182be8747d91b7.jpg)  
FIG. 8. Ratios of calculated capture, total inelastic and fission cross sections without EW transformation to the EW cases.

of the inelastic scattering cross sections, when the direct channels are strongly coupled. This underestimation decreases as the number of open channels increases. We believe this technique should be adopted by existing Hauser-Feshbach codes, leading to more accurate predictions of the scattering cross sections on collective nuclei.

# ACKNOWLEDGMENT

One of the authors (TK) carried out this work under the auspices of the National Nuclear Security Administration of the U.S. Department of Energy at Los Alamos National Laboratory under Contract No. DE-AC52-06NA25396.

[1] W. Hauser, H. Feshbach, Phys. Rev. 87, 366 (1952).   
[2] T. Tamura, Rev. Mod. Phys. 37, 679 (1965).   
[3] T. Kawano, P. Talou, J. E. Lynn, M. B. Chadwick, D. G. Madland, Phys. Rev. C 80, 024611 (2009).   
[4] M. W. Herman, R. Capote, B. V. Carlson, P. Oblozinsk´y, M. Sin, A. Trkov, H. Wienke, V. Zerkin, Nucl. Data Sheets 108, 2655 (2007).   
[5] A. J. Koning, S. Hilaire, M. C. Duijvestijn, Proc. Int. Conf. on Nuclear Data for Science and Technology, 22 – 27 Apr., 2007, Nice, France, Ed. O. Bersillon, F. Gunsing, E. Bauge, R. Jacqmin, and S. Leray, EDP Sciences, pp.211–214 (2008).   
[6] O. Iwamoto, J. Nucl. Sci. Technol. 44, 687 (2007).   
[7] T. Kawano, computer code CoH3 [unpublished].   
[8] T. Kawano, P. Talou, M. B. Chadwick, T. Watanabe J. Nucl. Sci. Technol. 47, 462 (2010).   
[9] T. Kawano, P. Talou, H. A. Weidenm¨uller Phys. Rev. C 92, 044617 (2015).   
[10] M. Kawai, A. K. Kerman, K. W. McVoy, Ann. Phys. 75, 156 (1973).   
[11] G. Arbanas, C. Bertulani, D.J. Dean, A.K. Kerman, Proc. of the 2007 Int. Workshop on Compound-Nuclear Reactions and Related Topics (CNR* 2007), Tenaya Lodge at Yosemite National Park, Fish Camp, California, USA 22-26 October 2007, AIP Conference Proceedings 1005, pp.160–163 Eds. J. Escher, F.S. Dietrich, T. Kawano, I. Thompson (2008).   
[12] T. Kawano, L. Bonneau, A. Kerman, “Effects of direct reaction coupling in compound reactions,” Proc. Int. Conf. on Nuclear Data for Science and Technology, 22 – 27 Apr., 2007, Nice, France, Ed. O. Bersillon, F. Gunsing, E. Bauge, R. Jacqmin, and S. Leray, EDP Sciences, pp.147– 150 (2008).   
[13] C. A. Engelbrecht, H. A. Weidenm¨uller, Phys. Rev. C 8, 859 (1973).

[14] H. M. Hofmann, J. Richert, J. W. Tepel, H. A. Weidenm¨uller, Ann. Phys. 90, 403 (1975).   
[15] P. A. Moldauer, Phys. Rev. C 12, 744 (1975).   
[16] H. Nishioka, H.A. Weidenm¨uller, S. Yoshida, Ann. Phys. 193, 195 (1989).   
[17] J. J. M. Verbaarschot, H. A. Weidenm¨uller, M. R. Zirnbauer, Phys. Rep. 129, 367 (1985).   
[18] R. Capote, A. Trkov, M. Sin, M. Herman, A. Daskalakis, Y. Danon, Nucl. Data Sheets 118, 26 (2014).   
[19] J. Raynal, computer code ECIS [unpublished].   
[20] T. Kawano, P. Talou, Nuclear Data Sheets 118, 183 (2014).   
[21] J. J. M. Verbaarschot, Ann. Phys. 168, 368 (1986).   
[22] P. A. Moldauer, Phys. Rev. C 11, 426 (1975).   
[23] P. A. Moldauer, Phys. Rev. C 14, 764 (1976).   
[24] P. A. Moldauer, “Statistical Theory of Neutron Nuclear Reactions,” ANL/NDM-40, Argonne National Laboratory (1978).   
[25] S. Hilaire, Ch. Lagrange, A. J. Koning, Ann. Phys. 306, 209 (2003).   
[26] P. A. Moldauer, Nucl. Phys. A, 344, 185 (1980).   
[27] M. Ernebjerg, M. Herman, Proc. Int. Conf. on Nuclear Data for Science and Technology, 26 Sept. – 1 Oct., 2004, Santa Fe, USA, Ed. R.C. Haight, M.B. Chadwick, T. Kawano, and P. Talou, American Institute of Physics, AIP Conference Proceedings 769, p.1233 (2005).   
[28] G. R. Satchler, Phys. Lett. 7, 55 (1963).   
[29] T. Kawano, Eur. Phys. J. A 51,164 (2015).   
[30] E. Sh. Soukhovitskii, R. Capote, J. M. Quesada, S. Chiba, Phys. Rev. C 72, 024604 (2005).   
[31] P. M¨oller, J. R. Nix, W. D. Myers, W. J. Swiatecki, At. Data and Nucl. Data Tables 59, 185 (1995).   
[32] J. L. Ullmann, T. Kawano, T. A. Bredeweg, A. Couture, R. C. Haight, M. Jandel, J. M. O’Donnell, R. S. Rundberg, D. J. Vieira, J. B. Wilhelmy, J. A. Becker,

A. Chyzh, C. Y. Wu, B. Baramsai, G. E. Mitchell, M. Krtiˇcka, Phys. Rev. C 89, 034603 (2014).   
[33] A. Gilbert, A. G. W. Cameron, Can. J. Phys., 43, 1446 (1965).   
[34] T. Kawano, S. Chiba, H. Koura, J. Nucl. Sci. Technol., 43, 1 (2006); T. Kawano, “updated parameters based on RIPL-3,” (unpublished, 2009).   
[35] S. F. Mughabghab, “Atlas of Neutron Resonances, Resonance Parameters and Thermal Cross Sections, $\mathrm { Z = 1 - }$ 100,” Elsevier (2006).   
[36] M. B. Chadwick, M. Herman, P. Obloˇzinsk´y, M.E. Dunn, Y. Danon, A.C. Kahler, D.L. Smith, B. Pritychenko, G. Arbanas, R. Arcilla, R. Brewer, D.A. Brown, R. Capote, A.D. Carlson, Y.S. Cho, H. Derrien, K. Guber, G.M.

Hale, S. Hoblit, S. Holloway, T.D. Johnson, T. Kawano, B.C. Kiedrowski, H. Kim, S. Kunieda, N.M. Larson, L. Leal, J.P. Lestone, R.C. Little, E.A. McCutchan, R.E. MacFarlane, M. MacInnes, C.M. Mattoon, R.D. McKnight, S.F. Mughabghab, G.P.A. Nobre, G. Palmiotti, A. Palumbo, M.T. Pigni, V.G. Pronyaev, R.O. Sayer, A.A. Sonzogni, N.C. Summers, P. Talou, I.J. Thompson, A. Trkov, R.L. Vogt, S.C. van der Marck, A. Wallner, M.C. White, D. Wiarda, P.G. Young Nuclear Data Sheets 112, 2887 (2011).   
[37] K. Shibata, O. Iwamoto, T. Nakagawa, N. Iwamoto, A. Ichihara, S. Kunieda, S. Chiba, K. Furutaka, N. Otuka, T. Ohsawa, T. Murata, H. Matsunobu, A. Zukeran, S. Kamada, J. Katakura, J. Nucl. Sci. Technol. 48, 1 (2011).