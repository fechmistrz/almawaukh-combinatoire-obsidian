Funkcje tworzące to formalne szeregi potęgowe, czyli wyrażenia postaci $a_0 + a_1x + a_2x^2 + \ldots$, gdzie liczby $\{a_n\}_0^\infty$ nazywamy współczynnikami funkcji tworzącej.

Nie rozpatruje się ich analitycznych własności, dlatego
$$
\begin{equation}
F(x) = \sum_{n=0}^\infty n! \cdot x^n = 1 + x + 2x^2 + 6x^3 + 24x^4 + 120x^5 + \ldots
\end{equation}
$$
jest dobrze zdefiniowanym obiektem, nawet jeśli promień zbieżności szeregu potęgowego wynosi $0$ (to znaczy, funkcja $f \colon \mathbb R \to \mathbb R$, którą zadaje, jest określona tylko w punkcie $x=0$).

Jak piszą [[Graham, Knuth, Patashnik - Matematyka konkretna]] s. 369 *,,(...) będziemy w tym rozdziale ignorować kwestię zbieżności szeregów. Stanowi ona bardziej przeszkodę niż pomoc''). Wilf [[Wilf - Generatingfunctionology]] s. 30 wspomina *,,the point of this section is that there's no need for the guilt, because the various manipulations can be carried out in the ring of formal power series, where questions of convergence are nonexistent''*; podobne opinie znaleźć można w każdym podręczniku kombinatoryki.

## Działania na funkcjach tworzących
Funkcje tworzące nie są dokładnie tym samym, co formalne szeregi potęgowe. Wprowadzimy dla nich wygodną notację, obowiązującą od teraz aż do ostatniej strony książki.

Niech $\{a_n\}_{n=1}^\infty$ będzie nieskończonym ciągiem liczb, zaś
$$
\begin{equation}
A(z) = a_0 + a_1 z + \ldots = \sum_{n = 0}^\infty a_n z^n.
\end{equation}
$$
stowarzyszoną z nim funkcją tworzącą. Współczynnik $a_n$ stojący przy $z^n$ w $A(z)$ będzie często oznaczany przez $[z^n]A(z)$. (Nie tylko tu, ale wszędzie, gdzie to możliwe, funkcje tworzące oznaczamy wielkimi literami, a~stowarzyszone z nimi ciągi -- małymi).

Tak jak Wilf \cite[s. 23]{wilf1994} będziemy często skracać ,,funkcja tworząca'' do ,,ft''.

Niech szeregi potęgowe $A(z), B(z)$ będą ft ciągów $a_n, b_n$, dopóki nie zaznaczono inaczej. Pokażemy od razu, jakie działania można wykonywać na ft $A$ i $B$.
### Kombinacje liniowe
Szeregi potęgowe tworzą przestrzeń liniową nad ciałem $\C$, możemy więc je dodawać oraz mnożyć przez skalary [[Wilf - Generatingfunctionology]] s. 31:
$$
\begin{equation}
\sum_{n = 0}^\infty (\alpha a_n + \beta b_n) z^n = \alpha A(z) + \beta B(z).
\end{equation}
$$
Zamiana zmiennej $z$ przez jej stałą wielokrotność $\lambda z$:
$$
\begin{equation}
\sum_{n = 0}^\infty \lambda^n a_n z^n = F(\lambda z).
\end{equation}
$$
jest szczególnie użyteczna, kiedy $\lambda = -1$.
### Przesunięcie w prawo albo lewo
Przemnożenie funkcji tworzącej przez $z^m$ odpowiada dopisaniu $m$ zer na początku ciągu, który ta funkcja koduje. Operacja przeciwna, usuwanie początkowych $m$ wyrazów ciągu, polega na odjęciu ,,głowy'' szeregu (tak, by został tylko ,,ogon'') i podzieleniu całości przez $z^m$.
$$
\begin{align}
\sum_{n = 0}^\infty a_{n - m} z^n & = z^m A(z), \\
\sum_{n = 0}^\infty a_{n + m} z^n & = \frac{A(z) - a_0 - a_1z - \ldots - a_{m-1}z^{m-1}}{z^m}.
\end{align}
$$
### Różniczkowanie
Często potrzebujemy funkcji tworzącej dla iloczynu ciągu $a_n$ oraz $n$ albo ogólniej, pewnego wielomianu. ,,Różniczkowanie jest tym, co pozwala nam to zrobić'':
$$
\begin{equation}
\sum_{n = 0}^\infty n a_{n} z^n = zA'(z).
\end{equation}
$$
Regułę w jej ogólniejszej wersji wysławia [[Wilf - Generatingfunctionology]] s. 35: niech $P$ będzie wielomianem jednej zmiennej, wtedy
$$
\begin{equation}
\sum_{n = 0}^\infty P(n) a_{n} z^n = P \left( x \frac{\mathrm{d}}{\mathrm{d}x} \right) A(z).
\end{equation}
$$
Jeżeli szereg potęgowy przedstawiający ft $A(z)$ zbiega wewnątrz pewnego dysku do funkcji analitycznej, to możemy za $z$ podstawić dowolną liczbę z dysku zbieżności. (Właśnie to odróżnia ft od ,,surowych'' formalnych szeregów potęgowych). Wilf podaje od razu przykład, który to tłumaczy.

> Znaleźć wzór na sumą kwadratów pierwszych $N$ liczb naturalnych, $1^2 + 2^2 + \ldots + N^2$.

Zacznijmy od wzoru na sumę szeregu geometrycznego:
$$
\begin{equation}
\sum_{n=0}^N x^n = \frac{x^{N+1}-1}{x-1}
\end{equation}
$$
i zauważmy, że możemy najpierw zróżniczkować go dwukrotnie, a następnie podstawić $x = 1$:
$$
\begin{align}
\sum_{n=0}^N n^2 & = \left . x \frac{\mathrm{d}}{\mathrm{d}x} x \frac{\mathrm{d}}{\mathrm{d}x} \frac{x^{N+1}-1}{x-1} \right |_{x=1} \\
& = \left . x \frac{\mathrm{d}}{\mathrm{d}x} \frac{N x^{N+2} - (N+1) x^{N+1} + x}{(x-1)^2} \right |_{x=1} \\
& = \left . \frac{x \left((-2 N^2-2N+1) x^{N+1}+N^2 x^{N+2}+(N+1)^2 x^{N}-x-1\right)}{(x-1)^3}  \right |_{x=1} \\
& = \frac{1}{6} N (N+1) (2N+1).
\end{align}
$$
### Całkowanie
Jak nietrudno się domyślić, całkowanie pozwala dzielić składniki przez $n$:
$$
\begin{equation}
\sum_{n = 1}^\infty \frac{a_{n-1}}{n} z^n = \int_0^z A(t) \,\mathrm{d}t.
\end{equation}
$$
(Graham, Knuth, Patashnik podpowiadają, że jeśli przesuniemy najpierw $A(z)$ o~jedno miejsce w~lewo, a dopiero potem przecałkujemy, dostaniemy funkcję tworzącą dla ${a_n}/n$).
### Splot
Przemnożenie przez siebie funkcji $A(z), B(z)$, czyli znalezienie ich iloczynu Cauchy'ego, odpowiada splataniu ciągów ([[Wilf - Generatingfunctionology]] s. 31, 36):
$$
\begin{equation}
\sum_{n = 0}^\infty \left(\sum_{k=0}^n a_k b_{n-k}\right) z^n = A(z) \cdot B(z).
\end{equation}
$$
Nie jest trudno wywnioskować stąd, co stanie się, kiedy przemnożymy większą ilość funkcji przez siebie:
$$
\begin{equation}
\sum_{n = 0}^\infty \left(\sum_{n_1 + \ldots + n_k = n} a_{n_1} a_{n_2} \cdot \ldots \cdot a_{n_k}\right) z^n = A(z)^k.
\end{equation}
$$
# W przygotowaniu
\paragraph{permutacje bez punktów stałych} Charalambides, strona 191
Funkcje tworzące momenty: Charalambides, s. 215
Historia: Charalambides, strona 223
% wykładnicze
% ft momenty