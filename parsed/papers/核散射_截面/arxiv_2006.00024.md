# Isotopically resolved neutron total cross sections at intermediate energies

C. D. Pruitt,1, ∗ R. J. Charity,1 L. G. Sobotka, $1 , 2$ J. M. Elson,1 D. E. M. Hoff,1, † K. W. Brown, $^ { 1 , 3 }$ M.C. Atkinson,2, ‡ W.H. Dickhoff,2 H. Y. Lee,4 M. Devlin,4 N. Fotiades,4 and S. Mosby4

$\mathit { 1 }$ Department of Chemistry, Washington University, St. Louis, MO 63130   
2Department of Physics, Washington University, St. Louis, MO 63130   
$_ { 3 }$ National Superconducting Cyclotron Laboratory, Departments of Physics and Astronomy, Michigan State University, East Lansing, MI 48824, USA   
4Los Alamos National Laboratory, Los Alamos, NM 87545, USA

The neutron total cross sections $\sigma _ { t o t }$ of $^ \mathrm { 1 6 , 1 8 }$ O, $^ \mathrm { 5 8 , 6 4 }$ Ni, $^ \mathrm { 1 0 3 }$ Rh, and $^ { 1 1 2 , 1 2 4 }$ Sn have been measured at the Los Alamos Neutron Science Center (LANSCE) from low to intermediate energies ( $3 \ \leq$ $E _ { l a b } \leq 4 5 0$ MeV) by leveraging waveform-digitizer technology. The $\sigma _ { t o t }$ relative differences between isotopes are presented, revealing additional information about the isovector components needed for an accurate optical-model (OM) description away from stability. Digitizer-enabled $\sigma _ { t o t }$ -measurement techniques are discussed and a series of uncertainty-quantified dispersive optical model (DOM) analyses using these new data is presented, validating the use of the DOM for modeling light systems ${ \big ( } ^ { 1 6 , 1 8 } \mathrm { O } { \big ) }$ and systems with open neutron shells ( $^ { \mathrm { 5 8 , 6 4 } } \mathrm { N i }$ and $^ { 1 1 2 , 1 2 4 } \mathrm { S n }$ ). The valence-nucleon spectroscopic factors extracted for each isotope reaffirm the usefulness of high-energy proton reaction cross sections for characterizing depletion from the mean-field expectation.

# INTRODUCTION

Neutron scattering is a direct, Coulomb-insensitive tool for probing the nuclear environment. The simplest neutron-nucleus interaction quantity is the neutron total cross section, $\sigma _ { t o t }$ , which provides information about nuclear size and the ratio of elastic-to-inelastic components of nucleon scattering. Additionally, $\sigma _ { t o t }$ data are thought to be tightly correlated with a variety of structural nuclear properties of great interest including the neutron skin of neutron-rich nuclei [1] and thus the density dependence of the symmetry energy $L$ , an essential equation-of-state input for neutron-star structure calculations [2–4].

In the crude “strongly-absorbing-sphere” (SAS) approximation, where a target nucleus absorbs incident neutrons passing within a nuclear radius, $\sigma _ { t o t }$ depends solely on the target nucleus size and the energy of the incident neutron:

$$
\sigma_ {t o t} (E) = 2 \pi (R + \lambda) ^ {2}, \tag {1}
$$

where $R = r _ { 0 } A ^ { \frac { 1 } { 3 } }$ and $\lambda$ is the reduced wavelength of the incident neutron with energy $E$ in the center of mass [5, 6]. While on average, experimental $\sigma _ { t o t }$ data comport with this na¨ıve model, the most prominent feature of experimental $\sigma _ { t o t }$ data is the oscillatory behavior centered about the average of Eq. (1), visible in Fig. 1. Peterson [7] interpreted these oscillations as the result of a phase shift between neutron partial waves passing around the nucleus (thus undergoing no phase shift) and

![](images/714765bb83df978712927ed5db6c20a461aacbc493fa83ed321294c2bccb048a.jpg)  
FIG. 1: Experimental $\sigma _ { t o t }$ data are shown from 2-500 MeV for nuclides from A=12 to A=208 [8–12]. Predictions for $\sigma _ { t o t }$ given by the “strongly absorbing sphere” (SAS) model [Eq. (1)], are shown as thin dashed lines for each nucleus. Regular oscillations about the SAS model are visible as is the trend for the oscillation maxima and minima to shift to higher energies as $A$ is increased.

waves passing through the nuclear potential, where they are refracted and exhibit a retardation of phase (an illustration is available in [6]). This explanation was termed the “nuclear Ramsauer effect” by Carpenter and Wilson [13] based on the analogous effect seen in electron scattering on noble gases.

Following Angeli and Csikai [14], this explanation can be incorporated by imbuing the strongly-absorbingsphere relations with a sinusoidal term:

$$
\sigma_ {t o t} = 2 \pi (R + \lambda) ^ {2} (1 - \rho \cos (\delta)) \tag {2}
$$

where $\rho = e ^ { - \operatorname { I m } ( \Delta ) }$ and $\delta = \operatorname { R e } ( \Delta )$ , $\Delta$ being the phase difference between a partial wave traveling around and traveling through the nucleus. The large amplitude of the oscillations suggests that elastic scattering accounts

for a significant fraction of the total cross section, in turn implying a larger mean free path for neutrons through the nucleus than might otherwise be expected in the absence of Pauli blocking [15, 16]. If we approximate the nucleus with a real spherical potential of radius $R$ and depth $U$ , the total phase shift $\delta$ is:

$$
\delta = \frac {\bar {C} \left(\left[ \frac {E + U}{E} \right] ^ {\frac {1}{2}} - 1\right)}{\lambda} \tag {3}
$$

where ${ \overline { { C } } } = { \scriptstyle { \frac { 4 } { 3 } } } R$ is the average chord length through the sphere [14]. Rearranging Eq. (3) in terms of $A$ and $E$ and discarding leading constants yields:

$$
\delta \propto A ^ {\frac {1}{3}} \times \left(\sqrt {E + U} - \sqrt {E}\right) \tag {4}
$$

This form reveals an important relation: as $A$ is increased, to maintain constant phase $\delta$ , $E$ must also increase [6, 7]. This is contrary to a typical resonance condition where an integer number of wavelengths are fit inside a potential; in that case, to maintain constant phase as $A$ is increased, $E$ must be decreased. Thus these $\sigma _ { t o t }$ oscillations have been referred to as “anti-resonances” or “echoes” [6, 17]. Other authors [18] have exposed weaknesses in Angeli and Csikai’s interpretation of Eq. (2) and have provided a more general semi-empirical equation for $\sigma _ { t o t }$ . However, Eq. (2) is a valuable starting point for connecting $\sigma _ { t o t }$ with the depth and shape of the nuclear potential as experienced by neutrons.

By including additional surface, spin-orbit, and other terms, OMs have been used to successfully reproduce the general features of all manner of single-nucleon scattering data across the chart of nuclides up to several hundred MeV [19–21]. However, despite the excellent agreement with experiment, OMs involve the interaction of many partial waves with many sometimes-opaque terms in the potential, complicating intuitive understanding of the underlying physics at play. In particular, the isovector components of optical potentials are quite difficult to constrain as they depend on both proton and neutron scattering data, one or both of which are often unavailable. For example, when Dietrich et al. conducted an analysis of neutron total cross section differences between W isotopes, including standard isovector terms in their optical potential worsened the reproduction of experimental relative differences, an illustration of how poorly these isovector components are known [22].

With these considerations in mind, our present goal is twofold: first, to provide new isotopically resolved $\sigma _ { t o t }$ data useful for identifying the dependence of optical potential terms on nuclear asymmetry; and second, conduct a DOM analysis of these new $\sigma _ { t o t }$ data along with a large corpus of scattering and bound-state data to extract veiled structural quantities (e.g. neutron skin thicknesses and spectroscopic factors, or SFs) for several cornerstone, closed-proton-shell nuclei. Key findings of this DOM analysis are presented in the companion Letter [23].

# EXPERIMENTAL CONSIDERATIONS

By scattering secondary radioactive beams off of hydrogen targets in inverse kinematics, proton-scattering experiments are possible even on highly unstable nuclides. Because neutrons themselves must be generated as a secondary radioactive beam, neutron-scattering experiments are restricted to normal kinematics and $\sigma _ { t o t }$ measurements are possible only for relatively stable nuclides that can be formed into a target. At present, $\sigma _ { t o t }$ measurements above the resonance region on nuclides with short half-lives (shorter than the timescale of days) are technically infeasible for this reason, though a handful have been carried out on samples with half-lives in the tens to thousands of years [10, 24, 25].

Traditionally, $\sigma _ { t o t }$ measurements have relied on analogelectronics techniques for recording events, techniques that suffer from a large per-event deadtime of up to several µs. For a typical analog intermediate-energy $\sigma _ { t o t }$ measurement with dozens or hundreds of energy bins, achieving statistical uncertainty at the level of 1% requires a thick sample to attenuate a sizable fraction of the incident neutron flux. If cross sections are in the 1-10 barn range, this means sample masses of tens of grams [8, 12]. Producing an isotopically enriched sample of this size is often prohibitively expensive. As a result, there is a dearth of $\sigma _ { t o t }$ data on isotopically resolved targets from 1-300 MeV, even for closed-shell isotopes of special importance like $^ { 3 , 4 }$ He, $^ { 1 8 }$ O, $^ { 6 4 }$ Ni, $^ \mathrm { 1 1 2 , 1 2 4 }$ Sn, and 204,206Pb (see Fig. 1.3 in [26]).

Recent developments in waveform digitizer technology have made it possible to reduce the per-event deadtime by an order of magnitude or more, enabling a corresponding reduction in the necessary sample size. In 2008, we embarked on a campaign of $\sigma _ { t o t }$ measurements on isotopically enriched samples using these new technical capabilities, starting with $^ { 4 0 , 4 8 }$ Ca from $1 5 \leq E _ { l a b } \leq 3 0 0$ MeV [27]. The data from that measurement were incorporated into several DOM analyses [28–30] that yielded proton and neutron SFs, charge radii, and initial estimates of the neutron skins [1] for these nuclei. Here we significantly expand on that effort by providing $\sigma _ { t o t }$ results for the important closed-shell nuclides 16,18O, $^ \mathrm { 5 8 , 6 4 }$ Ni, and 112,124Sn. We also present a measurement on a very thin sample of the naturally monoisotopic $^ \mathrm { 1 0 3 }$ Rh to demonstrate that $\sigma _ { t o t }$ experiments over a broad energy range using only a few grams of material are feasible.

# EXPERIMENTAL DETAILS

All $\sigma _ { t o t }$ measurements were carried out at the 15R beamline at the Weapons Neutron Research (WNR) facility of the Los Alamos Neutron Science Center (LANSCE) during the 2016 and 2017 run cycles. Our experiment was modeled on previous $\sigma _ { t o t }$ measurements at WNR [8, 12, 27]. At WNR, broad-spectrum neutrons up to

≈700 MeV are generated by impinging proton pulses onto a water-cooled, 7.5 cm-long tungsten target (Fig. 2). Before the beam enters the experimental area, a permanent magnet deflects all charged particles generated by the proton pulses, allowing only neutrons and $\gamma$ rays to reach the experimental area. At the entrance to the experimental area, the beam was collimated to 0.200 inches using steel donuts with a total thickness of 24 inches. In addition, the $\gamma$ -ray content of the beam was suppressed using a plug of Hevimet (90% W, 6% Ni, 4% Cu by weight) at the upstream entrance of the collimation stack. After collimation, the beam passed successively through a flux monitor, the sample of interest, a veto detector, and finally the time-of-flight (TOF) detector approximately 25 meters from the neutron source. All detectors consisted of BC-400 fast scintillating plastic mated with photomultiplier tubes (PMTs) and encased in either a plastic or an aluminum housing. The flux monitor and veto detector each had scintillator thicknesses of 0.25 inch and the TOF detector had a scintillator thickness of 1 inch. Signals from all detectors and the target changer were relayed to a 500-MHz CAEN DT-5730 waveform digitizer running custom software. To improve time resolution, the TOF detector used two PMTs (one left, one right) mated to the same plastic scintillator and the PMTs’ signals were summed before digitization.

The particular neutron beam structure at WNR dictates the energy range achievable for $\sigma _ { t o t }$ measurements (Fig. 3). Proton pulse trains, called “macropulses”, are delivered to the tungsten target at 120 Hz. Each macropulse consists of ≈350 individual proton pulses, called “micropulses”, spaced 1.8 µs apart. Each micropulse consists of a single proton packet that generates $\gamma$ rays and neutrons within a tight temporal-spatial range. As neutrons from this micropulse travel along the beam path, high-energy neutrons separate in time from lower-energy neutrons so that neutron energy can be determined by standard TOF techniques (see [31] for details). Because the $\gamma$ rays and high-energy neutrons from later micropulses can overtake slower neutrons from an earlier micropulse, the distance of the TOF detector from the neutron source determines both the minimum neutron energy that can be unambiguously resolved and the maximum instantaneous neutron flux, critical to correcting for per-event deadtime.

A programmable sample changer with six positions was used to cycle each sample into the beam at a regular interval of 150 seconds per sample. Once per macropulse, an analog signal from the sample changer was recorded to indicate its current position. The flux monitor was used to correct for variations in beam flux between macropulses. The veto detector suppressed events from charged-particle production in the samples and in air along the flight path.

Custom digitizer software was used to run the digitizer in two complementary modes, referred to as “DPP mode” and “waveform mode”. In DPP mode, triggers were ini-

![](images/4ca914ef29314e517515626621d656f765c2832b8a4f0976cb0895286466afd4.jpg)  
FIG. 2: Experimental configuration at WNR facility. Samples are cycled into and out of the beam using a linear actuator with a period of 150 seconds. Times-of-flight (TOFs) are determined by the TOF detector and used to calculate neutron energies.

tiated by the digitizer’s onboard peak-sensing firmware. For each trigger, several quantities were recorded: the trigger timestamp, two charge integrals over the detected peak with different integration ranges (32 ns for the short integral, 100 ns for the long integral), and a 96-ns portion of the raw digitized waveform, referred to as a “wavelet”. DPP mode was used for the vast majority of the experiment and accounts for ≈99% of the total data volume. In waveform mode, the digitizer performs no peaksensing and was externally triggered. Upon triggering, the trigger timestamp and a very long wavelet (60 µs) were recorded. While waveform mode data accounts for only ≈1% of the total data, the instantaneous data rate is much higher than in DPP mode because hundreds of µs of consecutive waveform samples are stored. Roughly once every three seconds, the digitizer was switched to

![](images/ef6180c3097c0e0ab768b3cc1e14d9ea0a5313280f2c675f70bb8d3261c0d1f3.jpg)  
FIG. 3: Neutron-beam structure at WNR facility. “Macropulses” of protons (d) are delivered to WNR’s tungsten Target 4, where they generate neutrons by spallation. Each macropulse consists of ≈350 proton “micropulses” (c). Neutrons from each micropulse (b) disperse in time as they travel along the flight path so that $\gamma$ rays and high-energy neutrons catch up to low-energy ones from the previous pulse (a).

waveform mode for one macropulse, then switched back to DPP mode as quickly as possible (10-40 ms, depending on run configuration).

Except for the O and Rh samples, all samples were prepared as right cylinders 8.25 mm in diameter and ranging from 10-27 mm in length (see Table I for sample characteristics). For each element studied, a natural-abundance sample was also prepared as were two natural C samples and a natural Pb sample, useful for benchmarking against literature data. The samples were inserted into styrofoam sleeves and seated in the cradles of the sample changer. This design minimizes the amount of non-target mass proximate to the neutron beam path. Our samples were generally much smaller than those used in previous measurements; for example, the Ni and Sn samples used in [8, 12] had areal densities of 1.515 and 0.5475 mol/cm2, respectively, 12.7 and 6.5 times larger than for our Ni and Sn samples.

The O isotopes were prepared as water samples to increase the areal density of atoms and for ease of handling. Each water sample was contained by a cylindrical brass vessel with thin brass endcaps (0.002 inches), and an empty brass vessel served as the blank. 16,18O cross sections were calculated by subtracting the well-known H cross section from the raw H2O results. We used H $\sigma _ { t o t }$ data sets from Clement et al. [32] and Abfalterer et al. [12], which together cover the range $0 . 5 \leq E _ { n } \leq 5 0 0$ MeV and are in excellent agreement where their energy ranges overlap. In light of the additional uncertainty inherent to this subtractive $\sigma _ { t o t }$ determination, we prepared a deuterated water sample, from which the literature $\sigma _ { t o t }$ for D $^ 2$ could be subtracted, to serve as an additional cross-check. Due to the poor machining properties of Rh, the $^ \mathrm { 1 0 3 }$ Rh sample was prepared by purchasing and

TABLE I: Physical characteristics of samples used for neutron $\sigma _ { t o t }$ measurements. The relevant “sample thickness” for cross section calculations is the areal density of nuclei $\rho _ { A }$ , equal to the volumetric number density times the length of the sample. For liquid samples $\mathrm { H _ { 2 } ^ { n a t } }$ O, D $_ { \mathrm { ~ 2 ~ } } ^ { \mathrm { n a t } }$ O, and $\mathrm { H _ { 2 } ^ { 1 8 } O }$ , the length and diameter given are for the interior of the vessels used to hold the samples and the masses listed are calculated based on literature values for the density of each sample at 25 C. Isotopic natural abundances (NA) and the abundances in our enriched samples (SA) are provided for reference.

<table><tr><td>Isotope</td><td>Length (mm)</td><td>Diam. (mm)</td><td>Mass (g)</td><td>ρA (mol/cm2)</td><td>NA (%)</td><td>SA (%)</td></tr><tr><td>natC</td><td>13.66(2)</td><td>8.260(5)</td><td>1.2363</td><td>0.1921(1)</td><td>-</td><td>-</td></tr><tr><td>natC</td><td>27.29(2)</td><td>8.260(5)</td><td>2.4680</td><td>0.3835(2)</td><td>-</td><td>-</td></tr><tr><td>H2O</td><td>20.00(1)</td><td>8.92(1)</td><td>1.2461</td><td>0.1107(3)</td><td>-</td><td>-</td></tr><tr><td>D2O</td><td>20.00(1)</td><td>8.92(1)</td><td>1.3852</td><td>0.1107(3)</td><td>0.02</td><td>99.9</td></tr><tr><td>H218O</td><td>20.00(1)</td><td>8.92(1)</td><td>1.3844</td><td>0.1107(3)</td><td>0.20</td><td>99.9</td></tr><tr><td>58Ni</td><td>7.97(3)</td><td>8.18(2)</td><td>3.6438</td><td>0.1197(3)</td><td>68.1</td><td>99.6</td></tr><tr><td>natNi</td><td>8.00(3)</td><td>8.20(2)</td><td>3.6898</td><td>0.1192(3)</td><td>-</td><td>-</td></tr><tr><td>64Ni</td><td>7.96(2)</td><td>8.20(4)</td><td>3.9942</td><td>0.1192(6)</td><td>0.93</td><td>92.2</td></tr><tr><td>103Rh</td><td>2.03(1)</td><td>10.20(2)</td><td>2.8359</td><td>0.02426(4)</td><td>100</td><td>99.9</td></tr><tr><td>112Sn</td><td>13.65(3)</td><td>8.245(5)</td><td>4.9720</td><td>0.08332(5)</td><td>0.97</td><td>99.9</td></tr><tr><td>natSn</td><td>13.68(3)</td><td>8.245(5)</td><td>5.3263</td><td>0.08414(5)</td><td>-</td><td>-</td></tr><tr><td>124Sn</td><td>13.73(3)</td><td>8.245(5)</td><td>5.5492</td><td>0.08399(5)</td><td>5.79</td><td>99.9</td></tr><tr><td>natPb</td><td>10.07(2)</td><td>8.27(1)</td><td>6.130</td><td>0.05508(6)</td><td>-</td><td>-</td></tr></table>

stacking a series of thin discs rather than by manufacturing a fused cylinder. These discs were held in place by a cylindrical plastic case with open ends.

# EXPERIMENTAL ANALYSIS

The quantity of interest, $\sigma _ { t o t }$ , is related to the flux loss through a sample by:

$$
I _ {t} = I _ {0} e ^ {- \ell \rho_ {A} \sigma_ {t o t}} \tag {5}
$$

or, equivalently,

$$
\sigma_ {t o t} = - \frac {1}{\ell \rho_ {A}} \ln \left(\frac {I _ {t}}{I _ {0}}\right) \tag {6}
$$

where $I _ { 0 }$ is the neutron flux entering the sample, $I _ { t }$ is the neutron flux transmitted through the sample without interaction, $\rho _ { A }$ is the number density of nuclei in the sample, and $\ell$ is the sample length. For thin or lowdensity samples, flux attenuation through the sample will be small (e.g., 13% for our Ni samples at 100 MeV) and a large number of counts will be required to determine the cross section to high precision.

Two post-processing steps were used to improve TOFdetector timing resolution (see Fig. 4). First, the waveform for each TOF-detector event was passed through a software constant-fraction discriminator (CFD) logic,

![](images/6daa5780e26f02e647f32dc4422248b8051e4ae758bc2f9f51ab482314eae112.jpg)  
FIG. 4: The effects of timing corrections on the $\gamma$ -ray peak of a typical run are shown. The uncorrected spectrum is shown in black, the spectrum after correction with our software CFD is shown in blue, and the spectrum after correction with both our software CFD and $\gamma$ -averaging is shown in magenta. For this run, the final $\gamma$ -ray peak FWHM after both corrections is 0.866 ns, comparable to the precision we achieved in our Ca study [27], which also employed $\gamma \cdot$ -averaging.

improving precision by a factor of two. Second, a $\gamma$ - ray-averaging procedure (cf. [27]) was used to improve the precision of each micropulse start time. The final corrected TOF resolution (taken as the FWHM of the $\gamma$ -ray peak in the TOF spectra) ranged from 0.60-0.90 ns over the series of $\sigma _ { t o t }$ measurements. This is comparable to the resolution from our digitizer-mediated $\sigma _ { t o t }$ measurement on Ca isotopes in 2008 [27]. For context, for a 100-MeV neutron and a TOF detector distance of 25 meters, a TOF uncertainty of 0.80 ns translates to an energy resolution of ≈900 keV. For neutrons below ≈20 MeV, the TOF time resolution worsens because the traversal time through the 1-inch thickness of the TOF detector becomes non-negligible. However, because the TOF of these neutrons is already very long (several hundred ns or longer) the relative energy resolution ( $\frac { \Delta E } { E }$ ) is superior at low energies. As an example from one of our runs, a 5 MeV neutron with a 0.82 ns detector-traversal time and an inherent TOF resolution of 0.80 ns has an energy uncertainty of 13 keV. These energy uncertainties have been propagated through subsequent analysis into our $\sigma _ { t o t }$ results below.

Calculating the neutron energy requires knowledge of the flight-path distance to high precision. We determined this distance by calculating putative $\sigma _ { t o t }$ data for natC from 3-15 MeV from our measurement and comparing the resonance peaks in this region with high-precision literature data sets. From this study, the mean TOF distance was determined as $2 7 0 9 \pm 1$ cm for the Ni and Rh run configuration and $2 5 5 4 \pm 1$ cm for the Sn and O run configuration.

Before cross sections could be tabulated, the per-event deadtime had to be modeled and corrected for. Because events are not processed instantaneously, there is a brief

period after each trigger during which the digitizer is busy processing that trigger. Any newly arriving events in this period will be ignored, privileging events arriving earlier and thus distorting TOF spectra and resulting cross sections. This busy period is referred to as the “analytic” or “per-event” deadtime and can be corrected for according to standard techniques [31]. An additional complication is the possibility of flux variation between micropulses. If there is no variation, the fraction of time that the digitizer is dead for a given time bin $i$ can be calculated [31]:

$$
F _ {i} = \sum_ {j = 0} ^ {N - 1} R _ {(i - j) \bmod N} \times P _ {j} \tag {7}
$$

where $N$ is the number of time bins in the micropulse, $R _ { x }$ is the rate of detected events per micropulse in bin $x$ , and $P _ { j }$ is the probability that the digitizer is still busy from a trigger $j$ bins ago. If the variation in beam flux is significant, a more advanced formula can be used; however, an examination of our flux-per-micropulse data showed very little flux variance across macropulses, except during the first 10% of the micropulses within each macropulse. In the final analysis we discarded these first 10% and used the simpler Eq. (7) to calculate the dead time fraction.

To model the experimentally observed probabilitydead, $P _ { j }$ , we fitted a logistic function to the observed spectrum for time differences between consecutive events (Fig. 5). For a given bin $_ i$ , the fraction of time that the digitizer is dead, $F _ { i }$ , is a discrete convolution of the measured TOF spectrum with $P _ { j }$ . Note that except for the first and last micropulses in a macropulse, all micropulses are consecutive, so deadtime effects can “wrap around” from the end of one micropulse to the next. For these wrap-around contributions (that is, $j > i$ ), the (mod $N$ ) term ensures that the bin referred to by $i - j$ is nonnegative.

Because trigger processing is done in firmware onboard the digitizer, the per-event deadtimes affecting our measurement were reduced to between 150-230 ns. After we calculated the average probability-dead for each time bin, the total number of events detected in that bin, $N _ { d } [ i ]$ , could be corrected to recover the true number of events that would have been detected in the absence of a perevent deadtime:

$$
N _ {t} [ i ] = - \ln \left[ 1 - \frac {\frac {N _ {d} [ i ]}{M}}{\left(1 - F _ {i}\right)} \right] \times M \tag {8}
$$

where $M$ is the total number of micropulse periods. At large TOFs (low energies) the correction is as low as a few percent, but at small TOFs (high energies), the digitizer is often still dead from the $\gamma$ -ray flash and highenergy neutrons. In this regime the correction can be quite large (≈20% for our Ni/Rh runs, and ≈40% for our Sn/O runs). Still, the corrections needed for our measurement are far smaller than the typical analytic

![](images/5863e6e7576ecda21346e4384671239eafc5e213c5841383a208e0d7b98bad4f.jpg)  
FIG. 5: The time difference between adjacent TOF-detector events for a single run is plotted (black histogram). Below a certain minimum time difference (the “deadtime”), no events are recorded. A logistic fit (red line) models the detector’s deadtime response and is used to generate a deadtime correction. The underlying linearly decreasing count rate (gray dashed line) is incorporated into the logistic model. From the fit, a mean deadtime of 228.1 ns was extracted for the Sn and O run configurations (a similar procedure was used to recover a deadtime of 159.7 ns for the Ni and Rh run configurations).

deadtime corrections required with the deadtime mitigation scheme of previous analog measurements [8, 12].

In addition to analytic deadtime, there is an additional deadtime effect associated with digitizer readout to the data acquisition computer (DAQ). During data collection, each pair of digitizer channels shares a common buffer for storing events. After several seconds of acquisition, the digitizer begins readout at which time the acquisition is paused and buffer contents are read out to the DAQ. However, because each buffer is independently read out to the DAQ, it is possible that buffers could be emptied and readied for new acquisition at slightly different times (10-40 ms apart), and a mismatch could develop between the number of macropulses seen on different channels. Such run-time interactions between the firmware and USB traffic of the DAQ were difficult to characterize, but we estimate that they might cause a systematic error of a few tenths of one percent in the number of macropulses seen by different channels, depending on the user-defined threshold and the buffer size. This effect could contribute to the discrepancy at the highest energies ( $>$ 100 MeV) between our results and past analog-enabled measurements.

During analysis, it was noted that occasionally (1 in 400 macropulses), one or two adjacent macropulses would have an abnormally small number of events. The frequency of these “data dropouts” was similar to the rate of switching between DPP and waveform modes; we suspect it is related to edge case behavior right before or after a mode switch. To mitigate this issue, we threw out any macropulse that had less than 50% of the average event rate in either the flux monitor or TOF detector

![](images/82d5cc7d296ffe674f3543338354d6288ade4fcea15b74d6884efdbb6166707d.jpg)  
FIG. 6: TOF spectra after the analytic deadtime correction and the veto and integrated charge gating for the blank sample (in red) and the $\mathrm { n a t }$ C sample (in blue), from the Ni/Rh experiment. The $\gamma$ -ray peak is visible as a sharp spike at 90 ns, followed by the highest-energy neutrons at 130 ns.

channel.

After applying these corrections, the veto and integrated charge gates were applied to all events and surviving events were populated into TOF spectra (Fig. 6). Next, room background was subtracted (responsible for $0 . 1 \%$ to $1 \%$ of event rate, depending on energy) and spectra were mapped to the energy domain.

From these energy spectra, the raw cross sections were calculated, bin-wise, as follows:

$$
\sigma_ {t o t} = - \frac {1}{\ell \rho_ {A}} \ln \left(\frac {I _ {0}}{I _ {s}} \times \frac {M _ {s}}{M _ {0}}\right) \tag {9}
$$

where $I _ { 0 } / I _ { s }$ is the ratio of counts in the energy spectra between the blank and sample, $M _ { s } / M _ { 0 }$ is the ratio of counts in the monitor detector between the sample and blank (for flux normalization).

Finally, two isotope-dependent corrections were applied to the raw cross sections. First, because the blank sample contains air and not vacuum, the cross section of air must be added to each sample’s cross section. Second, the cross section for $^ \mathrm { 6 4 }$ Ni was corrected for the isotopic enrichment of our sample (92.2%) using our measured $\mathrm { n a t }$ Ni cross section. All other isotopes were sufficiently pure such that the impurity correction was negligible.

To validate our analysis, we first benchmarked our $\sigma _ { t o t }$ measurements of natural samples ( $\mathrm { n a t }$ C, $\mathrm { n a t }$ Ni, $\mathrm { n a t }$ Sn, and $\mathrm { n a t }$ Pb) against the high-precision data sets on natural samples from [8] and [12] (Fig. 7). Our natural sample results are in excellent agreement with these previous results from 3-100 MeV and show slight deviation above 100 MeV (a relative difference of up to 5% at 300 MeV), suggesting a small systematic error at high energies in one or both approaches when the instantaneous neutron flux is highest. As an additional diagnostic, we compared $\sigma _ { t o t }$ results from our long and short natural carbon targets and found excellent agreement, within 1% through-

![](images/7c363fdf95bd7b2d885b392ab6bd7861b7ab40c1dca6188c7fda3e732310a1d7.jpg)  
FIG. 7: (a) A comparison of literature data (taken with analog techniques) and our results (signals processed with a digitizer, or “DSP”) for natural C, Ni, Sn, and Pb. The absolute cross sections are shown from 3-500 MeV. (b) Relative differences between the literature data and our data are shown in percent. From 3-100 MeV, our data are fully consistent with the literature but above 100 MeV, a difference arises, peaking at ${ \approx } 5 \%$ at 300 MeV.

out the measured energy domain.

Extracting the $^ \mathrm { 1 6 , 1 8 }$ O $\sigma _ { t o t }$ required subtraction of the well-measured $\sigma _ { t o t }$ for H. To better characterize the additional systematic uncertainty associated with this subtractive analysis, we subtracted our measured values for $^ { 1 6 }$ O neutron $\sigma _ { t o t }$ from our raw D $^ 2$ O and H2O data and calculated the D-to-H relative difference. A comparison of our D-to-H relative difference with that of [33] is shown in Fig. 8. Our results differ systematically from the previous (analog) measurement by 2-3% throughout the energy range, comparable to the 2% systematic difference between our final $^ { 1 6 }$ O neutron $\sigma _ { t o t }$ results and those of [12]. The size and uniformity of these systematic differences is consistent with a combination of slight (≈1%) normalization errors in some or all of the H, D, O, and C neutron $\sigma _ { t o t }$ results from our measurement or in the literature data.

![](images/7054e68275781b10063b26d01d84032a40a096a22da2eb1fcb8357b3fa6ceef8.jpg)  
FIG. 8: The $\sigma _ { t o t }$ relative difference between deuterium and hydrogen, as calculated by subtraction of our O $\sigma _ { t o t }$ results from D $_ 2$ O and H2O. Data from our measurement are shown as red squares; the data of Abfalterer et al. [33], which were generated using CH $^ 2$ , C8H18, and D $^ 2$ O targets, are shown as black circles.

# EXPERIMENTAL RESULTS

Our absolute $\sigma _ { t o t }$ results for O, Ni, and Sn isotopic targets are shown in Fig. 9. Results for Rh are shown in Fig. 11. Literature isotopic $\sigma _ { t o t }$ measurements (where they exist) are shown alongside our results for comparison. Residuals between our data and any existing literature data are also shown. In each figure, the literature data sets have been rebinned to match the bin structure of our data to facilitate comparison. In regions with a low density of states where individual resonances are visible (e.g., $\mathrm { n a t }$ C below 10 MeV), this rebinning washes out the fine structure of the cross sections.

Except for the already well-measured $^ { 1 6 }$ O, our new data significantly extend knowledge of the neutron $\sigma _ { t o t }$ for each sample. In the cases of $^ { 1 8 }$ O, $^ { 5 8 }$ Ni, $^ \mathrm { 1 0 3 }$ Rh, and $^ { 1 2 4 }$ Sn, almost no previous data were available above 20 MeV. Our new data are in good agreement with the previous measurements where available. In the cases of the rare isotopes $^ \mathrm { 6 4 }$ Ni and $^ { 1 1 2 }$ Sn, data were available at only one energy, 14.1 MeV, from a study from more than 50 years ago [34] and our measurement is in excellent agreement, within 2-3%.

Our results for relative differences between isotopic pairs 16,18O, $^ \mathrm { 5 8 , 6 4 }$ Ni, and $^ { 1 1 2 , 1 2 4 }$ Sn are shown in Fig. 10. For $^ \mathrm { 1 6 , 1 8 }$ O [Fig. 10(a)], the purely isoscalar SAS model [Eq. (1)] grossly reproduces the relative difference below 100 MeV, but fails completely above 100 MeV. Near 200 MeV, the $^ { 1 8 }$ O $\sigma _ { t o t }$ crosses over that of $^ { 1 6 }$ O resulting in a negative relative difference, in keeping with the Ramsauer-logic expectation of Eq. (2) that $\sigma _ { t o t }$ oscillation minima shift to higher energies as $A$ is increased. In the relative difference subfigures for $^ \mathrm { 5 8 , 6 4 }$ Ni and $^ \mathrm { 1 1 2 , 1 2 4 }$ Sn [Fig. 10(b) and 10(c)], the average $\sigma _ { t o t }$ values are below the SAS model trend $\ l _ { r \ \propto \ A ^ { \frac { 1 } { 3 } } }$ ), shown by the dashed

lines. The well-known $r \propto A ^ { \frac { 1 } { 6 } }$ trend in Sn isotope-shift data [35] is also shown for reference and underpredicts the relative differences. In the DOM analyses presented below, we fit only absolute $\sigma _ { t o t }$ data and did not directly fit these relative differences. Still, the relative differences between our individual DOM fits for $^ \mathrm { 5 8 , 6 4 }$ Ni and $^ \mathrm { 1 1 2 , 1 2 4 }$ Sn (black dashed-dotted lines) show overall agreement with the experimental relative differences, especially for the Sn relative difference. For the $^ \mathrm { 1 6 , 1 8 }$ O relative difference, there is an obvious phase mismatch between the oscillations of DOM calculation and the experimental data. This mismatch is symptomatic of a slight DOM overestimation of the $^ { 1 6 } \mathrm { O }$ radius (0.02 fm), which nudges the DOM-calculated $^ { 1 6 }$ O $\sigma _ { t o t }$ rightward so that the $^ { 1 8 } \mathrm { O }$ crossover occurs at too low an energy. As was noted by Dietrich et al. in their study of $\sigma _ { t o t }$ relative differences in W isotopes, a simultaneous OM analysis along the entire isotopic chain, as in [28], may be required to realize the full isovector-constraining power latent in the relative differences.

# DOM ANALYSIS

The DOM is a phenomenological Green’s-function framework enabling a simultaneous and self-consistent analysis of nuclear structure and reaction data. An essential feature of the DOM is the enforcement of a dispersion relation between the complex components of the selfenergy across the entire energy domain, allowing structural data from below the Fermi energy (e.g., charge densities, bound levels) to help constrain the potential above, and data from above the Fermi energy (e.g., elastic, reaction, and total cross sections) to help constrain the potential below. Using our new $\sigma _ { t o t }$ data for 16,18O, $^ \mathrm { 5 8 , 6 4 }$ Ni, and $^ \mathrm { 1 1 2 , 1 2 4 }$ Sn, we performed a simultaneous fit on each isotopic pair and also revisited $^ { 4 0 , 4 8 }$ Ca and $^ { 2 0 8 }$ Pb. Compared to previous DOM analyses [1, 28, 29, 43], we employ an updated version of the DOM that has been generalized for use with any combination of near-spherical even-even nuclei. Partial occupation of neutron open shells, as for the neutron $\mathrm { { d } _ { 5 / 2 } }$ valence shell in $^ { 1 8 } \mathrm { O }$ , is accommodated using the level’s energy $E$ and the pairing parameter $\Delta$ :

$$
\begin{array}{l} \Delta (N, Z) \equiv \frac {1}{4} [ B (N - 2, Z) - 3 B (N - 1, Z) \tag {10} \\ + 3 B (N, Z) - B (N + 1, Z) ], \\ \end{array}
$$

where $B ( N , Z )$ is the binding energy of the nucleus with $N$ neutrons and $Z$ protons. Occupation for the level is split into upper $( n _ { + } )$ and lower $( n _ { - } )$ components:

$$
n _ {\pm} = \frac {1}{2} \left(1 \pm \frac {\chi}{\mathrm {s}}\right), \tag {11}
$$

where $\chi \equiv E - \epsilon _ { F }$ , $s \equiv ( \chi ^ { 2 } + \Delta ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ . Only the lower (occupied) component is included in calculations of boundstate quantities (e.g., total particle number, binding energy).

In the appendices, we provide the functional forms used to define the potential (Appendix A), optimized parameter values with uncertainties (Appendix B), and figures showing the quality of the DOM reproduction to each experimental data set (Appendix C). The other major methodological difference is the use of Markov-Chain Monte Carlo (MCMC) for parameter optimization, discussed below.

For additional details on the underlying DOM formalism, see [44, 45]. To calculate cross sections from the self-energy, the standard R-matrix approach was used [46]. Except where indicated, experimental data used for fitting are the same as in [26]. To situate the reader, we describe the corpus of experimental data and DOM results for 16,18O in full detail. The experimental data used and fit quality for $^ { 4 0 , 4 8 }$ Ca, $^ \mathrm { 5 8 , 6 4 }$ Ni, $^ \mathrm { 1 1 2 , 1 2 4 }$ Sn, and 208Pb are similar in quantity and quality and only key differences are noted. For systematics of neutron skins and binding energies, see companion Letter [23].

# 16O experimental data used in DOM analysis

For protons, twenty-eight differential elastic cross sections data sets and twenty analyzing power data sets from 10-200 MeV were incorporated. Only three proton reaction cross section data sets, ranging from 20-65 MeV, were available. As an added constraint, we used systematic trends from the comprehensive proton $\sigma _ { r x n }$ review of Carlson [47] to generate proton $\sigma _ { r x n }$ pseudodata from 70-200 MeV, which were included in the fit. These pseudo-data are shown as gray open symbols in the proton $\sigma _ { r x n }$ figures in Appendix C. For neutrons, ten differential elastic cross section data sets from 10 MeV to 95 MeV, a single neutron reaction cross section data point at 14 MeV, and our newly measured $\sigma _ { t o t }$ results for $^ { 1 6 }$ O were included. In all, over sixty experimental nucleon scattering data sets were used to constrain the 16O parameters. $^ { 1 6 }$

In addition to nucleon scattering data, several sectors of bound-state data were included in the fit. Neutron (proton) $0 \mathrm { p } _ { 1 / 2 }$ and $0 \mathrm { d } _ { 5 / 2 }$ single-particle level energies were assigned according to the nucleon separation energies of $^ { 1 6 }$ O and 17O isotopes ( $^ { 1 6 }$ O, 17F isotopes) [48]. Charge density distributions were taken from the compilation of [49]. Since the time of that compilation, new experiments (particularly muonic-atom measurements) have improved the precision of many root-mean-square (rms) charge radii by roughly an order of magnitude [50]. To account for these improved data, we rescaled the distributions from [49] to recover the updated rms charge radii while still conserving particle number. We also fitted directly to the updated rms charge radii of [50]. Because the DOM self-energy does not necessarily conserve particle number, we included the “experimental” proton and neutron numbers of eight as part of the fit. Lastly, the total binding energy of $^ { 1 6 }$ O from [48] was included as

![](images/43bbb275dfbe981622661323c9613f31b1e07d55d7a9af8a13b76d72b0156d47.jpg)  
FIG. 9: Neutron $\sigma _ { t o t }$ for $^ \mathrm { 1 6 , 1 8 }$ O, $^ \mathrm { 5 8 , 6 4 }$ Ni, and $^ \mathrm { 1 1 2 , 1 2 4 }$ Sn: our results and literature data. In the upper three panels, our digitizermeasured isotopic results are shown in red and corresponding analog-measured literature data [8, 34, 36–42] are shown in blue. The data for $^ { 1 8 } \mathrm { O }$ have been shifted up by 1 barn for visibility. The lower three panels show residuals between our data and the literature data shown in the upper panels.

![](images/4533946e7291fdff663990c5a3c60f67f9258fbe2315c1fd0f42bcb107a90243.jpg)  
FIG. 10: $^ { 1 6 , 1 8 } \mathrm { O }$ , $^ \mathrm { 5 8 , 6 4 }$ Ni, $^ { 1 1 2 , 1 2 4 }$ Sn neutron $\sigma _ { t o t }$ relative differences from our measurement. In each panel, the colored bands indicate regions of $1 \sigma$ -uncertainty due to target thickness imprecision (blue) and from both target thickness and statistics (red). The gray dashed lines show the prediction for the $\sigma _ { t o t }$ relative difference per the strongly absorbing sphere (SAS) model of Eq. (1), which assumes a simple $A ^ { \frac { 1 } { 3 } }$ size scaling for the nuclear radius. The gray dotted lines show the SAS model prediction but with an $A ^ { \frac { 1 } { 6 } }$ size scaling. The black dash-dotted lines shows the $\sigma _ { t o t }$ relative differences from the median parameter values of the O, Ni, and Sn DOM analyses performed in this work (detailed in the following section).

a constraint.

# 18O experimental data used in DOM analysis

Extensive proton elastic scattering data for $^ { 1 8 }$ O was available from the EXFOR database. Twenty-eight proton elastic differential cross sections were included ranging from 10-200 MeV. Unfortunately, no proton reaction cross section data were available at all in the relevant range of 10-200 MeV. As with $^ { 1 6 }$ O, we generated proton reaction cross section pseudo-data from systematic trends in [47] from 70-200 MeV. On the neutron side,

two differential elastic cross section data sets were included, at 14 and 24 MeV, but no analyzing powers were available. One datum for the neutron reaction cross section, at 14.1 MeV, was incorporated as well. Our $\sigma _ { t o t }$ results for $^ { 1 8 }$ O were the sole neutron total cross section data used in the fit. The energies of the proton and neutron $\mathrm { { 0 p } _ { 1 / 2 } }$ and $0 \mathrm { d } _ { 5 / 2 }$ single-particle levels were assigned according to the same procedure used for $^ { 1 6 }$ O.

Unlike $^ { 1 6 }$ O, for $^ { 1 8 }$ O, no charge density distribution was available from [49]. To approximate it, we rescaled the charge density distribution used for $^ { 1 6 } \mathrm { O }$ to give the $^ { 1 8 } \mathrm { O }$ rms charge radius of [50] while preserving eight units of charge. As with $^ { 1 6 }$ O, we also fitted to the experimental

![](images/4fc8215f08c348872b82d756a38f928305291b6a41c4dfc954221ccac7af9a48.jpg)  
FIG. 11: Neutron $\sigma _ { t o t }$ for $^ \mathrm { 1 0 3 }$ Rh: our results and literature data. In panel (a), our digitizer-measured results are shown in red and corresponding analog-measured literature data [10] are shown in blue. Panel (b) shows the residuals between our data and the literature data, where it exists.

rms charge radius directly, to the particle numbers $N$ and $Z$ , and the total binding energy.

# MCMC analysis

Several aspects of the DOM potential make optimization challenging. Even with the reduced number of potential parameters used in this work (42 for 208Pb and 43 for all other pairwise fits) compared to past DOM studies (for example, 60 or more in [1]), we found that classical gradient-descent methods were inappropriate for reliably searching the parameter space. A recent study [51] systematically compared Bayesian optical model optimization techniques to frequentist ones, the type almost universally used in previous analyses, and found that traditional algorithms may be overconfident in their parameter estimation. To avoid these problems, we used the affine-invariant MCMC library, emcee [52], for optimization and uncertainty characterization. For an in-depth introduction to applied MCMC, see [53].

In the ensemble-sampling approach, several hundred “walkers” are first randomly initialized in parameter space for each isotopic system to be fitted. At each subsequent step $t$ during the random walk, each walker’s position is updated from $\vec { x } _ { t }  \vec { x } _ { t + 1 }$ either by accepting a new position ${ \vec { x } } ^ { \prime }$ with probability:

$$
p (\vec {x} \rightarrow \vec {x} ^ {\prime}) = \min  (1, \frac {U (\vec {x} ^ {\prime} | D)}{U (\vec {x} | D)}), \tag {12}
$$

or by remaining in the same position $\vec { x }$ with probability $1 - p ( \vec { x }  \vec { x } ^ { \prime } )$ . New positions are proposed according

to the stretch-move proposal distribution of [54] (for our stretch move scaling, we used $\alpha \ : = \ : 1 . 3$ instead of the default $\alpha = 2 . 0$ , which improved the typical acceptance fraction from around 5% to 15%). In Eq. (12), the utility of a parameter vector conditional on the experimental data $U ( \vec { x } | D )$ was defined according to Bayes rule (omitting the evidence term):

$$
U (\vec {x} | D) \propto L (D | \vec {x}) \times P (\vec {x}), \tag {13}
$$

where $D$ is the full set of constraining experimental data. The parameter prior distribution $P ( \vec { x } )$ was specified as uniform over a physically reasonable range for each parameter. For example, the diffusenesses of all Woods-Saxon potential geometry terms were restricted to 0.4-1.0 fm. Other more sophisticated choices for the prior distribution (e.g., broad truncated Gaussians) were tested and had little impact on the resulting posterior distributions. The likelihood function was defined as a least-squares function over all data sectors $d$ :

$$
L (D | \vec {x}) = \sum_ {d} \frac {1}{N _ {d}} \sum_ {i = 1} ^ {N _ {d}} \left(\frac {y _ {d , i} ^ {\text {c a l c}} - y _ {d , i} ^ {\text {e x p}}}{\sigma_ {d , i} ^ {\text {c a l c}} + \sigma_ {d , i} ^ {\text {e x p}}}\right) ^ {2}, \tag {14}
$$

where

• $N _ { d }$ is the number of experimental data points in a data sector $d$ ,   
• yd,i $y _ { d , i } ^ { c a l c , e x p }$ calc,exp are the calculated and experimental values, respectively, for the $i ^ { t h }$ datum of sector $d$ ,   
σd,i $\sigma _ { d , i } ^ { c a l c , e x p }$ calc,exp are the assigned model and experimental errors, respectively, for the $i ^ { t h }$ datum of sector $d$ .

Appendix A shows the parameter definitions and prior distributions used in the present analysis.

Due to the choice of functional form and finite model basis size, DOM predictions for nuclear observables suffer from inherent model error. For example, many previous OM analyses tend to easily reproduce low-angle experimental $\frac { d \sigma } { d \Omega }$ data taken at lower scattering energies but are increasingly discrepant with the data at high energies and at backward angles, where the predicted cross sections may differ from experimental results by an order of magnitude or more. This discrepancy indicates a deficiency in the potential form of the OM; ignoring it can lead to drastic underestimation of variances of extracted quantities. In this investigation, we found that the inclusion of reasonable model discrepancy terms in our utility function improved the visual fit to experimental data while broadening parameter uncertainties, in keeping with the methodological findings of [55]. Table II shows the model error terms we used for each data sector. We assigned model error for each data set according to how well preliminary fits could reproduce differing regions of each data sector, the flexibility of the functional forms, and intuition from the successes and failures of past OM analyses. In principle, the form of these model

TABLE II: Model error terms for each data sector used in the MCMC utility function. For terms with units of $\%$ , the model error was calculated as a percentage of the experimental data point magnitude. For $\textstyle { \frac { d { \boldsymbol { \sigma } } } { d \Omega } }$ the model error increased linearly with respect to the scattering angle in the center-ofmass frame with units of $\%$ per degree. $\epsilon _ { n l j }$ are the singleparticle energies for valence nucleons as calculated from separation energies in [48]. $r _ { r m s }$ is the root-mean-square charge radius and $\rho _ { q }$ is the charge density distribution.

<table><tr><td>dσ/dΩ</td><td>A</td><td>σtot</td><td>σrxn</td><td>εnlj</td><td>BE/A</td><td>N,Z</td><td>r_rms</td><td>ρq</td></tr><tr><td>(‰/°)</td><td>(-)</td><td>(%)</td><td>(%)</td><td>(MeV)</td><td>(%)</td><td>(-)</td><td>(fm)</td><td>(%)</td></tr><tr><td>0.25</td><td>0.10</td><td>0.25</td><td>0.25</td><td>0.10</td><td>5.0</td><td>0.10</td><td>0.005</td><td>1.0</td></tr></table>

error terms could also be treated as random variables to be sampled over during MCMC, but due to computational limitations and the already-challenging size of the DOM parameter space, we elected to fix the model error terms. After $N$ samples have been taken from the posterior distribution, a subset can be used to estimate the true parameter distributions, and physics results calculated for each sample. Ensuring that this subset is representative of the true posterior is discussed in the next section.

Following [52] we attempted an autocorrelation analysis to test for convergence and estimate the number of independent samples we had collected for each nucleus. Because of computational limitations on the number of walkers and steps used to approximate the posteriors, posterior estimation involves a finite MCMC sampling error. The integrated autocorrelation time for a physics feature $f$ , denoted $\tau _ { f }$ , represents the number of steps required for a walker to produce a new, decorrelated posterior sample for the feature that is independent of the previous independent sample. In an ideal MCMC analysis, $\tau _ { f }$ could be accurately computed for each physics quantity and the MCMC sampling error could be robustly estimated. In practice, we found this to be computationally infeasible for the DOM parameter space. For example, in preliminary analysis of 18O, we were able to perform $N = 3 1 0 0 0$ steps for each of 336 walkers (more than 100,000 CPU-hours in total). Over this domain, we calculated the integrated autocorrelation time for each potential parameter $p$ , denoted $\tau _ { p }$ , to be roughly 2800 steps. Assuming a $N > 1 0 0 \tau _ { p }$ rule-of-thumb condition for convergence of the $\tau _ { p }$ estimate near its true value, the decorrelation time appears to be extremely long. In other words, from $\tau _ { p }$ alone, we could not exclude the possibility that the parameters had not yet fully “settled” in the region of their optimal values and begun independent sampling of the parameter posteriors. We note that the true $\tau _ { f }$ could be considerably smaller than $\tau _ { p }$ due to the highly correlated nature of DOM parameter space.

To proceed, we applied several commonsense tests to judge whether our parameter and extracted-quantity estimates were accurate. First, we sampled as long as possible and used as many parallel walkers as possible, given

our computational resources. From time to time during sampling, we analyzed the mean walker positions and the mean walker position likelihood as a function of sampling step. Encouragingly, for all nuclei walkers quickly converged on a common region (within 1000 samples) and their mean parameter values stabilized soon afterward (within 10000 samples), suggesting that walkers were sampling a reasonably optimal subspace. At this point, we considered the chain tentatively converged. As an additional test, we re-started sampling from a different (uniformly random) initial position for each nucleus and found that a similar optimal subspace was reached, again within roughly 1000 samples, indicating that our results are independent of the initial walker positions. Finally, for a “converged” chain, we calculated extracted physics quantities (e.g., neutron skins, scattering cross sections) for all walkers at several intervals to confirm that their mean values were stable. Again using $^ { 1 6 }$ O and $^ { 1 8 }$ O as an example, we found their mean neutron skin values varied by less than 0.001 and 0.01 fm, respectively, over several thousand sampling steps late in sampling. Out of caution (and given our expectation of very large autocorrelation times) we used only the terminal sample for each walker chain to produce the results presented here and in the companion Letter [23]. In the end, we expect that additional sampling could slightly reduce the estimated variance of each extracted quantity but have a negligible effect on the mean values. For all quantities derived from MCMC analysis, the estimated $1 6 ^ { \mathrm { t h } }$ , $5 0 ^ { \mathrm { t h } }$ , and $8 4 ^ { \mathrm { t h } }$ posterior percentile values are denoted as $5 0 _ { 1 6 } ^ { 8 4 }$ . The range between the $1 6 ^ { \mathrm { t h } }$ and 84th percentiles corresponds to a $1 \sigma$ -uncertainty range if the posteriors are assumed to be Gaussian. The median values and ranges for each parameter for each isotope system are listed in Appendix B.

# Fit results on $^ \mathrm { 1 6 , 1 8 }$ O

Figure 12 in Appendix C shows the DOM fit of $^ { 1 6 }$ O and experimental data. The experimental proton $\sigma _ { r x n }$ , neutron dΩ , σtot, and σrxn charge density distribution, bind- dσ $\textstyle { \frac { d { \boldsymbol { \sigma } } } { d \Omega } }$ $\sigma _ { t o t }$ $\sigma _ { r x n }$ ing energy per nucleon, and p1/2 and $\mathrm { d } _ { 5 / 2 }$ single-particle energy data are all well-reproduced suggesting that the DOM is effective for modeling nuclei as light as A=16. Almost all experimental proton $\textstyle { \frac { d { \boldsymbol { \sigma } } } { d \Omega } }$ data are accurately reproduced by the DOM calculations with the exception of an overprediction of cross sections at backward angles and high energies, a regime known to be challenging from past OM analyses. In addition, the median DOMgenerated rms charge radius, 2.72 fm, slightly exceeds the experimental value of 2.70 fm. Taken together with the $^ \mathrm { 1 6 , 1 8 }$ O relative difference results in panel (a) of Fig. 10, these overestimations indicate that the traditional OM assumption of radial proportionality with $A ^ { 1 / 3 }$ must be tweaked for a better description of $^ { 1 6 }$ O.

To reproduce the $^ { 1 6 }$ O proton $\sigma _ { r x n }$ pseudo-data gen-

erated from [47], a larger volume imaginary term was required above 100 MeV, which in turn reduced the spectroscopic strength for the valence $\pi$ and $\nu$ p1/2 nucleons by roughly 0.05. We also note the importance of the charge density distribution for determining the magnitude of the imaginary strength below the Fermi energy. For example, in test fits where the charge density was not included as a constraint, most of the negative imaginary strength was concentrated in the surface term between $- 3 0 < E < \epsilon _ { F }$ MeV, and the tail of the charge density was overpredicted. With the charge density included as a constraint, the imaginary surface magnitude shrank by a factor of two and the volume term grew to compensate, pushing nucleon density deeper in energy space and increasing the binding energy closer to the experimental value.

While all data sectors contributed at least some information not fully captured by any other sector, the proton $\sigma _ { r x n }$ , neutron $\sigma _ { t o t }$ , and charge density provided the most stringent constraints on the self-energy. The analyzing powers were the most difficult sector of experimental data to reproduce, with moderate deviations visible from 10-15 MeV for both protons and neutrons and above 100 MeV for protons [Figs. 12(b) and 12(d)]. Some of the difficulty with the analyzing powers is attributable to our neglecting of an imaginary spin-orbit term in the DOM potential used in this work, a choice made due to the unreasonable unbounded growth of the imaginary spin-orbit term as $\ell$ grows in the traditional $\ell \cdot \sigma$ definition used in [21]. In a future analysis we intend to quantitatively investigate the importance of the imaginary spin-orbit term and to compare different options for its functional form.

Figure 13 in Appendix C shows the $^ { 1 8 }$ O experimental data and the DOM fit. The paucity of $^ { 1 8 }$ O experimental data presented a challenge for our analysis. To constrain the negative-energy domain of the potential, the only unambiguous experimental data were the neutron and proton separation energies and the overall binding energy. As with $^ { 1 6 }$ O, broad agreement with experimental data was achieved for experimental proton and neutron dσdΩ data, the neutron σtot, rms charge radius, binding en- $\frac { d \sigma } { d \Omega }$ $\sigma _ { t o t }$ ergy per nucleon, and $\mathrm { { p } _ { 1 / 2 } }$ and $\mathrm { { d } _ { 5 / 2 } }$ single-particle energy data. The artificially scaled charge density and proton $\sigma _ { r x n }$ data were also easily reproduced. Due to the deterioration of systematic trends from [47] below 70 MeV, we did not generate proton $\sigma _ { r x n }$ pseudo-data for lower energies, so the positive-energy surface term of the potential was largely unconstrained in this important area.

In symmetric $^ { 1 6 }$ O, the proton and neutron potentials were identical except for the Coulomb interaction, so the neutron $\sigma _ { t o t }$ data provided information about both the proton and neutron imaginary strength at positive energies. For $^ { 1 8 }$ O, this expectation of symmetric potentials was inapplicable, making proton $\sigma _ { r x n }$ data essential for fixing the positive-energy imaginary strength for protons. In principle, $^ { 1 8 }$ O proton and neutron differential elas-

tic scattering cross sections about 100 MeV could jointly yield some information about the asymmetry-dependence of the imaginary strength for $^ { 1 8 }$ O, but no neutron elastic scattering data were available above 24 MeV. For a better characterization of this nucleus, even a single proton $\sigma _ { r x n }$ datum between 10 and 50 MeV would be valuable.

# Fit results for 40,48Ca, $^ \mathrm { 5 8 , 6 4 }$ Ni, 112,124Sn, and 208Pb

Figures 14-20 in Appendix C show $^ { 4 0 , 4 8 }$ Ca, $^ \mathrm { 6 4 }$ Ni, 112,124Sn, and $^ \mathrm { 2 0 8 }$ Pb experimental data and the DOM fits. The availability of single-nucleon scattering data for $^ { 4 0 , 4 8 }$ Ca, $^ \mathrm { 5 8 , 6 4 }$ Ni, 112,124Sn, and $^ \mathrm { 2 0 8 }$ Pb followed the same trends as that for $^ \mathrm { 1 6 , 1 8 }$ O: plentiful proton differential elastic scattering data, moderate coverage for neutron differential elastic cross sections and proton reaction cross sections on abundant isotopes ( $^ { 4 0 }$ Ca, $^ { 5 8 }$ Ni, and $^ \mathrm { 2 0 8 }$ Pb), with little-to-no coverage for neutron scattering or proton reaction cross section data on rare isotopes ( $^ { 4 8 }$ Ca, $^ \mathrm { 6 4 }$ Ni, 112Sn, $^ { 1 1 2 }$ $^ { 1 2 4 }$ Sn). For $^ { 1 1 2 }$ Sn and $^ { 1 2 4 }$ Sn, however, even proton elastic scattering data sets were sparse and no data above 50 MeV were available, making our newly collected neutron $\sigma _ { t o t }$ data especially valuable in constraining the potential. For $^ { 4 0 }$ Ca and $^ \mathrm { 2 0 8 }$ Pb, experimental proton reaction cross section data were available up to 200 MeV; for the other isotopes, proton reaction cross section pseudodata (discussed in the $^ \mathrm { 1 6 , 1 8 }$ O subsections) were used as a constraint. As for $^ { 1 8 } \mathrm { O }$ , no charge-density parameterization was available for $^ { 1 1 2 }$ Sn in [49], so we rescaled the available $^ { 1 2 4 }$ Sn distribution to reproduce the $^ { 1 1 2 }$ Sn charge radius.

Generally, all sectors of experimental data were wellreproduced; exceptions include the high-angle (above 120°) proton elastic scattering data for $^ { 4 0 }$ Ca and $^ \mathrm { 2 0 8 }$ Pb, where data sets were available up to 200 MeV, and the single-particle energies for neutron open shells in 112,124Sn (see Figs. 18 and 19), where several levels are partially filled and clustered near the Fermi surface. Achieving more accurate single-particle energies while preserving particle number accuracy may require a more sophisticated treatment of pairing. Our new neutron $\sigma _ { t o t }$ data were well-reproduced across the board, typically within 2% of the experimental value, by the DOM fits, suggesting that our Lane-like parameterization of the potential’s asymmetry dependence [Eqs. (29-32)] is a promising starting point for extrapolation away from stability. We note that because $^ \mathrm { 2 0 8 }$ Pb was fit on its own without an isotopic partner, initial fits showed that the asymmetry-dependence of the HF radius term was too poorly constrained to yield reliable neutron skin results; in the final treatment, this term was disabled for 208Pb.

TABLE III: Spectroscopic factors for valence proton ( $\boldsymbol { \mathscr { n } }$ ) and neutron ( $\nu$ ) levels, extracted from our DOM analysis. The $1 6 ^ { \mathrm { t h } }$ , $5 0 ^ { \mathrm { t h } }$ , and ${ 8 4 } ^ { \mathrm { t h } }$ percentile values of the MCMC-generated posterior distributions are reported as $5 0 _ { 1 6 } ^ { 8 4 }$ .   

<table><tr><td colspan="2">Isotope</td><td>16O</td><td>18O</td><td>40Ca</td><td>48Ca</td><td>58Ni</td><td>64Ni</td><td>112Sn</td><td>124Sn</td><td>208Pb</td></tr><tr><td rowspan="2">π</td><td>Level</td><td>0p1/2</td><td>0p1/2</td><td>0d3/2</td><td>0d3/2</td><td>0f7/2</td><td>0f7/2</td><td>0g9/2</td><td>0g9/2</td><td>2s1/2</td></tr><tr><td>SF</td><td>0.640.700.58</td><td>0.590.660.53</td><td>0.630.700.55</td><td>0.620.700.55</td><td>0.590.650.55</td><td>0.570.630.52</td><td>0.550.610.52</td><td>0.560.620.52</td><td>0.640.700.58</td></tr><tr><td rowspan="2">ν</td><td>Level</td><td>0p1/2</td><td>0d5/2</td><td>0d3/2</td><td>0f7/2</td><td>1p3/2</td><td>1p3/2</td><td>1d5/2</td><td>0h11/2</td><td>1f5/2</td></tr><tr><td>SF</td><td>0.630.710.57</td><td>0.830.790.87</td><td>0.620.700.55</td><td>0.720.770.65</td><td>0.720.760.69</td><td>0.680.750.64</td><td>0.650.700.60</td><td>0.640.700.59</td><td>0.670.730.60</td></tr></table>

# Discussion

Table III shows DOM-calculated SFs for valence proton and neutron levels for all nine systems. Significant depletion from the mean-field expectation appears even in the light systems $^ \mathrm { 1 6 , 1 8 }$ O. In the present study, the extracted proton SFs show only a very weak dependence on neutron-richness within each isotopic pair, in keeping with the weak dependence extracted in $( e , e ^ { \prime } p )$ and transfer reaction studies and at odds with knockout-reaction analyses that recover a strong asymmetry-dependence [45, 56]. The recent DOM analyses of [43, 57] identified proton reaction cross sections above roughly 100 MeV as important for their successful reproduction of 40,48Ca $( e , e ^ { \prime } p )$ cross sections without arbitrary SF rescaling. Compared to the present work, these analyses found a much larger reduction of valence proton SFs in $^ { 4 8 }$ Ca with respect to $^ { 4 0 }$ Ca, indicative of an SF asymmetry dependence somewhere between the weak dependence deduced from transfer reactions and the very strong dependence from knockout reactions.

To understand the differences between these analyses, we conducted several diagnostic runs with artificially scaled Carlson pseudo-data in $^ { 4 8 }$ Ca. These diagnostic runs confirmed that fitting to appropriate highenergy proton reaction cross sections leads to larger 48Ca proton imaginary strength both far above and far below the Fermi energy, an effect already seen in previous DOM work. However, the growth we observed in the imaginary potential was more modest compared to previous treatments, potentially explaining the weaker asymmetry-dependent SF reduction. We also note that in the present work, the high-energy neutron total cross sections and proton reaction cross sections appeared to have little impact on other extracted quantities such as neutron skins, as had been previously hypothesized for the neutron skin of $^ { 4 8 }$ Ca [1]. We conclude that the different methodological choices, especially the focus of this work on simultaneous fitting of isotope pairs, is responsible for the differences in these asymmetry-dependent quantities. To further clarify the situation, the potentials of the present work should be used to generate $( e , e ^ { \prime } p )$ cross sections that can be compared to the previous findings of [57].

Surprisingly, despite the extensive proton and neutron elastic scattering data for $^ { 1 6 }$ O, $^ { 4 0 }$ Ca, and $^ \mathrm { 2 0 8 }$ Pb, the extracted spectroscopic factor distributions and parameter

uncertainties for these isotopes are just as wide as for those systems with barely any available elastic scattering data, such as $^ \mathrm { 6 4 }$ Ni. We tentatively conclude that the elastic scattering data we used are very weak constraints on the all-important imaginary terms of the optical potential, at least for the stable, spherical systems discussed here. Unfortunately, this suggests that elastic scattering measurements in inverse kinematics on radioactive beams are of diminishing utility for extrapolating optical potentials away from $\beta$ -stability. A program of proton reaction cross section and neutron total cross section measurements on radioactive targets could be useful for understanding the potential’s near-Fermi-level asymmetry dependence but is experimentally daunting. Instead, a two-pronged approach may be required. On the experimental side, proton reaction and neutron total cross section measurements on stable isotopic chains can help identify which asymmetry-dependence forms are justifiable for increasingly asymmetric systems. On the theoretical side, sensitivity studies are needed to clarify how bound-state data on highly asymmetric systems connect to scattering cross sections.

Lastly, a few systematics in optical potential parameter values are worth mention. For most of the parameters, there was minimal variation with nuclear size or asymmetry, suggesting that a global DOM treatment using the functional forms we have selected is achievable. The radial term for the real central potential (r1) and for the positive-energy imaginary volume and surface $( \mathbf { r _ { 4 } ^ { + } } , \mathbf { r _ { 5 } ^ { + } } )$ are nearly constant among $^ { 4 0 , 4 8 }$ Ca, $^ \mathrm { 5 8 , 6 4 }$ Ni, 112,124Sn, and 208Pb, but the values for $^ \mathrm { 1 6 , 1 8 }$ O show moderate deviations, another indication that the geometric form of the potential is insufficient for light systems. As a consequence of the limited negative-energy data available for fitting, the negative energy geometric terms $( \mathbf { r } _ { 4 } ^ { - } , \mathbf { r } _ { 5 } ^ { - } , \mathbf { a } _ { 4 } ^ { - } , \mathbf { a } _ { 5 } ^ { - } )$ show large variation. The nonlocalities for the negative imaginary components are systematically larger than those for the positive imaginary components. This suggests that while traditional OMs have been able to successfully reproduce positive-energy scattering data with strictly local potentials, description of hole properties requires true nonlocal character in the negativeenergy potential. In practice, we found it impossible to simultaneously reproduce charge density distributions, binding energies, and scattering data unless the central potential and at least the volume imaginary terms were equipped with a nonlocality. In the end, for simplic-

ity and generality, each element of the potential (except Coulomb) was treated nonlocally, but it is unclear which particular data are most important for constraining these several nonlocalities. As one moves further from stability to systems with even less (or no) scattering data available, the risk of overfitting will loom until this issue is resolved.

In preliminary fits, the imaginary volume magnitude $( \mathbf { A } _ { 4 } ^ { - }$ ) component of the potential was shown to be strongly sensitive to the inclusion of the binding energy as a constraint during fitting. We expect the asymmetrydependence of this term, $( \mathbf { A } _ { \mathbf { v o l , a s y m } } ^ { - } )$ , to impact DOMbased predictions of the Ca, Ni, and Sn neutron driplines (as in [28]), though in this work, this dependence was very poorly constrained due to the absence of experimental asymmetry-dependent data probing the most deeply bound nucleons. Because they encode information about how protons and neutrons share energy throughout the nucleus, experimental neutron-skin thicknesses could provide this kind of valuable information. For the Ca, Ni, Sn, and Pb fits, the median positive-energy surface imaginary magnitude $( \mathbf { A _ { s u r , a s y m m } ^ { + } }$ ) is positive, indicating enhancement in proton surface imaginary strength with increasing neutron richness, and a corresponding decrease for neutron surface imaginary strength. Of course, the nuclei under study in the present work are stable; the trend for nuclei with large asymmetries, relevant for the r-process neutron-capture rate, is unknown.

# CONCLUSION

By adopting a digitizer-driven approach, we measured $\sigma _ { t o t }$ on the important closed-shell nuclides $^ \mathrm { 1 6 , 1 8 }$ O, $^ \mathrm { 5 8 , 6 4 }$ Ni, and 112,124Sn across more than two orders of magnitude in energy (3-450 MeV). Except at the highest energies, our results on natural targets are in good agreement with previous analog-mediated measurements that required 10-20 times more target material.

Using these new data and a suite of scattering and bound-state literature data on 16,18O, 58,64Ni, and 112,124Sn, we extracted DOM potentials capable of reproducing a diverse range of scattering and structural data for both neutrons and protons, validating the use of the DOM away from doubly closed shells from $A { = } 1 6$ to A=208, though with indications that the traditional $A ^ { 1 / 3 }$ radial dependence may require modification for light systems. These analyses further indicate that simultaneous fits of isotopically resolved neutron $\sigma _ { t o t }$ , proton $\sigma _ { r x n }$ , and charge-density distribution data on isotopic partners provide a more stringent constraint on the asymmetrydependence of both real and imaginary components.

# ACKNOWLEDGEMENTS

This work is supported by the U.S. Department of Energy, Office of Science, Office of Nuclear Physics under award numbers DE-FG02-87ER-40316, by the U.S. National Science Foundation under grants PHY-1613362 and PHY-1912643, and by the National Nuclear Security Administration of the U.S. Department of Energy at Los Alamos National Laboratory under Contract No. 89233218CNA000001. C.D.P. acknowledges support from the U.S. Department of Energy SCGSR Program (2014 and 2016 solicitations) and the National Nuclear Security Administration through the Center for Excellence in Nuclear Training and University Based Research (CENTAUR) under grant number DE-NA0003841. Computations were performed in part using the facilities of the Washington University Center for High Performance Computing, which were partially provided through NIH grant S10 OD018091, and in part under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344.

[1] M. H. Mahzoon, M. C. Atkinson, R. J. Charity, and W. H. Dickhoff, Phys. Rev. Lett. 119, 222503 (2017), URL https://link.aps.org/doi/10. 1103/PhysRevLett.119.222503.   
[2] F. J. Fattoyev and J. Piekarewicz, Phys. Rev. C 86, 015802 (2012), URL https://link.aps.org/doi/10. 1103/PhysRevC.86.015802.   
[3] X. Vi˜nas, M. Centelles, X. Roca-Maza, and M. Warda, Eur. J. Phys. A 50, 27 (2014), URL https://doi.org/ 10.1140/epja/i2014-14027-8.   
[4] B. A. Brown, Phys. Rev. Lett. 85, 5296 (2000), URL https://link.aps.org/doi/10.1103/PhysRevLett.85. 5296.   
[5] S. Fernbach, R. Serber, and T. B. Taylor, Phys. Rev. 75, 1352 (1949), URL https://link.aps.org/doi/10.1103/ PhysRev.75.1352.   
[6] G. R. Satchler, Introduction to Nuclear Reactions (John Wiley And Sons, 1980).   
[7] J. M. Peterson, Phys. Rev. 125, 955 (1962), URL https: //link.aps.org/doi/10.1103/PhysRev.125.955.   
[8] R. W. Finlay, W. P. Abfalterer, G. Fink, E. Montei, T. Adami, P. W. Lisowski, G. L. Morgan, and R. C. Haight, Phys. Rev. C 47, 237 (1993), URL http://dx. doi.org/10.1103/PhysRevC.47.237.   
[9] R. B. Schwartz, R. A. Schrack, and H. T. Heaton II, Tech. Rep. 138, National Bureau of Standards (1974).   
[10] W. P. Poenitz and J. F. Whalen, Tech. Rep. 80, Argonne National Laboratory (1983).   
[11] W. P. Abfalterer, R. W. Finlay, and S. M. Grimes, Phys. Rev. C 62, 064312 (2000), URL https://link.aps.org/ doi/10.1103/PhysRevC.62.064312.   
[12] W. P. Abfalterer, F. B. Bateman, F. S. Dietrich, R. W. Finlay, R. C. Haight, and G. L. Morgan, Phys. Rev. C 63, 044608 (2001), URL http://dx.doi.org/10.1103/ PhysRevC.63.044608.

[13] S. G. Carpenter and R. Wilson, Phys. Rev. 114, 510 (1959), URL http://journals.aps.org/pr/pdf/10. 1103/PhysRev.114.510.   
[14] I. Angeli and J. Csikai, Nucl. Phys. A 158, 389 (1970), URL http://www.sciencedirect.com/science/ article/pii/0375947470901909.   
[15] C. B. O. Mohr, Proc. Phys. Soc. A 68, 340 (1955), URL http://stacks.iop.org/0370-1298/68/i=4/a=410.   
[16] H. Feshbach, Ann. Rev. Nucl. Part. Sci. 8, 49 (1958), URL https://doi.org/10.1146/annurev.ns.08. 120158.000405.   
[17] K. W. McVoy, Ann. Sci. 43, 91 (1967), URL http://www.sciencedirect.com/science/article/ pii/000349166790293X.   
[18] I. Ahmad, N. Bano, and A. N. Saharia, Pramana - J. Phys. 1, 188 (1973), URL https://link.springer.com/ article/10.1007/BF02847190.   
[19] C. M. Perey and F. G. Perey, Atom. Data Nucl. Data Tables 17 (1976).   
[20] R. L. Varner, W. J. Thompson, T. L. McAbee, E. J. Ludwig, and T. B. Clegg, Phys. Rep. 201, 57 (1991), URL http://www.sciencedirect.com/science/ article/pii/037015739190039O.   
[21] A. J. Koning and J. P. Delaroche, Nucl. Phys. A 713, 231 (2003), URL http://www.sciencedirect.com/science/ article/pii/S0375947402013210.   
[22] F. S. Dietrich, J. D. Anderson, R. W. Bauer, S. M. Grimes, R. W. Finlay, W. P. Abfalterer, F. B. Bateman, R. C. Haight, G. L. Morgan, E. Bauge, et al., Phys. Rev. C 67, 044606 (2003), URL https://link.aps.org/doi/ 10.1103/PhysRevC.67.044606.   
[23] C. D. Pruitt, R. J. Charity, L. G. Sobotka, M. C. Atkinson, and W. H. Dickhoff, Phys. Rev. Lett. 125, 102501 (2020).   
[24] T. W. Phillips, B. L. Berman, and J. D. Seagrave, Phys. Rev. C 22, 384 (1980), URL https://link.aps.org/doi/ 10.1103/PhysRevC.22.384.   
[25] D. G. Foster and D. W. Glasgow, Phys. Rev. C 3, 576 (1971), URL https://link.aps.org/doi/10.1103/ PhysRevC.3.576.   
[26] C. D. Pruitt, Ph.D. thesis, Washington University in St Louis (2019).   
[27] R. Shane, R. J. Charity, J. M. Elson, L. G. Sobotka, M. Devlin, N. Fotiades, and J. M. O‘Donnell, Nucl. Instrum. Meth. 614, 468 (2010), URL http://dx.doi.org/ 10.1016/j.nima.2010.01.005.   
[28] J. M. Mueller, R. J. Charity, R. Shane, L. G. Sobotka, S. J. Waldecker, W. H. Dickhoff, A. S. Crowell, J. H. Esterline, B. Fallin, C. R. Howell, et al., Phys. Rev. C 83, 064605 (2011), URL https://link.aps.org/doi/10. 1103/PhysRevC.83.064605.   
[29] M. H. Mahzoon, R. J. Charity, W. H. Dickhoff, H. Dussan, and S. J. Waldecker, Phys. Rev. Lett. 112, 162503 (2014), URL https://link.aps.org/doi/ 10.1103/PhysRevLett.112.162503.   
[30] M. Mahzoon, Ph.D. thesis, Washington University in St Louis (2015), URL http://libproxy.wustl.edu/ login?url=https://search.proquest.com/docview/ 1749780826?accountid=15159.   
[31] M. S. Moore, Nucl. Instrum. Meth. 169, 245 (1980), URL http://www.sciencedirect.com/science/ article/pii/0029554X80901299.   
[32] J. M. Clement, P. Stoler, C. A. Goulding, and R. W. Fairchild, Nucl. Phys. A 183, 51 (1972), URL http://dx. doi.org/10.1016/0375-9474(72)90930-X.

[33] W. P. Abfalterer, F. B. Bateman, F. S. Dietrich, C. Elster, R. W. Finlay, W. Gl¨ockle, J. Golak, R. C. Haight, D. H¨uber, G. L. Morgan, et al., Phys. Rev. Lett. 81 (1998).   
[34] Y. V. Dukarevich, A. N. Dyumin, and D. M. Kaminker, Nucl. Phys. A 92, 433 (1967), URL http://dx.doi.org/ 10.1016/0375-9474(67)90228-X.   
[35] M. Anselment, K. Bekk, A. Hanser, H. Hoeffgen, G. Meisel, S. Goring, H. Rebel, and G. Schatz, Phys. Rev. C 34, 1052 (1986).   
[36] F. G. Perey, T. A. Love, and W. E. Kinney, Tech. Rep. 4823, Oak Ridge National Lab (1972).   
[37] F. J. Vaughn, H. A. Grench, W. L. Imhof, J. H. Rowland, and M. Walt, Nucl. Phys. 64, 336 (1965), URL http: //dx.doi.org/10.1016/0029-5582(65)90361-5.   
[38] S. R. Salisbury, D. B. Fossan, and F. J. Vaughn, Nucl. Phys. 64, 343 (1965), URL http://dx.doi.org/10.1016/ 0029-5582(65)90362-7.   
[39] C. M. Perey, F. G. Perey, J. A. Harvey, N. W. Hill, N. M. Larson, R. L. Macklin, and D. C. Larson, Phys. Rev. C 47, 1143 (1993), URL http://dx.doi.org/10. 1103/PhysRevC.47.1143.   
[40] R. W. Harper, T. W. Godfrey, and J. L. Weil, Phys. Rev. C 26, 1432 (1982), URL http://dx.doi.org/10.1103/ PhysRevC.26.1432.   
[41] V. M. Timokhov, M. V. Bokhovko, A. G. Isakov, L. E. Kazakov, V. N. Kononov, G. N. Manturov, E. D. Poletaev, and V. G. Pronyaev, Yad. Fiz. 50, 609 (1989).   
[42] J. Rapaport, M. Mirzaa, M. Hadizadeh, D. E. Bainum, and R. W. Finlay, Nucl. Phys. A 341, 56 (1980), URL http://dx.doi.org/10.1016/0375-9474(80)90361-9.   
[43] M. C. Atkinson, H. P. Blok, L. Lapik´as, R. J. Charity, and W. H. Dickhoff, Phys. Rev. C 98, 044627 (2018), URL https://link.aps.org/doi/10. 1103/PhysRevC.98.044627.   
[44] C. Mahaux and R. Sartor, Adv. Nucl. Phys. 20, 1 (1991).   
[45] W. H. Dickhoff and R. J. Charity, Prog. Part. Nucl. Phys. (2018).   
[46] A. M. Lane and R. G. Thomas, Rev. Mod. Phys. 30, 257 (1958), URL https://link.aps.org/doi/10.1103/ RevModPhys.30.257.   
[47] R. F. Carlson, Atom. Data Nucl. Data Tables 63, 93 (1996), URL http://www.sciencedirect.com/science/ article/pii/S0092640X96900108.   
[48] M. Wang, G. Audi, F. G. Kondev, W. Huang, S. Naimi, and X. Xi, Chin. Phys. C 41, 030003 (2017).   
[49] H. D. Vries, C. W. D. Jager, and C. D. Vries, Atom. Data Nucl. Data Tables 36, 495 (1987), URL https://www.sciencedirect.com/science/article/ pii/0092640X87900131.   
[50] I. Angeli and K. P. Marinova, Atom. Data Nucl. Data Tables 99, 69 (2013), URL http://www.sciencedirect. com/science/article/pii/S0092640X12000265.   
[51] G. B. King, A. E. Lovell, L. Neufcourt, and F. M. Nunes, Phys. Rev. Lett. 122, 232502 (2019).   
[52] D. Foreman-Mackey, D. W. Hogg, D. Lang, and J. Goodman, Publ. Astron. Soc. Pac. 125, 306312 (2013), URL http://dx.doi.org/10.1086/670067.   
[53] S. Sharma, Ann. Rev. Astron. Astrophys. 55, 213 (2017).   
[54] J. Goodman and J. Weare, Commun. Appl. Math. Comput. Sci. 5, 65 (2010), URL https://doi.org/10.2140/ camcos.2010.5.65.   
[55] J. Brynjarsdttir and A. O’Hagan, Inverse Problems 30 (2014).   
[56] J. A. Tostevin and A. Gade, Phys. Rev. C 90, 057602 (2014), URL https://link.aps.org/doi/10.

1103/PhysRevC.90.057602.   
[57] M. C. Atkinson and W. H. Dickhoff, Phys. Lett. B 798, 135027 (2019), URL http://www.sciencedirect. com/science/article/pii/S037026931930749X.   
[58] F. Perey and B. Buck, Nucl. Phys. 32, 353 (1962), URL http://www.sciencedirect.com/science/ article/pii/0029558262903450.   
[59] R. J. Charity, J. M. Mueller, L. G. Sobotka, and W. H. Dickhoff, Phys. Rev. C 76, 044314 (2007), URL https: //link.aps.org/doi/10.1103/PhysRevC.76.044314.

# Appendix A: Definition of DOM Potential

# Functional Forms

Before giving the full parameterization, we identify a few standard functional forms. Radial dependences are defined by a Woods-Saxon shape or a derivative:

$$
f _ {v o l} (r; r _ {0}, a) = \frac {- 1}{1 + e ^ {(r - R) / a}}, \tag {15}
$$

$$
f _ {s u r} (r; r _ {0}, a) = \frac {1}{r} \frac {d}{d r} f _ {v o l} (r; r _ {0}, a).
$$

$R$ is the nuclear radius, calculated as $R = r _ { 0 } A ^ { \frac { 1 } { 3 } }$ . The sign of the potential is such that the Woods-Saxon form provides an attractive interaction. For nonlocalities, we use a Gaussian nonlocality first proposed by [58]:

$$
N (r, r ^ {\prime}; \beta) = \frac {1}{\pi^ {\frac {3}{2}} \beta^ {3}} e ^ {- (r - r ^ {\prime}) ^ {2} / \beta^ {2}}, \tag {16}
$$

where $\beta$ sets the Gaussian width. The energydependences of the imaginary components is based on the functional form of [59]:

$$
\omega_ {n} (E; A, B, C) = \Theta (X) A \frac {X ^ {n}}{X ^ {n} + B ^ {n}} \tag {17}
$$

where

$$
X = | E - \epsilon_ {F} | - C
$$

and $\Theta ( X )$ is the Heaviside step function.

For symmetric nuclei, the same potential was used for protons and neutrons, excepting Coulomb. For asymmetric nuclei, we introduced five asymmetry-dependent terms. For all energy dependences, the energy domain was $\epsilon _ { F }$ -300 MeV to $\epsilon _ { F } + 2 0 0$ MeV.

The irreducible self-energy (optical potential) used in this work is defined

$$
\Sigma^ {*} (\alpha , \beta ; E) = \Sigma_ {s} ^ {*} (\alpha , \beta) + \Sigma_ {i m} ^ {*} (\alpha , \beta ; E) + \Sigma_ {d} ^ {*} (\alpha , \beta ; E). \tag {18}
$$

The energy-independent real part $\Sigma _ { s } ( \alpha , \beta )$ and energydependent imaginary part $\Sigma _ { i m } ^ { * } ( \alpha , \beta )$ parameterizations are given in the following two subsections. The dispersive correction term $\Sigma _ { d } ^ { * } * \alpha , \beta ; E )$ is completely determined by an integral over the imaginary part [Eq. (3) of [29]]. All free parameters that are fit via MCMC sampling are typeset in bold.

