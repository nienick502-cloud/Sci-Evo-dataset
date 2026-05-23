# Neural-network quantum states for the nuclear many-body problem

Alessandro Lovatoa,b,c,d,, Giuseppe Carleo $\mathbf { e }$ , Bryce Forea, Morten Hjorth-Jensenf, Jane Kim $\mathrm { a , g }$ , Arnau Rios $^ { \mathrm { h , i } }$ , Noemi Roccoj,d

aPhysics Division, Argonne National Laboratory, Argonne, Illinois 60439, USA

$^ { b }$ Computational Science Division, Argonne National Laboratory, Argonne, Illinois 60439, USA

cINFN-TIFPA Trento Institute of Fundamental Physics and Applications, 38123 Trento, Italy.

$^ d$ Instituto de Física Corpuscular (IFIC), Consejo Superior de Investigaciones Científicas (CSIC) and Universidad de Valencia E-46980

Paterna, Valencia, Spain

eInstitute of Physics, École Polytechnique Fédérale de Lausanne (EPFL), CH-1015 Lausanne, Switzerland

fDepartment of Physics and Center for Computing in Science Education, University of Oslo, N-0316 Oslo, Norway

gInstitute of Nuclear and Particle Physics and Department of Physics and Astronomy, Ohio University, Athens, OH, 45701, USA

hDepartament de Física Quàntica i Astrofísica, Universitat de Barcelona (UB), c. Martí i Franquès 1, E08028 Barcelona, Spain

iInstitut de Ciències del Cosmos, Universitat de Barcelona (UB), c. Martí i Franquès 1, E08028 Barcelona, Spain

jTheoretical Physics Department Fermi National Accelerator Laboratory P.O. Box 500 Batavia Illinois 60510 USA

# Abstract

A long-standing goal of nuclear theory is to explain how the structure and dynamics of atomic nuclei and neutron-star matter emerge from the underlying interactions among protons and neutrons. Achieving this goal requires solving the nuclear quantum many-body problem with high accuracy across a wide range of length scales and density regimes. In this review, we discuss how artificial neural network representations of the nuclear many-body wave function have significantly extended the capabilities of continuum quantum Monte Carlo methods. In particular, neural-network quantum states enable calculations of larger systems than were previously accessible and provide a flexible framework for capturing phenomena that challenge conventional approaches, including the emergence of nuclear clusters and superfluid phases in dense matter. We highlight recent applications to finite nuclei, infinite nuclear and neutron matter, and dynamical processes relevant to lepton–nucleus and nucleus–nucleus scattering. We also discuss conceptual and methodological connections with condensed matter physics, emphasizing developments in neural-network quantum states that bridge strongly correlated systems across disciplines. Together, these developments demonstrate how neural-network methods open new avenues toward unified and accurate descriptions of nuclear structure, matter, and reactions.

Keywords: Neural Network Quantum States, Nuclear Quantum Many-Body Problem, Atomic Nuclei, Neutron Star Matter, Nuclear Electroweak Interactions

# Contents

1 Introduction 3   
2 The nuclear quantum many-body problem 5

2.1 Nuclear Hamiltonian 5  
2.2 Progress and challenges of quantum Monte Carlo methods 9

3 Neural-network quantum states for nuclear physics 13

3.1 Sampling the Hilbert space 13   
3.2 Optimization strategies 15   
3.3 Basics of deep learning 16   
3.4 Wave function ansätze . 19

3.4.1 Slater–Jastrow 19   
3.4.2 Operator-dependent Slater–Jastrow 20   
3.4.3 Hidden Nucleons . 21   
3.4.4 Pfaffian–Jastrow 24   
3.4.5 Backflow correlations 26

4 Nuclear Physics Applications 29

4.1 The deuteron 29   
4.2 Atomic nuclei 32

4.2.1 Nuclei with up to A=6 nucleons 32   
4.2.2 Relativistic effects 36   
4.2.3 Reaching $^ { 1 6 }$ O with systematically improvable ansätze 37   
4.2.4 Essential elements of nuclear binding 40   
4.2.5 High-resolution potentials 41

4.3 Nuclear matter 45

4.3.1 Pure neutron matter 45   
4.3.2 Clustering . 47   
4.3.3 Beta-equilibrated matter 47

4.4 Electroweak interactions 48   
4.5 Pairing interactions and the occupation-number formalism 51

5 Connections to condensed matter physics 54

5.1 Polarized fermions 54   
5.2 The homogeneous electron gas 56   
5.3 Ultra-cold Fermi gases . 59

6 Conclusions and perspectives 62

# 1. Introduction

At the energy scales relevant for the dynamics of atomic nuclei, the fundamental theory of strong interactions, quantum chromodynamics (QCD), becomes non-perturbative, and quarks and gluons are confined within hadrons. Following the seminal works of Weinberg [1, 2], effective field theories (EFTs) have emerged as the framework of choice for computing low-energy nuclear observables with quantified uncertainties. Two prominent examples are pionless EFT and chiral EFT, both of which exploit a separation between a “hard” momentum scale $\Lambda$ and a “soft” scale $Q$ that characterizes the typical momenta in low-energy nuclear systems [3, 4]. Pionless EFT is applicable when $Q \ll m _ { \pi }$ , and its breakdown scale is set by $\Lambda \sim m _ { \pi }$ . In contrast, chiral EFT retains explicit pion degrees of freedom, and its breakdown scale is considerably higher, Λ ∼ 600–700 MeV, while the soft scale remains $Q \sim m _ { \pi }$ . At low energies, protons and neutrons interact through nonrelativistic potentials systematically organized as an expansion in $Q / \Lambda$ [3–5]. High-momentum physics is integrated out and encoded in low-energy constants fitted to nucleon–nucleon scattering data and observables in light nuclei.

Interactions and electroweak currents derived consistently within the EFT framework provide the primary input to ab initio methods designed to solve the nuclear many-body Schrödinger equation with controlled and systematically improvable approximations [6, 7]. Single-particle basis methods such as the no-core shell model (NCSM) [8], coupledcluster (CC) theory [9], the in-medium similarity renormalization group (IMSRG) [10], and self-consistent Green’s function (SCGF) techniques [11] have achieved impressive success. The NCSM and its resonating-group extension [12] accurately describe clustering and collective dynamics [13–15] but are generally restricted to light nuclei, and convergence for longrange observables can be slow [16]. Polynomially scaling approaches such as CC and IMSRG now reach nuclei as heavy as $\scriptstyle 1 0 0$ Sn [17–19] and $^ { 2 0 8 }$ Pb [20], providing access to spectra, response functions, and transition rates [21–23]. These developments have deepened our understanding of the long-standing quenching of $g _ { A }$ [24] and enabled uncertaintyquantified predictions of neutrinoless double- $\beta$ decay [25–27]. Nevertheless, truncation of model spaces limits their ability to fully capture multi-scale phenomena, especially alpha clustering and short-range correlations. Symmetry-adapted shell-model approaches [28, 29] mitigate some of these challenges but they may not be able to fully capture short-distance dynamics.

A second class of ab initio methods relies on stochastic formulations, such as nuclear lattice EFT (NLEFT) [30] and continuum quantum Monte Carlo (QMC) techniques [31–33]. NLEFT has advanced to medium-mass nuclei [34], revealing compelling signatures of alpha clustering [35] and providing insights into nuclear matter at finite temperature [36, 37], enabled by substantial algorithmic progress [38]. However, the fermion sign problem and the computational cost of fine lattice spacings limit its ability to resolve short-range dynamics with high accuracy. Continuum QMC methods, such as Green’s function Monte Carlo (GFMC) [39] and auxiliary-field diffusion Monte Carlo (AFDMC) [40], accurately describe nuclear dynamics across long, intermediate, and short ranges. In practice, however, GFMC scales exponentially with the mass number, restricting applications to nuclei with $A \lesssim 1 3$ , while AFDMC encounters a severe sign problem when realistic correlations are introduced, limiting its applicability to nuclei with $A \sim 1 6$ [41, 42].

These challenges have motivated the exploration of neural-network representations of quantum many-body wave functions, a framework that has already achieved notable success in condensed-matter physics and quantum chemistry [43– 45]. In the nuclear domain, however, neural-network quantum states (NQS) methods face a distinct set of difficulties. Nuclear interactions are highly non-perturbative and exhibit strong spin–isospin dependence, placing them well outside the regime where mean-field approximations provide a reliable starting point [46]. As a result, NQS methods are confronted with correlations at all length scales. At the same time, realistic nuclear Hamiltonians require treating both continuous

spatial degrees of freedom and discrete spin and isospin degrees of freedom, significantly enlarging the structure of the underlying Hilbert space.

In this review, we discuss the development and application of NQS ansätze in nuclear physics and closely related areas. Following the pioneering application of NQS to the deuteron [47], variational Monte Carlo methods based on NQS [48–52] have proven to provide a systematically improvable framework with polynomial computational scaling and have begun to address several long-standing challenges in ab initio nuclear theory. Our focus is on first-quantized architectures, which operate directly on the continuous spatial coordinates and discrete spin–isospin degrees of freedom of the nucleons. This representation naturally accommodates short-, intermediate-, and long-range nuclear dynamics, from the repulsive core and tensor correlations to clustering and collective degrees of freedom. Moreover, NQS approaches capture the multiscale behavior characteristic of nuclei and neutron-star matter [53], including superfluidity, the emergence of nuclear clusters, and dominant short-range correlations [54, 55].

First, we briefly review existing continuum QMC methods, focusing in particular on GFMC and the computational challenges associated with treating nuclei with more than $A = 1 3$ nucleons. This naturally leads to a discussion on how the Hilbert space is sampled in VMC methods, with emphasis on the nuclear case, where both continuous (spatial coordinates) and discrete (spin–isospin) degrees of freedom must be sampled efficiently. After providing a short recap of the elements of deep learning relevant to NQS approaches, we introduce the main first-quantized NQS architectures proposed to date and discuss how physical symmetries—such as parity, time-reversal, and translation invariance—are incorporated into these models.

In the second part of the review, we summarize the most important recent results for finite nuclei and for infinite nuclear and neutron matter. We then discuss initial applications of NQS wave functions to lepton–nucleus and nucleus– nucleus scattering, highlighting the potential of these methods to deliver unified and accurate ab initio descriptions of both nuclear structure and reactions, and to extend the reach of nuclear many-body theory beyond the traditional limits imposed by basis truncations and the sign problem. Before concluding, we provide a selective overview NQS approaches to condensed matter theory, focusing particularly on those that have direct links to nuclear theory.

# 2. The nuclear quantum many-body problem

The nuclear quantum many-body problem presents formidable challenges due to the strong spin–isospin dependence and intrinsically non-perturbative character of realistic nuclear interactions. In contrast to quantum chemistry, where the Coulomb interaction is known a priori and provides a universal two-body potential, nuclear forces must be derived within the EFT framework. The construction of accurate two- and three-nucleon interactions with quantified uncertainties remains an active research frontier [3, 4, 7].

Recent advances in Bayesian parameter estimation and regulator optimization have further improved the consistency and predictive power of modern chiral EFT Hamiltonians. The complexity of these interactions has motivated the development of a broad suite of ab initio many-body approaches [6]. Single-particle basis methods, including the NCSM, CC theory, SCGF and the IMSRG, have achieved high-precision results across wide regions of the nuclear chart. Complementary stochastic formulations such as NLEFT have revealed striking signatures of clustering [35] and have advanced toward medium-mass nuclei, though their finite lattice spacing limits the resolution of short-range dynamics. Continuum QMC methods [31–33], including GFMC [39] and AFDMC [40], accurately capture nuclear dynamics from long to short distances, but their applicability across the nuclear chart remains restricted. GFMC scales exponentially with the mass number, while AFDMC suffers from a worsening sign problem for realistic chiral interactions [41, 42].

Because this review focuses on neural quantum states (NQS) applied to continuum QMC, this section summarizes the local coordinate-space Hamiltonians derived from EFT that serve as inputs to both conventional QMC and NQS-based VMC calculations [56]. We then discuss the principal scaling bottlenecks encountered by GFMC and AFDMC as the mass number increases, highlighting the aspects most relevant for constructing efficient NQS ansätze. These considerations motivate the exploration of first-quantized NQS architectures that act directly on the continuous spatial coordinates and discrete spin–isospin degrees of freedom, offering a promising path toward extending the reach of continuum QMC methods beyond their traditional limits.

# 2.1. Nuclear Hamiltonian

To a remarkable extent, the properties of atomic nuclei and neutron-star matter can be described by point-like nucleons whose dynamics are governed by a nonrelativistic Hamiltonian

$$
H _ {L O} = \sum_ {i} \frac {\mathbf {p} _ {i} ^ {2}}{2 m _ {N}} + \sum_ {i <   j} v _ {i j} + \sum_ {i <   j <   k} V _ {i j k}, \tag {2.1}
$$

where $\mathbf { p } _ { i }$ is the three-momentum of the $_ i$ -th nucleon, $m _ { N }$ is its mass, and $v _ { i j }$ and $V _ { i j k }$ are the potentials describing nucleon-nucleon ( $N N$ ) and three-nucleon ( $\Omega N$ ) interactions, respectively.

With the notable exception of Ref. [47], and more recently Refs. [57, 58], most applications of neural quantum states (NQS) to nuclear physics employ $N N$ and $3 N$ potentials based on the premise that the momentum scales relevant for modeling the structure of atomic nuclei are much smaller than the pion mass, $m _ { \pi } \simeq 1 4 0$ MeV. In this regime, pions can be integrated out, giving rise to pionless EFT [59, 60], in which the charge-independent (CI) nuclear interactions consist solely of contact terms between two or more nucleons. Pionless EFT provides a controlled and systematically improvable description of nuclear systems in the low-momentum regime, where short-range correlations and universal behavior dominate the structure of light nuclei and dilute nuclear matter. At the same time, its reduced operator complexity offers a natural setting for developing and benchmarking first-quantized NQS architectures, allowing one to

![](images/ef845d937d54878a01e6da3df355cb61dc0eebb2c677e9e7c09754d9dce7a29a.jpg)

![](images/1c0ee1bb194d101daca47e3877754d64c0fdcdcb990b4236feff7807a5325568.jpg)  
Figure 2.1: Phase shifts in the $^ 3 S _ { 1 }$ and $^ { 1 } S _ { 0 }$ channels for $n p$ scattering computed using the LO EFT Hamiltonian “o” of Ref. [61], compared to the PWA93 analysis and results from the realistic Argonne $\mathrm { v } _ { 1 8 }$ potential [46].

isolate representational and optimization challenges before confronting the additional multiscale structure and strong tensor correlations induced by explicit pion exchange.

In this review, we focus on the leading-order (LO) pionless EFT expansion of Ref. [61]. The LO NN interaction derived in that work is constrained to act only in even partial waves. In coordinate space, it is given by

$$
v _ {L O} ^ {C I} \left(r _ {i j}\right) = C _ {0 1} C _ {1} \left(r _ {i j}\right) P _ {0} ^ {\sigma} P _ {1} ^ {\tau} + C _ {1 0} C _ {0} \left(r _ {i j}\right) P _ {1} ^ {\sigma} P _ {0} ^ {\tau}, \tag {2.2}
$$

where $r _ { i j } = \left| \mathbf { r } _ { i } - \mathbf { r } _ { j } \right|$ and $P _ { 0 , 1 } ^ { o }$ ( $P _ { 0 , 1 } ^ { \tau }$ ) are the spin (isospin) projection operators for the nucleon pair $i j$ with total spin $S$ and isospin $T$ equal to $0$ or 1:

$$
P _ {0} ^ {\sigma} = \frac {1 - \sigma_ {i j}}{4}, \quad P _ {1} ^ {\sigma} = \frac {3 + \sigma_ {i j}}{4}, \quad P _ {0} ^ {\tau} = \frac {1 - \tau_ {i j}}{4}, \quad P _ {1} ^ {\tau} = \frac {3 + \tau_ {i j}}{4}. \tag {2.3}
$$

Here, $\sigma _ { i j } = { \pmb { \sigma } } _ { i } \cdot { \pmb { \sigma } } _ { j }$ and $\tau _ { i j } = \boldsymbol { \tau } _ { i } \cdot \boldsymbol { \tau } _ { j }$ , with $\pmb { \sigma } _ { i }$ and $\tau _ { i }$ denoting the Pauli spin and isospin operators acting on nucleon $i$ respectively. In this implementation, the contact interactions are regularized using Gaussian cutoff functions,

$$
C _ {\alpha} (r) = \frac {1}{\pi^ {3 / 2} R _ {\alpha} ^ {3}} e ^ {- (r / R _ {\alpha}) ^ {2}}, \tag {2.4}
$$

where $R _ { \alpha }$ controls the range of the regulator.

Most of the results presented in this review are obtained using model “o” of Ref. [61], in which the cutoff radii $R _ { 0 } = 1 . 5 4 5 9$ fm and $R _ { 1 } = 1 . 8 3 0 4$ fm, as well as the low-energy constants $C _ { 0 1 } = - 5 . 2 7 5 1 8 6 7 1 \ \mathrm { f m ^ { 2 } }$ and $C _ { 1 0 } = - 7 . 0 4 0 4 0 0 8 0$ $\mathrm { f m ^ { 2 } }$ , were adjusted to reproduce the neutron–proton scattering lengths and effective ranges in the singlet and triplet channels, as well as the deuteron binding energy. To demonstrate the performance of this interaction, Fig. 2.1 displays the phase shifts in the $^ 3 S _ { 1 }$ and $^ { 1 } S _ { 0 }$ channels for $n p$ scattering.

On the one hand, we observe excellent agreement with both the PWA93 analysis and those obtained from the highly realistic Argonne $\mathrm { v } _ { 1 8 }$ potential, extending up to $T _ { \mathrm { l a b } } = 5$ MeV. On the other hand, the phase shifts of the model “o” in the $^ { 1 } S _ { 0 }$ channels for $p p$ and nn scattering, displayed in Fig. 2.2, exhibit some discrepancies compared to both the PWA93 analysis and those obtained from the realistic Argonne $\mathrm { v } _ { 1 8 }$ potential [46]. These differences can be attributed to the absence of a charge-dependent term in model “o”, which enters at next-to-leading order (NLO) in the pionless EFT expansion. It has yet to be determined whether including these terms will stabilize $^ { 6 } \mathrm { H e }$ , $^ { \mathrm { ~ 8 ~ } }$ Li, 8B, $^ { 9 } \mathrm { C }$ , and $^ { 1 7 } \mathrm { F }$ against breakup into smaller clusters, or if P-wave terms need to be incorporated into the nucleon-nucleon interaction [62].

The $N N$ potential of Eq. (2.2) can be expressed compactly in the spin–isospin operator basis as

$$
v _ {i j} ^ {\mathrm {C I}} = \sum_ {p = 1} ^ {4} v ^ {p} \left(r _ {i j}\right) O _ {i j} ^ {p}, \tag {2.5}
$$

where $O _ { i j } ^ { p = 1 , 4 } = \left( 1 , \tau _ { i j } , \sigma _ { i j } , \sigma _ { i j } \tau _ { i j } \right)$ , akin to the $v _ { 4 } ^ { \prime }$ potential [63]. The explicit forms of the radial functions $v ^ { p } ( r _ { i j } )$ are provided in Appendix A of Ref. [61], and their radial dependence is illustrated in Fig. 2.3.

In addition to the CI component, the two-nucleon interaction includes an electromagnetic (EM) contribution, such that $v = v ^ { \mathrm { E M } } + v _ { \mathrm { L O } } ^ { \mathrm { C I } }$ . The full $v ^ { \mathrm { E M } }$ consists of one- and two-photon Coulomb terms, the Darwin-Foldy term, vacuum polarization, and magnetic moment interactions; see Ref. [46] for their explicit expressions. However, most NQS applications retain only the Coulomb repulsion between finite-size (rather than point-like) protons.

In pionless EFT, solving systems with $A \geq 3$ using purely attractive LO NN potentials leads to the so-called Thomas collapse [64] as the regulator is removed. This pathological behavior is avoided by promoting a contact $3 N$ force to LO [65]. In this review, we consider a regularized $3 N$ potential of the form

$$
V _ {i j k} = \frac {c _ {E}}{f _ {\pi} ^ {4} \Lambda_ {\chi}} \frac {(\hbar c) ^ {6}}{\pi^ {3} R _ {3} ^ {6}} \sum_ {\text {c y c}} e ^ {- (r _ {i j} ^ {2} + r _ {j k} ^ {2}) / R _ {3} ^ {2}}, \tag {2.6}
$$

where $\Lambda _ { \chi } = 1$ GeV, $f _ { \pi } = 9 2 . 4$ MeV is the pion decay constant, and $\scriptstyle \sum _ { \mathrm { c y c } }$ denotes cyclic permutations of the indices $i$ , $j$ , and $k$ . The low-energy constant $c _ { E }$ is fixed to reproduce the $^ 3 \mathrm { H }$ binding energy, $B ( ^ { 3 } \mathrm { H } ) = 8 . 4 7 5 \ ]$ MeV, for a given value of the cutoff $R _ { 3 }$ . The analysis of Ref. [61] shows that the choice $R _ { 3 } = 1 . 0$ fm and $c _ { E } = 1 . 0 7 8 6$ provides a satisfactory description of nuclear binding energies across a broad mass range, up to ${ } ^ { 9 0 } \mathrm { Z r }$ . However, subsequent VMC–NQS calculations have indicated that this choice leads to overbinding in $^ { 1 6 }$ O and heavier nuclei. Increasing the cutoff to $R _ { 3 } ~ = ~ 1 . 1$ fm with $c _ { E } = 1 . 2 9 4 5$ largely resolves this issue [52], as the extended range of the $3 N$ force introduces additional repulsion in heavier systems.

Very recent applications of nuclear NQS employ higher-resolution interactions, either phenomenological or derived within chiral EFT. In particular, Refs. [57, 58, 66] use consistent $N N$ and $3 N$ potentials derived at next-to-next-toleading order (N $^ 2$ LO) in the chiral EFT expansion that are local in coordinate space [56, 67, 68]. Notably, the authors of Ref. [66] were also able to employ NQS with the phenomenological Argonne $v _ { 8 } ^ { \prime }$ + Urbana IX Hamiltonian [69], which features a strongly repulsive core at short distances. The charge-independent (CI) part of both the Argonne $v _ { 8 } ^ { \prime }$ interaction

![](images/67510fb43a1dd075a9ad34da13f8d7287c71422a602cfb6ac91259be926e3f56.jpg)

![](images/fae0eba55dde302f8e6ebee55f01afe20071162c4ba19792d872c9b00c02b48b.jpg)  
Figure 2.2: Phase shifts in the $^ 1 S _ { 0 }$ channels for $p p$ and $_ { n n }$ scattering computed using the LO EFT Hamiltonian “o” of Ref. [61] compared to the PWA93 analysis and results from the realistic Argonne v18 potential [46]..

![](images/cbe442e8a8710db5e8f8cc93e843a0ce2d1988ea05ae62725c2c0cb12a9a4398.jpg)  
Figure 2.3: Radial functions of the model “o” NN potential at LO in the pionless EFT expansion, expressed in the spin–isospin basis.

![](images/d64a419c9abf974d9a3aaf2a7c592259bff7bdaa7903a280cda976fe8256da9c.jpg)  
Figure 2.4: Radial functions of the Argonne $v _ { 8 } ^ { \prime }$ potential, expressed in the spin–isospin basis.

and the local N $^ 2$ LO chiral EFT potentials can be written in operator form as

$$
v _ {i j} = \sum_ {p = 1} ^ {8} v ^ {p} \left(r _ {i j}\right) O _ {i j} ^ {p}, \tag {2.7}
$$

where $r _ { i j } = \left| \mathbf { r } _ { i } - \mathbf { r } _ { j } \right|$ is the interparticle distance. For the local N $^ 2$ LO chiral EFT potential, the sum is restricted to the first seven operators. Compared to Eq. (2.5), the additional operators entering this expansion include the tensor and spin-orbit components, for a total of eight operators, where $O _ { i j } ^ { p = 5 , 8 } = \left( S _ { i j } , S _ { i j } \tau _ { i j } , \mathbf { L } \cdot \mathbf { S } , \mathbf { L } \cdot \mathbf { S } \tau _ { i j } \right)$ . The tensor operator is

$$
S _ {i j} = \frac {3}{r _ {i j} ^ {2}} \left(\boldsymbol {\sigma} _ {i} \cdot \mathbf {r} _ {i j}\right) \left(\boldsymbol {\sigma} _ {j} \cdot \mathbf {r} _ {i j}\right) - \sigma_ {i j}, \tag {2.8}
$$

while the spin-orbit contribution is expressed in terms of the relative angular momentum $\begin{array} { r } { \mathbf { L } = \frac { 1 } { 2 i } \big ( \mathbf { r } _ { i } - \mathbf { r } _ { j } \big ) \times \big ( \nabla _ { i } - \nabla _ { j } \big ) } \end{array}$ and the total spin $\begin{array} { r } { \mathbf { S } = \frac { 1 } { 2 } \big ( { \pmb \sigma } _ { i } + { \pmb \sigma } _ { j } \big ) } \end{array}$ of the pair. The radial functions of the Argonne $v _ { 8 } ^ { \prime }$ potential are displayed in Fig. 2.4. In contrast to the model “o” interaction of Fig. 2.3, the Argonne potential exhibits a very strong short-range repulsive

core, exceeding 2 GeV (in the figure the central channel is divided by a factor of 5 for visibility). The sizable tensor and spin–orbit components, which extend to relatively large distances, are also clearly visible. This long-range behavior is a consequence of one-pion exchange. While the associated tensor interaction is singular at short distances in its bare form, scaling as $1 / r ^ { 3 }$ , this divergence is regularized in the Argonne interaction. The interaction nevertheless remains long-ranged in the Yukawa sense at large separations, decaying as $e ^ { - m _ { \pi } r } / r$ up to polynomial factors, and provides the dominant source of tensor correlations at intermediate distances in nuclei. Note that the Coulomb interaction, which is the longest-ranged component of the nuclear Hamiltonian, decays as $1 / r$ but is comparatively weak and acts only between protons.

The earliest example of a $3 N$ force dates back to the Fujita–Miyazawa interaction, whose main contributions arise from the virtual excitation of a $\Delta ( 1 2 3 2 )$ resonance in processes involving three interacting nucleons [70]. This term is included in both chiral EFT and in the Urbana IX potential [69] and reads

$$
V _ {i j k} ^ {\Delta} = V _ {i j k} ^ {\Delta , a} + V _ {i j k} ^ {\Delta , c}. \tag {2.9}
$$

The “anticommutator” and “commutator” contributions are

$$
V _ {i j k} ^ {\Delta , a} = \sum_ {\mathrm {c y c}} A _ {2 \pi} \left\{X _ {i j} ^ {\pi}, X _ {j k} ^ {\pi} \right\} \left\{\tau_ {i j}, \tau_ {j k} \right\}, V _ {i j k} ^ {\Delta , c} = \sum_ {\mathrm {c y c}} C _ {2 \pi} \left[ X _ {i j} ^ {\pi}, X _ {j k} ^ {\pi} \right] \left[ \tau_ {i j}, \tau_ {j k} \right], \tag {2.10}
$$

where $\scriptstyle \sum _ { \mathrm { c y c } }$ denotes a sum over the three cyclic permutations of the nucleons $i , j , k$ . The operator $X _ { i j } ^ { \pi }$ is defined as

$$
X _ {i j} ^ {\pi} = T \left(r _ {i j}\right) S _ {i j} + Y \left(r _ {i j}\right) \sigma_ {i j}, \tag {2.11}
$$

where the radial Yukawa and tensor functions, $Y ( r )$ and $T ( r )$ , are defined consistently with those appearing in the corresponding $N N$ interaction [46, 71].

Generally, a three-body potential composed only of $V _ { i j k } ^ { \Delta }$ does not reproduce the empirical saturation density of isospinsymmetric nucleonic matter [72]; a repulsive three-body contribution must be included,

$$
V _ {i j k} ^ {R} = A _ {R} \sum_ {\text {c y c}} T ^ {2} \left(r _ {i j}\right) T ^ {2} \left(r _ {j k}\right). \tag {2.12}
$$

The constants $A _ { 2 \pi }$ and $A _ { R }$ entering the Urbana IX model are determined by fitting the binding energy of $^ 3 \mathrm { H }$ and the saturation density of isospin-symmetric nucleonic matter, $\rho _ { 0 } = 0 . 1 6 \ \mathrm { f m } ^ { - 3 }$ [73]. Chiral EFT interactions likewise include a short-range three-body operator proportional to the low-energy constant $c _ { E }$ . This contribution may be purely scalar or contain isospin dependence, although the latter appears to be incompatible with astrophysical constraints.

In addition to the terms above, chiral EFT three-body forces at N $^ 2$ LO contain a one-pion-exchange (OPE) threebody component proportional to the low-energy constant $c _ { D }$ , as well as a second short-range contact proportional to $c _ { E }$ . The OPE three-body structure is also included in the phenomenological Illinois-7 force [74]. For detailed discussions of these terms, we refer the reader to Refs. [75], while Ref. [76] provides a comprehensive comparison between local phenomenological and chiral EFT interactions.

# 2.2. Progress and challenges of quantum Monte Carlo methods

The Hamiltonians discussed in the previous section are the main input to ab initio many-body methods that, within controlled approximations, solve the nuclear Schrödinger equation

$$
H \left| \Psi_ {n} \right\rangle = E _ {n} \left| \Psi_ {n} \right\rangle , \tag {2.13}
$$

where $\left| \Psi _ { n } \right.$ denotes the $n$ th eigenstate and $E _ { n }$ its associated eigenvalue. Several stochastic many-body frameworks have been developed to address this problem. Two broad and complementary approaches are lattice formulations based on path-integral methods and continuum quantum Monte Carlo techniques.

Nuclear lattice effective field theory (NLEFT) [30, 77], aided by notable algorithmic advances [38], has expanded its reach to medium-mass nuclei [34], provided compelling evidence for $\alpha$ clustering [35], and explored nuclear and neutron matter at finite temperature [36, 37]. However, NLEFT continues to face limitations arising from the fermion sign problem and the rapidly growing computational cost associated with fine lattice spacings, which constrain its ability to resolve short-range dynamics unless simplified interactions are used.

Continuum QMC methods [31, 33], originally developed in condensed-matter physics and later adapted to nuclear systems, operate directly in coordinate space. The variational Monte Carlo (VMC) method optimizes a parametrized trial state to capture the most important correlations and enforce the correct asymptotic behavior, thereby accurately describing long-range dynamics and $\alpha$ clustering. Building on VMC, Green’s function Monte Carlo (GFMC) [39, 78] projects the variational state in imaginary time toward exact eigenstates, while auxiliary-field diffusion Monte Carlo (AFDMC) [40] employs Hubbard–Stratonovich auxiliary fields to sample spin–isospin operators and access larger systems. These continuum approaches model nuclear dynamics across long, intermediate, and short distances and can accommodate “stiff” interactions with high-momentum components. Recent applications include ground-state properties [79], inclusive electron- and neutrino-scattering [80, 81], and a variety of electroweak observables such as electromagnetic moments and form factors, low-energy transitions and $\beta$ decays, and muon-capture processes [82, 83].

In this review, we focus primarily on the VMC method, first outlining the computational challenges of conventional variational states. VMC relies on the Rayleigh–Ritz variational principle

$$
\frac {\left\langle \Psi_ {V} (\boldsymbol {\theta}) \right| H \mid \Psi_ {V} (\boldsymbol {\theta}) \rangle}{\left\langle \Psi_ {V} (\boldsymbol {\theta}) \mid \Psi_ {V} (\boldsymbol {\theta}) \right\rangle} \equiv E _ {V} (\boldsymbol {\theta}) \geq E _ {0} \tag {2.14}
$$

to determine the optimal set of parameters $\pmb { \theta }$ defining the variational state $\Psi _ { V }$ . For the nuclear many-body problem, it is customary to assume that the trial state factorizes into long- and short-range components,

$$
\Psi_ {V} (R, S) \equiv \langle R, S | \Psi_ {V} \rangle = \langle R S | \left(1 + \sum_ {i <   j <   k} F _ {i j k}\right) \left(\mathcal {S} \prod_ {i <   j} F _ {i j}\right) | \Phi \rangle , \tag {2.15}
$$

where $F _ { i j }$ and $F _ { i j k }$ are two- and three-body correlation operators, respectively. The symbol $\boldsymbol { S }$ denotes a symmetrized product over nucleon pairs, since—in general, owing to their spin–isospin dependence—the $F _ { i j }$ need not commute. The symbol $R$ denotes the spatial coordinates of all nucleons, $( \mathbf { r } _ { 1 } , \ldots , \mathbf { r } _ { A } )$ , while $S$ stands for the spin–isospin degrees of freedom, to be discussed in detail below.

The long-range antisymmetric part $\Phi$ is commonly expressed as a linear combination of a few Slater determinants built from single-particle orbitals appropriate to the system of interest. For homogeneous matter, the orbitals are usually plane waves and may include pairing correlations [84]. For atomic nuclei, the single-particle orbitals are generally taken in the $\mathit { l s }$ - or $j j$ -coupling schemes and combined to yield the desired total angular momentum $J$ and parity $P$ of the nucleus [71]. Importantly, VMC calculations can explicitly incorporate the strong $\alpha$ -cluster structure of light nuclei: the wave function of $p$ -shell systems is constructed as a sum of independent-particle components, each with four nucleons in an $\alpha$ -like core and the remaining $( A - 4 )$ nucleons occupying $p$ -shell orbitals [85].

The spin–isospin structure of the two-body correlation operator mirrors that of the $N N$ potential and is written as

$$
F _ {i j} = \sum_ {p = 1} ^ {6} f ^ {p} \left(r _ {i j}\right) O _ {i j} ^ {p}. \tag {2.16}
$$

![](images/910d6a65ece8c006b6ad22b02e50a0c9f662bf3947f029d4767312dc2deab309.jpg)  
Figure 2.5: Number of many-body spin–isospin states, $2 ^ { A } { \binom { A } { Z } }$ , relevant to VMC and GFMC calculations for selected light nuclei.

Spin-orbit correlations, corresponding to $p = 7$ , 8, may also be included, but are often neglected due to the significant computational cost and the relatively small gain in variational energy [86]. The optimal radial functions $f ^ { p } ( r )$ are typically obtained by minimizing the two-body cluster contribution to the ground-state energy, subject to the correct asymptotic behavior [87]. Appropriate three-body correlation form factors have been derived within perturbation theory, as discussed in Ref. [31],

$$
F _ {i j k} = \sum_ {x} \epsilon_ {x} V _ {i j k} ^ {x} \left(\tilde {r} _ {i j}, \tilde {r} _ {i k}, \tilde {r} _ {j k}\right), \tag {2.17}
$$

where $\tilde { r } = y _ { x } r$ , with $y _ { x }$ a variational scaling parameter and $\epsilon _ { x }$ a small (negative) strength parameter, both optimized variationally. The superscript $x$ labels the different components of the three-nucleon interaction (e.g., $\Delta$ , $R$ ).

Both the VMC and GFMC methods employ an explicit many-body basis for the spin–isospin sector of the Hilbert space. A generic basis state can be written as $ { \left| { S } \right. } \equiv  { \left| { \chi _ { i _ { s } } } \right. } \otimes  { \left| { \chi _ { i _ { t } } } \right. }$ , where the indices $i _ { s }$ and $i _ { t }$ enumerate the many-body spin and isospin basis states, respectively. The $2 ^ { A }$ spin basis states can be written as

$$
\left| \chi_ {1} \right\rangle = \left| \downarrow_ {1}, \downarrow_ {2}, \dots , \downarrow_ {A} \right\rangle ,
$$

$$
\left| \chi_ {2} \right\rangle = \left| \uparrow_ {1}, \downarrow_ {2}, \dots , \downarrow_ {A} \right\rangle ,
$$

$$
\left| \chi_ {n _ {s}} \right\rangle = \left| \uparrow_ {1}, \uparrow_ {2}, \dots , \uparrow_ {A} \right\rangle , \tag {2.18}
$$

with $n _ { s } = 2 ^ { A }$ . The corresponding isospin states $| \chi _ { i _ { t } } \rangle$ are obtained by replacing ↓ with $n$ and $\uparrow$ with $p$ . For fixed proton number $Z$ (charge conservation), the dimension of the isospin basis is $\binom { A } { Z }$ . Figure 2.5 shows the spin–isospin Hilbert-space dimension for nuclei treated with GFMC to date. Data shown includes $^ { 1 3 } \mathrm { C }$ , currently being computed on ALCF’s Aurora supercomputer, and $^ { 1 6 } \mathrm { C }$ , anticipated to be within reach of the next generation of leadership-class machines.

The symmetrized product of pair correlation operators is evaluated by successive operations for each pair, sampling their ordering. As an example, consider the application of the operators $\sigma _ { 1 2 } \sigma _ { 1 3 } \sigma _ { 2 3 }$ on the three-body spin state $\mid \uparrow _ { 1 } , \downarrow _ { 2 } , \downarrow _ { 3 } \rangle$ .

Noting that $\sigma _ { i j } = 2 P _ { i j } ^ { o } - 1$ , where $2 P _ { i j } ^ { o }$ exchanges the spin of particles $i$ and $j$ , we obtain:

$$
\begin{array}{l} \left. \sigma_ {1 2} \sigma_ {1 3} \sigma_ {2 3} | \uparrow_ {1}, \uparrow_ {2}, \downarrow_ {3} \right\rangle = \sigma_ {1 2} \sigma_ {1 3} (2 | \uparrow_ {1}, \downarrow_ {2}, \uparrow_ {3}) - | \uparrow_ {1}, \uparrow_ {2}, \downarrow_ {3})) \\ = \sigma_ {1 2} \left(2 | \uparrow_ {1}, \downarrow_ {2}, \uparrow_ {3} \rangle - 2 | \downarrow_ {1}, \uparrow_ {2}, \uparrow_ {3} \rangle + | \uparrow_ {1}, \uparrow_ {2}, \downarrow_ {3}\right) \\ = 4 \left| \downarrow_ {1}, \uparrow_ {2}, \uparrow_ {3} \right\rangle - 6 \left| \uparrow_ {1}, \downarrow_ {2}, \uparrow_ {3} \right\rangle - 2 \left| \downarrow_ {1}, \uparrow_ {2}, \uparrow_ {3} \right\rangle + \left| \uparrow_ {1}, \uparrow_ {2}, \downarrow_ {3} \right\rangle). \tag {2.19} \\ \end{array}
$$

Hence, even starting from a single spin state, the action of the correlation operator generates four of them (even more are generated by the tensor correlations). In general, the the number of operations necessary to calculate the wave function grows exponentially with the number of nucleons, limiting the applicability of the VMC and GFMC methods to $A \le 1 3$ nuclei. Sampling the spin–isospin state and evaluating variational wave functions for that sampled state still requires a number of operations that is exponential in the particle number, bringing little savings in terms of computing time [31, 33]. For this reason, both VMC and GFMC are limited to relatively small mass numbers, up to $A \simeq 1 3$ .

To circumvent this difficulty, the authors of Ref. [88] developed a linearized version of the correlator in Eq. (2.15), in which the spin–isospin-independent correlations are retained in full, while the spin–isospin-dependent ones are kept only to first order:

$$
\left(\mathcal {S} \prod_ {i <   j} \sum_ {p = 1} ^ {6} f ^ {p} \left(r _ {i j}\right) O _ {i j} ^ {p}\right) \longrightarrow \left(\prod_ {i <   j} f ^ {c} \left(r _ {i j}\right)\right) \left(1 + \sum_ {i <   j} \sum_ {p = 1} ^ {6} u ^ {p} \left(r _ {i j}\right), O _ {i j} ^ {p}\right), \tag {2.20}
$$

where $u ^ { p } ( r _ { i j } ) \equiv f ^ { p } ( r _ { i j } ) / f ^ { c } ( r _ { i j } )$ . Because only linear terms in the spin–isospin-dependent two-body correlations are kept, this wave function is significantly cheaper to evaluate for a single spin–isospin amplitude than the full product of spin– isospin-dependent two-body correlations. This approach scalie as $A ^ { 5 }$ rather than exponentially. However, since only pairs of nucleons are correlated at a time, the cluster property is violated. Here, the cluster property means that, for two widely separated groups of nucleons the many-body wave function factorizes, $\Psi ( A \cup B )  \Psi ( A ) \Psi ( B )$ , so that connected cross-cluster correlations (and mixed contributions to extensive observables) should vanish.

Nevertheless, the use of these linearized spin-dependent correlations has enabled AFDMC calculations of properties of nuclei up to $A \sim 2 0$ with local chiral EFT interactions. However, the decreasing accuracy with system size prevents the application of AFDMC to medium-mass nuclei, as the method relies on accurate variational wave functions to control the fermion sign problem [89]. To address this issue, the AFDMC variational wave function has been improved by incorporating quadratic pair correlations [90], at a substantially higher computational cost that scales as $A ^ { 7 }$ . These increased costs, together with residual violations of the cluster property, substantially limit the current reach of AFDMC, with current applications around $A \sim 1 6$ [41, 42].

Extending VMC to larger nuclei calls for variational ansätze that capture the key physics, including short- and longrange correlations, clustering, correct asymptotics, and symmetries, while keeping the computational cost polynomial in $A$ . This motivates the development of nuclear neural-network quantum states, which provide compact, flexible parameterizations of many-body wave functions and can be optimized efficiently within VMC.

# 3. Neural-network quantum states for nuclear physics

In recent years, VMC methods leveraging NQS have been developed to model the wave functions of complex nuclear systems with high accuracy and favorable polynomial scaling with the number of nucleons. Similar to conventional continuum QMC methods, working in coordinate space enables NQS-based approaches to efficiently capture short-range nuclear dynamics. As illustrated schematically in Fig. 3.1, NQS architectures typically take as input the spatial and spin-isospin coordinates of the nucleons and output the amplitude and phase of the quantum many-body wave function. A generic neural-network architecture with this construction will not guarantee fermion anti-symmetry, so it must be explicitly imposed. To this aim, in parallel with condensed-matter and quantum-chemistry applications, different ansätze, discussed in detail in Section 3.4, have been developed.

In contrast, in second-quantized approaches, fermion antisymmetry is encoded directly by the basis and the operator algebra: states are expanded in the ordered occupation basis, and fermionic signs follow from the canonical anticommutation relations upon reordering operators. Consequently, in second quantization no additional permutation constraint is imposed on the variational wave function. The fermionic signs are determined by the ordered Fock basis and the anticommutation relations, not by any symmetry of the coefficients [91].

![](images/923c445ec9d012a55f3bae3559c9d5a28108ff7296f8a1208cc90741bdbb2fa7.jpg)  
Figure 3.1: Schematic representation of a NQS to solve the nuclear quantum many-body problem. An anti-symmetric artificial neural network takes as input the spatial and spin-isospin coordinates of the $A$ nucleons, $\{ \mathbf { r } _ { i } , s _ { i } ^ { z } , t _ { i } ^ { z } \}$ , and outputs the logarithmic amplitude and phase of the quantum many-body wave function, $\log ( \Psi _ { V } ( R S ; \theta ) ) = \log \left| \Psi _ { V } ( R S ; \theta ) \right| + i \Phi _ { V } ( R S ; \theta )$

# 3.1. Sampling the Hilbert space

Evaluating the variational energy in Eq. (2.14) requires carrying out a $3 A$ -dimensional integral over the continuous Cartesian coordinates of the nucleons, $R = \left( \mathbf { r } _ { 1 } , \ldots , \mathbf { r } _ { A } \right)$ , and a sum over the $2 ^ { A } { \binom { A } { Z } }$ discrete spin–isospin configurations, $S = \Big ( \big ( s _ { 1 } ^ { z } , t _ { 1 } ^ { z } \big ) , \dots , \big ( s _ { A } ^ { z } , t _ { A } ^ { z } \big ) \Big )$ , with $s _ { i } ^ { z }$ and $t _ { i } ^ { z }$ denoting the spin and isospin projections of the ith nucleon:

$$
E _ {V} = \frac {\left\langle \Psi_ {V} \right| H \mid \Psi_ {V} \rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle} = \frac {\sum_ {S} \int d R \left\langle \Psi_ {V} \right| R S \rangle \left\langle R S \mid H \mid \Psi_ {V} \right\rangle}{\sum_ {S} \int d R \left\langle \Psi_ {V} \right| R S \rangle \left\langle R S \mid \Psi_ {V} \right\rangle}, \tag {3.1}
$$

where, for brevity, we have dropped the explicit dependence of the variational state on a set of parameters $\pmb { \theta }$ . Since a deterministic evaluation is computationally prohibitive, these expressions are estimated stochastically using Monte Carlo

sampling. To this end, it is convenient to rewrite the variational energy as

$$
E _ {V} = \frac {\sum_ {S} \int d R | \Psi_ {V} (R , S) | ^ {2} \frac {\langle R S | H | \Psi_ {V} \rangle}{\langle R S | \Psi_ {V} \rangle}}{\sum_ {S} \int d R | \Psi_ {V} (R , S) | ^ {2}} = \sum_ {S} \int d R \pi_ {V} (R, S) E _ {L} (R, S), \tag {3.2}
$$

where we introduced the probability distribution and the local energy,

$$
\pi_ {V} (R, S) = \frac {| \Psi_ {V} (R , S) | ^ {2}}{\sum_ {S} \int d R | \Psi_ {V} (R , S) | ^ {2}}, \qquad E _ {L} (R, S) = \frac {\langle R S | H | \Psi_ {V} \rangle}{\langle R S | \Psi_ {V} \rangle}. \tag {3.3}
$$

This procedure is unbiased, since configurations with $\Psi _ { V } ( R , S ) = 0$ do not contribute to Eq. (3.1), and the reweighting by $| \Psi _ { V } ( R , S ) | ^ { 2 }$ is therefore well defined.

In most NQS-based applications of the VMC method to the nuclear many-body problem [48, 49, 51, 52, 92], with the notable exception of Ref. [57], the Metropolis–Hastings algorithm [93, 94] is used to generate Markov chain samples of spatial and spin–isospin configurations distributed according to $\pi _ { V } ( R , S )$ . The resulting $N _ { \mathrm { c o n f } }$ configurations are then used to estimate ground-state expectation values via

$$
E _ {V} \simeq \frac {1}{N _ {\text {c o n f}}} \sum_ {\{R, S \} \sim \pi_ {V}} E _ {L} (R, S). \tag {3.4}
$$

The initial $3 A$ spatial coordinates of the nucleons are typically sampled from a Gaussian distribution centered at the origin, with per–coordinate variance chosen to reproduce the target rms point radius. For example, taking $R _ { \mathrm { p t } } \approx$ $1 . 2 A ^ { 1 / 3 } \mathrm { f m }$ , one may set $\sigma ^ { 2 } = R _ { \mathrm { p t } } ^ { 2 } / 3$ . The $z$ -projections of the spin–isospin degrees of freedom are randomly initialized so that the total charge and total spin of the nucleus of interest are reproduced. Each Monte Carlo step consists of a Gaussian move of the $3 A$ spatial coordinates. Since charge is conserved, an ergodic isospin move within fixed $Z$ is to swap the isospin labels of a randomly selected pair of nucleons. The same swap is a legitimate move for the spin labels if tensor and spin–orbit contributions in the NN potential are neglected, so that the total spin projection $\begin{array} { r } { S _ { z } = \sum _ { i } s _ { i } ^ { z } } \end{array}$ is conserved. However, when tensor or spin–orbit interactions are present, one also needs moves that do not conserve $S _ { z }$ , such as single or double spin flips, to ensure ergodicity.

The newly proposed spatial configuration $R ^ { \prime }$ and spin–isospin projection $S ^ { \prime }$ are accepted separately (in two successive Metropolis updates) with probabilities

$$
A (R \rightarrow R ^ {\prime}) = \min  \left[ 1, \frac {| \Psi_ {V} (R ^ {\prime} , S) | ^ {2}}{| \Psi_ {V} (R , S) | ^ {2}} \right], \quad A (S \rightarrow S ^ {\prime}) = \min  \left[ 1, \frac {| \Psi_ {V} (R , S ^ {\prime}) | ^ {2}}{| \Psi_ {V} (R , S) | ^ {2}} \right], \tag {3.5}
$$

where we have assumed symmetric proposal kernels for the Gaussian spatial moves. The width of the Gaussian “kick” is tuned to keep the spatial acceptance rate near 0.6.

After $N _ { \mathrm { t h e r m } }$ thermalization steps, which are necessary to equilibrate the Markov chain, the Metropolis–Hastings algorithm produces configurations $\{ R , S \}$ distributed according to the target probability $\pi _ { V } ( R , S )$ . Because successive samples are correlated, $N _ { \mathrm { v o i d } }$ “void” (non-measurement) steps are typically inserted between measurements, and chosen such that the residual autocorrelation falls below a prescribed threshold. After equilibration, a total of $N _ { \mathrm { m e a s } }$ measurements are performed. To improve efficiency, the embarrassingly parallel nature of the Metropolis–Hastings algorithm is exploited by propagating $N _ { \mathrm { c h a i n s } }$ independent Markov chains in parallel, so that the total number of configurations used to estimate observables is $N _ { \mathrm { c o n f } } = N _ { \mathrm { c h a i n s } } \times N _ { \mathrm { m e a s } }$ .

# 3.2. Optimization strategies

The energy estimate in Eq. (2.14) provides an upper bound to the ground-state energy. One must still minimize this quantity with respect to the parameters $\pmb { \theta }$ , which turns VMC into a nonlinear optimization problem:

$$
E ^ {*} = \min  _ {\boldsymbol {\theta}} E _ {V} (\boldsymbol {\theta}), \quad \boldsymbol {\theta} ^ {*} = \arg \min  _ {\boldsymbol {\theta}} E _ {V} (\boldsymbol {\theta}). \tag {3.6}
$$

A standard strategy is to solve this problem iteratively. A succinct account of such iterative approaches in the NQS setting is given below. For comprehensive treatments in machine learning and optimization (including non-iterative methods), see Refs. [95, 96].

In an iterative scheme, one starts from an initial parameter vector $\pmb { \theta }$ and updates it as $\pmb { \theta } \gets \pmb { \theta } + \pmb { \delta }$ , where the increment $\pmb { \delta }$ is chosen to reduce the energy objective. In the NQS setting, a common choice is

$$
\boldsymbol {\delta} = - \eta S ^ {- 1} \mathbf {g}, \tag {3.7}
$$

which corresponds to minimizing the local quadratic model

$$
M (\boldsymbol {\delta}) = E _ {V} (\boldsymbol {\theta}) + \boldsymbol {\delta} ^ {\top} \mathbf {g} + \frac {1}{2} \boldsymbol {\delta} ^ {\top} S \boldsymbol {\delta}. \tag {3.8}
$$

The scalar $\eta$ is the learning rate that controls the overall step size in parameter space. The gradient of the variational energy is

$$
g _ {i} = 2 \left( \right.\frac {\left\langle \right. \Psi_ {V} \left. \right| O _ {i} ^ {\dagger} H \mid \Psi_ {V} \left. \right\rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle} - \frac {\left\langle \right. \Psi_ {V} \left. \right| O _ {i} ^ {\dagger} \mid \Psi_ {V} \left. \right\rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle} \frac {\left\langle \right. \Psi_ {V} \left. \right| H \mid \Psi_ {V} \left. \right\rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle}\left. \right), \tag {3.9}
$$

where $O _ { i } | \Psi _ { V } ( \pmb { \theta } ) \rangle = \partial _ { \theta _ { i } } | \Psi _ { V } ( \pmb { \theta } ) \rangle$ denotes a derivative of the wave function with respect to $i -$ th parameter. The matrix $S$ serves as a preconditioner, and different optimization schemes prescribe different choices. In the information-geometry paradigm, $S$ accounts for the curvature and geometry of parameter space, beyond the Euclidean (flat-space) gradient descent corresponding to $S = I$ [96]. In quadratic optimization, there is also a close relationship between $S$ and the Hessian of the loss function [95].

An extension of the information geometry approach in many-body quantum mechanics is the stochastic reconfiguration (SR) method [97]. Originally and independently introduced in the QMC literature at the end of the last century [98, 99], SR translates naturally to the NQS setting. It is commonly justified by minimizing the Fubini–Study distance between an updated NQS state and a small imaginary-time step for energy minimization [97, 98, 100]. This leads to identifying $S$ with the real part of the quantum geometric tensor (QGT),

$$
S _ {i j} = \frac {\left\langle \right. \Psi_ {V} \left. \right| O _ {i} ^ {\dagger} O _ {j} \mid \Psi_ {V} \left. \right\rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle} - \frac {\left\langle \right. \Psi_ {V} \left. \right| O _ {i} ^ {\dagger} \mid \Psi_ {V} \left. \right\rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle} \frac {\left\langle \right. \Psi_ {V} \left. \right| O _ {j} \mid \Psi_ {V} \left. \right\rangle}{\left\langle \Psi_ {V} \mid \Psi_ {V} \right\rangle}. \tag {3.10}
$$

The QGT acts as a metric under the Fubini–Study distance [97, 100] and thus encodes the curvature of the manifold of normalized wave functions [101]. Moreover, for real, non-negative ansätze, one can write $\Psi _ { V } = \sqrt { p }$ with $p$ the Born probability density. In this case, the QGT reduces to one quarter of the classical Fisher information matrix of $p$ , a central object in information geometry [96].

Whatever optimization setting is employed, both formal and numerical issues can affect the update in Eq. (3.7) and thereby hamper convergence. On the formal side, one wants the inverse to be well behaved so as to avoid, for instance, excessively large steps. In many schemes, $S$ is designed to be symmetric positive semidefinite, but it can be ill conditioned or rank deficient. A common remedy is to add a small diagonal damping term, $S  S + \epsilon I$ with $\epsilon > 0$ , which makes the system positive definite. This regularization augments the quadratic model in Eq. (3.8) with the term $\frac { \epsilon } { 2 } \parallel \pmb { \delta } \parallel _ { 2 } ^ { 2 }$ , where $\| \delta \| _ { 2 }$

is the Euclidean norm of the parameter update, thereby penalizing large displacements and favoring small-norm updates. However, with this simple regularization, all diagonal elements of the $S$ matrix are shifted by the same amount, neglecting potential order-of-magnitude differences in their typical changes [102].

To address this shortcoming, the authors of Ref. [50] introduce an RMSProp-inspired regularization by accumulating an exponentially decaying average of the squared gradients,

$$
\mathbf {v} _ {t} = \beta \mathbf {v} _ {t - 1} + (1 - \beta) \mathbf {g} _ {t} ^ {2}, \tag {3.11}
$$

and modifying the QGT as $S \to S + \epsilon \mathrm { d i a g } \bigl ( \sqrt { \mathbf { v } _ { t } } + 1 0 ^ { - 8 } \bigr )$ . In the original formulation of the SR algorithm, increasing $\epsilon$ suppresses the magnitude of the parameter update and rotates it toward the stochastic-gradient direction. In the RMSProp variant, the regularization instead biases the update toward the RMSProp direction, which typically leads to faster and more stable convergence than simple stochastic gradient descent.

Since the Fisher (QGT) matrix is of size $N _ { \mathrm { p a r } } { \times } N _ { \mathrm { p a r } }$ , its storage scales as $\mathcal { O } ( N _ { \mathrm { p a r } } ^ { 2 } )$ in memory, which quickly becomes infeasible. One way to overcome this limitation is to use iterative solvers, such as conjugate gradient [103] or MINRES [104], to solve the linear system associated with the SR update. Alternatively, Ref. [105] introduces an accelerated scheme, minSR, which leverages neural tangent kernel ideas to provide highly efficient inversions. Traditional ML preconditioners like K-FAC have also been employed to approximate $S$ and its inverse [45], although they were not originally devised for unsupervised settings such as standard NQS simulations [104].

SR is the most common approach for NQS optimization and, as noted above, aligns directly with the information geometry paradigm. However, alternative strategies based on different geometric principles can also be employed. Ref. [104] introduces the use of decision geometry within the NQS setting. Decision geometry [106] reduces to information geometry for specific choices of scoring rules and can therefore be viewed as a game-theoretic generalization of standard probabilistic optimization schemes. An appealing feature of this framework is the flexibility to choose among different (proper) scoring rules, while still obtaining well-behaved updates with positive semidefinite preconditioning metrics [107]. A scoring rule tailored to one-dimensional continuous fermion systems showed promising performance in Ref. [104], and further explorations for other systems are underway.

Finally, it is worth noting that iterative ML optimizers often exploit the history of the search via a momentum term: the update $\delta$ from iteration $k { - } 1$ is stored so that the update at iteration $k$ depends on both the current gradient and the previous step. Momentum-based schemes used in NQS include variants of RMSProp [47, 100]. By contrast, standard choices widely used in other neural-network contexts (e.g., stochastic gradient descent or Adam [108]) can be insufficient to achieve the percent-level accuracy typically required for ground-state energies in NQS. A recent example that incorporates step history in a natural-gradient setting is the Subsampled Projected-Increment Natural Gradient (SPRING) method [109]. In this approach, the quadratic model of Eq. (3.8) is augmented with a term $\frac { \epsilon } { 2 } \parallel \delta - \mu \delta _ { \mathrm { p r e v } } \parallel _ { 2 } ^ { 2 }$ , where $\delta _ { \mathrm { p r e v } }$ denotes the previous parameter update and $\mu < 1$ is a damping factor. This proximal term is centered at $\mu \delta _ { \mathrm { p r e v } }$ , pulling the new step toward the previous one rather than merely penalizing its magnitude.

# 3.3. Basics of deep learning

In nuclear physics, the simultaneous treatment of continuous spatial degrees of freedom and discrete spin and isospin degrees of freedom typically requires deep neural architectures composed of multiple multilayer perceptrons (MLPs). These individual MLPs are interconnected in structured ways to enforce the physical symmetries of the quantum manybody system. MLPs are widely recognized as one of the most prominent forms of artificial neural networks (ANN),

primarily due to their training simplicity and scalability. However, they can be prone to overfitting in situations where a large data set cannot be made available. VMC-NQS is less prone to this issue, since the number of Monte Carlo samples used to estimate the energy can be increased to improve the effective training set.

A multilayer perceptron is a type of deep feedforward neural network defined by alternating compositions of affine transformations and simple, nonlinear transformations. It consists of an input layer, at least one hidden layer, and an output layer, all of which are densely connected to the adjacent layers only. As the name implies, information flows only in one direction, starting from the input layer and ending at the output layer. For an MLP with $L$ layers (including the hidden and output layers, but excluding the input layer), we define the layers as

$$
\boldsymbol {h} ^ {(0)} = \boldsymbol {v} \in \mathbb {R} ^ {d _ {0}}, \tag {3.12}
$$

$$
\boldsymbol {h} ^ {(\ell)} = f _ {\ell} \left(W ^ {(\ell)} \boldsymbol {h} ^ {(\ell - 1)} + \boldsymbol {b} ^ {(\ell)}\right) \in \mathbb {R} ^ {d _ {\ell}}, \quad \text {f o r} \ell = 1, \dots , L, \tag {3.13}
$$

where $_ { \pmb { v } }$ denotes the vector of visible nodes for the input layer $\mathbf { \varepsilon } _ { h } ^ { ( 0 ) }$ ; $\mathbf { \Omega } _ { h } ^ { ( \ell ) }$ are the hidden layers for $\ell = 1 , \ldots , L - 1$ ; $\mathbf { \Omega } _ { h } ^ { ( L ) }$ is the output layer; and $f _ { \ell }$ represents the nonlinear activation function in the $\ell \cdot$ -th layer. Each hidden layer has dimension $d _ { \ell }$ , meaning $W ^ { ( \ell ) }$ is a $d _ { \ell } \times d _ { \ell - 1 }$ weight matrix and $\pmb { b } ^ { ( \ell ) }$ is a $d _ { \ell }$ -dimensional bias vector. The activation functions $f _ { \ell }$ introduce nonlinearity to the network, enabling it to learn and approximate complex functions. Without at least one nonlinear activation function, the neural network reduces to a purely linear model. In NQS applications for continuous-space systems, the activation functions in the hidden layers should be at least twice continuously differentiable to enable the stable computation of the local kinetic energy. If the target space is unbounded, the activation function for the output layer $f _ { L }$ is usually chosen to be the identity.

Gradients of MLPs with respect to the weights $W ^ { ( \ell ) }$ and biases $\pmb { b } ^ { ( \ell ) }$ are efficiently computed through backpropagation, which applies the chain rule recursively:

$$
\frac {\partial \boldsymbol {h} ^ {(L)}}{\partial W ^ {(\ell)}} = \left(\prod_ {k = \ell + 1} ^ {L} \frac {\partial \boldsymbol {h} ^ {(k)}}{\partial \boldsymbol {h} ^ {(k - 1)}}\right) \frac {\partial \boldsymbol {h} ^ {(\ell)}}{\partial W ^ {(\ell)}}, \quad \frac {\partial \boldsymbol {h} ^ {(L)}}{\partial \boldsymbol {b} ^ {(\ell)}} = \left(\prod_ {k = \ell + 1} ^ {L} \frac {\partial \boldsymbol {h} ^ {(k)}}{\partial \boldsymbol {h} ^ {(k - 1)}}\right) \frac {\partial \boldsymbol {h} ^ {(\ell)}}{\partial \boldsymbol {b} ^ {(\ell)}}. \tag {3.14}
$$

In deep architectures, the repeated multiplication of layer Jacobians can cause gradients to vanish or explode, as the eigenvalues of these matrices can be much smaller or larger than unity. Modern architectures mitigate this effect through skip connections, which facilitate gradient flow by providing alternative paths for information propagation. Two common forms are the residual skip connection,

$$
\boldsymbol {h} ^ {(\ell + 1)} = \boldsymbol {h} ^ {(\ell)} + F _ {\ell} \left(\boldsymbol {h} ^ {(\ell)}\right), \tag {3.15}
$$

and the concatenative skip connection,

$$
\boldsymbol {h} ^ {(\ell + 1)} = \operatorname {c o n c a t} \left(\boldsymbol {h} ^ {(\ell)}, F _ {\ell} \left(\boldsymbol {h} ^ {(\ell)}\right)\right), \tag {3.16}
$$

where $F _ { \ell }$ typically denotes a feedforward transformation (e.g. an MLP block). The additive, or residual, form preserves dimensionality and is widely used for stabilizing deep networks, while the concatenative form aggregates intermediate features, allowing later layers to access information from all previous representations.

To represent complex wave functions using deep neural networks with real parameters, one possible strategy is to predict the real and imaginary parts of the wave function separately, for instance using two output nodes in the final layer or two distinct networks. However, optimization is typically more stable when the network instead predicts the log-amplitude $\log | \Psi _ { V } |$ and phase $\Phi _ { V } = \arg ( \Psi _ { V } )$ . In this parameterization, $\Psi _ { V } = e ^ { \log | \Psi _ { V } | + i \Phi _ { V } }$ , the log-derivative reduces to $\nabla \log \Psi _ { V } = \nabla \log | \Psi _ { V } | + i \nabla \Phi _ { V }$ , so that the quantities entering the VMC estimators are directly given by smooth network

![](images/0aeded2bc6f3b73d98d3ae891d011f68f7a0e54bcfc413d9adb2bd59efc6949d.jpg)  
Figure 3.2: Cartoon of a Deep Set architecture (adapted from Ref. [111])

outputs. This leads to numerically well-behaved gradients and reduces the risk of vanishing or exploding updates during training.

A major advantage of deep neural networks is their flexibility to incorporate physical symmetries directly into the architecture. For systems of identical particles, the wave function must be symmetric under particle exchange for bosons and antisymmetric for fermions. In both cases, it is useful to construct permutation-invariant components so that the network naturally treats particles as indistinguishable, without requiring explicit handling of all possible particle permutations, whose number grows factorially with system size. The Deep Sets [110] construction provides a simple way to build such invariant representations,

$$
f \left(\left\{\mathbf {x} _ {i} \right\} _ {i = 1} ^ {A}\right) = \rho \left(\operatorname {p o o l} \left(\left\{\phi \left(\mathbf {x} _ {i}\right) \right\} _ {i = 1} ^ {A}\right)\right), \tag {3.17}
$$

where $\mathbf { x } _ { i } = \left( \mathbf { r } _ { i } , s _ { i } ^ { z } , t _ { i } ^ { z } \right)$ denotes the single-particle degrees of freedom of the ith nucleon; $\phi$ and $\rho$ are learnable maps; and pool is a permutation-invariant aggregation operation (e.g., sum, mean, or logsumexp). Here, $\phi$ embeds each element of the set into a higher-dimensional latent space, pool combines all elements into a single latent representation of the set, and $\rho$ maps this representation to the desired output space. This construction can be applied similarly to the set of all pairwise degrees of freedom.

A wide range of architectural components can be incorporated to further enhance the flexibility and expressive power of neural networks. One prominent example is the use of attention mechanisms [112], which dynamically weigh the importance of different elements in an input sequence when making predictions. Instead of processing all input features equally, attention allows the network to focus selectively on the most relevant parts, effectively learning context-dependent weighting. They form the foundation of modern large language models, enabling them to capture long-range dependencies and nuanced contextual relationships, and have recently been incorporated into neural quantum state architectures to enhance the representation of complex correlations in many-body wavefunctions [113–115].

The standard formulation of the self-attention mechanism [112] computes queries, keys and values for each element of the input through linear transformations,

$$
Q = X W _ {Q}, \quad K = X W _ {K}, \quad V = X W _ {V}. \tag {3.18}
$$

As a minimal example, consider the input matrix $X \in \mathbb { R } ^ { A \times 5 }$ , chosen to represent the row-wise collection of all singlenucleon degrees of freedom, corresponding to the three spatial coordinates together with the spin and isospin labels. One could alternatively construct $X$ to represent pair degrees of freedom or, more generally, the output of a preceding neural network layer. Choosing the query and key weight matrices $W _ { Q }$ and $W _ { K }$ to have dimension $5 \times d _ { k }$ , the value weight matrix $W _ { V }$ will have dimension $5 \times d _ { v }$ , yielding $Q , K \in \mathbb { R } ^ { A \times d _ { k } }$ and $V \in \mathbb { R } ^ { A \times d _ { v } }$ . The output of the attention layer is obtained

by comparing the query of each particle with the keys of all others, producing a set of normalized weights that are then applied to the values to generate a context-aware representation,

$$
\operatorname {a t t n} (Q, K, V) = \operatorname {s o f t m a x} _ {i} \left(\frac {Q K ^ {T}}{\sqrt {d _ {k}}}\right) V. \tag {3.19}
$$

The intermediate matrix $Q K ^ { T } \in \mathbb { R } ^ { A \times A }$ encodes all pairwise similarities between particles and is effectively bilinear in $X$ . The row-wise softmax $_ i$ activation function converts each row into a normalized probability distribution, and the factor of $1 / \sqrt { d _ { k } }$ aids numerical stability.

# 3.4. Wave function ansätze

Here we review the principal wave function ansätze that have been used in “first-quantized” NQS approaches to nuclear physics. These architectures act directly on the continuous spatial coordinates and spin–isospin degrees of freedom of the nucleons.

# 3.4.1. Slater–Jastrow

Initial applications of the NQS framework to atomic nuclei [48] extended the Slater–Jastrow (SJ) architecture, originally developed for quantum chemistry [44, 45], to handle the complex spin–isospin structure of nuclear interactions. Such an ansatz can be schematically written as

$$
\Psi_ {\mathrm {S J}} (X) = F (X) \Phi (X), \tag {3.20}
$$

where $F ( X )$ is a permutation-invariant Jastrow factor, and antisymmetry is enforced by the mean-field-like component $\Phi ( X )$ . For compactness, we use $X \ = \ \left( x _ { 1 } , \ldots , x _ { A } \right)$ to denote the collection of all single-particle degrees of freedom $x _ { i } = \left( \mathbf { r } _ { i } , s _ { i } ^ { z } , t _ { i } ^ { z } \right)$ , namely the three-dimensional spatial coordinates $\mathbf { r } _ { i }$ and the spin and isospin projections along the $z$ -axis.

The mean-field term $\Phi ( X )$ is typically expressed as a sum of Slater determinants of single-particle orbitals [48, 49, 116]. For atomic nuclei, it takes the form

$$
\Phi (X) = \left[ \sum_ {\mu} C _ {\mu} \mathcal {A} \left[ \phi_ {\alpha_ {1} ^ {\mu}} \left(x _ {1}\right) \phi_ {\alpha_ {2} ^ {\mu}} \left(x _ {2}\right) \dots \phi_ {\alpha_ {A} ^ {\mu}} \left(x _ {A}\right) \right] \right] _ {J ^ {\pi} T}, \tag {3.21}
$$

where $\mathcal { A }$ is the antisymmetrization operator acting on the particle labels $x _ { i }$ , and $\{ C _ { \mu } \}$ are configuration amplitudes that incorporate the Clebsch–Gordan couplings required to form a many-body state $\mu$ with the desired total angular momentum, parity, and isospin $J ^ { \pi } T$ for the nucleus of interest. The single-particle orbitals are evaluated as

$$
\phi_ {\alpha} \left(x _ {i}\right) = \mathcal {R} _ {n l} \left(r _ {i}\right) Y _ {\hat {l} l ^ {z}} \left(\hat {r} _ {i}\right) \left\langle s _ {i} ^ {z} \mid s ^ {z} \right\rangle \left\langle t _ {i} ^ {z} \mid t ^ {z} \right\rangle , \tag {3.22}
$$

where $\alpha = \left( n , l , l ^ { z } , s ^ { z } , t ^ { z } \right)$ are the quantum numbers, $\langle s _ { i } ^ { z } | s ^ { z } \rangle = \delta _ { s _ { i } ^ { z } , s ^ { z } }$ and $\langle t _ { i } ^ { z } | t ^ { z } \rangle = \delta _ { t _ { i } ^ { z } , t ^ { z } }$ project onto the fixed spin and isospin, $\mathcal { R } _ { n l } ( r _ { i } )$ are the radial functions parametrized by MLPs, and $Y _ { l l ^ { z } } \left( \hat { r } _ { i } \right)$ are the spherical harmonics.

To automatically remove the spurious center-of-mass contribution from the kinetic energy, the spatial coordinates are replaced by ${ \bf r } _ { i }  { \bf r } _ { i } - { \bf R } _ { \mathrm { C M } }$ , with $\begin{array} { r } { \mathbf { R } _ { \mathrm { C M } } = \frac { 1 } { A } \sum _ { i = 1 } ^ { A } \mathbf { r } _ { i } } \end{array}$ being the center-of-mass coordinate [117]. Since the network parameters are randomly initialized, in the early stages of training the Metropolis–Hastings walk can let the nucleons drift away from $\mathbf { R } _ { \mathrm { C M } }$ . To control this behavior, a Gaussian factor is multiplied by the single-particle radial functions to confine the nucleons within a finite volume,

$$
\mathcal {R} _ {n l} (r _ {i}) \rightarrow \mathcal {R} _ {n l} (r _ {i}) e ^ {- \alpha r _ {i} ^ {2}}. \tag {3.23}
$$

Typical values for the confining constant are in the range $\alpha = 0 . 0 2 – 0 . 0 5 \ \mathrm { f m ^ { - 2 } }$ .

In Refs. [48, 49, 116], the real-valued Jastrow correlator was taken to be of the form

$$
F (X) = e ^ {\mathcal {U} (X)} \tanh  [ \mathcal {V} (X) ]. \tag {3.24}
$$

Here, the positive-definite exponential is modulated by a hyperbolic tangent, which acts as a smooth surrogate for the sign. The functions $\boldsymbol { \mathcal { U } } ( \boldsymbol { X } )$ and $\mathcal { V } ( X )$ are implemented as permutation-invariant neural networks. Several architectures have been developed to represent such functions efficiently, including point-cloud [118] and attention-based [112, 119, 120] models. Among these, the authors of Ref. [48] found the Deep Sets architecture [110, 121] to be a practical and sufficiently accurate choice, discussed further in Section 3.3.

In particular, each single-particle input $x _ { i }$ is mapped independently to a latent representation, and a sum aggregation is applied to enforce permutation invariance:

$$
\mathcal {U} (X) = \rho_ {\mathcal {U}} \left(\sum_ {i = 1} ^ {A} \phi_ {\mathcal {U}} \left(x _ {i}\right)\right), \quad \mathcal {V} (X) = \rho_ {\mathcal {V}} \left(\sum_ {i = 1} ^ {A} \phi_ {\mathcal {V}} \left(x _ {i}\right)\right). \tag {3.25}
$$

Both $\phi _ { \mathcal { U } }$ and $\rho _ { \mathcal { U } }$ (and analogously $\phi _ { \gamma }$ and $\rho _ { \mathcal { V } }$ ) are typically implemented as MLPs. Computing the kinetic energy (Laplacian) requires activation functions that are differentiable (ideally twice). Standard choices include hyperbolic tangent, softplus [122], and GELU [123].

Instead of single-particle inputs as in Ref. [124], Ref. [116] maps the coordinates of each particle pair directly to a latent-space representation, in close analogy with earlier condensed-matter applications [44, 45]. As before, a sum aggregation removes any dependence on particle ordering and therefore enforces permutation invariance:

$$
\mathcal {U} (X) = \rho_ {\mathcal {U}} \left(\sum_ {i \neq j} \phi_ {\mathcal {U}} \left(x _ {i}, x _ {j}\right)\right), \quad \mathcal {V} (X) = \rho_ {\mathcal {V}} \left(\sum_ {i \neq j} \phi_ {\mathcal {V}} \left(x _ {i}, x _ {j}\right)\right). \tag {3.26}
$$

