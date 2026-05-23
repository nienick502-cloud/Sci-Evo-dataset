# Interpretable deep learning for nuclear deformation in heavy ion collisions

Long-Gang Pang $^ { 1 , 2 }$ ,∗ Kai Zhou $^ { 4 , 5 }$ , and Xin-Nian Wang1,2,3

1Physics Department, University of California, Berkeley, CA 94720, USA

$^ 2$ Nuclear Science Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA

$^ 3$ Key Laboratory of Quark & Lepton Physics (MOE) and Institute of Particle Physics, Central China Normal University, Wuhan 430079, China

$^ 4$ Frankfurt Institute for Advanced Studies, 60438 Frankfurt am Main, Germany and

5Institute for Theoretical Physics, Goethe University, 60438 Frankfurt am Main, Germany

The structure of heavy nuclei is difficult to disentangle in high-energy heavy-ion collisions. The deep convolution neural network (DCNN) might be helpful in mapping the complex final states of heavy-ion collisions to the nuclear structure in the initial state. Using DCNN for supervised regression, we successfully extracted the magnitude of the nuclear deformation from event-by-event correlation between the momentum anisotropy or elliptic flow $v _ { 2 }$ ) and total number of charged hadrons $( d N _ { \mathrm { c h } } / d \eta )$ ) within a Monte Carlo model. Furthermore, a degeneracy is found in the correlation between collisions of prolate-prolate and oblate-oblate nuclei. Using the Regression Attention Mask algorithm which is designed to interpret what has been learned by DCNN, we discovered that the correlation in total-overlapped collisions is sensitive to only large nuclear deformation, while the correlation in semi-overlapped collisions is discriminative for all magnitudes of nuclear deformation. The method developed in this study can pave a way for exploration of other aspects of nuclear structure in heavy-ion collisions.

# I. INTRODUCTION

The nuclear structure plays an important role in explaining the experimental data of heavy-ion collisions [1– 13]. For example, experimental data from collisions of deformed uranium nuclei [10] are found to favor one model of initial configurations, as described by semi-classical field of gluons from each nucleons [9, 14–16], whose initial entropy deposition does not have a distinctive linear dependence on the number of binary nucleon-nucleon collisions [17]. The mysterious enhancement of triangle flow in ultra central heavy-ion collisions can be partially resolved by considering many body quantum effects in the nuclear structure [6, 8, 11]. Despite of these empirical observations, a quantitative study of nuclear structure from high-energy heavy-ion collisions is still difficult because of the complexity of the final states.

Nuclear shape deformation is one aspect of the nuclear structure that can have observable influence on the hadron spectra and correlation in the final states of heavy-ion collisions. A well established measurement of the nuclear shape deformation is the low energy Coulomb excitation [18, 19]. When deformed nuclei pass through a thin slice of lead (Pb), some of the deformed nuclei are excited and deflected by the low energy Coulomb interaction. These excited nuclei radiate low-energy gamma rays that can be used to determine the nuclear shape deformation. The shape deformation of nuclear structure is used as input for the theoretical description of heavy ion collision [1, 2, 7]. It will be interesting to know whether the output of heavy-ion collisions is sufficient to constrain the nuclear shape deformation or other parameters in the

nuclear structure despite of the highly complex and dynamical nature of the collisions.

Mapping between two sets of data is always possible through deep neural network as long as there is a continuous geometric transformation [20]. However, the power of mapping is not yet fully explored in regression tasks to map high dimensional scientific data to continuously changing control variables. If a brute force mapping using deep learning succeeds to build the connection, it can discover knowledge that may evade observation through conventional approaches. Such mapping can be made more efficient when the connection is already intuitively or evidently apparent. This is how a recent research was motivated where a deep learning system discovered the surprising connection between human gender and their retinal images [21].

In this study we would like to use deep learning to map correlations between spectral observables to the initial nuclear deformation and explore whether the information on nuclear structure is encoded in the complex output of heavy-ion collisions using a Monte Carlo model. If the connection exists, we will investigate whether the deep learning can decode this information from the output of heavy-ion collisions using supervised regression and understand what has been learned by the deep neural network.

# II. RESULTS

The nucleon density distribution of deformed nuclei can be described by the deformed Woods-Saxon distribution. The deformation is controlled by two parameters, $\beta _ { 2 }$ and $\beta _ { 4 }$ (see Eq. [1] in Section IV), as visualized in Fig. 1(a). As the deformation parameter $\beta _ { 2 }$ changes smoothly from negative to positive values, the shapes of

![](images/813a78a57ab03cab3f8f59af2c36b671c030da45d211fecc198a0ea25a4c7a79.jpg)  
(a) nuclear shape deformation

![](images/1038cee924d3070ddfafe3d7cbaf5e06573f6d0c0aa6020d349cc585ef870c99.jpg)  
(c) final states of heavy ion collisions using different deformed nuclei   
(d) attention maps learned by the deep neural network

![](images/83c09d198bacfb7e1664c00705896fbcb8afcfe47ebed685b92cd68845b04a65.jpg)

![](images/fae6664851877175a2f1c01eba8c476231601ebec5be32b08fdb0c22664dbb14.jpg)  
(b) regression performance of deep neural network

![](images/e5cdfc6a1a9809d89960e708553ac32eaff2c8a2a9a7556bbdff37126a99b5c6.jpg)

![](images/8ddadbbfe228b05bcf9702cde427562409a87016b0122b3c43250eed36cefcf7.jpg)

![](images/67240351c4aac7d1b4dc859ab3bbf4e64ed66338469922b187037b69fcb1f915.jpg)  
Figure 1: (Color-online) Determining nuclear shape deformation using deep learning. (a) The three dimensional nuclear shapes as a function of two parameters $\beta _ { 2 } \in [ - 0 . 5 , 0 . 5 ]$ and $\beta _ { 4 } \in [ - 0 . 2 , 0 . 2$ ]. (b) The regression performance of two deep convolution neural networks using the same architectures but different weights learned by setting labels to be $\beta _ { 2 }$ , $\beta _ { 4 }$ (two left figures) and $| \beta _ { 2 } |$ and $| \beta _ { 4 } |$ (two right figures). (c) The complex Monte Carlo output for collisions of different deformed nuclei. Deep learning uses these images as training and testing inputs. The x-axis represents the normalized total number of charged particles. The y-axis represents the normalized elliptic anisotropy of final state particles in momentum space. There is a degeneracy in the correlation between prolate and oblate nuclei as the network failed to predict the sign of the nuclear deformation. (d) The Regression Attention Mask helps to discover the most discriminative regions for nuclear deformation. While the “ankle" region (semi-central collisions and large $v _ { 2 }$ ) is sensitive to nuclear deformation, the “toe” region (central collisions and small $v _ { 2 }$ ) is only sensitive to large nuclear deformation $| \beta _ { 2 } | > 0 . 1 7$ .

nuclei change from oblate (pumpkin-like) to prolate (egglike). We expect different patterns both in the initial energy density distribution and final state hadron spectra for collisions of different deformed nuclei.

To determine the nuclear shape deformation, we trained a deep convolution neural network (DCCN) to predict two deformation parameters $\beta _ { 2 }$ and $\beta _ { 4 }$ from physical observables obtained through theoretical simulations of heavy ion collisions using supervised regression as shown in Fig. 1(b). The physical observable we choose

is the correlation between momentum anisotropy and total number of charged hadrons that is termed as charged multiplicity in the final state. The horizontal-axis represents the ground truth of deformation parameters and the vertical-axis represents the predictions by the deep convolution neural network. We observe that the predicted values by deep learning span a wide range from $- \beta _ { 2 }$ to $\beta _ { 2 }$ and $- \beta _ { 4 }$ to $\beta _ { 4 }$ in the left two sub-figures. The uncertainty range indicates that there is a degeneracy for the selected physical observable $F ( \beta _ { 2 } ) \approx F ( - \beta _ { 2 } )$ . As

a result, no inverse function $F ^ { - 1 }$ can map the selected physical observable to the sign of $\beta _ { 2 }$ . Knowing the degeneracy, we change our target to predict only the absolute values of the deformation parameters. This way, DCNN successfully extracted $| \beta _ { 2 } |$ with small uncertainty and $| \beta _ { 4 } |$ with medium uncertainty as shown in the right two sub-figures. The success in predicting the absolute values of the deformation parameters indicates that the nuclear deformation is encoded in the complex output of heavy ion collisions. The failure in extracting the sign of the parameters, on the other hand, indicates a degeneracy in the physical observable of the final state between prolate and oblate nuclei as discovered by the network. The statistical distributions of momentum anisotropy as a function of charged multiplicity verifies this degeneracy as shown in Fig. 1(c), where the training image for $\beta _ { 2 } ~ = ~ - 0 . 2$ is indistinguishable visually from $\beta _ { 2 } = 0 . 2$ We will refer to the region of large multiplicity and small momentum anisotropy as the “toe", and the medium multiplicity and large anisotropy as the “ankle" in the statistical distributions of momentum anisotropy as a function of charged multiplicity in Fig. 1(c).

To understand what has been learned by the deep neural network, we use “Regression Attention Mask” to highlight the most discriminative regions in the testing images as shown in Fig. 1(d). We observed that the attention mask smoothly vary from spherical nuclei to highly deformed nuclei, indicating that the network has learned self-consistent features.

The most discriminative region is the “toe" at the right bottom corner that corresponds to most central collisions. The “Regression Attention Mask” discovered this “toe" region where the attention masks become higher and wider as $| \beta _ { 2 } |$ goes from 0.17 to 0.5. The observation is consistent with physical intuition that fully overlapped tip-tip and body-body collisions of highly deformed nuclei have large momentum anisotropy fluctuations.

The “toe" region discovered by deep learning has long been proposed to be sensitive to nuclear deformation. However, results from DCNN show that the “toe” is less sensitive to small deformations when $| \beta _ { 2 } | < 0 . 1 7$ where the attention mask is very small. The regression mask also finds that the “ankle" region for semi-overlapped collisions, where $d N _ { \mathrm { c h } } / d Y | _ { \mathrm { n o r m e d } } \approx 0 . 5$ , is sensitive to both small and large nuclear deformations.

# III. DISCUSSION

Our results suggest that the nuclear shape deformation is encoded in the complex outcome of heavy-ion collisions. Supervised regression in deep learning can decode part of the information from the final state outcome. DCNN can predict the deformation parameter $| \beta _ { 2 } |$ to high accuracy. We have designed the Regression Attention Mask algorithm to locate important regions in the input image. The attention of the artificial neural network vary smoothly as the value of $| \beta _ { 2 } |$ increases. It does

