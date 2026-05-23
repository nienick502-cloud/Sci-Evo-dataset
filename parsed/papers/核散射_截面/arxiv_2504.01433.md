# Reaction and interaction nucleus-nucleus cross sections in the complete Glauber theory

Yu.M. Shabelski and A.G. Shuvaev

NRC ”Kurchatov Institute” - PNPI, Gatchina 188300 Russia

E-mail: shabelsk@thd.pnpi.spb.ru

E-mail: shuvaev@thd.pnpi.spb.ru

# Abstract

The straightforward calculations of the reaction and interaction cross sections of the nuclear scattering are carried out in Glauber approach using the generating function method. It allows for the resummation of all orders of Glauber theory. The results are obtained for $^ 4$ He, $_ { 1 1 }$ Li, $\mathrm { ^ { 1 2 } C }$ scattering on $\mathrm { ^ { 1 2 } C }$ target. The difference between the reaction and the differential cross section is shown to be not exceeding several percents

# 1 Introduction

The information on the various aspects of the nuclear structure, in particular, about halo nuclei, comes mainly from the experimental data on the collision of the nucleus under study $A$ with a target $B$ . What is directly measured in this reaction is the interaction cross section. The interaction cross section is defined as that of the process when the beam nucleus $A$ scatters without being excited or disintegrated whereas it is allowed for the target nucleus $B$ ,

$$
\sigma_ {A B} ^ {I} = \sigma_ {A B} ^ {t o t} - \sigma_ {A B} ^ {e l} - \sigma_ {A B \rightarrow A B ^ {*}} = \sigma_ {A B} ^ {t o t} - \sigma_ {A B \rightarrow A B ^ {\prime}}.
$$

Here $B ^ { * }$ stands for all the excited or disintegrated states of the target nucleus, $B ^ { \prime } =$ $\{ B , B ^ { * } \}$ denotes the complete set of the target states. Introducing the reaction, or the total inelastic, cross section

$$
\sigma_ {A B} ^ {R} = \sigma_ {A B} ^ {t o t} - \sigma_ {A B} ^ {e l},
$$

it can be rewritten as

$$
\sigma_ {A B} ^ {I} = \sigma_ {A B} ^ {R} - \sigma_ {A B \rightarrow A B ^ {*}}
$$

The reason why it is the interaction cross section that is really measured is in the experimental difficulty to distinguish the pure elastic scattering from the processes giving rise to the target excitation or disintegration. The beam energy loss in the latter case is very small compared to the initial value to detect.

Usually the difference between $\sigma _ { A B } ^ { R }$ and $\sigma _ { A B } ^ { I }$ is assumed to be negligible. The Monte-Carlo simulation results into the value 2-3% of $\sigma _ { A B } ^ { R }$ RAB In this paper we present .1 a complete analytical Glauber calculation of the reaction and the interaction cross sections for several relatively light nuclei, $^ 4$ He, $_ { 1 1 }$ Li, $_ { 1 2 }$ C.

# 2 Complete Glauber calculation of the interaction cross section

The amplitude of the elastic scattering of the incident nucleus $A$ on the fixed target nucleus $B$ reads in the Glauber theory

$$
f _ {A B} (q) = \frac {i p}{2 \pi} \int d ^ {2} b e ^ {i q b} [ 1 - s _ {A B} (b) ]. \tag {1}
$$

Here $p$ is a relative momentum in the central of mass frame, $q$ is the transferred momentum. The impact parameter $b$ is a two dimensional vector in the transverse plane with respect to relative momentum of the colliding nuclei $A$ , $B$ . The evaluation of the function $s _ { A B } ( b )$ relies on the short range of the strong interaction. Due to this property the phase shift on a nucleus comes out the sum of those for the independent scattering of the constituent nucleons. The function $s _ { A B } ( b )$ reads

$$
s _ {A B} (b) = \langle A, | \langle B | \left\{\prod_ {i j} [ 1 - \Gamma_ {N N} (b + x _ {i} - y _ {j}) ] \right\} | A, | \rangle B \rangle , \tag {2}
$$

where

$$
\Gamma_ {N N} (b) \equiv 1 - s _ {N N} (b) = \frac {1}{2 \pi i p} \int d ^ {2} q e ^ {i q b} f _ {N N} (q),
$$