# Real Part

The energy-independent real part of the self-energy consists of a nonlocal Hartree-Fock and a spin-orbit component (plus a local Coulomb term if the nucleon in question is a proton):

$$
\Sigma_ {s} (r, r ^ {\prime}) = \Sigma_ {H F} (r, r ^ {\prime}) + V _ {s o} (r, r ^ {\prime}) + V _ {C} (r) \delta (r - r ^ {\prime}). \tag {19}
$$

The Coulomb potential is calculated using the same experimentally derived charge density distributions (see [49]) used in fitting. The Hartree-Fock component $V _ { H F }$ has two subcomponents:

$$
\Sigma_ {H F} (r, r ^ {\prime}) = V _ {v o l} (r, r ^ {\prime}) + V _ {w b} (r), \tag {20}
$$

where the nonlocal Hartree-Fock volume term $V _ { v o l } ( r , r ^ { \prime } )$ , is defined as a Woods-Saxon form coupled to a Gaussian nonlocality:

$$
V _ {v o l} \left(r, r ^ {\prime}\right) = - \mathbf {V} _ {\mathbf {1}} \times f _ {v o l} \left(r; \mathbf {r} _ {\mathbf {1}}, \mathbf {a} _ {\mathbf {1}}\right) \times N \left(r, r ^ {\prime}; \boldsymbol {\beta} _ {\mathbf {1}}\right). \tag {21}
$$

