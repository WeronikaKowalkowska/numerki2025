from funkcje import *

x = np.linspace(-20, 20, 400)

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
    literka = input("Wybrano: ")
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
    wyswietl_funkcje(x,funkcja).show()

# 3) WYBÓR PRZEDZIAŁU
print("\nWybierz przedział określając jego krańce w postaci x1 i x2:")
x1 = 0
x2 = 0
test=True
while (test):
    x1 = int(input("Wybrano x1: "))
    x2 = int(input("Wybrano x2: "))
    if (x1 < 0 and x2 > 0):
        test = False
    else:
        print("Błędny przedział, podaj ponownie")
        test = True

x = np.linspace(x1-10, x2+10, 400)

# 4) WYBÓR KRYTERIUM ZATRZYMANIA
print("\nWybierz kryterium zatrzymania:")
print("a) spełnienie warunku nałożonego na dokładność")
print("b) osiągnięcie zadanej liczby iteracji")
test = True
while (test):
    kryterium = input("Wybrano: ")
    # DOKŁADNOŚĆ
    if (kryterium == 'a' or kryterium == 'A' or kryterium == 'b' or kryterium == 'B'):
        test2 = True
        if (kryterium == 'a' or kryterium == 'A'):
            print("\nPodaj Epsilon: ")
            while (test2):
                epsilon = float(input("Wybrano: "))
                if (epsilon > 0):
                    if literka == 'a' or literka == 'A':
                        x0_bisekcja_epsilon_wynik=bisekcja_epsilon_wielomianu(x1, x2, [1, 5, -2, -10], 4, epsilon)
                    elif literka == 'b' or literka == 'B':
                        x0_bisekcja_epsilon_wynik = bisekcja_epsilon_wielomianu(x1, x2, [3, 3, -18, 0], 4, epsilon)
                    else:
                        x0_bisekcja_epsilon_wynik = bisekcja_epsilon(x1, x2, funkcja, epsilon)
                    print("Wynik wykonanika metody bisekcji przy kryterium wybranej dokładności to: ", x0_bisekcja_epsilon_wynik)
                    if literka == 'a' or literka == 'A':
                        x0_falsi_epsilon_wynik = falsi_epsilon_wielomianu(x1, x2, [1, 5, -2, -10], 4, epsilon)
                    elif literka == 'b' or literka == 'B':
                        x0_falsi_epsilon_wynik = falsi_epsilon_wielomianu(x1, x2, [3, 3, -18, 0], 4, epsilon)
                    else:
                        x0_falsi_epsilon_wynik = falsi_epsilon(x1, x2, funkcja, epsilon)
                    print("Wynik wykonanika metody falsi przy kryterium wybranej dokładności to: ", x0_falsi_epsilon_wynik)
                    print("Zakończono wykonanie obu metod przy kryterium wybranej dokładności.")
                    # WYŚWIETLENIE WYKRESÓW KOŃCOWYCH
                    if literka == 'a' or literka == 'A':
                        wyswietl_wynik_wielomianu(x, [1, 5, -2, -10], 4, x0_bisekcja_epsilon_wynik, x0_falsi_epsilon_wynik)
                        test2 = False
                    elif literka == 'b' or literka == 'B':
                        wyswietl_wynik_wielomianu(x, [3, 3, -18, 0], 4, x0_bisekcja_epsilon_wynik, x0_falsi_epsilon_wynik)
                        test2 = False
                    else:
                        wyswietl_wynik_funkcji(x,funkcja, x0_bisekcja_epsilon_wynik, x0_falsi_epsilon_wynik)
                        test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True
        # ITERACJE
        if (kryterium == 'b' or kryterium == 'B'):
            print("\nPodaj liczbę iteracji: ")
            test2 = True
            while (test2):
                iteracje = input("Wybrano: ")
                if iteracje.isdigit() and int(iteracje) > 0:
                    if literka == 'a' or literka == 'A':
                        x0_bisekcja_iteracje_wynik = bisekcja_iteracje_wielomianu(x1, x2, [1, 5, -2, -10], 4, int(iteracje))
                    elif literka == 'b' or literka == 'B':
                        x0_bisekcja_iteracje_wynik = bisekcja_iteracje_wielomianu(x1, x2, [3, 3, -18, 0], 4, int(iteracje))
                    else:
                        x0_bisekcja_iteracje_wynik = bisekcja_iteracje(x1, x2, funkcja, int(iteracje))
                    print("Wynik wykonanika metody bisekcji przy kryterium określonej ilości iteracji to: ", x0_bisekcja_iteracje_wynik)
                    if literka == 'a' or literka == 'A':
                        x0_falsi_iteracje_wynik = falsi_iteracje_wielomianu(x1, x2, [1, 5, -2, -10], 4, int(iteracje))
                    elif literka == 'b' or literka == 'B':
                        x0_falsi_iteracje_wynik = falsi_iteracje_wielomianu(x1, x2, [3, 3, -18, 0], 4, int(iteracje))
                    else:
                        x0_falsi_iteracje_wynik = falsi_iteracje(x1, x2, funkcja, int(iteracje))
                    print("Wynik wykonanika metody falsi przy kryterium określonej ilości iteracji to: ", x0_falsi_iteracje_wynik)
                    print("Zakończono wykonanie obu metod przy kryterium określonej ilości iteracji.")
                    # WYŚWIETLENIE WYKRESÓW KOŃCOWYCH
                    if literka == 'a' or literka == 'A':
                        wyswietl_wynik_wielomianu(x, [1, 5, -2, -10], 4, x0_bisekcja_iteracje_wynik,  x0_falsi_iteracje_wynik)
                        test2 = False
                    elif literka == 'b' or literka == 'B':
                        wyswietl_wynik_wielomianu(x, [3, 3, -18, 0], 4, x0_bisekcja_iteracje_wynik, x0_falsi_iteracje_wynik)
                        test2 = False
                    else:
                        wyswietl_wynik_funkcji(x,funkcja, x0_bisekcja_iteracje_wynik, x0_falsi_iteracje_wynik)
                        test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True
        test = False
    else:
        print("\nBłędne dane, podaj ponownie")
        test = True