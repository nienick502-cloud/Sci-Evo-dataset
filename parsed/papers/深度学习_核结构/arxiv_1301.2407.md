# Systematics on ground-state energies of nuclei within the neural networks

Tuncay Bayram, Serkan Akkoyun and S. Okan Kara

Department of Physics, Sinop University, 57000 Sinop, Turkey Department of Physics, Cumhuriyet University, 58140 Sivas, Turkey Department of Physics, Nigde University, Nigde, Turkey

Abstract. One of the fundamental ground-state properties of nuclei is binding energy. In this study, we have employed artificial neural networks (ANNs) to obtain binding energies based on the data calculated from Hartree-Fock-Bogolibov (HFB) method with the two SLy4 and SKP Skyrme forces. Also, ANNs have been employed to obtain two-neutron and two-proton separation energies of nuclei. Statistical modeling of nuclear data using ANNs has been seen as to be successful in this study. Such a statistical model can be possible tool for searching in systematics of nuclei beyond existing experimental nuclear data.

Keywords: Ground-state energies, artificial neural network, Hartree-Fock-Bogoliubov Method

# 1 Introduction

The latest advances in computational physics and experimental techniques have mock up renewed interest in nuclear structure theory. The development of the universal nuclear energy density functional still remains one of the major challenges for nuclear theory. While HFB methods have already achieved a level of sophistication and precision which allows analyses of experimental data for a wide range of properties and for arbitrarily heavy nuclei [1]. Much work remains to be done. There are many open questions when one moves towards the neutron and proton drip lines and superheavy region, while behaviour of the region near valley of stability is well understood. Developing a universal nuclear density functional will require a better understanding of the density dependence, isospin effects, and pairing, as well as an improved treatment of symmetry-breaking effects and many-body correlations.

For investigation of ground-state properties of nuclei in nuclidic chart, there are three most prominent methods the Skyrme energy functional, the Gogny model and relativistic mean field (RMF) model [2,3]. They have been formulated in terms of effective density-dependent nucleon-nucleon interactions. The Skyrme forces as an effective interaction are usually used within the fully microscopic self-consistent mean field theories, because the analytical simplicity of these forces provide easy determination of the parameters from same basic

properties of nuclei (e.g., the saturation of infinite nuclear matter and binding energies of some nuclei). However, their accuracy on the predictions for properties of nuclei is related with the parameters. There is a number of Skyrme forces in literature (details can be found in Ref. [4] and references therein). Three Skyrme forces SKM $^ *$ , SKP and SLy4 are widely used in calculations of the ground-state properties of nuclei within the (HFB) method. In recent decade, results of largescale ground-state calculations ( ${ \sim } 1 5 0 0$ nuclei) have been presented within the framework of HFB method by using the SKP and SLy4 parameters [5]. In the study of Ref.[5], the authors used the code HFBTHO [1]. In the code HFB equations can be solved by using the either axially deformed harmonic oscillator and transformed harmonic oscillator basis.

The correct predictions of properties of nuclei play an essential role for further mapping of nuclei in nuclidic chart. In Ref. [5], the authors have calculated ground-states of nuclei such as binding energies, nuclear radii and quadrupole moments. The binding energies of nuclei is one of the most fundamental properties as well as nuclear size. The correct prediction of the binding energy is important, because obtaining theoretical predictions of two-nucleon separation energies and alpha-decay properties of nuclei can be obtained from the calculated binding energies.

In recent years, ANNs have been used in many fields in nuclear physics as in the scientific areas, such as developing nuclear mass systematics [6], identification of impact parameter in heavy-ion collisions [7,8,9], estimating beta decay half-lives [10], investigating two photon exchange effect [11] and obtaining nuclear charge radii [12]. In the present work, we used feed-forward artificial neural networks (ANNs) in order to obtain binding and two-nucleon separation energies of Sr, Xe, Er and Pb isotopes. The fundamental task of the ANNs which have time advantage is to give outputs through computation on the inputs. The method does not need any relationship between input and output data. The main purpose of the present study is showing of the ANNs successes in describing of the unknown ground-state energies of nuclei by using known data. As can be seen in this study, by using known data as an input, ANN method can reproduce binding energies, two-neutron, two-proton separation energies of unknown nuclei as consistent with theoretical results.

