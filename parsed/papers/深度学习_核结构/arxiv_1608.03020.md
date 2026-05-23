# Nuclear charge radii: Density functional theory meets Bayesian neural networks

R. Utama,1, ∗ Wei-Chia Chen,1, † and J. Piekarewicz1, ‡

$^ { 1 }$ Department of Physics, Florida State University, Tallahassee, FL 32306

(Dated: August 30, 2018)

Background: The distribution of electric charge in atomic nuclei is fundamental to our understanding of the complex nuclear dynamics and a quintessential observable to validate nuclear structure models.

Purpose: To explore a novel approach that combines sophisticated models of nuclear structure with Bayesian neural networks (BNN) to generate predictions for the charge radii of thousands of nuclei throughout the nuclear chart.

Methods: A class of relativistic energy density functionals is used to provide robust predictions for nuclear charge radii. In turn, these predictions are refined through Bayesian learning for a neural network that is trained using residuals between theoretical predictions and the experimental data.

Results: Although predictions obtained with density functional theory provide a fairly good description of experiment, our results show significant improvement (better than 40%) after BNN refinement. Moreover, these improved results for nuclear charge radii are supplemented with theoretical error bars.

Conclusions: We have successfully demonstrated the ability of the BNN approach to significantly increase the accuracy of nuclear models in the predictions of nuclear charge radii. However, as many before us, we failed to uncover the underlying physics behind the intriguing behavior of charge radii along the calcium isotopic chain.

PACS numbers: 21.60.Jz,24.10.Jv,21.10.Ft

# I. INTRODUCTION

Nuclear saturation, the existence of an equilibrium density, is one of the most fundamental manifestations of the complex nuclear dynamics. The successful liquid drop model (LDM), formulated by Bethe and Weizs¨acker shortly after the discovery of the neutron by Chadwick, is firmly rooted in the existence of an equilibrium density [1, 2]. In the LDM, the nucleus is treated as an incompressible quantum drop of uniform density $\rho _ { 0 } \simeq 0 . 1 5 \mathrm { f m } ^ { - 3 }$ consisting of $Z$ protons, $N$ neutrons, and a total baryon number of $A = N + Z$ . Among the best-known consequences of nuclear saturation is the fact that the average size of the nucleus scales with the total number of nucleons as $A ^ { 1 / 3 }$ . That is,

$$
R _ {0} (A) = r _ {0} A ^ {1 / 3} \text {w h e r e} r _ {0} = \left(\frac {3}{4 \pi \rho_ {0}}\right) ^ {1 / 3} \simeq 1. 1 5 \mathrm {f m}. \tag {1}
$$

In turn, the root-mean-square (RMS) charge radius of such a uniform distribution is given by

$$
R _ {\mathrm {c h}} ^ {\mathrm {L D M}} (A) = \sqrt {\frac {3}{5}} r _ {0} A ^ {1 / 3}. \tag {2}
$$

In an effort to improve the quantitative standing of the LDM, microscopic-macroscopic (“mic-mac”) models have been developed to account for the physics that is missing from such a simple description. Although most of these efforts have been devoted to improve nuclear-mass predictions [3–6], significant activity has also been dedicated to refine the description of charge radii. For stable heavy nuclei with a large volume-to-surface ratio, the LDM estimates provide a qualitative—and often quantitative—description of experimental charge radii. However, given its description of the nucleus as a uniform liquid drop with a sharp density, the LDM fails to reproduce the charge radii of light nuclei that are dominated by surface effects [7]. In an attempt to account for the nuclear surface, Myers and Schmidt introduced a gaussian modification to the sharp density of the form $\exp ( - r ^ { 2 } / 2 b ^ { 2 } )$ , with a best-fit parameter b = 0.99 fm independent of $N$ and $Z$ [8]. Such form was inspired by the Helm form factor that was introduced six decades ago to analyze elastic scattering of electrons from nuclei [9]. The Helm form factor, namely, the Fourier transform of the underlying charge density, is defined as the product of two fairly simple form factors: one associated with a uniform sharp density and the other one with a gaussian distribution. In the refined model of Myers and Schmidt, referred hereafter as the “extended-liquid-drop” (ELD) model [7], the RMS charge radius of a nucleus with mass number $A$ is given by

$$
R _ {\mathrm {c h}} ^ {\mathrm {E L D}} (A) = \sqrt {\frac {3}{5}} r _ {0} A ^ {1 / 3} \left(1 + \alpha A ^ {- 2 / 3} - \beta A ^ {- 4 / 3}\right), \tag {3}
$$

where $\alpha { = } 1 . 5 7$ and $\beta { = } 1 . 0 4$ were obtained by fitting to the then available experimental data [8]. Although the ELD provides a definite improvement over the original LDM, its sole dependence on $A$ , rather than on both $Z$ and $A$ , suggests that some serious deficiencies remain. Nevertheless, the ELD model provides a useful baseline to test our approach. As a more recent mic-mac representative, we include the simple, yet fairly successful, model by Zhang and collaborators [10]. In this model the charge radius is parametrized as follows:

$$
R _ {\mathrm {c h}} (Z, A) = r _ {A} A ^ {1 / 3} \left[ 1 - b \left(\frac {N - Z}{A}\right) + \frac {c}{A} \right], \tag {4}
$$

where $r _ { A } = 0 . 9 6 6 \mathrm { f m } , \ b = 0 . 1 8 2$ and $c = 1 . 6 5 2$ . Note that whereas the adopted model is from Ref. [10], the model parameters are from the more recent—and accurate—calibration by Bayram et al.; see Table I of Ref. [11].

However, we expect that our suggested approach will find its best expression in a method that combines predictions from an accurately-calibrated density functional which are subsequently refined through the use of a Bayesian Neural Network (BNN). Although enormous progress has been made in the design of nuclear energy density functionals [12– 17], the reality is that some lingering discrepancy between theory and experiment is inevitable. The aim of Bayesian learning is to eliminate, or at least to significantly reduce, these discrepancies. Such an approach has already been successfully tested in the case of nuclear masses of relevance to the composition of the neutron-star crust [18]. Motivated by some intriguing new measurements in the calcium isotopes [19], we extend our formalism to predict nuclear charge radii across the whole nuclear landscape. In essence, our underlying theoretical approach is rooted in Strutinsky’s energy theorem [20] which states that the nuclear binding energy may be separated into two components: one large and smooth and the other one small and fluctuating [21]. Moreover, we successfully conjectured that Strutinsky’s energy theorem may be extended to any nuclear observable that also displays slowly varying dynamics [22]. In particular, it was shown that the Garvey-Kelson relations [23–25] provide a fruitful framework for the prediction of nuclear charge radii [22]. Indeed, besides successfully testing the Garvey-Kelson relations (GKRs) on hundreds of nuclei whose

charge radius is experimentally known, we made predictions for 116 nuclei whose charge radius was unknown at that time [22]; for a similar treatment see Ref. [26]. Unfortunately, the GKRs are local relations whose success depends critically on the knowledge of the landscape around the nucleus of interest. Hence, though enormously successful when measurements on the nearest neighbors to the nucleus of interest exist, the GKRs extrapolate poorly. Thus, it is our hope that by properly implementing a global description through Bayesian learning of neural networks some of these deficiencies will be mitigated.

Together with nuclear masses, nuclear sizes are among the most fundamental properties of atomic nuclei. With the commissioning of radioactive beam facilities all over the world, understanding the limits of nuclear existence, particularly the evolution of nuclear masses and sizes, represents one of the overarching questions that animate nuclear physics today. Regarding the charge radii of nuclei with a large neutron excess, a recent laser spectroscopy experiment at ISOLDE, CERN has observed “unexpectedly large charge radii of neutron-rich calcium isotopes” [19]. Although considerable theoretical progress has been made in reproducing—and predicting—the evolution of nuclear masses along the calcium isotopes [17, 27, 28], predicting the complex evolution of the corresponding charge radii remains a serious challenge for theoretical descriptions that range from ab initio methods to density functional theory (DFT) [19]. In an effort to gain some insights into this problem, we extend the (BNN) approach implemented for the first time in Ref. [22] to nuclear charge radii. In doing so, we follow closely the ideas outlined in the text by R.M. Neal entitled Bayesian Learning for Neural Networks [29]. To explore the foundations and applications of artificial neural networks see Refs. [30–32]. We note that the first application of artificial neural networks to nuclear physics dates back to the early 1990s and continues to this day in the work of Clark and collaborators [33–40]. Artificial neural networks have also been used in these studies to reproduce, among other things, (a) the differences between experimental nuclear masses and theoretical predictions provided by the Finite Range Droplet Models (FRDM) and (b) $\beta$ -decay rates of relevance to r-process nucleosynthesis. More recently, artificial neural networks have been used in the study of binding-energy systematics [41] and nuclear charge radii [42].

We have organized the paper as follows. In Sec. II we describe briefly the relativistic density functional that is used to predict charge radii throughout the nuclear chart. Following this discussion, we review the main ideas involved in training and validating a neural network by concentrating on the residuals between theoretical predictions and experimental measurements of charge radii, as obtained from the latest compilations by Angeli and collaborators [43, 44]. We then proceed to Sec. III to display the results of our calculations with a special emphasis on the BNN refinement of the “bare” model predictions. Finally, in Sec. IV we summarize our work.

# II. FORMALISM

The formalism section is composed of two subsections that briefly address topics that have been discussed in great detail in the existent literature. These are: (a) the calibration and predictions of a particular class of relativistic density functionals and (b) the Bayesian learning approach for neural networks.

# A. Relativistic Energy Density Functionals

The effective relativistic model employed here is inspired in the original work of Walecka from the mid 1970s [45] and continues to this day with refinements that systematically improve the quantitative predictions of the model. Besides providing an accurate description of finite nuclei, the relativistic approach offers a Lorentz covariant extrapolation to high-density matter, a critical fact in the simulation of neutron stars. In such a framework, the basic degrees of freedom include nucleons that interact via the exchange of three “mesons” and the photon. The effective Lagrangian density for this class of models is given by [16, 17, 45–54]:

$$
\begin{array}{l} \mathcal {L} _ {\mathrm {i n t}} = \bar {\psi} \left[ g _ {\mathrm {s}} \phi - \left(g _ {\mathrm {v}} V _ {\mu} + \frac {g _ {\rho}}{2} \pmb {\tau} \cdot \mathbf {b} _ {\mu} + \frac {e}{2} (1 + \tau_ {3}) A _ {\mu}\right) \gamma^ {\mu} \right] \psi \\ - \frac {\kappa}{3 !} \left(g _ {\mathrm {s}} \phi\right) ^ {3} - \frac {\lambda}{4 !} \left(g _ {\mathrm {s}} \phi\right) ^ {4} + \frac {\zeta}{4 !} g _ {\mathrm {v}} ^ {4} \left(V _ {\mu} V ^ {\mu}\right) ^ {2} + \Lambda_ {\mathrm {v}} \left(g _ {\rho} ^ {2} \mathbf {b} _ {\mu} \cdot \mathbf {b} ^ {\mu}\right) \left(g _ {\mathrm {v}} ^ {2} V _ {\nu} V ^ {\nu}\right). \tag {5} \\ \end{array}
$$

Note that here $\psi$ represents the isodoublet nucleon field, $A _ { \mu }$ the photon field, and $\phi$ , $V _ { \mu }$ , and ${ \mathbf { b } } _ { \mu }$ the isoscalar-scalar $\sigma$ -, isoscalar-vector $\omega$ -, and isovector-vector $\rho$ -meson fields, respectively. The first line of the above equation contains the conventional Yukawa couplings between the nucleons and the mesons. In the original Walecka model (also knows as the “ $o$ - $\omega$ model”) only the two isoscalar mesons were considered [45]. Nevertheless, such a simple description was already able to provide a natural and compelling explanation for the mechanism behind nuclear-matter saturation. Later on, Horowitz and Serot added the isovector $\rho$ -meson and the photon to provide a highly improved description of the ground-state properties of finite nuclei [47]. The second line in Eq. (5) includes nonlinear self and mixed interactions

among the meson fields that effectively generate many-body (or density-dependent) interactions. The need for such kind of terms was recognized early on by Boguta and Bodmer who introduced the two isoscalar parameters, $\kappa$ and $\lambda$ , to soften the equation of state of symmetric nuclear matter in the vicinity of the saturation density [46]. In turn, $\zeta$ may be used to calibrate the equation of state at high density from the astrophysical determination of neutron-star masses. Note that this may be done without sacrificing the good agreement with physical observables sensitive to the equation of state near saturation density [49]. Finally, $\Lambda _ { \mathrm { v } }$ is the only parameter that involves a mixing between the isoscalar and isovector sectors. As such, $\Lambda _ { \mathrm { v } }$ may be efficiently tuned to soften the density dependence of symmetry energy, which is traditionally stiff in relativistic mean-field models that contain only one single isovector parameter.

# B. Bayesian Neural Networks

Despite the steady and considerable progress that has been achieved in the design of nuclear mass models and energy density functionals, often the accuracy achieved is inadequate to properly describe astrophysical phenomena. For example, it appears that in order to resolve the abundance pattern in r-process nucleosynthesis, mass uncertainties must be reduced by factors of 3-5 from their current limit (to . 100 keV); see Ref. [55] and references contained therein. Moreover, given the suggestion of an inherent limit to the accuracy of mass models [56, 57], a novel approach is sorely needed. The novel approach that we advocate here is Bayesian learning for neural networks [29]. In the particular case of nuclear observables, we propose a combined scheme that relies on accurate model predictions which are then refined by training a suitable neural network on the residuals between the experimental data and the theoretical predictions. We have successfully tested such paradigm in the case of nuclear masses [18]. In this work we extend the approach to the description of nuclear charge radii.

Although a detailed description of Bayesian neural networks goes beyond the scope of this paper, we nevertheless highlight some of the main features that are critical to the implementation. First, multilayer feed-forward neural networks have been shown to be “universal approximators”, as they are capable of approximating any measurable function from one finite dimensional space to another to any desired degree of accuracy [58]. Given that we advocate an approach where the first step is the design of a model that incorporates as much physics as possible, we expect that the experiment-theory residuals will be a smooth function which may be faithfully emulated with a relatively simple neural network. Second, Bayesian learning requires specifying a prior distribution that captures our beliefs prior to unveiling the data. Once the data is unveiled, the posterior distribution is used to make predictions with properly quantified uncertainties about future measurements. Note that the posterior distribution encodes the improvement in our prior knowledge as a result of the new data. Finally, the Bayesian approach with the selection of a robust prior is less prone to overfitting the training data [29, 59]; unfortunately, the prior selection of neural network parameters has no obvious connection to our prior physics knowledge [58].

Statistical inference based on Bayes’ theorem connects a given hypothesis (in terms of our beliefs for a set of parameters $\omega$ ) and a set of data $( x , t )$ to a posterior probability $p ( \omega | x , t )$ that is used to make predictions on future data [60]. That is,

