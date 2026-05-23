# Investigation of the determination of nuclear deformation using high-energy heavy-ion scattering

Shin Watanabe∗

National Institute of Technology (KOSEN), Gifu College, Motosu 501-0495, Japan and

RIKEN Nishina Center, Wako 351-0198, Japan

Takenori Furumoto†

College of Education, Yokohama National University, Yokohama 240-8501, Japan

Wataru Horiuchi

Department of Physics, Osaka Metropolitan University, Osaka 558-8585, Japan

Nambu Yoichiro Institute of Theoretical and Experimental Physics (NITEP),

Osaka Metropolitan University, Osaka 558-8585, Japan

RIKEN Nishina Center, Wako 351-0198, Japan and

Department of Physics, Hokkaido University, Sapporo 060-0810, Japan

Tadahiro Suhara

National Institute of Technology (KOSEN), Matsue College, Matsue 690-8518, Japan

Yasutaka Taniguchi

Department of Computer Science, Fukuyama University, Fukuyama 729-0292, Japan

RIKEN Nishina Center, Wako 351-0198, Japan and

National Institute of Technology (KOSEN), Kagawa College, Mitoyo 769-1192, Japan

(Dated: August 7, 2024)

Background: Nuclear deformation provides a crucial characteristic of nuclear structure. Conventionally, the quadrupole deformation length of a nucleus, $\delta _ { 2 }$ , has often been determined based on a macroscopic model through a deformed nuclear potential with the deformation length $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ , which is determined to reproduce the nuclear scattering data. This approach assumes $\delta _ { 2 } = \delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ although there is no theoretical foundation.

Purpose: We clarify the relationship between $\delta _ { 2 }$ and $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ for high-energy heavy-ion scattering systematically to evaluate the validity of the conventional approach to determine the nuclear deformation.

Method: The deformation lengths for the $^ { 1 \bar { 2 } } \bar { \mathrm { C } }$ inelastic scattering by $^ { 1 2 } \mathrm { C }$ , $^ { 1 6 } \mathrm { O }$ , $^ { 4 0 } \mathrm { C a }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ targets at $E / A$ $= 5 0 { \mathrm { - } } 4 0 0 \ \mathrm { M e V }$ are examined. First, we perform microscopic coupled-channel (CC) calculations to relate $\delta _ { 2 }$ of the deformed density into the inelastic scattering cross section. Second, we use the deformed potential model to determine $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ so as to reproduce the microscopic CC result. We then compare $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ with $\delta _ { 2 }$ .

Results: We find that $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is about $20 \%$ smaller than presumed $\delta _ { 2 }$ , showing strong energy and target dependence. Further analysis, which considers higher-order deformation effects beyond the derivative model, reveals that $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is still about $1 5 \mathrm { - } 3 5 \mathrm { ~ \% ~ }$ smaller than $\delta _ { 2 }$ .

Conclusion: Our results suggest that one needs to be careful when the deformed potential model for the highenergy heavy-ion scattering is used to extract the nuclear deformation. The conventional approach may underestimate the deformation length $\delta _ { 2 }$ systematically.

# I. INTRODUCTION

The determination of nuclear deformation is one of the key issues in nuclear physics. As it significantly influences the nuclear structure and reaction dynamics [1, 2], the nuclear deformation has extensively been investigated from various points of views [3–17]. The nuclear surface of an axially symmetric deformed nucleus is often represented as $\begin{array} { r l } { R ( \theta ^ { \prime } ) { } = } \end{array}$ $\begin{array} { r l } { R _ { 0 } \left[ 1 + \sum _ { \lambda } \beta _ { \lambda } Y _ { \lambda 0 } ( \theta ^ { \prime } ) \right] } \end{array}$ , where $R _ { 0 }$ and $\beta _ { \lambda }$ denote the radius parameter and the deformation parameter with multipolarity $\lambda$ , respectively. Determining the deformation length $\delta _ { \lambda } = R _ { 0 } \beta _ { \lambda }$

is important as it provides a crucial indicator of nuclear deformation. The deformation length is also an essential input to the collective model, which offers a simple and powerful description of atomic nuclei, allowing us to predict the electromagnetic properties as well as the inelastic scattering cross sections with the help of the distorted wave Born approximation (DWBA).

In the present work, we focus on the most basic nuclear deformation, quadrupole deformation. The quadrupole deformation length $\delta _ { 2 }$ of a nucleus has often been deduced from inelastic scattering cross sections using the conventional approach such as coupled-channel (CC) formalism and DWBA. These conventional approaches are based on the collective model, and are often referred to as the deformed potential (DP) model [5]. In the DP model, the deformation length δ(pot) $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ of the nuclear optical potential is determined to reproduce the experimental cross sections. In order to extract $\delta _ { 2 }$ in the DP

model, the relation

$$
\delta_ {2} = \delta_ {2} ^ {(\mathrm {p o t})} \tag {1}
$$

is often assumed. However, this assumption has no basis and is questionable because $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ includes the information on both the projectile and target nuclei, and also the nuclear force. Based on this unestablished assumption (1), $\delta _ { 2 }$ has been experimentally determined with the DP model [18–22].

Here, we take a microscopic approach for extracting $\delta _ { 2 }$ . Over the past five decades, a microscopic CC calculation for heavy-ion scattering has been developed significantly [2, 23] and has been widely used to investigate nuclear structure and reactions [2, 5, 24–33]. These calculations are based on the double-folding model, where the nuclear optical potential is constructed by folding the effective nucleon-nucleon interaction with the projectile and target densities. When a coupling potential is required, a transition density, which reflects the deformation effect, is incorporated into the folding procedure. Henceforward, we call this microscopic framework the deformed density (DD) model to distinguish it from the DP model. The DD model enables us to extract $\delta _ { 2 }$ directly, not via $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ . Recently, the microscopic CC calculation with a complex $G$ -matrix interaction has been successfully applied to heavy-ion scattering [34–36]. The power of the complex $G$ -matrix interaction is also shown not only in reproducing the experimental data but also in predicting interesting nuclear reaction phenomena [30, 32, 37, 38].

In this study, we aim to elucidate the relationship between δ2 and δ(pot) $\delta _ { 2 }$ $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ using the DD and DP models in a wide range of incident energies and target nuclei. The earlier studies investigated this relationship mainly for the lower-energy region $( E / A < 1 0 0 ~ \mathrm { M e V } )$ , and showed that the use of the DP model significantly underestimates the nuclear deformation length [5, 39]. Extending these analyses to the high-energy region is challenging due to the lack of experimental data on high-energy heavy-ion scattering. As mentioned, recent development of the folding model approaches allows us to make a reliable prediction of high-energy heavy-ion scattering. Therefore, it is worthwhile to proceed with a theoretical analysis in the high-energy region. It should be noted that we can discuss deformation effects more straightforwardly as the reaction mechanism becomes simpler at higher incident energies. In the present study, we consider the $^ { \mathrm { i } 2 } \mathrm { C }$ inelastic scattering by $^ { 1 2 } \bar { \mathrm { C } }$ , $^ { 1 6 } \mathrm { O }$ , $^ { 4 0 } \mathrm { { C a } }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ targets at $E / A = 5 0 – 4 0 0$ MeV.

This paper is organized as follows. In Sec. II, we explain how to relate δ2 with δ(pot) $\delta _ { 2 }$ $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ using the DD and DP models. This section is further divided into three subsections. In Sec. II A, we present the theoretical framework to obtain the microscopic potential, which is used in both the DD and DP models. The DD and DP models are detailed in Secs. II B and II C, respectively. In Sec. III, we first show the validity of the present models for the elastic scattering. Next, we calculate the angular-integrated inelastic scattering cross sections using the DD model. The cross sections are used as reference calculations to extract $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ in the DP model. Then, $\delta _ { 2 }$ and $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ are compared systematically. Lastly, the conclusion is given in Sec. IV.

# II. FORMALISM

We calculate the inelastic scattering cross sections for the $2 _ { 1 } ^ { + }$ state of $^ { 1 2 } \mathrm { C }$ , denoted as $\sigma ( 2 _ { 1 } ^ { + } )$ , using the CC formalism. In the CC calculation, both diagonal and coupling potentials are required. They are obtained with two models: the deformed density (DD) model and the deformed potential (DP) model. In the DD model, we first assume a deformed density characterized by $\delta _ { 2 }$ . Then, we can construct the diagonal and coupling potentials microscopically through the folding procedure. Once these potentials are determined, the $\sigma ( 2 _ { 1 } ^ { + } )$ can be calculated in the standard CC framework. The result of the DD model is used as a reference calculation in this paper. On the other hand, in the DP model, we derive the coupling potential by assuming a deformed potential characterized by $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ . The value of $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is determined so as to reproduce the $\sigma ( 2 _ { 1 } ^ { + } )$ calculated with the DD model. Finally, we systematically compare $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ with $\delta _ { 2 }$ in high-energy heavy-ion scattering and elucidate the relationship between them.

# A. Microscopic potentials

We briefly summarize the construction of the microscopic potential used in this paper. The detailed formulation is described in Refs. [26, 29, 38, 40].

We consider the scattering of a deformed projectile (P) and a spherical target (T). The diagonal and coupling potentials between P and T are obtained by folding the effective nucleonnucleon interaction $\nu _ { N N }$ with the projectile and target densities:

$$
\begin{array}{l} U _ {I ^ {\prime} I} ^ {(\lambda)} (R) = \int \rho_ {I ^ {\prime} I} ^ {(\lambda)} \left(r _ {1}\right) \rho_ {\mathrm {T}} \left(r _ {2}\right) v _ {N N} (s, \rho) \\ \times \left[ \mathcal {Y} _ {\lambda} (\hat {r} _ {1}) \otimes \mathcal {Y} _ {\lambda} (\hat {\boldsymbol {R}}) \right] _ {0 0} d \boldsymbol {r} _ {1} d \boldsymbol {r} _ {2} d \hat {\boldsymbol {R}}, \tag {2} \\ \end{array}
$$

where $\pmb { R }$ is the coordinate between P and T, $r _ { 1 } \left( r _ { 2 } \right)$ is the coordinate of the interacting nucleon from the center of mass of P (T), and $s = R - r _ { 1 } + r _ { 2 }$ . The subscripts $I$ and $I ^ { \prime }$ are the initial and final spins of P, respectively, $\lambda$ denotes the multipolarity, and $\mathcal { V } _ { L M } ( \hat { \boldsymbol { r } } ) ~ = ~ i ^ { L } Y _ { L M } ( \hat { \boldsymbol { r } } )$ . The density-dependent part $\rho$ in $\nu _ { N N }$ is taken based on the frozen density approximation [37, 41]. The validity of this approximation is discussed in Refs. [41–43]. We define the transition density as

$$
\rho_ {I ^ {\prime} m ^ {\prime}, I m} (\boldsymbol {r}) = \sqrt {4 \pi} \sum_ {\lambda \mu} (I m \lambda \mu | I ^ {\prime} m ^ {\prime}) \rho_ {I ^ {\prime} I} ^ {(\lambda)} (r) \mathcal {Y} _ {\lambda \mu} ^ {*} (\hat {\boldsymbol {r}}), \tag {3}
$$

where $\rho _ { I ^ { \prime } I } ^ { ( \lambda ) }$ is the radial part of the transition density with rank λ, $( I m \lambda \mu | I ^ { \prime } m ^ { \prime } )$ is the Clebsch-Gordan coefficient, and m, m′, and $\mu$ denote the z components of I, I′, and $\lambda$ , respectively. In Eq. (2), T is assumed to be inert, that is, $\rho _ { \mathrm { T } } ( r _ { 2 } )$ is the ground state density ρ(λ=00 $\rho _ { 0 0 } ^ { ( \lambda = 0 ) } ( r _ { 2 } )$ in the definition (3). Equation (2) is the so-called direct part, and the exchange part is similarly obtained in the folding procedure as prescribed in Refs. [5, 29, 38]. The Coulomb potential is also constructed in the folding model, where the Coulomb nucleon-nucleon interaction is folded with the proton densities.

In the actual calculation, we adopt the complex $G$ -matrix interaction MPa [44] for the effective nucleon-nucleon interaction in Eq. (2). The MPa interaction is derived from the realistic nucleon-nucleon interaction [45, 46] in the $G$ - matrix calculation. The MPa interaction satisfies the saturation property in the infinite nuclear matter by applying the three-nucleon force. Since the complex $G$ matrix is constructed for infinite nuclear matter, the strength of its imaginary part is often adjusted for the finite nucleus because their level densities are quite different. Therefore, we apply the incident-energy-dependent renormalization factor, $N _ { W } =$ $0 . 5 + ( E [ \mathrm { M e V } ] / A ) / ( 1 0 0 0 [ \mathrm { M e V } ] )$ [47], to the imaginary part. We note that no additional parameter is introduced. Consequently, once the transition densities are determined, the elastic and inelastic scattering cross sections can be uniquely calculated from the double-folding potentials. Relativistic kinematics is used.

# B. Deformed density model

For the reference calculations of inelastic scattering cross sections, we employ the deformed density (DD) model. To make the discussion clearer, we consider the deformed Fermitype (DF) density in the first-order approximation [5]:

$$
\rho_ {\mathrm {i n}} ^ {(\lambda = 0)} \left(r ^ {\prime}\right) = \sqrt {4 \pi} \rho_ {\mathrm {D F}} \left(r ^ {\prime}\right), \tag {4}
$$

$$
\rho_ {\text {i n}} ^ {(\lambda = 2)} \left(r ^ {\prime}\right) = - \delta_ {2} \frac {d \rho_ {\mathrm {D F}} \left(r ^ {\prime}\right)}{d r ^ {\prime}} \tag {5}
$$

with

$$
\rho_ {\mathrm {D F}} \left(r ^ {\prime}\right) = \frac {\rho_ {0}}{1 + \exp \left(\frac {r ^ {\prime} - R _ {0}}{a}\right)}, \tag {6}
$$

where $\rho _ { 0 }$ is the normalization constant, $R _ { 0 }$ and $a$ are the radius and the diffuseness parameters, respectively. According to Ref. [48], the intrinsic density ρ(λ)in $\rho _ { \mathrm { i n } } ^ { ( \lambda ) }$ can be transformed into $\rho _ { I ^ { \prime } I } ^ { ( \lambda ) }$ ρI ′ I in Eq. (2) as

$$
\rho_ {I ^ {\prime} I} ^ {(\lambda)} (r) = \frac {i ^ {\lambda}}{\sqrt {4 \pi}} \rho_ {\text {i n}} ^ {(\lambda)} (r) \left(I ^ {\prime} 0 \lambda 0 | I 0\right). \tag {7}
$$

Using the transition densities defined above, we calculate the inelastic scattering cross section, which is used as a reference for the following analysis.

# C. Deformed potential model

Another way of calculating inelastic scattering cross sections is based on the deformed potential (DP) model, which has been conventionally used in the analysis of experiments. The deformed potential $U _ { \mathrm { D P } } ( R , \theta ^ { \prime } )$ can be expanded as

$$
U _ {\mathrm {D P}} (R, \theta^ {\prime}) = \sum_ {\lambda} U _ {\mathrm {D P}} ^ {(\lambda)} (R) Y _ {\lambda 0} (\theta^ {\prime}), \tag {8}
$$

where U (λ) $U _ { \mathrm { D P } } ^ { ( \lambda ) }$ is the radial part of the deformed potential, $\theta ^ { \prime }$ is the direction of the target nucleus in the intrinsic frame. For

simplicity, we consider the first-order approximation of $U _ { \mathrm { D P } }$ as

$$
U _ {\mathrm {D P}} ^ {(\lambda = 0)} (R) = \sqrt {4 \pi} U (R), \tag {9}
$$

$$
U _ {\mathrm {D P}} ^ {(\lambda = 2)} (R) = - \delta_ {2} ^ {(\text {p o t})} \frac {d U (R)}{d R}, \tag {10}
$$

where $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is the potential deformation length, and $U$ is the optical potential, for which the Woods-Saxon form is often taken. In the present analysis, we apply the microscopic optical potential obtained in Eq. (2) to $U$ , i.e.,

$$
U (R) = U _ {0 0} ^ {(\lambda = 0)} (R). \tag {11}
$$

This procedure ensures a fair comparison between the DD and DP models by maintaining the common potential for the entrance channels in both models. For simplicity, the values of $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ for the real and imaginary parts are taken to be identical. Furthermore, the Coulomb coupling potential is taken to be the same as in the DD model.

# III. RESULTS

the o, , $\delta _ { 2 }$ with , an $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ or the  targe $^ { 1 2 } \mathrm { C }$ $^ { 1 2 } \mathrm { C }$ $^ { 1 6 } \mathrm { O }$ $^ { 4 0 } \mathrm { C a }$ $^ { 2 0 8 } \mathrm { { P b } }$ $E / A = 5 0 – 4 0 0 \mathrm { M e V } .$ We search for the optimal $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ so as to reproduce the inelastic scattering cross sections for the $2 _ { 1 } ^ { + }$ state of $^ { 1 2 } \mathrm { C }$ , $\sigma ( 2 _ { 1 } ^ { + } )$ , obtained in the DD model with $\delta _ { 2 }$ . For the deformed nucleus $^ { 1 2 } \mathrm { C }$ , $R _ { 0 } = 2 . 1 5 4 5 \mathrm { f m }$ , $a = 0 . 4 2 5 \mathrm { f m }$ , and $| \delta _ { 2 } | = 1 . 5 6 4 \ : \mathrm { f m }$ are employed as used in Ref. [5], which reproduce the experimental $B ( E 2 )$ value [49]. We take $\delta _ { 2 } ~ < ~ 0$ as $^ { 1 2 } \mathrm { C }$ has an oblate shape. The ground-state densities of $^ { 1 6 } \mathrm { O }$ , $^ { 4 0 } \mathrm { C a }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ are obtained from the Hartree-Fock calculations available in Ref. [50]. The nuclear excitation of doubly-magic nuclei is neglected as its effect is expected to be small. For the $^ { 1 2 } \mathrm { C } +$ $^ { 1 2 } \bar { \mathrm { C } }$ system, the symmetrization of identical particles is made but only a single (target or projectile) excitation is considered.

First, we show the validity of microscopic potentials by comparing the DD model with available experimental data for elastic scattering cross sections. Figure 1 illustrates the angular distributions of the elastic scattering cross sections for the ${ } ^ { 1 2 } \mathrm { C } + { } ^ { 1 2 } \mathrm { C }$ system at $E / A = 8 5 { - } 2 0 0 \mathrm { M e V } .$ The solid curves represent the microscopic CC calculations and reproduce the experimental data. 1 Similarly, in Fig. 2, the elastic scattering cross sections for $^ { 1 2 } \mathrm { C } + ^ { \mathrm { i } 6 } \mathrm { O }$ at $E / A = 9 4 ~ \mathrm { { M e V } }$ are also reproduced well, especially in the forward angles. We see the reliability of the diagonal potential $U _ { 0 0 } ^ { ( \lambda = 0 ) }$ used in both the DD and DP models and proceed with the present analysis.

Next, we calculate the angular-integrated inelastic scattering cross sections $\sigma ( 2 _ { 1 } ^ { + } )$ as reference calculations using the

![](images/3173480d6bf1f8f96a8ba64d0b5a7192df236a128e085e134227ec8f0bc19a4f.jpg)  
FIG. 1: Angular distributions of elastic scattering for the ${ } ^ { 1 2 } \mathrm { C } + { } ^ { 1 2 } \mathrm { C }$ system at $E / A = 8 5 { - } 2 0 0 \mathrm { M e V } .$ . The experimental data are taken from Refs. [35, 36, 51–53].

![](images/946b97c2b4d4519030c65947642efab3c1d1515e9ec34127900ccb58624090e6.jpg)  
FIG. 2: Angular distributions of elastic scattering for the $^ { 1 2 } \mathrm { C } + ^ { 1 6 } \mathrm { O }$ system at $E / A = 9 4 ~ \mathrm { { M e V } } .$ . The experimental data are taken from Ref. [54].

DD model. Figure 3 shows the $\sigma ( 2 _ { 1 } ^ { + } )$ for $^ { 1 2 } \mathrm { C }$ scattering by the $^ { 1 2 } \mathrm { C }$ , $^ { 1 6 } \mathrm { O }$ , $^ { 4 0 } \mathrm { C a }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ targets at $E / A = 5 0 – 4 0 0 \mathrm { M e V } .$ The filled circles, open triangles, open squares, and open circles correspond to the reactions by $^ { \mathrm { { \bar { 1 } 2 } } } \mathrm { C } { . }$ , $^ { 1 \bar { 6 } } \mathrm { O }$ , $^ { 4 0 } \mathrm { C a }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ targets, respectively. The $\sigma ( 2 _ { 1 } ^ { + } )$ rapidly decreases as the incident energy increases up to $E / \dot { A } \lesssim 2 0 0 \mathrm { M e V } .$ . We find that, in the

![](images/91b2beaa268a8fe8ade2134c709ff1d7a84602a61aa7364485987345db2bf9d3.jpg)  
FIG. 3: Angular-integrated inelastic scattering cross sections for the $2 _ { 1 } ^ { + }$ state of the $^ { 1 2 } \mathrm { C }$ nucleus $[ \sigma ( 2 _ { 1 } ^ { + } ) ]$ by the $^ { 1 2 } \mathrm { C }$ (filled circles), $^ { 1 6 } \mathrm { O }$ (open triangles), $^ { 4 0 } \mathrm { C a }$ (open squares), and $^ { 2 0 8 } \mathrm { { P b } }$ (open circles) targets at incident energies $E / A = 5 0 – 4 0 0 \mathrm { M e V } .$ These results are obtained from the DD model and used as reference calculations for determining δ(pot)2 i $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ n the DP model.

low-energy region $( E / A \lesssim 1 0 0 \mathrm { M e V } )$ , the real part of the coupling potentials plays a decisive role in determining the $\sigma ( 2 _ { 1 } ^ { + } )$ because the imaginary part is relatively small. The strength of the real part becomes weaker as the energy increases; it is noteworthy that the real part of the diagonal potential shows the repulsive nature at $E / A \sim 2 0 0 \mathrm { M e V } .$ Beyond this energy $( E / A \gtrsim 2 5 0 \mathrm { M e V } )$ , the $\sigma ( 2 _ { 1 } ^ { + } )$ exhibits a weaker dependence on the incident energy. In the high-energy region, the imaginary part of the coupling potentials plays a major role in the $\sigma ( 2 _ { 1 } ^ { + } )$ values. We find that the contribution of the imaginary part to $\sigma ( 2 _ { 1 } ^ { + } )$ is almost constant in the energy range of our analysis $( 5 0 ~ \dot { \le } ~ E / A ~ \le ~ 4 0 0 ~ \mathrm { M e V } )$ . It should be noted that the $\sigma ( 2 _ { 1 } ^ { + } )$ for $^ { 1 2 } \mathrm { C } + ^ { 1 2 } \mathrm { C }$ scattering is relatively large although the target mass is the smallest. This is because the symmetrization procedure involving the single excitation is taken into account for this system. These theoretical results are used as reference calculations for determining $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ in the DP model.

For ${ } ^ { 1 2 } \mathrm { C } + { } ^ { 1 2 } \mathrm { C }$ inelastic scattering at $E / A \sim 1 0 0 \mathrm { M e V } ,$ several experimental data are available. At $E / A = 1 2 1 . 1 \mathrm { M e V } ,$ our calculation of $\sigma _ { \mathrm { t h e o } } ( 2 _ { 1 } ^ { + } ) = 2 7 ~ \mathrm { m b }$ underestimates the observed data of $\sigma _ { \mathrm { e x p } } ( 2 _ { 1 } ^ { + } ) \stackrel { - } { = } 4 3 \pm 3 ~ \mathrm { n }$ mb [55, 56]. Conversely, for the angular distribution $d \sigma ( 2 _ { 1 } ^ { + } ) / d \Omega$ at $E / A = 1 0 0 ~ \mathrm { M e V } ,$ our result tends to overestimate the experimental data as was also shown in Refs. [35, 36], which employed a similar reaction model. This discrepancy highlights the need for further investigations. Measurements of inelastic cross sections for heavy-ion scattering could provide crucial insights for the quantitative refinement of microscopic potentials.

Figure 4 illustrates the energy dependence of $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ derived from the $\sigma ( 2 _ { 1 } ^ { + } )$ calculated with the DD model. Note that the values of δ(pot) $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ are divided by $\delta _ { 2 }$ . The filled circles, open triangles, open squares, and open circles represent the results for the scattering of $^ { 1 2 } \mathrm { C }$ by $^ { 1 \bar { 2 } } \mathrm { C }$ , $^ { 1 6 } \mathrm { O }$ , $^ { 4 0 } \mathrm { C a }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ targets, respectively. Our primary finding is that $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ gets overall un-

![](images/9dbbece38b036eae11479b76c70f395b8f9120e1a73d5719101c9c8676469f5a.jpg)  
FIG. 4: Deformation length of the nuclear potential $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ derived from $^ { 1 2 } \mathrm { C }$ inelastic scattering cross sections at $E / A = 5 0 – 4 0 0 \ \mathrm { M e V } ,$ divided by $\delta _ { 2 } = - 1 . 5 6 4 \ : \mathrm { f m }$ . The filled circles, open triangles, open squares, and open circles represent the results for the scattering by $^ { 1 2 } \mathrm { { C } , ^ { 1 6 } \mathrm { { O } , ^ { 4 0 } \mathrm { { C a } } } }$ , and $^ { 2 0 8 } \mathrm { { P b } }$ targets, respectively.

derestimation, which is approximately $20 \%$ smaller than $\delta _ { 2 }$ , and shows strong incident energy and target dependence. The $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ values become smaller as the target mass increases. We confirmed that this behavior is kept even when the folding potential for the elastic channel $[ \bar { U } _ { 0 0 } ^ { ( \lambda = 0 ) }$ in Eq. (11)] is replaced with a phenomenological Woods-Saxon potential that is determined to reproduce the elastic scattering cross section calculated with the DD model. This significant deviation casts doubt on the determination of $\delta _ { 2 }$ with $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ from the highenergy heavy-ion scattering. A systematic underestimation of the quadrupole deformation length is expected in studies based on the DP model that assumes $\delta _ { 2 } = \delta _ { 2 } ^ { ( \mathrm {bar { p o t } } ) }$ .

![](images/b0ac4f70b116ef5a964e4228358b3549cd6ade42a31eb2bc1bd1a45c8bd9c10f.jpg)  
FIG. 5: Same as Fig. 4 but $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is extracted from the DP2 model.

Lastly, we investigate the higher-order effect of δ(pot)2 $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ on the form factor ${ U _ { \mathrm { D P } } ^ { ( \lambda = 2 ) } ( R ) }$ beyond the derivative form given DP in Eq. (10), because the extracted $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is relatively large $( | \delta _ { 2 } ^ { ( \mathrm { p o t } ) } | \ \sim \ 1 . 1 \ \mathrm { f m } )$ 2. In considering the folding potential, we

modify the optical potential as

$$
U _ {\mathrm {D P 2}} \left(R, \theta^ {\prime}\right) = U \left(R - \delta_ {2} ^ {(\mathrm {p o t})} Y _ {2 0} \left(\theta^ {\prime}\right)\right), \tag {12}
$$

where $U$ is the arbitrary optical potential [Eq. (11)], and the subscript “DP2” denotes the deformed potential 2 model, which is distinguished from the DP (derivative) model. This method is commonly used, for example, in FRESCO [57]. Following Eq. (16) of Ref. [58], we further define the form factor in the DP2 model

$$
U _ {\mathrm {D P 2}} ^ {(\lambda = 2)} (R) = 4 \pi \int_ {0} ^ {1} U _ {\mathrm {D P 2}} \left(R, \theta^ {\prime}\right) Y _ {2 0} \left(\theta^ {\prime}\right) d \left(\cos \theta^ {\prime}\right). \tag {13}
$$

In the present analysis, we assume the monopole part as $U _ { \mathrm { D P 2 } } ^ { ( \lambda = 0 ) } ( \bar { R } ) = \sqrt { 4 \pi } U ( \bar { R } )$ UDP2 to maintain the consistency of the DD and DP models. Note that Eq. (13) reduces to Eq. (10) when $| \delta _ { 2 } ^ { ( \mathrm { p o t } ) } |$ is small. Figure 5 shows $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ extracted using the DP2 model, where the values of $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ are divided by $\delta _ { 2 }$ as in Fig. 4. The overall trend is the same as Fig. 4 but the ratios are increased by $6- 9 \%$ from the DP model. This discrepancy arises only from U(λ=2), $U _ { \mathrm { D P 2 } } ^ { ( \lambda = 2 ) }$ whose peak position slightly shifts inward for larger δ(pot) $| \delta _ { 2 } ^ { ( \mathrm { p o t } ) } |$ compared to U(λ=2). This behavior results $U _ { \mathrm { D P } } ^ { ( \lambda = 2 ) }$ in smaller $\sigma ( 2 _ { 1 } ^ { + } )$ for the same value of $| \delta _ { 2 } ^ { ( \mathrm { p o t } ) } |$ , leading to the extraction of larger $| \delta _ { 2 } ^ { ( \mathrm { p o t } ) } |$ in the DP2 model. However, the extracted δ(pot)2 $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ remains $1 5 \mathrm { - } 3 5 \ \%$ smaller than $\delta _ { 2 }$ , indicating significant underestimation even in the DP2 model.

# IV. CONCLUSION

We have investigated the relation between the quadrupole deformation lengths of the nuclear density and potential ( $\phantom { + } \delta _ { 2 }$ and $\delta _ { 2 } ^ { ( \mathrm { p o t } ) } ,$ for the $^ { 1 2 } \mathrm { C }$ inelastic scattering by the $^ { 1 2 } \mathrm { C }$ , $^ { 1 6 } \mathrm { O }$ , $^ { 4 0 } \mathrm { C a }$ and $^ { 2 0 8 } \mathrm { { P b } }$ targets at $E / A = 5 0 – 4 0 0 \ \mathrm { M e V } .$ For this analysis, we employ two models: the deformed density (DD) model and the deformed potential (DP) model. In the DD model, the coupling potential is microscopically constructed from the transition density based on the deformed density characterized by $\delta _ { 2 }$ . In the DP model, the coupling potential is derived based on the deformed potential characterized by $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ , which is determined to reproduce the inelastic scattering cross section calculated with the DD model. We find that $\bar { \delta } _ { 2 } ^ { ( \mathrm { p o t } ) }$ shows overall underestimation of $\delta _ { 2 }$ by $20 \%$ , having strong incident energy and target dependence. Further analysis using the DP2 model, which considers higher-order deformation effects beyond the DP (derivative) model, reveals that $\delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is still about $1 5 \mathrm { - } 3 5 \%$ smaller than $\delta _ { 2 }$ . These results clearly indicate that the assumption $\delta _ { 2 } = \delta _ { 2 } ^ { ( \mathrm { p o t } ) }$ is too naive for the determination of the nuclear deformation using the high-energy heavy-ion scattering in the DP model.

# Acknowledgments

This work was supported by Research Network Support Program, National Institute of Technology (KOSEN) and

Japan Society for the Promotion of Science (JSPS) KAK-ENHI Grants No. JP18K03635, No. JP20K03943, No. JP21K03543, No. JP22K03610, No. JP22K14043, No. JP22H01214, and No. JP23K22485. One of the authors, S.W.,

thanks A. M. Moro and the faculty and staff at Universidad de Sevilla for their hospitality during his sabbatical stay, which enabled the completion of this work.

[1] A. Bohr and B. R. Mottelson, Nuclear Structure (World Scientific, Singapore, 1998).   
[2] G. R. Satchler, Direct Nuclear Reactions (Oxford University, Oxford, 1983).   
[3] S. Matsuki, T. Higo, T. Ohsawa, T. Shiba, T. Yanabu, K. Ogino, Y. Kadota, K. Haga, N. Sakamoto, K. Kume, et al., Phys. Rev. Lett. 51, 1741 (1983).   
[4] G. Haouat, C. Lagrange, R. de Swiniarski, F. Dietrich, J. P. Delaroche, and Y. Patin, Phys. Rev. C 30, 1795 (1984).   
[5] D. T. Khoa and G. R. Satchler, Nucl. Phys. A668, 3 (2000).   
[6] H. Iwasaki, T. Motobayashi, H. Akiyoshi, Y. Ando, N. Fukuda, H. Fujiwara, Z. F ¨ul ¨op, K. I. Hahn, Y. Higurashi, M. Hirai, et al., Phys. Lett. B481, 7 (2000).   
[7] S. Takeuchi, N. Aoi, T. Motobayashi, S. Ota, E. Takeshita, H. Suzuki, H. Baba, T. Fukui, Y. Hashimoto, K. Ieki, et al., Phys. Rev. C 79, 054319 (2009).   
[8] J.-Y. Lee, I. Hahn, Y. Kim, S.-W. Hong, S. Chiba, and E. S. Soukhovitskii, Phys. Rev. C 79, 064612 (2009).   
[9] H. A. Falou, R. Kanungo, C. Andreoiu, D. S. Cross, B. Davids, M. Djongolov, A. T. Gallant, N. Galinski, D. Howell, R. Kshetri, et al., Phys. Lett. B721, 224 (2013).   
[10] S. Michimasa, Y. Yanagisawa, K. Inafuku, N. Aoi, Z. Elekes, Z. F ¨ul ¨op, Y. Ichikawa, N. Iwasa, K. Kurita, M. Kurokawa, et al., Phys. Rev. C 89, 054307 (2014).   
[11] B. Canbula, D. Canbula, and H. Babacan, Phys. Rev. C 91, 044615 (2015).   
[12] P. Doornenbal, H. Scheit, S. Takeuchi, N. Aoi, K. Li, M. Matsushita, D. Steppenbeck, H. Wang, H. Baba, E. Ideguchi, et al., Phy. Rev. C 93, 044306 (2016).   
[13] A. Kundu, S. Santra, A. Pal, D. Chattopadhyay, T. N. Nag, R. Gandhi, P. C. Rout, B. J. Roy, B. K. Nayak, and S. Kailas, Phys. Rev. C 100, 024614 (2019).   
[14] Y. Jiang, J. L. Lou, Y. L. Ye, Y. Liu, Z. W. Tan, W. Liu, B. Yang, L. C. Tao, K. Ma, Z. H. Li, et al., Phys. Rev. C 101, 024601 (2020).   
[15] M. Holl, R. Kanungo, Z. Sun, G. Hagen, J. Lay, A. M. Moro, P. Navr´atil, T. Papenbrock, M. Alcorta, D. Connolly, et al., Phys. Lett. B822, 136710 (2021).   
[16] J. Chen, B. P. Kay, T. L. Tang, I. A. Tolstukhin, C. R. Hoffman, H. Li, P. Yin, X. Zhao, P. Maris, J. P. Vary, et al., Phys. Rev. C 106, 064312 (2022).   
[17] K. Kundalia, D. Gupta, S. M. Ali, S. K. Saha, O. Tengblad, J. D. Ovejas, A. Perea, I. Martel, J. Cederkall, J. Park, et al., Phys. Lett. B833, 137294 (2022).   
[18] P. Doornenbal, S. Takeuchi, N. Aoi, M. Matsushita, A. Obertelli, D. Steppenbeck, H. Wang, L. Audirac, H. Baba, P. Bednarczyk, et al., Phys. Rev. C 90, 061302(R) (2014).   
[19] K. Li, Y. Ye, T. Motobayashi, H. Scheit, P. Doornenbal, S. Takeuchi, N. Aoi, M. Matsushita, E. Takeshita, D. Pang, et al., Phys. Rev. C 92, 014608 (2015).   
[20] V. Vaquero, A. Jungclaus, P. Doornenbal, K. Wimmer, A. M. Moro, K. Ogata, T. Furumoto, S. Chen, E. N´acher, E. Sahin, et al., Phys. Rev. C 99, 034306 (2019).   
[21] K. Wimmer, W. Korten, P. Doornenbal, T. Arici, P. Aguilera, A. Algora, T. Ando, H. Baba, B. Blank, A. Boso, et al., Phys.

Rev. Lett. 126, 072501 (2021).   
[22] A. Revel, J. Wu, H. Iwasaki, J. Ash, D. Bazin, B. Brown, J. Chen, R. Elder, P. Farris, A. Gade, et al., Phys. Lett. B838, 137704 (2023).   
[23] G. R. Satchler and W. G. Love, Phys. Rep. 55, 184 (1979).   
[24] Y. Sakuragi, M. Yahiro, and M. Kamimura, Prog. Theor. Phys. Suppl. 86, 136 (1986).   
[25] G. R. Satchler and D. T. Khoa, Phys. Rev. C 55, 285 (1997).   
[26] M. Katsuma, Y. Sakuragi, S. Okabe, and Y. Kondo, Prog. Theor. Phys. 107, 377 (2002).   
[27] D. T. Khoa, E. Khan, G. Colo, and N. V. Giai, Nucl. Phys. A706, 61 (2002).   
[28] D. T. Khoa, H. G. Bohlen, W. von Oertzen, G. Bartnitzky, A. Blazevic, F. Nuoffer, B. Gebauer, W. Mitting, and P. Roussel-Chomaz, Nucl. Phys. A759, 3 (2005).   
[29] T. Furumoto, T. Suhara, and N. Itagaki, Phys. Rev. C 87, 064320 (2013).   
[30] T. Furumoto, T. Suhara, and N. Itagaki, Phys. Rev. C 97, 044602 (2018).   
[31] T. Furumoto and M. Takashina, Phys. Rev. C 103, 044602 (2021).   
[32] T. Furumoto, T. Suhara, and N. Itagaki, Phys. Rev. C 104, 034613 (2021).   
[33] K. Minomo and K. Ogata, Phys. Rev. C 93, 051601(R) (2016).   
[34] M. Takashina, T. Furumoto, and Y. Sakuragi, Phys. Rev. C 81, 047605 (2010).   
[35] W. W. Qu, G. L. Zhang, S. Terashima, T. Furumoto, Y. Ayyad, Z. Q. Chen, C. L. Guo, A. Inoue, X. Y. Le, H. J. Ong, et al., Phys. Lett. B751, 1 (2015).   
[36] W. W. Qu, G. L. Zhang, S. Terashima, T. Furumoto, Y. Ayyad, Z. Q. Chen, C. L. Guo, A. Inoue, X. Y. Le, H. J. Ong, et al., Phys. Rev. C 95, 044616 (2017).   
[37] T. Furumoto, Y. Sakuragi, and Y. Yamamoto, Phys. Rev. C 82, 044612 (2010).   
[38] T. Furumoto and Y. Sakuragi, Phys. Rev. C 87, 014618 (2013).   
[39] J. R. Beene, D. J. Horen, and G. R. Satchler, Nucl. Phys. A596, 137 (1996).   
[40] M. Ito, Y. Sakuragi, and Y. Hirabayashi, Phys. Rev. C 63, 064303 (2001).   
[41] T. Furumoto, Y. Sakuragi, and Y. Yamamoto, Phys. Rev. C 80, 044614 (2009).   
[42] D. T. Khoa, W. von Oertzen, H. G. Bohlen, and S. Ohkubo, J. Phys. G: Nucl. Part. Phys. 34, R111 (2007).   
[43] T. Furumoto, Y. Sakuragi, and Y. Yamamoto, Phys. Rev. C 94, 044620 (2016).   
[44] Y. Yamamoto, T. Furumoto, N. Yasutake, and T. A. Rijken, Phys. Rev. C 90, 045805 (2014).   
[45] T. A. Rijken, Phys. Rev. C 73, 044007 (2006).   
[46] T. A. Rijken and Y. Yamamoto, Phys. Rev. C 73, 044008 (2006).   
[47] T. Furumoto, K. Tsubakihara, S. Ebata, and W. Horiuchi, Phys. Rev. C 99, 034605 (2019).   
[48] M. Kamimura, Nucl. Phys. A351, 456 (1981).   
[49] S. Raman, C. Nestor, and P. Tikkanen, Atomic Data and Nuclear Data Tables 78, 1 (2001).   
[50] J. W. Negele, Phys. Rev. C 1, 1260 (1970).

[51] M. Buenerd, J. Pinston, J. Cole, C. Guet, D. Lebrun, J. M. Loiseaux, P. Martin, E. Monnand, J. Mougey, H. Nifenecker, et al., Phys. Lett. 102B, 242 (1981).   
[52] T. Ichihara, M. Ishihara, H. Ohmura, T. Niizeki, Y. Tajima, Y. Yamamoto, Y. Fuchi, S. Kubono, M. H. Tanaka, H. Okamura, et al., Phys. Lett. B323, 278 (1994).   
[53] J. Y. Hostachy, M. Buenerd, J. Chauvin, D. Lebrun, P. Martin, B. Bonin, G. Bruge, J. C. Lugol, L. Papineau, P. Roussel, et al., Phys. Lett. B184, 139 (1987).   
[54] P. Roussel-Chomaz, N. Alamanos, F. Auger, J. Barrette,

B. Berthier, B. Fernandez, and L. Papineau, Nucl. Phys. A477, 345 (1988).   
[55] M. Takechi, M. Fukuda, M. Mihara, K. Tanaka, T. Chinda, T. Matsumasa, M. Nishimoto, R. Matsumiya, Y. Nakashima, H. Matsubara, et al., Phys. Rev. C 79, 061601(R) (2009).   
[56] URL http://www-nds.iaea.org/EXFOR/E2149.007.   
[57] I. J. Thompson, Comp. Phys. Rep. 7, 167 (1988).   
[58] T. Tamura, Rev. Mod. Phys. 37, 679 (1965).