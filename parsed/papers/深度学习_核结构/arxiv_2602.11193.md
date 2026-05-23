# Addressing the ground state of the deuteron by physics-informed neural networks

Lorenzo Brevi a, Antonio Mandarino a,b, Carlo Barbieri a,c, Enrico Prati a,c

aDipartimento di Fisica "Aldo Pontremoli", Università degli studi di Milano, Via Celoria 16, Milano, 20133, Italy bInternational Centre for Theory of Quantum Technologies, University of Gdansk, Jana Ba˙zy´nskiego 1A, Gda´nsk, 80-309, Poland cINFN, Sezione di Milano, Via Celoria 16, Milano, 20133, Italy

# Abstract

Machine learning techniques have proven to be effective in addressing the structure of atomic nuclei. Physics−Informed Neural Networks (PINNs) are a promising machine learning technique suitable for solving integro-differential problems such as the manybody Schrödinger problem. So far, there has been no demonstration of extracting nuclear eigenstates using such method. Here, we tackle realistic nucleon-nucleon interaction in momentum space, including models with strong high-momentum correlations, and demonstrate highly accurate results for the deuteron. We further provide additional benchmarks in coordinate space. We introduce an expression for the variational energy that enters the loss function, which can be evaluated efficiently within the PINNs framework. Results are in excellent agreement with proven numerical methods, with a relative error between the value of the predicted binding energy by the PINN and the numerical benchmark of the order of $1 0 ^ { - 6 }$ . Our approach paves the way for the exploitation of PINNs to solve more complex atomic nuclei.

Keywords: Physics Informed Neural Network, Neural Network Quantum States, Ab Initio Nuclear Theory

# 1. Introduction