$f _ { N N } ( q )$ and $s _ { N N } ( b )$ are the nucleon-nucleon elastic scattering amplitude and the phase shift. The brackets stand for an average over the nucleons’ positions $x _ { i }$ and $y _ { j }$ lying in the same plain with the impact parameter. Each pair $\{ i , j \}$ enters the product only once, meaning that each nucleon from the projectile nucleus can scatter on each nucleon from the target no more than once.

The elastic nucleon-nucleon amplitude, $f _ { N N }$ , is mainly imaginary at the beam energy about 1 GeV per nucleon, $\mathrm { R e } f _ { N N } / \mathrm { I m } f _ { N N } \lesssim 1 0 ^ { - 1 }$ . The standard parametrization

is

$$
f _ {N N} (q) = i p \frac {\sigma_ {N N} ^ {t o t}}{4 \pi} e ^ {- \frac {1}{2} \beta q ^ {2}}, \tag {3}
$$

where $\sigma _ { N N } ^ { t o t }$ is the total nucleon-nucleon cross section. The slope $\beta$ is related to an effective interaction radius $a ^ { 2 } = 2 \pi \beta$ .

The elastic amplitude is simple related to the total cross section through the optic theorem,

$$
\sigma_ {A B} ^ {t o t} = \frac {4 \pi}{p} \mathrm {I m} f _ {A B} (q = 0) = 2 \int d ^ {2} b \left[ 1 - s _ {A B} (b) \right].
$$

The difference between the total cross section and the integrated elastic cross section,

$$
\sigma_ {A B} ^ {e l} = \int d ^ {2} b \left[ 1 - s _ {A B} (b) \right] ^ {2}, \tag {4}
$$

yields the reaction cross section,

$$
\sigma_ {A B} ^ {r} = \sigma_ {A B} ^ {t o t} - \sigma_ {A B} ^ {e l} = \int d ^ {2} b \left[ 1 - s _ {A B} ^ {2} (b) \right].
$$

The amplitude of the process when the target nucleus $B$ is exited or disintegrated after collision with the projectile takes in the Glauber approach a form similar to (2),

$$
s _ {A B ^ {*}} (b) = \langle A, B ^ {*} | \left\{\prod_ {i j} [ 1 - \Gamma_ {N N} (b + x _ {i} - y _ {j}) ] \right\} | A, B \rangle , \tag {5}
$$

Denoting through $| B ^ { \prime } \rangle = \{ | B \rangle , | B ^ { * } \rangle \}$ the set of all target states and using its completeness,

$$
\sum_ {B ^ {\prime}} \left| B ^ {\prime} \right\rangle \left\langle B ^ {\prime} \right| = \left| B \right\rangle \left\langle B \right| + \sum_ {B ^ {*}} \left| B ^ {*} \right\rangle \left\langle B ^ {*} \right| = 1, \tag {6}
$$

one gets for the cross section $A B  A B ^ { \prime }$

$$
\sigma_ {A B \rightarrow A B ^ {\prime}} = \int d ^ {2} b \left[ 1 - 2 s _ {A B} (b) + J _ {A B} (b) \right], \tag {7}
$$

where

$$
\begin{array}{l} J _ {A B} (b) = \langle A | \langle B | \left\{\prod_ {i j} [ 1 - \Gamma_ {N N} (b + x _ {i} - y _ {j}) ] \right\} | A \rangle \tag {8} \\ \times \langle A | \left\{\prod_ {i j ^ {\prime}} \left[ 1 - \Gamma_ {N N} (b + x _ {i} - y _ {j} ^ {\prime}) \right] \right\} | B \rangle | A \rangle . \\ \end{array}
$$

Subtracting from (7) the elastic cross section (4) we arrive at the interaction cross section,

$$
\sigma_ {A B} ^ {I} = \sigma_ {A B} ^ {r} - \sigma_ {A B \rightarrow A B ^ {*}}, \quad \sigma_ {A B \rightarrow A B ^ {*}} = \int d ^ {2} b \left[ J _ {A B} (b) - s _ {A B} ^ {2} (b) \right]. \tag {9}
$$