not only verify the old findings that fully overlapped collisions are sensitive to large nuclear deformation, but also discovers new features in the region of semi-overlapped collisions, which work well to determine nuclear deformation both small and large.

The Regression Attention Mask is an important step towards the interpretable deep learning for science research. In the present study, the attention mask reveals interesting features that are also physically sound. For most central collisions, the attention mask finds the “toe" region to be sensitive to large deformation, which corresponds to fully overlapped tip-tip and body-body collisions. For spherical nuclei with small $| \beta _ { 2 } |$ on the other hand, spatial eccentricity is strongly correlated with collision geometry with a thin “toe". Attention mask suggests a large discriminative “ankle" region for all values of $| \beta _ { 2 } |$ , because few events have extremely small or large $v _ { 2 }$ in semi-overlapped collisions.

Much to our disappointment, deep learning fails to predict the sign of $\beta _ { 2 }$ and $\beta _ { 4 }$ , indicating a degeneracy in the physical observable from collisions between prolate and oblate nuclei. Degeneracy can be observed directly in some nuclei, for example in Kr, whose ground-state wave function is a quantum superposition of prolate and oblate shapes [22]. The degeneracy we discover in the present study is with regard to observables in the final state of high-energy heavy-ion collisions. Data from heavy-ion experiments disfavor initial-state models whose entropy density deposition is linearly proportional to the number of binary collisions. As a result, tip-tip and bodybody fully overlapped collisions produce similar numbers of charged particles and momentum anisotropy fluctuations for both prolate and oblate nuclei. It becomes clear when the 3-dimensional deformed nuclei are projected to 2-dimension by the extremely strong Lorentz contraction along the beam direction. The failure in predicting the sign of $\beta _ { 2 }$ and $\beta _ { 4 }$ using shallow and deep neural network indicates that the model is not over-fitting.

Such a degeneracy discovered by the network should not be surprising. If the physical process $F ^ { \prime }$ maps both $| \beta _ { 2 } |$ and $- | \beta _ { 2 } |$ to the same final state observable $x$ , it would be impossible for the network to find the inverse function $\beta _ { 2 } = F ^ { - 1 } ( x )$ . However, deep learning is helpful to efficiently verify the existence of an inverse function for the absolute value of $\beta _ { 2 }$ . In the present study, the network helps us to discover the existence of both the degeneracy and the inverse function $| \beta _ { 2 } | = F ^ { - 1 } ( x )$ . The sign of $\beta _ { 2 }$ and $\beta _ { 4 }$ might be determined using data from other experiments such as low energy collisions or electron-ion collisions in which one might be able to study other interesting nuclear structures such as the neutron skin, the electric charge and weak charge distribution, the pair correlation and the alpha clustering structure.

Our input images to the deep learning are the statistical information of engineered features. This is different from common computer vision problems where DCNN learns correlations between different patches of the same image. For scientific problems, the statistical informa-

tion of many input samples from the same category is used to distinguish one category from another. It is also feasible to learn features in each event and use the statistical distribution of automatically learned features for the classification or regression task.

In the present study, we only use complete and semioverlapped collisions where $v _ { 2 }$ increases linearly as the initial state spatial eccentricity increases. For peripheral collisions where $d N _ { \mathrm { c h } } / d Y | _ { \mathrm { n o r m e d } } < 0 . 5$ , $v _ { 2 }$ decreases as the spatial eccentricity continue to increase. The mapping function we used to get $v _ { 2 }$ from spatial eccentricity does not work for peripheral collisions. It is the same reason for not using higher order momentum anisotropy as part of the training input.

A thorough study may require relativistic hydrodynamic simulations of heavy-ion collisions. The 3+1D hydrodynamic simulations may provide useful information that help to quantify the shape parameters, e.g., the event-plane twist along the longitudinal direction due to forward-backward asymmetry. This asymmetry not only arise in non-central collisions, but also in central (zero impact parameter) tip-body collisions. However, extending the present work to a full (3+1)D simulation is beyond our computational capability now. This might be feasible by running the recently developed GPU-parallelized hydrodynamic code in (2+1)D mode, e.g., CLVisc [23] or GPU-VH [24]. In addition, one may improve the efficiency by selecting events with specific collision geometry provided that some regions are more discriminative in determining the nuclear shape deformation.

In summary, Monte Carlo simulations of heavy-ion collisions with various deformed nuclei reveal clear patterns in the complex final state, from which one can retrieve information about the structure of the initial state nuclei. Deep convolution neural network designed for classification is successfully used in regression task to predict the magnitude of the nuclear deformation parameters from the correlation between momentum anisotropy and total hadron multiplicity. The network reveals that there is degeneracy between the outputs of prolate (positive $\beta _ { 2 }$ ) and oblate (negative $\beta _ { 2 }$ ) heavy-ion collisions. The Regression Attention Mask algorithm helps to locate the most discriminative regions in the input image. It not only verifies that the DCNN learned the hidden structures which are sensitive to nuclear deformation, but also discovers a degeneracy in the sign of the nuclear deformation.

# IV. METHOD

