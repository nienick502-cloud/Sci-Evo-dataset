# Voting in Transfer Learning System for Ground-Based Cloud Classification

Mario Manzo

IT Services, University of Naples “L’Orientale”

80121, Naples, Italy, mmanzo@unior.it

Simone Pellino

Department of Applied Science,

I.S. Mattei Aversa 81031, M.I.U.R. Rome, Italy; simonepellino@gmail.com

# Abstract

Clouds classification is a great challenge in meteorological research. The different types of clouds, currently known and present in our skies, can produce radioactive effects that impact on the variation of atmospheric conditions, with the consequent strong dominance over the earth’s climate and weather. Therefore, identifying their main visual features becomes a crucial aspect. In this paper, the goal is to adopt a pretrained deep neural networks based architecture for clouds image description, and subsequently, classification. The approach is pyramidal. Proceeding from the bottom up, it partially extracts previous knowledge of deep neural networks related to original task and transfers it to the new task. The updated knowledge is integrated in a voting context to provide a classification prediction. The framework trains the neural models on unbalanced sets, a condition that makes the task even more complex, and combines the provided predictions through statistical measures. Experimental phase on different cloud image datasets is performed and results achieved show the effectiveness of the proposed approach with respect to state of the art competitors.

Keywords: Cloud classification, Deep learning, Transfer learning, Voting-based classification, Climate change

# 1. Introduction

Clouds are a constant presence in our skies, combined with the role assumed by ecosystems, are also important in determining atmospheric conditions, hours of sunshine and temperature. Nowadays, dynamics atmospheric conditions, attributed to climate change, have led to an increase in attention to behavior of clouds Duda et al. (2013). Climate models allow to predict the climate changes, but their precision degree is currently insufficient and attributable to the alteration in the conditions determined by different phenomena. Consequently, clouds behavior prediction is important for estimating climate change. Furthermore, cloud changes are also a reason for influences on the earth radiation budget and energy balance Rossow and Schiffer (1991); Chen et al. (2000); Stephens (2005). A great deal of effort has been made by the scientific community to acquire many datasets, but not fully managed due to a lack of devices with adequate processing resources. In recent years, however, the state of the art has seen the birth of numerous studies and analyzes that can automate clouds attributes and classes detection scientifically relevant. Due to the amount of ground cloud images, the recognition phase has been extensively studied lately in the literature. Most of the standard algorithms adopt hand-made features, such as brightness, texture, shape, and color, to represent image content but without obtaining a model generalization due to the complex distribution of data. Indeed, the visual information contained in the image are unable to accurately describe the clouds due to the large variations in appearance. Finally, the non-visual features, also known as multimodal information, obtainable from the clouds process formation such as temperature, humidity, pressure and wind speed can be of help. According to recent studies, deep learning has proven effective for image management, analysis, representation and classification also in cloud recognition field. In particular, the success of deep neural networks, applied to the image classification task, concern several interesting aspects mainly connected to the software development and the large amount of data available. Specifically, for cloud images analysis, deep neural networks are adopted both in the segmentation and detection phases. However, image content and poor data balance among classes have a decisive impact on performance, causing uncertainty in the model generalization. With purpose to address the above problems, we present a framework based on deep transfer and voting learning for cloud image classification. It is built based on three steps. A first, which performs image preprocessing operations such as

resizing, essential for neural networks training. A second, which modifies and retrains multiple deep neural networks, exploiting previous knowledge. A third, which looks at the different predictions provided by the deep neural networks and combines them in order to provide the best decision in the classification phase. The main contributions about proposed framework can be summarized in some keypoints. First, a framework based on deep and voting learning designed to address the imbalance between classes in the cloud recognition task. Second, a framework built on multiple classification models based on deep transfer learning. Third, the demonstration that several models, suitably combined, can strengthen the decision in classification with respect to a single one. Finally, experimental demonstrations compared to established existing methods on the datasets recognized by field experts. The paper is structured as follows. Section 2 provides an overview of state of art about clouds classification approaches. Section 3 describes in detail proposed framework. Section 4 provides a wide experimental phase, while section 5 concludes the paper.

# 2. Related Work

In this section, we briefly describe the most important studies about clouds images classification in literature. In this field, numerous works address the task according to different aspects such as image characterization, segmentation algorithm application to get new descriptors, complex mechanisms of learning and classification and much more.

In Liu et al. (2018) authors present a layer named joint fusion (JFCNN) to jointly learn two kinds of cloud features under one framework. After training the proposed JFCNN, they extract the visual and multimodal features from two subnetworks, which are based on the well known Resnet50 He et al. (2016) and integrate them using a weighted strategy. The architecture consists of five parts: two subnetworks, one joint fusion layer, one FC layer and the loss function. The subnetworks are used for learning cloud visual features. Authors work with two kind of extracted features, combined in multimodal way, which contain some complementary information and different characteristics of the ground-based cloud.

An approach named multi-evidence and multi-modal fusion network (MMFN) is proposed in Liu et al. (2020b). The idea is to learn extended cloud information by fusing heterogeneous features (global and local) in a unified framework. MMFN takes advantage of multiple pieces of evidence using a main

network and an attentive network. In the attentive network, local visual features are extracted from attentive maps which are obtained by refining salient patterns from convolutional activation maps. Meanwhile, the main network learns multi-modal features for ground-based cloud. In order to combine the multi-modal and multi-evidence visual features, authors design two fusion layers in MMFN to incorporate multi-modal features with global and local visual features, respectively.

In Shi et al. (2017) authors propose to use deep convolutional activationsbased features (DCAFs). Cloud images are directly fed into a CNN model. Then, the features from different convolutional and FC layers are extracted through different pooling strategies. Finally, a multilabel linear support vector machine (SVM) model is used for the classification step.

A convolutional neural network model, called CloudNet, for accurate ground-based meteorological cloud classification is proposed in Zhang et al. (2018). The model consists in five convolutional layers and two FC layers. In addition, to optimize the network training, the image input is processed through a robust strategy that subtracts the mean red-green-blue value of each pixel over the training set to improve training speed and accuracy. Furthermore, the authors have created a clouds dataset, called Cirrus Cumulus Stratus Nimbus (CCSN), which consists of 11 categories under meteorological standards.

In Liu and Li (2018) authors propose an approach named deep multimodal fusion (DMF). In order to learn the visual features, CNN models have been applied to capture texture information. The extracted features, from deeper layers, have several eligible properties such as invariance and discrimination. Subsequently authors employ a weighted strategy to integrate visual and multimodal features. Finally, SVM algorithm to train the classification model is adopted.

In Li et al. (2020) a deep tensor fusion network is presented in order to hold spatial information of ground-based cloud images. It fuses cloud visual and multimodal features at the tensor level.

In Liu et al. (2019) author propose a approach, called Hierarchical Multimodal Fusion (HMF), which fuses deep multimodal and deep visual features in different levels. The architecture is composed of two subnetworks, visual subnetwork and multimodal subnetwork. The visual subnetwork is defined in order to extract deep visual features from ground-based cloud images employing Resnet50 He et al. (2016). The multimodal subnetwork is used to learn features from a vector composed of six FC layers. Classification step

through SVM is managed.

In Sun et al. (2009) author propose a classification method of sky-condition based on whole sky infrared cloud images, where the Local Binary Patterns operator (LBP) and the contrast of local cloud image texture (VAR signal) are combined to classify sky conditions. The correspondence relationship among traditional cloud classes and instrument-measured cloud classes is suggested. The approach analyzes the LBP spectra and VAR characteristics for five classes of clouds.

An automatic cloud classification algorithm is developed in Heinle et al. (2010), the approach uses a image-mask created by visually identifying image regions containing discriminative information. Furthermore the approach extracts a set of mainly statistical features describing the color as well as the texture of an image. Classification step adopts the k-nearest neighbour algorithm.

A modified texton-based classification approach that integrates both color and texture information to improve classification results is proposed in Dev et al. (2015). Color channel is adopted to generate image descriptors and filter responses of images across all the categories aggregating them together. Kmeans clustering is applied on the concatenated filter responses, producing the different cluster centers. These clusters centers are the modified-textons and constitute the texton dictionary. The discriminative histogram model for each image category is generated by comparing the filter responses of the pixels with the generated textons in the dictionary.

An ensemble learning method and resource allocation scheme for cloud observation and classification is proposed in Zhang et al. (2020). Ensemble methods, like Bagging, AdaBoost and Snapshot are used as a base classifier to take the cross-semantic and structure features of cloud images.

# 3. Materials and Methods

In this section we describe the proposed framework which includes two methodologies: deep neural networks Liu et al. (2017) and voting learning Peteiro-Barral and Guijarro-Berdi˜nas (2013). The goal is to combine several deep neural networks with purpose to classify clouds images. Specifically, a set of competitive models are aligned and provide a range of confidential decisions useful for making choices during classification. The framework is composed of three blocks. A first, which performs preprocessing in terms

of image resize. A second, which learns different deep neural networks, previously redesigned for the specific task. A third, which combines different potential indications, through voting rules, provided by deep neural networks for classification purpose. Finally, the framework runs a predetermined number of iterations in a supervised learning context.

# 3.1. Image resize

One of the drawbacks of neural networks concerns the fixed dimension about the input layer with reference to the images to be processed (details about adopted neural networks can be found in table 1 at column 5). Size normalization, according to the input layer dimension, is essential because it is not possible to process different or large sized images for the network training and classification stages. This step does not alter the content of the image information in any way.

