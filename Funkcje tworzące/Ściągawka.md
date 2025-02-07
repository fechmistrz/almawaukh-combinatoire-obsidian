%

  

\subsection{Proste ciągi i ich funkcje tworzące}

Poniższa lista powstała na podstawie \cite[s. 372]{grahamknuthpatashnik2011}.

% https://tex.stackexchange.com/questions/51682/is-it-possible-to-pagebreak-aligned-equations

{\allowdisplaybreaks
$$
\begin{alignat}{2}

% matematyka konkretna, 372/2

z^m & = \sum_{n=0}^\infty [n=m] z^n & & = z^m \\

% matematyka konkretna, 372/3

\frac{1}{1-z} & = \sum_{n=0}^\infty z^n & & = 1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + z^7 + \ldots \\

% matematyka konkretna, 372/4

\frac{1}{1+z} & = \sum_{n=0}^\infty (-1)^n z^n & & = 1 - z + z^2 - z^3 + z^4 - z^5 + z^6 - z^7 + \ldots \\

% matematyka konkretna, 372/12

\frac{1}{1-\lambda z} & = \sum_{n=0}^\infty \lambda^n z^n & & = 1 + \lambda z + \lambda^2 z^2 + \lambda^3 z^3 + \lambda^4 z^4 + \lambda^5 z^5 + \ldots \\

% matematyka konkretna, 372/6

\frac{1}{1-z^m} & = \sum_{n=0}^\infty [m \mid n] z^n & & = 1 + z^m + z^{2m} + z^{3m} + z^{4m} + z^{5m} + \ldots \\

% matematyka konkretna, 372/10

(1+z)^m & = \sum_{n=0}^\infty {m \choose n} z^n & & = 1 + {m \choose 1} z + {m \choose 2} z^2 + {m \choose 3} z^3 + \ldots \\

% matematyka konkretna, 372/13

\frac{1}{(1-z)^{m+1}} & = \sum_{n=0}^\infty {m+n \choose n} z^n & & = 1 + {m + 1 \choose 1} z + {m + 2 \choose 2} z^2 + \ldots \\

% matematyka konkretna, 372/14

\log \frac{1}{1-z} & = \sum_{n=1}^\infty \frac{1}{n} z^n & & = z + \frac{1}{2} z^2 + \frac{1}{3} z^3 + \frac{1}{4}z^4 + \frac{1}{5}z^5 + \frac{1}{6} z^6 + \ldots \\

% matematyka konkretna, 372/15

\log(1 + z) & = \sum_{n = 1}^\infty \frac{(-1)^{n+1}}n z^n & & = z - \frac{1}{2} z^2 + \frac{1}{3} z^3 - \frac{1}{4} z^4 + \frac{1}{5} z^5 - \frac{1}{6} z^6 - \ldots \\

% matematyka konkretna, 372/16

e^z & = \sum_{n = 0}^\infty \frac{1}{n!} z^n & & = 1 + z + \frac{1}{2}z^2 + \frac{1}{6}z^3 + \frac{1}{24}z^4 + \frac{1}{120}z^5 + \ldots

\end{alignat}
$$
}

  

Mnożenie ma kilka szczególnych (i interesujących przypadków). Na przykład mnożenie funkcji tworzącej przez $1/(1-z)$ daje funkcję tworzącą dla sum częściowych wyjściowego ciągu:
$$
\begin{equation}
\frac{1}{1-z} \cdot A(z) = \sum_{n = 0}^\infty \left(\sum_{k=0}^n a_k \right) z^n.
\end{equation}
$$
Z taką wiedzą możemy jeszcze raz zmierzyć się z ćwiczeniem \ref{ex:sum_of_squares} (jak Wilf \cite[s. 37]{wilf1994}):

  

\begin{exercise}

    Znaleźć wzór na sumą kwadratów pierwszych $N$ liczb naturalnych, $1^2 + 2^2 + \ldots + N^2$.

\end{exercise}

  

