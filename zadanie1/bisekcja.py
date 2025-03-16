from funkcje import *

#realizacja bisekcji dla funkcji c-h
def bisekcja_funkcji(a,b,funkcja,x_srodek):
    x_srodek, a, b=sprawdz_warunki(funkcja,x_srodek,a,b)
    return x_srodek,a,b

#ogólna realizacja bisekcji dla wszystkich wbudowanych funkcji
def bisekcja(a, b, wspolczynniki, epsilon,iteracje, kryterium, czy_wielomian,funkcja):
    ile_iteracji = 0
    if czy_wielomian:
        #dokładność
        if kryterium == 'a':
            x_srodek = (a + b) / 2
            if abs(horner(x_srodek, wspolczynniki)) < epsilon:
                return x_srodek, 1
            while abs(horner((a + b) / 2, wspolczynniki)) >= epsilon:
                x_srodek,a,b=sprawdz_warunki_wielomianu(a, b, wspolczynniki, (a + b)/2)
                ile_iteracji += 1
            return x_srodek, ile_iteracji
        # iteracje
        else:
            x_srodek = 0
            for i in range(iteracje):
                x_srodek,a,b = sprawdz_warunki_wielomianu(a, b, wspolczynniki, (a + b)/2)
            return x_srodek, iteracje
    else:
        #dokładność
        if kryterium == 'a':
            x_srodek = (a + b) / 2
            if abs(funkcja(x_srodek)) < epsilon:
                return x_srodek, 1
            while abs(funkcja(x_srodek)) >= epsilon:
                x_srodek,a,b=bisekcja_funkcji(a,b,funkcja,(a + b)/2)
                ile_iteracji += 1
            return x_srodek, ile_iteracji
        #iteracje
        else:
            x_srodek = 0
            for i in range(iteracje):
                x_srodek, a, b = bisekcja_funkcji(a, b, funkcja, (a + b) / 2)
            return x_srodek, iteracje
