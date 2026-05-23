# Analysis of a Skyrme energy density functional with deep learning

N. Hizawa,1 K. Hagino,1 and K. Yoshida ${ } ^ { 2 , 3 }$

$^ { 1 }$ Department of Physics, Kyoto University, Kyoto 606-8502, Japan

$^ 2$ Research Center for Nuclear Physics, Osaka University, Ibaraki, Osaka 567-0047 Japan   
$^ 3$ RIKEN Nishina Center for Accelerator-Based Science, Wako, Saitama 351-0198, Japan

Over the past decade, machine learning has been successfully applied in various fields of science. In this study, we employ a deep learning method to analyze a Skyrme energy density functional (Skyrme-EDF), that is a Kohn-Sham type functional commonly used in nuclear physics. Our goal is to construct an orbital-free functional that reproduces the results of the Skyrme-EDF. To this end, we first compute energies and densities of a nucleus with the Skyrme Kohn-Sham + Bardeen-Cooper-Schrieffer method by introducing a set of external fields. Those are then used as training data for deep learning to construct a functional which depends only on the density distribution. Applying this scheme to the $^ { 2 4 }$ Mg nucleus with two distinct random external fields, we successfully obtain a new functional which reproduces the binding energy of the original Skyrme-EDF with an accuracy of about 0.04 MeV. The rate at which the neural network outputs the energy for a given density is about $1 0 ^ { 5 } – 1 0 ^ { 6 }$ times faster than the Kohn-Sham scheme, demonstrating a promising potential for applications to heavy and superheavy nuclei, including the dynamics of fission.

# I. INTRODUCTION

Recent progress of deep learning is quite remarkable. It has actually gained popularity in various fields of science and technology, such as natural language processing, computer vision, and speech recognition [1–5]. In several fields of physics, such as condensed matter physics, a multitude of ideas to utilize machine learning are arising. For instance, in Ref. [6], an energy density functional (EDF) for electron systems that depends solely on an electron number density was constructed using the method developed in Ref. [7], in which an attempt was made with a neural network to predict the solution of a two-dimensional Schr¨odinger equation in a random potential. Other applications have already existed also for a variety of problems, including those in spin systems [8] and superconducting systems [9].

In contrast, an application of deep learning to nuclear physics has still been in its early stage [10–25]. We mention that nuclear physics continues to face numerous unresolved challenges that call for innovative solutions, including a description of large amplitude collective motions. Such problems may be solved efficiently by applying the machine learning techniques, developed in other fields of physics.

In particular, the recent application of deep learning to the Kohn-Sham type DFT [6] mentioned above could be readlily applied also to nuclear physics. In nuclear physics, phenomenological models for a functional have often been employed [26]. The resultant Kohn-Sham type energy density functional (KS-EDF) is not an explicit functional of the particle number density only, but is parameterized together with other local densities, such as the kinetic energy density, the spin-orbit density, and the pair density when considering explicitly the nucleonic superfluidity. To calculate observables using the KS-EDF, such as the binding energy of a nucleus, one needs to solve a self-consistent differential equation of the same form as that in the mean-field theory many times, which is

computationally expensive especially for heavy systems. Therefore, it is desirable to develop an orbital-free EDF (OF-EDF) theory that does not depend on Kohn-Sham orbitals. Deep learning can be a powerful tool for that purpose [6]. Such theory will be based on a functional that depends sorely on the particle number density. Notice that this is totally consistent with the original philosophy of the density functional theory (DFT).

The aim of this paper is to apply the method developed in Ref. [6] to a nuclear system and construct a deeplearning-based nuclear OF-EDF that reproduces results of the Skyrme-EDF. In applying the method of Ref. [6] to a nuclear system, one has to take into account several aspects that make nuclear systems different from electron systems. One obvious difference is that a nucleus is a self-bound attractive system. In a electron system without phonons, the only interaction between electrons is the repulsive Coulomb force, which causes two electrons to distribute as far as possible. In marked contrast, nucleons tend to get closer to each other due to a short-ranged attractive nuclear force, and thus the mechanism which determines the density distribution is quite different between electron and nucleon systems [27]. In addition, for electron systems, the KS-EDFs, which are inspired by the Hartree-Fock method, works well in general. On the other hand, in nuclear systems, superfluidity plays a crucial role in open-shell nuclei, and observables are better explained using a KS-EDF that is inspired by the Hartree-Fock-Bardeen-Cooper-Schrieffer (BCS) or Hartree-Fock-Bogoliubov method rather than by the Hartree-Fock method. This leads to a technical difference in that a nuclear KS-EDF depends also on the pair density. It will be intriguing to investigate how well the deep learning method works in such attractiondominated nuclear systems.

The paper is organized as follows. In Sec. II, we introduce the KS-EDF which we employ, and define a protocol for deep learning. We also discuss how to generate data sets to train neural networks. In Sec. III, we carry out

the deep learning for the $^ { 2 4 }$ Mg nucleus and discuss how well the data sets can be learned. We then summarize the paper in Sec. IV and discuss future perspectives.

# II. FORMULATION

# A. Skyrme EDF

We first introduce a Kohn-Sham type energy density functional (KS-EDF) for training on a neural network. Throughout this study, we consistently employ the following Skyrme-type EDF [28]:

$$
E _ {\text {t o t}} = E _ {\text {k i n}} + E _ {\text {i n t}} + E _ {\text {p a i r}} + E _ {\text {C o M}}, \tag {1}
$$

with

$$
E _ {\mathrm {k i n}} [ \tau ] = \frac {\hbar^ {2}}{2 m} \left(1 - \frac {1}{A}\right) \sum_ {q} \int d ^ {3} r \tau_ {q} (\boldsymbol {r}), \tag {2}
$$

$$
\begin{array}{l} E _ {\mathrm {i n t}} [ \rho , \tau , \boldsymbol {J} ] = \int d ^ {3} r \left\{\frac {b _ {0}}{2} \rho^ {2} - \frac {b _ {0} ^ {\prime}}{2} \sum_ {q} \rho_ {q} ^ {2} \right. \\ + \frac {b _ {3}}{3} \rho^ {\alpha + 2} - \frac {b _ {3} ^ {\prime}}{3} \rho^ {\alpha} \sum_ {q} \rho_ {q} ^ {2} + b _ {1} \rho \tau - b _ {1} ^ {\prime} \sum_ {q} \rho_ {q} \tau_ {q} \\ - \frac {b _ {2}}{2} \rho \nabla^ {2} \rho + \frac {b _ {2} ^ {\prime}}{2} \sum_ {q} \rho_ {q} \nabla^ {2} \rho_ {q} \\ \left. - b _ {4} \rho \nabla \cdot \boldsymbol {J} - b _ {4} ^ {\prime} \sum_ {q} \rho_ {q} \nabla \cdot \boldsymbol {J} _ {q} \right\}, \tag {3} \\ \end{array}
$$

$$
E _ {\text {p a i r}} [ \rho , \tilde {\rho} ] = \sum_ {q} \frac {V _ {0} ^ {(q)}}{4} \int d ^ {3} r \left\{1 - \left(\frac {\rho}{\rho_ {0}}\right) ^ {\gamma} \right\} \tilde {\rho} _ {q} ^ {2}, \tag {4}
$$

and

