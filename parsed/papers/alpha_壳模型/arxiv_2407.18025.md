# Alpha-decay from $^ { 4 4 }$ Ti: Microscopic alpha half-live calculation using normalized spectroscopic factor

A. C. Dassie1, 2 and R. M. Id Betan ${ } ^ { 1 , 2 }$

$^ { 1 }$ Instituto de F´ısica Rosario (CONICET-UNR), Ocampo y Esmeralda, Rosario 2000. Argentina. $^ 2$ Facultad de Ciencias Exactas, Ingenier´ıa y Agrimensura (UNR), Av. Pellegrini 250, Rosario 2000. Argentina. (ΩDated: July 26, 2024)

Background: The microscopic description of alpha decay from the nucleons’ degree of freedom involves a twostep process. The first consists of the clusterization of neutron and proton pairs; the second involves the tunneling process.

Purpose: A robust protocol for calculating the normalized spectroscopic factor (amount of clustering), as defined by Fliessbach, and its error is established and used for calculating the alpha-width for the $0 ^ { + }$ states of the nucleus 44Ti. $^ { 4 4 } \mathrm { T i }$

Method: The Gamow Shell Model is used to calculate the structure part of the alpha-decay (spectroscopic factor), while the Gamow wave function determines the reaction part (single particle width).

Results: The conventional and normalized spectroscopic factors are calculated for the ground and excited $0 ^ { + }$ states of $^ { 4 4 } \mathrm { T i }$ and the alpha-width and half-life of the excited states. A near alpha-threshold state has an alpha half-life of 5 µsec.

Conclusions: The normalization does not appreciably modify the ground-state clusterization, while the excited states do. The non-resonant continuum significantly increases the clustering of some of the excited states, particularly the $T ' = 2$ state. The normalized formation amplitude looks like a single-particle wave function.

PACS numbers: 21.10.-k, 21.30.Fe, 21.60.Cs, 27.40.+z

# I. INTRODUCTION

Alpha-decay, a phenomenon as enduring as quantum mechanics, remains a captivating research area with ongoing theoretical advancements [1, 2]. Traditionally, its decay width has been calculated via the Thomas-Lane equation [3, 4] involving penetrability and reduced width or through an expression linking spectroscopic factors and single-particle reduced widths [5, 6]. Both formulations stem from time-independent reaction theory. An alternative time-dependent framework for alpha-decay was developed by Mang [7], exhibiting formal equivalence to the time-independent approaches [8]. The numerical applications showed to be far smaller compared with experimental results [9], even using large configuration model spaces [10–12]. A major breakthrough was made by Fliessbach reinterpreting the spectroscopic factor. He argued that, due to the antisymmetrization, the cluster-channel wave function was not normalized [13]. Shell model calculations incorporating Fliessbach prescription got significantly closer to the experimental alpha-width of the archetypal nucleus $\mathrm { 2 1 2 } _ { \mathrm { P o } }$ but still failed to reproduce it [14–17]. On the other hand, the hybrid cluster plus shell model approach, complemented with Fliessbach normalization, does reproduce the $\mathrm { ^ { 2 1 2 } P o }$ alpha-width [18, 19].

It seems that the Shell Model alone cannot gain enough correlations to achieve the necessary clusterization. The elements involved in the alpha-width calculation are the single-particle model space, the four-body basis, the two-body interactions, and the Fliessbach normalization. Reference [17] is the first attempt to cover these ele-

ments by extending the single-particle proton and neutron bases to the resonant continuum and considering the normalization of the channel decay. Although the asymptotic of the alpha formation amplitude was properly described, the alpha width was still smaller than expected [17]. Reference [20] resumes this project by completing the single-particle bases with the non-resonant continuum and the two-body interaction in all nucleon-nucleon channels. The present work covers the calculation of the Fliessbach normalization by providing a robust protocol for calculating the normalized spectroscopic factor and its numerical error. The nucleus $^ { 4 4 } \mathrm { T i }$ is used as a benchmark since it has many $0 ^ { + }$ states; besides, it is of interest in nuclear astrophysics [21], for example, for understanding its formation through the $\alpha$ -Ca reaction in core-collapse supernova environments [22].

The paper is organized as follows. Section II gives the absolute width in terms of the normalized spectroscopic factor. Section III briefly defines the parameters for the system and introduces the protocol for calculating the normalized spectroscopic factor and its error. Sec. IV calculates the normalized spectroscopic factor for the $0 ^ { + }$ states of $^ { 4 4 }$ Ti of Ref. [20]. The microscopic alpha-decay width of the excited states are being calculated in Sec. V. The effects of truncating the many-body Hilbert space are studied in Sec. VI. Finally, Sec. VII summarizes the results.

# II. FORMALISM

The appropriate microscopic calculation of the alphadecay width $\Gamma _ { L }$ in terms of the single particle width $\Gamma _ { L } ^ { \mathrm { s p } }$

is given by the Arima expression [5] with the normalized spectroscopic factor as defined by Fliessbach [23]

$$
\Gamma_ {L} = \mathcal {S} _ {L} \Gamma_ {L} ^ {\mathrm {s p}}, \tag {1}
$$

with

$$
\mathcal {S} _ {L} = \int G _ {L} ^ {2} (R) R ^ {2} d R. \tag {2}
$$

The modified formation amplitude $G _ { L }$ is expressed in terms of the conventional one $g _ { L }$ and the norm kernel $\mathcal { N } _ { L }$ as follows [23–26],

