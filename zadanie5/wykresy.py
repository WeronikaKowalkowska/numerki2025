from matplotlib import pyplot as plt
from horner import *
import numpy as np


def wyswietl_funkcje(x, funkcja):
    y = funkcja(x) / np.sqrt(1 - x ** 2)
    return wyswietl_wykres(x, y)


def wyswietl_wielomian(x, wspolczynniki):
    y = []
    for i in range(len(x)):
        if -1 < x[i] < 1:
            try:
                y.append(horner(x[i], wspolczynniki) / np.sqrt(1 - x[i] ** 2))
            except FloatingPointError:
                print("Błąd: sqrt z liczby ujemnej. Sprawdź zakres x.")
        else:
            print(f"x = {x[i]} poza zakresem <-1, 1>, pomijam.")
            y.append(np.nan)
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


def wyswietl_aproksymacje(x, y):
    print("x aproksymacje: ")
    print(x)
    print("y aproksymacje: ")
    print(y)