$$
E _ {\mathrm {C o M}} [ \rho ] = \frac {C}{2} \left(\int d ^ {3} r z \rho (\boldsymbol {r})\right) ^ {2}, \tag {5}
$$

where $m$ is the nucleon mass and $A$ is the mass number of a nucleus. $E _ { \mathrm { k i n } }$ , $E _ { \mathrm { i n t } }$ , $E _ { \mathrm { p a i r } }$ , and $E _ { \mathrm { C o M } }$ are the kinetic energy, the interaction energy, the pairing energy, and a cost function for the center-of-mass, respectively. $\rho , \tau , J$ , and $\ddot { \rho }$ are the particle number density, the kinetic density, the spin density, and the pair density, respectively, in which the subscript $q$ refers to neutron or proton. Those are defined as

$$
\rho (\boldsymbol {r}) = 2 \sum_ {q} \sum_ {k > 0} v _ {q, k} ^ {2} \left| \varphi_ {q, k} (\boldsymbol {r}) \right| ^ {2}, \tag {6}
$$

$$
\tau (\boldsymbol {r}) = 2 \sum_ {q} \sum_ {k > 0} v _ {q, k} ^ {2} | \nabla \varphi_ {q, k} (\boldsymbol {r}) | ^ {2}, \tag {7}
$$

$$
\boldsymbol {J} (\boldsymbol {r}) = 2 \sum_ {q} \sum_ {k > 0} v _ {q, k} ^ {2} \varphi_ {q, k} ^ {*} (\boldsymbol {r}) (- i \nabla \times \boldsymbol {\sigma}) \varphi_ {q, k} (\boldsymbol {r}), \tag {8}
$$

$$
\tilde {\rho} (\boldsymbol {r}) = - 2 \sum_ {q} \sum_ {k > 0} u _ {q, k} v _ {q, k} | \varphi_ {q, k} (\boldsymbol {r}) | ^ {2}, \tag {9}
$$

where $\varphi _ { q , k } ( \pmb { r } )$ is the $k$ -th Kohn-Sham orbrbital in a spinor form with isospin $q$ , and v2 $v _ { q , k } ^ { 2 } = 1 - u _ { q , k } ^ { 2 }$ is the occupation probability for the $k$ -th orbital. Notice that we take the BCS approximation for the treatment of the pairing correlation.

In the interaction part of the functional, $b _ { i }$ and $b _ { i } ^ { \prime }$ ( $i =$ 1–4) as well as $\alpha$ are the Skyrme parameters. In this paper, we use the SLy4 parameter set [29] for these parameters. For simplicity, we ignore the Coulomb interaction, even though the entire Coulomb interaction term can be explicitly described as a functional of the proton number density if the Slater approximation is introduced to the exchange term.

For the pairing part, we employ a surface-type functinal of the Density-Dependent Delta-Interaction (DDDI) [30], which contains the parameters $V _ { 0 } ^ { ( q ) } , \rho _ { 0 }$ , and $\gamma$ . In this study, we take $\gamma ~ = ~ 1$ and $\rho _ { 0 } ~ = ~ 0 . 1 6 \mathrm { { f m } ^ { - 3 } }$ , and determine V (q) $V _ { 0 } ^ { ( q ) }$ so that the average pairing gap coin-√ cides with the empirical pairing gap, $\Delta _ { q } = 1 2 / \sqrt { A }$ MeV [28, 31]. The zero-range pairing interaction has to be supplemented with an energy cut-off. In this paper, the sharp cut-off energy of 60 MeV is introduced to the single particle energy of the Kohn-Sham orbitals. The resultant strengths for the pairing are $V _ { 0 } ^ { ( n ) } = V _ { 0 } ^ { ( p ) } = - 6 8 3 . 3 4 4$ MeV fm3.

In addition to the ordinal Skyrme EDF, we introduce a functional $E _ { \mathrm { C o M } } [ \rho ]$ to fix the center-of-mass position in the $z$ direction. This is necessary as we introduce external fields (see Sec. II C below) to generate various density distributions. By fixing the center-of-mass position, one can prevent a nucleus from localizing around the edges of the box, which is useful to generate various deformed states in a small box. In this study, we take $0 . 6 2 5 \mathrm { M e V / f m ^ { 2 } }$ for the value of $C$ .

In this paper, we consider only the $^ { 2 4 }$ Mg nucleus. This choice of a nucleus is convenient, as this nucleus has equal numbers of protons and neutrons, and thus the proton and the neutron densities coincide to each other when the Coulomb interaction is ignored. Furthermore, we impose the axial symmetry and the time-reversal symmetry on the system, enabling the local densities to be expressed in the cylindrical coordinates $( r , z )$ [32]. Notice that Ref. [6] also used a two-dimensional EDF for electron systems. With these simplifications, in principle, the EDF of the system should be able to be expressed solely with the nucleon number density $\rho ( r , z )$ , which can be considered as a monochromatic image.

We solve the Kohn-Sham equations for this EDF by introducing various external fields to obtain a set of ground state energies and nucleon number densities. The explcit forms of the external fields are specified in Sec. II C. We solve the Khon-Sham equations by discretizing the real space, with the mesh size of 0.8 fm in both the $r$ and $z$ directions. We take 10 grid points in the $r$ direction and 20 points in the $z$ -direction, with which the density $\rho ( r , z )$ can be considered as a $1 0 \times 2 0$ -dimensional vector in our calculations. We choose the box boundary condi-

tion and include the $z$ -component of angular momentum up to $9 / 2$ .

# B. Neural network

In this paper, we carry out a regression analysis of $E ~ = ~ E [ \rho ]$ using a set of the particle number density and the energy $D = \{ E ^ { ( i ) } , \rho ^ { ( i ) } \} _ { i }$ generated by the KS-DFT. To this end, we utilize a neural network with fullyconnected layers for the fitting function. The fundamental structure of a neural network involves a repetition of linear and nonlinear transformations on the input vector; fully-connected layers signify that all the neurons in the previous layer are connected to all the neutrons in the next layer.

We mention that neural networks composed solely of fully-connected layers may encounter an issue of an excessive number of parameters when the dimension of an input vector is large. To avoid this problem, a convolutional neural network (CNN) is often employed, which has demonstrated a remarkable success in the field of computer vision [33, 34]. In fact, in the previous application of deep learning to KS-DFT [6], the input size of a vector has as large as $2 5 6 \times 2 5 6$ dimension, and thus the CNN was employed. However, the dimension of our studies in this paper is much smaller, with $1 0 \times 2 0$ dimension. Therefore, we do not need to introduce the CNN, and a simpler neural network consisting of the fully-connected layers, as depicted in Fig. 1, is employed in this study (see the caption for the details).

We use the Adam optimizer [35], which has three tunable parameters. Among the three parameters, we set a learning rate to be $1 0 ^ { - 4 }$ and the others to be default value of the Keras API [36]. The batch size is 128, namely we divide training data into subsets, each of which contains 128 components. In each update of the fitting parameters, we do it only within each subset to minimize a loss function, for which we take a mean square loss function. To avoid the problem of overfitting, we adopt the early stopping strategy and stop the learning at the 500th epoch. We decrease the learning rate sequentially to $1 0 ^ { - 5 }$ (at epoch = 101), $1 0 ^ { - 6 }$ (at epoch = 201), $5 . 0 \times 1 0 ^ { - 7 }$ (at epoch = 301), and $1 0 ^ { - 7 }$ (at epoch = 401).

