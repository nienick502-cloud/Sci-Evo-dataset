# Machine learning the deuteron

JWT Keeblea, A Riosa,∗

aDepartment of Physics, Faculty of Engineering and Physical Sciences, University of Surrey, Guildford, Surrey GU2 7XH, United Kingdom

# Abstract

We use machine learning techniques to solve the nuclear two-body bound state problem, the deuteron. We use a minimal one-layer, feed-forward neural network to represent the deuteron $S -$ and $D -$ state wavefunction in momentum space, and solve the problem variationally using ready-made machine learning tools. We benchmark our results with exact diagonalisation solutions. We find that a network with 6 hidden nodes (or 24 parameters) can provide a faithful representation of the ground state wavefunction, with a binding energy that is within $0 . 1 \%$ of exact results. This exploratory proof-of-principle simulation may provide insight for future potential solutions of the nuclear many-body problem using variational artificial neural network techniques.

Keywords: deuteron, quantum many-body theory, machine learning, neural networks 2010 MSC: 81V35, 81V70, 82C32

# 1. Introduction

Machine learning (ML) techniques are ubiquitous within and outside the scientific domain. They are used in a variety of contexts and can be exploited to classify information; to compress it; to interpolate or extrapolate data, and to solve a variety of optimisation problems [1]. In physics, artificial neural networks (ANNs) have been ex-[ tensively used in the past to analyse data, particularly in particle physics experiments and theory [2, 3]. In nuclear physics, early applications of ANNs to nuclear systematics [4, 5] have been recently extended to exotic mass domains [6], fission yields [7], $\beta -$ and $\alpha -$ decay half-lives [8, 9] and nuclear deformation and spectroscopic properties [10]. In ab initio nuclear structure theory, ANNs can be used to extrapolate results of otherwise costly first-principles calculations from restricted model spaces [11? , 12].

A more recent development of ML techniques is their application to solve specific physics problems in the quantum domain [13, 14, 15]. In particular, a series of recent ML applications have shown promising results in the solution of quantum many-body problems from first principles. The pioneering application of Ref. [16] in spin systems used a restricted Boltzmann machine as a wavefunction ansatz. These simulations give access to both the ground state and the dynamics of systems with different dimensions, and extensions to excited states have also been formulated [17]. The solution of discrete [18] and real space [19] many-body bosonic systems followed shortly after. More sophisticated techniques based on deep neural networks have been recently developed to tackle realistic quantum

chemistry problems [20, 21, 22]. In all these cases, the problem is set up as a variational one, and the solution is fully ab initio. While we were preparing this manuscript, the preprint in Ref. [23] reported results for few-body nuclei similar in spirit to what we report here.

There are two key reasons that make ANNs particularly attractive in the quantum many-body domain. First, ANNs can encapsulate and compress information. If this compression is efficient enough, the complex content of many-body wavefunctions may be codified into manageable, specifically tailored and, possibly, deep ANNs [24]. Second, ML techniques are particularly suited to solve optimisation problems. In a physics setting, with the energy as a cost function, these can be easily mapped into variational problems. The expectation is that these variational artificial neural network (VANNs) are superior to traditional trial wavefunctions, due to their ability to express features flexibly and efficiently.

By providing direct access to the many-body wavefunction, ML techniques open a series of interesting possibilities to find nuclear ground states, operator expectation values and dynamics. Whether or not one can actually implement VANN algorithms efficiently in nuclear manybody systems is at present an open question. Here, we present a proof-of-principle calculation of a nuclear system, the deuteron, using ready-made, available ML resources. The deuteron is a natural starting point to explore the feasibility of ab initio methods [25]. While this is far from being a relevant many-body application, it allows for an exploratory analysis of the quality of ANN ans¨atze to the deuteron wavefunction.

![](images/b91a9434b347a85e7ae693f0a3f86685df17b0d326097adcf9f50404d7310dc5.jpg)  
Figure 1: ANN architecture used in this work. The input is a single value of momentum, $q$ , and the wavefunctions are modelled in terms of a minimal single-layer network. In the example above, the number of hidden nodes is $N _ { \mathrm { h i d } } = 4$ . The ANN has two outputs, one for the $S$ and one for the $D$ state.

# 2. Methods

Our solution for the deuteron is variational. We set up a minimal trial wavefunction. Our ANN has a single input node: a value of relative momentum, $q$ , between the neutron and the proton in the deuteron. The ANN has two output nodes, one for the $L = 0$ ( $S$ ) and one for the $L = 2$ (D) state. In between, we set up a single layer with $N _ { \mathrm { h i d } }$ hidden nodes. The architecture of the network is shown in Fig. 1, which translates mathematically into a wavefunction ansatz

$$
\psi_ {\mathrm {A N N}} ^ {L} (q) = \sum_ {i = 1} ^ {N _ {h i d}} \mathcal {W} _ {i, L} ^ {(2)} \sigma \left(\mathcal {W} _ {i} ^ {(1)} q + b _ {i}\right), \tag {1}
$$

where $\sigma ( x )$ represents a non-linear activation function. The weights $\boldsymbol { w } ^ { ( 1 ) }$ connect the input relative momentum, $q$ , to a hidden layer, whereas $w ^ { ( 2 ) }$ connects the hidden layer to the two outputs. We also use a bias between the input and the hidden layer, $\mathbf { b }$ . We use bold notation $\boldsymbol { w } ^ { ( 1 ) }$ to denote the full weight (or bias) vectors, as opposed to the vector components $\mathcal { W } _ { i } ^ { ( 1 ) }$ . The concatenation of all weights and biases is denoted by ${ \mathcal W } = \{ { \bf b } , { \mathcal W } ^ { ( 1 ) } , { \mathcal W } ^ { ( 2 ) } \}$ . For a given number of hidden layer nodes $N _ { \mathrm { h i d } }$ , there are a total of $4 N _ { \mathrm { h i d } }$ parameters in the trial ANN wavefunction.

We use both a sigmoid and a softplus activation function $\sigma ( x )$ in our ansatz. The two functions are continuous and differentiable, and softplus is less prone to be affected by the vanishing gradient problem [26]. The output layer is a weighted linear sum of the values of the hidden D− states, ψL=0,2ANN nodes, and provides arbitrary admixtures of the $D -$ $\psi _ { \mathrm { A N N } } ^ { L = 0 , 2 }$ . Dedicating a single layer to each of $S -$ and the two states would result in an increase of the number of parameters, departing from the minimal spirit of our approach.

The parameters $\mathcal { W }$ are used as variational parameters in a minimisation problem for the energy,

$$
E ^ {\mathcal {W}} = \frac {\left\langle \Psi_ {\mathrm {A N N}} ^ {\mathcal {W}} \right| \hat {H} \left| \Psi_ {\mathrm {A N N}} ^ {\mathcal {W}} \right\rangle}{\left\langle \Psi_ {\mathrm {A N N}} ^ {\mathcal {W}} \right| \Psi_ {\mathrm {A N N}} ^ {\mathcal {W}} \rangle}. \tag {2}
$$

We solve the problem explicitly in momentum space [27, 28, 29]. This is unlike previous VANN applications [19, 20, 21, 22], but helpful for three practical reasons. First, in momentum space the kinetic term in the Hamiltonian of Eq. (2) is a continuous function. In contrast, in real space, the kinetic term would involve numerically costly derivatives on the ANN wavefunctions. Second, for the deuteron, the separation between centre-of-mass and relative motion can be implemented straightforwardly. The centre-of-mass coordinate can be ignored and the problem is solved as an effective one-body Schr¨odinger equation in relative momentum, $q$ . Third, a momentum space approach allows us to employ directly the numerical routines associated to the N3LO Entem-Machleidt nucleon-nucleon force, our interaction of choice [30]. We have tested the method with other momentum-space potentials, and have found similar levels of agreement with the corresponding benchmarks.

We use the same momentum quadrature in all our integrals. In the many-body case, these integrals may be more efficiently performed using Monte Carlo techniques [19]. For the one-dimensional integrals associated to the deuteron, we estimate that a large number of Monte Carlo samples of order $> 1 0 ^ { 5 }$ is needed to get an accurate prediction for the binding energy. We instead use $N _ { k } = 6 4$ points in a Gauss-Legendre quadrature, and use a tangential change of variables to extend the integration range from 0 to $k _ { \mathrm { m a x } } = 5 0 0 ~ \mathrm { f m ^ { - 1 } }$ . This approach provides a dense mesh at low momenta, while sparsely covering the high-momentum region (only 7 mesh points lie beyond $k = 5 ~ \mathrm { f m ^ { - 1 } }$ ). We use the same quadrature to solve the exact ground state eigenvalue problem, to set a benchmark for the VANN solution and find an “exact” ground state energy, $E _ { \mathrm { G S } } = - 2 . 2 2 6 7$ MeV.

The choice of a continuous momentum basis, as opposed to a discrete basis, is further motivated by an important result on ANNs. The Universal Approximation Theorem guarantees that a network with a single layer provides a faithful representation of any continuous function within a given domain, provided $N _ { \mathrm { h i d } }$ is large enough [31, 32]. In this sense, working in continuous momentum space, rather than in a discrete basis, may be advantageous. One naively expects that ANNs should mimic the shape of any wavefunction, if given enough hidden nodes to do so. We note that perfect agreement between input and output is likely to require a local cost function, to penalise differences throughout momentum space. This is not necessarily the case here, where we use a global (integrated) energy cost function.

We solve the variational problem in three different steps, implemented using the ready-made PyTorch framework [33]. First, we initialise the network using random weight values. We sample from uniform distributions with $w ^ { ( 1 ) } \in$ $[ - 1 , 0 )$ , $ { \mathbf { b } } \in [ - 1 , 1 )$ and $\boldsymbol { w } ^ { ( 2 ) } \in [ 0 , 1 )$ . This differs from the traditional Xavier initialisation scheme, which has a poor performance in this problem [34]. After this random initialisation, the wavefunctions are featureless and have

![](images/c7d8fc3ffa9317b02500b140881bb7932c1296e845170587a1d374d4f301eaf7.jpg)  
Figure 2: Deuteron binding energy as a function of iteration number for a network with $N _ { \mathrm { h i d } } = 1 0$ and a softplus activation function. The energy cost function is minimised using RMSprop (see Appendix A for details).

no bearing to physical ones. In a second step, we therefore follow Ref. [19] and train the ANN to reproduce physically inspired, but arbitrary, target wavefunctions for each of the two states. We use a functional form $\psi _ { \mathrm { t a r g } } ^ { L } ( q ) \propto q ^ { L } e ^ { - \frac { \xi ^ { 2 } q ^ { 2 } } { 2 } }$ with $\xi = 1 . 5$ fm, which provides target wavefunctions with momentum space widths which are similar to the exact solutions.

We train the ANN wavefunction to match the target wavefunction in a supervised manner. The cost function, $\mathcal { C } = \mathcal { C } ^ { S } + \mathcal { C } ^ { D }$ , is the sum of the individual contributions for each state, $\mathcal { C } ^ { L } = ( \mathcal { K } ^ { L } - 1 ) ^ { 2 }$ , where we introduce the overlap

$$
\begin{array}{l} \mathcal {K} ^ {L} = \frac {\left\langle \right. \psi_ {\mathrm {t a r g}} ^ {L} \left. \right| \psi_ {\mathrm {A N N}} ^ {L} \left. \right\rangle^ {2}}{\left\langle \right. \psi_ {\mathrm {t a r g}} ^ {L} \left. \right| \psi_ {\mathrm {t a r g}} ^ {L} \rangle \left\langle \right. \psi_ {\mathrm {A N N}} ^ {L} \left. \right| \psi_ {\mathrm {A N N}} ^ {L} \rangle} \tag {3} \\ = \frac {[ \int_ {0} ^ {\infty} d q q ^ {2} \psi_ {\mathrm {t a r g}} ^ {L} (q) \psi_ {\mathrm {A N N}} ^ {L} (q) ] ^ {2}}{\int_ {0} ^ {\infty} d q q ^ {2} \psi_ {\mathrm {t a r g}} ^ {L} (q) \psi_ {\mathrm {t a r g}} ^ {L} (q) \int_ {0} ^ {\infty} d q q ^ {2} \psi_ {\mathrm {A N N}} ^ {L} (q) \psi_ {\mathrm {A N N}} ^ {L} (q)}. \\ \end{array}
$$

The RMSprop scheme is used to minimise $c$ for $1 0 ^ { 5 }$ iterations [14, 35]. We provide more details about this scheme in Appendix A, and list here only the relevant hyperparameters: $\alpha = 1 0 ^ { - 2 }$ , $\beta = 0 . 9$ and $\epsilon = 1 0 ^ { - 8 }$ . The network calculates an unnormalised wavefunction for each partial wave. In the minimisation algorithm, the wavefunction normalization constants divide the learning rates. Because these normalization constants are typically larger than one, unnormalized wavefunctions effectively reduce the learning rate during the minimisation process, allowing for a relatively large value of $\alpha$ . After this initial training step, the resulting overlap is within $1 - 5 \%$ of the desired value of ${ \kappa } ^ { L } = 1$ . The admixture of the $S -$ and the $D -$ states is deliberately chosen to have an unphysically large value of $5 0 \%$ .

The third and final step is the actual variational energy minimisation. We let the network evolve to readjust the wavefunctions while minimising the energy. The initial large admixture between the two states does not hinder the convergence of the VANN. We use RMSprop again to minimise the energy cost function in Eq. (2), with the same hyperparameter set discussed above. A typical energy min-

![](images/e351819a76998bf97407ec0141140463e6a9010815dacb8e44757c5e54300f36.jpg)

![](images/21cf0f8259143e435aaf5c5a72f00d1d0907a82fe53cd861d26a5af241a7b233.jpg)

![](images/b8e5c2a6e57746f703bd1cca4f9f02f4a273a0cfa3e4a8df42a0c6d3191c032a.jpg)  
Figure 3: Binding energy of the deuteron (top panel), fidelities $\mathcal { F } ^ { L }$ (central) and $D -$ state probability (bottom) as a function of the number of hidden layer nodes, $N _ { \mathrm { h i d } }$ . Lines (bands) are obtained from the average (standard deviation) of 50 independent VANN runs. Horizontal (dashed) lines show the benchmark result.

imisation curve for the case with $N _ { \mathrm { h i d } } = 1 0$ and a softplus activation function is shown in Fig. 2. Within the first few thousands of iterations (not shown in the Figure for clarity), the descent is fast and smooth and the network is able to bind the deuteron. After about $1 0 , 0 0 0$ iterations, fluctuations appear. This allows for the energy to be overshot at times, but the minimisation algorithm eventually corrects for that. At 50, 000 iterations, the binding energy is already within 10% of the benchmark value (dashed line). We stop our runs at 250, 000 iterations, where the binding energy is converged within fluctuations of the order of $2 - 3$ keV.

# 3. Results

We explore the bias and variance of our minimal VANN model, particularly the out-of-sample error, in two different ways. First, we change the number of hidden layer nodes from $N _ { \mathrm { h i d } } = 2$ to 20, in steps of 2. An extended discussion up to $N _ { \mathrm { h i d } } = 1 0 0$ is presented in Appendix B. This provides an idea of how model predictions change with an increase in the number of variational parameters. Second, we initialise the model, train it to target wavefunctions and minimise the energy with 50 different random seed configurations. The results shown here are obtained as the means and standard deviations of these 50 individual runs. This helps identify weight initialisation effects.

Table 1: VANN results for the fidelities $\mathcal { F } ^ { S }$ and $\mathcal { F } ^ { D }$ ; binding energy $E$ and $_ { D - }$ state probability $P ^ { D }$ as a function of $N _ { \mathrm { h i d } }$ . Columns 2-5 (6-9) provide results for sigmoid (softplus) activation functions. For completeness, we provide the benchmark exact values in the bottom row.   

<table><tr><td></td><td colspan="4">Sigmoid</td><td colspan="4">Softplus</td></tr><tr><td>Nhid</td><td>FS</td><td>FD</td><td>E (MeV)</td><td>PD(%)</td><td>FS</td><td>FD</td><td>E (MeV)</td><td>PD(%)</td></tr><tr><td>4</td><td>0.998(2)</td><td>0.995(10)</td><td>-2.15(16)</td><td>4.64(22)</td><td>0.9980(16)</td><td>0.993(21)</td><td>-2.14(12)</td><td>4.57(44)</td></tr><tr><td>6</td><td>0.99994(2)</td><td>0.99995(4)</td><td>-2.223(1)</td><td>4.51(7)</td><td>0.99983(13)</td><td>0.99976(20)</td><td>-2.220(6)</td><td>4.50(12)</td></tr><tr><td>8</td><td>0.999973(7)</td><td>0.999974(22)</td><td>-2.2247(7)</td><td>4.52(6)</td><td>0.999950(21)</td><td>0.999963(30)</td><td>-2.2243(18)</td><td>4.52(9)</td></tr><tr><td>10</td><td>0.999981(5)</td><td>0.999974(21)</td><td>-2.2249(8)</td><td>4.53(6)</td><td>0.999964(7)</td><td>0.999981(10)</td><td>-2.2248(8)</td><td>4.50(7)</td></tr><tr><td>12</td><td>0.999985(4)</td><td>0.999983(20)</td><td>-2.2253(7)</td><td>4.52(5)</td><td>0.999970(6)</td><td>0.999983(12)</td><td>-2.2251(7)</td><td>4.51(8)</td></tr><tr><td>14</td><td>0.999987(3)</td><td>0.999986(14)</td><td>-2.2254(6)</td><td>4.52(5)</td><td>0.999973(4)</td><td>0.999981(14)</td><td>-2.2251(7)</td><td>4.51(8)</td></tr><tr><td>16</td><td>0.999989(4)</td><td>0.999986(14)</td><td>-2.2254(6)</td><td>4.51(4)</td><td>0.999975(6)</td><td>0.999985(11)</td><td>-2.2252(8)</td><td>4.53(6)</td></tr><tr><td>18</td><td>0.999990(3)</td><td>0.999982(17)</td><td>-2.2255(5)</td><td>4.52(5)</td><td>0.999975(4)</td><td>0.999981(16)</td><td>-2.2251(8)</td><td>4.52(7)</td></tr><tr><td>20</td><td>0.999992(3)</td><td>0.999985(11)</td><td>-2.2256(5)</td><td>4.51(5)</td><td>0.999976(5)</td><td>0.999984(14)</td><td>-2.2252(8)</td><td>4.51(7)</td></tr><tr><td>Exact</td><td>1</td><td>1</td><td>-2.2267</td><td>4.51</td><td>1</td><td>1</td><td>-2.2267</td><td>4.51</td></tr></table>

When a ground-state ANN wavefunction has been obtained, we quantify its quality by comparing it to the benchmark wavefunction from exact diagonalisation using a partial-wave fidelity, $\mathcal { F } ^ { L }$ . This is akin to the overlap defined in Eq. (3) with the replacement ψLtarg → ψLGS [19]. $\psi _ { \mathrm { t a r g } } ^ { L }  \psi _ { \mathrm { G S } } ^ { L }$ The closer $\mathcal { F } ^ { L }$ is to one, the closer our wavefunction reproduces the exact diagonalisation results.

The main results of this paper are reported in Fig. 3 and, in a tabular form, in Table 1. In all cases, we report outcomes obtained for both sigmoid and softplus activation functions. With an $N _ { \mathrm { h i d } } = 2$ model, not shown for brevity, the deuteron is already bound by $\approx 0 . 8$ MeV. For $N _ { \mathrm { h i d } } = 4$ , the quality of the ANN ansatz is relatively competitive, with fidelities within 2% of $\mathcal { F } ^ { L } = 1$ , and a binding energy that is already within about $\approx 5 \%$ of the benchmark value, albeit with a significant standard deviation. At the level of $N _ { \mathrm { h i d } } = 6$ , we already obtain energies (fidelities) that are accurate within 10 keV (0.05%). As $N _ { \mathrm { h i d } }$ increases, the energy approaches the benchmark, and stabilises around $N _ { \mathrm { h i d } } \approx 1 0$ . Above this value, we find a relative agreement of the order of $\approx 2$ keV in energies. The error in fidelities remains relatively constant above $N _ { \mathrm { h i d } } \approx 1 0$ too, at a level of $\approx 0 . 0 0 5 \%$ across all the models.

Having access to the wavefunctions, we can also comprobability, pute structural properties of the deuteron. The $P _ { \mathrm { A N N } } ^ { D } =  \psi _ { \mathrm { A N N } } ^ { D } | \psi _ { \mathrm { A N N } } ^ { D } $ , is correlated with the $D -$ state strength of the tensor force. With as little as 4 hidden nodes the admixture between the $S$ and $D$ states is off by just over $0 . 1 \%$ . As $N _ { \mathrm { h i d } }$ increases, the values approach the benchmark $P _ { \mathrm { G S } } ^ { D } = 4 . 5 1 \%$ . The bottom panel of Fig. 3 indicates that the network is able to predict the admixture between the $S$ and $D$ state with a variance of less than $0 . 1 \%$ .

When it comes to different activation functions, the sigmoid and softplus results provide qualitatively similar results. We take this is as a sign of robustness in the methodology. At a quantitative level, the sigmoid calcu-

lations outperform the softplus results. Sigmoids seem to provide results that are closer to benchmarks and have relatively smaller variances. As seen in the Table 1, but also in the $N _ { \mathrm { h i d } }$ convergence shown in the central panels of Fig. 3, the fidelities predicted by the sigmoid ANN for the $S -$ state are substantially better than those predicted by the softplus ANN. $D -$ state fidelities, in contrast, have a similar level of quality for both activation functions.

Variational calculations with the same N3LO interaction typically require $\approx 8$ parameters to find energies within 0.1 MeV of the exact value [27, 28, 29]. We are not aware of other variational calculations in momentum space that use more parameters. We have however set up a stochastic variational method solution to the deuteron, with exactly the same momentum-space set-up [36]. We find that, to get an accuracy equivalent to the $N _ { \mathrm { h i d } } = 6$ case of the ANN models, $2 4 - 3 2$ parameters are required. We take this as an indication that other variational methods require a similar number of parameters to reach the same level of agreement with exact benchmarks.

Despite a relatively low variance and a very small error in the fidelities, the energy associated to the VANN wavefunction never quite reaches the benchmark value as $N _ { \mathrm { h i d } }$ increases. In an attempt to understand the origin of the discrepancy, we compare in Fig. 4 the exact wavefunctions (solid lines) and the $N _ { \mathrm { h i d } } = 1 0$ sigmoid (dashed) and softplus (dotted) ANN predictions for the $S$ (left panel) and $D$ states (right). The width associated to the $5 0 -$ run standard deviation is included in the ANN wavefunctions, but it is hard to see on this scale. The agreement between ANN and exact wavefunctions is excellent across a wide range of momenta, including the change of sign of the $S -$ state wavefunction around $q = 1 . 8 \ \mathrm { f m ^ { - 1 } }$ . The only region where a significant discrepancy is visible is close to the origin, $q \ < 0 . 0 5 \ \mathrm { f m ^ { - 1 } }$ . There, the softplus ANN overshoots linearly the $S -$ state wavefunction, and undershoots the $D -$ state result. While the sigmoid predictions have some inherent curvature, they still miss the quanti-

![](images/8836181fa88a8d6752bd9907f0adfbfe1894d368f1f28cd28e6ea1728ea2f269.jpg)  
Figure 4: Left (right) panel: the $S$ $( D )$ ) state wavefunction as a function of momentum. Exact wavefunctions (solid lines) are compared to the $N _ { \mathrm { h i d } } = 1 0$ ANN wavefunctions using sigmoid (dashed) and softplus (dotted) activation functions. The bands correspond to the standard deviation associated to 50 different initialisation runs.

tative dependence of $\psi _ { \mathrm { G S } }$ at low momentum.

The low-momentum mismatch is to a certain extent expected. All the integrals, including those associated to the energy cost function, carry a $q ^ { 2 }$ factor [see Eq. (3)]. Consequently, there is no energetic penalty for the VANN energy to miss the correct shape at zero momentum. As discussed further in Appendix B, the $q ^ { 2 }$ phase-space factor is also largely responsible for the constant variance in all quantities for $N _ { \mathrm { h i d } } > 1 0$ . Having said that, the presence of this factor also implies that energy differences with respect to the exact case must originate at finite momenta. Our preliminary analysis indicates that the small differences with respect to the benchmark energy value originate at relatively large momenta (in the region $2 - 1 0 \ \mathrm { f m ^ { - 1 } }$ ). The correct low-momentum boundary conditions may need to be explicitly incorporated to further improve these energy predictions. We note however that the asymptotics in this region are $L -$ dependent, $\psi ^ { L } ( q ) \approx q ^ { L }$ . Including these or any further information explicitly in the ansatz would require additional layers in the ANN, beyond the minimal philosophy of our exploratory analysis.

# 4. Conclusions

Our results show, for the first time, that VANN techniques can be used successfully in solving bound-state nuclear physics problems. We find that minimal networks with a single layer and as little as $N _ { \mathrm { h i d } } = 6$ nodes provide faithful representations of the exact wavefunction, providing binding energies within a few keV of benchmarks - or $0 . 1 \%$ in relative value. Structural properties, like $P _ { D }$ , are a by-product of the calculation and show similar levels of agreement. The variance of the models remain rather constant for a wide range of $N _ { \mathrm { h i d } }$ . We speculate that this constant variance, of the order of a fraction of a percent, arises as a consequence of the $q ^ { 2 }$ phase-space factors in all the integrals associated to physical values.

For the deuteron, these results are not yet competitive in terms of computing time. Our results however indi-

cate that very simple architectures with a small number of nodes are already good starting points, yielding accurate results. Our simple implementation using existing ML tools is effectively solving a one-body problem in relative coordinates in a fixed momentum mesh. It is not designed to solve fully fledged many-body systems. If the simplicity in the ANN ansatz could be exploited for heavier systems, the scaling in computing time of VANN techniques may remain relatively mild. If this is the case, one may be able to tackle heavier systems with this variational ab initio approach, as already demonstrated in quantum chemistry [20, 21, 22].

We foresee some bottlenecks before extending the reach of VANN techniques to higher mass numbers. First, techniques to explicitly include antisymmetrisation in the manybody wavefunction need to be developed. Recent results exploiting permutation-equivariant ANNs can provide a way forward [20]. Second, the network will have to deal with several configurations, as well as two- and threenucleon interactions. Third, and more important, it remains to be seen whether a generic extension of VANNs to incorporate arbitrary spin and isospin is possible. This may require specifically tailored deep ANN architectures. Only after these issues have been tackled, it will become clear whether ML is a competitive tool for ab initio nuclear physics.

# 5. Acknowledgments

This work is supported by the UK Science and Technology Facilities Council (STFC) through grant ST/P005314/1. We thank Pierre Arthuis and Mehdi Drissi for a careful reading of the manuscript and for useful discussions.