When single-particle coordinates are used as input, correlations are generated in the latent feature space by the aggregation network $\rho \mathcal { F }$ , where we use $\mathcal { F } \in \{ \mathcal { U } , \mathcal { V } \}$ to denote either of the two correlator networks. By contrast, using pair coordinates introduces correlations already at the level of the real-space inputs. The conventional two-body Jastrow ansatz is recovered when the latent dimension is one and $\rho \mathcal { F }$ is taken to be the identity, $\rho \mathcal { F } ( x ) = x$ . In a similar spirit, Ref. [49] feeds only rotationally invariant one- and two-body features to $\phi _ { \mathcal { U } }$ and $\phi _ { \gamma }$ , namely $\left\| \mathbf { r } _ { i } \right\|$ , $\| \mathbf { r } _ { j } \|$ , and $\| \mathbf { r } _ { i } - \mathbf { r } _ { j } \|$ , while neglecting spin– isospin dependence. This choice significantly reduces the number of variational parameters without compromising the accuracy of the resulting energies.

# 3.4.2. Operator-dependent Slater–Jastrow

Very recently, VMC methods based on NQS [57, 58, 66] have been applied to the nuclear many-body problem using highresolution phenomenological and chiral-EFT Hamiltonians that are local in coordinate space. To address the strongly nonperturbative character of these interactions, in particular their tensor component, the NQS includes explicit spin–isospin operator dependence, as in Eq. (2.15). To keep a polynomial computational cost in the number of nucleons, the ansatz introduced in Ref. [66] is expressed in the same linearized form used in AFDMC, reported in Eq. (2.20), namely

$$
\Psi_ {V} (R, S) = e ^ {\mathcal {U}} (R) \tanh  [ \mathcal {V} (R) ] \left(1 + \sum_ {i <   j} \sum_ {p = 1} ^ {6} W _ {i j} ^ {p} (R) O _ {i j} ^ {p}\right). \tag {3.27}
$$

As a reminder, the first six spin-isospin operators are $O _ { i j } ^ { p = 1 , 6 } \ = \ \left( 1 , \tau _ { i j } , \sigma _ { i j } , \sigma _ { i j } \tau _ { i j } , S _ { i j } , S _ { i j } \tau _ { i j } \right)$ . The central correlation functions $\mathcal { U } ( R )$ and $\mathcal { V } ( R )$ are represented by the spin–isospin independent permutation-invariant neural network of Eq. (3.26), introduced in Ref. [49]. Importantly, this construction ensures both translational and rotational invariance.

Contrary to conventional GFMC and AFDMC trial wave functions, in which the pair correlation functions $W _ { i j } ^ { p }$ depend only on the relative coordinate of particles $_ i$ and $j$ , the present ansatz makes $W _ { i j } ^ { p }$ a functional of the full configuration $R$ . This is achieved using the Deep Sets architecture, discussed above and in Section 3.3, which incorporates information from all particles through

$$
W _ {i j} ^ {p} (R) = \rho_ {\mathcal {W}} ^ {p} \left(\sum_ {k = 1} ^ {A} \phi_ {\mathcal {W}} \left(r _ {i k}, r _ {j k}, r _ {i j}\right)\right), \tag {3.28}
$$

where $\phi _ { \mathcal { W } }$ and $\rho _ { \mathcal { W } }$ are feedforward neural networks, each with a single fully connected hidden layer. This global dependence allows the pair correlations to adapt to the surrounding many-body environment. As a result, these wave functions provide an excellent starting point for GFMC calculations and were used in Ref. [66] to compute peripheral neutron– $\alpha$ scattering with high accuracy. A more detailed discussion of these results is given in Section 4.5.

A similar ansatz, but incorporating the symmetrized product of two-body correlations—see Eq. (2.15) for its conventional counterpart—has been proposed by the authors of Ref. [57]:

$$
\Psi_ {V} (R, S) = \left(1 + \sum_ {i <   j <   k} F _ {i j k}\right) \prod_ {i <   j} f _ {i j} ^ {c} (R) \left(1 + \sum_ {p = 2} ^ {6} u _ {i j} ^ {p} (R) O _ {i j} ^ {p}\right). \tag {3.29}
$$

The three-body correlation functions $F _ { i j k }$ are defined analogously to Eq. (2.17). As in the ansatz of Ref. [57], all radial functions entering the two- and three-body correlations depend on the full configuration $R$ . A representative example is the operator-dependent correlation,

$$
u _ {i j} ^ {p} (R) = \rho_ {u} ^ {p} \left(r _ {i j}, \sum_ {k \neq i, j} \left[ \phi_ {u} \left(r _ {i j}\right) + \phi_ {u} \left(r _ {i k}\right) \right]\right), \tag {3.30}
$$

where both $\rho _ { u } ^ { p }$ and $\phi _ { u }$ are feed-forward neural networks composed of multiple one-dimensional transformation layers connected by residual blocks and employing the RiLU activation function.

An important difference from previous NQS implementations is that this approach leverages normalizing flows to produce uncorrelated samples to solve the nuclear Schrödinger equation, as opposed to Metropolis–Hastings sampling. As a consequence, it avoids the autocorrelation issues inherent in Metropolis–Hastings and reduces the overall computational cost. Normalizing flows [125–127] generate samples by drawing an initial batch from a simple uniform distribution, implemented here using a Sobol quasi-random sequence, and passing it through a series of invertible change-of-variable transformations with tractable derivatives and Jacobians. By optimizing the parameters of the flow, the resulting distribution can be made to closely approximate the target distribution. Results for the $A = 3$ nuclei obtained with this ansatz and the local chiral-EFT interactions of Ref. [56] will also be summarized in Section 4.5.

# 3.4.3. Hidden Nucleons

A systematically improvable family of variational wave functions for strongly correlated fermionic systems was introduced in Ref. [128]. These wave functions are built from Slater determinants in an augmented Hilbert space that includes additional, “hidden” fermionic degrees of freedom. The authors demonstrated that this ansatz is universal on the lattice and applied it to the ground-state properties of the Hubbard model on the square lattice, achieving accuracies competitive with state-of-the-art variational methods. This framework was subsequently extended to nuclear systems, whose Hilbert spaces involve both continuous and discrete degrees of freedom [50]. In this formulation, the Hilbert space includes fictitious coordinates for $A _ { h }$ Hidden Nucleons (HN), defined as functions of the visible coordinates $X _ { h } \ = \ f ( X )$ . The

amplitudes of the HN wave function in the $X$ basis can be written schematically as

$$
\Psi_ {\mathrm {H N}} (X) \equiv \det  \left[ \begin{array}{l l} \Phi_ {v} (X) & \Phi_ {v} \left(X _ {h}\right) \\ \chi_ {h} (X) & \chi_ {h} \left(X _ {h}\right) \end{array} \right], \tag {3.31}
$$

where $\Phi _ { v } ( X )$ denotes the $A \times A$ matrix of visible single-particle orbitals evaluated at the visible coordinates, equivalent to the mean-field term $\Phi ( X )$ of Eq. (3.21). This would be the only component of the wave function in a Hartree–Fock description. In contrast to the original implementation of Ref. [128], the columns of the matrix in Eq. (3.31) correspond to different particles, while the rows correspond to different single-particle states. The $A _ { h } \times A _ { h }$ matrix $\chi _ { h } ( X _ { h } )$ contains the amplitudes of hidden orbitals evaluated at hidden coordinates, whereas $\chi _ { h } ( X )$ and $\Phi _ { v } ( X _ { h } )$ provide the amplitudes of hidden orbitals at visible coordinates and visible orbitals at hidden coordinates, respectively. The SJ ansatz of Eq. (3.20) is recovered in the limit $A _ { h } = 1$ , $\chi _ { h } ( X ) = 0$ , and $\Phi _ { v } ( X _ { h } ) = 0$ , allowing one to interpret it as a special case of the HN formulation. If the function $f$ is permutation invariant, $\Psi _ { \mathrm { H N } } ( X )$ is automatically antisymmetric under particle exchange. The expressivity of this construction for discrete degrees of freedom was formally proven in Ref. [128], provided that the functions $\chi _ { h }$ and $f$ are sufficiently general. To avoid the combinatorial complexity of $f$ , the $i$ -th columns of $\Phi _ { v } ( X _ { h } )$ and $\chi _ { h } ( X _ { h } )$ are parametrized by independent, permutation-invariant neural networks as

$$
\Phi_ {v} ^ {i} (X _ {h}) = e ^ {\mathcal {U} _ {\Phi} ^ {i} (X)} \tanh [ \mathcal {V} _ {\Phi} ^ {i} (X) ], \qquad \chi_ {h} ^ {i} (X _ {h}) = e ^ {\mathcal {U} _ {\chi} ^ {i} (X)} \tanh [ \mathcal {V} _ {\chi} ^ {i} (X) ]. \tag {3.32}
$$

A more recent implementations of the HN ansatz [52] employs complex-valued matrices of the form

$$
\Phi_ {v} ^ {i} \left(X _ {h}\right) = e ^ {\mathcal {U} _ {\Phi} ^ {i} (X) + i \mathcal {V} _ {\Phi} ^ {i} (X)}, \quad \chi_ {h} ^ {i} \left(X _ {h}\right) = e ^ {\mathcal {U} _ {x} ^ {i} (X) + i \mathcal {V} _ {x} ^ {i} (X)}. \tag {3.33}
$$

In both formulations, permutation invariance is enforced using Deep Sets architectures [110, 121] to express the functions $\mathcal { U } _ { \Phi } ^ { i }$ , $\mathcal { V } _ { \Phi } ^ { i }$ , $\mathcal { U } _ { \chi } ^ { i }$ , and $\mathcal { V } _ { \chi } ^ { i }$ . For applications to finite nuclei [50] and dilute neutron matter [53], a logsumexp pooling operation replaces the simple sums in Eqs. (3.25) and (3.26),

$$
\mathcal {F} (X) = \rho_ {\mathcal {F}} \left[ \log \left(\sum_ {i} e ^ {\phi_ {\mathcal {F}} \left(x _ {i}\right)}\right) \right]. \tag {3.34}
$$

In these works, $\phi _ { \mathcal { F } }$ and $\rho \mathcal { F }$ are implemented as MLPs with two hidden layers of 16 nodes each, and a 16-dimensional latent space connecting them. The output layers of $\rho \mathcal { F }$ contain $A$ nodes for $\mathcal { F } = \mathcal { U } _ { \Phi } ^ { i } , \mathcal { V } _ { \Phi } ^ { i }$ and $A _ { h }$ nodes for $\mathcal { F } = \mathcal { U } _ { \chi } ^ { i } , \mathcal { V } _ { \chi } ^ { i }$ . An ablation study in Ref. [50] examined the convergence of the 4He ground-state energy with network size and found that increasing the number of hidden layers or nodes beyond this configuration provided no substantial improvement, while smaller networks slightly degraded the accuracy (by about 0.2 MeV). The single-particle orbitals defining $\Phi _ { v } ( X )$ and $\chi _ { h } ( X )$ are also represented by MLPs that take as input the single-particle coordinates $x _ { i }$ . In Refs. [50, 53], these networks had two hidden layers with ten nodes each, tanh activation functions, and one-dimensional linear outputs. Other differentiable activations such as softplus and GELU were tested without appreciable differences. Differentiability is required to compute the kinetic energy, which involves second derivatives of the wave function. Unlike in the Slater–Jastrow case, confinement is not imposed at the single-particle level. Instead, the full wave function in Eq. (3.31) is multiplied by a global Gaussian factor,

$$
\Psi_ {\mathrm {H N}} (X) \rightarrow \Psi_ {\mathrm {H N}} (X), e ^ {- \alpha \sum_ {i = 1} ^ {A} r _ {i} ^ {2}}, \tag {3.35}
$$

which ensures spatial localization of the system.

![](images/5dabfc870cd4c2dfa7f5a93a30ed0bdc1e694112ba4f83466b67ad1811234744.jpg)

![](images/f008b83f24c76b4eaa288e24e2a3f5d237b2df55035b81e81d525459e03627c9.jpg)  
Figure 3.3: From Ref. [50] with permission from the Authors. Left panel: Convergence of the $^ 4 \mathrm { H e }$ ground-state energy obtained with the parityprojected HN ansatz (blue solid circles) and with the ansatz that enforces both parity and time-reversal symmetry (orange solid circles). The SJ and the hyper-spherical harmonics ground-state energies from Ref. [116] are shown by the purple dashed and solid green lines, respectively. Right panel: Convergence of the parity-projected ansatz when employing a wider neural-network architecture than in the left panel.

When introducing the HN ansatz, the authors of Ref. [50] found it beneficial to enforce point symmetries, such as parity and time reversal. For positive- and negative-parity states, one can impose

$$
\Psi_ {\mathrm {H N}} ^ {P ^ {+}} (X) = \Psi_ {\mathrm {H N}} (R, S) + \Psi_ {\mathrm {H N}} (- R, S),
$$

$$
\Psi_ {\mathrm {H N}} ^ {P ^ {-}} (X) = \Psi_ {\mathrm {H N}} (R, S) - \Psi_ {\mathrm {H N}} (- R, S). \tag {3.36}
$$

For even-even nuclei, such as $^ 4$ He and $^ { 1 6 }$ O, it is also possible to enforce time-reversal symmetry,

$$
\Psi_ {\mathrm {H N}} ^ {T} (X) \equiv \Psi_ {\mathrm {H N}} (R, S) + \Psi_ {\mathrm {H N}} ^ {*} (R, \theta S). \tag {3.37}
$$

where $\theta S$ is obtained by applying the operator $- i \sigma _ { y }$ to all single-particle spinors [129]. Note that, unlike the expression reported in Ref. [50], we explicitly take the complex conjugate, so that the construction applies to both real- and complexvalued NQS. Importantly, time reversal and parity have been combined, to form a simultaneous eigenstate of parity and time reversal, dubbed $\Psi _ { \mathrm { H N } } ^ { P T } ( X )$ .

The convergence of the $^ { 4 } \mathrm { H e }$ ground-state energy computed with $A _ { h } = 4$ HN is displayed in Fig. 3.3. The parityconserving wave function $\Psi _ { H N } ^ { P } ( R , S )$ is outperformed by $\Psi _ { H N } ^ { P I ^ { \prime } } ( R , S )$ , which additionally preserves time-reversal symmetry. Both provide significantly better energies than the SJ results of Ref. [92], as they can improve the nodal surface of the single-particle Slater determinant. In fact, $\Psi _ { \mathrm { H N } } ^ { P I ^ { \prime } } ( R , S )$ yields a variational energy consistent with the numerically exact HH estimate of Ref. [92].

It is worth noting that $\Psi _ { H N } ^ { P } ( R , S )$ should, in principle, converge to the exact energy, but this may require wider (or deeper) architectures. To illustrate this point, the right panel of Fig. 3.3 displays the training of $\Psi _ { H N } ^ { P } ( R , S )$ with $A _ { h } = 4$ , in which the number of nodes in the hidden layers of $\phi _ { \mathcal { F } }$ and $\rho \mathcal { F }$ has been increased from 16 to 24. After about 4800 optimization steps, the parity-conserving ansatz yields energies that are consistent with the HH method. Importantly, though, enforcing time-reversal symmetry in the ansatz is effective in reducing the training time and appears to enhance the expressivity of the HN ANN architecture.

# 3.4.4. Pfaffian–Jastrow

Pfaffian–Jastrow neural architectures were originally introduced to describe the unitary Fermi gas [54], where strong pairing correlations dominate. The same pairing-based formulation was later shown to be advantageous for nuclei and dilute neutron-star matter [55]. These neural architectures build on a long history of pairing wave functions in quantum Monte Carlo studies of ultracold Fermi gases, in which the many-body state is written as an antisymmetrized product of spin-singlet pairs [130–133]. These can be thought of as Bardeen–Cooper–Schrieffer (BCS) pairs within the nuclear context.

In the literature, this class of pairing states appears under several closely related names, including geminal wave functions [134, 135], number-projected BCS [136], and singlet-pairing wave functions [137]. These ansätze already provide a substantial improvement over single-determinant Slater states. However, their effectiveness is reduced in partially spinpolarized systems, since only the spin-singlet pairing channel is included [135]. This limitation motivated the introduction of the singlet–triplet–unpaired (STU) Pfaffian wave function [137, 138], which generalizes the geminal form by explicitly incorporating both singlet and triplet pairing channels, together with a separate sector for unpaired particles. In this formulation, the many-body wave function is written as the Pfaffian of a block matrix collecting singlet, triplet, and unpaired contributions. The original geminal ansatz is recovered as a special case when the triplet blocks are set to zero.

A key limitation of both geminal and STU wave functions in their original formulations is that they assume a fixed spin ordering of the fermions. This is perfectly adequate for model Hamiltonians with conserved spin species, but it is not well suited to nuclear interactions, which contain explicit spin-exchange terms and couple different spin–isospin channels [139]. In neutron-matter applications, this issue is commonly circumvented by expressing the Pfaffian pairing orbital as a plane-wave expansion weighted by BCS amplitudes and multiplied by a spin-singlet component [140]:

$$
\phi (x _ {i}, x _ {j}) = \sum_ {\alpha} c _ {\alpha} e ^ {i \mathbf {k} _ {\alpha} \cdot (\mathbf {r} _ {i} - \mathbf {r} _ {j})} \left(\frac {\eta_ {\uparrow} (s _ {i} ^ {z}) \eta_ {\downarrow} (s _ {j} ^ {z}) - \eta_ {\downarrow} (s _ {i} ^ {z}) \eta_ {\uparrow} (s _ {j} ^ {z})}{\sqrt {2}}\right), \tag {3.38}
$$

where $x _ { i } = \left( \mathbf { r } _ { i } , s _ { i } ^ { z } \right)$ , $\begin{array} { r } { \mathbf { k } _ { \alpha } = \frac { \cdot 2 \pi } { L } \big ( n _ { x } \hat { \mathbf { x } } + n _ { y } \hat { \mathbf { y } } + n _ { z } \hat { \mathbf { z } } \big ) } \end{array}$ denotes the momenta compatible with the periodic boundary conditions, and the complex-valued $c _ { \alpha }$ are variational parameters. While in neutron matter the spin-triplet channel is typically neglected, it can be incorporated within the same framework without requiring fixed spin ordering.

By introducing neural network representations of the pairing orbital, the Pfaffian can be employed in its most general form, capturing arbitrary spin–isospin–dependent correlations without relying on fixed assumptions about the pairing channel. For an even number of nucleons $A$ , the Pfaffian–Jastrow wave function is written as

$$
\Psi_ {P J} ^ {\text {e v e n}} (X) = e ^ {J (X)} \operatorname {p f} [ P (X) ], \tag {3.39}
$$

where $J ( X )$ is a Jastrow factor and $P ( X )$ is an $A \times A$ skew-symmetric matrix whose elements define the pairing orbital between any two nucleons. The antisymmetric structure of the wave function is thus fully encoded in the pairing matrix $P ( X )$ , given by [54, 55]

$$
P (X) = \left[ \begin{array}{c c c c c} 0 & \phi \left(x _ {1}, x _ {2}\right) & \phi \left(x _ {1}, x _ {3}\right) & \dots & \phi \left(x _ {1}, x _ {A}\right) \\ - \phi \left(x _ {1}, x _ {2}\right) & 0 & \phi \left(x _ {2}, x _ {3}\right) & \dots & \phi \left(x _ {2}, x _ {A}\right) \\ - \phi \left(x _ {1}, x _ {3}\right) & - \phi \left(x _ {2}, x _ {3}\right) & 0 & \dots & \phi \left(x _ {3}, x _ {A}\right) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ - \phi \left(x _ {1}, x _ {A}\right) & - \phi \left(x _ {2}, x _ {A}\right) & - \phi \left(x _ {3}, x _ {A}\right) & \dots & 0 \end{array} \right]. \tag {3.40}
$$

Similarly to the most recent implementations of the HN ansatz, the Jastrow factor is complex-valued [55] and can be written as

$$
F (X) = e ^ {\left[ \mathcal {U} (X) + i \mathcal {V} (X) \right]}, \tag {3.41}
$$

where $\boldsymbol { u }$ and $\nu$ are real functions that encode two-body correlations in the modulus and phase of the wave function, respectively. As in the real-valued case, the pairwise Deep-Sets construction of Eq. (3.26) is typically employed, so that two-body correlations are built directly in coordinate space rather than in the latent feature space.

Alternatively, the pairing orbital can be taken to be a sum over products of single-particle orbitals,

$$
\phi \left(x _ {i}, x _ {j}\right) = \sum_ {\alpha , \beta} c _ {\alpha \beta} \phi_ {\alpha} ^ {*} \left(x _ {i}\right) \phi_ {\beta} \left(x _ {j}\right), \tag {3.42}
$$

where the single-particle orbitals $\phi _ { \alpha } ( x )$ are those defined in Eq. (3.22). This strategy has also been adopted in recent condensed-matter applications of the Pfaffian family of wave functions [141], where the elements of the antisymmetric matrix $c _ { \alpha \beta }$ are treated as variational parameters. For a closed-shell system, the Slater–Jastrow ansatz is recovered by restricting the sum to the occupied orbitals and choosing $c _ { \alpha \beta }$ to be antisymmetric and nonzero only between time-reversed partners $( \alpha , \bar { \alpha } )$ , e.g. $c _ { \alpha \bar { \alpha } } = 1$ , $c _ { \bar { \alpha } \alpha } = - 1$ , with all other $c _ { \alpha \beta } = 0$ . This choice forms antisymmetric pairs of conjugate singleparticle states (the usual time-reversed pairs of a closed shell), and in this limit the Pfaffian reduces to the determinant built from the same one-body orbitals, thus recovering the SJ form as a special case.

In contrast to these orbital-product expansions, and to both the SJ and HN ansätze, one can require only a single trainable pair orbital $\phi$ , so the number of variational parameters does not grow with the number of particles $A$ . Skewsymmetry is enforced at the level of the orbital itself by parameterizing $\phi$ through a neural network $\nu$ ,

$$
\phi \left(x _ {i}, x _ {j}\right) = \nu \left(x _ {i}, x _ {j}\right) - \nu \left(x _ {j}, x _ {i}\right), \tag {3.43}
$$

so that $\phi ( x _ { i } , x _ { j } ) = - \phi ( x _ { j } , x _ { i } )$ holds identically. In practice [54, 55], $\nu$ is implemented as an MLP acting on the concatenated features of the two nucleons, which allows the orbital to depend simultaneously on relative position and on spin–isospin quantum numbers, thereby capturing correlations beyond pure pairing.

For systems with an odd number of nucleons, the ansatz is extended by adding a single unpaired orbital $\psi$ , parameterized by a separate MLP. In this case, the Pfaffian is taken over an enlarged $( A + 1 ) \times ( A + 1 )$ skew-symmetric matrix:

$$
\Psi_ {P J} ^ {\mathrm {o d d}} (X) = e ^ {J (X)} \operatorname {p f} \left[ \begin{array}{c c} P (X) & \mathbf {u} (X) \\ - \mathbf {u} (X) ^ {T} & 0 \end{array} \right], \tag {3.44}
$$

where

$$
\mathbf {u} (X) = \left[ \psi \left(x _ {1}\right) \psi \left(x _ {2}\right) \dots \psi \left(x _ {A}\right) \right] ^ {T} \tag {3.45}
$$

collects the values of the unpaired orbital on all single-particle degrees of freedom. This construction preserves antisymmetry while allowing Pfaffian-based NQS to describe odd-mass nuclei or systems with a blocked quasiparticle.

Although the Pfaffian ansatz for odd $A$ introduces an additional, unpaired orbital relative to the even- $A$ case, the overall number of trainable parameters in both formulations remains independent of the particle number. Moreover, because the even- and odd- $A$ constructions share the same underlying pairing orbital, transfer-learning strategies can be straightforwardly employed between neighboring systems. This favorable scaling has enabled simulations of dilute, isospin-asymmetric neutron-star matter with up to $A = 4 2$ nucleons under periodic boundary conditions [55]. Owing

to this efficiency, the Pfaffian ansatz is emerging as a particularly effective tool for larger systems, while benchmark studies continue to compare its performance with the HN ansatz, which is known to provide a universal approximation to antisymmetric wave functions [128].

In neutron matter, pairing is an essential ingredient, whereas in finite nuclei it may or may not be dominant, depending on shell structure and interaction strength [142]. Nevertheless, the Pfaffian formulation remains attractive because (i) for an appropriate choice of pairing orbital it collapses to a single Slater determinant; (ii) the orbital depends simultaneously on spatial and spin–isospin coordinates, allowing it to capture independent-pair correlations beyond pure pairing; (iii) it yields a compact description of open-shell systems without resorting to linear combinations of many Slater determinants; and (iv) its cost scales favorably with system size, since only a single pairing orbital is required regardless of $A$ .

# 3.4.5. Backflow correlations

Backflow correlations encode how the state of a single particle is influenced by the coordinates of all the others, effectively redefining its coordinates according to the many-body configuration, $x _ { i } \mapsto g _ { i } ( x _ { i } ; \{ x _ { j } \} _ { j \neq i } )$ . This idea dates back to Ref. [143] and has since become a widely adopted strategy for enhancing the expressivity of antisymmetric NQS [44, 45, 144]. A key requirement is permutation equivariance: permuting the particles in the input must produce the same permutation in the output, $g _ { i } \mapsto g _ { j }$ if $x _ { i } \mapsto x _ { j }$ , so as to preserve the antisymmetry of the fermionic wave function.

A relatively simple backflow transformation has been recently incorporated into the HN framework and applied to compute properties of nuclei such as $^ { 2 0 }$ Ne in Ref. [52]. The equivariant backflow transformation reads

$$
g _ {i} = \left(x _ {i}, \sum_ {j} m \left(x _ {i}, x _ {j}\right)\right), \tag {3.46}
$$

with $m$ an MLP made of two fully-connected layers with 32 nodes each [52].

The calculations in Ref. [51] for $^ 4$ He, $_ 6$ Li, and $^ { 1 6 }$ O employ a multi-determinant SJ architecture with neural backflow, dubbed FeynmanNet. The backflow transformation generalizes the Fermionic Neural Network of Ref. [45] to encompass both continuous spatial and discrete spin–isospin degrees of freedom. As shown in Sec. 4.5, this architecture yields highly accurate ground-state energies for input Hamiltonians from pionless EFT at leading and next-to-leading order, which include a short-range tensor component.

Many nuclear-physics calculations based on NQS make use of transformations built from message-passing neural networks (MPNNs) to improve the flexibility and scalability of the variational ansatz. MPNN-based backflow was first integrated into the SJ ansatz to preprocess the input coordinates. In its first application to the homogeneous electron gas, this strategy enabled simulations with up to $N = 1 2 8$ electrons at extremely low densities [114]. It was later extended to ultracold Fermi gases [54], where strong pairing correlations are particularly challenging. Most recently, MPNNs have been used to compute properties of dilute neutron-star matter, substantially enhancing the expressivity of the PJ ansatz and allowing a first-principles description of cluster formation in the neutron-star crust [55].

MPNNs are a class of graph neural networks designed to model correlations in graph-structured data. In quantum systems of identical particles, this graph is fully connected, with each particle interacting with every other. Importantly, to satisfy the Pauli principle, MPNNs can process inputs in a permutation-equivariant manner. There are many possible ways to implement an MPNN, but the core idea is to iteratively update the information encoded on the nodes and edges of a graph. The input graph typically encodes single-particle features on the nodes and pairwise features on the edges. At each iteration, messages are passed along the edges based on these features, allowing each node to incorporate information

from its neighbors. As a result, the node and edge representations become increasingly enriched with nonlocal, correlated information from the entire system. The output is then another graph with the same connectivity but with node and edge features that encode many-body correlations in a permutation-equivariant way. These features can then be fed into other parts of the NQS in place of the original node and edge features.

Here, we outline the structure of the MPNN following Ref. [55] based on earlier developments in Refs. [54, 114], with modifications appropriate for finite nuclei. We take the input single-particle “visible” features as $\mathbf { v } _ { i } = \left[ \bar { \mathbf { r } } _ { i } , s _ { i } ^ { z } , t _ { i } ^ { z } \right]$ . Note that—unlike in periodic systems, where only the spin and isospin of particle $_ i$ are used as inputs—here the Cartesian coordinates of the nucleons are also included. To automatically remove spurious center-of-mass contributions from all observables [117], we define the intrinsic spatial coordinates as $\bar { \mathbf { r } } _ { i } = \mathbf { r } _ { i } - \mathbf { R } _ { \mathrm { C M } }$ , where $\mathbf { R } _ { \mathrm { C M } }$ denotes the center of mass of the nucleus. The “visible” pairwise features encode spatial as well as spin–isospin coordinates and are defined by

$$
\mathbf {v} _ {i j} = \left[ \mathbf {r} _ {i} - \mathbf {r} _ {j}, \left\| \mathbf {r} _ {i} - \mathbf {r} _ {j} \right\|, s _ {i} ^ {z}, s _ {j} ^ {z}, t _ {i} ^ {z}, t _ {j} ^ {z} \right].
$$

The initial hidden features for the nodes and the edges are obtained by concatenating the original and transformed single-particle and two-particle features, respectively, as

$$
\mathbf {h} _ {i} ^ {(0)} = \left[ \mathbf {v} _ {i}, f _ {A} (\mathbf {v} _ {i}) \right], \quad \mathbf {h} _ {i j} ^ {(0)} = \left[ \mathbf {v} _ {i j}, f _ {B} (\mathbf {v} _ {i j}) \right].
$$

Here, $f _ { A }$ and $f _ { B }$ are MLPs that preprocess the input coordinates and map them into a common latent space, ensuring that the dimensions of the hidden features $\mathbf { h } _ { i } ^ { ( t ) }$ and $\mathbf { h } _ { i j } ^ { ( t ) }$ remain independent of the iteration index $t$ .

The MPNN update is performed iteratively for $t = 1 , \ldots , T$ . At each step, information between the node and edge features is exchanged through the message

$$
\mathbf {m} _ {i j} ^ {(t)} = f _ {M} ^ {(t)} \left(\mathbf {h} _ {i} ^ {(t - 1)}, \mathbf {h} _ {i j} ^ {(t - 1)}, \mathbf {h} _ {j} ^ {(t - 1)}\right), \tag {3.47}
$$

where $f _ { M } ^ { ( t ) }$ is an MLP. For each particle $i$ , the relevant messages are collected and pooled to eliminate any ordering with respect to the other particles $j \neq i$ . As in Ref. [54], we use logsumexp pooling, a smooth alternative to max pooling,

$$
\mathbf {m} _ {i} ^ {(t)} = \log \left(\sum_ {j \neq i} \exp \Big (\mathbf {m} _ {i j} ^ {(t)} \Big)\right).
$$

The hidden node and edge features are then updated as

$$
\mathbf {h} _ {i} ^ {(t)} = \left[ \mathbf {v} _ {i}, f _ {F} ^ {(t)} \left(\mathbf {h} _ {i} ^ {(t - 1)}, \mathbf {m} _ {i} ^ {(t)}\right) \right],
$$

$$
\mathbf {h} _ {i j} ^ {(t)} = \left[ \mathbf {v} _ {i j}, f _ {G} ^ {(t)} \left(\mathbf {h} _ {i j} ^ {(t - 1)}, \mathbf {m} _ {i j} ^ {(t)}\right) \right].
$$

The functions $f _ { M } ^ { ( t ) }$ , $f _ { F } ^ { ( t ) }$ , and $f _ { G } ^ { ( t ) }$ are distinct MLPs whose output dimensions match those of $f _ { A }$ and $f _ { B }$ . Including concatenated skip connections to the visible features ensures that the signal from the raw input remains accessible even as the MPNN depth $T$ increases.

Finally, after the $T$ -th iteration, we aggregate the hidden node and edge features into single-particle and pairwise feature vectors:

$$
\mathbf {g} _ {i j} = \left[ \mathbf {h} _ {i} ^ {(T)}, \mathbf {h} _ {j} ^ {(T)}, \mathbf {h} _ {i j} ^ {(T)} \right],
$$

$$
\mathbf {g} _ {i} = \log \left(\sum_ {j \neq i} \exp \left(\mathbf {g} _ {i j}\right)\right).
$$

![](images/ab8a3bc3559ee263f5ee5d7f976c3774e57b2f208d7d45009d3f0965adbe29ad.jpg)  
Figure 3.4: Schematic representation of the message-passing neural network. Each of the $T$ total iterations of the network is represented by a yellow box. Dashed lines represent the concatenation operations, while solid lines represent the parameterized transformations (linear transformations and nonlinear feedforward neural networks). Messages, highlighted in pink, mediate the exchange of information between the one- and two-body streams, in blue.

By construction, $\mathbf { g } _ { i }$ and $\mathbf { g } _ { i j }$ define a permutation-equivariant many-body feature embedding of the original single-particle and pairwise degrees of freedom. Rather than representing a fixed coordinate transformation, the MPNN learns a nonlinear, nonlocal reparameterization of the input graph that can be used as a drop-in replacement for the original node and edge features in a wide class of NQS.

In recent works [54, 55], the pairwise features ${ \bf { g } } _ { i j }$ are used to parameterize the Pfaffian pairing orbital and the Jastrow factor, replacing the bare inputs $( x _ { i } , x _ { j } )$ with their correlated counterparts. However, this choice is not intrinsic to the construction: the same embedding can be coupled to SJ [114], HN [52], or other operator-based ansätze, and the singleparticle features $\mathbf { g } _ { i }$ may equally be used to define backflow-modified one-body orbitals. In this sense, the MPNN provides a general, architecture-agnostic mechanism for incorporating many-body correlations into neural wave functions.

# 4. Nuclear Physics Applications

# 4.1. The deuteron

While the first applications of NQS to many-body problems date to 2017–18 [43, 145, 146], the first application to a nuclear system arrived in 2020 with Ref. [47]. That work presented a proof-of-principle calculation of the deuteron, the only bound state of a neutron and a proton. The setup was deliberately minimal, allowing the authors to focus on the capabilities of the NQS framework rather than on details of the ansatz architecture.

Because nucleon–nucleon interactions are naturally formulated in momentum space [147], and many existing numerical routines operate in this representation, the initial application was carried out in momentum space. In this basis, the twobody problem factorizes into a center-of-mass component and a relative component, with the former being irrelevant for the bound-state problem. The relative component is characterized by the relative momentum $q$ between the neutron and the proton. An additional practical advantage of working in momentum space is that no derivatives associated with the kinetic energy operator are required. In this formulation, the bound-state wave function can be decomposed into partial waves of definite orbital angular momentum. The deuteron exhibits a known quadrupole deformation [147], implying that its wave function contains both a relative orbital angular momentum $L = 0$ component, denoted $| \Psi ^ { S } \rangle$ , and an $L = 2$ component, denoted $| \Psi ^ { D } \rangle$ .

With these nuclear properties in mind, a minimal ansatz for the deuteron wave function was chosen, as shown in Fig. 4.1. The ansatz consists of a simple MLP with one input (the relative momentum $q$ ) and two outputs (the two components $| \Psi ^ { S , D } \rangle$ ). The first layer included a set of weights $\mathcal { W } ^ { ( 1 ) }$ and biases $\mathbf { b }$ , whereas the second layer did not incorporate any bias. The network contained $N _ { \mathrm { h i d } }$ hidden nodes and was assumed to be fully connected, as indicated in Fig. 4.1. The wave-function ansatz has the form

$$
\psi_ {\mathrm {A N N}} ^ {L} (q) = \sum_ {i = 1} ^ {N _ {\mathrm {h i d}}} \mathcal {W} _ {i, L} ^ {(2)} \sigma \left(\mathcal {W} _ {i} ^ {(1)} q + b _ {i}\right), \tag {4.1}
$$

where $\sigma ( x )$ denotes the chosen activation function. Since the deuteron wave function is a smooth, continuous function of

![](images/116cd740a9049280abeac26d66e43a741d99ace75f8e2f3da63587335142736d.jpg)  
Figure 4.1: Feed-forward neural network architecture used in Ref. [47]. The input is a single value of relative momentum, $q$ , and the wave functions are modeled in terms of a minimal single-layer network with $N _ { \mathrm { h i d } }$ nodes. The ansatz has two outputs, one for the $S$ and one for the $_ { D }$ state.

![](images/c9fc7b0d0125f5fab1b2f82f75acc12878b05aee30e0cfc45b491b637e5aa473.jpg)  
Figure 4.2: Deuteron binding energy as a function of iteration number for a network with $N _ { \mathrm { h i d } } = 1 0$ nodes and a softplus activation function [47].

$q$ , it is natural to employ continuous activation functions in this case. The initial exploration of Ref. [47] considered both sigmoid and softplus functions.

The one-dimensional nature of the problem in relative momentum coordinates allows the total energy to be evaluated straightforwardly by quadrature. For example, the kinetic energy expectation value is approximated as

$$
\langle K \rangle = \sum_ {L} \int_ {0} ^ {\infty} d q q ^ {2} \frac {\hbar^ {2} q ^ {2}}{\mu} | \Psi^ {L} (q) | ^ {2} \approx \sum_ {L} \sum_ {i = 1} ^ {N _ {q}} \omega_ {i} q _ {i} ^ {2} \frac {\hbar^ {2} q _ {i} ^ {2}}{\mu} | \Psi^ {L} (q _ {i}) | ^ {2}, \tag {4.2}
$$

