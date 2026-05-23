# Investigating the weak charge of $4 8$ Ca using a dispersive optical model

N. L. Calleya $^ { \mathrm { a } , \ast }$ , M. C. Atkinsonb, W. H. Dickhoffa

aDepartment of Physics, Washington University in St. Louis, MO 63130 USA

bLawrence Livermore National Laboratory, P.O. Box 808, L-414, Livermore, CA 94551, USA

# Abstract

A new nonlocal dispersive-optical-model analysis has been carried out for neutrons and protons in $^ { 4 8 }$ Ca that reproduces the weak-form-factor measurement of CREX. In addition to elastic-scattering angular distributions, total and reaction cross sections, single-particle energies, the neutron and proton numbers, and the charge distribution, the CREX-measured weak form factor has been fit to extract the neutron and proton self-energies both above and below the Fermi energy. The resulting single-particle propagators yield a weak form factor of $F _ { W } = 0 . 1 2 5 \pm 0 . 0 5$ and a neutron skin of $R _ { \mathrm { s k i n } } =$ 0.152 ± 0.05 fm, in good agreement with CREX. The rearrangement of the neutron distribution to accommodate such a thin neutron skin results in the high-momentum content of the neutrons exceeding that of the protons, in contrast to what is expected from high-energy two-nucleon knockout measurements by the CLAS collaboration and ab initio asymmetric matter calculations. The present analysis also emphasizes the importance of neutron experimental data in constraining weak charge observables necessary for a precise description of neutron densities. Notably, the neutron reaction cross section and further parity-violating experiments weak form factor measurements are essential to generate a unique way to determine the $^ { 4 8 }$ Ca neutron distribution in this framework.

