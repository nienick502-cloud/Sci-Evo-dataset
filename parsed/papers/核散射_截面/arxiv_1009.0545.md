# Running Coupling Corrections to High Energy Inclusive Gluon Production

W. A. Horowitz,1,2 Yuri V. Kovchegov 1

1Department of Physics, The Ohio State University, Columbus, OH 43210, USA

2Department of Physics, The University of Cape Town, Rondebosch 7701, South Africa

E-mail addresses: horowitz@mps.ohio-state.edu, yuri@mps.ohio-state.edu

Abstract: We calculate running coupling corrections for the lowest-order gluon production cross section in high energy hadronic and nuclear scattering using the BLM scale-setting prescription. In the final answer for the cross section the three powers of fixed coupling are replaced by seven factors of running coupling, five in the numerator and two in the denominator, forming a ‘septumvirate’ of running couplings, analogous to the ‘triumvirate’ of running couplings found earlier for the small- $x$ BFKL/BK/JIMWLK evolution equations. It is interesting to note that the two running couplings in the denominator of the ‘septumvirate’ run with complex-valued momentum scales, which are complex conjugates of each other, such that the production cross section is indeed real. We use our lowest-order result to conjecture how running coupling corrections may enter the full fixed-coupling $k _ { T }$ -factorization formula for gluon production which includes non-linear small- $x$ evolution.

Keywords: Running coupling, gluon production, Color Glass Condensate.

# Contents

1. Introduction 1   
2. Brief Review of the Fixed-Coupling Calculation 3

3. Running Coupling Corrections 6

3.1 Bremsstrahlung Diagrams 7   
3.2 Triple-Gluon Vertex Diagrams 12   
3.3 The Result 17

4. Discussion 20

4.1 Conjecture for the Running Coupling Corrected $k _ { T }$ -Factorization Formula 20   
4.2 Multiplicity per Unit Rapidity 22   
4.3 Summary 24

A. Loop integral evaluation 25

# 1. Introduction

With the advent of the LHC era the physics of parton saturation/Color Glass Condensate (CGC) [1–28] needs to produce more quantitative predictions with higher accuracy. To achieve this goal running coupling corrections to the Jalilian-Marian–Iancu–McLerran–Weigert–Leonidov–Kovner (JIMWLK) [13–20] and Balitsky–Kovchegov (BK) [21–25] evolution equations have been calculated recently in [29–32] (see also [33, 34]). This led to a significant improvement in the comparison of CGC predictions with data from heavy ion and deep inelastic scattering (DIS) experiments [35–37]. However, to make such comparisons theoretically consistent for observables like hadron production in proton-proton $( p p )$ , proton-nucleus $( p A )$ and nucleus-nucleus $( A A )$ collisions one needs to also include running coupling corrections into the formulas for particle production.

While an exact analytic formula for gluon production in $A A$ collisions is still not known, we do know that in $p p$ and $p A$ collisions gluon production at the level of classical gluon fields and leading- $\ln 1 / x$ nonlinear quantum evolution is given by the $k _ { T }$ -factorization formula [1, 38–42]:

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 \alpha_ {s}}{C _ {F}} \frac {1}{\boldsymbol {k} ^ {2}} \int d ^ {2} q \phi_ {p} (\boldsymbol {q}, y) \phi_ {A} (\boldsymbol {k} - \boldsymbol {q}, Y - y). \tag {1.1}
$$

Here $Y$ is the total rapidity interval of the collision, $C _ { F } = ( N _ { c } ^ { 2 } - 1 ) / 2 N _ { c }$ , boldface variables denote two-component transverse plane vectors $\pmb { k } = ( k ^ { 1 } , k ^ { 2 } )$ , and $\phi _ { p }$ , $\phi _ { A }$ are the unintegrated gluon distributions in the proton and the nucleus, respectively, which are defined by [28, 38, 40]

$$
\phi_ {A} (\boldsymbol {k}, y) = \frac {C _ {F}}{\alpha_ {s} (2 \pi) ^ {3}} \int d ^ {2} b d ^ {2} r e ^ {- i \boldsymbol {k} \cdot \boldsymbol {r}} \nabla_ {r} ^ {2} N _ {G} (\boldsymbol {r}, \boldsymbol {b}, y) \tag {1.2}
$$

and

$$
\phi_ {p} (\boldsymbol {k}, y) = \frac {C _ {F}}{\alpha_ {s} (2 \pi) ^ {3}} \int d ^ {2} b d ^ {2} r e ^ {- i \boldsymbol {k} \cdot \boldsymbol {r}} \nabla_ {r} ^ {2} n _ {G} (\boldsymbol {r}, \boldsymbol {b}, y). \tag {1.3}
$$

In Eq. (1.2) the quantity $N _ { G } ( \pmb { r } , \pmb { b } , \pmb { y } )$ denotes the forward scattering amplitude for a gluon dipole of transverse size $\mathbf { \nabla } ^ { \prime }$ with its center located at the impact parameter $^ { b }$ scattering on a target nucleus with total rapidity interval $y$ . $N _ { G } ( \pmb { r } , \pmb { b } , \pmb { y } )$ can, in general, be found from the JIMWLK evolution equation [13–20]. In the large- $N _ { c }$ limit it is related to the quark dipole forward scattering amplitude on the same nucleus $N ( r , b , y )$ by

$$
N _ {G} (\boldsymbol {r}, \boldsymbol {b}, y) = 2 N (\boldsymbol {r}, \boldsymbol {b}, y) - N (\boldsymbol {r}, \boldsymbol {b}, y) ^ {2}, \tag {1.4}
$$

where $N ( r , b , y )$ can be found from the BK evolution equation [21–25] (see also [43] for approximate ways of finding $N _ { G }$ beyond the large- $N _ { c }$ limit without solving the JIMWLK equation). The quantity $n _ { G } ( \pmb { r } , \pmb { b } , y )$ from Eq. (1.3) is also a gluon dipole amplitude, but taken in a dilute regime, where it is found by solving the linear Balitsky-Fadin-Kuraev-Lipatov (BFKL) evolution equation [44, 45].

In our notation the projectile or target is referred to as a ‘proton’ if the transverse momenta of interest in the problem are much larger than the projectile’s (target’s) saturation scale, such that only linear evolution is needed to describe such a projectile/target. Conversely, if the saturation scale of the projectile/target is comparable to the momentum scales of interest then we refer to this projectile/target as a ‘nucleus’. With this notation, Eq. (1.1) is not an assumption, but an exact answer which resulted in a non-obvious way from a diagram resummation done in [38, 41].

As mentioned above, the running coupling corrections have been calculated for the BFKL, BK, and JIMWLK evolution equations in [29–32] and for the initial conditions to these evolution equations in the Appendix of [46], yielding a prescription of how to find $N _ { G }$ and $n _ { G }$ in Eqs. (1.2) and (1.3) including running coupling corrections. However, there are three more factors of strong coupling $\alpha _ { s }$ in Eqs. (1.1), (1.2), and (1.3) for which one needs to set the scale. The first steps in this direction were taken in [46], where it was shown that, in accordance with conventional wisdom, in order to include running coupling corrections in Eq. (1.1) one has to slightly re-define the observable: on top of gluon production, one has to allow for contributions where the would-be produced gluon splits into a collinear gluon-gluon (or quark–anti-quark) pair. To ensure that the particles in the pair are really collinear, one can put a bound on the virtuality of the gluon splitting into a pair, by requiring that $k ^ { 2 } < \Lambda _ { \mathrm { c o l l } } ^ { 2 }$ , where $k ^ { \mu }$ is the four-momentum of the would-be produced gluon and $\Lambda _ { \mathrm { c o l l } }$

is some collinear infrared (IR) cutoff. In [46] it was demonstrated that, for the inclusive production cross section of gluons and collinear GG or $q q$ pairs with the invariant mass less than $\Lambda _ { \mathrm { c o l l } }$ , at least one factor of the coupling is $\alpha _ { s } ( \Lambda _ { \mathrm { c o l l } } ^ { 2 } )$ . While it may seem tempting to use this result and replace $\alpha _ { s }$ in Eq. (1.1) by $\alpha _ { s } ( \Lambda _ { \mathrm { c o l l } } ^ { 2 } )$ constructing a guess for the final answer, it is not even clear a priori that Eq. (1.1) retains its fixed-coupling, $k _ { T }$ -factorized form after the running coupling corrections are included. Moreover, there are factors of fixed couplings in Eqs. (1.2) and (1.3) for which one also has to specify the momentum scale. Therefore the problem of setting the scale of the running couplings for the gluon production cross section needs to be addressed by a detailed calculation, which we will perform here.1

In this paper we will tackle this problem by calculating the running coupling corrections to the lowest order $( O ( \alpha _ { s } ^ { 3 } ) )$ gluon production cross section [50–53]. Our lowest-order result will allow us to conjecture how Eq. (1.1) would be modified due to running coupling corrections. We will calculate the running coupling corrections using the scale-setting prescription due to Brodsky, Lepage, and Mackenzie (BLM) [54]. This prescription assumes that the scale of the coupling set by the introduction of resummed single-quark-loop corrections is the scale of the coupling set by the full calculation including both quark and gluon loop corrections to the propagators and vertices. After finding the $N _ { f }$ corrections due to resummed quark loops, one ‘completes the beta function’ by replacing the $N _ { f }$ in the corrections with $- 6 \pi \beta _ { 2 }$ . (Since we will be resumming powers of $\alpha _ { s } N _ { f }$ the calculation will not employ the large- $N _ { c }$ limit.)

The paper is structured as follows. We begin in Sec. 2 by briefly reviewing the fixed-coupling lowest-order calculation of the high energy inclusive gluon production cross section in quark-quark scattering. We then include running coupling corrections in Sec. 3. We begin with the easier bremsstrahlung diagrams in Sec. 3.1, and then move on to the case of diagrams with the triplegluon vertex in Sec. 3.2. The final result for the gluon production cross section is given by Eqs. (3.31) and (3.32) in Sec. 3.3. We conclude by conjecturing the running coupling generalization of Eq. (1.1) given by Eq. (4.7) in Sec. 4.1 and by discussing the implications of our result on the CGC predictions for particle multiplicity $d N / d \eta$ in heavy ion collisions as a function of the centrality of the collision in Sec. 4.2.

# 2. Brief Review of the Fixed-Coupling Calculation

Consider the leading-order contributions to the production of a gluon in a high-energy quark-quark scattering in standard Feynman perturbation theory, which we will use throughout the paper. We set up the problem in the experimentally relevant momentum regime such that one incoming quark has very large “ $^ +$ ” momentum $p _ { 1 } ^ { \mu } = ( p _ { 1 } ^ { + } , 0 , \mathbf { 0 } )$ , where we use light-cone coordinates $( + , - , \bot )$

throughout the paper with the normalization $v ^ { \pm } = ( v ^ { 0 } \pm v ^ { 3 } ) / \sqrt { 2 }$ for a 4-vector $v ^ { \mu }$ , and the other incoming quark has very large “ $-$ ” momentum $p _ { 2 } ^ { \mu } = ( 0 , p _ { 2 } ^ { - } , \mathbf { 0 } )$ . We take $p _ { 1 } ^ { + }$ and $p _ { 2 } ^ { - }$ to have the same order of magnitude, and $p _ { 1 } ^ { + }$ and $p _ { 2 } ^ { - }$ are large compared to any other momentum scale in the problem. This is the eikonal approximation, and, in particular, $p _ { 1 } ^ { + }$ and $p _ { 2 } ^ { - }$ are large compared to the transverse momentum of the final state particles. Throughout the paper we will work in the light-cone gauge, $\eta \cdot A = A ^ { + } = 0$ , with $\eta ^ { \mu } = ( 0 , 1 , \mathbf { 0 } )$ . In this case the three dominant leading order Feynman diagrams are shown in Fig. 1, which we will refer to as the triple-gluon vertex (A) and bremsstrahlung (B and C) diagrams. Note that the two bremsstrahlung diagrams that can be drawn with an emitted gluon connecting to the lower quark line are suppressed due to eikonality in this $A ^ { + } = 0$ light-cone gauge: an easy way to see this is to notice that at high energy the gluon emission from the lower quark line should come in to leading order with a factor of $\gamma ^ { - }$ in the quark-gluon vertex, which would be multiplied by the gluon polarization component $\epsilon _ { \lambda } ^ { + }$ , which, in turn, is zero in $A ^ { + } = 0$ light-cone gauge.

![](images/fec765b415f32cb833226960d77dedcad1a876b9b9928983ba15969886e5d4c5.jpg)

![](images/dc155990c1aa30c2bf080ff4f0f57b08c00335bb6f30c9c1cf6fc5213c6a3490.jpg)

![](images/4c8fa481688d4bb7d819c611a79c9096e173a30e30b2bfe1fae71ceec9c1d929.jpg)  
Figure 1: Diagrams contributing to the lowest-order gluon production in quark-quark scattering at high energy in the $A ^ { + } = 0$ light-cone gauge. The blob in A denotes a triple-gluon vertex while the outgoing gluon line in C is visualized as disconnected for clarity (there are only two gluon lines in C). The initial and final quark momenta and fundamental color indices are indicated on diagram A, the adjoint color indices are shown in diagrams A and B, and the initial and final quark helicities are indicated on diagram C.

In a process with three final state on-shell particles, there are five unconstrained momentum components in the cross section; we choose to take these components to be the components of the transverse momentum transferred from the lower quark line, $\mathbf { \pmb q }$ , and the components of the transverse momentum and the plus momentum of the emitted gluon, $\boldsymbol { k }$ and $k ^ { + }$ , respectively.

On-shellness of the final particles in Fig. 1 in particular gives for the top quark line $0 \ : =$ $( p _ { 1 } - k + q ) ^ { 2 } \approx - 2 p _ { 1 } ^ { + } ( k ^ { - } - q ^ { - } )$ , such that