# 3.2. Network design and transfer learning

The transfer learning has been selected as training strategy. The basic idea is to transfer the knowledge extracted from a source domain to a destination one, in our case clouds classification. Generally, a pretrained network is chosen as starting point in order to learn a new task. It turns out to be the most convenient and forthcoming solution to adopt the representational power of pretrained deep neural networks. Clearly, it is easy and fast to tune a network with transfer learning than training a new network from scratch with randomly initialized weights. For clouds recognition, deep learning architectures are selected based on their task compliance. The goal is to train networks on images by redesign their structures in the final layer according to different outgoing classes. Table 1 supports the description below about adopted neural models.

Alexnet Krizhevsky et al. (2012) consists of 5 convolutional layers and 3 fully connected layers. It includes the non-saturating ReLU activation function, better then tanh and sigmoid during training phase.

Googlenet Szegedy et al. (2015) is composed of 22 deep layers. The network is inspired by LeNet LeCun et al. (1989) but implemented a novel element which is dubbed an inception module. This module is based on several very small convolutions in order to drastically reduce the number of parameters. The architecture reduced the number of parameters from 60 million (AlexNet) to 4 million. Furthermore, it includes batch normalization, image distortions and Root Mean Square Propagation algorithm.

Densenet201 Huang et al. (2017) is a convolutional neural network with 201 deep layers. Unlike standard convolutional networks composed of $L$ layers with $L$ one-to-one connections between the current layers and the nexts, it contains $\textstyle { \frac { L ( L + 1 ) } { 2 } }$ direct connections. Specifically, each layer adopts the feature-maps of all preceding layers and its own feature-maps into all subsequent layers as inputs.

Resnet18 and Resnet50 He et al. (2016) are inspired by pyramidal cells contained in the cerebral cortex. They use particular skip connections or shortcuts to jump over some layers. They are composed of 18 and 50 deep layers, which with the help of a technique known as skip connection has paved the way for residual networks.

Nasnetlarge Zoph et al. (2018) is designed on a search space, called NAS-Net search space, which enables transferability. The model works by looking for the best convolutional layer, or cell, and subsequently replicating this layer in a stack, each with its own parameters to design a convolutional architecture. Also, a regularization technique, called ScheduledDropPath, that significantly improves generalization in the model is introduced.

Table 1: Description of adopted pretrained network.   

<table><tr><td>Network</td><td>Depth</td><td>Size (MB)</td><td>Parameters (Millions)</td><td>Input Size</td></tr><tr><td>Densenet201</td><td>201</td><td>77</td><td>20</td><td>224 × 224</td></tr><tr><td>Alexnet</td><td>8</td><td>227</td><td>61</td><td>227 × 227</td></tr><tr><td>Googlenet</td><td>8</td><td>27</td><td>7</td><td>224 × 224</td></tr><tr><td>Resnet18</td><td>18</td><td>44</td><td>11.7</td><td>224 × 224</td></tr><tr><td>Resnet50</td><td>50</td><td>96</td><td>25.6</td><td>224 × 224</td></tr><tr><td>Nasnetlarge</td><td>*</td><td>332</td><td>88.9</td><td>331 × 331</td></tr></table>

Deep neural networks have been adapted to the clouds classification problem. Originally, Imagenet dataset Deng et al. (2009), which includes one million images divided into 1000 classes, is adopted to perform the main training phase. Generally, a network elaborates an image and provides a prediction about a class it might belong to with an attached probability. Indeed, a network is structured to work on different layers. The first concerns the input image and requires 3 color channels. Next, convolutional layers, which work with the purpose to extract image features, are placed. The last learnable and the final classification layers are adopted to classify the input image. To make the pretrained network compliant to the classification of new images, the last two layers are replaced with new layers. Often, the last layer, with its

learnable weights, is completely connected. It is removed and replaced by a new one completely connected with the outputs related to classes of new data (clouds types). Furthermore, the learning of the new layer, connected with the transferred layers, can be speeded up by increasing the learning rate factors. Optionally, the weights of the previous levels can be left unchanged by resetting the learning rate to zero. This modification avoids weights update during training and a consequent flattening of the execution time as it is not necessary to calculate the gradients of the relative layers. This improvement has a strong impact in the case of small datasets to avoid overfitting.

# 3.3. Voting based learning

A voting based learning approach is adopted to manage the classification phase. In particular, among all possible strategies, we selected stacking. It works by training a single classifier and, subsequently, combines it with further classifiers. Unlike a standard approach, where weak or strong learners are adopted, we basically combined several equally powerful models that predict an outcome with a certain probability. Finally, we joined all the predictions for a classification result. The general model can be summarized by the following matrix

