# Nuclear cross sections from low-energy interactions

J. Bostr¨om, J. Rotureau, B. G. Carlsson, and A. Idini Division of Mathematical Physics, Department of Physics, LTH, Lund University, PO Box 118, S-22100 Lund, Sweden

We present a method to calculate neutron scattering cross sections for deformed nuclei using many–body wavefunctions described with multiple reference states. Nuclear states are calculated with the generator coordinate method using a low energy effective Hamiltonian. Using these states, a non–local and energy dependent optical potential is consistently constructed, allowing to directly investigate the role of nuclear structure properties in nuclear scattering. The case of neutron scattering on $^ { 2 4 }$ Mg is presented. The results are compared to experiment and to phenomenological optical potentials at energies below 13 MeV, demonstrating the importance of low–energy collectivity in elastic and non–elastic scattering.

# I. INTRODUCTION

Nuclear reactions are one of the fundamental methods used to study and understand atomic nuclei. Exotic nuclei, which must be produced in radioactive ion beam facilities and studied before they decay, are often investigated through reaction processes [1, 2]. Reactions are not only crucial for understanding nuclei but also play a significant role in various astrophysical phenomena, for example stellar burning and nucleosynthesis [3, 4], as well as reactor physics, where reactions such as neutron induced reactions have practical applications and are important in the quest of generating microscopic data for simulations of new types of reactors [5].

It is extremely challenging to study nuclear reactions using state–of–the–art nuclear structure information in a consistent framework. The complexity of the dynamical processes happening during a scattering process often forces the use of separate and inconsistent models of structure and reaction, frequently relying on phenomenological optical potentials [6, 7]. Optical potentials represent the effective interaction between projectile and target and they are an effective way to decouple internal degrees of freedom and reaction dynamics [8]. They can be calculated exactly from the Hamiltonian of the many– body problem projected onto the elastic scattering channel, as shown already in [9]. Recently, several efforts have been made to calculate cross sections and produce adequate optical potentials consistently using microscopic nuclear structure models from Hamiltonian projection (cf. [1, 10] and refs. therein).

It is additionally difficult to describe reactions involving deformed nuclei. The symmetry breaking mechanisms that efficiently describe the deformation, impose an additional complexity to both the formalism and the computation of nuclear properties and their application to reactions [11].

In this manuscript, we propose a novel method for constructing an optical potential for deformed nuclei using microscopic symmetry breaking and restoration calculations. The formalism needed to construct Green’s functions and corresponding self–energy from multiple reference states is presented. In particular, a sum rule is intro-

duced that allows to represent a large Fock space, necessary for reaction observables, while applying a truncation to the many-body space relevant for structure properties, reducing computational time.

This method is applicable to a wide range of interactions and for the whole nuclear chart. Here, as a test case, we use it to calculate scattering cross sections of $n + { } ^ { 2 4 } \mathrm { M g }$ .

Our approach builds on previous work utilizing the generator coordinate method (GCM) with an effective low–energy interaction [12]. This combination is a versatile many–body framework capable of describing both light and superheavy deformed nuclei [12–14], and extends the GCM with a procedure that allows it to account for single–particle excitations. The GCM combined with symmetry restoration and carefully chosen collective degrees of freedom is an efficient way of obtaining manybody solutions that can be very close to exact solutions [15].

The method allows investigating the role of many– body correlations in scattering, with a particular focus on the effects of low–energy collectivity on the observed elastic scattering cross sections. In [16] self–consistent Green’s functions were used to calculate neutron elastic scattering of $^ { 1 6 }$ O and $^ { 4 0 }$ Ca, noting that the overestimation of elastic scattering cross section was due to lacking correlations and collectivity. This method alleviates this issue, concluding that GCM can reproduce low–energy collectivity important for reaction properties. These results show a promising route towards the systematic construction of microscopic optical potentials for heavy and deformed nuclei.

# II. METHOD

The method to construct an optical potential from a microscopic calculation presented in this paper relies on calculating the time–ordered Green’s function of the system, and then finding the associated self energy. The unperturbed Green’s function $G _ { 0 } \left( E \right)$ represents the propagation of a particle in a fixed external potential $U ^ { 0 }$ , while the dressed propagator $G \left( E \right)$

considers the effect of the interaction of the particle with a many–body system. Both can be seen as operators on the single–particle space. The two are related through the self energy $\Sigma \left( E \right)$ and the Dyson equation $G \left( E \right) = G _ { 0 } \left( E \right) + G _ { 0 } \left( E \right) \Sigma \left( E \right) G \left( E \right)$ , which can be solved for $\Sigma ( E )$ as

$$
\Sigma (E) = G _ {0} (E) ^ {- 1} - G (E) ^ {- 1}. \tag {1}
$$

The sum of the external potential and the self energy, $V \left( E \right) = U ^ { 0 } + \Sigma \left( E \right)$ , which is independent of the choice of external potential, can then be identified with the optical potential experienced by an additional particle scattering on the system [17].

Using complete sets of states for the systems with one more and one less particle, the matrix elements of the time–ordered Green’s function’s can be written in the K¨all´en–Lehmann representation as

$$
\begin{array}{l} G _ {\alpha , \beta} (E) = \lim  _ {\eta \rightarrow 0 ^ {+}} \sum_ {i} \frac {\left\langle \right. \Psi_ {0} \left. \right| a _ {\alpha} | \Psi_ {i} ^ {+} \rangle \left\langle \right. \Psi_ {i} ^ {+} \left. \right| a _ {\beta} ^ {\dagger} | \Psi_ {0} \left. \right\rangle}{E - (E _ {i} ^ {+} - E _ {0} - i \eta)} \\ + \sum_ {i} \frac {\left\langle \Psi_ {i} ^ {-} \mid a _ {\alpha} \mid \Psi_ {0} \right\rangle \left\langle \Psi_ {0} \mid a _ {\beta} ^ {\dagger} \mid \Psi_ {i} ^ {-} \right\rangle}{E + \left(E _ {i} ^ {-} - E _ {0} - i \eta\right)}, \tag {2} \\ \end{array}
$$

where $\left| { \Psi _ { 0 } } \right.$ represents the ground state of the system with $A$ particles and energy $E _ { 0 }$ , $\left| \Psi _ { i } ^ { \pm } \right.$ are a complete set of energy eigenstates of the system with $A \pm 1$ particles with energies $E _ { i } ^ { \pm }$ , $a _ { \alpha }$ are the annihilation operators of the single–particle basis in $m$ –scheme, and the infinitesimal $\eta$ ensures the correct time–ordering. In the continuum energy region, the sums would become integrals. Due to $\eta$ , this contributes a non–Hermitian part to the Green’s function. This non–Hermitian part is directly related to the scattering states, and is therefore important in the description of scattering.

Using wavefunctions obtained from a many–body solution, one can calculate the spectroscopic amplitudes of the $A \pm 1$ –particle states with respect to the $A$ –particle ground state $\Psi _ { 0 }$ , defined as $s _ { i , \alpha } ^ { + } ~ \equiv ~ \left. \Psi _ { i } ^ { + } \big | a _ { \alpha } ^ { \dagger } \big | \Psi _ { 0 } \right.$ and $s _ { i , \alpha } ^ { - } \equiv \left. \Psi _ { 0 } \left| a _ { \alpha } ^ { \dagger } \right| \Psi _ { i } ^ { - } \right.$ . The spectroscopic amplitudes represent how well the states $\left| \Psi _ { i } ^ { \pm } \right.$ are described as a single particle in the state $\alpha$ added on (or removed from) the $A$ –particle ground state $\Psi _ { 0 }$ . Their absolute squares, $| s | ^ { 2 }$ , are called spectroscopic factors.

Since many–body solution methods must truncate the full Fock space, the set of solutions obtained might not be complete, and in this case the K¨all´en–Lehmann representation (2) cannot be used directly. Here we propose a method to augment the solution set with additional states so that the K¨all´en–Lehmann representation can still be used and the Green’s functions can be calculated. The idea is that the many–body solution will include the most important contributions from correlated states in the energy range of interest, and that the remaining part can be approximated by an additional mean field. To find this mean field, we consider

two sum rules. First, we have the completeness relation $\begin{array} { r } { \sum _ { i , x = \pm } \left( s _ { i , \alpha } ^ { x } \right) ^ { * } s _ { i , \beta } ^ { x } = \delta _ { \alpha , \beta } } \end{array}$ , which corresponds to stating that the solutions of the $A \pm 1$ system fully spans the space of single–particle and single–hole excitations on the $A$ –particle ground state $\left| { \Psi _ { 0 } } \right.$ . Secondly, we consider the expression $( H _ { A } ) _ { \alpha , \beta } \equiv \left. \Psi _ { 0 } \right| \left\{ a _ { \alpha } , \left[ H , a _ { \beta } ^ { \dagger } \right] \right\} \left| \Psi _ { 0 } \right.$ , which we can expand and insert the completeness relations $\begin{array} { r } { \sum _ { i } \left| \Psi _ { i } ^ { \pm } \right. \left. \Psi _ { i } ^ { \pm } \right| = I ^ { \pm } } \end{array}$ , where $I ^ { \pm }$ are the identity operators on the spaces of $A \pm 1$ particles, to get

