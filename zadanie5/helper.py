import numpy as np

def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def T_k(x, k):
    return np.cos(k * np.arccos(x))

def aproksymacja(x, wspolczynniki):
    suma = np.zeros_like(x)  # zapewnia wektorową obsługę
    for k in range(len(wspolczynniki)):
        a = wspolczynniki[k]
        suma += a * T_k(x, k)
    return suma

def blad_aproksymacji(y_fun, y_apr):
    # maksymalny błąd bezwzględny
    max_error = np.max(np.abs(y_fun - y_apr))
    return max_error
