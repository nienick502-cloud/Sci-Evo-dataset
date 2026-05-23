# The optical potentials and nuclear reaction cross sections for the $n$ $^ { 1 2 } \mathbf { C }$ and N -12C scattering

Imane Moumene 1,∗ and Angela Bonaccorso 2,†

1Istituto Nazionale di Fisica Nucleare, Galileo Galilei Institute for

Theoretical Physics, Largo Enrico Fermi, 2, 50125 Firenze, Italy.

$^ 2$ Istituto Nazionale di Fisica Nucleare, Sezione di Pisa, Largo Bruno Pontecorvo 3, 56127 Pisa, Italy.

(Dated: October 24, 2023)

In this work we extend a previously derived $_ n$ - $^ { 9 }$ Be optical potential up to 500 MeV and apply it to the system $n$ - $^ { 1 2 } \mathrm { C }$ , finding excellent results for the energy dependence of the total cross sections. Results obtained with a standard optical model calculation are compared to those from the eikonal formalism in order to asses the accuracy of the latter as a function of the nucleon incident energy. For comparison, single folded (s.f.) nucleon-target potentials are also obtained using $^ { 1 2 } \mathrm { C }$ densities from different models. These potentials are sensitive to the density used and none of them reproduce the characteristics of the phenomenological potential nor the cross section results. We then calculate nucleus-nucleus $( N N )$ potentials and total reaction cross sections for some ”normal” and exotic projectile nuclei on $^ { 1 2 } \mathrm { C }$ within the eikonal formalism. We find that single folded (S.F.) projectile-target imaginary potentials and double folded (D.F.) potentials can produce similar energy dependence of the reaction cross sections but the S.F. results agree better with experimental data provided the radius parameter of the phenomenological $n$ -target potential is allowed to be energy dependent. We conclude that the results previously obtained for a $^ { 9 } \mathrm { { B e } }$ target are quite general, at least for light systems, and that a S.F. $N N$ potential built on a phenomenological nN potential can constitute an interesting and useful alternative to D.F. potentials.

# I. Introduction

Since its first introduction in 1958 [1], the opticalmodel potential has been widely used to describe scattering of nucleons and composite particles off nuclei. As shown in Ref. [1; 2], the optical-model potential is the single-particle operator which, introduced in the onebody Schr¨odinger equation, yields the elastic part of the full many-channel wave function. As Feshbach already pointed out in [2] the ”generalized optical-model potential” is complex, nonlocal, and energy dependent, therefore it is very difficult to calculate without the introduction of several approximations. The first-order term of the Feshbach potential is real and it assumes a straightforward ”folding” form in terms of the projectile and target densities and a nucleon-nucleon interaction. Such a form is called double folding (D.F.) when both projectile and target are composite nuclei, while in the case of a projectile given by a single nucleon one talks of single folding (s.f.) because only the target density is folded with the nucleon-nucleon interaction. The second-order term is complex. Its real part represents a correction to the first-order term often referred to as ”polarization potential.” The imaginary part represents all possible reactions between projectile and target and it is obviously difficult to calculate microscopically.

However, the O.P. (optical potential) has been suc-

cessfully applied in the framework of a phenomenological approach in which its form factor has been chosen on the grounds of nuclear structure considerations and its parameters have been adjusted in order to fit the experimental data. In spite of its complexity, several attempts have been made to calculate the optical potential. In the past they were mainly concerned with the calculation of the real part of the O.P. via folding procedures, while the imaginary part has been treated phenomenologically due to its further complexity.

The folding procedure which is exact for the first-order real term was generalized by several authors [3–6] to obtain both the real and the imaginary part of the optical potential, introducing an effective, complex $g$ matrix which describes the nucleon-nucleon interaction. In the high energy limit one can easily obtain the Glauber [7] form of the reaction cross section in terms of the imaginary potential as given by the folding form [8], which was first used by De Vries and Peng [9] and Kox et al.[10].

However, from the time of the introduction of folding potentials Satchler [6] suggested that caution should be taken with the model, in particular when applied to obtain the imaginary part of the optical potential. The imaginary potential should be all orders in the interaction while the folding procedure provides first-order potentials. Furthermore a known drawback of imaginary folded potentials is that they are often too absorptive in the internal part while being too shallow on the surface. This can be a problem, for example for exotic nuclei which are often very diffuse due to the anomalous $N / Z$ ratios and present phenomena such as neutron halo and neutron skin. In order to improve the calculations of $N N$ folded potentials Satchler and Love [5] pro-

