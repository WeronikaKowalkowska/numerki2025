import matplotlib.pyplot as plt
import numpy as np


# schemat hornera
def potega(podstawa, wykladnik):
    wynik = podstawa
    while (wykladnik - 1 > 0):
        wynik = wynik * podstawa
        wykladnik = wykladnik - 1
    return wynik


def horner(argument, wspolczynniki, dlugoscTablicy):
    wynik = 0
    n = 0
    for i in range(dlugoscTablicy - 1, - 1, -1):
        if (n != dlugoscTablicy - 1):
            wynik = wynik + potega(argument, i) * wspolczynniki[n]
            n = n + 1
        else:
            wynik = wynik + wspolczynniki[n]

    return wynik


x = np.linspace(-10, 10, 400)


def wyswietl_wielomian(wspolczynniki, dlugoscTablicy):
    y = horner(x, wspolczynniki, dlugoscTablicy)
    return wyswietl_wykres(y)


def wyswietl_funkcje(funkcja):
    y = funkcja(x)
    return wyswietl_wykres(y)


def wyswietl_wykres(y):
    plt.plot(x, y)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    return plt


def wyswietl_wynik_wielomianu(wspolczynniki, dlugoscTablicy, wynik):
    plot = wyswietl_wielomian(wspolczynniki, dlugoscTablicy)
    plot.scatter(wynik, horner(wynik, wspolczynniki, dlugoscTablicy), color='red', s=100)
    plot.show()


def wyswietl_wynik_funkcji(funkcja, wynik):
    plot = wyswietl_funkcje(funkcja)
    plot.scatter(wynik, funkcja(wynik), color='red', s=100)
    plot.show()


# metoda bisekcji
def bisekcja_epsilon(a, b, funkcja, epsilon):
    x_srodek = (a + b) / 2
    while (abs(funkcja(x_srodek)) < epsilon):
        x_srodek = (a + b) / 2
        if (funkcja(x_srodek) * funkcja(b) < 0):
            a = x_srodek
        if (funkcja(x_srodek) * funkcja(a) < 0):
            b = x_srodek

    return x_srodek


def bisekcja_iteracje(a, b, funkcja, iteracje):
    x_srodek = (a + b) / 2
    for i in range(iteracje):
        x_srodek = (a + b) / 2
        if (funkcja(x_srodek) * funkcja(b) < 0):
            a = x_srodek
        if (funkcja(x_srodek) * funkcja(a) < 0):
            b = x_srodek

    return x_srodek


# metoda falsi
def falsi_iteracje(a, b, funkcja, iteracje):
    pierwiastek = 0
    for i in range(iteracje):
        if(funkcja(b) - funkcja(a)!=0):
            x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
            if (funkcja(x0) == 0):
                pierwiastek = x0
            if (funkcja(x0) * funkcja(b) < 0):
                a = x0
            if (funkcja(x0) * funkcja(a) < 0):
                b = x0
    return pierwiastek


def falsi_epsilon(a, b, funkcja, epsilon):
    if (funkcja(b) - funkcja(a) != 0):
      x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
    else:
      x0 = a
    while (abs(funkcja(x0)) < epsilon):
        if(funkcja(b) - funkcja(a)!=0):
            x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
        if (funkcja(x0) * funkcja(b) < 0):
            a = x0
        if (funkcja(x0) * funkcja(a) < 0):
            b = x0
    return x0


# menu
# 1)WYBÓR FUNKCJI
funkcje_map = {
    'a': lambda x: x**3 + 5*x**2 - 2*x - 10,
    'b': lambda x: 3*x**3 + 3*x**2 - 18*x,
    'c': np.sin,
    'd': np.cos,
    'e': lambda x: 2**x,
    'f': lambda x: (1/2)**x,
    'g': lambda x: np.sin((1/2)*x),
    'h': lambda x: np.cos(2*x + 1)
}
test = True
print("Wybierz funkcję:")
print("\na) f(x) = x^3+5x^2−2x−10")
print("\nb) f(x) = 3x^3+3x^2-18x")
print("\nc) f(x) = sin(x)")
print("\nd) f(x) = cos(x)")
print("\ne) f(x) = 2^x")
print("\nf) f(x) = (1/2)^x")
print("\ng) f(x) = sin((1/2)x)")
print("\nh) f(x) = cos(2x+1)")
funkcja = 0
while (test):
    funkcja = input()
    if (ord(funkcja) >= 97 and ord(funkcja) <= 104 or ord(funkcja) >= 65 and ord(funkcja) <= 72):
        #funcFunkcja = funkcja
        test = False
    else:
        print("Niepoprawny wybór funkcji. Wybierz ponownie: ")
wybrana_funkcja=funkcje_map.get(funkcja.lower())
    # wyswietl wykres wybranej funkcji
if (funkcja == 'a' or funkcja == 'A'):
    wyswietl_wielomian([1, 5, -2, -10], 4).show()
if (funkcja == 'b' or funkcja == 'B'):
    wyswietl_wielomian([3, 3, -18, 0], 4).show()
if (funkcja == 'c' or funkcja == 'C'):
    wyswietl_funkcje(np.sin).show()
if (funkcja == 'd' or funkcja == 'D'):
    wyswietl_funkcje(np.cos).show()
if (funkcja == 'e' or funkcja == 'E'):
    wyswietl_funkcje(2 ** x).show()
if (funkcja == 'f' or funkcja == 'F'):
    wyswietl_funkcje(1 / 2 ** x).show()
if (funkcja == 'g' or funkcja == 'G'):
    wyswietl_funkcje(np.sin((1 / 2) * x)).show()
if (funkcja == 'h' or funkcja == 'H'):
    wyswietl_funkcje(np.cos(2 * x + 1)).show()

    # 2)WYBÓR PRZEDZIAŁU
    print("\nWybierz przedział określając jego krańce w postaci x1 i x2:")
x1 = 0
x2 = 0
while (test):
    x1 = int(input())
    x2 = int(input())
    if (x1 > 0 and x2 < 0 or x1 < 0 and x2 > 0):
        test = False
    else:
        print("\nBłędny przedział, podaj ponownie")
        test = True

# 3)WYBÓR KRYTERIUM ZATRZYMANIA
print("\nWybierz kryterium zatrzymania:")
print("\na) spełnienie warunku nałożonego na dokładność")
print("\nb) osiągnięcie zadanej liczby iteracji")
test = True
while (test):
    kryterium = input()

    # dokladnosc
    if (kryterium == 'a' or kryterium == 'A' or kryterium == 'b' or kryterium == 'B'):
        test2 = True
        if (kryterium == 'a' or kryterium == 'A'):
            print("\nPodaj Epsilon: ")
            while (test2):
                epsilon = float(input())
                if (epsilon > 0):
                    print("Wykonanie metody bisekcji: ")
                    x0_bisekcja_epsilon_wynik = bisekcja_epsilon(x1, x2, wybrana_funkcja, epsilon)
                    if (funkcja == 'a' or funkcja == 'A'):
                        wyswietl_wynik_wielomianu([1, 5, -2, -10], 4, x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'b' or funkcja == 'B'):
                        wyswietl_wielomian([3, 3, -18, 0], 4, x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'c' or funkcja == 'C'):
                        wyswietl_wynik_funkcji(np.sin, x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'd' or funkcja == 'D'):
                        wyswietl_wynik_funkcji(np.cos, x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'e' or funkcja == 'E'):
                        wyswietl_wynik_funkcji(2 ** x, x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'f' or funkcja == 'F'):
                        wyswietl_wynik_funkcji(1 / 2 ** x, x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'g' or funkcja == 'G'):
                        wyswietl_wynik_funkcji(np.sin((1 / 2) * x), x0_bisekcja_epsilon_wynik)
                    if (funkcja == 'h' or funkcja == 'H'):
                        wyswietl_wynik_funkcji(np.cos(2 * x + 1), x0_bisekcja_epsilon_wynik)
                print("Wykonanie metody regula falsi:")
                x0_falsi_epsilon = falsi_epsilon(x1, x2, wybrana_funkcja, epsilon)
                if (funkcja == 'a' or funkcja == 'A'):
                    wyswietl_wynik_wielomianu([1, 5, -2, -10], 4, x0_falsi_epsilon)
                if (funkcja == 'b' or funkcja == 'B'):
                    wyswietl_wielomian([3, 3, -18, 0], 4, x0_falsi_epsilon)
                if (funkcja == 'c' or funkcja == 'C'):
                    wyswietl_wynik_funkcji(np.sin, x0_falsi_epsilon)
                if (funkcja == 'd' or funkcja == 'D'):
                    wyswietl_wynik_funkcji(np.cos, x0_falsi_epsilon)
                if (funkcja == 'e' or funkcja == 'E'):
                    wyswietl_wynik_funkcji(2 ** x, x0_falsi_epsilon)
                if (funkcja == 'f' or funkcja == 'F'):
                    wyswietl_wynik_funkcji(1 / 2 ** x, x0_falsi_epsilon)
                if (funkcja == 'g' or funkcja == 'G'):
                    wyswietl_wynik_funkcji(np.sin((1 / 2) * x), x0_falsi_epsilon)
                if (funkcja == 'h' or funkcja == 'H'):
                    wyswietl_wynik_funkcji(np.cos(2 * x + 1), x0_falsi_epsilon)
                test2 = False
        else:
            print("\nBłędne dane, podaj ponownie")
            test2 = True

# iteracje
if (kryterium == 'b' or kryterium == 'B'):
    print("\nPodaj liczbę iteracji: ")
    test2 = True
    while (test2):
        iteracje = input()
        if (iteracje.isdigit() and int(iteracje) > 0):
            print("Wykonanie metody bisekcji: ")
            bisekcja_iteracje(x1, x2, funkcja, int(iteracje))
            print("Wykonanie metody regula falsi:")
            falsi_iteracje(x1, x2, funkcja, int(iteracje))
            test2 = False
        else:
            print("\nBłędne dane, podaj ponownie")
            test2 = True

    test = False
else:
    print("\nBłędne kryterium, podaj ponownie")
    test = True