The generating function method $^ 2$ relies on the identity

$$
\begin{array}{l} \int \frac {D \Phi D \Phi^ {*}}{2 \pi i} \exp \Bigl \{- \int d ^ {2} x d ^ {2} y \Phi (x) \Delta^ {- 1} (x - y) \Phi^ {*} (y) + \sum_ {i} \Phi (x _ {i}) + \sum_ {j} \Phi^ {*} (y _ {j}) \Bigr \} \\ = \exp \left\{\sum_ {i, j} \Delta \left(x _ {i} - y _ {j}\right) \right\} = \left\{\prod_ {i j} \left[ 1 - \Gamma_ {N N} \left(x _ {i} - y _ {j}\right) \right] \right\}, \tag {10} \\ \end{array}
$$

valid for the function $\Delta ( x - y )$ chosen to obey the equation

$$
e ^ {\Delta (x - y)} - 1 = - \Gamma_ {N N} (x - y). \tag {11}
$$

The functional integral can be thought of as an infinite product of two dimensional integrals over the auxiliary independent fields $\Phi ( x )$ and $\Phi ^ { * } ( x )$ at each space point $x$ , the inverse, $\Delta ^ { - 1 } ( x - y )$ , is understood in a functional sense, $\begin{array} { r } { \int d ^ { 2 } z \Delta ^ { - 1 } ( x - z ) \Delta ( z - y ) = } \end{array}$ $\delta ^ { ( 2 ) } ( x - y )$ , $C _ { 0 }$ is the normalization constant unessential for the following.

We assume that the three-dimensional nuclear densities are reduced to the product of one-nucleon densities,

$$
\rho_ {N} (r _ {1}, \ldots , r _ {N}) = \prod_ {i = 1} ^ {N} \rho_ {N} (r _ {i}), \quad \int d ^ {3} r \rho_ {N} (r) = 1,
$$

so that

$$
\langle N | \prod_ {i} F (r _ {i}) | N \rangle = \left[ \int d ^ {3} r F (r) \rho_ {N} (r) \right] ^ {N}
$$

for any function $F ( r )$ .

Combining the formulas (2) and (10) one gets

$$
\begin{array}{l} S _ {A B} (b) = C _ {0} \int \frac {D \Phi D \Phi^ {*}}{2 \pi i} \exp \left\{- \int d ^ {2} x d ^ {2} y \Phi (x) \Delta^ {- 1} (x - y) \Phi^ {*} (y) \right\} \\ \times \left[ \int d ^ {2} x \rho_ {A} ^ {\perp} (x - b) e ^ {\Phi (x)} \right] ^ {A} \left[ \int d ^ {2} y \rho_ {B} ^ {\perp} (y) e ^ {\Phi^ {*} (y)} \right] ^ {B}, \tag {12} \\ \end{array}
$$

where

$$
\rho_ {A, B} ^ {\perp} (x) = \int d z \rho_ {A, B} (z, x), \quad \int d ^ {2} x \rho_ {A, B} ^ {\perp} (x) = 1
$$

are the transverse densities of the colliding nuclei $A$ and $B$ .

An efficient way to deal with the integral (12) is through the generating function,

$$
\begin{array}{l} Z (u, v) = \int \frac {D \Phi D \Phi^ {*}}{2 \pi i} \exp \left\{- \int d ^ {2} x d ^ {2} y \Phi (x) \Delta^ {- 1} (x - y) \Phi^ {*} (y) \right. \tag {13} \\ \left. + u \int d ^ {2} x \rho_ {A} ^ {\perp} (x - b) e ^ {\Phi (x)} + v \int d ^ {2} x \rho_ {B} ^ {\perp} (x) e ^ {\Phi^ {*} (x)} \right\}, \\ \end{array}
$$

$$
S _ {A B} (b) = \left. \frac {1}{Z (0 , 0)} \frac {\partial^ {A}}{\partial u ^ {A}} \frac {\partial^ {B}}{\partial v ^ {B}} Z (u, v) \right| _ {u = v = 0}. \tag {14}
$$

The short distance nature of the nuclear forces turns the generating function into the product of the independent integrals at the points $x _ { i }$ ,

