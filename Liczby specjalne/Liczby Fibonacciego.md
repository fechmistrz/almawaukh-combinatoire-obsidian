%

  

\subsection{Liczby Fibonacciego}

Opisane niżej liczby pierwszy przedstawił Leonardo Fibonacci w księdze matematycznej ,,Liber abaci'' z 1202 roku, użył ich do policzenia rozmiaru populacji królików.

\index[persons]{Fibonacci, Leonardo}%

Definiuje się je (liczby, nie króliki) wzorem rekurencyjnym $F_n = F_{n-1} + F_{n-2}$ dla $n \ge 2$, $F_1 = 1$, $F_0 = 0$.

  

Jednym z pierwszych twierdzeń udowodnionych o nich była tożsamość Cassiniego:

\begin{equation}

    F_{n+1}F_{n-1} - F_n^2 = (-1)^n

\end{equation}

odkryta przez Jean-Dominique Cassiniego w 1680 roku, chociaż Johannes Kepler wiedział o~niej już w 1608 roku\footnote{Patrz Miodrag Petkovic: Famous Puzzles of Great Mathematicians. AMS, 2009, ISBN 9780821848142, S. 30-31}.

\index[persons]{Cassini, Jean-Dominique}%

\index[persons]{Kepler, Johannes}%

Wzór ten ma dwa uogólnienia.

I tak pierwsze znalazł Eugène Catalan w~1879 roku ($r = 1$):

\index[persons]{Catalan, Eugène}%

\begin{equation}

    F_n^2 - F_{n-r}F_{n+r} = (-1)^{n-r} F_r^2,

\end{equation}

a drugie francuski inżynier Philbert d'Ocagne około 1889 roku ($m = n-1$):

% https://hsm.stackexchange.com/questions/2974/history-of-the-docagnes-identity-for-fibonacci-numbers

\begin{equation}

    F_mF_{n+1} - F_n F_{m+1} = (-1)^n F_{m-n}.

\end{equation}

Mamy wreszcie wzór Bineta:

\begin{equation}

    F_n = \frac{\varphi^n - (1-\varphi)^n}{\sqrt{5}}, \quad \varphi = \frac{1 + \sqrt{5}}{2}.

\end{equation}

  

Pierwszy raz wzór opublikował Daniel Bernoulli w 1728 roku, ale potem został zapomniany i odkryty jeszcze raz przez Jacquesa Bineta w 1843 roku.

\index{wzór Bineta}%

\index[persons]{Bernoulli, Daniel}%

\index[persons]{Binet, Jacques}%

  

%


%

  

\begin{exercise}[ciąg Fibonacciego]

    Rozwiązać rekurencję

\begin{equation}

    f_n = f_{n-1} + f_{n-2} + [n = 1],

\end{equation}

gdzie zakładamy, że $f_n = 0$ jeśli $n < 0$.

\end{exercise}

  

\begin{solution}

    Obydwie strony mnożymy przez $z^n$ oraz sumujemy po wszystkich $n$:

\begin{equation}

    F(z) = z F(z) + z^2 F(z) + z.

\end{equation}

Otrzymane równanie posiada dokładnie jedno rozwiązanie,

\begin{equation}

    F(z) = \frac{z}{1-z-z^2}.

\end{equation}

Pozostaje rozwinąć tę funkcję w szereg potęgowy i sprawdzić, jaki współczynnik stoi przy $z^n$.

Z kursu analizy wiemy, że każdą funkcję wymierną można rozłożyć na ułamki proste.

Pominiemy rachunki, mamy

\begin{equation}

    f_n = \frac{1}{\sqrt{5}} \left( \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right),

\end{equation}

czyli znany już wzór Bineta.

\index{wzór Bineta}%

\end{solution}

  

%