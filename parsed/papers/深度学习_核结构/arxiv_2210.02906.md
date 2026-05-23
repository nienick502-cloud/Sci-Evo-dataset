# Nuclear binding energies in artificial neural networks

Lin-Xing Zeng,1 Yu-Ying Yin,1 Xiao-Xu Dong,1 and Li-Sheng Geng2, 1, 3, 4, ∗

1School of Physics, Beihang University, Beijing 102206, China

2Peng Huanwu Collaborative Center for Research and Education, Beihang University, Beijing 100191, China

3Beijing Key Laboratory of Advanced Nuclear Materials and Physics, Beihang University, Beijing 102206, China

4School of Physics and Microelectronics, Zhengzhou University, Zhengzhou, Henan 450001, China

# Abstract

The binding energy (BE) or mass is one of the most fundamental properties of an atomic nucleus. Precise binding energies are vital inputs for many nuclear physics and nuclear astrophysics studies. However, due to the complexity of atomic nuclei and of the non-perturbative strong interaction, up to now, no conventional physical model can describe nuclear binding energies with a precision below 0.1 MeV, the accuracy needed by nuclear astrophysical studies. In this work, artificial neural networks (ANNs), the so called “universal approximators”, are used to calculate nuclear binding energies. We show that the ANN can describe all the nuclei in AME2020 with a root-mean-square deviation (RMSD) around 0.2 MeV, which is better than the best macroscopic-microscopic models, such as FRDM and WS4. The success of the ANN is mainly due to the proper and essential input features we identify, which contain the most relevant physical information, i.e., shell, paring, and isospin-asymmetry effects. We show that the well-trained ANN has excellent extrapolation ability and can predict binding energies for those nuclei so far inaccessible experimentally. In particular, we highlight the important role played by “feature engineering” for physical systems where data are relatively scarce, such as nuclear binding energies.

# I. INTRODUCTION

The atomic nucleus is a quantum many-body system with an extremely complex structure [1]. As one of the most fundamental properties of atomic nuclei, binding energies (BE) can provide crucial information on nuclear shapes [2], shell effects [3, 4] , pairing effects [5], and the disappearance as well as emergence of magic numbers [4, 6]. In addition, binding energies are essential inputs for superheavy nuclei syntheses [7] and nuclear astrophysical studies [8], e.g., the r-process ([9, 10]), X-ray bursts [11], and etc. Therefore, reliable theoretical predictions and experimental measurements of nuclear binding energies have always been at the frontier of nuclear physics [12–14].

In the latest atomic mass evaluation (AME 2020) [15], the masses of 3556 nuclei (including measured and extrapolated) are compiled. However, various theoretical models predict that about 8000 to 10000 nuclei may exist [12, 13, 16, 17], including most of those relevant in nuclear elements syntheses. Therefore, reliable and accurate theoretical predictions are in urgent need. Some of the most widely used theoretical models include the Weizsacker-Skyrme model (WS) [18– 22], the Relativistic Mean Field model (RMF) [17, 23], the Duflo-Zuker model (DZ) [24], the Hartree-Fock-Bogoliubov model [25–28], the Finite-Range Droplet model (FRDM) [12, 29, 30], and the RCHB [13] and DRHBc [31] models. Most of these models can describe the experimental data with a root-mean-square deviation (RMSD) ranging from about $0 . 3 ~ \mathrm { M e V }$ to several MeV. Among them, FRDM2012 [30] achieved an RMSD of $0 . 5 7 0 \mathrm { M e V }$ while the Weizsacker-Skyrme (WS4) [22] model gives the best description with an RMSD of 0.298 MeV. In general. the macromicro models, rather than the more “physical” microscopic models, perform better in describing nuclear masses because their parameters are determined by fitting to all the (then available) experimental data.

In recent years, artificial neural networks (ANNs), as one of the most powerful machine learning methods, have been successfully applied in nuclear physics studies [9, 32], e.g., binding energies [33–37] , charge radii [38–41], $\alpha$ -decay half-lives [42] , $\beta$ -decay half-lives [43], and fission fragment yields [44–46].

The studies of nuclear binding energies (masses) can be divided into two categories, i.e., either fitting to the experimental data directly or to the residuals between experimental data and model predictions. In Refs. [33, 37, 47–50], mass residuals are utilized to refine the theoretical models. In Refs. [33–35, 37], Bayesian neural networks are found to be able to describe nuclear binding

energies with an RMSD ranging from 0.266 to 0.850 MeV. The RMSD obtained in the WS4 supplemented with Light Gradient Boosting Machine (LightGBM) is $0 . 1 7 0 \pm 0 . 0 1 1 \ \mathrm { M e V }$ [48]. The Bayesian machine learning (BML) method proposed in Ref. [51] achieves an RMSD of 84 keV, the first crossing the $1 0 0 \mathrm { k e V }$ threshold.

However, there are fewer works that study the experimental data directly. In Refs. [36, 52], feed-forward neural networks with different structures are explored. Ref. [36] yielded an RMSD of $1 . 8 4 ~ \mathrm { M e V }$ for 1071 nuclei contained in AME2016 [53] as the test set. 1 Ref. [52] applied the data augmentation technique to expand the data set, and the RMSD decreased to 1.322 MeV for the test set within the training data region and $1 . 4 9 5 \mathrm { M e V }$ for the new nuclei beyond the training data region. In Refs. [54, 55], mixed density networks with 12 physically motivated features [55] or eight features constrained by the GK relation [54] are devised to describe nuclear mass excesses. In the latter work [54], an RMSD of 0.316 MeV for the test set and 0.186 MeV for the training set for nuclei with $Z \ge 2 0$ was achieved, whose performance is comparable to that of WS4 [22].

In this work, we develop an ANN with seven input features of most relevance. We find that among the 12 features studied in Ref. [55], only six of them are effective in our network. Meanwhile, we find that taking GeLU [56] as the activation function enhances the predictive power of the ANN. Our ANN provides a better description of nuclear binding energies than all the conventional models and in addition shows good extrapolation ability.

This article is organized as follows. In section II, we explain how to construct the ANN and determine the physically motivated input features. Results and discussions are presented in Section III. A short summary and outlook is provided in Section IV.

# II. THEORETICAL FORMALISM

In this section, we introduce the ANN and mass data we used in detail.

# A. Artificial neural network

Generally speaking, an ANN is a supervised machine learning method which is also regarded as a “universal approximator”. The ANN used in this work is a fully connected feed-forward neural network, consisting of one input layer with seven features, two hidden layers, and one output layer

as shown in Fig. 1. The inputs $I _ { j }$ and outputs $O _ { j }$ of layer $j$ are connected as follows

$$
O _ {j} = f \left(W _ {j} \cdot I _ {j} + b _ {j}\right), \tag {1}
$$

where $j$ runs over the input layer and the hidden layers, $W _ { j }$ are the weights, $b _ { j }$ are the bias, and $f$ is the activation function to be specified. For the output layer, no activation function is needed.

Although in principle one could improve the description of BEs with either more hidden layers or more nodes in each hidden layer, one often ends up with the over-fitting problem. By trial and error, we find that with two hidden layers and about 800 parameters, our ANNs can well describe the binding energies. For a ANN with $I$ inputs, two hidden layers, and one output, denoted as $[ I , H 1 , H 2 , O ]$ , the number of parameters is $( I + 1 ) \times H 1 + ( H 1 + 1 ) \times H 2 + ( H 2 + 1 ) \times O$ . Table I lists the nodes and number of parameters of the different ANNs investigated in the present work. Note that to better understand how the different input features affect the performance of ANNs, in addition to the default ANN with seven features, we also study three other ANNs, where two, four, and six features are used. For the activation function, we choose GeLU [56], which is found to perform better than Tanh. For the loss function, we use the standard mean absolute error (MAE):

$$
L O S S = \frac {\sum_ {i = 1} ^ {N} \left| B E _ {i} ^ {t h} - B E _ {i} ^ {e x p} \right|}{N}. \tag {2}
$$

For numerical implementation, we use the optimized tensor library PYTORCH [57] and employ the Adam algorithm [58] with a learning rate 0.0001 and the decay constants 0.9 and 0.999. The weight matrices of our ANNs are initialized in PYTORCH with the same random seed.

TABLE I. Structure, number of parameters, and input features of the different ANNs studied in the present work.   

<table><tr><td>Model</td><td>Structure</td><td>Number of parameters</td><td>Input features</td></tr><tr><td>ANN2</td><td>[2, 35, 19, 1]</td><td>809</td><td>Z, N</td></tr><tr><td>ANN4</td><td>[4, 35, 17, 1]</td><td>805</td><td>Z, N, ZEO, NEO</td></tr><tr><td>ANN6</td><td>[6, 32, 17, 1]</td><td>803</td><td>Z, N, ZEO, NEO, ΔZ, ΔN</td></tr><tr><td>ANN7</td><td>[7, 32, 16, 1]</td><td>801</td><td>Z, N, ZEO, NEO, ΔZ, ΔN, ASY</td></tr></table>

A supervised ANN maps inputs to the desired outputs. In the present case, the output is the binding energy of a nucleus. As an atomic nucleus is completely determined by its proton and

neutron numbers, one can naively take them as the only inputs. Nevertheless, it is well known that for small data sets, engineered features (in addition to these “fundamental features”) , which encode important information (priors) about the system under investigation, can play an invaluable role in enhancing the capacity of ANNs. Such a technique is widely used in nuclear physics studies (see, e.g., [38, 39, 54, 55]). In Ref. [38], it was shown that in addition to $N$ and $Z$ , with two more features accounting for the pairing and shell-closure effects, one is able to describe the nuclear charge radii much better than the Bayesian models without these two features. In particular, one is able to describe the strong odd-even staggerings of the charge radii of the calcium and potassium isotopes. In Ref. [39], it was shown that the description can be further improved with two more features accounting isospin dependence and local anomalies.

In the studies of binding energies, in addition to the above mentioned pairing, shell-closure, and isospin dependence effects, many other features have been studied [42, 55]. In the present work, we find that the most relevant features are those just mentioned, i.e., pairing, shell-closure, and isospin dependence. The pairing effects are encoded in $Z _ { E O }$ and $N _ { E O }$ , which is 1 when $Z / N$ is odd, or 0 otherwise. Shell effects are introduced via $\Delta Z$ and $\Delta N$ , which are the differences between $Z$ and $N$ and the closest magic numbers. In this work, the magic numbers are taken to be 8, 20, 28, 50, 82, 126, and 184. As one moves from the beta-stability line, isospin-asymmetry becomes large. Therefore, we take into account this effect by introducing the seventh feature, ASY, which is defined as

$$
A S Y = \left(1 - \frac {\kappa}{A ^ {1 / 3}} + \xi \frac {2 - | I |}{2 + | I | A}\right) I ^ {2} A f _ {s} \tag {3}
$$

where the parameters $\kappa , \xi$ , and $f _ { s }$ are taken from WS4 [22].

# B. Mass data

AME2020 [15], in which the masses of 3556 nuclei (including measured and extrapolated ones) are compiled, is referred to as the data set in this work. The training set and test set are extracted from AME2020 as follows. The nuclei in the training set are those which were already in AME2016 [53], and the rest of nuclei that are not in AME2016 but in AME2020 are chosen as the test set (test20). Based on this selection, there are 3434 nuclei in the training set and 122 nuclei in the test set.

![](images/779845460bef8e67681ae3b7bfce34a21660812f5d5521bede950f6b371d3c9b.jpg)  
FIG. 1. Architecture of a neural network consisting of seven input features, two hidden layers of nine and eight nodes, and one output layer.

# III. RESULTS AND DISCUSSIONS

To quantify how well the ANN can describe nuclear binding energies in the training and test sets, we use the standard root-mean-square deviation (RMSD), $\sigma _ { r m s }$ , defined as

$$
\sigma_ {r m s} = \sqrt {\sum_ {i} ^ {N} \frac {\left(B E _ {i} ^ {\mathrm {t h}} - B E _ {i} ^ {\exp}\right) ^ {2}}{N}}, \tag {4}
$$

where $B E _ { i } ^ { \mathrm { t h } }$ are the ANN predictions and $B E _ { i } ^ { \mathrm { e x p } }$ are the experimental binding energies contained in the training and test sets footnoteIn the present work, we do not distinguish between the measured and extrapolated masses compiled in the mass evaluations (AME2016 and AME2020).

TABLE II. RMSDs for the training set (consisting of 3434 nuclei) and test set (consisting of 122 nuclei) achieved using different network structures.   

<table><tr><td rowspan="2">Model</td><td colspan="3">σrms (MeV)</td></tr><tr><td>Training set</td><td>Test set</td><td>Entire set</td></tr><tr><td>ANN2</td><td>1.183</td><td>1.053</td><td>1.178</td></tr><tr><td>ANN4</td><td>0.548</td><td>0.628</td><td>0.551</td></tr><tr><td>ANN6</td><td>0.289</td><td>0.514</td><td>0.299</td></tr><tr><td>ANN7</td><td>0.190</td><td>0.340</td><td>0.197</td></tr></table>

TABLE III. Comparisons between ANN7 and the WS4 model [59], for nuclei with $Z \ge 8$ and $N \geq 8$ compiled in AME2020, i.e., 3336 nuclei and 120 nuclei contained in our training set and test set, respectively.   

