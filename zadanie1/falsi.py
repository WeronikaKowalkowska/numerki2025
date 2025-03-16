from funkcje import *

#realizacja regula falsi dla funkcji c-h
def falsi_funkcji(a,b,funkcja):
    if funkcja(a) == funkcja(b):
        return (a + b) / 2,a,b
    x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
    x0, a, b=sprawdz_warunki(funkcja,x0,a,b)
    return a,b,x0

#realizacja regula falsi dla wielomianu
'''def falsi_wielomianu(a,b,wspolczynniki,x0):

    horner_x0 = horner(x0, wspolczynniki)
    if horner_x0 == 0:
        return a,b,x0
    if horner_x0 * horner(b,wspolczynniki) < 0:
        a = x0
    if horner_x0 * horner(a,wspolczynniki) < 0:
        b = x0
    return a,b,x0'''

#ogólna realizacja regula falsi dla wszystkich wbudowanych funkcji
def falsi(a, b, wspolczynniki, epsilon,iteracje, kryterium, czy_wielomian,funkcja):
    ile_iteracji = 0
    if czy_wielomian:
        horner_a = horner(a, wspolczynniki)
        horner_b = horner(b, wspolczynniki)
        # dokładność
        if kryterium == 'a':
            x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
            horner_x0 = horner(x0, wspolczynniki)
            while abs(horner_x0) >= epsilon:
                x0,a,b=sprawdz_warunki_wielomianu(a,b,wspolczynniki,x0)
                # horner_x0 = horner(x0, wspolczynniki)
                ile_iteracji += 1
            return x0, ile_iteracji
        # iteracje
        else:
            x0 = 0
            for i in range(iteracje):
                x0, a, b = sprawdz_warunki_wielomianu(a, b, wspolczynniki, x0)
                return x0, iteracje
    else:
        #dokładność
        if kryterium == 'a':
            x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
            while abs(funkcja(x0)) >= epsilon:
                a,b,x0=falsi_funkcji(a,b,funkcja)
                ile_iteracji += 1
            return x0, ile_iteracji
        #iteracje
        else:
            x0 = 0
            for i in range(iteracje):
                a,b,x0=falsi_funkcji(a,b,funkcja)
            return x0, iteracje