$$
G _ {L} (R) = \int \mathcal {N} _ {L} ^ {- 1 / 2} (R, R ^ {\prime}) g _ {L} (R ^ {\prime}) R ^ {\prime 2} d R ^ {\prime},
$$

with [10]

$$
\begin{array}{l} g _ {L} (R) = \int d \Omega_ {R} \int d \xi_ {\alpha} \int d \xi_ {D} \\ \Psi_ {J M} \mathcal {A} \big [ \phi_ {\alpha} (\xi_ {\alpha}) \Psi_ {j} ^ {D} (\xi_ {D}) Y _ {L} (\hat {R}) \big ] _ {J M} ^ {*}, \\ \end{array}
$$

and

$$
\begin{array}{l} \mathcal {N} _ {L} (R, R ^ {\prime}) = \\ \left\langle \mathcal {A} \frac {\delta \left(R _ {\alpha} - R\right)}{R ^ {2}} \phi_ {\alpha} \left[ Y _ {L} \Psi_ {j} ^ {D} \right] _ {J M} \mid \mathcal {A} \frac {\delta \left(R _ {\alpha} - R ^ {\prime}\right)}{R ^ {\prime 2}} \phi_ {\alpha} \left[ Y _ {L} \Psi_ {j} ^ {D} \right] _ {J M} \right\rangle . \\ \end{array}
$$

The parent wave function (w.f.) $\Psi _ { J M }$ is a double-closed shell w.f. $\Psi _ { j m } ^ { D }$ plus two protons and two neutrons, as defined in Ref. [20]. The alpha particle w.f. $\phi _ { \alpha }$ is defined as in Ref. [17], and $Y _ { L M _ { L } }$ represents the angular part of the relative alpha-daughter w.f.

The norm kernel is expanded using an equidistant set of orthonormalized shifted Gaussian functions denoted as $\tilde { F } _ { L } ( R , R _ { k } )$ , where $R _ { k } \ = \ k \Delta R$ [27]. This expansion extends to the radial coordinate $R _ { \operatorname* { m a x } } = M \Delta R$ .

Expressing the modified formation amplitude in terms of the norm kernel eigenvalues $n _ { \nu }$ and eigenfunctions $u _ { \nu } ^ { L } ( R )$ yields [17]

$$
G _ {L} (R) = \sum_ {\nu = 1} ^ {\nu_ {\mathrm {m a x}}} n _ {\nu} ^ {- 1 / 2} u _ {\nu} ^ {L} (R) g _ {\nu} ^ {L}, \tag {3}
$$

with

$$
g _ {\nu} ^ {L} = \int u _ {\nu} ^ {L} (R) g _ {L} (R) R ^ {2} d R, \tag {4}
$$

and the corresponding spectroscopic factor is given by

$$
\mathcal {S} _ {L} = \sum_ {\nu = 1} ^ {\nu_ {\max}} s _ {\nu} ^ {L}, \tag {5}
$$

with $\nu _ { \mathrm { m a x } }$ to be determined, and

$$
s _ {\nu} ^ {L} = \int R ^ {2} \frac {\left[ u _ {\nu} ^ {L} (R) g _ {\nu} ^ {L} \right] ^ {2}}{n _ {\nu}} d R. \tag {6}
$$

The formation amplitude is expressed in terms of single-particle configurations as

$$
g _ {L} (R) = \sqrt {8} \sum_ {J _ {n} J _ {p}} \sum_ {a \leq b} \sum_ {c \leq d} b _ {j _ {a} j _ {b} j _ {c} j _ {d}} ^ {J _ {n} J _ {p}} (- 1) ^ {\theta} \frac {\hat {\mathcal {J}} _ {a} \hat {\mathcal {J}} _ {b} \hat {\mathcal {J}} _ {c} \hat {\mathcal {J}} _ {d}}{2} I _ {j _ {a} j _ {b} j _ {c} j _ {d}} ^ {J _ {n} J _ {p}} (R) \tag {7}
$$

where $\theta = J _ { n } + J _ { p } - j _ { a } - j _ { c } - l _ { b } - l _ { d } + 1$ . This equation relates the formation amplitude to the amplitudes of different configurations within the parent state. The pair indexes $a \leq b$ labels the two-neutron basis, similarly, $c \leq d$ for protons. The coefficients bJn Jpj j j $b _ { j _ { a } j _ { b } j _ { c } j _ { d } } ^ { J _ { n } J _ { p } } = Z _ { n p } ^ { J } X _ { a b } ^ { J _ { n } } X _ { c d } ^ { J _ { p } }$ = ZJ XJn XJp enclosed the amplitudes of the correlated two-neutron and two-proton states $X _ { a b } ^ { J _ { n } }$ and X Jp , $X _ { c d } ^ { J _ { p } }$ cd as well as the parent four-body wave-function amplitude [20]

$$
\Psi_ {J M} = \sum_ {J _ {n} J _ {p}} Z _ {n p} ^ {J} \left[ \Psi_ {J _ {n}} \Psi_ {J _ {p}} \right] _ {J M}. \tag {8}
$$

The following expression defines the radial matrix elements $I ( R )$ ,

$$
\begin{array}{l} I _ {j _ {a} j _ {b} j _ {c} j _ {d}} ^ {J _ {n} J _ {p}} (R) = W \left(l _ {a} j _ {a} l _ {b} j _ {b}; \frac {1}{2} J _ {n}\right) W \left(l _ {c} j _ {c} l _ {d} j _ {d}; \frac {1}{2} J _ {p}\right) \\ \int d \Omega_ {R} \int d \boldsymbol {\rho} _ {1} d \boldsymbol {\rho} _ {2} d \boldsymbol {\rho} _ {3} \phi_ {\alpha} \left(\rho_ {1} \rho_ {2} \rho_ {3}\right) \\ \left[ \mathbb {S} \left[ \varphi_ {a} ^ {*} (\boldsymbol {r} _ {1}) \varphi_ {b} ^ {*} (\boldsymbol {r} _ {2}) \right] _ {J _ {n}} \mathbb {S} \left[ \varphi_ {c} (\boldsymbol {r} _ {3}) \varphi_ {d} (\boldsymbol {r} _ {4}) \right] _ {J _ {p}} \right] _ {L M _ {L}} \tag {9} \\ \end{array}
$$

with coeffi $\begin{array} { r } { \varphi _ { a } \bigl ( r \bigr ) \ = \ \frac { u _ { n _ { a } l _ { a } j _ { a } } ( r ) } { r } Y _ { l _ { a } m _ { a } } \bigl ( \hat { r } \bigr ) } \end{array}$ , iz $W$ the usual Racah’sion and normaliza-$\mathbb { S }$ tion operator. This equation calculates the overlap integral between the single-particle states in nucleonic coordinates $_ { \pmb { T } } ^ { \star }$ and the alpha wave function in relative coordinates $\rho$ [17].

The expressions of this section reduce to that of Ref. [17] for the monopole interaction, i.e., $J _ { n } = J _ { p } = 0$ and $Z _ { n p } ^ { J } = 1$ .

# III. MODEL AND METHOD

The six $0 ^ { + }$ states of the $^ { 4 4 }$ Ti nucleus of the companion paper [20] are considered in the applications. These states are shown in Fig. 1 for the complete basis. The pole (PB) and complete (CB) many-body basis are specified in Table III of Ref. [20]. The pole basis is a manybody representation that includes only the resonant part of the single-particle continuum. The complete basis also contains the complex energy scattering states associated with the resonances of the pole basis, plus the real energy scattering states for the other partial waves. The single-particle energies are calculated using the Woods-Saxon and Spin-Orbit mean fields in Table I of Ref. [20]. The interactions described in Section III.B of Ref. [20] determine the two-body energy levels. All these parameters determine the single particle wave function, the two-$X _ { a b } ^ { J _ { n } }$ Xab , $X _ { c d } ^ { J _ { p } }$ , and four-body $Z _ { n p } ^ { 0 ^ { + } }$ amplitudes used for determining the formation amplitude. To study the impact of the four-body model space truncation on clusterization, we compare the calculation in the CB mentioned above with that of the truncated basis as defined in Ref. [20].

For the first time, reference [17] provided a thorough analysis of the impact of the parameters involved in determining the norm kernel and its effect on the normalized spectroscopic factors as defined by Fliessback

![](images/62b0414359da6e2a6c45b6000147c5d880dfb0837bb23205104f8dabe09acd7e.jpg)  
FIG. 1: Experimental (Exp) and calculated (CB) $0 ^ { + }$ states of $^ { 4 4 }$ Ti as explained in Ref. [20].

[23, 27]. The spacing $\Delta R$ between the Shifted Gaussian Functions (SGF) governs the quality of the basis set. If the SGF are widely separated, the basis becomes inadequate. If they are too close, it leads to an overcomplete representation [28]. Besides, the radial part of the SGF must also be normalized. The cutoff $R _ { m a x }$ (or the number of normalized SGF, $M$ ) influences the final result. Finally, the cutoff on the norm kernel eigenvalue $\nu _ { \mathrm { m a x } }$ significantly impacts the final value of the normalized spectroscopic factor.

Let us qualitatively describe the protocol for obtaining a reliable normalized spectroscopic factor with an assigned error. The determination of the normalized spectroscopic factor is performed in two steps. First, we initialize the SGF parameters $\Delta R$ and $R _ { \mathrm { m a x } }$ by expanding the single-particle core wave functions in the normalized SGF. A set of pairs $\Delta R$ and $R _ { \mathrm { m a x } }$ is established by defining an error for the expansion of the wave functions and the normalization of the SGF. Then, the normalized spectroscopic factor $\boldsymbol { S }$ , Eq. (5), is calculated for all possible $\nu _ { \operatorname* { m a x } } \leq M$ . Many of the estimated $\boldsymbol { S }$ diverge, but some patterns with plateaus can also be found; see, for example, Fig. 2. An exploration of this kind of figure gives a set of pair parameters $( \Delta R , R _ { \mathrm { m a x } } )$ of physical interest, as it is shown, for example, in Fig. 3 in section IV.

Next, we must determine $\nu _ { \mathrm { m a x } }$ to identify which plateau is adequate. The usual procedure is to take it as the change in the slope of $n _ { \nu }$ versus $\nu$ [17, 19, 26, 27, 29]. This criterion is unstable for different values $( \Delta R , R _ { \mathrm { m a x } } )$ , with $\Delta R$ and $R _ { \mathrm { m a x } }$ in the plateau [17]. Instead, we take all eigenvalues $n _ { \nu }$ with the condition that $s _ { \nu } ^ { L } < 1$ . We found that this criterion is more stable and, in some cases, coincides with the change in the slope of $n _ { \nu }$ . The motivation for constraining $s _ { \nu } ^ { L } \ < \ 1$ is that in practical

![](images/ce3baee79dbf79d9b9503df8ff636940661921ec40fdc51eb8250047fd080b7c.jpg)  
FIG. 2: Schematic representation of the normalized spectroscopic factor of Eq. (5) as a function of $\Delta R , R _ { \mathrm { m a x } } )$ parametrized on $\nu _ { \mathrm { m a x } }$ .

applications, the most important contributions to $S _ { L }$ are given for the $s _ { \nu } ^ { L }$ close to the slope change, just before $s _ { \nu } ^ { L }$ becomes bigger than the unit.

To determine an error to the calculated $S _ { L }$ , we thoroughly compute Eq. (5) on the three-dimensional parameter space $( \Delta R , R _ { \mathrm { m a x } } , \nu _ { \mathrm { m a x } } )$ . This calculation provides a colossal amount of normalized spectroscopic factors organized in a histogram, see, for example Fig. 5. Next, a Gaussian fit is performed around the calculated $S _ { L }$ . The error is defined as the width $\sigma$ of the Gaussian distribution.

# IV. APPLICATION: AMOUNT OF CLUSTERING

To illustrate the implementation of the protocol introduced in the previous section, the normalized spectroscopic factor is calculated for the $0 ^ { + }$ states of $^ { 4 4 }$ Ti using the wave functions calculated in Ref. [20]. A critical discussion of the results, in comparison with experimental data, is also performed.

Determination of the parameters: In order to estimate meaningful ranges for $\Delta R$ and $R _ { \mathrm { m a x } }$ , the singleparticle core states of $^ { 4 0 } \mathrm { C a }$ are expanded in the normalized SGF. The mean-field for proton and neutrons that define these states are the ones in Table I of Ref. [20]. The error for the normalization of the SGF is $1 0 ^ { - 4 }$ , while the absolute limit for the expansion of the singleparticle wave function is $1 0 ^ { - 2 } ~ \mathrm { f m ^ { - 1 / 2 } }$ . With these constrains we get the following ranges $0 . 4 \mathrm { f m } \lesssim \Delta \mathrm { R } \lesssim 0 . 8 \mathrm { f m }$ and $8 \mathrm { { f m } \lesssim \mathrm { { R } _ { m a x } \lesssim 1 0 \mathrm { { f m } } } }$ . Next, the normalized spectroscopic factor $\boldsymbol { S }$ is calculated for all possible values of $\nu _ { \mathrm { m a x } }$ , for each one of the $0 ^ { + }$ states. The result of this calculation is shown in Figure 3.

The second step of the protocol requires determining the cutoff $\nu _ { m a x }$ in Eq. (5). Figure 4 shows the distribution of the norm kernel eigenvalues $n _ { \nu }$ and $s _ { \nu }$ for a

![](images/c94296e4fdf8ed2a061d6712192957a299e12d3a7359f8a1f10a9514668fc2f2.jpg)

![](images/a714a71cd526259484bd0f901fb5db1eeccff54ee8c824d6375423798ea46ed1.jpg)

![](images/883ef0894ad513d655d39350ff2d69226d7dfe53ad3145a5dc44c4fb91fd09de.jpg)

![](images/d4f860f36e6b86e5f701b90b75f90a1cac0beab6cdef8f57961790ad2fd718c4.jpg)

![](images/abf616125dcef15d23c5455f9b7a163294bd9946e1f295f0122584bcd4e11af1.jpg)

![](images/5b065bb4f8faa9baa6124414571c52f580b17deff3b03066ada29c136d34d65c.jpg)  
FIG. 3: Normalized spectroscopic factor $\boldsymbol { S }$ parametrized in $\nu _ { \mathrm { m a x } }$ , as function of $\Delta R$ and $R _ { \mathrm { m a x } }$ .

typical case in the plateau region, $\Delta R = 0 . 4$ fm, $R _ { \mathrm { m a x } } = 8$ fm (these values for $\Delta R$ and $R _ { \mathrm { m a x } }$ are consistent with Refs. [24, 27]). The characteristic change in the slope of the norm kernel eigenvalues $n _ { \nu }$ can be appreciated in the region for which $s _ { \nu }$ became bigger than the unit $\nu \sim 1 5$ , 16.

![](images/9977a520819db5716962be243fbbd78bb18c6c7928c7fd02fcd0f7ef8867c967.jpg)

![](images/47f339d4b48dade1136d7c93d2802dd5d9e42e470c8764943af826d6844dca82.jpg)

![](images/fc74fbbd77874d12eeafe824f808ec844dc01da8dcc55d7a5b46a17b6539d768.jpg)

![](images/e23f780fcfc3aeb22f3e0bb81d1ec4b2ab724a0f3a94f128f7379cced59c0bc2.jpg)

![](images/6b89c54bbb332cc167daba238e4fd29f575fa1d9d71ff06339c167ee702690f1.jpg)

![](images/20105aea83fd3cc1a6f86aa0bb7491649ee00394e9480f0cbf2c0f09be1162a8.jpg)  
FIG. 4: Norm kernel eigenvalues $n _ { \nu }$ (filled circles) and partial spectroscopic factor $s _ { \nu }$ (filled bars) using the complete basis for each one of the $0 ^ { + }$ states of $^ { 4 4 } \mathrm { T i }$ .

Calculation of $\boldsymbol { S }$ : The calculated amount of cluster-

TABLE I: Amount of clustering (error in parenthesis) for the ground and excited $0 ^ { + }$ states of $\mathbf { ^ { 4 4 } T \dot { 1 } }$ calculated using the pole (PB) and complete (CB) bases.   

