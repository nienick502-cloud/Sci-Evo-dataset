# Deep learning on nuclear mass and $\alpha$ decay half-lives

Chen-Qi Li∗

Key Laboratory of Quark & Lepton Physics (MOE) and Institute of Particle Physics,

Central China Normal University, Wuhan 430079, China and

Physics Department, University of California, Berkeley, CA 94720, USA

Chao-Nan Tong, Hong-Jing Du, and Long-Gang Pang†

Key Laboratory of Quark & Lepton Physics (MOE) and Institute of Particle Physics,

Central China Normal University, Wuhan 430079, China

Ab-initio calculations of nuclear masses, the binding energy and the $\alpha$ decay half-lives are intractable for heavy nucleus, because of the curse of dimensionality in many body quantum simulations as proton number(N) and neutron number(Z) grow. We take advantage of the powerful non-linear transformation and feature representation ability of deep neural network(DNN) to predict the nuclear masses and $\alpha$ decay half-lives. For nuclear binding energy prediction problem we achieve standard deviation $\sigma = 0 . 2 6 3$ MeV on 10-fold cross validation on 2149 nuclei. Word-vectors which are high dimensional representation of nuclei from the hidden layers of mass-regression DNN help us to calculate $\alpha$ decay half-lives. For this task, we get $\sigma = 0 . 7 9 7$ on 100 times 10-fold cross validation on 350 nuclei on $l o g _ { 1 0 } T _ { 1 / 2 }$ and $\sigma = 0 . 7 3 1$ on 486 nuclei. DNN is also used to reduce the residual of three-parameter Gamow formula on 159 even-even nuclei, from 0.3627 to 0.2297 on $l o g _ { 1 0 } T _ { 1 / 2 }$ , using 100 times 10-fold cross validation. We find physical a priori such as shell structure, magic numbers and augmented inputs inspired by Finite Range Droplet Model are important for this small data regression task.

# I. INTRODUCTION

Ground state nuclear mass(binding energy), $\alpha$ decay half-life, $\beta$ decay half-life are all important properties of the nucleus [1, 2]. Accurately calculating and predicting these quantities are crucial for justifying ab-initio quantum many body calculations as well as phenomenology models, such as liquid droplet model and shell

model. Understanding the creation of heavy elements in our universe by the rapid neutroncapture process or r-process require accurate nuclear mass predictions in nuclear astrophysics[3, 4]. These quantities also play important roles in nuclear stability studies which may guide us to find more super-heavy nuclei and even the ”super-heavy island”.

Machine learning is a collection of algorithms that let the computer learn patterns from big data by themselves. The learned pat-

terns are widely used in classification and regression tasks to get the state-of-the-art performance in many scientific problems. Various machine learning methods have been used in nuclear physics for regression tasks. E.g., Bayesian Neural Network[5–8](BNN), Radial Basis Function (RBF), Light Gradient Boosting Machine[9] (LightGBM) and many other methods [10, 11] have been applied to predict the residual between true nuclear mass and phenomenology models, such as finite-range droplet model (FRDM) [12], Weizs¨acker-Skyrme (WS) mass model[13, 14] and Skyrme HartreeFock-Bogoliubov (HFB) model[15, 16]. These machine learning methods have improved both accuracy and extrapolation ability greatly[17, 18]. The mass predicted using Machine Learning algorithm is used to construct the outer crust equation of state (EoS) of a neutron star which is comparable to existing models [19].

Deep neural network (DNN) with multiple hidden layers is the most popular machine learning tool, which has outperformed many traditional ways and advances many scientific researches to the state-of-the-art. Read [20, 21] for more detailed review on its applications in nuclear physics. Deep neural network is proved to have universal approximation ability with at least one hidden layer. It has long been used to predict the ground state mass of nuclei [22–25]. However, even with the rapid development in recent years, the performance of deep neural network on ground state nuclear mass are still much

worse than other methods, as shown in many recent researches . E.g., the rms deviation is above 1 MeV using a 4-layer neural network [26] recently. As a comparison, the rms deviation from improved WS model is 0.336 MeV [14]. The best performance from a decision tree based method LightGBM has rms deviation around 0.170 MeV [9]. We believe that the feed forward neural network used in recent studies are not deep and wide enough to reach its best performance. After performing a simple neural architecture search (NAS), we achieve rms deviation 0.263 Mev in 10-fold cross validation.

The performance of deep neural network highly depends on the amount of data, however, there are only about 2500 existing experiment data till 2020[27] for nuclear mass regression, and less than 500 available experiment data for $\alpha$ decay half-life regression. One important question is whether a deep neural network can learn from this tiny data without terrible over-fitting. Will the patterns learned in mass prediction help the $\alpha$ decay half-life prediction?

One method is to train the same network to achieve multiple tasks, which is called multi-task learning (MTL). In this way, different tasks have shared module in the network as well as their own modules. MTL optimizes the shared parameter with limited data for each task. MTL has been used to describe the giant dipole resonance key parameters [28].

Another method is called representation learning. We use the latent representations of

each nucleus learned in the nuclear mass prediction task to assist the $\alpha$ decay half-life prediction. The latent representation is similar to word-vector in natural language processing tasks where each word is represented by a high dimensional vector with 256 or 512 floating numbers, to represent individual words in a text, taking into account the context and other surrounding words learned by the deep neural network in other big-data problems. Using a 256 dimensional word vector got from the previous nuclear mass prediction task as a new representation of a nucleus, we predict the $\alpha$ decay half-life and verify that the word-vector really improve its performance.