$$
\begin{array}{l} (H _ {A}) _ {\alpha , \beta} = \sum_ {i} \left(E _ {i} ^ {+} - E _ {0}\right) \left(s _ {i, \alpha} ^ {+}\right) ^ {*} s _ {i, \beta} ^ {+} \tag {3} \\ + \sum_ {i} (E _ {0} - E _ {i} ^ {-}) s _ {i, \beta} ^ {-} (s _ {i, \alpha} ^ {-}) ^ {*}. \\ \end{array}
$$

Defining $\bar { E } _ { i } ^ { \pm } = \pm \left( E _ { i } ^ { \pm } - E _ { 0 } \right)$ , this can be written as

$$
\sum_ {i, x = \pm} \left(s _ {i, \alpha} ^ {x}\right) ^ {*} \bar {E} _ {i} ^ {x} s _ {i, \beta} ^ {x} = \left\langle \Psi_ {0} \right| \left\{a _ {\alpha}, \left[ H, a _ {\beta} ^ {\dagger} \right] \right\} | \Psi_ {0} \rangle . \tag {4}
$$

This is related to the spectroscopic sum rule derived for nuclear matter in [18]. The right hand side is discussed in [19], where it is identified as the matrix elements of a generalized single–particle mean field for the state $\left| { \Psi _ { 0 } } \right.$ , and when $\left| { \Psi _ { 0 } } \right.$ is a Hartree–Fock state, it reduces to the matrix elements of the mean field Hamiltonian. Its eigenvalues are also identified as the experimentally observable centroids for the total stripping and pick–up strengths of the single–particle states [19].

For an incomplete set of states, these sum rules will in general not be fulfilled. However, using the sum rules we can find an estimate of the average contribution of the missing states, and allow us to introduce $N$ additional $A \pm 1$ –particle states, where $N$ is the number of single– particle states in the basis. Denoting the spectroscopic amplitudes and energies of the additional states $c _ { k , \alpha }$ and $\epsilon _ { k }$ , they must then satisfy the sum rules in the following way,

$$
\sum_ {i, x = \pm} \left(s _ {i, \alpha} ^ {x}\right) ^ {*} s _ {i, \beta} ^ {x} + \sum_ {k = 1} ^ {N} \left(c _ {k, \alpha}\right) ^ {*} c _ {k, \beta} = \delta_ {\alpha , \beta}, \quad (5)
$$

$$
\sum_ {i, x = \pm} \left(s _ {i, \alpha} ^ {x}\right) ^ {*} \bar {E} _ {i} ^ {x} s _ {i, \beta} ^ {x} + \sum_ {k = 1} ^ {N} \left(c _ {k, \alpha}\right) ^ {*} \epsilon_ {k} c _ {k, \beta} = \left(H _ {A}\right) _ {\alpha , \beta}. \tag {6}
$$

In the case of a rotationally and parity invariant system, the sum rules hold for each spin $J$ and parity $\pi$ , and in that case, $N = N ^ { J \pi }$ is the number of shells with the given spin and parity.

With the number of additional amplitudes and energies equal to the number of single–particle states, $N$ , the sum rules determine the additional states uniquely. This can be seen by rewriting the equations in matrix form. With $E _ { i j } = E _ { i } \delta _ { i j }$ and $\epsilon _ { i j } = \epsilon _ { i } \delta _ { i j }$ , the first sum rule then becomes $s ^ { \dagger } s + c ^ { \dagger } c = \mathrm { I }$ , and the second sum rule $s ^ { \dagger } E s + c ^ { \dagger } \epsilon c = H _ { A }$ . By using the polar decomposition of $c = U P$ , where $U$ is unitary and $P$ is Hermitian, we find $P ^ { 2 } = \mathrm { I } - s ^ { \dagger } s$ using the first rule, and

$U ^ { \dagger } \epsilon U = P ^ { - 1 } ( H _ { A } - s ^ { \dagger } \bar { E } s ) P ^ { - 1 }$ using the second. These can be uniquely solved using a matrix square root and as an eigenvalue equation, respectively.

With no many–body states with non–zero $s _ { i , \alpha } ^ { x }$ , the additional spectroscopic amplitudes and energies would be the eigenstates and eigenvalues of $H _ { A }$ , the generalized mean field. As the many–body solution converge and come closer to fulfilling the sum rules, the added ${ c } _ { k , \alpha }$ go to zero, and their contribution diminishes. The added contribution is therefore interpreted as the mean field average of the neglected states.

With these spectroscopic amplitudes and energies, we then construct the Green’s function in the K¨all´en– Lehmann representation using Eq. (5,6) as,