$$
C N = \left[ \begin{array}{c c c} \beta_ {1} i _ {1} & \dots & \beta_ {1} i _ {k} \\ \vdots & \ddots & \\ \beta_ {n} i _ {1} & & \beta_ {n} i _ {k} \end{array} \right] \tag {1}
$$

each $i _ { k }$ represent an image to be classified, taken from the set $I m g s =$ $\{ i _ { 1 } , i _ { 2 } , \ldots , i _ { k } \}$ with cardinality $k$ , belonging to one of $x$ classes. Furthermore, each $\beta _ { n }$ represent a deep neural network, taken from the set $C =$ $\{ \beta _ { 1 } , \beta _ { 2 } , . . . , \beta _ { n } \}$ with cardinality $n$ , which provides a decision $d \in I \{ 1 , \ldots , x \}$ , with reference to $i _ { k } \in { \cal I } m g s$ and $x$ membership classes. The set of decisions can be rearranged through the following matrix $\boldsymbol { D }$

$$
D = \left[ \begin{array}{c c c} d _ {\beta_ {1} i _ {1}} & \dots & d _ {\beta_ {1} i _ {k}} \\ \vdots & \ddots & \\ d _ {\beta_ {n} i _ {1}} & & d _ {\beta_ {n} i _ {k}} \end{array} \right] \tag {2}
$$

it describes the result of deep neural networks combination and images of the matrix $\zeta N$ in terms of position, such as $\beta _ { n } i _ { k } \to d _ { \beta _ { n } i _ { k } }$ . In addition, a score value $s \in S \{ 0 , \ldots , 1 \}$ is associated to each decision $d$ and provides the

posterior probability $P ( i | x )$ that an image $i$ could belong to class $x$ . Finally, all the score values relating to the results of the possible combinations of matrix $C N$ are collected in the matrix $S$

$$
S = \left[ \begin{array}{c c c} P (i _ {1} | x) _ {d _ {\beta_ {1} i _ {1}}} & \dots & P (i _ {k} | x) _ {d _ {\beta_ {1} i _ {k}}} \\ \vdots & \ddots & \\ P (i _ {1} | x) _ {d _ {\beta_ {n} i _ {1}}} & & P (i _ {k} | x) _ {d _ {\beta_ {n} i _ {k}}} \end{array} \right] \tag {3}
$$

each element of posterior probability in the matrix $S$ refers to element of the matrix $C N$ , such as $\beta _ { n } i _ { k } \to d _ { \beta _ { n } i _ { k } } \to P ( i _ { k } | x ) _ { d _ { \beta _ { n } i _ { k } } }$ . Moving on, each column of the matrix $D$ is analyzed with statistical mode and stored in the vector $D M$

$$
D M = \left\{d m _ {d _ {\beta_ {1}, \dots , n ^ {i _ {1}}}}, \dots , d m _ {d _ {\beta_ {1}, \dots , n ^ {i _ {k}}}} \right\}, \tag {4}
$$

the generic value dm contains the modal value of the class to which image $i$ could belong with the average probability score $d s$ . In essence, this is the class to which an image could belong based on the votes given by different deep neural networks. In this regard, the concept of statistical mode is introduced. It can be defined as the value which is repeatedly occurred in a given set

$$
m o d e = l + \left(\frac {f _ {1} - f _ {0}}{2 f _ {1} - f _ {0} - f _ {2}}\right) \times h \tag {5}
$$

where $l$ is the lower limit of the modal class, $h$ is the size of the class interval, $f _ { 1 }$ is the frequency of the modal class, $f _ { 0 }$ is the frequency of the class which precedes the modal class and $f _ { 2 }$ is the frequency of the class which successes the modal class. The columns of matrix $D$ are analyzed in order to obtain the values of the most frequent decisions. This step is performed in order to verify the highest voted classes from different deep neural networks, contained in the $\zeta N$ set. Moreover, the aim of mode application is twofold. First, to extract the most frequent value. Second, to extract its occurrences in terms of indices. For each most frequent occurrence, modal value, the corresponding score from the matrix $S$ is extracted. To this end, $D S$ vector is built

$$
D S = \left\{d s _ {P \left(i _ {1} \mid x\right) _ {d _ {\beta_ {1}, \dots , n ^ {i _ {1}}}}}, \dots , d s _ {P \left(i _ {k} \mid x\right) _ {d _ {\beta_ {1}, \dots , n ^ {i _ {k}}}}} \right\}, \tag {6}
$$

where each element $d s$ contains the average decision scores with higher frequency, extracted through the mode, with reference to corresponding column of the matrix $\boldsymbol { D }$ .

# 4. Experimental results

