import numpy as np

from calkowanie import wykonaj_calke, oblicz_wspolczynniki
from helper import *
from wykresy import *


# funkcja zwracająca wyrażenie matematyczne w zależności od wyboru użytkownika
def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: x ** 3 + 5 * x  # horner
    if literka == 'b':
        return lambda x: 3 * x ** 2 + 3  # horner
    if literka == 'c':
        return lambda x: np.sin(x)
    if literka == 'd':
        return lambda x: np.cos(x)
    if literka == 'e':
        return lambda x: abs(x + 2)
    if literka == 'f':
        return lambda x: abs(5 - x)
    if literka == 'g':
        return lambda x: np.sin((1 / 2) * x)
    if literka == 'h':
        return lambda x: np.cos(2 * x + 1)


# 1) WYBÓR FUNKCJI
print("Wybierz funkcję: (wszystkie zawierają wagę 1/(sqrt(1 - x^2))")
print("a) f(x) = (x^3+5x)")
print("b) f(x) = (3x^2+3)")
print("c) f(x) = (sin(x))")
print("d) f(x) = (cos(x))")
print("e) f(x) = (|x + 2|)")
print("f) f(x) = (|5 - x|)")
print("g) f(x) = (sin((1/2)x))")
print("h) f(x) = (cos(2x+1))")

funkcja_literka_flaga = True
funkcja_literka = input("Wybrano: ").lower()
while funkcja_literka_flaga:
    if ord('a') <= ord(funkcja_literka) <= ord('h'):
        funkcja_literka_flaga = False
    else:
        print("Wprowadź 'a', 'b', 'c', 'd', 'e', 'f', 'g' lub 'h'.")

wspolczynniki = None
if funkcja_literka == "a":
    wspolczynniki = [1, 0, 5, 0]
elif funkcja_literka == "b":
    wspolczynniki = [3, 0, 3]

# 2) WYŚWIETLENIE WYKRESU FUNKCJI
x = np.linspace(-1, 1, 1000)
funkcja = wybor_funkcji(funkcja_literka)
if wspolczynniki:
    wyswietl_wielomian(x, wspolczynniki).show()
else:
    wyswietl_funkcje(x,funkcja).show()

x1 = -1
x2 = 1
print("Działanie na przedziale <-1, 1>. \n"
      "Jeśli chcesz zmniejszyć przedział podaj wartość liczbową x1 (lub 2 jeżeli chcesz zostać przy domyślnym przedziale): \n"
      "Uwaga! Pamiętaj, że x1 < x2. ")
try:
    newX1 = float(input("Podaj wartość x1: "))
    if -1 <= newX1 <= 1:
        newX2 = float(input("Podaj wartość x2: "))
        if newX1 < newX2:
            x1 = newX1
            x2 = newX2
        else:
            print("Operujemy na domyślnym przedziale <-1, 1>. ")
    else:
        print("Operujemy na domyślnym przedziale <-1, 1>. ")
except ValueError:
    print("Niepoprawna wartość. Operujemy na domyślnym przedziale <-1, 1>.")

blad_dopuszczalny = None
stopien = None
test = True
test2 = True
while test:
    blad_dopuszczalny = float(input("Podaj dopuszczalny błąd (lub 0 jeśli chcesz ręcznie ustawić stopień): "))
    if blad_dopuszczalny < 0:
        print("Niepoprawna wartość. Wprowadź ponownie.")
    elif blad_dopuszczalny == 0:
        while test2:
            stopien = int(input("Podaj stopień wielomianu aproksymującego: "))
            if stopien < 1:
                print("Niepoprawna wartość. Wprowadź ponownie.")
            else:
                test2 = False
                test = False
    else:
        test = False

ilosc_wezlow = None
test = True
while test:
    ilosc_wezlow = int(input("Podaj ilość węzłów do całkowania: "))
    if ilosc_wezlow < 1:
        print("Niepoprawna wartość. Wprowadź ponownie.")
    else:
        test = False

wspolczynniki_wielomianu = []
x_aproksymacji = np.linspace(x1, x2, 50)
y_aproksymacji = []
y_funkcji = []

# wartości współczynników wielomianów
if blad_dopuszczalny > 0:
    stopien = 1
    flaga = True
    while flaga:

        wspolczynniki_wielomianu = oblicz_wspolczynniki(funkcja, ilosc_wezlow, stopien)
        y_aproksymacji = aproksymacja(x_aproksymacji, wspolczynniki_wielomianu)

        f = None

        if wspolczynniki is not None:
            f = lambda x: horner(x, wspolczynniki)
        else:
            f = funkcja

        y_funkcji = np.vectorize(f)(x_aproksymacji)

        blad = blad_aproksymacji(y_funkcji, y_aproksymacji)
        print(f"Stopień: {stopien}, Błąd: {blad:.10e}")

        if blad < blad_dopuszczalny:
            flaga = False
            print(f"Osiągnięto wymagany błąd przy stopniu: {stopien}")
        else:
            stopien += 1

        if stopien == 101:
            print("Osiągnięto maksymalny możliwy stopień. Zaprzestanie dalszych obliczeń.")
            flaga = False



else:
    wspolczynniki_wielomianu = oblicz_wspolczynniki(funkcja, ilosc_wezlow, stopien)
    y_aproksymacji = aproksymacja(x_aproksymacji, wspolczynniki_wielomianu)

    if wspolczynniki is not None:
        f = lambda x: horner(x, wspolczynniki)
    else:
        f = funkcja

    y_funkcji = np.vectorize(f)(x_aproksymacji)

# 3) WYŚWIETLENIE WYKRESU APROKSYMACJI
wyswietl_aproksymacje(x_aproksymacji, y_aproksymacji).show()

# 4) WYŚWIETLENIE WZORU NA WIELOMIAN APROKSYMACYJNY
wyswietl_wielomian_aproksymacjyny_sformatowany(
    wspolczynniki_wielomianu[::-1])  # odwracamy współczynniki, bo numpy/poly1d zakłada malejącą potęgę
