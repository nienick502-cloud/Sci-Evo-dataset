# Statistical learnability of nuclear masses

A. Idini

Division of Mathematical Physics, Department of Physics, LTH,

Lund University, Post Office Box 118, S-22100 Lund, Sweden

After more than 80 years from the seminal work of Weizs¨acker and the liquid drop model of the atomic nucleus, deviations from experiments of mass models ( $\sim$ MeV) are orders of magnitude larger than experimental errors ( $\lesssim$ keV). Predicting the mass of atomic nuclei with precision is extremely challenging. This is due to the non–trivial many–body interplay of protons and neutrons in nuclei, and the complex nature of the nuclear strong force. Statistical theory of learning will be used to provide bounds to the prediction errors of model trained with a finite data set. These bounds are validated with neural network calculations, and compared with state of the art mass models. Therefore, it will be argued that the nuclear structure models investigating ground state properties explore a system on the limit of the knowledgeable, as defined by the statistical theory of learning.

Introduction. Many relevant properties of the atomic nuclei are extremely sensitive to their binding energy, i.e. mass, e.g. decay lifetimes and reaction rates. Therefore, the highest possible precision in reproducing and predicting nuclear masses is needed [1]. However, current state of the art models deviate from experimental binding energies orders of magnitude more than experimental errors. This letter will investigate difficulty of improving the precision of nuclear mass models from an information theory point of view.

The complexity of this problem was hinted in the context of chaotic quantum systems [2, 3]. That is, the statistical distribution of masses shows a chaotic behaviour is formidable to deterministically reproduce (cf. also [4]). The amount of nuclear structure data is related to the finite number of nuclear isotopes available in the laboratory and that can possibly exist. In particular, theories that model only the ground state, such as some mass models and density functional theory (DFT), in principle access only few ground state properties of each nucleus. As of the last atomic mass evaluation [5], 3435 nuclei have been measured in the laboratories around the world. Due to the lack of a comprehensive model of nuclear binding energies, it is not known how many nuclei could exist. However, it is safe to assume that this number will not change by an order of magnitude (the current consensus argues that $\sim 7 0 0 0$ nuclei can possibly exist [1]). In practice, many of these exotic nuclei will not be measured in the foreseeable future. The effect of the limited number of nuclear masses available can be investigated using statistical learning theory.

Statistical learning theory deals with the problem of devising a specific predictive model, belonging to a class of models $\Lambda$ , using a set of data. When the number of data is finite, there is a limit to the precision that can be reached by a model. Qualitatively, the more a model is complex the more data it will need to reach a given predictive power. This manuscript will analyse the statistical learning bounds of deviation reachable by models attempting to reproduce and predict nuclear binding en-

ergies. This is done considering the mass model a statistical learning problem [6] with a complexity constrained by its parametric representation and the precision limited by finite number of available data points. Perceptron networks will be used to validate the statistical learning theory assumptions in this context. Moreover, the bounds for notable density functionals will be examined. The tools here provided enable the analysis of the performance that can be expected from a model when the statistical treatment is rigorous and without bias. This will shed light on the development of functionals and mass models from an information theory perspective.

Method. Statistical learning frames within quantifiable boundaries the effect that limited information has in the training of models [7]. The objective of a general learning problem is the minimization of the total risk functional $R ( \alpha )$ . That is, finding the set of parameters $\alpha$ by which a given model best reproduces the data available and predicts the ones that could be taken under consideration. However, when working with a finite data set, what is actually minimized is the empirical risk. That is, the risk evaluated over a finite number of data $\it l$ . Usually the risk is defined using the root mean square deviation (RMSD) of model function or functional $f _ { \alpha }$ respect to the data. $f _ { \alpha }$ takes a set $\alpha$ of parameters belonging to a space $\Lambda$ which defines the class of models under consideration. Therefore, the value of $\alpha$ which minimizes $R _ { e m p } ( \alpha )$ have to be found. Under specific conditions, defined by the empirical risk minimization principle (ERM), the minimum of $R _ { e m p } ( \alpha )$ converges (in probability) to the minimum of the total risk functional $R ( \alpha )$ when the number of data is large ( $l  \infty$ ) [6, 8]. Therefore this principle enables a model to make reliable predictions.

