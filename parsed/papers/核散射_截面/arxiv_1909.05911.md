# Investigating the link between proton reaction cross sections and the quenching of proton spectroscopic factors in $^ { 4 8 }$ Ca

M. C. Atkinson $^ { \mathrm { a , b , * } }$ , W. H. Dickhoffa

aDepartment of Physics, Washington University in St. Louis, MO 63130 USA bTheory Group, TRIUMF, BC V6T 2A3, Canada

# Abstract

The nucleon self-energies of $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca are determined using a nonlocal dispersive optical model (DOM). By enforcing the dispersion relation connecting the real and imaginary part of the self-energy, scattering and structure data are used to constrain these self-energies. The ability to calculate both bound and scattering states simultaneously puts these selfenergies in a unique position to consistently describe exclusive knockout reactions such as $( e , e ^ { \prime } p )$ . The present analysis reveals the importance of high-energy proton reaction cross-section data in constraining spectroscopic factors required for the description of the $( e , e ^ { \prime } p )$ cross sections. In particular, it is imperative that high-energy proton reaction cross-section data are measured for $^ { 4 8 }$ Ca in the near future so that the quenching of the spectroscopic factors in the $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ reaction can be unambiguously constrained using the DOM. Measurements of proton reaction cross sections in inverse kinematics employing rare isotope beams with large neutron excess will provide corresponding constraints on proton spectroscopic factors for exotic nuclei. Moreover, DOM generated spectral functions indicate that the quenching of spectroscopic factors compared to $^ { 4 0 }$ Ca is not only due to long-range correlation, but also partly due to the increase in high-momentum protons in $^ { 4 8 }$ Ca on account of the strong neutron-proton interaction. Single-particle momentum distributions of protons and neutrons in $^ { 4 8 }$ Ca calculated from these spectral functions confirm that neutron excess causes a higher fraction of high-momentum protons than neutrons.

Keywords: Nuclear, Theory, Many-Body, Reactions, Structure, Spectroscopic Factor

# 1. Introduction

Independent particle models (IPMs) provide a simplified picture of the nucleus in which correlations are neglected and all orbitals are $1 0 0 \%$ filled up to the Fermi level according to the Pauli principle and those above it are empty. However, due to residual interactions there is depletion of orbitals below the Fermi energy and filling of those above it. The best tool to study this experimentally is the $( e , e ^ { \prime } p )$ reaction [1–7]. At sufficiently high electron energy and momentum transfer, the proton can be knocked out with enough energy such that a description within the distorted-wave impulse approximation (DWIA) can be expected to be applicable, so that depletion (and also filling) of orbits can be studied [1, 2]. In the typical application of the DWIA to the $( e , e ^ { \prime } p )$ reaction, a fully occupied IPM proton wave function is used which then requires a scaling factor of about 0.6-0.7 to describe the overall magnitude of the data [6]. This scaling factor, usually referred to as the (reduced) spectroscopic factor, corresponds to the normalization of the overlap function between the target ground state and low-lying single-hole states. Furthermore, the

data show that additional removal strength with essentially the same overlap function is located at nearby energies, providing clear evidence of the fragmentation of the single-particle strength [1, 8].

This depletion of orbitals is closely linked with elastic scattering observables. Depletion becomes inevitable with the inclusion of a complex absorptive potential to account for inelastic processes in the description of elastic scattering. A non-zero imaginary component of the optical potential at positive energies pulls strength away from the IPM orbitals. The reaction (total inelastic) cross section is the most sensitive to the imaginary part of the optical potential, so it largely determines the depletion of these orbitals. In this way, the spectroscopic factors of orbitals are closely linked with the reaction cross section. Thus, a proper description of $( e , e ^ { \prime } p )$ data requires an optical potential that reproduces proton reaction cross-section data. In Ref. [9], a nonlocal dispersive optical model (DOM) which simultaneously describes both bound and scattering states was used to consistently provide all ingredients, including spectroscopic factors, for an accurate DWIA description of $^ { 4 0 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 3 9 } \mathrm { K }$ data.

A systematic study in Ref. [10] summarized results for reduction factors obtained from nucleon-knockout reactions for a wide variety of nuclei. The analysis employed results from shell-model calculations demonstrat-

ing that the removal of minority nucleons from nuclei with larger asymmetry leads to proportionally quenched reduction factors while nucleons of the majority species are less quenched. This is not consistent with corresponding results of transfer reactions reviewed in Ref. [11] or the single-nucleon removal experiments recently reported in Refs. [12, 13]. At this time no clear consensus has been reached on this intriguing difference. To investigate this discrepancy, a consistent DWIA analysis of $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ is performed using a nonlocal DOM description similar to the one reported in Ref. [9] for $^ { 4 0 }$ Ca. Comparing the DOM calculated spectroscopic factors of $^ { 4 8 }$ Ca and $^ { 4 0 }$ Ca will provide more information on the quenching of proton spectroscopic factors when neutrons are added.

The theoretical interpretation of the Nikhef $( e , e ^ { \prime } p )$ results, reviewed in Refs. [7, 14], has mainly been concerned with the explanation of the reduction in the spectroscopic strength to 60-70% of the IPM value. While the main reduction of strength can be attributed to long-range correlations (LRC) which are manifest in the reaction cross section at lower energy, it has been well documented that additional short-range and tensor correlations (SRC) are responsible for a 10-15% depletion of the IPM value [14]. These SRCs give rise to high-momentum nucleon pairs which have been measured with inclusive $( e , e ^ { \prime } )$ inelastic scattering by the Continuous Electron Beam Accelerator Facility (CEBAF) Large Acceptance Spectrometer (CLAS) collaboration at Jefferson Lab in $^ 3$ He, 4He, $\mathrm { ^ { 1 2 } C }$ , and $^ { 5 6 }$ Fe [15]. Asymmetric nuclear-matter calculations for various realistic interactions have documented the importance of the tensor force in generating a larger depletion of the proton Fermi sea compared to the neutron one when protons are in the minority, thus generating relatively more high-momentum protons than neutrons [16, 17]. Realistic many-body calculations of low- $A$ nuclei using variational Monte Carlo (VMC) techniques also reveal that the majority of this high-momentum content comes from the tensor force in the nucleon-nucleon interaction [18]. This nonnegligible fraction of high-momentum nucleons is further proof that there are correlations beyond the mean-field in nuclei. This high-momentum content can be calculated in the DOM framework, which provides another means of investigating the quenching of the spectroscopic factor and many-body correlations in $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca.

# 2. Analysis of $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ reaction employing the nonlocal DOM

The nonlocal dispersive-optical-model (DOM) uses both bound and scattering data to constrain the nucleon selfenergy $\Sigma _ { \ell j }$ for a given nucleus. This self-energy is a complex and nonlocal potential that unites the nuclear structure and reaction domains [19, 20]. The DOM was originally developed by Mahaux and Sartor [19], employing local real and imaginary potentials connected through dispersion relations. However, only with the introduction of nonlocality can realistic self-energies be obtained [20, 21].

The Dyson equation then determines the single-particle propagator or Green’s function $G _ { \ell j } ( \boldsymbol { r } , \boldsymbol { r } ^ { \prime } ; E )$ from which bound-state and scattering observables can be deduced. The hole spectral density for energies below the Fermi energy $\varepsilon _ { F }$ is obtained from the single-particle propagator in the following way,

$$
S _ {\ell j} ^ {h} (\alpha , \beta ; E) = \frac {1}{\pi} \operatorname {I m} G _ {\ell j} (\alpha , \beta ; E). \tag {1}
$$

The diagonal element of Eq. (1) is known as the (hole) spectral function identifying the probability density for the removal of a single-particle state with quantum numbers $\alpha \ell j$ at energy $E$ . The spectral strength for a given $\ell j$ combination can be found by summing (integrating) the spectral function according to

$$
S _ {\ell j} (E) = \sum_ {\alpha} S _ {\ell j} (\alpha , \alpha ; E). \tag {2}
$$

The spectral strength $S _ { \ell j } ( E )$ is the contribution at energy $E$ to the occupation from all orbitals with $\ell j$ . It reveals that the strength for these shells is fragmented, rather than concentrated at the independent-particle model (IPM) energy levels. Figure 1 shows the spectral strength for a representative set of neutron shells in $^ { 4 8 }$ Ca that would be considered bound in the IPM. The peaks in Fig. 1 correspond to the binding energies of the appropriate IPM orbitals. For example, the $\mathrm { p } { \frac { 3 } { 2 } }$ spectral function in Fig. 1 has two peaks, one below $\varepsilon _ { F }$ corresponding to the $0 \mathrm { p } { \frac { 3 } { 2 } }$ quasihole state, and one above $\varepsilon _ { F }$ corresponding to the $\mathrm { 1 p _ { 2 } ^ { 3 } }$ quasiparticle state. Comparing the neutron spectral functions in Fig. 1 with the proton spectral functions in Fig. 2 reveals that the proton peaks are broader at a similar distance from the corresponding Fermi energy than those of the neutrons. The larger broadening of these peaks is a consequence of the protons being more correlated than the neutrons as determined by the fit to all relevant experimental data generating larger absorptive potentials for protons than neutrons at all energies.

