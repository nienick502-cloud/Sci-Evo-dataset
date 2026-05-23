# Incomplete absorption reactions at high energy

Katsuhito Makiguchi1 and Wataru Horiuchi2,3,1*

1Department of Physics, Hokkaido University, Sapporo 060-0810, Japan   
2Department of Physics, Osaka Metropolitan University, Osaka 558-8585, Japan

3Nambu Yoichiro Institute of Theoretical and Experimental Physics (NITEP), Osaka Metropolitan University, Osaka 558-8585, Japan ∗E-mail: whoriuchi@omu.ac.jp

The total reaction cross section of high-energy nucleus-nucleus collision reflects the nuclear density profiles of the colliding nuclei and has been a standard tool to investigate the size properties of short-lived unstable nuclei. This basis relies on the assumption that the nucleusnucleus collision is strongly absorptive in the sense of an optical model. However, this property does not hold completely, while incomplete absorption occurs when an overlap density of two colliding nuclei is low enough. In this paper, we propose a way to quantify this incompleteness, that is, the “blackness” of the total reaction cross section. A significance of this quantification is drawn by taking an example of the total reaction cross sections of proton-rich C isotopes.

Subject Index xxxx, xxx

# 1 Introduction

Total reaction cross sections of nucleus-nucleus collision at a few tens to thousand MeV have been utilized to extract the nuclear size properties of short-lived unstable nuclei. These intensive measurements have revealed, a two-neutron halo nucleus [1], the development of neutron skin [2], and strong deformations of unstable nuclei [3, 4]. See, e.g., Ref. [5] for reviews of those advancements. Such studies have been extended to F isotopes near dripline nucleus $2 9$ F exhibiting two-neutron halo structure [6], and Ca isotopes showing a sudden core swelling phenomenon [7]. The total reaction cross section measurements for the unstable nuclei are always made in the inverse kinematics using a well-known and stable target nucleus, typically, carbon and proton targets. As those target nuclei offer different sensitivity to the nuclear density profile of the projectile nucleus, quantifying the sensitivity opens up the possibility of determining the selected density profile in exotic neutron-rich nuclei.

Since the beam energy is high and the nuclear interaction is short, the total reaction cross section at the high incident energies can be approximated well by a black-sphere (BS) model [8–10], and hence the cross section is roughly proportional to $\pi ( R _ { P } + R _ { T } ) ^ { 2 }$ , where $R _ { P }$ and $R _ { T }$ are the nuclear radii of the projectile and target nuclei, respectively. This is a basis that the nuclear radius can be extracted from the total reaction cross section. However, because the nuclear reaction is not a perfect black sphere, the information more than the nuclear radius, i.e., the density profile near the nuclear surface, can be extracted [10, 14, 15]. As it may be related to that incompleteness, in Ref. [16], an interesting observation was made in the nucleus-proton total reaction cross sections for proton-rich C isotopes: Despite that, the nuclear matter radius is enhanced, the total reaction cross section is reduced. This implies the deviation from the BS picture of the high-energy nuclear collision. The purpose of this paper is to quantify the “blackness” of high-energy nucleus-nucleus reactions and discuss the effect of its incompleteness on the total reaction cross sections.

The paper is organized as follows. To quantify the nuclear blackness we employ a microscopic high-energy reaction theory, the Glauber model. In Sec. 2, we briefly describe the basic inputs of the Glauber model. Section 3 is devoted to discuss our results. Section 3.1 quantifies the blackness of the high-energy nucleus-nucleus collisions. We conveniently divide the total reaction cross sections into the complete and incomplete absorption parts based on the reaction probabilities obtained by the present microscopic reaction model. In Sec. 3.2, the characteristic behavior of the total reaction cross sections as a function of the neutron number is discussed by taking an example of proton-rich C isotopes, in which the incomplete absorption part is dominant. Conclusion is made in Sec. 4.

# 2 Method

To describe the transparency in the high-energy nucleus-nucleus collsion, we employ a microscopic high-energy nuclear theory, the Glauber model [17]. The total reaction cross section is calculated by integrating the reaction probability

$$
P (\pmb {b}) = 1 - | e ^ {i \chi (\pmb {b})} | ^ {2}, \tag {1}
$$

over the impact parameter vector $^ { b }$ a s

$$
\sigma_ {R} = \int d \boldsymbol {b} P (\boldsymbol {b}). \tag {2}
$$

The reaction probability describes how the incoming flux is absorbed by the target nuclei. Note that

$$
P (\boldsymbol {b}) = \left\{ \begin{array}{l l} 1 & (b \leq R) \\ 0 & (b > R) \end{array} \right. \tag {3}
$$

holds for the BS or complete absorption model with a sharp nuclear radius $R$ . In the Glauber model, it is vital to evaluate the optical phase-shift function

$$
e ^ {i \chi (\boldsymbol {b})} = \left\langle \Psi_ {0} ^ {P} \Psi_ {0} ^ {T} \right| \prod_ {j \in \mathrm {P}} ^ {A _ {P}} \prod_ {k \in \mathrm {T}} ^ {A _ {T}} [ 1 - \Gamma_ {N N} (\boldsymbol {s} _ {j} ^ {P} - \boldsymbol {s} _ {k} ^ {T} + \boldsymbol {b}) ] \left| \Psi_ {0} ^ {P} \Psi_ {0} ^ {T} \right\rangle , \tag {4}
$$

where $s _ { j } ^ { F }$ (sTj ) is the two-dimensional single-particle coordinate of the $j$ th nucleon in the projectile (target) nucleus perpendicular to the beam direction $z$ , $\Psi _ { 0 } ^ { P }$ (ΨT0 ) is the groundstate wave function of the projectile (target) nucleus, and $\Gamma _ { N N }$ is the profile function, which describes the nucleon-nucleon (NN) collision and is usually parametrized as

$$
\Gamma_ {N N} (\boldsymbol {b}) = \frac {1 - i \alpha_ {N N}}{4 \pi \beta_ {N N}} \sigma_ {N N} ^ {\mathrm {t o t}} \exp \left[ - \frac {\boldsymbol {b} ^ {2}}{2 \beta_ {N N}} \right], \tag {5}
$$

where $\alpha N N$ is the ratio of the real to the imaginary part of the $N N$ scattering amplitude of forward angle, $\beta _ { N N }$ is the slope parameter of the $N N$ elastic scattering differential cross section, and $\sigma _ { N N } ^ { \mathrm { t o t } }$ is the total cross section of the $N N$ scattering. To describe the isospin dependence appropriately, especially for the proton scattering, we take the neutron-proton $( n p )$ profile function being different from the $p p$ one. The $n n$ profile function is taken the same as that for $p p$ . These parameter sets are tabulated in Ref. [18] for a wide energy range.

The evaluation of the phase-shift function of Eq. (4) involves multi-dimensional integration, which may be done with a Monte Carlo technique [19, 20]. However, in general, it is

demanding. Thus, the optical phase-shift function is usually approximated by taking the leading order of the cumulant expansion as

$$
i \chi (\boldsymbol {b}) = - \iint d \boldsymbol {r} ^ {P} d \boldsymbol {r} ^ {T} \rho^ {P} (\boldsymbol {r} ^ {P}) \rho^ {T} (\boldsymbol {r} ^ {T}) \Gamma_ {N N} (\boldsymbol {s} ^ {P} - \boldsymbol {s} ^ {T} + \boldsymbol {b}), \tag {6}
$$

where $\boldsymbol { r } ^ { P ( T ) } = ( s ^ { P ( T ) } , z ^ { P ( T ) } )$ denotes the two-dimensional coordinate of the projectile (target) nucleus perpendicular to the beam direction $z ^ { P ( T ) }$ , and $\rho ^ { P } ( r ^ { P } )$ $( \rho ^ { T } ( r ^ { T } ) )$ is the density distribution of the projectile (target) nucleus. This expression is called optical limit approximation (OLA) and works well for elastic and total reaction cross sections of nucleus-proton scattering where the multiple scattering effect is negligeble [19–24]. For the nucleus-nucleus collision, the multiple scattering effects become larger than the proton scattering. To incorporate such effects, we employ the nucleon-target formalism (NTG) [25] as

$$
i \chi (\pmb {b}) = - \int d \pmb {r} ^ {P} \rho^ {P} (\pmb {r} ^ {P}) \left[ 1 - \exp \left\{- \int d \pmb {r} ^ {T} \rho^ {T} (\pmb {r} ^ {T}) \Gamma_ {N N} (\pmb {s} ^ {P} - \pmb {s} ^ {T} + \pmb {b}) \right\} \right]. \tag {7}
$$

The equation symmetrized for the exchange of the projectile and target nuclei is employed [25]. The theory requires the same inputs as these of the OLA and gives a better description as demonstrated in Refs. [20, 26, 27]. As a carbon target, we take the harmonic-oscillator (HO) type density distribution [21] that reproduces the rms point-proton radius of $1 2$ C, 2.33 fm [28]. As the theory has no adjustable parameter, the total reaction cross section properly reflects the profile of the projectile density distribution. This model was well tested by comparisons of the available experimental data for neutron-rich unstable nuclei [20, 29–31], and also used as a standard tool to extract the nuclear matter radius [6, 32, 33].

# 3 Results

# 3.1 Blackness of nuclear collisions for medium to heavy nuclei

First, we see a global trend of the reaction probabilities for medium to heavy nuclei. For simplicity, we employ two-parameter Fermi (2pF) type density distributions for neutron ( $q = n$ ) and proton ( $q = p$ ) for a nucleus with the mass number $A$ as

$$
\rho_ {q} (r) = \frac {\rho_ {0 q}}{1 + \exp [ (r - R _ {0}) / a ]}. \tag {8}
$$

We take a conventional parametrization, $R _ { 0 } = 1 . 1 2 A ^ { 1 / 3 } - 0 . 8 6 A ^ { - 1 / 3 }$ and $a = 0 . 5 4$ fm [38]. The $\rho _ { 0 q }$ value is determined by the normalization condition $\begin{array} { r } { 4 \pi \int _ { 0 } ^ { \infty } d r r ^ { 2 } \rho _ { q } ( r ) = N _ { q } } \end{array}$ with the nucleon number $N _ { q }$ and $A = N _ { n } + N _ { p }$ .

![](images/bc04c705fd4c551ecc4330389d7d43a7abc851d0368ea4308757e691b30a2a32.jpg)

![](images/d990cc0b2292c3a6c3611671befdf8d82a0b6013f562399106ef3678a7f3c6e8.jpg)  
Fig. 1 Reaction probabilities of Eq. (1) using 2pF density distributions with $A = 4 0$ , 58, 120, and 208 on (a) carbon and (b) proton targets at 1000 MeV/nucleon. The arrows indicate the $S$ values for each system, which are defined by the $b$ value where the reaction probability becomes $\approx 0 . 9 9$ .

Figure 1 compares the reaction probabilities using the 2pF density distributions with $A =$ 40( $N _ { p } = 2 0$ ), 58( $N _ { p } = 2 8$ ), 120( $N _ { p } = 5 0$ ) and 208 ( $N _ { p } = 8 2$ ) on carbon and proton targets at the incident energy of 1000 MeV/nucleon. For a carbon target, typical behavior of the reaction probabilities is found: They are unity in the internal regions, where the two colliding nuclei strongly overlap with each other, showing the complete absorption in the sense of optics; and decrease rapidly as less number of nucleons can contribute to the collision at large impact parameter $b$ . Similar behavior is found for a proton target but for light projectiles, i.e., $A = 4 0$ , the reaction probability becomes less than unity even at $b = 0$ . This is because the mean-free path $\propto 1 / ( \rho \sigma _ { N N } ^ { \mathrm { t o t } } )$ of a proton target is large enough to penetrate a projectile nucleus, which is in contrast to the case for a carbon target, where more particles can contribute to the reaction processes.

Given the properties of the reaction probabilities shown above, it is convenient to separate the total reaction cross section into the complete and incomplete absorption parts. Defining the reaction radius $R = \sqrt { \sigma _ { R } / \pi }$ [8, 12], the decomposition reads

$$
\sigma_ {R} = \sigma_ {\text {c o m p}} + \sigma_ {\text {i n c o m p}} \tag {9}
$$

with

$$
\sigma_ {\mathrm {c o m p}} \equiv \pi S ^ {2}, \tag {10}
$$

$$
\sigma_ {\mathrm {i n c o m p}} \equiv \pi R ^ {2} \left[ 1 - \left(\frac {S}{R}\right) ^ {2} \right], \tag {11}
$$

where the boundary radius $S$ is introduced, which is defined by the impact parameter that the reaction probability becomes, say $P ( S ) \approx 0 . 9 9$ . For $S = R$ , i.e., $\sigma _ { R } = \sigma _ { \mathrm { c o m p } }$ , it corresponds to the limit that a complete absorption occurs below a sharp radius $R$ , which is simply expressed by Eq. (3). The $S$ value can also be zero, i.e., $\sigma _ { R } = \sigma _ { \mathrm { i n c o m p } }$ , which denotes a “complete” incomplete absorption, where the reaction probability is always less than unity even at $b = 0$ . Therefore, $\sigma _ { \mathrm { c o m p } }$ and σincomp can respectively be interpreted as black and opaque sphere parts of the obstacle in optics. As the complete absorption occurs below the boundary radius $S$ , any structural information in the internal regions cannot directly be obtained, while σincomp includes the information on the density profile near the nuclear surface. We note, however, that the information on the internal density can be obtained indirectly by probing the density profile near the nuclear surface, see, e.g., for nuclear bubble structure [34]. We also remark that the earlier study [35] proposed a similar decomposition, where the energy-independent volume and energy-dependent surface terms are assumed, offering a good parametrization for $\sigma _ { R }$ . In the present decomposition, to separate the complete and incomplete absorption regions based on the reaction probability, both the $R$ and $S$ values become energy dependent.

We evaluate the $S$ values for the high energy reactions on carbon and proton targets with the 2pF projectile density distributions. The arrows in Fig. 1 indicate these calculated $S$ values, which are $S = 4 . 9$ , 5.6, 7.0 and 8.2 fm for $A = 4 0 , 5 8 , 1 2 0$ and 208, respectively, for a carbon target, and $S = 0 , 1 . 7 , 3 . 7$ and 5.1 fm for $A = 4 0 , 5 8 , 1 2 0$ and 208, respectively, for a proton target. The larger the $S$ value, the larger the projectile nucleus becomes, indicating the penetrability of a probe, i.e., a target nucleus. This flat behavior is longer for a carbon target because it involves the size of the target nucleus $\approx 3$ fm. Since the reaction probability with $A = 4 0$ for a proton target is always less than unity, the $S$ value becomes zero by definition, and hence $\sigma _ { \mathrm { c o m p } } = 0$ .

The penetrability of the target nucleus strongly depends on the magnitudes of the elementary nucleon-nucleon cross sections. To see it clearly, we investigate the energy dependence of the “blackness” of the nucleus-nucleus collisions. Reminding the decomposition of Eqs. (9)– (11), the ratio $S / R$ , which ranges from zero to unity, can be a measure of the transparency in the colliding processes and expresses the blackness of the nucleus-nucleus reaction. Figure 2 plots the behavior of the nuclear blackness $S / R$ as a function of the incident energies for carbon and proton targets using the 2pF density distributions with different mass numbers

![](images/68ba8471d9d98652d2beb7a022bceb767bf6688b13856a720d4d8a7302364095.jpg)

![](images/b1a78bc0b6f192f77c5d80929caa244f458c6e7128e7f0352b553705d5d11bc1.jpg)  
Fig. 2 Nuclear blackness, $S / R$ , as a function of of the incident energy with $A = 4 0$ , 58, 120, and 208 on (a) carbon and (b) proton targets. See text for more detail.

$A = 4 0 , 5 8 , 1 2 0$ , and 208. The $S / R$ value becomes larger as $A$ increases because the contribution of the nuclear surface becomes relatively smaller than that of the nuclear bulk. For a carbon target, the $S / R$ values are large about 0.6–0.8. This means that the high-energy nucleus-carbon collision mostly consists of the complete absorption part. In the low-incident energy region, because the elementary nucleon-nucleon cross section is large, the blackness of the reaction becomes also large. Here the total reaction cross section is less sensitive to the internal density of the projectile nucleus but probes more surface regions. For a proton target, at the low incident energies $\approx 1 0 0$ MeV/nucleon, the blackness with large $A$ can be comparable to that of the carbon target. The $S / R$ values are more strongly dependent on the incident energy since the proton target reflects the elementary cross section more directly than that of the carbon target [12, 13]. The blackness becomes minimum for $\approx 2 0 0$ – 600 MeV/nucleon. where the nucleon-nucleon cross section becomes minimum and again increases for $\gtrsim 6 0 0$ MeV/nucleon, which reflects the behavior of the nucleus-nucleus total cross sections included in the profile function. For $A = 4 0$ and 58, since less number of nucleons contributes to the reaction processes of a proton target than these of a carbon target, the nuclear blackness becomes zero, exhibiting incomplete absorption for a whole impact parameter.

We see that the comparison made here quantifies the sensitivity of different probes on the nuclear density profile. It is interesting to investigate the blackness of the high-energy nuclear collisions with other probes. See Appendix for the results for $^ 4$ He and antiproton scattering.

# 3.2 Total reaction cross sections involving light nuclei

As seen in the previous subsection, the nucleus-proton scattering offers a unique opportunity to exhibit the complete incomplete absorption in the colliding process. It is interesting to clarify the effect of this incompleteness on the total reaction cross sections. Here we investigate proton-rich C isotopes because some experimental data of the total reaction cross sections are available for both the carbon and proton targets. Since the mass number is small, the total reaction cross section on a proton target can only be written by σincomp.

For projectile densities, we first employ the HO-type density distributions whose width parameters are set to reproduce the measured total reaction cross sections of the proton-rich C isotopes, $^ { 9 - 1 1 }$ C, on a carbon target at $\approx$ 700 MeV/nucleon [36, 37], and take commonly for proton and neutron. The difference between the proton and neutron radii becomes significant in the proton-rich C isotopes. To incorpolate this property, we generate the density distributions from the Woods-Saxon mean-field as [38]

$$
V (r) = V _ {0} f (r) + V _ {1} (\boldsymbol {l} \cdot \boldsymbol {s}) r _ {0} ^ {2} \frac {1}{r} \frac {d f}{d r} (r) + V _ {C} (r) \frac {1}{2} (1 - \tau_ {3}) \tag {12}
$$

with $\tau _ { 3 } = 1$ for neutron and $- 1$ for proton and $f ( r ) = \{ 1 + \exp [ ( r - R _ { \mathrm { W S } } ) / a _ { \mathrm { W S } } ] \} ^ { - 1 }$ . We take convenient parametrization given in Ref. [38]: $V _ { 0 } = - 5 1 + 3 3 ( N - 6 ) / ( N + 6 ) \tau _ { 3 }$ and $V _ { 1 } = 2 2 - 1 4 ( N - 6 ) / ( N + 6 ) \tau _ { 3 }$ in units of MeV with $N$ being the neutron number of C isotopes, and $V _ { C }$ is the Coulomb potential which only acts on protons. By applying them to light nuclei, we use smaller radius and diffuseness parameters $R _ { \mathrm { W S } } = 1 . 2 ( N + 6 ) ^ { 1 / 3 }$ fm and $a _ { \mathrm { W S } } = 0 . 6$ fm following Ref. [39], and modify the strength of the central potential $V _ { 0 }$ by multiplying a factor $f$ as $f V _ { 0 }$ to reproduce the measured cross sections as was done for the HO density. The properties of these density distributions are summarized in Tab. 1. For both the HO- and WS-type density distributions, the behavior of the root-mean-square (rms) matter radius, $r _ { m }$ , is similar: It increases significantly as going to the proton-rich side mainly due to the enhancement of the rms proton radius, $r _ { p }$ . Since the present WS parametrization accounts for the isospin dependence, the difference between the neutron and rms radii, i.e., the neutron-skin thickness, $\boldsymbol { r } _ { n } - \boldsymbol { r } _ { p }$ , is more significant than the HO one.

Figure 3 compares the total reaction cross sections of the proton-rich C isotopes on carbon and proton targets. The rms matter radii and neutron-skin thickness are also plotted. It appears that the total reaction cross section is well proportional to the matter radius when a carbon target is used. However, for a proton target, no increase or even decrease of the cross section is found for these isotopes as was seen in Ref. [16]. The calculated cross sections by the WS-type density distributions better reproduce the experimental data incident at

Table 1 Rms matter, proton, and neutron radii and total reaction cross sections of protonrich C isotopes. The HO width and WS potential parameters are respectively adjusted to reproduce the interaction cross section data at around 700 MeV/nucleon. The cross sections and incident energies are in units of mb and MeV/nucleon, respectively.   

<table><tr><td></td><td></td><td>rp (fm)</td><td>rn (fm)</td><td>rm (fm)</td><td>σR (Theo.)</td><td>σI (Expt.) (E)</td></tr><tr><td rowspan="2">9C</td><td>HO</td><td>2.58</td><td>2.37</td><td>2.51</td><td>819</td><td>834 ± 18 (~720) [36]</td></tr><tr><td>WS</td><td>2.70</td><td>1.94</td><td>2.48</td><td>818</td><td>812 ± 13 (680) [36]</td></tr><tr><td rowspan="2">10C</td><td>HO</td><td>2.36</td><td>2.26</td><td>2.32</td><td>795</td><td>795 ± 12 (~720) [36]</td></tr><tr><td>WS</td><td>2.45</td><td>2.07</td><td>2.30</td><td>797</td><td></td></tr><tr><td rowspan="2">11C</td><td>HO</td><td>2.18</td><td>2.14</td><td>2.16</td><td>776</td><td>778 ± 40 (~730) [37]</td></tr><tr><td>WS</td><td>2.20</td><td>2.06</td><td>2.13</td><td>771</td><td>772 ± 23 (700) [37]</td></tr></table>

$\approx 9 0$ MeV because the WS-type density distributions have a negative and thicker neutronskin thickness, i.e., a positive proton-skin thickness, than that of the HO-type density. We remark that the thick proton skin structure for $^ { 9 - 1 1 }$ C is consistent with the analysis made in Ref. [44]. As quantified in Refs. [12, 13], a thicker proton skin lowers the total reaction cross section as $\sigma _ { p p } ^ { \mathrm { t o t } }$ is $\approx 2 / 3$ of $\sigma _ { n p } ^ { \mathrm { t o t } }$ [18, 40] at incident energy of ${ \approx } 1 0 0$ MeV.

One may ask a question: Why is the different behavior found for the results with carbon and proton targets? Figure 4 displays the reaction probability of $_ { 1 0 }$ C on carbon and proton targets at 100 MeV/nucleon. The WS-type density distributions are used. As expected, for a carbon target, the reaction probability is unity up to $b = S = 3 . 4$ fm, while for a proton target, the probability is always less than unity ( $S = 0$ ) showing the complete incomplete absorption in the whole region. For a better understanding, we investigate the reaction probabilities by changing the rms matter radius of $_ { 1 0 }$ C by $\pm 0 . 2$ fm. The results are drawn in Fig. 4 (a). The probabilities appear to change beyond $b > S$ : For a carbon target, they only change in the surface region, whereas the change in the whole region is found for a proton target as $S = 0$ . We also plot in Fig 4 (b) the reaction probabilities by changing the neutron number by $\pm 1$ while keeping the same rms radius. The behavior is similar to that found in Fig 4 (a). Only the probabilities beyond $b > S$ are varied for a carbon target, while for a proton target, they change in the whole region.

More quantitatively, we evaluate the difference of the total reaction cross sections by changing the rms matter radius by +0.2 (−0.2) fm, $\Delta \sigma _ { R }$ , which are 62 ( $-$ 59) mb for a carbon and 14 (−17) mb for a proton target. Also, we do similar calculations by adding (removing) one neutron. They are 19 ( $-$ 21) mb for a carbon target and 23 ( $-$ 26) mb for a proton target, which is similar in both the targets. To guide the reader, those values are

summarized in Tab. 2. For a carbon target, since the cross section change by the radius change is larger than that by the mass number change, the total reaction cross section is in total enhanced by following the magnitude of the rms matter radius. On contrary, for a proton target, the decrease of the cross section due to the change of the neutron number exceeds the enhancement of the cross section by the rms matter radius, which can be possible in light nuclei, where the σincomp contribution is dominant. This sort of limit of $\sigma _ { R } = \sigma _ { \mathrm { i n c o m p } }$ is in contrast to the black sphere limit $\sigma _ { R } = \sigma _ { \mathrm { c o m p } }$ . In this case, the empirical relationship $\sigma _ { R } \propto \pi r _ { m } ^ { 2 }$ appears not to hold because it relies on the assumption that $\sigma _ { \mathrm { i n c o m p } }$ is smaller than σcomp.. $\sigma _ { \mathrm { c o m p } }$

![](images/044017dff27178549d8949bc6e3816ef54f42534833b3ed1ada8b21048e9d9b9.jpg)

![](images/27e370d60e2f9294bbcfbc7e2bb4fb2a9e1f97f6d1205606205f2552c7a83898.jpg)  
Fig. 3 (a) Total reaction cross sections as a function of the mass number of C isotopes. Incident energies are 700 and 90 MeV/nucleon for carbon and proton targets, respectively. The experimental data are taken from Refs. [36, 37, 41, 42] for a carbon target and Refs. [43, 44] for a proton target. (b) Rms matter radii $r _ { m }$ and neutron-skin thickness $\boldsymbol { r } _ { n } - \boldsymbol { r } _ { p }$ as a function of the mass number of C isotopes. The WS- and HO-type density distributions are employed.

# 4 Conclusion

The total reaction cross section measurement has been a standard tool to know the nuclear size properties as a basis that the nucleus-nucleus collision can be described as optics of strongly absorptive objects. We have proposed the decomposition of the total reaction cross section into complete and incomplete absorption parts as a measure of the “blackness” of the nucleus-nucleus collision.

![](images/2c8df70b0ae64d9f2b2fb36e0d65c5c003b73b375b9529b0aed5d4aacce4c0a5.jpg)

![](images/68c7a2a9b49f26252cb56ba6c438d638625a90bbf1c23ccbe81601d5aeeabf60.jpg)  
Fig. 4 Reaction probabilities of $_ { 1 0 }$ C at 100 MeV/nucleon by (a) changing the matter radius ±0.2 fm and (b) removing and adding one neutron while keeping the same matter radius. The arrow indicates the $S$ value of $_ { 1 0 }$ C for a carbon target, while $S = 0$ for a proton target.

Table 2 Modifications of the total reaction cross sections with respect to the changes of the density distributions of $_ { 1 0 }$ C generated from the WS potential. See text for details.   

<table><tr><td></td><td>rm (fm)</td><td>ΔσR(C)</td><td>ΔσR(p)</td></tr><tr><td>10C</td><td>2.30</td><td>-</td><td>-</td></tr><tr><td>+0.2 fm</td><td>2.50</td><td>62</td><td>14</td></tr><tr><td>-0.2 fm</td><td>2.10</td><td>-59</td><td>-17</td></tr><tr><td>+1n</td><td>2.30</td><td>19</td><td>23</td></tr><tr><td>-1n</td><td>2.30</td><td>-21</td><td>-26</td></tr></table>

For a carbon target, the reaction occurs almost completely when the projectile and target nuclei overlap significantly, that is, the nuclear collision is “black” enough, showing typical behavior of the cross sections as a function of the neutron number: The cross section increases as the nuclear radius increases. However, it is not always the case in the nuclear collision involving light elements using a proton target, where the cross section consists only of the incomplete absorption part. In that case, the cross section increase due to the enhancement of the rms matter radius becomes comparable to or even smaller than the cross section reduction by the mass number change, and thus the cross section can decrease despite that the nuclear radius is enhanced towards the proton dripline.

# Acknowledgment

We thank M. Tanaka for sending us the numerical data of the experimental cross sections on a proton target. This work was in part supported by JSPS KAKENHI Grant No. 18K03635. We acknowledge the Collaborative Research Program 2022, Information Initiative Center, Hokkaido University.

# A Blackness of other probes

The sensitivity of the nuclear density profile on the total reaction cross sections depends on choices of a target nucleus and incident energies originating from elementary hadronhadron cross sections [12, 13]. Here we show the blackness of the nuclear scattering by a 4He ( $\alpha$ ) and an antiproton (¯p). Figure A1 plots the $S / R$ values for $\alpha$ and $p$ scattering. The same 2pF density distributions used in Fig. 2 are employed. We take the HO-type density distribution that reproduces the charge radius of $^ 4$ He [28] for $\alpha$ -nucleus scattering and the nucleon-antinucleon ( $N N _ { \mathbf { \lambda } }$ ) profile function given in Ref. [15] for $p$ -nucleus scattering. As seen in Fig. A1 (a), for the $\alpha$ scattering, the behavior is almost the same as that of a carbon target but magnitudes of the $S / R$ values tend to be smaller. Because the size of $\alpha$ is smaller than that of the carbon target, the radius where the complete absorption occurs becomes smaller, and thus the $S$ value is relatively smaller compared to $R$ . For the $p$ scattering, as the energy dependence of $\sigma _ { N \bar { N } } ^ { \mathrm { t o t } }$ is different from that of $\sigma _ { N N } ^ { \mathrm { t o t } }$ , the $S / R$ values behave quite differently from the other probes examined in this paper. It is interesting to note that typical $S / R$ values are comparable to these of the $\alpha$ scattering, reflecting large elementary $N N$ cross section and effective interaction range [15].

# References

[1] I. Tanihata, H. Hamagaki, O. Hashimoto, Y. Shida, N. Yoshikawa, K. Sugimoto, O. Yamakawa, T. Kobayashi, and N. Takahashi, Phys. Rev. Lett. 55, 2676 (1985).   
[2] T. Suzuki, H. Geissel, O. Bochkarev, L. Chulkov, M. Golovkov, D. Hirata, H. Irnich, Z. Janas, H. Keller, T. Kobayashi et al., Phys. Rev. Lett. 75, 3241 (1995).   
[3] M. Takechi, T. Ohtsubo, M. Fukuda, D. Nishimura, T. Kuboki, T. Kubo, T. Suzuki, T. Yamaguchi, A. Ozawa, T. Moriguchi, H. Ooishi, Phys. Lett. B 707, 357 (2012).   
[4] M. Takechi, S. Suzuki, D. Nishimura, M. Fukuda, T. Ohtsubo, M. Nagashima, T. Suzuki, T. Yamaguchi, A. Ozawa, T. Moriguchi et al., Phys. Rev. C 90, 061305(R) (2014).   
[5] I. Tanihata, H. Savajols, and R. Kanungo, Prog. Part. Nucl. Phys. 68, 215 (2013), and references therein.   
[6] S. Bagchi, R. Kanungo, Y. K. Tanaka, H. Geissel, P. Doornenbal, W. Horiuchi, G. Hagen, T. Suzuki, N. Tsunoda, D. S. Ahn et al., Phys. Rev. Lett. 124, 222504 (2020).   
[7] M. Tanaka, M. Takechi, M. Fukuda, D. Nishimura, T. Suzuki, Y. Tanaka, T. Moriguchi, D. S. Ahn, A. Aimaganbetov, M. Amano et al., Phys. Rev. Lett. 124, 102501 (2020).   
[8] A. Kohama, K. Iida, and K. Oyamatsu, Phys. Rev. C 69, 064316 (2004).   
[9] A. Kohama, K. Iida, and K. Oyamatsu, Phys. Rev. C 72, 024602 (2005).   
[10] A. Kohama, K. Iida, and K. Oyamatsu, J. Phys. Soc. Jpn. 85, 094201 (2016).   
[11] W. Horiuchi and T. Inakura, Phys. Rev. C 101, 061301(R) (2020).   
[12] W. Horiuchi, Y. Suzuki, T. Inakura, Phys. Rev. C 89, 011601(R) (2014).

![](images/d7e0a2c1181c8daf4ddf56395f0b71577df61ad7d4e51052fafc95508b725333.jpg)

![](images/c55ddbe487500a05af54d99f472ba65ce9a1d47093089f149c11a0364f992034.jpg)  
Fig. A1 Same as Fig. 2 but for (a) $\alpha$ and (b) $p$ scattering.

[13] W. Horiuchi, S. Hatakeyama, S. Ebata, and Y. Suzuki, Phys. Rev. C 93, 044611 (2016).   
[14] S. Hatakeyama, W. Horiuchi, and A. Kohama, Phys. Rev. C 97, 054607 (2018).   
[15] K. Makiguchi, W. Horiuchi, and A. Kohama, Phys. rev. C 102, 034614 (2020).   
[16] K. Kaki, Prog. Theor. Exp. Phys. 2017, 093D01 (2017).   
[17] R. J. Glauber, Lectures in Theoretical Physics, edited by W. E. Brittin and L. G. Dunham (Interscience, New York, 1959), Vol. 1, p.315.   
[18] B. Abu-Ibrahim, W. Horiuchi, A. Kohama, and Y. Suzuki, Phys. Rev. C 77, 034607 (2008); ibid 80, 029903(E) (2009); 81, 019901(E) (2010).   
[19] K. Varga, S. C. Pieper, Y. Suzuki, and R. B. Wiringa, Phys. Rev. C 66, 034611 (2002).   
[20] T. Nagahisa and W. Horiuchi, Phys. Rev. C 97, 054614 (2018).   
[21] B. Abu-Ibrahim, S. Iwasaki, W. Horiuchi, A. Kohama, and Y. Suzuki, J. Phys. Soc. Jpn., Vol. 78, 044201 (2009).   
[22] S. Hatakeyama, S. Ebata,W. Horiuchi, and M. Kimura, J. Phys.: Conf. Ser. 569, 012050 (2014).   
[23] S. Hatakeyama, S. Ebata, W. Horiuchi, and M. Kimura, JPS Conf. Proc. 6, 030096 (2015).   
[24] S. Hatakeyama, W. Horiuchi, Nucl. Phys. 985, 20 (2019).   
[25] B. Abu-Ibrahim and Y. Suzuki, Phys. Rev. C 61, 051601(R) (2000).   
[26] W. Horiuchi and Y. Suzuki, Phys. Rev. C 74, 034311 (2006).   
[27] W. Horiuchi, Y. Suzuki, B. Abu-Ibrahim, and A. Kohama, Phys. Rev. C 75, 044607 (2007).   
[28] I. Angeli, K. P. Marinova, At. Data Nucl. Tables 99, 69 (2013).   
[29] W. Horiuchi, Y. Suzuki, P. Capel, and D. Baye, Phys. Rev. C 81, 024606 (2010).   
[30] W. Horiuchi, T. Inakura, T. Nakatsukasa, and Y. Suzuki, Phys. Rev. C 86, 024614 (2012).   
[31] W. Horiuchi, T. Inakura, T. Nakatsukasa, and Y. Suzuki, JPS Conf. Proc. 6, 030079 (2015).   
[32] R. Kanungo, A. Prochazka, W. Horiuchi, C. Nociforo, T. Aumann, D. Boutin, D. Cortina-Gil, B. Davids, M. Diakaki, F. Farinon et al., Phys. Rev. C 83, 021302(R) (2011).   
[33] R. Kanungo, A. Prochazka, M. Uchida, W. Horiuchi, G. Hagen, T. Papenbrock, C. Nociforo, T. Aumann, D. Boutin, D. Cortina-Gil et al., Phys. Rev. C 84, 061304(R) (2011).   
[34] V. Choudhary, W. Horiuchi, M. Kimura, and R. Chatterjee, Phys. Rev. C 102, 034619 (2020).   
[35] S. Kox, A. Gamp, C. Perrin, J. Arvieux, R. Bertholet, J. F. Bruandet, M. Buenerd, R. Cherkaoui, A. J. Cole, Y. El-Masri, N. Longequeue et al., Phys. Rev. C 35, 1678 (1987).   
[36] A. Ozawa, I. Tanihata, T. Kobayashi, Y. Sugahara, O. Yamakawa, K. Omata, K. Sugimoto, D. Olson, W. Christie, and H. Wieman, Nucl. Phys. A 608, 63 (1996).   
[37] A. Ozawa, I. Tanihata, T. Kobayashi, D. Hirata, O. Yamakawa, K. Omata, N. Takahashi, T. Shimada, K. Sugimoto, D. Olson, W. Christie and H. Wieman, Nucl. Phys. A 583, 807c (1995).   
[38] A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. I (W. A. Benjamin, New York, 1975).   
[39] W. Horiuchi, Prog. Theor. Exp. Phys. 2021, 123D01 (2021).   
[40] M. Tanabashi, K. Hagiwara, K. Hikasa, K. Nakamura, Y. Sumino, F. Takahashi, J. Tanaka, K. Agashe, G.

Aielli, C. Amsler et al. (Particle Data Group), Phys. Rev. D 98, 030001 (2018).   
[41] A.Ozawa, O. Bochkarev, L. Chulkov, D. Cortina, H. Geissel, M. Hellstr¨om, M. Ivanov, R.Janik, K. Kimura, T. Kobayashi et al., Nucl. Phys. A 691, 599 (2001).   
[42] A. Ozawa, T. Suzuki, and I. Tanihata, Nucl. Phys. A 693, 32 (2001).   
[43] A. Auce, A. Ingemarsson, R. Johansson, M. Lantz, G. Tibell, R. F. Carlson, M. J. Shachno, A. A. Cowley, G. C. Hillhouse, N. M. Jacobs et al., Phys. Rev. C 71, 064606 (2005).   
[44] K. Nishizuka, M. Takechi, T. Ohtsubo, D. Nishimura, M. Fukuda, K. Aoki, K. Abe, A. Ikeda, T. Izumikawa, H. Oikawa et al., JPS Conf. Proc. 14, 021015 (2017).