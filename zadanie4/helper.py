import numpy as np
from sympy import symbols, sympify, S
from sympy.calculus.util import continuous_domain


def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: x ** 2
    if literka == 'b':
        return lambda x: 4 * x ** 3 - 3 * x
    if literka == 'c':
        return lambda x: np.sqrt(1 - x ** 2)
    if literka == 'd':
        return lambda x: x ** 4 - 2 * x ** 2 + 1
    if literka == 'e':
        return lambda x: (x ** 3 - x + 1) / np.sqrt(1 - x ** 2)
    if literka == 'f':
        return lambda x: (3 * x ** 4) / np.sqrt(1 - x ** 2)


def funkcja_text(funkcja):
    if funkcja == 'a':
        return "x ** 2"
    if funkcja == 'b':
        return "4 * x ** 3 - 3 * x"
    if funkcja == 'c':
        return "sqrt(1 - x ** 2)"
    if funkcja == 'd':
        return "x ** 4 - 2 * x ** 2 + 1"
    if funkcja == 'e':
        return "(x ** 3 - x + 1) / sqrt(1 - x ** 2)"
    if funkcja == 'f':
        return "(3 * x ** 4) / sqrt(1 - x ** 2)"


def czy_wlasciwa(funkcja_literka):
    x = symbols('x')
    funkcja = sympify(funkcja_text(funkcja_literka))
    dziedzina = continuous_domain(funkcja, x,
                                  S.Reals)  # wyznaczenie dziedziny ciągłości funkcji f względem zmiennej x w zbiorze liczb rzeczywistych
    return dziedzina.contains(-1) and dziedzina.contains(
        1)  # sprawdzamy, czy końce przedziału [−1,1] należą do dziedziny ciągłości funkcji

# metoda Gaussa-Czebyszewa będzie aproksymować tę samą całkę standardową bez wagi
def funkcja_waga(f, x):
    return f(x) * np.sqrt(1 - x ** 2)

def simpson(funkcja, a, b, liczba_przedzialow, wspolczynniki):
    h = (b - a) / liczba_przedzialow  # długość jednego podprzedziału
    x = []

    if wspolczynniki:
        f = lambda val: horner(val, wspolczynniki)
    else:
        f = funkcja

    for i in range(liczba_przedzialow + 1):  # generuje liczba_przedzialow + 1 punktów
        x.append(a + i * h)

    wynik = f(x[0]) + f(x[len(x) - 1])  # pierwszy i ostatni punkt
    for i in range(1, len(x) - 1):
        if i % 2 != 0:
            wynik += f(x[i]) * 4
        else:
            wynik += f(x[i]) * 2
    return (1 / 3) * h * wynik


def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik
