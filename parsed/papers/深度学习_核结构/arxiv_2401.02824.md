# Nuclear mass predictions using machine learning models

Esra Y¨uksel,1, ∗ Derya Soydaner,2, † and H¨useyin Bahtiyar3, ‡

$^ { 1 }$ Department of Physics, University of Surrey, Guildford, Surrey GU2 7XH, United Kingdom

2Department of Brain and Cognition, University of Leuven (KU Leuven), Leuven, Belgium

3Y. Tahsinbey St. 8/4, 34841, Maltepe, Istanbul, T¨urkiye

(Dated: June 26, 2024)

The exploration of nuclear mass or binding energy, a fundamental property of atomic nuclei, remains at the forefront of nuclear physics research due to limitations in experimental studies and uncertainties in model calculations, particularly when moving away from the stability line. In this work, we employ two machine learning (ML) models, Support Vector Regression (SVR) and Gaussian Process Regression (GPR), to assess their performance in predicting nuclear mass excesses using available experimental data and a physics-based feature space. We also examine the extrapolation capabilities of these models using newly measured nuclei from AME2020 and by extending our calculations beyond the training and test set regions. Our results indicate that both SVR and GPR models perform quite well within the training and test regions when informed with a physicsbased feature space. Furthermore, these ML models demonstrate the ability to make reasonable predictions away from the available experimental data, offering results comparable to the model calculations. Through further refinement, these models can be used as reliable and efficient ML tools for studying nuclear properties in the future.

Keywords: Nuclear mass, machine learning, regression, explainable AI

# I. INTRODUCTION

The atomic nucleus, a strongly correlated many-body system, is characterized by its proton ( $Z$ ) and neutron ( $N$ ) numbers. Mass is a fundamental property of atomic nuclei, playing a crucial role in our understanding of strong nuclear interactions and a vital role in nuclear astrophysical calculations, such as r-process simulations, where they serve as inputs [1, 2]. Experimentally, it is possible to study nuclei near the stability lines, and accurate nuclear data for the masses of nuclei are available [3, 4]. However, despite significant advancements in nuclear facilities, measurements on the neutron-rich side of the nuclear chart remain unfeasible in the near future, and the exploration of the majority of nuclei involved in the r-process has yet to be undertaken. For instance, the neutron drip line, which indicates the position of the last bound nucleus, has been confirmed only up to $\mathrm { Z } = 1 0$ [5], and the boundaries of the nuclear landscape are not known experimentally. Therefore, our understanding of nuclear properties away from the stability line and the limits of the nuclear landscape relies heavily on theoretical calculations.

Up to now, several theoretical models have been used to investigate nuclear properties and determine the location of drip lines. Within this framework, microscopicmacroscopic (mic-mac) global nuclear mass models, such as Weizs¨acker-Skyrme Nuclear Mass Tables (WS4) [6] and Finite-Range Droplet Model (FRDM-2012) [7], have demonstrated considerable success and been extensively used in $r -$ process calculations over the years. However,

despite the success of the mic-mac models in fitting experimental data on the measured masses of nuclei, the root mean square (rms) errors with respect to the known experimental data are not at the desired level. The rms error, in relation to the available mass data, was found to be 0.298 MeV when using the WS4 model [6] and 0.662 MeV using the FRDM(2012) model [7]. Furthermore, these models have been fitted using the available experimental data, which makes the behavior of nuclei on the neutron-rich side of the nuclear chart still somewhat uncertain.

More sophisticated methods, such as self-consistent mean-field (SCMF) theories based on the Hartree-Fock-Bogolyubov (HFB) approach with nuclear energy density functionals (EDF), have also long been employed to investigate the properties of nuclei. Although using microscopic tools in calculations is a computationally demanding task, large-scale computations of the nuclear chart are nonetheless available. In recent years, both relativistic and non-relativistic calculations have been performed using different EDFs to probe the properties of nuclei and to define the boundaries of the nuclear landscape [8– 17]. While these models perform well around the stability line with respect to the available experimental data, they reveal local variations and significant discrepancies that increase with neutron number, ultimately impacting the location of the drip lines. The major source of these differences is the missing incomplete correlations on the purely mean-field level of the HFB description, the usage of different interactions that are optimized using different strategies, pairing correlations, and the impact of the continuum. Typically, the rms error of these mass tables compared to the available experimental data are quite high and range between 2.0 and 5.0 MeV, depending on the interaction used in the calculations. One of the most recent functionals, which are optimized using

the experimental data of all available nuclei, has reached an rms error between 0.5 and 0.6 MeV [14, 18–21]. Considering all of these factors, there is a need to find fast and reliable methods for determining nuclear properties, especially away from the stability line.

In recent years, machine learning (ML) models have gained considerable attention within the scientific community, demonstrating notable success, including also the field of nuclear physics (see Ref. [22] and references therein). These models have proven capable of directly predicting nuclear properties using experimental data [23–32]. Recently, the ML models have also been used to improve mic-mac and microscopic model predictions. Within this framework, the most popular tool is Bayesian neural networks (BNNs), which have been used to improve the results of microscopic calculations by training on the residuals. These residuals represent the differences between experimental data and microscopic calculations, and the BNNs have gained considerable attention and success in that respect [33–36]. In this context, ML models can be used as reliable and efficient tools to probe nuclear properties; however, more studies are necessary to better understand their predictive capability.

In this study, our goal is to assess the performance of the two ML models in predicting the nuclear mass excess ( $M$ ) of nuclei, rather than correcting existing mic-mac or microscopic model predictions. We use the Support Vector Regression (SVR) and Gaussian Process Regression (GPR) ML models to calculate the mass excess of nuclei. These models are trained using available experimental data along with the relevant physics-based feature space. Then, we evaluate the performance of these ML models in predicting the mass excess of nuclei, examining also their extrapolation capabilities far beyond the training and test regions.

# II. MACHINE LEARNING MODELS

In this section, we present an overview of the ML models employed in our calculations: SVR and GPR. Additionally, we describe the experimental data used to train these models and provide details about the physics-based feature space involved.

# A. Support Vector Regression