# Appendix A. RMSprop

We use the Root Mean Square Propagation (RMSprop) method in all the minimisation processes involved in our work [14, 35]. This deterministic approach is relatively popular in the ML community and can be thought of as an extension of the standard gradient descent method, including additional information on the second moment of the gradient. In a standard gradient descent scenario, ANN weights, $\mathcal { W } _ { t }$ , are updated at each optimisation iteration, $t$ , following the direction of maximum change in the cost function $c$ ,

$$
\mathcal {W} _ {t + 1} = \mathcal {W} _ {t} - \alpha \frac {\partial \mathcal {C}}{\partial \mathcal {W} _ {t}}. \tag {A.1}
$$

The hyperparameter $\alpha$ is generally referred to as learning rate. In contrast, in the RMSprop algorithm, the updates proceed in two steps,

$$
\mathcal {V} _ {t + 1} = \beta \mathcal {V} _ {t} + (1 - \beta) \left(\frac {\partial \mathcal {C}}{\partial \mathcal {W} _ {t}}\right) ^ {2}, \tag {A.2}
$$

$$
\mathcal {W} _ {t + 1} = \mathcal {W} _ {t} - \frac {\alpha}{\sqrt {\mathcal {V} _ {t}} + \epsilon} \frac {\partial \mathcal {C}}{\partial \mathcal {W} _ {t}}. \tag {A.3}
$$

In the first step, $\nu$ provides an exponential moving average (EMA) of the square of the gradient in the direction of a particular weight within the network. The starting point is $\mathscr { V } _ { t = 0 } = 0$ . The smoothing hyperparameter, $\beta \in \lbrack 0 , 1 )$ , controls the importance of the history of the square of the gradient. The EMA allows the recent history of the gradient to be stored efficiently. The second term, Eq. (A.3), is akin to the standard gradient descent, but the prefactor $\sqrt { \mathcal { V } _ { t } } + \epsilon$ regulates the learning rate, $\alpha$ . In this process, all weights have a learning rate that is modified to better suit the local geometry in the cost function minimisation landscape. The regularisation hyperparameter $\epsilon$ has a small value to stop any divide-by-zero errors in the event that $\nu _ { t } ~ = ~ 0$ . In our implementation, we use a learning rate $\alpha = 1 0 ^ { - 2 }$ , a smoothing constant $\beta = 0 . 9$ , and a numerical stability constant $\epsilon = 1 0 ^ { - 8 }$ . We note that PyTorch’s implementation of RMSprop differs from Tensorflow in the prefactor of Eq. (A.3), where the numerical stability constant $\epsilon$ is included within the square root.

RMSprop requires access to the explicit derivatives of the cost function with respect to the weights, $\partial \mathcal { C } / \partial \mathcal { W } _ { t }$ . These are calculated via PyTorch’s autograd library. autograd

is a form of differentiation which is not based on numerical nor symbolic methods [37].The autograd library supports reverse-mode automatic differentiation [33, 38]. This calculates the gradient of the network with respect to a given parameter by exploiting a tree map describing the dependencies of all nodes on different variables. autograd requires pre-computed derivatives at each node, and subsequently exploits the chain-rule to calculate derivatives throughout the network. A pedagogical example of the use of autograd can be found in section 3.2 of Ref. [37]. Finally, we note that we do not need to perform any derivatives of the wavefunction itself as a function of momentum $q$ . This is in contrast to real-space implementations, where gradients as a function of spatial coordinates are required to compute many-body kinetic energies.

# Appendix B. Wavefunction variance analysis

In a typical bias-variance tradeoff scenario, one expects the variance on the ANN predictions to initially decrease with $N _ { \mathrm { h i d } }$ , as the model improves its flexibility, only to see it increase above an optimal value, N opthid , as overfit- $N _ { \mathrm { h i d } } ^ { \mathrm { o p t } }$ ting takes over [14]. Instead, we find that the variance obtained as the standard deviation of 50 VANN runs remains relatively constant above $N _ { \mathrm { h i d } } \approx 1 0$ . We show this graphically in Fig. B.5, where the $N _ { \mathrm { h i d } }$ range of Fig. 3 is extended up to $N _ { \mathrm { h i d } } = 1 0 0$ . The figure clearly indicates that the variance remains constant across the whole $N _ { \mathrm { h i d } }$ range. In addition, the quality of the results in terms of difference with respect to benchmarks also saturates above a given threshold value.

We postulate that the constant variance is the result of a shortcoming of our implementation - namely the fact that we work with relative momenta in spherical coordinates. As a consequence, all the integrals associated

![](images/b8f1997327dba01c16e941c76bb3980f91c0cffc9699af9d60d78ef1469ce366.jpg)

![](images/876206992ec5e1e03354fabe72c45e2e3bc6d94520a8e9871de4cddb5ed8ffc4.jpg)  
Figure B.5: Same as Fig. 3 but with an extended range in $N _ { \mathrm { h i d } }$ . Note the change in scales in the $_ { y - }$ axis, which are significantly closer to the benchmark values here.

to physical quantities carry a $q ^ { 2 }$ prefactor, as shown in Eq. (3). This is the case for the (global) energy cost function, too. In other words, there is no penalty associated to changing the zero (or, for that matter, the low-momentum values) of the wavefunction. In principle, the wavefunction could be arbitrarily far away from the benchmark, without additional costs. In practice, however, the continuity of the activation function and its asymptotic properties at large values of input are reflected in this region. We stress that the local variability at low $q$ would not be identified in any of the global, integrated physical measures, like the energy, the fidelity or the $D -$ state probability.

We provide proof of this behaviour in Fig. B.6, where we show the equivalent to Fig. 4 for a range of values of $N _ { \mathrm { h i d } }$ . The top panel corresponds to $N _ { \mathrm { h i d } } = 2 0$ , and $N _ { \mathrm { h i d } }$ increases towards the bottom, which shows the extreme case of $N _ { \mathrm { h i d } } = 1 0 0$ . The wavefunction above $q \approx$ $0 . 1 0 ~ \mathrm { f m ^ { - 1 } }$ is reproduced by both the sigmoid and softplus ans¨atze to the wavefunctions. Towards the origin, however, both trial wavefunction struggle to reproduce the correct asymptotics. The low-momentum ANN predictions with sigmoid activation functions are much closer to the exact $S -$ state wavefunctions than the corresponding softplus ANN. For the $D -$ state, the softplus ANN generally misses the low-momentum asymptotics and undershoots the wavefunction linearly. The centroid of the sigmoid also misses the boundary condition at the origin, and in fact shows an increase in curvature as $N _ { \mathrm { h i d } }$ grows. These different behaviours towards the origin seem to reflect the bounded (sigmoid) or unbounded (softplus) nature of the

![](images/81e228ab82b05212673ed32a84101a23f61f2a5d54cd435e0707628d164892e2.jpg)

![](images/d8962ab494ed04664fc09a66576fac22244ef5b9b9a647d8a6b51259993e7e3f.jpg)

![](images/8130e2d1555bab9bcbbb47b6863f61e2964a399212ddafa09fcc9280516626e8.jpg)

![](images/546b06bf4877fb43d3bd6121b7b3ee473c75dfcb4abaf7000d64bc312f0fd014.jpg)

![](images/2d1ee5e8121569279bc05b038563f3a5cb1068939c4b0662055c8c9f56060ad0.jpg)

![](images/e7c61c02e109226baa0b67be17150ae14343b41dfb1d55fb8c39250b7b8e874e.jpg)

![](images/8f83418cfd3d85c7174e7a4942dcd819648d56dc2fe8b599734d99d53185465c.jpg)

![](images/f2a4a277b0d9b0cf98ec9e91cde1c10fb2982177aa6e8d45797519cbd357b286.jpg)

![](images/273f495e52c7e0a55d1a0cf8e3d6295fcf00bed68ad653e31d3c9f79af8cca75.jpg)