where $\mu = m _ { n } m _ { p } / ( m _ { n } + m _ { p } )$ is the reduced mass of the np system. A set of $N _ { q } ~ = ~ 6 4$ Gauss–Legendre quadrature points, tangentially transformed to extend up to $k _ { \mathrm { m a x } } = 5 0 0 ~ \mathrm { f m ^ { - 1 } }$ , was sufficient to obtain accurate results. The same quadrature scheme can be used to evaluate the potential energy. This initial study employed the N3LO Entem–Machleidt interaction [148], although in principle any other interaction could be used. The quadrature-discretized Hamiltonian can of course be diagonalized directly, providing an exact benchmark on the same footing as the NQS simulation.

With this quadrature set up, the calculation of the energy is rather straightforward. The original set-up employed a pre-training step to pre-optimize the shape of the ansatz in Eq. (4.1) to physically sound values. This step is not necessary, but helps accelerate the optimization procedure [149]. After the pre-training, the energy minimization was performed over $2 5 0 , 0 0 0$ steps employing RMSprop [150] as the optimizer of choice.

A typical minimization curve for the case with $N _ { \mathrm { h i d } } = 1 0$ is shown in Fig. 4.2. For this very simple architecture, the energy converged to 1% within a few tens of thousands of iterations. After around 150, 000 iterations, the energy is very close to the minimum, but oscillates above the actual benchmark minimum within $3 - 4 ~ \mathrm { e V }$ of the exact result. This minimal set-up already provides an excellent reproduction of the exact wave function and physical properties of the deuteron [47].

To address systematic errors in the NQS method as opposed to specific minimisations, the analysis of Refs. [47] and [149] focused on the characterization of uncertainties. Simulations of the deuteron were run for different numbers of hidden nodes, $N _ { \mathrm { h i d } }$ . Results of these numerical experiments for the simple architecture of Eq. (4.1) are presented in Fig. 4.3 [149]. Two different sets of uncertainties were identified to characterize the NQS minimization generally (as opposed to a minimization-by-minimization basis). First, different initializations of the network lead to different final results after $2 5 0 , 0 0 0$ iterations. This uncertainty can be assessed by running the minimization process 20 times and computing the associated standard deviation. This out-of-sample uncertainty is represented in dark bands in the top panel of Fig. 4.3. We stress that this uncertainty amounts to only a fraction of a keV in energy and that it is rather

![](images/4df1d80b2c6b017d21f449745d5b0424a6fc50a1dca9af584942d8aa47828389.jpg)

![](images/c16baf6f0b835d7b0ec4d65f5b22919ec047c9efa05cd60410660ae6580caec5.jpg)  
Figure 4.3: Binding energy of the deuteron (left panel) and fidelity $\mathcal { F }$ (right panel) as a function of the number of hidden layer nodes, $N _ { \mathrm { h i d } }$ from Ref. [149]. See main text for an explanation of the error bands. Horizontal (dashed) lines show the benchmark result.

independent of the number of nodes. Moreover, the fidelity, $F$ , between the ansatz at the end of minimization and the corresponding exact benchmark is given in the bottom panel of Fig. 4.3. We represent the fidelities of both the $S -$ and the $D -$ states. Again, out-of-sample uncertainties, represented by dark bands, are very small for fidelities [47].

As illustrated in Fig. 4.2, even at the end of a full minimization, the results still show some residual oscillations. These oscillations are typically within a few keV of the total energy and are hence larger than the out-of-sample uncertainty. In this context, Ref. [149] looked into these post-training oscillation amplitudes as an additional source of uncertainty that is associated not so much to minimization instances, but rather to the minimization process itself. To characterize this uncertainty, the model was minimized initially and then evolved for 300 final iterations. The number of these post-evolution epochs is small, to guarantee that mean energy values do not improve, but also large enough to observe periodicity in the oscillations. Upper and lower values of these oscillations were recorded for 20 different minimization instances, and their average values are shown as the light bands in Fig. 4.3.

These results clearly indicate that oscillation errors at the end of the minimization dominate over any out-of-sample uncertainties. Moreover, these uncertainties show a decreasing trend with $N _ { \mathrm { h i d } }$ . Whereas for $N _ { \mathrm { h i d } } = 2$ the post-evolution uncertainty in the energy is of the order of 2.5 keV, at $N _ { \mathrm { h i d } } = 1 0 0$ this falls just below 1 keV. A similar decrease in postevolution uncertainty is observed in the fidelities of the bottom panel. In this case, the fidelity of the $D$ −state presents a much larger uncertainty.

The high fidelity shown in Fig. 4.3 indicates a strong level of agreement between the exact wave function and the NQS ansatz. This agreement is illustrated more explicitly in Fig. 4.4, which displays the $S$ - (left panel) and $D$ -wave (right panel) components as functions of momentum for minimizations with $N _ { \mathrm { h i d } } = 1 0$ [47]. The solid (red) lines correspond to the benchmark exact solution, while the dashed (blue) and dotted (green) lines show the results of averaging 50 independent minimizations using sigmoid and softplus activation functions, respectively.

The agreement is excellent across nearly all momenta, with small deviations appearing near the origin, $q \approx 0 ~ \mathrm { f m ^ { - 1 } }$ . Because the wave functions are spherically symmetric, the energy functional includes a $q ^ { 2 }$ factor in the integration measure. As a result, the region near $q = 0$ contributes very little to the cost function, leaving the wave function weakly constrained there. A simple network with $N _ { \mathrm { h i d } } = 1 0$ has limited flexibility to adjust its behavior in this region. As $N _ { \mathrm { h i d } }$ increases,

![](images/d40ce36a65bf594ec58d5722a4baa2cda4b07a91969d6ed10f02a43b9932b3d1.jpg)

![](images/a55345a71f8ed4baa25d0839b4195d0eb59c69d9388f499b170cec13995f6c7e.jpg)  
Figure 4.4: Left (right) panel: the $S$ $D$ ) state wave function as a function of momentum, taken from Ref. [47]. The benchmark exact solutions (solid lines) are compared to the feed-forward ansatz with $N _ { \mathrm { h i d } } = 1 0$ using sigmoid (dashed) and softplus (dotted) activation functions. The shaded bands indicate the standard deviation over 50 different initialization runs.

however, additional flexibility tends to manifest primarily near the origin, where the weak energetic penalty may allow for large variations in shape, including non-physical behaviors [47].

While our discussion has focused on the simple architecture of Eq. (4.1), Ref. [149] presents an extensive analysis of more elaborate architectural extensions. These include separate, independent branches for the $S$ and $D$ channels, as well as deeper, multi-layer networks. Adopting these more complex architectures leads to two main consequences. First, the fraction of models that converge to an acceptable energy range, $E \in \left( { - 2 . 2 2 0 , - 2 . 2 2 7 } \right) \mathrm { M e V }$ , is significantly reduced. Whereas the simple one-layer MLP achieves a $1 0 0 \%$ success rate for nearly all values of $N _ { \mathrm { h i d } }$ , the acceptance rates of more complex architectures depend strongly on $N _ { \mathrm { h i d } }$ and range from $1 \%$ to 90% [149]. Second, more elaborate architectures exhibit substantially larger post-training uncertainties, with a pronounced dependence on $N _ { \mathrm { h i d } }$ . In some cases, indications of overfitting are also observed. Although understanding the internal behavior of NQS models is not easy, the systematic error analysis and architectural comparisons performed for the deuteron provide a useful starting point for probing these issues in nuclear systems.

# 4.2. Atomic nuclei

# 4.2.1. Nuclei with up to A=6 nucleons

The first application of VMC methods based on NQS to the nuclear many-body problem [48] computed the ground-state energies and single-particle densities of $^ 2 \mathrm { H }$ , $^ 3 \mathrm { H }$ , and $^ 4$ He. It is worth noting that the LO pionless-EFT Hamiltonian used in that work differs slightly from the one discussed in Sec. 2. Specifically, the NN interaction is

$$
v _ {\mathrm {L O}} ^ {\mathrm {C I}} \left(r _ {i j}\right) = \left(C _ {1} + C _ {2} \sigma_ {i j}\right) e ^ {- r _ {i j} ^ {2} \Lambda^ {2} / 4}, \tag {4.3}
$$

where, following Ref. [151], the low-energy constants $C _ { 1 }$ and $C _ { 2 }$ are fitted to the deuteron binding energy and the neutron–neutron scattering length. The 3N force is taken as

$$
V _ {i j k} = D _ {0} \sum_ {\text {c y c}} e ^ {- \left(r _ {i k} ^ {2} + r _ {i j} ^ {2}\right) \Lambda^ {2} / 4}, \tag {4.4}
$$

with $D _ { 0 }$ fixed by the $^ 3 \mathrm { H }$ ground-state energy.

Reference [48] employed the SJ wave-function ansatz of Eq. (3.20), together with the real-valued Jastrow factor of Eq. (3.24). In this construction, the Deep Sets architecture (see Section 3.3) uses the single-particle sum aggregation of Eq. (3.25). Table 4.1, adapted from Ref. [48], reports the ground-state energies of $^ 2 \mathrm { H }$ , $^ 3 \mathrm { H }$ , and $^ { 4 } \mathrm { H e }$ . The SJ results are benchmarked against VMC calculations based on spline parameterizations of the two- and three-body spin–isospin–independent Jastrow functions [152], as well as against virtually exact GFMC results. All three methods yield statistically consistent energies for $^ 2 \mathrm { H }$ , demonstrating that the SJ ansatz is flexible enough to accurately represent the deuteron ground state. This agrees with the findings of Ref. [47], discussed in Section 4.1. Since the LO pionless-EFT Hamiltonian lacks tensor and spin–orbit components, the SJ ansatz without backflow is in fact exact for this system. For $^ 3 \mathrm { H }$ , the neural SJ ansatz provides an improvement of about 0.5 MeV over conventional VMC for both $\Lambda = 4 ~ \mathrm { f m ^ { - 1 } }$ and $6 ~ \mathrm { f m ^ { - 1 } }$ . The GFMC energies are roughly 0.1 MeV more bound than the SJ ones. As noted in Ref. [48], this residual difference originates from spin-dependent correlations that are automatically generated in GFMC imaginary-time evolution but are only partially encoded in the Jastrow factor of Eq. (3.24). These correlations modify the nodal structure of the wave function, which the SJ architecture cannot recover without incorporating backflow transformations. A similar trend is observed for $^ { 4 } \mathrm { H e }$ : the SJ wave functions outperform the conventional VMC ones, improving the energies by about 0.8 MeV and 1.0 MeV for $\Lambda = 4 ~ \mathrm { f m ^ { - 1 } }$ and $6 ~ \mathrm { f m ^ { - 1 } }$ , respectively. The remaining discrepancies with GFMC again reflect missing spin–isospin–dependent correlations in the SJ ansatz.

To further elucidate the quality of the ANN wave function, we consider the point-nucleon density

$$
\rho_ {N} (r) = \frac {1}{4 \pi r ^ {2}} \left\langle \Psi_ {V} \right| \sum_ {i} \delta (r - | \mathbf {r} _ {i} ^ {\mathrm {i n t}} |) | \Psi_ {V} \rangle , \tag {4.5}
$$

which is of interest in a variety of experimental settings [153, 154]. Fig. 4.5 displays $\rho _ { N } ( r )$ of $^ { 4 } \mathrm { H e }$ as obtained from the SJ ansatz compared with GFMC calculations, both using as input the LO pionless-EFT Hamiltonian with $\Lambda = 4 ~ \mathrm { f m ^ { - 1 } }$ . There is an excellent agreement between the two methods, which further corroborates the representative power of the SJ ansatz for the wave functions of $A \leq 4$ nuclei. The SJ and GFMC densities overlap both at short distances and in the slowly-decaying asymptotic exponential tails, highlighted in the insets of Fig. 4.5. As already noted in Ref. [48], the NQS learns how to compensate for the original Gaussian confining function and reproduce the correct exponential falls off of the nuclear wave function, which is notoriously delicate to obtain within nuclear methods that rely on harmonic-oscillator basis expansions [16, 155].

Ref. [92] extended the SJ approach to the $^ 6$ Li and $^ 6$ He nuclei, employing the model “o” Hamiltonian of Eqs. (2.2)-(2.6)

Table 4.1: (From Ref. [48] with permission from the Authors). Ground-state energies in MeV of the $^ 2 \mathrm { H }$ , $^ 3 \mathrm { H }$ , and $^ 4 \mathrm { H e }$ for the LO pionless-EFT Hamiltonian for $\Lambda = 4 ~ \mathrm { f m ^ { - 1 } }$ and $\Lambda = 6 ~ \mathrm { f m ^ { - 1 } }$ . Numbers in parentheses indicate the statistical errors on the last digit.   

<table><tr><td></td><td>Λ</td><td>SJ</td><td>Spline</td><td>GFMC</td></tr><tr><td rowspan="2">2H</td><td>4 fm-1</td><td>-2.224(1)</td><td>-2.223(1)</td><td>-2.224(1)</td></tr><tr><td>6 fm-1</td><td>-2.224(4)</td><td>-2.220(1)</td><td>-2.225(1)</td></tr><tr><td rowspan="2">3H</td><td>4 fm-1</td><td>-8.26(1)</td><td>-7.80(1)</td><td>-8.38(2)</td></tr><tr><td>6 fm-1</td><td>-8.27(1)</td><td>-7.74(1)</td><td>-8.38(2)</td></tr><tr><td rowspan="2">4He</td><td>4 fm-1</td><td>-23.30(2)</td><td>-22.54(1)</td><td>-23.62(3)</td></tr><tr><td>6 fm-1</td><td>-24.47(3)</td><td>-23.44(2)</td><td>-25.06(3)</td></tr></table>

![](images/5296720d2d03581be3cb7b1e2d1a36cdc24adcbcf8d3f08c441116ed32455199.jpg)  
Figure 4.5: (From Ref. [48], with permission from the Authors) Point-nucleon densities of 4He (lower panel) for the LO pionless-EFT Hamiltonian with $\Lambda = 4 ~ \mathrm { f m ^ { - 1 } }$ . The solid points and the shaded area represent the SJ and GFMC results, respectively.

with the three-nucleon regulator set to $R _ { 3 } = 1 . 0$ fm. A key technical advance relative to Ref. [48] is the use of the linear combination of Slater determinants of Eq. (3.21) to represent the mean-field component of the open-shell systems $_ 6$ Li and $_ 6$ He. In addition, pairwise inputs were incorporated into the Deep Sets architecture used for the Jastrow factor, as in Eq. (3.26). In that work, the SJ energies and charge radii were benchmarked against the highly accurate hyperspherical harmonics (HH) method [156].

The binding energies and charge radii of $^ 2 \mathrm { H }$ , $^ 3 \mathrm { H }$ , $^ { 3 } \mathrm { H e }$ $^ { 3 }$ , $^ { 4 } \mathrm { H e }$ , $^ { 6 } \mathrm { H e }$ , and $_ 6$ Li obtained with the VMC method based on the SJ ansatz and with the HH method are listed in Table 4.2. For nuclei with $A \geq 3$ , the table separately shows the results computed using the $N N$ interaction alone and those obtained with the full model “o” Hamiltonian, which also includes the $3 N$ force.

The expectation value of the charge radius is derived from the point-proton radius using the relation:

$$
\left\langle r _ {\mathrm {c h}} ^ {2} \right\rangle = \left\langle r _ {\mathrm {p t}} ^ {2} \right\rangle + \left\langle R _ {p} ^ {2} \right\rangle + \frac {A - Z}{Z} \left\langle R _ {n} ^ {2} \right\rangle + \frac {3}{4 m _ {p} ^ {2}}, \tag {4.6}
$$

where $\langle r _ { \mathrm { p t } } ^ { 2 } \rangle$ is the calculated point-proton radius, $\langle R _ { p } ^ { 2 } \rangle = 0 . 7 7 0 ( 9 ) , \mathrm { f m } ^ { 2 }$ is the proton mean-square charge radius, $\left. R _ { n } ^ { 2 } \right. =$ $- 0 . 1 1 6 ( 2 ) , \mathrm { f m } ^ { 2 }$ is the neutron mean-square charge radius. Here, consistent with Ref. [92], we list the 2012 values for these quantities [157]. Finally, $( 3 ) / ( 4 m _ { p } ^ { 2 } ) \approx 0 . 0 3 3 , \mathrm { f m } ^ { 2 }$ is the Darwin–Foldy correction [158]. The point-proton radius can be computed as the ground-state expectation value

$$
\left\langle r _ {\mathrm {p t}} ^ {2} \right\rangle = \frac {1}{Z} \left\langle \Psi \right| \sum_ {i} P _ {p} \left| \mathbf {r} _ {i} - \mathbf {R} _ {\mathrm {c m}} \right| ^ {2} | \Psi \rangle , \tag {4.7}
$$

where $Z$ is the number of protons and $P _ { p } = \big ( 1 + \tau _ { z _ { i } } \big ) / 2$ projects onto proton states.

The SJ ansatz reproduces the HH binding energy of $^ 2 \mathrm { H }$ , with both calculations yielding values slightly more bound than experiment owing to the missing charge-dependent and charge-symmetry-breaking terms—aside from the Coulomb interaction—in the $N N$ potential. The charge radii obtained with the VMC–SJ and HH methods are compatible within uncertainties and only marginally smaller than the experimental value.

Moving to the $A = 3$ systems, VMC–SJ underbinds $^ 3 \mathrm { H }$ and 3He by about 0.25 MeV relative to HH for both the $N N$ and $N N + 3 N$ Hamiltonians. As discussed in Ref. [48], these small differences stem from the inability of the Jastrow

Table 4.2: Ground-state energies and charge radii for selected $A \leq 6$ nuclei obtained from VMC calculations based on the SJ ansatz and HH methods using as input model “o” Hamiltonian of Ref. [61] with and without the $_ { 3 N }$ force. We report also the experimental binding-energies from Ref. [159] and the charge radius taken from Refs. [160–165].   

<table><tr><td rowspan="2">Nucleus</td><td rowspan="2">Potential</td><td colspan="2">SJ</td><td colspan="2">HH</td><td colspan="2">Exp.</td></tr><tr><td>E (MeV)</td><td>rch (fm)</td><td>E (MeV)</td><td>rch (fm)</td><td>E (MeV)</td><td>rch (fm)</td></tr><tr><td>2H</td><td>NN</td><td>-2.242(1)</td><td>2.120(5)</td><td>-2.242</td><td>2.110(2)</td><td>-2.225</td><td>2.128</td></tr><tr><td rowspan="2">3H</td><td>NN</td><td>-9.511(1)</td><td>1.658(4)</td><td>-9.744</td><td>1.656(4)</td><td rowspan="2">-8.475</td><td rowspan="2">1.755(86)</td></tr><tr><td>3N</td><td>-8.232(1)</td><td>1.750(3)</td><td>-8.475</td><td>1.747(6)</td></tr><tr><td rowspan="2">3He</td><td>NN</td><td>-8.800(1)</td><td>1.845(3)</td><td>-9.035</td><td>1.848(6)</td><td rowspan="2">-7.718</td><td rowspan="2">1.964(1)</td></tr><tr><td>3N</td><td>-7.564(1)</td><td>1.961(3)</td><td>-7.811</td><td>1.969(8)</td></tr><tr><td rowspan="2">4He</td><td>NN</td><td>-36.841(1)</td><td>1.484(3)</td><td>-37.06</td><td>1.485(4)</td><td rowspan="2">-28.30</td><td rowspan="2">1.678</td></tr><tr><td>3N</td><td>-27.903(1)</td><td>1.643(2)</td><td>-28.17</td><td>1.646(4)</td></tr><tr><td rowspan="2">6He</td><td>NN</td><td>-37.25(4)</td><td>1.895(2)</td><td>-37.96(8)</td><td>1.71(1)</td><td rowspan="2">-29.27</td><td rowspan="2">2.05(1)</td></tr><tr><td>3N</td><td>-27.46(2)</td><td>&gt;4.89(1)</td><td>-27.41(8)</td><td>&gt;2.73</td></tr><tr><td rowspan="2">6Li</td><td>NN</td><td>-42.04(1)</td><td>2.248(3)</td><td>-42.51(5)</td><td>2.09(2)</td><td rowspan="2">-31.99</td><td rowspan="2">2.54(3)</td></tr><tr><td>3N</td><td>-30.82(3)</td><td>3.049(2)</td><td>-31.00(8)</td><td>&gt;2.74</td></tr></table>

correlator to compensate for zeros in the mean-field component $\langle R S | \Phi \rangle$ . Despite this limitation, the VMC–SJ and HH charge radii remain very similar and, once the $3 N$ force is included, agree well with experiment. It is also worth noting that the HH binding energy of $^ 3 \mathrm { H }$ matches the experimental value by construction, whereas the $^ { 3 }$ He energy differs from experiment by about 0.1 MeV—a discrepancy likely explained by the neutron–proton mass difference and by the missing charge-dependent and charge-symmetry-breaking components of the $N N$ interaction.

A similar pattern is observed in $^ { 4 } \mathrm { H e }$ : the VMC–ANN ground-state energy is approximately 0.2 MeV above the HH result, independent of whether the $3 N$ force is included. The repulsive character of the $3 N$ interaction is essential for improving agreement with experiment for both the binding energy and the charge radius. Including the $3 N$ force pushes nucleons to larger distances from the center of mass, thereby increasing the charge radius.

The $A = 6$ nuclei provide a more stringent test. With the $N N$ interaction alone, the SJ ansatz yields wave functions that are stable against breakup—6He into $^ { 4 } \mathrm { H e }$ plus two neutrons, and $_ 6$ Li into $^ { 4 } \mathrm { H e }$ $^ 4$ plus a deuteron. This is a nontrivial result, as conventional VMC calculations with standard two- and three-body Jastrow correlations often fail to place $^ 6$ Li below the $^ 4 \mathrm { H e } + \mathrm { d }$ threshold. In this $N N$ -only case, the SJ energies are about 0.5 MeV less bound than the HH results, corresponding to a per-nucleon difference comparable to that observed for the $A = 3$ nuclei. The SJ charge radii of $^ { 6 } \mathrm { H e }$ and $^ 6$ Li exceed the HH values, although they remain below the experimental ones. Part of this discrepancy is attributable to the slow convergence of HH calculations for $A = 6$ systems [116]: the limited hyperradial truncation tends to underestimate the radii and prevents a reliable extrapolation. As in lighter systems, the inclusion of the $3 N$ force significantly increases the charge radii, in some cases pushing them above experimental values. With the $3 N$ interaction, $_ 6$ Li becomes only marginally bound against breakup into $\mathrm { ^ 4 H e } + \mathrm { d }$ , while $_ 6$ He becomes unbound with respect to $^ { 4 } \mathrm { H e }$ . Its wave function therefore extends to increasingly large distances from the center of mass, producing a very large charge

radius. This behavior mirrors that observed in Ref. [152] for the unbound $^ { 1 6 }$ O system and is likely to be corrected once the -wave contributions of the $N N$ potential are included [62]. $p$

# 4.2.2. Relativistic effects

Within the standard quantum many-body paradigm, discussed in Section 2, nuclei are treated as systems of point-like nucleons interacting through instantaneous potentials. While this description successfully accounts for a broad range of nuclear properties, it is, strictly speaking, incompatible with causality and can lead to unphysical predictions — such as superluminal sound speeds in dense matter [73, 166]. Relativistic extensions of this framework have therefore been explored for decades [167], starting from analyses of nuclear matter [168] and few-body systems [169] to more recent Quantum Monte Carlo studies employing Poincarè-invariant Hamiltonians constructed from phenomenological NN and 3N forces [170]. In this approach, relativity is incorporated by adopting relativistic kinetic energies and by supplementing two- and three-body potentials with the corresponding Lorentz–boost corrections, which encode the dependence of the interaction on the total momentum of the nucleon pair. Calculations of $A = 3$ and $A = 4$ nuclei have shown that these boost corrections produce repulsive contributions that represent a substantial fraction of the repulsion usually attributed to irreducible three-nucleon forces.

Building on this framework, the authors of Ref. [49] derive, for the first time, a microscopic relativistic Hamiltonian at leading order in covariant pionless EFT that contains consistent relativistic and $3 N$ potentials, and solve nuclei with $A \leq 4$ using a VMC method based on a SJ ansatz. More specifically, they obtain a relativistically corrected expression of the LO pionless-EFT $N N$ interaction of Eq. (4.3),

$$
v _ {\mathrm {L O / R E L}} ^ {\mathrm {C I}} \left(r _ {i j}\right) = - \sum_ {i <   j} ^ {A} \left(C _ {1} + C _ {2} \sigma_ {i j}\right) \left[ 1 + V _ {b} \left(\mathbf {r} _ {i j}\right) + V _ {t} \left(\mathbf {r} _ {i j}\right) \right] e ^ {- \frac {\Lambda^ {2}}{4} r _ {i j} ^ {2}}. \tag {4.8}
$$

The boost and transfer interactions in coordinate space read

$$
V _ {b} \left(\mathbf {r} _ {i j}\right) = - \frac {\hat {\mathbf {P}} _ {i j} ^ {2}}{8 m _ {N} ^ {2}} - \frac {\Lambda^ {2}}{1 6 m _ {N} ^ {2}} \left(\hat {\mathbf {P}} _ {i j} \cdot \mathbf {r} _ {i j}\right) ^ {2}, \tag {4.9}
$$

$$
V _ {t} (\mathbf {r} _ {i j}) = - \frac {\Lambda^ {2}}{4 m _ {N} ^ {2}} \left[ 3 - \frac {\Lambda^ {2}}{2} r _ {i j} ^ {2} + 2 i \mathbf {r} _ {i j} \cdot \hat {\mathbf {p}} _ {i j} + 4 \frac {\hat {\mathbf {p}} _ {i j} ^ {2}}{\Lambda^ {2}} \right], \tag {4.10}
$$

where the total and relative momentum operators of the $_ i$ th and $j$ th nucleons are

$$
\hat {\mathbf {P}} _ {i j} = - i (\nabla_ {i} + \nabla_ {j}), \quad \hat {\mathbf {p}} _ {i j} = - \frac {i}{2} (\nabla_ {i} - \nabla_ {j}). \tag {4.11}
$$

Corrections to the kinetic energy are also included, while those to the $3 N$ force are neglected in that work.

In Ref. [49], the nuclear Schrödinger equation for the above relativistically corrected $N N$ interaction is solved using a VMC method based on an SJ ansatz that respects rotational symmetry. As discussed in Section 3, spin–isospin dependent correlations are omitted, though their impact is expected to be relatively small.

As noted in Section 2, the renormalization behaviour of few-nucleon systems provides a clear illustration of the role of relativity in pionless EFT. In the nonrelativistic formulation, calculations of $^ 3 \mathrm { H }$ and $^ 4$ He with only two-nucleon interactions exhibit the well-known Thomas collapse: as the cutoff is increased, the ground-state energies diverge, reflecting the lack of renormalizability of the leading-order theory. The standard remedy is to promote a repulsive three-nucleon force to leading order in order to stabilize the spectrum.

As shown in Fig. 4.6, taken from Ref. [49], in the relativistic framework the situation changes qualitatively. When the $N N$ potential includes the relativistic boost and transfer terms, the few-body energies converge with increasing cutoff,

![](images/b6873be6c0834c08a38481adb41a633b4b6d455a71fde6e19d7867b065f67d9f.jpg)  
transla- Fig. 1. The ground-state energies of 3H (a) and 4He (b)Figure 4.6: (From Ref. [49] with permission from the Authors) Ground-state energies of $^ 3 \mathrm { H }$ tained with the non- (panel a) and 4He (panel b) obtained with the ich leads relativistic LO Hamiltonian and the relativistic ones without and with “transfer”nonrelativistic LO Hamiltonian and the relativistic ones without and with “transfer” interactions, as functions of the cutoff $\Lambda$ .

indicating that relativistic dynamics alone can remove the Thomas collapse without introducing a leading-order three-1 & 2     nucleon interaction. This stabilizing mechanism is analogous to that observed in relativistic treatments of three-boson systems. The boost term generates effective short-range repulsion similar in character to a three-body force, while the ns to the the transfer interaction. As the relativistic kinetic energy is gener-transfer interaction contains a short-range repulsive core whose strength grows with the cutoff, preventing the nucleons ar to the ally smaller than the nonrfrom approaching arbitrarily close at large cutoffs.

interaction to the same 2H ground-state eneReproducing the experimental binding energies nevertheless requires a $3 N$ y leads to a less at-interaction. In this relativistic framework, , includ- tractive N N interaction. Hthe interplay between relativistic corrections and the $3 N$ ever, the same fit with the transferforce leads to a significant suppression of three-body contributions interaction leads to a more attractive to the binding energy, largely independent of the strength of the $3 N$ coupling strength as theinteraction. These findings, obtained using VMC calculations based on SJ wave functions, provide the first unified and internally consistent treatment of relativistic confinedynamics and many-body forces in light nuclei, and open new avenues for improving ab initio calculations through a r2 with nuclei. In Fig. 1, the grounmore complete understanding of relativistic effects.

# nd-state g4.2.3. Reaching $^ { 1 6 } \mathbf { O }$ nd-state energies of 3H and 4He gi with systematically improvable ansätze

→ ∞     As discussed above, the SJ ansatz is not universal, since the Jastrow factor cannot remove the nodes generated by the mean-field component of the wave function. To address this limitation, the authors of Ref. [50] generalized the hiddenate γ in the standard nonrelativistic formulations, is avoided by promotingfermion family of NQS introduced in Ref. [128] to encompass both continuous and discrete degrees of freedom—see Sec. 3 ve a sta- a repulsive 3N interaction to LO [56]. In contrast, the relativisticfor a detailed discussion of the HN architecture. Using this framework, they solved the nuclear many-body Schrödinger proposed results converge as the cutoff increases, so the “Thomas collapse”equation in a systematically improvable manner. In particular, they showed that augmenting the original Hilbert space use it re- problem can be overcome by taking into account relativistic effectswith HNs substantially enhances the expressivity of the neural-network ansatz compared to the SJ wave function.

instead of introducing 3N interactions. Note that the relativistic ef-The work in Ref. [50] also demonstrated that explicitly encoding parity and time-reversal symmetries in the wave function, as in Eqs. (3.36) and (3.37), significantly accelerates the training. In addition, the convergence of the SR algorithm is substantially improved by introducing the RMSProp-inspired regularization of Eq. (3.11). Figure 4.7, taken

![](images/fad40e50c08a661e67d0e79ad23667e48cb5d1a5906772ceee015b69162b1413.jpg)  
Figure 4.7: Convergence of the SR algorithm for $^ 3 \mathrm { H }$ with the original (blue solid circles) and RMSProp-like (orange solid circles) diagonal shifts. The SJ and the HH energies of Ref. [92] are displayed by the purple dashed and solid green lines, respectively.

from Ref. [50], shows the convergence of the ground-state energy of $^ 3 \mathrm { H }$ obtained with $A _ { h } \ = \ 3$ HNs and the positiveparity ansatz of Eq. (3.36). The orange solid circles, corresponding to energies obtained using the RMSProp-regularized SR scheme, are systematically closer to the numerically exact hyperspherical-harmonics result of Ref. [116] than those obtained with the original SR algorithm, shown by solid blue circles. Moreover, the reduced scatter of the SR–RMSProp estimates compared to the SR results indicates improved stability of the optimization. Most notably, regardless of the specific regularization employed, both SR and SR–RMSProp yield energies that are appreciably lower than the SJ value reported in Ref. [92].

Reference [50] significantly extended the applicability of variational Monte Carlo calculations based on neural-network quantum states to nuclei as large as $^ { 1 6 }$ O, whereas earlier applications [48, 92] were limited to systems with $A \leq 6$ . The ground-state energy of $^ { 1 6 }$ O obtained with the HN ansatz was compared with results from the AFDMC method. In particular, comparisons were carried out both with variational energies obtained using the linearized ansatz of Eq. (2.20) and with full diffusion Monte Carlo results that include imaginary-time projection.

Figure 4.8 displays the ground-state energy of $^ { 1 6 }$ O as a function of the number of HNs $A _ { h }$ for the parity- and time-reversal-conserving ansatz of Eq. (3.37). For reference, the VMC energy obtained with the correlation operator of Eq. (2.20) is indicated by the dashed green line, with the shaded band representing the corresponding Monte Carlo statistical uncertainty. The solid horizontal line and the associated shaded region denote the constrained-path AFDMC energy and its statistical uncertainty reported in Ref. [61]. Already for $A _ { h } = 2$ , the HN wave function reproduces the VMC result. Upon further increasing $A _ { h }$ , the variational energy is progressively lowered and becomes consistent with the AFDMC value within uncertainties, demonstrating the accuracy of the HN ansatz for $p$ -shell nuclei.

A comparable level of accuracy has been achieved in Ref. [51] by augmenting the SJ ansatz with a backflow transformation referred to as FeynmanNet. In that work, the authors show that FeynmanNet yields very accurate ground-state energies and wave functions for 4He and $_ 6$ Li, and extends to systems as large as $^ { 1 6 }$ O, using leading-order and next-toleading-order Hamiltonians of pionless effective field theory. Notably, the latter include tensor components, which render the ground-state wave functions complex valued. More specifically, FeynmanNet uses a linear combination of Slater deter-

![](images/63eede7a9520f18088283b2027ca2ec04480fc6eed90e9dec80a38840cb070d3.jpg)  
Figure 4.8: Ground-state energy of $^ { 1 6 } \mathrm { O }$ as a function of the number of hidden nucleons $A _ { h }$ (solid blue points). The VMC and AFDMC energies—the latter taken from Ref. [61]—are shown by the dashed green and solid orange lines, respectively. The shaded areas represent the corresponding Monte Carlo statistical uncertainties.

minants together with a backflow transformation constructed from expressive deep neural networks that act on both the continuous spatial coordinates and the discrete spin–isospin degrees of freedom of the nucleons. To capture many-body correlations induced by tensor and spin–orbit interactions, the networks are designed to represent complex-valued nuclear wave functions. In addition, key features of low-energy nuclear structure, such as the major shell structure and relevant point symmetries, are explicitly encoded in the architecture. As a result, the FeynmanNet ansatz achieves high accuracy while remaining robust and efficient during the training process.

Figure 4.9 illustrates the performance of the FeynmanNet architecture for $^ { 4 } \mathrm { H e }$ , $_ 6$ Li, and $^ { 1 6 }$ O, using a linear combination of $N _ { \mathrm { d e t } } = 4$ Slater determinants. Panels (a)–(c) correspond to calculations performed with the model “o” Hamiltonian, also used in the HN calculations discussed earlier, which is based on a leading-order pionless effective field theory expansion. Panel (a) shows that the $^ 4$ He energy rapidly converges to a ground-state value consistent with the numerically exact HH result, while improving upon the SJ ansatz. As emphasized in Ref. [51], this improvement originates from the combined use of multiple determinants and a backflow transformation, which enhances the nodal structure in both spatial and spin–isospin degrees of freedom. For the $p$ -shell nucleus $_ 6$ Li, shown in panel (b), where clustering effects increase the complexity of the wave function, FeynmanNet yields lower variational energies than both the SJ ansatz and HH calculations, the latter exhibiting slow convergence for such a halo-like system [116]. The expressive power of the approach is further demonstrated for $^ { 1 6 } \mathrm { O }$ in panel (c), where FeynmanNet attains energies competitive with constrained-path AFDMC results within a purely variational framework. Notably, a comparison with Fig. 4.8 indicates that FeynmanNet achieves lower variational energies than the HN ansatz. Finally, panel (d) shows results for 4He obtained with a next-to-leading-order pionless effective field theory Hamiltonian from Ref. [61], with a three-body range of $R _ { 3 } = 2 . 0$ fm. This Hamiltonian includes tensor and spin–orbit interactions that render the wave function complex valued and reduce the underlying symmetries. Despite this increased complexity, FeynmanNet retains a convergence rate comparable to the leading-order case and reaches energies consistent with HH calculations, highlighting the robustness of the ansatz.

![](images/aa9b33e3297b62a2e1688c65066f3cab4af2d55ff366c9cf6b2c13a2eadd8bc0.jpg)

![](images/850ae08cd2c96f37a30c9cb51d1cac20931f50d6e2fc40bf2fde4f55c4ecc1ef.jpg)

![](images/bca45f607f6fd2c5a9c46b35f23d7f169efb46631d902f3256b1aee00549fa6e.jpg)