Machine learning (ML) techniques have increasingly impacted the physical sciences in recent years, in some cases being able to outperform more traditional computational methods [1], while in others providing novel approaches to solve scientific problems [2]. The opportunity to directly solve quantum[ many-body systems was realized for the first time for the spin lattice [3]. Neural networks can be used to represent wavefunctions of complex quantum systems, by leveraging the property of exceptionally efficient universal approximators [4, 5, 6]. The combination of the variational principle with machine learning optimization techniques makes it possible to find the true ground state of the system through recursive computation and minimization of the expectation value of the Hamiltonian operator. Such approach, known as neural network quantum states (NQS), can be considered an extension of the variational Monte Carlo (VMC) method and has a similar computational cost, but it can achieve significantly higher accuracy. The NQS framework has since been enhanced through successful applications in solid-state physics [7] and quantum chemistry [8], often reaching comparable accuracy to the computationally much more expensive diffusion Monte Carlo (DMC) method. Recent developments have addressed the computation of the first lowlying excited molecular states [9] and have been extended to advanced deep learning architectures such as transformers [10]. NQS-based simulations are typically more complicated for nuclear physics, due to the complexity of the nuclear force among protons and neutrons [11, 12]. Ref. [13] provided a first proofof-principle for the deuteron – the simplest nucleus formed by

one neutron and one proton – in terms of standard feed-forward networks. The research was later extended to few-nucleon systems using Jastrow inspired networks [14] and an adaptation of the FermiNet [15] architecture to nuclei [16]. In general, nuclear structure theory highly benefits from innovation in ab initio nuclear many-body methods. Some of us have recently addressed diagrammatic Monte Carlo methods [17] and quantum algorithms for determining the energy spectrum of nuclei [18, 19, 20].

The NQS approach is best classified as reinforcement learning because no training or target data is provided to learn about many-body correlations. Rather, the algorithm samples directly the expectation value of the Hamiltonian and uses the variational principle as a guiding rule to constrain the wave function. Because of this feature, NQS could also be referred to as science-driven learning. Yet, it relies on only one piece of physics information, the variational principle, to learn about the quantum many-body structure. The latter limitation could be overcome by exploiting physics-informed neural networks (PINNs), introduced in Ref. [21] to solve partial differential equations (PDEs). The PINN framework focuses on integrating all possible physical knowledge of the problem into the loss function of the network. In most cases, it includes boundary conditions and physical symmetries as well as measured data points where the solution is partially known, making the approach particularly suited to studies of fluid dynamics [22, 23, 24]. However, PINNs can solve differential equations by exploiting the sole physical constraints of the system. Exploratory applications to the Schrödinger equation focused on one-dimensional elementary systems [25, 26]. More recently, some of us have employed PINNs to solve for both the

ground state and excited states of the anharmonic oscillator, a non-trivial and non-integrable quantum system [27, 28].

Here we solve for the ground state of the deuteron based on the PINN framework. We introduce a new strategy to compute eigenenergies that is a natural extension of the standard PINN approach. The improvement allows us to tackle realistic models of the nucleon-nucleon interaction in momentum space, even with strong high-momentum correlations, and obtain highly accurate benchmarks. We also provide an example of analogous simulations in coordinate space. To our knowledge, these are the first applications of PINNs to an ab initio nuclear structure problem.

Section 2 gives an overview of the PINN method and the techniques for training its networks. Sec. 2.1 describes the metrics used to quantify the accuracy of our solutions. Next, Secs. 3.1 and 3.2 reports on the computations in coordinate and momentum space, respectively. All results are discussed in Sec. 3.3.

# 2. Physics-Informed neural network for the eigenvalue problem

We discuss the implementation of PINNs for solving the Schrödinger’s equation, emphasizing the novelties introduced to better converge its eigenvalues. For a more in-depth review refer to previous work on the subject [28, 27]. A generic Physics-informed neural network is made to encode all prior knowledge about the physical system, including the differential equation itself that one aims at solving [21]. The general form for its loss function is

$$
\mathcal {L} _ {P I N N} = \mathcal {L} _ {P D E} + \mathcal {L} _ {p h y s} + \mathcal {L} _ {\text {d a t a}}, \tag {1}
$$

where $\mathcal { L } _ { d a t a }$ is the standard training loss of a supervised problem, given as the discrepancy between its output and training labels. This is omitted in our computations since we do not have data points. $\mathcal { L } _ { p h y s }$ encodes to the losses given by the physical constraints of the system, such as boundary conditions and initial conditions. Lastly, $\mathcal { L } _ { P D E }$ is the mean squared error or sum of squared errors of the differential equation. For instance, consider a generic PDE written in terms of its implicit solution $\mu ( t )$ and the derivative $\partial _ { t } \mu ( t )$ with the independent variable $t$ :

$$
\partial_ {t} \mu (t) + N [ \mu ; \xi ] = 0, \tag {2}
$$

where $N$ is a nonlinear operator and $\xi$ is some set of parameters. Then, one can write $\mathcal { L } _ { P D E }$ ξfor a network designed to solve this equation as:

$$
\mathcal {L} _ {P D E} = \frac {1}{N _ {c}} \sum_ {i = 1} ^ {N _ {c}} \left(\partial_ {t} \mu_ {\text {n e t}} \left(x _ {i}\right) + N \left[ \mu_ {\text {n e t}} \left(x _ {i}\right); \xi \right]\right) ^ {2} \tag {3}
$$

where $x _ { i }$ is the set of $N _ { c }$ chosen collocation points where the PDE will be evaluated. Partial derivatives can be computed exploiting the same automatic differentiation techniques used to train the weights of standard neural networks. Here, we also consider the derivatives of functions of the neural network with respect to its inputs.

This approach enables the training of neural networks with noisy or very little data, and even in the absence of labeled data as in this work. The eigenfunction and the corresponding eigenvalue of the deuteron must satisfy certain constraints, including boundary conditions, the normalization of the wavefunction, and the condition that it solves the Schrödinger’s equation. In addition, we impose that the solution minimizes the energy since the deuteron has no bound excitations and we are only targeting the ground state. In this work we focus on the radial Schrödinger equation, but the generalization to several spatial dimensions is straightforward.

Hence, the PINN wavefunction $\psi ( x )$ is computed in a onedimensional interval, $x \in [ 0 , M ]$ ψ, where $x$ is the radial coordi-,nate in either position or momentum space. The physical constraint due to boundary conditions is encoded in the loss function1

$$
\mathcal {L} _ {B C s} = \frac {N _ {c}}{2} \left(| \phi (x = 0) | ^ {2} + | \psi (x = M) | ^ {2}\right), \tag {4}
$$

where $\phi ( x ) ~ = ~ x \psi ( s )$ is used to impose the correct boundary ϕ ψcondition for partial waves of angular momentum $L = 0$ . The second term in Eq. (4) ensures that the wavefunction vanishes at large distances, as expected for bound states.

The normalization condition is imposed on the integral

$$
\mathcal {I} [ \psi ] = 4 \pi \int_ {0} ^ {M} | \psi (x) | ^ {2} x ^ {2} d x \tag {5}
$$

and can be implemented in two different ways. First, for the spatial coordinate case of Sec. 3.1 we follow the auxiliary output method from Ref. [29]. We add one additional output, $\nu ( x )$ , νto the neural network that will be trained to reproduce the integral

$$
\nu (x) = \int_ {0} ^ {x} | \psi \left(x ^ {\prime}\right) | ^ {2} \left(x ^ {\prime}\right) ^ {2} d x ^ {\prime}, \tag {6}
$$

so that ${ \mathcal { I } } [ \psi ] = 4 \pi \nu ( M )$ . This new network output is trained by ψ π νintroducing the partial ‘integration’ loss

$$
\mathcal {L} _ {i n t} = \sum_ {i = 0} ^ {N _ {c}} \left(\left| \partial_ {x} v (x _ {i}) - x ^ {2} | \psi (x _ {i}) | ^ {2} \right| + | \min  (0, \partial_ {x} v (x _ {i})) |\right) ^ {2}. \tag {7}
$$

This allows to compute the normalization integral in a meshfree way, but at the cost of additional computational overhead. The last term in parentheses in Eq. (7) imposes that the output $\nu ( x )$ is monotonically increasing, as expected from Eq. (6).

The second approach to the normalization consists in computing Eq. (5) directly from finite difference methods and it will be employed in Sec. 3.2. This results in less computationally demanding effort but, conversely, it can introduce discretization errors. The decision of which of the two methods may result more effective depends on a case-by-case basis. Regardless of how ${ \cal T } [ \psi ]$ has been computed, we obtain the normalization loss

$$
\mathcal {L} _ {\text {n o r m}} = N _ {c} \left(| \mathcal {I} [ \psi ] - \ln (\mathcal {I} [ \psi ]) - 1 | + | \nu (0) |\right), \tag {8}
$$

where the last term in parentheses is used only with the auxiliary output and ensures that $\int _ { 0 } ^ { 0 } \| \psi ( x ) \| ^ { 2 } \ d x = { \mathrm { ~ } } 0$ . Note that the ψlogarithm term in Eq. (8), even if not mandatory, produces efficient minimization because it implies that ${ \cal T } [ \psi ] = 0$ leads to an infinite loss, while ${ \cal T } [ \psi ] = 1$ ψ is a global minimum. Otherwise, $\psi ( x ) = 0 ~ \forall x$ ψwould be a local minimum, making it harder to ψtrain the network.

The PDE term in Eq. (1) imposes the solution the Schrödinger equation, $H \left| \psi \right. = E \left| \psi \right.$ , where $H$ is the nuclear Hamiltonian and $E$ ψ ψ is the eigenvalue. The corresponding loss, $\mathcal { L } _ { S c h r o d }$ , is the one that includes the nuclear Hamiltonian we are trying to solve, thus defining the specific physical system. To implement the PDE condition we first need to compute the expectation value of the energy with respect to the network output, $\vert \psi \rangle$ , as

$$
E = \frac {\langle \psi | H | \psi \rangle}{\mathcal {I} [ \psi ]} = \sum_ {j = 0} ^ {n} w _ {j} \frac {\psi \left(x _ {j}\right) [ H \psi ] \left(x _ {j}\right)}{\mathcal {I} [ \psi ]}, \tag {9}
$$

where $w _ { j }$ are integration weights and $[ H \psi ] ( x _ { j } )$ indicates the state $H \left| \psi \right.$ ψevaluated at the sampling point $x _ { j }$ . Note that $E$ ψcould be computed either via finite differences, Eq. (9), or using the auxiliary output method described above. We always use Eq. (9) in this work. The PDE term of the loss is then,

$$
\mathcal {L} _ {S c h r o d} = \sum_ {i = 0} ^ {N _ {c}} \left\{\left[ H \psi \right] \left(x _ {i}\right) - E \psi \left(x _ {i}\right) \right\}. \tag {10}
$$

The structure of the PINN allows a very efficiently computation of $[ H \psi ] ( x _ { j } )$ , and hence Eqs. (9) and (10), by exploiting ψautomatic differentiation for all relevant derivatives that enter the Hamiltonian operator $H$ .

Finally, the variational principle is implemented by the loss

$$
\mathcal {L} _ {v a r} = \min  \left[ 0, (b E) ^ {c} \right] + d (t) e ^ {a (E - E _ {0})}, \tag {11}
$$

where a, $^ b$ and $E _ { 0 }$ are real-valued hyperparameters, the $c$ takes only odd integers values to preserve the sign of $b E$ , and $E$ represents the energy expectation value of Eq. (9). The second term of Eq. (11) is used to lead the network toward the lowest energy states. Here, the quantity $d ( t ) = 0 . 9 9 9 9 ^ { t }$ , where t .enumerates the training epochs, is a decay parameter that goes to zero as the training proceeds, ensuring that the variational principle improves the early stages of training without damaging the latter stages due to the lack of a minimum of this term when $E$ assumes the correct value. In general, Eq. (11) has the purpose to both improve the early stages of training and to facilitate convergence toward the ground state. Note that Eq. (11) also works in the case of excited states, if any.

With all the above definitions, the overall PINN loss function can be summarized as

$$
\begin{array}{l} \mathcal {L} _ {P I N N} = \alpha_ {S c h} \mathcal {L} _ {S c h r o d} + \alpha_ {i n t} \mathcal {L} _ {i n t} + \alpha_ {B C s} \mathcal {L} _ {B C s} + \\ \alpha_ {\text {n o r m}} \mathcal {L} _ {\text {n o r m}} + \alpha_ {\text {v a r}} \mathcal {L} _ {\text {v a r}}, \tag {12} \\ \end{array}
$$

where we have added appropriate weights to each term.

# 2.1. Evaluation metrics

We now turn to the two evaluation metrics utilized to benchmark the quality of the results. Being the approach not supervised, these are not used for training they but reveal interesting insights. The main quantity is the relative error of the predicted energy with respect to the exact numerical solution. We choose a signed metric to indicate whether the network overestimates or underestimates the energy:

$$
\operatorname {e r r} _ {E, N u m} = \frac {E _ {N u m} - E _ {P I N N}}{E _ {N u m}}. \tag {13}
$$

The second indicator concerns the eigenvector and it is the fidelity between the predicted wave function and the exact one [30, 31, 32],

$$
\mathcal {F} _ {\psi} = | \langle \psi_ {N u m} | \psi_ {P I N N} \rangle | ^ {2}.
$$

ψ ψ ψWe evaluate this numerically as

$$
\mathcal {F} _ {\psi} = \left| \sum_ {i = 0} ^ {N _ {c}} \psi_ {P I N N} \left(x _ {i}\right) \overline {{\psi_ {N u m} \left(x _ {i}\right)}} \right| ^ {2}, \tag {14}
$$

where the $x _ { i }$ are a set of points spanning the whole domain, and $\psi _ { E x } ( x )$ and $\psi _ { P I N N } ( x )$ are wave functions from the exact numeriψ ψcal solution and obtained from the PINN network, respectively. Both of the vectors are properly normalized before evaluating Eq. (14). In this work, we chose to compute $\mathcal { F } _ { \psi }$ on the same $N _ { c }$ collocation points used for training.

# 3. Results

We now turn to the results for the deuteron ground state within the PINNs framework. We first focus on the Minnesota potential in coordinate space from Ref. [33]. This is a particularly simplified model for the nuclear force but one that allows us to test the PINN approach on the integro-differential form for the the Schrödinger equation, involving spatial derivatives for the kinetic energy term. We then turn to momentum space and consider two different realistic models of the nuclear interaction. The first is the so-called next-to-next-to-next-to-next lowest order $( N ^ { 4 } L O )$ interaction which is at fifth-order in chiral effective field theory $\mathrm { ( \chi E F T ) }$ expansion. The $\chi \mathrm { E F T }$ is curχ χrently the best performing paradigm for the derivation of nuclear Hamiltonians [12, 11, 34, 35, 36, 37] and it is exploited in most state-of-the-art ab initio simulation of nuclei [38]. Here, we exploit the $N ^ { 4 } L O$ two-nucleon force from Ref. [39] with a cutoff on the relative momentum of $5 5 0 ~ \mathrm { M e V / c }$ . The second interaction is the CD-Bonn model from Ref. [40]. This is also a high-precision potential but built to induce strong short-range correlations—hence, high momenta in the wave function—and it is therefore the most challenging interaction of the three to diagonalize. We focus on the (one-dimensional) radial Schrödinger equation for the deuteron and deal with S $\scriptstyle ( L = 0 )$ and D $( L { = } 2 )$ partial waves. The coupling among angular momentum and spin-isospin already implies the fulfillment of the Pauli principle and no loss function for constraining antisymmetry is required. In a more general framework with more nucleons, the Pauli principle can be effectively encoded into

Table 1: Optimal weights for the different partial losses entering Eq. (12), adopted to compensate for the different scales of each term.   

<table><tr><td>Loss (Li)</td><td>Weight (αi)</td><td>Loss (Li)</td><td>Weight (αi)</td></tr><tr><td>Lschrod</td><td>10-4</td><td>Lnorm</td><td>1</td></tr><tr><td>Lint</td><td>10-3</td><td>Lvar</td><td>106</td></tr><tr><td>LBCs</td><td>102</td><td></td><td></td></tr></table>

the network architecture through determinant wave functions, see for example Refs. [41, 15], or partially enforced using additional dedicated losses.

# 3.1. Deuteron in position space

We implemented the PINNs using a feed-forward network with 6 hidden layers of 256 neurons each. The network was trained using the overall loss from Eq. (12) computed over 4097 collocation points and with the weights from Table 1. It is important to note that the different partial losses can have very different scales, and this is taken into account by the choice of the weights. For the variational loss hyperparameters, we used $E _ { 0 } = - 2 ~ \mathrm { M e V } .$ , $a = 0 . 8 ~ \mathrm { M e V ^ { - 1 } }$ , $b = 1 0 ^ { 4 } \mathrm { ~ M e V ^ { - 1 } }$ and $c = 1$ . .The main metric used to evaluate the network’s performance is the accuracy with respect to the energy obtained from the exact diagonalization of the Hamiltonian.

Since the Minnesota potential does not account for angular momentum mixing, the network had only one output for the auxiliary integral, Eq. (6), and one for the wavefunction in the $^ 3 S _ { 1 }$ spin triplet channel, $\psi _ { S } ( k )$ . The converged wavefunction is ψcompared to the potential in Fig. 1 and follows the qualitative behavior of a bound $L { = } 0$ wave, with an enhanced probability where the interaction is most attractive. Figure 2a, shows the energy expectation value during training. It starts at a positive value and reaches near $- 2 \ \mathrm { M e V }$ after 5000 epochs. Then, it gradually converges to a value close to the exact numerical solution with a final relative error of $1 . 1 \%$ . Figure 2b demon-.strates the behavior of each partial loss contributing to Eq. (12). These are combined into the total loss shown in Fig. 2c through the weights from Table 1. We highlight that the differential equation loss starts converging later with respect to the other contributions shown in Figure 2b. This behavior has been induced intentionally by adjusting the $\alpha _ { S c h }$ weight, with the aim αof making the network first learn the physical constraints of the system and later refine the solution of the differential equation.

# 3.2. Deuteron in momentum space

The $N ^ { 4 } L O$ and CD-Bonn interactions in momentum space are high precision models of the nuclear force and, therefore, they account for a small admixture of $D$ partial waves in the deuteron wavefunction. The mixing of angular momentum by the nuclear force is well known to be necessary for explaining the quadrupole moment of the deuteron. Consequently, the ground state wavefunction will have two components,

$$
\psi (k) = \left( \begin{array}{c} \psi_ {S} (k) \\ \psi_ {D} (k) \end{array} \right), \tag {15}
$$

![](images/1d6591863c48515bbc9dbc0b3779d08bdd950320ad724f722e21acfa9fd8c41c.jpg)  
Figure 1: Ground state of the deuteron. The red dots show the predictions of the eigenfunction, as obtained after approximately 40000 training epochs. This is compared to the Minnesota potential in the $^ 3 S _ { 1 }$ channel as a blue line.

for the $^ 3 S _ { 1 }$ and ${ } ^ { 3 } D _ { 1 }$ partial waves. The Schrödinger equation for the deuteron reads

$$
\begin{array}{l} E \left( \begin{array}{c} \psi_ {S} (k) \\ \psi_ {D} (k) \end{array} \right) = \int_ {0} ^ {\infty} \left( \begin{array}{c c} V _ {S S} (k, k ^ {\prime}) & V _ {S D} (k, k ^ {\prime}) \\ V _ {D S} (k, k ^ {\prime}) & V _ {D D} (k, k ^ {\prime}) \end{array} \right) \left( \begin{array}{c} \psi_ {S} (k ^ {\prime}) \\ \psi_ {D} (k ^ {\prime}) \end{array} \right) (k ^ {\prime}) ^ {2} d k ^ {\prime} \\ + \frac {k ^ {2}}{2 \mu} \binom {\psi_ {S} (k)} {\psi_ {D} (k)} \tag {16} \\ \end{array}
$$

where $V _ { L L ^ { \prime } } ( k , k ^ { \prime } )$ is the interaction between partial waves $L$ and $L ^ { \prime }$ , $k$ ,is the momentum of the relative motion in $\mathrm { M e V / c }$ and $\mu = m _ { p } m _ { n } / ( m _ { p } + m _ { n } )$ is the reduced mass. We use the values $m _ { p } = 9 3 8 . 2 7 2 0 8 8 1 6 \mathrm { M e V } / \mathrm { c } ^ { 2 }$ and $m _ { n } = 9 3 9 . 5 6 5 4 2 0 5 2 { \mathrm { M e V } } / { \mathrm { c } } ^ { 2 }$ for proton and neutron masses, respectively [42]. The normalization condition reads

$$
\mathcal {I} [ \psi ] = \int_ {0} ^ {\infty} k ^ {2} \left(| \psi_ {S} (k) | ^ {2} + | \psi_ {D} (k) | ^ {2}\right) d k = 1 \tag {17}
$$

Note that $\psi _ { S } ( 0 )$ has finite value, while $\begin{array} { r } { \operatorname* { l i m } _ { k  0 } \psi _ { D } ( k ) = 0 } \end{array}$ .

# 3.2.1. Network architecture and hyperparameters

The neural networks we employ in momentum space is also of type feed forward, with 7 hidden layers of 256 neurons each and the momentum $k$ as the single input feature. Since we do not use the auxiliary output for normalization, the network will have only two outputs that are related to the wavefunction components of Eq. (15) by $\phi _ { S } ( k ) = k \psi _ { S } ( k )$ and $\phi _ { D } ( k ) = 1 0 k \psi _ { D } ( k )$ . The factor $k$ ϕ ψ ϕ ψin these definitions facilitates evaluating the $\mathcal { L } _ { B C s }$ loss, as well as implementing Eq. (16) into $\mathcal { L } _ { S c h r o d }$ . We have added a rescaling of a factor of 10 as a standardization correction for the ${ } ^ { 3 } D _ { 1 }$ wave, which gives a smaller contribution with respect to the $^ 3 S _ { 1 }$ counterpart. With these definitions, Eq. (4) is adapted to impose the boundary conditions

$$
\phi_ {s} (0) = \phi_ {d} (0) = \phi_ {s} \left(k _ {\max }\right) = \phi_ {d} \left(k _ {\max }\right) = 0, \tag {18}
$$

where $M = k _ { m a x }$ is the largest momentum point of an appropriate integration mesh, $\{ ( k _ { i } , w _ { i } ) : i = 1 , 2 , \ldots , N _ { c } \}$ , in k-space. ,This mesh covers the integration range $[ 0 , k _ { m a x } ]$ , where we use $k _ { m a x } = 1 3 8 9 . 0 2 \mathrm { M e V / c }$ with $N _ { c } { = } 1 0 0$ , points for the $N ^ { 4 } L O$ and $k _ { m a x } \approx 8 5 7 3 ~ \mathrm { M e V / c }$ with $N _ { c } { = } 2 0 0$ points for CD-Bonn. Note that the mesh points are also used as collocation points throughout the simulations. We found that the training in momentum

![](images/1a41107163f8b459e83415c214c33158c6d964a03ef1072fe4725ba13c8d44fe.jpg)

![](images/07fab54cfe555837d099da401666370553a308624f8d244a02ffccf20261a567.jpg)

![](images/e6b48c17d4eeb5deba3c50de9a784025667917ec96437d4bf860d454dc62113c.jpg)  
Figure 2: Training history for the Minnesota potential. (a) Behavior of the predicted nuclear eigenvalue. The purple line shows the energy of the deuteron predicted by the PINN, while the blue horizontal line is the experimental energy. (b) Partial contributions to the loss function. The green line is for the integral loss $\mathcal { L } _ { i n t e g }$ , yellow is for the normalization loss $\mathcal { L } _ { n o r m }$ , brown shows the boundary conditions loss $\mathcal { L } _ { B C s }$ and the black line is the differential equation loss $\mathcal { L } _ { s c h r o d }$ . We considered a loss to be converged once it reaches below the dashed line, which corresponds to a hyperparameter that has been set to 100. (a) Total loss, Eq. (12), through training.

![](images/d917a05105b47c28e8cb08437ac4af0d2a5d06a5993dc88469bd044868ae6130.jpg)  
Figure 3: Ground state of the deuteron for the $N ^ { 4 } L O \ \chi \mathrm { E F T }$ interaction. The red and green dots are the PINN solutions for the $^ 3 S _ { 1 }$ χand ${ } ^ { 3 } D _ { 1 }$ wavefunction, obtained after $4 \times 1 0 ^ { 5 }$ epochs of training. The blue and orange lines are the exact solutions for the $^ 3 S _ { 1 }$ and ${ } ^ { 3 } D _ { 1 }$ components, respectively.

space is more efficient if we employ a finite difference method for the normalization. Thus, the integral (17) is evaluated as

$$
\mathcal {I} [ \psi ] \approx \sum_ {i = 0} ^ {N} w _ {i} \left(\left| \phi_ {S} \left(k _ {i}\right) \right| ^ {2} + \left| \frac {\phi_ {D} \left(k _ {i}\right)}{1 0} \right| ^ {2}\right). \tag {19}
$$

For the $\mathcal { L } _ { v a r }$ loss, we implement the same hyperparameters used in coordinate space except for $E _ { 0 } = - 3$ , $a = 0 . 0 1$ . With all the .above definitions, the overall loss for the PINN in momentum space is given by Eq. (12) but without $\mathcal { L } _ { n o r m }$ and the last term in Eq. (8), which are specific to the auxiliary output method only.

# 3.2.2. $N ^ { 4 } L O$ interaction

With the $5 5 0 ~ \mathrm { M e V / c }$ cutoff of the $N ^ { 4 } L O$ interaction it is sufficient to exploit a uniform linear mesh mesh in the interval $[ 0 , k _ { m a x } ]$ with $k _ { m a x } \approx 1 4 0 0 ~ \mathrm { M e V / c }$ . This interval is suffi-,ciently large to make the wavefunction vanishingly small at the boundaries but small enough to avoid instabilities from training the network on a too vast region where the both interaction and kinetic energy are negligible. The network took around $4 \times 1 0 ^ { 5 }$ epochs to reach convergence. The final relative error with respect to the exact numerical diagonalization of Eq. (16) is $e r r _ { E , N u m } = - 5 . 2 1 \times 1 0 ^ { - 5 }$ with a fidelity of $\mathcal { F } _ { \psi } = 0 . 9 9 9 9 9 3 3$ , , . ψachieving more than acceptable levels of precision.

The PINN wavefunctions for both $^ 3 S _ { 1 }$ and ${ } ^ { 3 } D _ { 1 }$ components are compared to the exact diagonalization in Fig. 3. The curves agree very closely in shape, as it should be expected from the small above relative error and high fidelity in reducing the expected ground state energy of Eq. (9). However, the PINN wavefunctions are slightly smaller indicating the the $\mathcal { L } _ { n o r m }$ loss is not fully minimized and would require further training to improve although the energy is already converged. At the point were we stopped our training we have $\mathcal { I } [ \psi ] = 0 . 8 2 1 9$ . Fig. 3 ψ .also shows the difference in scale among the two components, with the $\psi _ { D } ( k )$ being significantly smaller.

Figures 4a and 4b demonstrate the trends of the energy and the fidelity during training. The energy increases rapidly in first few epochs and then it drops close to 0 MeV, which is the continuum threshold. It remains constant at this value for several iterations until around $8 \times 1 0 ^ { 4 }$ epochs, when it resumes dropping until it converges asymptotically. The behavior observed for the energy is reflected in the total loss in Figure 4c. While overall the loss always trends downwards, the three distinct regions of Fig. 4a are reflected in different slopes for the overall loss. The rapid change of the energy in the first epochs correspond to a very steep descent of the loss but its slope is reduced during the epochs of constant energy. Eventually, the convergence of the energy is affected by an oscillating loss. The cause of these behaviors can be understood by looking at the partial losses, in Figure 5. All the losses quickly decrease in the first region. In the second region, $\mathcal { L } _ { S c h r o d }$ decreases quite slowly, while $\mathcal { L } _ { B C s }$ stagnates. The large value of $\mathcal { L } _ { B C s }$ in this region indicates that the bound state boundary conditions are not met and scattering states are still admixed into the wavefunction. This is also reflected by the fidelity not being able to grow above 0.8. Once $\mathcal { L } _ { B C s }$ drops below the tolerance threshold, the energy starts dropping below the continuum threshold $\scriptstyle ( \mathbf { E } < 0 \mathbf { M e V } )$ ) <and the fidelity finally raises. This indicates that conditions of Eq. (18) are finally met. The kink in $\mathcal { L } _ { n o r m }$ around epoch $8 \times 1 0 ^ { 4 }$ signals that the normalization ${ \cal T } [ \psi ]$ moves monotoniψcally and it crosses the correct value of 1 at at the same epochs were the change in the structure of the wavefunction occurs. It then takes several other iterations before $\mathcal { L } _ { n o r m }$ starts dropping properly. Note that the oscillations in the total loss are a conse-

