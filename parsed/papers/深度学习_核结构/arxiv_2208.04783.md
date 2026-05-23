# Nuclear mass predictions with machine learning reaching the accuracy required by $r$ -process studies

Z. M. Niu1∗ and H. Z. Liang $^ { 2 , 3 }$ †

$^ { 1 }$ School of Physics and Optoelectronic Engineering,

Anhui University, Hefei 230601, China

$^ 2$ Department of Physics, Graduate School of Science,

The University of Tokyo, Tokyo 113-0033, Japan and

$^ 3$ RIKEN Nishina Center, Wako 351-0198, Japan

(Dated: August 10, 2022)

# Abstract

Nuclear masses are predicted with the Bayesian neural networks by learning the mass surface of even-even nuclei and the correlation energies to their neighbouring nuclei. By keeping the known physics in various sophisticated mass models and performing the delicate design of neural networks, the proposed Bayesian machine learning (BML) mass model achieves an accuracy of 84 keV, which crosses the accuracy threshold of the 100 keV in the experimentally known region. It is also demonstrated the corresponding uncertainties of mass predictions are properly evaluated, while the uncertainties increase by about 50 keV each step along the isotopic chains towards the unknown region. The shell structures in the known region are well described and several important features in the unknown region are predicted, such as the new magic numbers around $N = 4 0$ , the robustness of $N = 8 2$ shell, the quenching of $N = 1 2 6$ shell, and the smooth separation energies around $N = 1 0 4$ .

Introduction—The origin of heavy elements in the Universe is an important but unanswered fundamental question of science [1]. The rapid neutron-capture process ( $r$ - process) is responsible for producing about half of the elements heavier than iron [2]. During the past decades, the $r$ -process studies have made substantial progress from both nuclear physics and astrophysics sides [3, 4]. However, the $r$ -process astrophysical sources and their specific conditions remain mysteries, and the identification of the most important $r$ -process site also remains a hot topic [5–7].

The $r$ -process studies necessitate the joint efforts of nuclear physicists and astrophysicists [8]. From the nuclear side, nuclear mass is a crucial input [9], which determines the $r$ -process path, and hence relates the main $r$ -process abundance peaks at $A = 1 3 0$ and 195 to the nuclear shell closures at $N = 8 2$ and 126, respectively. Nuclear mass also determines the reaction energies of $\beta$ decay and neutron capture in the $r$ process, so it is one important source of theoretical uncertainties of $\beta$ -decay half-lives and neutron-capture rates [10, 11]. Although the measurements of nuclear mass have been made great progress in recent years, especially for the nuclei on the $r$ -process path around $N = 8 2$ [12], the $r$ -process path near $N = 1 2 6$ or above is still unreachable for the present, or even the next-generation, radioactive ion beam facilities. Therefore, accurate nuclear mass predictions are essential to understand the mysteries in the $r$ process.

Due to the difficulties in the quantum many-body problem and the complexity of nuclear force, accurate nuclear mass prediction is a very challenging theoretical task. Even in the experimentally known region, the accuracies of nuclear mass predictions are generally around 500 keV [13], which is much poorer than the accuracy of 100 keV required by the $r$ -process studies [14]. The greater difficulty lies in the extrapolation. It is found that the deviations of different mass models can even reach tens of MeV when they are extrapolated to the unknown neutron-drip line. Therefore, the accurate nuclear mass prediction has become one of the bottlenecks in the $r$ -process studies.

In particular, one of the hot topics in the $r$ -process studies during past decades is the origin of the rare-earth peak, which has been claimed to be associated with the $N \approx 1 0 4$ kink in the separation energies [15] or the doubly asymmetric fission fragment distributions in the $A \approx 2 7 8$ region [16]. If one can construct accurate enough mass predictions for the $r$ -path nuclei leading to the rare-earth peak, one can confirm whether there is a kink in the separation energies near $N = 1 0 4$ , which will become an essential step for understanding

the origin of the rare-earth peak.

For the above key open questions, we recall that the famous Bethe-Weizs¨acker (BW) formula is the first nuclear mass model, in which the nucleus is assumed as a charged liquid drop [17, 18]. It achieves an accuracy of about 3 MeV, while large deviations from the experimental data are found in the nuclei near the magic numbers. These large deviations can be reduced by including the microscopic correction energies, and the nuclear mass predictions with the accuracy of about 300–500 keV can be obtained. This kind of mass model is usually named as “macroscopic-microscopic” model, such as finite-range droplet model (FRDM) [19] and Weizs¨acker-Skyrme (WS) model [20]. However, the microscopic correction energies are generally extracted from the single-particle levels of phenomenological mean fields, which are generally independent of the macroscopic part. Such an inconsistency between the macroscopic and microscopic parts would affect the model reliability. The microscopic mass models based on the nuclear density functional theory are usually believed to have better extrapolation abilities, e.g., the relativistic mean-field model [21, 22] and the nonrelativistic Hartree-Fock-Bogliubov (HFB) model with Skyrme [23] or Gogny [24] force. Their present accuracies are, however, generally lower than the macroscopic-microscopic models.

To further improve the accuracy of nuclear models, the machine learning techniques have attracted much attention during the past years. In particular, the Bayesian version of machine learning is expected to be able to provide the corresponding theoretical uncertainties [25]. For the nuclear mass predictions with Bayesian neuron network (BNN), we pointed out that the performance of BNN can be improved by enriching the network inputs with information of physics [26], such as the pairing and shell effects. Neufcourt et al. [27] agreed with this idea in their study of two-neutron separation energies. Since then, nuclear structure with machine learning techniques has become a hot frontier, for example, in the studies of neutron-drip line in the Ca region [28], the incomplete fission yields [29], and the low-lying excitation spectra [30]. From the above studies, see also a recent review [31] and the references therein, one can conclude that the accuracy and the capability of extrapolation of study with machine learning techniques crucially depend on the delicate designs of neuron network, by taking into account as much physics as possible.

In this Letter, we propose a nuclear mass model with Bayesian machine learning and pay special attention on the designs of the structure, outputs, and inputs of the neuron

networks. We will first demonstrate the accuracy of mass prediction as well as the capability of extrapolation of the present model with a theory-to-theory validation. We will then show the present BML mass model achieves an accuracy of 84 keV with respect to the experimental data in AME2016 [32] and also discuss the shell structures in the experimentally known and unknown regions, which are crucial for the $r$ -process studies.

Designs of BNN —In the present study, we adopt the general scheme of BNN [33]. BNN can avoid the over-fitting problem automatically by using the hyper priors. It can also quantify the uncertainties in predictions, since all model parameters are described with probability distributions.

For the present designs of the network structure, we keep in mind that the physics (e.g., the ground-state spin and parity) of odd- $A$ and odd-odd nuclei are much more sophisticated than that of even-even nuclei. Thus, the predictive power, especially the extrapolation capability, will be substantially affected if we directly train the neural network with the whole nuclear mass surface. A much more effective strategy is the training of neural network with the smoother mass surface of even-even nuclei, together with the trainings with the separation energies related to their neighbouring odd- $A$ and odd-odd nuclei. As a result, there are in total 9 different BNNs to cover the mass predictions for the whole nuclear chart. See Fig. 1 in Supplemental Materials [34] and the corresponding descriptions.

For the designs of the network outputs, in our previous study [35], we showed quantitatively that the performance of machine learning is very limited if crucial information of physics is missing. The discrepancy between the experimental data and the predictions of a given model $\delta M = M ^ { \mathrm { e x p } } - M ^ { \mathrm { m o d e l } }$ is usually taken as the output, i.e., the learning target [25, 26], which can effectively inlcude the known physics in the given model. To make the best use of the established nuclear mass models, we employ the macroscopic model BW2 [36], the macroscopic-microscopic models KTUY [37], FRDM12 [19], and WS4 [20], the microscopic models RMF [21] and HFB-31 [38], and other high-precision global mass models Bhagwat [39] and DZ28 [40]. These mass models have taken into account the physics important to the description of nuclear mass from different aspects.

For the designs of the network inputs, in addition to $Z$ and $N$ , we further introduce ${ \cal E } _ { \mathrm { m i c } } ^ { \mathrm { m o d e l } } \equiv { \cal M } ^ { \mathrm { m o d e l } } - { \cal E } _ { \mathrm { m a c } }$ or the counterparts of the separation energies as an input. This quantity is completely missing in the macroscopic mass models, while it is related to the effective mass of nucleon in the microscopic mass models. It can be seen that the prefect

mass model that reproduces all the experimental data holds a prefect correlation between the input and output, $E _ { \mathrm { m i c } } ^ { \mathrm { m o d e l } } = E _ { \mathrm { m i c } }$ , independent of $Z$ and $N$ . In such a way, the systematic overestimation or underestimation on $E _ { \mathrm { m i c } } ^ { \mathrm { m o d e l } }$ of a given model can be corrected by BNN in an efficient way. In principle, $E _ { \mathrm { m a c } } ^ { ' }$ can be taken as any smooth function of $Z$ and $N$ on the nuclear mass surface. Here, it is taken from the macroscopic part of FRDM12.

Based on each mass model $i$ , we can get its corresponding BNN mass prediction $M _ { i }$ with the error $\sigma _ { i }$ . To describe the systematic error of mass prediction, the weighted mean $M$ and standard deviation $\sigma _ { M }$ of $M _ { i }$ are taken as the final mass prediction, which are

$$
M = \frac {\sum_ {i = 1} ^ {m} \omega_ {i} M _ {i}}{\sum_ {i = 1} ^ {m} \omega_ {i}}, \quad \sigma_ {M} = \frac {1}{\sqrt {\sum_ {i = 1} ^ {m} \omega_ {i}}} \tag {1}
$$

where $\omega _ { i } = 1 / \sigma _ { i } ^ { 2 }$ and $m$ is the number of mass models. Since some sources of error may not be taken into account, the error $\sigma _ { M }$ is further corrected with a factor $\chi _ { \nu }$ , which considers the deviations between mass predictions $M$ and experimental data

$$
\chi_ {\nu} ^ {2} = \frac {1}{n} \sum_ {Z, N \geqslant 8} \frac {1}{\sigma_ {M (Z , N)} ^ {2}} \left[ M (Z, N) - M _ {\exp} (Z, N) \right] ^ {2}, \tag {2}
$$

where $n$ is the number of nuclei in the learning set. Here $\chi _ { \nu } = 2 . 1$ for the experimental data in AME2016. For simplicity, this Bayesian machine learning model described above will be denoted by BML hereafter.

Before ending this part, we perform a theory-to-theory validation with the above designs of BNN, to demonstrate the accuracy of prediction and the capability of extrapolation. In such a benchmark calculation, the nuclear masses of FRDM12 are used as the pseudo experimental data (i.e., the target values). Meanwhile, the other 7 mass models—BW2, KTUY, WS4, RMF, HFB-31, Bhagwat, and DZ28—are regarded as our present knowledge and used as the inputs of BNN. To simulate the present experimentally known region, the learning set is limited to those nuclei listed in AME2016, and all nuclei outside AME2016 will be used to testify the extrapolation capability. As a result, the mass prediction accuracy in the learning region reaches 93 keV. It is also found that the mass prediction uncertainties increase by about 50 keV each step along the isotopic chains towards the unknown region, which agrees with the standard deviations between the mass predictions and the corresponding FRDM12 values. For details, see Fig. 2 in Supplemental Materials [34] and the corresponding discussion.

![](images/cfddc3715f305466229fd1aa735a4f410dc48e80ed34e111eb23187895facdb4.jpg)  
FIG. 1: (Color online) The rms deviations of $M$ , $S _ { n }$ , $S _ { 2 n }$ , $S _ { p }$ , $S _ { 2 p }$ , $S _ { D }$ , and $Q _ { \beta }$ with respect to the experimental data for the learning set of the BML mass model. The corresponding rms deviations given by the BW2, FRDM12, HFB-31, and DZ28 mass models are shown for comparison.

Results and Discussion—Using the high-precision experimental data in AME2016 as the learning set, we construct the mass predictions of the present BML model. The root-meansquare (rms) deviations of $M$ and various separation or decay energies with respect to the experimental data for the learning set are given in Fig. 1. For comparison, the corresponding rms deviations given by some other mass models are also given. It is clear that the BML model achieves a very high accuracy of mass prediction, which is of the best accuracy for global mass predictions as we have known and for the first time crosses the accuracy threshold of 100 keV in the known region. Furthermore, the BML model also achieves high accuracies for various separation or decay energies, which are at least about 3 times higher than other shown mass models. Even comparing with the previous machine learning model WS4+BNN-I4 [26], whose corresponding rms values are 184, 208, 216, 213, 227, and 255 keV for mass, $S _ { n }$ , $S _ { p }$ , $S _ { 2 n }$ , $S _ { 2 p }$ , and $Q _ { \beta }$ , respectively, the present BML model achieves much smaller rms values, i.e., 84, 78, 83, 105, 111, and 99 keV, respectively. This indicates the BML model describes excellently not only the mass surface globally but also its local details, including its derivatives in different directions on the nuclear chart.

The microscopic correction energies $E _ { \mathrm { m i c } } ^ { ' }$ can reveal the shell effects in nuclear properties. Therefore, we show $E _ { \mathrm { m i c } } ^ { \mathrm { B M L } } = E ^ { \mathrm { B M L } } { - } E _ { \mathrm { m a c } }$ of BML in Fig. 2. It is clear that the shell structures in the known region are well reproduced. Being extrapolated to the unknown region, even to the drip lines, there are several remarkable structure features, which are hardly achieved

![](images/1c124f610531e31d92f00497de7f56df90c9a4a54468456c24453fb1501abdd5.jpg)  
FIG. 2: (Color online) Microscopic correction energies $E _ { \mathrm { m i c } }$ of BML. The contours show the boundary of nuclei with known masses in AME2016 and the dotted lines denote the traditional magic numbers.

by other learning approaches, such as the radial basis function approach [41–43]. Apart from the traditional magic numbers, the new magic numbers around $N = 4 0$ in the light nuclei region and those around $Z = 1 2 0$ in the superheavy nuclei region are also predicted by BML.

It is well known that $N = 8 2$ and $N = 1 2 6$ shells are crucial for the $r$ -process properties, e.g., they are responsible for the main peaks of solar $r$ -abundance at $A = 1 3 0$ and $A = 1 9 5$ , respectively. From Fig. 2, it is found that the $N = 8 2$ shell remains robust even going to the neutron-drip line, which has been approved by recent experimental studies [44]. However, we predict that the $N = 1 2 6$ shell will first quench and then enhance as approaching the proton magic number $Z = 5 0$ when going to the neutron-drip line. The $N = 1 2 6$ shell also quenches when going to the proton-drip line, even just away from the known region.

The two-proton (neutron) gaps $\delta _ { 2 p }$ ( $\delta _ { 2 n }$ ) are also important signatures of nuclear magic numbers, which take local maxima at proton (neutron) magic numbers. From Fig. 3, which shows $\delta _ { 2 p }$ and $\delta _ { 2 n }$ of BML, the traditional magic numbers are well exhibited. The BML model predicts a neutron magic number at $N = 1 8 4$ , although its $\delta _ { 2 n }$ is not as strong as those of traditional magic numbers. It should be pointed out that the larger $\delta _ { 2 n }$ at $N \approx 2 0 0$ is not necessarily a signature of magic number, which mainly originates from the lack of mass predictions for nuclei with $N > 2 0 0$ in the KTUY model.

To show the details of the present BML mass model and illustrate explicitly its extrapolation capability, the mass differences between $M _ { \mathrm { t h } }$ from various mass models and $M _ { \mathrm { e x p } }$ in AME2016 are shown in Fig. 4, by taking the Cr and Nd isotopes as examples. In

![](images/583d32444a402cc20a236e61ceb66bf818473f2d55cb00386ccaf5f2fd6251e6.jpg)  
FIG. 3: (Color online) Same as Fig. 2 but for (a) the two-proton gaps $\delta _ { 2 p }$ and (b) the two-neutron gaps $\delta _ { 2 n }$ .

![](images/6d6d652dbc62c07dc74bead35faabd1277e9d70ed73a93ce02fb558fda34387c.jpg)  
FIG. 4: (Color online) Mass differences between $M _ { \mathrm { t h } }$ from the BML, NewBML, HFB-31, FRDM12, and WS4+BNN-I4 mass models and $M _ { \mathrm { e x p } }$ in AME2016 for the Cr and Nd isotopes. The shaded (white) regions indicate the BML learning (extrapolation) areas, where the accuracy of $M _ { \mathrm { e x p } }$ in AME2016 is higher (worse) than 100 keV. The new experimental data [45, 46] after AME2016 are shown with blue solid symbols.

particular, in these two isotopic chains, there are several experimental data on both neutronrich and proton-rich sides with the accuracy worse than 100 keV, shown as the white regions in Fig. 4. Therefore, we did not include those data in the learning set.

It is clear that in the BML learning areas, the shaded regions in Fig. 4, the BML mass predictions are in an excellent agreement with the experimental data with an accuracy around 100 keV, apart from the region around $^ \mathrm { 1 5 4 }$ Nd. It is also seen that in the extrapolation areas, both neutron-rich and proton-rich sides, the BML mass predictions agree with the experimental data within the experimental and theoretical uncertainties. Remarkably, we still hold such a nice agreement, when we extrapolate the mass predictions from $^ { 5 8 }$ Cr to $^ \mathrm { 7 0 } \mathrm { C r }$ with 12 neutrons more. In both learning and extrapolation areas, the performance of BML is much better than those of HFB-31 and FRDM12, even better than the previous machine learning results of WS4+BNN-I4.

In the regions of Cr and Nd, there are a number of new experimental data [45, 46] after AME2016, which are shown with blue solid symbols in Fig. 4. The comparison between the new data and the BML mass predictions again show excellent agreements not only on the values of the mass but also on the systematics of the mass surface. For example, the BML mass prediction on $^ \mathrm { 1 5 4 }$ Nd is consistent with the new data, instead of that in AME2016.

As a step further, to show the influence of new experimental data, the new BML mass predictions are made by including these new data after AME2016 [45–72] into the learning set, which are denoted by NewBML for simplicity. The corresponding results are also shown in Fig. 4 with dark-green shaded bands. It is found that, if the new data are included in the learning set, the theoretical uncertainties near the new data reduce to about half of the original values.

For the important issue related to the origin of the rare-earth peak and the possible kinks in the separation energies near $N = 1 0 4$ , we show in Fig. 5 the two-neutron separation energies $S _ { 2 n }$ for the $Z = 6 0$ –65 isotopes. While the BML mass predictions agree well with both AME2016 and new data in this region, the new data can further substantially reduce the theoretical uncertainties of $S _ { 2 n }$ for the neighboring nuclei. As a result, the $S _ { 2 n }$ predictions around $N = 1 0 4$ by NewBML tend to be smooth, rather than with kinks. In other words, it is more likely that the origin of the rare-earth peak is due to the doubly asymmetric fission fragment distributions in the $A \approx 2 7 8$ region [16]. More experimental data in the coming years will further testify this conclusion. By taking the new nuclei with $Z , N \geqslant 8$ first

![](images/9321ec91a463b8cdf59ed79b7f5a442676f4a8d5cf71a3ec91eb8999fc546b1e.jpg)  
FIG. 5: (Color online) Two-neutron separation energies $S _ { 2 n }$ of $Z \ = \ 6 0 – 6 5$ isotopes. The $S _ { 2 n }$ calculated with the experimental data in AME2016 are shown with yellow circles, while the new $S _ { 2 n }$ calculated by including the new experimental data [45–72] are shown with blue circles. The $S _ { 2 n }$ predictions of BML and NewBML are shown with open circles and open squares, respectively. For displaying the data clearly, all $S _ { 2 n }$ of $Z = 6 1 – 6 5$ isotopes are increased by $( Z - 6 0 )$ MeV.

appearing in latest database AME2020 [12] as the testing set, the rms deviation of BML model with respect to those new data with the experimental uncertainties smaller than 100 keV is 170 keV. This indicates a good accuracy is also achieved by the BML model for these new data, which are not in the training. In contrast, the corresponding rms deviations are 245, 691, and 718 keV for WS4+BNN-I4 [26], FRDM2012 [19], and HFB-31 [38] models, respectively.

Finally, all experimental masses with $Z , N \geqslant 8$ and uncertainties smaller than 100 keV in the latest database AME2020 [12] are employed to train the BML model, the resulting mass predictions are given in the Supplemental Materials [34].

Summary—High-precision mass predictions are made with the Bayesian neural networks by learning the mass surface of even-even nuclei and the correlation energies to their neighbouring nuclei. The known physics in various mass models are kept to achieve good predictive capability. With this strategy, the proposed BML mass model describes well not only the mass surface globally but also its local details including its derivatives in different directions on the nuclear chart. As a result, BML achieves high accuracy for both nuclear masses and various separation or decay energies. The accuracy of BML mass predictions

reaches 84 keV, which has crossed the accuracy threshold of 100 keV in the known region. The uncertainties of BML mass predictions are also reasonably evaluated, which increase about 50 keV as going forward one step along the isotopic chain from the known region, and the new experimental data after AME2016 can be precisely predicted by BML within the experimental and theoretical uncertainties.

While the shell structures in the known region are well described, we also predict several important features in the unknown region, such as the new magic numbers around $N = 4 0$ , the robustness of $N = 8 2$ shell, the quenching of $N = 1 2 6$ shell, and the smooth separation energies around $N = 1 0 4$ , which are all crucial for the quantitative $r$ -process calculations.

With the present designs of the BML mass model, the future experimental data of nuclear mass as well as the future advanced nuclear mass models can be taken into account by the same strategy. The nuclear mass predictions towards the unknown region can be carried out and improved systematically and continuously.

# Acknowledgements

We are grateful to Professor Shan-Gui Zhou and Professor Yi-Fei Niu for the fruitful discussions. This work was partly supported by the National Natural Science Foundation of China under Grant No. 11875070 and No. 11935001, the Anhui project (Z010118169), the JSPS Grant-in-Aid for Early-Career Scientists under Grant No. 18K13549, the JSPS Grant-in-Aid for Scientific Research (S) under Grant No. 20H05648, the RIKEN iTHEMS program, and the RIKEN Pioneering Project: Evolution of Matter in the Universe. The authors acknowledge the High-performance Computing Platform of Anhui University for providing computing resources.

∗ Electronic address: zmniu@ahu.edu.cn   
† Electronic address: haozhao.liang@phys.s.u-tokyo.ac.jp

[1] E. Haseltin, Discover 23(2), 37 (2002).   
[2] E. M. Burbidge, G. R. Burbidge, W. A. Fowler, and F. Hoyle, Rev. Mod. Phys. 29, 547 (1957).   
[3] M. Arnould, S. Goriely, and K. Takahashi, Phys. Rep. 450, 97 (2007).

[4] J. J. Cowan, C. Sneden, J. E. Lawler, A. Aprahamian, M. Wiescher, K. Langanke, G. Mart´ınez-Pinedo, and F. K. Thielemann, Rev. Mod. Phys. 93, 015002 (2021).   
[5] S. J. Smartt et al., Nature 551, 75 (2017).   
[6] D. Watson et al., Nature 574, 497 (2019).   
[7] D. M. Siegel, J. Barnes, and B. D. Metzger, Nature 569, 241 (2019).   
[8] T. Kajino, W. Aoki, A. B. Balantekin, R. Diehl, M. A. Famiano, and G. J. Mathews, Pro. Part. Nucl. Phys. 107, 109 (2019).   
[9] D. Martin, A. Arcones, W. Nazarewicz, E. Olsen, Phys. Rev. Lett. 116, 121101 (2016).   
[10] Z. Li, Z. M. Niu, B. H. Sun, Sci. China Phys. Mech. Astron. 62, 982011 (2019).   
[11] C. Ma, Z. Li, Z. M. Niu, and H. Z. Liang, Phys. Rev. C 100, 024330 (2019).   
[12] M. Wang, W. J. Huang, F. G. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003 (2021).   
[13] D. Lunney, J. M. Pearson, and C. Thibault, Rev. Mod. Phys. 75, 1021 (2003).   
[14] M. R. Mumpower, R. Surman, G. C. McLaughlin, A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016).   
[15] R. Surman, J. Engel, J. R. Bennett, and B. S. Meyer, Phys. Rev. Lett. 79, 1809 (1997).   
[16] S. Goriely, J. L. Sida, J. F. Lemaˆıtre, S. Panebianco, N. Dubray, S. Hilaire, A. Bauswein, and H. T. Janka, Phys. Rev. Lett. 111, 242502 (2013).   
[17] C. F. von Weizs¨acker, Z. Phys. 96, 431 (1935).   
[18] H. A. Bethe, R.F. Bacher, Rev. Mod. Phys. 8, 82 (1936).   
[19] P. M¨oller, W. D. Myers, H. Sagawa, and S. Yoshida, Phys. Rev. Lett. 108, 052501 (2012).   
[20] N. Wang, M. Liu, X. Z. Wu, and J. Meng, Phys. Lett. B 734, 215 (2014).   
[21] L. S. Geng, H. Toki, and J. Meng, Prog. Theor. Phys. 113, 785 (2005).   
[22] X. W. Xia, Y. Lim, P. W. Zhao, H. Z. Liang, X. Y. Qu, Y. Chen, H. Liu, L. F. Zhang, S. Q. Zhang, Y. Kim, and J. Meng, At. Data Nucl. Data Tables 121–122, 1 (2018).   
[23] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. Lett. 102, 152503 (2009).   
[24] S. Goriely, S. Hilaire, M. Girod, and S. P´eru, Phys. Rev. Lett. 102, 242501 (2009).   
[25] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C 93, 014311 (2016).   
[26] Z. M. Niu and H. Z. Liang, Phys. Lett. B 778, 48 (2018).   
[27] L. Neufcourt, Y. C. Cao, W. Nazarewicz, and F. Viens, Phys. Rev. C 98, 034318 (2018).   
[28] L. Neufcourt, Y. C. Cao, W. Nazarewicz, E. Olsen, and F. Viensl, Phys. Rev. Lett. 122,

062502 (2019).   
[29] Z. A. Wang, J. C. Pei, Y. Liu, and Y. Qiang, Phys. Rev. Lett. 123, 122501 (2019).   
[30] R. D. Lasser, D. Regnier, J. P. Ebran, and A. Penon, Phys. Rev. Lett. 124, 162502 (2020).   
[31] P. Bedaque et al., Eur. Phys. J. A 57, 100 (2021).   
[32] M. Wang, G. Audi, F. G. Kondev, W. J. Huang, S. Naimi, and X. Xu, Chin. Phys. C 41, 030003 (2017).   
[33] R. Neal, Bayesian Learning of Neural Network (Springer, New York, 1996).   
[34] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevC.106.L021303 for neuron-network designs, theory-to-theory validation, and the nuclear mass predictions of BML model.   
[35] Z. M. Niu, H. Z. Liang, B. H. Sun, Y. F. Niu, J. Y. Guo, and J. Meng, Sci. Bull. 63, 759 (2018).   
[36] M. W. Kirson, Nucl. Phys. A 798, 29 (2008).   
[37] H. Koura, T. Tachibana, M. Uno, and M. Yamada, Prog. Theor. Phys. 113, 305 (2005).   
[38] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 93, 034337 (2016).   
[39] A. Bhagwat, Phys. Rev. C 90, 064306 (2014).   
[40] J. Duflo, and A. P. Zuker, Phys. Rev. C 52, R23 (1995).   
[41] Z. M. Niu, Z. L. Zhu, Y. F. Niu, B. H. Sun, T. H. Heng, and J. Y. Guo, Phys. Rev. C 88, 024325 (2013).   
[42] Z. M. Niu, B. H. Sun, H. Z. Liang, Y. F. Niu, and J. Y. Guo, Phys. Rev. C 94, 054315 (2016).   
[43] Z. M. Niu, J. Y. Fang, and Y. F. Niu, Phys. Rev. C 100, 054311 (2019).   
[44] H. Watanabe et al., Phys. Rev. Lett. 111, 152501 (2013).   
[45] M. Mougeot et al., Phys. Rev. Lett. 120, 232501 (2018).   
[46] R. Orford et al., Phys. Rev. Lett. 120, 262702 (2018).   
[47] M. Vilen et al., Phys. Rev. Lett. 120, 262701 (2018).   
[48] M. Vilen et al., Phys. Rev. C 100, 054333 (2019).   
[49] M. Vilen et al., Phys. Rev. C 101, 034312 (2020).   
[50] L. Canete et al., Phys. Rev. C 101, 041304(R) (2020).   
[51] A. Welker et al., Phys. Rev. Lett. 119, 192502 (2017).   
[52] V. Manea et al., Phys. Rev. Lett. 124, 092502 (2020).   
[53] E. Leistenschneider et al., Phys. Rev. Lett. 120, 062503 (2018).

[54] M. P. Reiter et al., Phys. Rev. C 101, 025803 (2020).   
[55] Y. Ito et al., Phys. Rev. Lett. 120, 152501 (2018).   
[56] S. Michimasa et al., Phys. Rev. Lett. 121, 022506 (2018).   
[57] C. Izzo et al., Phys. Rev. C 97, 014309 (2018).   
[58] W. J. Ong et al., Phys. Rev. C 98, 065803 (2018).   
[59] A. A. Valverde et al., Phys. Rev. Lett. 120, 032701 (2018).   
[60] D. Puentes et al., Phys. Rev. C 101, 064309 (2020).   
[61] N. A. Althubiti et al., Phys. Rev. C 96, 044325 (2017).   
[62] P. Ascher et al., Phys. Rev. C 100, 014304 (2019).   
[63] D. A. Nesterenko et al., J. Phys. G: Nucl. Part. Phys. 44, 065103 (2017).   
[64] M. Brodeur et al., Phys. Rev. C 96, 034316 (2017).   
[65] M. P. Reiter et al., Phys. Rev. C 98, 024310 (2018).   
[66] C. Babcock et al., Phys. Rev. C 97, 024312 (2018).   
[67] D. J. Hartley et al., Phys. Rev. Lett. 120, 182502 (2018).   
[68] Y. H. Zhang et al., Phys. Rev. C 98, 014319 (2018).   
[69] X. Xu et al., Phys. Rev. C 100, 051303(R) (2019).   
[70] X. Xu et al., Phys. Rev. C 99, 064303 (2019).   
[71] S. A. S. Andr´es et al., Eur. Phys. J. A 56, 143 (2020).   
[72] M. Mougeot et al., Phys. Rev. C 102, 014301 (2020).