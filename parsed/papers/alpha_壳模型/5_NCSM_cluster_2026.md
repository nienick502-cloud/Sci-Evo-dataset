# Theoretical Studies of $\alpha$ Clustering in Nuclei and Beyond

Takaharu Otsuka $^ { 1 , 2 ^ { : } }$ *, Alexander Volya3 and Naoyuki Itagak $^ 4$

1*Department of Physics, University of Tokyo, Hongo 7-3-1, Bunkyo-ku, 1130033, Tokyo, Japan.

$^ 2$ RIKEN Nishina Center for Accelerator-Based Science, Hirosawa 2-1, Wako-shi, 3510198, Saitama, Japan.

$^ 3$ Department of Physics, Florida State University, 311 Keen Building, Tallahassee, 32306-4350, FL, USA.

$^ 4$ Department of Physics, Osaka Metropolitan University, 3-3-138 Sugimoto, Osaka, 558-8585, Osaka, Japan.

*Corresponding author(s). E-mail(s): otsuka@phys.s.u-tokyo.ac.jp; Contributing authors: avolya@fsu.edu; itagaki@omu.ac.jp;

# Abstract

This article comprises three sections after an introduction. Section 2 starts with a quick review of the results of ab initio no-core shell model calculations by Monte Carlo Shell Model on light nuclei. It is shown that $\pmb { \alpha }$ clustering arises in such first principles calculations for $\mathbf { s } , \mathbf { 1 0 } , \mathbf { 1 2 }$ Be and $\mathrm { ^ { 1 2 } C }$ with the Daejeon16 and JISP16 interactions. The $\pmb { \alpha }$ clustering occurs even in well bound states such as the ground state of $\mathbf { \Omega } ^ { 1 2 } \mathrm { C }$ . The Hoyle state is shown to be dominated by $\pmb { \alpha }$ clustering in triangular configurations. The crossover between clustering and nuclear matter is demonstrated. As the ground and Hoyle states show strong deformations, they are also good cases to investigate rotational excitations. As an original work, the recently proposed fully quantum (mechanical) formulation for deformation and rotation is extended to cluster or molecular states. Dual rotational modes are proposed: compact-object rotation and distant-object rotation. The former is found in many heavy nuclei, whereas the latter can be found for clustering states in Be and C isotopes. While 8Be is a transparent example for the latter, $^ { 1 2 } \mathrm { C }$ is a rare example that both modes appear in different states of the same nucleus, giving another novel significance to the Hoyle state. The duality of rotation by compactobject and distant-object rotations is a visible outcome of the hierarchy by the cluster formation, placing $^ { 1 2 } \mathrm { C }$ on the border. Atomic molecules and hadrons can be viewed in terms of this duality. Possible relevances to fission is mentioned.

Section 3 presents a general framework for an extended no-core shell model with cluster–nucleon configuration interaction, combining traditional shellmodel–like configurations with explicit microscopic configurations representing cluster degrees of freedom. This approach offers a complementary perspective to the strategy discussed in the other sections. The section reviews the microscopic origins of cluster substructures in light nuclei, emphasizing how nucleonic degrees of freedom, nucleon–nucleon interactions, and continuum coupling naturally extend the traditional shell model into configuration-interaction frameworks that incorporate clustering and reaction dynamics. Both methodological developments and applications are discussed, including clustering in well-bound states as well as reaction processes involving alpha clusters.

Section 4 presents that although the cluster structure is robust in Be-C nuclei, some ${ j j }$ -coupling shell model components are mixed with clustering components in the ground state of $^ { 1 2 } \mathrm { C }$ . This is a different feature than in the cases of the Be isotopes. Using the antisymmetrized quasi cluster model (AQCM), we can clearly model this competition between the cluster and shell components. The spin-orbit interaction is key to realizing the shell structure and contributes more to the 12C case than to the 8Be case due to closer α-α distances in the former case, thanks to attraction among the clusters.

Section 5 presents remarks and prospects transcending the whole article, besides summarizing discussions within Sections 2-4.

Keywords: $\pmb { \alpha }$ cluster, Hoyle state, shell model, no-core shell mode, deformation, rotation, triaxiality, dual rotational mode, molecule, fission

# 1 Introduction

The atomic nucleus consists of $Z$ protons and $N$ neutrons, collectively referred to as nucleons. In the $\alpha$ -clustering picture, illustrated schematically in Fig. 1, the $\alpha$ particle ( $Z = N = 2$ ) (see Fig. 1a) is regarded as a fundamental building block, and certain nuclei may be described as aggregates of $\alpha$ particles, perhaps for main components of some states. In such systems, the condition $Z = N = 2 i$ holds, where $_ i$ is an integer, and the mass number $A = Z + N$ takes the values $A = 4 , 8 , 1 2 , \ldots$ A nucleus is denoted as $^ A X$ , where $X$ represents the chemical element; for example, $^ { 8 }$ Be denotes beryllium– 8. Figures 1b-c provide intuitive illustrations of possible $\alpha$ -cluster configurations in $^ { 8 }$ Be and $\mathrm { ^ { 1 2 } C }$ , respectively, in which $\alpha$ particles are depicted as mid-sized circles forming a nucleus represented by the surrounding shaded region.

Models based on $\alpha$ clustering have been developed since the 1930s [1–7]. Despite this long history, direct experimental observation of $\alpha$ clustering within nuclei remains challenging. This is partly because $\alpha$ clusters are not fundamental degrees of freedom but rather emergent correlations within an interacting quantum many-body system of nucleons. The Pauli principle and residual nucleon-nucleon correlations may constrain the allowed spatial configurations and/or may lead to substantial mixing between cluster-like and other components in some ways. As a result, geometric cluster pictures provide superb intuition but do not correspond to directly observable structures;

instead, experimental signatures of clustering must be inferred indirectly through reaction dynamics and spectroscopic observables. Part of this difficulty also arises from the intrinsically quantum-mechanical nature of nuclear motion: nuclei are not static objects, and cluster wave functions represent configurations defined in an underlying intrinsic frame rather than in the laboratory coordinate system (see Fig. 1).

Motivated by these challenges, a broad body of theoretical work has been developed, several aspects of which are reviewed in the subsequent sections from different theoretical perspectives. These sections are authored by T. Otsuka, A. Volya, and N. Itagaki, respectively. In particular, a major research project headed by T. Nakamura had been conducted in the recent past years [8] focusing on hierarchy structures involving clustering. A brief comment will be made in relations to Sect. 2.

In Sect. 2, a recent challenge involving super-large-scale ab initio no-core shell model calculations for Be and C isotopes is reviewed, depicting the emergence of $\alpha ( \cdot$ like) clustering without assuming it a priori. Contrary to the usual anticipation that $\alpha ($ (-like) clustering appears in the energy region around $\alpha$ -particle emission threshold [5], α(-like) four nucleon correlations, called $\alpha$ clustering for brevity hereafter, emerges even in well-bound states, and its mixing with normal nuclear states lowers the groundstate energy of $\mathrm { ^ { 1 2 } C }$ , for instance. Similar $\alpha$ clustering arises more distinctly in $^ { 8 } \mathrm { { B e } }$ and in the Hoyle state of $\bot 2$ C. In other words, nuclear forces and nuclear many-body dynamics favor the $\alpha$ clustering, although details may vary. This work suggests, from first principles viewpoint, that the hierarchy structure with the appearance of the $\alpha$ cluster seems to occur, but may not manifest as clearly as intuitively expected, because of nuclear forces and antisymmetrization constraints. Beyond this review, some new features are discussed. Molecular(-like) configurations of $\alpha$ clusters can naturally result in rotational motion. On the other hand, a new general formulation of rotational bands in atomic nuclei with ellipsoidal shapes has recently been presented [9], where not only the prevailing of triaxial (i.e., almond-like) shapes but also the excitation mechanism within a rotational band were major subjects. This new picture can be confronted to the rotational excitation of molecular configurations, and we can indeed analyze their relationship by applying the new formulation. This analysis leads to two basic modes of quantum mechanical rotations. Such study goes beyonds the clarification of the $\alpha$ clustering, towards a new unified picture of the rotation of quantum manybody systems, possibly including hadrons and atomic molecules as future applications. All these developments illuminate the importance of the $\alpha$ clustering in the global landscape of physics. The transition between two rotational modes and the hierarchy boundary, likely found in $\mathrm { ^ { 1 2 } C }$ , may show a very interesting coincide [8].

In Sect. 3, $\alpha$ -clustering is reviewed from a microscopic many-body perspective. The section focuses on extended configuration-interaction frameworks that incorporate microscopically constructed cluster configurations, in which full fermionic antisymmetrization and proper treatment of center-of-mass dynamics are maintained. These approaches illustrate how cluster substructures emerge naturally from nucleonic degrees of freedom and realistic nucleon-nucleon interactions. Emphasis is placed on the unified treatment of nuclear structure and reactions, targeting both spectroscopic properties and scattering observables, with representative applications spanning well-bound systems as well as reaction processes involving $\alpha$ clusters.

Sect. 4 provides a complementary review of the competition and coexistence between cluster and shell-model structures in light nuclei. Using the antisymmetrized quasi-cluster model (AQCM), the section elucidates how $\alpha$ -cluster configurations mix with and can be continuously transformed into $j j$ -coupling shell-model states, thereby offering a unified description of intermediate regimes. Applications to $^ { \mathrm { ~ 8 ~ } }$ Be and $\mathrm { ^ { 1 2 } C }$ highlight the decisive role of the spin-orbit interaction in governing cluster persistence and breaking, clarifying the physical mechanisms that drive the evolution from cluster-dominated to shell-model-like structures.

In addition to summarizing discussions within Sects. 2 - 4, Sect. 5 presents remarks and prospects transcending the discussions and results depicted in Sects. 2 - 4 focusing on $\alpha$ clustering in $^ 8$ Be and $\mathrm { ^ { 1 2 } C }$ .

# 2 First-principle realization of $\pmb { \alpha }$ clustering and dual rotational modes in quantum many-body systems

Quite a few theoretical approaches have been made for the understanding of $\alpha$ clustering in atomic nuclei. Examples such as [11–20] were performed, up to around 2020, including limiting cases like linear chains[3, 19], equilateral triangles[14] and a Bose-Einstein condensate[13]. In about the same and later periods, ab initio calculations were reported[21–25]. More references may be mentioned in Sect. 3.

The initial impactful outcome was the appearance of di- $\alpha$ clusters in the ground state of $^ 8$ Be in a VMC calculation [21, 22], similarly to Fig. 1b. The $\alpha$ clustering is more crucial but less clarified for the $^ { 1 2 } \mathrm { C }$ nucleus: this nucleus can be formed by three $\alpha$ particles in configurations, triangular, linear, or others (see Figure 1c). Its lowest spin/parity $J ^ { \pi } { = } 0 ^ { + }$ excited state, the famous Hoyle state[26–28], is a critical gateway in the nucleosynthesis to the present carbon-abundant world filled with living organisms [29, 30], but its structure remains to be clarified. The clarification of these structures lead to a novel picture of dual rotational modes in quantum many-body systems.

# 2.1 First-principles realization of $\pmb { \alpha }$ clustering in $\mathbf { 8 }$ Be and $\mathbf { \mu _ { 1 2 } } _ { \mathbf { C } }$

We now briefly review a set of computational simulations [10] without assuming $\alpha$ clustering a priori, which exhibited that $\alpha$ clustering indeed occurs for the ground and excited states of $^ { 8 , 1 0 , 1 2 }$ Be and $_ { 1 2 }$ C isotopes, including the Hoyle state, in varying formation patterns. The simulations are performed by full Configuration Interaction

![](images/b40116c43f2e3c0c4a14b0b0ff25ea8d0f8af05a8266c9a43914bb8addda5b63.jpg)

![](images/9f053d56742da72ebb03c6bb36830ef21c22503b25f9c1ca7f9adf3579995296.jpg)

![](images/5862723ac03a4c930f456ec3f8e9f9a6dd344719eefa5662e4a9519dedf52f23.jpg)  
Fig. 1 Schematic illustrations of $_ \alpha$ clustering in atomic nuclei, for a ${ } ^ { 4 } \mathrm { H e } = \alpha$ particle, b $^ 8 \mathrm { B } \bar { \mathrm { e } }$ , and $\textbf { c } ^ { 1 2 } \mathrm { C }$ (three possible cases, i, ii and iii). The green areas represent atomic nuclei allowing some movements of $_ \alpha$ clusters. Taken from [10] with permission.

![](images/1027a496a5437711c813d9e301b6e70ebb6e712fabaae3a15608cace370753e0.jpg)

![](images/211b421ff2daa427ef4b3e1f40dd36332e382bab4a2cddf19edcfb3e931a8fd7.jpg)

![](images/ccd4c14537a875bdcd526595648238542d8fe8e61d8d519c7b4a4b45e9b17c53.jpg)  
Fig. 2 Level energies of a ${ } ^ { 8 } \mathbf { B } \mathbf { e }$ and b $^ { 1 2 } \mathbf { C }$ (left) Experimental data[24, 33], and (right) theoretical results in each panel. Taken from [10] with minor changes with permission.

(CI) calculations from first principles with the Daejeon16 interaction [31] for $\mathrm { ^ { 1 2 } C }$ and with JISP16 interaction [32] for the Be isotopes, and their validity is further examined for some observables by comparing with experimental data [33] (see [10]). In the computational side, the Monte Carlo Shell Model [34–37] has been used for the study of Sect. 2, and relevant results for light nuclei are also shown in [38, 39].

Figure 2a,b display, respectively, the level energies of $^ 8$ Be and $\mathrm { ^ { 1 2 } C }$ , both experimental and theoretical, with good experiment-theory agreement. Note that the theoretical calculations were performed in the bound state approximation, which is considered to be sensible for the states to be discussed. We point out that theoretical $0 _ { 1 } ^ { + }$ and $2 _ { 1 } ^ { + }$ states can be also obtained up to 99% probability by simply projecting the same intrinsic state $K ^ { P } { = } 0 ^ { + }$ ) extracted from the shell model wave functions. Considering large E2 matrix elements related to these states, the $0 _ { 1 } ^ { + }$ and $2 _ { 1 } ^ { + }$ states are identified as members of a strongly deformed rotational band with a prolate (an oblate) shape of the deformation parameter $\beta _ { 2 } \sim 1$ (0.6) for 8Be ( $^ { 1 2 } \mathrm { C }$ ) [10]. This is an important point, and we shall use this feature later. The $B ( E 2 ; 2 _ { 1 } ^ { + }  0 _ { 1 } ^ { + }$ ) value has been also measured experimentally for $^ { 1 2 } \mathrm { C }$ [24] in a high precision, and it has been reproduced well by the present calculation with free charges as displayed in Figure 2b.

The Hoyle state in the theoretical calculation is still too high as compared to the experimental one. This is probably due to the size of the model space (seven harmonic oscillator shells). This model space appears to suffice for the description of the ground and $2 _ { 1 } ^ { + }$ state, but a somewhat wider space may improve the quality of the description of the Hoyle state. We, however, assume that the present computational setup is sufficient for the discussions below, where conceptual features are main subjects and extrapolations towards better descriptions are also possible.

Figure 3 shows density profiles of the ground, Hoyle and $0 _ { 3 } ^ { + }$ states of $\mathrm { ^ { 1 2 } C }$ , and their decompositions according to their structures. The density profile of $^ { 4 } \mathrm { H e }$ , or $\alpha$ particle, is shown for comparisons. We will later present a beautiful di- $\alpha$ structure of $^ 8$ Be emerging also from first principles. It is mentioned that the present no-core calculation is very suitable for the density profile, because in-medium corrections, including couplings to Giant Resonances, are basically treated explicitly, in contrast to usual shell-model calculations with a one or at most two valence shells.

![](images/f6a7f7f8ddee705451941189289fe6215b392a880d6cb4812bc22feb85b0ae11.jpg)

![](images/fc3deb9340bd32f04465cfca43de38db75611aa66130d27ce832d30e45461b3a.jpg)

![](images/f328e635ea9849fef89e1b3c370706db35bb8675104e105be2ab22e6ed783370.jpg)

![](images/32182090e56c42100d1c7dec139c25d97afec9ef4fbc3fb005a9ef56fe1e6ffc.jpg)

![](images/a0382a886bcf71761033fe28d6721b73a79d7978574ac36a719cf7ff0b402e4b.jpg)

![](images/fecfa0113602a77f602227dde995bcc9e872c089cf19ddffa8e4c61dca25f0b7.jpg)

![](images/84051c84558dfa3291c938127e1440581c356696ebbe5e1ad262c7212bf9cbde.jpg)

![](images/3c6de2cc79fef380dfebec4cf503eb18cc782dc79bc2c65f9f5f16013e8a719d.jpg)  
Fig. 3 Density profiles of $^ { 1 2 } \mathbf { C }$ with that of ${ } ^ { 4 } \mathrm { H e } = \alpha$ particle The density profiles for $\mathrm { ^ { 1 2 } C }$ were obtained from intrinsic states, and in panels $\mathbf { i } - \mathbf { i }$ , eigenstates are decomposed according to shapes using T-plot analysis. Taken from [10] with permission.

The $\alpha$ clustering can then be identified by three separate high peaks of the nucleon density, particularly clearly in panels $\mathbf { d }$ , $\mathbf { e }$ , g, and i. We here decomposed MCSM basis vectors into three groups, (i) medium $\beta _ { 2 }$ (<0.7), (ii) large $\beta _ { 2 }$ (>0.7) not too close to prolate shape ( $6 ^ { \circ } \leq \gamma \leq 6 0 ^ { \circ }$ ), (iii) large $\beta _ { 2 }$ (>0.7) near prolate shape $\gamma < 6 ^ { \circ }$ ). This classification was supported independently by a statistical learning technique in data science [40] (see [10]).

Eigenstates of MCSM calculations are superpositions of these basis vectors. The ground state is composed of group (i) by 94 % (panel f), but contains group (ii) by $6 \%$ (panel g), which is not negligible. The group (ii) of the ground state (panel g) exhibits a clear $\alpha$ clustering. We stress that this occurs in the ground state which is well bound. So, this is not an effect of loose binding, in contrast to some beliefs that $\alpha$ clustering arises as a consequence of weak or no binding near $\alpha$ threshold [5]. In other words, the $\alpha$ clustering can occur without the threshold effect of Ikeda et al. [5], but this work does not deny possible appearance of this threshold effect. The $\alpha$ clustering in well-bound states may be one of the very important answer to the $\alpha$ -clustering question from the first principles.

Furthermore, the total density of the Hoyle state (panel $\mathbf { d }$ ) also manifests an even clearer $\alpha$ clustering. As this calculation is still a shell model calculation, all singleparticle basis vectors are provided by the eigenfunctions of the harmonic oscillator potential and no explicit continuum components are involved. We still see a good picture of $\alpha$ clustering, probably because the $\alpha$ clustering is also a correlation effect. The above decomposition can be performed for the Hoyle state as well. Panel $\mathbf { h }$ shows the density profile formed by the basis vectors in group (i), which constitutes $3 3 \ \%$ of the eigen wave function. Likewise, Panel i shows the density profile by group (ii), which constitutes $6 1 \ \%$ of the eigen wave function. A strong mixing is found between a nuclear matter-type density (panel h) and a molecular-type density (panel i). Because the present $0 _ { 2 } ^ { + }$ state is formed primarily of the $\alpha$ clustering state and its energy is close to the experimental value of Hoyle state, it is implied that the Hoyle state has thus been reproduced from first principles, apart form possible improvement of the precision. Note that Daejeon 16 interaction was not tuned for this calculation at all.

![](images/ffac6f840517565a38971a2cf1cacff95daf8a8a6520a06e48bd0b975c407bf8.jpg)  
Fig. 4 Overall picture of ground and Hoyle states of $^ { 1 2 } \mathbf { C }$

Thus, $\alpha$ clustering structures emerge from the first principles without assuming them a priori, as emphasized in [10]. This can be an important achievement of no-core MCSM calculation powered by Daejeon 16 interaction.

The nuclear-matter-type density profile, characterized by a constant density over a certain region, emerges definitely in the ground state, and rather modestly in the Hoyle states. At the same time, $\alpha$ -clustering-type density profile also emerges in these states, certainly to different extents. It is of interest how building-block states producing these density profiles arise and are mixed. Figure 4 exhibits a sketch for this point.

We begin with the ground state. The two components corresponding to groups (i) and (ii) are located at the energies $E = - 9 1 . 0$ and -80.4 MeV, as shown in the left half of Fig. 4. Due to the nuclear forces (Daejeon16 interaction in this case), they are mixed, and the resulting state appears at the energy lower by 0.8 MeV, with the mixing probabilities 94% and $6 \%$ , respectively, for nuclear matter (group (i)) and cluster (group (ii)) components. Note that the classification was made according to ellipsoidal shapes of basis vector states, but the two components were named after their density-profile characters. The mixing of 6% gives the ground state additional binding energy of 0.8 MeV. Thus, the nuclear forces favor the $\alpha$ clustering even in the middle of nuclear matter, although it may occur mainly around the surface. This surface enhancement is another interesting feature to be further investigated.

We now move on to the Hoyle state. The nuclear-matter component formed by group (i) is located at -86.0 MeV. It is closer to a sphere than the one for the ground state. The cluster component is located at -84.2 MeV, lower by 3.8 MeV than its counterpart for the ground state. This is 7.6 MeV above the ground-state energy, which is closer to the experimental Hoyle-state energy. However, nature is not so nice in this case, and pushes up the mixed state to -81.0 MeV. This repulsive mixing occurs

![](images/f4e6a7de9f3ab688ac51db19c8d2d37b642f175cbfb5b778c5e1dcee7e6de563.jpg)  
a legend

![](images/e6885dc076a9e89ef0e75bf7fd87ac3ce750f53e1409058389cc32185bffb3bc.jpg)

![](images/586cc6694bedc3ca93b956d50e494d1b5b10234906fbdd24712fd3f45301200e.jpg)  
d $0 . 5 \dot { 2 } < 0 . 5 \dot { 2 } < 0 . 5 \dot { 2 } < 0 . 5 \dot { 2 } < 0 . 5 \dot { 2 }$ (Hoyle) state

![](images/69d302058d45b1ec05cd0ff6794e7d513a62efe82d034a2dfc5f4c8d0302c9d2.jpg)  
$0 _ { 3 } ^ { + }$

![](images/5b5e40c28e06b3d2db53fb485aba912cdfb3fe9fec5309985dec060871dfa371.jpg)  
bαparticle（4He)

![](images/f73e1c1bb7e0084663ec81f97911d2270193fb74ddfb34b8b16324a10ddd851b.jpg)  
f $0 _ { 1 } ^ { + }$ state region I $94 \%$

![](images/3679a0af806ae0e4d44d6674848ee1c81ed4e8613e9dbcdf791acbefd0538ad8.jpg)  
g $0 _ { 1 } ^ { + }$ state region I 6%