![](images/771425a6efd0217dff0dee3153a60baf1d5870513cb2b33d5ed91548db78b2a5.jpg)  
Figure 1: Neutron spectral functions of a representative set of $\ell j$ shells in $^ { 4 8 }$ Ca. The particle states are distinguished from the hole states by the dotted line representing the Fermi energy.

![](images/03e6f7401ce03b7e4daf54deb2b05e7269803b851879dcc5181feead2859f09c.jpg)  
Figure 2: Proton spectral functions of a representative set of $\ell j$ shells in $^ { 4 8 }$ Ca. The particle states are differentiated from the hole states by the dotted line representing the Fermi energy.

The occupation of specific orbitals characterized by $n$ with wave functions that are normalized to 1 can be obtained from Eq. (1) by folding in the corresponding wave functions [22],

$$
S _ {\ell j} ^ {n -} (E) = \sum_ {\alpha , \beta} \left[ \phi_ {\ell j} ^ {n} (\alpha) \right] ^ {*} S _ {\ell j} ^ {h} (\alpha , \beta ; E) \phi_ {\ell j} ^ {n} (\beta). \tag {3}
$$

Note that this representation of the spectral strength involves off-diagonal elements of the propagator. The wave functions used in Eq. (3) are the solutions of the Dyson equation that correspond to discrete bound states with one proton/neutron removed. Such quasihole wave functions can be obtained from the nonlocal Schr¨odinger-like equation disregarding the imaginary part

$$
\sum_ {\gamma} \langle \alpha | T _ {\ell} + \operatorname {R e} \Sigma_ {\ell j} ^ {*} (\varepsilon_ {n} ^ {-}) | \gamma \rangle \psi_ {\ell j} ^ {n} (\gamma) = \varepsilon_ {n} ^ {-} \psi_ {\ell j} ^ {n} (\alpha), \tag {4}
$$

where $\langle \alpha | T _ { \ell } | \gamma \rangle$ is the kinetic-energy matrix element, including the centrifugal term. These wave functions correspond to overlap functions

$$
\psi_ {\ell j} ^ {n} (\alpha) = \left\langle \Psi_ {n} ^ {A - 1} \right| a _ {\alpha \ell j} \left| \Psi_ {0} ^ {A} \right\rangle , \quad \varepsilon_ {n} ^ {-} = E _ {0} ^ {A} - E _ {n} ^ {A - 1}. \tag {5}
$$

Such discrete solutions to Eq. (5) exist where there is no imaginary part of the self-energy, so near the Fermi energy. The normalization for these wave functions is the spectroscopic factor, which is given by [23]

$$
\mathcal {Z} _ {\ell j} ^ {n} = \left(1 - \frac {\partial \Sigma_ {\ell j} ^ {*} (\alpha_ {q h} , \alpha_ {q h} ; E)}{\partial E} \Big | _ {\varepsilon_ {n} ^ {-}}\right) ^ {- 1}, \tag {6}
$$

where $\alpha _ { q h }$ corresponds to the quasihole state that solves Eq. (4). This corresponds to the spectral strength at the quasihole energy $\varepsilon _ { n } ^ { - }$ , represented by a delta function. The quasihole peaks in Fig. 2 get narrower as the levels approach $\varepsilon _ { F }$ , which is a consequence of the imaginary part of the irreducible self-energy decreasing when approaching $\varepsilon _ { F }$ . In fact, the last mostly occupied proton level in Fig. 2 $( 1 \mathrm { s } \frac { \mathrm { 1 } } { 2 }$ ) has a spectral function that is essentially a delta function peaked at its energy level, where the imaginary

part of the self-energy vanishes. For these orbitals, the strength of the spectral function at the peak corresponds to the spectroscopic factor in Eq. (6). Note that because of the presence of imaginary parts of the self-energy at other energies, there is also strength located there, thus the spectroscopic factor will be less than one and also less than the occupation probability.

Previously, a fit of $^ { 4 8 }$ Ca was published in Ref. [24], quoting a neutron skin of $\Delta r _ { n p } = 0 . 2 4 9 \pm 0 . 0 2 3 \ .$ fm. However, just as in the case of $^ { 4 0 }$ Ca in Refs. [9, 20], the proton reaction cross section is underestimated at 200 MeV. While there are no experimental data for $^ { 4 8 }$ Ca at these energies, there is a data point at 700 MeV of the proton reaction cross section of $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca [25]. Comparing the available data for $\sigma _ { \mathrm { r e a c t } } ^ { 4 0 } ( E )$ at 200 MeV and 700 MeV reveals that the reaction cross section essentially stays flat between these energies. It is reasonable to expect that $\sigma _ { \mathrm { r e a c t } } ^ { 4 8 } ( E )$ assumes the same shape as $\sigma _ { \mathrm { r e a c t } } ^ { 4 0 } ( E )$ at high energies. Thus, data points are extrapolated from the $^ { 4 0 }$ Ca experimental data at energies above 100 MeV by applying the ratio that is seen in the 700 MeV data for ${ \sigma } _ { \mathrm { r e a c t } } ^ { 4 8 } ( E ) / { \sigma } _ { \mathrm { r e a c t } } ^ { 4 0 } ( E )$ , see Table 1. The extrapolated points are shown as blue squares in Fig. 3 while the updated fit is represented with the solid curve. The remainder of the fit did not change significantly from Ref. [24]. The parameterization of the $^ { 4 8 } \mathrm { C a }$ self-energy as well as the updated parameters are presented in the supplementary material.

Table 1: Experimental proton reaction cross-section data at 700 MeV taken from Ref. [25].   

<table><tr><td>Nucleus</td><td>40Ca</td><td>48Ca</td><td>48Ca/40Ca</td></tr><tr><td>σreact(E)</td><td>614 ± 38 mb</td><td>736 ± 46 mb</td><td>1.19</td></tr></table>

![](images/bbdce2108a1bf4f294c2266fe34a2965c66269f8321d1292ae04e7ae75e115c8.jpg)  
Figure 3: Proton reaction cross sections for $^ { 4 8 } \mathrm { C a }$ and $^ { 4 0 } \mathrm { C a }$ . The solid line represents the current $^ { 4 8 } \mathrm { C a }$ fit while the dashed line depicts the previous $^ { 4 8 } \mathrm { C a }$ fit [24]. The dotted line represents the $^ { 4 0 } \mathrm { C a }$ fit from Ref. [9]. The circular points are the same experimental data used in Ref. [26] and were included in the previous fit. The square points are extrapolated from the $\sigma _ { \mathrm { r e a c t } } ^ { 4 0 } ( E )$ experimental data points at the corresponding energies. The extrapolation is explained in the main text.

To analyze the proton spectroscopic factors, the $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ cross section is calculated using the DWIA

following the same procedure detailed in Ref. [9] for $^ { 4 0 }$ Ca. In the DWIA, the $( e , e ^ { \prime } p )$ cross section is calculated using a distorted wave to represent the outgoing proton, a proton bound-state wave function (BSWF) representing the struck proton, and the normalization of the BSWF corresponding to the spectroscopic factor. All of these quantities are directly provided by the DOM self-energy. The experimental data of the $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ reaction were obtained in parallel kinematics for outgoing proton kinetic energies of $T _ { p } = 1 0 0$ MeV at Nikhef and previously published in Ref. [27]. Just as in Ref. [9], the DOM spectroscopic factors need to be renormalized by incorporating the observed experimental fragmentation of the strength near the Fermi energy that is not yet included in the DOM selfenergy. The experimental strength distributions for the $\ell = 0$ and the $\ell = 2$ excitations of $^ { 4 7 } \mathrm { K }$ are shown in Fig. 4, overlaid with the corresponding DOM spectral functions calculated from Eq. (3). Analogously to the $^ { 4 0 }$ Ca calculation, the distributions in Fig. 4 are used to renormalize the DOM spectroscopic factors in the following way,

$$
\frac {\mathcal {Z} _ {F} ^ {\mathrm {D O M}}}{\int d E S ^ {\mathrm {D O M}} (E)} = \frac {\mathcal {Z} _ {F} ^ {\exp}}{\int d E S ^ {\exp} (E)}. \tag {7}
$$

This scaling results in a reduction from 0.64 to 0.55 for the $\mathrm { 1 s } { \frac { 1 } { 2 } }$ orbital and from 0.60 to 0.58 for the $\mathrm { 0 d } _ { 2 } ^ { 3 }$ orbital. These values are in good agreement with originally published spectroscopic factors [27], as seen in Table 2. The uncertainties in the values of the spectroscopic factors were determined using the same bootstrap method discussed in the previous DOM analysis of $^ { 4 0 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 3 9 } \mathrm { K }$ [9].

Table 2: Comparison of spectroscopic factors in $^ { 4 8 } \mathrm { C a }$ deduced from the previous analysis [27] using the Schwandt optical potential [28] to the normalization of the corresponding overlap functions obtained in the present analysis from the DOM including an error estimate as described in the text.   

<table><tr><td>Z</td><td>0d3/2</td><td>1s1/2</td></tr><tr><td>Ref. [27]</td><td>0.57 ± 0.04</td><td>0.54 ± 0.04</td></tr><tr><td>DOM</td><td>0.58 ± 0.03</td><td>0.55 ± 0.03</td></tr></table>

Using the resulting renormalized spectroscopic factors produces the momentum distributions shown in Fig. 5. Thus, the smaller spectroscopic factors in $^ { 4 8 }$ Ca are consistent with the experimental cross sections of the $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ reaction. The comparison of $\mathcal { Z } _ { 4 8 }$ and $\mathcal { Z } _ { 4 0 }$ in Table 3 reveals that both orbitals experience a reduction. This indicates that strength from the spectroscopic factors is pulled to the continuum in $S ( E )$ when eight neutrons are added to $^ { 4 0 }$ Ca. Thus, the stronger coupling to surface excitations in $^ { 4 8 }$ Ca, demonstrated by the larger proton reaction cross section when compared to $^ { 4 0 }$ Ca (see Fig. 3), strongly contributes to the quenching of the proton spectroscopic factor. It is important to note how crucial the extrapolated high-energy proton reaction crosssection data are in drawing these conclusions. Without

![](images/7aab34c35c91a30f8c64d361e078d9e13ea27b115913dfe4005cd8eb46feeb6c.jpg)

![](images/caf50b28c989cc91a10e6fb24565cb11af8b546eabef9a37b7b631c1133a2952.jpg)  
Figure 4: Spectral strength as a function of excitation energy in 48Ca. The solid lines are DOM spectral functions for (a) the $\mathrm { 1 s } { \frac { 1 } { 2 } }$ and (b) the $\mathrm { 0 d } { \frac { 3 } { 2 } }$ proton orbitals. The histograms are the excitation energy spectra in $^ { 3 9 } \mathrm { K }$ extracted from the $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ experiment [8, 27]. The peaks in the DOM curves and experimental data correspond to the quasihole energies of the protons in $^ { 4 0 }$ Ca. The experimental spectrum in (b) is the isolated $\mathrm { 0 d } { \frac { 3 } { 2 } }$ orbital.

them, there is no constraint for the strength of the spectral function at large positive energies, which could result in no quenching of the spectroscopic factors of $^ { 4 8 }$ Ca due to the sum rule that requires the strength to integrate to one when all energies are considered [22, 23].

Table 3: Comparison of DOM spectroscopic factors in $^ { 4 8 }$ Ca and $^ { 4 0 } \mathrm { C a }$ . These factors have not been renormalized and represent the aggregate strength near the Fermi energy.   

<table><tr><td>Z</td><td>0d3/2</td><td>1s1/2</td></tr><tr><td>40Ca</td><td>0.71 ± 0.04</td><td>0.74 ± 0.03</td></tr><tr><td>48Ca</td><td>0.60 ± 0.03</td><td>0.64 ± 0.03</td></tr></table>

In addition to the depletion of the spectroscopic factor due to LRC, strength is also pulled to continuum energies due to SRC. It was stated earlier that a large portion of high-momentum content is caused by the tensor force in the nucleon-nucleon interaction. In particular, the tensor force preferentially acts on pairs of neutrons and protons ( $n p$ pairs) with total spin $S = 1$ . This phenomenon is known as np dominance [29], and is demonstrated by a factor of 20 difference between the number of observed $n p$

![](images/ea4aafee2412c549d132d2c4a2d60e837d5ced3db6bee85acc285d0677f367d8.jpg)

![](images/df4112a5c923a62861d8e5057ea957bc3d81e77db7e73909ec06cc12b6420af0.jpg)  
Figure 5: $^ { 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 4 7 } \mathrm { K }$ spectral functions in parallel kinematics at an outgoing proton kinetic energy of 100 MeV. The solid line is the calculation using the DOM ingredients while the points are from the experiment detailed in Ref. [27]. (a) Distribution for the removal of the $\mathrm { 1 s } { \frac { 1 } { 2 } }$ proton. The curve contains the DWIA for the $1 / 2 ^ { + }$ ground state using the DOM generated spectroscopic factor of 0.55 (renormalized using Eq. (7)) (b) Distribution for the removal of the $\mathrm { 0 d } { \frac { 3 } { 2 } }$ with a DOM generated spectroscopic factor of 0.58 (renormalized using Eq. (7)) for the $3 / 2 ^ { + }$ excited state at 0.36 MeV.

SRC pairs and the number of observed $p p$ and nn SRC pairs in exclusive $( e , e ^ { \prime } p p )$ and $( e , e ^ { \prime } p )$ cross section measurements of $\mathrm { ^ { 1 2 } C }$ , $^ { 2 7 }$ Al, $^ { 5 6 }$ Fe, and $^ \mathrm { 2 0 8 }$ Pb [29]. The dominance of $n p$ SRC pairs would imply that the number of high-momentum protons observed in a nucleus is dependent on how many neutrons it contains. More specifically, one would expect that the high-momentum content of protons would increase with neutron excess since there are more neutrons available to make np SRC pairs. The CLAS collaboration confirmed this asymmetry dependence by measuring the high-momentum content of protons and neutrons from $( e , e ^ { \prime } p )$ and $( e , e ^ { \prime } n )$ cross section measurements in $\mathrm { ^ { 1 2 } C }$ , $^ { 2 7 }$ Al, $^ { 5 6 }$ Fe, and $^ \mathrm { 2 0 8 }$ Pb [30].

This effect can be studied by comparing the DOM generated momentum distributions for $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca, since the only difference between them is the eight additional neutrons in $^ { 4 8 }$ Ca mainly filling the $\mathrm { 0 f { \frac { 7 } { 2 } } }$ shell. The momentum distributions for $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca are shown in Fig. 6. It is clear that the $^ { 4 8 }$ Ca proton momentum distribution (solid blue line) has more high-momentum content than the $^ { 4 0 }$ Ca proton momentum distribution (dashed blue line). Furthermore, since the number of protons does not change between $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca, the added high-momentum con-

![](images/4b2eae43cf2abda8a101f76712605919a34c210754a1d9064bc5c63ac7f89971.jpg)  
Figure 6: Comparison of DOM calculated momentum distributions of protons (blue) and neutrons (red) in $^ { 4 8 } \mathrm { C a }$ (solid) and $^ { 4 0 } \mathrm { C a }$ (dashed). The dotted line marks the value used for $k _ { F }$ .

tent in the tail of $^ { 4 8 } \mathrm { C a }$ is accounted for by a reduction of the distribution in the $k < k _ { F }$ region. Turning now to the neutrons in Fig. 6, the 48Ca momentum distribution is larger in magnitude than the $^ { 4 0 } \mathrm { C a }$ distribution for $k < k _ { F }$ . This is not surprising since there are now eight more neutrons which are dominated by low-momentum content. The high-momentum content of the neutrons in 40Ca decreases from $1 4 . 7 \%$ to $1 2 . 6 \%$ when eight neutrons are added to form $^ { 4 8 }$ Ca while the high-momentum content of the protons increases from $1 4 . 0 \%$ to $1 4 . 6 \%$ . The effects of the asymmetry of $^ { 4 8 }$ Ca on high-momentum content are evident in the fact that there are now significantly more high-momentum protons than neutrons. Both the increase in proton high-momentum content and the decrease in neutron high-momentum content are qualitatively consistent with the CLAS measurements of neutron-rich nuclei [30] and support the $n p$ -dominance picture as predicted in Refs. [16, 17]. Note that at this stage of the DOM development, no attempt has been made to quantitatively account for the CLAS observations.

Another manifestation of the more correlated protons can be seen in the spectral functions of Figs. 1 and 2. The broader peaks of the proton spectral functions indicate that the protons are more correlated. Furthermore, increased proton high-momentum content in $^ { 4 8 }$ Ca comes from generating more strength in the continuum of the hole spectral function than in $^ { 4 0 }$ Ca. To compare how strength is distributed over energy in $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca, the sum over all $\ell j$ shells can be performed,

$$
S (E) = \sum_ {\ell j} ^ {\infty} (2 j + 1) S _ {\ell j} (E),
$$

where $S _ { \ell j } ( E )$ are defined in Eq. (2). The summed spectral function of $^ { 4 8 }$ Ca has more strength than that of $^ { 4 0 }$ Ca at large negative energies. In order to conserve proton number, an increase in strength at continuum energies in $S ( E )$ of $^ { 4 8 }$ Ca must be compensated by a decrease in strength from energies close to the proton Fermi energy in $^ { 4 8 }$ Ca. In

particular, this contributes to the quenching of the spectroscopic factors of the $\mathrm { 0 d } { \frac { 3 } { 2 } }$ and $\mathrm { 1 s } { \frac { \mathrm { 1 } } { \mathrm { 2 } } }$ orbitals, before renormalization (see Eq. (7)), in $^ { 4 8 }$ Ca from the values for $^ { 4 0 }$ Ca as can be seen in Table 3. In this way, the spectroscopic factor provides a link between the low-momentum knockout experiments done at Nikhef and the high-momentum knockout experiments done at JLAB by the CLAS collaboration.

# 3. Summary

The DOM analysis of the $^ { 4 0 , 4 8 } \mathrm { C a } ( e , e ^ { \prime } p ) ^ { 3 9 , 4 7 } \mathrm { K }$ reactions demonstrates that the addition of eight neutrons to $^ { 4 0 }$ Ca leads to a quenching of the proton spectroscopic factors, in agreement with the trend observed in Ref. [10] but with a reduced slope. Some form of quenching is inevitable if one accepts the $n p$ dominance picture, since the added neutrons cause the protons to become more correlated. The increase in the high-momentum content of protons in $^ { 4 8 }$ Ca is consistent with the $n p$ dominance picture, hence it contributes to the quenching of the spectroscopic factors. Additionally, the increased proton reaction cross section of $^ { 4 8 }$ Ca at all energies compared to $^ { 4 0 }$ Ca leads to more depletion, which also contributes to the observed quenching. The proton reaction cross section plays a delicate role in determining the spectroscopic factor. While in the case of $^ { 4 8 }$ Ca the lack of proton reaction cross-section data points at energies between 100-200 MeV was compensated for by modifying the corresponding $^ { 4 0 }$ Ca data points, precise measurements of the proton reaction cross sections at these energies are crucial in constraining spectroscopic factors. Such measurements in inverse kinematics with rare isotopes can further help understand the behavior of spectroscopic factors away from the valley of stability.

# Acknowledgements

This work was supported by the U.S. National Science Foundation under grants PHY-1613362 and PHY-1912643.

# References

[1] G. J. Kramer, H. P. Blok, J. F. J. van den Brand, H. J. Bulten, R. Ent, E. Jans, J. B. J. M. Lanen, L. Lapik´as, H. Nann, E. N. M. Quint, G. van der Steenhoven, P. K. A. De Witt Huberts, G. J. Wagner, Phys. Lett. B 227 (2) (1989) 199 – 203. doi:10.1016/S0370-2693(89)80022-X.   
[2] J. W. A. den Herder, H. P. Blok, E. Jans, P. H. M. Keizer, L. Lapik´as, E. N. M. Quint, G. van der Steenhoven, P. K. A. de Witt Huberts, Nucl. Phys. A 490 (3) (1988) 507 – 555. doi: 10.1016/0375-9474(88)90012-7.   
[3] P. K. A. de Witt Huberts, Journal of Physics G: Nuclear and Particle Physics 16 (4) (1990) 507–544. doi:10.1088/ 0954-3899/16/4/004.   
[4] A. E. L. Dieperink, P. K. A. Huberts, Annual Review of Nuclear and Particle Science 40 (1) (1990) 239–284. doi:10.1146/ annurev.ns.40.120190.001323.   
[5] I. Sick, P. K. A. de Witt Huberts, Comm. Nucl. Part. Phys. 20 (1991) 177.

