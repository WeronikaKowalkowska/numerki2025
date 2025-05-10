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
'''
wagi i współrzędne  - z pliku na Wikampie
n = 2
  1.5707963267948966192  -0.7071067811865475244
  1.5707963267948966192   0.7071067811865475244

n = 3
  1.0471975511965977462  -0.8660254037844386468
  1.0471975511965977462   0.0000000000000000000
  1.0471975511965977462   0.8660254037844386468

n = 4
  0.7853981633974483096  -0.9238795325112867561
  0.7853981633974483096  -0.3826834323650897717
  0.7853981633974483096   0.3826834323650897717
  0.7853981633974483096   0.9238795325112867561

n = 5
  0.6283185307179586477  -0.9510565162951535721
  0.6283185307179586477  -0.5877852522924731292
  0.6283185307179586477   0.0000000000000000000
  0.6283185307179586477   0.5877852522924731292
  0.6283185307179586477   0.9510565162951535721
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
        print("Wprowadź 'a', 'b' lub 'c'.")
funkcja = wybor_funkcji(funkcja_literka)
metoda = None
metoda_flaga = True
while metoda_flaga:
    metoda = input(
        "Wybierz metodę całkowania numerycznego: a) złożona kwadratura Newtona-Cotesa (wzór Simpsona) b) kwadratura Gaussa z użyciem wielomianów Czebyszewa  ").lower()
    if metoda == "a" or metoda == "b":
        metoda_flaga = False
    else:
        print("Wprowadź 'a' lub 'b'.")
if metoda == "a":
    epsilon_flaga = True
    epsilon = None
    while epsilon_flaga:
        epsilon = float(input("Podaj dokładność epsilon: "))
        if epsilon > 0:
            epsilon_flaga = False
        else:
            print("Wartość epsilon nia może być ujemna.")

    a = -1
    b = 1
    wynik = 0
    wynik_poprzedni = None
    liczba_przedzialow = 2  # musi być parzysta, zwiększana, żeby osiągnąć lepszą dokładność
    dokladnosc_flaga = True

    if czy_wlasciwa(funkcja_literka):

        while dokladnosc_flaga:

            wynik = simpson(funkcja, a, b, liczba_przedzialow)

            if wynik_poprzedni is not None and abs(wynik - wynik_poprzedni) < epsilon:
                dokladnosc_flaga = False
            else:
                liczba_przedzialow *= 2
                wynik_poprzedni = wynik
    else:

        liczba_przedzialow = 4
        wynik = 0
        krok = 0.5
        srodek_przedzalu = 0
        wynik_poprzedni = None
        nie_wlasciwa_flaga = True

        # część dodatnia (od 0 do 1)
        while nie_wlasciwa_flaga:

            # nowy podprzedział, na którym chcemy obliczyć kolejną „cząstkową” całkę
            a = srodek_przedzalu
            b = srodek_przedzalu + krok

            # sprawdzenie, czy granicy całkowania nie zostały przekroczone
            a = max(a, 0)
            b = min(b, 1)

            wynik_czastkowy = simpson(funkcja, a, b, liczba_przedzialow)

            if wynik_poprzedni is not None and abs(wynik - wynik_poprzedni) < epsilon:
                nie_wlasciwa_flaga = False

            wynik += wynik_czastkowy
            wynik_poprzedni = wynik
            srodek_przedzalu = b
            krok = krok / 2


        krok = 0.5
        srodek_przedzalu = 0
        wynik_poprzedni = None
        nie_wlasciwa_flaga = True

        # część ujemna (od -1 do 0)
        while nie_wlasciwa_flaga:

            # nowy podprzedział, na którym chcemy obliczyć kolejną „cząstkową” całkę
            a = srodek_przedzalu - krok
            b = srodek_przedzalu

            # sprawdzenie, czy granicy całkowania nie zostały przekroczone
            a = max(a, -1)
            b = min(b, 0)

            wynik_czastkowy = simpson(funkcja, a, b, liczba_przedzialow)

            if wynik_poprzedni is not None and abs(wynik - wynik_poprzedni) < epsilon:
                nie_wlasciwa_flaga = False

            wynik += wynik_czastkowy
            wynik_poprzedni = wynik
            srodek_przedzalu = a
            krok = krok / 2

    print("-------Złożona kwadratura Newtona-Cotesa (wzór Simpsona)-------")
    print("Wynik całki:", wynik, "z", liczba_przedzialow, "podprzedziałami.")

# !!!!! dla b i c dziwne wyniki daje !!!!!!
if metoda == "b":
    n = None
    n_flaga = True
    wspolrzedne = []
    wspolczynniki = [1.5707963267948966192, 1.0471975511965977462, 0.7853981633974483096, 0.6283185307179586477]
    while n_flaga:
        try:
            n = int(input("Podaj liczbę węzłów (2, 3, 4 lub 5): "))
            if n in (2, 3, 4, 5):
                n_flaga = False
            else:
                print("Wprowadź '2', '3', '4' lub '5'.")
        except ValueError:
            print("Wprowadź liczbę całkowitą.")

    if n == 2:
        wspolrzedne.append(-0.7071067811865475244)
        wspolrzedne.append(0.7071067811865475244)
    elif n == 3:
        wspolrzedne.append(-0.8660254037844386468)
        wspolrzedne.append(0.0000000000000000000)
        wspolrzedne.append(0.8660254037844386468)
    elif n == 4:
        wspolrzedne.append(-0.9238795325112867561)
        wspolrzedne.append(-0.3826834323650897717)
        wspolrzedne.append(0.3826834323650897717)
        wspolrzedne.append(0.9238795325112867561)
    elif n == 5:
        wspolrzedne.append(-0.9510565162951535721)
        wspolrzedne.append(-0.5877852522924731292)
        wspolrzedne.append(0.0000000000000000000)
        wspolrzedne.append(0.5877852522924731292)
        wspolrzedne.append(0.9510565162951535721)
    else:
        print("Wprowadź '2', '3', '4' lub '5'.")

    wynik = 0
    for i in wspolrzedne:
        wynik += wspolczynniki[n-2] * funkcja_waga(funkcja, i)

    print("-----Kwadratura Gaussa-Czebyszewa-----")
    print("Wynik całki:", wynik, "z", n, "węzłami.")
