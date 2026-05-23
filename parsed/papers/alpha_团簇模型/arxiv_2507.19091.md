# Bayesian optimization and nonlocal effects method for α decay of superheavy nuclei based on CPPM

Xuanpeng Xiao1, Panpan $\mathrm { Q i ^ { 1 } }$ , Gongming $\mathrm { Y u ^ { * 1 } }$ , Haitao Yang†2, and Qiang $\mathrm { H u } ^ { \ddag 3 }$

1College of Physics and Technology, Kunming University, Kunming 650214, China

2College of Science, Zhaotong University, Zhaotong 657000, China

3Institute of Modern Physics, Chinese Academy of Sciences, Lanzhou 730000, China

# Abstract

We combine nonlocal effects with Bayesian Neural Network (BNN) methods to enhance the prediction accuracy of $\alpha$ decay half-lives. The results indicate that accounting for nonlocal effects significantly impacts the half-life calculations, while the BNN method markedly improves prediction accuracy and demonstrates strong extrapolation capabilities. Furthermore, we discuss the impact of nuclear deformation (the quadrupole deformation factor $\beta _ { 2 }$ ) on machine learning predictions. Through Shapley Additive Explanations (SHAP), we conducted a quantitative comparison of six input features within the BNN, revealing that the $\alpha$ decay energy $Q _ { \alpha }$ is the primary driving factor affecting the half-life $T _ { 1 / 2 }$ . Leveraging the remarkable extrapolation ability of the BNN, we successfully predicted the $\alpha$ decay half-lives of the isotope chain ( $Z = 1 1 8 , 1 2 0 ,$ ), uncovering a significant shell effect at neutron number $N = 1 8 4$ . For the isotopic chains $\begin{array} { r } { Z = 1 1 8 , 1 2 0 } \end{array}$ ), the predicted $\alpha$ decay half-lives and $Q _ { \alpha }$ values satisfy the Geiger-Nuttall (G-N) linear relationship. This result further confirms the predictive reliability of the proposed model.

Keywords: $\alpha$ decay, half-lives, nonlocal effects, Bayesian Neural Network, Coulomb and proximity potential model.

# I. INTRODUCTION

The synthesis and properties of superheavy nuclei represent a frontier in contemporary nuclear physics, playing a crucial role in exploring the limits of the nuclear chart and understanding fundamental nuclear forces. $\alpha$ decay is one of the primary decay modes of superheavy nuclei, accurate prediction of $\alpha$ decay half-lives is essential for identification and synthesis of new elements. α decay is fundamentally a quantum tunneling phenomenon, independently proposed by Gamow [1] and Gurney and Condon [2] [3] in 1928.

A variety of theoretical models have been developed to calculate the $\alpha$ decay half-lives of superheavy nuclei, including the Generalized Liquid Drop Model (GLDM) [4] [5] the Effective Liquid Drop Model (ELDM) [6], the Modified Generalized Liquid Drop Model (MGLDM) [7] [8] [9], the Coulomb and Proximity Potential Model (CPPM) [10], and the Preformed Cluster

Model (PCM) [11]. Additionally, empirical formulas based on fitting experimental data have been extensively developed. For example, the Universal Decay Law (UDL: Formula-A) proposed by Qi [12], as well as the Modified Universal Decay Law that accounts for angular momentum effects (Formula-B) and isospin effects (Formula-C) [13]. While these models provide essential theoretical foundations for understanding $\alpha$ decay mechanisms, significant discrepancies persist between theoretical predictions and experimental data, particularly in the superheavy region.

To improve prediction accuracy, researchers have focused on nonlocal effects in particle-nucleus interactions. The concept of nonlocal potentials was introduced by Feshbach [14] and Frahn et al. [15] in the late 1950s. Recent studies have further confirmed the importance of nonlocal effects: in 2022, Medeiros et al. [16] conducted a systematic study of the $\alpha$ decay half-lives of $\alpha$ particles with effective mass for $5 2 \leq Z \leq 1 0 3$ ; Hu et al. [17] systematically investigated nonlocal effects in $\alpha$ decay half-lives for even-even nuclei within a two potential approach. These studies consistently demonstrate that incorporating nonlocal effects significantly improves theoretical predictions, offering a new avenue for reducing systematic deviations between theory and experiment.

Traditional theoretical models face challenges in handling complex many-body interactions and nonlinear effects. Recent advances in machine learning have provided new tools for nuclear physics research. Machine learning exhibits unique advantages in treating high-dimensional, strongly correlated complex systems [18]. Various machine learning methods have been successfully applied in nuclear physics, including Gaussian processes(GP) [19] [20] naive Bayes classifiers(NBC) [21] [22] deep learning(DL) [23] [24] restricted Boltzmann machines(RBM) [25] [26] radial basis function(RBF) [27] [28] networks, Bayesian Neural Networks(BNN) [29] [30], and light gradient boosting machines(LightGBM) [31]. Among these, BNN have attracted particular attention due to their advantages in uncertainty quantification and overfitting prevention. By incorporating the prior distribution of parameters, and Bayesian inference, BNN not only provides accurate predictions but also quantifies prediction uncertainties [18]. This capability has enabled BNN applications across multiple nuclear physics domains [32] [33], including predictions of atomic radii [34] [35], nuclear masses [36], and $\beta$ decay half-lives [37].

In this study, we systematically investigate the theoretical calculation and model optimization of $\alpha$ decay half-lives for superheavy nuclei. Initially, we calculated the $\alpha$ decay half-lives of 401 superheavy nuclides based on the CPPM framework. In the conventional CPPM, the $\alpha$ cluster preformation factor $P _ { \alpha }$ is typically treated as a constant empirical value for specific types of parent nuclei. This simplified treatment stems from the smooth variation of $P _ { \alpha }$ in open-shell regions [38]; however, this assumption may be insufficient for accurately reproducing half-lives near shell closures. The preformation factor is a highly complex physical quantity that reflects the interplay of nuclear many-body correlations, shell effects, and cluster formation dynamics. Particularly near closed shells (such as $Z ~ = ~ 8 2$ and $N = 1 2 6$ ), $P _ { \alpha }$ exhibits significant variations [39] [40]. Recently, researchers have proposed a cluster formation model (CFM) based on $\alpha$ -cluster formation energy [40] [41] [42], which extracts the $\alpha$ preformation factor by analyzing the binding energy differences of participating nuclides. This approach shows excellent agreement with various microscopic theoretical calculations. Therefore, we employ the CFM to systematically analyze separation energies and extract $P _ { \alpha }$ .

To account for nonlocal dynamical effects, we introduce a coordinate-dependent $\alpha$ -particle effective mass and recalculate the half-lives. The results demonstrate that the inclusion of nonlocal effects significantly impacts the predicted $\alpha$ decay half-lives,

consistent with previous studies [16] [17]. Subsequently, we construct a BNN model using mass number $A$ , proton number $Z$ , decay energy $Q _ { \alpha }$ , orbital angular momentum $l$ , and preformation factor $P _ { \alpha }$ as input parameters to optimize the CPPM, the nonlocally modified CPPM and three distinct parameterizations of the universal decay law (UDL: Formula-A, Formula-B, Formula-C). Given that prior research has shown that nuclear deformation can significantly alter the barrier shape and thereby affect the tunneling probability in $\alpha$ decay [43], [44], we further incorporate the quadrupole deformation parameter $\beta _ { 2 }$ in the BNN to improve prediction accuracy. By comparing the root-mean-square errors (RMSE) before and after optimization, we find that the BNN reduces the RMSE of all models by more than $2 3 . 2 5 \%$ , with the CPPM achieving an improvement of $3 6 . 2 8 \%$ . Using Shapley Additive Explanations (SHAP) for feature importance analysis, the results reveal that the decay energy $Q _ { \alpha }$ plays a dominant role among the six input parameters.

Finally, we predict the $\alpha$ decay half-lives for isotope chains of $Z = 1 1 8$ and $Z = 1 2 0$ . The predictions show that the logarithm of $\alpha$ half-life $( \log _ { 1 0 } T )$ exhibits the expected linear Geiger-Nuttall–type correlation with the decay energy $Q _ { \alpha }$ . This correlation is consistent with the relationship between $\log _ { 1 0 } T$ and the negative logarithm of penetration probability $( - \ln \mathsf { P } )$ . This demonstrates that our method not only reduces the RMSE but also preserves the fidelity of fundamental physical laws, providing compelling evidence that the approach captures the underlying physics.

This paper is organized as follows: Section 2 introduces $\alpha$ decay theoretical models and BNN methodology; Section 3 presents results and analysis; Section 4 is a summary.

# II. GENERAL FORMALISM

# A. Coulomb and proximity potential model framework

The partial half-life is related to the decay constant $\lambda$ by [45]

$$
T _ {1 / 2} = \frac {\ln 2}{\lambda} = \frac {\ln 2}{\nu P _ {\alpha} P}, \tag {1}
$$

where $\lambda$ is the decay constant, $\nu = 1 . 0 \times 1 0 ^ { 2 2 } s ^ { - 1 }$ is the frequency of the assault on the barrier [46] [47] [48]. $P _ { \alpha }$ refers to the preformation factor, which will be discussed in the following section.

The barrier penetration probability $P$ can be calculated within the semi-classical Wentzel-Kramers-Brillouin(WKB) approximation.

$$
P = \exp \left(- \frac {2}{\hbar} \int_ {R _ {i n}} ^ {R _ {o u t}} \sqrt {2 \mu | V _ {r} - Q _ {c} |} \mathrm {d} r\right), \tag {2}
$$

where the reduced mass is $\begin{array} { r } { \mu = \frac { m M } { m + M } } \end{array}$ . Here, with $M$ and $m$ being the daughter nucleus and the emitted cluster mass, respectively. $Q _ { c }$ represents the released energy [49], which can be expressed as

$$
Q _ {c} = B \left(A _ {c}, Z _ {c}\right) + B \left(A _ {d}, Z _ {d}\right) - B (A, Z), \tag {3}
$$

where $B ( A _ { c } , Z _ { c } )$ , $B ( A _ { d } , Z _ { d } )$ and $B ( A , Z )$ are the binding energies of the emitted cluster, daughter nucleus, and parent nucleus, respectively [20]. $Z _ { c }$ , $Z _ { d }$ and $Z$ are the proton numbers of the emitted cluster, daughter nucleus, and parent nucleus, respectively.

The classical turning points $R _ { i n } = A _ { c } ^ { 1 / 3 } + A _ { d } ^ { 1 / 3 }$ and $\begin{array} { r } { R _ { o u t } = ( \sqrt { ( \frac { Z _ { c } Z _ { d } e ^ { 2 } } { 2 Q _ { c } } ) ^ { 2 } + \frac { \hbar ^ { 2 } ( l + 1 / 2 ) ^ { 2 } } { 2 \mu Q _ { c } } } + \frac { Z _ { c } Z _ { d } e ^ { 2 } } { 2 Q _ { c } } ) } \end{array}$ ( ZcZde2 )2 + [50]. Here, Ac, Ad, and $A$ are the mass numbers of the emitted cluster, the daughter nucleus, and the parent nucleus, respectively.

The total interaction potential $V ( r )$ between the emitted cluster and the daughter nucleus consists of the nuclear potential $V _ { N } ( r )$ , Coulomb potential $V _ { C } ( r )$ , and centrifugal potential $V _ { l } ( r )$ . It can be expressed as

$$
V (r) = V _ {N} (r) + V _ {C} (r) + V _ {\ell} (r), \tag {4}
$$

In the present work, we adopt the proximity potential formalism in place of the nuclear potential. In the 1970s, Blocki et al. [51] proposed the original form of the proximity potential formalism for two interacting spherical nuclei, which is expressed as

$$
V _ {N} (r) = 4 \pi \gamma b \bar {R} \Phi (\xi), \tag {5}
$$

where $b \approx 1 \mathrm { f m }$ . Surface energy coefficient $\gamma$ has the following form [52]:

$$
\gamma = \gamma_ {0} \left(1 - k _ {s} I ^ {2}\right), \tag {6}
$$

where $\begin{array} { r } { I = \frac { N _ { p } - Z _ { p } } { A _ { p } } } \end{array}$ is the asymmetry parameter quantifying the neutron–proton excess of the parent nucleus; Here, $\gamma _ { 0 }$ and $k _ { s }$ denote the surface-energy coefficient and the surface-asymmetry coefficient, respectively. In the present work we use $\gamma _ { 0 } { = } 0 . 9 5 1 7 \mathrm { M e V / f m ^ { 2 } }$ and $k _ { s } = 1 . 7 8 2 6$ [52].

$\bar { R }$ denotes the mean curvature radius (or reduced radius). It can be obtained from

$$
\bar {R} = \frac {C _ {c} C _ {d}}{C _ {c} + C _ {d}}, \tag {7}
$$

where $\begin{array} { r } { C _ { i } = R _ { i } [ 1 - ( \frac { b } { R _ { i } } ) ^ { 2 } ] ( i = c , d ) } \end{array}$ denotes the matter radius. The effective sharp radius $R _ { i }$ is defined as $R _ { i } = 1 . 2 8 A _ { i } ^ { 1 / 3 } -$ $0 . 7 6 + 0 . 8 A _ { i } ^ { - 1 / 3 } ( i = c , d ) .$ .

The general functional form is given by

$$
\Phi (\xi) = \left\{ \begin{array}{l l} \frac {- 1}{2} (\xi - 2. 5 4) ^ {2} - 0. 0 8 5 2 (\xi - 2. 5 4) ^ {3}, & \xi <   1. 2 5 1 1, \\ - 3. 4 3 7 \exp \left(- \frac {\xi}{0 . 7 5}\right), & \xi \geq 1. 2 5 1 1, \end{array} \right. \tag {8}
$$

where $\begin{array} { r } { \xi = \frac { r - C _ { c } - C _ { d } } { b } } \end{array}$ is the distance between the near surface of the emitted cluster and daughter nucleus.

Here, the potential of a uniformly charged sphere of radius $R$ is treated as the Coulomb potential, which is given by

$$
V _ {C} = \left\{ \begin{array}{l l} \frac {Z _ {c} Z _ {d} e ^ {2}}{2 R} \left[ 3 - \left(\frac {r}{R}\right) ^ {2} \right], & r \leq R, \\ \frac {Z _ {c} Z _ {d} e ^ {2}}{r}, & r \geq R, \end{array} \right. \tag {9}
$$

where $e ^ { 2 } = 1 . 4 3 { \mathrm { ~ M e V } } .$ fm represents the Coulomb interaction constant, and $R$ is the Sharp radius, with $R _ { c }$ and $R _ { d }$ denoting the radii of the daughter nucleus and the emitted cluster, respectively.

In this work, we adopt $l ( l + 1 )  ( l + 1 / 2 ) ^ { 2 }$ as the Langer correction form, since it is a necessary correction for onedimensional problems. It can be expressed as [53]

$$
V _ {l} (r) = \frac {(l + 1 / 2) ^ {2} \hbar^ {2}}{2 \mu r ^ {2}}, \tag {10}
$$

where $\hbar$ is the reduced Planck constant. $l$ is the angular momentum carried by the emitted cluster. It can be obtained by

$$
l = \left\{ \begin{array}{l l} \triangle_ {j}, & \text {f o r e v e n} \triangle_ {j} \text {a n d} \pi_ {p} = \pi_ {d}, \\ \triangle_ {j} + 1, & \text {f o r e v e n} \triangle_ {j} \text {a n d} \pi_ {p} \neq \pi_ {d}, \\ \triangle_ {j}, & \text {f o r o d d} \triangle_ {j} \text {a n d} \pi_ {p} \neq \pi_ {d}, \\ \triangle_ {j} + 1, & \text {f o r o d d} \triangle_ {j} \text {a n d} \pi_ {p} = \pi_ {d}. \end{array} \right. \tag {11}
$$

where $\pi _ { p }$ and $\pi _ { d }$ are the parity value of the parent nucleus and the daughter nucleus, respectively. $\triangle _ { j } = | j _ { p } - j _ { d } - j _ { c } |$ , and $j _ { p } , j _ { d } , j _ { c }$ are the isospin value of the parent nuclei, the daughter nuclei and the emitted cluster, respectively [54].

# B. Cluster formation model(CFM)

The preformation factor $P _ { \alpha }$ , within the CFM, is expressible as as [40]

$$
P _ {\alpha} = \frac {E _ {f \alpha}}{E}, \tag {12}
$$

where the formation energy of the $\alpha$ cluster is designated as $E _ { f \alpha }$ , and the total energy of the system in question is referred to as E. The formation energy and total energy are determined by analyzing the neutron-neutron and proton-proton pairing interactions, along with the proton-neutron correlations. It is expressed as

$$
\begin{array}{l} E _ {j a} = 3 B (A, Z) + B (A - 4, Z - 2) \\ - 2 B (A - 1, Z - 1) - 2 B (A - 1, Z) \tag {13} \\ = [ 2 S _ {p} (A, Z) + 2 S _ {n} (A, Z) ] - 2 S _ {\alpha} (A, Z), \\ \end{array}
$$

$$
E = S _ {\alpha} (A, Z) = B (A, Z) - B (A - 4, Z - 2), \tag {14}
$$

The recently proposed CFM has been extended to evaluate the $\alpha$ preformation factors in odd- $A$ and odd-odd nuclei [55]. Subsequently, Deng et al. introduced an adaptive correction to the formation energy and investigated the $\alpha$ preformation in odd-A and odd-odd superheavy systems, achieving good consistency with both microscopic expectations and experimentally

extracted values. Moreover, the formation energy was recast in a unified form [40]:

$$
E _ {f \alpha} = \left\{ \begin{array}{l l} 2 S _ {p} + 2 S _ {n} - S _ {\alpha} & (\text {e v e n - e v e n}) \\ 2 S _ {p} + S _ {2 n} - S _ {\alpha} & (\text {e v e n - o d d}) \\ S _ {2 p} + 2 S _ {n} - S _ {\alpha} & (\text {o d d - e v e n}) \\ S _ {2 p} + S _ {2 n} - S _ {\alpha} & (\text {o d d - o d d}) \end{array} \right. \tag {15}
$$

where $S _ { p } ( S _ { n } ) , S _ { 2 p } ( S _ { 2 n } )$ are the one-proton (neutron) separation energy and two-proton (neutron) separation energy of the parent nucleus, respectively,

$$
\left\{ \begin{array}{l} S _ {p} (A, Z) = B (A, Z) - B (A - 1, Z - 1) \\ S _ {n} (A, Z) = B (A, Z) - B (A - 1, Z) \\ S _ {2 p} (A, Z) = B (A, Z) - B (A - 2, Z - 2) \\ S _ {2 n} (A, Z) = B (A, Z) - B (A - 2, Z), \end{array} \right. \tag {16}
$$

for the above formulas, we adopted existing experimental data and evaluated values from the Atomic Mass Evaluation (AME) table.

# C. Nonlocality effect

In the present work, considering the nonlocal dynamical effects, a coordinate-dependent effective mass of the $\alpha$ particle is introduced, which can be expressed as

$$
\mu = \frac {m ^ {*} M}{m ^ {*} + M}, \tag {17}
$$

where M is the nuclear mass of the daughter nucleus. In this work, a coordinate-dependent effective mass $\mathrm { m ^ { * } }$ correction is employed to describe the nonlocal dynamical effects in particle-nucleus interactions, which is expressed as the derivative of the Woods-Saxon function multiplied by a position-dependent effective mass function [56] [57] [58] [59].

$$
m ^ {*} = \frac {m}{1 - \rho (r)}, \tag {18}
$$

where m is the free mass of $\alpha$ particle and the $\rho ( r )$ function is defined as

$$
\rho (r) = \rho_ {s} a _ {s} \frac {d}{d r} \left[ 1 + \exp \left(\frac {r - R _ {s}}{a _ {s}}\right) \right] ^ {- 1}, \tag {19}
$$

where parameter $R _ { s }$ is defined as $R _ { s } = R + \Delta R$ , representing the centroid position of the effective mass function $\rho ( r )$ , with $a _ { s }$ related to the function width. The values $\Delta R = 3 . 4 4 \mathrm { f m }$ and $a _ { s } = 0 . 6 5$ are consistent with Ref. [16]. Global fitting of the mass parameter $\rho _ { s }$ to the complete experimental data set is necessary. Nonlocal effects can be incorporated into particlenucleus interactions through energy-dependent potential terms [54]. Within the WKB framework, the analytical form of the penetration factor P remains unchanged, requiring only the replacement of free mass m with effective mass $\mathrm { m ^ { * } }$ . To illustrate the contribution of effective mass $\mathrm { m ^ { * } }$ to tunneling calculations, Fig 1 presents the reduced effective mass $\mu ( r )$ [Fig. 1(a)] and

![](images/0ab5db22aa8e6d9c91530699b381bf1af4a883136c39366b7162b69e08e16581.jpg)

![](images/b8114c1360041e2a69a4fd239635d188cd092f2a950eba9ed88145ab5db917f4.jpg)  
Fig. 1: The impact of nonlocal effects on tunneling calculations is illustrated using the example of ${ } _ { 7 8 } ^ { 1 8 4 m } P t \ \alpha$ decay. In panel (a), the effective reduced mass $\mu$ is presented considering nonlocal effects. Panel (b) compares the barrier penetration integral function $f ( r )$ : the reduced mass $\mu$ (blue curve, $\rho _ { s } = - 0 . 6 1 5 )$ versus $\mu _ { 0 }$ (red curve, $\rho _ { s } = 0 \mathrm { \Omega }$ ).

Table 1: RMSE deviations $\sigma _ { \mathrm { p r e } }$ of $\alpha$ decay half-lives $T _ { 1 / 2 }$ calculated by the original CPPM, CPPM with nonlocalization considered, and three empirical formulas (UDL: Formula A, B, and C), as well as the BNN corrected $\sigma _ { \mathrm { p o s t } }$ (based on a complete dataset containing 401 α decay cases)   

<table><tr><td>Models</td><td>σpre</td><td>σpost</td><td>Δσ/σpost</td></tr><tr><td>CPPM</td><td>0.7268</td><td>0.4631</td><td>36.28%</td></tr><tr><td>CPPM(nonlocality)</td><td>0.4946</td><td>0.3796</td><td>23.25%</td></tr><tr><td>UDL(Formula-A)</td><td>0.6348</td><td>0.4121</td><td>35.99%</td></tr><tr><td>UDL(Formula-B)</td><td>0.6342</td><td>0.4345</td><td>31.49%</td></tr><tr><td>UDL(Formula-C)</td><td>0.7206</td><td>0.4596</td><td>36.22%</td></tr></table>

the function $f ( r ) = \sqrt { \mu ( r ) [ V ( r ) - Q _ { \alpha } ] }$ in the barrier penetration probability P integral [Fig. 1(b)] for $\alpha$ decay of $_ { 7 8 } ^ { 1 8 4 m } P t$ . The results reveal that nonlocality significantly affects the reduced effective mass $\mu ( r )$ near the nuclear surface, thereby modifying the profile of the penetration integral function compared to free-mass calculations.

# D. Empirical formula

1) Formula-A: The UDL formula without any modifications that was obtained by Qi et al. is expressed as [12]:

$$
\log_ {1 0} \left(T _ {1 / 2}\right) = a Z _ {c} Z _ {d} \sqrt {\frac {U}{Q _ {c}}} + b \sqrt {U Z _ {c} Z _ {d} \left(A _ {d} ^ {1 / 3} + A _ {c} ^ {1 / 3}\right)} + c, \tag {20}
$$

where U = Ac+Ad $\begin{array} { r } { U = \frac { A _ { c } A _ { d } } { A _ { c } + A _ { d } } } \end{array}$ AcAd and the adjustable parameters are $a = 0 . 4 3 1 4$ , $b = - 0 . 4 0 8 7$ , and $c = - 2 5 . 7 7 2 5$ [12].

2) Formula-B: The UDL formula for angular momentum cases, as proposed by Qi et al., takes the following form [60]:

$$
\begin{array}{l} \log_ {1 0} (T _ {1 / 2}) = a Z _ {c} Z _ {d} \sqrt {\frac {U}{Q _ {c}}} + b \sqrt {U Z _ {c} Z _ {d} (A _ {d} ^ {1 / 3} + A _ {c} ^ {1 / 3})} \\ + c + d \sqrt {U Z _ {c} Z _ {d} \left(A _ {d} ^ {1 / 3} + A _ {c} ^ {1 / 3}\right)} \sqrt {l (l + 1)}, \tag {21} \\ \end{array}
$$

where the parameters $a , b$ , and $c$ adopt the same values as in the UDL version, while the parameter $d = 0 . 0 0 4 7 6$ is taken from Ref. [13].

3) Formula-C: The UDL formula, modified to incorporate the isospin effect, can be expressed as follows:

$$
\begin{array}{l} \log_ {1 0} (T _ {1 / 2}) = a Z _ {c} Z _ {d} \sqrt {\frac {U}{Q _ {c}}} + b \sqrt {U Z _ {c} Z _ {d} (A _ {d} ^ {1 / 3} + A _ {c} ^ {1 / 3})} \\ + c + e \sqrt {I (I + 1)}, \tag {22} \\ \end{array}
$$

where $\begin{array} { r } { I = \frac { A - 2 Z } { A } } \end{array}$ . The parameter $a , b , c , e$ are taken from Ref. [13].

Table 2: The RMSE deviation of the half-life $T _ { 1 / 2 }$ provided by the theoretical model is denoted as $\sigma _ { \mathrm { p r e } }$ , while the RMSE deviation following calibration with the BNN is denoted $\mathrm { a s } \sigma _ { \mathrm { p o s t } }$ . A total of 401 data sets were randomly divided into a training set $8 0 \%$ , 300 sets) and a validation set $2 0 \%$ , 101 sets).

<table><tr><td rowspan="2">Models</td><td colspan="3">Learning set</td><td colspan="3">Validation set</td></tr><tr><td>σpre</td><td>σpost</td><td>Δσ/σpre</td><td>σpre</td><td>σpost</td><td>Δσ/σpost</td></tr><tr><td>CPPM</td><td>0.7178</td><td>0.4283</td><td>40.41%</td><td>0.7580</td><td>0.5509</td><td>27.32%</td></tr><tr><td>CMMP(nonlocality)</td><td>0.4924</td><td>0.3738</td><td>24.09%</td><td>0.5032</td><td>0.4398</td><td>12.60%</td></tr><tr><td>UDL(Formula-A)</td><td>0.6352</td><td>0.4044</td><td>36.34%</td><td>0.6768</td><td>0.4345</td><td>35.80%</td></tr><tr><td>UDL(Formula-B)</td><td>0.6287</td><td>0.4166</td><td>33.74%</td><td>0.6555</td><td>0.4906</td><td>25.16%</td></tr><tr><td>UDL(Formula-C)</td><td>0.7131</td><td>0.4486</td><td>37.09%</td><td>0.7496</td><td>0.4880</td><td>34.90%</td></tr></table>

# E. Bayesian Neural Network

BNN constitute a probabilistic architecture, with comprehensive details provided in Ref. [61]; This work focuses solely on their essential characteristics. Within the Bayesian framework, model parameters $\omega$ are represented as probability distributions rather than the deterministic values employed in conventional neural networks. A prior distribution $p ( \omega )$ is introduced over all possible values of $\omega$ . Given a dataset $D = \{ ( x _ { i } , t _ { i } ) \mid i = 1 , 2 , \ldots , n \}$ , where $x _ { i }$ and $t _ { i }$ denote the input and target output samples respectively, and $n$ represents the sample size, the posterior distribution $p ( \omega | D )$ can be derived through Bayes theorem

upon incorporation of the data $D$ .

$$
p (\omega | D) = \frac {p (D | \omega) p (\omega)}{p (D)}, \tag {23}
$$

where $p ( D | \omega )$ is the likelihood function, $p ( D )$ is a normalization constant, which ensures the posterior distribution is a valid probability density and integrates to one.

Table 3: Effect of different feature inputs on the RMSE deviation of $\alpha$ decay half-life $T _ { 1 / 2 }$ calculated by various models using the BNN Method. The quadrupole deformation parameters $\beta _ { 2 }$ are taken from Ref. [62]

<table><tr><td>Models</td><td>Inputs</td><td>RMSE</td></tr><tr><td>CPPM</td><td>A,Z,Q,l,Pa</td><td>0.4631</td></tr><tr><td>CPPM</td><td>A,Z,Q,l,Pa,β2</td><td>0.4535</td></tr><tr><td>CMMP(nonlocality)</td><td>A,Z,Q,l,Pa</td><td>0.3796</td></tr><tr><td>CMMP(nonlocality)</td><td>A,Z,Q,l,Pa,β2</td><td>0.3733</td></tr><tr><td>UDL(Formula-A)</td><td>A,Z,Q,l,Pa</td><td>0.4121</td></tr><tr><td>UDL(Formula-A)</td><td>A,Z,Q,l,Pa,β2</td><td>0.4113</td></tr><tr><td>UDL(Formula-B)</td><td>A,Z,Q,l,Pa</td><td>0.4345</td></tr><tr><td>UDL(Formula-B)</td><td>A,Z,Q,l,Pa,β2</td><td>0.4293</td></tr><tr><td>UDL(Formula-C)</td><td>A,Z,Q,l,Pa</td><td>0.4596</td></tr><tr><td>UDL(Formula-C)</td><td>A,Z,Q,l,Pa,β2</td><td>0.4373</td></tr></table>

In this study, the prior distribution $p ( \omega )$ is modeled as a zero-mean Gaussian, whose precision (inverse variance) is governed by a gamma distribution. This configuration allows the precision parameter to vary over a wide range, enabling the BNN method to automatically determine its optimal value during sampling [63]. The likelihood function is commonly modeled as a Gaussian distribution, $p ( D | \omega ) = \exp \bigl ( - \chi ^ { 2 } / 2 \bigr )$ , where

$$
\chi^ {2} = \sum_ {n = 1} ^ {N} \left(\frac {t _ {n} - S (x ; \omega)}{\Delta t _ {n}}\right) ^ {2}, \tag {24}
$$

here, $\Delta t _ { n }$ denotes the associated noise error for the i-th observable, and N represents the total number of observational data points. In the BNN framework, the network $S ( \boldsymbol { x } ; \boldsymbol { \omega } )$ can be expressed as:

$$
S (x; \omega) = a + \sum_ {j = 1} ^ {H} b _ {j} \tanh  \left(c _ {j} + \sum_ {i = 1} ^ {I} d _ {j i} x _ {i}\right), \tag {25}
$$

where $x = \{ x _ { i } \}$ represents the input data, $w = \{ a , b _ { j } , c _ { j } , d _ { j i } \}$ are the model free parameters. $H$ and $I$ denote, respectively, the number of hidden-layer neurons and the dimensionality of the input. Given the prior distribution $p ( \omega )$ and likelihood function $p ( D | \omega )$ , the posterior distribution $p ( \omega | D )$ is obtained via variational inference to compute BNN predictions:

$$
\langle S \rangle = \int S (x; \omega) p (\omega | D) d \omega , \tag {26}
$$

Within the Bayesian inference framework, variational inference approximates the intractable posterior distribution $p ( \omega | D )$ by introducing a parameterized distribution $q _ { \theta } ( \omega )$ , where $\theta$ denotes the variational parameters [64]. The core objective is to

minimize the Kullback-Leibler(KL) divergence [65] between the variational and true posterior distributions:

$$
K L \left(q _ {\theta} (\omega) | | p (\omega | D)\right) = \int q _ {\theta} (\omega) \log \left(\frac {q _ {\theta} (\omega)}{p (\omega | D)}\right) d \omega , \tag {27}
$$

Table 4: Based on the CPPM: comparison of optimization effects on the CPPM via different strategies (considering local effects, BNN Method, and BNN method combined with nonlocal).

<table><tr><td>Method</td><td>σpost</td><td>Δσ/σpost</td></tr><tr><td>nonlocality</td><td>0.4946</td><td>31.95%</td></tr><tr><td>BNN</td><td>0.4631</td><td>36.28%</td></tr><tr><td>nonlocality+BNN</td><td>0.3796</td><td>47.77%</td></tr></table>

Since direct computation of the posterior $p ( \omega | D )$ is typically intractable in practice, we introduce the evidence lower bound (ELBO) as an alternative optimization objective:

$$
\begin{array}{l} K L (q _ {\theta} | | p) = \log p (D) - \int q _ {\theta} (\omega) \log p (D | \omega) d \omega - \int q _ {\theta} (\omega) \log \left(\frac {q _ {\theta} (\omega)}{p (\omega)}\right) d \omega \\ { = } { \log p ( D ) - \left[ E _ { q _ { \theta } ( \omega ) } [ \log p ( D | \omega ) ] - K L ( q _ { \theta } ( \omega ) | | p ( \omega ) ) \right] } \\ = \log p (D) - \mathcal {L} (\theta) \tag {28} \\ \end{array}
$$

where

$$
\mathcal {L} (\theta) = E _ {q _ {\theta} (\omega)} \left[ \log (p (D | \omega)) - K L \left(q _ {\theta} (\omega) \mid \mid p (\omega)\right) \right], \tag {29}
$$

The first term represents the expected log-likelihood, encouraging the variational distribution to better fit the observed data, while the second term serves as a KL regularization that constrains the variational distribution to remain close to the prior $p ( \omega )$ . Since $\log ( P ( \omega ) )$ is constant with respect to $\theta$ , maximizing the ELBO is equivalent to minimizing the original KL divergence. The optimization is performed using the Bayes by Backprop algorithm [66], which employs Monte Carlo sampling to obtain unbiased gradient estimates for efficient parameter updates.

In this work, BNN is employed to directly train the residuals $t _ { k }$ , establishing their implicit correlations with the characteristic parameters $A , Z , Q _ { c } , l , P _ { \alpha }$ $P _ { \alpha }$ and $\beta _ { 2 }$ . Here, $t _ { k } = \log _ { 1 0 } ( T _ { 1 / 2 } ^ { \mathrm { e x p } } ) - \log _ { 1 0 } ( T _ { 1 / 2 } ^ { t h } ) = \log _ { 1 0 } ( T _ { 1 / 2 } ^ { \mathrm { e x p } } / ( T _ { 1 / 2 } ^ { t h } )$ . The RMSE deviation $\sigma$ is used to assess the predictive accuracy of BNN corrected models:

$$
\sigma = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} \left[ \log_ {1 0} \left(\frac {T _ {1 / 2} ^ {\exp}}{T _ {1 / 2} ^ {t h}}\right) \right] ^ {2}}, \tag {30}
$$

where, $\log _ { 1 0 } T _ { 1 / 2 } ^ { \mathrm { e x p } }$ represents the experimental half-life of nuclear decay, while $\log _ { 1 0 } T _ { 1 / 2 } ^ { t h }$ denotes the theoretical half-life calculated by the model.

# III. RESULTS AND DISCUSSION

In this study, we utilize a total of 401 datasets, which include the experimental decay half-lives $\log _ { 1 0 } T _ { 1 / 2 } ^ { \mathrm { e x p } }$ , the angular momentum $l$ of the emitted cluster, $\alpha$ decay energy $Q _ { c }$ and the parameters required to calculate $P _ { \alpha }$ using the CFM method,

![](images/0d11ce1456b3c14c7371229d5441dc34c96194b6f5beb22beb6aa72424937579.jpg)  
Fig. 2: The figure displays the importance ranking of four input features obtained using the SHAP toolkit. Each row represents a feature, with the horizontal axis showing its SHAP value, which reflects the feature’s significance in the specific prediction. Each point corresponds to a sample, and the color of the points indicates the feature value, with red representing high values and blue representing low values.