![](images/9e7c4aba0d094e93ea3161bfbdf385544c915a1e80af8bd3a1d1f005b28aad2b.jpg)  
8Be

![](images/de28fef2b842e1fda02ee32103a8dd2c079a270bdbc1cbbb0b4337cac2f6c7d3.jpg)

![](images/f0e92fec022e20b43e9a8c687d3dac2169b0297ac607cfd2825054003e576c63.jpg)

![](images/3e9f103a4e1ebe446cbc5246c9ceac1d50297aabff9799a2a41407b050025529.jpg)  
Fig. 5 Two-dimensional representation of matter density profile of $\mathbf { \mu } ^ { 1 2 } \mathbf { C }$ compared to ${ } ^ { 4 } \mathbf { H } \mathbf { e }$ and ${ } ^ { 8 } \mathbf { B } \mathbf { e }$ Densities of $^ 4 \mathrm { H e }$ and $^ 8 \mathrm { B e }$ are shown in the far left part. Panels c - i correspond, respectively, to Panels c - i of Fig. 3. Two-way arrow indicates the distance between two peaks of 8Be density with the length ${ \sim } 3 . 6 ~ \mathrm { f m }$ , and is also shown for some panels for $\mathrm { 1 2 } _ { \mathrm { C } }$ . Modified from figures in [10] with permissions.

basically because of the orthogonality to the ground state. The mixed state is still below the unperturbed cluster component of the ground state, so there is still some binding-energy gain.

This is a sketch how the ground and Hoyle state are formed. The relation between clustering and normal nuclear matter is considered to be a crossover[41] as pointed out in [10], and appears to be rather complicated as each structure also has variations. Indeed, the mixing between such two structures plays significant roles, especially in the ground state, and may lead us to further understanding of $\alpha$ decay of the states well-bound in general. The cluster-component wave function of the Hoyle state may be somewhat improved by including more single-particle states of harmonic oscillator potential, making individual “clusters” more $\alpha$ -particle-like as a possibility. The

positions of those clusters may not substantially change, however. In order to see this point, we show the distances between clusters in Fig. 5. The density profile for $^ { \mathrm { ~ 8 ~ } }$ Be is shown in the left lower corner of Fig. 5, and the distance between two peaks appears to be about 3.6 fm. This value is obtained by human eyes, but other manners will lead to similar values. The distance is displayed by two-way arrow. We can put the same arrow with angles tilted in panels for $\mathrm { ^ { 1 2 } C }$ in Fig. 5, where panels $\mathbf { c }$ - i correspond, respectively, to panels c - i in Fig. 3. We find remarkable similarities between the 8Be distance and the distances in those $\mathrm { ^ { 1 2 } C }$ cases. The distance ${ \sim } 3 . 6$ fm has a special meaning for keeping $\alpha$ -cluster-like structures, as a balance between kinetic energy and binding effects by nuclear forces. For $\mathrm { ^ { 1 2 } C }$ , additional single-particle states of harmonic oscillator potential may shape up wave functions of individual clusters, but may not change their positions much.

Summarizing this subsection, $\alpha$ clustering emerges as a consequence of nuclear forces in the present first principles calculation. The Hoyle state is primarily made up of three $\alpha$ clusters as discussed in quite a few earlier works of various types, but its triangular configuration is presently not equilateral. The ground and $2 _ { 1 } ^ { + }$ states are members of an oblate rotational band with $\beta _ { 2 } ~ \sim ~ 0 . 6$ [10]. The Hoyle state is also strongly deformed in terms of quadrupole deformation with $\beta _ { 2 } \gtrsim 1 . 0$ [10]. We now turn to discussions on such strongly deformed state and their rotations.

# 2.2 General description of rotational excitations within quantum many-body theory

In the classical mechanics, a rigid body rotates as sketched in Fig. 6a. This motion evolves as time goes by, following the Newtonian equation.

We then consider the free rotation of a rigid body in the quantum mechanics. The angular momentum has to be quantized. Provided that the rigid body is of axially symmetry, as illustrated in Fig. 6b, the rotational kinetic energy is proportional to ( $\vec { J }$ $\bar { J }$ ), where the angular momentum of the rigid body is denoted by $\hbar J$ . The eigenvalues of the rotational kinetic energy are then proportional to $J ( J + 1 )$ .

We now move on to nuclei. In the picture of deformed nuclei proposed by Aage Bohr [42–45], the nucleus is described as a deformed object with a fixed shape filled with a uniform-density matter. It was still a rigid body. The argument in the previous paragraph is applied to the nuclear case. The so-called Bohr Hamiltonian contains a kinetic term representing the rotational motion of this rigid body about three principal axes (see e.g., [46]). By assuming the axial symmetry of this object, the $J ( J + 1 )$ rule of excitation energies within a rotational band arises, exhibiting an account for the origin of observed level-energy regularity ( $\propto \ J ( J + 1 ) )$ in many nuclei. This axially-symmetric rigid-body picture for deformed nuclei seems to be one of the major elements of the Nobel prize of physics in 1975 [47], and has remained as a paradigm of nuclear rotational bands for (the majority of) the community.

We now turn to another formulation which is free from the classical (or semiclassical) picture/interpretation where a deformed nucleus is regarded as an axiallysymmetric rigid-body. In quantum many-body theory, a rotational band can be defined as a set of many-nucleon states, where the member of angular momentum $J$ is generated by projecting a common intrinsic state onto this angular momentum $J$ . This

![](images/12f5558b05948470e1b73711c6cfc685e24d2158e52edaf0d0169768c37bb2ad.jpg)  
Fig. 6 Schematic illustrations of the rotation in classical and quantum mechanics. a. Classical mechanical view. b. Quantization of freely rotating rigid body. c. View of the quantum mechanical system composed of many constituents with angular momentum $\hbar J$ . The $J ( J + 1 )  – K ^ { 2 }$ rule arises. The green arrow indicates similarity in the wave function, but the energy comes from different origins. Taken from Fig. 24 of [9] with kind permission of The European Physical Journal (EPJ).

definition itself may not be new, but we start from it and re-formulate the whole description of rotational bands, staying inside quantum mechanics (without resorting to the quantization of the free rotation of an axially-symmetric rigid-body). We will come back to differences from conventional formulations later.

We somewhat elaborate on the actual theoretical process as pedagogically as possible, largely because it matters to major discussions later. The angular-momentum projection method is formulated with Wigner’s D function (see eq.(9) of [9] where [46] is cited for it), and we begin with its concise sketch. First, the intrinsic state is denoted by $\phi$ . The state $\phi$ can be a sophisticated state containing full of correlations by nuclear forces. So, it does not have to be a simple state. From this $\phi$ , we obtain the state of definite $J$ and $M$ , the total angular momentum and its $\mathbf { Z }$ -projection in the laboratory frame. This projection can be performed by rotating $\phi$ in the threedimensional space with three Euler angles $\alpha , \beta$ and $\gamma$ , and by integrating it with an appropriate weighting factor, Wigner’s D function. The obtained state is written as,

$$
\begin{array}{l} \Psi [ \phi , J, M, K ] = (2 J + 1) / (8 \pi^ {2}) \int_ {0} ^ {2 \pi} d \alpha \int_ {0} ^ {\pi} d \beta \sin \beta \int_ {0} ^ {2 \pi} d \gamma \\ \left\{D _ {M, K} ^ {J} (\alpha , \beta , \gamma) \right\} ^ {*} e ^ {i \alpha \hat {J} _ {z}} e ^ {i \beta \hat {J} _ {y}} e ^ {i \gamma \hat {J} _ {z}} | \phi \rangle , \tag {1} \\ \end{array}
$$

where $D$ is the Wigner’s function.

Equation (1) implies that the three-fold rotation of $\phi$ generates states with good $( J , M )$ pairs. One notices an additional index of $K$ . In fact, there can be different and

independent states from the same $\phi$ for a given pair ( $J$ , $M$ ), and $K$ specifies them. By doing the $J _ { z }$ rotation $( e ^ { i \gamma \bar { J } _ { z } } )$ with proper weighting factor, we project $\phi$ onto a specific value of $K$ , the $z$ -component of $\vec { J }$ of $\phi$ . In this section, $K { = } 0$ is assumed for clarity, while more general cases can be discussed similarly [9].

This $K = 0$ state, denoted by $\phi _ { 0 }$ , is obtained by extracting the relevant parts from eq. (1),

$$
\phi_ {0} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} d \gamma e ^ {i \gamma \hat {J} _ {z}} \phi . \tag {2}
$$

It is clear that all relevant orientations are superposed with the same amplitude.

We also take $M { = } 0$ without losing generality, because the Hamiltonian is rotationally invariant. The relation

$$
D _ {M, K} ^ {J} (\alpha , \beta , \gamma) = e ^ {i M \alpha} d _ {M, K} ^ {J} (\beta) e ^ {i K \gamma}, \tag {3}
$$

is used with $d _ { M , K } ^ { J } ( \beta )$ being the (small) $d$ function. With M=K=0, eq. (3) becomes

$$
D _ {M = 0, K = 0} ^ {J} (\alpha , \beta , \gamma) = d _ {0, 0} ^ {J} (\beta). \tag {4}
$$

With this, we consider $J$ -projected norms and Hamiltonian matrix elements. Because of $M { = } 0$ , the $\phi _ { 0 }$ state appears for the bra state. The norm of the $J$ -state component contained in $\phi _ { 0 }$ is now given by,

$$
\begin{array}{l} | \mathcal {N} _ {J} | ^ {2} = \frac {2 J + 1}{8 \pi^ {2}} \int_ {0} ^ {2 \pi} d \alpha \int_ {0} ^ {\pi} d (\cos \beta) \int_ {0} ^ {2 \pi} d \gamma \\ \langle \phi | \left\{D _ {0, 0} ^ {J} (\alpha , \beta , \gamma) \right\} ^ {*} e ^ {i \alpha \hat {J} _ {z}} e ^ {i \beta \hat {J} _ {y}} e ^ {i \gamma \hat {J} _ {z}} | \phi \rangle \\ = \frac {2 J + 1}{2} \int_ {0} ^ {\pi} d (\cos \beta) d _ {0, 0} ^ {J} (\beta) \left\langle \phi_ {0} \mid e ^ {i \beta \hat {j} _ {y}} \right| \phi_ {0} \rangle . \tag {5} \\ \end{array}
$$

The corresponding quantity for the Hamiltonian, $H$ , is obtained by inserting $H$ after $\langle \phi |$ or $\langle \phi _ { 0 } \mid$ .

The normalized expectation value of the Hamiltonian $H$ for the projected state is then given by

$$
\begin{array}{l} E _ {J} = \frac {\int_ {0} ^ {\pi} d (\cos \beta) d _ {0 , 0} ^ {J} (\beta) \langle \phi_ {0} | H e ^ {i \beta \hat {J} _ {y}} | \phi_ {0} \rangle}{\int_ {0} ^ {\pi} d (\cos \beta) d _ {0 , 0} ^ {J} (\beta) \langle \phi_ {0} | e ^ {i \beta \hat {J} _ {y}} | \phi_ {0} \rangle} \\ = \frac {\int_ {0} ^ {\pi} d (\cos \beta) d _ {0 , 0} ^ {J} (\beta) h _ {y} (\beta)}{\int_ {0} ^ {\pi} d (\cos \beta) d _ {0 , 0} ^ {J} (\beta) n _ {y} (\beta)}, \tag {6} \\ \end{array}
$$

where the energy and norm kernels are introduced as,

$$
h _ {y} (\beta) = \left\langle \phi_ {0} \mid H e ^ {i \beta \cdot \tilde {J} _ {y}} \mid \phi_ {0} \right\rangle , \tag {7}
$$

and

$$
n _ {y} (\beta) = \langle \phi_ {0} | e ^ {i \beta \hat {J} _ {y}} | \phi_ {0} \rangle . \tag {8}
$$

The following identity is recalled,

$$
d _ {0, 0} ^ {J} (\beta) = P _ {J} (\cos \beta), \tag {9}
$$

where $P _ { J } ( \cos \beta )$ stands for a Legendre polynomial. By expanding it in terms of (cos $\beta -$ $1 ) ^ { k }$ , with k=0, 1, 2, ..., the first two terms of the expansion are written as,

$$
P _ {J} (\cos \beta) = 1 + J (J + 1) / 2 (\cos \beta - 1) + \dots . \tag {10}
$$

The two terms in eq. (10) give a good approximation if $\cos \beta$ is close enough to unity.

The values of $n _ { y } ( \beta )$ and $h _ { y } ( \beta )$ are reduced quickly as $\beta$ moves away from 0, as a consequence of strong deformation. With this situation, the $d$ function is approximated as

$$
d _ {0, 0} ^ {J} (\beta) = P _ {J} (\cos \beta) \approx 1 + F _ {J} (\cos \beta - 1) \text {f o r} \beta \approx 0, \tag {11}
$$

with

$$
F _ {J} = J (J + 1) / 2. \tag {12}
$$

As the integral is carried out with the variable cos $\beta$ in eqs. (5) and (6), the $d$ -function in eqs. (5) and (6) is naturally replaced by the function in eq. (11), a polynomial of $( \cos \beta - 1 )$ .

The range of $\beta$ runs from 0 to $\pi$ . Sizable contributions to the quantities are expected also for $\beta$ close to $\pi$ , as the overlap is generally restored. For $\beta \sim \pi$ , the linear and other approximations starting from $\beta \ : = \ : \pi$ back to smaller values work well also. Although these contributions can be evaluated in the same way as those from $\beta \sim 0$ , their concrete description is omitted for brevity.

We define

$$
n _ {k} = \int d (\cos \beta) n _ {y} (\beta) (\cos \beta - 1) ^ {k}, \quad \text {f o r} k = 0, 1, 2, \dots , \tag {13}
$$

and

$$
e _ {k} = \int d (\cos \beta) h _ {y} (\beta) (\cos \beta - 1) ^ {k}, \quad \text {f o r} k = 0, 1, 2, \dots . \tag {14}
$$

The projected energy of the state of $J$ is given by

$$
E _ {J} \approx \frac {e _ {0} + F _ {J} e _ {1}}{n _ {0} + F _ {J} n _ {1}}. \tag {15}
$$

As the inequalities, $n _ { 1 } / n _ { 0 } , e _ { 1 } / e _ { 0 } \ll 1$ , hold for strongly deformed states, the energy eigenvalues are then given by,

$$
E _ {J} \approx E _ {0} + J (J + 1) \frac {1}{2} \frac {e _ {0}}{n _ {0}} \left\{\frac {e _ {1}}{e _ {0}} - \frac {n _ {1}}{n _ {0}} \right\}, \text {w i t h} E _ {0} = \frac {e _ {0}}{n _ {0}}. \tag {16}
$$

The $J ( J + 1 )$ rule of the rotational excitation energy thus emerges within quantum many-body theory for strongly deformed states. We stress that the quantization of free rotation of axially symmetric rigid-body is not used. Some details about the

![](images/192a75f2c2df3faf436a8d930b931a2f1cd9b95005382fc5b3bd4140c7422bb5.jpg)  
Fig. 7 A graphical illustration of the origin of the $J ( J + 1 )$ rule of excitation energies within a rotational band. Blue downward arrows mean binding energies for the states with the angular momentum $J { = } 0$ , 2, 4. The differences from the energy of the $J { = } 0$ state are exhibited by open upward arrows. The present fully quantum mechanical study indicates their height being proportional to $J ( J + 1 )$ , if strong ellipsoidal deformation occurs, irrespectively of triaxiality. For $K \_ { \mathrm { { \scriptsize ~ > } 0 } }$ , the $\{ J ( J + 1 ) - K ^ { 2 } \}$ rule is obtained similarly, on top of the $J { = } K$ state. Taken from figures in [48].

polynomial expansion of the $d$ function are found in [9], including some history. For general $K > 0$ values, more general $\{ J ( J + 1 ) - K ^ { 2 } \}$ rule has also been given in [9, 48].

The most important property suggested by eq. (16) may be the feature displayed in Fig. 7: the $J ( J + 1 )$ dependence of the excitation energy originates in the $J$ -dependent reduction (i.e., decrease) of the binding energy provided by the Hamiltonian, $H$ . This reduction occurs primarily in the contributions of various parts of the nuclear forces, including single-particle energies, two-nucleon forces, three-nucleon forces, etc. All parts give the $J ( J + 1 )$ dependence for strong deformation. In many practical calculations made so far, the kinetic energy appears to be a tiny fraction, or even can work against (lowering rather than raising).

# 2.3 Rotational excitations built on clustering states

The quantum many-body formulation of the rotational mode presented in the previous subsection can obviously be applied to the ground and $2 _ { 1 } ^ { + }$ states of $\mathrm { ^ { 1 2 } C }$ , as they are nuclear-matter-type states. The properties shown in Fig. 7 should basically hold for them.

A question arises here as to what picture is appropriate for the states dominated by cluster formation, which differ in structure from nuclear-matter states as discussed in Subsect. 2.1. The most straightforward example may be the ground and $2 _ { 1 } ^ { + }$ states of 8Be, where the $d i$ - $\alpha$ cluster appears to be a full description of these states as demonstrated in the left lower corner of Fig. 5.

We therefore extend the general formulation described in Subsect. 2.2 so as to be applicable to the case of one cluster, as shown in Fig. 8a, where a small circle stands for a cluster. This is certainly a simplified treatment of more realistic case shown in Fig. 8b, which corresponds to $^ 8$ Be case. As the cluster is supposed to be stable internally and have spin zero, its motion as a whole is described in terms of its center of gravity. The intrinsic wave function of this cluster is denoted by $\phi _ { 0 }$ , following the convention of Subsect. 2.2. By definition, it is a $K ^ { P } { = } 0 ^ { + }$ state. We assume that the

![](images/ad5edd01a16d4e67109e3d5788394ce5b9ea9566aeabefb656185302e90d90f4.jpg)

![](images/b9a012d6869a407b66af9b70f522998b8e33c64696e8bb357ed0dbaae9d23fb0.jpg)

Fig. 8 A schematic illustration of the rotational mode of clustering states.   
![](images/8f717b5c6394e07b15028f67847db295e0e61ffe168c35166d544b2e8e9925bd.jpg)  
Red and yellow circles imply clusters for systems with a single cluster, b two clusters just opposite over the origin, and c a possible configuration of three clusters. Yellow circles in a,b denote rotation of red ones by angle $\beta$ in the integral (see the text). In $\mathbf { c }$ , such rotation angles are too complicated to be included. Gray rectangular boards indicate the planes where clusters are in relevant senses. $R$ stands for the radius of cluster’s moving surface.Bold blue lines are to guide the eye.

internal state of the cluster is of angular momentum $J _ { c } { = } 0$ with positive parity, for simplicity.

The overlap between intrinsic state $\phi _ { 0 }$ and its rotated state $e ^ { i \beta \hat { J } _ { y } } \mid \phi _ { 0 } \rangle$ is called norm kernel as mentioned earlier, and is shown in eq. (8). Likewise, the energy kernel is shown in eq. (7). Both quantities should have large magnitudes at and near $\beta$ =0, and damp quickly as $\beta$ moves away from $\beta$ =0.

The Hamiltonian $H$ of the present system contains two parts: the kinetic energy of the center of gravity of the cluster, $H _ { g }$ , and the internal part $H _ { i }$ of the cluster. The cluster is considered to be self-contained, implying that the internal state is the lowest eigen state of $H _ { i }$ with the eigenvalue $\epsilon$ . We assume this for obtaining the basic picture to start with, and obtain

$$
\begin{array}{l} h _ {y} (\beta) = \langle \phi_ {0} | (H _ {g} + H _ {i}) e ^ {i \beta \hat {J} _ {y}} | \phi_ {0} \rangle \\ = \left\langle \phi_ {0} \right| \left(H _ {g} + \epsilon\right) e ^ {i \beta \hat {J} _ {y}} \left| \phi_ {0} \right\rangle \\ = \left\langle \phi_ {0} \right| H _ {g} e ^ {i \beta \hat {J} _ {y}} \left| \phi_ {0} \right\rangle + \epsilon n _ {y} (\beta). \tag {17} \\ \end{array}
$$

Because the cluster is in the $J _ { c } = 0 ^ { + }$ ground state with its internal eigen energy denoted by $\epsilon$ , the second term on the right-hand-side produces a constant shift of $\epsilon = E _ { J _ { c } = 0 ^ { + } }$ (see eq. (6)). Keeping this in mind, we shall not consider contributions of this term hereafter. Likewise, besides $H _ { g }$ and $H _ { i }$ , there is Hamiltonian representing the radial motion of the cluster. It is not considered here either, as the radius of the center of gravity of the cluster is fixed at a given length. This is taken as a reasonable modeling for the present basic picture. Note that various properties of the radial motion, e.g.

radial smearing of wave function, can be included in more elaborate calculations at varying levels of sophistication, keeping basic features to be shown here.

In the present case, as shown in Fig. 8b, the center of gravity of the cluster is rotated by the Euler angle $\beta$ , with a fixed radius, $R$ , from the center of the gravity of the whole nucleus. The center of gravity of the cluster can be treated as a point mass. As the radius is fixed, the relevant part of the Hamiltonian is its zenith-angle dependent part of the kinetic energy, which can be found in any textbook of quantum mechanics:

$$
H _ {g} = - \frac {\hbar^ {2}}{2 \mathcal {I}} \frac {1}{\sin \beta} \frac {\partial}{\partial \beta} (\sin \beta \frac {\partial}{\partial \beta}), \tag {18}
$$

where $\mathcal { L }$ is moment of inertia with ${ \mathcal { T } } = m R ^ { 2 }$ with $m$ being the mass of cluster. The energy kernel is

$$
\begin{array}{l} h _ {y} (\beta) = - \frac {\hbar^ {2}}{2 \mathcal {I}} \langle \phi_ {0} | \frac {1}{\sin \beta} \frac {\partial}{\partial \beta} (\sin \beta \frac {\partial}{\partial \beta}) e ^ {i \beta \hat {J} _ {y}} | \phi_ {0} \rangle , \\ = - \frac {\hbar^ {2}}{2 \mathcal {I}} \frac {1}{\sin \beta} \frac {\partial}{\partial \beta} (\sin \beta \frac {\partial}{\partial \beta}) n _ {y} (\beta). \tag {19} \\ \end{array}
$$

By performing partial integration twice, we obtain

$$
\begin{array}{l} e _ {0} = - \frac {\hbar^ {2}}{2 \mathcal {I}} \int d \beta \sin \beta \frac {1}{\sin \beta} \frac {\partial}{\partial \beta} (\sin \beta \frac {\partial}{\partial \beta}) n _ {y} (\beta), \\ = - \frac {\hbar^ {2}}{2 \mathcal {I}} \left[ \left(\sin \beta \frac {\partial}{\partial \beta}\right) n _ {y} (\beta) \right] _ {0} ^ {\pi} = 0. \tag {20} \\ \end{array}
$$

Here $( \sin \beta \frac { \partial } { \partial \beta } ) n _ { y } ( \beta )$ is assumed to vanish at $\beta$ =0 and $\pi$ , as it is very likely.

Similarly, we obtain

$$
\begin{array}{l} e _ {1} = - \frac {\hbar^ {2}}{2 \mathcal {I}} \int d \beta (\sin \beta) (\cos \beta - 1) \frac {1}{\sin \beta} \frac {\partial}{\partial \beta} (\sin \beta \frac {\partial}{\partial \beta}) n _ {y} (\beta) \\ = + \frac {\hbar^ {2}}{2 \mathcal {I}} \int d \beta (2 \cos \beta \sin \beta) n _ {y} (\beta), \tag {21} \\ \end{array}
$$

If $n _ { y } ( \beta )$ is non-vanishing only for $\beta$ very close to 0, this quantity becomes

$$
e _ {1} \approx + \frac {\hbar^ {2}}{2 \mathcal {I}} 2 \int d \beta (\sin \beta) n _ {y} (\beta) = + \frac {\hbar^ {2}}{2 \mathcal {I}} 2 n _ {0}. \tag {22}
$$

Because of eq. (20), $\frac { e _ { 0 } } { n _ { 0 } } \frac { n _ { 1 } } { n _ { 0 } }$ term in eq. (16) vanishes. Equation (16) then becomes

$$
E _ {J} \approx E _ {0} + J (J + 1) \frac {1}{2} \frac {e _ {1}}{n _ {0}} \approx \frac {\hbar^ {2}}{2 \mathcal {I}} J (J + 1), \tag {23}
$$

with

$$
E _ {0} = \frac {e _ {0}}{n _ {0}} = 0. \tag {24}
$$

![](images/35671458f362e82f8acfa4aeff34968ad1311b6b9db97387070f272f811cc46e.jpg)  
Fig. 9 Conceptual comparison between (upper part) distant-object rotation and (lower part) compact-object rotation. Panels a and b represent $d i$ -cluster system at different orientations, where each cluster is an eigenstate of internal Hamiltonian. Panel $\mathbf { c }$ schematically displays superposition of the $d i$ -cluster system at various orientations, yielding distant-object rotation. Panels $\mathbf { d }$ and e represent the ellipsoid at different orientations. The elongated parts (green and blue) are coupled by the Hamiltonian including interactions among constituents. Panel f shows what would happen if only the center of gravity of blue part were to be rotated to another orientations. Panel $\mathbf { g }$ schematically displays superposition of the same ellipsoid at various orientations, yielding compactobject rotation.

We thus obtain the energy formula for strongly localized cluster contents. Note that the approximation in eq. (22) does not affect the appearance of the $J ( J + 1 )$ rule, and changes emerge in the coefficient depending on the deviation from this approximation. The deviation is expected to be small for visible clustering cases. The formula looks the same as the equation for the quantized energies of free rotation of a point mass, while corrections to it are also in the scope.

The excitation energy can be similarly derived for $d i$ -cluster systems like the one shown in Fig. 8b with proper value of the moment of inertia. Furthermore, the axially symmetric rigid-body follows the same equation. We stress that details of the localization are irrelevant, as $n _ { 0 }$ cancel each other between the numerator and the denominator in eq. (23), bringing about a kind of beauty.

It is very interesting that the excitation energy now originates in rotational kinetic energy in contrast to the situation discussed in Subsect. 2.2, the outcome of which is

graphically depicted in Fig. 7. A comparison between these two situations is intuitively illustrated in Fig. 9, where Panels a-c exhibit the rotational mode of clustering system and Panels d-g are about the rotational mode of ellipsoidal matter system. The “free” rotation of clusters within quantum many-body picture is characterized here: while the wave function of good $J$ is a superposition over all possible orientations, the excitation energy is provided by the total rotational kinetic energy of the centers of gravity of the clusters. Such a natural picture arises from the present formulation.

For the sake of transparency, we now characterize these two types of situations by calling the former “distant-object” rotation (see Figs. 9a-c) and the latter “compactobject” rotation (see Figs. 9d, $\mathbf { e }$ and g). Both are quantum mechanical in the sense that the wave functions are superpositions over all orientations with specified amplitudes. However, the dynamical origin differs completely between the two. In the distantobject rotation, each cluster is basically in an eigenstate of its internal Hamiltonian and the excitation energy within a band represents rotational kinetic energy. On the contrary, the compact-object rotation occurs, for instance, with ellipsoids, where the elongated parts are not eigenstates at all (see Panels $\mathbf { d }$ and $\mathbf { e }$ ), and those in different orientations are coupled by the Hamiltonian including interactions among constituents, which are nuclear forces presently. The change from Panels $\mathbf { d }$ to $\mathbf { e }$ involves proper tilting of the elongated part. This cannot be made by simply rotating the center of gravity of the elongated part, as intuitively shown from Panels $\mathbf { d }$ to f. The rotational kinetic term of this center of gravity is considered to yield quite minor contributions because of reduced overlap due to the tilting between Panels $\mathbf { e }$ and f. Note that this overlap remains unity for the distant-object rotation. A classical counterpart probably does not exist for the compact-object rotation.

We note that in both compact-object and distant-object rotations, the $J { = } 0$ state (or state of no spinning) implies that the phase remains the same in all orientations for the same intrinsic state, instead of pointing to one direction.

# 2.4 Rotational mode in $\pmb { 8 }$ Be

The formulation of Subsect. 2.3 is applied straightforwardly to the structure of $^ 8$ Be. For simplicity, we identify the peak position of the matter density as the center of gravity of cluster, and the density distribution is assumed to be localized enough, consistently with the picture of Subsect. 2.3. The radius of the center-of-gravity movement is estimated as $R = 1 . 8$ fm as shown in Fig. 5. From this value, we can obtain

$$
E _ {J} \approx 0. 8 0 J (J + 1) \mathrm {M e V}, \tag {25}
$$

where $J$ stands for the angular momentum of $^ 8$ Be nucleus and $E _ { J }$ is the excitation energy of the corresponding state in the rotational band. This gives us $E _ { 2 ^ { + } } \ \approx \ 4 . 8$ MeV. This value compares well with the result ( 4 MeV) of the ab initio no-core MCSM calculation shown in Fig. 2. The moment of inertia parameter should be larger, as the density distribution is somewhat more spread (see Fig. 5). From this viewpoint, the agreement here is considered to be quite good.

The present feature arises from the localization of the cluster (i.e., quick damping of norm kernel), but is independent of details of cluster wave functions, because the

![](images/5220a73eac371dae2c258c15204cbb8170bba44ae932ec6a98e4399d3d1b2df1.jpg)  
Fig. 10 Possible rotational band built on Hoyle state, a, experimental and b, theoretical. Panel a is taken from [53] with permission. Panel b displays the result of the present theoretical estimate with uncertainty depicted by the thickness of the bars due to simple approximation to precise calculation (see text).

same norm kernel appears both in the numerator and the denominator ( $\frac { \epsilon _ { 1 } } { n _ { 0 } }$ in eq. (23)). So, this beautiful feature is robust in this respect.

# 2.5 Coexistence of two rotational modes in $\mathbf { \mu _ { 1 2 } } _ { \mathbf { C } }$

We now come back to the nucleus $\mathrm { ^ { 1 2 } C }$ , which is not as simple as 8Be.

The structure of the Hoyle state is of great interests and still attracts attentions of comparatively recent works [49–55]. It is characterized by cluster configurations as suggested in Figs. 3 and 5. For this subsection, the latter figure is more suitable. Figure 5d indicates the emergence of three $\alpha$ -like clusters. We assume that each cluster is rather self-contained and stable, and behaves like an $\alpha$ particle. In fact, by enlarging the single-particle model space in the MCSM calculation, each cluster may better resemble a free $\alpha$ particle. With this expectation, certain properties of the Hoyle state may be described, in a reasonable approximation, as a system of three clusters with individual center of gravity located in the peak positions in Fig. 5d. These positions seem to be useful in further studies, because experimental data of E0 decay [33] and root-mean-square radius [56] compare well with the calculated values [10].

The rotational band built on the ground state has been discussed in Subsects. 2.1 and 2.2. This band is indicated in Fig. 2.

We now discuss another possible rotational band built on the Hoyle state. Its experimental observation has been reported in [52, 53], as displayed in Fig. 10 partly taken

from [53]. Although the establishment of this band may remain open experimentally, we assume it exists in the way proposed. While this band appears above $\alpha$ threshold, we suppose that we discuss doorway states before decays. The Hoyle state and the rotational band are then described by the distant-object rotation of a tri- $\alpha$ intrinsic state. However, as depicted in Fig. 5, the tri- $\alpha$ configuration is not of axial symmetry, and is indeed triaxial like the one shown in Fig. 8c. The structure is then not as simple as the one for 8Be.

The intrinsic state, $\phi$ , represents a tri- $\alpha$ state like the one shown in Fig. 8c, putting distortions from the pure (or free) $\alpha$ structure aside. We first look into the $K$ quantum number, which is the $z$ component of the angular momentum. For triaxial configurations like Fig. 8c, three moments of inertia emerge in the classical mechanics, with different values depending on the rotation axis. The moment of inertia can be similarly calculated from the nucleon density distribution of the intrinsic state, within quantum mechanics. We then define the $z$ axis so that the moment of inertia about the $z$ axis becomes the smallest, for the reason stated later. In this way, the $K$ quantum number gains a certain physical meaning rather than an arbitrary index, also in the cases being discussed. This definition is surely consistent with the one for compact-object rotation, where the $z$ axis is usually taken to be along the longest axis of the ellipsoid. We here mention that this $K$ value is practically conserved by the same argument as in [9], provided that in $\phi$ , strong mutual localization of nucleons into small volume of a specified cluster occurs and the center of gravity of each cluster is also localized in the intrinsic state, as expected in the usual $\alpha$ clustering. These arguments are partly based on [57].

Following eq. (14) of [9], the energy of the state with a good $K$ value, denoted by $\Phi [ \phi , K ]$ , is given by

$$
\begin{array}{l} h _ {K} = \left\langle \Phi [ \phi , K ] \mid H \mid \Phi [ \phi , K ] \right\rangle \\ \propto \int_ {0} ^ {2 \pi} d \gamma \cos (K \gamma) \langle \phi | H | e ^ {i \gamma \hat {J} _ {z}} \phi \rangle . \tag {26} \\ \end{array}
$$

The relevant part of Hamiltonian is the kinetic energy for the rotation about the $z$ axis of the centers of gravity for three $\alpha$ clusters in a fixed configuration, like the one shown in Fig. 8c. The angle of this $z$ -axis rotation is denoted by $\gamma$ . We then obtain

$$
H _ {\gamma} = - \frac {\hbar^ {2}}{2 \mathcal {I}} \frac {\partial^ {2}}{\partial \gamma^ {2}}, \tag {27}
$$

where $\mathcal { L }$ is the corresponding moment of inertia for this rotation. By performing partial integration twice for eq. (26), $h _ { K }$ is expressed by the product of the norm part and the ${ \frac { \hbar ^ { 2 } } { 2 \mathcal { T } } } K ^ { 2 }$ term. One then obtains the normalized contribution to the energy,

$$
E _ {K} = \frac {\hbar^ {2}}{2 \mathcal {I}} K ^ {2}. \tag {28}
$$

This is nothing but the kinetic rotational energy due to the rotation about the $z$ axis. As this energy increases as $K$ , the lowest state is of $K { = } 0$ . It is of interest that $K { = } 0$

![](images/3564922ba5f083941314941332c98046f29ff722e0243dde714058c063e724e1.jpg)  
Fig. 11 Schematic picture of proposed rotational bands built on the ground and Hoyle states of $^ { 1 2 } \mathbf { C }$ . Panel $\mathbf { a }$ is taken from [10] with permission. Panels $\mathbf { b }$ and $\mathbf { c }$ display, respectively, the rotation of the Hoyle and ground states (see text).

is favored both in the distant-object rotation and in the compact-object rotation [9]. In the latter, it is a consequence of the maximization of the binding energy, but in the former it arises in order to avoid rotational kinetic energy with $K > 0$ . In fact, by having $K { = } 0$ , all orientations about the $z$ axis are superposed with equal amplitudes, and the $K ^ { 2 }$ expectation value vanishes. This is a quantum realization of “stopped” ( $z$ axis) spinning. It is pointed out that the value of $\mathcal { T } ( > 0 )$ does not matter for the realization of $K { = } 0$ lowest band in the present scheme.

The rotational kinetic energy due to $K > 0$ (see eq. (28)) becomes higher with the present assignment of the $z$ axis than the corresponding energies with the $z$ - axes assigned otherwise, which implies that the lowest set of $K { = } 0$ states are better separated in energy from other states with $K > 0$ .

Figure 11 shows how rotational modes are created for the ground and Hoyle states. We start with the Hoyle band. Panel $\mathbf { b }$ indicates that the $K { = } 0$ projected intrinsic state enters the process, as discussed above. There are two other axes, $x$ and $y$ (see Fig. 8c). In the classical mechanics, the moment of inertia takes different values for the rotations about these axes. The motion is then considered to be very complicated. In quantum mechanics, the $K { = } 0$ projection comes in, which brings about a kind of averaging over the $x$ -axis and $y$ -axis rotations. This effect can be precisely incorporated by assessing energy kernels following the arguments in Subsect. 2.2 (or eventually [9]), but will be an elaborate work. Anyway, a simple formula like the one $\propto J ( J + 1 )$ arises in the quantum mechanical treatment, if the cluster localization is strong enough.

Putting such an elaborate calculation aside for the time being, we look into physics cases in a simpler manner. We here estimate the moment-of-inertia for the $y$ axis rotation and the $x$ axis rotation in Fig. 8c in a similar approximation used for $^ { 8 }$ Be in Subsect. 2.4. For the $y$ -axis rotation axis, the axis perpendicular to the paper plane of Fig. 5 is taken, and the positions of the center of gravity of each cluster are read from the figure. This is precise enough for the present purpose, similarly to the $^ 8$ Be case. Fig. 5d is used for this purpose, and the axis goes through the center of gravity of the whole nucleus. The calculated coefficient in front of $J ( J + 1 )$ is about 0.25 MeV. The other value of the moment of inertia is for the $x$ axis rotation, which corresponds to the rotation about the horizontal axis in the paper plane of Fig. 5. This axis goes through the cluster on the $x$ axis, yielding no contribution from this cluster. The calculated coefficient in front of $J ( J + 1 )$ is about 0.30 MeV.

The precise calculation can be performed with an appropriate Hamiltonian with a proper $| \phi \rangle$ or $| \Phi | \phi , K | \rangle$ . Such calculations are expected to provide results somewhere in between the corresponding values given by the present coefficient equal to 0.25 MeV or 0.30 MeV. This range generates the excitation energies of the $2 ^ { + }$ and $4 ^ { + }$ states in the Hoyle rotational band at 1.50-1.80 MeV and 5.0-6.0 MeV, respectively. The $J ( J + 1 )$ rule will be maintained well, but other mechanisms like accidental mixing with a nearby state may disturb this regularity. Far right part of Fig. 10 indicates that these values already depict quite interesting agreement with (possible) rotational levels observed in experiments [52, 53].

The ground band presents basically the same property (see Panel c). Because of faster convergence, the energies of the $0 _ { 1 } ^ { + }$ and $2 _ { 1 } ^ { + }$ states are calculated precisely enough by the MCSM calculations, which give a proper treatment of the $y$ - and $x$ -axis rotations. Namely, the elaborate calculation was feasible for these states, but infeasible for the Hoyle band due to the current computer resources.

In a comparison to the 8Be case in Subsect. 2.4, the difference of the observed $2 ^ { + }$ excitation energies between the 8Be band and the Hoyle band is as large as a factor of three. This agrees, to a good extent, with the present theoretical values: 0.80/0.25=3.2 and 0.80/0.30=2.67.

The Hoyle state is of great importance in the nucleosynthesis. The present discussion adds another fundamental significance to it as a showcase of the coexistence of dual rotational modes within the same nucleus: distant-object and compact-object rotations. This is so rare, and further investigations are of extreme importance.

# 2.6 Summary

In summary, the $\alpha$ -clustering is shown, in First-Principles no-core shell model calculations, to emerge, without assuming it a priori, as an effect of nuclear forces. This calculation, performed by the Monte Carlo Shell Model, reproduces various observed quantities. The $\alpha$ -clustering is shown to appear even in the well-bound ground state of $^ { 1 2 } \mathrm { C }$ , as a non-negligible component. Although, it is not a major component, this mixture lowers the energy of the ground state. In contrast to this, the $\alpha$ -clustering is virtually solo mechanism for the formation of the $^ 8$ Be ground state. The $\alpha$ -clustering remains the dominant mechanism for the Hoyle state, where about 2/3 probability

of the wave function, with proper superposition of basis vectors, is composed of $\alpha$ - like clustering. There are nuclear-matter components also in the Hoyle state, and it is of interest that the cluster and matter components are mixed repulsively, partly due to the orthogonality to the fully correlated ground state. This is another very interesting point, partly because the ground-state wave function is believed to be almost converged.

The clustering state is deformed, by definition; the density profile is not spherical in its intrinsic structure. As the deformed shape is connected to the rotational excitation, the clustering states are a very good testing ground of the theory of rotational excitations. The recently presented formulation comprising (i) fully quantum-mechanical derivation of “rotational” excitation energies, (ii) full inclusion of triaxiality as consequences of rotational symmetry and nuclear forces, (iii) practical conservation of $K$ quantum number in contrast to traditional belief, can be applied to clustering states. The same fundamental equation (eq. (16)) is used for the same picture that the intrinsic state pointing to all orientations are superposed properly according to the angular momentum of the state. The difference from the rotational excitation of ellipsoidal matter lies in the relevant parts of the Hamiltonian. For ellipsoidal matter cases, the nucleon-nucleon interactions produce the major contributions to the so-called rotational excitation energy. But, in the case of clustering states, each cluster is basically in eigenstates internally. What matters is the kinetic energy of the center of gravity of each cluster, which can be treated as a point mass. If the relative configuration of these centers of gravity is fixed (allowing quantum fluctuations), the whole system can be described as an intrinsic state to be projected on a given angular momentum (and parity). In this case, the origin of the “rotational” excitation energy is kinetic, and the same fundamental equation gives us the same energy formula as the one obtained from the quantization of free rigid-body with axial symmetry imposed, even for systems without axial symmetry thanks to the $K$ restoration. This $K$ quantum number is defined with the $z$ axis producing the smallest value of moment of inertia among three possible axes. Rigorously speaking, some of the discussions here may hold only in ideal cases such as perfect $\alpha$ cluster, but such approaches provide us with simple fundamental pictures, from which further understandings of more complicated cases may be developed. It is noted that the present formulation is completely different from and independent of pictures based on moving wave packet, which are quite problematical especially for rotational mode, in view of actual wave functions and also from standpoint of finite range of angles and periodic boundary condition. We definitely do not need them.

We presented the concept of dual rotational modes: the rotation of nuclear-matter ellipsoid is called compact-object rotation, whereas the rotation of clusters with fixed configuration is called distant-object rotation. We point out that the former occurs, if the range of interactions between constituents (e.g. nucleons for nucleus) and the size of the whole system (e.g. nuclear radius) are comparable. On the other hand, the latter occurs, if the clusters are separated enough and the clusters behave as eigenstates internally. The duality of rotational modes can be interpreted as an outcome of the clustering hierarchy [8], and remains visible despite sizable mixing of two hierarchies, as seen in 12C. It is of great interest to explore, experimentally or theoretically, any

physical systems exhibiting these features, including mixed/intermediate situations. In fact, the compact-object rotation is obviously rather special from the global viewpoint of entire physics, and might be one of the treasures of nuclear physics, unrecognized, at least openly, so far. The hadron spectroscopy can be a good candidate, where quark-gluon system can be compact but also can be spread like deuteron or neutron nuggets.

The $K { = } 0$ dominance in the lowest states of deformed systems can be applied to more complex systems. Although our arguments have been limited to positive-parity states, negative-parity states with clustering structure are very likely of $K { = } 0$ , which may be consistent with algebraic models for $\bot 2$ C [14]. This K=0 dominance seems to hold also for the lowest states with three-dimensional configurations/shapes like tetrahedron or $\alpha$ quartet, for instance, [58].

We further add two prospect subsections.

# 2.7 Prospects 1: Atomic molecules

It is evident that the present formulation extended to distant-object rotation can be applied to atomic molecules [59]. The discussions of $^ { \mathrm { ~ 8 ~ } }$ Be may be applied to the linearly configured structures of the O $^ 2$ and CO $^ 2$ molecules, for example. In the O $^ 2$ case, by putting O atoms at the red circles in Fig. 8b, the arguments for the $^ { 8 } \mathrm { { B e } }$ nucleus can generally be extended to the O $^ 2$ molecule.

The structure of the Hoyle state shows certain similarity to the structure of the $\mathrm { H _ { 2 } }$ O molecule; in Fig. 8c, H atoms can be put at the red circles at the top and the bottom, and O atom at the red circle in the middle. After the $K { = } 0$ projection, the rotational mode can be described with one rotational band on top of the ground state with the moment of inertia with the value between two classical ones obtained for two axes. It is really interesting how we can apply some of the arguments here to molecular structures, while certain approximations will be needed if norm and energy kernels are actually calculated.

# 2.8 Prospects 2: Fission

The dual rotational modes may have another completely different relevance. That is the nuclear fission [60]. Before fission, the nucleus may be deformed, and shows a compact-object rotation like many other heavy deformed nuclei. In the case of fast neutron capture, for instance, the nucleus gains a certain value of angular momentum. This angular momentum is conserved. After passing around scission point during the fission process, two fragments are formed, and their mutual rotation likely occurs. This mutual rotation should belong to distant-object rotation. For this distant-object rotation, excitation energies must be very low compared to compact-object rotation at the same angular momentum, and states may be quasi-degenerate, which is a favorable situation for a linear motion. If the nucleus gains a high value of the angular momentum at an initial stage of fission, this angular momentum is maintained. However, after scission point, the two fragments may start certain distant-object rotations, taking certain amount of angular momentum. As this mode has very low excitation energies

as compared to compact-object rotation, the nucleus may decay from its finite-angularmomentum state populated by fast neutron capture to a low-excitation-energy states of similar angular momenta. This means that a sizable energy may be released to neutron emission, with larger phase space. This mechanism may facilitate fission processes with neutron emission(s).

On the other hand, individual fission fragments likely generate own rotational modes, which are compact-object rotations. The angular momenta of distant-object rotation is then coupled with or transferred to those of such compact-object rotations. The interplay between the distant-object rotation and the compact-object rotation may thus occur in certain types of fission. As recently explored in [61], the time evolution of the angular-momentum distribution contains exciting open questions, and in such studies, the interplay between the compact-objet and the distant-object rotational modes can be an interesting aspect. It is mentioned that simultaneous emergence of compact-object and distant-object modes may result in spontaneous fission, as another interesting subject.

# 3 A review on cluster model approaches

# 3.1 Introduction

One of the enduring challenges of nuclear many-body physics is to elucidate how structures—such as clusters, phonon excitations, and shape changes—emerge from fundamental interactions among nucleons. As was discussed earlier, while considerable progress has been made by describing nuclei in terms of individual protons and neutrons, the phenomenon of nuclear clustering, emergence of cluster degrees of freedom, most notably $\alpha$ -like correlations, and their role in nuclear structure and dynamics remains not fully understood. Indeed, $\alpha$ -particle formation has been suggested since the early days of nuclear science as one of the guiding ideas behind observed decay modes and the unusual stability of certain nuclear configurations [62–64]. Many multi-cluster, molecular-like states in light nuclei appear near their respective cluster-decay thresholds—a feature succinctly illustrated in the well-known Ikeda diagram [5]—supporting the idea that alpha clusters serve as important building blocks for such states. A version of this diagram is shown in Fig. 12, highlighting the thresholds and pictorially illustrating cluster structures. Although threshold effects are known to restructure states, often helping to align structures to favor decay into corresponding thresholds [65], as shown in examples in Sec. 2 and further illustrated in this section and Sec. 3, clustering is not just a threshold phenomenon. Explicit $\alpha$ - particle clustering is closely related to pairing and quartet correlations in nuclei [66] and even in randomly interacting quantum many-body systems clusterization seems to naturally emerge [67], the mechanisms behind this remain to be fully explained.

Within this paradigm, the connection between the microscopic description of nuclear structure—based on nucleonic degrees of freedom and methods such as the nuclear shell model and, more broadly, configuration interaction—and clustering correlations, preformation, dynamics, and decay remains a central question. Historically, the two descriptions—one based on nucleonic degrees of freedom and the

![](images/c0b4662d076cd303f7698462d049cca6188b21d1c16ed52359b4827c4f6271e4.jpg)  
Fig. 12 Ikeda-style diagram illustrating clustering phenomena in light nuclei. The spectra of several light nuclei are shown along with illustrations of their potential clustering structures. Cluster decay thresholds are indicated with dashed lines, and decaying states are highlighted in red. For each state, the spin and parity are shown on the left, and the excitation energy is shown on the right. The total binding energy is indicated for the ground state. All energies are in units of MeV.

other on cluster degrees of freedom—have largely evolved in parallel. Nevertheless, the overlap between these parallel lines of thought has been growing. For example, antisymmetrized molecular dynamics has been extensively applied to the study of molecular-type states in clustered nuclei [68], incorporating both clusters and valence nucleons in a molecular-like structure, where valence nucleons mediate bonds between clusters.

Present-day advanced models employ fully microscopic descriptions based on nucleon-nucleon interactions and treat cluster dynamics microscopically using methods such as the Resonating Group Method (RGM) [69, 70], as well as modern configuration-interaction approaches like the Monte Carlo Shell Model discussed in Sec. 2. Furthermore, shell model calculations inspired by certain symmetry-based approaches, such as symplectic or SU(3) symmetries, have increasingly been able to capture key aspects of clustering [71–74]. Such symmetry-based methods are among the most promising present-day techniques [75, 76].

Microscopic calculations, such as those using Green’s Function Monte Carlo, have demonstrated the emergence of clustering in $^ 8$ Be directly from nucleon-nucleon (NN)

interactions [21]. This fundamental result has reignited modern, ab initio, theoretical interest in clustering. A variety of approaches—including mean-field models [77], lattice simulations [78, 79], large-scale ab initio no-core shell model calculations [20], and Bose-Einstein condensate wave studies functions [13, 80, 81]—have been employed to better understand how clusters form and which features of nuclear interactions and many-body dynamics favor the development of correlated substructures. Fully microscopic calculations that integrate nuclear structure and reactions from a configuration interaction perspective have also made significant progress [82–84]. A comprehensive list of references and historical discussions on the subject can be found in review [7].

The study of nuclear clustering is not only about emergent phenomena and the appearance of clustering degrees of freedom; it has become increasingly clear—supported by growing experimental evidence—that clustering plays a fundamental role in connecting nuclear structure and reactions. Clusters are predominantly observed near their corresponding decay thresholds, a pattern first noted by Ikeda [5] and subsequently confirmed by numerous experiments. The physics of open quantum systems have introduced a new perspective in clustering studies [85]. As mentioned earlier, the threshold for a given decay channel significantly impacts the restructuring of the many-body wave function along this channel. This is evident in the observation of cluster states near corresponding thresholds, as well as in the convenient placement of broad states near these thresholds. The effect can manifest in different ways—either enhancing clustering or, conversely, blocking certain decay channels, as seen in proton-decaying 11B, which inhibits the $\alpha$ -decay pathway [86, 87]. The near-threshold character of clustering makes many of these questions of paramount importance in astrophysics. The astrophysical significance of clustering is epitomized by the Hoyle state in $^ { 1 2 } \mathrm { C }$ [26, 27], whose triple- $\alpha$ nature is crucial for the nucleosynthetic pathway to heavier elements.

Furthermore, recent studies indicate that clustering can persist at high excitation energies and large angular momenta, sometimes in conjunction with rotational phenomena, all while embedded in the continuum of open decay channels [88–92]. This behavior may be driven by superradiance effects, leading to a separation of states into broad, strongly coupled, and structurally organized configurations that facilitate cluster decay, as well as narrow, trapped states [91]. Recent experimental results leveraging isospin symmetry have highlighted the distinct impact of the continuum on the realignment of wave functions toward clustering [65].

Advances in experimental techniques have significantly expanded the scope of clustering studies. The development of rare isotope beams has enabled novel studies of resonant reactions induced by radioactive nuclei. In particular, the Thick Target Inverse Kinematics (TTIK) approach [93] has proven to be a powerful tool for rarebeam experiments, facilitating the search for $\alpha$ -cluster states and systematic analysis of clustering strength distribution [65, 94–96, 96–101].

Against this backdrop, this section reviews how microscopic principles give rise to cluster substructures in light nuclei, with particular emphasis on the essential rosectionle of continuum coupling and reaction theory in shaping spectroscopic properties. In parallel with the discussion of the MCSM in Sec. 2, the framework presented here represents an alternative strategy within the broader configuration-interaction

approach. We approach clustering from the perspective of nucleonic degrees of freedom and nucleon-nucleon interactions, tracing its development from the traditional shell model into configuration interaction techniques that incorporate cluster configurations. In fact, the approach discussed here and that in Sec. 2 are fundamentally equivalent in their microscopic foundations, and in some examples employ identical Hamiltonians (e.g., JISP16), differing primarily in the strategy of configuration selection. They also offer complementary physical perspectives: a rotating intrinsic (body-fixed) frame in which clustering appears as spatially localized structures, versus the laboratory-frame picture adopted here, where clustering is characterized through overlaps and spectroscopic factors. The direction outlined here serves as a bridge between various other theoretical limits, including algebraic and symmetrybased methods, the resonating group method, the traditional shell model, the no-core shell model, and its continuum extensions.

In the following subsections of this section, we outline an alternative technique to that discussed in Sec. 2. Rather than identifying clusters from large-scale shell model solutions, we proceed in the opposite direction: we construct configurations starting from clusters and then mix them via configuration-interaction techniques with, albeit much smaller, traditional shell-model configurations of Slater determinants. In this way, we build what we call Cluster-Nucleon CI. We first present the details of this approach and then show applications, including the study of $\mathrm { ^ { 1 2 } C }$ , which reproduces the results discussed earlier while simultaneously bridging to the discussion in the final section, highlighting the competition between traditional shell-model configurations and cluster structures. We examine clustering in deeply bound and ground states, and briefly discuss the impact of the Pauli principle, as well as how four-nucleon correlations connect to physical $\alpha$ particles at larger distances. We conclude with the discussion of reactions, cluster resonances, and near-threshold clustering, which are addressed at the end of this section.

# 3.2 Cluster configurations

# 3.2.1 Center of mass and boosting

As in the standard shell model and no-core shell model approaches, we use the single-particle harmonic oscillator (HO) basis as the foundation of our configuration interaction (CI) framework:

$$
\langle \mathbf {r} | n \ell m \rangle = \phi_ {n \ell m} (r, \theta , \phi) = \frac {\phi_ {n \ell} (r)}{r} Y _ {\ell m} (\theta , \phi), \tag {29}
$$

where $n$ is the radial quantum number, $\ell$ the orbital angular momentum, and $m$ its projection. The HO potential is defined by frequency $\omega$ , we use $m$ for nucleon mass, the oscillator length $b = \sqrt { \hbar / m \omega }$ . The single-particle energy eigenvalues are

$$
E = \hbar \omega (N + 3 / 2), \quad N = 2 n + \ell . \tag {30}
$$

For explicit expressions and discussion of properties of HO wave functions, see e.g. [102].

Many-body wave functions are expressed as linear combinations of Slater determinants:

$$
| \Psi \rangle = \Psi^ {\dagger} | 0 \rangle = \sum_ {\{1, \dots , A \}} \langle 1, \dots , A | \Psi \rangle a _ {1} ^ {\dagger} \dots a _ {A} ^ {\dagger} | 0 \rangle , \tag {31}
$$

where $a _ { i } ^ { \dagger }$ creates a nucleon in a single-particle state labeled by HO quantum numbers and spin. The polymorphism between operators and states allows us to treat $\Psi ^ { \dagger }$ as a many-body creation operator acting on the vacuum. Pauli antisymmetry is ensured by fermionic commutation relations and operator ordering. Products of antisymmetrized states are written as

$$
\left| \mathcal {A} \left\{\Psi_ {\alpha} \Psi_ {\beta} \right\} \right\rangle = \Psi_ {\alpha} ^ {\dagger} \Psi_ {\beta} ^ {\dagger} | 0 \rangle . \tag {32}
$$

Unlike the traditional shell model, which relies on a predetermined basis, CI methods allow for flexible, on-demand construction of configurations. This generality enables efficient incorporation of physically relevant degrees of freedom, including symmetry-adapted or cluster-like configurations, the construction of those we discuss next.

The center-of-mass (CM) coordinate plays a crucial role in studies of clustering, where identifying and controlling the motion of cluster centers is essential. In traditional shell model calculations, the treatment of the CM has long been recognized as an important issue, particularly in ensuring translational invariance and in interpreting reaction channels. The use of the harmonic oscillator (HO) basis provides a powerful framework for addressing this problem, as it enables exact factorization of the CM degree of freedom due to the rich symmetry structure of many-body HO wave functions.

Following the no-core shell model approach [103], we exploit the symmetry of the many-body HO Hamiltonian, where energy eigenstates are degenerate with respect to the total number of oscillator quanta $N$ . States with fixed $N$ form representations of symmetry groups, including SU(3) and O(A), the latter of which enables exact CM separation in a truncated configuration space defined by a maximum excitation $N _ { \mathrm { m a x } }$ . For states with a given number of quanta

$$
N = N _ {\mathrm {C M}} + N ^ {\prime}. \tag {33}
$$

where $N _ { \mathrm { C M } }$ is the number of quanta in the CM excitation and $N ^ { \prime }$ is the number of quanta in the intrinsic wave function. In traditional applications, states of interest are those with $N _ { \mathrm { C M } } = 0$ , corresponding to a CM in the ground-state oscillator mode:

$$
\Psi = \phi_ {0 0 0} (\mathbf {R}) \Psi^ {\prime}, \tag {34}
$$

where $\mathbf { R }$ is the CM coordinate and $\Psi ^ { \prime }$ is the intrinsic wave function [104, 105].

For clustering studies, however, we require more general configurations in which the CM component can take any form. To achieve this, we construct CM-boosted states where the CM motion is expanded in terms of HO eigenfunctions with arbitrary quantum numbers.

$$
\Psi_ {n \ell m} = \phi_ {n \ell m} (\mathbf {R}) \Psi^ {\prime}, \tag {35}
$$

where $N _ { \mathrm { C M } } = 2 n + \ell$ defines the CM excitation. Although such CM-excited states naturally appear in full shell model diagonalizations—where they are typically regarded as spurious—our approach constructs them directly by acting on the CM coordinate. This CM boost procedure is significantly simpler and requires no additional diagonalization beyond the initial shell model solution [92].

To manipulate the CM motion, we use the standard CM creation and annihilation operators:

$$
\mathcal {B} _ {\mu} ^ {\dagger} = \frac {1}{\sqrt {2 A m \omega \hbar}} (A m \omega R _ {\mu} - i P _ {\mu}), \tag {36}
$$

$$
\mathcal {B} _ {\mu} = \frac {1}{\sqrt {2 A m \omega \hbar}} \left(A m \omega R _ {\mu} + i P _ {\mu}\right), \tag {37}
$$

which relate to the isoscalar E1 operator:

$$
D _ {\mu} = \sqrt {\frac {4 \pi}{3}} \sqrt {\frac {\hbar}{2 A m \omega}} \left(\mathcal {B} _ {\mu} ^ {\dagger} + \mathcal {B} _ {\mu}\right). \tag {38}
$$

Here, $R _ { \mu }$ represents the spherical component $\mu$ of the center-of-mass (CM) radius vector, and $P _ { \mu }$ is the corresponding component of the CM momentum.

The operator $B _ { m } ^ { \dagger }$ increases $N _ { \mathrm { C M } }$ by one and transforms as a vector. States with CM in a given state $( n , \ell , m )$ can be constructed recursively. Node number is increased via the scalar product:

$$
\mathcal {B} ^ {\dagger} \cdot \mathcal {B} ^ {\dagger} = \mathcal {B} _ {+ 1} ^ {\dagger} \mathcal {B} _ {- 1} ^ {\dagger} + \mathcal {B} _ {- 1} ^ {\dagger} \mathcal {B} _ {+ 1} ^ {\dagger} - \mathcal {B} _ {0} ^ {\dagger} \mathcal {B} _ {0} ^ {\dagger}, \tag {39}
$$

$$
\mathcal {B} ^ {\dagger} \cdot \mathcal {B} ^ {\dagger} \Psi_ {n \ell m} = \frac {1}{4} \sqrt {(2 n + 2) (2 n + 2 \ell + 3)} \Psi_ {n + 1, \ell , m}. \tag {40}
$$

Angular momentum $\ell$ is increased by acting on aligned states:

$$
\mathcal {B} _ {+ 1} ^ {\dagger} \Psi_ {n \ell \ell} = \sqrt {\frac {(\ell + 1) (2 n + 2 \ell + 3)}{4 (2 \ell + 3)}} \Psi_ {n, \ell + 1, \ell + 1}. \tag {41}
$$

The CM angular momentum operator is:

$$
\mathcal {L} _ {\pm} = \pm 4 \sqrt {2} \left(\mathcal {B} _ {0} ^ {\dagger} \mathcal {B} _ {\pm 1} - \mathcal {B} _ {\pm 1} ^ {\dagger} \mathcal {B} _ {0}\right), \tag {42}
$$

with action:

$$
\mathcal {L} _ {\pm} \Psi_ {n \ell m} = \sqrt {(\ell \mp m) (\ell \pm m + 1)} \Psi_ {n \ell , m \pm 1}. \tag {43}
$$

The boosted basis (35) generalizes the non-spurious form (34) and preserves translational invariance, as operations on the CM coordinate do not affect the intrinsic structure of $\Psi ^ { \prime }$ . A related discussion can be found in Refs. [72, 106, 107].

Next we comment on the structure of CM-boosted states and their connection to SU(3)-based models widely used in the literature [71, 72, 108, 109]. For simplicity, we focus on CM-boosted wave functions of $\alpha$ particles. The ground state of an $\alpha$ particle

is dominated by the fully symmetric $s ^ { 4 }$ configuration, which accounts for more than 90% of the wave function across a wide range of oscillator frequencies $\hbar \omega$ . Under the approximation that the $\alpha$ particle has this $s ^ { 4 }$ structure (equivalent to an $N _ { \mathrm { m a x } } = 0$ truncation), we recover the algebraic limit [71, 72, 109].

In this limit, where the internal excitation is zero ( $N ^ { \prime } = 0$ ), the CM-boosted wave function $\Psi _ { n \ell m }$ carries all oscillator quanta $N = 2 n + \ell$ in the CM motion. The spatial part is fully symmetric under particle exchange, and the SU(3) symmetry of the system is restricted to irreducible representations with $( \lambda , \mu ) = ( N , 0 )$ . The wave function can be expanded as:

$$
\Psi_ {n \ell m} = \sum_ {\eta} X _ {N} ^ {\eta} \Phi_ {(N, 0): \ell m} ^ {\eta}, \tag {44}
$$

where each term corresponds to a partition $\eta = \{ \alpha _ { i } , N _ { i } \}$ satisfying:

$$
A = \sum_ {i} \alpha_ {i}, \quad N = \sum_ {i} \alpha_ {i} N _ {i}. \tag {45}
$$

Here, $A$ is the total number of nucleons, $\alpha _ { i }$ is the number of particles in oscillator shell $_ i$ , and $N _ { i }$ the number of quanta associated with that shell.

The expansion coefficients $X _ { N } ^ { \prime \prime }$ , known as cluster coefficients [72, 108, 109], are given analytically by:

$$
X _ {N} ^ {\eta} = \sqrt {\frac {1}{4 ^ {N}} \cdot \frac {N !}{\prod_ {i} \left(N _ {i} !\right) ^ {\alpha_ {i}}} \cdot \frac {A !}{\prod_ {i} \alpha_ {i} !}}. \tag {46}
$$

The states $\Phi _ { ( N , 0 ) : \ell m } ^ { \eta }$ are SU(3)-symmetry states with SU(3) quantum numbers $( \lambda , \mu ) =$ $( N , 0 )$ ; such states are unique for each configuration.

This algebraic framework forms the basis of many SU(3)-based shell model studies of $\alpha$ clustering in nuclei [71, 72, 109]. The construction of CM-boosted wave functions via direct CM operations on intrinsic states, as employed in this work, reduces to the SU(3) expansion in the algebraic limit, thereby establishing a direct connection to these earlier models. However, since any intrinsic configuration $\Psi ^ { \prime }$ can serve as a starting point, the CM boosting approach is considerably more general applicable to clusters of any size and with realistic internal structure.

One notable limitation of the algebraic framework is the requirement to use the same HO frequency for all nuclei involved—such as the parent, daughter, and $\alpha$ particle in $\alpha$ decay—which can be problematic, as the optimal frequencies for these systems typically differ. While the CM boosting approach retains this frequency-matching constraint, the ability to represent the $\alpha$ particle in a more realistic basis, going beyond the $s ^ { 4 }$ configuration, helps to alleviate this issue.

In Fig. 13, to highlight the structure of the boosted wave function we illustrate the distribution of nucleons across oscillator shells in a CM-boosted wave function of an $s ^ { 4 }$ alpha particle, shown for different numbers of center-of-mass (CM) quanta. The structural content of a boosted state is presented in Tab. 1 two illustrative examples of an alpha-particle state boosted by 8 oscillator quanta, denoted as $\Psi _ { n = 4 , \ell = 0 } ^ { ( \alpha ) }$ n=4,ℓ=0. The left column corresponds to the alpha state described as $s ^ { 4 }$ ( $N _ { \mathrm { m a x } } = 0$ ) and agrees with

the result in (46). The right column shows the case with $N _ { \mathrm { m a x } } = 4$ wave function for the alpha particle calculated using JISP16 nucleon-nucleon interaction Hamiltonian [110] with oscillator basis frequency of $\hbar \omega = 2 0$ MeV.

![](images/06b4dc8cd75ae0297711424b6a7db72b336aa9e9f8445d9ff2a3731cff67103d.jpg)  
Fig. 13 Nucleonic occupation numbers across oscillator shells in a boosted wave function of an $_ { \alpha }$ particle, shown for different values of the center-of-mass (CM) excitation quanta. See ref. [111]

Table 1 Select configuration content of NCSM wave functions for $^ { 4 } \mathrm { H e }$ with $\hbar \Omega = 2 0$ MeV boosted by 8 quanta $L = 0$ ). This would correspond to a minimal number of quanta creating an alpha particle configuration within the $^ { s d }$ valence space.   

<table><tr><td>Configuration</td><td>Nmax=0</td><td>Nmax=4</td></tr><tr><td>(sd)4</td><td>0.038</td><td>0.035</td></tr><tr><td>(p)(sd)2(pf)1</td><td>0.308</td><td>0.282</td></tr><tr><td>(p)2(pf)2</td><td>0.103</td><td>0.094</td></tr><tr><td>(p)2(sd)1(sdg)1</td><td>0.154</td><td>0.141</td></tr><tr><td>(p)(sd)(sdg)(pfh)1</td><td>-</td><td>0.005</td></tr><tr><td>(p)(sd)(pf)1(sdg)1</td><td>-</td><td>0.009</td></tr></table>

# 3.2.2 Cluster channels

While the formalism is general and allows construction of configurations with multiple clusters it is instructive to concentrate on a two-body problem by considering clusters with $A _ { 1 }$ and $A _ { 2 }$ nucleons, which combine to form a system of $A = A _ { 1 } + A _ { 2 }$ . A reaction channel is defined as the asymptotic state of this two-cluster system, composed of wave functions $\Psi ^ { ( 1 ) }$ and $\Psi ^ { ( 2 ) }$ (obtained, for instance, from shell model or NCSM) and their relative motion specified by partial wave $\ell$ . In line with the standard Resonating Group Method (RGM) or Generator Coordinate Method [69, 70], we construct these channels from center-of-mass (CM) boosted fragments, Eq. (35). We construct the

basis states to expand the channel wave functions as follows:

$$
\Phi_ {n \ell m} = \mathcal {A} \left\{\phi_ {0 0 0} (\mathbf {R}) \phi_ {n \ell m} (\boldsymbol {\rho}) \Psi^ {\prime (1)} \Psi^ {\prime (2)} \right\}, \tag {47}
$$

where $\mathcal { A }$ ensures proper antisymmetrization among all nucleons. In this construction, we recouple the center-of-mass (CM) coordinates of the two clusters into an overall CM coordinate vector $\mathbf { R }$ and a relative coordinate : $\rho$

$$
\mathbf {R} = \frac {A _ {1} \mathbf {R} _ {1} + A _ {2} \mathbf {R} _ {2}}{A _ {1} + A _ {2}}, \quad \boldsymbol {\rho} = \mathbf {R} _ {1} - \mathbf {R} _ {2}. \tag {48}
$$

To incorporate these channel basis states within the configuration interaction (CI) approach, we focus exclusively on states whose overall CM motion is represented by the ground-state harmonic oscillator (HO) wave function $\phi _ { 0 0 0 } ( \mathbf { R } )$ , thus ensuring the states are non-spurious. The relative motion of the two clusters is described by an HO wave function characterized by the chosen quantum numbers $n , \ell , m$ .

Although expressed in cluster form, Eq. (47) remains a full many-body state that can be represented through Slater determinants (see Eq. (31)). The recoupling of the individual HO wave functions of fragments $A _ { 1 }$ and $A _ { 2 }$ into combined CM and relative HO wave functions is accomplished using Talmi–Moshinsky–Smirnov coefficients [112]:

$$
\Phi_ {n \ell} ^ {\dagger} = \sum_ {n _ {1} \ell_ {1}, n _ {2} \ell_ {2}} \mathcal {M} _ {n _ {1} \ell_ {1} n _ {2} \ell_ {2}} ^ {n \ell 0 0; \ell} \left[ \Psi_ {n _ {1} \ell_ {1}} ^ {\dagger} \times \Psi_ {n _ {2} \ell_ {2}} ^ {\dagger} \right] _ {\ell}. \tag {49}
$$

Here we omit the magnetic quantum number $m$ and interpret $\ell$ as a combined set of asymptotic quantum numbers. The recouping procedure of constructing a channel basis wave function is illustrated in Fig. 14

![](images/57d134c7f06f74901d9377769a2cd2f1aab0570dc2681d11701788fc55316175.jpg)  
Fig. 14 Illustration showing the construction of the channel basis wave function $\Phi _ { n \ell m }$ in (47)

The configurations described in Eq. (47) are obtained directly from existing solutions for the systems $A _ { 1 }$ and $A _ { 2 }$ and do not require additional diagonalizations. However, these states significantly enlarge the configuration interaction space, making this a powerful cluster-nucleon configuration interaction approach. The variety of

available configurations can be further increased by considering channels constructed from excited states of the nuclei. Extensions to multi-cluster systems are also feasible, although analogs of analytic Talmi–Moshinsky coefficients are generally unavailable due to multiple possible recouplings. In such cases, direct construction of channel states can be accomplished through alternative methods, including algebraic or numerical diagonalization of the relevant Casimir operators associated with the harmonic oscillator algebra.

The full cluster channel is described as a linear combinations of the basis states we defined in (47)

$$
\left| \Xi_ {\ell} \right\rangle = \sum_ {n} \chi_ {n} \left| \Phi_ {n \ell} \right\rangle . \tag {50}
$$

This effectively expresses the physical relative motion of two fragments (cluster plus core) in harmonic oscillator basis. The amplitudes $\chi _ { n }$ are obtained variationally within the Resonating Group Method (RGM) [70, 113], by solving a generalized eigenvalue problem involving Hamiltonian ( $\mathcal { H }$ ) and norm kernel ( $\mathcal { N }$ ):

$$
\sum_ {n ^ {\prime}} \mathcal {H} _ {n n ^ {\prime}} \chi_ {n ^ {\prime}} = E \sum_ {n ^ {\prime}} \mathcal {N} _ {n n ^ {\prime}} \chi_ {n ^ {\prime}}, \quad \mathcal {H} _ {n n ^ {\prime}} = \left\langle \Phi_ {n \ell} | H | \Phi_ {n ^ {\prime} \ell} \right\rangle , \quad \mathcal {N} _ {n n ^ {\prime}} = \left\langle \Phi_ {n \ell} | \Phi_ {n ^ {\prime} \ell} \right\rangle . \tag {51}
$$

Each solution $\{ \chi _ { n } \}$ is normalized via

$$
\sum_ {n, n ^ {\prime}} \chi_ {n} ^ {\star} \mathcal {N} _ {n n ^ {\prime}} \chi_ {n ^ {\prime}} = 1. \tag {52}
$$

Since the norm kernel $\mathcal { N }$ is positive definite, it admits a unique positive-definite square root. Thus, defining

$$
\tilde {\chi} _ {n} \equiv (\sqrt {\mathcal {N}} \chi) _ {n} = \sum_ {n ^ {\prime}} (\sqrt {\mathcal {N}}) _ {n n ^ {\prime}} \chi_ {n ^ {\prime}}, \tag {53}
$$

we obtain the normalized channel wave function

$$
\left| \tilde {\Xi} _ {\ell} \right\rangle = \sum_ {n} \tilde {\chi} _ {n} |, \Phi_ {n \ell} \rangle . \tag {54}
$$

Here, absorbing $\sqrt { \mathcal { N } }$ into $\chi$ converts Eq. (51) into a standard Hermitian eigenvalue problem. Consequently, the solutions $| \tilde { \Xi } _ { \ell } \rangle$ become orthonormal in the usual sense:

$$
\langle \tilde {\Xi} _ {\ell^ {\prime}} | \tilde {\Xi} _ {\ell} \rangle = \delta_ {\ell^ {\prime} \ell} \tag {55}
$$

the orthogonality among different eigenstates similarly follows from the Hermiticity of $\mathcal { N } ^ { - 1 / 2 } \mathcal { H } \mathcal { N } ^ { - 1 / 2 }$ .

# 3.3 Applications

# 3.3.1 Shell model studies of clustering spectroscopic factors

From the viewpoint of nuclear structure physics the level of clustering in any particular state can be assessed by a spectroscopic factor (SF), defined as the overlap between cluster channels (50) and shell-model states for a parent nucleus $\Psi ^ { ( A ) }$

$$
S _ {\ell} \equiv \left| \langle \Psi^ {(A)} | \Xi_ {\ell} \rangle \right| ^ {2}. \tag {56}
$$

Since the RGM equations in (51) have in general multiple solutions we can have SF into effectively different channels, which in traditional particle and potential problem would be characterized by a principal quantum number which represents the number of nodes in the wave function.

Historically, many studies of $p$ - and $s d$ -shell nuclei have been carried out within the traditional shell model with a core [71, 73, 108]. Despite its empirical nature, the traditional shell model remains one of the most successful and powerful predictive tools for describing a broad range of nuclear properties [114]. Even in the era of advanced computing and expanding ab initio calculations, it continues to play a critical role in bridging fundamental theory and experimental observations. By simplifying the complex nuclear many-body problem, the shell model helps pinpoint and explain a variety of emergent phenomena, including quartet and clustering correlations [66].

Multiple recent studies, fueled by experimental efforts, have been carried out in the mass region bridging the and $s d$ shells. In particular, advancements in TTIK $p$ methods have invigorated this field by systematically investigating clustering above the $\alpha$ -decay threshold [88, 94–96, 96–100, 115]. Recent systematic studies and comparisons with experiment affirm the applicability of the presented approach. However, owing to the inherent limitations of the traditional shell model and its effective nature, many results remain qualitative. In particular, understanding the effective operators involved in four-nucleon (i.e., $\alpha$ -particle) removal requires additional phenomenological adjustments.

Next, we consider several shell-model applications. Let us first focus on low-lying states, where the configuration space is restricted to a single oscillator shell. As a result, the entire cluster spectroscopy is limited to an effective operator within that shell. In an HO basis, this translates to a single $\Phi _ { n \ell }$ contributing a non-zero overlap in evaluating the spectroscopic factor:

$$
S _ {\ell} \approx | \chi_ {n} | ^ {2} \left| \langle \Psi^ {(A)} | \Phi_ {n \ell} \rangle \right| ^ {2}. \tag {57}
$$

Within this limit, it is natural to assume all basis states are decoupled, leading to diagonal RGM equations and hence $\chi _ { n } = 1$ . Conservation of oscillator quanta enforces this condition, as exploited in analytic studies [116–119].

Figure 15 shows the evaluation of $\alpha$ clustering in $N = Z$ , $s d$ -shell nuclei for groundstate-to-ground-state transitions, where $\ell \ = \ 0$ and $n \ = \ 4$ . The dashed black line presents spectroscopic factors calculated via Eq. (57) with $\chi _ { n } = 1$ (labeled as $S ^ { ( \mathrm { o l d } ) }$ ). These values lie an order of magnitude below experimental data and fail to reproduce

the observed trend of peaking at the beginning and end of the shell while dipping in the middle. This discrepancy is unsurprising, since an $\alpha$ particle boosted by eight quanta into the $s d$ shell contains only a 4% $( s d ) ^ { 4 }$ component, as indicated in Table 1. The issue has prompted significant discussion and highlights the need to renormalize the spectroscopic factors.

A frequently used approach is to adopt the Orthogonality Conditions Model (OCM) spectroscopic factors [108, 120, 121]. Given that the channel wave function’s normalization in the limited shell-model space is so small, renormalizing it to unity is a natural choice, thereby establishing a sum rule for the SF in a given channel. Formally, one can argue that the proper RGM solution in an orthonormal basis corresponds to $\ddot { \chi } _ { n } = 1$ , and in a diagonal scenario this defines the SM cluster channel as

$$
\left| \Xi_ {\ell} \right\rangle = \frac {1}{\sqrt {\langle \Phi_ {n \ell} \mid \Phi_ {n \ell} \rangle}} \left| \Phi_ {n \ell} \right\rangle . \tag {58}
$$

It is important to emphasize that while Pauli blocking and the projection onto a limited valence space are related, they are distinct reasons for renormalization. Consequently, in OCM the projection onto the valence space is included in the normalization overlap. The spectroscopic factors computed with this renormalization are referred to as $S _ { \ell } ^ { ( \mathrm { o c m ) } }$ in Fig. 15, and they reproduce both the experimental data and its trend more accurately.

Recent experimental studies [98] have tentatively identified the first limitations of the OCM method, noting that the procedure fails when the normalization due to Pauli blocking becomes extremely small, although further analysis is needed.

These results confirm strong clustering in the ground states of well-bound light nuclei. However, in these cases, the connection between a free $\alpha$ particle and one embedded in the nuclear medium is complex. This is evident from the direct overlaps between the $\alpha$ particle and the state being very small $S ^ { ( \mathrm { o l d } ) } )$ . Yet, when the reaction channel is properly reconstructed, the resulting measured OCM spectroscopic factor is large (see Fig. 15). We will further focus on this complex interplay between the traditional nucleon–nucleon shell-model picture and cluster configurations in the discussion of $\mathrm { ^ { 1 2 } C }$ and $^ 8$ Be in this and the following section.

# 3.3.2 Alpha cluster resonances

While some clustered states, such as those in $^ 8$ Be, have been known for decades, recent advances in experimental techniques and detailed analyses of scattering spectra have revealed numerous strongly clustered states in many nuclei (see reviews in Refs. [7, 124] and systematic investigations in Refs. [88, 94–96, 96–100, 115]). The strength of clustering is often gauged by comparing the observed $\alpha$ -decay width to the so-called Wigner limit, which represents the maximum possible width for an $\alpha$ particle in a potential model at the experimentally observed energy. Figure 16 illustrates a selection of these strongly clustered states across various light nuclei.

Discussions of $\alpha$ clustering that now includes $N \neq Z$ nuclei, and the influence of valence particles or holes on high-lying cluster states, have been guided by experimental data and theoretical SF evaluations [Eqs. (56) and (58)]. In contrast to older, more

![](images/0f1de19ebcafad40c826323d3807b47db1ad27fdc08039c3f2b90aca8a231876.jpg)  
Fig. 15 Spectroscopic factors for ground-state $_ \alpha$ transitions, $A \to ( A - 4 ) + \alpha$ , in $^ { s d }$ -valence $N =$ $Z$ nuclei. Scattered points are experimental data from knockout and pickup reactions [74, 122]. Connected points show theoretical results using the USDB Hamiltonian [123], with the $_ { \alpha }$ -particle wave function taken from an NCSM calculation (JISP16, $\hbar \omega = 1 4$ MeV) at the indicated $N _ { \mathrm { m a x } }$ . The dashed (black) line depicts the traditional shell-model spectroscopic factors [Eq. (57)] with $\chi = 1$ , while the solid (red) and dotted (blue) lines show OCM spectroscopic factors. See also ref. [111]

restrictive approaches, novel cross-shell effective Hamiltonians now enable significant progress toward a microscopic understanding of clustering in highly excited states and distribution of clustering strength. In particular, the recently developed FSU shellmodel Hamiltonian [125, 126], designed for cross-shell particle-hole excitations, has proven invaluable for explaining seemingly excessive experimental clustering strength.

As an example, we highlight the $\ell = 0$ and $\ell = 1$ channels in $^ { 2 0 }$ Ne and $^ { 1 9 }$ F, which are also included in Fig. 16 as analyzed in Ref. [101]. Selected results appear in Tables 2 and 3, although many other non-clustered states—accurately reproduced by the shell model—are omitted here for brevity. Many additonal studies, including those of rotational bands, connection with already mentioned SU(3) symmetry [127] as well as the emergence of rotational bands such as one seen in 20Ne can be found in Ref. [111].

Beyond general theory-experiment comparisons, these studies emphasize the impact of an extra nucleon degree of freedom, as seen by comparing $^ { 1 5 }$ N+α and $^ { 1 6 }$ O+α decay channels in 19F and $^ { 2 0 }$ Ne. In $^ { 1 9 }$ F, lower-lying states couple to an $n = 3$ channel that is unavailable in $^ { 2 0 }$ Ne due to Pauli blocking; these are low-lying, below-threshold states, and are hence inaccessible to $\alpha$ -scattering experiments. Meanwhile, in the $\ell = 0$

channel, the 6.540 MeV $1 / 2 ^ { - }$ state in $^ { 1 9 } \mathrm { F }$ mirrors the 6.725 MeV $0 ^ { + }$ state in $^ { 2 0 }$ Ne, both involving an $\alpha$ particle in an $n = 4$ radial mode. For $\ell = 1$ , the 5.79 MeV $1 ^ { - }$ resonance in $^ { 2 0 }$ Ne couples to the $n = 4$ channel, and higher-lying $n = 4$ clustered states are likewise identified in $\mathrm { ^ { 1 9 } F }$ as the spin-orbit partners $1 / 2 ^ { + }$ (5.333 MeV) and $3 / 2 ^ { + }$ (5.488 MeV), see Fig. 16.

![](images/fca89c4b8c781b28f3b2f8b4f031bf613a0ab84af7f1af20b36828f3781599c4.jpg)  
Fig. 16 Selected $_ { \alpha }$ -clustered states in several light nuclei, with $_ { \alpha }$ -decay thresholds indicated by dashed lines. Above the thresholds the resonances are broadened reflecting their width. The case of $^ { 2 0 }$ Ne and 19F, including spin-orbit partners for the $\ell = 1$ channel, is also shown.

Although the shell model accurately reproduces many observed features, certain highly excited states remain challenging. For instance, the very broad $0 _ { 4 } ^ { + }$ state in $^ { 2 0 }$ Ne—likely involving an $n = 6$ channel—has a small calculated SF, raising questions about its apparent lack of collectivity in theory. In general, strong clustering appears to emerge from the “collectivization” of cross-shell excitations, in the region of energy where states of a new $\hbar \omega$ structure first appear and exhibit enhanced near-threshold strength for each new RGM channel. The mixing across different particle-hole configurations seems to be suppressed in clustered states. However, this phenomenon remains under active investigation. Moreover, the super-radiance effect [91], which seems to drive the collectivization of states deeply embedded in the reaction continuum, has been experimentally observed to play an important role in realigning the wave functions [94, 101].

Table 2 Lowest states coupled to $\ell = 0$ and $\ell = 1$ clustering channels in $^ { 2 0 } \mathrm { N e }$ for the $^ { 1 6 } \mathrm { O } { + \alpha }$ Columns identify state, theoretical excitation energy, number of nodes in the alpha channel, experimental energy, experimental alpha reduced width. The labels in the second row “th” or “exp” refer to results coming from theory and experiment, respectively. Correspondence between data from theory and experiment represent a suggested assignment. The data is from ref. [101]   

<table><tr><td>\( J_{i}^{\pi} \)th</td><td>E(MeV)th</td><td>nth</td><td>\( SF_{\alpha} \)th</td><td>E(MeV)exp</td><td>\( \gamma_{\alpha} \)exp</td></tr><tr><td>\( 0_{1}^{+} \)</td><td>0</td><td>4</td><td>0.755</td><td>0</td><td></td></tr><tr><td>\( 0_{2}^{+} \)</td><td>6.698</td><td>4</td><td>0.143</td><td>6.725</td><td>0.47</td></tr><tr><td>\( 0_{3}^{+} \)</td><td>7.547</td><td>5</td><td>0.007</td><td>7.191</td><td>0.017</td></tr><tr><td>\( 0_{4}^{+} \)</td><td>10.121</td><td>6</td><td>0</td><td>8.7</td><td>broad</td></tr><tr><td>\( 0_{8}^{+} \)</td><td>13.521</td><td>5</td><td>0.246</td><td></td><td></td></tr><tr><td>\( 1_{1}^{-} \)</td><td>6.982</td><td>4</td><td>0.381</td><td>5.79</td><td>1.4</td></tr><tr><td>\( 1_{2}^{-} \)</td><td>7.918</td><td>4</td><td>0.379</td><td>8.708</td><td></td></tr></table>

Table 3 Lowest $\ell = 0$ and $\ell = 1$ states in $^ { 1 9 } \mathrm { F }$ , viewed as $^ { 1 5 } \mathrm { N } + \alpha$ channels. Columns are analogous to Table 2.   

<table><tr><td>\( J_i^\pi \)</td><td>E(MeV)</td><td>n</td><td>SFα</td><td>E(MeV)</td><td>γα</td></tr><tr><td>th</td><td>th</td><td>th</td><td>th</td><td>exp</td><td>exp</td></tr><tr><td>1/21-</td><td>0.468</td><td>4</td><td>0.706</td><td>0.110</td><td></td></tr><tr><td>1/22-</td><td>6.900</td><td>4</td><td>0.020</td><td>(6.095)</td><td></td></tr><tr><td>1/23-</td><td>7.092</td><td>4</td><td>0.041</td><td>7.048</td><td>0.12</td></tr><tr><td>1/25-</td><td>7.856</td><td>4</td><td>0.101</td><td>6.540*</td><td>0.53</td></tr><tr><td>1/21+</td><td>0.000</td><td>3</td><td>0.874</td><td>0.000</td><td></td></tr><tr><td>1/22+</td><td>6.060</td><td>4</td><td>0.311</td><td>5.333*</td><td>1.16</td></tr><tr><td>3/21+</td><td>1.770</td><td>3</td><td>0.672</td><td>1.554</td><td></td></tr><tr><td>3/24+</td><td>6.937</td><td>4</td><td>0.633</td><td>5.488*</td><td>0.98</td></tr></table>

# 3.3.3 Cluster Nucleon Configuraiton Interaction

Going beyond the analysis of spectroscopic factors discussed in the previous subsections, we next apply the Cluster Nucleon Configuration Interaction (CNCIM) approach to $^ { 2 1 }$ Ne as a simple illustration, demonstrating that a drastically reduced channel basis can still reproduce key features of a full shell-model (SM) calculation. This offers a powerful extension to the traditional shell model, especially in cases where full diagonalization is not feasible. We treat $^ { 2 0 }$ Ne as a $^ { 1 6 }$ O core plus $\alpha$ system, then add a neutron in the $d _ { 5 / 2 }$ orbital. Concretely, we place an $\alpha$ particle with relative angular momentum $L = 0 , 2 , 4 , 6$ onto $^ { 1 6 } \mathrm { O }$ and couple with the extra neutron, yielding 18 channel basis states—compared with 1935 many-body states in the full sd SM space.

In this reduced, non-orthogonal basis, we compute the Hamiltonian kernel using the USDB interaction [123] and solve it via the Resonating Group Method (RGM). Figure 17 shows the resulting low-lying spectrum, alongside the full USDB calculation and experimental data. Ground states indicate total binding; energies of other levels are shown relative to the ground state. The main spectral features and excitation energies are well reproduced, although we note that simple RGM model underbinds by about 3.5 MeV compared to the full diagonalization.

Figure 17 also includes a first column that lists the diagonal energies of the RGM basis states, $\langle \Xi _ { J L } | H | \Xi _ { J L } \rangle$ , where total angular momentum $J$ couples $L$ with the unpaired neutron ( $j = 5 / 2$ ). The RGM solution clarifies the mixing of partial waves; for example, two $5 / 2 ^ { + }$ states with $L = 0$ and $L = 4$ at 1.04 and 2.89 MeV in the first column undergo two-state mixing and repel each other. This implies that the first excited $5 / 2 ^ { + }$ state in $^ { 2 1 }$ Ne is a mixture of $L = 0$ and $L = 4$ , excluding $L = 2$ — a fact confirmed experimentally [128]. Further details of this study including matrix elements of the Hamiltonian and the norm kernel can be found in [107]

# 3.3.4 Cluster relative motion

Next, we move our discussion to clustering aspects in ab initio no-core applications of shell-model (SM) methods. We begin with the nucleus $^ 8$ Be, which, with its $\alpha + \alpha$ structure, has long served as a benchmark for nuclear clustering studies [21, 79, 109, 129–132].

Table 4 presents both experimental and theoretical energies/widths for the $0 ^ { + }$ , $2 ^ { + }$ , and $4 ^ { + }$ cluster resonances, each interpreted as two $\alpha$ particles with relative angular momenta $\ell = 0 , 2 , 4$ . A treatment based on the Resonating Group Method (RGM), which effectively employs a cluster-configuration-interaction (CI) approach with up to 12 basis channel states, in contrast to a full many-body expansion that would be prohibitively large. Here JISP16 [32, 110] interaction with $\hbar \omega = 2 5$ MeV is used.

A key signature of rotational two-alpha dynamics is the ratio $\mathrm { R } _ { 4 2 }$ of $4 ^ { + }$ to $2 ^ { + }$ excitation energies, which is found to be about 3.5—close to the $\mathrm { R } _ { 4 2 } = 3 . 3$ expected from a rotational band. This result, arising from a very different scattering perspective, is in quantitative agreement with our earlier rotation-based formulation in Sec. 2.4. Figure 18 shows the radial wave function for the $0 ^ { + }$ channel,

$$
u _ {\ell} (\rho) = \sum_ {n} \chi_ {n} \phi_ {n \ell} (\rho), \tag {59}
$$

![](images/97eca2204f6f4e90742d35edc739ddb4d610d7593c02787c3c6cb0769afc9d33.jpg)  
Fig. 17 Diagonal energies in the channel basis, low-lying states in RGM solution, full USDB and experimental spectra of $^ { 2 1 }$ Ne, see Ref. [111]

illustrating the effect of different harmonic-oscillator parameters $\hbar \omega$ . Beyond the spatial size of each $\alpha$ cluster, $u _ { \ell } ( \rho )$ describes the relative motion of the two $\alpha$ particles and can be matched to external Coulomb wave functions allowing to study asymptotic normalization and decay widths.

The decay widths in Table 4 are extracted using the standard $R$ -matrix approach [133],

$$
\Gamma_ {\ell} = \frac {\hbar^ {2} k}{\mu} \frac {\rho_ {c} ^ {2} u _ {\ell} ^ {2} \left(\rho_ {c}\right)}{F _ {\ell} ^ {2} (\eta , k \rho_ {c}) + G _ {\ell} ^ {2} (\eta , k \rho_ {c})}, \tag {60}
$$

