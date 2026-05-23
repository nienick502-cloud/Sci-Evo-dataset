# Machine Learning-Driven High-Precision Model for

# α-Decay Energy and Half-Life Prediction of

# Superheavy Nuclei

Qingning Yuan1, Panpan $\mathrm { Q i ^ { 1 } }$ , Xuanpen Xiao1, Xue Wang1, Juan $\mathrm { H e ^ { 1 } }$ , Guimei Long1, Zhengwei Duan1, Yangyan

Dai1, Runchao Yan1, Gongming $\mathrm { Y u ^ { * 1 } }$ , and Haitao Yang†2

1College of Physics and Technology, Kunming University, Kunming 650214, China

2College of Science, Zhaotong University, Zhaotong 657000, China

# Abstract

We develop a physics-informed machine-learning framework for predicting $\alpha$ -decay energies and half-lives across a broad range of nuclei. The approach is based on an eXtreme Gradient Boosting (XGBoost) regression model and incorporates physically motivated nuclear descriptors constructed from evaluated nuclear data and deformation tables. For half-life prediction, key structure-related features—including magic-number proximity, minimum orbital angular-momentum transfer, isospin asymmetry, and quadrupole deformation—are introduced to represent the dominant mechanisms governing $\alpha$ decay within a data-driven framework. Model performance for both the $Q _ { \alpha }$ and half-life prediction tasks is evaluated using five-fold cross-validation, which demonstrates strong predictive accuracy without evident overfitting. Benchmark comparisons with widely used empirical relations, including the Royer formula and the Universal Decay Law (UDL), show that the XGBoost model achieves systematically lower prediction errors while preserving the established systematics of $\alpha$ -decay observables. SHapley Additive exPlanations (SHAP) analysis further reveals that the leading contributions from decay-energy information, centrifugal hindrance, and shell-related effects follow physically consistent trends, supporting the interpretability of the learned relationships. These results indicate that gradient-boosting models equipped with physics-guided features provide an accurate and robust framework for describing $\alpha$ -decay systematics and for predicting half-lives in regions where experimental data remain scarce.

Keywords: $\alpha$ -decay,Machine learning,XGBoost,Half-life prediction,Nuclear structure.

# I. INTRODUCTION

The study of $\alpha$ decay dates back to the early stages of research on radioactivity. In 1899, Rutherford, while investigating uranium-series emissions, first distinguished a radiation component characterized by low penetration but strong ionization and termed it $\alpha$ radiation. Subsequent systematic experiments conducted in 1907–1908 further demonstrated that $\alpha$ particles are

doubly charged helium nuclei. This key discovery not only clarified the microscopic nature of radioactive emissions but also established an essential experimental foundation for the development of nuclear-structure models and for understanding nuclear stability. As experimental data continued to accumulate, the regularities underlying $\alpha$ decay gradually emerged, providing a solid basis for systematic investigations of $\alpha$ -decay behavior and for the later development of the quantum-tunneling description of nuclear $\alpha$ decay [1]–[3]. Consequently, $\alpha$ decay soon became not only an important subject in early nuclear physics but also a key phenomenon for revealing the structure and stability of atomic nuclei. Building on the accumulating experimental evidence, Geiger and Nuttall (1911) identified a clear correlation between the $\alpha$ -decay half-life and the decay energy. This observation led to the formulation of the Geiger–Nuttall law, which states that the logarithm of the $\alpha$ -decay half-life exhibits an approximately linear dependence on the inverse square root of the decay energy. The emergence of this empirical relation provided a crucial foundation for subsequent phenomenological descriptions of radioactive decay and significantly advanced the quantitative understanding of nuclear disintegration dynamics [4]–[6].

Following the empirical establishment of the Geiger–Nuttall law, the subsequent development of quantum mechanics provided a deeper physical interpretation of its underlying regularities. In 1928, Gamow introduced the pioneering quantum-tunneling model, which explained the emission of $\alpha$ particles as a consequence of their ability to penetrate the Coulomb barrier surrounding the daughter nucleus. Within this framework, the decay process is interpreted as the quantum tunneling of a preformed $\alpha$ particle through the potential barrier, naturally reproducing the characteristic exponential dependence of the half-life on the decay energy and providing a microscopic theoretical basis for the Geiger–Nuttall relation. This development marked an important transition toward a quantitative and microscopic understanding of nuclear $\alpha$ decay. Building upon Gamow’s theoretical insight, numerous empirical and semi-empirical formulas were subsequently proposed to predict the logarithm of $\alpha$ -decay half-lives, among which the Royer formula and the Universal Decay Law (UDL) have been widely applied in nuclear-structure and decay studies [7]–[10]. Continuous improvements driven by theoretical advances and the expansion of experimental databases have enhanced the predictive accuracy of these phenomenological models across broad regions of the nuclear chart. Nevertheless, their fixed functional forms limit the extent to which shell effects, nuclear deformation, and angular-momentum hindrance can be fully incorporated, motivating the exploration of approaches that integrate richer physical constraints or data-driven methodologies.Although these empirical formulations incorporate nucleon-parity effects and employ different parameter sets for distinct categories of nuclei, they often exhibit noticeable systematic deviations in low-energy regions or for nuclei far from the valley of stability. This limitation primarily arises because their parameters are fitted using experimental datasets densely concentrated near the stability line and at relatively high $Q _ { \alpha }$ values. In contrast, nuclei in low- $Q _ { \alpha }$ or more exotic regions frequently suffer from larger experimental uncertainties, which reduces both the reliability and the generalizability of these models.Moreover, lower $Q _ { \alpha }$ values correspond to significantly reduced barrier-penetration probabilities that exhibit exponential sensitivity to small variations in $Q _ { \alpha }$ . Consequently, even minor deviations in decay energy may lead to orders-of-magnitude discrepancies in half-life predictions. In addition, the simplified treatments of the potential barrier and tunneling dynamics adopted in these empirical approaches, though adequate within the fitted domains, tend to amplify prediction errors as the decay energy decreases, thereby further increasing their systematic deviations [11]–[13].

Recent advances in computational technologies have substantially enhanced data processing and analysis capabilities, thereby

accelerating the integration of machine-learning techniques across numerous scientific domains. In physics—where the objective is to uncover the fundamental properties of matter and the governing laws of natural phenomena—machine learning has increasingly emerged as a powerful tool for addressing complex problems. Traditional approaches that rely on mathematical modeling, experimental observation, and numerical simulation often face significant challenges when dealing with highdimensional phase spaces, multiscale systems, or strongly correlated phenomena. Under such circumstances, computational costs become prohibitive and accurate theoretical descriptions may be lacking, ultimately constraining both predictive accuracy and model generalizability [14]–[18]. In recent years, machine-learning techniques have been increasingly applied to the prediction of $\alpha$ -decay energies and half-lives. According to their modeling philosophy and algorithmic structure, existing studies can be broadly categorized into several methodological streams.

The first category comprises neural-network-based approaches, including artificial neural networks (ANN) and Bayesian neural networks (BNN). These models employ multi-layer nonlinear mappings to capture complex correlations among nuclearstructure descriptors. In particular, BNN frameworks additionally provide uncertainty quantification, which is valuable in extrapolative analyses of nuclear properties [19]–[24]. The second category includes kernel-based methods, such as Support Vector Machines (SVM) and Gaussian Process (GP) regression. These approaches perform nonlinear regression through kernel functions and are widely used in small- and medium-scale regression problems. In nuclear-physics-related applications, kernelbased models have also been explored for modeling complex physical observables. In particular, Gaussian Process models provide a natural probabilistic framework and allow predictive uncertainty estimation, which can be advantageous when dealing with limited experimental data [25]–[27]. The third category consists of ensemble tree-based methods, including gradientboosted decision tree algorithms and their variants. These methods iteratively construct decision-tree ensembles to minimize residual errors and have demonstrated strong generalization capability in structured tabular datasets [28], [29].The present work adopts the XGBoost framework, belonging to the ensemble tree-based family, while emphasizing the integration of physics-informed feature design and interpretability analysis. By explicitly incorporating shell-closure proximity, minimum orbital angular-momentum transfer $l _ { \mathrm { m i n } }$ , and deformation-related descriptors into the feature set, and by employing SHAPbased attribution analysis, the model not only achieves high predictive accuracy but also establishes a transparent connection between data-driven inference and the underlying physical mechanisms of $\alpha$ decay. Rather than replacing alternative machinelearning paradigms, the objective of this study is to provide a unified framework that balances predictive performance, physical consistency, and interpretability.

Despite recent progress in nuclear-decay modeling, most existing machine-learning approaches still face challenges related to limited precision control and susceptibility to overfitting or underfitting. Furthermore, systematic comparisons with classical empirical formulas across different energy regimes remain insufficient, hindering a comprehensive assessment of model performance. The interpretability of many machine-learning models also requires further improvement, as their internal decision mechanisms often lack clear connections to underlying nuclear-structure physics.

Furthermore, high-quality experimental data for exotic nuclei—particularly those far from the valley of stability or in low decay-energy regions—remain inherently scarce. This scarcity constrains not only the refinement of empirical models but also the development of robust and generalizable data-driven approaches. As a result, constructing models that can deliver

accurate and physically consistent predictions under limited-data conditions has become an essential objective in contemporary nuclear-decay research.