This section describes the experimental phase. In order to train the neural models, with purpose to perform classification task in a supervised context, labeled data are need. Consequently, the issue to be addressed concerns the quantity of data sufficient to produce experimental results. The content of a large dataset, useful to training and testing, strongly affects the classification performance. Therefore, the discriminating factor about the effectiveness of neural models is the amount of data. Contextually, with purpose to produce compliant performance, the settings reported in recent cloud classification methods are adopted.

# 4.1. Datasets

The proposed framework on a state-of-art datasets, containing groundbased clouds images, is tested. Datasets adopted are:

1. Multimodal-Ground-based-Cloud-Database (MGCD) Liu et al. (2020a,b). It is collected in China and consists in cloud images captured by a sky camera with a fisheye lens under a variety of conditions and multimodal cloud information. It includes a total amount of 1720 cloud data. Images are divided into seven classes: cumulus, cirrus, altocumulus, clear sky, stratus, stratocumulus, cumulonimbus. The number of item of each class varies from 140 to 350, and the detailed numbers are listed in Table 2.   
2. Singapore Whole sky IMaging CATegories Database (SWIMCAT) dataset Dev et al. (2015). It is composed of 784 sky/cloud patch images with 125 x 125 pixels captured using wide angle high-resolution sky imaging system, a calibrated ground-based WSI designed by Dev et al. (2014). The dataset is splitted into five distinct categories: clear sky, patterned clouds, thick dark clouds, thick white clouds, and veil clouds. Details are present in table 3.   
3. Cirrus Cumulus Stratus Nimbus (CCSN) dataset Zhang et al. (2018). It contains only 2,543 unique cloud images with 256 x 256 pixels in the JPEG format and contains 10 different forms in cloud observation. It

is characterized by a large set of images, making it the largest of the available public cloud dataset. Details are shown in table 4.

Table 2: Details of MGCD dataset.   

<table><tr><td>Label</td><td>Cloud Type</td><td>Number of samples</td></tr><tr><td>1</td><td>Cumulus</td><td>160</td></tr><tr><td>2</td><td>Cirrus</td><td>300</td></tr><tr><td>3</td><td>Altocumulus</td><td>340</td></tr><tr><td>4</td><td>Clear sky</td><td>350</td></tr><tr><td>5</td><td>Stratocumulus</td><td>250</td></tr><tr><td>6</td><td>Stratus</td><td>140</td></tr><tr><td>7</td><td>Cumulonimbus</td><td>180</td></tr></table>

Table 3: Details of SWIMCAT dataset.   

<table><tr><td>Label</td><td>Cloud Type</td><td>Number of samples</td></tr><tr><td>A</td><td>Clear Sky</td><td>224</td></tr><tr><td>B</td><td>Patterned clouds</td><td>89</td></tr><tr><td>C</td><td>Thick dark clouds</td><td>251</td></tr><tr><td>D</td><td>Thick white clouds</td><td>135</td></tr><tr><td>E</td><td>Veil clouds</td><td>85</td></tr></table>

# 4.2. Discussion

Table 5 provides indications about the adopted neural models with respect to datasets. As can be seen, different combinations are provided due to the variable composition (total images, images per class, etc) of each datasets. In fact, two additional neural models, Resnet18 and Nasnetlarge, have been added for CCSN processing as it is the most complex to manage. Moreover, the framework consists in different modules written in Matlab language. Neural models were trained based on different parameters. Stochastic Gradient Descent (SGDM) with Momentum is adopted as solver of training process. Its main peculiarity concerns the oscillation along the steepest descent path towards the optimum. Adding a momentum term to the parameter update is one way to reduce this oscillation. Carrying on, MiniBatchSize value, the subset size of the training set adopted to evaluate the gradient of the loss

Table 4: Details of CCSN Dataset.   

<table><tr><td>Label</td><td>Cloud Type</td><td>Number of samples</td></tr><tr><td>Ci</td><td>Cirrus</td><td>139</td></tr><tr><td>Cs</td><td>Cirrostratus</td><td>287</td></tr><tr><td>Cc</td><td>Cirrocumulus</td><td>268</td></tr><tr><td>Ac</td><td>Altocumulus</td><td>221</td></tr><tr><td>As</td><td>Altostratus</td><td>188</td></tr><tr><td>Cu</td><td>Cumulus</td><td>182</td></tr><tr><td>Cb</td><td>Cumulonimbus</td><td>242</td></tr><tr><td>Ns</td><td>Nimbostratus</td><td>274</td></tr><tr><td>Sc</td><td>Stratocumulus</td><td>340</td></tr><tr><td>St</td><td>Strtus</td><td>202</td></tr><tr><td>Ct</td><td>Contrails</td><td>200</td></tr></table>

function and update the weights, has been set to 10, optimal for the obtained results. About MaxEpochs, maximum number of epochs to use for training, the right compromise was reached with the value 6 optimizing execution time and performance. An iteration is a step performed by SGDM to minimize the loss function using MiniBatchSize. An epoch concerns the complete cycle of the training process on training set. InitialLearnRate has been set to 3e-4. If it is too low results in a high training time. Otherwise, if too high, the result may be suboptimal or training may diverge. The right compromise has also been found for the latter. To avoid discarding the same data every epoch, Shuffle parameter been set to every-epoch. Finally, ValidationFrequency, number of iterations between evaluations of validation metrics, has been set as the ratio between training set size and MiniBatchSize.

The classification accuracy on MGCD dataset is presented in table 6. In order to produce a comparison with further methods, that work on the same ground-based cloud classification task, the settings described in Liu et al. (2020b) have been adopted. Looking at the results, several conclusions can be drawn. The proposed model, composed of different pretrained networks, produces promising recognition accuracy, giving a high representation of clouds images. The implemented voting based architecture compared with the competitors gets the better performance.

The classification performance on SWIMCAT dataset are summarized in table 7. In this phase, the settings present in Shi et al. (2017) are adopted.

Table 5: Deep neural networks adopted with respect to datasets.   
Table 6: Experimental results on MGCD dataset.   

<table><tr><td>Networks\Datasets</td><td>MGCD</td><td>SWIMCAT</td><td>CCSN</td></tr><tr><td>Densenet201</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Alexnet</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Googlenet</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Resnet18</td><td></td><td></td><td>✓</td></tr><tr><td>Resnet50</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Nasnetlarge</td><td></td><td></td><td>✓</td></tr></table>

<table><tr><td>Method</td><td>Acc</td></tr><tr><td>Our</td><td>99.98</td></tr><tr><td>MMFN Liu et al. (2020b)</td><td>88.63</td></tr><tr><td>DCAFs + MI Liu et al. (2020b)</td><td>82.97</td></tr><tr><td>BOVW + MI Liu et al. (2020b)</td><td>67.20</td></tr><tr><td>PBOVW + MI Liu et al. (2020b)</td><td>67.15</td></tr><tr><td>LPB+ MI Liu et al. (2020b)</td><td>50.53</td></tr><tr><td>CLPB+ MI Liu et al. (2020b)</td><td>69.68</td></tr><tr><td>CloudNet + MI Liu et al. (2020b)</td><td>80.37</td></tr><tr><td>BoVW Csurka et al. (2004)</td><td>66.15</td></tr><tr><td>PBoVW Csurka et al. (2004)</td><td>66.13</td></tr><tr><td>LBP Ojala et al. (2002)</td><td>55.20</td></tr><tr><td>CLBP Guo et al. (2010)</td><td>69.18</td></tr><tr><td>VGG-16 Simonyan and Zisserman (2014)</td><td>77.95</td></tr><tr><td>DCAFs Shi et al. (2017)</td><td>82.67</td></tr><tr><td>CloudNet Zhang et al. (2018)</td><td>79.92</td></tr><tr><td>DMF Liu and Li (2018)</td><td>79.05</td></tr><tr><td>DTFN Li et al. (2020)</td><td>86.48</td></tr><tr><td>HMF Liu et al. (2019)</td><td>87.90</td></tr></table>

In particular, a cross validation on 2,3,4,5 folds was performed first. Subsequently, 40 images per class for training and 45 ones for testing have been selected randomly. The average accuracy of 50 random runs is reported. In

the training phase, the neural models that did not contribute to improve both the performance and the execution time were discarded, as can be seen in table 5. The results highlight that combining different multiple classification predictions is useful to capture more spatial and local layout information of clouds with purpose to outperform the compared methods. Furthermore, it is important to underline that the proposed approach is even better than neural models, such as VGG-16 Simonyan and Zisserman (2014) and Cloud-Net Zhang et al. (2018), in which a single classification confidence value is provided compared to a multiple voting based mechanism.

Table 7: Experimental results on SWIMCAT dataset.   

<table><tr><td>Folds
Methods</td><td>2</td><td>3</td><td>4</td><td>5</td><td>40/45</td></tr><tr><td>Our</td><td>99.36</td><td>99.49</td><td>99.49</td><td>99.75</td><td>99.91</td></tr><tr><td>LPB Sun et al. (2009)</td><td>85.26</td><td>81.60</td><td>83.51</td><td>85.03</td><td>93.47</td></tr><tr><td>Heinle Feature Heinle et al. (2010)</td><td>90.26</td><td>91.89</td><td>92.91</td><td>93.43</td><td>93.09</td></tr><tr><td>Text-based method Dev et al. (2015)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>95.00</td></tr><tr><td>DCAF Shi et al. (2017)</td><td>98.72</td><td>98.46</td><td>98.97</td><td>98.84</td><td>99.56</td></tr></table>