# C. External fields

For a given EDF, one can make a correspondence between the particle number density and the energy of the ground state for a specific external field. This property will be used to construct a data set to be trained for an OF-EDF. For this purpose, a diverse range of external fields is required. In this subsection, we introduce two methods to generate the external potentials used in this study. The basic idea of these methods is adapted from the previous studies [6, 7] on two-dimensional systems, but we modify them for the axial-symmetric systems.

![](images/eaf37de8bac1111cd268beacaa9c83299d74f70682cade066758ec54f8fa12ac.jpg)  
FIG. 1. A neural network employed in this work to learn the Skyrme-EDF, $E [ \rho ]$ . It consists of 10 hidden layers, all of which are fully connected. Their activation functions are the ReLU, and the sigmoid activation function is employed for the output layer. The number of neurons in each layer is listed below the layers.

# 1. Simple Harmonic Oscillators (SHO)

The first method is to use external fields based on a Simple Harmonic Oscillator (SHO). As the name implies, this is a deformed harmonic oscillator potential shifted in the $z$ -direction:

$$
v _ {\mathrm {S H O}} ^ {(i)} (r, z) = \frac {1}{2} k _ {r} ^ {(i)} r ^ {2} + \frac {1}{2} k _ {z} ^ {(i)} \left(z - z _ {0} ^ {(i)}\right) ^ {2}. \tag {10}
$$

The parameters in the range of $\begin{array} { r l r l } { 0 } & { { } \le } & { k _ { r } , k _ { z } } & { { } \le } \end{array}$ 1.1 MeV/fm2, and $- 1 . 6 \mathrm { f m } \le z _ { 0 } \le 1 . 6 $ fm in the potential are generated from uniform random parameters

The SHO potentials would be able to encompass only a small portion of a domain of the external fields to be used in the Skyrme-EDF. However, for practical calculations, only a limited variety of external fields, such as a quadrupole moment, has frequently been utilized, if a constrained field is regarded as an external field in a broad sense. It is therefore still useful to examine the effectiveness of the learning process with the SHO potentials.

# 2. Random Potentials (RND)

As the second method, we introduce a Random Potential (RND). This is a highly random potential with many random numbers:

$$
v _ {\mathrm {S H O}} ^ {(i)} (r, z) = m (r, z) \times \operatorname {s r} ^ {(i)} (r, z), \tag {11}
$$

where $m ( r , z )$ and $\mathrm { s r } ^ { ( i ) } ( r , z )$ are defined as,

$$
m (r, z) = e ^ {- 4. 0 \max  \left\{0, \sqrt {r ^ {2} + z ^ {2}} - r _ {0} \right\} ^ {2} / r _ {0} ^ {2}}, \tag {12}
$$

![](images/4428f7bd319cfbc1297f427f858a282c888fde8cea1f0437e9130435976cefa4.jpg)

![](images/d398f3e68bf8c9161d38da21e8229249ff8233d65e60b81352c017b24e8256a0.jpg)

![](images/16ab5ffa0d35c1330529312e93d73ca800072f10230c61cfcc92be08ea140d42.jpg)

![](images/1566bed1713c07886d395e8f503e418be88bc18dc3f2c07381cc36914ad6781b.jpg)  
energy/MeV   
FIG. 2. Histograms for the results of the Skyrme EDF calculations with 250,000 different external fields based on the SHO (the top panels) and the RND (the bottom panels) fields. The left and right panels show the binding energy and the pairing energy in units MeV, respectively. It can be observed that the structure in the shape of the histograms is washed out to a large extent for the RND external fields, which are more random than the SHO cases.

and

$$
\operatorname {s r} ^ {(i)} (r, z) = \sum_ {r ^ {\prime}, z ^ {\prime}} s ^ {(i)} \left(r, z; r ^ {\prime}, z ^ {\prime}\right) \operatorname {r n d} ^ {(i)} \left(r ^ {\prime}, z ^ {\prime}\right), \tag {13}
$$

respectively, with

$$
s ^ {(i)} (r, z; r ^ {\prime}, z ^ {\prime}) = e ^ {- \left\{\left(r - r ^ {\prime}\right) ^ {2} + \left(z - z ^ {\prime}\right) ^ {2} \right\} / \mu_ {2} ^ {(i)} \left(r ^ {\prime}, z ^ {\prime}\right)}. \tag {14}
$$

The meaning of $\mathrm { r n d } ^ { ( i ) } ( r , z )$ in Eq. (13) and $\mu _ { 2 } ^ { ( i ) } ( r , z )$ in Eq. (14) is as follows. First, for each grid point $( r , z )$ , a random number within the range of $[ v _ { \mathrm { m i n } } , v _ { \mathrm { m a x } } ]$ is generated and labeled as $\mathrm { r n d } ^ { ( i ) } ( r , z )$ . Since the potential with those random numbers is too irregular to be used as a potential, it is smoothed with a Gaussian filter, denoted as $s ^ { ( i ) }$ , as in Eq. (13). At this stage, the square of the Gaussian width $\mu _ { 2 } ^ { ( i ) } ( r , z )$ in Eq. (14) is randomly generated within the range of $[ \mu _ { \mathrm { 2 m i n } } , \mu _ { \mathrm { 2 m a x } } ]$ to prevent the external field from acquiring scale information due to the standard deviation of the Gaussian. Finally, a mask defined by Eq.(12) is applied in Eq.(11) to circumvent a numerical instability caused by a reduction of the

external field near the boundary. In this study, we take $r _ { 0 } = 1 . 4 \times 1 . 2 A ^ { 1 / 3 }$ fm, $v _ { \operatorname* { m i n } } = - 1 . 1$ MeV, $v _ { \mathrm { m a x } } = 1 . 1$ MeV, $\mu _ { 2 \mathrm { { m i n } } } = 0 . 8 ~ \mathrm { f m ^ { 2 } }$ , and $\mu _ { 2 \mathrm { { m a x } } } = 1 . 2 ~ \mathrm { { f m ^ { 2 } } }$ .

In Refs. [6, 7], random $\{ 0 , 1 \}$ binary data were utilized for $\mathrm { r n d } ^ { ( i ) } ( r , z )$ . For electronic systems, such a choice would be plausible because the potential primarily arises from the Coulomb potential due to a nucleus. On the other hand, in nuclear systems, it would be a highly non-trivial question to ask which potential is useful to describe static and dynamical properties of atomic nuclei. While many calculations employ a phenomenological deformed mean-field potential with e.g., a qudrupole deformation to study deformed nuclei, it is not obvious whether such choice is optimal. Therefore, in this study, we use random real numbers for $\mathrm { r n d } ^ { ( i ) } ( r , z )$ to generate more diverse external fields than in the previous studies. Additionally, since the constraint on the center-of-mass position is included in the definition of the KS-EDF (1), a different mask function $m$ from that in the previous studies is also introduced.

# III. RESULTS

# A. Generation of a dataset