<table><tr><td rowspan="2">Model</td><td colspan="3">σrms (MeV)</td></tr><tr><td>Training set</td><td>Test set</td><td>Entire set</td></tr><tr><td>ANN7</td><td>0.149</td><td>0.336</td><td>0.159</td></tr><tr><td>WS4</td><td>0.415</td><td>1.295</td><td>0.474</td></tr></table>

The $\sigma _ { r m s }$ obtained with different number of input features are shown in Table II. For the entire set, the RMSD reduces from $1 . 1 7 8 ~ \mathrm { M e V }$ in ANN2 to $0 . 1 9 7 ~ \mathrm { M e V }$ in ANN7. This demonstrates unambiguously that using engineered features that explicitly encode the pairing, shell and isospinasymmetry effects is able to significantly improve the capacity of ANNs to describe/predict nuclear binding energies. We stress that the total number of parameters are similar for all the four network structures. From ANN2 to ANN4, with the features ( $Z _ { e o }$ and $N _ { E O }$ ), the descriptions improve in not only the training set but also the test set. The RMSD decreases by almost 50 percent from ANN2 to ANN4. The explicit consideration of shell effects ( $\Delta Z$ and $\Delta N$ ) further improves the descriptions, and the RMSD for the entire set crosses the $0 . 3 \mathrm { M e V }$ threshold. Finally, the explicit consideration of the asymmetry effects further improves the description, and the RMSD of ANN7 (for the training set and entire set) falls below 0.2 MeV.

To put the performance of ANN7 into better perspective, we compare it with one of the most refined conventional models, WS4, which only studied those nuclei with $Z \ge 8$ and $N \ge 8$ , i.e., only 3336 nuclei and 120 nuclei among those contained in our training and test sets. The corresponding $\sigma _ { r m s }$ ’s are given in Table III. Three things are noteworthy. First, ANN7 performs

better than WS4 for all the three sets of data. Second, removing the light nuclei with $Z < 8$ or $N < 8$ , the RMSD of ANN7 decreases from 0.2 to 0.16 for the entire set. Third, from the training set to the test set, the RMSDs of both ANN7 and WS4 increase. Somehow surprisingly, in terms of percentage, the increase of WS4 is even larger than that of ANN7. We note in passing that for the 2353 nuclei studied in WS4 [22], ANN7 gives an RMSD of $0 . 1 5 4 \mathrm { M e V } ,$ , which should be compared with that of WS4, 0.293 MeV.

Fig. 2 and Fig. 3 provide more details on the deviations of the ANN predictions from the experimental data. As can be seen from Fig. 2, ANN2 performs relatively worse for even-even nuclei than for their neighboring nuclei (even-odd or odd-odd). With two more features $Z _ { E O }$ and $N _ { E O }$ , which take into account explicitly the pairing effects, ANN4 improves the description of even-even nuclei, and the $\sigma _ { r m s }$ is reduced from 1.053 MeV to $0 . 6 2 8 ~ \mathrm { M e V }$ for the test set and from $1 . 1 8 3 \ \mathrm { M e V }$ to $0 . 5 4 8 ~ \mathrm { M e V }$ for the training set. However, ANN4 does not capture the shell effects. One can see from the bottom panel of Fig. 2, the deviations between the ANN predictions and the experimental data are larger for those nuclei with either proton or neutron number being magic. For doubly magic nuclei, the deviation is particularly large. With the shell effects taken into account, the ANN6 successfully describes these nuclei as can be seen from the upper panel of Fig. 3. A closer examination of Fig. 3 reveals that for heavy nuclei with $N \sim 1 7 5$ and light nuclei with $N \sim 2 0$ and $Z \sim 2 5$ , the deviations are relatively large. We note that these nuclei are more neutron rich which are newly compiled in AME2020. As a result, one can anticipate that an improved description can be achieved by considering a feature that explicitly takes into account isospin asymmetry. This is indeed the case. The $\sigma _ { r m s }$ of ANN7 for the test set decreases from $0 . 5 1 4 \mathrm { M e V }$ to $0 . 3 4 0 \mathrm { M e V } ,$ even though the deviations for some light nuclei are still relatively large.

It is instructive to examine how the different ANNs perform for nuclei in different mass regions. In Fig. 4, we show the distribution of $\sigma _ { r m s }$ over different nuclei from light to heavy. It is clear that on average ANN7 performs the best, but for light nuclei with $A < 4 0$ , ANN4 is the best. For nuclei with $1 2 0 < A < 1 6 0$ , ANN7 and ANN6 work similarly well but ANN6 is slightly better. The fact that ANN7 is better than ANN6 for light and heavy nuclei indicates that the ASY feature plays an important role. Even though for nuclei with $8 0 \leq A < 2 0 0$ , their RMSDs are both small, as shown in Fig. 5, the generalizability of ANN7 is more robust .

It is interesting to study the performance of different network structures as one moves away from the beta stability line. In Fig. 5, we decompose those nuclei in the test set into seven groups in

![](images/256bf90cf5580fccb7b073dfe4c80f8f6bbc4d762406bc1435560478091506d7.jpg)

![](images/2922d4555e5f98c5f63ad83426790e61151f184cd8c7ceec8e4021006e9ad0f8.jpg)  
FIG. 2. Absolute deviations of the ANN2 and ANN4 predictions from the experimental binding energies. The gray lines denote the magic numbers.

![](images/ce9f97fa686cec17b1850a2284b29a15919c786710c627c38f2a2843e75c1c14.jpg)

![](images/8ca84d5ee486d081e508826d2c6d34159b08a8dc724084458c14d5ee316b029a.jpg)  
FIG. 3. Absolute deviations of the ANN6 and ANN7 predictions from the experimental binding energies. The gray lines denote the magic numbers.

![](images/1faecf625edec9f8295d4f199e131b7cb28d0a0905e2866969b4d9c6df9772f3.jpg)  
FIG. 4. Distributions of $\sigma _ { r m s }$ between every 40 mass numbers in test20.

terms of $| N - Z |$ to judge the predictive powers of ANNs in different isospin-asymmetry regions.It is obvious that ANN7 achieves the most stable and accurate predictions. For nuclei in the $| N -$ $Z | > 3 0$ region, the RMSDs between the predictions of ANN7 and the experimental data stay about only $2 0 0 \mathrm { k e V } .$

Single and two-neutron separation energies are observables better suited to showcase the details of theoretical models, particularly, whether the shell closure and pairing effects are properly considered. They could be deduced from the binding energies as follows.

$$
\begin{array}{l} S _ {n} (Z, N) = B E (Z, N) - B E (Z, N - 1), \\ \begin{array}{l} S _ {n} (Z, N) = B E (Z, N) - B E (Z, N - 1), \\ S _ {2 n} (Z, N) = B E (Z, N) - B E (Z, N - 2). \end{array} \tag {5} \\ \end{array}
$$

In Fig. 6 and Fig. 7, we compare the experimental one-neutron separation energies with the predictions of four ANNs for the Ca, Ni, Sn, and Pb isotopic chains. For $S _ { n }$ , ANN2 cannot describe at all the odd-even staggerings, while ANN4 largely improves the situation. However, as is also reflected in Fig. 7, for nuclei close to the shell closures, the deviations are larger. ANN6 and ANN7, on the other hand, can describe all the nuclei including the neutron-rich ones.

The predictions of a good theoretical model should center around its mean value with small spreads. To check how the four ANNs perform in this perspective, we show in Fig. 8, the number

![](images/16b232a42a77aebc8f73015909dcee3400e473c0ced62ec3cc38f42e1cb6f6b5.jpg)  
FIG. 5. $\sigma _ { r m s }$ as functions of $\vert N - Z \vert$ , which reflects the ability of ANNs in describing nuclei with large isospin asymmetries. Note that there is no nucleus in test20 with $5 0 < | N - Z | < 6 0$ .

of nuclei for which the deviations between theory and experiment fall in between certain ranges. We further fit these counts with normal distributions. The mean of the Gaussian fit indicates the accuracy of the predictions, and the variance reflects the range of deviations. From Fig. 8, it could be seen that the Gaussian fits of ANN2 and ANN4 are quite flat, and there are still many deviations that are over 0.7 MeV. In contrast, both ANN6 and ANN7 have very narrow distributions. In addition, most predictions by ANN7 deviate from their experimental counterparts by less than 0.7 MeV. In this sense, ANN7 not only predicts well but also is more certain.

# A. Comparison with some recent works

In the past, most machine learning studies of nuclear binding energies adopt the residual approach, which fits the residuals between experimental data and the predictions of an underlying theoretical model [33, 37, 47–50]. In the past two years, a number of studies fitting directly to

![](images/e93f6709f8ed9cf9b324de2546b03fb2f46d055efb2204cea8b2e1b0094feee9.jpg)

![](images/2a1ab9f0d2e9122f1a8aa7fe0f9a8bf8aa173612afb4a1673fcd28181ac1e17c.jpg)

![](images/c1fdbb71c7ebb59e115af66bf73ffa71f5de4f65364e9670fd53fff1429955e7.jpg)

