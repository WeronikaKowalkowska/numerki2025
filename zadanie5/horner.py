import numpy as np


def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def T_k(x, k):
    if -1 <= x <= 1:
        return np.cos(k * np.arccos(x))
    else:
        raise ValueError("x musi być w przedziale [-1, 1]")

def aproksymacja(x, wspolczynniki):
    suma = 0
    for k, a in enumerate(wspolczynniki):
        suma += a * T_k(x, k)
    return suma
