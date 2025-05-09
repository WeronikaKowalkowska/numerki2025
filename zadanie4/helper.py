import numpy as np

def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: 4 * x ** 3 - 3 * x
    if literka == 'b':
        return lambda x: 1 / (1 + x ** 2)
    if literka == 'c':
        return lambda x: np.cos(x)

def funkcja_waga(funkcja, x):
    return funkcja(x) * np.sqrt(1/(1 - (x ** 2)))

def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik
