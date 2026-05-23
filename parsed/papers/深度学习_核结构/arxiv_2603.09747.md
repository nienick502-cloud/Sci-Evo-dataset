# Architecture as physical prior: cooperative neural network for nuclear masses

Peiwen Zai ,1, ∗ Wei Cheng,1, 2 and Feng-Shou Zhang 1, 3, 4, †

1The Key Laboratory of Beam Technology of Ministry of Education,

School of Physics and Astronomy, Beijing Normal University, Beijing 100875, China

2Advanced Institute of Natural Sciences, Beijing Normal University at Zhuhai, Zhuhai 519087, China

3Institute of Radiation Technology, Beijing Academy of Science and Technology, Beijing 100875, China

$^ 4$ Center of Theoretical Nuclear Physics, National Laboratory of Heavy Ion Accelerator of Lanzhou, Lanzhou 730000, China

(Dated: March 11, 2026)

Machine learning approaches to nuclear mass prediction have achieved remarkable accuracy, but typically rely on existing theoretical baselines or hand-crafted physics features. Here we demonstrate that these prerequisites can be supplanted by structural inductive biases embedded directly in the network architecture. We present the Cooperative Neural Network (CoNN), which predicts binding energies from raw proton and neutron numbers $( Z , N )$ alone by additively combining four structurally constrained modules: a smooth network for bulk liquid-drop trends, discrete scalar embeddings for shell effects, a learnable two-dimensional grid for regional collective correlations, and a parity-aware network for odd–even staggering. On the AME2020 dataset, the CoNN achieves a root-mean-square deviation of 0.269 MeV across all 3558 nuclei, with 0.419 MeV on a held-out interpolation subset and 0.728 MeV on 122 nuclei newly measured since AME2016, placing it among the most accurate baseline-free approaches to direct mass prediction. Notably, the learned embeddings develop pronounced extrema at canonical magic numbers and the pairing module reproduces the expected odd–even staggering along isotopic chains, both emerging from the data without explicit supervision. These results demonstrate that physically motivated architectural constraints can effectively substitute for feature engineering, establishing architecture as physical prior as a promising paradigm for neural-network mass modeling.

# I. INTRODUCTION

Nuclear binding energies encode fundamental information about nuclear stability, decay energetics, and reaction thresholds [1, 2]. Reliable mass predictions far from stability are essential for modeling nucleosynthesis, particularly the rapid neutron-capture process ( $T$ -process), whose path traverses neutron-rich nuclei that remain experimentally inaccessible [3, 4]. The latest Atomic Mass Evaluation (AME2020) [5] compiles binding energies for 3558 nuclides, but theoretical estimates place the total number of bound nuclei at 7000–10000 [6–8], leaving a large region that must be covered by theoretical or datadriven extrapolation.

Global mass models fall into two broad classes [1, 9]. Microscopic approaches based on nuclear density functional theory (DFT) [10–13], including non-relativistic Skyrme/Gogny Hartree–Fock–Bogoliubov and covariant mean-field formulations, provide a self-consistent treatment of nuclear structure across the chart. Their predictive accuracy is typically limited to root-mean-square deviations (RMSDs) of 0.5–0.8 MeV [9], reflecting both the incomplete treatment of many-body correlations and the constraints of current energy-density functionals. Macroscopic–microscopic models often achieve higher accuracy by combining a smooth liquid-drop energy with shell and pairing corrections evaluated from a singleparticle potential [14–17]. Representative models such

as FRDM2012 [15] and WS4 [16] achieve RMSDs of 0.3– 0.6 MeV. The physical insight underlying these models— that binding energies decompose naturally into a smooth bulk contribution and oscillatory microscopic corrections [14, 17]—has proven remarkably effective and will serve as a guiding principle for the present work.

In recent years, machine-learning (ML) methods have become an active complement to traditional mass models [18, 19]. A highly successful strategy is residual correction: an ML model is trained on the difference $\Delta B =$ $B _ { \mathrm { e x p } } \ : - \ : B _ { \mathrm { t h } }$ between experiment and a chosen theoretical baseline, learning the systematic deficiencies of the baseline. Using Bayesian neural networks [20–24], kernel methods [25, 26], and various deep architectures [27– 29], such hybrid approaches have achieved RMSDs of 80– $1 7 0 \mathrm { k e V }$ . Although highly accurate, these approaches are fundamentally tethered to pre-existing theoretical baselines, acting as model-specific error patches rather than standalone predictive frameworks.

Direct prediction from the minimal identifiers $( Z , N )$ , without a theoretical baseline, is considerably more demanding: the network must learn the entire 2000 MeV range of binding energies from scratch [5]. Standard feed-forward neural networks in this setting exhibited RMSDs at the MeV level, a limitation that persists even when the number of parameters is substantially increased [30, 31], reflecting the intrinsic difficulty of resolving the multi-scale structure of the mass surface within a single unstructured architecture [32]. Subsequent work improved accuracy by supplementing $( Z , N )$ with physics-motivated input features—parity indicators, distances to shell closures, or isospin-asymmetry ratios—

typically reaching RMSDs of 0.2–0.5 MeV [33, 34]. While effective, this approach requires domain expertise to design the features, and different input feature choices can materially affect extrapolation behavior [28, 30, 34].

In this work, we pursue an alternative strategy: rather than encoding physical knowledge through hand-crafted input features, we embed it into the network architecture itself. The guiding idea is the macroscopic–microscopic decomposition: since binding energies are well described as a sum of a smooth bulk term and microscopic corrections (shell, collective, and pairing), we construct a modular network whose components are each structurally constrained to capture one type of contribution. We refer to the complete model as a Cooperative Neural Network (CoNN). The only input is the pair $( Z , N )$ ; no external theoretical baseline or additional features are used. An alternating training protocol anchors the macroscopic branch on smooth trends before resolving microscopic corrections, mirroring the traditional approach of fitting bulk properties first. On the AME2020 benchmark, the CoNN achieves an RMSD of 0.269 MeV on all 3558 nuclei, 0.419 MeV on the 20% held-out interpolation subset, and 0.728 MeV on the 122 nuclei newly measured since AME2016, with the learned components recovering clear shell-closure signatures and odd–even staggering patterns without explicit supervision.

The paper is organized as follows. Section II describes the model architecture and training procedure. Section III presents results and examines the physical content of the learned decomposition. Section IV summarizes our findings and discusses limitations and future directions.

# II. METHODOLOGY

The CoNN takes only $( Z , N )$ as input and decomposes the predicted binding energy into a smooth macroscopic term and three microscopic corrections—shell, collective, and pairing—each produced by a dedicated module. In the following, we describe the dataset (Sec. II A), the architecture of each module and its physical motivation (Sec. II B), and the alternating training procedure that enforces the separation between macroscopic and microscopic contributions (Sec. II C).

# A. Data

We use binding energies from the AME2020 [5] evaluation as reference truth labels. The dataset is split according to measurement availability across AME editions: the 3436 nuclei present in AME2016 [35] are randomly partitioned into training and validation subsets in an 80:20 ratio. The 122 nuclei appearing in AME2020 but absent from AME2016 constitute an extrapolation test set; these lie predominantly near the boundaries of the known nuclear chart (see Fig. 1). This temporal split ensures

that no newly measured nucleus leaks into training and cleanly separates interpolation from boundary extrapolation. The distribution of the three subsets on the $( N , Z )$ chart is shown in Fig. 1.

![](images/753864589c7356154505ab5c9e5f862a9feb181d79c3048f281373042bdce50e.jpg)  
FIG. 1. Distribution of nuclei on the $( N , Z )$ chart. Gray: training set (80% of the AME2016 pool); red: validation set (remaining $2 0 \%$ ); blue: extrapolation set (nuclei in AME2020 but absent from AME2016). Dashed lines indicate magic numbers.

# B. Model architecture

Following the macroscopic–microscopic picture, we decompose the predicted binding energy into a smooth bulk term and three structured microscopic corrections:

$$
\begin{array}{l} B _ {\text {p r e d}} = E _ {\text {M a c r o}} + E _ {\text {M i c r o}}, \\ \begin{array}{l} E _ {\text {p r e d}} = E _ {\text {M a c r o}} + E _ {\text {M i c r o}}, \\ E _ {\text {M i c r o}} = E _ {\text {S h e l l}} + E _ {\text {C o r}} + E _ {\text {P a i r}}. \end{array} \tag {1} \\ \end{array}
$$

Here $E _ { \mathrm { M a c r o } }$ denotes the smooth bulk energy, $E _ { \mathrm { S h e l l } }$ the shell effect, $E _ { \mathrm { { C o r } } }$ the regional correlation, and $E _ { \mathrm { P a i r } }$ the odd–even pairing. Each term is produced by a dedicated module whose architecture restricts the class of functions it can represent. Specifically, $E _ { \mathrm { M a c r o } }$ is parameterized by a fully connected network treating $( Z , N )$ as continuous inputs; $E _ { \mathrm { S h e l l } }$ by discrete scalar embeddings indexed by $Z$ and $N$ ; $E _ { \mathrm { { C o r } } }$ by a learnable two-dimensional grid with bilinear interpolation; and $E _ { \mathrm { P a i r } }$ by a small parity-aware network. The overall architecture is illustrated in Fig. 2.

Macroscopic branch. The dominant contribution to nuclear binding energies varies smoothly with $( Z , N )$ , as captured by the liquid-drop model [1, 36]. We parameterize $E _ { \mathrm { M a c r o } }$ with a fully connected network that takes $( Z , N )$ as input:

$$
E _ {\text {M a c r o}} (Z, N) = \mathcal {D} (\mathcal {E} (Z, N)), \tag {2}
$$

where $\varepsilon$ is an encoder mapping to a 16-dimensional representation through three hidden layers of width 128 with

![](images/952cb5f84bdc27d2daf8c2f1d8e9b29425158f5f8d9f728dce29582b2b0a8ffb.jpg)  
FIG. 2. Architecture of the CoNN model. The binding energy is decomposed into a macroscopic contribution from the bulkproperties network and microscopic corrections from three modules: shell embeddings, a regional correlation grid, and a pairing network. The four outputs are summed to yield $B _ { \mathrm { p r e d } }$ .

LeakyReLU activations, and $\mathcal { D }$ is a decoder with the mirrored layer structure, mapping back to a scalar. The narrow bottleneck caps the maximum number of independent modes of variation in the output, limiting the effective complexity of the learned function [37]. Combined with the spectral bias of gradient-based optimization, which causes fully connected networks to preferentially learn low-frequency components [38, 39], this makes the branch a natural parameterization for the slowly varying bulk energy. Any residual structure (shell effects, deformation, pairing) would be captured by the microscopic modules.

Shell embeddings. Shell closures produce kinks in the mass surface at magic numbers that a smooth function cannot efficiently represent [1, 14, 40]. We capture these with learnable scalar embeddings:

$$
E _ {\mathrm {S h e l l}} (Z, N) = e _ {Z} [ Z ] + e _ {N} [ N ], \qquad (3)
$$

where $e _ { Z } \in \mathbb { R } ^ { Z _ { \operatorname* { m a x } } + 1 }$ and $e _ { N } \ \in \mathbb { R } ^ { N _ { \operatorname* { m a x } } + 1 }$ are trainable vectors. Each proton number and neutron number receives an independent energy correction, analogous to the independent-particle picture in which proton and neutron shell closures arise from separate single-particle spectra [41, 42]. The additive, separable form means that correlations between proton and neutron degrees of freedom—shell evolution, enhanced binding at doublymagic nuclei [43, 44]—are not captured here but delegated to the correlation grid.