To address these challenges, this study introduces an integrated and interpretable machine-learning framework for the simultaneous prediction of $\alpha$ -decay energies and half-lives. The model is built upon the XGBoost regression algorithm and incorporates a set of physically motivated nuclear-structure features, including mass number, neutron–proton asymmetry, shell proximity quantified through magic-number distance, and the minimum angular-momentum transfer. Model performance is rigorously benchmarked against traditional empirical formulas, such as the Royer expression and the UDL, using both training and independent test sets. Furthermore, SHAP-based feature attribution is employed to elucidate the dominant physical mechanisms captured by the model, thereby enhancing interpretability and establishing clear connections between data-driven predictions and underlying $\alpha$ -decay physics.

This paper is organized as follows. Section 2 describes the XGBoost-based framework employed in this study, including feature construction, data preprocessing, and the overall training procedure. Section 3 presents a detailed analysis of the model’s performance in predicting $\alpha$ -decay energies and half-lives, together with comparisons against traditional empirical formulas and SHAP-based interpretations of the underlying physical trends. Finally, Section 4 summarizes the principal findings of this work.

# II. GENERAL FORMALISM

This section outlines the systematic modeling workflow adopted in this study, including the fundamental principles of the XGBoost method, the training strategy incorporating an early-stopping mechanism, the feature-engineering procedure, the model parameter configuration and analysis, and the benchmarking methodology against traditional empirical formulas. The nuclear properties used in this work—including decay energies, half-lives, and spin–parity assignments—are taken from the evaluated nuclear databases NUBASE2020 and AME2020 [30]–[32]. The quadrupole deformation parameters are adopted from the FRDM2012 deformation tables reported by Moller ¨ et al. [33]. All datasets undergo appropriate preprocessing before being utilized for both machine-learning training and empirical-formula evaluation.

Alpha decay is a quantum tunneling process in which a preformed $\alpha$ particle escapes the parent nucleus by penetrating the nuclear potential barrier. Its half-life can be described within the framework of Gamow theory, which employs the Wentzel– Kramers–Brillouin (WKB) approximation to evaluate the tunneling probability. In the standard WKB treatment, the $\alpha$ particle is assumed to be preformed inside the parent nucleus and subsequently tunnels through an effective potential barrier composed of nuclear attraction, Coulomb repulsion, and a centrifugal term. The tunneling probability is predominantly determined by the Gamow factor derived from the WKB approximation [13], [34], [35].

$$
P = \exp \left[ - \frac {2}{\hbar} \int_ {R _ {\mathrm {i n}}} ^ {R _ {\mathrm {o u t}}} \sqrt {2 \mu (V (r) - Q _ {\alpha})} d r \right], \tag {1}
$$

where $\mu$ is the reduced mass of the $\alpha$ particle–daughter nucleus system, defined as

$$
\mu = \frac {m _ {\alpha} m _ {d}}{m _ {\alpha} + m _ {d}}, \tag {2}
$$

where $m _ { \alpha }$ and $m _ { d }$ denote the masses of the emitted $\alpha$ particle and the daughter nucleus, respectively. The quantity $V ( r )$ represents the total interaction potential between the $\alpha$ particle and the daughter nucleus at a relative distance $r$ , including the Coulomb interaction, the nuclear proximity potential, and the centrifugal potential associated with the orbital angular momentum transfer. The decay energy $Q _ { \alpha }$ denotes the released $\alpha$ -decay energy.

The quantities $R _ { \mathrm { i n } }$ and $R _ { \mathrm { o u t } }$ correspond to the classical inner and outer turning points determined from the condition

$$
V (r) = Q _ {\alpha}. \tag {3}
$$

Specifically, the inner turning point $R _ { \mathrm { i n } }$ corresponds to the minimum separation between the $\alpha$ particle and the daughter nucleus at the touching configuration and is usually approximated as the sum of the nuclear radii of the daughter nucleus and the $\alpha$ particle,

$$
R _ {\text {i n}} = R _ {d} + R _ {\alpha}. \tag {4}
$$

The outer turning point $R _ { \mathrm { o u t } }$ is the larger root of the equation $V ( r ) = Q _ { \alpha }$ and represents the position where the kinetic energy of the emitted particle becomes zero. The interval $[ R _ { \mathrm { i n } } , R _ { \mathrm { o u t } } ]$ therefore defines the classically forbidden region through which the $\alpha$ particle tunnels quantum mechanically.

This formulation explicitly highlights the central role of the decay energy $Q _ { \alpha }$ in governing the tunneling probability, as variations in $Q _ { \alpha }$ enter exponentially and therefore exert a dominant influence on the resulting half-life. Following Ref. [13], the $\alpha$ -decay half-life can be expressed as:

$$
T _ {1 / 2} = \frac {\ln 2}{\lambda} = \frac {\ln 2}{\nu S _ {c} P}, \tag {5}
$$

where $\lambda$ denotes the decay constant, $\nu$ is the assault frequency, $P$ is the tunneling probability, and $S _ { c }$ represents the $\alpha$ -cluster preformation probability. As shown in Eqs. (1) and (5), even small variations in the input parameters can lead to changes of several orders of magnitude in the calculated half-life. This extreme sensitivity arises primarily from the exponential dependence of the penetration probability $P$ on the decay energy $Q _ { \alpha }$ . Consequently, any uncertainty in $Q _ { \alpha }$ propagates exponentially and introduces substantial uncertainty into the predicted half-life [36], [37].

Moreover, because $\alpha$ -decay half-lives typically span several orders of magnitude, this broad dynamic range presents significant challenges for data modeling and regression analysis. To enhance numerical stability and reduce the influence of extreme values during training, the present study adopts the base-10 logarithm of the half-life, $\log _ { 1 0 } T _ { 1 / 2 }$ , as the regression target [38], [39].

# A. The Mathematical Fundamentals of eXtreme Gradient Boosting

In this work, the Extreme Gradient Boosting (XGBoost) algorithm is employed as the regression framework for learning the nonlinear mapping between nuclear-structure features and decay observables. The selection of XGBoost is motivated by the characteristics of the present problem. The input variables consist of structured, physics-informed nuclear descriptors, including shell proximity, isospin asymmetry, angular-momentum transfer, and quadrupole deformation, for which gradientboosted decision trees have demonstrated strong performance. Moreover, $\alpha$ -decay datasets are typically moderate in size, and

XGBoost provides robust generalization through built-in regularization, shrinkage, and subsampling strategies. Importantly, tree-based ensemble models can naturally capture nonlinear interactions among physical quantities such as $Q _ { \alpha }$ , nuclear charge number $Z$ , and minimum angular momentum $l _ { \mathrm { m i n } }$ without requiring an assumed analytical functional form. XGBoost constructs its predictor as an additive ensemble of regression trees, where the model output for a given sample $\mathbf { x } _ { i }$ is expressed as [40], [41]:

$$
\hat {y} _ {i} = \sum_ {k = 1} ^ {K} f _ {k} \left(\mathbf {x} _ {i}\right), \quad f _ {k} \in \mathcal {F}, \tag {6}
$$

with $\mathcal { F }$ denoting the functional space of CART regression trees. Each tree $f _ { k }$ assigns a constant prediction to samples falling into the same leaf node, and can therefore be written as:

$$
f (\mathbf {x}) = w _ {q (\mathbf {x})}, \quad q: \mathbb {R} ^ {m} \rightarrow \{1, 2, \dots , L \}, \tag {7}
$$

where $L$ is the number of leaf nodes, $q ( \mathbf { x } )$ specifies the leaf index to which $\mathbf { x }$ is mapped, and $w _ { j }$ is the weight associated with the $j$ -th leaf. XGBoost employs a forward stagewise procedure, in which the model at iteration $t$ is obtained by adding a new tree $f _ { t }$ to the previous ensemble, such that [42]

$$
\hat {y} _ {i} ^ {(t)} = \hat {y} _ {i} ^ {(t - 1)} + f _ {t} (\mathbf {x} _ {i}). \tag {8}
$$

To suppress overfitting and enhance generalization, XGBoost minimizes a regularized objective function composed of a training loss and a structural penalty on the regression trees [43], [44]:

$$
\mathcal {L} ^ {(t)} = \sum_ {i} l \left(y _ {i}, \hat {y} _ {i} ^ {(t)}\right) + \sum_ {k = 1} ^ {t} \Omega \left(f _ {k}\right). \tag {9}
$$

In the present study the mean-squared-error loss is adopted,

$$
l \left(y _ {i}, \hat {y} _ {i}\right) = \frac {1}{2} \left(y _ {i} - \hat {y} _ {i}\right) ^ {2}, \tag {10}
$$

while the regularization term penalizes overly complex trees via

$$
\Omega \left(f _ {t}\right) = \gamma L _ {t} + \frac {1}{2} \lambda \sum_ {j = 1} ^ {L _ {t}} w _ {t j} ^ {2}, \tag {11}
$$

where $L _ { t }$ denotes the number of leaf nodes in tree $f _ { t }$ , $\gamma$ controls the creation of new leaves, and $\lambda$ regulates the magnitude of leaf weights. Since only $f _ { t }$ is newly introduced at iteration $t$ , the loss contribution of this tree is isolated by expanding the objective using a second-order Taylor approximation around the previous prediction $\hat { y } _ { i } ^ { ( t - 1 ) }$ [45], [46]:

$$
l \left(y _ {i}, \hat {y} _ {i} ^ {(t - 1)} + f _ {t} (\mathbf {x} _ {i})\right) \approx l \left(y _ {i}, \hat {y} _ {i} ^ {(t - 1)}\right) + g _ {i} f _ {t} (\mathbf {x} _ {i}) + \frac {1}{2} h _ {i} f _ {t} ^ {2} (\mathbf {x} _ {i}), \tag {12}
$$

where

$$
g _ {i} = \left. \frac {\partial l}{\partial \hat {y}} \right| _ {\hat {y} _ {i} ^ {(t - 1)}}, \quad h _ {i} = \left. \frac {\partial^ {2} l}{\partial \hat {y} ^ {2}} \right| _ {\hat {y} _ {i} ^ {(t - 1)}}, \tag {13}
$$

and for the MSE loss employed here, $g _ { i } = \hat { y } _ { i } ^ { ( t - 1 ) } - y _ { i }$ and $h _ { i } = 1$ . Substituting Eq. (12) into Eq. (9) and discarding constants

yields the approximate objective for optimizing the new tree:

$$
\tilde {\mathcal {L}} ^ {(t)} = \sum_ {i} \left[ g _ {i} f _ {t} (\mathbf {x} _ {i}) + \frac {1}{2} h _ {i} f _ {t} ^ {2} (\mathbf {x} _ {i}) \right] + \Omega (f _ {t}). \tag {14}
$$

Since $f _ { t } ( \mathbf { x } _ { i } ) = w _ { j }$ for all samples belonging to leaf $j$ , let $I _ { j } = \{ i | q ( \mathbf { x } _ { i } ) = j \}$ denote the index set of samples falling into this leaf. Defining the aggregated first- and second-order gradients as

$$
G _ {j} = \sum_ {i \in I _ {j}} g _ {i}, \quad H _ {j} = \sum_ {i \in I _ {j}} h _ {i}, \tag {15}
$$

the objective Eq. (14) becomes

$$
\tilde {\mathcal {L}} ^ {(t)} = \sum_ {j = 1} ^ {L _ {t}} \left[ G _ {j} w _ {j} + \frac {1}{2} \left(H _ {j} + \lambda\right) w _ {j} ^ {2} \right] + \gamma L _ {t}. \tag {16}
$$

Minimizing this expression with respect to each leaf weight yields the optimal solution [28], [47]:

$$
w _ {j} ^ {*} = - \frac {G _ {j}}{H _ {j} + \lambda}, \tag {17}
$$

and substituting Eq. (17) into Eq. (16) leads to the so-called structure score that evaluates the quality of a given tree structure [48]:

$$
\tilde {\mathcal {L}} _ {\text {s t r u c t}} = - \frac {1}{2} \sum_ {j = 1} ^ {L _ {t}} \frac {G _ {j} ^ {2}}{H _ {j} + \lambda} + \gamma L _ {t}. \tag {18}
$$

When considering a candidate split that divides a leaf $I$ into left and right subsets $I _ { L }$ and $I _ { R }$ , with corresponding gradient sums $\left( G _ { L } , H _ { L } \right)$ and $\left( G _ { R } , H _ { R } \right)$ , the improvement in the structure score is quantified by the split gain [40]:

$$
\operatorname {G a i n} = \frac {1}{2} \left[ \frac {G _ {L} ^ {2}}{H _ {L} + \lambda} + \frac {G _ {R} ^ {2}}{H _ {R} + \lambda} - \frac {\left(G _ {L} + G _ {R}\right) ^ {2}}{H _ {L} + H _ {R} + \lambda} \right] - \gamma . \tag {19}
$$

This quantity serves as the criterion for determining whether a proposed split is beneficial, and therefore governs the treegrowing process in XGBoost.

# B. Data input and feature engineering construction

All nuclear properties employed in this study—including proton number $Z$ , neutron number $N$ , $\alpha$ -decay energy $Q _ { \alpha }$ , spin– parity assignments $( J ^ { \pi } )$ , and experimentally measured half-lives $T _ { 1 / 2 }$ —were taken from the evaluated nuclear databases NUBASE2020 and AME2020 [30]–[32]. Quadrupole deformation parameters $\beta _ { 2 }$ were adopted from the FRDM2012 deformation tables [33].

Two datasets were constructed for the present study. For the $Q _ { \alpha }$ prediction task, a total of 1623 nuclei with experimentally evaluated $Q _ { \alpha } > 0$ were retained, covering the region $5 0 \leq Z \leq 1 1 8$ of the nuclear chart.

For the half-life prediction task, a dataset containing 498 nuclei with proton numbers in the range $6 4 \leq Z \leq 1 1 8$ was constructed. All nuclei included in this dataset possess experimentally measured half-lives $T _ { 1 / 2 }$ and the complete set of structural quantities required for feature construction. Entries with missing essential nuclear information or undefined structural descriptors were uniformly excluded to ensure consistency of the input feature space. The corresponding experimental $\alpha$ -decay

energies span the interval $2 . 2 0 \leq Q _ { \alpha } \leq 1 1 . 8 4 ~ \mathrm { M e V } ,$ , reflecting the range covered by the available experimental data satisfying the adopted data-quality criteria. To provide a transparent overview of the data coverage and density across different regions of the nuclear chart, Figure 1 presents the distributions of $Q _ { \alpha }$ , $\log _ { 1 0 } ( T _ { 1 / 2 } )$ , and the mass number $A$ for the nuclei included in the half-life dataset.

![](images/944416473d78822a38cfb71d9f0b3383e2da61da3e07f3abe8f6bc218df92b90.jpg)  
(a)

![](images/0947f5335b37d206bd95391c83743cc9c8cc205c960656928bde8572dab07132.jpg)  
(b)

![](images/d476387a01d4a390e57e1e90208227dc8bfaaeaf7dc8c59e5200c5427cc2a000.jpg)  
(c)   
Fig. 1: Distributions of (a) mass number $A$ , (b) logarithmic half-life $\log _ { 1 0 } ( T _ { 1 / 2 } )$ , and (c) $\alpha$ -decay energy $Q _ { \alpha }$ for the nuclei included in the half-life dataset. The continuous coverage across the considered intervals provides a transparent overview of the data density in different regions of the nuclear chart.

The overall modeling workflow consists of two conceptually independent components addressing distinct physical observables. One component employs an XGBoost-based regression model to predict the $\alpha$ -decay energy $Q _ { \alpha }$ , aiming to capture the nonlinear relationship between nuclear-structure features and decay energy release. The other component independently models the $\alpha$ -decay half-life by incorporating experimentally measured decay energies together with nuclear-structure parameters, enabling a direct investigation of the physical factors governing $T _ { 1 / 2 }$ without introducing uncertainty propagation from decayenergy prediction.

1) Decay Energy Prediction: To predict the decay energy, five nuclear-structure descriptors were employed as input variables for the model. Their definitions are summarized in Table 1.

These variables reflect the fundamental nuclear properties and nucleon configurations within atomic nuclei. Although the mass number $A$ is mathematically related to the proton number $Z$ and the neutron number $N$ through $A = Z + N$ , these quantities are not redundant from a physical perspective. Instead, they correspond to different aspects of nuclear structure: the proton number $Z$ is closely associated with Coulomb effects and proton shell structure, the neutron number $N$ characterizes isotopic systematics and neutron shell properties, while the mass number $A$ is related to the overall nuclear size and mass

Table 1: Decay-energy prediction related features used in the model.   

<table><tr><td>Name</td><td>Relevant Calculations</td></tr><tr><td>Mass number</td><td>A</td></tr><tr><td>Proton number</td><td>Z</td></tr><tr><td>Neutron number</td><td>N</td></tr><tr><td>Proton-neutron ratio</td><td>Z/N</td></tr><tr><td>Relative neutron excess</td><td>(N-Z)/A</td></tr></table>

scale. As key structural variables governing nuclear binding and decay behavior, they exhibit pronounced nonlinear correlations with the decay energy, a relationship well supported by both the liquid-drop model and shell-model frameworks [49], [50]. Additional tests indicate that removing any one of these variables, while keeping the remaining features unchanged, leads to a slight decrease in predictive accuracy. This result suggests that retaining these fundamental nuclear descriptors helps the model capture systematic nuclear-structure trends more effectively. Maintaining a consistent set of input features across light, heavy, and superheavy mass regions further improves the generalizability of the model over the entire nuclear chart.

In this study, nuclides with positive decay energies ( $Q _ { \alpha } > 0 ,$ ) were collected to construct the dataset used for the $Q _ { \alpha }$ prediction task. To obtain a reliable estimate of the predictive performance, a five-fold cross-validation strategy was adopted. Specifically, the dataset was randomly divided into five mutually exclusive subsets of approximately equal size. In each fold, four subsets were used for model training and the remaining subset was used for testing, so that every nucleus was evaluated once as independent test data. The final performance metrics were reported as the mean and standard deviation over the five folds. The results indicate that the proposed model possesses strong predictive capability, and the detailed numerical results together with the SHAP-based interpretability analysis will be discussed in the following section.

