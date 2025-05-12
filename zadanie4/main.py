from helper import *

funkcja_literka = None
funkcja_literka_flaga = True
wspolczynniki = None

while funkcja_literka_flaga:
    print("Wybierz funkcję:")
    print("a) f(x) = x^2")
    print("b) f(x) = 4x^3 - 3x")
    print("c) f(x) = sqrt(1 - x^2)")
    print("d) f(x) = x^4 - 2x^2 + 1")

    funkcja_literka = input("Wybrano: ").lower()
    if funkcja_literka == "a" or funkcja_literka == "b" or funkcja_literka == "c" or funkcja_literka == "d":
        funkcja_literka_flaga = False
    else:
        print("Wprowadź 'a', 'b', 'c' lub 'd'.")

funkcja = wybor_funkcji(funkcja_literka)

if funkcja_literka == "b":
    wspolczynniki = [4, 0, -3, 0]
elif funkcja_literka == "d":
    wspolczynniki = [1, 0, -2, 0, 1]

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

            wynik = simpson(funkcja, a, b, liczba_przedzialow, wspolczynniki)

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

            wynik_czastkowy = simpson(funkcja, a, b, liczba_przedzialow, wspolczynniki)

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

            wynik_czastkowy = simpson(funkcja, a, b, liczba_przedzialow, wspolczynniki)

            if wynik_poprzedni is not None and abs(wynik - wynik_poprzedni) < epsilon:
                nie_wlasciwa_flaga = False

            wynik += wynik_czastkowy
            wynik_poprzedni = wynik
            srodek_przedzalu = a
            krok = krok / 2

    print("-------Złożona kwadratura Newtona-Cotesa (wzór Simpsona)-------")
    print("Wynik całki:", wynik, "z", liczba_przedzialow, "podprzedziałami.")

if metoda == "b":
    n = None
    n_flaga = True
    wspolrzedne = []

    try:
        n = int(input("Podaj liczbę węzłów (2, 3, 4 lub 5): "))
        if n in (2, 3, 4, 5):
            n_flaga = False
    except ValueError:
        print("Liczba całkowita nie została wprowadzona, zatem obliczenia będą wykonane dla wszystkich węzłów.")


    if n_flaga:
        for n in range(2, 6):
            wspolrzedne = [np.cos((2 * i - 1) * np.pi / (2 * n)) for i in range(1, n + 1)]
            waga = np.pi / n

            wynik = 0
            for i in wspolrzedne:
                f = None
                if funkcja_literka == "b" or funkcja_literka == "d":
                    f = horner(i, wspolczynniki)
                else:
                    f = funkcja(i)
                wynik += waga * funkcja_waga(lambda x: f, i)

            print("-----Kwadratura Gaussa-Czebyszewa-----")
            print("Wynik całki:", wynik, "z", n, "węzłami.")
    else:

        wspolrzedne = [np.cos((2 * i - 1) * np.pi / (2 * n)) for i in range(1, n + 1)]
        waga = np.pi / n

        wynik = 0
        for i in wspolrzedne:
            f = None
            if funkcja_literka == "b" or funkcja_literka == "d":
                f = horner(i, wspolczynniki)
            else:
                f = funkcja(i)
            wynik += waga * funkcja_waga(lambda x: f, i)

        print("-----Kwadratura Gaussa-Czebyszewa-----")
        print("Wynik całki:", wynik, "z", n, "węzłami.")