[6] L. Lapik´as, Nuclear Physics A 553 (1993) 297 – 308. doi:10. 1016/0375-9474(93)90630-G.   
[7] V. R. Pandharipande, I. Sick, P. K. A. d. Huberts, Rev. Mod. Phys. 69 (1997) 981–991. doi:10.1103/RevModPhys.69.981.   
[8] G. J. Kramer, Ph.D. thesis, Universiteit van Amsterdam, Amsterdam (1990).   
[9] M. C. Atkinson, H. P. Blok, L. Lapik´as, R. J. Charity, W. H. Dickhoff, Phys. Rev. C 98 (2018) 044627. doi:10.1103/ PhysRevC.98.044627.   
[10] J. A. Tostevin, A. Gade, Phys. Rev. C 90 (2014) 057602. doi: 10.1103/PhysRevC.90.057602.   
[11] W. H. Dickhoff, R. J. Charity, Progress in Particle and Nuclear Physics 105 (2019) 252 – 299. doi:10.1016/j.ppnp.2018.11. 002.   
[12] L. Atar, et al., Phys. Rev. Lett. 120 (2018) 052501. doi:10. 1103/PhysRevLett.120.052501.   
[13] S. Kawase, et al., Progress of Theoretical and Experimental Physics 2018 (2) (2018) 021D01. doi:10.1093/ptep/pty011.   
[14] W. Dickhoff, C. Barbieri, Progress in Particle and Nuclear Physics 52 (2) (2004) 377 – 496. doi:https://doi.org/10. 1016/j.ppnp.2004.02.038.   
[15] K. S. Egiyan, et al., Phys. Rev. Lett. 96 (2006) 082501. doi: 10.1103/PhysRevLett.96.082501.   
[16] A. Rios, A. Polls, W. H. Dickhoff, Phys. Rev. C 79 (2009) 064308. doi:10.1103/PhysRevC.79.064308.   
[17] A. Rios, A. Polls, W. H. Dickhoff, Phys. Rev. C 89 (2014) 044303. doi:10.1103/PhysRevC.89.044303.   
[18] R. B. Wiringa, R. Schiavilla, S. C. Pieper, J. Carlson, Phys. Rev. C 89 (2014) 024305. doi:10.1103/PhysRevC.89.024305.   
[19] C. Mahaux, R. Sartor, Single-Particle Motion in Nuclei, Springer US, Boston, MA, 1991, pp. 1–223. doi:10.1007/ 978-1-4613-9910-0\_1.   
[20] M. H. Mahzoon, R. J. Charity, W. H. Dickhoff, H. Dussan, S. J. Waldecker, Phys. Rev. Lett. 112 (2014) 162503. doi:10.1103/ PhysRevLett.112.162503.   
[21] W. H. Dickhoff, R. J. Charity, M. H. Mahzoon, J. of Phys. G: Nucl. and Part. Phys. 44 (3) (2017) 033001. doi:10.1088/ 1361-6471/44/3/033001.   
[22] H. Dussan, M. H. Mahzoon, R. J. Charity, W. H. Dickhoff, A. Polls, Phys. Rev. C 90 (2014) 061603. doi:10.1103/ PhysRevC.90.061603.   
[23] W. H. Dickhoff, D. Van Neck, Many-Body Theory Exposed!, 2nd edition, World Scientific, New Jersey, 2008.   
[24] M. H. Mahzoon, M. C. Atkinson, R. J. Charity, W. H. Dickhoff, Phys. Rev. Lett. 119 (2017) 222503. doi:10.1103/PhysRevLett. 119.222503.   
[25] B. D. Anderson, P. R. Bevington, F. H. Cverna, M. W. Mc-Naughton, H. B. Willard, R. J. Barrett, N. S. P. King, D. J. Ernst, Phys. Rev. C 19 (1979) 905–912. doi:10.1103/PhysRevC. 19.905.   
[26] J. M. Mueller, R. J. Charity, R. Shane, L. G. Sobotka, S. J. Waldecker, W. H. Dickhoff, A. S. Crowell, J. H. Esterline, B. Fallin, C. R. Howell, C. Westerfeldt, M. Youngs, B. J. Crowe, R. S. Pedroni, Phys. Rev. C 83 (2011) 064605. doi: 10.1103/PhysRevC.83.064605.   
[27] G. Kramer, H. Blok, L. Lapiks, Nuclear Physics A 679 (3) (2001) 267 – 286. doi:10.1016/S0375-9474(00)00379-1.   
[28] P. Schwandt, H. O. Meyer, W. W. Jacobs, A. D. Bacher, S. E. Vigdor, M. D. Kaitchuck, T. R. Donoghue, Phys. Rev. C 26 (1982) 55–64. doi:10.1103/PhysRevC.26.55.   
[29] O. Hen, G. A. Miller, E. Piasetzky, L. B. Weinstein, Rev. Mod. Phys. 89 (2017) 045002. doi:10.1103/RevModPhys.89.045002.   
[30] M. Duer, et al., Nature 560 (7720) (2018) 617–621. doi:10. 1038/s41586-018-0400-z.