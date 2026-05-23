# Correlation between nuclear isospin asymmetry and $\alpha$ -particle preformation probability for superheavy nuclei from a Bayesian inference

Xiao-Yan Zhu $\textcircled{1}$ ,1, 2, ∗ Hao Zhang $\textcircled{1}$ ,3 Wei Gao $\textcircled{1}$ ,4 Wen-Jing

Xing ,3, † Wen-Bin Lin ,1, 2, ‡ and Xiao-Hua Li $\bigoplus 3 , \ S$

1School of Mathematics and Physics,

University of South China, Hengyang, 421001, China

2Hunan Provincial Key Laboratory of Mathematical Modeling and Scientific Computing,

University of South China, Hengyang, 421001, China

$^ 3$ School of Nuclear Science and Technology,

University of South China, Hengyang, 421001, China

4School of Physical Science and Technology,

Southwest Jiaotong University, Chengdu, 610031, China

(Dated: March 10, 2026)

# Abstract

In the study of $\alpha$ decay within the superheavy nuclear region ( $Z \ge 9 0$ and $N \ge 1 4 0$ ), the $\alpha$ - particle preformation probability $P _ { \alpha }$ serves as a crucial physical quantity linking nuclear structure to decay observables. We introduce a phenomenological model incorporating the decay energy $Q _ { \alpha }$ , mass number $A$ , orbital angular momentum $l$ , isospin asymmetry $I$ , and unpaired nucleon effect. For the first time, a Bayesian inference method combined with Markov Chain Monte Carlo (MCMC) sampling has been employed to impose global constraints on the model parameters, enabling the systematic and high-precision calculation of $P _ { \alpha }$ . The results reveal a significant suppressing effect of isospin asymmetry on $P _ { \alpha }$ , a finding independently corroborated by random forest-based feature importance analysis, which identified $I$ as a dominant factor. Furthermore, calculations using the maximum a posteriori (MAP) parameters not only reproduce the shell effect at $N = 1 5 2$ but also yield $\alpha$ decay half-life predictions in excellent agreement with experimental ones, thereby validating this model universality. This work provides the first global analysis tool for probing the $\alpha$ preformation mechanism in superheavy nuclei, underscores the potential of the Bayesian framework for inverting complex nuclear physics problems, and establishes a reliable theoretical benchmark for guiding future experimental exploration of superheavy nuclei.

# I. INTRODUCTION

Since George Gamow [1] and Gurrney and Condon [2] first described $\alpha$ decay based on quantum tunneling theory in 1928, quantum mechanics found its initial application in nuclear physics by successfully explaining this process. With the continuous development of radioactive ion beam facilities worldwide, $\alpha$ decay, as one of the dominant decay modes in heavy and superheavy nuclei, has attracted extensive attention [3–5]. Particularly in the synthesis of superheavy elements and the study of nuclear structure information, it remains a subject of considerable interest in both experimental and theoretical nuclear physics [6–12].

Theoretical support plays a crucial role in ensuring the feasibility of experimental implementation. Generally, the primary objective of theoretical studies on $\alpha$ decay is to predict the half-lives and decay modes of unknown nuclei. Various microscopic theories, such as the R-matrix method [13, 14], liquid-drop model [15, 16], Tohsaki-Horiuchi-Schuck-R¨opke wave function approach [17, 18], and so on [19–27], have been employed to calculate $\alpha$ decay half-lives. However, a significant factor contributing to the discrepancy between theoretically calculated half-lives and experimental data lies in the determination of the $\alpha$ -particle preformation factor, which represents the probability of an $\alpha$ -cluster forming on the surface of the parent nucleus. Owing to the structural complexity of quantum many-body systems, accurately calculating the $\alpha$ -particle preformation factor, particularly for superheavy nuclei with $Z \geq 9 0$ and $N \geq 1 4 0$ , remains exceptionally challenging [28–30].

In theoretical calculations, treating the $\alpha$ -particle preformation factor of an unknown nucleus as a constant for extrapolating $\alpha$ decay half-lives possesses certain limitations. Consequently, numerous models and phenomenological formulas have been proposed to evaluate $P _ { \alpha }$ , such as the expression based on the number of valence nucleons (or holes). Building on this approach, studies of nuclei near the $Z = 8 2$ and $N = 1 2 6$ shell closures have revealed a linear correlation between $P _ { \alpha }$ and the product of valence protons (holes) and valence neutrons (holes) [31–33]. Given that the magic numbers in superheavy nuclei remain uncertain, extending the systematics to the superheavy region proves difficult. Subsequent investigations have adopted a microscopic perspective, establishing a connection between $\alpha$ decay energy and $P _ { \alpha }$ by empirical half-life formulas, thereby proposing analytical expressions for estimating $P _ { \alpha }$ . While these phenomenological expressions improve the accuracy of halflife predictions, most of the resulting preformation factors are model-dependent and their

