# Nuclear binding energy predictions using neural networks: Application of the multilayer perceptron

Esra Y¨uksel,1, a) Derya Soydaner,2, b) and H¨useyin Bahtiyar3, c)

1)Department of Physics, Faculty of Science and Letters,   
Yildiz Technical University, Davutpasa Campus, 34220, Esenler, Istanbul, Turkey   
2)Department of Statistics, Mimar Sinan Fine Arts University, Bomonti 34380, Istanbul, Turkey   
3)Department of Physics, Mimar Sinan Fine Arts University, Bomonti 34380, Istanbul, Turkey

(Dated: 10 May 2021)

In recent years, artificial neural networks and their applications for large data sets have became a crucial part of scientific research. In this work, we implement the Multilayer Perceptron (MLP), which is a class of feedforward artificial neural network (ANN), to predict ground-state binding energies of atomic nuclei. Two different MLP architectures with three and four hidden layers are used to study their effects on the predictions. To train the MLP architectures, two different inputs are used along with the latest atomic mass table and changes in binding energy predictions are also analyzed in terms of the changes in the input channel. It is seen that using appropriate MLP architectures and putting more physical information in the input channels, MLP can make fast and reliable predictions for binding energies of atomic nuclei, which is also comparable to the microscopic energy density functionals.

# I. INTRODUCTION

One of the major research areas in nuclear physics is the nuclear mass (binding energy) predictions, especially for nuclei far from the stability line with extreme proton-neutron ratio. As the most fundamental property of nuclei, accurate nuclear mass measurements and theoretical predictions have vital importance not only for nuclear physics1 but also for nuclear astrophysics $^ { 2 - 4 }$ . Alongside with other nuclear properties (i.e., charge radii, separation energies, decay properties, etc.), the nuclear masses could provide information about the nucleon-nucleon interaction, shell, and pairing properties of nuclei, and its precise determination is also crucial for our understanding of the formation of chemical elements heavier than iron in the universe5.

In the last decades, nuclear mass measurements have gained acceleration with the developments in experimental facilities. According to the latest atomic mass table AME20166, the ground-state masses of 3435 nuclei have been measured. However, measurement of the ground-state properties for nuclei close to the drip lines still stands as a challenge. Also, there exist large deviations in theoretical model calculations for nuclei close to the drip lines. Therefore, further studies are needed to make reliable predictions in these regions. Up to now, microscopic-macroscopic (mic-mac) $^ { 7 - 9 }$ and microscopic models $_ \mathrm { 1 0 - 1 5 }$ have been employed for the mapping of the nuclear landscape. Although the microscopic models are more complete in terms of the physics behind them, much better results are obtained using the mic-mac models in nuclear mass predictions since their constants are determined using the experimental ground-state masses of nuclei. While the root-mean-square (rms) deviation of nuclear masses is generally high (several MeV) using the microscopic models, the FRDM20129 predicts an rms deviation 0.57 MeV with respect to the AME2003 atomic mass table16, and WS3 model gives even lower rms deviation (0.336 MeV) for nuclear masses8.

Considering the microscopic models, the first complete nuclear mass table was based on the well-known Skyrme Hartree–Fock (HF) method in the non-relativistic framework17, and the root-mean-square error was obtained as 0.738 MeV using the 1995 Audi–Wapstra compilation18. With further improvements, the HFB-31 mass model also gave a model error of 0.561 MeV for the measured mass of 2353 nuclei19. Using the Gogny HFB method, the rms deviation was obtained as 0.798 MeV with respect to the experimental predictions of the 2149 nuclei11. A systematic study was also conducted on 6969 nuclei to predict

nuclear properties using the relativistic mean-field model, and rms deviation for nuclear masses was obtained as 2.1 MeV20. According to the latest microscopic mass model based on the relativistic continuum Hartree-Bogoliubov (RCHB) theory21, the root-mean-square deviation of the binding energies with respect to the experimental data was obtained at around several MeV. Although considerable progress has been achieved with the mic-mac and microscopic models, the rms deviations are still high and one needs more accurate results, especially for astrophysical applications. Therefore, different approximations and models are required to understand the discrepancies in the results as well as to make more precise predictions.

In recent years, there has been an increasing amount of interest in artificial neural networks $2 2 \mathrm { - } 2 8$ , which is known as a nonparametric estimator in Machine Learning (ML). Applications of neural networks cover many areas in science as well as the different branches of physics. Considering the variety and richness of the available experimental data, nuclear physics is also a good candidate to study using neural networks. Long ago, several studies were performed to predict nuclear properties using various techniques $^ { 2 9 - 3 1 }$ . Neural networks were used to predict nuclear mass excess and neutron separation energies $^ { 3 0 }$ , and it is shown that neural networks can be used as a new tool to predict the properties of atomic nuclei. Later on, nuclear mass defect predictions were made using the neural networks, showing that the neural networks can be considered as powerful tools to explore nuclear properties alongside the theoretical models31. The ground-state energies $^ { 2 3 }$ and charge radii $^ { 2 2 }$ of nuclei were also investigated using artificial neural networks, and the usefulness of the method in the predictions was shown. Recently, various machine learning algorithms were used with the latest AME2016 data set to estimate the binding energies of atomic nuclei32. Besides, it was shown that the deep neural networks can predict the ground-state and excited energies as accurate as the nuclear energy density functional with less computational cost33. In recent years, neural network approaches were also used to train the mass residues of the theoretical models to improve the predictive power of the models and achieved considerable success $2 5 \mathrm { - } 2 8$ . As far as we are concerned, there is no work related to the application of the multilayer perceptron (MLP), which is a class of feedforward artificial neural network (ANN), to nuclear physics data. Therefore, it would be interesting to investigate the success of this model in the predictions of nuclear properties.

In this work, we implement the multilayer perceptron to predict the total binding en-

ergies (BE) of atomic nuclei. In our work, we first use the experimental data6 along with the proton (Z) and mass (A) numbers of the selected nuclei as inputs. Then, we study the effects of the increasing number of the hidden layers and inputs in the predictive power of the neural network. Finally, we compare our results with the other microscopic and microscopic-macroscopic models to evaluate the success of MLP in the binding energy predictions compared to the other models.

# II. MULTILAYER PERCEPTRON

In this study, we aim to create a model that makes ground-state binding energy predictions for atomic nuclei by using input data. Inputs are the nuclear properties that can affect the binding energies of nuclei. Our model takes these properties as input and predicts the binding energies as the output. Such problems, where the output is a numerical value, are known as the regression problems. Regression is a supervised learning problem where there is an input, $X$ , an output, $Y .$ , and the task is to learn the mapping from the input to the output34. To this end, in machine learning, we assume a model as shown below:

$$
y = f (x | \theta) \tag {1}
$$

where $f ( . )$ is the model and $\theta$ are its parameters. In our case, $y$ corresponds to the prediction for binding energy, and $f ( . )$ is the regression function. In the context of machine learning, the parameters, $\theta$ , are optimized by minimizing a loss function. Thus, the predictions are obtained as close as possible to the correct values given in the input data.

We choose multilayer perceptron (MLP) as the model $f ( . )$ . MLP is a neural network architecture that is mostly preferred to solve such regression problems. In the training stage of an MLP, the backpropagation algorithm $^ { 3 5 }$ is used for computing the gradient. On the other side, another algorithm is used to perform learning using this gradient24. The second algorithm is used for optimization, which is usually called as the optimizer. In recent years, a new type of algorithm, which is called the adaptive gradient method, is preferred as the optimizer. In this study, we use Adam algorithm $^ { 3 6 }$ to train the MLP.

Basically, an MLP is a feedforward neural network with one or more than one hidden layer between input and output layers. In the case of one hidden layer, first, input $x$ is fed to the input layer. By using an activation function, the activation propagates in the forward

direction, and the values of the hidden units $z$ are computed. Each hidden unit usually applies a nonlinear activation function to its weighted sum. After performing the forward pass, an error is computed by using a loss function. By using this error, the weights are updated in the backward pass35.

However, an MLP with one hidden layer has limited capacity, and using an MLP with multiple hidden layers can learn more complicated functions of the input. That is the idea behind deep neural networks where each hidden layer combines the values in its preceding layer and learns more complicated functions34. It is possible to have multiple hidden layers each with its own weights and applying the activation function to its weighted sum. It should be noted that different activation functions can be used in multilayer perceptrons, e.g., ReLU, tanh, sigmoid, etc. In this work, we implement both tanh and ReLU, which are two commonly used activation functions in nuclear mass predictions26,32,37,38, and find that the ReLU function gives better predictions on the test data. Therefore, we choose the ReLU function as the activation function of the hidden layers in this work, which is also mostly preferred for the hidden layers of deep neural networks39:

$$
\phi (x) = \max  (0, x) \tag {2}
$$

An MLP with three hidden layers is demonstrated in Fig. 1 where ${ \pmb w } _ { 1 h }$ , ${ \pmb w } _ { 2 l }$ and ${ \pmb w } _ { 3 k }$ are the weights belonging to the first, second and third hidden layers, respectively. The units on the first, second and third hidden layers are represented as $z _ { 1 h }$ , $z _ { 2 l }$ and $z _ { 3 k }$ , and $\mathbf { v }$ are the output layer weights. Such an architecture is required four stages to compute the output. Firstly, input $x$ is fed to the input layer, the weighted sum is computed, and the activation propagates in the forward direction. When the ReLU function is chosen as the activation function, $z _ { 1 h }$ is computed as shown below:

$$
\begin{array}{l} z _ {1 h} = R e L U (\mathbf {w} _ {1 h} ^ {T} \mathbf {x}) \\ = R e L U \left(\sum_ {j = 1} ^ {d} w _ {1 h j} x _ {j} + w _ {1 h 0}\right), h = 1, \dots , H _ {1} \tag {3} \\ \end{array}
$$

The computations for the second hidden layer are practiced similarly. At this stage, the second hidden layer activations are computed by taking the first hidden layer activations as their inputs. Then, the third hidden layer activations are computed by taking the second

![](images/5667af5fdaf71e0c5499716da24f3d487ea38caebe05b56d63fee7b9bb118535.jpg)  
FIG. 1. The structure of a multilayer perceptron with three hidden layers.

hidden layer activations as their inputs. In a regression problem, there is no nonlinearity in the output layer. Therefore, the output $y$ is computed by taking the $z _ { 3 }$ as input34. Thus, the forward propagation is completed:

$$
\begin{array}{l} z _ {2 l} = R e L U (\mathbf {w} _ {2 l} ^ {T} \mathbf {z} _ {1}) \\ = R e L U \left(\sum_ {h = 0} ^ {H _ {1}} w _ {2 l h} z _ {1 h} + w _ {2 l 0}\right), l = 1, \dots , H _ {2} \tag {4} \\ \end{array}
$$

$$
\begin{array}{l} z _ {3 k} = R e L U \left(\mathbf {w} _ {3 k} ^ {T} \mathbf {z} _ {2}\right) \\ = R e L U \left(\sum_ {l = 0} ^ {H _ {2}} w _ {3 k l} z _ {2 l} + w _ {3 k 0}\right), k = 1, \dots , H _ {3} \tag {5} \\ \end{array}
$$

$$
y = \mathbf {v} ^ {T} \mathbf {z} _ {3} = \sum_ {k = 1} ^ {H _ {3}} v _ {k} z _ {3 k} + v _ {0} \tag {6}
$$

When the MLP goes deeper, one more step is added to these computations for each one of additional hidden layer. In this study, we implement MLP architectures of two different depths. Whereas the first one includes three hidden layers, the other one includes four. Thus, we observe the effect of depth on the binding energy predictions. As we predict the binding energy, i.e. one single numerical value, only one unit exists in the output layer. In order to determine the MLP architecture, we gradually increase the number of hidden units according to the prediction performance on three data sets. Then, we choose our

final architectures. The MLP with three hidden layers includes 32,16 and 8 hidden units, respectively. It includes 769 (833) parameters for the MLP model with two (four) inputs, which is much smaller than the number of training data. On the other side, the MLP with four hidden layers includes 32,32,16 and 8 hidden units. It includes 1825 (1889) parameters for the MLP model with two (four) inputs. In addition to the smaller number of parameters, our architectures does not overfit because of two main reasons: Firstly, the central challenge in machine learning is that we must perform well on new, previously unseen inputs – not just those on which our model is trained24. As it is seen in our results below, our neural network can make good predictions on test data. Secondly, overfitting occurs when the gap between the training loss and test loss is too large24. However, in our calculations, the gap between the training loss and test loss is too small. For instance, it is found as 0.0023 (0.0029) for the training (test) data of MLP architecture with four hidden layers using four inputs. Therefore, it is seen that our neural network does not overfit, and it generalizes well on test data of each dataset, and the losses of training and test data are so close to each other.

Another important step of creating these architectures is to initialize the layer weights. We initialize them with the Glorot normal initializer, also known as Xavier normal initializer40. Besides, the input data is randomly divided into two subsets as 70.0% for training and 30.0% for testing. We prefer mean absolute error as the loss function on the training set $X$ :

$$
E (\mathbf {W}, \mathbf {v} | X) = \frac {\sum_ {t = 1} ^ {n} \left| r ^ {t} - f (x ^ {t}) \right|}{n} \tag {7}
$$

where $r ^ { t }$ are the desired values and $f ( x ^ { t } )$ are predictions for the binding energy.

We train our MLP architectures 800 epochs by using Adam optimization algorithm to minimize mean absolute error. The name Adam is derived from adaptive moment estimation. It is an adaptive gradient method that individually adapts the learning rates of model parameters36. During training, this algorithm computes the estimates of first and second moments of the gradients, and uses decay constants to update them. Therefore, Adam algorithm requires hyperparameters called decay constants in addition to the learning rate. In this study, the initial learning rate is 0.001, and decay constants are 0.9 and 0.999, respectively.

# III. RESULTS

In this work, the multilayer perceptron is used to predict ground-state binding energies of atomic nuclei. Two different MLP architectures and inputs are used to test the effect of the number of the hidden layers and inputs on the results. In the input channels, we first use proton (Z) and mass (A) numbers of nuclei as inputs along with the experimental data from the latest AME2016 mass table $_ 6$ to predict binding energies. Therefore, this part of the present work does not include any physical identity or theory, except the proton and mass numbers. In the second part, we also include additional physical inputs to improve the predictive power of our models. These inputs carry information about the shell structure of nuclei, which in turn related to nuclear binding energies41,42. One of them is the pairing term $\delta ( Z , N )$ , which is defined as

$$
\delta (Z, N) = \left[ (- 1) ^ {Z} + (- 1) ^ {N} \right] / 2. \tag {8}
$$

The pairing term becomes $+ 1$ (−1) for even-even (odd-odd) nuclei, and 0 for other nuclei. A positive value for the pairing term indicates that the nucleus is more bound while the opposite behavior is valid for a negative value42. Another input is the promiscuity factor (P) of nuclei $^ { 4 1 }$ and it is given by

$$
P = \nu_ {p} \nu_ {n} / (\nu_ {p} + \nu_ {n}), \tag {9}
$$

where $\nu _ { p ( n ) }$ is the difference between the actual proton (neutron) number and the nearest magic number. The promiscuity factor is defined as a measure of the valance proton-neutron $( p - n )$ interactions41. In this work, the proton and neutron magic numbers are taken as Z=8, 20, 28, 50, 82, 126 and N=8, 20, 28, 50, 82, 126, 184, respectively. The latest AME2016 mass table provides data for 3413 nuclei for A≥8. However, only 2479 of them are obtained experimentally, and the others are calculated using the trend from the mass surface (TMS) in the neighborhood. Although the properties of some nuclei are not obtained directly from experiments, they are expected to provide reasonable data and trends for unknown nuclei. As it is well-known, having a large amount of data is crucial for training an artificial neural network. Using a large collection of data, performance of an algorithm can be improved significantly. In our model, we make predictions by using only proton and mass numbers of nuclei alongside some shell effects in the input. Since we do not provide much information