The local Hartree-Fock wine-bottle term $V _ { w b }$ , named for resemblance to the dimple at the bottom of a wine bottle, is defined as a Gaussian centered at the nuclear origin,

$$
V _ {w b} (r) = \mathbf {V} _ {\mathbf {2}} \times e ^ {r ^ {2} / \sigma_ {\mathbf {2}} ^ {2}}. \tag {22}
$$

The real spin-orbit component $V _ { s o }$ is defined using a derivative-Woods-Saxon shape in keeping with the expectation that the spin-orbit coupling is strongest near the nuclear surface:

$$
\begin{array}{l} V _ {s o} \left(r, r ^ {\prime}\right) = \left(\frac {\hbar}{m _ {\pi} c}\right) ^ {2} \mathbf {V} _ {\mathbf {3}} \times \frac {1}{r} f _ {s u r} \left(r; \mathbf {r} _ {\mathbf {3}}, \mathbf {a} _ {\mathbf {3}}\right) \tag {23} \\ \times N (r, r ^ {\prime}; \boldsymbol {\beta} _ {3}) \times (\ell \cdot \sigma). \\ \end{array}
$$

The leading constant $\begin{array} { r l r } {  { ( \frac { \hbar } { m _ { \pi } c } ) ^ { 2 } } } & { { } } & { } \end{array}$ is taken to be 2.0 fm2 [30]. In total, there are ten free parameters for the symmetric real part of the potential.

# Imaginary Part

The imaginary part of the potential is comprised of independent surface and volume terms both above and below the Fermi surface:

$$
\Sigma_ {i m} ^ {*} (r, r ^ {\prime}, E) = \Sigma_ {v o l} ^ {\pm} (r, r ^ {\prime}, E) + \Sigma_ {s u r} ^ {\pm} (r, r ^ {\prime}, E), \tag {24}
$$

where the volume and surface components are defined:

$$
\begin{array}{l} \Sigma_ {v o l} ^ {\pm} (r, r ^ {\prime}, E) = W _ {v o l} ^ {\pm} (E) \times f _ {v o l} (r; \mathbf {r} _ {4} ^ {\pm}, \mathbf {a} _ {4} ^ {\pm}) \\ \times N \left(r, r ^ {\prime}; \beta_ {4} ^ {\pm}\right), \\ \end{array}
$$

$$
\begin{array}{l} \Sigma_ {s u r} ^ {\pm} (r, r ^ {\prime}, E) = 4 \mathbf {a} _ {\mathbf {5}} W _ {s u r} ^ {\pm} (E) \times f _ {s u r} (r; \mathbf {r} _ {\mathbf {5}} ^ {\pm}, \mathbf {a} _ {\mathbf {5}} ^ {\pm}) \tag {25} \\ \times N \left(r, r ^ {\prime}; \beta_ {5} ^ {\pm}\right). \\ \end{array}
$$

The terms labeled with $^ +$ determine the potential above $\epsilon _ { F }$ , and the terms labeled with $-$ determine the potential below $\epsilon _ { F }$ . The energy dependence of the imaginary volume terms read:

$$
W _ {v o l} ^ {\pm} (E) = \mathbf {A} _ {\mathbf {4}} ^ {\pm} \left[ \frac {(E _ {\Delta}) ^ {4}}{(E _ {\Delta}) ^ {4} + (\mathbf {B} _ {\mathbf {4}} ^ {\pm}) ^ {4}} + W _ {N M} ^ {\pm} (E) \right], \quad (2 6)
$$

where $\begin{array} { r } { E _ { \Delta } = | E - \epsilon _ { F } | } \end{array}$ and

$$
\begin{array}{l} W _ {N M} ^ {+} (E) = \alpha_ {\bf 4} \left[ \sqrt {E} + \frac {(\epsilon_ {F} + {\bf E _ {4} ^ {+}}) ^ {\frac {3}{2}}}{2 E} - \frac {3}{2} \sqrt {\epsilon_ {F} + {\bf E _ {4} ^ {+}}} \right], \\ W _ {N M} ^ {-} (E) = \frac {\left(\epsilon_ {F} - E - \mathbf {E} _ {4} ^ {-}\right) ^ {2}}{\left(\epsilon_ {F} - E - \mathbf {E} _ {4} ^ {-}\right) ^ {2} + \left(\mathbf {E} _ {4} ^ {-}\right) ^ {2}}. \tag {27} \\ \end{array}
$$

The terms $W _ { N M } ^ { \pm }$ are asymmetric above and below the Fermi surface and are modeled after nuclear-matter calculations. They account for the decreasing phase space at negative energies and the increasing phase space at positive energies. The energy-dependence of the imaginary surface terms read:

$$
W _ {s u r} ^ {\pm} (E) = \omega_ {4} \left(E, \mathbf {A} _ {5} ^ {\pm}, \mathbf {B} _ {5} ^ {\pm}, 0\right) - \omega_ {2} \left(E, \mathbf {A} _ {5} ^ {\pm}, \mathbf {B} _ {5} ^ {\prime \pm}, \mathbf {C} _ {5} ^ {\pm}\right) \tag {28}
$$

In total, there are thirteen free parameters for the symmetric imaginary volume terms of the potential and fourteen free parameters for the symmetric imaginary surface terms of the potential. Thus for symmetric nuclei, thirtyseven real and imaginary parameters were used.

# Parameterization of Asymmetry Dependence

For asymmetric nuclei, the parametric forms must be modified to account for the different potential experienced by protons and neutrons. For the real central potential, the depth $\mathbf { V _ { 1 } }$ and radius $\mathbf { r _ { 1 } }$ from Eq. (21) were allowed to vary linearly with asymmetry:

$$
\mathbf {V} _ {1} \Rightarrow \left\{ \begin{array}{l l} \mathbf {V} _ {1} + \mathbf {V} _ {\text {a s y m}} \times \frac {N - Z}{A} & \text {f o r p r o t o n s} \\ \mathbf {V} _ {1} - \mathbf {V} _ {\text {a s y m}} \times \frac {N - Z}{A} & \text {f o r n e u t r o n s ,} \end{array} \right. \tag {29}
$$

$$
\mathbf {r} _ {1} \Rightarrow \left\{ \begin{array}{l l} \mathbf {r} _ {1} + \mathbf {r} _ {\text {a s y m}} \times \frac {N - Z}{A} & \text {f o r p r o t o n s} \\ \mathbf {r} _ {1} - \mathbf {r} _ {\text {a s y m}} \times \frac {N - Z}{A} & \text {f o r n e u t r o n s .} \end{array} \right. \tag {30}
$$

The magnitude of the energy-dependence for the imaginary surface and volume potentials, ${ \bf A } _ { 4 } ^ { \pm }$ and $\mathbf { A _ { 5 } ^ { \pm } }$ from Eqs. (26) and (28), were also allowed to vary with linearly with asymmetry:

$$
\mathbf {A} _ {4} ^ {\pm} \Rightarrow \left\{ \begin{array}{l l} \mathbf {A} _ {4} ^ {\pm} + \mathbf {A} _ {\text {v o l , a s y m}} ^ {\pm} \times \frac {N - Z}{A} & \text {f o r p r o t o n s} \\ \mathbf {A} _ {4} ^ {\pm} - \mathbf {A} _ {\text {v o l , a s y m}} ^ {\pm} \times \frac {N - Z}{A} & \text {f o r n e u t r o n s}, \end{array} \right. \tag {31}
$$

$$
\mathbf {A} _ {5} ^ {\pm} \Rightarrow \left\{ \begin{array}{l l} \mathbf {A} _ {5} ^ {\pm} + \mathbf {A} _ {\text {s u r}, \text {a s y m}} ^ {\pm} \times \frac {N - Z}{A} & \text {f o r p r o t o n s} \\ \mathbf {A} _ {5} ^ {\pm} - \mathbf {A} _ {\text {s u r}, \text {a s y m}} ^ {\pm} \times \frac {N - Z}{A} & \text {f o r n e u t r o n s .} \end{array} \right. \tag {32}
$$

There should be no confusion between $\mathbf { A } _ { 4 , 5 } ^ { \pm }$ , $A$ (the total number of nucleons), and the analyzing power. With these six additional asymmetry-dependent terms, the total number of free parameters used for fitting asymmetric nuclei in the present work totals forty-three.

Parameter labels correspond to those in the equations of Appendix A. For each parameter, the prior distribution was defined to be uniform with minimum and maximum values listed in columns 2 and 3 of each table. For each nucleus, the $1 6 ^ { \mathrm { t h } }$ , $5 0 ^ { \mathrm { t h } }$ , and 84th percentile values for each estimated parameter distribution are listed. The format is $5 0 _ { 1 6 } ^ { 8 4 }$ . For $^ \mathrm { 2 0 8 }$ Pb, the asymmetry-dependent HF radius term (rasym) was disabled during fitting.

TABLE IV: Real central potential parameters   

<table><tr><td>Par.</td><td>Min</td><td>Max</td><td>Units</td><td>Eq.</td><td>16,18O</td><td>40,48Ca</td><td>58,64Ni</td><td>112,124Sn</td><td>208Pb</td></tr><tr><td>V1</td><td>50</td><td>150</td><td>MeV</td><td>19</td><td>112.0124.8100.1</td><td>101.6111.392.3</td><td>103.4115.892.5</td><td>108.7119.098.2</td><td>102.6120.491.0</td></tr><tr><td>Vasym</td><td>-100</td><td>200</td><td>MeV</td><td>27</td><td>-10.6634.39-49.61</td><td>40.5853.8128.47</td><td>-17.328.71-43.29</td><td>24.5943.084.09</td><td>30.3642.0520.18</td></tr><tr><td>r1</td><td>0.6</td><td>1.6</td><td>fm</td><td>19</td><td>0.991.030.95</td><td>1.101.131.07</td><td>1.091.121.06</td><td>1.111.141.09</td><td>1.121.161.09</td></tr><tr><td>rasym</td><td>-1.0</td><td>1.0</td><td>fm</td><td>28</td><td>0.10-0.11</td><td>-0.01-0.10</td><td>0.340.21</td><td>-0.04-0.13</td><td>-</td></tr><tr><td>a1</td><td>0.4</td><td>1.0</td><td>fm</td><td>19</td><td>0.510.560.46</td><td>0.580.630.54</td><td>0.600.640.56</td><td>0.480.580.42</td><td>0.680.750.60</td></tr><tr><td>β1</td><td>0.5</td><td>1.5</td><td>fm</td><td>19</td><td>1.051.130.96</td><td>1.141.201.06</td><td>1.101.191.02</td><td>1.171.231.12</td><td>1.141.231.06</td></tr><tr><td>V2</td><td>0</td><td>50</td><td>MeV</td><td>20</td><td>27.7643.6210.72</td><td>26.007.53</td><td>24.6840.647.01</td><td>29.5144.7710.54</td><td>25.50842.30</td></tr><tr><td>σ2</td><td>0</td><td>3</td><td>fm</td><td>20</td><td>0.110.200.04</td><td>0.160.250.05</td><td>0.170.260.05</td><td>0.260.330.21</td><td>0.170.270.07</td></tr></table>

TABLE V: Imaginary central potential parameters   

<table><tr><td>Par.</td><td>Min</td><td>Max</td><td>Units</td><td>Eq.</td><td>16,18O</td><td>40,48Ca</td><td>58,64Ni</td><td>112,124Sn</td><td>208Pb</td></tr><tr><td>A+4</td><td>0</td><td>60</td><td>MeV</td><td>24</td><td>34.244921</td><td>23.143487</td><td>25.694118</td><td>25.603694</td><td>26.463555</td></tr><tr><td>B+4</td><td>0</td><td>200</td><td>MeV</td><td>24</td><td>71.208682</td><td>74.909595</td><td>77.019772</td><td>53.226699</td><td>65.467713</td></tr><tr><td>r+4</td><td>0.6</td><td>1.6</td><td>fm</td><td>23</td><td>0.921.16</td><td>1.191.31</td><td>1.341.44</td><td>1.231.32</td><td>1.281.33</td></tr><tr><td>a+4</td><td>0.4</td><td>1.0</td><td>fm</td><td>23</td><td>0.820.94</td><td>0.780.93</td><td>0.650.83</td><td>0.780.93</td><td>0.680.84</td></tr><tr><td>β+4</td><td>0.5</td><td>1.5</td><td>fm</td><td>23</td><td>0.620.75</td><td>0.590.67</td><td>0.730.82</td><td>0.680.63</td><td>0.600.67</td></tr><tr><td>A-4</td><td>0</td><td>60</td><td>MeV</td><td>24</td><td>10.052498</td><td>34.265139</td><td>28.153791</td><td>30.564231</td><td>38.005109</td></tr><tr><td>B-4</td><td>0</td><td>200</td><td>MeV</td><td>24</td><td>130.31771</td><td>110.51539</td><td>79.01252</td><td>72.71172</td><td>105.81593</td></tr><tr><td>r-4</td><td>0.6</td><td>1.6</td><td>fm</td><td>23</td><td>1.091.36</td><td>0.961.14</td><td>1.001.15</td><td>0.911.07</td><td>1.121.23</td></tr><tr><td>a-4</td><td>0.4</td><td>1.0</td><td>fm</td><td>23</td><td>0.720.90</td><td>0.610.81</td><td>0.700.87</td><td>0.800.94</td><td>0.560.76</td></tr><tr><td>β-4</td><td>0.5</td><td>1.5</td><td>fm</td><td>23</td><td>1.021.35</td><td>0.981.31</td><td>1.001.29</td><td>1.031.31</td><td>1.151.39</td></tr><tr><td>α4</td><td>0</td><td>0.5</td><td>-</td><td>25</td><td>0.160.29</td><td>0.200.28</td><td>0.130.29</td><td>0.180.26</td><td>0.200.30</td></tr><tr><td>E+4</td><td>50</td><td>200</td><td>MeV</td><td>25</td><td>109.51605</td><td>109.9157</td><td>105.61606</td><td>90.01258</td><td>132.21780</td></tr><tr><td>E-4</td><td>50</td><td>200</td><td>MeV</td><td>25</td><td>104.71439</td><td>101.31316</td><td>114.21445</td><td>127.9970</td><td>135.11713</td></tr><tr><td>A+vol,asym</td><td>-100</td><td>200</td><td>MeV</td><td>29</td><td>37.727602</td><td>11.392873</td><td>8.473029</td><td>7.531804</td><td>17.442966</td></tr><tr><td>A- vol,asym</td><td>-100</td><td>200</td><td>MeV</td><td>29</td><td>131.11802</td><td>7.91178</td><td>-10.396667</td><td>-8.867086</td><td>-9.275004</td></tr></table>

TABLE VI: Imaginary surface potential parameters   

<table><tr><td>Par.</td><td>Min</td><td>Max</td><td>Units</td><td>Eq.</td><td>16,18O</td><td>40,48Ca</td><td>58,64Ni</td><td>112,124Sn</td><td>208Pb</td></tr><tr><td>A5+</td><td>0</td><td>50</td><td>MeV</td><td>26</td><td>24.1834.5417.24</td><td>23.5731.9116.31</td><td>25.2234.1717.14</td><td>31.6341.3222.73</td><td>32.9841.9022.15</td></tr><tr><td>B5+</td><td>0</td><td>50</td><td>MeV</td><td>26</td><td>21.9624.1419.70</td><td>21.7324.5718.83</td><td>18.3420.6015.74</td><td>18.8921.9016.54</td><td>18.4220.9315.79</td></tr><tr><td>B′5+</td><td>0</td><td>50</td><td>MeV</td><td>26</td><td>28.7337.5920.87</td><td>41.4047.7931.75</td><td>31.9240.2023.80</td><td>29.0838.4721.91</td><td>41.1447.1831.04</td></tr><tr><td>C5+</td><td>0</td><td>10</td><td>MeV</td><td>26</td><td>4.788.311.81</td><td>5.768.651.79</td><td>6.688.833.29</td><td>3.016.850.87</td><td>6.368.6222.75</td></tr><tr><td>r5+</td><td>0.6</td><td>1.6</td><td>fm</td><td>23</td><td>1.381.481.21</td><td>1.211.311.07</td><td>1.221.301.10</td><td>1.221.291.08</td><td>1.221.261.16</td></tr><tr><td>a5+</td><td>0.4</td><td>1.0</td><td>fm</td><td>23</td><td>0.590.790.49</td><td>0.730.860.63</td><td>0.660.800.56</td><td>0.670.800.57</td><td>0.610.760.51</td></tr><tr><td>β5+</td><td>0.5</td><td>1.5</td><td>fm</td><td>23</td><td>1.041.360.72</td><td>1.131.361.84</td><td>0.991.270.72</td><td>0.961.250.72</td><td>0.871.070.67</td></tr><tr><td>A-5</td><td>0</td><td>50</td><td>MeV</td><td>26</td><td>23.0234.3213.93</td><td>38.6147.5923.44</td><td>24.8536.3112.25</td><td>26.0434.5417.03</td><td>35.0845.7024.41</td></tr><tr><td>B-5</td><td>0</td><td>50</td><td>MeV</td><td>26</td><td>11.7814.839.09</td><td>13.4918.269.98</td><td>9.0711.067.23</td><td>9.1611.287.51</td><td>15.7721.6611.11</td></tr><tr><td>B′-5</td><td>0</td><td>50</td><td>MeV</td><td>26</td><td>33.4844.7921.44</td><td>36.3246.1122.61</td><td>32.1543.9920.96</td><td>28.4739.3118.61</td><td>34.4943.9523.61</td></tr><tr><td>C-5</td><td>0</td><td>10</td><td>MeV</td><td>26</td><td>6.479.023.35</td><td>6.248.571.88</td><td>5.848.712.54</td><td>5.518.681.70</td><td>7.079.244.03</td></tr><tr><td>r-5</td><td>0.6</td><td>1.6</td><td>fm</td><td>23</td><td>0.760.910.64</td><td>0.820.930.67</td><td>0.780.970.63</td><td>1.101.141.02</td><td>1.011.080.88</td></tr><tr><td>a-5</td><td>0.4</td><td>1.0</td><td>fm</td><td>23</td><td>0.470.570.42</td><td>0.510.620.43</td><td>0.620.740.48</td><td>0.530.680.44</td><td>0.640.850.50</td></tr><tr><td>β-5</td><td>0.5</td><td>1.5</td><td>fm</td><td>23</td><td>1.171.400.92</td><td>1.241.390.98</td><td>1.121.310.90</td><td>1.121.340.91</td><td>0.911.170.71</td></tr><tr><td>A+sur,asym</td><td>-100</td><td>200</td><td>MeV</td><td>30</td><td>-22.1015.74-64.99</td><td>20.1145.792.93</td><td>9.4240.11-25.44</td><td>54.3280.9129.32</td><td>27.4555.0066.87</td></tr><tr><td>Asur,asym</td><td>-100</td><td>200</td><td>MeV</td><td>30</td><td>48.2142.3-52.4</td><td>-7.6831.56-47.07</td><td>12.9254.11-28.07</td><td>11.3537.52-16.09</td><td>-4.7924.43-32.12</td></tr></table>

TABLE VII: Spin-orbit parameters   

<table><tr><td>Par.</td><td>Min</td><td>Max</td><td>Units</td><td>Eq.</td><td>16,18O</td><td>40,48Ca</td><td>58,64Ni</td><td>112,124Sn</td><td>208Pb</td></tr><tr><td>V3</td><td>0</td><td>20</td><td>MeV</td><td>21</td><td>10.4412648.57</td><td>12.0713.9310.36</td><td>13.4816.0011.28</td><td>9.9912.498.00</td><td>13.0516.6210.03</td></tr><tr><td>r3</td><td>0.6</td><td>1.6</td><td>fm</td><td>21</td><td>0.891.000.79</td><td>0.931.020.81</td><td>1.051.140.90</td><td>1.051.140.97</td><td>1.141.201.05</td></tr><tr><td>a3</td><td>0.4</td><td>1.0</td><td>fm</td><td>21</td><td>0.600.720.49</td><td>0.680.790.57</td><td>0.680.850.55</td><td>0.600.770.46</td><td>0.770.900.61</td></tr><tr><td>β3</td><td>0.5</td><td>1.5</td><td>fm</td><td>21</td><td>0.590.800.53</td><td>0.630.750.54</td><td>0.741.000.58</td><td>0.831.080.59</td><td>0.770.050.60</td></tr></table>

# Appendix C: DOM Fit Comparison to Experimental Data

Figures 12-20 show the data sectors used to constrain the DOM potential. Experimental scattering cross sections are shown as points with associated experimental error bars in panels (a) through (f) of each figure. Experimental bound-state data are shown as bands in panels (g) through (j). DOM calculations for each data sector are plotted as $1 \sigma$ and $2 \sigma$ uncertainty bands. References for each data set are provided in Appendix B of [26].

Panels (a) and (c) show proton $\textstyle { \frac { d { \boldsymbol { \sigma } } } { d \Omega } }$ and analyzing powers from 10-200 MeV. Panels (b) and (d) show neutron $\textstyle { \frac { d { \boldsymbol { \sigma } } } { d \Omega } }$ and analyzing powers from 10-200 MeV. For visibility, data sets at different energies are offset vertically and colored according to the scattering energy. Panels (e) show proton $\sigma _ { r x n }$ data. Experimental data are plotted as black points and pseudo-data generated from [47] are plotted as gray open circles. Panels (f) show the neutron $\sigma _ { t o t }$ and $\sigma _ { r x n }$ . The charge distributions of panels (g) are derived from the compilation of [49] (see comments in DOM Analysis section), and are displayed with an arbitrary 1% uncertainty band in black. In panels (h), single-particle energies $\epsilon _ { n l j }$ are shown as horizontal lines. In the “calc” column, DOM-calculated single-particle energies are plotted; the height of each rectangle spans the $1 \sigma$ calculated uncertainty for that level. Panels (i) show DOM-calculated charge radii; the experimental charge radius is displayed using dark gray and light gray bands representing $1 \sigma$ and $2 \sigma$ uncertainties, respectively. Panels (j) show the DOM-calculated binding energy per nucleon; the experimental value is shown with a thin gray band.

![](images/c579dae6e8c84234f41dd9a7adf603144c25e562266821beca246fd850634455.jpg)

![](images/e47dc35a093081fce9198ff5fb6c77def68ea06d551306eb31a918d09b35a591.jpg)

![](images/9d1fdd8dfd8231096be911fa3ed4e13dfa544262a2e479b1060270b0c203bc17.jpg)

![](images/040455ca5299685e9e1b4f1cf72540ff6f4651dafb7825eb5240fb8b3e100ff6.jpg)

![](images/e3d15390712eea0c9f980d793e54b8f4b0752132f79a9bf1122025ac84bc6de4.jpg)

![](images/cfb734fc58ad5bf87ee8893585634d22ea8533638f8b7d5a3905adcd834d39f1.jpg)

![](images/c3d4bd4085433b87412098b3bd2cda47fb1a2a69c6f634296310cfaf39e49b5e.jpg)

![](images/aedbc588f89fac19621d9d02386cf9219bdc8e0a01a5f064cfa352482bfd3f56.jpg)

![](images/b7716b969fdf0acca203d7f4cf8ac6107e9574f79fe9e476573caf89d8dc69bb.jpg)

![](images/13b90e5c65f76e8a7e9509e14f3d707585810de793d82bdd6de6da4700106ad3.jpg)  
FIG. 12: $^ { 1 6 }$ O: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/bf8661e5ee44c826b3484be941338aff1d38d622661f9ebeac643331fae29ea0.jpg)

![](images/e4c6192f2c23b076bae092e2989719e95587c26cf86a988fe7c7b1df400e8f1a.jpg)

![](images/6691bd973832472c876a0cc05869fe2064b82a4644458d94d9509ebdb870aab1.jpg)  
No $^ { 1 8 }$ O neutron analyzing powers were available

![](images/13c4f68c10b5159d2468c6c3114cef51d93c97a0f51976a7ac47cdebf5753cfd.jpg)

![](images/5b0a6d636b8beb9efc7e1ffe5cafd6fa48b63a8039d3c5de2a104f62137591e0.jpg)

![](images/20946918556e2cc87f090fdbbf61f0638d274f988b347cffd7d6abb518982ab9.jpg)

![](images/5fb42ee97a5ca44953ff919f3caf6833cc7552b2fed96a350dfdd70cac235687.jpg)

![](images/781c4a026f92a4ddad655ae7b88c1bd91568dc5fbd22609a0325f420632081e7.jpg)

![](images/fba21acaaebf467186b9f4bc4b5a5997ed5983b9fae2900e77e34929ddf1be90.jpg)  
FIG. 13: $^ { 1 8 }$ O: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/770d66fb17d45fb9d1340fedc8ec5ad9c7dd4e5361be53ff6c28555e390abf82.jpg)

![](images/352a0b48bb696701ca68e018bc6acc557d473a09e92632e4a1a95b47abf51d58.jpg)

![](images/6351c21b7d35b6a7af177bb58d944b982147cb2b1772889c4406042403183ddb.jpg)

![](images/cb8bebd3443db07a425a8ccdf02877560a80c14781a848aaa29ebf0bc000fed7.jpg)

![](images/44a21513ae7ca8d61e3669d6e23c2800f1cb59249a674083cee8d375362dcbdd.jpg)

![](images/4e0d01c3556c823ed7309717cafb76a9d15e3c9f0617fe4f9e26c8740166f778.jpg)

![](images/57865926e6d4764160769bdc98daf3f06f8ca62cc90691609ae241640260354d.jpg)

![](images/4d5fb78e531efad856c69848d490998d4d8be5499590728ca3ebf3fb05269f9f.jpg)

![](images/c5e508b299a432ca575e60543916369e8afa193e06c443ba5705dcc5ba91a206.jpg)

![](images/e2af3b45f8f9559aea4ba27aa0d4294535973986ec8696c652d60327116bdaf8.jpg)  
FIG. 14: $^ { 4 0 }$ Ca: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/096b39f41feb1dda1a13ee153830349333779cd048e37bd7e5195462cfbf4f0a.jpg)

![](images/5c04a1186ca9908e62a1418f079b1889bbc70b472b8f4d6b44a0addfac4954c8.jpg)

![](images/032cf613dd02b26052f8b55a5f0af56a94ed627d4f72b22985aa43b3708eb642.jpg)  
No $^ { 4 8 }$ Ca neutron analyzing powers were available

![](images/8fac4a08a09c47ef35b3f5b80a26d4d6a2dbf1101613ffc3d11d0f92ecd35d8e.jpg)

![](images/b4dea32737d89b075469bfc07d7092350ee86fedfaa771ae9fa235887be20457.jpg)

![](images/237d5a9a27eaa57735d23b97c42eb88b1399b383b25770de18d9b0311f9e8419.jpg)

![](images/1c6e0e7e4199815e38a54a4f9bd78d8d727414b94e1ac52131fa481b94776456.jpg)

![](images/630ab354820830a57b165e9dba0345ce73f16548c84ffa2afc34e537586f225c.jpg)

![](images/8f338e35059d07a16c881e3ad7e5e7eb454605cd43dab1bd2b982d2c5d61edcd.jpg)  
FIG. 15: $^ { 4 8 }$ Ca: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/bf08cdb4bcc095ddd31b56beb0b51baae2c7f20337687becdf9716383cfc0f31.jpg)

