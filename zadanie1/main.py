from bisekcja import *
from falsi import *
from wykresy import *
from funkcje import *

x = np.linspace(-20, 20, 400)       #zmienna służąca rozmieszczeniu punktów na osi OX wyświetlanych wykresów

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

test = True     #zmienna sprawdzająca poprwaność input
literka = ""        #znak określający wybór funkcji podany przez użytkownika
while test:
    literka = input("Wybrano: ")
    literka = literka.lower()       #zapewnienie odczytu jako mała litera
    if 97<=ord(literka)<=104:
        test = False
    else:
        print("Niepoprawny wybór funkcji. Wybierz ponownie: ")

funkcja = wybor_funkcji(literka)        #przypisanie funkcji wyboru użytkownika

# 2) WYŚWIETLENIE WYKRESU WYBRANEJ FUNKCJI
if literka == 'a':
    wyswietl_wielomian(x,[1, 5, -2, -10]).show()
elif literka == 'b':
    wyswietl_wielomian(x, [3, 3, -18, 0]).show()
else:
    wyswietl_funkcje(x,funkcja).show()

# 3) WYBÓR PRZEDZIAŁU
print("\nWybierz przedział określając jego krańce w postaci x1 i x2:")
x1 = 0
x2 = 0
test=True
while test:
    x1 = float(input("Wybrano x1: "))
    x2 = float(input("Wybrano x2: "))
    if x1 < 0 < x2:
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
while test:
    kryterium = input("Wybrano: ")
    kryterium = kryterium.lower()
    # DOKŁADNOŚĆ
    if kryterium == 'a'or kryterium == 'b':
        test2 = True
        if kryterium == 'a':
            print("\nPodaj Epsilon: ")
            while test2:
                epsilon = float(input("Wybrano: "))
                if epsilon > 0:
                    #BISEKCJA
                    if literka == 'a':
                                #przeprowadzenie bieskcji dla pierwszej funkcji wielomianowej dla zadanej dokładności
                        x0_bisekcja_epsilon_wynik=bisekcja(x1,x2, [1, 5, -2, -10],epsilon,None,'a',True,None)
                    elif literka == 'b':
                                # przeprowadzenie bieskcji dla drugiej funkcji wielomianowej dla zadanej dokładności
                        x0_bisekcja_epsilon_wynik = bisekcja(x1, x2, [3, 3, -18, 0], epsilon, None, 'a', True, None)
                    else:
                                # przeprowadzenie bieskcji dla pozostałych funkcji dla zadanej dokładności
                         x0_bisekcja_epsilon_wynik = bisekcja(x1, x2,None, epsilon, 0, 'a', False, funkcja)
                    print("Wynik wykonanika metody bisekcji przy kryterium wybranej dokładności to: ", x0_bisekcja_epsilon_wynik)

                    #FALSI
                    if literka == 'a':
                                # przeprowadzenie regula falsi dla pierwszej funkcji wielomianowej dla zadanej dokładności
                        x0_falsi_epsilon_wynik =falsi(x1,x2, [1, 5, -2, -10], epsilon, None, 'a', True,None)
                    elif literka == 'b':
                                # przeprowadzenie regula falsi dla drugiej funkcji wielomianowej dla zadanej dokładności
                        x0_falsi_epsilon_wynik = falsi(x1, x2, [3, 3, -18, 0], epsilon, None, 'a', True, None)
                    else:
                                # przeprowadzenie regula falsi dla pozostałych funkcji dla zadanej dokładności
                        x0_falsi_epsilon_wynik =falsi(x1, x2,None, epsilon, 0, 'a', False, funkcja)
                    print("Wynik wykonanika metody falsi przy kryterium wybranej dokładności to: ", x0_falsi_epsilon_wynik)

                    print("Zakończono wykonanie obu metod przy kryterium wybranej dokładności.")
                    # WYŚWIETLENIE WYKRESÓW KOŃCOWYCH NA WSPÓLNYM WYKRESIE
                    wyswietl_ogolne_wyniki(literka,x,x0_bisekcja_epsilon_wynik,x0_falsi_epsilon_wynik,funkcja)
                    test2= False        #zakończenie programu
                else:
                    print("\nBłędne dane, podaj ponownie. Dokładność musi być dodatnia:")
                    test2 = True        #ponowienie wyborów
        # ITERACJE
        if kryterium == 'b':
            print("\nPodaj liczbę iteracji: ")
            test2 = True
            while test2:
                iteracje = input("Wybrano: ")
                if iteracje.isdigit() and int(iteracje) > 0:
                    #BISEKCJA
                    if literka == 'a' :
                              # przeprowadzenie bieskcji dla pierwszej funkcji wielomianowej dla wybranej liczby iteracji
                        x0_bisekcja_iteracje_wynik=bisekcja(x1,x2,[1, 5, -2, -10],None,int(iteracje),'b',True,None)
                    elif literka == 'b':
                              # przeprowadzenie bieskcji dla drugiej funkcji wielomianowej dla wybranej liczby iteracji
                        x0_bisekcja_iteracje_wynik = bisekcja(x1, x2, [3, 3, -18, 0], None, int(iteracje), 'b', True, None)
                    else:
                                # przeprowadzenie bieskcji dla pozostałych funkcji dla wybranej liczby iteracji
                        x0_bisekcja_iteracje_wynik = bisekcja(x1, x2, None, None, int(iteracje), 'b', False, funkcja)
                    print("Wynik wykonanika metody bisekcji przy kryterium określonej ilości iteracji to: ", x0_bisekcja_iteracje_wynik)

                    #FALSI
                    if literka == 'a':
                                # przeprowadzenie regula falsi dla pierwszej funkcji wielomianowej dla wybranej liczby iteracji
                        x0_falsi_iteracje_wynik=falsi(x1, x2, [1, 5, -2, -10], None, int(iteracje), 'b', True, None)
                    elif literka == 'b':
                               # przeprowadzenie regula falsi dla drugiej funkcji wielomianowej dla wybranej liczby iteracji
                        x0_falsi_iteracje_wynik=falsi(x1, x2, [3, 3, -18, 0], None, int(iteracje), 'b', True, None)
                    else:
                                # przeprowadzenie regula falsi dla pozostałych funkcji dla wybranej liczby iteracji
                        x0_falsi_iteracje_wynik=falsi(x1, x2, None, None, int(iteracje), 'b', False, funkcja)
                    print("Wynik wykonanika metody falsi przy kryterium określonej ilości iteracji to: ", x0_falsi_iteracje_wynik)

                    print("Zakończono wykonanie obu metod przy kryterium określonej ilości iteracji.")
                    # WYŚWIETLENIE WYKRESÓW KOŃCOWYCH
                    wyswietl_ogolne_wyniki(literka, x, x0_bisekcja_iteracje_wynik, x0_falsi_iteracje_wynik, funkcja)
                    test2 = False       #zakończenie programu
                else:
                    print("\nBłędne dane, podaj ponownie. Liczba iteracji musi być naturalna: ")
                    test2 = True        #ponowienie wyborów
        test = False
    else:
        print("\nBłędne dane, podaj ponownie")
        test = True