2) Half-life Prediction: This stage constitutes the core component of the methodological framework developed in this study. In this part, the $\alpha$ -decay half-life regression model is constructed by incorporating the decay energy $Q _ { \alpha }$ together with multiple nuclear-structure features. The $Q _ { \alpha }$ values are taken from the AME2020 atomic mass evaluation, and the half-life data are adopted from the NUBASE 2020 database, both of which are based on experimentally measured or systematically evaluated nuclear data. The machine-learning model directly performs regression on the experimentally measured $\log _ { 1 0 } T _ { 1 / 2 }$ values, without employing residual corrections to empirical formulas or theoretical model predictions as training targets. The model takes physics-informed nuclear descriptors as input features and establishes a nonlinear mapping to the decay observables. The deformation parameters are extracted from the FRDM(2012) nuclear mass and deformation database, and are used solely as structural input features rather than for generating decay observables. All feature parameters employed in the half-life prediction task are summarized in Table 2.

In the feature system constructed for this study, the mass number $A _ { 1 }$ , neutron number $N _ { 1 }$ , and proton number $Z _ { 1 }$ of the parent nucleus serve as fundamental structural quantities. These variables determine the position of a nucleus on the nuclear chart and encode essential information on nuclear size, isospin asymmetry, and shell structure, thereby playing an important role in the description of $\alpha$ -decay dynamics.

Beyond these basic attributes, several additional physically motivated quantities are introduced to characterize the key

Table 2: Physics-informed feature set used in the half-life prediction model.   

<table><tr><td>Name</td><td>Relevant Calculations</td></tr><tr><td>Coulomb-energy coupling descriptor</td><td>Z1/√Qα</td></tr><tr><td>Proton number of the parent nucleus</td><td>Z1</td></tr><tr><td>Neutron number of the parent nucleus</td><td>N1</td></tr><tr><td>Mass number of the parent nucleus</td><td>A1</td></tr><tr><td>Neutron-proton ratio of the parent nucleus</td><td>N1/Z1</td></tr><tr><td>Relative neutron excess of the parent nucleus</td><td>(N1-Z1)/A1</td></tr><tr><td>Minimum orbital angular momentum</td><td>ℓmin</td></tr><tr><td>Quadrupole deformation term</td><td>√κ2β2</td></tr><tr><td>Distance to the nearest proton shell closure</td><td>|Z1-magic|min</td></tr></table>

mechanisms governing the decay process. These include the Coulomb–energy coupling term $Z _ { 1 } / \sqrt { Q _ { \alpha } }$ , the minimum orbital angular momentum $\ell _ { \mathrm { m i n } }$ required for $\alpha$ emission, indicators of isospin asymmetry, shell-structure descriptors, and deformationrelated parameters. Together, these quantities allow the model to incorporate both decay-energy dependence and nuclear-structure effects within a unified feature framework [51]–[53].

Among these features, the minimum orbital angular momentum $\ell _ { \mathrm { m i n } }$ required for $\alpha$ emission represents an important descriptor of the centrifugal barrier. Its value is determined by the coupling between the spins $( j _ { p } , j _ { d } )$ and parities $( \pi _ { p } , \pi _ { d } )$ of the parent and daughter nuclei and follows the selection rules [54]:

$$
\ell_ {\min } = \left\{ \begin{array}{l l} \Delta_ {j}, & \text {i f} \Delta_ {j} \text {i s e v e n a n d} \pi_ {p} = \pi_ {d}, \\ \Delta_ {j} + 1, & \text {i f} \Delta_ {j} \text {i s e v e n a n d} \pi_ {p} \neq \pi_ {d}, \\ \Delta_ {j}, & \text {i f} \Delta_ {j} \text {i s o d d a n d} \pi_ {p} \neq \pi_ {d}, \\ \Delta_ {j} + 1, & \text {i f} \Delta_ {j} \text {i s o d d a n d} \pi_ {p} = \pi_ {d}, \end{array} \right. \quad \Delta_ {j} = | j _ {p} - j _ {d} |. \tag {20}
$$

This quantity represents the lowest orbital angular momentum transfer compatible with angular-momentum and parity conservation. Larger values of $\ell _ { \mathrm { m i n } }$ increase the effective barrier through the centrifugal term, thereby reducing the tunneling probability and extending the $\alpha$ -decay half-life. The inclusion of $\ell _ { \mathrm { m i n } }$ therefore enables the model to account for the wellestablished angular-momentum hindrance effect observed in $\alpha$ -decay systematics.

The relative neutron excess $( N _ { 1 } - Z _ { 1 } ) / A _ { 1 }$ and the neutron-to-proton ratio $N _ { 1 } / Z _ { 1 }$ are introduced to characterize the isospin asymmetry of the parent nucleus. These quantities are closely related to the symmetry-energy term in the liquid-drop model and therefore provide important information on nuclear binding and structural stability. Their variations reflect the degree to which a nucleus deviates from the valley of stability.

For neutron-rich nuclides located far from stability, isospin asymmetry significantly influences the shape of the decay barrier and the preformation probability of the $\alpha$ cluster, thereby affecting the decay behavior [55], [56]. Incorporating these asymmetryrelated descriptors into the feature set allows the model to better capture systematic trends along isotopic chains and improves

the prediction accuracy for exotic and weakly bound nuclei.

To characterize the proximity of the parent nucleus to proton shell closures, we introduce the minimum proton magicnumber distance $\Delta Z _ { \mathrm { m a g i c } }$ , which quantifies the influence of shell structure on the $\alpha$ -decay half-life [57]–[59]. The proton magic numbers considered in this work are 2, 8, 20, 28, 50, 82, and 114. Nuclei located near shell closures generally possess enhanced binding energy and increased structural stability, which significantly affect the shape of the decay barrier and the preformation probability of the $\alpha$ cluster. Thus, this feature effectively strengthens the model’s sensitivity to shell effects.

To further examine the impact of nuclear deformation on the $\alpha$ -decay half-life, a deformation-related correction term $\sqrt { \kappa _ { 2 } \beta _ { 2 } }$ is introduced. Not all nuclei possess perfectly spherical shapes; for the majority of medium and heavy nuclei, spontaneous symmetry breaking leads to noticeable deformation, which manifests as a pronounced electric quadrupole moment. The nuclear surface is often parametrized by standard deformation variables, among which the quadrupole deformation parameter $\beta _ { 2 }$ is the simplest and most influential, as it governs the dominant deformation effects on the decay barrier [60]–[65]. In the present work, $\beta _ { 2 }$ refers to the quadrupole deformation parameter of the parent nucleus.

To describe the contribution of quadrupole deformation in the parent nucleus, different values of the coefficient $\kappa _ { 2 }$ are assigned according to the deformation type: $\kappa _ { 2 } = 2$ for prolate shapes $\beta _ { 2 } > 0 )$ ), $\kappa _ { 2 } = - 1$ for oblate shapes $\beta _ { 2 } < 0 ,$ , and $\kappa _ { 2 } = 0$ when the nucleus is nearly spherical $\beta _ { 2 } = 0$ ). This assignment is designed to embed, within the empirical modeling framework, the qualitative influence of distinct deformation modes on the $\alpha$ -decay half-life.

By combining the deformation sign information $\left( \kappa _ { 2 } \right)$ ) with the deformation magnitude $( \beta _ { 2 } )$ , the constructed term $\sqrt { \kappa _ { 2 } \beta _ { 2 } }$ effectively captures the modification of the half-life arising from deformation-induced changes in the Coulomb barrier [66]– [68]. Incorporating this feature enhances the model’s sensitivity to barrier-geometry effects and improves its physical consistency across nuclei exhibiting different deformation characteristics.

The selection of these features is grounded in well-established nuclear-physics models, enabling a deeper understanding of nuclear structural stability and the underlying mechanisms governing $\alpha$ -decay. By systematically incorporating key physical effects—such as shell structure, isospin asymmetry, angular-momentum conservation, and nuclear deformation—into the feature space, the model achieves enhanced predictive accuracy and improved physical consistency. This physically informed feature design further strengthens the generalization capability of our half-life framework and provides a more robust basis for interpreting the model’s predictions.

To ensure a robust and reliable evaluation of model performance, the same five-fold cross-validation strategy described in the $Q _ { \alpha }$ prediction task was adopted for the half-life regression model. In each fold, four subsets were used for training and the remaining subset was used for testing, and the final performance metrics were reported as the mean and standard deviation over the five folds. Within each cross-validation fold, $10 \%$ of the training data were further separated as a validation subset. Early stopping was implemented based on the validation RMSE, and the training process was terminated if no improvement was observed for 200 consecutive boosting rounds. The model parameters corresponding to the lowest validation RMSE were retained. In addition, a fixed random seed was used throughout the training process to ensure the reproducibility of the results. This procedure helps prevent overfitting and improves the stability of the training process. The detailed predictive performance of the model, together with the SHAP-based interpretability analysis, is presented in Section 3.

Table 3: Hyperparameter configuration of the XGBoost model used in the $\alpha$ -decay half-life prediction task.   

<table><tr><td>Hyperparameter</td><td>Value</td></tr><tr><td>Number of estimators (n_estimators)</td><td>1600</td></tr><tr><td>Learning rate</td><td>0.03</td></tr><tr><td>Maximum tree depth (max_depth)</td><td>4</td></tr><tr><td>Minimum child weight (min_child_weight)</td><td>6</td></tr><tr><td>Subsample ratio (subsample)</td><td>0.85</td></tr><tr><td>Column sample by tree (colsample_bytree)</td><td>0.85</td></tr><tr><td>Gamma (γ)</td><td>0.10</td></tr><tr><td>L1 regularization (α)</td><td>0.8</td></tr><tr><td>L2 regularization (λ)</td><td>5.0</td></tr><tr><td>Early stopping rounds</td><td>200</td></tr></table>

During model training, the hyperparameters of the XGBoost model were kept fixed and consistently applied across all cross-validation folds to ensure the stability and reproducibility of the training procedure. The model was trained using the Pseudo-Huber loss function together with a histogram-based tree construction algorithm. The main hyperparameters include the learning rate, maximum tree depth, subsample ratio, column sampling ratio, minimum child weight, and regularization coefficients. In addition, early stopping based on the validation RMSE was employed to prevent overfitting during training. The complete hyperparameter configuration is summarized in Table 3, and the same settings were used across all cross-validation folds.

# C. Empirical Formulas (Royer and Universal Decay Law)

In studies of $\alpha$ -decay half-lives, empirical formulas with compact analytical forms are widely employed for rapid estimation owing to their computational efficiency. Such models frequently serve as benchmark references for theoretical frameworks, where nuclide classification schemes are often incorporated to improve predictive performance. Although they do not explicitly describe all microscopic mechanisms, they continue to play a central role in systematics-based investigations of nuclear decay.

In this work, we adopt two of the most widely used and continuously refined empirical formulations: the Royer formula and the Universal Decay Law (UDL). A brief introduction to their analytical structures is provided in this section, and both will be utilized as comparative benchmarks in subsequent analyses to evaluate the physical consistency and predictive capability of our machine-learning framework.

1) Royer Formula: The Royer formula, originally proposed by G. Royer, is derived from the liquid-drop model and subsequently fitted to extensive experimental datasets [7]–[9], [33]. This empirical expression is applicable to nuclides with different proton–neutron parity combinations, and its general form is given by:

$$
\log_ {1 0} \left(T _ {1 / 2} ^ {\text {R o y e r}} (s)\right) = a + b A ^ {1 / 6} \sqrt {Z} + \frac {c Z}{\sqrt {Q _ {\alpha}}}, \tag {21}
$$

Table 4: Coefficients in the Royer formula.   

<table><tr><td>Nuclei</td><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>e-e</td><td>-25.3100</td><td>-1.1629</td><td>1.5864</td><td>-0.0106</td></tr><tr><td>e-o</td><td>-26.6500</td><td>-1.0859</td><td>1.5848</td><td>-0.0186</td></tr><tr><td>o-e</td><td>-25.6800</td><td>-1.1423</td><td>1.5920</td><td>0.0156</td></tr><tr><td>o-o</td><td>-20.4800</td><td>-1.1130</td><td>1.6971</td><td>-0.0223</td></tr></table>

to extend the applicability of the Royer expression to $\alpha$ -decay processes involving non-zero angular momentum transfer, G. Royer and collaborators introduced an angular-momentum correction term. Furthermore, to account for the influence of nuclear deformation on the $\alpha$ -decay half-life, an additional quadrupole deformation term associated with the parent nucleus is incorporated into the formulation. Accordingly, in the present study we adopt the modified Royer expression reported in Refs. [12], [33], [64], [65], [68] as the empirical benchmark for comparison.

$$
\log_ {1 0} \left(T _ {1 / 2} ^ {\text {R o y e r}} (s)\right) = a + b A ^ {1 / 6} \sqrt {Z} + \frac {c Z}{\sqrt {Q _ {\alpha}}} + \frac {\ell (\ell + 1)}{\sqrt {(A - 4) (Z - 2)} A ^ {2 / 3}} + d \sqrt {\kappa_ {2} \beta_ {2}} \frac {Z}{\sqrt {Q _ {\alpha}}}, \tag {22}
$$

Here, A denotes the mass number of the parent nucleus, $Z$ is the proton number, and $Q _ { \alpha }$ represents the decay energy. The determination of $\kappa _ { 2 }$ follows exactly the same convention described earlier, and the same rule also applies to the UDL formulation. The coefficients $a , b , c .$ , and $d$ are fitted parameters whose values depend on the even–odd structure of the parent nucleus. The corresponding parameter sets for the four nucleon-parity classifications (e–e, e–o, o–e, and o–o) are summarized in Table 4.

2) Universal Decay Law Formula: The UDL formula offers several significant advantages. Unlike purely empirical expressions, it is derived from a clear physical foundation that encapsulates the essential mechanism of barrier penetration in radioactive decay. Moreover, the UDL provides a unified description for both $\alpha$ decay and heavier cluster radioactivities, enabling consistent application across different decay modes within a single theoretical framework. It also exhibits strong predictive performance for even–even, odd–even, and odd–odd nuclei, and can be reliably extrapolated to the superheavy region, offering valuable insights into the structural stability of newly synthesized elements [10], [68], [69].

$$
\log_ {1 0} \left(T _ {1 / 2} ^ {\mathrm {U D L}} (s)\right) = a \frac {\sqrt {\mu} Z _ {\alpha} Z _ {d}}{\sqrt {Q _ {\alpha}}} + b \left[ \sqrt {\mu} Z _ {\alpha} Z _ {d} \left(A _ {\alpha} ^ {1 / 3} + A _ {d} ^ {1 / 3}\right) \right] ^ {1 / 2} + c + d \ell (\ell + 1) + e I + f I ^ {2}. \tag {23}
$$

Similarly, by incorporating the quadrupole deformation parameter $\beta _ { 2 }$ into the original UDL formulation, nuclear shape effects can be further embedded within the empirical description. This modification enables a more comprehensive representation of deformation-induced changes in the decay barrier and consequently the half-life. The resulting expression takes the following form [33], [64], [65], [68]:

$$
\begin{array}{l} \log_ {1 0} \left(T _ {1 / 2} ^ {\mathrm {U D L}} (s)\right) = a \sqrt {\mu Z _ {\alpha} Z _ {d}} \frac {1}{\sqrt {Q _ {\alpha}}} + b \left[ \sqrt {\mu Z _ {\alpha} Z _ {d}} \left(A _ {\alpha} ^ {1 / 3} + A _ {d} ^ {1 / 3}\right) \right] ^ {1 / 2} \tag {24} \\ + c + d \ell (\ell + 1) + e I + f I ^ {2} + g \sqrt {\kappa_ {2} \beta_ {2}} \frac {Z}{\sqrt {Q _ {\alpha}}}. \\ \end{array}
$$

Table 5: Coefficients used in the empirical $\alpha$ -decay half-life formula for different odd–even combinations of parent nuclei.   

<table><tr><td>Nuclei</td><td>a</td><td>b</td><td>c</td><td>d</td><td>e</td><td>f</td><td>g</td></tr><tr><td>e-e</td><td>0.4226</td><td>-0.5582</td><td>-25.116</td><td>0</td><td>2.5165</td><td>-27.929</td><td>-0.0183</td></tr><tr><td>e-o</td><td>0.4290</td><td>-0.5504</td><td>-25.916</td><td>0.04578</td><td>-15.408</td><td>43.457</td><td>-0.0218</td></tr><tr><td>o-e</td><td>0.4275</td><td>-0.5428</td><td>-24.855</td><td>0.0135</td><td>-16.031</td><td>32.542</td><td>-0.0085</td></tr><tr><td>o-o</td><td>0.4341</td><td>-0.5424</td><td>-26.0589</td><td>0.0401</td><td>-6.7131</td><td>14.46</td><td>-0.0235</td></tr></table>

Table 6: Five-fold cross-validation results of the XGBoost model for $Q _ { \alpha }$ prediction. The error metrics (RMSE and MAE) are reported in MeV.   

<table><tr><td>Metric</td><td>Training (mean ± std)</td><td>Testing (mean ± std)</td></tr><tr><td>RMSE</td><td>0.2403 ± 0.0121</td><td>0.2971 ± 0.0430</td></tr><tr><td>MAE</td><td>0.1147 ± 0.0053</td><td>0.1765 ± 0.0114</td></tr><tr><td>R²</td><td>0.9936 ± 0.0006</td><td>0.9901 ± 0.0024</td></tr></table>

Among the terms appearing in the UDL expression, $Z _ { \alpha } = 2$ and $A _ { \alpha } = 4$ denote the proton number and mass number of the emitted $\alpha$ particle, respectively. The quantities $Z _ { d }$ and $A _ { d }$ represent the proton number and mass number of the daughter nucleus, defined as $Z _ { d } = Z - Z _ { \alpha }$ and $A _ { d } = A - A _ { \alpha }$ . The quantity $I = ( N - Z ) / A$ characterizes the relative neutron excess of the parent nucleus and reflects the isospin asymmetry of the nuclear system. The fitting coefficients of the UDL formula depend on the even–odd parity combination of the parent nucleus’s proton and neutron numbers, corresponding to four distinct cases summarized in Table 5.

Both empirical formulations—the Royer model and the UDL—have undergone extensive validation in $\alpha$ -decay systematics. Although they cannot fully reproduce all microscopic mechanisms, they provide essential phenomenological frameworks for understanding global decay trends. Building upon these foundations, we subsequently generate half-life predictions using both empirical models and perform a comprehensive comparative analysis against the results obtained from our machine learning framework.

