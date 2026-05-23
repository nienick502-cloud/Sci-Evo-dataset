# Refining mass formulas for astrophysical applications: a Bayesian neural network approach

R. Utama1, ∗ and J. Piekarewicz1, †

$^ { 1 }$ Department of Physics, Florida State University, Tallahassee, FL 32306

(Dated: March 12, 2018)

Background: Exotic nuclei, particularly those near the driplines, are at the core of one of the fundamental questions driving nuclear structure and astrophysics today: what are the limits of nuclear binding? Exotic nuclei play a critical role in both informing theoretical models as well as in our understanding of the origin of the heavy elements.

Purpose: To refine existing mass models through the training of an artificial neural network that will mitigate the large model discrepancies far away from stability.

Methods: The basic paradigm of our two-pronged approach is an existing mass model that captures as much as possible of the underlying physics followed by the implementation of a Bayesian Neural Network (BNN) refinement to account for the missing physics. Bayesian inference is employed to determine the parameters of the neural network so that model predictions may be accompanied by theoretical uncertainties.

Results: Despite the undeniable quality of the mass models adopted in this work, we observe a significant improvement (of about 40%) after the BNN refinement is implemented. Indeed, in the specific case of the Duflo-Zuker mass formula, we find that the rms deviation relative to experiment is reduced from $\sigma _ { \mathrm { r m s } } { = } 0 . 5 0 3 \mathrm { M e V }$ t o $\sigma _ { \mathrm { r m s } } = 0 . 2 8 6$ MeV. These newly refined mass tables are used to map the neutron drip lines (or rather “dripbands”) and to study a few critical $r$ -process nuclei.

Conclusions: The BNN approach is highly successful in refining the predictions of existing mass models. In particular, the large discrepancy displayed by the original “bare” models in regions where experimental data is unavailable is considerably quenched after the BNN refinement. This lends credence to our approach and has motivated us to publish refined mass tables that we trust will be helpful for future astrophysical applications.

PACS numbers: 21.10.Dr, 26.50.+x, 26.60.Gj

# I. INTRODUCTION

Where do the chemical elements come from and how did they evolve is one of the central questions animating nuclear science today [1]. Stars heavier than about eight solar masses $( M _ { \star } \gtrsim 8 M _ { \odot } )$ reach high enough core temperatures to support the formation of ever-heavier chemical elements by thermonuclear fusion: from helium all the way to iron. Yet, once the iron-peak elements are synthesized, thermonuclear burning stops abruptly with the formation of an inert iron core that will collapse once its mass exceeds the Chandrasekhar limit [2–4]. This situation naturally begs the question: how did the elements heavier than iron form? Whereas the slow neutron capture process (“s-process”) in asymptotic giant branch stars is believed to be responsible for the formation of about half of the heavy elements beyond iron (such as strontium, barium, and lead) identifying the precise site (or sites) of the rapid neutron capture process (“ $r$ -process”) responsible for the remaining half of of the heavy elements (such as gold, platinum, and uranium) remains elusive [2, 5, 6]. Indeed, “How were the elements from iron to uranium made?” has been identified as one of the eleven science questions for the new century [7].

Understanding $r$ -process nucleosynthesis is a fascinating and challenging multidisciplinary problem. Progress in this area demands detailed knowledge of a host of nuclear-structure observables—often at the limits of nuclear existence— such as masses, neutron capture rates, and nuclear beta decays [5, 8, 9]. Given that the $r$ -process develops under extreme astrophysical conditions such as those found in the merger of two neutron stars, neutron capture on seed nuclei occurs on a time scale that is much faster than the competing beta-decay rates. This drives the $r$ -process far away from stability where little is known about the thousands of exotic nuclear species that participate in these reactions; see Refs. [6, 8, 9] and references contained therein. In an effort to mitigate this problem, Mumpower and collaborators have performed sensitivity studies to identify the nuclear inputs (e.g., nuclear masses) that have the greatest impact on the $r$ -process [9–11]. Whereas these studies suggest that some of the “most influential” nuclear masses are within reach of future radioactive beam facilities, it is also recognized that some others will likely remain beyond experimental reach. Hence, theoretical guidance becomes absolutely critical. Unfortunately, theoretical mass models that agree in the vicinity of measured nuclear masses, disagree strongly—often by several MeV—far away from stability. This is particularly troublesome given that some sensitivity studies suggest that resolving the abundance pattern will require reducing mass-model uncertainties to $\lesssim 1 0 0 \mathrm { k e V }$ [11].

The emergence of the $r$ -process pattern is highly sensitive to nuclear masses in the vicinity of neutron magic numbers $N = 5 0 , 8 2$ , and 126. Interestingly, nuclear masses around closed shells $N = 5 0$ and 82 also have a profound impact on the composition of a different astrophysical system: the outer crust of a neutron star. Given that at the low densities of relevance to the outer crust $( 1 0 ^ { 4 } - 1 0 ^ { 1 1 } \mathrm { g / c m ^ { 3 } } )$ the average inter-nucleon separation is considerably larger than the range of the nuclear interaction, it becomes energetically favorable for nucleons to cluster into individual nuclei that arrange themselves in a crystalline lattice that is immersed in a uniform free Fermi gas of electrons [12]. And whereas the underlying dynamics is relatively simple, the exotic composition of the outer stellar crust is also highly sensitive to nuclear masses in regions where experimental information is not yet available [13]. Thus, as in the case of the $r$ -process, understanding the composition of the stellar crust relies heavily on theoretical extrapolations into unknown regions of the nuclear chart.

In an effort to lessen the impact of such inevitable extrapolations we have recently intoduced a Bayesian Neural Network (BNN) approach for the calculation of nuclear masses [14, 15] and charge radii [16]. The novel framework proposed in Ref. [14] consists of a combined scheme that relies on accurate theoretical predictions that are subsequently refined by training a suitable artificial neural network on the residuals between the experimental data and the theoretical predictions. In essence, the central tenet of our approach is to include as much physics as possible in the underlying nuclear model and then rely on a BNN refinement to recover most of the physics that is missing from the model. In our earlier work we were able to identify several virtues of such combined approach. First, by using a randomly selected set of experimentally known masses to train the neural network, we observed a significant improvement in the predictions of the remaining known masses that were not included in the training set—even for some of the most sophisticated mass models available in the literature. Second, it is well known that theoretical mass models of similar quality agree in regions where masses are known, but differ widely (by as much as tens of MeVs) in regions where experimental data is not yet available [17]. However, after implementing the BNN refinement we found that the large differences in the model predictions were significantly reduced. Finally, given the “Bayesian” character of the approach, the refined predictions were accompanied by properly estimated theoretical errors [14].

In our earlier work we have successfully tested the BNN paradigm in the context of nuclear masses of relevance to the outer crust of neutron stars [14, 15]. It is the main goal of the present paper to provide updated mass tables that encompass the entire nuclear chart. As several sophisticated and successful mass tables already exist [18–24], the initial phase of our program—namely, the selection of an underlying model that incorporates as much physics as possible—is essentially complete. Thus, the remaining task is to implement the BNN refinement on these highly successful models. Our hope is that the BNN refinement will improve the original mass models by reducing the large systematic uncertainties and by providing realistic statistical errors. Together with the publication of these

