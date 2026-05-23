# $\alpha$ -decay systematics for superheavy nucleus: The effect of deformation of daughter nucleus

Jinyu $\mathrm { H u } ^ { 1 }$ and Chen Wu1

1. Xingzhi College, Zhejiang Normal University, Jinhua, 321004, Zhejiang, China

Recently, V. Yu. Denisov [1] introduced quadrupole deformation into the empirical formula for calculating $\alpha$ -decay half-lives, leading to a significant improvement in accuracy for even-even nuclei. In this work, we extend this approach by incorporating hexadecapole and hexacontatetrapole deformations into three empirical models: the formula proposed by Deng et al. (DUR) [2], the formula modified by AKrawy and Poenaru to include nuclear isospin (AKRA) [3], and the improved New Geiger-Nuttall law (NGN) by Y. Ren and Z. Ren [4]. Using these deformation-enhanced versions-denoted as $\mathrm { D U R + D }$ , AKRA+D, and $\mathrm { N G N + D }$ -along with their original forms, we calculated the $\alpha$ -decay half-lives of 400 isotopes. The results show that AKRA+D achieves the best agreement with experimental data. As an application, we employed $\mathrm { D U R + D }$ , AKRA+D, the extended formula by Xu et al. for odd-A nuclei (Improved $+ \mathrm { U L }$ ) [5] and odd-odd nuclei (Improved+EF) [6]-which account for centrifugal potential, shell effects, and the blocking effect of unpaired nucleons-as well as V. Yu. Denisov’s deformation-based empirical formula (ND), to predict $\alpha$ -decay properties of 71 even-even nuclei with $Z = 1 1 8$ , 120, 122, and 124. Predictions from all five models are in strong agreement, confirming the reliability of our approach and providing valuable guidance for future experiments aimed at synthesizing new elements.

# I. INTRODUCTION

Since Ernest Rutherford first described $\alpha$ -decay in 1908 as the emission of a $^ 4 \mathrm { H e }$ nucleus from a parent nucleus, it has remained a major research topic in nuclear physics. As the dominant decay mode for superheavy nuclei, $\alpha$ -decay provides rich information on nuclear structure-including nuclear spins, shell effects, ground-state energies, and half-lives. Moreover, with progress in experimental detection techniques, $\alpha$ -decay chains serve as an important tool for identifying new elements and isotopes. In summary, $\alpha$ -decay continues to be a central and active research area in nuclear physics [7–17].

In 1911, Geiger and Nuttall [18] first introduced an empirical formula to describe alpha decay. This formula suggests that the logarithm of the half-life of alpha decay is linearly correlated with the negative square root of the alpha decay energy. This empirical relationship is known as the Geiger-Nuttall law. It was written as:

$$
\log_ {1 0} T _ {1 / 2} (s) = a + b Q _ {\alpha} ^ {- 1 / 2}. \tag {1}
$$

Subsequently, Gamow and, independently, Condon and Gurney interpreted $\alpha$ -decay in terms of quantum tunneling, in agreement with the Geiger-Nuttall law. This development motivated a broad range of models for evaluating $\alpha$ -decay halflives, including the Gamow-like model [8], the modified generalized liquid-drop model [19, 20], the Coulomb and proximity potential model [21, 22], the two-potential approach (TPA) [23], and double-folding potential methods [24], among others [25, 26]. Despite substantial progress, a unified framework capable of describing $\alpha$ -decay and providing quantitatively reliable half-life predictions over the full nuclear chart is still lacking. Both the Geiger-Nuttall law and modern theoretical approaches indicate that $\alpha$ -decay half-lives are strongly influenced by multiple nuclear-structure and barrier characteristics, which contributes to the persistent challenge of achieving high predictive accuracy.

A variety of improved empirical formulas for describing α- decay have been developed on the basis of the Geiger-Nuttall law. Early efforts focused on incorporating the mass number $A$ , proton number $Z$ , and different functional forms of the

$\alpha$ -decay energy $( Q _ { \alpha } )$ , leading to widely used relations such as the Royer formula [27], the Viola-Seaborg-Sobiczewski formula [28], and the universal decay law (UDL) [29]. To provide a more accurate description of $\alpha$ -decay, later empirical formulations explicitly included the spin and parity of the ground states of both the parent and daughter nuclei, which notably improved the predicted half-lives of odd-A and oddodd systems [4, 30]. Numerous spin-parity-dependent empirical models have since been proposed [31–33]. More recently, additional refinements have been achieved by incorporating proton-neutron antisymmetry [3, 15, 34, 35]. In particular, Akrawy and collaborators [34] systematically demonstrated that the inclusion of proton-neutron antisymmetry significantly enhances the predictive accuracy of empirical $\alpha$ - decay half-life formulas. Overall, the incorporation of spinparity effects and proton-neutron antisymmetry has substantially improved the performance of empirical models for $\alpha$ - decay half-life calculations.

Despite decades of development that have substantially improved the performance of empirical formulas for describing $\alpha$ -decay, these approaches still exhibit notable limitations when compared with semi-classical WKB-based theoretical frameworks. For instance, although many theoretical models explicitly account for deformation effects of the daughter nucleus during $\alpha$ emission [36–39], most empirical formulas neglect such contributions. A significant advancement was achieved in 2024 by V. Yu. Denisov [1], who incorporated quadrupole deformation into an empirical $\alpha$ -decay formula and systematically compared deformation parameters obtained from three mass models (FRDM, HFB, and WS4 [40]) with those from spherical approximations. This modification reduced the root-mean-square deviation of the calculated decimal logarithms of $\alpha$ -decay half-lives by approximately $23 \%$ . Motivated by Denisov’s results-which demonstrate that an accurate treatment of nuclear quadrupole deformation significantly enhances half-life predictions-we extend this approach by including hexadecapole and hexacontatetrapole deformations in the empirical framework. Incorporating these higher-order shape degrees of freedom enables a more realistic description of nuclear deformation and further

reduces the discrepancy between calculated and experimental $\alpha$ -decay half-lives.

Research on superheavy elements has recently attracted considerable attention [41–45]. For example, Manjunatha et al. [43] showed that $\alpha$ -decay is the dominant decay mode for the isotopic chain of superheavy nuclei with $Z = 1 2 2$ . In addition, both quadrupole and hexadecapole deformations are known to play important roles in heavy-ion fusion processes [44, 45]. In this work, building upon the deformationdependent empirical formulation proposed by V. Yu. Denisov, we extend his approach to several additional empirical models. Specifically, we employ three empirical formulas. First, Yuejiao Ren and Zhongzhou Ren incorporated quantum numbers and the centrifugal potential into the Geiger-Nuttall law, yielding an improved expression known as the NGN formula. Second, D. T. Akrawy and D. N. Poenaru introduced isospin dependence into the Royer formula, resulting in the AKRA relation. Third, Jun-Gang Deng, Hong-Fei Zhang, and G. Royer incorporated the centrifugal potential into the Royer expression, producing the refined DUR model.We apply these three original formulas, together with their deformation-extended versions $( \mathrm { D U R + D }$ , AKRA+D, and $\mathrm { N G N + D } ,$ ), to analyze the $\alpha$ -decay half-lives of 400 selected nuclei. These nuclei are further classified into four categories even-even, even-odd, odd-even, and odd-odd for detailed examination. Importantly, we incorporate both hexadecapole and hexacontatetrapole deformations of the daughter nucleus into the empirical models to investigate how higher-order shape effects improve the predictive accuracy of $\alpha$ -decay half-lives. For comparative purposes, we further employ the $\mathrm { D U R + D }$ and AKRA+D models, the extended formulas proposed by Xu et al. for odd-A (Improved+UL) and odd-odd (Improved+EF) nuclei-which include centrifugal potential, shell corrections, and blocking effects of unpaired nucleons-as well as Denisov’s deformationbased empirical expression $\left( \mathrm { N + D } \right)$ , to calculate the $\alpha$ -decay half-lives of 71 even-even nuclei with $1 1 8 \leq Z \leq 1 2 4$ , and subsequently compare their predictive performance.

This work is organized as follows. In Sec. III, we apply these three original models and their improved model (the $\mathrm { D U R + D }$ model, the $\mathbf { A K R A + D }$ model, and the $\mathrm { N G N + D }$ model) to evaluate the alpha-decay half-lives for each isotope and compare the results with experimental values. The application of the DUR+D model, the AKRA+D model has been extended to 71 even-even nuclei with $Z = 1 1 8$ to $Z = 1 2 4$ ; the result was shown in figures for each set of isotopes. In Sec. IV, we present our conclusions.

# II. FORMALISM OF $\alpha$ -DECAY HALF-LIVES

Recently, V. Yu. Denisov [1] proposed a new empirical formula by introducing the deformation of the daughter nucleus. The new empirical relation is given as

$$
\begin{array}{l} \log_ {1 0} T _ {1 / 2} (s) = a \frac {Z}{Q ^ {1 / 2}} - b \left(\frac {A Q ^ {1 / 2}}{Z}\right) ^ {1 / 6} - c A ^ {1 / 6} Z ^ {1 / 2} \tag {2} \\ + d A ^ {1 / 6} \frac {\sqrt {l (l + 1)}}{Q} - e (k \beta) ^ {1 / 2} \frac {Z}{Q ^ {1 / 2}}, \\ \end{array}
$$

where the half-life is given in seconds, the $\alpha$ decay energy $( Q )$ in MeV, A is the mass number of parent nucleus, $\textsf { Z }$ i s the proton number of parent nucleus, and $\beta$ is the quadrupole deformation parameter of the deformed daughter nucleus.

V.Yu.Denisov’s study introduces a fifth term in the $\alpha$ -decay half-life calculation, which accounts for the influence of the daughter nucleus’s deformation on the Coulomb interaction between the emitted $\alpha$ -particle and the daughter nucleus. This effect is crucial because the half-life is significantly influenced by the daughter nucleus’s deformation. Denisov defines the effect of daughter nucleus deformation on the $\alpha$ -decay halflife based on the minimum value of the Coulomb interaction, $V _ { C } ^ { m i n }$ . This minimum value is expressed as:

$$
V _ {C} ^ {\min } = 2 (Z - 2) e _ {p} ^ {2} / \left(R _ {L} + R _ {\alpha}\right), \tag {3}
$$

where $Z$ is the proton number of the parent nucleus, $e _ { p }$ is the proton charge, $R _ { \alpha }$ is the radius of the $\alpha$ -particle, and $R _ { L }$ is the largest radius of the deformed daughter nucleus.

The most critical parameter governing the Coulomb interaction is the maximum value of the daughter nucleus’s quadrupole deformation parameter, $\beta$ . The surface radius of the deformed daughter nucleus, $R ( \theta )$ , is typically modeled by the expression $R ( \theta ) = R _ { 0 } [ 1 + \beta Y _ { 2 0 } ( \theta ) ]$ , where $R _ { 0 }$ is the radius of the corresponding spherical daughter nucleus. The value of $R _ { L }$ depends on the sign of the deformation parameter $\beta$ : For prolate deformation $( \beta > 0 )$ : The largest radius occurs at $\theta = 0$ (the poles), and is given by $R _ { L } = R _ { 0 } ( 1 + \sqrt { 5 / \pi } \beta / 2 )$ .For oblate deformation $( \beta < 0 )$ : The largest radius occurs at $\theta = \pi / 2$ (the equator), and is given by $R _ { L } = R _ { 0 } ( 1 + \sqrt { 5 / \pi } \beta / 4 )$ . The reduction in the $\alpha$ -decay halflife caused by the daughter nucleus’s deformation is quantified by subtracting the Coulomb interaction of the spherical nucleus from the minimum Coulomb interaction $( V _ { C } ^ { m i n } )$ induced by the deformation. In summary, V. Yu. Denisov’s analysis demonstrates that the reduction in the $\alpha$ -decay halflife attributed to daughter nucleus deformation is proportional to the difference between the largest deformed radius and the spherical radius $( \Delta \propto R _ { L } - R _ { 0 } )$ .

V. Yu. Denisov’s research established that the alteration in the $\alpha$ -decay half-life due to daughter nucleus deformation can be characterized by changes in the Coulomb interaction between the $\alpha$ -particle and the daughter nucleus. However, Denisov’s original formulation considered only quadrupole deformation $( \beta _ { 2 } )$ .In this work, we extend this framework by incorporating hexadecapole $( \beta _ { 4 } )$ and hexacontatetrapole $( \beta _ { 6 } )$ deformations of the daughter nucleus. The minimum value of the Coulomb interaction, $V _ { C } ^ { m i n }$ , remains defined based on the maximum distance: $V _ { C } ^ { m i n } = \stackrel { \textstyle - } { 2 } ( Z - 2 ) e _ { p } ^ { 2 } / ( R _ { L } + R _ { \alpha } )$ . With the inclusion of higher-order terms, the radius of the deformed daughter nucleus, $R$ , is given by:

$$
R (\theta) = R _ {0} \left(1 + \beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta) + \beta_ {6} Y _ {6 0} (\theta)\right),
$$

where $R _ { 0 }$ is the radius of the spherical daughter nucleus and $Y _ { l 0 } ( \theta )$ are spherical harmonics.To comprehensively describe the characteristics of the deformed daughter nucleus relevant to the $\alpha$ -particle’s tunneling probability, it is essential to consider the maximum value of its radius, $R _ { L }$ . This maximum

![](images/30a0d0fd7ac1f777b8045c954f5b8f934dc0446628c6d4632f622a00e2a98a2a.jpg)

![](images/bc10e44068628b7ce6a2930595bb41ec236e805723f5232a3fa6f239615a1c3a.jpg)

![](images/10d880cd832904a15aff8b8b7c9dd952db0a8d5856d6448fc75221fc5a67d277.jpg)

![](images/9c0af60cb99404d2d2a1326eba7271e41f38728d59359f5c5a62354d5c74c4b9.jpg)  
FIG. 1. Calculations of $\alpha$ decay half-lives for even-even nuclei, even-odd nuclei, odd-even nuclei and odd-odd nuclei. The experimental $\alpha$ decay half-lives are take from the latest evaluated nuclear properties table NUBASE2020 [46]. The logarithmic differences between calculated and experimental $\alpha$ -decay half-lives for the $\alpha$ -decay for even-even, even-odd, odd-even, odd-odd nuclei. The calculations are done for the values of the quadrupole, the hexadecapole and the hexacontatetrapole deformation parameters taken from Ref. [40]. The values of $\alpha$ -decay half-lives are given in seconds.

TABLE I. The coefficient of the DUR model (DUR).   

<table><tr><td>Set</td><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>Even-even</td><td>-25.62</td><td>-1.16</td><td>1.60</td><td>-</td></tr><tr><td>Even-odd</td><td>-27.1458</td><td>-1.15</td><td>1.64</td><td>0.045</td></tr><tr><td>Odd-even</td><td>-27.6654</td><td>-1.09</td><td>1.61</td><td>0.054</td></tr><tr><td>Odd-odd</td><td>-24.9491</td><td>-1.22</td><td>1.62</td><td>0.053</td></tr></table>

radius is determined by finding the largest positive contribution from the deformation terms:

$$
R _ {L} = R _ {0} \left(1 + \left| M a x \left(\beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta) + \beta_ {6} Y _ {6 0} (\theta)\right) \right|\right). \tag {4}
$$

Since this deformation primarily influences the Coulomb interaction, which is a key factor in the $\alpha$ -decay barrier height, we deduce a new deformation term for empirical half-life formulas. Based on an analysis informed by the Royer formula (which relates half-life to the Coulomb barrier height and $\alpha$ - decay energy, $Q$ ), the deformation term incorporated into the

empirical half-life calculation is expressed as:

$$
e \left(\left| M a x \left(\beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta) + \beta_ {6} Y _ {6 0} (\theta)\right) \right|\right) ^ {1 / 2} \frac {Z}{Q ^ {1 / 2}}. \tag {5}
$$

