from matplotlib import pyplot as plt
from helper import *
import numpy as np


def wyswietl_funkcje(x, funkcja):
    with np.errstate(divide='ignore', invalid='ignore'):
        y = funkcja(x) / np.sqrt(1 - x ** 2)
    return wyswietl_wykres(x, y, "Wykres funkcji:")


def wyswietl_wielomian(x, wspolczynniki):
    y = []
    for i in range(len(x)):
        if -1 < x[i] < 1:
            try:
                y.append(horner(x[i], wspolczynniki)/ np.sqrt(1 - x[i] ** 2))
            except FloatingPointError:
                print("Błąd: sqrt z liczby ujemnej. Sprawdź zakres x.")
        else:
            print(f"x = {x[i]} poza zakresem <-1, 1>, pomijam.")
            y.append(np.nan)
    return wyswietl_wykres(x, y, "Wykres funkcji:")


def wyswietl_wykres(x, y, text):
    plt.plot(x, y, color="pink")
    plt.title(text)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(-1, 1)
    plt.ylim(-10, 10)
    plt.subplots_adjust(left=0.15)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    return plt


def wyswietl_aproksymacje(x, y):
    return wyswietl_wykres(x, y, "Wykres wielomianu aproksymacyjnego:")


def wyswietl_wielomian_aproksymacjyny_sformatowany(wspolczynniki):
    stopien = len(wspolczynniki) - 1
    wynik = ""
    for i, wsp in enumerate(wspolczynniki):
        potega = stopien - i
        if abs(wsp) < 1e-6:  # pomiń zerowe współczynniki
            continue
        znak = " + " if wsp > 0 else " - "
        wsp_abs = abs(wsp)
        if wynik == "":
            znak = "-" if wsp < 0 else ""
        if potega > 1:
            wynik += f"{znak}{wsp_abs:.5f} x^{potega}"
        elif potega == 1:
            wynik += f"{znak}{wsp_abs:.5f} x"
        else:
            wynik += f"{znak}{wsp_abs:.5f}"
    print("Wielomian aproksymujący:\n" + wynik)