updated mass tables, we will also make available (with associated theoretical uncertainties) related observables that may be more suitable for certain astrophysical applications, such as one- and two-nucleon separation energies. It is our hope that these tables will contribute to further our understanding of astrophysical phenomena as well as to constrain theoretical models of nuclear structure. Ultimately, of course, any progress in theory is strongly coupled to experimental advances. Indeed, we are at the dawn of a new era where rare isotope facilities will probe the limits of nuclear existence and in so doing will provide critical guidance to theoretical models. And although some of the required theoretical extrapolations will take us far into regions of the nuclear chart that are unlikely to be explored even at the most sophisticated facilities, measurements of even a few exotic short-lived isotopes are of critical importance for the improvement of theoretical models.

The manuscript has been organized as follows. In the next section we provide some additional details on the strong synergy between nuclear structure and astrophysics. As the BNN approach has been presented elsewhere [14], we limit the discussion on the formalism to a brief outline of the method and its implementation in Sec. III. Next, in Sec. IV we focus on the improvement to several existing mass models after the BNN refinement. Only in the case of the 10-parameter version of the Duflo-Zuker mass model [21] we recalibrate the parameters in order to extract the associated covariance matrix that encodes statistical uncertainties and correlations among the model parameters. In this way the overall theoretical error will have its origin in two sources: (a) the uncertainty in calibration of the “bare” model parameters and (b) the errors emerging from the BNN refinement. Also presented in this section are results for proton and neutron drip lines as well as a few masses of particular relevance to the $r$ -process. Finally, we conclude in Sec. V with a summary of our important findings.

# II. ASTROPHYSICAL MOTIVATION

Although of fundamental and high intrinsic nuclear-physics value, modern nuclear mass tables find today their best expression in astrophysical applications. In particular, nuclear masses are of paramount importance in understanding nucleosynthesis in hot stellar environments and the crustal composition of cold neutron stars. In what follows we provide a brief description of these two scenarios underscoring the critical role of nuclear masses far away from equilibrium.

# A. Neutron capture and photo-dissociation: $( \gamma , n )$ equilibrium

Although modern $r$ -process simulations make no assumptions on whether stellar conditions—such as temperature, density, and neutron fraction—are favorable to maintain the reaction $( n , \gamma )  ( \gamma , n )$ in thermodynamic equilibrium, the outcome of such network calculations suggests that under many astrophysical scenarios equilibrium is indeed attained, at least during the early stages. Under such an astrophysical scenario, the final abundance pattern follows solely from statistical equilibrium and nuclear physics. In particular, the pattern along a given isotopic chain is set by the temperature ( $T$ ), the neutron density ( $N _ { n }$ ), and the one-neutron separation energy ( $S _ { n }$ ). In essence, once thermodynamic equilibrium has been established in a given astrophysical environment, the final abundance pattern along an isotopic chain is entirely determined by nuclear masses, both near and far from the valley of stability. The ratio of yields of neighboring isotopes at equilibrium is set by the equality of the chemical potential of the competing species. Given that $\mu _ { \gamma } \equiv 0$ one obtains,

$$
\mu (Z, A) + \mu_ {n} = \mu (Z, A + 1). \tag {1}
$$

In the limit of low neutron density and high temperature, so that each component may be treated as a classical ideal gas, the condition of chemical equilibrium is encoded in the Saha equation [2–4]:

$$
\frac {Y (Z , A + 1)}{Y (Z , A)} = \frac {G (Z , A + 1)}{2 G (Z , A)} N _ {n} \lambda_ {n} ^ {3} (T) \exp \left(\frac {S _ {n} (Z , A + 1)}{k _ {B} T}\right). \tag {2}
$$

Here $Y ( Z , A )$ and $G ( Z , A )$ denote the isotopic abundance and partition function of the seed nucleus, and $\lambda _ { n } ( T ) =$ $\sqrt { 2 \pi / m _ { n } k _ { \mathrm { B } } T }$ is the de Broglie thermal wavelength of the neutron. Often $N _ { Q } = \lambda _ { n } ^ { - 3 } ( T )$ is referred to as the quantum concentration; if $N _ { n } \ll N _ { Q }$ then the system behaves classically. The nuclear dynamics is imprinted in the neutron separation energy

$$
S _ {n} (Z, A + 1) \equiv M (Z, A) + m _ {n} - M (Z, A + 1) = B (Z, A + 1) - B (Z, A), \tag {3}
$$

with $B ( Z , A )$ the total nuclear binding energy. Note that the relative abundance is exponentially sensitive to errors in the neutron separation energy. For example, at a canonical stellar temperature of $T _ { 9 } = 1 0 ^ { 9 } \mathrm { K }$ , a relatively “modest”

error in the separation energy of 0.1 MeV translates into an error in the relative abundance of about a factor of three. Eventually, chemical equilibrium is lost and the final abundance pattern is dictated by a series of $\beta$ decays back to stability. Here too nuclear masses are of critical importance since the phase-space factor for beta decay is determined by the reaction $Q$ -value: $Q _ { \beta } = M ( Z , A ) - M ( Z + 1 , A )$ .

# B. Crustal composition of a neutron star

Another powerful connection between astrophysics and nuclear physics that is highly sensitive to nuclear masses involves the crustal composition of a neutron star, particularly its outer crust [12, 13, 25–28]. The crust is interesting because the dynamics is simple yet subtle. Simple, because nuclear masses is the only ingredient driving the composition of the outer crust. Subtle, since the crustal composition emerges from a delicate dynamics between the electronic energy and the nuclear symmetry energy. Indeed, at the densities of relevance to the outer crust, it is energetically favorable for nucleons to cluster into nuclei that arrange themselves in a body-centered cubic lattice that itself is immersed in a neutralizing electron background [12]. At zero temperature and fixed pressure, the dynamics of the outer crust is encoded in the following expression for the chemical potential (or Gibbs free energy per nucleon) of the system:

$$
\mu (Z, A; P) = \frac {M (Z , A)}{A} + \frac {Z}{A} \mu_ {e} - \frac {4}{3} C _ {l} \frac {Z ^ {2}}{A ^ {4 / 3}} p _ {\mathrm {F}}. \tag {4}
$$

The first term—which is independent of the pressure—depends exclusively on the mass per nucleon of the “optimal” nucleus populating the crystal lattice. The second term $\mu _ { e }$ is the chemical potential of a relativistic Fermi gas of electrons. Finally, the last term provides the relatively modest, although by no means negligible, lattice contribution ( $C _ { l } { = } 3 . 4 0 6 6 5 { \times } 1 0 ^ { - 3 }$ ) to the chemical potential. Note that both the electronic

