# Nuclear Mass Predictions Using a Neural Network with Additive Gaussian Process Regression-Optimized Activation Functions

H. X. Liu (刘辉鑫),1 S. Manzhos,2 and X. H. Wu (吴鑫辉)1, ∗

1Department of Physics, Fuzhou University, Fuzhou 350108, Fujian, China

$^ 2$ School of Materials and Chemical Technology, Institute of Science Tokyo, Tokyo 152-8552, Japan

Nuclear masses are machine-learned as a function of proton and neutron numbers. The neural network with additive Gaussian process regression-optimized activation functions (GPR-NN) method is employed for the first time for this purpose. GPR-NN combines the advantages of both neural networks and Gaussian process regression, in that it possesses the expressive power of an NN, in principle allowing modeling any kind of dependence of nuclear mass on the features, and robustness of a linear regression with respect to overfitting. A study of the GPR-NN approach for interpolation and extrapolation in nuclear mass predictions is presented. It is found that the optimal hyperparameters for the GPR-NN approach in interpolation and extrapolation are different. If an appropriate set of hyperparameters is adopted, the GPR-NN approach can achieve good extrapolation performance for nuclear mass prediction, which could potentially help improve the mass predictions of a large number of currently experimentally unknown nuclei.

# I. INTRODUCTION

The knowledge of nuclear masses is important for not only nuclear physics [1–3], but also nuclear astrophysics [4–6]. Experimentally, about 2500 nuclear masses have been measured to date [7]. Nevertheless, most exotic nuclei still remain beyond the current experimental capabilities, especially the neutron-rich ones related to the $r$ -process nucleosynthesis. Therefore, nuclear mass predictions from models are essential. Many efforts have been made to describe nuclear masses, including macroscopic models [8], macroscopic-microscopic models [9– 12], and microscopic models [13–18]. Among these models, the macroscopic-microscopic models, e.g., FRDM [11] and WS4 [10], are the ones most frequently used in related studies, especially in the $r$ -process studies [5, 19– 22]. However, different models can predict very different nuclear masses for neutron-rich exotic nuclei far away from the experimentally known region, indicating that uncertainties of theoretical models are still quite significant in predicting these exotic nuclei.

Efforts in two directions are ongoing to provide accurate nuclear mass predictions. One direction is to build microscopic nuclear mass models with more effects being included, e.g., the on-going DRHBc mass table project [18, 23, 24] which includes pairing, deformation, and continuum effects simultaneously. Microscopic models are usually believed to have a better reliability of extrapolation [3, 25], although their precision of pre-dicting experimentally known masses is currently poorer than that of the macroscopic-microscopic models.

Meanwhile, the other direction involves improving nuclear mass predictions using machine learning techniques [26–35]. The problem of nuclear mass prediction can be said to have become a testbed for the application of machine learning in nuclear physics. Most stan-

dard machine-learning approaches have been employed in nuclear mass studies, such as the kernel ridge regression (KRR) [32, 36–38] and Gaussian process regression (GPR) approaches [29], the radial basis function (RBF) approach [39, 40], the (Bayesian) neural network (NN) approach [26, 28], the principal component analysis (PCA) approach [41, 42], and so on. After a machine learning approach is successfully applied to nuclear mass, it will be promoted to applications in other aspects of nuclear physics. For example, the successful applications of the KRR approach in nuclear masses [32–38, 43, 44] have also stimulated its applications to other topics in nuclear physics, including the energy density functionals [45–47], charge radii [48, 49], and neutron-capture cross-sections [50].

Different machine-learning approaches have different advantages and disadvantages. For example, the neural network (NN) approach [51] has the advantage of high expressive power (universal approximator property) but requires non-linear optimization of a large number of parameters, which exacerbates the problem of overfitting and local minima, and can be CPU-intense for large NNs. Kernel regressions [52] such as the Gaussian process regression (GPR) combine the expressive power of a nonlinear method (achieved with nonlinear kernels) and robustness of regularized linear regression that it is; this can provide reliable machine learning from small datasets, and interpretability, especially with the use of structured kernels [53, 54], but kernel regression is difficult to use with large datasets and high-dimensional kernels [55–57]. The expressive power is also limited by the choices of nonlinear kernels that can only capture a restricted range of complex relationships.

A recently proposed machine learning approach, i.e., neural network with additive Gaussian process regression-optimized activation functions (GPR-NN) [58], combines the advantages of both NN and GPR approaches. It builds a representation of the target function that has the same form as a single hidden layer NN

with optimal shapes of neuron activation functions in the feature space, while algorithmically it is 1st order additive GPR in the space of redundant coordinates corresponding to neuron arguments. The use of additive kernels avoids problems associated with multidimensional kernels. As the redundant coordinates (corresponding to NN weights matrix) are defined by rules and no nonlinear optimization is performed, the method avoids overfitting as the number of neurons is grown beyond optimal, and obviates the problem of local minima. All neuron activation functions are optimal for given data and given redundant coordinates (weight matrix) and are obtained in one linear step.

The GPR-NN approach has been successfully employed to the construction of molecular potential energy surfaces [58, 59], to predicting properties of materials from chemical composition and structure (materials informatics) [60, 61], and to neuromorphic computing [62]. While being general, it allows interpretative ML including analysis of feature importance and of the type of functional dependence of the target on the features [60, 63].

In this work, the GPR-NN approach is employed to improve the nuclear mass predictions. The corresponding hyperparameters, including number of redundant coordinates $R$ , the length scale of the kernel $L$ , and the regularization parameter $\delta$ , are studied and optimized through careful validations for both interpolation and extrapolation. The performance and reliability of the GPR-NN approach in extrapolating nuclear mass predictions are analyzed in detail.

# II. THEORETICAL FRAMEWORK

The GPR-NN approach [58] is a hybrid between a single-hidden layer NN and GPR. The target function $f ( { \pmb x } )$ , $\textbf { \textit { x } } \in \textbf { \textit { R } } ^ { d }$ is represented as a first-order additive model in redundant coordinates $y \in R ^ { D }$ , $D > d$ , with the component functions constructed with GPR:

$$
\begin{array}{l} f (\boldsymbol {x}) = \sum_ {n = 1} ^ {D} f _ {n} \left(y _ {n}\right) = \sum_ {n = 1} ^ {D} \left[ \sum_ {m = 1} ^ {M} k \left(y _ {n}, y _ {n} ^ {(m)}\right) c _ {m} \right] \tag {1} \\ = \sum_ {m = 1} ^ {M} \left[ \sum_ {n = 1} ^ {D} k \left(y _ {n}, y _ {n} ^ {(m)}\right) \right] c _ {m}, \\ \end{array}
$$

where $k ( y _ { n } , y _ { n } ^ { ( m ) } )$ is the kernel, and $m$ indexes training data points. Each component function $f _ { n } ( y _ { n } )$ and the corresponding kernel are one-dimensional and therefore issues with (non-additive) high-dimensional kernels are avoided. The coefficients $_ c$ are obtained using standard GPR methodology:

$$
\boldsymbol {c} = \left(\boldsymbol {K} + \delta \boldsymbol {I}\right) ^ {- 1} \boldsymbol {f}, \tag {2}
$$

with

$$
\boldsymbol {K} = \left( \begin{array}{c c c c} k (\boldsymbol {y} ^ {(1)}, \boldsymbol {y} ^ {(1)}) & k (\boldsymbol {y} ^ {(1)}, \boldsymbol {y} ^ {(2)}) & \dots & k (\boldsymbol {y} ^ {(1)}, \boldsymbol {y} ^ {(M)}) \\ k (\boldsymbol {y} ^ {(2)}, \boldsymbol {y} ^ {(1)}) & k (\boldsymbol {y} ^ {(2)}, \boldsymbol {y} ^ {(2)}) & \dots & k (\boldsymbol {y} ^ {(2)}, \boldsymbol {y} ^ {(M)}) \\ \vdots & \vdots & \ddots & \vdots \\ k (\boldsymbol {y} ^ {(M)}, \boldsymbol {y} ^ {(1)}) & k (\boldsymbol {y} ^ {(M)}, \boldsymbol {y} ^ {(2)}) & \dots & k (\boldsymbol {y} ^ {(M)}, \boldsymbol {y} ^ {(M)}) \end{array} \right) \tag {3}
$$

where $\delta$ is the regularization parameter and $k ( \pmb { y } ^ { ( m ) } , \pmb { y } ^ { ( m ^ { \prime } ) } )$ is the additive kernel function that is specified as

$$
\begin{array}{l} k (\boldsymbol {y} ^ {(m)}, \boldsymbol {y} ^ {(m ^ {\prime})}) = \sum_ {n = 1} ^ {D} k \left(y _ {n} ^ {(m)}, y _ {n} ^ {(m ^ {\prime})}\right) \\ = \sum_ {n = 1} ^ {D} \exp \left[ - \frac {1}{2 L ^ {2}} \left(y _ {n} ^ {(m)} - y _ {n} ^ {\left(m ^ {\prime}\right)}\right) ^ {2} \right], \tag {4} \\ \end{array}
$$

where $L$ represents the length parameter of the kernel.

The redundant coordinates $y _ { n }$ are linear functions of $_ { x }$ , $y = W x$ , where $W$ is defined by rules and is not optimized. Here, the original coordinates $_ { x }$ are included as a subset of $\mathbf { \Delta } _ { \mathbf { \mu } _ { 3 } }$ ( $y _ { n } = x _ { n }$ for $n = 1 , 2 , . . . , d _ { \scriptscriptstyle { , } }$ ) and the rows of matrix $W$ defining other $y _ { n }$ ( $n > d$ ) are chosen as elements of a $d$ -dimensional Sobol sequence [64]. Control of the number of redundant coordinates $R = D - d$ ) allows studying important hidden features and the coupling of features. All terms $f _ { n } ( y _ { n } )$ of Eq. (1) are computed as a single linear step with a standard GPR code. The only computational cost overhead vs. standard GPR is the summation in the kernel. Functions $f _ { n } ( y _ { n } )$ are optimal in the least squares sense for given $W$ and data.

The schematic diagram of the GPR-NN approach is illustrated in Fig. 1. In the space of the original features $_ { x }$ , it is analogous to to a single-hidden layer NN with $D$ neurons, with optimal shapes of neuron activation functions for each neuron. It possesses therefore a universal approximator property. Note that biases and output weights are subsumed in the definition of $f _ { n } ( y _ { n } )$ and need not be considered separately. As no nonlinear optimization is done, the method is as robust as linear regression (as GPR is a regularized linear regression with nonlinear basis functions derived from the kernel function), and there is no overfitting as $D$ exceed the optimal number of neurons.

# III. NUMERICAL DETAILS

The calculations are performed based on the MATLAB code of the GPR-NN approach developed in Ref. [58]. Applying the GPR-NN approach to the studies of nuclear mass predictions, the input is proton number and neutron number, i.e., $\mathbf { \boldsymbol { x } } ~ = ~ ( Z , N )$ . After the redundant coordinates $y _ { n }$ are generated with the Sobol sequence, the $y _ { n }$ for all the training nuclei are scaled to [0, 1]. The target function is nuclear mass residuals $M _ { \mathrm { r e s } }$ , i.e., deviations between experimental data and theoretical predictions. Therefore, the predicted mass for

![](images/9c42e7c24c6f92fd7926d0121302e923b6243998c0dc41f60a6091239f352c3d.jpg)

![](images/45a9060b7ee5e6e799bb28f54a73ccc76228ea86c9cd7452466b66ef00d33f62.jpg)  
FIG. 1. Schematic diagram of the GPR-NN approach–A comparison of NN and GPR-NN.

a nucleus $( Z , N )$ is, thus, given by $M _ { \mathrm { G P R - N N } } ( Z , N ) =$ $M _ { \mathrm { t h } } ( Z , N ) + M _ { \mathrm { r e s } } ( Z , N )$ .

In the training process of the GPR-NN, the experimental nuclear masses from AME2020 [7] are taken for the nuclei with $Z \ \geq \ 8$ and $N \ \geq \ 8$ , while the masses with experimental error exceeding 100 keV are excluded. The theoretical predictions are taken from the RCHB nuclear mass model [16]. An overlap between the processed AME2020 and RCHB mass table was retained, encompassing 2278 nuclei. During the process of validating generalization ability, experimental mass data sets, AME1983 [65], AME1993 [66], AME2003 [67], and AME2012 [68] are also utilized.

# IV. RESULTS AND DISCUSSION

The hyperparameters involved in the GPR-NN approach includes the number of redundant coordinates $R$ , the length scale of the kernel $L$ , and the regularization parameter $\delta$ . In order to determine the hyperparameters $( R , L , \delta )$ , the data set of 2278 nuclei is randomly divided into ten bins of equal size (for convenience, eight nuclei are ignored randomly in the partitioning). For each bin, the GPR-NN is trained on the remaining samples using a series of hyperparameter sets. The obtained rms deviations are used to evaluate the performance of the corresponding hyperparameter sets. This procedure is also known as the so-called tenfold cross-validation, which is much efficient than the leave one out cross-validation.

The rms deviations $\Delta _ { \mathrm { r m s } }$ of the GPR-NN predictions relative to the experimental data under different sets of hyperparameters are presented in Fig. 2. As can be seen from Fig. 2, the performance of the GPR-NN approach is affected by the hyperparameters, and thus one should carefully validate the hyperparameters $( R , L , \delta )$ . On the other hand, in the basin around the optimal values of $( R , L , \delta )$ , the results are relatively stable with respect to specific values of $( R , L , \delta )$ , showing that the method is robust. One can see from each subplot with fixed $R$ , the hyperparameters $( L , \delta )$ can be well determined according to the minima of the rms deviations. The hyperparame-