$$
p (\omega | x, t) = \frac {p (x , t | \omega) p (\omega)}{p (x , t)}, \tag {6}
$$

where $p ( \boldsymbol { x } , t | \omega )$ is the “likelihood” that a given model describes the data and $p ( \omega )$ is the prior distribution of the parameters $\omega$ . Following common practices, we assume a Gaussian distribution for the likelihood in terms of an objective (or “cost”) function obtained from a least-squares fit to the empirical data. That is,

$$
p (x, t | \omega) = \exp (- \chi^ {2} (\omega) / 2), \tag {7}
$$

where $\chi ^ { 2 } ( \omega )$ is given by

$$
\chi^ {2} (\omega) = \sum_ {i = 1} ^ {N} \left(\frac {t _ {i} - f (x _ {i} , \omega)}{\Delta t _ {i}}\right) ^ {2}. \tag {8}
$$

Here $N$ is the number of empirical data, $t _ { i } \equiv t ( x _ { i } )$ is the ith observable with $\Delta t _ { i }$ its associated error, and the function $f ( x , \omega )$ (given below) depends on the input data $x$ and the model parameters $\omega$ . In our particular case, $x \equiv ( Z , A )$ denotes the two input variables (proton and mass numbers) and $t ( x ) \equiv \delta R _ { \mathrm { c h } } ( Z , A )$ the charge-radius residual, namely, the difference between the experimental data and the theoretical predictions as provided, for example, by a nuclear energy density functional. Unlike other approaches, Bayesian predictions are based on a large number of estimates of

the model parameters that are generated from the posterior distribution. That is,

$$
\langle f _ {n} \rangle = \int f (x _ {n}, \omega) p (\omega | x, t) d \omega = \frac {1}{K} \sum_ {k = 1} ^ {K} f (x _ {n}, \omega_ {k}), \tag {9}
$$

where $x _ { n } = \left( Z _ { n } , A _ { n } \right)$ represents a nucleus with charge $Z _ { n }$ and mass number $A _ { n }$ , and $f ( x _ { n } , \omega )$ is the neural network prediction for $\delta R _ { \mathrm { c h } } ( Z _ { n } , A _ { n } )$ for a given set of parameters $\omega$ . The Bayesian estimate of the average of $\delta R _ { \mathrm { c h } } ( Z _ { n } , A _ { n } )$ is obtained by integrating over the posterior parameter distribution using Markov Chain Monte Carlo (MCMC) sampling [29]; in Eq. (9) $K$ refers to the total number of Monte Carlo samples. A distinct advantage of the Bayesian method is that predictions for the averages can be complemented with a proper quantification of the uncertainty. Indeed, the statistical uncertainty is given by

$$
\Delta f _ {n} = \sqrt {\left\langle f _ {n} ^ {2} \right\rangle - \left\langle f _ {n} \right\rangle^ {2}}, \tag {10}
$$

where $\left. f _ { n } ^ { 2 } \right.$ is evaluated following the same procedure described in Eq. (9).

All that remains is to specify the form of the neural network function (or “emulator”) $f ( x , \omega )$ and the prior distribution $p ( \omega )$ . Note that we can ignore the marginal likelihood $p ( x , t )$ in Eq. (6) since as far as the MCMC is concerned, it represents an overall normalization factor independent of $\omega$ . In this work, as in our previous one [18], we use a feed-forward neural network model of the following form:

$$
f (x, \omega) = a + \sum_ {j = 1} ^ {H} b _ {j} \tanh  \left(c _ {j} + \sum_ {i = 1} ^ {I} d _ {j i} x _ {i}\right), \tag {11}
$$

where the model parameters are given by $\omega = \{ a , b _ { j } , c _ { j } , d _ { j i } \}$ , $H$ is the number of hidden nodes, and $I$ is the number of inputs. For two input variables (as in our case) the function in Eq. (11) contains a total of $1 + 4 H$ parameters. Naturally, a one-size-fits-all prescription for selecting the optimal number of hidden nodes $H$ is not available so a considerable amount of trial and error is required. An example of a neural network consisting of a single hidden layer with three nodes is shown in Fig. 1.

![](images/899fdbb24223c7ce727332e911f4e5f0673c688b94a4d83001439d469bac7122.jpg)  
FIG. 1. An example of a feed-forward neural network with a single hidden layer consisting of three nodes. In our case, two inputs define the nucleus of interest ( $Z$ and $A$ ) and a single output provides an estimate of $\delta R _ { \mathrm { c h } } ( Z , A )$ .

Prior probabilities encode our beliefs concerning the model parameters and are an essential ingredient of the Bayesian paradigm. This feature is highly desirable as it allows us to inject our own physics biases and intuition which are often well informed by previous data or experiences. Unfortunately, physics intuition is of no help in the design of the connection weights (i.e. model parameters) $\omega$ . In this case, one must rely on tried-and-true methods [29]. Following our earlier work [18], we assume all connection weights to be independent and adopt a Gaussian prior centered around zero and with four hyperparameters controlling the width of each set of the four connection weights $\omega = \{ a , b , c , d \}$ . As in Ref. [29], we assume a “gamma” probability distribution for each of the associated hyperparameters, properly adjusted so that it penalizes a large spread in the weights. For further details on methods for determining hyperparameters, see Refs. [61, 62].

# III. RESULTS

Having set up the formalism that will be implemented to describe and predict nuclear charge radii, we are now in a position to discuss our results. Predictions for charge radii will be made using a variety of macroscopic and

microscopic models that will then be refined through Bayesian training of neural networks. In most of these cases our predictions will be compared against experimental results using the compilations by Angeli and collaborators [43, 44]. Specifically, we start with an underlying nuclear model that provides predictions for charge radii all throughout the nuclear chart. Next, we refine the nuclear model predictions by focusing our attention on the residuals between the theoretical predictions and the experimental data. That is, the Bayesian learning is applied not to the overall predictions of the nuclear model but to the discrepancy. Namely, the target function defining the likelihood function in Eq. (7) is given by

$$
t (x) = \delta R _ {\mathrm {c h}} (x) = R _ {\mathrm {c h}} ^ {(\exp)} (x) - R _ {\mathrm {c h}} ^ {(\mathrm {t h})} (x). \tag {12}
$$

In essence, our aim in this two-prong approach is to include as much physics as possible in the underlying nuclear model and then hope that the Bayesian refinement will adequately capture most of the physics that is missing from the model [18].

Once the theoretical predictions from the nuclear model have been generated, the BNN refinement starts by separating the available experimental data into two disjoint sets: a learning set and a validation set. The learning set consists of a subset of nuclei contained within the experimental database that will be used to train the network, i.e., to determine the connection weights (or parameters) defined in Eq. (11). In contrast, the validation set comprises those other nuclei that, while still in the existent experimental database, were not used in the training of the network. If charge radii within the validation set are accurately reproduced, then one provides predictions for the charge radii of nuclei that have not yet been measured but are of particular interest to other applications or whose measurement may be critical in constraining nuclear models.

