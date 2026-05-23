# Machine learning the nuclear mass

Zepeng Gao, $1 , 2$ Yongjia Wang,2, ∗ Hongliang Lü,3 Qingfeng Li,2, 4, † Caiwan Shen,5 and Ling Liu1

$^ { 1 }$ College of Physics Science and Technology, Shenyang Normal University, Shenyang 110034, China $^ 2$ School of Science, Huzhou University, Huzhou 313000, China

$^ 3$ HiSilicon Research Department, Huawei Technologies Co., Ltd., Shenzhen 518000, China

$^ 4$ Institute of Modern Physics, Chinese Academy of Science, Lanzhou 730000, China

$^ 5$ School of Science, Huzhou University, Huzhou 110000, China

(Dated: May 7, 2021)

Background: The masses of about 2500 nuclei have been measured experimentally, however more than 7000 isotopes are predicted to exist in the nuclear landscape from H (Z=1) to Og (Z=118) based on various theoretical calculations. Exploring the mass of the remains is a hot topic in nuclear physics. Machine learning has been served as a powerful tool in learning complex representations of big data in many fields. Purpose: We use Light Gradient Boosting Machine (LightGBM) which is a highly efficient machine learning algorithm to predict the masses of unknown nuclei and to explore the nuclear landscape in neutron-rich side from learning the measured nuclear masses. Methods: Several characteristic quantities (e.g., mass number, proton number) are fed into LightGBM algorithm to mimic the patterns of the residual $\delta ( Z , A )$ between the experimental binding energy and the theoretical one given by the liquid-drop model (LDM), Duflo-Zucker (DZ) mass model, finite-range droplet model (FRDM), as well as the Weizsäcker-Skyrme (WS4) model, so as to refine these mass models. Results: By using the experimental data of 80 percent of known nuclei as the training dataset, the root mean square deviation (RMSD) between the predicted and the experimental binding energy of the remaining $2 0 \%$ is about 0.234±0.022 MeV, 0.213±0.018 MeV, 0.170±0.011 MeV, and $0 . 2 2 2 { \pm } 0 . 0 1 6$ MeV for the LightGBM-refined LDM, DZ, WS4, and FRDM models, respectively. These values are of about $9 0 \%$ , $6 5 \%$ , $4 0 \%$ , and $6 0 \%$ smaller than the corresponding origin mass models. The RMSD for 66 newly measured nuclei that appeared in AME2020 is also significantly improved on the same foot. One-neutron and two-neutron separation energies predicted by these refined models are in consistence with several theoretical predictions based on various physical models. In addition, the two-neutron separation energy of several newly measured nuclei (e.g., some isotopes of Ca, Ti, Pm, Sm) predicted with LightGBM-refined mass models are also in good agreement with the latest experimental data. Conclusions: LightGBM can be used to refine theoretical nuclear mass models so as to predict the binding energy of unknown nuclei. Moreover, the correlation between the input characteristic quantities and the output can be interpreted by SHapley Additive exPlanations (SHAP, a popular explainable artificial intelligence tool), this may provide new insights on developing theoretical nuclear mass models.

# I. INTRODUCTION

The mass of nuclei, which is of fundamental importance to explore nuclear landscape and properties of nuclear force, plays a crucial role in understanding many issues in both the fields of nuclear physics and astrophysics [1–6]. It is known that more than 7000 nuclei in the nuclear landscape from H (Z=1) to Og (Z=118) are predicted to be existed according to various theoretical models, while about 3000 nuclei have been found or synthesized in experimental and the masses of about 2500 nuclei have been measured accurately [7, 8]. Exploring the masses of the remains is of particular interest for both nuclear experimental and theoretical community. On the experimental side, facilities, such as HIRFL-CSR in China, RIBF at RIKEN in Japan, cooler-storage ring ESR and SHIPTRAP at GSI in Germany, CPT at Argonne and LEBIT at MSU in US, ISOLTRAP at CERN, JYFLTRAP at Jyväskylä in

Finland, TITAN at TRIUMPH in Canada, are partly dedicated to measuring the nuclear mass, especially for nuclei round the driplines. On the theoretical side, various models have been developed to study nuclear mass by considering different physics, such as finite-range droplet model (FRDM) [9, 10], the Weizsäcker-Skyrme (WS) model [11], Hartree-Fock-Bogoliubov (HFB) mass models [12–14], the relativistic mean-field (RMF) model [15], relativistic continuum Hartree-Bogoliubov (RCHB) theory [16]. Though tremendous progress has been made in both experimental and theoretical sides, exploring mass of nuclei around dirplines is still a great challenge for both sides.

Machine learning which is the subset of artificial intelligence has been widely applied for analyzing data in many branches of science, such as in physics, e.g., Refs. [17, 18]. In nuclear physics, a Bayesian neural network (BNN) has been applied to reduce the mass residuals between theory and experiment, and a significant improvement in the mass predictions of several theoretical models was obtained after BNN refinement [19–21], e.g., the root mean square deviation (RMSD) of the liquid-drop model (LDM) was reduced from about 3

MeV to 0.8 MeV. Later on, BNN approach is also applied to study nuclear charge radii [22], $\beta$ -decay half-lives [26], fission product yield [23], fragment Production in spallation reaction [24, 25]. Besides BNN, other machine learning or deep learning algorithms also have been employed in studying of nuclear reactions, e.g., Refs. [27– 32]. Focusing on nuclear mass, besides BNN in Refs. [19– 21], the Levenberg-Marquardt neural network approach [33], Gaussian processes [34, 35], decision tree algorithm [36], the Multilayer Perceptron (MLP) algorithm [37] also have been applied to refine nuclear mass models.

Indeed, studying nuclear mass with machine learning algorithms is not a new topic and it can be traced back to at least 1993, see e.g., Refs. [38–40] and reference therein. In Ref. [38], the capability of multilayer feedforward neural networks for learning the systematics of atomic masses and nuclear spins and parities with high accuracy has been found. This topic is flourishing again because of the rapid development of computer science and artificial intelligence. In 2016, Light Gradient Boosting Machine (LightGBM) which is a tree based learning algorithm was developed by Microsoft [49]. It is a state-of-theart machine learning algorithm which has achieved better performances in many machine learning tasks. Therefore, it would be interesting to explore whether LightGBM algorithm can achieve better accuracy than BNN on the task of predicting nuclear mass.

The paper is organized as follows: In Sec.II, we will introduce the LightGBM model and ten input features. The predicted binding energy and neutron separation energy obtained with LightGBM are discussed in detail in Sec.III. The conclusion and outlook are given in Sec.IV.

# II. LIGHTGBM AND THE INPUT FEATURES

LightGBM refers to a recent improvement of gradient boosting decision tree (GBDT) that provides efficient implementation of gradient boosting algorithms. It is becoming more popular by the day due to its efficiency and capability of handling large amounts of data. LightGBM has leaf-wise growth of trees, rather than a level-wise growth. After the first partition, the next split is performed only on the leaf node that adds more to the information gain.

The primary advantage of LightGBM is the change in training algorithm that speeds up the optimization process dramatically and results in a more effective model in many cases. More concretely, to speed up the training process, LightGBM uses a histogram-based methodology to select the best segmentation. For any continuous variable, instead of using individual values, these are divided into bins or buckets, which can accelerate the training process and reduce memory usage. In addition, LightGBM contains two novel techniques: Gradient bases One-Side Sampling (GOSS), which keeps all the instances of large gradient and performs random sampling on the instances with small

gradient, and Exclusive Feature Bundling (EFB), which helps to bundle multiple features into a single feature without losing any information. Furthermore, as a decision tree-based algorithm, LightGBM also has high level of interpretability, allowing the results obtained in machine learning model to be checked against previous knowledge regarding nuclear mass. For example, one can find which feature is more important for predicting nuclear mass, this would be helpful to further improve nuclear mass model.

In this work, the binding energies of 2408 nuclei between 16O and $^ { 2 7 0 }$ Ds from the atomic mass evaluation (AME2016) [8] are employed as the training and testing dataset. LightGBM is trained to learn the residual between the theoretical prediction and the experimental binding energy, $\delta ( Z , A ) = B _ { \mathrm { t h } } ( Z , A ) - B _ { \mathrm { e x p } } ( Z , A )$ . Four theoretical mass models are adopted in this work to obtain $B _ { t h }$ , including the LDM [33], DZ [41], FRDM [9, 10], and WS4 [11]. After LightGBM learns the behaviour of the residual $\delta ( Z , A )$ , the binding energy of an unknown mass nucleus can be obtained via $B _ { \mathrm { L i g h t G B M } } ( Z , A ) { = } B _ { \mathrm { t h } } ( Z , A ) + \delta ( Z , A )$ . It is found that the RMSD of these four theoretical mass models can be significantly improved after LightGBM refinement.

For the LDM model, nucleus is regarded as a noncompressible droplet, which contains the volume energy, surface energy, Coulomb energy of proton repulsion, the symmetry energy related to the ratio of neutrons to protons, and the pairing energy of the neutron-proton pairing effect. It can be described as follows:

$$
\begin{array}{l} B _ {\mathrm {L D M}} (Z, A) = a _ {v} \left(1 + \frac {4 k _ {v}}{A ^ {2}} | T _ {z} | \left(| T _ {z} | + 1\right)\right) A \\ + a _ {s} \left(1 + \frac {4 k _ {s}}{A ^ {2}} \left| T _ {z} \right| \left(\left| T _ {z} \right| + 1\right)\right) A ^ {\frac {2}{3}} \tag {1} \\ + a _ {c} \frac {Z ^ {2}}{A ^ {\frac {1}{3}}} + f _ {p} \frac {Z ^ {2}}{A} + E _ {p}. \\ \end{array}
$$

Where $E _ { p }$ is the pairing energy given by the following expression:

$$
E _ {p} = \left\{ \begin{array}{l l} \frac {d _ {n}}{N ^ {1 / 3}} + \frac {d _ {p}}{Z ^ {1 / 3}} + \frac {d _ {n p}}{A ^ {2 / 3}}, & \text {f o r Z a n d N o d d}, \\ \frac {d _ {p}}{Z ^ {1 / 3}}, & \text {f o r Z o d d , N e v e n}, \\ \frac {d _ {n}}{N ^ {1 / 3}}, & \text {f o r Z e v e n , N o d d}, \\ 0, & \text {f o r Z a n d N e v e n}. \end{array} \right. \tag {2}
$$

In the above formula, $A$ , $Z$ , $N$ and $T _ { z }$ are the mass number, proton number, neutron number and the third component of isospin ( $\begin{array} { r } { T _ { z } = \frac { 1 } { 2 } ( Z - N ) ) } \end{array}$ , $a _ { v }$ , $k _ { v }$ , $a _ { s }$ , $k _ { s }$ , $a _ { c }$ , $f _ { p }$ , $d _ { n }$ , $d _ { p }$ , $d _ { n p }$ are adjustable parameters with the values given in Table I. Based on these parameters the binding energy of 2408 nuclei theoretical and experimental values as an RMSD is 2.463 MeV.

This work mainly aims to find the relationship between the feature quantity of each nucleus and $\delta ( Z , A )$ with

Table I. Parameter setting   

<table><tr><td>Parameter</td><td>Value (MeV)</td></tr><tr><td>av</td><td>-15.4963</td></tr><tr><td>as</td><td>17.7937</td></tr><tr><td>kv</td><td>-1.8232</td></tr><tr><td>ks</td><td>-2.2593</td></tr><tr><td>ac</td><td>0.7093</td></tr><tr><td>fp</td><td>-1.2739</td></tr><tr><td>dn</td><td>4.6919</td></tr><tr><td>dp</td><td>4.7230</td></tr><tr><td>dnp</td><td>-6.4920</td></tr></table>

Table II. Selection of characteristic quantities   

<table><tr><td>Features</td><td>Description</td></tr><tr><td>A</td><td>mass number</td></tr><tr><td>Z</td><td>proton number</td></tr><tr><td>N</td><td>neutron number</td></tr><tr><td>N/Z</td><td>ratio of neutron to proton</td></tr><tr><td>BLDM</td><td>theoretical value from LDM</td></tr><tr><td>Npair=0,1,2</td><td>dependence on pair effect; for odd-odd,odd-even,even-even</td></tr><tr><td>Zm=1,2···</td><td>shell of the last proton; for 8 ≤ Z &lt; 20,20 ≤ Z &lt; 28,···</td></tr><tr><td>Nm=1,2···</td><td>shell of the last neutron; for 8 ≤ N &lt; 20,20 ≤ N &lt; 28,···</td></tr><tr><td>|Z-m|</td><td>the distance between the proton number and the nearest magic number; m ∈ {8,20,28,50,82,126}</td></tr><tr><td>|N-m|</td><td>the distance between the neutron number and the nearest magic number; m ∈ {8,20,28,50,82,126,184}</td></tr></table>

the LightGBM model. For each nucleus, we selected 10 physical quantities (cf. Table II) as the input features. It is known that nuclear binding energy and nuclear structure are linked, therefore, we selected four physical quantities related to the shell structure, among which $Z _ { m }$ and $N _ { m }$ are the shells where the last proton and neutron are located, and the level of the shell is given by the magic numbers. The number of protons between 8, 20, 50, 82 and 126 corresponds to $Z _ { m }$ of 1, 2, 3, 4, and the number of neutrons between 8, 20, 50, 82, 126 and 184 corresponds to $N _ { m }$ of 1, 2, 3, 4, 5. In addition, $| Z - m |$ and $| N - m |$ are the absolute values of the difference between the number of protons, the number of neutrons, and the nearest magic number, respectively, which represent the distance between the number of protons, the number of neutrons, and the nearest magic number. N pair is an index that considers the protonneutron pairing effect, the odd-odd nucleus is 0, the oddeven nucleus or even-odd nucleus is 1, and the even-even nucleus is 2.

In this work, the value of num_boost_round (maximum number of decision trees allowed) is 50000, num_leaves (maximum number of leaves allowed per tree) is 10, max_depth (maximum depth allowed per

tree) is -1 and other parameters are basically set as their default values of the LightGBM model. Varying these parameters would not alter the results significantly. During the training process, LightGBM will generate a decision tree based on the relevant information between the features of the training set and $\delta ( Z , A )$ . 10-fold cross-validation, which is a technique to evaluate models by partitioning the original dataset into 10 equal size subsamples., is also applied to prevent overfitting and selection bias. After training, the model will make predictions on the testing set. Each nucleus in the testing set traverses the decision tree grown during model training. Each decision tree will give its contribution to the predicted value according to the feature quantity of each nucleus. The sum of the contributions of all decision trees is the predicted value given by the final model.

# III. RESULT

# A. Predictions on the binding energy based on LDM

In this section, LightGBM is trained to learn the residual $\delta ( Z , A )$ between the LDM and experimental binding energies. For this purpose, binding energies of the 2408 nuclei between $^ { 1 6 }$ O and $^ { 2 7 0 }$ Ds from AME2016 are split into training and testing data sets. We note here that, nuclei with proton (neutron) number smaller than 8 and with relatively large experimental uncertainties in AME2016 are not used. First, the influence of training size on the predicted binding energy is examined, as displayed in Fig.1. We randomly select 482 (about 20% of the 2408 nuclei) nuclei to constitute the training set. The RMSD of LDM for the selected 482 nuclei is about 2.458 MeV, after the LightGBM refinement, the RMSD is reduced to 0.496, 0.272, 0.233 MeV when 482, 1204, and 1926 nuclei are used to train the LightGBM, respectively. This means that LightGBM has been able to capture the missing physics of the LDM and to decode the correlation between the input features and the residual, so as to further improve the agreement with experimental data.

In addition, it can be seen that the deviation between the experimental and LightGBM-refined LDM predictions for nuclei with the small number of proton and neutron is usually larger, this may due to the fact that the microstructure effect in the light-mass nuclei is strong, and there are less data on the light-mass nuclei in the training set. The value of the above mentioned RMSD will fluctuate when the training and test data sets are randomly selected, because $\delta ( Z , A )$ for some of nuclei (i.e., nuclei around magic number) are large and some of are small. To evaluate this issue, we randomly split the 2408 nuclei into training and testing data sets 500 times with each ratio (i.e., 4:1, 1:1, and 1:4), the RMSD and its density distribution are plotted in Fig.2 and Fig.3. As observed in Fig.2, fluctuation in the RMSD is the largest of all when the ratio of training

![](images/01a665e87427e08a89162e8de1c468f79ea4f17bc8810391693a86f36ad48091.jpg)  
Figure 1. Upper panels: Locations of training data sets with $2 0 \%$ (a), $5 0 \%$ (b), and 80% (c) of the 2408 nuclei from AME2016 in the N-Z plane. Lower panels: The absolute error between the experimental and LightGBM-refined LDM predicted binding energies for the testing set ( $2 0 \%$ of the 2408 nuclei). (d), (e), and (f) display the deviation obtained with LightGBM-refined LDM trained with $2 0 \%$ , $5 0 \%$ , and $8 0 \%$ of the 2408 nuclei. $\sigma _ { p r e }$ is RMSD of the original LDM, $\sigma _ { p o s t }$ is RMSD of the LightGBM-refined LDM.

![](images/072bb3b02ede4914ab8837e32874bad427d35cb122c00197e6c07b5d8f854c40.jpg)  
Figure 2. The RMSD for the testing data from 100 runs. In each run, the 2408 nuclei are randomly split into the training and testing data sets with the ratio of 4:1 (blue), 1:1 (orange), and 1:4 (green).

size to testing size is 1:4. The RMSD for 1926 nuclei predicted by LightGBM-refined LDM with learning the binding energy of 482 nuclei is about 0.508±0.035 MeV,

![](images/840a49a7fba33ed10f3afed6a69b7d5b1e9d9bf1beef1cf17784eb3373ec7e96.jpg)  
Figure 3. The density distribution of RMSD between the experimental and the predicted binding energy. Results from 500 runs for each set is displayed. Dash lines denote Gaussian fit to the distribution. The mean values and the standard deviation of RMSD are 0.508, 0.303, 0.224 MeV and 0.035, 0.020, 0.022 MeV for the three sets with different ratios of training to testing size, respectively.

![](images/1622caa7a2740e1edc87638e110a25a82900f116c7200f24d622145ae03de5c5.jpg)  
Figure 4. The residual $\delta ( Z , A )$ is plotted as a function of mass number. Nine runs with randomly splitting the 2408 nuclei into the training and testing groups with the ratio of 4:1 are displayed. Blue and orange points denote $\delta ( Z , A )$ for testing data obtained with the LDM and the LightGBM refined LDM, respectively. $\sigma _ { p r e }$ is RMSD of the original LDM, $\sigma _ { p o s t }$ is RMSD of the LightGBM-refined LDM.

this result is comparable to many physical mass models. With the training data set is built from 1926 nuclei and the remaining 482 nuclei constitute the testing data set, the RMSD is obtained to be 0.234±0.022 MeV, this performance is better than many physical mass models.

Fig. 4 shows the residual $\delta ( Z , A )$ obtained from the LDM and LightGBM-refined LDM. The results from nine runs with randomly selected 80% of 2408 nuclei as the training set and the remaining 20% as the testing set are displayed. It can be seen that the residual $\delta ( Z , A )$ obtained with the original LDM is large, especially for nuclei around magic number, due to the absence of shell effect in the LDM. After the refinement of LightGBM, $\delta ( Z , A )$ is considerably reduced, especially for nuclei with mass number larger than 60. The performance of LightGBM for nuclei with mass number smaller than 60 is not as good as that for nuclei with large mass number, the same as we already observed in Fig.1. This could be improved by feeding more relevant features to LightGBM.

# B. Predictions on the binding energy based on different mass models

In the previous section, the capability of LightGBM to refine LDM has been exhibited. In this section, besides LDM, three popular mass models, i.e., DZ, WS4 and FRDM, are tested as well. To do so, the $\delta ( Z , A )$ between experimental binding energy and the one obtained from each mass model is fed to LightGBM, and we randomly split the 2408 nuclei into training and testing groups with the ratio of 4:1, and run 500 times for each mass model. The distribution of RMSD on the training and testing data sets are displayed in Fig.5. In Tab. III, the performance of serval ML refined mass models are compared. It can be seen that the typical value of RMSD on the training data set is only about 0.05-0.1 MeV, which is the smallest of all, to our best knowledge, the highest performance mass model. The typical value of RMSD on the testing data set is bout 0.2 MeV, which is also smaller than others. In general, significant improvements

![](images/ed28a17bc24bccb2469d8f104f3ccb253cabef4326ab61873019b395c1be7654.jpg)  
Figure 5. The density distribution of RMSD for training and testing data sets. Results from 500 runs for each mass model (LDM, DZ, WS4 and FRDM) are displayed. Dash lines denote Gaussian fit to the distribution. The corresponding mean value and the standard deviation are listed in Tab. III. In each run, the 2408 nuclei are randomly split into the training and testing data sets with the ratio of 4:1.

Table III. Comparison of the RMSD for the ML refined mass models. $\sigma _ { p r e }$ denotes the RMSD of the original mass models, $\sigma _ { p r e }$ is the result obtained with the LightGBM-refined mass models.   

<table><tr><td colspan="2"></td><td>LDM</td><td>DZ</td><td>WS4</td><td>FRDM</td></tr><tr><td rowspan="7">Training set</td><td>σpre</td><td>2.462 ± 0.023</td><td>0.613 ± 0.007</td><td>0.302 ± 0.003</td><td>0.599 ± 0.009</td></tr><tr><td>LMNN by H. F. Zhang [33]</td><td>0.235</td><td>0.325</td><td>—</td><td>0.348</td></tr><tr><td>BNN by Z. M. Niu [21]</td><td>—</td><td>—</td><td>0.176</td><td>0.187</td></tr><tr><td>NN by R. Utama [19]</td><td>0.466</td><td>0.274</td><td>—</td><td>0.342</td></tr><tr><td>NN by A. Pastore [42]</td><td>—</td><td>0.324</td><td>—</td><td>—</td></tr><tr><td>Trees by M. Carnini [36]</td><td>2.070</td><td>0.471</td><td>—</td><td>—</td></tr><tr><td>LightGBM in this work</td><td>0.058 ± 0.011</td><td>0.066 ± 0.010</td><td>0.055 ± 0.011</td><td>0.077 ± 0.013</td></tr><tr><td rowspan="7">Testing set</td><td>σpre</td><td>2.467 ± 0.092</td><td>0.614 ± 0.028</td><td>0.303 ± 0.011</td><td>0.599 ± 0.034</td></tr><tr><td>LMNN by H. F. Zhang</td><td>0.256</td><td>0.329</td><td>—</td><td>0.368</td></tr><tr><td>BNN by Z. M. Niu</td><td>—</td><td>—</td><td>0.212</td><td>0.252</td></tr><tr><td>NN by R. Utama</td><td>0.486</td><td>0.278</td><td>—</td><td>0.352</td></tr><tr><td>NN by A. Pastore</td><td>—</td><td>0.358</td><td>—</td><td>—</td></tr><tr><td>Trees by M. Carnini</td><td>2.881</td><td>0.569</td><td>—</td><td>—</td></tr><tr><td>LightGBM in this work</td><td>0.234 ± 0.022</td><td>0.213 ± 0.018</td><td>0.170 ± 0.011</td><td>0.222 ± 0.016</td></tr></table>

of about 90%, 65%, 40%, and 60% after the LightGBM refinement on the LDM, DZ, WS4, and FRDM are obtained, indicating the strong capability of LightGBM to improve theoretical nuclear mass models.

Very recently, the AME2020 was published, thus it is interesting to see whether the LightGBM-refined mass models also work well for newly measured nuclei that appeared in the AME2020 mass evaluation. The comparison of the binding energy obtained with LDM,

DZ, WS4, and FRDM and LightGBM-refined mass models on the 66 newly measured nuclei that appeared in the AME2020 are illustrated in Fig.6. The RMSD of the original mass models on these newly measured nuclei are 2.468, 0.821, 0.350, and 0.778 MeV for the LDM, DZ, WS4, and FRDM, respectively. After the refinement of LightGBM, the RMSD of the above four mass models is significantly reduced to 0.452, 0.320, 0.222, and 0.292 MeV.

![](images/b4cb737fae07aec99991ab03dba7c60efc6052d27bee29379316a705effaa19c.jpg)  
Figure 6. The difference between the theoretical and the experimental binding energies (red horizontal line) obtained using LDM, DZ, WS4, and FRDM (open diamonds) and LightGBM-refined mass models (solid squares). The results of 66 newly measured nuclei that appeared in the AME2020 mass evaluation are displayed. $\sigma _ { p r e }$ and $\sigma _ { p o s t }$ denote the RMSD of the original and the LightGBM-refined mass models on the newly measured nuclei, respectively. The error of the predictions obtained with the LightGBM-refined mass models is the standard deviation of the predicted binding energy. It is obtained by running LightGBM 500 times with randomly splitting AME2016 data into training and testing sets with the ratio of 4:1.

# C. Extrapolation of Neutron Separation Energy

Single and two-neutron separation energies are of particular interest, because they provide information relevant to shell and subshell structure, nuclear deformation, paring effects, as well as the boundary of the nuclear landscape. They can be calculated by the following formula:

$$
\left\{ \begin{array}{l} S _ {n} (Z, A) = B (Z, A) - B (Z, A - 1) \\ S _ {2 n} (Z, A) = B (Z, A) - B (Z, A - 2). \end{array} \right. \tag {3}
$$

Good performance of the LightGBM-refined mass models on the prediction of nuclear binding has been shown, it is interesting to see whether the single and two-neutron separation energies also can be reproduced well on the same foot. Fig.7 compares the single neutron separation energy of Ca, Zr, Sn, and Pb isotopic chains given by different theoretical models and the experimental data from AME2016. All predictions are in good agreement with experimental data whenever there has data, while discrepancy appears as the increase of neutron number. The general trend of the $S _ { n }$ as a function of neutron number obtained with LightGBMrefined LDM and WS4 are similar as that obtained with

other nuclear mass models, e.g., the odd-even staggering also can be observed.

The latest experimental measurements of the twoneutron separation energy of the four elements (Ca, Ti, Pm, Sm) are compared with various theoretical model calculations in Fig. 8. It can be seen that the newly measured $S _ { 2 n }$ can be well reproduced by LightGBMrefined LDM and WS4 models, particularly, $S _ { 2 n }$ obtained with LightGBM-refined LDM lies much more closely to the experimental data than that obtained with LDM. For example, the sharp decrease of $S _ { 2 n }$ around magic number cannot be reproduced by LDM, while this issue can be fixed after the refinement of LightGBM. Good performance of LightGBM-refined mass models on both $S _ { n }$ and $S _ { 2 n }$ indicating again the strong capacity of LightGMB on refining nuclear mass model.

# D. Interpretability of the model

As a decision-tree based algorithm, one of advantage of LightGBM is its excellent degree of explainability. This is important because, as physicist, one expecting ML algorithm not only has a good performance on refining nuclear mass models, but also can provide some underlying physics that is absent from the original

![](images/74bb0244c8e27f1ab1595d6552bc2e06afc3f7b02c575b26a7450114da7927a8.jpg)

![](images/8c666c840bc93234c3954fb888a0959421ed3c74d773a5f8cf3f5ced13298b6a.jpg)  
Figure 7. Single neutron separation energy of Ca, Zr, Sn, and Pb isotopic chains given by different models. The results obtained using LightGBM-refined LDM and WS4 are compared with FRDM, WS4, as well as recent theoretical calculations given by Xia et al. [16] , Ma et al. [43] , and Yu et al. [44].   
Figure 8. Two-neutron separation energy of the neutron-rich nuclei on Ca, Ti, Pm, Sm isotopic chains given by different models. The red stars and green dots represent the experimental data from AME2016 and the latest measurement from Refs.[45, 46]. The neutron number of the predicted drip line isotopes (Ca and Ti) in each nuclear mass model are also listed in the figure. Note that $S _ { 2 n }$ obtained with WS4 and LightGBM-refined WS4 are almost completely overlapped.

nuclear mass models. Understanding what happens when ML algorithms make predictions that could help us further improving our knowledge about the relationship between the input feature quantity and the predicted value. One of the possible way to understand how the LightGBM algorithm gives a particular prediction is to appreciate the most important features that

drive the model. For this purpose, SHapley Additive exPlanation (SHAP) [47], which is one of the most popular feature attribution methods, is applied to obtain the contributions of each feature value to the prediction. Fig.10 illustrates the ranking of importance of the input 10 features. The top is the most important feature, while the bottom is the most irrelevant feature, to

![](images/09955ccf16e16487d0b03acc60df6db35211f7daf02d77bc303f142ffeebfcf1.jpg)

![](images/263e9b58a06347a581d91bac708244c53bc5f906d6db81196bcef9e61d73b6ff.jpg)

![](images/4c7c31ae83feb90228e904aee59b13a1e707bca0d0603d87ede55f93cd9d67c3.jpg)

![](images/8fca239b0a16afba316ce49cd54b3b362edd370866f151a4b00dcb48b9f92a72.jpg)  
Figure 9. Importance ranking for the input features obtained with SHAP package. Each row represents a feature, and the x-axis is the SHAP value which shows how important a feature is for a particular prediction. Each point represents a nucleus, and the color represents the feature value (red is high, blue is low).

predict the residual $\delta ( Z , A )$ between the experimental and theoretical binding energy. It can be seen that the importance ranks of input features are different for different mass models. Because shell effects are not included in LDM, the residual $\delta ( Z , A )$ around magic numbers are usually larger (also can be seen in Fig.4). As a result, $| N - m |$ and $| Z - m |$ are more important to predict the $\delta ( Z , A )$ between LDM calculation and experimental data. To demonstrate the meaning of SHAP value, residual $\delta ( Z , A )$ obtained from LDM and SHAP value are shown in Fig.10. In the upper panel of Fig.10, around magic number, i.e., $| N - m |$ is close to 0, larger difference between LDM calculated and experimental binding energy is existed, especially for nuclei with larger neutron number. While very similar behavior for SHAP value can be seen in the lower panel. It implies that by adding a $| N - m |$ -related term in the LDM, the accuracy of LDM on calculating nuclear binding energy can be improved to some extend. For FRDM, the neutron number $N$ stands for the most relevant feature and the SHAP value for smaller $N$ is usually larger. Indeed, the residual $\delta ( Z , A )$ for nuclei with smaller neutron number $N$ is larger has already been observed in FRDM paper, i.e., Fig. 6 of Ref. [48]. In addition, one sees that $N _ { p a i r }$ , $Z _ { m }$ , and $N _ { m }$ are three of the most irrelevant features to predict the residual

$\delta ( Z , A )$ , it means that the performance on predicting $\delta ( Z , A )$ may not be influenced if they are removed from input features.

# IV. CONCLUSION AND OUTLOOK

To summarize, several features are fed into the LightGBM algorithm to study the residual $\delta ( Z , A )$ between the theoretical and experimental binding energies, it turns out that LightGBM algorithm can mimic the patterns of $\delta ( Z , A )$ with high accuracy, so as to refine theoretical mass models. In this work, significant reductions on the RMSD of about 90%, 65%, 40%, and $6 0 \%$ after the LightGBM refinement on the LDM, DZ, WS4, and FRDM are obtained, indicating the strong capability of LightGBM to improve theoretical nuclear mass models. In addition, the RMSD for various mass models with respect to the 66 newly measured nuclei that appeared in AME2020 (compared with AME2016) is reduced on the same level as well. Furthermore, it is found that single and two-neutron separation energies obtained with the LightGBM-refined mass models are in good agreement with the newly appeared experimental data. By using the SHAP package, the most relevant input features to predict the residual $\delta ( Z , A )$ for each

![](images/1264248304264cdc94af29a09d7eb9636a9d661ebb2ca877c758cf237a14b626.jpg)  
Figure 10. Upper: The residual $\delta ( Z , A )$ obtained from LDM is plotted against $| N - m |$ colored by neutron number. Each point represents a nucleus, and the color represents the number of neutron in a nucleus. Lower: The same as the upper one but SHAP value is plotted instead of the residual $\delta ( Z , A )$ .

mass model are found out, which may provide guidance for the further developments of nuclear mass models.

The good performance of machine learning method on refining the nuclear mass model gives us a new tool to further investigate other properties of nuclei that we are interested in, such as, superheavy nuclei, halo nuclei, and nuclei around drip-line. In addition, with the development of the interpretable machine learning methods, more physical hints can be obtained thereby improving our understanding of present nuclear models.

# ACKNOWLEDGMENTS

Fruitful discussions with Prof. Jie Meng, Prof. Hongfei Zhang, Prof. Yumin Zhao, Dr. Nana Ma are greatly appreciated. The authors acknowledge support by the computing server C3S2 in Huzhou University. The work is supported in part by the National Science Foundation of China Nos. U2032145, 11875125, and 12047568, and the National Key Research and Development Program of China under Grant No. 2020YFE0202002, and the “Ten Thousand Talent Program" of Zhejiang province (No. 2018R52017). The mass table for the LightGBM-refined mass models is available in the Supplemental Material.

[1] D. Lunney, J. M. Pearson and C. Thibault, Rev. Mod. Phys. 75, 1021-1082 (2003). doi:10.1103/RevModPhys.75.1021   
[2] K. Blaum, Phys. Rep. 425, 1 (2006).   
[3] F. Wienholtz, D. Beck, K. Blaum, C. Borgmann, M. Breitenfeldt, R. B. Cakirli, S. George, F. Herfurth, J. D. Holt and M. Kowalska, et al. Nature 498, no.7454, 346-349 (2013) doi:10.1038/nature12226   
[4] K. Blaum, J. Dilling and W. Nortershauser, Phys. Scripta T 152, 014017 (2013) doi:10.1088/0031- 8949/2013/T152/014017 [arXiv:1210.4045 [physics.atom-ph]].   
[5] Z. Niu, H. Liang, B. Sun, Y. Niu, J. Guo and J. Meng, Sci. Bull. 63, 759-764 (2018) doi:10.1016/j.scib.2018.05.009 [arXiv:1807.05535 [nuclth]].   
[6] Wang M, Zhang Y H, Zhou X H. Nuclear mass measurements (in Chinese). Sci Sin-Phys Mech Astron, 2020, 50: 052006, doi: 10.1360/SSPMA-2019- 0308   
[7] C. Ma, M. Bao, Z. M. Niu, Y. M. Zhao and A. Arima, Phys. Rev. C 101, no.4, 045204 (2020) doi:10.1103/PhysRevC.101.045204   
[8] M. Wang, G, Audi, F. G. Kondev, W. J. Huang, S. Naimi, and X. Xu, Chinese Physics C(2017).   
[9] P. Möller, W. D. Myers, H. Sagawa and S. Yoshida,

Phys. Rev. Lett. 108, no.5, 052501 (2012) doi:10.1103/PhysRevLett.108.052501   
[10] P. Möller, J. R. Nix, W. D. Myers and W. J. Swiatecki, Atom. Data Nucl. Data Tabl. 59, 185-381 (1995) doi:10.1006/adnd.1995.1002 [arXiv:nucl-th/9308022 [nucl-th]].   
[11] N. Wang, M. Liu, X. Wu and J. Meng, Phys. Lett. B 734, 215-219 (2014) doi:10.1016/j.physletb.2014.05.049 [arXiv:1405.2616 [nucl-th]].   
[12] S. Goriely, N. Chamel and J. M. Pearson, Phys. Rev. C 93, no.3, 034337 (2016) doi:10.1103/PhysRevC.93.034337   
[13] S. Goriely, N. Chamel and J. M. Pearson, Phys. Rev. Lett. 102, 152503 (2009) doi:10.1103/PhysRevLett.102.152503 [arXiv:0906.2607 [nucl-th]].   
[14] Y. Aboussir, J. M. Pearson, A. K. Dutta and F. Tondeur, Atom. Data Nucl. Data Tabl. 61, 127-176 (1995) doi:10.1016/S0092-640X(95)90014-4   
[15] L. S. Geng, H. Toki and J. Meng, Prog. Theor. Phys. 113, 785-800 (2005) doi:10.1143/PTP.113.785 [arXiv:nuclth/0503086 [nucl-th]].   
[16] X. W. Xia, Y. Lim, P. W. Zhao, H. Z. Liang, X. Y. Qu, Y. Chen, H. Liu, L. F. Zhang, S. Q. Zhang and Y. Kim, et al. Atom. Data Nucl. Data Tabl. 121-122, 1-215

(2018) doi:10.1016/j.adt.2017.09.001 [arXiv:1704.08906 [nucl-th]].   
[17] C. Giuseppe, C. Ignacio, C. Kyle et al., Rev. Mod. Phys. 91, 045002 (2019).   
[18] Radovic. A, Williams, Rousseau. D et al., Nature 560, 41 (2018).   
[19] R. Utama, J. Piekarewicz and H. B. Prosper, Phys. Rev. C 93, no.1, 014311 (2016) doi:10.1103/PhysRevC.93.014311 [arXiv:1508.06263 [nucl-th]].   
[20] R. Utama and J. Piekarewicz, Phys. Rev. C 96, no.4, 044308 (2017) doi:10.1103/PhysRevC.96.044308 [arXiv:1704.06632 [nucl-th]].   
[21] Z. M. Niu and H. Z. Liang, Phys. Lett. B 778, 48-53 (2018) doi:10.1016/j.physletb.2018.01.002 [arXiv:1801.04411 [nucl-th]].   
[22] R. Utama, W. C. Chen and J. Piekarewicz, J. Phys. G 43, no.11, 114002 (2016).   
[23] Z. A. Wang, J. C. Pei, Y. Liu, Phys. Rev. Lett 123, 122501 (2019).   
[24] C. W. Ma, D. Peng, H. L. Wei, Y. T. Wang and J. Pu, Chin. Phys. C 44, no.12, 124107 (2020).   
[25] C. W. Ma, D. Peng, H. L. Wei, Z. M. Niu, Y. T. Wang and R. Wada, Chin. Phys. C 44, no.1, 014104 (2020).   
[26] Z. M. Niu, H. Z. Liang, B. H. Sun, W. H. Long and Y. F. Niu, Phys. Rev. C 99, no.6, 064307 (2019) doi:10.1103/PhysRevC.99.064307 [arXiv:1810.03156 [nucl-th]].   
[27] L. G. Pang, K. Zhou, N. Su et al., Nat. Commun 9 210 (2018).   
[28] Y. L. Du, K. Zhou, J. Steinheimer, L. G. Pang, A. Motornenko, H. S. Zong, X. N. Wang and H. Stöcker, Eur. Phys. J. C 80, no.6, 516 (2020) doi:10.1140/epjc/s10052- 020-8030-7 [arXiv:1910.11530 [hep-ph]].   
[29] J. Steinheimer, L. Pang, K. Zhou, V. Koch, J. Randrup and H. Stoecker, JHEP 12, 122 (2019).   
[30] Y. D. Song, R. Wang, Y. G. Ma, X. G. Deng and H. L. Liu, Phys. Lett. B 814, 136084 (2021) doi:10.1016/j.physletb.2021.136084 [arXiv:2101.10613 [nucl-th]].   
[31] R. Wang, Y. G. Ma, R. Wada, L. W. Chen, W. B. He, H. L. Liu and K. J. Sun, Phys. Rev. Res. 2, no.4, 043202 (2020)   
[32] F. Li, Y. Wang, H. Lü, P. Li, Q. Li and F. Liu, J. Phys. G 47, no.11, 115104 (2020).   
[33] H. F. Zhang, L. H. Wang, J. P. Yin, P. H. Chen and H. F. Zhang, J. Phys. G 44, no.4, 045110 (2017) doi:10.1088/1361-6471/aa5d78   
[34] M. Shelley and A. Pastore, arXiv:2102.07497 (2021).   
[35] L. Neufcourt, Y. Cao, W. Nazarewicz and F. Viens, Phys. Rev. C 98, no.3, 034318 (2018)

doi:10.1103/PhysRevC.98.034318 [arXiv:1806.00552 [nucl-th]].   
[36] M. Carnini and A. Pastore, J. Phys. G 47, no.8, 082001 (2020) doi:10.1088/1361-6471/ab92e3 [arXiv:2002.10290 [nucl-th]].   
[37] Esra Yüksel, Derya Soydaner, and Hüseyin Bahtiyar, arXiv:2101.12117v1 (2021).   
[38] K. A. Gernoth, J. W. Clark, J. S. Prater and H. Bohr, Phys. Lett. B 300, 1-7 (1993) doi:10.1016/0370- 2693(93)90738-4   
[39] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth and J. W. Clark, Nucl. Phys. A 743, 222-235 (2004) doi:10.1016/j.nuclphysa.2004.08.006 [arXiv:nuclth/0307117 [nucl-th]].   
[40] J. W. Clark and H. Li, Int. J. Mod. Phys. B 20, no.30n31, 5015-5029 (2006) doi:10.1142/S0217979206036053 [arXiv:nucl-th/0603037 [nucl-th]].   
[41] J. Duflo and A. P. Zuker, Phys. Rev. C 52, R23 (1995) doi:10.1103/PhysRevC.52.R23 [arXiv:nuclth/9505011 [nucl-th]].   
[42] A. Pastore, D. Neill, H. Powell, K. Medler and C. Barton, Phys. Rev. C 101, no.3, 035804 (2020) doi:10.1103/PhysRevC.101.035804 [arXiv:1912.11365 [nucl-th]].   
[43] N. N. Ma, H. F. Zhang, X. J. Bao and H. F. Zhang, Chin. Phys. C 43, no.4, 044105 (2019) doi:10.1088/1674- 1137/43/4/044105   
[44] H. C. Yu, M. Q. Lin, M. Bao, Y. M. Zhao and A. Arima, Phys. Rev. C 100, no.1, 014314 (2019) doi:10.1103/PhysRevC.100.014314   
[45] S. Michimasa, M. Kobayashi, Y. Kiyokawa, S. Ota, R. Yokoyama, D. Nishimura, D. S. Ahn, H. Baba, G. P. A. Berg and M. Dozono, et al. Phys. Rev. Lett. 125, no.12, 122501 (2020) doi:10.1103/PhysRevLett.125.122501   
[46] M. Vilen, J. M. Kelly, A. Kankainen, M. Brodeur, A. Aprahamian, L. Canete, T. Eronen, A. Jokinen, T. Kuta and I. D. Moore, et al. Phys. Rev. Lett. 120, no.26, 262701 (2018) [erratum: Phys. Rev. Lett. 124, no.12, 129901 (2020)] doi:10.1103/PhysRevLett.120.262701 [arXiv:1801.08940 [nucl-ex]].   
[47] S. Lundberg, S. I. Lee. arXiv:1705.07874 (2017) [cs.AI].   
[48] P. Möller, A. J. Sierk, T. Ichikawa and H. Sagawa, Atom. Data Nucl. Data Tabl. 109-110, 1-204 (2016) doi:10.1016/j.adt.2015.10.002 [arXiv:1508.06294 [nuclth]].   
[49] Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, Tie-Yan Liu. “LightGBM: A Highly Efficient Gradient Boosting Decision Tree.” Advances in Neural Information Processing Systems 30 (NIPS 2017), pp. 3149-3157.