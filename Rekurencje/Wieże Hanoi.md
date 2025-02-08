Dane są trzy paliki i $n$ krążków o różnych średnicach. Na początku wszystkie krążki są nałożone na pierwszym paliku w kolejności malejących średnic. Zadanie polega na przeniesieniu wszystkich krążków z pierwszego palika na trzeci zgodnie z regułami:
- w każdym kroku wolno zdjąć z palika szczytowy krążek i nałożyć go na inny palik,
- krążek o~średnicy większej nie może być nałożony na krążek o średnicy mniejszej.

Łamigłówkę wymyślił w 1883 roku Édouard Lucas, matematyk francuski.

Sekcja powstała na podstawie podręcznika Grahama, Knutha, Patashnika \cite[s. XXX-XXX]{grahamknuthpatashnik2011} oraz ciągu \href{https://oeis.org/A007664}{A007664} w OEIS.

Niech $h_n$ oznacza minimalną liczbę kroków do przełożenia całej wieży. Mamy zależność rekurencyjną $h_{n+1} = 2h_n + 1$ dla $n \ge 0$ z warunkiem początkowym $h_1 = 1$, ponieważ możemy wyobrazić sobie, że najpierw przenosimy górne $n-1$ krążków, potem przekładamy najszerszy krążek, po czym znowy przenosimy $n-1$ krążków. Można zgadnąć, że $h_n = 2^n - 1$ i udowodnić indukcyjnie ten wzór.

Można też wprowadzić pomocniczy ciąg $h'_n = h_n + 1$ i zauważyć, że spełnia on rekurencję $h'_{n+1} = 2h'_n$, $h'_1 = 2$. Łatwo widać, że rozwiązaniem tej rekurencji jest $h'_n = 2^n$.

Jeżeli zaczniemy wymagać, by każdy ruch dotyczył środkowego pręta, to potrzeba $3^n - 1$ ruchów [GKP, s. 33][[Graham, Knuth, Patashnik]].
s. 33 ma podobną treść, co https://en.wikipedia.org/wiki/Tower_of_Hanoi#Adjacent_pegs

Więcej kłopotu sprawia ograniczenie, by każdy ruch wykonywać zgodnie ze wskazówkami zegara -- wtedy wieżę $n$ krążków można przenieść w co najmniej
$$
\frac{(1+\sqrt{3})^{n+1} - (1-\sqrt{3})^{n+1}}{2 \sqrt{3}} - 1
$$
ruchach [GKP, s. 34][[Graham, Knuth, Patashnik]].

W jeszcze innej wersji zagadki mamy podwójną wieżę złożoną z $2n$ krążków $n$ różnych rozmiarów, po dwa krążki każdego rozmiaru. Jeżeli krążki są nieodróżnialne, wystarczają $2^{n+1} - 2$ ruchy, ale jeżeli wymagamy odtworzenia oryginalnego ułożenia, potrzeba $2^{n+2} - 5$ przełożeń.

## Bezużyteczna ciekawostka
Jeżeli początkowe oraz końcowe ustawienie krążków zostało wybrane losowo, to potrzeba średnio
$$
    \frac{466}{885} \cdot 2^n - \frac 1 3 - \frac 1 {5 \cdot 3^{n-1}} + \frac{204 + 18\sqrt{17}}{1003} \left({\frac {5+{\sqrt {17}}}{18}}\right)^{n} + \frac{204 - 18\sqrt{17}}{1003} \left({\frac {5-{\sqrt {17}}}{18}}\right)^{n}
$$
ruchów, żeby dokonać pełnego przełożenia. Wzór znaleźli niezależnie Tat-Hung Chan \cite{chan1988} oraz Andreas Hinz \cite{hinz1989}.
## Uogólnione wieże Hanoi: zagadka Revego
Henry Dudeney zapytał w listopadzie 1896 roku, ile ruchów jest potrzebnych do przeniesienia dziesięciu krążków, kiedy mamy do dyspozycji cztery zamiast trzech palików [[Henry Dudeney - Sphinx Junior's Latest]]. Dwa tygodnie później podał odpowiedź: potrzeba 49 ruchów, ale ze względu na brak miejsca nie podał uzasadnienia, dlaczego właśnie tyle. Zadanie pojawiło się jeszcze raz w lekko zmienionej formie jako {zagadka Revego}  \cite{dudeney1902} i długo czekało na pełne rozwiązanie.

Dalej referujemy artykuł Andreasa Hinza i Cirila Petra \cite{hinzpetr2016}. Zaczęło się od algorytmu podanego niezależnie w 1941 roku przez Bonniego Stewarta oraz Jamesa Frame'a \cite{stewartframe1941}: aby przenieść $n$ krążków należy najpierw przełożyć $k$ najmniejszych na drugi palik, przełożyć pozostałe $n-k$ krążków na końcowy palik nie korzystając z drugiego, wreszcie przełożyć najmniejsze krążki na końcowy palik (dla dobrze wybranego $1 \le k < n$). Mamy
$$
    r_n = \min \{2 r_k + 2^{n-k} : k < n\} - 1.
$$

Wzór ten mówiłby, że potrzeba $1, 3, 5, 9, 13, 17, 25, 33, 41, 49, \ldots$ ruchów by przełożyć $1, 2, 3, \ldots$ krążki. Niestety nikt nie uzasadnił, dlaczego ich algorytm daje optymalne rozwiązanie, co zauważył już redaktor magazynu, w którym opublikowano ich prace. Jens Bode, Andreas Hinz \cite{bodehinz1999} sprawdzili komputerowo, że tak jest co najmniej do 17 krążków. Wyniki rozszerzył Richard Korf \cite{korf2004} i dopiero dziesięć lat po jego pracy Thierry Bousch \cite{bousch2014} podał dowód poprawności algorytmu Stewarta-Frame'a dla 4 palików. Dudeney zapytał też, ile ruchów potrzeba do przeniesienia 20 (lub w ambitnej wersji, 35) krążków na 5 palikach. Odpowiedzi udzielili Hinz, Petr \cite{hinzpetr2016}: 20 krążków wymaga 111 ruchów, natomiast 35 krążków to za dużo dla superkomputera, jakim dysponowali.

% TODO: https://oeis.org/A024023 Amir Sapir, The Tower of Hanoi with Forbidden Moves, The Computer J. 47 (1) (2004) 20, case three-in-a row, sequence b(n)
% TODO: Uri Levy, The Magnetic Tower of Hanoi, Journal of Recreational Mathematics, Volume 35 Number 3 (2006),  2010, pp 173; arXiv:1003.0225 [math.CO], 2010.
% TODO: https://oeis.org/A005666 Tower of Hanoi with 3 pegs and cyclic moves only (counterclockwise).
% TODO: https://hasinarefinkhan.blogspot.com/2015/02/concrete-mathematics-exercise-solution.html