Let us now apply the deep learning protocol discussed in the previous section to the Skyrme EDF. We first prepare 250,000 data sets for each of the SHO and the RND external fields. For each calculation, the outputs are i) the nucleon number density $\rho$ , ii) the kinetic energy $E _ { \mathrm { k i n } }$ , iii) the interaction energy $E _ { \mathrm { i n t } }$ , iv) the pairing energy $E _ { \mathrm { p a i r } }$ , and v) the energy for the external field $\boldsymbol { E } _ { \mathrm { e x } }$ . The binding energy $E _ { \mathrm { b i n } }$ is also computed as a sum of $E _ { \mathrm { k i n } }$ , $E _ { \mathrm { i n t } }$ , and $E _ { \mathrm { p a i r } }$ , as $E _ { \mathrm { b i n } } = E _ { \mathrm { k i n } } + E _ { \mathrm { i n t } } + E _ { \mathrm { p a i r } }$ . Figure 2 displays the distribution of $E _ { \mathrm { b i n } }$ and $E _ { \mathrm { p a i r } }$ for each of the SHO and the RND external fields. The distributions of the other components of the energy are summarized in Appendix A (see Fig. 8). In order to use these data for deep learning, we reject those outside the regions given in Tab. I. From the remaining data, we select 200,000 data for training. Out of those 200,000 data, we adopt $9 0 \ \%$ of them for training data, while the rest for test data, which are not used for training.

TABLE I. The lower and the upper cut-off energies, in units MeV, for the two different types of the external fields, SHO and RND. For each leraning, only the data within the intervals are employed. The value of cutoffs are determined so that approximately all the data shown in Figs. 2 and 8 can be included.   

<table><tr><td></td><td colspan="2">SHO</td><td colspan="2">RND</td></tr><tr><td>type</td><td>lower</td><td>upper</td><td>lower</td><td>upper</td></tr><tr><td>Ebin</td><td>-∞</td><td>-217.5</td><td>-∞</td><td>-217.5</td></tr><tr><td>Ekin</td><td>395.0</td><td>450.0</td><td>360.0</td><td>420.0</td></tr><tr><td>Eint</td><td>-650.0</td><td>-600.0</td><td>-630.0</td><td>-550.0</td></tr><tr><td>Epair</td><td>-22.0</td><td>+∞</td><td>-35.0</td><td>+∞</td></tr><tr><td>Ex</td><td>-∞</td><td>120.0</td><td>-70.0</td><td>50.0</td></tr></table>

$$
\mathbf {B}. \quad \rho \rightarrow E [ \rho ]
$$

We first discuss the results for each energy as an objective variable with the nucleon number density as an explanatory variable. In other words, we construct the OF-EDF, which yields the energies from a density distribution as an input. In DFT, apart from an external field, there would be an ambiguity to divide the functional into components: $E _ { \mathrm { k i n } } , E _ { \mathrm { i n t } }$ , and $E _ { \mathrm { p a i r } }$ themselves may not have strict physical meanings. Nevertheless, these components can be employed as indicators at least for qualitative discussions, and we thus follow Ref. [6] to examine the subparts of the EDF. In particular, it is interesting to investigate the pairing energy $E _ { \mathrm { p a i r } }$ , as it qualitatively verifies whether we can learn the effect of superfluidity, or the pair density, with deep learning. Notice that this was not addressed in the previous study in Ref. [6].

The top panels in Fig. 3 compare the results of the Kohn-Sham method (the horizontal axes) with the neural network predictions (the vertical axes) for the test data with the RND external fields not used in learning. The results with the SHO external fields (see the third top panels) are found to be more accurate 2. Figure 3 shows only $E _ { \mathrm { b i n } }$ , $E _ { \mathrm { p a i r } }$ , and $E _ { \mathrm { e x } }$ , while the other components of the energy are displayed in Appendix A (see Fig. 9). If the learning is perfect, the distribution should be diagonal: actually this is almost the case for all the energies except for the energy of the external fields plotted in the rightmost figure.

We have found that the large error in $E _ { \mathrm { e x } }$ was not improved by changing the learning method, such as a CNN model (see Appendix). This may be due to the fact that the particle number densities with different external fields tend to have a similar shape because of the saturation property, which results in an information loss in the process of compressing information on the external fields into the density distributions. Of course, according to the principle of DFT, ideally there should be no loss of information because there is a bijection between an appropriately defined density and an external field. However, in actual calculations, information on the detailed structure of external fields may be lost due to several numerical errors such as rounding errors, finite difference errors, and errors associated with a convergence criterion in self-consistent calculations. It is then natural that the prediction error becomes large when one attempts to recover the external field information from such a density distribution. The inaccuracy in predicting the energy of external fields was reported also in the previous study [6], but the inaccuracy seems more pronounced in atomic nuclei, which are systems with an attractive interaction. As we will show in the next subsection, this problem can be improved by using the external fields as explanatory variables.

To quantitatively evaluate the errors, we calculate the mean absolute error (MAE) for each learning, which are summarized in Tab. II. It is remarkable that the MAE for the binding energy is as small as 0.0051 MeV for the SHO external fields and 0.0433 MeV for the RND external fields, which are much more accurate than the accuracy required e.g., for a fission barrier of heavy nuclei as well as for nuclear masses. For instance, for the latter, the accuracy of 100 keV is required for the r-process studies [37]. The MAE for the pairing energy is 0.0233 MeV for the SHO and 0.1567 MeV for the RND. These values indicate that the particle number density predicts well the contribution of the pairing correlation, even though the error is slightly larger than that for the binding energy.

Finally, let us discuss a computational time. For the 24Mg nucleus, it typically takes about a minute to solve

![](images/bfe7dd55c0c7f414b2e662941417be66ad8a134a26fd297d274f8bf76a241dc0.jpg)

![](images/5fbf62117c3a79ecda44c2c59ba5a6e4d65f44dfccb600d24a872ee95450884d.jpg)

![](images/a426a5c5ec5355fd17ecfa8d1373c830e3142e61e47e38981dd971135d190825.jpg)

![](images/29c3204864fd5d3db880e6e8cb4ecab82bd08b5fdfe02f5ba0bb60392820003c.jpg)

![](images/6876fa3cd21c123e6447c892eea5debaeb79e08dbf270194fc0178e29ce29903.jpg)

![](images/dc8532a99c87ef6b0e4091a664eb24516eb23c572a2b030aa5cabfba3b062552.jpg)

![](images/ebd4f82fa6c443288826f1a481aa9bb7ffea0c4238a268ebdbc4e11c2900be13.jpg)

![](images/bef292f3495a07897299f596359a9d8feaabe40fe219f8ba44be6666ca4cd360.jpg)

![](images/7ee8f377a4f4bf1ab5a1b24171039e9f601cbf0fe79c44d0d87cfd91ca4dcefb.jpg)

![](images/f3800acfcd81e636b05ea068ce9d8cbe19fb784620a5c3f2f0b79b98af193da7.jpg)

![](images/4521df5596b15bd23f6309d273924c9d59d6cc4024433abb8d71c745bae4caf3.jpg)

![](images/160ad713537275f697cb414a838ee33e52ab5a1e1519dc7064c5d6014cbacea9.jpg)  
Kohn-Sham energy /MeV   
FIG. 3. Comparisons of the Kohn-Sham method (the horizontal axes) and the predicted results from the neural network (the vertical axis) for $E [ \rho ]$ and $E [ v ]$ for the RND (the top panels) and SHO (the bottom panels) external fields, all given in units of MeV. From the left to the right panels, the training results are shown for the binding energy, the pairing energy, and the energy of the external fields. The results for 20,000 test data points are plotted in each figure, in which densely populated (under populated) points are displayed in red (blue).

