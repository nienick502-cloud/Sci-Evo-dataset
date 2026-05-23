# Deep learning for nuclear masses in deformed relativistic Hartree-Bogoliubov theory in continuum

Soonchul Choi,1 Kyungil Kim,2 Zhenyu He,3 Youngman Kim,1, 3, ∗ and Toshitaka Kajino3, 4, 5

$^ { 1 }$ Center for Exotic Nuclear Studies, Institute for Basic Science, Daejeon 34126, Korea

2Institute for Rare Isotope Science, Institute for Basic Science, Daejeon 34000, Korea

$^ 3$ School of Physics, International Research Center for Big-Bang Cosmology and Element Genesis,

Peng Huanwu Collaborative Center for Research and Education, Beihang University, Beijing 100191, China

$^ 4$ National Astronomical Observatory of Japan, Mitaka, Tokyo, 181-8588, Japan

$^ { 5 }$ Graduate School of Science, The University of Tokyo, Hongo, Tokyo, 113-033, Japan (Dated: December 2, 2024)

Most nuclei are deformed, and these deformations play an important role in various nuclear and astrophysical phenomena. Microscopic nuclear mass models have been developed based on covariant density functional theory to explore exotic nuclear properties. Among these, we adopt mass models based on the relativistic continuum Hartree-Bogoliubov theory (RCHB) with spherical symmetry and the deformed relativistic Hartree-Bogoliubov theory in continuum (DRHBc) with axial symmetry to study the effects of deformation on the abundances produced during the rapid neutron-capture process (r-process).

Since the DRHBc mass table has so far been completed only for even-Z nuclei, we first investigate whether a Deep Neural Network (DNN) can be used to extend the DRHBc mass table by focusing on nuclear binding energies. To incorporate information about odd-odd and odd-even isotopes into the DNN, we also use binding energies from AME2020 as a training set, in addition to those from the DRHBc mass table for even-Z nuclei. After generating an improved mass table through the DNN study, we conduct a sensitivity analysis of r-process abundances to deformation or mass variations using the RCHB $\star$ and DRHBc $\star$ mass tables (where $\star$ indicates that the mass table is obtained from the DNN study). For the r-process sensitivity study, we consider magnetohydrodynamic jets and collapsar jets. Our findings indicate that r-process abundances are sensitive to nuclear deformation, particularly within the mass range of $A = 8 0 - 1 2 0$ .

# I. INTRODUCTION

The mass of a nucleus is one of the fundamental nuclear properties, and as is well known it is not just the sum of its constituent nucleon masses. The nuclear mass is a basic observable to dissect theoretically internal structures of a nucleus such as deformations and paring gaps. It is also essential to determine the Q-value for nuclear reactions in astrophysical environments and so important to understand the origin of the elements [1]. The production of elements up to iron, as well as about half of the elements heavier than iron, is reasonably well explained by processes such as Big Bang nucleosynthesis and slow neutron capture. The other half of the heavy elements in the universe is attributed to the r-process. For a recent review of the r-process, we refer to Refs. [2–5]. The sensitivity of the r-process nucleosynthesis to nuclear masses has been extensively studied, see Refs. [6, 7] for a review and Refs. [8–10] for some recent works.

Many efforts have been made to theoretically develop a reliable global nuclear mass model: e.g. finite-range droplet model (FRDM) [11], Weiz¨sacker-Skyrme (WS) model [12] and Hartree-Fock-Bogoliubov method based on non-relativistic density functional theory [13–15].

Relativistic density functional theory has also been developed for nuclear properties with much success. To accurately capture the characteristics of loosely bound nuclei, it is crucial to treat pairing correlations and continuum effects in a self-consistent manner, as the Fermi energy of such nuclei is typically close to the continuum threshold. This feature was successfully implemented in the relativistic continuum Hartree-Bogoliubov (RCHB) theory [16–20] with the point coupling density functional, PC-PK1 [21], where the Dirac equations are solved by the shooting method in the coordinate space.

Nuclear deformations are common across most nuclei, particularly in exotic ones. To accurately describe deformed nuclei, the RCHB theory was extended to the deformed relativistic Hartree-Bogoliubov theory in the continuum (DRHBc) with meson-exchange interactions [22, 23], where the deformed relativistic Hartree-Bogoliubov equations are solved in a Dirac Woods-Saxon basis. DRHBc with contact interactions was developed, and its application to even-even nuclei was discussed in detail in Ref. [24]; recently, it is extended further to odd-A and odd-odd nuclei [25]. A difference in the parameters between DRHBc and RCHB is the paring strength. The pairing strength in DRHBc is−325.0 MeV fm3 and that in RCHB is −342.5 MeV fm3. DRHBc with PC-PK1 has been applied to investigate various exotic nuclear properties [26–34] and mass tables for even Z - even N [37] and for even-odd [38]. Here ”Z” and ”N” denote the proton and neutron numbers in a nucleus. As summarized in Table 1 of Ref. [38], for the even-Z nuclei the DRHBc mass table achieved the root-mean-square deviation (RMS) 1.433 MeV with respect to the AME2020 data [39] among nonrelativistic and relativistic microscopic density functional calculations; for example the nonrelativistic Hartree-Fock-Bogoliubov (HFB) theory with the UNEDF1 density functional obtained the rms deviation of 1.934 MeV which is the smallest rms deviation among the HFB theory with various density functionals. Since the main difference between RCHB and DRHBc is deformations which lead to different mass predictions for deformed nuclei, it will be interesting to investigate the sensitivity of the r-process abundances to nuclear deformations or masses. However, so far the DRHBc mass table is completed only for even-even and even-odd nuclei.

In this work, we first predict the masses of the odd-odd and odd-even nuclei using a deep neural network (DNN). For a recent study on the machine learning applied to the nuclear masses we refer to Refs. [40–51] and Refs. [52, 53] for a recent review. To validate the performance of the DNN in the present study, we first use the RCHB data and AME2020 [39] as a training data set. When we use the RCHB data, we exclude odd-Z data to see if the neural network system can learn about odd-Z information from the AME2020 data. After training, we compare the predicted data with AME2020 and also with RCHB combined with AME2020 data sets and obtain the RMS deviations of 1.599 MeV and 2.457 MeV, respectively. When the original RCHB mass table was compared with AME2020, the RMS deviation was 7.980 MeV. Though we have used AME2020 as a training set, it is a substantial improvement. We then apply the same method to the DRHBc case.

Finally, we calculate the r-process abundances by using some part of the RCHB $\star$ and DRHBc $\star$ mass tables, where the mass difference exceeds 5 MeV, in astrophysical sites of the r-process: magnetohydrodynamic (MHD) jets and collapsars.

# II. NEURAL NETWORK MODEL

In this study, we use a deep neural network (DNN) consisting of the first hidden layer, intermediate hidden layer, last hidden layer and output layer. The relations between the inputs and each layer are as follows:

With the first hidden layer, the relation is given by

$$
a _ {j} ^ {(1)} = E \left(\sum_ {i = 1} ^ {n} w _ {i j} ^ {(1)} x _ {i} + b _ {j} ^ {(1)}\right), \tag {1}
$$

with the intermediate hidden layer $l = 2 , 3 , . . . , j - 1$

$$
a _ {j} ^ {l} = E \left(\sum_ {i = 1} ^ {k} w _ {i j} ^ {l} a _ {i} ^ {l - 1} + b _ {j} ^ {l}\right), \tag {2}
$$

with the last hidden layer

$$
a _ {j} ^ {j} = E \left(\sum_ {i = 1} ^ {k} w _ {i j} ^ {j} a _ {i} ^ {j - 1} + b _ {j} ^ {j}\right) \tag {3}
$$

and with the output layer

$$
z _ {\text {o u t}} ^ {j + 1} = \sum_ {i = 1} ^ {k} w _ {i \text {o u t}} ^ {j + 1} a _ {i} ^ {j} + b _ {\text {o u t}} ^ {j + 1}. \tag {4}
$$

Here $x _ { i } , w _ { i j } ^ { l } , b _ { j } ^ { l } , a _ { j } ^ { l }$ , and $z _ { \mathrm { o u t } }$ are the input data, the weight from a node $i$ in a layer ${ \mathit { l } } - 1$ to a node $j$ in a layer $\it { \Delta } l$ , biases for a node $j$ in a layer $\it { \Delta } l$ , outputs of a node $j$ in a layer $\it { \Delta } l$ and output of the output layer, respectively. In the above relations, $E$ is the Elu function employed as the activation function [35],

$$
E (x) = x \quad x \geq 0,
$$

$$
E (x) = \alpha \left(e ^ {x} - 1\right) \quad x <   0, \tag {5}
$$

where $\alpha = 1$ .

The inputs of the neutral network are the proton number ( $Z$ ), neutron number ( $N$ ), nuclear pairing (δ) and shell effect ( $P$ ). $\delta$ is defined by $\delta = [ ( - 1 ) ^ { Z } + ( - 1 ) ^ { N } ] / 2$ , and $P$ is given by

$$
P = \frac {\nu_ {p} \nu_ {n}}{\nu_ {p} + \nu_ {n}}, \tag {6}
$$

Here, and are the differences between the actual nucleon numbers $Z$ and $N$ and the nearest magic numbers [54]. $\nu _ { p }$ $\nu _ { n }$ The value of $\nu _ { p }$ and $\nu _ { n }$ is zero at a closed shell and reaches a maximum at the mid-shell. When one considers the shell effect differently for protons and neutrons, one can use $P _ { n } = \nu _ { n }$ and $P _ { p } = \nu _ { p }$ [48].

In this study we consider three cases with different inputs: two-inputs $( Z , N )$ , four-inputs $( Z , N , \delta , P )$ , five-inputs $( Z , N , \delta , P _ { n } , P _ { p } )$ . We remark here that we also investigated the case with different pairing parameters for the proton and neutron and found that the results do not improve. We use the root-mean-square (RMS) as the objective function $\sigma$ ,

$$
\sigma = \sqrt {\sum_ {i} ^ {n} \frac {\left(E _ {i} ^ {\mathrm {t r a i n e d}} - E _ {i} ^ {\mathrm {r e f}}\right) ^ {2}}{n}}, \tag {7}
$$

where $n$ is the number of data. Here $E _ { i } ^ { \mathrm { r e t } }$ denotes the binding available binding energies from AME2020, DRHBc and RCHB.