![](images/57b5be899c7a38ae008fc54731b1a5a6e960fb200f0fc9381991744bf26c156c.jpg)  
FIG. 2. Performance of FeynmanNet on the He, Li, and O ground statFigure 4.9: Performance of the FeynmanNet ansatz for the ground states of 4He, $^ 6$ . (a) TLi, and $^ { 1 6 }$ He energy, calculated with the pionless effecO [51]. Panels (a)–(c) show the convergence of the ground-state energies obtained with the model “o” Hamiltonian. Statistical uncertainties from Monte Carlo sampling are indicated by error ing average to the energies. The ground-state energies given by the artificial neural network with Slater-Jastrow (ANN-SJ) ansatzbars, while the solid curves represent exponential moving averages. Results obtained with the SJ ansatz and the HH method are shown for hypershperical-harmonics (HH) method [33] are displayed for comparison. (b) Same as (a) but for 6 Li.comparison where available. Panel (d) displays 4He results obtained with next-to-leading-order Hamiltonians.

# statistical error. (d) Same as (a) but with the Hamiltoni4.2.4. Essential elements of nuclear binding

The authors of Ref. [52] improved the expressivity of the HN ansatz by introducing backflow transformations acting on O. The CD contact term at NLO takes the form V. RESULTS AND DISCUSSIONthe visible coordinates. In particular, they employed the equivariant backflow transformation defined in Eq. (3.46). The vCD (ri j ) vT (ri j )Ti j (20) Figure 2 depicts the performance of FeynmanNet by inclusion of backflow substantially increases the flexibility of the HN ansatz, allowing converged energies to be obtained with a HN number $A _ { h }$ O     that is much smaller than the number of physical nucleons, and in some cases as small as a single nucleon pair (i, j). The specific expressions of the radial 6Li, the obtained ground-state energies are compared withHN. Figure 4.10, adapted from the Supplemental Material of Ref. [52], shows the convergence of the ground-state energy of $^ { 1 6 }$ O computed using Hamiltonian “o” of Ref. [61] with $R _ { 3 } = 1 . 0$ ults given by the , as a function of $A _ { h }$ vious ANN . Even with $A _ { h } = 1$ Jastrow (ANN-, the resulting 6energy is lower than that obtained with $A _ { h } = 1 6$ in the absence of a backflow transformation. The converged energy is Vi jk (ri j, r jk , rki ) = 4 6 e− i j+ jk 3 , (21) and NLO Hamiltonians and, more importantly, is numericconsistent, within uncertainties, with that obtained using the FeynmanNet ansatz, shown in Fig. 4.9, as well as with the constrained-path AFDMC value.

#χ =   π = .   This architecture, employing up to $A _ { h } = 4$ than the ANN-SJ ansatz after training for only about HN to ensure convergence, has been used to compute the ground-state stands for the cyclic permutation of i, j, k.energies per nucleon of selected nuclei with $A \leq 2 0$ for $R _ { 3 } ~ = ~ 1 . 0$ ations, a fm and $R _ { 3 } ~ = 1 . 1$ al result is also consistent with thefm. As shown in the top panel of The LECs in the nuclear Hamiltonian are adjusted to the       Fig. 4.11, the agreement between the computed and experimental values is remarkably good, given the simplicity of the we use the optimal set (model “o”) with R 1.0 fm determinants and backflow transformation, which improinput Hamiltonian. As noted by the authors of Ref. [52], the ground-state energies obtained with this simple Hamiltonian LO and R3 = 2.0 fm at NLO given in Ref. [46] that was the nodal surfaare closer to experiment than those reported in Ref. [42] using AFDMC with N $^ 2$ e in both continuous spatial and discLO chiral EFT interactions. In addition, unlike in NCSM calculations employing consistent N $^ 2$ LO NN and 3N forces [171], no increasing overbinding with mass The rangnumber $A$ of the adopted NN is typically 2 fm, so we use MeV for is observed. An important caveat, however, is that neither $R _ { 3 } = 1 . 0$ the MD fm nor $R _ { 3 } = 1 . 1$ t with Ndet = 1 in Fig. 4( fm yield bound ground

![](images/5adb2ba5a324759fc7fd7d101fc06ecaed2fcd9b65d59f76266893c5fe2c195a.jpg)  
Figure 4.10: Adapted from Ref. [52] with permission from the authors. Ground-state energy of $^ { 1 6 } \mathrm { O }$ obtained using the Hamiltonian “o” of Ref. [61] with $R _ { 3 } = 1 . 0$ fm. The HN results of Ref. [50] are compared with those obtained by incorporating the simple message-passing neural networks backflow transformations introduced in Ref. [52]. For reference, the auxiliary-field diffusion Monte Carlo (AFDMC) energy from Ref. [61], together with its uncertainty, is shown by the orange shaded band, while the best FeynmanNet energy reported in Ref. [51] is indicated by the gray band.

states for $_ 6$ He, $^ 8$ Li, $^ 8$ B, $^ { 9 } \mathrm { C }$ , and $^ { 1 7 } \mathrm { F }$ with respect to breakup into smaller clusters. This behavior points to an excessively repulsive character of the Hamiltonian, since increasing $A _ { h }$ , and thus the flexibility of the NQS, does not lead to an improvement of the variational energies.

The corresponding charge radii are shown in the lower panel of Fig. 4.11. While the overall trend of the experimental data is well reproduced, consistent with the ground-state energies, the radii of $_ 6$ Li, $^ { 7 }$ Li, $^ 7 \mathrm { B e }$ , and $^ { 1 2 }$ C are overestimated. By contrast, the radii of $^ { 1 5 }$ N, $^ { 1 6 }$ O, $^ { 1 7 }$ O, and $^ { 2 0 }$ Ne are underestimated with respect to experiment, particularly for $R _ { 3 } = 1 . 0$ fm. Owing to its longer range, the 3N interaction with $R _ { 3 } = 1 . 1$ fm introduces additional repulsion and leads to larger radii in nuclei with $A \geq 1 5$ compared to the interaction with $R _ { 3 } = 1 . 0$ fm. In contrast to methods based on harmonic-oscillator basis expansions [16], the radii converge rapidly in VMC-NQS calculations. Consequently, the discrepancies between theoretical predictions and experimental data are most likely attributable to deficiencies in the input Hamiltonian.

The magnetic moments of selected nuclei with $A \leq 2 0$ , computed using model “o” with $R _ { 3 } = 1 . 1$ fm, are shown in Fig. 4.12. The theoretical predictions are in good agreement with experimental data, indicating that the NQS captures the nuclear shell structure, which emerges naturally during the energy minimization. Notably, at the beginning of the training, not only the ground-state energies and charge radii, but also the magnetic moments and angular momenta, differ substantially from their converged and experimentally observed values. The minor discrepancies observed for $^ 3 \mathrm { H }$ and 3He, consistent with GFMC, AFDMC, and HH results [42, 172, 173], are likely due to missing two-body current contributions.

# 4.2.5. High-resolution potentials

Most nuclear-physics applications of VMC methods with NQS take as input interactions based on pionless effective field theory. After the pioneering 2019 work [47], non-stochastic NQS-based approaches have been employed to solve light nuclear systems with high-resolution interactions. In this context, the authors of Ref. [174] introduced a compact neuralnetwork architecture based on a partial-wave expansion of the nuclear wave function, in which the radial components

![](images/955a3f7a2b8c276fb6609ba06f0d45dfd2426a1f343c5c6b21d692405d9fdb76.jpg)

![](images/46aae3b2618576e1bca0066fbe989b18cabd42e4a31a4a30159bdcc2360ca503.jpg)

![](images/8c5b429f831b42480154f95bb563591bfee073dadfa3c3bc0eca50359264b71d.jpg)  
Figure 4.11: Adapted from Ref. [52] with permission from the authors. Energies per particle (upper panel) and charge radii (lower panel) of selected nuclei with up to $A = 2 0$ obtained using the Hamiltonian “o” of Ref. [61] with $R _ { 3 } = 1 . 0$ fm and $R _ { 3 } = 1 . 1$ fm, compared with experimental data.   
Figure 4.12: Adapted from Ref. [52] with permission from the authors. Magnetic moments of selected nuclei with $A \leq 2 0$ obtained from VMC-NQS calculations using the Hamiltonian “o” of Ref. [61] with $R _ { 3 } = 1 . 1$ fm, compared with experimental data.

are represented by separate neural networks. This method was shown to accurately reproduce the deuteron ground-state energy and wave function starting from the highly realistic Argonne $v _ { 1 8 }$ NN potential [46], including its full spin–isospin

operator structure. More recently, closely related deterministic neural-network approaches have been extended beyond the two-body sector. In particular, Ref. [175] introduced an unsupervised deep-learning framework to solve both two- and three-body bound-state problems directly in coordinate space. Building on a discretized representation of the Schrödinger equation, the authors employed deep neural networks to represent the radial wave functions of coupled channels, achieving accurate calculations of $^ 2 \mathrm { H }$ and $^ 3 \mathrm { H }$ using the Entem–Machleidt N $^ { 3 }$ LO chiral-EFT potential of Ref. [148].

By contrast, actual VMC calculations based on NQS have more recently been carried out using high-resolution local Hamiltonians that are either phenomenological or derived within chiral EFT [57, 58, 66]. In particular, the authors of Ref. [66] presented QMC calculations of neutron– $\alpha$ D-wave phase shifts using chiral-EFT Hamiltonians at the three lowest orders in the chiral expansion: LO, NLO, and N $^ 2$ LO. Specifically, they employed the local $N N$ and $3 N$ potentials constructed in Ref. [67, 176]. However, the analysis was limited to the softest cutoff value, $R _ { 0 } = 1 . 2$ fm, which corresponds to a typical momentum cutoff $\Lambda \simeq 4 0 0$ MeV.

As in previous QMC studies of neutron– $\alpha$ scattering, the continuum problem is mapped onto a bound-state eigenvalue problem. To this end, an external harmonic-oscillator (HO) confining potential is added to the nuclear Hamiltonian through an additional two-body term of the form

$$
V _ {\mathrm {H O}} = \sum_ {i <   j} \frac {1}{2} \frac {m _ {N}}{A} \omega^ {2} r _ {i j} ^ {2}, \tag {4.12}
$$

where $m _ { N }$ denotes the nucleon mass, $\omega$ the HO frequency, and $r _ { i j }$ the relative distance between nucleons. The presence of the HO trap discretizes the spectrum, enabling the extraction of scattering information from bound-state energies. The neutron– $\alpha$ D-wave phase shifts are then obtained using the Busch–Englert–Rzażewski–Wilkens (BERW) formalism [177, 178], which relates the trapped eigenenergies of 5He and the ground-state energy of 4He to free-space scattering observables.

In Ref. [66], the energies of both 4He and $_ 5$ He are computed using the GFMC method. The lowest $J ^ { \pi } = 5 / 2 ^ { + }$ eigenstate of 5He is projected via imaginary-time propagation, starting from a previously optimized NQS. The trial wave function is taken in the form of Eq. (3.27), augmented by the transformation defined in Eq. (3.28). Despite the use of highly sophisticated variational wave functions, the GFMC propagation suffers from a severe fermion-sign problem. This issue is mitigated through a combination of constrained-path propagation followed by a transient estimate [179]. Nevertheless, the sign problem remains sufficiently severe that only the softest available cutoff value, $R _ { 0 } = 1 . 2$ fm, could be employed in the chiral nuclear Hamiltonian.

Figure 4.13 illustrates the neutron– $\alpha$ D-wave phase shifts predicted at different orders of chiral EFT as a function of the center-of-mass energy $E _ { \mathrm { c . m . } }$ . Each point corresponds to an individual GFMC calculation performed in a harmonicoscillator trap and is extracted using the BERW formalism. The theoretical predictions are compared with phase shifts obtained from $R$ -matrix analyses of elastic-scattering data [180]. At leading order, the chiral Hamiltonian yields nearly vanishing phase shifts, in line with general expectations. The dominant contribution emerges at next-to-leading order with the inclusion of the two-pion-exchange $N N$ interaction, but the resulting phase shifts significantly overestimate the empirical values. Corrections at next-to-next-to-leading order reduce the phase shifts and bring the theoretical predictions into closer agreement with the data. At this order, the leading $3 N$ force plays a crucial role, while the subleading two-pionexchange $N N$ interaction has a comparatively minor impact for the soft regulator values considered. Overall, these results identify neutron– $\alpha$ D-wave scattering as a sensitive probe of the long-range structure of the three-nucleon interaction.

In a later work [58], the same authors improved their variational ansatz by adopting a fully multiplicative form of two-body correlations, rather than the linearized version of Eq. (3.27). Using this more sophisticated wave function, they computed the binding energies of $^ { 4 } \mathrm { H e }$ and $_ 6$ Li with accuracy comparable to GFMC and significantly improved relative to

![](images/1f02ed96c67492e0872d067dac0dcb71c8ce780c623ad38a99a96063807d6b2d.jpg)  
2 FIG. 2. Phase shifts for neutroFigure 4.13: From Ref. [66], reproduced with permission. Neutron– $_ \alpha$ -α scattering in tphase shifts in the $^ 2 D _ { 5 / 2 }$ 5 channelchannel as a function of the center-of-mass as a function of the center-of-mass energy predicted at differentenergy, predicted at different orders of chiral EFT. Empty symbols denote GFMC results with statistical error bars, while shaded bands indicate orders of the chiral EFT expansion. Empty symthe combined statistical and BERW-related systematic uncertainties. Stars correspond to $R$ ols refer to the-matrix analyses of experimental neutron– $_ \alpha$ elasticscattering data [180], and red diamonds are taken from a private communication between the authors of Ref. [66] and G. M. Hale.

tion W has the form systematic uncertainties of the BERW formula (see Supplementalearlier VMC and AFDMC calculations. Notably, because VMC does not suffer from a fermion-sign problem, they were Material [56] for details). The stars and diamonable to employ local chiral-EFT interactions from Refs. [67, 176] with both $R _ { 0 } = 1 . 2$ om thefm and the harder cutoff $R _ { 0 } = 1 . 0$ r ; r : 7 data from [44] and [60], respectively.fm. In addition, they considered the high-resolution phenomenological Argonne $v _ { 8 } ^ { \prime }$ plus UIX Hamiltonian.

These calculations resolved the longstanding discrepancy between effective and elastic Zemach radii in $_ 6$ Li and 7Li through ab initio nuclear-structure calculations that consistently include nuclear polarizability effects. Enabled by the n effects [52], which [23], we use a transient estimate to mitigate the signuse of highly sophisticated NQS, the results show that nuclear polarizability effects are negligible in 7Li but dominant in f $_ 6$ rmance of neural- problem. We first perform the constrained-path propagationLi, thereby accounting for the observed deviation between the effective and elastic Zemach radii.

[53], which suppresses the sign problem, and then relThe authors of Ref. [57] employed the wave-function ansatz of Eq. (3.30) to study $A = 3$ nuclei, using as input the of two- and three- local chiral-EFT Hamiltonians of Refs. [56, 68]. Importantly, these interactions include tensor and spin–orbit components [53]. Iin the $N N$ ntrast, the pared to those without performing constrained-path propa-sector, as well as a consistent spin-isospin-dependent three-nucleon force. As discussed in Section 3.4.2, a gation at first. Moreover, the softest available cutoff value ofnormalizing flow is used to generate the samples required for the Monte Carlo estimation of the energy and its gradient. 0 ¼         Notably, the use of normalizing flows avoids the correlation-length problem that typically affects Markov chain Monte tion functions lCarlo algorithms.

rgies [45–47,52] GFMC calculations wFigure 4.14 displays the ground-state energy of $^ 3 \mathrm { H }$ neural-network wave functions. obtained using the N2LO chiral interaction with regulator values $( R _ { 0 } , \Lambda ) = ( 1 . 2 , \mathrm { f m } , 1 , \mathrm { G e V } )$ Figure 2 depicts the D-wave neutron-α phase shift. The energy and its uncertainty are estimated over 500 iterations, with 40,000 samples per work wave function,iteration generated by the normalizing flow. The average NQS energy is $E = - 8 . 3 0 \pm 0 . 0 9$ MeV, which closely matches the to project oGFMC result, $E = - 8 . 3 4$ corresponds to a single GFMC calculation using a HO trap, MeV. The two values agree within one-half of a standard deviation and differ by only $0 . 4 5 \%$ .

nary time propa- and it is derived from the BERW formula [Eq. (4)]. TheThese results indicate that the neural-network-generated wave function can effectively approximate the $^ 3 \mathrm { H }$ ground state values of HO frequency ω are chosen such that the oscillator with the soft-core interaction, without any imaginary-time evolution, even in the presence of complicated pion-exchange : 8  ¼ ð N Þ       ¼  terms as well as tensor, spin-orbit, charge-independence-breaking, and charge-symmetry-breaking interactions.

![](images/113a7d19061d9e8c8dc2517f9827fcfbbbf0945e0c43467f130b665e625669cf.jpg)  
Figure 4.14: From Ref. [57], reproduced with permission. Evaluation of the $^ 3 \mathrm { H }$ ground-state energy obtained with optimized neural-network wave functions using the full N2LO chiral interaction with $( R _ { 0 } , \Lambda ) = ( 1 . 2 \mathrm { f m } , 1 \mathrm { G e V } )$ . The average energy (blue horizontal line) and standard trained neural networks with the full version of the N LO chi-deviation (blue shaded band) are estimated over 500 iterations with 40,000 samples per iteration. The conventional VMC result is displayed by the purple line

# ite4.3. Nuclear matter

Multi-messenger astronomy is creating new observations of matter at densities and isospin asymmetries which are not directly accessible by terrestrial experiments, expanded most recently with the observation of GW170817 [181–184]. neural netwoTheoretical modeling of this matter, in particular material similar to the inner crust of neutron stars, poses significant captured by NN and represented as ! R˜ + R˜ . We next echallenges due to the inherent complexity of clustering phenomena, the emergence of superfluidity, and the existence The middle panel of Figure 2 illustrates how this feature to model nuof both free neutrons and neutron-rich nuclei. Various phenomenological approaches have been developed to address is encoded through Rik = NNa(rik), which gradually in- finer-resolutisome of these challenges, including the compressible liquid-drop model [185–193] and self-consistent mean-field models [194–196]. In the former, the energy is parameterized as a function of global properties, and the nucleons within ij        clusters are treated separately from the free neutrons, all of which are assumed to be uniformly distributed. While this ij   3H and 3Hetreatment has a low computational cost, it neglects quantum mechanical shell effects, which are critical for determining (c) 1,000 iteratithe equilibrium composition of the crust. In contrast, self-consistent mean-field models are fully quantum mechanical, presented inconstructing the many-body state in terms of single-particle or quasi-particle wave functions. However, since they neglect sion at short r implies that the probability of finding VMC prediccorrelations beyond the mean-field approximation, they have limited applicability for low-density nuclear matter, where two particles closely separated is extremelystrong correlations may lead to significant deviations from the mean-field behavior.

is consistent with the repulsive nature of short-range nu- the chiral exRecently, VMC methods utilizing NQS have been used to model nuclear matter without making similar, limiting clear interactions. Moreover, fij exhibits a strong de- We see thatassumptions within both pure neutron matter (PNM) and symmetric nuclear matter (SNM) using a pionless EFT potenwell when dtial [53, 55]. The initial results show promise through capturing signs of density dependent neutron superfluidity in PNM (c) likely due toas well as successfully modeling clustering in nuclear matter, without any assumptions on the structure of the material.

# k=i, 4.3.1. Pure neutron matter

observed in the correlation functions and therefore is suit-Low-density neutron matter is characterized by fascinating emergent quantum phenomena, such as the formation of able for the importance sampling Monte Carlo estimationCooper pairs and the onset of superfluidity. Quantum Monte Carlo approaches [31], in particular the auxiliary-field of the energy.diffusion Monte Carlo (AFDMC) method [40], have been extensively applied to accurately compute neutron-matter We next use the well-trained neural network models 0  properties [89, 197, 198]. In the low-density regime, AFDMC calculations have convincingly shown a depletion of the

![](images/808a28a68212a7855bdfd642530164eb6444a03f9d893a901f634f60fcc6e9a9.jpg)

![](images/2d992ee75b1fe84ca881466139bfe4a3046632a5f08640a5c52020b178eef9b0.jpg)  
Figure 4.15: NQS training data in neutron matter at $\rho = 0 . 0 4 ~ \mathrm { f m ^ { - 3 } }$ (data points) compared with Hartree-Fock (dotted line), conventional VMC (dashed line), constrained-path AFDMC (dash-dotted line) and unconstrained-path AFDMC results (solid line).   
Figure 4.16: Spin-singlet and triplet two-body distribution functions at $\rho = 0 . 0 1 ~ \mathrm { f m ^ { - 3 } }$ (panel a), $\rho = 0 . 0 4 ~ \mathrm { f m ^ { - 3 } }$ (panel b), and $\rho = 0 . 0 8$ fm−3 (panel c) vs pair distance in units of the Wigner-Seitz radius. The NQS calculations (solid symbols) are compared with non-interacting Fermi Gas results (solid lines).

superfluid gap with respect to BCS theory [199, 200]. However, because of the fermion sign problem, AFDMC predictions depend upon the starting variational wave function. For instance, the superfluid phase must be assumed a priori. No assumption of the phase is necessary when NQS are used to compute the initial variational state. It can be seen in Fig. 4.15 that the final trained state for a simulation of 14 neutrons with periodic boundary conditions that the variational NQS is able to recover almost an identical ground state energy to the unconstrained AFDMC calculation.

The trained NQS wave functions from these simulations are also used to evaluate two-body pair distributions as defined in Ref. [140]. Fig. 4.16 shows these distributions at $\rho = 0 . 0 1 \ \mathrm { f m ^ { - 3 } }$ (panel a), $\rho = 0 . 0 4 ~ \mathrm { f m ^ { - 3 } }$ (panel b), and $\rho = 0 . 0 8$ $\mathrm { f m } ^ { - 3 }$ (panel c). The significant increase in the spin-singlet channel compared to the non-interacting Fermi Gas indicates that the NQS wave function can capture the emergence of the $^ { 1 } S _ { 0 }$ neutron pairing, despite not being explicitly encoded in the ansatz. Consistent with the behavior of the pairing gap [199, 201], the enhancement is more prominent at low densities and vanishes at higher densities. On the other hand, at these densities, no pairing correlations are present in the spin-triplet channel.

![](images/21cc0987fe49d6bc119b80665f4a84154e6310cd1df843a55cdfe2a8189bff5f.jpg)  
Figure 4.17: Energy per particle of SNM from NQS and AFDMC simulations. The NQS results (blue circles) indicate stronger binding compared to AFDMC (orange squares), attributed to clustering at low densities. Our low-density results are compared to $^ { 2 8 }$ Si with no electromagnetic contribution, which serves as the expected zero-density ground state for a simulation of $N = 2 8$ nucleons with $x = 1 / 2$ . The error bars represent 95% confidence intervals for the mean.

# 4.3.2. Clustering

Simulations of matter with protons as well as neutrons are complicated by the nuclear interaction acting simultaneously in distinct spin-isospin channels, most notably the $^ { 1 } S _ { 0 }$ and $^ 3 S _ { 1 }$ channels, rather than collapsing to a single dominant channel as in pure neutron matter (see Section 2.1). This richer structure leads to pronounced clustering that is difficult for many methods to capture without simplifying assumptions. NQS, however, excel at learning these complex relationships.

Reference [55] utilizes the MPNN backflow method with the Pfaffian–Jastrow architecture to efficiently learn pairing correlations within isospin symmetric and asymmmetric matter. With this approach, NQS are able to correctly learn the structure of matter through a range of densities corresponding to the inner crust of neutron stars. Figure 4.17 shows ground state energies learned by the NQS are significantly improved compared to state-of-the-art AFDMC calculations given identical assumptions. For a simulation containing 28 particles, the expected low-density limit of periodic symmetric matter corresponds to the ground-state energy of $^ { 2 8 }$ Si in the absence of electromagnetic interactions. The NQS results approach this limit, providing clear evidence that clustering effects are being accurately captured. Further improvements may be achieved by initializing AFDMC calculations from a NQS wave function.

# 4.3.3. Beta-equilibrated matter

Cold nuclear matter at densities found in the inner crust of neutron stars is mostly composed of neutrons, protons, and electrons. Assuming the matter is neutrino transparent, the relative abundance of these particles at a specific density can be determined using a model for the energy as a function of proton fraction, under the well-supported assumptions of charge neutrality, $n _ { p } = n _ { e }$ , and beta equilibrium, $\mu _ { e } = \mu _ { n } - \mu _ { p }$ [202]. This model, along with simulation results for SNM and PNM, can be used to construct an equation of state for beta-equilibrated nuclear matter given a particular Hamiltonian.

At zero temperature, the beta-equilibrium condition directly relates the proton fraction to the density dependence of

the symmetry energy, defined as the difference between the energies of PNM and SNM. Working out these relations yields

$$
\mu_ {n} - \mu_ {p} = - \frac {\partial E (n _ {B} , x)}{\partial x} = 4 (1 - 2 x) S (n _ {B}), \tag {4.13}
$$

together with the expression for the electron density,

$$
x \equiv \frac {n _ {p}}{n _ {B}} = \frac {n _ {e}}{n _ {B}} = \frac {\left(\mu_ {e} ^ {2} - m _ {e} ^ {2}\right) ^ {3 / 2}}{3 \pi^ {2} n _ {B}}, \tag {4.14}
$$

which jointly determine the proton fraction in beta-equilibrated matter.

Due to the low proton fractions in the crust, directly modeling nuclear matter at these isospin asymmetries may require hundreds of nucleons to suppress finite-size effects associated with clustering. Such calculations are currently infeasible with ab initio variational Monte Carlo methods. Instead, in Ref. [55] simulations of PNM and SNM are performed, and ground-state energies at intermediate isospin asymmetries are inferred using well-known expansions in the neutron richness, given by $E ( n _ { B } , x ) = E { \left( n _ { B } , 1 / 2 \right) } + ( 1 - 2 x ) ^ { 2 } S { \left( n _ { B } \right) }$ .

The resulting proton fraction in beta-equilibrated matter as a function of baryon density is displayed in Fig. 4.18. The NQS predictions align closely with the phenomenological Skryme parameterizations of the equation of state (SLy4 EOS) for the inner crust of neutron stars [188, 203]. Figure 4.18 underscores the flexibility of the NQS ansatz: by leveraging identical neural network architectures across all densities, they successfully capture the complexity of nuclear structures relevant to the inner crust of neutron stars. In contrast, the AFDMC yields proton fractions that tend towards those of non-interacting matter. This difference arises because AFDMC does not account for the onset of nuclear clusters at low densities, which significantly lowers the energy per particle in isospin-symmetric nuclear matter, as captured by NQS. For instance, at $n _ { B } = 0 . 0 0 1 ~ \mathrm { f m ^ { - 3 } }$ , the NQS predicts an energy per particle that is 7.334(46) MeV lower than AFDMC, while at $n _ { B } = 0 . 0 8 ~ \mathrm { f m ^ { - 3 } }$ , this difference reduces to 0.758(35) MeV. In contrast, both methods yield similar energies for pure neutron matter, where clustering effects are absent, as shown in Ref. [53]. As a result, when solving the beta-equilibrium equations, the NQS predicts a higher proton fraction compared to AFDMC, reflecting its ability to capture nuclear clustering effects at low densities. All in all, these initial results showcase the potential of NQS simulations for dense matter physics of relevance for astrophysical simulations.

# 4.4. Electroweak interactions

Studying the response of a many-body system to perturbative probes is of great relevance for extracting information about the system’s dynamical structure at both the nuclear and nucleon levels [204]. These calculations are crucial for interpreting electron-scattering experiments, including assessing whether explicit QCD effects are required to explain the measured response functions [205–207]. Moreover, they are essential for fully exploiting current and next-generation accelerator-based neutrino oscillation experiments [22, 80], which use atomic nuclei in their detectors to enhance event rates.

In the linear-response regime, the interaction of an atomic nucleus with electroweak probes is described by the nuclear response function

$$
\mathcal {R} (\omega) = \iint_ {f} | \langle \Psi_ {f} | \hat {O} | \Psi_ {0} \rangle | ^ {2} \delta (E _ {f} - E _ {0} - \omega), \tag {4.15}
$$

which encapsulates the dynamical part of the reaction. In the above equation, $\hat { O }$ denotes the excitation operator, while $\left| { \Psi _ { 0 } } \right.$ and $\vert \Psi _ { f } \rangle$ represent the initial and final states of the system, with energies $E _ { 0 }$ and $E _ { f }$ , respectively. The final state may be either bound (belonging to the discrete part of the spectrum) or unbound (in the continuum). A direct evaluation of the response function therefore, in principle, requires calculating each individual transition amplitude.

![](images/abdd9b0bc228e078ec1e29065d38e1dfcfdcbed90b288fe0f78802cc21ea7d75.jpg)  
Figure 4.18: Proton fraction in beta-equilibrated matter as a function of baryon density. Blue circles and orange squares represent NQS and AFDMC calculations for $A = 2 8$ nucleons, respectively. Blue up-triangles and down-triangles indicate NQS results for $A = 4 2$ and $A = 1 4$ , respectively, highlighting finite-size effects. The green dashed line shows non-interacting matter, and the red solid curve represents a Skyrme parametrization of the equation of state (SLy4 EOS) for the inner crust of neutron stars [188, 203]. The inset displays NQS results for varying particle numbers at a density of $0 . 0 4 ~ \mathrm { f m ^ { - 3 } }$ to illustrate finite-size effects.

Microscopically computing continuum wave functions for medium-mass nuclei remains an outstanding theoretical challenge. At each continuum energy, the many-body wave function fragments into numerous channels, each representing a distinct breakup configuration, leading to substantial complexity in both momentum and coordinate representations. Integral transform techniques, such as the Laplace transform [208] and the Lorentz integral transform (LIT) [209], circumvent the difficulties associated with the direct calculation of continuum final states, reformulating the problem as a bound-state calculation.

The LIT is defined as

$$
\mathcal {L} \left(\omega_ {0}, \Gamma\right) = \int_ {\omega_ {t h}} ^ {\infty} d \omega \frac {\mathcal {R} (\omega)}{\left(\omega - \omega_ {0}\right) ^ {2} + \Gamma^ {2}}, \tag {4.16}
$$

where $\omega _ { t h }$ is the threshold energy and $\Gamma > 0$ is the Lorentzian width, serving as a resolution parameter. The LIT method proceeds in two steps. First, $\mathcal { L } ( \omega _ { 0 } , \Gamma )$ is computed directly, without requiring explicit knowledge of $\mathcal { R } ( \omega )$ . In a second step, the dynamical response function is obtained through an inversion of the LIT.

The function $\mathcal { L } ( \omega _ { 0 } , \Gamma )$ can be computed starting from its definition and substituting the expression in Eq. (4.15) for $\mathcal { R } ( \omega )$ . Using the completeness relation of the Hamiltonian eigenstates

$$
\iint_ {f} \left| \Psi_ {f} \right\rangle \left\langle \Psi_ {f} \right| = 1 \tag {4.17}
$$

yields

$$
\mathcal {L} \left(\omega_ {0}, \Gamma\right) = \frac {\Gamma}{\pi} \left\langle \Psi_ {0} \right| \hat {O} ^ {\dagger} \frac {1}{(\hat {H} - z)} \frac {1}{(\hat {H} - z ^ {*})} \hat {O} | \Psi_ {0} \rangle . \tag {4.18}
$$

We denote with $\Psi _ { L }$ the solution of the inhomogeneous Schrödinger equation

$$
(\hat {H} - z) | \Psi_ {L} \rangle = \hat {O} | \Psi_ {0} \rangle , \tag {4.19}
$$

where $z = E _ { 0 } + \omega _ { 0 } + i \Gamma$ . Finding the solution for different values of $\omega _ { 0 }$ and $\Gamma$ lead directly to the transform

$$
\mathcal {L} (z) = \frac {\Gamma}{\pi} \left\langle \Psi_ {L} \mid \Psi_ {L} \right\rangle . \tag {4.20}
$$

Because $\mathcal { L } ( z )$ is finite, the solution of Eq. (4.19) has the same asymptotic boundary conditions as a bound state.

In Ref. [210], the LIT of the dipole operator was computed for the first time using NQS, specifically the Pfaffian– Jastrow ansatz of Eq. (3.39), to represent both $\Psi _ { 0 }$ and the LIT state $\Psi _ { L }$ . In that work, the LIT equation is solved by maximizing the quantum fidelity between the auxiliary state $| \Psi \rangle \equiv ( \hat { H } - z ) | \Psi _ { L } \rangle$ and the source state $\vert \Phi \rangle \equiv { \hat { O } } \vert \Psi _ { 0 } \rangle$ , where the fidelity is defined as [211]

$$
\mathcal {F} (\Psi , \Phi) = \frac {\langle \Psi | \Phi \rangle \langle \Phi | \Psi \rangle}{\langle \Psi | \Psi \rangle \langle \Phi | \Phi \rangle}. \tag {4.21}
$$

The optimal parameters $\pmb { \theta }$ of the NQS are obtained by maximizing a linear combination of the fidelity defined above and a reverse Kullback–Leibler divergence between the target and proposal distributions $\operatorname { K L } ( \pi _ { \Psi } \parallel \pi _ { \Phi } )$ , where

$$
\pi_ {\Psi} (X) = \frac {| \Psi (X) | ^ {2}}{\langle \Psi | \Psi \rangle}, \quad \pi_ {\Phi} (X) = \frac {| \Phi (X) | ^ {2}}{\langle \Phi | \Phi \rangle}. \tag {4.22}
$$

The gradient of the loss function reads

$$
g _ {\boldsymbol {\theta}} = \nabla_ {\boldsymbol {\theta}} \mathcal {F} - \lambda \nabla_ {\boldsymbol {\theta}} \mathrm {K L} \left(\pi_ {\Psi} \| \pi_ {\Phi}\right), \tag {4.23}
$$

with $\lambda \ : = \ : 1$ in typical applications. Stable parameter updates are achieved by employing the spring algorithm (see Section 3.2) [109], which leads to the damped linear system $\bigl ( S + \epsilon I \bigr ) \delta \pmb \theta = g _ { \pmb \theta } + \epsilon \mu \delta \pmb \theta _ { \mathrm { p r e v } }$ . To ensure scale invariance, the authors of Ref. [210] set $\epsilon = \varepsilon \langle \mathrm { d i a g } ( S ) \rangle$ with a small $\varepsilon = 1 0 ^ { - 3 }$ . Note that maximizing the fidelity only fixes the auxiliary state $\left| \Psi \right.$ up to an overall complex normalization constant [212], given by $\mathcal { N } = \langle \Phi | \Psi \rangle / \langle \Phi | \Phi \rangle$ , which is estimated stochastically by sampling from $\pi _ { \Phi } ( X )$ .

Computing the LIT as the norm of $\Psi _ { L }$ is computationally challenging due to the slowly decaying and oscillatory tails of this wave function. To address this difficulty, one can rewrite the norm as

$$
\left<   \Psi_ {L} | \Psi_ {L} \right> = \left<   \Phi | \frac {1}{\hat {H} - z ^ {*}} \frac {1}{\hat {H} - z} | \Phi \right> = \frac {1}{\Gamma} \mathrm {I m} \left<   \Phi | \Psi_ {L} \right>
$$

which can instead be estimated in a numerically stable manner by sampling from $\pi _ { \Phi } ( X ) = | \Phi ( X ) | ^ { 2 } / \langle \Phi | \Phi \rangle$ . The authors of Ref. [210] also provide the following upper bound on the LIT uncertainty

$$
\Delta \mathcal {L} \left(\omega_ {0}, \Gamma\right) \leq \mathcal {D} \frac {\mathcal {N} ^ {- 1} \| \Phi \rangle |}{\Gamma} \sqrt {\frac {1 - \mathcal {F}}{\mathcal {F}}}, \tag {4.24}
$$

where

$$
\mathcal {D} = \min  \left(\left| (1 - P _ {\Phi}) | \Psi_ {L} \rangle \right|, \left| (1 - P _ {\Phi}) \frac {H}{| z |} | \Psi_ {L} \rangle \right|\right), \tag {4.25}
$$

and $P _ { \Phi } = | \Phi \rangle \langle \Phi | / \langle \Phi | \Phi \rangle$ . This relation implies that in the limit $\Gamma  0$ , $\omega _ { 0 } ~ \approx ~ \omega$ , and ${ \mathcal { L } }  ( \pi / \Gamma ) { \mathcal { R } }$ one finds $\Delta \mathcal { L } / \mathcal { L } \propto$ $\sqrt { ( 1 - \mathcal { F } ) / \Gamma }$ . Hence, choosing a smaller $\Gamma$ not only makes the required wave function more complex, but also demands correspondingly higher fidelity in the solution of the LIT equation.

Once the central values and the corresponding uncertainties of the LIT are determined, one needs to invert the integral transform to retrieve the response function and obtain the corresponding cross sections to be compared with experimental data. In Ref. [210] two different techniques have been investigated. The first is a regularized version of the standard inversion procedure introduced in Ref. [209], which relies on a suitable basis expansion of the response function. The second is an improved version of the so-called Bryan’s version of the Maximum Entropy method [213] which enables the propagation of the uncertainties in $\mathcal { L } ( \omega _ { 0 } , \Gamma )$ into the reconstructed $\mathcal { R } ( \omega )$ using Bayes’ theorem.

![](images/715c1e62806bb59b7178650d7810ba8abc8a6ea8cf8de08b682cd449e58cbe85.jpg)  
Figure 4.19: Adapted from Ref. [210] with permission from the Authors. Photo-disintegration cross section of $^ 4 \mathrm { H e }$ as a function of photon energy, obtained from NQS calculations of the LIT. The basis function results (solid orange lines) and the Maximum Entropy reconstruction (blue histogram with error bars) show good agreement with experimental data from Ref. [204].

Figure 4.19, adapted from Ref. [210] displays the photodisintegration cross section of $^ { 4 } \mathrm { H e }$ , obtained by inverting the LIT computed for $\Gamma = 1 0$ MeV within the NQS framework, and compare it with experimental data from Ref. [204]. The basis-expansion inversion method in orange and the maximum entropy approach in blue yield results that agree remarkably well with experiment, despite the simplicity of the input Hamiltonian.

# 4.5. Pairing interactions and the occupation-number formalism

All $A > 2$ nuclear physics applications of NQS discussed so far entail solving the quantum many-body problem in coordinate space, with the antisymmetry of the wave function enforced explicitly through tailored architectures, such as Slater determinants or Pfaffians. In this setting, fermionic statistics are hard-coded at the level of the wave function ansatz. A complementary and conceptually distinct approach consists in working in the occupation-number (second-quantized) formalism [91], where the many-body basis is built from antisymmetrized Fock states. In this representation, fermionic antisymmetry is not imposed on the neural-network architecture itself, but is instead automatically taken into account when evaluating expectation values of quantum-mechanical operators through the underlying algebra of creation and annihilation operators [214]. This shifts the burden of enforcing antisymmetry from the variational ansatz to the operator formalism.

In the second quantization setting within the occupation number formalism, a NQS representation can be chosen to be

$$
\Psi (N) \equiv \langle N | \Psi \rangle , \tag {4.26}
$$

where $\vert N \rangle = \vert n _ { 1 } , . . . , n _ { P } \rangle$ denotes a basis state in Fock space. The state is specified by occupation numbers $n _ { i }$ indicating whether the fermionic mode $i$ is occupied ( $n _ { i } = 1$ ) or empty ( $n _ { i } = 0$ ). Within this general framework, a particularly important class of applications involves pairing correlations, which provide a natural setting for occupation-number– based NQS approaches. In many physically relevant applications, the full fermionic Fock space is further restricted to a subspace adapted to the dominant correlations of the problem. For pairing interactions, this corresponds to limiting the Hilbert space to seniority-zero configurations, in which fermions occupy time-reversed states in correlated pairs. Within this restricted subspace, the occupation-number representation naturally encodes the presence or absence of fermion pairs in a set of active modes.

From a physical perspective, pairing correlations underlie a wide range of phenomena in interacting fermionic systems [142, 215, 216]. BCS theory provides the canonical framework for understanding pairing in electronic superconductors, wherein fermions near the Fermi surface form correlated Cooper pairs, giving rise to superconductivity. Soon after the formulation of BCS theory, Bohr, Mottelson, and Pines identified an analogous pairing mechanism in atomic nuclei, in which nucleons near the Fermi surface form spin-singlet pairs [215].

In finite nuclei, pairing manifests itself through characteristic signatures such as enhanced binding of even–even systems, energy gaps to the first excited states, and systematic trends in excitation spectra and moments of inertia. These effects are commonly described within mean-field frameworks such as BCS and its particle-number conserving extensions, most notably the Hartree–Fock–Bogoliubov formalism [217]. Beyond the mean-field level, symmetry restoration and configuration mixing techniques further refine the treatment of pairing correlations, particularly in finite systems.

Pairing Hamiltonians also play an important methodological role. Despite their apparent simplicity, they capture essential nonperturbative physics and include integrable subclasses, such as the Richardson–Gaudin models [218–220], which admit essentially exact solutions. As a result, pairing models provide valuable benchmarks for many-body methods, allowing controlled assessments of accuracy across weak- and strong-coupling regimes.

In its most compact form, the pairing Hamiltonian proposed by Richardson is given by

$$
H = \sum_ {p = 1} ^ {P} d _ {p} N _ {p} - \sum_ {p, q = 1} ^ {P} g _ {p q} A _ {p} ^ {\dagger} A _ {q}, \tag {4.27}
$$

where $\begin{array} { r } { N _ { p } = \sum _ { \sigma \in \{ - , + \} } a _ { p \sigma } ^ { \dagger } a _ { p \sigma } } \end{array}$ is the pair number operator. The operators $A _ { p } ^ { \dagger } = a _ { p + } ^ { \dagger } a _ { p - } ^ { \dagger }$ and $A _ { p } = a _ { p + } a _ { p - }$ create and annihilate fermion pairs, respectively. Exact solutions for this model can be obtained both for uniform pairing strengths, $g _ { p q } = g$ for all $p , q = 1 , \ldots , P$ , and for separable hyperbolic couplings of the form $g _ { p q } = 2 g \sqrt { ( \alpha - d _ { p } ) ( \alpha - d _ { q } ) }$ .

Once a neural-network quantum-state ansatz $\Psi _ { V } ( N )$ is adopted to represent the many-body wave function, quantummechanical expectation values can be estimated stochastically using the Metropolis–Hastings algorithm. Since the number of fermion pairs is conserved, admissible Monte Carlo updates consist of exchanging occupations between pair modes, ensuring ergodicity of the sampling. This procedure is directly analogous to the isospin-exchange moves discussed in Section 3 within the first-quantized formulation.

As in coordinate-space approaches, the optimal values of the variational parameters defining the NQS are determined by invoking the variational principle. To this end, all optimization strategies introduced in Section 3 remain applicable in the occupation-number representation, including the stochastic reconfiguration method supplemented with the RMSPropinspired shift of Eq. (3.11).

The main advantage of this formalism is that the NQS itself does not need to be antisymmetric. As a result, relatively simple architectures, such as restricted Boltzmann machines and feed-forward neural networks, provide valid representations of the many-body wave function (see however Refs. [221, 222] for a critical assessment of the representational power of NQS in second quantization). To demonstrate the power of this approach, the authors of Ref. [223] consider the pairing Hamiltonian in Eq. (4.27) for the exactly solvable uniform-coupling and separable-coupling cases. The NQS is parameterized as

$$
\Psi_ {V} (N) = e ^ {\mathcal {U} (N)} \tanh  \left[ \mathcal {V} (N) \right], \tag {4.28}
$$

where both $\mathcal { U } ( N )$ and $\mathcal { V } ( N )$ are MLPs. Although this functional form resembles those employed in Refs. [48, 49, 116], the resulting architectures are significantly simpler, as they do not rely on permutation-invariant Deep Sets constructions [111].

In Fig. 4.20, Ref. [223] compares correlation energies obtained with VMC–NQS, many-body perturbation theory

![](images/128f8490e71ad1c815c20de242c9bf33a21ff8c971e0f5f0001172ea969a2c8f.jpg)

![](images/8d0656de0562c1a513404a02ac9520ba9b49c72339d935b082033f60de11f402.jpg)  
Figure 4.20: Correlation energies as a function of the interaction strength $g$ for the constant-coupling pairing model (left) and the separablecoupling model (right), both with $P = 1 0$ energy levels and five fermion pairs. Results from VMC-NQS (orange circles), MBPT (red triangles), and pCCD (green crosses) are compared with the exact solution (solid blue line).

(MBPT), and pair coupled-cluster doubles (pCCD) against the exact solution for both the constant-coupling and separablecoupling pairing models. While all approaches yield similar results in the weak-coupling regime, MBPT rapidly deviates from the exact solution as the interaction strength increases, reflecting the breakdown of perturbation theory in the presence of strong pairing correlations. The pCCD method exhibits a different failure mode, significantly overbinding at intermediate and strong coupling and thereby violating the variational principle, with particularly pronounced deviations for the separable interaction. In contrast, the VMC–NQS results closely track the exact correlation energies across the entire range of coupling strengths shown, remaining accurate deep into the non-perturbative regime. Taken together, these results demonstrate that occupation-number–based NQS provide a highly accurate and variationally controlled description of pairing Hamiltonians, successfully capturing collective correlations across weak- and strong-coupling regimes where conventional many-body methods fail.

At the same time, this success must be understood within the scope of the models considered. When pairing Hamiltonians are formulated in terms of an underlying single-particle basis, realistic nuclear interactions are strongly nonperturbative. Converged calculations therefore require a large number of single-particle orbitals. Consequently, the dimension of the single-particle basis typically satisfies $P \gg A$ , where $A$ is the number of nucleons. In state-of-the-art no-core shell-model calculations [8], $P$ can reach several thousand. This, in turn, leads to neural-network representations of prohibitive size. As a result, the applicability of occupation-number–based NQS approaches to fully realistic nuclear Hamiltonians remains limited at present, motivating the exploration of complementary representations and hybrid strategies.

# 5. Connections to condensed matter physics

The development of neural quantum states (NQS) has been deeply influenced by challenges and innovations in condensed matter physics, where strongly correlated quantum many-body systems demand accurate and scalable computational approaches. Many of the foundational ideas behind NQS, including pioneering work using restricted Boltzmann machines [43], emerged from efforts to model lattice spin systems. These were subsequently extended to continuous-space systems such as the homogeneous electron gas [114] and ultracold Fermi gases [54]. Such advances offer a natural conceptual bridge to nuclear systems, which pose many of the same computational challenges. As a general-purpose variational ansatz, NQS provides greater flexibility than traditional techniques and holds promise for systems governed by complex interactions and symmetry constraints. We now review two condensed matter NQS applications which are closely tied to nuclear approaches. These approaches employ a continuous formulation and tackle either low dimensionality or extended, strongly-correlated systems.

# 5.1. Polarized fermions

One-dimensional fermionic systems offer a particularly useful and conceptually rich setting for studying quantum manybody physics, combining analytical insight with computational accessibility. Due to their reduced dimensionality, such systems admit simplified theoretical descriptions and, in some cases, exact or highly controlled solutions [177, 224], while still exhibiting nontrivial correlation effects that challenge mean-field approaches. From a computational standpoint, onedimensional models provide a natural proving ground for new variational methods, as they allow detailed benchmarking against established many-body techniques at modest numerical cost. In addition, one-dimensional fermions display distinctive phenomena, such as Fermi–Bose dualities and enhanced interaction effects, that have no direct analogue in higher dimensions and are of intrinsic theoretical interest [225–227]. These features make one-dimensional fermionic systems an attractive platform for exploratory studies of neural-network quantum states, serving as a stepping stone toward more realistic three-dimensional and spinful systems of relevance to nuclear and condensed-matter physics [47, 48, 50, 228].

This strategy has been adopted in several early applications of neural-network quantum states to continuous-space fermionic systems [229, 230]. In particular, Ref. [229] investigated fully polarized, or equivalently spinless, fermions confined to one dimension. In this setting, the absence of internal spin degrees of freedom allows the fermionic antisymmetry to be enforced entirely through the spatial structure of the wave function, making it a natural test case for NQS architectures without explicit spin inputs. To ensure nontrivial interactions in the polarized system, finite-range pairwise forces must be employed, since zero-range interactions do not contribute to the energy of identical fermions in one dimension [229].

The system considered in Ref. [229] consists of $A$ fermions in a harmonic trap interacting through a finite-range Gaussian potential, described by the Hamiltonian

$$
\hat {H} = - \frac {1}{2} \sum_ {i = 1} ^ {A} \nabla_ {i} ^ {2} + \frac {1}{2} \sum_ {i = 1} ^ {A} x _ {i} ^ {2} + \frac {V _ {0}}{\sqrt {2 \pi} \sigma_ {0}} \sum_ {i <   j} \exp \left[ - \frac {(x _ {i} - x _ {j}) ^ {2}}{2 \sigma_ {0} ^ {2}} \right]. \tag {5.1}
$$

Here, $V _ { 0 }$ and $\sigma _ { 0 }$ denote the interaction strength and range, respectively. The Hamiltonian is expressed in harmonicoscillator units corresponding to a trap frequency $\omega$ , such that lengths are measured in units of $a _ { \mathrm { h o } } ~ = ~ \sqrt { \hbar / m \omega }$ and energies in units of $\hbar \omega$ .

![](images/e5f2daf9cc360fe11785db5cffc55d84e3b87060b59ef4e4cf95cbc74bd68a74.jpg)  
Figure 5.1: Ground-state energies for few-body systems as a function of the interaction strength $V _ { \mathrm { 0 } }$ at fixed range $\sigma _ { 0 } = 0 . 5$ . Panels (a)–(c) show the total energy $E$ for systems with $A = 2 , 4$ , and 6, while panels (d)–(f) show the corresponding correlation energies $E / - E _ { \mathrm { H F } }$ . Neural-network quantum state (NQS) results are shown as solid blue lines. The real-space solution for $A = 2$ is indicated by filled circles. Configurationinteraction (CI) results are shown as red dashed lines, and the Hartree–Fock (HF) approximation as purple dash-dotted lines, following Ref. [229].

The NQS employed for this system was inspired by the FermiNet architecture [45]. In one dimension, the many-body wave function depends only on the particle coordinates $\Psi ( x _ { 1 } , \dots , x _ { A } )$ . The neural ansatz takes as input the set of particle positions and augments them with a permutation-equivariant feature, the mean position $\textstyle \mu = { \frac { 1 } { A } } \sum _ { i = 1 } ^ { A } x _ { i }$ . These features are propagated through two equivariant hidden layers with element-wise tanh nonlinearities, followed by a linear layer that constructs a symmetric generalized Slater matrix. The determinant of this matrix yields the full antisymmetric many-body wave function [229, 231]. For particle numbers in the range $A = 2$ –6, this architecture contains approximately 8,500–9,000 variational parameters, with only mild scaling as $A$ increases.

In Fig. 5.1, NQS results are compared with configuration interaction (CI), Hartree–Fock (HF), and real-space solutions (Space), where available, for a fixed width $\sigma _ { 0 } = 0 . 5$ . For all particle numbers $A = 2 , 4$ , and 6, the NQS yields energies below the HF results, with the discrepancy increasing as the interaction becomes either strongly attractive or strongly repulsive. This architecture only incorporates a single generalised Slater determinant, so the difference between the HF and NQS results can directly be linked to backflow correlations included by construction through the equivariant features.

While the NQS performs consistently across all interaction regimes and reproduces the exact results for $A = 2$ , the fixeddimension CI calculations exhibit noticeable basis-truncation effects as the interaction strength increases, particularly in the attractive regime. This behavior can be traced to the emergence of short-range structure in the wave function under strong attraction. Resolving accurately these structure requires progressively larger single-particle bases.

The density distributions of one-dimensional systems directly pinpoint the effect of complex many-body correlations. We show in Fig. 5.2 the density distributions across a wide range of strengths, from very attractive (left panels) to

![](images/4f4e176b09b3848456be436d060b606a2963f338efb2278066001b39f1895dbb.jpg)  
Figure 5.2: Density profiles $n ( x )$ for one-dimensional spinless trapped fermions as a function of position $_ x$ for different values of $V _ { \mathrm { 0 } }$ at fixed range $\sigma _ { 0 } = 0 . 5$ . From left to right, $V _ { \mathrm { 0 } }$ varies from $- 2 0$ to 20 in increments of 10. From top to bottom, results are shown for $A = 3 , 4 , 5$ , and 6 particles. Figure sourced from Ref. [229].

very repulsive (right panels). The repulsive regime can be easily understood in terms of Wigner crystallization [229]. In contrast, the density distribution in the strongly attractive regime displays a distinct bell shape that is reminiscent of bosonic systems. An associated pairing-like effect in the occupation numbers of the system further points towards the emergence of bosonic features in the many-body wavefunction [229]. CI approaches have a difficulty capturing such results. These features, however, can be understood in terms of a duality between strongly attractive fermions and weakly interacting bosons in 1D systems [225–227]. Overall, these results demonstrate that relatively compact, permutation-equivariant NQS architectures can capture strong-correlation effects in continuous-space fermionic systems. The one-dimensional exactly solvable case thus provides a clean benchmark and a foundation for extensions to higherdimensional and spinful systems.

# 5.2. The homogeneous electron gas

The three-dimensional homogeneous electron gas (HEG) has long served as a prototypical model for studying strongly correlated fermions with long-range Coulomb interactions. Despite its apparent simplicity, with electrons interacting via the Coulomb potential in a uniform, neutralizing background, the HEG exhibits rich many-body behavior. At low densities, where Coulomb repulsion dominates over kinetic energy, the system is expected to undergo Wigner crystallization into a body-centered cubic (BCC) lattice. Due to translational invariance, this crystal may appear as a “floating” phase, characterized by crystalline order in correlations rather than in the density itself.

The HEG has been investigated with a variety of NQS architectures in recent years, including LiNet [232], FermiNet [233], and WAPNet [234], as well as with conventional many-body methods such as diffusion Monte Carlo [235, 236] and coupled cluster approaches [237]. Rather than surveying these applications exhaustively, we focus here on the ap-

proach of Ref. [114], for which the HEG served as the primary development and validation platform for the permutationequivariant message-passing neural network (MPNN) architecture that appears throughout this review. The insights gained in this setting subsequently informed applications to other continuous-space fermionic systems, including ultracold Fermi gases [54], nuclear matter [55], and finite nuclei [52, 238].

To resolve the emergence of the floating Wigner crystal, NQS must scale to large particle numbers while accurately capturing subtle many-body correlations. This requirement directly motivated the development of a permutation-equivariant MPNN architecture augmented with an attention mechanism [114], which encodes how the state of a single electron is influenced by the instantaneous positions and spins of all other electrons. This approach enabled simulations of the HEG with up to 128 electrons, pushing far beyond the system sizes accessible in previous NQS studies [232], and made it possible to detect Wigner-like order in the structure factor at low densities (see Fig. 5.3).

In this HEG application, the construction of the MPNN begins by representing each electron as a node in a fully connected graph, with edges encoding the pairwise relationships between electrons. The goal of the MPNN is to produce spatial displacements $\delta \mathbf { r } _ { i } ( \mathbf { X } )$ for each particle $i = 1 , \ldots , N$ , thereby incorporating backflow correlations into the singleparticle orbitals of a neural Slater determinant. During each message-passing iteration, both the original one- and two-body features from the simulation and a set of auxiliary hidden one- and two-body vectors are propagated and updated, enabling the network to progressively refine its representation of correlations. Specifically, the visible two-body features for the HEG are taken to be

$$
\mathbf {v} _ {i j} = \left[ \mathbf {r} _ {i j}, \left\| \mathbf {r} _ {i j} \right\|, s _ {i} ^ {z} \cdot s _ {j} ^ {z} \right], \tag {5.2}
$$

where the pair displacements $\mathbf { r } _ { i j } = \mathbf { r } _ { i } - \mathbf { r } _ { j }$ and distances $\| \mathbf { r } _ { i j } \|$ are mapped to their $L$ -periodic versions:

$$
\mathbf {r} _ {i j} \mapsto \left[ \sin \left(\frac {2 \pi}{L} \mathbf {r} _ {i j}\right), \cos \left(\frac {2 \pi}{L} \mathbf {r} _ {i j}\right) \right], \quad \| \mathbf {r} _ {i j} \| \mapsto \left\| \sin \left(\frac {\pi}{L} \mathbf {r} _ {i j}\right) \right\|. \tag {5.3}
$$

The initial one-body features, on the other hand, are taken as a trainable embedding vector that is independent of the particle index,

$$
\mathbf {v} _ {i} = \mathbf {e}. \tag {5.4}
$$

Note that this choice of initial one-body features excludes dependence on absolute positions $\mathbf { r } _ { i }$ to ensure translational invariance.

Beyond the initial one- and two-body features and their processing into visible features, the main difference between this MPNN and the one in Section 3.4.5 is the use of an attention mechanism [112] in the message construction. Originally developed for natural language processing, attention mechanisms learn to assign weights to different inputs, enabling the model to focus on the most relevant information when updating each particle’s features (see Section 3.3 for more details). Unlike Eq. (3.47), where a feedforward neural network is applied directly to the pairwise features to produce the message, Ref. [114] first computes an attention score

$$
\boldsymbol {\omega} _ {i j} ^ {(t)} = \operatorname {G E L U} \left(\sum_ {k = 1} ^ {N} \mathbf {Q} _ {i k} ^ {(t)} \mathbf {K} _ {k j} ^ {(t)}\right), \tag {5.5}
$$

which modulates the signal element-wise based on similarities between the query tensor $\mathbf { Q } _ { i j } ^ { ( t ) } = W _ { Q } \mathbf { g } _ { i j } ^ { ( t ) }$ and the key tensor K(t) $\mathbf { K } _ { i j } ^ { ( t ) } = W _ { K } \mathbf { g } _ { i j } ^ { ( t ) }$ = WK g(t)ij . Note that the weight matrices used to produce the query and key are the same for each pair to ensure permutation equivariance. The message is then constructed as

$$
\mathbf {m} _ {i j} ^ {(t)} = \boldsymbol {\omega} _ {i j} ^ {(t)} \odot f _ {V} ^ {(t)} \left(\mathbf {h} _ {i j} ^ {(t - 1)}\right), \tag {5.6}
$$

![](images/ea45eb40d60c8b3e3aadaecc376f070b917d0ab44424d9a111f8239258351a4c.jpg)

![](images/88c8bf9e890ad034cd4951ea968553cb032665868c557fda8ac1648584712e3e.jpg)  
Figure 5.3: Spin-averaged radial distribution function (top panel) and the corresponding structure factor (bottom panel) for the homogeneous electron gas with $N = 1 2 8$ electrons, evaluated at $r _ { s } = 5 0 , 1 1 0$ , and 200. A permutation-equivariant message-passing neural network with an attention mechanism [114] was used to construct backflow correlations within a Slater–Jastrow NQS. Plane-wave orbitals were used at $r _ { s } = 5 0$ , while Gaussian orbitals centered on body-centered cubic (BCC) lattice sites were employed at $r _ { s } = 1 1 0$ and 200.

where $f _ { V } ^ { ( t ) }$ serves as the value network, providing the information to be passed through a nonlinear transformation, and $\odot$ denotes element-wise multiplication rather than the usual dot product. This construction provides flexibility in defining the message content while simultaneously weighting its relevance.

The MPNN approach achieves ground-state energies for the HEG that are on par with or better than those obtained with state-of-the-art NQS, such as FermiNet [233] and WAPNet [234], as well as fixed-node and backflow diffusion Monte Carlo methods [235, 236]. For small systems, it reaches chemical accuracy relative to exact methods, while for larger systems it outperforms comparable variational and diffusion Monte Carlo approaches, particularly at high densities. The method systematically improves with additional message-passing iterations and maintains accuracy across different densities and polarizations. Most notably, the MPNN uses orders of magnitude fewer parameters ( $\sim$ 19,000) than other NQS, and can simulate continuous-space systems with up to 128 electrons, more than double the size previously accessible.

The method also reproduces the expected liquid-to-Wigner-crystal phase transition around $r _ { s } = 1 0 0$ , in agreement with previous studies [239–241]. Gaussian orbitals were found to more easily capture the crystalline phase for large $r _ { s }$ compared to plane-wave orbitals, as shown in Fig. 5.3. The prominent peak in the structure factor that appears

![](images/860a1ca54e98f037d2168d949378c6c67db5ff456dd68cdb8c1f51cdf96e3442.jpg)

![](images/a87988f97c245cc9612a93fae88aeeaa1febbcd16113004cc0d209bd872cd19a.jpg)  
Figure 5.4: Ground-state energy per particle of the UFG, normalized by the noninteracting Fermi gas energy in the thermodynamic limit, $E _ { F G }$ , as a function of message-passing depth $T$ (left panel) and particle number $N$ (right panel). Details of the models, interaction parameters, and uncertainty estimates are discussed in the main text.

between $r _ { s } = 5 0$ and $r _ { s } = 1 1 0$ indicates the emergence of a crystalline state from a fluid state. These results demonstrate that MPNN-based NQS can efficiently and accurately model both delocalized and localized phases in extended systems, providing a framework applicable to other systems where backflow correlations play a central role.

# 5.3. Ultra-cold Fermi gases

The unitary Fermi gas (UFG) is a paradigmatic strongly correlated quantum system of two-component fermions interacting via a short-range potential tuned to infinite scattering length and negligible effective range. In this regime, the system exhibits universal behavior, with properties determined solely by the particle density rather than the microscopic details of the interaction. The UFG lies at the crossover between the BCS superfluid and the Bose–Einstein condensate (BEC) limits, and displays strong pairing correlations and superfluidity in the absence of a small expansion parameter. These features make the UFG both a challenging nonperturbative many-body problem and an ideal benchmark for testing wave-function ansätze and many-body methods. Moreover, low-density neutron matter in the inner crust of neutron stars shares similar universal characteristics, making the UFG a useful proxy for studying pairing and superfluidity in astrophysical systems.

In this review, we focus on the work of Ref. [54], which introduces a Pfaffian–Jastrow NQS augmented by neural backflow transformations generated through a permutation-equivariant message-passing architecture [114]. This construction combines a fully trainable Pfaffian pairing structure with many-body backflow effects, enabling the wave function to capture fermionic antisymmetry and strong pairing correlations within a unified framework, without imposing a predefined decomposition into singlet and triplet pairing channels, fixed functional forms for the pairing orbitals, or a prescribed spin ordering. As a result, the ansatz can be naturally extended to nuclear systems with explicit spin- and isospin-exchange interactions and nontrivial coupling to the spatial degrees of freedom. In parallel with Ref. [54], an NQS approach to the unitary Fermi gas based on the FermiNet architecture was developed around the same time [242]. However, its formulation targets systems with fixed internal spin degrees of freedom and can not directly address the explicit spin–isospin exchange structure of nuclear interactions.

![](images/423131b4647be2296058c1df8cca286725d09bc10b534c340f8e65a7c0f92451.jpg)

![](images/f3612a98e3058fac91142cccf48444aeb0d1750ced28d1ec796fb1013ba2c511.jpg)  
Figure 5.5: Ground-state energy per particle of the UFG, normalized by the noninteracting Fermi gas energy in the thermodynamic limit, ${ \mathit { E } } _ { F G }$ , as a function of effective range $k _ { F } r _ { e }$ (left panel) and inverse scattering length $1 / ( a k _ { F } )$ (right panel). Details of the calculations and uncertainty estimates are discussed in the main text.

As discussed in Sections 3.4.4 and 5.2, Ref. [54] employs a Pfaffian–Jastrow NQS combined with a permutationequivariant message-passing neural network. The ground-state energy per particle, normalized by the noninteracting Fermi gas energy in the thermodynamic limit, is shown in Figs. 5.4 and 5.5. For the NQS results, converged energies are obtained by averaging over the final 100 optimization iterations, with shaded bands indicating the corresponding standard deviations. DMC uncertainty bands correspond to standard errors extracted from block-averaged energies.

Figure 5.4 presents an initial comparison of three NQS architectures and two DMC benchmarks as a function of MPNN depth $T$ . The NQS architectures include Slater–Jastrow ansätze with plane-wave orbitals (SJ–PW) and with backflow correlations (SJ–BF), together with the Pfaffian–Jastrow (PJ–BF) ansatz. In the left panel, the interaction parameters are fixed such that $k _ { F } r _ { e } = 0 . 4$ , and DMC reference energies with (DMC–BCS) and without (DMC–PW) pairing are shown for comparison. As the MPNN depth increases, the SJ–PW energies approach the DMC–PW benchmark, indicating that the MPNN captures correlations at a level comparable to DMC with a restricted nodal surface. However, incorporating backflow correlations generated by the MPNN into the single-particle orbitals of the Slater determinant, as in the SJ–BF ansatz, is still insufficient to capture the strong pairing correlations. By contrast, the PJ–BF ansatz, which explicitly encodes these pairing correlations, outperforms DMC–BCS at all message-passing depths shown. The right panel shows the system-size dependence of the energy at fixed effective range $k _ { F } r _ { e } = 0 . 2$ . Since all the MLPs used to construct the PJ–BF ansatz act only on pairs or single particles, the number of variational parameters does not explicitly depend on the particle number. For all particle numbers shown, the Pfaffian–Jastrow ansatz systematically yields lower energies than the DMC–BCS reference, with the difference between the two energies growing as the number of particles increases.

Figure 5.5 shows energies at unitarity as a function of effective range, including extrapolations to zero effective range using quadratic fits, as well as results across the BCS–BEC crossover at fixed $k _ { F } r _ { e } = 0 . 2$ . These results demonstrate that the Pfaffian–Jastrow ansatz is robust across all parameter regions explored, indicating that the Pfaffian pairing structure provides a consistently more accurate variational description of strongly correlated pairing physics for ultracold Fermi gases near the unitary limit.

A central practical outcome of this work is the demonstration that transfer learning can stabilize and accelerate

optimization in regimes characterized by strong, short-range interactions and small effective ranges. Because the ansatz does not encode explicit assumptions about short-distance structure, it remains broadly applicable. By progressively pretraining on softer interactions and smaller systems, a single unified ansatz can be extended to harder regimes and larger particle numbers, enabling a controlled exploration of the BCS–BEC crossover and finite-size effects.

Beyond ground-state energies, the Pfaffian–Jastrow NQS accurately describes observables sensitive to the quality of the variational wave function, including pair distribution functions and pairing gaps. The predicted pairing gaps are closer to experimental values than those obtained from DMC calculations based on BCS trial states, and are consistent within uncertainties with DMC results for substantially larger systems. This highlights the potential of neural-networkbased Pfaffian ansätze for providing a faithful description of both energetic and pairing properties in strongly correlated fermionic systems.

# 6. Conclusions and perspectives

In this review, we report recent progress in the application of neural-network quantum states to nuclear many-body problems. Starting from the pioneering studies of the deuteron [47] and very light nuclei [48], the field has advanced enormously over the past five years. Thanks to algorithmic developments and the increased availability of GPU resources, it is now possible to compute ground-state properties of medium-mass nuclei [52] and infinite nuclear matter, simulating up to 42 particles in periodic boundary conditions [55]. While simulations of these relatively large systems have so far been carried out using “essential” nuclear interactions [61], NQS capable of tackling high-resolution potentials derived within chiral EFT have recently been successfully developed [57, 58]. Notably, these applications are not limited to ground-state properties, but also extend to neutron–nucleus scattering [66].

In addition to extending the reach of conventional continuum QMC methods to medium-mass nuclei, the use of NQS has enabled the study of properties of nuclear systems that are inaccessible to conventional QMC approaches. A notable example is the self-emergence of nuclear clusters in the crust of neutron stars [55], which lowers the energy per particle and increases the proton fraction. Previous continuum QMC studies in this density regime were unable to capture this phenomenon due to the fermion-sign problem and the reliance on variational ansätze that are only suitable for describing the uniform liquid phase. As a second example, the combination of the Lorentz Integral Transform with the VMC– NQS method enables QMC calculations of electroweak response functions [210] in the low-energy regime. This region is particularly challenging for conventional GFMC approaches based on imaginary-time current–current correlators, since the inversion of the corresponding Euclidean responses is an ill-posed problem and, in practice, becomes increasingly unreliable at low energy transfer, even when using Maximum Entropy techniques [207]. Importantly, the low-energy response is of central relevance for neutrino experiments, especially those involving astrophysical neutrinos, such as supernova and diffuse supernova neutrinos [243].

In this review, we have also highlighted the fertile connections with condensed-matter applications. One-dimensional fermionic systems provide an excellent, yet challenging, testing ground for NQS architectures [229] and for the development of new ones, including alternatives to standard MLPs, such as Kolmogorov–Arnold wave functions [230]. In addition, the first calculations of the dilute neutron-matter equation of state using NQS were enabled by the introduction of periodic coordinates as network inputs, an approach originally developed for periodic bosonic systems [244]. These include oneand two-dimensional interacting quantum gases with Gaussian interactions, as well as 4He confined in a one-dimensional geometry. Similarly, the highly expressive MPNN backflow transformation, now commonly employed to describe confined and periodic nuclear systems, was originally proposed in the context of the homogeneous electron gas [114]. Analogously, the Pfaffian–Jastrow ansatz, before being applied to elucidate the onset of nuclear clustering in the neutron-star crust [55], proved to be of critical importance for an accurate description of the unitary Fermi gas [54].

While not explicitly discussed in this review, recent advances in NQS applications to the nuclear quantum manybody problem include systematic studies of hypernuclei [238, 245]. In addition to their intrinsic interest, as evidenced by intense experimental campaigns [246], an accurate determination of nucleon–hyperon and nucleon–nucleon–hyperon interactions is of critical importance for the description of matter in the inner core of neutron stars [247]. In particular, a quantitative understanding of the repulsive components of the nucleon–nucleon–hyperon interaction is widely regarded as a key ingredient for resolving the so-called hyperon puzzle, namely the apparent tension between the onset of hyperons in dense matter and the existence of neutron stars with masses of about two solar masses [248].

Based on the rapid progress achieved over the past few years, VMC–NQS approaches are expected to play an increas-

ingly important role in the nuclear many-body community in the coming years. Potential future applications include the combination of NQS with eigenvector continuation techniques [249, 250] to enable systematic studies of nuclear interactions and the reliable quantification of theoretical uncertainties. In this context, foundation models recently developed in condensed-matter physics are also expected to play an important role [251]. Both eigenvector continuation and foundation models offer efficient avenues for exploring families of nuclear Hamiltonians characterized by varying couplings and regulator choices. These approaches are complementary to, and potentially more accurate than, Gaussian-process emulators, which have already been employed in conjunction with NQS to study the sensitivity of hypernuclear ground-state energies to the strength and range of the $\Lambda$ –nucleon–nucleon interaction [238].

Another promising future direction is the calculation of real-time quantum dynamics, which is of critical importance for an ab initio description of scattering, fission, and fusion processes. Compared with time-dependent Hartree–Fock approaches [252], time-dependent variational Monte Carlo (tVMC) [253] fully incorporates dynamical correlations at both short and long distances. Applications of tVMC to NQS in the continuum are still in their infancy, even in condensed-matter systems [254]. Consequently, beyond their direct relevance for the experimental program, employing these techniques to solve the nuclear time-dependent Schrödinger equation would also provide a stringent testbed, as nuclear dynamics requires the simultaneous treatment of discrete bound states and continuum degrees of freedom. Achieving this goal would however widen the reach of this promising ab initio approach to the realm of nuclear dynamics, potentially addressing open questions in fusion, low-energy transfer and, eventually, fission reactions.

# Acknowledgments

We acknowledge useful discussions with James Keeble, Mehdi Drissi, and Javier Rozalén-Sarmiento.   
The present research is supported by the U.S. Department of Energy, Office of Science, Office of Nuclear Physics, under contracts DE-AC02-06CH11357 (A. L., B. F.) and DE-FG02-93ER40756 (J. K.), by the DOE Early Career Research Program (A. L., B. F., J. K.), by the Fermi Research Alliance, LLC under Contract No. DE-AC02-07CH11359 with the U.S. Department of Energy, Office of Science, Office of High Energy Physics (N. R.), by the SciDAC-5 NeuCol and NUCLEI programs (A. L., N. R.). (A. L., N. R.) also acknowledge financial support by grant PID2023-147458NB-C21 funded by MCIN/AEI/10.13039/501100011033 and by the European Union.   
A. R. acknowledges financial support from MCIN/AEI/10.13039/501100011033 through grants PID2021-127890NB-I00,; PID2023-147112NB-C22; CNS2022-135529 funded by the “European Union NextGenerationEU/PRTR”, and CEX2024- 001451-M to the “Unit of Excellence María de Maeztu 2025-2031” award to the Institute of Cosmos Sciences; and by the Generalitat de Catalunya, through grant 2021SGR01095.   
M. H. J. has partly been partially supported by the U.S. Department of Energy through grant DE-SC0026198 and the U.S. National Science Foundation through grant PHY-2310020.

# References

[1] S. Weinberg, Nuclear forces from chiral Lagrangians, Phys. Lett. B251 (1990) 288–292. doi:10.1016/ 0370-2693(90)90938-3.   
[2] S. Weinberg, Effective chiral Lagrangians for nucleon - pion interactions and nuclear forces, Nucl. Phys. B363 (1991) 3–18. doi:10.1016/0550-3213(91)90231-L.   
[3] E. Epelbaum, H.-W. Hammer, U.-G. Meissner, Modern Theory of Nuclear Forces, Rev. Mod. Phys. 81 (2009) 1773–1825. doi:10.1103/RevModPhys.81.1773.   
[4] R. Machleidt, D. Entem, Chiral effective field theory and nuclear forces, Phys. Rept. 503 (2011) 1–75. doi: 10.1016/j.physrep.2011.02.001.   
[5] U. van Kolck, Few nucleon forces from chiral Lagrangians, Phys. Rev. C 49 (1994) 2932–2941. doi:10.1103/ PhysRevC.49.2932.   
[6] H. Hergert, A Guided Tour of ab initio Nuclear Many-Body Theory, Front. in Phys. 8 (2020) 379. doi:10.3389/ fphy.2020.00379.   
[7] A. Ekström, C. Forssén, G. Hagen, G. R. Jansen, W. Jiang, T. Papenbrock, What is ab initio in nuclear theory?, Frontiers in Physics 11 (2023) 125. doi:10.3389/FPHY.2023.1129094. URL https://www.frontiersin.org/articles/10.3389/fphy.2023.1129094/full   
[8] B. R. Barrett, P. Navratil, J. P. Vary, Ab initio no core shell model, Prog. Part. Nucl. Phys. 69 (2013) 131–181. doi:10.1016/j.ppnp.2012.10.003.   
[9] G. Hagen, T. Papenbrock, M. Hjorth-Jensen, D. J. Dean, Coupled-cluster computations of atomic nuclei, Rept. Prog. Phys. 77 (9) (2014) 096302. doi:10.1088/0034-4885/77/9/096302.

[10] H. Hergert, S. Bogner, T. Morris, A. Schwenk, K. Tsukiyama, The In-Medium Similarity Renormalization Group: A Novel Ab Initio Method for Nuclei, Phys. Rept. 621 (2016) 165–222. doi:10.1016/j.physrep.2015.12.007.   
[11] A. Carbone, A. Cipollone, C. Barbieri, A. Rios, A. Polls, Self-consistent Green’s functions formalism with threebody interactions, Physical Review C: Nuclear Physics 88 (5) (2013) 054326, arXiv: 1310.3688 [nucl-th]. doi: 10.1103/PhysRevC.88.054326.   
[12] P. Navratil, S. Quaglioni, I. Stetcu, B. R. Barrett, Recent developments in no-core shell-model calculations, J. Phys. G 36 (2009) 083101, _eprint: 0904.0463. doi:10.1088/0954-3899/36/8/083101.   
[13] S. Quaglioni, P. Navratil, Ab Initio Many-Body Calculations of n-H-3, n-He-4, p-He-3,4,and and n-Be-10 Scattering, Phys. Rev. Lett. 101 (2008) 092501, _eprint: 0804.1560. doi:10.1103/PhysRevLett.101.092501.   
[14] R. Roth, J. Langhammer, A. Calci, S. Binder, P. Navratil, Similarity-Transformed Chiral NN+3N Interactions for the Ab Initio Description of 12-C and 16-O, Phys. Rev. Lett. 107 (2011) 072501, _eprint: 1105.3173. doi: 10.1103/PhysRevLett.107.072501.   
[15] A. E. McCoy, M. A. Caprio, T. Dytrych, P. J. Fasano, Emergent Sp(3,R) Dynamical Symmetry in the Nuclear Many-Body System from an Ab Initio Description, Phys. Rev. Lett. 125 (10) (2020) 102505, _eprint: 2008.05522. doi:10.1103/PhysRevLett.125.102505.   
[16] M. A. Caprio, P. J. Fasano, P. Maris, Robust ab initio prediction of nuclear electric quadrupole observables by scaling to the charge radius, Phys. Rev. C 105 (6) (2022) L061302, _eprint: 2206.09307. doi:10.1103/PhysRevC. 105.L061302.   
[17] G. Hagen, G. R. Jansen, T. Papenbrock, Structure of $^ { 7 8 }$ Ni from first principles computations, Phys. Rev. Lett. 117 (17) (2016) 172501. doi:10.1103/PhysRevLett.117.172501.   
[18] T. D. Morris, J. Simonis, S. R. Stroberg, C. Stumpf, G. Hagen, J. D. Holt, G. R. Jansen, T. Papenbrock, R. Roth, A. Schwenk, Structure of the lightest tin isotopes, Phys. Rev. Lett. 120 (15) (2018) 152503. doi: 10.1103/PhysRevLett.120.152503.   
[19] M. Mougeot, others, Mass measurements of 99-101In challenge ab initio nuclear theory of the nuclide $_ \mathrm { 1 0 0 }$ Sn, Nature Phys. 17 (2021) 1099, _eprint: 2109.10673. doi:10.1038/s41567-021-01326-9.   
[20] B. Hu, others, Ab initio predictions link the neutron skin of $^ \mathrm { 2 0 8 }$ Pb to nuclear forces, Nature Phys. 18 (10) (2022) 1196–1200. doi:10.1038/s41567-023-02324-9.   
[21] J. E. Sobczyk, B. Acharya, S. Bacca, G. Hagen, Ab initio computation of the longitudinal response function in $^ { 4 0 }$ Ca, Phys. Rev. Lett. 127 (7) (2021) 072501. doi:10.1103/PhysRevLett.127.072501.   
[22] B. Acharya, J. E. Sobczyk, S. Bacca, G. Hagen, W. Jiang, 16O electroweak response functions from first principles (Oct. 2024).   
[23] F. Bonaiti, S. Bacca, G. Hagen, G. R. Jansen, Electromagnetic observables of open-shell nuclei from coupled-cluster theory, Phys. Rev. C 110 (4) (2024) 044306. doi:10.1103/PhysRevC.110.044306.

[24] P. Gysbers, others, Discrepancy between experimental and theoretical $\beta$-decay rates resolved from first principles, Nature Phys. 15 (5) (2019) 428–431. doi:10.1038/s41567-019-0450-7.   
[25] J. M. Yao, B. Bally, J. Engel, R. Wirth, T. R. Rodr\’ıguez, H. Hergert, Ab Initio Treatment of Collective Correlations and the Neutrinoless Double Beta Decay of $^ { 4 8 }$ Ca, Phys. Rev. Lett. 124 (23) (2020) 232501, _eprint: 1908.05424. $-$ doi:10.1103/PhysRevLett.124.232501.   
[26] R. Wirth, J. M. Yao, H. Hergert, Ab Initio Calculation of the Contact Operator Contribution in the Standard Mechanism for Neutrinoless Double Beta Decay, Phys. Rev. Lett. 127 (24) (2021) 242502, _eprint: 2105.05415. doi:10.1103/PhysRevLett.127.242502.   
[27] A. Belley, C. G. Payne, S. R. Stroberg, T. Miyagi, J. D. Holt, Ab Initio Neutrinoless Double-Beta Decay Matrix Elements for $^ { 4 8 }$ Ca , $^ { 7 6 }$ Ge , and $^ { 8 2 }$ Se, Phys. Rev. Lett. 126 (4) (2021) 042502, _eprint: 2008.06588. doi:10.1103/ PhysRevLett.126.042502.   
[28] K. D. Launey, T. Dytrych, J. P. Draayer, Symmetry-guided large-scale shell-model theory, Prog. Part. Nucl. Phys. 89 (2016) 101–136, _eprint: 1612.04298. doi:10.1016/j.ppnp.2016.02.001.   
[29] T. Dytrych, K. D. Launey, J. P. Draayer, D. Rowe, J. Wood, G. Rosensteel, C. Bahri, D. Langr, R. B. Baker, Physics of nuclei: Key role of an emergent symmetry, Phys. Rev. Lett. 124 (4) (2020) 042501, _eprint: 1810.05757. doi:10.1103/PhysRevLett.124.042501.   
[30] D. Lee, Lattice Effective Field Theory Simulations of Nuclei, Annual Review of Nuclear and Particle Science 75 (1) (2025) 109–128. doi:10.1146/annurev-nucl-101918-023343. URL https://www.annualreviews.org/content/journals/10.1146/annurev-nucl-101918-023343   
[31] J. Carlson, S. Gandolfi, F. Pederiva, S. C. Pieper, R. Schiavilla, K. E. Schmidt, R. B. Wiringa, Quantum Monte Carlo methods for nuclear physics, Rev. Mod. Phys. 87 (2015) 1067. doi:10.1103/RevModPhys.87.1067.   
[32] J. E. Lynn, I. Tews, S. Gandolfi, A. Lovato, Quantum Monte Carlo Methods in Nuclear Physics: Recent Advances, Annual Review of Nuclear and Particle Science 69 (Volume 69, 2019) (2019) 279–305. doi:10.1146/ annurev-nucl-101918-023600.   
[33] S. Gandolfi, D. Lonardoni, A. Lovato, M. Piarulli, Atomic Nuclei From Quantum Monte Carlo Calculations With Chiral EFT Interactions, Frontiers in Physics 8 (Apr. 2020). doi:10.3389/fphy.2020.00117.   
[34] S. Elhatisari, others, Wavefunction matching for solving quantum many-body problems, Nature 630 (8015) (2024) 59–63, _eprint: 2210.17488. doi:10.1038/s41586-024-07422-z.   
[35] S. Shen, S. Elhatisari, T. A. Lähde, D. Lee, B.-N. Lu, U.-G. Meißner, Emergent geometry and duality in the carbon nucleus, Nature Commun. 14 (1) (2023) 2777, _eprint: 2202.13596. doi:10.1038/s41467-023-38391-y.   
[36] Z. Ren, S. Elhatisari, T. A. Lähde, D. Lee, U.-G. Meißner, Ab initio study of nuclear clustering in hot dilute nuclear matter, Physics Letters B 850 (2024) 138463, arXiv: 2305.15037 [nucl-th]. doi:10.1016/j.physletb.2024.138463.   
[37] Y.-Z. Ma, Z. Lin, B.-N. Lu, S. Elhatisari, D. Lee, N. Li, U.-G. Meißner, A. W. Steiner, Q. Wang, Structure Factors for Hot Neutron Matter from Ab Initio Lattice Simulations with High-Fidelity Chiral Interactions, Phys. Rev. Lett. 132 (23) (2024) 232502, _eprint: 2306.04500. doi:10.1103/PhysRevLett.132.232502. $-$

[38] A. Sarkar, D. Lee, U.-G. Meißner, Floating Block Method for Quantum Monte Carlo Simulations, Phys. Rev. Lett. 131 (24) (2023) 242503, _eprint: 2306.11439. doi:10.1103/PhysRevLett.131.242503.   
[39] J. Carlson, Alpha particle structure, Phys. Rev. C 38 (1988) 1879–1885. doi:10.1103/PhysRevC.38.1879.   
[40] K. E. Schmidt, S. Fantoni, A quantum Monte Carlo method for nucleon systems, Physics Letters B 446 (1999) 99–103. doi:10.1016/S0370-2693(98)01522-6.   
[41] S. J. Novario, D. Lonardoni, S. Gandolfi, G. Hagen, Trends of Neutron Skins and Radii of Mirror Nuclei from First Principles, Phys. Rev. Lett. 130 (3) (2023) 032501, _eprint: 2111.12775. doi:10.1103/PhysRevLett.130.032501.   
[42] J. D. Martin, S. J. Novario, D. Lonardoni, J. Carlson, S. Gandolfi, I. Tews, Auxiliary field diffusion Monte Carlo calculations of magnetic moments of light nuclei with chiral effective field theory interactions, Phys. Rev. C 108 (3) (2023) L031304, _eprint: 2301.08349. doi:10.1103/PhysRevC.108.L031304.   
[43] G. Carleo, M. Troyer, Solving the quantum many-body problem with artificial neural networks, Science 355 (6325) (2017) 602–606. doi:10.1126/science.aag2302. URL http://science.sciencemag.org/content/355/6325/602   
[44] J. Hermann, Z. Schätzle, F. Noé, Deep-neural-network solution of the electronic Schrödinger equation, Nature Chem. 12 (10) (2020) 891–897. doi:10.1038/s41557-020-0544-y.   
[45] D. Pfau, J. S. Spencer, A. G. D. G. Matthews, W. M. C. Foulkes, Ab initio solution of the many-electron Schrödinger equation with deep neural networks, Phys. Rev. Res. 2 (3) (2020) 033429. doi:10.1103/PhysRevResearch.2. 033429. URL https://link.aps.org/doi/10.1103/PhysRevResearch.2.033429   
[46] R. B. Wiringa, V. G. J. Stoks, R. Schiavilla, An Accurate nucleon-nucleon potential with charge independence breaking, Phys. Rev. C 51 (1995) 38–51. doi:10.1103/PhysRevC.51.38.   
[47] J. W. T. Keeble, A. Rios, Machine learning the deuteron, Phys. Lett. B 809 (2020) 135743. doi:10.1016/j. physletb.2020.135743.   
[48] C. Adams, G. Carleo, A. Lovato, N. Rocco, Variational Monte Carlo Calculations of A\ensuremathłeq4 Nuclei with an Artificial Neural-Network Correlator Ansatz, Phys. Rev. Lett. 127 (2) (2021) 022502. doi:10.1103/ PhysRevLett.127.022502.   
[49] Y. L. Yang, P. W. Zhao, A consistent description of the relativistic effects and three-body interactions in atomic nuclei, Phys. Lett. B 835 (2022) 137587. doi:10.1016/j.physletb.2022.137587.   
[50] A. Lovato, C. Adams, G. Carleo, N. Rocco, Hidden-nucleons neural-network quantum states for the nuclear manybody problem, Phys. Rev. Res. 4 (4) (2022) 043178. doi:10.1103/PhysRevResearch.4.043178.   
[51] Y. Yang, P. Zhao, Deep-neural-network approach to solving the ab initio nuclear structure problem, Physical Review C: Nuclear Physics 107 (3) (2023) 034320, arXiv: 2211.13998 [nucl-th]. doi:10.1103/PhysRevC.107.034320.

[52] A. Gnech, B. Fore, A. J. Tropiano, A. Lovato, Distilling the Essential Elements of Nuclear Binding via Neural-Network Quantum States, Physical Review Letters 133 (14) (2024) 142501. doi:10.1103/PhysRevLett.133. 142501. URL https://link.aps.org/doi/10.1103/PhysRevLett.133.142501   
[53] B. Fore, J. M. Kim, G. Carleo, M. Hjorth-Jensen, A. Lovato, M. Piarulli, Dilute neutron star matter from neural-network quantum states, Physical Review Research 5 (3) (2023) 033062, arXiv: 2212.04436. doi: 10.1103/PhysRevResearch.5.033062.   
[54] J. Kim, G. Pescia, B. Fore, J. Nys, G. Carleo, S. Gandolfi, M. Hjorth-Jensen, A. Lovato, Neural-network quantum states for ultra-cold Fermi gases, Commun. Phys. 7 (1) (2024) 148. doi:10.1038/s42005-024-01613-w.   
[55] B. Fore, J. Kim, M. Hjorth-Jensen, A. Lovato, Investigating the crust of neutron stars with neural-network quantum states (Jul. 2024).   
[56] A. Gezerlis, I. Tews, E. Epelbaum, M. Freunek, S. Gandolfi, K. Hebeler, A. Nogga, A. Schwenk, Local chiral effective field theory interactions and quantum Monte Carlo applications, Phys. Rev. C 90 (5) (2014) 054323, _eprint: 1406.0454. doi:10.1103/PhysRevC.90.054323.   
[57] P. Wen, A. Gezerlis, J. W. Holt, Neural-Network Correlation Functions for Light Nuclei with Chiral Two- and Three-Body Interactions, arXiv:2505.11442 [nucl-th] (May 2025). doi:10.48550/arXiv.2505.11442. URL http://arxiv.org/abs/2505.11442   
[58] Y. Yang, E. Epelbaum, C. Ji, P. Zhao, Zemach radii and nuclear structure effects in hyperfine splitting of Lithium, version Number: 1 (2025). doi:10.48550/ARXIV.2509.01303. URL https://arxiv.org/abs/2509.01303   
[59] J.-W. Chen, G. Rupak, M. J. Savage, Nucleon-nucleon effective field theory without pions, Nucl. Phys. A 653 (1999) 386–412. doi:10.1016/S0375-9474(99)00298-5.   
[60] P. F. Bedaque, U. van Kolck, Effective field theory for few nucleon systems, Ann. Rev. Nucl. Part. Sci. 52 (2002) 339–396. doi:10.1146/annurev.nucl.52.050102.090637.   
[61] R. Schiavilla, L. Girlanda, A. Gnech, A. Kievsky, A. Lovato, L. E. Marcucci, M. Piarulli, M. Viviani, Two- and three-nucleon contact interactions and ground-state energies of light- and medium-mass nuclei, Phys. Rev. C 103 (5) (2021) 054003. doi:10.1103/PhysRevC.103.054003.   
[62] M. Gattobigio, A. Kievsky, M. Viviani, Embedding nuclear physics inside the unitary-limit window, Physical Review C 100 (3) (2019) 034004. doi:10.1103/PhysRevC.100.034004. URL https://link.aps.org/doi/10.1103/PhysRevC.100.034004   
[63] R. B. Wiringa, S. C. Pieper, Evolution of nuclear spectra with nuclear forces, Phys. Rev. Lett. 89 (2002) 182501, _eprint: nucl-th/0207050. doi:10.1103/PhysRevLett.89.182501.   
[64] C.-J. Yang, Do we know how to count powers in pionless and pionful effective field theory?, Eur. Phys. J. A 56 (3) (2020) 96. doi:10.1140/epja/s10050-020-00104-0.

[65] P. F. Bedaque, H. Hammer, U. van Kolck, Renormalization of the three-body system with short range interactions, Phys. Rev. Lett. 82 (1999) 463–467. doi:10.1103/PhysRevLett.82.463.   
[66] Y. Yang, E. Epelbaum, J. Meng, L. Meng, P. Zhao, Chiral Symmetry and Peripheral Neutron- $\alpha$ Scattering, Physical Review Letters 135 (17) (2025) 172502. doi:10.1103/45g7-bmp6. URL https://link.aps.org/doi/10.1103/45g7-bmp6   
[67] A. Gezerlis, I. Tews, E. Epelbaum, S. Gandolfi, K. Hebeler, A. Nogga, A. Schwenk, Quantum Monte Carlo Calculations with Chiral Effective Field Theory Interactions, Phys. Rev. Lett. 111 (3) (2013) 032501, _eprint: 1303.6243. doi:10.1103/PhysRevLett.111.032501.   
[68] J. E. Lynn, I. Tews, J. Carlson, S. Gandolfi, A. Gezerlis, K. E. Schmidt, A. Schwenk, Chiral Three-Nucleon Interactions in Light Nuclei, Neutron-$\alpha$ Scattering, and Neutron Matter, Phys. Rev. Lett. 116 (6) (2016) 062501, _eprint: 1509.03470. doi:10.1103/PhysRevLett.116.062501.   
[69] B. S. Pudliner, V. R. Pandharipande, J. Carlson, R. B. Wiringa, Quantum Monte Carlo Calculations of A $\leq$ 6 Nuclei, Physical Review Letters 74 (22) (1995) 4396–4399. doi:10.1103/PhysRevLett.74.4396. URL https://link.aps.org/doi/10.1103/PhysRevLett.74.4396   
[70] J.-i. Fujita, H. Miyazawa, Pion Theory of Three-Body Forces, Progress of Theoretical Physics 17 (3) (1957) 360–365. doi:10.1143/PTP.17.360. URL https://academic.oup.com/ptp/article-lookup/doi/10.1143/PTP.17.360   
[71] B. S. Pudliner, V. R. Pandharipande, J. Carlson, S. C. Pieper, R. B. Wiringa, Quantum Monte Carlo calculations of nuclei with A <~ 7, Physical Review C 56 (4) (1997) 1720–1750. doi:10.1103/PhysRevC.56.1720. URL https://link.aps.org/doi/10.1103/PhysRevC.56.1720   
[72] I. Lagaris, V. Pandharipande, Variational calculations of realistic models of nuclear matter, Nuclear Physics A 359 (2) (1981) 349–364. doi:10.1016/0375-9474(81)90241-4. URL https://linkinghub.elsevier.com/retrieve/pii/0375947481902414   
[73] A. Akmal, V. R. Pandharipande, D. G. Ravenhall, The Equation of state of nucleon matter and neutron star structure, Physical Review C: Nuclear Physics 58 (1998) 1804–1828, arXiv: nucl-th/9804027. doi:10.1103/PhysRevC. 58.1804.   
[74] S. C. Pieper, The Illinois Extension to the Fujita-Miyazawa Three-Nucleon Force, AIP Conf. Proc. 1011 (1) (2008) 143–152. doi:10.1063/1.2932280.   
[75] J. E. Lynn, I. Tews, J. Carlson, S. Gandolfi, A. Gezerlis, K. E. Schmidt, A. Schwenk, Quantum Monte Carlo calculations of light nuclei with local chiral two- and three-nucleon interactions, Physical Review C 96 (5) (2017) 054007. doi:10.1103/PhysRevC.96.054007. URL https://link.aps.org/doi/10.1103/PhysRevC.96.054007   
[76] A. Lovato, O. Benhar, S. Fantoni, K. E. Schmidt, Comparative study of three-nucleon potentials in nuclear matter, Physical Review C 85 (2) (2012) 024003. doi:10.1103/PhysRevC.85.024003. URL https://link.aps.org/doi/10.1103/PhysRevC.85.024003

[77] E. Epelbaum, H. Krebs, D. Lee, U.-G. Meissner, Ab initio calculation of the Hoyle state, Phys. Rev. Lett. 106 (2011) 192501. doi:10.1103/PhysRevLett.106.192501.   
[78] J. Carlson, Green’s function Monte Carlo study of light nuclei, Phys. Rev. C 36 (1987) 2026–2033. doi:10.1103/ PhysRevC.36.2026.   
[79] M. Piarulli, others, Light-nuclei spectra from chiral dynamics, Phys. Rev. Lett. 120 (5) (2018) 052503, _eprint: 1707.02883. doi:10.1103/PhysRevLett.120.052503.   
[80] A. Lovato, J. Carlson, S. Gandolfi, N. Rocco, R. Schiavilla, Ab initio study of \boldsymbol(\nu_\ell,\ell^-) and $^ { - }$ \boldsymbol(øverline\nu_\ell,\ell $\hat { \mathbf { \Omega } } + \mathbf { \Omega }$ ) inclusive scattering in $^ { 1 2 }$ C: confronting the MiniBooNE and T2K CCQE $^ { 1 } -$ data, Phys. Rev. X 10 (3) (2020) 031068. doi:10.1103/PhysRevX.10.031068.   
[81] L. Andreoli, G. B. King, S. Pastore, M. Piarulli, J. Carlson, S. Gandolfi, R. B. Wiringa, Quantum Monte Carlo calculations of electron scattering from C 12 in the short-time approximation, Physical Review C 110 (6) (2024) 064004. doi:10.1103/PhysRevC.110.064004. URL https://link.aps.org/doi/10.1103/PhysRevC.110.064004   
[82] G. B. King, A. Baroni, V. Cirigliano, S. Gandolfi, L. Hayen, E. Mereghetti, S. Pastore, M. Piarulli, Ab initio calculation of the \ensuremath\beta-decay spectrum of He6, Phys. Rev. C 107 (1) (2023) 015503, _eprint: 2207.11179. doi:10.1103/PhysRevC.107.015503.   
[83] G. Chambers-Wall, A. Gnech, G. B. King, S. Pastore, M. Piarulli, R. Schiavilla, R. B. Wiringa, Quantum Monte Carlo Calculations of Magnetic Form Factors in Light Nuclei, Phys. Rev. Lett. 133 (21) (2024) 212501, _eprint: 2407.03487. doi:10.1103/PhysRevLett.133.212501.   
[84] S. Gandolfi, A. Y. Illarionov, K. E. Schmidt, F. Pederiva, S. Fantoni, Quantum Monte Carlo calculation of the equation of state of neutron matter, Physical Review C 79 (5) (2009) 054005. doi:10.1103/PhysRevC.79.054005.   
[85] S. C. Pieper, K. Varga, R. B. Wiringa, Quantum Monte Carlo calculations of A = 9 , 10 nuclei, Physical Review C 66 (4) (2002) 044310. doi:10.1103/PhysRevC.66.044310. URL https://link.aps.org/doi/10.1103/PhysRevC.66.044310   
[86] D. Lonardoni, A. Lovato, S. C. Pieper, R. B. Wiringa, Variational calculation of the ground state of closed-shell nuclei up to A=40, Phys. Rev. C 96 (2) (2017) 024326, _eprint: 1705.04337. doi:10.1103/PhysRevC.96.024326.   
[87] J. Lomnitz-Adler, V. Pandharipande, R. Smith, Monte Carlo calculations of triton and 4 He nuclei with the Reid potential, Nucl. Phys. A 361 (1981) 399–411. doi:10.1016/0375-9474(81)90642-4.   
[88] S. Gandolfi, A. Lovato, J. Carlson, K. E. Schmidt, From the lightest nuclei to the equation of state of asymmetric nuclear matter with realistic nuclear interactions, Physical Review C 90 (6) (2014) 061306. doi:10.1103/PhysRevC. 90.061306.   
[89] M. Piarulli, I. Bombaci, D. Logoteta, A. Lovato, R. Wiringa, Benchmark calculations of pure neutron matter with realistic nucleon-nucleon interactions, Phys. Rev. C 101 (4) (2020) 045801. doi:10.1103/PhysRevC.101.045801.

[90] D. Lonardoni, S. Gandolfi, J. E. Lynn, C. Petrie, J. Carlson, K. E. Schmidt, A. Schwenk, Auxiliary field diffusion Monte Carlo calculations of light and medium-mass nuclei with local chiral interactions, Phys. Rev. C97 (4) (2018) 044318, _eprint: 1802.08932. doi:10.1103/PhysRevC.97.044318.   
[91] K. Choo, A. Mezzacapo, G. Carleo, Fermionic neural-network states for ab-initio electronic structure, Nature Communications 11 (1) (2020) 2368. doi:10.1038/s41467-020-15724-9. URL https://www.nature.com/articles/s41467-020-15724-9   
[92] A. Gnech, C. Adams, N. Brawand, G. Carleo, A. Lovato, N. Rocco, Nuclei with up to A=6 nucleons with artificial neural network wave functions, Few-Body Systems 63 (1) (2021) 7. doi:10.1007/s00601-021-01706-0. URL https://doi.org/10.1007/s00601-021-01706-0   
[93] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, E. Teller, Equation of state calculations by fast computing machines, J. Chem. Phys. 21 (1953) 1087–1092. doi:10.1063/1.1699114.   
[94] W. K. Hastings, Monte Carlo sampling methods using Markov chains and their applications, Biometrika 57 (1) (1970) 97–109. doi:10.1093/biomet/57.1.97. URL https://academic.oup.com/biomet/article/57/1/97/284580   
[95] J. Nocedal, S. J. Wright, Numerical Optimization, Springer Series in Operations Research and Financial Engineering, Springer New York, 2006. doi:10.1007/978-0-387-40065-5. URL http://link.springer.com/10.1007/978-0-387-40065-5   
[96] S.-i. Amari, Information Geometry and Its Applications, Vol. 194 of Applied Mathematical Sciences, Springer Japan, Tokyo, 2016. doi:10.1007/978-4-431-55978-8. URL https://link.springer.com/10.1007/978-4-431-55978-8   
[97] J. Stokes, J. Izaac, N. Killoran, G. Carleo, Quantum Natural Gradient, Quantum 4 (2020) 269, arXiv:1909.02108 [quant-ph]. doi:10.22331/q-2020-05-25-269. URL http://arxiv.org/abs/1909.02108   
[98] S. Sorella, Green Function Monte Carlo with Stochastic Reconfiguration, Physical Review Letters 80 (20) (1998) 4558–4561. doi:10.1103/PhysRevLett.80.4558.   
[99] S. Sorella, Wave function optimization in the variational Monte Carlo method, Phys. Rev. B 71 (24) (2005) 241103. doi:10.1103/PhysRevB.71.241103. URL http://link.aps.org/doi/10.1103/PhysRevB.71.241103   
[100] C.-Y. Park, M. J. Kastoryano, Geometry of learning neural quantum states, Physical Review Research 2 (2) (May 2020). doi:10.1103/physrevresearch.2.023232. URL https://link.aps.org/doi/10.1103/PhysRevResearch.2.023232   
[101] S. Dash, L. Gravina, F. Vicentini, M. Ferrero, A. Georges, Efficiency of neural quantum states in light of the quantum geometric tensor, Communications Physics 8 (1) (Mar. 2025). doi:10.1038/s42005-025-02005-4. URL https://www.nature.com/articles/s42005-025-02005-4

[102] S. Sorella, M. Casula, D. Rocca, Weak binding between two aromatic rings: Feeling the van der Waals attraction by quantum Monte Carlo methods, The Journal of Chemical Physics 127 (1) (2007) 014105. doi:10.1063/1.2746035. URL https://pubs.aip.org/jcp/article/127/1/014105/906474/Weak-binding-between-two-aromatic-rings-Feelin   
[103] E. Neuscamman, C. J. Umrigar, G. K.-L. Chan, Optimizing large parameter sets in variational quantum Monte Carlo, Physical Review B 85 (4) (2012) 045103. doi:10.1103/PhysRevB.85.045103. URL https://link.aps.org/doi/10.1103/PhysRevB.85.045103   
[104] M. Drissi, J. W. T. Keeble, J. Rozalén Sarmiento, A. Rios, Second-order optimization strategies for neural network quantum states, Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 382 (2275) (2024) 20240057. doi:10.1098/rsta.2024.0057. URL https://royalsocietypublishing.org/doi/10.1098/rsta.2024.0057   
[105] A. Chen, M. Heyl, Empowering deep neural quantum states through efficient optimization, Nature Physics 20 (9) (2024) 1476–1481. doi:10.1038/s41567-024-02566-1. URL https://www.nature.com/articles/s41567-024-02566-1   
[106] A. P. Dawid, The geometry of proper scoring rules, Annals of the Institute of Statistical Mathematics 59 (1) (2007) 77–93. doi:10.1007/s10463-006-0099-8. URL http://link.springer.com/10.1007/s10463-006-0099-8   
[107] M. Parry, A. P. Dawid, S. Lauritzen, Proper local scoring rules, The Annals of Statistics 40 (1) (Feb. 2012). doi:10.1214/12-AOS971. URL https://projecteuclid.org/journals/annals-of-statistics/volume-40/issue-1/ Proper-local-scoring-rules/10.1214/12-AOS971.full   
[108] D. P. Kingma, J. Ba, Adam: A Method for Stochastic Optimization, CoRR abs/1412.6980 (2014). URL https://api.semanticscholar.org/CorpusID:6628106   
[109] G. Goldshlager, N. Abrahamsen, L. Lin, A Kaczmarz-inspired approach to accelerate the optimization of neural network wavefunctions, Journal of Computational Physics 516 (2024) 113351. doi:10.1016/j.jcp.2024.113351. URL https://linkinghub.elsevier.com/retrieve/pii/S0021999124005990   
[110] M. Zaheer, S. Kottur, S. Ravanbakhsh, B. Poczos, R. Salakhutdinov, A. Smola, Deep Sets, arXiv e-prints (2017) arXiv:1703.06114.   
[111] F. Fuchs, E. Wagstaff, M. Engelcke, DeepSets: Modeling Permutation Invariance (Feb. 2019). URL https://www.inference.vc/deepsets-modeling-permutation-invariance/   
[112] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, I. Polosukhin, Attention Is All You Need, version Number: 7 (2017). doi:10.48550/ARXIV.1706.03762. URL https://arxiv.org/abs/1706.03762   
[113] I. von Glehn, J. S. Spencer, D. Pfau, A Self-Attention Ansatz for Ab-initio Quantum Chemistry (2022). doi: 10.48550/ARXIV.2211.13672. URL https://arxiv.org/abs/2211.13672

[114] G. Pescia, J. Nys, J. Kim, A. Lovato, G. Carleo, Message-passing neural quantum states for the homogeneous electron gas, Physical Review B 110 (3) (2024) 035108. doi:10.1103/PhysRevB.110.035108. URL https://link.aps.org/doi/10.1103/PhysRevB.110.035108   
[115] M. Geier, K. Nazaryan, T. Zaklama, L. Fu, Self-attention neural network for solving correlated electron problems in solids, Physical Review B 112 (4) (2025) 045119. doi:10.1103/qxc3-bkc7. URL https://link.aps.org/doi/10.1103/qxc3-bkc7   
[116] A. Gnech, M. Viviani, L. E. Marcucci, Calculation of the $^6$Li ground state within the hyperspherical harmonic basis, Phys. Rev. C 102 (1) (2020) 014001. doi:10.1103/PhysRevC.102.014001. URL https://link.aps.org/doi/10.1103/PhysRevC.102.014001   
[117] P. Massella, F. Barranco, D. Lonardoni, A. Lovato, F. Pederiva, E. Vigezzi, Exact restoration of Galilei invariance in density functional calculations with quantum Monte Carlo, J. Phys. G 47 (2020) 035105. doi:10.1088/1361-6471/ ab588c.   
[118] R. Q. Charles, H. Su, M. Kaichun, L. J. Guibas, PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation, in: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), IEEE, Honolulu, HI, 2017, pp. 77–85. doi:10.1109/CVPR.2017.16. URL http://ieeexplore.ieee.org/document/8099499/   
[119] O. Vinyals, M. Fortunato, N. Jaitly, Pointer Networks, version Number: 2 (2015). doi:10.48550/ARXIV.1506. 03134. URL https://arxiv.org/abs/1506.03134   
[120] J. Lee, Y. Lee, J. Kim, A. R. Kosiorek, S. Choi, Y. W. Teh, Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks, version Number: 3 (2018). doi:10.48550/ARXIV.1810.00825. URL https://arxiv.org/abs/1810.00825   
[121] E. Wagstaff, F. B. Fuchs, M. Engelcke, I. Posner, M. Osborne, On the Limitations of Representing Functions on Sets, arXiv e-prints (2019) arXiv:1901.09006.   
[122] C. Dugas, Y. Bengio, F. Bélisle, C. Nadeau, R. Garcia, Incorporating Second-Order Functional Knowledge for Better Option Pricing, in: T. K. Leen, T. G. Dietterich, V. Tresp (Eds.), Advances in Neural Information Processing Systems 13, MIT Press, 2001, pp. 472–478. URL http://papers.nips.cc/paper/1920-incorporating-second-order-functional-knowledge-for-better-optionpdf   
[123] D. Hendrycks, K. Gimpel, Gaussian Error Linear Units (GELUs), arXiv:1606.08415 [cs] (Jun. 2023). doi:10. 48550/arXiv.1606.08415. URL http://arxiv.org/abs/1606.08415   
[124] C. Adams, others, Sensitivity of a tonne-scale NEXT detector for neutrinoless double beta decay searches, JHEP 2021 (08) (2021) 164, _eprint: 2005.06467. doi:10.1007/JHEP08(2021)164.

