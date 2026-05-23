# Deep Learning approaches for nuclear binding energy prediction: A comparative study of RNN, GRU and LSTM Models

Amir Jalili $^ { 1 }$ ,∗ Feng Pan $^ { 2 , 3 }$ , Ai Xi Chen1, and Jerry P. Draayer3

$^ { 1 }$ Zhejiang Key Laboratory of Quantum State Control and Optical Field Manipulation,

Department of Physics, Zhejiang Sci-Tech University, Hangzhou 310018, China

$^ 2$ Department of Physics, Liaoning Normal University, Dalian 116029, P.R. China and

$^ 3$ Department of Physics and Astronomy, Louisiana State University, Baton Rouge, LA 70803-4001, USA

This study investigates the application of deep learning models-recurrent neural networks, gated recurrent units, and long short-term memory networks-for predicting nuclear binding energies. Utilizing data from the Atomic Mass Evaluation (AME2020), we incorporate key nuclear structure features, including proton and neutron numbers, as well as additional terms from the liquid drop model and shell effects. Our comparative analysis demonstrates that the gated recurrent units model achieves the lowest root-mean-square error (σRMSE) of 0.326 MeV, surpassing traditional regression-based approaches. To assess model reliability, we validate predictions using the Garvey-Kelson relations, obtaining an error of 0.202 MeV, and further test extrapolation capabilities using the WS, WS3, and WS4 models. The extrapolation analysis confirms the robustness of our approach, particularly in predicting binding energies for nuclei near the driplines. These results highlight the effectiveness of deep learning in nuclear BE predictions, highlighting its potential to enhance the accuracy and reliability of theoretical nuclear models.

# I. INTRODUCTION

The precise determination of nuclear binding energy (BE) is crucial for understanding the stability and structure of atomic nuclei, as well as the fundamental interactions that govern them. Traditional global models, such as the liquid drop model (LDM) [1] and the Bethe-Weizs¨acker (BW) formula [2, 3], have long served as the foundation for nuclear mass predictions. While subsequent refinements, including the finite-range droplet model (FRDM) [4] and Weizs¨acker-Skyrme (WS) model [5], have improved predictive accuracy, significant discrepancies persist, particularly near the nuclear drip lines. Different kinds of nuclear mass models have been developed to incorporate more effects, which are known microscopic mass models based on the relativistic [6–16], and nonrelativistic density functionals with other theoretical models [17–26]. These challenges necessitate the exploration of alternative approaches that can effectively capture the complex nonlinear dependencies within nuclear data. Theoretical models for nuclear mass predictions can generally be categorized into two main types: global models and local models [27–30]. Global theoretical models, such as macroscopic-microscopic approaches and nuclear density functional theories [31], aim to describe nuclear masses across the entire nuclear chart by utilizing a unified theoretical framework. While these models provide valuable insights into nuclear structure and large-scale trends, their accuracy may vary in regions where experimental data are scarce.

In contrast, local models rely on the assumption of strong correlations between neighboring nuclei and establish predictive relationships based on known exper-

imental masses. These approaches, often referred to as local-type theoretical models, have distinct advantages in regions where experimental data are available, as they can achieve higher predictive accuracy by using well-established nuclear interactions. Among the most notable local models is the Garvey-Kelson (GK) relation [32–35], which exploits linear mass relationships between neighboring nuclei to estimate unknown masses with remarkable precision. Another widely used local approach is the neutron-proton interaction-based mass relation, which incorporates the effects of nucleon interactions to refine mass predictions. Due to their reliance on empirical data, local models demonstrate exceptional accuracy within experimentally known regions. For instance, the GK relation and similar mass relations typically achieve an accuracy of approximately 0.2 MeV [29], significantly outperforming many global models in these well-characterized regions. However, their extrapolation capabilities are inherently limited, making them less reliable for predicting masses far from experimentally measured nuclei. Consequently, the integration of both global and local models, along with advanced machine learning (ML) techniques, presents a promising avenue for enhancing the precision and robustness of nuclear mass predictions across the entire nuclear landscape. In this paper, we will extend our analysis by testing and evaluating our models using the GK relations, further assessing their reliability and accuracy in predicting nuclear BE.

In recent years, ML and deep learning (DL) techniques have emerged as powerful tools for nuclear physics applications, enabling accurate predictions of various nuclear properties. In recent years, neural networks (NN) with various algorithms, along with advanced ML techniques, have been successfully applied to nuclear physics studies [36, 37]. Examples include convolutional NNs [38], support vector machines [39], and Kolmogorov-Arnold networks [40]. Additionally, several NN-based models have

been employed for predicting nuclear properties, such as binding energies [41–52], energy spectra [53, 54], charge radii [55–57], $\alpha$ -decay half-lives [58, 59], and $\beta$ -decay halflives [60, 61], among others [62–65]. Furthermore, kernel ridge regression has been applied for nuclear mass predictions, demonstrating its effectiveness in refining mass models and improving predictive accuracy [66–68]. These advancements underscore the increasing role of ML in nuclear physics, providing robust and data-driven approaches for modeling complex nuclear phenomena.

Their ability to analyze complex patterns within large datasets has significantly enhanced our understanding of nuclear structure and decay processes, offering new insights beyond traditional theoretical models. Unlike conventional models that rely on predefined functional forms, ML-based methods can extract intricate patterns from large datasets, enabling improved generalization and predictive performance. Among these, recurrent neural networks (RNNs) and their variants-gated recurrent units (GRUs) and long short-term memory (LSTM) networks-are particularly well-suited for sequential data modeling, making them promising candidates for nuclear properties predictions [69–74]. The advantage of RNNs stems from their feedback mechanism, which allows them to retain memory of previous inputs, effectively capturing long-range correlations in nuclear structure.

In this study, we employ RNN-based architectures to predict nuclear BE using data from the Atomic Mass Evaluation (AME2020) [75]. Our approach integrates nuclear structure features derived from the BW formula, including volume, surface, Coulomb, and pairing terms, alongside shell effects. By dynamically learning weights and feature interactions, our models surpass conventional regression-based approaches. The results demonstrate that GRUs achieve the lowest $\sigma$ RMSE of 0.326 MeV, significantly outperforming traditional models. To further validate our predictions, we apply the GK relations, which are highly accurate in regions where experimental data are available. To evaluate the reliability of our approach, we embed the mass predictions from three different RNN models into the GK relations and obtain an error of approximately 0.202 MeV for the GRU case. This confirms the effectiveness of DL models in capturing nuclear mass trends with high precision. Given that more than 11,000 nuclei require extrapolation, DL algorithms provide a powerful tool for extending nuclear BE predictions into unmeasured regions. Additionally, we investigate the extrapolation capabilities of our models in regions where experimental data are unavailable. Our study considers the WS [76], WS3 [77], and WS4 [5] models with both relu and tanh activation functions, ensuring the reliability of extrapolated predictions for unmeasured nuclei.

This paper is organized as follows: Section II presents the BW formula along with the fitting parameters and details of the RNN, LSTM, and GRU architectures, including data preprocessing and training procedures. Section III discusses the results, covering the evaluation of

RNN, GRU, and LSTM models, validation using GK relations, and an analysis of neutron and proton separation energies, mass excess, and extrapolation capabilities for the WS, WS3, and WS4 models. Finally, Section IV concludes the study and outlines future directions for advancing DL-based nuclear binding energy models.

# II. THEORY

# A. LDM

Traditional feed-forward NNs establish a direct, deterministic mapping between input features (x) and output (y) by optimizing complex non-linear functions [78, 79]. In contrast, RNNs introduce an additional feedback mechanism, where the output of a neuron at a given time step is fed back into the network as an input for the subsequent time step [80–83]. This feedback structure allows RNNs to effectively model sequential dependencies and long-range correlations within nuclear data, making them particularly suitable for nuclear BE predictions.

To construct our model, we employ features extracted from the BW mass formula [3, 84]. The LDM, which serves as the foundation for BW, describes the nucleus in terms of its fundamental constituents: protons ( $Z$ ), neutrons ( $N$ ), and atomic mass number ( $A$ ). The total nuclear binding energy ( $E _ { \mathrm { B } }$ ) is expressed as a sum of multiple energy contributions:

$$
B E = a _ {\mathrm {V}} A - a _ {\mathrm {S}} A ^ {2 / 3} - a _ {\mathrm {C}} \frac {Z (Z - 1)}{A ^ {1 / 3}} - a _ {\mathrm {A}} \frac {(N - Z) ^ {2}}{A} + \delta (N, Z), \tag {1}
$$

where: $a _ { \mathrm { V } } A$ represents the volume energy, $a _ { \mathrm { S } } A ^ { 2 / 3 }$ accounts for the surface energy, $a _ { \mathrm { C } } { \frac { Z ( Z - 1 ) } { A ^ { 1 / 3 } } }$ denotes the Coulomb repulsion energy between protons, $a _ { \mathrm { A } } { \frac { ( N - Z ) ^ { 2 } } { A } }$ corresponds to the symmetry energy associated with neutron-proton imbalance and $\delta ( N , Z )$ captures pairing effects and is given by:

$$
\delta (N, Z) = \left\{ \begin{array}{l l} + \delta_ {0}, & \text {f o r e v e n} Z, N (\text {e v e n} A), \\ 0, & \text {f o r o d d} A, \\ - \delta_ {0}, & \text {f o r o d d} Z, N (\text {e v e n} A), \end{array} \right. \tag {2}
$$

where $\delta _ { 0 } = a _ { \mathrm { P } } A ^ { k _ { \mathrm { P } } }$ .

Using a least squares fitting (LSF) approach, we determine the optimal values of the coefficients in our model. The resulting σRMSE for a dataset comprising approximately 3264 nuclei ( $Z \ge 8 , N \ge 8 ,$ ) is found to be 3.29 MeV. The fitted parameter values obtained through the LSF method are as follows: $a _ { V } = 1 5 . 4 5 , a _ { S } = 1 6 . 9 1 , a _ { C } =$ $0 . 7 0 , a _ { A } = 2 2 . 6 2 , a _ { P } = 9 . 3 5$ and $\begin{array} { r } { k _ { p } = - \frac { 3 } { 4 } } \end{array}$ .

These values provide an optimized representation of nuclear BE contributions and serve as key inputs for refining predictive models. Our objective is to apply the

![](images/31fc7b365a6b60140d89b143d1a8f45af44699bc4ff7379f733b5706e86c0f6b.jpg)  
FIG. 1. Theoretical predictions for the total binding energy (BE) relative to experimental data from AME2020 for 3,092 nuclei.

RNN architecture to refine these predictions by dynamically learning complex nuclear correlations, thereby reducing the deviation in BE estimations. The $\sigma$ RMSE reduction achieved through our approach is presented in Fig. 1.

# B. RNN, LSTM, and GRU Architectures

# 1. Simple RNN Architecture

RNNs are a specialized class of NNs designed for processing sequential data, such as time series or feature sequences, through feedback connections [80]. Unlike traditional feedforward networks, which handle inputs independently, RNNs incorporate past outputs as additional inputs at each time step. This enables them to retain historical information, allowing RNNs to remember past states when making future predictions. As a result, they are particularly well-suited for tasks that require understanding temporal dependencies. See Fig. 2

The concept of RNNs was first introduced by Rumelhart et al. (1986) [80] in a letter published in Nature, which described a self-organizing NN learning procedure. Over the years, RNNs have evolved into various forms, including input-output mapping networks, commonly used for classification and sequential data prediction. A major breakthrough in the field emerged with the demonstration that RNNs can effectively perform credit assignment over long sequences, equivalent to processing information across 1,200 layers in an unfolded network. This advancement significantly improved the ability of RNNs to model complex sequential dependencies. In 1997, one of the

![](images/b262074edb7a0e9623f39094db82f23b709d65ab15083e968762815e262fe552.jpg)  
FIG. 2. Comparison between a Feed-Forward Neural Network (ANN), where inputs are processed in a unidirectional manner, and a RNN, which incorporates feedback connections by passing outputs of processing nodes back into the model to capture sequential dependencies.

most influential architectures, LSTM, was introduced, enabling the processing of longer sequences by addressing the vanishing gradient problem [81, 85]. In this section, we introduce the three most prominent RNN architectures–Simple RNN, LSTM, and GRU–and highlight their significance in predicting nuclear binding energies. The Simple RNN is the most fundamental recurrent architecture. It consists of a simple NN with a feedback connection that enables it to process sequential data of variable length. Unlike feedforward NNs, where each input feature has independent weights, RNNs share weights across multiple time steps, allowing efficient generalization over sequences. In an RNN, the output at a given time step depends on previous time steps and is computed using a recursive update rule. This results in an unfolded computational graph, where weights are shared across time steps. Fig. 3 illustrates an RNN operating on an input sequence $x _ { t }$ over $t$ time steps, where $t$ represents the position in the sequence rather than real-world time. The cyclical nature of the computational graph highlights how previous values influence the present step. The unfolded computational graph represents a chain of events, demonstrating the flow of information both forward (computing outputs and losses) and backward (computing gradients during backpropagation).

# Training RNNs for Nuclear Data Prediction:

The training process for nuclear BE prediction involves computing gradients of the loss function concerning the model parameters. This consists of two key steps [86]:

1:Forward propagation: Information flows from left to right through the unfolded computational graph.

![](images/fdb39f03105ad309ecdc4b629d50a87891892021877db49d1c5aa1614b122a66.jpg)  
FIG. 3. (a) Internal structure of a simple RNN cell, (b) architecture of a GRU cell, and (c) structure of an LSTM cell. Here, $h _ { t }$ represents the hidden state, and $x _ { t }$ denotes the input at time step $t$ . The forget gate ( $f _ { t }$ ), input gate (it), and output gate (yt) regulate information flow in the LSTM model. $C _ { t }$ signifies the cell state at time step $t$ . AF refers to activation functions such as tanh and relu.

2:Backpropagation through time: The model iterates backward in time, computing gradients recursively for each node, starting from the final loss and propagating through all previous states.

Due to the sequential nature of forward propagation, gradient computations are computationally expensive, as parallelization is not feasible. To efficiently handle training, previously computed states from the forward pass are stored and reused in the backpropagation process. The total loss for a sequence is obtained by summing losses over all time steps. The output $o _ { t }$ is passed through a softmax activation function, producing probability distributions over the predicted output categories. One of the major challenges in training RNNs is the vanishing gradient problem, where gradients diminish exponentially as they are backpropagated through time. This leads to ineffective learning over long sequences. To mitigate this issue: tanh is often used as the activation function, as it retains nonzero gradients for longer time steps. We also explore the relu activation function to identify the bestperforming configuration for nuclear BE predictions.

RNNs can be configured with different types of recurrent connections, affecting how information is transferred between layers:

Hidden-to-hidden connections: The RNN produces outputs at each time step, passing information between hidden units across time steps. This corresponds to the standard SimpleRNN architecture. Output-to-hidden connections: Outputs at specific time steps are fed back

into hidden units for future time steps, enhancing memory retention. Sequential input to single output: The network processes an entire sequence before generating a single output, commonly used in applications like binding energy prediction. This feature makes RNNs particularly well-suited for learning sequential relationships in nuclear structure data, where the BE exhibits correlations with proton and neutron numbers.

An RNN cell takes an input vector $x _ { t }$ at time step $t$ , processes it through a hidden state $h _ { t }$ , and generates an output $y _ { t }$ using the following recurrence relations [86]:

$$
h _ {t} = f \left(W _ {h} x _ {t} + U _ {h} h _ {t - 1} + b _ {h}\right) \tag {3}
$$

$$
y _ {t} = f \left(W _ {y} h _ {t} + b _ {y}\right) \tag {4}
$$

where: - $W _ { h }$ , $U _ { h }$ , and $W _ { y }$ are weight matrices controlling interactions between inputs, hidden states, and outputs. - $b _ { h }$ and $b _ { y }$ are bias vectors. - $f ( \cdot )$ represents the activation function, typically a hyperbolic tangent tanh or relu.

The hidden state $h _ { t }$ retains memory of past inputs, allowing RNNs to model nuclear binding energy as a function of historical nuclear configurations.

# 2. LSTM Architecture

Despite their advantages, RNNs suffer from the vanishing gradient problem, which hinders learning over long sequences. To address this, LSTM networks introduce gated memory cells that regulate information flow through input, forget, and output gates [81]. The LSTM equations are given by:

$$
f _ {t} = \sigma (W _ {f} x _ {t} + U _ {f} h _ {t - 1} + b _ {f}) \qquad \qquad (5)
$$

$$
i _ {t} = \sigma \left(W _ {i} x _ {t} + U _ {i} h _ {t - 1} + b _ {i}\right) \tag {6}
$$

$$
\tilde {C} _ {t} = \tanh  \left(W _ {C} x _ {t} + U _ {C} h _ {t - 1} + b _ {C}\right) \tag {7}
$$

$$
C _ {t} = f _ {t} \odot C _ {t - 1} + i _ {t} \odot \tilde {C} _ {t} \tag {8}
$$

$$
y _ {t} = \sigma \left(W _ {o} x _ {t} + U _ {o} h _ {t - 1} + b _ {o}\right) \tag {9}
$$

$$
h _ {t} = o _ {t} \odot \tanh  \left(C _ {t}\right) \tag {10}
$$

where: - $f _ { t }$ , $i _ { t }$ , and $o _ { t }$ are the forget, input, and output gates, respectively. - $C _ { t }$ is the cell state, maintaining long-term dependencies. - $\sigma ( \cdot )$ is the sigmoid function. - The operator $\odot$ represents element-wise multiplication, ensuring that each gate influences only the corresponding elements of the cell state.

By incorporating nuclear structure features such as atomic mass (A), proton number ( $Z$ ), neutron number ( $N$ ) and others into LSTM networks, we can dynamically learn interactions affecting nuclear BE and improve predictive accuracy.

# 3. GRU Architecture

A GRU is a simplified variant of LSTM that combines the forget and input gates into a single update gate, reducing computational complexity [87]. The GRU update equations are:

$$
r _ {t} = \sigma \left(W _ {r} x _ {t} + U _ {r} h _ {t - 1} + b _ {r}\right) \tag {11}
$$

$$
z _ {t} = \sigma \left(W _ {z} x _ {t} + U _ {z} h _ {t - 1} + b _ {z}\right) \tag {12}
$$

$$
\tilde {h} _ {t} = \tanh  \left(W _ {h} \left(r _ {t} \odot h _ {t - 1}\right) + U _ {h} x _ {t} + b _ {h}\right) \tag {13}
$$

$$
h _ {t} = z _ {t} \odot \tilde {h} _ {t} + (1 - z _ {t}) \odot h _ {t - 1} \tag {14}
$$

where: - $r _ { t }$ is the reset gate, determining how much past information to forget. - $z _ { t }$ is the update gate, controlling the trade-off between past and new information. - $h _ { t }$ is the hidden state update.

GRUs provide a computationally efficient alternative to LSTMs while retaining memory for long-term dependencies in nuclear data. This allows GRUs to effectively capture binding energy variations across isotopic chains.

By training on binding energy datasets such as AME2020, our RNN, LSTM, and GRU models learn complex interactions between nuclear features, leading to improved generalization and predictive accuracy. The ability of these models to retain sequential dependencies is crucial for extrapolating BE values for unmeasured isotopes, reducing $\sigma$ RMSE compared to traditional mass models. In this work, we apply DL architectures, including RNNs, LSTMs, and GRUs, to enhance nuclear binding energy predictions. These models dynamically adjust their internal states based on sequential dependencies, making them highly effective for modeling complex nuclear interactions. The subsequent sections will outline our experimental setup, training methodology, and performance evaluation metrics.

# C. Nuclear features as the training, validation and testing sets

The properties of an atomic nucleus are fundamentally determined by the number of protons and neutrons it contains, making them the most straightforward choice for input variables in predictive models. However, when dealing with limited datasets, incorporating additional engineered features–beyond these fundamental parameters–can significantly enhance the predictive power of NNs. These engineered features serve as priors that encode critical domain-specific information, a well-established practice in nuclear physics research (e.g., [49, 52, 56, 88]).

For instance, Ref. [88] demonstrated that supplementing ( $Z$ ) and ( $N$ ) numbers with two additional features representing pairing interactions and shell-closure effects substantially improved the accuracy of nuclear charge radius predictions compared to Bayesian models that relied solely on $N$ and $Z$ . Similarly, in Ref. [56], further enhancements were observed by incorporating two additional features that account for isospin dependence and local nuclear structure anomalies. These findings highlight the crucial role of feature engineering in improving nuclear BE predictions. In our base model, denoted as RNN3, GRU3 and LSTM3, the input space includes the number of ( $N$ ), the number of ( $Z$ ), and ( $A$ ), with the sole prediction being the nuclear mass. For RNN7, GRU7 and LSTM7, we incorporate additional bulk properties, including the mass number ( $A$ ), $A ^ { 2 / 3 }$

(from volume and surface terms), $Z ( Z - 1 ) / A ^ { 1 / 3 }$ from the Coulomb term, $( N - Z ) ^ { 2 } / A$ from the asymmetry and $\delta _ { p } = ( - 1 ) ^ { Z } + ( - 1 ) ^ { N } / 2$ and incorporate information about magic numbers. RNN11, GRU11 and LSTM11, include pairing information, $Z _ { e o }$ and $N _ { e o }$ , where $Z _ { e o }$ ( $N _ { e o }$ ) is 0 if $Z$ ( $N$ ) is even and 1 if $Z$ ( $N$ ) is odd, and ( $V _ { N }$ ) and $V _ { Z }$ ), representing number of valance nucleons. The features of the different NNs can be found in Table I. To systematically evaluate the impact of feature selection and hyperparameter optimization, we designed three NN configurations with varying input layers. The first network utilizes three input features, the second expands to seven, and the final configuration includes eleven features, aligned with the terms of the LDM to assess deviations and their influence on BE predictions.

TABLE I. Feature space in different RNNs structure.   

<table><tr><td>Model</td><td>Input x</td><td>Output y</td></tr><tr><td>RNN3, GRU3, LSTM3</td><td>N, Z, A</td><td>BE</td></tr><tr><td>RNN7, GRU7, LSTM7</td><td>N, Z, A, A2/3, Z(Z-1)/A1/3, (N-Z)2/A, δp</td><td>BE</td></tr><tr><td>RNN11, GRU11, LSTM11</td><td>N, Z, A, A2/3, Z(Z-1)/A1/3, (N-Z)2/A, δp, VN, VZ, Zeo, Neo</td><td>BE</td></tr></table>

Given that our work involves a multidimensional feature space, we employed common techniques such as grid search and random search to fine-tune the hyperparameters, as detailed in Table III.

Given the multitude of features, particularly in the domain of nuclear BE prediction using the LDM, where diverse inputs such as $N , Z , A$ , and others are considered. The choice of feature combinations is contingent upon the characteristics of our data, such as the pairing term, Coulomb, or volume and surface terms. In our investigation, we systematically explored all possible combinations through a trial-and-error approach to determine the optimal values. To achieve this, we carefully prepared our training, validation and testing sets, spanning the nuclear landscape from $Z , N \ \geq \ 8$ for absolute BE prediction, utilizing data from the AME2020. In this implementation, we explore three types of RNN architectures. Each model is designed to capture temporal dependencies in the data effectively. The models are configured with specific numbers of units in their recurrent layers: 100 for SimpleRNN and LSTM, and 80 for GRU. The activation functions used are a combination of relu and tanh, which are chosen for their ability to handle the vanishing gradient problem and provide non-linearity. The dataset used for training these models consists of input features and target values, which are split into training, validation, and test sets with varying test sizes (0.1, 0.2, 0.3). The input data is normalized using the StandardScaler to ensure optimal performance during training. Each model is compiled using the

![](images/70f1ba66063652a3910d438f05fd7b4513d3e35750ced854613110e086c46445.jpg)

![](images/02ceb88ffcdd8a3b1e2a81d7f5135e66a1dcb9cbe09b48d57dc012cf09d0926c.jpg)

![](images/395d99130ac109b98fba893d678574dc687b901fdce028703e7cf4f919345309.jpg)  
FIG. 4. Distribution of data among the training set (blue circles), validation set (green circles), and testing set (red circles) for RNN models with different splits: (a) $9 0 \%$ training, $5 \%$ validation, 5% testing, (b) 80% training, $1 0 \%$ validation, $1 0 \%$ testing, and (c) 70% training, $1 5 \%$ validation, $1 5 \%$ testing. All data sets include nuclei from AME2020 [75].

Adam optimizer and the mean squared error loss function, which is suitable for regression tasks. The training process involves feeding the scaled input data through the respective RNN layers, followed by a dense output layer that produces the final predictions. The performance of these models is evaluated based on the $\sigma$ RMSE on the validation and test sets, providing insights into how well each architecture captures the underlying patterns in the data. This comparative analysis helps in understanding the strengths and limitations of each RNN variant for the given task.

TABLE II. The hyperparameter set of the RNN, LSTM, and GRU models.   

<table><tr><td>Theith layer</td><td>Layer Type</td><td>AF</td></tr><tr><td>0</td><td>Input</td><td>-</td></tr><tr><td>1</td><td>Recurrent (RNN / LSTM / GRU)</td><td>relu, tanh</td></tr><tr><td>2</td><td>Fully Connected</td><td>relu</td></tr><tr><td>3</td><td>Output</td><td>Linear</td></tr><tr><td colspan="3">Other hyperparameters</td></tr><tr><td>Hyperparameter</td><td>Value</td><td>Property</td></tr><tr><td>Batch size</td><td>32</td><td>-</td></tr><tr><td>Objective function</td><td>MSE</td><td>Loss</td></tr><tr><td>Optimizer</td><td>Adam</td><td>-</td></tr><tr><td>Learning rate</td><td>1 × 10-3</td><td>-</td></tr></table>

# D. BE data

The dataset used in this study is based on the AME2020 compilation [75], which includes the BE of 3100 nuclei with proton and neutron numbers $Z , N \ge 8$ , encompassing both measured and extrapolated values. One of the key objectives of this work is to generate reliable predictions that can be valuable for future applications, particularly in nuclear astrophysics.