parameters only locally applicable. Therefore, this work aims to explore a method that incorporates nuclear structure effects and enables a global and accurate description of the $\alpha$ -particle preformation factor.

The structure of this article is organized as follows. Section II gives $\alpha$ -particle preformation factor and local phenomenological expression. Section III presents the global application of Bayesian inference. In Section IV, $\alpha$ -particle preformation factors with isospin effects are discussed. Finally, Section V is a concise summary.

# II. $\alpha$ -PARTICLE PREFORMATION FACTOR AND LOCAL PHENOMENOLOG-ICAL EXPRESSION

In the cosh-type potential model (CTP), an analytical phenomenological formula incorporating five parameters has been extracted by combining experimental decay energies and half-lives to represent the $\alpha$ -particle preformation factor [34]. Utilizing this formula, the preformation factors for nuclides near the neutron magic numbers $N = 1 2 6$ , 152, and 162 were subsequently derived. The results indicate that nuclei in the vicinity of shell closures are more tightly bound compared to their neighboring isotopes. In this work, $P _ { \alpha }$ is extracted from the ratios between theoretical $\alpha$ decay half-life calculated by CTP and the corresponding experimental one. In the framework of CPT, the $\alpha$ decay constant $\lambda$ is defined as

$$
\lambda = \frac {\hbar P _ {\alpha} F P}{4 \mu}, \tag {1}
$$

where $\hbar$ and $\mu$ represent the Planck constant and reduced mass of the $\alpha$ -particle and daugh ter nucleus. $F ^ { \prime }$ is the normalized factor of bound-state wave function. $P$ represents the penetration probability calculated using the classical Wentzel-Kramers-Brillouin (WKB) approximation. The experimental $\alpha$ decay constant $\lambda ^ { E x p }$ can be obtained by

$$
\lambda^ {\mathrm {E x p}} = \frac {\hbar P _ {\alpha} ^ {\mathrm {E x p}} F P}{4 \mu} = \frac {\ln 2}{T _ {1 / 2} ^ {\mathrm {E x p}}}. \tag {2}
$$

And assuming the $\alpha$ -particle preformation factor to be a constant, $P _ { \alpha } = 1$ , the theoretical $\alpha$ decay constant $\lambda ^ { \mathrm { C a l } }$ is calculated by

$$
\lambda^ {\mathrm {C a l}} = \frac {\hbar P _ {\alpha} F P}{4 \mu} = \frac {\ln 2}{T _ {1 / 2} ^ {\mathrm {C a l}}}. (3)
$$

The experimental $\alpha$ -particle preformation factor can obtained from the ration the ratio between the theoretical $\alpha$ decay half-life and the corresponding experimental one. It can be expressed as

$$
P _ {\alpha} ^ {\mathrm {E x p}} = \frac {\lambda^ {\mathrm {E x p}}}{\lambda^ {\mathrm {C a l}}} = \frac {T _ {1 / 2} ^ {\mathrm {E x p}}}{T _ {1 / 2} ^ {\mathrm {C a l}}}. \tag {4}
$$

In our recent work [34], a local phenomenological expression for estimating $\alpha$ -particle preformation factor in heavy and superheavy nuclei has been proposed. It is given by

$$
\log_ {1 0} P _ {\alpha} = \mathrm {a Z Q} _ {\alpha} ^ {- 1 / 2} + \mathrm {b A} ^ {1 / 3} + \mathrm {c} + \mathrm {d} [ l (l + 1) ] ^ {1 / 2} + \mathrm {h}. \tag {5}
$$

Here, parameters a, b, c, d, and h are adjustable constants related to physical quantities. This expression is constructed similarly to other analytical forms, with the purpose of inferring the possibility of $\alpha$ -cluster formation inside the parent nucleus $P _ { \alpha }$ . This process incorporates all nuclides in the most recent evaluated atomic mass table [35, 36] and is based on the known linear correlations of $Q _ { \alpha }$ , $Z$ , and $A$ , combined with an inverse proportionality to the decay half-life. A major drawback of this method, however, is that the adjustable parameters are derived from specific datasets, meaning the resulting expression is only locally applicable.

# III. THE GLOBAL APPLICATION OF BAYESIAN INFERENCE

Bayesian inference method has been successfully employed to constrain model parameters across various subfields of physics, including the calibration of relativistic collision models and the analysis of jet energy loss in heavyion physics [37–39], as well as studies of the equation of state for nuclear matter [40, 41], nucleon distributions within atomic nuclei [42], and $\alpha$ decay properties in heavy and superheavy nuclei [27], among others [43–47]. In this work, we obtain the global $P _ { \alpha }$ by extracting the uncertainties of the input physical quantities given in Eq. (5). Provided that different schemes reflect the essential feature of $P _ { \alpha }$ and yield results that are consistent with experimental data after Bayesian calibration, a global analytical expression can be established.

In this study, Eq. (5) is formulated into a global phenomenological $\alpha$ -particle preformation factor model using a five-dimension parameter vector $\theta = ( \mathrm { a } , \mathrm { b } , \mathrm { c } , \mathrm { d } , \mathrm { h } )$ , with 200 uniformly distributed design points generated by Latin Hypercube Sampling (LHS) [48–50] across physically meaningful and broadly defined ranges to form a $2 0 0 \times 5$ design matrix

$\Theta = ( \theta _ { 1 } , \theta _ { 2 } , . . . , \theta _ { 2 0 0 } ) ^ { \top }$ , thereby balancing parameter space coverage and computational efficiency. To facilitate efficient Bayesian posterior inference, a Gaussian Process (GP) emulator [51] is constructed as a surrogate model. It employs an exponentiated quadratic kernel, defined as

$$
\sigma (\theta , \theta^ {\prime}) = \exp (- \frac {| | \theta - \theta^ {\prime} | | ^ {2}}{2 t ^ {2}}), \tag {6}
$$

where $t$ represents the characteristic length scale that governs the rate of correlation decay between input points. The model also incorporates output centralization. The training output $Y$ is assumed to follow a multivariate Gaussian distribution given by

$$
Y \sim \mathcal {N} (0, K), \tag {7}
$$

where the covariance matrix $K$ is characterized by elements $[ K ] _ { i j } = \sigma ( \theta _ { i } , \theta _ { j } )$ . For a new test point $\Theta ^ { * }$ , the GP emulator predicts its output $Y ^ { * }$ to follow a conditional Gaussian distribution:

$$
Y _ {*} | \Theta_ {*}, \Theta , Y \sim \mathcal {N} (K _ {*} K ^ {- 1} Y, K _ {* *} - K _ {*} K ^ {- 1} K _ {*} ^ {\top}). \tag {8}
$$

Here, $K _ { * } = \sigma ( \Theta _ { * } , \Theta )$ denotes the covariance matrix between the new test point and the training data, and $K _ { * * } = \sigma ( \Theta _ { * } , \Theta _ { * } )$ represents the covariance at the test point itself. This GP framework achieves efficient interpolation and uncertainty quantification in high-dimensional parameter spaces, thereby providing a reliable and computationally feasible foundation for subsequent Bayesian parameter inference.

In the following, we employ the Bayesian inference approach, leveraging experimental data on superheavy nuclei with $Z \ge 9 0$ and $N \geq 1 4 0$ from Ref. [27], to calibrate and quantify uncertainties in the parameters $\theta = ( \mathrm { a } , \mathrm { b } , \mathrm { c } , \mathrm { d } , \mathrm { h } )$ of Eq. (5). This calibration process constitutes an inverse problem, wherein the model input parameters are inferred from experimental data. The corresponding statistical inference is grounded in the posterior distribution, which is expressed as

$$
P (\theta | \text {d a t a}) \propto P (\text {d a t a} | \theta) \cdot P (\theta), \tag {9}
$$

where $P ( \theta )$ is the prior distribution. We employ uniform priors over physically plausible parameter ranges a $\in ~ ( - 0 . 1 5 , 0 . 0 5 )$ , $\mathrm { ~ b ~ } \in \ ( - 2 . 0 , 2 . 0 )$ , $\mathrm { ~ c ~ } \in \ ( 4 . 0 , 1 6 . 0 )$ , $\mathrm { ~ d ~ } \in \ ( - 0 . 2 5 , 0 . 6 7 )$ , $\mathrm { ~ h ~ } \in \mathsf { \Gamma } ( - 0 . 8 , - 0 . 1 )$ , which are sufficiently broad to allow the model outputs to cover all experimental data. The likelihood function $P ( \mathrm { d a t a } | \theta )$ is formulated based on a Gaussian

assumption and expressed in a $\chi ^ { 2 }$ form:

$$
P (\text {d a t a} | \theta) = \prod_ {i} \frac {1}{\sqrt {2 \pi} \sigma_ {i}} e ^ {- \left(y _ {i} (\theta) - y _ {i} ^ {\exp}\right) ^ {2} / \left(2 \sigma_ {i} ^ {2}\right)}, \tag {10}
$$

where $y _ { i } ( \theta )$ denotes the predicted value of the model at the $i$ -th data point. $y _ { i } ^ { \mathrm { { e x p } } }$ and $\sigma _ { i }$ represent the corresponding experimental data and its associated uncertainty, respectively. To conduct a comprehensive assessment of the consistency between the parameters and the entire set of experimental data, a joint likelihood function is constructed by integrating the data from even-even (ee), odd-A (oa), and odd-odd (oo) nuclei. It is given by