The SVR [37] is an ML model specifically designed for tackling regression tasks, offering a unique approach to predict continuous outcomes by leveraging the principles of support vector machines (SVMs) [38]. In contrast to classification-focused methods, SVR seeks a hyperplane that optimally fits the training data with minimized error. Central to SVR is the concept of support vectors, which are critical data points closest to the hyperplane’s boundaries. The model aims to align as many data points as possible within the optimal hyperplane, fitting within

a specified tolerance margin. It simultaneously controls margin violations, addressing instances where data points exceed the boundaries. This brings a hyperparameter $\epsilon$ , which controls the width of the hyperplane [39].

The strength of SVR is particularly notable in addressing non-linear regression problems, often yielding enhanced results [40]. At the core of SVR’s approach to these problems is the effective kernel trick. This technique is crucial when dealing with input data that is not linearly separable in its original feature space. By employing the kernel trick, SVR can implicitly project the data into a higher-dimensional space, achieving linear separability. This projection is facilitated by a kernel function, which efficiently calculates the dot product of data point pairs in this higher-dimensional space without the need for explicit calculation of transformed features. Thus, SVR involves mapping input data into a higherdimensional space using kernel functions, allowing for the capture of nonlinear relationships. Among various kernel functions, the Radial Basis Function (RBF) kernel is a widely used choice in SVR applications defined as:

$$
\begin{array}{l} K _ {G} \left(x, x ^ {\prime}\right) = \exp \left(- \frac {\left\| x - x ^ {\prime} \right\| ^ {2}}{2 \sigma^ {2}}\right) \tag {1} \\ = \exp \left(- \gamma | | x - x ^ {\prime} | | ^ {2}\right). \\ \end{array}
$$

In this context, $x$ and $x ^ { \prime }$ represent two data points, and their Euclidean distance is denoted as $\left| \left| x - x ^ { \prime } \right| \right|$ , while $\gamma$ is the kernel coefficient. Eq. 1 quantifies the similarity or dissimilarity between these data points, based on their distance in the input feature space. This results in higher similarity for closer data points, and conversely, lower similarity for those more distant [39, 41]. The tuning of hyperparameters plays a crucial role in SVR. Proper parameter adjustment is important to prevent overfitting or underfitting, ensuring the model generalizes well to unseen data. The regularization hyperparameter, denoted as $C$ , is essential in striking the balance between maximizing the margin and minimizing the training error. Additionally, the $\epsilon$ hyperparameter is important in determining the tolerance margin, within which the epsiloninsensitive loss function does not penalize errors. Data points within this margin do not contribute to the loss function, enhancing the model’s robustness against minor prediction errors and improving its resilience to outliers. In our experiments, we set the $\epsilon$ to 0.002, $C$ to 1000, and $\gamma$ to 0.03. Another hyperparameter, the tolerance, which indicates the desired precision for convergence, is set to $1 0 ^ { - 5 }$ . We performed calculations on several hyperparameter configurations to determine the optimal setting for our task, and ultimately report the model that exhibits the highest performance.

SVR offers a versatile framework for regression tasks, utilizing kernels to capture diverse relationships and incorporating a margin of tolerance to enhance robustness. Practical hyperparameter tuning and understanding the role of kernels are fundamental for optimizing the model

performance across various datasets and maximizing its efficiency in real-world applications.

# B. Gaussian Process Regression

When we consider a linear model expressed as $y =$ $w ^ { T } x$ , this model describes a linear relationship for every different value of $w$ . If we introduce a prior distribution for $w$ , denoted as $p ( w )$ , the distribution of possible $y$ values at any given $x$ , $y ( x | w )$ , emerges from sampling $w$ from $p ( w )$ . This is the main idea of a Gaussian process. When $p ( w )$ follows a Gaussian distribution, each resulting $y$ is also Gaussian, being a linear combination of Gaussians. Specifically, our interest lies in the joint Gaussian distribution of $y$ values computed at $N$ input data points $x ^ { t }$ , where $t = 1 , \ldots , N$ [42, 43]. We typically assume a Gaussian prior with zero-mean for $w$ , as shown in Eq.2:

$$
p (w) \sim \mathcal {N} (0, (1 / \alpha) I). \qquad (2)
$$

GPR [42, 44] operates by leveraging Gaussian processes to model distributions over functions. Initially, the algorithm establishes a prior distribution over functions, assuming Gaussian-distributed function values at input points. This prior distribution forms the foundation, characterized by a mean function and a kernel function. As training data is observed, this prior is updated to a posterior distribution using Bayes’ theorem. This update incorporates the observed data, refining the model’s beliefs about the underlying function. The resulting posterior distribution enables predictions at new data points, providing not only a mean prediction but also an associated measure of uncertainty, which is crucial for decision-making in uncertain scenarios.

The choice of kernels is important in GPR. In our work, we utilize a combination of the RBF kernel (Eq.1) and the White kernel (Eq.3). The RBF kernel is particularly effective at capturing intricate data patterns, adapting to various scales, and ensuring smooth connections between data points. Meanwhile, the White kernel models noise within the dataset. Adjusting the noise level hyperparameter within the White Kernel is essential, striking a balance between capturing the underlying signal and accommodating inherent noise. This delicate interplay between kernels enables our GPR model to provide robust predictions, while acknowledging and quantifying uncertainties. To optimize the model, we adjust the kernel parameters by spanning a range of values to obtain the optimum values for our calculations. In our experiments, the length scale of the RBF kernel is set to 1.0, with its lower and upper bounds on the length scale being $( 1 0 ^ { - 4 } , 1 0 ^ { 5 } )$ . For the White Kernel, the noise level is set at 1, with the noise level’s lower and upper bounds set at ( $1 0 ^ { - 1 0 }$ , 10).

