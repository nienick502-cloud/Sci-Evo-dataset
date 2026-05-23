# Nuclear mass systematics by complementing the Finite Range Droplet Model with neural networks

S. Athanassopoulos, E. Mavrommatis

Physics Department, Division of Nuclear & Particle Physics, University of Athens, GR–15771 Athens, Greece

K. A. Gernoth

School of Physics & Astronomy, University of Manchester, M13 9PL, UK

J. W. Clark

McDonnell Center for the Space Sciences and Department of Physics, Washington University, St. Louis, Missouri 63130, USA

# Abstract

A neural-network model is developed to reproduce the differences between experimental nuclear mass-excess values and the theoretical values given by the Finite Range Droplet Model. The results point to the existence of subtle regularities of nuclear structure not yet contained in the best microscopic/phenomenological models of atomic masses. Combining the FRDM and the neural-network model, we create a hybrid model with improved predictive performance on nuclear-mass systematics and related quantities.

# 1 Introduction

The problem of devising global models of nuclidic (atomic) masses (see Ref. [1] for a recent review) is of great current interest in connection with experimental studies of nuclei far from stability conducted at heavy-ion and radioactive ion-beam facilities and with the theory of nucleosynthesis and supernova explosions [2]. The spectrum of global mass models ranges from those with high theoretical input that explicitly take account of known physical principles in terms of a relatively small number of fitting parameters, to models that are shaped only by the data and thus have a correspondingly large number of

adjustable parameters. Current models of the former class that define the state of the art are the Finite Range Droplet Model (FRDM) of M¨oller, Nix, and coworkers [3] and the Hartree-Fock-Bogoliubov model (HFB2) of Pearson, Tondeur and coworkers [4]. Statistical models based on neural networks are situated far toward the other end of the spectrum. They have been under continuing development in recent years, to the extent that they can now provide a valuable complement to conventional global models [5].

Here we provide a preliminary report of results from a synthesis [6] of the two approaches. Training by example, a neural network is constructed that estimates the differences $\Delta M ^ { \mathrm { e x p } } - \Delta M ^ { \mathrm { F R D M } }$ between experiment and the FRDM, where $\Delta M$ denotes the nuclidic mass excess. Combining the FRDM with this neural network, we obtain a hybrid global mass model that performs with precision both in reproducing $\Delta M$ values for familiar nuclei and predicting them for new nuclei. This strategy is pursued with the hope of determining whether the residual physical corrections to the FRDM model (a) stem from a large number of small effects that may fluctuate strongly with $Z$ and $N$ , defying systematic quantification, or instead (b) can be attributed in part to regularities of nuclear structure not yet embodied in theory.

![](images/8ff45f52187e8341923bd58d4d786914d9b4aaf56a6e27eac4ec5b59a5636c18.jpg)  
Fig. 1. Locations in the $N - Z$ plane are indicated for the M1, M2, and M3 data sets employed in neural-network modeling of the differences between experimental mass-excess values and those given by the FRDM.

# 2 Neural-network model of the mass differences

A multilayer feedforward architecture is adopted for the neural network, having the structure indicated schematically by (4–6–6–6–1)[169]. The four input units encode the atomic number $Z$ , the neutron number $N$ , and their respective parities. The single output unit encodes the mass-excess difference $\Delta M ^ { \mathrm { e x p } } - \Delta M ^ { \mathrm { F A D M } }$ . Three intermediate layers, each containing six units, transfer information from input to output through weighted connections. The total number of weight parameters charactering the network is 169. To construct the neural-network model, we have employed the database of 1654 nuclei fitted by the FRDM parameterization of Ref. [3], screening out some uncertain cases in light of the more recent experimental mass-excess assignments published in the 2003 Atomic Mass Evaluation (AME03) [7]. The surviving 1620 nuclei are divided randomly into two data sets of 1276 (M1) and 344 (M2) nuclei, which respectively comprise the learning and validation sets for neural-network modeling. Performance on the learning set serves as the criterion for progressive adjustment of the weights of the feedforward connections, while performance on the validation set is used to guide the termination of training. To obtain an unambiguous measure of predictive performance, some of the data must be reserved as a test set, or prediction set, which is never referred to during the training process. The test set (denoted M3) is provided by the remaining 529 nuclei of the AME03 evaluation. These data points correspond predominantly to nuclides far from stability, lying on the outer fringes of the 1620-nuclide set $M 1 \cup M 2$ as viewed in the $N - Z$ plane (see Fig. 1). The ability of the neural network to model the difference $\Delta M ^ { \mathrm { e x p } } - \Delta M ^ { \mathrm { F R D M } }$ is illustrated in Fig. 2.