$$
q ^ {-} = k ^ {-} = \frac {\mathbf {k} ^ {2}}{2 k ^ {+}} \tag {2.1}
$$

to eikonal accuracy (i.e. to leading order in inverse powers of the large momenta, $p _ { 1 } ^ { + }$ and $p _ { 2 } ^ { - }$ ). Similarly imposing the on-shell condition on the outgoing quark line at the bottom of Fig. 1 yields

$$
q ^ {+} = 0 \tag {2.2}
$$

with the same accuracy.

The light-cone gauge propagator without loop corrections is

$$
\frac {- i}{q ^ {2} + i \epsilon} D _ {\mu \nu} (q) = \frac {- i}{q ^ {2} + i \epsilon} \left[ g _ {\mu \nu} - \frac {\eta_ {\mu} q _ {\nu} + \eta_ {\nu} q _ {\mu}}{\eta \cdot q} \right], \tag {2.3}
$$

and the outgoing gluon polarization vector $\epsilon _ { \lambda }$ obeys $\eta \cdot \epsilon _ { \lambda } = \epsilon _ { \lambda } ^ { + } = 0$ and $\boldsymbol { k } \cdot \boldsymbol { \epsilon } _ { \lambda } = 0$ for the two polarizations $\lambda = 1$ , 2; one may then immediately set

$$
\epsilon_ {\lambda} = \epsilon_ {\lambda} ^ {*} = \left(0, \frac {\boldsymbol {k} \cdot \boldsymbol {\epsilon}}{k ^ {+}}, \boldsymbol {\epsilon}\right). \tag {2.4}
$$

Exploiting the eikonality of the process, we can approximate

$$
\bar {u} _ {\sigma_ {2} ^ {\prime}} (p _ {2} - q) \gamma^ {\mu} u _ {\sigma_ {2}} (p _ {2}) \simeq 2 p _ {2} ^ {\mu} \delta_ {\sigma_ {2} ^ {\prime}, \sigma_ {2}}, \tag {2.5}
$$

where $\boldsymbol { \sigma } _ { 2 } ^ { \prime }$ and $\sigma _ { 2 }$ are the helicities of the outgoing and incoming lower line quarks, respectively [55]. A similar expression holds for the top quark line. The anti-commutation relations of the gamma matrices along with the Dirac equation yields the useful relation [56]

$$
\bar {u} (p) \notin p / = 2 p \cdot \epsilon \bar {u} (p); \quad p / \notin u (p) = 2 p \cdot \epsilon u (p). \tag {2.6}
$$

Finally, we will also find the following type of cancellation useful

$$
\bar {u} \left(p _ {2}\right) q / u \left(p _ {2}\right) = \bar {u} \left(p _ {2} - q\right) \left(- \left(\not p _ {2} - q /\right) + \not p _ {2}\right) u \left(p _ {2}\right) = 0, \tag {2.7}
$$

by the Dirac equation.

With the above notation and machinery one may almost immediate write down the leading order in eikonality result for the bremsstrahlung diagrams,

$$
i \mathcal {M} _ {B} \simeq \frac {8 i g ^ {3} p _ {1} ^ {+} p _ {2} ^ {-}}{\boldsymbol {q} ^ {2} \boldsymbol {k} ^ {2}} \boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k} (t ^ {a} t ^ {c}) _ {i ^ {\prime}, i} (t ^ {c}) _ {j ^ {\prime}, j} \delta_ {\sigma_ {1} ^ {\prime}, \sigma_ {1}} \delta_ {\sigma_ {2} ^ {\prime}, \sigma_ {2}} \tag {2.8}
$$

$$
i \mathcal {M} _ {C} \simeq - \frac {8 i g ^ {3} p _ {1} ^ {+} p _ {2} ^ {-}}{\boldsymbol {q} ^ {2} \boldsymbol {k} ^ {2}} \boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k} (t ^ {c} t ^ {a}) _ {i ^ {\prime}, i} (t ^ {c}) _ {j ^ {\prime}, j} \delta_ {\sigma_ {1} ^ {\prime}, \sigma_ {1}} \delta_ {\sigma_ {2} ^ {\prime}, \sigma_ {2}}, \tag {2.9}
$$

where repeated indices are summed over. A slightly more involved calculation yields

$$
i \mathcal {M} _ {A} \simeq - \frac {8 g ^ {3} p _ {1} ^ {+} p _ {2} ^ {-}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2} \boldsymbol {q} ^ {2}} \epsilon_ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}) f ^ {a b c} (t ^ {b}) _ {i ^ {\prime}, i} (t ^ {c}) _ {j ^ {\prime}, j} \delta_ {\sigma_ {1} ^ {\prime}, \sigma_ {1}} \delta_ {\sigma_ {2} ^ {\prime}, \sigma_ {2}} \tag {2.10}
$$

for the triple-gluon vertex diagram to leading order in eikonality.

Summing the results for $\mathcal { M } _ { A }$ , $\mathcal { M } _ { B }$ , and $\mathcal { M } _ { C }$ and using the commutation relations for the color matrices one finds that the matrix element for gluon production to leading order in fixed coupling $\alpha _ { s }$ and eikonality is

$$
i (\mathcal {M} _ {A} + \mathcal {M} _ {B} + \mathcal {M} _ {C}) = \frac {8 g ^ {3} p _ {1} ^ {+} p _ {2} ^ {-}}{q ^ {2}} \boldsymbol {\epsilon} _ {\lambda} \cdot \left(\frac {\boldsymbol {k}}{\boldsymbol {k} ^ {2}} - \frac {\boldsymbol {k} - \boldsymbol {q}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}}\right) f ^ {a b c} (t ^ {b}) _ {i ^ {\prime}, i} (t ^ {c}) _ {j ^ {\prime}, j} \delta_ {\sigma_ {1} ^ {\prime}, \sigma_ {1}} \delta_ {\sigma_ {2} ^ {\prime}, \sigma_ {2}} \tag {2.11}
$$

After summing over final states, averaging over initial states, and including the kinematic factors one arrives at the following expression for the gluon production cross section [50–53]:

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 \alpha_ {s} ^ {3} C _ {F}}{\pi^ {2}} \int \frac {d ^ {2} q}{(\mathbf {q} ^ {2}) ^ {2}} \sum_ {\lambda} \left| \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot (\mathbf {k} - \mathbf {q})}{(\mathbf {k} - \mathbf {q}) ^ {2}} - \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot \mathbf {k}}{\mathbf {k} ^ {2}} \right| ^ {2}. \tag {2.12}
$$

Summing over gluon polarizations and opening the brackets in Eq. (2.12) yields

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 \alpha_ {s} ^ {3} C _ {F}}{\pi^ {2}} \frac {1}{\pmb {k} ^ {2}} \int \frac {d ^ {2} q}{\pmb {q} ^ {2} (\pmb {k} - \pmb {q}) ^ {2}}. (2. 1 3)
$$

Our goal now is to set the scales for the three couplings in Eq. (2.13). Before we do that let us note that the lowest-order gluon distribution of a quark is (see e.g. [12, 40])

$$
\phi (\boldsymbol {k}, y) = \frac {\alpha_ {s} C _ {F}}{\pi} \frac {1}{\boldsymbol {k} ^ {2}}. \tag {2.14}
$$

With the help of Eq. (2.14) we can see that Eq. (2.13) reduces exactly to Eq. (1.1) for quark-quark scattering.

# 3. Running Coupling Corrections

To include running coupling corrections we will follow the BLM scale-setting procedure [54]. We will first resum the contribution of all quark bubble corrections giving powers of $\alpha _ { \mu } N _ { f }$ , with $N _ { f }$ the number of quark flavors and $\alpha _ { \mu }$ the physical coupling at some arbitrary renormalization scale $\mu$ . We will then complete $N _ { f }$ to the full beta-function by replacing

$$
N _ {f} \rightarrow - 6 \pi \beta_ {2} \tag {3.1}
$$

in the obtained expression. Here

$$
\beta_ {2} = \frac {1 1 N _ {c} - 2 N _ {f}}{1 2 \pi} \tag {3.2}
$$

is the one-loop QCD beta-function. After this, the powers of $\alpha _ { \mu } \beta _ { 2 }$ should combine into physical running couplings

$$
\alpha_ {s} (Q ^ {2}) = \frac {\alpha_ {\mu}}{1 + \alpha_ {\mu} \beta_ {2} \ln \frac {Q ^ {2}}{\mu^ {2}}} \tag {3.3}
$$

at various momentum scales $Q$ which would follow from this calculation. Throughout this paper we will use the $\overline { { \mathrm { M } S } }$ renormalization scheme.

Below we will begin by including running coupling corrections into the bremsstrahlung diagram B from Fig. 1 assuming that only a gluon can be produced in the final state. By doing so we will not be able to specify the scale for one of the coupling constants in the diagram, obtaining a contribution to the cross section that depends on an arbitrary renormalization scale $\mu$ . Following [46] we will rectify the problem by redefining the gluon production cross-section to include production of collinear gluon–gluon and quark–anti-quark pairs with the invariant mass lower than some collinear IR cutoff $\Lambda _ { \mathrm { c o l l } } ^ { 2 }$ . We will see that this new observable will be completely $\mu$ -independent and expressible in terms of the running coupling constants.

# 3.1 Bremsstrahlung Diagrams

We begin by considering bremsstrahlung diagrams B and C in Fig. 1. It is easier to see how running coupling corrections are organized if we consider the production cross section, which is given by the square of the sum of the diagrams in Fig. 1. Consider the square of the diagram B shown in the left panel of Fig. 2. Let us include all the quark loop corrections to it which bring in powers of $\alpha _ { \mu } N _ { f }$ . The non-vanishing quark loop corrections to diagram B from Fig. 1 squared are shown in the right panel of Fig. 2, where we imply that quark loops need to be resummed to all orders on the propagators where we inserted several loops. The corrections are limited to quark bubbles on the propagator of the gluon line carrying momentum $q$ in the amplitude and in the complex conjugate amplitude. The (massless) quark loop corrections on the outgoing gluon line are zero in dimensional regularization, since the produced gluon is on mass shell, $k ^ { 2 } = 0$ [57]. Throughout the paper we assume that the quarks in the loops are massless: quark mass is not needed to fix the scale of the coupling constants.

![](images/c718ede3e24d8b8a1ccd9e8466c4163b10dfbfb565611d2865a88ff1cfaaf4e6.jpg)  
Figure 2: Inclusion of quark loop corrections to diagram B from Fig. 1 squared. Vertical dashed line denotes the final state cut.

The result of the resummation of quark bubble corrections to a gluon propagator is well-known (see e.g. [56, 57]), and this result is particularly simple for the gluon propagator in the light-cone gauge that we are working in. With the form of the light-cone gauge propagator without loop corrections, Eq. (2.3), one can straightforwardly show that, if the contribution from each quark loop is written as

$$
\left[ q ^ {2} g _ {\alpha \beta} - q _ {\alpha} q _ {\beta} \right] i \Pi \left(q ^ {2}\right) \tag {3.4}
$$

then the resummed gluon propagator is

$$
\frac {- i}{\left(q ^ {2} + i \epsilon\right) \left[ 1 - \Pi \left(q ^ {2}\right) \right]} D _ {\mu \nu} (q). \tag {3.5}
$$

One can see that the tensor structure of the bare propagator, Eq. (2.3), is not modified by the loop corrections, Eq. (3.5). An explicit calculation of $\Pi ( q ^ { 2 } )$ to leading order due to the quark loop and the $N _ { f }$ part of the gluon propagator counterterm in the $\mathrm { \overline { { M S } } }$ renormalization scheme yields [57]

$$
\frac {- i}{(q ^ {2} + i \epsilon) \left[ 1 - \frac {\alpha_ {\mu} N _ {f}}{6 \pi} \ln \frac {- q ^ {2} - i \epsilon}{\mu^ {2}} \right]} D _ {\mu \nu} (q) \tag {3.6}
$$

where

$$
\mu^ {2} = \mu_ {\overline {{\mathrm {M S}}}} ^ {2} e ^ {5 / 3}. \tag {3.7}
$$

We introduce a graphical shorthand for this resummed gluon propagator in Fig. 3. In the same figure we also define for later convenience the cut of this resummed gluon propagator.

$$
\begin{array}{l} \left(a\right) \quad \begin{array}{l} \text {0 0 0 0 0 0 0 0 0 0} \\ \equiv \text {0 0 0 0 0} + \text {0 0 0 0 0} \bigcirc \text {0 0 0 0 0} + \text {0 0 0 0 0} \bigcirc \text {0 0} \text {0 0 0 0} + \dots \end{array} \\ \begin{array}{c c c c c c c} & \vdots & \vdots & \vdots \\ & \overbrace {0 0 0 0 0 0 0 0 0} ^ {\text {}} & \equiv \overbrace {0 0 0 0 0} ^ {\text {}} + \overbrace {0 0 0 0 0} ^ {\text {}} \bigcirc \overbrace {0 0 0 0 0} ^ {\text {}} + \overbrace {0 0 0 0 0} ^ {\text {}} \bigcirc \overbrace {0 0 0 0 0} ^ {\text {}} + & \dots \\ (b) & \vdots & \vdots & \vdots \\ & \vdots & \vdots & \vdots \end{array} \\ + \underbrace {0 0 0 0 0 0} _ {!} + \underbrace {0 0 0 0 0 0} _ {!} + \underbrace {0 0 0 0 0 0} _ {!} + \underbrace {0 0 0 0 0 0} _ {!} + \ldots \\ \end{array}
$$

Figure 3: (a) Graphical shorthand for the resummed gluon propagator, the bare gluon propagator dressed by an infinite sum of one loop quark loops. (b) Definition of the cut of the resummed gluon propagator, defined here for later convenience. Even though the cuts through gluon propagators on lines with massless quark loops are zero in dimensional regularization [57] we keep them explicit here for generality.