<table><tr><td></td><td colspan="2">S × 102</td></tr><tr><td>i</td><td>PB</td><td>CB</td></tr><tr><td>1</td><td>1.7(2) - i 0.2</td><td>2.1(2)</td></tr><tr><td>2</td><td>5.1(2), -i 2.2</td><td>7.3(4)</td></tr><tr><td>3</td><td>6.4(3), -i 0.5</td><td>4.6(2)</td></tr><tr><td>4</td><td>1.2(6), -i 0.5</td><td>10(1)</td></tr><tr><td>5</td><td>25(1), -i 5</td><td>49.3(2)</td></tr><tr><td>6</td><td>1.8(5), -i 0.2</td><td>2.1(1)</td></tr></table>

ing for each one of the $0 ^ { + }$ states is shown in Table I for the pole (PB) and complete basis (CB). Due to the truncation of the non-resonant continuum in the PB, $\boldsymbol { S }$ has a spurious imaginary component which varies from 16 to $4 3 \%$ . The inclusion of the non-resonant continuum (CB) wipes out the imaginary component and produces, in general, an enhancement of $\boldsymbol { S }$ . The increase in the amount of clustering is remarkable for the $0 _ { 4 } ^ { + }$ and $0 _ { 5 } ^ { + }$ excited states. The influence of the non-resonant continuum in the amount of clustering contrasts with its effects on the wave function amplitudes (see Table I of the companion paper [20]), where the non-resonant continuum mildly changes its real part, but rectifies the spurious imaginary component.

In Ref. [20], it was assumed that clusterization could be inferred from the amount of collectivity of the wave function. So, only single-particle width was calculated for the states $0 _ { 3 } ^ { + }$ and $0 _ { 5 } ^ { + }$ . The results of the amount of clustering of Table I reveal that this is not necessarily the case; for example, the state $0 _ { 4 } ^ { + }$ also has an appreciable clusterization.

States below the threshold: No excited states below the alpha-threshold was found [20]. A shell model calculation using the effective Kuo and Brown interaction also found none of these experimental states [30, 31]. Presumably, because they have different configurations than four-nucleon valence states; in particular, the first excited state belongs to the $N \ = \ 1 2$ band head [32]. The calculated spectroscopic factor of the ground state is 0.02. Since the spectroscopic factor is not an observable, it is model dependent [33–35]. The ground state’s alpha spectroscopic factor seems particularly intriguing since it ranges from 0.04 [36], 0.03-0.08 [35], 0.2 [37], to ∼ 1 [34, 38–40]. Our calculated value is closer to the one obtained from finite-range model [35] which uses complex squared Woods-Saxon optical potential [41].

States above the threshold: The calculated amount of clustering of the state $0 _ { 2 } ^ { + }$ is only 0.07. This state has no experimental counterpart but agrees in energy with Ref. [42]. In Ref. [20], the calculated state at 6.641 MeV was assigned to the $0 _ { 3 } ^ { + }$ due to its proximity to the experimental level $( 0 , 2 ) ^ { + }$ at 6.810 MeV [43]. The amount of clustering of this state is also small, 0.046. This figure compares well with 0.02 of Ref. [36], which assigns the quantum number $2 ^ { + }$ to this state. The amount of clus-

tering of the state $0 _ { 4 } ^ { + }$ , at the energy 7.857 MeV, is 0.10. Even when this state is $\sim$ 700 keV apart, we associate it with the state $( 0 ^ { + } , 1 ^ { - } )$ (this state was inadvertently left out in the companion paper [20]) at the energy 8.54 MeV. Reference [38] makes the tentative assignment of $0 ^ { + }$ for the state 8.54 MeV, with a tentative ratio of eight between its spectroscopic factor and the ground state. The amount of clustering of the state $0 _ { 5 } ^ { + }$ ( $T = 2$ [20]) is 0.49. Although 1.147 MeV apart from the experimental level at 9.338 MeV, it must be paired with it because it is the first experimental $T = 2$ state. The last state, $0 _ { 6 } ^ { + }$ , at the energy 9.401, has an amount of clustering of 0.02. There are not experimental spectroscopic factors for $0 ^ { + }$ states above 9 MeV, although, for high spin state they ranges from 0.02 to 0.003 [36].

Error for $\boldsymbol { S }$ : Following the protocol described in Section III for calculating the error, we get the histograms shown in Fig. 5. The errors range between 5% and $1 0 \%$ , as shown in Table I. The state $0 _ { 6 } ^ { + }$ exhibits the narrower Gaussian distribution when it corresponds to the state with a more extensive convergence plateau in Fig. 3. A dashed vertical line indicates the usual spectroscopic factor in the figure. For all states but the ground state, the Fliessbach procedure increases the spectroscopic factor.

Conventional spectroscopic factor: The usual $g ( R )$ and normalized $G ( R )$ formation amplitudes for the complete basis are shown in Fig. 6. The formation amplitude shows the usual overlap shape [17]. In contrast, the normalized one resembles an alpha single-particle wave function with several nodes ranging from six to eight. The maximum of the normalized forming amplitude is noticeably larger than the maximum of the usual formation amplitude, except for the ground state. The Fliessbach normalization produces a displacement of the peak to the outer region of the nuclear surface around $\sim 5 - 6 \mathrm { f m }$ , consistent with a rough approximation $R _ { c o r e } + R _ { \alpha } \sim 6$ fm.

# V. APPLICATION: ALPHA-DECAY WIDTH AND HALF-LIFE

