# A Data-Driven Density Functional Model for Nuclear Systems

Zu-Xing Yang, $1 , 2$ Xiao-Hua Fan,2, 3, 1 Zhi-Pan Li,2 and Haozhao Liang $3 , 4$

$^ { 1 }$ RIKEN Nishina Center, Wako, Saitama 351-0198, Japan

$^ 2$ School of Physical Science and Technology, Southwest University, Chongqing 400715, China

$^ 3$ Department of Physics, Graduate School of Science,

The University of Tokyo, Tokyo 113-0033, Japan

$^ 4$ RIKEN Interdisciplinary Theoretical and Mathematical Sciences Program, Wako 351-0198, Japan

Through ensemble learning with multitasking and complex connection neural networks, we aggregated nuclear properties, including ground state charge radii, binding energies, and single-particle state information obtained from the Kohn-Sham auxiliary single-particle systems. Compared to traditional density functional theory, our model can more accurately characterize nuclear ground state information. Aiming at binding energy, the root mean square error is reduced to 450 keV. Although the complexity involving the nuclear interaction is skipped, the model has not completely devolved into a black box. Leveraging the correlation between densities and binding energies, we calculate the neutron skin thickness of 208Pb to be 0.223 fm. This model will advance our understanding of nuclear properties and accelerate the integration of machine learning into modern nuclear physics.

# I. INTRODUCTION

Nuclear mass is a fundamental property for extracting various nuclear structure information including nuclear pairing correlation, shell effect, deformation transition, nuclear interactions, etc [1, 2]. In astrophysics and reaction research, nuclear mass also plays a crucial role in determining the nucleosynthesis composition on the surface of neutron stars [3] and the origin of elements in the Universe [4].

Considering the profound impact of mass in nuclear physics, a substantial amount of research has been devoted to enhancing the description and predictive accuracy. Traditional theoretical models, such as the Bethe–Weizs¨acker mass formula [5], finite-range droplet model [6], and the Weizs¨acker–Skyrme model [7], as well as the Hartree–Fock–Bogoliubov mass model [8–10] and the relativistic mean-field model [11, 12], typically exhibit an accuracy range between 0.3 MeV and 3 MeV. Currently, machine learning-based research is becoming gradually the main force on the path to achieving higher accuracy. Utama et al. introduced the application of Bayesian neural networks to the residuals between theoretical and experimental data [3], achieving remarkable success with an improvement in mass accuracy of approximately $4 0 \%$ . The accuracy further reached an impressive 84 keV through the incorporation of nuclear pairing and shell effects [13], coupled with meticulous design for multiple networks [14]. At the same time, machine learning approaches such as radial basis function [15, 16], kernel ridge regression [17, 18], support vector machine [19], Gaussian process [20–24], decision tree [25, 26], and others were also employed to describe the nuclear masses. From successful cases, another key insight we gather is ensemble learning, which involves integrating multiple learning models to make posterior predictions, also known as Bayesian model averaging [22–24, 27] or world averaging [3].

With the description accuracy approaching the limits, the research emphasis should revert to the fundamental

connections among observables for a deeper understanding of the physics behind the phenomena. Previously, the Kohn-Sham Network (KSN) was proposed to temporarily break free from the constraints of interactions and describe the nuclear single-particle wave functions as well as the shell corrections induced by Bardeen-Cooper-Schrieffer (BCS) correlations [28]. Under the calibration from experimental charge radii, the KSN-generated proton information received subtle adjustments, which implies that the connection between nuclear binding energies and densities needs to be re-established.

In this study, we will establish neural network mappings from the nuclear mass number density, kinetic density, and spin-orbit density to the nuclear binding energy, aiming to replenish the KSN. We will explore network performance, generalization capability, and the impact of ensemble learning on description accuracy and outlook the future research directions. Simultaneously, according to the correlation between densities and binding energies, the neutron skin thickness will also be further discussed.

# II. NEURAL NETWORK ARCHITECTURE