However, when the number of data is finite, a good $R _ { e m p }$ does not guarantee a corresponding predictivity (i.e., good total risk). In the case of limited number data, a model trained on limited data has only a probability of being generalizable for predictions. In this case, the complexity of the model plays a role. A conventional rule of thumb is that, given the same performance on

known data, a “simple” model generalizes better than a “complicated” one. The complexity is often summarily evaluated as the number of free parameters. This is well known as the Occam’s razor principle [9] (cf. also [10]). Statistical learning theory can precisely quantify the impact of the tradeoff between complexity and data availability through the structural risk minimization (SRM) induction principle [7, 11].

The degree of complexity of a set of functions can be quantitatively defined using Vapnik and Chervonekis (VC)–dimension [12]. The VC–dimension is, for a set of boolean functions $\Theta _ { \alpha } ( x )$ with $\alpha \in \Lambda$ , the maximum number $h$ of input vectors that can be shattered, i.e. $x _ { 1 } , . . . , x _ { h }$ separated in the $2 ^ { h }$ possible ways by the function in set $\Lambda$ . The definition can be generalized for a bounded, real model $a \leq f _ { \alpha } ( x ) \leq b$ , with $a , b \in \mathbb { R }$ (in the mass model case, e.g. $a = 0$ MeV and $b = 8 . 7 9 4 5$ MeV is the maximum binding energy per nucleon, that is of $^ { 6 2 }$ Ni isotope), defining a corresponding set of boolean functions,

$$
\Theta_ {\alpha} (x, c) = \theta \left(f _ {\alpha} (x) - c\right), \tag {1}
$$

with $\theta$ the Heaviside unit step function ( $\theta ( z ) = 0$ for $z < 0$ , and $\theta ( z ) = 1$ for $z \geq 0$ ), and $c \in ( 0 , b )$ . The VC– dimension of the set of real valued $f _ { \alpha } ( x )$ corresponds to the VC–dimension of the set of the indicator functions $\Theta _ { \alpha } ( x , c )$ in Eq. (1) [13]. That is, the number of points in $\mathbb { R }$ the related indicator function (1) can shatter.

For example, a lower bound on the VC–dimension of a polynomial in $f : \mathbb { N } ^ { 2 } \to \mathbb { R }$ is given by lifting the polynomial to the space of its monomials, and generating a set of point associated with each of the terms of the basis of polynomials. Therefore, is possible to calculate the complexity of this notable polynomial,

$$
E (N, Z) = \sum_ {i, j = 0} ^ {N} a _ {i j} A ^ {i} Z ^ {j}, \tag {2}
$$

where in mass models $A$ is the total number of nucleons, $Z$ the atomic charge or number of protons, and the binding energy $E$ is parametrized as a polynomial of these variables. The VC–dimension of such polynomial is therefore $h = ( N + 1 ) ^ { 2 }$ .

In the following, a sequence of real valued feed–forward neural networks will be used to validate the statistical learning bounds. For such a network, the VC–dimension $h$ was demonstrated to be $O ( N ) \leq h \leq O ( N ^ { 2 } )$ [14, 15], with $N$ the number of weights.

Using VC–dimension to quantify the data complexity of a model, it is possible to derive the minimum amount of data points needed to reach a generalization error with a certain probability. The generalization error is the difference between the RMSD over the training set $R _ { e m p } ( \alpha )$ , and the hypothetical RMSD over the whole set of applicability $R ( \alpha )$ . In other words, if a model class is bounded and has finite VC–dimension, then it is possible to obtain a polynomial bound on the generalization error that

this model will have, with a given probability, respect to the number of data provided. This paradigm is known as probably approximately correct (PAC) learning [16] and the model is defined as PAC learnable.

The lower bound of data points needed to learn a binary classifier up to a generalization error was demonstrated in [17]. The understanding of this case has been recently improved, demonstrating the exact bound [18]. The bound of the minimum number number of examples needed to reach a given generalization error was demonstrated also for bounded functions in $\mathbb { Z }$ [19], and it has been extended to include noisy data [20]. In this work the bound will be derived from the Hoeffding’s inequality [21]. Therefore, the number of data points $m$ needed to possibly reach a generalization error $\epsilon$ with probability $\delta$ in a PAC learning setting is at least

$$
m \geq \frac {1}{\epsilon} [ \ln (h) + \ln (\frac {1}{\delta}) ], \tag {3}
$$

with $h$ the VC–dimension of the model class under consideration. It is of notice that there is no guarantee that the function $f _ { \alpha }$ with $\alpha \in \Lambda$ with error $\epsilon$ exists, but only a $1 - \delta$ probability. Therefore, in the case of a mass model, there is probability $1 - \delta$ that within our hypothesis space $\Lambda$ exists a function where the training error is $\epsilon$ away from the total error over all nuclei in the whole nuclide chart up including the ones not yet discovered.

Results. Eq. (3) can be now used to estimate the number of data needed for a given precision. That is, to estimate the minimum expected error $\epsilon$ using $m$ data points to train a model with VC-dimension $h$ . The dataset used consists of the 2016 Atomic Mass Evaluation [5] (AME16), considering all nuclei with $N , Z \ge 8$ , including the phenomenological estimates, for a total of 3336 nuclei and associated masses.

At first, to validate the PAC–learning bounds in this context, several feed–forward neural networks with different properties have been trained on some fraction of the AME16 data. The network must take $A , Z$ integer doublets and give back an $\mathbb { R }$ number that represents the binding energy $E$ . Therefore, the network is a model $f _ { \alpha } : \mathbb { N } ^ { 2 } \to \mathbb { R }$ , with $\alpha \in \Lambda$ are the parameters of the network. The network is composed of an input layer with 50 sigmoid nodes, and a single output node to give $E$ . In between a number of hidden nodes and layers with rectified linear unit (reLU) activation function. The number of nodes $n$ and layers $L$ is varied to test different VC– dimensional networks. The number of weights for such a network is $5 1 n + n ^ { L }$ , therefore its VC–dimension is at least $h \geq 5 1 n + n ^ { L }$ . Of particular interest in this letter is the case of 1 hidden layer of 1000 nodes, denoted in the following as $N N 1$ , selected as example with $h \geq 5 2 0 0 0$ . The structure described has been chosen after a hyperparameter optimization for good performance. Rectified linear unit has been chosen for its piecewise linear structure, that guarantees the neural network dimensional-

ity bounds of [14, 15], and for performance aligned with other activation function (cf. supplementary material).

The training loss is evaluated and optimized as RMSD between calculated and experimental binding energies in a training set. The RMSD in Figs. 1, 2 are evaluated on the validation set, using $k -$ fold cross validation technique [22]. This guarantees an assessment of the fitting procedure which reduces the bias in the test/validation selection [23]. The uncertainty related to the RMSD is calculated as standard deviation of different folds. The results presented in Figs. 1, 2 testify to the reliability of PAC learning bounds for this system, the RMSD of models for different neuron number approaches the PAC limit of $\epsilon$ when the network can be trained to reliably describe the system. This result is useful to relate the VC–complexity of a mass model, and the training data provided, with its error. In the following we will use this result to relate VC–complexity of nuclear models with their expected performance.

![](images/7ea61d86fdd799ca9f2b9e98a8267e217e93239ed877ff0d7d16600e2a867af1.jpg)  
FIG. 1. (Color Online) Root mean square deviation of $N N 1$ on the $k$ –fold cross validation of the AME16 dataset (points). Related PAC–learning lower bound of the generalized error $\epsilon$ from (3) (line) in function of the number of data $m$ .

The Weizs¨acker semi–empirical mass formula [24, 25] is one of the first attempts to describe the binding energy of an atomic nucleus in function of powers of the number of nucleons $A$ and protons $Z$ (cf. supplementary material). It is of notice that its fractional contributions are not directly related to Eq. (2). However, it is straightforward to relate this function to a VC–dimension of at least ( $( N = 6 ) + 1 )$ 2, if we consider with no bias all the possible combinations of radius, surface, volume and symmetry terms, or 6 if we consider the parametrization derived with the physical bias.

Density functional theory is used to describe systems composed of many quantum particles [26], and has been an extremely successful model of atomic nuclei [27, 28]. It is based on the Hohenberg-Kohn theorems [29], and the variational principle. That is, the model functional of density $\rho$ , $E [ \rho ( x ) ]$ , will be minimized varying the densities with some Lagrangian constrains (e.g. that the densities contain the correct number of particles) and its minimum will correspond to the exact ground state den-

![](images/5eb52d781f4741ef64e90c47238ce4f9abd12e638dbe658329006c258dca0e2f.jpg)  
FIG. 2. (Color Online) Comparison of error lower bound and results of neural network training with a given number of nodes $n$ and hidden layers, figure (top) and close-up at small error/deviation (bottom). Root mean square deviation of a feedforward neural network on 10–fold cross–validation of the AME16 dataset (points). The neural network consist of 50 input layer, 1 output layer, a number of hidden layers specified by the following color coding: blue (1), green (2), red (4), cyan (8), magenta (16), yellow (32), black (64). Each of the hidden layers has $_ n$ nodes.  corresponding lower bounds from (3) with VC–dimension defined as directly proportional to number of weights (line).

sity and corresponding energy.

The functional $E _ { \alpha } [ \rho ( x ) ]$ is usually a complicated combination of densities, eventually derived from an pseudo– potential [30, 31]. The parameters $\alpha$ of the pseudo– potential are tuned to reproduce physical ground state properties. The densities and properties are calculated through the variational principle. Therefore, the same principle of risk minimization and consequent bounds applies. However, to calculate the exact VC–dimension of a complicated functional is not trivial due to the non– linearity of the operation the functional applies on the density. But a conservative lower bound can be provided considering that,

$$
h (E [ \rho (x) ]) \leq h (E (x)), \tag {4}
$$

this will allow us to calculate a lower bound on the VC– dimension of popular functionals, that in turn determines a lower PAC bound to the generalization error and number of data.

The very popular Skyrme density functional is composed of a contact interaction, with a momentum– dependent term (which translates in derivatives of the densities in the functional) and a density dependent term. The functional can be related to a polynomial expansion

(plus the density dependent term) of the density using (4), reducing to the VC–complexity of a second order polynomial [32] over two dimensions (neutrons and protons) and 8 constrains on the parameters, therefore with dimension at least $h _ { \mathrm { S k y r m e } } \geq 2 ( ( N = 2 ) + 1 ) ^ { 2 } - 8 = 1 0$ . As a title of example, in the case of the Gogny functional [33] the pseudo–potential is composed by two Gaussians with different widths and a density–dependent term. The Gaussian itself has VC–dimension 3, and there are 8 terms for each, making the VC–dimension at least $h _ { \mathrm { G o g n y } } \geq 2 4$ .

Interestingly, theorem 6.8 and following of [7] state that a good rate of convergence can be reached only for smooth functions. Despite being derived from pseudo– potentials with difficult discontinuities (e.g. Skyrme pseudo-potential is a combination of Dirac $\delta$ ) the resulting densities are smooth and therefore can be converged.

<table><tr><td>model</td><td>VC-dim</td><td>RMSD [MeV]</td><td>ε [MeV]</td><td>m</td></tr><tr><td>Weiszacker</td><td>6</td><td>3.41 ± 0.19</td><td>1.09</td><td>36434</td></tr><tr><td></td><td>49</td><td></td><td>1.45</td><td>48395</td></tr><tr><td>NN1</td><td>52000</td><td>4.22 ± 1.06</td><td>2.64</td><td>88076</td></tr><tr><td>Skyrme (UNEDF0)</td><td>10</td><td>1.428 [34]</td><td>1.18</td><td>39343</td></tr><tr><td>Gogny (D1M)</td><td>14</td><td>0.798 [35]</td><td>1.24</td><td>41259</td></tr></table>

TABLE I. Properties of different models to describe nuclear physics masses. The columns represent i) the lower bound on VC–dimension for the given model; ii) RMSD of the referred models; iii) lower bound on the $\epsilon$ error provided by the Hoeffing inequality in PAC–learning considering 3336 homogeneously weighted data points; iv) number of data points $\tilde { m }$ needed to reach a generalization error $\epsilon$ of $1 0 0 \ \mathrm { k e V }$ with 99% probability, a considerable improvement to current bounds. To be noted that the RMSD result for Gogny D1M in [35], contains beyond DFT corrections. RMSD for NN1 is obtained averaging all the results in Fig. 1.

A long standing problem in the creation of nuclear density functionals and mass models is the number and type of data that has to be included in their fitting. This is particularly important in the study of next generation, high order, nuclear density functionals [31, 36]. This work moves towards quantifying the amount of data needed to reach an expected precision in a given mass model. Table I shows a comparison of known mass models RMSD and PAC–learning bounds. The interpretation of Table I comes with several caveats.

The RMSD related to Skyrme UNEDF0 and Gogny D1M are calculated on the data available in the atomic mass evaluation 2003 [37]. Moreover, in the case of Skyrme UNEDF0 only on even–even nuclei. By definition a RMSD on a limited amount of data is the empirical risk and cannot be considered a generalization error, even more so when calculated on data belonging to the training set. The generalization error $\epsilon$ in Table I is derived from the PAC learning bounds considering training on

3336 homogeneously weighted data points, corresponding to the available measured binding energies in AME16 [5]. Most importantly, the objective of such functionals such as UNEDF0 and Gogny D1M is not only to reproduce masses but other properties as well, optimizing a complicated cost function. Physical bias enters in the construction of this cost function, even when the statistical approach is rigorous such as in the UNEDF program [38] and to a greater extent in the definition of other successful models. Sometimes functionals have been developed as interactions, considering a leaving room for beyond mean field correlations in the total energy and other observables in beyond mean field approaches. The RSMD value cited for Gogny D1M especially, includes beyond DFT physics and additional corrections. To be noted also that in some models parameters can be redundant or not sensitive to the observables under consideration. E.g. in the Weiszacker semi–empirical mass formula surface and Coulomb is easy to see parameters are highly correlated [39], and this is also true for DFT models [38, 40]. This, in principle, decreases the VC dimensionality with respect to the observable under consideration, but also the post– and pre–dictive power of the model. Despite these caveats, the close values of the bound $\epsilon$ and the RMSD of state of the art models, testifies to the possibility here discussed of investigating the limits of precision in mass models through statistical learning as defined by PAC learning. Moreover, considering the number of data needed for a significant improvement $\tilde { m } \sim 4 \times 1 0 ^ { 4 }$ according to PAC learning bounds, the relation between $\epsilon$ and RMSD appear robust to the addition of few more data points.

Conclusions. This work is just a first step in the evaluation of statistical learning precision bounds in many– body systems, and further investigations on different models and more complete properties will be required to analyze different many–body models. However, some conclusions can be drawn with better hindsight than before possible. In light of this work on statistical learning theory, the difficulty in further improving mass models to reach a predictive and precise estimate of nuclear masses might not be a shortcoming of some specific model. Instead, the necessary information for a model with predictivity is unlearnable on the basis of masses (or few ground state properties) alone. To increase the performance of these models, especially in biasless, statistically robust next generation functionals, a variety of observables must be included. Eventually, investigating the response to fields will be crucial. This will involve abinitio calculations (that is, interaction including nucleonnucleon scattering data) or unification of structure and reactions.

This work for the first time has investigated the VC– dimension related to a many-body method and its implication regarding the performance that a given model and related training can reach. This work suggests that

many–body methods might not only be judged by their computational complexity, as in the novel field of Hamiltonian complexity [41, 42], but also in terms of their information complexity represented by VC–dimension and PAC learning bounds.

# Acknowledgment

The Quadro P6000 GPU used for this research was donated by the NVIDIA Corporation. This work benefited from discussions with the participants to the workshop “Novel approaches for the description of heavy nuclei” organized at Lund University 19-21 March 2019, with the contribution of Newton Alumni Fellowship of the Royal Society. The source code used will be included in the supplementary material of the publication and publicly released on a git server at a later date.

# SUPPLEMENTARY

# Methods

The adopted geometry of the neural network and training: 50 input nodes, 1 output nodes and training making use of 0.5 dropout of the hidden layers have been obtained as the most consistent values after a tree Parzen estimate hyperparameter optimization (based on Expected Improvement method). Other than sigmoid activation function, also rectified linear unit and softmax have been tried in all the possible combination between input, hidden layers and output. The resulting RMSD was not significantly impacted, testifying to the robustness of the PAC–learnable boundary. Rectified linear unit in the hidden layer has been chosen for simplicity in calculating the VC dimensionality.

The root mean square deviation (RMSD) has been calculated in cross–validation [22]. It consist in dividing the dataset into training and validation exclusive subsets. The procedure is repeated several times with different separation of training and validation dataset guaranteeing a bias-free assessment of the fitting procedure which improves on Bootstrap method [23]. This method consist in:

Divide the training set in a number of equivalent subsets $k$ (usually, but not necessarily, randomly picked). This makes up the $k$ –fold. A popular option, empirically verified to perform well in a variety of situation, is $k = 1 0$ .   
• Train the set on a set composed of $k - 1$ subsets, and validate it on the remaining one.   
• Repeat the training $k$ times, so that training and

validation are considered over all the possible validation sets.

From the RMSD resulting from the combination of training–validation, consider the average and the standard deviation of RMS deviations.

The average RMSD and its deviation will inform on the performance of the model and cost function chosen, and its resilience to modification of the dataset and therefore predictive power. Where otherwise not specified, $k = 1 0$ has been used. Other $k$ –fold choices were also tested, including a “complete cross-validation”, that is a number of folds equal to the number of data.

The Weiszacker model represented in Table 1 of the main article, has been obtained with a RMSD optimization over AME12 database [43] and validated using the AME16 database [5]. The cost function adopted is the modified $\chi ^ { 2 }$ ,

$$
\tilde {\chi} ^ {2} = \sum_ {i} \left(f _ {\alpha} \left(x _ {i}\right) - y _ {i}\right) ^ {2} / \left(\log \left(\Delta y _ {i}\right)\right) ^ {2}, \tag {5}
$$

that has been adjusted in the case measured data $y _ { i }$ have errors $\Delta y _ { i }$ that span different orders of magnitude, as for the case of errors in mass measurements, from [44].

# Mass Model

Neural network approaches to fit to nuclear masses have been tried with specific configurations for neural network structure and propagation strategy [45, 46], obtaining results between 0.7 and 5 MeV of RMSD on masses on specific tests set. The result of this work, obtained with a randomly initialized model that does not introduce bias through the geometry, is 2.54 MeV on the larger AME16 dataset in Figs. 3 and 4. To be noted that the best results in [45] are obtained with the networks with the least number of weights, i.e. lower VC– dimension.

Also models to reproduce HFB calculations [47] and other nuclear properties, such has radii [48], have been recently introduced. Moreover, neural networks have recently emerged as possible method for providing additional corrections and correlations (arguably representing missing shell–effects) to a previously devised mass–model with excellent results [49, 50].

The Weiszacker semi–empirical mass formula has been studied for comparison,

$$
\begin{array}{l} E (A, Z) = a _ {v} A - a _ {s} A ^ {2 / 3} - a _ {C} \frac {Z (Z - 1)}{A ^ {1 / 3}} - a _ {a} \frac {(A - 2 Z) ^ {2}}{A} \\ + a _ {p} \frac {\delta_ {p}}{\sqrt {A}}, \tag {6} \\ \end{array}
$$

where $\delta _ { p }$ is 1 for $A$ and $Z$ even, $0$ for $A$ or $Z$ odd, -1 for $A$ and $Z$ odd. The coefficients of the of the semi–empirical

![](images/18f0b2e0f3e3c82fbf85aff602f9df4a31cd5b3376d0f42f345c452925af8499.jpg)

![](images/8e2a1c3393d4d7bded47309f887513a79bd9a50e7147482fbf2e4c80cc299ff6.jpg)  
FIG. 3. (Color Online) Difference between the neural network postdiction and experimental binding energy in MeV in function of the atomic mass number. The neural network is composed of 1000 rectified linear unit nodes in the hidden layer, is the best resulting out of the 10–fold cross validation over AME12 dataset. Similarly to most mass models, the familiar arches in correspondence of the magic numbers are present.   
FIG. 4. (Color Online) Segre chart of the isotopes with the difference between the neural network postdiction and experimental result in MeV. The neural network is composed of 1000 rectified linear unit nodes in the hidden layer, is the best resulting out of the 10–fold cross validation over AME12 dataset. That results in a root mean square deviation on the AME16 dataset of 2.54 MeV.