[125] M. Albergo, G. Kanwar, P. Shanahan, Flow-based generative models for Markov chain Monte Carlo in lattice field theory, Physical Review D 100 (3) (2019) 034515. doi:10.1103/PhysRevD.100.034515. URL https://link.aps.org/doi/10.1103/PhysRevD.100.034515   
[126] J. Brady, P. Wen, J. W. Holt, Normalizing flows for microscopic many-body calculations: an application to the nuclear equation of state, Physical Review Letters 127 (6) (2021) 062701, arXiv:2102.02726 [nucl-th]. doi:10.1103/ PhysRevLett.127.062701. URL http://arxiv.org/abs/2102.02726   
[127] P. Wen, J. W. Holt, A. Blackburn, Application of normalizing flows to nuclear many-body perturbation theory, arXiv:2412.19777 [nucl-th] (Dec. 2024). doi:10.48550/arXiv.2412.19777. URL http://arxiv.org/abs/2412.19777   
[128] J. R. Moreno, G. Carleo, A. Georges, J. Stokes, Fermionic wave functions from neural-network constrained hidden states, Proc. Nat. Acad. Sci. 119 (32) (2022) e2122059119, _eprint: 2111.10420. doi:10.1073/pnas.2122059119.   
[129] A. Bohr, B. R. Mottelson, Nuclear structure, World Scientific, Singapore ; River Edge, NJ, 1998.   
[130] A. Gezerlis, J. Carlson, Strongly paired fermions: Cold atoms and neutron matter, Physical Review C 77 (3) (2008) 032801. doi:10.1103/PhysRevC.77.032801. URL https://link.aps.org/doi/10.1103/PhysRevC.77.032801   
[131] J. Carlson, S.-Y. Chang, V. R. Pandharipande, K. E. Schmidt, Superfluid Fermi Gases with Large Scattering Length, Physical Review Letters 91 (5) (2003) 050401. doi:10.1103/PhysRevLett.91.050401. URL https://link.aps.org/doi/10.1103/PhysRevLett.91.050401   
[132] S. Y. Chang, V. R. Pandharipande, J. Carlson, K. E. Schmidt, Quantum Monte Carlo studies of superfluid Fermi gases, Physical Review A 70 (4) (2004) 043602. doi:10.1103/PhysRevA.70.043602. URL https://link.aps.org/doi/10.1103/PhysRevA.70.043602   
[133] A. Gezerlis, S. Gandolfi, K. E. Schmidt, J. Carlson, Heavy-Light Fermion Mixtures at Unitarity, Physical Review Letters 103 (6) (2009) 060403. doi:10.1103/PhysRevLett.103.060403. URL https://link.aps.org/doi/10.1103/PhysRevLett.103.060403   
[134] M. Casula, S. Sorella, Geminal wave functions with Jastrow correlation: A first application to atoms, The Journal of Chemical Physics 119 (13) (2003) 6500–6511. doi:10.1063/1.1604379. URL https://pubs.aip.org/jcp/article/119/13/6500/534927/Geminal-wave-functions-with-Jastrow-correlation-  
[135] M. Casula, C. Attaccalite, S. Sorella, Correlated geminal wave function for molecules: An efficient resonating valence bond approach, The Journal of Chemical Physics 121 (15) (2004) 7110–7126. doi:10.1063/1.1794632. URL https://pubs.aip.org/jcp/article/121/15/7110/534852/Correlated-geminal-wave-function-for-molecules-  
[136] A. Galea, H. Dawkins, S. Gandolfi, A. Gezerlis, Diffusion Monte Carlo study of strongly interacting two-dimensional Fermi gases, Physical Review A 93 (2) (2016) 023602. doi:10.1103/PhysRevA.93.023602. URL https://link.aps.org/doi/10.1103/PhysRevA.93.023602

[137] M. Bajdich, L. Mitas, L. K. Wagner, K. E. Schmidt, Pfaffian pairing and backflow wavefunctions for electronic structure quantum Monte Carlo methods, Physical Review B 77 (11) (2008) 115112. doi:10.1103/PhysRevB.77. 115112. URL https://link.aps.org/doi/10.1103/PhysRevB.77.115112   
[138] M. Bajdich, L. Mitas, G. Drobný, L. K. Wagner, K. E. Schmidt, Pfaffian Pairing Wave Functions in Electronic-Structure Quantum Monte Carlo Simulations, Physical Review Letters 96 (13) (2006) 130201. doi:10.1103/ PhysRevLett.96.130201. URL https://link.aps.org/doi/10.1103/PhysRevLett.96.130201   
[139] M. Piarulli, I. Tews, Local Nucleon-Nucleon and Three-Nucleon Interactions Within Chiral Effective Field Theory, Frontiers in Physics 7 (2020) 245. doi:10.3389/fphy.2019.00245. URL https://www.frontiersin.org/article/10.3389/fphy.2019.00245/full   
[140] S. Gandolfi, A. Y. Illarionov, F. Pederiva, K. E. Schmidt, S. Fantoni, Equation of state of low-density neutron matter, and the 1S0 pairing gap, Physical Review C - Nuclear Physics 80 (4) (2009) 045802. doi:10.1103/PHYSREVC.80. 045802/FIGURES/6/MEDIUM. URL https://journals.aps.org/prc/abstract/10.1103/PhysRevC.80.045802   
[141] N. Gao, S. Günnemann, Neural Pfaffians: Solving Many Many-Electron Schrödinger Equations, version Number: 3 (2024). doi:10.48550/ARXIV.2405.14762. URL https://arxiv.org/abs/2405.14762   
[142] D. J. Dean, M. Hjorth-Jensen, Pairing in nuclear systems: from neutron stars to finite nuclei, Reviews of Modern Physics 75 (2) (2003) 607–656. doi:10.1103/RevModPhys.75.607. URL https://link.aps.org/doi/10.1103/RevModPhys.75.607   
[143] R. P. Feynman, M. Cohen, Energy Spectrum of the Excitations in Liquid Helium, Physical Review 102 (5) (1956) 1189–1204. doi:10.1103/PhysRev.102.1189. URL https://link.aps.org/doi/10.1103/PhysRev.102.1189   
[144] D. Luo, B. K. Clark, Backflow Transformations via Neural Networks for Quantum Many-Body Wave Functions, Physical Review Letters 122 (22) (2019) 226401. doi:10.1103/PhysRevLett.122.226401. URL https://link.aps.org/doi/10.1103/PhysRevLett.122.226401   
[145] H. Saito, Solving the Bose–Hubbard Model with Machine Learning, Journal of the Physical Society of Japan 86 (9) (2017) 093001, arXiv: 1707.09723. doi:10.7566/JPSJ.86.093001. URL https://journals.jps.jp/doi/10.7566/JPSJ.86.093001   
[146] H. Saito, Method to Solve Quantum Few-Body Problems with Artificial Neural Networks, Journal of the Physical Society of Japan 87 (7) (2018) 074002. doi:10.7566/JPSJ.87.074002. URL https://doi.org/10.7566/JPSJ.87.074002   
[147] E. Epelbaum, H. Krebs, D. Lee, U.-G. Meissner, Ground state energy of dilute neutron matter at next-to-leading order in lattice chiral effective field theory, The European Physical Journal A: Hadrons and Nuclei 40 (2009) 199–213, arXiv: 0812.3653 [nucl-th]. doi:10.1140/epja/i2009-10755-0.