$$
\mu_ {e} = \sqrt {\left(\frac {Z}{A}\right) ^ {2 / 3} p _ {\mathrm {F}} ^ {2} + m _ {e} ^ {2}}, \tag {5}
$$

and lattice contributions have been written in terms of the Fermi momentum $p _ { \mathrm { F } } = ( 3 \pi ^ { 2 } n ) ^ { 1 / 3 }$ (or equivalently the baryon density $n$ ) rather than the pressure. The connection between the baryon density and the pressure is obtained through the equation of state. That is [13],

$$
P (Z, A; n) = \frac {m _ {e} ^ {4}}{3 \pi^ {2}} \left(x _ {\mathrm {F}} ^ {3} y _ {\mathrm {F}} - \frac {3}{8} \left[ x _ {\mathrm {F}} y _ {\mathrm {F}} \left(x _ {\mathrm {F}} ^ {2} + y _ {\mathrm {F}} ^ {2}\right) - \ln \left(x _ {\mathrm {F}} + y _ {\mathrm {F}}\right) \right]\right) - \frac {n}{3} C _ {l} \frac {Z ^ {2}}{A ^ {4 / 3}} p _ {\mathrm {F}}, \tag {6}
$$

where

$$
x _ {\mathrm {F}} = \frac {p _ {\mathrm {F}} ^ {(e)}}{m _ {e}} = \left(\frac {Z}{A}\right) ^ {1 / 3} \frac {p _ {\mathrm {F}}}{m _ {e}} \quad \text {a n d} \quad y _ {\mathrm {F}} = \sqrt {1 + x _ {\mathrm {F}} ^ {2}}, \tag {7}
$$

are the scaled electronic Fermi momentum and Fermi energy, respectively. Given that the outer crust spans nearly seven orders of magnitude in density, from about $\mathrm { 1 0 ^ { 4 } g / c m ^ { 3 } }$ to $1 0 ^ { 1 1 } \mathrm { g } / \mathrm { c m } ^ { 3 }$ , changes in the nuclear composition with density (or pressure) are interesting despite the simplicity of the underlying dynamics. For example, at the top of the outer crust where the pressure is low and so is the density, the electronic contribution to the chemical potential is negligible, so it is favorable to populate the crystal lattice with the nucleus having the the lowest mass per nucleon in the entire nuclear chart: $^ { 5 6 }$ Fe. However, as the pressure and the density increase, it becomes energetically advantageous for the system to lower its electron fraction $Y _ { e } = Z / A$ via electron capture on the protons. As a consequence, $^ { 5 6 }$ Fe ceases to be the optimal nucleus due to the presence of a uniform sea of neutralizing electrons whose chemical potential increases rapidly with density. Thus, the essential physics of the outer crust involves a competition between an electronic contribution that favors $Y _ { e } = 0$ and the nuclear symmetry energy that instead favors $Y _ { e } \simeq 1 / 2$ .

Ultimately, computing the nuclear composition of the stellar crust requires precise knowledge of nuclear masses over three well-defined regions of the nuclear chart. At the top of the crust the electronic contribution to the chemical potential is small to moderate, so the isotopes of relevance are located around the stable iron-nickel region where nuclear masses are very well known. As the proton fraction becomes too low and the symmetry energy large, it becomes energetically favorable for the system to jump into the $N = 5 0$ region. The nuclei of relevance in this region lie at the boundary between those whose masses are accurately known (e.g., ${ } ^ { 9 0 } \mathrm { Z r }$ , $^ { 8 8 }$ Sr, and $^ { 8 6 }$ $^ { 8 6 } \mathrm { K r }$ ) and those that are poorly known (such as $^ { 7 8 }$ Ni). We should mention that until very recently the mass of $^ { 8 2 }$ Zn was not known. Yet, the mass of $^ { 8 2 }$ Zn was determined fairly recently at the ISOLDE-CERN facility, leading to an interesting modification

of the crustal composition [29]. Finally, the third region comprising the bottom layers of the outer crust requires knowledge of nuclear masses at the $N = 8 2$ shell closure. Depending on the particular mass model, the nuclei of relevance span the region from $^ \mathrm { 1 3 2 }$ Sn $Z = 5 0$ ) all the way down to $^ { 1 1 8 }$ Kr ( $Z = 3 6$ ) [28]. For this region theoretical extrapolations are unavoidable as little or no experimental information is available [14]. Indeed, $^ { 1 1 8 }$ Kr is 21 neutrons away from the last measured isotope with a well measured mass [30].

# III. FORMALISM

# A. Bayesian neural networks

The novel theoretical approach that we advocate here aims to refine some existing mass models through a BNN approach [31]. Given the proven success of modern mass models, the BNN refinement is implemented by training a suitable neural network on the residuals between the experimental data and the “bare” (i.e., before refinement) theoretical predictions. Our ultimate goal is to generate a universal approximator [32, 33]; that is, a neural network that can provide an “educated” extrapolation into unexplored regions of the nuclear chart with properly quantified theoretical uncertainties. A detailed description of the origins and development of Bayesian neural networks goes beyond the scope of this paper; for a detailed exposition see Refs. [31, 34–36]. Thus, as we have done elsewhere [14– 16], we limit ourselves to highlight the main features of the approach. Before we do so, however, we note that the idea of using artificial neural networks in nuclear physics—mainly to estimate unknown properties of exotic nuclei of relevance to astrophysics—started in the early 90s with the work of Clark and collaborators [37–40] and continues up to this day [41–45] with more sophisticated applications.

Statistical inference based on Bayes’ theorem—as applied in this work—connects two critical pieces of information: (a) a prior hypothesis reflecting beliefs that one has acquired through experience or previous empirical information and (b) an improvement to the prior hypothesis by both adopting and adapting new evidence (e.g., experimental data). In this context Bayes’ theorem may be written as [46]:

$$
p (\omega | x, t) = \frac {p (x , t | \omega) p (\omega)}{p (x , t)}, \tag {8}
$$

where $p ( \omega )$ is the prior distribution of the model parameters $\omega$ and $p ( \boldsymbol { x } , t | \omega )$ is the “likelihood” that a given model $\omega$ describes the new evidence $t ( x )$ . The product of the prior and the likelihood form the posterior distribution $p ( \omega | x , t )$ that encodes the probability that a given model describes the data $t ( x )$ . In essence, the posterior represents the improvement to $p ( \omega )$ as a result of the new evidence $p ( \boldsymbol { x } , t | \omega )$ . Note that the “marginal likelihood” $p ( x , t )$ is independent of the model parameters $\omega$ , so for our purposes it may be regarded as an overall normalization factor. To define the likelihood we start by introducing an objective (or cost) function in terms of a least-squares fit to the empirical data. That is,

$$
\chi^ {2} (\omega) = \sum_ {i = 1} ^ {N} \left(\frac {t _ {i} - f (x _ {i} , \omega)}{\Delta t _ {i}}\right) ^ {2}, \tag {9}
$$