posed a different type of single folded (S.F.) potentials obtained by folding a phenomenological nucleon-nucleus interaction with the density of the other colliding nucleus. The authors of Ref.[11] applied this idea by using the Bruy`eres Jeukenne-Lejeune-Mahaux (JLMB) model [12; 13] for the $n N$ potentials folded with various projectile densities. Recently the authors of [14] folded the KD02 global nucleon-target potential [15] with $6 , 7$ Li densities. Another method called MOL [16], for modified optical limit, can also be interpreted as a special kind of the S.F. procedure that we will discuss with Eq. (5). In Ref.[16] an effective $n N$ profile function was introduced within the Glauber approach, which acts as the $n N$ optical potential does in the S.F. model.

A simple use and check of the imaginary folded potential is in the calculation of reaction cross sections. In the past, a very detailed study of the dependence of reaction cross section values on the parameters of the folded potential was done in the seminal paper Ref. [17], while Ref. [18] dealt with Pauli blocking and medium effects in nucleon knockout. In general D.F. potentials need to be corrected to take into account medium effects beyond the simple nn interaction. Toward this goal, more recently, in studying the energy dependence of reaction cross sections by the MOL [16] Glauber approach, several groups have tried to modify some of the ingredients of the double folding model in the attempt to improve its performances. For example in Ref. [19] the average neutronproton $( n p )$ and proton-proton $( p p )$ cross sections were modified, while in Ref. [20] the range parameters $\beta$ of the effective $( n n )$ and $( n p )$ interactions were fitted. See Eqs. (9-11).

More fundamental, microscopic approaches to calculate the imaginary potential have started to be quite successful in the last twenty years thanks also to improved computing methods. See Ref. [21] for a recent, exhaustive review. For nucleon-nucleus $( n N )$ potentials ab initio methods have reached a quite high degree of accuracy [22–26]. On the other hand the $n N$ potential [27] and $N N$ potentials (Refs. [28–31] and other works by the same authors) are based on a microscopic, complex $g$ matrix and then either a single folding or a double folding model is constructed. In the following we will define and discuss further these approaches.

However, when, for a give nucleus, a large set of data is available it might be useful to start fitting the parameters of a phenomenological potential. For example in Ref. [32], thanks to the existence of an almost continuous series of neutron- $^ { 9 }$ Be data as a function of the neutron incident energy, a phenomenological potential and a dispersive optical model (DOM) [33] potential were introduced for the system neutron- $^ { 9 } \mathrm { { B e } }$ , and were able to reproduce at the same time the total, elastic, and reaction cross sections and all available elastic scattering angular distributions. These results were important because they showed that a phenomenological nucleontarget O.P. could be obtained also for light nuclei and on a wide energy range. Then using one of those potentials,

AB, a S.F. (light)-nucleus- $^ { 9 }$ Be imaginary optical potential was derived and it was shown that it is more accurate than a D.F. optical potential [34–36] in reproducing $N N$ reaction cross section. Considering that $^ { 9 } \mathrm { { B e } }$ is one of the most used targets for a large number of reaction studies, the above cited works constituted an important starting point for further studies and applications, in particular for reactions with exotic nuclei.

Of course one might wonder whether such results are due to the special nature of $^ { 9 } \mathrm { { B e } }$ , which is itself weakly bound and strongly deformed. For this reason and to draw more general conclusions we decided to try to apply in this work the same AB potential to the description of $n$ - $\mathrm { ^ { 1 2 } C }$ scattering and calculate by the optical model total cross sections in the range 20-500 MeV. At the moment we do not attempt to fit the low energy resonance region, which would need an ad hoc study in particular as far as the spin-orbit potential is concerned. One motivation is that we are eventually interested in experiments with exotic nuclei studied at energies larger than about 60-80A. MeV. These are insensitive to the low energy part on the nucleon-target interaction, while there is a large bulk of data at relativistic energies larger than $2 0 0 A$ . MeV. For example the BARB experiment at GSI deals with high energy beams [37]. For this reason we have extended the AB potential to fit $n$ - $^ { 9 } \mathrm { { B e } }$ and $n$ - $\mathrm { ^ { 1 2 } C }$ total cross sections above $2 0 0 A$ . MeV, finding small differences in the two cases. Folding the newly established $n$ - $^ { 1 2 }$ C optical potential with several projectile densities, we will then construct S.F. $N$ - $^ { 1 2 }$ C potentials. These potentials are necessary to calculate reaction cross section and deduce from data unknown nuclear densities and rms radii, as mentioned above. Optical potentials are also necessary in breakup models to calculate the $S$ matrices for the core-target and nucleon-target scattering. In the future it would be interesting to apply the S.F. and D.F. potentials to a series of exotic nuclei knockout induced reactions in order to asses their accuracy in reproducing single nucleon breakup absolute cross sections as suggested in [38].

Besides fundamental research, we would like to stress the other important application of simple optical potentials in transport codes. An essential ingredient of such codes are the calculated realistic nuclear reaction cross sections used for risk evaluation of manned space exploration missions as well as for radiation therapy, where one needs dose calculations for treatment planning [39]. The therapeutic use of heavy ions, such as carbon, has gained significant interest due to advantageous physical and radiobiologic properties compared to photon based therapy [40]. Most recently exotic nuclei close to $\mathrm { ^ { 1 2 } C }$ , such as $_ { 1 2 }$ N, $^ { 1 1 } \mathrm { C }$ , and $^ { 1 0 } \mathrm { C }$ have been proposed for radiation therapy [37]. Also in reactor physics data and models of reaction cross sections are of fundamental importance [41].

Turning to theoretical methods which use the O.P. to obtain reaction cross sections, while the optical model (OM) and coupled-channel (CC) model are certainly the most accurate ways, as previously mentioned, the

Glauber model [7] with folded potentials (f.p.) [5; 6], has also been used for many years [9; 10] and its results have been compared to data. In particular from the beginning of physics with radioactive ion beams (RIBs) the method has become very popular for its simplicity in deducing density distributions of exotic nuclei and their root mean square (rms) radii [16; 19; 20; 42–47] and the core-target survival probability in knockout reactions [48]. In particular in a recent work [38] the sensitivity to folding methods used to obtain the nucleon-target and core-target optical potentials in standard knockout eikonal calculations used to extract spectroscopic factors has been discussed.

A brief reminder of basic formulas used in this paper is provided in Sec. II. Then Sec. III, which contains our results, is divided in two subsections. In the first the extension of the $n$ - $^ { 9 }$ Be AB potential of Ref. [32] up to 500 MeV is provided and it is shown that almost the same potential can be applied to $n$ - $\mathrm { ^ { 1 2 } C }$ scattering. Cross sections are calculated with a standard optical model and with the eikonal method using the phenomenological potential and some folded $n$ -target s.f. potentials. Our focus will be on the comparison of results for the energy dependence of the total cross sections. In this way, for the $n$ -target system, we will test the accuracy of the phenomenological potential vs the s.f. potential, the dependence on the target model density and of the optical model vs the Glauber model. To lend further support to our S.F. approach, similarly to what has been done in Refs. [34; 35], we will calculate in Sec. B , the imaginary part of $^ { 1 2 }$ C-$\mathrm { ^ { 1 2 } C }$ optical potential with the S.F. potential built from the projectile density and the phenomenological $n$ -target potential, and with the D.F. potential obtained from the projectile and target densities and the nucleon-nucleon interaction, and discuss their differences. Finally $N N$ reaction cross section calculations made with the two different potentials will be compared to experimental values for the systems $\bot 2$ C+ $^ { 1 2 }$ C, $^ { 9 } \mathrm { { B e + } }$ $_ { 1 2 }$ C, $^ { 2 0 }$ Ne+ $^ { 1 2 }$ C, $^ { n } \mathrm { C a } +$ $\mathrm { ^ { 1 2 } C }$ . Given the symmetry of projectile and target, the first system is a particularly interesting test case for the accuracy of the phenomenological potential approach vs folded potential.

For the various cases studied, we will provide figures of the radial dependence of the imaginary potentials used, their volume integrals, and rms radii, such that differences in cross section results can be traced back to how various potentials represent the localization of reactions and on how they might contain in-medium and shortrange repulsion effects.

# II. Theory

The $n$ - $^ { 9 }$ Be phenomenological potential AB of Ref. [32] is here extended to 500 MeV and to the system n+ $^ { 1 2 } \mathrm { C }$ . The potential of this paper has the form

$$
U _ {A B} (r, E) = - \left[ V _ {\mathrm {W S}} (r, E) + i W _ {\mathrm {W S}} (r, E) \right]. \tag {1}
$$

The real part of the neutron-target interaction is given by $V _ { \mathrm { W S } }$ , the usual Woods-Saxon potential:

$$
V _ {\mathrm {W S}} (r) = V ^ {R} f \left(r, R ^ {R}, a ^ {R}\right). \tag {2}
$$

Also, the imaginary part takes the form

$$
W _ {\mathrm {W S}} (r) = W ^ {v o l} f \left(r, R ^ {I}, a ^ {I}\right) - 4 a ^ {I} W ^ {s u r} \frac {d}{d r} f \left(r, R ^ {I}, a ^ {I}\right). \tag {3}
$$

with $f ( r , R ^ { i } , a ^ { i } ) = \left( 1 + e ^ { \frac { r - R ^ { i } } { a ^ { i } } } \right) ^ { - 1 }$ and $R ^ { i } = r ^ { i } A ^ { 1 / 3 }$

The real AB potential of Ref. [32] contained also a correction term $\delta V$ which originates from surfacedeformation effects and represents channels for which a simple Woods-Saxon form is not appropriate. Because such couplings are important only up to around 20 MeV, and here we are not interested in this low energy region for the present applications on $^ { 1 2 } \mathrm { C }$ , we shall take $\delta V = 0$ . For the same reason the spin-orbit term will be neglected. The parameters of $U _ { \mathrm { A B } } ( r , E )$ for the $\boldsymbol { n }$ - 9Be and $n$ - $\mathrm { ^ { 1 2 } C }$ interaction used in this paper are given in Tables I and II respectively.

For comparison we consider also a s.f. [6; 8] $n$ -target potential $U _ { \rho } ^ { n T }$ defined as

$$
U _ {\rho} ^ {n T} (\mathbf {r}) = - \frac {1}{2} \hbar v \sigma_ {n n} (1 - i \alpha_ {n n}) \rho_ {T} (\mathbf {r}), \tag {4}
$$

where $\rho _ { T } ( \mathbf { r } )$ is the target density function, for which we will use a number of different models as specified in the following, $\sigma _ { n n }$ is the average of the experimental neutron-proton and proton-proton cross sections, and $\alpha _ { n n }$ is the ratio of the real and imaginary scattering amplitude at zero degrees. $\boldsymbol { v }$ is the classical relative motion velocity of the scattering. The previous equation can be generalized in an obvious way in order to distinguish between the proton and neutron densities and the proton-neutron and proton-proton cross sections, using $\rho _ { P } ~ = ~ \rho ^ { \prime \prime } { } _ { P } + \rho ^ { \prime } { } _ { P }$ and $U _ { \rho } ^ { n T } ( r ) ~ = ~ - \frac { 1 } { 2 } \hbar v [ \sigma _ { n p } ( 1 ~ -$ $i \alpha _ { n p } ) \rho { ^ p } _ { T } ( r ) + \sigma _ { p p } ( 1 - i \alpha _ { p p } ) \rho { ^ n } _ { T } ( r ) ]$ . This is the formalism followed in the present work. Here we are assuming a zero-range nucleon-nucleon interaction, and in numerical calculations the values of $\sigma _ { n n }$ and $\alpha _ { n n }$ will be taken from the parametrization of Refs. [18; 43; 45].

In the case of $N N$ scattering we will discuss potentials $U ^ { N N }$ , negative defined as

$$
U ^ {N N} (\mathbf {r}) = \int d \mathbf {b} _ {\mathbf {1}} U ^ {n N} \left(\mathbf {b} _ {\mathbf {1}} - \mathbf {b}, z\right) \int d z _ {1} \rho \left(\mathbf {b} _ {\mathbf {1}}, z _ {1}\right). \tag {5}
$$

This quantity is the S.F. optical potential given in terms of a nucleon-nucleus $( n N )$ optical potential $U ^ { n N } ( \mathbf { r } )$ and the matter density $\rho ( \mathbf { b _ { 1 } } , z _ { 1 } )$ of the other nucleus. In the S.F. method, $U ^ { n N } ( \mathbf { r } )$ can be a phenomenological nucleon-target potential, Eq. (1), such as the DOM or the AB potentials of Ref. [32]. In the D.F. method, UNN is obtained from the microscopic densities ρP,T (r) $U ^ { N N }$ $\rho _ { P , T } ( \mathbf { r } )$

TABLE I: Energy-dependent optical-model parameters for the (AB) potential for $n { + } ^ { 9 } \mathrm { B e }$ . $r ^ { I } = 1 . 3$ fm, $a ^ { I } = 0 . 3$ fm at all energies. See also Table III and text.   

<table><tr><td>Elab
(MeV)</td><td>VR
(MeV)</td><td>rR
(fm)</td><td>aR
(fm)</td><td>Wsur
(MeV)</td><td>Wvol
(MeV)</td></tr><tr><td>20≤ Elab &lt;40</td><td>31.304 - 0.145Elab</td><td>1.647 - 0.005(Elab - 5)</td><td>0.3-0.0001Elab</td><td>1.65 + 0.365Elab</td><td>5.6 - 0.005(Elab - 20)</td></tr><tr><td>40≤ Elab &lt;111</td><td>”</td><td>”</td><td>”</td><td>16.25 - 0.05(Elab - 40)</td><td>5.5 - 0.01(Elab - 40)</td></tr><tr><td>111≤ Elab &lt;160</td><td>”</td><td>”</td><td>0.288</td><td>12.7</td><td>4.8</td></tr><tr><td>160≤ Elab &lt;200</td><td>”</td><td>”</td><td>”</td><td>12.7 - 0.025(Elab - 160)</td><td>4.8 - 0.025(Elab - 160)</td></tr><tr><td>200≤ Elab &lt;215</td><td>”</td><td>”</td><td>”</td><td>11.7 + 0.02(Elab - 200)</td><td>3.8 + 0.02(Elab - 200)</td></tr><tr><td>215≤ Elab ≤500</td><td>0</td><td>”</td><td>”</td><td>”</td><td>”</td></tr></table>

TABLE II: Energy-dependent optical-model parameters of the potential $n$ - $\mathrm { ^ { 1 2 } C }$ for $E _ { \mathrm { l a b } } \geq 1 6 0$ MeV. At lower energies, the parametrization is the same as for $^ { 9 }$ Be in Table I.   

<table><tr><td>Elab
(MeV)</td><td>VR
(MeV)</td><td>rR
(fm)</td><td>aR
(fm)</td><td>Wsur
(MeV)</td><td>Wvol
(MeV)</td></tr><tr><td>160 ≤ Elab &lt;200</td><td>31.304 - 0.145Elab</td><td>1.647 - 0.005(Elab - 5)</td><td>0.288</td><td>12.7 - 0.025(Elab - 160)</td><td>4.8 - 0.025(Elab - 160)</td></tr><tr><td>200 ≤ Elab &lt;215</td><td>”</td><td>”</td><td>”</td><td>11.7</td><td>3.8</td></tr><tr><td>215 ≤ Elab &lt;220</td><td>0</td><td>”</td><td>”</td><td>”</td><td>”</td></tr><tr><td>220 ≤ Elab ≤ 500</td><td>”</td><td>0.1</td><td>”</td><td>11.7 + 0.02(Elab - 220)</td><td>3.8 + 0.02(Elab - 220)</td></tr></table>

TABLE III: Energy-dependent optical-model parameter $r ^ { I }$ for the (AB) potential for $n { + } ^ { 9 } \mathrm { B e }$ and $n { + } ^ { 1 2 } \mathrm { C }$ used in calculations of S.F. $N N$ potentials.   

<table><tr><td>Elab
(MeV)</td><td>rI(9Be)
(fm)</td><td>rI(12C)
(fm)</td></tr><tr><td>30≤ Elab ≤160</td><td>1.4 - 0.0015Elab</td><td>1.32 - 0.0013Elab</td></tr><tr><td>Elab &gt;160</td><td>1.15</td><td>1.118</td></tr></table>

for the projectile and target respectively and an energydependent nucleon-nucleon (nn) cross section $\sigma _ { n n }$ , by using Eq. (4) for $U ^ { n N }$ with the notation $T = N$ in Eq. (5).

The reaction cross section, which depends only on the imaginary potential, in the eikonal formalism is given by the well known formula

$$
\sigma_ {R} = 2 \pi \int_ {0} ^ {\infty} b d b (1 - | S _ {P T} (\mathbf {b}) | ^ {2}) \tag {6}
$$

where

$$
\mid S _ {P T} (\mathbf {b}) \mid^ {2} = e ^ {2 \chi_ {I} (b)} \tag {7}
$$

is the probability that the projectile-target (PT) scattering is elastic for a given impact parameter $\mathbf { b }$ .

The imaginary part of the eikonal phase shift is given by

$$
\chi_ {I} (\mathbf {b}) = - \frac {1}{\hbar v} \int d z W ^ {P T} (\mathbf {b}, z), \tag {8}
$$

where, depending on the case studied, $W ^ { \mathrm { P T } }$ will be the imaginary part of one of the nucleon-target or nucleustarget potentials defined above.

# III. Results

# A. Nucleon- $^ { 1 2 } \mathbf { C }$

We start by showing in Fig. 1 the energy dependence of the total cross section calculated with an optical model code using the potential defined by Eqs. (1)-(3) and the parameters given in Tables I and II for $n { + } ^ { 9 } \mathrm { B e }$ and $n \mathrm { + ^ { 1 2 } C }$ . We include also the experimental data from Ref. [49]. It is interesting that the experimental data exhibit a clear scaling between the two nuclei, which the calculations reproduce accurately. Note that the two corresponding potentials have the same radius parameter but different radii, due to the difference in mass. Otherwise the other parameters differ only above 160 MeV. Reference [32] presented also results for $n { + ^ { 9 } }$ Be from a dispersive optical potential DOM calculation. DOM potentials exist also for $n { + } ^ { 1 2 } \mathrm { C }$ . Indeed in the same figure the green solid line shows the results obtained for a $^ { 9 }$ Be target using the DOM obtained for $^ { 1 2 }$ C [50]. It is amazing that, also for the DOM potential model, the same parametrization can be successfully applied to the two different targets. As was found in Ref. [32] for $^ { 9 }$ Be, the agreement shown here for the $\mathrm { ^ { 1 2 } C }$ target, between data and OM calculations, is remarkable and is comparable to that obtained for example in Ref. [41], where a coupled-channel (CC) technique was used. Note that also the authors of Ref. [41] stressed a similarity between parametrizations for 9Be and $\mathrm { ^ { 1 2 } C }$ . As we shall see in the following, the advantage of a simple OP approach, with respect to CC calculations, is that it can easily be used to build folding potentials for nucleus-nucleus scattering and also it can be used in eikonal and fully quantum-mechanical models [48; 51] of knockout from exotic nuclei.

In Fig. 2 the total experimental cross section for

TABLE IV: Comparison of the reaction cross sections of the $\bot 2$ C+12C system. Incident energies are indicated in the first column. Strong absorption radius parameters within the single and double folding methods are listed in the third column. The fourth column provides the volume integrals for active particles. The next columns contain the theoretical cross sections calculated with various densities. Before each of them are the rms radii of the corresponding imaginary potentials, some of which are shown in Fig. 5.   

<table><tr><td>Einc (MeV)</td><td>Model</td><td>rs (fm)</td><td>JW/APAT (MeVfm3)</td><td>rms radius (fm)</td><td>σNCSM (mb)</td><td>rms radius (fm)</td><td>σHF (mb)</td><td>rms radius (fm)</td><td>σHFB (mb)</td></tr><tr><td rowspan="2">83</td><td>S.F.</td><td>1.2</td><td>184</td><td>3.72</td><td>994</td><td>3.75</td><td>1008</td><td>3.78</td><td>1025</td></tr><tr><td>D.F.</td><td>1.22</td><td>279</td><td>3.29</td><td>957</td><td>3.36</td><td>995</td><td>3.43</td><td>1027</td></tr><tr><td rowspan="2">300</td><td>S.F.</td><td>1.18</td><td>151</td><td>3.57</td><td>760</td><td>3.60</td><td>768</td><td>3.64</td><td>780</td></tr><tr><td>D.F.</td><td>1.11</td><td>241</td><td>3.29</td><td>791</td><td>3.36</td><td>815</td><td>3.43</td><td>842</td></tr></table>

TABLE V: Results for the $\mathrm { ^ { 2 0 } N e + ^ { 1 2 } C }$ scattering. The strong absorption radius parameter is listed in the third column, and the fourth and the fifth columns give the predicted and the experimental [10] reaction cross sections. The HFB density is used for $^ { 2 0 }$ Ne.   

<table><tr><td>Einc(MeV)</td><td>Model</td><td>rs(fm)</td><td>σtheo (mb)</td><td>σexp (mb)</td></tr><tr><td rowspan="2">30</td><td>S.F.</td><td>(1.35) 1.33</td><td>(1478) 1456</td><td>1550 ±75</td></tr><tr><td>D.F.</td><td>1.37</td><td>1560</td><td></td></tr><tr><td rowspan="2">100</td><td>S.F.</td><td>(1.27) 1.23</td><td>(1327)1211</td><td>1161 ± 80</td></tr><tr><td>D.F.</td><td>1.21</td><td>1206</td><td></td></tr><tr><td rowspan="2">200</td><td>S.F.</td><td>(1.21)1.11</td><td>(1193) 1012</td><td>1123 ± 80</td></tr><tr><td>D.F.</td><td>1.15</td><td>1079</td><td></td></tr><tr><td rowspan="2">300</td><td>S.F.</td><td>(1.21)1.12</td><td>(1181)1001</td><td>1168 ± 100</td></tr><tr><td>D.F.</td><td>1.13</td><td>1062</td><td></td></tr></table>

$n \mathrm { + } ^ { \mathrm { { 1 2 } } } \mathrm { { C } }$ is shown again by red symbols while the blue full curve and green double-dotted-dashed line are results of the optical model and eikonal calculations, Ref.[7], respectively, with the potential of Eqs. (1)-(3) and Table II. The orange dot-dashed line is the eikonal calculation with the s.f. potential (4). These results indicate that, while the simple eikonal approximation with the phenomenological potential works well from about 100 MeV incident energy, the eikonal model with the folded potential starts to work well only from about 200 MeV. Clearly the Glauber and folding models miss some effects of excitation modes in the target, beyond the simple nn free scattering concept. The optical model with the phenomenological $n$ -T potential includes instead such effects. In this respect, we first note that the $U _ { \rho } ^ { n I ^ { \prime } }$ potential of Eq. (4) has the same range and profile as the target density because $\sigma _ { n n }$ and $\alpha _ { n n }$ are simple scaling factors. To understand better this point Fig. 3 shows the imaginary potentials calculated at 300 MeV with the densities indicated in the legend from Refs. [52], [53]. Hartree-Fock-Bogoliubov (HFB) densities were calculated with the code HFBTHO [54] and the Skyrme interaction SkM $^ *$ [55]. Using other Skyrme interactions does not produce substantial differences. No-core-shell-

TABLE VI: Results for system $^ n$ Ca- $^ { 1 2 }$ C at $E = 2 8 0 A$ MeV. The strong absorption radius parameter is listed in the third column, and the fourth and the fifth columns give the predicted and the experimental [44] reaction cross sections. Statistical and systematic errors for the experimental values are given in the first and second parentheses respectively. The root-mean-square (rms) matter radius of the HFB projectile density is listed in the last column.

<table><tr><td>Nucleus</td><td>Model</td><td>rs(fm)</td><td>σtheo (mb)</td><td>σexp (mb)</td><td>rms radius (fm)</td></tr><tr><td rowspan="2">42Ca</td><td>S.F.</td><td>(1.23)1.14</td><td>(1598) 1388</td><td>1463(13)(6)</td><td>3.38</td></tr><tr><td>D.F.</td><td>1.16</td><td>1460</td><td></td><td></td></tr><tr><td rowspan="2">43Ca</td><td>S.F.</td><td>(1.22)1.14</td><td>(1614)1402</td><td>1476(11)(6)</td><td>3.40</td></tr><tr><td>D.F.</td><td>1.17</td><td>1476</td><td></td><td></td></tr><tr><td rowspan="2">44Ca</td><td>S.F.</td><td>(1.23)1.15</td><td>(1630) 1417</td><td>1503(12)(6)</td><td>3.42</td></tr><tr><td>D.F.</td><td>1.16</td><td>1490</td><td></td><td></td></tr><tr><td rowspan="2">46Ca</td><td>S.F.</td><td>(1.24)1.15</td><td>(1683)1466</td><td>1505(8)(6)</td><td>3.50</td></tr><tr><td>D.F.</td><td>1.17</td><td>1543</td><td></td><td></td></tr><tr><td rowspan="2">48Ca</td><td>S.F.</td><td>(1.23)1.16</td><td>(1714)1495</td><td>1498(17)(6)</td><td>3.50</td></tr><tr><td>D.F.</td><td>1.18</td><td>1573</td><td></td><td></td></tr></table>

model (NCSM) densities were obtained by using the nn4lo [25] interaction. We provide also the volume integrals per particle and rms radius values. The former $\left( J _ { W } / A _ { T } \right)$ have all the same values because all densities are normalized to the number of nucleons. The latter (rms values) have very similar values although in the internal parts the potentials are quite different. The phenomenological potential is completely different, being very shallow at the interior and having instead a pronounced surface peak and long tail. Its volume integral is smaller than that of the s.f. potentials while its rms radius is much larger. Indeed Fig. 4 shows again the experimental cross sections as in Figs. 1 and 2 but this time, besides the optical model calculation with the phenomenological potential, results are shown of the eikonal approximation Ref.[7] with the s.f. potentials (4) of Fig. 3 obtained with different densities. One can notice the

![](images/ccaa444bd4c8f8f10fcf4e00886efd8aab8359c54539620b737eaa4ad006ab66.jpg)  
FIG. 1: (Color online) Total experimental and calculated cross sections. Lower blue symbols are for $n { + } ^ { 9 } \mathrm { B e }$ , upper red symbols for $n { + } ^ { 1 2 } \mathrm { C }$ . The optical model calculations are given by the orange and cyan dashed lines, respectively. The solid green line is a calculation made with a DOM potential obtained for $n \mathrm { + } ^ { \mathrm { { 1 2 } } } \mathrm { { C } }$ and applied to $n { + ^ { 9 } }$ Be [50].

![](images/1e86fc78e04e9427bd00a19ba7a1e4ecc89efcc89b83c21177b4ebb2626f8a88.jpg)  
FIG. 3: (Color online) $n { + } ^ { 1 2 } \mathrm { C }$ potentials calculated with various model densities at 300 MeV; see legend and text. The blue line is the potential deduced from the profile function of Ref. [16]. The magenta tick curve is the phenomenological potential of Eqs. (1)-(3) and Table II.

![](images/4401c264e0360212161ba147040903ed2c4bba7a7cb393c1856f5c1cac8dfe15.jpg)  
FIG. 2: (Color online) Total experimental and calculated cross sections for $n \mathrm { + ^ { 1 2 } C }$ . Red symbols are the data. The blue full curve and green double-dotted-dashed line are results of optical model and eikonal calculations respectively, with the potentials (1)-(3) and Table II. The orange dot-dashed line is the eikonal calculation with the s.f. potential (4).

![](images/c550023d8e8a033daf8effdd2a70fcfc95af08c85d1f6cad8edc2de75c89088f.jpg)  
FIG. 4: (Color online) Total experimental and calculated cross sections for $n { + } ^ { 1 2 } \mathrm { C }$ . Red symbols are the data. The blue curve is the calculation by the optical model with the phenomenological potential. The other curves are calculations using the s.f. potential (4) and Fig. 3 using fixed $\alpha _ { n n }$ values in Eq. (4) appropriate for 300 MeV. The brown dashed curve labeled as HFB N uses the energy dependent $\alpha _ { n n }$ from Refs. [18; 43; 45]. Note that they are known only from 40 MeV. See text for details.

small effect of changing the target density. However, it is interesting to note that the cross section values seem to scale with the rms radius of the potential. This result suggests that only the surface behavior of the potential (and of the target density) determine the value of the cross section, and that in turn it is only the rms

radius of the target density that can be deduced from data, a confirmation of the simple geometrical nature of the Glauber model. In this figure the calculations marked as HFB N were made from 40 MeV using the HFB density and $\sigma _ { n n }$ and $\alpha _ { n n }$ taken from the parametrization of Refs. [18; 43; 45] (brown dashed curve), while in the other

calculations with various densities we kept $\alpha _ { n n }$ fixed at the value appropriate to 300 MeV just to show the small dependence on the density. Note that a precise evaluation of the $\alpha _ { n n }$ parameters is a delicate issue which to our knowledge has not been fully resolved to date; see in particular Fig. 4 of [56].

# B. Nucleus- $^ { 1 2 } \mathbf { C }$

We turn now to the study of nucleus-nucleus scattering by building a D.F. potential and a S.F. potential according to Eq. (5). Note that s.f. refers to a potential for $n$ -T scattering, built on the target density, Eq. (4), while in the case of $N N$ scattering S.F. indicates a potential built using in Eq. (5) the projectile density and the $n$ -T phenomenological potential, Eq. (1). D.F. refers to a $N N$ potential obtained using Eq. (4) in Eq. (5).

In Fig. 5 a number of such imaginary potentials are shown for the $^ { 1 2 }$ C-12C system at 83 and 300 MeV as indicated in the legend. We show D.F. potentials obtained with the HF and no-core-shell-model (NCSM) densities obtained from the nn4lo [25] interaction and S.F. potentials obtained with the potentials of Table II, varying the $r ^ { I }$ values and the NCSM and HFB densities. We will see in the following that, in order to reproduce the experimental cross sections, the $r ^ { I }$ parameter needs to be energy dependent when the $n$ -T phenomenological potential is used to build up the $N N$ potential. The lower figure shows the potentials from the NCSM density at $3 0 0 A$ MeV, where the D.F. has been renormalized by a factor 0.4 in order to compare it directly to the S.F. potential and to emphasize the difference in shape and rms radius. The D.F. potentials shown in panel (a) of Fig. 5 are deeper and have smaller rms radii than the S.F. potentials which are characterized instead by longer tails and larger rms values while their volume integrals are smaller than those of the D.F. potentials; see also Table IV. In the same table the values of calculated reaction cross sections at 83 and $3 0 0 A$ MeV are given. Incident energies are indicated in the first column, strong absorption radius parameters within the single and D.F. methods using the HFB densities are listed in the third column, while the fourth column provides the volume integrals for active particles of the imaginary potentials. The next columns contain the theoretical cross sections calculated with various densities. On the left-hand side of each of them are the rms radii of the corresponding imaginary potentials shown in Fig. 5. Typically an increase of 5% in the rms value results in a similar increase in the calculated reaction cross section, Eq.(6), similarly to what we have noticed for the $n$ -target potential. The values of Table IV indicate that the volume integrals are the same for all densities, as they are normalized to the number of particles, while the rms values are different. However, they obviously depend on the energy and on the method used to build the potential. On the other hand for each D.F. potential the rms values are independent of the energy

![](images/4751792ff57cadd103d8e635495aeef02537f705293e276cb7cbad57bc47578e.jpg)

![](images/c1b04af50f0b072e2dfb58e7daeee7a1d427b402a46ff265bb121c2982d700b3.jpg)  
FIG. 5: (Color online) (a) Imaginary part of the $_ { 1 2 }$ C- 12C optical potential at 83 and 300 MeV as indicated in the legend. The D.F. potentials shown are obtained with the HF and NCSM densities. The S.F. potentials are obtained with the potentials of Table II varying the $r ^ { I }$ values and the NCSM and HFB densities. See text for details. The full magenta line with blue uses the MOL potential obtained from [16]. Panel (b) contains the potentials from the NCSM density at 300A MeV where the D.F. has been renormalized by a factor 0.4 in order to emphasize the difference in shape and rms radius.

because they are just determined by the densities. This is consistent with the results of Ref. [35]. The accuracy of our results can be discussed for example in comparison to Refs. [29; 30]. In that work the data for $^ { 1 2 } \mathrm { C } +$ 12C elastic scattering were studied at $1 0 0 A$ MeV using microscopic coupled-channel calculations with the explicit goal to check the effect of repulsive three-body forces. The potential between the colliding nuclei was determined by the double folding method with three different complex $g$ -matrix interactions, and also the reaction cross section

![](images/6615fde2d6c54c805918dc1649dc048902f8e373dd26fc100e73699524c73e1f.jpg)

![](images/eb2914359a5e74a76e47906302dff79d31b392eea941b6c6bebf105a9a612270.jpg)  
FIG. 6: Comparison of experimental reaction cross sections (circles with error bars) and theoretical values according to Eq.(6) within S.F. and D.F. potentials (dot-dashed and full lines respectively), for the scattering of 12C+ 9Be (a) and 12C+ 12C (b). The magenta dashed lines in both panels represent the S.F. results obtained using a fixed value $r ^ { I } = 1 . 3$ fm for the radius parameter of the imaginary phenomenological optical potential. The dot-dashed lines correspond to an energy dependent $r ^ { I }$ . according to Table III. See text for details. Data points are from Ref. [19]. In the lower panel the large red points are from Ref. [10].

was calculated. The calculated value which agreed better with the data was $\sigma _ { R } = 9 5 0$ mb, obtained with the MPa interaction [57] and a renormalization factor $N _ { W } = 0 . 5 7$ for the imaginary potential. The MPa interaction includes repulsive three-body forces. It is interesting to note that with our S.F. potential we obtain 969 and 953 mb with the HFB and HF densities respectively, without any renormalization for the potential, while the experimental value is 962 mb. With the D.F. potential and the

HFB densities we obtain 980 mb. Also, similarly to what is shown in Fig. 6 and Table IV for the D.F. and S.F. potentials at 300 MeV, we find that at 100 MeV the depth of the D.F. potential should be renormalized by a factor 0.4 with respect to the S.F. potential depths to make their values similar. However as noticed at 300 MeV, also at 100 MeV the rms radii would be very different, namely 3.75 and 3.43 fm for the S.F. and D.F. potentials respectively. This confirms the fact that a simple D.F. potential calculated according to Eqs. (4) and (5) would be far too absorptive because it does not contain in-medium effects which instead are partially contained in the microscopic potential of Ref. [30] thanks to the introduction of the three-body repulsive force. Thus such potentials need a not too strong renormalization. In light of such microscopic method results, one possible interpretation for our surface dominated $n$ -T phenomenological potentials which give rise to relatively shallow but ”wide” $N N$ potentials, cf. Figs. 3 and 5, is that they contain in a effective way the effects of short range repulsion pushing most nn interactions to the surface.

Another interesting comparison can be done with the MOL method of Ref. [16], in particular their Eq.(10) for the $S$ matrix,

$$
\exp \left(i \tilde {\chi} _ {O L A} (\mathbf {b})\right) = \exp \left(- \int d \mathbf {r} \rho_ {p} (\mathbf {r}) \Gamma_ {N T} (\mathbf {b} + \boldsymbol {\xi})\right), \tag {9}
$$

contains the profile function

$$
\Gamma_ {N T} (\mathbf {b}) = \left(\sigma_ {1} (1 - i \alpha_ {1}) \frac {e ^ {- \mathbf {b} ^ {2} / 2 \beta_ {1}}}{4 \pi \beta_ {1}} + \sigma_ {2} (1 - i \alpha_ {2}) \frac {e ^ {- \mathbf {b} ^ {2} / 2 \beta_ {2}}}{4 \pi \beta_ {2}}\right), \tag {10}
$$

with $\sigma _ { 1 , 2 }$ and $\beta _ { 1 , 2 }$ given by the values in Table I of [16] and $\rho _ { p }$ given by Eq. (75) and Table 2 of [58]. It could be interpreted as a S.F. model in which $\Gamma _ { \mathrm { N T } }$ would be the result of the $z$ -integration of an effective nucleon-target potential of Gaussian shape with imaginary part

$$
W _ {M O L} (\mathbf {r}) = \frac {1}{2} \hbar v \left(\sigma_ {1} \frac {e ^ {- r ^ {2} / 2 \beta_ {1}}}{(2 \pi \beta_ {1}) ^ {3 / 2}} + \sigma_ {2} \frac {e ^ {- r ^ {2} / 2 \beta_ {2}}}{(2 \pi \beta_ {2}) ^ {3 / 2}}\right). \tag {11}
$$

Such a potential, shown in Fig. 3 by the blue line for $n { + } ^ { 1 2 } \mathrm { C }$ , shows a repulsive behavior at very short distances, which could be interpreted as an effective representation of short distance repulsion originating in the three-body terms of the chiral interaction as used for example in the microscopic model of [30]. On the other hand in Fig. 5 the full magenta line with blue dots shows the corresponding $N N$ imaginary potential for the system $^ { 1 2 } \mathrm { C } + ^ { 1 2 } \mathrm { C }$ at $3 0 0 A$ MeV. It has a volume integral of 184 MeV fm3 and rms radius 3.48 fm, consistent with our S.F. results of Table IV. In particular we notice the same large distance behavior as in our best S.F. potential. Thus the modifications to the MOL parameters introduced in Ref. [19], which the authors mentioned are not easily interpreted from the physical point of view, might represent an effective way to obtain the correct energy

and radial dependence of their ”effective” NT imaginary potential.

From the discussion of our results it appears that Hartree-Fock and HFB densities are the best for reproducing the experimental reaction cross section values, and indeed they are used in most codes related to exotic nuclei reactions. Besides the system $^ { 1 2 } \mathrm { C } + ^ { 1 2 } \mathrm { C }$ , using HFB densities we study also the systems $^ { 9 } \mathrm { B e } + ^ { 1 2 } \mathrm { C }$ , $^ { 2 0 } \mathrm { N e } + ^ { 1 2 } \mathrm { C }$ , and $_ n$ Ca+ 12C. The energies of the scattering and cross sections and other relevant parameters are given in Tables IV, V, and VI. In particular as a significative parameter we provide also the strong-absorption radius $R _ { s }$ [59; 60], obtained from the S matrices as the radius where | SPT(Rs) |2= 12 , and in particular the ”strong absorption radius parameter” $r _ { s }$ extracted from

$$
R _ {s} = r _ {s} \left(E _ {\mathrm {i n c}}\right) \left(A _ {P} ^ {1 / 3} + A _ {T} ^ {1 / 3}\right). \tag {12}
$$

The values of this parameter in Tables IV, V, and VI indicate also that the S.F. potentials provide longer range absorption than the D.F. potential. The cross sections and rms radii in Tables V, and VI were calculated with two different options for the $r ^ { I }$ parameter of the phenomenological imaginary potential. The values in parentheses were obtained with $r ^ { I } = 1 . 3$ fm while the other values were obtained with the prescription of Table III. The best agreement with the data is obtained with an energy dependent $r ^ { I }$ , as we discuss further in the following.

Figure 6 presents the energy dependence of the calculated and experimental reaction cross sections [10; 19] for 9Be+ 12C and 12C+ 12C. There are two curves showing results obtained within the S.F. model: one (dot-dashed line), using in the phenomenological imaginary part of the $n$ -T potential the radius parameter $r ^ { I }$ which depends on the incident energy according to Table III, provides the best agreement with the data while the other (dashed line) using the standard $r ^ { I } = 1 . 3$ fm, corresponds to values larger than the data. This is consistent with the results in Tables V, and VI. It is interesting that the small change in $r ^ { I }$ brings the S.F. results in much better agreement with the data. The full lines are D.F. results which are in between the two S.F. curves. What we have found is interesting because it agrees with what has been discussed in other works like Ref. [19]. Namely it shows that modifications might be necessary in reaction models when including ingredients which successfully reproduce simpler reactions. In the case of the D.F. model it is evident that not only is the idea of a $N N$ reaction being a collection of nn free reactions is too simple, but so is the S.F. description of a collection of free, independent nucleons interacting with a nucleus via optical model po-

tentials. However, at the moment it seems that simple, understandable modifications are sufficient to reproduce the data. For example, the reduction in the radius parameter found useful in our model might indicate that, when a nucleus scatters from another nucleus, as the energy increases its nucleons interact with those of the other nucleus at smaller distances than a free nucleon interacts with the nucleons of a nucleus.

# IV. Conclusions

In this paper we obtained an excellent phenomenological $n$ - 12C optical potential which fits the total cross sections up to 500 MeV. We then single folded it with various projectile densities and studied the systems $^ { 1 2 } \mathrm { C } +$ 12C, 9Be+ 12C, 20Ne+ 12C, and $^ n$ Ca+ $\mathrm { ^ { 1 2 } C }$ , finding that the energy dependence of the reaction cross section data can be fitted by introducing a simple energy dependence in the radius parameter of the imaginary $n$ -target potential. D.F potentials were also calculated and it was shown once again that they are too deep and too ”narrow.” On the other hand we have shown that the MOL method to calculate phase shifts, in which nucleon-target multiple scattering effects are taken into account, would provide potentials with characteristics similar to ours. The general conclusion of our study is then that it is necessary that the imaginary part of microscopic and/or semi-phenomenological optical potentials contains higher order and in-medium effects. Also it would be useful to study further the importance of short range repulsion and/or or the effect of the three-body force which might be at the origin of the necessary reduction of the strength of the potential at short distances. As a next step our S.F. method could be also tested by evaluating the $S$ matrices that are necessary in the eikonal formalism of nuclear breakup.

# Acknowledgements

We are very grateful to Mack Atckinson for providing us with the unpublished calculations with the DOM potential shown in Fig.1, to Petr Navr´atil and Michael Gennari for the numerical values of the NCSM densities, and to Carlotta Giusti and Matteo Vorabbi for comments on the manuscript. One of us (I.M.) thanks M. Gaidarov and colleagues for allowing her to run and use results from the code HFBTHO[54].

[4] J.P. Vary and C.B. Dover, in Proceedings of the Second High Energy Heavy-Ion Summer Study, Lawrence Berkeley National Laboratory, July, 1974 (unpublished).   
[5] G.R. Satchler and W.G. Love, Phys. Rep. 55 183 (1979).   
[6] G.R. Satchler, in Proceedings of La Rabida international Summer School on Heavy Ion Collisions, La Rabida (Huelva), Spain,June 7-19, 1982 (unpublished). https://inis.iaea.org/search/search.aspx?orig q=RN:1472   
[7] R. J. Glauber, in Lectures in Theoretical Physics, Vol. 1, edited by W. E. Brittin and L. G. Dunham (Interscience, New York, 1959), p. 315.   
[8] A. Bonaccorso, ”A microscopic theory of the alpha-nucleus optical potential”, Ph.D. thesis, University of Oxford, 1980 (unpublished), https://ora.ox.ac.uk/objects/uuid:d77df433-a09d-46c2-b94b-4d032fcf39b4   
[9] R.M. De Vries, J.C. Peng, Phys. Rev. C 22 (1980) 1055.   
[10] S. Kox et al., Phys. Rev. C35,1678 (1987).   
[11] Y. P. Xu and D. Y. Pang, Phys. Rev. C 87, 044605 (2013).   
[12] J. P. Jeukenne, A. Lejeune, and C. Mahaux, Phys. Rev. C 16, 80 (1977).   
[13] E. Bauge, J. P. Delaroche, and M. Girod,Phys. Rev. C 63, 024607 (2001).   
[14] Y. Lu, J. Lei, and Z. Ren, Phys. Rev. C 108, 024612 (2023).   
[15] A. J. Koning , J. P. Delaroche, Nucl. Phys. A 713 231 (2003).   
[16] B. Abu-Ibrahim and Y. Suzuki, Phys. Rev. C 62, 034608 (2000), Phys. Rev. C 61, 051601(R) (2000).   
[17] M.S. Hussein, R. A. Rego, C. A. Bertulani, Phys. Rep. 201, (1991) 279N334. ˜   
[18] C. A. Bertulani, and C. De Conti, Phys. Rev. C 81, 064603 (2010).   
[19] M. Takechi, M. Fukuda, M. Mihara, K. Tanaka, T. Chinda, T. Matsumasa, M. Nishimoto, R. Matsumiya, Y. Nakashima, H. Matsubara, K. Matsuta, T. Minamisono, T. Ohtsubo, T. Izumikawa, S. Momota, T. Suzuki, T. Yamaguchi, R. Koyama, W. Shinozaki, M. Takahashi, A. Takizawa, T. Matsuyama, S. Nakajima, K. Kobayashi, M. Hosoi, T. Suda, M. Sasaki, S. Sato, M. Kanazawa, and A. Kitagawa, Phys. Rev. C 79, 061601(R) (2009).   
[20] D. T. Tran, H. J. Ong, T. T. Nguyen, I. Tanihata, N. Aoi, Y. Ayyad, P. Y. Chan, M. Fukuda, T. Hashimoto, T. H. Hoang, E. Ideguchi, A. Inoue, T. Kawabata, L. H. Khiem, W. P. Lin, K. Matsuta, M. Mihara, S. Momota, D. Nagae, N. D. Nguyen, D. Nishimura, A. Ozawa, P. P. Ren, H. Sakaguchi, J. Tanaka, M. Takechi, S. Terashima, R. Wada, and T. Yamamoto, Phys. Rev. C 94, 064604 (2016).   
[21] W.H. Dickhoff and R.J. Charity, Prog.Part. Nucl. Phys. 105 252 (2019).   
[22] M. Burrows, C. Elster, S. P. Weppner, K. D. Launey, P. Maris, A. Nogga, and G. Popa, Phys. Rev. C 99, 044603 (2019).   
[23] A. Idini, C.Barbieri, P. Navr´atil, Phys. Rev. Lett. 123, 092501 (2019).   
[24] M. Vorabbi, M. Gennari, P. Finelli, C. Giusti, P. Navr´atil, and R. Machleidt, Phys. Rev. C103, 024604 (2021).   
[25] D. R. Entem, R. Machleidt, and Y. Nosyk, Phys. Rev. C 96, 024004 (2017).   
[26] P. Finelli, M. Vorabbi, C.Giusti, J. Phys.: Conf. Ser. 2453, 012026 (2023), and refrences therein.

[27] T. Furumoto, K. Tsubakihara, S. Ebata, W. Horiuchi, Phys. Rev. C 99, 034605 (2019).   
[28] T. Furumoto, Y. Sakuragi, and Y. Yamamoto Phys. Rev. C 78, 044610 (2008)   
[29] T. Furumoto, W. Horiuchi, M. Takashina, Y. Yamamoto, and Y. Sakuragi Phys. Rev. C 85, 044607 (2012).   
[30] Qu,W.W., Zhang,G.L., Terashima,S., Furumoto,T., 68. Ayyad,Y., Chen,Z.Q., Guo,C.L., Inoue,A., Le,X.Y., Ong,H.J., Pang,D.Y., Sakaguchi,H., Sakuragi,Y., Sun,B.H., Tamii,A., Tanihata,I., Wang,T.F., Wada,R., Yamamoto,Y., Phys Rev. C95, 044616 (2017) and references therein.   
[31] M. Toyokawa, M. Yahiro, T. Matsumoto, K. Minomo, K. Ogata, and M. Kohno, Phys. Rev. C92, 024618 (2015) and references therein.   
[32] A. Bonaccorso and R. J. Charity, Phys. Rev. C 89, 024619 (2014).   
[33] C. Mahaux and R. Sartor, Adv. Nucl. Phys. 20, 1 (1991).   
[34] A. Bonaccorso, F. Carstoiu, R. J. Charity, R. Kumar and G. Salvioni, Few-Body Syst. 57, 331 (2016).   
[35] A. Bonaccorso, F. Carstoiu, R. J. Charity, Phys. Rev. C 94, 034604 (2016).   
[36] Imane Moumene and Angela Bonaccorso, Nucl. Phys. A1006 122109 (2021).   
[37] D. Boscolo et al., Front. Oncol. 11, 737050 (2021) https://doi.org/10.3389/fonc.2021.737050   
[38] C. Hebborn, T. R. Whitehead, A. E. Lovell, and F. M. Nunes, Phys. Rev. C 108, 014601 (2023).   
[39] F Luoni, F Horst, C A Reidel, A Quarz, L Bagnale, L Sihver, U Weber, R B Norman , W de Wet and M Giraudo, G Santin, J W Norbury and M Durante, New Journal of Physics 10, 101201(2021). https://dx.doi.org/10.1088/1367-2630/ac27e1   
[40] Malouff TD, Mahajan A, Krishnan S, Beltran C, Seneviratne DS and Trifiletti DM Front. Oncol. 10:82. doi: 10.3389/fonc.2020.00082 https://kcch.kanagawapho.jp/i-rock/english/medical/   
[41] S. Kunieda et al., Eur. Phys. J. A 59, 2 (2023).   
[42] I. Tanihata et al., Phys. Letters B 160 (1985) 380.   
[43] B. Abu-Ibrahim, W. Horiuchi, A. Kohama, and Y. Suzuki, Phys. Rev. C 77, 034607 (2008)   
[44] M. Tanaka et al. Phys. Rev. Lett. 124, 102501 (2020).   
[45] W. Horiuchi, Y. Suzuki, B. Abu-Ibrahim, and A. Kohama, Phys. Rev. C 75, 044607 (2007).   
[46] A. Ozawa et al., Nucl. Phys. A 691, 599 (2001). A. Ozawa, AIP Conf. Proc. 865, 57 (2006); http://dx.doi.org/10.1063/1.2398828   
[47] Isao Tanihata, Herve Savajols, Rituparna Kanungo, Prog. Part. Nucl. Phys. 68 (2013) 215, and references therein.   
[48] Angela Bonaccorso, Progress in Particle and Nuclear Physics, 101(2018) 1-54, and references therein.   
[49] EXFOR nuclear data library [http://www.nds. iaea.org/exfor/exfor.htm].   
[50] M. Atckinson, (private communication).   
[51] Jin Lei, A. Bonaccorso, Phys. Lett. B 813, 136032 (2021).   
[52] R. B. Wiringa, R. Schiavilla, S. C. Pieper, and J. Carlson, Phys. Rev. C 89, 024305 (2014); M. Piarulli, S. Pastore, R. B. Wiringa, S. Brusilow, and R. Lim, ibid. 107, 014314 (2023), https://www.phy.anl.gov/theory/research/density/, and references therein.   
[53] V. Som`a, P. Navr´atil, F. Raimondi, C. Barbieri, and T. Duguet, Phys. Rev. C 101, 014318 (2020).

[54] M. V. Stoitsov, N. Schunck, M. Kortelainen, N. Michel, H. Nam, E. Olsen, J. Sarich, and S. Wild, Comput. Phys. Commun. 184, 1592 (2013); M. V. Stoitsov, J. Dobaczewski, W. Nazarewicz, and P. Ring, ibid. 167, 43 (2005).   
[55] J. Bartel, E. Quentin, M. Brack, C. Guet and H.-B. Hakansson, Nucl. Phys. A 386 (1982) 79.   
[56] P. Schwaller et al., Nuclei. Phys. A316 317(1979).

[57] Y. Yamamoto, T. Furumoto, N. Yasutake, and Th.A. Rijken, 1 Eur. Phys. J. A (2016) 52: 19   
[58] Y. Ogawa, K. Yabana, and Y. Suzuki, Nucl. Phys. A543 722 (1992).   
[59] R. Bass, Nuclear Reactions with Heavy Ions, Springer-Verlag, Berlin, Heidelberg, New York, 1980, Sec. 3.3.   
[60] A. Bonaccorso, D. M. Brink and L. Lo Monaco, J. Phys. G 13 1407 (1987).