the Skyrme-EDF with the Kohn-Sham method and obtain a single training data point. In marked contrast, the time to predict the energy with the neural network used in this paper from a given density is much shorter, about 0.1 ms. The difference in the computational speed will become larger for heavy nuclei. This makes a great advantage of using the deep learning method e.g., in plotting a multi-dimensional potential energy surface for nuclear fission studies of heavy nuclei.

TABLE II. The mean absolute error (MAEs) for each learning with the SHO and the RND external fields. The units are MeV for $E [ \rho ]$ and $E [ v ]$ , while the MAE for $\rho [ v ]$ is dimensionless (see Eq. (16)).   

<table><tr><td></td><td colspan="2">SHO</td><td colspan="2">RND</td></tr><tr><td>type</td><td>E[ρ]</td><td>E[v]</td><td>E[ρ]</td><td>E[v]</td></tr><tr><td>Ebin</td><td>0.0051</td><td>0.0054</td><td>0.0433</td><td>0.0237</td></tr><tr><td>Ekin</td><td>0.0165</td><td>0.0071</td><td>0.1131</td><td>0.0900</td></tr><tr><td>Eint</td><td>0.0105</td><td>0.0182</td><td>0.0431</td><td>0.1499</td></tr><tr><td>Epair</td><td>0.0233</td><td>0.0261</td><td>0.1567</td><td>0.1411</td></tr><tr><td>Ex</td><td>0.0318</td><td>0.0105</td><td>6.6973</td><td>0.1338</td></tr><tr><td></td><td colspan="2">ρ[v]</td><td colspan="2">ρ[v]</td></tr><tr><td></td><td colspan="2">0.1107</td><td colspan="2">0.4101</td></tr></table>

$$
\begin{array}{l l}\text {C .}&v \rightarrow E [ v ]\end{array}
$$

While it is somewhat tangential to the topic of DFT, there is a certain demand in electronic systems for a functional that directly predicts the energy from a given external field. Because of this, in the previous study [6], an energy functional $E [ v ]$ was constructed following the same procedure as that to construct a functional $E [ \rho ]$ . Even though it is unclear whether such a functional is useful in nuclear physics, it may be worth investigating whether a functionl $E [ v ]$ can be constructed in connection to the discussion in Ref. [6]. We therefore carry out similar calculations using the same neural network and dataset as those in the previous subsection, but with the external fields as the explanatory variables.

The MAEs for $E [ v ]$ are summarized in Tab. II, which shows that the MAE for $E [ v ]$ tends to be decreased compared to that for $E [ \rho ]$ . This is because the external field contains more information than the density distribution. This is particularly true for learning the energy from the external fields. On the other hand, the accuracy gets lowered for the binding energy with the SHO external fields. To investigate the origin for this, the lower panels in Fig. 3 show comparisons between $E [ v ]$ from the Skyrme KS calcaulations and the result of the deep learning. We find that the points with large errors are due to external fields that have small amplitudes, that is, almost flat potentials. Since many SHO potentials used in the dataset have a large curvature, it is diffult to learn information about external fields with a small curvature. Such a prob-

![](images/51a1e5cccbbd15f11d7b64b9aeb4c6607b52402575bb16a6d8f7b294cba71019.jpg)  
FIG. 4. A neural network with the encoder-decoder structure employed in this work for a mapping from an external $v$ to a particle number density $\rho$ . It consists of 10 hidden layers, all of which are fully-connected. Their activation functions are ReLU, and the softmax activation function is employed for the output layer.

lem is less likely to occur in fermionic systems when density distributions are used as the explanatory variables, leading to a somewhat better accuracy.

$$
\mathbf {D}. \quad v \rightarrow \rho [ v ]
$$

Observables are in general calculated in DFT with a particle number density, which is obtained with a given functional. That is, a functional has to be known in advance in obtaining a particle number density. As demonstrated in Ref. [6], if a neural network can directly predict the density for a given external field, the calculation speed will be significantly improved. We therefore carry out deep learning for the nuclear system with the external fields as the explanatory variables and density distributions as the objective variables. To this end, we have to take into account the fact that the densities are normalized to the particle number, that is, $\textstyle \int d ^ { 3 } r \rho = A$ . The softmax function, which is commonly used in classification problems, enables one to require the normalization condition. We shall employ this approach in this study for the output layer. For the axial symmetric system, the following relationship exists with a discretized spatial mesh:

$$
\frac {2 \pi}{A} \iint r d r d z \rho (r, z) \simeq \sum_ {i, j} \rho \left(r _ {i}, z _ {j}\right) \frac {2 \pi r _ {i} \Delta r \Delta z}{A} = 1, \tag {15}
$$

where $\Delta r = \Delta z = 0 . 8 \mathrm { f m }$ are the mesh width.

Thus, by selecting $2 \pi r _ { i } \Delta r \Delta z \rho ( r _ { i } , z _ { j } ) / A$ as the objective variable, the normalization is automatically imposed. In this study, we use a neural network with an encoderdecoder structure for training, as is shown in Fig. 4. The MAE for the learning of $\rho [ v ]$ is defined as

$$
\mathrm {M A E} = \overline {{2 \pi \iint r d r d z \left| \rho_ {\text {p r e d}} (r , z) - \rho_ {\text {a n s}} (r , z) \right|}}, \tag {16}
$$

![](images/807499812ee64fdecb1ee2be9a39c34277dde2a68b2e2199da2d64b02a6991d8.jpg)

![](images/deaab3b765758195e6681be32fc535f3b0cb23a352a038c4426b4e7db2941e0f.jpg)  
FIG. 5. The absolute error of the density distribution directly generated by a deep learning from a given external field $v$ . It is plotted as a function of the binding energy from the corresponding Kohn-Sham calculation. The left and the right panels show the results with the SHO and the RND external fields, respectively. The densely populated points are displayed in red, while the underpopulated points are shown in blue.

![](images/cbe353e9dcaf6b35e81b56e6e3c36a3e5ae92dd2a7a7d68f3665a032ec47a329.jpg)  
FIG. 6. Examples of the predicted densities (the bottom panels) generated directly from the RND external potentials shown in the top panels. For a comparision, the corresponding Khon-Sham densities are also plotted in the middle panels. The units of the color coordinate are MeV for the external potentials and $\mathrm { f m } ^ { - 3 }$ for the densities. In each panel, the horizontal axis denotes the $r$ coordinate while the vertical axis denotes the $z$ coordinate, whose scales are shown in the left bottom panel.

![](images/63997c1d4d3b763825ba1bdeadac8079f48dbf3ec6a2a41b9b46b480dac055f5.jpg)

![](images/50cef953806032c1f2651dad4a72193645977d83d638dac1d222aa6f7251db88.jpg)  
FIG. 7. A verification of generalization performance for the present deep learning. The left and right panels show the results with the RND and the SHO external fields, respectively. The horizontal axes denote the energies obtained with the Kohn-Sham calculations. On the other hand, the vertical axes denote $E _ { \mathrm { S H O } } [ \rho _ { \mathrm { R N D } } ]$ (the left panel) and $E _ { \mathrm { R N D } } [ \rho _ { \mathrm { S H O } } ]$ (the right panel), that is, the predictions of deep learning trained with the SHO (the left panel) and the RND (the right panel) external fields. Both the taining and test data (200,000 data in total) are plotted in each panels because the RND (SHO) dataset are not used in training $E _ { \mathrm { S H O } } [ \rho ]$ $\mathrm { \Delta } E _ { \mathrm { R N D } } [ \rho ] _ { \ r { \mathrm { 1 } } } ,$ ).

where $\rho _ { \mathrm { p r e d } } ( r , z )$ and $\rho _ { \mathrm { a n s } } ( r , z )$ denote a predicted density and a Kohn-Sham result, respectively. Here, the bar symbol represents the average over the test data. We apply the same cut-off energies to the training data as those for the binding energy (see Tab. I).

Figure 5 shows the error for each test data point plotted as a function of the corresponding binding energy from the Kohn-Sham calculation. Their average corresponds to the MAE (16), which is 0.1107 for the SHO external fields and 0.4101 for the RND external fields. Figure 6 presents the images of the predicted densities for a few randomly selected data points for the RND external fields, in comparison to the corresponding Kohn-Sham densities. These examples clearly show that our neural networks successfully reproduce the Konh-Sham densities.

# E. Generalization performance

We have so far introduced the two types of external fields and constructed the two independent datasets. For each dataset, we have successfully provided predictions for the training data with sufficient accuracy; however, this does not guarantee performance for unknown data. For instance, a neural network trained with the RND data does not necessarily yield accurate predictions for the SHO data. This is because the RND and the SHO external fields yield density profiles in a different way to each other. In general, such generalization performance is a critical concern in applying a trained neural network to another dataset.

To investigate this issue in the context of nuclear physics, let us consider $E _ { \mathrm { S H O } } [ \rho _ { \mathrm { R N D } } ]$ and $E _ { \mathrm { R N D } } [ \rho _ { \mathrm { S H O } } ]$ , where $\rho _ { \mathrm { S H O } }$ and $\rho _ { \mathrm { R N D } }$ are the Kohn-Sham densities obtained with the SHO and the RND external fields, respectively, and $E _ { \mathrm { S H O } }$ and $E _ { \mathrm { R N D } }$ are the functionals trained with $\rho _ { \mathrm { S H O } }$ and $\rho _ { \mathrm { R N D } }$ , respectively. In Sec. III B, we have investigated $E _ { \mathrm { S H O } } [ \rho _ { \mathrm { S H O } } ]$ and ${ \cal E } _ { \mathrm { R N D } } [ \rho _ { \mathrm { R N D } } ]$ , but here we are interested in the performance of the functionals when the densities obtained with the other types of external fields are used as inputs. The left panel in Fig. 7 compares the binding energies obtained with the Kohn-Sham calculations with the RND external fields with $E _ { \mathrm { S H O } } [ \rho _ { \mathrm { R N D } } ]$ . The right panel shows similar quantities, but by inverting RND and SHO, that is a comparison between the Kohn-Sham calculations with the SHO external potentials and $E _ { \mathrm { R N D } } [ \rho _ { \mathrm { S H O } } ]$ . One can see that the performance of the neural network trained with the SHO external fields, $E _ { \mathrm { S H O } }$ , is quite poor in reproducing the RND test data with large randomness. On the other hand, the neural network trained with the RND external fields, $E _ { \mathrm { R N D } }$ , successfully predicts the SHO test data, although the errors are larger than those for ${ \cal E } _ { \mathrm { R N D } } [ \rho _ { \mathrm { R N D } } ]$ shown in Fig. 3. The MAEs between Kohn-Sham results and predictions are 1.1523 MeV for $E _ { \mathrm { S H O } } [ \rho _ { \mathrm { R N D } } ]$ and 0.122 MeV for $E _ { \mathrm { R N D } } [ \rho _ { \mathrm { S H O } } ]$ . A similar conclusion has been obtained also in Ref. [6]. Therefore we can conclude that the RND potentials which we adopted are random enough for deep learning.

# IV. SUMMARY AND FUTURE PERSPECTIVES

Starting from a Skyrme functional, we have successfully constructed an energy density functional (EDF) which depends only on a particle number density. This functional does not require Kohn-Sham orbitals, and thus can be regarded as an orbital-free EDF (OF-EDF). To this end, we have applied deep learning, in which the density distributions obtained with two types of random external fields (SHO and RND) were mapped on the energy with a neural network. The resultant EDF was found to predict various energies for the original Skyrme EDF with reasonable accuracy, except for the energy of the RND external fields, whose accuracy could however be considerably improved when the energies were predicted with deep learning in which the external fields themselves were directly learned. The latter feature is more pronounced in systems with an attractive interaction than in electron systems. We have also found that deep learning with less random SHO external potentials has smaller errors as compared to that with the RND external fields.

In this paper, we have employed simple supervised learning. However, there are various methods of machine learning besides this. For example, generative models such as a generative adversarial network (GAN) [38, 39] and a diffusion model [3, 40] may provide efficient ways to generate the particle number densities, that is the input for deep learning used in this work to construct an OF-EDF. These methods maybe useful alternatives for future application of the deep learning method discussed in this paper.

In nuclear physics, a triaxial deformation often plays an important role, particularly in nuclear fission. In that occasion, one needs to deal with 3-dimensional densities, accounting also for spin and isospin indices. We mention that traditional neural networks, comprising fullyconnected layers, tend not to perform efficiently with such 3-dimensional data, primarily because the data size tends to become huge when the data are converted to 1-dimensional data. On the other hand, CNNs have shown adaptability to data of general dimensions. With the Keras API [36], 3D CNNs can be conveniently implemented, making a straightfoward extension of the present work to 3D cases. Furthermore, the Vision Transformer (ViT) [4], which has recently demonstrated success in image recognition tasks, can also be extended to 3-dimensional data. With those schemes, the dimensionality of the density itself is not a crucial issue in learning EDFs, without incurring additional costs for preparing training data.

One of the big advantages of using deep learning meth-

ods is that energies can be rapidly computed once test data are prepared and trained. With such low-cost calculations, numerical experiments will become much easier than before. We mention that, as objectives of research become more and more sophisticated, the number of DFT calculations required to publish a single research paper has in general been increased in these days. A typical example is a calculation for fission barriers in a multidimensional space. Even though computer performance continues to be improved, a computational cost of research has in general been increased, and it has been more complicated than before to test an idea with a numerical experiment. Fast computational methods like the one developed in this work, particularly when they are provided in a convenient format such as a Python library, can significantly shorten the time required to test and validate ideas. If a numerical accuracy is an issue, one may revalidate ideas obtained with deep learning by using the traditional Kohn-Sham scheme. This could be interpreted as an application of the idea of materials informatics (MI) [41] to a theoretical research.

A potential problem in performing supervised learning is that one has to collect a large set of training data. In this work, we have chosen a relatively light nucleus, $^ { 2 4 }$ Mg, and imposed axial symmetry, and thus we have treated a relatively low-cost system. However, heavy and superheavy nuclei, such as uranium isotopes, will be very costly in terms of data collection, especially when no symmetry is imposed, even though those nuclei have attracted lots of attention in nuclear physics, as e.g. a finding the optimal pathway in fission has still been a big theoretical challenge. In this regard, we would like to point out that a data collection needs not be performed individually; it could actually be done collaboratively by many researchers. A lot of good quality data, which are ready to be used in deep learning, may have already existed for some selected nuclei. Therefore, we believe that it is desirable to establish a framework in the nuclear theory community to collect numerical data and/or to carry out numerical calculations with unified hyperparameters such as a mesh size. Such a collaborative approach will help advance research more efficiently and effectively, benefiting the whole nuclear physics community.

# ACKNOWLEDGMENTS

We thank G. Col`o for useful discussions. This work was supported by JSPS KAKENHI (Grant Nos. 21J22348, JP19K03824, JP19K03861, JP19K03872, and JP23K03414).

Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers), edited by J. Burstein, C. Doran, and T. Solorio (Association for Computational Linguistics, 2019) pp. 4171–4186.   
[2] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei, in Advances in Neural Information Processing Systems, Vol. 33, edited by H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin (Curran Associates, Inc., 2020) pp. 1877–1901.   
[3] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2022).   
[4] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby, in 9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021 (OpenReview.net, 2021).   
[5] A. Gulati, J. Qin, C. Chiu, N. Parmar, Y. Zhang, J. Yu, W. Han, S. Wang, Z. Zhang, Y. Wu, and R. Pang, CoRR abs/2005.08100 (2020), 2005.08100.   
[6] K. Ryczko, D. A. Strubbe, and I. Tamblyn, Phys. Rev. A 100, 022512 (2019).   
[7] K. Mills, M. Spanner, and I. Tamblyn, Phys. Rev. A 96, 042113 (2017).   
[8] K. Shiina, H. Mori, Y. Okabe, and L. Hwee-Kuan, Scientific Reports 10, 2177 (2020).   
[9] V. Stanev, C. Oses, A. G. Kusne, E. Rodriguez, J. Paglione, S. Curtarolo, and I. Takeuchi, npj Computational Materials 4, 29 (2018).   
[10] G. Saxena, A. Jain, and P. Sharma, Physica Scripta 96 (2021).   
[11] Z.-A. Wang and J. Pei, Phys. Rev. C 104, 064608 (2021).   
[12] X. Wu, L. Guo, and P. Zhao, Physics Letters B 819, 136387 (2021).   
[13] M. R. Mumpower, T. M. Sprouse, A. E. Lovell, and A. T. Mohan, Phys. Rev. C 106, L021301 (2022).   
[14] A. E. Lovell, A. T. Mohan, T. M. Sprouse, and M. R. Mumpower, Phys. Rev. C 106, 014305 (2022).   
[15] A. Sarkar and D. Lee, Phys. Rev. Res. 4, 023214 (2022), arXiv:2107.13449 [nucl-th].   
[16] O. M. Molchanov, K. D. Launey, A. Mercenne, G. H. Sargsyan, T. Dytrych, and J. P. Draayer, Phys. Rev. C 105, 034306 (2022).   
[17] X. H. Wu, Z. X. Ren, and P. W. Zhao, Phys. Rev. C 105, L031303 (2022).   
[18] M. Verriere, N. Schunck, I. Kim, P. Marevi´c, K. Quinlan, M. N. Ngo, D. Regnier, and R. D. Lasseri, Frontiers in Physics 10, 10.3389/fphy.2022.1028370 (2022).   
[19] M. Kn¨oll, T. Wolfgruber, M. L. Agel, C. Wenz, and R. Roth, Physics Letters B 839, 137781 (2023).   
[20] X. Zhang, W. Lin, J. M. Yao, C. F. Jiao, A. M. Romero, T. R. Rodr´ıguez, and H. Hergert, Phys. Rev. C 107, 024304 (2023).   
[21] G. P. A. Nobre, D. A. Brown, S. J. Hollick, S. Scoville, and P. Rodr´ıguez, Phys. Rev. C 107, 034612 (2023).   
[22] Y. L. Yang and P. W. Zhao, Phys. Rev. C 107, 034320 (2023).

[23] Z.-X. Yang, X.-H. Fan, Z.-P. Li, and H. Liang, Phys. Lett. B 840, 137870 (2023).   
[24] K.-F. Pu, H.-L. Li, H.-L. L¨u, and L.-G. Pang, Chinese Physics C 47, 054104 (2023).   
[25] A. Boehnlein, M. Diefenthaler, N. Sato, M. Schram, V. Ziegler, C. Fanelli, M. Hjorth-Jensen, T. Horn, M. P. Kuchera, D. Lee, W. Nazarewicz, P. Ostroumov, K. Orginos, A. Poon, X.-N. Wang, A. Scheinker, M. S. Smith, and L.-G. Pang, Rev. Mod. Phys. 94, 031003 (2022).   
[26] M. Bender, P.-H. Heenen, and P.-G. Reinhard, Rev. Mod. Phys. 75, 121 (2003).   
[27] T. Naito, S. Endo, K. Hagino, and Y. Tanimura, Journal of Physics B: Atomic, Molecular and Optical Physics 54, 165201 (2021).   
[28] P. Ring and P. Schuck, The nuclear many-body problem (Springer-Verlag, New York, 1980).   
[29] E. Chabanat, P. Bonche, P. Haensel, J. Meyer, and R. Schaeffer, Nuclear Physics A 635, 231 (1998).   
[30] P.-G. Reinhard, D. J. Dean, W. Nazarewicz, J. Dobaczewski, J. A. Maruhn, and M. R. Strayer, Phys. Rev. C 60, 014316 (1999).   
[31] A. Bohr and B. Mottelson, Nuclear Structure, Nuclear Structure No. 1 (World Scientific, 1998).   
[32] E. Ter´an, V. E. Oberacker, and A. S. Umar, Phys. Rev. C 67, 064314 (2003).   
[33] A. Krizhevsky, I. Sutskever, and G. E. Hinton, in Advances in Neural Information Processing Systems, Vol. 25, edited by F. Pereira, C. Burges, L. Bottou, and K. Weinberger (Curran Associates, Inc., 2012).   
[34] L. Alzubaidi, J. Zhang, A. J. Humaidi, A. Q. Al-Dujaili, Y. Duan, O. Al-Shamma, J. Santamar´ıa, M. A. Fadhel, M. Al-Amidie, and L. Farhan, Journal of Big Data 8 (2021).   
[35] D. P. Kingma and J. Ba, in 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings, edited by Y. Bengio and Y. LeCun (2015).   
[36] Keras official document, https://keras.io.   
[37] M. R. Mumpower, R. Surman, G. C. McLaughlin, and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016), arXiv:1508.07352 [nucl-th].   
[38] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, in Advances in Neural Information Processing Systems, Vol. 27, edited by Z. Ghahramani, M. Welling, C. Cortes, N. Lawrence, and K. Weinberger (Curran Associates, Inc., 2014).   
[39] J. Gui, Z. Sun, Y. Wen, D. Tao, and J. Ye, IEEE Transactions on Knowledge and Data Engineering 35, 3313 (2023).   
[40] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli, in Proceedings of the 32nd International Conference on Machine Learning, Proceedings of Machine Learning Research, Vol. 37, edited by F. Bach and D. Blei (PMLR, 2015) pp. 2256–2265.   
[41] R. Ramprasad, R. Batra, G. Pilania, A. Mannodi-Kanakkithodi, and C. Kim, npj Computational Materials 3, 54 (2017).   
[42] Kaggle, https://www.kaggle.com.   
[43] Winners of IceCube machine learning competition announced, https:// icecube.wisc.edu/news/outreach/2023/06/ winners-of-icecube-machine-learning-competition-

# Appendix A: Figures for $E _ { \mathrm { k i n } }$ and $E _ { \mathrm { i n t } }$

In this Appendix, we show figures for $E _ { \mathrm { k i n } }$ and $E _ { \mathrm { i n t } }$ which are not shown in Sec. III. We also show a figure for a histogram for $\boldsymbol { E } _ { \mathrm { e x } }$ . The conclusions remain the same as those for Figs. 2 and 3.

![](images/39be794f6fd395480d6f2558b021a8bb537067041541fb7f2147f2339f2d55d8.jpg)

![](images/6230606541e0a0a8546d366a9b700cd98c744a2f66ede489301173f20721ab34.jpg)

![](images/9835488e6d977570af227611a3379a82db83a8cbe0e47eb42fef77c78b6df44b.jpg)

![](images/c9590275cb67cca4b731b6ca9f840c83bfb6cf032881045383f8aa93448175f5.jpg)

![](images/0776f349433cbe246ffecc1f0393c11ec946dd52608918d5e54c3be7ca596eba.jpg)

![](images/8bd54a867329bf347d88f82b5b978588649c0cc44698af9ded6c5537b3ae31b1.jpg)  
energy/MeV   
FIG. 8. Same as Fig. 2, but for the kinetic energy, the interaction energy, and the energy for the external field.

![](images/91753186f248196bff42d1fdabaeeff1872a3c517ec760379ec436fce22fb338.jpg)

![](images/ab37643bdb6fc85288dd3e2ebed29bb762fd358d0f12f964b04bddffd0b8d67d.jpg)

![](images/a164b117507ef0482d75a070bf2dd555c7e1644aa797c812294c74ea2135f120.jpg)

![](images/6d80909fd02b75779699f449084d6490b8f72820df74935a3b7af9a38ff847c4.jpg)

![](images/13b4a74201bb492f55987a96d129cd2325f9eb24285e387176da04264f77b980.jpg)

![](images/97dc6b8710340e9c228485e7f6888a16b428e12e715251c41cbdaf1d2d80dd5d.jpg)

![](images/1767f13456066cf067f126b58bf08af56fa48a0239a661a0a288f890fd0c9846.jpg)

![](images/2e7b53a73122b8707a9b608498aa5b6d934c9dbeca443d67970e0c0c22251298.jpg)  
Kohn-Sham energy /MeV   
FIG. 9. Same as Fig. 8, but for the kinetic and the interaction energies.

# Appendix B: Convolutional Neural Network

In the previous study [6], the convolutional neural network (CNN) was used for calculating an OF-EDF. An efficient structure in the CNN enables computers to recognize images, which reduces the trainable parameters, and the CNN works well in learning with large-size images. Since the inputted image size is small enough in this study, we can use the neural network only consisting of the fully-connected layer. We can in principle perform the training with CNNs as well, but we find that the results are not significantly different (see Table V). To this end, we use the CNN listed in Tabs. III and IV. The learning methods are the same as for the fully-

connected layer. Considering that the CNN is computationally more expensive than the fully-connected layer, the benefit of using the CNN does not seem to be substantial, at least for the system studied in this paper.

Of course, there are many choices and hyperparameters in deep learning. Therefore, we do not mean to claim that there is no sufficient benefit from using CNNs. However, if one needs better and more accurate training results, skill and experience are required. In that occasion, one way to proceed is to ask professionals to submit their ideas in a competition on sites such as Kaggle [42], for example. Hopefully, such approach could help identify optimal machine learning methods and hyperparameters. For example, the IceCube held a competition on Kaggle [43].

TABLE III. A CNN employed in this work to learn $E [ \rho ]$ and $E [ v ]$ . The type of each layer is expressed with the language of Keras API [36], with which one can reproduce this neural network easily. In each layer, all arguments not mentioned are default values.

<table><tr><td>layer</td><td>type</td></tr><tr><td>input</td><td>Input(shape=(10, 20, 1))</td></tr><tr><td>1</td><td>Conv2D(filters=32, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>2</td><td>Conv2D(filters=64, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>3-8</td><td>Conv2D(filters=64, kernel_size=4, padding=&#x27;same&#x27;, activation=&#x27;relu&#x27;)</td></tr><tr><td>9</td><td>Conv2D(filters=128, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>10-13</td><td>Conv2D(filters=128, kernel_size=3, padding=&#x27;same&#x27;, activation=&#x27;relu&#x27;)</td></tr><tr><td>14</td><td>Flatten()</td></tr><tr><td>15</td><td>Dense(units=128, activation=&#x27;relu&#x27;)</td></tr><tr><td>output</td><td>Dense(units=1, activation=&#x27;sigmoid&#x27;)</td></tr></table>

TABLE IV. A CNN employed in this work to learn $\rho [ v ]$ . The neural network has encoder-decoder structure. Layer 1–4 are reducing convolutional layers, and Layer 5–7 are non-reducing convolutional layers, where the size of images are (2, 12). We use Layer 8–11 as deconvolution layers to enlarge them up to (10, 20). In each layer, all arguments not mentioned are default values.

<table><tr><td>layer</td><td>type</td></tr><tr><td>input</td><td>Input(shape=(10, 20, 1))</td></tr><tr><td>1</td><td>Conv2D(filters=32, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>2</td><td>Conv2D(filters=64, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>3</td><td>Conv2D(filters=128, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>4</td><td>Conv2D(filters=256, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>5-7</td><td>Conv2D(filters=256, kernel_size=4, padding=&#x27;same&#x27;, activation=&#x27;relu&#x27;)</td></tr><tr><td>8</td><td>Conv2DTranspose(filters=256, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>9</td><td>Conv2DTranspose(filters=128, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>10</td><td>Conv2DTranspose(filters=64, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>11</td><td>Conv2DTranspose(filters=32, kernel_size=3, activation=&#x27;relu&#x27;)</td></tr><tr><td>12</td><td>Flatten()</td></tr><tr><td>13</td><td>Dense(units=200, activation=&#x27;softmax&#x27;)</td></tr><tr><td>output</td><td>Reshape(target_shape=(10, 20, 1))</td></tr></table>

TABLE V. The mean absolute errors (MAEs) for each learning with the SHO and the RND external fields using the CNNs. The units are MeV for $E [ \rho ]$ and $E [ v ]$ , while the MAE for $\rho [ v ]$ is dimensionless.

<table><tr><td></td><td colspan="2">SHO</td><td colspan="2">RND</td></tr><tr><td>type</td><td>E[ρ]</td><td>E[v]</td><td>E[ρ]</td><td>E[v]</td></tr><tr><td>E_bin</td><td>0.0049</td><td>0.0055</td><td>0.0336</td><td>0.0245</td></tr><tr><td>E_kin</td><td>0.0151</td><td>0.0079</td><td>0.1010</td><td>0.1134</td></tr><tr><td>E_int</td><td>0.0119</td><td>0.0191</td><td>0.0484</td><td>0.1619</td></tr><tr><td>E_pair</td><td>0.0179</td><td>0.0250</td><td>0.1505</td><td>0.1852</td></tr><tr><td>E_ex</td><td>0.0220</td><td>0.0108</td><td>4.7059</td><td>0.0889</td></tr><tr><td></td><td colspan="2">ρ[v]</td><td colspan="2">ρ[v]</td></tr><tr><td></td><td colspan="2">0.1092</td><td colspan="2">0.3484</td></tr></table>