$$
K _ {W} \left(x, x ^ {\prime}\right) = \left\{ \begin{array}{l l} \text {n o i s e l e v e l} & \text {i f} x _ {i} = x _ {j} ^ {\prime} \\ 0 & \text {o t h e r w i s e .} \end{array} \right. \tag {3}
$$

GPR’s strength lies not only in its predictive accuracy but also in its ability to provide nuanced insights into the reliability of those predictions. This is achieved through its uncertainty quantification, which offers a probabilistic measure of confidence in its predictions. By effectively quantifying the uncertainty associated with each prediction, GPR enhances decision-making processes in various domains. This dual capability of delivering precise predictions while simultaneously assessing their reliability makes GPR a valuable tool across a wide range of applications.

![](images/3f288a08d4654b654d04ddd9ac5928289a777a89e8471dc3de6e2dfa21c4e0eb.jpg)  
FIG. 1: The training set (gray circles), test set (red circles), and extrapolation set (blue circles) used in the ML models. Both the training and test sets include nuclei from AME2020, with the exception of the newly measured 71 nuclei from AME2020, which are exclusively designated for the extrapolation set [4].

# C. The experimental data and feature space

In this study, our objective is to develop an ML model that predicts the mass excess of atomic nuclei using both experimental data on the mass excess of nuclei and a physics-based feature space. The experimental mass excess values are taken from the atomic mass evaluation 2020 (AME2020) [4] for nuclei with $Z , N \ge 8$ (2386 nuclei). Then, the experimental data is randomly divided into two subsets: 75.0% (1789 nuclei) for training and 25.0% (597 nuclei) for testing. The nuclei in the training and test sets remain the same for all calculations. The performance of the ML models is also assessed beyond the training and test data sets. The AME2020 data includes new experimental information for 71 nuclei compared to

the previous AME2016 [3]. These nuclei have been utilized to test the extrapolation capabilities of the models. The estimated mass excess values, derived from the trends in the mass surface (TMS) of nuclei, are also utilized to compare our findings in the extrapolation region. The selection of the training and test sets, as well as the new data from AME2020 (extrapolation set), is shown in Figure 1. Additionally, we evaluate the extrapolation performance of the models by extending calculations to the neutron-rich region beyond the reach of current experimental facilities, probing the limits of their predictive capabilities.

TABLE I: The ML models with different features.   

<table><tr><td>Model</td><td>Feature Space</td></tr><tr><td>SVR/GPR-5</td><td>Z, N, A, A2/3, (N-Z)/A</td></tr><tr><td>SVR/GPR-8</td><td>Z, N, A, A2/3, (N-Z)/A, 
νZ, νN, PF</td></tr><tr><td>SVR/GPR-10</td><td>Z, N, A, A2/3, (N-Z)/A, 
νZ, νN, PF, Zeo, Neo</td></tr><tr><td>SVR/GPR-12</td><td>Z, N, A, A2/3, (N-Z)/A, 
νZ, νN, PF, Zeo, Neo, Zshell, Nshell</td></tr></table>

As it is well known, the use of appropriate inputs during training can significantly impact the performance of ML models [26–28, 30, 31]. Therefore, in our models, we incorporate relevant features of nuclei that can influence mass predictions. Our feature space consists of 12 inputs: $Z$ , $N$ , $A$ , $A ^ { 2 / 3 }$ , $( N - Z ) / A$ , $Z _ { e o }$ , $N _ { e o }$ , $\nu _ { Z }$ , $\nu _ { N }$ , $P F$ , $\boldsymbol { Z _ { s h e l l } }$ , and $N _ { s h e l l }$ . Here, the bulk properties are defined as the proton (neutron) number $Z$ ( $N$ ), the mass number $( A )$ , and $A ^ { 2 / 3 }$ for volume and surface terms. The term odd-even $\frac { N - Z } { A }$ is a measuree of protons sospin asymmetr) and neutrons ( The) is $\mathop { Z _ { e o } }$ $N _ { e o }$ defined as follows: $Z _ { e o }$ ( $N _ { e o }$ ) equals zero when $Z$ $N$ ) is even and one when $Z$ ( $N$ ) is odd. We also provide information about the nuclear magic numbers: $\nu _ { Z }$ and $\nu _ { N }$ represent the valence number of protons and neutrons measured from the nearest closed shell. The nuclear magic numbers for protons and neutrons are taken as $Z ( N ) = 8 , 2 0 , 2 8 , 5 0 , 8 2 , 1 2 6 , 1 8 4 .$ . The promiscuity factor $( P F )$ is represented by the formula P F = νZ ·νN $\begin{array} { r } { P F = \frac { \nu _ { Z } \cdot \nu _ { N } } { \nu _ { Z } + \nu _ { N } } } \end{array}$ and serves as a measure of valence proton-neutron $( p - n )$ interactions [45]. Lastly, the system is informed about the nuclear shells with $Z _ { \mathrm { s h e l l } }$ and $N _ { \mathrm { s h e l l } }$ ; they represent the shell model orbitals of the last proton and neutron. The values of $Z _ { \mathrm { s h e l l } }$ and $N _ { \mathrm { s h e l l } }$ are defined as 0, 1, 2, 3, or 4, depending on whether the proton or neutron number falls within the specified ranges: 1–28, 29–50, 51–82, 83–126, and above 127, respectively [46]. In order to assess the importance of the feature space in model calculations, we implement ML models with different features. The inputs used in our ML models are given in Table I.

# III. RESULTS

Figure 2 displays the absolute differences between the results of GPR (upper panels) and SVR (lower panels) with different inputs and the experimental data taken from AME2020 [4]. The feature space of the ML models is provided in Table I. The rms errors for the training and test sets of each selected model are also presented in Figure 2. Using only the bulk properties of nuclei to construct the model, GPR-5 yields reasonable results, with rms errors of 0.91 and 1.08 MeV for the training and test sets, respectively, better than most of the microscopic model calculations. On the other hand, the performance of SVR-5 is lower compared to GPR-5, with rms errors of 2.40 and 2.55 MeV for the training and test sets, respectively.

In Figure 2, it is evident that increasing the physicsbased feature space significantly improves the performance of the models. The importance of the physicsbased feature space has also been discussed in previous studies, with similar results obtained using different ML models [26, 28, 30, 31]. It has been noticed that the inclusion of the odd-even nature of protons and neutrons ( $Z _ { e o }$ , $N _ { e o }$ ) leads to a significant improvement in ML predictions. Subsequently, the results improve further with the inclusion of information on the nuclear shells, $Z _ { \mathrm { s h e l l } }$ and $N _ { \mathrm { s h e l l } }$ . Utilizing 12 inputs (GPR-12) in the calculations, we achieved an rms error of 0.14 and 0.26 MeV for the training and test sets, respectively. These rms error values are even better than those of well-known mic-mac mass models, suggesting that the GPR model effectively captures the given information of nuclei and makes reasonable predictions. Additionally, we observe that GPR performs better for medium-heavy and heavy nuclei, while errors are slightly higher for light nuclei. The poorer performance in light nuclei is attributed to the lower number of available experimental data in this region. Similar results are also obtained using the SVR model. However, we find that SVR requires more data and information to make reasonable predictions for training and test set nuclei, and GPR outperforms SVR in that respect.

We also compare our findings with previous ML studies in which different ML models have been used to predict nuclear mass excess. One of the first applications of ML models in nuclear physics was performed using SVMs [24], predicting nuclear mass excess long ago. It yielded rms errors of 0.35, 0.5, and 0.71 MeV for the training, validation, and test sets, respectively. A recent application of the probabilistic ML algorithm, the Mixture Density Network (MDN), has yielded rms errors of around 0.5- 0.6 MeV with respect to the AME2016 [30] when supplemented with physics-based feature space. Recently, it has been shown that the inclusion of a soft physical constraint in the MDN achieved an rms error of 0.186 MeV for the training data (consisting of only 450 nuclei, approximately 20% of the AME2016 dataset) and an rms error of 0.316 MeV for the remainder of the AME2016

![](images/85bd7d3b72422ab44b964233d80322212701eba4aee00442385e7a42769c6d94.jpg)  
FIG. 2: The absolute value of mass excess differences between the GPR and SVR predictions for training and test set using different features (see Table I) and the AME2020 data [4]. The rms errors for the training and test sets are also provided.

data with $Z \ge 2 0$ [31]. Therefore, we also performed calculations using different train-test set ratios to assess the performance of our ML models, and the results are presented for nuclei with $Z \geq 8$ in Table II. Our findings indicate that our ML models exhibit robust predictive capabilities even when trained on a mere 25% of the available experimental data. However, as expected, the models’ performance on the test set declines with reduced training data, as they struggle to grasp details with limited information. Conversely, increasing the number of the training data yields noticeable improvements in the models’ test set performance, while the performance on the training set remains relatively stable. Similar results are also obtained in Ref. [32] using the MDN, whereas it is observed that our ML models require more training data to learn and generalize information to unseen data compared to the MDN. We anticipate that incorporating physical constraints into ML models, such as the Garvey-Kelson (GK) relations, can also enhance the predictive power of the ML model on unseen data, particularly with a limited amount of training data [31]. Alternatively, increasing the size of the training data, as demonstrated in our work, can also improve model performance on unseen data. Our results, even without applying a physical constraint, are in good agreement with the findings in Refs. [31, 32] when using train-test set ratios of 50%-50% and 75%-25%.

We conclude that our findings, obtained using different ML models, not only align with these previous studies but also establish GPR and SVR as alternative and reliable tools for ML studies in nuclear physics.

Extrapolation performance of ML models - One of the most important issues in ML studies is the low performance of the ML models when it comes to extrapolation, namely, outside the training and test set regions. It

TABLE II: Root mean square errors $\sigma _ { r m s }$ (in MeV) for GPR-12 and SVR-12 ML models, indicating their performance on training and test sets for $Z \geq 8$ across varying train-test data ratios from AME2020 set [4]. The percentages represent the proportion of data allocated to the training and test sets.

<table><tr><td></td><td colspan="3">Train-test ratio %</td></tr><tr><td></td><td>25-75</td><td>50-50</td><td>75-25</td></tr><tr><td>GPR-12 (train)</td><td>0.16</td><td>0.21</td><td>0.14</td></tr><tr><td>GPR-12 (test)</td><td>0.79</td><td>0.49</td><td>0.26</td></tr><tr><td>SVR-12 (train)</td><td>0.13</td><td>0.20</td><td>0.23</td></tr><tr><td>SVR-12 (test)</td><td>0.91</td><td>0.49</td><td>0.39</td></tr></table>

is essential to develop models that not only predict wellknown experimental data (training and test data) effectively but can also make accurate predictions for parts of the nuclear chart that are challenging to measure experimentally. Therefore, in this subsection, we assess the extrapolation capabilities of the ML models by extending beyond the experimentally known region. Initially, we test the performance of the ML models on the newly measured 71 nuclei from the AME2020 data [4] (see Fig. 1). We present the rms errors of each model in Table III. Clearly, the accuracy of model predictions improves with the use of appropriate features. Specifically, increasing the number of inputs from 5 to 12 improves the performance of the GPR and SVR models in the extrapolation region by 54.73% and $6 7 . 9 6 \%$ , respectively. Furthermore, the low rms errors of these ML models, which are comparable to those of modern nuclear mass models, indicate

that ML models are able to make reasonable predictions even outside the training region.

TABLE III: The root mean square errors (given in MeV) for the extrapolation set (71 nuclei from AME2020). The calculations are performed using different inputs.   

<table><tr><td>Feature</td><td>5</td><td>8</td><td>10</td><td>12</td></tr><tr><td>Model</td><td>σextrapol.</td><td>σextrapol.</td><td>σextrapol.</td><td>σextrapol.</td></tr><tr><td>GPR</td><td>1.48</td><td>1.10</td><td>0.75</td><td>0.67</td></tr><tr><td>SVR</td><td>2.31</td><td>1.17</td><td>0.70</td><td>0.74</td></tr></table>

How far can we go from the experimentally known region and get reasonable results using ML models? In order to assess the extrapolation performance of the ML models, we extend our calculations through the protonrich and neutron-rich regions. The results are presented for both the training and test regions (gray region) and the extrapolation region (white regions), where no experimental data currently exists. In Figure 3, we depict the predictions for the mass excess of nuclei using GPR-5 and SVR-5 for selected isotopic chains from various parts of the nuclear chart. The estimated values for the mass excess predictions from the trends in the mass surface (TMS) are also used to assess the performance of the models in the extrapolation region [4]. Additionally, we compare these predictions with results from well-known mass tables: the mic-mac model WS4+RBF [6] and the non-relativistic (BSk24) [20] calculations. The relativistic calculations with the point-coupling interaction DD-PCX [47] are performed for even-even nuclei using the axially-deformed Hartree-Bogoliubov (RHB) model with separable pairing [48], employing 20 harmonic oscillator shells for convergence in the calculations [15].