with all data sourced from the Atomic Mass Evaluation (AME) table1. Recent research by Medeiros demonstrates significant improvements in the theoretical calculations of the $\alpha$ decay half-lives for even-even nuclei using the semiclassical WKB method, achieved through the introduction of coordinate-dependent effective mass. Furthermore, Hu et al. systematically investigated nonlocal effects in the $\alpha$ decay half-lives of even-even nuclei within the framework of a two-potential model. The results indicate a significant improvement in model accuracy following the introduction of the effective mass parameter for the $\alpha$ particle.

To further investigate the application of effective mass in theoretical models of $\alpha$ decay half-lives, We incorporate a coordinate-dependent effective mass parameter into the CPPM. We calculate the $\alpha$ decay half-lives for 401 nuclei and compare these results with those obtained from CPPM without considering effective mass. In the calculations of $\alpha$ decay half-lives within the dataset, the parameter $\rho _ { s }$ is a critical parameter that is adjusted to minimize the RMSE deviations. Comparing with experimental results, when the coordinate-dependent effective mass is not considered (i.e., with the adjustment parameter $\rho _ { s } = 0 ,$ ), the standard deviation is $\sigma _ { \rho _ { s } = 0 } = 0 . 7 2 6 8$ . However, when the parameter $\rho _ { s }$ is adjusted to $- 0 . 6 1 5$ , the standard deviation reduces to $\sigma _ { \rho _ { s } = - 0 . 6 1 5 } = 0 . 4 9 4 6$ . These results indicate a significant enhancement in the CPPM calculations when incorporating the coordinate-dependent effective mass (with $\rho _ { s } = - 0 . 6 1 5 )$ . The RMSE deviations decreased by approximately $3 1 . 9 5 \%$ . We summarize the effects of the potential nonlocal dynamic effects. Fig 1 illustrates the reduced effective mass $\mu$ during the $\alpha$ decay of $_ { 7 8 } ^ { 1 8 4 m } P t$ (Fig.1(a)) and its simplified form of the potential function $f ( r ) = \sqrt { \mu ( r ) [ V ( r ) - Q _ { \alpha } ] }$ (Fig.1(b)). As shown in Fig.1(a), when considering the nonlocality of the potential, the effective mass decreases significantly; specifically, at $r = R _ { s }$ , the effective mass is reduced by approximately $1 7 . 7 \%$ , with a corresponding change in the simplified form of the potential function (as shown in Fig.1(b)). These results are consistent with the conclusions of Medeiros et al., further demonstrating the significant impact of nonlocal effects on $\alpha$ decay half-lives. Furthermore, accounting for these effects enhances the accuracy of the CPPM predictions for $\alpha$ decay half-lives.

Table 5: Predicted $\alpha$ decay half-lives of 14 nuclei $\langle Z = 1 1 8 , 1 2 0 \rangle$ ) using BNN in logarithmic form. The values of $Q _ { \alpha } ^ { R C H B }$ , $Q _ { \alpha } ^ { W S 4 }$ , and $Q _ { \alpha } ^ { F R D M }$ α denote data derived from the RCHB [67], WS4 [68], and FRDM [69] mass tables, respectively, with units in MeV.   

<table><tr><td>nucleus</td><td>\(Q_{\alpha}^{RCHB}\)</td><td>\(\log_{1/2}^{RCHB}\)</td><td>\(Q_{\alpha}^{WS4}\)</td><td>\(\log_{1/2}^{WS4}\)</td><td>\(Q_{\alpha}^{FRDM}\)</td><td>\(\log_{1/2}^{FRDM}\)</td></tr><tr><td>\(^{292}118\)</td><td>10.96</td><td>-0.880</td><td>12.24</td><td>-3.803</td><td>12.38</td><td>-4.110</td></tr><tr><td>\(^{294}118\)</td><td>10.91</td><td>-0.813</td><td>12.20</td><td>-3.784</td><td>12.36</td><td>-4.138</td></tr><tr><td>\(^{296}118\)</td><td>10.77</td><td>-0.534</td><td>11.75</td><td>-2.831</td><td>12.27</td><td>-4.010</td></tr><tr><td>\(^{298}118\)</td><td>10.61</td><td>-0.202</td><td>12.18</td><td>-3.880</td><td>12.48</td><td>-4.548</td></tr><tr><td>\(^{300}118\)</td><td>10.47</td><td>0.091</td><td>11.95</td><td>-3.425</td><td>12.50</td><td>-4.666</td></tr><tr><td>\(^{302}118\)</td><td>10.61</td><td>-0.303</td><td>12.04</td><td>-3.700</td><td>12.61</td><td>-4.985</td></tr><tr><td>\(^{304}118\)</td><td>12.65</td><td>-5.150</td><td>13.12</td><td>-6.204</td><td>13.38</td><td>-6.793</td></tr><tr><td>\(^{296}120\)</td><td>11.87</td><td>-2.413</td><td>13.34</td><td>-5.570</td><td>13.58</td><td>-6.086</td></tr><tr><td>\(^{298}120\)</td><td>11.76</td><td>-2.225</td><td>12.91</td><td>-4.734</td><td>13.23</td><td>-5.412</td></tr><tr><td>\(^{300}120\)</td><td>11.62</td><td>-1.967</td><td>13.32</td><td>-5.679</td><td>13.68</td><td>-6.460</td></tr><tr><td>\(^{302}120\)</td><td>11.51</td><td>-1.775</td><td>12.89</td><td>-4.837</td><td>13.55</td><td>-6.254</td></tr><tr><td>\(^{304}120\)</td><td>11.72</td><td>-2.316</td><td>12.76</td><td>-4.631</td><td>13.54</td><td>-6.310</td></tr><tr><td>\(^{306}120\)</td><td>13.58</td><td>-6.477</td><td>13.78</td><td>-6.919</td><td>14.26</td><td>-7.977</td></tr><tr><td>\(^{308}120\)</td><td>13.07</td><td>-5.443</td><td>12.96</td><td>-5.206</td><td>12.96</td><td>-5.206</td></tr></table>

In this section, we comprehensively evaluate the global optimization performance and extrapolation capability of the BNN approach. Five benchmark models are selected for comparative analysis: the CPPM, the nonlocally modified CPPM, and three distinct parameterizations of the UDL(Formula-A, Formula-B, Formula-C). The complete dataset comprising 401 α decay nuclides is employed for model training and validation. We first calculate the raw residuals $t _ { k } ( A , Z , Q _ { \alpha } , \ell , P _ { \alpha } )$ for each benchmark model and determine the RMSE $\sigma _ { \mathrm { p r e } }$ across the entire dataset; detailed numerical values are presented in Table 1. Subsequently, using the raw residuals $t _ { k } ( A , Z , Q _ { \alpha } , \ell , P _ { \alpha } )$ as input features, we systematically calibrate the theoretical predictions through the BNN method, yielding corrected half-lives $T _ { 1 / 2 }$ . To quantitatively assess the improvement achieved by BNN calibration, Table 1 also reports the relative improvement ratio

$$
\frac {\Delta \sigma}{\sigma_ {\mathrm {p r e}}} = \frac {\sigma_ {\mathrm {p r e}} - \sigma_ {\mathrm {p o s t}}}{\sigma_ {\mathrm {p r e}}}, \tag {31}
$$

where $\sigma _ { \mathrm { p o s t } }$ denotes the RMSE after calibration.

From Table 1, it is clear that although the CPPM exhibits excellent robustness, there remain notable discrepancies between the theoretical $T _ { 1 / 2 }$ and the experimental data. Following BNN calibration, the prediction accuracy for $\alpha$ decay based on CPPM(nonlocal) has increased by over $2 3 . 2 5 \%$ . This section presents a systematic assessment of the global optimization capability and extrapolation performance of the BNN approach. Using the relative RMSE reduction $\Delta \sigma / \sigma _ { \mathrm { p r e } }$ the predictive performance of the three distinct parameterizations of the UDL(Formula-A, Formula-B, Formula-C) has improved by $3 5 . 9 9 \%$ , $3 1 . 4 9 \%$ , and $3 6 . 2 2 \%$ , respectively. This underscores the ability of the BNN method to effectively uncover latent half-life correlations among different nuclei, thereby optimizing computational results and significantly enhancing the predictive capability of model-based semi-empirical formulas. A comparison of the data in Table 1 leads to the conclusion that the BNN method is applicable to both CPPM and various empirical formulas, with accuracy improvements reliant on the judicious selection of feature inputs.

In the field of nuclear physics, the prediction of nuclear decay half-lives holds significant practical value; however, it faces

![](images/f1e8f48b3d46e9f83399218b015273de28cac23e0583af5a4a01a2ffe0321a2f.jpg)

![](images/d19be87de2ddf1cf9e9949d4d401d9e1761412d9f59dd72853604698d235c0d6.jpg)