Employing Eq. (3.6) in evaluating the right panel of Fig. 2, completing $N _ { f }$ to the full beta function using Eq. (3.1), and using the definition of the running coupling, Eq. (3.3), we see that the

fixed couplings of diagram B in Fig. 1 squared are modified by loop corrections to

$$
\alpha_ {\mu} ^ {3} \rightarrow \frac {\alpha_ {\mu} ^ {3}}{\left[ 1 + \alpha_ {\mu} \beta_ {2} \ln \frac {q ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}} \right] ^ {2}} = \alpha_ {\mu} \alpha_ {s} ^ {2} \left(\boldsymbol {q} ^ {2} e ^ {- 5 / 3}\right). \tag {3.8}
$$

We clearly have a problem, since one of the factors of the coupling is still taken at some arbitrary renormalization scale $\mu$ . This problem cannot be mitigated simply by the inclusion of the corrections due to diagram A, as the above result is all one would obtain in QED for photon production (bremsstrahlung). It seems that the scale of the coupling is not fixed uniquely for the diagram in Fig. 2. As was shown in [46] the problem can be remedied if one redefines the observable: on top of the gluon production we should allow for the production of collinear gluongluon (GG) and quark–anti-quark $( q \bar { q } )$ pairs. This means that instead of calculating the diagram on the right-hand-side of Fig. 2, one has to calculate the graph pictured on the left of Fig. 4. As is shown in Fig. 3, the cut through the resummed gluon propagator in Fig. 4 includes the contribution from the square of diagram B in Fig. 1 and also cuts through both gluon propagators with the gluon line dressed with quark loops and cuts through the quark loops themselves. Even though the contribution from the cuts through gluon propagators with quark loop dressings are zero, as mentioned above, we will keep them explicit for the sake of generality (it will turn out that they are exactly canceled by a contribution from part of the cuts through the quark loops). Because of the redefined observable we are calculating, in addition to the gluon production resulting from the cuts through gluon propagators we now have to include the collinear $q q$ pair production from cuts through the quark loops. Since we are calculating quark loop corrections to sum up powers of $\alpha _ { \mu } N _ { f }$ , we do not need to explicitly include collinear gluon pair production in the calculation: it will be included when we complete $N _ { f }$ to the full beta-function. (Note that we are only interested in the terms with collinear singularities that contribute to the running of the coupling. Also note that – by the BLM prescription – by completing to the full beta-function we are including contributions from, e.g., the cut gluon loop, and therefore the running coupling contribution coming from collinear gluons.)

To sum the diagrams represented by the diagram on the left side of Fig. 4 we note that the sum of the cut diagrams can be written as the imaginary part of a dressed gluon propagator, as shown by the diagram on the right side of Fig. 4. The contribution of the dressed propagator is calculated using Eq. (3.6). Including the adjacent quark-gluon vertices one gets

$$
\begin{array}{l} \int \frac {d ^ {4} k}{(2 \pi) ^ {4}} 2 \mathrm {I m} \left[ i \frac {- i \alpha_ {\mu}}{(k ^ {2} + i \epsilon) [ 1 + \alpha_ {\mu} \beta_ {2} \ln \frac {- k ^ {2} - i \epsilon}{\mu^ {2}}} D _ {\mu \nu} (k) \right] = \\ \int \frac {d ^ {4} k}{(2 \pi) ^ {4}} 2 \mathrm {I m} \left[ \frac {\alpha_ {s} (- k ^ {2} e ^ {- 5 / 3} - i \epsilon)}{k ^ {2} + i \epsilon} D _ {\mu \nu} (k) \right], (3. 9) \\ \end{array}
$$

![](images/38629b937c806c45982066a5d586523e453435025a09281cb99a6667d3a826fd.jpg)  
Figure 4: Quark loop corrections to the diagram B in Fig. 1 for the calculation of the observable where one tags on both the gluons and collinear GG and $q q$ pairs. The left side of the equation indicates the cut diagrams to be summed. The right side of the equation explains a simple way of performing the summation (see text). The $k$ -line gluon propagator in the lower panel connects to the upper quark line as indicated by quark-gluon vertices at its ends, though this part of the diagram is separated from the rest for illustrative purposes.

where, according to the optical theorem, we took the imaginary part of the “forward amplitude” and multiplied it by 2. The factor of $i$ results from the $- i$ needed to convert $i M$ into the amplitude $M$ and from $i ^ { 2 } = - 1$ coming from the quark-gluon vertices. In the eikonal approximation used here the indices of the gluon propagator coupling to the upper quark line carrying a large “+” component of momentum are $\mu = \nu = +$ . However, we will keep the indices $\mu , \nu$ unspecified, as this will make our discussion more general. In arriving at Eq. (3.9) we have also completed $N _ { f }$ to the full beta function, which allowed us to replace the geometric series by a factor of the running coupling constant. Eq. (3.9) is illustrated on the right side of Fig. 4: it is a short hand way of taking the imaginary part of the whole diagram, keeping only the cuts going through the dressed gluon propagator with momentum $k$ .

Eq. (3.9) is still somewhat incomplete, since we need to specify what we mean by the collinear $q q$ pairs. To remedy this problem we write using the spectral representation (see [58,59] for a similar approach)

$$
\int \frac {d ^ {4} k}{(2 \pi) ^ {4}} = \int_ {- \infty} ^ {\infty} d k ^ {2} \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{2 k ^ {+} (2 \pi) ^ {4}} \Rightarrow \int_ {0} ^ {\Lambda_ {\mathrm {c o l l}} ^ {2}} d k ^ {2} \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{2 k ^ {+} (2 \pi) ^ {4}}, \tag {3.10}
$$

where $k ^ { 2 } = k _ { \mu } k ^ { \mu }$ is the virtuality of the gluon line. The last step of Eq. (3.10) completes the definition of our observable. By limiting the virtuality of the gluon line between 0 and some small momentum scale $\Lambda _ { \mathrm { c o l l } } ^ { 2 } > 0$ , we keep the diagrams with the gluon line in the final state (top line of Fig. 3 (b)) and limit the invariant mass of the produced $q q$ pair (bottom line of Fig. 3 (b)) to be smaller than $\Lambda _ { \mathrm { c o l l } } ^ { 2 }$ , which ensures the collinearity of the pair. (One can show that a small-virtuality

$q q$ pair with both quarks on-shell and massless necessarily has the two quarks collinear with each other.) $\Lambda _ { \mathrm { c o l l } }$ plays the role of the minimum momentum scale to be resolved by the “detector”. Below we will assume that $\Lambda _ { \mathrm { c o l l } }$ is much smaller than all the momentum scales involved in the problem, but is much larger than $\Lambda _ { Q C D }$ , such that perturbation theory remains applicable. Resummation of higher-order collinear emissions would likely lead to a Sudakov form-factor [60], reducing the dependence of the cross section on $\Lambda _ { \mathrm { c o l l } }$ . (A detailed discussion of the role of $\Lambda _ { \mathrm { c o l l } }$ can be found in [46], where it is argued that $\Lambda _ { \mathrm { c o l l } }$ plays the role of the factorization scale for the fragmentation functions.)

Using Eq. (3.10) in Eq. (3.9) yields

$$
\Delta_ {\mu \nu} \equiv \int_ {0} ^ {\Lambda_ {\mathrm {c o l l}} ^ {2}} d k ^ {2} \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{k ^ {+} (2 \pi) ^ {4}} \mathrm {I m} \left[ \frac {\alpha_ {s} (- k ^ {2} e ^ {- 5 / 3} - i \epsilon)}{k ^ {2} + i \epsilon} D _ {\mu \nu} (k) \right]. \qquad (3. 1 1)
$$

Since we assume that $\Lambda _ { \mathrm { c o l l } }$ is the smallest perturbative momentum scale in the problem, we are interested only in the terms which do not vanish in the $\Lambda _ { \mathrm { c o l l } } \  \ 0$ limit. Since the numerator of the gluon propagator $D _ { \mu \nu } ( k )$ is completely real and does not have any singularities at $k ^ { 2 } = 0$ (corresponding to the $\Lambda _ { \mathrm { c o l l } }  0$ limit), we can move $D _ { \mu \nu } ( k )$ outside the integral over gluon virtuality $k ^ { 2 }$ and outside the Im part sign. This modifies Eq. (3.11) into

$$
\Delta_ {\mu \nu} \approx \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{k ^ {+} (2 \pi) ^ {4}} D _ {\mu \nu} (k) \int_ {0} ^ {\Lambda_ {\mathrm {c o l l}} ^ {2}} d k ^ {2} \mathrm {I m} \left[ \frac {\alpha_ {s} (- k ^ {2} e ^ {- 5 / 3} - i \epsilon)}{k ^ {2} + i \epsilon} \right]. \tag {3.12}
$$

Extracting the imaginary part in Eq. (3.12) we obtain

$$
\Delta_ {\mu \nu} \approx \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{k ^ {+} (2 \pi) ^ {4}} D _ {\mu \nu} (k) \int_ {0} ^ {\Lambda_ {\mathrm {c o l l}} ^ {2}} d k ^ {2} \left[ - \pi \delta (k ^ {2}) \alpha_ {s} (0) + \frac {1}{k ^ {2}} \frac {\pi \beta_ {2} \alpha_ {\mu} ^ {2}}{\left(1 + \alpha_ {\mu} \beta_ {2} \ln \frac {k ^ {2}}{\mu^ {2}}\right) ^ {2} + \pi^ {2} \beta_ {2} ^ {2} \alpha_ {\mu} ^ {2}} \right] (3. 1 3)
$$

where for the moment we do not need to specify what we mean by $\alpha _ { s } ( 0 )$ . Integrating over $k ^ { 2 }$ in Eq. (3.13) yields

$$
\begin{array}{l} \Delta_ {\mu \nu} \approx \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{k ^ {+} (2 \pi) ^ {4}} D _ {\mu \nu} (k) \\ \times \left\{- \pi \alpha_ {s} (0) + \frac {1}{\beta_ {2}} \left[ \arctan \left(\frac {1}{\pi \beta_ {2} \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right)}\right) - \arctan \left(\frac {1}{\pi \beta_ {2} \alpha_ {s} (0)}\right) \right] \right\}. \tag {3.14} \\ \end{array}
$$

We see now that all the factors of $\alpha _ { \mu }$ got absorbed into running coupling constants at different momentum scales. However, since we are aiming to find the scale of one power of the coupling $\alpha _ { \mu }$ , we do not have control over higher powers of the coupling $\alpha _ { s }$ which enter (3.14). Therefore we need

to expand Eq. (3.14) to the lowest order in $\alpha _ { s }$ . This gives

$$
\Delta_ {\mu \nu} \approx \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{k ^ {+} (2 \pi) ^ {4}} D _ {\mu \nu} (k) (- \pi) \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) = \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \int \frac {d k ^ {+} d ^ {2} k _ {\perp}}{2 k ^ {+} (2 \pi) ^ {3}} \sum_ {\lambda} \epsilon_ {\mu} ^ {\lambda} (k) \epsilon_ {\nu} ^ {\lambda *} (k) \tag {3.15}
$$

with the polarization vector $\epsilon _ { \mu } ^ { \lambda }$ given by Eq. (2.4) and $^ *$ denoting complex conjugation. We see that in Eq. (3.15) we obtained all the standard factors for the outgoing gluon line, along with the running coupling constant $\alpha _ { s } \left( \Lambda _ { \mathrm { c o l l } } ^ { 2 } e ^ { - 5 / 3 } \right)$ . The kinematic factors and polarizations are the same as for the fixed coupling diagram B from Fig. 1 squared. We see that the scale of the remaining coupling constant in Eq. (3.8) has now been fixed and is given by $\Lambda _ { \mathrm { c o l l } } ^ { 2 } e ^ { - 5 / 3 }$ in the $\overline { { \mathrm { M } S } }$ renormalization scheme.2 (Note that the terms with $\alpha _ { s } ( 0 )$ from Eq. (3.14) got canceled in arriving at Eq. (3.15), thus relieving us of the need to properly define this quantity.)

Combining our result in (3.15) with (3.8) we see that the three fixed-coupling constants in the diagram in Fig. 1B squared become the following running couplings:

$$
\alpha_ {\mu} ^ {3} \rightarrow \alpha_ {s} \left(\Lambda_ {\text {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} ^ {2} \left(\boldsymbol {q} ^ {2} e ^ {- 5 / 3}\right). \tag {3.16}
$$

The above analysis can be repeated for the square of the diagram in Fig. 1C and for the cross term between diagrams B and C in Fig. 1, in each case leading to the same answer given by Eq. (3.16). We therefore conclude that Eq. (3.16) gives us the scales of the running couplings for the “bremsstrahlung diagrams” B and C in Fig. 1 taken by themselves, without the diagram A. We now will analyze the running coupling corrections to diagram A of Fig. 1.

# 3.2 Triple-Gluon Vertex Diagrams

Quark loop corrections to the triple-gluon vertex diagram from Fig. 1A squared are shown in Fig. 5. We now have to “dress” both the $q$ and $k - q$ gluon lines with quark bubbles. The outgoing gluon line also needs to be dressed like it was done in Fig. 4 for bremsstrahlung diagrams: again the cut can go either through the gluon line or through a quark loop. On top of that the triple gluon vertex may receive a quark bubble correction as well. Note that in principle the cut can go through the quark loop correction to the triple-gluon vertex. However, it is easy to show that that contribution does not have a singularity when the gluon virtuality is zero, $k ^ { 2 } = 0$ . Integration of the contribution from such a cut over $k ^ { 2 }$ from 0 to $\Lambda _ { \mathrm { c o l l } } ^ { 2 }$ would thus yield an expression proportional to $\Lambda _ { \mathrm { c o l l } } ^ { 2 }$ , which vanishes in the $\Lambda _ { \mathrm { c o l l } }  0$ limit. Since, just like for bremsstrahlung diagrams, we are interested in the contributions which do not vanish in the $\Lambda _ { \mathrm { c o l l } }  0$ limit, the cuts through the quark bubble at the triple gluon vertex can therefore be neglected. We see that for the outgoing gluon propagator

we have to sum over the same cuts as was done in Sec. 3.1 for the bremsstrahlung diagrams, as pictured in Fig. 4. Since our derivation of the result (3.16) of such a summation was valid for any values of the propagator indices $\mu$ and $\nu$ , the conclusion applies to the diagrams in Fig. 5 as well: the “dressing” of the outgoing gluon propagator along with the adjacent vertices gives us a factor of $\alpha _ { s } \left( \Lambda _ { \mathrm { c o l l } } ^ { 2 } e ^ { - 5 / 3 } \right)$ .

![](images/f7261dd927ef0c3e5efd20078d96cfd02f301917852d866c303284e201814315.jpg)  
Figure 5: Quark loop corrections to the square of diagram A from Fig. 1. The dot denotes the usual QCD triple-gluon vertex.

Concentrating on the top left diagram in Fig. 5 and using (3.6) along with (3.1) we see that quark loops lead to the following modification of the factors of coupling in it:

$$
\begin{array}{l} \alpha_ {\mu} ^ {3} \rightarrow \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \frac {\alpha_ {\mu} ^ {2}}{\left[ 1 + \alpha_ {\mu} \beta_ {2} \ln \frac {q ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}} \right] ^ {2} \left[ 1 + \alpha_ {\mu} \beta_ {2} \ln \frac {(k - q) ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}} \right] ^ {2}} \\ = \frac {\alpha_ {s} \left(\Lambda_ {\operatorname {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} ^ {2} \left(\boldsymbol {q} ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} ^ {2} \left((\boldsymbol {k} - \boldsymbol {q}) ^ {2} e ^ {- 5 / 3}\right)}{\alpha_ {\mu} ^ {2}}. \tag {3.17} \\ \end{array}
$$

Indeed, since we have analyzed only one diagram we have not fixed the scales of all the coupling constants. However, the expression in (3.17) is an overall factor, present in each of the diagrams in

Fig. 5. As was noted in [46] the effect of the quark loop corrections to the triple gluon vertex would be to generate factors of the type

$$
\left[ 1 + \alpha_ {\mu} \beta_ {2} \ln \frac {Q _ {A} ^ {2} e ^ {- 5 / 3}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {2}} \right] \left[ 1 + \alpha_ {\mu} \beta_ {2} \ln \frac {Q _ {B} ^ {2} e ^ {- 5 / 3}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {2}} \right] \tag {3.18}
$$

which, after multiplying Eq. (3.17), would turn $1 / \alpha _ { \mu } ^ { 2 }$ in it into $1 / \left\lfloor \alpha _ { s } ( Q _ { A } ^ { 2 } e ^ { - 5 / 3 } ) \alpha _ { s } ( Q _ { B } ^ { 2 } e ^ { - 5 / 3 } ) \right\rfloor$ with some physical momentum scales $Q _ { A }$ and $Q _ { B }$ to be determined by an explicit calculation.

Let us calculate the contribution of a quark-loop vertex correction to the diagram A from Fig. 1. The diagram with the one-loop correction is shown in Fig. 6. Considering the loop itself (in which we include only the quark propagators and quark-gluon vertices along the loop) and adding to it the contribution from the loop with the particle number in the loop flowing in the opposite direction we find

$$
\frac {i}{2} g ^ {3} f ^ {a b c} N _ {f} \int \frac {d ^ {d} l}{(2 \pi) ^ {d}} \frac {\mathrm {T r} [ \gamma^ {\mu} (\mathcal {X} + k ^ {\prime} - \mathcal {Q}) \gamma^ {\nu} \mathcal {X} \gamma^ {\rho} (\mathcal {X} - \mathcal {Q}) ]}{(l ^ {2} + i \epsilon) [ (l - q) ^ {2} + i \epsilon ] [ (l + k - q) ^ {2} + i \epsilon ]} \qquad (3. 1 9)
$$

where, in preparation for using dimensional regularization, we have switched to $d$ dimensions in the integral. Note that, as before, to simplify the algebra, we assume that all quarks in the loops are massless, since this assumption does not affect the scale of the running coupling.

Before we evaluate (3.19) let us make some simplifications due to the kinematics. The quarkgluon vertices at the top (carrying momentum $p _ { 1 }$ ) and at the bottom (carrying momentum $p _ { 2 }$ ) quark lines in Fig. 6 are eikonal: the dominant contribution to the vertex on the top comes with a Dirac matrix $\gamma ^ { + }$ , while the vertex at the bottom brings in $\gamma ^ { - }$ . Using these eikonal vertices along with Eqs. (2.1) and (2.2) we note that the propagator of the $k - q$ gluon line from Fig. 6 can be rewritten as

$$
\frac {- i}{(k - q) ^ {2}} D _ {\alpha \nu} (k - q) \rightarrow \frac {- i}{k ^ {+}} \frac {(k - q) _ {\nu} ^ {\perp}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}}. \tag {3.20}
$$

Therefore the $\nu$ index in Eq. (3.19) is only transverse, as indicated in Fig. 6. The propagator of the gluon line carrying momentum $q$ in Fig. 6 can be replaced by

$$
\frac {- i}{q ^ {2}} D _ {\beta \rho} (q) \rightarrow \frac {i}{q ^ {2}} g _ {\rho} ^ {+} \tag {3.21}
$$

making the $\rho$ -index in Eq. (3.19) equal to $+$ .

All the simplifications in Eqs. (2.1), (2.2), (3.20), and (3.21) are exactly the same as what is usually used in arriving at the fixed-coupling expression for the gluon production cross section (2.12). Since we are interested in corrections to the fixed-coupling result, we do not need to keep all the factors, since they are the same as for the running-coupling case, too: therefore, to simplify the algebra we multiply the expression in Eq. (3.19) only by $( k - q ) _ { \nu } ^ { \perp }$ from Eq. (3.20), $g _ { \rho } ^ { + }$ from

Eq. (3.21), and by $\epsilon _ { \mu } ^ { \lambda } ( k )$ from Eq. (2.4) for the outgoing gluon line in Fig. 6. This modifies Eq. (3.19) to

$$
\Gamma \equiv \frac {i}{2} g ^ {3} f ^ {a b c} N _ {f} \epsilon_ {\mu} ^ {\lambda} (k) (k - q) _ {\nu} ^ {\perp} \int \frac {d ^ {d} l}{(2 \pi) ^ {d}} \frac {\mathrm {T r} [ \gamma^ {\mu} (\mathcal {X} + k / - \mathcal {Q}) \gamma_ {\perp} ^ {\nu} \mathcal {X} \gamma^ {+} (\mathcal {X} - \mathcal {Q}) ]}{(l ^ {2} + i \epsilon) [ (l - q) ^ {2} + i \epsilon ] [ (l + k - q) ^ {2} + i \epsilon ]} \qquad (3. 2 2)
$$

The evaluation of the integral in Eq. (3.22) is carried out in the Appendix A with the answer given in Eqs. (A12), (A13), (A14), and (A11). In arriving at Eq. (A12) we have also added the $N _ { f }$ part of the triple-gluon vertex counterterm to remove the infinity in Eq. (3.22). We note that the tensor structure of the one-loop correction to the triple-gluon vertex is not limited to that of the lowest-order (LO) triple-gluon vertex, which, in fact, is well-known in the literature (see, e.g., [61, 62]). For diagram A in Fig. 1 the contribution of the triple-gluon vertex is given by Eq. (A9) and only leads to terms proportional to $\pmb { \epsilon } _ { \lambda } \cdot ( \pmb { k } - \pmb { q } )$ as can be seen from Eq. (A10). The full one-loop correction (A12) includes other tensor structures (see Eq. (A7)) leading to the appearance of $\epsilon _ { \lambda } \cdot k$ terms. Of course the ultraviolet (UV)-divergent part of the one-loop diagram does come in with the tensor structure of the lowestorder triple-gluon vertex (A9). However, in ac-

cordance with the BLM prescription, we need to collect all $\alpha _ { \mu } N _ { f }$ terms to set the scale of the coupling constants: therefore the UV-finite term coming with $\epsilon _ { \lambda } \cdot k$ in Eq. (A12) is also included.

Since the tensor structure of the LO triple-gluon vertex is modified, we see that the naive expectation for the quark loop correction to simply bring in overall factors like those shown in Eq. (3.18) into the square of the diagram in Fig. 5 is not correct. Instead we see that the square of diagram A in Fig. 1, which at the fixed-coupling order contributed

$$
\frac {d \sigma_ {A}}{d ^ {2} k _ {T} d y} = \frac {2 \alpha_ {s} ^ {3} C _ {F}}{\pi^ {2}} \int \frac {d ^ {2} q}{(q ^ {2}) ^ {2}} \sum_ {\lambda} \left| \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q})}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}} \right| ^ {2} \tag {3.23}
$$

to the gluon production cross section (see Eq. (2.12) above), with the help of Eqs. (3.17) and (A12)

![](images/f65a8153b1ec69c37c31d8a6d199657251b6a56ac42e7d41f965e893ef228dd4.jpg)  
Figure 6: One quark loop correction to the triple gluon vertex in diagram A from Fig. 1. The disconnected arrows denote momentum flow direction, while the arrow on the quark loop denotes the particle number flow. The diagram with the particle number flowing in the opposite direction should also be included.

gets modified to

$$
\begin{array}{l} \frac {d \sigma_ {A}}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \int \frac {d ^ {2} q}{(q ^ {2}) ^ {2}} \frac {\alpha_ {s} ^ {2} (q ^ {2} e ^ {- 5 / 3}) \alpha_ {s} ^ {2} ((\pmb {k} - \pmb {q}) ^ {2} e ^ {- 5 / 3})}{\alpha_ {\mu} ^ {2}} \\ \times \sum_ {\lambda} \left| \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}) (1 + \alpha_ {\mu} \beta_ {2} L _ {a}) - \boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k} \alpha_ {\mu} \beta_ {2} L _ {b}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}} \right| ^ {2}, \tag {3.24} \\ \end{array}
$$

where $L _ { a }$ and $L _ { b }$ are defined in Eq. (A13) and Eq. (A14), respectively. It is clear that Eq. (3.24) can be written in terms of the physical running-coupling constants, eliminating the $\mu$ -dependence completely. However, we will postpone this last step until the next Subsection, in which we will collect all the diagrams.

![](images/38807655870fd34139704a4575a778872c50e6967b660e5e3e46b8bdad05c6d5.jpg)  
Figure 7: Quark loop corrections to the interference terms between diagrams A and B from Fig. 1. The notation is the same as in Fig. 5.

Before we proceed, let us say a few words about the interference graphs between the triplegluon vertex diagram A and the bremsstrahlung diagrams B and C in Fig. 1. The quark loop corrections resumming powers of $\alpha _ { \mu } N _ { f }$ for such interference graphs are illustrated in Fig. 7. As was shown above in the discussion of the diagrams in Fig. 5, cuts through the quark loop correction to the triple-gluon vertex do not lead to collinearly-singular contributions (i.e. contributions that survive in the $\Lambda _ { \mathrm { c o l l } } ^ { 2 }  0$ limit) and should be discarded. Therefore the treatment of the quark loop corrections for the outgoing gluon propagator should be the same for the interference graphs in Fig. 7, as it was for diagram A squared in Fig. 5 and also for the diagrams B and C squared in Fig. 4: in each of the cases we obtain a factor of $\alpha _ { s } \left( \Lambda _ { \mathrm { c o l l } } ^ { 2 } e ^ { - 5 / 3 } \right)$ . The rest of the quark loop corrections is included at the amplitude level, as follows from the above analysis. For instance, the right-hand side of each graph in Fig. 7 would bring in $\alpha _ { s } \left( q ^ { 2 } e ^ { - 5 / 3 } \right)$ , while the left-hand side would give a contribution proportional to

$$
\frac {\alpha_ {s} (\boldsymbol {q} e ^ {- 5 / 3}) \alpha_ {s} ((\boldsymbol {k} - \boldsymbol {q}) ^ {2} e ^ {- 5 / 3})}{\alpha_ {\mu}} \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}) (1 + \alpha_ {\mu} \beta_ {2} L _ {a}) - \boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k} \alpha_ {\mu} \beta_ {2} L _ {b}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}} \tag {3.25}
$$

as can be inferred from the above discussion and from Eq. (3.24).

We are now ready to combine all the diagrams together to determine the scales of all the factors of the running coupling.

# 3.3 The Result

Adding the contributions of the “dressed” bremsstrahlung diagrams squared with the help of Eq. (3.16) to the “dressed” diagram A squared in Eq. (3.24), and including all the interference diagrams we finally write the expression for the gluon production cross section with the running coupling corrections included:

$$
\begin{array}{l} \frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \int \frac {d ^ {2} q}{(q ^ {2}) ^ {2}} \frac {\alpha_ {s} ^ {2} (q ^ {2} e ^ {- 5 / 3}) \alpha_ {s} ^ {2} ((\pmb {k} - \pmb {q}) ^ {2} e ^ {- 5 / 3})}{\alpha_ {\mu} ^ {2}} \\ \times \sum_ {\lambda} \left| \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}) (1 + \alpha_ {\mu} \beta_ {2} L _ {a}) - \boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k} \alpha_ {\mu} \beta_ {2} L _ {b}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}} - \frac {\boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k}}{\boldsymbol {k} ^ {2}} \left(1 + \alpha_ {\mu} \beta_ {2} \ln \frac {(\boldsymbol {k} - \boldsymbol {q}) ^ {2} e ^ {- 5 / 3}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {2}}\right) \right| ^ {2}, \tag {3.26} \\ \end{array}
$$

where, again, $L _ { a }$ and $L _ { b }$ are defined by Eq. (A13) and Eq. (A14), respectively. Equation (3.26) can be written more compactly as