Table 8 shows the performance on CCSN dataset. In order to compare results with further methods that work on same task, the settings described in Zhang et al. (2020) have been adopted. Also in this case, the combination of neural models lead to better performance. As shown in table 5, for this experimental phase we have stacked all analyzed deep neural network. Once again, the results demonstrate that the multiple base learners may lead to better performance according to the combination with the different number of base learners in the stacking.

The presented satisfactory results are attributable to many relevant aspects. The first regards the features extracted through convolutional layers of the deep neural network. They provide a good image representation, although are completely abstract and devoid of real meaning. Second regards the framework capability to provide multiple representation models, that lead to a significant improvement in performance. Another issue concerns the image size normalization, tackled to many methods in the field. It is performed before the features extraction, to avoid performance degradation. Again, we can look at the robustness with respect to the underrepresented classes in the datasets. In fact, the framework does not fail even though the samples

Table 8: Experimental results on CCSN dataset.   

<table><tr><td>Method</td><td>Acc</td></tr><tr><td>Our</td><td>95.08</td></tr><tr><td>Cloudnet Zhang et al. (2018)</td><td>90.00</td></tr><tr><td>Zhang et al. (2020)</td><td>80.00</td></tr><tr><td>MMI Liu et al. (2018)</td><td>75.42</td></tr><tr><td>M_DF Liu et al. (2018)</td><td>78.21</td></tr><tr><td>M_JFCNNLiu et al. (2018)</td><td>84.55</td></tr><tr><td>V_DF Liu et al. (2018)</td><td>85.10</td></tr><tr><td>V_JFCNN Liu et al. (2018)</td><td>86.79</td></tr><tr><td>V_DF + MMI Liu et al. (2018)</td><td>86.33</td></tr><tr><td>V_JFCNN + MMI Liu et al. (2018)</td><td>89.40</td></tr><tr><td>V_DF + M_DF Liu et al. (2018)</td><td>90.21</td></tr><tr><td>J_JFCNN Liu et al. (2018)</td><td>78.82</td></tr><tr><td>JFCNN Liu et al. (2018)</td><td>93.37</td></tr></table>

are not sufficient for a class representation in specific cases. The latter appears to be an open problem in the literature, as ad hoc classifiers are often designed for unbalanced classification different from the standard ones that produce untrue results. Contrary, a weak point concerns the computational aspect. First, the time required for training pretrained model is high but less than a model created from scratch. Second, the classification step, that provides multiple choices in decision making at each iteration, requires a lot of effort. The latter works for the purpose of choosing which classifiers are suitable for specific clouds images included in the test set. Finally, we have shown that although the framework is more expensive from a computational point of view and it produces better results than a single classifier.

# 5. Conclusions and Future Works

The challenge in ground-based cloud recognition is specifically interesting and, not only, for its multiple aspects and variety of data. The complexity of the task is linked to several factors such as the type of clouds and the visual patterns contained in them. In support, convolutional neural networks lend a big hand to understand the meaning of images with the consequent goal of their classification. In this regard, we proposed a framework that combines convolutional neural networks, adapted to the cloud recognition

task through a transfer learning approach, using voting rules. The results produced certainly strengthen the theoretical thesis. A multiple model, based on several deep neural networks, compared to a single one is a powerful factor. Through a large experimental phase, it has been shown how the proposed approach is competitive, and in some cases better, compared to the more advanced methods. Although pretrained models have been adopted, the main weakness concerns the computational complexity of learning phase that requires a long time, sensitive to the growth of the data. Future work will certainly concern the study and analysis of still unexplored convolutional neural networks for this type of problem and the application of the proposed framework to further datasets with the aim of taking a step forward in cloud recognition.

# Acknowledgements

Our thanking is for Alfredo Petrosino. He followed us during the first steps towards the Computer Science, through a whirlwind of goals, ideas and, especially, love and passion for the work. We will be forever grateful great master.

# References

Chen, T., Rossow, W.B., Zhang, Y., 2000. Radiative effects of cloud-type variations. Journal of climate 13, 264–286.   
Csurka, G., Dance, C., Fan, L., Willamowski, J., Bray, C., 2004. Visual categorization with bags of keypoints, in: Workshop on statistical learning in computer vision, ECCV, Prague. pp. 1–2.   
Deng, J., Dong, W., Socher, R., Li, L.J., Li, K., Fei-Fei, L., 2009. Imagenet: A large-scale hierarchical image database, in: 2009 IEEE conference on computer vision and pattern recognition, Ieee. pp. 248–255.   
Dev, S., Lee, Y.H., Winkler, S., 2015. Categorization of cloud image patches using an improved texton-based approach, in: 2015 IEEE International Conference on Image Processing (ICIP), IEEE. pp. 422–426.