$$
P (\mathrm {d a t a} | \theta) = P \left(\mathrm {d a t a} _ {\log_ {1 0} \mathrm {P} _ {\alpha} ^ {\mathrm {e e}}} | \theta\right) P \left(\mathrm {d a t a} _ {\log_ {1 0} \mathrm {P} _ {\alpha} ^ {\mathrm {o a}}} | \theta\right) P \left(\mathrm {d a t a} _ {\log_ {1 0} \mathrm {P} _ {\alpha} ^ {\mathrm {o o}}} | \theta\right). \tag {11}
$$

To effectively sample from the posterior distribution, we employ the Metropolis-Hastings algorithm to conduct the Markov-Chain Monte-Carlo (MCMC) method [50, 52] in the parameter space. The sampling process is performed in logarithmic probability space to enhance numerical stability, with new parameter proposals being generated by a Gaussian transition kernel centered on the current position. To further improve sampling efficiency, an ensemble of 150 walkers is initialized from random starting points within the parameter space. Following a burn-in phase of 5,000 steps to ensure the chains has adequately converged to the target posterior distribution, a subsequent set of 10,000 steps per walker is recorded to generate the final posterior sample ensemble.

Based on the MCMC sampling results, the marginal posterior distributions of the parameters are estimated, with their maximum a posteriori (MAP) estimates and 95% credible intervals (C.I.’s) obtained. The correlations and degeneracies among the parameters are visualized using a corner plot, as illustrated in Fig. 1. The diagonal subpanels of this figure display marginal posterior distributions for each parameter, where the MAP estimates and 95% C.I.’s are marked by red dashed lines. The off-diagonal subpanels, conversely, present the two-dimensional joint posterior distributions for each parameter pair. As can be seen from Fig. 1, the posterior distribution of parameter a (associated with $Z Q _ { \alpha } ^ { - 1 / 2 }$ ) is concentrated and independent, suggesting a well-constrained and stable underlying physical mechanism. In contrast, the strong positive correlations observed among parameters b, c, d, and h indicate potential coupling or redundancy in the physical effects related to mass number $A ^ { 1 / 3 }$ and angular momentum $( l ( l + 1 ) ) ^ { 1 / 2 }$ within the model. This correlation

structure provides crucial clues for understanding the microscopic mechanism of $\alpha$ -particle preformation factor.

![](images/fc7b4b4f7a00580543bf0f49490e69755adcc956dae6a953f9d2e01aab88b8f4.jpg)  
FIG. 1. Posterior distributions of model’s global parameters (diagonal panels) and their correlations (off-diagonal panels) extracted from Eq. (5) using the original uncertainties of the experimental data.

# IV. $\alpha$ -PARTICLE PREFORMATION FACTORS WITH ISOSPIN EFFECTS

For an extended period, decay has been regarded as a reliable avenue for investigating nuclear structural information. Among various decay modes, $\alpha$ decay, which stands as one of the predominant decay mechanisms in heavy and superheavy nuclei, continues to serve as one of the most crucial and effective means for probing the structure, properties,

and synthesis mechanisms of superheavy nuclei [4, 11, 12]. Recent studies [53, 54] have revealed that the isospin asymmetry effect plays an essential role in $\alpha$ decay lifetimes and the key physical quantity $P _ { \alpha }$ , by simultaneously influencing the nuclear potential and proton distribution. Based on this understanding, the present work focuses on investigating the specific manifestations of the isospin asymmetry effect in the $\alpha$ -particle preformation factor within the superheavy nuclear region ( $Z \ \geq \ 9 0$ and $N \geq 1 4 0$ ). In order to construct a global phenomenological model for $P _ { \alpha }$ , we employ the same experimental data and Bayesian inference method as described in the preceding section. The model adopts $Z$ , $Q _ { \alpha } ^ { - 1 / 2 }$ , $A ^ { 1 / 3 }$ , $l$ , and the isospin asymmetry parameter $I = ( N - Z ) / A$ as feature variable, with $\log _ { 1 0 } P _ { \alpha }$ as the target variable. It is given by

$$
\log_ {1 0} P _ {\alpha} = \mathrm {a Z Q} _ {\alpha} ^ {- 1 / 2} + \mathrm {b A} ^ {1 / 3} + \mathrm {c} + \mathrm {d} [ l (l + 1) ] ^ {1 / 2} + \mathrm {e} [ I (I + 1) ] ^ {1 / 2} + \mathrm {h}. \tag {12}
$$

Here, parameter a, associated with $Q _ { \alpha }$ and $Z$ , quantifies the contribution of decay energy to $\log _ { 1 0 } P _ { \alpha }$ . Parameter b, which relates to $A ^ { 1 / 3 }$ , reflects the modulation of nuclear surface effects. The constant term c represents other unspecified systematic effects or serves as a baseline value. Parameter d, connected with $l$ , characterizes the hindrance effect of the centrifugal barrier on $P _ { \alpha }$ . Parameter e, associated with the neutron-proton asymmetry $I$ , describes the influence of the isospin effect on $P _ { \alpha }$ . Lastly, Parameter h, linked to unpaired nucleons, accounts for the blocking effect resulting from nucleonic pairing correlations.

In the model considering isospin effects, Eq. (12), the parameter $\theta = ( \mathrm { a , b , c , d , e , h } )$ is a six-dimensional vector. A uniform prior distribution $P ( \theta )$ is assumed over the following intervals: a $\in ( 0 . 0 2 , 0 . 1 )$ , $\mathrm { b } \in ( - 2 . 0 , 2 . 0 )$ , $\mathrm { { c } \in ( - 2 . 0 , 4 . 0 ) }$ , $\mathrm { d } \in ( - 0 . 3 , 0 . 1 )$ , $\mathrm { ~ e ~ } \in ( - 1 0 . 0 , - 2 . 0 )$ , and $\mathrm { ~ h ~ } \in \left( - 1 . 0 , - 0 . 2 \right)$ . To improve the efficiency of parameter calibration, GP emulator is employed to scan the six-dimensional parameter space, serving as a surrogate for the actual perturbative calculations. This approach accelerates the evaluation of the likelihood in the Bayesian analysis. Using the same MCMC sampling method as described in the previous section, Fig. 2 displays the posterior probability distributions of the six parameters obtained from Bayesian inference to the experimental data. Along the diagonal are the marginal posterior distributions of individual parameters, with red dashed lines indicating MAP and 95% C.I.’s. The off-diagonal subplots display the joint posterior distributions between parameters. From Fig. 2, physically meaningful relationships among parameters can be observed. Parameter a exhibits a markedly positive peak value, indicating that $Q _ { \alpha }$

serves as the primary driving force enhancing $\alpha$ decay. The posterior distribution of parameter b is concentrated in the negative region, implying that the size effect represented by $A ^ { 1 / 3 }$ significantly suppresses the preformation probability of $\alpha$ -particle in the superheavy region, consistent with the higher Coulomb barrier and more complex cluster formation process in superheavy nuclei. Parameter e is negative and possesses a large absolute magnitude, providing strong evidence that the isospin effect inhibits $\alpha$ decay, reflecting the considerable difficulty of forming an $N = Z$ $\alpha$ -cluster in extremely neutron-rich superheavy nuclei. The peak of parameter h is also negative, suggesting that unpaired nucleons may impose additional suppression on $P _ { \alpha }$ . It is evident that in superheavy nuclei, the preformation probability of $\alpha$ decay is modulated collectively by the enhancing effect of $Q _ { \alpha }$ , the suppressing influence of $A ^ { 1 / 3 }$ , the inhibition due to strong neutron–proton asymmetry, and possible shell effects. Among these, the distinctly negative value of parameter e and its relative independence observed in the joint distributions underscore the necessity of incorporating an isospin asymmetry correction term when describing $\alpha$ decay in superheavy nuclei.

Furthermore, to independently validate the role of the isospin effect, we analyzed the relative dependence of the $\alpha$ -particle preformation factor on several key features using the random forest method, as illustrated in Fig. 3. The results reveal that, among the selected features $( l , Q , I , Z , A )$ , the feature $l$ , which is closely associated with isospin asymmetry, has the highest relative dependence, significantly exceeding that of other influencing factors. This independent machine learning analysis corroborates the notable role of parameter e observed in the Bayesian posterior analysis. These findings mutually reinforce the conclusion that the isospin effect plays a crucial role in the $\alpha$ preformation factor of $\alpha$ decay in superheavy nuclei.

As illustrated in Fig. 4, we present the calculated $\alpha$ -particle preformation factors based on the Bayesian calibrated model. Using the MAP values of parameters drawn from the posterior distribution, the preformation factors are calculated and compared with experimental ones for even-even (Cf), odd-even (Es), and odd-A (Md) nuclei. The posterior distributions derive from the calibrated model (depicted as blue, brown, and green bands) show good agreement with the corresponding experimental ones (including error bars) across most neutron number intervals, with the most consistent description achieved for the even-even Cf nuclei. Leveraging the robustness of the posterior distributions, we further constructed the three-dimensional plot shown in Fig. 5, based on the isospin $I$ , neutron number $N$ ,

![](images/87420f1cd0ad69c630924e3d1e9a04c4192728edf944878f0ebd1dd3c2d9efb3.jpg)  
FIG. 2. Posterior distributions of model’s global parameters and their correlations extracted from Eq. (12) using the original uncertainties of the experimental data.