![](images/73c3a4ca6d9501e348cf669f52cefc5c84a4f3856d2bad57e0ff5a27cebbc12e.jpg)  
FIG. 6. Experimental single neutron separation energies in comparison with the ANN predictions.

binding energies appeared. In the following, we compare our study with two recent works.

In Ref. [54], with the mixture density network (MDN) [60] the authors used 450 nuclei in AME2016 [53] with $Z \ \geq \ 2 0$ as the training set. The first test set contains all the nuclei in AME2016 with $Z \ge 2 0$ , and the second test set is the latest release of AME2020. The RMSDs of the training set and two test sets are 0.186 MeV, 0.316 MeV, and 0.336 MeV, respectively. We note that although the training sets of ANN7 and MDN are both taken from AME2016, the MDN training set contains fewer nuclei. Light nuclei, which are difficult to describe, are not considered by the MDN model. We note that although the present work and Ref. [54] adopt different networks, inputs, and training sets, their performances are rather similar.

The data augmentation technique, i.e., Gaussian Noise augmentation, was found in Ref [52] to improve the predictions of ANNs. The number of nuclei in the training set expands from 1685 to 10110. The improvements in different MLP from the perspective of RMSDs are from $1 8 . 8 6 \%$ t o $3 0 . 5 0 \%$ in the test set that is in the training data region, and from $2 3 . 4 7 \%$ to $3 6 . 3 3 \%$ in the test set

![](images/5120b217a8e0c940df7e0991aab5d56a4d1536ced2766bf199f2d17ec8da3d55.jpg)

![](images/04184f18a3ff61bf94b85601dcfa78b3cba1852592aa2a014b1dcc0b231e77c9.jpg)

![](images/35c37c42de732dc27c0e663c384b8f805768fc25cdd18a3aa6360430f976459d.jpg)

![](images/7c99df39ff43f2c3ed08f5ba10c6e1a62f44666abe5a6a96cce9212f515066df.jpg)  
FIG. 7. Experimental two-neutron separation energies in comparison with the ANN predictions.

that is beyond the training data region. We also tried to apply the data augmentation technique to our model, but found that this technique affects little our results.

# IV. SUMMARY AND OUTLOOK

In this work, we developed a deep neural network with seven physically motivated features: Z , N , $Z _ { E O }$ , $N _ { E O }$ , $\Delta Z$ , ∆N and ASY. We studied the nuclear masses compiled in AME2020 (measured and extrapolated), achieving a description with a root-mean-square deviation around $0 . 2 \mathrm { M e V }$ which is much smaller than the previous work [36] and closer to those of Refs. [54, 55]. The success of our work further demonstrated the importance of considering relevant physical information, i.e., “feature engineering”, when applying machine learning methods to study systems for which only limited data are available.

It is interesting to note that the description of the nuclear binding energies achieved in the present work is similar to those of Refs. [54, 55] but our work differs from those of Refs. [54, 55] in many details: the networks, constraints and input features. In Ref. [55], 12 features are used. While in our approach, we found that only six of them $( Z , N , Z _ { E O } , N _ { E O } , \Delta Z , \Delta N )$ $Z _ { E O }$ $N _ { E O }$ are relevant. On

![](images/7bc0eb231e8a3e324df53198d21b8d7fcf7940de275042b318627512c4adcfd7.jpg)  
FIG. 8. Number of nuclei for which the BE deviations fall below $0 . 7 \mathrm { M e V }$ are divided into seven equally spaced groups. The normal distribution curves fit the number of nuclei for which the $\sigma _ { r m s }$ are lower than 0.7 MeV. We note that $6 3 ( 5 1 . 6 \% )$ of the nuclei in ANN2, 32 $( 2 6 . 2 \% )$ of the nuclei in ANN4, $1 6 ( 1 3 . 1 \% )$ of the nuclei in ANN6 and $7 ( 5 . 7 \% )$ of the nuclei in ANN7 have deviations over 0.7 MeV.

the other hand, Ref. [54] considered the constraint of the GK relation in addition to eight features. Nevertheless, the similar results achieved in these works support the conclusion that machine learning methods are powerful enough to predict nuclear binding energies at a level comparable to or even better than the most refined conventional theoretical models.

This work reveals that for systems with limited data, the consideration of input features containing the most relevant physical information can be key to the success for physical studies using machine learning methods. Turning the argument around, by trial and error, one can also anticipate the discovery of “new physics” by examining the deficiency of ANNs in describing such systems.

# V. ACKNOWLEDGEMENT

We would like to express our gratitude towards Esra Yu¨ksel and M. R. Mumpower for useful communications. This work is supported in part by the National Natural Science Foundation of