![](images/61217387130157620cb112a827b17e5b02fcb1fbeaa78065f2b4061de27e6604.jpg)

![](images/8af8e379d60028661ccf17775d9fbcf71073e4070adc61d73393f5eb3fa41e12.jpg)

![](images/23399045e05aa2feeaff93183f7d9e55327548d925d0a63093918abcc90ba8cc.jpg)  
Figure 4: Behavior of the PINN network for the $N ^ { 4 } L O$ interaction during training. (a) Ground state energy. The purple line shows the energy of the deuteron predicted by the PINN, while the blue horizontal line is the experimental energy. (b) Fidelity computed with respect to the exact diagonalization. (c) Total loss.

![](images/42f01dc5ed2754e06c4bb7d91a87ddf2e5d066c410463f64b0e6aca4c64105f1.jpg)  
Figure 5: Behavior of the partial losses through training for the $N ^ { 4 } L O$ interactions. The yellow line is the normalization loss $\mathcal { L } _ { n o r m }$ , in brown is the boundary conditions loss $\mathcal { L } _ { B C s }$ and the black line is the differential equation loss $\mathcal { L } _ { S c h r o d }$ . A loss is considered converged once it passes the blue dashed line, which is a hyperparameter, here set at 1.

quence of noisy behavior of $\mathcal { L } _ { B C s }$ and $\mathcal { L } _ { S c h r o d }$ when they reach convergence. This indicates a critical behavior in training the boundaries of the wave function.

Finally, we point out that the number of epochs required to train this neural network is one order of magnitude larger than the epochs needed to tune the PINN in coordinate space with the setup of Sect. 3.1. Despite this, each epochs of the $N ^ { 4 } L O$ training required around a tenth of computing time with respect to Sect. 3.1 because of the different integration methods employed. The finite difference method means that PINN requires more epochs to reach convergence compared to the auxiliary output method. However, each epoch is significantly shorter because the automatic differentiation algorithm is executed only once per epoch, instead of four times as with the auxiliary output method.

# 3.2.3. CD-Bonn interaction

The CD-Bonn two-nucleon force is more demanding to diagonalize because it was specifically constructed to induce a very strong short-range repulsion [40]. This feature translates in small but non negligible components of the wave function at very high momenta. Correspondingly, we use a different mesh than for the $N ^ { 4 } L O$ with twice as many collocation points and that extends up to several $G e V / c$ . We follow the standard ap-/proach of mapping a set of Gauss-Legendre quarature points into the $[ 0 , \infty )$ interval through a hyperbolic tangent transfor-

![](images/85ad27f3cd895349a39cdcde778130c668fa29059476789d61840ff829ec360e.jpg)  
Figure 6: Ground state of the deuteron for the CD-Bonn potential. The meaning of the curves is the same as for Fig. 3.

mation. This allows to extend to large momenta while keeping a dense mesh at low values of $k$ . The largest momentum point in our mesh is $k _ { m a x } \approx 8 5 7 3 ~ \mathrm { M e V / c }$ .

We trained the solution of the CD-Bonn interaction by using the same neural network obtained for $N ^ { 4 } L O$ —with its converged weights and biases—as the starting point. Since physics-informed neural networks are excellent interpolators, this ansatz provides a rough qualitative solution up to momenta of $1 3 8 9 \ \mathrm { M e V / c }$ where it was trained, greatly accelerating the training process. To avoid instabilities due to the initial extrapolation to larger momenta we first train the CB-Bonn interaction with the same momentum range used for the $N ^ { 4 } L O$ interaction and then gradually enlarge $k _ { m a x }$ in steps of $4 0 0 \mathrm { M e V / c }$ until we cover the full mesh at $k _ { m a x } \approx 8 5 7 3 ~ \mathrm { M e V / c }$ .

Figure 6 demonstrated the final deuteron wavefunction components for momenta up to approx $2 \mathrm { \ G e V / c }$ . In this case, the training strategy is sufficient to force the normalization condition so that the curves overlap properly. Note that the highmomentum tail would be visible only in logarithmic scale. The fidelity of the wavefunction with respect to the numerical benchmark is such that $1 - \mathcal { F } _ { \psi } \approx 1 0 ^ { - 9 }$ . The relative error for ψthe deuteron binding energy with respect to the exact numerical benchmark is $e r r _ { E , N u m } = - 2 . 7 6 \times 1 0 ^ { - 7 }$ , while it would be $e r r _ { E , E x p } = - 6 . 0 1 \times 1 0 ^ { - 4 }$ . with respect to the experimental value.

# 3.3. Comparing the different interactions

The different final values we obtain for the relative errors with respect to the experimental energy mostly reflect how so-

phisticated is the interaction used. In fact, the error is maximum at 0 01 for the very simple Minnesota potential, and minimum .for the more modern $N ^ { 4 } L O$ , at $- 5 . 9 6 \times 1 0 ^ { - 6 }$ . We interpret this .fact by observing that the main source of error is from the potential itself and not the PINN method. In fact, when we compare the PINN results for $N ^ { 4 } L O$ to those for CD-Bonn, the older potential leads to worse results with respect to the experimental energy, with an error in the order of $1 0 ^ { - 4 }$ compared to the $1 0 ^ { - 6 }$ of $N ^ { 4 } L O$ , while the error with respect to the numerical benchmark is slightly lower for CD-Bonn, probably due to the better start and the larger set of collocation points, at $- 2 . 7 6 \times 1 0 ^ { - 7 }$ compared to the $- 5 . 7 6 \times 1 0 ^ { - 6 }$ for $N ^ { 4 } L O$ .. However, the error .for the Minnesota potential is still by far the highest even with respect to the numerical benchmark. This might reflect either a shortcoming in the auxiliary output method or just a need for longer training. Of course, all results will also be improved just by training for a longer period of time.

# 4. Conclusions and future directions

We were able to utilize physics-informed networks to tackle realistic models of the nucleon-nucleon interaction in momentum space, even with strong high-momentum correlations, and to obtain highly accurate results on the deuteron benchmarks. We also performed a similar simulation with a simplified interaction to prove the feasibility in coordinate space. The designed and validated neural network models are capable of computing the eigenvalue and eigenfunction of the ground state of the deuteron for these potentials. The PINN framework is particularly interesting with respect to standard variational approaches because it is not specific to ground states but can be applied to the solution of excited states [27]. In particular, the boundary condition loss can be naturally adapted to search for scattering solutions of the many-body problem.

The present implementation is specific to the onedimensional radial Schrödinger equation and remains computationally more demanding than the direct exact diagonalizaton for the two-nucleon problem. Nevertheless, it demonstrates the feasibility of PINN for microsopic nuclear simulation and, in this sense, it paves the way for a completely new way to utilize novel machine learning tools for theoretical physics. To do so, it remains imperative to extend the present PINN implementation to full three dimensional space. For example, exploiting ansätze similar to those used in the VMC framework with standard variational and NQS wavefunctions. This will open the possibility of studying simple atomic nuclei and molecules. Further work in nuclear physics would also require the implementation of three-nucleon interactions.

# Acknowledgements

The Authors acknowledge the project CQES of the Italian Space Agency (ASI) for having partially supported this research (Grant No. 2023-46-HH.0). The authors also acknowledge support from the Qxtreme project funded via the Partenariato Esteso FAIR (grant No. J33C22002830006). AM ac-

knowledges the IRA Programme, project no. FENG.02.01- IP.05-0006/23, financed by the FENG program 2021-2027, Priority FENG.02, Measure FENG.02.01., with the support of the FNP. This work used the DiRAC Data Intensive service (DIaL3) at the University of Leicester, managed by the University of Leicester Research Computing Service on behalf of the STFC DiRAC HPC Facility (www.dirac.ac.uk). The DiRAC service at Leicester was funded by BEIS, UKRI and STFC capital funding and STFC operations grants. DiRAC is part of the UKRI Digital Research Infrastructure.

# References

[1] J. Abramson, J. Adler, J. Dunger, R. Evans, T. Green, A. Pritzel, O. Ronneberger, L. Willmore, A. J. Ballard, J. Bambrick, S. W. Bodenstein, D. A. Evans, C.-C. Hung, M. O’Neill, D. Reiman, K. Tunyasuvunakool, Z. Wu, A. Žemgulyte, E. Arvaniti, C. Beattie,˙ O. Bertolli, A. Bridgland, A. Cherepanov, M. Congreve, A. I. Cowen-Rivers, A. Cowie, M. Figurnov, F. B. Fuchs, H. Gladman, R. Jain, Y. A. Khan, C. M. R. Low, K. Perlin, A. Potapenko, P. Savy, S. Singh, A. Stecula, A. Thillaisundaram, C. Tong, S. Yakneen, E. D. Zhong, M. Zielinski, A. Žídek, V. Bapst, P. Kohli, M. Jaderberg, D. Hassabis, J. M. Jumper, Accurate structure prediction of biomolecular interactions with alphafold 3, Nature 630 (8016) (2024) 493–500. doi:10.1038/s41586-024-07487-w. URL https://doi.org/10.1038/ s41586-024-07487-w   
[2] F. Noé, S. Olsson, J. Köhler, H. Wu, Boltzmann generators: Sampling equilibrium states of many-body systems with deep learning, Science 365 (6457) (2019) eaaw1147. arXiv:https://www. science.org/doi/pdf/10.1126/science.aaw1147, doi:10.1126/science.aaw1147. URL https://www.science.org/doi/abs/10. 1126/science.aaw1147   
[3] G. Carleo, M. Troyer, Solving the quantum manybody problem with artificial neural networks, Science 355 (6325) (2017) 602–606. arXiv:https://www. science.org/doi/pdf/10.1126/science.aag2302, doi:10.1126/science.aag2302. URL https://www.science.org/doi/abs/10. 1126/science.aag2302   
[4] K. Hornik, M. Stinchcombe, H. White, Multilayer feedforward networks are universal approximators, Neural networks 2 (5) (1989) 359–366.   
[5] M. Maronese, C. Destri, E. Prati, Quantum activation functions for quantum neural networks, arXiv preprint arXiv:2201.03700 (2022).   
[6] M. Medvidovic, J. R. Moreno, Neural-network quantum´ states for many-body physics, The European Physical Journal Plus 139 (7) (2024) 1–26.

[7] N. Yoshioka, W. Mizukami, F. Nori, Solving quasiparticle band spectra of real solids using neural-network quantum states, Communications Physics 4 (1) (2021) 106. doi:10.1038/s42005-021-00609-0. URL https://doi.org/10.1038/ s42005-021-00609-0   
[8] J. Hermann, J. Spencer, K. Choo, A. Mezzacapo, W. M. C. Foulkes, D. Pfau, G. Carleo, F. Noé, Ab initio quantum chemistry with neural-network wavefunctions, Nature Reviews Chemistry 7 (10) (2023) 692–709. doi:10.1038/s41570-023-00516-8. URL https://doi.org/10.1038/ s41570-023-00516-8   
[9] D. Pfau, S. Axelrod, H. Sutterud, I. von Glehn, J. S. Spencer, Accurate computation of quantum excited states with neural networks, Science 385 (6711) (2024) eadn0137. arXiv:https://www. science.org/doi/pdf/10.1126/science.adn0137, doi:10.1126/science.adn0137. URL https://www.science.org/doi/abs/10. 1126/science.adn0137   
[10] I. von Glehn, J. S. Spencer, D. Pfau, A self-attention ansatz for ab-initio quantum chemistry, in: The Eleventh International Conference on Learning Representations, 2023. URL https://openreview.net/forum?id= xveTeHVlF7j   
[11] E. Epelbaum, H.-W. Hammer, U.-G. Meißner, Modern theory of nuclear forces, Rev. Mod. Phys. 81 (2009) 1773–1825. doi:10.1103/RevModPhys.81.1773. URL https://link.aps.org/doi/10.1103/ RevModPhys.81.1773   
[12] R. Machleidt, D. Entem, Chiral effective field theory and nuclear forces, Physics Reports 503 (1) (2011) 1–75. doi:https://doi.org/10.1016/j.physrep.2011. 02.001. URL https://www.sciencedirect.com/science/ article/pii/S0370157311000457   
[13] J. Keeble, A. Rios, Machine learning the deuteron, Physics Letters B 809 (2020) 135743. doi:https: //doi.org/10.1016/j.physletb.2020.135743. URL https://www.sciencedirect.com/science/ article/pii/S0370269320305463   
[14] C. Adams, G. Carleo, A. Lovato, N. Rocco, Variational monte carlo calculations of $ { \boldsymbol { a } } \quad \le \quad 4$ nuclei with an artificial neural-network correlator ansatz, Phys. Rev. Lett. 127 (2021) 022502. doi:10.1103/PhysRevLett.127.022502. URL https://link.aps.org/doi/10.1103/ PhysRevLett.127.022502

[15] D. Pfau, J. S. Spencer, A. G. D. G. Matthews, W. M. C. Foulkes, Ab initio solution of the manyelectron schrödinger equation with deep neural networks, Phys. Rev. Res. 2 (2020) 033429. doi:10.1103/PhysRevResearch.2.033429. URL https://link.aps.org/doi/10.1103/ PhysRevResearch.2.033429   
[16] Y. L. Yang, P. W. Zhao, Deep-neural-network approach to solving the ab initio nuclear structure problem, Phys. Rev. C 107 (2023) 034320. doi:10.1103/PhysRevC.107.034320. URL https://link.aps.org/doi/10.1103/ PhysRevC.107.034320   
[17] S. Brolli, C. Barbieri, E. Vigezzi, Diagrammatic monte carlo for finite systems at zero temperature, Phys. Rev. Lett. 134 (2025) 182502. doi:10.1103/PhysRevLett.134.182502. URL https://link.aps.org/doi/10.1103/ PhysRevLett.134.182502   
[18] M. Grossi, O. Kiss, F. De Luca, C. Zollo, I. Gremese, A. Mandarino, Finite-size criticality in fully connected spin models on superconducting quantum hardware, Phys. Rev. E 107 (2023) 024113. doi:10.1103/PhysRevE.107.024113. URL https://link.aps.org/doi/10.1103/ PhysRevE.107.024113   
[19] F. P. Barone, O. Kiss, M. Grossi, S. Vallecorsa, A. Mandarino, Counterdiabatic optimized driving in quantum phase sensitive models, New Journal of Physics 26 (3) (2024) 033031. doi:10.1088/1367-2630/ad313e. URL http://dx.doi.org/10.1088/1367-2630/ ad313e   
[20] L. Nigro, C. Barbieri, E. Prati, Simulation of a threenucleons system transition on quantum circuits, Advanced Quantum Technologies 8 (5) (2025) 2400371.   
[21] M. Raissi, P. Perdikaris, G. Karniadakis, Physicsinformed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics 378 (2019) 686–707. doi:https: //doi.org/10.1016/j.jcp.2018.10.045. URL https://www.sciencedirect.com/science/ article/pii/S0021999118307125   
[22] X. I. A. Yang, S. Zafar, J.-X. Wang, H. Xiao, Predictive large-eddy-simulation wall modeling via physicsinformed neural networks, Phys. Rev. Fluids 4 (2019) 034602. doi:10.1103/PhysRevFluids.4.034602. URL https://link.aps.org/doi/10.1103/ PhysRevFluids.4.034602   
[23] B. Reyes, A. A. Howard, P. Perdikaris, A. M. Tartakovsky, Learning unknown physics of non-Newtonian fluids, Phys. Rev. Fluids 6 (2021) 073301.