$$
\begin{array}{l} Z (u, v) = \prod_ {x _ {i}} \int \frac {d \Phi (x _ {i}) d \Phi^ {*} (x _ {i})}{2 \pi i} \exp \left\{- \frac {1}{y} \Phi (x _ {i}) \Phi^ {*} (x _ {i}) \right. \\ + u a ^ {2} \rho_ {A} ^ {\perp} (x _ {i} - b) e ^ {\Phi (x _ {i})} + v a ^ {2} \rho_ {B} ^ {\perp} (x _ {i}) e ^ {\Phi^ {*} (x _ {i})} \}, z _ {y} = e ^ {y} = 1 - \frac {1}{2} \frac {\sigma_ {N N} ^ {t o t}}{a ^ {2}} \\ \end{array}
$$

with the parameters $\sigma _ { N N } ^ { t o t }$ and $a$ being defined in (3). Each integral is then evaluated with the help of the identity

$$
\int \frac {d \Phi d \Phi^ {*}}{2 \pi i} e ^ {- \frac {1}{y} \Phi \Phi^ {*}} \exp \left\{u e ^ {\Phi} + v e ^ {\Phi^ {*}} \right\} = y \sum_ {M, N} \frac {e ^ {y M \cdot N}}{M ! N !} u ^ {M} v ^ {N}, \tag {15}
$$

resulting into (see $^ 2$ for details)

$$
Z (u, v) = e ^ {W (u, v)}, \tag {16}
$$

$$
W (u, v) = \frac {1}{a ^ {2}} \int d ^ {2} x \ln \left(\sum_ {M \leq A, N \leq B} \frac {z _ {y} ^ {M N}}{M ! N !} \left[ a ^ {2} u \rho_ {A} ^ {\perp} (x - b) \right] ^ {M} \left[ a ^ {2} v \rho_ {B} ^ {\perp} (x) \right] ^ {N}\right). \tag {17}
$$

Now we are going to apply the same method to evaluate $J _ { A B } ( b )$ function (8). It is the product of two structures like (2) that is why the analog of the formula (12)

comprises two integrals,

$$
\begin{array}{l} J _ {A B} (b) = C _ {0} \int \frac {D \Phi D \Phi^ {*}}{2 \pi i} \int \frac {D \Psi D \Psi^ {*}}{2 \pi i} \\ \times \exp \left\{- \int d ^ {2} x d ^ {2} y \Phi (x) \Delta^ {- 1} (x - y) \Phi^ {*} (y) - \int d ^ {2} x ^ {\prime} d ^ {2} y ^ {\prime} \Phi (x ^ {\prime}) \Delta^ {- 1} (x ^ {\prime} - y ^ {\prime}) \Phi^ {*} (y ^ {\prime}) \right\} \\ \times \langle A | \prod_ {i} e ^ {\Phi (x _ {i})} | A \rangle \langle A | \prod_ {i} e ^ {\Psi (x _ {i} ^ {\prime})} | A \rangle \sum_ {B ^ {\prime}} \langle B | \prod_ {i} e ^ {\Phi (y _ {i})} | B ^ {\prime} \rangle \langle B ^ {\prime} | \prod_ {i} e ^ {\Psi (y _ {i} ^ {\prime})} | B \rangle . \\ \end{array}
$$

Recalling the completeness (6) one gets

$$
\begin{array}{l} J _ {A B} (b) = C _ {0} \int \frac {D \Phi D \Phi^ {*}}{2 \pi i} \int \frac {D \Psi D \Psi^ {*}}{2 \pi i} \\ \times \exp \left\{- \int d ^ {2} x d ^ {2} y \Phi (x) \Delta^ {- 1} (x - y) \Phi^ {*} (y) - \int d ^ {2} x ^ {\prime} d ^ {2} y ^ {\prime} \Phi (x ^ {\prime}) \Delta^ {- 1} (x ^ {\prime} - y ^ {\prime}) \Phi^ {*} (y ^ {\prime}) \right\} \\ \times \left[ \int d ^ {2} x \rho_ {A} ^ {\perp} (x - b) e ^ {\Phi (x)} \right] ^ {A} \left[ \int d ^ {2} x ^ {\prime} \rho_ {A} ^ {\perp} (x ^ {\prime} - b) e ^ {\Psi (x ^ {\prime})} \right] ^ {A} \left[ \int d ^ {2} y \rho_ {B} ^ {\perp} (y) e ^ {\Phi^ {*} (y) + \Phi^ {*} (y)} \right] ^ {B}. \\ \end{array}
$$

