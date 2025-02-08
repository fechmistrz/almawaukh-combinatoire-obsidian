> (LICZBY BELLA) Liczbę relacji równoważności na zbiorze $n$-elementowym oznaczamy przez $b_n$ i nazywamy $n$-tą liczbą Bella.

Na przykład $b_3 = 1 + 3 + 1 = 5$, gdyż zbiór $\{1, 2, 3\}$ można podzielić na singletony ($\{1\}$, $\{2\}$, $\{3\}$), singleton i parę ($\{1\}$, $\{2, 3\}$ lub $\{2\}$, $\{1, 3\}$ lub $\{3\}, \{1, 2\}$) albo nie dzielić go wcale ($\{1, 2, 3\}$). Początkowe wyrazy tego ciągu to $$1, 1, 2, 5, 15, 52, 203, 877, 4140, ...$$Szkocki matematyk Eric Temple Bell [[Bell - The iterated exponential integers]] napisał, że liczby Bella były częstym obiektem badań i~wielokrotnie odkrywane na nowo; cytuje tam między innymi Dobińskiego, który udowodnił w~1877 roku wzór ==(WSTAW LINK DO WZORU)== o~nich.

Bell nazywał je liczbami wykładniczymi, współczesna notacja $b_n$ oraz sama nazwa zostały nadane przez Beckera i~Riordana w 1948 roku na cześć nie trudno się domyślić kogo. Mamy więc kolejny przykład działania prawa eponimii Stiglera, że byty nie są nazwane na cześć tego, kto je odkrył!

Liczby Bella spełniają zależność rekurencyjną
$$
\begin{equation}
b_{n+1} = \sum_{k=1}^{n+1} {n \choose k-1} b_{n+1-k}
\end{equation}
$$
z warunkiem brzegowym $b_0 = 1$.

To jest proste ćwiczenie w [[Graham, Knuth, Patashnik - Matematyka konkretna]] s. 413, [[Charalambides - Enumerative combinatorics]] s. 97.

% https://math.stackexchange.com/questions/1974650/proof-of-dobinskis-formula-for-bell-numbers

\begin{proof}
Po lewej stronie zliczamy relacje równoważności na zbiorze $\{1, 2, \ldots, n+1\}$. Po prawej stronie robimy to samo, w następujący sposób: najpierw wybieramy podzbiór $k-1$ elementów, które należą do tej samej klasy abstrakcji co liczba $n$, a następnie zliczamy wszystkie relacje równoważności na pozostałych elementach.
\end{proof}

> Wykładnicza funkcja tworząca liczb Bella to
$$
\begin{equation}
B(x) = \sum_{n=0}^\infty \frac{b_n}{n!} x^n  = \exp(\exp(x) - 1).
\end{equation}
$$

To jest ćwiczenie 11 u~Lovásza \cite[s. 17]{lovasz1993}.

\begin{proof}
% http://www-groups.mcs.st-andrews.ac.uk/~pjc/Teaching/MT5821/1/l9.pdf
Niech $B(x)$ oznacza wykładniczą funkcję tworzącą liczb Bella.
Wtedy
$$
\begin{align}
\frac{\mathrm{d}}{\mathrm{d}x} B(x) & = \sum_{n=1}^\infty \frac{b_n x^{n-1}}{(n-1)!} \\
& = \sum_{n=0}^\infty \sum_{k=1}^n \frac{x^{k-1}}{(k-1)!} \frac{b_{n-k} x^{n-k}}{(n-k)!} \\
& = \sum_{k=0}^\infty \frac{x^k}{k!} \sum_{m=0}^\infty \frac{b_m x^m}{m!} \\
& = \exp(x) B(x).
\end{align}
$$
Dostaliśmy proste równanie różniczkowe, jego rozwiązanie to funkcja $B(x) = C \exp(\exp(x))$.
Z warunku początkowego obliczamy wartość stałej $C = \exp(-1)$.

\begin{corollary}[wzór Dobińskiego]
$$
\begin{equation}
b_n = \frac 1e \sum_{r=0}^\infty \frac{r^n}{r!}.
\end{equation}
$$
\end{corollary}

Wzór ten mówi, że momenty rozkładu Poissona o średniej 1 wyrażają się liczbami Bella.
% In particular, Bn is the nth moment of a Poisson distribution with mean 1.
% https://oeis.org/A000110
Znalazł go Gabriel Dobiński \cite{dobinski1877} w 1877 roku.
Pojawia się jako ćwiczenia 9, 13 u~Lovásza \cite[s. 17]{lovasz1993}.

\begin{proof}
Mamy
$$
\begin{equation}
e^{e^x-1} = \frac{1}{e} e^{e^x} = \frac{1}{e} \sum_{k=0}^\infty \frac{e^{kx}}{k!} = \frac{1}{e} \sum_{k=0}^\infty \frac{1}{k!} \sum_{n=0}^\infty \frac{(kx)^n}{n!}.
\end{equation}
$$
Wiemy, że współczynnik przy $x^n$ musi wynosić $b_n/n!$, skąd wynika już teza.
\end{proof}

% https://en.wikipedia.org/wiki/Bell_number#Permutations
Gardner \cite{gardner1978} opisuje problem, gdzie nieoczekiwanie pojawiają się liczby Bella. Tasujemy talię $n$ kart przez wielokrotne usuwanie wierzchniej karty i ponowne włożenie jej w dowolne miejsce w talii (być może tam, skąd ją przed chwilą wzięliśmy -- na samą górę talii). Wykonanie $n$ ruchów opisanych wyżej prowadzi do $n^n$ różnych tasowań. Okazuje się, że liczba tasowań, które przywracają talię do początkowej kolejności kart wynosi $B_n$ (i że $B_n/n^n$ jest znacznie większe niż $1/n!$).

> Niech  (odpowiednio: ) oznacza liczbę relacji równoważności na zbiorze  elementowym takich, że moc każdej klasy abstrakcji jest parzysta (że klas abstrakcji jest parzyście wiele). Wtedy
$$
\begin{align}
Q(x) & = \sum_{n=0}^\infty \frac{q_n}{n!}x^n = \cosh(\exp x - 1), \\
R(x) & = \sum_{n=0}^\infty \frac{r_n}{n!}x^n = \exp(\cosh x - 1).
\end{align}
$$

To jest ćwiczenie 14 u Lovásza \cite[s. 18]{lovasz1993} oraz ciągi \href{https://oeis.org/A024430}{24430}, \href{https://oeis.org/A005046}{5046} w bazie danych OEIS.

## Do zrobienia:
wft: Charalambides, strona 198