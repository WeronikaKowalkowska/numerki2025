import numpy as np
from sympy import symbols, sympify, S
from sympy.calculus.util import continuous_domain
from helper import *


def funkcja_waga(f, x):
    return f(x)


# chcesz liczyć z wagą, to podajesz bez wagi
def wykonaj_calke(funkcja, n):
    wezly = [np.cos((2 * i - 1) * np.pi / (2 * n)) for i in range(1, n + 1)]
    waga = np.pi / n
    wynik = 0
    for i in wezly:
         wynik += funkcja_waga(funkcja, i)
    return waga * wynik


def oblicz_wspolczynniki(funkcja, ilosc_wezlow, stopien):
    wspolczynniki_wielomianu = []
    for k in range(stopien +1):
        gk = lambda x: T_k(x, k)
        licznik = wykonaj_calke(lambda x: funkcja(x) * gk(x), ilosc_wezlow)
        mianownik = wykonaj_calke(lambda x: gk(x) ** 2, ilosc_wezlow)
        c_k = licznik / mianownik
        wspolczynniki_wielomianu.append(c_k)
    return wspolczynniki_wielomianu