![](images/56e705047db9f7ed33d26f01a75b4c3b225c93175db0499a0ea0bb43f297a9a6.jpg)

![](images/dc8c906dde79d332764fea47db89469f1f1e32cb7c6471a5ab0fd2e6852cb635.jpg)  
FIG. 2. Comparison of the experimental and predicted binding energy differences for the testing set of the three layers MLP architecture using (Z, A) (upper figure) and (Z, A, $\delta$ , P) (lower figure) as inputs.

![](images/d0c85f342ed9b6cf8677b6096e0b0644b31502319d723d09c5c48c09270558b8.jpg)

![](images/413dec3b64d3a0abcb08db371deeafd80b8d0db0686c7cc8980e0bd5695066cf.jpg)  
FIG. 3. The same as in Fig. 2, but for the four layers MLP architecture.

to the model in the input channel, we need a large amount of data to make reasonable

predictions. Therefore, non-experimental values from the AME2016 mass table are also used in the calculations to increase the performance of the model. While training the model, light nuclei with N<8 and A $<$ <10 is not taken into account and we randomly divide our data set (3388 nuclei in total) into training (70.0%) and testing sets (30.0%), as usual.

In Figs. 2 and 3, we display the binding energy (BE) differences between the experimental data and the results from the MLP model using two different architectures and inputs. The first architecture has three hidden layers (32-16-8), and we only use the proton and mass numbers of nuclei (Z, A) in the input channel (see Fig. 2(a)). Then, we also add pairing and promiscuity factors (Z, A, $\delta$ , P) to see their effects on the results (see Fig. 2(b)).

The predictions of the MLP with the three hidden layers are given in Fig. 2 for 1017 nuclei in the testing set. Although the root-mean-square deviation $( \sigma _ { r m s } )$ ) with respect to the experimental data is high and obtained as $\sigma _ { r m s } = 3 . 9 8$ MeV, the MLP can make reasonable predictions for the nuclear binding energies using only (Z, A) as inputs, and the results are comparable with the predictions of the nuclear energy density functionals. First thing to notice is the large deviation of the model results for light and heavy nuclei, which can be related to the limited number of experimental data in these regions. Adding more physical information to the input, we find that the predictive power of the MLP increases considerably as can be seen from Fig.2(b). By adding pairing and promiscuity factors to the input channel, the root-mean-square deviation is improved by about 45.73% and obtained as 2.16 MeV for the testing set nuclei. It is also clear that the predictive power of the MLP increases considerably for light and heavy nuclei. To see the performance of the MLP in different regions of the nuclear landscape, we divide the testing set into three parts as light nuclei (Z<20, 93 nuclei), medium-heavy nuclei (20 $\leq$ Z $\leq$ 82, 696 nuclei), and super-heavy nuclei (Z $\geq$ 82, 228 nuclei). Using (Z, A) as inputs, the $\sigma _ { r m s }$ values are obtained as 8.60, 2.93, and 3.80 MeV for light, medium-heavy and super-heavy nuclei, respectively. Increasing the number of the inputs in the MLP architecture, namely using (Z, A, $\delta$ , P) in the input channel, we obtain important improvements in the $\sigma _ { r m s }$ values (see Table I). For instance, the $\sigma _ { r m s }$ value for light nuclei is decreased and found as 3.39 MeV, which corresponds to 60.58% improvement in the predictions. Besides, the $\sigma _ { r m s }$ value for medium-heavy and super-heavy nuclei is decreased and obtained as 2.10 and 1.61 MeV, respectively. Using MLP with four inputs, the model predictions are improved by about 28.32% and 57.63% for medium-heavy and super-heavy nuclei, respectively.

TABLE I. The root-mean square deviations ( $\sigma _ { r m s }$ ) in units of MeV for different MLP architectures and inputs. The results of the best MLP architectures are shown in bold. Since the number of the parameters are higher than the number of the training data set, the results of the two hidden layers (64-64) MLP architecture are not presented.

<table><tr><td rowspan="2">MLP</td><td rowspan="2">Input</td><td>Z&lt;20</td><td>20 ≤ Z≤ 82</td><td>Z&gt;82</td><td>Testing set</td></tr><tr><td>93 nuclei</td><td>696 nuclei</td><td>228 nuclei</td><td>1017 nuclei</td></tr><tr><td>(32-32)</td><td>(A,Z)</td><td>7.80</td><td>2.80</td><td>2.11</td><td>3.46</td></tr><tr><td>(64-32)</td><td>(A,Z)</td><td>2.93</td><td>2.35</td><td>4.50</td><td>3.01</td></tr><tr><td>(32-32)</td><td>(A,Z,δ,P)</td><td>4.13</td><td>1.95</td><td>4.76</td><td>3.04</td></tr><tr><td>(64-32)</td><td>(A,Z,δ,P)</td><td>5.00</td><td>1.88</td><td>3.07</td><td>2.61</td></tr><tr><td>(32-16-8)</td><td>(A,Z)</td><td>8.60</td><td>2.93</td><td>3.80</td><td>3.98</td></tr><tr><td>(64-8-4)</td><td>(A,Z)</td><td>6.42</td><td>4.07</td><td>4.83</td><td>4.51</td></tr><tr><td>(64-16-8)</td><td>(A,Z)</td><td>6.22</td><td>2.11</td><td>2.05</td><td>2.75</td></tr><tr><td>(32-16-8)</td><td>(A,Z,δ,P)</td><td>3.39</td><td>2.10</td><td>1.61</td><td>2.16</td></tr><tr><td>(64-8-4)</td><td>(A,Z,δ,P)</td><td>6.75</td><td>2.93</td><td>4.76</td><td>3.90</td></tr><tr><td>(64-16-8)</td><td>(A,Z,δ,P)</td><td>4.60</td><td>1.89</td><td>2.47</td><td>2.40</td></tr><tr><td>(32-16-8-4)</td><td>(A,Z)</td><td>10.37</td><td>3.01</td><td>2.60</td><td>4.20</td></tr><tr><td>(32-16-16-8)</td><td>(A,Z)</td><td>1.98</td><td>2.73</td><td>2.37</td><td>2.60</td></tr><tr><td>(32-32-16-8)</td><td>(A,Z)</td><td>4.89</td><td>3.06</td><td>4.82</td><td>3.72</td></tr><tr><td>(32-16-8-4)</td><td>(A,Z,δ,P)</td><td>5.03</td><td>3.22</td><td>3.24</td><td>3.43</td></tr><tr><td>(32-16-16-8)</td><td>(A,Z,δ,P)</td><td>9.11</td><td>2.83</td><td>2.27</td><td>3.78</td></tr><tr><td>(32-32-16-8)</td><td>(A,Z,δ,P)</td><td>3.03</td><td>1.58</td><td>1.94</td><td>1.84</td></tr><tr><td>(32-16-8-8-8)</td><td>(A,Z)</td><td>4.20</td><td>2.56</td><td>5.25</td><td>3.50</td></tr><tr><td>(32-16-16-8-4)</td><td>(A,Z)</td><td>4.21</td><td>2.83</td><td>4.88</td><td>3.52</td></tr><tr><td>(64-32-16-16-8)</td><td>(A,Z)</td><td>2.87</td><td>2.46</td><td>5.55</td><td>3.44</td></tr><tr><td>(32-16-8-8-8)</td><td>(A,Z,δ,P)</td><td>5.56</td><td>2.17</td><td>1.35</td><td>2.54</td></tr><tr><td>(32-16-16-8-4)</td><td>(A,Z,δ,P)</td><td>10.83</td><td>2.98</td><td>1.78</td><td>4.18</td></tr><tr><td>(64-32-16-16-8)</td><td>(A,Z,δ,P)</td><td>3.83</td><td>7.47</td><td>2.47</td><td>4.92</td></tr></table>

![](images/063d74457015ed09710315ca89dc5b3093c6dff0639fed778edabe9cb38949c9.jpg)

![](images/4901ef1553fbaf2d34f969a1443d72229b5129493581e198153562251d599069.jpg)

![](images/da3724b3cab9be355f11c79670dec4c9845aa26b299e48f9f76cde56a5eddc2d.jpg)

![](images/28b09c8c7d62eabd56411e2b7e423957050e5d43d938e4785e46e6840f8132da.jpg)  
FIG. 4. Comparison of the experimental and predicted binding energy differences for 956 nuclei between the MLP with three hidden layers and (a) UNEDF113,43,44, SKM $^ { * 1 3 , 4 4 , 4 5 }$ , (c) FRDM-20129 and (d) WS3 $^ { 8 }$ models. The black dashed lines are given to guide the eye.

It is known that increasing or decreasing the number of hidden layers can also affect the predictive power of the neural networks. Therefore, we also increase the number of the hidden layers to four in the MLP architecture and the same calculations are repeated to see its effect on the results. In Fig. 3, the binding energy differences between the experimental data and MLP predictions with three hidden layers are displayed for 1017 nuclei in the testing set. By increasing the number of the hidden layer by one unit, the predictive power of the MLP model increases, and the $\sigma _ { r m s }$ values are obtained as 3.72 and 1.84 MeV with two (see Fig.3(a)) and four inputs (see Fig.3(b)), respectively. Similar to the MLP with the three hidden layers, the largest deviations in the binding energies are obtained for light and super-heavy nuclei, and inclusion of the additional inputs increases the success of the model in these regions. Using MLP with four hidden layers and two inputs (Z, A), the $\sigma _ { r m s }$ deviations are obtained as 4.89, 3.06, and 4.82 MeV for light, medium-heavy, and super-

![](images/7971562770f5a42425babd64e8771941a7153ff6879c55d059ba6f43713ca420.jpg)

![](images/0a32624d1d310f6c87273f9a3c0c737279830e3034b1f57da7b794c4873b98d2.jpg)

![](images/87dbe247847e1d1863ffd50343957a30d8a7246729584c62874a913ef1af360c.jpg)

![](images/b27e83247f3f91bafcbb1c5384d65686bd482047875bdf5336e8436334bc6f2e.jpg)  
FIG. 5. The same as in Fig. 4, but using the four layers MLP architecture.

heavy nuclei, respectively. Adding the pairing and promiscuity factors to the input channels, the results are improved by about 38.03%, 48.37%, and 59.75% and the $\sigma _ { r m s }$ deviation values are obtained as 3.03, 1.58, and 1.94 MeV for light, medium-heavy and super-heavy nuclei (see Table I), respectively.

We should mention that different MLP architectures with different number of hidden layers or hidden units are also tested to make nuclear mass predictions, and obtain the best MPL model. The results of these works are also given in Table I. We found that decreasing the number of the hidden layers also decrease the predictive power of the results. On the other hand, increasing the number of the hidden layers more than four also does not give better results. In this work, the best results are obtained using the three (32-16-8) and four (32-32-16-8) layers MLP architectures with four inputs. Our results indicate that using the proper number of hidden layers and inputs in the MLP architecture, we can make fast and reliable predictions for nuclear properties. Since the predictions are better using the (Z, A, $\delta$ , P) as inputs, we always use the results with four inputs to compare with other mic-mac

TABLE II. The root-mean square deviations ( $\sigma _ { r m s }$ ) in units of MeV for the common 956 nuclei using various models. In here, MLP $^ { - 1 }$ and MLP2 represent three layers (32-16-8) and four layers (32- 32-16-8) MLP architectures using (Z, A, $\delta$ , P) in the input channel. The nuclear bindings energy results are taken from the nuclear energy density functionals UNEDF1 $^ \mathrm { 1 3 , 4 3 , 4 4 }$ and SkM $^ { * 1 3 , 4 4 , 4 5 }$ . The results of the FRDM-2012 and WS3 models are taken from Refs.8,9.

<table><tr><td></td><td>MLP1</td><td>MLP2</td><td>UNEDF1</td><td>SKM*</td><td>FRDM-2012</td><td>WS3</td></tr><tr><td>σrms</td><td>1.97</td><td>1.72</td><td>2.13</td><td>7.81</td><td>0.99</td><td>0.55</td></tr></table>

and microscopic results in the rest of the paper.

In figures 4 and 5, we also display the binding energy differences between experimental data and modeling results from the MLP architectures with three and four hidden layers and using four (Z, A, $\delta$ , P) inputs. Both mic-mac (FRDM- $2 0 1 2 ^ { 9 }$ and WS38) and microscopic (UNEDF113,43,44 and SkM*13,44,45) results from theoretical database Explorer $^ { 4 4 }$ are shown along with the MLP predictions for comparison. It is known that the accuracy of the selfconsistent models is not high for the nuclear mass predictions and the root-mean-square deviations are obtained at about several MeV. On the other side, the mic-mac models (FRDM-2012 and WS3) are not self-consistent, and their parameter constants are fitted using the available experimental data, which in turn provide better estimations for the nuclear binding energies as can be seen from Figs. 4 and 5. The first thing to notice is that the binding energy differences are generally high for light and heavy nuclei in all model predictions. Compared to the UNEDF1, the deviation of the SkM $^ *$ results from the experimental data is quite high, and increases with the increase in mass number. For micmac models (FRDM-2012 and WS3), the highest deviations are obtained for nuclei with A $\geq$ 250. Comparing the results of MLP architectures with three and four layers (see figs. 4 and 5), it is clear that four layers MLP results are better than the three layers MLP. Besides, both MLP architectures are as successful as the FRDM-2012 and WS3 models in the description of nuclei with A $\geq$ 250. Although we only use the proton-mass numbers alongside pairing and promiscuity factors of nuclei as physical inputs in the training of the MLP, the model gives promising results that they are comparable to other microscopic and mic-mac models.

In Table II, the root-mean-square deviations $\sigma _ { r m s }$ ) are also given for each model to get a

better insight into the success of the models. The best results are obtained for FRDM-2012 and WS3 models, and rms deviations are obtained below 1.0 MeV. While the rms deviation is rather high using the SkM $^ *$ functional and obtained as 7.81 MeV, the UNEDF1 functional makes better predictions and rms deviation is obtained as 2.13 MeV. The root-mean-square deviations are still high using the self-consistent microscopic models in the calculations. Besides, calculations using nuclear energy density functionals are still computationally demanding. It is seen that the MLP model can make reliable predictions that are comparable to the well-known microscopic models, and the $\sigma _ { r m s }$ values are obtained as 1.97 and 1.72 MeV with three and four layers MLP architectures.

# IV. CONCLUSIONS

We implement the multilayer perceptron (MLP) to make ground-state binding energy predictions for atomic nuclei. Two different architectures and inputs are used in the MLP model to study the performance of this neural network in the binding energy predictions. In the first one, we only use the proton and mass numbers of nuclei alongside with the latest experimental data, and no physical input is included. Then, we also added two additional inputs: pairing and promiscuity factors of nuclei to give more physical information to the models. We find that using proper hidden layers and units with relevant information in the input channels, the nuclear binding energy predictions using the MLP improve considerably, especially for light and medium-heavy nuclei. For 1017 nuclei in the testing set, the best root-mean-square deviations are obtained as 2.16 MeV and 1.84 MeV for three and four layers MLP architectures using (Z, A, $\delta$ , P) inputs, respectively.

Our findings show that the MLP model can make reasonable predictions for binding energies of atomic nuclei and the results are also comparable to other models. Although the MLP does not include any physics theory behind it and considered as a statistical model, it is seen that the model can make fast and reliable predictions with a proper architecture and relevant inputs. In this respect, the artificial neural networks can be seen as an alternative tool to other mic-mac and microscopic models.

As future work, we plan to extend our calculations by including more physical quantities in the input to better estimate the nuclear properties. Improving the extrapolation abilities of the neural networks for very neutron-rich nuclei is also another challenging task and

remains as a future work. Besides, the neural network approaches can be used to train the residues of nuclear properties as it is done in Refs.25–28, which in turn can be helpful to understand the missing physics behind the microscopic models.

# REFERENCES

$^ { 1 }$ D. Lunney, J. M. Pearson, and C. Thibault, “Recent trends in the determination of nuclear masses,” Rev. Mod. Phys. 75, 1021–1082 (2003).   
$^ 2$ M. R. Mumpower, R. Surman, D.-L. Fang, M. Beard, P. M¨oller, T. Kawano, and A. Aprahamian, “Impact of individual nuclear masses on $r$ -process abundances,” Phys. Rev. C 92, 035807 (2015).   
$^ 3$ M. Mumpower, R. Surman, D. L. Fang, M. Beard, and A. Aprahamian, “The impact of uncertain nuclear masses near closed shells on ther-process abundance pattern,” Journal of Physics G: Nuclear and Particle Physics 42, 034027 (2015).   
$^ 4$ H. Schatz and W.-J. Ong, “Dependence of x-ray burst models on nuclear masses,” The Astrophysical Journal 844, 139 (2017).   
$^ { 5 }$ D. Martin, A. Arcones, W. Nazarewicz, and E. Olsen, “Impact of nuclear mass uncertainties on the $r$ process,” Phys. Rev. Lett. 116, 121101 (2016).   
$_ 6$ M. Wang, G. Audi, F. G. Kondev, W. Huang, S. Naimi, and X. Xu, “The AME2016 atomic mass evaluation (II). tables, graphs and references,” Chinese Physics C 41, 030003 (2017).   
7N. Wang, Z. Liang, M. Liu, and X. Wu, “Mirror nuclei constraint in nuclear mass formula,” Phys. Rev. C 82, 044304 (2010).   
$^ 8$ M. Liu, N. Wang, Y. Deng, and X. Wu, “Further improvements on a global nuclear mass model,” Phys. Rev. C 84, 014333 (2011).   
$^ { 9 }$ P. M¨oller, W. D. Myers, H. Sagawa, and S. Yoshida, “New finite-range droplet mass model and equation-of-state parameters,” Phys. Rev. Lett. 108, 052501 (2012).   
$_ { 1 0 }$ S. Goriely, N. Chamel, and J. M. Pearson, “Skyrme-hartree-fock-bogoliubov nuclear mass formulas: Crossing the 0.6 mev accuracy threshold with microscopically deduced pairing,” Phys. Rev. Lett. 102, 152503 (2009).   
$_ { 1 1 }$ S. Goriely, S. Hilaire, M. Girod, and S. P´eru, “First gogny-hartree-fock-bogoliubov nuclear mass model,” Phys. Rev. Lett. 102, 242501 (2009).

$^ { 1 2 }$ M. Stoitsov, J. Dobaczewski, W. Nazarewicz, and P. Borycki, “Large-scale self-consistent nuclear mass calculations,” International Journal of Mass Spectrometry 251, 243 – 251 (2006).   
$^ { 1 3 }$ J. Erler, N. Birge, M. Kortelainen, W. Nazarewicz, E. Olsen, A. Perhac, and M. Stoitsov, “The limits of the nuclear landscape,” Nature 486, 509–512 (2012).   
$^ { 1 4 }$ A. V. Afanasjev and S. E. Agbemava, “Covariant energy density functionals: Nuclear matter constraints and global ground state properties,” Phys. Rev. C 93, 054310 (2016).   
$^ { 1 5 }$ S. E. Agbemava, A. V. Afanasjev, D. Ray, and P. Ring, “Global performance of covariant energy density functionals: Ground state observables of even-even nuclei and the estimate of theoretical uncertainties,” Phys. Rev. C 89, 054320 (2014).   
$^ { 1 6 }$ G. Audi, A. Wapstra, and C. Thibault, “The ame2003 atomic mass evaluation: (ii). tables, graphs and references,” Nuclear Physics A 729, 337 – 676 (2003), the 2003 NUBASE and Atomic Mass Evaluations.   
$^ { 1 7 }$ S. Goriely, F. Tondeur, and J. Pearson, “A hartree–fock nuclear mass table,” Atomic Data and Nuclear Data Tables 77, 311 – 381 (2001).   
$^ { 1 8 }$ G. Audi and A. Wapstra, “The 1995 update to the atomic mass evaluation,” Nuclear Physics A 595, 409 – 480 (1995).   
$^ { 1 9 }$ S. Goriely, N. Chamel, and J. M. Pearson, “Further explorations of skyrme-hartree-fockbogoliubov mass formulas. xvi. inclusion of self-energy effects in pairing,” Phys. Rev. C 93, 034337 (2016).   
$^ { 2 0 }$ L. Geng, H. Toki, and J. Meng, “Masses, Deformations and Charge Radii—Nuclear Ground-State Properties in the Relativistic Mean Field Model,” Progress of Theoretical Physics 113, 785–800 (2005).   
$^ { 2 1 }$ X. Xia, Y. Lim, P. Zhao, H. Liang, X. Qu, Y. Chen, H. Liu, L. Zhang, S. Zhang, Y. Kim, and J. Meng, “The limits of the nuclear landscape explored by the relativistic continuum hartree–bogoliubov theory,” Atomic Data and Nuclear Data Tables 121-122, 1 – 215 (2018).   
$^ { 2 2 }$ S. Akkoyun, T. Bayram, S. O. Kara, and A. Sinan, “An artificial neural network application on nuclear charge radii,” Journal of Physics G: Nuclear and Particle Physics 40, 055106 (2013).   
$^ { 2 3 }$ T. Bayram, S. Akkoyun, and S. O. Kara, “A study on ground-state energies of nuclei by using neural networks,” Annals of Nuclear Energy 63, 172 – 175 (2014).

