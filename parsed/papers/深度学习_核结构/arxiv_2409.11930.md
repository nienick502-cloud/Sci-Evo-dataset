# Optimization of Nuclear Mass Models Using Algorithms and Neural Networks

Jin Li ∗1 and Hang Yang †1

1School of Science, Zhejiang Sci-Tech University, Hangzhou 310018, China

# Abstract

Taking into account nucleon-nucleon gravitational interaction, higher-order terms of symmetry energy, pairing interaction, and neural network corrections, a new BW4 mass model has been developed, which more accurately reflects the contributions of various terms to the binding energy. A novel hybrid algorithm and neural network correction method has been implemented to optimize the discrepancy between theoretical and experimental results, significantly improving the model’s binding energy predictions (reduced to around $3 5 0 \mathrm { k e V } _ { , }$ ). At the same time, the theoretical accuracy near magic nuclei has been marginally enhanced, effectively capturing the special interaction effects around magic nuclei and showing good agreement with experimental data.

# 1 Introduction

The nuclear mass, as one of the fundamental physical properties of atomic nuclei, contains abundant information about nuclear structure [1]. Changes in nuclear mass not only directly affect the stability of atomic nuclei but also play a crucial role in the energy release during nuclear reactions. In particular, for neutron-rich nuclei, their mass is a critical input parameter for the rapid neutron capture process (r-process) in stellar nucleosynthesis processes, and studying it helps in gaining a comprehensive understanding of the formation and evolution of elements in the universe [2, 3, 4, 5]. In recent years, with the ongoing advancements of radioactive ion beam facilities, the masses of over 3000 ground-state nuclei have been experimentally measured, and the experimental measurement scope is gradually extending to both sides of the $\beta$ -stability line [6, 7]. Since astrophysical research requires a large amount of nuclear mass data for neutron-rich or neutron-deficient nuclei far from the stability line, which remains challenging to measure directly with current technology, many different types of nuclear mass models have been proposed to address the limitations of existing experimental techniques.

The semi-empirical mass formula proposed by Bethe and Weizs?cker in the early days had a mass prediction accuracy of approximately 3 MeV [8, 9, 10]. The Strutinsky energy theorem [11] states that nuclear binding energy can be divided into two parts: one large and smooth, and the other small and oscillatory. Due to its limitations, the classical liquid drop model can only explain smooth trends but fails to account for the rapid oscillations in binding energy around shell gaps as a function of proton and neutron numbers. This suggests that some important physical effects are missing from the classical model [12, 13]. To address this issue, physicists developed macroscopic-microscopic models by introducing shell corrections. These models include the Finite-Range Droplet Model (FRDM) [14], the Koura-Tachibana-Uno-Yamada (KTUY) model [15], the Lublin Strasbourg Drop (LSD) model [16], and the Weizsacker-Skyrme (WS) mass model [17]. In addition, there are microscopic

mass models based on Density Functional Theory (DFT) [18], such as the Hartree-Fock-Bogoliubov (HFB) [19] method and the Relativistic Mean Field (RMF) theory [20]. Although these theoretical models are more complex, they possess better extrapolation capabilities and can describe nuclear mass and structure more accurately.

To address issues such as the lack of physical effects and overfitting in early semi-empirical mass formulas, Professor Kirson’s team introduced six physical terms into the model, including the exchange Coulomb term, surface symmetry term, and shell effects term [21, 22, 23, 24, 25, 26, 27]. These physical constraints significantly improved the accuracy of the model, and the resulting BW2 mass model partially addressed the original issues. Furthermore, thanks to the ability of machine learning to handle complex problems, the BW2 model has found wide application in nuclear physics, such as predicting half-lives, charge radii, and charge densities [28, 29, 30, 31, 32].

Neural Networks are an important method in machine learning, inspired by the structure and function of biological neural systems. They consist of a series of interconnected artificial neurons, simulating the brain’s learning process by adjusting connection weights. Neural networks are particularly adept at handling complex nonlinear relationships and high-dimensional data, and are thus widely used in fields such as image recognition, natural language processing, and predictive analytics [33]. In the optimization of nuclear mass models, neural networks can effectively capture the complex relationships within nuclear physics data. Traditional nuclear mass models may be limited by parameter selection and model assumptions, while neural networks, through training on large datasets, can adaptively adjust the model structure and parameters, improving accuracy and revealing underlying patterns and trends in nuclear mass [34, 35]. By incorporating neural networks to optimize nuclear mass models, not only can the performance of existing models be improved, but new ideas and methods for nuclear physics research can also be provided.

This work is based on the BW2 nuclear mass model. By introducing higher-order terms for symmetry energy, gravitational terms, and pairing interaction terms, combined with neural network-based model corrections, we have developed a new BW4 nuclear mass model. To verify the accuracy and performance of the model and method, we conducted detailed testing and analysis. The structure of the rest of this paper is as follows: In Section 2, we introduce the nuclear mass model, the principles of the algorithm, and the fundamentals of neural networks. In Section 3, we first introduce the evaluation metrics for model performance and analyze the performance improvements of the BW4 mass model under the optimization of the algorithm and neural network, from a local to global perspective. The final section provides a conclusion.

# 2 Mass Model and Algorithm

# 2.1 BW2 Mass Model

The BW2 mass model [36] is based on the classical liquid drop model, and by adding six physical terms as multiple constraints, it optimizes the deviations of the semi-empirical mass formula to a certain extent. The BW2 mass model is as follows:

$$
\begin{array}{l} B E _ {\mathrm {B W 2}} = \alpha_ {r} A + \alpha_ {s} A ^ {\frac {2}{3}} + \alpha_ {c} \frac {Z ^ {2}}{A ^ {\frac {1}{3}}} + \alpha_ {t} \frac {(N - Z) ^ {2}}{A} + \alpha_ {p} \frac {Z ^ {\frac {4}{3}}}{A ^ {\frac {1}{3}}} \\ + \alpha_ {\mathrm {c c}} \frac {| N - Z |}{A} + \alpha_ {\mathrm {s x}} \frac {(N - Z) ^ {2}}{A ^ {\frac {4}{3}}} + \alpha_ {\mathrm {s o}} \delta A ^ {- \frac {1}{2}} \tag {1} \\ + \alpha_ {\pi} A ^ {\frac {1}{3}} + \alpha_ {m} P + \beta_ {m} P ^ {2} \\ \end{array}
$$

Equation (1) contains 11 fitting coefficients. Here,

$$
P = \frac {v _ {n} v _ {p}}{v _ {n} + v _ {p}},
$$

$$
\delta (N,Z) = \frac{[(-1)^{N} + (-1)^{Z}]}{2},
$$

represent the differences between the actual proton number (Z) and neutron number (N) and the nearest magic numbers, respectively.

# 2.2 Improvements in the Mass Model

By considering the Fermi gas model to explain the binding energy of nucleons, we introduced higher-order terms for the symmetry energy

$$
\alpha_ {\mathrm {t m}} \frac {(N - Z) ^ {4}}{A ^ {3}}.
$$

Here,

$$
\alpha_ {\mathrm {t m}} = \frac {1}{1 6 2} \left(\frac {9 \pi}{8}\right) ^ {2 / 3} \frac {\hbar^ {2}}{m r _ {0} ^ {2}}
$$

represents the modified Planck constant, while $m$ and $r _ { 0 }$ denote the mass and radius of the nucleon, respectively.

Gravity is the most important interaction between objects on a macroscopic scale, and its range is infinite. Although the influence of gravity weakens as objects move farther apart, the gravitational interaction between nucleons in the liquid drop model cannot simply be ignored. Its expression is defined as:

$$
B E _ {g} = \alpha_ {g} \frac {A (A - 1)}{A ^ {1 / 3}},
$$

$\alpha _ { g }$ is the fitting coefficient for the gravitational term.

Additionally, we found that in atomic nuclei, nuclei with an even number of nucleons tend to be more stable than those with an odd number of nucleons. Even-numbered nucleons can pair up, while odd-numbered nucleons cannot fully pair. Therefore, we considered introducing a pairing interaction term to make the overall model more stable. The form of the pairing interaction term is:

$$
B E _ {\mathrm {p m}} = \alpha_ {\mathrm {p m}} A ^ {- 1 / 3} \delta_ {\mathrm {p m}},
$$

$$
\delta_ {\mathrm {p m}} = \left\{ \begin{array}{l l} 2 - \left| \frac {N - Z}{A} \right|, & \mathrm {N a n d Z e v e n} \\ \left| \frac {N - Z}{A} \right|, & \mathrm {N a n d Z o d d} \\ 1 - \left| \frac {N - Z}{A} \right|, & \mathrm {N e v e n , Z o d d , N > Z} \\ 1 - \frac {| N - Z |}{4 A}, & \mathrm {N o d d , Z e v e n , N <   Z} \\ 1, & \mathrm {N e v e n , Z o d d , N <   Z} \\ 1, & \mathrm {N o d d , Z e v e n , N > Z} \end{array} \right.
$$

The aforementioned section explains the large and smooth part of the liquid drop model, which is defined as $B E _ { \mathrm { L D M } }$ . However, the explanation for the small and oscillatory part is not ideal. Therefore, we introduced a neural network correction term to account for the small and oscillatory part. This term is defined as $\delta _ { \mathrm { N N } }$ .

After adding the aforementioned terms, we obtained a new mass model, BW4, as shown in Equation (2):

$$
\begin{array}{l} B E _ {\mathrm {B W 4}} = \alpha_ {r} A + \alpha_ {s} A ^ {\frac {2}{3}} + \alpha_ {c} \frac {Z ^ {2}}{A ^ {\frac {1}{3}}} + \alpha_ {t} \frac {(N - Z) ^ {2}}{A} + \alpha_ {p} \frac {Z ^ {4 / 3}}{A ^ {1 / 3}} \\ + \alpha_ {\mathrm {c c}} \frac {| N - Z |}{A} + \alpha_ {\mathrm {s x}} \frac {(N - Z) ^ {2}}{A ^ {4 / 3}} + \alpha_ {\mathrm {s o}} \delta A ^ {- 1 / 2} \\ + \alpha_ {\pi} A ^ {1 / 3} + \alpha_ {m} P + \beta_ {m} P ^ {2} + \alpha_ {\mathrm {t m}} \frac {(N - Z) ^ {4}}{A ^ {3}} \\ + \alpha_ {g} \frac {A (A - 1)}{A ^ {1 / 3}} + \alpha_ {\mathrm {p m}} A ^ {- 1 / 3} \delta_ {\mathrm {p m}} + \delta_ {\mathrm {N N}} \\ \end{array}
$$

# 2.3 Algorithm Principles

In this paper, we selected the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm and Sequential Least Squares Programming (SLSQP) for optimizing the coefficients of the BW4 mass model, and compared them with the commonly used least squares method [35, 36, 37, 38, 39, 40, 41, 42].

# 2.3.1 SLSQP

For solving constrained optimization problems (COP), SLSQP fully utilizes gradient and Hessian matrix information, allowing it to converge to the optimal solution more quickly. For any COP:

$$
\min  _ {\vec {x} \in X} f (\vec {x}) \quad \text {s . t .} \quad g (\vec {x}) = 0, \quad h (\vec {x}) \geq 0 \tag {3}
$$

where ${ \vec { x } } = \left( x _ { 1 } , x _ { 2 } , x _ { 3 } , . ~ . ~ , x _ { k } \right)$ , with $X = \{ \vec { x } \ | \ \vec { l } \leq \vec { x } \leq \vec { u } \}$ , $\Vec { l } = ( l _ { 1 } , l _ { 2 } , l _ { 3 } , \ldots , l _ { i } )$ , and $\vec { u } =$ $( u _ { 1 } , u _ { 2 } , u _ { 3 } , \ldots , u _ { j } )$ . Here, $\vec { x }$ represents the solution vector of the problem, $X$ is the vector space of the solution, $\vec { l , u }$ are the lower and upper boundary constraints of the solution space, $g ( \vec { x } )$ represents the equality constraint, $h ( \vec { x } )$ represents the inequality constraint, and $f ( \vec { x } )$ is the objective function to be optimized [43]. SLSQP finds the minimum of the objective function under constraints through iterative optimization. During each iteration, the gradient and Hessian matrix [42] of the objective function are computed to determine the search direction, and a linear approximation model is employed to update the current solution. Meanwhile, the satisfaction of constraints is also taken into account, and constraints are addressed by introducing Lagrange multipliers:

$$
L (\vec {x}, \vec {\lambda}, \vec {\mu}) = f (\vec {x}) + \vec {\lambda} ^ {T} * g (\vec {x}) + \vec {\mu} ^ {T} * h (\vec {x})
$$

Here, the superscript $T$ denotes the transpose of the vector, $\vec { \lambda }$ and $\vec { \mu }$ represent the penalty terms for equality and inequality constraints, respectively [44]. By solving the unconstrained least squares problem, the update rule for each iteration is obtained. This rule must satisfy not only the equality and inequality constraints but also the first-order necessary conditions:

$$
\nabla L (\vec {x}, \vec {\lambda}, \vec {\mu}) = \nabla f (\vec {x}) + J _ {g} ^ {T} * \vec {\lambda} + J _ {h} ^ {T} * \vec {\mu} = 0 (5)
$$

Here, $J _ { g }$ and $J _ { h }$ represent the Jacobian matrices of the equality and inequality constraint functions, respectively [45]. According to the aforementioned update rule, the initial value ${ \vec { x } } _ { 1 }$ is selected, and the stopping criterion is defined; the gradient vector $\bar { \nabla } f _ { k } ( \vec { x } _ { k } )$ is calculated, where $k$ represents the current iteration number. If $\| \nabla f _ { k } ( \bar { x _ { k } } ) \| < \epsilon$ , the algorithm terminates, yielding the approximate solution ${ \vec { x } } ^ { * }$ , where $\epsilon$ is the predefined stopping criterion. We construct a second-order sequential quadratic programming (SQP) model:

$$
\min  [ q (\vec {x}) ] = \min  \left[ f _ {k} (\vec {x}) + g _ {k} ^ {T} (\vec {x} - \vec {x} _ {k}) + \frac {1}{2} (\vec {x} - \vec {x} _ {k}) ^ {T} B _ {k} (\vec {x} - \vec {x} _ {k}) \right]
$$

$$
\begin{array}{l} \text {s . t .} \quad \left\{ \begin{array}{l} A _ {\mathrm {e q}} (\vec {x} - \vec {x} _ {0}) = 0 \\ g _ {k} (\vec {x}) \geq 0, k = 1, 2, \dots , k \end{array} \right. \end{array} \tag {6}
$$

Here, $B _ { k }$ is a positive definite symmetric matrix that approximates the inverse of the Hessian matrix, and $A _ { \mathrm { { e q } } }$ represents the Jacobian matrix of the equality constraints. Solving the sequential quadratic programming (SQP) model provides the correction direction $\Delta \vec { x }$ ; subsequently, the step size $\alpha$ is calculated to guarantee adequate descent of the objective function in the search direction:

$$
\alpha = \min  (1, r ^ {c})
$$

$$
r = \max  \left(\beta_ {s}, r _ {t}\right)
$$

$$
\beta_ {s} = \left(\frac {\partial f}{\partial \vec {x}}\right) ^ {T} (\Delta \vec {x} / s)
$$

$$
r _ {t} = \left(\frac {\partial g}{\partial \vec {x}}\right) ^ {T} (\Delta \vec {x} / t) \tag {7}
$$

$s$ and $t$ are positive scaling factors. Finally, the estimated point is updated as $\vec { x } _ { k + 1 } = \vec { x } _ { k } + \alpha \Delta \vec { x }$ . By solving the aforementioned system of equations, the optimal solution for the first iteration can be obtained. Following this iterative process, the objective function is gradually optimized, and the optimal solution that satisfies the constraints is found.

# 2.3.2 BFGS

BFGS (Broyden-Fletcher-Goldfarb-Shanno) is a quasi-Newton method for numerical optimization.

For any quasi-Newton equation:

$$
\nabla f (\vec {x} _ {k}) = \nabla f (\vec {x} _ {k + 1}) + G _ {k + 1} ^ {*} (\vec {x} _ {k} - \vec {x} _ {k + 1})
$$

By rearranging terms:

$$
G _ {k + 1} ^ {*} (\vec {x} _ {k + 1} - \vec {x} _ {k}) = \nabla f (\vec {x} _ {k + 1}) - \nabla f (\vec {x} _ {k})
$$

Let $H _ { k + 1 } \approx G _ { k + 1 }$ , we get:

$$
H _ {k + 1} ^ {*} (\vec {x} _ {k + 1} - \vec {x} _ {k}) = \nabla f (\vec {x} _ {k + 1}) - \nabla f (\vec {x} _ {k})
$$

It is usually assumed in BFGS that:

$$
H _ {k + 1} = H _ {k} + E _ {k}
$$

Let’s assume that:

$$
E _ {k} = \alpha_ {k} u _ {k} u _ {k} ^ {T} + \beta_ {k} v _ {k} v _ {k} ^ {T}
$$

Here, $u _ { k }$ and $v _ { k }$ are both $n \times 1$ vectors:

$$
y _ {k} = \nabla f (\vec {x} _ {k + 1}) - \nabla f (\vec {x} _ {k}), \quad s _ {k} = \vec {x} _ {k + 1} - \vec {x} _ {k}
$$

$$
u _ {k} = r H _ {k} s _ {k}, \quad v _ {k} = \theta y _ {k}
$$

Substituting into the original equation, it can be written as:

$$
\begin{array}{l} \Rightarrow \alpha \left(u _ {k} ^ {T} s _ {k}\right) u _ {k} + \beta \left(v _ {k} ^ {T} s _ {k}\right) v _ {k} = y _ {k} - H _ {k} s _ {k} \\ \Rightarrow \alpha \left(\left(H _ {k} s _ {k}\right) ^ {T} s _ {k}\right) H _ {k} s _ {k} + \beta \left(\left(\theta y _ {k}\right) ^ {T} s _ {k}\right) \left(\theta y _ {k}\right) - v _ {k} + H _ {k} s _ {k} = 0 \\ \Rightarrow \alpha \left(\left(H _ {k} s _ {k}\right) ^ {T} s _ {k}\right) H _ {k} s _ {k} + \beta \left(\left(\theta y _ {k}\right) ^ {T} s _ {k}\right) \left(\theta y _ {k}\right) - \left(y _ {k} - H _ {k} s _ {k}\right) = 0 \\ \Rightarrow \alpha \left(\left(H _ {k} s _ {k}\right) ^ {T} s _ {k}\right) \left(H _ {k} s _ {k}\right) + \beta \left(\theta^ {2} \left(y _ {k} ^ {T} s _ {k}\right) + 1\right) \left(H _ {k} s _ {k}\right) = 0 \\ \Rightarrow \alpha r ^ {2} = - \frac {1}{s _ {k} ^ {T} H _ {k} s _ {k}}, \quad \beta \theta^ {2} = \frac {1}{y _ {k} ^ {T} s _ {k}} \\ H _ {k + 1} = H _ {k} + \frac {H _ {k} s _ {k} s _ {k} ^ {T} H _ {k}}{s _ {k} ^ {T} H _ {k} s _ {k}} - \frac {y _ {k} y _ {k} ^ {T}}{y _ {k} ^ {T} s _ {k}} \\ \end{array}
$$

The algorithm proceeds through the following steps: first, initialization, then calculating the gradient of the objective function and updating the search direction; after selecting an appropriate step size, the parameters are updated, followed by updating the inverse Hessian matrix. Next, it checks whether the termination condition is satisfied; if not, the iteration continues until the preset conditions are met, and the final result is obtained [46].

# 2.4 Principles of Neural Networks

# 2.4.1 KANs

Kolmogorov-Arnold Networks (KANs) are a new type of neural network inspired by the Kolmogorov-Arnold representation theorem, which states that any multivariable continuous function $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n - 1 } , x _ { n } )$ on a bounded domain can be expressed as a finite combination of univariate continuous functions and addition operations:

$$
f \left(x _ {1}, x _ {2}, \dots , x _ {n - 1}, x _ {n}\right) = \sum_ {q = 1} ^ {2 n + 1} \Phi_ {q} \left(\sum_ {p = 1} ^ {n} \varphi_ {q, p} \left(x _ {p}\right)\right)
$$

Here, $\varphi _ { q , p }$ and $\Phi _ { q }$ represent univariate functions. This implies that multivariable functions can be expressed via univariate functions and addition, reducing the complexity of high-dimensional functions.

KANs consist of multiple layers, where each layer is made up of a set of univariate functions φq,p $\varphi _ { q , p }$ parameterized as B-spline curves with trainable coefficients. The connections between layers are not fixed activation functions but are learnable activation functions, represented by B-splines and parameterized as local B-spline basis functions.

# 2.4.2 LSTM

Long Short-Term Memory (LSTM) is a specialized type of recurrent neural network (RNN) initially designed for processing and predicting time series data. However, LSTM’s unique properties also give it an advantage in non-time series tasks. As an enhanced network, it effectively captures complex dependencies in the input data.

An LSTM network consists of multiple LSTM units, each of which includes a cell state (Cell State), an input gate (Input Gate), a forget gate (Forget Gate), and an output gate (Output Gate). The cell state is the central component of the LSTM unit, responsible for storing information and transmitting it across different time steps (or sequential steps). The gating mechanism governs the update and maintenance of the cell state, enabling the LSTM to effectively remember long-term dependencies.

The LSTM’s gating mechanism consists of three gates: the input gate, the forget gate, and the output gate. Each gate is governed by a Sigmoid activation function, whose output values range between 0 and 1, determining the retention or discarding of information [47].

The forget gate determines how much information should be forgotten from the current cell state. The formula is:

$$
f _ {t} = \sigma \left(W _ {f} \left[ h _ {t - 1}, x _ {t} \right] + b _ {f}\right)
$$

Here, $f _ { t }$ is the output of the forget gate, $\sigma$ is the Sigmoid activation function, $W _ { f }$ and $b _ { f }$ represent the weight matrix and bias vector of the forget gate, $h _ { t - 1 }$ denotes the hidden state from the previous time step, and $x _ { t }$ is the current input. The input gate determines which new information should be added to the cell state. The formula is:

$$
i _ {t} = \sigma \left(W _ {i} \left[ h _ {t - 1}, x _ {t} \right] + b _ {i}\right)
$$

The new candidate information is produced by a tanh layer:

$$
\tilde {C} _ {t} = \tanh  \left(W _ {c} \left[ h _ {t - 1}, x _ {t} \right] + b _ {c}\right)
$$

Then, the cell state is updated together with the input gate:

$$
C _ {t} = f _ {t} * C _ {t - 1} + i _ {t} * \tilde {C} _ {t}
$$

The output gate decides which information will be output from the cell state. The formula is:

$$
O _ {t} = \sigma \left(W _ {o} \left[ h _ {t - 1}, x _ {t} \right] + b _ {o}\right)
$$

The final output, along with the cell state, is processed through a tanh layer:

$$
h _ {t} = o _ {t} * \tanh (C _ {t})
$$

When processing non-time series data, LSTM enhances model performance by capturing the sequential dependencies and relationships between the upper and lower parts of the input data.

# 3 Results and discussions

We enhanced the overall stability of the model by considering the analysis of binding energy using the Fermi gas model, the gravitational interaction between nucleons, and incorporating a pairing interaction term. Building on the above neural network principles, we trained a neural network model on the residuals of the binding energy to obtain the necessary neural network correction term, ultimately developing the BW4 mass model.

# 3.1 Model Performance Metrics

The performance of the mass model is evaluated based on the root mean square deviation (RMSD), as defined in Equation (4):

$$
\mathrm {R M S D} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} \left(B E _ {\mathrm {E x} _ {i}} - B E _ {\mathrm {T h} _ {i}}\right) ^ {2}} \tag {4}
$$

Here, $n$ denotes the total number of nuclides involved in the calculation, and $B E _ { \mathrm { E x } _ { i } }$ and $B E _ { \mathrm { T h } _ { i } }$ represent the experimental binding energy and theoretical model value for each nuclide, respectively.

# 3.2 Optimization of $B E _ { \mathbf { L D M } }$

For the $B E _ { \mathrm { L D M } }$ component of the BW4 mass model, we optimized using multiple algorithms, conducted relevant calculations on the dataset, and fitted the optimal coefficients for each term under the current algorithm, as shown in Figure 1.

![](images/afd2ea0ff1bca7fa7000ac1665bf7686e68b5f4b2b5166858748108502457048.jpg)

![](images/c2678d1f00e4c000c5b562227ef57178055c9f33d62d1782692e6704b5565419.jpg)

![](images/684ebd199879ba019c188b3768c934f03235350c2e2d83cbc3815dedb6343534.jpg)

![](images/9c5d10555effae0f237e574725c7eed5bf0f8f0b997489e84ac045b865a3ef0f.jpg)  
Figure 1: Optimal coefficients for $B E _ { \mathrm { L D M } }$ and RMSD across different algorithms (Unit: MeV)

Figure 1 presents the coefficients obtained from algorithms like BFGS and SLSQP. Compared to Least Squares, the other algorithms have caused changes in the weights of the model terms, as reflected in the table. The magnitude of the weights indicates the degree of each term’s influence on the overall model, while the sign of each coefficient indicates whether it contributes a positive or negative correction to the model. We focus on the high performance of BFGS $( \mathrm { R M S D } = 1 . 6 2 6 \mathrm { M e V } )$ and SLSQP $( \mathrm { R M S D } = 1 . 6 2 7 \ \mathrm { M e V } )$ in Figure 1. In these two algorithms, the exchange Coulomb term, surface symmetry term, higher-order symmetry energy term, and pairing correction term significantly affect the model, resulting in higher weights, while other terms have smaller impacts and thus lower weights. Hence, these algorithms result in a lower root mean square deviation (RMSD) compared to the others.

Additionally, we focus on the performance of $B E _ { \mathrm { L D M } }$ on double magic isotope chains. Figure 2 illustrates the performance of $B E _ { \mathrm { L D M } }$ on different isotope chains (Ca, Ni, Sn, and Pb) under various algorithms (BFGS, Least Squares, SLSQP). The x-axis represents the neutron number, and the y-axis shows the relative error between the experimental values and theoretical calculations.

![](images/1a878f8ec7dc14dd5c2c7a99cb67afb9401665c7051cc03c16961e3b29df50d4.jpg)

![](images/c0c949f33f33001804eac694dcda59e70a67903e7367a049c0d588361515a331.jpg)  
Figure 2: The relative error between the experimental and theoretical values of $B E _ { \mathrm { L D M } }$ for the isotope chains of Ca, Ni, Sn, and Pb.

Figure 2(a) illustrates the optimization performance of three algorithms along the Ca isotope chain. Overall, the Least Squares algorithm outperforms the SLSQP and BFGS algorithms in terms of deviation from experimental values, while the SLSQP and BFGS algorithms show similar performance. At $N = 2 0$ , the error between the Least Squares algorithm and the SLSQP and BFGS algorithms shows a significant divergence from the experimental values. The Least Squares algorithm yields a deviation of $- 1 . 5 7 9 \mathrm { M e V }$ at $N = 2 0$ , whereas the SLSQP and BFGS algorithms produce deviations of -4.257 MeV and $- 4 . 2 4 3 \mathrm { M e V }$ , respectively. However, at $N = 2 8$ , the deviations from the experimental values are minimal across the three algorithms, with the Least Squares, SLSQP, and BFGS algorithms showing deviations of 1.805 MeV, 1.793 MeV, and $1 . 8 2 6 \mathrm { M e V } ,$ , respectively.

