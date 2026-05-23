# A new barrier penetration formula and its application to $\alpha$ -decay half-lives

Lu-Lu Li,1 Shan-Gui Zhou,1, 2 , ∗ En-Guang Zhao, $^ { 1 , 3 , 2 }$ and Werner Scheid4

1Key Laboratory of Frontiers in Theoretical Physics, Institute of Theoretical Physics, Chinese Academy of Sciences, Beijing 100190, China

$\mathcal { Z }$ Center of Theoretical Nuclear Physics, National Laboratory of Heavy Ion Accelerator, Lanzhou 730000, China

$_ { 3 }$ School of Physics, Peking University, Beijing 100871, China

4Institute for Theoretical Physics of Justus-Liebig-University, 35392 Giessen, Germany

(Dated: September 11, 2017)

Starting from the WKB approximation, a new barrier penetration formula is proposed for potential barriers containing a long-range Coulomb interaction. This formula is especially proper for the barrier penetration with penetration energy much lower than the Coulomb barrier. The penetrabilities calculated from the new formula agree well with the results from the WKB method. As a first attempt, this new formula is used to evaluate $\alpha$ decay half-lives of atomic nuclei and a good agreement with the experiment is obtained.

PACS numbers: 03.65.Xp, 23.60.+e, 25.60.Pj

Keywords: Quantum tunneling, penetrability, alpha decay, Coulomb barrier

# I. INTRODUCTION

As a common quantum phenomenon, the tunneling through a potential barrier plays a very important role in the microscopic world and has been studied extensively since the birth of quantum mechanics. One of the earliest applications of quantum tunneling is the explanation of $\alpha$ decays in atomic nuclei. The quantum tunneling effect governs also many other nuclear processes such as fission and fusion. In particular, a lot of new features are revealed in sub-barrier fusion reactions which are closely connected with the tunneling phenomena [1, 2, 3, 4].

For most of the potential barriers, the penetrability can not be calculated analytically [5]. Among those potentials for which analytical solutions can be obtained, the parabolic potential [6, 7] is the mostly used in the study of nuclear fusion. By approximating the Coulomb barrier to a parabola, Wong derived an analytic expression for the fusion cross section [8] which is widely adopted today in the study of heavy ion reactions (see, e.g., recent Refs. [9, 10]). The parabolic approximation works remarkably well both for the penetrability and for the fusion cross section at energies around or above the Coulomb barrier [11].

Apparently the parabolic approximation breaks down at energies much smaller than the barrier height due to the long-range Coulomb interaction. One may calculate the penetration probability numerically by using the path integral method or the WKB approximation. However, it is highly desirable to have an analytical expression for the barrier penetrability when one introduces an energydependent one-dimensional potential barrier [12] or barrier distribution functions [13, 14, 15, 16, 17].

In the present work, we derived a new barrier pene-

tration formula based on the WKB approximation. The influence of the long Coulomb tail in the barrier potential is taken into accout properly. Therefore this formula is especially applicable to the barrier penetration with penetration energy much lower than the Coulomb barrier.

As a first attempt and a test study, we apply this new formula to evaluate $\alpha$ decay half-lives of atomic nuclei. For the $\alpha$ decay, the penetrability is usually calculated with the WKB approach [18, 19, 20], in other words, integrating numerically the wave number within two turning points at which the interaction potential is equal to the $Q$ -value of the $\alpha$ decay. We will show that the present analytical formula reproduces the experimental results very well, especially for spherical nuclei.

The paper is organized as follows. In Sec. II we present the new barrier penetration formula. The validity of the new formula is investigated and its application to $\alpha$ decays are given in Sec. III. Finally in Sec. IV we summarize our work. In the Appendix, the detailed derivation of the new penetration formula is given.

# II. FORMALISM

When the penetration energy is well below the Coulomb barrier, the barrier penetrability formula derived from the WKB approximation reads,

$$
P (E) = \exp \left[ - 2 \int_ {R _ {\mathrm {i n}}} ^ {R _ {\mathrm {o u t}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} (V (R) - E)} d R \right], \quad (1)
$$

where the potential usually consists of three parts, the nuclear, the Coulomb, and the centrifugal potentials,

$$
V (R) = V _ {\mathrm {N}} (R) + V _ {\mathrm {C}} (R) + \frac {L (L + 1)}{2 \mu R ^ {2}}. \tag {2}
$$

$R _ { \mathrm { i n } }$ and $R _ { \mathrm { o u t } }$ are the inner and outer turning points determined by the relation $V ( R ) = E$ .

By approximating $V ( R )$ to a parabola with the height $V _ { \mathrm { B } }$ and the width $\hbar \omega$ , Eq. (1) is reduced as

$$
P (E) = \exp \left[ - \frac {2 \pi}{\hbar \omega} (V _ {\mathrm {B}} - E) \right], \qquad (3)
$$

which has been widely used in the study of heavy ion reactions.

Because of the long-range Coulomb interaction, the Coulomb barrier given in Eq. (2) has a long tail and is asymmetric. Thus for the penetration well below the barrier, the parabolic approximation is not valid. We may divide the potential barrier into two parts at the barrier position $R _ { \mathrm { B } }$ . The first part of $V ( R )$ with $R _ { \mathrm { i n } } < R < R _ { \mathrm { B } }$ could still be approximated by half of a parabola and we need to evaluate the integration in Eq. (1) in the range $R _ { \mathrm { B } } < R < R _ { \mathrm { o u t } }$ only. For S wave, the integral in Eq. (1) is evaluated as,

$$
P (E) = \exp [ - (x _ {1} + x _ {2}) ], \tag {4}
$$

with

$$
\begin{array}{l} x _ {1} \equiv 2 \int_ {R _ {\mathrm {i n}}} ^ {R _ {\mathrm {B}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} (V (R) - E)} d R \\ \approx \frac {\pi}{\hbar \omega} (V _ {B} - E), \tag {5} \\ \end{array}
$$

under the parabolic approximation and

$$
\begin{array}{l} x _ {2} \equiv 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {o u t}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} (V (R) - E)} d R \\ \approx 2 k R _ {\mathrm {B}} \left[ \tau \left(\frac {\pi}{2} - \arcsin \sqrt {\frac {1}{\tau}}\right) - \sqrt {\tau - 1} \right] \\ + \frac {k a}{\sqrt {\tau - 1}} \frac {V _ {0}}{E} \ln \left[ 1 + e ^ {\left(R _ {0} - R _ {B}\right) / a} \right], \tag {6} \\ \end{array}
$$

where $k = \sqrt { 2 \mu E } / \hbar$ and $\tau = V _ { \mathrm { C } } ( R _ { \mathrm { B } } ) / E$ . The details of the derivation of Eq. (6) are given in the Appendix. It should be mentioned that in the derivation of Eq. (6), a Woods-Saxon form is used for $V _ { \mathrm { N } } ( R )$ .

# III. RESULTS AND DISCUSSIONS

In this section, we use the new formula to study the typical barrier penetration problem, $\alpha$ decays of atomic nuclei. The $\alpha$ decay half-life is related to the decay width $\Gamma$ by [20, 21, 22]

$$
T _ {1 / 2} = \frac {\hbar \ln 2}{\Gamma}. \tag {7}
$$

The decay width $\Gamma$ is calculated as [20]

$$
\Gamma = \hbar \nu S P (Q) = \hbar \xi P (Q), \tag {8}
$$

where $\nu$ is the assaults frequency of $\alpha$ particle on the barrier, $S$ the spectroscopic or preformation factor and

![](images/9986cfe1452b0958ff10fe8f5a818cc80528ca313dc3c25487f9537b927af40d.jpg)

![](images/6f135fcdabbf657da99f53c764cf81ef58d037c9cc3113f9dbcb4870c8b233d6.jpg)  
FIG. 1: (Color online) The barrier potential between the $\alpha$ and the daughter nucleus for $\scriptstyle { ^ { 2 1 2 } \mathrm { P o } }$ and $^ { 1 4 4 }$ Nd. The solid curve shows the exact potential $V ( R )$ and the dashed curve stands for the effective potential given in Eq. (12) associated with the parabolic approximation Eq. (5) and the new barrier penetration formula Eq. (6). Note that the two curves are almost identical to each other.

$P ( Q )$ the penetrability with $Q$ the $\alpha$ decay Q-value. For spherical nuclei, $\xi$ is parametrized as [20]

$$
\xi = (6. 1 8 1 4 + 0. 2 9 8 8 A ^ {- 1 / 6}) \times 1 0 ^ {1 9} \quad \mathrm {s} ^ {- 1}, \tag {9}
$$

and the penetrability will be calculated with Eqs. (4), (5), and (6).

For the $\alpha$ -nuclear interaction, we adopt the Coulomb and the Woods-Saxon potentials and parameters proposed in Ref. [20],

$$
V _ {\mathrm {C}} (R) = \left\{ \begin{array}{l l} \frac {2 Z e ^ {2}}{R}, & R \geq R _ {m}, \\ \frac {Z e ^ {2}}{R _ {m}} \left[ 3 - \frac {R ^ {2}}{R _ {m} ^ {2}} \right], & R \leq R _ {m}, \end{array} \right. \tag {10}
$$

and

$$
V _ {\mathrm {N}} (R) = \frac {V (A , Z , Q)}{1 + \exp \left[ \left(R - R _ {m}\right) / a \right]}, \tag {11}
$$

with $A$ and $Z$ the mass and charge numbers of the daughter nucleus and $Q$ the $\alpha$ decay energy. The parameters

in these potentials and given in Eq. (9) were obtained by fitting $\alpha$ decay half lives and cross section data for several fusion reactions. It can be easily verified that the position of the Coulomb barrier $R _ { \mathrm { B } }$ is larger than $R _ { m }$ thus the use of the Coulomb force given in Eq. (A3) is valid.

# A. Validity of the new formula

Before the new formula is used to study alpha decays, we investigate in details its validity. First we examine

how the effective potential connected with the new formula Eq. (6) is close to the exact one. Two extreme examples are chosen for this purpose, 212Po which has a very short half-life $3 . 0 2 \times 1 0 ^ { - 7 }$ s and $^ { 1 4 4 }$ Nd which has a quite long half-life $7 . 2 4 \times 1 0 ^ { 2 2 }$ s [23]. The barrier potential $V ( R )$ is shown in Fig. 1 for these two systems. The effective potential,

$$
V _ {\mathrm {e f f}} (R) = \left\{ \begin{array}{l l} V _ {\mathrm {B}} - \frac {1}{2} \mu \omega^ {2} (R - R _ {B}) ^ {2}, & R _ {\mathrm {i n}} <   R <   R _ {\mathrm {B}}, \\ V _ {\mathrm {C}} (R) + \frac {V _ {\mathrm {C}} (R) - E}{V _ {\mathrm {C}} (R _ {B}) - E} V _ {\mathrm {N}} (R) + \frac {1}{4} \frac {V _ {\mathrm {N}} ^ {2} (R)}{V _ {\mathrm {C}} (R _ {\mathrm {B}}) - E}, & R _ {\mathrm {B}} <   R <   R _ {\mathrm {V}}, \\ V _ {\mathrm {C}} (R), & R _ {\mathrm {V}} <   R <   R _ {\mathrm {o u t}}, \end{array} \right. \tag {12}
$$

is also shown for comparison. $R _ { \mathrm { V } } \ \approx \ 9 \ - \ 1 2$ fm is the radial position outside of which the nuclear part of the $\alpha$ -nucleus potential could be neglected (see the Appendix for more details). In our calculations, the width of the parabolic potential is obtained by fitting the barrier potential from the inner turning point $R _ { \mathrm { i n } }$ to the position of the barrier $R _ { \mathrm { B } }$ . Unlike the full parabolic approximation, the effective potential is asymmetric and coincides with the exact potential very well, especially the outer side of the barrier which critically influences $\alpha$ decays.

In order to examine more closely the accuracy of the new formula, we list the calculated penetration probabilities for $\alpha$ decays of polonium isotopes in Table I. The values in the exponential of Eq. (4), $x _ { 1 }$ and $x _ { 2 }$ , calculated from the WKB approach, the parabolic approximation and the new formula are compared. One finds good agreement between the results from the new formula and the WKB approach. For $x _ { 2 }$ , the average relative root mean square deviation is $0 . 2 8 \ \%$ . This tells that the present formula could be used with satisfactory accuracy in the study the barrier penetration well below the Coulomb barrier.

# B. $\alpha$ -decay half-lives

The new barrier penetration formula is used to calculate $\alpha$ -decay half-lives of 344 nuclei collected in Ref. [23]. The experimental values of $\alpha$ decay half lives are also taken from Ref. [23] except for $\mathrm { ^ { 2 1 5 } P o }$ . In Ref. [23], $\log ( T _ { 1 / 2 } ^ { \mathrm { E x p } } / s ) = - 3 . 7 4$ for $^ { 2 1 5 }$ Po while in Refs. [24, 25, 26] the experimental value is $\log ( T _ { 1 / 2 } ^ { \mathrm { E x p } } / s ) = - 2 . 7 5$ . We take the latter value in the present work. The experimental values of the $\alpha$ decay half-lives range from $1 0 ^ { - 7 } \sim 1 0 ^ { 2 4 }$ s.

The $Q$ values of the $\alpha$ decays are also taken from Ref. [23] where these values were calculated from the Atomic Mass Evaluation by Audi et al. [27] or from the mass table by M¨oller et al. [28].

The angular momentum $L$ carried by the emitted $\alpha$ particle in a ground-state to ground-state $\alpha$ transition of even-even nucleus is zero. In odd- $A$ or odd-odd nuclei, $L$ could be non zero. Because the information on $L$ is absent, in the present work we assume $L = 0$ for all $\alpha$ decays as usually done [19, 20, 21, 29, 30].

In Fig. 2, the calculated results and experimental values for $\alpha$ decay half lives are compared. In order to show it clearly, these 344 nuclei are divided into four groups, namely, 159 even-even, 72 even-odd (even- $Z$ and odd- $N$ ), 66 odd-even, and 47 odd-odd nuclei. The ratios between the calculated and the experimental values $S _ { \alpha } = \log _ { 1 0 } ( T _ { 1 / 2 } ^ { \mathrm { C a l } } / T _ { 1 / 2 } ^ { \mathrm { E x p } } )$ are presented in Fig. 3. Two dashed lines are drawn to guide the eye. One finds that most of the calculated results are of the same order of magnitude as the experimental values.

A statistics of the agreement between the calculation and the experiment is made and given in Table II. Among all these 344 nuclei, there are only seven for which the calculated $\alpha$ decay half lives deviate by more than two orders of magnitude from the corresponding experimental values and $9 3 . 9 0 \%$ of them agree with experimental values within one order of magnitude.

Our results are particularly good for even-even nuclei, the calculated half lives for 97.48% of 159 even-even nuclei deviates from the experiment by less than one order of magnitude. The ratio $S _ { \alpha }$ is less than one for $9 5 . 8 3 \ \%$ of 72 even $Z$ and odd $N$ nuclei, 90.91 % of 66 odd-even nuclei and 82.98 % of 47 odd-odd nuclei. The angular momentum carried by the emitted $\alpha$ particle might not be zero for odd- $A$ or odd-odd nuclei. This will bring in

![](images/27651ac189ecc90cefa65bcdf93fef1a45460579ea7d8bf0bcfa82f9bfa2b50f.jpg)

![](images/a073d037e9f3cec6d7e445ccc3feab62f3562d60dce19cef7f4c9ae0edce820b.jpg)  
Ap

![](images/21aa135ceed517922d9e37ab15792074cfa5fff19af56e8de62b30a3aed3cef2.jpg)  
Ap

![](images/9dd7636a58f4c227cd0d80b16f54d24c5b49404b02a0f229030a31d207da0f91.jpg)  
Ap   
Ap   
FIG. 2: (Color online) Comparison of the calculated (blue crosses) and experimental (red dots) values for $\alpha$ decay half lives of 159 even-even, 72 even-odd, 66 odd-even, and 47 oddodd nuclei.

![](images/b8eea2fb08bac9944a04df1899fd3df90e7c02e925d1884d8920969e4d26fdd5.jpg)

![](images/9d423fcdbce68b8d8894e9ee99f6faaa3a9034cadba5dffe69a62c79dc51f8f6.jpg)  
Ap

![](images/36b22e96208385df59c87222dbd583d8853f1ad780936e82fa30a541c7e4033e.jpg)  
Ap

![](images/334d1d186e4c5a807488cfc8b0de39a42ecc4db91b8eaf5871e608a6b653ad7a.jpg)  
Ap   
Ap   
FIG. 3: (Color online) The ratios between the calculated and experimental values for $\alpha$ decay half lives of 159 even-even, 72 even-odd, 66 odd-even, and 47 odd-odd nuclei.

TABLE I: Comparison of the results for the barrier penetration probability for $\alpha$ decays in Po isotopes (charge and mass numbers of the $\alpha$ emitter are listed in the first and the second entries). The meaning of $x _ { 1 , 2 }$ is given in Eq. (4). The superscript “WKB” means the penetrability calculated from the WKB approach, “Para” from the parabolic approximation in Eq. (5), and “New” from the new formulas Eq. (6).   

<table><tr><td>Zp</td><td>Ap</td><td>Qα (MeV)</td><td>x1WKB</td><td>x1New = x1Para</td><td>x2WKB</td><td>x2New</td></tr><tr><td>84</td><td>190</td><td>7.64</td><td>4.9808</td><td>5.0816</td><td>34.9523</td><td>35.0751</td></tr><tr><td>84</td><td>191</td><td>7.48</td><td>5.0093</td><td>5.1146</td><td>36.0311</td><td>36.1527</td></tr><tr><td>84</td><td>192</td><td>7.32</td><td>5.0384</td><td>5.1482</td><td>37.1506</td><td>37.2712</td></tr><tr><td>84</td><td>193</td><td>7.10</td><td>5.0896</td><td>5.2031</td><td>38.7753</td><td>38.8944</td></tr><tr><td>84</td><td>194</td><td>7.00</td><td>5.0980</td><td>5.2165</td><td>39.5213</td><td>39.6397</td></tr><tr><td>84</td><td>195</td><td>6.75</td><td>5.1605</td><td>5.2823</td><td>41.5276</td><td>41.6445</td></tr><tr><td>84</td><td>196</td><td>6.66</td><td>5.1664</td><td>5.2931</td><td>42.2564</td><td>42.3725</td></tr><tr><td>84</td><td>197</td><td>6.41</td><td>5.2292</td><td>5.3592</td><td>44.4401</td><td>44.5546</td></tr><tr><td>84</td><td>198</td><td>6.31</td><td>5.2396</td><td>5.3743</td><td>45.3311</td><td>45.4449</td></tr><tr><td>84</td><td>199</td><td>6.08</td><td>5.2957</td><td>5.4338</td><td>47.5227</td><td>47.6352</td></tr><tr><td>84</td><td>200</td><td>5.99</td><td>5.3036</td><td>5.4463</td><td>48.3954</td><td>48.5072</td></tr><tr><td>84</td><td>201</td><td>5.81</td><td>5.3429</td><td>5.4894</td><td>50.2458</td><td>50.3564</td></tr><tr><td>84</td><td>202</td><td>5.70</td><td>5.3585</td><td>5.5093</td><td>51.4094</td><td>51.5193</td></tr><tr><td>84</td><td>203</td><td>5.50</td><td>5.4050</td><td>5.5594</td><td>53.6532</td><td>53.7618</td></tr><tr><td>84</td><td>204</td><td>5.49</td><td>5.3875</td><td>5.5468</td><td>53.7347</td><td>53.8430</td></tr><tr><td>84</td><td>205</td><td>5.32</td><td>5.4245</td><td>5.5875</td><td>55.7496</td><td>55.8569</td></tr><tr><td>84</td><td>206</td><td>5.33</td><td>5.4015</td><td>5.5693</td><td>55.5907</td><td>55.6978</td></tr><tr><td>84</td><td>207</td><td>5.22</td><td>5.4191</td><td>5.5908</td><td>56.9347</td><td>57.0410</td></tr><tr><td>84</td><td>208</td><td>5.22</td><td>5.4007</td><td>5.5769</td><td>56.8997</td><td>57.0058</td></tr><tr><td>84</td><td>210</td><td>5.41</td><td>5.3038</td><td>5.4892</td><td>54.4768</td><td>54.5836</td></tr><tr><td>84</td><td>212</td><td>8.95</td><td>4.1395</td><td>4.3264</td><td>26.3317</td><td>26.4569</td></tr><tr><td>84</td><td>213</td><td>8.54</td><td>4.2585</td><td>4.4498</td><td>28.5307</td><td>28.6533</td></tr><tr><td>84</td><td>214</td><td>7.83</td><td>4.4720</td><td>4.6690</td><td>32.8310</td><td>32.9495</td></tr><tr><td>84</td><td>215</td><td>7.53</td><td>4.5552</td><td>4.7559</td><td>34.8360</td><td>34.9528</td></tr><tr><td>84</td><td>216</td><td>6.91</td><td>4.7391</td><td>4.9445</td><td>39.4763</td><td>39.5896</td></tr><tr><td>84</td><td>218</td><td>6.11</td><td>4.9669</td><td>5.1798</td><td>46.5717</td><td>46.6806</td></tr></table>

some errors for these nuclei in our calculation because the centrifugal potential is ignored in the present study.

The deformation influences the $\alpha$ decay life time both on the preformation mechanism and on the penetration process [20, 31, 32, 33]. In the present work, we have assumed the barrier potential to be spherical. In 68 of these 344 nuclei, the spherical potential assumption is met well (with $| \beta _ { 2 } | < 0 . 0 1$ for the daughter nucleus [34]). In Table III the calculated and experimental values of the $\alpha$ decay half lives for these nuclei are given. The statistical summary is also shown in the last line of Table II. It is found that the new formula gives very good results for these spherical nuclei. In most cases, the differences between the calculated and the experimental values of $\log _ { 1 0 } T _ { 1 / 2 }$ are smaller than 0.5. The root mean square deviation between $\log _ { 1 0 } [ T _ { 1 / 2 } ^ { \mathrm { C a l } } / \mathrm { s } ]$ and $\log _ { 1 0 } [ T _ { 1 / 2 } ^ { \mathrm { E x p } } / \mathrm { s } ]$ is 0.34.

# IV. CONCLUSION

In the study of barrier penetration in nuclear physics, the parabolic approximation is usually adopted because an analytical solution exists for the penetrability of a

TABLE II: A statistics of tand the experimental values $S _ { \alpha } = \log _ { 1 0 } ( T _ { 1 / 2 } ^ { \mathrm { C a l } } / T _ { 1 / 2 } ^ { \mathrm { E x p } } )$ $\alpha$ $| \beta _ { 2 } | <$ 0.01) and the results for them are given in the last two lines.   

<table><tr><td>Nuclei</td><td>|Sα| ≤ 1</td><td>1 &lt; |Sα| ≤ 2</td><td>2 &lt; |Sα| ≤ 3</td></tr><tr><td rowspan="2">All</td><td>323</td><td>14</td><td>7</td></tr><tr><td>93.90 %</td><td>4.07 %</td><td>2.03 %</td></tr><tr><td rowspan="2">Even-even</td><td>155</td><td>3</td><td>1</td></tr><tr><td>97.48 %</td><td>1.89 %</td><td>0.63 %</td></tr><tr><td rowspan="2">Even-odd</td><td>69</td><td>2</td><td>1</td></tr><tr><td>95.83 %</td><td>2.78 %</td><td>1.39 %</td></tr><tr><td rowspan="2">Odd-even</td><td>60</td><td>4</td><td>2</td></tr><tr><td>90.91 %</td><td>6.06 %</td><td>3.03 %</td></tr><tr><td rowspan="2">Odd-odd</td><td>39</td><td>5</td><td>3</td></tr><tr><td>82.98 %</td><td>10.64 %</td><td>6.38 %</td></tr><tr><td rowspan="2">Spherical</td><td>68</td><td>0</td><td>0</td></tr><tr><td>100.00 %</td><td>0.00 %</td><td>0.00 %</td></tr></table>

TABLE III: Comparison between the calculated and experimental $\alpha$ decay half lives of 68 nuclei of which the daughter nuclei are spherical (with $| \beta _ { 2 } | < 0 . 0 1$ ). The charge and mass numbers of the $\alpha$ decay nucleus are listed in the first and the second columns.   

<table><tr><td rowspan="2">Zp</td><td rowspan="2">Ap</td><td rowspan="2">Qα (MeV)</td><td colspan="2">log10[T1/2/s]</td><td rowspan="2">Zp</td><td rowspan="2">Ap</td><td rowspan="2">Qα (MeV)</td><td colspan="2">log10[T1/2/s]</td></tr><tr><td>Cal</td><td>Exp</td><td>Cal</td><td>Exp</td></tr><tr><td>52</td><td>106</td><td>4.30</td><td>-3.83</td><td>-4.22</td><td>84</td><td>207</td><td>5.22</td><td>7.24</td><td>8.00</td></tr><tr><td>60</td><td>144</td><td>1.91</td><td>23.17</td><td>22.86</td><td>84</td><td>208</td><td>5.22</td><td>7.22</td><td>7.96</td></tr><tr><td>61</td><td>145</td><td>2.32</td><td>17.53</td><td>17.28</td><td>84</td><td>210</td><td>5.41</td><td>6.13</td><td>7.08</td></tr><tr><td>62</td><td>146</td><td>2.53</td><td>15.61</td><td>15.51</td><td>84</td><td>212</td><td>8.95</td><td>-6.58</td><td>-6.52</td></tr><tr><td>62</td><td>148</td><td>1.99</td><td>23.63</td><td>23.34</td><td>84</td><td>213</td><td>8.54</td><td>-5.58</td><td>-5.38</td></tr><tr><td>63</td><td>147</td><td>2.99</td><td>11.32</td><td>10.98</td><td>84</td><td>214</td><td>7.83</td><td>-3.62</td><td>-3.80</td></tr><tr><td>64</td><td>148</td><td>3.27</td><td>9.46</td><td>9.36</td><td>84</td><td>215</td><td>7.53</td><td>-2.71</td><td>-2.75</td></tr><tr><td>64</td><td>150</td><td>2.81</td><td>13.91</td><td>13.75</td><td>84</td><td>216</td><td>6.91</td><td>-0.61</td><td>-0.82</td></tr><tr><td>66</td><td>150</td><td>4.35</td><td>3.09</td><td>3.08</td><td>84</td><td>218</td><td>6.11</td><td>2.56</td><td>2.28</td></tr><tr><td>66</td><td>152</td><td>3.73</td><td>7.09</td><td>6.93</td><td>85</td><td>213</td><td>9.25</td><td>-6.95</td><td>-6.92</td></tr><tr><td>68</td><td>152</td><td>4.94</td><td>1.06</td><td>1.04</td><td>86</td><td>200</td><td>7.05</td><td>0.11</td><td>0.04</td></tr><tr><td>68</td><td>154</td><td>4.28</td><td>4.64</td><td>4.68</td><td>86</td><td>202</td><td>6.78</td><td>1.08</td><td>1.04</td></tr><tr><td>70</td><td>154</td><td>5.47</td><td>-0.33</td><td>-0.36</td><td>86</td><td>203</td><td>6.63</td><td>1.64</td><td>1.83</td></tr><tr><td>72</td><td>156</td><td>6.04</td><td>-1.66</td><td>-1.60</td><td>86</td><td>204</td><td>6.55</td><td>1.94</td><td>2.00</td></tr><tr><td>72</td><td>158</td><td>5.41</td><td>0.89</td><td>0.81</td><td>86</td><td>206</td><td>6.39</td><td>2.56</td><td>2.74</td></tr><tr><td>74</td><td>158</td><td>6.60</td><td>-2.76</td><td>-3.05</td><td>86</td><td>207</td><td>6.25</td><td>3.15</td><td>3.41</td></tr><tr><td>82</td><td>210</td><td>3.79</td><td>16.16</td><td>16.57</td><td>86</td><td>208</td><td>6.26</td><td>3.08</td><td>3.38</td></tr><tr><td>84</td><td>190</td><td>7.64</td><td>-2.51</td><td>-2.62</td><td>86</td><td>214</td><td>9.21</td><td>-6.52</td><td>-6.57</td></tr><tr><td>84</td><td>191</td><td>7.48</td><td>-2.03</td><td>-1.82</td><td>86</td><td>215</td><td>8.84</td><td>-5.63</td><td>-5.64</td></tr><tr><td>84</td><td>192</td><td>7.32</td><td>-1.53</td><td>-1.47</td><td>86</td><td>216</td><td>8.20</td><td>-3.93</td><td>-4.35</td></tr><tr><td>84</td><td>193</td><td>7.10</td><td>-0.80</td><td>-0.59</td><td>86</td><td>217</td><td>7.89</td><td>-3.04</td><td>-3.27</td></tr><tr><td>84</td><td>194</td><td>7.00</td><td>-0.47</td><td>-0.41</td><td>86</td><td>218</td><td>7.26</td><td>-1.02</td><td>-1.46</td></tr><tr><td>84</td><td>195</td><td>6.75</td><td>0.42</td><td>0.79</td><td>87</td><td>215</td><td>9.54</td><td>-6.94</td><td>-7.07</td></tr><tr><td>84</td><td>196</td><td>6.66</td><td>0.74</td><td>0.77</td><td>87</td><td>217</td><td>8.47</td><td>-4.32</td><td>-4.80</td></tr><tr><td>84</td><td>197</td><td>6.41</td><td>1.71</td><td>2.08</td><td>88</td><td>216</td><td>9.53</td><td>-6.59</td><td>-6.74</td></tr><tr><td>84</td><td>198</td><td>6.31</td><td>2.11</td><td>2.26</td><td>88</td><td>218</td><td>8.55</td><td>-4.17</td><td>-4.59</td></tr><tr><td>84</td><td>199</td><td>6.08</td><td>3.08</td><td>3.64</td><td>88</td><td>220</td><td>7.60</td><td>-1.35</td><td>-1.74</td></tr><tr><td>84</td><td>200</td><td>5.99</td><td>3.47</td><td>3.79</td><td>89</td><td>217</td><td>9.83</td><td>-6.93</td><td>-7.16</td></tr><tr><td>84</td><td>201</td><td>5.81</td><td>4.29</td><td>4.76</td><td>89</td><td>219</td><td>8.83</td><td>-4.56</td><td>-4.92</td></tr><tr><td>84</td><td>202</td><td>5.70</td><td>4.80</td><td>5.15</td><td>90</td><td>218</td><td>9.85</td><td>-6.65</td><td>-6.96</td></tr><tr><td>84</td><td>203</td><td>5.50</td><td>5.80</td><td>6.30</td><td>90</td><td>220</td><td>8.95</td><td>-4.51</td><td>-5.01</td></tr><tr><td>84</td><td>204</td><td>5.49</td><td>5.83</td><td>6.28</td><td>91</td><td>219</td><td>10.09</td><td>-6.85</td><td>-7.28</td></tr><tr><td>84</td><td>205</td><td>5.32</td><td>6.72</td><td>7.18</td><td>91</td><td>221</td><td>9.25</td><td>-4.93</td><td>-5.23</td></tr><tr><td>84</td><td>206</td><td>5.33</td><td>6.64</td><td>7.15</td><td>92</td><td>222</td><td>9.50</td><td>-5.20</td><td>-6.00</td></tr></table>

parabola barrier potential. The parabola approximation works indeed well both for the penetrability and for the fusion cross section at energies around or above the Coulomb barrier. But it fails at energies much smaller than the barrier height due to the long-range Coulomb interaction.

In the present work, we derived a new barrier penetration formula, Eq. (6), based on the WKB approximation. We took into account the influence of the long Coulomb tail in the barrier potential properly. Therefore this formula is especially applicable to the barrier penetration with penetration energy much lower than the Coulomb barrier. We have shown that the present analytical formula reproduces the WKB results very well.

This new penetration formula is used to calculate $\alpha$ decay half-lives of 344 nuclei with the $\alpha$ -nucleus potential given in Ref. [20]. Satisfactory agreement between the present calculation and the experiment is achieved. For spherical and even-even nuclei, the results are particularly good. Therefore, the new formula could be used in the study of barrier penetration at energies much smaller than the barrier height. Furthermore, we expect that the new formula will facilitate the study of the barrier penetrability where one has to introduce an energy-dependent one-dimensional potential barrier or a barrier distribution function.

# Acknowledgments

This work was partly supported by the National Natural Science Foundation (10575036, 10705014, and 10875157), the Major State Basic Research Development Program of China (2007CB815000), the Knowledge Innovation Project of CAS (KJCX3-SYW-N02 and KJCX2- SW-N17), and Deutsche Forschungsgemeinschaft. The computation of this work was supported by Supercomputing Center, CNIC, CAS.

# APPENDIX A: DERIVATION OF THE NEW PENETRATION FORMULA

In order to evaluate the integration $x _ { 2 }$ in Eq. (4), we divide the potential between the position of the barrier $R _ { \mathrm { B } }$ and the outer turning point $R _ { \mathrm { o u t } }$ into two parts, $R _ { \mathrm { B } } \leq$ $R \leq R _ { \mathrm { V } }$ and $R \mathrm { v } \leq R \leq R _ { \mathrm { o u t } }$ . $R _ { \mathrm { V } }$ should be large enough so that the nuclear potential vanishes for $R \geq R _ { \mathrm { V } }$ . For S

wave,

$$
\begin{array}{l} x _ {2} = 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {o u t}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} \left(V _ {\mathrm {N}} (R) + V _ {\mathrm {C}} (R) - E\right)} d R \\ = 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {V}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} \left(V _ {\mathrm {N}} (R) + V _ {\mathrm {C}} (R) - E\right)} d R \\ + 2 \int_ {R _ {\mathrm {V}}} ^ {R _ {\mathrm {o u t}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} \left(V _ {\mathrm {C}} (R) - E\right)} d R \\ = 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {V}}} \frac {\sqrt {2 \mu}}{\hbar} \sqrt {V _ {\mathrm {C}} (R) - E} \sqrt {1 + \frac {V _ {\mathrm {N}} (R)}{V _ {\mathrm {C}} (R) - E}} d R \\ + 2 \int_ {R _ {\mathrm {V}}} ^ {R _ {\mathrm {o u t}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} (V _ {\mathrm {C}} (R) - E)} d R. \tag {A1} \\ \end{array}
$$

It has been verified that when $R _ { \mathrm { V } }$ is not very close to $R _ { \mathrm { o u t } }$ , $| V _ { \mathrm { N } } ( R ) / ( V _ { \mathrm { C } } ( R ) - E ) | \ll 1$ , therefore,

$$
\begin{array}{l} x _ {2} \approx 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {V}}} \frac {\sqrt {2 \mu}}{\hbar} \sqrt {V _ {\mathrm {C}} (R) - E} \left[ 1 + \frac {1}{2} \frac {V _ {\mathrm {N}} (R)}{V _ {\mathrm {C}} (R) - E} \right] d R \\ + 2 \int_ {R _ {\mathrm {V}}} ^ {R _ {\mathrm {o u t}}} \sqrt {\frac {2 \mu}{\hbar^ {2}} \left(V _ {\mathrm {C}} (R) - E\right)} d R \\ = 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {o u t}}} \frac {\sqrt {2 \mu}}{\hbar} \sqrt {V _ {\mathrm {C}} (R) - E} d R \\ + \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {V}}} \frac {\sqrt {2 \mu}}{\hbar} \frac {V _ {\mathrm {N}} (R)}{\sqrt {V _ {\mathrm {C}} (R) - E}} d R. \tag {A2} \\ \end{array}
$$

Since the Coulomb potential outside the barrier ( $R \geq$ $R _ { \mathrm { B } }$ ) is well described by [c.f. Eq. (10],

$$
V _ {\mathrm {C}} (R) = \frac {Z _ {1} Z _ {2} e ^ {2}}{R}, \tag {A3}
$$

the first term in the above equation can be evaluated easily as,

$$
\begin{array}{l} x _ {2} ^ {(1)} \equiv 2 \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {o u t}}} \frac {\sqrt {2 \mu}}{\hbar} \sqrt {V _ {\mathrm {C}} (R) - E} d R \\ = 2 k R _ {\mathrm {B}} \left[ \tau \left(\frac {\pi}{2} - \arcsin \sqrt {\frac {1}{\tau}}\right) - \sqrt {\tau - 1} \right] (\mathrm {A} 4) \\ \end{array}
$$

with $k = \sqrt { 2 \mu E } / \hbar$ and $\tau = V _ { \mathrm { C } } ( R _ { \mathrm { B } } ) / E$ . For the evaluation of the second term in Eq. (A2), we adopt a Woods-Saxon form for the nuclear part of the barrier potential,

$$
V _ {\mathrm {N}} (R) = \frac {V _ {0}}{1 + \exp [ (R - R _ {0}) / a ]}, \tag {A5}
$$

and replace $\sqrt { V _ { \mathrm { C } } ( R ) - E }$ in the denominator by $\sqrt { V _ { \mathrm { C } } ( R _ { \mathrm { B } } ) - E }$ ,

$$
\begin{array}{l} x _ {2} ^ {(2)} \equiv \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {V}}} \frac {\sqrt {2 \mu}}{\hbar} \frac {V _ {\mathrm {N}} (R)}{\sqrt {V _ {\mathrm {C}} (R) - E}} d R \\ \approx \int_ {R _ {\mathrm {B}}} ^ {R _ {\mathrm {V}}} \frac {\sqrt {2 \mu}}{\hbar} \frac {V _ {\mathrm {N}} (R)}{\sqrt {V _ {\mathrm {C}} (R _ {\mathrm {B}}) - E}} d R \\ = \left. \frac {k}{\sqrt {\tau - 1}} \frac {V _ {0}}{E} \left\{R - a \ln \left[ 1 + e ^ {(R - R _ {0}) / a} \right] \right\} \right| _ {R _ {B}} ^ {R _ {\mathrm {V}}} \\ \approx \frac {k}{\sqrt {\tau - 1}} \frac {V _ {0}}{E} \left\{R _ {0} - R _ {B} + a \ln \left[ 1 + e ^ {\left(R _ {B} - R _ {0}\right) / a} \right] \right\} \\ = \frac {k a}{\sqrt {\tau - 1}} \frac {V _ {0}}{E} \ln \left[ 1 + e ^ {\left(R _ {0} - R _ {B}\right) / a} \right]. \tag {A6} \\ \end{array}
$$

In the above derivation, we have used the fact that $\exp { [ ( R _ { \mathrm { V } } - R _ { 0 } ) / a ] } \gg 1$ for $\alpha$ decay and penetration well below the Coulomb barrier. Finally, we have an analytical expression for $x _ { 2 }$ ,

$$
\begin{array}{l} x _ {2} = 2 k R _ {\mathrm {B}} \left[ \tau \left(\frac {\pi}{2} - \arcsin \sqrt {\frac {1}{\tau}}\right) - \sqrt {\tau - 1} \right] \\ + \frac {k a}{\sqrt {\tau - 1}} \frac {V _ {0}}{E} \ln \left[ 1 + e ^ {\left(R _ {0} - R _ {B}\right) / a} \right]. \tag {A7} \\ \end{array}
$$

[1] M. Dasgupta, D. J. Hinde, N. Rowley, and A. M. Stefanini, Annu. Rev. Nucl. Part. Sci. 48, 401 (1998).   
[2] J. F. Liang, D. Shapira, C. J. Gross, J. R. Beene, J. D. Bierman, A. Galindo-Uribarri, J. Gomez del Campo, P. A. Hausladen, Y. Larochelle, W. Loveland, et al., Phys. Rev. Lett. 91, 152701 (2003).   
[3] J. F. Liang, D. Shapira, C. J. Gross, J. R. Beene, J. D. Bierman, A. Galindo-Uribarri, J. G. del Campo, P. A. Hausladen, Y. Larochelle, W. Loveland, et al., Phys. Rev. Lett. 96, 029903 (2006).   
[4] A. S. Umar and V. E. Oberacker, Phys. Rev. C 76, 014614 (2007).   
[5] A. N. F. Aleixo, A. B. Balantekin, and M. A. C. Ribeiro, J. Phys. A 33, 1503 (2000).   
[6] E. C. Kemble, Phys. Rev. 48, 549 (1935).   
[7] D. L. Hill and J. A. Wheeler, Phys. Rev. 89, 1102 (1953).   
[8] C. Y. Wong, Phys. Rev. Lett. 31, 766 (1973).   
[9] N. Wang, K. Zhao, W. Scheid, and X. Wu, Phys. Rev. C 77, 014603 (2008).   
[10] R. Smolanczuk, Phys. Rev. C 78, 024601 (2008).   
[11] K. Hagino, Ph.D. thesis, Tohoku University (1998).   
[12] A. K. Mohanty, S. V. S. Sastry, S. K. Kataria, and V. S. Ramamurthy, Phys. Rev. Lett. 65, 1096 (1990).   
[13] N. Rowley, G. R. Satchler, and P. H. Stelson, Phys. Lett. B 254, 25 (1991).   
[14] V. I. Zagrebaev, Y. Aritomo, M. G. Itkis, Y. T. Oganessian, and M. Ohta, Phys. Rev. C 65, 014607 (2001).   
[15] Z.-Q. Feng, G.-M. Jin, F. Fu, and J.-Q. Li, Nucl. Phys. A 771, 50 (2006).   
[16] Z.-Q. Feng, G.-M. Jin, J.-Q. Li, and W. Scheid, Phys. Rev. C 76, 044606 (2007).   
[17] N. Wang, J.-Q. Li, and E.-G. Zhao, Phys. Rev. C 78, 054607 (2008).   
[18] B. Buck, J. C. Johnston, A. C. Merchant, and S. M.