We incorporated this new deformation term (Eq. 5) into three established empirical formulas: the DUR model, the AKRA model, and the NGN model. This modification yields the improved versions: $\mathrm { D U R + D }$ , AKRA+D, and $\mathrm { N G N + D } . S$ ubsequently, we used both the original and the modified versions (a total of six empirical formulas) to calculate the $\alpha$ -decay half-lives for a selected dataset of 400 nu-

TABLE II. The coefficient of the $\mathrm { D U R + D }$ model $( \mathrm { D U R + D } )$ ).   

<table><tr><td>Set</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr><tr><td>Even-even</td><td>-27.12</td><td>-1.13</td><td>1.64</td><td>-</td><td>-0.035</td></tr><tr><td>Even-odd</td><td>-28.70</td><td>-1.12</td><td>1.68</td><td>0.044</td><td>-0.026</td></tr><tr><td>Odd-even</td><td>-28.53</td><td>-1.07</td><td>1.63</td><td>0.051</td><td>-0.022</td></tr><tr><td>Odd-odd</td><td>-26.11</td><td>-1.16</td><td>1.65</td><td>0.048</td><td>-0.055</td></tr></table>

TABLE III. The coefficient of the AKRA model (AKRA).   

<table><tr><td>Set</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr><tr><td>Even-even</td><td>-26.99</td><td>-1.13</td><td>1.61</td><td>5.88</td><td>-27.02</td></tr><tr><td>Even-odd</td><td>-16.57</td><td>-1.34</td><td>1.44</td><td>-6.98</td><td>85.06</td></tr><tr><td>Odd-even</td><td>-21.62</td><td>-1.24</td><td>1.53</td><td>8.87</td><td>-1.36</td></tr><tr><td>Odd-odd</td><td>-14.52</td><td>-1.33</td><td>1.39</td><td>-5.45</td><td>64.32</td></tr></table>

clei. The necessary parameter fitting and curve fitting analysis were performed using the dedicated modules within the Python 3.11 programming language environment.

Prior to presenting our analysis, it is essential to briefly review the six phenomenological models that underpin this study.

# A. The DUR model(DUR)

In 2020, Deng et al. [2] presented an unitary Royer formula(DUR) for $\alpha$ decay half-lives. It can be expressed as

$$
\log_ {1 0} T _ {1 / 2} = a + b A ^ {1 / 6} \sqrt {Z} + c Z / \sqrt {Q _ {\alpha}} + d l (l + 1) + h, \tag {6}
$$

where the half-life is given in seconds, and decay energy(Q) in MeV, A and $Z$ are the mass and proton numbers of parent nucleus,respectively. The optimal parameters for a, b, c,and $d$ were obtained through fitting to experimental data and are listed in Table I. The h is given by

$$
h = \left\{ \begin{array}{l l} 0, & \text {f o r e v e n - e v e n n u c l e u s ,} \\ 0. 2 8 1 2 & \text {f o r o d d Z - e v e n N n u c l e u s ,} \\ 0. 3 6 2 5 & \text {f o r e v e n Z - o d d N n u c l e u s ,} \\ 0. 7 4 8 6 & \text {f o r o d d - o d d n u c l e u s .} \end{array} \right. \tag {7}
$$

# B. The DUR+D model(DUR+D)

In the present work, we modify the DUR model by adding deformation terms,and the DUR+D model takes the form

$$
\begin{array}{l} \log_ {1 0} T _ {1 / 2} (s) = a + b A ^ {1 / 6} \sqrt {Z} + c Z / \sqrt {Q _ {\alpha}} + d l (l + 1) + h \\ + e \left(\left| M a x \left(\beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta) + \beta_ {6} Y _ {6 0} (\theta)\right) \right|\right) ^ {1 / 2} \\ \times \frac {Z}{Q ^ {1 / 2}}, \tag {8} \\ \end{array}
$$

where $\beta _ { 2 } , \beta _ { 4 }$ , and $\beta _ { 6 }$ are the quadrupole, hexadecapole and hexacontatetrapole deformation of the deformed daughter nucleus, while the optimal parameters $a , b , c , d ,$ e are the obtained fitting to experimental data and are listed in Table III.

# C. The AKRA model(AKRA)

Akrawy and Poenaru [3] reported a new relation a new relationship for the calculations of alpha decay half-lives by introducing iso-spin asymmetry, $I$ , which is based on the Royer relationship. The new semiempirical relationship is given as,

$$
\log_ {1 0} T _ {1 / 2} (s) = a + b A ^ {1 / 6} \sqrt {Z} + c \frac {Z}{\sqrt {Q}} + d I + e I ^ {2}, \tag {9}
$$

where $I$ is the asymmetry term, $\begin{array} { r } { I = \frac { N - Z } { A } } \end{array}$ . The optimal parameters for a, b, c, d, e were obtained through fitting to experimental data and are listed in Table III.

# D. the AKRA+D model (AKRA+D)

The modification of the AKRA model was also done by adding the deformation terms; The AKRA $+ \mathbf { D }$ model is given as,

$$
\begin{array}{l} \log_ {1 0} T _ {1 / 2} (s) = a + b A ^ {1 / 6} \sqrt {Z} + c \frac {Z}{\sqrt {Q}} + d I + e I ^ {2} \\ + f \left(\left| M a x \left(\beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta) + \beta_ {6} Y _ {6 0} (\theta)\right) \right|\right) ^ {1 / 2} \\ \times \frac {Z}{Q ^ {1 / 2}}, \tag {10} \\ \end{array}
$$

where $\beta _ { 2 } , \beta _ { 4 }$ , and $\beta _ { 6 }$ are the quadrupole, hexadecapole and hexacontatetrapole deformation of the deformed daughter nucleus, while the optimal parameters $a , b , c , d , e , f$ re the obtained fitting to experimental data and are listed in Table IV.

# E. The New Geiger-Nuttall law (NGN)

The New Geiger-Nuttall law formula (NGN) [4] for $\alpha$ - decay half-lives is written as

$$
\begin{array}{l} \log_ {1 0} T _ {1 / 2} (s) = a \frac {\mu Z _ {c} Z _ {d}}{\sqrt {Q}} + b \sqrt {\mu} \sqrt {Z _ {c} Z _ {d}} \tag {11} \\ + c + S + d l (l + 1). \\ \end{array}
$$

TABLE IV. The coefficient of the AKRA+D model (AKRA+D).   

<table><tr><td>Set</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td></tr><tr><td>Even-even</td><td>-29.51</td><td>-1.06</td><td>1.68</td><td>-1.21</td><td>-13.74</td><td>-0.042</td></tr><tr><td>Even-odd</td><td>-20.10</td><td>-1.26</td><td>1.54</td><td>-12.94</td><td>107.30</td><td>-0.068</td></tr><tr><td>Odd-even</td><td>-24.63</td><td>-1.13</td><td>1.60</td><td>-2.95</td><td>24.53</td><td>-0.047</td></tr><tr><td>Odd-odd</td><td>-18.94</td><td>-1.14</td><td>1.52</td><td>-22.11</td><td>104.91</td><td>-0.13</td></tr></table>

TABLE V. The coefficient of the New Geiger-Nuttall law (NGN).   

<table><tr><td>Set</td><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>Even-even</td><td>0.013</td><td>-0.043</td><td>-18.13</td><td>-</td></tr><tr><td>Even-odd</td><td>0.014</td><td>-0.041</td><td>-20.25</td><td>0.047</td></tr><tr><td>Odd-even</td><td>0.013</td><td>-0.038</td><td>-21.45</td><td>0.060</td></tr><tr><td>Odd-odd</td><td>0.013</td><td>-0.045</td><td>-16.04</td><td>0.0051</td></tr></table>

Here $Q$ is the decay energy in MeV units, $Z _ { c }$ and $Z _ { d }$ are the charge number of the $\alpha$ particle and the daughter nucleus, $S =$ 0 for $N \geq 1 2 7$ and $S = 1$ for $N \leq 1 2 6$ , and $\mu$ is reduced mass the respectively, and the optimal parameters for a, $b$ and c, d are the obtained fitting to experimental data and are listed in Table V.

# F. The New Geiger-Nuttall+D law (NGN+D)

Similarly, as we did with the DUR model, the New Geiger-Nuttall law has been modified adding the deformation terms; the New Geiger-Nuttall+D (NGN+D) will be

$$
\begin{array}{l} \log_ {1 0} T _ {1 / 2} (s) = a \frac {\mu Z _ {c} Z _ {d}}{\sqrt {Q}} + b \sqrt {\mu} \sqrt {Z _ {c} Z _ {d}} \\ + c + S + d l (l + 1) \\ + e \left(\left| M a x \left(\beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta) + \beta_ {6} Y _ {6 0} (\theta)\right) \right|\right) ^ {1 / 2} \\ \times \frac {Z}{Q ^ {1 / 2}}, \tag {12} \\ \end{array}
$$

where $\beta _ { 2 } , \beta _ { 4 }$ , and $\beta _ { 6 }$ are the quadrupole, hexadecapole and hexacontatetrapole deformation of the deformed daughter nucleus, while the optimal parameters for $a , b , c , d , e$ are the obtained fitting to experimental data and are listed in Table VI.

# III. RESULTS AND DISCUSSION

In this study, we partitioned 400 nuclei into four groups (even-even, even-odd, odd-even, and odd-odd) and employed six empirical formulas-the DUR model, the AKRA model, the New Geiger-Nuttall (NGN) formula, and their deformationextended versions $( \mathrm { D U R + D }$ , AKRA $+ \mathbf { D }$ , and $\mathrm { N G N + D } ,$ )-to calculate their $\alpha$ -decay half-lives. V. Yu. Denisov demonstrated that the WS4 deformation parameters $\beta _ { 2 }$ , $\beta _ { 4 }$ , and $\beta _ { 6 }$ yield the smallest deviations between calculated and experimental $\alpha$ -decay half-lives; thus, these deformation parameters are

adopted in the present work. To enable a comprehensive comparison of the performance of the six models, we evaluate their predictive accuracy using the root-mean-square (RMS) deviation between the calculated and measured half-lives. The (RMS) is defined as

$$
\sigma = \left\{\frac {1}{n} \sum_ {i = 1} ^ {n} \left[ \log_ {1 0} \left(T _ {\frac {1}{2}, i} ^ {\text {c a l c .}}\right) - \log_ {1 0} \left(T _ {\frac {1}{2}, i} ^ {\text {e x p t .}}\right) \right] ^ {2} \right\} ^ {1 / 2}, \tag {13}
$$

where $l o g _ { 1 0 } \big ( T _ { \frac { 1 } { 2 } , i } ^ { c a l c . } \big )$ and $l o g _ { 1 0 } \big ( T _ { \frac { 1 } { 2 } , i } ^ { e x p t . } \big )$ are the calculated and 12 ,i 12 ,i experimental $\alpha$ -decay half-lives the nucleus, and $n$ is the number of nucleus involved for each group.

The calculated RMS for each model is listed in Table VII. The results shows the superiority the $\mathbf { A K R A + D }$ model over the other five models for all the studied sets of nucleus.

Another approach to compare the performance of different models is to calculate the difference between the calculated results and experimental data for each model. This can be expressed as:

$$
\Delta T = \log_ {1 0} \left(T _ {\frac {1}{2}, i} ^ {\text {c a l c .}}\right) - \log_ {1 0} \left(T _ {\frac {1}{2}, i} ^ {\text {e x p t .}}\right). \tag {14}
$$

As shown in Table VIII, the AKRA+D model reduces the deviation between calculated and experimental $\alpha$ -decay halflives by $22 \%$ for even-even nuclei, $5 \%$ for odd-odd nuclei, $4 . 7 \%$ for odd-even nuclei, and $1 4 . 7 \%$ for another odd-odd subset. These results indicate that the AKRA+D model outperforms the other five models considered, as well as the recently proposed deformation-dependent empirical formula (ND) of V. Yu. Denisov. Figure 1 further reveals pronounced discontinuities between the calculated and experimental values for all models at the neutron shell closures $N = 1 2 6$ and $N = 1 5 2$ . The first discontinuity corresponds to the wellestablished magic number $N = 1 2 6$ , which strongly influences the preformation probability of the $\alpha$ particle. The second discontinuity provides compelling evidence supporting $N = 1 5 2$ as the next neutron magic number. Our findings are consistent with the conclusions reported by Yuejiao Ren and Zhongzhou Ren [4].

TABLE VI. The coefficient of the New Geiger-Nuttall+D law (NGN+D).   

<table><tr><td>Set</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td></tr><tr><td>Even-even</td><td>0.014</td><td>-0.043</td><td>-18.89</td><td>-</td><td>-0.016</td></tr><tr><td>Even-odd</td><td>0.0136</td><td>-0.041</td><td>-19.64</td><td>0.047</td><td>0.00902</td></tr><tr><td>Odd-even</td><td>0.0134</td><td>-0.038</td><td>-21.26</td><td>0.060</td><td>0.00416</td></tr><tr><td>Odd-odd</td><td>0.014</td><td>-0.044</td><td>-17.16</td><td>0.047</td><td>-0.042</td></tr></table>

Three principal empirical models are examined in this work. The DUR model refines the Royer formula by incorporating the Coulomb interaction and accounting for the blocking effect of unpaired nucleons. The NGN model extends the Geiger-Nuttall law by introducing a Coulomb potential together with shell-effect quantum numbers. The AKRA model further modifies the Royer formula by adding an explicit isospin dependence. In heavy and superheavy nuclei, both deformation and isospin effects become significantly enhanced, indicating a potential synergistic relationship between them. Moreover, the work of V. Yu. Denisov shows that, for even-even nuclei, a precise treatment of nuclear spin-parity properties can markedly improve deformation-dependent empirical formulations. These findings together suggest that empirical formulas incorporating both nuclear deformation and spin-parity effects are better suited for accurately reproducing $\alpha$ -decay half-lives. Among the deformation-extended models considered here, only the AKRA+D formulation simultaneously includes nuclear deformation and spin-parity effects, whereas $\mathrm { D U R + D }$ and $\mathrm { N G N + D }$ consistent with the observations of Denisov include only the quantum-number contributions associated with unpaired-nucleon blocking and shell effects, respectively. Our results clearly indicate that, for heavy and superheavy nuclei, isospin plays a more critical role than the other factors. We also plot the resulting ∆T values as a function of mass number for even-even, even-odd, odd-even, and odd-odd nuclei (Fig. 1). The superiority of the AKRA+D model is evident: its deviations are systematically smaller and exhibit smoother behavior across the entire nuclear chart. In particular, the deviation patterns for odd-A systems shown in Fig. 1 demonstrate that incorporating both nuclear asymmetry and daughter-nucleus deformation yields predictions in excellent agreement with experimental data.

The strong correlation between Coulomb barrier parameters and different orders of nuclear deformation, as reported by Ismail et al. [47], aligns well with the foundational research by V. Yu. Denisov [1]. Denisov initially quantified the influence of daughter nucleus deformation on the Coulomb energy of the $\alpha$ -daughter system by considering the quadrupole deformation $( \beta _ { 2 } )$ . He proposed using the difference between the maximum radius of the deformed nucleus $( R _ { L } )$ and the radius of the corresponding spherical nucleus $( R _ { 0 } )$ as a measure of this influence $( \propto R _ { L } - R _ { 0 } )$ . Building upon this, our work focuses on the three dominant deformation parameters: quadrupole $( \beta _ { 2 } )$ , hexadecapole $( \beta _ { 4 } )$ , and hexacontatetrapole $( \beta _ { 6 } )$ . This selection is justified by the understanding that the influence of higher-order deformations (beyond $\beta _ { 6 }$ ) is typically suppressed by the larger $\beta _ { 2 }$ and $\beta _ { 4 }$ values. Crucially, studies have confirmed the importance of these

higher-order terms: The work of M. Ismail et al. [47] specifically indicates that the hexacontatetrapole deformation $( \beta _ { 6 } )$ directly influences the Coulomb barrier height, causing variations on the order of 1 MeV. Qiong Xiao et al. [48] supported the inclusion of deformation factors in semi-classical formulas by demonstrating that incorporating $\beta _ { 2 }$ , $\beta _ { 4 }$ , and $\beta _ { 6 }$ into the square well radius, $R _ { i n } ( \theta )$ , results in a higher tunneling potential peak for deformed nuclei. Furthermore, the research by Narayanaswamy Manjunatha et al. [44] on fusion reactions suggests that $\beta _ { 2 }$ enhances the reaction cross-section between helium and uranium, whereas $\beta _ { 4 }$ reduces it. This differential effect strongly suggests that higher-order multipole deformations significantly influence the preformation probability of the $\alpha$ -particle within the parent nucleus. Given this compelling evidence, we enhance three established empirical $\alpha$ -decay models (AKRA, DUR, and NGN) by incorporating a unified deformation term that accounts for $\beta _ { 2 }$ , $\beta _ { 4 }$ , and $\beta _ { 6 }$ . This approach aims to accurately describe the complex interplay between nuclear shape and the $\alpha$ -decay probability.

For a comprehensive comparative analysis, we employed five empirical models to predict the $\alpha$ -decay half-lives of 71 even-even nuclei spanning Z = 118,120,122, and 124. The models used were the AKRA+D model, the $\mathrm { D U R + D }$ model, the extended formula by Xu et al. for odd-A nuclei (Improved+UL) and odd-odd nuclei (Improved+EF)-which account for centrifugal potential, shell effects, and the blocking effect of unpaired nucleons-as well as V. Yu. Denisov’s deformation-based empirical formula (ND). To ensure consistency in the predictions, the essential input parameters-the $\alpha$ -decay energy $( Q _ { \alpha } )$ and the quadrupole $( \beta _ { 2 } )$ deformation parameters of the daughter nuclei-were systematically obtained from the WS4 mass table [40]. The complete set of prediction results is summarized in Figure 2, which visually illustrates the computational outcomes of each model. The predictions generated by the AKRA+D and $\mathrm { D U R + D }$ models demonstrate substantial agreement with those from the ND model, the Improved+UL model, and the Improved+EF model across the studied isotopic chains. A notable observation is the slight upward deviation exhibited by the predictions of the AKRA+D and $\mathrm { D U R + D }$ models compared to the ND model as the neutron number $( N )$ increases. This divergence can be directly attributed to the fundamental difference in model formulation: the AKRA+D and $\mathrm { D U R + D }$ models explicitly incorporate the contributions from hexadecapole $( \beta _ { 4 } )$ and hexacontatetrapole $( \beta _ { 6 } )$ deformations, which are not accounted for in the ND model. Furthermore, the predicted $\alpha$ -decay half-lives for the 71 even-even nuclei show distinct and consistent behavior at the parent neutron numbers $N = 1 8 0$ and $N = 1 8 6$ . This systematic change suggests that the daughter neutron numbers

corresponding to $N _ { d a u g h t e r } = 1 7 8$ and $N _ { d a u g h t e r } = 1 8 4$ may indicate the presence of a neutron magic number and a neutron submagic number, respectively, influencing the nuclear structure and decay dynamics of the superheavy region.

In this study, we successfully extended the approach pioneered by V. Yu. Denisov by incorporating hexadecapole $( \beta _ { 4 } )$ and hexacontatetrapole $( \beta _ { 6 } )$ deformations into three classical semi-empirical formulas for $\alpha$ -decay half-life calculations. Among the resulting modified models $( \mathbf { A K R A + D }$ , $\mathrm { D U R + D }$ , NGN+D), the $\mathbf { A K R A + D }$ model demonstrated the best overall performance in predicting $\alpha$ -decay half-lives. Despite its superior predictive power, the AKRA+D model, in its current form, presents two significant limitations that warrant further investigation: The model successfully accounts for the changes in the Coulomb interaction that arise from the deformation of the daughter nucleus. However, it does not include the corresponding changes in the $\alpha$ -decay energy $( Q _ { \alpha } )$ that are inherently caused by the same nuclear deformation. A comprehensive approach should ideally couple the deformation-induced changes in both the Coulomb barrier and the nuclear mass (which determines $Q \alpha$ ) for maximum accuracy. While higher-order deformations $\beta _ { 4 }$ and $\beta _ { 6 , }$ ) have been formally included in the model’s structure, the available deformation parameters for nuclei remain insufficiently accurate or refined. This uncertainty in the input deformation parameters ultimately limits the ability of the AKRA+D model to fully and precisely describe the complex $\alpha$ -decay behavior, particularly in the region of superheavy nuclei.Future work should focus on developing models that internally link the deformation effects on both the Coulomb barrier and the $\alpha$ -decay $Q$ value, while also leveraging or generating more precise deformation parameters.

# IV. SUMMARY AND CONCLUSION

Building upon the foundational work of V. Yu. Denisov, a new empirical formula incorporating deformation terms (ND) was proposed. We generalized these deformation terms to three classical semi-empirical frameworks: the DUR model, the AKRA model, and the New Geiger-Nuttall law (NGN), leading to the modified models: DUR+D, AKRA+D, and $\mathrm { N G N + D }$ . These six empirical formulas (the three original and three modified versions) were systematically employed to investigate the $\alpha$ -decay half-lives of a comprehensive set of 400 nuclei, spanning all four parity types (even-even, even-odd, odd-even, and odd-odd). The model performance was quantitatively assessed using the root-mean-square (RMS) deviation between the calculated and experimental $\alpha$ -decay halflives. As illustrated in Figure 1, among the six models tested,

the modified AKRA model (AKRA+D) consistently demonstrated the closest agreement with experimental results, indicating its superior predictive capability across the diverse nuclear dataset. The specific reduction in the RMS deviation achieved by the AKRA+D model compared to its original counterpart is detailed in Table VIII: The discrepancy between calculated and experimental $\alpha$ -decay half-lives was reduced by $22 \%$ in the even-even Nuclei. The discrepancy was reduced by $5 \%$ in odd-odd Nuclei. The discrepancy was reduced by $4 . 7 \%$ in the odd-even nuclei. The discrepancy was reduced by $1 4 . 7 \%$ in odd-odd nuclei. These results emphatically confirm that the inclusion of deformation terms, particularly within the AKRA framework, significantly enhances the accuracy of $\alpha$ -decay half-life predictions across various nuclear types.

To further validate the improvements achieved by incorporating higher-order deformation, we employed a set of five advanced empirical formulas to predict the $\alpha$ -decay half-lives of 71 even-even nuclei spanning the superheavy elements $Z = 1 1 8 , 1 2 0 , 1 2 2$ , and 124.The models used for this predictive study include the deformation-incorporated models developed in this work (the $\mathrm { D U R + D }$ model and the AKRA+D model), the new deformation formula by Denisov (ND), and two extended formulas by Xu et al. [5, 6], which account for centrifugal potential, shell effects, and the blocking effect of unpaired nucleons: Improved $+ \mathrm { U L }$ (originally for odd-A nuclei) and Improved+EF (originally for odd-odd nuclei). As demonstrated in Figure 2, a strong consistency is observed among the predictions from these five models. Crucially, the predicted $\alpha$ -decay half-lives for the 71 even-even nuclei exhibit distinct and consistent behavior at the parent neutron numbers $N = 1 8 0$ and $N = 1 8 6$ . This systematic stability change suggests that the corresponding daughter nucleus neutron numbers, $N = 1 7 8$ and $N = 1 8 4$ , may correspond to a neutron magic number and a neutron submagic number, respectively, providing critical insight into the nuclear structure in the superheavy region. A key finding is the divergence of predictions at larger neutron numbers: for $N > 1 9 0$ , the half-life predictions from the $\mathrm { D U R + D }$ model and the $\mathbf { A K R A + D }$ model consistently exceed those of the ND formula.This increasing divergence is directly attributed to the inclusion of hexadecapole $( \beta _ { 4 } )$ and hexacontatetrapole $( \beta _ { 6 } )$ deformation contributions in the $\mathrm { D U R + D }$ and AKRA+D models, terms which are not considered in the ND model. This result strongly validates the conclusion that incorporating these higher-order daughter nucleus deformation terms into empirical formulas significantly enhances the accuracy and physical reliability of $\alpha$ - decay half-life calculations, particularly for highly deformed even-even nuclei.