In GPR, the uncertainty is represented by the blue shaded region. It represents the probability distribution over the possible functions. This distribution is updated as more data or features are observed, which leads to a more precise estimate of the function. Therefore, it is expected that the uncertainty increases away from the training data, which is a direct consequence of the roots of Gaussian Process in probability and Bayesian inference. As can be seen from the upper panels of Figure 3, the GPR with only 5 features performs poorly when we move away from the training-test region, and the uncertainty is quite high in the extrapolation region. Apart from the Mg chain, the GPR can make reasonable predictions for the isotopic chains up to an increase in neutron number around 4 or 5. Then, the results start to deviate and do not follow the trends obtained in different mass models. Although the rms errors are higher for the training and test sets using the SVR-5 model, it is seen that the SVR-5 model captures the trends better in the extrapolation region.

By increasing the number of features in the GPR model, we observe a significant improvement in the model’s performance in the extrapolation region (Figure 4). Firstly, we note a considerable reduction in the uncertainties of the predictions. Secondly, the predictions of the GPR-12 model align with a trend that is similar and comparable to those obtained in different mass models, albeit slightly higher nearby the drip line. Increasing the number of features in the GPR model unequivocally enhances its generalizability and improves uncertainty estimation. As mentioned above, SVR-12 demonstrates improved predictions in both the training and test regions when the number of features is increased. However, an increase in the number of features in the SVR model does not lead to better results for the extrapolation region. The predictions of the SVR models start to deviate from other mass models and underestimate the mass excess values compared to them near the drip lines.

Finally, we explore the one- and two-neutron separation energies calculated using the mass excess $M$ values obtained from our ML models and compare them with those from other models and available experimental data. The one and two neutron separation energies are calculated by

$$
S _ {n} = - M (A, Z) + M (A - 1, Z) + m _ {n},
$$

$$
S _ {2 n} = - M (A, Z) + M (A - 2, Z) + m _ {2 n}, \tag {4}
$$

where $m _ { n }$ represents the mass of the neutron. In the upper panels of Figure 5, the results are displayed for the one-neutron separation energies of Kr (a) and Nd (b) isotopic chains. It is evident that the ML models provide reasonable predictions and are in agreement with the experimental data, exhibiting the well-known oddeven staggering (OES) in binding energies. As the neutron number increases, the results also show comparability with other theoretical model calculations. However, near the drip lines, the ML models start to deviate from other model calculations.

In the lower panels of Fig. 5, the two-neutron separation energies are displayed for the Kr (c) and Nd (d) isotopic chains. It can be observed that the ML models make reasonable predictions for the Kr chain. In comparison to the SVR-12 model, the GPR-12 model’s predictions are more reasonable near the drip lines and follow a smooth decreasing behaviour with increasing neutron number. Additionally, the predictions of the GPR-12 model are comparable to the WS4 model, while the SVR-12 model results align with the BSK4 model as neutron number increases. When it comes to nuclei near the drip lines, the predictions of the SVR-12 model become inaccurate and exhibit an increasing pattern. The ML model predictions deviate from other mass models, particularly for heavier Nd nuclei. It is also seen that the uncertainty in the GPR-12 predictions is higher for this chain in the extrapolation region. This discrepancy is a natural consequence of both the limited number of available experimental data points and the absence of information in

![](images/9253d2beac4c8e9b7b774f0e64cd42fd4bff89156371ad28c6507892e268c03f.jpg)

![](images/12a8652d405b59b58a63f1846b231510544cc8c2a70ae4e427f88f0b8f953478.jpg)

![](images/a8130f12a8b75f0e8e51f2abd39d0e179c114f12cb2d9f3893fdf9355964b341.jpg)

![](images/8dadb45d4bc818198f69bbb0549e9a76186f8cf3be65fb48c8454725887711d9.jpg)

![](images/a60797ec15fc0353a4eea02a32c4ae7ca050326ee429d17e1d6d7dafeba08633.jpg)

![](images/8eeaec6d972f120a56971b71fefbb3de28aff5806758eb259a979c7708d6ab22.jpg)  
FIG. 3: The GPR-5 and SVR-5 mass excess predictions are shown for the selected isotopic chains as a function of the neutron number. The blue shaded region represents the $9 5 . 0 \%$ confidence interval, and the gray region indicates the training and test set area, while the white region is used as extrapolation region. The estimated values for the mass excess predictions, away from the training and test set region, are derived from the trends in the mass surface (TMS) and are taken from Ref. [4]. Predictions of other mass models: mic-mac model WS4 [6], non-relativistic Skyrme-type BSk24 interaction [20], and relativistic point-coupling interaction DD-PCX [15, 47], are also provided for comparison.

![](images/ad74a9f45890ca4802de75b9de1d69e1ffd7679d49d37116038a54a8dc8dc84b.jpg)

![](images/f5ad1159c65a9baa602b0e0ab0a954840bfa9e61a169c9713f9b93ebef7fb0f3.jpg)

![](images/28ce135ebed86e53bcfe70f8aa4541475b123421c74f82c7f5d7ee9ac20c2089.jpg)

![](images/20ca41b21d1729ec8fad5daf65381a1865f117dc03dfa1d18bdd6686c71222a0.jpg)

![](images/4a7fed9479dfefef61219fd8c82a28c866bf239956ba6b421ee347fc7e247cf2.jpg)

![](images/a37a4e1f33f3cdccf84bb57771cd043a3ed670464825410c7ee0bb6619ee2ae7.jpg)  
FIG. 4: The same as in Fig. 3 but using GPR-12 and SVR-12 ML models.

![](images/e7d11e798af2688c25ac7ea5410dcf5e63d89d075be72de341d0d9611d831aa8.jpg)  
N e u t r o n n u m b e r ( N )

![](images/9aa73399f5885b2f95ed7ba3dd8ff46d9db824225a8faf499fe555c317ffeda5.jpg)  
N e u t r o n n u m b e r ( N )

![](images/7a8ff4d483b6a374ca8234545aae8b14c592e564a485cbb8c0e2ec186b2206fe.jpg)  
N e u t r o n n u m b e r ( N )

![](images/155083c6f787703c15956d12d0550a2ab29e65b4ab7a1f67b2c19220b468adf2.jpg)  
N e u t r o n n u m b e r ( N )   
FIG. 5: Upper panels: one-neutron separation energies for Kr (a) and Nd (b) isotopic chains using GPR-12 and SVR-12 models. Lower panels: two-neutron separation energies for Kr (c) and Nd (d) isotopic chains. The blue shaded region represents the $9 5 . 0 \%$ confidence interval. Theoretical model calculations (WS4, BSk24, DD-PCX) and experimental data are also provided when available [4].

