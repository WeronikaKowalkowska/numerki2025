import numpy as np
from sympy import symbols, Poly

def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def T_k(x, k):
    x = np.array(x)  # zapewnia wektorową obsługę
    if np.any((x < -1) | (x > 1)):
        raise ValueError("x musi być w przedziale [-1, 1]")
    return np.cos(k * np.arccos(x))

def aproksymacja(x, wspolczynniki):
    suma = np.zeros_like(x) # zapewnia wektorową obsługę
    for k, a in enumerate(wspolczynniki):
        suma += a * T_k(x, k)
    return suma

def blad_aproksymacji(y_fun, y_apr):

    # średni błąd kwadratowy (Mean Squared Error)
    mse = np.mean((y_fun - y_apr) ** 2)

    # maksymalny błąd bezwzględny
    max_error = np.max(np.abs(y_fun - y_apr))

    print(f"Średni błąd kwadratowy (MSE): {mse:.6f}")
    print(f"Maksymalny błąd bezwzględny: {max_error:.6f}")