Regional correlation grid. To capture effects that depend on both nucleon numbers jointly, we introduce a learnable two-dimensional parameter grid $\mathbf { G } \in \mathbb { R } ^ { H \times W }$ (where $H = 5 0$ and $W = 6 0$ correspond to the $Z$ and $N$

dimensions, respectively) spanning the nuclear chart:

$$
E _ {\mathrm {C o r}} (Z, N) = \operatorname {I n t e r p} (\mathbf {G}, z _ {g}, n _ {g}), \tag {4}
$$

where $( z _ { g } , n _ { g } ) \in [ - 1 , 1 ] ^ { 2 }$ are normalized coordinates and the interpolation is bilinear. The finite grid resolution and bilinear interpolation enforce spatial continuity, preventing the grid from fitting individual nuclei while allowing it to resolve coherent regional structures spanning several nucleon numbers.

Pairing network. None of the preceding modules can efficiently represent the rapid odd–even staggering caused by nuclear pairing correlations, which systematically modulates the binding energy depending on the parity of the nucleon numbers and constitutes a contribution of order 1 MeV [45]. We isolate this high-frequency component with a small multilayer perceptron (MLP; one hidden layer of width 32 with SiLU activation):

$$
E _ {\mathrm {P a i r}} (Z, N) = \mathrm {M L P} \left(\left[ \pi_ {Z}, \pi_ {N}, \frac {Z}{1 0 0}, \frac {N}{1 0 0} \right]\right), \qquad (5)
$$

where $\pi _ { Z } = Z$ mod 2 and $\pi _ { N } = N$ mod 2 are nucleonnumber parities extracted by the built-in modulo operation, distinguishing the four parity classes (even–even, even–odd, odd–even, odd–odd), and the continuous inputs Z/100, $N / 1 0 0$ are rescaled to match the magnitude of the standardized inputs used elsewhere in the model. Like an activation function or positional encoding, the modulo operation is a fixed, non-learnable transformation applied within the architecture; it introduces no external information beyond $( Z , N )$ themselves.

The complete model has approximately $7 . 4 \times 1 0 ^ { 4 }$ parameters: 71,000 in the macroscopic branch and 3,400 in the microscopic modules combined. To isolate the

effect of architectural priors from parameter increasing, we also prepare a plain MLP with a matched parameter count ( ${ \sim } 7 . 4 \times 1 0 ^ { 4 }$ ; 8 hidden layers, width 102), trained on the same dataset for the same number of epochs as a baseline model without structural constraints.

# C. Training protocol

All modules are trained to minimize the mean-squared error on the experimental binding energies, $\begin{array} { r l } { { \mathcal { L } } ( \theta ) } & { { } = } \end{array}$ $\begin{array} { r } { n ^ { - 1 } \sum _ { i } \left( B _ { \mathrm { p r e d } } ^ { ( i ) } - B _ { \mathrm { e x p } } ^ { ( i ) } \right) ^ { : _ { } } } \end{array}$ , utilizing full-batch gradient descent. A central challenge in training a decomposed model is preventing the components from learning each other’s intended contributions [47, 48]: the macroscopic branch may absorb microscopic fluctuations, or the microscopic modules may fit global bulk trends. We address this with a two-phase alternating protocol. Such stagewise approaches are known to simplify the optimization of modular architectures by sequentially injecting information into the training process [49, 50].

In the first phase (warmup), the macroscopic branch is trained alone on the standardized target $y _ { \mathrm { s t d } } = ( B _ { \mathrm { e x p } } -$ $\mu _ { y } ) / \sigma _ { y }$ with Adam [51] (learning rate $\alpha _ { \mathrm { M a c r o } } = 2 \times 1 0 ^ { - 4 }$ ), establishing a smooth baseline before the microscopic modules are introduced. In the second phase (cooperative training), the two groups of parameters are updated in alternating rounds until convergence:

1. Macroscopic step: freeze the microscopic modules and train the macroscopic branch on the target $y _ { \mathrm { M a c r o } } = ( B _ { \mathrm { e x p } } - E _ { \mathrm { S h e l l } } ^ { * } - E _ { \mathrm { C o r } } ^ { * } - E _ { \mathrm { P a i r } } ^ { * } - \mu _ { y } ) / \sigma _ { y }$ where asterisks denote values held fixed during the current step, with Adam ( $\alpha _ { \mathrm { M a c r o } } = 2 \times 1 0 ^ { - 4 }$ ).   
2. Microscopic step: freeze the macroscopic branch and train all microscopic modules on the residual $y _ { \mathrm { M i c r o } } = B _ { \mathrm { e x p } } - E _ { \mathrm { M a c r o } } ^ { \ast }$ with AdamW [52] ( $\alpha _ { \mathrm { M i c r o } } =$ $2 \times 1 0 ^ { - 3 }$ , weight decay $1 0 ^ { - 3 }$ ).

The 10:1 learning-rate ratio $\alpha _ { \mathrm { M i c r o } } / \alpha _ { \mathrm { M a c r o } }$ is the key asymmetry: it anchors the macroscopic branch to smooth trends while allowing the microscopic modules to adapt more rapidly to structured residuals. Both optimizers follow cosine-annealing schedules [53], and the best model state, selected by its performance on the validation set, is retained for final evaluation.

To reduce variance, we train an ensemble of $N _ { \mathrm { e n s } } = 5$ models with different initialization seeds [54]. The final prediction is the ensemble mean B¯pred = N −1ens ∑k B(k)pred, $\begin{array} { r } { \bar { B } _ { \mathrm { p r e d } } = N _ { \mathrm { e n s } } ^ { - 1 } \sum _ { k } B _ { \mathrm { p r e d } } ^ { ( k ) } } \end{array}$ k pred， and the ensemble standard deviation serves as a practical indicator of model disagreement, without claiming a calibrated posterior [55–57].

