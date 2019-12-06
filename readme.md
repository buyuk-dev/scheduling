Praktyka i Teoria Szeregowania Zadań
-------------------------------------

Michał Michalski Inf. Niest. 109679

*Problem PROBLEM P4 | rj | sum(Dj)*i


# Generator instancji

Zadaniem generatora instancji jest utworzenie losowego zbioru zadań.  Dobry
generator powinien unikać generowania trywialnych instancji, czyli takich, dla
których algorytmy listowe są w stanie wygenerować idealne (lub prawie idealne)
uszeregowania.

W mojej implementacji, generator posiada 3 parametry pozwalające sterować
generacją instancji. Są to liczba zadań N, liczba procesorów M oraz maksymalna
długość pojedynczego zadania Pmax

Opisy poszczególnych zadań obliczane są niezależnie od siebie według
następujących wzorów:

    p(i) = randint(0.25 * Pmax, Pmax)
    r(i) = randint(0, 0.5 * Pmax)
    d(i) = randint(r(i) + p(i), r(i) + 1.5 * p(i))

Czas trwania zadania został ograniczony od dołu przez 1/4 maksymalnej długości,
aby uniknąć zbyt krótkich zadań, które potencjalnie można by umieścić w
dowolnej 'przerwie' w uszeregowaniu, czyniąc instancje zbyt prostymi.

Aby uniknąć nadmiernego rozrzucenia zadań i niepotrzebnie dużych przestoi, co
mogłoby prowadzić do nadmiernej 'liniowości' uszeregowania i niewielkiego pola
do manewrów dla algorytmów szeregujących, czasy gotowości zadań zostały
wylosowane w taki sposób aby w większości przypadków okna czasowe
poszczególnych zadań na siebie nachodziły.

Linia krytyczna zadania musi w idealnym przypadku umożliwiać wykonanie zadania
bez opóźnień, stąd dolne ograniczenie przy jej losowaniu wynosi r(i) + p(i).
Jako górną granicę w drodze eksperymentów obrałem 1.5 * p(i). Taki margines
zostawiał wystarczającą swobodę w manewrowaniu zadaniami aby algorytmy
przeszukujące przestrzeń stanów miały co przeszukiwać, ale jednocześnie
algorytmy listowe miały trudności ze znalezieniem uszeregowań o małym
opóźnieniu.

Obsługa generatora:

    generator.py [-h] [--n N] [--m M] [--pmax PMAX] [--plot]

    optional arguments:
      -h, --help   show this help message and exit
      --n N        number of tasks
      --m M        processors number
      --pmax PMAX  max task length
      --plot       plot generated tasks

Przykładowy wynik:

    ./generator.py --n 20 --m 4 --pmax 50 --plot
    20
    13 17 32
    10 19 35
    14 20 36
    10 38 59
    25 26 54
    9 18 34
    3 42 45
    17 48 75
    8 46 56
    11 14 31
    3 38 58
    8 24 44
    15 29 55
    17 35 67
    19 18 40
    0 42 57
    11 39 65
    0 19 28
    10 14 24
    14 25 39


# Weryfikator rozwiązań

Zadaniem weryfikatora jest obliczenie całkowitego kosztu podanego uszeregowania
danej instancji (zbioru zadań). Uszeregowanie podane jest w formie 4 wierszy, w
każdym z nich są podane numery zadań kolejno wykonywanych na odpowiadającej im
maszynie.

Całkowity koszt w przypadku rozwiązywanego problemu jest sumą opóźnień
poszczególnych zadań względem ich linii krytycznych. Dla danej maszyny oraz
przypisanej jej sekwencji zadań można obliczyć dokładny czas rozpoczęcia
realizacji każdego z zadań jako s(i) = max(T[m], r(i)), gdzie T[m] jest czasem
na zegarze maszyny #m (czyli czasem zakończenia poprzedniego zadania na tej
maszynie). Czas rozpoczęcia jednoznacznie definiuje nam czas zakończenia jako
e(i) = s(i) + p(i). Wówczas opóźnienie dane jest wzorem: D(i) = max(0, d(i) -
e(i)).  Zatem opóźnienia zadań dla maszyny m można obliczyć według poniższego
algorytmu:

    e[0] = 0
    total_delay = 0
    for i = 1..n do:
        s[i] = max(e[i-1], r[i])
        e[i] = s[i] + p[i]
        total_delay += max(0, d[i] - s[i])

Obsługa weryfikatora:

    plotter.py [-h] [--instance INSTANCE] [--scheduling SCHEDULING]

    optional arguments:
      -h, --help               show this help message and exit
      --instance INSTANCE      instance filename
      --scheduling SCHEDULING  scheduling filename