To ensure robust model evaluation, we employ multiple data partitioning strategies with varying training, validation, and testing splits: 90%-5%-5%, 80%-10%-10%, and 70%-15%-15% of the available data. In the first evaluation, we allocate 2,781 nuclei for training and 155 nuclei for testing. The second and third evaluations follow a different partitioning scheme. These different data splits allow us to assess the model’s generalization capability under varying levels of training data availability. See Fig. 4

Additionally, for validation and extrapolation, we incorporate extended datasets for different models [5, 76, 77]:

• WS model: 11,248 nuclei   
• WS3 model: 11,824 nuclei   
• WS4 model: 11,879 nuclei

These expanded datasets enable further evaluation of model performance beyond the training regime, providing insights into their predictive reliability across a broader range of nuclear masses.

# III. RESULTS AND DISCUSSION

# A. Evaluation of RNN, GRU and LSTM

To quantify how well the RNNs can describe nuclear BEs in the training, validation, and testing sets for different activation functions and learning rates, we use RNN values, the standard deviation $B E ^ { \mathrm { R N N s } }$ , and the experimental data from $\sigma$ RMSE between the predicted AME2020, defined as

![](images/0ba81a61cf2277b5a83c4c58887dda6f3ff4e30451ee5285015f4a035aefdd14.jpg)

![](images/669322658d317ab2f11f8872ffa70fdb848710777ee682782f8f7d4795516101.jpg)

![](images/34d4a1d31bcfe23362d3f44a665a0c935dd49edd63775d6f097b086dee790828.jpg)  
FIG. 5. The absolute σRMSE value of BE between RNNs predictions using RNN11, GRU11 and LSTM11 features (see Table V) for 90%,5%,5% . The $\sigma$ RMSE for all the models are also provided in Table V.

$$
\sigma_ {\mathrm {R M S E}} = \sqrt {\frac {\sum_ {i = 1} ^ {\nu} \left(B E _ {i} ^ {\mathrm {E x p}} - B E _ {i} ^ {\mathrm {R N N s}}\right) ^ {2}}{\nu}}, \tag {15}
$$

where $\nu$ is the total number of nuclei considered.

In this phase of our study, we systematically expanded the input space by introducing new terms based on the BW mass formula. This augmentation aims to enhance the predictive capabilities of our RNN models. Tables III, IV, and V provide a comprehensive evaluation of different test sizes employed across various RNN architectures.

A key observation from the results is the significant deviation in $\sigma$ RMSE for certain cases. For instance, in Table III, the GRU3 model with the relu activation function exhibits a notable deviation in the testing set $\mathrm { ~ \sim ~ } 1 . 4 2$ MeV), which is higher compared to the tanh counterpart

TABLE III. Comparison of training, validation, and testing σRMSE for RNN3, GRU3, and LSTM3 across different learning rates, model architectures, and activation functions.   

<table><tr><td>LR</td><td>Model</td><td>AF</td><td>Training</td><td>Validation</td><td>Testing</td></tr><tr><td>90%,5%,5%</td><td>RNN3</td><td>tanh</td><td>1.1584</td><td>1.1289</td><td>1.1239</td></tr><tr><td>90%,5%,5%</td><td>RNN3</td><td>relu</td><td>1.3270</td><td>1.6657</td><td>1.3647</td></tr><tr><td>90%,5%,5%</td><td>GRU3</td><td>tanh</td><td>1.0673</td><td>1.0419</td><td>1.1476</td></tr><tr><td>90%,5%,5%</td><td>GRU3</td><td>relu</td><td>1.3844</td><td>1.2734</td><td>1.4251</td></tr><tr><td>90%,5%,5%</td><td>LSTM3</td><td>tanh</td><td>1.1624</td><td>1.1299</td><td>1.2123</td></tr><tr><td>90%,5%,5%</td><td>LSTM3</td><td>relu</td><td>1.2855</td><td>1.1604</td><td>1.2555</td></tr><tr><td>80%,10%,10%</td><td>RNN3</td><td>tanh</td><td>1.2281</td><td>1.2440</td><td>1.1551</td></tr><tr><td>80%,10%,10%</td><td>RNN3</td><td>relu</td><td>1.3022</td><td>1.2619</td><td>1.4610</td></tr><tr><td>80%,10%,10%</td><td>GRU3</td><td>tanh</td><td>1.1056</td><td>1.1652</td><td>1.0758</td></tr><tr><td>80%,10%,10%</td><td>GRU3</td><td>relu</td><td>1.3304</td><td>1.3929</td><td>1.2802</td></tr><tr><td>80%,10%,10%</td><td>LSTM3</td><td>tanh</td><td>1.1861</td><td>1.2573</td><td>1.1869</td></tr><tr><td>80%,10%,10%</td><td>LSTM3</td><td>relu</td><td>1.5782</td><td>1.6672</td><td>1.6093</td></tr><tr><td>70%,15%,15%</td><td>RNN3</td><td>tanh</td><td>1.2105</td><td>1.1831</td><td>1.2231</td></tr><tr><td>70%,15%,15%</td><td>RNN3</td><td>relu</td><td>1.7970</td><td>1.6499</td><td>1.6783</td></tr><tr><td>70%,15%,15%</td><td>GRU3</td><td>tanh</td><td>1.0838</td><td>1.0930</td><td>1.0192</td></tr><tr><td>70%,15%,15%</td><td>GRU3</td><td>relu</td><td>1.3233</td><td>1.3304</td><td>1.3790</td></tr><tr><td>70%,15%,15%</td><td>LSTM3</td><td>tanh</td><td>1.2303</td><td>1.3141</td><td>1.2976</td></tr><tr><td>70%,15%,15%</td><td>LSTM3</td><td>relu</td><td>1.4853</td><td>1.3755</td><td>1.5193</td></tr></table>

TABLE V. Comparison of training, validation, and testing σRMSE for RNN11, GRU11, and LSTM11 across different learning rates, model architectures, and activation functions.   

<table><tr><td>LR</td><td>Model</td><td>AF</td><td>Training</td><td>Validation</td><td>Testing</td></tr><tr><td>90%,5%,5%</td><td>RNN11</td><td>tanh</td><td>0.4931</td><td>0.5022</td><td>0.6016</td></tr><tr><td>90%,5%,5%</td><td>RNN11</td><td>relu</td><td>0.5030</td><td>0.5388</td><td>0.5141</td></tr><tr><td>90%,5%,5%</td><td>GRU11</td><td>tanh</td><td>0.3294</td><td>0.3791</td><td>0.4591</td></tr><tr><td>90%,5%,5%</td><td>GRU11</td><td>relu</td><td>0.5618</td><td>0.5518</td><td>0.5632</td></tr><tr><td>90%,5%,5%</td><td>LSTM11</td><td>tanh</td><td>0.4817</td><td>0.5537</td><td>0.5574</td></tr><tr><td>90%,5%,5%</td><td>LSTM11</td><td>relu</td><td>0.4942</td><td>0.6965</td><td>0.6074</td></tr><tr><td>80%,10%,10%</td><td>RNN11</td><td>tanh</td><td>0.5306</td><td>0.5521</td><td>0.6023</td></tr><tr><td>80%,10%,10%</td><td>RNN11</td><td>relu</td><td>0.5707</td><td>0.5667</td><td>0.5018</td></tr><tr><td>80%,10%,10%</td><td>GRU11</td><td>tanh</td><td>0.3975</td><td>0.5045</td><td>0.4332</td></tr><tr><td>80%,10%,10%</td><td>GRU11</td><td>relu</td><td>0.4617</td><td>0.6180</td><td>0.5687</td></tr><tr><td>80%,10%,10%</td><td>LSTM11</td><td>tanh</td><td>0.5075</td><td>0.5753</td><td>0.5503</td></tr><tr><td>80%,10%,10%</td><td>LSTM11</td><td>relu</td><td>0.5326</td><td>0.7173</td><td>0.7356</td></tr><tr><td>70%,15%,15%</td><td>RNN11</td><td>tanh</td><td>0.4331</td><td>0.5071</td><td>0.5140</td></tr><tr><td>70%,15%,15%</td><td>RNN11</td><td>relu</td><td>0.5260</td><td>0.5744</td><td>0.5150</td></tr><tr><td>70%,15%,15%</td><td>GRU11</td><td>tanh</td><td>0.4057</td><td>0.5084</td><td>0.5258</td></tr><tr><td>70%,15%,15%</td><td>GRU11</td><td>relu</td><td>0.5278</td><td>0.5233</td><td>0.5272</td></tr><tr><td>70%,15%,15%</td><td>LSTM11</td><td>tanh</td><td>0.4798</td><td>0.5300</td><td>0.5791</td></tr><tr><td>70%,15%,15%</td><td>LSTM11</td><td>relu</td><td>0.4700</td><td>0.6147</td><td>0.6969</td></tr></table>