where $N$ is the total number of data points, $t _ { i } \equiv t ( x _ { i } )$ is the empirical value of the target evaluated at the $_ i$ th input $x _ { i }$ , $\Delta t _ { i }$ is the associated error, and the universal approximator $f ( x , \omega )$ depends on both the input data and the model parameters $\omega$ ; see Eq.(11) below. From such an objective function the likelihood is customarily defined as

$$
p (x, t | \omega) = \exp \left(- \chi^ {2} (\omega) / 2\right). \tag {10}
$$

In the particular case of interest here, i.e., nuclear masses, the input $x \equiv ( Z , A )$ represents the charge and mass number of the nucleus and $t ( x ) \equiv \delta M ( Z , A )$ the mass residual between the experimental data and the theoretical predictions. Note that maximizing the likelihood $p ( \boldsymbol { x } , t | \omega )$ provides the maximum likelihood estimation of the model parameters.

The neural network function $f ( x , \omega )$ adopted here has the following “sigmoid” form:

$$
f (x, \omega) = a + \sum_ {j = 1} ^ {H} b _ {j} \tanh  \left(c _ {j} + \sum_ {i = 1} ^ {I} d _ {j i} x _ {i}\right), \tag {11}
$$

where the model parameters (or “connection weights”) are collectively given by $\omega = \left\{ a , b _ { j } , c _ { j } , d _ { j i } \right\}$ , $H$ is the number of hidden nodes, and $I$ is the number of inputs. The “universal approximation theorem” states that such a neural network can accurately represent a wide variety of functions; tanh is a common form of the sigmoid activation function that

![](images/07e4b26fb561210237cad23041735360f5bf075863a9a6e6e5f5d45a3e86fdd6.jpg)  
FIG. 1. An example of a feed-forward neural network with a single hidden layer consisting of three nodes. In our case, the two inputs that define the nucleus of interest are $Z$ and $A$ , and a single output provides an estimate of $\delta M ( Z , A )$ , namely, the discrepancy between the bare theoretical prediction and the experimental value.

controls the firing of the artificial neurons [32, 33]. See Fig. 1 for a simple depiction of a feed-forward neural network consisting of a single hidden layer with three nodes.

Given the complexity of the posterior distribution $p ( \omega | x , t )$ , we adopt Markov Chain Monte Carlo (MCMC) sampling to generate a faithful equilibrium distribution. Once a significant number of samples has been generated, reliable estimates for both the average and variance of $\delta M ( Z , A )$ are obtained. That is,

$$
\langle f _ {n} \rangle = \frac {1}{K} \sum_ {k = 1} ^ {K} f \left(x _ {n}, \omega_ {k}\right), \tag {12a}
$$

$$
\langle f _ {n} ^ {2} \rangle = \frac {1}{K} \sum_ {k = 1} ^ {K} f ^ {2} \left(x _ {n}, \omega_ {k}\right), \tag {12b}
$$

$$
\Delta f _ {n} = \sqrt {\left\langle f _ {n} ^ {2} \right\rangle - \left\langle f _ {n} \right\rangle^ {2}}, \tag {12c}
$$

where $x _ { n } = ( Z _ { n } , A _ { n } )$ represents a particular nucleus with charge $Z _ { n }$ and mass number $A _ { n }$ , $K$ is the total number of Monte Carlo configurations, and $f ( x _ { n } , \omega _ { k } )$ is the neural network estimate of $\delta M ( Z _ { n } , A _ { n } )$ as predicted by the $k$ th Monte Carlo configuration.

Finally, we conclude this section by briefly addressing the choice of prior $p ( \omega )$ assumed in this work. Prior probabilities encode our beliefs concerning the model parameters and are an essential ingredient of the Bayesian paradigm. Normally, the prior is highly informative as it is based on our own physics biases and intuition, which are often well informed by prior experimental data. Unfortunately, whereas physics principles guide the construction of modern nuclear mass models, physics intuition is of no help in designing the connection weights $\omega$ . Thus, we are forced to rely on assumptions that have been proven effective and reliable through mostly trial and error [31]. Following our earlier work [14], we assume all connection weights to be independent and adopt a Gaussian prior centered around zero and with a width determined as in Ref. [31]. For an extensive discussion on the determination of the “hyperparameters” controlling the width of the Gaussian prior see Refs. [47, 48].

# IV. RESULTS

The aim of this section is to discuss the improvement to three successful mass models as a result of the BNN refinement. The three models under consideration are: (i) the 10-parameter Duflo-Zuker model (DZ10) [49], (ii) the 28-parameter Duflo-Zuker model (DZ) [21], and (iii) the microscopic Hartree-Fock-Bogoliubov model (HF19) of Ref. [22]. In all three cases the predictions after refinement have the distinct advantage of being accompanied by theoretical uncertainties. However, for the simpler DZ10 model we found instructive to re-calibrated the modelparameters, as this process generates a suitable covariance matrix from where statistical uncertainties and correlation coefficients may be computed. To reiterate, the basic paradigm of our two-pronged approach is to start with a robust underlying mass model that captures as much physics as possible followed by a BNN refinement that will hopefully account for the missing physics [14].

The original Duflo-Zuker model containing a total of 28 parameters has stood the test of time [21]. The DZ model, fitted to the set of existing nuclear masses appearing in the 1995 compilation by Audi and collaborators [50], was enormously successful in predicting the more than 300 additional masses that appeared in the later AME03 compilation [51]. Indeed, the success of the DZ model in accurately reproducing the masses of the more than 3,000 nuclei presently known is truly remarkable [52]. However, despite its undeniable success, the underlying physics of the model remains puzzling and difficult to unravel. The simpler 10-parameter Duflo-Zuker model was conceived with the sole purpose of illuminating the physics. A detailed study of DZ10 that aims to understand and possibly to also improve the model has been carried out recently by Mendoza-Temis, Hirsch, and Zuker [49]. Even more recently, Doboszewski and Szpak have refitted DZ10 with the goal of quantifying the model uncertainties and the correlations among the model parameters [53].

We also proceed here by recalibrating the model parameters following closely Ref. [53]. To do so we start by constructing a likelihood function defined in terms of the square differences between the DZ10 predictions and the experimental binding energies provided by the AME2012 compilation [30]; we limit ourselves to the $^ { 4 0 }$ Ca to 240U region. For the initial distribution of model parameters we use an uninformative prior. In this way we generate a posterior probability distribution that is generated through Markov-Chain Monte Carlo (MCMC) sampling. Simulating such a posterior distribution is computationally inexpensive so we could afford generating one million Monte Carlo configurations, with the first 10,000 steps used for thermalization. To avoid correlations among subsequent configurations, we found that an autocorrelation “time” of about 20 configurations was sufficient. Overall, we used nearly 50,000 configurations to generate the correlation plot depicted in Fig. 2 together with the average values and uncertainties listed in Table I. For comparison, also included in Table I are the results reported in Refs. [49, 53].

![](images/aeeb43967c6d5ad4ac015ff2faeac51d7841b7aa1a1a6af5203d6c565338d846.jpg)  
FIG. 2. Correlations coefficients and marginalized probability densities (shown along the diagonal) for the 10-parameter Duflo-Zuker model [21, 49, 53].

Once the theoretical predictions from the DZ10 model—or indeed any other mass model—have been generated, the BNN refinement proceeds by separating the available experimental data into two disjoint sets: a learning and a validation set. Again, to avoid regions of the nuclear landscape where the masses fluctuate too rapidly (as in the case of the lightest nuclei) we limit the experimental data set to the 2,000-plus well measured nuclei between $^ { 4 0 }$ Ca and $^ { 2 4 0 }$ U. The learning set consists of a randomly-selected subset of nuclei contained within the experimental database that will be used to train the neural network, namely, to calibrate the connection weights as defined in Eq.(11). On the

TABLE I. Average values and uncertainties for the 10-parameter Duflo-Zuker model [21]. Comparisons are made against similar results presented in Ref. [49] (without uncertainties) and Ref. [53]. Here $\sigma$ represents the root-mean-square deviation of the predictions relative to the AME2012 compilation [52].   

<table><tr><td>Parameter</td><td>Ref [49]</td><td>Ref. [53]</td><td>This work</td></tr><tr><td>θ1=a3</td><td>0.707</td><td>0.70506(37)</td><td>0.70452(27)</td></tr><tr><td>θ2=a1</td><td>17.766</td><td>17.749 (70)</td><td>17.7466(49)</td></tr><tr><td>θ3=a2</td><td>16.314</td><td>16.267(2)</td><td>16.277(17)</td></tr><tr><td>θ4=a4</td><td>37.515</td><td>37.465(4)</td><td>37.608(27)</td></tr><tr><td>θ5=a5</td><td>53.351</td><td>53.23(19)</td><td>54.08(11)</td></tr><tr><td>θ6=a7</td><td>0.478</td><td>0.4631(58)</td><td>0.4601(63)</td></tr><tr><td>θ7=a8</td><td>2.183</td><td>2.101(30)</td><td>2.088(33)</td></tr><tr><td>θ8=a9</td><td>0.022</td><td>0.02144(17)</td><td>0.02106(19)</td></tr><tr><td>θ9=a10</td><td>41.338</td><td>41.5310(2)</td><td>41.50(22)</td></tr><tr><td>θ10=a6</td><td>6.199</td><td>6.238(89)</td><td>6.455(81)</td></tr><tr><td>σ (MeV)</td><td>0.554</td><td>0.571</td><td>0.552</td></tr></table>

other hand, the validation set comprises the remaining nuclei that, while still in the existent experimental database, were not used in the training of the network. Thus, the validation set provides the testbed for assessing the quality of the artificial neural network. If the test is successful, then one re-calibrates the network parameters using the entire experimental database in order to predict the masses of nuclei that have not yet been measured, yet are essential for astrophysical applications. Given that the limits of nuclear binding is one of the key science driver animating nuclear science today [54], besides generating refined mass tables we also provide tables for one- and two-nucleon separation energies:

$$
S _ {n} (Z, N) \equiv M (Z, N - 1) + m _ {n} - M (Z, N) = B (Z, N) - B (Z, N - 1), \tag {13a}
$$

$$
S _ {p} (Z, N) \equiv M (Z - 1, N) + m _ {p} - M (Z, N) = B (Z, N) - B (Z - 1, N), \tag {13b}
$$

$$
S _ {2 n} (Z, N) \equiv M (Z, N - 2) + 2 m _ {n} - M (Z, N) = B (Z, N) - B (Z, N - 2), \tag {13c}
$$

$$
S _ {2 p} (Z, N) \equiv M (Z - 2, N) + 2 m _ {p} - M (Z, N) = B (Z, N) - B (Z - 2, N). \tag {13d}
$$

All these BNN-improved tables are generated from the same ensemble of Monte Carlo configurations, so that theoretical uncertainties may be reliably attached to each individual prediction.

![](images/800551ad22ee90a69101b66485d8e3d01b6ef81fe5cfec673a3f2ce6e08d44f3.jpg)  
FIG. 3. Proton and neutron drip lines as predicted by both the bare and BNN-refined 10-parameter Duflo-Zuker (DZ10) model. In the case of the BNN predictions, the neutron drip line evolves into a “drip band” due to statistical uncertainties. Also shown (with green points) is the AME2012 data set [30] with the stable nuclei displayed with black points.

The calibration of the neural network is computationally expensive. With two input variables ( $Z$ and $N$ ) and a “canonical” number of $H = 4 0$ hidden nodes, a total of $1 + 4 H = 1 6 1$ parameters must be calibrated. To do so, we rely on the Flexible Bayesian Modeling package by Neal described in detail in Ref. [31]. After an initial thermalization phase consisting of 500 Monte-Carlo steps, a sampling set of 100 configurations is accumulated to determine statistical

averages and their associated uncertainties. As a measure of the accuracy of our predictions, we report root-meansquare (rms) deviations relative to experiment; for simplicity, the comparison is done using exclusively average values. Due to the relative simplicity of the DZ10 model, we were able to implement the BNN refinement using two different schemes. The first scheme consists of a unique set of masses obtained from the average values generated by the new DZ10 calibration—without accounting for the uncertainties in the bare model parameters. The second scheme remedies such deficiency by effectively incorporating the distribution of DZ10 model parameters depicted in Fig. 2. Such improved version is useful in assessing whether a recalibration of the bare model parameters may be necessary in other cases. Fortunately, our results suggest that, at least in the case of DZ10, this is not required. Our results indicate that whereas there is indeed a dramatic improvement in the predictions of the bare DZ10 model after the BNN refinement—from $\sigma _ { \mathrm { r m s } } = 0 . 5 5 2 \mathrm { M e V }$ to $\sigma _ { \mathrm { r m s } } = 0 . 2 9 2$ MeV—no significant changes are observed when one uses the proper statistical distribution of bare DZ10 parameters; for for this latter case one obtains $\sigma _ { \mathrm { r m s } } = 0 . 2 9 6 1$ MeV.

As alluded earlier, for each of the 100 Monte-Carlo configurations obtained from the BNN refinement one computes at every MC step the mass of each individual nucleus. Having generated all nuclear masses in such a way, one may then compute the mass differences required to generate one- and two-nucleon separation energies. At each MC step one proceeds in this same exact fashion, until by the end of the 100 Monte-Carlo configurations one can finally extract average values and associated theoretical uncertainties for each nuclear observable. The outcome of such a procedure is displayed in Fig. 3 for neutron and proton drip lines, identified at the point in which the two-neutron and two-proton separation energies become negative. For the case of the bare DZ10 model, the drip lines are displayed by a solid (red) line. In contrast, BNN-improved DZ10 predictions produce drip bands, as all the predictions are now accompanied by statistical uncertainties. Note that because of the Coulomb repulsion, the proton drip line is much closer to the valley of stability than the corresponding neutron drip line. Indeed, whereas the proton drip line has been experimentally established for a large number of nuclei (up to atomic number $Z = 9 1$ ), the neutron drip line is only known up to $Z = 8$ , with $^ { 2 4 } \mathrm { O }$ being the heaviest known oxygen isotope that remains stable against particle decay [55]. Moreover, Fig. 3 displays the characteristic signature of shell closures at neutron magic numbers 50, 82, 126, and (predicts) 184. Finally, the figure encapsulates the enormous experimental challenges faced in mapping the neutron drip line. However, even if reaching the neutron drip line for heavy nuclei may not be feasible in the foreseeable future, it is essential to continue the experimental quest to properly inform theoretical models. In turn, BNN approaches as the one advocated here may guide experimental searches for those “few” critical nuclei that may reduce the large systematic uncertainty that currently plagues theoretical models.

![](images/8722e340e9c572c5abad88ec6bf9f0abaf45bfa893da343869535667410b0200.jpg)

![](images/6d971c9e4eb79d80f1fc60890ed67ac44ffa0fde98cba907e971a1e8b94b7114.jpg)

![](images/b75984fb6c533816a0a329d462286ff22cc7ea0d51cb7b7c36dfdfb312c6b307.jpg)

![](images/96aeafed06626c72f975e9acbecd1c5583008d5cdb1a6cf47982c21511afc7ef.jpg)  
FIG. 4. Proton and neutron drip lines/drip bands as predicted by (a) the Duflo-Zuker model [21] and (b) the HFB19 model [22]; in both cases bare and BNN-refined predictions are displayed. The remaining two panels display the same information but now the comparison is between the predictions of both mass models: (c) displays bare-model results whereas (d) the corresponding ones after BNN-refinement. Also shown (with green points) is the AME2012 data set [30] with the stable nuclei displayed with black points.

So far DZ10 has provided a benchmark to quantify the impact of the BNN refinement and the role of uncertainty quantification. We found that while the BNN refinement is critical in improving the predictions of the model, there

seems to be little value in propagating the uncertainties inherent to the bare model. Thus, we now proceed to document and test the predictions of the two state-of-the-art mass models that will be refined in order to generate BNN-improved tables; the 28-parameter “mic-mac” model of Duflo and Zuker [21] and the microscopic HFB19 model of Goriely, Chamel, and Pearson [22]. Drip lines and drip bands as predicted by these two models are displayed in Fig. 4. The two left-hand panels, (a) for Duflo-Zuker and (b) for HFB19, aim to illustrate the improvement to the bare models as a result of the BNN refinement. Note that although the overall improvement to both mass models is considerable—about 40% [14]—the changes are difficult to discern because both the expanded scale as well as the intrinsic high quality of the bare models. In contrast, the two right-hand panels compare the models to each other: (c) for the bare predictions and (d) for the BNN-improved versions. In this case the improvement is clearly discernible, as the model discrepancies displayed by the bare models get significantly quenched after the BNN refinement. Indeed, at first there is an appreciable discrepancy in the predictions of the bare models—with HFB19 consistently predicting the location of the neutron drip line at larger values of $N .$ . Remarkably, much of the discrepancy disappears after the BNN refinement, especially in the region between shell closures $N = 8 2$ and $N = 1 2 6$ . Such reduction in the systematic model error is highly desirable and entirely consistent with the results obtained in an earlier publication [14]. Moreover, we observe a significant quantitative improvement in the predictions of both models. In the case of the Duflo-Zuker mass formula the root-mean-square mass deviation improves from $\sigma _ { \mathrm { r m s } } { = } 0 . 5 0 3$ MeV to $\sigma _ { \mathrm { r m s } } { = } 0 . 2 8 6 \mathrm { M e V }$ , whereas in the case of HFB19 it goes from $\sigma _ { \mathrm { r m s } } { = } 0 . 5 5 9$ MeV to $\sigma _ { \mathrm { r m s } } { = } 0 . 3 5 8 \ N$ eV.

We close this section with a brief discussion of the impact of the BNN refinement on a few critical $r$ -process nuclei that emerge from the sensitivity study of Mumpower and collaborators [9–11]; specifically, palladium ( $Z = 4 6$ ), cadmium ( $Z = 4 8$ ), indium ( $Z = 4 9$ ), and tin ( $Z = 5 0$ ). Note that these results may be readily extended to other isotopes by employing the refined mass tables provided here as supplemental material. The main goal of our analysis is to assess whether the ubiquitous bare-model discrepancies can be systematically reduced after the implementation of the BNN refinement.

![](images/a9002c3452051a7b18fc05b6b1d931e7f2627dadf80fd44fa7155415deed0e6c.jpg)

![](images/2e2a678e3748172f3b7ac059a014f75868b70070786c248e13fd437e01d9a13a.jpg)

![](images/91da8cd22b8dd4e603dbe8f133563d5a56254a6e13295c4a12f8b855fe593865.jpg)

![](images/d2bb22c50fe6374009de82bbb9c88e3ad0541dfb98933be0a6c50cd4837671b2.jpg)  
N   
N   
FIG. 5. Mass predictions for (a) palladium ( $Z = 4 6$ ), (b) cadmium ( $Z = 4 8$ ), (c) indium ( $Z = 4 9$ ), and (d) tin ( $Z = 5 0$ ) for both the Duflo-Zuker [21] and HFB19 [22] mass models. The predictions are relative to a reference mass value taken from either the AME2012 compilation when available [30] or from the bare Duflo-Zuker model when unavailable. Predictions are displayed with statistical error bars for the BNN-improved models.

In Fig. 5 we display model predictions relative to a reference mass value for palladium, cadmium, indium, and