# III. RESULTS AND DISCUSSION

# A. Decay Energy Prediction Performance

To quantitatively evaluate the predictive performance of the decay-energy model, the key error metrics obtained from the five-fold cross-validation procedure are summarized in Table 6. The results are reported as the mean and standard deviation over the five folds. The model achieves consistently high predictive accuracy with only small differences between the training and testing folds, indicating strong generalization capability and no evidence of significant overfitting.

The results show that the XGBoost model maintains very high predictive accuracy across different data partitions. Although the testing errors are slightly larger than the training errors, the overall error level remains low and the standard deviations across the five folds are small, demonstrating the stability and robustness of the model when applied to unseen nuclei.

Having obtained stable and physically consistent decay-energy predictions, it is important to further investigate the physical factors that the model relies on during the learning process. To this end, the SHAP framework was employed to perform a

Table 7: Overall prediction errors of the Royer and UDL formulas on the full $\alpha$ -decay dataset, evaluated for $\log _ { 1 0 } ( T _ { 1 / 2 } ( s ) )$ .   

<table><tr><td>Model</td><td>RMSE</td><td>MAE</td></tr><tr><td>UDL formula</td><td>0.8887</td><td>0.6839</td></tr><tr><td>Royer formula</td><td>3.0897</td><td>1.4727</td></tr></table>

feature-importance analysis, enabling a quantitative evaluation of the contributions of different nuclear-structure descriptors to the predicted decay energies. The interpretability results are shown in Figure 2.

![](images/6906821dcea51780744743d8eff59e8bee4aa9b4497de21c6ef9724cf9ec0ba5.jpg)  
Fig. 2: SHAP summary plot showing the feature-importance distribution in the decay-energy prediction model. The horizontal axis represents SHAP values, indicating the contribution of each feature to the model output. Each point corresponds to a single prediction sample and is colored according to the feature value from low (blue) to high (red).

Figure 2 presents the SHAP feature-importance distribution for the decay-energy prediction task. The model primarily relies on the proton number $Z$ , neutron number $N$ , mass number $A$ , and symmetry-energy-related quantities such as $Z / N$ and the relative neutron excess. The importance ranking of these features is consistent with expectations from the liquid-drop model and shell-model descriptions of nuclear binding energies, indicating that the model successfully captures the known systematic behavior governing $Q _ { \alpha }$ values.

Overall, the essential nuclear-structure information relevant to $Q _ { \alpha }$ is effectively captured, demonstrating the model’s capability to learn physically meaningful correlations within decay-energy systematics.

# B. Half-Life Prediction Performance

To quantify the baseline performance of traditional analytical approaches, we evaluate the Royer and UDL formulas on the full $\alpha$ -decay dataset considered in this work. The corresponding global prediction errors are summarized in Table 7. These values represent the typical level of accuracy achievable by widely used empirical relations. As expected, the UDL formula exhibits substantially better overall performance than the Royer expression, reflecting its more comprehensive incorporation of decay-systematics trends. These baseline results provide a quantitative reference for evaluating the performance of the machine-learning model introduced below.

For the half-life prediction task, a regression model is constructed by combining decay-energy information with multiple nuclear-structure features. To systematically evaluate the predictive performance of the model, three key metrics— $\cdot R ^ { 2 }$ , RMSE, and MAE—are calculated within a five-fold cross-validation framework. The results, summarized in Table 8, show that the

Table 8: Five-fold cross-validation results of the XGBoost model for $\alpha$ -decay half-life prediction. The error metrics (RMSE and MAE) are evaluated for $\log _ { 1 0 } ( T _ { 1 / 2 } ( s ) )$ .   

<table><tr><td>Metric</td><td>Training (mean ± std)</td><td>Testing (mean ± std)</td></tr><tr><td>RMSE</td><td>0.5231 ± 0.0630</td><td>0.7845 ± 0.1622</td></tr><tr><td>MAE</td><td>0.3648 ± 0.0112</td><td>0.4882 ± 0.0469</td></tr><tr><td>R²</td><td>0.9906 ± 0.0023</td><td>0.9780 ± 0.0137</td></tr></table>

model maintains consistently high predictive accuracy across different data partitions. The relatively small variations of the evaluation metrics among the folds indicate stable model performance under different data splits. Meanwhile, the model also retains high predictive accuracy for nuclei that are not involved in the training process, suggesting good generalization capability of the proposed approach.

The improvement of the XGBoost model relative to the Royer and UDL formulas can be clearly observed in both the quantitative performance metrics (Table 8) and the model–data comparison plots shown in Figure 3. In particular, the machinelearning predictions exhibit a noticeably tighter distribution around the ideal relation $y = x$ , indicating that the model more accurately captures the systematic behavior of $\alpha$ -decay half-lives across the considered nuclear region.

![](images/e50a624c5c0d5e6870cd8f415a7d2348e6fda6fe61283ff929f63ddb296481e8.jpg)

![](images/55ce45dad5c4339cb8a2ebcfe37aa9da3fa7f3a30fca1bda6d7b312c164764d2.jpg)

![](images/3142fdaa121a1bc9bd4268426eeb4e9788881e02c288326ec21cb5b556da0e47.jpg)  
Fig. 3: Comparison between predicted and experimental values of $\log _ { 1 0 } ( T _ { 1 / 2 } ( s ) )$ obtained using (a) the UDL empirical formula, (b) the Royer empirical formula, and (c) the XGBoost model. The horizontal axis represents the experimental values and the vertical axis denotes the predicted values. For the XGBoost model, the points correspond to test predictions obtained from five-fold cross-validation. The dashed line indicates the ideal relation $y = x$ .

Since $\alpha$ -decay half-lives are governed by multiple physical mechanisms—including decay energy, centrifugal-barrier effects, shell structure, nuclear deformation, and isospin asymmetry—it is essential to examine how these physical factors are utilized

within the machine-learning model. To this end, we employ the SHAP (SHapley Additive exPlanations) interpretability framework to analyze the trained XGBoost model. SHAP enables a quantitative decomposition of the prediction into contributions from individual nuclear-structure features and provides insight into whether the learned dependencies are consistent with established nuclear-structure and decay systematics. The resulting feature-importance distribution is shown in Figure 4.

![](images/01a2e9969403a053141ed0e508eacc60e98b1f327349d1d889045841333d309f.jpg)  
Fig. 4: SHAP-based feature importance for the $\alpha$ -decay half-life prediction model.   
Figure 4 presents the SHAP feature-importance distribution for the $\alpha$ -decay half-life regression model. A clear hierarchical structure of physical contributions can be identified from the SHAP distribution.

Among all variables, the composite feature $Z / { \sqrt { Q _ { \alpha } } }$ exhibits by far the largest SHAP amplitude, indicating that it provides the dominant contribution to the predicted $\log _ { 1 0 } ( T _ { 1 / 2 } )$ . In the SHAP distribution, large values of $Z / { \sqrt { Q _ { \alpha } } }$ (red points) are predominantly located on the positive side of the SHAP axis, implying an increase in the predicted half-life, whereas smaller values (blue points) tend to produce negative contributions. This behavior is fully consistent with the barrier-penetration picture of $\alpha$ decay and directly reflects the Geiger–Nuttall systematics, in which the decay probability is governed by the combined effect of the Coulomb barrier and the released decay energy. The dominance of $Z / { \sqrt { Q _ { \alpha } } }$ therefore confirms that the model correctly captures the fundamental energy dependence of $\alpha$ -decay half-lives.

Secondary contributions arise from nucleon-number related variables such as $Z _ { 1 }$ , $A _ { 1 }$ , and $N _ { 1 }$ . Although their SHAP amplitudes are smaller than that of the dominant feature, their distributions exhibit systematic patterns. These variables encode the global nuclear scale and nucleon configuration, which influence the Coulomb interaction, nuclear radius, and shell structure. Their non-negligible SHAP contributions indicate that the model incorporates nucleon-number systematics to refine the half-life prediction across different mass regions of the nuclear chart.

The minimum orbital angular momentum $\ell _ { \mathrm { m i n } }$ provides a particularly transparent physical interpretation within the model. In $\alpha$ decay, transitions with $\ell _ { \mathrm { m i n } } = 0$ correspond to favored decays, whereas transitions with $\ell _ { \mathrm { m i n } } > 0$ are classified as unfavored

decays because they require a non-zero orbital angular momentum transfer. In the SHAP distribution, larger values of $\ell _ { \mathrm { m i n } }$ generally give rise to positive SHAP contributions, corresponding to an increase in the predicted $\log _ { 1 0 } ( T _ { 1 / 2 } )$ , while $\ell _ { \mathrm { m i n } } = 0$ is associated with comparatively smaller or even negative contributions. This trend reflects the well-known centrifugal hindrance mechanism: when $\ell _ { \mathrm { m i n } } > 0$ , an additional centrifugal barrier is introduced into the effective potential, which reduces the barrierpenetration probability and therefore prolongs the half-life. The SHAP behavior of $\ell _ { \mathrm { m i n } }$ thus shows that the model is able to distinguish favored and unfavored decays in a physically meaningful way and correctly capture the role of angular-momentum hindrance in $\alpha$ -decay systematics.

