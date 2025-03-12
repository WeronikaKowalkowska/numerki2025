import numpy as np
from matplotlib import pyplot as plt


def horner(argument, wspolczynniki, dlugoscTablicy):
    wynik = wspolczynniki[0]
    for i in range(1, dlugoscTablicy):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik


def wyswietl_wykres(x, y):
    plt.plot(x, y)
    plt.title("Wykres funkcji:")
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    return plt


def wyswietl_wielomian(x, wspolczynniki, dlugoscTablicy):
    y = []
    for i in range(len(x)):
        y.append(horner(x[i], wspolczynniki, dlugoscTablicy))
    return wyswietl_wykres(x, y)


def wyswietl_wynik_wielomianu(x, wspolczynniki, dlugoscTablicy, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_wielomian(x, wspolczynniki, dlugoscTablicy)
    plot.scatter(wynik_bisekcji, horner(wynik_bisekcji, wspolczynniki, dlugoscTablicy), color='red', s=100, marker='o',
                 label="Bisekcja")
    plot.scatter(wynik_falsi, horner(wynik_falsi, wspolczynniki, dlugoscTablicy), color='blue', s=100, marker='x',
                 label="Metoda falsi")
    plot.legend()
    plot.title("Wykres funkcji:")
    plot.show()


def bisekcja_epsilon_wielomianu(a, b, wspolczynniki, dlugoscTablicy, epsilon):
    x_srodek = (a + b) / 2
    while (abs(horner(x_srodek, wspolczynniki, dlugoscTablicy)) < epsilon):
        x_srodek = (a + b) / 2
        horner_x_srodek = horner(x_srodek, wspolczynniki, dlugoscTablicy)
        if (horner_x_srodek * horner(b, wspolczynniki, dlugoscTablicy) < 0):
            a = x_srodek
        if (horner_x_srodek * horner(a, wspolczynniki, dlugoscTablicy) < 0):
            b = x_srodek
    return x_srodek


def bisekcja_iteracje_wielomianu(a, b, wspolczynniki, dlugoscTablicy, iteracje):
    x_srodek = (a + b) / 2
    for i in range(iteracje):
        x_srodek = (a + b) / 2
        horner_x_srodek = horner(x_srodek, wspolczynniki, dlugoscTablicy)
        if (horner_x_srodek * horner(b, wspolczynniki, dlugoscTablicy) < 0):
            a = x_srodek
        if (horner_x_srodek * horner(a, wspolczynniki, dlugoscTablicy) < 0):
            b = x_srodek
    return x_srodek


def falsi_iteracje_wielomianu(a, b, wspolczynniki, dlugoscTablicy, iteracje):
    pierwiastek = 0
    for i in range(iteracje):

        horner_a = horner(a, wspolczynniki, dlugoscTablicy)
        horner_b = horner(b, wspolczynniki, dlugoscTablicy)
        x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
        horner_x0 = horner(x0, wspolczynniki, dlugoscTablicy)
        if (horner_b - horner_a != 0):
            # x0 = a - (horner_a / horner_b - horner_a)) *(b - a)
            if (horner_x0 == 0):
                pierwiastek = x0
        if (horner_x0 * horner_b < 0):
            a = x0
        if (horner_x0 * horner_a < 0):
            b = x0
    return pierwiastek


def falsi_epsilon_wielomianu(a, b, wspolczynniki, dlugoscTablicy, epsilon):
    # DZIELENIE PRZEZ ZERO
    horner_a = horner(a, wspolczynniki, dlugoscTablicy)
    horner_b = horner(b, wspolczynniki, dlugoscTablicy)
    x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
    horner_x0 = horner(x0, wspolczynniki, dlugoscTablicy)
    while (abs(horner_x0) >= epsilon):
        horner_x0 = horner(x0, wspolczynniki, dlugoscTablicy)
        horner_a = horner(a, wspolczynniki, dlugoscTablicy)
        horner_b = horner(b, wspolczynniki, dlugoscTablicy)
        if horner_b - horner_a == 0:
            return None
        if ((horner_b - horner_a) != 0):
            x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
        if (horner_x0 * horner_b < 0):
            a = x0
            if (horner_x0 * horner_a) < 0:
                b = x0
    return x0
