import numpy as np
from sympy import symbols, sympify, S
from sympy.calculus.util import continuous_domain
from horner import *

def funkcja_waga(f, x):
    return f(x) * np.sqrt(1 - x ** 2)

# chcesz liczyć z wagą, to podajesz bez wagi
def wykonaj_calke(funkcja, n, wspolczynniki):

    wspolrzedne = [np.cos((2 * i - 1) * np.pi / (2 * n)) for i in range(1, n + 1)]
    waga = np.pi / n

    wynik = 0
    for i in wspolrzedne:
        f = None
        if wspolczynniki is not None:
            f = lambda x: horner(x, wspolczynniki)
        else:
            f = funkcja
        wynik += waga * funkcja_waga(f, i)

    return wynik

    # print("-----Kwadratura Gaussa-Czebyszewa-----")
    # print("Wynik całki:", wynik, "z", n, "węzłami.")