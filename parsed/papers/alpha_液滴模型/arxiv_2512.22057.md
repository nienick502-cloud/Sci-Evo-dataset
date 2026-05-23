# Unified Royer Law Revision for $\alpha$ -Decay Half-Lives: Shell Corrections, Pairing, and Orbital-Angular-Momentum

Kai Ren,1 Pengfei Ma,1 Minghui Hu,1 and Junlong Tian1, 2, ∗

$\mathit { 1 }$ Department of Physics, Guangxi Normal University,

Guilin 541004, People’s Republic of China

${ \boldsymbol { \mathcal { Z } } }$ Guangxi Key Laboratory of Nuclear Physics and Technology,

Guilin 541004, People’s Republic of China

(Dated: December 29, 2025)

# Abstract

The Royer law is a widely used empirical relation for calculating $\alpha$ -decay half-lives but requires 12 parity-dependent parameters. It exhibits systematic deviations near the $N = 1 2 6$ shell closure. We propose an improved Royer law by adding a shell-correction term, an odd-even pairing indicator, and an orbital-angular-momentum contribution. This unified framework reduces the number of free parameters to just four, leading to significant improvements in accuracy. The root-mean-square deviation across 550 experimental data points decreases from 0.520 to 0.279, corresponding to a 66.7% reduction in parameters and a 46.3% improvement in accuracy. Using this refined formalism, we predict $\alpha$ -decay half-lives for superheavy nuclei with atomic numbers $Z = 1 1 7 - 1 2 0$ .

# I. INTRODUCTION

The prediction of $\alpha$ -decay half-lives is fundamental to nuclear structure studies[1–15], particularly for superheavy nuclei[16–21]. In 1911, Geiger and Nuttall observed that plotting $\log _ { 1 0 } T _ { 1 / 2 }$ against $Q ^ { - 1 / 2 }$ yields a linear relationship for even-even isotopes [22]. The phenomenon of $\alpha$ decay was first explained as a quantum-tunneling process by Gamow [23] and independently by Gurney and Condon [24]. Since then, a variety of theoretical models have been developed to deepen our understanding of $\alpha$ decay. Notable examples include the Viola–Seaborg–Sobiczewski (VSS) formula [25], the effective liquid-drop model [26–30], the generalized liquid-drop model (GLDM) [31, 32], the fission-like model [33], and several others [34–39]. In parallel, many empirical formulas have been proposed based on the Geiger–Nuttall law (GNL) or quantum-tunneling arguments, such as the universal decay law (UDL) [40, 41], the Royer law [42], the Deng–Zhang–Royer (DZR) formula [43], and the new Geiger–Nuttall law (NGNL) [44]. Recent studies have further advanced the systematic understanding of $\alpha$ decay. For instance, El Batoul et al. [45] refined empirical formulations by incorporating a position-dependent mass formalism to improve accuracy; You et al. [46, 47] applied machine-learning techniques along with deformation effects to enhance predictive reliability; and Ismail et al. [48] investigated structural dependencies within Royer-type models.

The Royer law is a widely used empirical relation for calculating $\alpha$ -decay half-lives, yet it relies on 12 parity-dependent parameters. Despite its broad application, this model exhibits significant deviations from experimental data in the region of the $N = 1 2 6$ shell closure. To address these limitations, we propose an improved Royer law that incorporates the shellcorrection energy, a pairing term, and an angular-momentum term. This modification not only reduces discrepancies near $N = 1 2 6$ but also enhances the overall accuracy of calculating $\alpha$ -decay half-lives. Our analysis is based on 550 measured $\alpha$ -decay half-lives, comprising the 539 entries from the NUBASE2020 database [49] and 11 additional nuclei from recent publications ( $^ { 1 7 0 } \mathrm { H g }$ [50], $2 1 4$ U, $^ { 2 1 6 }$ U, $^ { 2 1 8 }$ U [51], $_ \mathrm { 1 6 0 }$ Os [52], $^ \mathrm { 1 9 0 }$ At [53], $^ { 2 0 7 }$ Th [54], $2 7 2$ Hs, $2 7 6$ Ds [55], $^ { 2 1 0 }$ Pa [56] and $2 8 6$ Mc [57]). The parameters of the improved Royer formula are determined by fitting to this robust and comprehensive dataset. The study focuses exclusively on ground-state-to-ground-state $\alpha$ decays. To ensure accurate extraction of half-lives, we account for the experimental branching ratio $R$ of $\alpha$ decay from the parent ground state to

various daughter states. From NUBASE2020 [49], we initially considered 701 nuclei with reported $\alpha$ -decay branching ratios. After applying rigorous selection criteria—experimental uncertainties below $5 0 \%$ , branching-ratio uncertainties smaller than $R$ itself, and exclusion of $2 6 4$ Hs (due to $\log _ { 1 0 } T _ { 1 / 2 } ^ { \prime } = 0$ )—we retained 539 nuclei. These were further categorized into four parity groups: 190 even-even (e-e), 146 even-odd (e-o), 114 odd-even (o-e), and 100 oddodd (o-o). Alternatively, the dataset can be classified by the orbital-angular-momentum $l$ o f the transition. Favored $\alpha$ decays ( $l = 0$ ) constitute the majority, with 406 cases (74% of the total), distributed as 190 e-e, 88 e-o, 71 o-e, and 57 o-o. Unfavored decays ( $l \neq 0$ ) account for the remaining 144 cases (26%), comprising 58 e-o, 43 o-e, and 43 o-o.

# II. THEORETICAL FRAMEWORK

The Royer law [42] establishes a benchmark relationship between $\log _ { 1 0 } T _ { 1 / 2 }$ and nuclear properties, expressed as

$$
\log_ {1 0} T _ {1 / 2} = a + b A ^ {1 / 6} \sqrt {Z} + c \frac {Z}{\sqrt {Q}}, \tag {1}
$$

where $A$ , $Z$ , and $Q$ represent the mass number, proton number, and decay energy of the parent nucleus, respectively. The parameters a, b, and $c$ are determined by fitting the experimental data. The original Royer law employs parity-dependent parameters (Table I). It requires separate treatments for e-e, e-o, o-e, and o-o nuclei, based on the proton ( $\cal { Z }$ ) and neutron ( $N$ ) parity of the parent nucleus. A total of 12 adjustable parameters are distributed across these four parity groups.

We first applied the Royer law to compute the $\alpha$ -decay half-lives of 16 even-even polonium (Po) isotopes. Figure 1(a) plots the logarithmic differences between experimental data and calculations. As shown, a significant deviation in $\log _ { 1 0 } ( T _ { 1 / 2 } ^ { \mathrm { e x p t } } / T _ { 1 / 2 } ^ { \mathrm { R o y e r } } )$ emerges near the magic number $N = 1 2 6$ in the even-even Po isotopic chain. This indicates inadequate accounting of shell effects in this region by the original Royer law, particularly around the neutron magic number $N = 1 2 6$ . To resolve such discrepancies, researchers have modified empirical formulas by introducing shell-effect-related terms. For example, Wang et al. improved accuracy in Ref. [58] by including a phenomenological shell-correction factor for nuclei near shell closures, but their fixed constant $S = 0 . 5$ cannot fully capture the nuanced relationship between structural effects and $\alpha$ -decay half-lives. Additionally, the Royer law’s segmented approach lacks physical unification and neglects angular-momentum contributions.

TABLE I: Parameters of the Royer law [42]   

<table><tr><td>Nuclear Type</td><td>a (s)</td><td>b (s)</td><td>c (s.√MeV)</td></tr><tr><td>Even-even</td><td>-25.31</td><td>-1.1629</td><td>1.5864</td></tr><tr><td>Even-Z/odd-N</td><td>-26.65</td><td>-1.0859</td><td>1.5848</td></tr><tr><td>Odd-Z/even-N</td><td>-25.68</td><td>-1.1423</td><td>1.5920</td></tr><tr><td>Odd-odd</td><td>-29.48</td><td>-1.1130</td><td>1.6971</td></tr></table>

To address these limitations of the Royer law, we introduce an improved formulation that incorporates a shell-correction energy term, a pairing term, and an angular-momentum term into the original model. The resulting expression for the $\alpha$ -decay half-life reads:

$$
\log_ {1 0} T _ {1 / 2} = a + b A ^ {1 / 6} \sqrt {Z} + c \frac {Z}{\sqrt {Q}} + d \left\{E _ {\mathrm {s h}} - \left[ (- 1) ^ {Z} + (- 1) ^ {N} \right] + \frac {l (l + 1)}{2} \right\}, \qquad (2)
$$

where the coefficients $a$ , $b$ , $c$ , and $d$ are determined from a fit to the 550 experimental data points and are listed in Table II. Compared to the original Royer law, Eq. (2) incorporates three physically motivated additions. The first additional term, $E _ { \mathrm { s h } }$ , represents the value of shell-correction energy, which captures the structural influence of the parent nucleus in the decay process. This form has previously been employed in calculations of spontaneous fission half-lives [59, 60]. The second term, $[ ( - 1 ) ^ { Z } + ( - 1 ) ^ { N } ]$ , acts as a unified pairing term that accounts for odd-even staggering across different nuclear parity combinations. It enables a consistent treatment of even–even, odd- $A$ , and odd-odd nuclei within a single framework. Specifically, along an isotopic chain, even-even nuclei generally exhibit shorter half-lives than the average of their neighboring odd- $A$ nuclei, whereas odd-odd nuclei tend to have longer ones. This behavior is encapsulated in the formula as a correction of $- 2 d$ for even-even nuclei, $+ 2 d$ for odd-odd nuclei, and 0 for odd- $A$ nuclei. Such a unified approach not only reduces the number of free parameters but also offers a more consistent description of pairing effects. The third term, proportional to $l ( l { + } 1 )$ , accounts for the orbital-angular-momentum carried by the emitted $\alpha$ particle, as commonly adopted in Royer-type formulas [43, 58, 61]. It is noteworthy that when an independent coefficient $f$ is introduced for this term, the fitting yields $f \approx d / 2$ , supporting the current form. Collectively, these modifications yield a phenomenological yet physically grounded representation of the microscopic factors governing $\alpha$ -decay systematics. The improved Royer formula thus provides a unified treatment of shell stabilization, pairing correlations, and angular-momentum hindrance within a single coherent framework.

TABLE II: Parameters of the improved Royer law   

<table><tr><td>a (s)</td><td>b (s)</td><td>c (s.√MeV)</td><td>d (s)</td></tr><tr><td>-28.1919 ± 0.1510</td><td>-1.0853 ± 0.0055</td><td>1.6260 ± 0.0039</td><td>0.1078 ± 0.0026</td></tr></table>

![](images/e06b395d1597c43611a939347f8fb5d1abc7dd70da8b6646864fb6ffa43f2933.jpg)  
FIG. 1: (a) The discrepancy between experimental and calculated logarithmic $\alpha$ -decay half-lives using Eq. (1) for even-even polonium isotopes is plotted against the neutron number $N$ . (b) Similar to (a), except that the ordinate represents the variation of shell-correction energy $E _ { \mathrm { s h } }$ with the neutron number, with calculated values taken from Eq. (3). The dashed line indicates the neutron number $N = 1 2 6$ . The variation trends and structural features of the two are highly similar.

# III. THE RESULTS AND DISCUSSIONS

From Fig. 1(a), we observe that the shell effects play a crucial role for certain nuclei, particularly near $N = 1 2 6$ . To incorporate shell effects into the Royer law, we first analyze

the relationship between shell-correction energy $E _ { \mathrm { s h } }$ and neutron number $N$ for even-even polonium isotopes in Fig. 1(b). The trend of $E _ { \mathrm { s h } } ^ { \prime }$ closely mirrors the discrepancy between experimental and calculated $\alpha$ -decay half-lives using the Royer law, with both peaking at $N = 1 2 6$ . This suggests a linear correlation between $E _ { \mathrm { s h } }$ and $\log _ { 1 0 } T _ { 1 / 2 }$ , well described by the fit $0 . 1 1 3 E _ { s h } + 0 . 0 2 6$ for even-even Po isotopes. We therefore introduce a shell-correction energy $d E _ { \mathrm { s h } }$ into the original Royer law, where $E _ { \mathrm { s h } }$ represents microscopic fluctuations of the nuclear binding energy relative to the macroscopic liquid-drop model [62]. It is computed as the difference between the experimental binding energy $B _ { \mathrm { e x p t } }$ and the macroscopic binding energy $B _ { \mathrm { L D } }$ of the nucleus,

$$
E _ {\mathrm {s h}} = \frac {B _ {\mathrm {e x p t}} - B _ {\mathrm {L D}}}{1 \mathrm {M e V}} \tag {3}
$$

Here the experimental binding energy is derived from the AME2020 [63] mass table, and $B _ { \mathrm { L D } }$ is the theoretical binding energy of the spherical nucleus based on the liquid drop model, expressed as

$$
B _ {\mathrm {L D}} = a _ {v} A - a _ {s} A ^ {2 / 3} - a _ {a} \left(\frac {A}{2} - Z\right) ^ {2} / A - a _ {c} \frac {Z ^ {2}}{A ^ {1 / 3}} + a _ {p} \delta A ^ {- 1 / 2}, \tag {4}
$$

where $a _ { v }$ , $a _ { s }$ , $a _ { a }$ , $a _ { c }$ and $a _ { p }$ are the volume, surface, symmetry, Coulomb, and pairing energy coefficients, respectively. $\delta = + 1$ for even-even nuclei, $\delta = 0$ for odd- $A$ nuclei, and $\delta = - 1$ for odd-odd nuclei. The experimental binding energies of 2463 atomic nuclei ( $Z \ge 8$ , $N \geq 8$ ) selected from the AME2020 mass table [63] were fitted using the least squares method. The resulting parameters are: $a _ { v } = 1 5 . 5 2 8 7$ MeV, $a _ { s } = 1 6 . 9 0 4 3$ MeV, $a _ { a } = 9 1 . 9 6 8 6$ MeV, $a _ { c } = 0 . 7 0 2 5$ MeV, and $a _ { p } = 1 2 . 4 4 3 9$ MeV. The root-mean-square deviation of the fit is 3.02 MeV.

To evaluate the improvement brought by the inclusion of shell-correction energy and pairing effects, we compare the half-life predictions of the original Royer law (Eq. (1)) with those of the improved version (Eq. (2)). The accuracy of the calculations is quantified using the root-mean-square deviation (RMSD) between experimental and theoretical half-lives, defined as:

$$
\sigma = \left[ \frac {1}{m} \sum_ {i = 1} ^ {m} (\log_ {1 0} T _ {1 / 2} ^ {\mathrm {e x p t}, i} - \log_ {1 0} T _ {1 / 2} ^ {\mathrm {c a l}, i}) ^ {2} \right] ^ {1 / 2}, \tag {5}
$$

where $m$ denotes the number of nuclei considered in each case. A smaller RMSD corresponds to better agreement with experimental data and thus indicates improved model performance.

# A. Favored $\alpha$ decay

![](images/bc0450ff91f9078991ddf28bc1e2ac275c5c24330281136f81a1a0c2e74a6f45.jpg)  
FIG. 2: (Color online) Comparison of the differences between experimental and theoretical $\alpha$ -decay half-lives calculated by Eq. (1) and Eq. (2) for four categories of $l = 0$ nuclei: (a) even-even (190 nuclei), (b) even-odd (88 nuclei), (c) odd-even (71 nuclei), and (d) odd-odd (57 nuclei), plotted against neutron number $N$ . The RMSD $\sigma$ is indicated in parentheses after each formula.

Fig. 2 compares the deviations between experimental and calculated $\alpha$ -decay half-lives for 406 favored $\alpha$ decays ( $l = 0$ ) nuclei, using the original Royer law Eq. (1) and its improved revision Eq.(2). The dataset spans four decay types: (a) even-even (190 nuclei), (b) even-odd (88 nuclei), (c) odd-even (71 nuclei), and (d) odd-odd (57 nuclei))—a division necessitated by the Royer law’s requirement for separate parameter sets per parity category. In contrast, the pairing term in Eq. (2) obviates the need for distinct parameter sets, allowing a single parameterization to uniformly describe all categories without loss of accuracy. Across all subsets, Eq. (2) exhibits consistently smaller deviations than Eq. (1), with the RMSD for $l ~ = ~ 0$ nuclei reduced from 0.311 to 0.242 (Fig. 3(a)). Most nuclei (open circles) show $\log _ { 1 0 } ( T _ { 1 / 2 } ^ { \mathrm { e x p t } } / T _ { 1 / 2 } ^ { \mathrm { c a l } } )$ values within [-0.4, 0.8] and cluster near the dotted line. Notably, the

shell-correction energy term $E _ { \mathrm { s h } }$ captures partial nuclear structure effects, allowing Eq. (2) to reproduce experimental values far more accurately near the neutron shell closure $N = 1 2 6$ , whereas Eq. (1) exhibits pronounced discrepancies (solid squares).

# B. Unfavored $\alpha$ decay

For unfavored $\alpha$ -decay ( $l \neq 0$ ), the centrifugal potential barrier effect must be considered. This barrier, originating from the orbital-angular-momentum $l$ of the emitted $\alpha$ particle, reduces the tunneling probability and thus increases the half-life. Its contribution to the half-life can be directly incorporated into the Royer law via the angular-momentum term $l ( l + 1 )$ . The value of $l$ is determined by angular-momentum and parity conservation, as given by Eq. (6). Notably, while selection rules permit multiple possible values for the orbital-angular-momentum $l$ of emitted $\alpha$ -particles, we adopt the minimum allowable value $l _ { \mathrm { m i n } }$ in all subsequent calculations for simplicity.

