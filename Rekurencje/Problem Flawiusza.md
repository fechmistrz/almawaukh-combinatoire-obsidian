%

  

\subsection{Problem Józefa Flawiusza}

\paragraph{Problem Flawiusza}

Podczas oblężenia Jotopaty w 67 roku n.e. otoczono czterdziestu jeden żydowskich powstańców.

\index[persons]{de Méziriac, Claude}%

Woleli samobójstwo od pojmania, ale żydowskie prawo religijne zabrania odbierania sobie życia.

Powstańcy ustawili się w kole i~kolejno zabijali co trzeciego.

Józef Flawiusz, nie chcąc umierać, szybko policzył, na którym miejscu powinien się ustawić, by być ostatnim.

  

To sformułowanie problemu pochodzi od Claude'a de Méziriaca około 1612 roku.

Historia była wielokrotnie powtarzana po de Méziriacu ze zmieniającymi się liczbami, zarówno powstańców (oryginalnie $n = 41$) jak i tego, co który był eliminowany ($k = 3$).

Na przykład u Hersteina, Kaplansky'ego\footnote{Herstein, I. N.; Kaplansky, I. (1974). Matters Mathematical. Harper and Row. ISBN 9780060428037.} mamy $n = 40$ oraz $k = 7$.

% TODO: zamienić na prawdziwe cytowanie

  

Najprostszy jest przypadek $k = 2$.

Ponumerujmy osoby liczbami od $1$ do $n$ i oznaczmy przez $f_n$ ostatnią osobę, która przeżywa.

Mamy $f_1 = 1$ (oczywiste) oraz

\begin{align}

f_{2i} & = 2f_i - 1\\

f_{2i + 1} & = 2f_i + 1,

\end{align}

co pozwala na szybkie znalezienie początkowych wartości ciągu $f_n$, czyli $1, 1, 3, 1, 3, 5, 7, \ldots$.

Są to kolejne liczby nieparzyste mniejsze od $2, 4, 8, 16, \ldots$.

Zapiszmy $n$ jako $2^m + l$, gdzie $0 \le l < 2^m$ (lub inaczej, $m$ jest maksymalne).

Wtedy $f(n) = 2l + 1$.

  

Przypadek $k = 3$ jest trudniejszy, ale nadal nie zbyt trudny.

Halbeisen, Hungerbühler \cite{halbeisen1997} pokazali w 1997, że istnieje stała $\alpha \approx 0.8111$ o następującej własności.

% TODO: .bib

% TODO: imiona niżej

\index[persons]{Halbeinsen, Lorenz}%

\index[persons]{Hungerbühler, Norbert}%

Niech $m$ będzie największą liczbą całkowitą taką, że $\alpha \cdot (3/2)^m$ po zaokrągleniu ($M$) nie przekracza $n$.

Wtedy

\begin{equation}

    f_n = 3(n - M) + \frac{3}{2} \pm \frac{1}{2}

\end{equation}

dla wszystkich $n \ge 5$, gdzie wybieramy $+$, gdy zaokrągliliśmy do góry i $-$, gdy do dołu.

  

% TODO: Pójdźmy jeszcze tropem wyznaczonym przez Andrew M. Odlyzko oraz Herberta S. Wilfa, którzy w pracy [1] z 1991 roku zaproponowali następujący wzór: ⎢ 2n--1⎥ ⎢⎢ 3- log32 K ⎥⎥ J(n, 3) = 3n + 1− ⎢⎢K(3) , (2) ⎥⎥ ⎣ ⎦ gdzie K(3) jest stałą (obliczoną za pomocą dość skomplikowanej procedury), której wartość do 9-go miejsca po przecinku wynosi 1,622705028. Jawny wzór, nieodwołujący się do żadnych innych procedur, dla J(n, | k), gdy |k > 2 nie jest znany. https://www.deltami.edu.pl/temat/matematyka/kombinatoryka/2019/12/29/Raz_dwa_trzy_wychodz_ty/

  

{

    \color{red}

Przypadek $k \ge 4$ można rozwiązać korzystając z programowania dynamicznego.

Niech powstańcy mają przypisane liczby $1, 2, 3, \ldots$.

Po zabiciu $k$-tej osoby, zostajemy z kręgiem $n - 1$ osób i odliczamy od osoby, która stała na miejscu $(k \mod n) + 1$.

Dostajemy tak zależność rekurencyjną:

\begin{equation}

    f_n = \begin{cases} 1 & \textrm{dla } n = 1 \\

    ((f_{n-1} + k - 1) \mod n) + 1 & \textrm{dla } n > 1.

    \end{cases}

\end{equation}

  

Daje się to zapisać prościej, jeśli liczymy od zera:

\begin{equation}

    g_n = \begin{cases} 0 & \textrm{dla } n = 1 \\

    (g_{n-1} + k) \mod n & \textrm{dla } n > 1.

    \end{cases}

\end{equation}

  

Dla małych $k$ oraz dużych $n$ warto przyjąć inną strategię: zabić równocześnie $k$-tą, $2k$-tą, ..., $\lfloor n/k \rfloor k$-tą osobę, po czym zmienić numerowanie.

Wtedy

\begin{equation}

    g_{n} = \begin{cases}

        0 & \textrm{dla } n = 1 \\

        (g_{n-1} + k) \mod n & \textrm{dla } 1 < n < k \\

        ...

    \end{cases}

\end{equation}

}

  

% TODO: Matematyka konkretna, zadanie 1.21 (dobrzy i źli)

  

Dla każdego początkowego ustawienia (pozycji Flawiusza wśród $n$ osób) można dobrać takie $k$, żeby Flawiusz przeżył.

Jest to treść zadania 1.23 w \cite{grahamknuthpatashnik2011}.

Wcześniejsze zadanie 1.13 pyta, gdzie powinien ustawić się przyjaciel Flawiusza, żeby też nie zginał.

Odpowiedź brzmi: na pozycji 1 ($n = 3$), 3, 5, 1 ($n = 6$), 3, 5, 7, 9, 11, 1 ($n = 12$) i tak dalej; widać już, że tym razem trzeba przedstawić $n$ w postaci $3 \cdot 2^m + l$.

  

%