To establish the most realistic mapping relationship, we focus on two main aspects for generating inputs. On one hand, we derive features that empirically encompass known physical information based on proton $Z$ and neutron numbers $N$ including valence proton number $Z _ { v }$ , valence neutron number $N _ { v }$ , proton hole number $Z _ { h }$ , neutron hole number $N _ { h }$ , proton shell number $Z _ { s }$ , neutron shell number $N _ { s }$ , shell effect parameter $S$ , proton number parity $Z _ { P }$ , Neutron number parity $N _ { P }$ , and parity parameter $P$ . Taking the proton as example, the relations among $Z$ , $Z _ { s }$ , $Z _ { v }$ , $Z _ { h }$ , $Z _ { P }$ satisfy

$$
Z = M \left(Z _ {s}\right) + Z _ {v}
$$

$$
Z _ {h} = M \left(Z _ {s} + 1\right) - Z _ {v} \tag {1}
$$

$$
Z _ {P} = Z \mod 2
$$

with the magic number list $M$ being {8, 20, 28, 50, 82, 126, 184}. The shell effect parameter $S$ and the parity parameter $P$ can be denoted as [13]

$$
S = d _ {p} \times d _ {n} / (d _ {p} + d _ {n}) \mathrm {a n d} P = [ (- 1) ^ {Z} + (- 1) ^ {N} ] / 2 (2)
$$

with $d _ { p }$ ( $d _ { n }$ ) representing the difference between the actual proton (neutron) numbers $Z$ ( $N$ ) and the nearest magic number. The $Z$ , $N$ , $Z _ { v }$ , $N _ { v }$ , $Z _ { h }$ , and $N _ { h }$ share the same dimension, we denote them as $X _ { 1 }$ for uniform normalization in the neural network, while $Z _ { s }$ , $N _ { s }$ , $S$ , $Z _ { P }$ , $N _ { P }$ , and $P$ would be a supplement organized as $X _ { 2 }$ . In addition to clearly defined shell effects and odd-even staggering, this part also plays a role in supplementing some beyond-mean-field physics that is challenging to describe within the Kohn-Sham framework, such as nucleon correlations forming on the nuclear surface, including the $\alpha$ -cluster [29, 30].

On the other hand, we obtain several crucial densities from KSN single-particle wave functions $\varphi _ { i }$ and occupancy weights $w _ { i }$ calibrated by experimental charge radii, which are nuclear spatial density

$$
\rho = \sum_ {i} \frac {d _ {i} (\sqrt {w _ {i}} \varphi_ {i}) ^ {2}}{4 \pi}, \qquad (3)
$$

kinetic density

$$
\tau = \sum_ {i} \frac {d _ {i}}{4 \pi} \left[ (\partial_ {r} \sqrt {w _ {i}} \varphi_ {i}) ^ {2} + \frac {l _ {i} (l _ {i} + 1)}{r ^ {2}} (\sqrt {w _ {i}} \varphi_ {i}) ^ {2} \right], \quad (4)
$$

and spin-orbit density

$$
J = \sum_ {i} \frac {d _ {i}}{4 \pi} \left[ j _ {i} \left(j _ {i} + 1\right) - l _ {i} \left(l _ {i} + 1\right) - \frac {3}{4} \right] \frac {2}{r} \left(\sqrt {w _ {i}} \varphi_ {i}\right) ^ {2}. \tag {5}
$$

Here $i \in \{ 1 s _ { 1 / 2 } , 1 p _ { 3 / 2 } , 1 p _ { 1 / 2 } , . . . \}$ indicates the singleparticle states, while $d _ { i }$ , $l _ { i }$ , and $j _ { i }$ respectively represent the degeneracy, the orbital angular momentum quantum number, and the total angular momentum quantum number at a state $i$ . In density functional theory (DFT), the three aforementioned densities determine the kinetic, potential, and spin-orbit terms of nuclear interactions, thereby determining the nuclear binding energy via the Kohn-Sham equations. In particular, when employing charge radii to calibrate densities [28], 640 nuclei data with $Z > 4 0$ were utilized, encompassing the majority of deformed nuclei. In this sense, all densities should be considered as angularly averaged. This implies that deformation-induced changes in binding energy should be also characterized by the features $X _ { 1 }$ and $X _ { 2 }$ .

The mapping network from the above inputs to the nuclear binding energy is referred to as a density-to-energy network (DTEN), the structure of which is shown in Fig. 1. The $X _ { 1 }$ and $X _ { 2 }$ are input into two separate 4-layer fully connected (FC) neural network cells ( $C _ { 1 }$ and $C _ { 2 }$ ), while the six densities ( $\rho _ { n }$ , $\tau _ { n }$ , $J _ { n }$ , ρp, $^ { \prime } p$ , $J _ { p }$ ) as continuous variables are fed into a 5-layer convolutional (Conv)

![](images/888d49d5dc78bdca2c86c3e16d3c2b7e92786c40fb8481963895165cf1733265.jpg)  
FIG. 1. Schematic diagram of the structure of density-toenergy network (DTEN). See the text for the abbreviation.

neural network cell with six channels ( $C _ { 3 }$ ). Specifically, a max-pooling layer is connected after each convolutional layer to reduce the parameter and expedite convergence. Subsequently, the outputs from these branch cells are concatenated and uniformly batch-normalized (BN) to align the feature distributions with a normal distribution. Afterward, passing through another FC cell ( $C _ { 4 }$ ), the features are finally mapped to the binding energy $E _ { b }$ . An essential point that must be emphasized is that the network consists of 23 layers with intricate connections, whose complexity can lead to some neurons being trapped in the negative range and becoming deactivated under the commonly used ReLU $( = \operatorname* { m a x } \{ 0 , x \} )$ [31] activation function for nonlinearity, especially after multiple iterations. To address this issue and improve convergence, we adopt the LReLU ( $= \operatorname* { m a x } \{ 0 . 0 1 x , x \} )$ activation function [32] to avoid gradient vanishing. Furthermore, to mitigate the influence of absolute data magnitudes, all input features are subject to min-max scaling, ensuring they fall within the range of 0 to 1. Due to the constrained range of values, we employed the Sigmoid $\displaystyle \left( = 1 / ( 1 + e ^ { - x } ) \right)$ ) activation function in the final layer. The meticulously designed hyperparameter set for the DTEN architecture is listed in Table I. In the table, the initial row and the concluding row of each cell respectively signify its input and output, with the symbol “ $\uplus$ ” meaning concatenating two vectors, i.e., $( a , b , . . . ) \uplus ( c , d , . . . ) = ( a , b , . . . , c , d , . . . )$ . During the training process, a dynamically decreasing learning rate, which reduces as the loss function converges, is applied

TABLE I. The hyperparameter set of DTEN structure. The “ $D$ ” represents the output dimension of the layer, “ $C _ { \mathrm { i n } }$ ” denotes the input channels, “ $C _ { \mathrm { o u t } }$ ” signifies the output channels, “ $K _ { s }$ ” refers to the size of the kernel which includes both convolutional and pooling dimensions, “St” indicates the stride used during convolution or pooling operations, and “ $g ( x )$ ” represents the non-linear activation function.   