As of 2011, the available data set of experimental charge radii consisted of 820 nuclei beyond $^ { 4 0 }$ Ca (i.e., with $Z \ge 2 0$ and $A \geq 4 0$ ) [44]. We decided to ignore light nuclei because both the macroscopic and microscopic nuclear models used in this work are not particularly suitable to describe such region of the nuclear chart. For charge radii, the division between the learning set and the validation set follows the chronological progression of the compilations by Angeli and collaborators. That is, for the learning set we use the 722 nuclei (beyond $^ { 4 0 }$ Ca) available in the earlier 2004 compilation [43]. We then use the additional 98 new measurements reported in the latest compilation [44] as the validation set. It is important to note that this division between learning and validation sets differs from the one adopted in our earlier work on nuclear masses [18]. There, the selection of nuclei belonging to each set was done at random; this procedure will also be adopted later in the paper. Now, however, we immediately test the suitability of BNN to extrapolate into unknown regions of the nuclear chart. Other than this, the training of the network follows closely the procedure adopted previously. That is, with two input variables ( $Z$ and $A$ ) and $H = 4 0$ hidden nodes, a total of $1 + 4 H = 1 6 1$ weights must be calibrated. To do so, we use the Flexible Bayesian Modeling package by Neal described in detail in Ref. [29]. After an initial thermalization phase consisting of 500 sets, we accumulate data for a total of 100 iterations that are then used to determine the statistical properties of the charge radius of various nuclei, such as their averages and variances as in Eqs. (9) and (10). Finally, to assess the quality of the BNN refinement, i.e., the resulting neural network function $f ( x , \omega )$ , we compute the root-mean-square (rms) deviation between the theoretical predictions and the experimental data as

$$
\sigma_ {\mathrm {r m s}} ^ {2} = \frac {1}{X _ {\mathrm {v}}} \sum_ {x = 1} ^ {X _ {\mathrm {v}}} \left[ R _ {\mathrm {c h}} ^ {(\exp)} (x) - R _ {\mathrm {c h}} ^ {(\mathrm {t h})} (x) \right] ^ {2}, \tag {13}
$$

where in this case $X _ { \mathrm { v } } = 9 8$ is the total number of nuclei in the validation set.

We now proceed to tabulate the rms deviation as per Eq. (13) for a representative set of both mic-mac and purely microscopic models. Among the former, we include the ELD model of Myers [8] as well as the predictions from Zhang and collaborators [10] with the more accurate parametrization by Bayram et al. [11]; see Eqs. (3) and (4). As for the microscopic models, we rely on three accurately-calibrated relativistic energy density functionals, namely, NL3 [51], FSUGold [54], and FSUGarnet [17]. The model parameters for these three relativistic density functionals, as per Eq. (5), are tabulated in Table I. It is important to note that in addition to relativistic energy density functionals, non-relativistic models based on Skyrme interactions have been very successful in the description of charge radii; see for example Refs. [14, 15, 63] and references contained therein.

We display in Table II the rms deviation as predicted by the above set of models for the charge radius of all nuclei beyond $^ { 4 0 }$ Ca ( $Z \geq 2 0$ and $A \geq 4 0$ ) that appear in the latest compilation by Angeli and Marinova [44]. The table displays results for: (a) the learning set, consisting of the charge radii of the 722 nuclei tabulated in an earlier compilation [43]; (b) the validation set, that includes the 98 additional nuclei appearing in the latest compilation; and (c) the entire set of 820 nuclei. We observe that the “raw” predictions (i.e., before BNN refinement) generate rms deviations $\sigma _ { \mathrm { p r e } }$ of the order of several one-hundredth fermis. Yet, as expected from a model that only depends on the mass number

TABLE I. Model parameters for the accurately-calibrated relativistic energy density functionals used in this work. The models included are: NL3 [51], FSUGold [54], and FSUGarnet [17]. The parameter $\kappa$ and all the masses are given in MeV. In all cases the omega-meson, rho-meson, and nucleon masses have been fixed at $m _ { \mathrm { v } } = 7 8 2 . 5$ , $m _ { \rho } = 7 6 3$ , and $M = 9 3 9$ , respectively.   

<table><tr><td>Model</td><td>ms</td><td>gs2</td><td>g2v</td><td>g2ρ</td><td>κ</td><td>λ</td><td>ζ</td><td>Λv</td></tr><tr><td>NL3</td><td>508.194000</td><td>104.387100</td><td>165.585400</td><td>79.600000</td><td>3.859900</td><td>-0.015905</td><td>0.000000</td><td>0.000000</td></tr><tr><td>FSUGold</td><td>491.500000</td><td>112.199551</td><td>204.546943</td><td>138.470113</td><td>1.420333</td><td>+0.023762</td><td>0.060000</td><td>0.030000</td></tr><tr><td>FSUGarnet</td><td>496.939473</td><td>110.349189</td><td>187.694676</td><td>192.927428</td><td>3.260179</td><td>-0.003551</td><td>0.023499</td><td>0.043377</td></tr></table>

$A$ , the worst performance is displayed by the ELD model. However, once properly trained, the improvement is truly impressive (see $\sigma _ { \mathrm { p o s t } }$ ) as it rivals the predictions of some of the most sophisticated models available to date. Even though the improvement is indeed impressive, ELD fails to capture the basic essence of our philosophy, namely, a raw model that includes as much physics as possible which is then fine tuned through BNN refinement. In this sense, the microscopic models conform better to this paradigm. Whereas all the models show consistent improvements after BNN refinement, the microscopic models see the smallest change. This suggests that the parameters of these models properly encode essential features of the nuclear dynamics. It is important to note, however, that in calibrating these density functionals, only a handful of charge radii were included in the fit [16, 17, 54].

Learning Set   

<table><tr><td>Model</td><td>ELD</td><td>Zhang</td><td>NL3</td><td>FSUGold</td><td>FSUGarnet</td></tr><tr><td>σpre(fm)</td><td>0.0628</td><td>0.0384</td><td>0.0304</td><td>0.0336</td><td>0.0373</td></tr><tr><td>σpost(fm)</td><td>0.0210</td><td>0.0207</td><td>0.0223</td><td>0.0214</td><td>0.0215</td></tr><tr><td>Δσ/σpre</td><td>0.67</td><td>0.46</td><td>0.27</td><td>0.36</td><td>0.42</td></tr></table>

Validation Set   

<table><tr><td>Model</td><td>ELD</td><td>Zhang</td><td>NL3</td><td>FSUGold</td><td>FSUGarnet</td></tr><tr><td>σpre(fm)</td><td>0.0595</td><td>0.0461</td><td>0.0412</td><td>0.0432</td><td>0.0510</td></tr><tr><td>σpost(fm)</td><td>0.0262</td><td>0.0280</td><td>0.0280</td><td>0.0298</td><td>0.0327</td></tr><tr><td>Δσ/σpre</td><td>0.56</td><td>0.39</td><td>0.32</td><td>0.31</td><td>0.36</td></tr></table>

Entire Set   
TABLE II. Root-mean-square deviation as predicted by a representative set of models for the charge radii of 722 nuclei (the learning set), 98 nuclei (the validation set), and 820 nuclei (the entire set); see text for details.   

<table><tr><td>Model</td><td>ELD</td><td>Zhang</td><td>NL3</td><td>FSUGold</td><td>FSUGarnet</td></tr><tr><td>σpre (fm)</td><td>0.0639</td><td>0.0394</td><td>0.0319</td><td>0.0349</td><td>0.0392</td></tr><tr><td>σpost (fm)</td><td>0.0217</td><td>0.0217</td><td>0.0230</td><td>0.0225</td><td>0.0231</td></tr><tr><td>Δσ/σpre</td><td>0.66</td><td>0.45</td><td>0.28</td><td>0.36</td><td>0.41</td></tr></table>