Not all nuclei have a perfect spherical shape. Many nuclei have large deformations that lead to complex structures in the final state of heavy-ion collisions. For example, the collisions of prolate-shaped uranium nuclei have tip-tip, tip-body and body-body crossing patterns. The fluid dynamic expansion transfers the initial geometric eccentricity to the momentum anisotropy of the final state hadrons. As a result, the most central tip-tip col-

lisions have high multiplicity and small anisotropic flow while the body-body aligned collisions have similar multiplicity but large anisotropic flow for soft hadrons of low transverse momenta $p _ { T }$ . In this paper, we first train a 34-layer deep residual neural network [25] with squeezeexcitation blocks [26] to predict the shape deformation parameter of deformed nuclei using regression. Then we use the “Regression Attention Mask ” to interpret what has been learned by the deep neural network.

# A. Collisions of deformed nuclei

We use the Trento Monte Carlo model [27] to provide IP-Glasma-like fluctuating initial conditions of heavy-ion collisions. The shapes of deformed nuclei are given by the deformed Woods-Saxon distribution,

$$
\rho (r, \theta , \phi) = \frac {\rho_ {0}}{1 + e ^ {(r - R _ {0} (1 + \beta_ {2} Y _ {2 0} (\theta) + \beta_ {4} Y _ {4 0} (\theta))) / a}} \quad (1)
$$

where $\rho _ { 0 }$ is the nucleon density in nucleus, $R _ { 0 }$ is the Woods-Saxon radius, $\beta _ { 2 }$ and $\beta _ { 4 }$ are the deformation parameters introduced via an expansion in spherical harmonics, $\begin{array} { r } { Y _ { 2 0 } = \frac { \sqrt { 5 } } { 4 \sqrt { \pi } } ( 3 \cos ^ { 2 } \theta - 1 ) } \end{array}$ , $\begin{array} { r } { Y _ { 4 0 } = \frac { 3 } { 1 6 \sqrt { \pi } } ( 3 5 \cos ^ { 4 } \theta - } \end{array}$ $3 0 \cos ^ { 2 } \theta + 3 )$ and $a$ is the Woods-Saxon tail width.

The orientations of the colliding nuclei are given by Euler rotations with random angles $( \alpha , \beta , \gamma )$ .

$$
R (\alpha , \beta , \gamma) = R _ {z} (\gamma) R _ {y} (\beta) R _ {z} (\alpha) \tag {2}
$$

where $R _ { z } ( \alpha )$ is the first rotation along $\mathbf { Z }$ -axis, $R _ { y } ( \beta )$ is the second rotation along y-axis and $R _ { z } ( \gamma )$ is the third rotation along the original z-axis. Because the deformed nuclei are symmetric along the z-axis, the first rotation $R _ { z } ( \alpha )$ can be ignored. To make sure the sampled rotations are isotropic, the tilt angle $\theta$ along y-axis is sampled according to a uniform distribution $\cos ( \theta ) \in U [ - 1 , 1 )$ , whereas the spin angle $\phi$ along z-axis is sampled according to a uniform distribution $\phi \in U [ 0 , 2 \pi )$ .

We prepare 51x51=2601 groups of deformed uranium nucleus with 51 $\beta _ { 2 } \in [ - 0 . 5 , 0 . 5 ]$ and 51 $\beta _ { 4 } \in [ - 0 . 2 , 0 . 2 ]$ . For each group, we simulate 100000 collisions with all possible collision geometries determined by the orientation of each nucleus and the impact parameter (the transverse distance between the center of two colliding nuclei). From these collisions we further select half of the events with highest total entropy, which corresponds to centrality range $0 - 5 0 \%$ .

In experiments, the directly accessible information is the number of final state charged hadrons at mid-rapidity $d N _ { \mathrm { c h } } / d Y \vert _ { Y = 0 }$ and the momentum anisotropy $v _ { 2 }$ of final state hadrons. It is shown in many studies that $d N _ { \mathrm { c h } } / d Y \vert _ { Y = 0 }$ is proportional to the total entropy density $s _ { 0 }$ of the initial state. The anisotropy $v _ { 2 }$ can be approximately computed from the geometric eccentricity of the initial state $\varepsilon _ { 2 } = \langle y ^ { 2 } - x ^ { 2 } \rangle / \langle y ^ { 2 } + x ^ { 2 } \rangle$ , where $x$ and $y$ are the transverse coordinates in the overlapped regions of collision, $\langle \cdots \rangle$ represents weighted average where weights are

given by the local entropy density $s ( x , y )$ . The geometric eccentricity in initial state transforms to momentum anisotropy in the final state through relativistic hydrodynamic expansion of the strongly coupled quark gluon plasma. To make the current method directly applicable to experiment, we match the $\varepsilon _ { 2 }$ to $v _ { 2 }$ through a heuristic equation [28, 29],

$$
v _ {2} = k _ {2} \varepsilon_ {2} + k _ {2} ^ {\prime} \varepsilon_ {2} ^ {3} + \delta_ {2} \tag {3}
$$

where the coefficients $k _ { 2 } = 0 . 2$ , $k _ { 2 } ^ { \prime } = 0 . 1$ and $\delta _ { 2 }$ is the residual that introduces additionally $\pm 1 0 \%$ uniformlydistributed random fluctuations.

The total entropy is self-normalized with the mean entropy of the $0 - 1 \%$ most central collisions for each nuclear shape deformation. The self-normalization makes the method applicable to experimental data because

$$
\left. d N _ {\mathrm {ch}} / d Y \right| _ {\text {normed}} = \frac {d N _ {\mathrm {ch}} / d Y}{\langle d N _ {\mathrm {ch}} / d Y \rangle_ {0 \sim 1 \%}} \approx \frac {s _ {0}}{\langle s _ {0} \rangle_ {0 - 1 \%}}. \tag{4}
$$

We now have 2601 groups of $( d N _ { \mathrm { c h } } / d Y | _ { \mathrm { n o r m e d } } , v _ { 2 } )$ distributions. The data are divided into 3 groups, $8 0 \%$ for training, 10% for validating and 10% for testing. We use data augmentation to enlarge the size of the training data set. For each distribution, we randomly sample 90% from 50000 data points to create a new image. The data augmentation produces 160000 images for training, 16000 for validating and 16000 for testing.

# B. Deep regression network

![](images/76d222bc6e50ed767104b27077948b016f16533f75834e29c3d69396878265fb.jpg)

![](images/ab399ce3f2c24aa434756b4b4d153e6664b1c0ecd32d99bb9f5dadb95b616f58.jpg)

![](images/26a4b5601d9aceea9fe036dd2ad159097c4317e1dd04a2c83c6857949cf06274.jpg)  
Figure 2: (Color-online) The architecture of the 34-layer regression neural network using residual and squeeze excitation blocks.

Shown in Fig. 2 is the 34-layer deep convolution neural network for the regression task. The residual blocks make it possible to design deep convolution neural network for image classifications. And the squeeze excitation operation additionally pushes the image classification to the state-of-the-art. We verify that the deep

residual neural network designed for image classification also works well on regression task. Our inputs are images of 2 dimensional event-by-event distributions of $( d N _ { \mathrm { c h } } / d Y | _ { \mathrm { n o r m e d } } , v _ { 2 } / v _ { 2 \mathrm { m a x } } )$ in $5 6 \times 5 6$ bins. The input image is first processed using a two-dimensional convolution, then it is fed to a type-I residual box containing 3 blocks named Residual Block-I, where the output feature maps have the same transverse size as the input image. The resulted feature maps are fed to four type-II residual boxes consecutively. Each type-II residual box has 3 to 6 blocks named Residual Block-II. The first Residual Block-II in each box reduces the width and height of the input feature map by a factor of 2. All the residual blocks have one “add” operation and the last “add” layer has a name “add_16”. Each residual block has 2 Conv2D layers and in total they contribute to $1 6 \times 2 = 3 2$ convolution layers. We have used global average pooling layer [30] to get the mean of each feature map with size $7 \times 7$ for the 512 channels. This 512 neurons are connected to 2 neurons in the output layer to make predictions for the nuclear deformation parameter $| \beta _ { 2 } |$ and $| \beta _ { 4 } |$ . One reason to use this deep residual neural network is to verify whether a deep network can learn the sign of the parameter $\beta _ { 2 }$ where a shallow network has already failed. The residual neural network also has better interpretability than VGG-like network as shown in the paper [31].

# C. Regression Attention Mask for interpretable deep learning

Interpretability is the most indispensable consideration of the deep neural networks when it is used in science researches, as well as self-driving cars, medical diagnosis and government policy making. The interpretability is defined as the ability to explain or to present in understandable terms to a human [32]. Visualization, verbal explanation and clustering of similar instances are all understandable representations of the deep neural networks with Interpretability.

There are many ways to visualize what has been learned by the network classifier. For reviews see the book “Interpretable Machine Learning” [33] and surveys [32, 34–36]. There are global explanations that explain the network in the whole input space by visualizing what each feature map learns. There are also local explanations that explain local features in one specific image. We have designed the “Regression Attention Mask” algorithm, which provides a local interpretation of a given image.

For the global explanation, deconvolution is used to visualize each feature map of the deep convolution neural network [37–40]. For the local explanation, there are many different methods developed based on the assumption that one highly complex machine learning model can be locally approximated by a linear model around one given input image. One way to construct the importance map is to measure the probability changes with parts

of the image occluded [41, 42] or similar pixels/superpixels (LIME) masked [43]. Different from our method, those occlusion methods depend on manually constructed masks of input images.

Saliency map is another way to explain the pre-trained convolution neural network around one given image [30]. It assumes that the predicted class score can be approximated by a linear function $f ( x ) \approx w \circ x + b$ around one given image $x$ in the input space, where $f$ is the function learned by the network. The gradient $w = \partial f / \partial x$ represents the importance of each pixel. However, the original saliency map is noisy [30] due to negative gradients and non-linear dependences on $x$ . The improved saliency map uses guided back-propagation [44] to maximize the class score of one given class by dropping negative influences. These gradient based methods as well as many alternatives [45–47] are sensitive to constant shift [48] except the pattern net [49, 50]. The interpretability of all different saliency maps can be quantified using our “Regression Attention Mask ” method.

What is closely related to our method is the class activation map where locations in the feature maps of the last convolution layer are matched to the input image [51, 52]. We have discarded the RELU activation function in the gradient weighted class activation map to get our specific activation map for regression tasks. RELU pick positive influence to enlarge the class score while regression needs both positive and negative components in the activation map to reproduce the regression value. The regression activation map is used to create “Regression Attention Mask”.

Based on the class activation map, the class activation mask is invented to quantify the interpretability of different neural networks. The class activation mask is a two-dimensional image that has the same size as the input image. It has only one channel and its pixel values are initialized with 0. Pixels are set to 1 if corresponding regions in class activation map have values larger than some threshold. The interpretability of one classifier is quantified by the intersection over union score between the class activation mask and human understandable concept-segmentation, e.g., human labeled masks for an object, part, scene, material, texture and color [31]. The interpretability has the order ResNet $>$ VGG $>$ GoogLeNet $>$ AlexNet regarding different network architectures. Different from that method, we propose to use prediction difference of the masked image to quantify the interpretability in the regression network.

To disentangle hidden representations of the learned feature maps, studies in Refs. [53] and [54] use graphs, decision trees and local part template. Recently a deep neural network has been trained to jointly classify images into categories and provide its reasoning [55]. Our framework provides an explanation about its decisions in the regression task and helps us to understand the features of the correlation in determination of the nuclear deformation.

For classification task, the importance of each pixel to classification can be computed using the gradient weighted class activation map (Grad-CAM),

$$
\operatorname {g r a d c a m} (x) = \frac {1}{c \times k \times k} \sum_ {n = 1} ^ {c} A ^ {n} \sum_ {i, j = 1} ^ {k} \frac {\partial f}{\partial A _ {i j} ^ {n}} \tag {5}
$$

where $x$ is the input image, $c$ is the number of channels, $k$ is the size of the activation map, $f$ is the class score, $A _ { i j } ^ { n }$ is the pixel value of the $n$ th activation map $A ^ { n }$ in layer “add_16” at site $( i , j )$ . The class activation map is scaled up to the same size as the input image by upsampling. In the original grad-cam paper, the weighted class activation map is forwarded to a ReLU activation function to remove negative contributions. Otherwise the positive influence on one class might be equally negative on the other to cancel the important regions, when the prediction probabilities are close for the top-2 classes. However, both positive and negative contributions are required to reproduce the regression value. Different from the original grad-cam algorithm, the ReLU activation function in our algorithm is removed to adapt to the regression task.

The attention mask for input image $x _ { i }$ is defined as $m _ { i } = g r a d c a m ( x _ { i } ) > T$ where $T$ is the threshold. In the present study, the threshold $T$ is set to the mean value of the given mask. Since the input images have similar structure for the same $\beta _ { 2 }$ and $\beta _ { 4 }$ , we compute the averaged attention mask $\begin{array} { r } { m = \sum _ { i } w _ { i } m _ { i } } \end{array}$ , for all events in the range $\in [ | \beta _ { 2 } | , | \beta _ { 2 } | + 0 . 0 2 ]$ , weighted by $w _ { i }$ ,

$$
w _ {i} = \frac {\exp [ - \sigma_ {i} ]}{\sum_ {j} \exp [ - \sigma_ {j} ]}, \quad \sigma_ {i} = | | f (m _ {i} \circ x _ {i}) - f (x _ {i}) | |, \tag {6}
$$

where $x _ { i }$ is the ith input image, $m _ { i }$ is the attention mask of the trained regression network. The $m _ { i } \mathrm { ~ o ~ } x _ { i }$ is the pixel-wise multiplication between the attention mask and the input image, which helps to occlude unimportant regions. Feeding the original image $x _ { i }$ and the occluded image $m _ { i } \mathrm { ~ O ~ } x _ { i }$ to the regression network $f$ helps to get the prediction difference $\sigma _ { i }$ . Smaller prediction difference indicates better attention mask that leads to higher weight $w _ { i }$ .

# ACKNOWLEDGMENTS

We thank Volker Koch, Jorgen Randrup, Feng Yuan and Xin Dong for helpful discussions. This work is supported by DOE under Contract No. DE-AC02- 05CH11231, by NSF under Grant No. ACI-1550228 within the JETSCAPE Collaboration, by NSFC under Grant No. 11861131009 and No. 11890714, by BMBF under the ErUM-Data project and the AI research grant of SAMSON AG, Frankfurt. Computations are performed on GPU workstations at CCNU and DOE NERSC.