ters $L$ and $\delta$ do not sensitively depend on $R$ , which enables increasing $R$ until the test error plateaus without or with minimal effort of retuning the hyperparameters.

It can also be noticed from Fig. 2 that the plots with $R \geq 3$ are generally identical, which indicates that the number of redundant coordinates $R = 3$ would be enough. This can be seen more clearly in Fig. 3, where the minima of the rms deviations $\Delta _ { \mathrm { r m s } }$ for each given $R$ are presented. For $R = 0$ , the rms deviation $\Delta _ { \mathrm { r m s } }$ is still as large as $\sim 1 0 0 0 \ \mathrm { k e V }$ , and then the $\Delta _ { \mathrm { r m s } }$ decreases with the inclusion of redundant coordinates. This indicates the importance of coupling between $Z$ and $N$ . When $R \geq 3$ , the $\Delta _ { \mathrm { r m s } }$ converges to about 440 keV. This means when applying the GPR-NN approach to the studies of nuclear masses, the number of redundant coordinates $R = 3$ is typically sufficient, and this value will be adopted for the remainder of this work. Fig. 3 also highlights the robustness of the method in that any sufficiently high value of $R$ will achieve a similar level of error, there is no overfitting when $R$ is larger than an optimal value. In the case of $R = 3$ , the other two optimized hyperparameters obtained from the tenfold cross-validation (see Fig. 2 (d)) are ( $L = 0 . 0 3 1 , \delta = 0 . 0 0 1$ ). This represents the optimized hyperparameters of the GPR-NN approach in the interpolation.

![](images/0c8190f399599778d05a64a9a50f886b088183400ba46a2901c5ba0d7f22f690.jpg)  
FIG. 2. The rms deviations obtained by the tenfold crossvalidation with different hyperparameters $( R , L , \delta )$ . Each panel presents the results with a specific number of redundant coordinates $R$ . The minima are labeled with red dots.

The predictive power of a machine-learning-based approach when extrapolating to experimentally unknown regions is more important. To evaluate this, similar to Ref. [32], for each isotopic chain, the eight most neutronrich nuclei are removed from the training set, and they are classified into eight test sets respectively, corresponding to the different extrapolation distances from the remain training set in the neutron direction.

In Fig. 4, the rms deviations $\Delta _ { \mathrm { r m s } }$ of the calculated masses for the eight test sets from the RCHB mass model, the GPR-NN approach with hyperparameters optimized in the interpolation (i.e., $L = 0 . 0 3 1 , \delta = 0 . 0 0 1$ ), and the GPR-NN approach with a new set of hyperparameters (i.e., $L = 0 . 0 8 0 , \delta = 0 . 2 0 0$ ), with respect to the experimental masses are shown as functions of the extrapolation distance.

![](images/d5c0c4511091d449fde4855af6235cee7b2811a902f26c6b8503ffc482844e03.jpg)

![](images/82f634e87fd6c95b34c5f33b255b9d75f841f9189afaafac02741240d7b62a45.jpg)  
FIG. 3. The minima of the rms deviations $\Delta _ { \mathrm { r m s } }$ obtained by the tenfold cross-validation by optimizing over $L$ and $\delta$ , for each specific number of redundant coordinates $R$ .   
FIG. 4. Comparison of the extrapolation power of the RCHB mass model, the GPR-NN approach with hyperparameters optimized in the interpolation (i.e., $L = 0 . 0 3 1 , \delta = 0 . 0 0 1$ ), and the GPR-NN approach with a new set of hyperparameters (i.e., $L = 0 . 0 8 0 , \delta = 0 . 2 0 0$ ) for eight test sets with different extrapolation distances (see text for details).

One can see from Fig. 4 that when the set of hyperparameters $L = 0 . 0 3 1 , \delta = 0 . 0 0 1$ ) optimized in the interpolation is adopted, the GPR-NN approach does not perform well in the extrapolation. The rms deviations $\Delta _ { \mathrm { r m s } }$ increase rapidly with the extrapolation distance, and they are even larger than the ones for the RCHB mass model, which means that the GPR-NN worsens the RCHB prediction instead of improving it in such extrapolation distance. This at least indicates that the hyperparameters optimized in the interpolation through ten-fold cross-validation are not guaranteed to perform well in the extrapolation. Optimal $L$ in the training region was low due to high corrugation of the mass as a function of $Z$ and $N$ , and the low $L$ naturally is detrimental to extrapolation.

However, the GPR-NN approach can perform very well in the extrapolations if one uses other sets of hyperparameters, e.g., ( $L = 0 . 0 8 0 , \delta = 0 . 2 0 0$ ), a new set of hy-

perparameters obtained by optimizing the GPR-NN predictions for these eight extrapolation test sets. Note that the new set of hyperparameters has larger length scale of the kernel $L$ , which is important for the extrapolation. It also has larger regularization parameter $\delta$ , which helps reduce overfitting. As can be seen from Fig. 4, with new hyperparameters optimized for extrapolation, the GPR-NN can significantly improve the RCHB predictions even at large extrapolation distances. This indicates that the GPR-NN approach loses its extrapolation capability relatively gradually as the extrapolation distance increases, which is an important feature for studying $r$ -processrelated neutron-rich nuclei far from the experimentally known region.

In order to study the generalization ability of the GPR-NN approach, the available 2278 data are divided into five sets according to the corresponding releasing time of the AME series [7, 65–68]. The details of the division are given in Fig. 5. The nuclei in the gray part are the overlap between the AME2020 [7] and AME1983 [65], except for those with errors beyond 100 keV. This gray part, labeled as AME1983 in the following, includes 1335 nuclei, and is considered as the training set. The other four groups, AME83-93 with 177 nuclei, AME93-03 with 404 nuclei, AME03-12 with 254 nuclei, and AME12-20 with 108 nuclei, are taken as the test sets, which correspond to the new data in AME1993, AME2003, AME2012, and AME2020, respectively.

![](images/04b1c8072d9b5a60e984cfab878ae7eb8c1b601aa860a088c83c427a586c767d.jpg)  
FIG. 5. The nuclear landscape for nuclei with the masses experimentally measured. The nuclei with masses firstly compiled in different time periods for AME, including AME1983 [65], AME83-93 [66], AME93-03 [67], AME03-12 [68], and AME12-20 [7], are labeled by different colors.

Figure 6 presents the $\Delta _ { \mathrm { r m s } }$ of nuclear mass in the RCHB, RBF, KRR, and GPR-NN predictions relative to the the five sets of available data. Two sets of hyperparameters, optimized for interpolation and extrapolation respectively, are adopted for the GPR-NN approach. The RBF and KRR predictions, obtained using the same manner as in Ref. [35], are provided for comparison. In the predictions for set AME1983, the leave-one-out crossvalidation is applied. In the predictions for sets AME83-

93, AME93-03, AME03-12, and AME12-20, predictions are made using the model trained on AME1983. One can see that the GPR-NN with hyperparameters optimized for interpolation achieves better performance than that with hyperparameters optimized for extrapolation. This is reasonable, as leave-one-out predictions for set AME1983 are certainly related to interpolation. One can see that the GPR-NN with hyperparameters optimized for extrapolation always provide a much lower $\Delta _ { \mathrm { r m s } }$ in all other four sets of data.

![](images/8b94027831c45fd5f46846caa3192a5b7ce527e3129ed12fccbae401fa927b71.jpg)  
FIG. 6. The rms deviations of nuclear mass $M$ of the RCHB, RBF, KRR, and GPR-NN predictions from the available data in the 5 sets, as divided in Fig. 5. Two sets of hyperparameters, optimized for interpolation and extrapolation respectively, are adopted for the GPR-NN approach.

It should be noted that the GPR-NN with hyperparameters optimized for extrapolation achieves better performance than the RBF and KRR approaches for large extrapolation sets, i.e., AME03-12 and AME12-20. The $\Delta _ { \mathrm { r m s } }$ of the GPR-NN approach increases slowly with the extrapolation distance (from AME83-93 to AME12-20). Significant improvements from the GPR-NN corrections can still be observed even for the AME12-20 set. This means that the GPR-NN approach trained with the mass data released in AME1983 [65] can still help improve the predictions of masses that became available in experiments more than 30 years later. In other words, the GPR-NN approach trained with the mass data released

in 2020 [7] would potentially help improve the mass predictions of a large number of currently experimentally unknown nuclei.

# V. SUMMARY

In summary, we have applied the neural network with additive Gaussian process-optimized activation functions (GPR-NN) to enhance nuclear mass predictions for the first time. By combining the strengths of neural networks and Gaussian processes, GPR-NN effectively models nuclear mass residuals relative to the RCHB theoretical predictions using experimental data from AME2020 for 2278 nuclei with $Z \geq 8$ and $N \geq 8$ . Hyperparameters, including the number of redundant coordinates $R$ , kernel length scale $L$ , and regularization parameter $\delta$ , are optimized through tenfold cross-validation for interpolation, yielding $R = 3$ , $L = 0 . 0 3 1$ , and $\delta = 0 . 0 0 1$ , with an rms deviation of approximately 440 keV. For extrapolation, a distinct set $L = 0 . 0 8 0 , \delta = 0 . 2 0 0 ,$ is found optimal, with rms deviations increasing gradually even at large distances. Generalization tests using historical AME data sets (1983-2020) indicate that GPR-NN performs well in long-range extrapolations, maintaining significant improvements for nuclei measured decades later. Overall, this study validates the GPR-NN as a robust and promising tool for nuclear mass predictions. Its good extrapolation performance, when paired with appropriate hyperparameters, makes it valuable for improving the mass predictions for experimentally unknown, neutronrich nuclei. This lays the groundwork for future applications in nuclear physics and nuclear astrophysics, such as refining $r$ -process nucleosynthesis models.