[1] V. Y. Denisov, Empirical relations for $\alpha$ -decay half-lives: The effect of deformation of daughter nuclei, Physical Review C 110, 014604 (2024).   
[2] J.-G. Deng, H.-F. Zhang, and G. Royer, Improved empirical for-

mula for $\alpha$ -decay half-lives, Physical Review C 101, 034307 (2020).   
[3] D. T. Akrawy and D. Poenaru, Alpha decay calculations with a new formula, Journal of Physics G: Nuclear and Particle

Physics 44, 105105 (2017).   
[4] Y. Ren and Z. Ren, New geiger-nuttall law for $\alpha$ decay of heavy nuclei, Physical Review C—Nuclear Physics 85, 044608 (2012).   
[5] Y.-Y. Xu, D.-X. Zhu, X. Chen, X.-J. Wu, B. He, and X.-H. Li, A unified formula for $\alpha$ decay half-lives, The European Physical Journal A 58, 163 (2022).   
[6] S. Luo, L.-J. Qi, D.-M. Zhang, B. He, P.-C. Chu, and X.-H. Li, An improved empirical formula of $\alpha$ decay half-lives for superheavy nuclei, The European Physical Journal A 59, 125 (2023).   
[7] W. Qu, G. Zhang, H. Zhang, and R. Wolski, Comparative studies of coulomb barrier heights for nuclear models applied to sub-barrier fusion, Physical Review C 90, 064603 (2014).   
[8] A. Zdeb, M. Warda, and K. Pomorski, Half-lives for $\alpha$ and cluster radioactivity within a gamow-like model, Physical Review C—Nuclear Physics 87, 024308 (2013).   
[9] X.-D. Sun, J.-G. Deng, D. Xiang, P. Guo, and X.-H. Li, Systematic study of $\alpha$ decay half-lives of doubly odd nuclei within the two-potential approach, Physical Review C 95, 044303 (2017).   
[10] K. Santhosh, C. Nithya, H. Hassanabadi, and D. T. Akrawy, $\alpha$ - decay half-lives of superheavy nuclei from a modified generalized liquid-drop model, Physical Review C 98, 024625 (2018).   
[11] S. Hosseini, H. Hassanabadi, and D. T. Akrawy, Alpha particle preformation factor of spherical nuclei for $6 7 \leq z \leq 9 1$ , Modern Physics Letters A 34, 1950039 (2019).   
[12] Y. T. Oganessian, F. S. Abdullin, P. Bailey, D. Benker, M. Bennett, S. Dmitriev, J. G. Ezold, J. Hamilton, R. A. Henderson, M. Itkis, et al., Synthesis of a new element with atomic number $z = 1 1 7$ , Physical review letters 104, 142502 (2010).   
[13] Y. Oganessian, Heaviest nuclei from 48ca-induced reactions, Journal of Physics G: Nuclear and Particle Physics 34, R165 (2007).   
[14] S. Hosseini and H. Hassanabadi, Theoretical approaches to alpha decay half-lives of super-heavy nuclei, Chinese Physics C 41, 064101 (2017).   
[15] D. T. Akrawy and A. H. Ahmed, $\alpha$ -decay systematics for superheavy nuclei, Physical Review C 100, 044618 (2019).   
[16] E. Javadimanesh, H. Hassanabadi, A. Rajabi, H. Rahimov, and S. Zarrinkamar, Investigation of deformed nuclei with a new potential combination, Chinese Physics C 37, 114102 (2013).   
[17] P. E. Hodgson and E. Beták, Cluster emission, transfer and cap- ˇ ture in nuclear reactions, Physics reports 374, 1 (2003).   
[18] H. Geiger and J. Nuttall, Lvii. the ranges of the $\alpha$ particles from various radioactive substances and a relation between range and period of transformation, The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science 22, 613 (1911).   
[19] S. Guo, X. Bao, Y. Gao, J. Li, and H. Zhang, The nuclear deformation and the preformation factor in the $\alpha$ -decay of heavy and superheavy nuclei, Nuclear Physics A 934, 110 (2015).   
[20] H. Zhang, W. Zuo, J. Li, and G. Royer, α decay half-lives of new superheavy nuclei within a generalized liquid drop model, Physical Review C—Nuclear Physics 74, 017304 (2006).   
[21] V. Zanganah, D. T. Akrawy, H. Hassanabadi, S. Hosseini, and S. Thakur, Calculation of $\alpha$ -decay and cluster half-lives for 197–226fr using temperature-dependent proximity potential model, Nuclear Physics A 997, 121714 (2020).   
[22] W. Yahya, Alpha decay half-lives of 171-189hg isotopes using modified gamow-like model and temperature dependent proximity potential, Journal of the Nigerian Society of Physical Sciences , 250 (2020).   
[23] S. Gurvitz and G. Kalbermann, Decay width and the shift of a quasistationary state, Physical review letters 59, 262 (1987).   
[24] M. Moghaddari Amiri and O. Ghodsi, Influence of the pauli

exclusion principle on $\alpha$ decay, Physical Review C 102, 054602 (2020).   
[25] D. Jian-Min, Z. Hong-Fei, W. Yan-Zhao, Z. Wei, S. Xin-Ning, and L. Jun-Qing, $\alpha$ -decay half-lives of superheavy nuclei and general predictions, Chinese Physics C 33, 633 (2009).   
[26] W. Yan-Zhao, Z. Hong-Fei, D. Jian-Min, S. Xin-Ning, Z. Wei, and L. Jun-Qing, Branching ratios of $\alpha$ decay for nuclei near deformed shell closures, Chinese Physics Letters 26, 062101 (2009).   
[27] G. Royer, Alpha emission and spontaneous fission through quasi-molecular shapes, Journal of Physics G: Nuclear and Particle Physics 26, 1149 (2000).   
[28] V. Viola Jr and G. Seaborg, Nuclear systematics of the heavy elements—ii lifetimes for alpha, beta and spontaneous fission decay, Journal of Inorganic and Nuclear Chemistry 28, 741 (1966).   
[29] C. Qi, F. Xu, R. J. Liotta, and R. Wyss, Universal decay law in charged-particle emission and exotic cluster radioactivity, Physical review letters 103, 072501 (2009).   
[30] H. Koura, Phenomenological formula for alpha-decay halflives, Journal of nuclear science and technology 49, 816 (2012).   
[31] G. Saxena, A. Jain, and P. Sharma, A new empirical formula for $\alpha$ -decay half-life and decay chains of ${ \bf z } = 1 2 0$ isotopes, Physica Scripta 96, 125304 (2021).   
[32] A. Soylu and C. Qi, Extended universal decay law formula for the $\alpha$ and cluster decays, Nuclear Physics A 1013, 122221 (2021).   
[33] D. T. Akrawy, D. N. Poenaru, A. H. Ahmed, and L. Sihver, $\alpha$ -decay half-lives new semi-empirical relationship including asymmetry, angular momentum and shell effects, Nuclear Physics A 1021, 122419 (2022).   
[34] D. T. Akrawy and A. H. Ahmed, New empirical formula for $\alpha$ - decay calculations, International Journal of Modern Physics E 27, 1850068 (2018).   
[35] D. T. Akrawy, A. Budaca, G. Saxena, and A. H. Ahmed, Generalization of the screened universal $\alpha$ -decay law by asymmetry and angular momentum, The European Physical Journal A 58, 145 (2022).   
[36] M. Yu, M. Xu, Z. Liu, and L. Liu, Model investigation on the probability of qgp formation at different centralities in relativistic heavy ion collisions, Physical Review C—Nuclear Physics 80, 064908 (2009).   
[37] M. Ismail, W. Seif, A. Adel, and A. Abdurrahman, Alpha-decay of deformed superheavy nuclei as a probe of shell closures, Nuclear Physics A 958, 202 (2017).   
[38] D. Deng and Z. Ren, Improved double-folding $\alpha$ -nucleus potential by including nuclear medium effects, Physical Review C 96, 064306 (2017).   
[39] V. Y. Denisov and A. Khudenko, Erratum: α decay of eveneven superheavy elements [phys. rev. c 81, 034613 (2010)], Physical Review C—Nuclear Physics 82, 059903 (2010).   
[40] N. Wang, M. Liu, X. Wu, and J. Meng, Surface diffuseness correction in global mass formula, Physics Letters B 734, 215 (2014).   
[41] H. Anushree, S. Shubha, H. Manjunatha, and N. Sowmya, Entrance channel-dependent compound nucleus formation probability of heavy nuclei, Pramana 99, 1 (2025).   
[42] S. Madhu, H. Manjunatha, N. Sowmya, B. Rajesh, L. Seenappa, and R. Susheela, Cr-induced fusion reactions to synthesize superheavy elements, Nuclear Science and Techniques 35, 90 (2024).   
[43] H. Manjunatha, K. Sridhar, and N. Sowmya, Investigations of the synthesis of the superheavy element $\mathbf { z } = 1 2 2$ , Physical Review C 98, 024308 (2018).

