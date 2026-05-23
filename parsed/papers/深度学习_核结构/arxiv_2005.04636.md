# The study of Nuclear binding energy for $\mathbf { A } \geq \mathbf { 1 0 0 }$ based on Odd-Even staggering of nuclear masses

B. B. Jiao ∗

School of Nuclear Science and Engineering, East China University of Technology Nanchang 330013, People’s Republic of China

Accurate measurement of nuclear masses plays a key role in the nuclear physics, nuclear technology and astrophysical fields, especially in the calculation of nucleosynthesis and fast neutron capture processes. The existing nuclear masses formula and nuclear masses model has undoubtedly achieved very good results, but it is still not satisfactory for some nuclear masses (especially near the neutron drip line), and even many nuclear masses have no prediction. Although there are many studies in Odd-Even staggering (OES) of nuclear masses, but the research on nuclear masses by using the systematicness of OES is indeed very few. Our purpose in this paper is to describe an empirical formula for Odd-Even staggering of nuclear masses that can be useful in describing and predicting nuclear masses. We empirically obtained the formula of odd- $Z$ (odd- $N$ ) nuclei and even- $Z$ (even- $N$ ) nuclei based on studying the OES of nuclear masses (AME2012), where $Z$ and $N$ represent the number of proton and neutron. Then describe and predict the nuclear masses with mass number $A \ge 1 0 0$ . With the proton (neutron) empirical pairing gap from the OES of the binding energies and AME2012 database, the root-mean-square deviation of even- $Z$ nuclei and odd- $Z$ nuclei that we have successfully obtained 208 keV and 238 keV, respectively. The RMSD of even- $N$ nuclei and odd- $N$ nuclei is 222 keV and 240 keV. The result shows that our predicted values are compared well with values in AME2016, and some predicted values agree better with the experimental values. These results demonstrate that our empirical formulas have good accuracy and reliability. Another advantage of these formulas is that they use less known nuclear masses to predict unknown nuclear masses. In addition, this paper also uses BP neural network to study proton Odd-Even staggering of nuclear masses (even- $Z$ and odd- $Z$ nuclei) and neutron Odd-Even staggering of nuclear masses (even- $N$ and odd- $N$ nuclei). The RMSD of even- $Z$ and odd- $Z$ nuclei is 141 keV and 159 keV; the RMSD of even- $N$ and odd- $N$ nuclei is 150 keV and 160 keV. The results show that the RMSD of nuclear masses based on neural network 60-80 keV decrease than that based on empirical formula (the accuracy is increased by about 32%). Accurate nuclear mass is helpful to the research of nuclear physics, nuclear technology and astrophysics.

keywords: nuclear masses; Odd-Even staggering of nuclear masses; neural network.

PACS numbers: 21.10.Dr; 07.05.Mh.

# 1. Introduction

Nuclear masses has attracted much attention[1-22]. Precise prediction and measurement of nuclear mass have always been an important issue in nuclear physics and astrophysics. It is found that the static mass of the nucleus is always less than the sum of the mass of the nucleon that makes up the nucleus, the difference is the mass excess. The study of nuclear mass based on global mass relation $\lfloor 1 - 1 1 \rfloor$ and regional mass relation $\lfloor 1 4 - 2 2 \rfloor$ is of great concern. At present, the comprehensive databases are AME2003[14], AME2012[15] and AME2016[16].

The phenomenon of pair correlation that people notice is the Odd-Even staggering of nuclear masses. In recent years, more and more people have paid close attention to the study of Odd-Even staggering of nuclear masses $[ 2 3 - 2 6 ]$ , but few people use Odd-Even staggering of nuclear masses to systematically describe and predict nuclear masses. This paper describes and predicts the nuclear masses based on the systematic study of Odd-Even staggering of nuclear masses. We obtained the empirical formula of odd- $Z$ (odd- $N$ ) nuclei and even- $Z$ (even- $N$ ) nuclei based on the Odd-Even staggering of nuclear masses by AME2012 database, and then obtained the nuclear masses of calculation. The RMSD of even- $Z$ nuclei and odd- $Z$ nuclei is 208 keV and 238 keV; the RMSD of even- $N$ nuclei and odd- $N$ nuclei is 222 keV and 240 keV, respectively. In addition, there are many papers using artificial neural networks in nuclear physics [27-37] and other subjects [38-40]. In the 1990s, people have used neural networks [27] to predict the mass of atomic nuclei. Research in recent years, many improvements have been made based on the neural network approach to reduce the deviation of the calculated values or the predicted values [34-37]. Ref. [34] shows that the accuracy of the Duflo-Zuker mass formula is improved by using the Bayesian neural network approach, the RMSD is reduced from 503 keV to 286 keV (the accuracy is increased by about 40% ); Ref. [37] used Levenberg-Marquardt neural network approach to study the nuclear masses in AME2012 database, results show that Levenberg-Marquardt neural network method is helpful to improve the accuracy of mass models, for a simple liquid drop formula: the RMSD between the predicted value and the 2353 experimental known masses decreased sharply from 2.455 MeV to 0.235 MeV, while for some other mass models, the accuracy is improved by about 30%. This paper we use BP neural network to study the Odd-Even staggering of nuclear masses (AME2012 database). Results show that the RMSD based on the neural network combined with Odd-Even staggering of nuclear masses is 60-80 keV less than that based on empirical formula (the accuracy is increased by about 32%). The RMSD of even- $Z$ nuclei and odd- $Z$ nuclei is 141 keV and 159 keV; the RMSD of even- $N$ nuclei and odd- $N$ nuclei is 150 keV and 160 keV, respectively.

