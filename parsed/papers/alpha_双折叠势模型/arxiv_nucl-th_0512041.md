# Predictions of $\alpha$ -decay half-lives based on potentials from self-consistent mean-field models

Z. A. Dupr´e $^ { \mathrm { a , b } }$ T. J. B¨urvenich a,c

aTheoretical Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA   
bDepartment of Physics and Astronomy, Louisiana State University, Baton Rouge, LS 70803-4001, USA   
cFrankfurt Institute for Advanced Studies, Johann Wolfgang Goethe University, Max-von-Laue-Str. 1, 60438 Frankfurt am Main, Germany

# Abstract

We present a microscopic model for the calculation of $\alpha$ -decay half lives employing potentials obtained from relativistic and non-relativistic self-consistent mean-field models. The nuclear and Coulomb potentials are used to obtain the tunneling probability and, in one model variant, also the knocking frequency. The model contains only one parameter. We compare this approach employing several modern meanfield parametrizations to experimental data and to the semi-empirical Viola-Seaborg systematics. We extrapolate our model to superheavy nuclei where assumptions entering semi-empirical approaches might lose validity.

Key words: alpha decay, relativistic mean-field model, Skyrme-Hartree-Fock, finite nuclei, Viola-Seaborg systematics

PACS: 21.10.Tg, 21.60.Jz, 23.60.+e, 24.10.Jv

# 1 Introduction

Alpha decay was experimentally studied by Rutherford just before the beginning of the 20th century and constitutes a beautiful example of quantum mechanical tunneling through a (classically impenetrable) barrier. The $\alpha$ -particle or helium nucleus, which is formed within the mother nucleus, tunnels through the Coulomb barrier created by the protons. In 1928, after the advent of quantum mechanics, Gamow proposed a semi-classical interpretation for $\alpha$ -decay

[1]. His model implied that the $\alpha$ -decay constant $\lambda$ can be written as a product of three factors: the probability $f$ that an alpha particle is formed inside the nucleus (pre-formation factor), the frequency $\nu$ at which the alpha particle knocks against the nucleus’s potential well (knocking frequency), and the probability $P$ with which the particle is able to tunnel through the barrier (Gamov factor), leaving behind the $\left( Z - 2 , N - 2 \right)$ daughter nucleus. Thus, in this model the $\alpha$ decay constant is given by

$$
\lambda = f \times \nu \times P \tag {1}
$$

We note that this approach assumes the statistical independence of these three processes.

The probability of transmission through the barrier, $P = e ^ { \tau }$ , can be determined by calculating semi-classically in the WKB approximation [2]

$$
\tau = - 2 \int_ {r _ {1}} ^ {r _ {2}} \sqrt {\frac {2 \mu [ V (r) - E ]}{\hbar^ {2}}} d r \tag {2}
$$

The knocking frequency $\nu$ is given by [3]

$$
\nu^ {- 1} = 2 \int_ {0} ^ {r _ {1}} \sqrt {\frac {\mu}{2 [ E - V (r) ]}} d r, \tag {3}
$$

which, for a constant nuclear potential $V$ , reduces to $v / 2 R$ , i.e., the number of times a particle with velocity $\boldsymbol { v }$ (determined from its energy $E$ ) goes back and forth in a confined space of size $2 R$ . In these formulas, $\mu$ is the reduced mass of the daughter-alpha particle system, and $r _ { 1 }$ and $r _ { 2 }$ are the points where the energy of the alpha particle is equal to the potential, $r _ { 1 }$ is the inner, $r _ { 2 }$ is the outer turning point, respectively.

Eq. (3) takes into account the varying contribution of the kinetic to the total $\alpha$ -particle energy which depends on the potential depth at position $r$ . Timedependent quantum-mechanical calculations [3], however, indicate that the oscillations of the $\alpha$ -particle wave-function within the nucleus have an extremely small amplitude, which might lead to a better estimate of the number of barrier assaults per second.

The $\alpha$ -decay half live $\tau _ { 1 / 2 }$ is then finally obtained by

$$
\tau_ {1 / 2} = \frac {\ln 2}{\lambda} \tag {4}
$$