[44] N. Manjunatha, H. C. S. Manjunatha, N. Sowmya, K. N. Sridhar, and P. S. Prabhavathi, Effect of quadrupole and hexadecapole deformations of target on projectile, Journal of the Physical Society of Japan 93, 054201 (2024).   
[45] N. Sowmya, H. Manjunatha, K. Sridhar, and M. Armstrong Arasu, Optimal incident energy of heavy ion fusion, Physical Review C 109, 024610 (2024).   
[46] F. Kondev, M. Wang, W. Huang, S. Naimi, and G. Audi, The

nubase2020 evaluation of nuclear physics properties, Chinese Physics C 45, 030001 (2021).   
[47] M. Ismail, W. Seif, and M. Botros, Effect of octupole and higher deformations on coulomb barrier, Nuclear Physics A 828, 333 (2009).   
[48] Q. Xiao, J.-H. Cheng, B.-L. Wang, Y.-Y. Xu, Y.-T. Zou, and T.- P. Yu, Half-lives for proton emission and $\alpha$ decay within the deformed gamow-like model, Journal of Physics G: Nuclear and Particle Physics 50, 085102 (2023).

![](images/33c09d1d950e12336581d4323b7b2aca674c0a3a0968e54cd3a6a70350aaadf1.jpg)

![](images/acd61fd399792c2a70246dca810eaeb5d10ab2fea594e2a8db4ba248ae2f1b0e.jpg)

![](images/b5fc7ab4236f089ba6ab91a9f09933c2505abb43512fad31e5b47e0322eeba84.jpg)

![](images/4e68ad58d054e3d3edeec7d3e87e686e70c1a9c3d506630a4cb6fed5aeb8a902.jpg)  
FIG. 2. The predicted $\alpha$ -decay half-lives in logaruthmic form of even-even nuclei with Z = 118, 120, 122, and 124 using Eq. (7) and Eq. (9), ND, Improved $+ \mathrm { U L }$ , and Improved $+ \mathrm { E F }$ with $Q _ { \alpha }$ obtained by WS4 [40]. The red square, the blue circle, the green triangle, the purple triangles and cyan diamonds denote the predictions by ND, Eq. (7), Eq. (9), Improved+UL, and Improved+EF respectively.

TABLE VII. The RMS deviation of the models DUR, DUR $+ \mathrm { D }$ , AKRA, AKRA+D,NGN,and NGN+D.   

<table><tr><td>Formula</td><td>Even-even n=181</td><td>Even-odd n=79</td><td>Odd-even n=80</td><td>Odd-odd n=60</td></tr><tr><td>DUR</td><td>0.3627</td><td>0.5565</td><td>0.4874</td><td>0.6595</td></tr><tr><td>DUR+D</td><td>0.3040</td><td>0.5449</td><td>0.4766</td><td>0.6016</td></tr><tr><td>The RMS reduction (%)</td><td>16</td><td>2</td><td>2.2</td><td>8.7</td></tr><tr><td>AKRA</td><td>0.3555</td><td>0.9596</td><td>0.7011</td><td>1.2580</td></tr><tr><td>AKRA+D</td><td>0.2775</td><td>0.9114</td><td>0.6676</td><td>1.077</td></tr><tr><td>The RMS reduction (%)</td><td>22</td><td>5</td><td>4.7</td><td>14.4</td></tr><tr><td>NGN</td><td>0.3121</td><td>0.6250</td><td>0.5213</td><td>0.6492</td></tr><tr><td>NGN+D</td><td>0.2994</td><td>0.6237</td><td>0.5209</td><td>0.6165</td></tr><tr><td>The RMS reduction (%)</td><td>4</td><td>0.2</td><td>0.07</td><td>5</td></tr></table>

TABLE VIII. ∆T different between experimental and theoretical formulas.   

<table><tr><td rowspan="2">Formula</td><td colspan="2">Even-even</td><td colspan="2">Even-odd</td><td colspan="2">Odd-even</td><td colspan="2">Odd-odd</td></tr><tr><td>Minimum</td><td>Maximum</td><td>Minimum</td><td>Maximum</td><td>Minimum</td><td>Maximum</td><td>Minimum</td><td>Maximum</td></tr><tr><td>DUR</td><td>-1.5708</td><td>0.6605</td><td>-1.8560</td><td>1.0952</td><td>-1.2388</td><td>1.3882</td><td>-2.1975</td><td>1.5149</td></tr><tr><td>DUR+D</td><td>-1.2194</td><td>0.7444</td><td>-1.7726</td><td>1.0750</td><td>-1.1644</td><td>1.2056</td><td>-2.4669</td><td>1.2479</td></tr><tr><td>AKRA</td><td>-1.5031</td><td>0.7323</td><td>-5.6337</td><td>1.7573</td><td>-2.3818</td><td>1.6460</td><td>-4.1263</td><td>1.8640</td></tr><tr><td>AKRA+D</td><td>-1.1861</td><td>0.7944</td><td>-5.3777</td><td>1.6525</td><td>-2.1315</td><td>1.4041</td><td>-4.073</td><td>1.6130</td></tr><tr><td>NGN</td><td>-1.2795</td><td>0.6773</td><td>-1.7121</td><td>1.2159</td><td>-1.5413</td><td>1.3080</td><td>-2.022</td><td>1.5198</td></tr><tr><td>NGN+D</td><td>-1.2485</td><td>0.6930</td><td>-1.7423</td><td>1.1905</td><td>-1.5554</td><td>1.3428</td><td>-2.22071</td><td>1.3167</td></tr></table>

TABLE IX. The DUR model log10TAKRA+D vs log10TDUR+D vs log10TND. Values for $Q \alpha$ is from Refs. [40].   

<table><tr><td>Z</td><td>A</td><td>Qα</td><td>log10TAKRA+D</td><td>log10TDUR+D</td><td>log10TND</td><td>Z</td><td>A</td><td>Qα</td><td>log10TAKRA+D</td><td>log10TDUR+D</td><td>log10TND</td></tr><tr><td>118</td><td>282</td><td>13.492</td><td>-5.598</td><td>-5.876</td><td>-6.160</td><td>122</td><td>290</td><td>15.092</td><td>-7.414</td><td>-7.731</td><td>-7.514</td></tr><tr><td></td><td>284</td><td>13.209</td><td>-5.084</td><td>-5.345</td><td>-5.116</td><td></td><td>292</td><td>14.994</td><td>-7.309</td><td>-7.600</td><td>-7.450</td></tr><tr><td></td><td>286</td><td>12.889</td><td>-4.485</td><td>-4.729</td><td>-4.704</td><td></td><td>294</td><td>14.643</td><td>-6.747</td><td>-7.022</td><td>-6.922</td></tr><tr><td></td><td>288</td><td>12.587</td><td>-3.893</td><td>-4.120</td><td>-4.079</td><td></td><td>296</td><td>14.670</td><td>-6.866</td><td>-7.108</td><td>-7.038</td></tr><tr><td></td><td>290</td><td>12.572</td><td>-3.931</td><td>-4.126</td><td>-4.250</td><td></td><td>298</td><td>14.678</td><td>-6.945</td><td>-7.156</td><td>-7.179</td></tr><tr><td></td><td>292</td><td>12.212</td><td>-3.182</td><td>-3.363</td><td>-3.508</td><td></td><td>300</td><td>14.197</td><td>-6.114</td><td>-6.314</td><td>-6.353</td></tr><tr><td></td><td>294</td><td>12.171</td><td>-3.156</td><td>-3.305</td><td>-3.459</td><td></td><td>302</td><td>14.212</td><td>-6.210</td><td>-6.378</td><td>-6.307</td></tr><tr><td></td><td>296</td><td>11.726</td><td>-2.157</td><td>-2.298</td><td>-2.421</td><td></td><td>304</td><td>13.714</td><td>-5.299</td><td>-5.457</td><td>-5.333</td></tr><tr><td></td><td>298</td><td>12.158</td><td>-3.264</td><td>-3.345</td><td>-3.399</td><td></td><td>306</td><td>13.780</td><td>-5.499</td><td>-5.621</td><td>-5.463</td></tr><tr><td></td><td>300</td><td>11.932</td><td>-2.797</td><td>-2.857</td><td>-2.876</td><td></td><td>308</td><td>14.918</td><td>-7.715</td><td>-7.753</td><td>-7.498</td></tr><tr><td></td><td>302</td><td>12.018</td><td>-3.072</td><td>-3.092</td><td>-3.101</td><td></td><td>310</td><td>13.435</td><td>-4.931</td><td>-5.004</td><td>-4.874</td></tr><tr><td></td><td>304</td><td>13.101</td><td>-5.557</td><td>-5.484</td><td>-5.444</td><td></td><td>312</td><td>12.141</td><td>-2.102</td><td>-2.209</td><td>-2.445</td></tr><tr><td></td><td>306</td><td>12.459</td><td>-4.235</td><td>-4.160</td><td>-4.192</td><td></td><td>314</td><td>12.096</td><td>-2.061</td><td>-2.136</td><td>-2.408</td></tr><tr><td></td><td>308</td><td>11.184</td><td>-1.191</td><td>-1.155</td><td>-1.282</td><td></td><td>316</td><td>11.638</td><td>-0.982</td><td>-1.050</td><td>-1.372</td></tr><tr><td></td><td>310</td><td>10.414</td><td>0.886</td><td>0.908</td><td>0.461</td><td></td><td>318</td><td>10.619</td><td>1.762</td><td>1.662</td><td>1.238</td></tr><tr><td></td><td>312</td><td>9.742</td><td>2.897</td><td>2.906</td><td>2.368</td><td></td><td>320</td><td>11.637</td><td>-1.128</td><td>-1.125</td><td>-1.778</td></tr><tr><td></td><td>314</td><td>8.365</td><td>7.854</td><td>7.780</td><td>7.088</td><td></td><td>322</td><td>11.221</td><td>-0.093</td><td>-0.082</td><td>-0.773</td></tr><tr><td></td><td>316</td><td>8.601</td><td>6.829</td><td>6.815</td><td>5.854</td><td>124</td><td>296</td><td>15.117</td><td>-6.965</td><td>-7.304</td><td>-7.152</td></tr><tr><td>120</td><td>286</td><td>14.013</td><td>-6.012</td><td>-6.322</td><td>-6.125</td><td></td><td>298</td><td>15.650</td><td>-7.952</td><td>-8.239</td><td>-8.125</td></tr><tr><td></td><td>288</td><td>13.705</td><td>-5.479</td><td>-5.772</td><td>-5.610</td><td></td><td>300</td><td>15.313</td><td>-7.440</td><td>-7.711</td><td>-7.607</td></tr><tr><td></td><td>290</td><td>13.676</td><td>-5.490</td><td>-5.753</td><td>-5.662</td><td></td><td>302</td><td>14.782</td><td>-6.558</td><td>-6.821</td><td>-6.685</td></tr><tr><td></td><td>292</td><td>13.441</td><td>-5.086</td><td>-5.328</td><td>-5.387</td><td></td><td>304</td><td>14.914</td><td>-6.865</td><td>-7.092</td><td>-6.905</td></tr><tr><td></td><td>294</td><td>13.215</td><td>-4.686</td><td>-4.907</td><td>-4.907</td><td></td><td>306</td><td>14.667</td><td>-6.479</td><td>-6.685</td><td>-6.453</td></tr><tr><td></td><td>296</td><td>13.316</td><td>-4.964</td><td>-5.148</td><td>-5.245</td><td></td><td>308</td><td>14.644</td><td>-6.504</td><td>-6.678</td><td>-6.453</td></tr><tr><td></td><td>298</td><td>12.981</td><td>-4.324</td><td>-4.492</td><td>-4.493</td><td></td><td>310</td><td>15.412</td><td>-7.945</td><td>-8.054</td><td>-7.774</td></tr><tr><td></td><td>300</td><td>13.294</td><td>-5.055</td><td>-5.174</td><td>-5.176</td><td></td><td>312</td><td>13.833</td><td>-5.066</td><td>-5.213</td><td>-4.998</td></tr><tr><td></td><td>302</td><td>12.866</td><td>-4.211</td><td>-4.318</td><td>-4.346</td><td></td><td>314</td><td>13.223</td><td>-3.864</td><td>-4.007</td><td>-4.185</td></tr><tr><td></td><td>304</td><td>12.740</td><td>-4.003</td><td>-4.082</td><td>-4.020</td><td></td><td>316</td><td>13.175</td><td>-3.827</td><td>-3.940</td><td>-4.147</td></tr><tr><td></td><td>306</td><td>13.765</td><td>-6.216</td><td>-6.210</td><td>-6.156</td><td></td><td>318</td><td>12.544</td><td>-2.469</td><td>-2.583</td><td>-2.824</td></tr><tr><td></td><td>308</td><td>12.945</td><td>-4.591</td><td>-4.591</td><td>-4.556</td><td></td><td>320</td><td>11.889</td><td>-0.939</td><td>-1.057</td><td>-1.350</td></tr><tr><td></td><td>310</td><td>11.478</td><td>-1.189</td><td>-1.236</td><td>-1.297</td><td></td><td>322</td><td>12.233</td><td>-1.873</td><td>-1.935</td><td>-2.509</td></tr><tr><td></td><td>312</td><td>11.196</td><td>-0.518</td><td>-0.548</td><td>-0.921</td><td></td><td>324</td><td>11.975</td><td>-1.303</td><td>-1.346</td><td>-1.949</td></tr><tr><td></td><td>314</td><td>10.739</td><td>0.679</td><td>0.655</td><td>0.233</td><td></td><td>326</td><td>12.241</td><td>-2.029</td><td>-2.023</td><td>-2.652</td></tr><tr><td></td><td>316</td><td>9.173</td><td>5.631</td><td>5.526</td><td>4.360</td><td></td><td>328</td><td>11.117</td><td>0.826</td><td>0.799</td><td>-0.199</td></tr><tr><td></td><td>318</td><td>9.912</td><td>3.045</td><td>3.034</td><td>2.243</td><td></td><td>330</td><td>12.311</td><td>-2.335</td><td>-2.256</td><td>-2.941</td></tr><tr><td></td><td>320</td><td>9.660</td><td>3.806</td><td>3.810</td><td>2.978</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>