<table><tr><td colspan="8">C1or C2</td></tr><tr><td>L</td><td>Type</td><td></td><td></td><td></td><td></td><td>D</td><td>g(x)</td></tr><tr><td>-</td><td>X1or X2</td><td></td><td></td><td></td><td></td><td>6</td><td>-</td></tr><tr><td>1</td><td>FC</td><td></td><td></td><td></td><td></td><td>32</td><td>LReLU</td></tr><tr><td>2</td><td>FC</td><td></td><td></td><td></td><td></td><td>64</td><td>LReLU</td></tr><tr><td>3</td><td>FC</td><td></td><td></td><td></td><td></td><td>128</td><td>LReLU</td></tr><tr><td>4</td><td>FC</td><td></td><td></td><td></td><td></td><td>256</td><td>LReLU</td></tr><tr><td>-</td><td>Output1or Output2</td><td></td><td></td><td></td><td></td><td>256</td><td>-</td></tr><tr><td colspan="8">C3</td></tr><tr><td>L</td><td>Type</td><td>D</td><td>Cin.</td><td>Cout.</td><td>Ks</td><td>St</td><td>g(x)</td></tr><tr><td>-</td><td>Densities</td><td>(6,150)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1</td><td>Conv.</td><td>(32,150)</td><td>6</td><td>32</td><td>3</td><td>1</td><td>LReLU</td></tr><tr><td>2</td><td>pooling</td><td>(32,75)</td><td>32</td><td>32</td><td>2</td><td>2</td><td>-</td></tr><tr><td>3</td><td>Conv.</td><td>(64,75)</td><td>32</td><td>64</td><td>3</td><td>1</td><td>LReLU</td></tr><tr><td>4</td><td>pooling</td><td>(64,25)</td><td>64</td><td>64</td><td>3</td><td>3</td><td>-</td></tr><tr><td>5</td><td>Conv.</td><td>(128,25)</td><td>64</td><td>128</td><td>3</td><td>1</td><td>LReLU</td></tr><tr><td>6</td><td>pooling</td><td>(128,8)</td><td>128</td><td>128</td><td>3</td><td>3</td><td>-</td></tr><tr><td>7</td><td>Conv.</td><td>(256,8)</td><td>128</td><td>256</td><td>3</td><td>1</td><td>LReLU</td></tr><tr><td>8</td><td>pooling</td><td>(256,2)</td><td>256</td><td>256</td><td>4</td><td>4</td><td>-</td></tr><tr><td>9</td><td>Conv.</td><td>(512,1)</td><td>256</td><td>512</td><td>2</td><td>1</td><td>LReLU</td></tr><tr><td>-</td><td>Output3</td><td>512</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="8">C4</td></tr><tr><td>L</td><td>Type</td><td></td><td></td><td></td><td></td><td>D</td><td>g(x)</td></tr><tr><td>-</td><td>Output1 ⊕ Output2 ⊕ Output3</td><td></td><td></td><td></td><td></td><td>1024</td><td>-</td></tr><tr><td>1</td><td>BN</td><td></td><td></td><td></td><td></td><td>1024</td><td>-</td></tr><tr><td>2</td><td>FC</td><td></td><td></td><td></td><td></td><td>512</td><td>LReLU</td></tr><tr><td>3</td><td>FC</td><td></td><td></td><td></td><td></td><td>256</td><td>LReLU</td></tr><tr><td>4</td><td>FC</td><td></td><td></td><td></td><td></td><td>128</td><td>LReLU</td></tr><tr><td>5</td><td>FC</td><td></td><td></td><td></td><td></td><td>32</td><td>LReLU</td></tr><tr><td>6</td><td>FC</td><td></td><td></td><td></td><td></td><td>1</td><td>Sigmoid</td></tr><tr><td>-</td><td>Binding Energy</td><td></td><td></td><td></td><td></td><td>1</td><td>-</td></tr></table>

with the Adaptive Momentum Estimation (Adam) [33] optimizer. The aforementioned definitions and concepts are entirely consistent with the patterns used in PyTorch [34].

In the current design, non-model-dependent inputs ( $X _ { 1 }$ and $X _ { 2 }$ ) and model-dependent inputs (Densities) are blended. The advantage is to retain accuracy as much as possible while exploring the impact of densities on binding energy. In this manner, the search for a parameterized energy density functional is replaced, but the insights from traditional functionals are not aborted, which will produce profound significance for describing complex nuclear systems.

![](images/0651462c4e8fc680efcb02dcc2cc2703d7f88977b362b0bee93a206e15e1bba2.jpg)  
FIG. 2. The proton ${ \sqrt { w _ { i } } } \varphi _ { i } ( r )$ in coordinate space for each single-particle orbital for the nucleus $^ { 1 3 6 }$ Xe with (a) SHF+BCS and (b) calibrated KSN, and the comparisons for the corresponding (c) spatial densities, (d) kinetic densities, and (e) spin-orbit densities.

# III. RESULTS AND ANALYSIS