The paper is organized as follows: In sec.II we introduce the network structure, the input data structure and the prediction accuracy of nuclear binding energy. In sec.III and section .IV we introduce the method of nuclear-representation and its application in predicting the $\alpha$ decay half-lives. The discussion and summary will be given in V and VI.

# II. NUCLEAR BINDING ENERGY PREDICTION

# A. Methods

The nuclear binding energy prediction is a supervised regression problem. The objective is to minimize the the residual which is defined as the difference between experimental data and semiempirical models. Two semi-empirical models

are used, one is Bethe-Weizs¨acker model (BWM) and the other is Liquid-Dropplet Model (LDM). Both models have root-mean-square error larger than 2 MeV.

Two types of inputs are used. The first type consists of 3 native features $Z , N , A$ for each nucleus. The second type has 26 features(see appendix) with physical a prior as shown below. The neural network has one adjustable architecture whose number of layers are $n + 2$ and neurons per hidden layer equal to $m$ or $4 \times m$ .

Data flow in the feed forward neural network according to the following equation for adjacent layers,

$$
h _ {i} = \sigma \left(\sum_ {j} w _ {i j} x _ {j} + b _ {i}\right) \tag {1}
$$

where $h _ { i }$ represent the value of the $i$ -th neuron in the next layer, $x _ { j }$ represent values of the $j$ -th neuron in the previous layer. The network parameters are $w _ { i j } \mathrm { ( w e i g h t s ) }$ $w _ { i j }$ and $b _ { i }$ (bias), which are initialized with random numbers and are adjusted gradually during training using stochastic gradient descent algorithm. The feature vector in the previous layer are first linearly transformed through $z _ { i } = x _ { j } w _ { i j } + b _ { i }$ , and then feed to a non-linear activation function $h _ { i } = \sigma ( z _ { i } )$ . The operation corresponds to a manipulations of feature vector in high-dimensional space.

As shown in Fig 1, the input consists of 3 native features (Z, N, A) or 26 physics-informed features. In the output layer, there is one neuron representing the residual binding energy. In

![](images/8b93c0a22003fa1958ffd68968c6f66cdfef1b02999df39077976ce0406ddaa7.jpg)  
FIG. 1. The adjustable neural network structure with the number of hidden layers changed by $n$ and the width of hidden layers changed by $m$ . The output layer is the residual defined in Equation (2).

between, there are $n + 2$ hidden layers. The first and the last hidden layer have $4 \times m$ neurons and the other $n$ hidden layers have $m$ neurons per layer. The number $m$ is defined as the ”width” of the neural network. The performance of the network prediction is scanned using 10- fold cross validation, for $n = ( 0 , 2 , 4 , 6 , 8 , 1 0 , 1 6 )$ and $m = ( 8 , 6 4 , 2 5 6 , 5 1 2 )$ .

Other special method used in our DNN: between each layer, Batch-Normalization method[29] is adopted to accelerate learning as well as avoid vanishing gradient and exploding gradient.

# B. Performance scan and prediction accuracy

Shown in Fig 2 are the 10-fold average RMS error for different numbers of hidden layers and different numbers of neurons per hidden layer. Using 26 features in the input, the RMS error

![](images/e91fc22958661cd3dd1cdc83b9a0077d2122b2a6918c09b9794b394af01a905f.jpg)

![](images/beddd98007ffa64713e333c2d3b8f4a18c4600df580cdd5c957931d89d340a22.jpg)  
FIG. 2. (color online) The performance of the atomic mass prediction using 10-fold cross validation. The bands represent the range of root mean square error using different numbers of hidden layers and different numbers of neurons per layer in the architecture of the deep neural network. The optimal RMSE is around 0.22 MeV using 10 hidden layers with 1024 neurons in the first and the last hidden layer and 256 neurons for 8 other hidden layers, which correspond to width=256 in the plot.

decreases from 1.5 to 0.3 MeV as the width of the network increases from $m = 8$ to $m = 6 4$ . Increasing $m$ from 256 to 512 does not bring further improvement. On the other hand, the performance is not sensitive to the depth of the neural network. The RMS error changes slightly as one increases the number of hidden layers from 2 to 18. For $m = 2 5 6$ , the RMS error reaches its

minimum for 10 hidden layers (n=8).

The parameters of the neural network are initialized with random numbers and adjusted during the training process, as a result, the final performance relies on the starting point of optimization in the parameter space. At rare times, the parameter optimization starts at a position which produces worse results than general cases. This happens in the performance scan for a network with structure ( $n = 0 , m = 2 5 6$ ). Although it is a rare event, we do not retrain the network for cherry picking. It reminds us that repeating the training process many times is a good way to capture the uncertainty of the network on small data.

According to the performance scan, the optimal network structure is ( $n = 8 , m = 2 5 6$ ) for LDM mass residual. As shown in Fig 3, the average RMS error of 10-fold is approximately 263 keV for 26 features and 332 keV for 3 features. Using physical a priori as input, the RMS error reduces by 69 keV.

Shown in Fig 4 are comparisons between semi-empirical models and network predictions with 3 and 26 features. As the network is trained to predict the residual of semi-empirical model, the new prediction error is defined as,

$$
\text {R e s i d u a l} = M _ {\exp} - M _ {\mathrm {L D M}} - R _ {\text {N e t w o r k}} \tag {2}
$$

In this comparison, both training and testing data are included as what has been done in semiempirical models.

Shown in Fig 5 is the comparison between

![](images/46bfe38ad8938742dffd87698486513fc084b699071a1c760309127b74646d74.jpg)

![](images/733cebe44b4a7fdbd391a20086f3eea3faaf7d499a5aa79ac00b1d5a2d2f9d24.jpg)  
FIG. 3. (color online) The optimal performance of the atomic mass prediction using 10-fold cross validation. The RMS error of the 10-fold cross validation for (A) 26 features and (B) 3 features as the input of the optimal network ( $n = 8 , m = 2 5 6$ ).

network prediction and LDM for 322 new elements that have never been used to train the network or to fit the parameters of LDM. The network prediction for these 322 new elements has RMS error 0.605 MeV which is larger than the validation accuracy during training. However, it is much smaller than LDM where the RMS is around 2.542 MeV. Usually it is believed that a theoretical model with a few parameters generalize better than a deep neural network, be-

![](images/edce38acc6abd409ff8848f0fca19deb1b4c51bbd5f6bb9179e94d589def03c6.jpg)

![](images/377a63b66ac5d19b28eaec9c567c599192b1dbf97400c6147868249f4e7a7f24.jpg)

![](images/59d986010839053db2a42f4cabc697b2f282e509b2d97e2b79c405b5eb96dfc7.jpg)  
FIG. 4. (color online) The prediction error for all the nuclei as compared with LDM. Both training and testing data are used with (A) 26 features and (B) 3 features as the input of the optimal network ( $n =$ $8 , m = 2 5 6$ ).   
FIG. 5. (color online) The mass-residual prediction error for 322 new elements in AME2020 as compared with LDM.

cause the later has millions of parameters(here our DNN has about one millions trainable parameters) and was thought to be easy to overfit to the training data and fail to extrapolate to new data. In this study, it is shown that the deep learning generalizes better than LDM on new data.

# III. GLOBAL ALPHA DECAY HALF-LIFE PREDICTION

# A. Methods

The neural network trained in the nuclear mass prediction task can help the $\alpha$ decay halflives[30][31] prediction in two folds. First, for super-heavy nucleus[32] whose $Q$ -value has no experimental measurements or ab-initio calculations, the high precision network prediction provides a cheap way to compute the Q-value[33], using the mass of the mother nucleus, daughter nucleus and the $\alpha$ particle. Second, the network trained in nuclear mass prediction produces a word-vector representation for each nucleus, it is simply get from one of its hidden layers with a high dimension. The representation encodes high-dimensional information of the nucleus which may help many other calculations in nuclear physics, such as $\alpha$ -decay, $\beta$ -decay[34][35] half-lives or charge radius prediction. In the present work, we test the effect on $\alpha$ -decay halflives prediction.

The Q-value is a key information in $\alpha$ -decay and the half-lives is really sensitive to it accord-

![](images/576d4746740b98b342634372163684474acdb883e3d6d579fd147ce92b095491.jpg)  
FIG. 6. (color online) The Q-value prediction error for 486 nuclei

![](images/062b5ea987a8661ccda545a619f313969e3d4b83ffb01be868ef3d93b905eb8a.jpg)

![](images/b044c07289015ce52588871d8860c8fa8ecb7812e5f9ed36553cf03dc7412f35.jpg)

![](images/b03f9dd53dc8120dd07c944fca43aefcf0694a8451814f42b469cb0bd893f320.jpg)

![](images/2c045c74747f09e4463219d8a557d5e934f60bd770ec0e3d9fe54953ddf28564.jpg)

![](images/47c3b8b239c9af3f28a788b36723d4580bdf937ba363403f8265b571ce76e521.jpg)

![](images/b55cf5bdeebe171cf81830e222b6531a2b003e1a2bc5d87d122f9f15e722aa11.jpg)  
FIG. 7. (color online) The Q-value from deep neural network (solid circles) as compared with experimental measurements (square) for nuclei with proton number = 86, 87, 88, 89, 92, 93.

ing to most semi-empirical formulas, e.g., Royer formula[36]. It will be an important feature to be used as the input of the neural network for $\alpha$ -decay half-lives prediction. Shown in Fig 6 is the prediction error of the Q-value as compared with experimental data for 486 nuclei. The performance is not good for some super-heavy nuclei, however, the average rms deviation is only 0.15 MeV. Fig 7 is a more detailed comparison for nuclei with proton number = 86, 87, 88, 89, 92, 93.

The network we used is smaller in the $\alpha$ decay half-lives prediction after the performance scan. The structure is (n-input, 128, 256, 256, 256, 256, 256, 1) where ’tanh’ activation functions are used for the first and the last hidden layer, ’relu’ activation functions are used for other hidden layers.

The training data used to get the nuclear word-vector is not those best physical nuclear mass models, which contain both macro and micro parts whose residual is only about 0.4 Mev [37–39]. We only use the macro part of Bethe-Weizs¨acker model (BWM) and Liquid-Dropplet Model (LDM). In our experience, subtracting both macro and micro parts will not benefit nuclear word-vector learning. We observe that keeping the micro parts in the mass residual helps to reduce the $\alpha$ decay half-lives predicting error. Although the learning is more difficult if the effects of micro parts are included in the mass residual, the network will try its best to encode the associated quantum properties of nu-

cleus to minimize the differences to the residual in supervised learning. The encoded quantum properties in the nuclear word-vector helps the $\alpha$ decay half-lives prediction.

The prediction accuracy for two types of inputs are calculated. The first type mainly consists of native features. The second type uses representations of nucleus learned in the atomic mass prediction task, which is the word-vector.

In the 10-fold cross validation, the data-set is evenly divided into 10 folds, 9 folds are used for training and 1 for validation. Since our training data set is small, even 10-fold cross validation method still have big fluctuation and can’t evaluate the performance in a credible way, so we do 100 times 10-fold cross validation to better evaluate the performance our neural network. As a result, there are 1000 validation scores for each type of inputs.

# B. Results

The latent representations of nuclei are learned in the nuclear mass prediction task. Analogous to the spatial representation and momentum representation, the word-vector representations carry the ground state information of nuclei using a high-dimensional array of floating numbers. The high-dimensional word-vector of nuclei are believed to capture physics of the many-body quantum system which will help other relating tasks. This representation helps the network to predict the $\alpha$ decay half-lives bet-

![](images/cc94cf8c45341c078e1332cbdbfd72f716b350789067b36ea0cb6ad7ad36d8da.jpg)

![](images/3d8a5a8375178e4b46c31cf7a63aa2e15451b9273d73ec846814a78273825d57.jpg)

![](images/24d8ac5029dbd4a3d7d663f6381dcde0d8bd9eb4742494bbd61189299f5433ac.jpg)  
RMS $( I o g _ { 1 0 } T _ { 1 / 2 } ^ { E x p } - I o g _ { 1 0 } T _ { 1 / 2 } ^ { C a I } )$

![](images/7a1598146dcd0cfc5654c2c00a6fd27d061cb69a6a0988f3f6f6e7b250694bb6.jpg)

![](images/950e0da59f0d6bc8dd8407b8a54bb8c99475af00f568eb542a3d9838eeb7132e.jpg)

![](images/2e9619eec919307987f891b2fddd57c2e1ecb6fd163f4d523639af52375bc56c.jpg)  
RMS $( I o g _ { 1 0 } T _ { 1 / 2 } ^ { E x p } - I o g _ { 1 0 } T _ { 1 / 2 } ^ { C a I } )$   
FIG. 8. Prediction for $\alpha$ -decay half-lives using native inputs as compared with word-vector representations on 350 nuclei. Word vector 1 means it is obtained from the first hidden layer of the deep neural network we used to predict nuclear mass, for the details of those native features, see the appendix.

ter as compared with that trained with native features as inputs on the 350 nuclei, as shown in Fig 8. We also test the performance of wordvector gotten from different hidden layers, as show in Fig 9 and find that as the network goes deeper, the performance turns worse. The word vectors from deep layers seem to encode more information about the nuclear mass, which is objective of the pre-training task and won’t help too much in other tasks. Word-vectors get from

![](images/f19f7c645abd8a2751b0f6c83c554f06541e8ecf83fff4fec97e934df129ae2e.jpg)  
FIG. 9. The performance of word-vector from different hidden layers compared with native features as inputs.

![](images/c58219de59aef91c5416a57223fda37bb59dce38a8550d7d46a6ab8522e9cc3d.jpg)  
FIG. 10. Result of $\alpha$ decay half lives prediction on 486 nuclei using 64 native features as input.

shallow hidden layers seem to be good representations for new tasks.

It might seem a bit confusing in 10, some histograms have ”two peaks”, that’s because there are two nuclei in the data set hard to be predicted( $\mathrm { Z = 6 4 }$ , N = 84 and $\mathrm { ~ Z ~ = ~ } 7 1$ , N = 82), so the folds that have these two will have bad scores.

If a nucleus in the $\alpha$ decay table has not been used to train the mass prediction network, its latent representation will not be as good as those nuclei in the training dataset. In the previous data-set with 350 nuclei, 26% are missing from the pre-training data. In another data-set which has 486 nuclei along with the experimental Q-value, 29% have not been used to train the mass-residual prediction network. For this new data-set, training with 64 native features still performs better than the best word-vector performance. Using the 64 native features as inputs, as show in Fig 10 we get an RMS = 0.7315 on 100 times 10-fold cross validation, and the average training loss is about 0.1.

![](images/2f8a799f239e0ead460c4696a7c65e6c525507393d5194324414ebf57ff1daab.jpg)  
FIG. 11. (color online) Best network model prediction on 486 $\alpha$ decay half-lives data.

The division of training data and testing data can hugely influence the test result as we have seen in Fig 10, the result of 100 times 10-fold cross validation. Fig 11 shows a certain division which lead to the best testing result.

# IV. ALPHA DECAY HALF-LIVES PREDICTION ON EVEN-EVEN NUCLEI

Three-parameter Gamow formula [40–42] has a quite low prediction error for the half-lives of even-even nuclei,

$$
\log T = a \frac {Z}{Q} + b \sqrt {Z} + c \tag {3}
$$

The residual between Gamow formula and measurements can be further reduced either using a polynomial fit or a neural network. Fig 12 shows the performance of DNN in improving the residual. Using DNN, we can reduce the residual of Gamow formula from 0.3627 to 0.2297, on 100 times 10-fold cross validation. The inputs(Native 64 inputs) and DNN structure is the same as what we use for the global half-life prediction.

![](images/615e15c842815452036d15a1a7dad886fe84d411be4d6b8901fc7c004a203286.jpg)  
FIG. 12. The distribution and the mean residual of the Gamow formula as compared with the DNN improvement, on the alpha decay half-lives of even-even nuclei.

Using polynomial fit, the lowest residual we can get is 0.3052 using the same cross validation.

The DNN generalizes better than a polynomial fit even on this small data problem. We also try to fit the network prediction using polynomial functions to see if it can generate some analytical relation. And we find among one to ten order polynomials, the second order can do the best job with a result of 0.2679 on 100 times 10- fold cross validation. Although it is still not as good as DNN’s 0.2297, it’s already much better than fit the Gamow residual directly, with lowest residual 0.3052 using different orders of polynomial functions. Higher order polynomials make the performance worse because of over fitting. The extracted coefficients are shown below,

$$
0. 1 5 4 7 Z - 0. 0 2 2 2 N - 0. 4 3 4 4 Q
$$

$$
- 0. 0 0 2 2 Z ^ {2} - 0. 0 0 0 8 N ^ {2} + 0. 0 2 0 4 Q ^ {2} \tag {4}
$$

$$
+ 0. 0 0 2 4 Z N + 0. 0 0 3 7 Z Q - 0. 0 0 2 2 N Q
$$

As $Z$ and $N$ are much larger than $Q$ , the following four terms, $Z$ , $Z ^ { 2 }$ , $Z N$ , $Q$ have large contributions. Adding these four terms may improve the performance of the Gamow formula,

$$
\log T = a \frac {Z}{Q} + b \sqrt {Z} + c Z ^ {2} + d Z N + e Q + f Z + g \tag {5}
$$

The cross validation performance of this modified Gamow formula on even-even nuclei is shown in Fig 13.

# V. DISCUSSION

# A. Correlation matrix between the mass residual and features

The Pearson correlation coefficient is a good measure of the importance of each feature for

![](images/090d32323ca573296eab867be31e185a3e9183f121cf4e50d3ab82c1b8628617.jpg)  
FIG. 13. The distribution and the mean residual of modified Gamow formula on the alpha decay halflives of even-even nuclei.

the mass residual prediction, it also tells what physics is missing or not fully considered in the semi-empirical model. The formula is given by

$$
r = \frac {n (\sum x y) - (\sum x) (\sum y)}{\sqrt {[ n \sum x ^ {2} - (\sum x) ^ {2} ] [ n \sum y ^ {2} - (\sum y) ^ {2} ]}}
$$

where $r$ is the Pearson correlation coefficient, $x$ and $y$ represent values of two features for various samples and n is the total number of samples. Shown in Table. I are the correlations between mass residual and various features. Some common features are important for the LDM and BWM mass residual prediction, E.g., the number of neutrons on the 8th shell[43], the number of protons on the 7th shell, the number of valence neutrons and whether N or Z are magic numbers. These features are important for both mass residual from LDM and BWM. In principle, the deep neural network is able to construct these features using native ones (N, Z, A). In

TABLE I. The correlations between various features and mass residual for LDM and BWM. According to the table, the magnitude of the correlation is strong for shell structure and magic numbers.   

<table><tr><td>Features</td><td>correlation</td><td>Features</td><td>correlation</td></tr><tr><td>residual_LDM</td><td>1.000000</td><td>residual_BWM</td><td>1.000000</td></tr><tr><td>N_shell8</td><td>0.194654</td><td>N_shell8</td><td>0.380971</td></tr><tr><td>Z_shell7</td><td>0.120731</td><td>Z_shell7</td><td>0.363741</td></tr><tr><td>N_shell3</td><td>0.116282</td><td>Z_shell6</td><td>0.170536</td></tr><tr><td>Z_shell3</td><td>0.086444</td><td>N_shell7</td><td>0.143813</td></tr><tr><td>N_shell4</td><td>0.072662</td><td>Z</td><td>0.130579</td></tr><tr><td>Z_shell4</td><td>0.070161</td><td>A</td><td>0.104727</td></tr><tr><td>N_shell5</td><td>0.040211</td><td>N</td><td>0.086945</td></tr><tr><td>pair_energy</td><td>0.013236</td><td>A2/3</td><td>0.082608</td></tr><tr><td>Z</td><td>0.002454</td><td>Z_shell3</td><td>0.039904</td></tr><tr><td>A2/3</td><td>-0.000487</td><td>N-Z</td><td>0.005158</td></tr><tr><td>A</td><td>-0.007885</td><td>pair_energy</td><td>-0.003228</td></tr><tr><td>N</td><td>-0.014537</td><td>Z_shell4</td><td>-0.018830</td></tr><tr><td>Z_shell5</td><td>-0.028344</td><td>A-1/3</td><td>-0.021580</td></tr><tr><td>Z_valence</td><td>-0.033500</td><td>N_shell3</td><td>-0.039164</td></tr><tr><td>Z_shell6</td><td>-0.036544</td><td>N_shell6</td><td>-0.039891</td></tr><tr><td>A-1/3</td><td>-0.036847</td><td>Z_valence</td><td>-0.043764</td></tr><tr><td>N-Z</td><td>-0.041295</td><td>N_shell4</td><td>-0.054386</td></tr><tr><td>N_shell6</td><td>-0.044589</td><td>Z_shell5</td><td>-0.055684</td></tr><tr><td>N_shell7</td><td>-0.096653</td><td>N_shell5</td><td>-0.064732</td></tr><tr><td>magic_Z</td><td>-0.188633</td><td>N_valence</td><td>-0.153176</td></tr><tr><td>N_valence</td><td>-0.249767</td><td>magic_Z</td><td>-0.157655</td></tr><tr><td>magic_N</td><td>-0.253896</td><td>magic_N</td><td>-0.201970</td></tr></table>

practice, the data are small and the network may arrive at the final conclusion using other latent features. From the 10-fold cross validation, these features help to reduce the RMS error by 60 keV.