$$
\begin{array}{l} \frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \int \frac {d ^ {2} q}{(q ^ {2}) ^ {2}} \frac {\alpha_ {s} ^ {2} (q ^ {2} e ^ {- 5 / 3})}{\alpha_ {\mu} ^ {2}} \frac {\alpha_ {s} ^ {2} ((\pmb {k} - \pmb {q}) ^ {2} e ^ {- 5 / 3})}{\alpha_ {\mu} ^ {2}} \\ \times \left[ \frac {\boldsymbol {k} - \boldsymbol {q}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}} \left(1 + \alpha_ {\mu} \beta_ {2} \ln \frac {Q _ {1} ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}}\right) - \frac {\boldsymbol {k}}{\boldsymbol {k} ^ {2}} \left(1 + \alpha_ {\mu} \beta_ {2} \ln \frac {Q _ {2} ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}}\right) \right] ^ {2} \tag {3.27} \\ \end{array}
$$

if we define momentum scales $Q _ { 1 }$ and $Q _ { 2 }$ by

$$
\ln \frac {Q _ {1} ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}} = \frac {\left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2} \ln \frac {\left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}} - \boldsymbol {q} ^ {2} \ln \frac {\boldsymbol {q} ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}}}{\left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2} - \boldsymbol {q} ^ {2}} - \frac {\boldsymbol {q} ^ {2} \left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2} \boldsymbol {k} ^ {2}}{\left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] ^ {3}} \ln \frac {\left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2}}{\boldsymbol {q} ^ {2}} + \frac {\boldsymbol {k} ^ {2} \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + \boldsymbol {q} ^ {2} \right]}{2 \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] ^ {2}} \tag {3.28}
$$

and

$$
\begin{array}{l} \ln \frac {Q _ {2} ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}} = \ln \frac {(\pmb {k} - \pmb {q}) ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}} + \frac {\pmb {k} ^ {2}}{(\pmb {k} - \pmb {q}) ^ {2}} \left[ \frac {\pmb {q} ^ {2} (\pmb {k} - \pmb {q}) ^ {2} [ \pmb {q} ^ {2} - (\pmb {k} - \pmb {q}) ^ {2} - 2 \pmb {k} ^ {2} ]}{2 [ (\pmb {k} - \pmb {q}) ^ {2} - \pmb {q} ^ {2} ] ^ {3}} \ln \frac {(\pmb {k} - \pmb {q}) ^ {2}}{\pmb {q} ^ {2}} \right] \\ \left. + \frac {\boldsymbol {q} ^ {2} \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] + \boldsymbol {k} ^ {2} \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + \boldsymbol {q} ^ {2} \right]}{2 \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] ^ {2}} \right]. \tag {3.29} \\ \end{array}
$$

We would like to point out that, as expected, the scales $Q _ { 1 }$ and $Q _ { 2 }$ are independent of $\mu _ { \mathrm { { M S } } }$ , as follows from Eqs. (3.28) and (3.29).

Recasting Eq. (3.27) in terms of physical running couplings we get

$$
\begin{array}{l} \frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right) \int \frac {d ^ {2} q}{(q ^ {2}) ^ {2}} \alpha_ {s} ^ {2} \left(q ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} ^ {2} \left((\pmb {k} - \pmb {q}) ^ {2} e ^ {- 5 / 3}\right) \\ \times \left[ \frac {\boldsymbol {k} - \boldsymbol {q}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2}} \frac {1}{\alpha_ {s} (Q _ {1} ^ {2} e ^ {- 5 / 3})} - \frac {\boldsymbol {k}}{\boldsymbol {k} ^ {2}} \frac {1}{\alpha_ {s} (Q _ {2} ^ {2} e ^ {- 5 / 3})} \right] ^ {2} \tag {3.30} \\ \end{array}
$$

which, together with Eqs. (3.28) and (3.29) can be considered the final answer for the gluon production cross-section with the running coupling corrections included. However, Eq. (3.30) is somewhat unsatisfactory. First, it does not explicitly exhibit the symmetry of the problem under the $\mathbf { \Delta } q  k - \mathbf { \Delta } q$ interchange. Such symmetry follows from the $+  -$ interchange symmetry of the high-energy scattering of identical hadrons/nuclei. We have broken this up-down symmetry in the diagrams by choosing the $A ^ { + } = 0$ gauge: however, the physical answer should be indeed independent of the gauge choice, and should be symmetric under $\pmb q  \pmb k - \pmb q$ . While Eq. (3.30) does posses such symmetry, it is not explicitly apparent in the form it is written. Second of all, Eq. (3.30) does not look like the fixed coupling cross-section (2.13) multiplied by the factors of running coupling, which is what one would expect from the procedure of setting the scales of the running coupling constants.

Both of these problems are remedied when, after considerable algebra, Eq. (3.30) can be recast into the following form:

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \frac {\alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right)}{\boldsymbol {k} ^ {2}} \int \frac {d ^ {2} q}{\boldsymbol {q} ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2}} \frac {\alpha_ {s} ^ {2} \left(\boldsymbol {q} ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} ^ {2} \left((\boldsymbol {k} - \boldsymbol {q}) ^ {2} e ^ {- 5 / 3}\right)}{\alpha_ {s} \left(Q ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} \left(Q ^ {* 2} e ^ {- 5 / 3}\right)} \tag {3.31}
$$

with the $\mu _ { \mathrm { { M S } } } ^ { }$ -independent momentum scale $Q$ defined by

$$
\begin{array}{l} \ln \frac {Q ^ {2}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {2}} = \frac {1}{2} \ln \frac {\boldsymbol {q} ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {4}} - \frac {1}{4 \boldsymbol {q} ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} ] ^ {6}} \left\{\boldsymbol {k} ^ {2} [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} ] ^ {3} \right. \\ \times \left\{\left[ \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} \right] ^ {2} - \left(\boldsymbol {q} ^ {2}\right) ^ {2} \right] \left[ \left(\boldsymbol {k} ^ {2}\right) ^ {2} + \left(\left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2} - \boldsymbol {q} ^ {2}\right) ^ {2} \right] + 2 \boldsymbol {k} ^ {2} \left[ \left(\boldsymbol {q} ^ {2}\right) ^ {3} - \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} \right] ^ {3} \right] \right. \\ \left. - \boldsymbol {q} ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} \left[ 2 (\boldsymbol {k} ^ {2}) ^ {2} + 3 [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} ] ^ {2} - 3 \boldsymbol {k} ^ {2} [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + \boldsymbol {q} ^ {2} ] \right] \ln \left(\frac {(\boldsymbol {k} - \boldsymbol {q}) ^ {2}}{\boldsymbol {q} ^ {2}}\right) \right\} \\ + i \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] ^ {3} \left\{\boldsymbol {k} ^ {2} \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] \left[ \boldsymbol {k} ^ {2} \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + \boldsymbol {q} ^ {2} \right] - \left(\boldsymbol {q} ^ {2}\right) ^ {2} - \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} \right] ^ {2} \right] \right. \\ \left. + \boldsymbol {q} ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} \left(\boldsymbol {k} ^ {2} \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + \boldsymbol {q} ^ {2} \right] - 2 (\boldsymbol {k} ^ {2}) ^ {2} - 2 \left[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} \right] ^ {2}\right) \ln \left(\frac {(\boldsymbol {k} - \boldsymbol {q}) ^ {2}}{\boldsymbol {q} ^ {2}}\right) \right\} \\ \left. \times \sqrt {2 q ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + 2 k ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + 2 q ^ {2} \boldsymbol {k} ^ {2} - (\boldsymbol {k} ^ {2}) ^ {2} - (\boldsymbol {q} ^ {2}) ^ {2} - [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} ] ^ {2}} \right\}. \tag {3.32} \\ \end{array}
$$

Note that the scale $Q ^ { 2 }$ is complex-valued! The expression under the square root in Eq. (3.32) is non-negative: therefore, to obtain the complex conjugate scale $Q ^ { * }$ from Eq. (3.32) one only needs to change the sign in front of the factor of $i$ in it. The cross-section (3.31) is, of course, real, as it contains a complex-valued coupling constant multiplied by its conjugate, $\alpha _ { s } \left( Q ^ { 2 } e ^ { - 5 / 3 } \right)$ $\alpha _ { s } \left( Q ^ { * 2 } e ^ { - 5 / 3 } \right)$ .

The scale $Q ^ { 2 }$ is explicitly symmetric under the $\mathbf { \Delta } q  k - \mathbf { \Delta } q$ interchange: therefore, the cross section (3.31) is also symmetric under $\mathbf { \Delta } q  k - \mathbf { \Delta } q$ , as expected from the symmetries of this high energy scattering problem. Also Eq. (3.31) clearly looks like the fixed-coupling cross-section (2.13) with three factors of fixed-coupling replaced by the seven running couplings: we will refer to this structure as the septumvirate of couplings.

Eq. (3.31), along with Eq. (3.32), are the main results of this work. They provide us with the gluon production cross section in high energy quark–quark scattering with the running coupling corrections included.

Let us point out one interesting feature of our result (3.31). It is well-known that the $\mathbf { \pmb q }$ -integral in Eq. (3.31) is dominated by regions where either $q \approx 0$ or $q \approx k$ [1, 2]. Due to the $\mathbf { \Delta } q  k - q$ symmetry each of these regions contributes equally, so we can concentrate on only one of them. Choosing the $q \approx 0$ region we see from Eq. (3.32) that in the $q \to 0$ limit

$$
\ln \frac {Q ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}} = \ln \frac {\boldsymbol {k} ^ {2}}{\mu_ {\mathrm {M S}} ^ {2}} + \frac {1}{2}. \tag {3.33}
$$

(In fact it is easier to see this by starting from Eqs. (3.28), (3.29), and (3.30).) Neglecting for simplicity numerical constants such as $e ^ { 5 / 3 }$ and 1/2 we approximate Eq. (3.31) by

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} \approx \frac {4 C _ {F}}{\pi} \frac {\alpha_ {s} (\Lambda_ {\mathrm {c o l l}} ^ {2})}{(k ^ {2}) ^ {2}} \int^ {k ^ {2}} \frac {d \pmb {q} ^ {2}}{\pmb {q} ^ {2}} \alpha_ {s} ^ {2} (\pmb {q} ^ {2}). \tag {3.34}
$$

The integral over $q ^ { \mathrm { 2 } }$ in Eq. (3.34) is cut off in the IR by the saturation scale in the case of hadron– hadron, hadron–nucleus, and nucleus–nucleus scattering. Eq. (3.34) demonstrates that, loosely speaking, the exact Eq. (3.31) can be interpreted as having only two powers of $\alpha _ { s }$ on top of $\alpha _ { s } \left( \Lambda _ { \mathrm { c o l l } } ^ { 2 } \right)$ , with the two factors of $\alpha _ { s }$ running at the smaller of the two scales $q ^ { 2 }$ and $( k - q ) ^ { 2 }$ .

Imagine that the quark–quark scattering considered here happens within a larger process of hadronic (or nuclear) scattering. After integrating over $q ^ { \cdot 2 }$ with the saturation scale $Q _ { s } ^ { 2 }$ as the IR cutoff, Eq. (3.34) becomes

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} \approx \frac {4 C _ {F}}{\pi} \frac {\alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2}\right) \alpha_ {s} (\boldsymbol {k} ^ {2}) \alpha_ {s} (Q _ {s} ^ {2})}{(\boldsymbol {k} ^ {2}) ^ {2}} \ln \frac {\boldsymbol {k} ^ {2}}{Q _ {s} ^ {2}}, \tag {3.35}
$$

which has a symmetric structure of one coupling running at the ‘gluon resolution scale’ $\Lambda _ { \mathrm { c o l l } } ^ { 2 }$ , another at the IR cutoff $Q _ { s } ^ { 2 }$ characterizing the distribution functions, and the third coupling running at the high transverse momentum scale $k ^ { 2 }$ .

# 4. Discussion

# 4.1 Conjecture for the Running Coupling Corrected $k _ { T }$ -Factorization Formula

Above in Eq. (3.31) we have calculated running coupling corrections to the lowest-order gluon production cross section in high-energy quark–quark scattering. Our result can be easily generalized to the case of nucleus–nucleus scattering in the McLerran–Venugopalan (MV) model, in which each nucleon in the nuclei is assumed to be made of valence quarks only. The generalization is accomplished by multiplying the right-hand side of Eq. (3.31) by $\left( N _ { c } A _ { 1 } \right) \left( N _ { c } A _ { 2 } \right)$ , with $A _ { 1 }$ and $A _ { 2 }$ the atomic numbers of the two nuclei. Such a generalization would only be valid for large momenta $k _ { \perp } = | \pmb { k } | \gg Q _ { s 1 } , Q _ { s 2 }$ where $Q _ { s 1 } , Q _ { s 2 }$ are the saturation scales of the two nuclei. In this regime non-linear saturation effects are not yet important and can be neglected.

It would be useful though to generalize our result (3.31) (i) beyond the MV model, i.e., to include small- $x$ evolution [4, 44, 45] in it and (ii) inside the saturation region, where the nonlinear effects are important [13–25]. Even for the fixed coupling constant result for the gluon production cross section including the small- $x$ evolution of [13–25] only exists for the case of proton–nucleus scattering, i.e., for the case when $Q _ { s } ^ { A } = Q _ { s 2 } \gg Q _ { s 1 } = Q _ { s } ^ { p }$ [38]; Eqs. (1.1), (1.2), and (1.3), which give the gluon production in proton-nucleus scattering, were shown to be valid in [38] only for $k _ { \perp } \gg Q _ { s } ^ { p }$ . Still it would be very useful to generalize Eqs. (1.1), (1.2), and (1.3) to include running coupling corrections.

To construct our conjecture for this generalization, let us start working in the framework of the MV model. The running-coupling corrections to the Glauber–Mueller formula [63], the forward amplitude of a $q q$ dipole on a nucleus in the MV model, was constructed in the Appendix of [46] and is given by Eq. (A8) there. Generalizing this result to the case of a $G G$ dipole scattering on a nucleus we write

