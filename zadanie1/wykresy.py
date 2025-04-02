from matplotlib import pyplot as plt
from funkcje import horner

#funkcja wyświetlająca wykres funkcji c-h bez zaznaczonego miejsca zerowego
def wyswietl_funkcje(x, funkcja):
    y = funkcja(x)
    return wyswietl_wykres(x, y)

#funkcja wyświetlająca wykres funkcji c-h wraz z miejscem zerowym
def wyswietl_wynik_funkcji(x, funkcja, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_funkcje(x, funkcja)
    plot.scatter(wynik_bisekcji, funkcja(wynik_bisekcji), color='green', s=100, marker='o', label="Bisekcja")
    plot.scatter(wynik_falsi, funkcja(wynik_falsi), color='magenta', s=100, marker='x', label="Metoda falsi")
    plt.legend()
    plot.show()

#funkcja wyświetlająca wykres funkcji wielomianowej bez zaznaczonego miejsca zerowego
def wyswietl_wielomian(x, wspolczynniki):
    y = []
    for i in range(len(x)):
        y.append(horner(x[i], wspolczynniki))
    return wyswietl_wykres(x, y)

#funkcja wyświetlająca wykres funkcji wielomianowej wraz z miejscem zerowym
def wyswietl_wynik_wielomianu(x, wspolczynniki, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_wielomian(x, wspolczynniki)
    plot.scatter(wynik_bisekcji, horner(wynik_bisekcji, wspolczynniki), color='green', s=100, marker='o',
                 label="Bisekcja")
    plot.scatter(wynik_falsi, horner(wynik_falsi, wspolczynniki), color='magenta', s=100, marker='x',
                 label="Metoda falsi")
    plot.legend()
    plot.title("Wykres funkcji:")
    plot.show()

#funkcja zbiorcza realizująca wyświetlenie wykresu
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

#funkcja realizująca wyświetlenie końcowych wyników dla wszystkich wbudowanych funkcji
def wyswietl_ogolne_wyniki(literka, x, wynik_bisekcja, wynik_falsi,funkcja):
    if literka == 'a':
        wyswietl_wynik_wielomianu(x, [1, 5, -2, -10], wynik_bisekcja, wynik_falsi)
    elif literka == 'b':
        wyswietl_wynik_wielomianu(x, [3, 3, -18, 0], wynik_bisekcja, wynik_falsi)
    else:
        wyswietl_wynik_funkcji(x, funkcja, wynik_bisekcja, wynik_falsi)