TABLE IV. Comparison of training, validation, and testing σRMSE for RNN7, GRU7, and LSTM7 across different learning rates, model architectures, and activation functions.   

<table><tr><td>LR</td><td>Model</td><td>AF</td><td>Training</td><td>Validation</td><td>Testing</td></tr><tr><td>90%,5%,5%</td><td>RNN7</td><td>tanh</td><td>0.5912</td><td>0.6490</td><td>0.6594</td></tr><tr><td>90%,5%,5%</td><td>RNN7</td><td>relu</td><td>0.7541</td><td>0.8457</td><td>0.8737</td></tr><tr><td>90%,5%,5%</td><td>GRU7</td><td>tanh</td><td>0.4447</td><td>0.4239</td><td>0.5473</td></tr><tr><td>90%,5%,5%</td><td>GRU7</td><td>relu</td><td>0.6231</td><td>0.7203</td><td>0.7988</td></tr><tr><td>90%,5%,5%</td><td>LSTM7</td><td>tanh</td><td>0.6044</td><td>0.5541</td><td>0.6492</td></tr><tr><td>90%,5%,5%</td><td>LSTM7</td><td>relu</td><td>0.8475</td><td>0.8677</td><td>1.0428</td></tr><tr><td>80%,10%,10%</td><td>RNN7</td><td>tanh</td><td>0.6633</td><td>0.7220</td><td>0.7431</td></tr><tr><td>80%,10%,10%</td><td>RNN7</td><td>relu</td><td>0.7897</td><td>0.8097</td><td>0.8413</td></tr><tr><td>80%,10%,10%</td><td>GRU7</td><td>tanh</td><td>0.5424</td><td>0.5673</td><td>0.5681</td></tr><tr><td>80%,10%,10%</td><td>GRU7</td><td>relu</td><td>0.7476</td><td>0.7817</td><td>0.7998</td></tr><tr><td>80%,10%,10%</td><td>LSTM7</td><td>tanh</td><td>0.5390</td><td>0.6568</td><td>0.6434</td></tr><tr><td>80%,10%,10%</td><td>LSTM7</td><td>relu</td><td>0.9369</td><td>1.1170</td><td>1.1298</td></tr><tr><td>70%,15%,15%</td><td>RNN7</td><td>tanh</td><td>0.7528</td><td>0.7999</td><td>0.7260</td></tr><tr><td>70%,15%,15%</td><td>RNN7</td><td>relu</td><td>0.7791</td><td>0.9288</td><td>0.8483</td></tr><tr><td>70%,15%,15%</td><td>GRU7</td><td>tanh</td><td>0.5372</td><td>0.6290</td><td>0.6152</td></tr><tr><td>70%,15%,15%</td><td>GRU7</td><td>relu</td><td>0.7914</td><td>0.9425</td><td>0.8951</td></tr><tr><td>70%,15%,15%3</td><td>LSTM7</td><td>tanh</td><td>0.5138</td><td>0.6363</td><td>0.6026</td></tr><tr><td>70%,15%,15%3</td><td>LSTM7</td><td>relu</td><td>0.9533</td><td>1.0979</td><td>1.0413</td></tr></table>

(∼ 1.15 MeV). Similarly, LSTM3 with relu activation also demonstrates relatively poor performance, reaching an σRMSE above 1.6 MeV in some cases. A substantial improvement is observed in Table IV, where RNN7 models incorporating surface and Coulomb terms lead to an approximate $5 0 \%$ reduction in error compared to RNN3. Notably, GRU7 with tanh activation achieves an σRMSE of 0.54 MeV in the testing set, contrasting with the relu activation case, which remains closer to 0.80 MeV. Moving to Table V, the most striking improvement is evident in GRU11 models. The transition from GRU3 to GRU11 results in a $6 8 . 9 \%$ reduction in $\sigma _ { \mathrm { R M S E } }$ , confirming the critical role of feature expansion. GRU11 with tanh ac-

tivation exhibits the lowest deviation, with training devation values around 0.326 MeV, whereas some RNN11 cases still hover near 0.50 MeV.

Overall, our findings suggest that GRU models outperform both standard RNN and LSTM architectures, particularly when employing the tanh activation function. The progressive enhancement from RNN3, GRU3, and LSTM3 to their respective 11-feature variants underscores the necessity of incorporating detailed nuclear properties for more accurate binding energy predictions.

Fig. 5 presents a comparative analysis of three different RNN architectures–RNN11, GRU11, and LSTM11–each utilizing 11 input features with the tanh activation function. The color gradient represents the absolute $\sigma$ RMSE in MeV, with darker shades indicating lower deviations and brighter colors (yellow-red) highlighting regions of higher error.

The error distribution shows a clear trend where deviations are more pronounced for nuclei with low proton ( $Z$ ) and neutron ( $N$ ) numbers. This is particularly evident from the red and yellow regions in the lower left of each subplot. This suggests that the models struggle more with light nuclei, likely due to stronger shell effects and nuclear structure complexities that are not fully captured by the input features. The intricate nature of magic numbers contributes to the sophisticated trends observed, underscoring the complex interplay between model features and the representation of nuclear phenomena. However, it is crucial to admit that some deviations are observed for all cases in light mass nuclei, specifically those near to $Z , N { = } 8 , 2 0$ . Regarding the performance across architectures, the GRU11 model exhibits the best overall performance, as indicated by a larger fraction of the domain covered in dark blue to purple shades, which correspond to lower $\sigma$ RMSE values.

![](images/617a7e5c0649b668a0c3cac573196882eecf093a5b0bf9f595eca0d7fbd4d53a.jpg)

![](images/b2c7ca35fe613e5816fb8ca2ccfdb2ea9be83d5942b111ae84e4960954219bda.jpg)

![](images/054f2992aad159ed039a4ec39e7fa92f93e2586383e1a4ebbb66aabff5f6b7fc.jpg)  
FIG. 6. Absolute deviations (in MeV) between the GK mass relations and the predicted masses using the RNN11, GRU11, and LSTM11 models.

The RNN11 model shows more scattered high-error regions, especially in the light-nuclei regime and near the neutron-rich dripline. So, the LSTM11 model also performs well but exhibits slightly larger deviations compared to GRU11, particularly at the neutron-rich and proton-rich extremes. The GRU11 model achieves the lowest error across most of the nuclear chart, making it the most reliable among the tested architectures.

# B. Evaluation with Garvey-Kelson relations

In this section, we emphasize the potential application of the GK mass relations [32] to validate and further analyze the BE errors of our NN models. The GK relations are known for their exceptional predictive power in nuclear mass evaluations, often yielding errors significantly lower than those found in conventional

macroscopic-microscopic or purely microscopic mass formulae. The GK relations for nuclear masses are defined as follows:

For nuclei with $N \geq Z$ :

$$
\begin{array}{l} M (Z - 2, N + 2) - M (Z, N) \\ + M (Z - 1, N) - M (Z - 2, N + 1) \\ + M (Z, N + 1) - M (Z - 1, N + 2) \approx 0, \tag {16} \\ \end{array}
$$

and for nuclei with $Z < N$ , the GK relation is given by:

$$
\begin{array}{l} M (Z + 2, N - 2) - M (Z, N) \\ + M (Z, N - 1) - M (Z + 1, N - 2) \\ + M (Z + 1, N) - M (Z + 2, N - 1) \approx 0. \tag {17} \\ \end{array}
$$

Here, $M ( Z , N )$ represents the nuclear mass for a nucleus with proton number $Z$ and neutron number $N$ .

To assess the reliability of our best-performing RNN models, we compare their predictions against the GK relations. Specifically, we evaluate the deviations of RNN11, GRU11, and LSTM11-each employing 11 input features with the tanh activation function-relative to the GK-predicted masses. The results indicate that the deviation of the GK relations from the GRU11 model is approximately 0.202 MeV, which is notably lower than the 0.327 MeV deviation obtained from LDM-based features using the tanh activation function. Similarly, the deviation for RNN11 with the GK relation is found to be 0.203 MeV, while LSTM11 exhibits a slightly higher deviation of 0.348 MeV.

The mean absolute error (MAE) for a given model is computed as follows:

$$
\mathrm {M A E} = \frac {1}{N} \sum_ {i = 1} ^ {N} \left| M _ {i} ^ {\mathrm {p r e d}} - M _ {i} ^ {\mathrm {e x p}} \right|
$$

where Mpred $M _ { i } ^ { \mathrm { p r e d } }$ and $M _ { i } ^ { \mathrm { e x p } }$ denote the predicted and experimental nuclear masses, respectively, and $N$ represents the number of nuclei in the dataset.

Table VI presents the σRMSE and MAE values obtained for training, validation, and testing phases of the RNN11, GRU11, and LSTM11 models, alongside the $\sigma _ { \mathrm { R M S E } }$ of the GK relation errors for each model.