# III. RESULTS AND DISCUSSION

In this section, we first evaluate the overall and extrapolation performance of the CoNN model against ex-

isting baselines (Sec. III A), then analyze the physically interpretable structures emerging from the modular decomposition (Sec. III B), and finally assess the model’s reliability on derived physical quantities such as separation energies (Sec. III C). For consistency throughout this discussion, all reported accuracy metrics refer to the ensemble mean over the five independently trained models.

# A. Overall accuracy and comparison

Table I summarizes representative physics and ML approaches. The most informative comparison for the present approach is with other baseline-free ML models. In that setting, models using only $( Z , N )$ as inputs struggle to reduce the RMSD significantly below 0.8 MeV (ANN2: 1.180 MeV; KAN-2: 0.870 MeV), whereas adding engineered physics features reduces the RMSD to 0.200– 0.260 MeV (ANN7 and KAN-11) [34, 46]. With the same two inputs $( Z , N )$ and no external baseline, CoNN reaches 0.269 MeV on all 3558 nuclei in AME2020. This result is close to KAN-11 (0.260 MeV, 11 features) and substantially lower than the other 2-feature direct models, showing that physically motivated architectural constraints can recover most of the gain commonly obtained from feature engineering.

To confirm that the improvement originates from architectural design rather than increased model size, we trained a plain MLP with a matched parameter budget ( ${ \sim } 7 . 4 \times 1 0 ^ { 4 }$ ; 8 hidden layers, width 102) under identical conditions: the same $( Z , N )$ inputs, data split, ensemble size, and total number of gradient steps. This parametermatched MLP achieves an ensemble RMSD of 0.836 MeV on all 3558 AME2020 nuclei and 1.232 MeV on the 122 extrapolation nuclei (Table I), both much larger than the corresponding CoNN values (0.269 and 0.728 MeV). The comparison demonstrates that the CoNN’s accuracy gain is not attributable to the number of trainable parameters but to the inductive biases imposed by the modular architecture and cooperative training protocol.

The residual maps in Fig. 3 illustrate the effect of each module through ablation. Panel (a) shows the FRDM2012 spherical macroscopic residual as a reference for global bulk structure [15]. Panel (b), the CoNN macroscopic branch alone (RMSD = 2.114 MeV), reproduces the broad arc-like residual bands seen in panel (a), with clear shell-closure signatures and deformation structures consistent with the FRDM2012 macroscopic residual. Panel (c), after adding shell embeddings, the correlation grid, and the pairing network, the full CoNN model (RMSD = 0.237 MeV, an 89% reduction) removes most systematic residual structure. Panel (d), the CoNN without the pairing module ( $\mathrm { R M S D } = 1 . 2 5 7 \mathrm { M e V }$ ), restores the checkerboard pattern characteristic of odd–even staggering, indicating that odd–even staggering is the largest single contributor to the overall RMSD among the microscopic corrections, as it affects virtually every nucleus rather than being localized near shell closures.

TABLE I. Comparison of representative nuclear mass models and ML approaches. The overall RMSD ( $\sigma _ { \mathrm { r m s } }$ ) is evaluated on the dataset and number of nuclei indicated in each row. The “Baseline” column indicates whether a theoretical mass model is used to define a residual target, and “Features” counts the input features for ML models. Where available, the extrapolation RMSD is evaluated on nuclei absent from the respective training dataset but included in a later AME edition, with the number of test nuclei listed.   

<table><tr><td rowspan="2">Model</td><td rowspan="2">Baseline</td><td rowspan="2">Features</td><td colspan="3">Overall Accuracy</td><td colspan="2">Extrapolation</td></tr><tr><td>σrms (MeV)</td><td>Nuclei</td><td>Data</td><td>σrms (MeV)</td><td>Nuclei</td></tr><tr><td colspan="8">Macroscopic-microscopic physics models</td></tr><tr><td>WS4 [16]</td><td>—</td><td>—</td><td>0.298</td><td>2353</td><td>AME2012</td><td>1.295</td><td>120a</td></tr><tr><td>FRDM2012 [15]</td><td>—</td><td>—</td><td>0.560</td><td>2149</td><td>AME2003</td><td>2.444</td><td>120a</td></tr><tr><td colspan="8">Machine learning: residual correction</td></tr><tr><td>BML [24]</td><td>Yesb</td><td>3</td><td>0.084</td><td>2271*</td><td>AME2016</td><td>0.170</td><td>51*</td></tr><tr><td colspan="8">Machine learning: direct prediction, (Z,N) only</td></tr><tr><td>ANN2 [34]</td><td>No</td><td>2</td><td>1.180</td><td>3556</td><td>AME2016</td><td>1.050</td><td>122</td></tr><tr><td>KAN-2 [46]</td><td>No</td><td>2</td><td>0.870</td><td>3456</td><td>AME2020</td><td>—</td><td>—</td></tr><tr><td>MLPc</td><td>No</td><td>2</td><td>0.836</td><td>3558</td><td>AME2020</td><td>1.232</td><td>122</td></tr><tr><td colspan="8">Machine learning: direct prediction, with engineered features</td></tr><tr><td>ANN7 [34]</td><td>No</td><td>7</td><td>0.200</td><td>3556</td><td>AME2016</td><td>0.340</td><td>122</td></tr><tr><td>KAN-11 [46]</td><td>No</td><td>11</td><td>0.260</td><td>3456</td><td>AME2020</td><td>—</td><td>—</td></tr><tr><td colspan="8">This work: direct prediction, (Z,N) with architectural constraints</td></tr><tr><td>CoNN</td><td>No</td><td>2</td><td>0.269</td><td>3558</td><td>AME2020</td><td>0.728</td><td>122</td></tr></table>

a Evaluated on the same 122-nuclei extrapolation set, excluding $^ { 1 1 } \mathrm { O }$ and $^ { 1 3 } \mathrm { F }$ , which are absent from the WS4 and FRDM2012 mass tables.   
b Weighted combination of BNNs trained on eight different mass models (FRDM2012, WS4, HFB-31, etc.).   
c Plain MLP with ${ \sim } 7 . 4 \times 1 0 ^ { 4 }$ parameters, matching the CoNN parameter count.   
* Estimated from the filtering criteria described in the original reference; not explicitly reported.

For out-of-sample performance, CoNN gives 0.419 MeV on the $2 0 \%$ held-out interpolation subset ( $n \ = \ 6 8 8$ ), and 0.728 MeV on the 122 nuclei newly appearing in AME2020. Within the same baseline-free setting and test dataset, CoNN reduces the extrapolation RMSD from 1.05 MeV (ANN2, two inputs) to 0.728 MeV through architectural inductive biases alone, though a gap remains relative to ANN7 (0.34 MeV), which supplements $( Z , N )$ with five hand-crafted inputs: parity indicators $Z _ { \mathrm { E O } }$ and $N _ { \mathrm { E O } }$ , distances to the nearest magic numbers $\Delta Z$ and $\Delta N$ , and an isospin-asymmetry parameter [34]. Evaluated on the same extrapolation set (120 of the 122 nuclei; see Table I), FRDM2012 [15] and WS4 [16] yield RMSDs of 2.444 and 1.295 MeV, respectively, both substantially larger than the CoNN value. The dominant source of error for both physics models is the superheavy region ( $Z \ = \ 1 1 1 { - } 1 1 5$ ), where FRDM2012 residuals reach $5 -$ 6 MeV and WS4 residuals 2–3 MeV as evaluated using the published mass tables, whereas the CoNN maintains an RMSD of 0.631 MeV on the same 12 superheavy nuclei. Residual-correction hybrids can achieve lower extrapolation RMSD (e.g. BML: 0.170 MeV [24]), but they address a different problem setting by inheriting the knowledge from baseline theoretical models. Overall, these comparisons show that the CoNN can achieve competitive direct-prediction accuracy with only $( Z , N )$ inputs, outperforming established macroscopic–microscopic models

on newly measured nuclei.

# B. Learned microscopic structures

A central question for the modular approach is whether the architectural constraints lead to physically interpretable components. Figure 4 shows the learned proton and neutron embedding biases [Eq. (3)]. Despite the absence of magic-number labels in the training objective, the embeddings develop pronounced local extrema near the canonical magic numbers $\textit { Z } = \ 2 0 , 2 8 , 5 0 , 8 2$ and $N ~ = ~ 2 0 , 2 8 , 5 0 , 8 2 , 1 2 6$ . The physical interpretation is straightforward: shell closures correspond to large gaps in the single-particle spectrum [40], producing energy shifts that the discrete embeddings are uniquely positioned to absorb. The smooth macroscopic branch cannot represent these discontinuous features, so they are naturally driven into the embedding layer during alternating training.

The one-dimensional embeddings capture independent shell gaps, but nuclear binding includes non-separable proton–neutron correlations that a sum $e _ { Z } [ Z ] + e _ { N } [ N ]$ cannot represent. As noted in Eq. (3), these effects are delegated to the two-dimensional correlation grid $E _ { \mathrm { { C o r } } }$ .

Figure 5 visualizes the learned grid on the $( N , Z )$ chart, revealing two distinct classes of structure. Near doubly-

![](images/2be61462f4ac264c7c9c877cdb8d17c296aa56177baef1600e44a432e1868267.jpg)  
FIG. 3. Residual maps ( $B _ { \mathrm { p r e d } } - B _ { \mathrm { e x p } }$ , in MeV) on the $( N , Z )$ chart. (a) FRDM2012 spherical macroscopic term. (b) CoNN macroscopic branch only. (c) CoNN Full model. (d) CoNN without the pairing network. All RMSDs are evaluated on the AME2016-overlap set ( $n = 3 4 3 6$ ), excluding the 122 extrapolation nuclei on the boundary.

magic nuclei (e.g. $^ \mathrm { 1 3 2 }$ Sn and $^ { 2 0 8 }$ Pb), localized corrections appear where the additive approximation $e _ { Z } + e _ { N }$ underestimates the enhanced stability arising from strong proton–neutron residual interactions [58–60]. The grid autonomously supplies the additional non-linear binding that the separable embeddings cannot produce. In midshell regions—particularly the rare-earth ( $Z \approx 6 0 – 7 0$ , $N \approx 9 0 – 1 1 0$ ) and actinide ( $Z \approx 9 0$ , $N \approx 1 4 0$ ) sectors— the grid develops spatially extended structures consistent with collective quadrupole deformation, an intrinsically two-dimensional effect that depends on the joint $( Z , N )$ configuration [44, 61]. The bilinear interpolation built into the grid module enforces the spatial continuity appropriate for such collective phenomena, while keeping these smooth corrections orthogonal to the discrete shell jumps handled by the embeddings.

Figure 6 shows the pairing contribution $E _ { \mathrm { P a i r } }$ along representative isotopic chains (top row, varying $N$ at fixed $Z$ ) and isotonic chains (bottom row, varying $Z$ at fixed $N$ ), after removing a smooth linear trend from each chain to isolate the oscillatory component. In all four panels, the predicted pairing term displays the ex-

pected alternating sawtooth pattern, with filled markers (even nucleon number) and open markers (odd) cleanly separated. The staggering amplitude progressively narrows toward heavier nuclei along each chain, particularly visible in the isotonic chains (bottom row). This is consistent with the empirical odd–even mass staggering $\Delta \propto 1 2 / \sqrt { A } \mathrm { M e V }$ : as the mass number increases, the pairing gap decreases [62].

These observations confirm that the architectural constraints—discrete indices for shell effects, a twodimensional grid for non-separable correlations, and a parity-extracting modulo operation for pairing—are sufficient to guide the network toward a physically meaningful decomposition. The separation is not imposed by hand but emerges from the interplay between module structure and alternating training.

# C. Derived quantities

Separation energies and decay $Q$ -values, obtained as finite differences of binding energies, provide a stringent

![](images/5de4b7d845a112c010486573b1ba0a571a9ea38029548330a369701db2a77c89.jpg)  
Proton Embedding: Learned Z-Specific Bias

![](images/67af4ae6d3a32f529a1228b960e9a3ed4db22d36849452aba0f86ed2edfc1536.jpg)  
Neutron Embedding: Learned N-Specific Bias   
FIG. 4. Learned proton (top) and neutron (bottom) embedding biases from the CoNN. Dashed vertical lines mark canonical magic numbers. The embeddings develop clear structure near shell closures without explicit magic-number supervision.

![](images/76d288573439ef22c243b5e71f2a539c0e0e7d9f9882cc6a731e74c600b1dd82.jpg)  
FIG. 5. Learned correlation grid $E _ { \mathrm { C o r } } ( Z , N )$ on the $( N , Z )$ chart. Dashed lines mark magic numbers. Localized patches near doubly-magic nuclei reflect non-separable proton–neutron correlations, while extended structures in mid-shell regions correspond to collective deformation.

test of the model’s local mass-surface structure. Small systematic errors in binding energies can be amplified in differences, so good performance on derived quantities

is not guaranteed by low absolute RMSD alone [63, 64]. Table II reports RMSDs for several derived quantities.

TABLE II. RMSDs for derived quantities on the AME2016- overlap set $n$ varies by availability of neighboring nuclei).   

<table><tr><td>Quantity</td><td>RMSD (MeV)</td><td>Nuclei</td></tr><tr><td>Sn</td><td>0.317</td><td>3317</td></tr><tr><td>S2n</td><td>0.316</td><td>3199</td></tr><tr><td>Sp</td><td>0.331</td><td>3257</td></tr><tr><td>S2p</td><td>0.324</td><td>3081</td></tr><tr><td>Qα</td><td>0.294</td><td>3297</td></tr><tr><td>Qβ-</td><td>0.360</td><td>3141</td></tr></table>

The derived-quantity RMSDs are modestly larger than the absolute binding-energy RMSD (0.237 MeV), as expected for derived quantities that are not directly optimized. Figure 7 compares separation-energy residuals ( $\Delta S = S _ { \mathrm { p r e d } } - S _ { \mathrm { e x p } } )$ of the CoNN with those of FRDM2012 and WS4 along several isotopic chains. For both $S _ { n }$ (Np, Md) and $S _ { 2 n }$ (Sc, Bh), the CoNN residuals remain centered near zero and are more stable than those of the two established macroscopic–microscopic models. The ensemble spread (shaded blue band) provides a prac-

![](images/a6e30c042fa9922c4889fc64b500c36a2a2ad8a20ad12323f4276da6ea0191a1.jpg)  
Pairing Net Sawtooth Pattern (Detrended)

![](images/eac3a433f7b7b4afb97bb43dda30818e39df9c88f92c1b6a32fed7786d470beb.jpg)

![](images/ce7017cb0467f2b2cbaef4507569187000a00dad09c3f72dd2a5398e079637ed.jpg)

![](images/3ef22e1c3ab92850e88487087eafca6f128f1fc025078f83167d345785ced00e.jpg)  
FIG. 6. Pairing contribution $E _ { \mathrm { P a i r } }$ (detrended) along representative isotopic chains (top: Sn and Sc, varying $N$ ) and isotonic chains (bottom: $N = 8 2$ and $N = 3 3$ , varying $Z$ ). The staggering amplitude narrows toward heavier nuclei, consistent with the empirical $\Delta \propto 1 2 / \sqrt { A }$ scaling of pairing gaps.

tical indicator of prediction confidence and widens noticeably for nuclei unseen during training.

# IV. SUMMARY AND OUTLOOK

We have presented a modular neural network—the Cooperative Neural Network (CoNN)—for predicting nuclear binding energies from proton and neutron numbers alone. The architecture decomposes the bindingenergy surface into four additive components: a smooth macroscopic branch, discrete shell embeddings, a twodimensional regional correlation grid, and a parity-aware pairing network. Each module is structurally constrained to capture a specific type of physical contribution, and the decomposition is realized through alternating training rather than explicit component labels.

The CoNN achieves an RMSD of 0.237 MeV on the AME2016-overlap set ( $n = 3 4 3 6$ ) and 0.269 MeV on all 3558 AME2020 nuclei, placing it among the most accurate direct-prediction approaches that use only $( Z , N )$ as

input. A plain MLP with an equal number of parameters yields a substantially higher RMSD (see Table I), ruling out sheer model size as the explanation for the CoNN’s accuracy. Component ablation shows that odd– even staggering is the largest single contributor to the overall RMSD among the microscopic corrections, and the learned embeddings recover shell-closure signatures at canonical magic numbers without supervision. Derived physical quantities, including separation energies and decay $Q$ -values, are reproduced with RMSDs of 0.29– 0.36 MeV. Together, these results establish the predictive accuracy and structural reliability of the CoNN framework.

The broader significance of these results lies in the demonstration that physical knowledge can be embedded into the network architecture as an alternative to handcrafted input features. Conventional ML mass models improve accuracy by supplementing $( Z , N )$ with physicsmotivated features that require domain expertise to design and whose choice can influence extrapolation behavior [28, 30, 34]. The CoNN achieves comparable accu-