Figure 2(b) presents the optimization of the Ni isotope chain using the three algorithms, where the Least Squares algorithm outperforms the SLSQP and BFGS algorithms before $_ { \mathrm { N } = 2 8 }$ . At $_ { \mathrm { N } = 2 8 }$ , the Least Squares algorithm reaches its largest deviation from the experimental value, at 2.759 MeV, while the deviations for the SLSQP and BFGS algorithms are $- 0 . 0 2 5 \mathrm { M e V }$ and -0.047 MeV, respectively. At $\Nu { = } 5 0$ , the SLSQP and BFGS algorithms outperform the Least Squares algorithm, with deviations of 0.878 MeV, 0.865 MeV, and 2.322 MeV, respectively. However, overall, the Least Squares algorithm provides better optimization for the Ni isotope chain, with the SLSQP and BFGS algorithms yielding comparable results.

Figure 2(c) demonstrates the optimization performance of the three algorithms for Sn. For $_ { \mathrm { N } < 5 7 }$ and $N { > } 7 5$ , the SLSQP and BFGS algorithms show better performance than the Least Squares algorithm. At $\Nu { = } 5 0$ and ${ \bf N } { = } 8 2$ , the Least Squares algorithm shows its largest deviations from the experimental values, with deviations of $8 . 1 3 7 \mathrm { M e V }$ and 9.091 MeV, respectively. However, for the SLSQP and BFGS algorithms, the deviations from the experimental values at these neutron magic numbers are $5 . 3 9 7 ~ \mathrm { M e V }$ and $7 . 1 1 9 \ \mathrm { M e V } ,$ , and $5 . 3 2 ~ \mathrm { M e V }$ and $7 . 0 7 6 ~ \mathrm { M e V } ,$ , respectively. The SLSQP and BFGS algorithms provide better optimization for Sn than the Least Squares algorithm, though their performance remains quite similar to each other.

Figure 2(d) presents the optimization results for Pb using the three algorithms. At $N { = } 1 2 6$ , the Least Squares algorithm performs worse than the SLSQP and BFGS algorithms, showing a deviation of 7.606 MeV from the experimental value, while the SLSQP and BFGS algorithms achieve deviations of 5.927 MeV and $5 . 8 6 7 \mathrm { M e V } ,$ , respectively. However, overall, the Least Squares algorithm demonstrates better optimization performance for Pb compared to the SLSQP and BFGS algorithms, while the performance results between SLSQP and BFGS remain comparable.

# 3.3 Optimized $B E _ { \mathbf { L D M } }$ Model with Neural Network-Based $\delta _ { N n }$ Correction Term

In the previous section, the optimized $B E _ { \mathrm { L D M } }$ partially reduced the gap between theoretical and experimental values. However, the classical liquid drop model (LDM), due to its inherent limitations, can only capture broad, smooth trends, and is unable to explain the rapid fluctuations in binding energy near shell gaps as a function of proton and neutron numbers. Therefore, we introduce a neural network correction to account for the small-scale fluctuations, enabling the theoretical values predicted by the mass model to better align with experimental data. Accordingly, we incorporate a neural network correction term $( \delta _ { N n } )$ to approximate the small, fluctuating components as indicated by the Strutinsky energy theorem.

The dataset was divided into a 7:3 split, consisting of 2275 training samples and 975 testing samples. A neural network model was trained on the binding energy residuals to develop the neural network correction term $( \delta _ { N n } )$ for the model. The final performance of the optimized $B E _ { \mathrm { L D M } } +$ Neural Network Correction Term $( \delta _ { N n } )$ in the BW4 mass model across different datasets is presented in Table 1.

LSTM demonstrated strong performance across the overall dataset when applied with different optimization algorithms. For instance, with the Least Squares optimization algorithm, LSTM achieved a root mean square deviation (RMSD) of 0.221, which was notably lower than other algorithm combinations. SLSQP and BFGS also exhibited strong performance when combined with LSTM, yielding RMSDs of 0.236 and 0.233, respectively. Additionally, KANs and GPR models demonstrated error reduction when paired with different optimization algorithms, though not as pronounced as LSTM. In the training set, the Least Squares $^ +$ LSTM model exhibited the lowest RMSD of 0.124, demonstrating superior fitting capability. The RMSD values for the $\mathrm { S L S Q P + L S T M }$ and BFGS $^ +$ LSTM models were also relatively low, at 0.150 and 0.155, respectively.

Table 1: Performance of the BW4 Mass Model Across Datasets (Unit: MeV)   

<table><tr><td colspan="5">Full Set (3250 nuclei)</td></tr><tr><td>Unit (MeV)</td><td>None</td><td>KAN</td><td>GPR</td><td>LSTM</td></tr><tr><td>Least Squares</td><td>1.822</td><td>0.231</td><td>0.229</td><td>0.221</td></tr><tr><td>SLSQP</td><td>1.627</td><td>0.649</td><td>0.333</td><td>0.236</td></tr><tr><td>BFGS</td><td>1.626</td><td>0.522</td><td>0.287</td><td>0.233</td></tr></table>

<table><tr><td colspan="5">Train Set (2275 nuclei)</td></tr><tr><td>Unit (MeV)</td><td>None</td><td>KAN</td><td>GPR</td><td>LSTM</td></tr><tr><td>Least Squares</td><td>1.850</td><td>0.158</td><td>0.182</td><td>0.124</td></tr><tr><td>SLSQP</td><td>1.643</td><td>0.625</td><td>0.280</td><td>0.150</td></tr><tr><td>BFGS</td><td>1.642</td><td>0.483</td><td>0.245</td><td>0.155</td></tr></table>

<table><tr><td colspan="5">Test Set (975 nuclei)</td></tr><tr><td>Unit (MeV)</td><td>None</td><td>KAN</td><td>GPR</td><td>LSTM</td></tr><tr><td>Least Squares</td><td>1.755</td><td>0.346</td><td>0.311</td><td>0.357</td></tr><tr><td>SLSQP</td><td>1.591</td><td>0.701</td><td>0.431</td><td>0.364</td></tr><tr><td>BFGS</td><td>1.589</td><td>0.604</td><td>0.366</td><td>0.352</td></tr></table>

The RMSD values for the $\mathrm { S L S Q P + L S T M }$ and BFGS + LSTM models were also relatively low, at 0.150 and 0.155, respectively. Results from the test set further confirmed these observations. The $\mathrm { S L S Q P + L S T M }$ and $\mathrm { B F G S } + \mathrm { L S T M }$ models had errors of 0.364 and 0.352, respectively, also demonstrating strong performance. The KAN and GPR models exhibited relatively higher errors on the test set, highlighting their limitations in generalization ability.

Moreover, the performance of different optimization algorithms varies significantly. The BFGS and SLSQP optimization algorithms, especially when paired with neural network models like LSTM, significantly reduce computational errors in nuclear binding energy, thereby enhancing model accuracy. In contrast, the CG and L-BFGS-B optimization algorithms perform poorly in error control, especially in the absence of model corrections, where they exhibit higher error rates, highlighting their limitations. Neural network models, such as LSTM, effectively enhance the computational precision of nuclear binding energy, bringing theoretical predictions closer to experimental results. Notably, the LSTM model excels in both the training and overall datasets. These findings suggest that the integration of optimization algorithms with neural network models can substantially enhance computational accuracy, offering more precise tools for nuclear physics research.

Figure 3 shows the performance of the BW4 model across various isotope chains $\scriptstyle { Z = 2 0 }$ , 28, 50, 82) under different optimization algorithms (BFGS, Least Squares, SLSQP). In these graphs, the horizontal axis represents the neutron number, and the vertical axis indicates the difference between experimental and model-calculated values. These plots reveal the differences in how each algorithm handles the correction of nuclear binding energy.

For the Ca isotope chain, Figure 3 (a) shows that the error between experimental values and the Least Squares $^ +$ Neural Network correction term has significantly decreased compared to the version without the neural network correction. Although certain neutron numbers still exhibit noticeable fluctuations, the correction captures key trends in error changes. At $N = 2 0$ , the difference between experimental and theoretical values improved from the previous optimal of $- 1 . 5 7 9 \mathrm { M e V }$ to 0.203 MeV (GPR), 0.009 MeV (KANs), and 0.429 MeV (LSTM). At $N = 2 8$ , the difference improved from 1.805 MeV to 0.003 MeV (GPR), 0.011 MeV (KANs), and 0.039 MeV (LSTM).

In contrast, Figure 3 (b) indicates that the SLSQP $^ +$ Neural Network correction term exhibits smaller error fluctuations, showing improved stability, though significant error points remain. At $N = 2 0$ , the difference between experimental and theoretical values improved from $- 4 . 2 5 7 \mathrm { M e V }$ to -0.203 MeV (GPR), -0.426 MeV (KANs), and 0.006 MeV (LSTM). At $N = 2 8$ , the difference improved from 1.793 MeV to 0.188 MeV (GPR), 0.528 MeV (KANs), and 0.023 MeV (LSTM).

In Figure 3 (c), the BFGS $^ +$ Neural Network correction term shows larger error fluctuations across neutron numbers, with pronounced peaks and troughs, indicating less stability for this method on the Ca isotope chain. At $N = 2 0$ , the difference between experimental and theoretical values improved

![](images/af1d458d27773bca4a3ced86188fd8f3ae52f3b2f2786212c1a8791a512277d7.jpg)  
Figure 3: Relative Errors Between Experimental and Theoretical Values for the BW4 Mass Model Across Ca, Ni, Sn, and Pb Isotope Chains

from -4.243 MeV to 0.096 MeV (GPR), 0.019 MeV (KANs), and 0.021 MeV (LSTM). At $N = 2 8$ the difference improved from 1.826 MeV to 0.476 MeV (GPR), 0.084 MeV (KANs), and -0.091 MeV (LSTM).

For the Ni isotope chain, Figure 3 (d) indicates that the error between experimental values and the Least Squares $^ +$ Neural Network correction term shows a significant reduction compared to the uncorrected version. Although there are still noticeable fluctuations at certain neutron numbers, the correction captures key error trends. At $N = 2 8$ , the difference between experimental and theoretical values improved from $2 . 7 5 9 \ \mathrm { M e V }$ to 0.251 MeV (GPR), 0.007 MeV (KANs), and -0.041 MeV (LSTM). At $N = 5 0$ , the difference improved from 2.322 MeV to 0.129 MeV (GPR), -0.005 MeV (KANs), and 0.071 MeV (LSTM).

In contrast, Figure 3 (e) demonstrates that the SLSQP $^ +$ Neural Network correction term exhibits smaller error fluctuations, indicating better stability, though significant error points remain. For instance, at $N = 2 8$ , the difference between experimental and theoretical values shifted from -0.025 MeV to -0.148 MeV (GPR), 0.981 MeV (KANs), and $0 . 0 0 3 \mathrm { M e V }$ (LSTM). At $N = 5 0$ , the difference improved from $0 . 8 7 8 \mathrm { M e V }$ to 0.469 MeV (GPR), 0.435 MeV (KANs), and -0.018 MeV (LSTM).

In Figure 3 (f), the BFGS + Neural Network correction term shows larger error fluctuations across neutron numbers, with pronounced peaks and troughs, indicating reduced stability for this method on the Ni isotope chain. At $N = 2 8$ , the difference between experimental and theoretical values shifted from -0.047 MeV to -0.281 MeV (GPR), 0.081 MeV (KANs), and 0.15 MeV (LSTM). At $N = 5 0$ , the difference improved from 0.865 MeV to 0.203 MeV (GPR), 0.188 MeV (KANs), and -0.012 MeV (LSTM).

For the Sn isotope chain, Figure 3 (i) shows a significant reduction in error between the experimental values and the Least Squares $^ +$ Neural Network correction term compared to the uncorrected model. Despite some noticeable fluctuations at certain neutron numbers, the correction captures key trends in error changes. At $N = 5 0$ , the difference between experimental and theoretical values improved from 8.137 MeV to -0.155 MeV (GPR), -0.028 MeV (KANs), and 0.018 MeV (LSTM). At $N = 8 2$ , the

difference improved from 9.091 MeV to 0.005 MeV (GPR), $6 . 3 1 \times 1 0 ^ { - 4 }$ MeV (KANs), and -0.004 MeV (LSTM).

In contrast, Figure 3 (g) demonstrates that the SLSQP $^ +$ Neural Network correction term exhibits smaller error fluctuations, showing improved stability, though significant error points remain. At $N = 5 0$ , the difference between experimental and theoretical values improved from 5.397 MeV to 0.46 MeV (GPR), 1.396 MeV (KANs), and 0.073 MeV (LSTM). At $N = 8 2$ , the difference improved from $7 . 1 1 9 \mathrm { M e V }$ to 1.288 MeV (GPR), 0.707 MeV (KANs), and 0.18 MeV (LSTM).

In Figure 3 (h), the BFGS + Neural Network correction term shows larger error fluctuations across neutron numbers, with pronounced peaks and troughs, indicating reduced stability for this method on the Sn isotope chain. At $N = 5 0$ , the difference between experimental and theoretical values improved from $5 . 3 2 \mathrm { M e V }$ to 0.145 MeV (GPR), 0.171 MeV (KANs), and 0.104 MeV (LSTM). At $N = 8 2$ , the difference improved from 7.076 MeV to 0.418 MeV (GPR), 0.825 MeV (KANs), and 0.38 MeV (LSTM).

For the Pb isotope chain, Figure 3 (j) demonstrates a significant reduction in the error between experimental values and the Least Squares $^ +$ Neural Network correction term compared to the uncorrected model, although substantial error fluctuations persist at certain neutron numbers. At $N = 1 2 6$ , the difference between experimental and theoretical values improved from $7 . 6 0 6 \mathrm { M e V }$ to 0.03745 MeV (GPR), 0.62288 MeV (KANs), and 0.48104 MeV (LSTM).

In contrast, Figure 3 (k) shows that the SLSQP $^ +$ Neural Network correction term exhibits superior stability, with the smallest error fluctuations and a lower overall error level, demonstrating its strength in handling isotope chains with high proton numbers. At $N = 1 2 6$ , the difference between experimental and theoretical values improved from 5.927 MeV to 0.31665 MeV (GPR), 0.86198 MeV (KANs), and 0.03674 MeV (LSTM).

In Figure 3 (l), the BFGS + Neural Network correction term’s error curve continues to show large fluctuations, suggesting reduced stability for this method on the $\mathrm { P b }$ isotope chain. At $N = 1 2 6$ , the difference between experimental and theoretical values improved from 5.867 MeV to $4 . 8 5 \times 1 0 ^ { - 4 }$ MeV (GPR), 1.72804 MeV (KANs), and 0.42378 MeV (LSTM).

# 4 Summary

The liquid drop model effectively explains the large and smooth components of the binding energy. However, its limitations prevent it from capturing the small, fluctuating components as described by the Strutinsky theorem. We enhanced the BW2 mass model by introducing nucleon gravitational effects, higher-order symmetry energy terms, and pairing interactions $( B E _ { \mathrm { L D M } } )$ ), and further optimized BE using algorithms. A neural network correction term $( \delta _ { N n } )$ was then added, leading to the development of the BW4 mass model. Based on this model, the following conclusions were reached:

(1) By refining the original BW2 mass model, the root mean square deviation (RMSD) of the $B E _ { \mathrm { L D M } }$ was reduced from 1.915 MeV to $1 . 8 2 2 \mathrm { M e V }$ using the Least Squares method. We tested and compared several optimization algorithms, obtaining lower RMSDs of 1.626 MeV (SLSQP) and $1 . 6 2 7 \mathrm { M e V }$ (BFGS). These improvements resulted from the optimized coefficients, which increased the weighting of the exchange Coulomb term, surface symmetry term, higher-order symmetry energy term, and pairing correction term.   
(2) In the doubly magic nucleus region, $B E _ { \mathrm { L D M } }$ (SLSQP) and $B E _ { \mathrm { L D M } }$ (BFGS) outperform $B E _ { \mathrm { L D M } }$ (Least Squares); however, in the semi-magic nucleus region, $B E _ { \mathrm { L D M } }$ (Least Squares) exhibits smaller errors relative to experimental values.   
(3) Subsequently, a neural network correction term was introduced to account for the small and fluctuating components, leading to the development of the BW4 mass model. The BW4 model combined with BFGS+LSTM(KANs) shows a significantly lower overall error compared to the model without the correction term, reducing from $1 . 8 2 2 \mathrm { M e V }$ to 0.233 MeV (0.522 MeV). The BW4 model with BFGS+LSTM provides notable optimization in both the doubly magic nucleus region and the semi-magic nucleus region.

# References

[1] B. Michael, P. H. Heenen, P. G. Reinhard, Self-consistent mean-field models for nuclear structure. Rev. Mod. Phys 75, 121-180 (2003). https://doi.org/10.1103/RevModPhys.75.121   
[2] D. Lunney, J. M. Pearson, and C. Thibault, Recent trends in the determination of nuclear masses. Rev. Mod. Phys 75, 1021-1082 (2003). https://doi.org/10.1103/RevModPhys.75.1021   
[3] A. C. Larsen, A. Spyrou, S. N. Liddick et al., Novel Techniques for Constraining Neutron-Capture Rates Relevant for r -Process Heavy-Element Nucleosynthesis. Prog. Part. Nucl. Phys 107, 69-108 (2019). https://doi.org/10.1016/j.ppnp.2019.04.002   
[4] T. Yamaguchi, H. Koura, M. Wang et al., Masses of exotic nuclei. Prog. Part. Nucl. Phys 120, 103882 (2021). https://doi.org/10.1016/j.ppnp.2021.103882   
[5] J. Erler, N. Birge, M. Kortelainen et al., The limits of the nuclear landscape. Nature 486, 509-512 (2012). https://doi.org/10.1038/nature11188   
[6] W. J. Huang, M. Wang, F. G. Kobdev et al., The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures. Chinese. Phys. C 45, 030002 (2021). https://doi.org/10.1088/1674-1137/abddb0   
[7] M. Wang, W. J. Huang, F. G. Kobdev et al., The AME 2020 atomic mass evaluation (II). Tables, graphs and references. Chinese. Phys. C 45, 030003 (2021). https://doi.org/10.1088/1674- 1137/abddaf   
[8] P. Mo¨ller, A. J. Sierk, T. Ichikawa et al., Nuclear ground-state masses and deformations: FRDM(2012). At. Data Nucl. Data Tables 109-110, 1-204 (2016). https://doi.org/10.1016/j.adt.2015.10.002   
[9] C. F. v. Weizsacker, Leipzig, Zur Theorie der Kernmassen. Z. Physik 96, 431-458 (1935). https://doi.org/10.1007/BF01337700   
[10] H. A. Bethe, R. F. Bacher, Nuclear Physics A. Stationary States of Nuclei. Rev. Mod. Phys 8, 82 (1936). https://doi.org/10.1103/RevModPhys.8.82   
[11] B. Mohammed-Azizi, Better insight into the Strutinsky method. Phys. Rev. C 100, 034319 (2019). https://doi.org/10.1103/PhysRevC.100.034319   
[12] D. Benzaid, S. Bentridi, A. Kerraci et al., Bethe-Weizsacker semiempirical mass formula coefficients 2019 update based on AME2016. Nucl. Sci. Tech 31, 9 (2020). https://doi.org/10.1007/s41365-019-0718-8   
[13] W. H. Ye, Y. B. Qian, Z. Z. Ren, Accuracy versus predictive power in nuclear mass tabulations. Phys. Rev. C 106, 024318 (2022). https://doi.org/10.1103/PhysRevC.106.024318   
[14] P. Mo¨ller, W. D. Myers, H. Sagawa et al., New Finite-Range Droplet Mass Model and Equation-of-State Parameters. Phys. Rev. Lett 108, 052501 (2012). https://doi.org/10.1103/PhysRevLett.108.052501   
[15] H. Koura, T. Tachibana, M. Uno et al., Nuclidic Mass Formula on a Spherical Basis with an Improved Even-Odd Term. Prog. Theor. Phys 113, 305 (2005). https://doi.org/10.1143/PTP.113.305   
[16] F. A. Ivanyuk, K. Pomorski,Optimal shapes and fission barriers of nuclei within the liquid drop model. Phys. Rev. C 79, 054327 (2009). https://doi.org/10.1103/PhysRevC.79.054327   
[17] N. Wang, Z. Y. Liang, M. Liu et al., Mirror nuclei constraint in nuclear mass formula. Phys. Rev. C 82, 044304 (2010). https://doi.org/10.1103/PhysRevC.82.044304   
[18] N. Wang, M. Liu, X. Z. Wu, Modification of nuclear mass formula by considering isospin effects. Phys. Rev. C 81, 044322 (2010). https://doi.org/10.1103/PhysRevC.81.044322   
[19] M. Liu, N. Wang, Y. G. Deng et al., Further improvements on a global nuclear mass model. Phys. Rev. C 84, 014333 (2011). https://doi.org/10.1103/PhysRevC.84.014333   
[20] N. Wang, M. Liu, X. Z. Wu et al., Surface diffuseness correction in global mass formula. Phys. Rev. C 734, 215 (2014). https://doi.org/10.1016/j.physletb.2014.05.049   
[21] S. Goriely, N. Chamel, J. M. Pearson,Further explorations of Skyrme-Hartree-Fock-Bogoliubov mass formulas. XII. Stiffness and stability of neutron-star matter. Phys. Rev. C 82, 035804 (2010). https://doi.org/10.1103/PhysRevC.82.035804