$^ { 2 4 }$ I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning (MIT Press, 2016).   
$^ { 2 5 }$ R. Utama and J. Piekarewicz, “Refining mass formulas for astrophysical applications: A bayesian neural network approach,” Phys. Rev. C 96, 044308 (2017).   
$^ { 2 6 }$ Z. Niu and H. Liang, “Nuclear mass predictions based on bayesian neural network approach with pairing and shell effects,” Physics Letters B 778, 48 – 53 (2018).   
$^ { 2 7 }$ L. Neufcourt, Y. Cao, W. Nazarewicz, and F. Viens, “Bayesian approach to model-based extrapolation of nuclear observables,” Phys. Rev. C 98, 034318 (2018).   
$^ { 2 8 }$ L. Neufcourt, Y. Cao, W. Nazarewicz, E. Olsen, and F. Viens, “Neutron drip line in the ca region from bayesian model averaging,” Phys. Rev. Lett. 122, 062502 (2019).   
$^ { 2 9 }$ K. Gernoth, J. Clark, J. Prater, and H. Bohr, “Neural network models of nuclear systematics,” Physics Letters B 300, 1 – 7 (1993).   
$^ { 3 0 }$ S. Gazula, J. Clark, and H. Bohr, “Learning and prediction of nuclear stability by neural networks,” Nuclear Physics A 540, 1 – 26 (1992).   
$^ { 3 1 }$ S. Athanassopoulos, E. Mavrommatis, K. Gernoth, and J. Clark, “Nuclear mass systematics using neural networks,” Nuclear Physics A 743, 222 – 235 (2004).   
$^ { 3 2 }$ M. U. Anil, T. Malik, and K. Banerjee, “Nuclear binding energy predictions based on machine learning,” ArXiv:2004.14196 (2020).   
$^ { 3 3 }$ R.-D. Lasseri, D. Regnier, J.-P. Ebran, and A. Penon, “Taming nuclear complexity with a committee of multilayer neural networks,” Phys. Rev. Lett. 124, 162502 (2020).   
$^ { 3 4 }$ E. Alpaydın, Introduction to Machine Learning (MIT Press, 2014).   
$^ { 3 5 }$ D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning representations by backpropagating errors,” Nature 323, 533–536 (1986).   
$^ { 3 6 }$ D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” preprint ArXiv:1412.6980 (2014).   
$^ { 3 7 }$ A. Idinil, “Statistical learnability of nuclear masses,” arXiv:1904.00057 (2019).   
$^ { 3 8 }$ H. F. Zhang, L. H. Wang, J. P. Yin, P. H. Chen, and H. F. Zhang, “Performance of the levenberg–marquardt neural network approach in nuclear mass prediction,” Journal of Physics G: Nuclear and Particle Physics 44, 045110 (2017).   
$^ { 3 9 }$ X. Glorot, A. Bordes, and Y. Bengio, “Deep sparse rectifier neural networks,” 14th International Conference on Artificial Intelligence and Statistics , 315–323 (2011).   
$^ { 4 0 }$ X. Glorot and Y. Bengio, “Understanding the difficulty of training deep feedforward neural networks,” Proceedings of the thirteenth international conference on artificial intelligence

and statistics , 249–256 (2010).   
$^ { 4 1 }$ R. F. Casten and N. V. Zamfir, “The evolution of nuclear structure: the scheme and related correlations,” Journal of Physics G: Nuclear and Particle Physics 22, 1521–1552 (1996).   
$^ { 4 2 }$ M. W. Kirson, “Mutual influence of terms in a semi-empirical mass formula,” Nuclear Physics A 798, 29 – 60 (2008).   
$^ { 4 3 }$ M. Kortelainen, J. McDonnell, W. Nazarewicz, P.-G. Reinhard, J. Sarich, N. Schunck, M. V. Stoitsov, and S. M. Wild, “Nuclear energy density optimization: Large deformations,” Phys. Rev. C 85, 024304 (2012).   
$^ { 4 4 }$ “Mass explorer, http://massexplorer.frib.msu.edu/content/dftmasstables.html,” (2020).   
$^ { 4 5 }$ J. Bartel, P. Quentin, M. Brack, C. Guet, and H.-B. H˚akansson, “Towards a better parametrisation of skyrme-like effective forces: A critical study of the skm force,” Nuclear Physics A 386, 79 – 100 (1982).