Having addressed the impact of the BNN refinement across the full nuclear chart, we turn our focus to a few of the isotopic chains that have seen the largest experimental gain in transitioning from the 2004 [43] to the latest [44] compilation; these are the most abundant isotopes in the validation set. In particular, the isotopic chains in yttrium ( $Z = 3 9$ ), lead ( $Z = 8 2$ ), and bismuth ( $Z = 8 3$ ) have benefited greatly from the remarkable experimental progress in laser spectroscopy. Indeed, our knowledge of charge radii in these isotopes has expanded from 1 to 16, from 23 to 32, and from 1 to 12 nuclei, respectively. As an illustration, we display in Fig. 2 the difference between theory and experiment for the charge radii of lead that, with the exception of $^ { 2 1 3 }$ Pb, are presently known from $1 8 2$ Pb all the way to $^ { 2 1 4 }$ Pb [44]. Shown in the plot are bare predictions from two mic-mac models (ELD and Zhang) and two relativistic density functionals (NL3 and FSUGarnet). Not surprisingly, among these the ELD predictions show the largest deviations relative to experiment; the other three models are, at worst, within 0.05 fm of the experimental data along the whole isotopic chain. Also shown in Fig. 2 are predictions using the Garvey-Kelson relations [22]; see Table III. Note that the GKR predictions were made before the publication of the experimental results. We observe that when enough information on the nearest neighbors to the nucleus of interest is available, then the GKR predictions are extremely accurate. However, the local GKRs extrapolate very poorly. This behavior is clearly indicated in the figure as one aims to predict the charge radii of progressively more neutron-deficient isotopes. To our knowledge, the only way that such extrapolations can be implemented is through an iterative procedure that uses “first-order” GKR predictions to extrapolate to “second order”, and so on. For example, we found enough neighbors in the 2004

compilation to be able to predict the charge radius of $\scriptstyle 1 8 9$ Pb. However, at that time it was not possible to predict the charge radius of $^ \mathrm { 1 8 8 }$ Pb. Hence, in order to make a prediction for $^ \mathrm { 1 8 8 }$ Pb, we are forced to use the charge radius of $\scriptstyle 1 8 9$ Pb—which itself was computed using the GKRs; this is the meaning of the number enclosed in parenthesis in Fig. 2. Indeed, in order to provide a GKR prediction for $1 8 2$ Pb “eight” iterations were needed. Not surprisingly, the local Garvey-Kelson relations are highly inaccurate far away from their region of applicability. In contrast, the improvement of the modest ELD model after the BNN refinement is very significant. These results indicate that, although extrapolations are always risky, global methods such as BNN are far superior in extrapolating than local methods, such as the GKRs that are inherently prone to error propagation.

![](images/0275d4354b313e542157001efcb755e6600ff5e73fabb8fd25a77eae74f3ca17.jpg)  
FIG. 2. Bare predictions for the charge radii of the lead isotopes (Z=82) relative to experiment [44] for some of the models considered in the text. Also shown are predictions from the Garvey-Kelson relations using an iterative method to extrapolate farther into the neutron-deficient region. Finally, denoted with error bars are the BNN-improved predictions of the extended liquid drop model.

TABLE III. Comparison between the bare predictions of a few models and the corresponding estimates using the Garvey-Kelson relations for some nuclei that were recently measured [44]. The GKR predictions compare extremely well against experiment but extrapolate very poorly; see Fig. 2.   

<table><tr><td>Z</td><td>N</td><td>A</td><td>Zhang</td><td>NL3</td><td>FSUGarnet</td><td>GKR</td><td>Experiment</td></tr><tr><td rowspan="3">Y</td><td>48</td><td>87</td><td>4.2811</td><td>4.2546</td><td>4.2305</td><td>4.2508</td><td>4.2498(22)</td></tr><tr><td>49</td><td>88</td><td>4.2885</td><td>4.2565</td><td>4.2325</td><td>4.2450</td><td>4.2441(21)</td></tr><tr><td>51</td><td>90</td><td>4.3034</td><td>4.2659</td><td>4.2442</td><td>4.2611</td><td>4.2573(26)</td></tr><tr><td rowspan="2">Pb</td><td>107</td><td>189</td><td>5.4587</td><td>5.4322</td><td>5.4080</td><td>5.4122</td><td>5.4177(24)</td></tr><tr><td>113</td><td>195</td><td>5.4871</td><td>5.4602</td><td>5.4338</td><td>5.4367</td><td>5.4389(45)</td></tr><tr><td rowspan="2">Bi</td><td>124</td><td>207</td><td>5.5540</td><td>5.5377</td><td>5.5176</td><td>5.5098</td><td>5.5103(32)</td></tr><tr><td>125</td><td>208</td><td>5.5587</td><td>5.5424</td><td>5.5232</td><td>5.5144</td><td>5.5147(28)</td></tr></table>

Having illustrated some of the central features of the BNN approach using Angeli’s 2004 compilation as the learning set and the nearly hundred new measurements as the validation set, we now turn to the slightly different strategy adopted in our earlier work that captures the robustness of the method. Using the entire data set from the latest compilation of 820 nuclei above $^ { 4 0 } \mathrm { C } \mathrm { { \bar { a } } }$ [44], we randomly select 80% of the nuclei as the learning set and then validate the resulting neural network model against the remaining $2 0 \%$ . Unlike the previous results that highlight the extrapolation properties of the BNN refinement, Table IV illustrates how well it interpolates. Qualitatively, no major trend differences are observed between the results shown in Tables II and IV. However, the quantitative improvement after the refinement is better in the present case, as extrapolating is always riskier than interpolating.

Ultimately, our main goal is to build a model that can predict charge radii which have never been measured. To do so, we use as the learning set the entire experimental data set containing 820 charge radii above $^ { 4 0 }$ Ca [44]. All the

Learning Set   

<table><tr><td>Model</td><td>ELD</td><td>Zhang</td><td>NL3</td><td>FSUGold</td><td>FSUGarnet</td></tr><tr><td>σpre(fm)</td><td>0.0645</td><td>0.0396</td><td>0.0319</td><td>0.0352</td><td>0.0393</td></tr><tr><td>σpost(fm)</td><td>0.0180</td><td>0.0171</td><td>0.0187</td><td>0.0179</td><td>0.0190</td></tr><tr><td>Δσ/σpre</td><td>0.72</td><td>0.57</td><td>0.41</td><td>0.49</td><td>0.52</td></tr></table>

Validation Set   

<table><tr><td>Model</td><td>ELD</td><td>Zhang</td><td>NL3</td><td>FSUGold</td><td>FSUGarnet</td></tr><tr><td>σpre(fm)</td><td>0.0618</td><td>0.0385</td><td>0.0318</td><td>0.0339</td><td>0.0388</td></tr><tr><td>σpost(fm)</td><td>0.0173</td><td>0.0163</td><td>0.0184</td><td>0.0179</td><td>0.0173</td></tr><tr><td>Δσ/σpre</td><td>0.72</td><td>0.58</td><td>0.42</td><td>0.47</td><td>0.55</td></tr></table>

Entire Set   
TABLE IV. Root-mean-square deviation as predicted by a representative set of models for the charge radii of 656 nuclei (the learning set), 164 nuclei (the validation set), and 820 nuclei (the entire set); see text for details.   

<table><tr><td>Model</td><td>ELD</td><td>Zhang</td><td>NL3</td><td>FSUGold</td><td>FSUGarnet</td></tr><tr><td>σpre (fm)</td><td>0.0639</td><td>0.0394</td><td>0.0319</td><td>0.0349</td><td>0.0392</td></tr><tr><td>σpost (fm)</td><td>0.0179</td><td>0.0169</td><td>0.0186</td><td>0.0179</td><td>0.0187</td></tr><tr><td>Δσ/σpre</td><td>0.72</td><td>0.57</td><td>0.42</td><td>0.49</td><td>0.52</td></tr></table>

