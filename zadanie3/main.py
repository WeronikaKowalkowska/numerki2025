# wariant 2 - interpolacja Lagrange'a dla nierównych odstępów argumentu
import numpy as np
import random
from matplotlib import pyplot as plt

class Funkcja:
    def __init__(self, funkcja, wzor):
        self.funkcja = funkcja
        self.wzor = wzor

    def __call__(self, x):
        return self.funkcja(x)

    def __str__(self):
        return self.wzor

# funkcja realizująca schemat hornera
def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def wyswietl_wykres(x, y):
    plt.plot(x, y, color='pink')
    plt.title("Wykres funkcji:")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.subplots_adjust(left=0.15)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.show()

def wyswietl_wykres_koncowy(x, y, punkty_x, punkty_y):
    plt.plot(x, y, color='pink')
    plt.scatter(punkty_x, punkty_y, marker='x', color='magenta')
    plt.title("Wykres interpolacji funkcji:")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.subplots_adjust(left=0.15)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.show()

def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: 5 * x + 2
    if literka == 'b':
        return lambda x: np.abs(x + 1)
    if literka == 'c':
        return lambda x: 3 * x ** 3 + 3 * x ** 2 - 18 * x
    if literka == 'd':
        return lambda x: np.sin(x)
    if literka == 'e':
        return lambda x: np.abs(np.sin(x))
    if literka == 'f':
        return lambda x: np.cos(2 * x + 1)
    if literka == 'g':
        return lambda x: np.abs(x ** 2 - 4)

funkcja_wzor = {
    'a': "5*x + 2",
    'b': "|x + 1|",
    'c': "3*x^3 + 3*x^2 - 18*x",
    'd': "sin(x)",
    'e': "|sin(x)|",
    'f': "cos(2x + 1)",
    'g': "|x^2 - 4|"
}

# 1) WYBÓR FUNKCJI
print("Wybierz funkcję:")
print("a) f(x) = 5x + 2")
print("b) f(x) = |x + 1|")
print("c) f(x) = 3x^3+3x^2-18x")
print("d) f(x) = sin(x)")
print("e) f(x) = |sin(x)|")
print("f) f(x) = cos(2x + 1)")
print("g) f(x) = |x^2-4|")

literka = ""  # znak określający wybór funkcji podany przez użytkownika
test = True  # zmienna sprawdzająca poprwaność input
while test:
    literka = input("Wybrano: ")
    literka = literka.lower()  # zapewnienie odczytu jako mała litera
    if 97 <= ord(literka) <= 104:
        test = False
    else:
        print("Niepoprawny wybór funkcji. Wybierz ponownie: ")

funkcja = Funkcja(wybor_funkcji(literka), funkcja_wzor[literka])

# 2)WYŚWIETLENIE WYBRANEJ FUNKCJI
x = np.linspace(-20, 20, 4000)  # zmienna służąca rozmieszczeniu punktów na osi OX wyświetlanych wykresów
wyswietl_wykres(x, funkcja(x))

rodzaj = input(
    "Wybierz rodzaj wczytania położenia węzłów interpolacyjnych:\na) wczytanie z pliku 'wezly.txt', b) wartości wylosowane, c) wartości wczytane z konsoli. (opcja domyślna to b): ")

# 3) WYBÓR PRZEDZIAŁU INTERPOLACJI
x_1 = 0
x_2 = 0
if rodzaj == "a":
    with open('wezly.txt', 'r') as f:
        w = []
        for line in f:
            w.append(float(line))
        x_1 = min(w)
        x_2 = max(w)
else:
    test = True
    while test:
        print("Wybierz przedział interpolacji: ")
        x_1 = int(input("Lewy kraniec(wartość mniejsza): "))
        x_2 = int(input("Prawy kraniec(wartość większa): "))
        if x_1 < x_2:
            test = False


# 4) WYLICZANIE WARTOŚCI WYBRANEJ FUNKCJI W WĘZŁACH INTERPOLACYJNYCH
# 5) WYBÓR LICZBY WĘZŁÓW INTERPOLACYJNYCH
ile_wezlow = 0
if rodzaj != 'a':
    test = True
    while test:
        ile_wezlow = int(input("Wybierz liczbę węzłów interpolacyjnych: "))
        if ile_wezlow > 0:
            test = False

wezly_x = []
czy_random = True
if rodzaj == 'a':
    with open('wezly.txt', 'r') as f:
        for line in f:
            wezly_x.append(float(line))
            czy_random = False
            ile_wezlow += 1
    for i in range(len(wezly_x)):
        if not x_1 <= wezly_x[i] <= x_2:
            wezly_x = []
            czy_random = True
            print(
                "Podane położenia nie są zgodne z zadeklarowanym przedziałem. Zatem będą one wybrane w sposób losowy.")
elif rodzaj == 'c':
    for i in range(0, ile_wezlow):
        wezly_x.append(float(input(f"Podaj położenie węzła {i}: ")))
        czy_random = False
elif rodzaj == 'b' or czy_random == True:
    for i in range(0, ile_wezlow):
        wezly_x.append(random.randint(x_1, x_2))

wezly_y = []
for i in range(0, ile_wezlow):
    if literka == 'c':
        wezly_y.append(horner(wezly_x[i], [3, 3, 0, -18]))
    else:
        wezly_y.append(funkcja(wezly_x[i]))


# 6) WYZNACZENIE WIELOMIANU INTERPOLUJĄCEGO WYBRANĄ FUNKCJĘ
def licz_x(funkcja, liczba):
    return Funkcja(lambda x: funkcja(x) + liczba, f"({funkcja.wzor}) + {liczba}")


def mnoz_x(funkcja, liczba):
    return Funkcja(lambda x: funkcja(x) * liczba, f"({funkcja.wzor}) * {liczba}")


def dziel_x(funkcja, liczba):
    if liczba != 0:
        return Funkcja(lambda x: funkcja(x) / liczba, f"({funkcja.wzor}) / {liczba}")
    else:
        exit(404)


def mnoz_funkcje(funkcja1, funkcja2):
    return Funkcja(lambda x: funkcja1(x) * funkcja2(x), f"({funkcja1.wzor}) * ({funkcja2.wzor})")


def licz_funkcje(funkcja1, funkcja2):
    return Funkcja(lambda x: funkcja1(x) + funkcja2(x), f"({funkcja1.wzor}) + ({funkcja2.wzor})")


L = []
for i in range(0, ile_wezlow):
    iloczyn = Funkcja(lambda x: 1, "1")
    suma = Funkcja(lambda x: 0, "0")
    for j in range(0, ile_wezlow):
        if i != j:
            if wezly_x[i] != wezly_x[j]:
                iloczyn = mnoz_funkcje(
                    dziel_x(licz_x(Funkcja(lambda x: x, "x"), -wezly_x[j]), (wezly_x[i] - wezly_x[j])), iloczyn)

    suma = licz_funkcje(mnoz_x(iloczyn, wezly_y[i]), suma)
    L.append(suma)  # dla węzła o numerze x suma jest x

L_koniec = L[0]
for i in range(1, len(L)):
    L_koniec = licz_funkcje(L[i], L_koniec)

print(L_koniec.wzor)
print(L_koniec.funkcja(1))

x = np.linspace(x_1 - 1, x_2 + 1, 4000)

# 7) RYSOWANIE WYKRESU WIELOMIANU INTERPOLUJĄCEGO Z ZAZNACZENIEM WĘZŁÓW INTERPOLACJI
wyswietl_wykres_koncowy(x, L_koniec(x), wezly_x, wezly_y)