and the logarithm of the $\alpha$ decay half-life, $\log _ { 1 0 } T _ { 1 / 2 }$ . The figure comprises four subplots, corresponding to the four superheavy nuclides Cf, Es, Fm, and Md. Each subplot uses a white grid as the background, with $N$ on the horizontal axis, $I$ on the depth axis, and $\log _ { 1 0 } T _ { 1 / 2 }$ on the vertical axis. Plotted within are the posterior distribution curves derived from Eq. (5) and Eq. (12). Experimental ones are denoted by blue triangles, while the red diamonds and green asterisks represent the calculations based on the MAP values from Eq. (5) and Eq. (12), respectively. A clear observation from the figure is a pronounced shell effect near $N = 1 5 2$ for all nuclides, where the half-life curves exhibit distinct peaks. Furthermore, the predictions from the posterior distributions show good overall agreement with the experimental ones, thereby providing further validation of the Bayesian calibration

![](images/97f1fa7b5da2e2a58925b7860b46e04050249f1a51b86574b44f7144d17a82c1.jpg)  
FIG. 3. Relative dependencies of $\alpha$ particle preformation factor on various features.

capability to describe the $\alpha$ decay behavior of nuclides with different parities.

![](images/48522ae98975bc565c40fe83e0460d68e20a21e438fec14e03d1984c0bc33257.jpg)  
FIG. 4. The calculation results of the posterior distribution $P _ { \alpha }$ of the parameters of for Cf, Es, and Md nuclei based on the model Eq. (12) are compared with the experimental data.

In addition, Table I lists the preformation factors and $\alpha$ decay half-lives for both light and heavy nuclei with different parities. These values are calculated using Eq. (5) and, with the

![](images/c1649584be825c23e6fd2c829121a74f8b4823a65248f2d6739d11325dc1fc3d.jpg)

![](images/d47e3ccf7975e1382b796176b3de65eb39682eb059226d16ff2771354d17d870.jpg)

![](images/28c59e227285743ed7bb0436083f51b44fd54e495e0d8f918f52f3a47fd89211.jpg)

![](images/dd431f0377037c681ca66d8a7a0e7a7a1ec88f190f14e04310510049aeb43134.jpg)

![](images/bef042fcf679d2a635c2c7ca24dd6bba2a53be5d389d87ffaeb4e7e62455c16a.jpg)  
FIG. 5. The $\alpha$ decay half-lives of Cf, Es, Fm, and Md near $N = 1 5 2$ , as calculated using the posterior distributions of Eq. (5) and Eq. (12) along with their corresponding MAP values.

inclusion of the isospin effect, Eq. (12), and are subsequently compared with experimental ones as well as results from the Refs. [55] and [33]. The table clearly shows that the $\alpha$ decay half-lives compute with the present model, particularly those obtained from the corrected isospin effect Eq. (12), are in remarkable agreement with the experimental values and remain consistent with other theoretical findings. This comparative analysis further confirms the effectiveness and universality of the current model in characterizing $\alpha$ decay behavior across various types of atomic nuclei.

TABLE I. The $\alpha$ -particle preformation factors $P _ { \alpha } ^ { \mathrm { C a l 1 } }$ and P Cal2α , $P _ { \alpha } ^ { \mathrm { C a l 2 } }$ are extracted from Eq. (5) and the included isospin effect Eq. (12), respectively. Comparing with both the experimental half-lives $T _ { 1 / 2 } ^ { \mathrm { e x p } }$ and the calculated half-lives $T _ { 1 / 2 } ^ { \mathrm { C a l 1 } }$ , T Cal21/2 , T Cal31/2 and T Cal41/2 o $T _ { 1 / 2 } ^ { \mathrm { C a l 3 } }$ , $T _ { 1 / 2 } ^ { \mathrm { C a l } 4 }$ btained using Eq. (5), Eq. (12), and Refs. [55] and [33].   

<table><tr><td>Nuclei l</td><td>Qα</td><td>PCal1</td><td>PCal2</td><td>Texp1/2(s)</td><td>TCal1(s)</td><td>TCal2(s)</td><td>TCal3(s)</td><td>TCal4(s)</td></tr><tr><td></td><td></td><td>Eq. (5)</td><td>Eq. (12)</td><td></td><td>Eq. (5)</td><td>Eq. (12)</td><td>[55]</td><td>[33]</td></tr><tr><td>105Te</td><td>2</td><td>5.069</td><td>0.502</td><td>1.198</td><td>6.330 × 10-7</td><td>1.880 × 10-7</td><td>7.876 × 10-8</td><td>2.397 × 10-7</td></tr><tr><td>109I</td><td>2</td><td>3.918</td><td>0.546</td><td>0.803</td><td>6.629 × 10-1</td><td>5.311 × 10-2</td><td>3.609 × 10-2</td><td>7.094 × 10-2</td></tr><tr><td>112Cs</td><td>0</td><td>3.360</td><td>0.253</td><td>0.925</td><td>1.885 × 10-1</td><td>2.451 × 103</td><td>6.718 × 102</td><td>7.511 × 10-1</td></tr><tr><td>210Pb</td><td>0</td><td>3.792</td><td>0.796</td><td>0.507</td><td>3.687 × 1016</td><td>4.775 × 1015</td><td>7.499 × 1015</td><td>-</td></tr><tr><td>212Po</td><td>0</td><td>8.954</td><td>0.329</td><td>0.081</td><td>2.944 × 10-7</td><td>1.706 × 10-7</td><td>6.910 × 10-7</td><td>-</td></tr></table>