The deformation-related term $\sqrt { \kappa _ { 2 } \beta _ { 2 } }$ also produces noticeable contributions. Variations in this feature modify the effective shape of the Coulomb barrier and consequently affect the tunneling probability of the emitted $\alpha$ particle. The presence of non-zero SHAP amplitudes indicates that the model incorporates deformation effects to improve predictions in regions where nuclear shapes deviate from spherical symmetry.

Additional variables, including the isospin-asymmetry indicator $N _ { 1 } / Z _ { 1 }$ , the relative neutron excess $( N _ { 1 } - Z _ { 1 } ) / A _ { 1 }$ , and the distance to the nearest proton magic number, contribute at a smaller yet non-negligible level. These quantities reflect isospin asymmetry and shell-structure effects, which influence nuclear stability and cluster preformation. Although their individual impacts are weaker, they provide useful structural corrections that improve the predictive accuracy in specific regions of the nuclear chart, particularly near shell closures.

Overall, the SHAP analysis demonstrates that the XGBoost regression model does not behave as a purely numerical black-box interpolator. Instead, it reproduces the established hierarchical dependence of $\alpha$ -decay half-lives on decay energy, nucleon-number systematics, angular-momentum hindrance, nuclear deformation, and shell structure. This physically consistent learning behavior explains the systematic improvement of the machine-learning model over traditional empirical formulas while remaining fully compatible with known nuclear-decay systematics.

# IV. ACKNOWLEDGEMENTS