Dev, S., Savoy, F.M., Lee, Y.H., Winkler, S., 2014. Wahrsis: A low-cost high-resolution whole sky imager with near-infrared capabilities, in: Infrared Imaging Systems: Design, Analysis, Modeling, and Testing XXV, International Society for Optics and Photonics. p. 90711L.   
Duda, D.P., Minnis, P., Khlopenkov, K., Chee, T.L., Boeke, R., 2013. Estimation of 2006 northern hemisphere contrail coverage using modis data. Geophysical Research Letters 40, 612–617.   
Guo, Z., Zhang, L., Zhang, D., 2010. A completed modeling of local binary pattern operator for texture classification. IEEE Transactions on Image Processing 19, 1657–1663.   
He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep residual learning for image recognition, in: Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 770–778.   
Heinle, A., Macke, A., Srivastav, A., 2010. Automatic cloud classification of whole sky images. Atmospheric Measurement Techniques 3, 557–567.   
Huang, G., Liu, Z., Van Der Maaten, L., Weinberger, K.Q., 2017. Densely connected convolutional networks, in: Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 4700–4708.   
Krizhevsky, A., Sutskever, I., Hinton, G.E., 2012. Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems 25, 1097–1105.   
LeCun, Y., Boser, B., Denker, J.S., Henderson, D., Howard, R.E., Hubbard, W., Jackel, L.D., 1989. Backpropagation applied to handwritten zip code recognition. Neural computation 1, 541–551.   
Li, M., Liu, S., Zhang, Z., 2020. Deep tensor fusion network for multimodal ground-based cloud classification in weather station networks. Ad Hoc Networks 96, 101991.   
Liu, S., Duan, L., Zhang, Z., Cao, X., 2019. Hierarchical multimodal fusion for ground-based cloud classification in weather station networks. IEEE Access 7, 85688–85695.

Liu, S., Li, M., 2018. Deep multimodal fusion for ground-based cloud classification in weather station networks. EURASIP Journal on Wireless Communications and Networking 2018, 1–8.   
Liu, S., Li, M., Zhang, Z., Cao, X., Durrani, T.S., 2020a. Ground-based cloud classification using task-based graph convolutional network. Geophysical Research Letters 47, e2020GL087338.   
Liu, S., Li, M., Zhang, Z., Xiao, B., Cao, X., 2018. Multimodal groundbased cloud classification using joint fusion convolutional neural network. Remote Sensing 10, 822. doi:10.3390/rs10060822.   
Liu, S., Li, M., Zhang, Z., Xiao, B., Durrani, T.S., 2020b. Multi-evidence and multi-modal fusion network for ground-based cloud recognition. Remote Sensing 12, 464.   
Liu, W., Wang, Z., Liu, X., Zeng, N., Liu, Y., Alsaadi, F.E., 2017. A survey of deep neural network architectures and their applications. Neurocomputing 234, 11–26.   
Ojala, T., Pietikainen, M., Maenpaa, T., 2002. Multiresolution gray-scale and rotation invariant texture classification with local binary patterns. IEEE Transactions on Pattern Analysis and Machine Intelligence 24, 971–987.   
Peteiro-Barral, D., Guijarro-Berdi˜nas, B., 2013. A survey of methods for distributed machine learning. Progress in Artificial Intelligence 2, 1–11.   
Rossow, W.B., Schiffer, R.A., 1991. Isccp cloud data products. Bulletin of the American Meteorological Society 72, 2–20.   
Shi, C., Wang, C., Wang, Y., Xiao, B., 2017. Deep convolutional activationsbased features for ground-based cloud classification. IEEE Geoscience and Remote Sensing Letters 14, 816–820.   
Simonyan, K., Zisserman, A., 2014. Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556 .   
Stephens, G.L., 2005. Cloud feedbacks in the climate system: A critical review. Journal of climate 18, 237–273.

Sun, X., Liu, L., Gao, T., Zhao, S., 2009. Classification of whole sky infrared cloud image based on the lbp operator. Transactions of Atmospheric Sciences 32, 490–497.   
Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D., Vanhoucke, V., Rabinovich, A., 2015. Going deeper with convolutions, in: Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1–9.   
Zhang, J., Liu, P., Zhang, F., Iwabuchi, H., de Moura, A.A., de Albuquerque, V.H.C., 2020. Ensemble meteorological cloud classification meets internet of dependable and controllable things. IEEE Internet of Things Journal .   
Zhang, J., Liu, P., Zhang, F., Song, Q., 2018. Cloudnet: Ground-based cloud classification with deep convolutional neural network. Geophysical Research Letters 45, 8665–8672.   
Zoph, B., Vasudevan, V., Shlens, J., Le, Q.V., 2018. Learning transferable architectures for scalable image recognition, in: Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 8697–8710.