![](images/332d7d36d0beac1891539280afcb9450e193c817b1de1421b396c6a123a60584.jpg)

![](images/e2ada11299fc19efaf873d6226fc019ed7dfc4dadcdfb3be7c4842f64fa48ee3.jpg)

![](images/e6588cc0827f8cfb0e46d2c59b61bf254745b57ca2d997be6dace0fd438ee0a6.jpg)

![](images/772b9603841ac827322426acc29aca2bcbcf1ca2d92a80d0da16b9022c0f4d29.jpg)  
FIG. 3. Predictions for the charge radii of a few neutron-rich tin isotopes from the bare models (without errors bars) and after BNN refinement (with error bars). The “World” predictions represent a simple way of combining the results of all models as per Eq. (14). The experimental data are from [44], except for $^ \mathrm { 1 3 6 }$ Sn where the bare prediction from the ELD model is adopted as reference.

results presented hereafter will use a neural network function constructed from all 820 nuclei. We have found that the results obtained in this manner are both consistent and indeed very similar to those reported in Table IV. In particular, we conclude that the excellent agreement with experiment (within 0.02 fm) rivals—and likely exceeds—the best models currently available in the literature. Finally, by treating the various predictions as statistically independent, we can properly combine them into a “world average”. That is,

$$
R _ {\text {w o r l d}} = \sum_ {n} \omega_ {n} R _ {n}, \quad V _ {\text {w o r l d}} = \sum_ {n} \omega_ {n} ^ {2} V _ {n}, \text {a n d} \omega_ {n} = \frac {V _ {n} ^ {- 1}}{\sum_ {k} V _ {k} ^ {- 1}}, \tag {14}
$$

where the sum runs over all five models and $V _ { n }$ represents the variance of each model. For example, world-average predictions for a few neutron-rich tin isotopes are displayed in Fig. 3, alongside the corresponding predictions from each individual model. With the exception of $^ \mathrm { 1 3 6 }$ Sn, all models are compared against existing experimental data. In

the particular case of $^ \mathrm { 1 3 6 }$ Sn where data is not yet available, we use the bare ELD prediction of $R _ { \mathrm { c h } } ^ { \mathrm { E L D } } = 4 . 8 4 6 \mathrm { f m }$ as a baseline. For reference, FSUGarnet predicts after BNN refinement a charge radius of about 0.1 fm smaller than the ELD reference, or $R _ { \mathrm { c h } } { = } ( 4 . 7 3 7 \pm 0 . 0 0 9 ) \mathrm { f m }$ . We observe that in all three cases where experimental measurements are available, the BNN refinement leads to significantly reduced scattering, an improvement in the theoretical predictions, especially in the case of the mic-mac models and ultimately, to world-average predictions that are both accurate and precise. This lends credence to our approach and validates our prediction of the charge radius of $^ \mathrm { 1 3 6 }$ Sn.

![](images/a47b9c95af1d37ef8a94babe8bc78d4a117987c1ee8656be8340ed243bea9f32.jpg)  
FIG. 4. Predictions for the charge radii of the tin isotopes using the mic-mac model of Zhang et al. [10, 11] and FSUGarnet [17]. Predictions are displayed without errors bars for the bare models and with error bars after the BNN refinement. Experimental data—available from $^ \mathrm { 1 0 8 }$ Sn all the way to $^ { 1 3 2 }$ Sn—are from Ref. [44].

Having illustrated the systematic improvement in our prediction for a few isotopes, we now display in Fig. 4 predictions along the whole isotopic chain in tin using the mic-mac model of Zhang et al. [10] (with the parameters from [11]) and FSUGarnet [17] as a representative set of our predictions. It is worth highlighting the remarkable experimental progress that has been made in the last few years in extending the measurement of charge radii far away from stability. In the particular case of tin, high precision data is now available from $^ \mathrm { 1 0 8 }$ Sn all the way to $^ \mathrm { 1 3 2 }$ Sn. In many ways, Fig. 4 captures the true essence of our theoretical approach: an accurately-calibrated density functional which by incorporating as much physics as possible provides an excellent description of the experimental data that is then improved even further after the BNN refinement. And whereas our aim is for BNN to provide a fine tuning, the figure illustrates that even when there is significant disagreement between the theoretical predictions and experiment, as in the case of the mic-mac model, the approach is powerful enough to overcome most of these deficiencies. Utilizing this combined DFT+BNN approach (labeled “Entire Set” in Table IV) we provide as a supplement to this paper predictions for the charge radii of all nuclei beyond $^ { 4 0 }$ Ca whose mass is experimentally known [64]. This large collection of nuclei is also displayed as a heat map in Fig. 5 using both “pre” and “post” FSUGarnet predictions. Note that color coded in green are predictions for those nuclei whose charge radius is presently unknown. Yet, given the remarkable experimental progress in the determination of charge radii of nuclei far away from stability, we trust that these predictions will be tested against experiment in the coming years.

Finally, we now return to one of the main motivations behind this work: understanding the underlying physics behind the intriguing trend displayed by the charge radii of the calcium isotopes [19]; see Fig. 6. The evolution of the charge radii in the calcium isotopes is puzzling for several reasons. First, within the region of the stable isotopes, a long-standing question remains unanswered: why are the charge radii of $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca practically identical; i.e., $R _ { \mathrm { c h } } ^ { 4 0 } { = } 3 . 4 7 7 6 ( 1 9 ) \mathrm { f m }$ and $R _ { \mathrm { c h } } ^ { 4 8 } { = } 3 . 4 7 7 1 ( 2 0 ) \mathrm { f m }$ . Second, although it is well known that pairing correlations are behind the pervasive odd-even effects observed in a variety of observables throughout the nuclear chart, why are these effects so pronounced as the system evolves from $N = 2 0$ to $N = 2 8$ . Finally, as reported in Ref. [19], there is a large and unexpected increase in the size of the neutron-rich calcium isotopes beyond $N = 2 8$ . Unexpected in the sense that theoretical results obtained with either ab initio approaches, configuration interaction, or density functional theory are unable to reproduce the complex experimental trend. We note that some studies using energy density functionals

![](images/290ef9a383bf4ec697d7c84586734b9fa52ace7a87b4bd71a8d0525271a5137e.jpg)

![](images/88abad2699984b2e4c1a06b8c29aa9dac534773e3a7181b025429f2c6a0ef702.jpg)  
FIG. 5. FSUGarnet predictions, before and after BNN refinement, for the charge radii of all nuclei whose mass is experimentally known [64]. Color coded in green are predictions for those nuclei whose charge radius is presently unknown. Tabulated values for all these nuclei appear in the supplemental material to this paper.

that include a sophisticated treatment of pairing correlations [12, 66] or shell model calculations using a relatively large model space [65] appear to successfully reproduce the charge radii along the isotopic chain in calcium. Yet, by the authors’ own admission [12], the anomalous behavior of charge radii in Ca isotopes was reproduced in excellent agreement with experiment ... by scaling the pairing effective interaction which was extracted from the lead chain by a factor of 1.35, thereby concluding that a universal parametrization of the pairing force is still lacking [12]. Similarly, it is concluded in Ref. [65] that whereas the experimental trends are well reproduced by shell model calculations, the magnitude of the calculated shifts is smaller than the experiment suggests.