![](images/a0b56c4514d9579e3177d1791f9b13877a0dda7c0ded69804b0536a15ee2a431.jpg)  
FIG. 7. Separation-energy residuals along selected isotopic chains: $\Delta S _ { n }$ for Np and Md (top), $\Delta S _ { 2 n }$ for Sc and Bh (bottom). The CoNN (blue) is compared with FRDM2012 (red, dashed) and WS4 (green, dash-dotted); the shaded blue band shows the CoNN ensemble spread. Vertical gray bands indicate nuclei not included in the training set.

racy without such features, relying instead on structural constraints that channel different types of physical contributions into dedicated modules. This shifts the design question from “what features should we provide?” to “what structure should the network have?”, opening a complementary route for incorporating prior knowledge into data-driven nuclear models. Moreover, the resulting decomposition is physically transparent: the learned components recover recognizable shell-closure signatures, regional correlations, and odd–even staggering patterns without explicit supervision, providing interpretive value that conventional black-box approaches lack.

Several limitations should be noted. First, the dis-

crete shell embeddings and finite correlation grid impose a hard boundary on the range of predictable nuclei: the current model is defined for $Z \le 1 2 0$ and $N \leq 1 8 0$ , covering all experimentally known nuclides but excluding superheavy elements and the most neutron-rich isotopes [5]. Beyond this range, the shell embeddings and correlation grid cannot contribute, leaving only the macroscopic branch and pairing network to carry the prediction. One natural extension would be to replace the discrete embeddings with a continuous parametrization—for instance, a small network taking $Z$ (or $N$ ) as input—that can extrapolate while retaining the ability to represent shell discontinuities. Alternatively, predictions from established mass models could serve as soft constraints in the unexplored region, providing physics-informed guidance where experimental data are absent. Second, even within the defined range, the extrapolation RMSD on the 122 AME2020-new nuclei (0.728 MeV) is significantly larger than the interpolation result (0.419 MeV). This reflects a fundamental limitation of purely data-driven structures, such as the two-dimensional correlation grid: without explicit physical priors to constrain their asymptotic behavior, they struggle to produce reliable extrapolations in regions devoid of training data. Third, the ensemble spread provides a qualitative measure of model disagreement but is not a calibrated uncertainty estimate.

Future work could address the extrapolation boundary through the continuous-embedding strategy described above, incorporate calibrated Bayesian uncertainty quantification [6, 22, 65, 66], and extend the cooperative architecture to jointly predict other nuclear observables such as charge radii and $\beta$ -decay properties.

# ACKNOWLEDGMENTS

This work was supported by the National Natural Science Foundation of China under Grants No. 12135004.

[1] D. Lunney, J. M. Pearson, and C. Thibault, Rev. Mod. Phys. 75, 1021 (2003).   
[2] M. Mumpower, R. Surman, G. McLaughlin, and A. Aprahamian, Prog. Part. Nucl. Phys. 86, 86 (2016).   
[3] D. Martin, A. Arcones, W. Nazarewicz, and E. Olsen, Phys. Rev. Lett. 116, 121101 (2016).   
[4] J. J. Cowan, C. Sneden, J. E. Lawler, A. Aprahamian, M. Wiescher, K. Langanke, G. Martínez-Pinedo, and F.- K. Thielemann, Rev. Mod. Phys. 93, 015002 (2021).   
[5] M. Wang, W. Huang, F. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003 (2021).   
[6] L. Neufcourt, Y. Cao, S. A. Giuliani, W. Nazarewicz, E. Olsen, and O. B. Tarasov, Phys. Rev. C 101, 044307 (2020).   
[7] J. Erler, N. Birge, M. Kortelainen, W. Nazarewicz, E. Olsen, A. M. Perhac, and M. Stoitsov, Nature 486,

509 (2012).   
[8] M. Thoennessen, Rep. Prog. Phys. 67, 1187 (2004).   
[9] A. Sobiczewski, Y. A. Litvinov, and M. Palczewski, At. Data Nucl. Data Tables 119, 1 (2018).   
[10] M. Bender, P.-H. Heenen, and P.-G. Reinhard, Rev. Mod. Phys. 75, 121 (2003).   
[11] J. Meng, H. Toki, S. Zhou, S. Zhang, W. Long, and L. Geng, Prog. Part. Nucl. Phys. 57, 470 (2006).   
[12] S. Goriely, S. Hilaire, M. Girod, and S. Péru, Phys. Rev. Lett. 102, 242501 (2009).   
[13] S. Goriely, N. Chamel, and J. M. Pearson, Phys. Rev. C 93, 034337 (2016).   
[14] V. Strutinsky, Nucl. Phys. A 95, 420 (1967).   
[15] P. Möller, A. Sierk, T. Ichikawa, and H. Sagawa, At. Data Nucl. Data Tables 109–110, 1 (2016).   
[16] N. Wang, M. Liu, X. Wu, and J. Meng, Phys. Lett. B

