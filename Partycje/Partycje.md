Partycją albo podziałem (dodatniej) liczby naturalnej $n$ nazywamy kolekcję (dodatnich) liczb naturalnych, których suma wynosi $n$. Liczbę wszystkich partycji oznaczamy $p(n)$, na przykład $p(4) = 5$, ponieważ
$$
\begin{align}
	4 & = 3 + 1 \\
	& = 2 + 2 \\
	& = 2 + 1 + 1 \\
	& = 1 + 1 + 1 + 1
\end{align}
$$
Pionierem w badaniu podziałów liczb był Euler, który udowodnił w 1748 nieoczywiste:

> Liczba podziałów liczby $r$ na różne składniki jest taka sama, jak liczba podziałów liczby $r$ na nieparzyste składniki.

(To są też ćwiczenia 18, 21 u [[Lovász - Combinatorial problems and exercises]]a s. 18). Pierwsze godne uogólnienie zawdzięczamy [[Glaisher - A theorem in partitions]]owi sto lat później:

> Niech $k, n$ będą liczbami naturalnymi. Wtedy liczba podziałów $n$ takich, że każdy składnik pojawia się co najwyżej $k$ razy jest równa liczbie podziałów $n$ takich, że żaden składnik nie dzieli się przez $k + 1$.

Zaintrygowani Czytelnicy powinni sięgnąć po pracę [[Alder - The use of generating functions to discover and prove partition identities]]a, która niezwykle wyczerpująco przedstawia różne wyniki podobne do tego, który uzyskał Euler.

Ciąg liczb $p(n)$ jak każdy inny posiada funkcję tworzącą:
$$
\begin{align}
\sum_{k=0}^\infty p(k) x^k & = \prod_{k=1}^\infty \frac{1}{1-x^k} \\
& = \sum_{k=0}^\infty x^k \prod_{i = 1}^k \frac{1}{1-x^i}\\
& = 1 + \sum_{k=1}^\infty \frac{x^{k^2}}{\prod_{i=1}^k (1-x^i)^2},
\end{align}
$$
którą przepisaliśmy z ciągu https://oeis.org/A000041 w bazie danych OEIS, a znalezienie której stanowi ćwiczenie 20 u [[Lovász - Combinatorial problems and exercises]]a s. 18. Niech $a_r$ oznacza liczbę partycji liczby $r$ na składniki $1, 2$ lub $3$. Wtedy funkcją tworzącą dla $a_r$ jest
$$
(1 + x + x^2 + \ldots)(1 + x^2 + x^4 + \ldots)(1 + x^3 + x^6 + \ldots) = \frac{1}{(1-x)(1-x^2)(1-x^3)}
$$
Jeżeli nie dopuszczamy powtórzeń, funkcja tworząca to $(1+x)(1+x^2)(1+x^3)$. 

## Diagramy Ferrera.
TODO: Diagramy Ferrera.
## Do zrobienia
TODO: Charalambides - rozdział 10, 11
TODO: https://en.wikipedia.org/wiki/Faà_di_Bruno%27s_formula ???