The correlation between mass residual and magic numbers is also shown in the heat-map

Fig 14. The deviations are large for either magic

![](images/8303c5820f7a19b14f13a405d3936ee17e12ef8e003d894291bf164ce1306f98.jpg)

![](images/82ec20169781183534819ab606e6e923b51a13bf22e3b928af5d102b5ee6c3bf.jpg)

![](images/0a008845874f88e20353e4e49e5b054aaa126152c3820104b6b41a2de2b79543.jpg)  
FIG. 15. The residual of binding energy per nucleon as a function of number of protons (left) and number of neutrons (right) on valence shells. Different shells contribute to different bands in the figure.

![](images/6b7f8db305a2949aec88bf9144f51cd5aa47b6f637f90921c74f50d945b217bf.jpg)

![](images/439954ce46769ca0192505047d8e2ff8500b6ed7b3ed69bd078c5d73c209e987.jpg)

![](images/9a5868401b084a2895b11c4ab11c105cb2d08c7cbc02a31560bf377b5f37597e.jpg)

![](images/c1576e4a147cccea4150fcbc8583b9433706a90967e9b16254d75f9ad55c6674.jpg)

![](images/f8a1580b61e1ef6870739722af73fce95a9bc160100c109a95381cf375de7a3f.jpg)  
FIG. 14. (color online) The binding energy per nucleon as a function of proton number Z and neutron number N.   
FIG. 16. The binding energy per nucleon as a function of number of protons (left) and number of neutrons (right) on valence shells 3 and 4.

Z or magic N.

The correlation between binding energy per nucleon and number of valence nucleons are shown in Fig 15. There seems to be several bands with each one shows a linear correlation between BE/A and valence nucleons. The bandstructure comes from different energy levels for different valence shells. In the differential study for different valence shells, light nuclei show negative correlation between BE/A and the number of valence nucleons as shown in Fig 16 while

![](images/cdf49d0c160cd3afe7702538b2b26de3441706723b75ab14414c48f2568e7f4c.jpg)

![](images/2483aae53df95409829c19408452f4bde7721fdda71479c059aff25b20b2325c.jpg)

![](images/59d42e3739035b10ef2f7304783151af3ff46dff51ae003236e4290b896fcc43.jpg)

![](images/3a0c827a4d59c2692b0d18f75f0bd1db4ec386fd02267852700661f9b95ac909.jpg)  
FIG. 17. The binding energy per nucleon as a function of number of protons (left) and number of neutrons (right) on valence shells of heavy nucleus.

heavy nuclei show positive correlation, as shown in Fig 17.

# VI. SUMMARY AND OUTLOOK

A deep neural network is trained to predict the nuclear mass residual between experimental data and phenomenological models. We achieve standard deviation $\sigma = 0 . 2 6 3$ MeV on 10-fold cross validation on 2149 nuclei. We verify that physical a prior (e.g., shell structure and magic numbers) helps to decrease the predicting error in this small data problem. The correlations between nuclear mass and various features, e.g., Z, N, magic number, as well as nucleons in each shell are calculated. It shows that the magic numbers as well as the number of nucleons on valence shells have strong correlation with mass residual. The values of neurons in the hidden layers of the network are used as latent representations or word-vectors of nuclei. These nuclear word-vectors from pre-trained models in mass predicting task is used in a new $\alpha$ decay halflives prediction. We observe that keeping the micro part in the mass residual helps to learn a better word-vector of nuclei for $\alpha$ decay prediction task. Word-vectors from shallow layers perform better than deep layers indicating that deep layers might be more specific to the mass residual prediction.

In the future, the nuclear word-vector learned in the mass residual, $\alpha$ decay half-lives prediction as well as other regression tasks can be used

in relating tasks, such as $\beta$ decay, r process and so on. The method developed in the present paper paves a new way to use heterogeneous big data in the field of nuclear physics.

# ACKNOWLEDGEMENT

This work is supported by the National Natural Science Foundation of China under Grant Nos.12075098 and 11861131009. Computations are performed at Nuclear Science Computer Center at CCNU (NSC3). LG Pang also acknowledge the support provided by Huawei Technologies Co., Ltd.

The data used in this study are listed below:

• 2149 nuclei(mass): FRDM (2012) [12]   
• 2471 nuclei(mass): AME2020 [27, 44]   
• 350 nuclei(α decay):[45]   
• 486 nuclei( $\alpha$ decay):[46–48]

# VII. APPENDIX: FEATURES OF DIFFERENT INPUTS

26 features for nucleus:

• (3 features) Z, N, A   
• (7 features) Number of protons on 7 shells   
• (8 features) Number of neutrons on 8 shells   
• (1 feature ) Number of valence protons

• (1 feature ) Number of valence neutrons   
• (3 features) N  Z, A2/3, A−1/3   
• (1 features) Is Z a magic number? (1 for yes, 0 for no)   
• (1 features) Is N a magic number? (1 for yes, 0 for no)   
• (1 features) Pair energy: (−1)Z +(−1)N2 $\frac { ( - 1 ) ^ { Z } + ( - 1 ) ^ { N } } { 2 }$ 2

4 features for odd-even

• (1 features) Is odd-odd nucleus? (1 for yes, 0 for no)   
• (1 features) Is even-even nucleus? (1 for yes, 0 for no)   
• (1 features) Is odd-even nucleus? (1 for yes, 0 for no)   
• (1 features) Is even-odd nucleus? (1 for yes, 0 for no)

30 features for nucleus:

• (26 features mentioned above)   
• (4 features) odd-even

Natives 11 features for $\alpha$ decay:

• (9 features) $Z , N , A$ for mother, daughter nucleus and He

• (1 features) Q-value calculated by network.   
• (1 features) $Q ^ { - 1 / 2 }$ calculated by network. Natives 14 features for $\alpha$ decay:   
• (9 features) $Z , N , A$ for mother nucleus, daughter nucleus and He.   
• (1 features) Q-value calculated by network.   
• (4 features) odd-even for mother nucleus.

Native 64 features for $\alpha$ decay:

• (60 features) 30 features for mother nucleus and daughter nucleus.   
• (3 features) $Z , N , A$ for $\alpha$ particle   
• (1 features) Q-value calculated by network.

Word-vector 517 inputs for $\alpha$ decay:

• (512 features) 256 dimensional wordvector features for mother nucleus and daughter nucleus.   
• (4 features) odd-even for mother nucleus.   
• (1 features) Q-value calculated by network.

[2] A. Akmal, V. R. Pandharipande, and D. G. Ravenhall. The Equation of state of nucleon matter and neutron star structure. Phys. Rev. C, 58:1804–1828, 1998.   
[3] M.R. Mumpower, R. Surman, G.C. McLaughlin, and A. Aprahamian. The impact of individual nuclear properties on r-process nucleosynthesis. Progress in Particle and Nuclear Physics, 86:86–126, 2016.   
[4] Dirk Martin, Almudena Arcones, Witold Nazarewicz, and Erik Olsen. Impact of nuclear mass uncertainties on the $r$ -process. Phys. Rev. Lett., 116(12):121101, 2016.   
[5] Z.M. Niu and H.Z. Liang. Nuclear mass predictions based on bayesian neural network approach with pairing and shell effects. Physics Letters B, 778:48–53, 2018.   
[6] Ubaldo Ba˜nos Rodr´ıguez, Cristofher Zu˜niga Vargas, Marcello Gon¸calves, Sergio Barbosa Duarte, and Fernando Guzm´an. Bayesian Neural Network improvements to nuclear mass formulae and predictions in the SuperHeavy Elements region. EPL, 127(4):42001, 2019.   
[7] Peter M¨oller, William D. Myers, Hiroyuki Sagawa, and Satoshi Yoshida. New Finite-Range Droplet Mass Model and Equationof-State Parameters. Phys. Rev. Lett., 108(5):052501, 2012.   
[8] Xiao-Xu Dong, Rong An, Jun-Xu Lu, and Li-Sheng Geng. Novel bayesian neural network based approach for nuclear charge radii. Phys. Rev. C, 105:014308, Jan 2022.   
[9] Zepeng Gao, Yongjia Wang, Hongliang L¨u, Qingfeng Li, Caiwan Shen, and Ling Liu. Machine learning the nuclear mass. 5 2021.   
[10] Raditya Utama and Jorge Piekarewicz. Refining mass formulas for astrophysical applications: a

Bayesian neural network approach. Phys. Rev. C, 96(4):044308, 2017.   
[11] Yifan Liu, Chen Su, Jian Liu, Pawel Danielewicz, Chang Xu, and Zhongzhou Ren. Improved naive Bayesian probability classifier in predictions of nuclear mass. Phys. Rev. C, 104(1):014315, 2021.   
[12] P. M¨oller, A.J. Sierk, T. Ichikawa, and H. Sagawa. Nuclear ground-state masses and deformations: Frdm(2012). Atomic Data and Nuclear Data Tables, 109-110:1–204, 2016.   
[13] Ning Wang, Min Liu, Xizhen Wu, and Jie Meng. Surface diffuseness correction in global mass formula. Physics Letters B, 734:215–219, 2014.   
[14] Min Liu, Ning Wang, Yangge Deng, and Xizhen Wu. Further improvements on a global nuclear mass model. Phys. Rev. C, 84:014333, Jul 2011.   
[15] S. Goriely, N. Chamel, and J. M. Pearson. Skyrme-hartree-fock-bogoliubov nuclear mass formulas: Crossing the 0.6 mev accuracy threshold with microscopically deduced pairing. Phys. Rev. Lett., 102:152503, Apr 2009.   
[16] W. D. Myers, W. J. Swiatecki, T. Kodama, L. J. El-Jaick, and Eberhard R. Hilf. Droplet model of the giant dipole resonance. Phys. Rev. C, 15:2032–2043, 1977.   
[17] Z. M. Niu, J. Y. Fang, and Y. F. Niu. Comparative study of radial basis function and Bayesian neural network approaches in nuclear mass predictions. Phys. Rev. C, 100(5):054311, 2019.   
[18] L´eo Neufcourt, Yuchen Cao, Witold Nazarewicz, and Frederi Viens. Bayesian approach to model-based extrapolation of nuclear observables. Phys. Rev. C, 98:034318, Sep 2018.   
[19] Murarka Utsav Anil, Kinjal Banerjee, Tuhin Malik, and Constan¸ca Providˆencia. The neutron