Passing to the generating function we have

$$
\begin{array}{l} Z _ {J} \left(u _ {A}, v _ {A}, v _ {B}\right) = \int \frac {D \Phi D \Phi^ {*}}{2 \pi i} \int \frac {D \Psi D \Psi^ {*}}{2 \pi i} \tag {18} \\ \times \exp \left\{- \int d ^ {2} x d ^ {2} y \Phi (x) \Delta^ {- 1} (x - y) \Phi^ {*} (y) - \int d ^ {2} x ^ {\prime} d ^ {2} y ^ {\prime} \Phi (x ^ {\prime}) \Delta^ {- 1} (x ^ {\prime} - y ^ {\prime}) \Phi^ {*} (y ^ {\prime}) \right. \\ \left. + u _ {A} \int d ^ {2} x \rho_ {A} ^ {\perp} (x - b) e ^ {\Phi (x)} + v _ {A} \int d ^ {2} x \rho_ {A} ^ {\perp} (x) e ^ {\Psi (x)} + v _ {B} \int d ^ {2} x \rho_ {B} ^ {\perp} (x) e ^ {\Phi^ {*} (x) + \Psi^ {*} (x)} \right\}. \\ \end{array}
$$

For the short range interaction the integrals over $\Phi$ and $\Psi$ variables turn into the products of the independent integrals at the points $x _ { i }$ ,

$$
\begin{array}{l} Z _ {J} (u _ {A}, v _ {A}, v _ {B}) = \prod_ {x _ {i}} \int \frac {d \Phi (x _ {i}) d \Phi^ {*} (x _ {i})}{2 \pi i} \int \frac {d \Psi (x _ {i}) d \Psi^ {*} (x _ {i})}{2 \pi i} \\ \times \exp \left\{- \frac {1}{y} \Phi (x _ {i}) \Phi^ {*} (x _ {i}) - \frac {1}{y} \Psi (x _ {i}) \Psi^ {*} (x _ {i}) \right. \\ + u _ {A} a ^ {2} \rho_ {A} ^ {\perp} (x _ {i} - b) e ^ {\Phi (x _ {i})} + v _ {A} a ^ {2} \rho_ {A} ^ {\perp} (x _ {i} - b) e ^ {\Psi (x _ {i})} + v _ {B} a ^ {2} \rho_ {B} ^ {\perp} (x _ {i}) e ^ {\Phi^ {*} (x _ {i}) + \Psi^ {*} (x _ {i})} \}. \\ \end{array}
$$

Using again the identity (15) to evaluate the integrals over $\Phi ( x _ { i } )$ , $\Psi ( x _ { i } )$ we arrive at the generating function,

$$
Z _ {J} \left(u _ {A}, v _ {A}, v _ {B}\right) = e ^ {W _ {J} \left(u _ {A}, v _ {A}, v _ {B}\right)}, \tag {19}
$$

$$
{W _ {J} (u _ {A}, v _ {A}, v _ {B})} = {\frac {1}{a ^ {2}} \int d ^ {2} x \ln \big (\sum_ {L \leq 2 A, K \leq B} \frac {z _ {y} ^ {L K}}{M ! N !} \big [ a ^ {2} (u _ {A} + v _ {A}) \rho_ {A} ^ {\perp} (x - b) \big ] ^ {L} \big [ a ^ {2} v _ {B} \rho_ {B} ^ {\perp} (x) \big ] ^ {K} \big).}
$$

Comparing this expression with (16) we conclude that

$$
Z _ {J} \left(u _ {A}, v _ {A}, v _ {B}\right) = Z \left(u _ {A} + v _ {A}, v _ {B}\right) \tag {20}
$$

and, respectively,

$$
J _ {A B} (b) = \frac {\partial^ {A}}{\partial u _ {A} ^ {A}} \frac {\partial^ {A}}{\partial v _ {A} ^ {A}} \frac {\partial^ {B}}{\partial v _ {B} ^ {B}} Z (u _ {A} + v _ {A}, v _ {B}) \Bigg | _ {u _ {A} = v _ {A} = v _ {B} = 0},
$$

