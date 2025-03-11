import matplotlib.pyplot as plt
import numpy as np

from funkcje import wybor_funkcji
from wielomiany import *

x = np.linspace(-50, 50, 400)

def wyswietl_funkcje(funkcja):
    y = funkcja(x)
    return wyswietl_wykres(x, y)

def wyswietl_wynik_funkcji(funkcja, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_funkcje(funkcja)
    plot.scatter(wynik_bisekcji, funkcja(wynik_bisekcji), color='red', s=100, marker='o', label="Bisekcja")
    plot.scatter(wynik_falsi, funkcja(wynik_falsi), color='blue', s=100, marker='x', label="Metoda falsi")
    plt.legend()
    plot.show()

# METODA BISEKCJI
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

# METODA FALSI
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

# 1) WYBÓR FUNKCJI
print("Wybierz funkcję:")
print("a) f(x) = x^3+5x^2−2x−10")
print("b) f(x) = 3x^3+3x^2-18x")
print("c) f(x) = sin(x)")
print("d) f(x) = cos(x)")
print("e) f(x) = 2^x")
print("f) f(x) = (1/2)^x")
print("g) f(x) = sin((1/2)x)")
print("h) f(x) = cos(2x+1)")

test = True
literka = ""
while (test):
    literka = input()
    if (ord(literka) >= 97 and ord(literka) <= 104 or ord(literka) >= 65 and ord(literka) <= 72):
        test = False
    else:
        print("Niepoprawny wybór funkcji. Wybierz ponownie: ")

funkcja = wybor_funkcji(literka)

# 2) WYŚWIETLENIE WYKRESU WYBRANEJ FUNKCJI
if (literka == 'a' or literka == 'A'):
    wyswietl_wielomian(x,[1, 5, -2, -10], 4).show()
elif (literka == 'b' or literka == 'B'):
    wyswietl_wielomian(x, [3, 3, -18, 0], 4).show()
else:
    wyswietl_funkcje(funkcja).show()

# 3) WYBÓR PRZEDZIAŁU
print("\nWybierz przedział określając jego krańce w postaci x1 i x2:")
x1 = 0
x2 = 0
test=True
while (test):
    x1 = int(input())
    x2 = int(input())
    if (x1 > 0 and x2 < 0 or x1 < 0 and x2 > 0):
        test = False
    else:
        print("Błędny przedział, podaj ponownie")
        test = True

# 4) WYBÓR KRYTERIUM ZATRZYMANIA
print("\nWybierz kryterium zatrzymania:")
print("a) spełnienie warunku nałożonego na dokładność")
print("b) osiągnięcie zadanej liczby iteracji")
test = True
while (test):
    kryterium = input()
    # DOKŁADNOŚĆ
    if (kryterium == 'a' or kryterium == 'A' or kryterium == 'b' or kryterium == 'B'):
        test2 = True
        if (kryterium == 'a' or kryterium == 'A'):
            print("\nPodaj Epsilon: ")
            while (test2):
                epsilon = float(input())
                if (epsilon > 0):
                    print("Wykonanie metody bisekcji")
                    if literka == 'a' or literka == 'A':
                        x0_bisekcja_epsilon_wynik=bisekcja_epsilon_wielomianu(x1, x2, [1, 5, -2, -10], 4, epsilon)
                    elif literka == 'b' or literka == 'B':
                        x0_bisekcja_epsilon_wynik = bisekcja_epsilon_wielomianu(x1, x2, [3, 3, -18, 0], 4, epsilon)
                    else:
                        x0_bisekcja_epsilon_wynik = bisekcja_epsilon(x1, x2, funkcja, epsilon)
                    print("Wykonanie metody regula falsi")
                    if literka == 'a' or literka == 'A':
                        x0_falsi_epsilon_wynik = falsi_epsilon_wielomianu(x1, x2, [1, 5, -2, -10], 4, epsilon)
                    elif literka == 'b' or literka == 'B':
                        x0_falsi_epsilon_wynik = falsi_epsilon_wielomianu(x1, x2, [3, 3, -18, 0], 4, epsilon)
                    else:
                        x0_falsi_epsilon_wynik = falsi_epsilon(x1, x2, funkcja, epsilon)
                    print("Wykonano metody")
                    # WYŚWIETLENIE WYKRESÓW KOŃCOWYCH
                    if literka == 'a' or literka == 'A':
                        wyswietl_wynik_wielomianu(x, [1, 5, -2, -10], 4, x0_bisekcja_epsilon_wynik, x0_falsi_epsilon_wynik)
                        test2 = False
                    elif literka == 'b' or literka == 'B':
                        wyswietl_wynik_wielomianu(x, [3, 3, -18, 0], 4, x0_bisekcja_epsilon_wynik, x0_falsi_epsilon_wynik)
                        test2 = False
                    else:
                        wyswietl_wynik_funkcji(funkcja, x0_bisekcja_epsilon_wynik, x0_falsi_epsilon_wynik)
                        test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True
        # ITERACJE
        if (kryterium == 'b' or kryterium == 'B'):
            print("\nPodaj liczbę iteracji: ")
            test2 = True
            while (test2):
                iteracje = input()
                if iteracje.isdigit() and int(iteracje) > 0:
                    print("Wykonanie metody bisekcji")
                    if literka == 'a' or literka == 'A':
                        x0_bisekcja_iteracje_wynik = bisekcja_iteracje_wielomianu(x1, x2, [1, 5, -2, -10], 4, int(iteracje))
                    elif literka == 'b' or literka == 'B':
                        x0_bisekcja_iteracje_wynik = bisekcja_iteracje_wielomianu(x1, x2, [3, 3, -18, 0], 4, int(iteracje))
                    else:
                        x0_bisekcja_iteracje_wynik = bisekcja_iteracje(x1, x2, funkcja, int(iteracje))
                    print("Wykonanie metody regula falsi")
                    if literka == 'a' or literka == 'A':
                        x0_falsi_iteracje_wynik = falsi_iteracje_wielomianu(x1, x2, [1, 5, -2, -10], 4, int(iteracje))
                    elif literka == 'b' or literka == 'B':
                        x0_falsi_iteracje_wynik = falsi_iteracje_wielomianu(x1, x2, [3, 3, -18, 0], 4, int(iteracje))
                    else:
                        x0_falsi_iteracje_wynik = falsi_iteracje(x1, x2, funkcja, int(iteracje))
                    # WYŚWIETLENIE WYKRESÓW KOŃCOWYCH
                    if literka == 'a' or literka == 'A':
                        wyswietl_wynik_wielomianu(x, [1, 5, -2, -10], 4, x0_bisekcja_iteracje_wynik,  x0_falsi_iteracje_wynik)
                        test2 = False
                    elif literka == 'b' or literka == 'B':
                        wyswietl_wynik_wielomianu(x, [3, 3, -18, 0], 4, x0_bisekcja_iteracje_wynik, x0_falsi_iteracje_wynik)
                        test2 = False
                    else:
                        wyswietl_wynik_funkcji(funkcja, x0_bisekcja_iteracje_wynik, x0_falsi_iteracje_wynik)
                        test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True
        test = False
    else:
        print("Błędne dane, podaj ponownie")
        test = True