A semi-empirical formula for the calculation of $\alpha$ half lives was presented by V. E. Viola and G. T. Seaborg (VS) in 1966 [2]. It is based on the Gamow picture and assumes a nuclear potential of uniform depth that rises abruptly

at the radius of the nucleus, going from this uniform potential to a Coulomb potential, resulting in a cusp at the radius of the nucleus. Also, the nucleus and therefore the potential are assumed to be spherically symmetric.

The resulting formula reads

$$
\log \tau_ {1 / 2} = \frac {a Z + b}{\sqrt {Q _ {\alpha}}} + (c Z + d), \tag {5}
$$

yielding the $\alpha$ -decay half life $\tau _ { 1 / 2 }$ in units of seconds. The experimental input are the charge number $Z$ and the $Q _ { \alpha }$ value (in units of MeV) for a given nucleus $( Z , N )$ . It contains four adjustable parameters $a , b , c , d$ . These parameters have been adjusted to the experimental data on half lives known at that time. In more recent work, the parameters have been readjusted, taking into account new experimental data on superheavy elements [4]. Table 1 summarizes the values of these parameters and also contains the parameters of our adjustment made in this paper, see Subsection 3.1 for details. The VS systematics has been used in Ref. [5] to calculate $\alpha$ half lives for unknown superheavy nuclei. We note that there exists a variety of very accurate semi-empirical half live formulas, see for example Refs. [6,7].

Table 1 Parameters of the original VS systematics [2], its readjustment including data on superheavy nuclei [4], as well as our adjustment to experimental data from Ref. [8].   

<table><tr><td></td><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>original VS</td><td>2.11329</td><td>-48.9879</td><td>-0.390040</td><td>-16.9543</td></tr><tr><td>readjusted VS</td><td>1.66175</td><td>-8.5166</td><td>-0.20228</td><td>-33.9069</td></tr><tr><td>our adjustment</td><td>1.58134</td><td>-2.27889</td><td>-0.23543</td><td>-30.1503</td></tr></table>

In this paper, we present a model for the calculation of $\alpha$ -decay half lives based on microscopically calculated potentials from self-consistent mean-field models, namely the relativistic mean-field (RMF) model and the Skyrme-Hartree-Fock (SHF) approach, thus replacing the simplified assumptions of Eq. (5). In Section 2 we present our approach. Section 3 describes the adjustment and analysis of our method. We compare its predictions with both experimental data as well as a new adjustment of the VS systematics. In Section 4 we extrapolate to superheavy nuclei and compare the two approaches. We conclude in Section 5.

# 2 Theoretical Framework

In our approach, which we henceforth denote as $\alpha$ -mf, the $\alpha$ -decay constant is given by Eq. (1). The $\alpha$ -nucleus potential is given by

$$
V _ {\alpha} = 2 \times V _ {p} + 2 \times V _ {n} (6)
$$

The proton potential $V _ { p }$ and the neutron potential $V _ { n }$ are taken from spherical self-consistent mean-field calculations (see below). Thus, $V _ { \alpha }$ contains the sum of the nuclear and the Coulomb potential. In the relativistic models, the $V _ { \alpha }$ potential is obtained as the sum of the scalar and vector potentials. The $\alpha$ - particle is treated as a spin-saturated system of two protons and two neutrons, thus it does not feel the spin-orbit force that is generated by the strong scalar and vector fields adding up with the same sign in the relativistic approaches, and put in by hand as an additional term in the SHF approach.

The transmission probability and the knocking frequency, given by Eqs. (2) and (3), respectively, are calculated by numerical integration using the meanfield potentials. While the bosonic and structure-less $\alpha$ -particle picture can be expected to work for the tunneling process as long as the Compton wavelength of the $\alpha$ -particle is small compared to the width of the barrier, the ’knocking’ process of the $\alpha$ -particle within the Coulomb barrier is certainly more complicated due to the fermionic nature of the nucleons and the necessary anti-symmetrization between the wave functions of $\alpha$ -particle and nucleus. Still, we may expect that these corrections will not affect too much the overall performance of our model.

Our approach contains only one free parameter which we denote by $f$ and which is related to $f$ in Eq. (1). It needs to be fitted to experimental data. This parameter not only in an average way describes the formation probability, but also absorbs all errors and approximations made in the calculations of $P$ and $\nu$ . Interpreting it as an (average) probability, it should be less than or equal to 1. According to Ref. [9] a pre-formation factor should be below 0.1. In order to estimate the accuracy of the knocking frequency calculation, we also build combined parametrizations with the combined parameter $c = \bar { f } \times \nu$ , in which only the transmission probability is computed numerically.

We note that with the knowledge of the single-particle wave functions, it is possible to calculate the pre-formation factor, see for example Ref. [10] for a calculation using Nilsson model single particle wave functions and Ref. [11] for a parameter-free approach for calculating the $\alpha$ -decay half live of $\mathrm { ^ { 2 1 2 } P o }$ employing a combined shell and cluster model. Complementing our model by such a pre-formation calculation would lead to a fully microscopic, parameterfree approach, which is, however, beyond the scope of this paper and will be dealt with in forthcoming work. The assumption of spherical potentials

in our approach loses its validity for deformed nuclei. It is, however, also used in the Viola-Seaborg systematics and appears to work well for life-time predictions. Future work will include potentials taken from deformed meanfield calculations [12].

The mean-field $\alpha$ -potential corrects the simplified potential of other approaches by providing a smooth surface and $r$ -dependent interior nuclear potential, and eliminates the spike at the transition from the nuclear to the Coulomb part, see Fig. 1 (the authors of Ref. [13] use a non-self-consistent potential with a smooth surface). Also, its radius automatically possesses the correct massdependence. The accuracy of our model tests the asymptotics of the Coulomb contribution to the mean-field potentials stemming from the relativistic meanfield calculations up to typical radii of $r \approx 7 0$ fm. The mean-field potentials – due to their self-consistent interdependence of proton and neutron densities – automatically introduce a dependence on neutron number, i.e., an isospin dependence. For each nucleus, the input to our model is the $V _ { \alpha }$ potential from the daughter nucleus (assuming that the $\alpha$ particle has already formed), the $Q _ { \alpha }$ value and the mass of the nucleus. The potential is being represented on a radial 1-D grid in coordinate space. The classical turning points $r _ { 1 }$ and $r _ { 2 }$ are determined and then used as boundaries for the numerical computation of transmission and knocking frequency according to Eqs. (2) and (3). Because of the uncertainties related to the calculation of odd-even and odd-odd nuclei, we consider only even-even nuclei in this study.

The self-consistent mean-field models used in this work are on the one hand two variants of the relativistic mean-field model, one employing contact interactions (RMF-PC) , and the other variant employing finite-range boson fields (RMF-FR), and on the other hand the Skyrme-Hartree-Fock (SHF) approach. We refer the reader to Refs. [14,15,16,17] for a detailed discussion of these models. In modern terms, self-consistent mean-field models are approximations to the exact many-body functional in the spirit of density functional theory [18], their interaction terms governed by principles of effective field theory such as naive dimensional analysis. Thus, these models are able to absorb various ground-state correlations and to incorporate physics beyond the (literal) mean-field approximation [19].

The models used here contain between 6-12 parameters plus two pairing strengths (for protons and neutrons separately) for BCS pairing with a densityindependent $\delta$ -force. The parameter sets employed in this work are NL3 [20] and NL-Z2 [21] for RMF-FR, PC-F1 [22] for RMF-PC, and SkI3 [23] and SLy6 [24] for SHF, which are modern mean-field forces that deliver great predictive power. They result from careful adjustments to nuclear ground-state observables, e.g., binding energies, rms charge and diffraction radii, and surface thicknesses [22]. The nucleon single-particle wave-functions are calculated self-consistently on a grid in coordinate space employing matrix multiplica-

tions in Fourier space for the derivatives. To obtain the solution with minimal energy, the damped gradient-step method is used [25]. Calculations with both models share the same basic numerical routines, thus numerical differences do not interfere with differences in physics for model comparisons. The center of mass correction is used as in the adjustment procedure of the mean-field parametrization.

Since the $\alpha$ -particle has a finite extension, in addition we test another model variant by folding its parametrized density distribution with the mean-field alpha potential, i.e.

$$
V _ {\alpha} ^ {f o l d.} (\vec {R}) = \int \rho_ {\alpha} (\vec {r} - \vec {R}) V _ {\alpha} (\vec {r}) d ^ {3} r \tag {7}
$$

The radial density parametrization of the $\alpha$ -particle is taken from Ref. [26] and is given by

$$
\rho_ {\alpha} (r) = 0. 4 2 2 9 \times e ^ {- 0. 7 0 2 4 r ^ {2}}, \tag {8}
$$

where $\rho _ { \alpha } ( \boldsymbol { r } )$ is given in units of $\mathrm { f m } ^ { - 3 }$ $^ { - 3 }$ , and the radius $r$ needs to be specified in units of fm. The effect of the folding procedure on the mean-field potential is shown in Figure 1.

Our $\alpha$ -decay model contains no assumptions on the nuclear potential, except for the calculation of the potentials in spherical symmetry. Thus, provided that the potentials from the self-consistent mean-field models are realistic, it should lead to more reliable extrapolations to exotic and superheavy nuclei compared to semi-empirical models. We note that these potentials automatically possess – due to the adjustment of the mean-field models to densityrelated ground-state observables – the correct mass dependence of the potential radius and also information on the surface region of the nucleus. These need to be parametrized in more schematic approaches.

We would like to point out possible extensions of the $\alpha$ -mf approach, most of them going clearly beyond the scope of semi-empirical approaches. The microscopic calculation of the pre-formation factor has already been mentioned. Another enhancement would be the usage of 2-dimensional potentials from axially deformed nuclei. In the case of shape coexistence of nuclei, the dependence of the decay width on the prolate or oblate minimum can be investigated. Furthermore, decay widths stemming from the ground state or an isomeric state (shape isomer) of a heavy nucleus can be computed. The description of fine structure in $\alpha$ -decay will be an interesting application, see for example Ref. [27]. The model could be enhanced still further by replacing the WKB approximation with numerical calculations of the stationary or time-dependent Schr¨odinger equation.

![](images/95cafe25634c534f94dbf4befbf9a1e217b9e782bb4af750c769dee8ee51350f.jpg)  
Fig. 1. Alpha-nucleus potential obtained from a mean-field calculation with PC-F1 (dashed line), the same potential but folded with the $\alpha$ -particle density (dotted line), and a schematic potential according to the VS systematics (full line) for the nucleus $2 5 4$ Cf

# 3 Results

# 3.1 Adjustment

For the model adjustment and comparison, we use recent $\alpha$ -decay data from Ref. [8]. Since the experimental data varies over thirty orders of magnitude (from $1 . 1 \times 1 0 ^ { - 7 }$ s to $2 . 2 \times 1 0 ^ { 2 3 }$ s) we have performed a logarithmic $\chi ^ { 2 }$ fit to adjust the model parameter. The logarithmic error of a given data point is given by

$$
\chi = \log \left(\frac {\tau_ {1 / 2 , t h}}{\tau_ {1 / 2 , e x p}}\right) \tag {9}
$$

Computing errors in this way measures how many orders of magnitude the calculated point is away from the experimental value (for example, $\chi = 2 . 5$ means that the calculated value is 2.5 orders greater than the experimental value, while $\chi = - 3$ means that the calculated value is 3 orders of magnitude less than the experimental value).

To obtain a fair comparison between $\alpha$ -mf and VS systematics, we have readjusted the VS systematics to exactly the same data that has been used in the

adjustment of our model [8], employing the Monte-Carlo methods described in Ref. [22] (down-hill methods got stuck very easily in adjacent local minima). The Monte-Carlo optimization was finally followed by a down-hill minimization, driving the parameter vector to the bottom of the (local) minimum. The resulting parameters are shown in Table 1. Note that this adjustment has been started with the parameters of the readjusted VS formula. The usage of Monte-Carlo techniques has reduced $\chi ^ { 2 }$ considerably. However, there might very well exist several local minima, of which some could correspond to models with even better predictive power.

The $\chi ^ { 2 }$ values of the $\alpha$ -mf approach employing different mean-field forces are displayed in table 2. In the following we implicitly refer to $\chi ^ { 2 }$ per point when we write $\chi ^ { 2 }$ . The $\chi ^ { 2 }$ value of our VS systematics adjustment is included as well. We see that the Skyrme forces SkI3 and SLy6 in three of four cases deliver a $\chi ^ { 2 }$ value that is below $\chi ^ { 2 }$ of this adjustment of the VS systematics, while the relativistic models have slightly larger values. This model difference is quite interesting since it yields information on the (otherwise unobservable) potentials of the different approaches. The SHF potentials (for both Skyrme forces) lead to better predictive power compared to RMF. This model difference, that might be related to the effective masses, radial dependences, and Coulomb exchange (absent in RMF) deserves further attention in future investigations. The model variants with the combined parameter $c$ (absorbing both preformation factor and knocking frequency into one parameter) perform better in most cases. The differences are not dramatic, however, indicating that the explicit calculation of $\nu$ is consistent with our model assumptions. The (average) preformation factors $f$ are smaller than one and thus can be interpreted as probabilities. They also agree with the estimates from Ref. [9].

The model variant employing the folded potentials from calculations with PC-F1 performs slightly better when explicitely computing the knocking frequency, and slightly worse when absorbing it into the parameter $c$ . This might be connected to the fact that in the folding case we still use the simple reduced mass in the calculation of the tunneling probability, while the mass parameter is certainly different for an extended object. The parameter $f$ for the folded PC-F1 potential is a factor of 10 smaller than the value without folding, which is related to the increase of the tunneling probability in the folded case, see Fig. 1.

We have determined the $\chi ^ { 2 }$ values of the previous fits of the VS systematics using the experimental data from Ref.[8]. The original Viola-Seaborg method yields $\chi ^ { 2 } = 2 . 5 7$ , and the improved Viola-Seaborg method $\chi ^ { 2 } = 1 . 2 7$ .

Table 2   

<table><tr><td>force</td><td>f̄</td><td>χ2</td><td>c (1/s)</td><td>χ2</td></tr><tr><td>NL3</td><td>0.028</td><td>0.21</td><td>9.78e19</td><td>0.21</td></tr><tr><td>NL-Z2</td><td>0.014</td><td>0.17</td><td>4.57e19</td><td>0.16</td></tr><tr><td>PC-F1</td><td>0.080</td><td>0.24</td><td>3.09e20</td><td>0.22</td></tr><tr><td>PC-F1, folded</td><td>0.006</td><td>0.23</td><td>1.95e19</td><td>0.24</td></tr><tr><td>SkI3</td><td>0.087</td><td>0.17</td><td>3.46e20</td><td>0.15</td></tr><tr><td>SLy6</td><td>0.075</td><td>0.15</td><td>2.85e20</td><td>0.14</td></tr><tr><td>our VS fit</td><td></td><td>0.16</td><td></td><td></td></tr></table>

The parameter $f$ and corresponding $\chi ^ { 2 }$ values for the model variant with explicit calculation of the knocking frequency (columns 1 and 2), and the combined parameter $c$ and corresponding $\chi ^ { 2 }$ values for the combined variant (columns 3 and 4), for the mean-field forces as indicated. For comparison, the $\chi ^ { 2 }$ value of our VS systematics adjustment is shown.

# 3.2 Analysis

In Figure 2 we compare half lives between $\alpha$ -mf employing the relativistic mean-field parametrization PC-F1 and experimental data (since the different mean-field approaches have similar predictive power, comparisons of other forces with experiment yield similar figures). Note that the $\alpha$ -mf approach delivers a very good overall agreement with $| \chi | < 0 . 3 - 0 . 6$ in most of the cases, i.e., the deviations are well below an order of magnitude. These errors have predominantly positive signs corresponding to an over-estimation of the $\alpha$ life-times, i.e., an over-estimation of stability of these nuclei with respect to $\alpha$ -decay. Negative errors are visible at and near shell closures, see the discussion below. The accuracy of our approach does not appear to depend strongly on the mass number of the decaying nucleus, indicating that the mass number dependence is correctly reproduced in the mean-field potentials. The best agreement, however, is achieved for the actinides.

We would like to examine our predictions for indications of physics not (yet) accounted for in our model. We can expect to see deviations originating from i) shell effects and ii) deformation effects. Let us first examine shell effects. At the magic neutron number $N = 1 2 6$ , for $Z = 8 4 - 9 0$ isotopes we notify a jump in the logarithmic error: $\alpha$ -mf overestimates the stability of $N = 1 2 8$ isotones, while the stability of $N \ = \ 1 2 6$ isotones is underestimated (indicated by a negative error). We see a similar effect at the magic proton number $Z = 8 2$ : $\alpha$ - mf underestimates stability. This trend can be nicely observed for the $N = 1 2 8$ isotones. As the proton number drops off towards 82, the nuclides become more and more stable compared to our predictions. Even though shell effects are taken into account to some extent via the experimental $Q _ { \alpha }$ values, the

![](images/b73c0ec3892212cee078642f300fde64c0d2cd6a60ee055c92fb1f851d70db64.jpg)  
Fig. 2. Logarithmic error of our approach with PC-F1 as a contour plot versus neutron number (x-axis) and proton number (y-axis). Each square corresponds to an even-even nucleus.

computation of the tunneling probability cannot reproduce them sufficiently. They would enter, however, in a microscopic calculation of the preformation amplitude.

Another cause of trends is the deformation of nuclei. Our current model – as does the VS systematics – assumes spherically symmetric nuclei. It is interesting that the assumption of spherical potentials works so well both in semi-empirical approaches and in our model. However, most nuclei for which we predict $\alpha$ half lives are deformed. Thus, for axially deformed nuclei the Coulomb barrier is 2-dimensional, leading to a more complicated tunneling dynamics (see Refs. [28,29] for a time-dependent description of 2-dimensional tunneling in proton emission). For the most part, our predictions do not display a random distribution pattern, but rather show clusters where the model is more accurate and clusters were it is less accurate. For example, nuclei with atomic numbers close to $Z = 8 8$ and $N = 1 3 6$ are less stable than our model predicts, and around $Z = 1 0 2$ and $N = 1 5 2$ there is a region of extra stability that our model does not yet account for. It is not possible to tell directly from our data whether the deformation effect results in making nuclei appear to have extra stability or extra instability, due to the masking effect of optimizing the (average) pre-formation factor. We believe, however, that accounting

![](images/c3a557c14d541ec7fa6d57ead1fb808dce1c23b5696259d9cd5d480770385e48.jpg)  
Fig. 3. Logarithmic error of the newly adjusted Viola-Seaborg systematics as a contour plot versus neutron number (x-axis) and proton number (y-axis). Each square corresponds to an even-even nucleus.

for deformations in nuclei shall improve our model.

Comparing the predictions of the $\alpha$ -mf approach (Fig. 2) with the ones from our VS systematics adjustment (Fig. 3), we detect a few differences. Firstly, nuclei with larger errors with respect to the surrounding ones are distributed differently in both approaches. Secondly, there are small regions of nuclei which are described better in each model, for example the nuclei centered around $Z = 8 6 , N = 1 3 0$ have larger errors within the VS systematics, while nuclei at or next to the $\alpha$ -decay chain starting at $Z = 9 0 , N = 1 2 0$ are more accurately described by the VS model. Moreover, we detect similar wrong trends that can be attributed to missing deformation and/or shell structure features in the VS systematics.

In the next Section, we extrapolate with $\alpha$ -mf employing SLy6 to superheavy nuclei and compare with the predictions of the VS systematics.

