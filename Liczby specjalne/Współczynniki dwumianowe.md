==https://en.wikipedia.org/wiki/Binomial_coefficient==

==The [Indian](https://en.wikipedia.org/wiki/India "India") mathematician [Mahāvīra](https://en.wikipedia.org/wiki/Mah%C4%81v%C4%ABra_\(mathematician\) "Mahāvīra (mathematician)") (c. 850) provided formulae for the number of [permutations](https://en.wikipedia.org/wiki/Permutation "Permutation") and [combinations](https://en.wikipedia.org/wiki/Combination "Combination"),[[13]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-13)[[14]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-14) and these formulas may have been familiar to Indian mathematicians as early as the 6th century CE.[[15]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-15) The [philosopher](https://en.wikipedia.org/wiki/Philosopher "Philosopher") and [astronomer](https://en.wikipedia.org/wiki/Astronomer "Astronomer") Rabbi [Abraham ibn Ezra](https://en.wikipedia.org/wiki/Abraham_ibn_Ezra "Abraham ibn Ezra") (c. 1140) established the symmetry of [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient "Binomial coefficient"), while a closed formula was obtained later by the [talmudist](https://en.wikipedia.org/wiki/Talmudist "Talmudist") and [mathematician](https://en.wikipedia.org/wiki/Mathematician "Mathematician") [Levi ben Gerson](https://en.wikipedia.org/wiki/Levi_ben_Gerson "Levi ben Gerson") (better known as Gersonides), in 1321.[[16]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-16) The arithmetical triangle—a graphical diagram showing relationships among the binomial coefficients—was presented by mathematicians in treatises dating as far back as the 10th century, and would eventually become known as [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle "Pascal's triangle"). Later, in [Medieval England](https://en.wikipedia.org/wiki/Medieval_England "Medieval England"), [campanology](https://en.wikipedia.org/wiki/Campanology "Campanology") provided examples of what is now known as [Hamiltonian cycles](https://en.wikipedia.org/wiki/Hamiltonian_cycle "Hamiltonian cycle") in certain [Cayley graphs](https://en.wikipedia.org/wiki/Cayley_graph "Cayley graph") on permutations.[[17]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-17)[[18]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-18)==

Współczynnik dwumianowy $n \choose k$, znany też jako symbol Newtona, wyraża liczbę sposobów, na które można wybrać $k$ elementów ze zbioru liczącego $n$ elementów.
==TODO: DOPISAĆ, DLACZEGO TO SIĘ TAK NAZYWA. Charalambides s. 111, 115==
% vandermonde 1772 - notacja dla silnii
% Bernoulli 1713 - wzór dwumianowy
% pierwsza notacja dla sumbolu NEwtona - Euler 1781' obecnie używamy Raabe 1851

> Na ile sposobów możemy wybrać  elementowy podzbiór zbioru  tak, by nie zawierał pary kolejnych liczb całkowitych?

% f(n, k) = (n-k+1 choose k)
% sum k 0 n f(n, k) = F_{n+2} (fibo)
(To jest [[Aigner - A course in enumeration]], ćwiczenie 1.8 oraz [[Charalambides - Enumerative combinatorics]], przykład 2.28).

% sum (n, k) = 2^n : charalambides, s. 116
% suma k (n, k)

Mamy
$$
\begin{equation}
{n \choose k} = \frac{n(n-1) \cdot \ldots \cdot (n-(k-1))}{k (k-1) \cdot \ldots \cdot 1}.
\end{equation}
$$
Kombinatoryczna interpretacja dopuszcza tylko nieujemne liczby całkowite w górnym oraz dolnym indeksie, ale ograniczenia te łatwo usuwają się:
$$
\begin{equation}
{n \choose k} = \begin{cases}
r\fallingfactorial{k} / k! & k \ge 0 \textrm{, całkowite} \\ 0 & k < 0\textrm{, całkowite}
\end{cases}
\end{equation}
$$
Reguła symetrii mówi, że jeżeli $k, n$ są całkowite i $n \ge 0$, to
$$
\begin{equation}
{n \choose k} = {n \choose n-k}.
\end{equation}
$$
Ten wzór ma prostą interpretację kombinatoryczną: wybierając $k$ przedmiotów ze zbioru $n$-elementowego jednocześnie wybieramy pozostałe $n-k$ przedmiotów.

Tożsamość pochłaniania pozwala przesuwać liczby do i ze współczynnika dwumianowego: jeśli $k \neq 0$ jest całkowite, to
$$
\begin{equation}
{n \choose k} = \frac{n}{k} {n-1 \choose k-1}.
\end{equation}
$$
Jest jeszcze reguła dodawania: dla całkowitych $k$ mamy
$$
\begin{equation}
{n \choose k} = {n-1 \choose k-1} + {n-1 \choose k}.
\end{equation}
$$
Kiedy $n$ też jest całkowite, możemy podać dowód kombinatoryczny: żeby spośród $n$ osób wybrać $k$-osobową drużynę możemy wziąć najstarszą osobę i dobrać do niej $k-1$ graczy albo wziąć $k$ osób, pomijając za każdym razem tę najstarszą osobę.

(Wykorzystaliśmy tu regułę dodawania ze strony \pageref{rule_of_sum} jak Aigner \cite[s. 5]{aigner2007}).
Sumowanie po górnym indeksie orzeka, że dla całkowitych $m, n \ge 0$ mamy
$$
\begin{equation}
\sum_{k=0}^{n} {k \choose m} = {n+1 \choose m+1}.
\end{equation}
$$
(Jeśli chcemy ze zbioru $n+1$ biletów ponumerowanych $0, 1, \ldots, n$ wybrać $m+1$ biletów, to na ${k \choose m}$ sposobów wybieramy je tak, żeby największy był bilet $k$).

Oprócz sumowania górnego jest też sumowanie równoległe: dla całkowitych $n$ mamy
$$
\begin{equation}
\sum_{k=-\infty}^{n} {n+k \choose k} = {n+k+1 \choose n}.
\end{equation}
$$
Poniższa równość, prawdziwa dla całkowitych $k$, nazywana jest negowaniem górnego indeksu:
$$
\begin{equation}
{n \choose k} = (-1)^{k} {k-n-1 \choose k}.
\end{equation}
$$
> (WZÓR DWUMIANOWY) Jeśli  jest całkowite lub jeśli , mamy równość
$$
\begin{equation}
(x+y)^n = \sum_k {n \choose k} x^k y^{n-k}.
\end{equation}
$$
Powyższy wzór jest powodem, dlaczego współczynniki dwumianowe nazywa się właśnie tak, a nie inaczej.

> (TOŻSAMOŚĆ CAUCHY'EGO) Jeśli $n$ jest całkowite, to
$$
\begin{equation}
\sum_k {r \choose k}{s \choose n-k} = {r+s \choose n}.
\end{equation}
$$

Tożsamość była znana w Chinach już na początku XIV wieku. Czasami określa się ją jako splot Vandermonde'a, ponieważ Alexander Vandermonde napisał o niej ważną pracę ,,\emph{Mémoire sur les irrationnelles des différents ordres avec une application au cercle}''.
% matematyka konkretna 197

Istnieje prosty dowód tej równości: aby wybrać $n$ osób z grupy $r$ mężczyzn oraz $s$ kobiet należy wybrać $k$ panów oraz $n-k$ pań.

Patrz też: Charalambides \cite[s. 94, 105]{charalambides2002}, który nazywa tak zupełnie inny wzór dla potęg kroczących.



% suma (-1)^(r-k) (n po k) to (n-1 po k-1) - charalambides s. 95


## Uogólnione szeregi dwumianowe i wykładnicze
Książka [[Graham, Knuth, Patashnik - Matematyka konkretna]]a s. 320 wprowadza uogólniony szereg dwumianowy oraz uogólniony szereg wykładniczy, które są źródłem nowych tożsamości ze współczynnikami dwumianowymi. Nie wydają się zbyt ciekawe, dlatego przytoczymy tylko definicję.

Mamy
$$
\begin{align}
B_t(z) & = \sum_{k \ge 0} (tk)\fallingfactorial{k-1} \frac{z^k}{k!}, \\
E_t(z) & = \sum_{k \ge 0} (tk+1)^{k-1} \frac{z^k}{k!}.
\end{align}
$$
Szereg $B_1(z) = 1/(1-z)$ nie jest ciekawy, ale w rozwinięciu $B_2$ pojawiają się liczby Catalana. Szereg $E_1(z)$ jest związany z funkcją W Lamberta, spełnia $E_1(z) = \exp(z E_1(z))$ i mamy:
$$
\begin{equation}
E_1(z) = 1 + z + \frac{3}{2}z^2 + \frac{8}{3}z^3 + \frac{125}{24}z^4 + \ldots
\end{equation}
$$