tin in the region $N \gtrsim 8 2$ . The masses of all 18 nuclei displayed in the figure, 130−132Pd, $1 3 2 { - } 1 3 8$ Cd, $1 3 3 - 1 3 8$ In, and 136,138Sn, have been identified as important nuclei in the determination of the $r$ -process abundance pattern; see Table I in Ref. [11]. Note that the reference mass has been adopted from either “experimental” values (although derived not from purely experimental data [30]) or when data is unavailable, from the predictions of the bare Duflo-Zuker model. Theoretical predictions with error bars are from the BNN-refined models. We can state categorically that the BNN refinement has an appreciable impact in reducing the systematic model discrepancies. Easiest to visualize are the cases of palladium and tin where the number of isotopes displayed is small; three and two, respectively. For palladium there is no available experimental data so we display theoretical estimates relative to the predictions from the bare Duflo-Zuker model (depicted by the light-blue line). Whereas the bare HFB19 predictions hover around 0.5-1 MeV relative to such a baseline, the model discrepancy narrows considerably after the BNN refinement. Indeed, for 130Pd the predictions are now consistent with each other and for the most unfavorable case of $^ { 1 3 0 }$ Pd they agree at the $2 \sigma$ level. For tin the situation is similar, although in this case we display with a red line the recommended experimental values [30]. Once again, we note that the bare-model predictions differ significantly from each other and, especially in the case of HFB19, from the recommended AME2012 values. However, once the BNN refinement is completed, both the model discrepancy is significantly reduced and the comparison with experiment is much more favorable. Indeed, both BNN-DZ predictions are now fully consistent with experiment. Finally, the two remaining isotopes of cadmium and indium display the same trends observed so far. In particular, note that for all of these 18 important nuclei the BNN refinement suggest an increase in the value of the mass, or equivalently, a reduction in the binding energy. For these two larger isotopic chains—having seven and six important nuclei, respectively—experimental mass values do exist but only for the smaller values of $N$ . Yet regardless of whether experimental masses are available, we see the model spread diminishes considerably after the BNN refinement. And when recommended mass values exist, the BNN predictions are practically consistent with experiment. The isotopic chain in cadmium contains the largest number of important $r$ -process nuclei. As we have learned from earlier studies (see for example Refs. [10, 17, 54]) bare-model discrepancies diverge dramatically as one moves away from measured mass values. This is evident in Fig. 5b where the bare-model discrepancy becomes as large as $\sim 2$ MeV for $^ \mathrm { 1 3 8 }$ Cd (i.e., $N = 9 0$ ). Remarkably, all model discrepancies are largely eliminated after the BNN refinement. In particular, even for the least favorable case of $^ \mathrm { 1 3 8 }$ Cd the $1 \sigma$ mismatch gets reduced to merely 130 keV.

![](images/3b7c476451766750c6ed5f232124a3746b16e202db12c60559826ab130423a3c.jpg)  
FIG. 6. Two-neutron separation energies for all even-even cadmium isotopes from $^ { 9 4 }$ Cd to $^ \mathrm { 1 6 4 }$ Cd, as predicted by the mic-mac model of Duflo and Zuker [21] and the microscopic HFB19 model [22]. Predictions are displayed without error bars for the bare models and with error bars after the BNN refinement. Experimental data are from Ref. [30].

We conclude this section by displaying in Fig. 6 two-neutron separation energies for all even-even isotopes in cadmium: from $^ { 9 4 }$ Cd to $^ \mathrm { 1 6 4 }$ Cd. Clearly discernible in the figure is the characteristic “jumps” at magic numbers 50 and 82. The figure also encapsulates the inherent risk in extrapolating theoretical models far away from regions where

experimental information is available. Whereas the models agree where data is available (from $5 0 \leq N \leq 8 2$ ), the model-discrepancy grows gradually with increasing neutron numbers. And while the BNN refinement is successful in mitigating the problem up to $N { \lesssim } 9 0$ (see Fig. 5c), the BNN predictions for $S _ { 2 n }$ can differ by $\sim 1$ MeV far away from stability. This situation is reminiscent of the one addressed in Ref. [54] for $S _ { 2 n }$ in the case of the even-even erbium ( $Z = 6 8$ ) isotopes. It was found there that the discrepancy between various model predictions steadily grows with neutron excess as a result of the poorly known isovector effective interaction. Indeed, models that are successful in reproducing the experimentally determined two-neutron separation energy, differ in their predictions of the location of the neutron drip line by as many as eight neutrons. Fortunately, next-generation rare-isotope facilities will produce hundreds of new exotic nuclei very far away from stability that will help constrain the isovector sector. Yet a most pressing challenge is to identify the “few” critical nuclei that will best inform nuclear theory. We are confident that the BNN formalism will successfully meet this challenge.

# V. CONCLUSIONS

The quest for the nuclear driplines is at the heart of one of the central themes animating nuclear physics today: what are the limits of nuclear existence? As a fundamental nuclear-structure problem, the driplines define the most extreme combinations of protons and neutrons that can remain bound by the strong nuclear force. Drip-line nuclei are weakly bound, finite, strongly correlated quantum systems where the virtual coupling to the continuum is critical. Besides being of intrinsic interest in nuclear structure, nuclei far away from stability also play a predominant role in astrophysics; for example, in stellar nucleosynthesis and in neutron stars. However, the enormous theoretical challenges faced in describing exotic nuclei are compounded by the lack of experimental guidance. For example, theoretical predictions seem to suggest that 118Kr is the drip-line nucleus separating the inner and outer crust of neutron stars. Yet $^ { 1 1 8 }$ Kr is 21 neutrons away from the last well-measured isotope. Thus, having to resort to extrapolations seems unavoidable.

Undoubtedly, large extrapolations pose a considerable risk. In an effort to mitigate such risk we proposed a novel approach based on the construction of an artificial neural network. Moreover, given that the neural-network parameters are determined through Bayesian inference, our results are accompanied by statistical uncertainties. The proposed approach adopts a highly successful mass model that is then refined through the construction of an artificial neural network. Briefly, the implementation of the BNN refinement proceeds by dividing the existing experimental database of nuclear masses into a learning and a validation set, with the members of each set selected at random. One then uses the learning set to train the artificial neural network by focusing on the mass residuals, i.e., on the difference between the experimentally measured and predicted mass. The validation set is then used to test the robustness and reliability of the refined model. If a significant improvement relative to the bare model is observed, then the training is repeated but now using the entire experimental database. Although we developed most of these ideas using the relatively simple, yet highly accurate, 10-parameter Duflo-Zuker model, our ultimate goal was to publish refined mass tables for two existing mass models, one microscopic and the other one of the mic-mac type. For the latter we used the 28-parameter Duflo-Zuker model while for the former HFB19.

These are some of the most salient conclusions of our work. First, despite the intrinsic high-quality of both mass models, the BNN refinement lead to a significant improvement: $\sigma _ { \mathrm { r m s } } = ( 0 . 5 0 3  0 . 2 8 6 ) \mathrm { M e }$ V and $\sigma _ { \mathrm { r m s } } = ( 0 . 5 5 9 $ 0.358) MeV for DZ and HFB19, respectively. Second, although theoretical mass models agree in regions where masses are known but differ widely in regions where they are not, we found a systematic and significant reduction in the model spread after implementing the BNN refinement. Third, given the Bayesian character of the approach, all BNN refined predictions are now accompanied by theoretical uncertainties. Finally, we provided as supplemental material mass tables, as well as tables for other derived quantities such as separation energies, for the two BNN refined models considered in this work. We trust that these refined mass tables will be helpful for future astrophysical applications.

# ACKNOWLEDGMENTS

This material is based upon work supported by the U.S. Department of Energy Office of Science, Office of Nuclear Physics under Award Number DE-FD05-92ER40750.