# ACKNOWLEDGMENTS

This work was partly supported by the National Natural Science Foundation of China under Grant No. 12405134 and the start-up grant XRC-23103 of Fuzhou University.

[1] T. Yamaguchi, H. Koura, Y. Litvinov, and M. Wang, Prog. Part. Nucl. Phys. 120, 103882 (2021).   
[2] B. Monteagudo, F. M. Marqu´es, J. Gibelin, N. A. Orr, A. Corsi, Y. Kubota, J. Casal, J. G´omez-Camacho, G. Authelet, H. Baba, C. Caesar, D. Calvet, A. Delbart, M. Dozono, J. Feng, F. Flavigny, J.-M. Gheller, A. Giganon, A. Gillibert, K. Hasegawa, T. Isobe, Y. Kanaya, S. Kawakami, D. Kim, Y. Kiyokawa, M. Kobayashi, N. Kobayashi, T. Kobayashi, Y. Kondo, Z. Korkulu, S. Koyama, V. Lapoux, Y. Maeda, T. Motobayashi, T. Miyazaki, T. Nakamura, N. Nakatsuka, Y. Nishio, A. Obertelli, A. Ohkura, S. Ota, H. Otsu,

T. Ozaki, V. Panin, S. Paschalis, E. C. Pollacco, S. Reichert, J.-Y. Rousse, A. T. Saito, S. Sakaguchi, M. Sako, C. Santamaria, M. Sasano, H. Sato, M. Shikata, Y. Shimizu, Y. Shindo, L. Stuhl, T. Sumikama, Y. L. Sun, M. Tabata, Y. Togano, J. Tsubota, T. Uesaka, Z. H. Yang, J. Yasuda, K. Yoneda, and J. Zenihiro, Phys. Rev. Lett. 132, 082501 (2024).   
[3] K. Y. Zhang, C. Pan, X. H. Wu, X. Y. Qu, X. X. Lu, and G. A. Sun, AAPPS Bulletin 35, 13 (2025).   
[4] M. Mumpower, R. Surman, G. McLaughlin, and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016).