![](images/4213abb8e91763ec75102412e6500ac6d90b7a8d80b8e2ce264fd46d3b6b55da.jpg)  
Figure B.6: Same as Fig. 4, but for increasing values of $N _ { \mathrm { h i d } }$ from $N _ { \mathrm { h i d } } = 2 0$ (top row) to $N _ { \mathrm { h i d } } = 1 0 0$ (bottom row).

activation functions at large values of input.

Our arguments relate to the size of the bands towards the origin, shown in the insets. These figures demonstrate that the variance in the low-momentum values of the wavefunction increases with $N _ { \mathrm { h i d } }$ . As opposed to global integrated measures, local regions of the wavefunction are subject to a bias-variance trade-off. We take this as an indication that, above a certain threshold value of $N _ { \mathrm { h i d } } ^ { \mathrm { o p t } }$ hid an , increase in ANN complexity does not bring in an increase in wavefunction quality.

More details are provided in Fig. B.7. Rather than showing the wavefunction itself, we focus here on the standard deviation of the wavefunction, $\sigma _ { \psi ^ { L } }$ , i.e. the width of the bands in Fig. B.6. This is shown as a function of momentum in a log-log scale, to magnify the differences. Left (right) panels correspond to sigmoid (softplus) activation functions, and top (bottom) panels show results for the $S -$ $( D - )$ state. Different lines correspond to different values of $N _ { \mathrm { h i d } }$ . First, we reiterate the message that the variance of the wavefunction is maximal at the lowest momenta. In fact, the variance decreases sharply above $q \approx 1 ~ \mathrm { f m ^ { - 1 } }$ . Second, the $N _ { \mathrm { h i d } }$ dependence is also rather informative, as it indicates that the minimal variance in all the models is reached around $N _ { \mathrm { h i d } } ^ { \mathrm { o p t } } \approx 2 0$ . Values of $N _ { \mathrm { h i d } }$ below or above the optimum value provide larger variances in wavefunctions. For the optimal value in the Figure, the differences between the underlying activation functions are small for the $S -$ state, and within a factor of 2 for the $D -$ state.

Finally, the dependence of $\sigma _ { \psi ^ { L } }$ on $N _ { \mathrm { h i d } }$ is also prone to relatively large jumps, as seen in the softplus $S -$ state results between $N _ { \mathrm { h i d } } = 4 0$ and 60 or in the sigmoid $D -$ state predictions between $N _ { \mathrm { h i d } } = 2 0$ and 40. A more detailed analysis may be needed to fully understand the origin, shape and $N _ { \mathrm { h i d } }$ dependence of these structures. Alternatively, it may be more interesting to incorporate the knowledge of low-momentum asymptotics in the ANN ansatz. In real-space implementations for electronic structure, the exponentially decaying asymptotics at large distances and the corresponding cusp conditions are known, and deliberately coded into the ANN as an additional layer [20, 21]. In the case of the deuteron, the implementation of the $L -$ dependent boundary conditions would require an additional layer in the network to match wavefunctions into analytical behaviours at low values of momentum. We leave the analysis of these types of extensions for future work.

# References

[1] MacKay D J C 2003 Information Theory, Inference, and Learning Algorithms 1st ed (Cambridge University Press) ISBN 9780521642989   
[2] Feindt M and Kerzel U 2006 Nucl. Instrum. Meth. A 559 190 proceedings of the X International Workshop on Advanced Computing and Analysis Techniques in Physics Research URL http://www.sciencedirect.com/science/article/pii/ S0168900205022679

![](images/c0ebd7e355a96f8d44472c048d2b6b9d468cfd4e48c2fbef8fea2f45a88dc39c.jpg)

![](images/6e70e18f3b698de05caae02a697227308beb4a4cde440703a34b5500baa0742a.jpg)

![](images/b02562b97a0b22fa1944ac49945b586fb5bf5ff2ccf057c2b190ba38f5433b51.jpg)

![](images/4dc7ce2945f8d885e5a984f285ce6eed6028ba78d49cebd9cbc6e632f0f828c3.jpg)  
Figure B.7: Top panels: standard deviation of the $S -$ state wavefunction obtained after 50 minimisation runs as a function of momentum for the sigmoid (left) and softplus (right) activation functions. Different lines correspond to different values of $N _ { \mathrm { h i d } }$ . Bottom panels: the same for the $D -$ state.

[3] Ball R D, Debbio L D, Forte S, Guffanti A, Latorre J I, Rojo J and Ubiali M 2010 Nuc. Phys. B 838 136 URL http://www. sciencedirect.com/science/article/pii/S0550321310002853   
[4] Gernoth K, Clark J, Prater J and Bohr H 1993 Phys. Lett. B 300 1–7 URL https://www.sciencedirect.com/science/ article/abs/pii/0370269393907384   
[5] Gazula S, Clark J and Bohr H 1992 Nucl. Phys. A 540 1–26 URL https://www.sciencedirect.com/science/article/abs/ pii/037594749290191L   
[6] Utama R, Piekarewicz J and Prosper H B 2016 Phys. Rev. C 93 014311 URL https://link.aps.org/doi/10.1103/PhysRevC. 93.014311   
[7] Wang Z A, Pei J, Liu Y and Qiang Y 2019 Phys. Rev. Lett. 123 122501 URL https://link.aps.org/doi/10.1103/ PhysRevLett.123.122501   
[8] Niu Z M, Liang H Z, Sun B H, Long W H and Niu Y F 2019 Phys. Rev. C 99(6) 064307 URL https://link.aps.org/doi/ 10.1103/PhysRevC.99.064307   
[9] Freitas P S A and Clark J W 2019 Experiments in machine learning of alpha-decay half-lives (Preprint 1910.12345) URL http://arxiv.org/abs/1910.12345   
[10] Lasseri R D, Regnier D, Ebran J P and Penon A 2020 Phys. Rev. Lett. 124(16) 162502 URL https://link.aps.org/doi/ 10.1103/PhysRevLett.124.162502   
[11] Negoita G A, Luecke G R, Vary J P, Maris P, Shirokov A M, Shin I J, Kim Y, Ng E G and Yang C 2018 (Preprint 1803. 03215) URL http://arxiv.org/abs/1803.03215   
[12] Jiang W G, Hagen G and Papenbrock T 2019 Phys. Rev. C 100(5) 054326 URL https://link.aps.org/doi/10.1103/ PhysRevC.100.054326   
[13] Dunjko V and Briegel H J 2018 Rep. Prog. Phys. 81 074001 URL https://doi.org/10.1088/1361-6633/aab406   
[14] Mehta P, Bukov M, Wang C H, Day A G, Richardson C, Fisher C K and Schwab D J 2019 Phys. Rep. 810 1–124 URL https: //doi.org/10.1016/j.physrep.2019.03.001   
[15] Carleo G, Cirac I, Cranmer K, Daudet L, Schuld M, Tishby N, Vogt-Maranto L and Zdeborov´a L 2019 Rev. Mod. Phys. 91(4) 045002 URL https://link.aps.org/doi/10.1103/ RevModPhys.91.045002   
[16] Carleo G and Troyer M 2017 Science 355 602 URL https: //doi.org/10.1126/science.aag2302   
[17] Choo K, Carleo G, Regnault N and Neupert T 2018