In this study, the proton single-particle wave functions generated by KSN have undergone calibrations with the experimental charge radii of over 600 nuclei. However, due to the lack of neutron information from laboratories, the original SHF $^ +$ BCS neutron densities with SkM $^ *$ interaction [35] is still employed. To ensure that the variation in density is within physically permissible limits, we need to examine the calibrated proton densities.

The comparisons in Fig. 2 depict $\sqrt { w _ { i } } \varphi _ { i } ( r )$ in coordinate space for each single-particle orbital, spatial densities, kinetic densities, and spin-orbit densities between SHF+BCS and calibrated KSN. It is evident that there are only minimal changes for the various densities. This is understandable: during the calibration process of KSN [28], the original ${ \sqrt { w _ { i } } } \varphi _ { i } ( r )$ from SHF $^ +$ BCS still retains a certain weight, and the calibration for charge radii often only minor changes on the typical order of a few $1 0 ^ { - 2 }$ fm. This implies that the loss of self-consistency in the Kohn-Sham equation is maintained at a minimal level, hence it is feasible to roughly explore changes in the kinetic, potential, and spin-orbit terms of nuclear interactions on the basis of the SkM $^ *$ parameters. However, delving into the intricate details of binding energy along such an approach directly is not practical. As illustrated in Ref. [36], a neural network trained with density and binding energy data from Skyrme DFT was applied to discuss Ca isotopes, encountering a failure in describ-

![](images/57b775fc3ee5b9891bf01ab08985b3539ac33be09847d42a7b391432e304c561.jpg)  
FIG. 3. Panel (a): Loss values on the training set and validation set as a function of training epochs, where the rootmean-square binding energy error, weighted multiple models, is shown in the inner panel. Panel (b): The mass errors $\Delta m$ as a function of mass number $A$ . Panel (c): The count of mass errors in different intervals.

ing $^ { 4 8 }$ Ca with an overbinding phenomenon. Such failure can be attributed to an indispensable beyond-mean-field effect appearing near $^ { 4 8 }$ Ca [37, 38]. To capture the descriptive capacity of the beyond-mean-field effect, it is a natural approach to establish a mapping relation that targets experimental data.

Turn to the training processes of DTEN, of which the changes in the loss value across training epochs are depicted in Fig. 3(a). In approximately 2400 nuclei with proton numbers greater than 40, for which binding energies have been measured with high precision, we utilized an 8:2 ratio for dividing the data into training and validation sets. After each epoch, all nuclei in the training set have undergone training, then the decision to retain the model depends on whether there is a reduction in the observed loss value on the validation set. Here, a weighted mean squared error is selected as the loss function,

$$
\operatorname {L o s s} = \left\langle \left(E _ {b, \text {p r e}} - E _ {b, \text {t a r}}\right) ^ {2} \times A \right\rangle , \tag {6}
$$

where $E _ { b , \mathrm { p r e } }$ and $\mathit { E } _ { b , \mathrm { t a r } }$ represent the predicted and experimental values of the binding energy, respectively, while weight $A$ corresponds to the mass number, reflecting the higher demand for prediction accuracy in average binding energy as the mass increases. It can be observed

that the training set and validation set have essentially converged after 150 epochs, with only minor differences between them. This indicates no overfitting occurs, emphasizing the generalization capability. It is crucial to highlight that, in a neural network, the number of parameters typically influences training efficiency, whereas the network predictive capability is determined by the loss value and the presence of overfitting.

Although the training seems successful, upon further examination of the results, we note that the description for nuclear masses is disappointingly reflected in a root mean squared (RMS) error reaching 1.6 MeV. To address this issue, we employ ensemble learning, combining multiple DTENs with identical structures for a final prediction. The differences amongst these DTENs are solely caused by the random initialization parameters. The superiority or inferiority of the network can be described by the RMS error $\sigma$ , serving as a prior according to the Bayesian principle. Therefore, the final prediction can be expressed as

$$
E _ {b, \text {f i n a l}} = \sum_ {i} ^ {M} w _ {i} \times E _ {b, \text {p r e}, i} \tag {7}
$$

with

