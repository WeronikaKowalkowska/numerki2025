import matplotlib.pyplot as plt
import numpy as np

def wybor_funkcji(literka):
    if literka == 'A' or literka == 'a':
        return lambda x: x ** 3 + 5 * x ** 2 - 2 * x - 10
    if literka == 'B' or literka == 'b':
        return lambda x: 3 * x ** 3 + 3 * x ** 2 - 18 * x
    if literka == 'C' or literka == 'c':
        return np.sin
    if literka == 'D' or literka == 'd':
        return np.cos
    if literka == 'E' or literka == 'e':
        return lambda x: 2 ** x
    if literka == 'F' or literka == 'f':
        return lambda x: (1 / 2) ** x
    if literka == 'G' or literka == 'g':
        return lambda x: np.sin((1 / 2) * x)
    if literka == 'H' or literka == 'h':
        return lambda x: np.cos(2 * x + 1)

def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

# METODA BISEKCJI
def bisekcja_epsilon(a, b, funkcja, epsilon):
    x_srodek = (a + b) / 2
    while abs(funkcja(x_srodek)) >= epsilon:
        x_srodek = (a + b) / 2
        funkcja_x_srodek = funkcja(x_srodek)
        if funkcja_x_srodek == 0:
            return x_srodek
        if funkcja_x_srodek * funkcja(b) < 0:
            a = x_srodek
        elif funkcja_x_srodek * funkcja(a) < 0:
            b = x_srodek
    return x_srodek

def bisekcja_iteracje(a, b, funkcja, iteracje):
    x_srodek = (a + b) / 2
    for i in range(iteracje):
        x_srodek = (a + b) / 2
        funkcja_x_srodek = funkcja(x_srodek)
        if funkcja_x_srodek  == 0:
            return x_srodek
        if funkcja_x_srodek  * funkcja(b) < 0:
            a = x_srodek
        if funkcja_x_srodek  * funkcja(a) < 0:
            b = x_srodek
    return x_srodek

def bisekcja_epsilon_wielomianu(a, b, wspolczynniki, epsilon):
    x_srodek = (a + b) / 2
    while abs(horner(x_srodek, wspolczynniki)) >= epsilon:
        x_srodek = (a + b) / 2
        horner_x_srodek = horner(x_srodek, wspolczynniki)
        if horner_x_srodek == 0:
            return x_srodek
        if horner_x_srodek * horner(b, wspolczynniki) < 0:
            a = x_srodek
        if horner_x_srodek * horner(a, wspolczynniki) < 0:
            b = x_srodek
    return x_srodek


def bisekcja_iteracje_wielomianu(a, b, wspolczynniki, iteracje):
    x_srodek = (a + b) / 2
    for i in range(iteracje):
        x_srodek = (a + b) / 2
        horner_x_srodek = horner(x_srodek, wspolczynniki)
        if horner_x_srodek == 0:
            return x_srodek
        if horner_x_srodek * horner(b, wspolczynniki) < 0:
            a = x_srodek
        if horner_x_srodek * horner(a, wspolczynniki) < 0:
            b = x_srodek
    return x_srodek

# METODA FALSI
def falsi_iteracje(a, b, funkcja, iteracje):
    x0 = 0
    for i in range(iteracje):
        if funkcja(a) == funkcja(b):
            return (a + b) / 2
        x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
        funkcja_x_srodek = funkcja(x0)
        if funkcja_x_srodek == 0:
           return x0
        if funkcja_x_srodek * funkcja(b) < 0:
            a = x0
        if funkcja_x_srodek * funkcja(a) < 0:
            b = x0
    return x0

def falsi_epsilon(a, b, funkcja, epsilon):
    x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
    while abs(funkcja(x0)) >= epsilon:
        if funkcja(a) == funkcja(b):
            return (a + b) / 2
        x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
        funkcja_x_srodek = funkcja(x0)
        if funkcja_x_srodek == 0:
           return x0
        if funkcja_x_srodek * funkcja(b) < 0:
            a = x0
        if funkcja_x_srodek * funkcja(a) < 0:
            b = x0
    return x0

def falsi_iteracje_wielomianu(a, b, wspolczynniki, iteracje):
    x0 = 0
    for i in range(iteracje):
        horner_a = horner(a, wspolczynniki)
        horner_b = horner(b, wspolczynniki)
        if horner_a == horner_b:
            return (a + b) / 2
        x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
        horner_x0 = horner(x0, wspolczynniki)
        if horner_x0 == 0:
            return x0
        if horner_x0 * horner_b < 0:
            a = x0
        if horner_x0 * horner_a < 0:
            b = x0
    return x0


def falsi_epsilon_wielomianu(a, b, wspolczynniki, epsilon):
    horner_a = horner(a, wspolczynniki)
    horner_b = horner(b, wspolczynniki)
    x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
    horner_x0 = horner(x0, wspolczynniki)
    while abs(horner_x0) >= epsilon:
        horner_a = horner(a, wspolczynniki)
        horner_b = horner(b, wspolczynniki)
        if horner_a == horner_b:
            return (a + b) / 2
        x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
        horner_x0 = horner(x0, wspolczynniki)
        if horner_x0 == 0:
            return x0
        if horner_x0 * horner_b < 0:
            a = x0
        if horner_x0 * horner_a < 0:
            b = x0
    return x0


def wyswietl_funkcje(x,funkcja):
    y = funkcja(x)
    return wyswietl_wykres(x, y)

def wyswietl_wynik_funkcji(x,funkcja, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_funkcje(x,funkcja)
    plot.scatter(wynik_bisekcji, funkcja(wynik_bisekcji), color='yellow', s=100, marker='o', label="Bisekcja")
    plot.scatter(wynik_falsi, funkcja(wynik_falsi), color='magenta', s=100, marker='x', label="Metoda falsi")
    plt.legend()
    plot.show()

def wyswietl_wielomian(x, wspolczynniki, dlugoscTablicy):
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

def wyswietl_wynik_wielomianu(x, wspolczynniki, dlugoscTablicy, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_wielomian(x, wspolczynniki, dlugoscTablicy)
    plot.scatter(wynik_bisekcji, horner(wynik_bisekcji, wspolczynniki), color='yellow', s=100, marker='o',
                 label="Bisekcja")
    plot.scatter(wynik_falsi, horner(wynik_falsi, wspolczynniki), color='magenta', s=100, marker='x',
                 label="Metoda falsi")
    plot.legend()
    plot.title("Wykres funkcji:")
    plot.show()