$$
N _ {G} (\boldsymbol {r}, \boldsymbol {b}, y = 0) = 1 - \exp \left[ - \pi \alpha_ {s} \left(\frac {1}{\boldsymbol {r} ^ {2}}\right) \alpha_ {s} \left(\Lambda^ {2}\right) \rho T (\boldsymbol {b}) \boldsymbol {r} ^ {2} \ln \frac {1}{| \boldsymbol {r} | \Lambda} \right]. \tag {4.1}
$$

(Strictly speaking the BLM analysis used in [46] to obtain the quark dipole amplitude has to be modified for the gluon dipole: however, Eq. (4.1) is valid at least in the large- $N _ { c }$ limit when it could be obtained from Eq. (A8) of [46] with the help of Eq. (1.4) above.) The dipole amplitude given by the Glauber–Mueller formula is rapidity-independent [63] and serves as the initial condition for the subsequent BK/JIMWLK evolution: this is denoted by putting $y = 0$ in Eq. (4.1). Above, $\rho$ is the number density of nucleons in the nucleus and $T ( b )$ is the nuclear profile function equal to the length of the nuclear medium at the impact parameter $^ { b }$ , such that $T ( \pmb { b } ) = 2 \sqrt { R ^ { 2 } - b ^ { 2 } }$ for a spherical nucleus of radius $R$ . $\Lambda$ is some scale characterizing the nucleon, which, in general, is non-perturbative and is comparable to $\Lambda _ { Q C D }$ .

Eq. (4.1) is an approximation of a more exact expression [46]

$$
N _ {G} (\boldsymbol {r}, \boldsymbol {b}, y = 0) = 1 - \exp \left(- \frac {1}{2} \rho T (\boldsymbol {b}) \sigma^ {G G N} (\boldsymbol {r})\right) \tag {4.2}
$$

with $\sigma ^ { G G N } ( r )$ the cross-section of the gluon dipole scattering on a nucleon calculated at the twogluon exchange level with the running coupling corrections [46]

$$
\sigma^ {G G N} (\boldsymbol {r}) = \int \frac {d ^ {2} l _ {\perp}}{\left[ l ^ {2} \right] ^ {2}} \alpha_ {s} ^ {2} \left(l ^ {2} e ^ {- 5 / 3}\right) \left(2 - e ^ {i \boldsymbol {l} \cdot \boldsymbol {x}} - e ^ {- i \boldsymbol {l} \cdot \boldsymbol {x}}\right). \tag {4.3}
$$

$\Lambda$ is the IR cutoff for the $\iota$ -integral in Eq. (4.3). To construct the unintegrated gluon distribution at the lowest order we expand Eq. (4.2) to the lowest non-trivial order in $\sigma ^ { G G N }$ and use the result along with Eq. (4.3) in Eq. (1.2) to obtain

$$
\alpha_ {\mu} \phi_ {A} ^ {L O} (\pmb {k}, y = 0) = N _ {c} A \frac {\alpha_ {s} ^ {2} (\pmb {k} ^ {2} e ^ {- 5 / 3})}{\pi} \frac {1}{\pmb {k} ^ {2}}. (4. 4)
$$

In arriving at Eq. (4.4) we have, for simplicity, assumed that the nucleus is a cylinder of radius $R$ with the axis parallel to the beam direction and $T ( \pmb { b } ) = 2 R$ , such that we could replace $\rho T ( b ) $ $N _ { c } A / ( \pi R ^ { 2 } )$ with $A$ the atomic number of the nucleus.

Eq. (4.4) demonstrates one important point: it shows that the product $\alpha _ { \mu } \phi ( \pmb { k } , y )$ can be rewritten in terms of running couplings. It may be possible to define the unintegrated gluon distribution $\phi ( \pmb { k } , y )$ in such a way that it would be expressible in terms of running couplings all by itself. However, Eq. (3.31) appears to suggest that such a separation is not necessary, as it contains two powers of $\alpha _ { s } \left( q ^ { 2 } \right)$ which are likely to be absorbed into one distribution function and two powers of $\alpha _ { s } \left( ( \pmb { k } - \pmb { q } ) ^ { 2 } \right)$ which are likely to enter the other distribution function.

Defining

$$
\overline {{\phi}} (\boldsymbol {k}, y) = \alpha_ {s} \phi (\boldsymbol {k}, y) \tag {4.5}
$$

we use Eq. (4.4) to rewrite Eq. (3.31) (multiplied by $A N _ { c } ^ { 2 }$ for the $p A$ case) in the form of a generalization of Eq. (1.1):

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \frac {1}{\pmb {k} ^ {2}} \int d ^ {2} q \overline {{\phi}} _ {p} ^ {L O} (\pmb {q}, 0) \overline {{\phi}} _ {A} ^ {L O} (\pmb {k} - \pmb {q}, 0) \frac {\alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right)}{\alpha_ {s} \left(Q ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} \left(Q ^ {* 2} e ^ {- 5 / 3}\right)}. (4. 6)
$$

Again it seems natural that all factorized $\mathbf { \pmb { q } }$ -dependence enters one distribution function $\overline { { \phi } } _ { p } ^ { L O } ( \pmb { q } , 0 )$ , while all factorized $( k - q )$ -dependence enters the other distribution function $\overline { { \phi } } _ { A } ^ { L O } ( \pmb { k } - \pmb { q } , 0 )$ . The terms depending on momenta $\mathbf { \pmb q }$ and $k - q$ in a way that can not be factorized into separate $\pmb q$ - and $( k - q )$ -dependent parts are all included in the scale $Q$ , which generates a “vertex correction”.

Eq. (4.6) is still an exact result as long as all momenta involved are much larger than the saturation scale of the nucleus. However, inspired by this formula we would like to conjecture the following running-coupling generalization of Eq. (1.1):

$$
\frac {d \sigma}{d ^ {2} k _ {T} d y} = \frac {2 C _ {F}}{\pi^ {2}} \frac {1}{\pmb {k} ^ {2}} \int d ^ {2} q \overline {{\phi}} _ {p} (\pmb {q}, y) \overline {{\phi}} _ {A} (\pmb {k} - \pmb {q}, Y - y) \frac {\alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2} e ^ {- 5 / 3}\right)}{\alpha_ {s} \left(Q ^ {2} e ^ {- 5 / 3}\right) \alpha_ {s} \left(Q ^ {* 2} e ^ {- 5 / 3}\right)} \tag {4.7}
$$

with the distribution functions defined by

$$
\overline {{\phi}} _ {A} (\boldsymbol {k}, y) = \frac {C _ {F}}{(2 \pi) ^ {3}} \int d ^ {2} b d ^ {2} r e ^ {- i \boldsymbol {k} \cdot \boldsymbol {r}} \nabla_ {r} ^ {2} N _ {G} (\boldsymbol {r}, \boldsymbol {b}, y) \tag {4.8}
$$

and

$$
\overline {{\phi}} _ {p} (\boldsymbol {k}, y) = \frac {C _ {F}}{(2 \pi) ^ {3}} \int d ^ {2} b d ^ {2} r e ^ {- i \boldsymbol {k} \cdot \boldsymbol {r}} \nabla_ {r} ^ {2} n _ {G} (\boldsymbol {r}, \boldsymbol {b}, y). \tag {4.9}
$$

Here $N _ { G }$ should be found from the running-coupling BK/JIMWLK evolution [29, 30], while $n _ { G }$ should be obtained from the running coupling BFKL equation [31]. The scale $Q$ is given by Eq. (3.32). We hope that Eq. (4.7) is valid in the same regime as the original Eq. (1.1): it should be true both inside and outside the nuclear saturation region, with and without the non-linear small- $x$ evolution. Of course only exact calculations can prove or disprove the ansatz of Eq. (4.7).

Just like with the BK/JIMWLK nonlinear evolution equations, it is likely that even if Eq. (4.7) is valid, obtaining it may require a subtraction similar to the one done in [29, 30] for the runningcoupling BK and JIMWLK equations, possibly leading, in the end, to an additive UV-finite correction. However, similar to the case of BK/JIMWLK equations, it may be that for a choice of subtraction which preserves the linear evolution in the running-coupling part of the answer, the additive correction would be small [30, 32]. Since Eq. (4.7) is likely to correctly take into account all the linear running-coupling BFKL evolution, it may still be a good approximation for the exact answer, even if there is an additive correction to it.

# 4.2 Multiplicity per Unit Rapidity

Another interesting question to explore is the effect of our main result (3.31) on the integrated gluon multiplicity per unit rapidity $d N / d y$ . The latter is related to the hadronic multiplicity in $p p$ , $p A$ and $A A$ collisions, as was utilized in [35, 64–66]. Indeed to find $d N / d y$ one has to integrate Eq. (3.31) over all $\pmb { k }$ : at the same time Eq. (3.31) is only valid for $k _ { \perp } \gg Q _ { s }$ . However, we will use the trick which is valid for the fixed-coupling calculations at least in the quasi-classical limit of the MV model [67–69]: we will integrate (3.31) over $k _ { \perp }$ with the saturation scale $Q _ { s }$ providing the IR cutoff. The result would be proportional to the correct value of $d N / d y$ up to a constant. We have to note that the fact that this procedure gives the correct answer for $d N / d y$ (up to a constant) does not, in general, guarantee the same in the running coupling case. In this sense our calculation below should be treated as an approximation.

The integration of the exact Eq. (3.31) over $\pmb { k }$ appears to be rather daunting: instead we will use the approximate formula (3.34) and write

$$
\frac {d N}{d y} \approx 4 C _ {F} \frac {A ^ {2}}{S _ {\perp}} \alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2}\right) \int_ {Q _ {s} ^ {2}} ^ {\infty} \frac {d \boldsymbol {k} ^ {2}}{\left(\boldsymbol {k} ^ {2}\right) ^ {2}} \int_ {Q _ {s} ^ {2}} ^ {\boldsymbol {k} ^ {2}} \frac {d \boldsymbol {q} ^ {2}}{\boldsymbol {q} ^ {2}} \alpha_ {s} ^ {2} \left(\boldsymbol {q} ^ {2}\right). \tag {4.10}
$$

We assume that both nuclei are identical, each with atomic number $A$ : to generalize (3.34) to the case of $A A$ scattering we multiplied it by $A ^ { 2 }$ (for simplicity we left out the number of valence quarks in each nucleon, which would have given us an extra factor of $N _ { c } ^ { 2 }$ ). Here $S _ { \perp } = \pi R ^ { 2 }$ is the crosssectional area of the nucleus, which is again assumed to be cylindrical. Performing the integrals in Eq. (4.10) yields

$$
\frac {d N}{d y} \approx 4 C _ {F} S _ {\perp} \left(\frac {A}{S _ {\perp}}\right) ^ {2} \frac {\alpha_ {s} \left(\Lambda_ {\mathrm {c o l l}} ^ {2}\right) \alpha_ {s} ^ {2} \left(Q _ {s} ^ {2}\right)}{Q _ {s} ^ {2}}. \tag {4.11}
$$

To further evaluate Eq. (4.11), with the goal of determining the $A$ -dependence of $d N / d y$ , one has to define the saturation scale $Q _ { s }$ . We are working in the quasi-classical framework of the MV model. Therefore, the $A$ -dependence of $Q _ { s }$ that we are going to find is necessarily limited to the quasi-classical regime, and is going to be strongly modified by small- $x$ evolution with the running coupling corrections, as shown in [32,70,71]. Even within the classical approximation there appear to be two different ways of defining $Q _ { s }$ :

(i) Defining $Q _ { s }$ by requiring that the dipole amplitude (4.1) is of the order of one at $| r | = 1 / Q _ { s }$ , or, more precisely, that the exponent in Eq. (4.1) is equal to $- 1 / 4$ at $| r | = 1 / Q _ { s }$ , yields

$$
Q _ {s} ^ {2} = 4 \pi \alpha_ {s} \left(Q _ {s} ^ {2}\right) \alpha_ {s} \left(\Lambda^ {2}\right) \frac {A}{S _ {\perp}} \ln \frac {Q _ {s}}{\Lambda} \tag {4.12}
$$

where we again replaced $\rho T ( \pmb { b } )  A / S _ { \bot }$ . Using Eq. (4.12) we eliminate factors of $A / S _ { \perp }$ in Eq. (4.11) obtaining

$$
\frac {d N}{d y} \approx \frac {C _ {F}}{4 \pi^ {2}} S _ {\perp} \frac {Q _ {s} ^ {2}}{\ln^ {2} \frac {Q _ {s}}{\Lambda}} \frac {\alpha_ {s} (\Lambda_ {\mathrm {c o l l}} ^ {2})}{\alpha_ {s} ^ {2} (\Lambda^ {2})} \propto \frac {A}{\ln^ {2} A}. \tag {4.13}
$$

The proportionality follows from the assumption that for large enough $Q _ { s }$ we may neglect the differences between $\Lambda$ and $\Lambda _ { Q C D }$ in Eq. (4.12) and write $Q _ { s } ^ { 2 } \ \propto \ A ^ { 1 / 3 }$ . Identifying the number of participating nucleons $N _ { p a r t }$ with $A$ we see that the multiplicity per participant $( 1 / N _ { p a r t } ) d N / d y$ , in this naive model with cylindrical nuclei, is a decreasing function of $A$ . It seems that running coupling effects alone are not sufficient to describe RHIC heavy ion collision data on hadron multiplicity per participant along the lines of [66]. Other effects used in [66], like realistic nuclear profiles leading to two different saturation scales $Q _ { s } ^ { m a x }$ and $Q _ { s } ^ { m a n }$ for the two nuclei appear to be more important in describing the data (see [72, 73]).

(ii) Another, possibly less justified way of defining $Q _ { s }$ is to require that

$$
\bar {\phi} (| \boldsymbol {k} | = Q _ {s}, y) = \frac {S _ {\perp}}{(2 \pi) ^ {2}}. \tag {4.14}
$$

This is motivated by the saturation requirement for the unintegrated gluon distribution in the IR, though we have to point out that the distributions entering the $k _ { T } .$ -factorization formula

(1.1) given by Eqs. (1.2) and (1.3) in fact go to zero in the $k _ { T }  0$ limit [39, 40]. Eq. (4.14) gives

$$
Q _ {s} ^ {2} = 4 \pi \alpha_ {s} ^ {2} \left(Q _ {s} ^ {2}\right) \frac {A}{S _ {\perp}}, \tag {4.15}
$$

which, when used in Eq. (4.11) yields

$$
\frac {d N}{d y} \approx \frac {C _ {F}}{4 \pi^ {2}} S _ {\perp} \frac {Q _ {s} ^ {2}}{\alpha_ {s} ^ {2} (Q _ {s} ^ {2})} \alpha_ {s} (\Lambda_ {\mathrm {c o l l}} ^ {2}) \propto A. \tag {4.16}
$$

We see that in this scenario the particle multiplicity per participant does not change with centrality, reinforcing our earlier conclusion that running coupling corrections alone are not enough to describe the centrality dependence of the multiplicity per participant observed in heavy ion collisions at RHIC.

Indeed our above conclusions are limited to the quasi-classical regime and are derived under the assumption that Eq. (4.11), which gives us the multiplicity of particles with $k _ { \perp } > Q _ { s }$ , correctly describes the centrality-dependence of the total particle multiplicity. More detailed (possibly numerical) work is needed to derive the centrality dependence of the conjecture (4.7). Another way of including an $A$ dependence in Eqs. (4.13) and (4.16) is to identify $\Lambda _ { \mathrm { c o l l } }$ with $Q _ { s }$ (or make it proportional to some other power of $Q _ { s }$ ). However, it is not clear whether this is justified theoretically, since $Q _ { s }$ is clearly not the smallest momentum scale in the problem in the full non-linear regime. From the phenomenological side such a substitution would introduce an (extra) decrease of $( 1 / N _ { p a r t } ) d N / d y$ with $A$ in both Eqs. (4.13) and (4.16), making a successful comparison with RHIC data more difficult to achieve.

# 4.3 Summary

To summarize, in this paper we have found the running coupling corrections to the lowest order gluon production cross section in hadronic and nuclear high energy scattering. Our exact results are presented in Eqs. (3.31) and (3.32). An approximate simplified version of the exact formula is given in Eq. (3.35). Based on the results (3.31) and (3.32) we have conjectured the $k _ { T }$ -factorization formula for the gluon production cross section with running coupling corrections included, given in Eqs. (4.7), (4.8), and (4.9). We hope future work will verify our conjecture.

# Acknowledgments

Yu.K. is grateful to Genya Levin and Larry McLerran for discussions. Yu.K. would also like to thank the organizers of the workshop on High Energy Strong Interactions 2010 at the Yukawa Institute for Theoretical Physics, Kyoto, Japan, where part of this work was completed.

This research is sponsored in part by the U.S. Department of Energy under Grant No. DE-SC0004286.

# A. Loop integral evaluation

The goal of this Appendix is to evaluate the expression in Eq. (3.22). Following the standard procedure for evaluating loop integrals in dimensional regularization [56,57] we introduce Feynman parameters $x$ and $y$ and shift the integration variable by defining

$$
\tilde {l} ^ {\mu} = l ^ {\mu} - y q ^ {\mu} + x (k - q) ^ {\mu}. \tag {A1}
$$

After dropping the tilde we rewrite Eq. (3.22) as

$$
\begin{array}{l} \Gamma = i g ^ {3} f ^ {a b c} N _ {f} \epsilon_ {\mu} ^ {\lambda} (k) (k - q) _ {\nu} ^ {\perp} \int_ {0} ^ {1} d x \int_ {0} ^ {1 - x} d y \int \frac {d ^ {d} l}{(2 \pi) ^ {d}} \frac {\mathrm {T r} [ \gamma^ {\mu} \gamma^ {\alpha} \gamma_ {\perp} ^ {\nu} \gamma^ {\beta} \gamma^ {+} \gamma^ {\delta} ]}{[ l ^ {2} - (1 - x - y) (y q ^ {2} + x (k - q) ^ {2}) ] ^ {3}} \\ \times \left\{l _ {\alpha} l _ {\beta} \left[ - \bar {y} q _ {\delta} - x (k - q) _ {\delta} \right] + l _ {\alpha} l _ {\delta} \left[ y q _ {\beta} - x (k - q) _ {\beta} \right] + l _ {\beta} l _ {\delta} \left[ y q _ {\alpha} + \bar {x} (k - q) _ {\alpha} \right] \right. \\ + \left[ y q _ {\alpha} + \bar {x} (k - q) _ {\alpha} \right] \left[ y q _ {\beta} - x (k - q) _ {\beta} \right] \left[ - \bar {y} q _ {\delta} - x (k - q) _ {\delta} \right] \} \tag {A2} \\ \end{array}
$$

with

$$
\bar {x} = 1 - x, \quad \bar {y} = 1 - y \tag {A3}
$$

and $\alpha$ , $\beta$ , and $\delta$ some internal indices.

The first three terms in the curly brackets of Eq. (A2) are evaluated by substituting

$$
l _ {\alpha} l _ {\beta} \rightarrow \frac {1}{d} l ^ {2} g _ {\alpha \beta} \tag {A4}
$$

which makes the Dirac traces trivial. Denoting the contribution of these first three terms by $\Gamma _ { 3 }$ we perform the Wick rotation and integrate over $l$ to obtain

$$
\Gamma_ {3} = - g f ^ {a b c} k ^ {+} \boldsymbol {\epsilon} _ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}) \frac {\alpha_ {\mu} N _ {f}}{2 \pi} \int_ {0} ^ {1} d x (1 + x) \int_ {0} ^ {1 - x} d y \left\{\ln \left[ \frac {(1 - x - y) (y \boldsymbol {q} ^ {2} + x (\boldsymbol {k} - \boldsymbol {q}) ^ {2})}{\mu_ {\mathrm {M S}} ^ {2}} \right] + 1 \right\} \tag {A5}
$$

where we have added the $N _ { f }$ piece of the triple-gluon vertex counterterm in the $\overline { { \mathrm { M } S } }$ renormalization scheme. Integrating (A5) over $x$ and $y$ and completing $N _ { f }$ to the full beta-function using (3.1) yields

$$
\begin{array}{l} \Gamma_ {3} = 2 g f ^ {a b c} k ^ {+} \alpha_ {\mu} \beta_ {2} \epsilon_ {\lambda} \cdot (\pmb {k} - \pmb {q}) \left\{\frac {1}{1 2 [ (\pmb {k} - \pmb {q}) ^ {2} - \pmb {q} ^ {2} ] ^ {2}} \left[ (1 9 \pmb {q} ^ {2} - 1 6 (\pmb {k} - \pmb {q}) ^ {2}) ((\pmb {k} - \pmb {q}) ^ {2} - \pmb {q} ^ {2}) \right] \right. \\ \left. + 3 \left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2} \left(4 \left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2} - 5 \boldsymbol {q} ^ {2}\right) \ln \frac {\left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {2}} + 3 \boldsymbol {q} ^ {2} \left(4 \boldsymbol {q} ^ {2} - 3 \left(\boldsymbol {k} - \boldsymbol {q}\right) ^ {2}\right) \ln \frac {\boldsymbol {q} ^ {2}}{\mu_ {\overline {{\mathrm {M S}}}} ^ {2}} \right] - \frac {7}{1 2} \Bigg \}. \tag {A6} \\ \end{array}
$$

We now turn our attention to the last term in the curly brackets of Eq. (A2). We denote the contribution of this term by $\Gamma _ { 4 }$ . Wick rotation, integration over $l$ , and evaluation of the trace of Dirac matrices, after somewhat convoluted algebra, gives

$$
\begin{array}{l} \Gamma_ {4} = g f ^ {a b c} k ^ {+} \epsilon_ {\mu} ^ {\lambda} (k) (k - q) _ {\nu} ^ {\perp} \frac {\alpha_ {\mu} N _ {f}}{2 \pi} \int_ {0} ^ {1} d x \int_ {0} ^ {1 - x} d y \frac {1}{y q ^ {2} + x (k - q) ^ {2}} \\ \times \left\{g ^ {\mu \nu} \left[ x ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + y (1 + x) \boldsymbol {q} ^ {2} \right] - 2 x (1 - 2 x - 2 y) q ^ {\mu} q _ {\perp} ^ {\nu} + 2 x (1 - 2 x) q ^ {\mu} k _ {\perp} ^ {\nu} \right\}. \tag {A7} \\ \end{array}
$$

Integrating over $x$ and $y$ in (A7), replacing $N _ { f }$ with the help of (3.1), and bringing $\epsilon _ { \mu } ^ { \lambda } ( k ) ( k - q ) _ { \nu } ^ { \perp }$ inside the curly brackets we obtain

$$
\begin{array}{l} \Gamma_ {4} = 2 g f ^ {a b c} k ^ {+} \alpha_ {\mu} \beta_ {2} \left\{\pmb {\epsilon} _ {\lambda} \cdot (\pmb {k} - \pmb {q}) \left[ \frac {3 (\pmb {k} - \pmb {q}) ^ {2} (\pmb {q} ^ {2} - (\pmb {k} - \pmb {q}) ^ {2} + \pmb {q} ^ {2} \ln \frac {(\pmb {k} - \pmb {q}) ^ {2}}{q ^ {2}})}{4 [ (\pmb {k} - \pmb {q}) ^ {2} - q ^ {2} ] ^ {2}} + 1 \right] \right. \\ + \epsilon_ {\lambda} \cdot q (k - q) \cdot q \frac {q ^ {2} - (k - q) ^ {2} + q ^ {2} \ln \frac {(k - q) ^ {2}}{q ^ {2}}}{2 [ (k - q) ^ {2} - q ^ {2} ] ^ {2}} \\ \end{array}
$$

$$
\left. - \epsilon_ {\lambda} \cdot q (k - q) \cdot k \frac {[ (k - q) ^ {2} - q ^ {2} ] [ (k - q) ^ {2} + 3 q ^ {2} ] - q ^ {2} [ 3 (k - q) ^ {2} + q ^ {2} ] \ln \frac {(k - q) ^ {2}}{q ^ {2}}}{2 [ (k - q) ^ {2} - q ^ {2} ] ^ {3}} \right\}. \tag {A8}
$$

In order to more efficiently combine Eqs. (A6) and (A8) we note that the triple gluon vertex in the leading-order diagram A in Fig. 1 contributes

$$
- 2 g f ^ {a b c} k ^ {+} g ^ {\mu \nu} \tag {A9}
$$

such that, when multiplied by $\epsilon _ { \mu } ^ { \lambda } ( k ) ( k - q ) _ { \nu } ^ { \perp }$ , it becomes

$$
2 g f ^ {a b c} k ^ {+} \epsilon_ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}). \tag {A10}
$$

Therefore, defining

$$
\Gamma_ {\mathrm {L O}} = 2 g f ^ {a b c} k ^ {+} \tag {A11}
$$

we finally write for $\mathrm { \Delta I ^ { \prime } = I _ { 3 } ^ { \prime } + I _ { 4 } ^ { \prime } }$

$$
\Gamma = \Gamma_ {\mathrm {L O}} \alpha_ {\mu} \beta_ {2} \left\{\boldsymbol {\epsilon} _ {\lambda} \cdot (\boldsymbol {k} - \boldsymbol {q}) L _ {a} - \boldsymbol {\epsilon} _ {\lambda} \cdot \boldsymbol {k} L _ {b} \right\}, \tag {A12}
$$

where we define

$$
L _ {a} \equiv \frac {(\boldsymbol {k} - \boldsymbol {q}) ^ {2} \ln \frac {(\boldsymbol {k} - \boldsymbol {q}) ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}} - \boldsymbol {q} ^ {2} \ln \frac {\boldsymbol {q} ^ {2} e ^ {- 5 / 3}}{\mu_ {\mathrm {M S}} ^ {2}}}{(\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2}} - \frac {\boldsymbol {q} ^ {2} (\boldsymbol {k} - \boldsymbol {q}) ^ {2} \boldsymbol {k} ^ {2}}{[ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} ] ^ {3}} \ln \frac {(\boldsymbol {k} - \boldsymbol {q}) ^ {2}}{\boldsymbol {q} ^ {2}} + \frac {\boldsymbol {k} ^ {2} [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} + \boldsymbol {q} ^ {2} ]}{2 [ (\boldsymbol {k} - \boldsymbol {q}) ^ {2} - \boldsymbol {q} ^ {2} ] ^ {2}} (A 1 3)
$$

and

$$
L _ {b} \equiv \frac {\mathbf {q} ^ {2} (\mathbf {k} - \mathbf {q}) ^ {2} [ \mathbf {q} ^ {2} - (\mathbf {k} - \mathbf {q}) ^ {2} - 2 \mathbf {k} ^ {2} ]}{2 [ (\mathbf {k} - \mathbf {q}) ^ {2} - \mathbf {q} ^ {2} ] ^ {3}} \ln \frac {(\mathbf {k} - \mathbf {q}) ^ {2}}{\mathbf {q} ^ {2}} + \frac {\mathbf {q} ^ {2} [ (\mathbf {k} - \mathbf {q}) ^ {2} - \mathbf {q} ^ {2} ] + \mathbf {k} ^ {2} [ (\mathbf {k} - \mathbf {q}) ^ {2} + \mathbf {q} ^ {2} ]}{2 [ (\mathbf {k} - \mathbf {q}) ^ {2} - \mathbf {q} ^ {2} ] ^ {2}}. \tag {A14}
$$

Note that the first term on the right-hand side of Eq. (A13) is formally similar to what was obtained for the kernel of the running-coupling BK/JIMWLK evolution equations (see Eq. (86) in [29]). However the similarity does not extend beyond this term.

# References

[1] L. V. Gribov, E. M. Levin, and M. G. Ryskin, Semihard Processes in QCD, Phys. Rept. 100 (1983) 1–150.   
[2] J. P. Blaizot and A. H. Mueller, The Early Stage of Ultrarelativistic Heavy Ion Collisions, Nucl. Phys. B289 (1987) 847.   
[3] A. H. Mueller and J.-w. Qiu, Gluon recombination and shadowing at small values of x, Nucl. Phys. B268 (1986) 427.   
[4] A. H. Mueller, Soft gluons in the infinite momentum wave function and the BFKL pomeron, Nucl. Phys. B415 (1994) 373–385.   
[5] A. H. Mueller and B. Patel, Single and double BFKL pomeron exchange and a dipole picture of high-energy hard processes, Nucl. Phys. B425 (1994) 471–488, [hep-ph/9403256].   
[6] A. H. Mueller, Unitarity and the BFKL pomeron, Nucl. Phys. B437 (1995) 107–126, [hep-ph/9408245].   
[7] L. D. McLerran and R. Venugopalan, Gluon distribution functions for very large nuclei at small transverse momentum, Phys. Rev. D49 (1994) 3352–3355, [hep-ph/9311205].   
[8] L. D. McLerran and R. Venugopalan, Computing quark and gluon distribution functions for very large nuclei, Phys. Rev. D49 (1994) 2233–2241, [hep-ph/9309289].   
[9] L. D. McLerran and R. Venugopalan, Green’s functions in the color field of a large nucleus, Phys. Rev. D50 (1994) 2225–2233, [hep-ph/9402335].   
[10] Y. V. Kovchegov, Non-abelian Weizsaecker-Williams field and a two- dimensional effective color charge density for a very large nucleus, Phys. Rev. D54 (1996) 5463–5469, [hep-ph/9605446].   
[11] Y. V. Kovchegov, Quantum structure of the non-abelian Weizsaecker-Williams field for a very large nucleus, Phys. Rev. D55 (1997) 5445–5455, [hep-ph/9701229].

[12] J. Jalilian-Marian, A. Kovner, L. D. McLerran, and H. Weigert, The intrinsic glue distribution at very small x, Phys. Rev. D55 (1997) 5414–5428, [hep-ph/9606337].   
[13] J. Jalilian-Marian, A. Kovner, A. Leonidov, and H. Weigert, The BFKL equation from the Wilson renormalization group, Nucl. Phys. B504 (1997) 415–431, [hep-ph/9701284].   
[14] J. Jalilian-Marian, A. Kovner, A. Leonidov, and H. Weigert, The Wilson renormalization group for low x physics: Towards the high density regime, Phys. Rev. D59 (1998) 014014, [hep-ph/9706377].   
[15] J. Jalilian-Marian, A. Kovner, and H. Weigert, The Wilson renormalization group for low x physics: Gluon evolution at finite parton density, Phys. Rev. D59 (1998) 014015, [hep-ph/9709432].   
[16] J. Jalilian-Marian, A. Kovner, A. Leonidov, and H. Weigert, Unitarization of gluon distribution in the doubly logarithmic regime at high density, Phys. Rev. D59 (1999) 034007, [hep-ph/9807462].   
[17] A. Kovner, J. G. Milhano, and H. Weigert, Relating different approaches to nonlinear QCD evolution at finite gluon density, Phys. Rev. D62 (2000) 114005, [hep-ph/0004014].   
[18] H. Weigert, Unitarity at small Bjorken x, Nucl. Phys. A703 (2002) 823–860, [hep-ph/0004044].   
[19] E. Iancu, A. Leonidov, and L. D. McLerran, Nonlinear gluon evolution in the color glass condensate. I, Nucl. Phys. A692 (2001) 583–645, [hep-ph/0011241].   
[20] E. Ferreiro, E. Iancu, A. Leonidov, and L. McLerran, Nonlinear gluon evolution in the color glass condensate. II, Nucl. Phys. A703 (2002) 489–538, [hep-ph/0109115].   
[21] Y. V. Kovchegov, Small-x $F _ { 2 }$ structure function of a nucleus including multiple pomeron exchanges, Phys. Rev. D60 (1999) 034008, [hep-ph/9901281].   
[22] Y. V. Kovchegov, Unitarization of the BFKL pomeron on a nucleus, Phys. Rev. D61 (2000) 074018, [hep-ph/9905214].   
[23] I. Balitsky, Operator expansion for high-energy scattering, Nucl. Phys. B463 (1996) 99–160, [hep-ph/9509348].   
[24] I. Balitsky, Operator expansion for diffractive high-energy scattering, hep-ph/9706411.   
[25] I. Balitsky, Factorization and high-energy effective action, Phys. Rev. D60 (1999) 014020, [hep-ph/9812311].   
[26] E. Iancu and R. Venugopalan, The color glass condensate and high energy scattering in QCD, hep-ph/0303204.   
[27] H. Weigert, Evolution at small $x _ { b j }$ : The Color Glass Condensate, Prog. Part. Nucl. Phys. 55 (2005) 461–565, [hep-ph/0501087].   
[28] J. Jalilian-Marian and Y. V. Kovchegov, Saturation physics and deuteron gold collisions at RHIC, Prog. Part. Nucl. Phys. 56 (2006) 104–231, [hep-ph/0505052].

[29] Y. Kovchegov and H. Weigert, Triumvirate of Running Couplings in Small-x Evolution, Nucl. Phys. A 784 (2007) 188–226, [hep-ph/0609090].   
[30] I. I. Balitsky, Quark Contribution to the Small-x Evolution of Color Dipole, Phys. Rev. D 75 (2007) 014001, [hep-ph/0609105].   
[31] Y. V. Kovchegov and H. Weigert, Quark loop contribution to BFKL evolution: Running coupling and leading-N(f) NLO intercept, Nucl. Phys. A789 (2007) 260–284, [hep-ph/0612071].   
[32] J. L. Albacete and Y. V. Kovchegov, Solving high energy evolution equation including running coupling corrections, Phys. Rev. D75 (2007) 125021, [0704.0612].   
[33] M. A. Braun, Reggeized gluons with a running coupling constant, Phys. Lett. B348 (1995) 190–195, [hep-ph/9408261].   
[34] E. Levin, Renormalons at low x, Nucl. Phys. B453 (1995) 303–333, [hep-ph/9412345].   
[35] J. L. Albacete, Particle multiplicities in Lead-Lead collisions at the LHC from non-linear evolution with running coupling, Phys. Rev. Lett. 99 (2007) 262301, [arXiv:0707.2545].   
[36] J. L. Albacete, N. Armesto, J. G. Milhano, and C. A. Salgado, Non-linear QCD meets data: A global analysis of lepton- proton scattering with running coupling BK evolution, Phys. Rev. D80 (2009) 034031, [arXiv:0902.1112].   
[37] K. Kutak and A. M. Stasto, Unintegrated gluon distribution from modified BK equation, Eur. Phys. J. C41 (2005) 343–351, [hep-ph/0408117].   
[38] Y. V. Kovchegov and K. Tuchin, Inclusive gluon production in dis at high parton density, Phys. Rev. D65 (2002) 074026, [hep-ph/0111362].   
[39] M. A. Braun, Inclusive jet production on the nucleus in the perturbative QCD with $N ( c )  \infty$ , Phys. Lett. B483 (2000) 105–114, [hep-ph/0003003].   
[40] D. Kharzeev, Y. V. Kovchegov, and K. Tuchin, Cronin effect and high-p(t) suppression in p a collisions, Phys. Rev. D68 (2003) 094013, [hep-ph/0307037].   
[41] Y. V. Kovchegov and A. H. Mueller, Gluon production in current nucleus and nucleon nucleus collisions in a quasi-classical approximation, Nucl. Phys. B529 (1998) 451–479, [hep-ph/9802440].   
[42] A. Kovner and M. Lublinsky, One gluon, two gluon: Multigluon production via high energy evolution, JHEP 11 (2006) 083, [hep-ph/0609227].   
[43] Y. V. Kovchegov, J. Kuokkanen, K. Rummukainen, and H. Weigert, Subleading-Nc corrections in non-linear small-x evolution, Nucl. Phys. A823 (2009) 47–82, [arXiv:0812.3238].   
[44] Y. Y. Balitsky and L. N. Lipatov Sov. J. Nucl. Phys. 28 (1978) 822.

[45] E. A. Kuraev, L. N. Lipatov, and V. S. Fadin, The Pomeranchuk singularity in non-Abelian gauge theories, Sov. Phys. JETP 45 (1977) 199–204.   
[46] Y. V. Kovchegov and H. Weigert, Collinear Singularities and Running Coupling Corrections to Gluon Production in CGC, Nucl. Phys. A807 (2008) 158–189, [arXiv:0712.3732].   
[47] S. Catani, M. Ciafaloni, and F. Hautmann, High-energy factorization and small x heavy flavor production, Nucl. Phys. B366 (1991) 135–188.   
[48] J. C. Collins and R. K. Ellis, Heavy quark production in very high-energy hadron collisions, Nucl. Phys. B360 (1991) 3–30.   
[49] E. M. Levin, M. G. Ryskin, Y. M. Shabelski, and A. G. Shuvaev, Heavy quark production in parton model and in QCD, Sov. J. Nucl. Phys. 54 (1991) 867–871.   
[50] E. A. Kuraev, L. N. Lipatov, and V. S. Fadin, Multi - reggeon processes in the yang-mills theory, Sov. Phys. JETP 44 (1976) 443–450.   
[51] Y. V. Kovchegov and D. H. Rischke, Classical gluon radiation in ultrarelativistic nucleus nucleus collisions, Phys. Rev. C56 (1997) 1084–1094, [hep-ph/9704201].   
[52] A. Kovner, L. D. McLerran, and H. Weigert, Gluon production at high transverse momentum in the McLerran-Venugopalan model of nuclear structure functions, Phys. Rev. D52 (1995) 3809–3814, [hep-ph/9505320].   
[53] A. Kovner, L. D. McLerran, and H. Weigert, Gluon production from nonAbelian Weizsacker-Williams fields in nucleus-nucleus collisions, Phys. Rev. D52 (1995) 6231–6237, [hep-ph/9502289].   
[54] S. J. Brodsky, G. P. Lepage, and P. B. Mackenzie, On the elimination of scale ambiguities in perturbative quantum chromodynamics, Phys. Rev. D28 (1983) 228.   
[55] J. R. Forshaw and D. A. Ross, Quantum chromodynamics and the pomeron. Cambridge University Press, 2004.   
[56] M. E. Peskin and D. V. Schroeder, An Introduction to quantum field theory. Addison-Wesley, Reading, USA, 1995.   
[57] G. Sterman, An Introduction to quantum field theory. Cambridge University Press, Cambridge, UK, 1993.   
[58] Y. L. Dokshitzer, D. Diakonov, and S. I. Troian, Hard Processes in Quantum Chromodynamics, Phys. Rept. 58 (1980) 269–395.   
[59] Y. L. Dokshitzer and D. V. Shirkov, On exact account of heavy quark thresholds in hard processes, Z. Phys. C67 (1995) 449–458.

[60] V. V. Sudakov, Vertex parts at very high-energies in quantum electrodynamics, Sov. Phys. JETP 3 (1956) 65–71.   
[61] J. S. Ball and T.-W. Chiu, Analytic properties of the vertex function in gauge theories. 2, Phys. Rev. D22 (1980) 2550.   
[62] A. I. Davydychev, P. Osland, and L. Saks, Quark mass dependence of the one-loop three-gluon vertex in arbitrary dimension, JHEP 08 (2001) 050, [hep-ph/0105072].   
[63] A. H. Mueller, Small x Behavior and Parton Saturation: A QCD Model, Nucl. Phys. B335 (1990) 115.   
[64] D. Kharzeev and M. Nardi, Hadron production in nuclear collisions at RHIC and high density QCD, Phys. Lett. B507 (2001) 121–128, [nucl-th/0012025].   
[65] D. Kharzeev and E. Levin, Manifestations of high density QCD in the first RHIC data, Phys. Lett. B523 (2001) 79–87, [nucl-th/0108006].   
[66] D. Kharzeev, E. Levin, and M. Nardi, The onset of classical QCD dynamics in relativistic heavy ion collisions, Phys. Rev. C71 (2005) 054903, [hep-ph/0111315].   
[67] T. Lappi, Wilson line correlator in the MV model: relating the glasma to deep inelastic scattering, Eur. Phys. J. C55 (2008) 285–292, [arXiv:0711.3039].   
[68] J. P. Blaizot, T. Lappi, and Y. Mehtar-Tani, On the gluon spectrum in the glasma, Nucl. Phys. A846 (2010) 63–82, [arXiv:1005.0955].   
[69] Y. V. Kovchegov, Classical initial conditions for ultrarelativistic heavy ion collisions, Nucl. Phys. A692 (2001) 557–582, [hep-ph/0011252].   
[70] A. H. Mueller, Nuclear A-dependence near the saturation boundary, hep-ph/0301109.   
[71] J. L. Albacete, N. Armesto, J. G. Milhano, C. A. Salgado, and U. A. Wiedemann, Numerical analysis of the Balitsky-Kovchegov equation with running coupling: Dependence of the saturation scale on nuclear size and rapidity, Phys. Rev. D71 (2005) 014003, [hep-ph/0408216].   
[72] H.-J. Drescher, A. Dumitru, A. Hayashigaki, and Y. Nara, The eccentricity in heavy-ion collisions from color glass condensate initial conditions, Phys. Rev. C74 (2006) 044905, [nucl-th/0605012].   
[73] A. Kuhlman, U. W. Heinz, and Y. V. Kovchegov, Gluon saturation effects in relativistic $U + U$ collisions, Phys. Lett. B638 (2006) 171–177, [nucl-th/0604038].