# Successful prediction of total $\alpha$ -induced reaction cross sections at astrophysically relevant sub-Coulomb energies using a novel approach

P. Mohr,1, 2 , ∗ Zs. F¨ul¨op,1 Gy. Gy¨urky,1 G. G. Kiss,1 and T. Sz¨ucs1

1Institute for Nuclear Research (MTA Atomki), H–4001 Debrecen, Hungary

2Diakonie-Klinikum, D–74523 Schw¨abisch Hall, Germany

(Dated: June 9, 2020)

The prediction of stellar (γ,α) reaction rates for heavy nuclei is based on the calculation of $( \alpha , \gamma )$ cross sections at sub-Coulomb energies. These rates are essential for modeling the nucleosynthesis of so-called $p$ -nuclei. The standard calculations in the statistical model show a dramatic sensitivity to the chosen $\alpha$ -nucleus potential. The present study explains the reason for this dramatic sensitivity which results from the tail of the imaginary $\alpha$ -nucleus potential in the underlying optical model calculation of the total reaction cross section. As an alternative to the optical model, a simple barrier transmission model is suggested. It is shown that this simple model in combination with a wellchosen $\alpha$ -nucleus potential is able to predict total $\alpha$ -induced reaction cross sections for a wide range of heavy target nuclei above $A \gtrsim 1 5 0$ with uncertainties below a factor of two. The new predictions from the simple model do not require any adjustment of parameters to experimental reaction cross sections whereas in previous statistical model calculations all predictions remained very uncertain because the parameters of the $\alpha$ -nucleus potential had to be adjusted to experimental data. The new model allows to predict the reaction rate of the astrophysically important $^ { 1 7 6 } \mathrm { W } ( \alpha , \gamma ) ^ { 1 8 0 } \mathrm { O }$ s reaction with reduced uncertainties, leading to a significantly lower reaction rate at low temperatures. The new approach could also be validated for a broad range of target nuclei from $A \approx 6 0$ up to $A \gtrsim 2 0 0$ .

Introduction. The astrophysical $\gamma$ -process is mainly responsible for the nucleosynthesis of so-called $p$ -nuclei; these are a group of heavy neutron-deficient nuclei with very low abundances which are bypassed in the otherwise dominating neutron capture processes [1]. The $\gamma$ -process operates in an explosive astrophysical environment at high temperatures of $2 - 3$ Giga-Kelvin $T _ { 9 } = 2 - 3$ ). Both, supernovae of type II [2–4] and of type Ia [5–7] have been suggested. Up to now, a final conclusion on the astrophysical site(s) of the $\gamma$ -process could not be reached. The combined uncertainties from the stellar models and from the underlying nuclear reaction rates still prevent to reproduce the abundances of all $p$ -nuclei [8, 9].

Nucleosynthesis in the $\gamma$ -process proceeds via a series of photon-induced reactions of (γ,n), ( $\gamma$ ,p), and $( \gamma , \alpha )$ type. In particular, most relevant for the final abundances of the $p$ -nuclei are the branching points between (γ,n) and $( \gamma , \alpha )$ which are typically located several mass units “west” of the valley of stability for heavy $p$ -nuclei and closer to stability for lighter $p$ -nuclei in the $A \approx 1 0 0$ mass region [3, 4, 7–10]. The astrophysical rates of photon-induced reactions are calculated from the inverse capture reactions using detailed balance. It is generally accepted that nucleon capture rates can be predicted with an uncertainty of about a factor of two, whereas $\alpha$ capture rates are more uncertain by at least one order of magnitude (see e.g. the variation of rates in the sensitivity study [4]).

Astrophysically relevant energies, the so-called Gamow window, are of the order of 10 MeV for heavy nuclei and temperatures of $T _ { 9 } \approx 2 - 3$ . At these sub-Coulomb energies the prediction of $\alpha$ -induced reaction cross sections is complicated because the usual statistical model cal-

culations show a wide range of predicted cross sections spanning over at least one order of magnitude. This huge uncertainty results from the choice of the $\alpha$ -nucleus optical model potential (AOMP) in the statistical model (SM). For completeness it has to be mentioned that the SM calculations are based on the total cross section σreac $\sigma _ { \mathrm { r e a c } }$ which is calculated in the optical model (OM) by solving the Schr¨odinger equation with a reasonable complex AOMP. Here $\sigma _ { \mathrm { r e a c } }$ is given by:

$$
\sigma_ {\mathrm {r e a c}} (E) = \sum_ {L} \sigma_ {L} = \frac {\pi \hbar^ {2}}{2 \mu E} \sum_ {L} (2 L + 1) \left[ 1 - \eta_ {L} ^ {2} (E) \right] (1)
$$

with the reduced mass $\mu$ and the (real) reflexion coefficient $\eta _ { L }$ for the $L$ -th partial wave. Note that all $\eta _ { L } = 1$ and thus $\sigma _ { \mathrm { r e a c } } = 0$ in the OM for any purely real AOMP without imaginary part.

The present study is organized as follows. In a first step, the main origin of the huge uncertainties of $( \alpha , \gamma )$ cross sections in the Gamow window is identified for the first time. It will be shown that the imaginary part of the AOMP at large radii (far outside the colliding nuclei) plays an essential role. In a second step, a simple barrier transmission model will be suggested which avoids the complications with the imaginary part of the AOMP. Next, this simple model is combined with a carefully chosen AOMP, and total $\alpha +$ nucleus reaction cross sections are calculated at low energies, thus enabling the prediction of $\alpha$ -induced reaction rates for heavy target nuclei with significantly reduced uncertainties. As a first example, $\alpha$ -induced reactions for $^ \mathrm { 1 9 7 }$ Au were chosen because a recent experiment has provided high-precision data down to energies close to the Gamow window [11]. Then, predictions of $\alpha$ -induced cross sections for several heavy tar-

gets (above $A = 1 5 0$ ) are compared to experimental data from literature. Finally, a new prediction is given for the reaction rate of the $^ { 1 7 6 } \mathrm { W } ( \alpha , \gamma ) ^ { 1 8 0 }$ Os reaction which governs the production of the $p$ -nucleus $1 8 0$ W [4]; no experimental data are available for the unstable target nucleus 176W. The new approach is also valid for target nuclei between $A \approx 6 0$ and $A \gtrsim 2 0 0$ (see Supplement [12]).

The present study uses spherical symmetry. The role of deformation for the tunneling of $\alpha$ particles was mainly investigated in $\alpha$ -decay studies (e.g., [13–15]). Additional information on the relevance of deformation is given in the Supplement [12].

Identification of the source of uncertainties. Much work has been devoted to the determination of global AOMPs at low energies in the recent years. Starting with the pioneering work of Somorjai et al. [16] on the 14 $^ { 4 } \mathrm { S m } ( \alpha , \gamma ) ^ { 1 4 8 }$ Gd reaction, it was noticed that the available AOMPs overestimate the experimental data in particular towards low energies. This holds for the widely used simple AOMP by McFadden and Satchler (MCF) [17] and the early AOMP by Watanabe [18] which was the default choice in previous versions of the widely used SM code TALYS [19]. Nowadays, TALYS offers a broader choice of AOMPs, including the AOMPs by Avrigeanu et al. [20] (present default choice in TALYS) and by Demetriou et al. [21]. Furthermore, we modified TALYS to implement the recent ATOMKI-V1 potential [22]. It was found that the total reaction cross section of $\alpha +$ $\scriptstyle 1 9 7$ Au from the different AOMPs varies by less than a factor of two at higher energies of 25 MeV above the Coulomb barrier; however, around 10 MeV, i.e., in the center of the Gamow window at $T _ { 9 } \approx 2 . 5$ , the predicted cross sections vary dramatically by about four orders of magnitude [23]. Obviously, the reason for the wide range of predictions should be understood.

For explanation, we start with the simple 4-parameter MCF potential which uses a standard Woods-Saxon (WS) parametrization with the real and imaginary depths of $V _ { 0 } = 1 8 5$ MeV, $W _ { 0 } = 2 5$ MeV, radius $R = 1 . 4$ fm $\times A _ { T } ^ { 1 / 3 } = 8 . 1 5$ fm, and diffuseness $a = 0 . 5 2$ fm. Three changes are applied to the MCF potential; these changes show that the tail of the imaginary part of the potential far outside the colliding nuclei has the dominating influence on the calculated low-energy cross sections.

(i) We truncate the imaginary part of the MCF WS potential at $r = 1 2$ fm (with the tiny $W ( r ) \approx 0 . 0 1 5$ MeV or $W ( r ) / W _ { 0 } < 1 0 ^ { - 3 }$ !). This truncation has minor influence at higher energies but reduces $\sigma _ { \mathrm { r e a c } }$ at low energies by one order of magnitude (dotted line in Fig. 1).   
(ii) We change the parameterization of the imaginary part to a squared Woods-Saxon (WS2) and re-adjust the parameters of the WS2 potential such that the imaginary potential is practically identical to the initial MCF WS potential up to about 10 fm, but significantly weaker at larger radii; for the WS $^ 2$ potential we find $W _ { 0 } = 2 5 . 0 7$ MeV, $R _ { 0 } = 1 . 4 9 9$ fm, $a = 0 . 6 2 3$ fm. This results in a

similar energy dependence for $\sigma _ { \mathrm { r e a c } }$ as in the previous case (i), see wide-dotted line in Fig. 1.

(iii) We reduce the real part of the MCF WS potential by a significant factor of two. This reduction increases the effective barrier, and thus $-$ as expected – $\sigma _ { \mathrm { r e a c } }$ is reduced at higher energies (dash-dotted line in Fig. 1). However, around 10 MeV $\sigma _ { \mathrm { r e a c } }$ does not change because $\sigma _ { \mathrm { r e a c } }$ results from the tail of the imaginary potential; i.e., absorption (in the OM calculation) occurs at large radii far outside the colliding nuclei, before the incoming $\alpha$ has tunneled through the barrier. Consequently, the height of the barrier is practically not relevant at the lowest energies in Fig. 1.

The extreme sensitivity to the tail of the imaginary potential at large radii is the simple explanation for the huge range of predictions of low-energy $\sigma _ { \mathrm { r e a c } }$ for $\alpha$ -induced reactions from different AOMPs (shown as gray-shaded area in Fig. 1). It has to be noted that the shape of the imaginary potential is usually fixed by the analysis of elastic scattering at energies around and above the Coulomb barrier. These experiments, however, do not constrain the tail of the imaginary part. For example, at an energy of 25 MeV, the WS and WS2 potentials in cases $( i i )$ and (iii) provide $\sigma _ { \mathrm { r e a c } }$ within 2%, and the deviation in the calculated angular distributions never exceeds 9% in the full angular range. In practice, the tail of the imaginary potential results – more or less by

![](images/8d9ba93cb58a7ced3556a149bc5db10e6d3ee115ed126444c425e29cdbd5611b.jpg)  
FIG. 1. (Color online) Total reaction cross section $\sigma _ { \mathrm { r e a c } }$ for $\alpha + ^ { 1 9 7 }$ Au for different potentials (shown as astrophysical Sfactor), compared to experimental data which are taken from the sum of $( \alpha , \gamma )$ , (α,n), and ( $\alpha$ ,2n) in [11, 24]. (The comparison of calculated total reaction cross sections $\sigma _ { \mathrm { r e a c } }$ to the sum of partial experimental cross sections avoids any complications from other ingredients of the SM calculations like the $\gamma$ -strength function or the level density.) Modifications (i) and $( i i )$ of the imaginary MCF WS potential reduce $\sigma _ { \mathrm { r e a c } }$ at low energies dramatically (dotted red lines); the reduction of the real MCF potential (iii) has minor influence at low energies (dash-dotted red). The TALYS and pBTM calculations are discussed in the text. The shaded area represents the wide range of TALYS predictions.

accident – from the chosen parametrization in the fitting of the elastic angular distribution where the parameters of the imaginary part are mainly sensitive to the nuclear surface region but not to the far exterior.

An alternative approach. From the above discussion it is obvious that any calculation of the total reaction cross section $\sigma _ { \mathrm { r e a c } }$ in the OM at energies far below the Coulomb barrier must have significant uncertainties. Here we present an alternative approach which avoids the uncertainties from the unknown imaginary potential at large radii. A similar approach – extended by coupling to lowlying excited states – is widely used for heavy-ion fusion reactions, and there it was found that WS potentials are inappropriate to describe data far below the Coulomb barrier [25–27].

The suggested model is based on the calculation of transmission through the Coulomb barrier in a purely real nuclear potential; it will be called “pure barrier transmission model” (pBTM) in the following. By definition, this model assumes absorption of an incoming $\alpha$ -particle, as soon as the $\alpha$ has tunneled through the barrier from the exterior to the interior. This assumption is reasonable because the small tunneling probability of the $\alpha$ -particle prevents the $\alpha$ from tunneling back to the exterior; it is much more likely that the formed compound nucleus decays by $\gamma$ -ray or neutron emission. The total cross section in the pBTM is given by

$$
\sigma_ {\mathrm {r e a c}} (E) = \sum_ {L} \sigma_ {L} = \frac {\pi \hbar^ {2}}{2 \mu E} \sum_ {L} (2 L + 1) T _ {L} (E) \quad (2)
$$

with the barrier transmission $T _ { L }$ ; for comparison, see also Eq. (1) for $\sigma _ { \mathrm { r e a c } }$ in the OM.

Technically, the calculations in the pBTM were performed using the code CCFULL [28]. Minor modifications to the code had to be made to use numerical external potentials. For further technical details of the pBTM and the calculations, see also [29] and the Supplement [12].

The real part of the full ATOMKI-V1 potential is energy-independent whereas the imaginary part increases with energy around the barrier. The resulting coupling between the imaginary and real parts is governed by the so-called dispersion relation [30–33]. It is found that the additional consideration of the dispersion relation has only minor influence of less than 30% on the total cross section $\sigma _ { \mathrm { r e a c } }$ for all energies under study because the parameters of the chosen ATOMKI-V1 potential were adjusted to elastic scattering data at energies around the Coulomb barrier. A study of dispersion relations is provided in the Supplement [12].

The results for $^ { 1 9 7 } \mathrm { A u } \ + \ \alpha$ from the simple pBTM are compared to SM calculations using different AOMPs from TALYS in Fig. 1. Obviously, the SM calculations using the MCF and the ATOMKI-V1 potentials overestimate the experimental low-energy cross sections. Lower

cross sections result from the Avrigeanu AOMP [20] and from a Demetriou AOMP [21]; the latter has been scaled by a factor of 1.2 (as suggested in [34]). Interestingly, the simple pBTM model in combination with the real part of the ATOMKI-V1 potential leads to cross sections which are close to the experimental data and also close to the many-parameter potentials by Avrigeanu et al. [20] and Demetriou et al. [21, 34].

Encouraged by this successful application of the pBTM for $^ { \mathrm { 1 9 7 } } \mathrm { A u } + \alpha$ , we have calculated $\sigma _ { \mathrm { r e a c } }$ for a series of $\alpha$ - induced reactions of heavy target nuclei above $A = 1 5 0$ . Fig. 2 shows that the predictions from the pBTM are in excellent agreement with recent experimental data [35– 42]. Typical deviations are less than a factor of two which is marked as grey-shaded uncertainty band in Fig. 2. No parameter adjustment to reaction cross sections is necessary for the present calculations because the real part of the ATOMKI-V1 potential is completely constrained from elastic scattering and an imaginary part is not required in the simple pBTM. Technical details on the calculation of the double-folding potential ATOMKI-V1 and the chosen density distributions are provided in the Supplement [12].

We benchmark the calculations in the simple pBTM with the results from the AOMP by Avrigeanu et al. [20] (shown as dotted lines in Fig. 2). This many-parameter AOMP ( $\gg 1 0$ parameters, see Table II of [20]) has been adjusted to most of the experimental data shown in Fig. 2. Interestingly, a minor enhancement of the imaginary potential was introduced in [20] for $1 5 2 \leq A \leq 1 9 0$ , leading to a significantly increased low-energy S-factor which is not present for 151Eu and 191,193Ir. Contrary to the many-parameter approach of [20], no adjustment of parameters is required in the present pBTM; nevertheless, the deviation from the experimental data is typically less than a factor of two.

