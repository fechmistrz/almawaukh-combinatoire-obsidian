Do zrobienia:
- ==https://en.wikipedia.org/wiki/Schröder_number==
- ==https://en.wikipedia.org/wiki/Catalan_number==
- https://en.wikipedia.org/wiki/Schröder–Hipparchus_number -> Delannoy number ? https://en.wikipedia.org/wiki/Delannoy_number

Ciąg (liczb) Catalana został opisany po raz pierwszy w osiemnastym wieku przez Leonharda Eulera, którego interesowało, ile jest triangulacji wielokąta foremnego. Ponieważ Eugène Catalan odkrył (kiedy pracował nad wieżami Hanoi (!)), że wyrazy tego ciągu opisują liczbę wyrażeń w~nawiasach, dzisiaj nazywamy go właśnie ciągiem Catalana -- tak zasugerował John Riordan w recenzji pracy Motzkina z 1948 roku (\href{https://mathscinet.ams.org/mathscinet-getitem?mr=24411}{MR24411}).

Ciąg spełnia zależność rekurencyjną
$$
\begin{equation}
c_0 = 1, \quad c_{n+1} = \sum_{k=0}^n c_k c_{n-k}.
\end{equation}
$$
Ciąg $c_n$ pojawia się często jako rozwiązanie problemów kombinatorycznych:
- $c_n$ to liczba słów Dycka długości , czyli wyrażeń złożonych z nawiasów połączonych w pary tak, że nawiasy otwierające ( występują zawsze przed domykającymi ).
- $c_n$ to liczba pełnych drzew binarnych z $n+1$ liśćmi.
- $c_n$ to liczba ścieżek z dolnego lewego wierzchołka do górnego prawego w kwadracie $n \times n$tak, by nie przekroczyć przekątnej i tak, by były monotoniczne (możemy poruszać się tylko w prawo lub do góry).
- $c_n$ to liczba triangulacji $(n+2)$-kąta wypukłego.

(Nawiasy: \cite[s. 100]{charalambides2002})
Ft: Charalambides, strona 196

To tylko niektóre intepretacje, wiele więcej można znaleźć w \cite{stanley1999}. Aby rozwiązać rekurencję \ref{eqn:catalan_definition}, wykorzystamy funkcje tworzące. Funkcja tworząca $C(z)$ spełnia równanie
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
Bierzemy rozwiązanie z minusem, bo tylko wtedy $c_0 = \lim_{z \to 0} C(z) = 1$.

Mamy
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


% TODO: The n×n Hankel matrix whose (i, j) entry is the Catalan number Ci+j−2 has determinant 1
% TODO: https://en.wikipedia.org/wiki/Motzkin_number
% TODO: https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Hipparchus_number
% TODO: https://en.wikipedia.org/wiki/Wedderburn%E2%80%93Etherington_number
# Do zrobienia
Uogólnienie: https://en.wikipedia.org/wiki/Lobb_number