$$
w _ {i} = \frac {1 / \sigma_ {i} ^ {2}}{\sum_ {i} ^ {M} 1 / \sigma_ {i} ^ {2}}, \tag {8}
$$

where $M$ is the total number of models in the ensemble. The inner panel of Fig. 3(a) depicts the variation of the final $\sigma$ with respect to $M$ . It is clear that with the increase in the number of models, the RMS error is substantially reduced, ultimately converging to 0.455 MeV. This precision, compared to the adopted SHF+BCS theory [39] with the RMS error being about 10 MeV/ $c ^ { 2 }$ , has been improved by order of magnitude.

As a final result, the errors of nuclear mass $\Delta m$ are demonstrated in Fig. 3(b), for which the mass number $A$ serves as the horizontal axis. The $\Delta m$ for the majority of nuclei are within 0.5 MeV/ $c ^ { 2 }$ , while there is still a small fraction of nuclei with errors ranging from 0.5 to 2 MeV/ $c ^ { 2 }$ . Within this distribution, it is difficult to discern whether there is a clear correlation between the $\Delta m$ and any physical quantities. Further projecting the errors into the counting space, as shown in (c), a standard normal distribution can be observed. This strongly suggests that the model exhibits robustness and delivers reliable predictions.

Based on the strong correlation between densities and binding energies, inferring the nuclear neutron skin thickness is an interesting and crucial problem. The proton densities generated by KSN have been calibrated against the charge radii, and we believe they reflect the true information about protons. Thus, by observing the correlation between neutron density variations and the binding states of a nucleus, we can further infer the neutron skin thickness. To this end, $^ \mathrm { 2 0 8 }$ Pb, as a prominent spher-

![](images/5f0af1cf65dddaf5d725fe0805a82e2a016f2700999be204f23c5b3e38ebdc7a.jpg)  
FIG. 4. The binding energy of $^ { 2 0 8 }$ Pb as a function of neutron skin thickness. The blue dashed line represents the calculated values on the training set, while the shadow indicates the experimental value [40].

ical nucleus, is taken for examination. Physically, the variation in spatial density will also lead to changes in kinetic density and spin-orbit density. To maintain selfconsistency, based on the Kohn-Sham auxiliary singleparticle system, we apply a compression operator to the neutron single-particle wave function, i.e.,

$$
\varphi (r) \rightarrow C _ {k} \varphi (k r), \tag {9}
$$

where the parameter $k$ controls the compression ratio, while $C _ { k }$ maintains the normalization.

With the variation of $k$ , corresponding changes occur in the neutron skin and binding energy, as shown in Fig. 4. At a neutron skin thickness of 0.223 fm, the nuclear binding strength is maximized. The obtained value is greater than the initial training value (blue dashed line) and coincidentally falls on the edge of the experimental measurement range [40]. Another noteworthy point is that near the minimum point, the energy changes relatively softly, less than 100 keV, suggesting that there are significant fluctuations in the neutron skin thickness. This result is crucial for both astrophysics and nuclear reactions through the equation of state. We look forward to further experimental validation in the future.

The current research, in conjunction with Ref. [28], has essentially completed the construction of neural networks based on the Kohn-Sham scheme for enhancing DFT. Regarding observables, it achieves high accuracy in describing binding energies, nuclear radii, and neutron skin thickness. In terms of physical details, it can also be employed to explore the contributions of singleparticle states and shell structure, as well as the impact of various densities on binding energy.

Nevertheless, the current model still deserves further refinement and optimization. Primarily, when considering non-magic number nuclei, the valence-nucleoninduced deformation effects do not directly manifest in the densities. The current densities are assumed to be

angularly averaged, which may impact the accuracy of describing binding energies and further compromise the capability to characterize multipole deformation potential surfaces. Therefore, three-dimensionalizing the current model is imperative. Secondly, the current loss function may not adequately capture the differences among nuclei, especially certain beyond-mean-field effects, hindering further improving precision. Introducing an adversarial neural network that autonomously assesses the credibility of predictions, as opposed to a conventional RMS error, could be a more rational enhancement. Additionally, this may eliminate subtle non-physical zig-zag patterns technologically.