# V. SUMMARY

In our systematic investigation of the correlation between isospin asymmetry and $\alpha$ - particle preformation probability in the superheavy region, a Bayesian inference method is employed. Within the CTP framework, $P _ { \alpha }$ are first extracted from experimental decay energies and half-lives, leading to the construction of a multi-parameter model incorporating an isospin-dependent term. To efficiently explore the high-dimensional parameter space and perform uncertainty quantification, a GP emulator is constructed using design points generated via LHS. Posterior distributions of the parameters are subsequently obtained through MCMC sampling based on the Metropolis-Hastings algorithm. It is shown that neutronproton asymmetry significantly suppresses $P _ { \alpha }$ . Furthermore, an independent analysis using the random forest method confirm the prominent role of isospin, showing that it exhibits a higher relative dependence among the various influencing factors. These findings collectively demonstrate that the Bayesian-calibrated model is capable of providing a global description of $\alpha$ decay preformation factors and half-lives for superheavy nuclei with different structural types. We offer a reliable theoretical method for systematically exploring decay properties in the superheavy region and underscores the necessity of incorporating isospin-dependent corrections in $\alpha$ decay studies.

# ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China (Grants Nos: 12175100, 11975132 and 12405154).

[1] G. Gamow, Z. Phys. 51, 204 (1928).   
[2] R. W. Gurney and E. U. Condon, Nature 122, 439 (1928).   
[3] H. J. Mang, Ann. Rev. Nucl. Part. Sci. 14, 1 (1964).   
[4] A. N. Andreyev et al., Phys. Rev. Lett. 110, 242502 (2013).   
[5] J. H. Hamilton, S. Hofmann, and Y. T. Oganessian, Ann. Rev. Nucl. Part. Sci. 63, 383 (2013).   
[6] S. Singh, R. K. Gupta, W. Scheid, and W. Greiner, J. Phys. G 18, 1243 (1992).   
[7] Y. T. Oganessian et al., Phys. Rev. C 76, 011601 (2007).   
[8] Y. T. Oganessian et al., Phys. Rev. Lett. 104, 142502 (2010).   
[9] P. A. Ellison et al., Phys. Rev. Lett. 105, 182701 (2010).   
[10] B. Abelev et al. (ALICE), J. Phys. G 41, 087001 (2014).   
[11] L. Ma et al., Phys. Rev. C 91, 051302 (2015).   
[12] S. Hofmann and G. Munzenberg, Rev. Mod. Phys. 72, 733 (2000).   
[13] G. Dodig-Crnkovic, F. A. Janouch, and R. J. Liotta, Nucl. Phys. A 501, 533 (1989).   
[14] K. Varga, R. G. Lovas, and R. J. Liotta, Phys. Rev. Lett. 69, 37 (1992).   
[15] G. Royer and B. Remaud, Nucl. Phys. A 444, 477 (1985).   
[16] H. Zhang, W. Zuo, J. Li, and G. Royer, Phys. Rev. C 74, 017304 (2006), arXiv:nuclth/0607060.   
[17] G. R¨opke, P. Schuck, B. Zhou, Y. Funaki, H. Horiuchi, Z. Ren, A. Tohsaki, C. Xu, and T. Yamada, Phys. Rev. C 90, 034304 (2014), arXiv:1407.0510 [nucl-th].   
[18] C. Xu, Z. Ren, G. R¨opke, P. Schuck, Y. Funaki, H. Horiuchi, A. Tohsaki, T. Yamada, and B. Zhou, Phys. Rev. C 93, 011306 (2016), arXiv:1511.07584 [nucl-th].   
[19] B. Buck, A. C. Merchant, and S. M. Perez, J. Phys. G 18, 10.1088/0954-3899/18/1/012.   
[20] B. Buck, A. C. Merchant, and S. M. Perez, Phys. Rev. C 45, 2247 (1992).   
[21] D. N. Poenaru and R. A. Gherghescu, Phys. Rev. C 94, 014309 (2016), arXiv:1604.00529 [nucl-th].