by matching the interior wave function to the asymptotic solution at $\rho _ { c } = 3 . 6 \mathrm { f m }$ . Beyond the range of the nuclear potential, the result is not sensitive to the exact matching point; however, in a restricted HO basis, this issue must be treated with care. The chosen matching location maximizes the outgoing flux while minimizing sensitivity to the matching point. This study simultaneously reproduces the nearlybound $0 ^ { + }$ ground state ( $\Gamma = 5 . 6 \mathrm { e V }$ ) and the broad $4 ^ { + }$ resonance, highlighting the effectiveness of the cluster-based RGM approach.

To conclude this discussion, we pause on Fig. 18, which highlights that the 8Be ground state is a long-lived state of two $\alpha$ particles, with a resonant wave function suggesting that the two $\alpha$ particles move around each other with an average separation of about 3.5 fm, as can be inferred from the figure. This result is also obtained from a different perspective in Sec. 4.

Table 4 Experimental and RGM results for 8Be with the JISP16 interaction, allowing up to 12 HO quanta in each ℓ channel. Energies and widths are given in MeV except for those marked with $^ *$ (in eV).   

<table><tr><td>l</td><td>Ex</td><td>Γ</td><td>(RGM)ex</td><td>Γ(RGM)</td><td>S</td></tr><tr><td>0</td><td>0.0</td><td>5.6*</td><td>0.0</td><td>8.9*</td><td>0.69</td></tr><tr><td>2</td><td>3.0</td><td>1.5</td><td>4.6</td><td>1.4</td><td>0.66</td></tr><tr><td>4</td><td>11.4</td><td>3.5</td><td>16.0</td><td>2.7</td><td>0.51</td></tr></table>

![](images/748b77c977c2ad4428bb52b8a11fa396c422600b542a37b12437a9f8146fbf0e.jpg)  
Fig. 18 Relative $\alpha + \alpha$ wave function for the $0 ^ { + }$ RGM channel in $^ { 8 }$ Be, computed using the JISP16 interaction. Different curves correspond to various values of $\hbar \omega$ .

# 3.3.5 Hoyle state

One important future direction of the method is its extension to multi cluster problems. In this context, $^ { 1 2 } ($ , including both its ground state and the Hoyle state, occupies a central role in this review, as it is examined across this section and Secs. 2 and 4, consistently revealing the same underlying physics from complementary perspectives. A classic example is the Hoyle state in $\mathrm { ^ { 1 2 } C }$ , which has been studied in various approaches [14, 78, 134].

The Hoyle state, an excited $0 ^ { + }$ state just 285 keV above the triple-alpha threshold, decays almost exclusively via an intermediate $^ { 8 }$ Be resonance, itself only 93 keV above the two-alpha threshold [135–138]. This sequential decay path, in addition to being favored by Coulomb dynamics, highlights important structural features of the threealpha configuration. A first application of the method to this problem is presented in Ref. [111], and we summarize it below.

While no direct analytic method analogous to Moshinsky coefficients exists for the three-cluster case, the channels can be constructed through a sequential coupling of Jacobi coordinates. In the present calculation, up to $N _ { \mathrm { m a x } } = 1 2$ oscillator quanta are distributed among the two relative coordinates. The RGM framework is applied to a system of three identical $\alpha$ particles, each in an $s ^ { 4 }$ configuration, using the JISP16 interaction with $\hbar \omega = 2 5$ MeV. The minimal configuration allowed by the Pauli principle corresponds to $N = 8$ , representing a filled 0s shell with eight nucleons occupying the $0 p$ shell.

Table 5 Excitation energies (in MeV) for rotational band members in $^ { 1 2 } \mathrm { C }$ : experimental data, NCSM results, and RGM results (both with $\hbar \omega = 2 5 ~ \mathrm { M e V }$ ), along with spectroscopic factors $S _ { \ell }$ for triple-alpha decay.   

<table><tr><td>Jπ</td><td>E(exp)ex</td><td>E(NCSM)ex</td><td>E(RGM)ex</td><td>SL</td></tr><tr><td>0+</td><td>0</td><td>0</td><td>0</td><td>0.42</td></tr><tr><td>2+</td><td>4.4</td><td>6.06</td><td>3.61</td><td>0.49</td></tr><tr><td>4+</td><td>14.1</td><td>19.8</td><td>13.6</td><td>0.60</td></tr></table>

As seen in Table 5, the RGM and NCSM results both suggest significant clustering in the lowest $0 ^ { + }$ , $2 ^ { + }$ , and $4 ^ { + }$ states. While the NCSM is not ideally suited to describe the Hoyle state, the triple-alpha spectroscopic factor $S ( 0 _ { 2 } ^ { + } ) = 0 . 2 5 7$ is reasonable. Furthermore, the squared overlap of the triple-alpha channel ( $J ^ { \pi } = 0 ^ { + }$ ) with a twofragment channel consisting of the 8Be ground state ( $N _ { \mathrm { m a x } } = 4$ ) and an $\alpha$ in relative motion with $n = 2$ , $\ell = 0$ , is 0.51. This large overlap supports the dominance of the sequential decay mechanism through 8Be.

These results essentially reiterate the findings from the MCSM in Sec. 2. The states listed in Table 5 are members of the ground-state band seen in Fig. 4. While here we do not project onto the intrinsic frame to pictorially display the density profile of a rotating three- $\alpha$ system as in Fig. 5, we instead infer this structure from the energies of states that form a rotational band, from quadrupole moments that can be shown to

follow rotor-model systematics, and from the consistency of the spectroscopic factors $S _ { \ell }$ in the last column of Table 5. The gradual increase of $S _ { \ell }$ with angular momentum highlights the role of rotational motion, which slightly deforms the two- $\alpha$ configuration and increases their separation, thereby explaining the growth of $S _ { \ell }$ .

Our numerical results for the spectroscopic factors discussed above show that both the ground state and the Hoyle state couple to the same lowest asymptotic three- $\alpha$ channel. This channel is open for the Hoyle state but closed for the ground state, highlighting the mixing discussed in Fig. 3. Furthermore, this channel couples strongly to the $^ { 8 } \mathrm { B e } + \alpha$ configuration, placing the qualitative picture shown in Fig. 3 on a quantitative footing.

# 3.3.6 Scattering problem

Having established a cluster-based framework for spectroscopy of bound and weakly bound states, we now illustrate its extension to scattering. In particular, $\alpha + \alpha$ scattering serves as an instructive example for studying resonances and continuum dynamics in light nuclei.

Unlike the case of deeply bound states, the HO expansion is a poor choice for weakly bound and scattering states because of spatially extended nature of the wave functions. However, the analytic form of the basis functions remedies this issue. The J-matrix method, Ref. [139], also known as the Harmonic Oscillator Representation of Scattering Equations (HORSE) [140, 141], has been extensively discussed in the literature [139]. In its traditional form, which we discuss here, the method is limited to the case where remotely the Hamiltonian matrix is represented just by the kinetic energy operator. The Coulomb problem presents a significant challenge for the standard Jmatrix/HORSE method, but the method can be appropriately modified, as discussed in Refs. [107, 140, 141].

The integer $n$ in Eq. (59), which enumerates the basis states, coincides with the number of nodes in the radial part of the wave function. The method relies on the asymptotic limit $r  \infty$ in coordinate space being equivalent to the configurationspace limit $n \to \infty$ , with the approximate correspondence

$$
r = \sqrt {\frac {\hbar}{m \omega} (2 n + \ell + 3 / 2)}. \tag {61}
$$

Thus, the RGM solution (50), expressed in radial form (59) needs to be matched with the asymptotic solution for the free-space Hamiltonian, such that the asymptotic behavior is expressed as

$$
\chi_ {n} \simeq \alpha F _ {n \ell} + \beta G _ {n \ell}, \tag {62}
$$

where $F _ { n \ell }$ and $G _ { n \ell }$ represent the regular and irregular solutions for the free-space Hamiltonian (which are Coulomb or Bessel functions), expanded in the HO basis; see Ref. [142].

The central idea, describing the J-matrix (or HORSE) method [139–141], is represented by the following equation, showing the structure of the RGM matrix:

$$
\left( \begin{array}{c c c c} \hline \mathcal {H} _ {0 0} & \dots & \mathcal {H} _ {0 n} & 0 \\ \vdots & \ddots & \vdots & 0 \\ \mathcal {H} _ {n 0} & \dots & \mathcal {H} _ {n n} & T _ {n n + 1} \\ \hline 0 & 0 & T _ {n + 1 n} & T _ {n + 1 n + 1} \\ \vdots & 0 & 0 & T _ {\dots} \\ 0 & \dots & 0 & 0 \end{array} \right) \left( \begin{array}{c} \chi_ {0} \\ \vdots \\ \chi_ {n} \\ \chi_ {n + 1} \\ \chi_ {n + 2} \\ \vdots \end{array} \right) = E \left( \begin{array}{c c c c c c} \hline \mathcal {N} _ {0 0} & \dots & \mathcal {N} _ {0 n} & 0 & \dots & 0 \\ \vdots & \ddots & \dots & 0 & 0 & \vdots \\ \mathcal {N} _ {n 0} & \dots & \mathcal {N} _ {n n} & 0 & 0 & 0 \\ \hline 0 & 0 & 0 & 1 & 0 & \vdots \\ \vdots & 0 & 0 & 0 & 1 & 0 \\ 0 & \dots & 0 & \dots & 0 & \ddots \end{array} \right) \left( \begin{array}{c} \chi_ {0} \\ \vdots \\ \chi_ {n} \\ \chi_ {n + 1} \\ \chi_ {n + 2} \\ \vdots \end{array} \right) \tag {63}
$$

At the core of the method is an approximation that assumes the Hamiltonian and norm kernels in Eq. (51) are range-limited in configuration space up to some maximum value $n$ , related to the radial distance $r$ as described in Eq. (61). The upper-left blocks in (63), spanning from 0 to $n$ nodes, is computed exactly, let us call this space $\mathcal { P }$ and denote matrices and vectors restricted to this subspace with superscript $\mathcal { P }$ . Beyond this point, an asymptotic form is assumed: the norm kernel becomes the identity matrix, and the Hamiltonian kernel is given by the kinetic energy operator, represented by the lower-right blocks on both sides of equation (63). The solution, starting from $\xi _ { n }$ , is matched to the asymptotic form given in Eq. (62).

Here, $E$ denotes the continuous scattering energy. In the asymptotic region, the kinetic energy Hamiltonian in the harmonic oscillator basis is represented by a tridiagonal matrix. Consequently, only a single matrix element, $T _ { n n + 1 }$ , connects the two blocks (or spaces).

$$
\sum_ {m = 0} ^ {m = n} \left(E \mathcal {N} _ {n m} - \mathcal {H} _ {n m}\right) \chi_ {m} = T _ {n n + 1} \chi_ {n + 1}, \tag {64}
$$

Relating $\xi _ { n }$ and $\xi _ { n + 1 }$ and writing them both in the asymptotic form, we obtain

$$
\alpha F _ {n \ell} + \beta G _ {n \ell} = \left(\frac {1}{E \mathcal {N} ^ {(\mathcal {P})} - \mathcal {H} ^ {(\mathcal {P})}}\right) _ {n n} T _ {n n + 1} \left(\alpha F _ {n + 1 \ell} + \beta G _ {n + 1 \ell}\right), \tag {65}
$$

where the first term on the right is the $_ { n }$ th diagonal element of the inverse matrix. This relation allows one to determine the ratio $\beta / \alpha$ , which in turn determines the scattering phase shift at energy $E$ .

Figure 19 shows the $\ell = 2$ ( $D$ -wave) phase shifts for $\alpha + \alpha$ scattering. The solid line corresponds to the phase shift obtained using this method with HO truncation up to $N = 1 2$ quanta. Once the threshold is adjusted to the experimental $Q$ value, the agreement with data [143] is quite good.

The scattering phase shift presented here constitutes a direct experimental observable associated with the $2 ^ { + }$ state in 8Be, which is also discussed in Table 4. This provides strong experimental support for the validity of these results and for their interpretation in terms of clustering, as developed in this section and in Secs. 2 and 4.

![](images/18a0c8135e101c76fe61b955d1904a7d206b37f4634ee8e857318d9c6d9267bf.jpg)  
Fig. 19 (Color online) Phase shifts for $\alpha + \alpha$ scattering in the $\ell = 2$ channel. Experimental data are from Ref. [143], while the line shows RGM theoretical results, for further details see Ref. [111]

# 4 Cluster-shell competition and its modeling

One of the most intriguing features of nuclear structure physics is the interplay between shell and cluster structures [144]. This is mainly caused by the effect of the spinorbit interaction, which strengthens the symmetry of the $j j$ -coupling shell model. This interaction is well known to be vital in explaining the observed magic numbers of 28, 50, 82 and 126. The spin-orbit interaction also breaks clusters, where some of the strongly correlated nucleons are spatially localized.

Nevertheless, as we discussed in this article, the $\alpha$ cluster structure is important in the light mass region. Be isotopes are known to have a robust $\alpha$ - $\alpha$ cluster structure: $^ 8$ Be decays into two $\alpha$ clusters, and the molecular orbital structure of valence neutrons appears in neutron-rich Be isotopes [145, 146], which has been confirmed by the $a b$ 0 initio calculation as we have seen. The persistence of the $\alpha$ - $\alpha$ cluster structure is due to the relative distance, which is about 3–4 fm and large compared to the range of the spin-orbit interaction.

In light nuclei, it is considered that these two different models (shell and cluster) coexist and compete with each other. Although the $\alpha$ - $\alpha$ cluster structure persists in $^ { 8 }$ Be, when one more $\alpha$ cluster is added in 12C the interaction among $\alpha$ clusters becomes stronger and the system has a shorter $\alpha$ - $\alpha$ distance. In this case, the $\alpha$ clusters are trapped within the interaction range of the spin-orbit interaction. In $\mathrm { ^ { 1 2 } C }$ , although the three $\alpha$ cluster structure remains in the ground state, the $j j$ -coupling shlell model components mix in.

We can model this transition from the cluster state to the shell state owing to the spin-orbit interaction with clear perspective. The $\alpha$ clusters are spin-zero systems, so the spin-orbit interaction — a rank-one non-central interaction — does not contribute

for the systems consisting of the $\alpha$ clusters only. However, we have developed the antisymmetrized quasi cluster model (AQCM) [147–149]. This method enables us to smoothly transform the wave functions of the $\alpha$ -cluster model to those of the $j j$ -coupling shell model. We refer to the clusters that experience the effects of the spinorbit interaction due to this model as quasi-clusters, which alows us to discuss the intermediate state between this transition from the cluster state to the shell state. We previously introduced AQCM to $^ { 1 2 }$ C and discussed the competition between cluster states and the $j j$ -coupling shell model state.

Here, we summarize the basic concept of AQCM, which allows the smooth transformation of cluster model wave functions to $j j$ -coupling shell model ones. In AQCM, as in many other cluster models including the Brink model, each single particle is described by a Gaussian form.

$$
\phi^ {\tau , \sigma} (\mathbf {r}) = \left(\frac {2 \nu}{\pi}\right) ^ {\frac {3}{4}} \exp \left[ - \nu (\mathbf {r} - \zeta) ^ {2} \right] \chi^ {\tau , \sigma}, \tag {66}
$$

where the Gaussian center parameter $\zeta$ is related to the expectation value of the position of the nucleon, and $\chi ^ { \tau , \sigma }$ is the spin-isospin part of the wave function. The Slater determinant is constructed from these single-particle wave functions by antisymmetrizing them. For the Gaussian center parameters $\{ \zeta _ { i } \}$ , ihere four single-particle wave functions with different spin and isospin sharing a common $\zeta$ value correspond to an $\alpha$ cluster. This cluster wave function is transformed into $j j$ -coupling shell model based on the AQCM. When the original value of the Gaussian center parameter $\zeta$ is $\mathbf { R }$ , which is real and related to the spatial position of this nucleon, it is transformed by adding the imaginary part as

$$
\zeta = \mathbf {R} + i \Lambda \mathbf {e} ^ {\mathrm {s p i n}} \times \mathbf {R}, \tag {67}
$$

where $\mathbf { e } ^ { \mathrm { { s p i n } } }$ is a unit vector for the intrinsic-spin orientation of this nucleon. The control parameter, labelled as $\Lambda$ , is associated with the breaking of the $\alpha$ cluster. With a finite value of $\Lambda$ , the two nucleons with opposite spin orientations have complex conjugate $\zeta$ values. This situation corresponds to the time-reversal motion of the two nucleons.

Here, we explain the intuitive meaning of this procedure. Including the imaginary part allows us to connect the single-particle wave function directly to the spherical harmonics of the $j j$ -coupling shell model. Suppose the Gaussian center parameter, represented by the vector symbolized as $\zeta$ has an $x$ -component and the spin direction is defined along the $z$ -axis (i.e., a spin-up nucleon). According to Eq. (67), the imaginary part of the $x$ component of the Gaussian center parameter is given to the $y$ component. When we expand $- \nu \left( \mathbf { r } - \zeta \right) ^ { 2 }$ in the exponent of Eq. (66), a factor corresponding to the cross term of this expansion appears: e $\exp \left[ 2 \nu \zeta \cdot \mathbf { r } \right]$ . The factor $\exp \left[ 2 \nu \zeta \cdot \mathbf { r } \right]$ contains all the information related to the angular momentum of this single particle. The Taylor expansion allows us to show that the $p$ wave component of $\exp \left[ 2 \nu \zeta \cdot \mathbf { r } \right]$ is $2 \nu \zeta \cdot \mathbf { r }$ , which is proportional to $( x + i \Lambda y )$ . At the limit of $\Lambda = 1$ , this is proportional to $Y _ { 1 1 }$ of the spherical harmonics. The nucleon is introduced as spin-up, and thus the coupling with the spin part gives the stretched state of the angular momentum, $\left| 3 / 2 \ 3 / 2 \right.$ of the

![](images/68afbf2b3717ee475a9ead643edf691bdc58af9d0a9fba62c1d42e54ed9669a9.jpg)  
Fig. 20 Energy curves of $0 ^ { + }$ state of $^ 8 \mathrm { B e }$ as a function of the distance between two $^ 4 \mathrm { H e }$ clusters. Solid line is for $\Lambda = 0$ (pure two α’s) and dotted and dashed lines are for two quasi-clusters with $\Lambda = 0 . 1$ and 0.2, respectively. See the details in Ref. [150].

$j j$ -coupling shell model, where the spin-orbit interaction acts attractively. For the spindown nucleon, we introduce the complex conjugate $\zeta$ value, which gives $\left| 3 / 2 \right. \mathrm { ~ - ~ } 3 / 2 \rangle$ .

This transformation is quite general, and we can easily generate the $j j$ -coupling shell model wave functions corresponding to the magic numbers 28, 50, and 82 starting with the cluster wave functions. In the case of $^ { 1 2 } \mathrm { C }$ , we prepare three quasi clusters. The next two nucleons are generated by rotating the $\zeta$ values and spin-directions of these two nucleons by $2 \pi / 3$ . The last two nucleons are generated by changing the rotation angle to $4 \pi / 3$ . Eventually, all the six nucleons have spin-stretched states, and after the antisymmetrization, the configuration becomes the subclosure configuration of $\left( s 1 / 2 \right) ^ { 2 } \left( p 3 / 2 \right) ^ { 4 }$ . This procedure is applied for both proton and neutron parts.

We start the discussion with $^ { \mathrm { ~ 8 ~ } }$ Be. Our Hamiltonian gives the energy of $- 2 7 . 5 7$ MeV for the $\alpha$ cluster, and thus, $- 5 5 . 1$ MeV is the two- $\alpha$ threshold energy (experimentally $- 5 6 . 6$ MeV, to which our theoretical value does not contradict). Figure 20 shows the energy curves of the $0 ^ { + }$ state of $^ 8$ Be as a function of the distance between two 4He clusters. The solid line is for $\Lambda = 0$ (pure two $\alpha$ ’s), and the dotted and dashed line are for two quasi-clusters with $\Lambda = 0 . 1$ and 0.2, respectively. The energy minimum point appears around the relative distance of ${ \sim } 3 . 5$ fm. This distance is quite large, and this is outside of the interaction range of the spin-orbit interaction. Therefore, the $\Lambda$ value that gives the minimum energy is zero (solid line), which means that the $\alpha$ clusters are not broken. The $\alpha$ breaking effect can be seen in more inner regions, where the energies of dotted and dashed lines are lower than the solid line. The $\alpha$ clusters are surely broken there. However, at short relative distances, the energy itself is high enough, and the spin-orbit interaction only plays a role in reducing the increase of the excitation energy to some extent when two clusters get closer.

Next we discuss $\bot 2$ C. The three- $\alpha$ threshold energy is $- 8 2 . 7$ MeV in our calculation compared with the experimental value of $- 8 4 . 9$ MeV. Figure 21 shows the energy curves of $0 ^ { + }$ state of $\mathrm { ^ { 1 2 } C }$ with an equilateral triangular configuration as a function of the distance between two 4He clusters. The solid line is for $\Lambda = 0$ (pure three $\alpha$ ’s). Since one 4He is added to $^ { 8 }$ Be, the energy minimum point appears around the relative

![](images/1fdad67b35436c3601e2c614495e55f896a215b1490f0f3c74777bf9dd1532cb.jpg)  
Fig. 21 Energy curves of $0 ^ { + }$ state of $^ { 1 2 } \mathrm { C }$ as a function of the distance between three $^ { 4 } \mathrm { H e }$ clusters with equilateral triangular configuration. Solid line is for $\Lambda = 0$ (pure three $_ \alpha$ ’s) and dotted and dashed lines are for two quasi-clusters with $\Lambda = 0 . 1$ and 0.2, respectively. See the details in Ref. [150].

distance of 2.5–3.0 fm, shorter by 1 fm than the previous $^ 8 \mathrm { B e }$ case before allowing the breaking of $\alpha$ clusters. Therefore, it is considered that the three $\alpha$ clusters step in the interaction range of the spin-orbit interaction. The dotted line $\Lambda = 0 . 1$ ) and dashed line ( $\Lambda = 0 . 2$ ) almost degenerate at the region of the lowest energy (the relative cluster-cluster distance shrinks to 2 fm there).

It can be summarized that the cluster breaking effect is negligibly small in 8Be, where $\alpha$ –α cluster structure keeps enough distance; they stay out of the interaction range of the spin-orbit interaction, which breaks the $\alpha$ clusters. The situation is completely different in the $^ { 1 2 } \mathrm { C }$ case since the additional $\alpha$ cluster shrinks the cluster-cluster distance, and clusters are in the interaction range of the spin-orbit interaction. The ground state of $^ { 1 2 } \mathrm { C }$ contains the component of the $j j$ -coupling shell model.

# 5 Remarks and prospects transcending sections

We here present some remarks and prospects over multiple sections, keep aside subjects presented in individual sections such as rotational features in Sect. 2.