star outer crust equation of state: a machine learning approach. JCAP, 01(01):045, 2022.   
[20] Giuseppe Carleo, Ignacio Cirac, Kyle Cranmer, Laurent Daudet, Maria Schuld, Naftali Tishby, Leslie Vogt-Maranto, and Lenka Zdeborov´a. Machine learning and the physical sciences. Rev. Mod. Phys., 91:045002, Dec 2019.   
[21] Amber Boehnlein et al. Artificial Intelligence and Machine Learning in Nuclear Physics. 12 2021.   
[22] S. Gazula, J. W. Clark, and H. Bohr. Learning and prediction of nuclear stability by neural networks. Nucl. Phys. A, 540:1–26, 1992.   
[23] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, and John Walter Clark. Nuclear mass systematics using neural networks. Nucl. Phys. A, 743:222–235, 2004.   
[24] Tuncay Bayram, Serkan Akkoyun, and S. Okan Kara. A study on ground-state energies of nuclei by using neural networks. Annals of Nuclear Energy, 63:172–175, 2014.   
[25] R. Utama, J. Piekarewicz, and H. B. Prosper. Nuclear Mass Predictions for the Crustal Composition of Neutron Stars: A Bayesian Neural Network Approach. Phys. Rev. C, 93(1):014311, 2016.   
[26] Esra Y¨uksel, Derya Soydaner, and H¨useyin Bahtiyar. Nuclear binding energy predictions using neural networks: Application of the multilayer perceptron. Int. J. Mod. Phys. E, 30(03):2150017, 2021.   
[27] W.J. Huang, Meng Wang, Kondev F.G., and S. Naimi Audi G. The ame 2020 atomic mass evaluation (ii). tables, graphs and references, 2021”.   
[28] J. H. Bai, Z. M. Niu, B. Y. Sun, and Y. F. Niu. The description of giant dipole resonance

key parameters with multitask neural networks. Phys. Lett. B, 815:136147, 2021.   
[29] Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. ICML’15, page 448–456. JMLR.org, 2015.   
[30] B. Alex Brown. Simple relation for alpha decay half-lives. Phys. Rev. C, 46:811–814, 1992.   
[31] B. Buck, A. C. Merchant, and S. M. Perez. Half-Lives of Favored Alpha Decays from Nuclear Ground States. Atom. Data Nucl. Data Tabl., 54:53–73, 1993.   
[32] J. P. Cui, Y. L. Zhang, S. Zhang, and Y. Z. Wang. α -decay half-lives of superheavy nuclei. Phys. Rev. C, 97(1):014316, 2018.   
[33] Ubaldo Ba˜nos Rodr´ıguez, Cristofher Zu˜niga Vargas, Marcello Gon¸calves, Sergio Barbosa Duarte, and Fernando Guzm´an. Alpha halflives calculation of superheavy nuclei with Q $\alpha$ -value predictions based on the Bayesian neural network approach. J. Phys. G, 46(11):115109, 2019.   
[34] N. J. Costiris, E. Mavrommatis, K. A. Gernoth, and J. W. Clark. Decoding $\beta$ -decay systematics: A global statistical model for $\beta ^ { - }$ half-lives. Phys. Rev. C, 80:044332, Oct 2009.   
[35] N. J. Costiris, E. Mavrommatis, K. A. Gernoth, J. W. Clark, and H. Li. Statistical global modeling of beta-decay halflives systematics using multilayer feedforward neural networks and support vector machines, 2008.   
[36] Dashty T. Akrawy, H. Hassanabadi, S. S. Hosseini, and K. P. Santhosh. Systematic study of $\alpha$ -decay half-lives using Royer and related formula. Nucl. Phys. A, 971:130–137, 2018.   
[37] J. Toivanen, J. Dobaczewski, M. Kortelainen, and K. Mizuyama. Error analysis of nuclear

mass fits. Phys. Rev. C, 78:034306, 2008.   
[38] R. Utama and J. Piekarewicz. Validating neuralnetwork refinements of nuclear mass models. Phys. Rev. C, 97(1):014306, 2018.   
[39] K. P. Santhosh, Jayesh George Joseph, and B. Priyanka. Fine structure in the \alpha-decay of odd-even nuclei. Nucl. Phys. A, 877:1–18, 2012.   
[40] Gamow. Zur Quantentheorie des Atomkernes. 1928.   
[41] Roger H. Stuewer. Gamow’s Theory of Alpha-Decay, pages 147–186. Springer Netherlands, Dordrecht, 1986.   
[42] Barry R. Holstein. Understanding alpha decay. American Journal of Physics, 64:1061– 1071, 1996.   
[43] D. N. Poenaru, R. A. Gherghescu, and N. Carjan. Alpha-decay lifetimes semiempirical relationship including shell effects. EPL, 77(6):62001, 2007.   
[44] W.J. Huang, Meng Wang, Kondev F.G., and

Audi G.and S. Naimi. The ame 2020 atomic mass evaluation (i). evaluation of input data, and adjustment procedures, 2021”.   
[45] www.radiochemistry.org/periodictable/elements, 2005.   
[46] Shan Zhang, Yanli Zhang, Jianpo Cui, and Yanzhao Wang. Improved semi-empirical relationship for $\alpha$ -decay half-lives. Phys. Rev. C, 95:014311, Jan 2017.   
[47] J.P. Cui, Y. Xiao, Y.H. Gao, and Y.Z. Wang. α- decay half-lives of neutron-deficient nuclei. Nuclear Physics A, 987:99–111, 2019.   
[48] S. Samanta, S. Das, R. Bhattacharjee, S. Chatterjee, R. Raut, S. S. Ghugre, A. K. Sinha, U. Garg, Neelam, N. Kumar, P. Jones, Md. Sazedur R. Laskar, F. S. Babra, S. Biswas, S. Saha, P. Singh, and R. Palit. Single-particle excitations in the level structure of $^ \mathrm { 6 4 }$ Cu. Phys. Rev. C, 97:014319, Jan 2018.