These findings affirm that the GK relations serve as a robust benchmark, substantiating the reliability of our RNN-based mass predictions. The strong agreement, particularly with the GRU11 model, underscores the capability of NNs to capture nuclear mass systematics with high fidelity. However, further investigations are necessary to assess the model’s generalization ability in extrapolation regions, such as near the nuclear drip lines, where experimental data are sparse. See Fig. 6

![](images/b44a41a4368ac291d568cefb5a24c44918cf713b3c34e4a6ca710f881b15a036.jpg)

![](images/b370dd0eac80b4ef51c107b8b7a224034d62be4a0f552aad3d8dc3126a9e4504.jpg)

![](images/bd561f251225aabf6b4b2f66a2f458104af018ad320123fad5ce83faf186e732.jpg)

![](images/09d4a15b9edb552701bfafb65b4ef8ee8980cbb463be00860f531d9bb8a8b1a5.jpg)  
FIG. 7. Comparison of experimental single neutron separation energies with predictions from RNN11, GRU11, and LSTM11 models for 20Ca, 46Pd, 66Dy, and $^ { 7 6 }$ Os isotopes. All (σRMSE) are given in MeV.

![](images/b6a57b053b548c49237a0ae5a0a9b445d2a69298a4df81a6c0fd16b8f3e5515c.jpg)

![](images/7d8e9a06f0785900f818cb08a03035a0c5032995eaafb1409cea1ef47da3cdad.jpg)  
FIG. 8. Comparison of experimental single proton separation energies with predictions from RNN11, GRU11, and LSTM11 models for $^ { 2 0 }$ Ca, 46Pd, 66Dy, and $^ { 7 6 }$ Os isotopes. All ( $\sigma$ RMSE) are given in MeV.

# C. Evaluation of Neutron and Proton Separation Energies and Mass Excess

In pursuit of reducing the $\sigma$ RMSE discrepancy between RNNs predictions and AME2020, a secondary objective is to navigate specific mass regions. This distinction is particularly evident in the $\sigma$ RMSE variations, which represent the absolute differences in neutron separation energy ( $S _ { n }$ ) and proton separation energy ( $S _ { p }$ ) between the predictions from different RNN models and the experimental data from AME2020.

The single-neutron and single-proton separation energy curves further reinforce the importance of these terms [50]:

$$
M (Z, N) = Z M _ {p} + N M _ {n} - B (Z, N) \tag {18}
$$

$$
S _ {n} (Z, N) = B (Z, N) - B (Z, N - 1) \tag {19}
$$

$$
S _ {p} (Z, N) = B (Z, N) - B (Z - 1, N) \tag {20}
$$

where $M ( Z , N )$ represents the nuclear mass, which is related to the total binding energy $B ( Z , N )$ , and $M _ { n }$ and $M _ { p }$ denote the neutron and proton rest masses, respectively. Figs. 7, 8 and 9 compare the neutron and proton separation energies, as well as mass excess, for isotopic chains of four different elements: $^ { 2 0 }$ Ca, 46Pd, $^ { 6 6 }$ Dy, and $^ { 7 6 }$ Os isotopes. The absence of shell effects and pairing terms in the RNN, GRU, and LSTM models results in significantly larger prediction errors compared to RNN-7 and RNN-11 models, which incorporate these critical nu-

![](images/b0309c8ecb76c1031e349b8c665b10bcdcaa5b1a3e763fee8dbf0671cdf96594.jpg)

![](images/465e2b6bd8ea21a0e4d2defa28c1fa1c3cb8aea40d4d2eb68a75d0fcb385faab.jpg)

![](images/27f4d5e2aaa433132e7586c0f1bf7b346b589bdb440281a922ff387b68dbf47a.jpg)  
FIG. 9. Comparison of experimental mass excess energies with predictions from RNN11, GRU11, and LSTM11 models for 20Ca, 46Pd, 66Dy, and $^ { 7 6 }$ Os isotopes.

TABLE VI. Performance metrics of RNN11, GRU11, and LSTM11 models evaluated against the GK relations.   

<table><tr><td>Model</td><td>σRMSE (MeV)</td><td>MAE (MeV)</td><td>σRMSE (GK Errors)</td></tr><tr><td colspan="4">RNN11</td></tr><tr><td>Training</td><td>0.564</td><td>0.412</td><td>0.203</td></tr><tr><td>Validation</td><td>0.596</td><td>0.429</td><td>0.223</td></tr><tr><td>Testing</td><td>0.725</td><td>0.480</td><td>0.239</td></tr><tr><td colspan="4">GRU11</td></tr><tr><td>Training</td><td>0.506</td><td>0.358</td><td>0.202</td></tr><tr><td>Validation</td><td>0.546</td><td>0.393</td><td>0.209</td></tr><tr><td>Testing</td><td>0.624</td><td>0.412</td><td>0.228</td></tr><tr><td colspan="4">LSTM11</td></tr><tr><td>Training</td><td>0.571</td><td>0.437</td><td>0.348</td></tr><tr><td>Validation</td><td>0.705</td><td>0.507</td><td>0.342</td></tr><tr><td>Testing</td><td>0.681</td><td>0.499</td><td>0.332</td></tr></table>

clear structure effects. Therefore, it is essential to highlight the best-performing model for comparison.

The variations in $S _ { n }$ and $S _ { p }$ , as shown in Figures 5 and 6, highlight the impact of including shell and pairing terms in ML models. While most models show significant improvement when these effects are considered, small deviations remain, particularly in the GRU predictions for both $S _ { n }$ and $S _ { p }$ . These deviations suggest the need for further optimization to fully capture fine nuclear structure details.

# D. Extrapolation Capabilities

The evaluation of a model’s extrapolation capabilities is essential in nuclear physics, particularly for predicting nuclear properties beyond experimentally known regions. In this section, we assess the extrapolation performance of the RNN-based models by examining their predictions for nuclear BEs near the neutron and proton drip lines. The predictive power of the RNN-based

![](images/764033331b4894103bebe8a9add62c2077f1bb339584c2184413aff3db981ab9.jpg)  
FIG. 10. Binding energy (BE) differences between GRU11 predictions using various activation functions and the WS, WS3, and WS4 models in the extrapolation region.

models is benchmarked against established mass models, such as the WS4 model [5], which has demonstrated high accuracy in nuclear mass predictions. Several theoretical approaches, including the deformed Hartree-Fock-Bogoliubov method and nuclear density functional theory (DFT), have been widely employed to study groundstate and excited-state nuclear properties. Notably, nu-

![](images/70ef181ab25592134dd0689c7b314e595d9ba31db836fc72a2d570caa1cdec46.jpg)  
FIG. 11. Absolute σRMSE (in MeV) between WS3 and RNN11 predictions for different extrapolation regions: $8 2 \leq Z \leq 8 4$ , $1 0 0 \leq Z \leq 1 0 4$ , $1 1 0 \leq Z \leq 1 1 4$ , and $1 2 0 \leq Z \leq 1 2 3$ .

![](images/0ec842623227d4f9c351908e907241fc6df546a32c4121f6846fa0fa6424ad6d.jpg)  
FIG. 12. Absolute σRMSE (in MeV) between WS3 and GRU11 predictions for different extrapolation regions: $8 2 \leq Z \leq 8 4$ , $1 0 0 \leq Z \leq 1 0 4$ , $1 1 0 \leq Z \leq 1 1 4$ , and $1 2 0 \leq Z \leq 1 2 3$ .

clear DFT, despite utilizing a minimal set of parameters, has successfully predicted approximately 7,000 bound nuclides concerning neutron or proton emission, with this number potentially exceeding 10,000 when including continuum effects [89–91].

In macroscopic-microscopic mass models, the WS4 model has achieved precise nuclear mass descriptions by fitting 18 parameters to 2,353 experimental mass data points, reaching a remarkable accuracy of 0.298 MeV [5]. For comparison, previous studies have explored three widely used mass models-DZ, WS, and FRDMalongside the liquid-drop model (LDM). To provide a clearer perspective, we compare the $\sigma$ RMSE distribu-

![](images/18d2c38a00e01cc4608e3b8227529f4cebb3d48eda4b4bc79bff1a6cf03f4989.jpg)  
FIG. 13. Absolute σRMSE (in MeV) between WS3 and LSTM11 predictions for different extrapolation regions: $8 2 \leq$ $Z \le 8 4$ , $1 0 0 \leq Z \leq 1 0 4$ , $1 1 0 \leq Z \leq 1 1 4$ , and $1 2 0 \leq Z \leq 1 2 3$ ..