[1] V. Zelevinsky, Acta Physica Polonica A 128, 1008 (2015).   
[2] A. de Roubin et al., Phys. Rev. C 96, 014310 (2017), [Erratum: Phys.Rev.C 97, 059902 (2018)].   
[3] Q. Mo, M. Liu, and N. Wang, Phys. Rev. C 90, 024320 (2014), arXiv:1408.4872 [nucl-th].   
[4] M. Rosenbusch et al., Phys. Rev. Lett. 114, 202501 (2015), arXiv:1506.00520 [nucl-ex].   
[5] D. Lunney, J. M. Pearson, and C. Thibault, Rev. Mod. Phys. 75, 1021 (2003).   
[6] W. S. Porter et al., Phys. Rev. C 106, 024312 (2022), arXiv:2206.15329 [nucl-ex].   
[7] T. Tanaka et al., Phys. Rev. Lett. 124, 052502 (2020).   
[8] M. E. Burbidge, G. R. Burbidge, W. A. Fowler, and F. Hoyle, Rev. Mod. Phys. 29, 547 (1957).   
[9] A. Boehnlein et al., Rev. Mod. Phys. 94, 031003 (2022), arXiv:2112.02309 [nucl-th].   
[10] M. R. Mumpower, R. Surman, G. C. McLaughlin, and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016), [Erratum: Prog.Part.Nucl.Phys. 87, 116–116 (2016)], arXiv:1508.07352 [nucl-th].   
[11] H. Schatz and W. J. Ong, Astrophys. J. 844, 139 (2017), arXiv:1610.07596 [astro-ph.HE].   
[12] P. Moller, A. J. Sierk, T. Ichikawa, and H. Sagawa, Atom. Data Nucl. Data Tabl. ¨ 109-110, 1 (2016), arXiv:1508.06294 [nucl-th].   
[13] X. W. Xia et al., Atom. Data Nucl. Data Tabl. 121-122, 1 (2018), arXiv:1704.08906 [nucl-th].   
[14] W. Zhang, Z. Li, W. Gao, and T. Sun, Chinese Physics C 46, 104105 (2022).   
[15] M. Wang, W. J. Huang, F. G. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003 (2021).   
[16] W. Nazarewicz, Nature Physics 14, 537–541 (2018).   
[17] L.-S. Geng, H. Toki, and J. Meng, Prog. Theor. Phys. 113, 785 (2005), arXiv:nucl-th/0503086.   
[18] C. F. V. Weizsacker, Z. Phys. 96, 431 (1935).   
[19] N. Wang, M. Liu, and X. Wu, Phys. Rev. C 81, 044322 (2010), arXiv:1001.1493 [nucl-th].   
[20] N. Wang, Z. Liang, M. Liu, and X. Wu, Phys. Rev. C 82, 044304 (2010), arXiv:1008.2115 [nucl-th].   
[21] M. Liu, N. Wang, Y. Deng, and X. Wu, Phys. Rev. C 84, 014333 (2011), arXiv:1104.0066 [nucl-th].   
[22] N. Wang, M. Liu, X. Wu, and J. Meng, Phys. Lett. B 734, 215 (2014), arXiv:1405.2616 [nucl-th].   
[23] Y. Gambhir, P. Ring, and A. Thimet, Annals of Physics 198, 132 (1990).   
[24] J. Duflo and A. P. Zuker, Phys. Rev. C 52, R23 (1995), arXiv:nucl-th/9505011.   
[25] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 88, 061302 (2013).   
[26] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 88, 024308 (2013).

