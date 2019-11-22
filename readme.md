Praktyka i Teoria Szeregowania Zadań
-------------------------------------

Michał Michalski Inf. Niest. 109679

*Problem PROBLEM P4 | rj | sum(Dj)*i


## Generator instancji

Sposób użycia: generator.py --n N --dmax DMAX --m M --pmax PMAX [--plot] [--help]

Argumenty:
  --help       wyświetla sposób użycia skryptu
  --n N        liczba zadań do wygenerowania
  --dmax DMAX  maksymalna wartość due date dla jednego zadania
  --m M        liczba maszyn w systemie
  --pmax PMAX  maksymalna długość jednego zadania
  --plot       graficzna prezentacja wygenerowanej instancji

Każde zadanie jest generowane losowo według następującej procedury:

    1. Losowana jest długość zadania pj z zakresu [1, PMAX].
    2. Losowany jest czas gotowości rj zadania z zakresu [0, DMAX - pj].
    3. DMAX := min(DMAX, (rj + pj) * 1.25)
    4. Losowany jest due time dj z zakresu [rj + pj, DMAX]

Powyższe kroki są powtórzone N razy, wygenerowane wartości pj, rj oraz dj
trafiają na standardowe wyjście programu.


## Algorytm listowy

Sposób użycia: schedule.py [--plot] [--help] [input]

Argumenty:
    --plot      Wyświetla wykres Gantta dla wygenerowanego uszeregowania.
    --help      Wyświetla sposób użycia skryptu.

Zaimplementowana została zachłanna heurystyka:

    1. Zaadnia sortowane są w kolejności niemalejących czasów gotowości.
    2. Z każdym procesorem (maszyną) związany zostaje wyzerowany licznik czasu.
    3. Zadania przydzielane są kolejno do najbliższego wolnego procesora.
    4. Obliczane jest summaryczne opóźnienie wszystkich zadań.

## Algorytm genetyczny

<something something bla bla>


## TODO

+ Implement crossover
+ Implement selection of pairs for crossovers
+ Implement mutations
+ Design automatic algorithm quality tests
+ Assign scheduling params after computing best genetic solution