To obtain the odd-even and odd-odd binding energies using a deep neural network, the binding energies of even-even and even-odd isotopes from DRHBc calculations are used as a training set. In addition, to include information about odd-odd and odd-even isotopes to the deep neural network system we also use the binding energies in AME2020 [39] as a training set. In case the binding energy of an isotope is available in both DRHBc and AME2020, we take the value from AME2020. In a DNN study, in general one divides the available data into training, validation and test data sets. In this work since we have no available data for odd-odd and odd-even nuclei in the DRHBc results, we perform our DNN study as follows. We first consider the RCHB and AME2020 data. Though the binding energies of the odd-odd and odd-even isotopes are available in RCHB, we use the AME2020 data and even-Z results of RCHB to train the DNN system and predict the whole mass table from Z=8 to 120. We then evaluate the RMS deviations to judge if our DNN system predicts the binding energies reliably. If this procedure works, we do the same study with DRHBc.

Now, we use the RCHB data and AME2020 [39] as a training data set. When we employ the RCHB data, we exclude odd-Z data to see if the neural network systems can learn about odd-Z information from the AME2020 data. After training with the five inputs, the predicted data are compared with both AME2020 and RCHB combined with AME2020 data sets and the corresponding RMS deviations are 1.862 MeV and 1.957 MeV, respectively. When the original RCHB mass table was compared with AME2020, the RMS deviation was 7.980 MeV. Though we use AME2020 as a training set, it is a substantial improvement. This successful method is then applied to the DRHBc case.

<table><tr><td></td><td>Two-inputs</td><td>Four-inputs</td><td>Five-inputs</td></tr><tr><td>RMS deviation (RCHB*)</td><td>1.779</td><td>1.584</td><td>1.862</td></tr><tr><td>RMS deviation (DRHBC*)</td><td>1.747</td><td>1.541</td><td>0.842</td></tr></table>

TABLE I. The RMS deviations between AME2020 [39] and predicted masses in units of MeV.   
TABLE II. The mass excess of the newly measured isotopes [55] compared with that of the calculated ones in DRHBc $\star$ in units of keV.   

<table><tr><td></td><td>Exp</td><td>DRHBe*</td><td></td><td>Exp</td><td>DRHBe*</td></tr><tr><td>82Ge</td><td>-65413.7</td><td>-66241.4</td><td>86Br</td><td>-75638.4</td><td>-75753.7</td></tr><tr><td>82As</td><td>-70107.2</td><td>-71057.0</td><td>87As</td><td>-55617.8</td><td>-56543.6</td></tr><tr><td>82Se</td><td>-77589.8</td><td>-78087.6</td><td>87Se</td><td>-66425.3</td><td>-66893.0</td></tr><tr><td>88Se</td><td>-63882.5</td><td>-64558.6</td><td>88As</td><td>-50677.8</td><td>-51316.9</td></tr><tr><td>83Ga</td><td>-49260.8</td><td>-49916.4</td><td>89As</td><td>-46686.5</td><td>-48107.6</td></tr><tr><td>83Ge</td><td>-60975.6</td><td>-61449.0</td><td>89Se</td><td>-58989.4</td><td>-59523.4</td></tr><tr><td>83As</td><td>-69670.0</td><td>-70609.5</td><td>89Br</td><td>-68275.0</td><td>-69105.2</td></tr><tr><td>84Ga</td><td>-44088.5</td><td>-44293.8</td><td>89Kr</td><td>-76537.0</td><td>-76086.8</td></tr><tr><td>84Ge</td><td>-58148.0</td><td>-58600.7</td><td>90Se</td><td>-55881.3</td><td>-56777.5</td></tr><tr><td>84As</td><td>-65853.5</td><td>-66646.1</td><td>90Br</td><td>-63998.8</td><td>-64679.2</td></tr><tr><td>84Se</td><td>-75952.5</td><td>-76627.1</td><td>90Rb</td><td>-79352.3</td><td>-79180.9</td></tr><tr><td>85Ge</td><td>-53116.2</td><td>-53231.4</td><td>91Se</td><td>-50267.4</td><td>-51382.0</td></tr><tr><td>85As</td><td>-63196.4</td><td>-64369.0</td><td>91Br</td><td>-61106.8</td><td>-62240.5</td></tr><tr><td>85Se</td><td>-72415.9</td><td>-72619.9</td><td>91Kr</td><td>-70971.1</td><td>-71101.7</td></tr><tr><td>85Br</td><td>-78599.0</td><td>-79468.2</td><td>91Rb</td><td>-77760.6</td><td>-77942.6</td></tr><tr><td>86Ge</td><td>-49596.7</td><td>-49951.6</td><td>92Br</td><td>-56240.5</td><td>-57256.0</td></tr><tr><td>86As</td><td>-58964.6</td><td>-59529.7</td><td>92Kr</td><td>-68772.0</td><td>-69465.0</td></tr><tr><td>86Se</td><td>-70503.5</td><td>-71228.0</td><td></td><td></td><td></td></tr></table>

# III. DNN RESULTS

Before we perform a sample mass sensitivity study in r-abundances, we present our results from the DNN study.

In Table I, we show the RMS deviation of RCHB $\star$ and DRHBc $\star$ compared with the AME2020 data sets, where it can be seen that the case with the five-inputs results in the smallest RMS deviation (0.842 MeV) for DRHBc $\star$ . For comparison, the RMS deviation between AME2020 and the even-Z DRHBc $\star$ mass table is 1.433 MeV. Therefore, we present our results with the five-inputs. We remark here again that to obtain RCHB $\star$ we don’t use odd-Z information from RCHB.

In Table II, we compare the masses of the newly measured neutron-rich isotopes in Ref. [55], where the masses of 88,89As were measured for the first time, with our results in DRHBc $\star$ and obtain the RMS deviation of 0.725 MeV. This deviation is a bit improved compared with 0.842 MeV in Table I, which indicates that DRHBc $\star$ (and also DRHBc) may work better for exotic nuclei.

Figure 1 shows the one-neutron separation energy Sn of a few selected isotopes from DRHBc and DRHBc⋆ compared with the experiments. Our results exhibit, as expected, an odd-even staggering. It can be seen from Fig. 1 that our results from DRHBc $\star$ agree with the available experimental data.

To perform a sample sensitivity study of the r-process abundances to nuclear deformations (or masses) using the RCHB $\star$ and DRHBc $\star$ data, we select a sample regime where the mass difference between RCHB $\star$ and DRHBc $\star$ is significant. Figure 2 summarizes the mass difference between RCHB $\star$ and DRHBc $\star$ near Germanium isotopes. The filled square indicates a significant discrepancy between them, exceeding 5 MeV, while open square represents a minor difference below 5 MeV variance. The maximum discrepancy in the filled square region is 6.3 MeV from $^ { 9 3 }$ As which is a deformed nucleus with $\beta _ { 2 } = 0 . 3 1 6$ in FRDM(2012) [56]. From a preliminary result of DRHBc, the $\beta _ { 2 }$ of $^ { 9 3 }$ As is -0.254 [57]. In Table III we list the isotopes used in our sample sensitivity study. As expected they are all deformed. The study of mass sensitivity will be conducted using the nuclei marked with filled squares in Table III for the magnetohydrodynamic (MHD) and collapsar jet scenarios. Among several candidate sites for the r-process

![](images/66e31e249a5dafc3ea32aae75e9dd7225f8496de608cadf3229e260f6b59301f.jpg)

![](images/fdcece12892d04f02fa46da65e9f016c06d3f023100fedd6c0a8347d16cbcebd.jpg)

![](images/ac4afa067cbef773edbcc0d89d3043d490a3c5dd866a29c155ceff12b5b1d06a.jpg)

![](images/510c8d8dd1c85680f91a4b8bbfcb111d0eed0cd26f29ebba773229279f0e81d3.jpg)  
FIG. 1. One neutron separation energies of the Ca, Dy, U and As isotopes from DRHBc and DRHBc $\star$ compared with those from AME2020 [39]. Note that for the As isotopes we compare the separation energies only with AME2020, as DRHBc is not yet available for odd-Z nuclei.

![](images/2b6d87d01db0ed8da46f5250a96a29ef8eacfbbd1c4bd9284f4bb9a052a7c99f.jpg)  
FIG. 2. The isotopes with a mass difference greater than 5 MeV between DRHBc $\star$ and RCHB $\star$ for the five-inputs case.

nucleosynthesis, neutron star mergers contribute to the solar r-abundances only in recent epochs, whereas MHD and collapsar jets contribute over the entire history of cosmic evolution [58, 59].

We finally remark that the 5 MeV difference is a bit larger than the mass variation in a sensitivity study of rprocess abundances to nuclear masses: for example ±0.5 MeV (or 1 MeV difference) in Ref. [8] and ±1 MeV (or 2 MeV difference) in Ref. [10].

TABLE III. The isotopes used in our sample sensitivity study. The values of the quadrupole deformation $\beta _ { 2 }$ are taken from AME2020 [39] and from FRDM(2012) [56].   

<table><tr><td></td><td>AME2020</td><td>FRDM(2012)</td><td></td><td>AME2020</td><td>FRDM(2012)</td></tr><tr><td>89Ga</td><td>-</td><td>0.206</td><td>93As</td><td>-</td><td>0.316</td></tr><tr><td>89Ge</td><td>0.244</td><td>0.207</td><td>94As</td><td>-</td><td>0.316</td></tr><tr><td>90Ge</td><td>-0.255</td><td>0.207</td><td>95As</td><td>-</td><td>0.328</td></tr><tr><td>91Ge</td><td>-0.250</td><td>0.240</td><td>96As</td><td>-</td><td>0.329</td></tr><tr><td>92Ge</td><td>-0.246</td><td>0.316</td><td>94Se</td><td>-0.260</td><td>0.339</td></tr><tr><td>93Ge</td><td>-0.238</td><td>0.327</td><td>95Se</td><td>-0.254</td><td>0.328</td></tr><tr><td>94Ge</td><td>-0.231</td><td>0.327</td><td>96Se</td><td>-0.252</td><td>0.340</td></tr><tr><td>91As</td><td>-</td><td>0.208</td><td>97Se</td><td>-0.252</td><td>0.340</td></tr><tr><td>92As</td><td>-</td><td>0.208</td><td></td><td></td><td></td></tr></table>

# IV. SAMPLE MASS SENSITIVITY STUDY

The r-process can be understood through a network of various reactions, mainly involving neutron capture, photodissociation (the inverse of neutron capture), and beta decay. Different mass tables yield varying Q-values for reactions, which are crucial for determining reaction rates. Because the Q-value represents the energy associated with a reaction, in general an increase in the Q-value leads to a decrease in the reaction rate. These changes in reaction rates influence the equilibrium between neutron capture and photo-dissociation processes. Fission recycling is also important in the r-process nucleosynthesis. Some of the heavy nuclei produced in the r-process can become so massive that they undergo fission, splitting into lighter nuclei. This fission can also release a significant number of neutrons and then the released neutrons can be captured by nearby nuclei, inducing further nucleosynthesis [60].

Now, we perform a sample sensitivity study of the r-process abundances to nuclear deformations (or masses) using the isotopes summarized in Table III from the RCHB $\star$ and DRHBc $\star$ data. For this, we use the nuclear reaction network calculation code, Libnucnet [61] and take the thermonuclear reaction rate from JINA-REACLIB database [62]. In addition to the masses observed in experiments, a theoretical mass model, FRDM (2012) [56], is used. The code has been slightly updated by adding several new reaction rates and by adopting latest experimental measurements if available [63].

Once the mass of a nucleus changes, the corresponding $\beta$ -decay rates and neutron capture rates can also change. The neutron capture rates are calculated with the publicly available statistical model code TALYS [64]. We evaluate the corresponding $\beta$ -decay rates by using the empirical $\beta$ -decay rates developed in Ref. [65]:

$$
\log t _ {1 / 2} = c _ {1} - c _ {2} \log Q, \tag {8}
$$

where $c _ { 1 }$ and $c _ { 2 }$ take the values of (3.69, 4.80), (4.59, 5.08), (4.98, 5.53), and (6.32, 6.34) for even-even, even-odd, odd-even, and odd-odd parents nuclei, respectively.

For the mass sensitivity study, we consider the MHD jet supernova model and collapsar jets.

# MHD jet model

In the MHD jet model [66–68], rapid rotation and strong magnetic fields can produce neutron-rich jets in polar direction along the rotational axis of the core collapse supernova, providing a favorable environment for the $r$ -process. In our simulations, the twenty-three trajectories from the MHD jet model in Ref. [70] are used.

Figure 3 shows the final r-process yield ( $Y _ { i }$ ) patterns obtained from the MHD jet environments with fission recycling with two different nuclear mass models: RCHB $\star$ (blue line with dots) and DRHBc $\star$ (orange line). All yield values are normalized such that $\sum Y _ { i } = 1$ , ensuring that the total abundance across all mass numbers remains consistent for comparison between different models. In the figure, we examine three cases: changing only the mass (top panel), altering both the mass and the beta-decay rate (second panel), and modifying the mass alongside the neutron capture rate (third panel). The bottom panel presents a case where all three —mass, beta-decay rate, and neutron capture rate— are changed simultaneously. The figures on the left use an expanded scale. It can be seen from Fig. 3 that the r-process yields of RCHB $\star$ and DRHBc $\star$ can differ by up to two orders of magnitude in the regime from $A = 8 0$ to 120. We note that fission recycling plays a minimal role in the MHD model, as the yields of nuclei with $A > 2 6 5$ prior to fission recycling are negligible. As a result, in the MHD scenario, the final r-process yield patterns are practically identical with and without fission recycling.

![](images/a53ad5d7827306dd92dfaf65df3c7a1e6816eb51c9e53ea3dc1e6a83e54ba4a9.jpg)

![](images/9accd630ec563cec87a00579483c20345f9f64d0c0ebba5ee501f86312d30f98.jpg)

![](images/8c34c36b552840860b1db8c196f6f04759d89dcf2227bd68246f42074f2b16c0.jpg)

![](images/372c8623a23ef4bf51cb701ea037ba6b5bbb9af85ac553b15796a6b769a2f7d8.jpg)

![](images/508f6ee81f7f4678466d99d08c4b6df1d0cfb1ab752c4f75dadc6f2c9a9d25bc.jpg)

![](images/336a54a1367ae9bb600b772c5792e39e902cb9ceb5b1ce9659b2d6449bcc6357.jpg)

![](images/b40c06f34b2d27824176371c6bb4f890a78edc2c110678e053d2218ed7a46d70.jpg)

![](images/12544a100dd48ea7626599cf633911b8e3f7b28a9b17d8ecf6024de987b410e9.jpg)  
FIG. 3. MHD results with fission recycling: The top panel shows the effect of changing only the mass, the second panel adjusts both the mass and beta decay rate, the third panel modifies the mass and neutron capture rate, and the bottom panel varies the mass, beta decay rate, and neutron capture rate. The figures on the left are displayed on an expanded scale.

Another notable feature in Fig. 3 is that the lines ( $Y _ { i }$ s) are intersect near $A = 9 1 \mathrm { { o r } 9 2 }$ . This behavior can be explained by examining the Q-values of neutron capture reactions using the RCHB $\star$ and DRHBc $\star$ mass tables. The differences between the Q-values from the RCHB $\star$ and DRHBc $\star$ mass tables change sign from negative to positive as the neutron number increases. For example, the Q-values for the $^ { 9 0 } \mathrm { A s } ( \mathrm { n } , \gamma ) ^ { 9 1 }$ As reaction are 1.04 MeV for the RCHB $\star$ mass table and 6.22 MeV for the DRHBc $\star$ mass table. In contrast, the Q-values for $^ { 9 3 } \mathrm { A s } ( \mathrm { n } , \gamma ) ^ { 9 4 }$ As are 1.96 MeV (RCHB $\star$ ) and 1.88 MeV (DRHBc $\star$ ), while for $^ { 9 6 } \mathrm { A s } ( \mathrm { n } , \gamma ) ^ { 9 7 } { \dot { F } }$ s are 4.41 MeV (RCHB $\star$ ) and -1.13 MeV DRHBc⋆. This indicates that neutron capture reactions involving more neutron-rich nuclei are more favorable with the DRHBc⋆

mass table. Within the mass range we explored, the DRHBc $\star$ mass table predicts the production of more neutron-rich nuclei, leading to higher abundances of elements with $A > 9 2$ .

![](images/d1bba7bd2468c8702838501c7c34f198c5fb6c274e44cbebc21a6875d83c3588.jpg)  
FIG. 4. The contribution from the MHD model with RCHB $\star$ and DRHBc $\star$ to the solar r-abundances.

We finally present the contribution of the MHD model with RCHB $\star$ and DRHBc $\star$ to the solar r-abundances [69]. As shown in Fig. 4, the DRHBc $\star$ model contributes more than the RCHB $\star$ model to the small peak near A = 104. We anticipate that the complete mass table from the DRHBc calculation will enable a more precise study of the relationship between the solar r-abundances near A = 104 and nuclear deformations.

As it can be seen from Fig. 4, there are large error bars in the solar r-abundance around A=90. It is crucial to reduce these error bars by accurately determining the s-process components in the solar abundances, in order to better understand the role of nuclear deformations in r-process nucleosynthesis.

# Collapsar jet model

We adopt the collapsar model developed in Ref. [71, 72], where the progenitor mass is 35 $M _ { \odot }$ , rotational velocity is vϕ = 380 km/s and metallicity is approximately 0.1 $Z _ { \odot }$ . In our calculations we consider the eight representative trajectories from Ref. [72].

Figure 5 shows the final abundance patterns of the r-process in collapsar environments with fission recycling, using the fission rates provided in [70]. Unlike the MHD model scenario, fission recycling plays a crucial role in shaping the final abundance pattern in collapsar jets. In particular, the abundance distribution for nuclei at the mass region 100<A<150 is significantly redistributed by fission fragments. Therefore, the pronounced abundance differences at 100<A $<$ <120 in the MHD model (Fig. 3) are nearly eliminated in the collapsar model (Fig. 5).

This can be explained as follows: The collapsar environment is more explosive than the MHD jet environment, leading to the formation of more neutron-rich nuclei as a result of the active occurrence of neutron-capture reactions. In this context, nuclear reactions involving elements from $^ { 8 9 }$ Ga to $^ { 9 7 }$ Se contribute relatively little. As the results show, the r-process predominantly produces heavy elements by consuming lighter ones, underscoring the critical role of fission recycling in this environment.

# V. SUMMARY AND DISCUSSION

As an initial step in studying the role of nuclear deformations in r-process nucleosynthesis, we conducted a preliminary sensitivity study of the r-process. To complete the DRHBc mass table for nuclear binding energies, we employed the DNN method, which resulted in an improved RMS deviation of 0.842 MeV between the AME2020 and DRHBc $\star$ datasets; the RMS deviation between AME2020 and the even-Z DRHBc mass table is 1.433 MeV. We also compared the mass of the neutron-rich isotopes newly measured in [55] with our results in DRHBc $\star$ and obtained the RMS deviation of 0.725 MeV. This deviation is a bit improved compared with 0.842 MeV in Table I, which indicates that DRHBc $\star$ (and also DRHBc) may work better for exotic nuclei. Additionally, we compared the one-neutron separation energies for the isotopes of Ca, Dy, U, and As between DRHBc and DRHBc $\star$ and the AME2020 data, and observed that our results show reasonable agreement.

We then calculated the r-process abundances by using portions of the RCHB $\star$ and DRHBc $\star$ mass tables, where the mass difference exceeds 5 MeV, in the astrophysical sites of the r-process:MHD and collapsar jets. We found that r-process abundances in these two sites are sensitive to the mass difference between RCHB $\star$ and DRHBc $\star$ , particularly

![](images/fe37a3dc2b668904633ecfdd79076c392ddeeac5022b86de556f5dc621eb9f6a.jpg)

![](images/e5abdf264b98de3dca438912f33c3ceca35d6cc3e60e1c468d15e1b1a818a783.jpg)

![](images/82f9f47fdcdd2aba92a32d156933c14251028dd69ee45adfcd5ff876ee9345d9.jpg)

![](images/c4b59e6a25e6fea2394f0e6a6d14e48d56440eb503ebbbf735983706e47ee47a.jpg)

![](images/c96569d148908c10a876bb9c851c37d51507d91df1346031520b0e5744d90cfe.jpg)

![](images/290695379df239948c8347e1dce3303a844ed7001bc7ea1c2c04c56b85e9f78e.jpg)

![](images/f58d5cf7f4b86d0d8ed5be24470da99e391af7a7a96c9ceac5eee5827fcd9558.jpg)

![](images/2680cbc154ae8ef25eaa3d3eee4af42b25908a2bbf900b28a3f4121c3585b990.jpg)  
FIG. 5. Collapsar results with fission recycling: the top panel changes only the mass, the second panel modifies both the mass and beta decay rate, the third panel adjusts the mass and neutron capture rate and the bottom panel varies the mass, beta decay rate, and neutron capture rate.

within the mass range of $A = 8 0 - 1 2 0$ . Since the primary difference between the two mass tables lies in nuclear deformations, our study suggests that deformations play a significant role in r-process nucleosynthesis. In the future, once the complete DRHBc mass table becomes available, we plan to conduct an in-depth study of the relationship between the solar r-process abundances (particularly near A=104) and nuclear deformations.

Y.K. thanks the DRHBc collaboration members for helpful comments. This work was supported in part by the Institute for Basic Science (IBS-R031-D1, 2013M7A1A1075764), the National Key R&D Program of China (2022YFA1602401) and the National Natural Science Foundation of China (No. 12335009 & 12435010).

[1] D. Lunney, J. M. Pearson and C. Thibault, Rev. Mod. Phys. 75, 1021 (2003).   
[2] C. A. Bertulani and T. Kajino, Prog. Part. Nucl. Phys. 89, 56 (2016).   
[3] T. Kajino, W. Aoki, A. B. Balantekin, R. Diehl, M. A. Famiano and G. J. Mathews, Prog. Part. Nucl. Phys. 107, 109 (2019).   
[4] C. J. Horowitz, A. Arcones, B. Cˆot´e, I. Dillmann, W. Nazarewicz, I. U. Roederer, H. Schatz, A. Aprahamian, D. Atanasov and A. Bauswein, et al. J. Phys. G 46, 083001 (2019).   
[5] J. J. Cowan, C. Sneden, J. E. Lawler, A. Aprahamian, M. Wiescher, K. Langanke, G. Mart´ınez-Pinedo and F. K. Thielemann, Rev. Mod. Phys. 93, 15002 (2021).   
[6] M. R. Mumpower, R. Surman, G. C. McLaughlin and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016) [erratum: Prog. Part. Nucl. Phys. 87, 116 (2016)].   
[7] T. Kajino and G. J. Mathews, Rept. Prog. Phys. 80, 084901 (2017).   
[8] M. R. Mumpower, R. Surman, D. L. Fang, M. Beard, P. M¨oller, T. Kawano and A. Aprahamian, Phys. Rev. C 92, no.3, 035807 (2015).   
[9] X. F. Jiang, X. H. Wu and P. W. Zhao, Astrophys. J. 915, 29 (2021).   
[10] Y. W. Hao, Y. F. Niu and Z. M. Niu, Phys. Lett. B 844, 138092 (2023).   
[11] P. Moller, J. R. Nix, W. D. Myers and W. J. Swiatecki, Atom. Data Nucl. Data Tabl. 59, 185-381 (1995).   
[12] N. Wang, Z. Liang, M. Liu and X. Wu, Phys. Rev. C 82, 044304 (2010).   
[13] S. Goriely, N. Chamel and J. M. Pearson, Phys. Rev. Lett. 102, 152503 (2009).   
[14] S. Goriely, S. Hilaire, M. Girod and S. Peru, Phys. Rev. Lett. 102, 242501 (2009).   
[15] S. Goriely, N. Chamel and J. M. Pearson, Phys. Rev. C 82, 035804 (2010).   
[16] J. Meng, Nucl. Phys. A 635, 3 (1998).   
[17] J. Meng and P. Ring, Phys. Rev. Lett. 77, 3963 (1996).   
[18] J. Meng, H. Toki, S. G. Zhou, S. Q. Zhang, W. H. Long and L. S. Geng, Prog. Part. Nucl. Phys. 57, 470-563 (2006).   
[19] D. Vretenar, A. V. Afanasjev, G. A. Lalazissis and P. Ring, Phys. Rept. 409, 101 (2005).   
[20] X. W. Xia, Y. Lim, P. W. Zhao, H. Z. Liang, X. Y. Qu, Y. Chen, H. Liu, L. F. Zhang, S. Q. Zhang and Y. Kim, et al. Atom. Data Nucl. Data Tabl. 121-122, 1 (2018).   
[21] P. W. Zhao, Z. P. Li, J. M. Yao and J. Meng, Phys. Rev. C 82, 054319 (2010).   
[22] S. G. Zhou, J. Meng, P. Ring and E. G. Zhao, Phys. Rev. C 82, 011301 (2010).   
[23] L. Li, J. Meng, P. Ring, E. G. Zhao and S. G. Zhou, Phys. Rev. C 85, 024312 (2012).   
[24] K. Zhang et al. [DRHBc Mass Table], Phys. Rev. C 102, 024314 (2020).   
[25] C. Pan et al. [DRHBc Mass Table], Phys. Rev. C 106, 014316 (2022).   
[26] C. Pan, K. Y. Zhang, P. S. Chong, C. Heo, M. C. Ho, J. Lee, Z. P. Li, W. Sun, C. K. Tam and S. H. Wong, et al. Phys. Rev. C 104, 024331 (2021).   
[27] R. An, X. Jiang, L. G. Cao and F. S. Zhang, Phys. Rev. C 105, 014325 (2022).   
[28] S. Kim, M. H. Mun, M. K. Cheoun and E. Ha, Phys. Rev. C 105, 034340 (2022).   
[29] Y. B. Choi, C. H. Lee, M. H. Mun and Y. Kim, Phys. Rev. C 105, 024306 (2022).   
[30] X. Sun and J. Meng, Phys. Rev. C 105, 044312 (2022).   
[31] K. Y. Zhang, P. Papakonstantinou, M. H. Mun, Y. Kim, H. Yan and X. X. Sun, Phys. Rev. C 107, L041303 (2023).   
[32] K. Y. Zhang, S. Q. Yang, J. L. An, S. S. Zhang, P. Papakonstantinou, M. H. Mun, Y. Kim and H. Yan, Phys. Lett. B 844, 138112 (2023).   
[33] Y. Xiao, S. Z. Xu, R. Y. Zheng, X. X. Sun, L. S. Geng and S. S. Zhang, Phys. Lett. B 845, 138160 (2023).   
[34] X. Y. Zhang, Z. M. Niu, W. Sun and X. W. Xia, Phys. Rev. C 108, 024310 (2023).   
[35] Mart´ın Abadi et al., https://www.tensorflow.org/ (2015).   
[36] M. W. Kirson, Nucl. Phys. A 798, 29-60 (2008).   
[37] K. Zhang et al. [DRHBc Mass Table], Atom. Data Nucl. Data Tabl. 144, 101488 (2022).   
[38] P. Guo et al. [DRHBc Mass Table], Atom. Data Nucl. Data Tabl. 158, 101661 (2024).   
[39] M. Wang, W. J. Huang, F. G. Kondev, G. Audi and S. Naimi, Chin. Phys. C 45, 030003 (2021).   
[40] Z. M. Niu and H. Z. Liang, Phys. Lett. B 778, 48 (2018).   
[41] G. A. Negoita, J. P. Vary, G. R. Luecke, P. Maris, A. M. Shirokov, I. J. Shin, Y. Kim, E. G. Ng, C. Yang and M. Lockner, et al. Phys. Rev. C 99, 054308 (2019).   
[42] W. G. Jiang, G. Hagen and T. Papenbrock, Phys. Rev. C 100, 054326 (2019).   
[43] M. R. Mumpower, T. M. Sprouse, A. E. Lovell and A. T. Mohan, Phys. Rev. C 106, L021301 (2022).   
[44] C. Q. Li, C. N. Tong, H. J. Du and L. G. Pang, Phys. Rev. C 105, 064306 (2022).   
[45] L. X. Zeng, Y. Y. Yin, X. X. Dong and L. S. Geng, [arXiv:2210.02906 [nucl-th]].

[46] Z. M. Niu and H. Z. Liang, Phys. Rev. C 106, L021303 (2022).   
[47] X. H. Wu, Y. Y. Lu and P. W. Zhao, Phys. Lett. B 834, 137394 (2022).   
[48] M. Mumpower, M. Li, T. M. Sprouse, B. S. Meyer, A. E. Lovell and A. T. Mohan, Front. in Phys. 11, 1198572 (2023).   
[49] M. Kn¨oll, T. Wolfgruber, M. L. Agel, C. Wenz and R. Roth, Phys. Lett. B 839, 137781 (2023).   
[50] M. Li, T. M. Sprouse, B. S. Meyer and M. R. Mumpower, Phys. Lett. B 848, 138385 (2024).   
[51] E. Y¨uksel, D. Soydaner and H. Bahtiyar, [arXiv:2401.02824 [nucl-th]].   
[52] A. Boehnlein, M. Diefenthaler, N. Sato, M. Schram, V. Ziegler, C. Fanelli, M. Hjorth-Jensen, T. Horn, M. P. Kuchera and D. Lee, et al. Rev. Mod. Phys. 94, 031003 (2022).   
[53] J. E. Garc´ıa-Ramos, A. S´aiz, J. M. Arias, L. Lamata and P. P´erez-Fern´andez, [arXiv:2307.07332 [quant-ph]].   
[54] M. W. Kirson, Nucl. Phys. A 798, 29 (2008).   
[55] W. Xian, S. Chen, S. Nikas, M. Rosenbusch, M. Wada, H. Ishiyama, D. Hou, S. Iimura, S. Nishimura and P. Schury, et al. Phys. Rev. C 109, 035804 (2024).   
[56] P. M¨oller, A. J. Sierk, T. Ichikawa and H. Sagawa, Atom. Data Nucl. Data Tabl. 109-110, 1-204 (2016)   
[57] P. Guo, private communication.   
[58] C. Kobayashi, A. I. Karakas and M. Lugaro, Astrophys. J. 900, 179 (2020).   
[59] Y. Yamazaki, Z. He, T. Kajino, G. J. Mathews, M. A. Famiano, X. Tang and J. Shi, Astrophys. J. 933, 112 (2022).   
[60] Z. He, T. Kajino, M. Kusakabe et. al., Astrophys. J. Lett. 966, L37 (2024).   
[61] B. S. Meyer, D. C. Adams, M&PSA, 42, 5215 (2007).   
[62] R. H. Cyburt, A. M. Amthor, R. Ferguson, et al. Astrophys. J. Suppl. Ser. 189, 240 (2010).   
[63] K. Kim, Y. Kim, Z. He, X. Yao, et al. Impact of light-mass nuclear reactions on the r-process nucleosynthesis, revisited, ”in preparation.”   
[64] A. Koning, S. Hilaire and S. Goriely, Eur. Phys. J. A 59, no.6, 131 (2023).   
[65] Y. Zhou, Z. Li, Y. Wang, et al. Sci. China Phys. Mech. Astron. 60, 082012 (2017).   
[66] S. Nishimura, K. Kotake, M. a. Hashimoto, S. Yamada, N. Nishimura, S. Fujimoto and K. Sato, Astrophys. J. 642, 410 (2006).   
[67] C. Winteler, R. Kaeppeli, A. Perego, A. Arcones, N. Vasset, N. Nishimura, M. Liebendoerfer and F. K. Thielemann, Astrophys. J. Lett. 750, L22 (2012).   
[68] N. Nishimura, T. Takiwaki and F. K. Thielemann, Astrophys. J. 810, 109 (2015).   
[69] S. Goriely, Astronomy and Astrophysics 342, 881 (1999).   
[70] S. Shibagaki, T. Kajino, G. J. Mathews, S. Chiba, S. Nishimura and G. Lorusso, Astrophys. J. 816, 79 (2016)   
[71] S. Harikae, T. Takiwaki and K. Kotake, Astrophys. J. 704 (2009), 354-371   
[72] K. Nakamura, T. Kajino, G.J. Mathews, S. Sato and S. Harike, Internat. J. Modern Phys. E 22 (2013), 1330022.