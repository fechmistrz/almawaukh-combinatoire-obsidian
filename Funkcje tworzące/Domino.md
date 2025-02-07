  

\begin{exercise}

    Na ile sposobów $T_n$ można rozciąć prostokąt rozmiaru $2 \times n$ na kamienie domina rozmiaru $2 \times 1$?

\end{exercise}

  

\begin{solution}

    ?

\end{solution}

  

\begin{exercise}

    Na ile sposobów $T_n$ można rozciąć prostokąt rozmiaru $3 \times n$ na kamienie domina rozmiaru $2 \times 1$?

\end{exercise}

  

\begin{solution}

    ?

\end{solution}

  

\begin{exercise}

    Iloczyn

    \begin{equation}

        2^{mn/2} \prod_{j=1}^{m} \prod_{k = 1}^n \left(\left(x\cos \frac{j \pi}{m+1}\right)^2 + \left(y \cos \frac{k \pi}{n+1}\right)^2 \right)^{1/4}

    \end{equation}

    jest funkcją tworzącą liczby podziałów prostokąta $m \times n$ kamieniami domina (współczynnik przy $x^j y^k$ jest liczbą spososbów podziału $j$ pionowymi oraz $k$ poziomymi kamieniami).

\end{exercise}

  

Graham, Knuth, Patashnik \cite[s. 420]{grahamknuthpatashnik2011} piszą \emph{,,to jest trudny problem, naprawdę wybiegający poza ramy tej książki. Może wystarczy, jeśli sprawdzisz to wyrażenie dla $m = 3, n = 4$''}.

  

\begin{solution}

    Dowód podali niezależnie Harold Temperley, Michael Fisher \cite{temperleyfisher1961} oraz Pieter Kasteleyn \cite{kasteleyn1961}.

\index[persons]{Temperley, Harold}%

\index[persons]{Fisher, Michael}%

\index[persons]{Kasteleyn, Pieter}%

\end{solution}

  

\begin{exercise}[cegły]

    Na ile sposobów można zbudować kolumnę rozmiaru $2 \times 2 \times n$ z cegieł rozmiaru $2 \times 1 \times 1$?

\end{exercise}

  

(To jest \cite[zadanie 24, s. 415]{grahamknuthpatashnik2011}).

  

\begin{solution}

    Niech $a_n$ będzie szukaną liczbą, $b_n$ liczbą sposobów zbudowania mniejszej kolumny, z wycięciem $2 \times 1 \times 1$ na górze.

    Otrzymujemy

    \begin{align}

        a_n & = 2a_{n-1} + 4b_{n-1} + a_{n-2} + [n=0] \\

        b_n & = a_{n-1} + b_{n-1},

    \end{align}

    zatem funkcje tworzące spełniają równania

    \begin{align}

        A & = 2zA + 4zB + z^2 A + 1 \\

        B & = zA + zB,

    \end{align}

    i mamy

    \begin{equation}

        A(z) = \frac{1-z}{(1+z)(1-4z+z^2)}.

    \end{equation}

    Początkowe wyrazy ciągu $a_n$ to 1 ($n = 0$), 2, 9, 32, 121, 450, 1\,681, 6\,272, 23\,409, 87\,362, 326\,041, ...  (\href{https://oeis.org/A006253}{A006253} w OEIS).

    Jak stwierdził Kaplansky \emph{,,niespodziewanie $a_{2n}$ jest równe kwadratowi liczby podziałów prostokąta $3 \times 2n$ kamieniami domina''}.

    % matematyka konkretna, s. 629

\end{solution}