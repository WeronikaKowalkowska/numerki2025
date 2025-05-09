'''
Złożona kwadratura Newtona-Cotesa (wzór Simpsona):
-> na każdym małym przedziale funkcję aproksymujemy parabolą
-> Algorytm:
1. Dzielisz przedział [a,b] na parzystą liczbę podprzedziałów N o równej długości h.
2. Obliczasz wartości funkcji f(x) w punktach x0, x1, …, xN.
3. Podstawiasz je do wzoru:
    * pierwszy i ostatni punkt mają współczynnik 1,
    * punkty o nieparzystych indeksach: współczynnik 4,
    * punkty o parzystych indeksach wewnętrznych: współczynnik 2.
4. Mnożysz przez 1/3h i dodajesz błąd E.
Kwadratura Gaussa-Czebyszewa:
'''

from helper import *

funkcja_literka = None
funkcja_literka_flaga = True
while funkcja_literka_flaga:
    print("Wybierz funkcję:")
    print("a) f(x) = 4x^3 - 3x")
    print("b) f(x) = 1 / (1 + x^2)")
    print("c) f(x) = cos(x)")
    funkcja_literka = input("Wybrano: ").lower()
    if funkcja_literka == "a" or funkcja_literka == "b" or funkcja_literka == "c":
        funkcja_literka_flaga = False
    else:
        print("Wprowadź 'a', 'b' lub 'c'")
funkcja = wybor_funkcji(funkcja_literka)
metoda = None
metoda_flaga = True
while metoda_flaga:
    metoda = input(
        "Wybierz metodę całkowania numerycznego: a) złożona kwadratura Newtona-Cotesa (wzór Simpsona) b) kwadratura Gaussa z użyciem wielomianów Czebyszewa  ").lower()
    if metoda == "a" or metoda == "b":
        metoda_flaga = False
    else:
        print("Wprowadź 'a' lub 'b'")
if metoda == "a":
    epsilon = float(input("Podaj dokładność epsilon: "))
    a = -1
    b = 1
    wynik = None
    wynik_poprzedni = None
    liczba_przedzialow = None
    dokladnosc_flaga = True
    liczba_iteracji = 1
    while dokladnosc_flaga:
        liczba_przedzialow = 2  # musi być parzysta, zwiększana, żeby osiągnąć lepszą dokładność
        h = (b - a) / liczba_przedzialow  # długość jednego podprzedziału
        x = []
        for i in range(liczba_przedzialow + 1):  # generuje liczba_przedzialow + 1 punktów
            x.append(a + i * h)
        wynik = funkcja(x[0]) + funkcja(x[len(x) - 1])  # pierwszy i ostatni punkt
        for i in range(1, len(x) - 1):
            if i % 2 != 0:
                wynik += funkcja(x[i]) * 4
            else:
                wynik += funkcja(x[i]) * 2
        wynik = 1 / 3 * h * wynik
        if liczba_iteracji == 1:
            wynik_poprzedni = wynik
        if abs(wynik - wynik_poprzedni) < epsilon :
            dokladnosc_flaga = False
            liczba_iteracji = liczba_iteracji + 1
        else:
            liczba_przedzialow = liczba_przedzialow * 2
            wynik_poprzedni = wynik
            liczba_iteracji = liczba_iteracji + 1

    print("Wynik całki:", wynik, "z", liczba_przedzialow, "podprzedziałami.")

if metoda == "b":
    wezly = [2, 3, 4, 5]
