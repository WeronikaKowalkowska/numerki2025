
# metoda bisekcji

# metoda falsi

# menu
# 1)WYBÓR FUNKCJI
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
while (test):
    funkcja = input()
    if (ord(funkcja) >= 97 and ord(funkcja) <= 104 or ord(funkcja) >= 65 and ord(funkcja) <= 72):
        test = False
    else:
        print("Niepoprawny wybór funkcji. Wybierz ponownie: ")

    # wyswietl wykres wybranej funkcji

    # 2)WYBÓR PRZEDZIAŁU
    print("\nWybierz przedział określając jego krańce w postaci x1 i x2:")
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
    if (kryterium == 'a' or kryterium == 'A' or kryterium == 'b' or kryterium == 'B'):
        test2 = True
        if (kryterium == 'a' or kryterium == 'A'):
            print("\nPodaj Epsilon: ")
            while (test2):
                epsilon = int(input())
                if (epsilon > 0):
                    test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True

        if (kryterium == 'b' or kryterium == 'B'):
            print("\nPodaj liczbę iteracji: ")
            test2 = True
            while (test2):
                iteracje = int(input())
                if (iteracje > 0 and iteracje %1 == 0):
                    test2 = False
                else:
                    print("\nBłędne dane, podaj ponownie")
                    test2 = True

            test = False
        else:
            print("\nBłędne kryterium, podaj ponownie")
            test = True

# schemat hornera
def potega(podstawa ,wykladnik):
    wynik =podstawa
    while(wykladnik - 1 >0):
        wynik =wynik *podstawa
        wykladnik =wykladnik -1
    return wynik

def horner(argument, wspolczynniki, dlugoscTablicy):
    wynik = 0
    n=0
    for i in range(dlugoscTablicy -1, - 1, -1):
        if(n!= dlugoscTablicy-1):
            wynik = wynik + potega(argument, i) * wspolczynniki[n]
            n = n + 1
        else:
            wynik = wynik + wspolczynniki[n]

    return wynik