the physics-based feature space in this particular region.

Do the results of the ML models satisfy the Garvey-Kelson mass relations? The Garvey-Kelson relations [49], which are based on the independent particle shell model, consist of mathematical expressions that establish links among the masses of neighboring nuclides. These relations arise from the condition that various interactions between nucleons cancel out at the first order, resulting in a series of mass relations between adjacent nuclei [49, 50]. The GK mass relation for nuclei with $N \geq Z$ is given by

$$
\begin{array}{l} M (Z - 2, N + 2) - M (Z, N) \\ + M (Z - 1, N) - M (Z - 2, N + 1) \tag {5} \\ + M (Z, N + 1) - M (Z - 1, N + 2) \approx 0, \\ \end{array}
$$

and for nuclei with $Z < N$

$$
\begin{array}{l} M (Z + 2, N - 2) - M (Z, N) \\ + M (Z, N - 1) - M (Z + 1, N - 2) \tag {6} \\ + M (Z + 1, N) - M (Z + 2, N - 1) \approx 0. \\ \end{array}
$$

Using the results obtained from the GPR-12 and SVR-12 models, we also assess whether the GK relations are

maintained in our ML models, serving as an additional evaluation of the ML models and their extrapolation abilities. In Fig. 6, we present the results of the GK relationship described by Eqs. 5 and 6. It is evident that the GK relationships are well maintained within the training and test set regions for the ML models under consideration. However, deviations become apparent with increasing proton and neutron numbers, especially for low mass nuclei and throughout the neutron drip lines. Interestingly, while the GPR-12 model seems to perform better than the SVR-12 model near the neutron drip line (see Fig. 5), we find that the SVR-12 model exhibits better performance in the neutron-rich region concerning the GK mass relations. The differences between GPR and SVR predictions can be attributed to their distinct mathematical principles and model complexities. Including physical constraints, such as GK mass relations, alongside the physical feature space in the ML models, may enhance the model predictions in the extrapolation region [31].

Explainable AI - The implementation of ML models often faces the challenge of their perceived ‘black box’ nature. To counter this issue, Explainable AI (XAI)

![](images/fbdc5b4ecfa13d9c7d327908bdaa712f4c66ebff737b90d84fc350880f4ad26b.jpg)

![](images/1c15b75516c53ab3be078e0751998b9d7103e73284fa7cbb8c773a191630b8ba.jpg)  
FIG. 6: The GK mass relations for the results obtained using the (a) GPR-12 and (b) SVR-12 ML models. The dashed gray lines indicate the borders of the training and test set regions.

techniques have become increasingly popular for their role in demystifying these models and enhancing understanding. Among a range of XAI techniques, SHapley Additive exPlanations (SHAP) [51] has emerged as a prominent technique that has achieved widespread recognition.

The SHAP technique utilizes the concept of SHAP values, derived from Game Theory, which illustrates the individual contributions of players in a cooperative coalition. This concept, originally known as Shapley values [52], has been extensively studied in game theory literature [53]. Recently adapted to AI research, specifically in XAI, this approach treats model features as ‘players’ and the prediction as the ‘game’. SHAP values assigned to these features indicate their relative importance compared to a baseline reference. Thus, this technique effectively highlights the features most influential in the model’s decision-making process.

![](images/7fbaebfc1e233c91041a778729a39703f745a99a5b74a73a32067f8f4cb60b98.jpg)  
FIG. 7: SHAP summary plot for the GPR-12 model. Each input is represented by a horizontal bar on the plot, where the length of the bar reflects the SHAP values’ magnitude. The color of each bar indicates the direction of the feature’s influence on the prediction: blue for a decrease with lower feature values and red for an increase with higher feature values, with the intensity of the color denoting the magnitude of the feature’s value.

We apply the SHAP technique to interpret the results of the GPR-12 model more in depth. For the test dataset, we compute the SHAP values, where each value indicates the contribution of a specific feature to the model’s prediction. These SHAP values are visually summarized in the Figure 7. The SHAP summary plot offers an insightful illustration of how each feature influences the predictions by the GPR-12 model. In this plot, features are ordered on the y-axis based on their impact, with the most impactful feature positioned at the top and the least impactful at the bottom. To manage the extensive computational demands of calculating SHAP values for the GPR-12 model, we adhered to the guidelines suggested in the official SHAP documentation [54], utilizing k-means clustering on the training data. We condensed the training data into three clusters using k-means, assigning weights to each cluster proportionate to the number of data points it encompasses. Experiments with varying numbers of clusters, including more than three, consistently yielded comparable results.

The analysis reveals that $A ^ { 2 / 3 }$ is the most impactful factor in predicting the mass, as shown by the SHAP values. It is closely followed by $Z$ , $A$ and $N$ , both making noteworthy contributions to the model’s predictions. In contrast, $Z _ { e o }$ and $N _ { e o }$ demonstrate a limited impact on predicting the mass, as indicated by their lower placement on the plot. Nonetheless, their inclusion is important to improve model predictions as we explain above in Fig.2. The SHAP values depicted in the Figure 7 clearly show the extent of each input’s contribution

![](images/3e54165fdaeeb7324cc62b8f6111f343aaf948456bcf38634063619541b859ca.jpg)

![](images/0143675cf085581f9a73826adb78207dfa170ccfd60cd3c85c6eab376ef7fec6.jpg)

![](images/458cbd53655a2fd019518d17078f3e192211096da734784d8792825fc9b507f5.jpg)

![](images/789e1b9c1d9c3c723c2734bd3f87f22677ad191eae3814534b3a295ec936f7cd.jpg)

![](images/6ce4391a8ef8de8db70d475f38a44b77b1939ee02b39567e848091edd72f64be.jpg)

![](images/118dd31a20f7fff4232f517e9574775d7aa958e30ff6cbe102b6eb1980cbffa3.jpg)  
FIG. 8: Selected SHAP interaction plots. In these plots, an intense red color indicates higher positive SHAP values, while a deep blue color signifies lower negative SHAP values.

to individual predictions. The $x$ -axis represents the relative importance of each feature based on their SHAP values. Inputs with larger absolute SHAP values indicate a more significant effect on the model’s predictions, whereas those with smaller absolute values have a lesser influence. It is worth noting that we also examined the SHAP summary plot for the SVR-12 model, and the results are found to be identical. In Figure 7, the contributions of features beyond the top five may appear minimal. However, as previously explained, the GPR-12 model outperforms its versions with fewer features (see

Fig. 2). This enhanced performance of the GPR-12 model can be attributed to the interactions between features, which can also be examined in detail through SHAP analysis. The SHAP analysis provides us with the opportunity to visualize the binary interactions between features. Although we can pinpoint the most impactful features in the ML models using SHAP summary plots as shown in Figure 7, interactions between these features also play an important role in the models’ performance. SHAP interaction plots provide us with an opportunity to observe the interactions of features across different

parts of the nuclear chart and better understand the working mechanism of the ML models by making them more transparent.

In Figure 8, we present selected interaction plots derived from the SHAP values of the GPR-12 model. While many interaction plots can be generated based on SHAP analysis, we choose to focus on interactions between the feature proton number $Z$ and others to simplify our discussion. A majority of red in the interaction plots suggest a positive joint contribution of both features to the model’s prediction. This means that higher values of these features together are likely to elevate the model’s output. In contrast, a majority of blue suggests that the combined features negatively influence the model’s prediction, with lower values of both features together expected to decrease the model’s output. Thus, we can pinpoint critical feature interactions and enhance our understanding of the model’s decision-making based on feature combinations. For instance, the combined effect of higher values of $Z$ and $A$ (see Fig. 8(a)) impacts the model’s prediction positively, while lower values have a negative impact on the output. A similar situation is also observed among $Z$ , $\nu _ { N }$ (c), and $Z _ { \mathrm { s h e l l } }$ (f). It is also seen that the interaction between $Z$ and $P F$ (e) shows variations according to the region of interest. Nonetheless, low values of $Z$ and $P F$ have a negative impact on the output. On the other hand, there is no such interaction between $Z$ and $( N - Z ) / A$ or $Z _ { e o }$ , as shown in panels (b) and (d) of Fig. 8. The combined effects of $Z$ and $( N - Z ) / A$ , and $Z$ and $Z _ { e o }$ can demonstrate both positive and negative impacts across all regions. It is clear that, in the majority of plots, the interaction of proton number $Z$ with other features demonstrates a negative impact on the predictions of nuclei with low mass. Similar results are also observed for other impactful features, such as the neutron number ( $N$ ) and mass number ( $A$ ), indicating the necessity to identify relevant features to probe these regions more

effectively. Therefore, interaction plots can be useful for identifying the relevant features to enhance predictions of ML models in regions with low prediction capability.

# IV. CONCLUSION

This study presents successful implementations of two ML models, SVR and GPR, using the available experimental data and physics-based feature space to make predictions for the mass excess of atomic nuclei. The ML models achieve good results not only in accurately predicting nuclear mass excesses for training and test sets but also in demonstrating robust extrapolation capabilities. Our comprehensive analysis, which includes the extrapolation region using the newly measured data from AME2020 and the region beyond, underscores the models’ success in handling a diverse range of nuclear data. In addition to demonstrating the effective application of ML models, our study incorporates SHAP, an Explainable AI (XAI) technique, enhancing the interpretability of our ML models.

It is evident that SVR and GPR can be effectively utilized as reliable and efficient tools for predicting mass excess of atomic nuclei. This study highlights the potential of these ML models as powerful tools in nuclear physics and opens up new avenues for future research. These ML models can be further refined to improve their performance, especially near the drip lines. While the chosen ML models demonstrated success in predicting the mass excess of atomic nuclei, their potential applications in exploring additional nuclear properties and evaluating their performance remain as tasks for future research.

# V. ACKNOWLEDGEMENTS

E.Y. acknowledges support from the Science and Technology Facilities Council (UK) through Grant No. ST/Y000013/1.

[1] M. R. Mumpower, R. Surman, D.-L. Fang, M. Beard, P. M¨oller, T. Kawano, and A. Aprahamian, Phys. Rev. C 92, 035807 (2015).   
[2] D. Martin, A. Arcones, W. Nazarewicz, and E. Olsen, Phys. Rev. Lett. 116, 121101 (2016).   
[3] and, F. G. Kondev, , and S. N. and, Chinese Physics C 41, 030003 (2017).   
[4] M. Wang, W. Huang, F. Kondev, G. Audi, and S. Naimi, Chinese Physics C 45, 030003 (2021).   
[5] D. S. Ahn, N. Fukuda, H. Geissel, N. Inabe, N. Iwasa, T. Kubo, K. Kusaka, D. J. Morrissey, D. Murai, T. Nakamura, M. Ohtake, H. Otsu, H. Sato, B. M. Sherrill, Y. Shimizu, H. Suzuki, H. Takeda, O. B. Tarasov, H. Ueno, Y. Yanagisawa, and K. Yoshida, Phys. Rev. Lett. 123, 212501 (2019).

[6] N. Wang, M. Liu, X. Wu, and J. Meng, Physics Letters B 734, 215 (2014).   
[7] P. M¨oller, A. Sierk, T. Ichikawa, and H. Sagawa, Atomic Data and Nuclear Data Tables 109-110, 1 (2016).   
[8] K. Zhang, M.-K. Cheoun, Y.-B. Choi, P. S. Chong, J. Dong, Z. Dong, X. Du, L. Geng, E. Ha, X.-T. He, C. Heo, M. C. Ho, E. J. In, S. Kim, Y. Kim, C.-H. Lee, J. Lee, H. Li, Z. Li, T. Luo, J. Meng, M.-H. Mun, Z. Niu, C. Pan, P. Papakonstantinou, X. Shang, C. Shen, G. Shen, W. Sun, X.-X. Sun, C. K. Tam, Thaivayongnou, C. Wang, X. Wang, S. H. Wong, J. Wu, X. Wu, X. Xia, Y. Yan, R. W.-Y. Yeung, T. C. Yiu, S. Zhang, W. Zhang, X. Zhang, Q. Zhao, and S.-G. Zhou, Atomic Data and Nuclear Data Tables 144, 101488 (2022).

