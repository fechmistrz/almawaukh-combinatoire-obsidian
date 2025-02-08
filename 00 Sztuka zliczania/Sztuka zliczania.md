Kombinatoryka to dziedzina matematyki, co się głównie liczeniem zajmuje – i to nie byle jakim, ale takim, co do skarbów wiedzy prowadzi! Tyczy się ona rozmaitych własności skończonych struktur, a przy tym splątana jest jak stary żeglarski węzeł z innymi gałęziami matematyki. Znajduje zastosowanie od morskiej logiki po sztuczki w fizyce statystycznej, od tajemnic ewolucji po czarnoksięskie machiny zwane komputerami! Arrr!

Stary grecki kronikarz **Plutarch** opowiada o kłótni między **Chryzypem** (III wiek przed naszym czasem) a **Hipparchem** (II wiek przed naszym czasem) o pewien wyjątkowo zawiły problem z liczeniem. Później okazało się, że sprawa ta miała związek z liczbami **Schrödera-Hipparcha**, co to wśród matematyków są równie tajemnicze, jak mapa do zaginionego skarbu! Arrr!
==Patrz: https://en.wikipedia.org/wiki/History_of_combinatorics#Earliest_records !==


https://en.wikipedia.org/wiki/Schröder–Hipparchus_number

==Earlier, in the _[Ostomachion](https://en.wikipedia.org/wiki/Ostomachion "Ostomachion")_, [Archimedes](https://en.wikipedia.org/wiki/Archimedes "Archimedes") (3rd century BCE) may have considered the number of configurations of a [tiling puzzle](https://en.wikipedia.org/wiki/Tiling_puzzle "Tiling puzzle"),[[10]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-10) while combinatorial interests possibly were present in lost works by [Apollonius](https://en.wikipedia.org/wiki/Apollonius_of_Perga "Apollonius of Perga").[[11]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-11)[[12]](https://en.wikipedia.org/wiki/Combinatorics#cite_note-12)==


## Reguła dodawania i mnożenia
Zaczniemy tak jak [[Aigner - A course in enumeration]] s. 5 od oczywistych stwierdzeń, które leżą u podstaw zliczania. Prawie każdy podręcznik kombinatoryczny zaczyna się od tego samego.
### Reguła dodawania
Reguła dodawania (\cite[s. 14-17]{charalambides2002}):

Jeżeli zbiór
$$
\begin{equation}
S = \bigcup_{k=1}^n S_k
\end{equation}
$$
jest sumą rozłącznych zbiorów $S_k$, to
$$
\begin{equation}
|S| = \sum_{k=1}^n |S_k|.
\end{equation}
$$
(Przez $|S|$ oznaczamy moc zbioru $S$, liczbę jego elementów.) Reguła dodawania służy do rozbijania być może trudnego problemu na prostsze przypadki, rozpatrzenie ich osobno i~dodanie do siebie wyników.
### Reguła mnożenia
Reguła mnożenia (\cite[s. 17-21]{charalambides2002})

Jeżeli zbiór
$$\begin{equation}
S = \prod_{k=1}^n S_k
\end{equation}
$$
jest iloczynem kartezjańskim zbiorów $S_k$, to
$$
\begin{equation}
|S| = \prod_{k=1}^n |S_k|.
\end{equation}
$$
Zbiór $S$ składa się z $n$-krotek uporządkowanych $(a_1, a_2, \ldots, a_n)$, gdzie $a_k \in S_k$.

> Skończony ciąg zer i jedynek nazywamy \emph{słowem} nad \emph{alfabetem} $\{0, 1\}$, a liczba jego elementów to \emph{długość} słowa. Ile jest słów długości $n$?

Mamy $S_1 = S_2 = \ldots = S_n = \{0, 1\}$ i szukamy mocy zbioru $S = \prod_{k=1}^n$. Reguła mnożenia mówi, że $|S| = 2^n$.

==Basic combinatorial concepts and enumerative results appeared throughout the [ancient world](https://en.wikipedia.org/wiki/Ancient_history "Ancient history"). [Indian](https://en.wikipedia.org/wiki/Timeline_of_Indian_history "Timeline of Indian history")[physician](https://en.wikipedia.org/wiki/Physician "Physician") [Sushruta](https://en.wikipedia.org/wiki/Sushruta "Sushruta") asserts in [Sushruta Samhita](https://en.wikipedia.org/wiki/Sushruta_Samhita "Sushruta Samhita") that 63 combinations can be made out of 6 different tastes, taken one at a time, two at a time, etc., thus computing all 26 − 1 possibilities.==

\cite[przykład 1.4]{charalambides2002}

### Reguła bijekcji
Reguła bijekcji (\cite[s. 14]{charalambides2002})

Niech $S, T$ będą zbiorami, zaś $f \colon S \to T$ bijekcją. Wtedy zbiory $S$ i $T$ są równoliczne: $|S| = |T|$.

Zazwyczaj korzystamy z tej reguły następująco: chcemy policzyć, ile elementów ma zbiór $S$. Zamiast robić to wprost, szukamy bijekcji $S \to T$ na inny zbiór $T$, którego moc znamy.

> Niech $X$ będzie skończonym zbiorem $n$-elementowym. Ile jest podzbiorów zbioru $X$?

Zbiór wszystkich podzbiorów zbioru $X$ oznaczać będziemy $\mathfrak P(X)$. Ponumerujmy jego elementy w dowolny sposób jako $x_1, x_2, \ldots, x_n$. Wtedy funkcja, która przypisuje podzbiorowi $A \subseteq X$ ciąg $(a_1, \ldots, a_n)$ taki, że $a_k = [x_k \in A]$, jest bijekcją na zbiór słów binarnych długości $n$. Zatem zbiór $X$ ma $2^n$ podzbiorów.

\cite[przykład 1.7]{charalambides2002}

Zapis $[x_k \in A]$ to przykład nawiasu Iversona: wartość tego wyrażenia wynosi $1$, jeśli zdanie wewnątrz nawiasów jest prawdziwe i $0$ w przeciwnym razie.

> Dane są rozłączne zbiory $S_1, S_2, \ldots, S_n$ takie, że $|S_k| = a_k$. Pokazać, że podzbiorów $X \subseteq \bigcup_{k=1}^n S_k$, które kroją zbiory $S_k$ co najwyżej jednopunktowo: $|X \cap S_k| \le 1$ jest $\prod_{k=1}^n (a_k + 1)$. Wywnioskować stąd, ile dzielników ma liczba całkowita, której rozkład na czynniki pierwsze jest znany.

(To jest \cite[ćwiczenie 1.1]{aigner2007}, \cite[przykład 1.5]{charalambides2002}).

Rekurencjami będziemy zajmować się bardziej w rozdziale \ref{chapter_rekurencje}.

> Niech  będzie -kątem wypukłym, zaś  liczbą par przekątnych , które przecinają się w jego wnętrzu. Mamy $f(4) = 1$ i $f(5) = 5$. Znaleźć rekurencję, którą spełnia $f(n)$ i rozwiązać ją.

(To jest \cite[ćwiczenie 1.6]{aigner2007}).

> Na ile sposobów możemy uporządkować liczby $1, 2, \ldots, n$ tak, że poza pierwszym wyrazem ciągu, każdy następny (nazwijmy go $k$) może się pojawić tylko wtedy, jeśli wśród poprzednich wystąpił już $k-1$ lub $k+1$?

(To jest \cite[ćwiczenie 1.7]{aigner2007}).

## Permutacje
\cite[s. 40-50]{charalambides2002}
==https://en.wikipedia.org/wiki/Permutation==


Do sprawdzenia:
- $k$-permutacja to uporządkowana krotka długości $k$, $(a_1, a_2, \ldots, a_k)$, taka że $a_k \in W$. (mogą być powtórzenia?). Jest ich n (n-1) ... (n-k+1)
- Permutacje z powtórzeniami; $n^k$
- \cite[s. 51-61]{charalambides2002}
- kombinacja: nieuporządkowane kolekcja $k$ elementów (z powtórzeniami lub nie)
- % ile można ułożyć słów o takich samych literach jak "Characterization"? lovasz1993 s. 16
- % podział kul do urn Charalambides 68; rozdział 9
- % że zawsze rozróżnialne
- % liczba rozwiązań równania liniowego Charalambides 68
- % k kul (nierozróżnialne), n ludzi (rozróżnialne) -> lovasz1993, s. 16
## Do zrobienia 
TODO: przybliżenie Stirlinga -- gdzieś tutaj?
funkcje (injekcje, surjekcje, bijekcje)
funkcji jakichkolwiek jest k^n -- \cite[s. 37]{charalambides2002}
Zliczanie funkcji (dowolnych \cite[s. 15]{lovasz1993}, injekcji, surjekcji, bijekcji).