[148] D. R. Entem, R. Machleidt, Accurate charge-dependent nucleon-nucleon potential at fourth order of chiral perturbation theory, Physical Review C 68 (4) (2003) 041001. doi:10.1103/PhysRevC.68.041001. URL http://link.aps.org/doi/10.1103/PhysRevC.68.041001   
[149] J. Rozalén Sarmiento, J. W. T. Keeble, A. Rios, Machine learning the deuteron: new architectures and uncertainty quantification, The European Physical Journal Plus 139 (2) (2024) 189. doi:10.1140/epjp/s13360-024-04983-w. URL https://link.springer.com/10.1140/epjp/s13360-024-04983-w   
[150] G. Hinton, T. Tieleman, Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude (2012). URL https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf   
[151] J. Kirscher, N. Barnea, D. Gazit, F. Pederiva, U. van Kolck, Spectra and Scattering of Light Lattice Nuclei from Effective Field Theory, Phys. Rev. C 92 (5) (2015) 054002. doi:10.1103/PhysRevC.92.054002.   
[152] L. Contessi, A. Lovato, F. Pederiva, A. Roggero, J. Kirscher, U. van Kolck, Ground-state properties of $^4$He and $^{16}$O extrapolated from lattice QCD with pionless EFT, Phys. Lett. B 772 (2017) 839–848. doi:10.1016/j. physletb.2017.07.048.   
[153] H. De Vries, C. De Jager, C. De Vries, Nuclear charge-density-distribution parameters from elastic electron scattering, Atomic Data and Nuclear Data Tables 36 (3) (1987) 495–536. doi:10.1016/0092-640X(87)90013-1. URL https://linkinghub.elsevier.com/retrieve/pii/0092640X87900131   
[154] I. Angeli, K. Marinova, Table of experimental nuclear ground state charge radii: An update, Atomic Data and Nuclear Data Tables 99 (1) (2013) 69–95. doi:10.1016/j.adt.2011.12.006. URL https://linkinghub.elsevier.com/retrieve/pii/S0092640X12000265   
[155] M. Sharaf, R. McCarty, R. A. Basili, J. P. Vary, Comparing Sinc and Harmonic Oscillator Basis for Bound States of a Gaussian Interaction (Dec. 2019).   
[156] A. Kievsky, S. Rosati, M. Viviani, L. E. Marcucci, L. Girlanda, A high-precision variational approach to threeand four-nucleon bound and zero-energy scattering states, J. Phys. G: Nucl. Part. Phys. 35 (6) (2008) 063101. doi:10.1088/0954-3899/35/6/063101.   
[157] J. Beringer, others, Review of Particle Physics (RPP), Phys. Rev. D 86 (2012) 010001. doi:10.1103/PhysRevD. 86.010001.   
[158] J. L. Friar, J. Martorell, D. W. L. Sprung, Nuclear sizes and the isotope shift, Phys. Rev. A 56 (1997) 4579–4586. doi:10.1103/PhysRevA.56.4579.   
[159] National Nuclear Data Center, NuDat Nuclear Structure and Decay Data. URL https://www.nndc.bnl.gov/nudat/   
[160] E. Tiesinga, P. J. Mohr, D. B. Newell, B. N. Taylor, CODATA recommended values of the fundamental physical constants: 2018, Reviews of Modern Physics 93 (2) (2021) 025010. doi:10.1103/RevModPhys.93.025010. URL https://link.aps.org/doi/10.1103/RevModPhys.93.025010

[161] A. Amroun, V. Breton, J.-M. Cavedon, B. Frois, D. Goutte, F. P. Juster, P. Leconte, J. Martino, Y. Mizuno, X.-H. Phan, S. K. Platchkov, I. Sick, S. Williamson, 3H and 3He electromagnetic form factors, Nuclear Physics A 579 (3) (1994) 596–626. doi:https://doi.org/10.1016/0375-9474(94)90925-3. URL https://www.sciencedirect.com/science/article/pii/0375947494909253   
[162] D. C. Morton, Q. Wu, G. W. F. Drake, Nuclear charge radius for ^3\mathrmHe, Phys. Rev. A 73 (3) (2006) 034502. doi:10.1103/PhysRevA.73.034502. URL https://link.aps.org/doi/10.1103/PhysRevA.73.034502   
[163] J. Krauth, K. Schuhmann, M. Ahmed, ıt et al., Measuring the $\alpha$-particle charge radius with muonic helium-4 ions, Nature 598 (2021) 527–531. doi:10.1038/s41586-021-03183-1.   
[164] L.-B. Wang, P. Mueller, K. Bailey, G. W. F. Drake, J. P. Greene, D. Henderson, R. J. Holt, R. V. F. Janssens, C. L. Jiang, Z.-T. Lu, T. P. O’Connor, R. C. Pardo, K. E. Rehm, J. P. Schiffer, X. D. Tang, Laser Spectroscopic Determination of the ^6\mathrmH\mathrme Nuclear Charge Radius, Phys. Rev. Lett. 93 (14) (2004) 142501. doi:10.1103/PhysRevLett.93.142501. URL https://link.aps.org/doi/10.1103/PhysRevLett.93.142501   
[165] M. Puchalski, K. Pachucki, Ground State Hyperfine Splitting in ^6,7\mathrmLi Atoms and the Nuclear Structure, Phys. Rev. Lett. 111 (24) (2013) 243001. doi:10.1103/PhysRevLett.111.243001. URL https://link.aps.org/doi/10.1103/PhysRevLett.111.243001   
[166] A. Sabatucci, O. Benhar, A. Lovato, Relativistic corrections to the correlated basis function effective nuclear Hamiltonian, Phys. Rev. C 110 (5) (2024) 055801, _eprint: 2406.05732. doi:10.1103/PhysRevC.110.055801.   
[167] F. Coester, S. C. Pieper, F. J. D. Serduke, Relativistic effects in phenomenological nucleon-nucleon potentials and nuclear matter, Physical Review C 11 (1) (1975) 1–18. doi:10.1103/PhysRevC.11.1. URL https://link.aps.org/doi/10.1103/PhysRevC.11.1   
[168] R. Brockmann, R. Machleidt, Relativistic nuclear structure. I. Nuclear matter, Physical Review C 42 (5) (1990) 1965–1980. doi:10.1103/PhysRevC.42.1965. URL https://link.aps.org/doi/10.1103/PhysRevC.42.1965   
[169] W. Glöckle, T.-S. H. Lee, F. Coester, Relativistic effects in three-body bound states, Physical Review C 33 (2) (1986) 709–716. doi:10.1103/PhysRevC.33.709. URL https://link.aps.org/doi/10.1103/PhysRevC.33.709   
[170] J. L. Forest, V. R. Pandharipande, A. Arriaga, Quantum Monte Carlo studies of relativistic effects in light nuclei, Physical Review C 60 (1) (1999) 014002. doi:10.1103/PhysRevC.60.014002. URL https://link.aps.org/doi/10.1103/PhysRevC.60.014002   
[171] P. Maris, E. Epelbaum, R. J. Furnstahl, J. Golak, K. Hebeler, T. Hüther, H. Kamada, H. Krebs, U.-G. Meißner, J. A. Melendez, A. Nogga, P. Reinert, R. Roth, R. Skibiński, V. Soloviov, K. Topolnicki, J. P. Vary, Y. Volkotrub, H. Witała, T. Wolfgruber, LENPIC Collaboration, Light nuclei with semilocal momentum-space regularized chiral interactions up to third order, Physical Review C 103 (5) (2021) 054001. doi:10.1103/PhysRevC.103.054001. URL https://link.aps.org/doi/10.1103/PhysRevC.103.054001

[172] S. Pastore, S. C. Pieper, R. Schiavilla, R. B. Wiringa, Quantum Monte Carlo calculations of electromagnetic moments and transitions in A $\leq$ 9 nuclei with meson-exchange currents derived from chiral effective field theory, Physical Review C 87 (3) (2013) 035503. doi:10.1103/PhysRevC.87.035503. URL https://link.aps.org/doi/10.1103/PhysRevC.87.035503   
[173] A. Gnech, R. Schiavilla, Magnetic structure of few-nucleon systems at high momentum transfers in a chiral effective field theory approach, Physical Review C 106 (4) (2022) 044001. doi:10.1103/PhysRevC.106.044001. URL https://link.aps.org/doi/10.1103/PhysRevC.106.044001   
[174] C. Wang, T. Naito, J. Li, H. Liang, A neural network approach for two-body systems with spin and isospin degrees of freedom, arXiv:2403.16819 [nucl-th] (Mar. 2024). doi:10.48550/arXiv.2403.16819. URL http://arxiv.org/abs/2403.16819   
[175] R. Li, X. Luo, H. Sun, P. G. Ortega, Solving two and three-body systems with deep neural networks, arXiv:2507.17559 [hep-ph] (Jul. 2025). doi:10.48550/arXiv.2507.17559. URL http://arxiv.org/abs/2507.17559   
[176] J. E. Lynn, J. Carlson, E. Epelbaum, S. Gandolfi, A. Gezerlis, A. Schwenk, Quantum Monte Carlo Calculations of Light Nuclei Using Chiral Potentials, Phys. Rev. Lett. 113 (19) (2014) 192501, _eprint: 1406.2787. doi: 10.1103/PhysRevLett.113.192501.   
[177] T. Busch, B.-G. Englert, K. Rzażewski, M. Wilkens, Two Cold Atoms in a Harmonic Trap, Foundations of Physics 28 (4) (1998) 549–559. doi:10.1023/A:1018705520999. URL https://link.springer.com/10.1023/A:1018705520999   
[178] P. Büttiker, U.-G. Meißner, Pion–nucleon scattering inside the Mandelstam triangle, Nuclear Physics A 668 (1-4) (2000) 97–112. doi:10.1016/S0375-9474(99)00813-1. URL https://linkinghub.elsevier.com/retrieve/pii/S0375947499008131   
[179] R. B. Wiringa, S. C. Pieper, J. Carlson, V. R. Pandharipande, Quantum Monte Carlo calculations of A = 8 nuclei, Physical Review C 62 (1) (2000) 014001. doi:10.1103/PhysRevC.62.014001. URL https://link.aps.org/doi/10.1103/PhysRevC.62.014001   
[180] J. Bond, F. Firk, Determination of R-function and physical-state parameters for n-4He elastic scattering below 21 MeV, Nuclear Physics A 287 (2) (1977) 317–343. doi:10.1016/0375-9474(77)90499-7. URL https://linkinghub.elsevier.com/retrieve/pii/0375947477904997   
[181] B. P. Abbott, others, GW170817: Observation of gravitational waves from a binary neutron star inspiral, Physical Review Letters 119 (16) (2017) 161101, arXiv: 1710.05832 [gr-qc] Number: LIGO-P170817 tex.collaboration: LIGO Scientific Collaboration and Virgo Collaboration. doi:10.1103/PhysRevLett.119.161101.   
[182] B. P. Abbott, others, Multi-messenger observations of a binary neutron star merger, Astrophysical Journal 848 (2) (2017) L12, arXiv: 1710.05833 [astro-ph.HE] Number: LIGO-P1700294, VIR-0802A-17, FERMILAB-PUB-17-478- A-AE-CD tex.collaboration: LIGO Scientific Collaboration and Virgo Collaboration. doi:10.3847/2041-8213/ aa91c9.

[183] A. Sabatucci, O. Benhar, Tidal deformation of neutron stars from microscopic models of nuclear dynamics, Physical Review C: Nuclear Physics 101 (4) (2020) 045807, arXiv: 2001.06294 [nucl-th]. doi:10.1103/PhysRevC.101. 045807.   
[184] P. Senger, Probing dense nuclear matter in the laboratory: Experiments at FAIR and NICA, Universe 7 (6), number: 171 (2021). doi:10.3390/universe7060171. URL https://www.mdpi.com/2218-1997/7/6/171   
[185] G. Baym, H. A. Bethe, C. Pethick, Neutron star matter, Nuclear Physics A 175 (1971) 225–271. doi:10.1016/ 0375-9474(71)90281-8.   
[186] G. Baym, C. Pethick, P. Sutherland, The Ground state of matter at high densities: Equation of state and stellar models, Astrophysical Journal 170 (1971) 299–317. doi:10.1086/151216.   
[187] D. G. Ravenhall, C. J. Pethick, J. R. Wilson, Structure of matter below nuclear saturation density, Physical Review Letters 50 (1983) 2066–2069. doi:10.1103/PhysRevLett.50.2066.   
[188] F. Douchin, P. Haensel, A unified equation of state of dense matter and neutron star structure, Astronomy & Astrophysics 380 (1) (2001) 151–167, tex.copyright: $©$ ESO, 2001. doi:10.1051/0004-6361:20011402.   
[189] W. G. Newton, M. Gearheart, B.-A. Li, A survey of the parameter space of the compressible liquid drop model as applied to the neutron star inner crust 204 (2013) 9, arXiv: 1110.4043 [astro-ph.SR]. doi:10.1088/0067-0049/ 204/1/9.   
[190] F. Gulminelli, A. R. Raduta, Unified treatment of subsaturation stellar matter at zero and finite temperature, Physical Review C: Nuclear Physics 92 (5) (2015) 055803, arXiv: 1504.04493 [nucl-th]. doi:10.1103/PhysRevC. 92.055803.   
[191] Y. Lim, J. W. Holt, Structure of neutron star crusts from new Skyrme effective interactions constrained by chiral effective field theory, Physical Review C: Nuclear Physics 95 (6) (2017) 065805, arXiv: 1702.02898 [nucl-th]. doi: 10.1103/PhysRevC.95.065805.   
[192] T. Carreau, F. Gulminelli, J. Margueron, Bayesian analysis of the crust-core transition with a compressible liquiddrop model, The European Physical Journal A: Hadrons and Nuclei 55 (10) (2019) 188, arXiv: 1902.07032 [nucl-th]. doi:10.1140/epja/i2019-12884-1.   
[193] G. Grams, R. Somasundaram, J. Margueron, S. Reddy, Properties of the neutron star crust: Quantifying and correlating uncertainties with improved nuclear physics, Physical Review C: Nuclear Physics 105 (3) (2022) 035806, arXiv: 2110.00441 [nucl-th]. doi:10.1103/PhysRevC.105.035806.   
[194] J. W. Negele, D. Vautherin, Neutron star matter at sub-nuclear densities, Nuclear Physics A 207 (2) (1973) 298–320. doi:10.1016/0375-9474(73)90349-7.   
[195] M. Baldo, E. E. Saperstein, S. V. Tolokonnikov, Role of the boundary conditions in the Wigner-Seitz approximation applied to the neutron star inner crust, Nuclear Physics A 775 (2006) 235–244, arXiv: nucl-th/0605010. doi: 10.1016/j.nuclphysa.2006.07.003.

[196] F. Grill, J. Margueron, N. Sandulescu, The Cluster structure of the inner crust of neutron stars in the Hartree-Fock-Bogoliubov approach, Physical Review C: Nuclear Physics 84 (2011) 065801, arXiv: 1107.4275 [nucl-th]. doi:10.1103/PhysRevC.84.065801.   
[197] D. Lonardoni, I. Tews, S. Gandolfi, J. Carlson, Nuclear and neutron-star matter from local chiral interactions, Phys. Rev. Res. 2 (2020) 022033. doi:10.1103/PhysRevResearch.2.022033.   
[198] A. Lovato, I. Bombaci, D. Logoteta, M. Piarulli, R. B. Wiringa, Benchmark calculations of infinite neutron matter with realistic two- and three-nucleon potentials, Physical Review C: Nuclear Physics 105 (5) (2022) 055808, arXiv: 2202.10293 [nucl-th]. doi:10.1103/PhysRevC.105.055808.   
[199] S. Gandolfi, A. Y. Illarionov, S. Fantoni, F. Pederiva, K. E. Schmidt, Equation of state of superfluid neutron matter and the calculation of S(0)-1 pairing gap, Physical Review Letters 101 (2008) 132501, arXiv: 0805.2513 [nucl-th]. doi:10.1103/PhysRevLett.101.132501.   
[200] S. Gandolfi, G. Palkanoglou, J. Carlson, A. Gezerlis, K. E. Schmidt, The 1S0 pairing gap in neutron matter 7 (1) (2022) 19, arXiv: 2201.01308 [nucl-th] Number: LA-UR-21-31849. doi:10.3390/condmat7010019.   
[201] O. Benhar, G. De Rosi, Superfluid gap in neutron matter from a microscopic effective interaction, Journal of Low Temperature Physics 189 (5-6) (2017) 250–261, arXiv: 1705.06607 [nucl-th]. doi:10.1007/s10909-017-1823-x.   
[202] O. Benhar, Structure and dynamics of compact stars, Lecture notes in physics, Springer International Publishing, 2023. URL https://books.google.com/books?id=aZDvzwEACAAJ   
[203] E. Chabanat, P. Bonche, P. Haensel, J. Meyer, R. Schaeffer, A Skyrme parametrization from subnuclear to neutron star densities Part II. Nuclei far from stabilities, Nuclear Physics A 635 (1) (1998) 231–256. doi: 10.1016/S0375-9474(98)00180-8.   
[204] S. Bacca, S. Pastore, Electromagnetic reactions on light nuclei, J. Phys. G 41 (12) (2014) 123002. doi:10.1088/ 0954-3899/41/12/123002.   
[205] A. Lovato, S. Gandolfi, R. Butler, J. Carlson, E. Lusk, S. C. Pieper, R. Schiavilla, Charge Form Factor and Sum Rules of Electromagnetic Response Functions in ^12C, Phys. Rev. Lett. 111 (9) (2013) 092501. doi:10.1103/ PhysRevLett.111.092501.   
[206] I. C. Cloët, W. Bentz, A. W. Thomas, Relativistic and Nuclear Medium Effects on the Coulomb Sum Rule, Phys. Rev. Lett. 116 (3) (2016) 032701. doi:10.1103/PhysRevLett.116.032701.   
[207] A. Lovato, S. Gandolfi, J. Carlson, S. C. Pieper, R. Schiavilla, Electromagnetic response of $_ { 1 2 }$ C: A first-principles calculation, Phys. Rev. Lett. 117 (8) (2016) 082501. doi:10.1103/PhysRevLett.117.082501.   
[208] J. Carlson, R. Schiavilla, Euclidean proton response in light nuclei, Phys. Rev. Lett. 68 (1992) 3682–3685. doi: 10.1103/PhysRevLett.68.3682.   
[209] V. D. Efros, W. Leidemann, G. Orlandini, N. Barnea, The Lorentz Integral Transform (LIT) method and its applications to perturbation induced reactions, J. Phys. G 34 (2007) R459–2456. doi:10.1088/0954-3899/34/12/ R02.

[210] E. Parnes, N. Barnea, G. Carleo, A. Lovato, N. Rocco, X. Zhang, Nuclear Responses with Neural-Network Quantum States, Physical Review Letters 136 (3) (2026) 032501. doi:10.1103/tlqz-nw28. URL https://link.aps.org/doi/10.1103/tlqz-nw28   
[211] A. Sinibaldi, C. Giuliani, G. Carleo, F. Vicentini, Unbiasing time-dependent Variational Monte Carlo by projected quantum evolution, Quantum 7 (2023) 1131. doi:10.22331/q-2023-10-10-1131.   
[212] D. Hendry, A. E. Feiguin, Machine learning approach to dynamical properties of quantum many-body systems, Phys. Rev. B 100 (24) (2019) 245123. doi:10.1103/PhysRevB.100.245123. URL https://link.aps.org/doi/10.1103/PhysRevB.100.245123   
[213] M. Jarrell, J. E. Gubernatis, Bayesian inference and the analytic continuation of imaginary-time quantum Monte Carlo data, Phys. Rept. 269 (1996) 133–195. doi:10.1016/0370-1573(95)00074-7.   
[214] A. L. Fetter, J. D. Walecka, Quantum Theory of Many-Particle Systems, Dover Books on Physics, Dover Publications, Newburyport, 2012.   
[215] A. Bohr, B. R. Mottelson, D. Pines, Possible Analogy between the Excitation Spectra of Nuclei and Those of the Superconducting Metallic State, Physical Review 110 (4) (1958) 936–938. doi:10.1103/PhysRev.110.936. URL https://link.aps.org/doi/10.1103/PhysRev.110.936   
[216] P. Ring, P. Schuck, The nuclear many body problem, 1st Edition, Texts and monographs in physics, Springer, Berlin Heidelberg, 1980.   
[217] J. Dobaczewski, W. Nazarewicz, P.-G. Reinhard, Pairing interaction and self-consistent densities in neutron-rich nuclei, Nuclear Physics A 693 (1-2) (2001) 361–373. doi:10.1016/S0375-9474(01)00993-9. URL https://linkinghub.elsevier.com/retrieve/pii/S0375947401009939   
[218] R. Richardson, A restricted class of exact eigenstates of the pairing-force Hamiltonian, Physics Letters 3 (6) (1963) 277–279. doi:10.1016/0031-9163(63)90259-2. URL https://linkinghub.elsevier.com/retrieve/pii/0031916363902592   
[219] R. Richardson, Application to the exact theory of the pairing model to some even isotopes of lead, Physics Letters 5 (1) (1963) 82–84. doi:10.1016/S0375-9601(63)80039-0. URL https://linkinghub.elsevier.com/retrieve/pii/S0375960163800390   
[220] M. Gaudin, Diagonalisation d’une classe d’hamiltoniens de spin, Journal de Physique 37 (10) (1976) 1087–1098. doi:10.1051/jphys:0197600370100108700. URL http://www.edpsciences.org/10.1051/jphys:0197600370100108700   
[221] G. Passetti, D. Hofmann, P. Neitemeier, L. Grunwald, M. A. Sentef, D. M. Kennes, Can Neural Quantum States Learn Volume-Law Ground States?, Physical Review Letters 131 (3) (2023) 036502. doi:10.1103/PhysRevLett. 131.036502. URL https://link.aps.org/doi/10.1103/PhysRevLett.131.036502

[222] Z. Denis, A. Sinibaldi, G. Carleo, Comment on “Can Neural Quantum States Learn Volume-Law Ground States?”, Physical Review Letters 134 (7) (2025) 079701. doi:10.1103/PhysRevLett.134.079701. URL https://link.aps.org/doi/10.1103/PhysRevLett.134.079701   
[223] M. Rigo, B. Hall, M. Hjorth-Jensen, A. Lovato, F. Pederiva, Solving the nuclear pairing model with neural network quantum states, Physical Review E 107 (2) (2023) 025310. doi:10.1103/PhysRevE.107.025310. URL https://link.aps.org/doi/10.1103/PhysRevE.107.025310   
[224] H. Bethe, Zur Theorie der Metalle: I. Eigenwerte und Eigenfunktionen der linearen Atomkette, Zeitschrift für Physik 71 (3-4) (1931) 205–226. doi:10.1007/BF01341708. URL http://link.springer.com/10.1007/BF01341708   
[225] M. Girardeau, Relationship between Systems of Impenetrable Bosons and Fermions in One Dimension, Journal of Mathematical Physics 1 (6) (1960) 516–523. doi:10.1063/1.1703687. URL https://pubs.aip.org/jmp/article/1/6/516/222573/Relationship-between-Systems-of-Impenetrable   
[226] M. Valiente, Bose-Fermi dualities for arbitrary one-dimensional quantum systems in the universal low-energy regime, Physical Review A 102 (5) (2020) 053304. doi:10.1103/PhysRevA.102.053304. URL https://link.aps.org/doi/10.1103/PhysRevA.102.053304   
[227] M. Girardeau, H. Nguyen, M. Olshanii, Effective interactions, Fermi–Bose duality, and ground states of ultracold atomic vapors in tight de Broglie waveguides, Optics Communications 243 (1-6) (2004) 3–22. doi:10.1016/j. optcom.2004.09.079. URL https://linkinghub.elsevier.com/retrieve/pii/S0030401804010582   
[228] A. Gnech, C. Adams, N. Brawand, G. Carleo, A. Lovato, N. Rocco, Nuclei with Up to $$\varvec{A=6}$$ Nucleons with Artificial Neural Network Wave Functions, Few-Body Systems 63 (1) (2022) 7. doi:10.1007/ s00601-021-01706-0. URL https://link.springer.com/10.1007/s00601-021-01706-0   
[229] J. W. T. Keeble, M. Drissi, A. Rojo-Francàs, B. Juliá-Díaz, A. Rios, Machine learning one-dimensional spinless trapped fermionic systems with neural-network quantum states, Physical Review A 108 (6) (2023) 063320. doi: 10.1103/PhysRevA.108.063320. URL https://link.aps.org/doi/10.1103/PhysRevA.108.063320   
[230] P. F. Bedaque, H. Kumar, A. Sheng, A Machine Learning Approach to Trapped Many-Fermion Systems, arXiv:2410.17383 [nucl-th] (Oct. 2024). doi:10.48550/arXiv.2410.17383. URL http://arxiv.org/abs/2410.17383   
[231] J. W. KEEBLE, Neural Network Solutions to the Fermionic Schrödinger Equation (2022). doi: 10.15126/thesis.900505. URL https://openresearch.surrey.ac.uk/esploro/outputs/doctoral/Neural-Network-Solutions-to-the-99688465902346?institution=44SUR_INST

[232] X. Li, Z. Li, J. Chen, Ab initio calculation of real solids via neural network ansatz, Nature Communications 13 (1) (2022) 7895. doi:10.1038/s41467-022-35627-1. URL https://www.nature.com/articles/s41467-022-35627-1   
[233] G. Cassella, H. Sutterud, S. Azadi, N. Drummond, D. Pfau, J. S. Spencer, W. Foulkes, Discovering Quantum Phase Transitions with Fermionic Neural Networks, Physical Review Letters 130 (3) (2023) 036401. doi:10.1103/ PhysRevLett.130.036401. URL https://link.aps.org/doi/10.1103/PhysRevLett.130.036401   
[234] M. Wilson, S. Moroni, M. Holzmann, N. Gao, F. Wudarski, T. Vegge, A. Bhowmik, Neural network ansatz for periodic wave functions and the homogeneous electron gas, Physical Review B 107 (23) (2023) 235139. doi: 10.1103/PhysRevB.107.235139. URL https://link.aps.org/doi/10.1103/PhysRevB.107.235139   
[235] P. López Ríos, A. Ma, N. D. Drummond, M. D. Towler, R. J. Needs, Inhomogeneous backflow transformations in quantum Monte Carlo calculations, Physical Review E 74 (6) (2006) 066701. doi:10.1103/PhysRevE.74.066701. URL https://link.aps.org/doi/10.1103/PhysRevE.74.066701   
[236] S. Azadi, N. D. Drummond, Low-density phase diagram of the three-dimensional electron gas, Physical Review B 105 (24) (2022) 245135. doi:10.1103/PhysRevB.105.245135. URL https://link.aps.org/doi/10.1103/PhysRevB.105.245135   
[237] K. Liao, T. Schraivogel, H. Luo, D. Kats, A. Alavi, Towards efficient and accurate ab initio solutions to periodic systems via transcorrelation and coupled cluster theory, Physical Review Research 3 (3) (2021) 033072. doi: 10.1103/PhysRevResearch.3.033072. URL https://link.aps.org/doi/10.1103/PhysRevResearch.3.033072   
[238] A. D. Donna, L. Contessi, A. Lovato, F. Pederiva, Hypernuclei with Neural Network Quantum States, arXiv:2507.16994 [nucl-th] (Jul. 2025). doi:10.48550/arXiv.2507.16994. URL http://arxiv.org/abs/2507.16994   
[239] S. Azadi, N. D. Drummond, S. M. Vinko, Correlation energy of the paramagnetic electron gas at the thermodynamic limit, Physical Review B 107 (12) (2023) L121105. doi:10.1103/PhysRevB.107.L121105. URL https://link.aps.org/doi/10.1103/PhysRevB.107.L121105   
[240] N. D. Drummond, Z. Radnai, J. R. Trail, M. D. Towler, R. J. Needs, Diffusion quantum Monte Carlo study of three-dimensional Wigner crystals, Physical Review B 69 (8) (2004) 085116. doi:10.1103/PhysRevB.69.085116. URL https://link.aps.org/doi/10.1103/PhysRevB.69.085116   
[241] D. M. Ceperley, B. J. Alder, Ground State of the Electron Gas by a Stochastic Method, Physical Review Letters 45 (7) (1980) 566–569. doi:10.1103/PhysRevLett.45.566. URL https://link.aps.org/doi/10.1103/PhysRevLett.45.566   
[242] W. T. Lou, H. Sutterud, G. Cassella, W. Foulkes, J. Knolle, D. Pfau, J. S. Spencer, Neural Wave Functions for Superfluids, Physical Review X 14 (2) (2024) 021030. doi:10.1103/PhysRevX.14.021030. URL https://link.aps.org/doi/10.1103/PhysRevX.14.021030

[243] K. Scholberg, Supernova Neutrino Detection, Annual Review of Nuclear and Particle Science 62 (1) (2012) 81–103. doi:10.1146/annurev-nucl-102711-095006. URL https://www.annualreviews.org/doi/10.1146/annurev-nucl-102711-095006   
[244] G. Pescia, J. Han, A. Lovato, J. Lu, G. Carleo, Neural-network quantum states for periodic systems in continuous space, Physical Review Research 4 (2) (2022) 023138. doi:10.1103/PhysRevResearch.4.023138. URL https://link.aps.org/doi/10.1103/PhysRevResearch.4.023138   
[245] Z.-X. Zhang, Y.-L. Yang, W.-B. He, P.-W. Zhao, B.-N. Lu, Y.-G. Ma, Machine learning the single-$\Lambda$ hypernuclei with neural-network quantum states, arXiv:2508.03575 [nucl-th] (Aug. 2025). doi:10.48550/arXiv. 2508.03575. URL http://arxiv.org/abs/2508.03575   
[246] O. Hashimoto, H. Tamura, Spectroscopy of $\Lambda$ hypernuclei, Progress in Particle and Nuclear Physics 57 (2) (2006) 564–653. doi:10.1016/j.ppnp.2005.07.001. URL https://linkinghub.elsevier.com/retrieve/pii/S0146641005000761   
[247] D. Lonardoni, A. Lovato, S. Gandolfi, F. Pederiva, Hyperon Puzzle: Hints from Quantum Monte Carlo Calculations, Phys. Rev. Lett. 114 (9) (2015) 092301, _eprint: 1407.4448. doi:10.1103/PhysRevLett.114.092301.   
[248] I. Bombaci, The Hyperon Puzzle in Neutron Stars, in: Proceedings of the 12th International Conference on Hypernuclear and Strange Particle Physics (HYP2015), Journal of the Physical Society of Japan, Sendai, Japan, 2017. doi:10.7566/JPSCP.17.101002. URL http://journals.jps.jp/doi/10.7566/JPSCP.17.101002   
[249] D. Frame, R. He, I. Ipsen, D. Lee, D. Lee, E. Rrapaj, Eigenvector continuation with subspace learning, Phys. Rev. Lett. 121 (3) (2018) 032501, _eprint: 1711.07090. doi:10.1103/PhysRevLett.121.032501.   
[250] T. Duguet, A. Ekström, R. J. Furnstahl, S. König, D. Lee, Colloquium: Eigenvector continuation and projectionbased emulators, Reviews of Modern Physics 96 (3) (2024) 031002. doi:10.1103/RevModPhys.96.031002. URL https://link.aps.org/doi/10.1103/RevModPhys.96.031002   
[251] R. Rende, L. L. Viteritti, F. Becca, A. Scardicchio, A. Laio, G. Carleo, Foundation neural-networks quantum states as a unified Ansatz for multiple hamiltonians, Nature Communications 16 (1) (2025) 7213. doi:10.1038/ s41467-025-62098-x. URL https://www.nature.com/articles/s41467-025-62098-x   
[252] C. Simenel, A. Umar, Heavy-ion collisions and fission dynamics with the time-dependent Hartree–Fock theory and its extensions, Progress in Particle and Nuclear Physics 103 (2018) 19–66. doi:10.1016/j.ppnp.2018.07.002. URL https://linkinghub.elsevier.com/retrieve/pii/S0146641018300693   
[253] G. Carleo, F. Becca, M. Schiró, M. Fabrizio, Localization and Glassy Dynamics Of Many-Body Quantum Systems, Scientific Reports 2 (1) (Feb. 2012). doi:10.1038/srep00243. URL https://doi.org/10.1038%2Fsrep00243

[254] J. Nys, G. Pescia, A. Sinibaldi, G. Carleo, Ab-initio variational wave functions for the time-dependent many-electron Schrödinger equation, Nature Communications 15 (1) (2024) 9404. doi:10.1038/s41467-024-53672-w. URL https://www.nature.com/articles/s41467-024-53672-w