[9] X. Xia, Y. Lim, P. Zhao, H. Liang, X. Qu, Y. Chen, H. Liu, L. Zhang, S. Zhang, Y. Kim, and J. Meng, Atomic Data and Nuclear Data Tables 121-122, 1 (2018).   
[10] A. V. Afanasjev and S. E. Agbemava, Phys. Rev. C 93, 054310 (2016).   
[11] A. V. Afanasjev, S. E. Agbemava, D. Ray, and P. Ring, Phys. Rev. C 91, 014324 (2015).   
[12] S. E. Agbemava, A. V. Afanasjev, D. Ray, and P. Ring, Phys. Rev. C 89, 054320 (2014).   
[13] J. Erler, N. Birge, M. Kortelainen, W. Nazarewicz, E. Olsen, A. M. Perhac, and M. Stoitsov, Nature 486, 509 (2012).   
[14] G. Grams, W. Ryssens, G. Scamps, S. Goriely, and N. Chamel, The European Physical Journal A 59, 270 (2023).   
[15] A. Ravli´c, E. Y¨uksel, T. Nikˇsi´c, and N. Paar, Phys. Rev. C 108, 054305 (2023).   
[16] A. Ravli´c, E. Y¨uksel, T. Nikˇsi´c, and N. Paar, Phys. Rev. C 109, 014318 (2024).   
[17] A. Ravli´c, E. Y¨uksel, T. Nikˇsi´c, and N. Paar, Nature Communications 14, 4834 (2023).   
[18] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 88, 024308 (2013).   
[19] R. Utama and J. Piekarewicz, Phys. Rev. C 96, 044308 (2017).   
[20] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 88, 061302 (2013).   
[21] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 93, 034337 (2016).   
[22] A. Boehnlein, M. Diefenthaler, N. Sato, M. Schram, V. Ziegler, C. Fanelli, M. Hjorth-Jensen, T. Horn, M. P. Kuchera, D. Lee, W. Nazarewicz, P. Ostroumov, K. Orginos, A. Poon, X.-N. Wang, A. Scheinker, M. S. Smith, and L.-G. Pang, Rev. Mod. Phys. 94, 031003 (2022).   
[23] S. Gazula, J. Clark, and H. Bohr, Nuclear Physics A 540, 1 (1992).   
[24] J. W. Clark and H. Li, International Journal of Modern Physics B 20, 5015–5029 (2006).   
[25] S. Athanassopoulos, E. Mavrommatis, K. Gernoth, and J. Clark, Nuclear Physics A 743, 222 (2004).   
[26] E. Y¨uksel, D. Soydaner, and H. Bahtiyar, International Journal of Modern Physics E 30, 2150017 (2021).   
[27] H. Bahtiyar, Derya, and E. Y¨uksel, Applied Soft Computing 128, 109470 (2022).   
[28] C.-Q. Li, C.-N. Tong, H.-J. Du, and L.-G. Pang, Phys. Rev. C 105, 064306 (2022).   
[29] M. Shelley and A. Pastore, Universe 7, 10.3390/universe7050131 (2021).   
[30] A. E. Lovell, A. T. Mohan, T. M. Sprouse, and M. R. Mumpower, Phys. Rev. C 106, 014305 (2022).

[31] M. R. Mumpower, T. M. Sprouse, A. E. Lovell, and A. T. Mohan, Phys. Rev. C 106, L021301 (2022).   
[32] M. Mumpower, M. Li, T. M. Sprouse, B. S. Meyer, A. E. Lovell, and A. T. Mohan, Frontiers in Physics 11, 10.3389/fphy.2023.1198572 (2023).   
[33] R. Utama and J. Piekarewicz, Phys. Rev. C 97, 014306 (2018).   
[34] Z. Niu and H. Liang, Physics Letters B 778, 48 (2018).   
[35] L. Neufcourt, Y. Cao, W. Nazarewicz, and F. Viens, Phys. Rev. C 98, 034318 (2018).   
[36] L. Neufcourt, Y. Cao, W. Nazarewicz, E. Olsen, and F. Viens, Phys. Rev. Lett. 122, 062502 (2019).   
[37] H. Drucker, C. Burges, L. Kaufman, A. Smola, and V. Vapnik, Advances in Neural Information Processing Systems 9 (1996).   
[38] B. Boser, I. Guyon, and V. Vapnik, Proceedings of the Fifth Annual Workshop on Computational Learning Theory , 144 (1992).   
[39] A. G´eron, Hands-On Machine Learning with Scikit-Learn & Tensorflow (O’Reilly Media, Inc., 2017) pp. 154–156.   
[40] B. Sch˝olkopf and A. Smola, Learning with kernels: support vector machines, regularization, optimization, and beyond (MIT Press, 2002).   
[41] D. Soydaner and J. Wagemans, British Journal of Psychology 00, 1 (2024).   
[42] D. MacKay, Introduction to Gaussian Processes, Neural networks and machine learning (Springer, 1998) pp. 133– 166.   
[43] E. Alpaydın, Introduction to Machine Learning (MIT Press, 2014) pp. 474–478.   
[44] C. Rasmussen and C. Williams, Gaussian Processes for Machine Learning (MIT Press, 2006).   
[45] R. F. Casten and N. V. Zamfir, Journal of Physics G: Nuclear and Particle Physics 22, 1521 (1996).   
[46] K. Vogt, T. Hartmann, and A. Zilges, Physics Letters B 517, 255 (2001).   
[47] E. Y¨uksel, T. Marketin, and N. Paar, Phys. Rev. C 99, 034318 (2019).   
[48] T. Nikˇsi´c, N. Paar, D. Vretenar, and P. Ring, Computer Physics Communications 185, 1808 (2014).   
[49] G. T. Garvey, W. J. Gerace, R. L. Jaffe, I. Talmi, and I. Kelson, Rev. Mod. Phys. 41, S1 (1969).   
[50] J. Barea, A. Frank, J. G. Hirsch, P. V. Isacker, S. Pittel, and V. Vel´azquez, Phys. Rev. C 77, 041304 (2008).   
[51] S. Lundberg and S. Lee, Advances in Neural Information Processing Systems 30, 061302 (2017).   
[52] L. Shapley, Contributions to the Theory of Games II , 307–317 (1953).   
[53] E. Winter, Handbook of Game Theory with Economic Applications 3, 2025–2054 (2002).   
[54] Https://shap-lrjball.readthedocs.io/en/latest/examples.html.