![](images/62b5e69a5e1c1b51d39737216d9bd40ddd3466684951389cdb1bb56b9a08c34f.jpg)  
Fig. 2. Mass-excess differences between experiment and FRDM for the data sets M1 and M2 involved in the training process are compared with the corresponding differences predicted by the neural network.

It is seen that the deviations of the FRDM evaluation from experiment for the data sets M1 and M2 involved in the training process can be substantially reproduced by the neural network.

# 3 Mass excess evaluation – Hybrid Model

To generate and predict mass-excess values for nuclides of specified $Z$ and $N$ , we construct a hybrid model by combining the FRDM outputs with the difference values predicted by the neural-network model described in Section 2. In Table 1 we compare performance (measured by the rms error $\sigma _ { \mathrm { r m s } }$ ) on the learning, validation, and prediction sets for (i) the hybrid model, (ii) the neural-network mass model of Ref. [5] and its most recent version [6] and (iii) the theoretical models FRDM [3] and HFB2 [4]. The neural-network mass models of Refs. [5,6] were trained to directly predict mass-excess values (as opposed to differences of mass-excess values). Likewise, the FRDM and HFB2 models were fitted to mass-excess data.

Overall, the hybrid model shows the best performance among the four models considered, having very small error figures even for the prediction set M3. Further insight into the behavior of the hybrid model of mass excess is furnished by Fig. 3, where the rms error of the difference estimate per isotope chain, i.e., calculated for all $N$ for given $Z$ , is plotted for the full database $M 1 \cup M 2 \cup M 3$ . For the majority of chains, the hybrid model yields smaller errors than FRDM and HFB2.

# 4 Mass-related nuclear quantities – Hybrid Model

Mass-related quantities of interest can also be evaluated based on the various models of mass excess, statistical and theoretical. Table 2 presents the rms Table 1

Root-mean-square error σrms(MeV) in estimation of mass excess by global models (see text for details).

<table><tr><td>Model</td><td>Learning set (M1)</td><td>Validation set (M2)</td><td>Prediction set (M3)</td></tr><tr><td>FRDM ([3])</td><td>0.68</td><td>0.71</td><td>0.58</td></tr><tr><td>HFB2 ([4])</td><td>0.67</td><td>0.68</td><td>0.67</td></tr><tr><td>Neural net mass model ([5])</td><td>0.44</td><td>0.44</td><td>0.95</td></tr><tr><td>Neural net mass model ([6])</td><td>0.28</td><td>0.40</td><td>0.71</td></tr><tr><td>Hybrid model</td><td>0.40</td><td>0.49</td><td>0.41</td></tr></table>

![](images/b1d56909d3c66a0e350b9a0546f77e9a953246444cbb1830b16d275f6be80777.jpg)  
Fig. 3. RMS mass-excess error per isotope chain, plotted versus atomic number $Z$ for the full AME03 database. Results are shown for the hybrid, FRDM, and HFB2 global mass formulas.

errors in determination of the one- and two-proton separation energies $S ( p )$ and $S ( 2 p )$ , the one- and two-neutron separation energies $S ( n )$ and $S ( 2 n )$ , and the $Q$ -values for alpha and beta-minus decays, for all nuclei in AME03 with experimentally measured values. The hybrid model outperforms its competitors in all of the comparisons, although generally by smaller margins than for the mass excess (cf. Table 1). However, the ultimate test of any global model is in the accuracy it can achieve on nuclei that have not been used in adjusting its parameters. Table 3 reports rms errors in the separation energies and $Q$ - values for the subset of cases involving only nuclides of the prediction set $M 3$ . In this part of the nuclidic chart, the hybrid model demonstrates predictive performance comparable to that of FRDM alone.

Table 2 Performance of global mass models for various quantities related to nuclear-mass systematics, quantified by the corresponding rms error over all cases involving AME03 nuclides [7] for which experimentally measured values are available. Numerical entries are in MeV.   

