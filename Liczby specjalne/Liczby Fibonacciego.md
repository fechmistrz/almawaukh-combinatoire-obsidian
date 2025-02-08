Do zrobienia:
- https://en.wikipedia.org/wiki/Fibonacci_sequence

==The Fibonacci numbers were first described in [Indian mathematics](https://en.wikipedia.org/wiki/Indian_mathematics "Indian mathematics") as early as 200 BC in work by [Pingala](https://en.wikipedia.org/wiki/Pingala "Pingala") on enumerating possible patterns of [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit "Sanskrit") poetry formed from syllables of two lengths.[[3]](https://en.wikipedia.org/wiki/Fibonacci_sequence#cite_note-GlobalScience-3)[[4]](https://en.wikipedia.org/wiki/Fibonacci_sequence#cite_note-HistoriaMathematica-4)[[5]](https://en.wikipedia.org/wiki/Fibonacci_sequence#cite_note-Donald_Knuth_2006_50-5) They are named after the Italian mathematician Leonardo of Pisa, also known as [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci "Fibonacci"), who introduced the sequence to Western European mathematics in his 1202 book _[Liber Abaci](https://en.wikipedia.org/wiki/Liber_Abaci "Liber Abaci")_.[[6]](https://en.wikipedia.org/wiki/Fibonacci_sequence#cite_note-FOOTNOTESigler2002404%E2%80%9305-6)== In the Sanskrit poetic tradition, there was interest in enumerating all patterns of long (L) syllables of 2 units duration, juxtaposed with short (S) syllables of 1 unit duration. Counting the different patterns of successive L and S with a given total duration results in the Fibonacci numbers: the number of patterns of duration m units is _F__m_+1.

Opisane niżej liczby pierwszy przedstawił Leonardo Fibonacci w księdze matematycznej ,,Liber abaci'' z 1202 roku, użył ich do policzenia rozmiaru populacji królików. Definiuje się je (liczby, nie króliki) wzorem rekurencyjnym $F_n = F_{n-1} + F_{n-2}$ dla $n \ge 2$, $F_1 = 1$, $F_0 = 0$. Gdzie jeszcze się pojawiają?
- - The number of binary strings of length n without consecutive 1s is the Fibonacci number _F__n_+2. For example, out of the 16 binary strings of length 4, there are _F_6 = 8 without consecutive 1s—they are 0000, 0001, 0010, 0100, 0101, 1000, 1001, and 1010. Such strings are the binary representations of [Fibbinary numbers](https://en.wikipedia.org/wiki/Fibbinary_number "Fibbinary number"). Equivalently, _F__n_+2is the number of subsets S of {1, ..., _n_} without consecutive integers, that is, those S for which {_i_, _i_ + 1} ⊈ _S_ for every i. A [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") with the sums to _n_+1 is to replace 1 with 0 and 2 with 10, and drop the last zero.
- - The Fibonacci numbers are also an example of a [complete sequence](https://en.wikipedia.org/wiki/Complete_sequence "Complete sequence"). This means that every positive integer can be written as a sum of Fibonacci numbers, where any one number is used once at most. -> ZECKENDORF

Jednym z pierwszych twierdzeń udowodnionych o nich była tożsamość Cassiniego:
$$ 
\begin{equation}
F_{n+1}F_{n-1} - F_n^2 = (-1)^n
\end{equation}
$$
odkryta przez Jean-Dominique Cassiniego w 1680 roku, chociaż Johannes Kepler wiedział o~niej już w 1608 roku. (Patrz Miodrag Petkovic: Famous Puzzles of Great Mathematicians. AMS, 2009, ISBN 9780821848142, S. 30-31). Wzór ten ma dwa uogólnienia.

I tak pierwsze znalazł Eugène Catalan w~1879 roku ($r = 1$):
$$
\begin{equation}
F_n^2 - F_{n-r}F_{n+r} = (-1)^{n-r} F_r^2,
\end{equation}
$$
a drugie francuski inżynier Philbert d'Ocagne około 1889 roku ($m = n-1$), patrz https://hsm.stackexchange.com/questions/2974/history-of-the-docagnes-identity-for-fibonacci-numbers:
$$
\begin{equation}
F_mF_{n+1} - F_n F_{m+1} = (-1)^n F_{m-n}.
\end{equation}
$$
Mamy wreszcie wzór Bineta:
$$
\begin{equation}
F_n = \frac{\varphi^n - (1-\varphi)^n}{\sqrt{5}}, \quad \varphi = \frac{1 + \sqrt{5}}{2}.
\end{equation}
$$
Pierwszy raz wzór opublikował Daniel Bernoulli w 1728 roku, ale potem został zapomniany i odkryty jeszcze raz przez Jacquesa Bineta w 1843 roku.

**Do zrobienia**: https://en.wikipedia.org/wiki/Fibonacci_sequence#Matrix_form

> Rozwiązać rekurencję $f_n = f_{n-1} + f_{n-2} + [n = 1]$, gdzie zakładamy, że $f_n = 0$ jeśli $n < 0$.

==Like every [sequence](https://en.wikipedia.org/wiki/Sequence "Sequence") defined by a homogeneous [linear recurrence with constant coefficients](https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients "Linear recurrence with constant coefficients"), the Fibonacci numbers have a [closed-form expression](https://en.wikipedia.org/wiki/Closed-form_expression "Closed-form expression").==. Obydwie strony mnożymy przez $z^n$ oraz sumujemy po wszystkich $n$:
$$
F(z) = z F(z) + z^2 F(z) + z.
$$
Otrzymane równanie posiada dokładnie jedno rozwiązanie,
$$
F(z) = \frac{z}{1-z-z^2}.
$$
Pozostaje rozwinąć tę funkcję w szereg potęgowy i sprawdzić, jaki współczynnik stoi przy $z^n$. Z kursu analizy wiemy, że każdą funkcję wymierną można rozłożyć na ułamki proste. Pominiemy rachunki, mamy
$$
\begin{equation}
f_n = \frac{1}{\sqrt{5}} \left( \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right),
\end{equation}
$$
czyli znany już wzór Bineta.

## Jakieś przypadkowe zależności
$$
\sum_{i=1}^{n} F_{i}=F_{n+2}-1
$$
// https://en.wikipedia.org/wiki/Fibonacci_sequence#Matrix_form -> A different trick may be used to prove
$$
\sum_{i=1}^{n}F_{i}^{2}=F_{n}F_{n+1}
$$
Do zrobienia
- \cite[przykład 2.29]{charalambides2002}
## Inne liniowe rekurencje z nazwami
https://en.wikipedia.org/wiki/Padovan_sequence: $p_0 = p_1 = p_2 = 1$, $p_n = p_{n-2} + p_{n-3}$
https://en.wikipedia.org/wiki/Lucas_number: $l_0 = 2, l_1 = 1$, $l_{n} = l_{n-1} + l_{n-2}$. *Liczby Lucasa* $L_n$ to ciąg liczb naturalnych, które zliczają być-może-puste podzbiory $n$ krzeseł umieszczonych na brzegu okrągłego stołu, które nie zawierają sąsiadujących ze sobą krzeseł. Początkowe wyrazy tego ciągu to 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199. Patrz też https://math.stackexchange.com/questions/1166269/lucas-numbers-and-fibonacci
Perrin number -> https://en.wikipedia.org/wiki/Perrin_number. *The Perrin numbers bear the same relationship to the Padovan sequence as the Lucas numbers do to the Fibonacci sequence.*