The letter is organized as follows. In Section 2, the theoretical framework for HFB and ANNs are given briefly. The results of this study and discussions are presented in Section 3. Finally, conclusions are given in Section 4.

# 2 Artificial Neural Networks (ANNs)

Artificial neural networks (ANNs) [13] are mathematical models that mimic the brain functionality. They are composed of several processing units which are called neurons and they are connected each other via adaptive synaptic weights. By this synaptic connections, the neurons in the different layers communicate each other and the data is transmitted. In our calculation, we have used feedforward ANN with four layers for estimating binding energies and two nucleon

separation energies. The first layer called input layer consist of two neurons (corresponding to N and Z number of the isotopes), the two intermediate layers named hidden layers are composed of 16 neurons in each and the last one is output layer with one neuron corresponding to the binding energy, neutron or proton separation energies. The used architecture of the ANN was 2-16-16-1 (Fig. 1) and the total numbers of adjustable weights were 304. No bias was used. The input neurons collect data from the outside and the output neurons give the results. The hidden neuron activation function was tangent hyperbolic $( t a n h = ( e ^ { x } - e ^ { - x } ) / ( e ^ { x } + e ^ { - x } ) )$ which is sigmoidlike function. For details we refer the reader to Ref. [13].

![](images/9c071a17ef7101245bbb8886ef7f0abcda79f97a49c15eb65600062ec9cec7ed.jpg)  
Fig. 1. 2-16-16-1 ANN architecture that was used in this work.

The ANN method would be a perfect tool to determine the binding and two nucleon separation energies. One has to train network by known isotopes data and then to feed the trained network with unknown isotopes data in order to obtain neural network outputs for binding and separation energies. In the learning stage of this work, a back-propagation algorithm with Levenberg-Marquardt [14,15] were used for the change of the connections between neurons in order to obtain aggrement between neural network output and known output. The purpose of this training stage is to minimize the difference between the outputs by convenient modifications of synaptic connections. The error function which measures this difference was mean square error (MSE). In the training stage, 1300 isotopes except Sr, Xe, Er and Pb were used for training of the ANN. The test of the trained ANN was performed on Sr, Xe, Er and Pb isotopes which have been never seen before by the network.

# 3 Results and Discussions

The ANNs, as in this work, are capable of learning systematics of the binding and two nucleon separation energies for the isotopes with high accuracy. In this study

for different h numbers, the minimum MSE values were between 0.00002 and 0.01 for training stage and 0.00003 and 0.005 for testing stage. The differences in total binding energy of nuclei between the HFB calculations and ANNs results for SLy4 and SKP Skyrme parameters are shown in Fig. 2. As can be seen in the figure, the ANN outputs are consistent with the calculations. The differences between calculated results obtained from HFB method with SKP parameters and ANN outputs are smaller than those of SLy4 Skyrme parameters.

![](images/2c6f11da188c4dfd3e96e4707d174f05012a1461dd70e321a9ee171ac8331bf0.jpg)  
Fig. 2. The differences of total binding energy of nuclei between the HFB calculations and ANN calculations for SLy4 (left panels) and SKP (right panels) Skyrme parameters. Upper panels show the differences for test data while lower panels show train data.

In Fig. 3 and 4, we show two-neutron separation energies of Sr, Xe, Er and Pb isotopic chains obtained by ANN method based on HFB results with Skyrme forces SLy4 and SKP, respectively. Also, the results of the HFB calculations taken from [5] are shown in the same figures for comparison. As can be seen in these figures, the predictions of two-neutron separation energies of ANNs close to the input data. This results show the predictive power of ANN method in the present study. As is well known nuclei have a shell closure at magic neutron numbers $N = 5 0$ , 82 and 126). In particular, the correct predictions of abrupt decreases of two-neutron separation energies at magic neutron numbers are in agreement with the HFB predictions.