model mass formula, consist in the well known volume $a _ { v }$ , surface $a _ { s }$ , Coulomb $a _ { C }$ , asymmetry $a _ { a }$ and pairing $a _ { p }$ terms. The parameter regarding the results used in Table 1 of the main article are reported here in Table II, with a striking resemblance in quantity and uncertainties with [39] (results obtained independently and with different fitting procedures). The related uncertainties have been computed with the covariance matrix calculated as inverse of the Hessian, which is composed by derivatives of the cost function respect to the free parameters. By

linear approximation it is possible to estimate errors related to a parameter or observable [31, 44, 51]

$$
a _ {v} = 1 5. 4 0 \pm 0. 0 1 4
$$

$$
a _ {s} = 1 6. 7 1 \pm 0. 0 4 2
$$

$$
a _ {C} = 0. 7 0 1 \pm 0. 0 0 1
$$

$$
a _ {a} = 2 2. 5 6 \pm 0. 0 3 7
$$

$$
a _ {p} = 1 1. 8 8 \pm 0. 8 2 3
$$

TABLE II. Coefficients in MeV of the semi–empirical mass formula (6) obtained fitting AME12. Notice the uncertainties related to the different quantities, especially concerning pairing that testifies the softness of the regression of Weizsacker mass formula respect to pairing, that is also the reason why different formulations are used for this term.

Support vector machine [52] obtained interesting results of accuracy and would be also an interesting object of study in light of PAC learning bounds which are well established [7].

[1] W. Nazarewicz, Nature Physics 14, 537 (2018).   
[2] S. ˚Aberg, Nature 417, 499 (2002).   
[3] O. Bohigas and P. Leboeuf, Phys. Rev. Lett. 88, 092502 (2002).   
[4] J. Barea, A. Frank, J. G. Hirsch., and P. V. Isacker, Phys. Rev. Lett. 94, 102501 (2005).   
[5] M. Wang, G. Audi, F. Kondev, W. Huang, S. Naimi, and X. Xu, Chinese Physics C 41, 030003 (2017).   
[6] V. N. Vapnik, IEEE Transactions on Neural Networks 10, 988 (1999).   
[7] V. N. Vapnik, The Nature of Statistical Learning Theory (Springer-Verlag, Berlin, Heidelberg, 1995).   
[8] V. Vapnik, in Advances in neural information processing systems (1992) pp. 831–838.   
[9] A. Blumer, A. Ehrenfeucht, D. Haussler, and M. K. Warmuth, Information Processing Letters 24, 377 (1987).   
[10] P. Domingos, Data Mining and Knowledge Discovery 3, 409 (1999).   
[11] J. Shawe-Taylor, P. L. Bartlett, R. C. Williamson, and M. Anthony, IEEE Transactions on Information Theory 44, 1926 (1998).   
[12] V. Vapnik and A. Chervonenkis, Theory of Probability & Its Applications 16, 264 (1971), https://doi.org/10.1137/1116025.   
[13] T. Hastie, R. Tibshirani, and J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Second Edition, Springer Series in Statistics (Springer New York, 2009).   
[14] W. Maass, in Handbook of Brain Theory and Neural Networks, edited by M. A. Arbib (MIT Press, 1995) pp. 1000–1003.   
[15] P. Koiran and E. D. Sontag, in Advances in neural information processing systems (1996) pp. 197–203.   
[16] L. G. Valiant, Commun. ACM 27, 1134 (1984).   
[17] A. Ehrenfeucht, D. Haussler, M. Kearns, and L. Valiant, Information and Computation 82, 247 (1989).   
[18] A. Kontorovich and I. Pinelis, CoRR abs/1606.08920

