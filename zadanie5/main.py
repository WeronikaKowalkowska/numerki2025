import numpy as np
from matplotlib import pyplot as plt
from sympy import false


#funkcja zwracająca wyrażenie matematyczne w zależności od wyboru użytkownika
def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: x ** 3 + 5 * x ** 2 - 2 * x - 10
    if literka == 'b':
        return lambda x: 3 * x ** 3 + 3 * x ** 2 - 18 * x
    if literka == 'c':
        return lambda x: np.sin(x)
    if literka == 'd':
        return lambda x: np.cos(x)
    if literka == 'e':
        return lambda x: abs(x+2)
    if literka == 'f':
        return lambda x: abs(5-x)
    if literka == 'g':
        return lambda x: np.sin((1 / 2) * x)
    if literka == 'h':
        return lambda x: np.cos(2 * x + 1)

def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def wyswietl_funkcje(x, funkcja):
    y = funkcja(x)
    return wyswietl_wykres(x, y)

def wyswietl_wielomian(x, wspolczynniki):
    y = []
    for i in range(len(x)):
        y.append(horner(x[i], wspolczynniki))
    return wyswietl_wykres(x, y)

def wyswietl_wykres(x, y):
    plt.plot(x, y)
    plt.title("Wykres funkcji:")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.subplots_adjust(left=0.15)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    return plt

test = True
while test:
    x1,x2=int(input("Wybierz przedział (x1,x2) : (x1 < x2) : "))
    if x1<x2:
        test=false
    else:
        print("Niewłaściwy przedział. Wybierz ponownie")

test=True
while test:
    stopien=int(input("Podaj stopień wielomianu: "))
    