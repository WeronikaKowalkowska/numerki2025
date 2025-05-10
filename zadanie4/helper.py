import numpy as np
from sympy import symbols, sympify, S
from sympy.calculus.util import continuous_domain

def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: 4 * x ** 3 - 3 * x
    if literka == 'b':
        return lambda x: 1 / (1 + x ** 2)
    if literka == 'c':
        return lambda x: np.cos(x)

def funkcja_text(funkcja):
    if funkcja == 'a':
        return "4 * x ** 3 - 3 * x"
    if funkcja == 'b':
        return "1 / (1 + x ** 2)"
    if funkcja == 'c':
        return "cos(x)"

def funkcja_waga(funkcja, x):
    return funkcja(x) * np.sqrt(1/(1 - (x ** 2)))

def czy_wlasciwa(funkcja_literka):
    x = symbols('x')
    funkcja = sympify(funkcja_literka)
    dziedzina = continuous_domain(funkcja, x, S.Reals) # wyznaczenie dziedziny ciągłości funkcji f względem zmiennej x w zbiorze liczb rzeczywistych
    return dziedzina.contains(-1) and dziedzina.contains(1) # sprawdzamy, czy końce przedziału [−1,1] należą do dziedziny ciągłości funkcji

def simpson(funkcja, a, b, liczba_przedzialow):
    h = (b - a) / liczba_przedzialow  # długość jednego podprzedziału
    x = []
    for i in range(liczba_przedzialow + 1):  # generuje liczba_przedzialow + 1 punktów
        x.append(a + i * h)
    wynik = funkcja(x[0]) + funkcja(x[len(x) - 1])  # pierwszy i ostatni punkt
    for i in range(1, len(x) - 1):
        if i % 2 != 0:
            wynik += funkcja(x[i]) * 4
        else:
            wynik += funkcja(x[i]) * 2
    return (1 / 3) * h * wynik

def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik
