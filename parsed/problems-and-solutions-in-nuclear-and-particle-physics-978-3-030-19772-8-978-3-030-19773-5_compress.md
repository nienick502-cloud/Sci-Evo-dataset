Sergio Petrera

# Problems and Solutions in Nuclear and Particle Physics

# UNITEXT for Physics

# Series Editors

Michele Cini, University of Rome Tor Vergata, Roma, Italy Attilio Ferrari, University of Turin, Turin, Italy Stefano Forte, University of Milan, Milan, Italy Guido Montagna, University of Pavia, Pavia, Italy Oreste Nicrosini, University of Pavia, Pavia, Italy Luca Peliti, University of Napoli, Naples, Italy Alberto Rotondi, Pavia, Italy Paolo Biscari, Politecnico di Milano, Milan, Italy Nicola Manini, University of Milan, Milan, Italy Morten Hjorth-Jensen, University of Oslo, Oslo, Norway

UNITEXT for Physics series, formerly UNITEXT Collana di Fisica e Astronomia, publishes textbooks and monographs in Physics and Astronomy, mainly in English language, characterized of a didactic style and comprehensiveness. The books published in UNITEXT for Physics series are addressed to graduate and advanced graduate students, but also to scientists and researchers as important resources for their education, knowledge and teaching.

More information about this series at http://www.springer.com/series/13351

Sergio Petrera

# Problems and Solutions in Nuclear and Particle Physics

ISSN 2198-7882

ISSN 2198-7890 (electronic)

UNITEXT for Physics

ISBN 978-3-030-19772-8

ISBN 978-3-030-19773-5 (eBook)

https://doi.org/10.1007/978-3-030-19773-5

# $©$ Springer Nature Switzerland AG 2019

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Switzerland AG The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland

# Preface

“The reader who has read the book but cannot do the exercises has learned nothing.” I used this quote by J. J. Sakurai [1] at each and every first lesson of my courses on nuclear and particle physics. In my message to the students, the “book” in the quote represented the course they were attending. In this way, I wanted to place special emphasis on the importance of exercises in such introductory courses. There are several good textbooks that I used as the basis of my courses and that I have proposed to my students, yet the exercises proposed therein are only partly solved or simply sketched. For this reason, I used to tell my students that even if they missed some lessons, they should follow closely the lessons dedicated to working out problems.

This book contains a sample of about 140 solved problems on nuclear and particle physics. These problems have been used in partial and final examinations of courses I have given for about twenty years, mostly to undergraduates in the University of L’Aquila. In these lecture notes, the solutions are explained in detail and different approaches are proposed and sometimes compared. Another feature of the exercises originates from the decision to consider only realistic cases, to have solutions as close as possible to what is available from actual measurements. Whenever possible, some problems are based on well-known experiments to show that even with their basic knowledge students can understand the main outcomes of these researches.

The exercises are grouped by different subjects. This grouping criterion is not (and cannot be) rigorous because a generic exercise needs inputs from different topics. Therefore, the exercises included in each chapter refer to it only because this is the prevalent subject. The levels of the exercises and the required skills to solve them can be very different. Most of the exercises do not require too much mathematics. Yet, some of the exercises are more difficult and complex and serve as prototypes for a class of problems, so that others of the same class can be solved promptly.

Apart from the use of this book as a supplement to textbooks on nuclear and particle physics for undergraduate classes, it can provide a valid aid to graduate students preparing for selection examinations.

L’Aquila, Italy

April 2019

Sergio Petrera

# Acknowledgements

Several young collaborators helped me to prepare and check the problems along the courses I have given. I wish to thank all of them and, in particular, Eugenio Scapparone and Francesco Salamida. I also would like to thank Celina Paul for her help with the English language.

# Contents

# 1 Nuclear Physics . 1

1.1 Initial Problems 1   
1.2 Nuclear Scattering 2   
1.3 Nuclear Binding Energy 5   
1.4 Nuclear Decays 8   
1.5 Nuclear Models 10

References 12

# 2 Particle Physics . 13

2.1 Fundamental Interactions. 13   
2.2 Hadrons . 15   
2.3 Weak and Electro-Weak Interactions . 19

References 21

# 3 Experiments and Detection Methods . 23

3.1 Kinematics . 23  
3.2 Interaction of Radiation with Matter 29   
3.3 Detection Techniques and Experimental Methods . 33

References 41

# Appendix: Solutions of Exercises and Problems . 43

# Notes

# Data

Each problem can be taken as stand-alone. This means that all input data are provided in the text: For example, the relevant particle masses are usually given in the text. The reader may notice that their accuracies can change on a case-by-case basis. This feature is a consequence of the origin of the text, since these problems were used for examinations and I preferred to give all the needed input data at the accuracy required for each specific case. On the other hand, it also allows the reader to pick up problems randomly without requiring a sequential reading.

The problems are mainly numerical and require values of physical constants, especially for conversion purposes. Whenever these values are not reported in the text, the reader can refer to the PDG Review of Particle Physics [2] which provides an up-to-date collection of constants, units, atomic, and nuclear properties. This review is much more than a simple collection and can be considered as a “must” for dealing with any nuclear and particle physics case.

Nuclear physics data are available from several sources. Some examples are the National Nuclear Data Center (NNDC) at Brookhaven National Laboratory [3] and the IAEA Nuclear Data Section [4].

#

We use the International System of Units (SI), except for energy, mass, and momentum which are specified in terms of eV. This mixed system can be easily handled and the system-specific electromagnetic constants disappear promptly, using the SI definition of the fine structure constant $\mathscr { X }$ and the value of hc in mixed units.

In nuclear physics, kinematical expressions are mostly non-relativistic. In particle physics, the relativistic treatment is instead mandatory. As adopted in many

books, in all kinematical expressions $c$ is omitted (i.e., $c = 1$ ), making them simpler to be handled. Once the energy scale of the problem is set, e.g., GeV, the right units are easily restored with the rule that momenta, energies, and masses are finally given in $\mathrm { G e V } / c$ , GeV, and $\mathrm { G e V } / c ^ { 2 }$ respectively. For all the other quantities (e.g., velocity, time, distance, etc.), the light velocity $c$ is kept in the equations.

# Other References

There are several excellent books that deal with either nuclear or particle physics. Less frequently does one see textbooks presenting these two areas of physics in a unified manner, especially at the undergraduate level. The books Nuclear and Particle Physics by W. S. C. Williams [5], Particles and Nuclei by B. Povh et al. [6], Nuclear and Particle Physics by B. R. Martin [7], and Introduction to Nuclear and Particle Physics by A. Das and T. Ferbel [8] provide the kind of combined exposition more appropriate to the level of the problems proposed here. Finally, a very useful collection of solved problems, including also different topics, is Problems and Solutions on Atomic, Nuclear and Particle Physics by Yung-Kuo Lim [9].

Abstract This chapter is dedicated to Nuclear Physics. After a few very simple problems, it addresses nuclear scattering, the binding energy of nuclei, nuclear decays and nuclear models. Most of the formulas used here are based on the book by Williams (Nuclear and Particle Physics. Clarendon Press, Oxford, 1991) [1], but sometimes the expressions from other books are preferred, when they lead to simpler solutions. In fact, some parametric formulas, e.g. the nuclear radius dependence on the mass number, the semi-empirical mass formula, etc., can differ from text to text and the associated parameters change accordingly.

# 1.1 Initial Problems

# Exercise 1.1.1

Estimate the nuclear density in $\mathrm { g } / \mathrm { c m } ^ { 3 }$ .

# Exercise 1.1.2

Using only classical electromagnetism, give an estimate of the Coulomb term $( a _ { C } )$ in the semi-empirical mass formula (SEMF).

# Exercise 1.1.3

A neutron star is an astrophysical object with a density similar to the one of a nucleus. Knowing that its typical mass is of the order of one solar mass $( M _ { \odot } = 2 \times 1 0 ^ { 3 0 } \mathrm { k g } )$ ), calculate its radius.

# Exercise 1.1.4

A deuteron gas (a deuteron is a nucleus of deuterium, ${ } _ { 1 } ^ { 2 } \mathrm { H } )$ is heated at temperature $T$ . For which temperature nuclear processes occur? Which is the interaction involved? $[ k _ { B } = 8 . 6 \times 1 0 ^ { - 5 } \mathrm { e V / K } ]$ .

Hint: nuclear interaction is possible if the distance between deuterons is of the order of 1 fm.

# Exercise 1.1.5

A gaseous tritium $( _ { 1 } ^ { 3 } \mathrm { H } )$ target is bombarded with a mono-energetic deuteron $( \mathrm { ^ { 2 } H } )$ beam. The tritium nuclei can be assumed at rest. In the collisions $\alpha$ particles and neutrons are produced, through the reaction

$$
{ } _ { 1 } ^ { 2 } \mathrm { H } + { } _ { 1 } ^ { 3 } \mathrm { H } \rightarrow { } _ { 2 } ^ { 4 } \mathrm { H e } + n
$$

What is the neutron rate (neutrons per sec) in a detector at $\theta = 3 0 ^ { \circ }$ having section $S = 2 0 \thinspace \mathrm { c m } ^ { 2 }$ and distance $R = 3 { \mathrm { m } }$ from the target?

The target thickness is $L \rho = 0 . 2 ~ \mathrm { m g } / \mathrm { c m } ^ { 2 }$ , the differential cross section is $d \sigma / d \Omega ( 3 0 ^ { \circ } ) = 1 3 ~ \mathrm { m b / s r }$ . The beam intensity is $I = 2 \mu \mathrm { A }$ .

# 1.2 Nuclear Scattering

# Exercise 1.2.1

(1) A $5 ~ \mu \mathrm { A }$ electron beam with momentum $7 0 0 ~ \mathrm { M e V / c }$ is incident upon a $^ { 4 0 } \mathrm { C a }$ target thick $0 . 1 2 \ \mathrm { g } / \mathrm { c m } ^ { 2 }$ . A detector having section $2 0 \mathrm { c m } ^ { 2 }$ far $1 \mathrm { m }$ from the target is positioned at $4 0 ^ { \circ }$ with respect to the beam direction to measure the scattered electrons. Assuming that the charge distribution of the nucleus is uniform in a sphere of radius $( 1 . 1 8 \ A ^ { 1 / 3 } \ - 0 . 4 8 )$ fm, calculate the rate of the electrons hitting the detector.

(2) The detector is moved and positioned at $2 5 ^ { \circ }$ , where is the first local maximum of the differential cross section. Here the detector collects about 1400 counts per second. The detector consists in two gas counters in sequence, 1 mm thick each, filled with an $\mathbf { A r / C O } _ { 2 }$ mixture. In this gas the electron energy loss is about 1.4 times the ionization minimum, the density is $1 . 8 \mathrm { m g } / \mathrm { c m } ^ { 3 }$ , the ionization potential is $1 5 \ \mathrm { e V } .$ Assume that about $10 \%$ of the energy deposit is effectively converted into electron-ion pairs. Each detector provides a count even if a single electron reaches the anode, being the probability for the electron to reach the anode $\mathrm { P } \simeq 3 0 \%$ . An event is recorded when the two counters provide signals in coincidence. Estimate the counting rate.

# Exercise 1.2.2

Electrons with energy $1 8 0 \ \mathrm { M e V }$ are elastically scattered by an $^ { 1 9 7 } \mathrm { A u }$ target. The angular distribution has a typical diffractive behaviour with several local maxima and minima. Assuming that the nucleus is a hard uniform sphere, evaluate the number of minima.

# Exercise 1.2.3

In the Geiger and Marsden experiment the scattered $\alpha$ particles were counted observing the light flashes produced in a ZnS detector put in a movable ocular looking at the target. A human is able to count up to a maximum rate of few per second. Assuming that this rate is achieved when the ocular is positioned at $2 0 ^ { \circ }$ , what is the beam

# 1.2 Nuclear Scattering

attenuation needed to extend the measurements down to $1 0 ^ { \circ } \mathrm { ? }$ Using the attenuated beam, what is the mean waiting time between two flashes at $2 0 ^ { \circ } \mathrm { ? }$

# Exercise 1.2.4

An electron beam with momentum $1 0 0 \ \mathrm { M e V / c }$ and intensity $I _ { 0 } = 1 0 ~ \mu \mathrm { A }$ hits a carbon target $1 \ \mathrm { g } / \mathrm { c m } ^ { 2 }$ thick. A detector of section $S = 3 0 \mathrm { c m } ^ { 2 }$ is positioned at $1 5 ^ { \circ } { }$ at a distance $R = 2 { \mathrm { m } }$ from the target. Calculate the rate of scattered electrons.

# Exercise 1.2.5

${ 5 0 0 } \ \mathrm { M e V }$ electrons are elastically scattered through an angle of $1 0 ^ { \circ }$ by Fe nuclei $A = 5 6$ ). Calculate:

– the momentum transfer;   
– the Mott cross section;   
– the differential cross section for a uniform charge distribution.

# Exercise 1.2.6

We aim to repeat the Geiger and Marsden experiment in a science lab. For this purpose the following items are available:

• an ${ } ^ { 2 4 1 } \mathrm { A m }$ source emitting $\alpha$ particles with $5 . 5 \mathrm { M e V }$ kinetic energy;   
a thin gold foil as target $A = 1 9 7$ , $Z = 7 9$ ) having $\rho \Delta l = 0 . 1 \ \mathrm { g } / \mathrm { c m } ^ { 2 }$   
a detector with associated electronics to discriminate and count $\alpha$ particles and a computer to read out data. The detector has a sensitive surface of $1 0 \mathrm { c m } ^ { 2 }$ and can be positioned at different angles, keeping the same distance (1 m) from the target.

To achieve a good measurement of the cross section between $1 0 ^ { \circ }$ and $1 5 0 ^ { \circ } $ we require to count at least $1 0 \alpha / s$ . What is the (minimum) intensity of $\alpha$ particles on target to achieve the required accuracy?

# Exercise 1.2.7

Consider the reaction $p \ + \ _ { 3 } ^ { 7 } \mathrm { L i }  \ _ { 2 } ^ { 4 } \mathrm { H e } \ + \ _ { 2 } ^ { 4 } \mathrm { H e }$ . The binding energies of $^ { 4 } _ { 2 } \mathrm { H e }$ and $_ { 3 } ^ { 7 } \mathrm { L i }$ are $2 8 . 3 \mathrm { M e V }$ and $3 9 . 3 \mathrm { M e V }$ respectively.

– Establish if the reaction is either exothermic $( \mathbf { Q } > 0$ ) or endothermic $( \mathrm { Q } < 0 ) ,$   
– Evaluate the spin-parity of the $_ 3 ^ { 7 } \mathrm { L i }$ nucleus.   
– Assuming the $_ { 3 } ^ { 7 } \mathrm { L i }$ at rest, calculate the minimum proton energy for the reaction to occur.   
– Knowing that the final angular momentum is null, calculate the initial angular momentum of the $( p , \ l _ { 3 } ^ { 7 } \mathrm { L i } )$ system. [The proton parity is $+ ]$ .

# Exercise 1.2.8

Expanding the nuclear form factor in series of $\pmb q ^ { 2 }$ powers, one gets

$$
F \left(\boldsymbol {q} ^ {2}\right) = 1 - \frac {\boldsymbol {q} ^ {2}}{6 \hbar^ {2}} \langle r ^ {2} \rangle + \dots \tag {1.1}
$$

A measurement of the differential cross section of electrons, scattered elastically through $5 ^ { \circ }$ , gives $8 0 \mathrm { m b } / \mathrm { s r }$ for incident electrons with momentum 720 MeV/c upon carbon target.

1. Compare the measured cross section to the Mott formula.   
2. Estimate the nuclear radius from (1.1).

# Exercise 1.2.9

In his paper on Nature in 1932, Chadwick [2] motivates the discovery of the neutron arguing that the ‘penetrating’ neutral particle, obtained bombarding the nucleus of $^ { 9 } \mathrm { { B e } }$ with $\alpha$ particles, cannot be a gamma (as supposed earlier), that is

$$
\alpha + ^ {9} \mathrm {B e} \rightarrow^ {1 3} \mathrm {C} + \gamma , \tag {1.2}
$$

but is instead a neutral particle having approximately the same mass of a proton, the ‘neutron’

$$
\alpha + ^ {9} \mathrm {B e} \rightarrow^ {1 2} \mathrm {C} + n. \tag {1.3}
$$

These particles are studied through their scattering against protons

$$
\gamma (n) + p \rightarrow \gamma (n) + p. \tag {1.4}
$$

Chadwick reports that the scattered protons have $\beta$ not exceeding 0.1.

Show that:

(a) in the case of photons from reaction (1.2), the protons scattered in reaction (1.4) cannot have energies corresponding to the measured velocity, if their energies are of the order of $1 0 \mathrm { M e V } ,$ , as expected from the $\alpha$ energy and the mass difference between initial and final nuclei.   
(b) To have protons with the observed energies, photons in (1.2) should have an energy of ${ \approx } 5 0 \mathrm { \ : M e V } .$ .   
(c) If instead the neutral particles are neutrons as in (1.3), the scattered protons are consistent with the measurements.

# Exercise 1.2.10

To repeat the Geiger and Marsden experiment we use

• an ${ } ^ { 2 4 1 } \mathrm { A m }$ source emitting $\alpha$ particles with $T _ { \alpha } = 5 . 6 4 \mathrm { M e V } ;$   
• a $5 0 \mu \mathrm { m }$ thick gold foil as target $A = 1 9 7$ , $Z = 7 9$ , $\rho = ~ 1 9 . 3 ~ \mathrm { g / c m ^ { 3 } } \mathrm { \ : , }$ );   
a detector of section $0 . 5 \mathrm { c m } ^ { 2 }$ and distance $1 0 \mathrm { { c m } }$ , which is moved at seven different angles to count the scattered $\alpha$ particles.

After one hour of measurements at each angle, we collect the counts reported in the table below.

# 1.3 Nuclear Binding Energy

Calculate the intensity of $\alpha$ particles and its uncertainty.

<table><tr><td>θ</td><td>15°</td><td>25°</td><td>35°</td><td>45°</td><td>55°</td><td>65°</td><td>75°</td></tr><tr><td>counts per hour</td><td>4265</td><td>594</td><td>149</td><td>50</td><td>31</td><td>13</td><td>7</td></tr></table>

# 1.3 Nuclear Binding Energy

# Exercise 1.3.1

Among the radioactive $A = 1 9 7$ isobaes for e nu and $_ { 7 9 } ^ { 1 9 7 } \mathrm { A u }$ able. Which are the expected $^ { 1 9 7 } _ { 7 8 } \mathrm { P t }$ $^ { 1 9 7 } _ { 8 0 } \mathrm { H g }$ $_ { 7 9 } ^ { 1 9 7 } \mathrm { A u ? }$

# Exercise 1.3.2

Thermal neutrons (i.e. neutrons in thermal equilibrium with the medium) can induce the following fission reaction

$$
{ } _ { 9 2 } ^ { 2 3 5 } \mathrm { U } + n \longrightarrow { } _ { 5 7 } ^ { 1 4 8 } \mathrm { L a } + { } _ { 3 5 } ^ { 8 7 } \mathrm { B r } + n
$$

Assuming that the medium temperature is $3 0 0 \mathrm { K }$ , estimate the energy released in the reaction.

# Exercise 1.3.3

Deuterium ${ \textstyle \binom { 2 } { 1 } } \mathrm { H } )$ and tritium $( _ { 1 } ^ { 3 } \mathrm { H } )$ nuclei have binding energies of $2 . 2 3 ~ \mathrm { M e V }$ and $8 . 4 8 \mathrm { M e V }$ respectively. What is mean kinetic energy of the nuclei to bring them at a distance of $1 . 4 \ : \mathrm { f m ^ { 2 } }$ What is the corresponding temperature?

In this thermal condition the following reaction can occur

$$
{ } _ { 1 } ^ { 2 } \mathrm { H } + { } _ { 1 } ^ { 2 } \mathrm { H } \longrightarrow { } _ { 1 } ^ { 3 } \mathrm { H } + p
$$

Calculate the energy release per reaction.

# Exercise 1.3.4

TheSunisacopious source of neutrinos (solar neutrinos).Thefirst observationofthese neutrinos has been achieved in 1978 by R. Davis [3] in the Homestake mine (USA), using a large detector filled with $\mathrm { C } _ { 2 } \mathrm { C l } _ { 4 }$ . The reaction used for the detection is

$$
\nu_ {e} + _ {1 7} ^ {3 7} \mathrm {C l} \rightarrow_ {1 8} ^ {3 7} \mathrm {A r} + e ^ {-}.
$$

Calculate the threshold energy of the reaction.

N.B. - Assume both nuclei in their ground state. The following numerical values are needed for the calculation $M _ { p } - M _ { n } = - 1 . 2 9 3 ~ \mathrm { M e V / c ^ { 2 } }$ , $m _ { e } = 0 . 5 1 1 ~ \mathrm { M e V / c ^ { 2 } }$ and

the Coulomb and asymmetry coefficients appearing in the SEMF, $a _ { C } = 0 . 6 9 7 \mathrm { M e V } ,$ $a _ { A } = 2 3 . 3 \mathrm { M e V } .$ .

# Exercise 1.3.5

Using the semi-empirical mass formula establish if the nucleus $^ { 6 4 } _ { 2 9 } \mathrm { C u }$ can have $\beta ^ { - }$ decay (into $^ { 6 4 } _ { 3 0 } \mathrm { Z n }$ ) and/or $\beta ^ { + }$ decay (into $^ { 6 4 } _ { 2 8 } \mathrm { N i }$ ). Calculate also the maximum energies of the emitted $e ^ { \pm }$ $[ M _ { p } = 9 3 8 . 2 7 2 ~ \mathrm { M e V / c ^ { 2 } }$ , $M _ { n } = 9 3 9 . 5 6 5 ~ \mathrm { M e V / c ^ { 2 } }$ , $m _ { e } = 0 . 5 1 1$ $\mathrm { { M e V } } / \mathrm { { c } } ^ { 2 }$ .]

# Exercise 1.3.6

The most stable nucleus with $A = 1 0 1$ is $_ { 4 4 } ^ { 1 0 1 } \mathrm { R u }$ . Using this knowledge, the semiempirical mass formula and the Coulomb coefficient in this formula, asymmetry $[ M _ { n } - m _ { e } - M _ { p } = 0 . 7 8 2 \ : \mathrm { M e V / c ^ { 2 } }$ , $a _ { C } = 0 . 6 9 7 ~ \mathrm { M e V } ]$ .

Hint: The stability condition can be expressed as a minimum of the atomic mass.

# Exercise 1.3.7

The maximum kinetic energy of the positrons from the $\beta ^ { + }$ decay of $^ { 3 5 } _ { 1 8 } \mathrm { A r }$ is 4.95 MeV. Estimate the Coulomb term $a _ { C }$ as defined in the semi-empirical mass formula. Compare this value with the best-fit value of the SEMF.

$$
\left[ M _ {p} - M _ {n} = - 1. 2 9 3 \mathrm {M e V} / c ^ {2}, m _ {e} = 0. 5 1 1 \mathrm {M e V} / c ^ {2} \right]
$$

# Exercise 1.3.8

Confirm with the SEMF that $_ { 4 3 } ^ { 1 0 0 } \mathrm { T c }$ can transmute to both $_ { 4 4 } ^ { 1 0 0 } \mathrm { R u }$ and $^ { 1 0 0 } _ { 4 2 } \mathrm { M o }$ . Which are the corresponding transitions?

$$
[ M _ {p} = 9 3 8. 2 \tilde {7} 2 \mathrm {M e V / c ^ {2}}, M _ {n} = 9 3 9. 5 6 5 \mathrm {M e V / c ^ {2}}, m _ {e} = 0. 5 1 1 \mathrm {M e V / c ^ {2}} ]
$$

# Exercise 1.3.9

A nuclear reactor produces a total power of 2 GW. The fission reaction involved in the energy production is

$$
{ } _ { 9 2 } ^ { 2 3 5 } \mathrm { U } \rightarrow ( A _ { 1 } , Z ) + ( A _ { 2 } , 9 2 - Z ) + k n + \sim 2 0 0 \mathrm { M e V }
$$

where $k$ is an integer with values 2÷3.

(a) Calculate the number of fission reactions per second.   
(b) Knowing that the fissile nucleus, $^ { 2 3 5 } _ { 9 2 } \mathrm { U }$ , constitutes about $30 \%$ of the total fuel mass, estimate how much of this mass is consumed in a year.

Nuclear reactors are the major source of human-generated neutrinos. Neutrinos are produced in the $\beta ^ { - }$ decay of the neutron-rich uranium fission fragments. This implies that they are actually $\bar { \nu } _ { e }$ . Assuming for simplicity that all neutrinos originate from the decay of $_ { 5 7 } ^ { 1 4 5 } \mathrm { L a }$ (as representative of all possible $\beta ^ { - }$ decays) and the total decay rate corresponds to about $20 \%$ of the total fission rate,

(c) calculate the maximum neutrino energy;   
(d) calculate the neutrino flux at $5 0 0 \mathrm { m }$ from the reactor core.

# 1.3 Nuclear Binding Energy

(e) Knowing that the cross section for the reaction $\bar { \nu } _ { e } + p \to n + e ^ { + }$ at these energies is about $6 \times 1 0 ^ { - 4 4 } \mathrm { c m } ^ { 2 }$ , with an ideal detector of 1 ton active mass placed at $5 0 0 \mathrm { m }$ from the core, how many neutrinos per year are detected?

# Exercise 1.3.10

$^ { 2 7 } _ { 1 4 } \mathrm { S i }$ nuclei decay by $\beta ^ { + }$ -decay into $^ { 2 7 } _ { 1 3 } \mathrm { A l }$ , whose binding energy is 224.95 MeV. The maximum kinetic energy of the emitted positrons is 3.79 MeV.

(a) Calculate the binding energy of the parent nucleus.   
(b) Show that the difference in the binding energies between parent and daughter nuclei depend only on the Coulomb term of the semi-empirical mass formula.   
(c) Estimate the $^ { 2 7 } _ { 1 4 } \mathrm { S i }$ radius, assuming a uniform charge distribution.

# Exercise 1.3.11

The reaction $\nu _ { e } + \ O _ { 3 1 } ^ { 7 1 } \mathrm { G a } \to \ O _ { 3 2 } ^ { 7 1 } \mathrm { G e } + e ^ { - }$ is exploited for the detection of solar neutrinos in Gallium detectors [4, 5]. Knowing that the threshold energy is $2 3 3 \mathrm { k e V }$ and the $^ { 7 1 } _ { 3 1 } \mathrm { G a }$ binding energy is $6 1 8 . 9 5 \mathrm { M e V } ,$ evaluate:

• the $^ { 7 1 } _ { 3 2 } \mathrm { G e }$ binding energy;   
the relative error in the same binding energy, if the semi-empirical mass formula is used instead.

Assume the following numerical value $M _ { n } - M _ { p } - m _ { e } = 7 8 2 \mathrm { k e V } / \mathrm { c } ^ { 2 }$ .

# Exercise 1.3.12

According to certain theories the strengths of fundamental interactions can vary with time (on cosmological scale). For simplicity assume that only the electromagnetic coupling constant changes, the others remaining unchanged. The stablest nucleus for isobars having $\mathbf { A } = 1 3 3$ is nowadays $^ { 1 3 3 } _ { 5 5 } \mathrm { C s }$ . If we assume that in another epoch it is $_ { 5 4 } ^ { 1 3 3 } \mathrm { X e }$ 55  instead, estimate how much the electromagnetic coupling constant should change.

$$
\left[ a _ {C} = 0. 6 9 7 \mathrm {M e V}, a _ {A} = 2 3. 3 \mathrm {M e V}, M _ {n} - M _ {p} - m _ {e} = 0. 7 8 2 \mathrm {M e V} / c ^ {2} \right]
$$

# Exercise 1.3.13

The interaction between photons and nuclei can proceed through the following processes (nuclear photo-disintegration)

$$
\gamma + (A, Z) \rightarrow (A - 1, Z - 1) + p \quad \gamma + (A, Z) \rightarrow (A - 1, Z) + n
$$

In particular consider the photo-disintegration of $^ { 5 6 } _ { 2 6 } \mathrm { F e }$

$$
\gamma + _ {2 6} ^ {5 6} \mathrm {F e} \rightarrow_ {2 6} ^ {5 5} \mathrm {F e} + n. \tag {1.5}
$$

(a) Establish the photon threshold energy for reaction (1.5) in the case of an experiment with a photon beam against an iron fixed target.

(b) The same process (1.5) occurs when very energetic Cosmic Rays produced by an extra-galactic source propagate through the Universe. $^ { 5 6 } _ { 2 6 } \mathrm { F e }$ nuclei involved in this process are ultra-relativistic and the hit photons belong to the Cosmic Microwave Background radiation. This radiation pervades the Universe and can be simplified by an isotropic flux of 1 meV energy photons.

Establish the threshold energy for $^ { 5 6 } _ { 2 6 } \mathrm { F e }$ Cosmic Rays. Consider the case in which the photon direction is equal and opposite to the one of the propagating nuclei (head-on collision).

# Exercise 1.3.14

In nuclear physics, the separation energy is the energy needed to remove one nucleon from a nucleus. It is denoted by $S _ { p }$ for a removed proton and $S _ { n }$ for a neutron.

(a) Derive an expression for $\Delta S = S _ { p } - S _ { n }$ , using the semi-empirical mass formula.   
(b) For light nuclei $\begin{array} { r } { A < 4 0 } \end{array}$ ) the stability line is approximately $A = 2 Z$ : write $\Delta S$ for this assumption and discuss the sign of the obtained expression.   
(c) For heavy nuclei $\mathit { \Pi } _ { M } ^ { ' } > 1 0 0 \mathit { \Pi } _ { , }$ ) the stability line approaches $A = 2 . 5 Z$ : write $\Delta S$ and discuss the sign for this case.   
(d) Calculate $\Delta S$ for the following (stable) nuclei $^ { 2 0 } _ { 1 0 } \mathrm { N e }$ , $^ { 3 8 } _ { 1 8 } \mathrm { A r }$ , $_ { 4 6 } ^ { 1 0 6 } \mathrm { { P d } }$ , $_ { 5 6 } ^ { 1 3 7 } \mathrm { B a }$ and $^ { 2 0 0 } _ { 8 0 } \mathrm { H g }$ , discussing the results.

# 1.4 Nuclear Decays

# Exercise 1.4.1

Consider the $\alpha$ -decay $^ { 2 4 0 } \mathrm { P u }  ^ { 2 3 6 } \mathrm { U } + \alpha$ . Experimentally we observe two lines for the $\alpha$ kinetic energies, at 5.17 and $5 . 1 2 \mathrm { M e V } .$ . Which are the $Q _ { \alpha }$ -values for the two modes? The lower energy line corresponds to the decay from an excited level $^ { 2 3 6 } \mathrm { U ^ { * } }$ . Nucleus de-excites from this level via $\gamma$ -decay. What is the γ energy?

# Exercise 1.4.2

Consider the following decay chain

$$
{ } _ { 9 4 } ^ { 2 4 4 } \mathrm { P u } ( 8 1 \mathrm { M y r } ) \rightarrow { } _ { 9 2 } ^ { 2 4 0 } \mathrm { U } ( 1 4 \mathrm { h } ) \rightarrow { } _ { 9 3 } ^ { 2 4 0 } \mathrm { N p } ( 6 7 \mathrm { m i n } ) \rightarrow { } _ { 9 4 } ^ { 2 4 0 } \mathrm { P u } ,
$$

where half-lives are reported in brackets. Having 1 mol of pure $^ { 2 4 4 } \mathrm { P u }$ , how many ${ } ^ { 2 4 0 } \mathrm { U }$ and $^ { 2 4 0 } \mathrm { N p }$ nuclei will be present after 1 month? Which is the radioactive process involved in each decay? What is the measured activity in the first decay process?

# Exercise 1.4.3

The half life of $^ { 2 2 6 } \mathrm { R a }$ is 1600 years. Assuming to have a pure $1 \mathrm { g }$ source of $^ { 2 2 6 } \mathrm { R a }$ , evaluate its activity.

# Exercise 1.4.4

In dating organic specimens, carbon is usually used. Carbon-14 is a radioactive isotope of carbon that is produced by the action of Cosmic Rays on nitrogen in the atmosphere. If the flux of Cosmic Rays remains roughly constant over time, then the ratio of $_ { 6 } ^ { 1 4 } \mathrm { C }$ to the stable most abundant isotope $_ 6 ^ { 1 2 } \mathrm { C }$ reaches an equilibrium value of about $1 . 3 \times 1 0 ^ { - 1 2 }$ . $_ 6 ^ { 1 4 } \mathrm { C }$ decays by $\beta ^ { - }$ with a half life of 5700 years.

Measuring the activity of a fossil of $5 \mathrm { g }$ mass we get 3600 decays in 2 h. Estimate the age of the fossil.

# Exercise 1.4.5

The activity of $1 \mathrm { g }$ of $^ { 2 2 6 } \mathrm { R a }$ is used to define the unity of activity of 1 Curie (Ci). The half life of $^ { 2 2 6 } \mathrm { R a }$ is 1600 yr. Which is the mass of a $^ { 6 0 } \mathrm { C o }$ source $( T _ { 1 / 2 } = 5 . 2 6$ yr), if we measure an activity of $1 0 \mathrm { C i 2 }$

# Exercise 1.4.6

Consider the following decay chain

• $N _ { 1 }  N _ { 2 }$ , with a decay constant $\omega _ { 1 } = 1 0 \mathrm { s } ^ { - 1 }$   
· $N _ { 2 }  N _ { 3 }$ , with $\omega _ { 2 } = 5 0 \mathrm { s } ^ { - 1 }$ ;   
· $N _ { 3 }$ is stable.

Assume that at time 0 the nuclei of type 1 are $N _ { 0 }$ and none of the other types are present. Find the numbers $N _ { 1 } , N _ { 2 }$ and $N _ { 3 }$ at any time. In particular, find the ratio $N _ { 3 } / N _ { 1 }$ after 1/4 s.

# Exercise 1.4.7

$^ { 2 3 8 } \mathrm { U }$ , the most abundant isotope of natural uranium, originates from the solidification of the Earth’s crust occurred about 2.5 billions of years ago. Knowing that its half life is $4 . 5 \ 1 0 ^ { 9 }$ years, derive

• the fraction of $^ { 2 3 8 } \mathrm { U }$ decayed so far;   
• the specific activity of $^ { 2 3 8 } \mathrm { U }$ in $\mathrm { C i } / \mathrm { g }$

# Exercise 1.4.8

Consider the following radioactive decays

1. $\mathrm { \Delta _ { 2 2 } ^ { 4 4 } T i  \ _ { 2 0 } ^ { 4 0 } C a } + \alpha$   
2. ${ \bf \Lambda } _ { 9 5 } ^ { 2 4 1 } \mathrm { A m }  { \bf \Lambda } _ { 9 3 } ^ { 2 3 7 } \mathrm { N p } + \alpha$   
$^ { 1 4 1 } _ { 5 5 } \mathrm { C s } \to \ { 1 4 1 } \mathrm { B a } + e ^ { + } + \nu _ { e }$   
4. $\mathrm { \Lambda _ { 2 8 } ^ { 6 9 } N i } \to \mathrm { \Lambda _ { 2 9 } ^ { 6 9 } C u } + e ^ { - } + \bar { \nu } _ { e }$

Establish which ones are allowed or forbidden specifying the reason(s) in each case. $[ B _ { \alpha } = 2 8 . 3 \mathrm { M e V }$ , $M _ { p } = 9 3 8 . 2 7 \mathrm { M e V / c } ^ { 2 }$ , $M _ { n } = 9 3 9 . 5 7 \mathrm { M e V / c } ^ { 2 }$ , $m _ { e } = 0 . 5 1 1 \mathrm { \mathrm { M e V / c ^ { 2 } } } ]$ .

# Exercise 1.4.9

Consider the following sequence of decays

$$
{ } _ { 3 8 } ^ { 7 9 } \mathrm { S r } ( 2 . 2 5 \mathrm { m i n } ) \rightarrow { } _ { 3 7 } ^ { 7 9 } \mathrm { R b } ( 2 2 . 9 \mathrm { m i n } ) \rightarrow { } _ { 3 6 } ^ { 7 9 } \mathrm { K r } ( 3 5 \mathrm { h } ) \rightarrow { } _ { 3 5 } ^ { 7 9 } \mathrm { B r }
$$

where half-lives are reported in brackets and the last nucleus is stable.

Find the time at which an initially pure $^ { 7 9 } _ { 3 8 } \mathrm { S r }$ source has the maximum abundance of $^ { 7 9 } _ { 3 7 } \mathrm { R b }$ nuclei.

# Exercise 1.4.10

A concrete basement $( 4 \mathrm { m } \times 5 \mathrm { m } \times 3 \mathrm { m } )$ is not ventilated for long periods. Measuring the $^ { 2 2 2 } \mathrm { R n }$ activity in the volume of the basement we get $1 0 0 ~ \mathrm { B q } / \mathrm { m } ^ { 3 }$ . Knowing that ${ } ^ { 2 2 2 } \mathrm { R n }$ is produced along the $^ { 2 3 8 } \mathrm { U }$ sequential decay chain and this gas diffuses from the walls from a maximum depth of about $2 \mathrm { c m }$ , find the $^ { 2 3 8 } \mathrm { U }$ concentration in the concrete (in number of $^ { 2 3 8 } \mathrm { U }$ nuclei per unit volume). The $^ { 2 3 8 } \mathrm { U }$ half-life is 4.5 billion years.

# Exercise 1.4.11

The half-life of the $^ { 2 3 9 } \mathrm { { P u } }$ decay $( ^ { 2 3 9 } \mathrm { P u }  ^ { 2 3 5 } \mathrm { U } + \alpha )$ has been measured immersing a $1 2 0 \mathrm { g }$ source of $^ { 2 3 9 } \mathrm { { P u } }$ in a liquid nitrogen vessel whose volume is large enough to contain the alpha decays. An evaporation rate of the liquid corresponding to a power of 0.231 W has been measured. Knowing that kinetic energy of alpha particles is $5 . 1 4 4 \mathrm { M e V } ,$ calculate the half-life of $^ { 2 3 9 } \mathrm { { P u } }$ .

[Assume that the time of the measurement is much smaller than the half-life.]

# 1.5 Nuclear Models

# Exercise 1.5.1

In a shell model the ground state energy is calculated using a Saxon-Woods potential, with parameters $( R , d$ and $V _ { 0 }$ ), tuned to fit experimental data. If in Nature the nuclear radius $R$ were larger, e.g. 1.5 times the one found in experiments, all other model parameters being unchanged, discuss what we would expect for the energy of the ground state and the binding energy of the nucleus.

# Exercise 1.5.2

On the basis of the shell model assign spin and parity, $J ^ { P }$ , to the ground states of the following carbon isotopes: $^ { 1 1 } \mathrm { C }$ , $^ { 1 2 } \mathrm { C }$ , $^ { 1 3 } \mathrm { C }$ , $^ { 1 4 } \mathrm { C }$ .

# Exercise 1.5.3

On the basis of the shell model assign spin and parity to the ground states of $^ { 3 3 } _ { 1 6 } \mathrm { S } , _ { 1 9 } ^ { 3 9 } \mathrm { K }$ and $^ { 6 0 } _ { 2 8 } \mathrm { N i }$ .

# Exercise 1.5.4

Using the nuclear Fermi gas model, estimate the mean kinetic energy of nucleons for $_ 8 ^ { 1 6 } \mathrm { O }$ and $^ { 4 0 } _ { 2 0 } \mathrm { C a }$ nuclei.

# Exercise 1.5.5

Using the shell model find $J ^ { P }$ for $_ 7 ^ { 1 5 } \mathrm { N }$ , $^ { 2 7 } _ { 1 2 } \mathrm { M g }$ , $^ { 6 0 } _ { 2 8 } \mathrm { N i }$ and $^ { 8 7 } _ { 3 8 } \mathrm { S r }$ , motivating the results in terms of their shell configurations.

# Exercise 1.5.6

Consider the following oxygen isotopes $_ 8 ^ { 1 5 } \mathrm { O }$ , $_ { 8 } ^ { 1 6 } \mathrm { O }$ and $_ 8 ^ { 1 7 } \mathrm { O }$ in their ground states.

1. Establish if they are stable. In case of decay, identify the possible decay type.   
2. Using the shell model, assign spin and parity and evaluate the magnetic moment.

# Exercise 1.5.7

Assign spin and parity to $_ 3 ^ { 7 } \mathrm { L i }$ and $^ { 2 9 } _ { 1 4 } \mathrm { S i }$ ground states using

(a) the standard shell model;   
(b) a shell model with direct spin-orbit interaction, that is having a positive term multiplying L S.

# Exercise 1.5.8

In the context of the shell model find the shell configurations and assign (whenever possible) spin and parity to the ground states of $^ { 5 1 } _ { 2 4 } \mathrm { C r }$ , $^ { 5 2 } _ { 2 4 } \mathrm { C r }$ and $^ { 5 5 } _ { 2 4 } \mathrm { C r }$ .

$^ { 5 2 } \mathrm { C r }$ is stable. Identify the possible decays of the other isotopes.

# Exercise 1.5.9

The copper isotope $^ { 5 7 } _ { 2 9 } \mathrm { C u } _ { 2 8 }$ decays by $\beta ^ { + }$ to $^ { 5 7 } _ { 2 8 } \mathrm { N i } _ { 2 9 }$ . For both nuclei involved in the decay,

(a) assign spin and parity to ground states and first excited levels;   
(b) find the magnetic moments;   
(c) estimate the maximum energy of the positron emitted in the decay. Show that it is possible to get such estimate without using the semi-empirical mass formula giving the motivation.

$$
[ M _ {p} = 9 3 8. 2 7 \mathrm {M e V / c ^ {2}}, M _ {n} = 9 3 9. 5 7 \mathrm {M e V / c ^ {2}}, m _ {e} = 0. 5 1 1 \mathrm {M e V / c ^ {2}} ]
$$

# Exercise 1.5.10

Assign spin and parity to the following nuclei: $_ 8 ^ { 1 7 } \mathrm { O }$ , $_ { 9 } ^ { 1 8 } \mathrm { F }$ and $^ { 2 0 7 } _ { 8 2 } \mathrm { P b }$

# References

1. Williams, W.S.C.: Nuclear and Particle Physics. Clarendon Press, Oxford (1991)   
2. Chadwick, J.: Possible existence of a neutron. Nature 129, 312 (1932)   
3. Davis Jr., R., Harmer, D.S., Hoffman, K.C.: Search for neutrinos from the sun. Phys. Rev. Lett. 20, 1205 (1968)   
4. Anselmann, P., et al.: [GALLEX Collaboration], Solar neutrinos observed by GALLEX at Gran Sasso. Phys. Lett. B 285, 376 (1992)   
5. Abdurashitov, D.N., et al.: [SAGE Collaboration] Results from SAGE. Phys. Lett. B 328, 234 (1994)

Abstract The problems collected in this chapter deal with Particle Physics from a phenomenological viewpoint. Whenever possible, the problems ask for numerical calculations, even though these are more properly estimates than actual calculations. This is because at introductory level the mathematical techniques are not yet available. In the first section, the general properties of the fundamental interactions are addressed. For this purpose, tools like Feynman diagrams and conservation properties are used. The further two sections are more specific in electro-weak and strong interactions.

# 2.1 Fundamental Interactions

# Exercise 2.1.1

Show the Feynman diagrams at the lowest $\alpha$ order for the following processes

γ γ e+e−   
· $e ^ { + } e ^ { - } \to \mu ^ { + } \mu ^ { - }$   
： $e ^ { + } e ^ { - }  4 \gamma$

# Exercise 2.1.2

The high energy neutrino-nucleon cross section can be written in natural units $\hbar = c = 1$ ) as

$$
\sigma_ {\nu N} = \frac {2 G _ {F} ^ {2} s}{9 \pi},
$$

where $G _ { F }$ is the Fermi constant and $s$ is the square total energy in the CMS. Find the neutrino energy above which the Earth becomes opaque to neutrinos. Assume that the Earth density is $2 . 1 5 ~ \mathrm { g } / \mathrm { c m } ^ { 3 }$ and its radius is $6 0 0 0 { \mathrm { k m } }$ .

# Exercise 2.1.3

Find the boson (or bosons) exchanged in the following processes

• $e ^ { + } + e ^ { - }  \mu ^ { + } + \mu ^ { - }$

• n → p + e− + ¯νe   
• μ− → e− + ¯νe + νμ   
• νe + e− → νe + e−   
• νμ + e− → νμ + e−

# Exercise 2.1.4

Among the following processes, establish which ones are allowed or forbidden and which is the interaction type. Specify the reason(s) in each case.

# Exercise 2.1.5

Among the following reactions, which ones are allowed? which ones are forbidden? Motivate the answers with Feynman diagrams, flavor flow diagrams or conservation principles.

• $e ^ { + } + e ^ { - }  \gamma + \gamma$

π− n K − 

• $\Sigma ^ { + }  n + e ^ { + } + \nu _ { e }$

• $\Sigma ^ { + } \to \Lambda + e ^ { + } + \nu _ { e }$

· $\rho ^ { 0 }  K ^ { + } + K ^ { - }$

νe e− νe e−

$\nu _ { e } + e ^ { - } \to \nu _ { e } + e ^ { - }$

# Exercise 2.1.6

In the following reactions $X$ denotes an unknown particle. Identify the unknown particle, giving the motivation for your choice.

a. $\pi ^ { - } + p  \Sigma ^ { 0 } + X$   
b. $e ^ { + } + n  p + X$   
c. $\Xi ^ { 0 } \to \Lambda + X$

# Exercise 2.1.7

Draw the Feynman diagrams at the lowest order of the following processes:

(a) e+ e− e+ e−   
(b) e+ e− τ + τ −   
(c) $\gamma + \gamma  \gamma + \gamma$   
(d) $p + \bar { p }  W ^ { - } + X$   
(e) $K ^ { 0 }  \pi ^ { + } + \pi ^ { - }$

# Exercise 2.1.8

For each of the following reactions establish whether it is allowed or not. If it is, establish the type of interaction and possibly draw the Feynman diagram. If it is not, specify the reason.

1. μ+ → e+ + γ   
2. e− → νe + γ   
3. p p + K +   
4. $e ^ { + } + e ^ { - }  \gamma$   
5. νμ + p → μ+ + n   
6. νμ + n → μ− + p   
7. $e ^ { + } + n  p + \nu _ { e }$   
8. $e ^ { - } + p  n + \nu _ { e }$   
9. $\pi ^ { + } \to \pi ^ { 0 } + e ^ { + } + \nu _ { e }$   
10. $p + \bar { p }  Z ^ { \cup } + X$

# 2.2 Hadrons

# Exercise 2.2.1

(1) An experiment is performed to study the inclusive $K ^ { 0 }$ production in the reaction

$$
p + p \longrightarrow K ^ {0} + X, \tag {2.1}
$$

where $X$ denotes any particle system (one or more particles).

– What are the values of its characteristic numbers (electric charge $\boldsymbol { Q } , \boldsymbol { B } , \boldsymbol { S } , \ldots ) ^ { \epsilon }$   
– What is the minimum number of particles in X ?   
– Propose a few solutions with known particles.

(2) With reference to the previous experiment, $K ^ { 0 }$ -mesons are detected observing their decays. Knowing that: (a) $\tau ( K _ { S } ^ { 0 } ) = 0 . 8 9 \times 1 0 ^ { - 1 0 } \ s$ , (b) $K ^ { 0 }$ -mesons produced in (2.1) have momenta in the range $1 { \div } 3 \ \mathrm { G e V } / \mathrm { c }$ , (c) the main $K ^ { 0 }$ decay modes are $\pi ^ { + } \pi ^ { - } \left( 6 9 \% \right)$ and $\pi ^ { 0 } \pi ^ { 0 } \left( 3 1 \% \right)$ ,

– Propose and discuss a possible experimental set-up (detector types, sizes, positioning, etc.) aimed to observe reaction (2.1).

# Exercise 2.2.2

Among the following reactions, establish which ones are allowed, motivating the answers

· $K ^ { - } + p  \Omega ^ { - } + K ^ { + } + K ^ { 0 }$   
· $\psi  \pi ^ { + } + \pi ^ { 0 } + \pi ^ { - }$

· $\pi ^ { - } + p  \Sigma ^ { + } + K ^ { - }$   
· $\pi ^ { - } + p  \pi ^ { 0 } + \pi ^ { 0 }$   
• p + p → n + ++ + p + ¯p

# Exercise 2.2.3

Among the following decays, establish which ones are allowed and which are the interactions:

φ ρ0 π 0   
• $\pi ^ { 0 }  e ^ { + } + e ^ { - } + \gamma$   
• $\Xi ^ { - } \to \Sigma ^ { 0 } + \mu ^ { - } + \bar { \nu _ { e } }$   
· $\Sigma ^ { - }  n + \pi ^ { - }$   
· $\Xi ^ { - } \to \pi ^ { 0 } + \pi ^ { - }$

[masses in $\mathrm { M e V } / \mathrm { c } ^ { 2 }$ : $M _ { \phi } = 1 0 2 0$ , $M _ { \rho ^ { 0 } } = 7 6 9$ , $M _ { \pi ^ { - } } = 1 3 9 . 6$ , $M _ { \pi ^ { 0 } } = 1 3 5$ , $M _ { \Xi ^ { - } } =$ 1321, $M _ { \Sigma ^ { 0 } } = 1 1 9 3$ , $M _ { \mu } = 1 0 5 . 6$ , $M _ { \Sigma ^ { - } } = 1 1 9 7$ , $M _ { n } = 9 3 9 . 6 ]$ .

# Exercise 2.2.4

Estimate the cross section $\sigma ( e ^ { + } + e ^ { - } $ hadrons) in nb at CMS energy $\sqrt { s } = 2$ GeV, knowing that the cross section into $\mu ^ { + } + \mu ^ { - }$ in natural units is:

$$
\sigma = \frac {4 \pi \alpha^ {2}}{3 s}
$$

# Exercise 2.2.5

The total decay width of the $J / \psi$ is $\Gamma = 9 1 \mathrm { k e V } .$ What is the mean lifetime? Which interaction is responsible for the decay?

# Exercise 2.2.6

A 12 GeV/c $\pi ^ { + }$ beam is sent to a liquid hydrogen Bubble Chamber. An event is observed exhibiting an interaction with two charged tracks and two neutral vertexes pointing back to the interaction point. The two $\mathrm { V } ^ { 0 } \mathrm { s } ^ { 1 }$ have distances from the primary interaction point $3 7 \mathrm { c m }$ and 11 cm respectively. The measurements for the first $\mathrm { V } ^ { 0 }$ give $p _ { 1 } ^ { + } = 0 . 4 \mathrm { G e V / c }$ , $p _ { 1 } ^ { - } = 1 . 9 \mathrm { G e V } / \mathrm { c }$ and an opening angle $\theta _ { 1 } = 2 4 . 5 ^ { \circ } ( ^ { + } , ^ { - }$ stand for the sign of the particle charge). The second $\mathrm { V } ^ { 0 }$ has $p _ { 2 } ^ { + } = 0 . 7 5 ~ \mathrm { G e V / c }$ , $p _ { 2 } ^ { - } =$ $0 . 2 5 \mathrm { G e V } / \mathrm { c }$ and $\theta _ { 2 } = 2 2 ^ { \circ }$ . The resolution on the invariant mass using the momentum errors is about $5 \%$ .

a. Which are the particles originating the two $\mathrm { V } ^ { 0 } \mathrm { s } ?$ ;   
b. give a possible interpretation of the observed reaction;   
c. evaluate the lifetimes of the two particles.

# 2.2 Hadrons

# Exercise 2.2.7

Among the following reactions, which ones are allowed? which ones are forbidden? Explain why:

a. $\pi ^ { - } + p  K ^ { - } + \Sigma ^ { + }$   
b. $\pi ^ { + } + p  K ^ { 0 } + \Sigma ^ { + }$   
c. $\pi ^ { - } + p  \Xi ^ { - } + K ^ { + } + K ^ { 0 }$   
d. $\Lambda  \Sigma ^ { - } + \pi ^ { + }$   
e. $K ^ { - } + p  K ^ { 0 } + n$   
f. $\pi ^ { + } + p  \Lambda + K ^ { + } + \pi ^ { + }$

# Exercise 2.2.8

The $\Sigma ^ { 0 }$ strange baryon decays, with a mean lifetime $0 . 7 4 ~ 1 0 ^ { - 1 9 } ~ \mathrm { s }$ , as $\Sigma ^ { 0 }  \Lambda + \gamma$ . It is an e.m. decay according to the lifetime value. The charged member of the $\Sigma$ triplet, e.g. $\Sigma ^ { + }$ , decays weakly in $0 . 8 0 ~ 1 0 ^ { - 1 0 } ~ \mathrm { s }$ .

a. Motivate the $\Sigma ^ { 0 }$ e.m. decay (why e.m.? why neither strong nor weak?)   
b. Motivate the $\Sigma ^ { + }$ weak decay (why weak? why neither strong nor e.m.?)   
c. Draw the Feynman graph(s) at the lowest order for the $\Sigma ^ { 0 }$ decay.

[masses: $\Sigma ^ { 0 } = 1 . 1 9 3 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , $\Sigma ^ { + } = 1 . 1 8 9 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ ,  = 1.116 GeV/c2]

# Exercise 2.2.9

The magnetic moment of the $\Lambda$ -baryon has been measured in 1971 using nuclear emulsions [1]. Stacks of emulsion plates were placed at a distance of $1 0 \mathrm { c m }$ from the target where ’s were produced in the reaction

$$
\pi^ {-} + p \rightarrow \Lambda + K ^ {0},
$$

with $\pi ^ { - }$ of $1 \mathrm { G e V / c }$ momentum. In this strong interaction process $\Lambda$ ’s are polarized with $P \approx 1$ along the normal to the scattering plane.

(a) Prove that the normal polarization is a consequence of the parity conservation in strong interactions. (Hint: assume that a component of the spin is in the plane of the reaction and show that it violates parity conservation.)   
A magnetic field $B = 2 0$ Tesla, normal to the  flight path and parallel to the scattering plane, was pulsed at the arrival of each beam burst to the target (see Fig. 2.1). The  magnetic moment precesses about the direction of this magnetic field. Assume that the emulsion stack is positioned at a small angle $( \approx 0 ^ { \circ } )$ with respect to the direction of the pion beam.   
(b) Calculate the fraction of $\Lambda$ -particles decaying before reaching the detector.   
(c) Calculate the precession angle as $\Lambda$ -particles reach the detector.

![](images/4423f8b9a25915a86c03de0f8d3085142fbfe26da04c8647ab4184c446b75331.jpg)  
Fig. 2.1 Precession of the $\Lambda$ magnetic moment in a uniform magnetic field

The $\Lambda$ -decays into $p + \pi ^ { - }$ were observed in the emulsions and the angle $\theta ^ { * }$ of the proton with respect to the direction of the  magnetic moment was derived in the CMS. The $\theta ^ { * }$ distribution is

$$
N \left(\cos \theta^ {*}\right) \propto \left(1 - \alpha \cos \theta^ {*}\right). \tag {2.2}
$$

The decay asymmetry, $f _ { + }$ , is defined as the fractions of protons emitted forward $( \theta ^ { * } \le 9 0 ^ { \circ }$ ).

(d) Assuming $f _ { + } = 0 . 3 2$ , calculate the value of the $\alpha$ -parameter in Eq. (2.2).   
(e) What is the reason the observed asymmetry?

$\begin{array} { r } { [ m _ { \Lambda } = 1 . 1 1 6 \ \mathrm { G e V } / \mathrm { c } ^ { 2 } } \end{array}$ , $\tau _ { \Lambda } = 2 . 6 3 ~ 1 0 ^ { - 1 0 }$ s, $\mu _ { \Lambda } = - 0 . 6 1 ~ \mu _ { N }$ , with $\mu _ { N } = 1$ nuclear magneton $\mathrm { { ( n . m . ) = 3 . 1 5 \ 1 0 ^ { - 1 4 } \ M e V / T } }$ ; $m _ { p } = 0 . 9 3 8 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , $m _ { \pi } = 0 . 1 4 0 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , $m _ { K ^ { 0 } } = 0 . 4 9 7 { \mathrm { G e V / c ^ { 2 } } } ]$

# Exercise 2.2.10

An experiment is done to study of the associated production of strange particles

$$
\pi^ {-} + p \rightarrow \Lambda + K ^ {0}
$$

with a $\pi ^ { - }$ beam of momentum $1 . 5 ~ \mathrm { G e V / c }$ . Outgoing particles are analyzed in a magnetic spectrometer. An event is observed with two neutral vertexes $( \mathbf { V } ^ { 0 } )$ , pointing back to the interaction point in the target, respectively with angles $5 8 ^ { \circ }$ and $2 1 ^ { \circ }$ with respect to the beam direction. The two ${ \bf V } ^ { 0 } { \bf s }$ exhibit the following features:

– The first $\mathrm { V } ^ { 0 }$ is reconstructed unambiguously as a $K ^ { 0 }$ having a momentum 0.52 $\mathrm { G e V } / \mathrm { c }$ ;   
– The second $\mathrm { V } ^ { 0 }$ , $1 0 \ \mathrm { c m }$ far from the target, decays into a positive particle with $p _ { + } = 0 . 9 2 \mathrm { G e V } / \mathrm { c }$ and a negative particle with $p _ { - } = 0 . 2 1 \mathrm { G e V } / \mathrm { c }$ . These particles are emitted at angles $4 ^ { \circ }$ (θ ) and $1 4 ^ { \circ } ~ ( \theta _ { - } )$ respectively with respect to the $\mathrm { V } ^ { 0 }$ direction.

a. Motivate why the second $\mathrm { V } ^ { 0 }$ cannot be a $\Lambda$ decaying as $\Lambda  p + \pi ^ { - }$ (assume that the momentum resolution is $5 \%$ );   
b. if instead the decay is $\Lambda \to p + e ^ { - } + \bar { \nu _ { e } }$ , evaluate the longitudinal momentum of the neutrino (i.e. w.r.t. the direction of the $\Lambda$ );

# 2.2 Hadrons

c. if the particle is actually a $\Lambda$ , calculate the lifetime.

[Particle masses in $\mathrm { G e V } / \mathrm { c } ^ { 2 }$ : $p = 0 . 9 3 8$ , $\pi ^ { - } = 0 . 1 4 0$ ,  = 1.116, K0 = 0.498]

# Exercise 2.2.11

Explain why each of the following particles cannot exist in the framework of the quark model:

(a) A baryon of spin 1.   
(b) An antibaryon of electric charge $+ 2$ .   
(c) A meson with charge $+ 1$ and strangeness $^ { - 1 }$

# Exercise 2.2.12

What are the possible charges in the quark model for:

(a) a meson?   
(b) an antibaryon?

# 2.3 Weak and Electro-Weak Interactions

# Exercise 2.3.1

Calculate the length of an iron target a $3 0 0 \mathrm { G e V }$ neutrino beam must cross in order that $1 / 1 0 ^ { 9 }$ of the neutrinos interact. Assume that the high energy neutrino total crosssection is $\sigma _ { \nu } = 1 0 ^ { - 3 8 } E _ { \nu } ~ \mathrm { c m } ^ { 2 }$ , with $E _ { \nu }$ in $\operatorname { G e V } .$ . The iron density is $\rho _ { \mathrm { F e } } = 7 . 9 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ .

# Exercise 2.3.2

In the decay of $D ^ { 0 } ( = c \bar { u } , M _ { D ^ { 0 } } = 1 8 6 5 \mathrm { M e V / c ^ { 2 } } )$ ), two decay modes have the following measured ratio:

$$
\frac {B R (D ^ {0} \rightarrow K ^ {-} + e ^ {+} + \nu_ {e})}{B R (D ^ {0} \rightarrow \pi^ {-} + e ^ {+} + \nu_ {e})} = 1 1. 3 7 \pm 0. 0 5
$$

Discuss and motivate this experimental result.

Hint: consider both quark mixing and phase space contributions.

# Exercise 2.3.3

Draw the Feynman graphs associated to the following weak decays:

· $\Sigma ^ { - }  n + e ^ { - } + \bar { \nu } _ { e }$   
• $\pi ^ { + } \to \pi ^ { 0 } + e ^ { + } + \nu _ { e }$   
· $\tau ^ { + } \to \pi ^ { + } + \bar { \nu } _ { \tau }$

# Exercise 2.3.4

The neutron mean lifetime is 886 s. Assuming that the Sargent rule holds,

$\diamond$ Estimate the Fermi constant.   
$\diamond$ Estimate the mean lifetime for the $\beta ^ { - }$ decay of the nucleus $^ { 3 5 } _ { 1 6 } S$ , knowing that its decay $Q$ -value is $1 6 8 \ \mathrm { k e V . }$ For the calculation neglect the contributions of the nuclear transition amplitude and the Coulomb term.   
$\diamond$ Establish the nuclear spins of the parent and daughter nuclei in the context of the nuclear shell model.

N.B. The three answers are independent from each other.

# Exercise 2.3.5

The OPERA experiment [2] at Gran Sasso Lab has detected a few events interpreted as charged current (CC) interactions of tau neutrinos. The detector was exposed to a muon neutrino beam, produced at CERN (Long Baseline Neutrino Beam), and having an average energy of $2 0 \mathrm { G e V } .$ The observation of interactions $\nu _ { \tau } \to \tau ^ { - }$ , followed by the decays of the $\tau$ leptons, has been interpreted as evidence of the oscillation in flight $\nu _ { \mu } \to \nu _ { \tau }$ . Using the oscillation parameters obtained in other experiments, the oscillation probability $P ( \nu _ { \mu }  \nu _ { \tau } )$ at this distance and energy is expected to be about $1 . 5 \%$ .

The primary background of this experiment is due to charm production in CC muon neutrino interactions $( \nu _ { \mu }  \mu ^ { - } + c )$ , because the mean lifetimes of charmed hadrons (around $1 0 ^ { - 1 2 } \div 1 0 ^ { - 1 3 }$ s) are comparable to the tau lifetime and they can mimic the tau decay.

1. What is the expected fraction of $\nu _ { \mu }$ CC interactions producing charm to all CC interactions?   
2. What is the signal-to-noise ratio: $( \nu _ { \tau }  \tau ^ { - } ) / ( \nu _ { \mu }  \mu ^ { - } + c ) !$   
3. Show a few possible $\tau ^ { - }$ decay modes and draw the associated Feynman graphs.

# Exercise 2.3.6

The branching ratios of the following $\Sigma ^ { - }$ decays are

$$
\begin{array}{l} B R \left(\Sigma^ {-} \rightarrow n + e ^ {-} + \bar {\nu} _ {e}\right) = 1. 0 2 1 0 ^ {- 3} \\ B R \left(\Sigma^ {-} \rightarrow \Lambda + e ^ {-} + \bar {\nu} _ {e}\right) = 0. 5 7 1 0 ^ {- 4} \\ \end{array}
$$

Draw the Feynman diagrams of these decays and estimate the Cabibbo angle from their ratio.

$$
[ m _ {\Sigma^ {-}} \simeq 1 1 9 7 \mathrm {M e V} / \mathrm {c} ^ {2}, m _ {\Lambda} \simeq 1 1 1 6 \mathrm {M e V} / \mathrm {c} ^ {2}, m _ {n} \simeq 9 4 0 \mathrm {M e V} / \mathrm {c} ^ {2} ]
$$

# Exercise 2.3.7

Consider the following decay rates:

$$
\Gamma (D ^ {+} \to \bar {K} ^ {0} + e ^ {+} + \nu_ {e}) = 7 \times 1 0 ^ {1 0} \mathrm {s} ^ {- 1} \quad \Gamma (\mu^ {+} \to e ^ {+} + \nu_ {e} + \bar {\nu} _ {\mu}) = \frac {1}{2 . 2 \mu \mathrm {s}}
$$

Motivate the ratio between these two values.

$$
[ m _ {D ^ {+}} = 1 8 7 0 \mathrm {M e V} / c ^ {2}, m _ {\tilde {K} ^ {0}} = 4 9 8 \mathrm {M e V} / c ^ {2}, m _ {\mu} = 1 0 6 \mathrm {M e V} / c ^ {2}, m _ {e} = 0. 5 \mathrm {M e V} / c ^ {2} ]
$$

# Exercise 2.3.8

Atmospheric neutrinos are produced by the interaction of cosmic rays in the Earth atmosphere. They emerge from the decays of charged pions, which populate the cascades produced in the atmosphere, and the following decays of muons. What is the expected ratio between muon and electron neutrinos $( \nu _ { \mu } + \bar { \nu } _ { \mu } ) / ( \nu _ { e } + \bar { \nu } _ { e } ) ?$

[For a comprehensive answer one should consider that the bulk of the atmospheric neutrinos have energies between 0.1 and $1 \mathrm { G e V }$ and the mean lifetimes of charged pions and muons are $2 . 6 1 0 ^ { - 8 }$ and $2 . 2 1 0 ^ { - 6 }$ s respectively.]

# Exercise 2.3.9

Consider the decays $\mu ^ { - }  e ^ { - } + \bar { \nu } _ { e } + \nu _ { \mu }$ and $\tau ^ { - } \to e ^ { - } + \bar { \nu } _ { e } + \nu _ { \tau }$ . The branching ratios are $100 \%$ for the former and $18 \%$ for the latter. The muon mean lifetime is 2.2 $\mu \mathrm { s }$ . Calculate the tau mean lifetime.

[Masses: $\mu = 1 0 6 \mathrm { M e V } / \mathrm { c } ^ { 2 }$ , $\tau = 1 7 7 7 \mathrm { { M e V } } / \mathrm { { c } } ^ { 2 } .$ ]

# References

# Chapter 3 Experiments and Detection Methods

![](images/ca1c4df97cd0bb850143325218db2269ffc446ae1e0ff3c89c013f767ae2a9f8.jpg)

Abstract The subject of this chapter is related to experiments and detection methods. It is divided into three sections: relativistic kinematics, passage of particles and radiation through matter and detection techniques and methods. In the first section several problems involving relativistic scattering and decay are proposed. Here we use the relativistic invariant approach (and the formalism) following Relativistic Kinematics, by R. Hagedorn [1]. The interaction of radiation with matter deals with the electromagnetic processes occurring to particles at each experimental site and which also make them detectable. An excellent review of this subject can be found in [2]. In the last section problems address experimental and detection techniques in realistic and actual cases.

# 3.1 Kinematics

# Exercise 3.1.1

An experiment is done to study the $\Sigma ^ { + }$ decay. To this aim the used detector is a “tracker” (i.e., a detector of ionising particles having a high spatial resolution, e.g. a bubble chamber, a drift chamber, etc.). $\Sigma ^ { + }$ -baryons are produced in the reaction

$$
\pi^ {+} + p \rightarrow \Sigma^ {+} + K ^ {+}
$$

$( m _ { \pi } = 0 . 1 3 9 6 ~ \mathrm { G e V / c ^ { 2 } }$ , $m _ { p } = 0 . 9 3 8 3 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , $m _ { \Sigma } = 1 . 1 8 9 ~ \mathrm { G e V / c ^ { 2 } }$ , $m _ { K } = 0 . 4 9 3 7$ $\mathrm { G e V } / \mathrm { c } ^ { 2 } )$ , from a 20 GeV/c $\pi ^ { + }$ beam hitting a thin target. The detector can be simplified as a cylinder, with radius $R$ and length $L$ with the axis coincident to the beam line and placed immediately downstream of the target.

For simplicity let us assume that all $\Sigma ^ { + }$ ’s decay within three times their mean lifetime $\tau _ { \Sigma } = 0 . 7 9 9 \times 1 0 ^ { - 1 0 } \ \mathrm { s } )$ .

1. Is the designed apparatus capable of detecting all the $\Sigma ^ { + }$ ’s produced?   
2. What is the minimum detector length to contain all the $\Sigma ^ { + }$ -decay points?   
3. What is the minimum detector radius to fulfill the same requirement?   
4. Is the designed apparatus capable of detecting all the $K ^ { + }$ ’s produced?

5. If it is not the case, which is the fraction of detectable kaons, assuming that they are produced isotropically in the CMS?

# Exercise 3.1.2

(1) Consider a pion beam with total energy $E _ { \pi }$ impinging on a hydrogen target to produce a resonance having mass $M$ . The resonance fastly decays in two particles with masses $m _ { 1 }$ and $m _ { 2 }$ . Knowing that $M = 2 . 5 8 m _ { 1 }$ and $m _ { 2 }$ is negligible with respect to $m _ { 1 }$ , establish the minimum value of $E _ { \pi }$ to have a maximum production angle for particle 1.   
(2) The produced resonance is $\Delta ( 2 4 2 0 )$ , where the number in brackets stands for the invariant mass in MeV. A possible decay channel, different from the one considered in (1), is $\Delta ( 2 4 2 0 )  \Sigma + K ^ { 1 }$ , with $m _ { \Sigma } = 1 . 1 8 9 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ and $m _ { K } = 0 . 4 9 4 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ . Assume that the beam energy is that determined in (1). If a $\Sigma$ is emitted at an angle of $1 2 0 ^ { \circ }$ in the CMS, (a) what is the corresponding angle in the Laboratory system? (b) what is its momentum?   
(3) An experimental set-up has been designed to detect the $\Sigma$ ’s produced in the above reaction. A detector length of $2 6 \mathrm { c m }$ fulfills the requirement that at least $9 9 \%$ of the $\Sigma$ -decay points are contained in the detector. What is the $\Sigma$ mean lifetime?

# Exercise 3.1.3

A negative pion beam is incident on a proton target to produce the reaction $\pi ^ { - } + p $ $\Lambda + K ^ { 0 }$ .

1. Calculate the minimum pion energy for which the reaction is allowed.   
2. Setting the pion energy at $E _ { \pi } = 2 \mathrm { G e V } ,$ , establish if there is a maximum production angle (in the LS) for the $\Lambda$ -particle.

$$
[ M _ {\pi} = 1 4 0 \mathrm {M e V / c ^ {2}}, M _ {p} = 9 3 8 \mathrm {M e V / c ^ {2}}, M _ {\Lambda} = 1 1 1 6 \mathrm {M e V / c ^ {2}}, M _ {K} = 4 9 8 \mathrm {M e V / c ^ {2}} ]
$$

# Exercise 3.1.4

In a certain experiment neutral particles having energy $1 0 \mathrm { G e V }$ are observed to decay into $\pi ^ { + } + \pi ^ { - }$ . The opening angle distribution exhibits a minimum value of about $5 . 2 ^ { \circ }$ . Calculate the mass of the particle.

# Exercise 3.1.5

In an electron-electron collider two $e ^ { - }$ beams hit each other in opposite directions. The respective beam energies are $E _ { 1 } = 1 2 \mathrm { G e V }$ and $E _ { 2 } = 5 \mathrm { G e V } .$ .

• What is the total CMS energy?   
• What are the electron momenta in the CMS?   
What are the beta and gamma, $\beta _ { \mathrm { C M } }$ and $\gamma _ { \mathrm { { C M } } }$ , of the Lorentz transformation $\mathbf { L } S $ CMS?   
• In a collider with equal beam energies, $E _ { 1 } = E _ { 2 }$ , establish the relation between CMS and LS.

# 3.1 Kinematics

# Exercise 3.1.6

Consider the weak decay $\Xi ^ { 0 } \to \Sigma ^ { + } + e ^ { - } + \bar { \nu _ { e } }$ . Assuming that the $\Xi ^ { 0 }$ -baryon $( M _ { \Xi ^ { 0 } } = 1 3 1 5 ~ \mathrm { M e V / c ^ { 2 } } )$ is at rest, calculate the maximum and minimum energies of the electron.

$$
\left[ M _ {\Sigma^ {+}} = 1 1 8 9 \mathrm {M e V} / \mathrm {c} ^ {2}, M _ {e ^ {-}} = 0. 5 1 1 \mathrm {M e V} / \mathrm {c} ^ {2} \right]
$$

# Exercise 3.1.7

A negative pion beam with momentum $p _ { \pi } = 2 0 \mathrm { G e V } / \mathrm { c }$ is incident on a proton target to produce the reaction

$$
\pi^ {-} + p \rightarrow \Sigma_ {c} ^ {0} + \bar {D} ^ {0}.
$$

Considering a $\bar { D ^ { 0 } }$ produced at the maximum angle in the LS and decaying into $\pi ^ { + } + \pi ^ { - }$ , calculate the minimum opening angle between the two pions.

$$
[ M _ {\pi} = 0. 1 4 \mathrm {G e V / c ^ {2}}, M _ {p} = 0. 9 4 \mathrm {G e V / c ^ {2}}, M _ {D} = 1. 8 6 \mathrm {G e V / c ^ {2}}, M _ {\Sigma} = 2. 4 5 \mathrm {G e V / c ^ {2}} ]
$$

# Exercise 3.1.8

In the study of Ultra High Energy Cosmic Rays (UHE stands for $E _ { \mathrm { C R } } > 1 0 ^ { 1 8 } ~ \mathrm { e V } )$ the following process (called the “GZK effect” [3]) occurs

$$
p + \gamma_ {\mathrm {C M B}} \rightarrow p + \pi^ {0}. \tag {3.1}
$$

This reaction represents the photo-production of pions induced by CR protons as they cross the Universe and interact with the photon background contained therein. These photons, which are usually referred to as Cosmic Microwave Background photons (and are denoted by $\gamma _ { \mathrm { C M B } } .$ ), represent the residual radiation emitted after the Big Bang.

– Show the dependence of the threshold energy of reaction (3.1) as a function of the scattering angle between the proton and the CMB photon.   
– Calculate the minimum energy for a CR proton to make pion photo-production.

Use the following numerical values: $E _ { \gamma _ { \mathrm { C M B } } } = 1 0 ^ { - 3 } \mathrm { ~ e ~ }$ V, $M _ { p } = 0 . 9 4 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , $M _ { \pi } =$ $1 3 5 \mathrm { M e V } / \mathrm { c } ^ { 2 }$ .

# Exercise 3.1.9

Consider the following neutron capture reaction, $n + p  d + \gamma$ , assuming that the initial particles are at rest. From a measurement of the photon energies we get $E _ { \gamma } = 2 . 2 3 0 \pm 0 . 0 0 5 \mathrm { M e V } .$ Calculate the deuteron mass and its error.

$$
[ M _ {p} = 9 3 8. 2 7 2 \mathrm {M e V / c ^ {2}}, M _ {n} = 9 3 9. 5 6 5 \mathrm {M e V / c ^ {2}} ]
$$

# Exercise 3.1.10

1. In the annihilation of anti-protons with momentum $p _ { \bar { p } } = 1 \mathrm { G e V } / \mathrm { c }$ against protons at rest $K ^ { - } K ^ { + }$ pairs are produced. Consider the case of symmetric production (kaons having the same energies), corresponding to kaons emitted at $9 0 ^ { \circ }$ with respect to the anti-proton direction in the center-of-momentum system. What are the momenta and angles of the kaons in the LS?

2. We want to detect the produced kaons using two ionization detectors placed at the angles determined above. Assume that the detectors are $1 0 \mathrm { c m }$ thick and contain a gas with density $\rho _ { \mathrm { \Delta } } = 2 ~ \mathrm { m g } / \mathrm { c m } ^ { 3 }$ and ionization potential $I = 1 5 \mathrm { e V } .$ . If the efficiency for producing electron-ion pairs is $\epsilon _ { p } = 2 0 \%$ and the collection efficiency is $\epsilon _ { c } = 3 0 \%$ , what is the number of pairs collected in each detector?

$$
[ M _ {p} = 0. 9 4 \mathrm {G e V / c ^ {2}}, M _ {K} = 0. 4 9 \mathrm {G e V / c ^ {2}} ]
$$

# Exercise 3.1.11

In a pp experiment an event is observed with two opposite sign muons $( m _ { \mu } =$ $1 0 6 \ \mathrm { M e V } / \mathrm { c } ^ { 2 } ,$ ), emitted along opposite directions, having momenta respectively 45 ${ \bf M e V } / \mathrm { c }$ and $3 0 \mathrm { G e V / c }$ . If these muons are originating from the decay of a particle, what are the momentum and mass of this particle?

# Exercise 3.1.12

Ultra High Energy Cosmic Rays propagating through the Universe undergo the following reaction

$$
p + \gamma_ {\mathrm {C M B}} \rightarrow p + e ^ {+} + e ^ {-}.
$$

This process originates from their collisions against the Cosmic Microwave Background photons $\left( \gamma _ { \mathrm { C M B } } \right)$ . These photons pervade the whole Universe and are distributed isotropically.

Calculate the energy threshold as a function of the scattering angle and determine the angle corresponding to the minimum threshold value. Assume $E _ { \gamma _ { \mathrm { C M B } } } \simeq 1 ~ \mathrm { m e V } .$

# Exercise 3.1.13

In the Large Hadron Collider (LHC) at CERN, Geneva, proton-proton interactions are investigated at the highest energy ever reached by humans. Protons hit each others with opposite momenta so that the laboratory is in the CMS. The current total energy is $1 3 \ \mathrm { T e V } .$ .

(a) Cosmic Rays hitting the Earth are mostly protons having energies between approximately $1 0 ^ { 8 }$ and 1020 eV. What is the energy in eV to produce $p p$ interactions equivalent to the ones studied at LHC?

(b) Which velocity should have an insect $\mathrm { ~ \textit ~ { ~ M ~ } ~ } \approx 0 . 2 5 \mathrm { ~ g ~ }$ ) to have the same kinetic energy of these cosmic rays?

# Exercise 3.1.14

The rapidity is a quantity that is used in high energy hadronic interactions, defined as

$$
y = \frac {1}{2} \ln \frac {E + p _ {\parallel}}{E - p _ {\parallel}},
$$

where $E$ is the particle energy and $p _ { \parallel }$ is the parallel component of its momentum. In the $p p$ scattering at colliders, this component is identified as the projection onto the beam directions in the interaction point.

(a) Show that under Lorentz transformation, the rapidity is only shifted by a quantity that depends on the $\beta$ of the transformation.   
(b) Calculate the maximum and minimum rapidities in the case of LHC ( pp colliding beams at $1 3 \ \mathrm { T e V }$ in the center-of-momentum reference system).   
(c) Show that in the ultra-relativistic limit $E \simeq p )$ ) the rapidity can be approximated by the pseudorapidity, defined as

$$
\eta = - \ln \tan {\frac {\theta}{2}},
$$

where $\theta$ is the particle angle $( p _ { | | } = p \cos \theta )$ .

(d) Compare the rapidities and the pseudorapidities at $9 0 ^ { \circ }$ and $1 ^ { \circ }$ in the LHC case.

# Exercise 3.1.15

The so called “impact parameter” method [4] is used to select particle decays with very short lifetimes. This method is based on the idea that, if the observed event has a track (or more tracks) coming from a secondary decay, the backward prolongation of this track does not point to the vertex of the primary interaction. This method is particularly interesting for those cases in which the track of the decaying particle is too short to be observed. Defining the impact parameter as the distance between the line corresponding to the decay track and the primary vertex, we have $\Delta =$ $L \sin \theta$ where $L$ is the decay distance and $\theta$ is the angle of the particle emitted in the decay (see figure).

P production vertex   
D decay vertex   
Ltrack length

![](images/c57d45517d099bda2617dd6c313271c41ea87a63f9d7375c67540b7a10274aa6.jpg)

Prove that for ultra-relativistic particles (primaries and secondaries), the impact parameter does not depend on the momentum of the decaying particle, which is not the case for the decay length.

(Hint: calculate the expression $\beta \gamma$ $\beta \gamma \sin \theta$ as a function of the $\theta ^ { \star }$ in the CMS.)

In these conditions, we can write that $\Delta = c t$ tan $( \theta ^ { \star } / 2 )$ , where $t$ is the particle lifetime and $\theta ^ { \star }$ is the angle of the emitted particle in the CMS. Consider the $D ^ { + }$ - decay and calculate, for a lifetime equal to the mean lifetime $\tau = 1 . 0 4 \times 1 0 ^ { - 1 2 } \mathrm { s }$ ), the mean impact parameter and the one corresponding to $\theta ^ { \star } = 9 0 ^ { \circ }$ .

# Exercise 3.1.16

In an accelerator experiment two opposite sign muons are interpreted as being due to the decay of a neutral particle. The muons $( \mathrm { m } _ { \mu } = 1 0 6 \mathrm { M e V / c ^ { 2 } } )$ are emitted with an opening angle of $4 2 ^ { \circ }$ and momenta respectively 7.4 and $2 . 6 \ : \mathrm { G e V / c }$ . Calculate the mass and the energy of the neutral particle.

During the same experiment several events are observed with roughly the same energy and decaying particles: calculate the energy of the muons when the opening angle is minimum.

# Exercise 3.1.17

High Energy neutrino beams are produced in proton accelerator sites, injecting almost mono-energetic secondary pion beams (e.g. $\pi ^ { + }$ ) into a long vacuum pipe to allow their decays $( \pi ^ { + }  \mu ^ { + } + \nu _ { \mu } )$ ).

(a) Find the neutrino energy in the pion rest frame (RF).

In the laboratory system the neutrino energy depends on the decay angle. Assume that the pion beam energy is $2 0 0 \mathrm { G e V } .$

(b) What is the maximum neutrino energy in the LS?   
(c) What is the neutrino energy for neutrinos emitted in the forward hemisphere $\mathcal { O } _ { \nu } ^ { * } \le 9 0 ^ { \circ } ,$ ) in the pion RF?   
(d) What is the maximum LS angle for the neutrinos emitted forward in the pion RF?

[Particle masses: $\pi ^ { + } = 0 . 1 4 0 \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , μ+ = 0.106 GeV/c2.]

# Exercise 3.1.18

An astrophysical source at 5000 light-years distance emits neutrons. What is the minimum energy that neutrons must have to reach the Earth?

To make the estimate, assume that neutrons decay after a mean lifetime and the half-life is about $1 0 \mathrm { { m i n } }$ .

# Exercise 3.1.19

The Universe is filled with black-body microwave (CMB, Cosmic Microwave Background) radiation. The average photon energy is $E \approx 1 0 ^ { - 3 }$ eV. Very high energy photons from astrophysical sources make electron-positron pairs in their collisions with CMB photons.

(a) Draw the Feynman graph for this process and evaluate the $\alpha$ order of the cross section.   
(b) What is the minimum photon energy to produce pairs, in the case of head-on collisions?   
(c) For the same case, find the Lorentz factor $\gamma$ of the CMS reference system.

# 3.2 Interaction of Radiation with Matter

# Exercise 3.2.1

The total photon absorption coefficient for $5 \ \mathrm { M e V }$ photons in lead is about 0.04 $\mathrm { c m } ^ { 2 } / \mathrm { g }$ . Knowing that the density is $1 1 . 3 ~ \mathrm { g / c m ^ { 3 } }$ , what is the Pb thickness to halve the intensity of a 5 MeV photon beam? What is the thickness to allow a $5 \%$ beam survival?

# Exercise 3.2.2

The radiation length of lead $\langle A \rangle = 2 0 7$ , $\rho = 1 1 . 3 ~ \mathrm { g / c m ^ { 3 } }$ ) is $5 . 6 \mathrm { m m }$ . What is the absorption coefficient and the cross section for $e ^ { + } e ^ { - }$ pair production from high energy photons?

# Exercise 3.2.3

A $2 0 \mathrm { G e V / c }$ muon crosses a $5 0 \mathrm { c m }$ thick slab of magnetized iron, where a field $B =$ 2 Tesla is produced parallel to the plane of the slab. The initial direction of the muon is normal to the slab. Knowing that the iron radiation length and density are $X _ { 0 } =$ $1 . 8 ~ \mathrm { c m }$ and $\rho = 7 . 8 7 ~ \mathrm { g / c m } ^ { 3 }$ respectively, find the magnetic deflection angle, the momentum at the exit of the slab and the multiple scattering dispersion in the plane containing the muon trajectory.

# Exercise 3.2.4

Find the Compton scattering mean pathlength in water $\langle Z / A \rangle = 0 . 5 6$ ) for $1 \ \mathrm { k e V }$ photons.

# Exercise 3.2.5

A thin X-ray beam is sent to an imaging detector exposed to a magnetic field, $B =$ 0.1 T, uniform and with a direction normal to the beam. A Compton event is identified with an electron ejected at an angle $\phi = 1 0 ^ { \circ }$ , with respect to the beam direction. The electron generates a circular track and leaves the detector at a distance $L = 3 ~ \mathrm { c m }$ from the initial point. A sagitta $s = 0 . 2 \ \mathrm { c m }$ is measured from the electron trajectory. Calculate the energy of the beam and that of the scattered photon.

# Exercise 3.2.6

A $2 0 \mathrm { G e V } \pi ^ { - }$ beam with a current intensity of $1 0 \mu \mathrm { A }$ is monitored by an ionization counter. This counter can be viewed as a gas cell having thickness 1 cm, density 1.8 $1 0 ^ { - 3 } \ : \mathrm { g } / \mathrm { c m } ^ { 3 }$ and mean ionization potential $\langle I \rangle = 1 5 \mathrm { e V } .$ . Assuming that each electronion pair created in the ionization process is actually detected, estimate the current measured in the detector.

# Exercise 3.2.7

An extracted $\pi ^ { + }$ beam contains a minor contamination of protons: both particles have the same momentum $p = 5$ GeV/c. To separate the two beam components two

Cherenkov detectors, having refractive indexes $n _ { \mathrm { 1 } } = 1 . 0 5$ and $n _ { 2 }$ , are placed along the beam line. Find a possible choice for $n _ { 2 }$ to achieve the beam separation.

$$
[ M _ {\pi} = 0. 1 3 9 \mathrm {G e V / c ^ {2}}, M _ {p} = 0. 9 3 8 \mathrm {G e V / c ^ {2}} ]
$$

# Exercise 3.2.8

A $5 0 0 \mathrm { M e V / c }$ muon beam $( { \mathrm { m a s s } } = 0 . 1 0 6 { \mathrm { G e V } } / { \mathrm { c } } ^ { 2 } )$ ) is incident normally on a copper slab $( \rho = 9 \ : \mathrm { g } / \mathrm { c m } ^ { 3 }$ , $X _ { 0 } = 1 . 4 \mathrm { c m }$ ).

(a) Find the thickness needed to stop the beam.   
(b) If instead the slab is $d = 1 0 \ \mathrm { c m }$ thick, calculate the energy and the multiple scattering angle of the muons after the slab.

# Exercise 3.2.9

To study the photoelectric effect a monochromatic UV beam $\lambda = 2 0 0 \mathrm { n m }$ ) is sent to a silver foil. Knowing that the electron binding energy in silver is $W = 4 . 7 3 \mathrm { e V } ,$ establish if the photoelectric process actually occurs and, if so, find the kinetic energy of emitted electrons.

# Exercise 3.2.10

A cosmic photon having energy $1 0 0 \mathrm { G e V }$ interacts with air molecules hitting the Earth atmosphere. Knowing that in air the critical energy is $8 0 \mathrm { M e V }$ and the radiation length is $3 7 \mathrm { g } / \mathrm { c m } ^ { 2 }$ , estimate the thickness of crossed atmosphere (in $\mathrm { g } / \mathrm { c m } ^ { 2 }$ ) where the electromagnetic shower is developed at its maximum.

# Exercise 3.2.11

In the Positron Emission Tomography (PET), the $e ^ { + } e ^ { - }$ annihilation is exploited to produce photons which are detected and measured in the apparatus. The positrons are produced in the organic material where a $\beta ^ { + }$ emitting radionuclide is introduced for this purpose. Subsequently $e ^ { + } e ^ { - }$ annihilate at rest into pairs of photons. Assuming that photons are detected through the Compton scattered electrons, find their minimum and maximum energy.

# Exercise 3.2.12

The Earth’s atmosphere has a total thickness of $1 0 3 0 \mathrm { g } / \mathrm { c m } ^ { 2 }$ at the sea level.

• Estimate the minimum energy for a vertical muon $( m _ { \mu } = 1 0 6 \mathrm { M e V / c ^ { 2 } } )$ ) to cross the whole atmosphere.   
Knowing that the air mean ionization potential is about $1 0 \ \mathrm { e V } ,$ , find the mean number of electrons extracted during the muon path to the ground.

# Exercise 3.2.13

A 1 GeV electron beam crosses normally a lead plate having thickness $X _ { 0 } / 2 0$ , where $X _ { 0 }$ is the lead radiation length. Establish which of the following processes (i) bremsstrahlung, (ii) multiple scattering dominates the angular distribution.

# Exercise 3.2.14

A thin $3 \mathrm { \ G e V }$ muon beam hits a copper slab $1 0 \ \mathrm { c m }$ thick $( \rho = 9 \mathrm { \ g } / \mathrm { c m } ^ { 3 }$ , $X _ { 0 } =$ $1 3 . 3 ~ \mathrm { g } / \mathrm { c m } ^ { 2 }$ ). Evaluate the energy loss and the broadening of the beam produced by multiple scattering.

# Exercise 3.2.15

Explain in few lines, suggesting an example, how the knowledge of the proton range can be used to infer the range of another particle with different charge and mass.

# Exercise 3.2.16

Estimate the mean energy radiated from 1 GeV electrons crossing an aluminium plate $5 \mathrm { c m }$ thick.

$$
[ A = 2 7, Z = 1 3, \rho = 2. 7 \mathrm {g} / \mathrm {c m} ^ {3}, D = 4 N _ {A} \alpha r _ {0} ^ {2} = 1. 4 \times 1 0 ^ {- 3} \mathrm {c m} ^ {2} / \mathrm {g} ]
$$

# Exercise 3.2.17

A muon beam with momentum $p = 5 0 0 ~ \mathrm { M e V / c }$ enters a region with an uniform magnetic field $B = 0 . 1 \ \mathrm { T }$ , orthogonal to the beam direction. Due to the magnetic field the beam is making a curved orbit.

(a) Calculate the radius of the orbit in vacuum.   
(b) Assuming that particles are moving in a gas $( \rho = 2 ~ 1 0 ^ { - 3 } ~ \mathrm { g / c m ^ { 3 } } ,$ ), calculate the radius of curvature after a complete round.

# Exercise 3.2.18

In Compton scattering electrons show a peak in their distribution at a characteristic maximum energy (‘Compton edge’). What is the value of this energy for $0 . 5 ~ \mathrm { M e V }$ photons?

# Exercise 3.2.19

An ionization-sensitive detector, exposed to a $\gamma$ source, measures the energy spectrum shown in the figure.

![](images/b494afbf62adefcd5ab420f0c84d16dca71049d3731f251e55aaacde81be896f.jpg)

The spectrum is produced by Compton scattered electrons that release their kinetic energy in the detector and is interpreted as originated by three $\gamma$ -decay lines whose corresponding ‘Compton edges’ are represented by arrows in the figure. Find the $Q _ { \gamma }$ values for the decays.

# Exercise 3.2.20

High energy muons are produced in extensive air showers as Cosmic Rays hit the Earth atmosphere. Assume for simplicity that all muons have energy $1 0 \mathrm { \ G e V }$ and their production occurs at $1 0 \mathrm { k m }$ a.s.l. Answer the following questions:

(a) knowing that the air refractive index is $n = 1 . 0 0 0 2 9$ , do such muons produce Cherenkov photons?   
(b) if yes, what is the opening angle (w.r.t to the muon direction) of the produced photons?   
(c) how many photons hit the sea level?

# Exercise 3.2.21

A detector is used to measure the energies of photons from a monoenergetic source. The photons are collimated and hit the detector inclined at $3 0 ^ { \circ }$ with respect to the beam, as shown in the figure. The detector measures Compton scattered electrons and consists in a bundle of scintillating fibres (a single fiber is shown in the figure) with a photomultiplier applied to their exit. Assume that the fibre has a thickness $\mathrm { d } = 2 \mathrm { m m }$ , density $\rho = 1 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ , $Z / A \simeq 0 . 5$ and an acceptance of $1 5 ^ { \circ } { }$ . The angular acceptance is meant as the semi-opening angle with respect to the bundle axis for which the electron energy release is fully contained. In the detector a release of 2 MeV is measured as due to the scattered electrons. Calculate:

![](images/5f8a2e89053b378a0a18b3d4e1439724c331a5e4e406588437c1481548d69dc8.jpg)

(a) the beam photon energy;   
(b) the cross section for the electrons accepted by the detector;   
(c) the fraction of detected electrons.

# Exercise 3.2.22

After crossing one radiation length, what is the mean energy lost by 1 GeV electrons?

# 3.3 Detection Techniques and Experimental Methods

# Exercise 3.3.1

Two equal scintillation counters, S1 and S2, 1 cm thick, placed on a beamline at a relative distance $L = 3 ~ \mathrm { m }$ , are used to measure the time-of-flight of crossing particles. All the particles in the beamline have the same momentum $p$ . The scintillator radiation length is $X _ { o } = 4 0 \mathrm { c m }$ .

(1) Show that, in the limit $E \gg m$ , the following relation holds for the difference between the time-of-flights of two particles having square mass difference $\Delta m ^ { 2 } =$ $m _ { 1 } ^ { 2 } - m _ { 2 } ^ { 2 }$

$$
\Delta T = \frac {L}{2 c} \frac {\Delta m ^ {2}}{p ^ {2}},
$$

where $\Delta T = T _ { 2 } - T _ { 1 }$ and $T _ { i }$ is the time-of-flight of particle $i$ .

(2) If this set-up is used to separate $\pi ^ { + }$ $( m _ { \pi } = 1 3 9 \mathrm { M e V / c ^ { 2 } } )$ ) from $K ^ { + }$ $( m _ { K } = 4 9 3$ $\mathrm { M e V } / \mathrm { c } ^ { 2 } )$ in a beamline with $p = 1 \ \mathrm { G e V } / \mathrm { c }$ , what is the time resolution needed to achieve a particle discrimination within 4 standard deviations?   
(3) Assume that S1 and S2 are segmented in parallel strips $5 \mathrm { { c m } }$ wide and a third identical detector S3 is inserted in between S1 and S2 at the same distance from both. A uniform magnetic field of 1 Tesla, normal to the plane of the figure, is set up in the region between S1 and S2. This system is used as a spectrometer to get the momentum from a sagitta measurement.   
(a) Show that the multiple scattering does not affect the measurement.   
(b) Evaluate the momentum resolution $\Delta p / p$ , for 1 GeV/c pions.

![](images/d92e02ba003fe5d1f3ada2ee976c713ef46c9fcd074ad76d9601b5fa045975ee.jpg)

# Exercise 3.3.2

A $3 0 0 \mathrm { M e V / c }$ muon enters a magnetic field region, whose horizontal section is shown in the figure. Assume that the magnetic field is uniform, is normal to the plane of

the figure and has an intensity of 0.5 Tesla. The initial muon direction is normal to the magnetic field direction. At the time $t _ { 0 }$ , when the muon is at O in the figure, the magnetic field is switched on to keep it on a circular orbit of radius $R$ . The medium crossed by the muon in its trajectory has a density $\rho = 1 0 ^ { - 3 } \mathrm { g } / \mathrm { c m } ^ { 3 } .$ . Travelling along its trajectory the muon crosses two $2 \mathrm { m m }$ thick iron septa $( \rho _ { \mathrm { F e } } = 7 . 8 7 ~ \mathrm { g / c m ^ { 3 } } )$ ).

(a) Estimate the difference $\Delta B = B ^ { \prime } ~ - ~ B$ , where $B$ is the magnetic field intensity at the time $t _ { 0 }$ and $B ^ { \prime }$ is the field needed to keep the muon in the circular orbit after one turn.   
(b) If the same apparatus is operated in the vacuum and the iron septa are removed, what is the mean number of turns made by the muon before its decay?

![](images/23bf30862231342d75b4d0ffad6e3e3a1d49fc1d8bb2d611421e143ce0edab8d.jpg)

# Exercise 3.3.3

The SuperKamiokande detector [5] consists in a huge vertical cylinder filled with pure water $\mathit { \Delta } n = 1 . 3 3$ , $\rho = 1 ~ \mathrm { g } / \mathrm { c m } ^ { 3 } .$ ) looked by a grid of photodetectors. Muonic atmospheric neutrinos are detected through the Cherenkov radiation emitted by the muons produced in the neutrino interactions with water nuclei. Assume for simplicity that all muons have a momentum of $1 \mathrm { G e V / c }$ .

1. Estimate the maximum pathlength of the muons.   
2. What is the fraction of this pathlength for which muons emit Cherenkov radiation?   
3. What is the radius of the circle in the bottom of the detector illuminated by the Cherenkov radiation, if a muon is produced at $5 0 ~ \mathrm { c m }$ from the cylinder base, directed downward along its axis (see figure)?

![](images/00c95907b6bdd2dad504e1e1e46a22bbd1810fe511ea7f985dda7c2029e7ee16.jpg)

# Exercise 3.3.4

In a colliding beam accelerator electrons and positrons make interactions (with equal and opposite momenta) at a total energy of $9 0 \mathrm { G e V } .$ An annular detector at a distance of $2 \mathrm { m }$ from the interaction point measures the rate of particles produced in the interaction $e ^ { + } + e ^ { - }  e ^ { + } + e ^ { - }$ . Assume that the detector has internal and external diameters 12 and $2 0 \mathrm { c m }$ respectively and a negligible thickness. The detected rate turns out to be 1 event-per-second. Knowing that the Bhabha cross section at small angles can be written as

$$
\frac {d \sigma}{d \theta} = \frac {8 \pi \alpha^ {2}}{E _ {e} ^ {2}} \frac {(\hbar c) ^ {2}}{\theta^ {3}},
$$

where $E _ { e }$ is the energy of $e ^ { - }$ and $e ^ { + }$ , calculate the collider luminosity.

# Exercise 3.3.5

Theories unificating strong and electro-weak interactions (Grand Unified Theories) predict that nucleons are unstable and decay with a mean lifetime around $1 0 ^ { 3 2 }$ years. Estimate the minimum mass of a nucleon-decay experiment to detect at least one decay per year.

# Exercise 3.3.6

A charged pion beam having momenta ranging between 0.5 and $1 . 5 \mathrm { G e V / c }$ is collimated by a narrow slit $1 \mathrm { c m }$ wide after having crossed a region $1 . 1 \textrm { m }$ long, where a magnet generates a 0.2 Tesla uniform field (see figure). What is the distance between the slit and the end of the magnet to select a momentum $p _ { 0 } = 1 \mathrm { G e V } / \mathrm { c } \pm 5 \%$ $p _ { 0 } = 1$ .

![](images/f2edeaf7363d78805eda2fde451b68bde89da9a2f5527645fcba0366a1af353a.jpg)

# Exercise 3.3.7

A muon beam is circulating in an accumulation ring of $1 4 \mathrm { m }$ radius with a magnetic field of 0.5 Tesla. Knowing that $m _ { \mu } = 1 0 6 \mathrm { M e V / c ^ { 2 } }$ and $\tau _ { \mu } = 2 . 2 ~ \mu \mathrm { s }$ , what are the muon momentum, the revolution period and the fraction of muons lost in a turn?

# Exercise 3.3.8

An experiment is made to search for proton decays as predicted by Grand Unified Theories (GUT). The detector consists of a huge water container of cubic shape where decays can be observed through the Cherenkov radiation emitted by the proton decay products. In particular the search addresses the observation of the ‘golden’ channel

$$
p \to e ^ {+} + \pi^ {0}
$$

Positrons and photons (emitted in the decay $\pi ^ { 0 } \to \gamma \gamma$ ) induce e.m. cascades in the detector and the charged particles contained therein emit Cherenkov photons.

1. Estimate the size of the detector required to fully contain the e.m. cascades.   
2. Assuming that the Cherenkov photon yield in the detection wavelength inter is about $I _ { 0 } = 4 0 0 \mathrm { c m } ^ { - 1 }$ , estimate the total number of photons.

[Water: radiation length $X _ { 0 } \simeq 3 6 \ : \mathrm { g } / \mathrm { c m } ^ { 2 }$ , critical energy $E _ { \mathrm { c } } \simeq 8 0 \ : \mathrm { M e V } ;$ ; proton mass $m _ { p } \simeq 0 . 9 4 ~ \mathrm { G e V } / \mathrm { c } ^ { 2 }$ , positron mass $m _ { e } \simeq 0 . 5 1 1 ~ \mathrm { M e V / c ^ { 2 } }$ , neutral pion mass $m _ { \pi } { } ^ { 0 } \simeq$ $0 . 1 3 5 \mathrm { G e V } / \mathrm { c } ^ { 2 } ]$ ]

Hint: having in mind that the photon opening angle in the $\pi ^ { 0 }$ decay is negligible, the decays appears as two back-to-back cascades.

# Exercise 3.3.9

A $3 0 0 \mathrm { G e V }$ proton beam circulates in an accumulation ring where vacuum is kept at $1 0 ^ { - 1 1 }$ atm. Protons interact against the residual air molecules (assume for air: $Z =$ 7, $A = 1 4$ , $\rho = 1 . 2 5 \times 1 0 ^ { - 3 } ~ \mathrm { g / c m } ^ { 3 }$ in standard atmospheric conditions). Knowing that the total p-Air cross section is about $3 0 0 \mathrm { m b }$ , calculate the mean beam lifetime.

# Exercise 3.3.10

A hadron beam is incident on a lead (density $1 1 . 3 ~ \mathrm { g / c m } ^ { 3 } ,$ ) target $2 \mathrm { m m }$ thick. The beam has a circular section of radius $1 \mathrm { c m }$ . Assuming that the total cross section is $3 0 ~ \mathrm { m b }$ ,

– What is the number of scattering centres within the beam area?   
– What is the fraction of the beam scattered by the target?

# Exercise 3.3.11

The Earth is hit continuously by solar neutrinos (i.e. produced by the Sun). They have an energy spectrum extending up to about 10 MeV. Neutrinos above $4 \mathrm { M e V }$ are detected in a huge detector containing 50,000 tons of water, observing their interaction against atomic electrons. At this energy the $\nu _ { e } e ^ { - }$ cross section is about $7 ~ 1 0 ^ { - 2 0 }$ b and the neutrino flux at the Earth is about $1 0 ^ { 6 } ~ \mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 }$ . Calculate the number of neutrino interactions per year.

# Exercise 3.3.12

Consider cosmic photons of energy $5 0 0 \mathrm { G e V }$ hitting the Earth atmosphere. We use a ground apparatus to detect the electromagnetic showers produced in the atmosphere.

(a) Knowing that in air the critical energy is $E _ { c } ^ { \mathrm { a t m } } = 8 0 ~ \mathrm { M e V }$ and the radiation length is $X _ { 0 } ^ { \mathrm { a t m } } = 3 7 ~ \mathrm { g / c m } ^ { 2 }$ , find the optimal altitude to measure the cascades at their maximum development for vertical photons. [Assume that the vertical grammage (the atmosphere depth in $\mathrm { g } / \mathrm { c m } ^ { 2 } .$ ) depends on altitude as $X _ { \mathrm { v } } ( h ) =$ $X _ { \mathrm { v } } ( 0 ) ~ \exp ( - h / h _ { 0 } )$ $X _ { \mathrm { v } } ( 0 )$ , where con $X _ { \mathrm { v } } ( 0 ) = 1 0 0 0 \ : \mathrm { g } / \mathrm { c m } ^ { 2 }$ and $h _ { 0 } = 7 { \mathrm { k m } } .$ .]   
(b) Assume that the detector is a water tank viewed by optical sensors. Can we exploit the Cherenkov effect to detect the e.m. shower? $[ n _ { H _ { 2 } O } = 1 . 3 3 ]$ 1   
(c) The critical energy in water is almost equal to the one in air. Assume that the water thickness is $5 0 \mathrm { c m }$ , What is the total energy lost by the shower electrons $( e ^ { \pm } )$ crossing the detector? What is their mean pathlength in the detector?

# Exercise 3.3.13

In 1974 a team led by S.C. Ting [6] carried out one of the experiments that demonstrated the existence of particles made of charm quarks. This experiment was run at the Brookhaven National Laboratory using $2 8 \mathrm { \ G e V }$ protons hitting a beryllium target and studying the process

$$
p + \operatorname {B e} \rightarrow e ^ {+} + e ^ {-} + X
$$

where $X$ indicates whatever particle or group of particles not detected. The invariant mass of the system $( e ^ { + } , e ^ { - } )$ , accessible through the identification of $e ^ { + }$ and $e ^ { - }$ and the measurement of their momenta (both absolute value and direction), showed an evident peak at $3 . 1 \mathrm { G e V }$ energy, later interpreted as the production and the consecutive decay of the $J / \psi$ ( cc) neutral meson having mass $\mathrm { m } _ { J } = 3 . 1 \mathrm { G e V } / \mathrm { c } ^ { 2 }$

$$
J / \psi \rightarrow e ^ {+} + e ^ {-}
$$

Consider, for the sake of simplicity, that the observed process is

$$
p + p \rightarrow J / \psi + p + p \tag {3.2}
$$

assuming target protons to be at rest:

1. Calculate the energy threshold for the process (3.2).   
2. As in the experiment, assume proton energy to be $2 8 \mathrm { G e V } .$ Calculate the minimum and maximum production energy for the $J / \psi$ .   
3. Calculate the minimum opening angle of the $e ^ { + } e ^ { - }$ pair.   
4. One of the observed events has an electron with $1 0 \ \mathrm { G e V / c }$ momentum and a positron at $\Delta \theta = 1 6 ^ { \circ }$ . What is the positron momentum such that this pair can originate from the decay of the $J / \psi$ ?

# Exercise 3.3.14

In an $e ^ { + } e ^ { - }$ collider an experiment is carried out to study the tau-lepton production $( m _ { \tau } = 1 7 7 7 \mathrm { { M e V / c ^ { 2 } } } )$ at $2 9 \mathrm { G e V } .$

$$
e ^ {+} + e ^ {-} \rightarrow \tau^ {+} + \tau^ {-}
$$

(a) What is the energy of the τ ’s?   
(b) Estimate the $\tau ^ { + }$ mean lifetime, taking into account that the $\mu ^ { + }$ has a mean lifetime of $2 . 2 ~ \mu \mathrm { s }$ , decays with $100 \%$ branching ratio (BR) as $\mu ^ { + }  e ^ { + } + \nu _ { e } + \bar { \nu } _ { \mu }$ and the BR of the $\tau ^ { + } \to e ^ { + } + \nu _ { e } + \bar { \nu } _ { \tau }$ decay mode is about $18 \%$ .   
(c) The particle detection is performed in a cylindrical detector oriented along the two colliding beams and capable of tracking all charged particles. The detector has an internal radius of $5 \mathrm { c m }$ to host the beam pipe. Is it possible to observe tau decays in this detector?

# Exercise 3.3.15

An electromagnetic calorimeter is calibrated using different particle beams. The calorimeter is a sandwich of lead $\mathbf { ( P b ) }$ and plastic scintillators. It is made up of consecutive stacks of one scintillator and one Pb slab, both 1 cm thick. Beams of 5 GeV electrons, muons and photons are used for calibration.

Determine the mean energy deposited by electrons and muons in the fourth scintillator.   
Compare the results obtained using electron and photon beams. Explain how to discriminate between these two cases.

[Pb: $X _ { 0 } = 0 . 5 6 \mathrm { c m }$ , $\rho = 1 1 \ \mathrm { g } / \mathrm { c m } ^ { 3 }$ - Scintillator: $X _ { 0 } = 4 2 \mathrm { c m }$ , $\rho = 1 . 0 3 ~ \mathrm { g / c m ^ { 3 } } \ ]$

# Exercise 3.3.16

In the years 70’s, a series of experiments were conducted to detect neutrinos and antineutrinos (in large mass neutrino detectors) emerging from thick targets. These experiments were called beam dump experiments [7].

Assume a copper target $A = 6 3 . 5$ , $\rho = 8 . 9 6 \mathrm { g } / \mathrm { c m } ^ { 3 } ,$ ), where an intense $4 0 0 \mathrm { G e V }$ proton beam is dumped on. Emerging neutrinos can be interpreted as originating from the associate production of $c \bar { c }$ pairs, their fragmentation into charmed hadrons

and their subsequent decays via leptonic or semi-leptonic channels (i.e. including neutrinos).

This technique is based upon the fact that all hadrons, produced in the dump, are absorbed but charmed particles, which are able to decay before interacting with the matter.

(a) Assuming that the proton cross-section depends on the target mass number A as

$$
\sigma_ {p A} = \sigma_ {p p} A ^ {\frac {2}{3}}, \tag {3.3}
$$

with $\sigma _ { p p } \simeq 4 0 \ : \mathrm { m b }$ , calculate the $p$ -Cu interaction length.

(b) Assume for simplicity that all associated charm production processes can be represented as

$$
p + p \rightarrow D ^ {+} + D ^ {-} + X, \tag {3.4}
$$

where $X$ stands for any other particles involved in the reaction (3.4). Draw the flavor flow diagrams corresponding to the simplest choice of $X$ .

(c) Which are the simplest leptonic and semi-leptonic decays of $D ^ { \prime } s$ giving rise to neutrinos? Are either neutrinos, $\nu _ { \mu }$ or $\nu _ { e }$ , or antineutrinos, $\bar { \nu } _ { \mu }$ or $\bar { \nu } _ { e }$ , produced from $D ^ { + } ?$ Draw the Feynman graphs for a decay into $\nu _ { \mu }$ and another into $\bar { \nu } _ { e }$ .   
(d) Neutrinos are produced in the beam dump provided that $\lambda _ { \mathrm { d e c } } \ll \lambda _ { \mathrm { i n t } }$ , where $\lambda _ { \mathrm { d e c } }$ is the mean decay pathlength and $\lambda _ { \mathrm { i n t } }$ is the $D ^ { \pm }$ interaction length in Copper. Evaluate if, and for which $D ^ { \pm }$ momenta, this condition is fulfilled in the reaction (3.4). For this purpose, assume that $D ^ { \pm }$ interaction length follows Eq. (3.3), with $\sigma _ { D p } \approx 3 0 \mathrm { m b }$ replacing $\sigma _ { p p }$ . Use also the following values $\mathbf { m } _ { D ^ { \pm } } = 1 . 8 7 \mathbf { G e V } / \mathrm { c } ^ { 2 }$ , $\tau ( \stackrel { \cdot } { D ^ { \pm } } ) = 1 . 0 4 \times 1 0 ^ { - 1 2 } \stackrel { \cdot } { }$ s, $B R ( D ^ { \pm } \to \nu _ { \mu } ) = B R ( D ^ { \pm } \to \nu _ { e } ) = 1 7 \%$ .   
=  ×  → (e) Which is the expectation for the ratio $\frac { \nu _ { \mu } + \bar { \nu } _ { \mu } } { \nu _ { e } + \bar { \nu } _ { e } }$ νe + ¯νe =?

# Exercise 3.3.17

A typical experiment measures neutral pions through the detection of the photons emitted in the decay $\pi ^ { 0 } \to \gamma \gamma$ . Assume that the pion energies are around $1 \mathrm { G e V }$ and that a $1 \mathrm { c m P b }$ plate is used for their conversion to electrons $^ +$ and ), which are measured in a downstream detector. The Pb radiation length is $5 . 6 \mathrm { m m }$ . What is the pion detection efficiency?

Hint:The detection efficiency is the probability that both photons from $\pi ^ { 0 }$ -decays are converted in one or more electrons.

# Exercise 3.3.18

The search for neutrino oscillations [8] is one of the hottest topics in recent years. Assume that the oscillation probability between electron and muon neutrino (or antineutrinos) is

$$
P \left(v _ {e} \rightarrow v _ {\mu}\right) \simeq 0. 2 0 \sin^ {2} \left(1 0 ^ {- 3} \frac {L [ m ]}{E [ M e V ]}\right) \tag {3.5}
$$

where $L$ is the distance between the neutrino production and detection points and $E$ is the neutrino energy.

We aim to study the oscillation phenomenon operating a neutrino detector near a nuclear reactor. The nuclear reactor emits electron antineutrinos through the $\beta ^ { - }$ decays of the radionuclides present in the reactor core at a rate of $1 0 ^ { 1 8 } \ \mathrm { s ^ { - 1 } }$ . The detector has a mass of 1 ton and is located at $2 0 0 \mathrm { m }$ from the reactor core (both the reactor core and the detector can be considered point-like). Assume that the average energy of the antineutrinos from the reactor is $2 \mathrm { M e V }$ and their detection efficiency is $70 \%$ . The total electron antineutrino cross section at $2 \mathrm { M e V }$ is about $2 ~ 1 0 ^ { - 4 3 } ~ \mathrm { c m } ^ { \dot { 2 } }$ .

(a) Which are the possible reactions and the particles that is possible to detect for the two species of antineutrinos $( \bar { \nu } _ { e } , \bar { \nu } _ { \mu } ) ?$ which are the interactions involved?   
(b) If antineutrinos do not oscillate, how many interactions per year are measured?   
(c) If they oscillate following Eq. (3.5), how many interactions per year are measured?   
(d) In the latter case, what is the probability that the oscillation phenomenon is not observed (null result) in one year?

# Exercise 3.3.19

A sequential experimental apparatus is used to analyze a charged particle. In the first part the particle trajectory in a magnetic field $B = 1$ Tesla is found to have a curvature corresponding to a sagitta $s _ { 1 } = 3 \mathrm { c m }$ measured along a track length $l _ { 1 } = 8 0 \mathrm { c m }$ . After passing though a passive medium the same particle is found to have a curvature of radius $R _ { 2 } = 1 2 1 \mathrm { c m }$ in the same field $B$ . In the same region, a time-of-flight system performs a speed measurement which gives $v _ { 2 } = 2 . 8 \times 1 0 ^ { 8 } \mathrm { m / s }$ .

(a) Find the rest mass and kinetic energy of the particle before the slowing down.   
(b) Evaluate the energy lost in the medium.   
(c) The time-of-flight measurement is performed over a basis of $1 4 ~ \mathrm { m }$ . Repeating the same measurement with several equal particles, only $50 \%$ of the particles reach the last counter. Interpreting this loss as being due to the decay of this particle, compute its mean lifetime.

# Exercise 3.3.20

A photon hits the wall of a liquid hydrogen bubble chamber (BC) producing an electron pair as shown in the figure below. The magnetic field $B = 0 . 8 \mathrm { T }$ is perpendicular to the plane of the figure, the density is $\rho = 0 . 0 7 1 \mathrm { g } / \mathrm { c m } ^ { 3 }$ . The electron and positron tracks are detected in the BC as two opposite arcs whose measured diameters are $8 0 ~ \mathrm { c m }$ . The diameters are measured as the distance between the entrance and exit points for each particle.

![](images/3198c9bdfc40bb3ae7994af799a90a16e0361190a02ef8aa79e012d8fc1327f2.jpg)

(a) Find the energy of the photon, neglecting the energy losses in the liquid hydrogen; (b) estimate the same energy, taking into account these losses.

Hint: considering energy losses, at first approximation the track length is the same as in the case of no losses.

# Exercise 3.3.21

Electron antineutrinos from nuclear reactors have typical energies $E _ { \nu }$ of a few MeV (assume a continuous spectrum with a mean value of $2 \mathrm { M e V } _ { \cdot }$ ). They can be detected via the reaction $\bar { \nu } _ { e } + p \to e ^ { + } + n$ in a detector medium containing free protons. The process is observable because of the positron annihilation, $e ^ { + } + e ^ { - }  2 \gamma$ that follows the antineutrino interaction. Assume that the detector is large enough to measure the entire deposit of energy of the gammas. The detector medium (e.g. liquid scintillator) is surrounded by photomultipliers: the total energy, called visible energy $E _ { \mathrm { v i s } }$ , is measured and the neutrino energy is inferred.

(a) What is the dominating process for gamma energy deposit? Which is the characteristic length of the medium which determines if the detector is large enough?   
(b) Estimate the kinetic energy of the recoiling neutron.   
(c) Find the relation between $E _ { \nu }$ and $E _ { v i s }$   
(d) Which is the minimum detectable neutrino energy?

# References

1. Hagedorn, R.: Relativistic Kinematics. Literary Licensing, LLC (2012)   
2. Tanabashi et al., M.: Particle data group. Phys. Rev. D 98, 030001 (2018). http://pdg.lbl.gov/   
3. Greisen, K.: End to the cosmic-ray spectrum? Phys. Rev. Lett. 16 748 (1966); Zatsepin, G.T., Kuzmin, V.A.: Upper limit of the spectrum of cosmic rays. Sov. Phys. JETP Lett. 4, 78 (1966)   
4. Baroni, G., Di Liberto, S., Ginobbi, P., Petrera, S., Romano, G.: An attempt to detect particles of very short lifetimes produced in high-energy neutrino interactions. Lett. Nuovo Cim. 24, 45 (1979)   
5. Fukuda, S., et al.: The Super-Kamiokande detector. Nucl. Instr. Meth. A 501, 418 (2003)   
6. Aubert, J.J., et al.: Experimental observation of a heavy particle J. Phys. Rev. Lett. 33, 1404 (1974)

7. Hansl, T., et al.: Results of a beam dump experiment at the CERN SPS neutrino facility. Phys. Lett. 74B, 139 (1978)   
8. Bettini, A.: Beyond the standard model. In: Introduction to Elementary Particle Physics, pp. 354–385. Cambridge University Press, Cambridge (2008)

# Appendix Solutions of Exercises and Problems

# A.1 Solutions of Nuclear Physics (Chapter 1)

# 1.1 Initial Problems

# Exercise 1.1.1

To give a rough estimate of the nuclear density, we assume that

– the binding energy is negligible;   
– proton and neutron have the same mass, $m _ { p } = m _ { n }$   
– the nuclear radius is $R = r _ { 0 } \cdot A ^ { 1 / 3 }$ , with $r _ { 0 } = 1 . 2 \mathrm { f m }$

Under these assumptions we have

$$
\rho = \frac {M}{V} = \frac {A \cdot m _ {p}}{4 / 3 \pi r _ {0} ^ {3} A} = \frac {3 m _ {p}}{4 \pi r _ {0} ^ {3}} \simeq \frac {3 \times 1 . 6 7 1 0 ^ {- 2 4} \mathrm {g}}{1 2 . 5 6 (1 . 2 1 0 ^ {- 1 3} \mathrm {c m}) ^ {3}} \simeq 2. 3 \cdot 1 0 ^ {1 4} \mathrm {g} / \mathrm {c m} ^ {3}.
$$

# Exercise 1.1.2

The electrostatic energy for a charge $Q$ distributed uniformly in a sphere of radius $R$ is $3 / 5 \cdot Q ^ { 2 } / ( 4 \pi \epsilon _ { 0 } R )$ . Equating this energy to the Coulomb binding energy in the SEMF we get ,

$$
\frac {3 Z ^ {2} e ^ {2}}{2 0 \pi \epsilon_ {0} r _ {0} A ^ {1 / 3}} = a _ {C} \cdot \frac {Z ^ {2}}{A ^ {1 / 3}},
$$

and then

$$
a _ {C} = \frac {3}{5} \times \frac {e ^ {2}}{4 \pi \epsilon_ {0}} \times \frac {1}{r _ {0}} = \frac {3}{5} \times \alpha \hbar c \times \frac {1}{r _ {0}} \simeq 0. 6 \times \frac {1 9 7 \mathrm {M e V f m}}{1 3 7} \times \frac {1}{1 . 2 \mathrm {f m}} \simeq 0. 7 \mathrm {M e V}.
$$

# Exercise 1.1.3

Using the result of problem 1.1.1, we assume for the nuclear density $\rho ~ \simeq ~ 2 . 3 \times$ $1 0 ^ { 1 4 } \mathrm { g } / \mathrm { c m } ^ { 3 }$ . Denoting with $R$ and $M$ respectively the radius and mass of the neutron star, from the relation

$$
\frac {4}{3} \pi R ^ {3} \rho = M \approx M _ {\odot}
$$

we obtain

$$
R \approx \left(\frac {3 M _ {\odot}}{4 \pi \rho}\right) ^ {1 / 3} \simeq \left(\frac {3 \cdot 2 1 0 ^ {3 3} \mathrm {g}}{4 \cdot 3 . 1 4 \cdot 2 . 3 1 0 ^ {1 4} \mathrm {g} / \mathrm {c m} ^ {3}}\right) ^ {1 / 3} \simeq 1 2. 8 \mathrm {k m}.
$$

# Exercise 1.1.4

Let us consider two deuterons moving along a certain direction with equal but opposite velocities (head-on collision). Since the motion is thermal, the kinetic energy of each deuteron can be treated as non-relativistic, $E = 1 / 2 M \nu ^ { 2 }$ , and assumed to be of the order of $k _ { B } T$ .

At large distance, in the rest frame of one of the deuterons, the other has velocity $2 \nu$ . The corresponding kinetic energy equates the repulsive electrostatic energy at the minimum distance, because of energy conservation

$$
\frac {1}{2} M (2 \nu) ^ {2} = 4 E = 4 k _ {B} T = \frac {1}{4 \pi \epsilon_ {0}} \frac {e ^ {2}}{r _ {\mathrm {m i n}}}.
$$

Thus a rough estimate of the minimum temperature to get nuclear processes is

$$
\begin{array}{l} T _ {\mathrm {m i n}} = \frac {e ^ {2}}{4 \pi \epsilon_ {0}} \frac {1}{4 k _ {B} r _ {\mathrm {m i n}}} = \frac {\alpha \hbar c}{4 k _ {B} r _ {\mathrm {m i n}}} \simeq \\ \simeq \frac {1 9 7 \mathrm {M e V} \cdot \mathrm {f m}}{1 3 7 \times 4 \times 8 . 6 1 0 ^ {- 1 1} \mathrm {M e V} \cdot \mathrm {K} ^ {- 1} \times 1 \mathrm {f m}} \simeq 4 1 0 ^ {9} \mathrm {K}. \\ \end{array}
$$

# Exercise 1.1.5

The neutron rate per solid angle is

$$
\frac {d N}{d t d \Omega} = \frac {d \sigma}{d \Omega} \frac {d n _ {\mathrm {b}}}{d t} n _ {\mathrm {T}} L
$$

where $d n _ { \mathrm { b } } / d t = I / e$ is the deuteron beam intensity and $n _ { \mathrm { T } }$ is the number of target nuclei per unit volume, $n _ { \mathrm { T } } = N _ { A } / A \rho .$ . The solid angle between the detector and the interaction region (assumed point-like) is $\Delta \Omega = S / R ^ { 2 }$ . Then we have

$$
\begin{array}{l} \frac {d N}{d t} = \frac {d \sigma}{d \Omega} \frac {S}{R ^ {2}} \frac {I}{e} \frac {N _ {A}}{A} \rho L \simeq \\ 1 3 \mathrm {1 0} ^ {- 3} \mathrm {1 0} ^ {- 2 4} \mathrm {c m} ^ {2} / \mathrm {s r} \frac {2 0}{3 0 0 ^ {2}} \frac {2 \mathrm {1 0} ^ {- 6} \mathrm {A}}{1 . 6 \mathrm {1 0} ^ {- 1 9} \mathrm {C}} \frac {6 \mathrm {1 0} ^ {2 3}}{3} 0. 2 \mathrm {1 0} ^ {- 3} \mathrm {g} / \mathrm {c m} ^ {2} \simeq 1. 4 \mathrm {1 0} ^ {3} \mathrm {s} ^ {- 1} \\ \end{array}
$$

# 1.2 Nuclear Scattering

# Exercise 1.2.1

(1) The rate of electrons scattered in the solid angle $\Delta \Omega$ around the angle $\theta$ , from a beam of intensity $d n _ { \mathrm { b } } / d t$ (e/s) incident perpendicularly on a target with atomic number $A$ , thick $x _ { \mathrm { T } }$ $( \mathrm { g } / \mathrm { c m } ^ { 2 } )$ ), is

$$
\frac {d n}{d t} = \frac {d n _ {\mathrm {b}}}{d t} \times \frac {d n _ {\mathrm {T}}}{d S} \times \int_ {\Delta \Omega} \frac {d \sigma}{d \Omega} d \Omega \simeq \frac {I _ {e}}{e} \times x _ {\mathrm {T}} \frac {N _ {A}}{A} \times \frac {S}{R ^ {2}} \times \frac {d \sigma}{d \Omega} (\theta),
$$

being $\sqrt { S } / R \ll 1$ . Then we have

$$
\begin{array}{l} \frac {d n}{d t} \simeq \frac {5 1 0 ^ {- 6}}{1 . 6 1 0 ^ {- 1 9}} \times \frac {0 . 1 2 \cdot 6 . 0 2 1 0 ^ {2 3}}{4 0} \times \frac {2 0}{1 0 0 ^ {2}} \times \frac {d \sigma}{d \Omega} (\theta) \simeq \\ \simeq 1. 1 3 1 0 ^ {3 2} \frac {\mathrm {s r}}{\mathrm {c m} ^ {2} \cdot \mathrm {s}} \times \frac {d \sigma}{d \Omega} (\theta). \\ \end{array}
$$

$d \sigma / d \Omega ( \theta )$ is given by $| F ( q ^ { 2 } ) | ^ { 2 } \times ( d \sigma / d \Omega ) _ { \mathrm { M o t t } }$ . For $\beta \to 1$ the Mott cross section at $4 0 ^ { \circ }$ is

$$
\begin{array}{l} \left(\frac {d \sigma}{d \Omega}\right) _ {\mathrm {M o t t}} = \frac {Z ^ {2} \alpha^ {2} (\hbar c) ^ {2} \cos^ {2} \theta / 2}{4 (p c) ^ {2} \sin^ {4} \theta / 2} \simeq \left(\frac {2 0 \times 1 9 7}{1 3 7}\right) ^ {2} \\ \times \frac {\cos^ {2} 2 0 ^ {\circ}}{4 \times 7 0 0 ^ {2} \times \sin^ {4} 2 0 ^ {\circ}} \mathrm {f m} ^ {2} / \mathrm {s r} \simeq 0. 2 7 2 \mathrm {m b} / \mathrm {s r} \\ \end{array}
$$

The form factor for a uniform charge distribution in a sphere of radius $R _ { A }$ is

$$
F (q ^ {2}) = 3 \frac {\sin x - x \cos x}{x ^ {3}},
$$

where $\mathit { x } = \mathit { q } \ R _ { A } / \hbar$

$$
\begin{array}{l} x = \frac {2 p c \sin \theta / 2 \times (1 . 1 8 A ^ {1 / 3} - 0 . 4 8) \mathrm {f m}}{\hbar c} \simeq \\ \simeq \frac {2 \times 7 0 0 \mathrm {M e V} \times \sin 2 0 ^ {\circ} \times 3 . 5 6 \mathrm {f m}}{1 9 7 \mathrm {M e V} \mathrm {f m}} \simeq 8. 6 4, \\ \end{array}
$$

Hence we get $F ( q ^ { 2 } ) \simeq 3 . 1 8 1 0 ^ { - 2 }$ and finally obtain

$$
\frac {d n}{d t} \simeq 1. 1 3 1 0 ^ {3 2} \frac {\mathrm {s r}}{\mathrm {c m} ^ {2} \cdot \mathrm {s}} \times 0. 2 7 2 1 0 ^ {- 2 7} \frac {\mathrm {c m} ^ {2}}{\mathrm {s r}} \times (3. 1 8 1 0 ^ {- 2}) ^ {2} \simeq 3 1 \text {e l e c t r o n s / s}.
$$

In Fig. 1.1 the rate of the scattered electrons is shown as a function of the angle.

![](images/fb6d05576bec07c5b0b981c20317deba0eb47122315fbc3431462ff3789638c5.jpg)  
Fig. 1.1 Rate (counts-per-sec) for 700 MeV/c electron scattering against $^ { 4 0 } \mathrm { C }$

(2) As it can be seen in the figure the first local maximum is at about $2 5 ^ { \circ }$ . Here the detector delivers about 1400 counts per second. The mean number of electron-ion pairs produced by an electron crossing the gas mixture is

$$
\begin{array}{l} N _ {e} = \frac {(- d E / d x) _ {\mathrm {i o n}} \times \rho \times d}{W _ {\mathrm {i o n}}} \times \epsilon_ {\mathrm {i o n}} \\ \simeq \frac {1 . 4 \times 2 1 0 ^ {6} \mathrm {e V} / (\mathrm {g} \mathrm {c m} ^ {- 2}) \times 1 . 8 1 0 ^ {- 3} \mathrm {g} / \mathrm {c m} ^ {3} \times 0 . 1 \mathrm {c m}}{1 5 \mathrm {e V}} \times 0. 1 0 \simeq 3. 3 6, \\ \end{array}
$$

where we used $2 \mathrm { M e V } / ( \mathrm { g } \mathrm { c m } ^ { - 2 } )$ for the minimum ionization energy loss. The number of events for which no electron reaches the anode is

$$
\epsilon_ {0} = (1 - P) ^ {N _ {e}} \simeq 0.70 ^ {3.36} \simeq 30.2 \%.
$$

The rate of coincident counts is finally

$$
\frac {d n _ {c}}{d t} = \frac {d n}{d t} \times (1 - \epsilon_ {0}) ^ {2} \simeq 1 4 0 0 \times 0. 6 9 8 ^ {2} \simeq 1 4 0 0 \times 0. 4 9 \simeq 6 9 0 \text {c o u n t s / s}.
$$

# Exercise 1.2.2

The number of minima is given by number of the zeroes of the form factor for a uniform charge distribution. The latter is given by

$$
F (q ^ {2}) = 3 \frac {\sin x - x \cos x}{x ^ {3}},
$$

![](images/2b98f17a556efe9ee54434442760d04a42abfde16890fd947eccb9897d00f25e.jpg)  
Fig. 1.2 tan $x$ versus $x$ (black). $y = x$ (red)

where $\textstyle x ~ = ~ q ~ R / \hbar$ , with $R$ given by the radius of the nucleus, $R = ( 1 . 1 8 A ^ { 1 / 3 } -$ 0.48) fm. $F ( q ^ { 2 } ) = 0$ leads to the equation

$$
\tan x = x.
$$

A graphical method allows to estimate the positions of the zeroes (see Fig. 1.2, black: tan $x$ , red: $x$ ) as the ones where the tangent equates the straight line. This occurs close to $x \simeq 3 \pi / 2 , 5 \pi / 2 , 7 \pi / 2 , 9 \pi / 2 \ldots$ .

In the actual experimental conditions $x$ is limited up to a maximum $x _ { \operatorname* { m a x } } =$ $q _ { \operatorname* { m a x } } R / \hbar$ . Remembering that

$$
q = 2 p \cdot \sin \frac {\theta}{2} \Rightarrow q _ {\max } = 2 p \simeq 2 \frac {E}{c}
$$

we have

$$
x _ {\max } = 2 \frac {E}{\hbar c} \times (1. 1 8 A ^ {1 / 3} - 0. 4 8) \mathrm {f m} \simeq \frac {2 \cdot 1 8 0 \mathrm {M e V}}{1 9 7 \mathrm {M e V f m}} \times 6. 4 \mathrm {f m} \simeq 1 1. 7.
$$

There are three minima below this value, corresponding to the zeroes up to $7 \pi / 2$ .

# Exercise 1.2.3

Considering the Rutherford cross section, we can write the counting rate at angle $\theta$ as

$$
f (\theta) = K \frac {\Phi}{\sin^ {4} \theta / 2},
$$

where $\Phi$ is the incident flux and $K$ an overall factor including various terms (kinematical, geometrical, etc.). We assume that

$$
f \left(2 0 ^ {\circ}\right) = K \frac {\Phi}{\sin^ {4} \left(2 0 ^ {\circ} / 2\right)} = 1 \mathrm {s} ^ {- 1}. \tag {1.1}
$$

Denoting with $f _ { a }$ the counting rate for a flux attenuated by a factor $a$ , we have

$$
f _ {a} \left(1 0 ^ {\circ}\right) = K \frac {a \Phi}{\sin^ {4} \left(1 0 ^ {\circ} / 2\right)} = 1 \mathrm {s} ^ {- 1}, \tag {1.2}
$$

Dividing (1.2) by (1.1) we get

$$
a = \left(\frac{\sin 5^{\circ}}{\sin 10^{\circ}}\right)^{4} \simeq 6.3\%.
$$

Using the attenuated beam, the counting rate at $2 0 ^ { \circ }$ is $f _ { a } ( 2 0 ^ { \circ } )$ . The mean waiting time is its inverse

$$
\langle \Delta t \rangle = \frac {1}{f _ {a} (2 0 ^ {\circ})} = \frac {1}{a f (2 0 ^ {\circ})} = \frac {1}{0 . 0 6 3 \times 1 \mathrm {s} ^ {- 1}} \simeq 1 6 \mathrm {s}.
$$

# Exercise 1.2.4

The differential cross section $d \sigma / d \Omega ( \theta )$ is given by $| F ( q ^ { 2 } ) | ^ { 2 } \times ( d \sigma / d \Omega ) _ { \mathrm { M o t t } }$ . For $\beta \to 1$ the latter cross section is

$$
\left(\frac {d \sigma}{d \Omega}\right) _ {\text {M o t t}} = \frac {Z ^ {2} \alpha^ {2} (\hbar c) ^ {2} \cos^ {2} \theta / 2}{4 (p c) ^ {2} \sin^ {4} \theta / 2}
$$

$$
\simeq \left(\frac {6 \times 1 9 7}{1 3 7}\right) ^ {2} \times \frac {\cos^ {2} 7 . 5 ^ {\circ}}{4 \times 1 0 0 ^ {2} \times \sin^ {4} 7 . 5 ^ {\circ}} \mathrm {f m} ^ {2} / \mathrm {s r} \simeq 6. 3 \times 1 0 ^ {- 2 6} \mathrm {c m} ^ {2} / \mathrm {s r}.
$$

The form factor can be neglected because the momentum transfer is small.1 Since $\sqrt { S } / R \ll 1$ , we can simply write

$$
\sigma = \left(\frac {d \sigma}{d \Omega}\right) _ {\text {M o t t}} \times S / R ^ {2} \simeq 6. 3 \cdot 1 0 ^ {- 2 6} \mathrm {c m} ^ {2} / \mathrm {s r} \times 7. 5 \cdot 1 0 ^ {- 4} \mathrm {s r} \simeq 4 7 \mu \mathrm {b}.
$$

$$
F (q ^ {2}) = 3 \frac {\sin x - x \cos x}{x ^ {3}} \simeq 0. 9 9.
$$

The number of scatterers per unit surface is $d n _ { \mathrm { T } } / d S = d \times N _ { A } / A \simeq 5 \times 1 0 ^ { 2 2 } { \mathrm { c m } } ^ { - 2 }$ . Then we have

$$
\frac {d N _ {e}}{d t} = \frac {I _ {0}}{e} \sigma \frac {d n _ {\mathrm {T}}}{d S} \simeq 1. 5 \times 1 0 ^ {8} \mathrm {s} ^ {- 1}.
$$

# Exercise 1.2.5

The momentum transfer (we have $p c \simeq E$ ) is

$$
q = 2 p \cdot \sin \theta / 2 = 2 \times 5 0 0 \times \sin 5 ^ {\circ} \simeq 8 7. 2 \mathrm {M e V} / \mathrm {c}.
$$

The Mott cross section at $1 0 ^ { \circ }$ can be written as

$$
\begin{array}{l} \left(\frac {d \sigma}{d \Omega}\right) _ {\mathrm {M o t t}} = 4 \frac {Z ^ {2} \alpha^ {2} (\hbar c) ^ {2}}{(q c) ^ {4}} E ^ {2} \cos^ {2} \frac {\theta}{2} \simeq \\ \simeq 4 \times \left(\frac {2 6 \times 1 9 7}{1 3 7}\right) ^ {2} \times \frac {5 0 0 ^ {2} \cos^ {2} 5 ^ {\circ}}{8 7 . 2 ^ {4}} f m ^ {2} / s r \simeq 0. 2 4 b / s r \\ \end{array}
$$

The form factor is given by

$$
F (q ^ {2}) = 3 \frac {\sin x - x \cos x}{x ^ {3}},
$$

where $\mathit { x } ~ = ~ q ~ R _ { A } / \hbar$ . Using $R _ { A } \simeq 1 . 2 \mathrm { f m } \times A ^ { 1 / 3 }$ for the nucleus radius, we find $x = 8 7 . 2 \times 4 . 6 / 1 9 7 \simeq 2$ and then

$$
\frac {d \sigma}{d \Omega} = \left(\frac {d \sigma}{d \Omega}\right) _ {\mathrm {M o t t}} | F (q ^ {2}) | ^ {2} = 0. 2 4 \frac {\mathrm {b}}{\mathrm {s r}} \times 0. 6 5 ^ {2} \simeq 0. 1 0 \frac {\mathrm {b}}{\mathrm {s r}}
$$

# Exercise 1.2.6

The Rutherford cross section can be written as

$$
\frac {d \sigma}{d \Omega} = \left[ \frac {z Z \alpha (\hbar c)}{4 E _ {\alpha}} \right] ^ {2} \frac {1}{\sin^ {4} \frac {\theta}{2}},
$$

where $z$ and $E _ { \alpha }$ are respectively the charge and kinetic energy of alpha particles. The solid angle corresponding to the detector is

$$
\Delta \Omega = \frac {S}{R ^ {2}} = 1 0 ^ {- 3} \mathrm {s r}.
$$

To achieve the required accuracy, we calculate the cross section at the largest angle $( 1 5 0 ^ { \circ } )$ in the chosen interval, where it has the smallest value

$$
\sigma = \left[ \frac {z Z \alpha (\hbar c)}{4 E _ {\alpha}} \right] ^ {2} \frac {\Delta \Omega}{\sin^ {4} \frac {\theta}{2}} \simeq \left[ \frac {2 \times 7 9 \times 1 9 7}{1 3 7 \times 4 \times 5 . 5} \right] ^ {2} \frac {1 0 ^ {- 3}}{0 . 8 7 0 5} \simeq 0. 1 2 \mathrm {f m} ^ {2} = 1. 2 \times 1 0 ^ {- 2 7} \mathrm {c m} ^ {2}.
$$

The event rate in the detector is

$$
r = I _ {\alpha} \rho \Delta l \frac {N _ {A}}{A} \sigma
$$

where $I _ { \alpha }$ is the beam intensity $( N _ { A } = 6 . 0 2 \times 1 0 ^ { 2 3 } \mathrm { m o l e } ^ { - 1 }$ is the Avogadro number). Thus the intensity of the $\alpha$ beam must be

$$
I _ {\alpha} > \frac {A}{\rho \Delta l N _ {A}} \frac {r}{\sigma} = \frac {1 9 7}{0 . 1 \times 6 . 0 2 \times 1 0 ^ {2 3}} \frac {1 0}{1 . 2 \times 1 0 ^ {- 2 7} \mathrm {c m} ^ {2}} \simeq 2. 7 \times 1 0 ^ {7} \mathrm {s} ^ {- 1}.
$$

# Exercise 1.2.7

The Q-factor of the reaction $p \ + \ _ { 3 } ^ { 7 } \mathrm { L i }  \ _ { 2 } ^ { 4 } \mathrm { H e } \ + \ _ { 2 } ^ { 4 } \mathrm { H e }$ is

$$
\begin{array}{l} Q = M _ {p} + M _ {\mathrm {L i}} - 2 M _ {\alpha} = M _ {p} + \left[ 3 M _ {p} + 4 M _ {n} - B \left(\stackrel {\rightharpoonup} {3} \mathrm {L i}\right)\right] - 2 \left[ 2 M _ {p} + 2 M _ {n} - B (\alpha) \right] = \\ = 2 B (\alpha) - B \left(_ {3} ^ {7} \mathrm {L i}\right) = 2 \cdot 2 8. 3 - 3 9. 3 = 1 7. 3 \mathrm {M e V} > 0 \\ \end{array}
$$

The reaction is exothermic.

According to the shell model, the $_ 3 ^ { 7 } \mathrm { L i }$ shell occupancies for protons and neutrons are

$$
\begin{array}{l} p: (1 s ^ {1 / 2}) ^ {2} (1 p ^ {3 / 2}) ^ {1} \\ n: (1 s ^ {1 / 2}) ^ {2} (1 p ^ {3 / 2}) ^ {2} \\ \end{array}
$$

The spin-parity is then determined by the odd $( 1 p ^ { 3 / 2 } )$ proton shell and is $J ^ { P } = ( 3 / 2 ) ^ { - }$ .

Protons at rest cannot interact with $_ { 3 } ^ { 7 } \mathrm { L i }$ nuclei because of the Coulomb barrier. Neglecting for simplicity the size of the proton with respect to the one of $_ { 3 } ^ { 7 } \mathrm { L i }$ , the minimum proton kinetic energy turns out to be

$$
T _ {\mathrm {m i n}} = \frac {z Z e ^ {2}}{4 \pi \epsilon_ {0} d} \simeq \frac {z Z \alpha \hbar c}{R (_ {3} ^ {7} \mathrm {L i})} \simeq \frac {3 \cdot 1 9 7 \mathrm {M e V f m}}{1 3 7 \cdot 1 . 2 7 ^ {1 / 3} \mathrm {f m}} \simeq 1. 9 \mathrm {M e V}.
$$

Indicating the spin-parities of the nuclei involved in the reaction, we have

$$
p \left(\frac {1}{2} ^ {+}\right) + _ {3} ^ {7} \mathrm {L i} \left(\frac {3}{2} ^ {-}\right)\rightarrow_ {2} ^ {4} \mathrm {H e} (0 ^ {+}) + _ {2} ^ {4} \mathrm {H e} (0 ^ {+})
$$

Knowing that the final orbital angular momentum is zero, we deduce that the initial total angular momentum must be zero. The angular momentum conservation imposes

$$
\frac {1}{2} \oplus \frac {3}{2} \oplus L _ {i} = 0
$$

denoting with $\oplus$ the operation of addition of angular momenta and with $L _ { i }$ the initial orbital angular momentum. Since $\textstyle { \frac { 1 } { 2 } } \oplus { \frac { 3 } { 2 } } = 1 , 2$ , then it follows that $L _ { i }$ must be either 1 or 2.

On the other hand parity conservation imposes the same parity for the initial and final states. The final parity is evidently $+ 1$ and then

$$
P _ {i} = P (p) \times P (_ {3} ^ {7} \mathrm {L i}) \times P _ {\mathrm {o r b}} = (+ 1) \times (- 1) \times (- 1) ^ {L _ {i}}
$$

hence $L _ { i }$ must be odd and finally $L _ { i } = 1$ .

# Exercise 1.2.8

The Mott cross section at $5 ^ { \circ }$ is

$$
\begin{array}{l} \left(\frac {d \sigma}{d \Omega}\right) _ {\text {M o t t}} = \left(\frac {Z \alpha \hbar c}{p c}\right) ^ {2} \frac {\cos^ {2} \theta / 2}{4 \sin^ {4} \theta / 2} \simeq \\ \simeq \left(\frac {6 \times 1 9 7}{1 3 7 \times 7 2 0}\right) ^ {2} \times \frac {\cos^ {2} 2 . 5 ^ {\circ}}{4 \times \sin^ {4} 2 . 5 ^ {\circ}} \frac {\mathrm {f m} ^ {2}}{\mathrm {s r}} \simeq 9 9 \frac {\mathrm {m b}}{\mathrm {s r}} \\ \end{array}
$$

Using the measured cross section, we derive the absolute square of the form factor as

$$
| F (\boldsymbol {q} ^ {2}) | ^ {2} = \frac {\left(\frac {d \sigma}{d \Omega}\right) _ {\text {m e a s}}}{\left(\frac {d \sigma}{d \Omega}\right) _ {\text {M o t t}}} \simeq \frac {8 0}{9 9} \simeq 0. 8 0 8
$$

If the nucleus is spherically symmetric, the form factor is real and then it can be obtained as the square root of its absolute square. Note that the indetermination of the sign is resolved looking at the momentum transfer. At $5 ^ { \circ }$ it is small and the form factor is still far from the first zero. Thus we can assume that the form factor is positive.

The momentum transfer turns out to be

$$
q = 2 p \sin \frac {\theta}{2} \simeq 6 2. 8 \mathrm {M e V / c}
$$

and then

$$
\langle r ^ {2} \rangle = \frac {6 \hbar^ {2}}{q ^ {2}} [ 1 - F (q ^ {2}) ] \simeq \frac {6 1 9 7 ^ {2}}{6 2 . 8 ^ {2}} \times (1 - \sqrt {0 . 8 0 8}) \simeq 5. 9 5 \mathrm {f m} ^ {2}
$$

from which we get for the $^ { 1 2 } \mathrm { C }$ nuclear radius 2.44 fm.

# Exercise 1.2.9

For $\beta \simeq 0 . 1$ a proton is non-relativistic and its maximum energy can be written as

$$
T _ {\max } \simeq \frac {1}{2} m _ {p} \beta^ {2} \simeq 0. 5 \times 9 3 8 \times 0. 0 1 \simeq 4. 7 \mathrm {M e V}. \tag {1.3}
$$

The maximum value of beta (and then of energy) corresponds to the forward scattering with the incident particle (γ or $n$ ) scattered back. In the case of photon scattering, $\gamma + p  \gamma + p$ , the kinematic relation is the same as in the Compton scattering, with the proton replacing the electron.

$$
E _ {\gamma} ^ {\prime} = \frac {E _ {\gamma}}{1 + E _ {\gamma} / m _ {p} (1 - \cos \theta)},
$$

where $E _ { \gamma }$ and $E _ { \gamma } ^ { \prime }$ are the photon initial and final energies and $\theta$ is the photon scattering angle. For $\theta = \dot { 1 } 8 0 ^ { \circ }$ the proton energy is maximum. Denoting with $T = E _ { \gamma } - E _ { \gamma } ^ { \prime }$ the proton kinetic energy, its maximum is

$$
T _ {\max } = E _ {\gamma} - \frac {E _ {\gamma}}{1 + 2 E _ {\gamma} / m _ {p}} = \frac {2 E _ {\gamma} ^ {2}}{m _ {p} + 2 E _ {\gamma}} \tag {1.4}
$$

(a) If we assume $1 0 \mathrm { M e V }$ for the photon energy, from (1.4) we have

$$
T _ {\max } = \frac {2 E _ {\gamma} ^ {2}}{m _ {p} + 2 E _ {\gamma}} \simeq \frac {2 \times 1 0 0}{9 3 8 + 2 0} \simeq 0. 2 1 \mathrm {M e V},
$$

which is largely smaller than (1.3).

(b) Solving Eq. (1.4) in $E _ { \gamma }$ and assuming that the proton energy is the one measured (1.3), the photon energy is

$$
E _ {\gamma} = \frac {T _ {\max } + \sqrt {T _ {\max } \left(T _ {\max } + 2 m _ {p}\right)}}{2} \simeq \frac {4 . 7 + \sqrt {4 . 7 (4 . 7 + 2 \cdot 9 3 8)}}{2} \simeq 4 9 \mathrm {M e V}.
$$

(c) In the case of neutron scattering, $n + p  n + p$ , the maximum proton energy occurs again in the forward scattering. Since the proton and neutron masses are very similar, this corresponds to the neutron stopped and the proton achieving the entire initial energy. This is a well known fact in a billiard, but can be easily obtained from kinematics. Being $\theta = 0$ , we can treat the kinematics in one dimension as

$$
T _ {n} = T _ {n} ^ {\prime} + T _ {p} ^ {\prime} \qquad p _ {n} = p _ {n} ^ {\prime} + p _ {p} ^ {\prime}.
$$

Expressing the kinetic energies as $T = p ^ { 2 } / ( 2 m )$ and assuming $m _ { n } = m _ { p }$ , we get

$$
p _ {p} ^ {\prime} \left(p _ {p} ^ {\prime} - p _ {n}\right) = 0 \quad \Longrightarrow \quad p _ {p} ^ {\prime} = p _ {n} \simeq 4. 7 \mathrm {M e V}.
$$

# Exercise 1.2.10

The Rutherford cross section is

$$
\frac {d \sigma}{d \Omega} = \left[ \frac {z Z \alpha (\hbar c)}{4 E _ {\alpha}} \right] ^ {2} \frac {1}{\sin^ {4} \frac {\theta}{2}},
$$

where z and $E _ { \alpha }$ are respectively the charge and kinetic energy of alpha particles. Using the solid angle subtended by the detector

$$
\Delta \Omega = \frac {S}{R ^ {2}} = \frac {0 . 5}{1 0 ^ {2}} = 5 1 0 ^ {- 3} \mathrm {s r},
$$

we get for the cross section at angle $\theta$

$$
\begin{array}{l} \sigma (\theta) = \left[ \frac {z Z \alpha (\hbar c)}{4 E _ {\alpha}} \right] ^ {2} \frac {\Delta \Omega}{\sin^ {4} \frac {\theta}{2}} \simeq \left[ \frac {2 \times 7 9 \times 1 9 7}{1 3 7 \times 4 \times 5 . 6 4} \right] ^ {2} \frac {5 1 0 ^ {- 3}}{\sin^ {4} \frac {\theta}{2}} \simeq \\ \simeq \frac {0 . 5 0 7}{\sin^ {4} \frac {\theta}{2}} \mathrm {f m} ^ {2} = \frac {5 . 0 7 \times 1 0 ^ {- 2 7}}{\sin^ {4} \frac {\theta}{2}} \mathrm {c m} ^ {2}. \\ \end{array}
$$

The number of counts during the time interval $\Delta t$ is

$$
N (\theta) = I _ {\alpha} \Delta t \rho d \frac {N _ {A}}{A} \sigma (\theta)
$$

where $I _ { \alpha }$ is the $\alpha$ beam intensity and $d$ is the target thickness. Solving in $I _ { \alpha }$ we have

$$
I _ {\alpha} = \frac {N (\theta)}{d \rho \Delta t \frac {N _ {A}}{A} \sigma (\theta)} = \frac {1 9 7}{0 . 0 0 5 \times 1 9 . 3 \times 3 6 0 0 \times 6 . 0 2 1 0 ^ {2 3} \times 5 . 0 7 1 0 ^ {- 2 7}} \times N (\theta) \sin^ {4} \frac {\theta}{2}
$$

and then

$$
I _ {\alpha} \simeq N (\theta) \times 1 8 6 \times \sin^ {4} \frac {\theta}{2} \mathrm {s} ^ {- 1}.
$$

The following table gives the beam intensity in $\mathrm { s } ^ { - 1 }$ resulting at each angle

<table><tr><td>θ</td><td>15°</td><td>25°</td><td>35°</td><td>45°</td><td>55°</td><td>65°</td><td>75°</td></tr><tr><td>Iα(s-1)</td><td>229.9 ± 3.5</td><td>242.1 ± 9.9</td><td>226 ± 19</td><td>199 ± 28</td><td>262 ± 47</td><td>201 ± 56</td><td>179 ± 67</td></tr></table>

The statistical errors are calculated as $\sqrt { N ( \theta ) } \times 1 8 6 \times \sin ^ { 4 } \theta / 2$ . Calculating the weighted average and its variance we get

$$
I _ {\alpha} = 2 3 0. 7 \pm 3. 2 \mathrm {s} ^ {- 1}.
$$

# 1.3 Nuclear Binding Energy

# Exercise 1.3.1

Decays among isobar nuclei belong to the class of beta decays. In the present case the mass number, $A = 1 9 7$ , is odd so that there is only one stable nucleus. In fact, using the semi-empirical mass formula (SEMF) the atomic mass $M ( A , Z )$ as a function of $Z$ is a single curve, because the pairing term is null for all isobars. The stable nucleus has $Z _ { s } = 7 9$ , the nucleus with $Z = Z _ { s } - 1 = 7 8$ can transmute to it via $\beta ^ { - }$ decay whereas the nucleus with $Z = Z _ { s } + 1 = 8 0$ can do it via $\beta ^ { + }$ decay or electron capture $( E C )$ .

We can write the atomic mass of $A = 1 9 7$ nuclei as

$$
\mathcal {M} (1 9 7, Z) = Z m _ {p} + (1 9 7 - Z) m _ {n} - B (1 9 7, Z) / c ^ {2} + Z m _ {e},
$$

where $B ( 1 9 7 , Z )$ is the nuclear binding energy, for which we use the SEMF. Writing explicitly only the terms depending on $Z$ we have

$$
\begin{array}{l} \mathcal {M} (1 9 7, Z) c ^ {2} = \operatorname {c o n s t} + Z \left(m _ {p} - m _ {n} + m _ {e}\right) c ^ {2} + a _ {C} \frac {Z ^ {2}}{1 9 7 ^ {1 / 3}} + a _ {A} \frac {(1 9 7 - 2 Z) ^ {2}}{1 9 7} \simeq \\ \simeq \operatorname {c o n s t} - 0. 7 8 2 Z + 0. 6 9 7 \frac {Z ^ {2}}{5 . 8 2} + 2 3. 3 \frac {(1 9 7 - 2 Z) ^ {2}}{1 9 7} \mathrm {M e V}. \\ \end{array}
$$

For the $\beta ^ { - }$ transition from $_ { 7 8 } ^ { 1 9 7 } \mathrm { P t }$ we have $M ( 1 9 7 , 7 8 ) - M ( 1 9 7 , 7 9 ) \simeq 0 . 9 0 \mathrm { M e V } ,$ hence it is allowed.

The $\beta ^ { + }$ transition from $_ { 8 0 } ^ { 1 9 7 } \mathrm { H g }$ is allowed if $M ( 1 9 7 , 8 0 ) - M ( 1 9 7 , 7 9 ) > 2 m _ { e }$ , if instead this difference is positive only the electron capture is possible. In the present case we have $M ( 1 9 7 , 8 0 ) - M ( 1 9 7 , 7 9 ) \simeq 0 . 3 ~ \mathrm { M e V / c ^ { 2 } }$ .

As a conclusion the possible decay types are

$$
\begin{array}{l} \beta^ {-}: \quad_ {7 8} ^ {1 9 7} \mathrm {P t} \rightarrow_ {7 9} ^ {1 9 7} \mathrm {A u} + e ^ {-} + \bar {\nu} _ {e} \\ E C: \quad e ^ {-} + _ {8 0} ^ {1 9 7} \mathrm {H g} \rightarrow_ {7 9} ^ {1 9 7} \mathrm {A u} + v _ {e} \\ \end{array}
$$

# Exercise 1.3.2

The mean neutron kinetic energy is $\langle E \rangle \approx k _ { B } T \simeq k _ { B }$ $3 0 0 \simeq 2 5 ~ \mathrm { m e V }$ . From the semi-empirical mass formula we get

$$
\begin{array}{l} B (2 3 5, 9 2) = 1 7 8 6. 8 \mathrm {M e V} \\ B (1 4 8, 5 7) = 1 2 0 9. 8 \mathrm {M e V} \\ B (8 7, 3 5) = 7 4 5. 4 \mathrm {M e V}. \\ \end{array}
$$

The neutron energy is negligible with respect to the other energies and then we have for the energy release

$$
Q = B (1 4 8, 5 7) + B (8 7, 3 5) - B (2 3 5, 9 2) \simeq 1 6 8 \mathrm {M e V}.
$$

A similar though less accurate conclusion can be reached using the $B / A$ values from the binding energy per nucleon plot reported in all the textbooks. The values are 7.6, 8.2 and $8 . 6 \mathrm { M e V } ,$ respectively $A = 2 3 5$ , 148 e 87. Hence we obtain

$$
Q = 1 4 8 \cdot 8. 2 + 8 7 \cdot 8. 6 - 2 3 5 \cdot 7. 6 \simeq 1 7 6 \mathrm {M e V}.
$$

# Exercise 1.3.3

At large distance, in the rest frame of one of the nuclei, the other has velocity $2 \nu$ . At the minimum distance $R$ the two nuclei are at rest. From energy conservation then we get

$$
\frac {1}{2} M (2 \nu) ^ {2} = 4 E = \frac {e ^ {2}}{4 \pi \epsilon_ {0} R} = \frac {\alpha \hbar c}{R} = \frac {1 9 7 \mathrm {M e V f m}}{1 3 7 \cdot 1 . 4 \mathrm {f m}} \simeq 1 \mathrm {M e V},
$$

$E$ , the mean kinetic energy of each nucleus, is then about $0 . 2 5 \mathrm { M e V } .$ .

Knowing that for $T = 3 0 0 ~ \mathrm { K }$ the mean kinetic energy is $k _ { B } T \simeq 2 5 \ \mathrm { m e V } _ { \mathrm { \Omega } }$ , the temperature for which nuclei have $E \simeq 0 . 2 5 \mathrm { M e V }$ is

$$
T = \frac {E}{k _ {B}} = \frac {0 . 2 5 1 0 ^ {6} \mathrm {e V} \times 3 0 0}{2 5 1 0 ^ {- 3} \mathrm {e V}} \simeq 3 1 0 ^ {9} \mathrm {K}.
$$

The energy release is

$$
Q = B _ {T} - 2 B _ {D} \simeq 4 \mathrm {M e V}.
$$

# Exercise 1.3.4

The reaction in the text belongs to the more general class

$$
v _ {e} + (A, Z) \rightarrow (A, Z + 1) + e ^ {-}.
$$

The threshold energy is given by

$$
E _ {\mathrm {t h}} = \frac {\left(m _ {e} + M ^ {\prime}\right) ^ {2} - M ^ {2}}{2 M}, \tag {1.5}
$$

where $M$ and $M ^ { \prime }$ are the masses of $( A , Z )$ and $( A , Z + 1 )$ nuclei respectively. These masses are related to the binding energies as follows

$$
M = Z M _ {p} + (A - Z) M _ {n} - B (A, Z) / c ^ {2}
$$

$$
M ^ {\prime} = (Z + 1) M _ {p} + (A - Z - 1) M _ {n} - B (A, Z + 1) / c ^ {2} = M + \Delta M,
$$

hence we have

$$
\Delta M = \left(M _ {p} - M _ {n}\right) + \Delta B / c ^ {2} \text {w i t h} \Delta B = B (A, Z) - B (A, Z + 1).
$$

$\Delta B$ can be calculated using the semi-empirical mass formula. In particular for odd-A nuclei only the Coulomb and asymmetry terms are needed, because:

1. the volume and surface terms depend only on A and they cancel out in the difference;   
2. for odd- A the pairing term is null for both initial and final nuclei.

We have

$$
\begin{array}{l} \Delta B = - a _ {C} \left\{\frac {Z ^ {2}}{A ^ {1 / 3}} - \frac {(Z + 1) ^ {2}}{A ^ {1 / 3}} \right\} - a _ {A} \left\{\frac {(A - 2 Z) ^ {2}}{A} - \frac {[ A - 2 (Z + 1) ] ^ {2}}{A} \right\} = \\ = a _ {C} \frac {2 Z + 1}{A ^ {1 / 3}} - 4 a _ {A} \frac {A - 2 Z - 1}{A} \\ \end{array}
$$

In the reaction considered in the text $A = 3 7$ and $Z = 1 7$ and then we have

$$
\Delta M = - 1. 2 9 3 + 0. 6 9 7 \times \frac {3 5}{3 7 ^ {1 / 3}} - 4 \times 2 3. 3 \times \frac {2}{3 7} \simeq 1 \mathrm {M e V}.
$$

Substituting this value in (1.5) we obtain

$$
\begin{array}{l} E _ {\mathrm {t h}} = \frac {[ m _ {e} + (M + \Delta M) ] ^ {2} - M ^ {2}}{2 M} = \frac {m _ {e} (m _ {e} + 2 M) + \Delta M (2 m _ {e} + \Delta M + 2 M)}{2 M} \\ \simeq m _ {e} + \Delta M \simeq 1. 5 \mathrm {M e V}. \\ \end{array}
$$

# Exercise 1.3.5

Denoting by $Q _ { - }$ the $Q$ -factor for the $\beta _ { - }$ decay

$$
{ } _ { 2 9 } ^ { 6 4 } \mathrm { C u } \rightarrow { } _ { 3 0 } ^ { 6 4 } \mathrm { Z n } + e ^ { - } + \bar { \nu } _ { e }
$$

and $Q _ { + }$ the one for the $\beta _ { + }$ decay

$$
{ } _ { 2 9 } ^ { 6 4 } \mathrm { C u } \rightarrow { } _ { 2 8 } ^ { 6 4 } \mathrm { N i } + e ^ { + } + \nu _ { e }
$$

we have (omitting the factor $c ^ { 2 }$ in the mass terms)

$$
\begin{array}{l} Q _ {-} = 2 9 M _ {p} + 3 5 M _ {n} - B (6 4, 2 9) - 3 0 M _ {p} - 3 4 M _ {n} + B (6 4, 3 0) - m _ {e} \\ = M _ {n} - M _ {p} - m _ {e} + B (6 4, 3 0) - B (6 4, 2 9) \simeq 0. 7 8 2 \mathrm {M e V} + \mathrm {B} (6 4, 3 0) - \mathrm {B} (6 4, 2 9). \\ \end{array}
$$

Similarly we have

$$
Q _ {+} = M _ {p} - M _ {n} - m _ {e} + B (6 4, 2 8) - B (6 4, 2 9) \simeq - 1. 8 0 4 \mathrm {M e V} + \mathrm {B} (6 4, 2 8) - \mathrm {B} (6 4, 2 9).
$$

From the SEMF we get

$$
\begin{array}{l} B (6 4, 3 0) - B (6 4, 2 9) = - 0. 6 9 7 \times \frac {3 0 ^ {2} - 2 9 ^ {2}}{6 4 ^ {1 / 3}} - 2 3. 3 \times \frac {(6 4 - 6 0) ^ {2} - (6 4 - 5 8) ^ {2}}{6 4} + \\ + \frac {1 2 + 1 2}{\sqrt {6 4}} \simeq 0. 0 0 0 5 \mathrm {M e V}, \\ \end{array}
$$

$$
\begin{array}{l} B (6 4, 2 8) - B (6 4, 2 9) = - 0. 6 9 7 \times \frac {2 8 ^ {2} - 2 9 ^ {2}}{6 4 ^ {1 / 3}} - 2 3. 3 \times \frac {(6 4 - 5 6) ^ {2} - (6 4 - 5 8) ^ {2}}{6 4} + \\ + \frac {1 2 + 1 2}{\sqrt {6 4}} \simeq 2. 7 4 \mathrm {M e V}. \\ \end{array}
$$

Hence we have

$$
Q _ {-} \simeq 0. 7 8 \mathrm {M e V} \quad Q _ {+} \simeq 0. 9 4 \mathrm {M e V}.
$$

Both decays are allowed. The maximum kinetic energies of the electron and positron are equal respectively to $Q _ { - }$ and $Q _ { + }$ .

# Exercise 1.3.6

The stability condition can be written as ∂M(A,Z) 0, (A, Z ) being the atomic $\begin{array} { r } { \frac { \partial \mathcal { M } ( A , Z ) } { \partial Z } = 0 } \end{array}$ $M ( A , Z )$ mass of the nucleus $( A , Z )$ , which is is single function for odd-A nuclei. Using the SEMF we have

$$
\frac {2 a _ {c} Z}{A ^ {1 / 3}} - \frac {4 a _ {a} (A - 2 Z)}{A} - \left(M _ {n} - M _ {p} - m _ {e}\right) c ^ {2} = 0
$$

hence we get for the asymmetry coefficient

$$
a _ {A} = \frac {A}{4 (A - 2 Z)} \left[ \frac {2 a _ {c} Z}{A ^ {1 / 3}} - \left(M _ {n} - M _ {p} - m _ {e}\right) c ^ {2} \right] \simeq 2 4 \mathrm {M e V}.
$$

# Exercise 1.3.7

For a $\beta ^ { + }$ decay, $( A , Z ) \to ( A , Z - 1 ) + e ^ { + } + \nu _ { e }$ , the $Q _ { \beta }$ value, is

$$
Q _ {\beta} = [ M (A, Z) - M (A, Z - 1) - m ] c ^ {2},
$$

where

$$
M (A, Z) = Z M _ {p} + (A - Z) M _ {n} - B (A, Z) / c ^ {2}
$$

$$
M (A, Z - 1) = (Z - 1) M _ {p} + (A - Z + 1) M _ {n} - B (A, Z - 1) / c ^ {2}.
$$

Hence we have

$$
Q _ {\beta} = \left[ M _ {p} - M _ {n} - m \right] c ^ {2} - \Delta B, \tag {1.6}
$$

where

$$
\Delta B = B (A, Z) - B (A, Z - 1).
$$

Calculating $\Delta B$ from the SEMF, we observe that all terms cancel but the Coulomb and asymmetry ones because

1. the volume and surface terms depend on A only,   
2. A is odd and the pairing term is the same $( = 0 )$ ) for both nuclei.

Then we have

$$
\begin{array}{l} \Delta B = - a _ {C} \left\{\frac {Z ^ {2}}{A ^ {1 / 3}} - \frac {(Z - 1) ^ {2}}{A ^ {1 / 3}} \right\} - a _ {A} \left\{\frac {(A - 2 Z) ^ {2}}{A} - \frac {[ A - 2 (Z - 1) ] ^ {2}}{A} \right\} \\ = - a _ {C} \frac {2 Z - 1}{A ^ {1 / 3}} - 4 a _ {A} \frac {A - 2 Z + 1}{A} \tag {1.7} \\ \end{array}
$$

Considering the decay in the text, we have $A = 3 5$ and $Z = 1 8$ : hence the term multiplying $a _ { A }$ vanishes. Inverting equation (1.7) we obtain

$$
a _ {C} = - \frac {A ^ {1 / 3} \Delta B}{2 Z - 1}.
$$

From (1.6) we have

$$
\Delta B = \left[ M _ {p} - M _ {n} - m \right] c ^ {2} - Q _ {\beta} = - 1. 2 9 3 - 0. 5 1 1 - 4. 9 5 \simeq - 6. 7 5 \mathrm {M e V},
$$

where we have used the maximum positron energy for $Q _ { \beta }$ . Finally we get

$$
a _ {C} = - \frac {3 5 ^ {1 / 3} \times - 6 . 7 5}{3 5} \simeq 0. 6 3 \mathrm {M e V}.
$$

The value obtained in this way differs from the best-fit value (0.697 MeV) given with the SEMF by less than $10 \%$ .

# Exercise 1.3.8

Denoting by $Q _ { - }$ the $Q$ -value for

$$
{ } _ { 4 3 } ^ { 1 0 0 } \mathrm { T c } \rightarrow { } _ { 4 4 } ^ { 1 0 0 } \mathrm { R u } + e ^ { - } + \bar { \nu } _ { e }
$$

and with $Q _ { + }$ the one for

$$
{ } _ { 4 3 } ^ { 1 0 0 } \mathrm { T c } \rightarrow { } _ { 4 2 } ^ { 1 0 0 } \mathrm { M o } + e ^ { + } + \nu _ { e }
$$

we have (omitting $c ^ { 2 }$ multiplying the masses)

$$
\begin{array}{l} Q _ {-} = 4 3 M _ {p} + 5 7 M _ {n} - B (1 0 0, 4 3) - 4 4 M _ {p} - 5 6 M _ {n} + B (1 0 0, 4 4) - m _ {e} = \\ = M _ {n} - M _ {p} - m _ {e} + B (1 0 0, 4 4) - B (1 0 0, 4 3) \simeq \\ \simeq B (1 0 0, 4 4) - B (1 0 0, 4 3) + 0. 7 8 2 \mathrm {M e V} \\ \end{array}
$$

and

$$
\begin{array}{l} Q _ {+} = M _ {p} - M _ {n} - m _ {e} + B (1 0 0, 4 2) - B (1 0 0, 4 3) \simeq \\ \simeq B (1 0 0, 4 2) - B (1 0 0, 4 3) - 1. 8 0 4 \mathrm {M e V} \\ \end{array}
$$

From the semi-empirical mass formula we have for an odd-A odd-Z nucleus

$$
\begin{array}{l} B (A, Z) - B (A, Z \pm 1) = - a _ {C} \frac {Z ^ {2} - (Z \pm 1) ^ {2}}{A ^ {1 / 3}} - \\ - a _ {A} \frac {(A - 2 Z) ^ {2} - [ A - 2 (Z \pm 1) ] ^ {2}}{A} - 2 \frac {a _ {P}}{A ^ {1 / 2}}. \\ \end{array}
$$

In the current case we have

$$
B (1 0 0, 4 3) - B (1 0 0, 4 4) = - 0. 6 9 7 \times \frac {4 3 ^ {2} - 4 4 ^ {2}}{1 0 0 ^ {1 / 3}} -
$$

$$
- 2 3. 3 \times \frac {(1 0 0 - 8 6) ^ {2} - (1 0 0 - 8 8) ^ {2}}{1 0 0} - 2 \times \frac {1 2}{\sqrt {1 0 0}} \simeq - 1. 4 5 \mathrm {M e V}
$$

$$
\begin{array}{l} B (1 0 0, 4 3) - B (1 0 0, 4 2) = - 0. 6 9 7 \times \frac {4 3 ^ {2} - 4 2 ^ {2}}{1 0 0 ^ {1 / 3}} - \\ - 2 3. 3 \times \frac {(1 0 0 - 8 6) ^ {2} - (1 0 0 - 8 4) ^ {2}}{1 0 0} - 2 \times \frac {1 2}{\sqrt {1 0 0}} \simeq - 1. 1 8 \mathrm {M e V}. \\ \end{array}
$$

Hence we obtain

$$
Q _ {-} \simeq 2. 2 3 \mathrm {M e V} \quad Q _ {+} \simeq - 0. 6 2 \mathrm {M e V}.
$$

The $\beta ^ { - }$ decay to $_ { 4 4 } ^ { 1 0 0 } \mathrm { R u }$ is allowed. Instead the $\beta ^ { + }$ decay is forbidden, yet the electron capture, allowing the transition to $^ { 1 0 0 } _ { 4 2 } \mathrm { M o }$ , is possible since we have $Q _ { E C } = Q _ { + } +$ $2 m _ { e } \simeq 0 . 4 0 \mathrm { M e V } > 0$ .

# Exercise 1.3.9

(a) Each fission reaction releases $2 0 0 ~ { \mathrm { M e V } } = 2 ~ 1 0 ^ { 8 } ~ { \mathrm { e V } } \times 1 . 6 ~ 1 0 ^ { - 1 9 } ~ { \mathrm { J / e V } } \simeq 3 . 2$ $1 0 ^ { - 1 1 }$ J. Hence the fission rate is

$$
r = \frac {P}{E _ {\mathrm {f i s s}}} = \frac {2 1 0 ^ {9}}{3 . 2 1 0 ^ {- 1 1}} \simeq 6. 2 5 1 0 ^ {1 9} \mathrm {s} ^ {- 1}.
$$

(b) $1 \mathrm { { g } }$ of $^ { 2 3 5 } \mathrm { U }$ releases an energy

$$
E _ {\mathrm {f i s s}} \times \frac {N _ {A}}{A} = 3. 2 1 0 ^ {- 1 1} \times \frac {6 1 0 ^ {2 3}}{2 3 5} \simeq 0. 8 1 0 ^ {1 1} \mathrm {J / g}.
$$

In a year the total energy is

$$
2 1 0 ^ {9} \frac {\mathrm {J}}{\mathrm {s}} \times 3. 1 5 1 0 ^ {7} \mathrm {s} \simeq 6. 3 1 0 ^ {1 6} \mathrm {J}.
$$

The $^ { 2 3 5 } \mathrm { U }$ mass consumed in a year is then

$$
M \left(^ {2 3 5} \mathrm {U}\right) = \frac {6 . 3 1 0 ^ {1 6} \mathrm {J}}{0 . 8 1 0 ^ {1 1} \mathrm {J / g}} \simeq 7. 8 8 1 0 ^ {5} \mathrm {g} = 7 8 8 \mathrm {k g}.
$$

Since $^ { 2 3 5 } \mathrm { U }$ is about $30 \%$ , the used fuel mass is about 2.6 ton.

(c) The maximum neutrino energy is equal to the $Q$ -factor of the beta decay. Denoting it by $Q _ { - }$ , for the $5 7 ^ { 1 4 5 } \mathrm { L a } \beta ^ { - }$ $\beta ^ { - }$ decay, we have (omitting $c ^ { 2 }$ in the mass terms):

$$
Q _ {-} = M _ {n} - M _ {p} - m _ {e} - B (1 4 5, 5 7) + B (1 4 5, 5 8) \simeq 0. 7 8 2 \mathrm {M e V} - \Delta B _ {-}
$$

where $\Delta B _ { - }$ is the difference in binding energy between parent and daughter nuclei. Using the SEMF we have for odd-A nuclei

$$
\begin{array}{l} \Delta B _ {-} = B (A, Z) - B (A, Z + 1) \simeq \\ \simeq - a _ {C} \frac {Z ^ {2} - (Z + 1) ^ {2}}{A ^ {1 / 3}} - a _ {A} \frac {(A - 2 Z) ^ {2} - [ A - 2 (Z + 1) ] ^ {2}}{A}, \\ \end{array}
$$

which becomes in our case

$$
\Delta B _ {-} = - 0. 6 9 7 \times \frac {5 7 ^ {2} - 5 8 ^ {2}}{1 4 5 ^ {1 / 3}} - 2 3. 3 \times \frac {(1 4 5 - 1 1 4) ^ {2} - (1 4 5 - 1 1 6) ^ {2}}{1 4 5} \simeq - 4. 0 3 \mathrm {M e V}
$$

The maximum neutrino energy is then $0 . 7 8 2 + 4 . 0 3 \simeq 4 . 8 1 \mathrm { M e V } .$

(d) The neutrino intensity is $20 \%$ of the fission rate $0 . 2 0 \times 6 . 2 5 1 0 ^ { 1 9 } \mathrm { { \ s } } ^ { - 1 } = 1 . 2 5$ $1 0 ^ { 1 9 } \mathrm { ~ s ^ { - 1 } }$ . At $5 0 0 \mathrm { m }$ distance the neutrino flux is

$$
\Phi = \frac {I _ {\nu}}{4 \pi R ^ {2}} \simeq \frac {1 . 2 5 1 0 ^ {1 9}}{1 2 . 5 6 5 0 0 ^ {2}} \simeq 4 \times 1 0 ^ {1 2} \mathrm {m} ^ {- 2} \mathrm {s} ^ {- 1}
$$

(e) For a detector having a length $l$ (along the neutrino direction), a section S, composed of material of atomic mass $A$ , the interaction rate is

Appendix: Solutions of Exercises and Problems

$$
r = \Phi \times \sigma \times \frac {N _ {A}}{A} \times \rho l S = \Phi \times \sigma \times \frac {N _ {A}}{A} \times M.
$$

Such proportionality between rate and mass is holding each time the detector length is much smaller of the interaction length. Inserting our values we get

$$
r = 4 \times 1 0 ^ {1 2} \mathrm {m} ^ {- 2} \mathrm {s} ^ {- 1} \times 6 1 0 ^ {- 4 8} \mathrm {m} ^ {2} \times \frac {6 1 0 ^ {2 3}}{\mathrm {g} A} \times 1 0 ^ {6} \mathrm {g} \simeq \frac {1 . 4 4 1 0 ^ {- 5}}{A} \mathrm {s} ^ {- 1} \simeq \frac {4 5 0}{A} \mathrm {y r} ^ {- 1}
$$

# Exercise 1.3.10

Let us call $Q _ { + }$ the Q-factor for the $\beta ^ { + }$ -decay of $^ { 2 7 } _ { 1 4 } \mathrm { S i }$ . Omitting the factor $c ^ { 2 }$ multiplying the mass terms, we have:

$$
(E _ {e}) _ {\max } = Q _ {+} = M _ {p} - M _ {n} - m _ {e} - B (2 7, 1 4) + B (2 7, 1 3)
$$

(a) The binding energy of $^ { 2 7 } _ { 1 3 } \mathrm { A l }$ is then

$$
B (2 7, 1 4) = B (2 7, 1 3) + M _ {p} - M _ {n} - m _ {e} - \left(E _ {e}\right) _ {\max } = 2 1 9. 3 6 \mathrm {M e V}
$$

(b) The nuclei involved in the decay are odd-A, hence the pairing term of the SEMF disappears from the mass difference. The volume and surface terms do not contribute in any case. Considering the two surviving terms $\scriptstyle { a _ { C } }$ and $a _ { A }$ ), the asymmetry term does not contribute since we have, for $A = 2 7$ and $Z = 1 4$ , $( A - 2 Z ) ^ { 2 } = ( A -$ $2 ( Z - 1 ) ) ^ { 2 }$ . Hence the mass difference depends only on the Coulomb term $a _ { C }$ .

(c) For a uniform charge distribution, we have

$$
\Delta B = \frac {3}{5} \frac {e ^ {2}}{4 \pi \epsilon_ {0} R} [ Z ^ {2} (\mathrm {S i}) - Z ^ {2} (\mathrm {A l}) ] = \frac {3}{5} \frac {\alpha \hbar c}{R} [ Z ^ {2} (\mathrm {S i}) - Z ^ {2} (\mathrm {A l}) ].
$$

Hence we get for the $^ { 2 7 } _ { 1 4 } \mathrm { S i }$ radius

$$
R = \frac {3}{5} \frac {\alpha \hbar c}{\Delta B} \left[ Z ^ {2} (\mathrm {S i}) - Z ^ {2} (\mathrm {A l}) \right] = 0. 6 \times \frac {1 . 4 \mathrm {M e V f m}}{5 . 5 9 \mathrm {M e V}} \times (1 4 ^ {2} - 1 3 ^ {2}) \simeq 4. 1 \mathrm {f m}
$$

# Exercise 1.3.11

The reaction $\nu _ { e } + \ O _ { 3 1 } ^ { 7 1 } \mathrm { G a } \to \ O _ { 3 2 } ^ { 7 1 } \mathrm { G e } + e ^ { - }$ belongs to the more general class

$$
v _ {e} + (A, Z) \rightarrow (A, Z + 1) + e ^ {-},
$$

for which the neutrino threshold energy is

$$
E _ {\mathrm {t h}} = \frac {(m _ {e} + M ^ {\prime}) ^ {2} - M ^ {2}}{2 M},
$$

where $M$ and $M ^ { \prime }$ are the masses of the nuclei $( A , Z )$ and $( A , Z + 1 )$ respectively. Denoting by $\Delta M$ the mass difference $M ^ { \prime } - M$ , we have

$$
E _ {\mathrm {t h}} = \frac {[ m _ {e} + (M + \Delta M) ] ^ {2} - M ^ {2}}{2 M}
$$

which, being M, $m _ { e } \ll M$ , becomes

$$
E _ {\text {t h}} \simeq m _ {e} + \Delta M. \tag {1.8}
$$

We can write $\Delta M$ as

$$
\Delta M = M ^ {\prime} - M = M _ {p} - M _ {n} + \Delta B / c ^ {2} \tag {1.9}
$$

with

$$
\Delta B = B (A, Z) - B (A, Z + 1).
$$

Combining (1.8) and (1.9) we finally get

$$
\begin{array}{l} B (7 1, 3 2) = B (7 1, 3 1) - \Delta B = B (7 1, 3 1) - \Delta M - \left(M _ {n} - M _ {p}\right) c ^ {2} = \\ = B (7 1, 3 1) - E _ {\mathrm {t h}} - \left(M _ {n} - M _ {p} - m _ {e}\right) c ^ {2} \simeq \\ \simeq 6 1 8. 9 5 - 0. 2 3 3 - 0. 7 8 2 \simeq 6 1 7. 9 3 \mathrm {M e V}. \\ \end{array}
$$

Using the SEMF we have instead

$$
B (7 1, 3 2) \simeq 6 2 0. 8 8 \mathrm {M e V}
$$

which differs about 0.5 percent from the previous value.

# Exercise 1.3.12

The minimum atomic mass for isobars can be obtained from the equation ∂M( A,Z ) $\begin{array} { r } { \frac { \partial \mathcal { M } ( A , Z ) } { \partial Z } = 0 } \end{array}$ Using the SEMF we obtain

$$
\frac {2 a _ {C} Z}{A ^ {1 / 3}} - \frac {4 a _ {A} (A - 2 Z)}{A} + (M _ {n} - M _ {p} - m _ {e}) c ^ {2} = 0
$$

The term which depends on the electromagnetic coupling constant is $a _ { C }$ . Solving in $a _ { C }$ we get

$$
a _ {C} = \frac {A ^ {1 / 3}}{2 Z} \left[ \frac {4 a _ {A} (A - 2 Z)}{A} - (M _ {n} - M _ {p} - m _ {e}) c ^ {2} \right]
$$

If the stable nucleus is $_ { 5 4 } ^ { 1 3 3 } \mathrm { X e }$ , the $a _ { C }$ parameter should be

Appendix: Solutions of Exercises and Problems

$$
a _ {C} = \frac {1 3 3 ^ {1 / 3}}{2 \times 5 4} \left[ \frac {4 \times 2 3 . 3 (1 3 3 - 1 0 8)}{1 3 3} - 0. 7 8 2 \right] \mathrm {M e V} \simeq 0. 7 9 1 \mathrm {M e V}.
$$

From classical electrostatics we know that the Coulomb term is proportional to the fine structure constant $a _ { C } \propto \alpha$ . Hence the change in the coupling constant is

$$
\frac {\Delta \alpha}{\alpha} = \frac {\Delta a _ {C}}{a _ {C}} \simeq \frac {0 .791 - 0.697}{0.697} \simeq 13 \%
$$

# Exercise 1.3.13

(a) For photons colliding against a fixed iron target, the threshold energy is

$$
E _ {\gamma} ^ {\mathrm {t h}} = \frac {(M ^ {\prime} + m) ^ {2} - M ^ {2}}{2 M} = \frac {\mu^ {2}}{2 M} \tag {1.10}
$$

where $M$ is the mass of the initial nucleus, $( A , Z )$ , $M ^ { \prime }$ that of the final nucleus, $( A - 1 , Z )$ , and $m$ the neutron mass. Denoting by $\Delta M$ the nuclear mass difference $M - M ^ { \prime }$ and with $\Delta B$ the corresponding binding energy difference, we have

$$
\mu^ {2} = [ (M - \Delta M) + m ] ^ {2} - M ^ {2} = m (m + 2 M) - \Delta M (2 M + 2 m - \Delta M).
$$

Since M, m  M, we get

$$
\mu^ {2} \simeq 2 M (m - \Delta M) = 2 M \Delta B, \tag {1.11}
$$

having used the relation

$$
\Delta M = M - M ^ {\prime} = m - \Delta B
$$

For $^ { 5 6 } _ { 2 6 } \mathrm { F e }$ photo-disintegrating into $^ { 5 5 } _ { 2 6 } \mathrm { F e }$ , $\Delta B$ can be obtained from the semi-empirical mass formula

$$
\Delta B = B (5 6, 2 6) - B (5 5, 2 6) \simeq 4 9 0. 9 5 - 4 7 8. 9 0 \simeq 1 2 \mathrm {M e V}. \tag {1.12}
$$

Hence the photon threshold energy is

$$
E _ {\gamma} ^ {\mathrm {t h}} \simeq \frac {2 M \Delta B}{2 M} = \Delta B \simeq 1 2 \mathrm {M e V}.
$$

(b) In the case of Cosmic Rays, the collision does not occur in a fixed target frame and the expression (1.10) cannot be used. Instead we make use of the invariance of the total 4-momentum squared so that we can write, at the threshold

$$
(M ^ {\prime} + m) ^ {2} = (E _ {N} ^ {\mathrm {t h}} + E _ {\gamma}) ^ {2} - (\boldsymbol {p} _ {N} ^ {\mathrm {t h}} + \boldsymbol {p} _ {\gamma}) ^ {2} = E _ {N} ^ {\mathrm {t h}} ^ {2} + E _ {\gamma} ^ {2} + 2 E _ {N} ^ {\mathrm {t h}} E _ {\gamma} - \boldsymbol {p} _ {N} ^ {\mathrm {t h}} ^ {2} - \boldsymbol {p} _ {\gamma} ^ {2} - 2 \boldsymbol {p} _ {N} ^ {\mathrm {t h}} \cdot \boldsymbol {p} _ {\gamma},
$$

where $( E _ { N } ^ { \mathrm { t h } } , p _ { N } ^ { \mathrm { t h } } )$ is the 4-momentum of the initial nucleus (at the threshold energy) and $( E _ { \gamma } , p _ { \gamma } )$ the photon 4-momentum. Since nuclei are ultra-relativistic we have

$$
(M ^ {\prime} + m) ^ {2} \simeq M ^ {2} + 2 E _ {N} ^ {\mathrm {t h}} E _ {\gamma} (1 - \cos \theta),
$$

where $\theta$ is the angle between the nucleus and photon directions. Using $\mu ^ { 2 }$ we obtain

$$
2 E _ {N} ^ {\mathrm {t h}} E _ {\gamma} (1 - \cos \theta) \simeq \mu^ {2}.
$$

The nucleus threshold energy is

$$
E _ {N} ^ {\mathrm {t h}} = \frac {\mu^ {2}}{2 E _ {\gamma} (1 - \cos \theta)}.
$$

Using (1.11) and $\theta = \pi$ (head-on collisions), we finally get

$$
E _ {N} ^ {\mathrm {t h}} = \frac {M \Delta B}{2 E _ {\gamma}} = \frac {5 2 \mathrm {G e V} 1 2 \mathrm {M e V}}{2 1 0 ^ {- 3} \mathrm {e V}} \simeq 3 \times 1 0 ^ {2 0} \mathrm {e V}
$$

where we have used $M = M ( 5 6 , 2 6 ) \simeq 5 2 { \mathrm { G e V } } ,$ as obtained from the SEMF.

# Exercise 1.3.14

(a) We can write the two separation energies as

$$
S _ {p} = B (A, Z) - B (A - 1, Z - 1)
$$

$$
S _ {n} = B (A, Z) - B (A - 1, Z)
$$

hence we obtain for the difference

$$
S _ {p} - S _ {n} = B (A - 1, Z) - B (A - 1, Z - 1).
$$

Using the SEMF we get

$$
\begin{array}{l} S _ {P} - S _ {n} = - a _ {C} \frac {Z ^ {2} - (Z - 1) ^ {2}}{(A - 1) ^ {1 / 3}} - a _ {A} \frac {(A - 1 - 2 Z) ^ {2} - [ A - 1 - 2 (Z - 1) ] ^ {2}}{A - 1} + D _ {P} = \\ - a _ {C} \frac {2 Z - 1}{(A - 1) ^ {1 / 3}} + 4 a _ {A} \frac {A - 2 Z}{A - 1} + D _ {P}, \tag {1.13} \\ \end{array}
$$

where $D _ { P }$ originates from the difference of the pairing terms, $\delta _ { P } ( A )$

The possible values of $D _ { P }$ are reported in the following table, where $e$ and $o$ stand for even and odd nucleon parity in the corresponding nucleus.

(b) If in Eq. (1.13) we insert $Z = A / 2$ , valid for light nuclei, we obtain

<table><tr><td>parent</td><td colspan="2">Sp:(Z,N-1)</td><td colspan="2">Sn:(Z-1,N)</td><td>DP</td></tr><tr><td>Z,N</td><td>parity</td><td>δP</td><td>parity</td><td>δP</td><td></td></tr><tr><td>e e</td><td>e o</td><td>0</td><td>o e</td><td>0</td><td>0</td></tr><tr><td>o o</td><td>o e</td><td>0</td><td>e o</td><td>0</td><td>0</td></tr><tr><td>e o</td><td>e e</td><td>+ap/√A-1</td><td>o o</td><td>-AP/√A-1</td><td>+2AP/√A-1</td></tr><tr><td>o e</td><td>o o</td><td>-AP/√A-1</td><td>e e</td><td>+AP/√A-1</td><td>-2AP/√A-1</td></tr></table>

$$
S _ {p} - S _ {n} = - a _ {C} \frac {A - 1}{(A - 1) ^ {1 / 3}} = - a _ {C} (A - 1) ^ {2 / 3}.
$$

Note that in this case we have $D _ { P } = 0$ , because $A = 2 Z$ is necessarily even, corresponding to the first two rows of the table. The difference $S _ { p } - S _ { n }$ is always negative and decreasing with A. Hence larger energy is needed to extract neutrons than protons.

(c) If instead we use $Z = A / 2 . 5$ , approximately valid for heavy nuclei, we obtain

$$
\begin{array}{l} S _ {p} - S _ {n} = - a _ {C} \frac {2 / 2 . 5 A - 1}{(A - 1) ^ {1 / 3}} + a _ {A} \frac {2}{2 . 5} \frac {A}{A - 1} + D _ {P} = \\ = \frac {2}{2 . 5} \left[ - a _ {C} \frac {A - 1 . 2 5}{(A - 1) ^ {1 / 3}} + a _ {A} \frac {A}{A - 1} \right] + D _ {P}. \\ \end{array}
$$

Also in this case the difference $S _ { p } - S _ { n }$ decreases with A. The general treatment is complicated because of the presence of $D _ { P }$ , which can have either sign.

For even-A nuclei ( $\boldsymbol { D } _ { P } = 0$ ) the curve starts from positive values because of the $a _ { A }$ term. In the following figure the $S _ { p } - S _ { n }$ behaviour is shown for even-A nuclei.

![](images/2cb95a582e8561126dcf8e5ccdf9065c56fe353546a85e71a4e8551c7b25c7b2.jpg)

(d) Using (1.13) we get

• $^ { 2 0 } _ { 1 0 } \mathrm { N e } { \mathrm { : } }$ : $S _ { p } - S _ { n } \simeq - 4 . 9 6 \mathrm { M e V } .$   
• $^ { 3 8 } _ { 1 8 } \mathrm { A r }$ : $S _ { p } - S _ { n } \simeq - 2 . 2 8 \mathrm { M e V }$   
$^ { 1 0 6 } _ { 4 6 } \mathrm { { P d } }$ $S _ { p } - S _ { n } \simeq - 1 . 0 2 \ : \mathrm { M e V }$   
$_ { 5 6 } ^ { 1 3 7 } \mathrm { B a }$ $S _ { p } - S _ { n } \simeq + 4 . 1 5 \mathrm { ~ M e V } .$   
$8 0 ^ { 2 0 0 } \mathrm { H g } ; S _ { p } - S _ { n } \simeq - 0 . 2 4 8 \mathrm { M e V } .$

Apart the fourth nucleus, $_ { 5 6 } ^ { 1 3 7 } \mathrm { B a }$ , all nuclei are even A and the values of the separation differences can be interpreted looking at the figure. The nuclei reported in the list increase with $A$ and show a transition from case (a) to case (b). The two assumptions are strictly valid only for the first and last nuclei. The arrow in the figure sketches the transition region.

# 1.4 Nuclear Decays

# Exercise 1.4.1

Denoting by $T _ { \alpha }$ the kinetic energy of the emitted $\alpha$ -particle, we have approximately

$$
Q _ {\alpha} \simeq \frac {A}{A - 4} T _ {\alpha}.
$$

Hence the $Q _ { \alpha }$ values are

$$
Q _ {1} \simeq \frac {2 4 0}{2 3 6} \times 5. 1 7 \simeq 5. 2 6 \mathrm {M e V}
$$

$$
Q _ {2} \simeq \frac {2 4 0}{2 3 6} \times 5. 1 2 \simeq 5. 2 1 \mathrm {M e V}
$$

The $\gamma$ energy corresponds to the difference between $Q _ { 1 }$ $^ { 2 4 0 } \mathrm { P u } \ \to \ ^ { 2 3 6 } \mathrm { U } )$ and $Q _ { 2 }$ $^ { 2 4 0 } \mathrm { P u } \to ^ { 2 3 6 } \mathrm { U } ^ { * } .$ ). Hence we get

$$
E _ {\gamma} = Q _ {1} - Q _ {2} = 0. 0 5 \mathrm {M e V}
$$

# Exercise 1.4.2

Calling $\tau _ { 1 }$ and $N _ { 1 }$ the mean lifetime and number of $^ { 2 4 4 } \mathrm { P u }$ nuclei at time $t$ , $\tau _ { 2 }$ and $N _ { 2 }$ the same quantities for $^ { 2 4 0 } \mathrm { U }$ and $\tau _ { 3 }$ and $N _ { 3 }$ the same quantities for $^ { 2 4 0 } \mathrm { N p }$ , we have $\tau _ { 1 } \gg \tau _ { 2 }$ , $\tau _ { 3 }$ . Furthermore if $t$ corresponds to the time of the measurement $( = 3 0 \mathrm { d }$ ), we have also $t \ll \tau _ { 1 }$ . Under these conditions the secular equilibrium equation2 holds

$$
\frac {N _ {1}}{\tau_ {1}} \simeq \frac {N _ {2}}{\tau_ {2}} \simeq \frac {N _ {3}}{\tau_ {3}}.
$$

The source has a mass of 1 mol and then $N _ { 1 } = N _ { A }$ , with $N _ { A }$ the Avogadro number

$$
\begin{array}{l} N ^ {(2 4 0} U) = N _ {2} = \frac {\tau_ {2}}{\tau_ {1}} N _ {1} = \frac {T _ {2} ^ {(1 / 2)}}{T _ {1} ^ {(1 / 2)}} N _ {A} \simeq \frac {1 4 h \times 6 . 0 2 \cdot 1 0 ^ {2 3}}{8 . 1 \cdot 1 0 ^ {7} \times 3 6 5 \times 2 4 h} \simeq 1. 2 \cdot 1 0 ^ {1 3} \\ N ^ {(2 4 0} N p) = N _ {3} = \frac {\tau_ {3}}{\tau_ {1}} N _ {1} = \frac {T _ {3} ^ {(1 / 2)}}{T _ {1} ^ {(1 / 2)}} N _ {A} \simeq \\ \simeq \frac {6 7 \min  \times 6 . 0 2 \cdot 1 0 ^ {2 3}}{8 . 1 \cdot 1 0 ^ {7} \times 3 6 5 \times 2 4 \times 6 0 \min } \simeq 9. 4 \cdot 1 0 ^ {1 1} \\ \end{array}
$$

The decays involved in the chain are

$$
{ } _ { 9 4 } ^ { 2 4 4 } \mathrm { P u } \rightarrow { } _ { 9 2 } ^ { 2 4 0 } \mathrm { U } + \alpha
$$

$$
{ } _ { 9 2 } ^ { 2 4 0 } \mathrm { U } \rightarrow { } _ { 9 3 } ^ { 2 4 0 } \mathrm { N p } + e ^ { - } + \bar { \nu } _ { e }
$$

$$
{ } _ { 9 3 } ^ { 2 4 0 } \mathrm { N p } \rightarrow { } _ { 9 4 } ^ { 2 4 0 } \mathrm { P u } + e ^ { - } + \bar { v } _ { e } .
$$

The activity measured in the $\alpha$ -decay is

$$
\mathcal {A} = \left| \frac {d N _ {1}}{d t} \right| \simeq \frac {N _ {1}}{\tau_ {1}} = \frac {N _ {1} \ln 2}{T _ {1} ^ {(1 / 2)}} \simeq \frac {6 . 0 2 \cdot 1 0 ^ {2 3} \times 0 . 6 9}{8 . 1 \cdot 1 0 ^ {7} \times 3 6 5 \times 2 4 \times 3 6 0 0 \mathrm {s}} \simeq 1. 6 \cdot 1 0 ^ {8} \mathrm {s} ^ {- 1}.
$$

# Exercise 1.4.3

The decay constant of $^ { 2 2 6 } \mathrm { R a }$ is

$$
\omega = \frac {\ln 2}{T _ {1 / 2}} \simeq \frac {0 . 6 9 3}{1 . 6 \times 1 0 ^ {3} \times 3 . 1 5 \times 1 0 ^ {7} \mathrm {s}} \simeq 1. 4 1 0 ^ {- 1 1} \mathrm {s} ^ {- 1}.
$$

The activity of a source is given by

$$
\mathcal {A} (t) = \left| \frac {d N}{d t} \right| = \omega N (t) = \omega N _ {0} e ^ {- \omega t} \quad [ s ^ {- 1} ]
$$

The number of $^ { 2 2 6 } \mathrm { R a }$ nuclei at time 0 is

$$
N _ {0} = \frac {N _ {A}}{A} = \frac {6 . 0 2 \times 1 0 ^ {2 3}}{2 2 6} \simeq 2. 6 6 \times 1 0 ^ {2 1}
$$

Hence we have

$$
\mathcal {A} (0) = \omega N _ {0} \simeq 1. 4 1 0 ^ {- 1 1} \times 2. 6 6 1 0 ^ {2 1} \simeq 3. 7 1 0 ^ {1 0} \mathrm {s} ^ {- 1}.
$$

Note that this is the definition of 1 Curie (1 Ci).

# Exercise 1.4.4

The $_ { 6 } ^ { 1 4 } \mathrm { C }$ beta decay is $_ { 6 } ^ { 1 4 } \mathrm { C } \to _ { 7 } ^ { 1 4 } \mathrm { N } + e ^ { - } + \bar { \nu } _ { e }$ . The specimen activity is given by

$$
\mathcal {A} = \left| \frac {d N}{d t} \right| = \frac {\mathrm {N} ^ {(1 4} C)}{\tau^ {(1 4} \mathrm {C)}}.
$$

The number of $_ { 6 } ^ { 1 4 } \mathrm { C }$ nuclei present in the specimen when it was still a living organism is

$$
N _ {0} (^ {1 4} \mathrm {C}) = f \times N _ {0} (\mathrm {C}) = f \times m \times \frac {N _ {A}}{\langle A (\mathrm {C}) \rangle} \simeq 1. 3 \cdot 1 0 ^ {- 1 2} \times 5 \times \frac {6 . 0 2 \cdot 1 0 ^ {2 3}}{1 2 . 0 0 1} \simeq 3. 3 \cdot 1 0 ^ {1 1},
$$

where $f$ is the fraction of $_ 6 ^ { 1 4 } \mathrm { C }$ nuclei in a living organism, m its mass, $N _ { A }$ the Avogadro number and $ { \langle A ( \mathbf { C } ) \rangle }$ the atomic mass of natural carbon. The $_ 6 ^ { 1 4 } \mathrm { C }$ mean lifetime is $\tau ( { } ^ { 1 4 } \mathbf { C } ) = T _ { 1 / 2 } ( { } ^ { 1 4 } \mathbf { C } ) / \ln 2 \simeq 8 2 0 0$ years. Hence we have for the specimen activity when the organism died

$$
\mathcal {A} _ {0} = \frac {N _ {0} (^ {1 4} \mathrm {C})}{\tau (^ {1 4} \mathrm {C})} \simeq \frac {3 . 3 \cdot 1 0 ^ {1 1}}{8 2 0 0 \times 3 . 1 5 \cdot 1 0 ^ {7} \mathrm {s}} \simeq 1. 2 8 \mathrm {s} ^ {- 1},
$$

The present activity is related to ${ \mathcal { A } } _ { 0 }$ through the equation

$$
\mathcal {A} (t) = \mathcal {A} _ {0} \cdot e ^ {- t / \tau^ {(1 4 C)}} = \frac {3 6 0 0}{2 \times 3 6 0 0 \mathrm {s}} \simeq 0. 5 \frac {\text {d e c a y s}}{\mathrm {s}},
$$

hence we get the age of the fossil

$$
T = - \tau (^ {1 4} \mathrm {C}) \times \ln \frac {\mathcal {A} (t)}{\mathcal {A} _ {0}} \simeq - 8 2 0 0 \mathrm {y r} \times \ln \frac {0 . 5}{1 . 2 8} \simeq 7 7 0 0 \mathrm {y r}.
$$

# Exercise 1.4.5

The nucleus $^ { 2 2 6 } \mathrm { R a }$ has a decay constant given by

$$
\omega = \frac {\ln 2}{T _ {1 / 2}} = \frac {0 . 6 9 3}{1 . 6 \times 1 0 ^ {3} \times 3 . 1 5 \times 1 0 ^ {7} \mathrm {s}} \simeq 1. 4 1 0 ^ {- 1 1} \mathrm {s} ^ {- 1}.
$$

For $1 \mathrm { g }$ of $^ { 2 2 6 } \mathrm { R a }$ we have then an activity

$$
\mathcal {A} = \left| \frac {d N}{d t} \right| = \omega N _ {0} = \omega \frac {N _ {A}}{A} \times 1 \simeq 1. 4 1 0 ^ {- 1 1} \times \frac {6 . 0 2 \times 1 0 ^ {2 3}}{2 2 6} \simeq 3. 7 1 0 ^ {1 0} \mathrm {s} ^ {- 1}.
$$

This is the current definition of 1 Curie (1 Ci).

The $^ { 6 0 } \mathrm { C o }$ source we are considering has an activity of $1 0 \mathrm { C i }$ , that is $3 . 7 ~ 1 0 ^ { 1 1 } ~ \mathrm { s ^ { - 1 } }$ . If $m$ is its mass we get

$$
m = \mathcal {A} \frac {A}{N _ {A}} \frac {T _ {1 / 2}}{\ln 2} \simeq 3. 7 1 0 ^ {1 1} \times \frac {6 0}{6 . 0 2 \times 1 0 ^ {2 3}} \frac {5 . 2 6 \times 3 . 1 5 \times 1 0 ^ {7}}{0 . 6 9 3} \simeq 8. 8 \mathrm {m g}.
$$

A simpler approach to get the same result is obtained using the following relation, which holds for sources with equal activities

$$
\frac {m _ {1}}{m _ {2}} = \frac {A _ {1}}{A _ {2}} \times \frac {T _ {1 / 2} ^ {(1)}}{T _ {1 / 2} ^ {(2)}}.
$$

This equation can be used in our case knowing that our source has the same activity of $1 0 \mathrm { g }$ of $^ { 2 2 6 } \mathrm { R a } .$ . Hence we get

$$
m _ {\mathrm {C o}} = m _ {\mathrm {R a}} \times \frac {A _ {\mathrm {C o}}}{A _ {\mathrm {R a}}} \times \frac {T _ {1 / 2} ^ {(\mathrm {C o})}}{T _ {1 / 2} ^ {(\mathrm {C u})}} \simeq 1 0 \times \frac {6 0}{2 2 6} \times \frac {5 . 2 6}{1 6 0 0} \simeq 8. 7 \mathrm {m g}.
$$

# Exercise 1.4.6

The numbers of nuclei of the three types are ruled by the following nested equations

$$
\frac {d N _ {1}}{d t} = - \omega_ {1} N _ {1}
$$

$$
\frac {d N _ {2}}{d t} = \omega_ {1} N _ {1} - \omega_ {2} N _ {2}
$$

$$
\frac {d N _ {3}}{d t} = \omega_ {2} N _ {2} - \omega_ {3} N _ {3}.
$$

In our case, the initial conditions are $N _ { 1 } ( 0 ) = N _ { 0 }$ , $N _ { k } ( 0 ) = 0$ and $d N _ { k } / d t ( 0 ) = 0$ for $k = 2 , 3$ . The particular solution for these consitions is

$$
N _ {1} (t) = N _ {0} e ^ {- \omega_ {1} t}
$$

$$
N _ {2} (t) = N _ {0} \frac {\omega_ {1}}{\omega_ {2} - \omega_ {1}} \left(e ^ {- \omega_ {1} t} - e ^ {- \omega_ {2} t}\right)
$$

$$
N _ {3} (t) = N _ {0} \omega_ {1} \omega_ {2} \left[ \frac {e ^ {- \omega_ {1} t}}{(\omega_ {2} - \omega_ {1}) (\omega_ {3} - \omega_ {1})} + \frac {e ^ {- \omega_ {2} t}}{(\omega_ {3} - \omega_ {2}) (\omega_ {1} - \omega_ {2})} + \frac {e ^ {- \omega_ {3} t}}{(\omega_ {1} - \omega_ {3}) (\omega_ {2} - \omega_ {3})} \right].
$$

uhe nucleus 3 is stable and then $\omega _ { 3 } = 0$ and $N _ { 3 } ( t )$ can be written as

$$
N _ {3} (t) = N _ {0} \left[ 1 + \frac {e ^ {- \omega_ {1} t}}{\omega_ {1} / \omega_ {2} - 1} + \frac {e ^ {- \omega_ {2} t}}{\omega_ {2} / \omega_ {1} - 1} \right].
$$

![](images/f87251d637b3ef39dbc00815809021fa7824626e2ecb26f191225fa72331a5dc.jpg)  
Fig. 1.3 Relative abundances for a decay chain with three nuclei having the decay constants given in the figure

In Fig. 1.3 the three nuclear populations are shown as a function of time for the decay constants given in the text. For $t = 1 / 4$ s we obtain

$$
\frac {N _ {3}}{N _ {1}} = \frac {\left[ 1 + \frac {e ^ {- \omega_ {1} t}}{\omega_ {1} / \omega_ {2} - 1} + \frac {e ^ {- \omega_ {2} t}}{\omega_ {2} / \omega_ {1} - 1} \right]}{e ^ {- \omega_ {1} t}} \simeq 1 0. 9.
$$

# Exercise 1.4.7

The fraction of $^ { 2 3 8 } \mathrm { U }$ isotopes decayed in $2 . 5 \ 1 0 ^ { 9 }$ years is

$$
\begin{array}{l} f = 1 - \exp \left(- \frac {t}{\tau}\right) = 1 - \exp \left(- \frac {t \ln 2}{T _ {1 / 2}}\right) \simeq \\ \simeq 1 - \exp \left(-\frac{2.510^{9}\times 0.693}{4.510^{9}}\right)\simeq 32\% \\ \end{array}
$$

The specific activity is the activity per unit mass. Hence we have

$$
a = \frac {\mathcal {A}}{M} = \frac {N _ {A}}{A} \frac {\ln 2}{T _ {1 / 2}} \simeq
$$

$$
\simeq \frac {6 . 0 2 1 0 ^ {2 3}}{2 3 8} \frac {0 . 6 9 3}{4 . 5 1 0 ^ {9} \times 3 . 1 5 1 0 ^ {7}} \simeq 1. 2 3 1 0 ^ {4} \mathrm {s} ^ {- 1} \cdot \mathrm {g} ^ {- 1} \simeq 0. 3 3 \frac {\mu \mathrm {C i}}{\mathrm {g}}
$$

# Exercise 1.4.8

$$
1. _ {2 2} ^ {4 4} \mathrm {T i} \rightarrow \mathrm {\frac {4 0}{2 0}} \mathrm {C a} + \alpha .
$$

This decay is not allowed. Only nuclei having $A \geq 2 0 0$ can fulfill the kinematical conditions for the $\alpha$ -decay.

$$
2. _ {9 5} ^ {2 4 1} \mathrm {A m} \rightarrow \mathrm {\Lambda} _ {9 3} ^ {2 3 7} \mathrm {N p} + \alpha .
$$

This decay is allowed if $Q _ { \alpha } > 0$ . Using the SEMF we obtain

$$
\begin{array}{l} Q _ {\alpha} = M (2 4 1, 9 5) - M (2 3 7, 9 3) - M _ {\alpha} = B (2 3 7, 9 3) - B (2 4 1, 9 5) + B _ {\alpha} \\ = 1 7 9 8 - 1 8 2 0 + 2 8. 3 \simeq 5. 9 1 \mathrm {M e V}. \\ \end{array}
$$

Hence the decay is allowed.

$$
3. _ {5 5} ^ {1 4 1} \mathrm {C s} \rightarrow_ {5 6} ^ {1 4 1} \mathrm {B a} + e ^ {+} + v _ {e}.
$$

This decay is forbidden because charge is not conserved.

$$
4. _ {2 8} ^ {6 9} \mathrm {N i} \rightarrow_ {2 9} ^ {6 9} \mathrm {C u} + e ^ {-} + \bar {\nu} _ {e}.
$$

This decay is allowed, provided that we have $Q _ { \beta - } > 0$ .

$$
\begin{array}{l} Q _ {\beta -} = M (6 9, 2 8) - M (6 9, 2 9) - m _ {e} \\ = 2 8 M _ {p} + 4 1 M _ {n} - B (6 9, 2 8) - 2 9 M _ {p} - 4 0 M _ {n} + B (6 9, 2 9) - m _ {e} \\ = M _ {n} - M _ {p} - m _ {e} + B (6 9, 2 9) - B (6 9, 2 8) \simeq 0. 7 8 2 + 6 0 0. 0 - 5 9 3. 5 \simeq 7. 3 \mathrm {M e V} \\ \end{array}
$$

Hence the decay is allowed.

# Exercise 1.4.9

As in problem 1.4.6, the time evolution of the nuclei involved in the chain is

$$
N _ {1} (t) = N _ {0} e ^ {- \omega_ {1} t}
$$

$$
N _ {2} (t) = N _ {0} \frac {\omega_ {1}}{\omega_ {2} - \omega_ {1}} \left(e ^ {- \omega_ {1} t} - e ^ {- \omega_ {2} t}\right)
$$

$$
N _ {3} (t) = N _ {0} \omega_ {1} \omega_ {2} \left[ \frac {e ^ {- \omega_ {1} t}}{(\omega_ {2} - \omega_ {1}) (\omega_ {3} - \omega_ {1})} + \frac {e ^ {- \omega_ {2} t}}{(\omega_ {3} - \omega_ {2}) (\omega_ {1} - \omega_ {2})} + \frac {e ^ {- \omega_ {3} t}}{(\omega_ {1} - \omega_ {3}) (\omega_ {2} - \omega_ {3})} \right].
$$

In our case the third equation is not used. We have $\omega _ { 1 } = \ln 2 / 2 . 2 5 = 0 . 3 1 \mathrm { \ m i n } ^ { - 1 }$ , $\omega _ { 2 } = \ln 2 / 2 2 . 9 = 0 . 0 3 \mathrm { m i n } ^ { - 1 }$ . The maximum $N _ { 2 }$ is found solving the equation

$$
\begin{array}{l} \frac {d N _ {2}}{d t} = 0 \\ - \omega_ {1} e ^ {- \omega_ {1} t} + \omega_ {2} e ^ {- \omega_ {2} t} = 0 \\ \end{array}
$$

whose solution is

$$
t = \frac {\ln \left(\omega_ {1} / \omega_ {2}\right)}{\omega_ {1} - \omega_ {2}} \simeq 8. 5 \min
$$

The time dependence of the nuclear fractions is shown below.

![](images/8e7f1f9f0f943c434c4f6308f0ab9e5fff125c24d2d74983241f3a20890e3e6a.jpg)

# Exercise 1.4.10

Denoting by $N _ { \mathrm { U } }$ and $N _ { \mathrm { R n } }$ the numbers of $^ { 2 3 8 } \mathrm { U }$ and ${ } ^ { 2 2 2 } \mathrm { R n }$ nuclei, $\omega _ { \mathrm { U } }$ and $\omega _ { \mathrm { R n } }$ their decay constants, the condition of secular equilibrium can be written as

$$
N _ {\mathrm {U}} \omega_ {\mathrm {U}} = N _ {\mathrm {R n}} \omega_ {\mathrm {R n}}.
$$

$\omega _ { \mathrm { R n } }$ is related to the specific activity measurement as

$$
a = \frac {\mathcal {A}}{V} = \frac {N _ {\mathrm {R n}} \omega_ {\mathrm {R n}}}{V} = \frac {N _ {\mathrm {U}} \omega_ {\mathrm {U}}}{V}
$$

where $V$ is the volume of the basement $( 6 0 ~ \mathrm { m } ^ { 3 } .$ ). $N _ { \mathrm { U } }$ can be expressed as the $^ { 2 3 8 } \mathrm { U }$ concentration $\rho _ { \mathrm { U } }$ times the volume from which the Radon gas diffuses

$$
a = \frac {\rho_ {\mathrm {U}} S d \omega_ {\mathrm {U}}}{V},
$$

where $s$ is the surface of the walls $( 9 4 ~ \mathrm { m } ^ { 2 } )$ ) and $d$ is the thickness $( 0 . 0 2 ~ \mathrm { m } )$ of the layer from which the gas diffuses. Hence we have

$$
\rho_ {\mathrm {U}} = \frac {a V}{S d \omega_ {\mathrm {U}}} = \frac {a V T _ {U} ^ {1 / 2}}{S d \ln 2} \simeq \frac {1 0 0 \times 6 0 \times 4 . 5 1 0 ^ {9} \times 3 . 1 5 1 0 ^ {7}}{9 4 \times 0 . 0 2 \times 0 . 6 9 3 \mathrm {m} ^ {3}} \simeq 6. 5 \times 1 0 ^ {2 0} \mathrm {m} ^ {- 3}
$$

# Exercise 1.4.11

The $Q _ { \alpha }$ -value of the decay can be obtained from the alpha decay energy

$$
Q _ {\alpha} = \frac {A}{A - 4} T _ {\alpha} = \frac {2 3 9}{2 3 5} 5. 1 4 4 \simeq 5. 2 3 2 \mathrm {M e V}.
$$

The measured power is equal to the intensity of the alpha decays multiplied by the released energy $( Q _ { \alpha } )$ . Hence we get

$$
I = \frac {W}{Q _ {\alpha}} \simeq \frac {0 . 2 3 1 \mathrm {J o u l e / s}}{5 . 2 3 2 1 0 ^ {6} \mathrm {e V}} \simeq \frac {0 . 2 3 1 \mathrm {J o u l e / s}}{5 . 2 3 2 1 0 ^ {6} 1 . 6 1 0 ^ {- 1 9} \mathrm {J o u l e}} \simeq 2. 7 6 1 0 ^ {1 1} \mathrm {s} ^ {- 1}.
$$

The half-life is then

$$
\begin{array}{l} T _ {1 / 2} = \frac {N \left(^ {2 3 9} \mathrm {P u}\right) \ln 2}{I} = \frac {N _ {A} m \left(^ {2 3 9} \mathrm {P u}\right) \ln 2}{A I} \simeq \\ \simeq \frac {6 . 0 2 1 0 ^ {2 3} \times 1 2 0 \times 0 . 6 9 3}{2 3 9 \times 2 . 7 6 1 0 ^ {1 1}} \simeq 7. 5 7 1 0 ^ {1 1} \mathrm {s} ^ {- 1} \simeq 2 4 0 0 0 \mathrm {y r}. \\ \end{array}
$$

# 1.5 Nuclear Models

# Exercise 1.5.1

The Saxon-Woods potential has the following expression

$$
V (r) = \frac {- V _ {0}}{1 + \exp {\frac {r - R}{d}}},
$$

where $- V _ { 0 }$ , $R$ and $d$ are the three potential parameters, representing respectively the minimum depth, the nuclear radius and the thickness of region where nuclear matter vanishes.

Taken any spherical potential well, a larger radius generates eigenfunctions which are contained in larger volumes. As a consequence the energy levels (i.e. the eigenvalues) decrease. Hence for a nucleus with larger radius we expect lower energy levels.

A more quantitative result cannot be obtained, as the radial Schödinger equation for a Saxon-Woods potential is not analytically integrable. However using the Fermi gas model we can estimate the relative effect. The Fermi energy is:

$$
E _ {F} = \frac {1}{2 m} \left(\frac {\hbar}{r _ {0}}\right) ^ {2} \left(\frac {9 \pi}{8}\right) ^ {2 / 3} \simeq 3 3 \mathrm {M e V}, \tag {1.14}
$$

where $m$ is the nucleon mass and $r _ { 0 } \simeq 1 . 2$ fm is the coefficient of the nuclear radius A-dependence $( R \simeq r _ { 0 } A ^ { 1 / 3 } $ ). This energy represents the maximum kinetic energy of nucleons in the nucleus. The energy of the ground state is obtained as $E _ { \mathrm { G S } } =$ $- V _ { 0 } + E _ { F }$ , with $V _ { 0 } \approx 4 1 \ \mathrm { { M e V } }$ to agree with a binding energy per nucleon of about 8 MeV. From (1.14) increasing by $50 \%$ the nuclear radius one gets

$$
E _ {\mathrm {G S}} = - V _ {0} + E _ {F} (1. 5 r _ {0}) \simeq - 4 1 + 1 5 \simeq - 2 6 \mathrm {M e V},
$$

which has to be compared with $- 8 \mathrm { M e V }$ for the standard radius.

The binding energy is related to the ground state energy (about equal to its absolute value), hence it increases with the nuclear radius.

# Exercise 1.5.2

The carbon isotopes have 6 protons. These are all contained in fully closed shells according to the configuration $( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 }$ . Hence they do not contribute to the spin-parities of the nuclei. These are instead determined by the last neutron shells.

The configurations of the carbon isotopes are

$^ { 1 1 } { \bf C } : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 3 }$   
$^ { 1 2 } { \bf C } : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 }$   
$^ { 1 3 } { \bf C } : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 } ( 1 p _ { 1 / 2 } ) ^ { 1 }$   
$^ { 1 4 } { \bf C } : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 } ( 1 p _ { 1 / 2 } ) ^ { 2 }$

In all cases the last shell has $l = 1$ . We then have for odd-N isotopes

${ } ^ { 1 1 } \mathbf { C } : J = 3 / 2$ , $\begin{array} { r l } { P = ( - 1 ) ^ { 1 } = - } & { { } \Rightarrow J ^ { P } = 3 / 2 ^ { - } } \end{array}$ $P = ( - 1 ) ^ { 1 } = -$   
$^ { 1 3 } \mathrm { C } : J = 1 / 2$ , P = (−1)1 = − ⇒ J P = 1/2−.

Instead for even-N isotopes, all neutrons are paired and then

$^ { 1 2 } { \bf C } , { } ^ { 1 4 } { \bf C } : J = 0 , P = \bar { + } \Rightarrow J ^ { P } = 0 ^ { + }$ $^ { 1 2 } \mathrm { C }$

# Exercise 1.5.3

The first two nuclei are odd-A. Hence their spin and parity is determined by the last unpaired nucleon. The shell configurations are

$_ { 1 6 } ^ { 3 3 } \textbf { S } n : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 } ( 1 p _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 5 / 2 } ) ^ { 6 } ( 2 s _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 3 / 2 } ) ^ { 1 }$   
$_ { 1 9 } ^ { 3 9 } \textbf { K } p : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 } ( 1 p _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 5 / 2 } ) ^ { 6 } ( 2 s _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 3 / 2 } ) ^ { 3 }$   
Both nucleons have $l = 2$ . Their spin and parity are   
${ } _ { 1 6 } ^ { 3 3 } \mathrm { ~ } n : J = 3 / 2 .$ , $P = ( - 1 ) ^ { 2 } = +$ ⇒ J P = 3/2+   
39 K p : J = 3/2, P = (−1)2 = + ⇒ J P = 3/2+   
$^ { 6 4 } _ { 2 8 } \mathrm { N i }$ $J ^ { P } = 0 ^ { + }$

# Exercise 1.5.4

Using the Fermi gas distribution we have

$$
\langle E _ {k} \rangle = \frac {\int_ {0} ^ {p _ {F}} \frac {p ^ {2}}{2 M} d ^ {3} p}{\int_ {0} ^ {p _ {F}} d ^ {3} p} = \frac {4 \pi}{2 M} \frac {\int_ {0} ^ {p _ {F}} p ^ {4} d p}{\int_ {0} ^ {p _ {F}} 4 \pi p ^ {2} d p} = \frac {3}{5} \frac {p _ {F} ^ {2}}{2 M}
$$

where $\begin{array} { r } { p _ { F } = \frac { \hbar } { 2 r _ { 0 } } ( 9 \pi ) ^ { 1 / 3 } } \end{array}$ is the Fermi momentum $\begin{array} { r } { r _ { 0 } = 1 . 2 \mathrm { f m } } \end{array}$ ) and $M$ is the nucleon mass (can be assumed equal for the purpose). Multiplying and dividing by $c ^ { 2 }$ , we obtain

$$
\langle E _ {k} \rangle = \frac {3 (\hbar c) ^ {2} (9 \pi) ^ {2 / 3}}{4 0 r _ {0} ^ {2} M c ^ {2}} \simeq \frac {3 \times 1 9 7 ^ {2} \times 2 8 . 2 7 ^ {2 / 3}}{4 0 \times 1 . 2 ^ {2} \times 9 4 0} \simeq 2 0 \mathrm {M e V}.
$$

This expression does not depend on the content of protons $( Z )$ and neutrons $( N )$ . Therefore the mean kinetic energy is the same for all nuclei.

# Exercise 1.5.5

The nuclear shells involved and the spin-parity of the ground states are

$$
\begin{array}{l} - \frac {1 5}{7} \mathrm {N} \text {o d d - A n u c l e u s}, p: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {1} \Rightarrow J ^ {P} = \frac {1}{2} ^ {-} \\ - \frac {2 7}{1 2} \mathrm {M g} \text {o d d - A n u c l e u s ,} n: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6} (2 s _ {1 / 2}) ^ {1} \Rightarrow J ^ {P} = \frac {1}{2} ^ {+} \\ - \begin{array}{l} 6 0 \\ 2 8 \end{array} \text {N i e v e n - e v e n n u c l e u s} \Rightarrow J ^ {P} = 0 ^ {+} \\ - \frac {8 7}{3 8} \mathrm {S r} \text {o d d - A n u c l e u s}, n: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6} (2 s _ {1 / 2}) ^ {2} (1 d _ {3 / 2}) ^ {4} (1 f _ {7 / 2}) ^ {8} \\ (2 p _ {3 / 2}) ^ {4} (1 f _ {5 / 2}) ^ {6} (2 p _ {1 / 2}) ^ {2} (1 g _ {9 / 2}) ^ {9} \Rightarrow J ^ {P} = \frac {9}{2} ^ {+} \\ \end{array}
$$

# Exercise 1.5.6

All these isotopes can be unstable because of beta decay. Gamma decay is not possible because they are in the ground states. Alpha decay is kinematically forbidden for $A \lesssim 2 0 0$ . To establish if they are stable it is then necessary to evaluate their $Q _ { \beta }$ values.

$_ 8 ^ { 1 5 } \mathrm { O }$ nuclide. We have to calculate $Q _ { - }$ , $Q _ { + }$ and $Q _ { E C }$ respectively for $\beta ^ { - }$ , $\beta ^ { + }$ decays and electron capture (EC). We have

$$
\begin{array}{l} Q _ {-} = - \Delta B _ {-} + 0. 7 8 2 \mathrm {M e V} \\ Q _ {+} = - \Delta B _ {+} - 1. 8 0 4 \mathrm {M e V} \\ Q _ {E C} = Q _ {+} + 1. 0 2 2 \mathrm {M e V} \\ \end{array}
$$

where $\Delta B _ { \mp } \ = \ B ( A , Z ) - B ( A , Z \pm 1 )$ , the difference between the binding energies of the parent and daughter nuclei, can be derived from the SEMF.

We obtain $Q _ { - } < 0$ , instead $Q _ { + } = 2 . 4 4 \mathrm { M e V }$ and $Q _ { E C } = 3 . 4 6 \mathrm { M e V } .$ $_ 8 ^ { 1 5 } \mathrm { O }$ is then unstable and can decay by both $\beta ^ { + }$ -decay and EC.

This isotope is odd-A, so the spin and parity are determined by the unpaired neutron of the last shell. The neutron shell configuration and spin-parity are

$$
n: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {1} \Rightarrow J ^ {P} = 1 / 2 ^ {-}.
$$

In the shell model the magnetic moment is $\mu ~ = ~ g _ { J } ~ J$ . We have an unpaired neutron $( g _ { l } \ = \ 0 , g _ { s } \ = \ - 3 . 8 3 \mathrm { n . m . }$ ) and $g _ { J }$ is given by

$$
g _ {J} = g _ {s} \frac {j (j + 1) - l (l + 1) + s (s + 1)}{2 j (j + 1)} \tag {1.15}
$$

which for $_ 8 ^ { 1 5 } \mathrm { O }$ turns out to be $g _ { J } = 1 . 2 8$ corresponding to a magnetic moment $\mu \simeq 0 . 6 4 \mathrm { n . m }$ .

$_ 8 ^ { 1 6 } \mathrm { O }$ nuclide. This nucleus is even-even. Furthermore it is the well-known stable and most abundant oxygen isotope. Hence we have $J ^ { P } = 0 ^ { + }$ and $\mu = 0$ .

$_ 8 ^ { 1 7 } \mathrm { O }$ nuclide. Evaluating $Q _ { - }$ , $Q _ { + }$ e $Q _ { E C }$ =   = as for the first nuclide we obtain negative values for all of them. Hence $_ 8 ^ { 1 7 } \mathrm { O }$ is stable.

The same nuclide is odd-A. Again the spin and parity are determined by the unpaired neutron of the last shell. The shell configuration and spin-parity are

$$
n: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {1} \Rightarrow J ^ {P} = 5 / 2 ^ {+}.
$$

Using Eq. (1.15) we now get $g _ { J } = - 0 . 7 7$ corresponding to a magnetic moment $\mu \simeq - 1 . 9 2 \mathrm { n . m }$ .

# Exercise 1.5.7

We have odd-A nuclei and so the spin and parity of the ground states are that of the unpaired nucleon. The maximum occupation is 15, corresponding to the neutron number for $^ { 2 9 } _ { 1 4 } \mathrm { S i }$ . The shell sequence up to 20 in the standard shell model, that is with inverse spin-orbit coupling, is

$$
(a) \quad (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6} (2 s _ {1 / 2}) ^ {2} (1 d _ {3 / 2}) ^ {4}.
$$

If instead the spin-orbit coupling were direct (case b) the shell sequence proceeds with increasing $J$ values as

$$
\begin{array}{l l} \text {(b)} & (1 s _ {1 / 2}) ^ {2} (1 p _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 d _ {3 / 2}) ^ {4} (2 s _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6}. \end{array}
$$

For $_ { 3 } ^ { 7 } \mathrm { L i }$ , whose unpaired nucleon is a proton, we have

$$
\begin{array}{l} \left(a\right) \quad p: \left(1 s _ {1 / 2}\right) ^ {2} \left(1 p _ {3 / 2}\right) ^ {1} \quad J ^ {P} = 3 / 2 ^ {-} \\ p: (1 s _ {1 / 2}) ^ {2} (1 p _ {1 / 2}) ^ {1} J ^ {P} = 1 / 2 ^ {-}. \tag {b} \\ \end{array}
$$

For $^ { 2 9 } _ { 1 4 } \mathrm { S i }$ a neutron is unpaired and we have

$$
\begin{array}{l} \left(a\right) \quad n: \left(1 s _ {1 / 2}\right) ^ {2} \left(1 p _ {3 / 2}\right) ^ {4} \left(1 p _ {1 / 2}\right) ^ {2} \left(1 d _ {5 / 2}\right) ^ {6} \left(2 s _ {1 / 2}\right) ^ {1} \quad J ^ {P} = 1 / 2 ^ {+} \\ n: \left(1 s _ {1 / 2}\right) ^ {2} \left(1 p _ {1 / 2}\right) ^ {2} \left(1 p _ {3 / 2}\right) ^ {4} \left(1 d _ {3 / 2}\right) ^ {4} \left(2 s _ {1 / 2}\right) ^ {2} \left(1 d _ {5 / 2}\right) ^ {1} J ^ {P} = 5 / 2 ^ {+} \tag {b} \\ \end{array}
$$

# Exercise 1.5.8

$^ { 5 2 } \mathrm { C r }$ is even-even and then spin-parity is $J ^ { P } = 0 ^ { + }$ . The other $\mathrm { C r }$ isotopes are odd-A and $J ^ { P }$ is that of the unpaired nucleon. The proton number is even, hence only the neutron shell configuration is relevant. We have

$$
\begin{array}{l} { } ^ { 5 1 } \mathrm { C r } \quad 2 7 n : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 } ( 1 p _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 5 / 2 } ) ^ { 6 } ( 2 s _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 3 / 2 } ) ^ { 4 } ( 1 f _ { 7 / 2 } ) ^ { 7 } \\ { } ^ { 5 5 } \mathrm { C r } \quad 3 1 n : ( 1 s _ { 1 / 2 } ) ^ { 2 } ( 1 p _ { 3 / 2 } ) ^ { 4 } ( 1 p _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 5 / 2 } ) ^ { 6 } ( 2 s _ { 1 / 2 } ) ^ { 2 } ( 1 d _ { 3 / 2 } ) ^ { 4 } ( 1 f _ { 7 / 2 } ) ^ { 8 } ( 2 p _ { 3 / 2 } ) ^ { 3 } . \\ \end{array}
$$

Therefore spin and parity of the ground states are

$$
\begin{array}{l} { } ^ { 5 1 } \mathrm { C r } \quad J = 7 / 2 , P = ( - 1 ) ^ { 3 } \Rightarrow J ^ { P } = 7 / 2 ^ { - } \\ { } ^ { 5 5 } \mathrm { C r } \quad J = 3 / 2 , P = ( - 1 ) ^ { 1 } \Rightarrow J ^ { P } = 3 / 2 ^ { - } \\ \end{array}
$$

These two isotopes ate unstable because of $\beta$ decay. To find the possible decay modes we calculate $Q _ { - }$ , $Q _ { + }$ e $Q _ { E C }$ respectively for $\beta ^ { - }$ , $\beta ^ { + }$ and electronic capture (EC). These are

$$
\begin{array}{l} Q _ {-} = - \Delta B _ {-} + 0. 7 8 2 \mathrm {M e V} \\ Q _ {+} = - \Delta B _ {+} - 1. 8 0 4 \mathrm {M e V} \\ \end{array}
$$

$$
Q _ {E C} = Q _ {+} + 1. 0 2 2 \mathrm {M e V},
$$

where $\Delta B _ { \mp } ~ = ~ B ( A , Z ) - B ( A , Z \pm 1 )$ is the binding energy difference corresponding to each decay. To get $\Delta B _ { \mp }$ we use the SEMF.

For the $^ { 5 1 } _ { 2 4 } \mathrm { C r }$ isotope, $Q _ { + }$ and $Q _ { - }$ are both negative, yet we find $Q _ { E C } \simeq 1 . 5 2 -$ $1 . 8 0 4 + 1 . 0 2 2 \simeq 0 . 7 4 ~ \mathrm { M e V } .$ −  This means that $^ { 5 1 } _ { 2 4 } \mathrm { C r }$ transmutes to $_ { 2 3 } ^ { 5 1 } \mathrm { V }$ by electron capture.

For $^ { 5 5 } _ { 2 4 } \mathrm { C r }$ , $Q _ { + }$ and $Q _ { E C }$ are both negative, but $Q _ { - } \simeq 1 . 1 9 + 0 . 7 8 2 \simeq 1 . 9 7 \mathrm { M e V } .$ 24 +  Hence this nucleus decays to $^ { 5 5 } _ { 2 5 } \mathrm { M n }$ by $\beta ^ { - }$ -decay.

# Exercise 1.5.9

(a) $^ { 5 7 } \mathrm { C u } \mathrm { ~ e ~ } ^ { 5 7 } \mathrm { N i }$ are mirror nuclei with a single nucleon (valence nucleon) out of complete shells. The valence nucleon is a proton for $^ { 5 7 } \mathrm { C u }$ and a neutron for $^ { 5 7 } \mathrm { N i }$ . The shell sequence is

$$
1 s _ {1 / 2} 1 p _ {3 / 2} 1 p _ {1 / 2} 1 d _ {5 / 2} 2 s _ {1 / 2} 1 d _ {3 / 2} 1 f _ {7 / 2} 2 p _ {3 / 2} 1 f _ {5 / 2} \dots
$$

The shell configuration up to the valence nucleon (occupancy no. 29) is

$$
(1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6} (2 s _ {1 / 2}) ^ {2} (1 d _ {3 / 2}) ^ {4} (1 f _ {7 / 2}) ^ {8} (2 p _ {3 / 2}) ^ {1}
$$

and the first excited level corresponds to the following shell, $1 f _ { 5 / 2 }$

Hence we have for spin and parity

$$
\mathrm {G S}: l = 1, j = \frac {3}{2} \Rightarrow J ^ {P} = \frac {3}{2} ^ {-}; \quad 1 \mathrm {s t} \operatorname {E x c}: l = 3, j = \frac {5}{2} \Rightarrow J ^ {P} = \frac {5}{2} ^ {-}.
$$

(b) The magnetic moment is $\mu \ : = \ : g _ { j } \ : j$ , where

$$
g _ {j} = g _ {l} \frac {j (j + 1) + l (l + 1) - s (s + 1)}{2 j (j + 1)} + g _ {s} \frac {j (j + 1) - l (l + 1) + s (s + 1)}{2 j (j + 1)}
$$

For $j = l + 1 / 2$ , which holds for both nuclei since the valence nucleus is in ${ { p } _ { 3 / 2 } }$ , the previous equation simplifies to

$$
j g _ {j} = g _ {l} l + g _ {s} / 2
$$

For $^ { 5 7 } \mathrm { C u }$ , substituting the orbital and spin $g$ -factors for a proton, $g _ { l } = 1$ , $g _ { s } = + 5 . 6 \mathrm { n . m . }$ ., we obtain

$$
\mu (^ {5 7} \mathrm {C u}) = j g _ {j} = 1 \times 1 + 5. 6 / 2 = 3. 8 \mathrm {n . m}.
$$

For $^ { 5 7 } \mathrm { N i }$ , having a valence neutron, the $g$ -factors are $g _ { l } = 0$ , $g _ { s } = - 3 . 8 \mathrm { n . m }$ . and we have

$$
\mu (^ {5 7} \mathrm {N i}) = j g _ {j} = 0 \times 1 - 3. 8 / 2 = - 1. 9 \mathrm {n . m}.
$$

(c) $Q _ { \beta ^ { + } }$ is given by $[ \mathcal M ( A , Z ) - \mathcal M ( A , Z - 1 ) - 2 m ] c ^ { 2 }$ , where $M$ denotes the atomic mass and $m$ the electron mass. Since the parent ${ \binom { 5 7 } { 5 } } \mathbf { C u } )$ and daughter $( ^ { 5 7 } \mathrm { { N i } ) }$ nuclei are mirror nuclei, the binding energy difference is only due to the difference in the Coulomb energies. To write the atomic mass difference we have only to subtract3 the mass difference because a proton is exchanged into a neutron after the decay. Hence we can write

$$
\begin{array}{l} \Delta \mathcal {M} c ^ {2} \approx E _ {c} (Z) - E _ {c} (Z - 1) + \left(M _ {p} - M _ {n}\right) c ^ {2} \simeq \\ \simeq \frac {3}{5} \frac {e ^ {2}}{4 \pi \epsilon_ {0} R} [ Z ^ {2} - (Z - 1) ^ {2} ] + (M _ {p} - M _ {n}) c ^ {2} \simeq \frac {3}{5} \frac {\alpha \hbar c}{r _ {0}} \frac {2 Z + 1}{A ^ {1 / 3}} + (M _ {p} - M _ {n}) c ^ {2} \simeq \\ \simeq \frac {3}{5} \frac {1 9 7}{1 3 7 \times 1 . 2} \frac {5 9}{5 7 ^ {1 / 3}} + 9 3 8. 2 7 - 9 3 9. 5 7 \simeq 9. 7 2 \mathrm {M e V} \\ \end{array}
$$

The maximum positron energy is equal to $Q _ { \beta ^ { + } }$ and then we have

$$
T _ {\max } = Q _ {\beta^ {+}} = (\Delta \mathcal {M} - 2 m) c ^ {2} \approx 9. 7 2 - 2 \times 0. 5 1 1 \simeq 8. 7 \mathrm {M e V}.
$$

It is worth to notice that using the SEMF the result is 8.5 MeV.

# Exercise 1.5.10

The shell sequence up to 14 is $1 s _ { 1 / 2 } 1 p _ { 3 / 2 } 1 p _ { 1 / 2 } 1 d _ { 5 / 2 }$

The spin and parity of $_ 8 ^ { 1 7 } \mathrm { O }$ is that of the uncomplete neutron shell:

$$
- _ {8} ^ {1 7} \mathrm {O}, n: (1 d _ {5 / 2}) ^ {1} l = 2, j = \frac {5}{2} \Rightarrow J ^ {P} = \frac {5}{2} ^ {+}.
$$

In the case of $^ { 1 8 } _ { 9 } \mathrm { F } ,$ there are valence nucleons in both proton and neutron shells. Hence the shell model prediction is not unique. The valence shell is the same $1 d _ { 5 / 2 }$ . The resulting spin comes from the angular momentum composition $\textstyle { \frac { 5 } { 2 } } \oplus { \frac { 5 } { 2 } }$ , whereas the parity is the product $( - 1 ) ^ { 2 } \times ( - 1 ) ^ { 2 } = + 1$ . So we have

$$
- _ {9} ^ {1 8} \mathrm {F}, p: (1 d _ {5 / 2}) ^ {1}, \mathrm {n}: (1 d _ {5 / 2}) ^ {1} \Rightarrow J ^ {P} = 0 ^ {+}, 1 ^ {+} 2 ^ {+}, 3 ^ {+}, 4 ^ {+}, 5 ^ {+}.
$$

(From measurements we have $J ^ { P } = 1 ^ { + }$ ).

For the last nucleus we need to extend the shell sequence. The two last shells up to an occupation 82 are $2 d _ { 3 / 2 } 3 s _ { 1 / 2 }$ , instead up to 126 are $1 i _ { 1 3 / 2 } 3 p _ { 1 / 2 }$ . $^ { 2 0 7 } _ { 8 2 } \mathrm { P b } _ { 1 2 5 }$ has a valence neutron in the $3 p _ { 1 / 2 }$ shell. Hence we find

$$
- \begin{array}{c} 2 0 7 \\ 8 2 \end{array} \mathrm {P b}, n: (3 p _ {1 / 2}) ^ {1} l = 1, j = \frac {1}{2} \Rightarrow J ^ {P} = \frac {1}{2} ^ {-}.
$$

# A.2 Solutions of Particle Physics (Chapter 2)

# 2.1 Fundamental Interactions

# Exercise 2.1.1

![](images/8b63f89e74d6e7539393882854a63b82524d30c3955e4f745e5057cc8e3b0619.jpg)

![](images/8614c714fa4f6b8740add5b4bb4b665fbfabc6f947d3f0c337ab5d2753a305ad.jpg)

# Exercise 2.1.2

Let us first convert the cross section from natural to CGS units. In natural units $G _ { F } = 1 . 2 \times 1 0 ^ { - 5 } ~ \mathrm { G e V ^ { - 2 } }$ ; then expressing $\sqrt { s }$ in GeV, we obtain $G _ { F } ^ { 2 } s = 1 . 4 4 \times$ 10−10  √s $\begin{array} { r } { 1 0 ^ { - 1 0 } \left( \frac { \sqrt { s } } { 1 \mathrm { ~ G e V } } \right) ^ { 2 } \mathrm { G e V } ^ { - 2 } } \end{array}$ . To perform the conversion we use the relationship $\hbar c \simeq 1 9 7 \ : \mathrm { M e V } . \mathrm { f m } \simeq 1 . 9 7 \times 1 0 ^ { - 1 4 } \ : \mathrm { G e V } { \cdot } \mathrm { c m }$ , which allows to get $1 / \mathrm { G e V } = 1 . 9 7 \times$ $1 0 ^ { - 1 4 }$ cm. Hence

$$
G _ {F} ^ {2} s = 5. 6 \times 1 0 ^ {- 3 8} \left(\frac {\sqrt {s}}{1 \mathrm {G e V}}\right) ^ {2} \mathrm {c m} ^ {2}.
$$

The CMS square total energy of the $\nu$ -nucleon is given by the invariant $( p _ { \nu } + p _ { p } ) ^ { 2 }$ , where $p _ { \nu }$ and $p _ { p }$ are the 4-momenta of the neutrino and proton respectively. Therefore $s = M _ { p } ^ { 2 } + \stackrel { . . } M _ { \nu } ^ { 2 } + 2 M _ { p } E _ { \nu } .$ : substituting $M _ { \nu } = 0$ and neglecting $M _ { p } ^ { 2 }$ $M _ { p } = 0 . 9 4$ $\mathrm { G e V } / \mathrm { c } ^ { 2 } )$ in the high energy limit, we get

$$
s \simeq 2 M _ {p} E _ {\nu} \simeq 1. 8 8 \left(\frac {E _ {\nu}}{1 \mathrm {G e V}}\right) \mathrm {G e V} ^ {2}
$$

and for the cross section

$$
\sigma \simeq \frac {2 \times 5 . 6 1 0 ^ {- 3 8} \times 1 . 8 8}{2 8 . 2 7} \left(\frac {E _ {v}}{1 \mathrm {G e V}}\right) \simeq 7. 4 \times 1 0 ^ {- 3 9} \left(\frac {E _ {v}}{1 \mathrm {G e V}}\right) \mathrm {c m} ^ {2}.
$$

The number of scatterers (nucleons) per unit volume is $n = \rho / M _ { p } = N _ { A } \rho \simeq 1 . 3 \times$ $1 0 ^ { 2 4 } \mathrm { c m } ^ { - 3 }$ and hence the interaction length is

$$
\lambda = \frac {1}{\sigma n} \simeq 1. 0 \times 1 0 ^ {1 4} \left(\frac {E _ {\nu}}{1 \mathrm {G e V}}\right) ^ {- 1} \mathrm {c m}.
$$

An estimate of the $\nu$ energy above which the Earth becomes opaque is obtained equating such length to the Earth diameter $D = 1 . 2 \times 1 0 ^ { 9 } \mathrm { { c m } }$ . This energy turns out to be $E _ { \nu } > 8 . 3 \times 1 0 ^ { 4 } \mathrm { G e V . }$

# Exercise 2.1.3

$e ^ { + } + e ^ { - }  \mu ^ { + } + \mu ^ { - } : \gamma + Z ^ { 0 }$   
$n  p + e ^ { - } + \bar { \nu } _ { e } : W$   
· $\mu ^ { - }  e ^ { - } + \bar { \nu } _ { e } + \nu _ { \mu } : W$   
$\nu _ { e } + e ^ { - } \to \nu _ { e } + e ^ { - } : W + Z ^ { 0 }$   
• $\nu _ { \mu } + e ^ { - } \to \nu _ { \mu } + e ^ { - } ; Z ^ { 0 }$

# Exercise 2.1.4

All the processes are allowed, except $p + p  K ^ { + } + p$ , which is forbidden because of baryon conservation $( B _ { \mathrm { i n i } } = 2 \neq B _ { \mathrm { f i n } } = 1 _ { . }$ ) and strangeness conservation $S _ { \mathrm { i n i } } =$ $0 \ne S _ { \mathrm { f i n } } = + 1 .$ ). The first two processes

$$
\gamma + \gamma \rightarrow \gamma + \gamma , e ^ {+} + e ^ {-} \rightarrow 4 \gamma
$$

are due to electromagnetic interaction, the third and the fifth ones

$$
p + \bar {p} \rightarrow W ^ {-} + X, \quad v _ {\mu} + e ^ {-} \rightarrow v _ {\mu} + e ^ {-}
$$

to weak interaction. The Feynman diagrams of the allowed reactions are shown below.

![](images/8ec5dbbd3e0e677f4deb63cfeff864d054b08db79e32bcc0e616ec9ad9b72925.jpg)

# Exercise 2.1.5

· $e ^ { + } + e ^ { - }  \gamma + \gamma$ : allowed—e.m. interaction   
： $\pi ^ { - } + n  K ^ { - } + \Lambda$ : forbidden—strangeness not conserved $K ^ { - } = s \bar { u }$ , $\Lambda = u d s$ $\Rightarrow \ S _ { \mathrm { i n i } } = 0 \neq S _ { \mathrm { f i n } } = - 2 ;$ ).  
· $\Sigma ^ { + }  n + e ^ { + } + \nu _ { e }$ : forbidden—weak interaction but two flavors changed $\Sigma ^ { + } =$ uus, $n = u d d `$ ).   
· $\Sigma ^ { + } \to \Lambda + e ^ { + } + \nu _ { e }$ : allowed—weak interaction $( u  d + W ^ { + } )$ ).   
• $\rho ^ { 0 }  K ^ { + } + K ^ { - }$ : forbidden—kinematics $( m _ { \mathrm { f i n } } > m _ { \mathrm { i n i } }$ ).   
• $\bar { \nu } _ { e } + e ^ { - } \to \bar { \nu } _ { e } + e ^ { - }$ : allowed—weak interaction $( W ^ { - } + Z ^ { 0 } )$   
• $\nu _ { e } + e ^ { - } \to \nu _ { e } + e ^ { - }$ : allowed—weak interaction $( W ^ { - } + Z ^ { 0 } )$

The Feynman diagrams for the allowed processes are shown below.

![](images/a746acf3ad83f995647f80c6ef8b12a6a6c43a60e10f60eb29c52cb66f8276be.jpg)

![](images/c7838dc39a75a073cf570ea74777dbb78cf696f1c2eee1e6dee3422473af73db.jpg)

![](images/ea0588f45998eeaee724af60a0fdbe10040881488d2f7e216a6b0cf342a48066.jpg)

![](images/5ea0f002e46b2a9d6edba09852636cc3872ebf3a983fd2a1d0e3d46b2075d65a.jpg)

![](images/b8a60e8c41f40ec1bfd53da6d71618c33e5b6317a8c336f128ce8074004d6afb.jpg)

# Exercise 2.1.6

a. $\pi ^ { - } + p  \Sigma ^ { 0 } + K ^ { 0 }$ : it is a strong interaction process. $X$ must have $Q = 0$ , $B = 0$ and strangeness $S = + 1$ (s) (because $\Sigma ^ { 0 } = u d s$ and then $S = - 1$ ). $K ^ { 0 } = d \bar { s }$ possesses all these features.   
b. $e ^ { + } + n  p + \bar { \nu } _ { e }$ : it is a weak process. $X$ must have $Q = 0$ and electron lepton number $L _ { e } = - 1 .$ Hence it is an $\bar { \nu } _ { e }$ . The same result can be obtained using the neutron beta decay, $n  p + e ^ { - } + \bar { \nu } _ { e }$ , and moving the electron to the initial state.

c. $\Xi ^ { 0 } \to \Lambda + X$ . The missing particle must be a meson. Looking at the particles involved (all hadrons) the decay can be either strong or weak.4

If the decay were strong, the meson should have $Q = 0$ and strangeness $S = - 1$ . It might be a ${ \bar { K } } ^ { 0 }$ , but the system $\Lambda + \bar { K } ^ { 0 }$ is too heavy for the $\Xi ^ { 0 }$ decay. So a strong decay is excluded.

The decay is weak and the strangeness conservation is not holding any more, being replaced by $\Delta S = \pm 1$ : a neutral pion is the right answer. Hence it is $\Xi ^ { 0 } \to \Lambda + \pi ^ { 0 }$ .

# Exercise 2.1.7

The figure below shows the Feynman diagrams for all the processes. It has to be noticed that (a) and (b) can also occur as neutral current processes $Z ^ { 0 }$ instead of $\gamma$ ). This concurrence is more and more important as energy increases.

![](images/d09de8390b5560af638729c9da0ffc1986c8ba609decb766fef5785d9fcc52cf.jpg)

![](images/eeef703f1656700b256b58d2df67af247656b339cbdb7819c0bb5b7507ba343d.jpg)

![](images/79b3a9fb1805909f846bb2d0be2ba6739ec2bea7040d4fff11c2a07ec010f2cc.jpg)

![](images/baf368e53c0fb56a36fd52f212249697ea04af915f8b1270ce08ec359aa1ec82.jpg)

![](images/edee8bd5759b8f591e3b0944c9ca6ccfe651828458023b98066e1654159e1ee5.jpg)

# Exercise 2.1.8

Hereafter is the list of reactions (A for allowed, $\mathbf { F }$ for forbidden, “conservation” is implicit):

1. $\mu ^ { + }  e ^ { + } + \gamma$ : F, violates $L _ { e }$ and $L _ { \mu }$   
2. $e ^ { - }  \nu _ { e } + \gamma$ : F, violates charge.   
3. $p + p  \Sigma ^ { + } + K ^ { + }$ : F, violates B.   
4. $e ^ { + } + e ^ { - }  \gamma$ : F, violates energy.   
5. $\nu _ { \mu } + p \to \mu ^ { + } + n$ : $\mathbf { F }$ , violates $L _ { \mu }$   
6. $\nu _ { \mu } + n  \mu ^ { - } + p$ : A, see figure.

7. $e ^ { + } + n  p + \nu _ { e }$ : F, violates $L _ { e }$   
8. $e ^ { - } + p  n + \nu _ { e }$ : A, see figure.   
9. $\pi ^ { + } \to \pi ^ { 0 } + e ^ { + } + \nu _ { e }$ : A, see figure for one of the possible graphs   
10. $p + \bar { p }  Z ^ { 0 } + X$ : A, a possible case is shown, with $q \bar { q }$ fragmentations omitted.

![](images/437c71e2e42be169d97a2f41a466d8d3f18889882b73b4029caf1c7201f9a54a.jpg)

![](images/200e0904b7db936c8dfc2a5842d02b2d6a6a83fb32c2455214cabca17e0c6856.jpg)

# 2.2 Hadrons

# Exercise 2.2.1

(1) $K ^ { 0 }$ -mesons as in (2.1) are produced in a strong interaction process. The following quantities are then conserved: electric charge $Q$ , baryon number $B$ , lepton number $L$ , strangeness S. Considering the initial state and the $K ^ { 0 }$ in the final state, the requirements for $X$ are $Q = + 2$ , $B = + 2$ , $L = 0$ , S 1. No known particle exists with such numbers. The minimum number of particles composing $X$ is two because two baryons can realize a system with $B = + 2$ . Hereafter a few processes fulfilling these requirements are listed:

$p + p  K ^ { 0 } + p + \Sigma ^ { + }$   
$p + p  K ^ { 0 } + \Delta ^ { + } + \Sigma ^ { + }$   
• p + p → K 0 + 0 + ++ $p + p  K ^ { 0 } + \Sigma ^ { 0 } + \Delta ^ { + + }$

We further notice that the minimum energy (threshold energy) is different for each of the listed processes.

(2) Several experimental set-ups can be used to study reaction (2.1), depending on the quantities to be measured and the particle identification required.

Let us assume that the experimental configuration consists in a beam of protons hitting a fixed target. Since we want to select events including $K ^ { 0 }$ -mesons, the observation of their decays is mandatory. As $K ^ { 0 }$ is neutral, its decay is detected through the observation of the decay particles. One can use various types of detectors positioned downstream of the target (e.g., wire or drift chambers) or imaging detectors acting as target as well (e.g., bubble chamber). With such detectors it is possible to observe the decay into $\pi ^ { + } \pi ^ { - }$ from their tracks. To measure charge and momentum of the pions a suitable magnetic field is the best solution. The detection of the decay into neutral pions is much more challenging, because it requires the observation of the two photons emerging from the quasi immediate $\pi ^ { 0 }$ decay. This can be achieved with a downstream electromagnetic calorimeter or, in the case of a bubble chamber, using a heavy liquid filling (e.g. freon).

The $K ^ { 0 }$ decay follows the exponential decay law $N ( t ) = N _ { 0 } e ^ { - t / \tau }$ , where $N ( t )$ $( N _ { 0 } )$ is the number of particles at time t (time 0) and $\tau$ is the mean lifetime. It can be reasonable to require that $9 9 \%$ of the neutral kaons decay in the detector. This requirement determines the size of the experimental set-up. We have

$$
0. 9 9 = \int_ {0} ^ {T} \frac {d t}{\tau} \frac {N (t)}{N _ {0}} = 1 - e ^ {T / \tau}
$$

hence $T \simeq 4 . 6 \tau$ . Therefore the minimum length of the experimental set-up is

$$
L \simeq 4. 6 \beta \gamma c \tau = 4. 6 c \tau \frac {p}{m} \simeq 0. 7 4 \mathrm {m}.
$$

# Exercise 2.2.2

All the reactions are strong interaction processes. Considering the particles involved we need to check the conservation of the following quantities: electric charge $Q$ , baryon number $B$ and strangeness $s$ .

· $K ^ { - } + p  \Omega ^ { - } + K ^ { + } + K ^ { 0 }$ : allowed;   
• $\psi  \pi ^ { + } + \pi ^ { 0 } + \pi ^ { - }$ : allowed;   
• $\pi ^ { - } + p  \Sigma ^ { + } + K ^ { - }$ : forbidden for $s$ non conservation;   
· $\pi ^ { - } + p  \pi ^ { 0 } + \pi ^ { 0 }$ : forbidden for $B$ non conservation;   
• $p + p  n + \Delta ^ { + + } + p + \bar { p }$ : allowed.

# Exercise 2.2.3

The answers about the decays and the interaction type are

• $\phi \to \rho ^ { 0 } + \pi ^ { 0 }$ : allowed, strong interaction;   
• $\pi ^ { 0 }  e ^ { + } + e ^ { - } + \gamma$ : allowed, e.m. interaction;   
• $\Xi ^ { - } \to \Sigma ^ { 0 } + \mu ^ { - } + \bar { \nu _ { e } }$ : forbidden, violates the electron and muon numbers conservations;   
· $\Sigma ^ { - }  n + \pi ^ { - } ;$ : allowed, weak interaction;   
· $\Xi ^ { - } \to \pi ^ { 0 } + \pi ^ { - }$ : forbidden, violates the baryon number conservation.

# Exercise 2.2.4

To get the $e ^ { + } + e ^ { - }  \mu ^ { + } + \mu ^ { - }$ cross section in $\mathrm { c m } ^ { 2 }$ we simply multiply it by $( \hbar c ) ^ { 2 }$ :

$$
\sigma \left(\mu^ {+} \mu^ {-}\right) = \frac {4 \pi \alpha^ {2}}{3 s} (\hbar c) ^ {2} \simeq \frac {4 3 . 1 4}{3 s} \times \left(\frac {0 . 1 9 7 \mathrm {G e V} \cdot \mathrm {f m}}{1 3 7}\right) ^ {2} \simeq 8 6. 6 \mathrm {n b} \left(\frac {\mathrm {G e V} ^ {2}}{s}\right)
$$

Neglecting strong interaction effects, the cross section into hadrons can be estimated from the ratio $R$

$$
R = \frac {\sigma (\text {h a d r o n s})}{\sigma (\mu^ {+} \mu^ {-})} = C \sum_ {q} Q _ {q} ^ {2}
$$

where $C$ is the number of quark colors (3), $Q _ { q }$ is the charge of the quark $q$ (in $e$ units) and the sum includes those quarks for which $m ( q \bar { q } ) < \sqrt { s }$ . At 2 GeV u, d e s fulfill such condition and then

$$
\sigma (\text {h a d r o n s}) = 3 \times \left(\frac {1}{9} + \frac {4}{9} + \frac {1}{9}\right) \times 8 6. 6 \mathrm {n b} \left(\frac {\mathrm {G e V} ^ {2}}{4 \mathrm {G e V} ^ {2}}\right) \simeq 4 3. 3 \mathrm {n b}
$$

# Exercise 2.2.5

We have

$$
\tau_ {J / \psi} = \frac {\hbar}{\Gamma (J / \psi)} = \frac {\hbar c}{\Gamma (J / \psi) c} \simeq \frac {1 9 7 \mathrm {M e V f m}}{0 . 0 9 1 \mathrm {M e V} 3 1 0 ^ {2 3} \mathrm {f m / s}} \simeq 7. 2 \times 1 0 ^ {- 2 1} \mathrm {s}
$$

The decay time corresponds to a strong interaction decay.

# Exercise 2.2.6

The beam energy is above the energy threshold for the production of strange particles, but below that for producing particles with heavier quarks. Therefore the simplest hypothesis for the event is the associated production of $\Lambda$ and $K ^ { 0 }$ observed through their respective decays into $p + \pi ^ { - }$ and $\pi ^ { + } + \pi ^ { - }$ . Having in mind also the two charged tracks, the simplest interpretation for the event is

$$
\pi^ {+} + p \rightarrow \pi^ {+} + \pi^ {+} + \Lambda + K ^ {0}
$$

To verify the correctness of the interpretation and to assign a specific particle to each $\mathrm { V } ^ { 0 }$ , we assume that the negative track is a $\pi ^ { - }$ , whereas the positive one can be either $p$ (-hypothesis) or $\pi ^ { + }$ ( $K ^ { 0 }$ -hypothesis).

Let us call $\mathrm { v } _ { 1 } ^ { 0 }$ the first vertex. If it is a $\Lambda$ decay, we have

$$
\begin{array}{l} M ^ {2} = m _ {p} ^ {2} + m _ {\pi} ^ {2} + 2 \sqrt {p _ {1 +} ^ {2} + m _ {p} ^ {2}} \sqrt {p _ {1 -} ^ {2} + m _ {\pi} ^ {2}} - 2 p _ {1 +} p _ {1 -} \cos \theta_ {1} = \\ = 0. 9 3 8 ^ {2} + 0. 1 3 9 ^ {2} + 2 \times 1. 0 2 \times 1. 9 0 5 - 2 \times 0. 4 \times 1. 9 \times \cos 2 4. 5 ^ {\circ} \simeq 3. 4 0 \mathrm {G e V} ^ {2} \\ \end{array}
$$

hence $M \simeq 1 . 8 4 \mathrm { G e V } ,$ which is inconsistent with the hypothesis, since it differs by more than $5 \%$ from the $\Lambda$ mass $( 1 . 1 1 6 \mathrm { G e V } / \mathrm { c } ^ { 2 } )$ ).

If $\mathrm { v } _ { 1 } ^ { 0 }$ is a $K ^ { 0 }$ decay, we have

$$
\begin{array}{l} M ^ {2} = m _ {\pi} ^ {2} + m _ {\pi} ^ {2} + 2 \sqrt {p _ {1 +} ^ {2} + m _ {\pi} ^ {2}} \sqrt {p _ {1 -} ^ {2} + m _ {\pi} ^ {2}} - 2 p _ {1 +} p _ {1 -} \cos \theta_ {1} = \\ = 0. 1 3 9 ^ {2} + 0. 1 3 9 ^ {2} + 2 \times 0. 4 2 3 \times 1. 9 0 5 - 2 \times 0. 4 \times 1. 9 \times \cos 2 4. 5 ^ {\circ} \simeq 0. 2 6 7 \mathrm {G e V} ^ {2} \\ \end{array}
$$

hence $M \simeq 0 . 5 1 7 \mathrm { G e V } ,$ , which is consistent with the hypothesis, being within $5 \%$ from the $K ^ { 0 }$ mass $( 0 . 4 9 8 \mathrm { G e V } / \mathrm { c } ^ { 2 } )$ ).

$\mathrm { V } _ { 2 } ^ { 0 }$ is the second vertex. If it is a  decay, we have

$$
\begin{array}{l} M ^ {2} = m _ {p} ^ {2} + m _ {\pi} ^ {2} + 2 \sqrt {p _ {2 +} ^ {2} + m _ {p} ^ {2}} \sqrt {p _ {2 -} ^ {2} + m _ {\pi} ^ {2}} - 2 p _ {2 +} p _ {2 -} \cos \theta_ {2} = \\ = 0. 9 3 8 ^ {2} + 0. 1 3 9 ^ {2} + 2 \times 1. 2 0 \times 0. 2 8 6 - 2 \times 0. 7 5 \times 0. 2 5 \times \cos 2 2 ^ {\circ} \simeq 1. 2 4 \mathrm {G e V} ^ {2} \\ \end{array}
$$

hence $M \simeq 1 . 1 1 \mathrm { G e V } ,$ which differs from the $\Lambda$ mass by less than $5 \%$ .

To further confirm the $\Lambda$ -hypothesis for $\mathrm { V } _ { 2 } ^ { 0 }$ , we calculate the invariant mass for a $K ^ { 0 }$ as

$$
\begin{array}{l} M ^ {2} = m _ {\pi} ^ {2} + m _ {\pi} ^ {2} + 2 \sqrt {p _ {2 +} ^ {2} + m _ {\pi} ^ {2}} \sqrt {p _ {2 -} ^ {2} + m _ {\pi} ^ {2}} - 2 p _ {2 +} p _ {2 -} \cos \theta_ {2} = \\ = 0. 1 3 9 ^ {2} + 0. 1 3 9 ^ {2} + 2 \times 0. 7 6 \times 0. 2 8 6 - 2 \times 0. 7 5 \times 0. 2 5 \times \cos 2 2 ^ {\circ} \simeq 0. 1 2 6 \mathrm {G e V} ^ {2} \\ \end{array}
$$

$M \simeq 0 . 3 5 4 \mathrm { G e V }$ is inconsistent with the $K ^ { 0 }$ mass.

As a conclusion $\mathrm { v _ { 1 } ^ { 0 } }$ is a $K ^ { 0 }$ , $\mathrm { V } _ { 2 } ^ { 0 }$ is a $\Lambda$ .

The lifetime of each particle is

$$
t = \frac {l}{\beta \gamma c} = \frac {l}{c} \times \frac {m}{p}
$$

where $m$ and $p$ are mass and momentum of the decaying particle. We have

$$
\begin{array}{l} p _ {K ^ {0}} = \sqrt {p _ {1 +} ^ {2} + p _ {1 -} ^ {2} + 2 p _ {1 +} p _ {1 -} \cos \theta_ {1}} \simeq \\ \simeq \sqrt {0 . 4 ^ {2} + 1 . 9 ^ {2} + 2 \times 0 . 4 \times 1 . 9 \times \cos 2 4 . 5 ^ {\circ}} \simeq 2. 2 7 \mathrm {G e V / c} \\ p _ {\Lambda} = \sqrt {p _ {2 +} ^ {2} + p _ {2 -} ^ {2} + 2 p _ {2 +} p _ {2 -} \cos \theta_ {2}} \simeq \\ \simeq \sqrt {0 . 7 5 ^ {2} + 0 . 2 5 ^ {2} + 2 \times 0 . 7 5 \times 0 . 2 5 \times \cos 2 2 ^ {\circ}} \simeq 0. 9 9 \mathrm {G e V / c} \\ \end{array}
$$

and the lifetimes are

$$
t _ {K ^ {0}} \simeq \frac {3 7 \mathrm {c m}}{3 \times 1 0 ^ {1 0} \mathrm {c m / s}} \times \frac {0 . 4 9 8}{2 . 2 7} \simeq 2. 7 1 0 ^ {- 1 0} \mathrm {s}
$$

$$
t _ {\Lambda} \simeq \frac {1 1 \mathrm {c m}}{3 \times 1 0 ^ {1 0} \mathrm {c m / s}} \times \frac {1 . 1 1 6}{0 . 9 9} \simeq 4. 1 1 0 ^ {- 1 0} \mathrm {s}
$$

# Exercise 2.2.7

a. Forbidden: strangeness is not conserved.   
b. Forbidden: electric charge is not conserved.   
c. Allowed.   
d. Forbidden: energy is not conserved.   
e. Forbidden: strangeness is not conserved.   
f. Allowed.

# Exercise 2.2.8

a. $\Sigma ^ { 0 }$ decays by electromagnetic interaction. For this interaction the quark flavor is conserved as for the strong interaction. The strangeness conserving decay is possible because a lighter baryon with the same strangeness does exist. The $\Sigma ^ { 0 } \to \Lambda$ decay would be also possible by strong interaction if accompanied by $\pi ^ { 0 }$ , but there is not enough energy $[ M ( \Sigma ^ { 0 } ) < M ( \Lambda ) + M ( \pi ^ { 0 } ) ]$ . The electromagnetic decay is instead possible with the emission of a photon, which is kinematically allowed. The mean lifetime reflects the nature of the interaction.   
b. $\Sigma ^ { + }$ cannot decay by strong interaction for the same reason as above $[ M ( \Sigma ^ { + } ) <$ $M ( \Lambda ) + M ( \pi ^ { + } ) ]$ . Nor can decay by e.m. interaction because there is no lighter charged baryon with $S = - 1$ . Hence it decays by weak interaction as shown by the mean lifetime.   
c. Any diagram with a quark (among u, d and $s$ ) emitting a photon, because the quark contents of $\Sigma ^ { 0 }$ and $\Lambda$ are the same and there is no flavor change.

# Exercise 2.2.9

(a) Denoting by ${ \pmb { \sigma } } _ { \pmb { \Lambda } }$ and ${ \pmb p } _ { \pmb { \Lambda } }$ the $\Lambda$ spin and momentum, and by ${ \pmb p } _ { \pmb K }$ the $K ^ { 0 }$ momentum, the vector product $\pmb { t } = \pmb { \sigma } _ { \pmb { \Lambda } } \times ( \pmb { p } _ { \pmb { \Lambda } } \times \pmb { p } _ { K } )$ is parallel to the scattering plane and proportional to the $\Lambda$ spin value. Hence it is proportional to the component of the spin in this plane. $\pmb { t }$ is an axial vector and then must be zero if parity is conserved $t \to - t$ under parity transformation). This is the case for the strong reaction $\pi ^ { - } + p  \Lambda + K ^ { 0 }$ . Being null the spin component in the scattering plane, the $\Lambda$ spin can only be normal to this plane.   
(b) Using the star superscript for center-of-momentum system (CMS) kinematic variables, we have the following relations

$$
\epsilon_ {\pi} = \sqrt {\boldsymbol {p} _ {\pi} ^ {2} + m _ {\pi} ^ {2}} = \sqrt {p _ {\pi} ^ {2} + m _ {\pi} ^ {2}} \simeq 1. 0 1 \mathrm {G e V / c}
$$

$$
E ^ {*} = \epsilon_ {\pi} ^ {*} + \epsilon_ {p} ^ {*} = \sqrt {m _ {\pi} ^ {2} + m _ {p} ^ {2} + 2 m _ {p} \epsilon_ {\pi}} \simeq 1. 6 7 \mathrm {G e V}
$$

$$
\begin{array}{l} \beta_ {\mathrm {C M}} = | \boldsymbol {p} _ {\pi} | / (\epsilon_ {\pi} + \epsilon_ {p}) = p _ {\pi} / (\epsilon_ {\pi} + m _ {p}) \simeq 0. 5 1 3 \\ \gamma_ {\mathrm {C M}} = \left(\epsilon_ {\pi} + \epsilon_ {p}\right) / E ^ {*} \simeq 1. 1 6 \\ p ^ {*} = | \pmb {p} ^ {*} | = \frac {\sqrt {[ E ^ {* 2} - (m _ {\Lambda} + m _ {K}) ^ {2} ] [ E ^ {* 2} - (m _ {\Lambda} - m _ {K}) ^ {2} ]}}{2 E ^ {*}} \simeq 0. 2 0 3 \mathrm {G e V / c m ^ {2}} \\ \epsilon_ {\Lambda} ^ {*} = \sqrt {p ^ {* 2} + m _ {\Lambda} ^ {2}} \simeq 1. 1 3 \mathrm {G e V}. \\ \end{array}
$$

$\theta = 0$ in the Laboratory system (LS) corresponds to $\theta ^ { * } = 0$ in the CMS. Hence the $\Lambda$ momentum in the LS is

$$
p _ {\Lambda} = \gamma_ {\mathrm {C M}} \left(p ^ {*} + \beta_ {\mathrm {C M}} \cdot \epsilon_ {\Lambda} ^ {*}\right) \simeq 0. 9 1 5 \mathrm {G e V / c}
$$

The mean decay path of the $\Lambda$ -particle is

$$
\lambda_ {\Lambda} = c \tau_ {\Lambda} \cdot \beta_ {\Lambda} \gamma_ {\Lambda} = c \tau_ {\Lambda} \cdot \frac {p _ {\Lambda}}{m _ {\Lambda}} \simeq 6. 4 7 \mathrm {c m}
$$

and the probability that it decays before reaching the detector is

$$
P (<  L) = \frac {1}{\lambda_ {\Lambda}} \int_ {0} ^ {L} \exp (- l / \lambda_ {\Lambda}) d l \simeq 1 - \exp (- 1 0 / 6. 4 7) \simeq 7 9 \%
$$

(c) The precession angle at distance $L$ from the target is

$$
\phi = \omega t = \omega \frac {L}{v _ {\Lambda}} = \omega \frac {L}{\beta_ {\Lambda} c},
$$

where $\omega$ is the Larmor angular frequency

$$
\omega = \frac {\mu_ {\Lambda} B}{\hbar}.
$$

Hence we have

$$
\begin{array}{l} \phi = \frac {\mu_ {\Lambda} B L}{\hbar c} \frac {E _ {\Lambda}}{p _ {\Lambda}} \simeq \frac {0 . 6 1 \times 3 . 1 5 1 0 ^ {- 1 4} \mathrm {M e V / T} \times 2 0 \mathrm {T} \times 1 0 \mathrm {c m}}{1 9 7 1 0 ^ {- 1 3} \mathrm {M e V c m}} \times \frac {\sqrt {0 . 9 1 5 ^ {2} + 1 . 1 1 6 ^ {2}}}{0 . 9 1 5} \simeq \\ \simeq 0. 3 0 8 \mathrm {r a d} \simeq 1 7. 6 ^ {\circ} \\ \end{array}
$$

(d) The decay asymmetry is defined as

$$
f _ {+} = \frac {\int_ {0} ^ {1} N (\cos \theta^ {*}) d \cos \theta^ {*}}{\int_ {- 1} ^ {1} N (\cos \theta^ {*}) d \cos \theta^ {*}} = \frac {(x - \alpha x ^ {2} / 2) | _ {0} ^ {1}}{(x - \alpha x ^ {2} / 2) | _ {- 1} ^ {1}} = \frac {1}{2} \left(1 - \frac {\alpha}{2}\right).
$$

Thus we have for the asymmetry parameter $\alpha$ :

$$
\alpha = 2 (1 - 2 f _ {+}) \simeq 0. 7 2
$$

(e) The decay asymmetry is a consequence of the parity non conservation in weak interactions, as for the decay $\Lambda  \pi ^ { - } + p$ . In fact we have $N ( \theta ^ { * } ) \ \ne \ N ( \pi - \theta ^ { * } )$ .

# Exercise 2.2.10

The event in the text is interpreted as $\pi ^ { - } + p  \Lambda + K ^ { 0 }$ . From momentum conservation, $\pmb { p } _ { \pi } = \pmb { p } _ { \Lambda } + \pmb { p } _ { K }$ , we derive the $\Lambda$ momentum

$$
\boldsymbol {p} _ {\Lambda} = \boldsymbol {p} _ {\pi} - \boldsymbol {p} _ {K}
$$

whose absolute value is

$$
\begin{array}{l} p _ {\Lambda} = \sqrt {\boldsymbol {p} _ {\pi} ^ {2} + \boldsymbol {p} _ {K} ^ {2} - 2 | \boldsymbol {p} _ {\pi} | | \boldsymbol {p} _ {K} | \cos \theta_ {K}} \simeq \\ \simeq \sqrt {1 . 5 ^ {2} + 0 . 5 2 ^ {2} - 2 \times 1 . 5 \times 0 . 5 2 \times \cos 5 8 ^ {\circ}} \simeq 1. 3 \mathrm {G e V / c} \\ \end{array}
$$

a. Assuming that the particles decayed from the second $\mathrm { V } ^ { 0 }$ are a proton (with momentum $p _ { + }$ ) and a negative pion (with momentum $p _ { - }$ ), the square of the invariant mass is

$$
\begin{array}{l} M ^ {2} = m _ {p} ^ {2} + m _ {\pi} ^ {2} + 2 \sqrt {p _ {+} ^ {2} + m _ {p} ^ {2}} \sqrt {p _ {-} ^ {2} + m _ {\pi} ^ {2}} - 2 p _ {+} p _ {-} \cos (\theta_ {+} + \theta_ {-}) = \\ = 0. 9 3 8 ^ {2} + 0. 1 4 0 ^ {2} + 2 \times 1. 3 1 \times 0. 2 5 - 2 \times 0. 9 2 \times 0. 2 1 \times \cos 1 8 ^ {\circ} \simeq 1. 1 9 5 \mathrm {G e V} ^ {2} \\ \end{array}
$$

Hence the invariant mass is $\sqrt { 1 . 1 9 5 } ~ \simeq ~ 1 . 0 9 \mathrm { G e V }$ which does not correspond to a $\Lambda$ -particle. The invariant mass is smaller: this implies that (at least) a neutral particle is not observed in the decay (as hypothesized in b.). This fact can be put in evidence using the momentum conservation in the longitudinal direction (i.e. along the $\Lambda$ momentum). The total longitudinal momentum of the decay products is

$$
p _ {+} \cos \theta_ {+} + p _ {-} \cos \theta_ {-} = 0. 9 2 \cos 4 ^ {\circ} + 0. 2 1 \cos 1 4 ^ {\circ} \simeq 1. 1 2 \mathrm {G e V / c}
$$

which is smaller than the $\Lambda$ momentum $( 1 . 3 \mathrm { G e V } / \mathrm { c } )$ by more than $5 \% \sqrt { 2 }$ .

Finally we notice that the text did not provide the azimuthal angles of the decay products. Having these angles it would have been possible to evaluate the momentum vectors of these particles. The best way to verify the presence of unobserved neutrals is showing that $\pmb { p } _ { \Lambda } , \pmb { p } _ { + }$ and $\pmb { p } _ { - }$ are not lying in the same plane or equivalently the sum of the proton and pion transverse momenta is not zero.

b. If a neutrino is the missing neutral particle, its longitudinal momentum is

$$
(p _ {v}) _ {L} = p _ {\Lambda} - \left(p _ {+} \cos \theta_ {+} + p _ {-} \cos \theta_ {-}\right) \simeq 1. 3 - 1. 1 2 = 0. 1 8 \mathrm {G e V / c}
$$

c. The $\Lambda$ lifetime is

$$
t = \frac {l}{\beta \gamma c} = \frac {l}{c} \frac {m _ {\Lambda}}{p _ {\Lambda}} \simeq \frac {1 0 \mathrm {c m}}{3 1 0 ^ {1 0} \mathrm {c m / s}} \frac {1 . 1 1 6}{1 . 3} \simeq 2. 0 4 1 0 ^ {- 1 0} \mathrm {s}.
$$

# Exercise 2.2.11

(a) In the quark model baryons are 3-quark systems. Since quarks are fermions with spin 1/2, baryons must have a half-integer spin.   
(b) An antibaryon is constituted of 3 antiquarks whose charges are either $- 2 / 3$ or $+ 1 / 3$ . Hence the maximum charge is $+ 1 \left[ = 3 \times ( + 1 / 3 ) \right]$ .   
(c) A meson is a quark-antiquark system. To get $S = - 1$ , the quark must be $s$ whose charge is $Q _ { q } = - 1 / 3$ . It follows that the charge of the meson can be either $^ { - 1 }$ $Q _ { \bar { q } } = - 2 / 3 )$ ) or 0 ( $Q _ { \bar { q } } = + 1 / 3$ ).

# Exercise 2.2.12

(a) Mesons are $q \bar { q }$ , the charges are $+ 2 / 3$ and $- 1 / 3$ for $q$ and $- 2 / 3$ and $+ 1 / 3$ for $\bar { q }$ . Combining the four possible cases, one finds that the charges for mesons are 1, 0 and $+ 1$ .   
(b) Antibaryons are ${ \bar { q } } { \bar { q } } { \bar { q } }$ . Again there are four possible cases which are $- 2 , - 1 , 0$ , $+ 1$ .

# 2.3 Weak and Electro-Weak Interactions

# Exercise 2.3.1

The neutrino mean free path in Iron is

$$
\lambda = \frac {1}{n _ {p} \sigma_ {\nu}}
$$

where $n _ { p } = \rho _ { F e } / m _ { p }$ is the number of nucleons per unit volume. We have

$$
n _ {p} \simeq \frac {7 . 9 \mathrm {g} / \mathrm {c m} ^ {3}}{1 . 6 7 1 0 ^ {- 2 4} \mathrm {g}} \simeq 4. 7 \times 1 0 ^ {2 4} \mathrm {c m} ^ {- 3} \quad \lambda = 7. 1 \times 1 0 ^ {1 0} \mathrm {c m}
$$

Then, if $f = 1 / 1 0 ^ { 9 }$ is the fraction of interacting neutrinos, the corresponding thickness is

$$
L = f \lambda = 7 1 \mathrm {c m}
$$

# Exercise 2.3.2

For an estimate of the branching ratios we assume that they are simply proportional to the transition rates as given by the Fermi golden rule. Hence we have

$$
\frac {B R (D ^ {0} \to K ^ {-} e ^ {+} \nu_ {e})}{B R (D ^ {0} \to \pi^ {-} e ^ {+} \nu_ {e})} \simeq \frac {| \mathcal {M} (D ^ {0} \to K ^ {-} e ^ {+} \nu_ {e}) | ^ {2}}{| \mathcal {M} (D ^ {0} \to \pi^ {-} e ^ {+} \nu_ {e}) | ^ {2}} \times \frac {\rho (D ^ {0} \to K ^ {-} e ^ {+} \nu_ {e})}{\rho (D ^ {0} \to \pi^ {-} e ^ {+} \nu_ {e})},
$$

where $M$ denotes the transition amplitude and $\rho$ the phase space factor. In the first ratio all the terms cancel but the effective coupling constants. These are $g _ { w } \cos \theta _ { C }$ for $D ^ { 0 } \to K ^ { - }$ $( c \to s + W ^ { + } )$ ) and $g _ { w } \sin \theta _ { C }$ for $D ^ { 0 } \to \pi ^ { - }$ , $( c  d + W ^ { + } )$ ), where $g _ { w }$ is the weak coupling constant and $\theta _ { C }$ is the Cabibbo angle $( \sin \theta _ { C } \simeq 0 . 2 2 )$ ).

The phase space terms can be estimated using the so called Sargent rule, originally established for the beta decay, taking into account the kinematic analogy of the present decays with the beta case. Following this rule we have $w \propto E _ { 0 } ^ { 5 }$ , where $w$ is the transition rate and $E _ { 0 }$ is the energy available in the decay $( = m _ { n } - m _ { p } - m _ { e }$ , for the beta decay $n  p + e ^ { - } + \bar { \nu _ { e } } )$ . We also recall that in the Fermi theory the beta decay is only ‘kinematical’, that means that the energy dependence is only due to phase space. Therefore for the phase space we can write $\rho \propto E _ { 0 } ^ { 5 }$ . Under this assumption we have

$$
\frac {B R \left(D ^ {0} \rightarrow K ^ {-} e ^ {+} v _ {e}\right)}{B R \left(D ^ {0} \rightarrow \pi^ {-} e ^ {+} v _ {e}\right)} = \frac {\cos^ {2} \theta_ {C}}{\sin^ {2} \theta_ {C}} \times \left(\frac {m _ {D} - m _ {K} - m _ {e}}{m _ {D} - m _ {\pi} - m _ {e}}\right) ^ {5} \simeq 2 0 \times 0. 3 2 \simeq 6. 4
$$

Despite the crudeness of the estimate, this results differs from the experimental value by only $40 \%$ .

# Exercise 2.3.3

The Feynman diagrams are reported below

![](images/ab2bb874939178638da201c3a0259e2aec74c45d599cf7dd2e591fd93ca8114a.jpg)

![](images/ccee31c54842b8628440b8f2680602954ce0d800d1047e65c672f2ad8014c809.jpg)

![](images/29d7bea0041760218f456933f83bf6fec9d802126e09ee4160e20bd69fc40afe.jpg)

![](images/dcb4e12b8356e160e66fab488f1406cbd550a791570d94f2b1fe3f5f1f06c1ea.jpg)

# Exercise 2.3.4

$\diamond$ The beta decay rate in the limit of the Sargent rule, i.e. assuming $E \gg m c ^ { 2 }$ and substituting $E _ { 0 }$ with $T _ { \mathrm { m a x } } ( \simeq 0 . 7 8 2 \ : \mathrm { M e V } )$ is

$$
\omega = \frac {G _ {F} ^ {2}}{2 \pi^ {3} \hbar^ {7} c ^ {6}} \frac {T _ {\operatorname* {m a x}} ^ {5}}{3 0}. \tag {2.1}
$$

The squared Fermi constant (divided by $( \hbar c ) ^ { 3 }$ , as it is usually expressed) is

$$
\left[ \frac {G _ {F}}{(\hbar c) ^ {3}} \right] ^ {2} = \frac {\omega 2 \pi^ {3} (\hbar c) 3 0}{c T _ {\max} ^ {5}} = \frac {\frac {1}{8 8 6 \mathrm {s}} \times 6 2 \times 1 9 7 \mathrm {M e V f m} \times 3 0}{3 \cdot 1 0 ^ {2 3} \mathrm {f m s} ^ {- 1} \times (0 . 7 8 2 \mathrm {M e V}) ^ {5}} \simeq 4. 7 1 0 ^ {- 2 1} \mathrm {M e V} ^ {- 4},
$$

hence we have

$$
\frac {G _ {F}}{(\hbar c) ^ {3}} \simeq 6. 9 1 0 ^ {- 1 1} \mathrm {M e V} ^ {- 2} = 6. 9 1 0 ^ {- 5} \mathrm {G e V} ^ {- 2}.
$$

The value is different from the one reported in the literature $\left( 1 . 1 7 \ 1 0 ^ { - 5 } \ \mathrm { G e V } ^ { - 2 } \right)$ ) because of the spectrum integration inaccuracy implicit in the Sargent rule and other aspects of Fermi theory not included in Eq. (2.1), e.g. the $V - A$ feature of weak interaction and the quark structure of the neutron.

$\diamond$ Using the Sargent rule we have for the $^ { 3 5 } _ { 1 6 } \mathrm { S }  _ { 1 7 } ^ { 3 5 } \mathrm { C l } + e ^ { - } + \bar { \nu } _ { e }$ decay

$$
\frac {\omega [ ^ {3 5} \mathrm {S} ]}{\omega [ n ]} = \left(\frac {Q [ ^ {3 5} \mathrm {S} ]}{Q [ n ]}\right) ^ {5} = \left(\frac {0 . 1 6 8}{0 . 7 8 2}\right) ^ {5} \simeq 0. 0 0 0 4 6,
$$

and then

$$
\tau [ ^ {3 5} \mathrm {S} ] = \frac {8 8 6 \mathrm {s}}{0 . 0 0 0 4 6} \simeq 1. 9 1 0 ^ {6} \mathrm {s} \simeq 2 2 \mathrm {d}.
$$

$\diamond$ Both the parent and daughter nuclei are odd-A, hence the spin-parity is determined by the unpaired nucleon. The shell occupation of this nucleon is

$$
\begin{array}{l} - \begin{array}{l} 3 5 \\ 1 6 \end{array} S \quad n: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6} (2 s _ {1 / 2}) ^ {2} (1 d _ {3 / 2}) ^ {3} \\ - _ {1 7} ^ {3 5} \mathrm {C l} p: (1 s _ {1 / 2}) ^ {2} (1 p _ {3 / 2}) ^ {4} (1 p _ {1 / 2}) ^ {2} (1 d _ {5 / 2}) ^ {6} (2 s _ {1 / 2}) ^ {2} (1 d _ {3 / 2}) ^ {1} \\ \end{array}
$$

The unpaired nucleons have $l = 2$ : both $^ { 3 5 } _ { 1 6 } \mathrm { S }$ and $^ { 3 5 } _ { 1 7 } \mathrm { C l }$ have $J = 3 / 2$ , $P = ( - 1 ) ^ { 2 } = +$ $\implies J ^ { P } = 3 / 2 ^ { + }$ .

# Exercise 2.3.5

(1) Charged current $\nu _ { \mu }$ -interactions on nucleon valence quarks can be either

$$
\nu_ {\mu} + d \rightarrow \mu^ {-} + u
$$

or the ones associated to charm production

$$
\nu_ {\mu} + d \rightarrow \mu^ {-} + c.
$$

In these processes, the leptonic vertex is the same whereas the hadronic one is $g _ { W } \cos \theta _ { C }$ in the former and $g _ { W } \sin \theta _ { C }$ in the latter case, where $\theta _ { C }$ is the Cabibbo angle $( \sin \theta _ { C } ~ \simeq ~ 0 . 2 2 )$ . The fraction of charm events in CC interactions can be estimated as

$$
\begin{array}{l} \frac {\sigma \left(v _ {\mu} + d \rightarrow \mu^ {-} + c\right)}{\sigma \left(v _ {\mu} + d \rightarrow \mu^ {-} + u\right) + \sigma \left(v _ {\mu} + d \rightarrow \mu^ {-} + c\right)} = \frac {\sin^ {2} \theta_ {C}}{\cos^ {2} \theta_ {C} + \sin^ {2} \theta_ {C}} = \\ = \sin^ {2} \theta_ {C} \simeq 0. 0 5 \\ \end{array}
$$

(2) The probability for muon neutrinos to be detected as tau neutrinos is $P _ { \mu \tau }$ whereas $1 - P _ { \mu \tau }$ is the probability to survive in the initial state. The signal-to-noise ratio is then

$$
r = \frac {N (v _ {\tau} \rightarrow \tau^ {-})}{N (v _ {\mu} + d \rightarrow \mu^ {-} + c)} \simeq \frac {P _ {\mu \tau}}{1 - P _ {\mu \tau}} \times \frac {1}{\sin^ {2} \theta_ {C}} \simeq \frac {0 . 0 1 5}{0 . 9 8 5} \times \frac {1}{0 . 2 2 ^ {2}} \simeq 0. 3 1.
$$

(3) The $\tau ^ { - }$ decay modes are of type $\tau ^ { - } \to W ^ { - } + \nu _ { \tau }$ . A few cases are given below

•   
• $\tau ^ { - } \to e ^ { - } + \bar { \nu } _ { e } + \nu _ { \tau }$   
• $\tau ^ { - } \to \pi ^ { - } + \nu _ { \tau }$   
etc.

The Feynman graphs for these decays are shown below.

![](images/c73fc00c571f8cfc7bb4a612c8e60a315225ab2d2999f815896040a6055d4d59.jpg)

![](images/dbeb3ba3b282ff86ecad7ca934bfc3e57f7f257a63bcdc576b68c944d7f52072.jpg)

![](images/859133e5265233c12e180e07d91754fea549f8ed5b1bd2c2eca2c47492f49674.jpg)

# Exercise 2.3.6

Following the Fermi golden rule, the branching ratio is proportional to the absolute square of the transition amplitude times the phase space factor. In the decays of the text we have

$$
\frac {B R \left(\Sigma^ {-} \rightarrow n + e ^ {-} + \bar {\nu} _ {e}\right)}{B R \left(\Sigma^ {-} \rightarrow \Lambda + e ^ {-} + \bar {\nu} _ {e}\right)} \simeq \frac {| \mathcal {M} \left(\Sigma^ {-} \rightarrow n + e ^ {-} + \bar {\nu} _ {e}\right) | ^ {2}}{| \mathcal {M} \left(\Sigma^ {-} \rightarrow \Lambda + e ^ {-} + \bar {\nu} _ {e}\right) | ^ {2}} \times \frac {\rho \left(\Sigma^ {-} \rightarrow n + e ^ {-} + \bar {\nu} _ {e}\right)}{\rho \left(\Sigma^ {-} \rightarrow \Lambda + e ^ {-} + \bar {\nu} _ {e}\right)}
$$

For $\Sigma ^ { - }  n$ we have an effective coupling constant $g _ { w } \sin \theta _ { C }$ $g _ { w }$ $( d d s  d d u$ involves $s  u + W ^ { - } )$ , with $\theta _ { C }$ the Cabibbo angle. Instead for $\Sigma ^ { - }  \Lambda$ we have $g _ { w } \cos \theta _ { C }$ $( d d s  u d s$ involves $d  u + W ^ { - }$ ).

The phase space factors $( \rho )$ can be estimated using the Sargent rule. It is written as $w \propto E _ { 0 } ^ { 5 }$ , where $w$ is the decay rate and $E _ { 0 }$ is the energy available in the decay

![](images/6311688b20004d3d00ab756b38871accbe794ec9bafa656056b6841f1ed4992f.jpg)

![](images/65dc2259c1b1eb69392ef8513b5e6a63103fa8531671cb2082f4db249dcc864a.jpg)

$( = m _ { n } - m _ { p } - m _ { e }$ , in the case of the neutron decay $n  p + e ^ { - } + \bar { \nu _ { e } } )$ . In the Fermi theory of beta decay the transition rate is entirely due to kinematics. Therefore we can use the same expression for the phase space factor. So we have

$$
\frac {B R \left(\Sigma^ {-} \rightarrow n + e ^ {-} + \bar {\nu} _ {e}\right)}{B R \left(\Sigma^ {-} \rightarrow \Lambda + e ^ {-} + \bar {\nu} _ {e}\right)} \simeq \frac {\sin^ {2} \theta_ {C}}{\cos^ {2} \theta_ {C}} \times \left(\frac {m _ {\Sigma} - m _ {n} - m _ {e}}{m _ {\Sigma} - m _ {\Lambda} - m _ {e}}\right) ^ {5}
$$

and then

$$
\begin{array}{l} \tan^ {2} \theta_ {C} \simeq \frac {B R (\Sigma^ {-} \rightarrow n + e ^ {-} + \bar {\nu} _ {e})}{B R (\Sigma^ {-} \rightarrow \Lambda + e ^ {-} + \bar {\nu} _ {e})} \times \left(\frac {m _ {\Sigma} - m _ {\Lambda} - m _ {e}}{m _ {\Sigma} - m _ {n} - m _ {e}}\right) ^ {5} \simeq \\ \simeq \frac {1 0 . 2}{0 . 5 7} \times \left(\frac {1 1 9 7 - 1 1 1 6}{1 1 9 7 - 9 4 0}\right) ^ {5} \simeq 0. 0 5 6 \\ \end{array}
$$

Hence $\sin \theta _ { C } \simeq 0 . 2 3$ , which is in good agreement with the known value $\mathrm { s i n } \theta _ { C } \simeq$ 0.22).

# Exercise 2.3.7

Considering the transition amplitudes, for $D ^ { + } \to \bar { K } ^ { 0 } + e ^ { + } + \nu _ { e }$ we have $c  s +$ $W ^ { + }$ and an effective coupling constant $g _ { W } \cos \theta _ { C }$ ; for $\mu ^ { + }  e ^ { + } + \nu _ { e } + \bar { \nu } _ { \mu }$ we have a pure leptonic vertex $\mu ^ { + } \to \bar { \nu } _ { \mu } + W ^ { + }$ and thus only $g _ { W }$ . Making use of the Sargent rule for the phase space factors we get

$$
\begin{array}{l} \frac {\Gamma (D ^ {+} \rightarrow \bar {K} ^ {0} + e ^ {+} + v _ {e})}{\Gamma (\mu^ {+} \rightarrow e ^ {+} + v _ {e} + \bar {v} _ {\mu})} = \frac {| \mathcal {M} (D ^ {+} \rightarrow \bar {K} ^ {0} + e ^ {+} + v _ {e}) | ^ {2}}{| \mathcal {M} (\mu^ {+} \rightarrow e ^ {+} + v _ {e} + \bar {v} _ {\mu})) | ^ {2}} \times \frac {\rho (D ^ {+} \rightarrow \bar {K} ^ {0} + e ^ {+} + v _ {e})}{\rho (\mu^ {+} \rightarrow e ^ {+} + v _ {e} + \bar {v} _ {\mu})} \\ = \cos^ {2} \theta_ {C} \times \left(\frac {m _ {D ^ {+}} - m _ {\bar {K} ^ {0}} - m _ {e}}{m _ {\mu} - m _ {e}}\right) ^ {5} \simeq 0. 9 5 ^ {2} \times \left(\frac {1 8 7 0 - 4 9 8 - 0 . 5}{1 0 6 - 0 . 5}\right) ^ {5} \simeq 3. 5 \times 1 0 ^ {5} \\ \end{array}
$$

The experimental value is $1 . 5 \times 1 0 ^ { 5 }$ .

# Exercise 2.3.8

Pions produced in the atmospheric showers decay as $\pi ^ { - }  \mu ^ { - } + \bar { \nu } _ { \mu }$ and $\pi ^ { + } $ $\mu ^ { + } + \nu _ { \mu }$ . The muons produced in this way decay as $\mu ^ { - }  e ^ { - } + \bar { \nu } _ { e } + \nu _ { \mu }$ and $\mu ^ { + } \to$ $e ^ { + } + \nu _ { e } + \bar { \nu } _ { \mu }$ . All the charges have the same probability.

The pions produced in the hadronic interactions with atmosphere nuclei have energies higher than the ones observed for the atmospheric neutrinos. Let us assume that the pion energy is at most 1 GeV. The pion mean free path is

$$
l _ {\pi} = \beta \gamma c \tau_ {\pi} = \frac {p _ {\pi}}{m _ {\pi}} c \tau_ {\pi} <   \frac {1}{0 . 1 4 0} 3 1 0 ^ {8} \times 2. 6 1 0 ^ {- 8} \mathrm {m} \simeq 5 5 \mathrm {m}.
$$

Since their production height is around $1 0 \mathrm { k m }$ , all the pions decay before reaching the ground, unless they interact with the atmosphere again. Under the same assumption,

the produced muons have a mean free path

$$
l _ {\mu} = \beta \gamma c \tau_ {\mu} = \frac {p _ {\mu}}{m _ {\mu}} c \tau_ {\mu} <   \frac {1}{0 . 1 0 6} 3 1 0 ^ {5} \times 2. 2 1 0 ^ {- 6} \mathrm {k m} \simeq 6 \mathrm {k m}
$$

and also muons preferentially decay. Counting all the types of neutrinos appearing in the decays we obtain a flavor ratio

$$
\frac {\nu_ {\mu} + \bar {\nu} _ {\mu}}{\nu_ {e} + \bar {\nu} _ {e}} \simeq 2
$$

# Exercise 2.3.9

The Feynman graphs for $\mu ^ { - }  e ^ { - } + \bar { \nu } _ { e } + \nu _ { \mu }$ and $\tau ^ { - }  e ^ { - } + \bar { \nu } _ { e } + \nu _ { \tau }$ are identical apart the masses involved. Recalling the Sargent rule, one gets:

$$
R = \frac {\Gamma (\tau^ {-} \rightarrow e ^ {-} + \bar {\nu} _ {e} + \nu_ {\tau})}{\Gamma (\mu^ {-} \rightarrow e ^ {-} + \bar {\nu} _ {e} + \nu_ {\mu})} = \left(\frac {m _ {\tau} - m _ {e}}{m _ {\mu} - m _ {e}}\right) ^ {5} \simeq \left(\frac {m _ {\tau}}{m _ {\mu}}\right) ^ {5} \simeq 1. 3 2 \times 1 0 ^ {6}
$$

Denoting with $B ( \tau ^ { - }  e ^ { - } + \bar { \nu } _ { e } + \nu _ { \tau } )$ the branching ratio of this mode, the tau mean lifetime is then

$$
\tau_ {\tau} = \frac {\tau_ {\mu}}{R} \times B (\tau^ {-} \rightarrow e ^ {-} + \bar {\nu} _ {e} + \nu_ {\tau}) \simeq \frac {2 . 2 \times 1 0 ^ {- 6}}{1 . 3 2 \times 1 0 ^ {6}} \times 0. 1 8 \simeq 3 \times 1 0 ^ {- 1 3} \mathrm {s}
$$

# A.3 Solutions of Experiments and Detection Methods (Chapter 3)

# 3.1 Kinematics

# Exercise 3.1.1

Here we write a few kinematical relations useful for the solution:

$$
\begin{array}{l} \epsilon_ {\pi} = \sqrt {p _ {\pi} ^ {2} + m _ {\pi} ^ {2}} = \sqrt {p _ {\pi} ^ {2} + m _ {\pi} ^ {2}} \simeq 2 0 \mathrm {G e V} \\ E ^ {*} = \epsilon_ {\pi} ^ {*} + \epsilon_ {p} ^ {*} = \sqrt {m _ {\pi} ^ {2} + m _ {p} ^ {2} + 2 m _ {p} \epsilon_ {\pi}} \simeq 6. 1 9 9 \mathrm {G e V} \\ \beta_ {\mathrm {C M}} = \left| p _ {\pi} \right| / \left(\epsilon_ {\pi} + \epsilon_ {p}\right) = p _ {\pi} / \left(\epsilon_ {\pi} + m _ {p}\right) \simeq 0. 9 5 5 1 6 5 \\ \gamma_ {\mathrm {C M}} = (\epsilon_ {\pi} + \epsilon_ {p}) / E ^ {*} \simeq 3. 3 7 7 5 \\ p ^ {*} = | \boldsymbol {p} ^ {*} | = \frac {\sqrt {[ E ^ {* 2} - (m _ {\Sigma} + m _ {K}) ^ {2} ] [ E ^ {* 2} - (m _ {\Sigma} - m _ {K}) ^ {2} ]}}{2 E ^ {*}} \simeq 2. 9 6 5 \mathrm {G e V / c} \\ \end{array}
$$

1. Neglecting the thickness of the target, detectable tracks are produced by ionising particles emitted between $0 ^ { \circ }$ and $9 0 ^ { \circ }$ in the Laboratory system (LS). To answer the first question we have to establish if $\Sigma ^ { + }$ ’s produced in the experiment do exhibit a maximum angle. We have

$$
\epsilon_ {\Sigma} ^ {*} = \sqrt {p ^ {* 2} + m _ {\Sigma} ^ {2}} \simeq 3. 1 9 4 \mathrm {G e V}
$$

$$
\beta_ {\Sigma} ^ {*} = p ^ {*} / \epsilon_ {\Sigma} ^ {*} \simeq 0. 9 2 8 1
$$

$\beta _ { \Sigma } ^ { * } < \beta _ { \mathrm { C M } }$ is the condition to have such limiting angle and hence all $\Sigma ^ { + }$ ’s can be detected.5

2. Assuming that all $\Sigma ^ { + }$ ’s decay within 3 mean lifetimes, the maximum distance for the decay point is

$$
D _ {\Sigma} = 3 \cdot c \tau_ {\Sigma} \cdot \beta_ {\Sigma} \gamma_ {\Sigma} = 3 \cdot c \tau_ {\Sigma} \cdot \frac {p _ {\Sigma}}{m _ {\Sigma}} \simeq 6. 0 5 \times \frac {p _ {\Sigma}}{\mathrm {G e V / c}} \mathrm {c m},
$$

along the direction $\pmb { p } _ { \Sigma } / p _ { \Sigma }$ . From this expression we desume that the minimum length for the tracker corresponds to the maximum longitudinal momentum $( p _ { \Sigma } ) _ { L }$ . This occurs for $( p ^ { * } { } _ { \Sigma } ) _ { L } = p ^ { * }$ . Hence we have

$$
\begin{array}{l} (p _ {\Sigma}) _ {L} ^ {\max } = \gamma_ {\mathrm {C M}} \left(p ^ {*} + \beta_ {\mathrm {C M}} \cdot \epsilon_ {\Sigma} ^ {*}\right) \simeq 2 0. 3 \mathrm {G e V / c} \quad \Longrightarrow \\ L = 6. 0 5 \times 2 0. 3 \mathrm {c m} \simeq 1 2 2. 8 \mathrm {c m} \\ \end{array}
$$

3. As in the previous case, the minimum radius corresponds to the maximum $( p _ { \Sigma } ) _ { T }$ , that is for $( p ^ { * } { } _ { \Sigma } ) _ { T } = p ^ { * }$

$$
R = 6. 0 5 \times \frac {\left(p _ {\Sigma}\right) _ {T} ^ {\max}}{\mathrm {G e V / c}} = 6. 0 5 \times 2. 9 6 5 \mathrm {c m} \simeq 1 7. 9 \mathrm {c m}
$$

4. To establish if there is a maximum angle for $K ^ { + }$ , we calculate its velocity in the CMS

$$
\begin{array}{l} \epsilon_ {K} ^ {*} = \sqrt {p ^ {* 2} + m _ {K} ^ {2}} \simeq 3. 0 0 6 \mathrm {G e V} \\ \beta_ {K} ^ {*} = p ^ {*} / \epsilon_ {K} ^ {*} \simeq 0. 9 8 6 4 \\ \end{array}
$$

We have $\beta _ { K } ^ { * } > \beta _ { \mathrm { C M } }$ , so there is no limiting angle. Hence kaons can escape from the tracker.

5. The detectable kaons are those produced in the forward direction in the LS $\mathrm { ( 0 ^ { \circ } < }$ $\theta < 9 0 ^ { \circ }$ ). The CMS angle corresponding to $\theta = 9 0 ^ { \circ }$ can be obtained from the Lorentz transformation of the kaon longitudinal momentum $( p _ { K } ) _ { L } = \gamma _ { \mathrm { C M } } [ ( p _ { K } ^ { * } ) _ { L } + \beta _ { \mathrm { C M } } .$ · $\epsilon _ { K } ^ { * } ]$ by setting $( p _ { K } ) _ { L } = 0$ . Hence we have

$$
(p _ {K} ^ {*}) _ {L} = p ^ {*} \cos \theta^ {*} (9 0 ^ {\circ}) = - \beta_ {\mathrm {C M}} \epsilon_ {K} ^ {*} \Rightarrow
$$

$$
\cos \theta^ {*} (9 0 ^ {\circ}) = - \beta_ {\mathrm {C M}} \cdot \frac {\epsilon_ {K} ^ {*}}{p ^ {*}} = - \frac {\beta_ {\mathrm {C M}}}{\beta_ {K} ^ {*}} \simeq - 0. 9 6 8 3,
$$

corresponding to angle of about $1 6 5 . 5 ^ { \circ }$ .

In the CMS frame the kaon angular distribution is isotropic so it is given by $d N / d \Omega \ : = \ : 1 / 4 \pi$ (normalized to unity). The fraction of detectable kaons is then

$$
r = \frac {1}{4 \pi} \int_ {0} ^ {2 \pi} d \phi \int_ {\theta^ {*} (9 0 ^ {\circ})} ^ {1} d \cos \theta^ {*} = \frac {1 - \cos \theta^ {*} (9 0 ^ {\circ})}{2} \simeq \frac {1 . 9 6 8 3}{2} \simeq 9 8. 4
$$

# Exercise 3.1.2

(1) To have a limiting production angle, particle 1 must fulfill the condition $\beta _ { \mathrm { C M } } \geq \beta _ { 1 } ^ { \ast }$ . The maximum limiting angle, corresponding to $9 0 ^ { \circ }$ , is obtained for the equality in the previous relation. The CMS energy is the mass of the resonance, $E ^ { * } = M$ . Hence we have

$$
\begin{array}{l} p ^ {*} = | \pmb {p} ^ {*} | = \sqrt {[ M ^ {2} - (m _ {1} + m _ {2}) ^ {2} ] [ M ^ {2} - (m _ {1} - m _ {2}) ^ {2} ]} / 2 M \\ \epsilon_ {1} ^ {*} = \left(M ^ {2} + m _ {1} ^ {2} - m _ {2} ^ {2}\right) / 2 M \\ \end{array}
$$

and then

$$
\beta_ {1} ^ {*} = \frac {p ^ {*}}{\epsilon_ {1} ^ {*}} = \frac {\sqrt {[ M ^ {2} - (m _ {1} + m _ {2}) ^ {2} ] [ M ^ {2} - (m _ {1} - m _ {2}) ^ {2} ]}}{M ^ {2} + m _ {1} ^ {2} - m _ {2} ^ {2}}
$$

Since $m _ { 2 }$ is negligible with respect to $m _ { 1 }$ , we get

$$
\beta_ {1} ^ {*} = \frac {M ^ {2} - m _ {1} ^ {2}}{M ^ {2} + m _ {1} ^ {2}} = \frac {2 . 5 8 ^ {2} - 1}{2 . 5 8 ^ {2} + 1} \simeq 0. 7 3 8 8
$$

We can get the pion beam energy $E _ { \pi }$ , solving the equation $\beta _ { \mathrm { C M } } = \beta _ { 1 } ^ { * }$

$$
\beta_ {\mathrm {C M}} = \frac {| \pmb {p} _ {\pi} |}{E _ {\pi} + m _ {p}} = \frac {\sqrt {E _ {\pi} ^ {2} - m _ {\pi} ^ {2}}}{E _ {\pi} + m _ {p}} = \beta_ {1} ^ {*}.
$$

Solving it in $E _ { \pi }$ we have

$$
E _ {\pi} = \frac {\beta_ {1} ^ {* 2} m _ {p} + \sqrt {(\beta_ {1} ^ {* 2} m _ {p}) ^ {2} + (1 - \beta_ {1} ^ {* 2}) (m _ {\pi} ^ {2} + \beta_ {1} ^ {* 2} m _ {p} ^ {2})}}{1 - \beta_ {1} ^ {* 2}} \simeq 2. 6 5 \mathrm {G e V}.
$$

For higher $E _ { \pi }$ values particle 1 is produced up to angles less than $9 0 ^ { \circ }$ .

(2) Considering the decay $\Delta ( 2 4 2 0 )  \Sigma + K$ , for a fixed CMS angle $\theta ^ { * } = 1 2 0 ^ { \circ }$ and $\beta _ { \mathrm { C M } } = 0 . 7 3 8 8$ , we have

$$
p ^ {*} = | \boldsymbol {p} ^ {*} | = \frac {\sqrt {[ M ^ {2} - (m _ {\Sigma} + m _ {K}) ^ {2} ] [ M ^ {2} - (m _ {\Sigma} - m _ {K}) ^ {2} ]}}{2 M} \simeq 0. 8 3 3 \mathrm {G e V / c m ^ {2}}
$$

$$
\epsilon_ {\Sigma} ^ {*} = \sqrt {p ^ {* 2} + m _ {\Sigma} ^ {2}} \simeq 1. 4 5 2 \mathrm {G e V}
$$

$$
(p _ {\Sigma}) _ {L} = \gamma_ {\mathrm {C M}} \left(p ^ {*} \cos \theta^ {*} + \beta_ {\mathrm {C M}} \cdot \epsilon_ {\Sigma} ^ {*}\right) \simeq 0. 9 7 4 \mathrm {G e V / c}
$$

$$
(p _ {\Sigma}) _ {T} = p ^ {*} \sin \theta^ {*} \simeq 0. 7 2 1 \mathrm {G e V / c}.
$$

From the last expressions we can get the momentum and angle of the $\Sigma$ in the Laboratory system

$$
p _ {\Sigma} = \sqrt {(p _ {\Sigma}) _ {L} ^ {2} + (p _ {\Sigma}) _ {T} ^ {2}} \simeq 1. 2 1 \mathrm {G e V / c}
$$

$$
\theta_ {\Sigma} = \arccos  \frac {(p _ {\Sigma}) _ {L}}{p _ {\Sigma}} \simeq 3 6. 5 ^ {\circ}
$$

(3) The $\Sigma$ -decay mean pathlength is $c \tau _ { \Sigma } \cdot \beta _ { \Sigma } \gamma _ { \Sigma } = c \tau _ { \Sigma } \cdot p _ { \Sigma } / m _ { \Sigma }$ . The length of the detector is determined by the $\Sigma$ ’s decaying in the forward direction, for which the momentum is maximum. This is

$$
p _ {\Sigma} ^ {\max } = \gamma_ {\mathrm {C M}} \left(p ^ {*} + \beta_ {\mathrm {C M}} \cdot \epsilon_ {\Sigma} ^ {*}\right) \simeq 2. 8 3 \mathrm {G e V / c}
$$

The designed length corresponds to the requirement that $9 9 \%$ of the decay points are contained in the detector. This occurs for a proper time $T$ so that we have

$$
\begin{array}{l} 0. 9 9 = \int_ {0} ^ {T} \frac {1}{\tau_ {\Sigma} N _ {0}} N (t) d t = 1 - \int_ {T} ^ {\infty} \frac {1}{\tau_ {\Sigma}} \exp \left(- \frac {t}{\tau_ {\Sigma}}\right) d t = 1 - \exp \left(- \frac {T}{\tau_ {\Sigma}}\right) \\ \Longrightarrow \quad T = - \ln (0. 0 1) \cdot \tau_ {\Sigma} \simeq 4. 6 \cdot \tau_ {\Sigma} \\ \end{array}
$$

Hence the length of the detector must be

$$
L = c T \cdot \frac {p _ {\Sigma} ^ {\mathrm {m a x}}}{m _ {\Sigma}} \simeq 4. 6 c \tau_ {\Sigma} \cdot \frac {p _ {\Sigma} ^ {\mathrm {m a x}}}{m _ {\Sigma}}
$$

Solving this equation in $\tau _ { \Sigma }$ , we finally get

$$
\tau_ {\Sigma} = \frac {L m _ {\Sigma}}{4 . 6 c p _ {\Sigma} ^ {\mathrm {m a x}}} \simeq \frac {0 . 2 6 \times 1 . 1 8 9}{4 . 6 \times 3 \cdot 1 0 ^ {8} \times 2 . 8 3} \simeq 0. 7 9 \times 1 0 ^ {- 1 0} \mathrm {s}
$$

# Exercise 3.1.3

1. The minimum energy for a reaction is its threshold energy $( E _ { \mathrm { t h } } )$ . It corresponds to the production of the final particles at rest in the CMS. Equating the 4-momentum invariants in the LS for the initial state and in the CMS for the final state, we have

$$
M _ {\pi} ^ {2} + M _ {p} ^ {2} + 2 E _ {\mathrm {t h}} M _ {p} = (M _ {\Lambda} + M _ {K}) ^ {2}
$$

and then

$$
E _ {\mathrm {t h}} = \frac {(M _ {\Lambda} + M _ {K}) ^ {2} - M _ {\pi} ^ {2} - M _ {p} ^ {2}}{2 M _ {p}} \simeq 0. 9 1 \mathrm {G e V}
$$

2. A maximum production angle is possible provided that $\beta ^ { * } < \beta _ { \mathrm { C M } }$ , where $\beta ^ { * }$ is the CMS velocity of the particle and $\beta _ { \mathrm { C M } }$ is the velocity of the CMS with respect to the LS. For $E _ { \pi } = 2 \mathrm { G e V }$ , we have

$$
\beta_ {\mathrm {C M}} = \frac {p _ {\pi}}{E _ {\pi} + M _ {p}} \simeq 0. 6 8
$$

To get the $\Lambda$ velocity in the CMS, we first calculate the total CMS energy ( $P _ { \pi }$ and $P _ { p }$ are the 4-momenta of the pion and proton respectively)

$$
E ^ {*} = \sqrt {\left(P _ {\pi} + P _ {p}\right) ^ {2}} = \sqrt {M _ {p} ^ {2} + M _ {\pi} ^ {2} + 2 E _ {\pi} M _ {p}} \simeq 2. 1 6 \mathrm {G e V}
$$

The momentum in the CMS is

$$
p ^ {*} = | \boldsymbol {p} ^ {*} | = \frac {\sqrt {[ E ^ {* 2} - (M _ {\Lambda} + M _ {K}) ^ {2} ] [ E ^ {* 2} - (M _ {\Lambda} - M _ {K}) ^ {2} ]}}{2 E ^ {*}} \simeq 0. 6 9 \mathrm {G e V / c}
$$

Hence we have for the $\Lambda$ -velocity in the CMS

$$
\beta^ {*} = \frac {p ^ {*}}{\sqrt {p ^ {* 2} + M _ {\Lambda} ^ {2}}} \simeq 0. 5 2.
$$

The condition $\beta ^ { * } < \beta _ { \mathrm { C M } }$ is fulfilled so that there is a maximum production angle for the $\Lambda$ ’s. This angle turns out to be

$$
\theta_ {\max } = \arctan \left\{\left[ \gamma_ {\mathrm {C M}} \sqrt {\left(\frac {\beta_ {\mathrm {C M}}}{\beta^ {*}}\right) ^ {2} - 1} \right] ^ {- 1} \right\} \simeq 0. 7 3 \mathrm {r a d} \simeq 4 2 ^ {\circ}
$$

# Exercise 3.1.4

The invariant mass of the two-pion system is the mass $M _ { X }$ of the observed neutral particle

$$
M _ {X} ^ {2} = (P _ {\pi^ {+}} + P _ {\pi^ {-}}) ^ {2} = 2 M _ {\pi} ^ {2} + 2 E _ {\pi^ {+}} E _ {\pi^ {-}} - 2 p _ {\pi^ {+}} p _ {\pi^ {-}} \cos \theta .
$$

The minimum opening angle corresponds to the case in which the two pions have the same energy $E _ { \pi ^ { + } } = E _ { \pi ^ { - } } ( = E _ { X } / 2 )$ . Imposing this condition and having in mind that $E _ { \pi } \gg M _ { \pi }$ we get

$$
M _ {X} = \sqrt {E _ {X} ^ {2} \sin^ {2} \theta / 2 + 2 M _ {\pi} ^ {2}} \simeq 0. 4 9 5 \mathrm {G e V} / \mathrm {c} ^ {2}
$$

# Exercise 3.1.5

Denoting by $P _ { i }$ the 4-momentum of electron $i$ , the total CMS energy is written as

$$
E ^ {*} = \sqrt {(P _ {1} + P _ {2}) ^ {2}} = \sqrt {(E _ {1} + E _ {2}) ^ {2} - (p _ {1} + p _ {2}) ^ {2}} =
$$

$$
\sqrt {E _ {1} ^ {2} + E _ {2} ^ {2} + 2 E _ {1} E _ {2} - p _ {1} ^ {2} - p _ {2} ^ {2} + 2 p _ {1} p _ {2}} = \sqrt {2 m ^ {2} + 2 E _ {1} E _ {2} + 2 p _ {1} p _ {2}} \simeq \sqrt {4 E _ {1} E _ {2}}
$$

where, in the last step, we have neglected the electron masses with respect to their energies. Therefore we have $E ^ { * } = 1 5 . 5 \mathrm { G e V }$ .

In the CMS the two electron momenta are opposite. Neglecting the masses we have

$$
p ^ {*} = \frac {E ^ {*}}{2} \simeq 7. 7 4 \mathrm {G e V / c}.
$$

The CMS velocity (in $c$ units) in the LS is given by

$$
\beta_ {\mathrm {C M}} = \frac {| \boldsymbol {p} _ {1} + \boldsymbol {p} _ {2} |}{E _ {1} + E _ {2}} = \frac {\sqrt {E _ {1} ^ {2} - m ^ {2}} - \sqrt {E _ {2} ^ {2} - m ^ {2}}}{E _ {1} + E _ {2}} \simeq \frac {E _ {1} - E _ {2}}{E _ {1} + E _ {2}} \simeq 0. 4 \tag {3.1}
$$

and the Lorentz factor is

$$
\gamma_ {\mathrm {C M}} = (1 - \beta_ {\mathrm {C M}} ^ {2}) ^ {- 1 / 2} \simeq 1. 1.
$$

If $E _ { 1 } = E _ { 2 }$ and $p _ { 1 } = - p _ { 2 }$ , from Eq. (3.1) we get $\beta _ { \mathrm { C M } } = 0$ . Hence the center-ofmomentum and laboratory systems are coincident.

# Exercise 3.1.6

The minimum electron energy is its rest mass $( \simeq 0 . 5 1 1 \mathrm { \ : M e V } ,$ ), corresponding to the emission of an electron at rest.

To evaluate the maximum energy in a three-body decay $M  m _ { 1 } + m _ { 2 } + m _ { 3 }$ , it is convenient to re-write it as a two-body decay $M  M _ { 1 2 } + m _ { 3 }$ , where $M _ { 1 2 }$ is the

invariant mass of particles 1 and 2. It then turns out that the maximum energy for 3 is obtained when $M _ { 1 2 }$ is minimum, that is when it is equal to the $m _ { 1 } + m _ { 2 }$ . Hence we have

$$
(E _ {3}) _ {\max } = \frac {M ^ {2} + m _ {3} ^ {2} - (m _ {1} + m _ {2}) ^ {2}}{2 M}.
$$

In our case $M = M _ { \Xi ^ { 0 } }$ , $m _ { 3 } = M _ { e ^ { - } }$ , $m _ { 1 } = M _ { \Sigma ^ { + } }$ and $m _ { 2 } = M _ { \nu } = 0$ and we have

$$
(E _ {e ^ {-}}) _ {\max } \simeq \frac {1 3 1 5 ^ {2} + 0 . 5 1 1 ^ {2} - 1 1 8 9 ^ {2}}{2 \times 1 3 1 5} \simeq 1 2 0 \mathrm {M e V}
$$

# Exercise 3.1.7

The minimum opening angle for a decay into two equal (ultra-relativistic) particles is obtained for

$$
E _ {\pi^ {+}} = E _ {\pi^ {-}} = \frac {E _ {D}}{2}.
$$

Hence for the minimum opening angle between the pions we have

$$
\theta_ {\min } = \arcsin \left(\frac {\sqrt {M _ {D} ^ {2} - 2 M _ {\pi} ^ {2}}}{E _ {\pi}}\right) = \arcsin \left(2 \frac {\sqrt {M _ {D} ^ {2} - 2 M _ {\pi} ^ {2}}}{E _ {D}}\right) \tag {3.2}
$$

To get the $\bar { D ^ { 0 } }$ energy, we make use of the knowledge that this particle is produced at the maximum angle $\theta _ { \mathrm { m a x } }$ . The corresponding angle in the CMS is given by the equation

$$
\cos \bar {\theta} ^ {*} = \cos \theta^ {*} (\theta_ {\mathrm {m a x}}) = - \frac {\beta_ {D} ^ {*}}{\beta_ {\mathrm {C M}}},
$$

where $\beta _ { D } ^ { * }$ is the $\bar { D ^ { 0 } }$ velocity in the CMS and $\beta _ { \mathrm { C M } }$ is the CMS velocity in the LS. Denoting by $E _ { D } ^ { * }$ and $p ^ { * }$ the energy and momentum of the ${ \bar { D } } ^ { 0 }$ -particle in the CMS, using the Lorentz transformation for the energy, we get

$$
E _ {D} = \gamma_ {\mathrm {C M}} \left(E _ {D} ^ {*} + \beta_ {\mathrm {C M}} p ^ {*} \cos \bar {\theta} ^ {*}\right) = \gamma_ {\mathrm {C M}} \left(E _ {D} ^ {*} - \beta_ {D} ^ {*} p ^ {*}\right). \tag {3.3}
$$

The total energy in the CMS is

$$
E ^ {*} = \sqrt {\left(P _ {\pi} + P _ {p}\right) ^ {2}} = \sqrt {2 E _ {\pi} M _ {p} + M _ {\pi} ^ {2} + M _ {p} ^ {2}} = 6. 2 1 \mathrm {G e V}.
$$

Hence the ${ \bar { D } } ^ { 0 }$ -momentum in the CMS is

$$
p ^ {*} = \frac {\sqrt {[ E ^ {* 2} - (M _ {\Sigma} - M _ {D}) ^ {2} ] [ E ^ {* 2} - (M _ {\Sigma} + M _ {D}) ^ {2} ]}}{2 E ^ {*}} \simeq 2. 2 2 \mathrm {G e V / c}
$$

and the corresponding energy is $\sqrt { p ^ { * 2 } + M _ { D } ^ { 2 } } \simeq 2 . 9 0 \mathrm { G e V } .$

For the quantities appearing in Eq. (3.3) we get

$$
\beta_ {D} ^ {*} = \frac {p ^ {*}}{\sqrt {p ^ {* 2} + M _ {D} ^ {2}}} = 0. 7 6 7 \quad \gamma_ {\mathrm {C M}} = \frac {E _ {\pi} + M _ {p}}{E ^ {*}} = 3. 3 7,
$$

and hence we have $E _ { D } = 4 . 0 \ \mathrm { G e V } .$ . Using (3.2), we finally get for the minimum opening angle

$$
\theta_ {\min } = \arcsin \left(2 \times \frac {\sqrt {1 . 8 6 ^ {2} - 2 \times 0 . 1 4 0 ^ {2}}}{4}\right) \simeq 1. 1 8 \mathrm {r a d} \simeq 6 7. 6 ^ {\circ}
$$

# Exercise 3.1.8

Equating the 4-momentum invariants in the LS for the initial state and in the CMS for the final state, we have at the threshold

$$
E _ {p} ^ {2} + E _ {\gamma} ^ {2} + 2 E _ {p} E _ {\gamma} - p _ {p} ^ {2} - p _ {\gamma} ^ {2} - 2 \pmb {p} _ {p} \cdot \pmb {p} _ {\gamma} = (M _ {p} + M _ {\pi}) ^ {2}
$$

In the UHE regime we assume $E _ { p } \approx p _ { p }$ and then we get

$$
2 E _ {p} E _ {\gamma} (1 - \cos \theta) = (M _ {p} + M _ {\pi}) ^ {2} - M _ {p} ^ {2}
$$

The threshold energy as a function of the scattering angle is then

$$
E _ {\mathrm {t h}} (\theta) = \frac {(M _ {p} + M _ {\pi}) ^ {2} - M _ {p} ^ {2}}{2 E _ {\gamma} (1 - \cos \theta)}.
$$

The minimum value is obtained in the case of head-on scattering, $\theta = \pi$

$$
E _ {\mathrm {t h}} ^ {\mathrm {m i n}} = \frac {(M _ {p} + M _ {\pi}) ^ {2} - M _ {p} ^ {2}}{4 E _ {\gamma}} \simeq 6. 8 \times 1 0 ^ {1 9} \mathrm {e V}.
$$

# Exercise 3.1.9

Using the relativistic invariants we have

$$
(M _ {p} + M _ {n}) ^ {2} = (E _ {d} + E _ {\gamma}) ^ {2} - (\pmb {p} _ {d} + \pmb {p} _ {\gamma}) ^ {2} = M _ {d} ^ {2} + 2 E _ {\gamma} E _ {d} - 2 \pmb {p} _ {d} \cdot \pmb {p} _ {\gamma}.
$$

From the momentum conservation we can write ${ \pmb p } _ { d } = - { \pmb p } _ { \gamma }$ and then

$$
(M _ {p} + M _ {n}) ^ {2} = M _ {d} ^ {2} + 2 E _ {\gamma} (E _ {d} - p _ {d}) \simeq M _ {d} ^ {2} + 2 E _ {\gamma} M _ {d} \simeq (M _ {d} + E _ {\gamma}) ^ {2},
$$

where, in the last two steps, we have considered that both the deuteron recoil momentum the photon energy (both $O ( \mathrm { M e V } ) _ { \it \Delta }$ ) are negligible with respect to the deuteron mass. Hence we can write

$$
M _ {d} \simeq M _ {p} + M _ {n} - E _ {\gamma}.
$$

Assuming that the proton and neutron masses have negligible errors, it follows that $\Delta M _ { d } = \Delta E _ { \gamma }$ , and finally we get

$$
M _ {d} = 1 8 7 5. 6 0 7 \pm 0. 0 0 5 \mathrm {M e V / c ^ {2}}
$$

# Exercise 3.1.10

1. The total CMS energy is

$$
E ^ {*} = \sqrt {2 M _ {p} ^ {2} + 2 M _ {p} E _ {\bar {p}}} \simeq 2. 0 8 \mathrm {G e V}
$$

were we used $E _ { \bar { p } } = \sqrt { p _ { \bar { p } } ^ { 2 } + M _ { p } ^ { 2 } } = 1 . 3 7 \mathrm { G e V } .$ The kaons in final state are produced back-to-back at $9 0 ^ { \circ }$ in the CMS. Their energies are $E _ { K } ^ { * } = E ^ { * } / 2$ and the momenta are

$$
p _ {K} ^ {*} = \sqrt {(E ^ {*} / 2) ^ {2} - M _ {K} ^ {2}} \simeq 0. 9 2 \mathrm {G e V / c}.
$$

Therefore in the CMS $p _ { T } ^ { * } = p _ { K } ^ { * }$ and $p _ { L } ^ { * } = 0$ . Using the Lorentz transformation to the LS we get

$$
(p _ {K}) _ {T} = p _ {T} ^ {*} \simeq 0. 9 2 \mathrm {G e V / c}
$$

$$
(p _ {K}) _ {L} = \gamma_ {\mathrm {C M}} [ p _ {L} ^ {*} + \beta_ {\mathrm {C M}} E _ {K} ^ {*} ] = 0 + \frac {p _ {\bar {p}}}{E ^ {*}} \sqrt {(p _ {K} ^ {*}) ^ {2} + M _ {K} ^ {2}} \simeq 0. 5 0 \mathrm {G e V / c m}
$$

The kaon energy in the LS is then

$$
E _ {K} = \sqrt {[ (p _ {K}) _ {T} ^ {2} + (p _ {K}) _ {L} ^ {2} ] + M _ {K} ^ {2}} \simeq 1. 1 6 \mathrm {G e V}
$$

and the production angle is

$$
\theta_ {K} = \arctan \left[ \frac {\left(p _ {K}\right) _ {T}}{\left(p _ {K}\right) _ {L}} \right] \simeq 6 1. 5 ^ {\circ}
$$

The kaons we are detecting have $\beta \gamma = p _ { K } / M _ { K } = 2 . 1$ and we can then assume that their energy loss in the gas is $\begin{array} { r } { \left( \frac { d E } { d x } \right) _ { \mathrm { i o n } } = 2 ~ \frac { \mathrm { M e V } } { \mathrm { g ~ c m } ^ { - 2 } } } \end{array}$ dx  K K =       2 MeVg cm−2 . The number of electron-ion pairs in each detector turns out to be

$$
n = \frac {1}{I} \left(\frac {d E}{d x}\right) _ {\text {i o n}} \rho d \epsilon_ {p} \epsilon_ {c} \simeq \frac {2 1 0 ^ {6}}{1 5} \times 2 1 0 ^ {- 3} \times 1 0 \times 0. 2 0 \times 0. 3 0 \simeq 1 6 0.
$$

# Exercise 3.1.11

The mass of the particle is obtained from the invariant mass of the two muons. Their energies in the LS are

$$
E _ {1} = \sqrt {p _ {1} ^ {2} + m _ {\mu} ^ {2}} \simeq \sqrt {4 5 ^ {2} + 1 0 6 ^ {2}} \simeq 1 1 5 \mathrm {M e V}
$$

$$
E _ {2} = \sqrt {p _ {2} ^ {2} + m _ {\mu} ^ {2}} \simeq p _ {2} = 3 0 \mathrm {G e V}.
$$

The square of the total 4-momentum is the invariant mass of the system. The total energy and momentum are

$$
E _ {t} = E _ {1} + E _ {2} \simeq 0. 1 1 5 + 3 0 \simeq 3 0. 1 2 \mathrm {G e V}
$$

$$
| \boldsymbol {p} _ {t} | = | \boldsymbol {p} _ {1} + \boldsymbol {p} _ {2} | = | \boldsymbol {p} _ {2} | - | \boldsymbol {p} _ {1} | = 3 0 - 0. 0 4 5 = 2 9. 9 6 \mathrm {G e V / c}
$$

Hence for the mass we have

$$
M = \sqrt {E _ {t} ^ {2} - p _ {t} ^ {2}} = \sqrt {3 0 . 1 2 ^ {2} - 2 9 . 9 6 ^ {2}} = 3. 1 0 \mathrm {G e V / c ^ {2}}.
$$

The particle is the $J / \psi$ -meson.

# Exercise 3.1.12

At the threshold we have

$$
E _ {p} ^ {2} + E _ {\gamma} ^ {2} + 2 E _ {p} E _ {\gamma} - p _ {p} ^ {2} - p _ {\gamma} ^ {2} - 2 \boldsymbol {p} _ {p} \cdot \boldsymbol {p} _ {\gamma} = (M _ {p} + 2 m _ {e}) ^ {2},
$$

and for $E _ { p } \simeq p _ { p }$ :

$$
2 E _ {p} E _ {\gamma} (1 - \cos \theta) = (M _ {p} + 2 m _ {e}) ^ {2} - M _ {p} ^ {2} \simeq 4 M _ {p} m _ {e}.
$$

Substituting $E _ { \gamma _ { \mathrm { C M B } } }$ to $E _ { \gamma }$ , the threshold energy as a function of $\theta$ turns out to be

$$
E _ {\mathrm {t h}} (\theta) \simeq \frac {2 M _ {p} m _ {e}}{E _ {\gamma_ {\mathrm {C M B}}} (1 - \cos \theta)}.
$$

The minimum value is obtained for $\theta = \pi$ (head on scattering) and is

$$
E _ {\text {t h}} ^ {\min } = \frac {M _ {p} m _ {e}}{E _ {\gamma_ {\mathrm {C M B}}}} \simeq 0. 5 \times 1 0 ^ {1 8} \mathrm {e V}.
$$

# Exercise 3.1.13

(a) Denoting by $s$ the square of the total energy at LHC and with $E _ { \mathrm { L a b } }$ the energy in fixed target $p p$ interactions, we require

$$
s = 2 m E _ {\mathrm {L a b}}
$$

where m is the proton mass. Here we have assumed that protons are ultra-relativistic. Hence we get

$$
E _ {\mathrm {L a b}} = \frac {s}{2 m} \simeq \frac {(1 3 1 0 ^ {1 2}) ^ {2} \mathrm {e V} ^ {2}}{2 \times 0 . 9 4 1 0 ^ {9} \mathrm {e V}} \simeq 9 \times 1 0 ^ {1 6} \mathrm {e V}
$$

(b) Denoting by $\nu$ the insect velocity we have

$$
\frac {1}{2} M v ^ {2} = E _ {\mathrm {L a b}},
$$

since in the ultra-relativistic limit the proton kinetic energy is almost equal to its total energy. Then we get

$$
v = \sqrt {\frac {2 E _ {\mathrm {L a b}}}{M}} \simeq \sqrt {\frac {2 \times 9 1 0 ^ {1 6} \times 1 . 6 1 0 ^ {- 1 9} \mathrm {J}}{0 . 2 5 1 0 ^ {- 3} \mathrm {k g}}} \simeq 1 1 \mathrm {m / s} \simeq 3 9 \mathrm {k m / h}
$$

# Exercise 3.1.14

(a) Consider the Lorentz transformation between the reference systems $\mathbf { K } '$ and K. Denoting by $\beta$ the velocity of $\mathbf { K } '$ with respect to K, we have

$$
E = \gamma (E ^ {\prime} + \beta p _ {\parallel} ^ {\prime}), \quad p _ {\parallel} = \gamma (p _ {\parallel} ^ {\prime} + \beta E ^ {\prime}).
$$

Hence we get

$$
E \pm p _ {\parallel} = \gamma (1 \pm \beta) (E ^ {\prime} \pm p _ {\parallel} ^ {\prime}),
$$

$$
\frac {E + p _ {\parallel}}{E - p _ {\parallel}} = \frac {1 + \beta}{1 - \beta} \times \frac {E ^ {\prime} + p _ {\parallel} ^ {\prime}}{E ^ {\prime} - p _ {\parallel} ^ {\prime}}
$$

Using the definition of rapidity we finally obtain

$$
y = y ^ {\prime} + \ln \sqrt {\frac {1 + \beta}{1 - \beta}}
$$

(b) The maximum (minimum) rapidity is obtained for the elastic scattering, $p p $ $p p$ , at $\theta = 0 ^ { \circ }$ $\ m \mathcal { O } = 1 8 0 ^ { \circ }$ ). The maximum value is then for $p _ { \parallel } = p$ and $p$ equal to the beam momentum $( { \simeq } 6 . 5 \mathrm { T e V } _ { \ }$ )

$$
y _ {\max } = \frac {1}{2} \ln \frac {E + p}{E - p} = \frac {1}{2} \ln \frac {(E + p) ^ {2}}{E ^ {2} - p ^ {2}} = \ln \frac {E + p}{m} = \ln \frac {6 5 0 0 + 6 5 0 0}{0 . 9 4} \simeq 9. 5
$$

and $y _ { \mathrm { m i n } } = - y _ { \mathrm { m a x } }$ .

(c) If $\theta$ is the scattering angle, we have $p _ { \parallel } = p$ cosθ . In the ultra-relativistic limit $E \simeq p$ and we get

$$
y \simeq \frac {1}{2} \ln \frac {E (1 + \cos \theta)}{E (1 - \cos \theta)} = \frac {1}{2} \ln \frac {\cos^ {2} \theta / 2}{\sin^ {2} \theta / 2} = - \ln \tan \frac {\theta}{2} = \eta
$$

(d) At $9 0 ^ { \circ }$ rapidity and pseudorapidity are identical: $y = \eta = 0$ . At $1 ^ { \circ }$ we have

$$
y = \frac {1}{2} \ln \frac {\sqrt {p ^ {2} + m ^ {2}} + p \cos 1 ^ {\circ}}{\sqrt {p ^ {2} + m ^ {2}} - p \cos 1 ^ {\circ}} = \frac {1}{2} \ln \frac {\sqrt {6 5 0 0 ^ {2} + 0 . 9 4 ^ {2}} + 6 5 0 0 \cos 1 ^ {\circ}}{\sqrt {6 5 0 0 ^ {2} + 0 . 9 4 ^ {2}} - 6 5 0 0 \cos 1 ^ {\circ}} \simeq 4. 7 4 1 2 3
$$

$$
\eta = - \ln \tan 0. 5 ^ {\circ} \simeq 4. 7 4 1 3 4.
$$

Therefore the difference is of the order of 1 over $1 0 ^ { 5 }$ .

# Exercise 3.1.15

For a particle moving along the $x$ direction and emitting a decay particle at angle $\theta$ after a (proper) time $t$ , we have

$$
\Delta = c t \beta \gamma \sin \theta = c t \frac {p}{m} \sin \theta
$$

Denoting CMS quantities with * and with no index the ones in the LS, we obtain from the Lorentz transformations

$$
p _ {y} = p _ {y} ^ {*}, \epsilon = \gamma (\epsilon^ {*} + \beta p _ {x} ^ {*})
$$

$$
p \sin \theta = p ^ {*} \sin \theta^ {*}, \quad \epsilon = \gamma \epsilon^ {*} (1 + \beta \beta^ {*} \cos \theta^ {*}),
$$

where $\beta ^ { * }$ is the velocity of the emitted particle in the CMS $( = p ^ { * } / \epsilon ^ { * }$ ). From their ratio we get

$$
\beta \gamma \sin \theta = \frac {\beta^ {*} \sin \theta^ {*}}{1 + \beta \beta^ {*} \cos \theta^ {*}}
$$

In the ultra-relativistic limit for both particles $( \beta \to 1 , \beta ^ { * } \to 1 ,$ $\beta \to 1$ ) we have

$$
\beta \gamma \sin \theta \rightarrow \frac {\sin \theta^ {*}}{1 + \cos \theta^ {*}} = \tan \frac {\theta^ {*}}{2}
$$

and finally obtain

$$
\Delta \rightarrow c t \tan \frac {\theta}{2} ^ {*}
$$

which proves that the impact parameter is independent from the particle momentum.

The mean value of the impact parameter for $t = \tau$ is

Appendix: Solutions of Exercises and Problems

$$
\langle \Delta \rangle = c \tau \int_ {0} ^ {\pi} \tan \frac {\theta}{2} ^ {*} \frac {\sin \theta^ {*} d \theta^ {*}}{2} = c \tau \frac {(x - \sin x) | _ {0} ^ {\pi}}{2} = \frac {\pi}{2} c \tau
$$

For the $D ^ { + }$ decay we get

$$
\langle \Delta \rangle \simeq 1. 5 7 \times 3 1 0 ^ {8} \mathrm {m} / \mathrm {s} \times 1. 0 4 1 0 ^ {- 1 2} \mathrm {s} \simeq 4 9 0 \mu \mathrm {m}
$$

For a CMS angle $\theta ^ { * } = 9 0 ^ { \circ }$ we obtain

$$
\Delta \simeq 3 1 0 ^ {8} \mathrm {m} / \mathrm {s} \times 1. 0 4 1 0 ^ {- 1 2} \mathrm {s} \times \tan 4 5 ^ {\circ} \simeq 3 1 2 \mu \mathrm {m}
$$

# Exercise 3.1.16

The mass of the parent particle is the invariant mass of the two muons. We have

$$
M ^ {2} = P ^ {2} = \left(p _ {1} + p _ {2}\right) ^ {2} = m _ {1} ^ {2} + m _ {2} ^ {2} + 2 E _ {1} E _ {2} - 2 | \boldsymbol {p} _ {1} | | \boldsymbol {p} _ {2} | \cos \theta ,
$$

where $p _ { i }$ and $p _ { i }$ are respectively the 4-momentum and the momentum of particle i $( = 1 , 2 )$ . In the ultra-relativistic limit, holding for both muons, we get

$$
M ^ {2} = m _ {1} ^ {2} + m _ {2} ^ {2} + 4 E _ {1} E _ {2} \sin^ {2} \frac {\theta}{2}. \tag {3.4}
$$

Substituting $m _ { 1 } = m _ { 2 } = m _ { \mu }$ and considering that the muon mass is negligible with respect to the energies of both muons, we get

$$
\begin{array}{l} M = \sqrt {2 m _ {\mu} ^ {2} + 4 E _ {1} E _ {2} \sin^ {2} \frac {\theta}{2}} \simeq 2 \sqrt {E _ {1} E _ {2}} \sin \frac {\theta}{2} \simeq \\ \simeq 2 \sqrt {7 . 4 \times 2 . 6} \sin \frac {4 2 ^ {\circ}}{2} \simeq 3. 1 \mathrm {G e V / c ^ {2}} \\ \end{array}
$$

The mass value corresponds to the one of $J / \psi$ .

The momentum of the particle can be obtained from the Carnot theorem

$$
p = \sqrt {p _ {1} ^ {2} + p _ {2} ^ {2} + 2 p _ {1} p _ {2} \cos \theta} = \sqrt {7 . 4 ^ {2} + 2 . 6 ^ {2} + 2 \times 7 . 4 \times 2 . 6 \cos 4 2 ^ {\circ}} \simeq 9. 5 \mathrm {G e V / c m ^ {3}}
$$

and its energy is then $E = \sqrt { p ^ { 2 } + M ^ { 2 } } \simeq 1 0 \mathrm { G e V } .$

Substituting $E _ { 2 } = E - E _ { 1 }$ in (3.4), we can express the opening angle as a function of $E$ and $E _ { 1 }$ :

$$
\sin {\frac {\theta}{2}} = \sqrt {\frac {M ^ {2} - m _ {1} ^ {2} - m _ {2} ^ {2}}{4 E _ {1} (E - E _ {1})}}
$$

This expression is minimum for $E _ { 1 } = E / 2$

$$
\left(\sin \frac {\theta}{2}\right) _ {\min } = \frac {\sqrt {M ^ {2} - m _ {1} ^ {2} - m _ {2} ^ {2}}}{E} \simeq \frac {M}{E} \simeq \frac {3 . 1}{1 0} = 0. 3 1
$$

which corresponds to an opening angle of $3 6 ^ { \circ }$ . The energy of the muons is then 10/2 $= 5 { \mathrm { G e V } } .$

# Exercise 3.1.17

(a) The CMS energy of a particle emitted in a two-bosy decay is $( M = m _ { \pi }$ )

$$
\epsilon_ {v} ^ {*} = \frac {m _ {\pi} ^ {2} + m _ {v} ^ {2} - m _ {\mu} ^ {2}}{2 m _ {\pi}} = \frac {m _ {\pi} ^ {2} - m _ {\mu} ^ {2}}{2 m _ {\pi}} \simeq \frac {0 . 1 4 0 ^ {2} - 0 . 1 0 6 ^ {2}}{2 \times 0 . 1 4 0} \simeq 3 0 \mathrm {M e V}
$$

(b) For a $2 0 0 \ \mathrm { G e V }$ pion the Lorentz factor and the velocity are $\gamma = p / m _ { \pi } \simeq$ $2 0 0 / 0 . 1 4 0 \simeq 1 4 2 9$ and $\beta \approx 1$ respectively. Transforming the neutrino energy to the LS we get

$$
E _ {v} = \gamma \left(\epsilon_ {v} ^ {*} + \beta p _ {v} ^ {*} \cos \theta^ {*}\right) = \gamma \epsilon_ {v} ^ {*} (1 + \beta \cos \theta^ {*})
$$

where $\theta ^ { * }$ is the neutrino emission angle in the rest frame. The maximum energy is obtained for $\theta ^ { * } = 0$ and is

$$
E _ {v} (\max) = \gamma \epsilon_ {v} ^ {*} (1 + \beta) \simeq 2 \gamma \epsilon_ {v} ^ {*} \simeq 2 \times 1 4 2 9 \times 3 0 \mathrm {M e V} \simeq 8 5. 7 \mathrm {G e V}
$$

(c) Consider neutrinos emitted at $\theta ^ { * } = 9 0 ^ { \circ }$ in the CMS. Their energy in the LS is

$$
E _ {v} \left(\theta^ {*} = 9 0 ^ {\circ}\right) = \gamma \epsilon_ {v} ^ {*} \left(1 + \beta \cos 9 0 ^ {\circ}\right) = \gamma \epsilon_ {v} ^ {*} = \frac {E _ {v} (\max )}{2} \simeq 4 2. 9 \mathrm {G e V}.
$$

Therefore forward emitted neutrinos have energies larger than this value.

(d) Using the relationship between angles under a Lorentz transformation we have

$$
\tan \theta = \frac {\sin \theta^ {*}}{\gamma (\cos \theta^ {*} + \beta)}
$$

For neutrinos in the forward hemisphere in the CMS the maximum angle corresponds to $\theta ^ { * } = 9 0 ^ { \circ }$

$$
\tan \theta_ {\max } = \frac {1}{\gamma \beta} \simeq \frac {1}{\gamma} \simeq 0. 0 0 0 7 0
$$

which is an angle of $0 . 0 4 ^ { \circ }$ .

# Exercise 3.1.18

If $p$ and $m$ are respectively the momentum and mass of the neutron, the distance it has to cover in a mean lifetime is

$$
L = \gamma \beta c \tau = \frac {p}{m} \frac {c T _ {1 / 2}}{\ln 2},
$$

$$
\mathrm {f o r} \gamma + \gamma \rightarrow e ^ {+} + e ^ {-}
$$

![](images/39a85da99e72527aaa6b48ef64c00c33bcaf87f62b05480974ce15ab315a115a.jpg)  
Fig. 3.1 Feynman diagram

where $L ( \simeq 5 0 0 0 \times 3 6 5 \times 2 4 \times 6 0 c \times 1$ minutes) is the distance of the source. Hence we get

$$
p \simeq \frac {L \times \ln 2}{T _ {1 / 2}} \times m \simeq \frac {2 . 6 1 0 ^ {9} \mathrm {m i n} \times 0 . 6 9 3}{1 0 \mathrm {m i n}} \times m \simeq 1. 8 1 0 ^ {8} \times 0. 9 4 0 \mathrm {G e V} \simeq 1. 7 1 0 ^ {1 7} \mathrm {e V / c m ^ {2}}
$$

Neutrons with such momentum are ultra-relativistic and thus also their energy has the same value.

# Exercise 3.1.19

(a) The lowest order Feynman diagram is shown in Fig. 3.1. The amplitude is proportional to $\alpha$ and the cross section to $\alpha ^ { 2 }$ .   
(b) Let us write $( E , K )$ the 4-momentum of the photon from the source and $( \epsilon , k )$ the one of the CMB photon, in the LAB system. $\pmb { K }$ and $\pmb { k }$ are opposite (head-on) and, considering also that they are massless, their sum is $E - \epsilon$ . At the threshold we have:

$$
P ^ {2} = (E + \epsilon) ^ {2} - (\mathbf {K} + \mathbf {k}) ^ {2} = (E + \epsilon) ^ {2} - (E - \epsilon) ^ {2} = (2 m _ {e}) ^ {2}
$$

$$
4 E \epsilon = 4 m _ {e} ^ {2},
$$

and therefore the minimum photon energy is

$$
E = \frac {m _ {e} ^ {2}}{\epsilon} \simeq \frac {(0 . 5 1 1 \times 1 0 ^ {6}) ^ {2}}{1 0 ^ {- 3}} \simeq 2. 6 \times 1 0 ^ {1 4} \mathrm {e V}
$$

(c) Denoting by $M$ the invariant mass, at the threshold the Lorentz factor of the CMS system is

$$
\gamma = \frac {E + \epsilon}{M} = \frac {E + \epsilon}{2 m _ {e}} \simeq 2. 5 \times 1 0 ^ {8}
$$

# 3.2 Interaction of Radiation with Matter

# Exercise 3.2.1

The number of photons as a function of the matter thickness $x$ is

$$
N (x) = N _ {0} e ^ {- \mu x}
$$

where $\mu = 0 . 0 4 \mathrm { c m } ^ { 2 } / \mathrm { g }$ for lead and $x$ is expressed in $\mathrm { g } / \mathrm { c m } ^ { 2 }$ . To halve the number of photons we require

$$
\frac {N _ {0}}{2} = N _ {0} e ^ {- \mu x _ {1 / 2}} \quad \Longrightarrow \quad x _ {1 / 2} = \frac {\ln 2}{\mu} \simeq 1 7. 3 3 \mathrm {g} / \mathrm {c m} ^ {2}.
$$

Using $\rho = 1 1 . 3 ~ \mathrm { g } / \mathrm { c m } ^ { 3 }$ , we have $\begin{array} { r } { l _ { 1 / 2 } = \frac { x _ { 1 / 2 } } { \rho } = 1 . 5 3 \mathrm { c m } } \end{array}$

For a $5 \%$ photon survival we have

$$
0. 0 5 N _ {0} = N _ {0} e ^ {- \mu x} \Rightarrow x = - \frac {1}{\mu} \ln (0. 0 5) \simeq 7 5 \mathrm {g} / \mathrm {c m} ^ {2},
$$

and then $l _ { 5 \% } = 6 . 6 3 \mathrm { c m }$ .

# Exercise 3.2.2

In the high energy limit $( E _ { \gamma } \gg m _ { e } ,$ ) the absorption coefficient for pair production is

$$
\mu = \left(\frac {7}{9}\right) X _ {0} ^ {- 1} \simeq 1. 4 \mathrm {c m} ^ {- 1}
$$

The cross section can be obtained from the absorption coefficient $\mu$ using the relationship

$$
\mu = n \sigma , \quad \text {w h e r e} \quad n = \frac {\rho N _ {A}}{A}.
$$

Using $A = 2 0 7 , \rho = 1 1 . 3 \mathrm { g / c m ^ { 3 } }$ and the Avogadro number $N _ { A } = 6 . 0 2 \cdot 1 0 ^ { 2 3 } \mathrm { m o l e } ^ { - 1 }$ we get

$$
\sigma = \frac {A}{N _ {A}} \frac {\mu}{\rho} \simeq 4. 2 \cdot 1 0 ^ {- 2 3} \mathrm {c m} ^ {2} = 4 2 \mathrm {b}
$$

# Exercise 3.2.3

Neglecting the momentum loss in the slab (see below), the radius of curvature of the muon is

$$
R = \frac {p}{0 . 3 B} \simeq 3 3. 3 \mathrm {m},
$$

where, in this equation, B, R and $p$ are given in Tesla, meter and GeV/c respectively. The muon deflection angle $\theta$ is equal to the angle of the radius at the exit with respect to the slab. For small angles the circular segment can be approximated to the slab thickness (see figure) and then we can write

$$
\theta \simeq \arcsin \left(\frac {L}{R}\right) \simeq 0. 0 1 5 \mathrm {r a d} \simeq 0. 8 6 ^ {\circ}
$$

![](images/b99a21d770cdc440fb8cef3b0f0f2f03cc1b3c50f07e78ea339b7712acf22a02.jpg)

Considering its initial energy the muon energy loss rate corresponds to the one of a minimum ionising particle, $\begin{array} { r } { \left( - \frac { d E } { d x } \right) \simeq 1 . 4 \mathrm { M e V } \mathrm { c m } ^ { 2 } / \mathrm { g } } \end{array}$ . The energy loss is then

$$
\Delta E = \left(- \frac {d E}{d x}\right) \times \rho l \simeq 5 5 0 \mathrm {M e V}.
$$

where $l = R \theta \simeq L \simeq 5 0 \mathrm { c m }$ . Since $\begin{array} { r } { \frac { \Delta E } { E } = \frac { \Delta p } { p } } \end{array}$ p , it follows that the muon momentum after the slab is

$$
p ^ {\prime} = p - \Delta p \simeq p - \Delta E \simeq 1 9. 5 \mathrm {G e V / c}.
$$

The multiple scattering dispersion in the plane of the figure is given by

$$
\sqrt {\left\langle \theta_ {s} ^ {2} \right\rangle} = \frac {E _ {s}}{\sqrt {2} \bar {p} \beta} \sqrt {\frac {l}{X _ {0}}} \simeq 4 \mathrm {m r a d} \simeq 0. 2 3 ^ {\circ}
$$

where $E _ { s } \simeq 2 0  { \mathrm { M e V } }$ is the multiple scattering constant and $\bar { p } { = } \sqrt { p p ^ { \prime } } { \simeq } 1 9 . 7 5 ~ \mathrm { G e V / c }$ (see Exercise 3.2.8). The factor $\sqrt { 2 }$ at denominator converts the spatial dispersion angle to the plane angle $( \theta _ { \mathrm { p r o j } } ^ { 2 } = \theta _ { \mathrm { s p a c e } } ^ { 2 } / 2 )$ ).

# Exercise 3.2.4

The Compton scattering cross section in the low energy limit, $E _ { \gamma } \ll m _ { e } c ^ { 2 }$ , is given by the Thomson cross section

$$
\sigma = \frac {8}{3} \pi r _ {0} ^ {2},
$$

where $r _ { 0 }$ is classical electron radius $[ = e ^ { 2 } / ( 4 \pi \epsilon _ { 0 } m c ^ { 2 } ) \simeq 2 . 8 \ \mathrm { f m } ]$ . Hence we have

$$
\lambda = \frac {1}{\sigma n} = \frac {1}{\frac {8}{3} \pi r _ {0} ^ {2} N _ {A} \frac {Z}{A} \rho} \simeq 4. 5 2 \mathrm {c m}
$$

# Exercise 3.2.5

Using the equation $p [ \mathrm { G e V / c } ] = 0 . 3 \times B [ \mathrm { T } ] \times R [ \mathrm { m } ]$ and writing the sagitta as $s \simeq$ $L ^ { 2 } / ( 8 R )$ , valid for $R \gg s$ , the electron momentum is

$$
p = 0. 3 \: B \: \frac {L ^ {2}}{8 s} \simeq 0. 3 \times 0. 1 \: \frac {0 . 0 3 ^ {2}}{8 \times 0 . 0 0 2} \simeq 1. 7 \: \mathrm {M e V / c}.
$$

The kinetic energy of the electron is $T = { \sqrt { p ^ { 2 } + m ^ { 2 } } } - m \simeq 1 . 3 { \mathrm { ~ M e V } } .$

The 4-momentum conservation in the Compton scattering can be written as

$$
E _ {\gamma} + m = E _ {\gamma} ^ {\prime} + E \quad k = k ^ {\prime} + p,
$$

being $( E _ { \gamma } , k )$ and $( m , \mathbf { 0 } )$ the initial 4-momenta of the photon and electron, and $( E _ { \gamma } ^ { \prime } , \pmb { k } ^ { \prime } )$ and $( E , p )$ the final ones. Squaring $\pmb { k } - \pmb { p } = \pmb { k } ^ { \prime }$ and solving in $E _ { \gamma }$ , we get for the initial photon energy6

$$
E _ {\gamma} = \frac {p ^ {2} - T ^ {2}}{2 (p \cos \phi - T)} \simeq 1. 6 \mathrm {M e V}.
$$

The scattered photon energy is

$$
E _ {\gamma} ^ {\prime} = E _ {\gamma} - T \simeq 0. 3 \mathrm {M e V}
$$

# Exercise 3.2.6

The mean number of pairs created by a single pion is

$$
n = \frac {\left(- \frac {d E}{d x}\right) _ {\mathrm {i o n}} \rho d}{\langle I \rangle}.
$$

In this exercise, as in many others in this book, the value of the ionization loss rate is not given for the specific case (particle, material, etc.). Most of the cases refer to relativistic singly charged particles. To help making a correct estimate one should have in mind the main features of $( - d E / d x ) _ { \mathrm { i o n } }$ that can be easily deduced from a figure of this function, e.g., as reported in the PDG Review of Particle Physics [1]. These features can be summarized as follows:

the minimum of $( - d E / d x ) _ { \mathrm { i o n } }$ is at $\beta \gamma \approx 3$ . The differences in the minimum ionization loss rate among the different materials is modest, because it is mainly determined by the ratio $Z / A$ : they change from ${ \approx } 1 . 2 ~ \mathrm { M e V } ~ \mathrm { g } ^ { - 1 } ~ \mathrm { c m } ^ { 2 }$ for Pb up to

${ \approx } 2 ~ \mathrm { M e V } ~ \mathrm { g } ^ { - 1 } ~ \mathrm { c m } ^ { 2 }$ for He. The only exception is hydrogen, whose $Z / A$ is 2 and about twice w.r.t all the other elements, which has a minimum ionization energy loss rate of ${ \approx } 4 \ \mathrm { M e V } \ \mathrm { g } ^ { - 1 } \ \mathrm { c m } ^ { 2 }$ .

In the relativistic and ultra-relativistic regimes, the increase of $( - d E / d x ) _ { \mathrm { i o n } }$ with $\beta \gamma$ is very small and in some case negligible. To have a reference number, there is a factor of about 1.5 with respect to the minimum ionization in the $\beta \gamma$ range from 3 to 10,000.   
The previous consideration is actually true only for solid and liquid materials. In these materials the energy loss is modified at increasing $\beta \gamma$ by the so-called “density effect”. Instead for gases this effect is negligible and the increase of $( - d E / d x ) _ { \mathrm { i o n } }$ with $\beta \gamma$ is somewhat larger (in the $\beta \gamma$ range from 3 to 10,000 a factor about 2).

$2 0 \mathrm { \ G e V }$ pions have $\beta \gamma \simeq 1 4 0$ and the medium in the counter is a gas (whose composition is not given). Taking into account the fact that the typical gases used in ionization counters have a minimum ionization of $1 . 5 \div 2 \ \mathrm { M e V } \ \mathrm { g } ^ { - 1 } \ \mathrm { c m } ^ { 2 }$ and a contribution due to the relativistic increase in gases, we can assume an energy loss rate

$$
\left(- \frac {d E}{d x}\right) _ {\text {i o n}} \simeq 2 \frac {\mathrm {M e V} \mathrm {c m} ^ {2}}{\mathrm {g}}.
$$

Using $d = 1 \mathrm { c m }$ , $\rho = 1 . 8 \times 1 0 ^ { - 3 } ~ \mathrm { g / c m ^ { 3 } }$ and $\langle I \rangle = 1 5 \ \mathrm { ~ e V } ,$ we get $n = 2 4 0$ pairs. Hence we have for the current

$$
I _ {\text {o u t}} = I _ {0} \times n = 2. 4 \mathrm {m A}
$$

# Exercise 3.2.7

The velocity for protons and pions are

$$
\beta_ {p} = \frac {p}{\sqrt {p ^ {2} + M _ {p} ^ {2}}} \simeq 0. 9 8 3 \quad \beta_ {\pi} = \frac {p}{\sqrt {p ^ {2} + M _ {\pi} ^ {2}}} \simeq 0. 9 9 9 6
$$

Hence they are related as

$$
\beta_ {\pi} > \beta_ {p} > \frac {1}{n _ {1}} = 0. 9 5 2
$$

So the first Cherenkov detector is sensitive to both particle types. To get the beam separation we then require a refractive index in the second detector allowing the detection of the faster particle only

$$
\beta_ {\pi} > \frac {1}{n _ {2}} > \beta_ {p}
$$

from which we get

$$
1. 0 0 0 4 <   n _ {2} <   1. 0 1 7.
$$

# Exercise 3.2.8

$5 0 0 \mathrm { M e V / c }$ muons have $\beta \gamma \simeq 4 . 7$ and so they are close to the ionization minimum. For the copper slab we can assume

$$
\left(- \frac {d E}{d x}\right) _ {\mathrm {i o n}} = 1. 4 \frac {\mathrm {M e V}}{\mathrm {g c m} ^ {- 2}}.
$$

The thickness to stop the muon beam is the range for these muons. A simple estimate can be done assuming that the energy loss is constant along the particle trajectory

$$
R = \frac {1}{\rho} \int_ {0} ^ {T} \frac {d T}{(- d E / d x) _ {\mathrm {i o n}}} \simeq
$$

$$
\simeq \frac {1}{\rho} \frac {T}{(- d E / d x) _ {\mathrm {i o n}}} = \frac {\sqrt {p ^ {2} + M ^ {2}} - M}{\rho (- d E / d x) _ {\mathrm {i o n}}} \simeq \frac {4 0 5 \mathrm {M e V}}{9 \times 1 . 4 \mathrm {M e V / c m}} \simeq 3 2 \mathrm {c m},
$$

where $T$ and $p$ are the initial muon kinetic energy and momentum respectively, and $M$ is their mass. A better value for the range can be obtained from the graph $R / M$ versus $\beta \gamma$ shown in the figure below, taken from the PDG Review of Particle Physics [1]. From this figure we deduce for an element (Fe) close to the copper $R / M \simeq 2 3 0 0 \mathrm { g c m } ^ { - 2 } / \mathrm { G e V } .$ . Substituting to $M$ the muon mass we get $R \simeq 2 7 \mathrm { c m }$ .

![](images/02053de3959c2f80bd876c0fc73f72628fc68725769164accb108a4935d0a23d.jpg)

The kinetic energy lost in a $1 0 \mathrm { { c m } }$ slab is

$$
\Delta T = \left(- \frac {d E}{d x}\right) _ {\mathrm {i o n}} \rho d = 1 2 6 \mathrm {M e V}.
$$

Hence the mean energy of the muons after the slab crossing is

$$
T ^ {\prime} = T - \Delta T \simeq 2 7 9 \mathrm {M e V}.
$$

The multiple scattering angle at the exit has to be calculated taking into account the ionization energy loss in the slab, because this loss is not negligible $\Delta T / T \ \simeq$ $1 2 6 / 4 0 5 \simeq 3 1 \%$ . The calculation has to be done as follows

$$
d \theta^ {2} = \left(\frac {E _ {s}}{p \beta}\right) ^ {2} \frac {d x}{X _ {0}} = \left(\frac {E _ {s}}{p \beta}\right) ^ {2} \frac {d p \beta}{X _ {0} (- d p \beta / d x) _ {\mathrm {i o n}}}.
$$

where $X _ { 0 }$ , converted to $\mathrm { g } / \mathrm { c m } ^ { 2 }$ , is $1 . 4 \times 9 = 1 2 . 6 ~ \mathrm { g } / \mathrm { c m } ^ { 2 }$ and $( - d p \beta / d x ) _ { \mathrm { i o n } }$ , the $p \beta$ loss rate, can be obtained from the ionization energy loss rate as

$$
\left(- \frac {d p \beta}{d x}\right) _ {\mathrm {i o n}} = \left(- \frac {d E}{d x}\right) _ {\mathrm {i o n}} \frac {d p \beta}{d T}.
$$

We can write

$$
p \beta = \frac {p ^ {2}}{E} = \frac {(T + M) ^ {2} - M ^ {2}}{T + M} = T \left(1 + \frac {M}{T + M}\right) \tag {3.5}
$$

hence we get

$$
\left(- \frac {d p \beta}{d x}\right) _ {\text {i o n}} = \left(- \frac {d E}{d x}\right) _ {\text {i o n}} \left[ 1 + \left(\frac {M}{T + M}\right) ^ {2} \right] = \left(- \frac {d E}{d x}\right) _ {\text {i o n}} [ 1 + \epsilon (T) ]
$$

The function $\epsilon ( T )$ is ${ \sim } 4 \%$ for the entrance energy and ${ \sim } 7 . 5 \%$ for the exit energy. For an estimate of the scattering angle (within an accuracy of less than $10 \%$ ) we can neglect such function in the previous expression and calculate the r.m.s. scattering angle as

$$
\begin{array}{l} \theta_ {s} ^ {2} = \langle \theta^ {2} \rangle = \int_ {(p \beta) _ {i}} ^ {(p \beta) _ {f}} d \theta^ {2} = \frac {E _ {s} ^ {2}}{X _ {0} (- d E / d x) _ {\mathrm {i o n}}} \int_ {(p \beta) _ {i}} ^ {(p \beta) _ {f}} \frac {d p \beta}{(p \beta) ^ {2}} = \\ = \frac {E _ {s} ^ {2}}{X _ {0} (- d E / d x) _ {\text {i o n}}} \frac {(p \beta) _ {f} - (p \beta) _ {i}}{(p \beta) _ {f} (p \beta) _ {i}}, \tag {3.6} \\ \end{array}
$$

where $( p \beta ) _ { i } \simeq 4 8 9 \mathrm { M e V / c }$ and $( p \beta ) _ { f } \simeq 3 5 6 \mathrm { M e V / c }$ are the $p \beta$ value corresponding to the entrance and exit of the muons. In the previous expression we have assumed constant the energy loss rate within the integration range. Hence we obtain

$$
\theta_ {s} ^ {2} = \frac {2 0 ^ {2}}{1 2 . 6 \cdot 1 . 4} \frac {4 8 9 - 3 5 6}{4 8 9 \cdot 3 5 6} \simeq 0. 0 1 7
$$

and

$$
\theta_ {s} \simeq 0. 1 3 2 \mathrm {r a d} \simeq 7. 5 ^ {\circ}.
$$

Equation (3.6) allows to get a simple rule to calculate the multiple scattering angle to be used in case of sizeable energy loss. In fact, considering that we have $( p \beta ) _ { f } \ : -$ $( p \beta ) _ { i } \approx ( - d E / d x ) _ { \mathrm { i o n } } \times d$ , the r.m.s. scattering angle can be written as in the case of $p \beta$ constant

$$
\theta_ {s} = \left(\frac {E _ {s}}{[ p \beta ]}\right) \sqrt {\frac {d}{X _ {0}}}
$$

replacing $p \beta$ with the geometric mean $[ p \beta ] = \sqrt { ( p \beta ) _ { f } ( p \beta ) _ { i } } ~ \simeq 4 1 7 ~ \mathrm { M e V / c } .$

# Exercise 3.2.9

The energy of the photons which are incident on the silver foil is

$$
E _ {\gamma} = \frac {h c}{\lambda} \simeq \frac {6 . 2 8 \times 1 9 7 1 0 ^ {6} \times 1 0 ^ {- 6} \mathrm {e V} \mathrm {n m}}{2 0 0 \mathrm {n m}} \simeq 6. 2 \mathrm {e V}.
$$

To have the photoelectric effect the photon energy must fulfill the condition $E _ { \gamma } > W$ . With $W = 4 . 7 3 \mathrm { e V }$ the photoelectric process is allowed. The electron kinetic energy is $E _ { K } = E _ { \gamma } - W = 1 . 4 7 \ : \mathrm { e V } .$ .

# Exercise 3.2.10

According to the Heitler toy model, the depth $T$ at which the shower reaches the maximum development is given by the equation $2 ^ { T } = E _ { 0 } / E _ { \mathrm { c r i t } }$ . Hence we have

$$
T = \frac {\log_ {1 0} \left(E _ {0} / E _ {\mathrm {c r i t}}\right)}{\log_ {1 0} 2} = \frac {\log_ {1 0} (1 0 0 \mathrm {G e V} / 8 0 \mathrm {M e V})}{\log_ {1 0} 2} \simeq 1 0. 3
$$

where $T$ is given in units of radiation lengths. Hence the air thickness is

$$
X _ {\max } = T \times X _ {0} = 1 0. 3 \times 3 7 \mathrm {g} / \mathrm {c m} ^ {2} \simeq 3 8 0 \mathrm {g} / \mathrm {c m} ^ {2}
$$

# Exercise 3.2.11

The photons emitted in the $e ^ { + } e ^ { - }$ annihilation at rest have energy $E _ { \gamma } = M / 2 = m _ { e }$ being $M = 2 m _ { e }$ and $m _ { e }$ the electron mass. In the Compton process the scattered photons have energy

Appendix: Solutions of Exercises and Problems

$$
E _ {\gamma} ^ {\prime} = \frac {E _ {\gamma}}{1 + E _ {\gamma} / m _ {e} (1 - \cos \theta)}
$$

from which it follows that the extremal electron kinetic energies are for cos $\theta = 1$ and co $\displaystyle { | \mathbf { s } \theta = - 1 }$

$$
\left(T _ {e}\right) _ {\min } = E _ {\gamma} - \left(E _ {\gamma} ^ {\prime}\right) _ {\max } = E _ {\gamma} - E _ {\gamma} = 0
$$

$$
(T _ {e}) _ {\max } = E _ {\gamma} - \left(E _ {\gamma} ^ {\prime}\right) _ {\min } = E _ {\gamma} - \frac {E _ {\gamma} m _ {e}}{2 E _ {\gamma} + m _ {e}} = \frac {2}{3} m _ {e} \simeq 0. 3 4 \mathrm {M e V}
$$

# Exercise 3.2.12

Assuming an energy loss rate of $2 \mathrm { M e V } / ( \mathrm { g } \cdot \mathrm { c m } ^ { - 2 } )$ , the minimum kinetic energy for a vertical muon to reach ground7 is

$$
T _ {\min } \simeq \left(- \frac {d E}{d x}\right) _ {\text {i o n}} \times \Delta x \simeq 2 \frac {\mathrm {M e V}}{\mathrm {g} \cdot \mathrm {c m} ^ {- 2}} \times 1 0 3 0 \mathrm {g} \cdot \mathrm {c m} ^ {- 2} \simeq 2. 1 \mathrm {G e V}
$$

The number of ionized electrons are

$$
N _ {e} = \frac {T _ {\mathrm {m i n}}}{\langle I \rangle} \simeq \frac {2 . 1 \times 1 0 ^ {9} \mathrm {e V}}{1 0 \mathrm {e V}} \simeq 1 0 ^ {8}.
$$

# Exercise 3.2.13

We notice first that the plate thickness is much smaller than a radiation length so that we can neglect the electron energy loss. In this condition the r.m.s. scattering angle is simply

$$
\theta_ {s} = \sqrt {\langle \theta^ {2} \rangle} \simeq \frac {E _ {s}}{E _ {0}} \sqrt {\frac {x}{X _ {0}}}
$$

where $E _ { 0 }$ is the electron energy, $E _ { s } \simeq 2 0 \ \mathrm { M e V }$ and $x = X _ { 0 } / 2 0$ . Considering the electron bremsstrahlung the dispersion angle is about

$$
\theta_ {b} \simeq \frac {m _ {e}}{E _ {0}}
$$

where $m _ { e }$ is the electron mass. We have

$$
\theta_ {s} = \frac {2 0}{1 0 0 0} \sqrt {\frac {1}{2 0}} \simeq 4. 5 \mathrm {m r a d} \gg \theta_ {\mathrm {b}} = \frac {0 . 5}{1 0 0 0} \simeq 0. 5 \mathrm {m r a d}
$$

and then the angular distribution is dominated by the multiple scattering.

# Exercise 3.2.14

For muons $\ ^ { \prime } E = 3 \mathrm { G e V } ,$ ) in copper we can assume (see Exercise 3.2.6) a ionization energy loss rate

$$
\left(- \frac {d E}{d x}\right) _ {\text {i o n}} = 1. 8 \frac {\mathrm {M e V}}{\mathrm {g} \mathrm {c m} ^ {- 2}}.
$$

In a $d = 1 0 \mathrm { c m }$ thick slab muons lose an energy

$$
\Delta E = \left(- \frac {d E}{d x}\right) _ {\mathrm {i o n}} \rho d = 0. 1 6 \mathrm {G e V},
$$

and so we have $E \gg \Delta E$ . The lateral beam broadening can be calculated assuming that the muon energy is unaffected by the slab crossing and we can write

$$
\langle (\rho r) ^ {2} \rangle = \int_ {0} ^ {x _ {S}} x ^ {2} d \theta^ {2} = \int_ {0} ^ {x _ {S}} d x \frac {x ^ {2}}{X _ {0}} \left(\frac {E _ {s}}{p \beta}\right) ^ {2} \simeq \frac {x _ {S} ^ {3}}{3 X _ {0}} \left(\frac {E _ {s}}{p \beta}\right) ^ {2}
$$

where $x _ { S } = d \rho \simeq 9 0 ~ \mathrm { g / c m } ^ { 2 }$ is the slab mass thickness and $E _ { s } = 2 0 ~ \mathrm { M e V }$ is the scattering constant. Hence we have

$$
\sqrt {\langle (\rho r) ^ {2} \rangle} \simeq x _ {S} \sqrt {\frac {x _ {S}}{3 X _ {0}}} \left(\frac {E _ {s}}{p \beta}\right)
$$

Since $E \gg M _ { \mu }$ , we can write $p \beta \approx E$ and finally get for the beam broadening

$$
\sqrt {\langle r ^ {2} \rangle} \simeq 1 0 \sqrt {\frac {9 0}{3 \times 1 3 . 3}} \left(\frac {2 0}{3 0 0 0}\right) \simeq 0. 1 \mathrm {c m}.
$$

# Exercise 3.2.15

The quantity $z ^ { 2 } R / M$ (where $z$ is the charge in $e$ units, $R$ the range and $M$ the mass of the particle) is a universal function of $\beta \gamma = p / M .$ . As an example an $\alpha$ -particle having a kinetic energy $T _ { \alpha }$ has the same range of a proton with kinetic energy $T _ { p } = T _ { \alpha } / 4$ (same $\beta \gamma$ ), because $z _ { \alpha } ^ { 2 } / M _ { \alpha } = 1 / M _ { p }$ .

# Exercise 3.2.16

Electrons having $E = 1 \mathrm { G e V }$ loose energy by bremstrahlung as

$$
\left(- \frac {d E}{d x}\right) _ {\mathrm {b r e m}} = \frac {E}{X _ {0}}.
$$

Therefore the mean electron energy after crossing a plate of thickness $x$ is

$$
E (x) = E _ {0} \exp \left(- \frac {x}{X _ {0}}\right). \tag {3.7}
$$

$X _ { 0 }$ is the aluminium radiation length whose inverse is

$$
\frac {1}{X _ {0}} \approx D \frac {Z ^ {2}}{A} \ln (1 8 3 Z ^ {- 1 / 3}) \simeq 3. 8 \times 1 0 ^ {- 2} \mathrm {c m} ^ {2} / \mathrm {g}.
$$

The radiated energy corresponds to the value of $E ( x )$ in Eq. (3.7) at $x = \rho d \simeq$ $1 3 . 5 \ : \mathrm { g } / \mathrm { c m } ^ { 2 }$ , and then is

$$
\langle E _ {\gamma} \rangle = \Delta E = E _ {0} \left[ 1 - \exp \left(- \frac {x}{X _ {0}}\right) \right] \simeq 0. 4 0 \times E _ {0} = 4 0 0 \mathrm {M e V}.
$$

# Exercise 3.2.17

(a) In vacuum muons travel along a circular orbit whose radius is

$$
R [ \mathrm {m} ] = \frac {p [ \mathrm {G e V / c} ]}{0 . 3 B [ \mathrm {T} ]} \simeq 1 6. 7 \mathrm {m}
$$

(b) Muons have an initial energy

$$
E _ {0} = \sqrt {p _ {0} ^ {2} + m ^ {2}} = 5 1 1 \mathrm {M e V}
$$

and a $\beta \gamma$ equal to $p / m \simeq 4 . 7 $ . Hence we can assume for the energy loss rate in the gas a value close to that of a minimum ionizing particle

$$
\left(\frac {d E}{d x}\right) _ {\text {i o n}} \simeq 2 \frac {\mathrm {M e V}}{\mathrm {g} / \mathrm {c m} ^ {2}}.
$$

The energy lost after a complete round is approximately8

$$
\Delta E \simeq \left(\frac {d E}{d x}\right) _ {\text {i o n}} \rho \times 2 \pi R \simeq 4 2 \mathrm {M e V}
$$

and the final energy is $E _ { 1 } = E _ { 0 } - \Delta E \simeq 4 6 9 \mathrm { ~ M e V } .$ The corresponding muon momentum is $p _ { 1 } = \sqrt { E _ { 1 } ^ { 2 } - m ^ { 2 } } \simeq 4 5 7 \mathrm { ~ M e V / c }$ and so the radius of curvature after one round is $R _ { 1 } \simeq 1 5 . 2 \ : \mathrm { m }$ .

# Exercise 3.2.18

The scattered photon energy as a function of the scattering angle $\theta$ is

$$
E _ {\gamma} ^ {\prime} = \frac {E _ {\gamma}}{1 + \epsilon (1 - \cos \theta)}
$$

where $\epsilon = E _ { \gamma } / m \simeq 1$ , for $0 . 5 \mathrm { M e V }$ photons. If $E$ , $T$ and $m$ are the energy, kinetic energy and mass of the scattered electron, from the energy conservation we have

$$
E _ {\gamma} + m = E _ {\gamma} ^ {\prime} + E
$$

and then

$$
T = E - m = E _ {\gamma} - E _ {\gamma} ^ {\prime} = E _ {\gamma} \frac {\epsilon (1 - \cos \theta)}{1 + \epsilon (1 - \cos \theta)}
$$

The maximum energy is obtained when the photon is scattered backward $( \theta = \pi$ ) and hence we obtain for the Compton edge energy

$$
T _ {\max } = E _ {\gamma} \frac {2 \epsilon}{1 + 2 \epsilon} \simeq \frac {2}{3} E _ {\gamma} \simeq 0. 3 3 \mathrm {M e V}
$$

# Exercise 3.2.19

The energy of the Compton scattered photon as a function of $\theta$ is

$$
E _ {\gamma} ^ {\prime} = \frac {E _ {\gamma}}{1 + \epsilon (1 - \cos \theta)}
$$

where $\epsilon = E _ { \gamma } / m$ . The electron kinetic energy is then

$$
T = E - m = E _ {\gamma} - E _ {\gamma} ^ {\prime} = E _ {\gamma} \frac {\epsilon (1 - \cos \theta)}{1 + \epsilon (1 - \cos \theta)}
$$

This energy is maximum for $\theta = \pi$ and this value corresponds to the co-called ‘Compton edge’

$$
T _ {\mathrm {m a x}} = E _ {\gamma} \frac {2 \epsilon}{1 + 2 \epsilon} = E _ {\gamma} \frac {2 E _ {\gamma}}{m + 2 E _ {\gamma}}.
$$

Solving the equation in $E _ { \gamma }$ we have

$$
E _ {\gamma} = \frac {T _ {\max } + \sqrt {T _ {\max } \left(T _ {\max } + 2 m\right)}}{2}. \tag {3.8}
$$

The three $T _ { \mathrm { m a x } }$ values shown in the figure are about 0.22, 0.62 and $0 . 8 0 \mathrm { M e V } .$ . Knowing that in $\gamma$ -transitions, neglecting the nucleus recoil, $Q _ { \gamma } = E _ { \gamma }$ , from (3.8) we get

$$
Q _ {\gamma} (1) \simeq 0. 3 7 \mathrm {M e V}, \quad Q _ {\gamma} (2) \simeq 0. 8 1 \mathrm {M e V}, \quad Q _ {\gamma} (3) \simeq 1. 0 \mathrm {M e V}
$$

# Exercise 3.2.20

(a) The muon velocity is

Appendix: Solutions of Exercises and Problems

$$
\beta = \frac {p}{E} = \frac {p}{\sqrt {p ^ {2} + m ^ {2}}} = \frac {1 0}{\sqrt {1 0 ^ {2} + 0 . 1 0 6 ^ {2}}} \simeq 0. 9 9 9 9 4 4
$$

Thus Cherenkov effect is done because we have

$$
\beta \simeq 0. 9 9 9 9 4 4 > \frac {1}{n} = \frac {1}{1 . 0 0 0 2 9} \simeq 0. 9 9 9 7 1
$$

(b) The Cherenkov opening angle is given by

$$
\cos \theta_ {C} = \frac {1}{n \beta} \simeq \frac {1}{1 . 0 0 0 2 9 \times 0 . 9 9 9 9 4 4} \simeq 0. 9 9 9 7 7
$$

corresponding to an angle of $1 . 2 ^ { \circ }$

(c) The number of Cherenkov photons per unit length in the visible bandwidth is

$$
N _ {\mathrm {p h}} / L \approx z ^ {2} \frac {\alpha}{c} \Delta \omega \sin^ {2} \theta_ {C} \approx z ^ {2} 7 5 0 \sin^ {2} \theta_ {C} \mathrm {c m} ^ {- 1},
$$

where $\Delta \omega$ corresponds to the visible and near UV bandwidth, where Cherenkov radiation is possible $\hbar \Delta \omega \approx 2 \mathrm { e V }$ ). $1 0 \mathrm { G e V }$ muons produced at $1 0 \mathrm { k m }$ reach the sea level since their mean decay length is $( \tau _ { \mu } \simeq 2 . 2 \mu \mathrm { s } )$ :

$$
l _ {\mu} = \beta \gamma c \tau_ {\mu} = \frac {p _ {\mu}}{m _ {\mu}} c \tau_ {\mu} \simeq \frac {1 0}{0 . 1 0 6} 3 1 0 ^ {5} 2. 2 1 0 ^ {- 6} \mathrm {k m} \simeq 6 2 \mathrm {k m},
$$

and then emit Cherenkov photons along their whole pathlengths. For muons hitting normally the Earth surface $\begin{array} { r } { \theta _ { Z } = 0 } \end{array}$ ) we have

$$
N _ {\mathrm {p h}} \approx 7 5 0 (1 - \cos^ {2} \theta_ {C}) \times L \simeq 7 5 0 (1 - 0. 9 9 9 7 7 ^ {2}) \mathrm {c m} ^ {- 1} \times 1 0 ^ {6} \mathrm {c m} \simeq 3. 4 1 0 ^ {5}.
$$

For angles $\theta _ { Z } > 0$ , the number of photons scales as sec $\theta _ { Z }$

# Exercise 3.2.21

From the 4-momentum conservation in the Compton scattering we have

$$
E _ {\gamma} + m = E _ {\gamma} ^ {\prime} + E \quad k = k ^ {\prime} + p
$$

where $( E _ { \gamma } , \pmb { k } )$ , $( E _ { \gamma } ^ { \prime } , \pmb { k } ^ { \prime } )$ and $( E , p )$ are the 4-momenta of the incident photon, scattered photon and scattered electron respectively. We need to calculate the relationship between the initial photon and the scattered electron as a function of the electron angle $\phi$ . To get this we write

$$
\begin{array}{l} \boldsymbol {k} ^ {\prime 2} = (\boldsymbol {k} - \boldsymbol {p}) ^ {2} = k ^ {2} + p ^ {2} - 2 k p \cos \phi = E _ {\gamma} ^ {2} + p ^ {2} - 2 E _ {\gamma} p \cos \phi \\ \boldsymbol {k} ^ {\prime 2} = E _ {\gamma} ^ {\prime 2} = (E _ {\gamma} + m - E) ^ {2} = (E _ {\gamma} - T) ^ {2} \\ \end{array}
$$

where $T$ is the electron kinetic energy. Hence we have

$$
E _ {\gamma} = \frac {p ^ {2} - T ^ {2}}{2 (p \cos \phi - T)}
$$

(a) An electron having an angle $\phi$ within the fibre acceptance releases its whole kinetic energy, because it has enough pathlength to come at rest. Thus the measured energy release corresponds to the kinetic energy of the electron at $\phi = 3 0 ^ { \circ }$ and we have for the source energy

$$
E _ {\gamma} \simeq \frac {2 . 4 6 ^ {2} - 2 ^ {2}}{2 \cdot (2 . 4 6 \cdot \cos 3 0 ^ {\circ} - 2)} \simeq 7. 9 \mathrm {M e V},
$$

where we have used $p = \sqrt { ( T + m ) ^ { 2 } - m ^ { 2 } } \simeq 2 . 4 6 \mathrm { M e V / c }$ . (b) The Klein–Nishina cross section is

$$
\frac {d \sigma}{d \Omega} = \frac {r _ {0} ^ {2}}{2} \left(\frac {E _ {\gamma} ^ {\prime}}{E _ {\gamma}}\right) ^ {2} \left[ \frac {E _ {\gamma} ^ {\prime}}{E _ {\gamma}} + \frac {E _ {\gamma}}{E _ {\gamma} ^ {\prime}} - \sin^ {2} \theta \right] \tag {3.9}
$$

where $\theta$ is the photon scattering angle. To get this angle we equate the photon and electron transverse momenta

$$
p \sin \phi = E _ {\gamma} ^ {\prime} \sin \theta \quad \Longrightarrow \quad \sin \theta = \frac {p}{E _ {\gamma} ^ {\prime}} \sin \phi
$$

The photon energy $E _ { \gamma } ^ { \prime }$ , corresponding to the electron emitted at $3 0 ^ { \circ }$ , can be derived from $E _ { \gamma } ^ { \prime } = E _ { \gamma } - T$ . Hence we have $E _ { \gamma } ^ { \prime } / E _ { \gamma } \simeq 0 . 7 5$ and s $\mathrm { i n } \theta \simeq 0 . 2 1$ . Substituting these values in (3.9) we get

$$
\frac {d \sigma}{d \Omega} \simeq \frac {2 . 8 \mathrm {f m} ^ {2}}{2} \times 0. 7 5 ^ {2} \times (0. 7 5 + 1 / 0. 7 5 - 0. 2 1 ^ {2}) \simeq 4. 5 1 0 ^ {- 2 6} \mathrm {c m} ^ {2} / \mathrm {s r}.
$$

The cross section for all the accepted electrons is this differential cross section multiplied by the acceptance solid angle

$$
\Delta \Omega = 2 \pi \int_ {0} ^ {1 5 ^ {\circ}} d \cos \theta = 2 \pi (1 - \cos 1 5 ^ {\circ}) \simeq 6. 2 8 \times (1 - 0. 9 6 6) \simeq 0. 2 1 \mathrm {s r}
$$

Hence we have

$$
\sigma_ {\mathrm {a c c}} \simeq \frac {d \sigma}{d \Omega} \Delta \Omega \simeq 4. 5 1 0 ^ {- 2 6} \times 0. 2 1 \simeq 9. 5 1 0 ^ {- 2 7} \mathrm {c m} ^ {2}.
$$

(c) The Compton absorption coefficient for the accepted electrons is

$$
\mu_ {\mathrm {a c c}} = N \frac {Z}{A} \rho \sigma_ {\mathrm {a c c}} \simeq 6 1 0 ^ {2 3} \times 0. 5 \times 1 \times 9. 5 1 0 ^ {- 2 7} \simeq 0. 0 0 2 9 \mathrm {c m} ^ {- 1}
$$

where we have taken into account that $Z$ electrons per each atom contribute to the scattering. The number of detected electrons per incident photon is then

$$
\frac {N _ {e}}{N _ {\gamma}} \simeq \frac {d}{\sin 3 0 ^ {\circ}} \mu_ {\mathrm {a c c}} \simeq \frac {0 . 2}{0 . 5} \times 0. 0 0 2 9 \simeq 0. 0 0 1.
$$

# Exercise 3.2.22

By definition $E ( x ) = E _ { 0 } \exp ( - x / X _ { 0 } )$ $E ( x ) = E _ { 0 }$ , where $X _ { 0 }$ is the radiation length. The mean energy loss is then $\Delta E = E _ { 0 } - E ( X _ { 0 } ) = E _ { 0 } ( 1 - 1 / e ) = 0 . 6 3 \mathrm { G e V } .$

# 3.3 Detection Techniques and Experimental Methods

# Exercise 3.3.1

(1) The inverse of $\beta$ is given by

$$
\frac {1}{\beta} = \frac {1}{\sqrt {1 - \frac {1}{\gamma^ {2}}}}.
$$

Since $E \gg m$ , we have $\gamma \gg 1$ , so that can use the relationship, valid for $x \to 0$

$$
\frac {1}{\sqrt {1 - x ^ {2}}} \simeq 1 + \frac {1}{2} x ^ {2}.
$$

The difference between the time-of-flights of two particles having velocities $\beta _ { 1 }$ and $\beta _ { 2 }$ is

$$
\begin{array}{l} \Delta T = \frac {L}{\beta_ {1} c} - \frac {L}{\beta_ {2} c} \simeq \frac {L}{c} \left(1 + \frac {1}{2 \gamma_ {1} ^ {2}} - 1 - \frac {1}{2 \gamma_ {2} ^ {2}}\right) = \frac {L}{2 c} \left(\frac {1}{\gamma_ {1} ^ {2}} - \frac {1}{\gamma_ {2} ^ {2}}\right) = \\ = \frac {L}{2 c} \left(\frac {m _ {1}}{E _ {1} ^ {2}} - \frac {m _ {2}}{E _ {2} ^ {2}}\right) \simeq \frac {L}{2 c} \left(\frac {m _ {1} ^ {2}}{p _ {1} ^ {2}} - \frac {m _ {2} ^ {2}}{p _ {2} ^ {2}}\right) = \frac {L}{2 c} \frac {m _ {1} ^ {2} - m _ {2} ^ {2}}{p ^ {2}}, \\ \end{array}
$$

having set $p _ { 1 } = p _ { 2 } = p$ in the last step.

(2) The difference in time-of-flight between pions and kaons is

$$
\Delta T = \frac {L}{2 c} \frac {\Delta m ^ {2}}{p ^ {2}} = \frac {3 \mathrm {m}}{2 c} \frac {0 . 4 9 3 ^ {2} - 0 . 1 3 9 ^ {2}}{1} \simeq \frac {3 \mathrm {m} \times 0 . 2 2 4}{2 \times 3 \times 1 0 ^ {8} \mathrm {m / s}} \simeq 1. 1 2 \mathrm {n s}
$$

Using the time resolution requirement, $\Delta T = 4 \sigma _ { t }$ , we obtain for the time resolution needed for each counter

$$
\sigma \simeq \frac {1 . 1 2 \mathrm {n s}}{4 \sqrt {2}} \simeq 0. 2 \mathrm {n s},
$$

where we have used the relationship $\sigma _ { t } ^ { 2 } = \sigma ^ { 2 } ( T _ { 1 } - T _ { 2 } ) = \sigma ^ { 2 } ( T _ { 1 } ) + \sigma ^ { 2 } ( T _ { 2 } ) = 2 \sigma ^ { 2 }$ . (3) When S1 and S2 are segmented and a third scintillator S3 is inserted in the middle, the system can be used as a spectrometer.

(a) The space resolution of each scintillator is $\sigma _ { y } { = } 5 \mathrm { c m } / \sqrt { 1 2 } \simeq 1 . 4 4 \mathrm { c m }$ (y is the direction orthogonal to the beam in the figure). The lateral spread due to the multiple scattering (see Exercise 3.2.14), in the same direction, is:

$$
\sigma_ {y} \simeq \frac {x}{\sqrt {3}} \frac {E _ {s}}{\sqrt {2} p \beta} \sqrt {\frac {x}{X _ {0}}} \simeq \frac {1 \mathrm {c m} 1 4 \mathrm {M e V}}{\sqrt {3} 1 0 0 0 \mathrm {M e V} \beta} \sqrt {\frac {1}{4 0}} \simeq \frac {0 . 0 1 3}{\beta} \mathrm {m m},
$$

which turns out to be negligible for both particles ${ \beta } _ { \pi } \simeq 0 . 9 9$ , $\beta _ { K } \simeq 0 . 9 0$ ) with respect to the resolution.

(b) The sagitta is

$$
s = 0. 3 \frac {B L ^ {2}}{8 p} = \frac {0 . 3 \times 1 \mathrm {T} \times 9 \mathrm {m} ^ {2}}{8 \times 1 \mathrm {G e V / c}} \simeq 0. 3 3 7 \mathrm {m} = 3 3. 7 \mathrm {c m}.
$$

The sagitta is measured as $s \simeq y _ { 3 } - ( y _ { 1 } + y _ { 2 } ) / 2$ and the uncertainty on each $y _ { i }$ is $\sigma _ { y }$ . Hence we have for the sagitta uncertainty

$$
\sigma_ {s} \simeq \sqrt {\frac {3}{2}} \sigma_ {y} \simeq 1. 7 6 \mathrm {c m}.
$$

The relative error on the momentum measurement is finally

$$
\frac {\Delta p}{p} \simeq \frac {\Delta s}{s} = \frac {1.76 \mathrm {cm}}{33.7 \mathrm {cm}} \simeq 5 \%
$$

# Exercise 3.3.2

The radius $R$ of the orbit at $t = t _ { o }$ is

$$
R [ \mathrm {m} ] = \frac {p [ \mathrm {G e V} / c ]}{0 . 3 B [ \mathrm {T} ]} = \frac {0 . 3}{0 . 3 \times 0 . 5} \mathrm {m} \simeq 2 \mathrm {m}.
$$

A $3 0 0 ~ \mathrm { M e V / c }$ muon $\beta \gamma \simeq 3 )$ is at the minimum of the ionization loss rate. The medium is not specified but it may be a gas, considering its density. Let assume to be air for which the minimum ionization loss is ${ \approx } 1 . 8 \mathrm { M e V } \mathrm { g } ^ { - 1 } \mathrm { c m } ^ { 2 }$ . For the energy loss in iron we use instead ${ \approx } 1 . 5 \mathrm { M e V } \mathrm { g } ^ { - 1 } \mathrm { c m } ^ { 2 }$ $\mathbf { g } ^ { - 1 } \mathbf { c m } ^ { 2 }$ . Under this assumption we have

Appendix: Solutions of Exercises and Problems

$$
\begin{array}{l} \Delta E \simeq 1. 5 \frac {\mathrm {M e V}}{\mathrm {g} \mathrm {c m} ^ {- 2}} \times \rho_ {\mathrm {F e}} \times 2 d _ {\mathrm {F e}} + 1. 8 \frac {\mathrm {M e V}}{\mathrm {g} \mathrm {c m} ^ {- 2}} \times \rho_ {\mathrm {a i r}} \times 2 \pi R \simeq \\ = 1. 5 \times 7. 8 7 \times 2 \times 0. 2 + 1. 8 \times 1 0 ^ {- 3} \times 2 \pi \times 2 0 0 = 6. 9 8 \mathrm {M e V}. \\ \end{array}
$$

The initial muon energy is

$$
E = \sqrt {p ^ {2} + m ^ {2}} \simeq \sqrt {3 0 0 ^ {2} + 1 0 6 ^ {2}} \mathrm {M e V} \simeq 3 1 8 \mathrm {M e V};
$$

After one turn the energy becomes

$$
E ^ {\prime} = E - \Delta E \simeq 3 1 8 - 6. 9 8 \mathrm {M e V} = 3 1 1 \mathrm {M e V}.
$$

and the momentum is

$$
p ^ {\prime} = \sqrt {E ^ {\prime 2} - m ^ {2}} \simeq \sqrt {3 1 1 ^ {2} - 1 0 6 ^ {2}} = 2 9 2 \mathrm {M e V / c}.
$$

(a) The magnetic field needed to keep the muon in an orbit of radius $R$ after one turn is

$$
B ^ {\prime} = \frac {p ^ {\prime} [ \mathrm {G e V / c} ]}{0 . 3 R [ \mathrm {m} ]} \simeq 0. 4 8 6 \mathrm {T}
$$

and hence we have $\Delta B = B ^ { \prime } - B \simeq 0 . 4 8 6 - 0 . 5 \simeq - 0 . 0 1 4 \mathrm { T } .$

(b) The muon mean decay pathlength is $\lambda = \beta \gamma c \tau$ , where $\beta \gamma = p / m$ . Hence we have

$$
\lambda = \frac {p}{m} c \tau \simeq \frac {3 0 0 \times 3 1 0 ^ {8} \times 2 . 2 1 0 ^ {- 6}}{1 0 6} \simeq 1 8 6 8 \mathrm {m}.
$$

The mean number of turns is then

$$
\langle n _ {\text {t u r n s}} \rangle = \frac {\lambda}{2 \pi R} \simeq \frac {1 8 6 8}{4 \pi} \simeq 1 4 9.
$$

# Exercise 3.3.3

1. Muons come at rest in water loosing their kinetic energy by ionization. The energy lost by Cherenkov effect is negligible (order of per mill). Muons with 1 GeV/c momentum $\begin{array} { r } { { \cal I } m = 1 0 6 \mathrm { M e V } / \mathrm { c } ^ { 2 } , } \end{array}$ ) are close to the ionization minimum and we can use an energy loss rate of about $2 ~ \mathrm { M e V } / ( \mathrm { g } ~ \mathrm { c m } ^ { - 2 } )$ $( = 2 ~ \mathrm { M e V / c m }$ in water). A simple estimate of the total pathlength can be done under the assumption that the changes in energy loss rate along the muon path can be neglected

$$
R (E) \simeq \int_ {0} ^ {T} \frac {d E}{(- d E / d l) _ {\mathrm {i o n}}} \simeq \int_ {0} ^ {T} \frac {d E}{2 \mathrm {M e V / c m}} \simeq \frac {9 0 0 \mathrm {M e V}}{2 \mathrm {M e V / c m}} \simeq 4. 5 \mathrm {m},
$$

where $T = \sqrt { p ^ { 2 } + m ^ { 2 } } - m \simeq 9 0 0 \mathrm { M e V }$ is the initial kinetic energy of the muons.

A better estimate is made using the range-versus-energy plots reported in the PDG Review of Particle Physics [1]. Here only a few elements are shown: in particular for 1 GeV/c muons we get $R / m \approx 2 0 0 0 \mathrm { g } \mathrm { c m } ^ { - 2 } \mathrm { G e V } ^ { - 1 }$ for H $Z / A = 1 \rangle$ ) and $R / m \approx$ $4 0 0 0 \ \mathrm { g } \ \mathrm { c m } ^ { - 2 } \ \mathrm { G e V } ^ { - 1 }$ for C $( Z / A = 0 . 5 )$ . In the mixtures, as water, one has to take into account that the primary dependence of the ionization energy loss is on the ratio $Z / A$ . Therefore $- d E / d x$ of the mixture is proportional to $\begin{array} { r } { \langle Z / A \rangle = \sum w _ { j } Z _ { j } / A _ { j } = } \end{array}$ $\sum n _ { j } Z _ { j } / \sum n _ { j } A _ { j }$ , where $w _ { j } \left( n _ { j } \right)$ is the weight fraction (number of atoms) of the $j$ -th element in the compound. In water we have $\langle Z / A \rangle = ( 2 \times 1 + 8 ) / ( 2 \times 1 + 1 6 ) \simeq$ 0.56. Therefore the range in water is dominated by the energy loss in oxygen. If we take the range in carbon as a reference we obtain $R \simeq 4 0 0 0 ~ \mathrm { c m / G e V \times 0 . 1 0 6 ~ G e V }$ $\simeq 4 . 2 \mathrm { ~ m ~ }$ . We notice that the value obtained assuming a constant energy loss rate overestimates the actual range, but is adequate for a rough estimate.

2. The condition to emit Cherenkov photons is $\beta \ge \beta _ { \mathrm { m i n } } ~ = ~ 1 / n \simeq 0 . 7 5$ . Hence we have for a particle mass m

$$
p _ {\min } = \beta_ {\min } \gamma_ {\min } m \Rightarrow p _ {\min } \simeq 1. 1 3 4 m,
$$

and then for a muon

$$
T _ {\min } = \sqrt {p _ {\min } ^ {2} + m ^ {2}} - m \simeq 0. 5 1 m \simeq 5 4 \mathrm {M e V}.
$$

The length of the path where the muon emits Cherenkov radiation is (for a constant energy loss rate)

$$
L _ {C} = \int_ {T _ {\min }} ^ {T} \frac {d E}{(- d E / d l) _ {\mathrm {i o n}}} \simeq \int_ {T _ {\min }} ^ {T} \frac {d E}{2 \mathrm {M e V} / \mathrm {c m}} \simeq \frac {9 0 0 - 5 4 \mathrm {M e V}}{2 \mathrm {M e V} / \mathrm {c m}} \simeq 4. 2 3 \mathrm {m}.
$$

Comparing this value with the one obtained under the same approximation we obtain a fraction $4 . 2 3 / 4 . 5 \simeq 9 4 \%$ .

3. The initial opening angle of the Cherenkov cone is obtained from

$$
\cos \theta_ {C} = \frac {1}{\beta n} = \frac {\sqrt {p ^ {2} + m ^ {2}}}{p n} \simeq \frac {1 . 0 0 6}{1 . 3 3} \simeq 0. 7 5 6.
$$

The muon energy loss up to the exit from the detector is small enough $( \approx 1 0 0 \mathrm { M e V } )$ ) so that the Cherenkov angle is almost constant. Hence the region illuminated on the base is determined by the Cherenkov cone at the initial point and the radius of the circle is

$$
R = D \tan \theta_ {C} = \frac {D \sqrt {1 - \cos^ {2} \theta_ {C}}}{\cos \theta_ {C}} \simeq 0. 8 6 5 D \simeq 4 3 \mathrm {c m}.
$$

# Exercise 3.3.4

Considering the distance and the size of the detector, electrons and positrons are detected for angles between

$$
\theta_ {\min } = \arctan (6 / 2 0 0) \simeq 3 0 \mathrm {m r a d}
$$

and

$$
\theta_ {\max } = \arctan (1 0 / 2 0 0) \simeq 5 0 \mathrm {m r a d}.
$$

The energy of each beam is $E _ { e } = \sqrt { s } / 2 = 4 5 \mathrm { G e V . }$

Integrating the given expression of the Bhabha cross section between $\theta _ { \mathrm { { m i n } } }$ and $\theta _ { \mathrm { m a x } }$ we have

$$
\begin{array}{l} \sigma = \frac {8 \pi \alpha^ {2}}{E _ {e} ^ {2}} (\hbar c) ^ {2} \int_ {\theta_ {\min }} ^ {\theta_ {\max }} \frac {d \theta}{\theta^ {3}} = \frac {8 \pi \alpha^ {2}}{E _ {e} ^ {2}} (\hbar c) ^ {2} \left(\frac {1}{2 \cdot \theta_ {\min } ^ {2}} - \frac {1}{2 \cdot \theta_ {\max } ^ {2}}\right) = \\ \simeq 2. 5 7 \cdot 1 0 ^ {- 8} \mathrm {f m} ^ {2} \left(\frac {1}{2 \cdot (0 . 0 3 0) ^ {2}} - \frac {1}{2 \cdot (0 . 0 5 0) ^ {2}}\right) \simeq 0. 9 1 \cdot 1 0 ^ {- 5} \mathrm {f m} ^ {2} \simeq 9. 1 \cdot 1 0 ^ {- 3 2} \mathrm {c m} ^ {2} \\ \end{array}
$$

For a rate of 1 ev/s we obtain a luminosity

$$
L = \frac {n}{\sigma} \simeq \frac {1 \mathrm {s} ^ {- 1}}{9 . 1 \cdot 1 0 ^ {- 3 2} \mathrm {c m} ^ {2}} \simeq 1. 1 \cdot 1 0 ^ {3 1} \mathrm {c m} ^ {- 2} \mathrm {s} ^ {- 1}
$$

# Exercise 3.3.5

If $\tau$ is the mean lifetime, the number of particles surviving after a time $t$ is

$$
N (t) = N _ {0} e ^ {- t / \tau}.
$$

In our case we require to have at least one decay in $t = 1$ yr

$$
N _ {0} - 1 = N _ {0} e ^ {- t / \tau} \simeq N _ {0} \left(1 - \frac {t}{\tau}\right)
$$

hence $\begin{array} { r } { N _ { 0 } = \frac { \tau } { t } } \end{array}$ . Since the number of nucleons in the detector mass $M$ is $N _ { 0 } = N _ { A } M$ (where $N _ { A } \stackrel { \cdot } { \simeq } 6 . 0 2 \cdot 1 0 ^ { 2 3 } \mathrm { m o l e } ^ { - 1 }$ is the Avogadro number) we obtain for the required mass

$$
M = \frac {\tau}{t N _ {A}} \simeq \frac {1 0 ^ {3 2}}{6 . 0 2 \cdot 1 0 ^ {2 3} \mathrm {g} ^ {- 1}} \simeq 1. 7 \cdot 1 0 ^ {8} \mathrm {g} = 1 7 0 \mathrm {t o n}
$$

# Exercise 3.3.6

The pion momentum in GeV/c is given by the relationship

$$
p = 0. 3 B R,
$$

where $R$ is the curvature radius in metres and $B$ the magnetic field in Tesla. The deflection angle in the magnetic field can be written to a good approximation as

$$
\theta \simeq \frac {L}{R} = \frac {0 . 3 B L}{p}.
$$

We notice that the approximation of using $L$ equal to the length of the magnet (instead of the length of the trajectory) is justified by the fact that the deflection angles are small for all the momenta (130 mrad at $0 . 5 \mathrm { G e V / c }$ down to 44 at $1 . 5 \mathrm { G e V } / \mathrm { c } $ ).

The distance $L$ and the width $w$ of the slit allow to select the pion momentum and its uncertainty. The angle subtended for a momentum $p _ { 0 } \pm \Delta p$ is

$$
\Delta \theta \simeq \frac {w}{d} = \frac {0 . 3 B L}{p _ {0} ^ {2}} \Delta p.
$$

Hence to select $1 \mathrm { G e V } / \mathrm { c } \pm 5 \%$ charged pions we need a distance

$$
d = \frac {p _ {0} w}{0 . 3 B L \left(\frac {\Delta p}{p _ {0}}\right)} \simeq \frac {1 \times 0 . 0 1}{0 . 3 \times 0 . 2 \times 1 . 1 \times 0 . 1} \simeq 1. 5 \mathrm {m}
$$

# Exercise 3.3.7

The relationship for a particle of charge e among the curvature radius $R$ in metres, the uniform magnetic field $B$ in Tesla and the momentum $p$ in $\mathrm { G e V } / \mathrm { c }$ is

$$
p = 0. 3 \text {B R}
$$

hence the muon momentum is $p \simeq 2 . 1 \mathrm { G e V } / \mathrm { c }$ .

For the revolution period we have

$$
T = \frac {2 \pi R}{\beta c},
$$

where the velocity is $\beta = p / E = p / \sqrt { p ^ { 2 } + m _ { \mu } ^ { 2 } } \approx 1 .$ . The revolution period is then $T \simeq 2 . 9 3 \times 1 0 ^ { - 7 } \mathrm { { s } }$ s.

The mean muon lifetime in the Lab system is

$$
\tau_ {\mathrm {L S}} = \gamma \tau \simeq \frac {p}{m _ {\mu}} \tau \simeq 2 0 \tau .
$$

The number of muons surviving after one period is

$$
N (T) = N _ {0} e ^ {- T / \tau_ {\mathrm {L S}}},
$$

where $N _ { 0 }$ is the initial muon number. The fraction of muons decayed after one period is then

$$
f = \frac {N _ {0} (1 - e ^ {- T / \tau_ {\mathrm {L S}}})}{N _ {0}} \simeq 1 - \left(1 - \frac {T}{\tau_ {\mathrm {L S}}}\right) = \frac {T}{\tau_ {\mathrm {L S}}} \simeq 6. 7 \times 1 0 ^ {- 3}.
$$

# Exercise 3.3.8

1. The total energy of the particles involved in the proton decay is ${ \cal E } _ { 0 } = m _ { p }$ . In the considered decay channel the energies of the two particles are almost equal so that $\epsilon _ { e } \approx \epsilon _ { \pi ^ { 0 } } \approx E _ { 0 } / 2$ (the correct calculation gives $0 . 4 6 \ \mathrm { G e V }$ and $0 . 4 8 {  { \mathrm { ~ G e V } } }$ for the energies of the positron and pion respectively). Positrons and photons (from $\pi ^ { 0 }$ decay) are produced back-to-back and, having energies above the water critical energy and then produce e.m. cascades. Under the approximation of equal energies, the maximum of the longitudinal development is (in units of $X _ { 0 }$ )

$$
T _ {\max } = \frac {\ln \left[ E _ {0} / \left(2 E _ {\mathrm {c}}\right) \right]}{\ln 2} \simeq 2. 5 5.
$$

Hence most of the Cherenkov emitting particles are contained in a segment of length $\begin{array} { r } { L = 2 \times \frac { X _ { 0 } } { \rho } \times T _ { \mathrm { m a x } } \simeq 1 . 8 ~ \mathrm { m } } \end{array}$ . This length determines the size of the detector (each side $\gg L$ ) .

2. To estimate the number of emitted Cherenkov photons, we need to evaluate the total track length for the charged particles $( e ^ { + } , e ^ { - } )$ contained each cascade. This total length (called track length integral) is given by

$$
T _ {\mathrm {t o t}} = \frac {2}{3} \int_ {0} ^ {T _ {\max }} 2 ^ {t} d t = \frac {2}{3 \ln 2} \left(2 ^ {T _ {\max }} - 1\right) = \frac {2}{3 \ln 2} \left(\frac {E _ {0}}{2 E _ {\mathrm {c}}} - 1\right) \simeq 4. 7,
$$

where the factor 2/3 is the average fraction of charged particles in the cascade. Hence we have for the total number of Cherenkov photons

$$
N _ {\text {p h o t}} = 2 \frac {X _ {0} \cdot T _ {\text {t o t}}}{\rho} \times I _ {0} \simeq 3 3 8 \mathrm {c m} \times 4 0 0 \mathrm {c m} ^ {- 1} \simeq 1. 4 \times 1 0 ^ {5}
$$

# Exercise 3.3.9

When a proton interacts with a residual air molecule it is thrown away from the trajectory where the accumulated protons are kept by the magnetic field. Then at each scattering a proton is lost. The absorption coefficient is given by

$$
\mu = \sigma n \qquad n = \rho \frac {N _ {A}}{A},
$$

where $\sigma$ is the total cross section, $n$ is the number of scatterers per unit volume and $N _ { A }$ is the Avogadro number. In the proton ring $1 0 ^ { - 1 1 }$ atm) we have

$$
\mu = 3 0 0 \times 1 0 ^ {- 2 7} \times 1. 2 5 1 0 ^ {- 1 4} \times \frac {6 1 0 ^ {2 3}}{1 4} \simeq 1. 6 \times 1 0 ^ {- 1 6} \mathrm {c m} ^ {- 1}.
$$

The inverse of this value corresponds is the mean pathlength. $3 0 0 \mathrm { G e V }$ protons are ultra-relativistic and their velocity is ${ \approx } c$ . Hence the mean beam lifetime is

$$
\tau = \frac {1}{c \mu} \simeq 2. 0 8 \times 1 0 ^ {5} \mathrm {s} \simeq 5 8 \mathrm {h}
$$

# Exercise 3.3.10

The interactions occurs against the nuclei along the beam. These are

$$
N _ {\mathrm {s c}} = \frac {N _ {A}}{A} \rho d S = \frac {6 . 0 2 \times 1 0 ^ {2 3}}{2 0 7} \times 1 1. 3 \times 0. 2 \times \pi \times 1 \simeq 2 \times 1 0 ^ {2 2}
$$

The fraction of scattered particle is given by

$$
f _ {s} = \frac {N _ {s}}{S} \sigma = \frac {2 \times 1 0 ^ {2 2}}{3 . 1 4} \times 3 1 0 ^ {- 2 6} \simeq 1. 9 1 0 ^ {- 4}
$$

# Exercise 3.3.11

The neutrino interaction rate is given by

$$
w _ {\text {i n t}} = \sigma \phi \simeq 7 \times 1 0 ^ {- 4 4} \mathrm {c m} ^ {2} \times 1 0 ^ {6} \mathrm {c m} ^ {- 2} \mathrm {s} ^ {- 1} \simeq 7 \times 1 0 ^ {- 3 8} \mathrm {s} ^ {- 1}.
$$

The number of scattering centres (electrons) per unit volume is

$$
n _ {\mathrm {s c}} = \rho \frac {Z}{A} N _ {A} V = \frac {Z}{A} N _ {A} M = 0. 5 \times 6. 0 2 \cdot 1 0 ^ {2 3} \times 5 \cdot 1 0 ^ {1 0} \simeq 1. 5 \times 1 0 ^ {3 4}.
$$

Hence the number of interactions per year is $( \Delta T = 1 \ \mathrm { y r } \simeq 3 . 1 5 \times 1 0 ^ { 7 } \ \mathrm { s }$ )

$$
N _ {\mathrm {y r}} = w _ {\mathrm {i n t}} \times n _ {\mathrm {s c}} \times \Delta T = 3. 3 \times 1 0 ^ {4}
$$

# Exercise 3.3.12

(a) The maximum shower development is reached at a depth

$$
T = \frac {\log_ {1 0} \left(E _ {0} / E _ {c}\right)}{\log_ {1 0} 2} = \frac {\log_ {1 0} (5 0 0 \mathrm {G e V} / 8 0 \mathrm {M e V})}{\log_ {1 0} 2} \simeq 1 2. 6
$$

where T is expressed in radiation length units. Therefore the actual depth in $\mathrm { g } / \mathrm { c m } ^ { 2 }$ is

$$
X _ {\max } = T \times X _ {0} \simeq 4 7 0 \mathrm {g} / \mathrm {c m} ^ {2}
$$

corresponding to an optimal altitude (for vertical showers)

$$
h = - h _ {0} \ln \left(\frac {X _ {\mathrm {m a x}}}{X _ {\mathrm {v}} (0)}\right) \simeq 5 3 0 0 \mathrm {m}.
$$

There are sites suitable for such observations, e.g. in the Andes or in Tibet.

(b) Electrons at the shower maximum have an energy equal to the critical energy $E _ { c } ^ { \mathrm { w a t e r } } \simeq E _ { c } ^ { \mathrm { a t m } } = 8 0 \ : \mathrm { M e V } .$ At this energy the Cherenkov condition is fulfilled

$$
n \beta = \frac {n}{\sqrt {1 + (m / p) ^ {2}}} = \frac {1 . 3 3}{\sqrt {1 + (0 . 5 1 1 / 8 0) ^ {2}}} > 1.
$$

Hence Cherenkov photons can be used to detect shower events.

(c) Shower particles (photons and electrons) at the critical energy have equal probability to loose energy by ionization and bremsstrahlung. Therefore they are not energetic enough to produce e.m. cascades. The component of the shower which are already electrons mostly loose energy by ionization. Instead those which are photons have still enough energy for pair production (threshold energy $\simeq 1 ~ \mathrm { M e V } ,$ ) and can generate electrons of both signs with lower energies. To make an estimate of the path done by electron loosing energy in water we can calculate the residual range of electrons at the critical energy

$$
\Delta x = \int_ {0} ^ {E _ {c} ^ {\text {w a t e r}}} \frac {d E}{\left(\frac {- d E}{d x}\right) _ {\text {i o n}}} \simeq \frac {E _ {c} ^ {\text {w a t e r}}}{2 \mathrm {M e V} / (\mathrm {g c m} ^ {- 2})} = 4 0 \mathrm {g} / \mathrm {c m} ^ {2}
$$

and then $\Delta l \simeq 4 0 ~ \mathrm { c m }$ . Hence electrons loose their whole energies in the water tanks, apart those which exit the tank and loose only a part of their energy.

# Exercise 3.3.13

1. The reaction threshold for the proton kinetic energy is

$$
T _ {\mathrm {t h}} = \frac {(2 m _ {p} + m _ {J}) ^ {2} - (2 m _ {p}) ^ {2}}{2 m _ {p}} = 2 m _ {J} + \frac {m _ {J} ^ {2}}{2 m _ {p}} \simeq 1 1. 3 \mathrm {G e V}
$$

2. Denoting with $M$ the total CMS energy for protons of $2 8 \ \mathrm { G e V }$ energy against target protons (at rest), we have

$$
M \simeq \sqrt {2 m _ {p} E _ {p}} \simeq 7. 3 \mathrm {G e V}.
$$

The final state in the reaction (3.2) is a three body system. Then the maximum and minimum energy of the $\boldsymbol { \mathrm { J } } / \psi$ particle in the CMS are given by

$$
\min : E _ {J} ^ {*} = m _ {J} \simeq 3. 1 \mathrm {G e V}
$$

$$
\max : E _ {J} ^ {*} = \frac {M ^ {2} + m _ {J} ^ {2} - (2 m _ {p}) ^ {2}}{2 M} \simeq 4. 0 7 \mathrm {G e V}.
$$

To obtain the maximum and minimum values in the Lab system we make a Lorentz transformation with the following $\beta$ and $\gamma$ values

$$
\beta = \frac {p _ {p}}{E _ {p} + m _ {p}} \simeq 0. 9 6 7, \quad \gamma = \frac {E _ {p} + m _ {p}}{M} \simeq 3. 9 6
$$

To calculate the minimum and maximum $\boldsymbol { \mathrm { J } } / \psi$ energies in the Lab frame we consider the following cases

min:

max/min:

max/max:

It follows that the minimum and maximum energies are 6 and $2 6 . 2 \mathrm { G e V }$ respectively.

3. The minimum opening angle $\theta _ { \mathrm { { m i n } } }$ of the $e ^ { + } e ^ { - }$ pair is obtained from

$$
\sin \left(\frac {\theta_ {\mathrm {m i n}}}{2}\right) = \frac {\sqrt {m _ {J} ^ {2} - 2 m _ {e} ^ {2}}}{E _ {J}} \simeq \frac {m _ {J}}{E _ {J}}
$$

Therefore the minimum angle is obtained for the maximum $\boldsymbol { \mathrm { J } } / \psi$ energy, 26.2 GeV, and turns out to be $\theta _ { \mathrm { m i n } } ~ \simeq ~ 1 3 . 6 ^ { \circ }$ .

4. Electrons are ultra-relativistic $( p \simeq E )$ ): hence the $\mathrm { e ^ { + } e ^ { - } }$ invariant mass is

$$
M _ {e e} ^ {2} \simeq 4 p ^ {+} p ^ {-} \sin^ {2} \frac {\Delta \theta}{2}
$$

where $p ^ { + } ( p ^ { - } )$ is the $e ^ { + } ( e ^ { - } )$ momentum and $\Delta \theta$ is the opening angle of the observed pair. Using for $M _ { e e }$ the $\boldsymbol { \mathrm { J } } / \psi$ mass we obtain

$$
p ^ {+} = \frac {m _ {J} ^ {2}}{4 p ^ {-} \sin^ {2} \frac {\Delta \theta}{2}} \simeq 1 2. 4 \mathrm {G e V / c}.
$$

# Exercise 3.3.14

(a) The collider system is the CMS, hence $E _ { \tau } = E _ { 0 } / 2 = 1 4 . 5 \mathrm { G e V }$ .

(b) Using the Sargent rue we have for the transition rates $( \Gamma = 1 / \tau$ )

$$
\frac {\Gamma (\tau^ {+} \to e ^ {+} + v _ {e} + \bar {\nu} _ {\tau})}{\Gamma (\mu^ {+} \to e ^ {+} + v _ {e} + \bar {\nu} _ {\mu})} = \frac {m _ {\tau} ^ {5}}{m _ {\mu} ^ {5}}.
$$

Taking into account the tau branching ratio into neutrinos we have

$$
\Gamma (\tau^ {+} \to e ^ {+} + \nu_ {e} + \bar {\nu} _ {\tau}) = \frac {B R (\tau^ {+} \to e ^ {+} + \nu_ {e} + \bar {\nu} _ {\tau})}{\tau_ {\tau}}
$$

Hence the tau mean lifetime is

$$
\tau_ {\tau} = \frac {B R (\tau^ {+} \rightarrow e ^ {+} + \nu_ {e} + \bar {\nu} _ {\tau})}{\Gamma (\tau^ {+} \rightarrow e ^ {+} + \nu_ {e} + \bar {\nu} _ {\tau})} = \tau_ {\mu} \times B R (\tau^ {+} \rightarrow e ^ {+} + \nu_ {e} + \bar {\nu} _ {\tau}) \times \left(\frac {m _ {\mu}}{m _ {\tau}}\right) ^ {5} \simeq 1.
$$

$$
\simeq 2. 2 1 0 ^ {- 6} \times 0. 1 8 \times \left(\frac {1 0 6}{1 7 7 7}\right) ^ {5} \simeq 3. 0 \times 1 0 ^ {- 1 3} \mathrm {s}.
$$

(c) The $\tau$ mean pathlength is

$$
\langle L \rangle = \beta \gamma c \tau_ {\tau} = \frac {p _ {\tau}}{m _ {\tau}} c \tau_ {\tau} = \frac {\sqrt {E _ {\tau} ^ {2} - m _ {\tau} ^ {2}}}{m _ {\tau}} c \tau_ {\tau} \simeq 8. 1 \times 3 1 0 ^ {1 0} \times 3 1 0 ^ {- 1 3} \simeq 0. 0 7 3 \mathrm {c m}.
$$

For a cylindrical detector the minimum distance to observe a decay is given by the internal radius $r$ (the distance increases with the angle). Hence the maximum detection probability is

$$
f _ {\max } (l > r) = \frac {1}{\langle L \rangle} \int_ {r} ^ {\infty} e ^ {- \frac {l}{\langle L \rangle}} d l = e ^ {- \frac {r}{\langle L \rangle}} \simeq 2 1 0 ^ {- 3 0}
$$

and is then negligible.

# Exercise 3.3.15

Photon and electron beams of $5 \ \mathrm { G e V }$ produce electromagnetic showers. For their developments the relevant parameter is the number of radiation lengths. Each scintillator layer has $1 / 4 2 \simeq 0 . 0 2$ radiation lengths, whereas the lead slabs have about 2 radiation lengths each. Therefore the scintillator layers have a negligible contribution. Upstream of the fourth scintillator there are 3 lead slabs, hence the total number of radiation lengths is

$$
T = \frac {3 \times 1 \mathrm {c m}}{0 . 5 6 \mathrm {c m}} \simeq 5. 4.
$$

Using the Heitler toy model the number of shower particles $e ^ { + }$ , e− and γ ) is $2 ^ { T }$ . The scintillator detects charged particles via the ionization process whereas photons have a very low probability to convert to electrons because of the low $Z$ of the material. In an e.m. showers charged particle are approximately 2/3 of the total content of particles, they have an energy loss rate corresponding to minimum ionizing particles $( \simeq 2 \ : \mathrm { M e V } \ : \mathrm { g } ^ { - 1 } \ : \mathrm { c m } ^ { 2 } )$ and then their total energy release is

$$
\Delta E = \frac {2}{3} \times 2 ^ {T} \times \left(- \frac {d E}{d x}\right) _ {\text {i o n}} \times \rho d \simeq 0. 6 7 \times 4 2. 2 \times 2 \times 1. 0 3 \simeq 5 8 \mathrm {M e V},
$$

where $d$ is the scintillator thickness. This energy release is the same for incident electron and photons.

Instead muons loose energy only by ionization. The energy lost before the fourth scintillator is $2 \mathrm { M e V } \mathrm { g } ^ { - 1 } \mathrm { c m } ^ { 2 } \times 3 \mathrm { c m } \times 1 1 \mathrm { g } / \mathrm { c m } ^ { 3 } \simeq 6 6 \mathrm { M e V } ,$ hence their energy is almost unaffected. We can assume for them the same energy loss rate of $\simeq 2 ~ \mathrm { M e V }$ $\mathbf { g } ^ { - 1 } \mathbf { c m } ^ { 2 }$ and then the energy release in the fourth scintillator is

$$
\Delta E = 2 \times 1. 0 3 \simeq 2 \mathrm {M e V}.
$$

Finally to discriminate electrons from photons we can use the signal in the first scintillator which can be detected only for electrons but is absent for photons.

# Exercise 3.3.16

(a) The $p$ -Cu interaction length is

$$
\lambda_ {\mathrm {i n t}} ^ {p \mathrm {C u}} = \frac {A}{N _ {A} \rho \sigma_ {p \mathrm {C u}}} = \frac {A ^ {\frac {1}{3}}}{N _ {A} \rho \sigma_ {p p}} = \frac {6 3 . 5 ^ {\frac {1}{3}}}{6 1 0 ^ {2 3} 8 . 9 6 4 0 1 0 ^ {- 2 7}} \simeq 1 8. 5 \mathrm {c m}
$$

(b) The initial state has baryon number $B = + 2$ , the two $D$ -particles are mesons and have $B = 0$ . Hence $X$ must have $B = + 2$ . The simplest case is

$$
p + p \rightarrow D ^ {+} + D ^ {-} + p + p
$$

The flavor flux diagram is shown in Fig. 3.2 (left).

(c) The quark flavor content of $D ^ { + }$ and $D ^ { - }$ is $D ^ { + } = c \bar { d }$ and $D ^ { - } = \bar { c } d$ respectively. $D ^ { + }$ decays into neutrinos via $c  W ^ { + } + s$ followed by $W ^ { + }  l ^ { + } + \nu _ { l }$ . Hence $D ^ { + }$ is associated to neutrinos. Similarly $D ^ { - }$ decays into $W ^ { - }$ and then anti-neutrinos are produced. Examples of Feynman diagrams with $\bar { \nu } _ { e }$ and $\nu _ { \mu }$ final states are shown in Fig. 3.2 (right).

(d) The interaction length of $D$ -particles is

$$
\lambda_ {D C u} = \frac {\sigma_ {p p}}{\sigma_ {D p}} \times \lambda_ {p C u} = \frac {4 0}{3 0} \times 1 8. 5 \mathrm {c m} \simeq 2 5 \mathrm {c m}
$$

The decay length is instead

$$
\lambda_ {\mathrm {d e c}} = \beta \gamma c \tau (D ^ {\pm}) = \frac {p}{m _ {D ^ {\pm}}} \times c \tau (D ^ {\pm})
$$

Therefore $\lambda _ { \mathrm { d e c } } \ll \lambda _ { D \mathrm { C u } }$ is obtained for

$$
p \ll m _ {D ^ {\pm}} \times \frac {\lambda_ {D C u}}{c \tau (D ^ {\pm})} \simeq 1. 8 7 \times \frac {2 5}{3 1 0 ^ {1 0} \times 1 . 0 4 1 0 ^ {- 1 2}} \mathrm {G e V / c} \simeq 1 5 0 0 \mathrm {G e V / c}
$$

which is always fulfilled for $4 0 0 \mathrm { G e V }$ incident protons.

(e) Taking into account the considerations at point (c) and the fact that $B R ( D ^ { \pm } \to$ $\nu _ { \mu } / \bar { \nu } _ { \mu } ) = B R ( D ^ { \pm } \to \nu _ { e } / \bar { \nu } _ { e } )$ we expect for the muon to electron neutrino ratio

$$
\frac {\nu_ {\mu} + \bar {\nu} _ {\mu}}{\nu_ {e} + \bar {\nu} _ {e}} = 1.
$$

# Exercise 3.3.17

The absorption coefficient for pair production, which is the dominant process at high energies, is given by

![](images/8e1ceecb5a1a74d8de3c1a9457a9d14510121a37a2843577443ec04843ea2da0.jpg)  
Fig. 3.2 Flavor flux diagram for $p + p  D ^ { + } + D ^ { - } + p + p$ (left). Feynman diagrams for two $D$ decays (right)

$$
\mu = \left(\frac {7}{9}\right) X _ {0} ^ {- 1} \simeq 1. 3 8 \mathrm {c m} ^ {- 1}
$$

A photon hitting the lead plate has a probability $\exp ( - \mu d )$ to escape from the lead plate. Instead in case of pair production electrons emerge from the plate or induce e.m. showers, depending on the first interaction point. If conversion occurs one or more electrons will reach the downstream detector. The conversion probability is then

$$
P _ {c} = 1 - \exp (- \mu d)
$$

Hence the $\pi ^ { 0 }$ detection efficiency is

$$
\epsilon = P _ {c} ^ {2} = [ 1 - \exp (- \mu d) ] ^ {2} = [ 1 - \exp (- 1.38) ] ^ {2} \simeq 56 \%
$$

# Exercise 3.3.18

(a) The process that makes electron antineutrino detectable is the same used in the celebrated experiment by Reines and Cowan [2]

$$
\bar {\nu} _ {e} + p \rightarrow n + e ^ {+}
$$

The process, called also ‘inverse beta decay’, is a charged current weak interaction (i.e. with W virtual boson). The detected particles are the positron through its annihilation in two photons of $0 . 5 \ \mathrm { M e V }$ and the delayed photons emitted by the capture of the neutron. The process has the cross section given in the text. Instead muon antineutrinos, originating from the oscillation phenomenon, are difficult to detect. In fact the charged current process $\bar { \nu } _ { \mu } + p \to n + \mu ^ { + }$ is forbidden by kinematics $E _ { \mathrm { t h r } } \simeq 1 0 0  { \mathrm { M e V } } )$ and the neutral current process (i.e. with $Z ^ { 0 }$ virtual boson) $\bar { \nu } _ { \mu } + p / n \to \bar { \nu } _ { \mu } + p / n$ can be only detected from the nucleon recoil with very low

efficiency. Hence the oscillation phenomenon can be observed counting the number of disappeared electron antineutrinos.

(b) If neutrinos do not oscillate the interaction rate is

$$
r = \frac {I _ {v}}{4 \pi L ^ {2}} \times \sigma_ {v} \times N _ {n} \times \rho l S
$$

where $N _ { n }$ is the number of target nucleons per gram, $\rho$ is the medium density, $l$ and S are the detector length and section respectively. The product $\rho l S$ is the detector mass and we have

$$
\begin{array}{l} r = \frac {I _ {v}}{4 \pi L ^ {2}} \times \sigma_ {v} \times N _ {A} \times M \simeq \\ \simeq \frac {1 0 ^ {1 8} \mathrm {s} ^ {- 1}}{1 2 . 5 6 2 0 0 0 0 ^ {2} \mathrm {c m} ^ {2}} \times 2 1 0 ^ {- 4 3} \mathrm {c m} ^ {2} \times \frac {6 1 0 ^ {2 3}}{\mathrm {g}} \times 1 0 ^ {6} \mathrm {g} \simeq 2. 4 1 0 ^ {- 5} \mathrm {s} ^ {- 1} \\ \end{array}
$$

Denoting with $\epsilon$ the detection efficiency, the number of expected interactions per year is

$$
N = r \times \epsilon \times T \simeq 2. 4 1 0 ^ {- 5} \times 0. 7 0 \times 3. 1 5 1 0 ^ {7} \simeq 5 2 9.
$$

(c) For a detector at $2 0 0 \mathrm { m }$ from the reactor core and 2 MeV electron antineutrinos the probability to become muon antineutrinos is

$$
P \left(\bar {v} _ {e} \rightarrow \bar {v} _ {\mu}\right) \simeq 0. 2 0 \sin^ {2} \left(1 0 ^ {- 3} \frac {L [ m ]}{E [ M e V ]}\right) \simeq 0. 2 0 \times \sin^ {2} \left(1 0 ^ {- 3} \frac {2 0 0}{2}\right) \simeq 0. 0 0 2
$$

Hence the number of detectable electron antineutrinos is

$$
N _ {e} \simeq N \times [ 1 - P (\bar {\nu} _ {e} \rightarrow \bar {\nu} _ {\mu}) ] \simeq 5 2 8
$$

and the mean number of disappeared $\bar { \nu } _ { e }$ is 1.1.

(d) The probability to have a null result is given by the poissonian probability to observe no event out of an expectation of 1.1

$$
P (0 \mid 2) = e ^ {- 1.1} \frac {1.1 ^ {0}}{0 !} = e ^ {- 1.1} \simeq 33 \%
$$

It is worth to notice that this probability is not realistic, because it is based on the assumption that the knowledge of the number of neutrino interactions is perfectly known. In real experiments the uncertainty on the neutrino flux and detection efficiency makes it impossible to observe a disappearance ratio (1/529) so small.

# Exercise 3.3.19

(a) To get the mass of the particle we consider the region 2, after the slowing down, where two measurements are available.

From the time-of-flight we have $\begin{array} { r } { \beta _ { 2 } = \frac { \nu _ { 2 } } { c } \simeq \frac { 2 . 8 \times 1 0 ^ { 8 } } { 3 \times 1 0 ^ { 8 } } \simeq 0 . 9 3 } \end{array}$ - 0.93 and β2γ2 = $\begin{array} { r } { \beta _ { 2 } \gamma _ { 2 } = \frac { \beta _ { 2 } } { \sqrt { 1 - \beta _ { 2 } ^ { 2 } } } \simeq } \end{array}$ 2.60.

From the curvature we have $p _ { 2 } = 0 . 3 ~ B R _ { 2 } = 0 . 3 \times 1 \times 1 . 2 1 \simeq 0 . 3 6 3 ~ \mathrm { G e V / c } .$ .

The rest mass of the particle is

$$
m = \frac {p _ {2}}{\beta_ {2} \gamma_ {2}} \simeq \frac {0 . 3 6 3}{2 . 6 0} \simeq 0. 1 4 0 \mathrm {G e V / c ^ {2}}.
$$

It is a charged pion whose momentum before the slowing down is

$$
p _ {1} = 0. 3 B \frac {l _ {1} ^ {2}}{8 s _ {1}} \simeq 0. 3 \times 1 \times \frac {0 . 8 0 ^ {2}}{8 \times 0 . 0 3} \simeq 0. 8 0 \mathrm {G e V / c},
$$

and the kinetic energy is

$$
T _ {1} = \sqrt {p _ {1} ^ {2} + m ^ {2}} - m \simeq 0. 6 7 0 \mathrm {G e V}.
$$

(b) The energy lost in the medium is

$$
\Delta E = T _ {1} - T _ {2} = T _ {1} - \left(\sqrt {p _ {2} ^ {2} + m ^ {2}} - m\right) \simeq 0. 6 7 0 - 0. 2 5 0 \simeq 0. 4 2 0 \mathrm {G e V}.
$$

(c) The mean half-time is $T _ { 1 / 2 } = L _ { 1 / 2 } / ( c \beta _ { 2 } \gamma _ { 2 } )$ . Then the mean lifetime is

$$
\tau = \frac {L _ {1 / 2}}{c \beta_ {2} \gamma_ {2} \ln 2} \simeq \frac {1 4}{3 \times 1 0 ^ {8} \times 2 . 6 \times 0 . 6 9} \simeq 2. 6 \times 1 0 ^ {- 8} \mathrm {s}.
$$

# Exercise 3.3.20

(a) Neglecting energy losses, the momentum of the electron (positron) is

$$
\begin{array}{l} \frac {p}{\mathrm {G e V} / \mathrm {c}} = 0. 3 \frac {B}{\text {T e s l a}} \frac {R}{\mathrm {m}} \tag {3.10} \\ \simeq 0. 3 \times 0. 8 \times 0. 4 0 \simeq 0. 0 9 6. \\ \end{array}
$$

The photon energy is the sum of the two momenta $\begin{array} { r } { E _ { \gamma } = 2 p \simeq 1 9 2  { \mathrm { M e V } } . } \end{array}$ In this calculation the opening angle of the pair has not been considered: in fact it is negligible, $\theta \approx m _ { e } / E _ { \gamma } \simeq 2 . 7 \times 1 0 ^ { - 3 }$ .

(b) To make a rough estimate of the energy loss along the electron (positron) track, we assume that the track length is the same as in the previous case (though the track actually changes). This energy loss is due to ionization, because the bremsstrahlung is negligible for $E < E _ { \mathrm { c r i t } }$ $( { \approx } 3 0 0 \mathrm { M e V }$ in $\mathrm { L H } _ { 2 }$ )

![](images/9feb0d5b4932426aef99f8035e7503f2ca0d7675bd136c8cfe55329cd87e5adf.jpg)  
Fig. 3.3 Solid line: no energy losses; dashed line: with energy losses

$$
\Delta E \simeq \left(- \frac {d E}{d x}\right) _ {\text {i o n}} \rho \pi R
$$

Since the electron (positron) has $p / m _ { e }$ of few hundreds, we can assume9 that $( - d E / d x ) _ { \mathrm { i o n } } \approx ( - d E / d x ) _ { \mathrm { m i n } } \simeq 4 . 1 \mathrm { M e V } \mathrm { g ^ { - 1 } c m ^ { 2 } }$ . Therefore we have

$$
\Delta E \simeq 4. 1 \times 0. 0 7 1 \times 1 2 5. 6 \simeq 3 6. 6 \mathrm {M e V}.
$$

The electron (positron) momentum at the entrance of the chamber can be estimated using the following arguments (see Fig. 3.3):

the track is not a semi-circle: its radius at entrance $R _ { 1 }$ (at exit $R _ { 2 }$ ) is larger (smaller) than the circle radius in the case of no energy losses $R$ ;   
the sum of these two radii can be approximated to $2 R$ (the measured diameter).

Since $R \propto p$ , denoting with $p _ { \mathrm { i n } }$ and $p _ { \mathrm { o u t } }$ respectively the momentum at entrance and exit of the chamber, from $2 R = R _ { 1 } + R _ { 2 }$ we obtain

$$
p = \frac {p _ {\text {i n}} + p _ {\text {o u t}}}{2} = \frac {2 p _ {\text {i n}} - \Delta p}{2}.
$$

Therefore we have:

$$
p _ {\mathrm {i n}} \simeq p + \frac {\Delta p}{2} \simeq p + \frac {\Delta E}{2} \simeq 9 6 + \frac {3 7}{2} \simeq 1 1 4. 5 \mathrm {M e V}
$$

and the photon energy is $E _ { \gamma } ^ { \mathrm { c o r r } } = 2 \ p _ { \mathrm { i n } } \simeq 2 2 9 \ \mathrm { M e V } .$

A more accurate calculation can be done as follows.

$$
d p \simeq \left(- \frac {d E}{d x}\right) _ {\text {i o n}} \rho d l \simeq \left(- \frac {d E}{d x}\right) _ {\text {i o n}} \rho R d \alpha .
$$

In this expression we have assumed that the arc element is centered as in the case of no losses: it is not actually true, but it is a sensible approximation for an estimate. Substituting here Eq. (3.10) one gets

$$
\frac {d p}{p} = \left(- \frac {d E}{d x}\right) _ {\mathrm {i o n}} \rho \frac {3}{B} d \alpha = - k d \alpha ,
$$

with $k = 4 . 1 \times 0 . 0 7 1 \times 3 / 0 . 8 \simeq 0 . 1 2 1$ . Integrating we have

$$
p (\alpha) = p _ {\text {i n}} \exp (- k \alpha).
$$

Therefore

$$
\Delta p = p _ {\text {i n}} - p _ {\text {o u t}} = p _ {\text {i n}} \left[ 1 - \exp (- k \pi) \right]
$$

$$
p _ {\mathrm {i n}} = \frac {\Delta p}{1 - \exp (- k \pi)} \simeq \frac {3 7}{1 - \exp (- 0 . 1 2 1 \pi)} \simeq 1 1 7 \mathrm {M e V}
$$

from which we get $E _ { \gamma } ^ { \mathrm { c o r r } } = 2 \ p _ { \mathrm { i n } } \simeq 2 3 4 \ \mathrm { M e V } .$

# Exercise 3.3.21

(a) The dominating process at this energy is Compton scattering by which photons transfer part of their energies to electrons. Iterating this process the whole energy of the photons is deposited and the measurement is possible through the ionization energy loss of the electrons. The characteristic length which is relevant to determine the sizes of the detector is the Compton mean free path

$$
\lambda_ {C} = \frac {A}{Z} \frac {1}{N _ {A} \sigma_ {C}},
$$

where $\sigma _ { C }$ is the Compton cross section, $N _ { A }$ is the Avogadro number and A, Z refer to the detector material. To make a rough estimate one can assume $A / Z \approx 2$ and use the Thomson cross section, $\sigma _ { T }$ , for the Compton scattering

$$
\lambda_ {C} \approx 2 \times \frac {1}{6 \times 1 0 ^ {2 3} \times 6 . 6 \times 1 0 ^ {- 2 5}} \simeq 5 \mathrm {g c m} ^ {- 2}.
$$

A more accurate calculation would give a larger $\lambda _ { C }$ (by about a factor 2), being the Thomson cross section the low energy limit of Compton scattering.

(b) In the antineutrino scattering $\bar { \nu } _ { e } + p \to e ^ { + } + n$ , the outgoing particles have momenta of the same order of the momentum of the incident neutrino. Assuming that $p _ { n } \approx E _ { \nu }$ , the neutron is non-relativistic and we get for the its kinetic energy

$$
T _ {n} \approx \frac {E _ {\nu} ^ {2}}{2 m _ {n}} \simeq 2 \mathrm {k e V}
$$

which means that the recoil energy is negligible with respect to the other energies.10 (c) Denoting by $E _ { + }$ the positron energy, from energy conservation in the process $\bar { \nu } _ { e } + p \to e ^ { + } + n$ , neglecting the neutron recoil energy, we get

$$
E _ {v} = E _ {+} + m _ {n} - m _ {p}.
$$

Energy conservation applied to the positron annihilation gives

$$
E _ {\text {v i s}} = E _ {+} + m _ {e}. \tag {3.11}
$$

Then the asked relationship is

$$
E _ {v} = E _ {\text {v i s}} + m _ {n} - m _ {p} - m _ {e} \simeq E _ {\text {v i s}} + 0. 7 8 \mathrm {M e V}
$$

(d) Since $E _ { \mathrm { v i s } } \geq 2 m _ { e }$ because of Eq. (3.11), the detected neutrinos must have

$$
E _ {v} \geq 2 m _ {e} + 0. 7 8 \mathrm {M e V} \simeq 1. 7 8 \mathrm {M e V}.
$$

This corresponds to the energy threshold of the process.

# References

1. Tanabashi, M., et al.: (Particle data group). Phys. Rev. D 98, 030001 (2018). http://pdg.lbl.gov/   
2. Reines, F., Cowan, Jr., C.L.: Free anti neutrino absorption cross section. I. Measurement of the free anti neutrino absorption cross section by protons. Phys. Rev. 113, 273 (1959)