In this paper, we use Odd-Even staggering of nuclear masses combined with AME2012 database to study the nuclear masses of $A \ \geq \ 1 0 0$ . In Sec. 2, we use the known nuclear mass in ame2012 database and the three parameters Odd-Even staggering of nuclear masses formula to get many data sets of nuclear masses. The empirical formulas are obtained based on the selected nuclei, and then calculated

the nuclei with known mass. In Sec. 3, we used BP neural network to study the Odd-Even staggering of nuclear masses, and then obtained the RMSD of known masses nuclei based on BP neural network and databases. In Sec. 4, compares the predicted value calculated by empirical formulas (BP neural network method) and AME2012 database with the experimental value in AME2016, which shows that the predicted value in this paper is close to the experimental value. In Sec. 5, discusses and summarizes this article.

# 2. The method of empirical formula

There are several kinds of pairing gap parameters $\lfloor 2 3 - 2 6 \rfloor$ , here we study the threepoint formula $\Delta _ { p } ^ { ( 3 ) }$ and $\Delta _ { n } ^ { ( 3 ) }$ for proton pairing gaps and neutron pairing gaps,

$$
\begin{array}{l} \Delta_ {p} ^ {(3)} (Z, N) = \frac {1}{2} [ B (Z + 1, N) - 2 B (Z, N) + B (Z - 1, N) ] \\ = \frac {1}{2} \left[ S _ {p} (Z + 1, N) - S _ {p} (Z, N) \right]. \tag {1} \\ \end{array}
$$

$$
\begin{array}{l} \Delta_ {n} ^ {(3)} (Z, N) = \frac {1}{2} [ B (Z, N + 1) - 2 B (Z, N) + B (Z, N - 1) ] \\ = \frac {1}{2} \left[ S _ {n} (Z, N + 1) - S _ {n} (Z, N) \right]. \tag {2} \\ \end{array}
$$

where $B ( Z , N )$ denotes the binding energy of the $( Z , N )$ nucleus with $A = Z + N$ .

Here we define the binding energy as a positive value, which is easy to get:

$$
\Delta_ {p} ^ {(3)} (Z, N) = \frac {1}{2} [ 2 M (Z, N) - M (Z - 1, N) - M (Z + 1, N) ]. \tag {3}
$$

$$
\Delta_ {n} ^ {(3)} (Z, N) = \frac {1}{2} [ 2 M (Z, N) - M (Z, N - 1) - M (Z, N + 1) ]. \tag {4}
$$

The experimental nuclear mass is usually determined from the known atomic mass in AME databases. However, electron binding energy and Coulomb energy are usually neglected in nuclear mass studies. It can be seen from eqs. (3) and (4) that the electron mass does not affect the calculation of OES of nuclear masses. Therefore, we assume that the atomic mass is equal to the nuclear mass in this section.

As is depicted in Fig. 1, the OES of nuclear masses for even- $Z$ nuclei is less than zero and the OES of nuclear masses for odd- $Z$ nuclei is greater than zero. It can

![](images/4bd68b61c05972929d918e83000cbee4c40ac32dbda19e536a2212bec4030a53.jpg)  
Fig. 1. (Color online) The odd-even staggering of nuclear masses for proton. We present separately for nuclei with even- $Z$ (green circles) and odd- $Z$ (red circles). The black circles represent the OES of nuclear masses with $Z = 5 0 , 8 2$ (the nuclei with a magic number of protons). The yellow and blue curve are plotted in terms of Eq. (5).

be seen from Fig.1 that the black circles are different from red circles and green circles, so the OES of nuclear masses for nuclei with $Z = 5 0 , 8 2$ are not included. In addition, the OES of nuclear masses has certain linear characteristics. Based on this behavior, we obtained the ${ \Delta } _ { p } ^ { ( 3 ) }$ formulas of even- $Z$ and odd- $Z$ nuclei for $A \geq 1 0 0$ :

$$
\overline {{\Delta_ {p - e v e n} ^ {(3)}}} (A) \simeq \frac {- 3 9 6 0 0 \cdot \ln A}{A} \mathrm {k e V},
$$

$$
\overline {{\Delta_ {p - o d d} ^ {(3)}}} (A) \simeq \frac {2 6 0 0 0 \cdot \ln A}{A} \mathrm {k e V}. \tag {5}
$$

Fig. 2 shows that the OES of nuclear masses for even- $N$ nuclei is less than zero and the OES of nuclear masses for odd- $N$ nuclei is greater than zero. In Fig.2, the black circles are different from red circles and green circles, so the OES of nuclear masses for nuclei with N = 82, 126 are not included. In addition, the OES of nuclear masses has certain linear characteristics, then we obtained the $\Delta _ { n } ^ { ( 3 ) }$ formulas of even- $N$ and odd- $N$ nuclei for $A \geq 1 0 0$ :

$$
\overline {{\Delta_ {n - e v e n} ^ {(3)}}} (A) \simeq \frac {- 3 2 6 0 0 \cdot \ln A}{A} \mathrm {k e V},
$$

$$
\overline {{\Delta_ {n - o d d} ^ {(3)}}} (A) \simeq \frac {2 6 0 0 0 \cdot \ln A}{A} \mathrm {k e V}. \tag {6}
$$

Interestingly, the empirical formula of odd- $Z$ nuclei and odd- $N$ nuclei are on the same. In addition, then we can easy get the formula of nuclear masses based on Eqs. (3) and (4).

![](images/08c6a07da87c18c1f93fb796ce67310ef05a62d52a7df64d7f0fd0e13b94938d.jpg)  
Fig. 2. (Color online) The odd-even staggering of nuclear masses for neutron. We present separately for nuclei with even- $Z$ (green circles) and odd- $Z$ (red circles), where black circles represent the OES of nuclear masses with $N = 8 2 , 1 2 6$ (the nuclei with a magic number of neutrons). The yellow and blue curve are plotted in terms of Eq. (6).

$$
M (Z, N) = \frac {2 \Delta_ {p} ^ {(3)} (A) + M (Z - 1 , N) + M (Z + 1 , N)}{2}, \tag {7}
$$

$$
M (Z, N) = \frac {2 \Delta_ {n} ^ {(3)} (A) + M (Z , N - 1) + M (Z , N + 1)}{2}. \tag {8}
$$

Result shows that the RMSD of even- $Z$ and odd- $Z$ nuclei is 208 keV and 238 keV; the RMSD of even- $N$ and odd- $N$ nuclei is 222 keV and 240 keV, respectively. Calculated values confirm that our new formula can be used to calculate and predict nuclear masses.

The nuclear mass is equal to the atomic mass minus masses of electrons and Coulomb energy plus the electron binding energy. However, the electron binding energy, the electron mass and the Coulomb energy are often neglected in the research of nuclear masses. But in this section, the role of the electron binding energy and the Coulomb energy are studied. Because the electron mass has no effect on the odd even difference, therefore the electron mass is neglected in our studies. The formula of nuclear masses is given by[46]: $M ^ { * } ( Z , N ) = M ( Z , N ) + B _ { e } ( Z ) - B _ { e } ^ { f i t } ( Z , A )$ . Where the formulas of the electron binding energy ( $B _ { e }$ ) and the Coulomb energy $( B _ { e } ^ { f i t } )$ derived from [15] are respectively

$$
B _ {e} (Z) = 1 4. 4 3 8 1 \cdot Z ^ {2. 3 9} + 1. 5 5 4 6 8 \cdot 1 0 ^ {- 6} \cdot Z ^ {5. 3 5} \mathrm {e V}, \tag {9}
$$

![](images/5c85f7efaf3ef2a03ff6d4efdf67c00ce6453510f28eb82b51f74978dfb233a9.jpg)  
Fig. 3. (Color online) The difference of RMSD for even- $Z$ nuclei.

$$
B _ {e} ^ {f i t} (Z, A) = 5 0 5 \cdot \frac {Z ^ {2}}{A ^ {1 / 3}} \cdot \left(1 - 0. 7 6 \cdot Z ^ {- 2 / 3}\right) \mathrm {e V}. \tag {10}
$$

It can be seen from Eqs. (7) and (8) that the electron binding energy and Coulomb energy are only significant for the proton OES of nuclear masses. In this section, we introduce the electron binding energy and Coulomb energy to obtain the new nuclear masses, and then obtain the known nuclear masses based on formula (7). Fig. 3 and Fig. 4 represents the RMSD of the masses of even- $Z$ and odd- $Z$ nuclei, respectively . We assume that the atomic mass is equal to the nuclear mass, by using the empirical formula combination (7) and even- $Z$ (odd- $Z$ ) OES obtained the RMSD of the known nuclear mass is $\sigma _ { 1 }$ ( $\sigma _ { 5 }$ ); when the binding energy of electron is considered, the RMSD is $\sigma _ { 2 }$ ( $\sigma _ { 6 }$ ); the RMSD obtained by considering Coulomb energy in nuclear mass is $\sigma _ { 3 }$ ( $o _ { 7 }$ ); when the nuclear mass is obtained after used the electron binding energy to minus the Coulomb energy, and then obtained the RMSD is $\sigma _ { 4 }$ ( $o _ { 8 }$ ).

The points in Fig. 3 represent the RMSD of nuclear masses, and the number of nuclei between the two points is 10. Red dot line represents the difference of RMSD between the $\sigma _ { 2 }$ and $\sigma _ { 1 }$ . The difference is greater than 0 means that the introduction of electron binding energy leads to the increase of the deviation, and the larger nuclear mass, the greater deviation will be obtained. The black dot line represents the difference of RMSD between the $\sigma _ { 3 }$ and $\sigma _ { 1 }$ . The difference is less than 0 means that the increase of Coulomb energy reduces the deviation, and the larger nuclear mass, the smaller deviation will be obtained. The green solid rectangular dotted line represents the difference of RMSD between the $\sigma _ { 4 }$ and $\sigma _ { 1 }$ . The difference is greater than 0 and less than the red dotted line indicates means that the Coulomb energy offsets part of the electron binding energy. However, the introduction of these two energies will cause the deviation to increase.

![](images/cf16f202b5bf5952f2324a23b2bdb5b2ac922ecefa2edb1cdf0f6d08d263aa3d.jpg)  
Fig. 4. (Color online) The difference of RMSD for odd- $Z$ nuclei.

# 3. The method of BP neural network

In addition, our paper using the ’newff’ function provided by the neural network toolbox of MATLAB 2015b to create the forward BP neural network, and then to study the OES of nuclear masses. We study the OES of nuclear masses based on the neural network function of tansig $[ f ( x ) = 2 / ( 1 + e ^ { - 2 x } ) - 1 ]$ , which the function comes from the neural network toolbox in MATLAB 2015b. The data sets Z, N, $\Delta _ { p } ^ { ( 3 ) } ( Z , N )$ [or $\Delta _ { n } ^ { ( 3 ) } ( Z , N ) ]$ (calculated values of the OES of nuclear masses for known mass) as the input sample(that is training data) for the network. After training obtained the residual interaction $\Delta _ { p } ^ { ( 3 ) } ( Z , N )$ [or $\Delta _ { n } ^ { ( 3 ) } ( Z , N ) ]$ [analog values of the OES of nuclear masses for known mass] and ${ \Delta } _ { p } ^ { ( 3 ) } ( Z 1 , N 1 )$ [or $\Delta _ { n } ^ { ( 3 ) } ( Z 1 , N 1 ) ]$ [predicted value of the OES of nuclear masses for unknown mass]. Using OES of nuclear masses and Eqs. (7) and (8), combined with AME2012 and AME2016, the values of the known nuclear masses were calculated and the values of unknown nuclear masses were predicted. Then, the RMSD between the calculated values of nuclear mass and the corresponding experimental values in AME2012 and AME2016 was obtained.

In this section, we study the OES of even- $Z$ and odd- $Z$ nuclear masses respectively. Using BP neural network got the fitting values of OES of nuclear masses, then obtained the calculated values of known masses. Fig. 5 shows the RMSD between the calculated values of even- $Z$ (odd- $Z$ ) nuclear masses and the experimental values in AME2012 (AME2016) database. The line in black (blue) represents the RMSD of comparing the calculated values (we obtained the calculated values based on AME2012) of even- $Z$ (odd- $Z$ ) nuclei masses with the experimental values in AME2012 database. The curve in red(pink) is plotted by using the RMSD between calculated values (we obtained the calculated values based on AME2016) of even- $Z$ (odd- $Z$ ) nuclei and experimental values in AME2016 database. The results show that the accuracy of the OES of nuclear masses is significantly improved by using BP neural network approach, the RMSD relative to experiment is reduced about

![](images/23de30e8ec2338e500ef8fba05971c01739038d3d6138db915dc900749b29be9.jpg)  
Fig. 5. (Color online) The RMSD for even- $Z$ and odd- $Z$ nuclei.

![](images/22df2be2efa123587d125d891c32ea7be802aac7abc7eeaceed0d4698c63bbf0.jpg)  
Fig. 6. (Color online) The RMSD for even- $N$ and odd- $N$ nuclei.

70 keV.

In Fig. 6, the lines represent the RMSD between the calculated values of even-$N$ (odd- $N$ ) nuclear masses and the experimental values in AME2012 (AME2016) database. We use the black (blue) line represents the RMSD between calculated values (we obtained the calculated values based on AME2012) of even-N(odd- $N$ ) nuclear masses and experimental values in AME2012 database. The curve in red(pink) corresponds to the RMSD between calculated values (we obtained the calculated values based on AME2016) of even- $N$ (odd- $N$ ) nuclei and experimental values in AME2016 database. The result shows that the accuracy of the empirical formula of OES is significantly improved by using BP neural network approach, the RMSD relative to experiment is reduced about 70 keV.

Figs. 5 and 6 show that the calculated values of nuclear masses based on BP neural network is better than that using empirical formulas, the accuracy is increased by about 32%. The accuracy of nuclear masses based on the proposed BP neural network method is better than that using empirical formulas, which we can also use Eqs. (7) and (8) combination BP neural network obtained the predicted values of nuclear masses.

# 4. Prediction of nuclear masses

In this section, we used the predictable formula of nuclear masses to predict the nuclear masses that are difficult to be measured experimentally. The main idea of nuclear mass prediction is to get the $\Delta _ { p } ^ { ( 3 ) } ( Z , N )$ and $\Delta _ { n } ^ { ( 3 ) } ( Z , N )$ of unknown mass, then calculate the unknown nuclear mass combined with Eq.(7) , Eq.(8) and AME2016 database. The OES of nuclear masses of unknown mass nuclei is obtained based on the empirical formulas and BP neural network method. In table 1 and 2 we present a set of values among our predicted values, then compare with experimental and predicted values in AME2016.

We obtained the predicted values of unknown mass based on $\Delta _ { p } ^ { ( 3 ) } ( Z , N )$ [Eq. (5)] and Eq.(7). In Table 1, we give 38 predicted values in comparison with the dates in AME2016. ME $\bot$ and ME $^ 2$ are obtained based on empirical formula and BP neural network method respectively. The dev0 represents the deviation of mass excess in AME2016 database; dev1 is the difference between the values (ME2016) of the mass excess in the AME2016 database and our predicted values (ME1); we use dev2 to represents the difference between the values (ME2016) and our predicted values (ME $^ 2$ ). There are five predicted values( $^ { 1 4 1 } I$ , ${ } ^ { 1 9 0 } T l$ , $^ { 1 9 4 } B i$ , $^ { 1 9 8 } A t$ , ${ } ^ { 2 0 2 } F r$ ) have their experimental values in AME2016 database. We found that our predicted values of simulation is according with experiment. The predicted values we get also agree with those in the AME2016 database, especially for those heavy nuclei and superheavy nuclei. In addition, the RMSD between our calculated values (ME $\bot$ ) and the AME2016 database (ME2016) is 182keV, and the RMSD between ME2016 and ME $^ { 1 2 }$ is 167keV. It can be seen that the deviation of predicted values based on neural network is smaller than that based on empirical formulas.

By using $\Delta _ { n } ^ { ( 3 ) } ( Z , N )$ [Eq. (6)] and Eq.(8) obtained the predicted values. Table 2 lists 38 predicted values in comparison with the dates in the AME2016 database. Where, ME $^ { 3 }$ (ME $^ 4$ ) are obtained based on empirical formula (BP neural network method). The dev0 is the deviation of mass excess in AME2016 database; dev3 is the difference between the values (ME2016) of the mass excess in the AME2016 database and our predicted values (ME $^ { 3 }$ ); we use dev4 to represents the difference between the values (ME2016) and our predicted values (ME $^ 4$ ). Table 2 shows that our predicted values are close to the data in AME2016 database, and the prediction value is more accurate in the heavy nuclear region. Moreover, the RMSD between ME2016 and ME $\bot$ is 232keV, and the RMSD between ME2016 and ME $^ 2$ is 190keV. Again, it is shown that the predicted value obtained by neural network is more

<table><tr><td>Nucl.</td><td>ME2016</td><td>dev0</td><td>ME1</td><td>ME2</td><td>dev1</td><td>dev2</td></tr><tr><td>101In</td><td>-68610</td><td>200</td><td>-68372</td><td>-68700</td><td>-238</td><td>90</td></tr><tr><td>114I</td><td>-72800</td><td>150</td><td>-72418</td><td>-72455</td><td>-382</td><td>-345</td></tr><tr><td>116Cs</td><td>-62040</td><td>100</td><td>-62070</td><td>-62031</td><td>30</td><td>-9</td></tr><tr><td>139Gd</td><td>-57630</td><td>200</td><td>-57521</td><td>-57745</td><td>-109</td><td>115</td></tr><tr><td>141I</td><td>-59927</td><td>16</td><td>-59878</td><td>-60239</td><td>-49</td><td>312</td></tr><tr><td>150Tm</td><td>-46490</td><td>200</td><td>-46771</td><td>-46341</td><td>281</td><td>-149</td></tr><tr><td>167Re</td><td>-34830</td><td>40</td><td>-35138</td><td>-34976</td><td>308</td><td>146</td></tr><tr><td>170Ir</td><td>-23360</td><td>90</td><td>-23308</td><td>-23073</td><td>-52</td><td>-287</td></tr><tr><td>174Au</td><td>-14240</td><td>90</td><td>-14185</td><td>-13943</td><td>-55</td><td>-297</td></tr><tr><td>178Tl</td><td>-4790</td><td>90</td><td>-4607</td><td>-4355</td><td>-183</td><td>-435</td></tr><tr><td>178Ta</td><td>-50600</td><td>50</td><td>-50331</td><td>-50528</td><td>-269</td><td>-72</td></tr><tr><td>185Bi</td><td>-2234</td><td>80</td><td>-2744</td><td>-2517</td><td>510</td><td>283</td></tr><tr><td>190Tl</td><td>-24372</td><td>8</td><td>-24211</td><td>-24137</td><td>-161</td><td>-235</td></tr><tr><td>194Bi</td><td>-16029</td><td>6</td><td>-15920</td><td>-15792</td><td>-109</td><td>-237</td></tr><tr><td>198At</td><td>-6715</td><td>6</td><td>-6732</td><td>-6517</td><td>17</td><td>-198</td></tr><tr><td>202Fr</td><td>3096</td><td>7</td><td>2983</td><td>3186</td><td>113</td><td>-90</td></tr><tr><td>222Pa</td><td>22160</td><td>70</td><td>22023</td><td>22110</td><td>137</td><td>50</td></tr><tr><td>232Am</td><td>43340</td><td>300</td><td>43401</td><td>43447</td><td>-61</td><td>-107</td></tr><tr><td>232Np</td><td>37360</td><td>100</td><td>37542</td><td>37442</td><td>-182</td><td>-82</td></tr><tr><td>233Am</td><td>43260</td><td>100</td><td>43154</td><td>43161</td><td>106</td><td>99</td></tr><tr><td>236Am</td><td>46040</td><td>110</td><td>46319</td><td>46226</td><td>-279</td><td>-186</td></tr><tr><td>237Am</td><td>46570</td><td>60</td><td>46776</td><td>46657</td><td>-206</td><td>-87</td></tr><tr><td>239Bk</td><td>54250</td><td>210</td><td>54316</td><td>54277</td><td>-66</td><td>-27</td></tr><tr><td>241Bk</td><td>56030</td><td>200</td><td>56150</td><td>56049</td><td>-120</td><td>-19</td></tr><tr><td>245Es</td><td>66370</td><td>200</td><td>66420</td><td>66346</td><td>-50</td><td>24</td></tr><tr><td>246Am</td><td>64994</td><td>18</td><td>64941</td><td>64950</td><td>53</td><td>44</td></tr><tr><td>247Am</td><td>67150</td><td>100</td><td>66976</td><td>66980</td><td>174</td><td>170</td></tr><tr><td>248Es</td><td>70300</td><td>50</td><td>70392</td><td>70265</td><td>-92</td><td>35</td></tr><tr><td>248Bk</td><td>68080</td><td>70</td><td>68210</td><td>68176</td><td>-130</td><td>-96</td></tr><tr><td>249Es</td><td>71180</td><td>30</td><td>71235</td><td>71112</td><td>-55</td><td>68</td></tr><tr><td>250Es</td><td>73230</td><td>100</td><td>73416</td><td>73311</td><td>-186</td><td>-81</td></tr><tr><td>252Md</td><td>80510</td><td>130</td><td>80729</td><td>80621</td><td>-219</td><td>-111</td></tr><tr><td>252Bk</td><td>78540</td><td>200</td><td>78548</td><td>78548</td><td>-8</td><td>-8</td></tr><tr><td>253Md</td><td>81170</td><td>30</td><td>81342</td><td>81230</td><td>-172</td><td>-60</td></tr><tr><td>254Md</td><td>83450</td><td>100</td><td>83647</td><td>83545</td><td>-197</td><td>-95</td></tr><tr><td>256Md</td><td>87460</td><td>120</td><td>87591</td><td>87544</td><td>-131</td><td>-84</td></tr><tr><td>257Lr</td><td>92670</td><td>40</td><td>92646</td><td>92551</td><td>24</td><td>119</td></tr><tr><td>263Bh</td><td>114500</td><td>310</td><td>114518</td><td>114519</td><td>-18</td><td>-19</td></tr><tr><td>Nucl.</td><td>ME2016</td><td>dev0</td><td>ME3</td><td>ME4</td><td>dev3</td><td>dev4</td></tr><tr><td>101In</td><td>-68610</td><td>200</td><td>-68993</td><td>-68810</td><td>383</td><td>200</td></tr><tr><td>114I</td><td>-72800</td><td>150</td><td>-72645</td><td>-72521</td><td>-155</td><td>-279</td></tr><tr><td>118Ba</td><td>-62350</td><td>200</td><td>-62424</td><td>-62595</td><td>74</td><td>245</td></tr><tr><td>129Cd</td><td>-63058</td><td>17</td><td>-63405</td><td>-63734</td><td>347</td><td>676</td></tr><tr><td>141I</td><td>-59927</td><td>16</td><td>-60327</td><td>-59926</td><td>400</td><td>-1</td></tr><tr><td>153Yb</td><td>-47210</td><td>200</td><td>-47269</td><td>-47261</td><td>59</td><td>51</td></tr><tr><td>154Lu</td><td>-39720</td><td>200</td><td>-39634</td><td>-39595</td><td>-86</td><td>-125</td></tr><tr><td>157Hf</td><td>-38900</td><td>200</td><td>-39145</td><td>-39131</td><td>245</td><td>231</td></tr><tr><td>158Ta</td><td>-31170</td><td>200</td><td>-31208</td><td>-31193</td><td>38</td><td>23</td></tr><tr><td>161W</td><td>-30560</td><td>200</td><td>-30865</td><td>-30801</td><td>305</td><td>241</td></tr><tr><td>162Re</td><td>-22500</td><td>200</td><td>-22630</td><td>-22587</td><td>130</td><td>87</td></tr><tr><td>165Os</td><td>-21800</td><td>200</td><td>-22148</td><td>-22016</td><td>348</td><td>216</td></tr><tr><td>165Tb</td><td>-60570</td><td>100</td><td>-60989</td><td>-60677</td><td>419</td><td>107</td></tr><tr><td>167Re</td><td>-34840</td><td>40</td><td>-34843</td><td>-35099</td><td>3</td><td>259</td></tr><tr><td>169Pt</td><td>-12510</td><td>200</td><td>-12890</td><td>-12691</td><td>380</td><td>181</td></tr><tr><td>170Ir</td><td>-23360</td><td>90</td><td>-23459</td><td>-23127</td><td>99</td><td>-233</td></tr><tr><td>173Hg</td><td>-2710</td><td>200</td><td>-3101</td><td>-2840</td><td>391</td><td>130</td></tr><tr><td>174Au</td><td>-14240</td><td>90</td><td>-14343</td><td>-13967</td><td>103</td><td>-273</td></tr><tr><td>178Tl</td><td>-4790</td><td>90</td><td>-5043</td><td>-4621</td><td>253</td><td>-169</td></tr><tr><td>178Ta</td><td>-50600</td><td>50</td><td>-50279</td><td>-50414</td><td>-321</td><td>-186</td></tr><tr><td>182Lu</td><td>-41880</td><td>200</td><td>-41511</td><td>-41702</td><td>-369</td><td>-178</td></tr><tr><td>185Bi</td><td>-2240</td><td>80</td><td>-1889</td><td>-2100</td><td>-351</td><td>-140</td></tr><tr><td>190Tl</td><td>-24372</td><td>8</td><td>-24722</td><td>-24422</td><td>350</td><td>50</td></tr><tr><td>194Bi</td><td>-16029</td><td>6</td><td>-16241</td><td>-15877</td><td>212</td><td>-152</td></tr><tr><td>198At</td><td>-6715</td><td>6</td><td>-6887</td><td>-6505</td><td>172</td><td>-210</td></tr><tr><td>198Ir</td><td>-25820</td><td>200</td><td>-25636</td><td>-25683</td><td>-184</td><td>-137</td></tr><tr><td>202Fr</td><td>3096</td><td>7</td><td>2924</td><td>3276</td><td>172</td><td>-180</td></tr><tr><td>212Tl</td><td>-1550</td><td>200</td><td>-1488</td><td>-1497</td><td>-62</td><td>-53</td></tr><tr><td>220Pa</td><td>20220</td><td>50</td><td>20098</td><td>20198</td><td>122</td><td>22</td></tr><tr><td>222Pa</td><td>22160</td><td>70</td><td>21983</td><td>22096</td><td>177</td><td>64</td></tr><tr><td>226Np</td><td>32780</td><td>90</td><td>32701</td><td>32834</td><td>79</td><td>-54</td></tr><tr><td>232Np</td><td>37360</td><td>100</td><td>37400</td><td>37352</td><td>-40</td><td>8</td></tr><tr><td>235Cm</td><td>48030</td><td>200</td><td>47895</td><td>47881</td><td>135</td><td>149</td></tr><tr><td>241Cf</td><td>59330</td><td>170</td><td>59282</td><td>59227</td><td>48</td><td>103</td></tr><tr><td>243Cf</td><td>60990</td><td>110</td><td>61023</td><td>60951</td><td>-33</td><td>39</td></tr><tr><td>247Fm</td><td>71670</td><td>120</td><td>71625</td><td>71579</td><td>45</td><td>91</td></tr><tr><td>248Bk</td><td>68080</td><td>70</td><td>68251</td><td>68162</td><td>-171</td><td>-82</td></tr><tr><td>256Md</td><td>87460</td><td>120</td><td>87486</td><td>87484</td><td>-26</td><td>-24</td></tr></table>

From table 1 and table 2 we can see that our predicted values are close to the experimental values and predicted values, and some nuclear mass deviations are only tens of keV. Although the deviation of some nuclear masses larger than is desired, it has little effect on the overall prediction of nuclear masses. Therefore, both empirical formula and neural network method can be used to predict nuclear masses. In addition, the results show that the predicted values of unknown masses based on BP neural network are better than that using empirical formulas. More accurate predictions could be readily made if the OES of nuclear masses was more accurate.

# 5. Discussion and Conclusions

In this paper we study the OES of nuclear masses for even- $Z$ and odd- $Z$ nuclei (even-N and odd-N nuclei), then obtained the calculated and predicted values of nuclear masses. In Sec. 2, the empirical formulas obtained from studying the OES of nuclear masses. We obtained the nuclear masses for $A \geq 1 0 0$ by using the empirical formulas and AME databases. Although the nuclear mass with large error exists, it does not affect the overall description and prediction effect. In addition, in Sec. 3 we use BP neural network to study the OES of nuclear masses. The results show that the BP neural network is useful for described and predicted the nuclear masses.

Using the empirical formula of OES obtained the calculated and predicted values of nuclear masses. The known nuclear mass with mass number $A \ge 1 0 0$ is in good agreement with the experimental value. The RMSD of even- $Z$ nuclei and odd- $Z$ nuclei is 208 keV and 238 keV, and the RMSD of even- $N$ nuclei and odd- $N$ nuclei is 222 keV and 240 keV. At the same time, the research shows that the OES of even- $Z$ nuclei (even- $N$ nuclei) is better than that of odd- $Z$ nuclei (odd- $N$ nuclei), so the RMSD of even- $Z$ nuclei (even- $N$ nuclei) is less than that of odd- $Z$ nuclei (odd- $N$ nuclei). It can be seen from table 1 and table 2 that the predicted value based on AME2012 is consistent with the value in AME2016 database, and the larger the mass number, the smaller the deviation. In addition, it is feasible to describe and predict the OES of nuclear masses based on BP neural network. The calculated value based on BP neural network is in good agreement with the experimental value, the RMSD of even- $Z$ and odd- $Z$ nuclei is 141 keV and 159 keV; the RMSD of even- $N$ and odd- $N$ nuclei is 150 keV and 160 keV. At the same time, the prediction value based on the OES of nuclear masses and AME2012 database is close to the values in the AME2016 database. Because the OES of even- $Z$ nuclei and even- $N$ nuclei is statistically good, so the RMSD of the even- $Z$ nuclei (even- $N$ nuclei) is smaller than the odd- $Z$ nuclei (odd- $N$ nuclei). It is found that the deviation of nuclear mass by BP neural network is 60-80keV less than that by empirical formulas, and the deviation is reduced by 32%. The advantage of BP neural networks method is to reduce the calculation and prediction deviation of nuclear masses, but the disadvantage is that we can not participate in the operation of neural networks.

The result shows that the nuclear mass can be described and predicted by using

the formula of OES. In addition, the nuclear mass calculated and predicted by using BP neural network to study the OES of nuclear masses is also in good agreement with the values in databases. The number of nuclei involved in the description and prediction of nuclear mass is 2, less nuclear involvement makes extrapolation easier. The more accurate the calculated and predicted values of the OES of nuclear masses are, the more accurate the nuclear mass will be.

# References

1. C.F. Von Weizs¨acker, Z. Phys 96, 431 (1935).   
2. P. M¨oller et al., At. Data Nucl. Data Tables 59, 185 (1995).   
3. J. Duflo and A.P. Zuker, Phys. Rev. C 52, R23 (1995).   
4. G.T. Garvey and I. Kelson, Phys. Rev. Lett. 16, 197 (1966).   
5. L. Geng, H. Toki and J. Meng, Prog. Theor. Phys. 113, 785 (2005).   
6. S. Goriely, N. Chamel and J.M. Pearson, Phys. Rev. Lett. 102, 152503 (2009).   
7. P. M¨oller et al., Phys. Rev. Lett. 108, 052501 (2012).   
8. C. Qi, J. Phys. G: Nucl. Par. 42, 045104 (2015).   
9. N. Wang, Z. Liang, M. Liu et al., Phys. Rev. C 82, 044304 (2010).   
10. S. Goriely, F. Tondeur and J.M. Pearson, At. Data Nucl. Data Tables 77, 311 (2001).   
11. M. Bao, Z. He, Y. Lu et al., Phys. Rev. C 88, 064325 (2013).   
12. B. Krusche, Eur. Phys. J. A 26, 7 (2005).   
13. J.M. Pearson, S. Goriely, M. Samyn, Eur. Phys. J. A 15, 13 (2002).   
14. G.J. Fu, H. Jiang, Y.M. Zhao et al., Phys. Rev. C 82, 034304 (2012).   
15. H. Jiang, G.J. Fu, Y.M. Zhao et al., Phys. Rev. C 82, 054317 (2010).   
16. D. Lunney, J.M. Pearson and C. Thibault, Rev. Mod. Phys. 75, 1021 (2003).   
17. B.B. Jiao, Mod. Phys. Lett. A 32, 1850156 (2018).   
18. Z. Wu, S.A. Changizi and C. Qi, Phys. Rev. C 93, 034334 (2016).   
19. G. Audi, A.H. Wapstra and C. Thibault, Nucl. Phys. A 729, 337 (2003).   
20. G. Audi, F.G. Kondev, M. Wang et al., Chin. Phys. C 41, 030001 (2017).   
21. M. Wang, G. Audi, A.H. Wapstra et al., Chin. Phys. C 36, 1603 (2012).   
22. B.B. Jiao, Sci Sin-Phys Mech Astron 48, 052001 (in Chinese) (2018).   
23. J.W. Clark, H. Li, Int. J. Mod. Phys. B 20, 5015 (2006).   
24. N.J. Costiris, E. Mavrommatis, K.A. Gernoth et al., Phys. Rev. C 80, 044332 (2009).   
25. S. Akkoyun, T. Bayram, T. Turker, Radiat. Phys. Chem. 96, 186 (2014).   
26. S. Akkoyun, T. Bayram, Int. J. Mod. Phys. E 23, 1450064 (2014).   
27. S. Gazula, J.W. Clark and H. Bohr, Nucl. Phys. A 540, 1 (1992).   
28. K.A. Gernoth K, J.W. Clark, J.S. Prater et al., Phys. Lett. B 300, 1 (1993).   
29. T. Bayram, S. Akkoyun and S.O. Kara, Ann. Nucl. Energy 63, 172 (2014).   
30. S. Athanassopoulos, E. Mavrommatis, K.A. Gernoth et al., Nucl. Phys. A 743, 222 (2004).   
31. L. Alvarez-Ruso, K.M. Graczyk and E. Saul-Sala, Phys. Rev. C 99, 025204 (2019).   
32. N.J. Costiris, E. Mavrommatis, K.A. Gernoth et al., Phys. Rev. C 80, 044332 (2009).   
33. S. Akkoyun, T. Bayram and T. Turker, Radiat. Phys. Chem. 96, 186 (2014).   
34. R. Utama and J. Piekarewicz, Phys. Rev. C 96, 044308 (2017).   
35. R. Utama and J. Piekarewicz, Phys. Rev. C 97, 014306 (2018).   
36. Z.M. Niu and H.Z. Liang, Physics Letters B 778, 48 (2018).   
37. H.F. Zhang, L.H. Wang, J.P. Yin et al., J. Phys. G: Nucl. Par. 44, 045110 (2017).   
38. J. He, X. Tang, P. Gong et al., Ann. Nucl. Energy 112, 1 (2018).   
39. D. Ma, T. Zhou, J. Chen et al., Nucl. Eng. Des. 320, 400 (2017).   
40. K.X. Peng, J.B. Yang, X.G. Tuo et al., Mod. Phys. Lett. B 30, 87 (2016).