734, 215 (2014).   
[17] M. Brack, J. Damgaard, A. S. Jensen, H. C. Pauli, V. M. Strutinsky, and C. Y. Wong, Rev. Mod. Phys. 44, 320 (1972).   
[18] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld, N. Tishby, L. Vogt-Maranto, and L. Zdeborová, Rev. Mod. Phys. 91, 045002 (2019).   
[19] A. Boehnlein, M. Diefenthaler, N. Sato, M. Schram, V. Ziegler, C. Fanelli, M. Hjorth-Jensen, T. Horn, M. P. Kuchera, D. Lee, W. Nazarewicz, P. Ostroumov, K. Orginos, A. Poon, X.-N. Wang, A. Scheinker, M. S. Smith, and L.-G. Pang, Rev. Mod. Phys. 94, 031003 (2022).   
[20] R. Utama, J. Piekarewicz, and H. B. Prosper, Phys. Rev. C 93, 014311 (2016).   
[21] R. Utama and J. Piekarewicz, Phys. Rev. C 96, 044308 (2017).   
[22] L. Neufcourt, Y. Cao, W. Nazarewicz, and F. Viens, Phys. Rev. C 98, 034318 (2018).   
[23] Z. Niu and H. Liang, Phys. Lett. B 778, 48 (2018).   
[24] Z. M. Niu and H. Z. Liang, Phys. Rev. C 106, L021303 (2022).   
[25] X. Wu, Y. Lu, and P. Zhao, Phys. Lett. B 834, 137394 (2022).   
[26] E. Yüksel, D. Soydaner, and H. Bahtiyar, Phys. Rev. C 109, 064322 (2024).   
[27] Y. Lu, T. Shang, P. Du, J. Li, H. Liang, and Z. Niu, Phys. Rev. C 111, 014325 (2025).   
[28] Y. Huang, J. Chen, J. Jia, L.-M. Liu, Y.-G. Ma, and C. Zhang, Phys. Rev. C 111, 034329 (2025).   
[29] A. Jalili, F. Pan, A. X. Chen, and J. P. Draayer, Phys. Rev. C 112, 024305 (2025).   
[30] A. E. Lovell, A. T. Mohan, T. M. Sprouse, and M. R. Mumpower, Phys. Rev. C 106, 014305 (2022).   
[31] S. Athanassopoulos, E. Mavrommatis, K. A. Gernoth, and J. W. Clark, Nucl. Phys. A 743, 222 (2004).   
[32] Y. Y. Huang and X. H. Wu, Phys. Lett. B 874, 140262 (2026).   
[33] M. R. Mumpower, T. M. Sprouse, A. E. Lovell, and A. T. Mohan, Phys. Rev. C 106, L021301 (2022).   
[34] L.-X. Zeng, Y.-Y. Yin, X.-X. Dong, and L.-S. Geng, Phys. Rev. C 109, 034318 (2024).   
[35] M. Wang, G. Audi, F. G. Kondev, W. Huang, S. Naimi, and X. Xu, Chin. Phys. C 41, 030003 (2017).   
[36] W. D. Myers and W. J. Swiatecki, Nucl. Phys. 81, 1 (1966).   
[37] G. E. Hinton and R. R. Salakhutdinov, Science 313, 504 (2006).   
[38] N. Rahaman, A. Baratin, D. Arpit, F. Draxler, M. Lin, F. Hamprecht, Y. Bengio, and A. Courville, Proc. ICML,

PMLR 97, 5301 (2019).   
[39] Z.-Q. J. Xu, Y. Zhang, T. Luo, Y. Xiao, and Z. Ma, Commun. Comput. Phys. 28, 1746 (2020).   
[40] L. Buskirk, K. Godbey, W. Nazarewicz, and W. Satuła, Phys. Rev. C 109, 044311 (2024).   
[41] M. G. Mayer, Phys. Rev. 75, 1969 (1949).   
[42] O. Haxel, J. H. D. Jensen, and H. E. Suess, Phys. Rev. 75, 1766 (1949).   
[43] P. Federman and S. Pittel, Phys. Lett. B 69, 385 (1977).   
[44] R. F. Casten, Nucl. Phys. A 443, 1 (1985).   
[45] A. Bohr, B. R. Mottelson, and D. Pines, Phys. Rev. 110, 936 (1958).   
[46] H. Liu, J. Lei, and Z. Ren, Phys. Rev. C 111, 024316 (2025).   
[47] R. A. Jacobs, M. I. Jordan, S. J. Nowlan, and G. E. Hinton, Neural Comput. 3, 79 (1991).   
[48] V. Piratla, P. Netrapalli, and S. Sarawagi, Proc. ICML, PMLR 119, 7728 (2020).   
[49] S. J. Wright, Math. Program. 151, 3 (2015).   
[50] J. Zeng, T. T.-K. Lau, S. Lin, and Y. Yao, Proc. ICML, PMLR 97, 7313 (2019).   
[51] D. P. Kingma and J. Ba, in ICLR (2015).   
[52] I. Loshchilov and F. Hutter, in ICLR (2019).   
[53] I. Loshchilov and F. Hutter, in ICLR (2017).   
[54] B. Lakshminarayanan, A. Pritzel, and C. Blundell, Adv. Neural Inf. Process. Syst. 30, 6405 (2017).   
[55] E. Hüllermeier and W. Waegeman, Mach. Learn. 110, 457 (2021).   
[56] P. Izmailov, S. Vikram, M. D. Hoffman, and A. G. Wilson, Proc. ICML, PMLR 139, 4629 (2021).   
[57] R. Rahaman and A. Thiery, Adv. Neural Inf. Process. Syst. 34, 20063 (2021).   
[58] J. Y. Zhang, R. F. Casten, and D. S. Brenner, Phys. Lett. B 227, 1 (1989).   
[59] R. B. Cakirli, D. S. Brenner, R. F. Casten, and E. A. Millman, Phys. Rev. Lett. 94, 092501 (2005).   
[60] D. S. Brenner, R. B. Cakirli, and R. F. Casten, Phys. Rev. C 73, 034315 (2006).   
[61] A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II: Nuclear Deformations (W. A. Benjamin, Reading, MA, 1974).   
[62] A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. I: Single-Particle Motion (W. A. Benjamin, New York, 1969).   
[63] A. Sobiczewski and Y. A. Litvinov, Phys. Rev. C 90, 017302 (2014).   
[64] S. Martinet and S. Goriely, Astron. Astrophys. 694, A180 (2025).   
[65] Y. Saito, I. Dillmann, R. Krücken, M. R. Mumpower, and R. Surman, Phys. Rev. C 109, 054301 (2024).   
[66] D. J. C. MacKay, Neural Comput. 4, 448 (1992).