or, finally

$$
J _ {A B} (b) = \left. \frac {\partial^ {2 A}}{\partial u ^ {2 A}} \frac {\partial^ {B}}{\partial v} Z (u, v) \right| _ {u = v = 0}. \tag {21}
$$

# 3 Results of the calculations

The function $W ( u , v )$ (16) goes as the series built of the densities overlaps,

$$
t _ {m, n} (b) = \frac {1}{a ^ {2}} \int d ^ {2} x \left[ a ^ {2} \rho_ {A} ^ {\perp} (x - b) \right] ^ {m} \left[ a ^ {2} \rho_ {B} ^ {\perp} (x) \right] ^ {n} \tag {22}
$$

with $m \le 2 A$ and $n \leq B$ . For the following calculations the nucleon density has been taken in a simple Gaussian parameterizations well suited for light nuclei,

$$
\rho (r) = \rho_ {0} e ^ {- \frac {r ^ {2}}{a _ {c} ^ {2}}}, \tag {23}
$$

the value $a _ { c }$ being expressed through the mean square nuclear radius, $a _ { c } = \sqrt ( 3 / 2 ) R _ { r m s }$ . The total nucleon-nucleon cross section and the slope value (averaged over $p p$ and pn interaction) are taken in the amplitude (3) as $3 , 4$

$$
\sigma_ {N N} ^ {t o t} = 4 3 \mathrm {m b}, \quad \beta = 0. 2 \mathrm {f m} ^ {2} \tag {24}
$$

for the energy around 1000 MeV per projectile nucleon.

The mean square radius $R _ { m s }$ has been adjusted to match the experimental interaction cross section $\sigma _ { ^ { 1 2 } \mathrm { C } - ^ { 1 2 } \mathrm { C } } ^ { r } = 8 5 3 \pm 6$ mb at the energy about 1 GeV per nucleon taken from the review .6 With these parameters and the overlap functions (22) evaluated for the distribution (23) one gets the generating function and the amplitudes (14) and (21).

The calculations have been carried out for $\alpha$ –12C, $_ { 1 2 }$ C– $_ { . 1 2 }$ C and $_ { 1 1 }$ Li– $_ { 1 2 }$ C scattering. The last case provides a remarkable example of a halo nucleus $_ { 1 1 }$ Li, which can be

treated as a core $^ { 9 }$ Li surrounded with a halo made up of two neutrons. The density of this composite system is assumed to be the sum

$$
\rho (r) = N _ {c} \rho_ {c} (r) + N _ {v} \rho_ {v} (r) \tag {25}
$$

of the core including $N _ { c } = 9$ nucleons and the halo with $N _ { v } = 2$ valence nucleons. Both the densities are taken in Gaussian form (23), with the parameters $a _ { c }$ being expressed through the mean square radii of the core and the halo. The core radius is found by calculating the interaction cross sections of the scattering of the nucleus $^ { 9 }$ Li, representing the core, on the target $_ { 1 2 }$ C. Comparing the output with the experimental cross sections collected in Ref.,6 we tune the $R _ { c }$ value. Plugging it then into the density (25) (normalized to unity) and comparing the calculated interaction cross sections of the composite $_ { 1 1 }$ Li nucleus scattering on the $_ { 1 2 }$ C with the same data set we extract the halo radius $R _ { v }$ .

Even though the table below shows the small difference between the reaction and the interaction cross sections, it has to be taken into account for the correct analysis of the experimental data.

Table. Mean square radii extracted by comparing the interaction cross section evaluated for the given nucleus scattering on the 12C target with the experimental cross section. The last column presents the reaction cross sections resulting from the obtained radii. The $_ { 1 1 }$ Li core radius is chosen as that for $^ { 9 }$ Li nucleus. The halo radius for the $_ { 1 1 }$ Li is found to match the interaction cross section of its scattering on the $_ { 1 2 }$ C. The experimental data are taken from $_ 6$ for 790 MeV. 1