[22] S. Goriely, N. Chamel, Further explorations of Skyrme-Hartree-Fock-Bogoliubov mass formulas. XIII. The 2012 atomic mass evaluation and the symmetry coefficient. Phys. Rev. C 88, 024308 (2013). https://doi.org/10.1103/PhysRevC.88.024308   
[23] R. A. Rego, Mean free path in the relativistic mean field. Phys. Rev. C 44, 1944 (1991). https://doi.org/10.1103/PhysRevC.44.1944   
[24] J. L. Janssen, Y. Gillet, A. Martin et al., Precise effective masses from density functional perturbation theory. Phys. Rev. B 93, 205147 (2016). https://doi.org/10.1103/PhysRevB.93.205147   
[25] W. K. Michael, Mutual influence of terms in a semi-empirical mass formula. Nucl. Phys. A. 798, 29-60 (2008). https://doi.org/10.1016/j.nuclphysa.2007.10.011   
[26] D. M. William, J. S. Wladyslaw, Nuclear masses and deformations. Nucl. Phys 81, 1-60 (1966). https://doi.org/10.1016/S0029-5582(66)80001-9   
[27] A. N. Antonov, D. N. Kadrev, M. K. Gaidarov et al., Temperature dependence of the symmetry energy and neutron skins in Ni, Sn, and Pb isotopic chains. Phys. Rev. C 95, 024314 (2017). https://doi.org/10.1103/PhysRevC.95.024314   
[28] T. Naito, R. Akashi, H. Z. Liang, Application of a Coulomb energy density functional for atomic nuclei: Case studies of local density approximation and generalized gradient approximation. Phys. Rev. C 97, 044319 (2018). https://doi.org/10.1103/PhysRevC.97.044319   
[29] G. Lugones, A. G. Grunfeld, Surface and curvature properties of charged strangelets in compact objects. Phys. Rev. C 103, 035813 (2021). https://doi.org/10.1103/PhysRevC.103.035813   
[30] E. Wigner, On the Consequences of the Symmetry of the Nuclear Hamiltonian on the Spectroscopy of Nuclei. Phys. Rev 51, 106 (1937). https://doi.org/10.1103/PhysRev.51.106   
[31] F. C. Richard, Nuclear Structure from a Simple Perspective. Oxford. Acad 15, 10 (2001). https://doi.org/10.1093/acprof:oso/9780198507246.001.0001   
[32] G. Royer, C. Gautier, Coefficients and terms of the liquid drop model and mass formula. Phys. Rev. C 73, 067302 (2006). https://doi.org/10.1103/PhysRevC.73.067302   
[33] Z. M. Niu, H. Z. Liang, Nuclear mass predictions based on Bayesian neural network approach with pairing and shell effects. Phys. Lett. B 778, 48-53 (2018). https://doi.org/10.1016/j.physletb.2018.01.002   
[34] B. S. Cai, C. X. Yuan, Random forest-based prediction of decay modes and half-lives of superheavy nuclei. Nucl. Sci. Tech 34, 204 (2023). https://doi.org/10.1007/s41365-023-01354-5   
[35] Y. Y. Cao, J. Y. Guo, B. Zhou, Predictions of nuclear charge radii based on the convolutional neural network. Nucl. Sci. Tech 34, 152 (2023). https://doi.org/10.1007/s41365-023-01308-x   
[36] T. S. Shang, J. Li, Z. M. Niu, Prediction of nuclear charge density distribution with feedback neural network. Nucl. Sci. Tech 33, 153 (2022). https://doi.org/10.1007/s41365-022-01140-9   
[37] W. H. Ye, Y. B. Qian, H. K. Wang, Multiple constraints on nuclear mass formulas for reliable extrapolations. Phys. Rev. C 107, 044302 (2023). https://doi.org/10.1103/PhysRevC.107.044302   
[38] G. T. GARVEY, W. J. GERACE, R. L. JAFFE et al., Set of Nuclear-Mass Relations and a Resultant Mass Table. Rev. Mod. Phys 41, 1-80 (1969). https://doi.org/10.1103/RevModPhys.41.S1   
[39] W. H. Ye, Y. B. Qian, Z. Z. Ren, Accuracy versus predictive power in nuclear mass tabulations. Phys. Rev. C 106, 024318 (2022). https://doi.org/10.1103/PhysRevC.106.024318   
[40] M. Gong, F. Zhao, S. Y. Zeng et al., An experimental study on local and global optima of linear antenna array synthesis by using the sequential least squares programming. Appl. Soft. Comput. 148, 110859 (2023). https://doi.org/10.1016/j.asoc.2023.110859   
[41] M. J. D. Powell, A direct search optimization method that models the objective and constraint functions by linear interpolation. In: Advances in Optimization and Numerical Analysis. 275, 51-67 (1994). https://doi.org/10.1007/978-94-015-8330-5   
[42] Y. G. Pei, D. T. Zhu, On the Global Convergence of a Projective Trust Region Algorithm for Nonlinear Equality Constrained Optimization. Acta. Math. Sin.-English Ser. 34, 1804-1828 (2018). https://doi.org/10.1007/s10114-018-7063-4   
[43] P. G. Chen, Y. J. Peng, S. J. Wang, The Hessian matrix of Lagrange function. Linear. Algebra. Appl. 531, 537-546 (2017). https://doi.org/10.1016/j.laa.2017.06.012

[44] F. S. P. S. Abad, M. Allahdadi, H. M. Nehi, Interval linear fractional programming: optimal value range of the objective function. Comp. Appl. Math 39, 261 (2020). https://doi.org/10.1007/s40314-020-01308-2   
[45] D. M. Hou, Y. X. Ning, C. Zhang, An efficient and robust Lagrange multiplier approach with a penalty term for phase-field models. J. Comput. Phys 488, 112236 (2023). https://doi.org/10.1016/j.jcp.2023.112236   
[46] P. Armand, N. N. Tran, Boundedness of the inverse of a regularized Jacobian matrix in constrained optimization and applications. Optim. Lett 16, 2359-2371 (2022). https://doi.org/10.1007/s11590-021-01829-7   
[47] Z. M. Niu, B. H. Sun, H. Z. Liang et al., Improved radial basis function approach with odd-even corrections. Phys. Rev. C 94, 054315 (2016). https://doi.org/10.1103/PhysRevC.94.054315