![](images/d3786a88a9f6531e318e9ef74b3a6c6fe8205bb70380cf365f5b1f8fd47ec6c0.jpg)  
FIG. 6. Predictions for the charge radii of the calcium isotopes using the mic-mac model of Zhang et al. [10, 11] and FSUGarnet [17]. Predictions are displayed without errors bars for the bare models and with error bars after the BNN refinement. Experimental data are from Refs. [19, 44].

Unfortunately, our own DFT+BNN approach does not fare any better. In an effort to eliminate, or at least mitigate, the discrepancy with experiment, we have modified our fitting strategy in the following manner. First, we have limited the training set to the region between oxygen ( $Z = 8$ ) and neodymium ( $Z = 6 0$ ). Second, we have biased our results in

favor of the calcium isotopes by readjusting the weights in the likelihood function; all the weights are enhanced by a factor of two, except in the case of the two doubly magic nuclei $^ { 4 0 }$ Ca and $^ { 4 8 }$ Ca where they are enhanced by a factor of three. Thus, the training of the neural network involves incorporating the entirety of the 472 nuclei in this region [44]. Finally, keeping all other inputs unchanged, we re-train the neural network function using only the models of Zhang and FSUGarnet.

In Fig. 6 we show the bare results of the Zhang et al. model (red triangles with no error bars) that predict a nearly linear dependence with $A$ (or $N$ ) which in no way resembles the trend displayed by the data. In turn, predictions with FSUGarnet (blue squares with no error bars) show a behavior that is characteristic of most energy density functionals: a relatively slow increase in the $A = 4 0 – 4 8$ region preceding a sharp rise beyond $^ { 4 8 }$ Ca, although not as sharp as demanded by the data. BNN results for both models, now shown with uncertainty bars, improve significantly after the refinement, particularly in the case of FSUGarnet that now accounts, albeit with large error bars, for the steep rise in the data beyond $^ { 4 8 }$ Ca. However, although both models develop some structure in the $A = 4 0 – 4 8$ region after BNN refinement, neither of them can reproduce the dramatic odd-even effects displayed by the data. We must conclude then that at present, the intriguing trend displayed by the charge radii of the calcium isotopes remains “a riddle, wrapped in a mystery, inside an enigma”.

# IV. CONCLUSIONS

The mass and size of atomic nuclei feature among their most distinctive and fundamental characteristics. Within a few years after the discovery of the neutron by Chadwick, Bethe and Weizs¨acker conceived the liquid drop model, which up to this day continues to provide a qualitative description of both the mass and radius of nuclei. During the past eight decades, sophisticated theoretical approaches have been developed to improve this very early description. Ultimately, the goal of nuclear theory is to develop a predictive understanding of the structure and dynamics of nuclei based on QCD, the fundamental theory of the strong interaction. While significant progress has been made in understanding QCD in the low-energy regime, at present most of our understanding of nuclear phenomena derives from effective field theories of nucleons/mesons that incorporate the underlying symmetries of QCD. Thus, whereas the predictive capability of nuclear theory has increased dramatically, it has not yet reach the level of precision that is required to guide applications into other areas, primarily fundamental symmetries and astrophysics. In response to this situation, we have recently proposed a hybrid approach that combines sophisticated theoretical models with Bayesian neural networks. The basic tenet of this approach is to start with a model that incorporates as much physics as possible which then gets refined by building a Bayesian neural network model. This approach was recently implemented with considerable success in the case of nuclear masses of relevance to the crustal composition of neutron stars [18]. Motivated by some recent results along the isotopic chain in calcium [19], we have extended the approach to the description of nuclear charge radii.

As illustrated previously for nuclear masses [18], the hybrid approach starts by invoking both mic-mac and microscopic models. Among the mic-mac models we have used two simple extensions of the liquid-drop model, and in the case of the microscopic models we relied on accurately-calibrated relativistic parametrizations. In all cases, the theoretical models provide baseline estimates that often compare favorably against the extensive database of experimental charge radii [44]. However, those models, although accurate, can all benefit from further refinement. This additional refinement is implemented through training a Bayesian neural network on the residuals between the theoretical predictions and experiment. The BNN formalism is an approximation scheme that relies on the application of Bayes’ theorem and a highly nonlinear neural network function aiming at refining our predictions. Besides improved predictions, BNN has the enormous advantage of providing an estimate of the theoretical uncertainties. Given that neural network learning involves information on charge radii all throughout the nuclear chart, we found it pertinent to compare this global approach against predictions from the Garvey-Kelson relations, a highly successful local method.

Several optimization protocols were adopted to test the reliability of our proposed approach, from one that uses the 2004 compilation by Angeli [43] as the learning set and the new nuclei appearing in the latest compilation as the validation set [44], to one in which the full 2013 dataset is used to calibrate the neural network function. In all cases we saw considerable improvement after the BNN refinement, ultimately achieving rms deviations below 0.02 fm for a collection of 820 nuclei. Although it is impractical to illustrate the performance of our approach for many isotopic chains, several important findings were obtained. First, we showed that whereas local methods such as the Garvey-Kelson relations work extremely well when enough neighbors are available, they extrapolate—in contrast to the global BNN approach—extremely poorly. Second, we regarded our results for the tin isotopes as a “textbook example” of the combined DFT+BNN method. Indeed, although we found very good initial agreement using the bare predictions of FSUGarnet, these predictions became even better after the BNN refinement and were properly supplemented with error bars. Finally, like many before us, we failed to reproduce in detail the complex behavior of the calcium isotopes. While a convincing explanation for the pronounced odd-even effects in the $A = 4 0 – 4 8$ region has

been proven elusive, recent experiments at ISOLDE have complicated matters even further by reporting a very sharp increase in the charge radii of the neutron-rich calcium isotopes that is inconsistent with theoretical predictions [19]. Yet, by a “proper” adjustment of the neural network function, we were able to eliminate some of these discrepancies. Indeed, the steep rise can be accounted for within the large theoretical uncertainties. However, the physics behind the odd-even staggering and the very steep rise remains a mystery.

In summary, BNN training has been shown to be a promising new tool to refine the predictions of existing nuclear models. In this paper we have extended our earlier work on nuclear masses to nuclear charge radii. In cases in which the underlying physics model is sound, then BNN refinement works extremely well. In contrast, if there is important physics missing from the underlying model, it is unlikely that BNN by itself can fix such deficiencies. That is, although the BNN framework is very robust for model refinement, an essential requirement for its success is that the quantity to be fitted, such as model residuals, be a relatively smooth function of the input parameters. In other words, we are confident that if the physics model is able to reproduce the main trends in the data, then BNN can provide the fine-tuning necessary to reach the precision demanded by astrophysics (and other) applications.

# ACKNOWLEDGMENTS

We are very grateful to Dr. Harrison Prosper and Dr. Michelle Kuchera for many fruitful discussions. This material is based upon work supported by the U.S. Department of Energy Office of Science, Office of Nuclear Physics under Award Number DE-FD05-92ER40750.