# IV. SUMMARY

With the aid of the nuclear single-particle wave functions generated by the experimental charge radiuscalibrated Kohn-Sham network, we computed three essential densities in DFT, i.e., spatial density, kinetic density, and spin-orbital density. Through an elaborated neural network, the densities are further mapped to the experimental binding energies. By employing a weighted ensemble of multiple models, the RMS error in describing binding energies reached about 450 keV. There has been a noticeable improvement compared to the initial calculations based on SHF $^ +$ BCS. Meanwhile, the distribution of errors conforms to a standard normal distribution, reflecting the robustness of the model.

In this research, charge-radius-based calibration does not influence neutron densities. Therefore, it is feasible to further explore the relation between binding energy and neutron skin thickness. Considering the self-consistency among densities, a contraction operator is applied to the neutron single-particle wave functions to establish the correlation between neutron skin and binding energy. By searching for the minimum point, the estimated neutron skin thickness is obtained equaling approximately 0.223 fm.

This study aggregates the charge radius data over 600 nuclei, binding energy data for more than 2400 nuclei, and single-particle state data based on DFT. Ultimately, it bypasses the many-body interaction potential and establishes the correlations among observables, whose descriptive performance for the nuclear ground state has surpassed that of the majority of existing density functional models. In the future, by three-dimensionalizing the model, incorporating adversarial neural networks, as well as introducing more experimental data, the neural network for enhancing DFT will possess stronger descriptive capabilities.

# V. ACKNOWLEDGEMENTS

This work is supported by the National Natural Science Foundation of China under Grants No. 12005175,

12375126 the Fundamental Research Funds for the Central Universities under Grant No. SWU119076, the JSPS Grant-in-Aid for Early-Career Scientists under Grant No. 18K13549, the JSPS Grant-in-Aid for Scientific Re-

search (S) under Grant No. 20H05648. This work is also partially supported by the RIKEN Pioneering Project: Evolution of Matter in the Universe.

[1] D. Lunney, J. M. Pearson, and C. Thibault, Rev. Mod. Phys. 75, 1021 (2003).   
[2] M. Bender, P.-H. Heenen, and P.-G. Reinhard, Rev. Mod. Phys. 75, 121 (2003).   
[3] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C 93, 014311 (2016).   
[4] E. M. Burbidge, G. R. Burbidge, W. A. Fowler, and F. Hoyle, Rev. Mod. Phys. 29, 547 (1957).   
[5] H. A. Bethe and R. F. Bacher, Rev. Mod. Phys. 8, 82 (1936).   
[6] P. M¨oller, W. D. Myers, H. Sagawa, and S. Yoshida, Phys. Rev. Lett. 108, 052501 (2012).   
[7] N. Wang, M. Liu, X. Wu, and J. Meng, Phys. Lett. B 734, 215 (2014).   
[8] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. Lett. 102, 152503 (2009).   
[9] S. Goriely, S. Hilaire, M. Girod, and S. P´eru, Phys. Rev. Lett. 102, 242501 (2009).   
[10] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 93, 034337 (2016).   
[11] J. Meng, J. Peng, S. Q. Zhang, and S.-G. Zhou, Phys. Rev. C 73, 037303 (2006).   
[12] H. Liang, N. V. Giai, and J. Meng, Phys. Rev. Lett. 101, 122502 (2008).   
[13] Z. Niu and H. Liang, Phys. Lett. B 778, 48 (2018).   
[14] Z. M. Niu and H. Z. Liang, Phys. Rev. C 106, l021303 (2022).   
[15] Z. M. Niu, Z. L. Zhu, Y. F. Niu, B. H. Sun, T. H. Heng, and J. Y. Guo, Phys. Rev. C 88, 024325 (2013).   
[16] Z. M. Niu, J. Y. Fang, and Y. F. Niu, Phys. Rev. C 100, 054311 (2019).   
[17] X. H. Wu and P. W. Zhao, Phys. Rev. C 101, 051301 (2020).   
[18] X. Wu, L. Guo, and P. Zhao, Phys. Lett. B 819, 136387 (2021).   
[19] J. W. CLARK and H. LI, Int. J. Mod. Phys. B 20, 5015 (2006).   
[20] A. Pastore, D. Neill, H. Powell, K. Medler, and C. Barton, Phys. Rev. C 101, 035804 (2020).   
[21] M. Shelley and A. Pastore, Universe 7, 131 (2021).   
[22] L. Neufcourt, Y. Cao, W. Nazarewicz, E. Olsen, and F. Viens, Phys. Rev. Lett. 122, 062502 (2019).   
[23] L. Neufcourt, Y. Cao, S. A. Giuliani, W. Nazarewicz, E. Olsen, and O. B. Tarasov, Phys. Rev. C 101, 044307 (2020).   
[24] L. Neufcourt, Y. Cao, S. Giuliani, W. Nazarewicz, E. Olsen, and O. B. Tarasov, Phys. Rev. C 101, 014319