![](images/c682fddc1bb1bd10ec91a766b460177354b04256de53e60047b104f7d2a028c6.jpg)  
Fig. 3: α decay half-lives of isotopes with atomic numbers $Z = 1 1 8$ and $Z = 1 2 0$ predicted using the BNN method. Herein, black squares and red dots correspond to $Z = 1 1 8$ and $Z = 1 2 0$ , respectively; the horizontal axis denotes the neutron number $N$ , and the vertical axis represents the logarithm of the half-life, $\log _ { 1 0 } T _ { 1 / 2 }$ ; three mass tables (RCHB, WS4, FRDM) are employed in this figure.

considerable challenges, particularly in regions with scarce experimental data. This section focuses on evaluating the capability of the BNN method for extrapolating $\alpha$ decay half-life predictions. Prior to the predictions, we randomly divided 401 data sets into a training set $8 0 \%$ , 300 sets) and a validation set $2 0 \%$ , 101 sets). Initially, we determined the neural network parameters using the training set data, and upon completing the model calibration, we calculated the RMSE deviations and improvement rates $\Delta \sigma / \sigma _ { p o s t }$ for both the training and validation sets, as detailed in Table 2. After posterior correction based on the BNN, compared with the uncorrected original CPPM, the RMSE of the model decreases by $4 0 . 4 1 \%$ on the training set and by $2 7 . 3 2 \%$ on the validation set. For the nonlocally modified CPPM, the corresponding RMSE reductions are $2 4 . 0 9 \%$ and $1 2 . 6 0 \%$ . Across the three empirical formulas examined, the BNN likewise yields substantial improvements, particularly for Formula A and Formula B, for which the training and validation set RMSEs are both reduced by more than $3 4 . 9 0 \%$ . Altogether, results based on CPPM and multiple $\alpha$ decay empirical relations indicate that the BNN provides reliable extrapolation in half-life prediction and delivers highly credible estimates.

Building on the preceding calculations, we incorporate the quadrupole deformation parameter $\beta _ { 2 }$ into the feature vector $\left( A , Z , Q _ { \alpha } , \ell , P _ { \alpha } , \beta _ { 2 } \right)$ and re-calibrate the BNN for each physical model and empirical relation. The results are summarized in Table 3. Relative to the deformation-agnostic BNN, including $\beta _ { 2 }$ yields additional RMSE reductions of 0.0096, 0.0063, 0.0008, 0.0052, and 0.0023 for CPPM, CPPM (nonlocal), and three distinct parameterizations of the UDL(Formula-A, Formula-B, Formula-C), respectively. These findings are consistent with Ref. [70].

![](images/e762b446eebde30fbf0200760e8f66769bd749600d0628854e9fef27ff748d37.jpg)

![](images/37b55f3150c05ea5bafea7a9c06ef97bfdc4fa8c4e865587d074ea0091822cd6.jpg)

![](images/a604814b499a196b7bbab7a0a0613c62a1978d01aa3ba2d29ad3c0f6efd6a0de.jpg)  
Fig. 4: G-N plots of $\alpha$ decay for $Z { = } 1 1 8$ and ${ \cal Z } { = } 1 2 0$ isotopes predicted by the BNN method.

Table 4 provides a clear comparison of the optimization gains achieved for CPPM by different strategies. When considering only localization effects or when directly optimizing CPPM with the BNN, the relative reduction in RMSE $\Delta \sigma / \sigma _ { \mathrm { p r e } }$ reaches $3 1 . 9 5 \%$ and $3 6 . 2 8 \%$ , respectively. By contrast, applying BNN optimization to the nonlocal CPPM yields $\Delta \sigma / \sigma _ { \mathrm { p r e } } = 4 7 . 7 7 \%$ , indicating a markedly stronger improvement and highlighting the synergy between nonlocality and BNN modeling in enhancing CPPM’s predictive accuracy.

The interpretability of machine learning has emerged as a key area of research. Through interpretability analysis, we gain deeper insights into how algorithms extract meaningful information from vast datasets. To unveil the learning patterns of the CPPM, this study employs Shapley Additive Explanations to calculate SHAP values for each signal sample, thereby identifying the features that most significantly impact the prediction of T values. The arrangement of signals reflects their contribution levels. Each row represents a signal, with red points indicating higher value data points and blue points indicating lower value data points. Points on the right indicate a significant positive impact of the feature on the prediction, while points on the left suggest a negative influence. Fig 2 presents the importance ranking of six features, revealing that the decay energy $Q _ { \alpha }$ and the proton number $Z$ are crucial driving factors in the CPPM predictions. This finding provides significant insights into the understanding of nuclear decay mechanisms.

This study employs BNN approach to predict the $\alpha$ decay half-lives. Given the high sensitivity of half-lives to the $\alpha$ decay energy ( $Q _ { \alpha }$ value), selecting appropriate mass models for calculation is crucial. For comparative purposes, we utilized three mass models: Relativistic Continuum Hartree-Bogoliubov (RCHB) [67], Weizsacker–Skyrme-4(WS4) [68], and Finite Range Droplet Model (FRDM) [69] to compute $Q _ { \alpha }$ values. The calculation results are presented in Table 5, where the first column

![](images/381f57fab0a6a0d912bad8f5775571d1eab125835ee7ec2276f55a8b1a370b09.jpg)  
Fig. 5: Universal curves of $\alpha$ decay half-lives for isotopes with atomic numbers $Z = 1 1 8$ and $Z = 1 2 0$ versus negative logarithm of penetrability $( - \ln \mathbf { P } )$ predicted using BNN method.

lists the $\alpha$ decay parent nuclei, The second to third columns, fourth to fifth columns, and sixth to seventh columns correspond to the $Q _ { \alpha }$ values and the logarithmic forms of the $\alpha$ decay half-lives for the three models, respectively. To visually illustrate the impact of the three mass models on half-life calculations, we present the data from Table 5 in graphical form. Fig 3 presents the predicted half-life curves for isotopes with $Z = 1 1 8$ and $Z = 1 2 0$ . The figure clearly shows that $N = 1 8 4$ exhibits a significant shell effect across all three models. Notably, the shell effect at $N = 1 7 8$ varies depending on the model employed: specifically, it is more pronounced in the WS4 and FRDM models, whereas it appears relatively vague in the RCHB model.

To further validate the reliability of the predicted half-lives, we employ the classical G-N law as a benchmark test [71] [72]. Established by Geiger and Nuttall in 1911, this law describes the relationship between the half-life of $\alpha$ decay and the $Q$ value, expressed mathematically as

$$
\log_ {1 0} \left(T _ {1 / 2}\right) = \frac {a}{\sqrt {Q _ {\alpha}}} + b, \tag {32}
$$

where $a$ and $b$ denote the intercept and slope of the linear fit, respectively. In Fig. 4, we can observe that the BNN calibrated CPPM (including nonlocal corrections) predictions adhere well to the expected G-N linear relationship.

Furthermore, as shown in Fig. 5, we investigate the correlation between the logarithm of predicted half-lives $\log _ { 1 0 } ( T _ { 1 / 2 } )$ , and the negative logarithm of penetration probabilities $- \ln \mathrm { P } .$ The results reveal a robust linear correlation consistent with the G-N law. These findings indicate that the BNN approach not only significantly reduces the RMSE but also accurately preserves the fundamental physical scaling laws of $\alpha$ decay, thereby confirming that our method captures the essential physics of the decay process.

# IV. SUMMARY

We extend the semiclassical WKB approach within the CPPM by introducing a coordinate-dependent effective mass for the emitted $\alpha$ particle, thereby quantifying the impact of nonlocal effects on $\alpha$ decay half-lives. Furthermore, we develop the BNN framework to capture the intrinsic correlations between the half-life and the relevant physical descriptors, including the mass number $A$ , proton number $Z$ , decay energy $Q _ { \alpha }$ , orbital angular momentum l, preformation factor $P _ { \alpha }$ , quadrupole deformation $\beta _ { 2 }$ , along with residual $t _ { k }$ . The application of the BNN to optimize CPPM, CPPM (nonlocal), and three distinct parameterizations of the UDL(Formula-A, Formula-B, Formula-C), leads to a notable enhancement in $\alpha$ decay half-life prediction accuracy, exceeding $2 3 . 2 5 \%$ overall. Moreover, combining the BNN with a non-localized method for the optimization of the CPPM results in a further dramatic improvement, with an accuracy gain of up to $4 7 . 7 7 \%$ . These results demonstrate the robustness and reliability of the BNN-based approach for $\alpha$ decay modeling. Building on this framework, we predict $\alpha$ decay halflives for the isotopic chains with $Z \ = \ 1 1 8$ and $Z ~ = ~ 1 2 0$ , unveiling pronounced shell effects and showcasing excellent extrapolation capability. The predictions exhibit a linear Geiger-Nuttall-type correlation between $\log _ { 1 0 } T$ and $Q _ { \alpha }$ , consistent with the correlation between $\log _ { 1 0 } T$ and the negative logarithm of the barrier penetration probability $- \ln \mathbf { P }$ thereby lending further credence to the method. Overall, BNN opens an effective and versatile avenue for quantitative descriptions of nuclear decay processes.