The three sections, Sects. 2-4, of this article approach $\alpha$ clustering in light nuclei from distinct theoretical perspectives, yet they converge on an identical physical picture. It is worth making this convergence explicit, as it constitutes one of the unique messages of this work. At the level of methodology, all three approaches are rooted in the same conceptual foundation: a configuration-interaction (CI) and variational description based on nucleonic degrees of freedom and realistic nucleonnucleon interactions. What differs is the strategy of configuration selection and representation. Section 2 employs a very large-scale no-core shell model diagonalization (MCSM), where cluster correlations are not assumed but emerge organically from the superposition of a vast number of many-body basis states. Section 3 adopts a complementary strategy, the Cluster-Nucleon Configuration Interaction (CNCIM), in which traditional shell-model-like Slater determinant configurations are combined with microscopically constructed cluster channel configurations, enriching the basis

in a physically targeted way. Section-4 uses the antisymmetrized quasi-cluster model (AQCM), where cluster wave functions built from Gaussian single-particle states with complex center parameters are smoothly connected to $j j$ -coupling shell-model wave functions through a continuous deformation parameter, thereby modeling the intermediate regime between pure cluster and pure shell structure. Together, the three approaches thus bridge the two structural limits from complementary view points.

All three approaches are applied to the same nuclei, and the degree of agreement across methods is instructive. The ground state of 8Be, a di- $\alpha$ resonance just above the two- $\alpha$ threshold, provides the clearest example. Figures 5, 18, and 20, drawn from Sects. 2, 3, and 4 respectively, independently arrive at the same result: the two $\alpha$ clusters orbit each other with a center-to-center separation of approximately 3.5–3.6 fm. This value emerges from a two-dimensional nucleon density profile in the intrinsic frame, from the structure of the RGM relative-motion wave function, and from the minimum of the AQCM energy surface as a function of cluster-cluster distance. The agreement across such different theoretical languages is not a coincidence: this separation reflects a balance between kinetic energy and nuclear attraction that is robust across model choices, and it places the two clusters well outside the range of the spin-orbit interaction, explaining why the $\alpha$ structure in $^ { 8 } \mathrm { { B e } }$ is essentially unperturbed. The two $\alpha$ clusters rotate at this nearly fixed separation, giving rise to a rotational band consistently identified across approaches.

12C presents a richer case where the three perspectives are genuinely complementary rather than merely confirmatory. All three sections find that the ground state is not a pure cluster state but contains a significant admixture of shell-model-type structure, yet each illuminates a different facet of this competition: Sect. 2 quantifies the mixing and its energetic consequence, Sect. 3 addresses its manifestation in spectroscopic factors, and Sect. 4 provides the dynamical mechanism: the contraction of the inter-cluster distance to approximately 2.5–3.0 fm upon adding a third alpha cluster brings the system within the range of the spin-orbit interaction, generating shell-model admixtures that have no counterpart in $^ { \mathrm { ~ 8 ~ } }$ Be. For the Hoyle state, the approaches confirm that alpha clustering is the dominant structural feature, with shell-model components present as a secondary admixture from the ground state.

Experimental evidence for $\alpha$ clustering extends well beyond the light nuclei discussed here, and the question of how clustering strength evolves across the nuclear chart remains open. Near-threshold clustering phenomena, only briefly touched upon in this article, represent a particularly rich subject: the restructuring of many-body wave functions in the vicinity of cluster-decay thresholds, the role of superradiance in organizing broad doorway and narrow trapped states embedded in the continuum, all remain areas of active investigation.

A broader perspective connects $\alpha$ clustering to the more general question of fournucleon correlations and their evolution across the nuclear chart. The connection between alpha particles, proton-neutron quartets, and pairing correlations in heavier nuclei is well motivated theoretically but not yet fully explored in a unified framework. The crossover from a regime dominated by pairing, through quartet condensation, to explicit spatial clustering as a function of nuclear size or proton-neutron asymmetry represents a yet unsolved problem in nuclear many-body physics.

The methods presented and developed here offer promising tools for addressing these open questions in nuclear physics and beyond.

# Acknowledgments

All authors thank Dr. Takashi Nakamura for arranging the excellent opportunity to publish this article. Regarding the work presented in Sect. 2, TO acknowledges Drs. T. Yoshida, T. Abe, Y. Tsunoda, N. Shimizu, N. Itagaki, Y. Utsuno, H. Ueno, J. Vary and P. Maris for very fruitful collaborative works shown primarily in Refs. [9, 10]. TO thanks Dr. K. C. W. Li and Dr. M. Kimura for useful discussions on the clustering, Dr. S. Kuma and Dr. T. Azuma for various information about atomic molecules, and Dr. Y. Aritomo for updating on nuclear fission studies. TO is grateful to Dr. T. Kobori for encouragements crucially contributing to this work. TO and AV acknowledge the visitor program of GANIL, and TO thanks the Alexander von Humboldt Foundation for the Research Award, as some parts of their works were made under these supports. The MCSM (incl. QVSM) calculations quoted in Sect. 2 were performed on the supercomputers K and Fugaku at RIKEN AICS K and Fugaku at RIKEN AICS (hp190160, hp200130, hp210165, hp220174, hp230207, hp240213, hp250224). The work presented in Sect. 2 are supported in part by JSPS KAKENHI Grant Number JP19H05145 and JP21H00117 as well as JP25K00998. It was also supported in part by MEXT as “Program for Promoting Researches on the Supercomputer Fugaku” (Simulation for basic science: from fundamental laws of particles to creation of nuclei, JPMXP1020200105, Simulation for basic science: approaching the new quantum era, JPMXP1020230411), and by JICFuS. Regarding the work presented in Sect. 3, AV acknowledges partial support by the US Department of Energy (DOE), Office of Science, Office of Nuclear Physics grant DE-SC0009883. Regarding the work presented in Sect. 4, NI acknowledges partial support by JSPS KAKENHI Grant Numbers JP22K03618 and JP25K01005.

# References

[1] Wefelmeier, W.V.: Ein geometrisches modell des atomkerns. Z. Phys. Hadrons Nucl. 107, 332 (1937)   
[2] A., W.J.: Molecular viewpoints in nuclear structure. Phys. Rev. 52, 1083 (1937)   
[3] Morinaga, H.: Interpretation of some of the excited states of 4n self-conjugate nuclei. Phys. Rev. C 101, 254 (1956)   
[4] Brink, D.: Alpha-particle model of light nuclei. In: The Proc. Intl. School of Physics Enrico Fermi, Course 36, p. 020030 (247)   
[5] Ikeda, K., Takigawa, N., Horiuchi, H.: The Systematic Structure-Change into the Molecule-like Structures in the Self-Conjugate 4n Nuclei. Prog. Thoer. Phys. Suppl. E68, 464–475 (1968) https://doi.org/10.1143/PTPS.E68.464   
[6] Arima, A., Horiuchi, H., Kubodera, K., Takigawa, N.: Clustering in light nucle. Advances in Nuclear Physics, vol. 5, p. 345. Springer, Berlin, Heidelberg (1973)   
[7] Freer, M., Horiuchi, H., Kanada-En’yo, Y., Lee, D., Meißner, U.-G.: Microscopic clustering in light nuclei. Rev. Mod. Phys. 90(3), 35004 (2018) https://doi.org/10.1103/RevModPhys.90.035004

[8] Nakamura, T., Shigaki, K., Ohnishi, H., et al.: Clustering as a window on the hierarchical structure of quantum systems. Eur. Phys. J. A 61, 273 (2025)   
[9] Otsuka, T., Tsunoda, Y., Shimizu, N., Utsuno, Y., Abe, T., Ueno, H.: Prevailing triaxial shapes in atomic nuclei and a quantum theory of rotation of composite objects. Eur. Phys. J. A 61, 126 (2025)   
[10] Otsuka, T., Abe, T., Yoshida, T., Tsunoda, Y., Shimizu, N., Itagaki, N., Utsuno, Y., Vary, J., Maris, P., Ueno, H.: $\alpha$ -clustering in atomic nuclei from first principles with statistical learning and the hoyle state character. Nat. Commun. 13, 2234 (2022)   
[11] Uegaki, E., Okabe, S., Abe, Y., Tanaka, H.: Structure of the excited states in 12c. i. Prog. Thoer. Phys. 57, 1262 (1977)   
[12] Kamimura, M.: Transition densities between the $0 _ { 1 } ^ { + }$ , $2 _ { 1 } ^ { + }$ , $4 _ { 1 } ^ { + }$ , $0 _ { 2 } ^ { + }$ , $2 _ { 2 } ^ { + }$ , $1 _ { 1 } ^ { - }$ and $3 _ { 1 } ^ { - }$ states in $^ { 1 2 } \mathrm { c }$ derived from the three-alpha resonating-group wave functions. Nucl. Phys. A 351, 456 (1981)   
[13] Tohsaki, A., Horiuchi, H., Schuck, P., R¨opke, G.: Alpha cluster condensation in 12C and $^ { 1 6 }$ O. Phys. Rev. Lett. 87(19), 192501 (2001) https://doi.org/10.1103/PhysRevLett.87.192501   
[14] Bijker, R., Iachello, F.: The algebraic cluster model: Three-body clusters. Ann. Phys. 298(2), 334–360 (2002) https://doi.org/10.1006/aphy.2002.6255   
[15] Itagaki, N., Aoyama, S., Okabe, S., Ikeda, K.: Cluster-shell competition in light nuclei. Phys. Rev. C 70, 054307 (2004)   
[16] Chernykh, M., Feldmeier, H., Neff, T., Von Neumann-Cosel, P., Richter, A.: Structure of the hoyle state in c12. Phys. Rev. Lett. 98, 032501 (2007)   
[17] Kanada-En’yo, Y.: The structure of ground and excited states of $^ { 1 2 } \mathrm { c }$ . Prog. Thoer. Phys. 117, 655 (2007)   
[18] Maris, P., Caprio, M.A., Vary, J.P.: Emergence of rotational bands in ab initio no-core configuration interaction calculations of the be isotopes. Phys. Rev. C 91, 014310 (2015)   
[19] Zhao, P.W., Itagaki, N., Meng, J.: Rod-shaped nuclei at extreme spin and isospin. Phys. Rev. Lett. 115, 022501 (2015)   
[20] Dreyfuss, A.C., Launey, K.D., Dytrych, T., Draayer, J.P., Baker, R.B., Deibel, C.M., Bahri, C.: Understanding emergent collectivity and clustering in nuclei from a symmetry-based no-core shell-model perspective. Phys. Rev. C 95(4), 044312 (2017) https://doi.org/10.1103/PhysRevC.95.044312   
[21] Wiringa, R.B., Pieper, S.C., Carlson, J., Pandharipande, V.R.: Quantum monte carlo calculations of a=8 nuclei. Phys. Rev. C: Nucl. Phys. 62(1), 14001 (2000) https://doi.org/10.1103/PhysRevC.62.014001   
[22] Carlson, J., Gandolfi, S., Pederiva, F., Pieper, S.C., Schiavilla, R., Schmidt, K.E., Wiringa, R.B.: Quantum monte carlo method for nuclear physics. Rev. Mod. Phys. 87, 1067 (2015)   
[23] Epelbaum, E., Krebs, H., L¨ahde, T.A., Lee, D., Meißner, U.-G.: Structure and rotations of the hoyle state. Phys. Rev. Lett. 109, 252501 (2012)   
[24] D’Alessio, A., Mongelli, T., Arnold, M., Bassauer, S., Birkhan, J., Brandherm, I., Hilcker, M., H¨uther, T., Isaak, J., J¨urgensen, L., Klaus, T., Mathy, M., Neumann-Cosel, P., Pietralla, N., Yu. Ponomarev, V., Ries, P.C., Roth, R.,

Singer, M., Steinhilber, G., Vobig, K., V., W.: Precision measurement of the e2 transition strength to the $2 _ { 1 } ^ { + }$ state of $^ { 1 2 } \mathrm { c }$ . Phys. Rev. C 102, 011302 (2020)   
[25] Shen, S., Elhatisari, S., L¨ahde, T.A., et al.: Emergent geometry and duality in the carbon nucleus. Nat. Commun. 14, 2777 (2023)   
[26] Hoyle, F.: On nuclear reactions occuring in very hot stars. 1. The synthesis of elements from carbon to nickel. Astrophys. J. Suppl. 1, 121 (1954)   
[27] Dunbar, D.N.F., Pixley, R.E., Wenzel, W.A., Whaling, W.: The 7.68-mev state in $\mathrm { C ^ { 1 2 } }$ . Phys. Rev. 92(3), 649–650 (1953) https://doi.org/10.1103/PhysRev.92.649   
[28] Freer, M., Fynbo, H.O.U.: The hoyle state in $^ { 1 2 } \mathrm { c }$ . Prog. Part. Nucl. Phys. 78, 1 (2014)   
[29] Fynbo, H.O.U., et al.: Revised rates for the stellar triple- $\alpha$ process from measurement of $^ { 1 2 } \mathrm { c }$ nuclear resonances. Nature 433, 136–139 (2005)   
[30] Jin, S., Roberts, L.F., Austin, S.M., Schatz, H.: Enhanced triple- $\alpha$ reaction reduces proton-rich nucleosynthesis in supernovae. Nature 588, 57–60 (2020)   
[31] Shirokov, A.M., Shin, I.J., Kim, Y., Sosonkina, M., P., M., Vary, J.P.: N3lo nn interaction adjusted to light nuclei in ab exitu approach. Phys. Lett. B 761, 87 (2016)   
[32] Shirokov, A.M., Vary, J.P., Mazur, A.I., Weber, T.A.: Realistic nuclear hamiltonian: Ab exitu approach. Phys. Lett. B 644, 33 (2007)   
[33] National Nuclear Data Center’s “Evaluated Nuclear Structure Data File”. http://www.nndc.bnl.gov/ensdf/   
[34] Honma, M., Mizusaki, T., Otsuka, T.: Diagonalization of hamiltonians for manybody systems by auxiliary field quantum monte carlo technique. Phys. Rev. Lett. 75, 1284 (1995)   
[35] Otsuka, T., Mizusaki, T., Honma, M.: Structure of the n=z=28 closed shell studied by monte carlo shell model calculation. Phys. Rev. Lett. 81, 1588 (1998)   
[36] Otsuka, T., Honma, M., Mizusaki, T., Shimizu, N., Utsuno, Y.: Monte carlo shell model for atomic nuclei. Prog. Part. Nucl. Phys. 47, 319–400 (2001)   
[37] Shimizu, N., et al.: New-generation monte carlo shell model for the k computer era. Prog. Theor. Exp. Phys. 2012, 01–205 (2012)   
[38] Abe, T.at al. .: Benchmarks of the full configuration interaction, monte carlo shell model, and no-core full configuration methods. Phys. Rev. C 86, 054301 (2012)   
[39] Abe, T., et al.: Ground-state properties of light $4 n$ self-conjugate nuclei in ab initio no-core monte carlo shell model with nonlocal nn interactions. Phys. Rev. C 104, 054315   
[40] Hastie, T., Tibshirani, R., Friedman, J.: The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Second Edition. Springer, Berlin (2009)   
[41] Strinati, G.C., Pieri, P., R¨opke, G., Schuck, P., Urban, M.: The bcs–bec crossover: From ultra-cold fermi gases to nuclear systems. Phys. Rept. 738, 1 (2018)   
[42] Bohr, A.: The coupling of nuclear surface oscillations to the motion of individual nucleons. Mat. Fys. Medd. Dan. Vid. Selsk. 26, 14 (1952)   
[43] Bohr, A., Mottelson, B.R.: Collective and individual-particle aspects of nuclear structure. Mat. Fys. Medd. Dan. Vid. Selsk. 27, 16 (1953)

[44] Bohr, A.N.: Rotational motion in nuclei. In: Lundqvist, S. (ed.) Nobel Lectures, Physics 1971–1980, p. 213. World Scientific, Singapore,1992   
[45] Bohr, A., Mottelson, B.R.: Nuclear Structure, Vol. II. Benjamin, New York (1975)   
[46] Ring, P., Schuck, P.: The Nuclear Many-Body Problem. Springer, Berlin (1980)   
[47] Johansson, S.: Award ceremony speech, 1975. In: Lundqvist, S. (ed.) Nobel Lectures, Physics 1971–1980. World Scientific, Singapore, 1992   
[48] Otsuka, T.: A comprehensive view of nuclear shapes, rotations and vibrations from fully quantum mechanical perspectives. EPJ Web of Conferences 342, 01021 (2025) https://doi.org/10.1051/epjconf/202534201021   
[49] Chernykh, M., Feldmeier, H., Neff, T., Neumann-Cosel, P., Richter, A.: Structure of the hoyle state in $_ { 1 2 }$ C. Phys. Rev. Lett. 98, 032501 (2007) https://doi.org/10.1103/PhysRevLett.98.032501   
[50] Zimmerman, W.R., Destefano, N.E., Freer, M., Gai, M., Smit, F.D.: Further evidence for the broad $2 _ { 2 } ^ { + }$ state at 9.6 mev in $^ { 1 2 } \mathrm { c }$ . Phys. Rev. C 84, 027304 (2011) https://doi.org/10.1103/PhysRevC.84.027304   
[51] Zimmerman, W.R., Ahmed, M.W., Bromberger, B., Stave, S.C., Breskin, A., Dangendorf, V., Delbar, T., Gai, M., Henshaw, S.S., Mueller, J.M., Sun, C., Tittelmeier, K., Weller, H.R., Wu, Y.K.: Unambiguous identification of the second $2 ^ { + }$ state in $^ { 1 2 } \mathbf { C }$ and the structure of the hoyle state. Phys. Rev. Lett. 110, 152502 (2013) https://doi.org/10.1103/PhysRevLett.110.152502   
[52] Ogloblin, A.A., et al.: Rotational band in $^ { 1 2 } \mathrm { c }$ based on the hoyle state. EPJ Web of Conferences 66, 02074 (2014)   
[53] Mar’in-L’ambarri, D.J., et al.: Evidence for triangular d3h symmetry in ${ } ^ { 1 2 } \mathrm { c }$ . Phys. Rev. Lett. 113, 012502 (2014)   
[54] Funaki, Y.: Hoyle band and $\alpha$ condensation in $^ { 1 2 }$ C. Phys. Rev. C 92, 021302 (2015) https://doi.org/10.1103/PhysRevC.92.021302   
[55] Marevi´c, P., Ebran, J.-P., Khan, E., Nikˇsic, T., Vretenar, D.: Cluster structures in $^ { 1 2 }$ C from global energy density functionals. Phys. Rev. C 99, 034317 (2019) https://doi.org/10.1103/PhysRevC.99.034317   
[56] Danilov, A.N., Belyaeva, T.L., Demyanova, A.S., Goncharov, S.A., Ogloblin, A.A.: Determination of nuclear radii for unstable states in 12c with diffraction inelastic scattering. Phys. Rev. C 80, 054603 (2009)   
[57] Otsuka, T., Utsuno, Y.: Quantum appearance of tennis racket effect in atomic nuclei and conservation of K quantum number (tentative) (2026)   
[58] Bijker, R., Iachello, F.: Evidence for tetrahedral symmetry in $^ { 1 6 } ($ o. Phys. Rev. Lett. 112, 152501 (2014)   
[59] Atkins, P., Paula, J., Keeler, J.: Physical Chemistry. Springer, Berlin (2012)   
[60] Krappe, J.K., Pomorski, K.: Theory of Nuclear Fission. Springer, Berlin (2012)   
[61] Wilson, J.N., et al.: Angular momentum generation in nuclear fission. Nature 590, 566 (2021)   
[62] Gamow, G.: Mass defect curve and nuclear constitution. Proc. R. Soc. Lond. A: Math. Phys. Eng. Sci. 126(803), 632–644 (1930) https://doi.org/10.1098/rspa.1930.0032   
[63] Hafstad, L.R., Teller, E.: The alpha-particle model of the nucleus. Phys. Rev.

54(9), 681–692 (1938) https://doi.org/10.1103/PhysRev.54.681   
[64] Blatt, J.M., Weisskopf, V.F.: Theoretical Nuclear Physics. Dover Books on Physics. Dover Publications, New York (2012)   
[65] Volya, A., Barbui, M., Goldberg, V.Z., Rogachev, G.V.: Superradiance in alpha clustered mirror nuclei. Commun Phys 5(1), 1–6 (2022) https://doi.org/10.1038/s42005-022-01105-9   
[66] Sandulescu, N., Sambataro, M., Volya, A.: Proton-neutron pairing, quartet condensation and $A -$ transfer in N=Z nuclei. EPJ Web Conf. 292, 1003 (2024) https://doi.org/10.1051/epjconf/202429201003   
[67] White, C., Volya, A., Mulhall, D., Zelevinsky, V.: Structured ground states of randomly interacting bosons. Phys. Rev. Res. 5(1), 013109 (2023) https://doi.org/10.1103/PhysRevResearch.5.013109   
[68] Kanada-En’yo, Y., Kimura, M., Ono, A.: Antisymmetrized molecular dynamics and its applications to cluster phenomena. Prog. Theor. Exp. Phys. 2012(1), 1–202 (2012) https://doi.org/10.1093/ptep/pts001   
[69] Wheeler, J.A.: On the mathematical description of light nuclei by the method of resonating group structure. Phys. Rev. 52(11), 1107–1122 (1937) https://doi.org/10.1103/PhysRev.52.1107   
[70] Wildermuth, K., Kanellopoulos, E.J.: Clustering aspects in nuclei and their microscopic description. Rep. Prog. Phys. 42(10), 1719 (1979) https://doi.org/10.1088/0034-4885/42/10/003   
[71] Draayer, J.P.: Alpha-particle spectroscopic amplitudes for sd shell nuclei. Nucl. Phys. A 237(1), 157–181 (1975) https://doi.org/10.1016/0375-9474(75)90470-4   
[72] Smirnov, Y.F., Tchuvilsky, Y.M.: Cluster Spectroscopic Factors for P-Shell Nuclei. Phys. Rev. C 15(1), 84–93 (1977) https://doi.org/10.1103/PhysRevC.15.84   
[73] Chung, W., van Hienen, J., Wildenthal, B.H., Bennett, C.L.: Shell-model predictions of alpha-spectroscopic factors between ground states of 16 a 40 nuclei. Phys. Lett. B 79(4), 381–384 (1978) https://doi.org/10.1016/0370- 2693(78)90387-8   
[74] Anantaraman, N., Bennett, C.L., Draayer, J.P., Fulbright, H.W., Gove, H.E., To ¯oke, J.: Systematics of ground-state $\alpha$ -particle spectroscopic strengths for sd- and fp-shell nuclei. Phys. Rev. Lett. 35(17), 1131–1134 (1975) https://doi.org/10.1103/PhysRevLett.35.1131   
[75] Dreyfuss, A.C., Launey, K.D., Escher, J.E., Sargsyan, G.H., Baker, R.B., Dytrych, T., Draayer, J.P.: Clustering and $ ensuremath alpha $- capture reaction rate from ab initio symmetry-adapted descriptions of $ˆ{20}\mathrm{Ne}$. Phys. Rev. C 102(4), 044608 (2020) https://doi.org/10.1103/PhysRevC.102.044608   
[76] Dytrych, T., Launey, K.D., Draayer, J.P., Rowe, D.J., Wood, J.L., Rosensteel, G., Bahri, C., Langr, D., Baker, R.B.: Physics of Nuclei: Key Role of an Emergent Symmetry. Phys. Rev. Lett. 124(4), 042501 (2020) https://doi.org/10.1103/PhysRevLett.124.042501   
[77] Ebran, J.-P., Khan, E., Nikˇsi´c, T., Vretenar, D.: How atomic nuclei cluster. Nature 487(7407), 341 (2012) https://doi.org/10.1038/nature11246

[78] Epelbaum, E., Krebs, H., Lee, D., Meißner, U.-G.: Ab initio calculation of the hoyle state. Phys. Rev. Lett. 106(19), 192501 (2011) https://doi.org/10.1103/PhysRevLett.106.192501   
[79] Elhatisari, S., Lee, D., Rupak, G., Epelbaum, E., Krebs, H., L¨ahde, T.A., Luu, T., Meißner, U.-G.: Ab initio alpha–alpha scattering. Nature 528(7580), 111–114 (2015) https://doi.org/10.1038/nature16067   
[80] Schuck, P., Funaki, Y., Horiuchi, H., R¨opke, G., Tohsaki, A., Yamada, T.: Alpha particle clusters and their condensation in nuclear systems. Phys. Scr. 91(12), 123001 (2016) https://doi.org/10.1088/0031-8949/91/12/123001   
[81] Tohsaki, A., Horiuchi, H., Schuck, P., R¨opke, G.: Colloquium: Status of $\alpha$ - particle condensate structure of the hoyle state. Rev. Mod. Phys. 89(1), 11002 (2017) https://doi.org/10.1103/RevModPhys.89.011002   
[82] Navr´atil, P., Quaglioni, S.: Ab initio many-body calculations of the H-3(d, n)he-4 and he-3(d, p)he-4 fusion reactions. Phys. Rev. Lett. 108(4), 42503 (2012) https://doi.org/10.1103/PhysRevLett.108.042503   
[83] Navr´atil, P., Quaglioni, S., Hupin, G., Romero-Redondo, C., Calci, A.: Unified ab initio approaches to nuclear structure and reactions. Phys. Scr. 91(5), 53002 (2016) https://doi.org/10.1088/0031-8949/91/5/053002   
[84] Zhang, X., Stroberg, S.R., Navr´atil, P., Gwak, C., Melendez, J.A., Furnstahl, R.J., Holt, J.D.: Ab initio calculations of low-energy nuclear scattering using confining potential traps. Phys. Rev. Lett. 125(11), 112503 (2020) https://doi.org/10.1103/PhysRevLett.125.112503   
[85] Johnson, C.W., Launey, K.D., Auerbach, N., Bacca, S., Barrett, B.R., R Brune, C., Caprio, M.A., Descouvemont, P., Dickhoff, W.H., Elster, C., Fasano, P.J., Fossez, K., Hergert, H., Hjorth-Jensen, M., Hlophe, L., Hu, B., Id Betan, R.M., Idini, A., K¨onig, S., Kravvaris, K., Lee, D., Lei, J., Mercenne, A., Perez, R.N., Nazarewicz, W., Nunes, F.M., P loszajczak, M., Rotureau, J., Rupak, G., Shirokov, A.M., Thompson, I., Vary, J.P., Volya, A., Xu, F., Zegers, R.G.T., Zelevinsky, V., Zhang, X.: White paper: From bound states to the continuum. J. Phys. G: Nucl. Part. Phys. 47(12), 123001 (2020) https://doi.org/10.1088/1361- 6471/abb129   
[86] Oko lowicz, J., P loszajczak, M., Nazarewicz, W.: Convenient Location of a Near-Threshold Proton-Emitting Resonance in $ˆ 11 mathrm B $. Phys. Rev. Lett. 124(4), 042502 (2020) https://doi.org/10.1103/PhysRevLett.124.042502   
[87] Volya, A.: Assessment of the beta-delayed proton decay rate of 11Be. EPL 130(1), 12001 (2020) https://doi.org/10.1209/0295-5075/130/12001   
[88] Avila, M.L., Rogachev, G.V., Goldberg, V.Z., Johnson, E.D., Kemper, K.W., Tchuvil’sky, Y.M., Volya, A.S.: Alpha-cluster structure of O-18. Phys. Rev. C 90(2), 024327 (2014) https://doi.org/10.1103/PhysRevC.90.024327   
[89] Kuchera, A.N.: Clustering Phenomena in the a=10 T=1 Isobaric Multiplet. PhD thesis, unknown (2013)   
[90] Oko lowicz, J., P loszajczak, M., Rotter, I.: Dynamics of quantum systems embedded in a continuum. Phys. Rep. 374(4), 271–383 (2003) https://doi.org/10.1016/S0370-1573(02)00366-6   
[91] Auerbach, N., Zelevinsky, V.: Super-radiant dynamics, doorways and resonances

in nuclei and other open mesoscopic systems. Rep. Prog. Phys. 74(10), 106301 (2011) https://doi.org/10.1088/0034-4885/74/10/106301   
[92] Kravvaris, K., Volya, A.: Constructing realistic alpha cluster channels. J. Phys.: Conf. Ser. 863(1), 012016 (2017) https://doi.org/10.1088/1742- 6596/863/1/012016   
[93] Koshchiy, E., Rogachev, G.V., Pollacco, E., Ahn, S., Uberseder, E., Hooker, J., Bishop, J., Aboud, E., Barbui, M., Goldberg, V.Z., Hunt, C., Jayatissa, H., Magana, C., O’Dwyer, R., Roeder, B.T., Saastamoinen, A., Upadhyayula, S.: Texas Active Target (TexAT) detector for experiments with rare isotope beams. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 957, 163398 (2020) https://doi.org/10.1016/j.nima.2020.163398   
[94] Barbui, M., Volya, A., Aboud, E., Ahn, S., Bishop, J., Goldberg, V.Z., Hooker, J., Hunt, C.H., Jayatissa, H., Kokalova, Tz., Koshchiy, E., Pirrie, S., Pollacco, E., Roeder, B.T., Saastamoinen, A., Upadhyayula, S., Wheldon, C., Rogachev, G.V.: $\alpha$ -cluster structure of $^ { 1 8 }$ Ne. Phys. Rev. C 106(5), 054310 (2022) https://doi.org/10.1103/PhysRevC.106.054310   
[95] Goldberg, V.Z., Nurmukhanbetova, A.K., Volya, A., Nauruzbayev, D.K., Serikbayeva, G.E., Rogachev, G.V.: $\alpha$ -cluster structure in $^ { 1 9 }$ F and $^ { 1 9 }$ Ne in resonant scattering. Phys. Rev. C 105(1), 014615 (2022) https://doi.org/10.1103/PhysRevC.105.014615   
[96] Nauruzbayev, D.K., Goldberg, V.Z., Nurmukhanbetova, A.K., Golovkov, M.S., Volya, A., Rogachev, G.V., Tribble, R.E.: Structure of Ne 20 states in resonance O $1 6 ~ + ~ \alpha$ elastic scattering. Phys. Rev. C 96(1), 014322 (2017) https://doi.org/10.1103/PhysRevC.96.014322   
[97] Nurmukhanbetova, A.K., Goldberg, V.Z., Nauruzbayev, D.K., Golovkov, M.S., Volya, A.: Evidence for $\alpha$ -cluster structure in $^ { 2 1 }$ Ne in the first measurement of resonant $\mathbf { \bot 7 }$ O+α elastic scattering. Phys. Rev. C 100(6), 062802 (2019) https://doi.org/10.1103/PhysRevC.100.062802   
[98] Nurmukhanbetova, A.K., Goldberg, V.Z., Volya, A., Nauruzbayev, D.K., Rogachev, G.V.: $$ˆ{18}$$F alpha cluster structure in the resonant $$ˆ{14}$$N+$$\alpha $$ scattering. Eur. Phys. J. A. 60(11), 217 (2024) https://doi.org/10.1140/epja/s10050-024-01434-z   
[99] Nurmukhanbetova, A.K., Goldberg, V.Z., Volya, A., Nauruzbayev, D.K., Serikbayeva, G.E., Rogachev, G.V.: $R$- matrix analysis of $ˆ{22}\mathrm{Ne}$ states populated in $ˆ 18 mathrm O ( ensuremath alpha , ensuremath alpha )$ resonant elastic scattering. Phys. Rev. C 109(2), 24607 (2024) https://doi.org/10.1103/PhysRevC.109.024607   
[100] Upadhyayula, S., Rogachev, G.V., Bishop, J., Goldberg, V.Z., Hooker, J., Hunt, C., Jayatissa, H., Koshchiy, E., Uberseder, E., Volya, A., Roeder, B.T., Saastamoinen, A.: Search for the high-spin members of the α : 2 n : α band in Be 10. Phys. Rev. C 101(3), 034604 (2020) https://doi.org/10.1103/PhysRevC.101.034604   
[101] Volya, A., Goldberg, V.Z., Nurmukhanbetova, A.K., Nauruzbayev, D.K.,

Rogachev, G.V.: Lowest-energy broad $\alpha$ -cluster resonances in $^ { 1 9 }$ F. Phys. Rev. C 105(1), 014614 (2022) https://doi.org/10.1103/PhysRevC.105.014614   
[102] de-Shalit, A., Talmi, I.: Nuclear Shell Theory. Dover Books on Physics. Dover, New York (2004)   
[103] Barrett, B.R., Navr´atil, P., Vary, J.P.: Ab Initio no core shell model. Prog. Part. Nucl. Phys. 69, 131–181 (2013) https://doi.org/10.1016/j.ppnp.2012.10.003   
[104] Palumbo, F., Prosperi, D.: Effects of translational invariance violation in particle-hole calculations. Application to 208Pb. Nucl. Phys. A 115(2), 296–308 (1968) https://doi.org/10.1016/0375-9474(68)90005-5   
[105] Gloeckner, D.H., Lawson, R.D.: Spurious center-of-mass motion. Phys. Lett. B 53(4), 313–318 (1974) https://doi.org/10.1016/0370-2693(74)90390-6   
[106] Moshinksy, M., Smirnov, Y.F.: The Harmonic Oscillator in Modern Physics. Contemporary Concepts in Physics, vol. 9. Harwood academic publishers GmbH, Amsterdam, The Netherlands (1996)   
[107] Kravvaris, K.: Clustering in light nuclei with configuration interaction approaches. PhD thesis, ProQuest Dissertations & Theses (2018)   
[108] Volya, A., Tchuvil’sky, Y.M.: Nuclear clustering using a modern shell model approach. Phys. Rev. C 91(4), 044319 (2015) https://doi.org/10.1103/PhysRevC.91.044319   
[109] Ichimura, M., Arima, A., Halbert, E.C., Terasawa, T.: Alpha-particle spectroscopic amplitudes and the su(3) model. Nucl. Phys. Sect. A A204(2), 225–278 (1973) https://doi.org/10.1016/0375-9474(73)90272-8   
[110] Maris, P., Vary, J.P.: Ab Initio Nuclear Structure Calculations of P-Shell Nuclei with JISP16. Int. J. Mod. Phys. E 22(07), 1330016 (2013) https://doi.org/10.1142/S0218301313300166   
[111] Kravvaris, K., Volya, A.: Clustering in structure and reactions using configuration interaction techniques. Phys. Rev. C 100(3), 034321 (2019) https://doi.org/10.1103/PhysRevC.100.034321   
[112] Trlifaj, L.: Simple formula for general oscillator brackets. Phys. Rev. C: Nucl. Phys. 5(5), 1534 (1972) https://doi.org/10.1103/PhysRevC.5.1534   
[113] Quaglioni, S., Navratil, P.: Ab initio many-body calculations of nucleon-nucleus scattering. Phys. Rev. C 79(4), 044606 (2009) https://doi.org/10.1103/PhysRevC.79.044606   
[114] Brown, B.A.: The Nuclear Shell Model towards the Drip Lines. Physics 4(2), 525–547 (2022) https://doi.org/10.3390/physics4020035   
[115] Nurmukhanbetova, A.K., Goldberg, V.Z., Nauruzbayev, D.K., Volya, A., Zholdybayev, T.K.: Study of Alpha-cluster States in (N neq Z ) Nuclei Using the TTIK Approach. Acta Phys. Pol. B Proc. Suppl. 16(2), 1 (2023) https://doi.org/10.5506/APhysPolBSupp.16.2-A16   
[116] Filippov, G.F., Lashko, Yu.A., Korennov, S.V., Kat¯o, K.: Norm Kernels and the Closeness Relation for Pauli-Allowed Basis Functions. Few-Body-Systems 33(2), 173–198 (2003) https://doi.org/10.1007/s00601-003-0009-z   
[117] Filippov, G., Lashko, Y.: Peculiar properties of the cluster-cluster interaction induced by the Pauli exclusion principle. Phys. Rev. C 70(6), 064001 (2004) https://doi.org/10.1103/PhysRevC.70.064001

[118] Lashko, Yu.A., Filippov, G.F.: Cluster structure of a low-energy resonance in tetraneutron. Phys. Atom. Nuclei 71(2), 209–214 (2008) https://doi.org/10.1134/S1063778808020014   
[119] Lashko, Yu.A., Vasilevsky, V.S., Filippov, G.F.: Properties of a potential energy matrix in oscillator basis. Annals of Physics 409, 167930 (2019) https://doi.org/10.1016/j.aop.2019.167930   
[120] Fliessbach, T., Mang, H.: Absolute values of alpha-decay rates. Nucl. Phys. A 263(1), 75 (1976) https://doi.org/10.1016/0375-9474(76)90184-6   
[121] Fliessbach, T., Manakos, P.: Alpha spectroscopic factors for light nuclei. J. Phys. G: Nucl. Phys. 3(5), 643–656 (1977) https://doi.org/10.1088/0305- 4616/3/5/012   
[122] Carey, T.A., Roos, P.G., Chant, N.S., Nadasen, A., Chen, H.L.: Alpha-clustering systematics from the quasifree ( p , p α ) knockout reaction. Phys. Rev. C: Nucl. Phys. 23(1), 576 (1981) https://doi.org/10.1103/PhysRevC.23.576   
[123] Brown, B.A., Richter, W.A.: New “USD” Hamiltonians for the $\mathit{sd}$ shell. Phys. Rev. C 74(3), 034315 (2006) https://doi.org/10.1103/PhysRevC.74.034315   
[124] Freer, M.: The clustered nucleus—cluster structures in stable and unstable nuclei. Rep, Prog, Phys, 70(12), 2149–2210 (2007) https://doi.org/10.1088/0034-4885/70/12/R03   
[125] Lubna, R.S., Kravvaris, K., Tabor, S.L., Tripathi, V., Volya, A., Rubino, E., Allmond, J.M., Abromeit, B., Baby, L.T., Hensley, T.C.: Structure of $^ { 3 8 }$ Cl and the quest for a comprehensive shell model interaction. Phys. Rev. C 100(3), 034308 (2019) https://doi.org/10.1103/PhysRevC.100.034308   
[126] Lubna, R.S., Kravvaris, K., Tabor, S.L., Tripathi, V., Rubino, E., Volya, A.: Evolution of the N=20 and 28 shell gaps and two-particle-two-hole states in the FSU interaction. Phys. Rev. Research 2(4), 043342 (2020) https://doi.org/10.1103/PhysRevResearch.2.043342   
[127] Manakos, P., Fliessbach, T., Walliser, H.: Spectroscopic alpha amplitudes in $ˆ 20 mathrm Ne $. Phys. Rev. C 27(6), 2930–2939 (1983) https://doi.org/10.1103/PhysRevC.27.2930   
[128] Anantaraman, N., Draayer, J.P., Gove, H.E., To ¯oke, J., Fortune, H.T.: Alphaparticle stripping to $^ { 2 1 }$ Ne. Phys. Rev. C: Nucl. Phys. 18(2), 815–819 (1978) https://doi.org/10.1103/PhysRevC.18.815   
[129] Tanabe, F., Tohsaki, A., Tamagaki, R.: α- $\alpha$ scattering at intermediate EnergiesApplicability of orthogonality condition model and upper limit of isoscalar meson-nucleon coupling constants inferred from potential tail. Prog. Theor. Phys. 53(3), 677 (1975) https://doi.org/10.1143/PTP.53.677   
[130] Suzuki, Y., Hecht, K.T.: Symplectic and cluster excitations in nuclei:. Nucl. Phys. A 455(2), 315–343 (1986) https://doi.org/10.1016/0375-9474(86)90021-7   
[131] Lovas, R.G., Liotta, R.J., Insolia, A., Varga, K., Delion, D.S.: Microscopic theory of cluster radioactivity. Physics Reports 294(5), 265–362 (1998) https://doi.org/10.1016/S0370-1573(97)00049-5   
[132] Varga, K., Lovas, R.G., Liotta, R.J.: Cluster-configuration shell model for alpha

decay. Nuclear Physics A 550(3), 421–452 (1992) https://doi.org/10.1016/0375- 9474(92)90017-E   
[133] Thomas, R.G.: A formulation of the theory of alpha-particle decay from time-independent equations. Prog. Theor. Phys. 12(3), 253–264 (1954) https://doi.org/10.1143/PTP.12.253   
[134] Chernykh, M., Feldmeier, H., Neff, T., von Neumann-Cosel, P., Richter, A.: Structure of the hoyle state in $^ { 1 2 }$ C. Phys. Rev. Lett. 98(3), 32501 (2007) https://doi.org/10.1103/PhysRevLett.98.032501   
[135] Raduta, Ad. R., Borderie, B., Geraci, E., Neindre, N.L., Napolitani, P., Rivet, M.F., Alba, R., Amorini, F., Cardella, G., Chatterjee, M., Filippo, E.D., Guinet, D., Lautesse, P., Guidara, E.L., Lanzalone, G., Lanzano, G., Lombardo, I., Lopez, O., Maiolino, C., Pagano, A., Pirrone, S., Politi, G., Porto, F., Rizzo, F., Russotto, P., Wieleczko, J.P.: Evidence for $\alpha$ -particle condensation in nuclei from the hoyle state deexcitation. Phys. Lett. B 705(1–2), 65–70 (2011) https://doi.org/10.1016/j.physletb.2011.10.008   
[136] Itoh, M., Ando, S., Aoki, T., Arikawa, H., Ezure, S., Harada, K., Hayamizu, T., Inoue, T., Ishikawa, T., Kato, K., Kawamura, H., Sakemi, Y., Uchiyama, A.: Further improvement of the upper limit on the direct 3α decay from the hoyle state in $\bot 2$ C. Phys. Rev. Lett. 113(10), 102501 (2014) https://doi.org/10.1103/PhysRevLett.113.102501   
[137] Smith, R., Kokalova, Tz., Wheldon, C., Bishop, J.E., Freer, M., Curtis, N., Parker, D.J.: New measurement of the direct 3α decay from the $^ { 1 2 }$ C hoyle state. Phys. Rev. Lett. 119(13), 132502 (2017) https://doi.org/10.1103/PhysRevLett.119.132502   
[138] Dell’Aquila, D., Lombardo, I., Verde, G., Vigilante, M., Acosta, L., Agodi, C., Cappuzzello, F., Carbone, D., Cavallaro, M., Cherubini, S., Cvetinovic, A., D’Agata, G., Francalanza, L., Guardo, G.L., Gulino, M., Indelicato, I., La Cognata, M., Lamia, L., Ordine, A., Pizzone, R.G., Puglia, S.M.R., Rapisarda, G.G., Romano, S., Santagati, G., Spart`a, R., Spadaccini, G., Spitaleri, C., Tumino, A.: High-precision probe of the fully sequential decay width of the hoyle state in $ˆ 12 mathrm C $. Phys. Rev. Lett. 119(13), 132501 (2017) https://doi.org/10.1103/PhysRevLett.119.132501   
[139] Alhaidari, A.D., Heller, E.J., Yamani, H.A., Abdelmonem, M.S. (eds.): The Jmatrix Method: Developments and Applications. Springer, Dordrecht (2008)   
[140] Bang, J.M., Mazur, A.I., Shirokov, A.M., Smirnov, Yu. F., Zaytsev, S.A.: P-Matrix and J-Matrix Approaches: Coulomb Asymptotics in the Harmonic Oscillator Representation of Scattering Theory. Annals of Physics 280(2), 299–335 (2000) https://doi.org/10.1006/aphy.1999.5992   
[141] Shirokov, A.M., Mazur, A.I., Mazur, I.A., Vary, J.P.: Shell model states in the continuum. Phys. Rev. C: Nucl. Phys. 94(6), 64320 (2016) https://doi.org/10.1103/PhysRevC.94.064320   
[142] Yamani, H.A., Fishman, L.: $J$ -matrix method: Extensions to arbitrary angular momentum and to coulomb scattering. J. Math. Phys. 16(2), 410–420 (1975) https://doi.org/10.1063/1.522516   
[143] Afzal, S.A., Ahmad, A.A.Z., Ali, S.: Systematic survey of the

$\alpha$ - $\alpha$ interaction. Rev. Mod. Phys. 41(1), 247–273 (1969) https://doi.org/10.1103/RevModPhys.41.247   
[144] Itagaki, N., Aoyama, S., Okabe, S., Ikeda, K.: Cluster-shell competition in light nuclei. Phys. Rev. C 70, 054307 (2004) https://doi.org/10.1103/PhysRevC.70.054307   
[145] Itagaki, N., Okabe, S.: Molecular orbital structures in $^ { 1 0 }$ Be. Phys. Rev. C 61, 044306 (2000) https://doi.org/10.1103/PhysRevC.61.044306   
[146] Itagaki, N., Okabe, S., Ikeda, K.: Important role of the spin-orbit interaction in forming the $1 / 2 ^ { + }$ orbital structure in Be isotopes. Phys. Rev. C 62, 034301 (2000) https://doi.org/10.1103/PhysRevC.62.034301   
[147] Itagaki, N., Masui, H., Ito, M., Aoyama, S.: Simplified modeling of cluster-shell competition. Phys. Rev. C 71, 064307 (2005) https://doi.org/10.1103/PhysRevC.71.064307   
[148] Suhara, T., Itagaki, N., Cseh, J., P loszajczak, M.: Novel and simple description for a smooth transition from $\alpha$ -cluster wave functions to $j j$ - coupling shell model wave functions. Phys. Rev. C 87, 054334 (2013) https://doi.org/10.1103/PhysRevC.87.054334   
[149] Itagaki, N., Naito, T.: Consistent description for cluster dynamics and single-particle correlation. Phys. Rev. C 103, 044303 (2021) https://doi.org/10.1103/PhysRevC.103.044303   
[150] Itagaki, N., Hiyama, E.: Cluster-shell competition and effect of adding hyperons. Phys. Rev. C 107, 024309 (2023) https://doi.org/10.1103/PhysRevC.107.024309