We calculate the single-particle width $\Gamma _ { \mathrm { s p } }$ of the excited states by taking the average of the calculation obtained with the two mean-field potentials as explained in the companion paper [20]. Using the amount of clustering $\boldsymbol { S }$ of the previous section (Table I), we get the absolute alpha-width $\Gamma = S \Gamma _ { \mathrm { s p } }$ and half-life $T _ { 1 / 2 } = \ln 2 \hbar / \Gamma$ . The error for the single-particle width was defined through the two mean fields as discussed in Ref. [20], while the error for $\Gamma$ corresponds to the error propagation from $\Gamma _ { \mathrm { s p } }$ and $\boldsymbol { S }$ . These results are presented in Table II.

The calculated half-life of the not observed $0 _ { 2 } ^ { + }$ state is of the order of microsecond due to its proximity to the alpha-threshold, while the half-life of the $0 _ { 3 } ^ { + }$ is 24 ns, three times bigger than the lower limit proposed in Ref. [20]. Figure 7 shows that its half-live decreases by a factor of ten when the energy is taken as the paired state

![](images/5cdb84959c549e7cdbbc3dc4604001fe886486f627927a385affa1c3b8fb0c12.jpg)

![](images/83ca7dcfda74569b34875a5695cf343b69c2a6faaaa90d8dc34b62f3ce39b887.jpg)

![](images/469773bdb70545c047fa64d07189781613d1e2dc52341135d68d2a4fe80c228b.jpg)

![](images/2aa07614db7599b4b3b098a9b80aba3de78dc5fb9e3dc7008c4063a14f083cc6.jpg)

![](images/6bc73a38fc126ba5730751729f0f40c8a546b41e1324e31177c9fd6969ff9ddd.jpg)

![](images/ac386f9e08c72da1e1adbd802ea3423d8b93d9904363b57175c5fdcbba114bd4.jpg)  
FIG. 5: Histogram for occurrences of the normalized spectroscopic factors calculated as explained in Sec. III. The dashed vertical lines in each histogram correspond to the usual spectroscopic value [17]. The fitted Gaussian curve is shown around each normalized spectroscopic factor of Table I (CB).

TABLE II: Alpha single-particle width $\Gamma _ { \mathrm { s p } }$ and alpha width $\Gamma$ scaled with the amount of clustering $\boldsymbol { S }$ , for the excited states of $^ { 4 4 }$ Ti in the complete basis [20]. The calculated half-live of the $0 _ { 5 } ^ { + }$ state incorporated $\Gamma _ { \gamma } = 0 . 7 5 \times 1 0 ^ { - 6 }$ MeV [44]. Errors are given in parentheses.   

<table><tr><td>State</td><td>Γsp (MeV)</td><td>Γ (MeV)</td><td>T1/2 (sec)</td></tr><tr><td>0+2</td><td>0.13(2) × 10-14</td><td>0.95(15) × 10-16</td><td>0.48 × 10-5</td></tr><tr><td>0+3</td><td>0.42(16) × 10-12</td><td>0.19(7) × 10-13</td><td>0.24 × 10-7</td></tr><tr><td>0+4</td><td>0.11(1) × 10-5</td><td>0.11(1) × 10-6</td><td>0.43 × 10-14</td></tr><tr><td>0+5</td><td>0.15(4) × 10-4</td><td>0.74(20) × 10-5</td><td>0.56 × 10-16</td></tr><tr><td>0+6</td><td>0.54(10) × 10-2</td><td>0.11(2) × 10-3</td><td>0.40 × 10-17</td></tr></table>

$( 0 , 2 ) ^ { + }$ . Vertical lines in the figure indicate the calculated and experimental states.

It is known that the $T = 2$ state decay mainly by $\gamma$ but also by $\alpha$ , with $\Gamma _ { \gamma } = 0 . 7 5 { \scriptstyle \pm 0 . 1 9 \mathrm { ~ e V } }$ and $\Gamma _ { \alpha } = 0 . 3 5 { \pm } 0 . 0 7 \ : \mathrm { e V }$

![](images/b2ccc17c893c802591c6d5b77c0025f45b4a600b12d71b6e6a84340cd7870d34.jpg)

![](images/277a10a73e45d672c8790e4a5c31c3812301bd16f04681e87bdc0f22dc688bc8.jpg)

![](images/b636c0612acae806c89ed6e5887443a378857708f01d4dfcb97032641b61f9d6.jpg)

![](images/af47a3747bb9be194927d83b4383e5a42126137520ee6ed6cc49349e3ba13de2.jpg)

![](images/6a512a40407ab436c3df0c39c0346c4bee3021c538fe03fba7ed6cf01549ec70.jpg)

![](images/1c5745872967566ad843f9e7967d72695cfbbaf3121636c1e469b63ed197f7b9.jpg)  
FIG. 6: Conventional $g ( R )$ (dashed line) and normalized $G ( R )$ (continuum line) formation amplitudes of the six states $0 ^ { + }$ calculated in the complete basis.

![](images/0cbe6596a4a064f1a0496d451ec1578b30191f055d50da6becba26257253e566.jpg)  
FIG. 7: Alpha-decay width (increasing curve with right scale) and half-life (left scale) of the state $0 _ { 3 } ^ { + }$ as functions of the decay energy. The calculated energy and the energy of the paired estate are shown as vertical lines. The width of the curves represents the error calculated, as explained in the text.

[44]. Our calculated value is 7.4 eV, which is twenty times bigger than the experimental one. This could indicate that the clusterization is not as big (49 $\%$ ) as our result predicts. The $0 _ { 4 } ^ { + }$ state can be considered an alpha-decay

