# Cluster decay dynamics of Actinides yielding non-Pb-daughter

Joshua T. Majekodunmi $^ { 1 }$ ,∗ M. Bhuyan $^ 2$ ,† and Raj Kumar3‡

$^ { 1 }$ Institute of Engineering Mathematics, Universiti Malaysia Perlis, Arau, 02600, Perlis, Malaysia

2Center for Theoretical and Computational Physics, Department of Physics,

Faculty of Science, University of Malaya, Kuala Lumpur 50603, Malaysia and

$^ 3$ School of Physics and Materials Science, Thapar Institute of Engineering and Technology, Patiala, Punjab 147004, India

(Dated: July 6, 2023)

The cluster dynamics of radioactive nuclei decaying to neighbouring daughter nuclei of the double magic $^ { 1 3 2 }$ Sn and $^ { 2 0 8 }$ Pb is investigated using the relativistic mean-field (RMF) approach with NL3∗ parameter set within the preformed cluster-decay model (PCM). The novel feature of the present study is the application of the newly derived preformation formula, laying the groundwork for accessing the break-up of the Q-value: preformation energy, cluster emission energy and the recoil energy of the daughters formed. The energy associated with cluster preformation is theoretically quantified for the first time. This treatment underscores the shell effect, pairing correlation as well as the blocking of particular orbitals by unpaired nucleons. To ascertain the applicability of the new formula, the PCM based calculations are carried out with nuclear potential obtained using the phenomenological M3Y and microscopic RMF-based R3Y nucleon-nucleon (NN) potentials along with corresponding densities. We found a marginal variation that can be attributed to the difference in their barrier properties, however, the predictions for the case of both M3Y and R3Y potentials are found to agree well with the experimental half-lives. Although none of the considered reaction systems yields a double magic daughter nucleus, we found that the kinematics of their cluster emissions is governed by their proximity to the shell closure. The deduced systematic of the recoil energy in cluster decays can provide valuable insight for the synthesis of elements in superheavy mass region in the future.

PACS numbers: 21.65.Mn, 26.60.Kp, 21.65.Cd

# I. INTRODUCTION

The bedrock of nuclear physics can be traced to the discovery of natural radioactivity. Particularly, the spontaneous disintegration of nuclei in which the emitted particles are heavier than 4He but lighter than fission fragments was first predicted by Sandulescu [1] and experimentally observed by Rose and Jones [2]. Thereafter, the possibility of emission of several other clusters ranging from 14C $^ { - 3 4 }$ Si from various heavy nuclei have been discovered [3] and their daughter nuclei are usually the double magic nucleus $^ \mathrm { 2 0 8 }$ Pb and its neighbouring nuclei. This dominant double magic structure in the heavier fragment strongly indicates the shell effect on cluster radioactivity. Thus, cluster emission for heavy nuclei is a highly asymmetry fission process [4].

Beside the empirical relations [5, 6] used for the calculation of decay half-lives, the literature is replete with several microscopic descriptions of cluster emission [7– 10]. Clustering occurs as an intermediate process between $\alpha$ -decay and spontaneous fission. From the theoretical front, it follows the description of the Gamow model of $\alpha$ -decay which hinges on the quantum tunnelling effect [11, 12]. Nonetheless, cluster decay models can be classified into two different approaches based

on their treatment of cluster emissions. The first is the fission-like models [13–16] where it is assumed that clusters are gradually formed as the parent nucleus undergoes successive geometrical deformation until it reaches a saddle or scission point. The second refers to the alpha-like models e.g. the preformed cluster-decay model (PCM) [17–20] which holds the assumption that clusters are pre-formed within the decaying parent nucleus before its penetration across the interaction barrier. Unlike the fission-like models where the preformation probability $P _ { 0 }$ is usually taken as unity (i.e. $P _ { 0 } = 1$ ), the PCM requires the calculation of a realistic $P _ { 0 }$ which could be challenging due to the complexities associated with the many-body system and the variability of the nuclear potential. As such, certain range of $P _ { 0 }$ values have been assigned to different regions of the nuclear chart (in Table 2 of Ref.[21] and the references therein) and various $P _ { 0 }$ formulae [22, 23] have been employed to reproduce the experimental half-lives. Yet, no complete/clear link that is traceable to the mechanism of cluster emission has been established.

However, we have demonstrated in our recent studies [24–26] that a thorough estimate of cluster preformation can shed new light on the essential features of the decaying system. Further, the cluster preformation energy was systematically quantified for the first time. We realised that there is a distinct but subtle difference in the behaviours of the radioactive nuclei yielding the double magic daughter $^ { 2 0 8 }$ Pb in comparison and those with daughters in its vicinity. This could be due to numer-

ous reasons (e.g pairing and odd-even staggering effects associated with open-shell nuclei, relatively higher binding energies (and Q-values) of parent nuclei with double magic daughters at shell closure or a relatively low number of valence particles of isotopes near the shell closure and other factors) which the present study aims to establish in connection with their effect(s) on the preformation and mechanism of cluster emissions. Moreover, the effective number of valence particles (or holes) is known to largely influence the parameterization of several nuclear quantities [27]. Besides, in $\alpha$ -decay studies [21, 28], it has been demonstrated that the preformation probability of nuclei near magic numbers is susceptible to rapid variations. As an extension, the present study will be devoted to probing the behaviour and trend of $P _ { 0 }$ for near magic-number daughters in cluster decays. Thus, cluster formation energy and the recoil effect of the daughter nuclei are taken into consideration within the PCM. The only adjustable parameter of the PCM is the neck-length $\Delta \mathrm { R }$ which accounts for the relative separation (whose proximity potential limit is in the range $( 0 . 0 - 2 . 0 ) $ fm [29]) between the decay fragments and decides the $1 ^ { s t }$ turning point of the barrier penetration [30].

It is assumed that the preformed clusters tunnels across the barrier jointly built by the Coulomb and the nuclear potentials. The nuclear potential between the emitted cluster and the daughter nuclei is obtained from the well-established double-folding technique [31]. One of the necessary inputs for the double-folding technique is the nuclear matter densities of the decay fragment which is estimated in this study from the relativistic mean-field (RMF) [32–35] with the NL3∗ parameter set [36]. The RMF formalism is well known for its successful description of various bulk properties of nuclei in both ground and excited states [37–39]. The second input for the double-folding process is the effective nucleon-nucleon (NN) interaction [31]. Here, we employ the phenomenological M3Y NN potential and the microscopic R3Y NN potential [18, 20, 40] which stems from the non-linear RMF Lagrangian [41, 42] for the sake of comparison. In our previous studies [18, 30, 40], we have demonstrated that $\Delta \mathrm { R } = 0 . 5$ fm is suitable enough for M3Y interaction while the R3Y fits nicely at $\Delta \mathrm { R } = 1 . 0$ fm in cluster radioactivity. The Q-values are estimated from the experimental binding energies given in a recent mass table [43]. The penetration probability $P$ is calculated from the well-known Wentzel-Kramers-Brillouin (WKB) approximation.

Sec. II briefly describes the theoretical framework: non-linear RMF Lagrangian, the double-folding technique for both R3Y and M3Y potentials, the preformed cluster-decay model (PCM) and our recently derived $P _ { 0 }$ formula and its components. The obtained results are discussed in Sec. III. Finally, the conclusion and summary of this work are given in Sec. IV.

# II. THEORETICAL FORMALISM

The relativistic mean-field (RMF) approach denotes a kind of implementation of the density functional theory based on a Lorentz covariance. An atomic nucleus is considered as a system composed of Dirac nucleons, exchange various mesons $( \sigma , \ \omega$ and $\rho$ ) and the photon field ( $A _ { \mu }$ ) through an effective Lagrangian given by [18, 20, 32–35],

$$
\begin{array}{l} \mathcal {L} = \overline {{\psi}} _ {i} \left\{i \gamma^ {\mu} \partial_ {\mu} - M \right\} \psi_ {i} + \frac {1}{2} \partial^ {\mu} \sigma \partial_ {\mu} \sigma \\ - \frac {1}{2} m _ {\sigma} ^ {2} \sigma^ {2} - \frac {1}{3} g _ {2} \sigma^ {3} - \frac {1}{4} g _ {3} \sigma^ {4} - g _ {\sigma} \overline {{\psi}} _ {i} \psi_ {i} \sigma \\ - \frac {1}{4} \Omega^ {\mu \nu} \Omega_ {\mu \nu} + \frac {1}{2} m _ {\omega} ^ {2} \omega^ {\mu} \omega_ {\mu} - g _ {\omega} \overline {{\psi}} _ {i} \gamma^ {\mu} \psi_ {i} \omega_ {\mu} \\ - \frac {1}{4} \vec {B} ^ {\mu \nu}. \vec {B} _ {\mu \nu} + \frac {1}{2} m _ {\rho} ^ {2} \vec {\rho} ^ {\mu}. \vec {\rho} _ {\mu} - g _ {\rho} \bar {\psi} _ {i} \gamma^ {\mu} \vec {\tau} \psi_ {i}. \vec {\rho} ^ {\mu} \\ - \frac {1}{4} F ^ {\mu \nu} F _ {\mu \nu} - e \bar {\psi} _ {i} \gamma^ {\mu} \left(\frac {1 - \tau_ {3 i}}{2}\right) \psi_ {i} A _ {\mu}. \tag {1} \\ \end{array}
$$

The parameters $g _ { \sigma }$ , $g _ { \omega }$ , $g _ { \rho }$ denotes the respective coupling constants of the mesons whose corresponding masses are $m _ { \sigma }$ , $m _ { \omega }$ and $m _ { \rho }$ while $M$ is the mass of nucleons. Similarly, $g _ { 2 }$ , $g _ { 3 }$ and $\frac { e ^ { 2 } } { 4 \pi }$ are the coupling constants of the non-linear terms. The third component of the isospin is $\tau _ { 3 i }$ . Here, the contribution of the $\pi$ -meson has been omitted in Eq. (1) in the mean-field calculation due to its pseudoscalar nature [35, 44]. A detailed description of the field tensors for $\omega ^ { \mu }$ , $\vec { \rho _ { \mu } }$ and $A _ { \mu }$ fields can be found in Ref [45] and the references therein. By taking the field tensors as classical fields, the Dirac equation is obtained for the nucleons and simplified as,

$$
[ - i \alpha . \nabla + \beta (M ^ {*} + g _ {\sigma} \sigma) + g _ {\omega} \omega + g _ {\rho} \tau_ {3} \rho_ {3} ] \psi_ {i} = \epsilon_ {i} \psi_ {i}. (2)
$$

Similarly, the Klein-Gordon equations for the participating mesons are simplified as

$$
\left(- \nabla^ {2} + m _ {\sigma} ^ {2}\right) \sigma (r) = - g _ {\sigma} \rho_ {s} (r) - g _ {2} \sigma^ {2} (r) - g _ {3} \sigma^ {3} (r),
$$

$$
\left(- \nabla^ {2} + m _ {\omega} ^ {2}\right) V (r) = g _ {\omega} \rho (r),
$$

$$
\left(- \nabla^ {2} + m _ {\rho} ^ {2}\right) \rho (r) = g _ {\rho} \rho_ {3} (r). \tag {3}
$$

These equations are solved self consistently using the NL3∗ parameter set. Within the limit of one-meson exchange for a heavy and static baryonic medium, the microscopic R3Y NN potential is obtained as,

$$
\begin{array}{l} V _ {e f f} ^ {R 3 Y} (r) = \frac {g _ {\omega} ^ {2}}{4 \pi} \frac {e ^ {- m _ {\omega} r}}{r} + \frac {g _ {\rho} ^ {2}}{4 \pi} \frac {e ^ {- m _ {\rho} r}}{r} - \frac {g _ {\sigma} ^ {2}}{4 \pi} \frac {e ^ {- m _ {\sigma} r}}{r} \\ + \frac {g _ {2} ^ {2}}{4 \pi} r e ^ {- 2 m _ {\sigma} r} + \frac {g _ {3} ^ {2}}{4 \pi} \frac {e ^ {- 3 m _ {\sigma} r}}{r} + J _ {0 0} (E) \delta (s (4) \\ \end{array}
$$

Here $J _ { 0 0 } ( E ) \delta ( s )$ is the zero-range pseudopotential symbolizing the exchange effect. Eq. (4) is similar to the phenomenological prescription of Reid-Elliott [31] called M3Y NN potential which is constructed to reproduce the G-matrix element. The M3Y NN potential takes the

TABLE I. Fitting parameters a, b and c for the preformation formula in Eq. (14) for known experimentally favoured cluster decays. The Chi-square ( $\chi ^ { 2 }$ ) for the half-life predictions of the M3Y and R3Y interactions are given in columns 5 and 6 respectively. Note that odd-odd cluster emitters have not been experimentally observed.   

<table><tr><td rowspan="2">System</td><td colspan="3">Constant Parameters</td><td colspan="2">x²</td></tr><tr><td>a</td><td>b</td><td>c</td><td>M3Y</td><td>R3Y</td></tr><tr><td>e-e</td><td>17.67</td><td>0.114</td><td>8.00</td><td>0.284</td><td>0.075</td></tr><tr><td>o-A</td><td>16.12</td><td>0.119</td><td>0.88†</td><td>0.390¶</td><td>0.063¶</td></tr><tr><td></td><td>16.12</td><td>0.119</td><td>4.02§</td><td>0.061</td><td>0.065</td></tr></table>

†Parameter $_ c$ appears lower for systems having daughters with non-magic neutron numbers $N _ { d } \leq 1 2 6 )$ .   
§Systems having daughters with a magic neutron (or neighbours) require a higher value of parameter $^ c$ $2 6 \leq N _ { d } \leq 1 2 8 )$ ).   
¶Experimental lower limits are available here.

form,

$$
V _ {e f f} ^ {M 3 Y} (r) = 7 9 9 9 \frac {e ^ {- 4 r}}{4 r} - 2 1 3 4 \frac {e ^ {- 2 . 5 r}}{2 . 5 r} + J _ {0 0} (E) \delta (s). \tag {5}
$$

The double folding technique [31] is employed to calculate the nuclear interaction potential $V _ { n } ( R )$ and expressed as

$$
V _ {n} (R) = \int d r _ {c} \int d r _ {d} \rho_ {c} (\vec {r} _ {c}) \rho_ {d} (\vec {r} _ {d}) V _ {e f f} (\vec {r} _ {c d} = \vec {R} + \vec {r} _ {d} - \vec {r} _ {c}), \tag {6}
$$

where $\rho _ { c }$ and $\rho _ { d }$ are the nuclear densities of the cluster and daughter nuclei respectively. $V _ { n } ( R )$ given by Eq. (6) combines with the Coulomb potential $\begin{array} { r } { V _ { C } ( R ) = \frac { Z _ { c } Z _ { d } } { R } e ^ { 2 } } \end{array}$ to obtain the total interaction potential

$$
V (R) = V _ {n} (R) + V _ {C} (R) + V _ {\ell} (R), \tag {7}
$$

which is used to estimate the WKB penetration probability and hence, the cluster decay half-lives using the preformed cluster-decay model (PCM) [30]. Note that the contribution of the centrifugal potential $\begin{array} { r } { V _ { \ell } ( R ) = \frac { \hbar ^ { 2 } \ell ( \ell + 1 ) } { 2 \mu R ^ { 2 } } } \end{array}$ (where $\mu = m ( A _ { c } A _ { d } / A )$ is the reduced mass) is neglected in the ground state to ground state transitions where the angular momentum $\ell = 0$ . The penetration probability of clusters across the tunnelling path is given as

$$
P = P _ {a} W _ {i} P _ {b}, \tag {8}
$$

which involves a three step process [18]. Here,

$$
P _ {a} = \exp \left(- \frac {2}{\hbar} \int_ {R _ {a}} ^ {R _ {i}} \left\{2 \mu [ V (R) - V (R _ {i}) ] \right\} ^ {1 / 2} d R\right), \tag {9}
$$

and