$$
G _ {\alpha , \beta} (E) = \sum_ {i, x = \pm} \frac {(s _ {i , \alpha} ^ {x}) ^ {*} s _ {i , \beta} ^ {x}}{E - \bar {E} _ {i} ^ {x} (\eta)} + \sum_ {k} \frac {(c _ {k , \alpha}) ^ {*} c _ {k , \beta}}{E - \bar {\epsilon} _ {k} (\eta)}, \quad (7)
$$

where $\bar { E } _ { i } ^ { \pm } \left( \eta \right) = \pm \left( E _ { i } ^ { \pm } - E _ { 0 } - i \eta \right)$ . $\bar { \epsilon } _ { k } \left( \eta \right)$ is chosen as $\bar { \epsilon } _ { k } \left( \eta \right) = \epsilon _ { k } + i \eta$ for $\epsilon _ { k } < E _ { \mathrm { F } }$ and $\bar { \epsilon } _ { k } \left( \eta \right) = \epsilon _ { k } - i \eta$ for $\epsilon _ { k } > E _ { \mathrm { F } }$ , where $E _ { \mathrm { F } }$ can be set appropriately according to the French-McFarlane sum rules [20, 21] but it can be taken as the Fermi energy $( E _ { 0 } ^ { + } - E _ { 0 } ^ { - } ) / 2$ with no difference to the results presented here.

Due to the discrete basis, continuum effects are not included, and so a finite value of $\eta$ is necessary to get nonelastic scattering. This is equivalent to treating the discrete energies as resonances with widths proportional to $\eta$ . There are methods for calculating the appropriate imaginary parts of the energies $\bar { E }$ , for example using a Berggren basis [22], as done in [23], however such a method is not employed in this first application of this method. In the results we will use a simpler recipe to set $\eta$ to an average resonance width.

To demonstrate the method, we employ the Hamiltonian described in [12] $H = E _ { 0 } + \Gamma + V$ , where $E _ { 0 }$ is a constant, $\Gamma$ and $V$ are the one and two–body components respectively. The form may be derived starting from a general interaction by a normal ordering procedure that approximates the three–body interaction [24]. In our case, the terms are given by a low–energy effective Hamiltonian that captures the response of an energy density functional to external fields [12].

The many–body basis that is used to solve the Hamiltonian consists of Hartree–Fock–Bogoliubov (HFB) vacua varied over a set of generator coordinates. The collective coordinates that generate the GCM basis are the familiar $\beta$ , and $\gamma$ for quadrupole deformation and triaxiality, in addition to a variation of the neutron (proton) pairing fields scaled by $g _ { n }$ ( $g _ { p }$ ) factors, and different cranking constraint $j _ { x }$ . To also include single– particle excitations, each HFB state $| \Phi ( \beta , \gamma , g _ { n } , g _ { p } , j _ { x } ) \rangle$ is also excited with a Bogoliubov singles coupled cluster operator with a temperature–like weighting obtaining $\left| { \Phi _ { x } } \right.$ [12]. This choice of generator coordinates and reference states accounts for the most important degrees of freedom of single–particle, collective vibrations, rotations and pairing vibrations already within the reference

states.Additionally, to describe states with an odd number of particles, we apply the quasiparticle creation operator $\beta _ { a } ^ { \dagger }$ to each HFB reference state, $\left| \Phi _ { a , x } ^ { \pm } \right. = \beta _ { a } ^ { \dagger } \left| \Phi _ { x } \right.$ .

These basis states are then projected to good angular momenta and particle numbers to calculate Hamiltonian and overlap matrices. The Hill–Wheeler equation is then constructed and solved, finally obtaining states $\begin{array} { r } { \left| \Psi _ { i } ^ { \pm , { J } \pi } \right. \ = \ \sum _ { a , x , M } h _ { a , x , i , M } ^ { J \pi } P _ { K , M } ^ { J } P _ { Z } P _ { N \pm 1 } \left| \Phi _ { a , x } ^ { \pm } \right. } \end{array}$ , where $\Psi _ { i } ^ { \pm }$ denote states with $A \pm 1$ particles with energy $E _ { i } ^ { \pm }$ , and $\Psi _ { i }$ denotes a state with $A$ particles with energy $E _ { i }$ . ity, $J$ is the total angular momentum, $_ i$ the label of the state, $h _ { a , x , i } ^ { J \pi }$ are coefficients, and $\pi = \pm 1$ is the par-$P _ { M , K } ^ { J }$ , $P _ { Z }$ and $P _ { N }$ are the projection operators for angular momentum, proton number and neutron number respectively. This method can be used with a wide variety of interactions and is able to cover the whole nuclear chart. The method described in this paper extends the GCM approach to also be used for scattering calculations.

When calculating using a spherically symmetric single– particle basis, and since an even–even ground state will have spin 0 and positive parity, the spectroscopic amplitude is only non–zero when the spin and parity of the operator $a _ { \alpha } ^ { \dagger }$ matches the spin and parity of the odd–even state Ψ+Jπ, $\Psi ^ { + } { } _ { i } ^ { J \pi }$ so $J _ { \alpha } = J$ and $\pi _ { \alpha } = \pi$ , and it’s only necessary to project the ket [25, 26]. More information regarding the calculation of the spectroscopic factors can be found in [20, 27].

We then construct $G _ { \alpha , \beta } \left( E \right)$ using (7) and the GCM solutions. $( G _ { 0 } ) _ { \alpha , \beta } \left( E \right)$ is constructed using the spherical Hartree–Fock solution used to define $\Gamma$ [12], substituting in Eq. (7) $s _ { i , \alpha } ^ { x }$ and $\bar { E } _ { i } ^ { \pm } \left( \eta \right)$ with the spectroscopic amplitudes and energies of the HF excitations, and $c _ { k , \alpha }$ $V _ { \alpha , \beta } ( E ) = U _ { \alpha , \beta } ^ { \mathrm { 0 } } + \Sigma _ { \alpha , \beta } ( E )$ with 0. We can then calculate the optical potential using (1), with $U ^ { 0 } = \Gamma - T$ as the potential part of $\Gamma$ while $T$ is the kinetic part.

To improve convergence, a smoothing factor is applied to the potential, as was proposed in [28] and used in several scattering calculations [29, 30]. The factor reduces the effect of basis truncation and the details of its implementation can be found in [21]. With this smoothed potential, the momentum space potential $V ^ { J \pi } \left( p , p ^ { \prime } , E \right)$ is calculated using the momentum space single–particle wavefunctions. The momentum space Schr¨odinger equation describing the scattering neutron of energy $E _ { \mathrm { { c m } } }$ in the center of mass frame for a given partial wave is

$$
\begin{array}{l} \frac {p ^ {2}}{2 \mu} u (p) + \gamma^ {3} \int \mathrm {d} p ^ {\prime} p ^ {\prime 2} V ^ {J \pi} (\gamma p, \gamma p ^ {\prime}, \gamma E _ {\mathrm {c m}}) u (p ^ {\prime}) \\ = E _ {\mathrm {c m}} u (p), \tag {8} \\ \end{array}
$$

where $\gamma \equiv m _ { 1 } / \mu = 1 + 1 / A$ , $\mu = m _ { 1 } m _ { 2 } / ( m _ { 1 } + m _ { 2 } )$ is the reduced mass, $m _ { 1 }$ and $m _ { 2 }$ are the projectile and target masses [16]. The Schr¨odinger equation in the laboratory frame is obtained substituting the reduced mass with the projectile mass, $\gamma$ with 1, and $E _ { \mathrm { { c m } } }$ with the projectile energy in the laboratory frame $E _ { p }$ .

This Schr¨odinger equation is then solved using the Lippmann–Schwinger equation in momentum space, giv-

ing the phase shifts for each partial wave, $\delta _ { J \pi }$ . The phase shifts are then used to calculate differential cross sections $\mathrm { d } \sigma / \mathrm { d } \Omega$ , as well as integrated elastic, reaction, and total cross sections $\sigma _ { E }$ , and $\sigma _ { T }$ , in the same way as in [31].

# III. RESULTS

As the first implementation of this method, we have calculated total and elastic neutron scattering cross sections of the characteristically prolate deformed nucleus $^ { 2 4 }$ Mg. The calculation of the nuclear wavefunctions were executed following the framework described in [12, 27]. The effective Hamiltonian was created for $^ { 2 4 }$ Mg using the SLy4 Skyrme parameterization [32]. SLy4 was previously used to calculate properties of $^ { 2 4 }$ Mg in [12, 33]. Using this Hamiltonian and basis states, the eigenstates of 23,24,25Mg were calculated [12, 27]. The convergence parameters are described in [21]. The wavefunctions were then used to calculate the spectroscopic amplitudes of $^ { 2 3 }$ Mg and $^ { 2 5 }$ Mg relative to the ground state of $^ { 2 4 }$ Mg and to construct the corresponding Green’s functions (7).

For the scattering calculations, $\eta$ was set to $\eta \quad =$ $\frac { a } { \pi } \frac { ( E - E _ { f } ) ^ { 2 } } { ( E - E _ { f } ) ^ { 2 } + b ^ { 2 } }$ with $a = 1 2$ MeV and $b = 2 2 . 3 6$ MeV following a common prescription to represent the average resonance widths [34, 35]. A variation of a factor 4 of the $\eta$ parameter obtains scattering results generally close to the provided convergence band, as shown in the inset of Fig. 1. $a = 2 4$ MeV gives on average 8.8% lower total cross section than $a = 6$ MeV, much smaller than the factor 4 increase of the average resonance widths represented by $\eta$ . Methods for treating the imaginary part of the Green’s function in (7) have been developed for example in [36] using self–consistency or in [1, 23] using continuum states. Such a consistent approach is not within the scope of this paper, but since the method can be seen to perconclusions of this paper. Neutron scattering on form well for a wide range of $\eta$ , it would not change the $^ { 2 4 }$ Mg was also calculated in [36, 37] with single–reference configuration interaction (shell model) prescriptions, making it an interesting case of comparison.

The cross sections are calculated using two different odd nucleus bases. These basis states are generated as eigenstates of the intrinsic $\exp ( - i \pi j _ { x } )$ operator with eigenvalue either $+ i$ or $- i$ known as their signature quantum number. Since either basis forms a complete set of many-body states after angular momentum projection [15], comparing the two can give an indication of the convergence of the cross section calculation. Additionally, cross sections werstates by setting $s _ { i , \alpha } ^ { x } = 0$ ted using only the completion in (5,6) and are presented in Fig. 2 and 3.

In Fig. 1 the integrated neutron total cross sections are shown for energies from $E = 0 . 5$ MeV to 13 MeV, together with the result of Koning–Delaroche optical potential [6]. We can see that below 10 MeV the calculation overestimates the cross section. Due to the choice of $\eta$ ,

![](images/5dbdde833fb46d4ac1de57ac3e909173ce57e6d450d4beace12708c1b955fc7f.jpg)  
Fig. 1. The total scattering cross section of $^ { 2 4 } \mathrm { M g } + n$ in function of the neutron energy in the lab frame. In the main figure, the red and purple lines correspond to the cross sections calculated using the method described in this paper with signature $+ i$ and $- i$ respectively and the area between them is shaded red. The cyan dashdotted line shows the result using the Koning–Delaroche optical potential. The black circles are experimental cross sections for $^ { 2 4 }$ Mg [38], while the diamonds are natural Magnesium [39]. In the inset, the results for $+ i$ signature and variation of $\eta$ parameters, with $a = 6 , 1 2 , 2 4$ MeV for light blue, green and purple line respectively.

resonances are wider than what experiments show at energies below 5 MeV.

The elastic scattering cross section is also calculated and compared to experiment in Fig. 2. We see that the calculated cross section slightly overestimates the cross section up to 9 MeV, and this difference increases for neutron energies above 10 MeV. This indicates that the method fails to find enough states that contribute to the non–elastic channels above 9 MeV, and progressively more of the contribution comes from the mean field through the completion. The potential obtained using only completion states is a real potential and only the elastic scattering channel is available in this case, resulting in a sizeable overestimation of the elastic scattering cross section in Fig. 2. At higher energy the calculated GCM $_ { O _ { E , T } }$ will gradually reach the result with only completion above 20 MeV.

The angular differential cross sections were calculated for several projectile energies, as shown in Fig. 3, along with the corresponding experimental values. It is important to note that the solution to the scattering problem represents only one component of the experimentally measured cross section. When a neutron is absorbed, forming an excited $^ { 2 5 }$ Mg nucleus that subsequently decays by emitting another neutron of the same energy, this compound nucleus reaction contributes to the measured cross section and is indistinguishable from elastic scattering. Since the compound nucleus has time to thermalize, its emission is approximately isotropic, contributing to

![](images/e49212236ea821a6ce13014fb35e073a1b563ede6b1b18e55589d69791d5b76d.jpg)  
Fig. 2. The elastic scattering cross section of $^ { 2 4 } \mathrm { M g } + n$ in function of neutron energy in the lab frame. The lines and datapoints mean the same as in Fig. 1. Additionally, the integrated cross section calculated with only the completion states is shown as a dashed blue line. The experimental cross sections for 24Mg are from [40–42], while the natural Magnesium cross sections are from [43–50].

the differential cross section with little angular dependence. This effect is expected to be more significant at lower energies and around the minima.