[22] V. Y. Denisov and H. Ikezoe, Phys. Rev. C 72, 064613 (2005), arXiv:nucl-th/0510082.   
[23] P. R. Chowdhury, C. Samanta, and D. N. Basu, Phys. Rev. C 73, 014612 (2006), arXiv:nuclth/0507054.   
[24] P. Roy Chowdhury, C. Samanta, and D. N. Basu, Phys. Rev. C 77, 044603 (2008), arXiv:0802.3837 [nucl-th].   
[25] D. N. Poenaru, H. St¨ocker, and R. A. Gherghescu, Eur. Phys. J. A 54, 14 (2018).   
[26] X.-Y. Zhu, S. Luo, W. Gao, L.-J. Qi, M. Li, X.-H. Li, and W.-B. Lin, Chin. Phys. C 48, 074102 (2024).   
[27] X.-Y. Zhu, W. Gao, L. Zhu, W.-J. Xing, X. Chen, W.-B. Lin, and X.-H. Li, Phys. Rev. C 112, 024329 (2025).   
[28] G. Gangopadhyay, J. Phys. G 36, 095105 (2009), arXiv:1007.1520 [nucl-th].   
[29] S. Guo, X. Bao, Y. Gao, J. Li, and H. Zhang, Nucl. Phys. A 934, 110 (2014).   
[30] J.-G. Deng and H.-F. Zhang, Phys. Rev. C 102, 044314 (2020).   
[31] J.-G. Deng, J.-C. Zhao, D. Xiang, and X.-H. Li, Phys. Rev. C 96, 024318 (2017), arXiv:1903.05366 [nucl-th].   
[32] J.-G. Deng, J.-C. Zhao, P.-C. Chu, and X.-H. Li, Phys. Rev. C 97, 044322 (2018), arXiv:1804.06010 [nucl-th].   
[33] J.-G. Deng and H.-F. Zhang, Phys. Lett. B 816, 136247 (2021).   
[34] S. Luo, D.-M. Zhang, L.-J. Qi, X. Chen, P.-C. Chu, and X.-H. Li, Chin. Phys. C 48, 044105 (2024).   
[35] W. J. Huang, M. Wang, F. G. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030002 (2021).   
[36] M. Wang, W. J. Huang, F. G. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003.   
[37] Y. He, L.-G. Pang, and X.-N. Wang, Phys. Rev. Lett. 122, 252302 (2019), arXiv:1808.05310 [hep-ph].   
[38] J. Wu, W. Ke, and X.-N. Wang, Phys. Rev. C 108, 034911 (2023), arXiv:2304.06339 [hep-ph].   
[39] W.-J. Xing, S. Cao, and G.-Y. Qin, Phys. Lett. B 850, 138523 (2024), arXiv:2303.12485 [hep-ph].   
[40] M. Omana Kuttan, J. Steinheimer, K. Zhou, and H. Stoecker, Phys. Rev. Lett. 131, 202303 (2023), arXiv:2211.11670 [hep-ph].

[41] L. Zhu, X. Chen, K. Zhou, H. Zhang, and M. Huang, Phys. Rev. D 112, 026019 (2025), arXiv:2501.17763 [hep-ph].   
[42] Y.-L. Cheng, S. Shi, Y.-G. Ma, H. St¨ocker, and K. Zhou, Phys. Rev. C 107, 064909 (2023), arXiv:2301.03910 [nucl-th].   
[43] J. Novak, K. Novak, S. Pratt, J. Vredevoogd, C. Coleman-Smith, and R. Wolpert, Phys. Rev. C 89, 034917 (2014), arXiv:1303.5769 [nucl-th].   
[44] S. Pratt, E. Sangaline, P. Sorensen, and H. Wang, Phys. Rev. Lett. 114, 202301 (2015), arXiv:1501.04042 [nucl-th].   
[45] E. Sangaline and S. Pratt, Phys. Rev. C 93, 024908 (2016), arXiv:1508.07017 [nucl-th].   
[46] D. Everett et al. (JETSCAPE), Phys. Rev. Lett. 126, 242301 (2021), arXiv:2010.03928 [hepph].   
[47] H. M¨antysaari, B. Schenke, C. Shen, and W. Zhao, Phys. Lett. B 833, 137348 (2022), arXiv:2202.01998 [hep-ph].   
[48] B. Tang, J. Am. Stat. Assoc. 88, 1392 (1993).   
[49] M. D. Morris and T. J. Mitchell, J. Stat. Plann. Infer. 43, 381 (1995).   
[50] D. Foreman-Mackey, D. W. Hogg, D. Lang, and J. Goodman, Publ. Astron. Soc. Pac. 125, 306 (2013), arXiv:1202.3665 [astro-ph.IM].   
[51] N. J. McMillan, J. Sacks, W. J. Welch, and F. Gao, J. Biopharm. Stat. 9, 145.   
[52] J. Goodman and J. Weare, Commun. Appl. Math. Comput. Sc. 5, 65 (2010).   
[53] E. Shin, Y. Lim, C. H. Hyun, and Y. Oh, Phys. Rev. C 94, 024320 (2016), arXiv:1511.02555 [nucl-th].   
[54] G. Saxena, P. K. Sharma, and P. Saxena, Eur. Phys. J. A 60, 50 (2024), arXiv:2402.04970 [nucl-th].   
[55] N. Wan and J. Fan, Phys. Rev. C 104, 064320 (2021).