Perez, Phys. Rev. C 53, 2841 (1996).   
[19] C. Xu and Z. Ren, Nucl. Phys. A 753, 174 (2005).   
[20] V. Y. Denisov and H. Ikezoe, Phys. Rev. C 72, 064613 (2005).   
[21] C. Xu and Z. Ren, Nucl. Phys. A 760, 303 (2005).   
[22] Z. Dupre and T. Buervenich, Nucl. Phys. A 767, 81 (2006).   
[23] S. B. Duarte, O. A. P. Tavares, F. Guzman, A. Dimarco, F. Garecia, O. Rodriguez, and M. Goncalves, At. Data Nucl. Data Tables 80, 235 (2002).   
[24] G. Royer, J. Phys. G 26, 1149 (2000).   
[25] G. Audi, O. Bersillon, J. Blachot, and A. H. Wapstra, Nuclear Physics A 729, 3 (2003).   
[26] J. K. Tuli, Nuclear wallet cards 2005 (7th edition), Brookhaven National Laboratory, (2005).   
[27] G. Audi, O. Bersillon, J. Blachot, and A. H. Wapstra, Nucl. Phys. A 624, 1 (1997).   
[28] P. Moeller, J. R. Nix, W. D. Myers, and W. J. Swiatecki, At. Data Nucl. Data Tables 59, 185 (1995).   
[29] H. Zhang, W. Zuo, J. Li, and G. Royer, Phys. Rev. C 74, 017304 (2006).   
[30] J. C. Pei, F. R. Xu, Z. J. Lin, and E. G. Zhao, Phys. Rev. C 76, 044326 (2007).   
[31] T. L. Stewart, M. W. Kermode, D. J. Beachey, N. Rowley, I. S. Grant, and A. T. Kruppa, Phys. Rev. Lett. 77, 36 (1996).   
[32] T. L. Stewart, M. W. Kermode, D. J. Beachey, N. Rowley, I. S. Grant, and A. T. Kruppa, Nucl. Phys. A 611, 332 (1996).   
[33] C. Xu and Z. Ren, Phys. Rev. C 73, 041301 (2006).   
[34] S. Raman, C. W. Nestor, and P. Tikkanen, At. Data Nucl. Data Tables 78, 1 (2001).