[5] X. F. Jiang, X. H. Wu, and P. W. Zhao, Astrophys. J. 915, 29 (2021).   
[6] X.-H. Wu and J. Meng, Sci. Bull. 68, 539 (2023).   
[7] M. Wang, W. Huang, F. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003 (2021).   
[8] C. F. v. Weizs¨acker, Z. Physik 96, 431 (1935).   
[9] J. Pearson, R. Nayak, and S. Goriely, Phys. Lett. B 387, 455 (1996).   
[10] N. Wang, M. Liu, X. Wu, and J. Meng, Phys. Lett. B 734, 215 (2014).   
[11] P. M¨oller, A. Sierk, T. Ichikawa, and H. Sagawa, Atom. Data Nucl. Data Tables 109-110, 1 (2016).   
[12] H. Koura, T. Tachibana, M. Uno, and M. Yamada, Prog. Theor. Phys. 113, 305 (2005).   
[13] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. Lett. 102, 152503 (2009).   
[14] S. Goriely, S. Hilaire, M. Girod, and S. P´eru, Phys. Rev. Lett. 102, 242501 (2009).   
[15] D. Pe˜na-Arteaga, S. Goriely, and N. Chamel, The European Physical Journal A 52, 320 (2016).   
[16] X. Xia, Y. Lim, P. Zhao, H. Liang, X. Qu, Y. Chen, H. Liu, L. Zhang, S. Zhang, Y. Kim, and J. Meng, Atom. Data Nucl. Data Tables 121-122, 1 (2018).   
[17] Y. L. Yang, Y. K. Wang, P. W. Zhao, and Z. P. Li, Phys. Rev. C 104, 054312 (2021).   
[18] K. Zhang, M.-K. Cheoun, Y.-B. Choi, P. S. Chong, J. Dong, Z. Dong, X. Du, L. Geng, E. Ha, X.-T. He, C. Heo, M. C. Ho, E. J. In, S. Kim, Y. Kim, C.- H. Lee, J. Lee, H. Li, Z. Li, T. Luo, J. Meng, M.-H. Mun, Z. Niu, C. Pan, P. Papakonstantinou, X. Shang, C. Shen, G. Shen, W. Sun, X.-X. Sun, C. K. Tam, Thaivayongnou, C. Wang, X. Wang, S. H. Wong, J. Wu, X. Wu, X. Xia, Y. Yan, R. W.-Y. Yeung, T. C. Yiu, S. Zhang, W. Zhang, X. Zhang, Q. Zhao, and S.-G. Zhou, Atom. Data Nucl. Data Tables 144, 101488 (2022).   
[19] R. H. Cyburt, A. M. Amthor, R. Ferguson, Z. Meisel, K. Smith, S. Warren, A. Heger, R. D. Hoffman, T. Rauscher, A. Sakharuk, H. Schatz, F. K. Thielemann, and M. Wiescher, Astrophys. J. Suppl. Ser. 189, 240 (2010).   
[20] B. Zhao and S. Q. Zhang, Astrophys. J. 874, 5 (2019).   
[21] X. H. Wu, P. W. Zhao, S. Q. Zhang, and J. Meng, Astrophys. J. 941, 152 (2022).   
[22] Y. Y. Huang, Q. Q. Cui, X. H. Wu, and S. Q. Zhang, Astrophys. J. 988, 22 (2025).   
[23] C. Pan, M.-K. Cheoun, Y.-B. Choi, J. Dong, X. Du, X.- H. Fan, W. Gao, L. Geng, E. Ha, X.-T. He, J. Huang, K. Huang, S. Kim, Y. Kim, C.-H. Lee, J. Lee, Z. Li, Z.-R. Liu, Y. Ma, J. Meng, M.-H. Mun, Z. Niu, P. Papakonstantinou, X. Shang, C. Shen, G. Shen, W. Sun, X.-X. Sun, J. Wu, X. Wu, X. Xia, Y. Yan, T. C. Yiu, K. Zhang, S. Zhang, W. Zhang, X. Zhang, Q. Zhao, R. Zheng, and S.-G. Zhou (DRHBc Mass Table Collaboration), Phys. Rev. C 106, 014316 (2022).   
[24] P. Guo, X. Cao, K. Chen, Z. Chen, M.-K. Cheoun, Y.- B. Choi, P. C. Lam, W. Deng, J. Dong, P. Du, X. Du, K. Duan, X. Fan, W. Gao, L. Geng, E. Ha, X.-T. He, J. Hu, J. Huang, K. Huang, Y. Huang, Z. Huang, K. D. Hyung, H. Y. Chan, X. Jiang, S. Kim, Y. Kim, C.- H. Lee, J. Lee, J. Li, M. Li, Z. Li, Z. Li, Z. Lian, H. Liang, L. Liu, X. Lu, Z.-R. Liu, J. Meng, Z. Meng, M.-H. Mun, Y. Niu, Z. Niu, C. Pan, J. Peng, X. Qu, P. Papakonstantinou, T. Shang, X. Shang, C. Shen, G. Shen, T. Sun, X.-X. Sun, S. Wang, T. Wang,