(2016), to be published in annals of statistics, arXiv:1606.08920.   
[19] D. Haussler, Information and Computation 100, 78 (1992).   
[20] P. L. Bartlett, P. M. Long, and R. C. Williamson, Journal of Computer and System Sciences 52, 434 (1996).   
[21] W. Hoeffding, Journal of the American Statistical Association 58, 13 (1963), https://www.tandfonline.com/doi/pdf/10.1080/01621459   
[22] P. A. Lachenbruch and M. R. Mickey, Technometrics 10, 1 (1968).   
[23] B. Efron, Journal of the American Statistical Association 78, 316 (1983).   
[24] C. F. v. Weizs¨acker, Zeitschrift f¨ur Physik 96, 431 (1935).   
[25] H. A. Bethe and R. F. Bacher, Rev. Mod. Phys. 8, 82 (1936).   
[26] D. S. Sholl and J. A. Steckel, Density Functional Theory: A Practical Introduction (John Wiley and sons, 2009).   
[27] M. Bender, P.-H. Heenen, and P.-G. Reinhard, Rev. Mod. Phys. 75, 121 (2003).   
[28] P. Ring and P. Schuck, The Nuclear Many–Body Problem (Springer, Berlin, 1980).   
[29] P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964).   
[30] E. Perli´nska, S. G. Rohozi´nski, J. Dobaczewski, and W. Nazarewicz, Phys. Rev. C 69, 014316 (2004).   
[31] K. Bennaceur, A. Idini, J. Dobaczewski, P. Dobaczewski, M. Kortelainen, and F. Raimondi, Journal of Physics G: Nuclear and Particle Physics 44, 045106 (2017).   
[32] First order derivatives go to 1, and other terms cancel.   
[33] J. Decharg´e and D. Gogny, Phys. Rev. C 21, 1568 (1980).   
[34] M. Kortelainen, J. McDonnell, W. Nazarewicz, E. Olsen, P.-G. Reinhard, J. Sarich, N. Schunck, S. M. Wild, D. Davesne, J. Erler, and A. Pastore, Phys. Rev. C 89, 054314 (2014).   
[35] S. Goriely, S. Hilaire, M. Girod, and S. P´eru, Phys. Rev. Lett. 102, 242501 (2009).   
[36] D. Davesne, A. Pastore, and J. Navarro, Journal of Physics G: Nuclear and Particle Physics 40, 095104

(2013).   
[37] A. Wapstra, G. Audi, and C. Thibault, Nuclear Physics A 729, 129 (2003), the 2003 NUBASE and Atomic Mass Evaluations.   
[38] M. Kortelainen, T. Lesinski, J. Mor´e, W. Nazarewicz, J. Sarich, N. Schunck, M. V. Stoitsov, and S. Wild, Phys. Rev. C 82, 024313 (2010).   
[39] A. Pastore, Journal of Physics G: Nuclear and Particle 63.10500830.Physics (2019).   
[40] T. Haverinen and M. Kortelainen, Journal of Physics G: Nuclear and Particle Physics 44, 044008 (2017).   
[41] J. D. Whitfield, P. J. Love, and A. Aspuru-Guzik, Physical Chemistry Chemical Physics 15, 397 (2013).   
[42] S. Gharibian, Y. Huang, Z. Landau, S. W. Shin, et al., Foundations and TrendsR in Theoretical Computer Science 10, 159 (2015).   
[43] G. Audi, F. G. Kondev, M. Wang, B. Pfeiffer, X. Sun, J. Blachot, and M. MacCormick, Chin.Phys.C 36, 1157 (2012).   
[44] J. Dobaczewski, W. Nazarewicz, and P.-G. Reinhard, Journal of Physics G: Nuclear and Particle Physics 41, 074001 (2014).   
[45] K. Gernoth, J. Clark, J. Prater, and H. Bohr, Physics Letters B 300, 1 (1993).   
[46] S. Athanassopoulos, E. Mavrommatis, K. Gernoth, and J. Clark, Nuclear Physics A 743, 222 (2004).   
[47] T. Bayram, S. Akkoyun, and S. O. Kara, Annals of Nuclear Energy 63, 172 (2014).   
[48] S. Akkoyun, T. Bayram, S. O. Kara, and A. Sinan, Journal of Physics G: Nuclear and Particle Physics 40, 055106 (2013).   
[49] R. Utama and J. Piekarewicz, Physical Review C 96, 044308 (2017).   
[50] Z. Niu and H. Liang, Physics Letters B 778, 48 (2018).   
[51] J. Toivanen, J. Dobaczewski, M. Kortelainen, and K. Mizuyama, Phys. Rev. C 78, 034306 (2008).   
[52] H. Li, J. Clark, E. Mavrommatis, S. Athanassopoulos, and K. Gernoth, Condensed Matter Theories, Vol. 20.