[1] Ulrich W. Heinz and Anthony Kuhlman. Anisotropic flow and jet quenching in ultrarelativistic U + U collisions. Phys. Rev. Lett., 94:132301, 2005.   
[2] Anthony J. Kuhlman and Ulrich W. Heinz. Multiplicity distribution and source deformation in full-overlap U+U collisions. Phys. Rev., C72:037901, 2005.   
[3] Peter Filip, Richard Lednicky, Hiroshi Masui, and Nu Xu. Initial eccentricity in deformed Au-197 + Au-197 and U-238 + U-238 collisions at sNN=200 GeV at the BNL Relativistic Heavy Ion Collider. Phys. Rev., C80:054903, 2009.   
[4] Sergei A. Voloshin. Testing the Chiral Magnetic Effect with Central U+U collisions. Phys. Rev. Lett., 105:172301, 2010.   
[5] Andy Goldschmidt, Zhi Qiu, Chun Shen, and Ulrich Heinz. Collision geometry and flow in uranium + uranium collisions. Phys. Rev., C92(4):044903, 2015.   
[6] M. Alvioli, H. Holopainen, K. J. Eskola, and M. Strikman. Initial state anisotropies and their uncertainties in ultrarelativistic heavy-ion collisions from the Monte Carlo Glauber model. Phys. Rev., C85:034902, 2012.   
[7] P. Filip. Ground-State Properties Of Nuclei And Initial State In Relativistic Heavy Ion Collisions. In Proceedings, 11th International Workshop Relativistic Nuclear Physics: from Hundreds of MeV to TeV: Stara Lesna, Slovak Republik, June 17-23, 2012, page 111, 2013.   
[8] G. S. Denicol, C. Gale, S. Jeon, J. F. Paquet, and B. Schenke. Effect of initial-state nucleon-nucleon correlations on collective flow in ultra-central heavy-ion collisions. 2014.   
[9] Bjoern Schenke, Prithwish Tribedy, and Raju Venugopalan. Initial-state geometry and fluctuations in Au+Au, Cu+Au, and U+U collisions at energies available at the BNL Relativistic Heavy Ion Collider. Phys. Rev., C89(6):064908, 2014.   
[10] L. Adamczyk et al. Azimuthal anisotropy in U+U and Au+Au collisions at RHIC. Phys. Rev. Lett., 115(22):222301, 2015.   
[11] M. Alvioli and M. Strikman. Neutron skin effect in W+ and W $-$ production in high-energy proton-lead collisions. 2018.   
[12] Maciej Rybczyński, Milena Piotrowska, and Wojciech Broniowski. Signatures of $\alpha$ clustering in ultrarelativistic collisions with light nuclei. Phys. Rev., C97(3):034912, 2018.   
[13] J. Noronha-Hostler, N. Paladino, S. Rao, Matthew D. Sievert, and Douglas E. Wertepny. Ultracentral Collisions of Small and Deformed Systems at RHIC: $U U$ , $d A u$ , $^ { \mathrm { { s } } } B e A u$ , $^ { 9 } B e ^ { 9 } B e$ , $^ 3 H e ^ { 3 } H e$ , and $^ 3 H e A u$ Collisions. 2019.   
[14] Larry D. McLerran and Raju Venugopalan. Computing quark and gluon distribution functions for very large nuclei. Phys. Rev., D49:2233–2241, 1994.   
[15] Larry D. McLerran and Raju Venugopalan. Gluon distribution functions for very large nuclei at small transverse momentum. Phys. Rev., D49:3352–3355, 1994.   
[16] Bjoern Schenke, Prithwish Tribedy, and Raju Venugopalan. Event-by-event gluon multiplicity, energy density, and eccentricities in ultrarelativistic heavy-ion collisions. Phys. Rev., C86:034908, 2012.   
[17] Michael L. Miller, Klaus Reygers, Stephen J. Sanders, and Peter Steinberg. Glauber modeling in high energy

nuclear collisions. Ann. Rev. Nucl. Part. Sci., 57:205– 243, 2007.   
[18] H. Morinaga and P.C. Gugelot. Gamma rays following (α, xn) reactions. Nuclear Physics, 46:210 – 224, 1963.   
[19] D Cline. Nuclear shapes studied by coulomb excitation. Annual Review of Nuclear and Particle Science, 36(1):683–716, 1986.   
[20] Francois Chollet. Deep Learning with Python. Manning Publications Co., Greenwich, CT, USA, 1st edition, 2017.   
[21] Ryan Poplin, Avinash V. Varadarajan, Katy Blumer, Yun Liu, Michael V. McConnell, Greg S. Corrado, Lily Peng, and Dale R. Webster. Prediction of cardiovascular risk factors from retinal fundus photographs via deep learning. Nature Biomedical Engineering, 2(3):158–164, 2018.   
[22] E. Clement et al. Shape coexistence in neutron-deficient krypton isotopes. Phys. Rev., C75:054313, 2007.   
[23] Long-Gang Pang, Hannah Petersen, and Xin-Nian Wang. Pseudorapidity distribution and decorrelation of anisotropic flow within the open-computing-language implementation CLVisc hydrodynamics. Phys. Rev., C97(6):064918, 2018.   
[24] Dennis Bazow, Ulrich W. Heinz, and Michael Strickland. Massively parallel simulations of relativistic fluid dynamics on graphics processing units with CUDA. Comput. Phys. Commun., 225:92–113, 2018.   
[25] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. CoRR, abs/1512.03385, 2015.   
[26] Jie Hu, Li Shen, and Gang Sun. Squeeze-and-excitation networks. CoRR, abs/1709.01507, 2017.   
[27] J. Scott Moreland, Jonah E. Bernhard, and Steffen A. Bass. Alternative ansatz to wounded nucleon and binary collision scaling in high-energy nuclear collisions. Phys. Rev., C92(1):011901, 2015.   
[28] Fernando G. Gardim, Frederique Grassi, Matthew Luzum, and Jean-Yves Ollitrault. Mapping the hydrodynamic response to the initial geometry in heavy-ion collisions. Phys. Rev., C85:024908, 2012.   
[29] Jacquelyn Noronha-Hostler, Li Yan, Fernando G. Gardim, and Jean-Yves Ollitrault. Linear and cubic response to the initial eccentricity in heavy-ion collisions. Phys. Rev., C93(1):014909, 2016.   
[30] Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. Deep inside convolutional networks: Visualising image classification models and saliency maps. CoRR, abs/1312.6034, 2013.   
[31] David Bau, Bolei Zhou, Aditya Khosla, Aude Oliva, and Antonio Torralba. Network dissection: Quantifying interpretability of deep visual representations. In Computer Vision and Pattern Recognition, 2017.   
[32] Finale Doshi-Velez and Been Kim. Towards A Rigorous Science of Interpretable Machine Learning. arXiv e-prints, page arXiv:1702.08608, Feb 2017.   
[33] Christoph Molnar. Interpretable Machine Learning, A Guide for Making Black Box Models Explainable. 2019.   
[34] Quan shi Zhang and Song chun Zhu. Visual interpretability for deep learning: a survey. Frontiers of Information Technology & Electronic Engineering, 19(1):27–39, Jan 2018.   
[35] Riccardo Guidotti, Anna Monreale, Franco Turini, Dino

Pedreschi, and Fosca Giannotti. A survey of methods for explaining black box models. CoRR, abs/1802.01933, 2018.   
[36] A. Adadi and M. Berrada. Peeking inside the black-box: A survey on explainable artificial intelligence (xai). IEEE Access, 6:52138–52160, 2018.   
[37] Dumitru Erhan, Y Bengio, Aaron Courville, and Pascal Vincent. Visualizing higher-layer features of a deep network. Technical Report, UniveristÃc de MontrÃc al, 01 2009.   
[38] Matthew D. Zeiler and Rob Fergus. Visualizing and understanding convolutional networks. CoRR, abs/1311.2901, 2013.   
[39] Chris Olah, Alexander Mordvintsev, and Ludwig Schubert. Feature visualization. Distill, 2017. https://distill.pub/2017/feature-visualization.   
[40] Chris Olah, Arvind Satyanarayan, Ian Johnson, Shan Carter, Ludwig Schubert, Katherine Ye, and Alexander Mordvintsev. The building blocks of interpretability. Distill, 2018. https://distill.pub/2018/building-blocks.   
[41] Marko Robnik-Šikonja and Igor Kononenko. Explaining classifications for individual instances. IEEE Trans. on Knowl. and Data Eng., 20(5):589–600, May 2008.   
[42] Luisa M. Zintgraf, Taco S. Cohen, Tameem Adel, and Max Welling. Visualizing deep neural network decisions: Prediction difference analysis. CoRR, abs/1702.04595, 2017.   
[43] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. "why should I trust you?": Explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, August 13-17, 2016, pages 1135–1144, 2016.   
[44] Jost Tobias Springenberg, Alexey Dosovitskiy, Thomas Brox, and Martin A. Riedmiller. Striving for simplicity: The all convolutional net. CoRR, abs/1412.6806, 2014.   
[45] Mukund Sundararajan, Ankur Taly, and Qiqi Yan. Axiomatic attribution for deep networks. CoRR, abs/1703.01365, 2017.   
[46] Mariusz Bojarski, Anna Choromanska, Krzysztof Choromanski, Bernhard Firner, Larry D. Jackel, Urs Muller,

and Karol Zieba. Visualbackprop: visualizing cnns for autonomous driving. CoRR, abs/1611.05418, 2016.   
[47] K. Fu, W. Dai, Y. Zhang, Z. Wang, M. Yan, and X. Sun. Multicam: Multiple class activation mapping for aircraft recognition in remote sensing images. Remote Sens, 11(544), 2019.   
[48] Pieter-Jan Kindermans, Sara Hooker, Julius Adebayo, Maximilian Alber, Kristof T. Schütt, Sven Dähne, Dumitru Erhan, and Been Kim. The (Un)reliability of saliency methods. arXiv e-prints, page arXiv:1711.00867, Nov 2017.   
[49] Grégoire Montavon, Sebastian Bach, Alexander Binder, Wojciech Samek, and Klaus-Robert Müller. Explaining nonlinear classification decisions with deep taylor decomposition. CoRR, abs/1512.02479, 2015.   
[50] Pieter-Jan Kindermans, Kristof T. Schütt, Maximilian Alber, Klaus-Robert Müller, Dumitru Erhan, Been Kim, and Sven Dähne. Learning how to explain neural networks: PatternNet and PatternAttribution. arXiv eprints, page arXiv:1705.05598, May 2017.   
[51] B. Zhou, A. Khosla, Lapedriza. A., A. Oliva, and A. Torralba. Learning Deep Features for Discriminative Localization. CVPR, 2016.   
[52] Ramprasaath R. Selvaraju, Abhishek Das, Ramakrishna Vedantam, Michael Cogswell, Devi Parikh, and Dhruv Batra. Grad-cam: Why did you say that? visual explanations from deep networks via gradient-based localization. CoRR, abs/1610.02391, 2016.   
[53] Feng Shi Ying-Nian Wu Quan-Shi Zhang, Rui-Ming Cao and Song-Chun Zhu. Interpreting cnn knowledge via an explanatory graph. In TThe Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18), Febrary 2018.   
[54] Quan-Shi Zhang, Ying-Nian Wu, and Song-Chun Zhu. Interpretable convolutional neural networks. In The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2018.   
[55] Atsushi Kanehira and Tatsuya Harada. Learning to explain with complemental examples. CoRR, abs/1812.01280, 2018.