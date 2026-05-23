# Deep-neural-network approach to solving the ab initio nuclear structure problem

Y. L. Yang1 and P. W. Zhao1, ∗

1State Key Laboratory of Nuclear Physics and Technology, School of Physics, Peking University, Beijing 100871, China

# Abstract

Predicting the structure of quantum many-body systems from the first principles of quantum mechanics is a common challenge in physics, chemistry, and material science. Deep machine learning has proven to be a powerful tool for solving condensed matter and chemistry problems, while for atomic nuclei it is still quite challenging because of the complicated nucleon-nucleon interactions, which strongly couple the spatial, spin, and isospin degrees of freedom. By combining essential physics of the nuclear wave functions and the strong expressive power of artificial neural networks, we develop FeynmanNet, a deep-learning variational quantum Monte Carlo approach for ab initio nuclear structure. We show that FeynmanNet can provide very accurate solutions of ground-state energies and wave functions for 4He, $_ 6$ Li, and even up to $^ { 1 6 }$ O as emerging from the leading-order and next-to-leading-order Hamiltonians of pionless effective field theory. Compared to the conventional diffusion Monte Carlo approaches, which suffer from the severe inherent fermion-sign problem, FeynmanNet reaches such a high accuracy in a variational way and scales polynomially with the number of nucleons. Therefore, it paves the way to a highly accurate and efficient ab initio method for predicting nuclear properties based on the realistic interactions between nucleons.

# I. INTRODUCTION

Atomic nuclei are self-bound systems consisting of protons and neutrons, which interact with each other via strong interactions. However, it is a great challenge to describe nuclear structure directly from the fundamental theory of strong interactions, quantum chromodynamics (QCD), due to its non-perturbative nature at the low-energy regime. The advent of the effective field theory (EFT) paradigm in the early 1990s [1, 2] has opened the way to linking QCD and the low-energy nuclear structure by establishing nuclear EFTs [3], which are nowadays the main inputs [4–7] to ab initio nuclear many-body approaches. The nuclear EFTs provide the nuclear Hamiltonian with controlled approximations and the corresponding many-nucleon Schr¨odinger equation is then solved with state-of-the-art manybody methods. Such a combination has achieved a great success in describing many nuclear properties including binding energies and radii [8–10], $\beta$ decays [11], $\alpha$ - $\alpha$ scattering [12], etc.

Nevertheless, some major challenges remain because the nucleon-nucleon interaction is extremely complex, in contrast to the Coulomb force and/or the van der Waals potential used in atomic and molecular physics. It contains a strong tensor component involving both the spin and isospin of the nucleons and also significant spin-orbit forces, inducing strong coupling between the spin-isospin and spatial degrees of freedom [13]. These features lead to complex nuclear many-body phenomena, whose description requires a consistent treatment of both short-range (or high-momentum) and long-range (or low-momentum) correlations. Among the variety of nuclear many-body methods, quantum Monte Carlo (QMC) methods [14] based upon Feynman path integrals formulated in the continuum have proven to be quite valuable for these problems. They are able to deal with a wide range of momentum components of the interaction and, thus, can accommodate “bare” potentials derived within nuclear EFTs. However, the QMC methods are presently limited to either light nuclei with up to $A = 1 2$ nucleons [15–18] or larger systems but with simplified nuclear Hamiltonians [19, 20]. This is mainly because of the infamous fermion-sign problem [21], which leads to an exponential increasing ratio of error to signal with the number of nucleons. Therefore, an accurate and polynomial scaling solution is highly desired to extend the QMC calculations to medium-mass nuclei.

Machine learning has provided the opportunity for a polynomial scaling solution of quantum many-body problems, especially for many-electron systems [22]. It is motivated by the fact that artificial neural networks (ANNs) can compactly represent complex highdimensional functions and, thus, should be able to provide efficient means for representing the wave function of quantum many-body states. A variational representation of ANN-based many-body quantum states has been originally introduced for prototypical spin lattice systems [23], and then generalized to several quantum systems in continuous space [24, 25]. Recently, deep neural networks trained within variational Monte Carlo (VMC) have been further developed to tackle ab initio chemistry problems [26–29].

For ab initio nuclear structure, due to the complexity of the nucleon-nucleon interaction, the application of machine-learning approaches to nuclear many-body problems is still in its infancy. They are often split into two main categories, supervised and unsupervised [30]. Here, the many-nucleon Schr¨odinger equation is solved directly with unsupervised learning. The first attempt was given to solve deuteron, a two-body bound state, in momentum space [31]. Subsequently, an ANN quantum state ansatz defined by the product of a Jastrow

factor and a Slater determinant was introduced to solve nuclei with up to $A = 6$ nucleons in coordinate space within the VMC method [32, 33]. It outperforms the routinely employed ansatz based on two- and three-body Jastrow functions, while there are still significant deviations from the numerically exact results for three- and four-body nuclei, mainly caused by the incorrect nodal surface of the single Slater determinant.1 The incorrect nodal surface can be largely improved with an augmented Slater determinant involving hidden nucleonic degrees of freedom [34], but the nuclear Hamiltonian is limited to contain central forces only, thereby preventing the application to realistic nuclear structure problems, which depend crucially on the tensor and spin-orbit forces [16].

A key development improving the nodal surface in the present work is the consideration of a many-body backflow transformation, which was originally proposed by Feynman and Cohen for liquid helium [35]. While the traditional backflow does not reach a very high accuracy, a series of recent works showed that representing the backflow with a neural network is a powerful generalization [36] and can greatly improve the accuracy in solving many-electron problems [26, 27].

In this work, we develop a novel deep-learning QMC approach for nuclear many-body problems, FeynmanNet, which includes multiple Slater determinants and backflow transformation based on powerful deep-neural-network representations encompassing both continuous spatial and discrete spin-isospin degrees of freedom for nucleons. In particular, to incorporate many-body correlations induced by the tensor and spin-orbit forces, the deep neural networks are designed to represent complex-valued nuclear wave functions. Moreover, physics related to low-energy nuclear structure including the major shell structure and the point symmetries is explicitly encoded in the neural-network architecture, and it makes the obtained FeynmanNet not only highly accurate, but also robust and efficient in the training process. We demonstrate the high performance of FeynmanNet by benchmarking our results against the hyperspherical-harmonics (HH) method for $^ 4$ He and $_ 6$ Li and the auxiliary-field diffusion Monte Carlo (AFDMC) approach for $^ { 1 6 }$ O. Considering that FeynmanNet scales polynomially with the number of nucleons, the present work opens the way to highly accurate ab initio studies of medium-mass nuclei with quantum Monte Carlo approaches.

# II. ARCHITECTURE

At the core of our approach is a deep-learning architecture, dubbed FeynmanNet, designed for a compact representation of the nuclear wave function. Due to the strong tensor and spin-orbit interactions among nucleons, it is essential to explicitly write the nuclear wave function to be complex-valued,

$$
\Psi (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}) = \Psi^ {\mathrm {(R)}} (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}) + \mathrm {i} \Psi^ {\mathrm {(I)}} (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}), \tag {1}
$$

where $\pmb { x } _ { i } = ( \bar { r } _ { i } , s _ { i } , t _ { i } )$ are the single-nucleon variables, including the intrinsic spatial coordinates $\bar { \pmb { r } } _ { i } = \pmb { r } _ { i } - \pmb { r } _ { \mathrm { c , m } }$ . with ${ r } _ { \mathrm { c . m } }$ . being the position of the center of mass, the spin $s _ { i } = \pm 1 / 2$ , and the isospin $t _ { i } = \pm 1 / 2$ . The introduction of the intrinsic spatial coordinates $\mathbf { \nabla } _ { r _ { i } }$ assures the translational invariance of the wave function and avoids the spurious center-of-mass motions [14].

Both the real and imaginary parts of the wave function are constructed by considering Jastrow correlations and multiple Slater determinants consisting of backflow transformed orbitals,

$$
\Psi^ {(\alpha)} (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}) = \mathrm {e} ^ {\mathcal {U} ^ {(\alpha)} (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A})} \sum_ {n = 1} ^ {N _ {\mathrm {d e t}}} w _ {n} ^ {(\alpha)} \det  [ \mathbf {f} ^ {(\alpha , n)} (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}) ], \quad \alpha = \mathrm {R}, \mathrm {I}. \tag {2}
$$

Here, $\mathcal { U } ^ { ( \alpha ) }$ are the permutation-invariant Jastrow factors, $N _ { \mathrm { d e t } }$ the number of Slater determinants, and $w _ { n } ^ { ( \alpha ) }$ the weight of the corresponding Slater determinant. The weights $w _ { n } ^ { ( \alpha ) }$ are determined variationally during the training process.

Following the basic idea of the backflow transformation [35], the single-nucleon orbitals of the $i$ th nucleon in the determinant depend not only on its own variables ${ \bf { \chi } } _ { x }$ , but also on the variables of all other nucleons in an exchangeable way. Specifically, as the architecture illustrated in Fig. 1, the matrix elements of $\mathbf { f } ^ { ( \alpha , n ) }$ are represented row by row with neural networks,

$$
f _ {i \mu} ^ {(\alpha , n)} (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}) = \rho_ {\mu} ^ {(\alpha , n)} \left(\phi^ {(\alpha , n)} (\boldsymbol {x} _ {i i}) + \sum_ {j \neq i} \eta^ {(\alpha , n)} (\boldsymbol {x} _ {i j}) \mathrm {e} ^ {- r _ {i j} ^ {2} / R ^ {2}}\right), \tag {3}
$$

where $\mu = 1 , \ldots , A$ is the index of the orbitals for the $i$ th nucleon.

First, the single-nucleon variables $\pmb { x } _ { i } = ( \bar { \pmb { r } } _ { i } , s _ { i } , t _ { i } )$ for the $i$ th nucleon are combined with those of all other nucleons $j \left( j \ne i \right)$ to form pairwise inputs $\pmb { x } _ { i j } = ( r _ { i j } , r _ { i j } , s _ { i } , s _ { j } , t _ { i } , t _ { j } )$ with

$\pmb { r } _ { i j } = \pmb { r } _ { i } - \pmb { r } _ { j }$ and $r _ { i j } = | \boldsymbol { r } _ { i j } |$ . In principle, the distances $r _ { i j }$ are redundant inputs. However, it was found that inputting $r _ { i j }$ could improve the performance of the neural-network wave functions in both electronic [26] and nuclear [37] systems. This should be due to the fact that the inclusion of distances $r _ { i j }$ respects the rotational invariance of the ground state.

Then, the pair-wise inputs are successively mapped into $N _ { \mathrm { l a t } }$ latent variables via a feedforward neural network $\eta ^ { ( \alpha , n ) }$ . The summation of these latent variables over $j$ assures the permutation invariance for nucleons other than the $i$ th nucleon. The Gaussian function $\mathrm { e } ^ { - r _ { i j } ^ { 2 } / R ^ { 2 } }$ in Eq. (3), with $R$ as a hyperparameter characterizing the range of nuclear force, is adopted to reduce the correlations of two nucleons which are outside the interacting range. For the case of $j = i$ , the pairwise inputs should be reduced to $\pmb { x } _ { i i } = ( \bar { r } _ { i } , \bar { r } _ { i } , s _ { i } , t _ { i } )$ , and they are mapped into $N _ { \mathrm { l a t } }$ latent variables via another feed-forward neural network $\phi ^ { ( \alpha , n ) }$ . The summation of these latent variables over all nucleon pairs are then input to a new feed-forward neural network $\pmb { \rho } ^ { ( \alpha , n ) }$ with $A$ outputs, providing the $A$ matrix elements for the $i$ th row. The designed architecture ensures the antisymmetry of the nuclear wave function, because one can exchange two nucleons by swapping two rows of the matrix $\mathbf { f } ^ { ( \alpha , n ) }$ , the determinant of which then changes its sign.

The Jastrow factors $\mathcal { U } ^ { ( \alpha ) }$ in Eq. (2) are represented by neural networks similar to the ones adopted in the previous work [33] based on the Deep Sets architecture [38, 39]. The pair-wise inputs of each pair of nucleons $( i , j )$ are mapped separately into a latent-space representation, and a summation over all pairs is then applied to enforce permutation invariance,

$$
\mathcal {U} ^ {(\alpha)} \left(\boldsymbol {x} _ {1}, \boldsymbol {x} _ {2}, \dots , \boldsymbol {x} _ {A}\right) = \rho^ {(\alpha , \mathcal {U})} \left(\sum_ {i \neq j} \phi^ {(\alpha , \mathcal {U})} \left(\boldsymbol {r} _ {i j}, r _ {i j}, s _ {i}, s _ {j}, t _ {i}, t _ {j}\right)\right). \tag {4}
$$

Here, $\phi ^ { ( \alpha , { \mathcal { U } } ) }$ and $\rho ^ { ( \alpha , { \mathcal { U } } ) }$ are feed-forward neural networks.

In the present work, all the feed-forward neural networks, namely $\eta$ , $\phi$ , and $\rho$ , are comprised of one fully-connected hidden layer with 16 nodes. Each of them translates mathematically into the following mapping from the inputs to the outputs,

$$
\boldsymbol {x} _ {\mathrm {o u t}} = \sigma (\mathbf {W} [ \sigma (\mathbf {V} \boldsymbol {x} _ {\mathrm {i n}} + \boldsymbol {a}) ] + \boldsymbol {b}). \tag {5}
$$

In the above equation, W, $\mathbf { V }$ , $\textbf { \em u }$ , and $^ { b }$ are the weights and biases of the network, which serve as variational parameters of the wave function. The activation function $\sigma$ is taken to be the Softplus function [40]. The number of latent variables $N _ { \mathrm { l a t } }$ , i.e., the output dimensions of $\eta$ and $\phi$ , as well as the input dimension of $\rho$ , is taken to be 16.

![](images/6b12b95a148743c16d5b8feb1d2e20077c3ad85717c8930b2d926771c7b1a4ed.jpg)  
FIG. 1. (Color online). Architecture of a backflow neural network in FeynmanNet. The input single-nucleon variables of $A$ nucleons are transformed row by row to the $A \times A$ Slater matrix elements consisting of the backflow transformed orbitals. $\phi$ , $\eta$ , and $\rho$ , feed-forward neural networks; $N _ { \mathrm { l a t } }$ , number of latent variables for each row.

Besides the essential antisymmetry, we also encode other physical knowledge about the nuclear wave function into FeynmanNet, and this significantly strengthens the expressive power of the network and accelerates the training process. First, the major shell structure of nuclei is embedded in each Slater determinant in Eq. (2) by replacing the matrix elements with $f _ { i \mu } ^ { ( \alpha , n ) } ( { \pmb x } _ { 1 } , \ldots , { \pmb x } _ { A } ) \cdot \varphi _ { \mu } ( { \pmb x } _ { i } )$ , where $\varphi _ { \mu } ( { \pmb x } _ { i } )$ takes the form

$$
\varphi_ {\mu} (\boldsymbol {x} _ {i}) = \sum_ {k = 1} ^ {N _ {f}} w _ {\mu k} \tilde {\varphi} _ {k} (\boldsymbol {x} _ {i}). \tag {6}
$$

Here, $\tilde { \varphi } _ { k } ( { \pmb x } _ { i } ) , \ k = 1 , 2 , \ldots , N _ { f }$ , is a set of single-particle shell model orbitals within a closed major shell $( n l )$ , and $w _ { \mu k }$ the expansion coefficients determined variationally during the training process. The shell model orbitals are of the form

$$
\tilde {\varphi} _ {k} \left(\boldsymbol {x} _ {i}\right) = R _ {n l} \left(\bar {r} _ {i}\right) Y _ {l l _ {z}} \left(\hat {\boldsymbol {r}} _ {i}\right) \chi_ {s t} \left(s _ {i}, t _ {i}\right), \tag {7}
$$

where $R _ { n l }$ are radial functions of a harmonic oscillator

$$
R _ {1 s} (r) = \mathrm {e} ^ {- r ^ {2} / 2 b ^ {2}}, \quad R _ {1 p} (r) = r \mathrm {e} ^ {- r ^ {2} / 2 b ^ {2}}, \quad \ldots , \tag {8}
$$

$Y _ { l l _ { z } }$ the spherical harmonics, and $\chi _ { s t } \in \{ \uparrow _ { n } , \downarrow _ { n } , \uparrow _ { p } , \downarrow _ { p } \}$ the spinors in the spin-isospin space.

In this work, we take the oscillator length $b ^ { 2 } = 1 0 ~ \mathrm { f m ^ { 2 } }$ , and using a different value should not affect FeynmanNet after training. The harmonic oscillator orbitals up to the ${ 1 s }$ shell are adopted for $^ 4$ He, and $1 p$ shell for $_ 6$ Li and $^ { 1 6 }$ O.

Moreover, FeynmanNet explicitly preserves the total isospin projection on the $z$ axis $T _ { z }$ and the parity $\pi$ by writing the nuclear wave function as

$$
\Psi_ {A, Z} ^ {\pi} \left(\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}\right) = \delta_ {T _ {z}, \frac {A}{2} - Z} (1 + \pi \hat {\mathcal {P}}) \Psi \left(\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {A}\right), \tag {9}
$$

where $A$ and $Z$ are, respectively, the mass and proton numbers of nuclei, and $\hat { \mathcal { P } }$ denotes the operator of space inversion. For even-even nuclei, the time-reversal symmetry of the wave function is additionally imposed by multiplying $( 1 + { \hat { \mathcal { T } } } )$ with $\hat { \mathcal { T } }$ being the time-reversal operator.

# III. TRAINING DETAILS

FeynmanNet is trained with the VMC approach by minimizing the energy expectation

$$
E [ \Psi ] = \frac {\langle \Psi | \hat {H} | \Psi \rangle}{\langle \Psi | \Psi \rangle}. \tag {10}
$$

The stochastic reconfiguration method [41], closely related to the natural gradient descent method [42] in unsupervised learning, is employed in the training progress to minimize the energy iteratively. During the training, the parameters at iteration $t$ are updated as

$$
\boldsymbol {p} _ {t + 1} = \boldsymbol {p} _ {t} - \gamma [ \operatorname {R e} (\mathbf {S} _ {t}) ] ^ {- 1} \boldsymbol {g} _ {t}, \tag {11}
$$

where $\gamma = 5 \times 1 0 ^ { - 4 }$ is the learning rate, $\mathbf { \pmb { g } }$ is the gradient of the energy $\partial _ { p } E$ ,

$$
g _ {a} = 2 \operatorname {R e} \left(\frac {\left\langle \partial_ {p _ {a}} \Psi \right| \hat {H} | \Psi \rangle}{\left\langle \Psi | \Psi \right\rangle} - E \frac {\left\langle \partial_ {p _ {a}} \Psi \right| \Psi \rangle}{\left\langle \Psi | \Psi \right\rangle}\right), \tag {12}
$$

and S is a precondition matrix

$$
\mathrm {S} _ {a b} = \frac {\left\langle \partial_ {p _ {a}} \Psi \right| \partial_ {p _ {b}} \Psi \rangle}{\left\langle \Psi | \Psi \right\rangle} - \frac {\left\langle \partial_ {p _ {a}} \Psi \right| \Psi \rangle}{\left\langle \Psi | \Psi \right\rangle} \frac {\left\langle \Psi \right| \partial_ {p _ {b}} \Psi \rangle}{\left\langle \Psi | \Psi \right\rangle}. \tag {13}
$$

Only the real part of $\mathbf { S }$ is employed because the parameters in the neural networks are realvalued. Moreover, to achieve a robust and efficient training process, the matrix elements S $a b$ associated with the mixed derivatives with respect to the parameters in the neural network $\eta$ and the parameters in other networks are neglected.

In practice, the precondition matrix S could be ill-conditioned, namely, with very small eigenvalues, and its inversion could lead to numerical instability. Therefore, the precondition