<table><tr><td></td><td>Experimental cross section, mb</td><td>Mean square radius, fm</td><td>Reaction cross section, mb</td></tr><tr><td>4He</td><td>503 ± 5</td><td>1.64</td><td>523</td></tr><tr><td>12C</td><td>853 ± 6</td><td>2.46</td><td>864</td></tr><tr><td>9Li</td><td>796 ± 6</td><td>2.55</td><td>804</td></tr><tr><td>11Li</td><td>1047 ± 40</td><td>3.28</td><td>1057</td></tr></table>

The nuclear radii found from the data are to be renormalized for the difference between the interaction cross section, which is actually measured, and the reaction one (9). The new value of $_ { 1 2 }$ C radius is 0.02 fm larger than that obtained in the same Gaussian parametrization (23) but when the reaction cross section is matched. This

new target radius is used to get the renormalized radii for the beam nuclei presented in the Table. The mean square radius, $R _ { m }$ , of the $_ { 1 1 }$ Li, treated as the composite core plus halo system in the parametrization (25), is expressed through the mean square radii of the core, $R _ { c }$ and the halo, $R _ { v }$ , as $R _ { m } ^ { 2 } = ( N _ { c } R _ { c } ^ { 2 } + N _ { v } R _ { v } ^ { 2 } ) / ( N _ { c } + N _ { v } )$ . The halo radius is found to be $R _ { v } = 5 . 4 8$ fm. The radii of the $^ { 9 }$ Li and the $_ { 1 1 }$ Li nuclei are 0.11 fm and 0.13 fm larger as compared to those obtained through the reaction cross section.

The increase of the radius when going from the interaction to the reaction cross section is natural since $\sigma _ { A B } ^ { I } ~ < ~ \sigma _ { A B } ^ { R }$ , although the difference between the two cross sections in the Table varies from 4% for $^ 4$ He to 1–1.5% for more heavy nuclear beams in a qualitative agreement with.1

# 4 Conclusion

The difference between the reaction and the interaction cross sections have been calculated for the beam nuclei $^ 4$ He, $_ { 1 1 }$ Li, $_ { 1 2 }$ C scattering on the $^ { 1 2 }$ C target. The results are presented in the Table above. The difference between the two values obtained for the mean square $_ { 1 1 }$ Li halo radius, which are extracted by comparing the evaluated interaction and the reaction cross sections with the experimental one, is 0.13fm, that is about 2%.

It is worth pointing out that the core – halo structure may be more complex than that underlying the density (25). There could be, in principle, a state with the core $^ { 9 }$ Li and two neutrons halo moving around their common center of mass. However the bound state of two neutrons does not exist, which makes three-body configuration of the neutrons and the core more subtle.

# References

[1] I. S. Novikov and Y. Shabelski, Complete Glauber calculations of reaction and interaction cross sections for light-ion collisions, Phys. Atom. Nucl. 78, no.8, 951- 955 (2015) [arXiv:1302.3930 [nucl-th]].   
[2] Y. M. Shabelski and A. G. Shuvaev, “Generating function for nucleus-nucleus scattering amplitudes in Glauber theory, Phys. Rev. C 104, no.6, 064607 (2021) [arXiv:2104.04943 [hep-ph]].

[3] W. Horiuchi, Y. Suzuki, B. Abu-Ibrahim and A. Kohama, Systematic analysis of reaction cross-sections of carbon isotopes, Phys. Rev. C 75, 044607 (2007) [erratum: Phys. Rev. C 76, 039903 (2007)] [arXiv:nucl-th/0612029 [nucl-th]].   
[4] G. D. Alkhazovi, Y. Shabelski and I. S. Novikov, Nuclear Radii of Unstable Nuclei, Int. J. Mod. Phys. E 20, 583-627 (2011) [arXiv:1101.4717 [nucl-th]].   
[5] Y. M. Shabelski and A. G. Shuvaev, High-energy nucleus–nucleus collision and halo radii in different approaches of Glauber theory, Mod. Phys. Lett. A 37, no.37n38, 2250248 (2022) [arXiv:2211.15177 [nucl-th]].   
[6] A. Ozawa, T. Suzuki and I. Tanihata, Nuclear size and related topics, Nucl. Phys. A 693, 32-62 (2001)