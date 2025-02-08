
- https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
- https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind

%

  

\section{Liczby Stirlinga I i II rodzaju}

Liczby Stirlinga wprowadził James Stirling w \cite{stirling1753}, ale jak piszą Graham, Knuth, Patashnik nasza notacja pochodzi od Karamaty \cite{karamata1935}.

  

\begin{definition}[liczby Stirlinga II rodzaju]

    Symbol

    \begin{equation}

        \stirlingtwo{n}{k}

    \end{equation}

    oznacza liczbę sposobów podziału zbioru $n$ elementowego na $k$ niepustych podzbiorów.

\end{definition}

  

Mamy $\stirlingtwo{n}{n} = \stirlingtwo{n}{1} = 1$, nawet kiedy $n = 0$.

Z drugiej strony $\stirlingtwo{n}{0} = [n = 0]$, jak pisze Knuth ,,przypadek (...) wymaga nieco zręczności''.

Inne szczególne wartości to $\stirlingtwo{n}{2} = 2^{n-1}-1$ (pierwszy zbiór składa się z $n$ i dowolnych ale nie wszystkich liczb spośród $\{1, 2, ..., n-1\}$) oraz $\stirlingtwo{n}{n-1} = {n \choose 2}$ (jeden zbiór składa się z dwóch elementów, pozostałe są singletonami).

  

Charalambides \cite[s. 37]{charalambides2002} każe znaleźć (jako ćwiczenie) liczbę Stirlinga drugiego rodzaju.

Lovász \cite[s. 16]{lovasz1993} pyta, jaką rekurencję spełniają liczby Stirlinga I i II rodzaju, a następnie prosi o znalezienie ich dla $n \le 6$.

  

\begin{definition}[liczby Stirlinga I rodzaju]

    Symbol

    \begin{equation}

        \stirlingone{n}{k}

    \end{equation}

    oznacza liczbę sposobów podziału zbioru $n$ elementowego na $k$ niepustych cykli (,,naszyjników'').

\end{definition}

  

Istnieje jeden 1-cykl $[1]$, jeden 2-cykl $[1, 2] = [2, 1]$, ale dwa 3-cykle $[1, 2, 3] \neq [1, 3, 2]$.

Łatwo widać, że w ogólności mamy $(n-1)!$ różnych $n$-cykli; zatem $\stirlingone{n}{1} = (n-1)!$ dla $n > 0$, $\stirlingone{n}{n} = 1$ oraz $\stirlingone{n}{n-1} = {n \choose 2}$.

Mamy też $\stirlingone{n}{k} \ge \stirlingtwo{n}{k}$ dla całkowitych $n, k \ge 0$, bo z każdego zbioru można utworzyć co najmniej jeden cykl.

  

Ponieważ każdą permutację można rozłożyć jednoznacznie na cykle, mamy też

\begin{equation}

    \sum_{k=0}^n \stirlingone{n}{k} = n!.

\end{equation}

  

Jak nietrudno się domyślić, podobieństwa w definicjach liczb Stirlinga I i II rodzaju sprawiają, że ich własności także są podobne.

Prawdziwe są na przykład proste rekurencje

\begin{align}

    \stirlingtwo{n}{k} & = \stirlingtwo{n-1}{k-1} + k \stirlingtwo{n-1}{k}, \\

    \stirlingone{n}{k} & = \stirlingone{n-1}{k-1} + (n-1) \stirlingone{n-1}{k}

\end{align}

ponieważ element $n$ albo mieścimy w jednym z $k$ podzbiorów zbioru $\{1, 2, \ldots, n-1\}$, albo będzie jedynym elementem nowego zbioru.

  

Zachodzi

  

\begin{proposition}[przekształcanie potęg]

\begin{align}

x^n & = \sum_{k} \stirlingtwo{n}{k} x\fallingfactorial{k}

      = \sum_{k} \stirlingtwo{n}{k} (-1)^{n-k} x\raisingfactorial{k}, \\

x\fallingfactorial{n} & = \sum_{k} \stirlingone{n}{k} (-1)^{n-k} x^k, \\

x\raisingfactorial{n} & = \sum_{k} \stirlingone{n}{k} x^k.

\end{align}

\end{proposition}

  

o czym łatwo przekonać się indukcyjnie, patrz \cite[s. 294]{grahamknuthpatashnik2011}.

Pierwsza równość to ćwiczenie u Lovásza \cite[s. 16]{lovasz1993}.

  

\begin{proposition}[wzory inwersji]

\begin{align}

    \sum_k \stirlingtwo{n}{k}\stirlingone{k}{m}(-1)^{n-k} & = [m = n] \\

    \sum_k \stirlingone{n}{k}\stirlingtwo{k}{m}(-1)^{n-k} & = [m = n].

\end{align}

\end{proposition}

  

\subsection{Liczby Eulera}

Czasami pojawia się jeszcze jeden trójkąt wartości oznaczanych $\eulerone{n}{k}$: jest to liczba permutacji $\pi_1\pi_2\dots\pi_n$ zbioru $n$-elementowego, które mają $k$ wzniesień ($\pi_j < \pi_{j+1}$).

Spełniają zależność rekurencyjną:

\begin{equation}

    \eulerone{n}{k} = (k+1) \eulerone{n-1}{k} + (n-k) \eulerone{n-1}{k-1}

\end{equation}

dla całkowitych $n > 0$, z warunkami brzegowymi: $\eulerone{0}{k} = [k=0]$, $\eulerone{n}{k} = 0$ dla $k < 0$.

  

Liczby te mają być ciekawe, bo wiążą zwykłe potęgi ze współczynnikami dwumianowymi, jak orzeka

  

\begin{proposition}[tożsamość Worpitzky'ego]

    Dla całkowitych $n > 0$ zachodzi

    \begin{equation}

        x^n = \sum_k \eulerone{n}{k}{x+k \choose n}.

    \end{equation}

\end{proposition}

  

\begin{proof}

    Julius Worpitzky w \cite{worpitzky1883}.

\end{proof}

  

%

  

Charalambides, strona 277-

Wzór Schlomilcha