# V. ACKNOWLEDGEMENTS

This work is supported by Yunnan Provincial Science Foundation Project (No. 202501AT070067), Yunnan Provincial Xing Dian Talent Support Program (Young Talents Special Program, No. XDYC-QNRC-2023-0162), Kunming University Talent Introduction Research Project (No. YJL24019), Yunnan Provincial Department of Education Scientific Research Fund Project (No. 2025Y1055 and 2025Y1042), the Program for Frontier Research Team of Kunming University 2023, and National Natural Science Foundation of China (No. 12063006), the Special Basic Cooperative Research Programs of Yunnan Provincial Undergraduate Universities’ Association (grant NO. 202101BA070001-144).

# REFERENCES

[1] George Gamow, “Zur quantentheorie des atomkernes,” Zeitschrift fur Physik ¨ , vol. 51, no. 3, pp. 204–212, 1928.   
[2] Ronald W Gurney and Edw U Condon, “Wave mechanics and radioactive disintegration,” Nature, vol. 122, no. 3073, pp. 439–439, 1928.   
[3] EU Condon and RW Gurney, “Wave mechanics and radioactive disintegration,” Nature, vol. 122, pp. 439, 1928.   
[4] Xiaojun Bao, Hongfei Zhang, Haifei Zhang, Guy Royer, and Junqing Li, “Systematical calculation of $_ \alpha$ decay half-lives with a generalized liquid drop model,” Nuclear Physics A, vol. 921, pp. 85–95, 2014.   
[5] Guy Royer and R Moustabchir, “Light nucleus emission within a generalized liquid-drop model and quasimolecular shapes,” Nuclear Physics A, vol. 683, no. 1-4, pp. 182–206, 2001.   
[6] JP Cui, YL Zhang, S Zhang, and YZ Wang, “ $\scriptstyle \cdot _ { \alpha }$ -decay half-lives of superheavy nuclei,” Physical Review C, vol. 97, no. 1, pp. 014316, 2018.   
[7] KP Santhosh, C Nithya, H Hassanabadi, and Dashty T Akrawy, “ $_ \alpha$ -decay half-lives of superheavy nuclei from a modified generalized liquid-drop model,” Physical Review C, vol. 98, no. 2, pp. 024625, 2018.   
[8] KP Santhosh and Tinu Ann Jose, “Half-lives of cluster radioactivity using the modified generalized liquid drop model with a new preformation factor,” Physical Review C, vol. 99, no. 6, pp. 064604, 2019.   
[9] KP Santhosh, Dashty T Akrawy, H Hassanabadi, Ali H Ahmed, and Tinu Ann Jose, “ $\scriptstyle { \dot { \alpha } }$ -decay half-lives of lead isotopes within a modified generalized liquid drop model,” Physical Review C, vol. 101, no. 6, pp. 064610, 2020.

[10] KP Santhosh and B Priyanka, “The role of doubly magic 208pb and its neighbour nuclei in cluster radioactivity,” The European Physical Journal A, vol. 49, no. 6, pp. 66, 2013.   
[11] BirBikram Singh, SK Patra, and Raj K Gupta, “Cluster radioactive decay within the preformed cluster model using relativistic mean-field theory densities,” Physical Review C—Nuclear Physics, vol. 82, no. 1, pp. 014607, 2010.   
[12] Chong Qi, FR Xu, Roberto J Liotta, and Ramon Wyss, “Universal decay law in charged-particle emission and exotic cluster radioactivity,” Physical review letters, vol. 103, no. 7, pp. 072501, 2009.   
[13] Asım Soylu and Chong Qi, “Extended universal decay law formula for the $_ \alpha$ and cluster decays,” Nuclear Physics A, vol. 1013, pp. 122221, 2021.   
[14] Herman Feshbach, “The optical model and its justification,” Annual Review of Nuclear Science, vol. 8, no. 1, pp. 49–104, 1958.   
[15] WE Frahn and RH Lemmer, “Velocity-dependent nuclear interaction,” Il Nuovo Cimento (1955-1965), vol. 5, no. 6, pp. 1564–1572, 1957.   
[16] Emil L Medeiros, N Teruya, Sergio B Duarte, and OAP Tavares, “Nonlocality effect in ´ $_ \alpha$ decay of heavy and superheavy nuclei,” Physical Review C, vol. 106, no. 2, pp. 024608, 2022.   
[17] Jinyu Hu and Chen Wu, “Nonlocality effect in $_ \alpha$ decay half-lives for even-even nuclei within a two potential approach,” The European Physical Journal A, vol. 61, no. 6, pp. 129, 2025.   
[18] ZM Niu, HZ Liang, BH Sun, WH Long, and YF Niu, “Predictions of nuclear $\beta$ -decay half-lives with machine learning and their impact on r-process nucleosynthesis,” Physical Review C, vol. 99, no. 6, pp. 064307, 2019.   
[19] Hiroki Iwamoto, “Generation of nuclear data using gaussian process regression,” Journal of Nuclear Science and Technology, vol. 57, no. 8, pp. 932–938, 2020.   
[20] Ziyi Yuan, Dong Bai, Zhongzhou Ren, and Zhen Wang, “Theoretical predictions on $_ \alpha$ -decay properties of some unknown neutron-deficient actinide nuclei using machine learning,” Chinese Physics C, vol. 46, no. 2, pp. 024101, 2022.   
[21] Yunfei Ma, Chen Su, Jian Liu, Zhongzhou Ren, Chang Xu, and Yonghao Gao, “Predictions of nuclear charge radii and physical interpretations based on the naive bayesian probability classifier,” Physical Review C, vol. 101, no. 1, pp. 014304, 2020.   
[22] Yifan Liu, Chen Su, Jian Liu, Pawel Danielewicz, Chang Xu, and Zhongzhou Ren, “Improved naive bayesian probability classifier in predictions of nuclear mass,” Physical Review C, vol. 104, no. 1, pp. 014315, 2021.   
[23] Chen-Qi Li, Chao-Nan Tong, Hong-Jing Du, and Long-Gang Pang, “Deep learning approach to nuclear masses and $_ \alpha$ -decay half-lives,” Physical Review C, vol. 105, no. 6, pp. 064306, 2022.   
[24] Na-Na Ma, Tian-Liang Zhao, Wen-Xia Wang, and Hong-Fei Zhang, “Simple deep-learning approach for $_ \alpha$ -decay half-life studies,” Physical Review C, vol. 107, no. 1, pp. 014310, 2023.   
[25] Roger G Melko, Giuseppe Carleo, Juan Carrasquilla, and J Ignacio Cirac, “Restricted boltzmann machines in quantum physics,” Nature Physics, vol. 15, no. 9, pp. 887–892, 2019.   
[26] Tom Vieijra, Corneel Casert, Jannes Nys, Wesley De Neve, Jutho Haegeman, Jan Ryckebusch, and Frank Verstraete, “Restricted boltzmann machines for quantum states with non-abelian or anyonic symmetries,” Physical review letters, vol. 124, no. 9, pp. 097201, 2020.   
[27] ZM Niu, BH Sun, HZ Liang, YF Niu, and JY Guo, “Improved radial basis function approach with odd-even corrections,” Physical Review C, vol. 94, no. 5, pp. 054315, 2016.   
[28] JS Zheng, NY Wang, ZY Wang, ZM Niu, YF Niu, and B Sun, “Mass predictions of the relativistic mean-field model with the radial basis function approach,” Physical Review C, vol. 90, no. 1, pp. 014303, 2014.   
[29] Xuanpeng Xiao, Panpan Qi, Gongming Yu, Haitao Yang, and Qiang Hu, “Bayesian optimization and nonlocal effects method for {\alpha} decay of superheavy nuclei based on cppm,” arXiv preprint arXiv:2507.19091, 2025.   
[30] Leo Neufcourt, Yuchen Cao, Witold Nazarewicz, Erik Olsen, and Frederi Viens, “Neutron drip line in the ca region from bayesian model averaging,”´ Physical review letters, vol. 122, no. 6, pp. 062502, 2019.   
[31] Ze-Peng Gao, Yong-Jia Wang, Hong-Liang Lu, Qing-Feng Li, Cai-Wan Shen, and Ling Liu, “Machine learning the nuclear mass,” ¨ Nuclear Science and Techniques, vol. 32, no. 10, pp. 109, 2021.   
[32] Igor Kononenko, “Bayesian neural networks,” Biological Cybernetics, vol. 61, no. 5, pp. 361–370, 1989.   
[33] Jouko Lampinen and Aki Vehtari, “Bayesian approach for neural networks—review and case studies,” Neural networks, vol. 14, no. 3, pp. 257–274, 2001.   
[34] Raditya Utama, Wei-Chia Chen, and Jorge Piekarewicz, “Nuclear charge radii: density functional theory meets bayesian neural networks,” Journal of Physics G: Nuclear and Particle Physics, vol. 43, no. 11, pp. 114002, 2016.

[35] Xiao-Xu Dong, Rong An, Jun-Xu Lu, and Li-Sheng Geng, “Novel bayesian neural network based approach for nuclear charge radii,” Physical Review C, vol. 105, no. 1, pp. 014308, 2022.   
[36] Leo Neufcourt, Yuchen Cao, Witold Nazarewicz, and Frederi Viens, “Bayesian approach to model-based extrapolation of nuclear observables,” ´ Physical Review C, vol. 98, no. 3, pp. 034318, 2018.   
[37] Futoshi Minato, Zhongming Niu, and Haozhao Liang, “Calculation of $\beta$ -decay half-lives within a skyrme-hartree-fock-bogoliubov energy density functional with the proton-neutron quasiparticle random-phase approximation and isoscalar pairing strengths optimized by a bayesian method,” Physical Review C, vol. 106, no. 2, pp. 024306, 2022.   
[38] PE Hodgeson and E Betak, “Cluster emission, transfer and capture in nuclear reaction,” Physics Reports, vol. 374, no. 1, pp. 1–89, 2003.   
[39] AN Andreyev, Mark Huyse, Piet Van Duppen, Chong Qi, Roberto J Liotta, S Antalic, D Ackermann, S Franchoo, FP Heßberger, S Hofmann, et al., “Signatures of the $\mathbf { z } _ { \mathrm { i } } \mathrm { ? }$ format? $\gamma _ { i } { = } _ { \dot { 1 } } ?$ format?¿ 82 shell closure in $_ \alpha$ -decay process,” Physical review letters, vol. 110, no. 24, pp. 242502, 2013.   
[40] Daming Deng, Zhongzhou Ren, Dongdong Ni, and Yibin Qian, “Realistic $_ \alpha$ preformation factors of odd-a and odd-odd nuclei within the cluster-formation model,” Journal of Physics G: Nuclear and Particle Physics, vol. 42, no. 7, pp. 075106, 2015.   
[41] Saad M Saleh Ahmed, Redzuwan Yahaya, and Shahidan Radiman, “Clusterization probability in alpha-decay 212po nucleus within cluster-formation model; a new approach,” Romanian Reports in Physics, vol. 65, no. 4, pp. 1281–1300, 2013.   
[42] Saad M Saleh Ahmed, “Alpha-cluster preformation factor within cluster-formation model for odd-a and odd–odd heavy nuclei,” Nuclear Physics A, vol. 962, pp. 103–121, 2017.   
[43] Dongdong Ni and Zhongzhou Ren, “Systematic calculation of $_ \alpha$ decay within a generalized density-dependent cluster model,” Physical Review C—Nuclear Physics, vol. 81, no. 2, pp. 024315, 2010.   
[44] M Hassanzad and ON Ghodsi, “Theoretical study on favored alpha-decay half-lives of deformed nuclei,” arXiv preprint arXiv:2109.13681, 2021.   
[45] KP Santhosh and Tinu Ann Jose, “Cluster decay half-lives using modified generalized liquid drop model (mgldm) with different pre-formation factors,” Indian Journal of Physics, vol. 95, no. 1, pp. 121–131, 2021.   
[46] Dorin N Poenaru and Walter Greiner, “Cluster preformation as barrier penetrability,” Physica Scripta, vol. 44, no. 5, pp. 427, 1991.   
[47] DN Poenaru, Y Nagame, RA Gherghescu, and W Greiner, “Systematics of cluster decay modes,” Physical Review C, vol. 65, no. 5, pp. 054308, 2002.   
[48] DN Poenaru, RA Gherghescu, and W Greiner, “Single universal curve for cluster radioactivities and $_ \alpha$ decay,” Physical Review C—Nuclear Physics, vol. 83, no. 1, pp. 014601, 2011.   
[49] F Saidi, MR Oudih, M Fellah, and NH Allal, “Cluster decay investigation within a modified woods–saxon potential,” Modern Physics Letters A, vol. 30, no. 30, pp. 1550150, 2015.   
[50] JM Dong, HF Zhang, JQ Li, and W Scheid, “Cluster preformation in heavy nuclei and radioactivity half-lives,” The European Physical Journal A, vol. 41, no. 2, pp. 197–204, 2009.   
[51] J Błocki, J Randrup, WJ Swiatecki, and CF Tsang, “Proximity forces,” ´ Annals of Physics, vol. 105, no. 2, pp. 427–462, 1977.   
[52] W. D. Myers and W. J. Swiatecki, “Anomalies in nuclear masses,” Ark. Fys., vol. 36, pp. 343–352, 1967.   
[53] James J Morehead, “Asymptotics of radial wave equations,” Journal of Mathematical Physics, vol. 36, no. 10, pp. 5431–5452, 1995.   
[54] Xiao Liu, Jie-Dong Jiang, Lin-Jing Qi, Yang-Yang Xu, Xi-Jun Wu, and Xiao-Hua Li, “Systematic calculations of cluster radioactivity half-lives with a screened electrostatic barrier,” Chinese Physics C, vol. 47, no. 9, pp. 094103, 2023.   
[55] Saad M Saleh Ahmed, Redzuwan Yahaya, Shahidan Radiman, and Muhamad Samudi Yasir, “Alpha-cluster preformation factors in alpha decay for even–even heavy nuclei using the cluster-formation model,” Journal of Physics G: Nuclear and Particle Physics, vol. 40, no. 6, pp. 065105, 2013.   
[56] N Teruya, SB Duarte, and MMN Rodrigues, “Nonlocality effect in the tunneling of one-proton radioactivity,” Physical Review C, vol. 93, no. 2, pp. 024606, 2016.   
[57] MI Jaghoub, MF Hassan, and GH Rawitscher, “Novel source of nonlocality in the optical model,” Physical Review C—Nuclear Physics, vol. 84, no. 3, pp. 034618, 2011.   
[58] RA Zureikat and MI Jaghoub, “Surface and volume term nonlocalities in the proton–nucleus elastic scattering process,” Nuclear Physics A, vol. 916, pp. 183–209, 2013.   
[59] Sajedah Alameer, MI Jaghoub, and I Ghabar, “Nucleon-nucleus velocity-dependent optical model: revisited,” Journal of Physics G: Nuclear and Particle Physics, vol. 49, no. 1, pp. 015106, 2021.   
[60] Chong Qi, Doru S Delion, Roberto J Liotta, and Ramon Wyss, “Effects of formation properties in one-proton radioactivity,” Physical Review C—Nuclear Physics, vol. 85, no. 1, pp. 011303, 2012.

[61] Radford M Neal, Bayesian learning for neural networks, vol. 118, Springer Science & Business Media, 2012.   
[62] Peter Moller, J Rayford Nix, WD Myers, and WJ Swiatecki, “Nuclear ground-state masses and deformations,” ¨ arXiv preprint nucl-th/9308022, 1993.   
[63] ZM Niu and HZ Liang, “Nuclear mass predictions based on bayesian neural network approach with pairing and shell effects,” Physics Letters B, vol. 778, pp. 48–53, 2018.   
[64] Bakhouya Mostafa, Ramchoun Hassan, Hadda Mohammed, and Masrour Tawfik, “A review of variational inference for bayesian neural network,” in International conference on artificial intelligence & industrial applications. Springer, 2023, pp. 231–243.   
[65] Solomon Kullback and Richard A Leibler, “On information and sufficiency,” The annals of mathematical statistics, vol. 22, no. 1, pp. 79–86, 1951.   
[66] Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra, “Weight uncertainty in neural network,” in International conference on machine learning. PMLR, 2015, pp. 1613–1622.   
[67] Ning Wang, Min Liu, Xizhen Wu, and Jie Meng, “Surface diffuseness correction in global mass formula,” Physics Letters B, vol. 734, pp. 215–219, 2014.   
[68] XW Xia, Y Lim, PW Zhao, HZ Liang, XY Qu, Y Chen, H Liu, LF Zhang, SQ Zhang, Y Kim, et al., “The limits of the nuclear landscape explored by the relativistic continuum hartree–bogoliubov theory,” Atomic Data and Nuclear Data Tables, vol. 121, pp. 1–215, 2018.   
[69] P Moller, Arnold John Sierk, Takatoshi Ichikawa, and Hiroyuki Sagawa, “Nuclear ground-state masses and deformations: Frdm (2012),” ¨ Atomic Data and Nuclear Data Tables, vol. 109, pp. 1–204, 2016.   
[70] Hong-Qiang You, Ren-Hang Wu, Hao-Ze Su, Jing-Jing Li, Hai-Qian Zhang, and Xiao-Tao He, “Calculating $_ \alpha$ -decay half-lives with artificial neural networks considering the effects of angular momentum and deformation,” Physical Review C, vol. 110, no. 2, pp. 024319, 2024.   
[71] Hans Geiger and JM Nuttall, “Lvii. the ranges of the $_ \alpha$ particles from various radioactive substances and a relation between range and period of transformation,” The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, vol. 22, no. 130, pp. 613–621, 1911.   
[72] Hans Geiger, “Reichweitemessungen an $_ \alpha$ -strahlen,” Zeitschrift fur Physik ¨ , vol. 8, no. 1, pp. 45–57, 1922.