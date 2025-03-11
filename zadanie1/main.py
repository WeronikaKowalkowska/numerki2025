import matplotlib.pyplot as plt
import numpy as np

from funkcje import wybor_funkcji


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

x = np.linspace(-50, 50, 400)
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

def wyswietl_wynik_wielomianu(wspolczynniki, dlugoscTablicy, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_wielomian(wspolczynniki, dlugoscTablicy)
    plot.scatter(wynik_bisekcji, horner(wynik_bisekcji, wspolczynniki, dlugoscTablicy), color='red', s=100, marker='o')
    plot.scatter(wynik_falsi, horner(wynik_falsi, wspolczynniki, dlugoscTablicy), color='red', s=100, marker='x')
    plot.show()

def wyswietl_wynik_funkcji(funkcja, wynik_bisekcji, wynik_falsi):
    plot = wyswietl_funkcje(funkcja)
    plot.scatter(wynik_bisekcji, funkcja(wynik_bisekcji), color='red', s=100, marker='o')
    plot.scatter(wynik_falsi, funkcja(wynik_falsi), color='pink', s=100, marker='x')
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

# 1)WYBÓR FUNKCJI
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

funkcja=wybor_funkcji(literka)

#wybrana_funkcja=funkcje_map.get(funkcja)
# wyswietl wykres wybranej funkcji
if (literka == 'a' or literka == 'A'):
    wyswietl_wielomian([1, 5, -2, -10], 4).show()
if (literka == 'b' or literka == 'B'):
    wyswietl_wielomian([3, 3, -18, 0], 4).show()
if (literka == 'c' or literka == 'C'):
    wyswietl_funkcje(np.sin).show()
if (literka == 'd' or literka == 'D'):
    wyswietl_funkcje(np.cos).show()
if (literka == 'e' or literka == 'E'):
    wyswietl_funkcje(lambda x: 2**x).show()
if (literka == 'f' or literka == 'F'):
    wyswietl_funkcje(lambda x: (1/2)**x).show()
if (literka == 'g' or literka == 'G'):
    wyswietl_funkcje(lambda x: np.sin((1/2)*x)).show()
if (literka == 'h' or literka == 'H'):
    wyswietl_funkcje(lambda x: np.cos(2*x + 1)).show()

# 2)WYBÓR PRZEDZIAŁU
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

# 3)WYBÓR KRYTERIUM ZATRZYMANIA
print("\nWybierz kryterium zatrzymania:")
print("a) spełnienie warunku nałożonego na dokładność")
print("b) osiągnięcie zadanej liczby iteracji")
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
                    x0_bisekcja_epsilon_wynik = bisekcja_epsilon(x1, x2, funkcja, epsilon)
                    print("Wykonanie metody regula falsi:")
                    x0_falsi_epsilon = falsi_epsilon(x1, x2, funkcja, epsilon)
                    print("Wykonano metody")
                if (literka == 'a' or literka == 'A'):
                    wyswietl_wynik_wielomianu([1, 5, -2, -10], 4,x0_bisekcja_epsilon_wynik, x0_falsi_epsilon)
                if (literka == 'b' or literka == 'B'):
                    wyswietl_wynik_wielomianu([3, 3, -18, 0], 4,x0_bisekcja_epsilon_wynik, x0_falsi_epsilon)
                else:
                    wyswietl_wynik_funkcji(funkcja,x0_bisekcja_epsilon_wynik, x0_falsi_epsilon )
                test2 = False
        # iteracje
        if (kryterium == 'b' or kryterium == 'B'):
            print("\nPodaj liczbę iteracji: ")
            test2 = True
            while (test2):
                iteracje = input()
                if (iteracje.isdigit() and int(iteracje) > 0):
                    print("Wykonanie metody bisekcji: ")
                    x0_bisekcja_iteracje_wynik=bisekcja_iteracje(x1, x2, funkcja, int(iteracje))
                    wyswietl_wynik_funkcji(funkcja,x0_bisekcja_iteracje_wynik)
                    print("Wykonanie metody regula falsi:")
                    x0_falsi_iteracje_wynik=falsi_iteracje(x1, x2, funkcja, int(iteracje))
                    wyswietl_wynik_funkcji(funkcja, x0_falsi_iteracje_wynik)
                    test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True

            test = False

        else:
            print("Błędne dane, podaj ponownie")
            test2 = True
        test=False