tions of WS, WS3, and WS4 across the training, validation, and testing datasets for GRU, which emerged as the best-performing model among RNN variants. A systematic analysis spanning $Z = 8$ to $Z = 1 3 2$ , covering nuclei from the proton drip line to the neutron drip line, was conducted to evaluate the ground-state BE of these nuclei. Fig. 10 illustrates the BE differences between GRU-based model and extrapolation data, highlighting discrepancies in extrapolation predictions. These findings emphasize the necessity of larger datasets to enhance predictive performance. Notably, the WS3 macroscopic-microscopic model shows significant improvement with expanded datasets, nearly matching the performance of the GRU model. The GRU model consistently demonstrates reliable and robust extrapolation capabilities, maintaining accurate predictions even in regions with sparse experimental data. The comparison between the relu and tanh activation functions for WS3 [77] and GRU-calculated BEs reveals a substantial improvement when using tanh. Specifically, the deviation for extrapolation is reduced to 0.382 MeV, as detailed in Table VII. This improvement underscores the effectiveness of the GRU model in predicting BEs for unknown nuclei near the drip lines. See Fig. 10.

To further illustrate these extrapolation capabilities, Figs. 11, 12 and 13 present $\sigma _ { \mathrm { R M S E } }$ variations across different nuclear regions, specifically for $8 2 \leq Z \leq 8 4$ , $1 0 0 \leq Z \leq 1 0 4$ , $1 1 0 \leq Z \leq 1 1 4$ , and $1 2 0 \leq Z \leq 1 2 3$ using the RNN11, GRU11, and LSTM11 models. These plots highlight the significant role of shell effects and pairing terms in improving nuclear mass predictions, with GRU consistently outperforming other models.

TABLE VII. σRMSE for different models using tanh and relu activation functions. All (σRMSE) are given in MeV.   

<table><tr><td colspan="4">tanh AF</td></tr><tr><td>Model</td><td>Training</td><td>Validation</td><td>Testing</td></tr><tr><td>WS</td><td>0.505</td><td>0.515</td><td>0.533</td></tr><tr><td>WS3</td><td>0.382</td><td>0.401</td><td>0.406</td></tr><tr><td>WS4</td><td>0.570</td><td>0.667</td><td>0.496</td></tr><tr><td colspan="4">relu AF</td></tr><tr><td>Model</td><td>Training</td><td>Validation</td><td>Testing</td></tr><tr><td>WS</td><td>0.519</td><td>0.603</td><td>0.542</td></tr><tr><td>WS3</td><td>0.477</td><td>0.533</td><td>0.478</td></tr><tr><td>WS4</td><td>0.574</td><td>0.635</td><td>0.606</td></tr></table>

# IV. CONCLUSION

In this study, we investigated the capability of RNNbased models, including GRU and LSTM, in predicting nuclear BEs and separation energies. The augmentation of features led to a substantial improvement in $\sigma _ { \mathrm { R M S } }$ between RNN-based predictions and the AME2020 data. Specifically, the inclusion of bulk properties, surface terms, and Coulomb contributions initially reduced the error from several MeV to sub-MeV levels. Further refinement by incorporating nuclear shell effects and pairing terms led to an even more significant reduction, bringing deviations down to the hundred-keV scale in the GRU model. Our results demonstrate that including these nuclear structure effects substantially enhances predictive performance, minimizing $\sigma$ RMS deviations compared to models that neglect them. A comparative analysis with established mass models such as WS3 highlights the reliability of DL approaches in nuclear mass predictions. The GRU model, in particular, exhibited superior generalization capabilities, achieving competitive σRMSE values

comparable to those of macroscopic-microscopic models while maintaining robustness across different nuclear regions. The systematic extrapolation study, spanning from $Z = 8$ to $Z = 1 3 2$ , further confirmed the model’s effectiveness in predicting nuclear masses near the neutron and proton drip lines. Additionally, we evaluated the influence of activation functions on model performance. The results indicate that using the tanh activation function yields lower σRMSE values compared to relu, particularly in WS3 and WS4 mass models. This suggests that tanh activation better captures the complex correlations in nuclear structure, enhancing predictive accuracy. The findings underscore the potential of DL techniques in nuclear physics, particularly in regions where experimental data is sparse or unavailable. While the GRU-based model provides a promising approach to nuclear mass predictions, further improvements, such as incorporating additional physical constraints or hybridizing DL with macroscopic-microscopic models, could further enhance predictive accuracy. Future work will focus on extending these models to other nuclear observables, refining hyperparameter tuning strategies, and integrating uncertainty quantification to assess the reliability of extrapolations. The integration of physics-informed NN and transfer learning could also provide new avenues for improving model generalizability across the nuclear landscape.

# ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China (Grant No. 12250410254 and No. 12175199) , the ZSTU intramural grant (Grant No. 23062211-Y).

[1] C. F. v. Weizs¨acker, Eur.Phys.J.A 96, 431 (1935).   
[2] C. v. Weizs¨acker, Zur theorie der kernmassen, Z. Phys. 96, 431 (1935).   
[3] H. A. Bethe and R. F. Bacher, Nuclear physics A, Rev. Mod. Phys.8, 82 (1936).   
[4] P. M¨oller, W. D. Myers, H. Sagawa, and S. Yoshida, Phys. Rev. Lett.108, 052501 (2012).   
[5] N. Wang, M. Liu, X. Wu, and J. Meng, Phys. Lett. B 734, 215 (2014).   
[6] Wu, X. H, Pan, C, Zhang, K. Y, Hu, J. Phys. Rev. C, 109, 024310 (2024).   
[7] Guo, Y. Y, et al. Phys. Rev. C 110: 064310 (2024).   
[8] K. Zhang, et al. At. Data Nucl. Data Tables 144, 101488 (2022).   
[9] C. Pan, et al. Phys. Rev. C 106, 014316 (2022).   
[10] Y. L. Yang, Y. K. Wang, P. W. Zhao, and Z. P. Li, Phys. Rev. C 104, 054312 (2021).   
[11] X. Meng, B. Lu, and S. Zhou, Sci. China: Phys., Mech. Astron. 63, 212011 (2020).   
[12] X. Xia, Y. Lim, P. Zhao, H. Liang, X. Qu, Y. Chen, H. Liu, L.Zhang, S. Zhang, Y. Kim, and J. Meng,At. Data

Nucl. DataTables 121-122, 1 (2018).   
[13] A. Afanasjev, S. Agbemava, D. Ray, and P. Ring, Phys. Lett. B 726, 680 (2013).   
[14] Sun, B., et al. Phys. Rev. C 78, 025806 (2008).   
[15] L. S. Geng, H. Toki, and J. Meng, Prog. Theor. Phys.113, 785 (2005).   
[16] Vretenar, Dario, et al. Physics reports 409.3-4: 101-259 (2005).   
[17] J. Dobaczewski et al., Journal of Physics G: Nuclear and Particle Physics 48, 102001 (2021).   
[18] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 93, 034337 (2016).   
[19] Wang, Ning, et al. Lett. B 734, 215-219 (2014).   
[20] Goriely, St´ephane, Nicolas Chamel, and J. M. Pearson. Phys. Rev. C 88, 061302 (2013).   
[21] P. M¨oller, W. D. Myers, H. Sagawa, and S. Yoshida, Phys. Rev. Lett.108, 052501 (2012).   
[22] J. Erler, N. Birge, M. Kortelainen, W. Nazarewicz, E. Olsen,A. M. Perhac, and M. Stoitsov, Nature (London) 486, 509 (2012).   
[23] Dutra, M., et al. Phys. Rev. C 85, 035201 (2012).