Again encouraged by the successful application of the simple pBTM model to $A > 1 5 0$ nuclei, we finally predict the reaction rate of the $^ { 1 7 6 } \mathrm { W } ( \alpha , \gamma ) ^ { 1 8 0 } ( $ Os reaction which is essential for the nucleosynthesis of the $p$ -nucleus $^ { 1 8 0 } \mathrm { W }$ [4]. Because of the highly negative $Q$ -value of the (α,n) channel, the total cross section is approximately identical to the $( \alpha , \gamma )$ cross section in the astrophysically relevant energy range. Thus, the total cross section $\sigma _ { \mathrm { r e a c } }$ from the pBTM can be directly used for the calculation of the reaction rate $N _ { A } \langle \sigma v \rangle$ of the $( \alpha , \gamma )$ reaction. The result from the pBTM is compared to other predictions [43–45] in Fig. 3. The rates from literature cover several orders of magnitude, even exceeding the the range of variations in the sensitivity study [4], whereas the present approach should be valid within a factor of two. For further details, see the Supplement [12].

Summary and conclusions. The present work has identified the reason for the huge variations of $\alpha$ -induced reaction cross sections at low energies in the statistical model which results from the tail of the imaginary part of the

$\alpha$ -nucleus potential. As an alternative to the statistical model, a simple barrier transmission model is suggested where the total reaction cross section is calculated from the transmission through the Coulomb barrier in a real

![](images/95232a27a64222d9eabea202a546bb73be9d0296483ef0ad1a50d10f7d1a9f9b.jpg)  
FIG. 2. (Color online) Total reaction cross section $\sigma _ { \mathrm { r e a c } }$ (given as astrophysical S-factor) for $\alpha$ -induced reactions above $A = 1 5 0$ . The pBTM predicts practically all experimental data [35–42] within a factor of two (grey shaded). The dotted lines show the results from the many-parameter AOMP of [20]. The arrows indicate the ( $\alpha$ ,n) and ( $\alpha$ ,2n) thresholds.

potential. The combination of this simple barrier transmission model with the real part of the ATOMKI-V1 potential leads to predictions of total $\alpha$ -induced cross sections which agree with the experimental data within less than a factor of two for a wide range of heavy target nuclei above $A > 1 5 0$ . Contrary to previous approaches, the present calculations do not require any adjustment of parameters and thus predict low-energy cross sections from a simple, but physically sound model.

The new approach is used to predict the reaction rate of the astrophysically important $^ { 1 7 6 } \mathrm { W } ( \alpha , \gamma ) ^ { 1 8 0 }$ Os reaction which has strong impact on the abundance of the $p$ -nucleus 180W [4]. According to the small deviations from the experimental data for all targets under study, we claim an uncertainty of less than a factor of two for this rate whereas previous predictions of $N _ { A } \langle \sigma v \rangle$ are higher than the present result and vary by orders of magnitude.

The present study focuses on heavy target nuclei with masses above $A > 1 5 0$ where the predictions from different $\alpha$ -nucleus potentials vary over orders of magnitude. For lighter targets, the predictions of $\alpha$ -induced cross sections from different potentials do not vary as dramatic, and it was found that also the simple barrier transmission model reproduces experimental data very well. The recently measured $^ { 1 0 0 } \mathrm { M o } ( \alpha , \mathrm { n } ) ^ { 1 0 3 } \mathrm { R u }$ data were predicted with similar uncertainties as in the $A \gtrsim 1 5 0$ mass range [46], and data for $^ { 6 4 } \mathrm { Z n } + \alpha$ and $^ { 5 8 } \mathrm { N i } + \alpha$ were also reproduced. Further information on the applicability of the barrier transmission model in a wide mass range and for nuclei beyond the valley of stability is provided in the Supplement [12]. In conclusion, the present approach is valid for masses above $A \geq 5 8$ , and thus a reliable prediction of $\alpha$ -induced reaction cross sections comes within reach for the whole nucleosynthesis network of the $\gamma$ - process. Furthermore, the present approach is also able

![](images/2437ba885ff3b7f2126978b666d57ffd851a78eb1c3ca25b3869254ed93f92c1.jpg)  
FIG. 3. (Color online) Reaction rate $N _ { A } \left. \sigma v \right.$ of the $^ { 1 7 6 } \mathrm { W } ( \alpha , \gamma ) ^ { 1 8 0 } \mathrm { O }$ s reaction, normalized to the present calculation in the pBTM. The grey shaded area indicates the uncertainty of a factor of two (see also Fig. 2). Further discussion see text and the Supplement [12].

to provide improved reaction rates for ( $\alpha$ ,n) reactions in the weak $r$ -process [47–50].

The Supplement [12] provides the following additional references: [51–68].

Acknowledgments We thank E. Somorjai, T. Rauscher, and D. Galaviz for countless encouraging discussions on $\alpha$ -induced reaction cross sections over more than two decades. This work was supported by NKFIH (Gr. No. K120666, NN128072) and by the New National Excellence Program of the Ministry for Innovation and Technology (UNKP-19-4-DE-65). G. G. Kiss acknowledges ´ support from the J´anos Bolyai research fellowship of the Hungarian Academy of Sciences.

∗ mohr@atomki.mta.hu   
[1] M. Arnould and S. Goriely, Physics Reports 384, 1 (2003).   
[2] S. E. Woosley and W. M. Howard, Astroph. J. Suppl. 36, 285 (1978).   
[3] T. Rauscher, A. Heger, R. D. Hoffman, and S. E. Woosley, Astrophys. J. 576, 323 (2002).   
[4] T. Rauscher, N. Nishimura, R. Hirschi, G. Cescutti, A. S. J. Murphy, and A. Heger, Mon. Not. R. Astron. Soc. 463, 4153 (2016).   
[5] C. Travaglio, F. K. R¨opke, R. Gallino, and W. Hillebrandt, The Astrophysical Journal 739, 93 (2011).   
[6] C. Travaglio, R. Gallino, T. Rauscher, F. K. R¨opke, and W. Hillebrandt, The Astrophysical Journal 799, 54 (2015).   
[7] N. Nishimura, T. Rauscher, R. Hirschi, A. S. J. Murphy, G. Cescutti, and C. Travaglio, Monthly Notices of the Royal Astronomical Society 474, http://oup.prod.sis.lan/mnras/article-pdf/474/3/3133/22   
[8] T. Rauscher, N. Dauphas, I. Dillmann, C. Fr¨ohlich, Z. F¨ul¨op, and G. Gy¨urky, Reports on Progress in Physics 76, 066201 (2013).   
[9] M. Pignatari, K. G¨obel, R. Reifarth, and C. Travaglio, International Journal of Modern Physics E 25, 1630003 https://doi.org/10.1142/S0218301316300034.   
[10] W. Rapp, J. G¨orres, M. Wiescher, H. Schatz, and F. K¨appeler, The Astrophysical Journal 653, 474 (2006).   
[11] T. Sz¨ucs, P. Mohr, G. Gy¨urky, Z. Hal´asz, R. Husz´ank, G. G. Kiss, T. N. Szegedi, Z. T¨or¨ok, and Z. F¨ul¨op, Phys. Rev. C 100, 065803 (2019).   
[12] See Supplemental Material at [URL will be inserted by publisher] for additional details.   
[13] D. S. Delion, Z. Ren, A. Dumitrescu, and D. Ni, Journal of Physics G: Nuclear and Particle Physics 45, 0   
[14] C. Xu and Z. Ren, Phys. Rev. C 73, 041301 (2006).   
[15] D. S. Delion, A. Sandulescu, and W. Greiner, Phys. Rev. C 69, 044318 (2004).   
[16] E. Somorjai, Z. F¨ul¨op, A. Z. Kiss, C. E. Rolfs, H. P. Trautvetter, U. Greife, M. Junker, S. Goriely, M. Arnould, M. Rayet, T. Rauscher, and H. Oberhummer, Astronomy & Astrophysics 333, 1112 (1998).   
[17] L. McFadden and G. R. Satchler, Nuclear Physics 84, 177 (1966).   
[18] S. Watanabe, Nuclear Physics 8, 484 (1958).

[19] A. J. Koning, S. Hilaire, and S. Goriely, “computer code talys, version 1.9,” (2017).   
[20] V. Avrigeanu, M. Avrigeanu, and C. M˘an˘ailescu, Phys. Rev. C 90, 044612 (2014).   
[21] P. Demetriou, C. Grama, and S. Goriely, Nuclear Physics A 707, 253 (2002).   
[22] P. Mohr, G. Kiss, Z. F¨ul¨op, D. Galaviz, G. Gy¨urky, and E. Somorjai, Atomic Data and Nuclear Data Tables 99, 651 (2013).   
[23] T. Sz¨ucs, P. Mohr, G. Gy¨urky, Z. Hal´asz, R. Husz´ank, G. G. Kiss, T. N. Szegedi, Z. T¨or¨ok, and Z. F¨ul¨op, “Activation measurement of $\alpha$ -induced cross sections for $^ { 1 9 7 } A u$ : analysis in the statistical model and beyond,” (2019), proc. Nuclear Physics in Astrophysics NPA-IX, J. Phys. Conf. Proc., accepted for publication.   
[24] M. S. Basunia, H. A. Shugart, A. R. Smith, and E. B. Norman, Phys. Rev. C 75, 015802 (2007).   
[25] B. B. Back, H. Esbensen, C. L. Jiang, and K. E. Rehm, Rev. Mod. Phys. 86, 317 (2014).   
[26] K. Hagino and N. Takigawa, Progress of Theoretical Physics 128, 1061 (2012), http://oup.prod.sis.lan/ptp/article-pdf/128/6/1061/9681414/128-6-1   
[27] A. B. Balantekin and N. Takigawa, Rev. Mod. Phys. 70, 77 (1998).   
[28] K. Hagino, N. Rowley, and A. Kruppa, Computer Physics Communications 123, 143 (1999).   
[29] P. Mohr, International Journal of Modern Physics E 28, 1950029 (20   
[30] M. A. Nagarajan, C. C. Mahaux, and G. R. Satchler, Phys. Rev. Lett. 54, 1136 (1985).   
[31] M. A. Nagarajan and G. R. Satchler, Physics Letters B 173, 29 (1986).   
[32] C. Mahaux, H. Ngˆo, and G. R. Satchler, Nuclear Physics A 449, 354 (1986).   
[33] C. Mahaux, H. Ngˆo, and G. R. Satchler, Nuclear Physics A 456, 134 (1986).   
[34] P. Scholz, F. Heim, J. Mayer, C. M¨unker, 33 (2017),L. Netterdon, F. Wombacher, and A. Zilges, 2024/stx3033.pdf.Physics Letters B 761, 247 (2016).   
[35] G. Gy¨urky, Z. Elekes, J. Farkas, Z. F¨ul¨op, Z. Hal´asz, G. G. Kiss, E. Somorjai, T. Sz¨ucs, R. T. G¨uray, N. Ozkan, C. Yal¸cın, and T. Rauscher, ¨ Journal of Physics G: Nuclear and Particle Physics 37, 115201 (2010   
6),[36] J. Glorius, K. Sonnabend, J. G¨orres, D. Robertson, M. Kn¨orzer, A. Kontos, T. Rauscher, R. Reifarth, A. Sauerwein, E. Stech, W. Tan, T. Thomas, and M. Wiescher, Phys. Rev. C 89, 065808 (2014).   
[37] G. Kiss, T. Sz¨ucs, T. Rauscher, Z. T¨or¨ok, Z. F¨ul¨op, G. Gy¨urky, Z. Hal´asz, and E. Somorjai, Physics Letters B 735, 40 (2014).   
[38] G. G. Kiss, T. Sz¨ucs, T. Rauscher, Z. T¨or¨ok, L. Csedreki, Z. F¨ul¨op, G. Gy¨urky, and Z. Hal´asz, Journal of Physics G: Nuclear and Particle Physics 42, 055103 (2015   
[39] G. Kiss, T. Rauscher, T. Sz¨ucs, Z. Kert´esz, Z. F¨ul¨op, 001 (2018).G. Gy¨urky, C. Fr¨ohlich, J. Farkas, Z. Elekes, and E. Somorjai, Physics Letters B 695, 419 (2011).   
[40] L. Netterdon, P. Demetriou, J. Endres, U. Giesen, G. Kiss, A. Sauerwein, T. Sz¨ucs, K. Zell, and A. Zilges, Nuclear Physics A 916, 149 (2013).   
[41] P. Scholz, A. Endres, A. Hennig, L. Netterdon, H. W. Becker, J. Endres, J. Mayer, U. Giesen, D. Rogalla, F. Schl¨uter, S. G. Pickstone, K. O. Zell, and A. Zilges, Phys. Rev. C 90, 065807 (2014).   
[42] T. Sz¨ucs, G. Kiss, G. Gy¨urky, Z. Hal´asz, Z. F¨ul¨op, and T. Rauscher, Physics Letters B 776, 396 (2018).

[43] R. H. Cyburt, A. M. Amthor, R. Ferguson, Z. Meisel, K. Smith, S. Warren, A. Heger, R. D. Hoffman, T. Rauscher, A. Sakharuk, H. Schatz, F. K. Thielemann, and M. Wiescher, The Astrophysical Journal Supplement Series 189, 240 (2010).   
[44] T. Rauscher and F.-K. Thielemann, Atomic Data and Nuclear Data Tables 75, 1 (2000).   
[45] A. L. Sallaska, C. Iliadis, A. E. Champange, S. Goriely, S. Starrfield, and F. X. Timmes, The Astrophysical Journal Supplement Series 207, 18 (2   
[46] T. N. Szegedi, G. G. Kiss, G. Gy¨urky, and P. Mohr, “Activation cross section measurement of the $^ { 1 0 0 } M o ( \alpha , \mathrm { n } ) ^ { 1 0 3 } R u$ reaction for optical potential studies,” (2019), proc. Nuclear Physics in Astrophysics NPA-IX, J. Phys. Conf. Proc., accepted for publication.   
[47] J. Pereira and F. Montes, Phys. Rev. C 93, 034611 (2016).   
[48] P. Mohr, Phys. Rev. C 94, 035801 (2016).   
[49] J. Bliss, A. Arcones, F. Montes, and J. Pereira, Journal of Physics G: Nuclear and Particle Physics 44, 0   
[50] J. Bliss, A. Arcones, F. Montes, and J. Pereira, Phys. Rev. C 101, 055807 (2020).   
[51] H. D. Vries, C. D. Jager, and C. D. Vries, Atomic Data and Nuclear Data Tables 36, 495 (1987).   
[52] H. Feshbach, Ann. Phys. (N.Y.) 5, 357 (1958).   
[53] H. Abele and G. Staudt, Phys. Rev. C 47, 742 (1993).   
[54] P. R. S. Gomes, J. Lubian, I. Padron, and R. M. Anjos, Phys. Rev. C 71, 017601 (2005).   
[55] S. J. Quinn, A. Spyrou, E. Bravo, T. Rauscher, A. Si-

mon, A. Battaglia, M. Bowers, B. Bucher, C. Casarella, M. Couder, P. A. DeYoung, A. C. Dombos, J. G¨orres, A. Kontos, Q. Li, A. Long, M. Moran, N. Paul, J. Pereira, D. Robertson, K. Smith, M. K. Smith, E. Stech, R. Talwar, W. P. Tan, and M. Wiescher, Phys. Rev. C 89, 054611 (2014).   
[56] F. K. McGowan, P. H. Stelson, and W. G. Smith, Phys. Rev. 133, B907 (1964).   
[57] A. Vlieks, J. Morgan, and S. Blatt, ). Nuclear Physics A 224, 492 (1974).   
[58] J. B. Cumming, Phys. Rev. 114, 1600 (1959).   
[59] P. H. Stelson and F. K. McGowan, Phys. Rev. 133, B911 (1964).   
[60] P. Mohr, The European Physical Journal A 51, 56 (2015).   
[61] G. Gy¨urky, P. Mohr, Z. F¨ul¨op, Z. Hal´asz, G. G. Kiss, T. Sz¨ucs, and E. Somorjai, Phys. Rev. C 86, 041601 (2012).   
[62] A. Ornelas, P. Mohr, G. Gy¨urky, Z. Elekes, Z. F¨ul¨op, Z. Hal´asz, G. G. Kiss, E. Somorjai, T. Sz¨ucs, M. P. 003 (2017).Tak´acs, D. Galaviz, R. T. G¨uray, Z. Korkulu, N. Ozkan, ¨ and C. Yal¸cın, Phys. Rev. C 94, 055807 (2016).   
[63] P. Mohr, G. Gy¨urky, and Z. F¨ul¨op, Phys. Rev. C 95, 015807 (2017).   
[64] L. Trache, EPJ Web Conf. 227, 01016 (2020).   
[65] A. R. Barnett and J. S. Lilley, Phys. Rev. C 9, 2010 (1974).   
[66] J. Pereira, private communication (2019).   
[67] M. Avila, private communication (2019).   
[68] T. Rauscher, Phys. Rev. C 81, 045807 (2010).