To more accurately compare with experimental data, in Fig. 3 we include the compound nucleus contribution calculated using the semi-microscopic optical model of [52, 53] (known as JLM), which is based on properties of nuclear matter and it is phenomenologically adjusted to reproduce scattering. Developing a compound nucleus model for a general non–local potential is particularly challenging and beyond the scope of the present study, hence we use a local optical model as in [36]. This additional component is necessary because of the use of scattering theory (8) to describe elastic scattering, not due to our particular microscopic approach constructing the optical potential.

In conclusion, an energy weighted sum rule for spectroscopic amplitudes is introduced, interpreted as a generalized mean field, which bridges the gap between nuclear structure and scattering that arise due to the necessary truncations done in many–body methods. The results demonstrate the viability of this new method, and it enables calculating scattering observables from a wide range of many–body methods and interactions. In addition, the results suggest the lack of absorption observed when using a microscopically generated optical potential, that was linked to configurations beyond particle–hole excitation in [16], is partially taken into account through the collective degrees of freedom when using GCM. This shows that GCM can capture necessary low energy correlations needed to describe low energy neutron scattering with a microscopic method using multiple reference states, though further research is required to better un-

![](images/9068c1da8c1ba38610c75a596b60c4574772182b66fda12a41746bbdce1064fe.jpg)  
Fig. 3. The differential cross section of elastic $^ { 2 4 } \mathrm { M g } + n$ scattering for four different neutron energies with respect to center–of–mass angle. The lab frame energies are shown in the figure in MeV. The lines and datapoints mean the same as in Fig. 2. The dashed lines at 1.5 and 9.76 MeV refer to the calculation with only the completion states. The experimental data are from [40, 41, 45, 51]. The cross sections for each energy are shifted down by a factor of 10 relative to the previous.

derstand the resonance widths of GCM states, important in the description of both elastic and nonelastic scattering. A need for compound scattering implementations for general non–local potentials was also identified. This work extends microscopic reaction approaches to study deformed, heavy, and exotic nuclei, representing a significant step towards a unified model of nuclear structure and reaction. The flexibility of this method will allow for further improvements through the use of new interactions, functionals, collective coordinates, and many–body expansions, and enables it to be used for the whole nuclear chart.

This work has been supported by the Swedish Research Council (Vetenskapsr˚adet) VR 2020-03721, Knut and Alice Wallenberg foundation (KAW 2015.0021), Crafo-

ord fundation, and Krapperup fundation. Computing was enabled by resources provided by the National Academic Infrastructure for Supercomputing in Sweden (NAISS), partially funded by the Swedish Research Council through grant agreement no. 2022-06725, and The Centre for Scientific and Technical Computing at Lund University (LUNARC).

[1] C. W. Johnson, K. D. Launey, and others, Journal of Physics G: Nuclear and Particle Physics 47, 123001 (2020).   
[2] H. Crawford, K. Fossez, S. K¨onig, and A. Spyrou, Annual Review of Nuclear and Particle Science 74 (2024).   
[3] F. Nunes, Nucl. Phys. A 757, 349 (2005).   
[4] H. Schatz and et al., Journal of Physics G: Nuclear and Particle Physics 49, 110502 (2022).   
[5] D. Rochman, A. Koning, S. Goriely, and S. Hilaire, Nuclear Physics A 1054, 122979 (2025).   
[6] A. J. Koning and J. P. Delaroche, Nucl. Phys. A 713, 231 (2003).   
[7] C. D. Pruitt, J. E. Escher, and R. Rahman, Phys. Rev. C 107, 014602 (2023).   
[8] H. Feshbach, Annual Review of Nuclear Science 8, 49 (1958).   
[9] H. Feshbach, Annals of Physics 5, 357 (1958).   
[10] C. Hebborn, F. M. Nunes, G. Potel, et al., J. Phys. G 50, 060501 (2023).   
[11] A. Idini et al., J. Phys.: Conf. Ser. 2586, 012049 (2023).   
[12] J. Ljungberg, B. G. Carlsson, J. Rotureau, A. Idini, and I. Ragnarsson, Phys. Rev. C 106, 014314 (2022).   
[13] A. S˚amark-Roth et al., Phys. Rev. Lett. 126, 032503 (2021).   
[14] J. Ljungberg et al., J. Phys.: Conf. Ser. 2586, 012081 (2023).   
[15] B. Bally and M. Bender, Phys. Rev. C 103, 024315 (2021).   
[16] A. Idini, C. Barbieri, and P. Navr´atil, Phys. Rev. Lett. 123, 092501 (2019).   
[17] F. Capuzzi and C. Mahaux, Annals of Physics 245, 147 (1996).   
[18] A. Polls, A. Ramos, J. Ventura, S. Amari, and W. H. Dickhoff, Phys. Rev. C 49, 3050 (1994).   
[19] D. J. Rowe, Rev. Mod. Phys. 40, 153 (1968).   
[20] J. Bostr¨om, B. G. Carlsson, and A. Idini, To be published.   
[21] Supplementary Material.   
[22] T. Berggren, Nuclear Physics A 109, 265 (1968).   
[23] J. Rotureau, P. Danielewicz, G. Hagen, F. M. Nunes, and T. Papenbrock, Phys. Rev. C 95, 024315 (2017).   
[24] W. Lin, E. Zhou, J. Yao, and H. Hergert, Symmetry 16, 10.3390/sym16040409 (2024).   
[25] H.-B. H˚akansson, T. Berggren, and R. Bengtsson, Nuclear Physics A 306, 406 (1978).   
[26] K. Enami, K. Tanabe, and N. Yoshinaga, Phys. Rev. C 59, 135 (1999).   
[27] J. Bostr¨om et al., J. Phys.: Conf. Ser. 2586, 012080 (2023).   
[28] J. Revai, M. Sotona, and J. Zofka, J. Phys. G: Nucl. Phys. 11, 745 (1985).