candidate for $^ { 4 4 } \mathrm { T i }$ with a half-life of 4.3 fs.

# VI. TRUNCATED HILBERT SPACE

The Gamow wave function and the Gamow Shell Model for calculating $\Gamma _ { \mathrm { s p } }$ and $\boldsymbol { S }$ , respectively, unify the reaction and structure parts of the alpha-decay calculation. There are two main parts of this unified approach which demand considerable computation resources. The first is calculating the four-body wave function in the full Berggren representation, including the non-resonant continuum. The second one is the many-dimensional integrals. To reduce the computation time, we investigate the effect of the many-body Hilbert space truncation on the amount of clustering. We calculate it in the four-body basis generated with the neutron-neutron and protonproton bases up to 10 MeV of excitation energy, called Case $I I$ in Ref. [20]. Table III shows the result.

TABLE III: Ratio of the amount of clustering in the CB versus the one in the truncated basis (Case $I$ and Case II, respectively in Ref. [20]).   

<table><tr><td>Ratio</td><td>01+</td><td>02+</td><td>03+</td><td>04+</td><td>05+</td><td>06+</td></tr><tr><td>SCase I/SCase II</td><td>2.6</td><td>50</td><td>15</td><td>12</td><td>1.3</td><td>1</td></tr></table>

The amount of clustering decreases in most of the states calculated on the truncated basis. This indicates that high-energy excited states of the many-body bases are important to build the clusterization. This behavior contrasts with the one found for the wave function amplitudes, for which the truncation has no significant effects (see Table VIII in [20].) This analysis shows that truncating the many-body Hilbert space may be justified for calculating spectra and wave functions but not for calculating the amount of clustering.

# VII. SUMMARY AND CONCLUSIONS

The present work and the companion paper [20] takes the $0 ^ { + }$ states of the nucleus $^ { 4 4 }$ Ti to refine the technique introduced in Ref. [17] for the calculation of the halflive of drip-line nuclei. The resonant model space of Ref. [17] was complemented with the non-resonant continuum. Consequently, the spurious imaginary part on the twoand four-body wave functions and on the formation amplitudes disappeared. An effective Gaussian interaction replaced the schematic separable force. This force produced more realistic two-particle spectra and wave functions. The missing proton-neutron interaction in [17] was incorporated into the formalism. This extra interaction permitted adjustments to the four-body threshold. It also contributes to gaining extra correlations, which are essential in the alpha-decay process. Finally, a protocol for calculating the normalized spectroscopic factor and an associated numerical error was introduced. Besides

all these improvements, the calculation indicates that the tensor interaction is essential for properly describing the neutron-proton threshold and possibly affects the amount of clustering.

It was shown that the many-body Hilbert space truncation, although valid for determining the spectrum and wave functions, is not valid for clustering calculation. This result indicates that while the effect of the missing correlations in the spectrum may be compensated by renormalizing the interaction, this is not the case when it comes to clustering many nucleons. It was also shown that the non-resonant continuum is important not only to eliminate the spurious imaginary part of the pole approximation but also to create essential multi-nucleon correlations.

The Fliessbach normalization produces that the profile of the spectroscopic factor changes from an overlapping shape to that of the alpha-daughter wave function. The normalized spectroscopic factor can then be used to generate an effective Heel-Wheeler potential between the alpha cluster and the core nucleus. The effect of Fliessbach normalization is also noticeable in a shift of the maximum of amplitude towards the outside part of the radial coordinate.

The amount of clusterization of the calculated $0 ^ { + }$ states of $^ { 4 4 }$ Ti range from ∼ 2% to $\sim 5 0 \%$ . The value of $\boldsymbol { S }$ of the ground state is small, in agreement with some bibliography and strong disagreement with others. This par-

ticular state shows a significant model dependence on the definition of the spectroscopic factor. For the excites states, the minimum $( \sim 2 \% )$ is reached by the $T = 1$ state, while the maximum is for the $T = 2$ one, although this figure may be overestimated since the calculated width is twenty times bigger than the experimental one. We found a near-threshold alpha-decay state with a half-live of $5 \mu \mathrm { s }$ . The calculated half-live for the state $0 _ { 3 } ^ { + }$ paired with the experimental $( 0 , 2 ) ^ { + }$ is the order of nanoseconds, while the state $0 _ { 4 }$ , paired with the experimental $( 0 ^ { + } 1 ^ { - } )$ , is calculated to have a half-live of 4 fs.

As a final remark, including the non-resonant continuum allows alpha-decay calculation beyond the drip line. In particular, in the region $N = Z = 5 0$ , where each proton’s single-particle state is unbound. An application to the alpha-decay of the nucleu s 104Te is in progress. $^ \mathrm { 1 0 4 }$

# ACKNOWLEDGMENTS

This work has been partially supported by CON-ICET (Consejo Nacional de Investigaciones Cient´ıficas y T´ecnicas, Argentina) through Grant No. PIP-0930. The computations were performed on the Computational Center of CCT-Rosario and CCAD-UNC, members of the SNCAD, MincyT-Argentina.

[1] A. Volya and Y. M. Tchuvil’Sky, Physical Review C 91, 1 (2015).   
[2] S. Yang, C. Xu, and G. R¨opke, Phys. Rev. C 104, 034302 (2021).   
[3] R. G. Thomas, Progress of Theoretical Physics 12, 253 (1954).   
[4] A. M. Lane and R. G. Thomas, Reviews of Modern Physics 30, 257 (1958).   
[5] A. Arima and S. Yoshida, Physics Letters B 40 (1972).   
[6] T. Fliessbach, Journal of Physics G: Nuclear and Particle Physics 2, 531 (1976).   
[7] H. J. Mang, Z. Physik 148, 582 (1957).   
[8] H. D. Zeh, Zeitschrift f¨ur Physik A: Atoms and Nuclei 175, 490 (1963).   
[9] H. J. Mang, Annual Review of Nuclear Science 14, 1 (1964).   
[10] K. Harada, Progress of Theoretical Physics 26, 667 (1961).   
[11] F. A. Janouch and R. J. Liotta, Physical Review C 27, 896 (1983).   
[12] G. Dodig-Crnkovic, F. A. Janouch, R. J. Liotta, and Z. Xiaolin, Physica Scripta 37, 523 (1988).   
[13] T. Fliessbach and P. Manakos, J. Phys. G: Nucl. Phys. 3, 643 (1977).   
[14] I. Tonozuka and A. Arima, Nuclear Physics A 323, 45 (1979).   
[15] S. M. Lenzi, O. Dragun, E. E. Maqueda, R. J. Liotta, and T. Vertse, Physical Review C 48, 1463 (1993).   
[16] D. S. Delion and J. Suhonen, Physical Review C 61, 12

(2000).   
[17] R. M. Id Betan and W. Nazarewicz, Physical Review C 86 (2012).   
[18] K. Varga, R. G. Lovas, and R. J. Liotta, Physical Review Letters 69, 37 (1992).   
[19] R. G. Lovas, R. J. Liotta, A. Insolia, K. Varga, and D. S. Delion, Physics Reports 294, 265 (1998).   
[20] A. C. Dassie and R. M. Id Betan, Phys. Rev. C 108, 044314 (2023).   
[21] E. L. Cooperman, M. H. Shapiro, and H. Winkler, Nuclear Physics A 284, 163 (1977).   
[22] D. Robertson, J. G¨orres, P. Collon, and M. Wiescher, Physical Review C 85, 045810 (2012).   
[23] T. Fliessbach, Zeitschrift f¨ur Physik A: Atoms and Nuclei 272, 39 (1975).   
[24] T. Fliessbach and H. J. Mang, Nuclear Physics A 263, 75 (1976).   
[25] R. Beck, F. Dickmann, and R. G. Lovas, Annals of Physics 173, 1 (1987).   
[26] K. Varga, R. G. Lovas, and R. J. Liotta, Nuclear Physics A 550, 421 (1992).   
[27] T. Fliessbach, Zeitschrift f¨ur Physik A: Atoms and Nuclei 277, 151 (1976).   
[28] S. Saito, Progress of Theoretical Physics 41, 705 (1969). [29] A. Arima, AIP Conference Proceedings 47, 1 (1978).   
[30] J. J. Simpson, W. R. Dixon, and R. S. Storey, Physics Letters B 30, 478 (1969).   
[31] W. R. Dixon, R. S. Storey, and J. J. Simpson, Physical Review C 18, 2731 (1978).

[32] F. Michel, G. Reidemeister, and S. Ohkubo, Phys. Rev. Lett. 57, 1215 (1986).   
[33] G. Kramer, H. Blok, and L. Lapikas, Nuclear Physics A 679, 267 (2001).   
[34] H. W. Fulbright, C. L. Bennett, R. A. Lindgren, R. G. Markham, S. C. McGuire, G. C. Morrison, U. Strohbusch, and J. T¯oke, Nuclear Physics A 284, 329 (1977).   
[35] U. K. Mazumder, A. Somadder, E. Hoque, Y. Haque, S. K. Das, and H. M. S. Gupta, Pramana - J Phys 86, 1275 (2016).   
[36] T. Yamaya, S. Oh-Ami, M. Fujiwara, T. Itahashi, K. Katori, M. Tosaki, S. Kato, S. Hatori, and S. Ohkubo, Physical Review C 42, 1935 (1990).   
[37] T. Yamaya, S. Ohkubo, S. Okabe, and M. Fujiwara, Phys. Rev. C 47, 2389 (1993).   
[38] U. Strohbusch, C. L. Fink, B. Zeidman, R. G. Markham, H. W. Fulbright, and R. N. Horoshko, Phys. Rev. C 9, 965 (1974).   
[39] C.-Y. Kim and T. Udagawa, Physical Review C 46, 532

(1992), publisher: American Physical Society.   
[40] P. Guazzoni, M. Jaskola, L. Zetta, K. Chong-Yeal, T. Udagawa, and G. Bohlen, Nuclear Physics A 564, 425 (1993).   
[41] F. Michel, J. Albinski, P. Belery, T. Delbar, G. Gregoire, B. Tasiux, and G. Reidemeister, Phys. Rev. C 28, 1904 (1983).   
[42] J. A. Shah and M. Danos, Physical Review 183, 899 (1969).   
[43] W. Bohne, K. D. B¨uchs, H. Fuchs, K. Grabisch, D. Hilscher, U. Janetzki, U. Jahnke, H. Kluge, T. G. Masterson, and H. Morgenstern, Nuclear Physics A 284, 14 (1977).   
[44] S. J. Freedman, C. A. Gagliardi, M. A. Oothoudt, A. V. Nero, R. G. H. Robertson, F. J. Zutavern, E. G. Adelberger, and A. B. McDonald, Physical Review C 17, 2071 (1978), publisher: American Physical Society.