This work is supported by Yunnan Provincial Science Foundation Project (No. 202501AT070067), Yunnan Provincial Xing Dian Talent Support Program (Young Talents Special Program, (Young Talents Special Program, No. XDYC-QNRC-2023-0162), Kunming University Talent Introduction Research Project (No. YJL24019), Yunnan Provincial Department of Education Scientific Research Fund Project (No. 2025Y1055 and 2025Y1042), the Special Basic Cooperative Research Programs of Yunnan ProvincialUndergraduate Universities’ Association (NO. 202101BA070001-144), the Program for Frontier Research Team of Kunming University 2023, National Natural Science Foundation of China (No. 12063006), National College Student Innovation and Entrepreneurship Training Program (No. 202511393012, 202511393013, and 202511393016), Yunnan Province College Student Innovation and Entrepreneurship Training Program (No. S202511393003, S202511393043, and S202511393044), and Xing Dingyu Academician Workstation of Yunnan Province (No. 202605AF350035).

# REFERENCES

[1] Ernest Rutherford and Thomas Royds, “Xxi. the nature of the $_ \alpha$ particle from radioactive substances,” The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, vol. 17, no. 98, pp. 281–286, 1909.

[2] Ernest Rutherford, “Viii. uranium radiation and the electrical conduction produced by it,” The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, vol. 47, no. 284, pp. 109–163, 1899.   
[3] Ernest Rutherford and Hans Geiger, “An electrical method of counting the number of $_ \alpha$ -particles from radio-active substances,” Proceedings of the Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character, vol. 81, no. 546, pp. 141–161, 1908.   
[4] Hans Geiger and JM Nuttall, “Lvii. the ranges of the $_ \alpha$ particles from various radioactive substances and a relation between range and period of transformation,” The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, vol. 22, no. 130, pp. 613–621, 1911.   
[5] George Gamow, “Zur quantentheorie des atomkernes,” Zeitschrift fur Physik ¨ , vol. 51, no. 3, pp. 204–212, 1928.   
[6] Ronald W Gurney and Edw U Condon, “Wave mechanics and radioactive disintegration,” Nature, vol. 122, no. 3073, pp. 439–439, 1928.   
[7] Guy Royer, “Alpha emission andspontaneous fission through quasi-molecularshapes,” Journal of Physics G: Nuclear and Particle Physics, vol. 26, no. 8, pp. 1149, 2000.   
[8] Jun-Gang Deng, Hong-Fei Zhang, and Guy Royer, “Improved empirical formula for $_ \alpha$ -decay half-lives,” Physical Review C, vol. 101, no. 3, pp. 034307, 2020.   
[9] Jianmin Dong, Hongfei Zhang, Yanzhao Wang, Wei Zuo, and Junqing Li, “Alpha-decay for heavy nuclei in the ground and isomeric states,” Nuclear Physics A, vol. 832, no. 3-4, pp. 198–208, 2010.   
[10] Chong Qi, Roberto J Liotta, and Ramon Wyss, “Alpha decay measured in single-particle units as a manifestation of nuclear collectivity,” Physics Letters B, vol. 818, pp. 136373, 2021.   
[11] NG Kelkar and M Nowakowski, “Tunneling times and bremsstrahlung in $_ \alpha$ decay,” Physical Review C, vol. 89, no. 1, pp. 014602, 2014.   
[12] YZ Wang, JM Dong, BB Peng, and HF Zhang, “Fine structure of $_ \alpha$ decay to rotational states of heavy nuclei,” Physical Review C—Nuclear Physics, vol. 81, no. 6, pp. 067301, 2010.   
[13] Xiao Liu, Jie-Dong Jiang, Xi-Jun Wu, and Xiao-Hua Li, “Systematic study of cluster radioactivity in trans-lead nuclei with various versions of proximity potential formalisms,” Chinese Physics C, vol. 48, no. 5, pp. 054101, 2024.   
[14] Matthew Ryan Mumpower, Trevor Michael Sprouse, Amy Elizabeth Lovell, and Arvind Thanam Mohan, “Physically interpretable machine learning for nuclear masses,” Physical Review C, vol. 106, no. 2, pp. L021301, 2022.   
[15] Wanbing He, Qingfeng Li, Yugang Ma, Zhongming Niu, Junchen Pei, and Yingxun Zhang, “Machine learning in nuclear physics at low and intermediate energies,” Science China Physics, Mechanics & Astronomy, vol. 66, no. 8, pp. 282001, 2023.   
[16] Pramila P Shinde and Seema Shah, “A review of machine learning and deep learning applications,” in 2018 Fourth international conference on computing communication control and automation (ICCUBEA). IEEE, 2018, pp. 1–6.   
[17] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton, “Deep learning,” nature, vol. 521, no. 7553, pp. 436–444, 2015.   
[18] Jie M Zhang, Mark Harman, Lei Ma, and Yang Liu, “Machine learning testing: Survey, landscapes and horizons,” IEEE Transactions on Software Engineering, vol. 48, no. 1, pp. 1–36, 2020.   
[19] Zisheng Jin, Mingshuai Yan, Hao Zhou, An Cheng, Zhongzhou Ren, and Jian Liu, “Bayesian optimization approach to model-based description of $_ \alpha$ decay,” Physical Review C, vol. 108, no. 1, pp. 014326, 2023.   
[20] Na-Na Ma, Tian-Liang Zhao, Wen-Xia Wang, and Hong-Fei Zhang, “Simple deep-learning approach for $_ \alpha$ -decay half-life studies,” Physical Review C, vol. 107, no. 1, pp. 014310, 2023.   
[21] G Saxena, A Jain, and PK Sharma, “A new empirical formula for $_ \alpha$ -decay half-life and decay chains of $\mathbf { z } = 1 2 0$ isotopes,” Physica Scripta, vol. 96, no. 12, pp. 125304, 2021.   
[22] Hong-Qiang You, Zheng-Zhe Qu, Ren-Hang Wu, Hao-Ze Su, and Xiao-Tao He, “Study of $_ \alpha$ -decay energy by an artificial neural network considering pairing and shell effects,” Symmetry, vol. 14, no. 5, pp. 1006, 2022.   
[23] Jian Liu, Zisheng Jin, and Zhongzhou Ren, “Physical interpretation in favored and unfavored $_ \alpha$ transitions with a bayesian optimization approach,” Physical Review C, vol. 112, no. 2, pp. 024309, 2025.   
[24] Yunfei Ma, Chen Su, Jian Liu, Zhongzhou Ren, Chang Xu, and Yonghao Gao, “Predictions of nuclear charge radii and physical interpretations based on the naive bayesian probability classifier,” Physical Review C, vol. 101, no. 1, pp. 014304, 2020.   
[25] Amir Jalili, Feng Pan, Jerry P Draayer, Ai-Xi Chen, and Zhongzhou Ren, “-decay half-life predictions with support vector machine,” Scientific Reports, vol. 14, no. 1, pp. 30776, 2024.   
[26] Na Wang, Jie Zhou, Xiangjun Kuang, Jianqi Qi, Jun Zhou, Shijie Wang, Tingting Song, and Peng Sun, “Exploring the potential of magnesium clusters as effective adsorbents for gaseous radioactive iodine in nuclear energy applications,” Structural Chemistry, vol. 36, no. 1, pp. 29–38, 2025.

[27] Jie Chen, Pengfei Ou, Yuxin Chang, Hengrui Zhang, Xiao-Yan Li, Edward H Sargent, and Wei Chen, “Materials discovery using uncertainty-aware constrained bayesian optimization with representation learning of high-dimensional inputs,” Journal of Mechanical Design, vol. 148, no. 2, pp. 021707, 2026.   
[28] Chen-Qi Li, Chao-Nan Tong, Hong-Jing Du, and Long-Gang Pang, “Deep learning approach to nuclear masses and $_ \alpha$ -decay half-lives,” Physical Review C, vol. 105, no. 6, pp. 064306, 2022.   
[29] Jian Liu, Huiguang Zhang, Xiaoyong Guo, and Yibin Qian, “Interpretable comparison of different machine learning families on $_ \alpha$ -decay,” Physica Scripta, vol. 101, no. 1, pp. 016005, 2026.   
[30] FG Kondev, Meng Wang, WJ Huang, S Naimi, and G Audi, “The nubase2020 evaluation of nuclear physics properties,” Chinese Physics C, vol. 45, no. 3, pp. 030001, 2021.   
[31] WJ Huang, Meng Wang, Filip G Kondev, Georges Audi, and Sarah Naimi, “The ame 2020 atomic mass evaluation (i). evaluation of input data, and adjustment procedures,” Chinese Physics C, vol. 45, no. 3, pp. 030002, 2021.   
[32] Meng Wang, Wen Jie Huang, Filip G Kondev, Georges Audi, and Sarah Naimi, “The ame 2020 atomic mass evaluation (ii). tables, graphs and references,” Chinese Physics C, vol. 45, no. 3, pp. 030003, 2021.   
[33] P Moller, Arnold John Sierk, Takatoshi Ichikawa, and Hiroyuki Sagawa, “Nuclear ground-state masses and deformations: Frdm (2012),” ¨ Atomic Data and Nuclear Data Tables, vol. 109, pp. 1–204, 2016.   
[34] Boshuai Cai, Guangshang Chen, Jiongyu Xu, Cenxi Yuan, Chong Qi, and Yuan Yao, “ $_ \alpha$ decay half-life estimation and uncertainty analysis,” Physical Review C, vol. 101, no. 5, pp. 054304, 2020.   
[35] M Hosseini-Tabatabaei, SA Alavi, and V Dehghani, “Systematic of alpha decay half-lives: role of quantization condition,” Canadian Journal of Physics, vol. 99, no. 1, pp. 24–32, 2021.   
[36] HF Zhang and Guy Royer, “ $_ \alpha$ particle preformation in heavy nuclei and penetration probability,” Physical Review C—Nuclear Physics, vol. 77, no. 5, pp. 054318, 2008.   
[37] V Yu Denisov and AA Khudenko, “ $_ \alpha$ -decay half-lives: Empirical relations,” Physical Review C—Nuclear Physics, vol. 79, no. 5, pp. 054614, 2009.   
[38] Md Manjurul Ahsan, MA Parvez Mahmud, Pritom Kumar Saha, Kishor Datta Gupta, and Zahed Siddique, “Effect of data scaling methods on machine learning algorithms and model performance,” Technologies, vol. 9, no. 3, pp. 52, 2021.   
[39] Lucas BV De Amorim, George DC Cavalcanti, and Rafael MO Cruz, “The choice of scaling technique matters for classification performance,” Applied Soft Computing, vol. 133, pp. 109924, 2023.   
[40] Tianqi Chen, “Xgboost: A scalable tree boosting system,” Cornell University, 2016.   
[41] Yingjie Li, Yan Feng, and Quan Qian, “Fdpboost: Federated differential privacy gradient boosting decision trees,” Journal of Information Security and Applications, vol. 74, pp. 103468, 2023.   
[42] S Madhumitha Shree and M Balasubramaniam, “α-decay half-life predictions for superheavy elements through machine learning techniques,” The European Physical Journal A, vol. 61, no. 2, pp. 32, 2025.   
[43] Yan Zhang and Lin Chen, “A study on forecasting the default risk of bond based on xgboost algorithm and over-sampling method,” Theoretical economics letters, vol. 11, no. 2, pp. 258–267, 2021.   
[44] Monty-Maximilian Zuhlke and Daniel Kudenko, “Tcr: topologically consistent reweighting for xgboost in regression tasks,” ¨ Machine Learning, vol. 114, no. 4, pp. 108, 2025.   
[45] Zhi-Hua Zhou, Ensemble methods: foundations and algorithms, CRC press, 2025.   
[46] Jerome H Friedman, “Greedy function approximation: a gradient boosting machine,” Annals of statistics, pp. 1189–1232, 2001.   
[47] Laurens Sluijterman, Frank Kreuwel, Eric Cator, and Tom Heskes, “Composite quantile regression with xgboost using the novel arctan pinball loss,” International Journal of Machine Learning and Cybernetics, pp. 1–15, 2025.   
[48] Xuchen Dong, Ting Lei, Shangtai Jin, and Zhongsheng Hou, “Short-term traffic flow prediction based on xgboost,” in 2018 IEEE 7th data driven control and learning systems conference (DDCLS). IEEE, 2018, pp. 854–859.   
[49] Guy Royer, “On the coefficients of the liquid drop model mass formulae and nuclear radii,” Nuclear Physics A, vol. 807, no. 3-4, pp. 105–118, 2008.   
[50] Hongfei Zhang, Wei Zuo, Junqing Li, and Guy Royer, “ $_ \alpha$ decay half-lives of new superheavy nuclei within a generalized liquid drop model,” Physical Review C—Nuclear Physics, vol. 74, no. 1, pp. 017304, 2006.   
[51] WM Seif and A Adel, “Additional hindrance of unfavored $_ \alpha$ decay between states of different parity,” Physical Review C, vol. 99, no. 4, pp. 044311, 2019.

[52] Raymond K Sheline and Botho Bo-Mbaka Bossinga, “Alpha decay hindrance factors and reflection asymmetry in nuclei,” Physical Review C, vol. 44, no. 1, pp. 218, 1991.   
[53] DS Delion, RJ Liotta, and Ramon Wyss, “ $_ \alpha$ decay of high-spin isomers in superheavy nuclei,” Physical Review C—Nuclear Physics, vol. 76, no. 4, pp. 044301, 2007.   
[54] G Saxena, PK Sharma, and Prafulla Saxena, “Modified empirical formulas and machine learning for $_ \alpha$ -decay systematics,” Journal of Physics G: Nuclear and Particle Physics, vol. 48, no. 5, pp. 055103, 2021.   
[55] JP Cui, YH Gao, YZ Wang, and JZ Gu, “Improved effective liquid drop model for $_ \alpha$ -decay half-lives,” Nuclear Physics A, vol. 1017, pp. 122341, 2022.   
[56] Takaharu Otsuka, Alexandra Gade, Olivier Sorlin, Toshio Suzuki, and Yutaka Utsuno, “Evolution of shell structure in exotic nuclei,” Reviews of modern physics, vol. 92, no. 1, pp. 015002, 2020.   
[57] H Nakada, “Irregularities in nuclear radii at magic numbers,” Physical Review C, vol. 100, no. 4, pp. 044310, 2019.   
[58] O Sorlin and M-G Porquet, “Nuclear magic numbers: New features far from stability,” Progress in Particle and Nuclear Physics, vol. 61, no. 2, pp. 602–673, 2008.   
[59] S Amiel and H Feldstein, “Odd-even systematics in neutron fission yields of u 233 and u 235,” Physical Review C, vol. 11, no. 3, pp. 845, 1975.   
[60] NJ Stone, “Table of nuclear electric quadrupole moments,” Atomic Data and Nuclear Data Tables, vol. 111, pp. 1–28, 2016.   
[61] Liang Ma, Kui Wang, Yu Xie, Xin Yang, Yingying Wang, Mi Zhou, Hanyu Liu, Xiaohui Yu, Yongsheng Zhao, Hongbo Wang, et al., “High-temperature superconducting phase in clathrate calcium hydride cah 6 up to $^ { 2 1 5 \mathrm { ~ k ~ } }$ at a pressure of 172 gpa,” Physical Review Letters, vol. 128, no. 16, pp. 167001, 2022.   
[62] PA Butler, “Studies of heavy pear-shaped nuclei,” in Journal of Physics: Conference Series. IOP Publishing, 2023, vol. 2453, p. 012001.   
[63] Paul E Garrett, Magda Zielinska, and Emmanuel Cl ´ ement, “An experimental view on shape coexistence in nuclei,” ´ Progress in Particle and Nuclear Physics, vol. 124, pp. 103931, 2022.   
[64] Yibin Qian and Zhongzhou Ren, “Shape probe of hg and pt isotopes by $_ \alpha$ decay,” Journal of Physics G: Nuclear and Particle Physics, vol. 39, no. 11, pp. 115106, 2012.   
[65] Monika Manhas and Raj K Gupta, “Proximity potential for deformed, oriented nuclei:“gentle” fusion and “hugging” fusion,” Physical Review C—Nuclear Physics, vol. 72, no. 2, pp. 024606, 2005.   
[66] V Yu Denisov, “Alpha-decay half-lives and alpha-capture cross-sections,” Atomic Data and Nuclear Data Tables, vol. 161, pp. 101684, 2025.   
[67] V Yu Denisov, “Empirical relations for $_ \alpha$ -decay half-lives: The effect of deformation of daughter nuclei,” Physical Review C, vol. 110, no. 1, pp. 014604, 2024.   
[68] Enayatolah Yazdankish and Mostafa Nejatolahi, “Improved calculation of alpha decay half-life by incorporating nuclei deformation shape and proximity potential,” Physica Scripta, vol. 98, no. 11, pp. 115309, 2023.   
[69] TianLiang Zhao and HongFei Zhang, “Unified description of $_ \alpha$ decay and cluster radioactivity using the neural network approach and universal decay law,” Journal of Physics G: Nuclear and Particle Physics, vol. 49, no. 10, pp. 105104, 2022.