![](images/973ae200add9175709369a036844a722b2d39beb248b1affe8f4cb5771c561b5.jpg)  
Fig. 4. Logarithmic ratio of the predicted life time from $\alpha$ -mf over the predicted life time of our Viola-Seaborg adjustment systematics as a contour plot versus neutron number (x-axis) and proton number (y-axis). Each square corresponds to an even-even nucleus, nuclei without a converged solution have been omitted. The black squares indicate the valley of $\beta$ stability, the grey line corresponds to the two-proton dripline.

# 4 Extrapolation to superheavy elements

We employ the $\alpha$ -mf approach with the force SLy6, which has performed best in terms of $\chi ^ { 2 }$ , for an extrapolation to superheavy nuclei. We compare its predictions to the predictions from our adjustment of the VS systematics. The $Q _ { \alpha }$ values are obtained from axially deformed ground-state calculations with SLy6, similarly to Refs. [30,5]. The potentials are obtained from calculations in spherical symmetry. For both models, the $Q _ { \alpha }$ values calculated with SLy6 are used, since a) experimental data in that region is very scarce (especially for even-even nuclei) and b) we aim at a pure model comparison.

The logarithmic ratio of the two approaches can be seen in Fig. 4. The difference between the two approaches remains quite small (below 0.1) for nuclei close to $\beta$ -stability. Also, both models show no visible difference in the error with mass number, a feature we have seen before for the known elements. However, an isovector trend appears in the figure between the two methods.

With decreasing $N - Z$ ratio, the $\alpha$ -mf approach predicts increasingly larger life times. Since both approaches use the same – calculated – $Q _ { \alpha }$ values, the isospin dependence has its origin in the potential shapes used in $\alpha$ -mf which introduces a dependence on the neutron number. This isovector trend is absent in the VS systematics.

For nuclei with masses beyond superheavy nuclei ( $A \ge 2 9 2$ ), various groups have theoretically found semi-bubble and bubble structures [31,32,33,34], i.e., the density in the interior of the nucleus is reduced or even completely suppressed, leading to nuclear systems with an inner surface. Because of this structure, these systems possess potentials that differ to a great extent from usual nuclear potentials. Thus, they will constitute an interesting application for $\alpha$ -decay models based on self-consistent potentials [12].

# 5 Conclusions

We have presented a one-parameter model for $\alpha$ -decay that can be used to predict life times of $\alpha$ -emitters. This model can be applied successfully over a large range of nuclei. Its accuracy is comparable to or even slightly better than semi-empirical approaches. This has been demonstrated by a new adjustment of the Viola-Seaborg formula. However, universality and extensibility are the decisive features of this model. It can be applied to exotic and superheavy nuclei, in which the assumptions of (very successful) semi-empirical formulas about the shape of the potential lose more and more validity, given that the potentials from the self-consistent mean-field models are still realistic. By employing a variety of recent mean-field parametrizations, we have found that $\alpha$ -nucleus potentials from the Skyrme-Hartree-Fock method yield slightly better results compared to the RMF model potentials.

An extrapolation to superheavy elements has shown that the $\alpha$ -mf approach displays an isospin dependence of life times which is absent in the Viola-Seaborg approach. This point deserves further attention as new data become available.

The model is simple in terms of required parameters. While the Viola-Seaborg systematics contains four parameters that need to be simultaneously optimized, it contains only one adjustable parameter, the (average) pre-formation (or a combined) factor. Furthermore, our model has ample room for improvement. One potential improvement would be to microscopically calculate the pre-formation factors using nuclear single-particle and $\alpha$ -particle wavefunctions, yielding a fully microscopic, parameter-free approach. Other enhancements and applications involve multi-dimensional potentials and finestructure $\alpha$ -decay calculations.

# Acknowledgements

Z. A. D. and T. J. B. would like to thank N. Magee, L. Collins, D. James and S. Seidel for the organizing of the Los Alamos Summer School 2004. T. J. B. would also like to thank D. G. Madland, C. M¨uller, P.–G. Reinhard, O. Serot, and P. Talou for helpful comments. This work was supported by the U.S. Department of Energy.

# References

[1] G. Gamow, Z. Phys., 51 (1928) 204   
[2] V. E. Viola Jr. and G. T. Seaborg, J. Inorg. Nucl. Chem. 28 (1966) 741   
[3] O. Serot, N. Carjan, and D. Strottman, Nucl. Phys. A569 (1994) 562   
[4] A. Sobiczewski et al., Phys. Lett. B 224 (1989) 1   
[5] T. B¨urvenich, K. Rutz, M. Bender, P.–G. Reinhard, J. A. Maruhn, and W. Greiner, Eur. Phys. J. A 3 (1998) 139   
[6] B. A. Brown, Phys. Rev. C 46 (1992) 811   
[7] D. N. Poenaru and M. Ivascu, J. Phys. (Paris) 44 (1983) 791   
[8] Jag Tuli, Evaluated Nuclear Structure Data File, Brookhaven National Lab (June 30, 2004) http://www.nndc.bnl.gov/ensdf/index.jsp   
[9] T. L. Stewart et al., J. Phys. G. Nucl. Part. Phys. 25 (1999) 1057   
[10] D. S. Delion, A. Insolia, and R. J. Liotta, Phys. Rev. C 46 (1992) 1346   
[11] K. Varga, R. G. Lovas, and R. J. Liotta, Phys. Rev. Lett. 69 (1992) 37   
[12] Z. A. Dupr´e and T. J. B¨urvenich, in preparation   
[13] B. Buck, A. C. Merchant, and S. M. Perez, Phys. Rev. C 45 (1992) 2247   
[14] M. Bender, P.–H. Heenen, and P.–G. Reinhard, Rev. Mod. Phys. 75 (2003) 121   
[15] P.–G. Reinhard, Rep. Prog. Phys. 52 (1989) 439   
[16] B. D. Serot and J. D. Walecka, Advances in Nuclear Physics (Plenum Press, New York, 1986), Vol. 16   
[17] B. A. Nikolaus, T. Hoch, and D. G. Madland, Phys. Rev. C 46 (1992) 1757   
[18] R. M. Dreizler and E. K. U. Gross, Density functional theory, Springer, Berlin, 1990

[19] R. J. Furnstahl, Lect.Notes Phys. 641 (2004) 1   
[20] G. A. Lalazissis, J. K¨onig, and P. Ring, Phys. Rev. C 55 (1997) 540   
[21] M. Bender, K. Rutz, P.–G. Reinhard, J. A. Maruhn, and W. Greiner, Phys. Rev. C 60 (1999) 034304   
[22] T. B¨urvenich, D. G. Madland, J. A. Maruhn, and P.–G. Reinhard, Phys. Rev. C 65 (2002) 044 308   
[23] P.–G. Reinhard and H. Flocard, Nucl. Phys. A584 (1995) 467   
[24] E. Chabanat, P. Bonche, P. Haensel, J. Meyer, and R. Schaeffer, Nucl. Phys. A635 (1998) 231   
[25] P.–G. Reinhard and R. Y. Cusson, Nucl. Phys. A378 (1982) 418   
[26] D.N. Basu, J. Phys. G 29 (2003) 2079   
[27] K. Van de Vel et al., Phys. Rev. C 68 (2003) 054311   
[28] P. Talou, N. Carjan, and D. Strottman, Nucl. Phys. A 647 (1999) 21   
[29] N. Carjan, P. Talou, and D. Strottman, in: The Nucleus: New Physics for the New Millenium, edited by Smit et al., Kluwer Academic/Plenum Publishers, New York, 2000, p. 115-119   
[30] S. Typel, A. Brown, Phys. Rev. C 67 (2003) 034313   
[31] K. Dietrich, K. Pomorski, Nucl. Phys. A (1976) 175   
[32] K. Dietrich, K. Pomorski, Phys. Rev. Lett. 80 (1998) 37   
[33] K. Rutz, M. Bender, T. B¨urvenich, T. Schilling, P.–G. Reinhard, J. A. Maruhn, and W. Greiner, Phys. Rev. C 56 (1997) 238   
[34] J. Decharg´e, J.–F. Berger, K. Dietrich, and M. S. Weiss, Phys. Lett. B 451 (1999) 275