$$
P _ {b} = \exp \left(- \frac {2}{\hbar} \int_ {R _ {i}} ^ {R _ {b}} \left\{2 \mu \left[ V \left(R _ {i}\right) - Q \right] \right\} ^ {1 / 2} d R\right). \tag {10}
$$

and $W _ { i }$ in Eq. (8) is estimated as unity, following the Greiner and Scheid de-excitation ansatz [46].

# A. Preformed cluster-decay model (PCM)

Within the preformed cluster-decay model (PCM), the half-life $T _ { 1 / 2 }$ (and decay constant $\lambda$ ) is usually expressed in terms of the penetration probability $P$ , and preformation probability $P _ { 0 }$ as,

$$
T _ {1 / 2} = \frac {\ln 2}{\lambda}, \quad \lambda = \nu_ {0} P _ {0} P. \tag {11}
$$

The assault frequency $\nu _ { 0 }$ has nearly constant value of $1 0 ^ { 2 1 } ~ \mathrm { s } ^ { - 1 }$ and can be calculated as

$$
\nu_ {0} = \frac {\text {v e l o c i t y}}{R _ {0}} = \frac {\sqrt {2 E _ {c} / \mu}}{R _ {0}}, \tag {12}
$$

where $R _ { 0 }$ symbolises the radius of the parent nucleus and $E _ { c }$ is the kinetic energy of the emitted cluster. The Q-values are calculated from the experimental binding energies data [43] using the expression

$$
Q = \left(B E _ {d} + B E _ {c}\right) - B E _ {p}, \tag {13}
$$

where $B E _ { p }$ , $B E _ { d }$ and $B E _ { c }$ are the binding energies of the parent, daughter nuclei and the emitted cluster respectively.

As a result, we have studied the relationship among various theoretically established properties/factors that influences cluster preformation such as the cluster mass $A _ { c }$ [47], mass and charge asymmetries $\eta _ { A } ~ = ~ ( A _ { d } -$ $A _ { c } ) / ( A _ { d } + A _ { c } )$ and $\eta _ { Z } = ( Z _ { d } - Z _ { c } ) / ( Z _ { d } + Z _ { c } )$ [47], the relative separation between the centers of the fragments $r _ { B } = 1 . 2 ( A _ { c } ^ { 1 / 3 } { + } A _ { d } ^ { 1 / 3 } )$ [48, 49] and the Q-value [50]. Thus, the newly proposed $P _ { 0 }$ formula [24] is of the form

$$
\log P _ {0} = - \frac {a A _ {c} \eta_ {A}}{r _ {B}} - Z _ {c} \eta_ {Z} + b Q + c. \tag {14}
$$

Here $a$ , $b$ and $c$ are the fitting parameters in Table I. A thorough and intuitive analysis of the third term on the right-hand side of Eq. (14) reveals the fractional amount of the decay energy contributed during the cluster preformation process. Thus a narrow bridge linking the contributions of the decay energy is constructed via the new $P _ { 0 }$ formula. Thus, the Q-value is presented in terms of its disbursement in the kinematics of cluster emission as,

$$
Q = \overbrace {\underbrace {b Q} _ {\text {e n e r g y}} + \underbrace {\kappa \sqrt {Q}} _ {\text {e n e r g y}}} ^ {E _ {c}} + \underbrace {E _ {d}} _ {\text {r e c o i l}} \tag {15}
$$

where the $\kappa \sqrt { Q }$ is the energy contributed in cluster emission. Further, the kinetic energy of the emitted cluster of Gupta et al. [47] is simplified as

$$
E _ {c} = \frac {A _ {d}}{A} Q = b Q + \kappa \sqrt {Q}, \tag {16}
$$

which yields

$$
\kappa = \sqrt {Q} \left(\frac {A _ {d}}{A} - b\right). \tag {17}
$$

The quantity $\kappa$ in Eq.(17) refers to the tunneling factor. The newly derived expressions in Eq.s (14)-(17) are analysed and explained in section III.

# III. CALCULATIONS AND DISCUSSIONS

In the context of heavy fragment nuclear decay (otherwise called cluster radioactivity), the parent nucleus having mass $A$ undergoes a spontaneous disintegration in which two separate fragments (daughter nucleus and the emitted cluster with masses $A _ { d }$ and $A _ { c }$ respectively) are formed. The mass asymmetry between these fragments is expressed as [51, 52]

$$
\eta_ {A} = \frac {A _ {d} - A _ {c}}{A _ {d} + A _ {c}} = 1 - \frac {2 A _ {c}}{A}. \tag {18}
$$

It is worth noting that for cluster decays, $0 . 6 0 \leq \eta _ { A } \leq$ 0.90 whereas $0 . 9 2 \leq \eta _ { A } \leq 0 . 9 7$ in alpha decay and $\eta _ { A } \leq$ 0.5 in fission studies [51]. Interestingly, all $\eta _ { A }$ values of the considered reaction systems are found within the established range for cluster decays as shown in the last Column of Table II.

Fig. 1 displays the variation of the preformation probability and penetration probability (in logarithmic scale) as a function of the mass asymmetry of the parent nuclei (ηA). It is worth noting that the preformation probability ( $P _ { 0 }$ ) and penetration probability ( $P$ ) are moderately model-dependent quantities. The calculated $P _ { 0 }$ values from Eq. (14) and the actual values are given in Column 6 of Table III. The upper panel of the figure shows the preformation of (a) $^ { 1 4 } \mathrm { C }$ cluster emission from different parent nuclei. From the figure, a slight drop is noticed in the magnitude of $P _ { 0 }$ between $^ { 2 2 1 } \mathrm { F r }$ (yielding 207Tl $N _ { d } = 1 2 6 , Z _ { d } = 8 1$ daughter) and $^ { 2 2 3 }$ Ac that yields 209Bi of $N _ { d } = 1 2 6 , Z _ { d } = 8 3$ . Thus, the small dip can be correlated with the neutron magic shell closure. However, the effect of an enhanced clusterization is visible as $P _ { 0 }$ increases drastically for an odd-A isotope of larger $\eta _ { A }$ i.e $^ { 2 2 5 }$ Ac resulting in the formation of daughters (with $N _ { d } = 1 2 8$ ) having two loosely bonded neutrons above the shell, taking part in the cluster formation process. Nonetheless, this effect may not be so apparent in medium-mass nuclei [53]. The usual trend is maintained with increasing mass asymmetry. A closer look at the figure suggests that pairing plays a vital role in cluster preformation and even-even nuclei may face less structural hindrance as compared to those from odd-parents. Details of the correlation of ground state spin (in terms of paired neutrons and orbital filling) and its effect on preformation can be found in Ref. [54].

Fig 1 (b) illustrates the effect of pairing correlation between the even-even and odd-A parent Uranium isotopic chain with each following a similar trend. As the

considered nuclei are laying at and/or near the $\beta -$ stable region of the nuclear chart, hence the BCS approach [34] is reasonable to predict the appropriate pairing effect, and it can be expected that the prediction will be not changed by adopting more appropriate approach such as Bogoliubov transformation [44]. The lower panel of the figure shows the profile of the penetration probability for (c) different nuclei and (d) $^ { 2 3 2 }$ U isotopes. In both cases, it is obvious that the penetration probability of systems is not merely influenced by their masses but also, by the collective nature of the daughters formed. Hence, the dip formed at $^ { 2 2 3 }$ Ac and $^ { 2 3 4 }$ U is illustrative of the proximity to a magic proton number of daughter $N _ { d }$ produced as explained earlier. The small variation in the M3Y and R3Y predictions can be attributed to the difference in their individual barrier properties.

The anatomy of the three-step barrier penetration process is further typified in Fig. 2. As a representative sample, the figure shows the total interaction potential of $\mathrm { ^ { 2 3 4 } U  ^ { 2 0 6 } H g + ^ { 2 8 } M g }$ as a function of the internuclear distance between the decaying fragments. Prior to the decay process, the emitted cluster $^ { 2 8 }$ Mg (green circle) is assumed to pre-exist within the $^ { 2 3 4 }$ U -parent nuclei (red circle). After the quantum tunneling process, a necklength $\Delta \mathrm { R }$ is formed between the decay fragments (the emitted cluster $^ { 2 8 }$ Mg and $^ { 2 0 5 }$ Hg-daughter nucleus (Pink colour). The black dash-lines and black solid lines are used to depict the three-step barrier penetration process for M3Y and R3Y respectively. The process begins at point $R _ { a }$ whose corresponding potential is $V ( R _ { a } )$ (also known as the effective Q-value, $Q _ { e f f }$ ), usually higher than the $Q$ -value. Thereafter, de-excitation begins at point $R _ { i }$ which is primarily decided by the peculiarity and profile of the employed NN potential. For R3Y, $R _ { i }$ is further extended due to its repulsive nature as compared to its cognate M3Y NN potential. In each case, the de-excitation probability $W _ { i } = 1$ , following the Greiner and Scheid’s ansatz [46] and then penetration process continues until it reaches point $R _ { b }$ having a potential $V ( R _ { b } ) = Q$ .

The difference between $V ( R _ { a } )$ and the barrier height $V _ { B }$ basically provides the barrier lowering parameter $\Delta V _ { B }$ , which gives a vivid picture of the behaviour of the microscopic R3Y and phenomenological M3Y interaction. Fig. 3 (a) and (b) illustrates the variation of the barrier lowering $\Delta V _ { B }$ for $^ { 1 4 } C$ decay from various actinides and $^ { A } U \ \to ^ { 2 8 } \ M g \ + ^ { A - 2 8 } \ H g$ respectively, with respect to the mass (and neutron) number of their respective parent nuclei. The shaded portion in the figures depicts the difference between the $\Delta V _ { B } ^ { M 3 Y }$ (red solid square) and $\Delta V _ { B } ^ { R 3 Y }$ (blue solid circle). A close assessment of both figures reveals that the M3Y and R3Y potentials manifest similar trend, although at different magnitudes. This is due to the repulsive nature of the R3Y interaction potential, as earlier mentioned. Particularly, in Fig. 3(a), $\Delta V _ { B }$ is found to decrease significantly with each increase in the mass of the considered actinides emitting the same ( $^ { 1 4 }$ C) cluster. A similar phenomenon is no-

![](images/72918c60a0df066a0f152d0f870af913a2cfd7a0c123fa4f35df434a4ece4546.jpg)

![](images/9f143a70b8429becf76ec3a9f27a6adb5075c8bf3b960e519cfac42d59d88ea8.jpg)  
FIG. 1. The calculated preformation probability $^ { 1 4 } \mathrm { C }$ emission from different actinides and panels (b) $P _ { 0 }$ (in logarithmic scale) versus the mass asymmetry $^ { 2 8 }$ Mg emission from 232−236U isotopes. The profiles of the penetration $2 3 2 - 2 3 6$ $\eta A$ in Eq. (18) for (a) probability $P$ (in logarithmic scale) for both cases are given in panels (c) and (d) respectively.

TABLE II. The penetrability, decay half-lives and mass asymmetry of various actinides using the M3Y and R3Y NN potentials. The Q-values are calculated from the experimental binding energies given in a recent mass table [43]. The experimentally observed half-lives are taken from Ref. [3].   

<table><tr><td rowspan="2">Parents nuclei</td><td rowspan="2">Emitted cluster</td><td rowspan="2">Daughters nuclei</td><td rowspan="2">Q-value (MeV)</td><td colspan="2">Penetrability</td><td colspan="3">log10T1/2</td><td rowspan="2">ηA</td></tr><tr><td>PM3Y</td><td>PR3Y</td><td>Texp1/2</td><td>TM3Y1/2</td><td>TR3Y1/2</td></tr><tr><td>114Ba</td><td>12C</td><td>102Sn</td><td>19.02</td><td>1.08×10-19</td><td>3.08×10-18</td><td>&gt;4.10</td><td>11.90</td><td>10.44</td><td>0.789</td></tr><tr><td>221Fr</td><td>14C</td><td>207Tl</td><td>31.29</td><td>4.11×10-20</td><td>8.04×10-20</td><td>14.52</td><td>14.90</td><td>14.61</td><td>0.873</td></tr><tr><td>223Ac</td><td>14C</td><td>209Bi</td><td>33.06</td><td>5.28×10-19</td><td>6.05×10-19</td><td>12.6</td><td>13.57</td><td>13.51</td><td>0.874</td></tr><tr><td>225Ac</td><td>14C</td><td>211Bi</td><td>30.48</td><td>1.82×10-22</td><td>3.84×10-22</td><td>17.16</td><td>17.34</td><td>20.16</td><td>0.876</td></tr><tr><td>226Th</td><td>14C</td><td>212Po</td><td>30.55</td><td>5.21×10-23</td><td>1.39×10-22</td><td>&gt;15.3</td><td>15.95</td><td>15.53</td><td>0.876</td></tr><tr><td>230Th</td><td>24Ne</td><td>206Hg</td><td>57.76</td><td>2.85×10-22</td><td>2.98×10-21</td><td>24.61</td><td>24.91</td><td>23.89</td><td>0.791</td></tr><tr><td>231Pa</td><td>24Ne</td><td>207Tl</td><td>60.41</td><td>2.08×10-20</td><td>8.48×10-20</td><td>23.23</td><td>23.62</td><td>23.01</td><td>0.792</td></tr><tr><td>232U</td><td>28Mg</td><td>204Hg</td><td>74.32</td><td>1.61×10-20</td><td>7.89×10-19</td><td>&gt;22.26</td><td>25.58</td><td>23.89</td><td>0.759</td></tr><tr><td>233U</td><td>28Mg</td><td>205Hg</td><td>74.23</td><td>1.62×10-20</td><td>5.83×10-19</td><td>&gt;27.59</td><td>29.24</td><td>27.69</td><td>0.760</td></tr><tr><td>234U</td><td>28Mg</td><td>206Hg</td><td>74.11</td><td>1.53×10-20</td><td>4.01×10-19</td><td>25.14</td><td>25.64</td><td>24.23</td><td>0.761</td></tr><tr><td>235U</td><td>28Mg</td><td>207Hg</td><td>72.43</td><td>5.13×10-22</td><td>1.77×10-20</td><td>&gt;28.09</td><td>30.98</td><td>29.44</td><td>0.762</td></tr><tr><td>235U</td><td>29Mg</td><td>206Hg</td><td>72.48</td><td>4.79×10-22</td><td>2.55×10-21</td><td>&gt;28.09</td><td>28.55</td><td>27.82</td><td>0.753</td></tr><tr><td>236U</td><td>28Mg</td><td>208Hg</td><td>70.73</td><td>1.38×10-23</td><td>6.18×10-22</td><td>27.58</td><td>29.11</td><td>27.46</td><td>0.763</td></tr><tr><td>236U</td><td>30Mg</td><td>206Hg</td><td>72.27</td><td>2.11×10-22</td><td>3.70×10-21</td><td>27.58</td><td>29.22</td><td>27.97</td><td>0.746</td></tr><tr><td>238U</td><td>34Si</td><td>204Pt</td><td>85.01</td><td>8.95×10-22</td><td>1.29×10-20</td><td>29.04</td><td>30.63</td><td>29.47</td><td>0.714</td></tr><tr><td>237Np</td><td>30Mg</td><td>207Tl</td><td>74.79</td><td>5.70×10-21</td><td>4.72×10-20</td><td>&gt;26.93</td><td>27.91</td><td>26.99</td><td>0.747</td></tr><tr><td>238Pu</td><td>32Si</td><td>206Hg</td><td>91.19</td><td>1.19×10-18</td><td>6.51×10-18</td><td>25.27</td><td>25.62</td><td>24.88</td><td>0.731</td></tr><tr><td>240Pu</td><td>34Si</td><td>206Hg</td><td>91.06</td><td>8.74×10-19</td><td>1.83×10-18</td><td>&gt;25.52</td><td>27.07</td><td>26.75</td><td>0.717</td></tr><tr><td>241Am</td><td>34Si</td><td>207Tl</td><td>93.96</td><td>1.46×10-17</td><td>1.17×10-17</td><td>&gt;22.71</td><td>25.61</td><td>25.71</td><td>0.718</td></tr><tr><td>252Cf</td><td>46Ar</td><td>206Hg</td><td>126.75</td><td>6.02×10-15</td><td>2.79×10-16</td><td>&gt;15.89</td><td>26.81</td><td>28.14</td><td>0.635</td></tr><tr><td>252Cf</td><td>48Ca</td><td>204Pt</td><td>137.97</td><td>3.68×10-15</td><td>3.68×10-14</td><td>&gt;15.89</td><td>26.81</td><td>25.81</td><td>0.619</td></tr><tr><td>252Cf</td><td>50Ca</td><td>202Pt</td><td>138.32</td><td>7.14×10-15</td><td>6.92×10-16</td><td>&gt;15.89</td><td>27.03</td><td>28.05</td><td>0.603</td></tr></table>

TABLE III. The predicted driving potential ${ d _ { p o t } } = V ( R _ { a } ) - Q$ from M3Y and R3Y interactions are given in columns (2-5). The preformation properties calculated from a newly derived set of Eqs. (14) - (17) are given in columns (6-11).   

<table><tr><td rowspan="2">Reaction systems</td><td colspan="4">Barrier Properties</td><td colspan="6">Preformation Properties</td></tr><tr><td>\(V^{M3Y}(R_a)\) (MeV)</td><td>\(d_{pot}^{M3Y}\) (MeV)</td><td>\(V^{R3Y}(R_a)\) (MeV)</td><td>\(d_{pot}^{R3Y}\) (MeV)</td><td>\(P_0\) Eq. (14)</td><td>b.Q (MeV)</td><td>κ</td><td>\(\kappa\sqrt{Q}\) (MeV)</td><td>\(E_c\) (MeV)</td><td>\(E_d\) (MeV)</td></tr><tr><td>\({}^{114}\mathrm{Ba}\rightarrow{}^{12}\mathrm{C}+{}^{102}\mathrm{Sn}\)</td><td>32.37</td><td>13.34</td><td>29.56</td><td>10.54</td><td>\(2.61\times 10^{-15}\)</td><td>2.17</td><td>3.40</td><td>14.85</td><td>17.02</td><td>2.00</td></tr><tr><td>\({}^{221}\mathrm{Fr}\rightarrow{}^{14}\mathrm{C}+{}^{207}\mathrm{Tl}\)</td><td>42.49</td><td>11.20</td><td>36.73</td><td>5.44</td><td>\(7.32\times 10^{-18}\)</td><td>3.74</td><td>4.57</td><td>25.57</td><td>29.31</td><td>1.98</td></tr><tr><td>\({}^{223}\mathrm{Ac}\rightarrow{}^{14}\mathrm{C}+{}^{209}\mathrm{Bi}\)</td><td>43.63</td><td>10.57</td><td>37.82</td><td>4.76</td><td>\(1.19\times 10^{-17}\)</td><td>3.95</td><td>4.70</td><td>27.04</td><td>30.99</td><td>2.08</td></tr><tr><td>\({}^{225}\mathrm{Ac}\rightarrow{}^{14}\mathrm{C}+{}^{211}\mathrm{Bi}\)</td><td>42.38</td><td>11.91</td><td>36.38</td><td>5.90</td><td>\(4.40\times 10^{-21}\)</td><td>3.64</td><td>4.52</td><td>24.94</td><td>28.58</td><td>1.90</td></tr><tr><td>\({}^{226}\mathrm{Th}\rightarrow{}^{14}\mathrm{C}+{}^{212}\mathrm{Po}\)</td><td>42.87</td><td>12.32</td><td>36.82</td><td>6.27</td><td>\(5.17\times 10^{-16}\)</td><td>3.49</td><td>4.55</td><td>25.16</td><td>28.66</td><td>1.89</td></tr><tr><td>\({}^{230}\mathrm{Th}\rightarrow{}^{24}\mathrm{Ne}+{}^{206}\mathrm{Hg}\)</td><td>75.30</td><td>17.54</td><td>66.43</td><td>8.67</td><td>\(1.00\times 10^{-25}\)</td><td>6.60</td><td>5.94</td><td>45.13</td><td>51.73</td><td>6.03</td></tr><tr><td>\({}^{231}\mathrm{Pa}\rightarrow{}^{24}\mathrm{Ne}+{}^{207}\mathrm{Tl}\)</td><td>76.40</td><td>15.99</td><td>67.52</td><td>7.11</td><td>\(2.61\times 10^{-26}\)</td><td>7.22</td><td>6.04</td><td>46.92</td><td>54.13</td><td>6.28</td></tr><tr><td>\({}^{232}\mathrm{U}\rightarrow{}^{28}\mathrm{Mg}+{}^{204}\mathrm{Hg}\)</td><td>95.30</td><td>20.98</td><td>85.26</td><td>10.94</td><td>\(3.64\times 10^{-28}\)</td><td>8.49</td><td>6.60</td><td>56.86</td><td>65.35</td><td>8.97</td></tr><tr><td>\({}^{233}\mathrm{U}\rightarrow{}^{28}\mathrm{Mg}+{}^{205}\mathrm{Hg}\)</td><td>94.74</td><td>20.51</td><td>84.64</td><td>10.42</td><td>\(7.85\times 10^{-32}\)</td><td>8.87</td><td>6.55</td><td>56.44</td><td>65.31</td><td>8.92</td></tr><tr><td>\({}^{234}\mathrm{U}\rightarrow{}^{28}\mathrm{Mg}+{}^{206}\mathrm{Hg}\)</td><td>94.18</td><td>20.07</td><td>84.02</td><td>9.90</td><td>\(4.02\times 10^{-29}\)</td><td>8.47</td><td>6.59</td><td>56.77</td><td>65.24</td><td>8.87</td></tr><tr><td>\({}^{235}\mathrm{U}\rightarrow{}^{28}\mathrm{Mg}+{}^{207}\mathrm{Hg}\)</td><td>93.35</td><td>20.93</td><td>83.04</td><td>10.62</td><td>\(4.59\times 10^{-32}\)</td><td>8.65</td><td>6.48</td><td>55.15</td><td>63.80</td><td>8.63</td></tr><tr><td>\({}^{235}\mathrm{U}\rightarrow{}^{29}\mathrm{Mg}+{}^{206}\mathrm{Hg}\)</td><td>91.33</td><td>18.86</td><td>80.32</td><td>7.84</td><td>\(1.36\times 10^{-29}\)</td><td>8.66</td><td>6.45</td><td>54.88</td><td>63.53</td><td>8.94</td></tr><tr><td>\({}^{236}\mathrm{U}\rightarrow{}^{28}\mathrm{Mg}+{}^{208}\mathrm{Hg}\)</td><td>92.52</td><td>21.79</td><td>82.06</td><td>11.33</td><td>\(1.30\times 10^{-28}\)</td><td>8.08</td><td>6.45</td><td>54.26</td><td>62.34</td><td>8.39</td></tr><tr><td>\({}^{236}\mathrm{U}\rightarrow{}^{30}\mathrm{Mg}+{}^{206}\mathrm{Hg}\)</td><td>92.44</td><td>20.17</td><td>81.56</td><td>9.29</td><td>\(6.72\times 10^{-30}\)</td><td>8.26</td><td>6.45</td><td>54.83</td><td>63.08</td><td>9.19</td></tr><tr><td>\({}^{238}\mathrm{U}\rightarrow{}^{34}\mathrm{Si}+{}^{204}\mathrm{Pt}\)</td><td>106.25</td><td>21.24</td><td>93.90</td><td>8.89</td><td>\(6.03\times 10^{-32}\)</td><td>9.71</td><td>6.85</td><td>63.15</td><td>72.87</td><td>12.14</td></tr><tr><td>\({}^{237}\mathrm{Np}\rightarrow{}^{30}\mathrm{Mg}+{}^{207}\mathrm{Tl}\)</td><td>93.76</td><td>18.97</td><td>82.84</td><td>8.05</td><td>\(5.02\times 10^{-30}\)</td><td>8.93</td><td>6.52</td><td>56.39</td><td>65.32</td><td>9.47</td></tr><tr><td>\({}^{238}\mathrm{Pu}\rightarrow{}^{32}\mathrm{Si}+{}^{206}\mathrm{Hg}\)</td><td>110.02</td><td>18.83</td><td>98.48</td><td>7.30</td><td>\(4.40\times 10^{-30}\)</td><td>10.42</td><td>7.17</td><td>68.51</td><td>78.93</td><td>12.26</td></tr><tr><td>\({}^{240}\mathrm{Pu}\rightarrow{}^{34}\mathrm{Si}+{}^{206}\mathrm{Hg}\)</td><td>109.32</td><td>18.26</td><td>96.91</td><td>5.84</td><td>\(2.15\times 10^{-31}\)</td><td>10.41</td><td>7.10</td><td>67.76</td><td>78.16</td><td>12.90</td></tr><tr><td>\({}^{241}\mathrm{Am}\rightarrow{}^{34}\mathrm{Si}+{}^{207}\mathrm{Tl}\)</td><td>110.85</td><td>16.89</td><td>98.39</td><td>4.43</td><td>\(3.68\times 10^{-31}\)</td><td>11.22</td><td>7.17</td><td>69.48</td><td>80.70</td><td>13.26</td></tr><tr><td>\({}^{252}\mathrm{Cf}\rightarrow{}^{46}\mathrm{Ar}+{}^{206}\mathrm{Hg}\)</td><td>142.31</td><td>15.56</td><td>127.19</td><td>0.44</td><td>\(5.77\times 10^{-35}\)</td><td>14.48</td><td>7.92</td><td>89.13</td><td>103.61</td><td>23.14</td></tr><tr><td>\({}^{252}\mathrm{Cf}\rightarrow{}^{48}\mathrm{Ca}+{}^{204}\mathrm{Pt}\)</td><td>158.79</td><td>20.82</td><td>143.59</td><td>5.62</td><td>\(9.13\times 10^{-35}\)</td><td>15.77</td><td>8.17</td><td>95.92</td><td>111.69</td><td>26.28</td></tr><tr><td>\({}^{252}\mathrm{Cf}\rightarrow{}^{50}\mathrm{Ca}+{}^{202}\mathrm{Pt}\)</td><td>156.11</td><td>17.79</td><td>139.07</td><td>0.76</td><td>\(2.89\times 10^{-35}\)</td><td>15.81</td><td>8.08</td><td>95.07</td><td>110.87</td><td>27.44</td></tr></table>

![](images/64950fb7c09e7fb684205ae7c38963528deb7d191e358cf860e3d66b9fc38510.jpg)  
FIG. 2. The total interaction potential of $^ { 2 3 4 } \mathrm { U  ^ { 2 0 6 } H g \ : + }$ $^ { 2 8 }$ Mg as a function of the mass-center distance between the decaying fragments (R). Prior to the decay process, the emitted cluster $^ { 2 8 }$ Mg (green circle) is assumed to pre-exist within the 234U -parent nuclei (red circle). After the quantum tunneling process, a neck-length $\Delta \mathrm { R }$ is formed between the decay fragments (28Mg and $^ { 2 0 5 }$ Hg-daughter nucleus (Pink colour)). The black dash-lines and black solid lines are used to depict the three-step barrier penetration process for M3Y and R3Y respectively.

ticed in Fig 3(b). However, across the uranium ( $Z = 9 2$ ) isotopic chain, the decline in $\Delta V _ { B }$ is found to arise primarily from the increase in the neutron number (N). The M3Y and R3Y barrier properties within the PCM can be examined more closely by probing the driving potential $d _ { p o t } = V ( R _ { a } ) - Q$ . Usually, the $d _ { p o t }$ is influenced by the choice of interaction potential as well as the nature of the decaying parent nucleus and decay fragments (cluster and daughter nucleus). Fig. 3(c)-(d) depicts the profile of $d _ { p o t }$ as a function of the mass (and neutron number) of the parent nuclei for $^ { 1 4 } C$ decay from various actinides and $^ { A } U  ^ { 2 8 }$ $M g \mathrel { + } ^ { A - 2 8 } H g$ respectively. In Fig. 3(c), both M3Y and R3Y reproduced the deepest minima at $^ { 2 2 3 }$ Ac corresponding to $^ { 2 0 9 }$ Bi $Z = 8 3 , N = 1 2 6$ ) daughter nucleus i.e just above the proton shell closure and at the neutron shell closure. Thereafter, the driving potential rises with each increase in the mass number of the parent nuclei. Also, a similar occurrence is found in Fig. 3(d) where the minima is formed at $N = 1 4 2$ corresponding to 206Hg ( $Z = 8 0 , N = 1 2 6 ,$ ) i.e at neutron shell closure along the isotopic chain.

As one examines the shaded portion of Fig. 3(a)-3(d), it is salient to note that the difference between the M3Y and R3Y predictions reduces successively for parent nuclei with lower masses. Thus, we presume that the predic-

tions from the M3Y and R3Y may quantitatively agree for parent nuclei with relatively lower mass such that $\Delta V _ { B } ^ { M 3 Y } - \Delta V _ { B } ^ { R 3 Y } \approx 0$ . In other words, the relative difference in the M3Y and R3Y interactions could be mass region-dependent. We have recently shown [26] that a wider difference may ensue for studies involving heavy particle radioactivity (HPR).

Fig. 4 (a) and (b) depicts the logarithmic half-lives of different actinides emitting $^ { 1 4 } \mathrm { C }$ and AU →28 $M g + ^ { A - 2 8 }$ $H g$ . In both cases, the $\log _ { 1 0 } T _ { 1 / 2 }$ predictions of M3Y (red solid square) and R3Y (blue star) are in good agreement with the experimentally measured half-lives (black sphere) and the lower limit (black sphere with an upward arrow) for $^ { 2 2 6 }$ Th. As expected, the lowest minima is formed at the nearest double magic neighbour $^ { 2 2 3 }$ Ac having 209Bi ( $Z \ = \ 8 3 , N \ = \ 1 2 6 ,$ ) daughter nucleus in Fig. 4(a). It is worth noting that the precise experimental half-lives of most of the studied systems in Fig 4(b) are unavailable but the predictions here, especially for $N = 1 4 0$ are most probable since, by principle, the lowest minima is expected at 142, whose daughter is formed at the neutron magic number $N = 1 2 6$ . The half-lives of all the systems considered in this work are given in Columns 7 - 10 of Table II. In most cases, the predictions of the microscopic R3Y interaction, give a relatively closer agreement with the experiment [3]. Beside the effect of the neutron shell closures of the daughter nuclei, the $\log _ { 1 0 } T _ { 1 / 2 }$ values are generally lower for parent nuclei with even mass numbers, which is reminiscent of an odd-even staggering behaviour.

The third term of Eq. (14) is the fractional amount of the decay energy contributed during the cluster formation process only. The contribution of the Q-value to each stage of the kinematics of cluster emission is fully spelt out in Eq. (15) and thus, their qualitative estimate is given in Fig. 5 for $^ { A } U  ^ { 2 8 } \ M g  ^ { A - 2 8 } \ H g$ . Particularly, Fig. 5 typifies the share of energy participating in the cluster preformation of each reaction system as a function of the neutron number of the daughter nuclei. The weighted Q-value i.e. $b Q$ can only be influenced by the decay energy and parameter $b$ . For the sake of accuracy, the Q-values are calculated from the experimental binding energy data [43]. A detailed inspection of the figure shows that the magnitude of $b Q$ is all-time higher for odd-A nuclei as compared to their neighbouring even-even nuclei. This presupposes that the energy required for the preformation of nuclear clusters can be relatively higher for odd-A than those with even-even parents. This behaviour reflects the odd-even staggering effects originating from both pairing correlations as well as the blocking of particular orbitals by unpaired nucleons associated with 205Hg and 207Hg. Interestingly, this trend is repeated for all the systems under study in Table III and our observation corroborates with recent findings [55, 56].

Although none of the considered reaction systems yields a double magic daughter nucleus, it is apparent that the kinematics of their cluster emission is governed

![](images/25b9414354cc338f9c2736b4f42a6770bc88bd12a87b289863ea8d8264125ca4.jpg)

![](images/31d7dcac506918adacff882af3c25442236cc42c577a1057b2bfc41527c846b6.jpg)  
FIG. 3. Variation of the barrier lowering $\Delta V _ { B }$ for (a) $^ { 1 4 } C$ decay from various actinides and $( \mathrm { b } ) ^ { A } U  ^ { 2 8 } M g + ^ { A - 2 8 } H g$ . The profile of the driving potential $d _ { p o t } = V ( R _ { a } ) - Q$ for both cases are shown in (c) and (d) respectively.

![](images/ee97dfd87c69c824767fd3881de0a25b31c284c9c652954ac3a4800059201827.jpg)

![](images/51d85eefba625b67a5ec42efeb53ea7a73d379609de3c4c7a6aff90b0e2175bb.jpg)  
FIG. 4. Logarithmic half-lives of (a) different actinides emitting $^ { 1 4 } \mathrm { C }$ cluster and (b) Uranium isotopes emitting $^ { 2 8 }$ Mg clusters $^ { \prime A } U  ^ { 2 8 } M g + ^ { A - 2 8 } H g )$ .

by their proximity to the shell closure. A vivid picture of this fact is given in the footnote of Table I where the parameter $' c ^ { \prime }$ assumes a uniform fitting to either $N _ { d } \leq 1 2 6$ or $1 2 6 \leq N _ { d } \leq 1 2 8$ for all odd-A nuclei. The effect of parameter $' c ^ { \prime }$ is further revealed in Fig. 5(b) where $\kappa \sqrt { Q }$ (the energy required for the emission of a preformed cluster) is plotted as a function of the neutron number of the participating daughter nuclei. In the figure, a conspicuous minimal is formed at $N _ { d } = 1 2 5$ ( $N _ { d } \leq 1 2 6$ ) corresponding to a relatively low parameter $' c ^ { \prime }$ . In the same vein, at $N = 1 2 7$ , there is a nearly imperceptible bend

arising from the larger value of $' c ^ { \prime }$ since it is found within the range $1 2 6 \leq N _ { d } \leq 1 2 8$ . Thus, the mass of the parent nucleus as well as those of the decay fragment plays a decisive role in the tunnelling factor $\kappa$ . By definition, $\kappa$ is the fraction of the $Q$ -value required, just for the propagation of the preformed cluster. Its actual value is given in column 8 of Table III where it becomes evident that there is a direct proportionality between the quantity $\kappa$ and $b Q$ i.e $b Q$ increases with increasing value of $\kappa$ . This implies that there is a close correlation between the amount of energy contributed during cluster preformation and its tunnelling as portrayed in Eq. (15).

Fig. 5 (c) shows the variation of the recoil energy as a function of the neutron number of the daughter $N _ { d }$ . The recoil energy maintains a regular profile until it attains the neutron magic shell closure $N _ { d } = 1 2 6$ where a conspicuous shift is noticed in the isotopic chain. Again, this indicates the dominance of the shell effect. Detailed discussions on the shell closure effect as well as its correlation with the isotopic shift in charge radius and the single-particle energy levels can be found in Ref. [57]. A notable inference that can be drawn from the figure is that the recoil energy of a reaction system decreases as the mass of the corresponding daughter (and parent) nucleus increases along the isotopic chain (e.g. $A$ U $ ^ { 2 8 } \mathrm { M g } \ + ^ { A - 2 8 } \mathrm { H g } )$ ) in which the same cluster is emitted provided that no constituent (proton and neutron number) of the daughter formed is a magic number.On the other hand, a careful inspection of the last column of Table III shows that the recoil energy increases propor-

![](images/a54ccd212adc91ff6773e4a64abb35573f446972511093eafc16114093de55f7.jpg)  
FIG. 5. Variation of the preformation properties: (a) weighted Q-values of various Uranium isotopes as a function of the neutron number of the daughters formed from the emission of $^ { 2 8 }$ Mg clusters respectively, (b) cluster emission energy and (c) recoil energy of the daughter nuclei.

tionately for the reaction systems with the same daughter nuclei but of different clusters and parent nuclei (with increasing size/mass). For example

$\mathrm { ^ { 2 2 1 } F r \mathrm { \to ^ { 1 4 } C + ^ { 2 0 7 } T l } }$ yields $E _ { d } = 1 . 9 8$ MeV, $\mathrm { ^ { 2 3 1 } P a } \mathrm {  ^ { 2 4 } N e  ^ { 2 0 7 } T l }$ yields $E _ { d } = 6 . 2 8$ MeV, $\mathrm { ^ { 2 3 7 } N p \mathrm {  ^ { 3 0 } M g + ^ { 2 0 7 } T l } }$ yields $E _ { d } = 9 . 4 7$ MeV, $\mathrm { ^ { 2 4 1 } A m {  } ^ { 3 4 } S i + ^ { 2 0 7 } T l }$ yields $E _ { d } = 1 3 . 2 6$ MeV.

In other words, $E _ { d }$ increases proportionately with systems yielding the same daughter nucleus but of increasing cluster masses if and only if no constituent of the daughter formed is a magic number. This observation is also true for the emission of clusters of different masses from the same parent nucleus. For example:   
$\mathrm { ^ { 2 3 8 } P u \mathrm {  ^ { 3 2 } S i + ^ { 2 0 6 } H g } }$ yields $E _ { d } = 1 2 . 2 6$ MeV,   
$\mathrm { ^ { 2 4 0 } P u \mathrm { \to ^ { 3 4 } S i + ^ { 2 0 6 } H g } }$ yields $E _ { d } = 1 2 . 9 0$ MeV,

provided that the daughter formed are non-double magic nuclei. We hope that the analysis of the recoil energy in cluster emissions will be informative for meaningful

extrapolations in the (synthesis of the) superheavy region since recent studies have shown that cluster decay could be a dominant decay mode in the superheavy region [9, 10, 58, 59].

# IV. SUMMARY AND CONCLUSIONS

The dynamics of cluster emission are studied within the relativistic mean-field (RMF) formalism using the NL3∗ parameter set. Assuming that a cluster pre-exists as an entity within the parent nucleus, we have applied our newly developed cluster preformation $P _ { 0 }$ formula for radioactive nuclei decaying to yield daughters in the vicinity of double magic shell closure. The $P _ { 0 }$ formula opens a novel route for remodelling the $Q -$ value such that it gives a quantitative estimate of the energy contributed during the cluster preformation process, transmission energy of the preformed clusters and the recoil energy of the daughters formed. Besides, to ensure the applicability of the formula, we have employed the wellknown M3Y and microscopic-based R3Y NN potentials for the analysis. Despite the difference in the barrier properties of these NN potentials, our result reveals that with the inclusion of the new $P _ { 0 }$ formula, the calculated half-lives are in good agreement with the experimentally measured half-lives. We have also demonstrated that the kinematics of cluster emission is governed by the proximity of the corresponding daughter nuclei to the shell closure. The pairing correlation and the odd-even staggering effect arising from the unpaired neutrons are appraised. A detailed analysis of the recoil energy that can be extrapolated for the forthcoming synthesis of superheavy nuclei is also discussed. However, in principle, the shapes degree of freedom of each of the participating nuclei plays a crucial role in its description. This is an interesting future problem that will be given due consideration.

# ACKNOWLEDGMENTS

The authors would like to acknowledge the support from the Fundamental Research Grant Scheme (FRGS) under the grant number FRGS/1/2019/STG02/UNIMAP/02/2 from the Ministry of Education Malaysia stipulated with the Institute of Engineering Mathematics (IMK), UniMAP as the beholder. This work was supported by FOSTECT Project Code: FOSTECT.2019B.04, FAPESP Project Nos. 2017/05660-0, and Science Engineering Research Board (SERB), File No. CRG/2021/001229.

[1] A. Sandulescu, D. N. Poenaru, and W. Greiner, Sov. J. Part. Nucl. 11, 528 (1980).   
[2] H. J. Rose and G. A. Jones, Nature 307, 245 (1984).   
[3] R. Bonetti and A. Guglielmetti, Rom. Rep. Phys. 59, 301 (2007).   
[4] V. Yu. Denisov, Phys. Rev. C 88, 044608 (2013).   
[5] N. Jain, R. Kumar and M. Bhuyan, Nucl. Phys. A 1019, 122379 (2022).   
[6] D. Pathak, N. Singh, H. Kaur and S. R. Jain, J. Phys. G: Nucl. Part. Phys. 48, 075103 (2021).   
[7] R. G. Lovas, R. J. Liotta, A. Insolia, K. Varga, and D. S. Delion, Phys. Rep. 294, 265 (1998).   
[8] M. Warda and L. M. Robledo, Phys. Rev. C 84, 044608 (2011).   
[9] M. Warda, A. Zdeb, and L. M. Robledo, Phys. Rev. C 98, 041602(R) (2018).   
[10] Z. Matheson, S. A. Giuliani, W. Nazarewicz, J. Sadhukhan, and N. Schunck, Phys. Rev. C 99, 041304(R) (2019).   
[11] J. Maruhn and W. Greiner, Phys. Rev. Lett. 32, 548 (1974).   
[12] H. J. Fink, J. Maruhn, W. Scheid, and W. Greiner, Z. Phys. 268, 321 (1974).   
[13] D. N. Poenaru, M. Iva¸scu, A. Sandulescu, and Walter Greiner, Phys. Rev. C 32, 572 (1985).   
[14] D. N. Poenaru , W. Greiner , K. Depta , M. Ivascu , D. Mazilu and A. Sandulescu, At. Data Nucl. Data Tables 34, 423 (1986).   
[15] D. N. Poenaru, Y. Nagame, R. A. Gherghescu, and W. Greiner, Phys. Rev. C 65, 054308 (2002).   
[16] D. N. Poenaru and W. Greiner, C. Beck (Ed.) Clusters in Nuclei. Volume 1 Lect. Not. Phys. 818, (Springer, Heidelberg, 2010).   
[17] R. K. Gupta, in Proceedings of the Fifth International Conference on Nuclear Reaction Mechanisms, edited by E. Gadioli (Ricerca Scientifica ed Educazione Permanente, Milan, 1988), p. 416.   
[18] J. T. Majekodunmi, M. Bhuyan, D. Jain, K. Anwar, N. Abdullah, and R. Kumar, Phys. Rev. C 105, 044617 (2022)   
[19] W. A. Yahya and T. T. Ibrahim, Eur. Phys. J. A 58, 48 (2022).   
[20] T. M. Joshua, N. Jain, R. Kumar, K. Anwar, N. Abdullah, and M. Bhuyan, Foundations, 2, 85-104 (2022).   
[21] S. M. S. Ahmed, R. Yahaya, S. Radiman, M. S. Yasir, H. A. Kassim, and M. U. Khandaker, Eur. Phys. J. A 51, 13 (2015).   
[22] R. Blendowske and H. Walliser, Phys. Rev. Lett. 61, 1930 (1988).   
[23] K. P. Santhosh and T. A. Jose, Phys. Rev. C 104, 064604 (2021).   
[24] J. T. Majekodunmi, M. Bhuyan, K. Anwar, N. Abdullah and R. Kumar, Chin. Phys. C 47, 074106 (2023).   
[25] J. T. Majekodunmi, T. Y. Alsultan, K. Anwar, Raj Kumar, and M. Bhuyan. Nucl. Phys. A 1034, 122652 (2023).   
[26] J. T. Majekodunmi, M. Bhuyan, K. Anwar, and R. Kumar, http://arxiv.org/abs/2305.05613 Euro Phys. Lett., submitted (2023).   
[27] R. F. Casten, Phys. Rev. Lett. 54, 1991 (1985).   
[28] D. Ni, Z. Ren, Nucl. Phys. A 828, 348 (2009).

[29] J. Blocki, J. Randrup, W. J. Swiatecki, and C. F. Tsang, Ann. Phys. (N.Y.) 105, 427 (1977).   
[30] R. Kumar, Phys. Rev. C 86, 044612 (2012).   
[31] G. R. Satchler and W. G. Love, Phys. Rep. 55, 183 (1979).   
[32] J. Boguta and A. R. Bodmer, Nucl. Phys. A 292, 413 (1977).   
[33] P. -G. Reinhard, Rep. Prog. Phys. 52, 439 (1989).   
[34] Y. K. Gambhir, P. Ring, and A. Thimet, Ann. Phys. 198, 132 (1990).   
[35] B. D. Serot and J. D. Walecka, in Advances in Nuclear Physics, edited by J. W. Negele and E. Vogt (Plenum, New York, 1986), Vol. 16, p. 1.   
[36] G. A. Lalazissis, S. Karatzikos, R. Fossion, D. Pena Arteaga, A. V. Afanasjev, and P. Ring, Phys. Lett. B 671, 36 (2009).   
[37] S. Biswal, M. A. El Sheikh, N. Biswal, N. Yusof, H. Kassim, S. K. Patra, and M. Bhuyan, Nucl. Phys. A 1004, 122042 (2020).   
[38] N. Itagaki, A. Afanasjev, and D. Ray, Phys. Rev. C 101, 034304 (2020).   
[39] M. Panigrahi, R. N. Panda, M. Bhuyan, and S. K. Patra, Can. Jour. of Phys. 99, 412 (2021)   
[40] J. T. Majekodunmi, S. Rana, N. Jain, K. Anwar, N. Abdullah, R. Kumar, and M. Bhuyan. Relativistic R3Y Nucleon–Nucleon Potential: Decay Characteristics of Ba Isotope Within the Preformed Cluster Decay Approach, edited by S. K. Sethi and S. Gao, XZ. (In Intelligent Systems Springer, Singapore, 2022.) Vol. 431, p. 135-142.   
[41] S. K. Biswal, S. K. Singh, M. Bhuyan and S. K. Patra, Braz. J. Phys., 45, 347 (2015).   
[42] B. B. Sahu, S. K. Singh, M. Bhuyan, S. K. Biswal and S. K. Patra, Phys. Rev. C 89, 034614 (2014).   
[43] M. Wang, W. Huang, F. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003 (2021).   
[44] P. Ring, Prog. Part. Nucl. Phys. 37, 193 (1996).   
[45] A. Singh, A. Shukla, and M. K. Gaidarov, J. Phys. G: Nucl. Part. Phys, 49, 025101 (2021).   
[46] M. Greiner and W. Scheid, J. Phys. G 12, L229 (1986).   
[47] B. B. Singh, S. K. Patra, and R. K. Gupta, Int. J. Mod. Phys. E 20, 1003 (2011).   
[48] D. S. Delion, Phys. Rev. C 80, 024310 (2009).   
[49] Y. Qian and Z. Ren, J. Phys. G 39, 015103 (2012).   
[50] M. Ismail and A. Adel, Phys. Rev. C 89, 034617 (2014).   
[51] O. A. P. Tavares, L. A. M. Roberto, E. L. Medeiros, Phys. Scr. 76, 375 (2007).   
[52] R. K. Gupta, in Clusters in Nuclei, Vol. I, edited by C. Beck, Lecture Notes in Physics, Vol. 818 (Springer, Heidelberg, 2010), p. 223.   
[53] D. Deng and Z. Ren, Phys. Rev. C 93, 044326 (2016).   
[54] M. Ismail and A. Adel, Phys. Rev. C 88, 054604 (2013).   
[55] W. Seif, Phys. Rev. C 91, 014322 (2015).   
[56] H. B. Yang, Z. G. Gan, Z. Y. Zhang, M. H. Huang, L. Ma, M. M. Zhang, C. X. Yuan, Y. F. Niu, C. L. Yang, Y. L. Tian et al., Phys. Rev. C 105, L051302 (2022).   
[57] M. Bhuyan, B. Maheshwari, H. A. Kassim, N. Yusof, S. K. Patra, B. V. Carlson and P. D. Stevenson, J. Phys. G: Nucl. Part. Phys. 48, 075105 (2021).   
[58] D. N. Poenaru, R. A. Gherghescu, and W. Greiner, Phys. Rev. C 85, 034615 (2012).

[59] K. P. Santhosh, T. A. Jose, and N. K. Deepak, Phys. Rev. C 105, 054605 (2022).