Y. Wang, Y. Wang, J. Wu, L. Wu, X. Wu, X. Xia, H. Xie, J. Yao, K. Y. Ip, T. C. Yiu, J. Yu, Y. Yu, K. Zhang, S. Zhang, S. Zhang, W. Zhang, X. Zhang, Y. Zhang, Y. Zhang, Y. Zhang, Z. Zhang, Q. Zhao, Y. Zhao, R. Zheng, C. Zhou, S.-G. Zhou, and L. Zou, Atom. Data Nucl. Data Tables 158, 101661 (2024).   
[25] P. W. Zhao, L. S. Song, B. Sun, H. Geissel, and J. Meng, Phys. Rev. C 86, 064324 (2012).   
[26] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C 93, 014311 (2016).   
[27] L. Neufcourt, Y. C. Cao, W. Nazarewicz, and F. Viens, Phys. Rev. C 98, 034318 (2018).   
[28] Z. M. Niu and H. Z. Liang, Phys. Lett. B 778, 48 (2018).   
[29] L. Neufcourt, Y. Cao, W. Nazarewicz, E. Olsen, and F. Viens, Phys. Rev. Lett. 122, 062502 (2019).   
[30] Z. M. Niu and H. Z. Liang, Phys. Rev. C 106, L021303 (2022).   
[31] M. Li, T. M. Sprouse, B. S. Meyer, and M. R. Mumpower, Phys. Lett. B 848, 138385 (2024).   
[32] X. H. Wu and P. W. Zhao, Phys. Rev. C 101, 051301 (R) (2020).   
[33] X.-K. Du, P. Guo, X.-H. Wu, and S.-Q. Zhang, Chin. Phys. C 47, 074108 (2023).   
[34] X. H. Wu, C. Pan, K. Y. Zhang, and J. Hu, Phys. Rev. C 109, 024310 (2024).   
[35] Y. Y. Guo, T. Yu, X. H. Wu, C. Pan, and K. Y. Zhang, Phys. Rev. C 110, 064310 (2024).   
[36] X. H. Wu, L. H. Guo, and P. W. Zhao, Phys. Lett. B 819, 136387 (2021).   
[37] X. H. Wu, Y. Y. Lu, and P. W. Zhao, Phys. Lett. B 834, 137394 (2022).   
[38] X. H. Wu and C. Pan, Phys. Rev. C 110, 034322 (2024).   
[39] N. Wang and M. Liu, Phys. Rev. C 84, 051303 (2011).   
[40] Z. M. Niu, B. H. Sun, H. Z. Liang, Y. F. Niu, and J. Y. Guo, Phys. Rev. C 94, 054315 (2016).   
[41] X. H. Wu and P. W. Zhao, Sci. China-Phys. Mech. Astron. 67, 272011 (2024).   
[42] P. Giuliani, K. Godbey, V. Kejzlar, and W. Nazarewicz, Phys. Rev. Res. 6, 033266 (2024).   
[43] L. H. Guo, X. H. Wu, and P. W. Zhao, Symmetry 14, 1078 (2022).   
[44] X. H. Wu, Front. Phys. 11, 1061042 (2023).   
[45] X. H. Wu, Z. X. Ren, and P. W. Zhao, Phys. Rev. C 105, L031303 (2022).   
[46] Y. Y. Chen and X. H. Wu, Int. J. Mod. Phys. E 33, 2450012 (2024).   
[47] X. Wu, Z. Ren, and P. Zhao, Communications Physics 8, 316 (2025).   
[48] J.-Q. Ma and Z.-H. Zhang, Chin. Phys. C 46, 074105 (2022).   
[49] L. Tang and Z.-H. Zhang, Nucl. Sci. Tech. 35, 19 (2024).   
[50] T. X. Huang, X. H. Wu, and P. W. Zhao, Commun. Theor. Phys. 74, 095302 (2022).   
[51] G. Montavon, G. B. Orr, and K.-R. M¨uller, eds., Neural Networks: Tricks of the Trade, 2nd ed., Lecture Notes in Computer Science, Vol. 7700 (Springer Berlin, Heidelberg, 2012).   
[52] C. M. Bishop, Pattern Recognition and Machine Learning, Information Science and Statistics (Springer, New York, NY, USA, 2006) also available online via Springer.   
[53] Y. M. Thant, T. Wakamiya, M. Nukunudompanich, K. Kameda, M. Ihara, and S. Manzhos, Chem. Phys. Rev. 6, 011306 (2025).

[54] S. Manzhos, T. Carrington, and M. Ihara, AI Chem. 1, 100008 (2023).   
[55] J. Quinonero-Candela and C. Rasmussen, J. Mach. Learn. Res. 6, 1939 (2005).   
[56] S. Manzhos and M. Ihara, J. Chem. Phys. 160, 021101 (2024).   
[57] S. Manzhos and M. Ihara, J. Chem. Phys. 158, 044111 (2023).   
[58] S. Manzhos and M. Ihara, J Phys. Chem. A 127, 7823 (2023).   
[59] S. Manzhos and M. Ihara, J. Chem. Phys. 159, 211103 (2023).   
[60] Y. Tang, B. Xiao, M. Ihara, S. Manzhos, and Y. Liu, J. Mater. Inform. 5, 38 (2025).   
[61] M. Nukunudompanich, H. Yoon, L. Hyojae, et al., MRS Adv. 9, 857 (2024).

[62] S. Manzhos, Q. G. Chen, W.-Y. Lee, Y. Heejoo, M. Ihara, and C.-C. Chueh, J. Phys. Chem. Lett. 15, 6974 (2024).   
[63] S. Manzhos, J. Luder, P. Golub, and M. Ihara, Mach. Learn.-Sci. Techn. 6, 035002 (2025).   
[64] I. Sobol’, USSR Comput. Math. & Math. Phys. 7, 86 (1967).   
[65] A. Wapstra and G. Audi, Nucl. Phys. A 432, 1 (1985).   
[66] G. Audi and A. Wapstra, Nucl. Phys. A 565, 1 (1993).   
[67] G. Audi, A. Wapstra, and C. Thibault, Nucl. Phys. A 729, 337 (2003), the 2003 NUBASE and Atomic Mass Evaluations.   
[68] M. Wang, G. Audi, A. Wapstra, F. Kondev, M. MacCormick, X. Xu, and B. Pfeiffer, Chin. Phys. C 36, 1603 (2012).