[27] S. Goriely, S. Hilaire, M. Girod, and S. Peru, Phys. Rev. Lett. 102, 242501 (2009).   
[28] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 93, 034337 (2016).   
[29] P. Moller, J. R. Nix, W. D. Myers, and W. J. Swiatecki, Atom. Data Nucl. Data Tabl. 59, 185 (1995), arXiv:nucl-th/9308022.   
[30] P. Moller, W. D. Myers, H. Sagawa, and S. Yoshida, Phys. Rev. Lett. ¨ 108, 052501 (2012).   
[31] K. Zhang et al. (DRHBc Mass Table), Atom. Data Nucl. Data Tabl. 144, 101488 (2022), arXiv:2201.03216 [nucl-th].   
[32] P. Harris et al., in 2022 Snowmass Summer Study (2022) arXiv:2203.16255 [cs.LG].   
[33] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C 93, 014311 (2016), arXiv:1508.06263 [nucl-th].   
[34] R. Utama and J. Piekarewicz, Phys. Rev. C 96, 044308 (2017), arXiv:1704.06632 [nucl-th].   
[35] R. Utama and J. Piekarewicz, Phys. Rev. C 97, 014306 (2018), arXiv:1709.09502 [nucl-th].   
[36] E. Yuksel, D. Soydaner, and H. Bahtiyar, Int. J. Mod. Phys. E ¨ 30, 2150017 (2021), arXiv:2101.12117 [nucl-th].   
[37] Z. M. Niu and H. Z. Liang, Phys. Lett. B 778, 48 (2018), arXiv:1801.04411 [nucl-th].   
[38] X.-X. Dong, R. An, J.-X. Lu, and L.-S. Geng, Phys. Rev. C 105, 014308 (2022), arXiv:2109.09626 [nucl-th].   
[39] X.-X. Dong, R. An, J.-X. Lu, and L.-S. Geng, (2022), arXiv:2206.13169 [nucl-th].   
[40] D. Wu, C. L. Bai, H. Sagawa, and H. Q. Zhang, Phys. Rev. C 102, 054323 (2020), arXiv:2006.09677 [nucl-th].   
[41] R. Utama, W.-C. Chen, and J. Piekarewicz, J. Phys. G 43, 114002 (2016), arXiv:1608.03020 [nucl-th].   
[42] C.-Q. Li, C.-N. Tong, H.-J. Du, and L.-G. Pang, Phys. Rev. C 105, 064306 (2022), arXiv:2202.11897 [nucl-th].   
[43] Z. M. Niu, H. Z. Liang, B. H. Sun, W. H. Long, and Y. F. Niu, Phys. Rev. C 99, 064307 (2019), arXiv:1810.03156 [nucl-th].   
[44] C.-W. Ma, D. Peng, H.-L. Wei, Y.-T. Wang, and J. Pu, Chin. Phys. C 44, 124107 (2020), arXiv:2007.15416 [nucl-th].   
[45] C.-W. Ma, D. Peng, H.-L. Wei, Z.-M. Niu, Y.-T. Wang, and R. Wada, Chin. Phys. C 44, 014104 (2020).   
[46] Z.-A. wang, J. Pei, Y. Liu, and Y. Qiang, Phys. Rev. Lett. 123, 122501 (2019), arXiv:1906.04485 [nucl-th].

[47] M. Carnini and A. Pastore, J. Phys. G 47, 082001 (2020), arXiv:2002.10290 [nucl-th].   
[48] Z. Gao, Y. Wang, H. Lu, Q. Li, C. Shen, and L. Liu, Nucl. Sci. Tech. ¨ 32, 118 (2021), arXiv:2105.02445 [nucl-th].   
[49] H. F. Zhang, L. H. Wang, J. P. Yin, P. H. Chen, and H. F. Zhang, J. Phys. G 44, 045110 (2017).   
[50] X. H. Wu, Y. Y. Lu, and P. W. Zhao, Physics Letters B 834, 137394 (2022), arXiv:2208.13966 [nuclth].   
[51] Z. M. Niu and H. Z. Liang, “Nuclear mass predictions with machine learning reaching the accuracy required by $\$ 1$ -process studies,” (2022), arXiv:2208.04783 [astro-ph, physics:nucl-ex, physics:nuclth].   
[52] H. Bahtiyar, D. Soydaner, and E. Yuksel, Applied Soft Computing ¨ 128, 109470 (2022), arXiv:2205.07953 [cs.LG].   
[53] M. Wang, G. Audi, F. Kondev, W. Huang, S. Naimi, and X. Xu, Chinese Physics C 41, 481 (2017).   
[54] M. R. Mumpower, T. M. Sprouse, A. E. Lovell, and A. T. Mohan, Phys. Rev. C 106, L021301 (2022).   
[55] A. E. Lovell, A. T. Mohan, T. M. Sprouse, and M. R. Mumpower, Phys. Rev. C 106, 014305 (2022), arXiv:2201.00676 [nucl-th].   
[56] D. Hendrycks and K. Gimpel, arXiv preprint arXiv:1606.08415 (2016).   
[57] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, ¨ M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala, “Pytorch: An imperative style, high-performance deep learning library,” in Proceedings of the 33rd International Conference on Neural Information Processing Systems (Curran Associates Inc., Red Hook, NY, USA, 2019) p. 8024–8035.   
[58] D. P. Kingma and J. Ba, arXiv preprint arXiv:1412.6980 (2014).   
[59] N. Wang, “Nuclear mass table with ws4 model,” (2014).   
[60] C. M. Bishop, “Mixture density networks,” (1994).