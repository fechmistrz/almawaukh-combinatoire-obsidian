Liczby Catalana to $$(c_n) = 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, \ldots$$Po raz pierwszy opisał je [[Leonhard, Euler]] w osiemnastym wieku; interesowało go, na ile sposobów można rozciąć wielokąt foremny na trójkąty. Wiemy od Stanleya (https://arxiv.org/pdf/2105.07884), że nazwa "liczby Catalana" została zasugerowana przez [[Riordan, John]] *(R. Stanley, Catalan Numbers, Cambridge University Press, New York, 2015., pp. 186–187)*, w recenzji pracy Motzkina (https://mathscinet.ams.org/mathscinet-getitem?mr=24411 - brak dostępu). Eugène Catalan pracował nad [[Wieże Hanoi]], wtedy też odkrył, że liczby Catalana opisują liczbę wyrażeń w nawiasach.

Ciąg $c_n$ pojawia się często jako rozwiązanie problemów kombinatorycznych:
- $c_n$ to liczba słów Dycka długości $2n$, czyli wyrażeń złożonych z nawiasów połączonych w pary tak, że nawiasy otwierające ( występują zawsze przed odpowiadającym im domykającymi ). -- sprawdź [[Charalambides - Enumerative combinatorics]] s. 100
- $c_n$ to liczba pełnych drzew binarnych z $n+1$ liśćmi.
- $c_n$ to liczba monotonicznych (w prawo lub do góry) ścieżek z dolnego lewego wierzchołka do górnego prawego w kwadracie $n \times n$ tak, by nie przekroczyć przekątnej.
- $c_n$ to liczba triangulacji $(n+2)$-kąta wypukłego.

(To tylko niektóre intepretacje, wiele więcej można znaleźć w [[Stanley - Enumerative combinatorics, vol. 2]]). Ciąg spełnia zależność rekurencyjną
$$
\begin{equation}
c_0 = 1, \quad c_{n+1} = \sum_{k=0}^n c_k c_{n-k}.
\end{equation}
$$
Aby rozwiązać rekurencję \ref{eqn:catalan_definition}, wykorzystamy funkcje tworzące. Funkcja tworząca $C(z)$ spełnia równanie
$$
\begin{equation}
C(z) = 1 + z C(z)^2,
\end{equation}
$$
więc
$$
\begin{equation}
C(z) = \frac{1 \pm \sqrt{1-4z}}{2z}.
\end{equation}
$$
Bierzemy rozwiązanie z minusem, bo tylko wtedy $c_0 = \lim_{z \to 0} C(z) = 1$. Mamy
$$
\begin{equation}
\sqrt{1-4z} = \sum_{n=0}^\infty {1/2 \choose n} (-4z)^n = 1 - \sum_{n=1}^\infty \frac{1}{2n-1}{2n \choose n} z^n,
\end{equation}
$$
co po wstawieniu do definicji szeregu $C(z)$ daje
$$
\begin{align}
C(z) = \sum_{n=0}^\infty {2n \choose n} \frac{z^n}{n+1}.
\end{align}
$$
Funkcja tworząca -- [[Charalambides - Enumerative combinatorics]], s. 196

## Liczby Lobba
**Liczby Lobba** stanowią uogólnienie liczb Catalana. $l_{m,n}$ to ilość rozstawień $n+m$ otwartych oraz $n-m$ zamkniętych nawiasów tak, by otrzymany napis był początkiem jakiegoś słowa Dycka. https://en.wikipedia.org/wiki/Dyck_language


# Do zrobienia
Do zrobienia:
- https://en.wikipedia.org/wiki/Schröder_number
- https://en.wikipedia.org/wiki/Catalan_number
- https://en.wikipedia.org/wiki/Schröder–Hipparchus_number -> Delannoy number ? https://en.wikipedia.org/wiki/Delannoy_number
- % TODO: The n×n Hankel matrix whose (i, j) entry is the Catalan number Ci+j−2 has determinant 1
- % TODO: https://en.wikipedia.org/wiki/Motzkin_number
- % TODO: https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Hipparchus_number
- % TODO: https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Etherington_number