[1] C. F. von Weizs¨acker, Z. Physik 96, 431 (1935).   
[2] H. A. Bethe and R. F. Bacher, Rev. Mod. Phys. 8, 82 (1936).   
[3] P. M¨oller and J. R. Nix, Atom. Data Nucl. Data Tabl. 26, 165 (1981).   
[4] P. M¨oller and J. R. Nix, Atom. Data Nucl. Data Tabl. 39, 213 (1988).   
[5] P. M¨oller, J. R. Nix, W. D. Myers, and W. J. Swiatecki, Atom. Data Nucl. Data Tabl. 59, 185 (1995).   
[6] J. Duflo and A. Zuker, Phys. Rev. C 52, R23 (1995).   
[7] B. A. Brown, C. R. Bronk, and P. E. Hodgson, J. Phys. G: Nucl. Phys. 10, 1683 (1984).   
[8] W. Myers and K.-H. Schmidt, Nucl. Phys. A410, 61 (1983).   
[9] R. H. Helm, Phys. Rev. 104, 1466 (1956).   
[10] S. Q. Zhang, J. Meng, S. G. Zhou, and J. Y. Zheng, Eur. Phys. J. A13, 285 (2002).   
[11] T. Bayram, S. Akkoyun, and S. O. Kara, Acta Physica Polonica B 44, 1791 (2013).   
[12] S. Fayans, S. Tolokonnikov, E. Trykov, and D. Zawischa, Nuclear Physics A676, 49 (2000).   
[13] S. Goriely, N. Chamel, and J. Pearson, Phys. Rev. C82, 035804 (2010).   
[14] M. Kortelainen, T. Lesinski, J. More, W. Nazarewicz, J. Sarich, et al., Phys.Rev. C82, 024313.   
[15] J. Erler, C. J. Horowitz, W. Nazarewicz, M. Rafalski, and P.-G. Reinhard, Phys. Rev. C87, 044320 (2013).   
[16] W.-C. Chen and J. Piekarewicz, Phys. Rev. C90, 044305 (2014).   
[17] W.-C. Chen and J. Piekarewicz, Phys. Lett. B748, 284 (2015).   
[18] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C93, 014311 (2016).   
[19] R. F. Garcia Ruiz et al., Nature Phys. 12, 594 (2016).   
[20] M. Brack and R. K. Bhaduri, “Semiclassical physics,” (Addison-Wesley, Reading, MA, 1997).   
[21] V. M. Strutinsky, Nuclear Physics A 95, 420 (1967).   
[22] J. Piekarewicz, M. Centelles, X. Roca-Maza, and X. Vi˜nas, Eur. Phys. J. A46, 379 (2010).   
[23] G. T. Garvey and I. Kelson, Phys. Rev. Lett. 16, 197 (1966).   
[24] G. T. Garvey, W. J. Gerace, R. L. Jaffe, I. Talmi, and I. Kelson, Rev. Mod. Phys. 41, S1 (1969).   
[25] M. A. Preston and R. K. Bhaduri, “Structure of the nucleus,” (Westview Press, Boulder, Colorado, 1993).   
[26] B. H. Sun, Y. Lu, J. P. Peng, C. Y. Liu, and Y. M. Zhao, Phys. Rev. C 90, 054318 (2014).   
[27] J. D. Holt, T. Otsuka, A. Schwenk, and T. Suzuki, J. Phys. G39, 085111 (2012).   
[28] G. Hagen, M. Hjorth-Jensen, G. R. Jansen, R. Machleidt, and T. Papenbrock, Phys. Rev. Lett. 109, 032502 (2012).   
[29] R. Neal, Bayesian Learning of Neural Network (Springer, New York, 1996).   
[30] C. Bishop, Neural Networks for Pattern Recognition (Oxford University Press, Birmingham, UK).   
[31] S. Haykin, Neural Networks: A Comprehensive Foundation (Prentice Hall, Upper Saddle River, NJ).   
[32] V. Vapnik, Statistical Learning Theory (Wiley-Interscience, New York, NY).   
[33] S. Gazula, J. Clark, and H. Bohr, Nucl. Phys. A 540, 1 (1992).   
[34] K. Gernoth, J. Clark, J. Prater, and H. Bohr, Phys. Lett. B 300, 1 (1993).   
[35] K. Gernoth and J. Clark, Neural Networks 8, 291 (1995).   
[36] J. W. Clark, T. Lindenau, and M. Ristig, “Scientific applications of neural nets springer lecture notes in physics,” (Springer-Verlag, Berlin, 1999) pp. 1–96.

[37] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Nucl. Phys. A743, 222 (2004).   
[38] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Nuclear mass systematics by complementing the finite range droplet model with neural networks, edited by G. Lalazissis and C. Moustakidis (Advances in Nuclear Physics, Proceedings of the 15th Hellenic Symposium on Nuclear Physics, 2006) pp. 65–70.   
[39] J. W. Clark and H. Li, Int. J. Mod. Phys. B20, 5015 (2006).   
[40] N. J. Costiris, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Phys. Rev. C 80, 044332 (2009).   
[41] T. Bayram, S. Akkoyun, and S. O. Kara, Annals of Nuclear Energy 63, 172 (2014).   
[42] S. Akkoyun, T. Bayram, S. O. Kara, and A. Sinan, J. Phys. G40, 055106 (2013).   
[43] I. Angeli, At. Data Nucl. Data Tables 87, 185 (2004).   
[44] I. Angeli and K. Marinova, At. Data Nucl. Data Tables 99, 69 (2013).   
[45] J. D. Walecka, Annals Phys. 83, 491 (1974).   
[46] J. Boguta and A. R. Bodmer, Nucl. Phys. A292, 413 (1977).   
[47] C. J. Horowitz and B. D. Serot, Nucl. Phys. A368, 503 (1981).   
[48] B. D. Serot and J. D. Walecka, Adv. Nucl. Phys. 16, 1 (1986).   
[49] H. Mueller and B. D. Serot, Nucl. Phys. A606, 508 (1996).   
[50] B. D. Serot and J. D. Walecka, Int. J. Mod. Phys. E6, 515 (1997).   
[51] G. A. Lalazissis, J. Konig, and P. Ring, Phys. Rev. C55, 540 (1997).   
[52] G. A. Lalazissis, S. Raman, and P. Ring, At. Data Nucl. Data Tables 71, 1 (1999).   
[53] C. J. Horowitz and J. Piekarewicz, Phys. Rev. Lett. 86, 5647 (2001).   
[54] B. G. Todd-Rutel and J. Piekarewicz, Phys. Rev. Lett 95, 122501 (2005).   
[55] M. R. Mumpower, R. Surman, G. C. McLaughlin, and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016).   
[56] S. Aberg, Nature 417, 499 (2002).   
[57] J. Barea, A. Frank, J. G. Hirsch, and P. Van Isacker, Phys. Rev. Lett. 94, 102501 (2005).   
[58] K. Hornik, M. Stinchcombe, and H. White, Neural Networks 2, 359 (1989).   
[59] D. M. Titterington, Statist. Sci. 19, 128 (2004).   
[60] J. V. Stone, “Bayes’ rule: A tutorial introduction to bayesian analysis,” (Sebtel Press, Sheffield, UK, 2013) 1st ed.   
[61] D. J. MacKay, Nuclear Instruments and Methods in Physics Research Section A 354, 73 (1995).   
[62] D. J. MacKay, Neural Computation 11, 1035 (1999).   
[63] W. A. Richter and B. A. Brown, Phys. Rev. C67, 034317 (2003).   
[64] M. Wang, G. Audi, A. Wapstra, F. Kondev, M. MacCormick, X. Xu, and B. Pfeiffer, Chinese Phys. C 36, 1603 (2012).   
[65] E. Caurier, K. Langanke, G. Martinez-Pinedo, F. Nowacki, and P. Vogel, Phys. Lett. B522, 240 (2001).   
[66] E. E. Saperstein and S. V. Tolokonnikov, Physics of Atomic Nuclei 74, 1277 (2011).