Phys. Rev. Lett. 121 167204 URL https://doi.org/10.1103/ PhysRevLett.121.167204   
[18] Saito H 2017 J. Phys. Soc. Japan 86 093001 URL https:// journals.jps.jp/doi/10.7566/JPSJ.86.093001   
[19] Saito H 2018 J. Phys. Soc. Japan 87 074002 URL https:// journals.jps.jp/doi/10.7566/JPSJ.87.074002   
[20] Pfau D, Spencer J S, Matthews A G d G and Foulkes W M C 2019 Ab-Initio Solution of the Many-Electron Schr¨odinger Equation with Deep Neural Networks arxiv:1909.02487 URL http://arxiv.org/abs/1909.02487   
[21] Hermann J, Sch¨atzle Z and No´e F 2019 Deep neural network solution of the electronic Schr¨odinger equation arxiv:1909.08423 URL http://arxiv.org/abs/1909.08423   
[22] Choo K, Mezzacapo A and Carleo G 2020 Nat. Commun. 11 2368 URL https://doi.org/10.1038/s41467-020-15724-9   
[23] Adams C, Carleo G, Lovato A and Rocco N 2020 Variational Monte Carlo calculations of $A \leq 4$ nuclei with an artificial neural-network correlator ansatz arxiv:2007.14282 URL http://arxiv.org/abs/2007.14282   
[24] Gao X and Duan L M 2017 Nat. Commun. 8 1 URL https: //doi.org/10.1038/s41467-017-00705-2   
[25] Dumitrescu E F, McCaskey A J, Hagen G, Jansen G R, Morris T D, Papenbrock T, Pooser R C, Dean D J and Lougovski P 2018 Phys. Rev. Lett. 120(21) 210501 URL https://link.aps. org/doi/10.1103/PhysRevLett.120.210501   
[26] Hochreiter S, Bengio Y, Frasconi P and Schmidhuber J 2001 A Field Guide to Dynamical Recurrent Networks ed Kremer S C and Kolen J F (Wiley-IEEE Press) chap Gradient flow in recurrent nets: the difficulty of learning long-term dependencies   
[27] Bogner S and Furnstahl R 2006 Phys. Lett. B 632 501 – 506 URL http://www.sciencedirect.com/science/article/ pii/S0370269305015923   
[28] Bogner S and Furnstahl R 2006 Phys. Lett. B 639 237 – 241 URL http://www.sciencedirect.com/science/article/ pii/S0370269306007350   
[29] Anderson E R, Bogner S K, Furnstahl R J and Perry R J 2010 Phys. Rev. C 82 054001 URL https://link.aps.org/doi/10. 1103/PhysRevC.82.054001   
[30] Entem D R and Machleidt R 2003 Phys. Rev. C 68 041001 URL http://link.aps.org/doi/10.1103/PhysRevC.68.041001   
[31] Cybenko G 1989 Math. Control. Signals, Syst. 2 303–314 URL http://link.springer.com/10.1007/BF02551274   
[32] Hornik K 1991 Neural Networks 4 251–257 URL https://www.sciencedirect.com/science/article/pii/ 089360809190009T?via{%}3Dihub   
[33] Paszke A, Gross S, Chintala S, Chanan G, Yang E, DeVito Z, Lin Z, Desmaison A, Antiga L and Lerer A 2017 Automatic differentiation in PyTorch NIPS Autodiff Workshop URL https://pytorch.org/   
[34] Glorot X and Bengio Y 2010 Understanding the difficulty of training deep feedforward neural networks Proceedings of the thirteenth international conference on artificial intelligence and statistics pp 249–256   
[35] Tieleman T and Hinton G 2012 Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude COURSERA: Neural networks for machine learning URL https://www.cs.toronto.edu/ tijmen/csc321/slides/ lecture_slides_lec6.pdf   
[36] Rios A and Keeble JWT T 2020 In preparation   
[37] Baydin A G, Pearlmutter B A, Radul A A and Siskind J M 2017 J. Mach. Learn. Res. 18 5595–5637   
[38] Paszke A, Gross S, Massa F, Lerer A, Bradbury J, Chanan G, Killeen T, Lin Z, Gimelshein N, Antiga L, Desmaison A, Kopf A, Yang E, DeVito Z, Raison M, Tejani A, Chilamkurthy S, Steiner B, Fang L, Bai J and Chintala S 2019 Pytorch: An imperative style, high-performance deep learning library Advances in Neural Information Processing Systems 32 ed Wallach H, Larochelle H, Beygelzimer A, dAlche-Buc F, Fox E and Garnett R (Curran Associates, Inc.) pp 8024–8035 URL http://papers.neurips.cc/paper/ 9015-pytorch-an-imperative-style-high-performance-deep-

pdf