[1] Reaching for the Horizon; The 2015 Long Range Plan for Nuclear Science (2015).   
[2] D. D. Clayton, “Principles of stellar evolution and nucleosynthesis,” (University of Chicago Press, Chicago, 1983).   
[3] A. C. Phillips, “The physics of stars,” (John Wiley & Sons, Chichester, 1998) 2nd ed.   
[4] C. Iliadis, “Nuclear physics of stars,” (Wiley-VCH, Weinheim, 2007).   
[5] M. E. Burbidge, G. R. Burbidge, W. A. Fowler, and F. Hoyle, Rev. Mod. Phys. 29, 547 (1957).   
[6] G. Wallerstein, I. Iben, P. Parker, A. M. Boesgaard, G. M. Hale, A. E. Champagne, et al., Rev. Mod. Phys. 69, 995 (1997).   
[7] Connecting Quarks with the Cosmos: Eleven Science Questions for the New Century (The National Academies Press, Washington, 2003).   
[8] I. Petermann, G. Mart´ınez-Pinedo, A. Arcones, W. R. Hix, A. Keli, K. Langanke, I. Panov, T. Rauscher, K.-H. Schmidt, F.-K. Thielemann, and N. Zinner, Journal of Physics: Conference Series 202, 012008 (2010).   
[9] M. R. Mumpower, R. Surman, G. C. McLaughlin, and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016).   
[10] M. Mumpower, R. Surman, D. L. Fang, M. Beard, and A. Aprahamian, J. Phys. G42, 034027 (2015).   
[11] M. R. Mumpower, R. Surman, D. L. Fang, M. Beard, P. Moller, T. Kawano, and A. Aprahamian, Phys. Rev. C92, 035807 (2015).   
[12] G. Baym, C. Pethick, and P. Sutherland, Astrophys. J. 170, 299 (1971).   
[13] X. Roca-Maza and J. Piekarewicz, Phys. Rev. C78, 025807 (2008).   
[14] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C93, 014311 (2016).   
[15] J. Piekarewicz and R. Utama, Proceedings, 34th Mazurian Lakes Conference on Physics: Frontiers in Nuclear Physics: Piaski, Poland, September 6-13, 2015, Acta Phys. Polon. B47, 659 (2016).   
[16] R. Utama, W.-C. Chen, and J. Piekarewicz, J. Phys. G (2016).   
[17] K. Blaum, Physics Reports 425, 1 (2006).   
[18] P. M¨oller and J. R. Nix, Atom. Data Nucl. Data Tabl. 26, 165 (1981).   
[19] P. M¨oller and J. R. Nix, Atom. Data Nucl. Data Tabl. 39, 213 (1988).   
[20] P. M¨oller, J. R. Nix, W. D. Myers, and W. J. Swiatecki, Atom. Data Nucl. Data Tabl. 59, 185 (1995).   
[21] J. Duflo and A. Zuker, Phys. Rev. C 52, R23 (1995).   
[22] S. Goriely, N. Chamel, and J. Pearson, Phys. Rev. C82, 035804 (2010).   
[23] M. Kortelainen, T. Lesinski, J. More, W. Nazarewicz, J. Sarich, et al., Phys.Rev. C82, 024313.   
[24] J. Erler, C. J. Horowitz, W. Nazarewicz, M. Rafalski, and P.-G. Reinhard, Phys. Rev. C87, 044320 (2013).   
[25] P. Haensel, J. L. Zdunik, and J. Dobaczewski, Astron. Astrophys. 222, 353 (1989).   
[26] P. Haensel and B. Pichon, Astron. Astrophys. 283, 313 (1994).   
[27] S. B. Ruester, M. Hempel, and J. Schaffner-Bielich, Phys. Rev. C73, 035804 (2006).   
[28] X. Roca-Maza, J. Piekarewicz, T. Garcia-Galvez, and M. Centelles, in Neutron Star Crust, edited by C. Bertulani and J. Piekarewicz (Nova Publishers, New York, 2011).   
[29] R. Wolf et al., Phys. Rev. Lett. 110, 041101 (2013).   
[30] M. Wang, G. Audi, A. Wapstra, F. Kondev, M. MacCormick, X. Xu, and B. Pfeiffer, Chinese Phys. C 36, 1603 (2012).   
[31] R. Neal, Bayesian Learning of Neural Network (Springer, New York, 1996).   
[32] G. Cybenko, Math. Control Signals Systems 2, 303 (1989).   
[33] K. Hornik, M. Stinchcombe, and H. White, Neural Networks 2, 359 (1989).   
[34] C. Bishop, Neural Networks for Pattern Recognition (Oxford University Press, Birmingham, UK).   
[35] S. Haykin, Neural Networks: A Comprehensive Foundation (Prentice Hall, Upper Saddle River, NJ).   
[36] V. Vapnik, Statistical Learning Theory (Wiley-Interscience, New York, NY).   
[37] S. Gazula, J. Clark, and H. Bohr, Nucl. Phys. A 540, 1 (1992).   
[38] K. Gernoth, J. Clark, J. Prater, and H. Bohr, Phys. Lett. B 300, 1 (1993).   
[39] K. Gernoth and J. Clark, Neural Networks 8, 291 (1995).   
[40] J. W. Clark, T. Lindenau, and M. Ristig, “Scientific applications of neural nets springer lecture notes in physics,” (Springer-Verlag, Berlin, 1999) pp. 1–96.   
[41] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Nucl. Phys. A743, 222 (2004).   
[42] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Nuclear mass systematics by complementing the finite range droplet model with neural networks, edited by G. Lalazissis and C. Moustakidis (Advances in Nuclear Physics, Proceedings of the 15th Hellenic Symposium on Nuclear Physics, 2006) pp. 65–70.   
[43] J. W. Clark and H. Li, Int. J. Mod. Phys. B20, 5015 (2006).   
[44] N. J. Costiris, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Phys. Rev. C 80, 044332 (2009).   
[45] T. Bayram, S. Akkoyun, and S. O. Kara, Annals of Nuclear Energy 63, 172 (2014).   
[46] J. V. Stone, “Bayes’ rule: A tutorial introduction to bayesian analysis,” (Sebtel Press, Sheffield, UK, 2013) 1st ed.   
[47] D. J. MacKay, Nuclear Instruments and Methods in Physics Research Section A 354, 73 (1995).   
[48] D. J. MacKay, Neural Computation 11, 1035 (1999).   
[49] J. Mendoza-Temis, J. G. Hirsch, and A. P. Zuker, Nucl. Phys. A843, 14 (2010).   
[50] G. Audi and A. H. Wapstra, Nucl. Phys. A595, 409 (1995).   
[51] G. Audi, A. H. Wapstra, and C. Thibault, Nucl. Phys. A729, 337 (2002).   
[52] M. Wang, G. Audi, A. H. Wapstra, F. G. Kondev, M. MacCormick, X. Xu, and B. Pfeiffer, Chinese Phys. C 36, 1603 (2012).

[53] I. Doboszewski, Predictive Power of Atomic Nuclei Mass Models, Master’s thesis, AGH University of Science and Technology, Cracow, Poland (2014), in Polish, unpublished.   
[54] J. Erler, N. Birge, M. Kortelainen, W. Nazarewicz, E. Olsen, A. M. Perhac, and M. Stoitsov, Nature 486, 509 (2012).   
[55] M. Thoennessen, Rep. Prog. Phys. 67, 1187 (2004).