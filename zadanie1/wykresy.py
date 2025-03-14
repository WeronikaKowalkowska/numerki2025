from matplotlib import pyplot as plt

from metody import horner

def wyswietl_funkcje(x,funkcja):
    y = funkcja(x)
    return wyswietl_wykres(x, y)

def wyswietl_wynik_funkcji(x,funkcja, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_funkcje(x,funkcja)
    plot.scatter(wynik_bisekcji, funkcja(wynik_bisekcji), color='yellow', s=100, marker='o', label="Bisekcja")
    plot.scatter(wynik_falsi, funkcja(wynik_falsi), color='magenta', s=100, marker='x', label="Metoda falsi")
    plt.legend()
    plot.show()

def wyswietl_wielomian(x, wspolczynniki):
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

def wyswietl_wynik_wielomianu(x, wspolczynniki, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_wielomian(x, wspolczynniki)
    plot.scatter(wynik_bisekcji, horner(wynik_bisekcji, wspolczynniki), color='yellow', s=100, marker='o',
                 label="Bisekcja")
    plot.scatter(wynik_falsi, horner(wynik_falsi, wspolczynniki), color='magenta', s=100, marker='x',
                 label="Metoda falsi")
    plot.legend()
    plot.title("Wykres funkcji:")
    plot.show()