![](images/cf1275fffc7960c330984df49c2ba6ad7d9f18da3cfee54b68f8a4ee5b957634.jpg)

![](images/00f589001442d1abbfeb0f1ef5d26574ec4237fee10d980d72c934afb8fa366d.jpg)

![](images/26a05d988485c76c11d409509222912254b1e3596eb0df808f029326da112248.jpg)

![](images/2724fc2965a94479d66f11ceb81be7ebde468bd5fb61cfd2f1fa841267fee126.jpg)

![](images/64d8b064021e7681aac28fdf9763861b8a4ca186ecafa0ab088505fab3192e8d.jpg)

![](images/186d98037e0a293daeb776056c5589481fc01725387291af330e5daaaad82505.jpg)

![](images/eb1f39b4d55d714049748922e9609c5b4c6dd9ae9c46ecc92033571bcf81a13a.jpg)

![](images/e8ecafa8e9fab8be93750d0c9fb72047cb0721f1e639fd2b0ca61c3be1ab80cf.jpg)

![](images/7c18874b8f461bd3dd3f89b50d0f7fbd1a43e6bdc4070e8b7626efe69cd2d416.jpg)  
FIG. 16: $^ { 5 8 }$ Ni: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/2162fc3ba06071141621900ac202fed9e5ac46f02cd559c7b99f392c2dac07b7.jpg)

![](images/c73f09f5c14068af0a53b23d16239a872bc8f0f648901aa2a2c770089f5e525e.jpg)

![](images/253a19e367b5e04e32fb8ec4600d62d98336cc2f4799f83eee87ade35880a538.jpg)  
No $^ { 6 4 }$ Ni neutron analyzing powers were available

![](images/c0f643f0b4a23b311abce5f62a4280392b424fed3a88a98fac9d3442b408930b.jpg)

![](images/216a78cd53546df44076ea936847f214139f83029f4599312119573bb9d6fcfb.jpg)

![](images/c2ecd9f3f0daabcd1e3c5e0bb4e1c62289d72754581aad04339c572b2b3e5971.jpg)

![](images/b5502147071d626c7486673a9cd2a1a54800b5237a99205c78dd5324481ac666.jpg)

![](images/8a872f65391e10c6b9ff5a5566a0727d49801e6f84d31906040588e4550a4874.jpg)

![](images/691e50ae1f5f58a3f361b6c05b6dbaf6a3be4dcb7542be3920773e4282c553ec.jpg)  
FIG. 17: $^ { 6 4 }$ Ni: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/8f711b0dde430bdedefdbb10a8e7fc78985b5dcf4b3159632d254974ddc5b3f1.jpg)

![](images/14156d5db0c229ecfefb27c5600e923e8ff6843045c1bc254f254b976ca7067f.jpg)

![](images/14cfd18e0c937b381f09b53a6b1c4380d0481f91945c221147fdf13be1ff7ada.jpg)

![](images/a9b4cc7d829138608df37d422acbb448177a5cba662b695f5dcb89f3ea815493.jpg)

![](images/fbdffdf0540063815a94fb9a50b57c34ded003f505cba7375b4ddb072da391ea.jpg)

![](images/bfe26ea06f9a2d6fca2fcd94fc330cf6757d073a2633ce875e0f7a4561160c28.jpg)

![](images/5dfb192da3e1356a08f25479679688884148b786c0a7e5c5d9f1c3b0d4a53ac0.jpg)

![](images/214a299f4b0431e015d323569044d90ecfeed7175777246660896dfb497cd3ed.jpg)  
FIG. 18: $^ { 1 1 2 }$ Sn: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/b3eabd6eae88562e4a0de6277c64c8286af31c1a4e542434ef89a8ebe0cdc48e.jpg)

![](images/4ebb4edf1cde6cf6af7953acf01d88d1b38b47fb99f25da37d889d43b9b88d28.jpg)

![](images/42fd60aaddbeeac24a42ca6bb38748e1b3a16b1d3922ecd8b6858a0319e9e37d.jpg)  
No $^ { 1 2 4 }$ Sn neutron analyzing powers were available

![](images/ae1f5b0708876d3bde9291d8c2712db7d8ac976d44b9af9f3178007c02914910.jpg)

![](images/812248c657ba8d24fb9a248cdf5ab973e46ab8292ceb9907751246742e452187.jpg)

![](images/0799fa12e2d4b69aa5537f97af6e2f76586355f818ab4637953ffb9006cdf6d6.jpg)

![](images/c4d67d5ba6d4e1b8d9a55e137aea3da6cd2c6a0a388e0e2bb64a5c1b01d5a50c.jpg)

![](images/1f1b363988ebf79cc777dd45d8614947163288c5c3acef7dc010ca75ba4ff1fd.jpg)

![](images/ab7daa3d664c1e17e251012cbb048fbb15b8d7aec871fd6a7ee3c18cbdfe1941.jpg)  
FIG. 19: $^ { 1 2 4 }$ Sn: constraining experimental data and DOM fit. See introduction of Appendix C for description.

![](images/5ce2ba48a60ac825ac6709893c071448fd18d4f3b0d71d42d80dc5bb22b54e2c.jpg)

![](images/b01088f3c5529fde1fe3a7029a23192e43cd1d25ba8391e272b54db8c19f8801.jpg)

![](images/ed5a0d968124a1983b659cac070ae645a51dff5f6689ec8ca53d5cf80d84cb62.jpg)

![](images/f96326e83454e10300895eaa073549af103fa84ba855d72f7b28701693b70913.jpg)

![](images/a8dc3b11653a5fb09cbaed529f7bb50bf4ae689f745e3995b6a39740431f2e03.jpg)

![](images/63fcfa8bf7b1817d050fedabd6464a77d0eed14aa0de09695a0b67116d55e2b2.jpg)

![](images/976a863427a7f7037931d8de50e4a3c56dcf308bb629ca5068ecc87a5d9a9364.jpg)

![](images/b83f9e1aea967d770b3c0cc7c6f421de1f76b7f58022ed6f72442d927ae4050d.jpg)

![](images/d7a2fc65851a7a43f376c6369adf72cd4550f0e8863ca9c10b4e97a6e9c15283.jpg)

![](images/066e1a52d6d976861a2eb6c9c898ff28af72303f77e2084d8362f98f13f203f2.jpg)  
FIG. 20: $^ { 2 0 8 }$ Pb: constraining experimental data and DOM fit. See introduction of Appendix C for description.