\begin{solution}

    Ft ciągu $1, 1, 1, \ldots$ jest $1/(1-x)$, więc ft ciągu $n^2$ to dokładnie

    \begin{equation}

        \left(x \frac{\mathrm{d}}{\mathrm{d}x} \right)^2 \frac{1}{1-x},

    \end{equation}

    z czego skorzystamy szukając ft ciągu sum częściowych ciągu $n^2$.

    Mamy

    \begin{equation}

        \frac{1}{1-x}\left(x \frac{\mathrm{d}}{\mathrm{d}x} \right)^2 \frac{1}{1-x} = \frac{x(1+x)}{(1-x)^4},

    \end{equation}

    współczynnik przy $x^N$ będzie sumą pierwszych $N$ kwadratów liczb naturalnych.

    Ale my już wiemy, że

    \begin{equation}

        [x^n] \frac{1}{(1-x)^4} = {n+3 \choose 3},

    \end{equation}

    więc szukana suma to

    \begin{equation}

        {N+2 \choose 3} + {N+1 \choose 3} = \frac{1}{6} N \cdot (N+1) \cdot (2N+1).

    \end{equation}

\end{solution}

  

\begin{exercise}

    Znaleźć wzór ft ciągu liczb harmonicznych $H_n = 1 + 1/2 + 1/3 + \ldots + 1/n$.

\end{exercise}

  

(Ćwiczenie ukradzione Wilfowi \cite[s. 38]{wilf1994})

  

\begin{solution}

    Liczby harmoniczne są ciągiem sum częściowych ciągu $a_n = 1/n$.

    Pochodna ft tego ciągu to $\sum_{n=0}^\infty x^n = 1/(1-x)$, więc

    \begin{align}

        \sum_{n=1}^\infty H_n x^n = \frac{1}{1-x} \int \frac{\mathrm{d}x}{1-x} = \frac{1}{1-x} \log \frac{1}{1-x}.

    \end{align}

\end{solution}

  

\begin{exercise}

    Niech $f_n$ oznacza ciąg Fibonacciego.

    Pokazać, że $f_0 + f_1 + \ldots + f_n = f_{n+2} - 1$.

\end{exercise}

  

Poniższa lista powstała na podstawie \cite[s. 390]{grahamknuthpatashnik2011}.

% https://tex.stackexchange.com/questions/51682/is-it-possible-to-pagebreak-aligned-equations

{\allowdisplaybreaks

\begin{align}

% matematyka konkretna, 7.43

\frac{1}{(1-z)^{m+1}} \log \frac{1}{1-z} & = \sum_{n=0}^\infty (H_{m+n} - H_m) {m + n \choose n} \cdot z^n \\

% matematyka konkretna, 7.44

\frac{z}{e^z - 1} & = \sum_{n=0}^\infty {B_n} \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.45

\frac{F_m z}{1-(F_{m-1} + F_{m+1})z + (-1)^m z^2)} & = \sum_{n=0}^\infty F_{mn} \cdot z^n \\

% matematyka konkretna, 7.46

\sum_{k} \stirlingtwo{m}{k} \frac{k! z^k}{(1-z)^{k+1}} & = \sum_{n=0}^\infty n^m \cdot z^n \\

% matematyka konkretna, 7.47

(1/z)\raisingfactorial{-m} & = \sum_{n=0}^\infty \stirlingtwo{n}{m} \cdot z^n \\

% matematyka konkretna, 7.48

z\raisingfactorial{m} & = \sum_{n=0}^\infty \stirlingone{m}{n} \cdot z^n \\

% matematyka konkretna, 7.49

(e^z-1)^m & = m! \sum_{n=0}^\infty \stirlingtwo{n}{m} \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.50

\left(\log \frac{1}{1-z}\right)^m & = m! \sum_{n=0}^\infty \stirlingone{n}{m} \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.51

\left(\frac{z}{\log (1+z)}\right)^m & = \sum_{n=0}^\infty \frac{\stirlingtwo{m}{m-n}}{ {m-1 \choose n} } \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.52

\left(\frac{z}{1-e^{-z}}\right)^m & = \sum_{n=0}^\infty \frac{\stirlingone{m}{m-n}}{ {m-1 \choose n} } \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.53

\exp (z + wz) & = \sum_{m=0}^\infty \sum_{n=0}^\infty {n \choose m} w^m \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.54

\exp (w(e^z - 1)) & = \sum_{m=0}^\infty \sum_{n=0}^\infty \stirlingtwo{n}{m} w^m \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.55

\frac{1}{(1-z)^w} & = \sum_{m=0}^\infty \sum_{n=0}^\infty \stirlingone{n}{m} w^m \cdot \frac{z^n}{n!} \\

% matematyka konkretna, 7.56

\frac{1-w}{\exp(wz-z) - w} & = \sum_{m=0}^\infty \sum_{n=0}^\infty \eulerone{n}{m} w^m \cdot \frac{z^n}{n!}

\end{align}

}

  

%