[24] Kortelainen, Markus, et al. Phys. Rev. C 82, 024313 (2010).   
[25] S. Goriely, S. Hilaire, M. Girod, and S. P´eru, Phys. Rev. Lett. 102, 242501 (2009).   
[26] J. Duflo and A. P. Zuker, Phys. Rev. C 52, R23 (1995).   
[27] Guo, S. T., et al. Phys. Rev. C 109, 014304 (2024).   
[28] Ma, C., et al. Phys. Rev. C 102, 024330 (2020).   
[29] H. Jiang, G. J. Fu, B. Sun, M. Liu, N. Wang, M. Wang, Y. G. Ma, C. J. Lin, Y. M. Zhao, Y. H. Zhang, Z. Ren, and A. Arima, Phys. Rev. C 85, 054303 (2012).   
[30] Liu, Min, et al. Phys. Rev. C 84, 014333 (2011).   
[31] P. W. Zhao, L. S. Song, B. Sun, H. Geissel, and J. Meng, Phys. Rev. C 86, 064324 (2012).   
[32] G. T. Garvey and I. Kelson, New nuclidic mass relationship, Phys.Rev.Lett. 16, 197 (1966).   
[33] J¨anecke, J., and P. J. Masson. Atomic Data and Nuclear Data Tables 39, 265-271 (1988).   
[34] Tian, Junlong, et al. Phys. Rev. C 87, 014313 (2013).   
[35] Bao, M., et al. Phys. Rev. C 88, 064325 (2013).   
[36] Boehnlein, A. et al. Colloquium: Machine learning in nuclear physics. Reviews of modern physics 94, 031003 (2022).   
[37] Wu, X.-H. and Zhao, P. Principal components of nuclear mass models. Science China Physics, Mechanics and Astronomy 67, 272011 (2024).   
[38] Lu, Y. et al. Nuclear mass predictions based on a convolutional neural network. Physical Review C 111, 014325 (2025).   
[39] Y¨uksel, E., Soydaner, D. and Bahtiyar, H. Nuclear mass predictions using machine learning models. Physical Review C 109, 064322 (2024).   
[40] Liu, H., Lei, J. and Ren, Z. Kolmogorov-Arnold networks in nuclear binding energy prediction. Physical Review C 111, 024316, doi:10.1103/PhysRevC.111.024316 (2025).   
[41] Liu, Y. et al. Improved naive Bayesian probability classifier in predictions of nuclear mass. Physical Review C 104, 014315 (2021).   
[42] Niu, Z. and Liang, H. Nuclear mass predictions with machine learning reaching the accuracy required by rprocess studies. Physical Review C 106, L021303 (2022).   
[43] Zhao, T.-L. and Zhang, H.-F. A neural network approach based on more input neurons to predict nuclear mass. Chinese Physics C 46, 044103 (2022).   
[44] Xie, J. et al. Novel Bayesian probability method in predictions of nuclear masses. Physical Review C 109, 064317 (2024).   
[45] Niu, Z., Fang, J. and Niu, Y. Comparative study of radial basis function and Bayesian neural network approaches in nuclear mass predictions. Physical Review C 100, 054311 (2019).   
[46] Gao, Z.-P. et al. Machine learning the nuclear mass. Nuclear Science and Techniques 32, 109 (2021).   
[47] Liu, G.-P., Wang, H.-L., Zhang, Z.-Z. and Liu, M.-L. Model-repair capabilities of tree-based machine-learning algorithms applied to theoretical nuclear mass models. Physical Review C 111, 024306 (2025).   
[48] Utama, R. and Piekarewicz, J. Refining mass formulas for astrophysical applications: A Bayesian neural network approach. Physical Review C 96, 044308 (2017).   
[49] Lovell, A. E., Mohan, A. T., Sprouse, T. M. and Mumpower, M. R. Nuclear masses learned from a probabilistic neural network. Physical Review C 106, 014305 (2022).

[50] Zeng, L.-X., Yin, Y.-Y., Dong, X.-X. and Geng, L.-S. Nuclear binding energies in artificial neural networks. Physical Review C 109, 034318 (2024).   
[51] Zhang, H. F., Wang, L. H., Yin, J. P., Chen, P. H. and Zhang, H. F. Performance of the Levenberg-Marquardt neural network approach in nuclear mass prediction. Journal of Physics G: Nuclear and Particle Physics 44, 045110 (2017).   
[52] Mumpower, M., Sprouse, T., Lovell, A. and Mohan, A. Physically interpretable machine learning for nuclear masses. Physical Review C 106, L021301 (2022).   
[53] He, W. et al. Machine learning in nuclear physics at low and intermediate energies. Science China Physics, Mechanics and Astronomy 66, 282001 (2023).   
[54] Wang, Y., Zhang, X., Niu, Z. and Li, Z. Study of nuclear low-lying excitation spectra with the Bayesian neural network approach. Physics Letters B 830, 137154 (2022).   
[55] Jalili, A. and Chen, A.-X. Prediction of ground state charge radius using support vector regression. New Journal of Physics 26, 103017 (2024).   
[56] X.-X. Dong, R. An, J.-X. Lu, and L.-S. Geng, Phys. Lett. B 838,137726 (2023).   
[57] D. Wu, C. L. Bai, H. Sagawa, and H. Q. Zhang,Phys.Rev.C 102, 054323 (2020).   
[58] Li, C.-Q., Tong, C.-N., Du, H.-J. and Pang, L.-G. Deep learning approach to nuclear masses and alpha-decay half-lives. Physical Review C 105, 064306 (2022).   
[59] Jalili, A., Pan, F., Draayer, J. P., Chen, A.-X. and Ren, Z. alpha-decay half-life predictions with support vector machine. Scientific Reports 14, 30776 (2024).   
[60] Jalili, A., Pan, F., Luo, Y. and Draayer, J. P. Nuclear beta-decay half-life predictions and r-process nucleosynthesis using machine learning models. Physical Review C 111, 034321 (2025).   
[61] Z. M. Niu, H. Z. Liang, B. H. Sun, W. H. Long, and Y. F. Niu, Phys.Rev.C99, 064307 (2019).   
[62] Wu, X., Ren, Z. and Zhao, P. Nuclear energy density functionals from machine learning. Physical Review C 105, L031303 (2022).   
[63] Shang, T.-S., Li, J. and Niu, Z.-M. Prediction of nuclear charge density distribution with feedback neural network. Nuclear Science and Techniques 33, 153 (2022).   
[64] Shang, T. S., Xie, H. H., Li, J. and Liang, H. Global prediction of nuclear charge density distributions using a deep neural network. Physical Review C 110, 014308 (2024).   
[65] Z.-A. Wang, J. Pei, Y. Liu, and Y. Qiang,Phys. Rev. Lett.123, 122501 (2019).   
[66] Wu, X. and Zhao, P. Predicting nuclear masses with the kernel ridge regression. Physical Review C 101, 051301 (2020).   
[67] Wu, X., Lu, Y. and Zhao, P. Multi-task learning on nuclear masses and separation energies with the kernel ridge regression. Physics Letters B 834, 137394 (2022).   
[68] Wu, X., Guo, L. and Zhao, P. Nuclear masses in extended kernel ridge regression with odd-even effects. Physics Letters B 819, 136387 (2021).   
[69] S. Dragovic, Science of the Total Environment 847, 157526 (2022).   
[70] J. Ling, G.-J. Liu, J.-L. Li, X.-C. Shen, and D.-D. You, Nuclear Science and Techniques 31, 75 (2020).   
[71] E. Zio, M. Broggi, and N. Pedroni, Progress in Nuclear Energy 51, 573 (2009).

[72] T. Adali, B. Bakal, M. K. S¨onmez, R. Fakory, and C. O. Tsaoi, Neurocomputing 15, 363 (1997).   
[73] F. Chen, X. Dong, Y. Luo, M. Yang, Y. Liu, A. Xu, J. Wang, and S. Chen, Quality and Reliability Engineering International 40, 759 (2024).   
[74] M.-D. Wang, T.-H. Lin, K.-C. Jhan, and S.-C. Wu, Progress in Nuclear Energy 140, 103928 (2021).   
[75] M. Wang, W. J. Huang, F. G. Kondev, G. Audi, and S. Naimi, Chin. Phys. C45, 030003 (2021).   
[76] Ning Wang, Min Liu and Xizhen Wu, Phys. Rev. C 81, 044322 (2010).   
[77] Min Liu, Ning Wang, Yangge Deng, Xizhen Wu, Phys. Rev. C 84, 014333 (2011).   
[78] V. Vapnik, The nature of statistical learning theory (Springer science and business media, 1999).   
[79] Jain, Anil K., Robert P. W. Duin, and Jianchang Mao. 22.1, 4-37 (2000).   
[80] Rumelhart, D. E., Hinton, G. E., and Williams, R. J. Learning representations by back-propagating errors. Nature, 323, 533-536 (1986).

[81] Hochreiter, S., and Schmidhuber, J. . Long short-term memory. Neural Computation, 9(8), 1735-1780 (1997).   
[82] Graves, Alex. Supervised sequence labeling. Springer Berlin Heidelberg, (2012).   
[83] Goodfellow, I., Bengio, Y., and Courville, A. . Deep learning. MIT Press (2016).   
[84] M. W. Kirson, Nuclear Physics A 798, 29 (2008).   
[85] Schmidhuber, J.: Deep learning in neural networks: An overview, Neural Networks, 61, 85-117, (2015).   
[86] Lipton, Zachary C., John Berkowitz, and Charles Elkan. arXiv preprint arXiv:1506.00019 (2015).   
[87] Rezaeianjouybari, Behnoush, and Yi Shang. Measurement 163, 107929 (2020).   
[88] X.-X. Dong, R. An, J.-X. Lu, and L.-S. Geng,Phys. Rev. C105, 014308 (2022).   
[89] Erler J, Birge N, Kortelainen M, Nazarewicz W, Olsen E, Perhac A M and Stoitsov M Nature 486 509-512 (2012).   
[90] Afanasjev A, Agbemava S, Ray D and Ring P Phys. Lett. B 726 680-684 (2013).   
[91] Agbemava S E, Afanasjev A V, Ray D and Ring P Phys. Rev. C 89 054320-37 (2014).