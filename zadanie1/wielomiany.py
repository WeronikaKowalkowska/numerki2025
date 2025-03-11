import numpy as np
from matplotlib import pyplot as plt

# def potega(podstawa, wykladnik):
#     wynik = 1
#     for _ in range(wykladnik):
#         wynik *= podstawa
#     # while (wykladnik > 0):
#     #     wynik = wynik * podstawa
#     #     wykladnik = wykladnik - 1
#     return wynik

# def horner(argument, wspolczynniki, dlugoscTablicy):
#     wynik = 0
#     n = 0
#     for i in range(dlugoscTablicy - 1, -1, -1):
#         if (n < dlugoscTablicy - 1):
#             wynik = wynik + potega(argument, i) * wspolczynniki[n]
#             n = n + 1
#         else:
#             wynik = wynik + wspolczynniki[n]
#     return wynik

def horner(argument, wspolczynniki, dlugoscTablicy):
    wynik = wspolczynniki[0]
    for i in range(1, dlugoscTablicy):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def wyswietl_wykres(x,y):
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
    plot.scatter(wynik_bisekcji, horner(wynik_bisekcji, wspolczynniki, dlugoscTablicy), color='red', s=100, marker='o', label="Bisekcja")
    plot.scatter(wynik_falsi, horner(wynik_falsi, wspolczynniki, dlugoscTablicy), color='blue', s=100, marker='x', label="Metoda falsi")
    plot.legend()
    plot.title("Wykres funkcji:")
    plot.show()

def bisekcja_epsilon_wielomianu(a, b, wspolczynniki, dlugoscTablicy, epsilon):
    x_srodek = (a + b) / 2
    while (abs(horner(x_srodek, wspolczynniki, dlugoscTablicy)) < epsilon):
        x_srodek = (a + b) / 2
        if (horner(x_srodek, wspolczynniki, dlugoscTablicy) * horner(b, wspolczynniki, dlugoscTablicy) < 0):
            a = x_srodek
        if (horner(x_srodek, wspolczynniki, dlugoscTablicy) * horner(a, wspolczynniki, dlugoscTablicy) < 0):
            b = x_srodek
    return x_srodek

def bisekcja_iteracje_wielomianu(a, b, wspolczynniki, dlugoscTablicy, iteracje):
    x_srodek = (a + b) / 2
    for i in range(iteracje):
        x_srodek = (a + b) / 2
        if (horner(x_srodek, wspolczynniki, dlugoscTablicy) * horner(b, wspolczynniki, dlugoscTablicy) < 0):
            a = x_srodek
        if (horner(x_srodek, wspolczynniki, dlugoscTablicy) * horner(a, wspolczynniki, dlugoscTablicy) < 0):
            b = x_srodek
    return x_srodek

def falsi_iteracje_wielomianu(a, b, wspolczynniki, dlugoscTablicy, iteracje):
    pierwiastek = 0
    for i in range(iteracje):
        if(horner(b, wspolczynniki, dlugoscTablicy) - horner(a, wspolczynniki, dlugoscTablicy)!=0):
            x0 = a - (horner(a, wspolczynniki, dlugoscTablicy) / (horner(b, wspolczynniki, dlugoscTablicy) - horner(a, wspolczynniki, dlugoscTablicy))) * (b - a)
            if (horner(x0, wspolczynniki, dlugoscTablicy) == 0):
                pierwiastek = x0
            if (horner(x0, wspolczynniki, dlugoscTablicy) * horner(b, wspolczynniki, dlugoscTablicy) < 0):
                a = x0
            if (horner(x0, wspolczynniki, dlugoscTablicy) * horner(a, wspolczynniki, dlugoscTablicy) < 0):
                b = x0
    return pierwiastek

def falsi_epsilon_wielomianu(a, b,  wspolczynniki, dlugoscTablicy, epsilon):
    # DZIELENIE PRZEZ ZERO
    if horner(b, wspolczynniki, dlugoscTablicy) - horner(a, wspolczynniki, dlugoscTablicy) == 0:
        return None
    x0 = a - (horner(a, wspolczynniki, dlugoscTablicy) / (horner(b, wspolczynniki, dlugoscTablicy) - horner(a, wspolczynniki, dlugoscTablicy))) * (b - a)
    while (abs(horner(x0, wspolczynniki, dlugoscTablicy)) >= epsilon):
        if(horner(b, wspolczynniki, dlugoscTablicy) - horner(a, wspolczynniki, dlugoscTablicy)!=0):
            x0 = a - (horner(a, wspolczynniki, dlugoscTablicy) / horner(b, wspolczynniki, dlugoscTablicy) - horner(a, wspolczynniki, dlugoscTablicy)) * (b - a)
        if (horner(x0, wspolczynniki, dlugoscTablicy) * horner(b, wspolczynniki, dlugoscTablicy) < 0):
            a = x0
        if (horner(x0, wspolczynniki, dlugoscTablicy) * horner(a, wspolczynniki, dlugoscTablicy) < 0):
            b = x0
    return x0