We have also obtained two-proton separation energies of Sr, Xe, Er and Pb isotopic chains with ANN method. The results are shown in Fig. 5 and 6 for SLy4 and SKP Skyrme forces, respectively. In the calculations same methodology has been followed as in the calculation of the two-neutron separation energies. The results of the ANNs are in good agrement with the HFB calculations with Skyrme forces SLy4 and SKP, respectively. Also, the results of the HFB calculations taken from [5] are shown for comparison in the same figures.

![](images/ffd5e93c7da68a4773688773e06f47425147f511c46b0851dcf18ce1136cfff0.jpg)  
Fig. 3. Calculated two-neutron separation energies of Sr, Xe, Er and Pb isotopic chains in HFB method with Skyrme force SLy4 [5] and the results of the present study with ANN method

![](images/5aba6c1c232ca6be27756a0c2de5f2b5e3a67b859bb0a74aef0d3ae3ca331b9b.jpg)  
Fig. 4. Calculated two-neutron separation energies of Sr, Xe, Er and Pb isotopic chains in HFB method with Skyrme force SKP [5] and the results of the present study with ANN method

![](images/b08b23f9b01242539276ce84c31d46c1d656d67ea4088db85d3479d2054f8246.jpg)  
Fig. 5. Calculated two-proton separation energies of Sr, Xe, Er and Pb isotopic chains in HFB method with Skyrme force SLy4 [5] and the results of the present study with ANN method

![](images/6e0a893c53cc34a3d76e9735edeeac1e0e0f0cc67444ec914e4416ab65aae081.jpg)  
Fig. 6. Calculated two-proton separation energies of Sr, Xe, Er and Pb isotopic chains in HFB method with Skyrme force SKP [5] and the results of the present study with ANN method

# 4 Summary

Artificial neural network (ANN) has been employed to investigate the groundstate energies of nuclei. In the calculations, the binding energies of even-even 46 isotopic chains calculated in HFB method with SLy4 and SKP Skyrme forces have been used as input data. The ANN results for the ground-state binding energies of nuclei have been obtained as in agreement with the original data. Also, we have employed ANN method to obtain two-neutron and two-proton separation energies of Sr, Xe, Er and Pb isotopic chains. The results show that ANNs are capable in describing systematics of the ground-state energies of nuclei. Particularly it has been understood that one should take into account of predictive power of ANNs when dealing with area which is unknown experimentally.

# References

1. Stoitsov M V, Dobaczewski J Nazarewicz W and Ring P 2005 Comp. Phys. Commun. 167, 43.   
2. Ring P and Schuck P, 1980 The Nuclear Many-Body Problem. Springer-Verlag, Berlin.   
3. Greiner W and Maruhn J, 1996 Nuclear Models. Springer-Verlag, New York.   
4. Chabanat E, Bonche P, Haensel P, Meyer J and Schaeffer, R 1998 Nucl. Phys. A 635, 231.   
5. Skyrme-HFB deformed nuclear mass table, http://www.fuw.edu.pl/~dobaczew/ \thodri/thodri.html   
6. Athanassopoulos S, Mavrommatis E, Gernoth K A and Clark J W 2004 Nuclear Physics A 743, 222.   
7. David C, Freslier M and Aichelin J 1995 Phys. Rev. C 51, 3, 1453.   
8. Bass S A, Bischoff A, Maruhn J A St¨ocker H and Greiner W 1996 Phys. Rev. C 53, 5, 2358.   
9. Haddad F, Hagel K, Li J, Mdeiwayeh N, Natowitz J B, Wada R, Xiao B, David C, Freslier M and Aichelin J 1997 Phys. Rev. C 55, 3, 1371.   
10. Costiris N, Mavrommatis E, Gernoth K A and Clark J W 2007 arXiv:nuclth/0701096v1.   
11. Graczyk K.M 2011 Phys. Rev. C 84, 034314.   
12. Akkoyun S, Bayram T, Kara S O and Sinan A 2012 arXiv:1212.6319 [nucl-th].   
13. Haykin S, 1999 Neural Networks: A Comprehensive Foundation. Prentice-Hall Inc., Englewood Cliffs, NJ, USA.   
14. Levenberg K, 1944 Quart. Appl. Math., Vol. 2, 164.   
15. Marquardt D, 1963. SIAM J. Appl. Math., Vol. 11, 431.