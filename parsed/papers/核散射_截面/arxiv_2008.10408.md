# The total reaction cross section of heavy-ion reactions induced by stable and unstable exotic beams: The low-energy regime

L. F. Canto1, V. Guimar˜aes $^ 2$ , J. Lubian3, and M. S. Hussein4,5a

1 Instituto de F´ısica, Universidade Federal do Rio de Janeiro, CP 68528, Rio de Janeiro, Brazil, e-mail: canto@if.ufrj.br   
  
3 Instituto de F´ısica, Universidade Federal Fluminense, Av. Litoranea s/n, Gragoat´a, Niter´oi, R.J., 24210-340, Brazil,   
4 Instituto de Estudos Avan¸cados, Universidade de S˜ao Paulo C. P. 72012, 05508-970 S˜ao Paulo-SP, Brazil, and Instituto de F´ısica, Universidade de S˜ao Paulo, C. P. 66318, 05314-970 S˜ao Paulo,-SP, Brazil,   
5 Departamento de F´ısica, Instituto Tecnol´ogico de Aeron´autica, CTA, S˜ao Jos´e dos Campos, S˜ao Paulo, SP, Brazil

August 25, 2020

Abstract. In this review paper we present a detailed account of the extraction and the calculation of the total reaction cross section of strongly bound and weakly bound, stable and unstable, exotic, nuclei. We discuss the optical model and the more general coupled channels model of direct reactions, and how from fits to the data on elastic scattering supplies the elastic element of (partial wave) S-matrix and correspondingly the differential cross section and the total reaction cross section. The effect of long-range absorption due to the coupling to excited states in the target and to the breakup continuum in the projectile is also discussed. The semiclassical method is then analyzed and the Hill-Wheeler expression of the tunneling probability and the Wong formula for the fusion and the total reaction cross sections are discussed in details. The generalized optical theorem for charged particle scattering and the resulting sum-of differences method is then discussed. Also, the strong absorption model in its sharp cutoff form and its generalization, the smooth cutoff, is discussed. The so-called ”quarter-point recipe” is discussed next, and the quarter-point angle is introduced as a simple and rapid mean to obtain the total reaction cross section. The last topic discussed is the reduction of the total reaction cross section that would allow a large body of data to sit on a single universal function. Such a universal function exists in the case of the fusion data, and the aim of this last topic of the review is to extend the fusion case to the total reaction, by adding the direct reaction contribution. Also discussed is the inclusive breakup cross section and how it can be used to extract the total reaction cross section of the interacting fragment with the target. This method is also known as the Surrogate method and represents a case of hybrid reactions. The sum of the integrated inclusive breakup cross section with the complete fusion cross section supplies the total fusion cross section. The main experimental methods to determine the total reaction cross section are also discussed, with emphasis in recent techniques developed to deal with reactions induced by unstable beams.

PACS. 24.10Eq 25.70.Bc 25.60Gc

# Contents

1 Introduction . 2   
2 Potential scattering and the optical Model . . . . 3

2.1 Fusion and total reaction cross sections 4   
2.2 The semiclassical scattering amplitude . . . . . 7   
2.3 The Generalized Optical Theorem and the Sum of Differences Method 9   
2.4 Comparison of Quantum mechanical cross sections with the Wong and the quarter-point approximations 10

3 Many-body scattering theory . . . 11

3.1 The CC equations 11

3.2 Coupled channels in the continuum - The CDCC method 12

4 Hybrid reactions: The Surrogate Method . . . . . . . 19

4.1 The inclusive nonelastic breakup cross section . 19   
4.2 Applications . 22

5 The total reaction cross section data . . . 24

5.1 Elastic scattering measurements and total reaction cross section 24   
5.2 Direct measurements and total reaction cross section . 29   
5.3 Comparative studies of cross sections . . . . . . 32

6 Summary 37

# 1 Introduction

The field of nuclear reactions has evolved greatly over the last 6 or so decades. In most applications to low energy direct reactions the reliance has been on the use of the optical model in its single channel version and its coupled channels version. The more complex compound nuclear reactions are treated within the Statistical Theory and gives for the average cross section for a transition (a,b) that proceeds through the compound nucleus (CN) the Hauser-Feshbach form whose calculation involves precisely the theory of direct reactions. This closed theory has been recently pushed to the limits when confronted with reactions induced by weakly bound normal and exotic nuclei. These latter nuclei, such as the Borromean twoneutron halo ones $^ { 6 } \mathrm { H e }$ $^ 4 \mathrm { H e } + 2 n$ , $S _ { 2 n } = 0 . 9 7 3$ MeV), $\mathrm { ^ { 1 1 } L i }$ ${ } ^ { \mathrm { 9 } } \mathrm { L i } + 2 n$ , $S _ { 2 n } = 0 . 3 6 9 \mathrm { M e V }$ ), $^ { 1 4 } \mathrm { { B e } }$ ( $^ { \cdot 1 2 } \mathrm { B e } + 2 n$ , $S _ { 2 n } = 1 . 2 7$ MeV ), $^ { 2 2 } \mathrm { C }$ $^ { \prime 2 0 } \mathrm { C } + 2 n$ , $S _ { 2 n } = 0 . 4 2 \pm 0 . 9 4$ MeV), the oneproton halo isotope $^ { 8 } \mathrm { { B } }$ ${ } ^ { 7 } \mathrm { B e } + p$ , $S _ { p } = 0 . 1 4$ MeV), and the one-neutron halo isotopes $^ { 1 1 } \mathrm { { B e } }$ $^ { \mathrm { { \circ } } _ { \mathrm { { B e } } + n } }$ , $S _ { n } = 0 . 5 0 3$ MeV), $^ { 1 5 } \mathrm { C }$ $^ { 1 4 } \mathrm { C } + n$ , $S _ { n } = 1 . 2 1 8$ MeV), $^ { 1 9 } \mathrm { C }$ ( $^ { 1 8 } \mathrm { C } + n$ , $S _ { n } =$ $0 . 2 4 2 \pm 0 . 0 9 5$ MeV) and 23O ${ \bigl ( } ^ { 2 2 } \mathrm { O } + n { \bigr ) }$ , $S _ { n } = 2 . 7 4$ MeV), are produced in several laboratories scattered in the world and used as secondary beams to react with target nuclei such as $^ { 1 2 } \mathrm { C }$ , 58Ni and ${ } ^ { 2 0 8 } \mathrm { { P b } }$ . An important consequence of the small binding energy of the valence particles in these weakly-bound nuclei is the increase of the radii as compared to normal nuclei with the same mass number. Several review articles have been written on different reactions involving weakly bound nuclei [1, 2, 3, 4, 5, 6, 7, 8].

What distinguishes the reactions induced by these very short lived nuclei as well as by stable weakly bound nuclei, such as 6Li ( $\mathrm { ^ 4 H e + ^ { 2 } H }$ , $S = 1 . 4 7$ MeV), 7Li $( ^ { 4 } \mathrm { H e } + ^ { 3 } \mathrm { H }$ , $S =$ 2.47 MeV) and $^ { 9 } \mathrm { { B e } }$ ( ${ ^ { 4 } \mathrm { H e } } + { ^ { 4 } \mathrm { H e } } + n$ , $S = 1 . 6 7$ MeV), from the usual reactions involving stable strongly bound projectiles is the presence in the former of two important features: existence of appreciable dipole strength at low excitation energy (the Pygmy resonance), and strong couplings with the breakup channel even at energies close to the Coulomb barrier. The latter feature is shared by the well studied deuteron scattering, with breakup threshold of 2.2 MeV, which is to be compared to 0.369 MeV for $_ { 1 1 }$ Li and 0.973 MeV for 6He. This implies that the continuum must always be taken into account in any serious attempt to analyze the data with the direct reaction theory. This was not the case in the past where ordinary strongly bound projectiles such as 16O were used to induce the nuclear reaction. At low energies, the single channel optical model was found to be adequate for spherical targets, whereas its coupled channels version is required for deformed targets such as $^ \mathrm { 1 5 2 }$ Sm or $^ { 2 3 8 }$ U, where, in these cases, the target’s rotational states must be taken into account.

One of the most important source of information about the size, radius, and geometry of nuclei comes from elastic scattering. A byproduct of the analysis of this reaction is the total reaction cross section, which accounts for all nonelastic processes. Whether the analysis of the elastic scattering data is done within the single channel or the

coupled channel version of the optical model theory of direct reactions, the total reaction cross section is defined in terms of the modulus of the partial-wave projected elastic $S$ -matrix. This cross section is the sum of the compound nucleus formation cross section (fusion) plus the sum of all direct nonelastic cross sections. In the case of non-exotic and strongly bound projectiles, the fusion cross section is that which accounts for the capture of the whole projectile, while the direct processes are inelastic excitations of the target and projectile and possibly transfer processes. In the case of exotic nuclei, the direct processes should include the elastic and nonelastic breakup of the projectile as well. The fusion cross section should also be defined differently here. The complete fusion (CF) is the compound nucleus formation cross section. There are other processes that come from the direct part, which involve the capture of one of the fragments of the projectile after the breakup process. This type of hybrid reaction is a new feature in the reaction and requires a new addition to the theory. This process is called incomplete fusion (ICF). The sum of CF and ICF is the total fusion TF. The cross section for these processes are denoted $\sigma _ { \mathrm { C F } }$ , $\sigma _ { \mathrm { I C F } }$ , and $\sigma _ { \mathrm { T F } }$ , with the sum rule, $\sigma _ { \mathrm { T F } } = \sigma _ { \mathrm { C F } } + \sigma _ { \mathrm { I C F } }$ . Experimentally, one usually measures $\sigma _ { \mathrm { T F } }$ . However, separate measurements of $\sigma _ { \scriptstyle \mathrm { C F } }$ and $\sigma _ { \mathrm { I C F } }$ are available for a few particular projectile-target combinations (see Ref. [4] and references therein). The analysis of the data, is usually done within the coupled channel version of the optical model theory of direct reactions, extended to include the breakup coupling. The resulting theory which reduced a three-body or four-body scattering system into an equivalent two-body system through a diligent discretization of the breakup continuum, is called the Continuum Discretized Coupled Channels (CDCC) theory [9, 10] is widely used [11, 12, 13]. Again from the analysis of the elastic scattering data one extracts the total reaction cross section which is of paramount importance in supplying a unitarity constraint on models used to calculate the different pieces of the direct reaction part and the CF part. For its importance in both strongly bound and weakly bound projectiles induced nuclear reactions, we felt the need to give an account of the different methods used for its extraction from the data. Back in 1991, Hussein, Rego and Bertulani [14] wrote a comprehensive review of the theory of the total reaction cross section. At that time, very few data existed for the elastic scattering of exotic and other weakly bound nuclear projectiles. The same happened for total reaction data. Thus, we think the time has come to supply, not a review, but an overall account with new and original material concerning this cross section, in view of the existence of a reasonably large body of new elastic scattering data of these exotic nuclear system.

This paper is organized as follows. In section 2 we introduce the potential scattering approach to heavy-ion collisions, where the influence of intrinsic degrees of freedom is simulated by a complex optical potential. We then consider some frequently used semiclassical approximations to the scattering amplitude and to the fusion cross

section, and discuss the optical theorem in the presence of absorption and Coulomb forces. The effects of intrinsic degrees of freedom on the collision dynamics are explicitly included in section 3. We introduce the coupled channel approach, and its generalization to deal with continuum states, the so-called continuum discretized coupled channel method. The latter is a basic tool to describe collisions of weakly bound projectiles, which may break up into fragments as it interacts with the target. In section 4 we discuss the surrogate method, which is very useful to determine inclusive cross sections in collisions of weakly bound projectiles. In section 5, we discuss experimental methods to determine total reaction cross sections in heavy-ion collisions. Special attention is devoted to recently developed techniques to handle reactions induced by low intensity radioactive beams. We discuss also the available procedures to reduce fusion and total reaction data, for the purpose of comparing results for different systems. Finally, in section 6 we present a summary of the topics discussed in this review paper.

# 2 Potential scattering and the optical Model

The description of heavy-ion collisions by potential scattering relies on the optical model. In this approach, the intrinsic properties of the collision partners are not explicitly taken into account. The attenuation of the incident wave owing to transitions to excited states of the system are then mocked up by a negative imaginary part in the interaction, which gives rise to a sub-unitary S-matrix. In typical situations, the potential is complex, spherically symmetric, depending only on the modulus of the collision vector, r, and it can be written as:

$$
U (r) = V (r) + i W (r). \tag {1}
$$

The real potential

$$
V (r) = V _ {\mathrm {C}} (r) + V _ {\mathrm {N}} (r), \tag {2}
$$

is the sum of the Coulomb and the nuclear interactions. An immediate consequence of this simplified treatment is that it cannot give cross sections for a particular nonelastic channel. It can only predict the elastic cross section and the total reaction cross section. The latter, given by the absorption cross section, represents the inclusive cross section for all nonelastic events (fusion plus direct reactions).

The details of $W ( r )$ depend on the physical processes responsible for the absorption of the incident flux. The formation of the CN, that is, fusion, always contribute to the absorption. Therefore, $W ( r )$ must be very strong at small values of $r$ , i.e., at the inner region of the Coulomb barrier. If fusion is the only process responsible for the absorption, the imaginary potential must be given by a function with large strength and short range. It can be represented, for instance, by the Woods-Saxon function,

$$
W (r) = - \frac {W _ {0}}{1 + \exp \left[ \left(r - R _ {0 \mathrm {i}}\right) / a _ {0 \mathrm {i}}\right)} \tag {3}
$$

![](images/c762fe77946f3086776cffdb07db61cc28e7243a4e613d006d30461a2d530bf7.jpg)

![](images/885b1a1f4fef21410503145d774cb7b7064fbff242f4bb65db4d6e5fe71a1b1c.jpg)  
Fig. 1. (Color on line) Panel (a): The Coulomb barrier for the S˜ao Paulo potential [15, 16] in $^ { 1 6 }$ $^ { 1 6 } \mathrm { O } \ - \ ^ { 2 0 8 } \mathrm { P b }$ scattering; Panel (b): Imaginary potentials simulating pure fusion absorption ( $W ^ { \mathbf { F } }$ ) and absorption arising from fusion and from direct reactions ( $W ^ { \mathrm { R } }$ ). For detail, see the text.

where $R _ { \mathrm { 0 i } } = r _ { 0 \mathrm { i } } \ \left[ A _ { \mathrm { P } } ^ { 1 / 3 } + A _ { \mathrm { T } } ^ { 1 / 3 } \right]$ , with $A _ { \mathrm { P } }$ and $A _ { \mathrm { T } }$ standing for the mass numbers of the projectile and the target, respectively. In this case, $W _ { 0 }$ is of the order of tens of MeV and the radius and diffusivity parameters, $r _ { \mathrm { 0 i } }$ and $a _ { \mathrm { 0 i } }$ , are chosen as to make $W ( r )$ be of short range. Typical values are $W _ { 0 } = 5 0$ MeV, $r _ { \mathrm { 0 i } } \sim 1 . 0$ fm and $a _ { \mathrm { 0 i } } \sim 0 . 2$ fm.

However, in typical heavy-ion collisions, the elastic and the reaction cross sections are strongly affected by direct reactions. Thus, the imaginary potentials should account also for the influence of these processes. Since they take place in grazing collisions, the range of the imaginary potential should be longer, reaching the barrier region. A common practice is to use the same radial dependence for the real and imaginary parts of the potential. Using this procedure with the double-folding S˜ao Paulo potential [15, 16], Gasques et al. [17] successfully described elastic scattering and total reaction cross sections for systems in different mass regions.

An illustration of the imaginary potentials in the cases of pure fusion absorption ( $W ^ { \mathrm { F } }$ ) and fusion plus direct reaction absorption ( $W ^ { \mathrm { R } }$ ) for the $\mathrm { ^ { 1 6 } O \mathrm { ~ - ~ } ^ { 2 0 8 } P b }$ scattering is presented in Fig. 1. In this example, the real part of the interaction is given by the Aky¨uz-Winther potential [18, 19]. Panel (a) shows the Coulomb barrier for this potential, whereas panel (b) shows the imaginary potentials $W ^ { \mathbf { F } }$ and $W ^ { \mathrm { R } }$ . The potential $W ^ { \mathrm { F } }$ was evaluated by Eq. (3), with $W _ { 0 } = 5 0$ MeV, $r _ { \mathrm { 0 i } } = 1 . 0$ fm and $a _ { \mathrm { 0 i } } = 0 . 2$ fm, and $W ^ { \mathrm { R } }$ was obtained by multiplying the real part of the potential by the factor 0.78.

# 2.1 Fusion and total reaction cross sections

In potential scattering the absorption cross section is given by the partial-wave series1

$$
\sigma_ {\mathrm {a b s}} (E) = \frac {\pi}{k ^ {2}} \sum_ {l = 0} ^ {\infty} (2 l + 1) P _ {\mathrm {a b s}} (l, E), \tag {4}
$$

where

$$
P _ {\mathrm {a b s}} (l, E) = 1 - \left| S _ {l} (E) \right| ^ {2} \tag {5}
$$

is the absorption probability at the $l ^ { \mathrm { t h } }$ -partial wave, which is given by the deviation of the partial-wave component of the S-matrix, $S _ { l } ( E )$ , from the unitary behaviour.

The absorption cross section can also be given in terms of the expectation value of the imaginary potential, through the expression

$$
\sigma_ {\mathrm {a b s}} (E) = - \frac {1}{| A | ^ {2}} \frac {k}{E} \left<   \psi^ {(+)} \mid W (r) \mid \psi^ {(+)} \right > , \qquad (6)
$$

where $A$ is the normalization constant of the scattering wave function, $\psi ^ { ( + ) } ( \mathbf { r } )$ . Eq. (6), can be easily derived from the continuity equation for the Schr¨odinger equation with the complex potential [20]. Carrying out the partial-wave expansion of Eq. (6), the reaction cross section takes the form of Eq. (4), with the absorption probabilities of Eq. (5) given by the radial integral

$$
P _ {\mathrm {a b s}} (l, E) = - \frac {4 k}{E} \int_ {0} ^ {\infty} d r W (r) | u _ {l} (k, r) | ^ {2}, \qquad (7)
$$

with $u _ { l } ( k , r )$ standing for the radial wave function of the $l ^ { \mathrm { t h } }$ partial wave, in a collision with wave number $k \mathbf { \Psi } =$ $\sqrt { 2 \mu E } / \hbar$ , where $\mu$ stands for the reduced mass.

The relation between $\sigma _ { \mathrm { a b s } } ( E )$ and the observable cross sections depends on the nature of the imaginary potential. When it simulates the influence of fusion plus direct reactions ( $W ( r ) = W ^ { \mathrm { { R } } } ( r )$ ), $\sigma _ { \mathrm { a b s } } ( E )$ corresponds to the total reaction cross section. On the other hand, if one is interested in the fusion cross section, one should use a strong imaginary potential with a short-range. However, this does not guarantee fusion. For CN formation, the projectile and the target must remain in close proximity for a long time, long enough for the full thermalization of the excitation energy. This happens when the system is caught inside a pocked of the effective potential,

$$
V _ {l} (r) = V (r) + \frac {\hbar^ {2}}{2 \mu r ^ {2}} l (l + 1), \qquad (8)
$$

which appears in the radial equation. Thus, the fusion cross section should be written,

$$
\sigma_ {\mathrm {F}} (E) = \frac {\pi}{k ^ {2}} \sum_ {l = 0} ^ {\infty} (2 l + 1) P _ {\mathrm {F}} (l, E), \tag {9}
$$

with

$$
P _ {\mathrm {F}} (l, E) = P _ {\mathrm {a b s}} (l, E) \times P _ {\mathrm {C N}} (l, E). \tag {10}
$$

Above, $P _ { \mathrm { C N } } \left( l , E \right)$ is the probability of CN formation, after the system enters the strong absorption region. For low partial waves and near-barrier energies, this probability is very close to one. The situation is different for partial waves above the critical angular momentum, $l _ { \mathrm { c r } }$ . This angular momentum is defined as the highest $\it l$ -value for which the potential $V _ { l } ( r )$ exhibits a pocket. Above $l _ { \mathrm { c r } }$ , $V _ { l } ( r )$ is strongly repulsive (dominated by the centrifugal term), decreasing monotonically with $r$ . In this way, the system may enter the strong absorption region but it stays there for a short time, orders of magnitude shorter than that required for thermalization and CN formation. In this situation, the absorption corresponds to inelastic scattering, transfer or pre-equilibrium reactions, but definitely not to fusion. Therefore, partial-wave above $\boldsymbol { l } _ { \mathrm { c r } }$ should not be included in the calculation of fusion. This is is achieved by setting,

$$
\begin{array}{l} \mathcal {P} _ {\mathrm {C N}} (l, E) = 1, \quad \text {f o r} l <   l _ {\mathrm {c r}} \\ = 0, \quad \text {f o r} \geq l _ {\mathrm {c r}}. \tag {11} \\ \end{array}
$$

There is an alternative to the use of a complex potential in the calculation of fusion cross sections. One can keep the potential real and adopt ingoing wave boundary conditions (IWBC) [1, 21, 22, 23] for the radial wave functions at the bottom of the pocked of $V _ { l } ( r )$ , $R _ { \mathrm { i n } }$ . The wave functions and their derivatives at $r = R _ { \mathrm { i n } }$ are then evaluated within the WKB approximation, and the radial equations are numerically integrated, from $R _ { \mathrm { i n } }$ to the matching radius. In an optical model calculation with a strong and short range imaginary potential, the incident waves reaching the inner region of the barrier are completely absorbed, so that there is no reflected wave coming out. In this way, radial wave functions obtained with $W ^ { \mathrm { F } } ( r )$ are expected to be equivalent to those of a real potential with IWBC, and the same happens with the corresponding components of the S-matrix, $S _ { l } ( E )$ .

# The WKB approximation and the Hill-Wheeler transmission coefficient

The absorption probability in Eq. (5), $P _ { \mathrm { a b s } } ( l , E )$ , acquires a simple form in the WKB (Wentzel, Kramers, and Brillouin) approximation, where the radial wave functions are written in terms of the local wave numbers, $k _ { l } ( r )$ , defined as,

$$
\kappa_ {l} (r) = \frac {1}{\hbar} \sqrt {V _ {l} (r) + i W (r) - E}. \tag {12}
$$

However, the explicit presence of the imaginary potential in $k _ { l } ( r )$ leads to extra difficulties in the calculation, as one has to deal with complex turning points (this will become clear in Eqs. (14) and (15)). Although, in principle, such calculation can be performed by resorting to the method of complex angular momenta (through the requirement

that the imaginary part of the turning point is identically zero), practical usage of the results is limited.

The situation is better in calculations of fusion cross sections, where the imaginary potential is very strong but has a short-range. In this case, it absorbs completely the current that reaches the inner region of the barrier, but it is negligible elsewhere. It is still simpler in IWBC calculations, which are based on real potentials. In this case, the absorption probability at the partial-wave $l \left( \leq l _ { \mathrm { c r } } \right)$ is equal to the transmission coefficient of the incident wave through the barrier of $V _ { l } ( r )$ , $T ( l , E )$ , namely

$$
P _ {\mathrm {a b s}} (l, E) = P _ {\mathrm {F}} (l, E) \simeq T (l, E). \tag {13}
$$

Within Kemble’s improved version [24] of the WKB approximation, the transmission coefficient is given by the expression

$$
T (l, E) \simeq T ^ {\mathrm {W K B}} (l, E) = \frac {1}{1 + \exp \left[ 2 \Phi_ {l} ^ {\mathrm {W K B}} (E) \right]}, \tag {14}
$$

where $\phi _ { l } ^ { \mathrm { w e s } } ( E )$ is the integral of the local wave number evaluated along the classically forbidden region,

$$
\Phi_ {l} ^ {\mathrm {W K B}} (E) = \int_ {r _ {i}} ^ {r _ {e}} \kappa_ {l} (r) d r, \tag {15}
$$

with $r _ { i }$ and $r _ { e }$ standing respectively for the internal and external classical turning points for the potential $V _ { l } ( r )$ . These turning points are real at sub-barrier energies but they become complex above the barrier. Kemble argued that this problem could be solved through an analytical continuation of the radial variable to the complex plane. He pointed out that in the case of a parabolic barrier, discussed in the next sub-section, the integral of Eq. (15) is given by an analytical expression and this expression is valid for any collision energy, below or above the barrier. Recently, the analytical continuation of the radial variable for typical heavy-ion potentials was discussed, and the applicability of the Wong formula (see section 2.1) was extended to above-barrier energies [25, 26].

Hill and Wheeler studied the transmission through the parabolic barrier

$$
V (r) = V _ {\mathrm {B}} - \frac {1}{2} \mu \omega^ {2} \left(r - R _ {\mathrm {B}}\right) ^ {2}. \tag {16}
$$

In this case, the transmission coefficient can be evaluated exactly. The result, known as the Hill-Wheeler transmission factor, is

$$
T (E) = \frac {1}{1 + \exp \left[ 2 \pi \left(V _ {\mathrm {B}} - E\right) / \hbar \omega \right]}. \tag {17}
$$

Approximate expression for heavy-ion fusion cross sections can be obtained by taking the Hill-Wheeler transmission function to obtain the fusion probabilities. For this purpose, the effective $\it l$ -dependent potentials are approximated by a parabola, as

$$
V _ {l} (r) = B _ {l} - \frac {1}{2} \mu \omega_ {l} ^ {2} \left(r - R _ {l}\right) ^ {2}, \tag {18}
$$

where $B _ { l }$ , $R _ { l }$ and $\hbar \omega _ { l }$ are respectively the height, radius and curvature parameter of the barrier for the $l ^ { \mathrm { t h } }$ -partial wave. The corresponding transmission coefficients are, then, given by the expression,

$$
T ^ {\mathrm {H W}} (l, E) = \frac {1}{1 + \exp \left[ 2 \pi \left(B _ {l} - E\right) / \hbar \omega_ {l} \right]}. \tag {19}
$$

If the imaginary potential has a short range, as the case of $W ^ { \mathrm { F } } ( r )$ in Fig. 1, absorption is equivalent to fusion and the fusion probabilities should be very close to the corresponding transmission coefficients. However, this assumption is meaningless for partial-waves above $l _ { \mathrm { c r } }$ , where the potential $V _ { l } ( r )$ decreases monotonically as $r$ increases. To deal with this problem, one truncates the partial-wave series for $\sigma _ { \mathrm { { F } } }$ at $\mathit { l } \ = \ l _ { \mathrm { c r } }$ . In this way, the WKB approximation for $\sigma _ { \mathrm { { F } } }$ contains the implicit assumption that the factor $P _ { \mathrm { C N } } ( l , E )$ of Eq. (10) is equal to one below $l _ { \mathrm { c r } }$ and zero otherwise. The fusion cross section in the WKB approximation can be written,

$$
\sigma_ {\mathrm {F}} (E) = \frac {\pi}{k ^ {2}} \sum_ {l = 0} ^ {l _ {\mathrm {c r}}} (2 l + 1) T ^ {\mathrm {H W}} (l, E). \tag {20}
$$

The quality of the parabolic approximation for the potential barriers depends on the collision energy and on the mass of the system. It is reasonable at near-barrier energies but becomes very inaccurate at energies well below the Coulomb barrier. It works fairly well for heavy systems even at collision energies several MeV below the Coulomb barrier. However, this approximation is quite poor for light heavy ions [1]. A common practice that leads to a very accurate fusion cross section is to use Kemble’s transmission coefficients (Eq. (14)) below the Coulomb barrier and the Hill-Wheeler transmission factors (Eq. (19)) above.

# Poisson series and the Wong formula

The sum of partial waves giving the fusion cross section can be transformed into a rapidly converging series of integrals. According to the Poisson formula, we can write

$$
\begin{array}{l} \sigma_ {\mathrm {F}} (E) = \frac {\pi}{k ^ {2}} \sum_ {l = 0} ^ {\infty} (2 l + 1) T (l, E) \\ = \frac {2 \pi}{k ^ {2}} \sum_ {m = 0, \pm 1, \dots} (-) ^ {m} \int \lambda T (\lambda , E) e ^ {2 i \pi m \lambda} d \lambda , \tag {21} \\ \end{array}
$$

where

$$
\lambda = l + 1 / 2 \quad \text {a n d} \quad T _ {l} (E) = T \left(\lambda , E\right).
$$

The sum over $m$ converges very rapidly, so that, in most cases, it is enough to consider the leading term, with $m = 0$ .

Wong [27] obtained a very useful expression for the fusion cross section by considering only the $m = 0$ term of the Poisson series and making additional approximations

on the $\it l$ -dependent effective potential. First, he adopted the parabolic approximations of Eq. (18). Next, he neglected the $\it l$ -dependences of the $R _ { l }$ and $\hbar \omega _ { l }$ and made the approximations,

$$
R _ {l} = R _ {l = 0} \equiv R _ {\mathrm {B}}
$$

$$
\hbar \omega_ {l} = \hbar \omega_ {l = 0} \equiv \hbar \omega ,
$$

$$
B _ {\lambda} \simeq V _ {\mathrm {B}} + \frac {\hbar^ {2} \lambda^ {2}}{2 \mu R _ {\mathrm {B}} ^ {2}}. \tag {22}
$$

With these approximations the integral over $\lambda$ can be carried out analytically and one gets the so-called Wong cross section [27]

$$
\sigma^ {\mathrm {w}} (E) = \frac {\hbar \omega R _ {\mathrm {B}} ^ {2}}{2 E} \ln \left[ 1 + \exp \left(\frac {2 \pi}{\hbar \omega} (E - V _ {\mathrm {B}})\right) \right]. \tag {23}
$$

At low enough sub-barrier energies $E \ll V _ { \mathrm { B } } - \hbar \omega ,$ ), Eq. (23) may be approximated by the simpler expression,

$$
\sigma_ {\mathrm {F}} (E) \simeq \frac {\hbar \omega R _ {\mathrm {B}} ^ {2}}{2 E} \exp \left[ - 2 \pi \frac {| E - V _ {\mathrm {B}} |}{\hbar \omega} \right]. \tag {24}
$$

A simpler approximation for the Wong formula can also be derived at energies few MeV above the Coulomb barrier $( E \gtrsim V _ { \mathrm { B } } + \hbar \omega )$ . In this energy region one can neglect the unity within the square bracket of Eq. (23), and it becomes

$$
\sigma_ {\mathrm {F}} (E) \simeq \sigma_ {\text {g e o}} \left[ 1 - \frac {V _ {\mathrm {B}}}{E} \right], \tag {25}
$$

where

$$
\sigma_ {\mathrm {g e o}} = \pi R _ {\mathrm {B}} ^ {2} \tag {26}
$$

is the geometric cross section.

Wong’s formula is quite accurate in collisions of heavy systems at near-barrier energies (say $V _ { \mathrm { B } } + 5 \mathrm { M e V } \geq E \geq$ $V _ { \mathrm { B } } - 5$ MeV). However, it is a poor approximation in collisions of light systems, both below and above the Coulomb barrier. The problem at sub-barrier energies is that the barrier for light systems is highly asymmetric, whereas the parabolic approximation is symmetric. The tail of $V ( r )$ falls off slowly, as the Coulomb potential $( \sim 1 / r$ ), while the parabola goes to zero much faster. Thus, the external turning points for the two potentials become very different as the energy decreases, with $r _ { \mathrm { e } }$ for the parabola being progressively smaller. In this way, the function $\varPhi _ { l } ^ { \mathrm { w e s } } ( E )$ for the parabola is too small, and the transmission coefficient of Eq. (14) is badly overestimated. For example, the fusion cross section for the $\mathrm { ^ 6 L i ~ + ~ ^ { 1 2 } C }$ system predicted by the Wong formula at $E = 1$ MeV ( $V _ { \mathrm { B } } \simeq 3$ MeV) is more than two orders of magnitude larger than the value obtained by a quantum mechanical calculations (see Fig. 26 of Ref. [1]). The inaccuracy of the Wong formula above the Coulomb barrier has another origin. Contrary to what was assumed in the derivation of the Wong formula, the parameters $R _ { l }$ and $\omega _ { l }$ for light systems have a strong $\it l$ - dependence.

![](images/ff5cbff9ed2ea24994620d36b0220f70e20b82bd39341d77c3efbecb2498be38.jpg)

![](images/043b1901e6df1c963676762e1b953964443b35a52c5e5d167f68897f77c6575f.jpg)  
Fig. 2. (Color on line) Fusion cross sections for the $^ { 1 2 } \mathrm { C } \mathrm { ~ + ~ }$ 12C system. Panel (a): Comparison of the energy-dependent Wong formula (red dot-dashed curve) with the standard Wong formula (dashed curve); Panel (b): Comparison of the energydependent Wong formula with the exact cross section, calculated by full quantum mechanics (solid line). The figure was taken from Ref. [28].

Rowley and Hagino [28] have shown that the accuracy of the Wong formula for light systems at above-barrier energies is significantly improved if one replaces the s-wave barrier parameters in Eq. (23) by the barrier parameters associated with the grazing angular momentum, $R _ { E }$ , $\hbar \omega _ { E }$ and $V _ { E }$ . This is illustrated in Fig. 2. Panel (a) shows a comparison of the standard Wong cross section with the one obtained using the parameters associated with the grazing angular momentum at the corresponding collision energy, $E$ . One observes that the two cross sections become progressively different as the energy increases. At 40 MeV, the standard Wong cross section is about 3/2 of the one obtained with the energy dependent parameters.

Panel (b) shows a comparison of the energy-dependent Wong formula with exact results of full quantum mechanics. One concludes that the improved Wong formula of Ref. [28] is a very good approximation to the quantum mechanical cross section.

Usually, higher order terms of the Poisson series give negligible contributions to the fusion cross section. The situation is slightly different in the case of identical nuclei. These contributions are responsible for the weak oscillations in the exact fusion cross section of the $\mathrm { ^ { 1 2 } C + ^ { 1 2 } C }$ system (solid line on panel (b) of Fig. 2). Adding these contributions to the energy-dependent Wong formula, Rowley

and Hagino were able to reproduce the quantum mechanical cross section of Fig. 2 with great accuracy [28]. Recently, the study of Rowley and Hagino has been extended to collisions of identical nuclei with arbitrary spin [29].

# The Wong formula at $E > E _ { \mathrm { c r } }$

Eq. (25) indicates that the cross section tends to a constant value as the energy goes to infinity, This is not consistent with the prediction of quantum mechanics in potential scattering, where the cross section goes to zero in the $E \to \infty$ limit. The origin of this discrepancy is that Wong assumes that the radii and the shapes of the barriers of the effective potentials are independent of $\it l$ . In this way the partial-wave series always gets important contributions from waves around the grazing angular momentum, given by the condition $V _ { l _ { \mathrm { g } } } ( R _ { l } ) = E$ . The situation is quite different for the actual potential. In the WKB calculation, the fusion probability vanishes above $l _ { \mathrm { c r } }$ , since $V _ { l } ( r )$ has no barrier. On the other hand, in the quantum mechanical calculation, the partial-wave series of Eq. (9) is limited by the factor $P _ { \mathrm { C N } } ( l , E )$ , that vanishes above $l _ { \mathrm { c r } }$ . Owing to the repulsive nature of the potential, the collision time is not long enough to allow the formation of an equilibrated CN. Thus, both in quantum mechanical calculation and in the WKB approximation with the actual effective potential, the partial-wave series is truncated at $l = l _ { \mathrm { c r } }$ . At high enough energies, all non-vanishing fusion probabilities are equal to one and the partial-wave series can be summed analytically. This establishes a new energy regime, where the fusion cross section decreases monotonically with $E$ , according to the expression,

$$
\sigma_ {\mathrm {F}} (E) \simeq \sigma_ {0} \times \frac {E _ {\mathrm {c r}}}{E}, \tag {27}
$$

with

$$
\sigma_ {0} = \frac {\pi \hbar^ {2} \left(l _ {\mathrm {c r}} + 1\right) ^ {2}}{2 \mu E _ {\mathrm {c r}}}. \tag {28}
$$

# Wong formula vs. $\sigma _ { \mathrm { R } }$

The derivation of the Wong formula is based on the assumption that the absorption probability is equal to the transmission coefficient through the barrier of the real potential of Eq. (8). This assumption is consistent with the IWBC or calculations with a very strong imaginary potential acting exclusively in the inner region of the barrier. Thus, Wong’s formula is an approximation for the fusion cross section. It is expected to be a poor approximation for the total reaction cross section, since it may get important contributions from direct reactions, which correspond to absorption in the barrier region and beyond. Nevertheless, in Wong’s original paper [27] and in other publications it has been taken as an approximation for $\sigma _ { \mathrm { R } }$ . In such cases, $R _ { \mathrm { B } }$ , $V _ { \mathrm { B } }$ and $\hbar \omega$ should be interpreted as effective quantities, rather than the parameters extracted from the parabolic fit of the real potential.

# 2.2 The semiclassical scattering amplitude

The partial-wave expansion of the nuclear part of the scattering amplitude is given by [20]

$$
f _ {\mathrm {N}} (\theta) = \frac {1}{2 i k} \sum_ {l = 0} ^ {\infty} (2 l + 1) P _ {l} (\cos \theta) e ^ {2 i \sigma_ {l}} \left[ | S _ {\mathrm {N}} (l, E) | e ^ {2 i \delta_ {l}} - 1 \right], \tag {29}
$$

where $\sigma _ { l }$ and $\delta _ { l }$ are respectively the Coulomb and the nuclear phase-shifts at the $l ^ { \mathrm { t h } }$ partial-wave, $\vert S _ { \mathrm { N } } ( l , E ) \vert$ is the modulus of the nuclear S-matrix and $P _ { l } ( \cos \theta )$ is the Legendre polynomial. The semiclassical scattering amplitude is obtained through the following approximations.

1. use the Poisson series to evaluate the partial-wave sum;   
2. evaluate nuclear phase-shifts within the WKB approximation;   
3. use Legendre polynomials of continuous order (λ) and adopt the large $\lambda$ approximation:

$$
\begin{array}{l} P _ {l} (\cos \theta) \longrightarrow P (\lambda , \cos \theta) \simeq \left(\frac {1}{2 \pi \lambda \sin \theta}\right) ^ {1 / 2} \\ \left[ e ^ {i (\lambda \theta - \pi / 4)} + e ^ {- i (\lambda \theta - \pi / 4)} \right]; \tag {30} \\ \end{array}
$$

4. evaluate integrals using the stationary phase approximation.

With the above approximations, one can infer several characteristic features of heavy-ion scattering. The two terms within square brackets in Eq. (30) give rise to a near and a far component of the scattering amplitude and to near-far and rainbow oscillations of the cross section in heavy-ion elastic scattering.

The Fresnel diffraction formula and the quarter point recipe

Heavy-ion scattering is dominated by Coulomb repulsion and strong absorption. This leads to the sharp cut-off model (black disk approximation) for charged particle scattering at low energies. In this model, nuclear phase shifts are neglected and the $\it l$ -projected components of the Smatrix are given by,

$$
S (l) \equiv | S _ {\mathrm {N}} (l, E) | e ^ {2 i (\sigma_ {l} + \delta_ {l})} \rightarrow S (\lambda) \simeq \mathcal {H} (\lambda - \bar {\Lambda}) e ^ {2 i \sigma (\lambda)}. \tag {31}
$$

Above, $\varLambda$ is the grazing angular momentum and

$$
\begin{array}{l} \mathcal {H} (\lambda - \bar {\Lambda}) = 1, \text {f o r} \lambda \geq \bar {\Lambda} (32) \\ = 0, \text {f o r} \lambda <   \bar {\Lambda} (33) \\ \end{array}
$$

is the Heaviside step function.

Within the sharp cut-off model of the semiclassical scattering amplitude, the elastic cross section is dominated by the interference between a refractive Coulomb wave at $\lambda > \Lambda$ and a diffractive wave for smaller values of $\lambda$ . Frahn [30, 31] demonstrated that the ratio of the

![](images/d98e821c0019a706583bf2a3c37b5772bded13199dba7f352a63cc7e7ec39ae6.jpg)  
Fig. 3. Fresnel diffraction within the sharp cut-off approximation. Figure from Ref. [20].

elastic scattering cross section with respect to the corresponding Rutherford cross section, which will be denoted by $\sigma ( \theta ) / \sigma _ { \mathrm { { C } } } ( \theta )$ , is given by the Fresnel diffraction formula

$$
\frac {\sigma (\theta)}{\sigma_ {C} (\theta)} = \frac {1}{2} \left[ \left(\frac {1}{2} - C (w)\right) ^ {2} + \left(\frac {1}{2} - S (w)\right) ^ {2} \right], \tag {34}
$$

where $C ( w )$ and $S ( w )$ are the Fresnel integrals given by,

$$
C (w) = \int_ {0} ^ {W} d \omega \cos \left(\frac {\pi}{2} \omega^ {2}\right) \tag {35}
$$

and

$$
S (W) = \int_ {0} ^ {W} d \omega \sin \left(\frac {\pi}{2} \omega^ {2}\right). \tag {36}
$$

The argument of the Fresnel integrals is

$$
w = \sqrt {\frac {2 \eta}{\pi}} \left[ \frac {\sin \left(\frac {\theta - \bar {\Theta}}{2}\right)}{\sin \frac {\bar {\Theta}}{2}} \right], \tag {37}
$$

where $\eta$ is the Sommerfeld parameter, $\theta$ is the scattering angle and $\Theta$ is the grazing angle.

An important property of the Fresnel integrals is that they vanish at $W = 0$ (this can be immediately checked in Eqs. (35) and (36)). This value of $W$ is reached at the scattering angle $\theta = \Theta$ . Using these results in Eq. (34), the ratio of the cross sections at the grazing angle becomes

$$
\frac {\sigma (\bar {\Theta})}{\sigma_ {\mathrm {C}} (\bar {\Theta})} = \frac {1}{4}. \tag {38}
$$

To emphasize this property, the grazing angle is denoted

$$
\bar {\Theta} = \theta_ {1 / 4}.
$$

An important consequence of Eq. (38) is that the grazing angle can be determined directly from the scattering

data: $\Theta$ is the angle where $\sigma ( \theta ) / \sigma \mathrm { c } ( \theta )$ reaches the value $1 / 4$ . Having $\Theta$ , one can determine the argument W for each value of $\theta$ , and evaluate the Fresnel integrals. Then, inserting them into Eq. (34), one obtains $\sigma ( \theta ) / \sigma _ { \mathrm { { C } } } ( \theta )$ , within the sharp cut-off approximation for the S-matrix. This result is known as Frahn’s Fresnel diffraction formula for the angular distribution.

An illustration of this procedure is given in Fig. 3, for the $\mathrm { ^ { 1 6 } O \ + \ ^ { 2 0 8 } P b }$ collision. This example was discussed in detail by Frahn [30]. In this case, the grazing angle is $\theta _ { 1 / 4 } = 4 0 . 9 ^ { \mathrm { o } }$ , $\varLambda = 8 6$ and the Sommerfeld parameter is $\eta = 3 2 . 0 5$ . Frahn [30] has shown that the predictions of the sharp cut-off model are in qualitative agreement with the data. It predicts oscillations at low scattering angles (illuminated region) with increasing amplitudes, which ends in a pronounced maximum, followed by a rapid decrease of $\sigma ( \theta ) / \sigma _ { \mathrm { { C } } } ( \theta )$ as $\theta$ increases (shadow region). However, the Fresnel diffraction formula completely ignores the effects of nuclear refraction. These effects are responsible for other kind of oscillations, like near-far interference and the rainbow. One should stress that rainbow scattering with a unitary S-matrix leads also to the typical pattern of heavyion scattering, exhibited in Fig. 3. Quantum mechanical potential scattering calculations with complex potentials, which include both refractive and diffractive effects of the nuclear potential, lead to more quantitative prediction of the elastic angular distributions.

The sharp cut-off model can also be used to make qualitative prediction of total reaction cross sections. From the experimental $\sigma ( \theta ) / \sigma _ { \mathrm { { C } } } ( \theta )$ ratio at a given collision energy, $E$ , one determines the grazing angle. Then, one finds the grazing angular momentum from the Rutherford trajectory by the equation,

$$
\bar {\Lambda} (E) = \eta \cot \left(\frac {\theta_ {1 / 4}}{2}\right). \tag {39}
$$

Next, we evaluate the total reaction cross section taking Eq. (4) and replacing the partial-wave sum by an integral over $\lambda$ . This corresponds to taking only the $m = 0$ term in the Poisson series (see e.g. Ref. [20]). One gets

$$
\sigma_ {\mathrm {R}} (E) = \frac {2 \pi}{k ^ {2}} \int d \lambda \lambda P (\lambda , E). \tag {40}
$$

Using the sharp cut-off model, the absorption (reaction) probability of Eq. (5) becomes

$$
P _ {\mathrm {a b s}} (\lambda , E) = 1 - \mathcal {H} (\lambda - \bar {\Lambda} _ {(\mathrm {E})}) = \mathcal {H} (\bar {\Lambda} _ {(\mathrm {E})} - \lambda). \tag {41}
$$

Then, the integral of Eq. (40) can be immediately evaluated and one gets

$$
\sigma_ {\mathrm {R}} = \frac {\pi}{k ^ {2}} \bar {\Lambda} ^ {2} (E). \tag {42}
$$

It is worth mentioning that at higher energies, the Coulomb effect becomes small and the angular distribution corresponding to the black disk or sharp cutoff model

approximates the Fraunhoffer diffraction. The grazing angular momentum can still be obtained from the angular period of oscillations, $\varDelta \theta = \pi / \bar { A }$ .

# 2.3 The Generalized Optical Theorem and the Sum of Differences Method

The Optical Theorem is an important result in scattering theory and it expresses unitarity in a useful mathematical form. For uncharged particle scattering, the theorem states that the total (angle integrated) elastic scattering cross section is proportional to the imaginary part of the elastic amplitude evaluated at $\theta = 0$ . In potential scattering from a real potential, one has

$$
\int \frac {d \sigma_ {\mathrm {e l}} (\theta)}{d \Omega} d \Omega = \frac {4 \pi}{k} \operatorname {I m} \left\{f _ {\mathrm {e l}} (\theta = 0) \right\}. \tag {43}
$$

When absorption is present, the above becomes the Generalized Optical Theorem (GOT),

$$
\int \frac {d \sigma_ {\mathrm {e l}} (\theta)}{d \Omega} d \Omega + \sigma_ {\mathrm {R}} = \frac {4 \pi}{k} \operatorname {I m} \left\{f _ {\mathrm {e l}} (\theta = 0) \right\}. \tag {44}
$$

For charged particles, the GOT needs to be modified to cope with the point Coulomb singularity. The integral in Eqs. (43) and (44) is divergent. First, the scattering amplitude is written as

$$
f _ {\mathrm {e l}} (\theta) = f _ {\mathrm {C}} (\theta) + f _ {\mathrm {N}} (\theta), \tag {45}
$$

where $f _ { \mathrm { C } } ( \boldsymbol { \theta } )$ is the Coulomb scattering amplitude for two point charges, and $f _ { \mathrm { N } } ( \theta )$ is a correction arising from the short-range nuclear potential. The former is given by the analytical expression,

$$
\begin{array}{l} f _ {\mathrm {c}} (\theta) = \frac {\eta}{2 k \sin^ {2} (\theta / 2)} e ^ {i [ 2 \sigma_ {0} + \pi - 2 \eta \ln (\sin \theta / 2) ]} \\ = - \frac {\eta}{k} 2 ^ {i \eta} \frac {e ^ {2 i \sigma_ {0}}}{(1 - \cos \theta) ^ {i \eta + 1}}, \tag {46} \\ \end{array}
$$

and the latter is given by the partial-wave expansion2,

$$
f _ {\mathrm {N}} (\theta) = \frac {1}{2 i k} \sum_ {l = 0} ^ {\infty} (2 l + 1) e ^ {2 i \sigma_ {l}} [ S _ {\mathrm {N}} (l) - 1 ] P _ {l} (\cos \theta). \tag {47}
$$

To get rid of the singularity, the GOT for charged particles is expressed in terms of the difference

$$
\sigma_ {\mathrm {S O D}} \left(\theta_ {0}\right) = 2 \pi \int_ {\theta_ {0}} ^ {\pi} \left[ \frac {d \sigma_ {\text {R u t h}} (\theta)}{d \Omega} - \frac {d \sigma_ {\mathrm {e l}} (\theta)}{d \Omega} \right] \sin \theta d \theta , \tag {48}
$$

where $\theta _ { 0 }$ is a very small angle. The cross section difference, $\sigma _ { \mathrm { { S O D } } } \left( \theta _ { 0 } \right)$ , is called the sum-of-difference (SOD) cross section. The replacement $\theta = 0  \theta = \theta _ { 0 }$ in the lower limit

![](images/e646f45b3266e0a75ba93aae94cbc889b8b4881ef18e2b6eead2a474cd74cec9.jpg)  
Fig. 4. The SOD cross section for the $^ { 1 6 }$ O + 28Si system at $E _ { \mathrm { c . m . } } = 3 5$ MeV. The solid line and the dashed lines correspond respectively to the exact result of Eq. (48), and the approximation of Eq. (51). The calculations adopted the optical potential of Shkolnik et al. [39] (figure taken from Ref. [36]).

of the integration is justified by the fact that, in a realistic collision, the Coulomb potential is screened.

Using the explicit forms of the elastic and the Coulomb cross sections, namely

$$
\frac {d \sigma_ {\mathrm {e l}} (\theta)}{d \Omega} = \left| f _ {\mathrm {C}} (\theta) + f _ {\mathrm {N}} (\theta) \right| ^ {2}; \quad \frac {d \sigma_ {\mathrm {C}} (\theta)}{d \Omega} = \left| f _ {\mathrm {C}} (\theta) \right| ^ {2}, \tag {49}
$$

Eq. (48) becomes

$$
\begin{array}{l} \sigma_ {\mathrm {S O D}} (\theta_ {0}) = - 2 \pi \int_ {\theta_ {0}} ^ {\pi} | f _ {\mathrm {N}} (\theta) | ^ {2} \sin \theta d \theta \\ - 4 \pi \int_ {\theta_ {0}} ^ {\pi} \operatorname {R e} \left\{f _ {\mathrm {C}} ^ {*} (\theta) \cdot f _ {\mathrm {N}} (\theta) \right\} \sin \theta d \theta . \tag {50} \\ \end{array}
$$

The above cross section has been discussed by several author [32, 33, 34, 35, 36, 37, 38]. Marty evaluated the integrals of Eq. (50) and obtained the SOD cross section,

$$
\begin{array}{l} \sigma_ {\mathrm {S O D}} (\theta_ {0}) = \sigma_ {\mathrm {R}} - \frac {4 \pi}{k} | f _ {\mathrm {N}} (0) | \\ \times \sin \left[ \arg \left\{f _ {\mathrm {N}} (0) \right\} - 2 \sigma_ {0} + \eta \ln \left\{\sin^ {2} \theta_ {0} / 2 \right\} \right] + O \left(\theta_ {0} ^ {2}\right). \tag {51} \\ \end{array}
$$

Above, $\eta$ is the Sommerfeld parameter, $\sigma _ { 0 }$ is the s-wave Coulomb phase shift, and $O \left( \theta _ { 0 } ^ { 2 } \right)$ is a correction3, that becomes negligible when $\theta _ { 0 }$ is a very forward angle.

The accuracy of Eq. (51) is illustrated in Fig. 4, where the approximate cross section of Eq. (51) and the exact result of Eq. (48) are compared. In this example, taken from Ref. [36], $\sigma _ { \mathrm { e l } } ( \theta )$ and $f _ { \mathrm { N } } ( 0 )$ were calculated with the optical potential of Ref. [39]. Clearly, the approximation is quite accurate for small values of $\theta _ { 0 }$ . The oscillatory behaviour of $\sigma _ { \mathrm { { S O D } } } ( \theta _ { 0 } )$ at forward angles provide two important pieces of information. First, the total reaction cross

section is given by the SOD cross section averaged over a period of oscillation in the low $\theta _ { 0 }$ region. Thus, the total reaction cross section can be determined from accurate measurements of the elastic cross section at forward angles. The use of this technique is discussed in sect. 5.2.

The second important consequence of Eq. (51) is that the modulus of $f _ { \mathrm { N } } ( 0 )$ can be extracted from the period of oscillation. This equation has been fully analysed in the context of heavy-ions collisions [35, 36, 37, 40, 41]. In most of the applications of Eq.(51), the aim was to study the oscillations in the nuclear amplitude at forward angles, which can be traced to forward glory effects. The existence of a non-zero value of the impact parameter, $b _ { \mathrm { g l } }$ , at which the classical deflection angle defined through the relation,

$$
\Theta (l) = 2 \frac {\delta (\sigma_ {l} + \delta_ {l})}{\delta l}.
$$

satisfies the condition $\Theta ( b _ { \mathrm { g l } } ) = 0$ , corresponds to forward glory. Under this condition, the scattering amplitude at forward angles is enhanced and with conspicuous oscillations. In fact, this nuclear amplitude, $f _ { \mathrm { N } } ( \boldsymbol { \theta } )$ , in the vicinity of the forward glory angle ( $\theta = 0 ^ { o }$ ) is given by the product $A ( \theta ) J _ { 0 } ( \lambda _ { \mathrm { g l } } \theta )$ , where $J _ { 0 }$ is the Bessel function of order zero and $A ( \theta )$ is a smooth function of $\theta$ . Thus the SOD method, in the presence of forward glory, would supply a reaction cross section with greatly enhanced energy oscillations [35, 36, 37]. Besides this, the forward glory effect can be used to learn more about the nuclear interaction at the surface region, complementary to the information obtained from the study of nuclear rainbow scattering, as emphasised in Ref. [35].

# 2.4 Comparison of Quantum mechanical cross sections with the Wong and the quarter-point approximations

In potential scattering, fusion and direct reactions are taken into account through the inclusion of an imaginary part in the nucleus-nucleus potential. This procedure leads to reasonable predictions for $\sigma _ { \mathrm { { F } } }$ and $\sigma _ { \mathrm { R } }$ . These cross sections are calculated by Eq. (4), with absorption probabilities expressed in terms of the unitarity defect of the S-matrix (Eq. (5)), or with the radial integrals involving the imaginary potential (Eq. (7)). However, calculations of fusion and of total reaction cross sections must use different imaginary potentials, as discussed in section 2. In the previous sections we discussed also the Wong formula and the quarter-point recipe, where the cross sections are approximated by simple analytical expressions. Now we discuss the validity of these approximations.

As an example, let us consider the potential model for the $^ { 1 6 }$ O − 208Pb collision, adopting the S˜ao Paulo Potential [15, 16] for the real part of the nucleus-nucleus potential. In calculations of $\sigma _ { \mathrm { { F } } }$ , the imaginary potential is given by a short range WS function with the parameters: $W _ { 0 } ~ = ~ 5 0$ MeV, $r _ { 0 i } ~ = ~ 1 . 0$ fm and $a _ { i } ~ = ~ 0 . 2$ fm. In calculations of $\sigma _ { \mathrm { R } }$ , the imaginary part of the potential

![](images/6fdb64ab4d3871588fd10bd617c3500f1c61443b1a588bbeb2f10e5d8275a9f0.jpg)  
Fig. 5. (Color on line) Quantum mechanical total reaction (thick blue solid line) and fusion (thin solid green line) cross sections, in comparison with the Wong cross section of Eq. (22) (green dot-dashed line with open circles) and the quarter point recipe cross section of Eq. (42) (blue dashed line).

is proportional to its real part, $W ( r ) = 0 . 7 8 ~ V ( r )$ $V ( r )$ . This prescription has been successfully used to describe the average behaviour of total reaction cross sections of many systems [17]. In Fig 5, the two quantum mechanical cross sections are shown in comparison with the ones obtained using the Wong formula and the quarter point recipe. The quarter point cross section (blue dashed line) was obtained by Eqs. (42) and (39), using in the latter the quarter point angle extracted from angular distributions of the quantum mechanical calculations, using $W ^ { \mathrm { R } } ( r )$ . Therefore, it is should be compared to $\sigma _ { \mathrm { R } }$ . We find that it underestimates the quantum mechanical cross section systematically. The difference between the two cross section is roughly constant, except at energies just above the barrier, where this approximation cannot be applied. In this region, $\theta _ { 1 / 4 }$ is not defined, since the ratio between the elastic cross section and its Coulomb counterpart is above $1 / 4$ for any scattering angle.

Now let us consider the Wong cross section. We note that it is very close to the fusion cross section, except at the higher energies $E > 1 0 0$ MeV). Although this approximation is known to become progressively poorer as the energy falls well below the Coulomb barrier [1], this shortcoming cannot be observed in Fig. 5. However, it would be clear in a logarithmic scale plot. We should remark that it is not a surprise that the Wong cross section falls well below $\sigma _ { \mathrm { R } }$ . In the derivation of his formula, Wong approximates the absorption probability at each partial-wave by the transmission coefficient through the barrier of the $\it l$ - dependent effective potential. This approximation implies that there is total absorption of the current that reaches the inner region of the barrier, but no absorption in the barrier region. This procedure is justified in the case of fusion absorption but it does not account for absorption arising from direct reactions, which gives an important contribution to $\sigma _ { \mathrm { R } }$ .

![](images/2fc4e8ca470a9e49eb618795dc345ed577c1b6d4a566755738f8441b28fef587.jpg)  
Fig. 6. (Color on line) The quantum mechanical total reaction cross section (thick blue solid line) and Wong’s cross sections obtained with the barrier parameters of the s˜ao Paulo potential, and with barrier parameters fitted as to reproduce the quantum mechanical cross section. The notation is indicated in the legend of the figure.

To finish this sub-section, we point out that, in the original paper of Wong, his formula was presented as an approximation for the total reaction cross section. This may be reasonable if the reaction cross section is dominated by the fusion process. However, contributions of direct reactions can hardly be neglected. This becomes clear when one tries to compare reduced reaction cross section for different systems. Although the reduction method of Ref. [42, 43], which is based on the Wong formula works fine for fusion data, it fails when applied to total reaction data [44]. Nevertheless, the Wong formula can be a very good parameterization of the total reaction cross section, if $V _ { \mathrm { B } } , R _ { \mathrm { B } }$ and $\hbar \omega$ are treated as adjustable parameters, fitted to the total reaction data. This is illustrated in Fig. 6, where the quantum mechanical cross section, $\sigma _ { \mathrm R }$ (blue solid line), is compared with results of the Wong formula (green dot-dashed line with open circles) with the barrier parameters of the S˜ao Paulo potential, $R _ { \mathrm { B } } = 1 1 . 7$ fm, $V _ { \mathrm { B } } = 7 6 . 0$ MeV and $\hbar \omega = 4 . 8$ MeV, and with the Wong formula with barrier parameters fitted to reproduce the quantum mechanical cross section (purple dotted line and open squares). The total reaction cross section given by the Wong formula with the parameters of the S˜ao Paulo potential falls well below its quantum mechanical counterpart. On the other hand, the cross section given by the Wong formula with the fitted parameters can hardly be distinguished from the quantum mechanical result. However, we stress that using barrier parameters which do not correspond to the actual potential has no physical meaning. In this case, the Wong formula is just a smart parameterization for the total reaction cross section.

# 3 Many-body scattering theory

Potential scattering is a very limited theory for heavy-ion collisions. In typical situations, the dynamics is strongly

influenced by the nuclear structure of the collision partners, and then the coupled channel (CC) theory is a more suitable approach. In this treatment, the intrinsic degrees of freedom of the projectile and/or the target, denoted by $\xi$ , are explicitly taken into account. The scattering wave function, $\Psi ^ { ( + ) } ( { \bf R } , \xi )$ , where $\mathbf { R }$ in the vector joining the centers of the collision partners4, is the solution of the Schr¨odinger equation5,

$$
\left[ E - \mathbb {H} \right] \Psi^ {(+)} (\mathbf {R}, \xi) = 0, \tag {52}
$$

with scattering boundary conditions. Above,

$$
\mathbb {H} = h (\xi) + \hat {K} + \mathbb {U} (\mathbf {R}, \xi) \tag {53}
$$

is the total Hamiltonian of the system, $\hat { K }$ is the kinetic energy operator associated with the projectile-target relative motion, $h ( \xi )$ is the intrinsic Hamiltonian, and $\mathbb { U } ( \mathbf { R } , \boldsymbol { \xi } )$ is the complex coupling interaction. In the CC method, the scattering wave function is expanded on a set of eigenstates of the intrinsic Hamiltonian (channels), $\varphi _ { \alpha } ( \boldsymbol { \xi } )$ , given by the eigenvalue equation,

$$
h \varphi_ {\alpha} (\xi) = \varepsilon_ {\alpha} \varphi_ {\alpha} (\xi), \tag {54}
$$

where $\alpha$ stands for the set of quantum numbers required to specify the intrinsic state (usually the energy and the appropriate angular momentum quantum numbers, $\it { l s j }$ and $m$ ). That is

$$
\Psi^ {(+)} (\mathbf {R}, \xi) = \sum_ {\alpha = 0} ^ {N} \varphi_ {\alpha} (\xi) \psi_ {\alpha} ^ {(+)} (\mathbf {R}). \tag {55}
$$

Although the channel expansion involves an infinite number of intrinsic states, there is a finite number of nonelastic states, denoted by $N$ , that are relevant to the reaction dynamics. Thus, the series is truncated after $N { + 1 }$ terms (the elastic, labelled by $\alpha = 0$ , and $N$ nonelastic channels).

# 3.1 The CC equations

Inserting the channel expansion into Eq. (52), taking scalar products with each of the intrinsic states, and using their orthonormality properties, one gets the set of CC equations

$$
\left[ E - H _ {\alpha} (\mathbf {R}) \right] \psi_ {\alpha} ^ {(+)} (\mathbf {R}) = \sum_ {\alpha^ {\prime}} H _ {\alpha , \alpha^ {\prime}} (\mathbf {R}) \psi_ {\alpha^ {\prime}} ^ {(+)} (\mathbf {R}), \quad (5 6)
$$

where $\alpha$ and $\alpha ^ { \prime }$ run from 0 to $N$ . Above, $H _ { \alpha , \alpha ^ { \prime } } ( \mathbf { R } )$ is the matrix-element of the Hamiltonian in the basis of intrinsic states,

$$
H _ {\alpha , \alpha^ {\prime}} (\mathbf {R}) = \int d \xi \varphi_ {\alpha} ^ {*} (\xi) \mathbb {H} (\mathbf {R}, \xi) \varphi_ {\alpha^ {\prime}} (\xi). \tag {57}
$$

Note that we used the short-hand notation for the diagonal matrix-elements of $\mathbb { H }$ : $H _ { \alpha , \alpha ^ { \prime } } ( \mathbf { R } ) \equiv H _ { \alpha } ( \mathbf { R } )$ . The expansion of Eq. (55) is restricted to excited or transfer states with simple structure, reached through a small number of steps. They correspond to the so called direct reactions. On the other hand, equilibrated CN states are too complicated to be included in the expansion. Nevertheless, they cannot be totally neglected. This situation can be remedied by the generalized optical potential,

$$
\mathbb {U} (\mathbf {R}, \xi) = \mathbb {V} (\mathbf {R}, \xi) + i \mathbb {W} (\mathbf {R}, \xi). \tag {58}
$$

The imaginary part of this potential accounts for the loss of flux going to CN formation. Alternatively, the effects of the CN can be simulated by keeping the potential real but assuming ingoing IWBC for all radial wave functions at some radial distance inside the potential barrier.

If all relevant direct channels are included in the CC expansion, absorption is associated exclusively with the fusion process. On the other hand, the total reaction cross section results from absorption by the imaginary potential, and also from the population of the direct reaction channels. Thus, it can be expressed by the deviation of the modulus of the elastic S-matrix from unity. In the simpler situation of spin zero, where the angular momentum projected components of the S-matrix are denoted by $S _ { \alpha , l } ( E )$ , the total reaction cross section is given by

$$
\sigma_ {\mathrm {R}} (E) = \frac {\pi}{k ^ {2}} \sum_ {l = 0} ^ {\infty} (2 l + 1) P _ {l} ^ {\mathrm {R}} (E), \tag {59}
$$

with the reaction probability at the $l ^ { \mathrm { t h } }$ partial-wave given by

$$
P _ {l} ^ {\mathrm {R}} (E) = 1 - \left| S _ {0, l} (E) \right| ^ {2}, \tag {60}
$$

where $S _ { 0 , l } ( E )$ is the elastic $S$ -matrix at the $l ^ { \mathrm { t h } }$ partial wave.

The fusion cross section is then given by the difference between the reaction cross section and the summed cross sections for the direct channels involved in the CC calculation, $\sigma _ { \alpha } ( E )$ . That is,

$$
\sigma_ {\mathrm {F}} (E) = \sigma_ {\mathrm {R}} (E) - \sum_ {\alpha = 1} ^ {N} \sigma_ {\alpha} (E). \tag {61}
$$

Since fusion corresponds to absorption by the shortrange imaginary potential, the cross section can be extracted directly from the violated continuity equation. A straightforward generalization of Eq. (6) to the CC space leads to the expression [20],

$$
\begin{array}{l} \sigma_ {\mathrm {F}} (E) = - \frac {1}{| A | ^ {2}} \frac {k}{E} \left\langle \Psi^ {(+)} \right| \mathbb {W} \left| \Psi^ {(+)} \right\rangle \\ = - \frac {1}{| A | ^ {2}} \frac {k}{E} \sum_ {\alpha , \alpha^ {\prime}} \left\langle \psi_ {\alpha} ^ {(+)} \mid W _ {\alpha \alpha^ {\prime}} \mid \psi_ {\alpha^ {\prime}} ^ {(+)} \right\rangle . \tag {62} \\ \end{array}
$$