[29] A. M. Shirokov, A. I. Mazur, and V. A. Kulikov, Physics of Atomic Nuclei 84, 131 (2021).   
[30] W. Du, S. Pal, M. Sharaf, P. Yin, S. Sarker, A. M. Shirokov, and J. P. Vary, Phys. Rev. C 106, 054608 (2022).   
[31] H. Arellano and G. Blanchon, Computer Physics Communications 259, 107543 (2021).   
[32] E. Chabanat, P. Bonche, P. Haensel, J. Meyer, and R. Schaefferha, Nucl. Phys. A 635, 231 (1998).   
[33] M. Bender and P.-H. Heenen, Phys. Rev. C 78, 024309 (2008).   
[34] S. Waldecker, C. Barbieri, and W. H. Dickhoff, Phys. Rev. C 84, 034616 (2011).   
[35] G. Brown and M. Rho, Nuclear Physics A 372, 397 (1981).   
[36] G. H. Sargsyan, G. Potel, K. Kravvaris, and J. E. Escher, Microscopic optical potentials from a greens function approach (2024), arXiv:2410.21714 [nucl-th].   
[37] K. Kravvaris, S. Quaglioni, and P. Navr´atil, Phys. Rev. C 109, 054603 (2024).   
[38] J. Bommer, M. Ekpo, H. Fuchs, K. Grabisch, and H. Kluge, Nuclear Physics A 263, 86 (1976).   
[39] W. P. Abfalterer, F. B. Bateman, F. S. Dietrich, R. W. Finlay, R. C. Haight, and G. L. Morgan, Phys. Rev. C 63, 044608 (2001).   
[40] A. Virdis, Rept: Centre dEtudes Nucleaires, Saclay Re- ´ ports , 5144 (1981).   
[41] T. Schweitzer, D. Seeliger, and S. Unholzer, EX-FOR30463 (1978).   
[42] L. Frittelli, F. Vinci, and E. Demanins, Rept: Com.Naz. per l’Energia Nucleare Reports (1970).   
[43] I. Korzh, V. Mishchenko, N. Pravdivy, and N. Sklyar, Ukrainskii Fizichnii Zhurnal 39, 785 (1994).   
[44] M. Adel-Fawzy, H. F¨ortsch, D. Schmidt, D. Seeliger, and T. Streil, Nuclear Physics A 440, 35 (1985).   
[45] I. Korzh, V. Mishchenko, M. Pasechnik, N. Pravdivyi, I. Sanzhur, and I. Totskii, Ukrainian Physics Journal 13, 1266 (1969).   
[46] I. Korzh, N. Kopytin, M. Pasechnik, N. Pravdivyi, N. Sclyar, and I. Totskii, Soviet Atomic Energy 16, 312 (1964).   
[47] I. Korzh and N. Sklyar, Ukrainskii Fizichnii Zhurnal 8, 1389 (1963).   
[48] D. B. Thomson, L. Cranberg, and J. S. Levin, Phys. Rev. 125, 2049 (1962).   
[49] R. N. Little, R. W. Long, and C. E. Mandeville, Phys. Rev. 69, 414 (1946).   
[50] M. R. MacPhail, Phys. Rev. 57, 669 (1940).   
[51] D. Stewart, W. Currie, J. Martin, and P. Martin, Conf: Nuclear Structure Study with Neutrons, Antwerp , 509 (1965).   
[52] E. Bauge, J. P. Delaroche, and M. Girod, Phys. Rev. C 63, 024607 (2001).

[53] A. Koning, S. Hilaire, and S. Goriely, The European Physical Journal A 59, 131 (2023).