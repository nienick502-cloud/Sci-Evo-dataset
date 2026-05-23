# Wavefunction-Based Emulation of Coupled-Channels Scattering with Non-Affinely Parametrized Interactions

M. Catacora-Rios,1, 2, ∗ K. Beyer,1, 2, † P. Giuliani,1, ‡ K. Godbey,1, 2, § R. J. Furnstahl,3, ¶ and F. M. Nunes1, 2, ∗∗

1Facility for Rare Isotope Beams, Michigan State University, East Lansing, Michigan 48824, USA $^ 2$ Department of Physics and Astronomy, Michigan State University, East Lansing, Michigan 48824, USA $^ 3$ Department of Physics, The Ohio State University, Columbus, Ohio 43210, USA (Dated: December 10, 2025)

Background: Physics based emulators offer a fast and reliable replacement for an exact solution of the scattering problem in nuclear physics. Previous work developed a reduced basis emulator for single-channel scattering using an optical potential to describe elastic scattering.

Purpose: Since many reactions of interest can be cast as a coupled-channel problem, the purpose of this work is to extend the RBM to a coupled-channel framework.

Method: We generalize the reduced basis method to coupled-channel equations (CC-RBM) to describe inelastic scattering. Although our framework is general, in this work we apply it to reactions where the Hamiltonian coupling term comes from assuming a rotational structure model for the target. From a set of training coupledchannel wavefunctions, we perform a singular value decomposition to obtain a reduced set of basis wavefunctions, and then solve the extended (Petrov-)Galerkin equations in that basis. In addition, the empirical interpolation method is used to expand the potentials.

Results: We apply the CC-RBM method to elastic and inelastic scattering of neutrons on $^ { 4 8 }$ Ca including a quadrupole coupling to populate the first $2 ^ { + }$ state, and neutrons on $^ { 2 0 8 }$ Pb, including an octupole coupling to populate its first $3 ^ { - }$ state. We demonstrate that the CC-RBM calculated elastic and inelastic cross sections match those obtained using traditional finite-difference (high-fidelity) methods. We show that the CC-RBM results can reliably reproduce the nuclear scattering cross sections at different energy regimes.

Conclusions: The computational accuracy versus time plots demonstrate that the CC-RBM method efficiently increases precision with increasing basis size. Most importantly, for the precisions required in reaction calculations (a percent on the cross section), we find the CC-RBM method offers roughly one and a half orders of magnitude gain in computational speed compared to the traditional coupled-channels solver. However, we also discuss how this scaling becomes less favorable, the larger the number of channels included in the original coupled-channel set.

# I. INTRODUCTION

Nuclear reactions play a fundamental role in understanding the structure and dynamics of atomic nuclei, as well as in describing the processes that govern nucleosynthesis in the universe. Accurate reaction modeling is also essential for applications ranging from nuclear energy and astrophysics to national security and medical isotope production[1, 2]. In few-body nuclear reactions, one attempts to capture the relevant degrees of freedom arising from the complex many-body interactions [3, 4]. A critical component of few-body reaction theory is the effective interaction between composite particles—the optical potential [5].

The parameters of optical potentials have been shown to be a major source of uncertainty in the theoretical description of reactions [6], and Bayesian studies have sought to quantify, understand, and propagate this para-

metric uncertainty within various few-body models [7– 12]. However, Bayesian analyses require repeatedly solving the Schrödinger equation for many parameter values, a computationally demanding task that has motivated the development of emulators. Emulators based on Reduced Basis Methods (RBMs) [13–15] can quickly approximate the solution to the full scattering problem within a low-dimensional subspace spanned by representative solutions of the Schrödinger equation from a few parameter sets.

The governing equations for this low-dimensional subspace are obtained by projecting the full scattering operators onto the reduced basis through either the Kohn Variational Principle (KVP) [16] or a Petrov–Galerkin projection [13]. Such projections ensure that the emulator reproduces the observables of the original scattering problem with orders-of-magnitude speedups and minimal loss of physical interpretability [15, 17–21].

A class of RBM emulators well adapted for nuclear scattering, the Reduced Order Scattering Emulator (ROSE), was developed and implemented in a userfriendly software in Ref. [22]. This approach employs the Empirical Interpolation Method (EIM) [13, 23, 24] to efficiently perform scattering calculations with realistic potentials that exhibit non-affine parameter dependence, such as the Woods-Saxon interaction often used in phe-

nomenological optical potentials. An additional advantage of ROSE is that it does not appear to suffer from Kohn anomalies [25].

The focus of ROSE was on single-channel scattering, yet the most general few-body reaction problem often results in a set of coupled-channel (CC) equations that need to be solved. The CC framework has been widely used to model nuclear reactions, with applications ranging from elastic (e.g., [26]) and inelastic scattering (e.g., [27]), to more complex probes such as transfer [28], breakup [29] and fusion [30]. Many CC reaction applications involve a large number of channels and significant computation time. Being such an important method in the field of nuclear reactions, it would be extremely useful to develop an efficient and accurate emulator that can replace the full CC calculations, especially for those studies when many reaction calculations are necessary. This work represents the first step in this direction.

In particular, we extend the RBM formalism based on the Galerkin projection used in ROSE to a general CC framework. We apply this framework to neutron–nucleus inelastic scattering using a realistic interaction within a collective model for target excitation. In doing so, we obtain a general, physics-informed CC emulator capable of treating arbitrary interaction forms with non-affine parameter dependencies, providing a unified and efficient tool for emulating complex reaction dynamics.

The remainder of this paper is organized as follows. In Sec. II, we present a general formulation of the CC equations and derive the Petrov–Galerkin equations used to construct the reduced system for this general case, along with the EIM employed to efficiently treat nonaffinely parametrized interaction potentials. Section III outlines an implementation of the emulator and details the generation of the training and testing data sets, using the fresco reaction code [31]. In Section IV we benchmark the emulator against coupled-channel calculations obtained using a high-fidelity method (i.e. solutions obtained using traditional finite-difference methods such as Numerov), analyzing the emulator’s accuracy, computational performance, and stability. Section V summarizes the main findings and discusses possible extensions of this framework. The coupling matrix elements and other CC scattering formulas required to compute the observables for inelastic scattering are provided in Appendix A. Finally, a pedagogical derivation of the RBM equations for a two-level system is presented in Appendix B.

# II. FORMALISM

# A. General coupled-channels formalism

The physical problem under consideration involves quantum mechanical scattering between two composite systems: a projectile and a target, each potentially possessing internal degrees of freedom. The total Hamiltonian can be written as the sum of the internal Hamilto-

nians of the projectile and target and the Hamiltonian describing their relative motion:

$$
H _ {\mathrm {t o t}} = H _ {\mathrm {r e l}} (\boldsymbol {r}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}) + h _ {\mathrm {t}} (\boldsymbol {\xi} _ {t}) + h _ {\mathrm {p}} (\boldsymbol {\xi} _ {p}), \tag {1}
$$

where $\mathbf { \nabla } ^ { \prime }$ denotes the relative coordinate between the two bodies and $\xi _ { t }$ and $\xi _ { p }$ are the internal coordinates of the target and projectile systems. Note that the Hamiltonian of the relative motion can be decomposed as $H _ { \mathrm { r e l } } ( r , \xi _ { t } , \xi _ { p } ) = T _ { r } + V ( r , \xi _ { t } , \xi _ { p } )$ , where $V ( \boldsymbol { r } , \boldsymbol { \xi } _ { t } , \boldsymbol { \xi } _ { p } )$ is the scattering potential between projectile and target. The contribution from the center-of-mass motion has been separated and is not included in the following expressions. The eigenstates of the target and projectile satisfy the following eigenequations:

$$
h _ {t} \left(\boldsymbol {\xi} _ {t}\right) \Phi_ {I _ {\nu}} ^ {t} \left(\boldsymbol {\xi} _ {t}\right) = \epsilon_ {\nu} ^ {t} \Phi_ {I _ {\nu}} ^ {t} \left(\boldsymbol {\xi} _ {t}\right), \tag {2}
$$

$$
h _ {\mathrm {p}} (\pmb {\xi} _ {\pmb {p}}) \Phi_ {s _ {\nu}} ^ {\mathrm {p}} (\pmb {\xi} _ {\pmb {p}}) = \epsilon_ {\nu} ^ {p} \Phi_ {s _ {\nu}} ^ {\mathrm {p}} (\pmb {\xi} _ {\pmb {p}}).
$$

Here, the index $\nu$ labels a specific channel, uniquely specified by the internal states of the target and projectile, $I _ { \nu }$ and $s _ { \nu }$ . Each channel $\nu$ is therefore associated with a channel energy $E _ { \nu } = E - { \epsilon } _ { \nu } ^ { t } - { \epsilon } _ { \nu } ^ { p }$ , where the beam energy $E$ is reduced by the corresponding projectile and target eigenenergies. The total wavefunction of the scattering system can be expanded in a channel basis as:

$$
\Psi_ {\lambda} = \sum_ {\nu = 1} ^ {N _ {c}} | \nu (\hat {\boldsymbol {r}} _ {\boldsymbol {\nu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}) \rangle \frac {1}{r _ {\nu}} \psi_ {\nu , \lambda} (r _ {\nu}). \tag {3}
$$

where the ket $| \nu \rangle$ encodes all the quantum numbers necessary to specify the internal structure of the target and projectile as well as their angular-momentum couplings. The sum over $\nu$ is taken over the maximum number of coupled channel states $N _ { c }$ being considered. As an example, using an $\it { \Delta } l$ –s coupling scheme (coupling of the orbital angular momentum and projectile spin), we could have:

$$
\left| \nu \left(\hat {\boldsymbol {r}} _ {\boldsymbol {\nu}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}\right) \right\rangle = \left[ \left[ i ^ {l} \mathcal {Y} _ {l _ {\nu}} ^ {m _ {\nu}} \left(\hat {\boldsymbol {r}} _ {\boldsymbol {\nu}}\right) \otimes \Phi_ {s _ {\nu}} ^ {p} (\boldsymbol {\xi} _ {p}) \right] _ {j} \otimes \Phi_ {I _ {\nu}} ^ {t} (\boldsymbol {\xi} _ {t}) \right] _ {J M} \tag {4}
$$

where $\mathbf { \mathcal { { y } } } _ { l _ { \nu } } ^ { m _ { \nu } }$ is the spherical harmonic representing the angular motion between the projectile and the target. Furthermore, the indices $\nu$ and $\lambda$ in Eq. (3) indicate the asymptotic boundary conditions satisfied by the radial part of the wavefunction. By convention the second index, $\lambda$ , is typically taken to be the incoming channel such that asymptotically we have:

$$
\psi_ {\nu , \lambda} (r) \xrightarrow [ r \rightarrow \infty ]{} I _ {\lambda} (r) - S _ {\lambda , \nu} O _ {\nu} (r), \tag {5}
$$

where $S$ is the scattering matrix of the coupled-channel system and $I ( O )$ is the incoming (outgoing) free scattering Coulomb function $H ^ { - } ( \eta , k _ { \lambda } r )$ $( H ^ { + } ( \eta , k _ { \nu } r ) )$ , and where $\eta$ is the Sommerfeld parameter and $k _ { \nu }$ is the corresponding channel wavenumber (related to the beam energy $\begin{array} { r } { E _ { \nu } = \frac { \hbar ^ { 2 } k _ { \nu } ^ { 2 } } { 2 \mu _ { p t } } } \end{array}$ 2µpt , with $\mu _ { p t }$ being the reduced mass between

projectile and target). Letting the total Hamiltonian of Eq. (1) act on the total wavefunction defined in Eq. (3) and projecting onto some state $r _ { \mu } \langle \mu ( \hat { r } _ { \nu } , \xi _ { t } , \xi _ { p } ) |$ we obtain the general set of coupled-channel equations for the radial wavefunctions:

$$
\begin{array}{l} \sum_ {\nu = 1} ^ {N _ {c}} r _ {\mu} \left\langle \mu \left(\hat {\boldsymbol {r}} _ {\boldsymbol {\mu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}\right) \mid H _ {\text {t o t}} - E \mid \nu \left(\hat {\boldsymbol {r}} _ {\boldsymbol {\nu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}\right) \right\rangle r _ {\nu} ^ {- 1} \psi_ {\nu , \lambda} \left(r _ {\nu}\right) \tag {6} \\ = \sum_ {\nu = 1} ^ {N _ {c}} N _ {\mu \nu} \left[ T _ {\nu} \left(r _ {\nu}\right) - \left(E - \epsilon_ {\nu}\right) \right] \psi_ {\nu , \lambda} \left(r _ {\nu}\right) + \sum_ {\nu = 1} ^ {N _ {c}} \hat {V} _ {\mu \nu} \psi_ {\nu , \lambda} \left(r _ {\nu}\right). \\ \end{array}
$$

Here, the non-orthogonality terms $N _ { \mu \nu }$ arise if the two coupled-channels change mass partition. In that case, the scattering potential between projectile and target $\hat { V }$ also becomes:

$$
\begin{array}{l} N _ {\mu \nu} = r _ {\mu} \langle \mu (\hat {\boldsymbol {r}} _ {\boldsymbol {\mu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}) | \nu (\hat {\boldsymbol {r}} _ {\boldsymbol {\nu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}) \rangle r _ {\nu} ^ {- 1} \\ \hat {V} _ {\mu \nu} = r _ {\mu} \left\langle \mu \left(\hat {\boldsymbol {r}} _ {\boldsymbol {\mu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}\right) \mid V \left(\boldsymbol {r} _ {\boldsymbol {\nu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}\right) \mid \nu \left(\hat {\boldsymbol {r}} _ {\boldsymbol {\nu}}, \boldsymbol {\xi} _ {\boldsymbol {t}}, \boldsymbol {\xi} _ {\boldsymbol {p}}\right) \right\rangle r _ {\nu} ^ {- 1}. \tag {7} \\ \end{array}
$$

Here and for the remainder of the paper we will consider processes in which the partition does not change, which includes elastic and inelastic scattering, allowing us to set $r _ { \mu } = r _ { \nu }$ . This leads to the simplified set of coupled channel equations:

$$
[ T _ {\mu} (r) - (E - \epsilon_ {\mu}) ] \psi_ {\mu , \lambda} (r) = - \sum_ {\nu = 1} ^ {N _ {c}} V _ {\mu \nu} \psi_ {\nu , \lambda} (r). \qquad (8)
$$

Here the couplings are generated through:

$$
V _ {\mu \nu} = \left\langle \mu \left(\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}\right) \mid V \left(\boldsymbol {r}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}\right)\right) \mid \nu \left(\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}\right) \rangle , \tag {9}
$$

By the symmetries of the system, one can perform a tensor decomposition that separates the coupling potential in a geometric part dependent on $\xi _ { t }$ , $\xi _ { p }$ and $\hat { r }$ , and a scalar function that depends on the relative separation $r$ [32]. In our work, the dependence on any interaction parameters $\pmb { \alpha }$ (e.g. the parameters of a deformed Woods-Saxon), must be included in the radial part. Explicitly, this means that we can write the coupling potential as:

$$
V (\boldsymbol {r}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}; \boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega} (\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {p}) f _ {\omega} (r; \boldsymbol {\alpha}). \tag {10}
$$

The sum in the equation above runs over the number of terms included in the tensor decomposition of the potential up to $N _ { m }$ . Throughout the remainder of this work, we will use a semicolon to distinguish between coordinate arguments and parametric dependencies in the potential functions. The tensor decomposition of the coupling potential could be, for example, a multipole expansion of the deformed potential as is frequently adopted in collective model descriptions of nuclear inelastic scattering, where target excitations are modeled as deformations or vibrational modes [33]. Expanding Eq. (8) using Eq. (10) we get the final form of the coupled-channel equations:

$$
\begin{array}{l} [ T _ {\mu} (r) - (E - \epsilon_ {\mu}) ] \psi_ {\mu , \lambda} (r) \\ = - \sum_ {\nu = 1} ^ {N _ {c}} \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega \mu \nu} f _ {\omega} (r; \boldsymbol {\alpha}) \psi_ {\nu , \lambda} (r), \tag {11} \\ \end{array}
$$

where

$$
\mathcal {V} _ {\omega \mu \nu} = \left\langle \mu (\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {\boldsymbol {p}}) \mid \mathcal {V} _ {\omega} (\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {\boldsymbol {p}}) \mid \nu (\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}, \boldsymbol {\xi} _ {\boldsymbol {p}}) \right\rangle . \tag {12}
$$

The geometric term of the coupling potential, $\mathcal { V } _ { \omega \mu \nu }$ , now acts purely as a scalar coupling strength which depends only on the internal coordinates $\xi _ { t }$ , $\xi _ { p }$ of the two subsystems and the relative angular coordinate $\hat { r }$ . The component index $\nu$ on the right-hand side of Eq. (11), runs over all the allowed couplings between $\nu$ and $\lambda$ , $\nu = 1 , 2 , 3 , . . , N _ { c }$ . The choice of the coupling potential as well as the choice of internal eigenstates $\Phi$ will determine the number of couplings, as can be seen in Eq. (12). In general, there will be a finite set of couplings, for example using the $\ell - s$ coupling scheme shown in Eq. (4), angular momentum rules limit the couplings to states within a given $J$ and a given total parity $\pi$ :

$$
\pi = (- 1) ^ {l} \pi^ {p} \pi^ {t}.
$$

Here $\pi _ { p }$ , and $\pi _ { t }$ are the intrinsic parities of the projectile and the target and $\it l$ is the orbital angular momentum. Therefore, in a general scattering problem, the coupledchannel equations will be solved per total angular momentum number $J$ and total parity.

$$
\begin{array}{l} [ T _ {\mu} (r) - (E - \epsilon_ {\mu}) ] \psi_ {\mu , \lambda} ^ {J ^ {\pi}} (r) \\ = - \sum_ {\nu = 1} ^ {N _ {c}} \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega \mu \nu} ^ {J ^ {\pi}} f _ {\omega} (r; \boldsymbol {\alpha}) \psi_ {\nu , \lambda} ^ {J ^ {\pi}} (r). \tag {13} \\ \end{array}
$$

For notational simplicity, we will omit the superscript $J ^ { \pi }$ , but we emphasize that all the coupled equations in the following sections must be solved for each coupled $J ^ { \pi }$ block unless otherwise stated. We also note that the radial form-factor $f _ { \omega }$ no longer carries any dependence on the quantum numbers of the projectile-target system.

# B. The Reduced Basis Method for coupled channels

# 1. Training space

The Reduced Basis Method (RBM) for neutronnucleus elastic scattering, as developed in the ROSE framework [22], can be extended to the general class of coupled channel equations shown in Eq. (11). We denote $\psi _ { \nu , \lambda } ( r ; \pmb { \alpha } )$ as the radial wavefunction in channel $\nu$ , resulting from an incoming wave in channel $\lambda$ , under an interaction parametrized by $\alpha$ (e.g., Woods-Saxon potential parameters). The key component in constructing

a coupled channels emulator is to identify a suitable lowdimensional subspace onto which high-fidelity solutions for each channel can be accurately projected. Once such a subspace is determined, the full high-fidelity wavefunction $\psi$ can be approximated by $\hat { \psi }$ as follows:

$$
\begin{array}{l} \psi_ {\nu , \lambda} (r; \boldsymbol {\alpha}) \approx \hat {\psi} _ {\nu , \lambda} (r; \boldsymbol {\alpha}) \\ = \phi_ {\nu} (r) \delta_ {\nu \lambda} + \sum_ {k = 1} ^ {N _ {\psi}} c _ {\nu} ^ {(k)} (\boldsymbol {\alpha}) \tilde {\psi} _ {\nu , \lambda} ^ {(k)} (r). \tag {14} \\ \end{array}
$$

Here, the expansion in the reduced basis elements $\ddot { \psi }$ runs up to $N _ { \psi }$ , the number of basis states chosen in the approximation. The first term on the right-hand side, $\phi _ { \nu }$ , represents the free solution—i.e., the solution in the absence of any nuclear interaction. A standard Kronecker delta is used to indicate that this term contributes only when the outgoing channel $\nu$ matches each incoming channel $\lambda$ . We will call the channel for which $\nu = \lambda$ the elastic channel, and those for which $\nu \neq \lambda$ the inelastic channels. The dependence of the expansion coefficients $c _ { \nu } ^ { ( i ) } ( \alpha )$ on the potential parameters $\alpha$ has been made explicit. We note that the expansion of the approximate wavefunction is made component by component, this means that each $\nu = 1 , 2 , . . , N _ { c }$ in a $J _ { \pi }$ coupled block, each incoming channel $\lambda$ will have its own expansion. The chosen basis functions $\tilde { \psi } _ { \nu , \lambda } ^ { ( k ) } ( \boldsymbol { r } )$ , will also be channel dependent, that is: ψ˜(k) $\tilde { \psi } _ { \nu , \lambda } ^ { ( k ) } \neq \tilde { \psi } _ { \mu , \lambda } ^ { ( k ) }$ ̸= for $\mu \neq \nu$ . This channel-dependent choice of wavefunctions ensures that the asymptotic boundary conditions of the emulated wavefunctions are satisfied by construction.

We will now follow a similar procedure to the ROSE framework [22] to get an orthonormal set of basis functions that define a subspace of solutions. We will choose a basis $\{ \tilde { \psi } _ { \nu , \lambda } ^ { ( k ) } ( \boldsymbol { r } ) \}$ by performing a principal component analysis (PCA), also known as proper orthogonal decomposition [13]. The PCA is performed on the space spanned by $N _ { s }$ snapshots, that is, $N _ { s }$ high-fidelity solutions $\{ \psi _ { \nu , \lambda } ( r ; \alpha _ { i } ) \} _ { i = 1 } ^ { N _ { s } }$ to Eq. (11), generated from the set of parameters $\{ \alpha _ { i } \} _ { i = 1 } ^ { N _ { s } }$ . This gives rise to the notion of a training space for the emulator. For those wavefunctions where we have that $\nu = \lambda$ , the snapshots will be modified by subtracting the free solution. Our $N _ { \psi }$ basis functions are then the first $N _ { \psi }$ principal components defined as:

$$
\{\tilde {\psi} _ {\nu , \lambda} ^ {(k)} (r) \} _ {k = 1} ^ {N _ {\psi}} = \operatorname {P C A} \left[ \left\{\psi_ {\nu , \lambda} (r; \boldsymbol {\alpha} _ {\boldsymbol {i}}) - \phi_ {\nu} (r) \delta_ {\nu \lambda} \right\} _ {i = 1} ^ {N _ {s}} \right]. \tag {15}
$$

Naturally we have the requirement that $N _ { s } ~ \ge ~ N _ { \psi }$ . This choice of basis elements can be understood as the $N _ { \psi }$ most relevant directions of variability in the snapshots, and in the channel where $\nu = \lambda$ , the variability is defined with respect to the solution without a nuclear potential. Figure 1 shows the first four PCA vectors obtained for a realistic $^ { 4 8 } \mathrm { C a } ( n , n ^ { \prime } ) ^ { 4 8 } \mathrm { C a } ( 2 ^ { + } )$ at $E _ { \mathrm { l a b } } = 1 2$ MeV calculation.

![](images/48389e93281b53452d6a4b004ace9e4a080786ea74a90dd3b633d9cb30689e16.jpg)  
FIG. 1. Real parts of the first four PCA components for the two coupled channels in the $^ { 4 8 } \mathrm { C a } ( n , n ^ { \prime } ) ^ { 4 8 } \mathrm { C a } ( 2 ^ { + } )$ system at $E _ { \mathrm { l a b } } ~ = ~ 1 2$ MeV and $J ^ { \pi } = 0 ^ { + }$ . Panel (a) shows the $\iota = 0$ , $I _ { t } = 0 ^ { + }$ channel, and panel (b) the $l = 2$ , $I _ { t } = 2 ^ { + }$ channel.

# 2. The Petrov-Galerkin equations

After defining the reduced basis, the next step is to formulate a system of equations to determine the expansion coefficients $c _ { \nu } ^ { ( k ) } ( \alpha )$ in the approximate wavefunction. Several frameworks have been developed to achieve this in the context of scattering (see e.g. [19, 34]). For this work, we adopt the Petrov-Galerkin approach, a generalization of the Galerkin method used in the ROSE framework [22]. In this method the coefficients are found by projecting the radial part of the Hamiltonian acting on the approximatsome functions $\rho _ { \nu , \lambda _ { \bf - } } ^ { ( j ) } ( r )$ ion o, for $j = 1 , 2 , . . , N _ { \psi }$ ace spanned by. As previously stated, each channel component $\nu$ of the wavefunction defined in Eq. (11), must have its own RBM approximation using Eq. (14). We choose the case where $\rho _ { \nu , \lambda } ^ { ( j ) } = ( \tilde { \psi } _ { \nu , \lambda } ^ { ( k ) } ) ^ { * }$ ˜(k) ∗ , where ∗ denotes complex conjugation. Therefore, the before-mentioned projection leads to the following set of coupled equations:

$$
\begin{array}{l} \sum_ {k = 1} ^ {N _ {\psi}} \left[ c _ {\mu} ^ {(k)} \mathcal {D} _ {\mu , \lambda} ^ {(j k)} + \sum_ {\nu = 1} ^ {N _ {c}} c _ {\nu} ^ {(k)} \mathcal {U} _ {\mu \nu , \lambda} ^ {(j k)} (\boldsymbol {\alpha}) \right] \\ + \mathcal {R} _ {\mu , \lambda} ^ {(j)} + \sum_ {\nu = 1} ^ {N _ {c}} \mathcal {C} _ {\mu \nu , \lambda} ^ {(j)} (\boldsymbol {\alpha}) = 0 \tag {16} \\ f o r \mu = 1, 2,.., N _ {c}, \\ \end{array}
$$

where we have defined:

$$
\mathcal {D} _ {\mu , \lambda} ^ {(j k)} = \langle \tilde {\psi} _ {\mu , \lambda} ^ {(j)} | T _ {\mu} (r) - (E - \epsilon_ {\mu}) | \tilde {\psi} _ {\mu , \lambda} ^ {(k)} \rangle ,
$$

$$
\mathcal {U} _ {\mu \nu , \lambda} ^ {(j k)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega \mu \nu} \left\langle \tilde {\psi} _ {\mu , \lambda} ^ {(j)} \mid f _ {\omega} (r; \boldsymbol {\alpha}) \mid \tilde {\psi} _ {\nu , \lambda} ^ {(k)} \right\rangle , \tag {17}
$$

$$
\mathcal {R} _ {\mu , \lambda} ^ {(j)} = \langle \tilde {\psi} _ {\mu , \lambda} ^ {(j)} | T _ {\mu} (r) - (E - \epsilon_ {\mu}) | \phi_ {\mu} \rangle \delta_ {\mu \lambda},
$$

$$
\mathcal {C} _ {\mu \nu , \lambda} ^ {(j)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega \mu \nu} \langle \tilde {\psi} _ {\mu , \lambda} ^ {(j)} | f _ {\omega} (r; \boldsymbol {\alpha}) | \phi_ {\nu} \rangle \delta_ {\nu \lambda}.
$$

Here the bra-ket notation denotes integration over the of ρ(j)ν,λ of ρ $\rho _ { \nu , \lambda } ^ { ( j ) }$ coordinatwe have ⟨ψ˜(j) | $\langle \tilde { \psi } _ { \mu , \lambda } ^ { ( j ) } | = | \tilde { \psi } _ { \mu , \lambda } ^ { ( j ) } \rangle$ $r$ hat with the above choice. These equations can be cast into an algebraic linear system for the desired set of coefficients $\{ c _ { \mu } ^ { ( k ) } \} _ { \mu = 1 } ^ { N _ { c } }$ {cµ , which are obtained by solving Eq. (16) for all the channels in a $J _ { \pi }$ block simultaneously. These equations are worked out in detail, in their matrix form, for a two-level system in Appendix B.

# 3. The Empirical Interpolation method for deformed potentials

When building an emulator, it is useful to conceptualize the computation as occurring in two distinct stages: an offline stage, which consists of calculating and extracing $N _ { s }$ snapshots from the high-fidelity solver, which comprise the training space $\{ \psi _ { \nu , \lambda } \mathrm { \bar { ( } } r ; \alpha _ { i } ) \} _ { i = 1 } ^ { N _ { s } }$ , followed by performing the PCA and then pre-computating of the matrices Eq. (17). This enables the online stage, in which one desires to quickly emulate the solution for a new set of parameters $\pmb { \alpha }$ . This can be done efficiently only if operations in the full, high-dimensional space used by the high-fidelity solver can be avoided, e.g. by pre-computing the matrix elements of the matrices in Eq. (17). This would be straightforward if the parameters $\alpha$ were affine—that is, if the radial part of the potential could be expressed in a separable form:

$$
f _ {\omega} (r, \boldsymbol {\alpha}) = \sum_ {i} g _ {\omega} ^ {(i)} (\boldsymbol {\alpha}) u _ {\omega} ^ {(i)} (r), \tag {18}
$$

where $g _ { \omega } ^ { ( i ) }$ are general functions of the full vector of parameters $\pmb { \alpha }$ and $u _ { \omega } ^ { ( i ) } ( r )$ are the corresponding radial functions. Such an affine form of the potential would allow all integrals in Eq. (17) to be precomputed during the offline stage, so that the online computation reduces to simple weighted sums involving the parameters $\alpha$ . However, most nucleon-nucleus scattering potentials do not allow for such a factorized representation for all parameters. Therefore, we will now use the Empirical Interpolation Method (EIM) [13, 23, 24, 35] to make these calculations affine. To do this, we will approximate each $f _ { \omega } ( r ; \alpha )$ in Eq. (11) as a linear combination of interaction basis functions, weighted by parameter-dependent coefficients:

$$
f _ {\omega} (r; \boldsymbol {\alpha}) \approx \sum_ {i = 1} ^ {N _ {\mathrm {U}}} b _ {\omega} ^ {(i)} (\boldsymbol {\alpha}) u _ {\omega} ^ {(i)} (r), \tag {19}
$$

where $\{ u _ { \omega } ^ { ( i ) } ( r ) \} _ { i = 1 } ^ { N _ { \mathrm { U } } }$ are a reduced basis for the radial interaction functions $f _ { \omega }$ , and $b _ { \omega } ^ { ( i ) } ( \pmb { \alpha } )$ are the corresponding interpolation coefficients encoding the dependence on the interaction parameters $\pmb { \alpha }$ . We obtain these basis functions by sampling the parameter space in a similar manner as for the reduced basis elements. We calculate a set of interactions $\{ f _ { \omega } ( r , \pmb { \alpha } _ { j } ) \} _ { j = 1 } ^ { n _ { U } }$ and then retain the $N _ { U }$ most important components of a PCA analysis (note that we once again require $n _ { U } \ge N _ { U }$ ):

$$
\left\{u _ {\omega} ^ {(i)} (r) \right\} _ {i = 1} ^ {N _ {U}} = \operatorname {P C A} \left[ \left\{f _ {\omega} (r, \boldsymbol {\alpha} _ {j}) \right\} _ {j = 1} ^ {n _ {U}} \right]. \tag {20}
$$

Then the equation that determines the coefficients can be expressed as:

$$
f _ {\omega} \left(r _ {j}, \boldsymbol {\alpha}\right) - \sum_ {i = 1} ^ {N _ {U}} b _ {\omega} ^ {(i)} (\boldsymbol {\alpha}) u _ {\omega} ^ {(i)} \left(r _ {j}\right) = 0 \tag {21}
$$

$$
f o r j = 1, 2,, N _ {U}.
$$

This equation can be understood as interpolating the value of the radial interaction $f _ { \omega } ( r , \alpha )$ at $r _ { j }$ to determine its values at all other points $r$ . The MaxVol algorithm [36] we use to select the radial points $r _ { j }$ is described in the ROSE framework [22], and it consists of maximizing the determinant of a sub-matrix containing snapshots of the interactions over the coordinate grid. This system of equations can then be cast into a linear system involving a $N _ { U } \times N _ { U }$ matrix. Explicitly, we have:

$$
\boldsymbol {b} _ {\omega} (\boldsymbol {\alpha}) = \left(\boldsymbol {U} _ {\omega} ^ {\mathrm {E I M}}\right) ^ {- 1} \cdot \boldsymbol {c} _ {\omega} ^ {\mathrm {E I M}} (\boldsymbol {\alpha}), \tag {22}
$$

with

$$
\boldsymbol {U} _ {\omega} ^ {\mathrm {E I M}} = \left[ \begin{array}{c c c c} u _ {\omega} ^ {(1)} \left(r _ {1}\right) & u _ {\omega} ^ {(2)} \left(r _ {1}\right) & \dots & u _ {\omega} ^ {\left(n _ {U}\right)} \left(r _ {1}\right) \\ u _ {\omega} ^ {(1)} \left(r _ {2}\right) & u _ {\omega} ^ {(2)} \left(r _ {2}\right) & \dots & u _ {\omega} ^ {\left(n _ {U}\right)} \left(r _ {2}\right) \\ \vdots & \vdots & \vdots & \vdots \\ u _ {\omega} ^ {(1)} \left(r _ {N _ {U}}\right) & u _ {\omega} ^ {(2)} \left(r _ {N _ {U}}\right) & \dots & u _ {\omega} ^ {\left(n _ {U}\right)} \left(r _ {N _ {U}}\right) \end{array} \right] _ {N _ {U} \times N _ {U}} \tag {23}
$$

and

$$
\boldsymbol {c} _ {\omega} ^ {\text {E I M}} (\boldsymbol {\alpha}) = \left[ \begin{array}{c} f _ {\omega} \left(r _ {1}, \boldsymbol {\alpha}\right) \\ f _ {\omega} \left(r _ {2}, \boldsymbol {\alpha}\right) \\ \vdots \\ f _ {\omega} \left(r _ {N _ {U}}, \boldsymbol {\alpha}\right) \end{array} \right]. \tag {24}
$$

Since the matrix $U _ { \omega } ^ { \mathrm { E I M } }$ is independent of the potential parameters $\pmb { \alpha }$ one can invert this matrix in the offline stage of the calculation and for each set of new parameters $\alpha$ , simply evaluate the potential at the corresponding locations $r _ { j }$ and multiply as shown in Eq. (22). Therefore, using the EIM we are able to perform all radial integrations in (17) only in the offline stage of the emulator, using the fixed basis states. We can then expand the coupling potential as:

$$
\begin{array}{l} V _ {\mu \nu} (r, \boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega \mu \nu} f _ {\omega} (r; \boldsymbol {\alpha}) \tag {25} \\ \approx \sum_ {\omega = 0} ^ {N _ {m}} \sum_ {i = 1} ^ {N _ {U}} \mathcal {V} _ {\omega \mu \nu} b _ {\omega} ^ {(i)} (\boldsymbol {\alpha}) u _ {\omega} ^ {(i)} (r), \\ \end{array}
$$

where $\nu$ is the geometric coupling matrix element defined in Eq. (12). With this definition we can update Eq. (16):

$$
\mathcal {U} _ {\mu \nu , \lambda} ^ {(j k)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \sum_ {i = 1} ^ {N _ {U}} \mathcal {V} _ {\omega \mu \nu} b _ {\omega} ^ {(i)} (\boldsymbol {\alpha}) \langle \tilde {\psi} _ {\mu , \lambda} ^ {(j)} | u _ {\omega} ^ {(i)} (r) | \tilde {\psi} _ {\nu , \lambda} ^ {(k)} \rangle
$$

$$
\mathcal {C} _ {\mu \nu , \lambda} ^ {(j)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \sum_ {i = 1} ^ {N _ {U}} \mathcal {V} _ {\omega \mu \nu} b _ {\omega} ^ {(i)} (\boldsymbol {\alpha}) \left\langle \tilde {\psi} _ {\mu , \lambda} ^ {(j)} \right| u _ {\omega} ^ {(i)} (r) | \phi_ {\nu} \rangle \delta_ {\nu \lambda}. \tag {26}
$$

Using the EIM the radial integrals of Eq. (16) are now independent of $\pmb { \alpha }$ and so only need to be computed once in the offline stage. The online computational cost of solving the equations for a new set of parameters $\alpha$ now involves two steps:

1. For each $\omega$ , compute the coefficient vector $b _ { \omega } ^ { ( i ) } ( { \pmb \alpha } )$ by multiplying the inverse of the $N _ { U } \times N _ { U }$ matrix $\pmb { c } _ { \omega } ^ { \mathrm { E I M } }$ $( U _ { \omega } ^ { \mathrm { E I M } } ) ^ { - 1 }$ ω , as defined in Eqs. (23) and (24). Then, re- with the evaluated potential vector construct the radial form factor by multiplying the resulting EIM coefficients with the corresponding basis functions as shown in Eq. (25).   
2. Solve the linear system involving the $( N _ { \psi } \cdot N _ { c } ) \times$ $( N _ { \psi } \cdot N _ { c } )$ matrix defined in Eq. (16) for the wavefunction coefficients $c _ { \mu } ^ { ( i ) } ( \pmb { \alpha } )$ .

For a pedagogical implementation of all equations, we refer the reader to Appendix B.

# 4. Emulating Cross Sections

When attempting to get cross sections for a coupledchannel system, it is not sufficient to solve for a single total wavefunction $\Psi _ { \lambda }$ as defined in Eq. (3). Rather, one must solve for all possible $\Psi _ { \lambda }$ allowed per $J _ { \pi }$ with $\lambda = 1 , 2 , . . , N _ { c }$ . Physically, this means that one must solve for the wavefunction corresponding to all possible incoming and outgoing boundary conditions in the coupled $J _ { \pi }$ block, including those for which the target is initially in an excited state, even if our physical problem restricts the target to be in the ground state in the incoming channel [37]. For high-fidelity solvers using a Numerov implementation such as fresco [31], it is often easier to solve for the fundamental matrix of solutions $Y ( r )$ . A second-order differential equation allows for two linearly independent solutions, taking all possible channel combinations yields this $N _ { c } \times N _ { c }$ matrix. From the fundamental matrix of solutions one can then construct any radial solution as a linear combination of its columns:

$$
\psi_ {\mu , \lambda} (r) = \sum_ {\beta = 1} ^ {N _ {c}} Y _ {\mu \beta} (r) c _ {\beta \lambda}. \tag {27}
$$

Numerically, $\mathbf { Y }$ is obtained by imposing linearly independent boundary conditions such as:

$$
Y _ {\mu \beta} \left(r _ {\text {m i n}}\right) = \delta_ {\mu \beta} C \left(l _ {\beta}\right) \tag {28}
$$

Where, $C ( l _ { \beta } )$ is any suitable normalization function dependent of the orbital angular momentum between the projectile and target and $r _ { \mathrm { m i n } }$ is the minimum radius of numerical integration. From the $Y ( r )$ matrix we can then obtain the scattering R-matrix by matching to the asymptotic solutions at some maximum radius $a$ [32]:

$$
\boldsymbol {R} = \boldsymbol {Y} (a) \left[ a \boldsymbol {Y} ^ {\prime} (a) \right] ^ {- 1}. \tag {29}
$$

A simple derivation shows that if $\hat { \Psi } ( r )$ is the full matrix of solutions whose rows $\mu$ and columns $\lambda$ correspond to the radial wavefunctions $\psi _ { \mu , \lambda } ( r )$ , then we also have:

$$
\boldsymbol {R} = \hat {\boldsymbol {\Psi}} (a) [ a \hat {\boldsymbol {\Psi}} ^ {\prime} (a) ] ^ {- 1}. \tag {30}
$$

This means that the Petrov-Galerkin equations defined in Eq. (16) must be solved for each possible $\lambda = 1 , 2 , . . , N _ { c }$ in each $J _ { \pi }$ block independently and with its own basis expansion, leading to $N _ { c }$ solutions per block. This is slightly different from [34] where $\frac { N _ { c } ( N _ { c } + 1 ) } { 2 }$ solutions are required. Once the R-matrix has been obtained we can compute the S-matrix:

$$
\boldsymbol {S} = [ \boldsymbol {O} (a) - a \boldsymbol {R O} ^ {\prime} (a) ] ^ {- 1} [ \boldsymbol {I} (a) - a \boldsymbol {R I} ^ {\prime} (a) ]. \tag {31}
$$

Here $\mathbf { \delta } _ { I ( O ) }$ are matrices whose diagonals are the free incoming(outgoing) Coulomb functions corresponding to each channel $\nu$ in the coupled $J _ { \pi }$ block.

# III. IMPLEMENTATION

The formulation presented in the previous section is general and applies to a broad class of coupled-channel scattering problems, including projectiles with charge and any type of inelastic couplings. As a proof of principle, we implement this formalism for realistic coupledchannel neutron–nucleus inelastic scattering, assuming a collective model for the target structure. In such a case, the interaction is described by a deformed optical potential composed of three Woods–Saxon (WS) terms. In the absence of deformation, the potential takes the form:

$$
\begin{array}{l} U (r; \boldsymbol {\alpha}) = - \left[ V _ {v} f _ {\mathrm {W S}} (r, R _ {v}, a _ {v}) \right. \\ \left. + i W _ {v} f _ {\mathrm {W S}} \left(r, R _ {w}, a _ {w}\right) \right] \\ - i 4 a _ {d} W _ {d} \frac {d}{d r} f _ {\mathrm {W S}} (r, R _ {d}, a _ {d}), \tag {32} \\ \end{array}
$$

where the Woods–Saxon form factor is defined as:

$$
f _ {\mathrm {W S}} (r, R, a) = \left[ 1 + \exp \left(\frac {r - R}{a}\right) \right] ^ {- 1}. \tag {33}
$$

Since we do not expect internal excitations of the incident nucleon at the beam energies considered, we neglect the internal Hamiltonian of the projectile. Furthermore, since the focus of this work is the coupled-channel system

arising from target excitations, we simplify the projectile and neglect its spin. This amounts to not having a spinorbit term in the interaction potential, as can be seen in Eq. (32). A generalization to include the spin-orbit term is straightforward. By neglecting the intrinsic spin of the projectile, the resulting channel states $\nu$ are defined as:

$$
\left| \nu (\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {\boldsymbol {t}}) \right\rangle = \left| \left(l _ {\nu} I _ {\nu} ^ {t}\right) J \right\rangle = \left[ i ^ {l} \mathcal {Y} _ {l _ {\nu}} ^ {m _ {l}} (\hat {\boldsymbol {r}}) \otimes \Phi_ {I _ {\nu}} ^ {t} (\boldsymbol {\xi} _ {\boldsymbol {t}}) \right] _ {J M}. \tag {34}
$$

The nucleus’ deformation is incorporated in this framework (a rigid rotor) by adding an angular dependence (for example in the form of a spherical harmonic function $_ { \mathcal { V } }$ ), relative to the body-fixed frame, to the radial coordinate of the optical potential:

$$
V (\boldsymbol {r}, \boldsymbol {\xi} _ {t}; \boldsymbol {\alpha}) = U (r - \delta_ {\omega} \mathcal {Y} _ {\omega} ^ {0} (\hat {\boldsymbol {r}} ^ {\prime}); \hat {\boldsymbol {\alpha}}). \tag {35}
$$

Here ${ \hat { r } } ^ { \prime }$ is the $\hat { r }$ vector rotated to the body-fixed frame defined by the Euler angles $\xi _ { t }$ . Therefore, our parameters in this model, $\alpha = \{ \delta _ { \omega } , \hat { \alpha } \}$ , consist of one deformation parameter and nine WS parameters,

$$
\boldsymbol {\alpha} = \left\{\delta_ {\omega}, V _ {v}, R _ {v}, a _ {v}, W _ {v}, R _ {w}, a _ {w}, W _ {d}, R _ {d}, a _ {d} \right\}. \tag {36}
$$

Here, $\delta _ { \omega }$ defines the length and multipole order $\omega$ of the deformation. Following the derivation in [33] or [32], a simple expansion for small deformations yields:

$$
V (\boldsymbol {r}, \boldsymbol {\xi} _ {t}; \boldsymbol {\alpha}) = \sqrt {4 \pi} U (r; \hat {\boldsymbol {\alpha}}) \mathcal {Y} _ {0} ^ {0} \left(\hat {\boldsymbol {r}} ^ {\prime}\right) - \delta_ {\omega} U ^ {\prime} (r; \hat {\boldsymbol {\alpha}}) \mathcal {Y} _ {\omega} ^ {0} \left(\hat {\boldsymbol {r}} ^ {\prime}\right). \tag {37}
$$

The first term in the coupling potential yields the diagonal Woods-Saxon terms, the second are the potentials that generate the coupling. In this framework, the sum over $\omega$ in Eq. (11) includes only two terms. We naturally have $f _ { \omega = 0 } ( r ; \pmb { \alpha } ) = U ( r ; \pmb { \alpha } )$ and $f _ { \omega > 0 } ( r ; \pmb { \alpha } ) = \delta _ { \omega } U ^ { \prime } ( r ; \hat { \pmb { \alpha } } )$ .

All details of the coupling matrix elements defined in Eq. (12), applied to this system can be found in Appendix A. In the next two subsections, we will discuss two implementations for two coupling orders $\omega$ of the above formalism. Specifically, the coupling of the $0 ^ { + }$ ground state to a $2 ^ { + }$ or $3 ^ { - }$ excited target state.

The speed gain of the emulator is strongly implementation dependent, but it can be understood as arising from two distinct sources. The first gain comes from restructuring the calculation to avoid redundant work: quantities such as the Petrov–Galerkin integrals (Eq. (16)), coupling matrix elements (Eq. (12)), Coulomb functions (Eq. (31)), and other system-specific terms that do not change across different parameter sets $\pmb { \alpha }$ can be precomputed once in the offline stage and reused. The second gain comes from the reduced dimensionality of the problem: by projecting onto the reduced-basis functions, the emulator replaces the full system with a much smaller linear system (Eq. (16)), which can be solved far more efficiently than using a finite-differences method such as Runge-Kutta or Numerov.

Large speed-ups of more than three orders of magnitude have been reported using dimensionality-reduction

techniques [21]. In neutron–nucleon scattering, the main efficiency gain comes from reducing the basis size: a standard $R$ -matrix approach—commonly used to solve the scattering equations [38]—typically requires $\sim 1 0 ^ { 2 }$ Lagrange–Legendre basis functions [39], whereas their RBM (eigenvector continuation) needs only $\sim 8$ RBM functions. Since the computational cost of a matrix inversion scales as $\mathcal { O } ( N _ { \psi _ { - } } ^ { 3 } )$ , this reduction directly accounts for the dramatic speed-up observed. In our application to low-energy neutron–nucleus scattering, however, we find that a single RBM function corresponds to approximately 2–2.5 Lagrange–Legendre $R$ -matrix functions. As a result, the improvement is more modest, though still significant.

The implementation presented here combines fresco for generating wavefunctions with the JAX library (on CPU) for efficient vectorization of the Petrov–Galerkin equations (Eq. 16). Unlike a conventional Numerov solver, the linear algebra formulation of the equations naturally enables the construction of an emulator that can exploit GPU parallelization. This advantage, however, comes at the cost of additional memory requirements for storing the precomputed quantities discussed in the previous section. For a fair comparison with fresco, we restrict the results shown here to the CPU-based emulator. All calculations—both emulator and fresco—are performed on a laptop. The fresco results correspond to the fastest converged calculation, i.e., the configuration with the coarsest integration grid that yields stable results. To minimize overhead when comparing to fresco, only the minimal standard output was requested in fresco (no wavefunctions or auxiliary quantities were printed). The reported fresco timing therefore includes only the actual computation and standard output plus the time required to load the cross sections into a Python array.

# IV. RESULTS

$$
\mathbf {A}. ^ {4 8} \mathbf {C a} (n, n ^ {\prime}) ^ {4 8} \mathbf {C a} (2 ^ {+}) 4 8 \mathbf {C a} (2 +)
$$

We first consider the case of neutron scattering on $^ { 4 8 }$ Ca with excitation of the $2 ^ { + }$ vibrational state at 3.83 MeV. This is a canonical benchmark for coupled-channel methods, since the $2 ^ { + }$ state is a textbook example of vibrational excitation. In our framework, this corresponds to setting $\omega = 2$ in the deformation expansion of Eq. (37).

We choose two energies, $E _ { \mathrm { l a b } } = 1 2$ MeV and $E _ { \mathrm { l a b } } = 2 6$ MeV, corresponding to different energy regimes and different signatures in the cross-section diffraction pattern. Using fresco, we find that including 15 partial waves is sufficient for these calculations, that is $J _ { \mathrm { m a x } } = 1 5$ . To test the accuracy of the emulator, we select physically relevant parameter values. We adopt the Koning–Delaroche (KD) global parametrization [40] as a reference. For the quadrupole deformation parameter of this system we use $\beta _ { 2 } = 0 . 1 0 7$ [41], from which the deformation length, $\delta _ { 2 }$ ,

![](images/a28399cc795abc67dd5f145d26b0f954f81dc72b35838ea373eada90ec46ea0d.jpg)

![](images/35e85202709b5d2dffe9bb2b2760098e8bbf95e6c660d25fbbba2418401ce674.jpg)  
FIG. 2. Calculated differential cross sections for 48Ca(n, n′)48Ca inelastic scattering at two incident energies. $^ { 4 8 } \mathrm { C a } ( n , n ^ { \prime } ) ^ { 4 8 } \mathrm { C a }$ Panels (a)–(b) show the elastic and inelastic cross sections at $E _ { \mathrm { l a b } } = 1 2 \mathrm { M e V }$ , while panels (c)–(d) show the corresponding results at $E _ { \mathrm { l a b } } = 2 6 \mathrm { M e V }$ . Solid colored lines denote the fresco calculations; dashed black lines denote the emulator results with $N _ { \psi } = 1 2$ and $N _ { U } = 1 2$ . Each curve corresponds to a different choice of interaction parameters $\pmb { \alpha }$ .

can be easily computed. At each incident energy, the KD and previously mentioned $\beta _ { 2 }$ parameters serve as the central values around which the sampling is performed. Training and testing parameter sets are generated using

the latinhypercube() sampling routine from the SciPy library, with parameter ranges extending up to $\pm 2 0 \%$ of their corresponding central value.

We find that at least 200 training snapshots are required to obtain well-converged RBM and EIM basis functions. In this work, 300 snapshots are used for the training of all systems considered, and an additional 50 points are selected for testing. Note that although the samples for the EIM and RBM are drawn from parameter boxes of the same size, they are generated independently. Figure 1 presents the first four principal components obtained from the wavefunction decomposition of the coupled-channel emulator at the two incident energies. The elastic channels ( $l = 0$ , $I = 0 ^ { + }$ ) are shown in panels (a) and (c), while the inelastic channels ( $l = 2$ , $I = 2 ^ { + }$ ) are shown in panels (b) and (d). The corresponding singular values of the RBM basis, consistent with the findings of Ref. [22], indicate that only a small number of components are sufficient to capture the dominant channel dynamics, thereby supporting the dimensionalreduction strategy employed in the emulator.

One favorable feature of the RBM emulator is the ability to tune the trade-off between speed and accuracy by varying the number of EIM ( $N _ { \mathrm { U } }$ ) and RBM ( $N _ { \psi }$ ) basis functions included in the approximation. Figure 2 compares the high-fidelity cross sections produced by fresco with those generated by the emulator using $N _ { \psi } = 1 2$ and $N _ { \mathrm { U } } = 1 2$ . Even though the cross sections span several orders of magnitude with complex angular dependence, the RBM emulator is able to reliably predict both elastic and inelastic observables at different energy regimes.

The resulting trade-off between speed and accuracy is quantified in Fig. 3, which presents the Computational Accuracy vs. Time (CAT) performance of the emulator relative to the high-fidelity fresco solver. In the CAT plot we vary the emulator basis sizes between $N _ { \psi } = 8 - 1 6$ and $N _ { \mathrm { U } } = 1 0 - 1 2$ . The red dashed line corresponds to the average time it takes to run fresco. For $^ { 4 8 } \mathrm { C a } ( n , n ^ { \prime } ) ^ { 4 8 } \mathrm { C a } ( 2 ^ { + } )$ , it corresponds to 60.9 milliseconds. The fresco calculation is run in the same processor as the emulator. Across the 50 test parameter values at $E _ { \mathrm { l a b } } ~ = ~ 1 2$ and 26 MeV, the emulator achieves median relative errors in the cross section well below $1 0 \%$ while reducing the evaluation time by almost two orders of magnitude. Increasing the basis dimensions $N _ { \psi }$ and $N _ { \mathrm { { U } } }$ systematically improves the accuracy while retaining a substantial computational advantage. These results demonstrate that the coupled-channel emulator efficiently and reliably reproduces both elastic and inelastic observables for the $^ { 4 8 }$ Ca system.

$$
\mathbf {B}. ^ {2 0 8} \mathbf {P b} (n, n ^ {\prime}) ^ {2 0 8} \mathbf {P b} \left(3 ^ {-}\right)
$$

As a second case study, we examine neutron scattering on 208Pb, including excitation of the low-lying collective $3 ^ { - }$ state at 2.61 MeV. The $^ \mathrm { 2 0 8 }$ Pb system provides a stringent benchmark for the emulator due to its heavy mass,

![](images/5d3ab1fa3726b649bb7789d4972365768a23b2da3fe8059865268ebb365be05b.jpg)  
FIG. 3. Computational Accuracy vs. Time (CAT) plot illustrating the trade-off between accuracy and computational speed for both the CC emulator and the high-fidelity fresco solver in the calculation of the differential cross section for the elastic (open markers) and inelastic (filled markers) channels of the $^ { 4 8 } \mathrm { C a } ( n , n ^ { \prime } ) ^ { 4 8 } \mathrm { C a } ( 2 ^ { + } )$ reaction at $E _ { \mathrm { l a b } } ~ = ~ 1 2$ MeV [panel (a)] and $E _ { \mathrm { l a b } } ~ = ~ 2 6$ MeV [panel (b)]. The horizontal axis represents the evaluation time per calculation, while the vertical axis shows the accuracy, defined as the median relative error in the differential cross section with respect to the fresco result, computed across 50 test parameter sets centered on the corresponding KD values. For the CC emulator, the number of basis functions in the wavefunction expansion ( $N _ { \psi }$ ) and the EIM representation ( $N _ { \mathrm { { U } } }$ ) were varied between 8 and 16. The vertical red dashed line indicates the average fresco solver evaluation time of 60.9 ms. The emulator achieves relative errors below $1 0 ^ { - 1 }$ while providing speedups approaching one and a half orders of magnitude, depending on the basis size employed.

strong absorption, and the significance of octupole couplings in the low-energy spectrum. In the formalism of Eq. (36), this corresponds to a deformation of multipolarity $\omega = 3$ , with coupling potentials proportional to the derivative of the Woods–Saxon interaction weighted by $Y _ { 3 } ^ { 0 } ( { \hat { r } } ^ { \prime } )$ . Calculations are performed at the same two incident energies, $E _ { \mathrm { l a b } } = 1 2$ and 26 MeV, including partial waves up to $J _ { \mathrm { m a x } } = 1 5$ . As before, the KD parametrization at each energy serves as the reference point for sampling. The octupole deformation parameter, also being sampled, was centered around $\beta _ { 3 } = 0 . 0 3 7 5$ [42].

Figure 4 presents the CAT plots for both energies,

with $E _ { \mathrm { l a b } } = 1 2$ MeV shown in the top panel and $E _ { \mathrm { l a b } } =$ 26 MeV in the bottom panel. As in the calcium case, the emulator basis sizes were varied between $N _ { \psi } = 8 – 1 6$ and $N _ { \mathrm { U } } = 1 0 – 1 2$ , while the fresco solver result, indicated by the red dashed line, corresponds to an evaluation time of 75.1 ms. The emulator consistently achieves median relative errors well below $1 0 \%$ across the test parameter sets, confirming its reliability in describing both elastic and inelastic observables in a heavy, strongly coupled system with octupole couplings.

The robustness of the emulator across different multipole orders and mass regimes underscores its potential as a versatile tool for large-scale studies of coupled-channel reactions. Nevertheless, we observe a marginal decrease in the speed-up compared to the quadrupole case. This reduction stems from the need to emulate the wavefunctions for all incoming and outgoing boundary conditions, as discussed in Subsection $\mathrm { 1 1 8 4 }$ . To obtain the Petrov– Galerkin coefficients in Eq. (16), one must solve a linear system of dimension $( N _ { c } \cdot N _ { \psi } ) \times ( N _ { c } \cdot N _ { \psi } )$ , leading to a computational complexity of $\mathcal { O } ( N _ { c } ^ { 3 } N _ { \psi } ^ { 3 } )$ .

Since this calculation must be repeated $N _ { c }$ times, corresponding to the possible incoming boundary conditions, the total cost of emulating cross sections scales as $\mathcal { O } ( N _ { c } ^ { 4 } N _ { \psi } ^ { 3 } )$ . For example, octupole couplings can connect up to five different partial waves by angular-momentum selection rules, in contrast to quadrupole couplings which involve at most four. Other coupled-channel emulators based on reduced-basis methods appear to face similar scaling limitations [34, 43]. In practice, however, for the medium- and heavy-mass systems studied here, this trade-off still yields speed-ups exceeding one and a half orders of magnitude relative to the high-fidelity solver, while maintaining median cross-section errors below the percent level. This demonstrates that, although unfavorable scaling can diminish efficiency gains in large coupled systems, the emulator framework remains robust and highly efficient in the low-energy neutron-nucleus cases studied.

![](images/befdc35934c8b4fe88aaa1df736799c19eff38925f69a87d59acf19b21874324.jpg)

![](images/d92f5c320efe63e038c1c8d8dbea73d26db86ed296e4de4a7e472f996e880cc3.jpg)  
FIG. 4. Computational Accuracy vs. Time (CAT) plot illustrating the trade-off between accuracy and computational speed for both the coupled-channel (CC) emulator and the high-fidelity fresco solver in the calculation of the differential cross section for the elastic (open markers) and inelastic (filled markers) channels of the $^ { 2 0 8 } \mathrm { P b } ( n , n ^ { \prime } ) ^ { 2 0 8 } \mathrm { P b } ( 3 ^ { - } )$ reaction at $E _ { \mathrm { l a b } } ~ = ~ 1 2$ MeV [panel (a)] and $E _ { \mathrm { l a b } } ~ = ~ 2 6$ MeV [panel (b)]. The horizontal axis represents the evaluation time per calculation, while the vertical axis shows the accuracy, defined as the median relative error in the differential cross section with respect to the fresco result, computed across 50 test parameter sets centered on the corresponding KD values. For the CC emulator, the number of basis functions in the wavefunction expansion ( $\mathrm { ~ \textmu ~ } _ { {  } } N _ { \psi }$ ) and the EIM representation ( $N _ { \mathrm { { U } } }$ ) were varied between 8 and 16. The vertical red dashed line indicates the fresco solver evaluation time of 75.1 ms. The emulator achieves relative errors below $1 0 ^ { - 1 }$ while providing speedups around one and a half orders of magnitude, depending on the basis size employed.

# V. CONCLUSIONS AND OUTLOOK

In this work we have developed and demonstrated a coupled-channel emulator for neutron–nucleus scattering based on a reduced-basis Petrov–Galerkin formalism for non-affinely parametrized potentials and realistic nuclear couplings (rigid-rotor). The emulator combines precomputation of system-dependent quantities with a dimensionality-reduced representation of the scattering wavefunctions, enabling fast and accurate evaluation of differential cross sections. We used the benchmark cases of $^ { 4 8 } \mathrm { C a } ( n , n ^ { \prime } ) ^ { 4 8 } \mathrm { C a } ( 2 ^ { + } )$ and $^ { \mathrm { 2 0 s } } \mathrm { P b } ( n , n ^ { \prime } ) ^ { \mathrm { 2 0 s } } \mathrm { P b } ( 3 ^ { - } )$

at $E _ { \mathrm { l a b } } = 1 2$ MeV and $E _ { \mathrm { l a b } } = 2 6$ MeV. The method generalizes robustly from medium-mass to heavy nuclei and across multipole couplings, energies and masses.

The observed efficiency gains are primarily the result of two factors: (i) restructuring the computation to avoid redundant evaluation of integrals, coupling matrix elements, and Coulomb functions, and (ii) reducing the dimensionality of the linear system through projection onto the reduced-basis functions. Although unfavorable scaling with the number of coupled channels $N _ { c }$ introduces some reduction in speed-up for large coupled systems (e.g., octupole excitations), the emulator remains highly efficient and accurate within the regimes relevant to low-energy nucleon–nucleus reactions.

The coupled-channel emulator developed here offers a practical and flexible tool for accelerating reaction theory, with controlled trade-offs of speed and accuracy in a way that makes systematic studies of complex nuclear systems tractable. Its demonstrated performance in medium- and heavy-mass nuclei motivates future work extending the approach to broader classes of couplings and embedding it within modern uncertainty quantification pipelines.

Further work must be carried out to understand the limitations of this approach and if indeed the poor scaling with increasing number of coupled-channels can be overcome. For the moment, the emulator appears to not be appropriate for nuclear reactions including many states such as those in [44]. Looking ahead, several extensions of this framework are promising. The use of GPU acceleration, already natural in the linear-algebra formulation, offers additional gains in speed that can further expand the scope of feasible parameter studies.

# ACKNOWLEDGEMENTS

This research was supported by the CSSI program Award OAC-2004601 (BAND collaboration). F.M.N. and K.B. acknowledge support of the U.S. Department of Energy Grant No. DE-SC0021422. R.J.F. acknowledges support from the National Science Foundation Award Nos. PHY-2209442/PHY-2514765 and the NUCLEI Sci-DAC program under award DE-FG02-96ER40963.

# Appendix A: Details for coupled-channel equations and observables

# 1. Coupling Matrix Elements

The effective n-target potential $V ( \pmb { r } , \pmb { \xi } _ { t } )$ for a deformed rigid rotor can be decomposed in multipoles $\omega$ :

$$
\begin{array}{l} V (\boldsymbol {r}, \boldsymbol {\xi} _ {t}; \boldsymbol {\alpha}) = \sqrt {4 \pi} \sum_ {\omega m _ {\omega}} U _ {\omega} (r; \boldsymbol {\alpha}) D _ {m _ {\omega} 0} ^ {\omega} \mathcal {Y} _ {\omega} ^ {m _ {\omega}} (\hat {\boldsymbol {r}}) \\ = \sqrt {4 \pi} \sum_ {\omega} ^ {\omega m _ {\omega}} U _ {\omega} (r; \boldsymbol {\alpha}) P _ {\omega} (\cos \theta^ {\prime}), \tag {A1} \\ \end{array}
$$

where $D$ is the Wigner rotation matrix relating the labframe vector $\hat { r }$ to the body-fixed frame $\hat { r ^ { \prime } }$ , often referred to as the Euler angles. The exact form the radial dependence of these multipole couplings can be derived from the properties of Legendre polynomials:

$$
U _ {\omega} (r; \boldsymbol {\alpha}) = \frac {1}{\sqrt {4 \pi}} \int_ {0} ^ {2 \pi} V (\boldsymbol {r}, \boldsymbol {\xi} _ {t}; \boldsymbol {\alpha}) P _ {\omega} \left(\cos \theta^ {\prime}\right) \sin \theta^ {\prime} d \theta^ {\prime} d \phi^ {\prime}. \tag {A2}
$$

For small deformation lengths $\delta _ { \omega }$ , such as those used in this work, one can perform a first order expansion which simplifies Eq. (A1):

$$
V (\boldsymbol {r}, \boldsymbol {\xi} _ {t}; \boldsymbol {\alpha}) \approx U (r; \hat {\boldsymbol {\alpha}}) - \sum_ {\omega} \delta_ {\omega} U ^ {\prime} (r; \hat {\boldsymbol {\alpha}}) P _ {\omega} (\cos \theta^ {\prime}) \tag {A3}
$$

The eigenstates of a deformed rotor are given by:

$$
\Phi_ {I _ {\nu}} (\boldsymbol {\xi} _ {t}) = \sqrt {\frac {2 I _ {\nu} + 1}{8 \pi^ {2}}} D _ {M K _ {\nu}} ^ {I _ {\nu}} ^ {*} (\boldsymbol {\xi} _ {t}). \tag {A4}
$$

We can now calculate the geometric part of the coupling potential defined in Eq. (12). As in Sect. III, we neglect the internal structure of the projectile, as well as its spin. Following the derivation in [32] we project onto a state:

$$
| \nu (\hat {\boldsymbol {r}}, \boldsymbol {\xi} _ {t}) \rangle = | (l _ {\nu} I _ {\nu} ^ {t}) J \rangle , \tag {A5}
$$

and obtain the following matrix elements:

$$
\begin{array}{l} \mathcal {V} _ {\omega \mu \nu} = \left\langle \left(l _ {\mu} I _ {\mu} ^ {t}\right) J ^ {\prime} \right| | P _ {\omega} (\cos \theta^ {\prime}) | | \left(l _ {\nu} I _ {\nu} ^ {t}\right) J \rangle \\ = \delta_ {J J ^ {\prime}} (- 1) ^ {\omega + J + l _ {\nu} + I _ {\mu}} \\ \times i ^ {l _ {\nu} - l _ {\mu}} \hat {I} _ {\nu} \hat {l} _ {\nu} \hat {\omega} \left\{ \begin{array}{c c c} l _ {\nu} & I _ {\nu} & J \\ I _ {\mu} & l _ {\mu} & \omega \end{array} \right\} \tag {A6} \\ \times \left\langle l _ {\nu} 0, \omega 0 \mid l _ {\mu} 0 \right\rangle \left\langle I _ {\nu} K _ {\nu}, \Omega 0 \mid I _ {\mu} K _ {\mu} \right\rangle , \\ \end{array}
$$

# 2. Calculating Inelastic Cross Sections

Once the S-matrix is obtained (see Eq. (31)), computing the cross sections is straightforward. In the most general nucleus-nucleon scattering case, where we include projectile spin, the cross section for populating a target in state $I _ { \nu }$ from some initial state $I _ { 0 }$ can be expressed as:

$$
\frac {d \sigma_ {I _ {\nu}}}{d \Omega} = \frac {1}{(2 s + 1) (2 I _ {0} + 1)} \sum_ {m _ {s ^ {\prime}} m _ {I _ {\nu}} m _ {s} m _ {I _ {0}}} | f _ {m _ {s ^ {\prime}} m _ {I _ {\nu}} m _ {s} m _ {I _ {0}}} (\theta) | ^ {2} \tag {A7}
$$

In the (l–s) coupling basis, the scattering amplitude is:

$$
\begin{array}{l} f _ {m _ {s ^ {\prime}} m _ {I _ {\nu}} m _ {s} m _ {I _ {0}}} (\theta) = \delta_ {m _ {s ^ {\prime}} m _ {s}} \delta_ {m _ {I _ {\nu}}, m _ {I _ {0}}} f _ {C, I _ {0}} (\theta) \\ \times \frac{4\pi}{2i}\sum_{\substack{JM\\ l jI_{0},l^{\prime}j^{\prime}I_{\nu}\\ mm^{\prime},m_{j},m_{j^{\prime}}}}Y_{l^{\prime}m^{\prime}}(\theta ,0)  Y_{l0}^{*}(0,0) \\ \times \langle l ^ {\prime} m ^ {\prime} s ^ {\prime} m _ {s ^ {\prime}} | j ^ {\prime} m _ {j ^ {\prime}} \rangle \langle j ^ {\prime} m _ {j ^ {\prime}} I _ {\nu} m _ {I _ {\nu}} | J M \rangle \\ \times \langle J M | j m _ {j} I _ {0} m _ {I _ {0}} \rangle \langle j m _ {j} | l 0 s m _ {s} \rangle e ^ {i \sigma_ {l ^ {\prime} I _ {\nu}}} \\ \times \left(\mathbf {S} _ {l ^ {\prime} j ^ {\prime} I _ {\nu}, l j I _ {0}} ^ {J} - \delta_ {l l ^ {\prime}} \delta_ {j j ^ {\prime}} \delta_ {I _ {0} I _ {\nu}}\right) \frac {e ^ {i \sigma_ {l I _ {0}}}}{k _ {\nu}}, \tag {A8} \\ \end{array}
$$

where $f _ { C , I _ { 0 } }$ is the amplitude from the Coulomb interaction alone, $o$ is the Coulomb phase shift and $k _ { \nu }$ is the momentum corresponding of a channel labeled by $\nu$ [32].

# Appendix B: 2-level system example

In this appendix, we present a pedagogical example illustrating the formalism developed in Sec. II. We consider a simple and general two-level system and explicitly derive the corresponding Petrov–Galerkin equations. Starting from Eq. (8), we consider the transition from an initial channel $\lambda$ to a final state $\nu$ , resisticting only to two channels. This leads to a pair of coupled equations to be solved for each incoming boundary condition corresponding to $\lambda = 1 , 2$ . We work out explicitly the equation when the initial channel is $\lambda = 1$ . We have:

$$
\begin{array}{l} \left(T _ {1} + V _ {1 1} - \left(E - \epsilon_ {1}\right) \psi_ {1, 1} = - V _ {1 2} \psi_ {2, 1} \right. \\ \left(T _ {2} + V _ {2 2} - \left(E - \epsilon_ {2}\right)\right) \psi_ {2, 1} = - V _ {2 1} \psi_ {1, 1} \tag {B1} \\ \end{array}
$$

Although not shown explicitly, $\psi$ and $V$ depend on the radial coordinate $r$ and the interaction parameters $\alpha$ . To construct the reduced basis elements, we obtain $N _ { s }$ high-fidelity solutions to the coupled equations (B1) and perform the PCA. The set of $N _ { \psi }$ chosen basis elements for the two level system with incoming wave $\lambda = 1$ are then expressed as:

$$
\begin{array}{l} \{\tilde {\psi} _ {1, 1} ^ {(k)} (r) \} _ {k = 1} ^ {N _ {\psi}} = \operatorname {P C A} \left[ \left\{\psi_ {1, 1} (r; \boldsymbol {\alpha} _ {i}) - \phi_ {1} (r) \right\} _ {i = 1} ^ {N _ {s}} \right] \tag {B2} \\ \{\tilde {\psi} _ {2, 1} ^ {(k)} (r) \} _ {k = 1} ^ {N _ {\psi}} = \operatorname {P C A} \left[ \{\psi_ {2, 1} (r; \boldsymbol {\alpha} _ {i}) \} _ {i = 1} ^ {N _ {s}} \right], \\ \end{array}
$$

where $\phi _ { 1 }$ is the free solution. Following Sect. II, we then approximate the solution to each wavefunction in the coupled system as a linear combination of the corresponding basis elements $\tilde { \psi }$ and some coefficients $c$ :

$$
\begin{array}{l} \psi_ {1, 1} (r; \boldsymbol {\alpha}) \approx \phi_ {1} (r) + \sum_ {k = 1} ^ {N _ {\psi}} c _ {1} ^ {(k)} (\boldsymbol {\alpha}) \tilde {\psi} _ {1, 1} ^ {(k)} (r) \tag {B3} \\ \psi_ {2, 1} (r; \boldsymbol {\alpha}) \approx \sum_ {k = 1} ^ {N _ {\psi}} c _ {2} ^ {(k)} (\boldsymbol {\alpha}) \tilde {\psi} _ {2, 1} ^ {(k)} (r) \\ \end{array}
$$

To obtain the coefficients we now perform the Petrov-Galerkin projection used in Eq. (17):

$$
\mathcal {D} _ {1, 1} ^ {(j k)} = \left\langle \tilde {\psi} _ {1, 1} ^ {(j)} \mid T _ {1} (r) - \left(E - \epsilon_ {1}\right) \mid \tilde {\psi} _ {1, 1} ^ {(k)} \right\rangle , \tag {B4}
$$

$$
\mathcal {D} _ {2, 1} ^ {(j k)} = \langle \tilde {\psi} _ {2, 1} ^ {(j)} | T _ {2} (r) - (E - \epsilon_ {2}) | \tilde {\psi} _ {2, 1} ^ {(k)} \rangle .
$$

These terms involve only the kinetic operator and the channel energy. Next we calculate the terms pertaining to the interaction:

$$
\mathcal {U} _ {1 1, 1} ^ {(j k)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega 1 1} \langle \tilde {\psi} _ {1, 1} ^ {(j)} | f _ {\omega} (r; \boldsymbol {\alpha}) | \tilde {\psi} _ {1, 1} ^ {(k)} \rangle ,
$$

$$
\mathcal {U} _ {1 2, 1} ^ {(j k)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega 1 2} \left\langle \tilde {\psi} _ {1, 1} ^ {(j)} \mid f _ {\omega} (r; \boldsymbol {\alpha}) \mid \tilde {\psi} _ {2, 1} ^ {(k)} \right\rangle , \tag {B5}
$$

$$
\mathcal {U} _ {2 1, 1} ^ {(j k)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega 2 1} \langle \tilde {\psi} _ {2, 1} ^ {(j)} | f _ {\omega} (r; \boldsymbol {\alpha}) | \tilde {\psi} _ {1, 1} ^ {(k)} \rangle ,
$$

$$
\mathcal {U} _ {2 2, 1} ^ {(j k)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega 2 2} \langle \tilde {\psi} _ {2, 1} ^ {(j)} | f _ {\omega} (r; \boldsymbol {\alpha}) | \tilde {\psi} _ {2, 1} ^ {(k)} \rangle
$$

Note that the sum over $\omega$ often collapses due to angular momentum selection rules.

In the case of a non-affinely parametrized interaction, the integrals above must be replaced by those of Eq. (26). The remnant term in the Petrov-Galerkin equations com-

ing from the added free solution yields:

$$
\mathcal {R} _ {1, 1} ^ {(j)} = \langle \tilde {\psi} _ {1, 1} ^ {(j)} | T _ {1} (r) - (E - \epsilon_ {1}) | \phi_ {1} \rangle ,
$$

$$
\mathcal {C} _ {1 1, 1} ^ {(j)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega 1 1} \left\langle \tilde {\psi} _ {1, 1} ^ {(j)} \right| f _ {\omega} (r; \boldsymbol {\alpha}) | \phi_ {1} \rangle , \tag {B6}
$$

$$
\mathcal {C} _ {2 1, 1} ^ {(j)} (\boldsymbol {\alpha}) = \sum_ {\omega = 0} ^ {N _ {m}} \mathcal {V} _ {\omega 2 1} \langle \tilde {\psi} _ {2, 1} ^ {(j)} | f _ {\omega} (r; \boldsymbol {\alpha}) | \phi_ {1} \rangle .
$$

Now, we cast the Petrov-Galerkin equations into linear algebra form:

$$
\begin{array}{l} \left( \begin{array}{c c} \mathcal {D} _ {1, 1} ^ {(j k)} + \mathcal {U} _ {1 1, 1} ^ {(j k)} (\boldsymbol {\alpha}) & \mathcal {U} _ {1 2, 1} ^ {(j k)} (\boldsymbol {\alpha}) \\ \mathcal {U} _ {2 1, 1} ^ {(j k)} (\boldsymbol {\alpha}) & \mathcal {D} _ {2, 1} ^ {(j k)} + \mathcal {U} _ {2 2, 1} ^ {(j k)} (\boldsymbol {\alpha}) \end{array} \right) \left( \begin{array}{c} c _ {1} ^ {(k)} \\ c _ {2} ^ {(k)} \end{array} \right) \\ = \binom {\mathcal {R} _ {1, 1} ^ {(j)} + \mathcal {C} _ {1 1, 1} ^ {(j)} (\boldsymbol {\alpha})} {\mathcal {C} _ {2 1, 1} ^ {(j)} (\boldsymbol {\alpha}).} \tag {B7} \\ \end{array}
$$

These equations are now solved for some unknown $c _ { 1 }$ and $c _ { 2 }$ . In addition to the solutions for $\lambda = 1$ (shown above), we also need to compute the solutions for the incoming channel $\lambda = 2$ . The full scattering wavefunction can then be expressed as:

$$
\hat {\boldsymbol {\Psi}} = \left( \begin{array}{c c} \psi_ {1, 1} & \psi_ {1, 2} \\ \psi_ {2, 1} & \psi_ {2, 2} \end{array} \right). \tag {B8}
$$

From the asymptotic form of this full solution, we extract the full scattering matrix (see Eq. (31)).

[1] U. D. of Energy (USDOE), A New Era of Discovery: The 2023 Long Range Plan for Nuclear Science, Tech. Rep. (US Department of Energy (USDOE), Washington, DC (United States). Office of Science, 2023).   
[2] H. Schatz, A. D. Becerril Reyes, A. Best, E. F. Brown, K. Chatziioannou, K. A. Chipps, C. M. Deibel, R. Ezzeddine, D. K. Galloway, C. J. Hansen, F. Herwig, A. P. Ji, M. Lugaro, Z. Meisel, D. Norman, J. S. Read, L. F. Roberts, A. Spyrou, I. Tews, F. X. Timmes, C. Travaglio, N. Vassh, C. Abia, P. Adsley, S. Agarwal, M. Aliotta, W. Aoki, A. Arcones, A. Aryan, A. Bandyopadhyay, A. Banu, D. W. Bardayan, J. Barnes, A. Bauswein, T. C. Beers, J. Bishop, T. Boztepe, B. Côté, M. E. Caplan, A. E. Champagne, J. A. Clark, M. Couder, A. Couture, S. E. de Mink, S. Debnath, R. J. deBoer, J. den Hartogh, P. Denissenkov, V. Dexheimer, I. Dillmann, J. E. Escher, M. A. Famiano, R. Farmer, R. Fisher, C. Fröhlich, A. Frebel, C. Fryer, G. Fuller, A. K. Ganguly, S. Ghosh, B. K. Gibson, T. Gorda, K. N. Gourgouliatos, V. Graber, M. Gupta, W. C. Haxton, A. Heger, W. R. Hix, W. C. G. Ho, E. M. Holmbeck, A. A. Hood, S. Huth, G. Imbriani, R. G. Izzard, R. Jain, H. Jayatissa, Z. Johnston, T. Kajino, A. Kankainen, G. G. Kiss,

A. Kwiatkowski, M. La Cognata, A. M. Laird, L. Lamia, P. Landry, E. Laplace, K. D. Launey, D. Leahy, G. Leckenby, A. Lennarz, B. Longfellow, A. E. Lovell, W. G. Lynch, S. M. Lyons, K. Maeda, E. Masha, C. Matei, J. Merc, B. Messer, F. Montes, A. Mukherjee, M. R. Mumpower, D. Neto, B. Nevins, W. G. Newton, L. Q. Nguyen, K. Nishikawa, N. Nishimura, F. M. Nunes, E. O’Connor, B. W. O’Shea, W.-J. Ong, S. D. Pain, M. A. Pajkos, M. Pignatari, R. G. Pizzone, V. M. Placco, T. Plewa, B. Pritychenko, A. Psaltis, D. Puentes, Y.-Z. Qian, D. Radice, D. Rapagnani, B. M. Rebeiro, R. Reifarth, A. L. Richard, N. Rijal, I. U. Roederer, J. S. Rojo, J. S. K, Y. Saito, A. Schwenk, M. L. Sergi, R. S. Sidhu, A. Simon, T. Sivarani, A. Skúladóttir, M. S. Smith, A. Spiridon, T. M. Sprouse, S. Starrfield, A. W. Steiner, F. Strieder, I. Sultana, R. Surman, T. Szücs, A. Tawfik, F. Thielemann, L. Trache, R. Trappitsch, M. B. Tsang, A. Tumino, S. Upadhyayula, J. O. Valle Martínez, M. Van der Swaelmen, C. Viscasillas Vázquez, A. Watts, B. Wehmeyer, M. Wiescher, C. Wrede, J. Yoon, R. G. T. Zegers, M. A. Zermane, and M. Zingale, Journal of Physics G: Nuclear and Particle Physics 49, 110502 (2022).

[3] G. Potel, G. Perdikakis, B. V. Carlson, M. C. Atkinson, W. H. Dickhoff, J. E. Escher, M. S. Hussein, J. Lei, W. Li, A. O. Macchiavelli, A. M. Moro, F. M. Nunes, S. D. Pain, and J. Rotureau, European Physical Journal A 53, 178 (2017).   
[4] C. W. Johnson, K. D. Launey, N. Auerbach, S. Bacca, B. R. Barrett, C. Brune, M. A. Caprio, P. Descouvemont, W. H. Dickhoff, C. Elster, P. J. Fasano, K. Fossez, H. Hergert, M. Hjorth-Jensen, L. Hlophe, B. Hu, R. M. Id Betan, A. Idini, S. König, K. Kravvaris, D. Lee, J. Lei, P. Maris, A. Mercenne, K. Minomo, R. Navarro Pérez, W. Nazarewicz, F. M. Nunes, M. Płoszajczak, S. Quaglioni, J. Rotureau, G. Rupak, A. M. Shirokov, I. Thompson, J. P. Vary, A. Volya, F. Xu, V. Zelevinsky, and X. Zhang, J. Phys. G: Nucl. Part. Phys. 47, 123001 (2020).   
[5] H. Feshbach, Annals of Physics 5, 357 (1958).   
[6] C. Hebborn, F. Nunes, G. Potel, W. Dickhoff, J. Holt, M. Atkinson, R. Baker, C. Barbieri, G. Blanchon, M. Burrows, et al., Journal of Physics G: Nuclear and Particle Physics 50, 060501 (2023).   
[7] A. E. Lovell and F. M. Nunes, Phys. Rev. C 97, 16 (2018).   
[8] G. B. King, A. E. Lovell, L. Neufcourt, and F. M. Nunes, Phys. Rev. Lett. 122, 5 (2019).   
[9] A. E. Lovell, F. M. Nunes, M. Catacora-Rios, and G. B. King, J. Phys. G: Nucl. Part. Phys 48, 014001 (2020).   
[10] M. Catacora-Rios, A. E. Lovell, and F. M. Nunes, Phys. Rev. C 108, 024601 (2023).   
[11] M. Catacora-Rios, G. B. King, A. E. Lovell, and F. M. Nunes, Phys. Rev. C 100, 10 (2019).   
[12] M. Catacora-Rios, G. B. King, A. E. Lovell, and F. M. Nunes, Phys. Rev. C 104, 9 (2021).   
[13] A. Quarteroni, A. Manzoni, and F. Negri, Reduced Basis Methods for Partial Differential Equations: An Introduction, Vol. 92 (Springer, 2015).   
[14] E. Bonilla, P. Giuliani, K. Godbey, and D. Lee, Phys. Rev. C 106, 054322 (2022).   
[15] C. Drischler, J. A. Melendez, R. J. Furnstahl, A. J. Garcia, and X. Zhang, Front. Phys. 10, 92931 (2023), arXiv:2212.04912.   
[16] W. Kohn, Phys. Rev. 74, 1763 (1948).   
[17] R. J. Furnstahl, A. J. Garcia, P. J. Millican, and X. Zhang, Phys. Lett. B 809, 135719 (2020).   
[18] C. Drischler, M. Quinonez, P. Giuliani, A. Lovell, and F. Nunes, Phys. Lett. B 823, 136777 (2021).   
[19] X. Zhang and R. J. Furnstahl, Phys. Rev. C 105, 064004 (2022), arXiv:2110.04269 [nucl-th].   
[20] J. A. Melendez, C. Drischler, A. J. Garcia, R. J. Furnstahl, and X. Zhang, Phys. Lett. B 821, 136608 (2021).   
[21] A. Garcia, C. Drischler, R. Furnstahl, J. Melendez, and X. Zhang, Physical Review C 107, 054001 (2023).   
[22] D. Odell, P. Giuliani, K. Beyer, M. Catacora-Rios, M. Y.- H. Chan, E. Bonilla, R. J. Furnstahl, K. Godbey, and F. M. Nunes, Phys. Rev. C 109, 044612 (2024).   
[23] M. Barrault, Y. Maday, N. C. Nguyen, and A. T. Patera,

C. R. Math. 339, 667 (2004).   
[24] M. A. Grepl, Y. Maday, N. C. Nguyen, and A. T. Patera, ESAIM: Math. Model. Numer. Anal. 41, 575 (2007).   
[25] C. Schwartz, Phys. Rev. 124, 1468 (1961).   
[26] K. Rusek, I. Martel, J. Gómez-Camacho, A. M. Moro, and R. Raabe, Phys. Rev. C 72, 037603 (2005).   
[27] G. P. A. Nobre, F. S. Dietrich, J. E. Escher, I. J. Thompson, M. Dupuis, J. Terasaki, and J. Engel, Phys. Rev. C 84, 064609 (2011).   
[28] D. Smalley, F. Sarazin, F. M. Nunes, B. A. Brown, P. Adsley, H. Al-Falou, C. Andreoiu, B. Baartman, G. C. Ball, J. C. Blackmon, H. C. Boston, W. N. Catford, S. Chagnon-Lessard, A. Chester, R. M. Churchman, D. S. Cross, C. A. Diget, D. D. Valentino, S. P. Fox, B. R. Fulton, A. Garnsworthy, G. Hackman, U. Hager, R. Kshetri, J. N. Orce, N. A. Orr, E. Paul, M. Pearson, E. T. Rand, J. Rees, S. Sjue, C. E. Svensson, E. Tardiff, A. D. Varela, S. J. Williams, and S. Yates, Phys. Rev. C 89, 024602 (2014).   
[29] N. C. Summers and F. M. Nunes, Phys. Rev. C 70, 011602 (2004).   
[30] J. L. Ferreira, J. Rangel, J. Lubian, and L. F. Canto, Phys. Rev. C 107, 034603 (2023).   
[31] I. J. Thompson, Computer Physics Reports 7, 167 (1988).   
[32] I. J. Thompson and F. M. Nunes, Nuclear Reactions for Astrophysics: Principles, Calculation and Applications of Low-Energy Reactions (Cambridge University Press, 2009).   
[33] T. TAMURA, Rev. Mod. Phys. 37, 679 (1965).   
[34] A. J. Garcia, C. Drischler, R. J. Furnstahl, J. A. Melendez, and X. Zhang, Phys. Rev. C 107, 054001 (2023).   
[35] J. S. Hesthaven, G. Rozza, B. Stamm, et al., Certified Reduced Basis Methods for Parametrized Partial Differential Equations, Vol. 590 (Springer, 2016).   
[36] S. A. Goreinov, I. V. Oseledets, D. V. Savostyanov, E. E. Tyrtyshnikov, and N. L. Zamarashkin, in Matrix Methods: Theory, Algorithms and Applications (World Scientific, 2010) pp. 247–256.   
[37] M. Herman, R. Capote, B. Carlson, P. Obložinsk`y, M. Sin, A. Trkov, H. Wienke, and V. Zerkin, Nuclear data sheets 108, 2655 (2007).   
[38] P. Descouvemont and D. Baye, Reports on progress in physics 73, 036301 (2010).   
[39] D. Baye, Physics reports 565, 1 (2015).   
[40] A. Koning and J. Delaroche, Nuclear Physics A 713, 231 (2003).   
[41] B. Pritychenko, M. Birch, B. Singh, and M. Horoi, Atomic Data and Nuclear Data Tables 107, 1 (2016).   
[42] L. M. Robledo and G. F. Bertsch, Phys. Rev. C 84, 054302 (2011).   
[43] K. Hagino, Z. Liao, S. Yoshida, M. Kimura, and K. Uzawa, Phys. Rev. C 112, 024618 (2025).   
[44] E. S. Soukhovitski˜ı, R. Capote, J. M. Quesada, S. Chiba, and D. S. Martyanov, Phys. Rev. C 94, 064605 (2016).