doi:10.1103/PhysRevFluids.6.073301.   
URL https://link.aps.org/doi/10.1103/ PhysRevFluids.6.073301   
[24] M. Raissi, A. Yazdani, G. E. Karniadakis, Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations, Science 367 (6481) (2020) 1026 – 1030. doi:10.1126/science.aaw4741.   
URL https://www.science.org/doi/10.1126/ science.aaw4741   
[25] H. Jin, M. Mattheakis, P. Protopapas, Physics-informed neural networks for quantum eigenvalue problems (2022). arXiv:2203.00451.   
[26] L. Harcombe, Q. Deng, Physics-informed neural networks for discovering localised eigenstates in disordered media (2023). arXiv:2305.06802.   
[27] L. Brevi, A. Mandarino, E. Prati, Addressing the non-perturbative regime of the quantum anharmonic oscillator by physics-informed neural networks, New Journal of Physics 26 (10) (2024) 103015. doi:10.1088/1367-2630/ad8302.   
URL https://dx.doi.org/10.1088/1367-2630/ ad8302   
[28] L. Brevi, A. Mandarino, E. Prati, A tutorial on the use of physics-informed neural networks to compute the spectrum of quantum systems, Technologies 12 (10) (2024). doi:10.3390/technologies12100174.   
URL https://www.mdpi.com/2227-7080/12/10/ 174   
[29] L. Yuan, Y.-Q. Ni, X.-Y. Deng, S. Hao, A-pinn: Auxiliary physics informed neural networks for forward and inverse problems of nonlinear integro-differential equations, Journal of Computational Physics 462 (2022) 111260. doi: https://doi.org/10.1016/j.jcp.2022.111260.   
URL https://www.sciencedirect.com/science/ article/pii/S0021999122003229   
[30] M. Bina, A. Mandarino, S. Olivares, M. G. A. Paris, Drawbacks of the use of fidelity to assess quantum resources, Phys. Rev. A 89 (2014) 012305. doi:10.1103/PhysRevA.89.012305.   
URL https://link.aps.org/doi/10.1103/ PhysRevA.89.012305   
[31] A. Mandarino, M. Bina, S. Olivares, M. G. Paris, About the use of fidelity in continuous variable systems, International Journal of Quantum Information 12 (02) (2014) 1461015. doi:10.1142/S0219749914610152.   
URL https://doi.org/10.1142/ S0219749914610152   
[32] A. Mandarino, M. Bina, C. Porto, S. Cialdi, S. Olivares, M. G. A. Paris, Assessing the significance of fidelity as a figure of merit in quantum state reconstruction of discrete and continuous-variable systems, Phys. Rev. A 93 (2016)

062118. doi:10.1103/PhysRevA.93.062118.   
URL https://link.aps.org/doi/10.1103/ PhysRevA.93.062118   
[33] D. Thompson, M. Lemere, Y. Tang, Systematic investigation of scattering problems with the resonating-group method, Nuclear Physics A 286 (1) (1977) 53–66. doi:https://doi.org/10.1016/0375-9474(77) 90007-0.   
URL https://www.sciencedirect.com/science/ article/pii/0375947477900070   
[34] R. Machleidt, F. Sammarruca, Chiral eft based nuclear forces: achievements and challenges, Physica Scripta 91 (8) (2016) 083007. doi: 10.1088/0031-8949/91/8/083007.   
URL https://dx.doi.org/10.1088/0031-8949/ 91/8/083007   
[35] H.-W. Hammer, S. König, U. van Kolck, Nuclear effective field theory: Status and perspectives, Rev. Mod. Phys. 92 (2020) 025004. doi:10.1103/RevModPhys.92.025004.   
URL https://link.aps.org/doi/10.1103/ RevModPhys.92.025004   
[36] R. Machleidt, Historical perspective and future prospects for nuclear interactions, International Journal of Modern Physics E 26 (11) (2017) 1730005. arXiv: https://doi.org/10.1142/S0218301317300053, doi:10.1142/S0218301317300053.   
URL https://doi.org/10.1142/ S0218301317300053   
[37] R. Machleidt, F. Sammarruca, Recent advances in chiral eft based nuclear forces and their applications, Progress in Particle and Nuclear Physics 137 (2024) 104117. doi: https://doi.org/10.1016/j.ppnp.2024.104117. URL https://www.sciencedirect.com/science/ article/pii/S0146641024000218   
[38] L. Coraggio, S. Pastore, C. Barbieri, Editorial: The future of nuclear structure: Challenges and opportunities in the microscopic description of nuclei, Frontiers in Physics 8 (2021) 626976. doi:10.3389/fphy.2020.626976.   
URL https://www.frontiersin.org/ research-topics/9952   
[39] D. R. Entem, R. Machleidt, Y. Nosyk, High-quality two-nucleon potentials up to fifth order of the chiral expansion, Phys. Rev. C 96 (2017) 024004. doi:10.1103/PhysRevC.96.024004.   
URL https://link.aps.org/doi/10.1103/ PhysRevC.96.024004   
[40] R. Machleidt, High-precision, charge-dependent bonn nucleon-nucleon potential, Phys. Rev. C 63 (2001) 024001. doi:10.1103/PhysRevC.63.024001.   
URL https://link.aps.org/doi/10.1103/ PhysRevC.63.024001

[41] A. Lovato, C. Adams, G. Carleo, N. Rocco, Hiddennucleons neural-network quantum states for the nuclear many-body problem, Phys. Rev. Res. 4 (2022) 043178. doi:10.1103/PhysRevResearch.4.043178. URL https://link.aps.org/doi/10.1103/ PhysRevResearch.4.043178   
[42] E. Tiesinga, P. J. Mohr, D. B. Newell, B. N. Taylor, Codata recommended values of the fundamental physical constants: 2018, Rev. Mod. Phys. 93 (2021) 025010. doi:10.1103/RevModPhys.93.025010. URL https://link.aps.org/doi/10.1103/ RevModPhys.93.025010