This equation takes a simpler form when the imaginary potential is diagonal in channel space and it is channelindependent ( $W _ { \alpha \alpha ^ { \prime } } = W ( r ) \ \delta _ { \alpha \alpha ^ { \prime } } \nonumber$ . One gets

$$
\sigma_ {\mathrm {F}} = \sum_ {\alpha} \sigma_ {\mathrm {F}} ^ {(\alpha)}, \tag {63}
$$

with

$$
\sigma_ {\mathrm {F}} ^ {(\alpha)} = - \frac {1}{| A | ^ {2}} \frac {k}{E} \left\langle \psi_ {\alpha} ^ {(+)} \mid W \mid \psi_ {\alpha} ^ {(+)} \right\rangle . \tag {64}
$$

In potential scattering calculations with long range imaginary potentials, one might be tempted to associate fusion and direct reactions with absorption in the inner region of the barrier and absorption on the surface region, respectively. This could be done as follows. First, one splits the long range imaginary potential as the sum of two terms, namely

$$
W ^ {\mathrm {R}} (R) = W ^ {\mathrm {F}} (R) + W ^ {\mathrm {s}} (R),
$$

where $W ^ { \mathrm { F } } ( R )$ is a short-range term and $W ^ { \mathrm { s } } ( R )$ is a surface term. Then, the fusion and the direct reaction cross sections would be evaluated by Eq. (6), with the replacements $W ( R ) \to W ^ { \mathrm { F } } ( R )$ and $W ( R ) \to W ^ { \mathrm { R } } ( S )$ , respectively.

However, this procedure is misleading. This can be seen clearly in a comparison with the more reliable CC approach. An ideal potential scattering calculation would use an exact polarization potential, which leads to the same wave function as the elastic wave function obtained by the CC method, with the imaginary potential $W ^ { \mathrm { F } } ( R )$ . The fusion cross section of the CC method would then be given by Eq. (63), which contains contributions from both the elastic and nonelastic channels. The fusion cross section of the ideal potential scattering calculation would give the exact contribution from the elastic channel, but it would miss the contributions from nonelastic ones. This could be a very serious flaw. In typical CC calculations, the contributions from the main nonelastic channels may be comparable to that from the elastic one. Thus, the fusion cross section evaluated in this way may be greatly underestimated. Although this procedure may lead to the correct total reaction cross section, it does not take into account the fact that the incident flux lost to excited direct channels may, eventually, lead to fusion (the contribution from nonelastic channels to Eq. (63)).

# 3.2 Coupled channels in the continuum - The CDCC method

In typical collisions of tightly bound nuclei, the channel expansion of Eq. (55) involves only bound intrinsic states. This is justified by the fact that the breakup threshold of these nuclei are typically of several MeV, which makes the couplings to unbound channels negligible, at nearbarrier collision energies. A different situation is found in collisions of weakly bound nuclei. This is the case of the stable light nuclei $_ 6$ Li, $^ { 9 }$ Be and 7Li, which have breakup

thresholds of 1.47, 1.67 and 2.48 MeV, respectively, and radioactive nuclei like 6He, $^ { \mathrm { s } } \mathrm { B }$ , $\perp \perp$ Li and $^ { 1 1 }$ Be, with breakup thresholds below 1 MeV. In such cases, couplings with channels in the continuum (the breakup channel) have strong influence on the reaction dynamics, and it is necessary to include the continuum in the channel expansion. Eq. (55) then becomes,

$$
\Psi^ {(+)} (\mathbf {R}, \xi) = \Psi_ {\mathrm {B}} ^ {(+)} (\mathbf {R}, \xi) + \Psi_ {\mathrm {C}} ^ {(+)} (\mathbf {R}, \xi), \tag {65}
$$

with

$$
\Psi_ {\mathrm {B}} ^ {(+)} (\mathbf {R}, \xi) = \sum_ {\alpha = 0} ^ {N _ {\mathrm {B}}} \varphi_ {\alpha} (\xi) \psi_ {\alpha} ^ {(+)} (\mathbf {R}), \tag {66}
$$

where $N _ { \mathrm { B } }$ is the number of bound states of the projectile, with $\alpha$ standing for the quantum numbers required to specify them (usually $\varepsilon _ { \alpha } , l _ { \alpha } , j _ { \alpha }$ and $\nu$ ), and

$$
\Psi_ {\mathrm {C}} ^ {(+)} (\mathbf {R}, \xi) = \sum_ {\beta} \int d \varepsilon \varphi_ {\varepsilon \beta} (\xi) \psi_ {\varepsilon \beta} ^ {(+)} (\mathbf {R}). \tag {67}
$$

Above, $\varepsilon$ is the intrinsic energy in the continuum, which runs from the breakup threshold to infinity, and $\beta$ stands for the remaining quantum numbers of the states representing the scattering of the projectile’s fragments. In principle, this label runs from 1 to infinity, independently of $\varepsilon$ .

Coupled equations could be derived as described in section 3.1. That is, taking scalar product of Eq. (52) with each of the intrinsic states ( $\varphi _ { \alpha } ( \boldsymbol { \xi } )$ and $\varphi _ { \varepsilon \beta } ( \boldsymbol { \xi } )$ ), and using their orthonormality properties. However, this procedure would lead to an infinite number of coupled equations, even truncating the intrinsic energy and keeping only a few values of $\beta$ . This problem can be traced back to the fact that the expansion involves the continuous quantum number $\varepsilon$ .

However, a finite number of coupled equations can be obtained if one expands the wave function $\Psi _ { \mathrm { C } } ^ { ( + ) } ( { \bf R } , \xi )$ over a finite set of states, $\phi _ { n \beta } ( \boldsymbol { \xi } )$ , instead of the infinite basis of scattering states. This is the basic idea of the continuum discretized coupled channel approximation (CDCC). The choice of these basis states is arbitrary, provided that it gives a good representation of the space spanned by the set of scattering states, truncated at some reasonable intrinsic energy, $\varepsilon _ { \mathrm { m a x } }$ . In the next sub-sections, we discuss the CDCC approximation in further detail.

# Three-body CDCC

Let us consider the situation where, during the collision, the projectile breaks up into two fragments without internal structure, $c _ { 1 }$ and $c _ { 2 }$ . In this case, the intrinsic coordinate (previously denoted by $\xi$ ) is the vector joining the centers of the two fragments, $\mathbf { r }$ , as shown in Fig. 7. Along the collision, the target interacts with the fragments through the complex potentials $U _ { 1 } ( r _ { 1 } )$ and $U _ { 2 } ( r _ { 2 } )$ , which are functions of the moduli of the vectors $\mathbf { r } _ { 1 } ~ =$

![](images/47b67e3daf86a9ef8a5d63ae10c09653458cafe903e36b4a5c8701a6a2e2cae7.jpg)  
Fig. 7. (Color on line) Schematic representation of the colliding system in the 3-body CDCC calculations (figure taken from Ref. [45]). For details, see the text.

U

${ \bf R } - ( A _ { 2 } / A _ { \mathrm { P } } ) \ .$ r and ${ \bf r } _ { 2 } = { \bf R } + ( A _ { 1 } / A _ { \mathrm { P } } ) { \bf \delta r }$ , respectively. Thus, the projectile-target interaction is given by

$$
\mathbb {U} (\mathbf {R}, \mathbf {r}) = U _ {1} \left(r _ {1}\right) + U _ {2} \left(r _ {2}\right). \tag {68}
$$

Then, the total Hamiltonian of the system is

$$
\mathbb {H} (\mathbf {R}, \mathbf {r}) = h (\mathbf {r}) + \hat {K} + \mathbb {U} (\mathbf {R}, \mathbf {r}), \tag {69}
$$

and the scattering state satisfies the Schr¨odinger equation,

$$
\left[ E - \mathbb {H} \right] | \Psi^ {(+)} \rangle = 0. \tag {70}
$$

Proceeding as in the case of tightly bound systems, we take scalar product of both sides of the above equation with each of the intrinsic states appearing in the expansions of Eqs. (66) and (67). In this way, we get the sets of coupled equations,

$$
\begin{array}{l} \left[ E - H _ {\alpha , \alpha} (\mathbf {R}) \right] \psi_ {\alpha} ^ {(+)} (\mathbf {R}) = \sum_ {\alpha^ {\prime}} H _ {\alpha , \alpha^ {\prime}} (\mathbf {R}) \psi_ {\alpha^ {\prime}} ^ {(+)} (\mathbf {R}) \\ + \sum_ {\beta} \int d \varepsilon H _ {\alpha , \varepsilon \beta} (\mathbf {R}) \psi_ {\varepsilon \beta} ^ {(+)} (\mathbf {R}) \tag {71} \\ \end{array}
$$

and

$$
\begin{array}{l} \left[ E - H _ {\varepsilon \beta , \varepsilon \beta} (\mathbf {R}) \right] \psi_ {\varepsilon \beta} ^ {(+)} (\mathbf {R}) = \sum_ {\alpha} H _ {\varepsilon \beta , \alpha} (\mathbf {R}) \psi_ {\alpha} ^ {(+)} (\mathbf {R}) \\ + \sum_ {\beta^ {\prime}} \int d \varepsilon^ {\prime} H _ {\varepsilon \beta , \varepsilon^ {\prime} \beta^ {\prime}} (\mathbf {R}) \psi_ {\varepsilon^ {\prime} \beta^ {\prime}} ^ {(+)} (\mathbf {R}), \quad (7 2) \\ \end{array}
$$

where the matrix-elements of the Hamiltonian involving continuum states are defined analogously to Eq. (57). Now, however, the situation is different. This procedure lead to an infinite set of coupled equations, which cannot be solved.

The CDCC method deals with this problem by approximating the infinite dimensional space of scattering states by the reduced space spanned by a finite set of functions. In the simple case where the $c _ { 1 }$ and $c _ { 2 }$ have spin zero, $\beta$ stands for the total angular momentum of the projectile, $j$ , and its $\mathbf { Z }$ -projection, $\nu$ . Then, the wave function describing the scattering of the fragments with relative energy $\varepsilon$ can be written as:

$$
\varphi_ {\varepsilon \beta} (\mathbf {r}) = \frac {u _ {\varepsilon \beta} (r)}{r} \quad \mathcal {Y} _ {\beta} (\hat {\mathbf {r}}), \tag {73}
$$

where $u _ { \varepsilon \beta } ( r )$ is the radial part of $\varphi _ { \varepsilon \beta } ( \mathbf { r } )$ . Above, $\mathcal { V } _ { \beta } ( \hat { \mathbf { r } } )$ is a complementary function of the orientation $_ 6$ of $\mathbf { r }$ . The radial wave functions must be normalized to satisfy the relations,

$$
\int d r u _ {\varepsilon \beta} ^ {*} (r) u _ {\varepsilon^ {\prime} \beta} (r) = \delta (\varepsilon - \varepsilon^ {\prime}). \tag {74}
$$

In the particular case of fragments with spin zero, $\beta$ represents the quantum numbers $\{ j , \nu \}$ . Then, $\mathcal { V } _ { \beta } ( \hat { \mathbf { r } } ) \equiv \mathcal { V } _ { j m } ( \hat { \mathbf { r } } )$ are the usual spherical harmonics. In more general situations, it is a more complicated function [20, 46, 47], involving spherical harmonics, spin states and angular momentum coupling coefficients.

The CDCC approximation consists in replacing the infinite integral over $\varepsilon$ by the sum

$$
\int d \varepsilon \frac {u _ {\varepsilon \beta} (r)}{r} \longrightarrow \sum_ {n = 1} ^ {n _ {\max }} \frac {\phi_ {n \beta} (r)}{r}, \tag {75}
$$

where the set of $n _ { \mathrm { m a x } }$ functions $\phi _ { n \beta } ( \boldsymbol { r } )$ must satisfy the orthonormality relations7

$$
\int d \varepsilon \phi_ {n \beta} ^ {*} (r) \phi_ {n ^ {\prime} \beta} (r) = \delta_ {n n ^ {\prime}}. \tag {76}
$$

Further, the intrinsic hamiltonian should be diagonal in the $n _ { \mathrm { m a x } }$ dimensional space of the functions $\phi _ { n \beta } ( \boldsymbol { r } )$ . That is

$$
\left\langle \phi_ {n \beta} \mid h \mid \phi_ {n ^ {\prime} \beta} \right\rangle = \bar {\varepsilon} _ {n} \delta_ {n n ^ {\prime}}. \tag {77}
$$

Otherwise, there would be channel couplings even without the interaction with the target.

With the continuum discretization of Eq. (75), bound and unbound states can be treated on the same grounds. Then, the infinite set of Eqs. (71) and (72) reduces to a finite set of equations with the general form of Eq. (56). Now, however, $\alpha$ stands for any state of the projectile, bound or unbound. The number of coupled equations, $N$ , is given by

$$
N = N _ {\mathrm {B}} + N _ {\mathrm {C}}, \tag {78}
$$

where $N _ { \mathrm { B } }$ and $N _ { \mathrm { { C } } }$ are respectively the number of bound and continuum-discretized states of the projectile. The latter is given by

$$
N _ {\mathrm {C}} = n _ {\max } \times \beta_ {\max }. \tag {79}
$$

In practice, the number of coupled equation is much smaller than $N$ . When proper angular momentum projections are carried out, and angular momentum, and parity conservations are taken into account, the set of equations splits into decoupled sets of smaller dimensions, one for each invariant sub-space.

The discretization of the continuum may be performed by two methods: the bin method and the method of pseudostates. These methods are briefly discussed below.

# a) The bin method

In the bin method, the functions $\phi _ { n \beta } ( \boldsymbol { r } )$ are generated by scattering states of the fragments through wave packets with the general form,

$$
\phi_ {n \beta} (r) = \int d \varepsilon \Gamma_ {n} (\varepsilon) u _ {\varepsilon \beta} (r), \tag {80}
$$

with the weight function, $T _ { n } ( \varepsilon )$ , concentrated around $\varepsilon _ { n }$

The most common weight functions used in nuclear physics are constant within some limited energy interval, and zero elsewhere [9, 10, 47, 48]. The continuum is truncated at some energy $\varepsilon _ { \mathrm { m a x } }$ and the interval from 0 to the cut-off energy is divided into a set of non-overlapping intervals $\varDelta _ { m }$ , centered at the energy $\varepsilon _ { m }$ , such that the upper limit of each interval coincides with the lower limit of the subsequent one. That is,

$$
\begin{array}{l} \Gamma_ {m} (\varepsilon) = \frac {1}{\sqrt {\Delta_ {m}}}, \qquad \text {i f} \varepsilon_ {m} ^ {(+)} \geq \varepsilon_ {m} \geq \varepsilon_ {m} ^ {(-)} \\ = 0, \quad \text {o t h e r w i s e}, \tag {81} \\ \end{array}
$$

where $\varepsilon _ { m } ^ { ( \pm ) } = \varepsilon _ { m } { \pm \varDelta _ { m } } / 2$ are the limits of the interval. The most common choice is to use bins of constant width in momentum space. In this case, the energy width increase linearly with $k$ . On the other hand, when there are sharp resonances in the scattering of the fragments, it is necessary to reduce the width and increase the density of bins around the resonance.

In most CDCC calculations the discretization is carried out with bins in momentum space, labeled by $k =$ $\sqrt { 2 \mu _ { 1 2 } \varepsilon / \hbar }$ , where $\mu _ { 1 2 }$ is the reduced mass in the $c _ { 1 } - c _ { 2 }$ collision. In this case, the bins are given by

$$
\phi_ {m \beta} (r) = \int d k \Gamma_ {m} (k) u _ {k \beta} (r), \tag {82}
$$

with the scattering states satisfying the orthonormality relations

$$
\int d r u _ {k \beta} ^ {*} (r) u _ {k ^ {\prime} \beta} (r) = \frac {\pi}{2} \delta \left(k - k ^ {\prime}\right). \tag {83}
$$

The constant weight functions now are given by

$$
\begin{array}{l} \Gamma_ {m} (k) = \frac {1}{\sqrt {\Delta_ {m}}}, \qquad \text {i f} k _ {m} ^ {(+)} \geq k _ {m} \geq k _ {m} ^ {(-)} \\ = 0, \quad \text {o t h e r w i s e}, \tag {84} \\ \end{array}
$$

with $k _ { m } ^ { ( \pm ) } = k _ { m } \pm \varDelta _ { m } / 2$ , and $\varDelta _ { m }$ now has the dimension of $p / \hbar$ . Since the energy is proportional to $k ^ { 2 }$ , the energy width of a bin with constant width in $k$ -space increases linearly with $k$ .

It can be easily proved that the functions generated by the weight functions of Eq. (81) form an orthonormal set. For this purpose, we take the scalar product of two bins and use the orthonormality of the scattering states (Eq. (74)). We get,

$$
\left\langle \phi_ {n \beta} \mid \phi_ {n ^ {\prime} \beta} \right\rangle = \int d \varepsilon \Gamma_ {n} (\varepsilon) \Gamma_ {n ^ {\prime}} (\varepsilon) = \delta_ {n, n ^ {\prime}}. \tag {85}
$$

The second equality in the above equation was obtained inserting the weight functions of Eq. (81) into the integral over $\varepsilon$ . It is equally straightforward to show that the intrinsic Hamiltonian is diagonal in this bin space. Proceeding similarly, one gets

$$
\left\langle \phi_ {n \beta} \mid h \mid \phi_ {n ^ {\prime} \beta} \right\rangle = \int d \varepsilon \Gamma_ {n} (\varepsilon) \varepsilon \Gamma_ {n ^ {\prime}} (\varepsilon) = \bar {\varepsilon} _ {n} \delta_ {n, n ^ {\prime}}. \tag {86}
$$

The weight functions of Eq. (81) are very easy to handle but the abrupt change at the edges leads to bins with longer ranges and with beats at large radial distances [49]. Although it is not a serious problem, it can be avoided with smooth weight functions, as the ones proposed in Ref. [49], and used in Refs. [45, 49, 50, 51]. However, there is a drawback with these weight functions: they do not diagonalize the intrinsic Hamiltonian. It is then necessary to perform a unitary transformation in the bin space,

$$
\phi_ {n \beta} (r) \rightarrow \bar {\phi} _ {n \beta} (r) = \sum_ {n = 1} ^ {n _ {\max }} U _ {n m} (\beta) \phi_ {m \beta} (r), \tag {87}
$$

with the operator $U ( \beta )$ determined by the condition

$$
\left\langle \bar {\phi} _ {n j} \right| h \left| \bar {\phi} _ {n ^ {\prime} j} \right\rangle = \sum_ {m, m ^ {\prime} = 1} ^ {n _ {\max }} U _ {n m} ^ {\dagger} (\beta) h _ {m m ^ {\prime}} U _ {m ^ {\prime} n ^ {\prime}} (\beta) = \bar {\varepsilon} _ {n} \delta_ {n, n ^ {\prime}}, \tag {88}
$$

where

$$
h _ {m m ^ {\prime}} = \left\langle \phi_ {m \beta} \right| h \left| \phi_ {m ^ {\prime} \beta} \right\rangle . \tag {89}
$$

# b) The pseudo-states method

In the pseudo-states (PS) method, the space of scattering states is approximated by a finite dimensional space spanned by a set of square-integrable functions. These functions are approximate eigenstates of $h$ with positive energy. The method is developed in two steps. First, one selects a set of square integrable functions $\phi _ { m \beta } ( \boldsymbol { r } )$ . Then,

the pseudo-states, $\phi _ { n \beta } ( \boldsymbol { r } )$ , are determined by diagonalizing $h$ in this space spanned by this set. The diagonalization is performed as in the case of non-orthogonal bins, following the procedure of Eqs. (87), (88) and (89). There is, however, a difference. In the bin method, the functions $\phi _ { m \beta } ( \boldsymbol { r } )$ are wave packets of scattering states. Thus, the eigenvalues $\varepsilon _ { n }$ are all positive. Now the situation is different. There are also negative eigenvalues, which represent the bound states of the projectile. In most cases, these states are calculated directly, without expansion in PC basis. In such cases, the eigenstates with negative energy obtained through the diagonalization of $h$ should be discarded.

The choice of square-integrable set of states, $\phi _ { n \beta } ( \boldsymbol { r } )$ , is arbitrary, provided that they give a good description of the radial wave functions, within the range of the coupling interactions. Choices based on Gaussian functions are extensively discussed in Ref. [52]. We mention two of them. The first is the set of $N$ real Gaussian functions with variable range [48],

$$
\phi_ {n \beta} (r) = r ^ {l _ {\beta}} \exp \left[ - r ^ {2} / a _ {n} ^ {2} \right], \tag {90}
$$

where $l _ { \beta }$ is the orbital angular momentum of the $c _ { 1 } - c _ { 2 }$ relative motion in the state $\phi _ { n \beta }$ . The range increases from $a _ { 1 }$ to $a _ { \mathrm { N } }$ , in the geometrical progression

$$
a _ {n} = a _ {1} \left(\frac {a _ {\mathrm {N}}}{a _ {1}}\right) ^ {(n - 1) / (N - 1)}, \tag {91}
$$

where $a _ { 1 }$ and $a _ { \mathrm { N } }$ are parameters of the set. The second is a set of $2 N$ functions obtained by the multiplication of the Gaussians of Eq. (90) by oscillating functions, in the form [52],

$$
\phi_ {n \beta} ^ {\mathrm {C}} = \phi_ {n \beta} \cos [ b (r / a _ {n}) ] \tag {92}
$$

$$
\phi_ {n \beta} ^ {\mathrm {S}} = \phi_ {n \beta} \sin [ b (r / a _ {n}) ], \tag {93}
$$

where $b$ is an adjustable parameter. This set corresponds to taking the real and the imaginary parts of the functions of Eq. (90) with complex widths. Calculations using this set of states converge more rapidly than the ones using the Gaussians of Eq. (90).

Some CDCC calculations adopting the Lagrange-mesh method make a different choice of basis functions. In such cases, one frequently uses basis functions associated with a Gauss quadrature [46, 53]. This greatly simplifies the numerical calculations.

A large number of three-body CDCC calculations neglecting excitations of the fragments and the target have been reported. For a review, see, e.g. Refs. [4, 9, 10].

# Core and target excitations

Until recently, the available CDCC calculations ignored intrinsic structures of the projectile’s fragments and of the target, treating them as point particles. Frequently, these

approximations are reasonable. However, the neglected degrees of freedom may play an important role in the reaction dynamics of some colliding systems. Formally, the inclusion of excitations of the fragments or of the target is straightforward. However, from the computational point of view it is not a trivial task. Usually, the calculations are performed by standard computer codes available in the literature and the inclusion of fragment or target excitation involves modifications that requires considerable knowledge of the structure of the code. In addition, the inclusion of these excitations enlarges significantly the dimension of the matrices involved in the calculations, demanding much more computer power. Calculations with excitations of one of the fragments or of the target will be briefly discussed below (we follow Ref. [54]).

# a) CDCC with Core excitation (XCDCC)

If the intrinsic structure of a projectile fragment, say $c _ { 1 }$ , with coordinates $\xi _ { 1 }$ , is taken into account, the total Hamiltonian of the system becomes

$$
\mathbb {H} (\mathbf {R}; \mathbf {r}, \xi_ {1}) = h (\mathbf {r}, \xi_ {1}) + \hat {K} + \mathbb {U} (\mathbf {R}; \mathbf {r}, \xi_ {1}), \tag {94}
$$

with the projectile-target potential8

$$
\mathbb {U} (\mathbf {R}; \mathbf {r}, \xi_ {1}) = U _ {1} \left(\mathbf {r} _ {1}, \xi_ {1}\right) + U _ {2} \left(r _ {2}\right). \tag {95}
$$

Above, $\xi _ { 1 }$ stands for the intrinsic coordinates of fragment $c _ { 1 }$ . Then, the projectile’s wave functions of Eq. (73) takes the form

$$
\varphi_ {\varepsilon \beta} (\mathbf {r}) = \frac {u _ {\varepsilon \beta} (r)}{r} \quad \mathcal {Y} _ {\beta} (\hat {\mathbf {r}}, \xi_ {1}). \tag {96}
$$

Now the index $\beta$ stands for angular momenta of the projectile and the fragments, and also for the quantum numbers associated with the degrees of freedom represented by $\xi _ { 1 }$ .

This generalization of the CDCC approximation, known as XCDCC, was introduced by Summers et al. [55, 56], to study the breakup of $^ { 1 7 } \mathrm { C }$ $\left( ^ { 1 6 } \mathrm { C } + p \right)$ and 11Be (10Be + n) projectiles on 9Be targets. The calculations included excitation channels related to rotational bands of the deformed $^ { 1 6 } \mathrm { C }$ and $^ { 1 0 } \mathrm { { B e } }$ cores.

More recently, similar calculations have been carried out to study different reactions. Moro and Crespo [57] studied the influence of rotational excitations of the deformed $^ { 1 0 }$ Be core in the breakup of 11Be ${ \binom { 1 0 } { \mathrm { B e } + n } }$ projectiles in collisions with a proton target. For this purpose, they proposed a simple reaction model using the DWBA.

De Diego et al. [58] used a more realistic XCDCC model to evaluate quasi-elastic and breakup cross sections for the same system, at collision energies ranging from 10 to 200 MeV/nucleon.

Chen et al. [59] measured elastic and breakup cross sections for the same $^ { 1 1 } \mathrm { B e } + p$ system at 26.9 MeV/nucleon,

![](images/b1ff9cd8199880ac0a0d9afd1b9545f557c8e6a649484a8cd557be5fc595431f.jpg)  
Fig. 8. (Color on line) Elastic angular distribution in the $^ { 1 1 }$ Be $+ ~ ^ { 1 9 7 }$ Au collision at two collision energies, divided by the corresponding Rutherford cross sections. Results of XCDCC (solid line) and CDCC (dashed line) are compared to the experimental data. The figure, the data and the calculations are from Ref. [61].

and compared the data with results of CDCC and XCDCC calculations including rotational excitations of $^ { 1 0 }$ Be. They concluded that excitations of the core play a moderate role in the reaction dynamics.

Later on, De Diego et al. [60] performed similar XCDCC calculations, to evaluate cross sections for different twoand three-body observables, at different collision energies, for which there are data available. In this way, they investigated the importance of core excitation in the reaction dynamics.

Pesudo et al. [61] measured elastic scattering, inelastic scattering and breakup in collisions of $^ { 1 1 }$ Be projectiles with a heavy target. They studied the 11Be − 197Au collision at two energies, below and around the Coulomb barrier. The experimental cross sections were then compared with predictions of CDCC and XCDCC calculations. Their elastic and breakup cross sections are shown in Figs. 8 and 9, respectively. The elastic scattering data is well reproduced by the XCDCC calculations, whereas the predictions of the standard CDCC calculations fall systematically below the data. This clearly indicates the importance of the core excitation for a proper description of the reaction dynamics of this system. On the other hand, inspecting Fig. 9, one concludes that the inclusion of core excitations in the calculations of breakup cross sections is not as important as in the case of elastic scattering.

![](images/779a1ad4fe02d214778b306ed7daced3ee65846054ec7c1990d3a86a778ce678.jpg)  
Fig. 9. (Color on line) Similar to the previous figure, but for breakup angular distributions (figure extracted from Ref. [61]).

Lay et al. [62] performed XCDCC calculations for $^ { 1 9 } \mathrm { C } +$ $p$ system, to analyse the resonant breakup of $^ { 1 9 } \mathrm { C }$ , which has been measured at RIKEN [63]. The inclusion of core excitation was shown to be essential for a good description of the data. CDCC calculations with an inert core largely underestimated the data.

# b) CDCC with excitations of the target

If the intrinsic degrees of freedom of the target, $\xi _ { \mathrm { T } }$ are taken into account, the system’s Hamiltonian becomes,

$$
\mathbb {H} (\mathbf {R}; \mathbf {r}, \xi_ {\mathrm {T}}) = h (\mathbf {r}) + H _ {\mathrm {T}} \left(\xi_ {\mathrm {T}}\right) + \hat {K} + \mathbb {V} (\mathbf {R}; \mathbf {r}; \xi_ {\mathrm {T}}), \tag {97}
$$

with

$$
\mathbb {V} (\mathbf {R}; \mathbf {r}; \xi_ {\mathrm {T}}) = V _ {1} \left(\mathbf {r} _ {1}, \xi_ {\mathrm {T}}\right) + V _ {2} \left(\mathbf {r} _ {2}, \xi_ {\mathrm {T}}\right). \tag {98}
$$

In this case, the label $\beta$ stands also for quantum numbers of the target, and Eq. (73) becomes

$$
\varphi_ {\varepsilon \beta} (\mathbf {r}) = \frac {u _ {\varepsilon \beta} (r)}{r} \quad \mathcal {Y} _ {\beta} (\hat {\mathbf {r}}, \xi_ {\mathrm {T}}). \tag {99}
$$

The importance of target excitations in weakly bound systems has been investigated by Lubian et al. [64]. They performed CDCC calculations for the $\mathrm { ^ { 9 } B e } + \mathrm { ^ { 5 8 } N i }$ system, including and not including excitations of the target. Comparing their results to the data of Aguilera et al. [65], they concluded that the inclusion of continuum states was essential to describe the data, whereas the influence of target excitations was weak.

![](images/4791de97df4e6b1b79bae77f3837578a28be4517d37912cb1d3c807056409a17.jpg)  
Fig. 10. (Color on line) Coordinates used in four-body CDCC calculations, where the projectile breaks up into three fragments (figure taken from Ref. [68]).

Woodward et al. [66] performed CDCC calculations for the $^ { 6 } \mathrm { L i } + ^ { 1 4 4 }$ Sm system. Besides the continuum space of the projectile, the calculations took into account the excitation of the $2 _ { 1 } ^ { + }$ and $3 _ { 1 } ^ { - }$ states in $\pm 4 4$ Sm. Inelastic angular distributions populating the two excited states of the target have been measured at near-barrier energies, and the results were compared with the predictions of standard coupled channel calculations and with their CDCC calculations with target excitation. This study lead to the conclusion that a full treatment of the continuum, including continuum-continuum couplings, is essential for a good description of the data.

G´omez-Ramos and Moro [67] developed a comprehensive study of the influence of the breakup channel on excitations of the target, in collisions with weakly bound projectiles. They performed standard coupled channel and CDCC calculations with target excitation for the following reactions:

58Ni(d, d)58Ni∗, 24Mg(d, d)24Mg∗, 144Sm(6Li,6 Li)144Sm∗, $\begin{array} { r l } & { \mathrm { ^ { 5 8 } N i } ( d , d ) ^ { \mathrm { 5 8 } } \mathrm { N i } ^ { \ast } \mathrm { , ~ } ^ { \mathrm { ~ } 2 4 } \mathrm { M g } ( d , d ) ^ { \mathrm { 2 4 } } \mathrm { M g } ^ { \ast } \mathrm { , ~ } ^ { \mathrm { 1 4 4 } } \mathrm { S m } ( ^ { \mathrm { 6 } } \mathrm { L i } , ^ { \mathrm { 6 } } \mathrm { L i } ) ^ { \mathrm { 1 4 4 } } \mathrm { S m } ^ { \ast } \mathrm { , } } \\ & { \mathrm { ^ 9 B e } ( ^ { \mathrm { 6 } } \mathrm { L i } , ^ { \mathrm { 6 } } \mathrm { L i } ) ^ { \mathrm { 9 } } \mathrm { B e } ^ { \ast } \mathrm { . } } \end{array}$

They obtained a satisfactory agreement with the data for both, standard and target excitation calculations, and concluded that the continuum had a moderate influence in the inelastic scattering.

# Four-body CDCC

Owing to their cluster configuration, several weakly bound nuclei can break up into three fragments during a collision. Important examples are the stable 9B $\mathrm { e } \ ( ^ { 4 } \mathrm { H e } + ^ { 4 } \mathrm { H e } + n )$ and radioactive two neutron halo nuclei, like $^ { 6 } \mathrm { H e } \ ( ^ { 4 } \mathrm { H e } + n + n )$ and $^ { 1 1 }$ Li $( ^ { 5 } \mathrm { L i } + n + n )$ . Thus, in collisions of projectiles with this configuration, the reaction dynamics involves four particles: the three clusters of the projectile, and the target. This calls for a generalization of the CDCC method, usually called four-body CDCC (to distinguish these methods, we henceforth adopt the notations 3b-CDCC and 4b-CDCC).

A collision of a three-fragment projectile with a target is schematically represented in Fig. 10. The projectiletarget interaction is the sum of interactions between the

fragments and the target, $U _ { c _ { i } - T } \left( i = 1 , 3 \right)$ ), which depend on the fragment-target coordinates $\mathbf { r } _ { i }$ , shown in Fig. 10. These coordinates are usually expressed in terms of the Jacobi coordinates9, defined as

$$
\mathbf {x} = \sqrt {\frac {A _ {1} A _ {2}}{A _ {1} + A _ {2}}} \left(\mathbf {r} _ {2} - \mathbf {r} _ {3}\right), \tag {100}
$$

$$
\mathbf {y} = \sqrt {\frac {A _ {3} \left(A _ {1} + A _ {2}\right)}{A _ {\mathrm {P}}}} \left[ \mathbf {r} _ {3} - \frac {A _ {1} \mathbf {r} _ {1} + A _ {2} \mathbf {r} _ {2}}{A _ {1} + A _ {2}} \right]. \tag {101}
$$

The Hamiltonian of the projectile-target system then reads

$$
\mathbb {H} (\mathbf {R}; \mathbf {x}, \mathbf {y}) = h (\mathbf {x}, \mathbf {y}) + \hat {K} + \mathbb {U} (\mathbf {R}; \mathbf {x}, \mathbf {y}), \tag {102}
$$

where $\mathbb { U } ( \mathbf { R } ; \mathbf { x } , \mathbf { y } )$ is the sum of the three complex fragmenttarget interactions, expressed in terms of the Jacobi coordinates.

The system’s wave functions still have the general form of Eq. (73), but with $\beta$ representing a larger number of intrinsic quantum numbers, and with the replacement,

$$
\mathcal {Y} _ {\beta} (\hat {\mathbf {r}}) \rightarrow \mathcal {Y} _ {\beta} (\mathbf {x}, \mathbf {y}).
$$

4b-CDCC calculations have been performed to evaluate several observables in different collisions of weakly bound nuclei. Matsumoto et al. [69] performed 3b- and 4b-CDCC calculations of elastic angular distributions in ${ } ^ { 6 } \mathrm { L i } - { } ^ { \mathrm { 1 2 } } \mathrm { C }$ scattering.

Rodr´ıguez-Gallardo et al. [68] performed 4b-CDCC calculations of elastic angular distributions for 6He projectiles on $^ { 1 2 }$ C, $^ \mathrm { 6 4 }$ Zn and $^ \mathrm { 2 0 8 }$ Pb targets.

Cubero et al. [70] measured elastic angular distributions for $^ { 1 1 }$ Li projectiles on a 208Pb target, at two energies around the Coulomb barrier. The data exhibited a strong damping at small angles, even at the energy below the barrier. This behaviour can be traced back to the breakup of the two-neutro-halo projectile, under the action of the long-range dipole interaction. The authors performed 4b-CDCC calculations, and compared the resulting cross sections with the data. The agreement between theory and experiment was very good.

Morcelle et al. [71] measured elastic angular distributions in collisions of 6He projectiles with a $^ { 5 8 } \mathrm { N i }$ target, at three near-barrier energies. The results are shown in Fig. 11, in comparison with predictions of 3b- and 4b-CDCC calculations. Clearly, the predictions of 4b-CDCC are much closer to the data than those of 3b-CDCC, mainly at $E _ { \mathrm { l a b } } = 1 6 . 5$ MeV.

Descouvemont et al. [72] performed four-body CDCC calculations for the ${ } ^ { 9 } \mathrm { B e } + { } ^ { 2 0 9 } \mathrm { B i }$ system. Elastic scattering, breakup and total fusion cross sections were evaluated simultaneously. The results were shown to be in good agreement with the data.

![](images/bf1a6f3aafb33732ea57f1fe2ce8e42138133d300daf47da94b2622f7cad7d9a.jpg)  
Fig. 11. (Color on line) Experimental elastic angular distribution in the ${ } ^ { 6 } \mathrm { H e } + { } ^ { 5 8 } \mathrm { N i }$ collision at three energies, in comparison with predictions of 3-body and 4-body CDCC calculations [71].

Fern´andez-Garc´ıa et al. [73] measured elastic angular distributions and cross sections for the production of 4He, in the ${ } ^ { 6 } \mathrm { H e } - { } ^ { 6 4 } \mathrm { Z n }$ collision. They performed coupled reaction channel (CRC), 3b-CDCC and 4b-CDCC calculations, and compared the resulting cross sections with the data. They found that the elastic cross sections of 3b-CDCC (using the di-neutron model) and 4b-CDCC are very similar, and close to the data. On the other hand, the contribution from elastic breakup to the 4He production cross section is very small. Although CRC calculations of 2n transfer gave a reasonable description of the data, inclusive cross section obtained with the Ichimura, Austern and Vincent (IAV) model [10, 74] are closer to the experiment.

A very nice example where 4b-CDCC reproduces the data much better than 3b-CDCC is shown in Fig. 12. Although the two CDCC calculations reproduce equally well the data at backward angles, the 4b-CDCC cross section remains close to it at forward angles, whereas the 3b-CDCC cross section falls significantly below.

# Other generalizaions of the CDCC

Recently, Pierre Descouvemont introduced two generalizations of the CDCC method. The first [79] is to use microscopic wave functions in a multi-cluster model $\left( \alpha + \alpha + n \right)$ for the bound states of $^ { 9 } \mathrm { { B e } }$ . This treatment has the nice feature of being based exclusively on nucleon-target interactions. The model was applied to the $^ { 9 } \mathrm { { B e }  { \mathrm { ~ + ~ } } ^ { 2 0 8 } \mathrm { { P b } } }$ and $^ { 9 } \mathrm { B e } \mathrm { ~ + ~ } ^ { 2 7 } \mathrm { A l }$ systems, and the results were shown to be in fair agreement with the data.

The second generalization [80, 81] is an extension of the 4b-CDCC approach to deal with collisions between

![](images/ccbbe0816037c8b453fe4f2aa65f30cf75551bbd469ee33a52b89abc03381c90.jpg)  
Fig. 12. (Color on line) Experimental angular distribution in ${ } ^ { 6 } \mathrm { H e } + { } ^ { 2 0 8 } \mathrm { P b }$ elastic scattering, in comparison with predictions of theoretical models. The data denoted by PH189 and PH215 are respectively from Refs. [75] and [76], the 1-channel and the 3b-CDCC calculations are from Ref. [77], and the 4b-CDCC calculations are from Ref. [78] (figure taken from a private communication with A. Moro).

two weakly bound nuclei, when each one can break up into two fragments. The new reaction model was applied to the $^ { 1 1 } \mathrm { B e } \mathrm { ~ - ~ } d$ collision at $E _ { \mathrm { c , m . } } ~ = ~ 4 5 . 5$ MeV. It was shown that for a good description of the elastic scattering data it is necessary to consider continuum states of the two collision partners simultaneously.

# 4 Hybrid reactions: The Surrogate Method

With the advent of secondary beams of unstable nuclei one is bound to deal with reaction cross sections of only a piece of the projectile. Further, some of the desired reactions can not be measured in the laboratory even in the case of stable projectiles. Thus one has to find a way to extract the desired cross section from a measurement of the spectrum of the observed piece of the primary projectile. An example, is deuteron-induced reaction of the type $( d , p )$ where the neutron is captured by a target such as $^ { 2 3 8 } \mathrm { U }$ or $^ { 2 3 2 }$ Th of importance for nuclear energy generation in fast breeder reactions. The measured proton spectrum can then be used to extract cross sections for neutron capture reactions, like: $n + ^ { 2 3 8 } \mathrm { U }  ^ { 2 3 9 } \mathrm { U }$ or $n + ^ { 2 3 2 } \mathrm { T h }  ^ { 2 3 3 } \mathrm { T h }$ . The method used to extract the desired neutron capture cross sections is referred to as the Surrogate Method (SM). Even in cases where the primary projectile is a weakly bound two-cluster projectile such as ${ ^ { 6 } \mathrm { L i } } = { ^ { 4 } \mathrm { H e } } + d$ , the measurement of the deuteron spectrum will supply information on the alpha capture by the target. This represents the incomplete fusion of the projectile, which when added to the complete fusion supplies the total fusion. Therefore, as part of this review it is important to give an account of the theory which supplies the expression of the spectrum of the detected fragment, and exhibit how this spectrum

is directly proportional to the secondary reaction cross section (the desired cross section). The primary reaction cross section of the full projectile is of course extracted as discussed in the previous section, and relies on the careful measurement of the angular distribution of the elastic scattering.

The theory that we summarise below is the inclusive nonelastic breakup theory (NEB). Let us first deal with the reaction $A \left( d , p \right) B$ , where $B = A + n$ . The NEB cross section for the emerging proton at an angle $\theta _ { p }$ and with energy $E _ { p }$ is

$$
\frac {d ^ {2} \sigma_ {p} ^ {\mathrm {N E B}}}{d E _ {p} d \Omega_ {p}} = \rho_ {p} \left(E _ {p}\right) \bar {\sigma} _ {\mathrm {R}} ^ {\mathrm {n A}}, \tag {103}
$$

where $\rho _ { p } ( E _ { p } )$ is the density of proton states and $\bar { \sigma } _ { \mathrm { ~ R ~ } } ^ { \mathrm { n A } }$ is the medium-modified total reaction cross section in the collision between the neutron and the target.

The Surrogate Method (SM) purports to extract $\bar { \sigma } _ { \mathrm { ~ R ~ } } ^ { n }$ through a measurement of $d ^ { 2 } \sigma _ { p } / d E _ { p } d \varOmega _ { p }$ . In fact, what is done is a measurement of the protons in coincidence with one decay product of the secondary compound nucleus $B \ = \ A + \ n$ [82]. Several publications on the SM have recently appeared [83]. Very recently this method was employed to populate the compound nucleus involving radioactive targets [84].

# 4.1 The inclusive nonelastic breakup cross section

In the more general case of a two-cluster primary projectile, $a = b + x$ , the NEB theory gives for the $a + A  b + B$ (with $B = x + A$ ) reaction cross section,

$$
\frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N E B}}}{d E _ {b} d \Omega_ {b}} = \rho_ {b} (E _ {b}) \bar {\sigma} _ {\mathrm {R}} ^ {x \mathrm {A}}, \tag {104}
$$

where $\bar { \sigma } _ { \mathrm { ~ R ~ } } ^ { x _ { \mathrm { { A } } } }$ is the total reaction cross section of the interacting fragment, $x$ , on the target and

$$
\rho_ {b} \left(E _ {b}\right) \equiv \frac {1}{(2 \pi) ^ {3}} \frac {d ^ {3} \mathbf {k} _ {b}}{d E _ {b} d \Omega_ {b}} = \frac {\mu_ {b} k _ {b}}{8 \pi^ {3} \hbar^ {2}} \tag {105}
$$

is the density of states of the observed fragment, $b$ . We consider the situation where $a$ is much lighter than $A$ , so that one can assume the target has infinite mass.

In this section we discuss the calculation of the NEB cross section within different participant-spectator models, following the work of Ichimura [85] (a recent review on this topic, can be found in Ref. [84]). They all lead to an expression of the form

$$
\frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N E B}}}{d E _ {b} d \Omega_ {b}} = - \frac {2}{v _ {a}} \rho \left(E _ {b}\right) \left\langle \varphi_ {x} \right| W _ {x A} | \varphi_ {x} \rangle , \tag {106}
$$

where $W _ { x A }$ is the imaginary part of an effective potential $U _ { x A }$ , which will be derived below, and $\varphi _ { x }$ is is the so called

source function, which varies according to the particular implementation of the model. The starting point is the system Hamiltonian,

$$
H = K _ {b} + K _ {x} + h _ {A} (\xi) + V _ {b x} + V _ {x A} + U _ {b A}, \tag {107}
$$

where $K _ { b }$ and $K _ { x }$ are respectively the kinetic energy operators of particles $b$ and $x$ , $h _ { A }$ is the intrinsic Hamiltonian of the target, $V _ { b x }$ and $V _ { x A }$ are respectively real potentials representing the interactions of $x$ with $b$ and $A$ , and $U _ { b A }$ is the complex optical potential between particle $b$ and the target. The intrinsic structures of $b$ and $x$ are neglected, whereas the target has a set of intrinsic states satisfying the equation,

$$
h _ {A} \phi_ {\alpha} (\xi) = \varepsilon_ {\alpha} \phi_ {\alpha} (\xi). \tag {108}
$$

We are interested in final states in the form

$$
\left| \chi_ {\mathbf {k} _ {b}} ^ {(-)} \Phi_ {\alpha} ^ {(-)} \right\rangle \equiv \left| \chi_ {\mathbf {k} _ {b}} ^ {(-)}\right) \otimes \left| \Phi_ {\alpha} ^ {(-)}\right), \tag {109}
$$

whereingoin $| \chi _ { \mathbf { k } _ { b } } ^ { ( - ) } \big )$ is a distorted wave with momentum e boundary condition, satisfying the $\hbar { \bf k } _ { b }$ withation

$$
\left[ K _ {b} + U _ {b A} ^ {\dagger} - E _ {b} \right] \left| \chi_ {\mathbf {k} _ {b}} ^ {(-)}\right) = 0, \tag {110}
$$

and $| \Phi _ { \alpha } ^ { ( - ) } )$ is a scattering state of the $x + A$ system with ingoing wave boundary condition, satisfying the equation

$$
\left[ H _ {x A} - E _ {\alpha} \right] \left| \Phi_ {\alpha} ^ {(-)}\right) = 0. \tag {111}
$$

Above, $E _ { \alpha } = E - E _ { b }$ and

$$
H _ {x A} = h _ {\mathrm {A}} + K _ {x} + V _ {x A}. \tag {112}
$$

is the Hamiltonian of the $x + A$ system. Then, the corresponding T-matrix in the post representation is

$$
T _ {\alpha \mathbf {k} _ {b}} = \left\langle \chi_ {\mathbf {k} _ {b}} ^ {(-)} \Phi_ {\alpha} ^ {(-)} \right| V _ {b x} | \Psi^ {(+)} \rangle , \tag {113}
$$

where $\big | \Psi ^ { ( + ) } \big \rangle$ is the scattering wave function, which satisfies the Schr¨odinger equation with the full Hamiltonian of Eq. (107), namely

$$
\left[ H - E \right] \left| \Psi^ {(+)} \right\rangle = 0. \tag {114}
$$

The inclusive breakup cross section is given in terms of the T-matrix by the expression (see e.g. Eq.(1.31) of Ref. [86])

$$
\frac {d ^ {2} \sigma_ {b} ^ {\text {i n c}}}{d E _ {b} d \Omega_ {b}} = \frac {2 \pi}{v _ {a}} \rho_ {b} \left(E _ {b}\right) \sum_ {\alpha} \left| T _ {\alpha \mathbf {k} _ {b}} \right| ^ {2} \delta \left(E - E _ {b} - E _ {\alpha}\right), \tag {115}
$$

where $v _ { a }$ is the incident velocity of $a$ . Using in Eq. (115) the well known identity

$$
\frac {1}{x + i \epsilon} = \mathcal {P} \left\{\frac {1}{x} \right\} - i \pi \delta (x), \tag {116}
$$

with $\mathcal { P }$ standing for the principal value, and replacing $T _ { \alpha \mathbf { k } _ { b } }$ by its explicit form ((Eq. (113)), the inclusive breakup cross section becomes

$$
\begin{array}{l} \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {i n c}}}{d E _ {b} d \Omega_ {b}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \operatorname {I m} \left\{\left\langle \Psi^ {(+)} \right| V _ {b x} \mid \chi_ {\mathbf {k} _ {b}} ^ {(-)} \right. \\ \left[ \sum_ {\alpha} \left(\Phi_ {\alpha} ^ {(-)} \right| \frac {1}{E - E _ {b} - E _ {\alpha} + 1 \epsilon} \left| \Phi_ {\alpha} ^ {(-)} \right.\right) \\ \left. \left(\chi_ {\mathbf {k} _ {b}} ^ {(-)} \right| V _ {b x} \mid \Psi^ {(+)} \right\rangle \}. \tag {117} \\ \end{array}
$$

The quantity within square brackets in the above equation is the spectral representation of the Green’s function associated with the Hamiltonian of Eq. (112), $G _ { x A } ^ { ( + ) } \big ( E - E _ { b } \big )$ Then, we can write

$$
\begin{array}{l} \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {i n c}}}{d E _ {b} d \Omega_ {b}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \operatorname {I m} \left\{\left\langle \Psi^ {(+)} \right| V _ {b x} \mid \chi_ {\mathbf {k} _ {b}} ^ {(-)} \right. \\ \left. G _ {x A} ^ {(+)} \left(E - E _ {b}\right) \left(\chi_ {\mathbf {k} _ {b}} ^ {(-)} \mid V _ {b x} \mid \Psi^ {(+)} \right\rangle \right\}. \tag {118} \\ \end{array}
$$

Different approximations have been adopted for the exact wave function $\left| \Psi ^ { ( + ) } \right.$ . Some of them are discussed below.

# The three-body model

First, we consider the approximation of $\big | \Psi _ { \cdot } ^ { ( + ) } \big \rangle$ by the three-body wave function of Austern et al. [10],

$$
\left| \Psi^ {(+)} \right\rangle \sim \left| \Psi_ {3 b} ^ {(+)} \right\rangle = \left| \psi_ {3 b} ^ {(+)}\right) \otimes \left| \phi_ {0}\right), \tag {119}
$$

where $\vert \phi _ { 0 } \rangle \equiv \vert \phi _ { \alpha = 0 }$ ) is the ground state of the target. Since the excitations of the target have been neglected, it is necessary to replace the real interaction $V _ { x A }$ by an optical potential, $U _ { x A }$ . Formally, this potential is the energy averaged potential of Feshbach’s theory [87, 88, 89, 90]. However, for practical purposes, it is treated phenomenologically. The three-body wave function is then the solution of the Schr¨odinger equation

$$
\left[ K _ {b} + K _ {x} + V _ {b x} + U _ {x A} + U _ {b A} \right] | \psi_ {3 b} ^ {(+)}) = E | \psi_ {3 b} ^ {(+)}). (1 2 0)
$$

Inserting Eq. (119) into Eq. (118), we get

$$
\begin{array}{l} \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {i n c}}}{d E _ {b} d \Omega_ {b}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \operatorname {I m} \left\{\left(\psi_ {3 b} ^ {(+)} \right| V _ {b x} \mid \chi_ {b} ^ {(-)} \right. \\ \left. G _ {x A} ^ {\text {o p t}} \left(\chi_ {b} ^ {(-)} \mid V _ {b x} \mid \psi_ {3 b} ^ {(+)}\right) \right\}, \tag {121} \\ \end{array}
$$

where

$$
G _ {x A} ^ {\text {o p t}} = \left(\phi_ {0} \right| G _ {x A} ^ {(+)} (E - E _ {b}) | \phi_ {0}). \tag {122}
$$

Now, we split the inclusive BU cross section into its elastic (EBU) and inelastic (NBU) components. For this purpose, we use the identity [91, 92]

$$
\begin{array}{l} \operatorname {I m} \left\{G _ {x A} ^ {\text {o p t}} \right\} = - \pi \int \left| \chi_ {\mathbf {k} _ {x}} ^ {(-)}\right) \delta \left(E - E _ {b} - \frac {\hbar^ {2} k _ {x} ^ {2}}{2 m _ {x}}\right) \\ \times \left(\chi_ {\mathbf {k} _ {x}} ^ {(-)} \right\rvert d \mathbf {k} _ {x} ^ {3} + G _ {x A} ^ {\mathrm {o p t} \dagger} W _ {x A} G _ {x A} ^ {\mathrm {o p t} \dagger}, \tag {123} \\ \end{array}
$$

where $W _ { x A }$ is the imaginary part of the optical potential $U _ { x A }$ . Inserting Eq. (123) into Eq. (121), the inclusive BU cross section can be put in the form

$$
\frac {d ^ {2} \sigma_ {b} ^ {\mathrm {i n c}}}{d E _ {b} d \Omega_ {b}} = \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {E B U}}}{d E _ {b} d \Omega_ {b}} + \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N B U}}}{d E _ {b} d \Omega_ {b}}, \tag {124}
$$

where

$$
\begin{array}{l} \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {E B U}}}{d E _ {b} d \Omega_ {b}} = \frac {2 \pi}{v _ {a}} \rho_ {b} (E _ {b}) \int \left| \left(\psi_ {3 b} ^ {(+)} \right| V _ {b x} \left| \chi_ {\mathbf {k} _ {b}} ^ {(-)} \chi_ {\mathbf {k} _ {x}} ^ {(-)}\right) \right| ^ {2} \\ \delta \left(E - E _ {b} - \frac {\hbar^ {2} k _ {x} ^ {2}}{2 m _ {x}}\right) d \mathbf {k} _ {x} ^ {3} \tag {125} \\ \end{array}
$$

is identified with the inclusive elastic breakup cross section. The remaining part, which corresponds to the inclusive nonelastic breakup cross section, can be put in the general form of Eq. (104), namely

$$
\left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N B U}}}{d E _ {b} d \varOmega_ {b}} \right] _ {\mathrm {3 b}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \left(\varphi_ {x} ^ {\mathrm {3 b}} \mid W _ {x A} \mid \varphi_ {x} ^ {\mathrm {3 b}}\right), \quad (1 2 6)
$$

with

$$
\left| \varphi_ {x} ^ {3 b} \right\rangle = G _ {x A} ^ {\text {o p t}} \left(\chi_ {b} ^ {(-)} \right| V _ {b x} \left| \psi_ {3 b} ^ {(+)} \right\rangle . \tag {127}
$$

Eq. (127) can be simplified if one uses the identity

$$
\begin{array}{l} V _ {b x} = \left[ V _ {b x} + K _ {b} + K _ {x} + U _ {x A} + U _ {b A} \right] \\ - \left[ K _ {b} + K _ {x} + U _ {x A} + U _ {b A} \right] \tag {128} \\ \end{array}
$$

in Eq. (126), and take into account Eqs. (110) and (120). One gets,

$$
\left| \varphi_ {x} ^ {3 b} \right\rangle = \left(\chi_ {b} ^ {(-)} \mid \psi_ {3 b} ^ {(+)} \right\rangle . \tag {129}
$$

# The IAV, the Hussein-McVoy and the Udagawa-Tamura formulae

Now we consider the model of Ichimura, Austern and Vincent [74, 92, 93]. These authors use the post representation but adopts the DWBA approximation. The exact wave function is replaced by

$$
\left| \Psi^ {(+)} \right\rangle \simeq \left| \Psi_ {\mathrm {I A V}} ^ {(+)} \right\rangle = \left| \chi_ {a} ^ {(+)} \psi_ {a}\right) \otimes \left| \phi_ {0}\right), \tag {130}
$$

where $\psi _ { a }$ is the ground state of the incident projectile and $\chi _ { a } ^ { ( + ) }$ is its distorted wave. They satisfy the equation,

$$
\left[ K _ {b} + K _ {x} + V _ {b x} + U _ {x A} + U _ {b A} \right] \left| \chi_ {a} ^ {(+)} \psi_ {a}\right) = E \left| \chi_ {a} ^ {(+)} \psi_ {a}\right). \tag {131}
$$

To derive the NBU cross section one follows the same procedures as in the previous section, but replacing $\left| \Psi _ { 3 b } ^ { ( + ) } \right.$ by $\left| \Psi _ { \mathrm { I A V } } ^ { ( + ) } \right.$ . Then, Eq. (121) becomes

$$
\begin{array}{l} \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {i n c}}}{d E _ {b} d \Omega_ {b}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \mathrm {I m} \Bigl \{\left(\chi_ {a} ^ {(+)} \psi_ {a} \right| V _ {b x} \big | \chi_ {b} ^ {(-)} \Bigr) \\ \left. G _ {x A} ^ {\text {o p t}} \left(\chi_ {b} ^ {(-)} \mid V _ {b x} \mid \chi_ {a} ^ {(+)} \psi_ {a}\right) \right\}, \tag {132} \\ \end{array}
$$

Next, we use Eq. (123) to split the cross section into its EBU and NBU components, getting the DWBA version of Eq. (124). The EBU cross section is given by Eq. (125), with the replacement: $\psi _ { 3 b } ^ { ( + ) }  \chi _ { a } ^ { ( + ) } \psi _ { a }$ . The NBU component reads

$$
\left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N B U}}}{d E _ {b} d \Omega_ {b}} \right] _ {\mathrm {I A V}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \left(\varphi_ {x} ^ {\mathrm {I A V}} \mid W _ {x A} \mid \varphi_ {x} ^ {\mathrm {I A V}}\right), (1 3 3)
$$

with the source function

$$
\left| \varphi_ {x} ^ {\mathrm {I A V}} \right\rangle = G _ {x A} ^ {\text {o p t}} \left(\chi_ {b} ^ {(-)} \right| V _ {b x} \left| \chi_ {a} ^ {(+)} \psi_ {a} \right\rangle . \tag {134}
$$

The Hussein-McVoy formula [94] adopts also the post representation and the approximation of Eq. (130) for the three-body wave function. However, the source function is generated using this approximation in Eq. (129) instead of in Eq. (127). In this way, one gets the NEB cross section

$$
\left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N B U}}}{d E _ {b} d \Omega_ {b}} \right] _ {\mathrm {H M}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \left(\varphi_ {x} ^ {\mathrm {H M}} \mid W _ {x A} \mid \varphi_ {x} ^ {\mathrm {H M}}\right), (1 3 5)
$$

with the source function

$$
\left| \varphi_ {x} ^ {\mathrm {H M}} \right\rangle = \left(\chi_ {b} ^ {(-)} \mid \chi_ {a} ^ {(+)} \psi_ {a} \right\rangle . \tag {136}
$$

The IAV and the HM formulae are obtained using the same approximation for the three-body wave function in different equations for the source function. However, although these equations are formally equivalent when the three-body wave function is used, the IAV formula is more convenient for numerical calculations [85]. The reason is that, owing to the short-range of the $V _ { b x }$ interaction, one does not need a good approximation for the three-body wave function at large distances between particles $b$ and $x$ . The calculation becomes considerably simpler if one adopts the zero-range approximation for $V _ { b x }$ [95]. The accuracy of this approximation has been studied by Lei and Moro [96] and by Potel et al. [84]. The situation is different in the HM formula, where the scalar product of Eq. (136) is not constrained to small values of $r _ { b x }$ .

The Udagawa-Tamura [91, 97] formula adopts the prior representation. Then, the T-matrix of Eq. (113) will involve the coupling interaction $U _ { x a } + U _ { b A } - U _ { a A }$ , instead of $V _ { b x }$ , and the NEB cross section becomes

$$
\left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N B U}}}{d E _ {b} d \varOmega_ {b}} \right] _ {\mathrm {U T}} = - \frac {2}{v _ {a}} \rho_ {b} (E _ {b}) \left(\varphi_ {x} ^ {\mathrm {U T}} \mid W _ {x A} \mid \varphi_ {x} ^ {\mathrm {U T}}\right), (1 3 7)
$$

with the source function

$$
\left| \varphi_ {x} ^ {\mathrm {U T}} \right\rangle = G _ {x A} ^ {\mathrm {o p t}} \left(\chi_ {b} ^ {(-)} \right| U _ {x a} + U _ {b A} - U _ {a A} \left| \chi_ {a} ^ {(+)} \psi_ {a} \right\rangle . (1 3 8)
$$

The relation between the IAV, the UT and the HM versions of the participant-spectator model has been discussed in several papers [84, 85, 96, 98, 99]. It has been

shown that within DWBA the IAV, the HM and the UT source functions satisfy the relation [97, 100],

$$
\left| \varphi_ {x} ^ {\mathrm {I A V}} \right\rangle = \left| \varphi_ {x} ^ {\mathrm {U T}} \right\rangle + \left| \varphi_ {x} ^ {\mathrm {H M}} \right\rangle . \tag {139}
$$

Then, inserting the above equation into Eq. (133), one gets

$$
\begin{array}{l} \left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N E B}}}{d E _ {b} d \Omega_ {b}} \right] _ {\mathrm {I A V}} = \left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N E B}}}{d E _ {b} d \Omega_ {b}} \right] _ {\mathrm {U T}} + \left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N E B}}}{d E _ {b} d \Omega_ {b}} \right] _ {\mathrm {H M}} \\ + \left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N E B}}}{d E _ {b} d \Omega_ {b}} \right] _ {\text {i n t}}, \tag {140} \\ \end{array}
$$

where

$$
\left[ \frac {d ^ {2} \sigma_ {b} ^ {\mathrm {N B U}}}{d E _ {b} d \Omega_ {b}} \right] _ {\text {i n t}} = - \frac {4}{v _ {a}} \rho_ {b} (E _ {b}) \operatorname {R e} \left\{\left(\varphi_ {x} ^ {\mathrm {I A V}} \mid W _ {x A} \mid \varphi_ {x} ^ {\mathrm {U T}}\right) \right\} \tag {141}
$$

is the interference term.

# IAV vs. UT models

There is some controversy about which model is more suitable to describe inclusive breakup experiments. Udagawa and Tamura [97] argued that the last two terms on the RHS of Eq. (140) are unphysical, since they arise from a non-orthogonality component of the wave function. Later, Mastroleo, Udagawa, and Tamura [101] performed numerical calculations for $^ { \mathrm { 5 8 , 6 2 } } \mathrm { N i } ( \alpha , X )$ reactions, using both the UT and the IAV models. They showed that the UT model predicts accurately the experimental cross section of Kleinfeller et al. [102], whereas the cross section obtained with the IAV model overestimated the data.

On the other hand, more recently, Lei and Moro [98] studied the accuracy of the IAV and the UT models, performing calculations of the $^ { 2 0 9 } \mathrm { B i } ( ^ { 6 } \mathrm { L i } , \alpha X )$ reaction at $E =$ 36 MeV. They obtained the EBU cross section by a CDCC calculation and evaluated the NBU cross section using both the UT and the IAV models. The IAV, UT, HM (denoted by NO) and the interference (IN) cross sections of Eq. (140) are shown in panel (a) of Fig. 13. The sum of the UT, HM and IN terms is represented by the long-dashed line. Note that this curve is very close to the one representing the IAV cross section, as predicted by Eq. (140).

Summing the NBE cross section of the IAV and UT models with the EBU cross section, Lei and Moro obtained the inclusive breakup cross section predicted by the two models. The results are shown in panel (b) of Fig. 13, in comparison with the data of Santra et al. [103]. Whereas the predictions of the IAV model reproduces very well the experimental cross section, the results of the UT model fall well below the data.

# 4.2 Applications

The surrogate method allows evaluation of cross sections that cannot be directly measured, such as neutron capture by short-lived targets. In this section we illustrate the use of the SM in two examples.

![](images/53b43a9536aa18d1221bd8c33ddf1946635c5f4616c0a8f9d4fe2a480982674e.jpg)

![](images/4e23479a647731f396c4e91f2b0d80936d6201ee95ed8afb7130ed49731094c3.jpg)  
Fig. 13. (Color on line) Panel (a): the IAV, UT, HM and IN cross sections; Panel (b): The inclusive BU cross sections predicted by the IAV and UT models, in comparison with data Ref. [103]. See the text for details.

# Neutron capture by short-lived targets

Neutron capture reactions are of great interest in nuclear physics, astrophysics and in theoretical models for generation of energy. In different situations, the direct measurement of these cross sections are very difficult to perform. One example is radioactive capture of neutrons by a short-lived target (more details on this topic can be found in Ref. [84]). We will discuss below the indirect measurement of the $( n , \gamma )$ cross section for the short-lived 87Y nucleus ( $t _ { 1 / 2 } = 7 9 . 8$ h), for which there are no data available. According to the Hauser-Feshbach theory [104], this cross section can be written as,

$$
\sigma_ {n \gamma} (E _ {n}) = \sum_ {J, \pi} \sigma_ {\mathrm {C N}} \left(E _ {\mathrm {e x}}, J ^ {\pi}\right) G _ {\gamma} \left(E _ {\mathrm {e x}}, J ^ {\pi}\right), \tag {142}
$$

where $\sigma _ { \mathrm { C N } } \left( E _ { \mathrm { e x } } , J ^ { \pi } \right)$ is the formation probability of the $^ { 8 8 } \mathrm { Y ^ { * } }$ compound nucleus with excitation energy $E _ { \mathrm { e x } }$ , angular momentum $J$ and parity $\pi$ , and $G _ { \gamma } \left( E _ { \mathrm { e x } } , J ^ { \pi } \right)$ is the probability that the CN decays emitting one or more $\gamma$ - rays. The excitation energy is related to the energy of the incident neutron by the equation, $E _ { n } = ( 1 + 1 / A ) ( E _ { \mathrm { e x } } -$ $S _ { n }$ ), where $S _ { n }$ is the energy needed to remove the neutron from $^ { \mathrm { 8 8 } } \mathrm { Y }$ . The CN formation probability can be obtained theoretically, using a properly chosen neutron-nucleus com-

![](images/f9d9e6cece5e9498d6169a4a1468651ceb307baa12a466a3e7cf610e4fcb6dd9.jpg)  
Fig. 14. (Color on line) The $\sigma _ { n \gamma } ( E _ { n } )$ cross section in the $p + { } ^ { \mathrm { s y } } \mathrm { Y }  d + { } ^ { \mathrm { s s } } \mathrm { Y } ^ { \ast }$ reaction, obtained by the SM (blue solid curve), with 1 $\sigma$ uncertainty (gray band). The figure was taken from Ref. [105]. For details see the text.

plex potential in a standard potential scattering calculation. The decay probability $G _ { \gamma }$ , which is very hard to calculate, can be obtained by the surrogate method from the $\mathrm { ^ { 8 9 } Y } \left( p , d \right) \mathrm { ^ { 8 8 } Y ^ { * } }$ reaction [105], through coincidence measurements of the deuteron with the characteristic $\gamma$ -rays emitted by $^ { 8 8 } \mathrm { Y ^ { * } }$ . The coincidence probability can be written as,

$$
P \left(E _ {\mathrm {e x}}, \theta_ {d}\right) = \sum_ {J, \pi} F _ {\mathrm {C N}} \left(E _ {\mathrm {e x}}, J ^ {\pi}, \theta_ {d}\right) G _ {\gamma} \left(E _ {\mathrm {e x}}, J ^ {\pi}\right), \tag {143}
$$

where $F _ { \mathrm { C N } } \left( E _ { \mathrm { e x } } , J ^ { \pi } , \theta _ { d } \right)$ is the formation probability of a 88Y CN with quantum numbers $\{ E _ { \mathrm { e x } } , J ^ { \pi } \}$ in the $( p , d )$ reaction, with the $d$ being emitted at an angle $\theta _ { d }$ , and $G _ { \gamma } \left( E _ { \mathrm { e x } } , J ^ { \pi } \right)$ is the $\gamma$ -decay probability that appears in Eq. (142). The former can be evaluated by standard nuclear reaction techniques. Then, $G _ { \gamma } \left( E _ { \mathrm { e x } } , J ^ { \pi } \right)$ is expressed in terms of parameters, which were determined by fitting the experimentally determined $P ( E _ { \mathrm { e x } } , \theta _ { d } )$ probability. The cross section $\sigma _ { n \gamma } ( E _ { n } )$ was then determined by inserting the resulting decay probability into Eq. (142) and using the calculated CN formation probability. The results are shown in Fig. 14, together with the TENDL 2015 (brown curves, with hatched 1 $\sigma$ uncertainty) and the Rosfond 2010 evaluations which are based on regional systematics (Nikolaev [106], Koning [107]).

The validity of the SM could not be checked in the above discussed reaction because there is no direct measurement of $\sigma _ { n \gamma } ( E _ { n } )$ . However, Escher et al. [105] assessed the accuracy of their surrogate approach using it for another target in the same Zr-Y region. They evaluated the $^ { 9 0 } \mathrm { Z r } ( n , \gamma )$ cross section through the surrogate reaction $^ { 9 2 } \mathrm { Z r } ( p , d ) ^ { 9 1 } \mathrm { Z r } ^ { * }$ . The agreement was reasonable. The surrogate cross section and the one measured directly exhibited similar energy dependences and the same order of magnitude.

# Complete fusion in collisions of weakly bound nuclei

Determining complete fusion (CF) and incomplete fusion (ICF) cross sections in collisions of weakly bound nuclei

![](images/f64fc8ed1e6295f587359b2884050e13285aa3b8b95af3a21452a6e77fe676de.jpg)  
Fig. 15. (Color on line) The cross sections of Eq. (144) together with the fusion cross section of barrier penetration models and the CF data. The figure was taken from Ref. [108] and the data are from Refs. [109, 111].

is a great challenge both for experimentalists and theoreticians [1, 4, 8]. Owing to the influence of the breakup channel, the CF cross section is reduced in comparison to predictions of barrier penetration models. In the $^ { 6 , 7 } \mathrm { L i } +$ 209Bi and $^ { 9 } \mathrm { { B e } + ^ { 2 0 8 } \mathrm { { P b } } }$ collisions, for example, the reduction is $\sim 2 0 - 3 5 \ \%$ . Recently, Lei and Moro evaluated the CF cross section using the inclusive breakup model [108]. For this purpose, they wrote the total reaction cross section as,

$$
\sigma_ {\mathrm {R}} = \sigma_ {\text {i n e l}} + \sigma_ {\mathrm {E B U}} + \sigma_ {\mathrm {N E B}} ^ {(\mathrm {b})} + \sigma_ {\mathrm {N E B}} ^ {(\mathrm {x})} + \sigma_ {\mathrm {C F}}, \tag {144}
$$

where $\sigma _ { \mathrm { R } } , \sigma _ { \mathrm { i n e l } } , \sigma _ { \mathrm { E B U } } , \sigma _ { \mathrm { N E B } } ^ { ( \mathrm { b } ) } , \sigma _ { \mathrm { N E B } } ^ { ( \mathrm { x } ) }$ and $\sigma _ { \scriptstyle \mathrm { C F } }$ are respectively the total reaction, inelastic scattering, elastic breakup, nonelastic breakup of fragments (b) and (x), and complete fusion cross sections. These cross sections were determined as follows. The $\sigma _ { \mathrm { R } }$ , $\sigma _ { \mathrm { E B U } }$ and $\sigma _ { \mathrm { i n e l } }$ cross sections were obtained from standard theoretical approaches (CC or CDCC calculations), and $\sigma _ { \mathrm { N E B } } ^ { ( \mathrm { b } , \mathrm { x } ) }$ were obtained from inclusive breakup model calculations as described in section 4.1. The remaining cross section, $\sigma _ { \scriptstyle \mathrm { C F } }$ was extracted from Eq. (144).

The method described above was used to study CF in the $^ { 6 , 7 } \mathrm { L i } \ : + \ : ^ { 2 0 9 } \mathrm { E }$ i collisions and the theoretical cross sections were compared with the data of Dasgupta et. al [109, 110, 111]. The comparison is reproduced in Fig. 15. Clearly, the surrogate approach of Lei and Moro [108] can describe the CF cross section very well, at leat for collision energies above the Coulomb barrier. On the other hand, it is unable to predict ICF cross section individually. This cross section is included in the NBE cross section, together with that for target excitations.

# 5 The total reaction cross section data

The total reaction cross section, $\sigma _ { \mathrm { R } }$ , is a very important quantity in collisions of heavy nuclei, since it contains information about the size of the collision partners and on the open channels. Although very desirable, determining $\sigma _ { \mathrm { R } }$ as the sum of individual measurement of each channel is a great challenge for experimentalists. Thus, most of the available total reaction data have been obtained from optical model analyses of experimental angular distributions in elastic scattering. In this way, the angular momentum components of the nuclear S-matrix are determined, and the total reaction cross section is evaluated.

In the past two decades or so, with the development and modernization of experimental techniques, several new experiments have been performed with the purpose of determining total reaction cross sections, and investigating the reaction mechanisms involved in heavy nuclei collisions. In particular, the possibility of using radioactive beams out of short-lived nuclei has offered unique opportunities for research in the frontier field of nuclear physics. Several experiments with radioactive nuclei as projectiles have been performed, and previous reviews on these measurements can be found in Refs. [3, 4, 5]. The results of the analysis of these experiments have provided very interesting information, improving our understanding of the interaction mechanism between heavy nuclei and their structures. The strong synergy between reaction mechanism and structure of the nuclei involved in the collision allows for both static and dynamics effects to be investigated in the experiments related to the elastic scattering and direct measurements. It is important to mention that, from its beginning, nuclear physics is a science impelled by experiments. The development of nuclear physics is strongly dependent on the continuous advance of experimental techniques and instrumentation. A review on the thousands of interesting experiments related to elastic scattering and total reaction cross section would be unpractical. Thus, in this section, we are going to review and discuss some basic features of these experiments with a focus on reactions with projectile in the mass range o $6 < A < 2 0$ on medium to heavy mass target, and at energies close and above the Coulomb barrier, performed in the last 10 years or so. Special attention will be given to experiments with radioactive ion beams.

# 5.1 Elastic scattering measurements and total reaction cross section

As mentioned, total reaction cross sections can be obtained from optical model analyses of elastic angular distributions. Elastic scattering is the simplest process which can occur in collisions of two nuclei, since it involves only a few degrees of freedom. At low energy, the cross sections are quite large and a phenomenological approach, in which the interaction between the colliding nuclei is represented by an appropriate optical-model potential, is still a very reliable and practical method to analyze angular

distribution data. Complex potentials are used to fit the experimental angular distribution and with these potentials the total reaction cross section can be determined. Investigations of elastic scattering is a very fruitful area and thousands of experiments have been carried out with very interesting results. In the past, most of the experiments were related to reactions with different combinations of complex projectile-target nuclear systems where the projectiles were stable nuclei. Elastic scattering cross sections of a quite large number of heavy-ion systems have been measured at several energies and the optical model has been found to be successful in extracting total reaction cross sections, as well as interaction radii. A large amount of nuclear reaction data can be found in the EXFOR database [112]. A compilation of elastic scattering data can also be found in the webpage of the NRV project [113, 114].

The important requirement in experiments related to elastic scattering is the identification and separation of the scattered particles from the large number of reaction products which can be produced in collisions between two heavy nuclei. Although it might seem to be a simple requirement, it can be more challenging for experiments with radioactive ion beam, which, sometimes, is produced as a cocktail of beams. To fulfil this requirement, a detection system with good energy, mass, and charge resolution, as well as a large dynamic range, is necessary. Over these several years of elastic scattering measurements, different experimental techniques have been developed to meet these requirements, all of which have its advantages and disadvantages. In the earlier times, the experiments with stable nuclei as projectiles, had a quite simple setup, which consisted of just a combination of thin and thick standard planar Silicon (Si) surface-barrier detectors, forming $\varDelta E - E$ telescopes. This kind of detectors was largely used in experiments and they were enough for particle identification and to cover the complete angular range for precise angular distribution measurements. A recent paper discussing improvements on particle identification when using this kind of detector configuration can be found in Ref. [115]. Although the planar silicon detectors are still being used, the recent generation of silicon detectors, with a more complex configuration, as double-sided silicon strip detectors (DSSSD), as well as gas ionizing detectors and active targets, have been developed and are being used.

The possibility of using radioactive beams out of shortlived nuclei has offered unique opportunities for research in the frontier field of nuclear physics. Many laboratories have installed or upgraded their facilities, and/or developed new techniques to produce radioactive nuclear beams. The idea of these facilities is to investigate nuclei at extreme conditions in terms of density, temperature, angular momentum and isospin. Reactions induced by these beams have been performed and exotic nuclear structures, such as halo properties, have been investigated [5]. Several laboratories are pushing to produce all kinds of exotic and very energetic species of nuclei as beams. Some lab-

oratories use fragmentation reactions and in-flight technique to produce radioactive ion beams at intermediate energies: NSCL at MSU (USA) [116], RIBLL at HIRFL (China) [117], FAIR at GSI (Germany) [118], RIBF at RIKEN (Japan) [119], LISE at GANIL (France) [120], EXOTIC at INFN-LNL (Italy) [121], MARS at Texas A&M (USA) [122], and ACCULINNA at Dubna (Russia) [123]. Other laboratories are using the ISOL technique: SPIRAL2 at GANIL (France) [124], SPES at INFN-LNL (Italy) [125], REX-ISOLDE at CERN (Switzerland) [126] and ISAC at TRIUMF (Canada) [127]. There are also several laboratories producing radioactive nuclei at the lower energy regime such as Twinsol at University of Notre Dame (USA) [128], RIBRAS (Brazil) [129], ATLAS and CARIBU at ANL (USA) [130], CRIB-RIKEN (Japan) [131] and SOLEROO (Australia) [132]. These laboratories are constantly improving their capabilities in terms of beam intensity, and development of new devices to increase the detection efficiency. Reviews on these facilities can be found in Refs. [133] and [134]. Some new laboratories, such as VECC-RIB (India) [135], BRIF [136] and HIAF (China) [137], which are under construction, will broaden even further the scope of the studies on nuclear reactions.

Most of these laboratories have scientific programs based on measurements of nuclear reactions, and several elastic scattering experiments, at energies close and above the Coulomb barrier, have been performed. These measurements allowed the extraction of total reaction cross sections and to investigate the influence of other mechanisms in the elastic scattering. The basic idea of these experiments is to obtain angular distributions for a wide range of angles and energies and extract the total reaction cross section. The angular distributions for elastic scattering can exhibit different features depending on the incident energy and on the structure of the colliding nuclei. For instance, angular distributions for tightly bound projectiles at near-barrier energies divided by the corresponding Rutherford cross section exhibit typical Fresnel oscillatory diffraction patterns [138]. For light projectiles, and at higher energies, the Coulomb force is weaker and the diffractive pattern changes from Fresnel to Fraunhofer oscillations.

On the other hand, angular distributions for weakly bound nuclei may deviate from the diffractive patterns. When the binding energy of the projectile fragments is very low, their motion decouples as they approach the target, leading to nonelastic processes. Owing to the long ranges of the Coulomb and nuclear couplings, this can occur even in distant collisions, giving rise to strong absorption at forward angles. As a result, the diffractive oscillations and the Fresnel peak are damped, or completely disappear.

![](images/c1a111e253f5501d4466926b98e0416ee3d8ba19d85c22896ca313ef5e22baec.jpg)  
Fig. 16. (Color online) Detector setup (DINEX) used in the experiment for the 6He+208Pb [141]. Figure extracted from ref. [141].

Some weakly-bound nuclei are called exotic, as they can exhibit peculiar properties such as halo and borromean10 configurations, where the valence nucleon(s) orbits around a compact core, forming an extended matter distribution [139, 140]. Typical examples of exotic nuclei with two valence nucleons (borromean) are 6He, and $\perp \perp$ Li, and with one valence nucleon (halo nuclei) are $^ { \mathrm { s } } \mathrm { B }$ , $^ { 1 1 }$ Be and $^ { 1 5 }$ C. In collisions of these nuclei with medium to heavy mass target, the breakup process is favoured during the interaction, due to the Coulomb field of the target and/or possibly a long-range component of the nuclear potential. During the collision, the charged core is decelerated by the repulsive Coulomb forces, while the valence neutrons are not affected. This phenomenon is called electric dipole polarization or Coulomb dipole excitation (CDE).

Radioactive ion beams produced as secondary beams have the limitation of much lower intensity (in the order of $1 0 ^ { 3 }$ up to $1 0 ^ { 6 }$ pps), when compared to beams of stable nuclei $\sim 1 0 ^ { 1 2 }$ pps). For experiments with these beams, larger solid angles and better detection efficiency of the setup are required to compensate for the low beam intensity. State-of-art experiments, using a combination of double-sided silicon strip detectors (DSSSD) have been performed for the 6He, 8He and $^ { 1 1 }$ Li nuclei on $^ \mathrm { 2 0 8 }$ Pb targets. Experiments with $_ 6$ He beams were performed at Louvain-la-Neuve (Belgium), before the facility was decommissioned, using an array of DSSSD telescopes called DINEX [141]. For the 8He beam, an experiment was performed at GANIL, France, using an arrangement called GLORIA (Global Reaction Array) detection system [142, 143], while for the $^ { 1 1 }$ Li beam an experiment at the ISAC-II line at TRIUMF, Canada, using an array of four DSSSD telescopes, was performed [70]. A sketch of the DINEX setup used in the elastic scattering of the $^ { 6 } \mathrm { H e } \ + \ ^ { 2 0 8 } \mathrm { P b }$ system is shown in Fig. 16. With this kind of arrangement, a quite large total solid angle (about $2 0 \%$ of $4 \pi$ ) can be reached and a wide angular range ( $1 0 ^ { \circ }$ to $1 5 0 ^ { \circ }$ ) can be covered, allowing precise angular distribution mea-

![](images/69c3bec733d9241d89f9e7746b594dcfa7cde9e0af268aa24d71b0359670cbed.jpg)  
Fig. 17. (Color online) T-Rex experimental setup used for the $^ { 1 0 } \mathrm { { B e } }$ , $^ { 1 1 } \mathrm { { B e } + ^ { 6 4 } \mathrm { { Z n } } }$ and 11Be+120Sn experiments at REX-ISOLDE, at CERN. Figure extracted from Ref. [149].

surements. It is also important to mention that these experiments, using low-intensity radioactive ion beams, are quite challenging from the experimental point of view. For instance, the use of detection setups with several DSSSDs demands a considerable effort in the analysis to assign the scattering and solid angles of each pixel of the array. However, all the efforts paid off, since covering a wide angular range and obtaining cross sections at very backward angles, is quite important for a better theoretical analysis and better interpretation of the influence of the several mechanisms such as breakup and transfer in the elastic scattering. The measured angular distributions obtained from these experiments have been analyzed with different approaches, such as optical model, coupled channel calculations and phenomenological models [144, 145, 146, 147]. From the optical model analysis reported in Ref. [144], the derived total reaction cross section for the ${ } ^ { 6 } \mathrm { H e } + { } ^ { 2 0 8 } \mathrm { P b }$ and 8He+208Pb systems are very similar. The decoupling of the single-particle motion of the halo with respect to the core has also motivated the application of new reactions models such as the CDCC, discussed in section 3.2. In particular, the analysis performed for the ${ } ^ { 6 } \mathrm { H e }  { + } \ { } ^ { 2 0 8 } \mathrm { P b }$ data is a good example of the success of 4b-CDCC applications, as discussed in section 3.2.

Besides the previously discussed experiments with the neutron-rich borromean beams, several experiment have been performed with $^ { 1 1 }$ Be [61, 148, 149, 150] and $\mathrm { ^ { 1 2 } B }$ beams. $\perp \perp$ Be is a typical one-neutron halo nucleus, where the valence neutron moves around the $^ { 1 0 }$ Be core in an sorbit, with the low separation energy ( $S _ { n }$ =0.503 MeV). Differently from the borromean nuclei, 11Be has the peculiarity of having one bound excited state, with excitation energy 320 keV ( $j ^ { \pi } = 1 / 2$ ).

Di Pietro et al. [148] obtained high quality quasi-elastic scattering angular distribution data for collisions of 11Be with $^ { 6 4 } \mathrm { Z n }$ , at energies around the Coulomb barrier. The experiment was performed at the REX-ISOLDE facility of CERN, using the array of six DSSSDs telescopes, shown in Fig. 17. Since the energy resolution was not good enough to distinguish between elastic scattering and inelastic scat-

tering to the excited state of $\perp \perp$ Be, the angular distributions were considered quasi-elastic in nature. They also measured breakup cross sections but, due to low statistics at the backward angles, they considered only data from the three DSSSDs telescopes. The data clearly indicates the suppression of the Coulomb $-$ nuclear interference peaks due to the halo structure of the $\perp \perp$ Be nucleus, which is an indication of strong absorption, even at forward angles. Indeed, the obtained total reaction cross section was $\sigma _ { \mathrm { { R } } } = 2 7 3 0$ mb for $\perp \perp$ Be, which is more than twice those obtained for $^ { 1 0 }$ Be ( $\sigma _ { \mathrm { { R } } } = 1 . 2 6 0 \mathrm { { m b } }$ ) and $^ { 9 }$ Be ( $\sigma _ { \mathrm { { R } } } = 1 . 0 9 0$ mb).

Another quasi-elastic scattering experiment at the REX-ISOLDE facility was performed by Acosta et al. [149]. They studied the 11Be+120Sn system, using the same setup as in the experiment of Di Pietro et al. [148], for the $\mathrm { ^ { 1 1 } B e ~ + ~ ^ { 6 4 } Z n }$ system. Despite their impressive detection system, allowing measurements of 1536 pixels and covering an angular range of $1 0 ^ { \circ }$ to $1 5 0 ^ { \circ }$ , they could only obtain reliable data at forward angles, between $1 5 ^ { \mathrm { { o } } }$ and $3 8 ^ { \circ }$ . This was mainly due to the use of a too thick target, which made it impossible to separate $_ { 1 1 }$ Be from $^ { 1 0 } \mathrm { { B e } }$ contamination at more backward angles.

Mazzoco et al. [151] measured elastic cross sections in collisions of $^ { 1 1 }$ Be projectiles on a 209Bi target, at nearbarrier energies. The experiment was performed at RIKEN, using eight two-stage $\varDelta E - E$ telescopes placed along the lateral faces of two cubes closely-packed around the target, called EXODET array [151]. Despite the large fluctuations in the cross sections, the results of the optical model analysis indicate that direct processes related to the 11Be halo structure and smaller binding energies are more important at near-barrier energies.

More recently, Pesudo et al. [61] measured elastic, inelastic and breakup angular distributions for the $^ { 1 1 } \mathrm { { B e } ~ + }$ 197Au system. The experiment was performed at TRI-UMF, Canada, with an array of 4 DSSSD telescopes surrounded by twelve high-purity germanium clovers of TI-GRESS. This setup allowed measurements of elastic and inelastic scattering events at angles ranging from $1 4 ^ { \circ }$ to157◦. The inelastic channel was identified by gating the $\perp \perp$ Be events on the 320 keV gamma-ray peak. The data were analyzed with an extended continuum-discretized coupledchannels (XCDCC), discussed in section 3.2, where the $^ { 1 0 }$ Be core excitation was considered. Theory and experiment were shown to be in excellent agreement (see Figs. 8 and 9).

Experiments on elastic scattering induced by protonrich nuclei, such as $^ 7$ Be, $^ { \mathrm { s } } \mathrm { B }$ , $^ { 9 } \mathrm { C }$ , $^ { 1 0 } \mathrm { C }$ and $^ { 1 7 } \mathrm { F }$ , on medium to heavy target, have also been performed in several laboratories, as described below. One of the first experiment with $^ 7 \mathrm { B e }$ and $^ { \mathrm { s } } \mathrm { B }$ secondary beams on medium to heavy target was performed at the University of Notre Dame, USA [152]. In this experiment, angular distributions for the elastic scattering of the 7Be, $\mathrm { ^ 8 B + ^ { 5 8 } N i }$ systems were measured simultaneously, at several energies near and above the coulomb barrier. The large derived total reaction cross sections for $^ { 8 } \mathrm { B }$ were considered an evidence of the halo ef-

fect in this nucleus. The CDCC calculations performed for the $^ { 8 } \mathrm { B } + ^ { 5 8 }$ Ni system showed the strong influence of the breakup channel in the elastic scattering [153, 154].

For heavier targets, the breakup is expected to be more prominent, since the long-range Coulomb interaction is predominant over the nuclear potential. Elastic scattering measurements for the $\mathrm { ^ 8 B + ^ { 2 0 8 } P b }$ system were performed at $E _ { \mathrm { L a b } } = 5 0$ MeV [155] and $E _ { \mathrm { L a b } } = 1 7 0$ MeV [156]. The measurement at the lower energy, close to the barrier, was performed at the CRIB facility in RIKEN, Japan, using the EXPADES detector array [157], which consisted of six DSSSD telescopes covering the angular range of $8 ^ { \circ }$ to $1 6 6 ^ { \circ }$ . The obtained angular distribution shows a quite strong damping of the Fresnel peak, although the differential cross sections data in the corresponding angular region show large fluctuations and uncertainties. The extracted total reaction cross section from an optical model analysis was $\sigma _ { \mathrm { { R } } } = 1 1 1 2 ~ $ mb, which is much larger than the one for the 7Be core on the same target, measured in the same experiment $\sigma _ { \mathrm { R } } = 2 5 3 ~ \mathrm { m b }$ ). Full CDCC calculations performed for the $\mathrm { ^ 8 B + ^ { 2 0 8 } P b }$ system poorly reproduces the experimental angular distribution, indicating that some other effect, such as core excitation, may be playing an important role for this system. For the data obtained at the higher energy, three times that of the Coulomb barrier, at the Radioactive Ion Beam Line in Lanzhou (RIBLL), the Fresnel peak is still present and the full CDCC calculation describes quite well the data [156].

Besides the data on the $\mathrm { ^ 8 B + ^ { 5 8 } N i }$ system reported in Ref. [158], elastic scattering experiments involving other boron isotopes have been performed, studying the $^ { 1 0 } \mathrm { B } \mathrm { ~ + ~ }$ 58Ni [159], $\mathrm { ^ { 1 1 } B + ^ { 5 8 } N i }$ [160] and $\mathrm { ^ { 1 2 } B + ^ { 5 8 } N i }$ [161] systems. All these data were analyzed with coupled channel calculations, and the analyses indicated that the elastic cross sections are sensitive to the cluster configuration of the projectiles. Different configurations of the boron isotopes were shown to produce different effects on the elastic angular distributions [162].

Elastic scattering experiments on collisions of $^ { 9 } \mathrm { C }$ , $^ { 1 0 } \mathrm { C }$ , $^ { 1 1 } \mathrm { C }$ , 12C, $\mathrm { ^ { 1 3 } C }$ , $^ { 1 4 } \mathrm { C }$ , and 15C beams on heavy targets have also been performed, as described below. Santra et al. [163] studied the 12C+208Pb system, measuring elastic and inelastic scattering, transfer, fission, and evaporation residue cross sections, at energies around and above the Coulomb barrier, in the range: $E _ { \mathrm { L a b } } = 5 8 . 9 - 8 4 . 9$ MeV. Simultaneous coupled reaction channel (CRC) calculations involving the elastic and all the nonelastic channels were performed. Optical-model analyses of the elastic data have been also carried out. The resulting optical potential showed a strong energy dependence, mainly at near-barrier energies, and some long-range absorption. Although elastic scattering and various nonelastic channels are studied in Ref. [163], the total reaction cross section has not been given in this work.

Several measurements of elastic cross sections in collisions of $\mathrm { ^ { 1 3 } C }$ and $^ { 1 4 } \mathrm { C }$ on heavy targets have been performed (see, for instance, the database in the website given in

Ref. [113, 114]). Most of these experiments investigated the influence of one- or two-neutron transfer reactions on the elastic process. In particular, the study of Landowne and Wolter for the $^ { 1 3 }$ C+208Pb system [164] at sub-barrier energies is one of the pioneering works in the early days on the use of single-folding potential models and on the importance of valence nucleon in elastic scattering.

Experiments with secondary beams of radioactive carbon isotopes have also been performed. Yang et al.[156, 165] measured elastic angular distributions for collisions of $^ { 9 , 1 0 , 1 1 } \mathrm { C }$ on $^ \mathrm { 2 0 8 }$ Pb. The experiments were performed at the RIBLL in Lanzhou, China, at collision energies three times the height of the Coulomb barrier. The measured angular distributions did not show any suppression of the Fresnel peak, resembling those for stable projectile. On other hand, a strong absorption has been observed for the elastic scattering of 10C+58Ni system at energies closer to the barrier, most probability due to the combination of deformation and cluster configuration [166]. The $^ { 1 0 } \mathrm { C }$ isotope is assumed to be the only nucleus to have a brunnian (super-borromean) structure, where the four interconnected rings are associated to the four-body interactions $( \alpha + \alpha + p + p )$ [167, 168].

An interesting experiment was performed with the AT-LAS accelerator, at ANL, to measure fusion reactions for the 12,13,14,15C $^ +$ 232Th systems, at near-barrier energies [169]. The $^ { 1 5 }$ C nucleus is a good candidate for an exotic halo nucleus. The valence neutron is orbiting around the $^ { 1 4 } \mathrm { C }$ core, in an $s _ { 1 / 2 }$ orbit with a binding energy of $\mathrm { S } _ { n } { = } 1 . 2 1 8$ MeV. The experiment showed that, at the lowest energies, the fusion-fission cross sections for $^ { 1 5 } \mathrm { C } + ^ { 2 3 2 } \mathrm { T h }$ is enhanced by a factor of 5, in comparison to those for $^ { 1 2 , 1 3 , 1 4 } \mathrm { C }$ projectiles. Considering that, at this very low energy, the fusion-fission would exhaust the total reaction cross section, this is an indication of large total reaction cross section, typical of an exotic nucleus.

Very recently an elastic scattering experiment for the 15C+208Pb system was performed at the HIE-ISOLDE facility, at CERN [170]. Although they used the GLORIA detector array [142], which covers a large solid angle and angular range of $1 5 ^ { \mathrm { { o } } }$ to $1 6 5 ^ { \circ }$ , the cross sections were determined only at the most forward angles. The preliminary data indicated a strong absorption and strong damping of the Fresnel peak.

Laboratories as GANIL (France), NSCL-MSU (USA), ANL (USA), RIKEN (Japan), TRIUMF (Canada), RI-BLL (China), Dubna (Russia) etc. are producing several other radioactive ion beams, with $Z \ > \ 6$ , such as $^ { 1 2 }$ N, 13O, $^ { 1 4 } \mathrm { O }$ , 17F, and $\mathbf { \bot 7 }$ Ne etc. However, most of the experiments are related to the investigation of the structure of these nuclei, using reactions on light targets (H and He) at high energies (> 50MeV/A). Very few experiments are being performed to measure reactions induced by radioactive nuclei with $Z > 6$ on medium to heavy target. The exception is the $^ { 1 7 } \mathrm { F }$ nucleus, where some efforts have been devoted to measure elastic scattering, breakup and fusion reaction. Fluorine-17 is a weakly-bound proton drip line

![](images/66e77547061f4f1ab5c28b838bcc666e5145243914eceb5dc009d2477e2dcccd.jpg)

![](images/fa0c0a417acbb15b90ed834ee85daf36e71e5e18e36755f89e3fdd22f6d8c297.jpg)  
Fig. 18. (Color online) Time-dependent density distribution of: (a) the neutron; (b) the proton valence particle (figure extracted from Ref. [175]).

nucleus, where the valence proton has the binding energy $S _ { p } = 0 . 6 0 1$ MeV. One of the first experiment involving $^ { 1 7 } \mathrm { F }$ was the fusion-fission measurement of 17F+208Pb performed at energies in the vicinity of the Coulomb barrier at ANL, USA [130]. For proton drip-line nuclei, the breakup process produces a residual nucleus (the core), with one less proton, and thus with a lower Coulomb barrier. This is expected to lead to appreciable incomplete fusion, and to large total fusion cross sections. However, no enhancement of fusion-fission yields due to breakup or to a large interaction radius was observed in this experiment.

Later, some other experiments were performed [171] at the Holifield Radioactive Ion Beam Facility (HRIBF) at Oak Ridge, USA, to measure elastic scattering and breakup of the same 17F+208Pb system [172, 173]. In these works, a discussion on the diffraction and stripping breakup was presented, where the late is related to incomplete fusion of the proton fragment. Their results suggested that, for proton-rich nuclei, sub-barrier fusion would be suppressed. This is in sharp contrast with the large subbarrier fusion enhancements observed for the exotic neutronrich nucleus $_ 6$ He [174].

There has been some speculation about the possible polarizability of the proton- and neutron-rich exotic nuclei, as they approach a heavy target. In the case of a proton halo nucleus, both the valence proton and the core would be scattered to the backward direction by the Coulom field of the target. On the other hand, for neutron-rich nuclei, the charged core is repelled by the Coulomb field, whereas the neutron halo is not affected. In this way, the neutron-rich projectile would be polarized along the collision. This idea is corroborated by the time-dependent dynamic calculation of the fusion process by Ito et al. [175], illustrated in Fig.18. The figure shows time evolutions of the projectile’s density in a collision of a neutronrich (panel (a)) and of a proton-rich (panel (b)) projectile with a heavy target, at a sub-barrier energy.

Due to the high interest in investigations of breakup effects in fusion, elastic and total reaction cross sections for proton-rich nuclei, other elastic scattering experiments were carried out, for the 17F+208Pb [176] and 17F+58Ni [177] systems at near-barrier energies. The experiments were performed at INFN-LNL, Italy, using the EXOTIC

![](images/7582e51a0672b408628efc0cc49718487450695e6d68f8ba669f673d9ed1d61a.jpg)  
Fig. 19. (Color online) Cross section for total reaction, inclusive and exclusive breakup and fusion. Figure taken from Ref. [176].

facility [121]. In these experiments the charged particles coming out from the reaction were detected by the EX-ODET detector array, which consisted of eight $\varDelta E$ - $E$ telescopes arranged as faces of two cubes closely packed in the front and at the back side of the target [178]. This setup covered a solid angle of about 70% of $4 \pi$ sr and allowed the coincidence detection of both $^ { 1 6 }$ O and $p$ fragments from the $^ { 1 7 } \mathrm { F }$ breakup (exclusive breakup). The results for the 17F+208Pb system are summarized in Fig. 19. At energies below the coulomb barrier ( $\mathrm { V _ { B } } \ : = \ : 9 2 . 0$ MeV), the sum of exclusive breakup and fusion exhausted the total reaction cross section. Above the barrier, the inclusive breakup, where only the $^ { 1 6 }$ O fragment is detected, was quite strong. The conclusion is that the reactivity of the proton-rich 17F nucleus is not very large. Thus, the small binding energy of the valence proton plays a minor role in the reaction dynamics.

Very recently, another experiment for the $^ { 1 7 } \mathrm { F } + ^ { 5 8 } \mathrm { N i }$ system was performed at the CRIB, RIKEN, Japan. In this experiment, elastic, breakup and fusion cross sections were measured using a multilayer ionization-chamber telescope Array (MITA) [179], shown in Fig. 20. This device bis a combination of 10 independent telescopes, where each of them consists of four stages detectors: one ionization chamber, followed by thin (40 or $6 0 ~ \mu \mathrm { { m } }$ ) DSSSD and two layers of thick (300 and $1 0 0 0 \ \mu \mathrm { m }$ ) quadrant silicon detectors (QSDs). The possibility of detecting, distinguishing and separating high Z particle as well as light particles enables the simultaneous measurements of all the important reactions (elastic, breakup and fusion) produced in the collision, where the ionization chamber is important to measure energy loss of high Z particles. A single angular distribution for the elastic scattering is presented in Ref. [179]. The full set of data of this experiment is been submitted for publication and the results is promising and very much awaited.

Usually different experimental setups, not always available at the same laboratory, would be required to measure the different reaction channels produced in a collision be-

![](images/2579d8528cbea5ab70d51a487d62517a591c078789e41d2c3ccd67170fe8e49e.jpg)

![](images/8300efc848d29a8527e2c926d6794da71efcad229235d0f058e7bc247c5a7f6a.jpg)  
Fig. 20. (Color online) View of general structure and the photograph of the assembled multilayer ionization-chamber telescope array MITA. Figure extracted from Ref. [179].

tween heavy nuclei. In most cases, it would demand different measurements at different times and, consequently, it would take several years to get information on all channels for a given system.

An example of such an effort is the work developed at University of Notre Dame to investigate the channels involved in the collision of $_ 6$ He on a $^ { 2 0 9 }$ Bi target. The different reactions were measured in different experiments, using different setups, such as sub-fusion measurement ( $1 n , 2 n , 3 n$ evaporation) [174], fusion-fission [180], fusionevaporation ( $_ { 4 n }$ evaporation) [181], transfer and breakup [182], elastic scattering [183], $2 n$ -transfer [184] and breakup [185]. The discussion of these mechanisms, in terms of total reaction cross section and evidence for core-halo decoupling, was reported in Ref. [186]. A similar effort was also devoted to the 8B+58Ni system, where elastic [158], breakup [187, 188] and fusion cross sections [189] were measured in different experiments, and with different setups. The discussion of the total reaction cross section for this system was reported in Ref. [190]. The sum of the total fusion plus breakup cross sections gives about the same large total cross section as those extracted from elastic scattering, see Fig. 21.

# 5.2 Direct measurements and total reaction cross section

In the previous section, some experiments on the elastic scattering of radioactive ion beams were highlighted. The total reaction cross sections were extracted from optical model (OM) analyses of the scattering data.

However, this indirect method has a limitation. It relies on a precise determination of the optical potential, which

![](images/2899cd42c785a49872dccb6c3bc3dc6e7da77f09fcb06446adefe0a3c96d0123.jpg)  
Fig. 21. (Color online) The several cross sections for $\mathrm { ^ 8 B + ^ { 5 8 } N i }$ system, as indicated. The fusion curve was calculated using the S˜ao Paulo potential. Figure extracted from Ref. [190].

requires accurate elastic scattering data over a fine angular mesh. Frequently, this condition is not met, mainly in collisions of exotic nuclei. On the other hand, some direct methods to measure the total reaction cross section have been developed, and reported in the literature. A brief discussion of these methods is presented below.

# Sum of differences

The sum of difference method, described in section 2.3, is a very convenient way to obtain the total reaction cross section and information on the nuclear interaction from the elastic angular distribution at very forward angles. In this angular region, heavy-ion scattering exhibits oscillations, known as forward glory effect. These oscillations result from the interference between the nuclear and Coulomb scattering amplitudes. As the Coulomb amplitude is known analytically, it is possible to extract $f _ { \mathrm { N } } ( \theta =$ 0) from the data, and then obtain the total reaction cross section (see section 2.3).

This method was used to investigate forward nuclear glory in the scattering of the $^ { 1 2 } \mathrm { C } + ^ { 1 2 } \mathrm { C }$ system of identical nuclei [38]. Total reaction cross sections were extracted and a clear evidence of nuclear glory in heavy-ion collisions was observed. In another experiment, this method was used to study collisions of $\mathrm { ^ { 1 2 } C }$ , $\mathrm { ^ { 1 3 } C }$ , $^ { 1 5 }$ N and $^ { 1 6 }$ O projectiles on $^ { 2 8 }$ Si targets [191]. The elastic scattering data were used to extract the total reaction cross section and to investigate the importance of the neutron transfer in the reaction.

Ueda and Takigawa studied the forward glory effect in collisions of the two-neutron halo $\perp \perp$ Li nucleus on $\mathrm { ^ { 1 2 } C }$ , within a semiclassical approximation [192]. They found that the halo of $\perp \perp$ Li leads to a higher glory angular momentum and shifts the first glory minimum towards a smaller angle. Further, they concluded that these features enhance the oscillations of the nuclear amplitude in the sum of difference analysis.

To investigate these effects, Ostrowski et al. [193] measured elastic angular distributions for the $\mathrm { ^ { 6 } H e + ^ { 1 2 } C }$ system at forward angles. The experiment was performed at

Louvain-la-Neuve, Belgium. They concluded that the low neutron binding energy of 6He reduces the nuclear forward glory effect due to flux losses from the elastic channel to breakup or transfer channel, and that the total reaction cross section for this weakly bound system is twice as high at that for for $\mathrm { ^ 6 L i + ^ { 1 2 } C }$ at the same Coulomb parameter value.

# Backscattering cross section

A simple method to extract the total reaction cross section has been proposed by Sargsyan et al. [194], which consists of using only the cross section measured at very backward angles.

The starting point is the usual expression for the total reaction cross section,

$$
\sigma_ {\mathrm {R}} (E) = \frac {\pi}{K ^ {2}} \sum_ {J = 0} ^ {\infty} (2 J + 1) \mathcal {P} _ {\mathrm {R}} (J, E), \tag {145}
$$

where $\mathcal { P } _ { \mathrm { R } } ( J , E )$ is the total reaction probability in a collision with energy $E$ and angular momentum $J$ . Then, $\mathcal { P } _ { \mathrm { R } } ( 0 , E )$ is written in terms of the elastic scattering probability for $J = 0$ ,

$$
\mathcal {P} _ {\mathrm {R}} (0, E) = 1 - \mathcal {P} _ {\mathrm {e l}} (0, E), \tag {146}
$$

and $\mathcal { P } _ { \mathrm { e l } } ( 0 , E )$ is approximated by the ratio between the elastic and the Rutherford cross sections at $\theta \ : = \ : 1 8 0 ^ { \circ }$ , namely

$$
\mathcal {P} _ {\mathrm {e l}} (0, E) \simeq \left[ \frac {d \sigma_ {\mathrm {e l}} (\theta) / d \Omega}{d \sigma_ {\mathrm {R u t h}} (\theta) / d \Omega} \right] _ {\theta = 1 8 0 ^ {\circ}}. \tag {147}
$$

Next, the total reaction probabilities for $J \ne 0$ are approximated by the probability at $J = 0$ , but at the lower energy

$$
E ^ {\prime} = E - \frac {\hbar^ {2}}{2 \mu R _ {J} ^ {2}} J (J + 1), \tag {148}
$$

where $R _ { J }$ is the radius of the barrier of the effective potential (including the centrifugal term), $V _ { J } ( R )$ .

The sum over $J$ in Eq. (145) is then transformed into an integral over $E ^ { \prime }$ involving $\mathcal { P } _ { \mathrm { R } } ( 0 , E ^ { \prime } )$ , which is related to the backscattering scattering data ( $\theta _ { \mathrm { L a b } } > 1 5 0 ^ { \circ }$ ), through Eqs. (146) and (147).

To assess the validity of the method, Sargsyan et al. [194] used it to evaluate cross sections for several systems: $\mathrm { ^ 4 H e \mathrm { ~ + ~ } ^ { 9 2 } M o }$ , $^ { 4 } \mathrm { H e } \mathrm { ~ + ~ } ^ { 1 1 0 } \mathrm { C d }$ , $^ { 4 } \mathrm { H e } \mathrm { ~ + ~ } ^ { 1 1 0 } \mathrm { C d }$ , $^ { 4 } \mathrm { H e } \mathrm { ~ + ~ } ^ { \mathrm { 1 1 6 } } \mathrm { C d }$ , $\mathrm { ^ { 4 } H e } + \mathrm { ^ { 1 1 2 } S n }$ , $\mathrm { ^ { 4 } H e } + \mathrm { ^ { 1 2 0 } S n }$ , $\mathrm { ^ { 1 6 } O + ^ { 2 0 8 } P b }$ and $^ { 6 , 7 } \mathrm { L i } + ^ { 6 4 } \mathrm { Z n }$ . In each case, the obtained cross section was compared with total reaction data obtained by the standard method, fitting elastic angular distributions. The overall agreement was good, except for the $\mathrm { ^ { 1 6 } O \ + \ ^ { 2 0 8 } P b }$ and $^ { 6 } \mathrm { { L i } + ^ { 6 4 } \mathrm { { Z n } } }$ systems. There was no clear justification for these discrepancies. The authors suggested that it might be related to the uncertainties in the elastic data at backward angles.

An analogous procedure can be used to determine the capture component of the total reaction cross section. In this case, one replaces in Eq. (146) the elastic cross section by the quasi-elastic one, and truncate the $J$ -sum of Eq. (145) at the critical angular momentum (the limit of integration over $E ^ { \prime }$ is modified accordingly). Using this method, capture cross sections for the $^ { 6 , 7 } \mathrm { L i } + ^ { 6 4 } \mathrm { Z n }$ systems were determined in Ref. [194].

Guimar˜aes et al. [195] performed a dedicated backscattering experiment to determine the elastic cross section for the ${ } ^ { 6 } \mathrm { H e } + { } ^ { 2 0 9 } \mathrm { B i }$ system, at sub-barrier energies. They measured cross sections at $1 5 0 ^ { \circ }$ , with uncertainties better than 10%. Several other elastic scattering data sets for collisions of exotic beams at back angles ( $1 5 0 ^ { \circ }$ or higher) are available in the literature. However, usually they have uncertainties of not less than $2 0 \%$ . Thus, it would be interesting to employ the backscattering method to determine the total reaction cross section for the ${ } ^ { 6 } \mathrm { H e } + { } ^ { 2 0 9 } \mathrm { B i }$ system, using the data of Ref. [195].

# Total cross section from beam attenuation

The beam attenuation or transmission method is an old and quite simple direct method to obtain the total reaction cross section [196, 197]. In this method, one measures the number of particles in the incident beam, $N _ { \mathrm { B } }$ , and the number of unscattered particles plus particles scattered elastically, after the beam traverses a thick target, $N _ { \mathrm { T } }$ . The difference of the two is proportional to the total reaction cross section. That is,

$$
\sigma_ {\mathrm {R}} = k \times \left[ \frac {N _ {\mathrm {B}} - N _ {\mathrm {T}}}{N _ {\mathrm {B}}} \right], \tag {149}
$$

where $k$ is a constant related to the target thickness. This is a reliable method to be applied to nucleus-nucleus collisions at medium to high energies (10-50 MeV/A). At first, it was used to measure the total reaction cross section in collisions of light particles $\textstyle p , d , t$ and $\alpha$ ) with several targets, mostly for practical applications in reactors and space science [198].

This method was first applied in an experiment performed at CERN, to measure the total reaction cross section for the $^ { 1 2 } \mathrm { C } + ^ { 1 2 } \mathrm { C }$ system [196]. An improvement of the method was achieved when TOF was added to the $\varDelta E - E$ signals for a better identification of the particles. Details can be found in the work of Zheng et al. [199], reporting their experiment to study of the halo structure of $^ { 1 6 }$ C, performed at RIKEN.

Using a simular approach, Erdemshimeg et al. [200] performed experiments at the Flerov Laboratory of Nuclear Reactions, JINR, Russia. They measured total reaction cross sections in collisions of $^ { 4 , 6 , 8 }$ He, 7,9,10,11,12Be, 7,8,9Li and 8,10,11,12B projectiles on $^ { 2 8 }$ Si targets, at energies in the range $( 1 0 - 5 0 ) \mathrm { M e V } \cdot A$ . A smooth mass dependence was observed for the extracted radius, but with

fluctuations for some particular projectiles. These fluctuations might be an indication of halo structure.

Another interesting experiment was performed at the Radioactive Ion Beam Line in Lanzhou (RIBLL) at the HIRFL, China. Li et al. [201] measured total reaction cross sections in collisions of the mirror nuclei $^ { 1 2 }$ N and $\mathrm { ^ { 1 2 } B }$ on $^ { 2 8 }$ Si. The data were analyzed by Glauber model calculations, using gaussian-gaussian distributions [202] for the nuclear densities of 12N and $\boldsymbol { ^ { 1 2 } \mathrm { B } }$ . The parameters of the densities were then fitted to reproduce the total reaction data. The density of $^ { 1 2 }$ N obtained in this way is consistent with the $^ { 1 1 } \mathrm { C } + p$ cluster configuration.

# Total reaction cross section by solid active target method

The pioneering work of Tanihata et al. [139] on the interaction cross section11 in collisions of the radioactive lithium and beryllium isotopes triggered a series of experiments to measure total reaction cross sections for halo nuclei.

A simple method has been developed for this purpose, using solid active targets. In this method, the incident particles are stopped within the solid-state detector, which has the double function of detector and target. Owing to the $Q$ -value of the non-reacting events ( $Q = 0$ ), it is possible to distinguish them from reacting events. The former produce a sharp peak, with large intensity, at the beam energy, $E _ { 0 }$ , whereas reactive events give much weaker contributions to the spectrum at different energies ( $E = E _ { 0 } + Q$ ). The energy signal in coincidence with $\gamma$ -ray signals from a surrounding $4 \pi$ array of NaI(Tl) detectors can help to clean the energy spectra from spurious events, mainly in the energy region of $Q \sim 0$ . The reaction probability, $\mathcal { P } _ { \mathrm { R } }$ , is then determined by dividing the number of reactive events (outside of the sharp elastic peak) by the total number of counts in this spectrum.

This method was first applied at GANIL, for silicon target-detectors and light radioactive projectiles at intermediate energies (20-50 MeV/A) [203]. In this experiment, the mean (energy-integrated) total reaction cross section and the associated reduced radius, $r _ { 0 } ^ { 2 }$ , were obtained for several neutron-rich radioactive nuclei in the mass range $8 < A < 4 0$ , such as $^ { 8 } \mathrm { H e }$ , 12Be, 15B, 22O, $^ { 2 6 }$ Ne, 37Si. The authors observed a strong isospin-dependence in the total reaction cross section and in the reduced radius for all isobars with $A = 1 0$ to 18.

Applying this technique and using a stack of silicon detectors, Warner et al. [204, 205] performed several experiments with proton- and neutron-rich radioactive beams at the NSCL-MSU laboratory. They performed simultaneous measurements of total reaction and multi-nucleon

removal cross sections at intermediate energies. The radioactive nuclei were separated by the A1200 analyzing system of this laboratory [206] and impinged on a stack of silicon detectors. Reaction events were then identified by the total energy loss in the telescope, which is different from that of non-reacting projectiles. Since the projectile’s energy decreases as it travels through the telescopes, the cross sections were obtained at different energies by identifying in which detector the reaction occurred. The obtained data were interpreted with the phenomenological strong absorption models and the optical limit of Glauber multiple-scattering theory. The later reproduced quite well the data.

The above technique has also been applied to low energy incident projectiles [207]. In this case, the short-range of the particles within the detector is an important issue to be considered. Besides, the reaction probability is substantially reduced by the Coulomb barrier, and this reduction leads to a low signal-to-noise ratio. Further, particles may backscatter and then leave the detector without loosing completely its energy. This would yield a small pulse that would be misinterpreted as a reaction event [208]. Using this technique, total reaction cross section were obtained for the $^ { 6 , 7 } \mathrm { L i } + ^ { 2 8 } \mathrm { S i }$ systems at near-barrier energies [209]. The measured excitation function for the total reaction cross section agrees with the data obtained in previous standard experiments, where the total reaction cross section is determined from optical model analysis of angular distributions.

The active silicon target technique has also been used to study fusion of exotic nuclei. An experiment to measure fusion cross sections for the $^ { 8 } \mathrm { { B } + ^ { 2 8 } \mathrm { { S i } } }$ system was performed at LNL, Italy [210]. The $^ { \mathrm { s } } \mathrm { B }$ secondary beam was produced at the EXOTIC facility and, from the detected evaporated alpha particles, the authors determined complete fusion cross sections at several energies above the Coulomb barrier. This measurement was based on the assumption that the observed alpha particles resulted exclusively from the evaporation of the compound nucleus formed in the collision. Their fusion excitation function was compared to data for several other weakly and tightly bound systems, measured in different experiments. To eliminate the influence of trivial factors, like charges and masses of the collision partners, the data were reduced by the fusion function method [42, 43] (see section 5.3). They concluded that their reduced complete fusion cross section was similar to the data of most other systems, and to the predictions of barrier penetration models. The exception was the $^ { 8 } \mathrm { B } + ^ { 5 8 }$ Ni data of Ref. [189], obtained from the proton evaporation multiplicity. These data were much larger that those for the other systems, above and below the barrier. The 8B + 58Ni and $\mathrm { ^ 8 B + ^ { 2 8 } S i }$ data were later analyzed on the same basis and potentials assumptions and they were shown to be consistent with each other and in the fusion enhancement, despite the small overlap of the collision energies [211]. To clarify this issue, a new experiment was performed at the Cyclotron Institute of the Texas A&M University, USA, involving a similar system. Direct measurements of the fusion cross sections for the

![](images/461add61c8c7adc86892f084dd3b0ad4fb40602de31f17023d982b17d23c1ca1.jpg)  
Fig. 22. (Color online) Working principle of an Active target. Figure extracted from Ref. [134].

$\mathrm { ^ { 8 } B \ + \ ^ { 4 0 } A r }$ system were performed, using the gaseous active target TexAT [212] (this technique is discussed in the next section). The final results of this study are expected to be soon available.

# Promising future methods

As described in the previous sections, facilities offering radioactive ion beams are constantly improving, and developing new techniques to overcome the limitations due to the low beam intensity. One of these techniques is the use of active gaseous targets. They consist of an ionizing gas, which plays the double role of target and detector. Their geometry allows a high solid angle detection (4π), they have variable thickness, and great detection efficiency. In addition, they have good resolution, since the locations of the reaction events within the target are accurately measured.

The working principle of an active target is schematically represented in Fig. 22. The trajectory of the incident projectile (thick red line) ends at the point where the reaction takes place (red circle), giving rise to reaction products - two in this example - that follow new trajectories (thin lines). Along the trajectories, the particles ionize the medium, producing free electrons. These electrons move under the action of the vertical electric field, until they are detected on the segmented horizontal plane (bottom of the figure). In this way, the projections of the three trajectories on the horizontal $( x - y )$ plane are determined. Then, three-dimensional trajectories are constructed using the information of the drift time of the pulses detected on the horizontal plane. The high luminosities achieved in gaseous active targets (due to their large dimensions in comparison with a target foil) are of great importance in experiments involving low intensity radioactive ion beams.

Active targets as the IKAR, at GSI [213], and the MAYA, at GANIL [214], have been used for a long time,

to investigate resonant scattering and transfer reactions on hydrogen and helium targets in inverse kinematics. A review on the existing active target and its corresponding working principles can be found in Ref. [215, 216].

A new generation of active targets, based on a time projection chamber, are becoming operational. The electrons produced by the particles inside the gaseous target drift towards a micromegas plane, which multiplies them and provide position and time information of the particle tracks. This allows a complete kinematical reconstruction of the reaction in the 3-dimensional space. The ACTAR-TPC, at GANIL [217], the TexAT, at Texas A & M University [212], and the AT-TPC, at NSCL-MSU/University of Notre dame [218] are examples of such new generation devices. More recently, the prototype AT-TPC was used to measure fusion cross sections for the 10Be+40Ar system [219], indicating that this new technique can be extended to experiments with heavy targets (at least in the case of 40Ar). This kind of device is quite promising to allow the simultaneous measurement of complete fusion, incomplete fusion, breakup, scattering, and transfer reactions, in one experiment, which is a dream for experimentalist.

Another promising experimental technique, not yet fully explored for reaction measurements, is based on the stored ion beams. The use of a heavy-ion storage ring with internal gas-jet targets, such as the ESR, at GSI [220], or the HIRFL-CSR, at Lanzhou [221], allows a great increase of the beam luminosity, since the beam revolutions in a closed trajectory with a very high frequency ( $\sim 1 0 ^ { 6 }$ MHz). However, a major challenge of this technique is to install a detector setup compatible with the ultra-high vacuum regime (in the order of $1 0 ^ { - 1 0 }$ mbar or below) needed to the operation of a storage ring. At this level any type of outgassing material can significantly deteriorate the vacuum conditions [222]. Recently, nuclear reaction experiments were successfully performed at the heavy-ion storage ring at the GSI facility, using stored 56,58Ni beams, and hydrogen and helium internal gas-jet targets. The recoiled particles were detected by in-ring DSSSDs and angular distributions were measured, allowing studies of nuclear matter [223, 224] and giant resonances [225]. In the future this type of technique may be applied to investigate nuclear reactions using heavy jet gas targets.

# 5.3 Comparative studies of cross sections

It is well known that total reaction cross sections in heavyion collisions at near-barrier energies have important contributions from fusion and also from direct reactions (inelastic scattering, transfer, and breakup). Besides, couplings with direct reaction channels may exert a strong influence on the fusion cross section itself [226, 227, 228]. An important example is the collision of a heavy or medium mass projectile with a strongly deformed target [229] at sub-barrier energies. The fusion cross section is several orders of magnitude larger than those for the same projectile

![](images/594a71e1c9ea204b16ecaa6473f8ae30eb55c0351f795b29a97e0793d7a5939a.jpg)  
show direct results of the calculations, without any kind of reduction. In each curve,Fig. 23. (Color online) Comparison of the total reaction cross sections for several systems, obtained through single-channel calculations. (Figure taken from Ref. [230]).

e concludes that Gomes’ method is definitely much better. This is particon a spherical target with similar mass. In this way, the enets, where it almost produces a universal curve.hancement of the fusion cross section may be a signature of the deformation. Nevertheless, despite this enhancement, ight targets, represented by 58Ni and 64Zn (Fig. 6), medium-heavy targethe total reaction cross section is still dominated by direct 44Sm (Fig. 7), and heavy targets, represented by 208Pb and 209Bi (Fig. 8). Toreactions in this energy region. Another example, which ng from the limitations of the reduction method, each experimental cross shas attracted considerable interest in the last few decades, ding theoretical curve. When the theoretical curves of two systems are veis the suppression of complete fusion in collisions of weakly me plot. The reductions were performed by the Gomes’s method. bound nuclei (see e.g. Ref. [4] and references therein).

ention in the energy region above the Coulomb barrier, since theClearly, comparisons of fusion and/or reaction data for ions are obtained from elastic scattering data. At sub-barrier energies thedifferent systems is a very useful tool in studies of nuclear rford type.structure and reaction mechanisms. However, direct com-7Al (Fig. 5) target, one can observe that the reaction cross section forparisons of data for different systems may be misleading. h the theoretical curve, whereas for the weakly bound 6Li, 7Li, 9Be andThe reason is that the cross sections also depend on trivcross section is just a little above the theoretical curves. Data used in thial properties of the system, like the charges and sizes of the collision partners. We illustrate this point with an exthe results for the medium-mass targets 58Ni and 64Zn. Similar concample. We consider the cross sections for collisions of $^ { 1 6 } \mathrm { O }$ and stable weakly bound projeprojectiles with energy $E _ { \mathrm { l a b } } = 5 0$ w the enhancement of the hal MeV on two different B and the neutron-halo 6Hetargets: the spherical $^ { 4 0 }$ d 11Be, cross sections with respect to the Ca and the highly deformed 154Sm nuclei. Estimating the cross sections by potential scatterthe Sn, Ba and Sm medium-heavy targets are shown in Fig. 7. Ting calculations with the Aky¨uz-Winther potential [18, 19] y similar to the one observed for medium-mass taand short-range absorption, one finds $\sigma _ { \mathrm { { F } } } ~ = ~ 7 6 4 ~ \mathrm { { m b } }$ his ca for o $^ { 4 0 }$ Refs. [48,6Ca and $\sigma _ { \mathrm { { F } } } = 0 . 6 \times 1 0 ^ { - 1 0 }$ mb for $^ \mathrm { 1 5 4 }$ Sm. Clearly, the show the reduced cross sections for the Pb and Bi heavy targets.comparison of these cross sections at the same beam enion for the tightly bound O projectile still coinci6 9ergy is meaningless. In the case of the $^ { 4 0 }$ with the theoreticaCa target, the es, the differences between data and tbeam energy corresponds to $E _ { \mathrm { c , m . } } = 3 5 . 7$ are larger than for MeV and the also larger thbarrier is $V _ { \mathrm { B } } = 2 4$ or the same projectiles on lighter targets. Data are  MeV, whereas for 154Sm the energy is $E _ { \mathrm { c , m . } } = 4 5 . 3$ MeV and the barrier $V _ { \mathrm { B } } = 6 0$ MeV. Thus, er than the stable weakly bound nuclei. The latter present cross sections sthe vanishingly small cross section for the heavier target projectiles. Furthermore, these differences are more important when his a trivial consequence of the fact that the collision eng almost negligible for light targets.ergy is almost 15 MeV below the Coulomb barrier. At this very low energy, all nonelastic cross sections are extremely low. The importance of the barrier height in comparisons of cross sections for different systems emerges more clearly in Fig. 23, which shows fusion cross sections for systems in different mass regions, as functions of the collision energy in the center of mass frame. One observes that this kind of comparison does not reveal any physical property of these systems. It only shows trivial differences in the Coulomb barriers. The examples discussed above clearly show that static properties, like the barrier height and geometric ef-

fects arising from the size of the system, must be eliminated from the analysis. For this purpose, it is necessary to make transformations on the collision energy and on the cross section to get rid of these trivial factors. This procedure is known as reduction. Several reduction methods have been proposed over the last two decades. Detailed discussions of this subject, pointing out their successes and shortcomings, can be found, e.g., in Refs. [4, 44, 230]. Some of the main reduction methods available in the literature are discussed below.

We begin with the traditional reduction method, which consists in the transformations,

$$
E \rightarrow E _ {\text {r e d}} = \frac {E}{V _ {\mathrm {B}}}, \tag {150}
$$

$$
\sigma \rightarrow \sigma_ {\mathrm {r e d}} = \frac {\sigma}{\pi R _ {\mathrm {B}} ^ {2}}. \tag {151}
$$

anels at the leftQualitatively, the above transformations go in the right arly clear in thedirection. They modify the scales of the x- and y-axes of Fig. 23, bringing the curves of the different systems to the esented by 27Alsame region12.

resented byThe second method considered here, proposed by Gomes et al. [231], adopts the transformations,

$$
E \rightarrow E _ {\mathrm {r e d}} = E \times \left[ \frac {Z _ {\mathrm {P}} Z _ {\mathrm {T}}}{A _ {\mathrm {P}} ^ {1 / 3} + A _ {\mathrm {T}} ^ {1 / 3}} \right] ^ {- 1}
$$

$$
\sigma \rightarrow \sigma_ {\mathrm {r e d}} = \frac {\sigma}{\left(A _ {\mathrm {P}} ^ {1 / 3} + A _ {\mathrm {T}} ^ {1 / 3}\right) ^ {2}}. \tag {152}
$$

This method, inspired by the previous one, is based on the he neutron-haloassumptions that the barrier radius scales like $A _ { \mathrm { P } } ^ { 1 / 3 } + A _ { \mathrm { T } } ^ { 1 / 3 }$ figure are fromand that the potential barrier can be approximated by the Coulomb potential at the barrier radius. Thus, it scales an belike $Z _ { \mathrm { P } } Z _ { \mathrm { T } } / ( A _ { \mathrm { P } } ^ { 1 / 3 } + A _ { \mathrm { T } } ^ { 1 / 3 } )$ . This method has the advantage projectiles, bothof being independent of the parameters of the interaction eoretical curvpotential, $V _ { \mathrm { B } }$ and $R _ { \mathrm { B } }$ .

avior of theThe above methods have been widely used to reduce , the figures arereaction and fusion data. However, a comprehensive study of reduction methods for fusion cross sections, considering ne can observea large number of systems in different mass ranges [42, 43], curve, whereasconcluded that the best results were achieved by the fuutron-halo Hesion function method, which is discussed below.

The fusion function method hinges on the use of the nt total reactionWong’s formula for the fusion cross section (Eq.(23)). The collision energy and the cross section are replaced by the dimensionless quantities [42, 43],

$$
E \rightarrow x = \frac {E - V _ {\mathrm {B}}}{\hbar \omega}; \quad \sigma (E) \rightarrow F (x) = \frac {2 E}{\hbar \omega R _ {\mathrm {B}} ^ {2}} \times \sigma (E). \tag {153}
$$

It can be immediately checked that if one applies the reduction method to the Wong’s cross section itself, one gets

$$
F _ {0} (x) = \ln \left[ 1 + e ^ {2 \pi x} \right]. \tag {154}
$$

The above function, being basically independent on the system, is called Universal Fusion Function (UFF). The UFF would be a good representation of the reduced fusion data when they can be described by a one-channel calculations with a standard interaction, like the S˜ao Paulo [15, 16] or the Aky¨uz-Winther [18, 19] potential, with shortrange absorption. The Wong’s formula is a reasonable approximation in heavy-ion fusion at near-barrier energies. For heavy systems ( $Z _ { \mathrm { P } } ~ Z _ { \mathrm { P } } ~ \gtrsim ~ 2 5 0$ ), it remains valid down to several MeV below $V _ { \mathrm { B } }$ . However, for lighter systems it deteriorates more rapidly as the energy decreases below $V _ { \mathrm { B } }$ . A detailed discussion of the reduction of fusion data is presented in the next section.

# Reduction of fusion cross sections

The reduction of fusion cross sections by different methods has been systematically investigated in Ref. [44]. The methods were submitted to a simple test. They were used to reduce theoretical cross sections obtained by one-channel calculations using the Aky¨uz-Winther potential and strong short-range absorption. This study involved several systems in different mass regions. Since there are no nuclear structure effects in these calculations, a successful reduction method should lead to reduced cross section with very weak system dependence. This study has shown that only the fusion function method meets this criterium. The other methods kept important system dependence, mainly in comparisons of reduced cross sections for systems in different mass ranges.

The reduction of fusion cross sections by the fusion function method is carried out in two steps, as follows.

1. The Coulomb barrier calculated with some version of the double-folding potential, like the AW or the SPP, is fitted by a parabola, and the barrier parameters $R _ { \mathrm { B } }$ , $V _ { \mathrm { B } }$ , and $\hbar \omega$ are determined.   
2. The data points, $\{ E _ { i } , \sigma ( E _ { i } ) \}$ , are converted to reduced data points, $\{ x _ { i } , F _ { \mathrm { e x p } } ( x _ { i } ) \}$ , according to Eq. (153).

If there are no relevant channel coupling effects and the Wong’s formula gives an accurate description of the optical model cross section, the experimental fusion function, $F _ { \mathrm { e x p } } ( x )$ , is expected to be very close to the UFF. In this way, the function $F _ { 0 } ( x )$ can be used as a benchmark, to which $F _ { \mathrm { e x p } } ( x )$ should be compared. Deviations from the UFF in a given energy region indicates that the Wong’s formula is inaccurate there, or it is an evidence of relevant channel coupling effects. In the latter case, the strength of the deviation measures the importance of the couplings. In most collisions, couplings with direct reaction channels play an important role in the reaction dynamics. Then, the fusion data can not be accurately described by onechannel calculations with typical heavy-ion potentials.

Usually, one wants to assess the influence of some specific process on fusion, like the breakup. Then, there may be a difficulty. The deviations of the experimental fusion

function from the UFF may arise from breakup couplings and couplings with other channels. Besides, deviations may also arise from inaccuracies of the Wong’s formula. Then, the influence of such undesired effects should be minimized. This can be done introducing the renormalized experimental fusion function, denoted by $\mathrm { F } _ { \mathrm { e x p } } ( x )$ , defined as,

$$
F _ {\exp} (x) \rightarrow \overline {{\mathrm {F}}} _ {\exp} (x) = F _ {\exp} (x) \times \frac {\sigma^ {\mathrm {W}} (E)}{\sigma_ {\mathrm {F}} ^ {\mathrm {C C}} (E)}. \tag {155}
$$

Above, $\sigma ^ { \mathrm { w } } ( E )$ is the Wong’s cross section of Eq. (23), and $\sigma _ { \mathrm { F } } ^ { \mathrm { C C } } ( E )$ is the theoretical fusion cross section obtained through a CC calculation that includes all relevant channels, but the ones we are investigating (usually the breakup channel). Using the reduction procedure of Eq. (155), one estimates the influence of the channels left out of the CC calculations. In Refs. [42, 43], where this method was introduced, the channels left out were breakup and transfer. Of course, if all relevant channels are included in the CC calculations, the renormalized experimental fusion function is expected to coincide with the UFF. The fusion function method has been widely used in comparative studies of fusion cross sections in collisions of weakly-bound and tightly-bound projectiles [155, 232, 233, 234, 235, 236, 237, 238].

# Detailed discussion of breakup effects on fusion

Significant channel coupling effects have been observed in collisions of weakly bound nuclei. In this case, the relevant couplings are with the breakup channel. These couplings give rise to different fusion processes. In addition to complete fusion (CF), where the whole projectile is absorbed by the target, there is incomplete fusion (ICF). The latter takes place in two steps. First, the weakly bound projectile breaks up into fragments, say two, as it interacts with the target. Then, one fragment is absorbed by the target, while to other is not. Compared with the fusion cross section of a typical one-channel calculation, the experimental CF cross section is suppressed above the Coulomb barrier, and the TF (the sum of CF and ICF) cross section is enhanced at sub-barrier energies, due to the ICF of the lighter fragment. The determination of individual CF and ICF cross sections in collisions of weakly bound projectiles is a great challenge for both experimentalists and theorists. This subject has been reviewed in several works [1, 2, 3, 4, 5, 8, 239]. Most fusion experiments measure only the TF cross section. However, the available measurements of CF cross sections for weakly bound systems systematically find suppression at abovebarrier energies. Further, the strongest suppressions were observed in collisions of the most weakly bound projectiles on heavy targets.

Another kind of reduction method has been used to investigate the influence of breakup couplings in the fusion of weakly bound systems. It is well established that there is suppression of a CF in collisions of weakly bound

![](images/50573e9763f90a0c523ad1f3fec681824d5dc648f17cbfdd4ef2a57e64ae2b61.jpg)  
Fig. 24. (Color online) Experimental fusion function for col-The solid black curve is the benchmark UFF. The dotted red lin lisions of $_ 4$ Li with different heavy targets (figure taken fromthe UFF multiplied by 0.66 (for details see text). Ref. [248]).

projectiles on heavy targets at above-barrier energies com-experimental CF function for three systems, viz., 19F + 175 pared to predictions of barrier penetration models or fu-(in the present work), F + Tb [24], and F + Tm [3 sion cross sections of tightly bound projectiles of similaris shown separately in Fig. 9. The lowest break-up chan masses. Further, the suppression is not very sensitive tofor F is F → N + α with a threshold energy of 4. the collision energy, provided that it is higher enough thanMeV. From Fig. 9, as expected the CF function is found the Coulomb barrier  break-up effe $( E _ { \mathrm { c . m . } } \gtrsim V _ { \mathrm { B } } + 2 \hbar \omega )$ . For comparative    on. The experimental studies of this phenomenon, it is convenient to measure the suppression by the single number:which is displayed by the dotte

$$
F _ {C F} = \frac {\sigma_ {C F}}{\sigma_ {T F}}, \tag {156}
$$

where $\sigma _ { \scriptstyle \mathrm { C F } }$ and $\sigma _ { \mathrm { T F } }$ are respectively the complete and to-          ≈ tal fusion cross sections, above the Coulomb barrier. Thislog(1 F ) 0.33 exp( 0.29/E ) 0.087E . procedure was used in studies $6 , 7$ Li collisions with several medium-heavy and heavy targets, with the aim of corre-Figure 10 represents an exponential relation between lating CF suppression with the mass and charge of thesuppression factor in terms of the break-up threshold ene targets [109, 111, 240, 241, 242, 243, 244, 245, 246]. Theyof the projectile. The suppression factor obtained by fitting a19 concluded thatby Eq. $\operatorname { F } _ { \mathrm { C F } }$ has a weak target dependence. It isr the strongly bound projectile F are present between 0.60 and 0.67 for     19 $_ 6$ Li, and between 0.70 and 0.75 for 7Li. It is not surprising that the largest suppressions            weakly bound projectile 9Be and higher than for the stron (lowest FCF) were found for   bound projectile 10B $_ 6$ Li, which has a lower breakup       which is related to the fact that t threshold.

Jha et al. [247] carried out a study along the same line,projectile on different targets presented in Fig. 10 are found for collisions ofbe in go $^ { 9 } \mathrm { { B e } }$ on several targets. They investigatedgreement with the systematics developed by Wa the correlation of the fusion processes with the charge ofet al. [54] and show a well-established exponential relati the target. Instead ofbetween the CF $\mathrm { F } _ { \mathrm { C F } }$ , they used an ICF probability,pression factor and the break-up thresh $P _ { \mathrm { I C F } }$ , defined asof the p

$$
P _ {\mathrm {I C F}} = 1 - \mathrm {F} _ {\mathrm {C F}}. \tag {157}
$$

They concluded that the dependence of the CF/ICF processes on the target is more pronounced than that observed for the $6 , 7$ Li projectiles.

A similar reduction method has been used to study the influence of the breakup threshold of the projectile on

![](images/2b9428ab4df6382fc0f0fa5361495a0a0936f3735842ecb4f3ed6cbd467a77d4.jpg)  
e plotted as a function of the break-up threshold of the projectile. TheFig. 25. (Color online) Dependence of the suppression factor . dotted line represents the empirical Eq. (7) (for details see text).on the breakup threshold of the projectile. (Figure taken from s Ref. [249]).

uncertainty, which means that there is no effect of break-up onthe CF cross section [248, 249]. These studies considered the total fusion cross section.CF data of several weakly bound projectiles on different ,targets, with mass numbers in the range $8 9 \leq A _ { \mathrm { T } } \leq 2 0 9$ . l D. Observation of incomplete fusion below ℓcrit:They found that the experimental fusion functions were 1 Diffuseness in the ℓ distributionessentially independent or the target. This is illustrated o As demonstrated in Ref. [30], the study of the ℓ distributionin Fig. 24, which shows experimental fusion functions for e for the precollisions of $^ { 7 }$ ent system has been studied as well. The valuesLi on different heavy targets. One observes F of ℓcrit for the F + Lu system is deduced using thethat the data points follow the dotted line, corresponding , to $0 . 6 7 \times F _ { 0 } ( x )$ iven in Ref. [55] and found to be 65¯h. The. Then, the authors adopt the suppression d fusfactor

$$
F _ {\mathrm {B . U .}} = \frac {F (x)}{F _ {0} (x)} \tag {158}
$$

to express the influence of the breakup channel on CF.

On the other hand, the suppression factor has an appreciable dependence on the breakup threshold of the proe jectile. This can be seen in Fig. 25, which shows the logayrithm of $1 - F _ { \mathrm { B . U . } }$ , as a function of the breakup threshold dof the projectile, $E _ { \mathrm { B . U . } }$ .

# Reduction of the reaction cross section data

eThe reduction of total reaction (TR) data is much more complicated because they are sums of contributions from fusion and direct reactions, which have very different nantures. Fusion is absorption by a strong imaginary potential dacting within the inner region of the Coulomb barrier. In e FIG. 11. The experimentally deduced total fusion functions forthis way, it is equivalent to a barrier penetration problem. s strongly bound projectiles on different target nuclei are comparedFor this reason, the cross section scales with the barrier d with the UFF. The solid black curve is the UFF (for details see text).parameters, as predicted by the Wong formula. This explains the success of the fusion function method to reduce 14605-8fusion data. On the other hand, direct reactions are processes taking place in peripheral collisions. In 1-channel calculations, they can be simulated by a long-range imaginary potential, reaching beyond the barrier radius. These processes do not depend on the barrier parameters as pre-

![](images/ea43f7e72535635de9ab6f76335fa911968422f88d256f5491bcdc0de7849f0f.jpg)  
Fig. 26. (Color online) Reduced TR cross sections for collisions of several projectiles on $^ { 2 7 }$ Al, obtained by the procedure of Eq. (159) (figure taken from Ref. [250]).

dicted by the Wong formula.

Owing to the different characteristics of fusion and direct reactions, the available reduction methods have poor performances when applied to total reaction data. A detailed study of this problem was carried out in Refs. [44, 230]. Different reduction methods were applied to total reaction cross sections obtained by 1-channel calculations using the Aky¨uz-Winther interaction [18, 19], $V _ { \mathrm { N } } ( R )$ , and the long-range imaginary potential, $W ( R ) = 0 . 7 8 V _ { \mathrm { N } } ( R )$ . This procedure was applied to a large number of systems in different mass regions. Since the calculations did not take into account nuclear structure properties of the collision partners, differences among the reduced cross sections should be attributed to the gross properties of the systems, like charges and masses. Such differences should not be found in a successful reduction method. This study has shown that the reduced cross sections kept a strong system dependence, independently of the method used. Nevertheless, the situation was much better when the comparison involved systems of similar masses.

Recently, Morcelle et al. [250] proposed a new procedure to reduce TR data, which emphasises the influence of the breakup channel. This method was applied to collisions of several weakly and tightly bound projectiles on 27Al. The method consists of the transformations, $^ { 2 7 }$

$$
E \rightarrow E _ {\mathrm {r e d}} = \frac {E}{V _ {\mathrm {B}}} ; \quad \sigma_ {\mathrm {R}} ^ {\exp} \rightarrow \sigma_ {\mathrm {r e d}} = \frac {\sigma_ {\mathrm {R}} ^ {\exp}}{\sigma_ {\mathrm {F}} ^ {\mathrm {C C}}}, \tag {159}
$$

where $\sigma _ { \mathrm { F } } ^ { \mathrm { C C } }$ is the fusion cross section obtained by a CC calculation including couplings with the low-lying collective states of the 27Al target, and $\sigma _ { \mathrm { { R } } } ^ { \mathrm { { e x p } } }$ is the total reaction cross section obtained from fits to elastic scattering data. They considered data at above barrier energies for the following systems: $\mathrm { ^ 8 B + ^ { 2 7 } A l }$ [250], ${ } ^ { 6 } \mathrm { H e } + { } ^ { 2 7 } \mathrm { A l }$ [251], $^ { 6 } \mathrm { L i } +$ 27Al [252], $^ 7 { \mathrm { L i } } + ^ { 2 7 } { \mathrm { A l } }$ [253], $^ { 9 } \mathrm { B e } \mathrm { ~ + ~ } ^ { 2 7 } \mathrm { A l }$ [254, 255], 7Be $+ ~ ^ { 2 7 } \mathrm { A l }$ [256], and 16O + 27Al [257]. Sub-barrier energies

![](images/e7ef81d68164bf7878f991f5a910aab4447217b3b5b5877d8725ea49df588b75.jpg)  
Fig. 27. (Color online) Comparison of the reduced total reaction cross sections for several projectiles on medium mass range targets., obtained through coupled-channel calculations. The experimental data were taken from Ref. [71] for $^ { 6 } \mathrm { H e } \ +$ $^ { 5 8 }$ Ni, Refs. [152, 258, 259] for $^ { 6 } \mathrm { { L i } + ^ { 5 8 } \mathrm { { N i } } }$ , Ref. [259] for $^ 7 \mathrm { L i } +$ $^ { 5 8 }$ Ni, Refs. [152, 260] for $^ 7 \mathrm { B e } + ^ { 5 8 } \mathrm { N i }$ , Ref. [261] for ${ } ^ { 9 } \mathrm { B e } + { } ^ { 5 1 } \mathrm { V }$ , Ref. [262] for ${ } ^ { 9 } \mathrm { B e } + { } ^ { 6 4 } \mathrm { Z n }$ , Ref. [152] for $\mathrm { ^ 8 B + ^ { 5 8 } N i }$ , Ref. [160] for $\mathrm { ^ { 1 1 } B + ^ { 5 8 } N i }$ , and Ref. [263] for the $^ { 1 6 } \mathrm { O } + ^ { 6 4 } \mathrm { Z n }$ system (Figure taken from Ref. [264]).

were left out because, in this energy region, the angular distribution corresponds, basically, to Rutherford scattering. In this way, the determination of the nuclear S-matrix tends to be inaccurate, leading to large error bars in the TR cross section. Breakup couplings, which hinder complete fusion, has the opposite effect on the total reaction cross section. It gives an additional contribution, which enhances TR. Therefore, $\sigma _ { \mathrm { r e d } }$ must be larger than one.

The reduced cross sections obtained in Ref. [250] are shown in Fig. 26. First, one notices that the reduced cross sections systematically increase as $E _ { \mathrm { r e d } }$ decreases. This is a trivial consequence of the fact that the contribution from direct processes is dominant at low energies. Second, one observes that comparing data of different systems in the same energy range, the largest reduced cross sections are for the projectiles with the lowest breakup thresholds.

Deshmukh, Lubian, and Mukherjee [264, 265] used the same reduction procedure to investigate the TR cross sections in collisions of stable and radioactive weakly bound projectiles with intermediate mass targets, also considering data below the Coulomb barrier. Their results are shown in Fig. 27. As could be expected, the reduced cross section below $V _ { \mathrm { B } }$ grows abruptly, reaching very high values. However, the correlation between the reduced cross section and the breakup threshold of the projectile emerges clearly, in the whole energy interval. The data points for the stable weakly bound nuclei ( $_ 6$ Li, 7Li, and $^ { 9 } \mathrm { { B e } }$ ) are clearly above those for the tightly bound $^ { 1 6 } \mathrm { O }$ , and the ones for the radioactive projectiles (6He, $^ { 8 } \mathrm { B }$ and $^ { 1 1 } \mathrm { { B e } }$ ), which have breakup thresholds below 1 MeV, are still higher.

# 6 Summary

We have presented an account of recent theoretical and experimental developments in the study of nuclear reactions at near-barrier energies, with emphasis on weakly bound systems and in evaluations of the total reaction cross sections. Nuclear reactions with weakly bound nuclei have large breakup cross sections, and other reaction channels are strongly influenced by the breakup process.

We began reviewing the main features of the quantum mechanical treatment of potential scattering, and its semiclassical approximations. Then, we have discussed the coupled channel approach, with emphasis in the discretization of the continuum, which is essential to describe collisions of weakly bound nuclei. The influence of core and target excitations on the elastic and reaction cross sections were then reviewed, and a few applications were considered.

We addressed also the surrogate method to describe inclusive cross sections in collisions of weakly bound nuclei. Different formulations of the method were discussed and a few examples were given.

A detailed discussion of the available methods to measure the total reaction cross section has been presented, with emphasis on the most recent experimental techniques to measure cross sections in experiments with low intensity secondary beams of unstable nuclei. We then discussed reduction method to allow meaningful comparisons of data for different systems. We pointed out that the fusion function reduction method works very well for fusion data, even for very different systems, but satisfactory reductions of total reaction data can only be achieved for very similar systems.

# References

1. L. F. Canto, P. R. S. Gomes, R. Donangelo, and M. S. Hussein, Phys. Rep. 424, 1 (2006).   
2. N. Keeley, R. Raabe, N. Alamanos, and J. L. Sida, Prog. Part. Nucl. Phys. 59, 579 (2007).   
3. N. Keeley, N. Alamanos, K. W. Kemper, and K. Rusek, Prog. Part. Nucl. Phys. 63, 396 (2009).   
4. L. F. Canto, P. R. S. Gomes, R. Donangelo, J. Lubian, and M. S. Hussein, Phys. Rep. 596, 1 (2015).   
5. J. J. Kolata, V. Guimar˜aes, and E. F. Aguilera, Eur. Phys. J. A 52, 123 (2016).   
6. G. Montagnoli and A. M. Stefanini, Eur. Phys. J. A 53, 169 (2017).   
7. A. Bonaccorso, Prog. Part. Nucl. Phys. 101, 1 (2018).   
8. V. Jha, V. V. Parkar, and S. Kailas, Phys. Rep. 845, 1 (2020).   
9. Y. Sakuragi, M. Yahiro, and M. Kamimura, Prog. Theoret. Phys. Suppl. 89, 136 (1986).   
10. N. Austern, Y. Iseri, M. Kamimura, M. Kawai, G. Rawitscher, and M. Yashiro, Phys. Rep. 154, 125 (1987).

11. K. Hagino, A. Vitturi, C. H. Dasso, and S. M. Lenzi, Phys. Rev. C 61, 037602 (2000).   
12. A. Diaz-Torres and I. J. Thompson, Phys. Rev. C 65, 024606 (2002).   
13. A. Diaz-Torres, I. J. Thompson, and C. Beck, Phys. Rev. C 68, 044607 (2003).   
14. M. S. Hussein, R. A. Rego, and C. A. Bertulani, Phys. Rep. 201, 279 (1991).   
15. L. C. Chamon, D. Pereira, M. S. Hussein, M. A. Candido Ribeiro, and D. Galetti, Phys. Rev. Lett. 79, 5218 (1997).   
16. L. C. Chamon, B. V. Carlson, L. R. Gasques, D. Pereira, C. De Conti, M. A. G. Alvarez, M. S. Hussein, M. A. Cˆandido Ribeiro, E. S. Rossi Jr., and C. P. Silva, Phys. Rev. C 66, 014610 (2002).   
17. L. R. Gasques, L. C. Chamon, P. R. S. Gomes, and J. Lubian, Nucl. Phys. A 764, 135 (2006).   
18. R. A. Broglia and A. Winther, Heavy Ion Reactions (Westview Press, 2004).   
19. O. Aky¨uz and A. Winther, in Nuclear Structure of Heavy Ion Reaction, edited by R. A. Broglia, C. H. Dasso, and R. A. Ricci (North Holland, 1981), proc. E. Fermi Summer School of Physics.   
20. L. F. Canto and M. S. Hussein, Scattering Theory of Molecules, Atoms and Nuclei (World Scientific Publishing Co. Pte. Ltd., 2013).   
21. H. Feshbach, D. C. Peasly, and V. F. Weisskopft, Phys. Rev. 71, 145 (1947).   
22. G. H. Rawitscher, Phys. Rev. 135, B605 (1964).   
23. G. H. Rawitscher, Nucl. Phys. 85, 337 (1966).   
24. E. C. Kemble, Phys. Rev. 48, 549 (1935).   
25. A. J. Toubiana, L. F. Canto, and M. S. Hussein, Eur. Phys. J. A 53, 34 (2017).   
26. A. J. Toubiana, L. F. Canto, and M. S. Hussein, Braz. J. Phys. 47, 321 (2017).   
27. C. Y. Wong, Phys. Rev. Lett. 31, 766 (1973).   
28. N. Rowley and K. Hagino, Phys. Rev. C 91, 044617 (2015).   
29. A. J. Toubiana, L. F. Canto, R. Donangelo, and M. S. Hussein, Phys. Rev. C 96, 064615 (2017).   
30. W. E. Frahn, Nucl. Phys. A 75, 577 (1966).   
31. W. E. Frahn, Diffraction processes in Nuclear Physics (Oxford University Press, Oxford U.K., 1985).   
32. J. T. Holdeman and R. M. Thaler, Phys. Rev. Lett. 14, 81 (1965).   
33. J. T. Holdeman and R. M. Thaler, Phys. Rev. 139, B 1186 (1965).   
34. C. Marty, Z. Phys. 309, 261 (1983).   
35. M. Ueda, M. P. Pato, M. S. Hussein, and N. Takigawa, Nucl. Phys. A 648, 229 (1999).   
36. J. Barrette and N. Alamanos, Phys. Lett. B 153, 208 (1985).   
37. J. Barrette and N. Alamanos, Nucl. Phys. A 441, 733 (1985).   
38. A. N. Ostrowski, W. Tiereth, and H. Voit, Phys. Rev. C 44, 2082 (1991).   
39. V. Shkolnik, D. Dehnhard, S. Kubono, M. Franey, and S. Tripp, Phys. Lett. B 74, 195 (1978).

40. A. N. Ostrowski, W. Thiereth, and H. Voit, Phys. Rev. C 44, 2082 (1991).   
41. M. Ueda, M. P. Pato, M. S. Hussein, and N. Takigawa, Phys. Rev. Lett. 81, 1809 (1998).   
42. L. F. Canto, P. R. S. Gomes, J. Lubian, L. C. Chamon, and E. Crema, J. Phys. G: Nucl. Part. Phys. 36, 015109 (2009).   
43. L. F. Canto, P. R. S. Gomes, J. Lubian, L. C. Chamon, and E. Crema, Nucl. Phys. A 821, 51 (2009).   
44. L. F. Canto, D. R. Mendes Junior, P. R. S. Gomes, and J. Lubian, Phys. Rev. C 92, 014626 (2015).   
45. G. D. Kolinger, L. F. Canto, R. Donangelo, and S. R. Souza, Phys. Rev. C 98, 044604 (2018).   
46. T. Druet, D. Baye, P. Descouvemont, and J.-M. Sparenberg, Nucl. Phys. A 845, 88 (2010).   
47. I. J. Thompson and F. M. Nunes, Nuclear Reactions for Astrophysics: Principles, Calculation and Applications (Cambridge University Press, 2009), 1st ed.   
48. T. Matsumoto, T. Kamizato, K. Ogata, Y. Iseri, E. Hiyama, M. Kamimura, and M. Yahiro, Phys. Rev. C 68, 064607 (2003).   
49. C. A. Bertulani and L. F. Canto, Nucl. Phys. A539, 163 (1992).   
50. H. D. Marta, L. F. Canto, and R. Donangelo, Phys. Rev. C78, 034612 (2008).   
51. H. D. Marta, L. F. Canto, and R. Donangelo, Phys. Rev. C 89, 034625 (2014).   
52. E. Hiyama, Y. Kino, and M. Kamimura, Prog. Part. Nucl. Phys. 51, 223 (2003).   
53. M. Hesse, J.-M. Sparenberg, F. Van Raemdonck, and D. Baye, Nucl. Phys. A 640, 37 (1998).   
54. A. M. Moro and J. G´omez-Camacho, EPJ Web of Conferences 117, 06002 (2016).   
55. N. C. Summers, F. M. Nunes, and I. J. Thompson, Phys. Rev. C 74, 014606 (2006).   
56. N. C. Summers and F. M. Nunes, Phys. Rev. C 76, 014611 (2007).   
57. A. M. Moro and R. Crespo, Phys. Rev. C 85, 054613 (2012).   
58. R. de Diego, J. M. Arias, J. A. Lay, and A. M. Moro, Phys. Rev. C 89, 064609 (2014).   
59. J. Chen, J. L. Lou, Y. L. Ye, Z. H. Li, Y. C. Ge, Q. T. Li, J. Li, W. Jiang, Y. L. Sun, H. L. Zang, et al., Phys. Rev. C 93, 034623 (2016).   
60. R. de Diego, R. Crespo, and A. M. Moro, Phys. Rev. C 95, 044611 (2017).   
61. V. Pesudo, M. J. G. Borge, A. M. Moro, J. A. Lay, E. N´acher, J. G´omez-Camacho, O. Tengblad, L. Acosta, M. Alcorta, M. A. G. Alvarez, et al., Phys. Rev. Lett. 118, 152502 (2017).   
62. J. A. Lay, R. de Diego, R. Crespo, A. M. Moro, J. M. Arias, and R. C. Johnson, Phys. Rev. C 94, 021602 (2016).   
63. Y. Satou, T. Nakamura, N. Fukuda, and et al., Phys. Lett. B 660, 320 (2008).   
64. J. Lubian, T. Correa, E. F. Aguilera, L. F. Canto, A. Gomez-Camacho, E. M. Quiroz, and P. R. S. Gomes, Phys. Rev. C 79, 064605 (2009).

65. E. F. Aguilera, E. Martinez-Quiroz, D. Lizcano, A. G´omez-Camacho, J. J. Kolata, L. O. Lamm, V. Guimar˜aes, R. Lichtenth¨aler, O. Camargo, F. D. Becchetti, et al., Phys. Rev. C 79, 021601 (2009).   
66. A. E. Woodward, J. M. Figueira, D. R. Otomar, J. O. Fern´andez Niello, J. Lubian, A. Arazi, O. A. Capurro, P. Carnelli, L. Fimiani, G. V. Mart´ı, et al., Nucl. Phys. A 873, 17 (2012).   
67. M. G´omez-Ramos and A. M. Moro, Phys. Rev. C 95, 034609 (2017).   
68. M. Rodr´ıguez-Gallardo, J. M. Arias, J. G´omez-Camacho, R. C. Johnson, A. M. Moro, I. J. Thompson, and J. A. Tostevin, Phys. Rev. C 77, 064609 (2008).   
69. T. Matsumoto, E. Hiyama, K. Ogata, Y. Iseri, M. Kamimura, S. Chiba, and M. Yahiro, Phys. Rev. C 70, 061601 (2004).   
70. M. Cubero, J. P. Fern´andez-Garc´ıa, M. Rodr´ıguez-Gallardo, L. Acosta, M. Alcorta, M. A. G. Alvarez, M. J. G. Borge, L. Buchmann, C. A. Diget, H. A. Falou, et al., Phys. Rev. Lett. 109, 262701 (2012).   
71. V. Morcelle, K. C. C. Pires, M. Rodr´ıguez-Gallardo, R. Lichtenth¨aler, A. L´epine-Szily, V. Guimar˜aes, P. N. de Faria, D. R. Mendes Junior, A. M. Moro, L. R. Gasques, et al., Phys. Lett. B 732, 228 (2014).   
72. P. Descouvemont, T. Druet, L. F. Canto, and M. S. Hussein, Phys. Rev. C 91, 024606 (2015).   
73. J. P. Fern´andez-Garc´ıa, A. Di Pietro, P. Figuera, J. G´omez-Camacho, M. Lattuada, J. Lei, A. M. Moro, M. Rodr´ıguez-Gallardo, and V. Scuderi, Phys. Rev. C 99, 054605 (2019).   
74. M. Ichimura, N. Austern, and C. M. Vincent, Phys. Rev. C 32, 431 (1985).   
75. A. M. S´anchez-Ben´ıtez, D. Escrig, M. A. G. Alvarez, ´ M. V. Andr´es, C. Angulo, M. J. G. Borge, J. Cabrera, S. Cherubini, P. Demarelt, J. M. Espino, et al., Nucl. Phys. A 803, 30 (2008).   
76. L. Acosta, A. M. S´anchez-Ben´ıtez, M. E. G´omez, I. Martel, F. P´erez-Bernal, F. Pizarro, J. Rodr´ıguez-Quintero, K. Rusek, M. A. G. Alvarez, M. V. Andr´es, et al., Phys. Rev. C 84, 044604 (2011).   
77. A. M. Moro, K. Rusek, J. M. Arias, J. G´omez-Camacho, and M. Rodr´ıguez-Gallardo, Phys. Rev. C 75, 064607 (2007).   
78. M. Rodr´ıguez-Gallardo, J. M. Arias, J. G´omez-Camacho, A. M. Moro, I. J. Thompson, and J. A. Tostevin, Phys. Rev. C 80, 051601 (2009).   
79. P. Descouvemont and N. Itagaki, Phys. Rev. C 97, 014612 (2018).   
80. P. Descouvemont, Phys. Lett. B 772, 1 (2017).   
81. Desc, Phys. Rev. C 97, 064607ccs (2018).   
82. M. S. Hussein, Eur. Phys. J. A 53, 110 (2017).   
83. J. E. Escher, J. T. Burke, F. S. Dietrich, N. D. Scielzo, I. J. Thompson, and W. Younes, Rev. Mod. Phys. 84, 353 (2012).   
84. G. Potel, G. Perdikakis, B. V. Carlson, M. C. Atkinson, W. H. Dickhoff, J. E. Escher, M. S. Hussein, J. Lei, W. Li, A. O. Macchiavelli, et al., Eur. Phys. J. A 53, 178 (2017).

85. M. Ichimura, Phys. Rev. C 41, 834 (1990).   
86. L. Rodberg and R. Thaler, Introduction to the Quantum Theory of Scattering (Academic Press, N.Y., 1967).   
87. H. Feshbach, Ann. Phys. (NY) 5, 357 (1958).   
88. H. Feshbach, Ann. Phys. (NY) 19, 287 (1962), ibid. 5 (1958) 357.   
89. F. S. Levin and H. Feshbach, Reaction Dynamics (Gordon and Breach, Science Publisher, Inc., New York & London & Paris, 1973).   
90. H. Feshbach, Theoretical Nuclear Physics: Nuclear Reactions (Wiley Publishing, N.Y., 1992).   
91. T. Udagawa and T. Tamura, Phys. Rev. C 24, 1348 (1981).   
92. A. Kasano and M. Ichimura, Phys. Lett. B 115, 81 (1982).   
93. N. Austern and C. M. Vincent, Phys. Rev. C 23, 1847 (1981).   
94. M. S. Hussein and K. W. McVoy, Nucl. Phys. A 445, 124 (1985).   
95. B. V. Carlson, R. Capote, and M. Sin, EPJ Web of Conferences 146, 12001 (2017).   
96. J. Lei and A. M. Moro, Phys. Rev. C 92, 044616 (2015).   
97. X. H. Li, T. Udagawa, and T. Tamura, Phys. Rev. C 30, 1895 (1984).   
98. J. Lei and A. M. Moro, Phys. Rev. C 92, 061602(R) (2015).   
99. G. Potel, F. M. Nunes, and I. J. Thompson, Phys. Rev. C 92, 034611 (2015).   
100. M. S. Hussein, T. Frederico, and R. C. Mastroleo, Nucl. Phys. A 511, 269 (1990).   
101. R. C. Mastroleo, T. Udagawa, and T. Tamura, J. Phys. G: Nucl. Part. Phys. 15, 473 (1989).   
102. J. Kleinfeller, J. Bisplinghoff, J. Ernst, T. Mayer-Kuckuk, G. Baur, B. Hoffmann, R. Shyam, F. R¨osel, and D. Trautmann, Nucl. Phys. A 370, 205 (1981).   
103. S. Santra, S. Kailas, K. Ramachandran, V. V. Parkar, V. Jha, B. J. Roy, and P. Shukla, Phys. Rev. C 83, 034616 (2011).   
104. W. Hauser and H. Feshbach, Phys. Rev. 87, 336 (1952).   
105. J. E. Escher, J. T. Burke, R. O. Hughes, N. D. Scielzo, R. J. Casperson, S. Ota, H. I. Park, A. Saastamoinen, and T. J. Ross, Phys. Rev. Lett. 121, 052501 (2018).   
106. National nuclear data center-nndc, Brookhaven National Laboratory (2018), URL http://www.nndc. bnl.gov/.   
107. A. J. Koning, Nuclear Data Sheets 123, 207 (2015).   
108. J. Lei and A. M. Moro, Phys. Rev. Lett. 122, 042503 (2019).   
109. M. Dasgupta, D. J. Hinde, K. Hagino, S. B. Moraes, P. R. S. Gomes, R. M. Anjos, R. D. Butt, A. C. Berriman, N. Carlin, C. R. Morton, et al., Phys. Rev. C 66, 041602(R) (2002).   
110. M. Dasgupta, D. J. Hinde, R. D. Butt, R. M. Anjos, A. C. Berriman, N. Carlin, P. R. S. Gomes, C. R. Morton, J. O. Newton, A. Szanto de Toledo, et al.,

Phys. Rev. Lett. 82, 1395 (1999).   
111. M. Dasgupta, P. R. S. Gomes, D. J. Hinde, S. B. Moraes, R. M. Anjos, A. C. Berriman, R. D. Butt, N. Carlin, J. Lubian, C. R. Morton, et al., Phys. Rev. C 70, 024606 (2004).   
112. (2020), URL www-nds.iaea.org/exfor/.   
113. A. Karpov, A. Denikin, M. Naumenko, A. Alekseev, V. Rachkov, V. Samarin, V. Saiko, and V. Zagrebaev, Nucl. Instrum. Methods Phys. Res. A 859, 112 (2017).   
114. V. I. Zagrebaev, A. S. Denikin, A. V. Karpov, A. P. Alekseev, M. A. Naumenko, V. A. Rachkov, V. V. Samarin, and V. V. Saiko, NRV web knowledge base on low-energy nuclear physics, http://nrv.jinr. ru/ (1999).   
115. V. Scarduelli, L. R. Gasques, L. C. Chamon, and A. L´epine-Szily, The European Physical Journal A 56, 24 (2020).   
116. URL www.nscl.msu.edu.   
117. Z. Sun, W.-L. Zhan, Z.-Y. Guo, G. Xiao, and J.-X. Li, Nucl. Instrum. Methods Phys. Res. A 503, 496 (2003).   
118. URL fair-center.eu/.   
119. Y. Yano, Nucl. Instrum. Methods Phys. Res. B 261, 1009 (2007).   
120. R. Anne, D. Bazin, A. C. Mueller, J. C. Jacmart, and M. Langevin, Nucl. Instrum. Methods Phys. Res. A 257, 215 (1987).   
121. C. Parascandolo, A. Boiano, C. Boiano, M. La Commara, G. La Rana, M. Mazzocco, D. Pierroutsakou, C. Signorini, F. Soramel, and E. Strano, EPJ Web Conf. 165, 01041 (2017).   
122. R. E. Tribble, R. H. Burch, and C. A. Gagliardi, Nucl. Instrum. Methods Phys. Res. A 285, 441 (1989).   
123. G. Ter-Akopian, Y. Oganessian, M. Itkis, G. Gulbekian, D. Bogdanov, A. Fomichev, M. Golovkov, A. Rodin, S. Stepantsov, and R. Wolski, Nucl. Phys. A 734, 295 (2004).   
124. URL www.ganil-spiral2.eu/.   
125. G. Bisoffi, G. Prete, A. Andrighetto, V. Andreev, L. Bellan, M. Bellato, D. Bortolato, M. Calderolla, S. Canella, M. Comunian, et al., Nucl. Instrum. Methods Phys. Res. B 376, 402 (2016).   
126. D. Voulot, F. Wenander, E. Piselli, R. Scrivens, M. Lindroos, H. B. Jeppesen, L. M. Fraile, S. Sturm, and P. Delahay, Nucl. Instrum. Methods Phys. Res. B 266, 4103 (2008).   
127. URL www.triumf.ca/research-program/.   
128. D. Becchetti, M. Lee, T. O’Donnell, D. Roberts, J. Kolata, L. Lamm, G. Rogachev, V. Guimar˜aes, P. DeYoung, and S. Vincent, Nucl. Instrum. Methods Phys. Res. A 505, 377 (2003).   
129. R. Lichtenth¨aler, A. L´epine-Szily, V. Guimar˜aes, C. Perego, V. Placco, O. Camargo jr., R. Denke, P. N. de Faria, E. A. Benjamim, N. Added, et al., Eur. Phys. J. A 25, 733 (2005).   
130. B. Harss, R. C. Pardo, K. E. Rehm, F. Borasi, J. P. Greene, R. V. F. Janssens, C. L. Jiang, J. Nolen,

M. Paul, J. P. Schiffer, et al., Rev. Sci. Inst. 71, 380 (1999).   
131. Y. Yanagisawa, S. Kubono, T. Teranishi, K. Ue, S. Michimasa, M. Notani, J. He, Y. Ohshiro, S. Shimoura, S. Watanabe, et al., Nucl. Instrum. Methods Phys. Res. A 539, 74 (2005).   
132. R. Rafiei, D. Hinde, M. Dasgupta, D. Weisser, A. Muirhead, A. Harding, A. Cooper, H. Wallace, N. Lobanov, A. Wakhle, et al., Nucl. Instrum. Methods Phys. Res. A 631, 12 (2011).   
133. Y. Blumenfeld, T. Nilsson, and P. Van Duppen, Phys. Scr. T152, 014023 (2013).   
134. R. Raabe, Eur. Phys. J. Plus 131, 362 (2016).   
135. A. Chakrabarti, Nucl. Instrum. Methods Phys. Res. B 261, 1018 (2007).   
136. T. J. Zhang, B. Q. Cui, Z. G. Li, Y. L. Lu, C. H. Peng, and F. Yang, in Proc. 4th Int. Particle Accelerator Conf. (IPAC’13) (Shanghai, China, 2013), p. 345.   
137. J. Yang, J. Xia, G. Xiao, H. Xu, H. Zhao, X. Zhou, X. Ma, Y. He, L. Ma, D. Gao, et al., Nucl. Instrum. Methods Phys. Res. B 317, 263 (2013).   
138. C. C. Sahm, T. Murakami, J. G. Cramer, A. J. Lazzarini, D. D. Leach, D. R. Tieger, R. A. Loveman, W. G. Lynch, M. B. Tsang, and J. Van der Plicht, Phys. Rev. C 34, 2165 (1986).   
139. I. Tanihata, H. Hamagaki, O. Hashimoto, Y. Shida, N. Yoshikawa, K. Sugimoto, O. Yamakawa, T. Kobayashi, and N. Takahashi, Phys. Rev. Lett. 55, 2676 (1985).   
140. I. Tanihata, H. Savajols, and R. Kanung, Prog. Part. Nucl. Phys. 68, 215 (2013).   
141. L. Acosta, A. M. S´anchez-Ben´ıtez, M. E. G´omez, I. Martel, F. P´erez-Bernal, F. Pizarro, J. Rodr´ıguez-Quintero, K. Rusek, M. A. G. Alvarez, M. V. Andr´es, et al., Phys. Rev. C 84, 044604 (2011).   
142. G. Marqu´ınez-Dur´an, L. Acosta, R. Berjillos, J. Due˜nas, J. Labrador, K. Rusek, A. S´anchez-Ben´ıtez, and I. Martel, Nucl. Instrum. Methods Phys. Res. A 755, 69 (2014).   
143. G. Marqu´ınez-Dur´an, I. Martel, A. M. S´anchez-Ben´ıtez, L. Acosta, R. Berjillos, J. Due˜nas, K. Rusek, N. Keeley, M. A. G. Alvarez, M. J. G. Borge, et al., ´ Phys. Rev. C 94, 064618 (2016).   
144. N. Keeley, K. W. Kemper, I. Martel, K. Rusek, and A. M. S´anchez-Ben´ıtez, Phys. Rev. C 99, 024603 (2019).   
145. G. Marqu´ınez-Dur´an, N. Keeley, K. W. Kemper, R. S. Mackintosh, I. Martel, K. Rusek, and A. M. S´anchez-Ben´ıtez, Phys. Rev. C 95, 024602 (2017).   
146. W. Y. So, K. S. Kim, K. S. Choi, and C. Myung-Ki, Phys. Rev. C 90, 054615 (2014).   
147. V. Guimar˜aes, J. Lubian, J. J. Kolata, E. F. Aguilera, M. Assun¸c˜ao, and V. Morcelle, Eur. Phys. J. A 54, 223 (2018).   
148. A. Di Pietro, V. Scuderi, A. M. Moro, L. Acosta, F. Amorini, M. J. G. Borge, P. Figuera, M. Fisichella, L. M. Fraile, J. Gomez-Camacho, et al., Phys. Rev. C 85, 054607 (2012).

149. L. Acosta, M. A. G. Alvarez, M. V. Andr´esA, ´ M. J. G. Borge, M. Cort´es, J. M. Espino, D. Galaviz, J. G´omez-Camacho, A. Maira, I. Martel, et al., Eur. Phys. J. A 42, 461 (2009).   
150. M. Mazzocco, C. Signorini, M. Romoli, A. De Franesco, M. Di Pietro, E. Vardaci, K. Yoshida, R. Yoshida, A. Bonetti, A. De Rosa, T. Glodariu, et al., Eur. Phys. J. A 28, 295 (2006).   
151. M. Mazzocco, C. Signorini, M. Romoli, R. Bonetti, A. De Francesco, A. De Rosa, M. Di Pietro, L. Fortunato, T. Glodariu, A. Guglielmetti, et al., The European Physical Journal Special Topics 150, 37 (2007).   
152. E. F. Aguilera, E. Martinez-Quiroz, D. Lizcano, A. G´omez-Camacho, J. J. Kolata, L. O. Lamm, V. Guimar˜aes, R. Lichtenth¨aler, O. Camargo, F. D. Becchetti, et al., Phys. Rev. C 79, 021601 (2009).   
153. L. Lubian, T. Correa, P. R. S. Gomes, L. F. Canto, and M. Hussein, Nucl. Phys. A 834, 802c (2010).   
154. N. Keeley, J. Phys. Conf. Series 381, 012087 (2012).   
155. M. Mazzocco, N. Keeley, A. Boiano, C. Boiano, M. La Commara, C. Manea, C. Parascandolo, D. Pierroutsakou, C. Signorini, E. Strano, et al., Phys. Rev. C 100, 024602 (2019).   
156. Y. Y. Yang, X. Liu, D. Y. Pang, D. Patel, R. F. Chen, J. S. Wang, P. Ma, J. B. Ma, S. L. Jin, Z. Bai, et al., Phys. Rev. C 98, 044608 (2018).   
157. D. Pierroutsakou, A. Boiano, C. Boiano, P. D. Meo], M. L. Commara], C. Manea, M. Mazzocco, M. Nicoletto, C. Parascandolo, C. Signorini, et al., Nucl. Instrum. Methods Phys. Res. A 834, 46 (2016).   
158. E. F. Aguilera, E. Martinez-Quiroz, D. Lizcano, A. G´omez-Camacho, J. J. Kolata, L. O. Lamm, V. Guimar˜aes, R. Lichtenth¨aler, O. Camargo, F. D. Becchetti, et al., Phys. Rev. C 79, 021601(R) (2009).   
159. V. Scarduelli, E. Crema, V. Guimar˜aes, D. Abriola, A. Arazi, E. de Barbar´a, O. A. Capurro, M. A. Cardona, J. Gallardo, D. Hojman, et al., Phys. Rev. C 96, 054610 (2017).   
160. N. N. Deshmukh, V. Guimar˜aes, E. Crema, D. Abriola, A. Arazi, E. de Barbar´a, O. A. Capurro, M. A. Cardona, J. Gallardo, D. Hojman, et al., Phys. Rev. C 92, 054615 (2015).   
161. E. O. N. Zevallos, V. Guimar˜aes, E. N. Cardozo, J. Lubian, R. Linares, R. L. Filho, K. C. C. Pires, O. C. B. Santos, S. Appannababu, E. Crema, et al., Phys. Rev. C 99, 064613 (2019).   
162. V. Guimar˜aes, E. O. N. Zevallos, E. N. Cardozo, J. Lubian, O. C. B. Santos, R. Linares, M. Assun¸c˜ao, J. Alcantara-Nunez, A. L. de Lara, R. Lichtenthaler Filho, et al., in Recent Progress in Few-Body Physics, edited by N. A. Orr, M. Ploszajczak, F. M. Marqu´es, and J. Carbonell (Springer International Publishing, Cham, 2020), p. 195.   
163. S. Santra, P. Singh, S. Kailas, A. Chatterjee, A. Shrivastava, and K. Mahata, Phys. Rev. C 64, 024602 (2001).   
164. S. Landowne and H. H. Wolter, Nucl. Phys. A 351, 171 (1981).

165. Y. Y. Yang, J. S. Wang, Q. Wang, D. Y. Pang, J. B. Ma, M. R. Huang, P. Ma, S. L. Jin, J. L. Han, Z. Bai, et al., Phys. Rev. C 90, 014606 (2014).   
166. V. Guimar˜aes, E. N. Cardozo, V. B. Scarduelli, J. Lubian, J. J. Kolata, P. D. O’Malley, D. W. Bardayan, E. F. Aguilera, E. Martinez-Quiroz, D. Lizcano, et al., Phys. Rev. C 100, 034603 (2019).   
167. N. Curtis, N. Achouri, N. Ashwood, H. Bohlen, W. Catford, N. Clarke, M. Freer, P. Haigh, B. Laurent, N. Orr, et al., J. Phys. Conf. Series 111, 012022 (2008).   
168. R. J. Charity, T. D. Wiser, K. Mercurio, R. Shane, L. G. Sobotka, A. H. Wuosmaa, A. Banu, L. Trache, and R. E. Tribble, Phys. Rev. C 80, 024306 (2009).   
169. M. Alcorta, K. E. Rehm, B. B. Back, S. Bedoor, P. F. Bertone, C. M. Deibel, B. DiGiovine, H. Esbensen, J. P. Greene, C. R. Hoffman, et al., Phys. Rev. Lett. 106, 172701 (2011).   
170. J. Ovejas, A. Knyazev, I. Martel, O. Tengblad, M. J. G. Borge, J. Cederk¨all, N. Keeley, K. Rusek, C. G. a Ramos, L. A. Acosta, et al., Acta Phys. Pol. B 51, 731 (2020).   
171. J. R. Beene, D. W. Bardayan, A. G. Uribarri, C. J. Gross, K. L. Jones, J. F. Liang, W. Nazarewicz, D. W. Stracener, B. A. Tatum, and R. L. Varner, J. Phys. G: Nucl. Part. Phys. 38, 024002 (2011).   
172. J. F. Liang, J. R. Beene, H. Esbensen, A. Galindo-Uribarri, J. Gomez del Campo, C. J. Gross, M. L. Halbert, P. E. Mueller, D. Shapira, D. W. Stracener, et al., Phys. Rev. C 65, 051603 (2002).   
173. J. F. Liang, J. R. Beene, A. Galindo-Uribarri, J. Gomez del Campo, C. J. Gross, P. A. Hausladen, P. E. Mueller, D. Shapira, D. W. Stracener, R. L. Varner, et al., Phys. Rev. C67, 044603 (2003).   
174. J. J. Kolata, V. Guimar˜aes, D. Peterson, P. Santi, R. White-Stevens, P. A. De Young, G. F. Peaslee, B. Hughey, B. Atalla, M. Kern, et al., Phys. Rev. Lett. 81, 4580 (1998).   
175. M. Ito, K. Yabana, T. Nakatsukasa, and M. Ueda, Nucl. Phys. A 787, 267c (2006).   
176. C. Signorini, D. Pierroutsakou, B. Martin, M. Mazzocco, T. Glodariu, R. Bonetti, A. Guglielmetti, M. La Commara, M. Romoli, M. Sandoli, et al., Eur. Phys. J. A 44, 63 (2010).   
177. M. Mazzocco, C. Signorini, D. Pierroutsakou, T. Glodariu, A. Boiano, C. Boiano, F. Farinon, P. Figuera, D. Filipescu, L. Fortunato, et al., Phys. Rev. C 82, 054604 (2010).   
178. M. Romoli, M. D. Pietro, E. Vardaci, A. D. Francesco, M. Mazzocco, R. Bonetti, A. D. Rosa, T. Glodariu, A. Guglielmetti, G. Inglima, et al., IEEE Trans. Nucl. Sci. 52, 1860 (2005).   
179. N. R. Ma, L. Yang, C. J. Lin, H. Yamaguchi, D. X. Wang, L. J. Sun, M. Mazzocco, H. M. Jia, S. Hayakawa, D. Kahl, et al., Eur. Phys. J. A 55, 87 (2019).   
180. J. J. Kolata, V. Guimar˜aes, D. Peterson, P. Santi, R. White-Stevens, J. von Schwarzenberg, J. D. Hinnefeld, E. F. Aguilera, E. Martinez-Quiroz, D. A.

Roberts, et al., Phys. Rev. C57, R6 (1998).   
181. P. A. DeYoung, B. Hughey, P. L. Jolivette, G. F. Peaslee, J. J. Kolata, V. Guimar˜aes, D. Peterson, P. Santi, H. C. Griffin, J. A. Zimmerman, et al., Phys. Rev. C 58, 3442 (1998).   
182. E. F. Aguilera, J. J. Kolata, F. M. Nunes, F. D. Becchetti, P. A. De Young, M. Goupell, V. Guimar˜aes, B. Hughey, M. Y. Lee, D. Lizcano, et al., Phys. Rev. Lett. 84, 5058 (2000).   
183. E. F. Aguilera, J. J. Kolata, F. D. Becchetti, P. A. De Young, J. D. Hinnefeld, A. Horvath, L. O. Lamm, H. Y. Lee, D. Lizcano, E. Martinez-Quiroz, et al., Phys. Rev. C 63, 061603(R) (2001).   
184. P. A. DeYoung, P. J. Mears, J. J. Kolata, E. F. Aguilera, F. D. Becchetti, Y. Chen, M. Cloughesy, H. Griffin, C. Guess, J. D. Hinnefeld, et al., Phys. Rev. C 71, 051601 (2005).   
185. J. J. Kolata, H. Amro, F. D. Becchetti, J. A. Brown, P. A. DeYoung, M. Hencheck, J. D. Hinnefeld, G. F. Peaslee, A. L. Fritsch, C. Hall, et al., Phys. Rev. C 75, 031302 (2007).   
186. E. F. Aguilera, J. J. Kolata, and L. Acosta, Phys. Rev. C 81, 011604(R) (2010).   
187. V. Guimar˜aes, J. J. Kolata, D. Peterson, P. Santi, R. H. White-Stevens, S. M. Vincent, F. D. Becchetti, M. Y. Lee, T. W. O’Donnell, D. A. Roberts, et al., Phys. Rev. Lett. 84, 1862 (2000).   
188. E. F. Aguilera, E. Martinez-Quiroz, T. L. Belyaeva, J. J. Kolata, and R. Leyte-Gonz´alez, Phys. Atomic Nucl. 71, 1163 (2008).   
189. E. F. Aguilera, P. Amador-Valenzuela, E. Martinez-Quiroz, D. Lizcano, P. Rosales, H. Garc´ıa-Mart´ınez, A. G´omez-Camacho, J. J. Kolata, A. Roberts, L. O. Lamm, et al., Phys. Rev. Lett. 107, 092701 (2011).   
190. J. J. Kolata, E. F. Aguilera, and V. Guimar˜aes, EPJ Web Conf. 163, 00031 (2017).   
191. T. Yamaya, H. Ishiyama, A. Yamazaki, J. Tojima, M. Katoh, T. Kuzumaki, H. Yahata, K. Suzuki, K. Kotajima, T. Shinozuka, et al., Phys. Lett. B 417, 7 (1998).   
192. M. Ueda and N. Takigawa, Nucl. Phys. A 598, 273 (1996).   
193. A. N. Ostrowski, A. C. Shotter, W. Galster, S. Cherubini, T. Davinson, A. M. Laird, and A. Ninane, Phys. Rev. C 60, 064603 (1999).   
194. V. V. Sargsyan, G. G. Adamian, N. V. Antonenko, and P. R. S. Gomes, Phys. Rev. C 88, 044606 (2013).   
195. V. Guimar˜aes, J. J. Kolata, E. F. Aguilera, A. Howard, A. Roberts, F. D. Becchetti, R. O. Torres-Isea, A. Riggins, M. Febrarro, V. Scarduelli, et al., Phys. Rev. C 93, 064607 (2016).   
196. C. Perrin, S. Kox, N. Longequeue, J. B. Viano, M. Buenerd, R. Cherkaoui, A. J. Cole, A. Gamp, J. Menet, R. Ost, et al., Phys. Rev. Lett. 49, 1905 (1982).   
197. S. Kox, A. Gamp, R. Cherkaoui, A. Cole, N. Longequeue, J. Menet, C. Perrin, and J. Viano, Nucl. Phys. A 420, 162 (1984).

198. V. Meyer, R. M. Eisberg, and R. F. Carlson, Phys. Rev. 117, 1334 (1960).   
199. T. Zheng, T. Yamaguchi, A. Ozawa, M. Chiba, R. Kanungo, T. Kato, K. Katori, K. Morimoto, T. Ohnishi, T. Suda, et al., Nucl. Phys. A 709, 103 (2013).   
200. B. Erdemchimeg, A. G. Artukh, S. Davaa, B. M. Hue, T. Isataev, S. A. Klygin, G. A. Kononenko, G. Khuukhenkhuu, S. M. Lukyanov, T. I. Mikhailova, et al., Journal of Physics: Conference Series 1390, 012005 (2019).   
201. L. Jia-Xing, L. Ping-Ping, W. Jian-Song, H. Zheng-Guo, M. Rui-Shi, S. Zhi-Yu, L. Chen, C. Ruo-Fu, X. Hu-Shan, X. Guo-Qing, et al., Chinese Physics C 34, 452 (2010).   
202. G. Alkhazov, A. Dobrovolsky, P. Egelhof, H. Geissel, H. Irnich, A. Khanzadeev, G. Korolev, A. Lobodenko, G. M¨unzenberg, M. Mutterer, et al., Nucl. Phys. A 712, 269 (2002).   
203. A. Villari, W. Mittig, E. Plagnol, Y. Schutz, M. Lewitowicz, L. Bianchi, B. Fernandez, J. Gastebois, A. Gillibert, C. Stephan, et al., Phys. Lett. B 268, 345 (1991).   
204. R. E. Warner, R. A. Patty, P. M. Voyles, A. Nadasen, F. D. Becchetti, J. A. Brown, H. Esbensen, A. Galonsky, J. J. Kolata, J. Kruse, et al., Phys. Rev. C 54, 1700 (1996).   
205. R. E. Warner, F. Carstoiu, J. A. Brown, F. D. Becchetti, D. A. Roberts, B. Davids, A. Galonsky, R. M. Ronningen, M. Steiner, M. Horoi, et al., Phys. Rev. C 74, 014605 (2006).   
206. B. Sherrill, D. Morrissey, J. Nolen, N. Orr, and J. Winger, Nucl. Instrum. Methods Phys. Res. B 70, 298 (1992).   
207. A. Musumarra, P. Figuera, F. D. Luca], A. D. Pietro], P. Finocchiaro, M. Fisichella, M. Lattuada, A. Pakou, M. Pellegriti, G. Randisi, et al., Nucl. Instrum. Methods Phys. Res. A 612, 399 (2010).   
208. R. E. Warner, C. P. Browne, S. E. Darden, J. J. Kolata, A. Rollefson, P. A. Kimoto, and A. Galonsky, Phys. Rev. C 37, 1884 (1988).   
209. A. Pakou, A. Musumarra, D. Pierroutsakou, N. Alamanos, P. Assimakopoulos, N. Divis, G. Doukelis, A. Gillibert, S. Harissopulos, G. Kalyva, et al., Nucl. Phys. A 784, 13 (2006).   
210. A. Pakou, E. Stiliaris, D. Pierroutsakou, N. Alamanos, A. Boiano, C. Boiano, D. Filipescu, T. Glodariu, J. Grebosz, A. Guglielmetti, et al., Phys. Rev. C 87, 014619 (2013).   
211. E. F. Aguilera, P. Amador-Valenzuela, E. Martinez-Quiroz, J. Fern´andez-Arn´aiz, J. J. Kolata, and V. Guimar˜aes, Phys. Rev. C 93, 034613 (2016).   
212. E. Koshchiy, G. Rogachev, E. Pollacco, S. Ahn, E. Uberseder, J. Hooker, J. Bishop, E. Aboud, M. Barbui, V. Goldberg, et al., Nucl. Instrum. Methods Phys. Res. A 957, 163398 (2020).   
213. S. Ilieva, F. Aksouh, G. Alkhazov, L. Chulkov, A. Dobrovolsky, P. Egelhof, H. Geissel, M. Gorska, A. Inglessi, R. Kanungo, et al., Nucl. Phys. A 875, 8 (2012).

214. C. Demonchy, W. Mittig, H. Savajols, P. Roussel-Chomaz, M. Chartier, B. Jurado, L. Giot, D. Cortina-Gil, M. Caama˜no, G. Ter-Arkopian, et al., Nucl. Instrum. Methods Phys. Res. A 573, 145 (2007).   
215. S. Beceiro-Novo, T. Ahn, D. Bazin, and W. Mittig, Prog. Part. Nucl. Phys. 84, 124 (2015).   
216. D. Bazin, T. Ahn, Y. Ayyad, S. Beceiro-Novo, A. Macchiavelli, W. Mittig, and J. Randhawa, Progress in Particle and Nuclear Physics p. 103790 (2020).   
217. J. Giovinazzo, J. Pancin, J. Pibernat, and T. Roger, Nucl. Instrum. Methods Phys. Res. A 953, 163184 (2020).   
218. W. Mittig, S. Beceiro-Novo, A. Fritsch, F. Abu-Nimeh, D. Bazin, T. Ahn, W. Lynch, F. Montes, A. Shore, D. Suzuki, et al., Nucl. Instrum. Methods Phys. Res. A 784, 494 (2015).   
219. J. Kolata, A. Howard, W. Mittig, T. Ahn, D. Bazin, F. Becchetti, S. Beceiro-Novo, Z. Chajecki, M. Febbrarro, A. Fritsch, et al., Nucl. Instrum. Methods Phys. Res. A 830, 82 (2016).   
220. B. Franzke, Nucl. Instrum. Methods Phys. Res. B 24, 18 (1987).   
221. J. Xia, W. Zhan, B. Wei, Y. Yuan, M. Song, W. Zhang, X. Yang, P. Yuan, D. Gao, H. Zhao, et al., Nucl. Instrum. Methods Phys. Res. A 488, 11 (2002).   
222. M. Mutterer, P. Egelhof, V. Eremin, S. Ilieva, N. Kalantar-Nayestanaki, O. Kiselev, H. Kollmus, T. Kr¨oll, M. Kuilman, L. X. Chung, et al., Physica Scripta T166, 014053 (2015).   
223. M. von Schmid, S. Bagchi, S. B¨onig, M. Csatl´os, I. Dillmann, C. Dimopoulou, P. Egelhof, V. Eremin, T. Furuno, H. Geissel, et al., Physica Scripta T166, 014005 (2015).   
224. J. C. Zamora, T. Aumann, S. Bagchi, S. B¨onig, M. Csatl´os, I. Dillmann, C. Dimopoulou, P. Egelhof, V. Eremin, T. Furuno, et al., Phys. Rev. C 96, 034617 (2017).   
225. J. Zamora, T. Aumann, S. Bagchi, S. B¨onig, M. Csatl´os, I. Dillmann, C. Dimopoulou, P. Egelhof, V. Eremin, T. Furuno, et al., Phys. Lett. B 763, 16 (2016).   
226. M. Beckerman, J. Ball, H. Enge, M. Salomaa, A. Sperduto, S. Gazes, A. DiRienzo, and J. D. Molitoris, Phys. Rev. C 23, 1581 (1981).   
227. M. Beckerman, M. Salomaa, A. Sperduto, J. D. Molitoris, and A. DiRienzo, Phys. Rev. C 25, 837 (1982).   
228. W. Reisdorf, F. P. Hessberger, K. D. Hildenbrand, S. Hofmann, G. M¨unzenberg, K.-H. Schmidt, J. H. R. Schneider, W. F. W. Schneider, K. S¨ummerer, G. Wirth, et al., Nucl. Phys. A614, 112 (1997).   
229. R. G. Stokstad and E. E. Gross, Phys. Rev. C23, 281 (1981).   
230. P. R. S. Gomes, D. R. Mendes Junior, L. F. Canto, J. Lubian, and P. N. de Faria, Few Body Syst. 57, 205 (2016).   
231. P. R. S. Gomes, J. Lubian, I. Padr´on, and R. M. Anjos, Phys. Rev. C 71, 017601 (2005).

232. M. Aversa, D. Abriola, M. A. G. Alvarez, A. Arazi, M. A. Cardona, L. C. Chamon, E. de Barbar´a, J. de Jes´us, J. P. Fern´andez-Garc´ıa, L. R. Gasques, et al., Phys. Rev. C 101, 044601 (2020).   
233. M. Kaushik, G. Gupta, S. Thakur, H. Krishnamoorthy, P. P. Singh, V. V. Parkar, V. Nanal, A. Shrivastava, R. G. Pillay, K. Mahata, et al., Phys. Rev. C 101, 034611 (2020).   
234. F. Torabi, E. F. Aguilera, O. N. Ghodsi, and A. G´omez-Camacho, Nucl. Phys. A 994, 121661 (2020).   
235. S. Ali, K. Kumar, M. Gull, T. Ahmad, I. A. Rizvi, A. Agarwal, A. K. Chaubey, and S. S. Ghugre, Phys. Rev. C 100, 064607 (2019).   
236. R. Gharaei and G. L. Zhang, Nucl. Phys. A 990, 294 (2019).   
237. N. Rani, P. Singh, R. Kumar, R. Kumar, and R. Kharab, Mod. Phys. Lett. A 34, 1950087 (2019).   
238. V. V. Sargsyan, G. G. Adamian, N. V. Antonenko, W. Scheid, and H. Q. Zhang, Phys. Rev. C 95, 054619 (2017).   
239. J. Rangel, M. Cortes, J. Lubian, and L. F. Canto, Phys. Lett. B 803, 135337 (2020).   
240. Y. W. Wu, Z. H. Liu, C. J. Lin, H. Q. Zhang, M. Ruan, F. Yang, Z. C. Li, M. Trotta, and K. Hagino, Phys. Rev. C68, 044605 (2003).   
241. P. K. Rath, S. Santra, N. L. Singh, R. Tripathi, V. V. Parkar, B. K. Nayak, K. Mahata, R. Palit, S. Kumar, S. Mukherjee, et al., Phys. Rev. C 79, 051601(R) (2009).   
242. A. Mukherjee, S. Roy, M. K. Pradhan, M. S. Sarkar, P. Basu, B. Dasmahapatra, T. Bhattacharya, S. Bhatacharya, S. K. Basu, A. Chatterjee, et al., Phys. Lett. B 636, 91 (2006).   
243. H. Kumawat, V. Jha, V. V. Parkar, B. Roy, S. K. Pandit, R. Palit, P. K. Rath, C. F. Palshetkar, S. K. Sharma, S. Thakur, et al., Phys. Rev. C 86, 024607 (2012).   
244. M. K. Pradhan, A. Mukherjee, P. Basu, A. Goswami, R. Kshetri, S. Roy, P. R. Chowdhury, M. S. Sarkar, R. Palit, V. V. Parkar, et al., Phys. Rev. C 83, 064606 (2011).   
245. A. Shrivastava, A. Navin, A. Lemasson, K. Ramachandran, V. Nanal, M. Rejmund, K. Hagino, T. Ishikawa, S. Bhattacharyya, A. Chatterjee, et al., Phys. Rev. Lett. 103, 232702 (2009).   
246. M. S. Gautam, K. Vinod, S. Duhan, R. P. Chahal, and H. Khatri, Nucl. Phys. A 998, 121730 (2020).   
247. V. Jha, V. V. Parkar, and S. Kailas, Phys. Rev. C 89, 034605 (2014).   
248. B. Wang, W. J. Zhao, P. R. S. Gomes, E. G. Zhao, and S. G. Zhou, Phys. Rev. C 90, 034612 (2014).   
249. M. Shuaib, V. R. Sharma, A. Yadav, M. K. Sharma, P. P. Singh, D. P. Singh, R. Kumar, R. P. Singh, S. Muralithar, B. P. Singh, et al., Phys. Rev. C 98, 014605 (2018).   
250. V. Morcelle, R. Lichtenth¨aler, A. L´epine-Szily, V. Guimar˜aes, K. C. C. Pires, J. Lubian, D. R. Mendes Junior, P. N. de Faria, J. J. Kolata, F. D.

Becchetti, et al., Phys. Rev. C 95, 014615 (2017).   
251. E. Benjamim, A. L´epine-Szily, D. Mendes Junior, R. Lichtenth¨aler, V. Guimar˜aes, P. Gomes, L. Chamon, M. Hussein, A. Moro, A. Arazi, et al., Phys. Lett.B 647, 30 (2007).   
252. J. M. Figueira, J. O. Fern´andez Niello, D. Abriola, A. Arazi, E. Capurro, O. A. andde Barbar´a, G. V. Mart´ı, D. Mart´ınez Heimann, A. E. Negri, A. J. Pacheco, I. Padr´on, et al., Phys. Rev. C 75, 017602 (2007).   
253. J. M. Figueira, D. Abriola, J. O. Fern´andez Niello, A. Arazi, O. A. Capurro, E. d. Barbar´a, G. V. Mart´ı, D. Mart´ınez Heimann, A. J. Pacheco, J. E. Testoni, et al., Phys. Rev. C 73, 054603 (2006).   
254. P. R. S. Gomes, R. M. Anjos, C. Muri, J. Lubian, I. Padr´on, L. C. Chamon, R. Liguori Neto, N. Added, J. O. Fern´andez Niello, G. V. Mart´ı, et al., Phys. Rev. C70, 054605 (2004).   
255. G. V. Mart´ı, P. R. S. Gomes, M. D. Rodriguez, J. O. Fern´andez Niello, O. A. Capurro, A. J. Pacheco, J. E. Testoni, M. Ramirez, A. Arazi, I. Padr´on, et al., Phys. Rev. C71, 027602 (2005).   
256. V. Morcelle, R. Lichtenth¨aler, R. Linares, M. C. Morais, V. Guimar˜aes, A. L´epine-Szily, P. R. S. Gomes, J. Lubian, D. R. Mendes Junior, P. N. De Faria, et al., Phys. Rev. C 89, 044611 (2014).   
257. E. Crema, Masters degree thesis, Universidade de S˜ao Paulo (1979), unpublished.   
258. M. Biswas, S. Roy, M. Sinha, M. K. Pradhan, A. Mukherjee, P. Basu, H. Majumdar, K. Ramachandran, and A. Shrivastava, Nucl. Phys. A 802, 67 (2008).   
259. K. O. Pfeiffer, E. Speth, and K. Bethege, Nucl. Phys. A 206, 545 (1973).   
260. M. Mazzocco, D. Torresi, D. Pierroutsakou, N. Keeley, L. Acosta, A. Boiano, C. Boiano, T. Glodariu, A. Guglielmetti, M. La Commara, et al., Phys. Rev. C 92, 024615 (2015).   
261. J. C. Morales-Rivera, E. Martinez-Quiroz, T. L. Belyaeva, E. F. Aguilera, D. Lizcano, and A.-V. P., EPJ Web of Conferences 117, 07027ß (2016).   
262. P. R. S. Gomes, M. D. Rodriguez, G. V. Mart´ı, I. Padr´on, L. C. Chamon, J. O. F. Niello, O. A. Capurro, A. J. Pacheco, J. E. Testoni, A. Arazi, et al., Phys. Rev. C71, 034608 (2005).   
263. N. Keeley, J. A. Christley, N. M. Clarke, B. R. Fulton, J. S. Lilley, M. A. Nagarajan, and I. J. Thompson, Nucl. Phys. A 582, 314 (1995).   
264. N. Deshmukh and J. Lubian, Eur. Phys. J. A 54, 101 (2018).   
265. N. Deshmukh, J. Lubian, and S. Mukherjee, Europhys. Lett. 127, 12001 (2019).