matrix is regularized by $\textbf { S } \to \textbf { S } + \epsilon \mathrm { d i a g } ( \sqrt { \pmb { v } _ { t } } + 1 0 ^ { - 8 } )$ with the regularization parameter $\epsilon = 1 0 ^ { - 3 }$ and $\pmb { v } _ { t } = \beta \pmb { v } _ { t - 1 } + ( 1 - \beta ) \pmb { g } _ { t } ^ { 2 }$ [34]. Here, ${ \pmb v } _ { t }$ accumulates the exponentially-decaying averages of the squared gradients and $\beta$ is the exponential decay factor taken to be 0.9. In addition, a constraint on the Fubini-Study distance between the wave functions of two adjacent iterations

$$
d _ {\mathrm {F S}} \left[ \Psi (\boldsymbol {p} ^ {t + 1}), \Psi (\boldsymbol {p} ^ {t}) \right] = \arccos  \sqrt {\frac {| \langle \Psi (\boldsymbol {p} ^ {t + 1}) | \Psi (\boldsymbol {p} ^ {t}) \rangle | ^ {2}}{\langle \Psi (\boldsymbol {p} ^ {t}) | \Psi (\boldsymbol {p} ^ {t}) \rangle \langle \Psi (\boldsymbol {p} ^ {t + 1}) | \Psi (\boldsymbol {p} ^ {t + 1}) \rangle}} <   d _ {\max }, \tag {14}
$$

is employed to prevent accidental large changes of the parameters that might lead to instability. The limit $d _ { \mathrm { m a x } }$ is initially set to be 0.1 and lowered to 0.05 when the iteration nearly converges.

At each iteration, a large set of configuration samples $( \pmb { x } _ { 1 } ^ { ( n ) } , \dots , \pmb { x } _ { A } ^ { ( n ) } )$ x(nA with $n = 1 , \ldots , N$ is generated following the probability distribution $| \Psi | ^ { 2 }$ by the standard Metropolis Monte Carlo sampling [43]. Then, the energy expectation $E$ , gradient $\mathbf { \pmb { g } }$ , and precondition matrix S are evaluated on these samples as in conventional variational Monte Carlo approaches,

$$
E = \mathrm {R e} \langle E ^ {(n)} \rangle ,
$$

$$
g _ {a} = 2 \mathrm {R e} \left[ \langle O _ {a} ^ {* (n)} E ^ {(n)} \rangle - E \langle O _ {a} ^ {* (n)} \rangle \right], \tag {15}
$$

$$
\mathrm {S} _ {a b} = \langle O _ {a} ^ {* (n)} O _ {b} ^ {(n)} \rangle - \langle O _ {a} ^ {* (n)} \rangle \langle O _ {b} ^ {(n)} \rangle .
$$

Here, the brackets denote the averages over the $N$ configuration samples and

$$
E ^ {(n)} = \frac {\hat {H} \Psi \left(\boldsymbol {x} _ {1} ^ {(n)} , \dots , \boldsymbol {x} _ {A} ^ {(n)}\right)}{\Psi \left(\boldsymbol {x} _ {1} ^ {(n)} , \dots , \boldsymbol {x} _ {A} ^ {(n)}\right)}, \quad O _ {a} ^ {(n)} = \frac {\partial_ {p _ {a}} \Psi \left(\boldsymbol {x} _ {1} ^ {(n)} , \dots , \boldsymbol {x} _ {A} ^ {(n)}\right)}{\Psi \left(\boldsymbol {x} _ {1} ^ {(n)} , \dots , \boldsymbol {x} _ {A} ^ {(n)}\right)}. \tag {16}
$$

The derivatives of the wave function with respect to either the spatial coordinates or the neural-network parameters are calculated based on the automatic differentiation framework of TensorFlow [44].

# IV. NUCLEAR HAMILTONIAN

The nuclear Hamiltonian adopted in this work is derived within the pionless EFT, which is based on the tenet that the typical momenta of nucleons in nuclei are much smaller than the pion mass [3]. The nuclear Hamiltonian reads

$$
\hat {H} = \sum_ {i = 1} ^ {A} \frac {- \nabla_ {i} ^ {2}}{2 m _ {N}} + \sum_ {i <   j} v _ {i j} + \sum_ {i <   j <   k} V _ {i j k}, \tag {17}
$$

where $m _ { N }$ is the nucleon mass, $A$ the number of nucleons, $v _ { i j }$ the nucleon-nucleon ( $N N )$ interaction, and $V _ { i j k }$ the three-nucleon (3 $\mathcal { N }$ ) interaction. The $N N$ interactions consists of an electromagnetic (EM) term and charge-independent (CI) contact terms at leading order (LO) and additionally charge-dependent (CD) contact terms at next-to-leading-order (NLO),

$$
v _ {\mathrm {L O}} = v ^ {\mathrm {E M}} + v _ {\mathrm {L O}} ^ {\mathrm {C I}}, \tag {18}
$$

$$
v _ {\mathrm {N L O}} = v ^ {\mathrm {E M}} + v _ {\mathrm {L O}} ^ {\mathrm {C I}} + v _ {\mathrm {N L O}} ^ {\mathrm {C I}} + v _ {\mathrm {N L O}} ^ {\mathrm {C D}}.
$$

The Coulomb repulsion between finite-size (rather than point-like) protons is considered for $v ^ { \mathrm { E M } }$ [45]. The contact interactions are regularized by Gaussian cutoff functions [46], and can be conveniently expressed in terms of radial functions multiplying spin and isospin operators. The CI contact terms take the form

$$
v _ {\mathrm {L O}} ^ {\mathrm {C I}} (\boldsymbol {r} _ {i j}) = \sum_ {p = 1} ^ {4} v _ {\mathrm {L O}} ^ {p} (r _ {i j}) \mathcal {O} _ {i j} ^ {p}, \quad v _ {\mathrm {N L O}} ^ {\mathrm {C I}} (\boldsymbol {r} _ {i j}) = \sum_ {p = 1} ^ {8} v _ {\mathrm {N L O}} ^ {p} (r _ {i j}) \mathcal {O} _ {i j} ^ {p}, \tag {19}
$$

with $\pmb { r } _ { i j } = \pmb { r } _ { i } - \pmb { r } _ { j }$ , $r _ { i j } = | \boldsymbol { r } _ { i j } |$ , and Op=1,2,...,8ij = 1, τi · τj , σi · σj , σi · σj τi · τj , $S _ { i j }$ , $S _ { i j } \tau _ { i }$ · $\tau _ { j }$ , $L \cdot S , ~ L \cdot S \tau _ { i } \cdot \tau _ { j }$ . Here, $\sigma _ { i }$ ( $\tau _ { i }$ ) are the Pauli spin (isospin) matrices of the $i$ th nucleon, and $S _ { i j } = 3 \pmb { \sigma } _ { i } \cdot \hat { \pmb { r } } _ { i j } \pmb { \sigma } _ { i } \cdot \hat { \pmb { r } } _ { i j } - \pmb { \sigma } _ { i } \cdot \pmb { \sigma } _ { j }$ , $\pmb { L } = - \textstyle { \frac { 1 } { 2 } } \pmb { r } _ { i j } \times \left( \pmb { \nabla } _ { i } - \pmb { \nabla } _ { j } \right)$ , and $\begin{array} { r } { S = \frac 1 2 ( \pmb { \sigma } _ { i } + \pmb { \sigma } _ { j } ) } \end{array}$ are the tensor operator, the relative angular momentum, and the total spin of a pair of nucleons $( i , j )$ , respectively. Only central forces ( $p = 1$ -4) are present at LO, while the tensor and spin-orbit forces ( $p = 5$ -8) appear at NLO. The CD contact term at NLO takes the form

$$
v _ {\mathrm {N L O}} ^ {\mathrm {C D}} \left(\boldsymbol {r} _ {i j}\right) = v _ {\mathrm {N L O}} ^ {T} \left(r _ {i j}\right) T _ {i j}, \tag {20}
$$

with $\begin{array} { r } { T _ { i j } ^ { \prime } = 3 \tau _ { i z } \tau _ { j z } - \pmb { \tau _ { i } } \cdot \pmb { \tau _ { j } } } \end{array}$ being the isotensor operator of the nucleon pair $( i , j )$ . The specific expressions of the radial functions in Eqs. (19) and (20) can be found in Ref. [46].

The regularized $3 N$ contact interaction reads

$$
V _ {i j k} \left(r _ {i j}, r _ {j k}, r _ {k i}\right) = \frac {c _ {E}}{f _ {\pi} ^ {4} \Lambda_ {\chi}} \frac {\left(\hbar c\right) ^ {6}}{\pi^ {3} R _ {3} ^ {6}} \sum_ {\text {c y c}} \mathrm {e} ^ {- \left(r _ {i j} ^ {2} + r _ {j k} ^ {2}\right) / R _ {3} ^ {2}}, \tag {21}
$$

where $\Lambda _ { \chi } ~ = ~ 1$ GeV, $f _ { \pi } ~ = ~ 9 2 . 4$ MeV is the pion decay constant, $c _ { E }$ is a three-nucleon low-energy constant (LEC), and $\sum \mathrm { _ { c y c } }$ stands for the cyclic permutation of $i , j , k$ .

The LECs in the nuclear Hamiltonian are adjusted to the experimental $N N$ scattering data and $^ 3 \mathrm { H }$ binding energy [46], and we use the optimal set (model “o”) with $R _ { 3 } = 1 . 0$ fm at LO and $R _ { 3 } = 2 . 0$ fm at NLO given in Ref. [46] that was proved to yield reasonably well ground-state energies for several light- and medium-mass nuclei [46].

The range of the adopted $N N$ is typically 2 fm, so we use this value for $R$ in the backflow neural network in Eq. (3). In addition, for the LO Hamiltonian, only the real part of the FeynmanNet wave function is needed as the tensor and spin-orbit forces are not present [Eq. (19)].

# V. RESULTS AND DISCUSSION

Figure 2 depicts the performance of FeynmanNet by taking $^ 4$ He, $_ 6$ Li and $^ { 1 6 }$ O as examples. The FeynmanNet results here are obtained using $N _ { \mathrm { d e t } } = 4$ determinants. For $^ 4$ He and $_ 6$ Li, the obtained ground-state energies are compared with the results given by the previous ANN Slater-Jastrow (ANN-SJ) ansatz and the HH method [33]. The former works only for the LO Hamiltonian, while the latter is valid for both LO and NLO Hamiltonians and, more importantly, is numerically exact for $s$ -shell nuclei, e.g., 4He. For the 4He ground-state energy at LO (Fig. 2a), FeynmanNet provides lower energy than the ANN-SJ ansatz after training for only about 200 iterations, and the final result is also consistent with the numerically exact HH value. This indicates that FeynmanNet outperforms the ANN-SJ ansatz by introducing the multiple determinants and backflow transformation, which improves the nodal surface in both continuous spatial and discrete spin-isospin spaces. Note that the extra energy given by FeynmanNet grows dramatically for heavier nuclei, e.g., about 7 MeV for $^ { 1 6 }$ O (see the MD-SJ result with $N _ { \mathrm { d e t } } = 1$ in Fig. 4c).

The experimental value of $^ 4$ He ground-state energy is $- 2 8 . 3 0$ MeV, slightly lower than the HH value, $- 2 8 . 1 7$ MeV [33]. However, since the HH method provides a numerically exact solution of the Schr¨odinger equation for $^ 4$ He, this discrepancy originates from the model of the nuclear force, which is out of the scope for this work.

Unlike the $s$ -shell nucleus 4He, the $p$ -shell nucleus $_ 6$ Li is strongly clustered in an $\alpha$ particle and a deuteron, and such a cluster structure brings additional complexity in the calculations. As a result, the HH result for $_ 6$ Li is not as accurate as that for $^ 4$ He [47]. FeynmanNet converges to the lowest ground-state energies for $_ 6$ Li in comparison with the ANN-SJ and HH results (Fig. 2b), which are respectively higher by about 500 keV and 300 keV than the FeynmanNet energy.

The expressive power of FeynmanNet is further highlighted for a larger system $^ { 1 6 }$ O. Such a system is too large for the HH method, so we benchmark our results with the AFDMC

![](images/c5d8c50a30ffdd858e65ccde2b774bb88959995b15a1122dba6c65698c9fd4e9.jpg)  
FIG. 2. (Color online). Performance of FeynmanNet on the 4He, $_ 6$ Li, and $^ { 1 6 }$ O ground states. (a) The $^ 4$ He energy, calculated with the pionless effective field theory Hamiltonian at leading order (LO), as a function of the iterations in the training progress of FeynmanNet. The statistical errors of the energies from the Metropolis Monte Carlo sampling are shown by error bars. The solid line is obtained by applying exponential moving average to the energies. The ground-state energies given by the artificial neural network with Slater-Jastrow (ANN-SJ) ansatz and the hypershpericalharmonics (HH) method [33] are displayed for comparison. (b) Same as (a) but for $_ 6$ Li. The ANN-SJ and HH results are displayed, with shadow areas indicating the corresponding statistical and extrapolation errors, respectively. (c) Same as (a) but for $^ { 1 6 }$ O. The ground-state energy provided by the auxiliary-field diffusion Monte Carlo (AFDMC) method [46] is displayed with shadow areas indicating the statistical error. (d) Same as (a) but with the Hamiltonian at next-to-leading-order (NLO). The results of FeynmanNet with the LO and NLO Hamiltonians are shown in blue and orange, respectively.

approach [46]. One can see that the energy given by FeynmanNet is lower than the AFDMC energy by more than 1 MeV (Fig. 2c). Note that the AFDMC calculations adopt the constrained-path approximation to mitigate the fermion-sign problem in imaginary-time propagations, and therefore could not solve the ground state exactly [48]. In contrast, the strong expressive power of FeynmanNet allows a variational approach to reach accurate solutions without performing imaginary-time propagations.

Moreover, the calculation of $^ 4$ He with the NLO Hamiltonian demonstrates the ability of FeynmanNet to deal with tensor and spin-orbit forces (Fig. 2d). The NLO Hamiltonian has lower symmetries than the LO one. At LO, the spatial and spin angular momenta, namely $\pmb { L }$ and $S$ , are respectively conserved in addition to the total angular momentum $\pmb { J }$ . However, they are broken by the tensor and spin-orbit forces introduced at NLO. Despite these difficulties, it is remarkable that the number of iterations for convergence of FeynmanNet at NLO is similar to that at LO. FeynmanNet reaches an accuracy of $\simeq 5 0$ keV after training for only 200 iterations, and the energy obtained after 500 iterations is consistent with the HH value within 30 keV.

In addition to accurate ground-state energies, FeynmanNet also provides a whole solution of the nuclear many-body wave function that, in principle, gives access to all ground-state properties. To elucidate the quality of FeynmanNet wave function, the obtained pointnucleon densities of the $^ 4$ He, $_ 6$ Li, and $^ { 1 6 }$ O ground states are shown in Fig. 3. The pointnucleon densities are calculated as

$$
\rho_ {N} (r) = \frac {1}{4 \pi r ^ {2}} \frac {\langle \Psi | \sum_ {i = 1} ^ {A} \delta (\bar {r} _ {i} - r) | \Psi \rangle}{\langle \Psi | \Psi \rangle}, \tag {22}
$$

where $r _ { i }$ are the distance from the $i$ th nucleon to the center of mass and $\Psi$ taken to be the FeynmanNet wave function after convergence. The obtained point-nucleon densities are compared to the previous results with the LO Hamiltonian given by the ANN-SJ ansatz and HH method for $^ 4$ He and $_ 6$ Li [33] and AFDMC method for $^ { 1 6 }$ O [34]. Note that the HH method is also valid for 4He with the NLO Hamiltonian, but we have not found the results of point-nucleon density from the literature.

Similar to the energy, the FeynmanNet point-nucleon density for $^ 4$ He is in an excellent agreement with the HH result (Fig. 3a). For $_ 6$ Li, FeynmanNet provides not only the lowest ground-state energy but also a significantly more compact point-nucleon density than the ANN-SJ ansatz and the HH method (Fig. 3b). For $^ { 1 6 }$ O, the point-nucleon density given

![](images/aa8945ea9df0ca4e918faa456d22fac9e2c223e91b65fb30bcbfd808ba46d6c2.jpg)  
FeynmanNet HH ANN-SJ AFDMC

![](images/389001b6c2bf49f43e31a0fd9010818f3633d8b8afe3d024df9af74e8dc2a489.jpg)

![](images/d6400045e4e08a3075dd2812033603f73629ea1c791110bd54cf0da7d6b6dba9.jpg)

![](images/66de9da75b0df117f4e2a226c47dbcc6a3d6d854dea25c968b53daeb6b1f0652.jpg)  
FIG. 3. (Color online). Point-nucleon densities of the $^ 4$ He, $_ 6$ Li, and $^ { 1 6 }$ O ground states obtained with FeynmanNet. The results for the LO and NLO pionless EFT Hamiltonians are shown in blue and orange, respectively. The statistical errors from the Metropolis Monte Carlo sampling are smaller than the points. For the LO Hamiltonian, also shown are the point-nucleon densities given by the ANN-SJ ansatz and the HH method for 4He and $_ 6$ Li [33] and the AFDMC method for $^ { 1 6 }$ O [34].

by FeynmanNet is very close to the AFDMC one (Fig. 3c). These results corroborate once again the accuracy of FeynmanNet in representing nuclear wave functions. In the future, we envisage wide applications of FeynmanNet in realistic nuclear structure studies of nuclear momentum distributions, form factors, currents, etc.

Figure 4 highlights the specific roles of multiple Slater determinants, the Jastrow factor, and the backflow transformation in capturing nuclear many-body correlations. We compare the $^ 4$ He and $^ { 1 6 }$ O ground-state energies obtained with FeynmanNet and its two simpler vari-

![](images/1a558f9bf5c63b40ef6fe9a8857d9a6a1c27e6cf297554166e5fa23aab7e7d85.jpg)

![](images/128a02b4bb634828c14c7e58907954b012f74c4145900dda5a0f18e5a87a0329.jpg)

![](images/de5ed47c6dbbd38f22462594f5a627227e8e0e72154304901fdc62429ddfc002.jpg)  
FIG. 4. (Color online). Roles of the number of determinants, Jastrow factor, and backflow transformation in FeynmanNet. The ground-state energies of $^ 4$ He and $^ { 1 6 }$ O, obtained with the ansatz of multiple Slater determinants (MD) alone and in combination with the Jastrow factor (SJ) and an optional backflow transformation (BF), are shown as functions of the number of the determinants $N _ { \mathrm { d e t } }$ . The numerically exact results for $^ 4$ He from the HH method [33] are shown by the black dashed line. The result for $^ { 1 6 }$ O from the AFDMC method [46] is displayed by the green dash-dotted line and the shadow area indicating its statistical error.

ants without the backflow transformation and additionally the Jastrow factor. For 4He at LO (Fig. 4a), the result obtained using the ansatz of one Slater determinant alone is higher than the HH energy by about 800 keV, and this deviation can be nicely removed by the consideration of Jastrow correlations. While both the Jastrow factor and the multiple Slater determinants are crucial to improve the energy at NLO (Fig. 4b), the energy deviation from the exact value remains about 300 keV with $N _ { \mathrm { d e t } } = 4$ , which can only be further reduced by taking into account the backflow transformation. This should be attributed to the more complicated nodal surface of the nuclear wave function with the NLO Hamiltonian, arising from the presence of tensor and spin-orbit forces. The Jastrow factor can compactly incorporate many-body correlations, but cannot modify the nodal surface of the Slater determinants due to its nonnegative feature. Therefore, the backflow transformation plays a crucial role in improving the nodal surface and reaching a significantly higher accuracy.

The importance of the backflow transformation is even more evident in the larger nucleus $^ { 1 6 }$ O. As seen in Fig. 4c, the backflow transformation lowers the Slater-Jastrow energy by about 7 MeV and achieves, with just one determinant, an energy similar to the AFDMC

result. By increasing the number of the determinants $N _ { \mathrm { d e t } }$ , the calculated energy is further lowered by about 1 MeV.

# VI. SUMMARY

We have developed FeynmanNet, a deep-learning QMC approach aiming to solve the ab initio nuclear many-body problems, and demonstrated that it can provide very accurate solutions of $^ 4$ He, $_ 6$ Li, and $^ { 1 6 }$ O ground-state energies and wave functions emerging from the LO and NLO Hamiltonians from pionless EFT. By introducing a well-designed backflow transformation, it outperforms the previous ANN Slater-Jastrow wave functions in not only the higher accuracy but also the nice compatibility with the Hamiltonian containing tensor and spin-orbit forces, which induce a complicated nodal surface of the wave function in the spatial and spin-isospin space. Compared to the conventional nuclear QMC approaches, Feynman-Net has a more favorable polynomial scaling instead of an exponential scaling. Moreover, the strong expressive power of the deep neural networks in FeynmanNet allows a variational approach to reach or even exceed the accuracy of diffusion Monte Carlo method and, thus, avoids the imaginary-time propagations that suffer from the severe inherent fermion-sign problem. Therefore, FeynmanNet is a promising ab initio method that can accurately solve light and medium-mass nuclei. Note that the adopted Hamiltonians in the present work are based on the relatively simplified pionless EFT. In the future, we plan to adopt more realistic and sophisticated chiral EFT interactions.

# ACKNOWLEDGMENTS

This work has been supported in part by the National Key R&D Program of China (Contract No. 2018YFA0404400),the National Natural Science Foundation of China (Grants No. 12070131001, No. 11875075, No. 11935003, No. 11975031, No. 12141501), and the High-performance Computing Platform of Peking University.

[2] S. Weinberg, Effective chiral lagrangians for nucleon-pion interactions and nuclear forces, Nucl. Phys. B 363, 3 (1991).   
[3] H.-W. Hammer, S. K¨onig, and U. van Kolck, Nuclear effective field theory: Status and perspectives, Rev. Mod. Phys. 92, 025004 (2020).   
[4] E. Epelbaum, H.-W. Hammer, and U.-G. Meißner, Modern theory of nuclear forces, Rev. Mod. Phys. 81, 1773 (2009).   
[5] R. Machleidt and D. Entem, Chiral effective field theory and nuclear forces, Phys. Rep. 503, 1 (2011).   
[6] A. Gezerlis, I. Tews, E. Epelbaum, S. Gandolfi, K. Hebeler, A. Nogga, and A. Schwenk, Quantum Monte Carlo Calculations with Chiral Effective Field Theory Interactions, Phys. Rev. Lett. 111, 032501 (2013).   
[7] E. Epelbaum, H. Krebs, and U.-G. Meißner, Precision Nucleon-Nucleon Potential at Fifth Order in the Chiral Expansion, Phys. Rev. Lett. 115, 122301 (2015).   
[8] F. Wienholtz, D. Beck, K. Blaum, C. Borgmann, M. Breitenfeldt, R. B. Cakirli, S. George, F. Herfurth, J. D. Holt, M. Kowalska, S. Kreim, D. Lunney, V. Manea, J. Men´endez, D. Neidherr, M. Rosenbusch, L. Schweikhard, A. Schwenk, J. Simonis, J. Stanja, R. N. Wolf, and K. Zuber, Masses of exotic calcium isotopes pin down nuclear forces, Nature 498, 346 (2013).   
[9] G. Hagen, A. Ekstrom, C. Forssen, G. R. Jansen, W. Nazarewicz, T. Papenbrock, K. A. Wendt, S. Bacca, N. Barnea, B. Carlsson, C. Drischler, K. Hebeler, M. Hjorth-Jensen, M. Miorelli, G. Orlandini, A. Schwenk, and J. Simonis, Neutron and weak-charge distributions of the $^ { 4 8 }$ Ca nucleus, Nat. Phys. 12, 186 (2016).   
[10] B. Hu, W. Jiang, T. Miyagi, Z. Sun, A. Ekstr¨om, C. Forss´en, G. Hagen, J. D. Holt, T. Papenbrock, S. R. Stroberg, and I. Vernon, Ab initio predictions link the neutron skin of $^ { 2 0 8 }$ Pb to nuclear forces, Nat.Phys. 10.1038/s41567-022-01715-8 (2022).   
[11] P. Gysbers, G. Hagen, J. D. Holt, G. R. Jansen, T. D. Morris, P. Navr´atil, T. Papenbrock, S. Quaglioni, A. Schwenk, S. R. Stroberg, and K. A. Wendt, Discrepancy between experimental and theoretical $\beta$ -decay rates resolved from first principles, Nat. Phys. 15, 428 (2019).   
[12] S. Elhatisari, D. Lee, G. Rupak, E. Epelbaum, H. Krebs, T. A. L¨ahde, T. Luu, and U.-G. Meißner, Ab initio alpha-alpha scattering, Nature 528, 111 (2015).   
[13] P. Ring and P. Schuck, The Nuclear Many-Body Problem, 3rd ed. (Springer-Verlag Berlin Heidelberg, 2004).

[14] J. Carlson, S. Gandolfi, F. Pederiva, S. C. Pieper, R. Schiavilla, K. E. Schmidt, and R. B. Wiringa, Quantum Monte Carlo methods for nuclear physics, Rev. Mod. Phys. 87, 1067 (2015).   
[15] B. S. Pudliner, V. R. Pandharipande, J. Carlson, and R. B. Wiringa, Quantum Monte Carlo Calculations of $A \leq 6$ Nuclei, Phys. Rev. Lett. 74, 4396 (1995).   
[16] R. B. Wiringa and S. C. Pieper, Evolution of Nuclear Spectra with Nuclear Forces, Phys. Rev. Lett. 89, 182501 (2002).   
[17] A. Lovato, S. Gandolfi, R. Butler, J. Carlson, E. Lusk, S. C. Pieper, and R. Schiavilla, Charge Form Factor and Sum Rules of Electromagnetic Response Functions in $^ { 1 2 } \mathbf { C }$ , Phys. Rev. Lett. 111, 092501 (2013).   
[18] M. Piarulli, A. Baroni, L. Girlanda, A. Kievsky, A. Lovato, E. Lusk, L. E. Marcucci, S. C. Pieper, R. Schiavilla, M. Viviani, and R. B. Wiringa, Light-Nuclei Spectra from Chiral Dynamics, Phys. Rev. Lett. 120, 052503 (2018).   
[19] S. Gandolfi, F. Pederiva, S. Fantoni, and K. E. Schmidt, Auxiliary Field Diffusion Monte Carlo Calculation of Nuclei with $ { \begin{array} { r l r l } { A } & { { } \leq } & { 4 0 } \end{array} }$ with Tensor Interactions, Phys. Rev. Lett. 99, 022507 (2007).   
[20] D. Lonardoni, J. Carlson, S. Gandolfi, J. E. Lynn, K. E. Schmidt, A. Schwenk, and X. B. Wang, Properties of Nuclei up to $\begin{array} { r l r } { A } & { { } = } & { 1 6 } \end{array}$ using Local Chiral Interactions, Phys. Rev. Lett. 120, 122502 (2018).   
[21] M. Troyer and U.-J. Wiese, Computational Complexity and Fundamental Limitations to Fermionic Quantum Monte Carlo Simulations, Phys. Rev. Lett. 94, 170201 (2005).   
[22] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld, N. Tishby, L. Vogt-Maranto, and L. Zdeborov´a, Machine learning and the physical sciences, Rev. Mod. Phys. 91, 045002 (2019).   
[23] G. Carleo and M. Troyer, Solving the quantum many-body problem with artificial neural networks, Science 355, 602 (2017).   
[24] M. Ruggeri, S. Moroni, and M. Holzmann, Nonlinear Network Description for Many-Body Quantum Systems in Continuous Space, Phys. Rev. Lett. 120, 205302 (2018).   
[25] J. Han, L. Zhang, and W. E, Solving many-electron Schr¨odinger equation using deep neural networks, J. Comput. Phys. 399, 108929 (2019).

[26] D. Pfau, J. S. Spencer, A. G. D. G. Matthews, and W. M. C. Foulkes, Ab initio solution of the many-electron Schr¨odinger equation with deep neural networks, Phys. Rev. Research 2, 033429 (2020).   
[27] J. Hermann, Z. Sch¨atzle, and F. No´e, Deep-neural-network solution of the electronic Schr¨odinger equation, Nat. Chem. 12, 891 (2020).   
[28] K. Choo, A. Mezzacapo, and G. Carleo, Fermionic neural-network states for ab-initio electronic structure, Nature Communications 11, 2368 (2020).   
[29] M. Scherbela, R. Reisenhofer, L. Gerard, P. Marquetand, and P. Grohs, Solving the electronic Schr¨odinger equation for multiple nuclear geometries with weight-sharing deep neural networks, Nat. Comp. Sci. 2, 331 (2022).   
[30] A. Boehnlein, M. Diefenthaler, N. Sato, M. Schram, V. Ziegler, C. Fanelli, M. Hjorth-Jensen, T. Horn, M. P. Kuchera, D. Lee, W. Nazarewicz, P. Ostroumov, K. Orginos, A. Poon, X.-N. Wang, A. Scheinker, M. S. Smith, and L.-G. Pang, Colloquium: Machine learning in nuclear physics, Rev. Mod. Phys. 94, 031003 (2022).   
[31] J. Keeble and A. Rios, Machine learning the deuteron, Phys. Lett. B 809, 135743 (2020).   
[32] C. Adams, G. Carleo, A. Lovato, and N. Rocco, Variational Monte Carlo Calculations of $ { \boldsymbol { A } } \quad \leq \quad  { \boldsymbol { 4 } }$ Nuclei with an Artificial Neural-Network Correlator Ansatz, Phys. Rev. Lett. 127, 022502 (2021).   
[33] A. Gnech, C. Adams, N. Brawand, G. Carleo, A. Lovato, and N. Rocco, Nuclei with Up to $A =$ 6 Nucleons with Artificial Neural Network Wave Functions, Few-Body Systems 63, 7 (2021).   
[34] A. Lovato, C. Adams, G. Carleo, and N. Rocco, Hidden-nucleons neural-network quantum states for the nuclear many-body problem, Phys. Rev. Research 4, 043178 (2022).   
[35] R. P. Feynman and M. Cohen, Energy Spectrum of the Excitations in Liquid Helium, Phys. Rev. 102, 1189 (1956).   
[36] D. Luo and B. K. Clark, Backflow Transformations via Neural Networks for Quantum Many-Body Wave Functions, Phys. Rev. Lett. 122, 226401 (2019).   
[37] Y. Yang and P. Zhao, A consistent description of the relativistic effects and three-body interactions in atomic nuclei, Phys. Lett. B 835, 137587 (2022).   
[38] M. Zaheer, S. Kottur, S. Ravanbakhsh, B. Poczos, R. Salakhutdinov, and A. Smola, Deep Sets, arXiv:1703.06114 (2018).

[39] E. Wagstaff, F. B. Fuchs, M. Engelcke, I. Posner, and M. Osborne, On the Limitations of Representing Functions on Sets, arXiv:1901.09006 (2019).   
[40] C. Dugas, Y. Bengio, F. B´elisle, C. Nadeau, and R. Garcia, Incorporating second-order functional knowledge for betteroption pricing (MIT Press. Cambridge, MA, 2001, 2001) Chap. Advances in Neural Information Processing Systems 13, pp. 472–478.   
[41] S. Sorella, Wave function optimization in the variational Monte Carlo method, Phys. Rev. B 71, 241103 (2005).   
[42] S.-i. Amari, Natural Gradient Works Efficiently in Learning, Neural Computation 10, 251 (1998).   
[43] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, Equation of State Calculations by Fast Computing Machines, The Journal of Chemical Physics 21, 1087 (1953).   
[44] M. Abadi, A. Agarwal, P. Barham, E. Brevdo, Z. Chen, C. Citro, G. S. Corrado, A. Davis, J. Dean, M. Devin, S. Ghemawat, I. Goodfellow, A. Harp, G. Irving, M. Isard, Y. Jia, R. Jozefowicz, L. Kaiser, M. Kudlur, J. Levenberg, D. Man´e, R. Monga, S. Moore, D. Murray, C. Olah, M. Schuster, J. Shlens, B. Steiner, I. Sutskever, K. Talwar, P. Tucker, V. Vanhoucke, V. Vasudevan, F. Vi´egas, O. Vinyals, P. Warden, M. Wattenberg, M. Wicke, Y. Yu, and X. Zheng, TensorFlow: Large-scale machine learning on heterogeneous systems (2015), software available from tensorflow.org.   
[45] R. B. Wiringa, V. G. J. Stoks, and R. Schiavilla, Accurate nucleon-nucleon potential with charge-independence breaking, Phys. Rev. C 51, 38 (1995).   
[46] R. Schiavilla, L. Girlanda, A. Gnech, A. Kievsky, A. Lovato, L. E. Marcucci, M. Piarulli, and M. Viviani, Two- and three-nucleon contact interactions and ground-state energies of lightand medium-mass nuclei, Phys. Rev. C 103, 054003 (2021).   
[47] A. Gnech, M. Viviani, and L. E. Marcucci, Calculation of the $_ 6$ Li ground state within the hyperspherical harmonic basis, Phys. Rev. C 102, 014001 (2020).   
[48] R. B. Wiringa, S. C. Pieper, J. Carlson, and V. R. Pandharipande, Quantum Monte Carlo calculations of $A = 8$ nuclei, Phys. Rev. C 62, 014001 (2000).