$$
l _ {m i n} = \left\{ \begin{array}{l l l l l l} \Delta_ {j}, & f o r & e v e n & \Delta_ {j} & a n d & \pi_ {p} = \pi_ {d} \\ \Delta_ {j} + 1, & f o r & e v e n & \Delta_ {j} & a n d & \pi_ {p} \neq \pi_ {d} \\ \Delta_ {j}, & f o r & o d d & \Delta_ {j} & a n d & \pi_ {p} \neq \pi_ {d} \\ \Delta_ {j} + 1, & f o r & o d d & \Delta_ {j} & a n d & \pi_ {p} = \pi_ {d} \end{array} \right. \tag {6}
$$

where $\Delta _ { j } = \mid j _ { p } - j _ { d } \mid$ , with $j _ { p }$ , $\pi _ { p }$ , $j _ { d }$ and $\pi _ { d }$ represent the spin and parity values of the parent and daughter nuclei, respectively. Their values used in this work are taken from Refs. [49, 64].

To evaluate the effect of the third additional term, we compare calculations with and without the angular-momentum $l ( l + 1 )$ term in Eq. (2) for 144 unfavored $\alpha$ -decay half-lives ( $l \neq 0$ ). The resulting RMSDs are 0.363 (with $l ( l + 1 )$ ) and 0.871 (without it), indicating the importance of explicitly including the $l ( l + 1 )$ contribution. Including this term reduces the RMSD from 0.871 (Eq. (1)) to 0.363, corresponding to a 58.3% improvement in accuracy. In these cases, a nonzero $l$ introduces a centrifugal barrier in unfavored $\alpha$ decays—an effect that is not accounted for in the absence of the $l ( l + 1 )$ term. Incorporating this term effectively captures the centrifugal barrier effect. This correction is especially significant for unfavored $\alpha$ decays ( $l \neq 0$ ) in odd- $A$ and odd-odd nuclei, leading to improved accuracy in half-life predictions across all nuclear types. The good agreement between the calculated results (Fig. 3(c)) and experimental data demonstrates that the improved Royer law, which

includes both the shell-correction energy and the angular-momentum $l ( l + 1 )$ term, performs well across all 550 $\alpha$ -decay cases studied.

TABLE III: RMSDs of five empirical formulas.   

<table><tr><td></td><td>lmin=0</td><td>lmin≠0</td><td>Total</td></tr><tr><td></td><td>(n=406)</td><td>(n=144)</td><td>(n=550)</td></tr><tr><td>Eq. (1)</td><td>0.311</td><td>0.871</td><td>0.520</td></tr><tr><td>Eq. (2)</td><td>0.242</td><td>0.363</td><td>0.279</td></tr><tr><td>Ref. [43]</td><td>0.322</td><td>0.443</td><td>0.358</td></tr><tr><td>Ref. [58]</td><td>0.314</td><td>0.385</td><td>0.334</td></tr><tr><td>Ref. [61]</td><td>0.300</td><td>0.581</td><td>0.393</td></tr></table>

![](images/e2f365f00589e76caafc5679e51083e9ef8a1b3437249c9cd74f803d3dac348a.jpg)  
FIG. 3: (Color online) Comparison of deviations between experimental and calculated $\alpha$ -decay half-lives: (a) 406 favored $\alpha$ -decays with angular-momentum $l = 0$ ; (b) 144 unfavored $\alpha$ -decays with $l \neq 0$ ; (c) Full dataset of 550 nuclei.

The calculations of $\alpha$ -decay half-lives with three other well-known empirical formulas in Refs. [43, 58, 61] are also performed and the corresponding RMSDs are presented in Table III. we evaluate separately for nuclei with $l = 0$ , $l \neq 0$ , and the full dataset of 550 nuclei. Comparing the results, it is found that the improved Royer law Eq. (2) yields the smallest values of RMSDs for both the full data set (0.279) and for two subsets (0.242 for favored and 0.363 for unfavored). In other words, the precision in our formula is better than that of the previous methods.

To further examine the physical reliability of the improved Royer law, we performed a

systematic analysis of the reduced $\alpha$ -decay widths. The reduced width $\gamma ^ { 2 }$ is defined as [65]

$$
\gamma^ {2} = \frac {\Gamma}{2 P}, \tag {7}
$$

where $\Gamma$ is the decay width and $P$ is the Coulomb penetrability evaluated. The decay width is related to the half-life $T _ { 1 / 2 }$ by

$$
\Gamma = \frac {\hbar \ln 2}{T _ {1 / 2}}. \tag {8}
$$

Hence, the logarithm of the reduced width can be expressed as

$$
\log_ {1 0} \gamma^ {2} = \log_ {1 0} (\hbar \ln 2) - \log_ {1 0} T _ {1 / 2} - \log_ {1 0} P - \log_ {1 0} 2. \tag {9}
$$

The Coulomb barrier at the touching configuration is given by

$$
V _ {c} (r _ {B}) = \frac {Z _ {d} Z _ {\alpha} e ^ {2}}{r _ {B}}, r _ {B} = 1. 2 \left(A _ {d} ^ {1 / 3} + A _ {\alpha} ^ {1 / 3}\right) \mathrm {f m}, \tag {10}
$$

where $Z _ { d }$ and $A _ { d }$ denote the proton and mass numbers of the daughter nucleus, and $Z _ { \alpha } = 2$ , $A _ { \alpha } = 4$ for the $\alpha$ particle. The fragmentation potential is then defined as

$$
V _ {\text {f r a g}} = V _ {c} \left(r _ {B}\right) - Q. \tag {11}
$$

The analysis focuses on 406 favored $\alpha$ -decay nuclei with $l = 0$ , where the centrifugal barrier is absent, thereby providing a clear test of the linear relationship between $\log _ { 1 0 } \gamma ^ { 2 }$ and $V _ { \mathrm { f r a g } }$ . Fig. 4 presents the results across four neutron-number regions, with experimental data indicated by black squares and theoretical values from Eq. (2) shown as red circles. As observed, both experimental and theoretical results adhere to the expected nearly linear trend between $\log _ { 1 0 } \gamma ^ { 2 }$ and $V _ { \mathrm { f r a g } }$ in each region. This agreement confirms that the improved formula not only enables more accurate predictions of half-lives but also establishes an approximate linear relationship between reduced widths and fragmentation potentials. The robustness of this correspondence further validates the physical reliability of our model across different nuclear regions. Although minor local fluctuations are present, the overall linearity between $\log _ { 1 0 } \gamma ^ { 2 }$ and $V _ { \mathrm { f r a g } }$ remains clear, in line with the universal behavior reported by Delion [65].

To further verify the applicability of the improved formula (Eq. (2)), we used it to calculate the $\alpha$ -decay half-lives of superheavy nuclei with $Z = 1 1 7  – 1 2 0$ . For those nuclei lacking experimental $Q$ -values or binding energies, we adopted the Weizs¨acker–Skyrme (WS4+RBF)

![](images/644c31a0466f0fa1327594328262c44de659d34ef1f19bd96771de693578d661.jpg)  
FIG. 4: Systematic behavior of $\log _ { 1 0 } \gamma ^ { 2 }$ as a function of the fragmentation potential $V _ { c } - Q$ . Panels (a) to (d) correspond to the neutron-number regions: (a) $N \leq 8 2$ , (b) $8 2 < N \le 1 2 6$ , (c) $1 2 6 < N \le 1 5 2$ , and (d) $N > 1 5 2$ . Black squares represent values derived from experimental half-lives, and red circles denote results calculated using the improved Royer law in Eq. (2). The blue lines indicate the linear fitting of the experimental data.

mass table [66]. In such cases, the shell-correction energy $E _ { \mathrm { s h } }$ is evaluated using binding energies from the WS4 $^ +$ RBF model, where the experimental binding energy $B _ { \mathrm { e x p t } }$ is replaced by BWS4+RBF to maintain consistency with the definition given in Eq. (3). Fig. 5 presents the calculated $\alpha$ -decay half-lives as a function of the daughter neutron number $N _ { d }$ , using the improved Royer law (Eq. (2)), the original Royer law (Eq. (1)), and the DZR model [43]. Although three different computational methods were employed, they all exhibit the same variation trend and consistently indicate the possible existence of magic numbers or neutron subshell structures at neutron numbers $N _ { d } = 1 7 8$ , 184, and 196. As shown, the improved Royer law yields results that are more consistent with the systematic trends predicted by the DZR model in the region $N _ { d } \leq 1 8 4$ , and lower than those results of two in

the region $N _ { d } \geq 1 8 4$ . This consistency is particularly evident for the existing experimental data $^ \mathrm { 2 9 3 , 2 9 4 }$ Ts and $^ { 2 9 4 }$ Og. Overall, the improved formula demonstrates strong extrapolation capability in predicting the decay properties of superheavy nuclei, reinforcing its reliability beyond the region used for parameter fitting.

![](images/78b8baae3011e1d6cd11a082d3bd77a19b630797f7ba62d2a4b50ba4ee618706.jpg)  
FIG. 5: (Color online) The $\log _ { 1 0 } T _ { 1 / 2 }$ values of $Z = 1 1 7 - 1 2 0$ isotopes versus neutron number of daughter nucleus $N _ { d }$ . The open circles, stars, and the solid squares denote the prediction results with the improved Royer law (Eq. (2)), the original revision (Eq. (1)), and the DZR model (Ref. [43]). Experimental data (solid circles) for $^ { 2 9 3 , 2 9 4 }$ Ts and $2 9 4$ Og are included for comparison. The vertical dashed lines indicate the possible existence of magic numbers or neutron subshell structures at neutron numbers $N _ { d } = 1 7 8$ , 184, and 196.

# IV. SUMMARY

In summary, we have developed an improved Royer formula, Eq. (2), for calculating $\alpha$ -decay half-lives by incorporating three physically motivated correction terms—shell-

TABLE IV: Comparison of model performance: Royer law versus its improved revision.   

<table><tr><td>Metric</td><td>Eq. (1)</td><td>Eq. (2) (Improved)</td></tr><tr><td>Number of parameters</td><td>12</td><td>4</td></tr><tr><td>RMS deviation</td><td>0.520</td><td>0.279</td></tr><tr><td>Parity treatment</td><td>Segmented</td><td>Unified</td></tr><tr><td>Physics extensions</td><td>None</td><td>Shell+pair+l term</td></tr></table>

correction energy, pairing effects, and angular momentum—into a unified four-parameter framework. This work not only offers a simplified and more accurate empirical formula but also establishes a structure that naturally integrates nuclear-structure corrections, thereby bridging phenomenological approaches with microscopic insights. Unlike the original Royer law, which treats nuclei differently based on parity, the new formulation provides a unified description for all nuclei, reducing the number of free parameters from 12 to 4—a 66.7% reduction in complexity. The inclusion of shell-correction energy markedly mitigates discrepancies near the neutron number $N = 1 2 6$ and improves the overall predictive accuracy of $\alpha$ -decay half-lives. Moreover, the angular-momentum term accounts for hindrance effects arising from spin and parity changes between parent and daughter nuclei. As a result, the model consistently describes both favored and unfavored $\alpha$ -decays within a single framework, improving physical coherence and practical utility. Using this refined formula, we systematically computed the half-lives of 550 $\alpha$ transitions between ground states of parent and daughter nuclei, achieving a significant improvement in accuracy: the root-mean-square deviation drops from 0.520 to 0.279, corresponding to a 46.3% enhancement (see Table IV). We further applied the formula to predict $\alpha$ -decay half-lives for superheavy nuclei with $Z = 1 1 7  – 1 2 0$ . The formula also captures the emergence of magic numbers or neutron subshell structures at neutron numbers $N _ { d } = 1 7 8$ , 184, and 196.

# ACKNOWLEDGMENTS

This work was supported by the Guangxi Natural Science Foundation (Nos. 2023GXNSFDA026005, and 2023GXNSFBA026008), the National Natural Science Foundation of China (Nos. 12465019, 12465021, 12265006 and U1867212), and the Central Government Guides Local Scientific and Technological Development Fund Projects (No. Guike

[1] W. M. Seif, Phys. Rev. C 74, 034302 (2006).   
[2] J. Khuyagbaatar, A. Yakushev, Ch. E. Dullmann et al., Phys. Rev. Lett. 112, 172501 (2014)   
[3] R. Carroll, R. D. Page, D. T. Joss et al., Phys. Rev. Lett. 112, 092501 (2014)   
[4] D. S. Delion, R. J. Liotta, and R. Wyss, Phys. Rev. C 92, 051301 (2015)   
[5] W. M. Seif, M. Shalaby, and M. F. Alrakshy, Phys. Rev. C 84, 064608 (2011)   
[6] Z. Z. Ren, Phys. Rev. C 65, 051304 (2002)   
[7] D. D. Ni and Z. Z. Ren, Ann. Phys. 358, 108 (2015)   
[8] M. Brack, Jens Damgaard, A. S. Jensen, H. C. Pauli, V. M. Strutinsky, and C. Y. Wong, Rev. Mod. Phys. 44, 320 (1972)   
[9] D. N. Poenaru, I. H. Plonski, R. A. Gherghescu, and W. Greiner, J. Phys. G 32, 1223 (2006)   
[10] Z. Z. Ren and G. O. Xu, Phys. Rev. C 36, 456 (1987)   
[11] D. H. Feng, J. N. Ginocchio, D. D. Strottman and T. Otsuka, Nucl. Phys. A 522, 257 (1991)   
[12] K. P. Santhosh, B. and Priyanka, Phys. Rev. C 89, 064604 (2014)   
[13] G. Audi, O. Bersillon, J. Blachot, and A. H. Wapstra, Nucl. Phys. A 729, 3 (2003)   
[14] D. Seweryniak, K. Starosta, C. N. Davids et al., Phys. Rev. C 73, 061301 (2006)   
[15] A. P. Leppanen, J. Uusitalo, M. Leino et al., Phys. Rev. C 75, 054307 (2007)   
[16] Yu. Ts. Oganessian, V. K. Utyonkov, Yu. V. Lobanov et al., Phys. Rev. C 76, 011601 (2007)   
[17] P. A. Ellison, K. E. Gregorich, J. S. Berryman et al., Phys. Rev. Lett. 105, 182701 (2010)   
[18] Yu. Ts. Oganessian, F. Sh. Abdullin, P. D. Bailey et al., Phys. Rev. Lett. 104, 142502 (2010)   
[19] T. N. Ginter, K. E. Gregorich, W. Loveland et al., Phys. Rev. C 67, 064609 (2003)   
[20] Yu. Ts. Oganessian, V. K. Utyonkov, S. N. Dmitriev et al., Phys. Rev. C 72, 034611 (2005)   
[21] Yu. Ts. Oganessian, F. Sh. Abdullin, C. Alexander et al., Phys. Rev. Lett. 109, 162501 (2012)   
[22] H. Geiger and J. M. Nuttall, Phil. Mag. 22, 613 (1911)   
[23] G. Gamow, Z. Phys 51, 204 (1928)   
[24] R. W. Gurney, E. U. Condon, Nature 122, 439 (1928)   
[25] V. E. Viola and G. T. Seaborg, J. Inorg. Nucl. Chem. 28, 741 (1966)   
[26] S. B. Duarte, O. Rodriguez, O. A. P. Tavares, M. Goncalves, F. Garcia, and F. Guzman, Phys. Rev. C 57, 2516 (1998)

[27] M. G. Goncalves and S. B. Duarte, Phys. Rev. C 48, 2409 (1993)   
[28] J. P. Cui, Y. H. Gao, Y. Z. Wang, and J. Z. Gu, Nucl. Phys. A 1017, 122341 (2022)   
[29] S. B. Duarte, and M. G. Goncalves, Phys. Rev. C 53, 2309 (1996)   
[30] S. B. Duarte, O. A. P. Tavares, F. Guzman, A. Dimarco, F. Garcia, O. Rodriguez, and M. Gongalves, Atom. Data Nucl. Data Tabl. 80, 235 (2002)   
[31] H. F. Zhang, W. Zuo, J. Q. Li and G. Royer, Phys. Rev. C 74, 017304 (2006)   
[32] J. M. Dong, H. F. Zhang, Y. Z. Wang, W. Zuo, and J. Q. Li, Nucl. Phys. A 832, 198 (2010)   
[33] B. Buck, A. C. Merchant, and S. M. Perez, Atom. Data Nucl. Data Tabl. 54, 53 (1993)   
[34] C. Samanta, P. R. Chowdhury, and D. N. Basu, Nucl. Phys. A 789, 142 (2007)   
[35] P. R. Chowdhury, C. Samanta, D. N. Basu, Phys. Rev. C 77, 044603 (2008)   
[36] S. A. Gurvitz, P. B. Semmes, W. Nazarewicz, and T. Vertse, Phys. Rev. A 69, 042705 (2004)   
[37] X. D. Sun, J. G. Deng, D. Xiang, P. Guo and X. H. Li, Phys. Rev. C 95, 044303 (2017)   
[38] X. D. Sun, C. Duan, J. G. Deng, P. Guo, and X. H. Li, Phys. Rev. C 95, 014319 (2017)   
[39] Y. B. Qian, and Z. Z. Ren, Phys. Rev. C 85, 027306 (2012)   
[40] C. Qi, F. R. Xu, R. J. Liotta, and R. Wyss, Phys. Rev. Lett. 103, 072501 (2009)   
[41] C. Qi, F . Xu, R. J. Liotta, R. A. Wyss, M. Y. Zhang, C. Asawatangtrakuldee, and D. Hu, Phys. Rev. C 80, 044326 (2009)   
[42] G. Royer, J. Phys. G: Nucl. Part. Phys. 26, 1149 (2000)   
[43] J. G. Deng, H. F. Zhang and G. Royer, Phys. Rev. C 101, 034307 (2020)   
[44] Y. J. Ren, and Z. Z. Ren, Phys. Rev. C 85, 044608 (2012)   
[45] A. El Batoul, I. Moumene, and M. Oulne, Eur. Phys. J. A 57, 254 (2021)   
[46] H.Q. You, X.T. He, R.H. Wu, S.S. Zhang, J.J. Li, Q.H. He, and H.Q. Zhang, Nucl. Sci. Tech. 36, 191 (2025)   
[47] H.Q. You, R.H. Wu, H.Z. Su, J.J. Li, H.Q. Zhang, and X.T. He, Phys. Rev. C 110, 024319 (2024)   
[48] M. Ismail, A. Adel, and Asmaa Ibrahim, Chin. Phys. C 49, 034106 (2025)   
[49] F. Kondev, M. Wang, W. Huang, S. Naimi, and G. Audi, Chin.Phys. C 45, 030001 (2021)   
[50] J. Hilton, J. Uusitalo, J.Saren et al., Phys. Rev. C 100, 014305 (2019)   
[51] Z. Y. Zhang, H. B. Yang, M. H. Huang et al., Phys. Rev. Lett. 126, 152502 (2021)   
[52] H. B. Yang, Z.G. Gan, Y.J. Li et al., Phys. Rev. Lett. 132, 072502 (2024)   
[53] M. Thoennessen, Int. J. Mod. Phys. E 33, 2430001 (2024)

[54] H. B. Yang, Z.G.Gan, Z. Y. Zhang et al., Phys. Rev. C 105, L051302 (2022)   
[55] Yu. Ts. Oganessian, V. K. Utyonkov, M. V. Shumeiko et al., Phys. Rev. C 108, 024611 (2023)   
[56] M. M. Zhang, J.G.Wang, L.Ma et al., Nat. Commun. 16, 5003 (2025)   
[57] Yu. Ts. Oganessian, V. K. Utyonkov, N. D. Kovrizhnykh et al., Phys. Rev. C 106, 064306 (2022)   
[58] Z. Y. Wang, Z. M. Niu, Q. Liu, and J. Y. Guo, J. Phys. G 42, 055112 (2015)   
[59] X. J. Bao, S. Q. Guo, H. F. Zhang, Y. Z. Xing, J. M. Dong and J. Q. Li, J. Phys. G: Nucl. Part. Phys.42, 085101 (2015)   
[60] A. V. Karpov, V. I. Zagrebaev, Y. Martinez Palenzuela, and W. Greiner, Int. J. Mod. Phys. E 21, 1250013 (2012)   
[61] M. Ismail, A. Y. Ellithi, A. Adel, and M. A. Abbas, Phys. Scr. 97, 075303 (2022)   
[62] W. D. Myers and W. J. Swiatecki, Nucl. Phys. 81, 1 (1966)   
[63] M. Wang, W. Huang, F. Kondev, G. Audi, and S. Naimi, Chin. Phys. C 45, 030003 (2021)   
[64] S. Goriely, N. Chamel and J. M. Pearson, Phys. Rev. C 88, 061302 (2013)   
[65] D. S. Delion, Phys. Rev. C 80, 024310 (2009)   
[66] N. Wang, M. Liu, X. Z. Wu and J. Meng, Phys. Lett. B 734, 215 (2014) http://www.imqmd.com/mass/WS4 RBF.txt