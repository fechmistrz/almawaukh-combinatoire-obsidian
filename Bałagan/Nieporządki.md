  

\begin{exercise}[nieporządki]

    Ile jest permutacji zbioru $n$-elementowego bez punktów stałych, czyli takich $x$, że $f(x) = x$?

    Takie permutacje nazywamy nieporządkami.

\end{exercise}

  

Nieporządki były rozpatrywane po raz pierwszy przez Pierre'a Remonda \cite{demontmort1708} (który był pierwszą osobą, która nazwała trójkąt Pascala trójkątem Pascala).

Liczbę nieporządków nazywa się czasem słabnią albo podsilnią, jest ich 1 ($n = 0$), 0, 1, 2, 9, 44, 265, 1\,854, 14\,833, 133\,496, 1\,334\,961, ...  (\href{https://oeis.org/A000166}{A000166} w OEIS).

Wzór na liczbę nieporządków znaleźli około 1713 roku Pierre de Montmort oraz Nicholas Bernoulli.

% The problem of counting derangements was first considered by Pierre Raymond de Montmort in his Essay d'analyse sur les jeux de hazard.[4] in 1708; he solved it in 1713, as did Nicholas Bernoulli at about the same time.

  

\begin{solution}

    Rozwiązanie takie jak u Grahama, Knutha, Patashnika \cite[s. 223-225]{grahamknuthpatashnik2011}: dla $1 \le k \le n$ niech $S_k$ oznacza zbiór permutacji takich, że $f(k) = k$.

    Przekrój dowolnej rodziny $i$ zbiorów $S_k$ posiada $i$ punktów stałych, więc posiada $(n-i)!$ elementów.

    Takich rodzin jest dokładnie ${n \choose i}$, zatem z~zasady włączeń i~wyłączeń:

    % https://tex.stackexchange.com/questions/51682/is-it-possible-to-pagebreak-aligned-equations

    {\allowdisplaybreaks

    \begin{align}

        \left|\bigcup_{k=1}^n S_k\right| & = \sum_{k_1} |S_{k_1}| - \sum_{k_1 < k_2} |S_{k_1} \cap S_{k_2}| + \ldots + (-1)^{n+1} \left|\bigcap_{k=1}^n S_k\right| \\

                                        & = {n \choose 1} (n-1)! - {n \choose 2} (n-2)! + \ldots + (-1)^{n+1} {n \choose n} 0! \\

                                        & = \sum_{k=1}^n (-1)^{k+1} {n \choose k} (n-i)! \\

                                        & = n! \sum_{k=1}^n \frac{(-1)^{k+1}}{k!}.

    \end{align}

    }

    Zatem wszystkich nieporządków jest

    \begin{equation}

    \label{eqn:derangement}%

    !n = n! \sum_{k=0}^n \frac{(-1)^k}{k!} = \left \lfloor \frac{n! + 1}{e} \right \rfloor.

    \qedhere

    \end{equation}

\end{solution}

  

\begin{exercise}[nieporządki]

    Ile jest permutacji zbioru $n$-elementowego bez punktów stałych, czyli takich $x$, że $f(x) = x$?

\end{exercise}

  

\begin{solution}

    To jest inne rozwiązanie tego samego problemu.

    Rekurencję

    \begin{equation}

        n! = \sum_k {n \choose k} !(n-k)

    \end{equation}

    zapiszmy w postaci

    \begin{equation}

        1 = \sum_{k=0}^n \frac{1}{k!} \frac{!(n-k)}{(n-k)!},

    \end{equation}

    co po przejściu do funkcji tworzących daje

    \begin{equation}

        \frac{1}{1-z} = e^z D(z).

    \end{equation}

    Porównując współczynniki przy $z^n$ po obydwu stronach równości $D(z) = e^{-z} / (1-z)$ dostajemy znowu równanie \ref{eqn:derangement}.

\end{solution}

  

\begin{exercise}

    Ile jest permutacji alternujących, czyli permutacji $f$ zbioru $\{1, 2, \ldots, n\}$ takich, że $f(1) < f(2) > f(3) < f(4) > \ldots$?

\end{exercise}

  

Pierwsza wersja tego akapitu powstała na podstawie \cite[s. 418, 631-632]{grahamknuthpatashnik2011}, gdzie permutacje te określa się terminem ,,rosnąco-malejące''.

Później dowiedzieliśmy się, że Désiré André badał takie permutacje około 1881 roku \cite{desire1881} i dlatego powyższy problem to problem André.

\index[persons]{André, Désiré}%

\index{problem André}%

  

\begin{solution}

    Oznaczmy przez $a_n$ szukaną liczbę permutacji.

    Ciąg $a_n$ zaczyna się od 1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521, 353792, ... (\href{https://oeis.org/A000111}{A000111} w OEIS).

    Permutacji rosnąco-malejących z~największym elementem $n$ na pozycji $2k$ jest

    \begin{equation}

        {n-1 \choose 2k-1} a_{2k-1} a_{n-2k}.

    \end{equation}

    Ponieważ permutacji rosnąco-malejących jest tyle samo, co permutacji malejąco-rosnących, to szukanych permutacji z najmniejszym elementem $1$ na pozycji $2k+1$ jest

    \begin{equation}

        {n-1 \choose 2k} a_{2k} a_{n-2k-1}.

    \end{equation}

    Sumując po wszystkich możliwościach mamy

    \begin{equation}

        2A_n = \sum_k {n-1 \choose k} A_k A_{n-1-k} + 2[n=0] + [n=1].

    \end{equation}

    Wykładnicza funkcja tworząca $A$ dla ciągu $(a_n)$ spełnia zależność $2A'(z) = A(z)^2 + 1$, mamy też warunek brzegowy $A(0) = 1$, dlatego odpowiedź brzmi

    \begin{equation}

        A(z) = \frac{1 + \sin z}{\cos z} = \tan z + \sec z.

    \end{equation}

\end{solution}

  

%