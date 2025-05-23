import numpy as np
from sympy import false

from calkowanie import wykonaj_calke
from horner import *
from wykresy import *


# funkcja zwracająca wyrażenie matematyczne w zależności od wyboru użytkownika
def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: x ** 3 + 5 * x ** 2 - 2 * x - 10  # horner
    if literka == 'b':
        return lambda x: 3 * x ** 3 + 3 * x ** 2 - 18 * x  # horner
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
print("Wybierz funkcję:")
print("a) f(x) = (x^3+5x^2−2x−10)/sqrt(1 - x^2)")
print("b) f(x) = (3x^3+3x^2-18x)/sqrt(1 - x^2)")
print("c) f(x) = (sin(x))/sqrt(1 - x^2)")
print("d) f(x) = (cos(x))/sqrt(1 - x^2)")
print("e) f(x) = (|x + 2|)/sqrt(1 - x^2)")
print("f) f(x) = (|5 - x|)/sqrt(1 - x^2)")
print("g) f(x) = (sin((1/2)x))/sqrt(1 - x^2)")
print("h) f(x) = (cos(2x+1))/sqrt(1 - x^2)")

funkcja_literka_flaga = True
funkcja_literka = input("Wybrano: ").lower()
if ord('a') <= ord(funkcja_literka) <= ord('h'):
    funkcja_literka_flaga = False
else:
    print("Wprowadź 'a', 'b', 'c', 'd', 'e', 'f', 'g' lub 'h'.")

wspolczynniki = None
if funkcja_literka == "a":
    wspolczynniki = [1, 5, -2, -10]
elif funkcja_literka == "b":
    wspolczynniki = [3, 3, -18, 0]

# 2) WYŚWIETLENIE FUNKCJI
x = np.linspace(-20, 20, 400)
funkcja=wybor_funkcji(funkcja_literka)

if wspolczynniki:
    wyswietl_wielomian(x, wspolczynniki)
else:
    wyswietl_funkcje(x,funkcja)

x1 = -1
x2 = 1
print("Działanie na przedziale <-1,1>. \n"
      "Jeśli chcesz zmniejszyć przedział podaj wartość liczbową x1. W przeciwnym wypadku przejdź dalej.\n"
      "Uwaga! Pamiętaj, że x1 < x2 ")
newX1=input()
if -1<=float(newX1)<=1:
    newX2=input("Podaj wartość x2: ")
    if float(newX1)<=float(newX2)<=1:
        x1=float(newX1)
        x2=float(newX2)
    else:
        print("Wprowadzona wartość x2 jest jest niepoprawna. Operujemy na domyślnym przedziale <-1,1> ")
else:
    print("Wprowadzona wartość x1 jest jest niepoprawna. Operujemy na domyślnym przedziale <-1,1> ")

stopien = None
test = True
while test:
    stopien = int(input(
        "Podaj stopień wielomianu aproksymującego: "))  # błąd aproksymacji, a program iteracyjnie dobiera stopień wielomianu aproksymacyjnego
    if stopien < 1:
        print("Niepoprawna wartość. Wprowadź ponownie.")
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


# wartości współczynników wielomianów aproksymacyjnych należy wyliczać w sposób iteracyjny
# i zapamiętywać w tablicy tak, aby możliwe było wykorzystanie tych współczynników w schemacie Hornera.

wspolczynniki_wielomianu = []

for k in range(stopien+1):

    f_licznik = funkcja(x) * T_k(x, k)
   # f_mianownik = T_k(x, k) * T_k(x, k)

    if k == 0:
        wsp = 1 / np.pi
    else:
        wsp = 2 / np.pi

    calka = (wykonaj_calke(f_licznik, ilosc_wezlow, None))
    wspolczynniki_wielomianu.append(wsp * calka)

x_aproksymacji = np.linspace(-1, 1, 500)
wynik = aproksymacja(x_aproksymacji, wspolczynniki_wielomianu)


# wielomian aproksymacyjny podanego stopnia
# rysuje jego wykres
# oblicza błąd aproksymacji