(2020).   
[25] M. Carnini and A. Pastore, J. Phys. G: Nucl. Part. Phys. 47, 082001 (2020).   
[26] Z.-P. Gao, Y.-J. Wang, H.-L. L¨u, Q.-F. Li, C.-W. Shen, and L. Liu, Nucl. Sci. Tech. 32 (2021), 10.1007/s41365- 021-00958-z.   
[27] A. Hamaker, E. Leistenschneider, R. Jain, G. Bollen, S. A. Giuliani, K. Lund, W. Nazarewicz, L. Neufcourt, C. R. Nicoloff, D. Puentes, R. Ringle, C. S. Sumithrarachchi, and I. T. Yandow, Nat. Phys. 17, 1408 (2021).   
[28] Z.-X. Yang, X.-H. Fan, Z.-P. Li, and H. Liang, Phys. Lett. B 840, 137870 (2023).   
[29] J. Tanaka, Z. Yang, S. Typel, S. Adachi, S. Bai, P. van Beek, D. Beaumel, Y. Fujikawa, J. Han, S. Heil, S. Huang, A. Inoue, Y. Jiang, M. Kn¨osel, N. Kobayashi, Y. Kubota, W. Liu, J. Lou, Y. Maeda, Y. Matsuda, K. Miki, S. Nakamura, K. Ogata, V. Panin, H. Scheit, F. Schindler, P. Schrock, D. Symochko, A. Tamii, T. Uesaka, V. Wagner, K. Yoshida, J. Zenihiro, and T. Aumann, Science 371, 260 (2021).   
[30] S. Typel, Phys. Rev. C 89, 064321 (2014).   
[31] M. J. Villani and N. Schoots, “Any deep relu network is shallow,” (2023).   
[32] B. Xu, N. Wang, T. Chen, and M. Li, (2015), arXiv:1505.00853 [cs.LG].   
[33] D. P. Kingma and J. Ba, in 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings, edited by Y. Bengio and Y. LeCun (2015).   
[34] “PyTorch Documentation,” https://pytorch.org/ docs/stable/index.html (Accessed on 2023-08-03).   
[35] J. Bartel, P. Quentin, M. Brack, C. Guet, and H.-B. H˚akansson, Nucl. Phys. A 386, 79 (1982).   
[36] Z.-X. Yang, X.-H. Fan, T. Naito, Z.-M. Niu, Z.-P. Li, and H. Liang, “Calibration of nuclear charge density distribution by back-propagation neural networks,” (2022).   
[37] U. C. Perera, A. V. Afanasjev, and P. Ring, Phys. Rev. C 104, 064313 (2021).   
[38] T. Naito, T. Oishi, H. Sagawa, and Z. Wang, Phys. Rev. C 107, 054307 (2023).   
[39] P.-G. Reinhard, in Computational Nuclear Physics 1 (Springer Berlin Heidelberg, 1991) pp. 28–50.   
[40] D. Adhikari, H. Albataineh, D. Androic, K. Aniol, D. Armstrong, et al., Phys. Rev. Lett. 126, 172502 (2021).