In contrast to proton distributions and its related charge density, which has been experimentally probed for many nuclei across the periodic table, the neutron counterpart remains elusive. In particular, for nuclei with more neu-[ trons than protons such as $^ { 4 8 }$ Ca, the determination of how these nucleons are distributed over the nuclear volume is of significant importance not only for its value as a nuclearstructure observable but also for its close relation to the neutron skin thickness $R _ { \mathrm { s k i n } }$ and consequently what this quantity represents.

Defined as the difference between neutron and proton root-mean-squared (RMS) radii, i.e., $R _ { \mathrm { s k i n } } = R _ { n } – R _ { p }$ , the neutron skin has a connection to the nuclear symmetry energy: its value is determined by the relative strengths of the symmetry energy between the central near-saturation and peripheral less-dense regions. In other words, $R _ { \mathrm { s k i n } }$ is a measure of the density dependence of the symmetry energy around saturation [1–4]. The skin is also directly correlated to the slope of the symmetry energy $L$ , since a thicker skin favors a larger $L$ and a thinner skin a smaller one. The precise determination of $R _ { \mathrm { s k i n } }$ is pertinent to further understand many nuclear properties including masses, radii, and the location of the drip lines in the chart of nuclides. Its importance extends to astrophysics for understanding supernovae and neutron stars [5, 6] due to the aforementioned symmetry energy role in the equation of state (EOS) for nuclear matter, and to heavy-ion reactions [7].

Given the broad implications in a wide variety of physics research areas, the neutron skin has been the subject of many studies both experimental and theoretical to determine its thickness [8, 9]. While $R _ { p }$ is extracted quite accurately from the charge form factor, $F _ { \mathrm { c h } }$ , derived from elastic electron scattering cross sections [10] and laser spectroscopy [11], most experimental determinations of $R _ { n }$ are model dependent [8] and rely on strong interacting probes. With the use of parity-violating electron scattering [12], it is possible to obtain the weak distribution with the same degree of model independence since the weak charge distribution. Since the weak charge distribution is predominantly determined by the neutrons, this is an accurate method for determining the neutron skin.

The first parity-violating experiment performed by the PREX collaboration yielded a thick neutron skin of $^ \mathrm { 2 0 8 }$ Pb with a rather large uncertainty [13]. A second experiment, dubbed PREX-2, was later performed resulting in a $^ \mathrm { 2 0 8 }$ Pb skin of $R _ { \mathrm { s k i n } } ^ { 2 0 8 } = 0 . 2 8 3 \pm 0 . 0 7 1$ fm [14]. The following year, the CREX experiment extracted a much smaller skin in $^ { 4 8 }$ Ca of $R _ { \mathrm { { s k i n } } } ^ { 4 8 } = 0 . 1 2 1 \pm 0 . 0 2 6 ( \mathrm { e x p } ) \pm 0 . 0 2 4 ( \mathrm { m o d e l } )$ fm [15]. A thick-thin skin scenario between the two asymmetric nuclei creates friction regarding the nuclear EOS and slope of the symmetry energy $L$ , and also in exotic astrophysical systems such as neutron stars [16]. More specifically, mass-radius curves predicted from the two different $R _ { \mathrm { s k i n } }$ - derived EOS are incompatible with each other and even with observations.

Currently there are no adequate models that can predict both PREX-2 and CREX results for neutron skins simultaneously. Mean-field approaches predict a strong

positive correlation between the neutron skins of $^ { 2 0 8 }$ Pb and $^ { 4 8 }$ Ca although it has been argued that the large error bars for PREX-2 may not provide a stringent constraint on the isovector part of energy density functionals [17]. $A b$ initio approaches also exist for both nuclei. In Ref. [18] a neutron skin for $^ { 4 8 }$ Ca was predicted that is consistent with CREX while the result of Refs. [19, 20] exhibits mild tension with PREX-2.

A unique approach to determining neutron skins in $^ { 4 8 }$ Ca and $^ \mathrm { 2 0 8 }$ Pb is provided by the dispersive optical model (DOM) which, unlike mean-field or ab initio methods applied to these nuclei, describes scattering observables in addition to bound nucleon properties by making use of a dispersion relation that couples both energy domains above and below the Fermi energy. By leveraging Green’s function theory, the DOM establishes a nucleon self-energy as a phenomenological optical potential constrained by both bound-state and scattering measurements [21–23].

An earlier DOM analysis of $^ \mathrm { 2 0 8 }$ Pb predicted a neutron skin of $R _ { \mathrm { s k i n } } ^ { \mathrm { \tiny { D O M } } } = 0 . 2 5 \pm 0 . 0 5$ fm which is within $1 \sigma$ of th e PREX-2 measurement published the following year [24]. nalysis of $^ { 4 8 }$ Ca in 2017 resulted in $R _ { \mathrm { s k i n } } ^ { \mathrm { D O M } } =$ $0 . 2 4 9 \pm 0 . 0 2 3$ tions suggested by previous systematic studies, is over $2 \sigma$ away from the CREX measurement published five years later [25]. These skins are also in agreement with those predicted by a separate DOM fit using a slightly different parametrization of the optical potential together with a Markov Chain Monte Carlo approach [26, 27].

We aim to confront the CREX-PREX puzzle by constraining the DOM self-energy to reproduce the CREXmeasured weak form factor at momentum transform $q =$ $0 . 8 7 3 3 \ \mathrm { f m } ^ { - 1 }$ of $F _ { W } = 0 . 1 3 0 4 \pm 0 . 0 0 5 2 ( \mathrm { s t a t } ) \pm 0 . 0 0 2 0 ( \mathrm { s y s t }$ ). Our new DOM fit of $^ { 4 8 }$ Ca results in a much thinner skin of $R _ { \mathrm { s k i n } } ^ { \mathrm { D O M } } = 0 . 1 5 2 \pm 0 . 0 5$ fm while maintaining an acceptable all observables are in good agreement with experimental data, we find that the high-momentum content, defined here as the percentage of particles with momentum greater than 270 MeV/c, is affected in a way consistent with a more confined neutron distribution. This may point to tension with expectations based on high-energy knockout measurements by the CLAS collaboration [28, 29] as well as ab initio asymmetric matter calculations that properly treat the effect of the nuclear tensor force [30, 31].

In the many-body Green’s function formalism the socalled irreducible self-energy, $\Sigma ^ { \ast } ( \boldsymbol { r } , \boldsymbol { r } ^ { \prime } ; E )$ , is a complex one-body potential which, in principle, is comprised of an infinite set of Feynman diagrams describing the propagation of an interacting nucleon through a nucleus based on a Hamiltonian containing relevant two- and three-body interactions [32]. This complex one-body potential can be parametrized as an optical potential, and the link to the negative-energy domain emerges naturally in the Green’s function framework as was realized by Mahaux and Sartor who introduced the DOM as reviewed in Ref. [33]. The analytic structure of the nucleon self-energy allows one to ap-

ply a dispersion relation, which relates the real part of the self-energy at a given energy to a dispersion integral of its imaginary part over all energies. The energy-independent correlated Hartree-Fock (HF) contribution [32] is removed by employing a subtracted dispersion relation with the Fermi energy used as the subtraction point [33]

$$
\begin{array}{l} \operatorname {R e} \Sigma^ {*} (\alpha , \beta ; E) = \operatorname {R e} \Sigma^ {*} (\alpha , \beta ; \varepsilon_ {F}) \tag {1} \\ - \mathcal {P} \int_ {\varepsilon_ {F}} ^ {\infty} \frac {d E ^ {\prime}}{\pi} \operatorname {I m} \Sigma^ {*} (\alpha , \beta ; E ^ {\prime}) \left[ \frac {1}{E - E ^ {\prime}} - \frac {1}{\varepsilon_ {F} - E ^ {\prime}} \right] \\ + \mathcal {P} \int_ {- \infty} ^ {\varepsilon_ {F}} \frac {d E ^ {\prime}}{\pi} \operatorname {I m} \Sigma^ {*} (\alpha , \beta ; E ^ {\prime}) \left[ \frac {1}{E - E ^ {\prime}} - \frac {1}{\varepsilon_ {F} - E ^ {\prime}} \right], \\ \end{array}
$$

where $\varepsilon _ { F } = { \textstyle { \frac { 1 } { 2 } } } ( E _ { 0 } ^ { A + 1 } - E _ { 0 } ^ { A - 1 } )$ is the average Fermi energy which separates the particle and hole domains [32].

The subtracted form has the further advantage that the emphasis is placed on energies closer to the Fermi energy for which more experimental data are available. The real part of the self-energy at the Fermi energy is then still referred to as the HF term, $\Sigma _ { \mathrm { H F } }$ , but is sufficiently attractive for binding. In practice, the imaginary part is assumed to extend to the Fermi energy on both sides while being very small in its vicinity. Initially, standard functional forms for these terms were introduced by Mahaux and Sartor who also cast the DOM potential in a local form by a standard transformation which turns a nonlocal static HF potential into an energy-dependent local potential [34]. Such an analysis was extended in Refs. [35, 36] to a sequence of Ca isotopes and in Ref. [37] to semi-closed-shell nuclei heavier than Ca.

The transformation to the exclusive use of local potentials precludes a proper calculation of nucleon particle number and expectation values of the one-body operators, such as the charge density in the ground state. This obstacle was eliminated in Ref. [38], but it was shown that the introduction of nonlocality in the imaginary part was still necessary in order to accurately account for particle number and the charge density [21]. Theoretical work provided further support for this introduction of a nonlocal representation of the imaginary part of the self-energy [39, 40]. A review has been published in Ref. [41].

We implement a nonlocal representation of the selfenergy following Ref. [21] where $\Sigma _ { \mathrm { H F } } ( \boldsymbol { r } , \boldsymbol { r } ^ { \prime } )$ and the imaginary part Im $\Sigma ( \boldsymbol { r } , \boldsymbol { r } ^ { \prime } ; E )$ are parametrized, and Eq. (1) generates the energy dependence of the real part. The HF term consists of a volume term, spin-orbit term, and a wine bottle shape [42] to simulate a surface contribution. The imaginary self-energy consists of volume, surface, and spinorbit terms. Nonlocality is represented using the Gaussian form as proposed in Ref. [34]. This form is particularly useful as it has an analytic expression in a partial-wave basis [43]. More details can be found in [24], a description of the potential terms as well the final parameter set is left to the supplementary material.

To use the DOM self-energy for predictions, the parameters are fit through a weighted $\chi ^ { 2 }$ minimization of

available elastic differential cross section data $\textstyle { \left( { \frac { d \sigma } { d \Omega } } \right) }$ , analyzing power data ( $A _ { \theta }$ ), reaction cross sections (σr), total cross sections (σt), charge density ( $\rho _ { \mathrm { c h } }$ ), energy levels $( \varepsilon _ { \ell j } )$ , particle number, separation energies, the rootmean-square charge radius ( $R _ { \mathrm { c h } }$ ), and the energy of the ground state [44]. Also included in this fit is the weak form factor of $^ { 4 8 }$ Ca, $F _ { W } ^ { 4 8 }$ . The scattering calculations are performed using the framework of $R$ -matrix theory [45] and the bound-state calculations utilize Green’s function formalism. All calculations are done in a Lagrange basis with 30 mesh points, where Legendre polynomials mapped to $r \ = \ 0 \  \ 1 2$ fm are used for scattering calculations and Laguerre polynomials are used for bound-state calculations [45, 46].

We employ the Dyson equation to obtain the Green’s function, $G _ { \ell j } ( \alpha , \beta ; E )$ , from the DOM self-energy,

$$
\begin{array}{l} G _ {\ell j} (\alpha , \beta ; E) = G _ {\ell} ^ {(0)} (\alpha , \beta ; E) \\ + \sum_ {\gamma , \delta} G _ {\ell} ^ {(0)} (\alpha , \gamma ; E) \Sigma_ {\ell j} ^ {*} (\gamma , \delta ; E) G _ {\ell j} (\delta , \beta ; E), \\ \end{array}
$$

where $G _ { \ell } ^ { ( 0 ) } ( \alpha , \beta ; E )$ corresponds to the free propagator (the Green’s function when $\Sigma _ { \ell j } ^ { * } ( \gamma , \delta ; E ) = 0$ ) [32]. The particle number, binding energy, and charge density are all obtained from the so-called hole spectral function which corresponds to the imaginary part of the Green’s functions,

$$
S _ {\ell j} ^ {(p, n)} (\alpha , \beta ; E) = \frac {1}{\pi} \mathrm {I m} G _ {\ell j} ^ {(p, n)} (\alpha , \beta ; E).
$$

The single-particle density distribution can be calculated from the hole spectral function in the following way,

$$
\rho^ {(p, n)} (r) = \frac {1}{4 \pi} \sum_ {\ell j} (2 j + 1) \int_ {- \infty} ^ {\varepsilon_ {F}} d E S _ {\ell j} ^ {(p, n)} (r, r; E), \quad (2)
$$

where we are now explicitly in coordinate space. The RMS radii of the proton and neutron distributions of Eq. (2) are used to calculate $R _ { \mathrm { s k i n } }$ as well as the nuclear charge radius,

$$
R _ {\mathrm {c h}} ^ {2} = R _ {p} ^ {2} + \langle r _ {p} ^ {2} \rangle + \frac {N}{Z} \langle r _ {n} ^ {2} \rangle + \langle r _ {\mathrm {D F}} ^ {2} \rangle + \langle r _ {S O} ^ {2} \rangle , (3)
$$

where $\langle r _ { S O } ^ { 2 } \rangle$ is the spin-orbit contribution calculated according to Ref. [22], $\langle r _ { p } ^ { 2 } \rangle = 0 . 7 0 9 \ \mathrm { f m ^ { 2 } }$ is the charge radius squared of the proton [47], $\langle r _ { n } ^ { 2 } \rangle = - 0 . 1 0 6 \ : \mathrm { f m ^ { 2 } }$ is the charge radius squared of the neutron [48], and $\langle r _ { \mathrm { D F } } ^ { 2 } \rangle$ is the socalled Darwin-Foldy term which is a relativistic correction. To obtain the charge density, $\rho _ { \mathrm { c h } } ( r )$ , we fold the singleparticle densities with neutron and proton charge distributions in addition to calculating their spin-orbit contributions as detailed in Refs. [22, 49]. To ensure that the proton charge density is consistent with $R _ { \mathrm { c h } }$ of Eq.(3), we updated the proton charge distribution to reflect the updated proton charge radius of Ref. [47]. Particle numbers $N$ and $Z$ are the normalizations of the neutron and proton distributions in Eq. (2). The ground-state binding energy is calculated from $S _ { \ell j } ^ { ( p , n ) } ( \alpha , \beta ; E )$ Sℓj using the Migdal-Galitski

sum rule [32, 50]. Quasihole energy levels are calculated from a Schr¨odinger-like equation derived from the Dyson equation, see Ref. [24] for details.

As discussed previously, the difference between the current fit and the previous one of Ref. [25] involves the inclusion of the CREX-measured $F _ { W } ( q ^ { 2 } )$ at $q = 0 . 8 7 3 3 \ \mathrm { f m ^ { - 1 } }$ as a constraint on the DOM self energy. We chose to fit directly to $F _ { W }$ rather than $R _ { \mathrm { s k i n } }$ to have a closer comparison to what is actually measured. This removes any ambiguity arising from the reduced correlation between $R _ { \mathrm { s k i n } }$ and $F _ { W }$ in $^ { 4 8 }$ Ca vs. $^ \mathrm { 2 0 8 }$ Pb [16]. Another difference from the earlier fit is the relaxation of the error associated with neutron total cross section data above 100 MeV [51] that were an important ingredient in generating a thick skin [25]. We found that this adjustment was necessary in order to reproduce a thin skin.

The weak form factor is the Fourier transform of the weak-charge distribution $\rho _ { W } ( r )$ which, analogously to $\rho _ { c h } ( r )$ , is calculated by folding the proton and neutron weakcharge distributions with $\rho ^ { ( p , n ) } ( r )$ from Eq. (2). Following the prescription of Ref. [49], we also include the spin-orbit contribution which has a non-negligible impact on $F _ { W }$ . Notably, we found that explicitly calculating the spin-orbit contributions from all protons and neutrons yielded a different result than calculating only the spin-orbit contribution from the additional $f 7 / 2$ neutrons.

Among the many parametrizations explored during the fitting process, we found several that reproduced similar $F _ { W }$ at the particular value of $q = 0 . 8 7 3 3 \ \mathrm { f m ^ { - 1 } }$ , but had different $F _ { W } ( q )$ shapes for other values of $q$ (see the solid and dot-dashed lines in Fig. 1). Included in Fig. 1 is also the original DOM prediction of Ref. [25] that yielded a large skin (dashed line). The two alternative current fits yield skin values of 0.14 and 0.15 fm, where the latter was chosen as the representative fit for this work and subsequent figures where no other fits are indicated. For a brief comparison of these fits, see the supplementary material. The uncertainty band in Fig. 1 was generated by running numerous DOM fits to randomly-scrambled neutron data (including the $F _ { W } ^ { \prime }$ ) within $1 \sigma$ of their experimental uncertainties. The standard deviation of this band at $q = 0 . 8 7 3 3$ $\mathrm { f m } ^ { - 1 }$ results in an uncertainty of $0 . 0 5 ~ \mathrm { f m ^ { - 1 } }$ for our predicted weak form factor. The different weak form factor shapes illustrated in Fig. 1 translate to having several different neutron distribution shapes while keeping similar $R _ { \mathrm { s k i n } }$ values consistent with CREX.

Additional measurements at different $q$ values can hopefully further constrain the shape of $F _ { W } ( q )$ and provide greater insight into the neutron distribution for $^ { 4 8 }$ Ca. It is clear that measurements of the weak form factor at lower momentum transfer will not affect the skin value (if consistent with CREX) but may reduce the experimental error. A measurement at higher momentum transfer will of course clarify the properties of the interior weak (and therefore neutron) distribution but will most likely have a substantial percent error, which in turn may not help select the best DOM parametrization.

![](images/b0dc5ddd2e54ec26ea5c9824812a463f387fa7223540d6e9d83e15029b5b6c01.jpg)  
Figure 1: Difference between the charge and weak form factors in $^ { \mathrm { 4 8 } } \mathrm { C a }$ . The data point indicates CREX measurement with both experimental and model uncertainty represented by error bars. The solid blue line is the result of the best DOM fit with $R _ { \mathrm { s k i n } } = 0 . 1 5$ fm while the dash-dotted red line is a comparable DOM fit with $R _ { \mathrm { s k i n } } = 0 . 1 4$ fm. The dashed black line is the result of the previous fit from Refs. [25, 52] with $R _ { \mathrm { s k i n } } = 0 . 2 5 ~ \mathrm { f m }$ . The shaded region is an uncertainty band determined from the experimental errors of the neutron data included in the DOM fit using a bootstrap method.

It is no surprise that the neutron distributions of the current fits concentrate more strength near $r = 0$ fm to accommodate the thin skin of $R _ { \mathrm { s k i n } } = 0 . 1 5 2$ fm (see Fig. 2 for a comparison to the previous thick-skin fit). Due to the Heisenberg uncertainty principle, concentrating neutron presence near the origin leads to increased high-momentum content in the momentum distribution $n ( k )$ . This highmomentum content is associated with short-range correlation (SRC) pairs. Knockout experiments [28, 29] and ab initio calculations for asymmetric matter [30, 31] suggest an increased high-momentum content for the minority species in nuclei. Realistic many-body calculations of low-$A$ nuclei using variational Monte Carlo (VMC) techniques also reveal that the majority of this high-momentum content comes from the tensor force in the nucleon-nucleon interaction [54].

The tensor force preferentially acts on neutron-proton $( n p )$ pairs with total spin $S = 1$ . This phenomenon is known as np dominance [57], and is demonstrated by a factor of 20 difference between the number of observed np SRC pairs and the number of observed $p p$ and nn SRC pairs in exclusive $( e , e ^ { \prime } p p )$ and $( e , e ^ { \prime } p )$ cross section measurements of $\mathrm { ^ { 1 2 } C }$ , 27Al, $^ { 5 6 }$ Fe, and ${ } ^ { 2 0 8 } \mathrm { P b }$ [57]. The dominance of $n p$ SRC pairs would imply that the number of high-momentum protons observed in a nucleus is dependent on how many neutrons it contains. More specifically, one would expect that the high-momentum content of protons would increase with neutron excess since there are more neutrons available to make np SRC pairs. The CLAS collaboration confirmed this asymmetry dependence by measuring the high-momentum content of pro-

![](images/e941db062005b0d67e5ce74c5b18f8d51fe1c9698045bc02980d37f9da3abf3a.jpg)  
Figure 2: DOM charge and neutron distributions in $^ { 4 8 } \mathrm { C a }$ . The experimental charge distribution is represented by the breen band [53], with the dash-dot-dot green line representing the charge density from the best-fit DOM with a corresponding $R _ { \mathrm { s k i n } } = 0 . 1 5 ~ \mathrm { f m }$ . The solid blue line is the best-fit DOM prediction of the neutron distribution of the same fit. The dash-dotted red line is the neutron distribution of a comparable DOM fit with $R _ { \mathrm { s k i n } } = 0 . 1 4 ~ \mathrm { f m }$ . The dashed black line is the neutron distribution of our previous DOM fit with $R _ { \mathrm { s k i n } } = 0 . 2 5$ fm [25, 52]. The large shaded region is an uncertainty band for the neutron distribution determined from the experimental errors of the neutron data included in the DOM fit using a bootstrap method.

tons and neutrons from $( e , e ^ { \prime } p )$ and $( e , e ^ { \prime } n )$ cross section measurements in $\mathrm { ^ { 1 2 } C }$ , $^ { 2 7 }$ Al, $^ { 5 6 }$ Fe, and $^ \mathrm { 2 0 8 }$ Pb [29]. We note that no such measurements are available for $^ { 4 8 }$ Ca. This nucleus may not conform with expectations as most of the extra neutrons will occupy the valence $f _ { 7 / 2 }$ orbit. As it has been demonstrated in the past such an orbit doesn’t exhibit high-momentum content itself [58, 59]. The shrinking of the neutron distribution must therefore involve more deeply bound contributions thereby leading to a larger presence of high-momentum components.

Notable is the fact that our previous fit [25, 52] with the thick neutron skin had more high-momentum protons than neutrons. The current fit, due to having more neutrons near the center to accommodate a thin skin, has more high-momentum neutrons than protons instead (see Fig. 3 for comparison of old and new fits). Evidently, the additional experimental point provided by the weak form factor has a critical influence on this change of direction, solidifying that such data are crucial to provide a complete picture of the neutron properties in $^ { 4 8 }$ Ca. We note that the additional experimental result involves properties of neutrons below the Fermi energy.

Apparently for protons, the available experimental data already provide sufficient constraints to construct such a complete picture. The most important data for protons include the charge density and proton reaction cross sections as discussed in Ref. [52]. Together with level structure near the Fermi energy and differential cross sections in a large energy domain, a sufficiently complete set of constraints is

![](images/07caaf2b517913ccb2b54e8d85ea81e4479d29d245df5d5eef8246252d02f29f.jpg)  
Figure 3: Momentum distribution of neutrons and protons in $^ { 4 8 } \mathrm { C a }$ . The solid blue and red lines are the proton and neutron momentum distributions, respectively, predicted in the current DOM fit with $R _ { \mathrm { s k i n } } = 0 . 1 5 \ \mathrm { f m }$ . The dashed red line is the neutron distribution predicted in our earlier DOM fit with $R _ { \mathrm { s k i n } } = 0 . 2 5 ~ \mathrm { f n }$ [25, 52].

provided to generate predictive power for proton observables that are not part of the fit. This is illustrated by the success of describing $( e , e ^ { \prime } p )$ cross sections as documented in Refs. [23, 52]. The DOM renders the potential for the outgoing proton at the corresponding energy (100 MeV), the overlap function and its spectroscopic factor. Subsequently these ingredients are employed in the distorted wave impulse approximation of the $( e , e ^ { \prime } p )$ reaction using the updated DWEEPY code [60]. This feature is maintained in the current fit as illustrated in Fig. 4.

The same conclusion cannot be drawn for the neutron data that were originally employed in generating a neutron skin for $^ { 4 8 }$ Ca [25]. Even one extra experimental data point that carries information about the neutron distribution, including but not limited to the weak form factor, can alter the picture quite dramatically. It should also be noted that while total neutron cross sections are available, there are no neutron reaction cross sections and only a very small set of elastic scattering data exists [37]. Expansion of the experimental data set can therefore contribute significantly to the additional information necessary to pin down the neutron properties in $^ { 4 8 }$ Ca. Our experience with protons suggests that neutron reaction cross sections can provide important constraints [52] and it is echoed by the present analysis. In fact, the neutron reaction cross section predictions of the $R _ { \mathrm { s k i n } } = 0 . 1 5$ fm and $R _ { \mathrm { s k i n } } = 0 . 1 4$ fm fits are non-negligibly different, so the addition of these experimental data would help to remove the degeneracy in DOM $F _ { W }$ predictions (see supplementary material).

Another reaction that could help to constrain neutron predictions is the charge exchange reaction, $^ { 4 8 } \mathrm { C a } ( p , n ) ^ { 4 8 }$ Sc, which is largely determined by the isovector component of Lane-like optical potentials [62] (such as the DOM). According to Ref. [62], this link with the isovector potential connects charge exchange reactions to neutron skins. While $^ { 4 8 } \mathrm { C a } ( p , n ) ^ { 4 8 } ,$ Sc data are not included in our fit, we

![](images/147eb4bc3460c19d3c99b3325be464f79a2df7e36e75c26e065ea5215a621206.jpg)

![](images/71ddbebc700a91e60f9eba97f506a5c2ee0ad6f58d37c85f7d327793919334b6.jpg)  
Figure 4: Comparison of DOM-generated (via DWIA) $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ cross sections with experiment at an outgoing proton energy of 100 MeV. The solid line is the DOM prediction of the current fit while the data points are from Ref. [55, 56]. (a) Cross section for the removal of a 0d3/2 proton (leaving the resulting $^ { 3 9 } \mathrm { K }$ nucleus in a $3 / 2 ^ { + }$ state) with a spectroscopic factor of 0.59. (b) Cross section for the removal of a 1s1/2 proton (leaving the resulting $^ { 3 9 } \mathrm { K }$ nucleus in a $1 / 2 ^ { + }$ state) with a spectroscopic factor of 0.6.

calculated charge-exchange cross sections (in the coupledchannel formalism [63]) after completion of our fit to determine its sensitivity to our predicted neutron skin. The negligible difference between the charge-exchange predictions of the previous DOM fit with $R _ { \mathrm { s k i n } } = 0 . 2 5$ fm and the current fit with $R _ { \mathrm { s k i n } } = 0 . 1 5$ fm (see solid and dashed lines in Fig. 5) indicates that these cross sections are not particularly sensitive to the neutron skin. Recent work on the $^ { 4 8 } \mathrm { C a } ( p , n ) ^ { 4 8 }$ Sc reaction [64] yields substantial uncertainties which further suggest that no strong conclusions can be extracted concerning the neutron skin from these data. We note that local optical potentials were employed in the work of Refs. [62, 64] whereas our DOM results are obtained with nonlocal potentials.

The current results for the DOM neutron skins in $^ { 4 8 }$ Ca and $^ { 2 0 8 }$ Pb are summarized in Fig. 6. As demonstrated above, our constrained self-energies for $^ { 4 8 }$ Ca utilize both

![](images/185dc9a4f1297873fe590a86744f3706b4e944e2243e805db147622a011ad063.jpg)  
Figure 5: Comparison of DOM-calculated and experimental charge exchange differential cross sections, $^ { 4 8 } \mathrm { C a } ( p , n ) ^ { 4 8 } \mathrm { S c }$ , at $E _ { \mathrm { l a b } } ~ = ~$ 25, 45, 45 MeV. The points are experimental measurements taken from Ref. [61] while the lines are DOM calculations. Solid lines are from the current fit with $R _ { \mathrm { s k i n } } = 0 . 1 5$ fm while dashed lines are from the previous fit with $R _ { \mathrm { s k i n } } = 0 . 2 5$ fm [25, 52].

scattering and bound-state data for a robust picture of nuclei. Such a fit for $^ { 4 8 }$ Ca now includes the CREX $F _ { W }$ data point resulting in a thin neutron skin, Rskin DOM48 $R _ { \mathrm { s k i n } } ^ { \mathrm { { D O M 4 8 } } } ~ =$ = ±remains at $0 . 1 5 \pm 0 . 0 5$ fm, while the corresponding result for $R _ { \mathrm { s k i n } } ^ { \mathrm { D O M 2 0 8 } } = 0 . 2 5 \pm 0 . 0 5$ fm using the uncer- 208Pb, $^ \mathrm { 2 0 8 }$ sults are represented by the shaded box labeled DOM in Fig. 6. The figure is adapted from Ref. [65] and includes the coupled-cluster result from Ref. [18] as a horizontal band. The vertical band represents the ab initio work reported in Refs. [19, 20]. Relativistic and nonrelativistic mean-field calculations cited in Ref. [65] are represented by squares and circles, respectively. The dashed rectangle is centered on the CREX and PREX-2 results. As made evident by the overlapping of the DOM and CREX-PREX boxes in Fig. 6, the DOM can now simultaneously describe both the thin CREX and thick PREX-2 neutron skins.

In conclusion, we have updated our DOM fit of $^ { 4 8 }$ Ca to reproduce the CREX measurement of the $^ { 4 8 }$ Ca weak form factor and its correspondingly neutron skin. A natural consequence of predicting a thin neutron skin is a neutron distribution with concentrated strength in the interior of the nucleus. This translates to more high-momentum neutrons reversing the hierarchy from the previous thick-skin fit, which could point to some tension with the $n p$ dominance observed in CLAS measurements of asymmetric nuclei [28, 29].

We have demonstrated that the availability of more neutron scattering and bound-state data would allow for a more precise description of $^ { 4 8 }$ Ca and would also elucidate the DOM predictive power for neutron observables, leveling it to its current capability with respect to protons. Furthermore, constraining $F _ { W }$ to only a single $q$ value allows ambiguity in the shape of weak form factor $F _ { W }$ and

![](images/a16f8e85e4143ef625e3fc3d761a629e47e4228ecb5c3b76a566d9acebaddbb1.jpg)  
Figure 6: Figure adapted from Ref. [65]. The dashed rectangle represents the CREX and PREX-2 analyses [14, 15]. The shaded rectangle labeled DOM represents the DOM results for $^ { 2 0 8 } \mathrm { { P b } }$ from Ref. [24] and the updated 48Ca from the current fit. Smaller squares and circles refer to relativistic and nonrelativistic mean-field calculations, respectively, cited in Ref. [65]. The ab initio predictions from Ref. [18] for 48Ca and Refs. [19, 20] for $^ { 2 0 8 } \mathrm { { P b } }$ are represented by horizontal and vertical bands, respectively, labeled ab initio. All uncertainties are reported at the $1 \sigma$ level.

hence the neutron distribution. Ideally, future measurements (such as the Mainz Radius Experiment (MREX)) will be performed at different $q$ values to pinpoint a more detailed shape of $F _ { W }$ and hence the neutron distribution.

This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344 and was supported by the LLNL-LDRD Program under Project No. 24-LW-062. This work was also supported by the U.S. National Science Foundation under grants PHY-1912643 and PHY-2207756.

# References

[1] S. Typel and B. A. Brown, Phys. Rev. C 64, 027302 (2001).   
[2] R. J. Furnstahl and H. Hammer, Phys. Lett. B 531, 203 (2002).   
[3] A. Steiner, M. Prakash, J. Lattimer, and P. Ellis, Physics Reports 411, 325 (2005).   
[4] X. Roca-Maza, M. Centelles, X. Vi˜nas, and M. Warda, Phys. Rev. Lett. 106, 252501 (2011).   
[5] C. J. Horowitz and J. Piekarewicz, Phys. Rev. Lett. 86, 5647 (2001).   
[6] A. W. Steiner, J. M. Lattimer, and E. F. Brown, The Astrophysical Journal 722, 33 (2010).   
[7] B.-A. Li, L.-W. Chen, and C. M. Ko, Physics Reports 464, 113 (2008).   
[8] M. B. Tsang, J. R. Stone, F. Camera, P. Danielewicz, S. Gandolfi, K. Hebeler, C. J. Horowitz, J. Lee, W. G. Lynch, Z. Kohley, R. Lemmon, P. M¨oller, T. Murakami, S. Riordan, X. Roca-Maza, F. Sammarruca, A. W. Steiner, I. Vida˜na, and S. J. Yennello, Phys. Rev. C 86, 015803 (2012).   
[9] J. M. Mammei, C. J. Horowitz, J. Piekarewicz, B. T. Reed, and C. Sfienti, Annual Review of Nuclear and Particle Science (2024), https://doi.org/10.1146/annurev-nucl-102122-024207.   
[10] I. Angeli and K. Marinova, Atomic Data and Nuclear Data Tables 99, 69 (2013).

[11] R. Garcia Ruiz, M. Bissell, B. K., et al., Nature Phys. , 594 (2016).   
[12] C. J. Horowitz, Phys. Rev. C 57, 3430 (1998).   
[13] S. Abrahamyan et al. (PREX Collaboration), Phys. Rev. Lett. 108, 112502 (2012).   
[14] D. Adhikari et al. (PREX Collaboration), Phys. Rev. Lett. 126, 172502 (2021).   
[15] D. Adhikari et al. (CREX Collaboration), Phys. Rev. Lett. 129, 042501 (2022).   
[16] B. T. Reed, F. J. Fattoyev, C. J. Horowitz, and J. Piekarewicz, Phys. Rev. C 109, 035803 (2024).   
[17] P.-G. Reinhard, X. Roca-Maza, and W. Nazarewicz, Phys. Rev. Lett. 129, 232501 (2022).   
[18] G. Hagen, A. Ekstr¨om, C. Forss´en, G. R. Jansen, W. Nazarewicz, T. Papenbrock, K. A. Wendt, S. Bacca, N. Barnea, B. Carlsson, C. Drischler, K. Hebeler, M. Hjorth-Jenson, M. Miorelli, G. Orlandini, A. Schwenk, and J. Simonis, Nature Phys. 12, 186 (2016).   
[19] B. Hu, W. Jiang, T. Miyagi, et al., Nat. Phys. 18, 1196 (2022).   
[20] B. Hu, W. Jiang, T. Miyagi, et al., Nat. Phys. 20, 169 (2024).   
[21] M. H. Mahzoon, R. J. Charity, W. H. Dickhoff, H. Dussan, and S. J. Waldecker, Phys. Rev. Lett. 112, 162503 (2014).   
[22] M. C. Atkinson, Developing Nucleon Self-Energies to Generate the Ingredients for the Description of Nuclear Reactions (Springer, 2020).   
[23] M. C. Atkinson, H. P. Blok, L. Lapik´as, R. J. Charity, and W. H. Dickhoff, Phys. Rev. C 98, 044627 (2018).   
[24] M. C. Atkinson, M. H. Mahzoon, M. A. Keim, B. A. Bordelon, C. D. Pruitt, R. J. Charity, and W. H. Dickhoff, Phys. Rev. C 101, 044303 (2020).   
[25] M. H. Mahzoon, M. C. Atkinson, R. J. Charity, and W. H. Dickhoff, Phys. Rev. Lett. 119, 222503 (2017).   
[26] C. D. Pruitt, R. J. Charity, L. G. Sobotka, M. C. Atkinson, and W. H. Dickhoff, Phys. Rev. Lett. 125, 102501 (2020).   
[27] C. D. Pruitt, R. J. Charity, L. G. Sobotka, J. M. Elson, D. E. M. Hoff, K. W. Brown, M. C. Atkinson, W. H. Dickhoff, H. Y. Lee, M. Devlin, N. Fotiades, and S. Mosby, Phys. Rev. C 102, 034601 (2020).   
[28] K. S. Egiyan et al. (CLAS Collaboration), Phys. Rev. Lett. 96, 082501 (2006).   
[29] M. Duer et al., Nature 560, 617 (2018).   
[30] A. Rios, A. Polls, and W. H. Dickhoff, Phys. Rev. C 79, 064308 (2009).   
[31] A. Rios, A. Polls, and W. H. Dickhoff, Phys. Rev. C 89, 044303 (2014).   
[32] W. H. Dickhoff and D. Van Neck, Many-Body Theory Exposed!, 2nd edition (World Scientific, New Jersey, 2008).   
[33] C. Mahaux and R. Sartor, “Single-particle motion in nuclei,” in Advances in Nuclear Physics, edited by J. W. Negele and E. Vogt (Springer US, Boston, MA, 1991) pp. 1–223.   
[34] F. Perey and B. Buck, Nuclear Physics 32, 353 (1962).   
[35] R. J. Charity, L. G. Sobotka, and W. H. Dickhoff, Phys. Rev. Lett. 97, 162503 (2006).   
[36] R. J. Charity, J. M. Mueller, L. G. Sobotka, and W. H. Dickhoff, Phys. Rev. C 76, 044314 (2007).   
[37] J. M. Mueller, R. J. Charity, R. Shane, L. G. Sobotka, S. J. Waldecker, W. H. Dickhoff, A. S. Crowell, J. H. Esterline, B. Fallin, C. R. Howell, C. Westerfeldt, M. Youngs, B. J. Crowe, and R. S. Pedroni, Phys. Rev. C 83, 064605 (2011).   
[38] W. H. Dickhoff, D. Van Neck, S. J. Waldecker, R. J. Charity, and L. G. Sobotka, Phys. Rev. C 82, 054306 (2010).   
[39] S. J. Waldecker, C. Barbieri, and W. H. Dickhoff, Phys. Rev. C 84, 034616 (2011).   
[40] H. Dussan, S. J. Waldecker, W. H. Dickhoff, H. M¨uther, and A. Polls, Phys. Rev. C 84, 044319 (2011).   
[41] W. H. Dickhoff, R. J. Charity, and M. H. Mahzoon, J. of Phys. G: Nucl. and Part. Phys. 44, 033001 (2017).   
[42] I. Brida, S. C. Pieper, and R. B. Wiringa, Phys. Rev. C 84, 024319 (2011).   
[43] M. H. Mahzoon, Implications of a Fully Nonlocal Implementation of the Dispersive Optical Model, Ph.D. thesis, Washington

University in St. Louis (2015).   
[44] M. C. Atkinson, W. H. Dickhoff, M. Piarulli, A. Rios, and R. B. Wiringa, Phys. Rev. C 102, 044333 (2020).   
[45] P. Descouvemont and D. Baye, Rep. Prog. Phys. 73, 036301 (2010).   
[46] D. Baye, Physics Reports 565, 1 (2015), the Lagrange-mesh method.   
[47] R. Pohl et al., Nature 466, 213 (2010).   
[48] A. A. Filin, V. Baru, E. Epelbaum, H. Krebs, D. M¨oller, and P. Reinert, Phys. Rev. Lett. 124, 082501 (2020).   
[49] C. J. Horowitz and J. Piekarewicz, Phys. Rev. C 86, 045503 (2012).   
[50] V. M. Galitski and A. B. Migdal, Sov. Phys. JETP 7, 96 (1958).   
[51] R. J. Charity and C. D. Pruitt, private communication (2022).   
[52] M. C. Atkinson and W. H. Dickhoff, Phys. Lett. B 798, 135027 (2019).   
[53] H. de Vries, C. W. de Jager, and C. de Vries, Nucl. Data Tables 36, 495 (1987).   
[54] R. B. Wiringa, R. Schiavilla, S. C. Pieper, and J. Carlson, Phys. Rev. C 89, 024305 (2014).   
[55] G. Kramer, H. Blok, and L. Lapik´as, Nuclear Physics A 679, 267 (2001).   
[56] G. J. Kramer, Ph.D. thesis, Universiteit van Amsterdam, Amsterdam (1990).   
[57] O. Hen, G. A. Miller, E. Piasetzky, and L. B. Weinstein, Rev. Mod. Phys. 89, 045002 (2017).   
[58] I. Bobeldijk, M. Bouwhuis, D. G. Ireland, C. W. de Jager, E. Jans, N. de Jonge, W.-J. Kasdorp, J. Konijn, L. Lapik´as, J. J. van Leeuwe, R. L. J. van der Meer, G. J. L. Nooren, E. Passchier, M. Schroevers, G. van der Steenhoven, J. J. M. Steijger, J. A. P. Theunissen, M. A. van Uden, H. de Vries, R. de Vries, P. K. A. de Witt Huberts, H. P. Blok, H. B. van den Brink, G. E. Dodge, M. N. Harakeh, W. H. A. Hesselink, N. Kalantar-Nayestanaki, A. Pellegrino, C. M. Spaltro, J. A. Templon, R. S. Hicks, J. J. Kelly, and C. Marchand, Phys. Rev. Lett. 73, 2684 (1994).   
[59] H. M¨uther and W. H. Dickhoff, Phys. Rev. C 49, R17 (1994).   
[60] C. Giusti, A. Meucci, F. D. Pacati, G. Co’, and V. De Donno, Phys. Rev. C 84, 024615 (2011).   
[61] R. R. Doering, D. M. Patterson, and A. Galonsky, Phys. Rev. C 12, 378 (1975).   
[62] P. Danielewicz, P. Singh, and J. Lee, Nucl. Phys. A 958, 147 (2017).   
[63] D. T. Khoa, H. S. Than, and D. C. Cuong, Phys. Rev. C 76, 014603 (2007).   
[64] A. J. Smith, C. Hebborn, F. M. Nunes, and R. G. T. Zegers, Phys. Rev. C 110, 034602 (2024).   
[65] C. J. Horowitz, K. S. Kumar, and R. Michaels, Eur. Phys. A 50, 48 (2014).