<table><tr><td>Model</td><td>S(p) (1968)</td><td>S(2p) (1836)</td><td>S(n) (1988)</td><td>S(2n) (1937)</td><td>Q(α) (2039)</td><td>Q(β-) (1868)</td></tr><tr><td>FRDM ([3])</td><td>0.40</td><td>0.49</td><td>0.40</td><td>0.51</td><td>0.61</td><td>0.50</td></tr><tr><td>HFB2 ([4])</td><td>0.49</td><td>0.51</td><td>0.47</td><td>0.46</td><td>0.55</td><td>0.60</td></tr><tr><td>Neural net mass model ([5])</td><td>0.53</td><td>0.61</td><td>0.48</td><td>0.58</td><td>0.67</td><td>0.64</td></tr><tr><td>Neural net mass model ([6])</td><td>0.56</td><td>0.49</td><td>0.38</td><td>0.46</td><td>0.62</td><td>0.53</td></tr><tr><td>Hybrid model</td><td>0.36</td><td>0.40</td><td>0.35</td><td>0.42</td><td>0.48</td><td>0.42</td></tr></table>

# 5 Conclusions – Future steps

Global semi-empirical models of atomic masses have reached a stage of sophisication such that sub-MeV accuracy is achievable in predicting the mass excess of newly created nuclides. At this stage one is naturally led to inquire whether the residual errors are “chaotic” or random in nature, arising from the fluctuation and interplay of a large number of small physical effects as well as some experimental error. We have addressed this question by creating a neural-network model that generates the difference between experimental mass excesses and the values given by a state-of-the-art global mass model, specifically, the Finite Range Droplet Model of M¨oller, Nix, and coworkers [3]. Our results suggest that a significant portion of the residual error (perhaps 30-40%) can be treated systematically, i.e., some regularities remain to be extracted from the data. More extensive neural-network studies aimed at revealing the statistical behavior of the discrepancy are needed to test this inference.

The present work has shown that hybrid models built by supplementing the FRDM evaluation with a trained neural network show promise of accurate prediction of atomic masses far from stability, as well as other nuclear properties required as input for theories of nucleosynthesis and supernova explosions.

Table 3 Performance of global mass models for various quantities related to nuclear-mass systematics, quantified by the corresponding rms error over all cases involving only nuclides of the prediction set M3. Numerical entries are in MeV.   

<table><tr><td>Model</td><td>S(p) (453)</td><td>S(2p) (434)</td><td>S(n) (435)</td><td>S(2n) (418)</td><td>Q(α) (465)</td><td>Q(β-) (387)</td></tr><tr><td>FRDM ([3])</td><td>0.41</td><td>0.44</td><td>0.40</td><td>0.40</td><td>0.52</td><td>0.51</td></tr><tr><td>HFB2 ([4])</td><td>0.45</td><td>0.46</td><td>0.41</td><td>0.41</td><td>0.48</td><td>0.56</td></tr><tr><td>Neural net mass model ([5])</td><td>0.65</td><td>0.70</td><td>0.70</td><td>0.78</td><td>0.48</td><td>0.50</td></tr><tr><td>Neural net mass model ([6])</td><td>0.65</td><td>0.65</td><td>0.54</td><td>0.67</td><td>0.48</td><td>0.50</td></tr><tr><td>Hybrid model</td><td>0.41</td><td>0.39</td><td>0.37</td><td>0.41</td><td>0.48</td><td>0.50</td></tr></table>

# Acknowledgements

This research has been supported in part by the U. S. National Science Foundation under Grant No. PHY-0140316 and by the University of Athens under Grant No. 70/4/3309. We thank J. Rayford Nix for suggesting the hybrid strategy explored here.

# References

[1] D. Lunney, J. M. Pearson, C. Thibault, Rev. Mod. Phys. 75 (2003) 1021.   
[2] Opportunities in Nuclear Science: “A Long Range Plan in the Next Decade” (DOE/NSF, 2002); NUPECC Long Range Plan 2004: Perspectives for Nuclear Physics Research in Europe in the Coming Decade and Beyond” (April 2004).   
[3] P. M¨oller, J. R. Nix, W. D. Myers, W. J. Swiatecki, At. Data Nucl. Data Tables 59 (1995)185; P. M¨oller, J. R. Nix, K. L. Kratz, At. Data Nucl. Data Tables 66 (1997) 131.   
[4] S. Goriely, M. Samyn, P.-H. Heenen, J. M. Pearson, F. Tondeur, Phys. Rev. C66 (2002) 024326.   
[5] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, J. W. Clark, Nucl. Phys. A743 (2004) 222, and references therein.   
[6] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, J. W. Clark, to be submitted.   
[7] A. H. Wapstra, G. Audi, C. Thibault, Nucl. Phys. A729 (2003) 337.