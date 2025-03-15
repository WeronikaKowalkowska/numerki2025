from funkcje import *

#realizacja regula falsi dla funkcji c-h
def falsi_funkcji(a,b,funkcja):
    # if funkcja(a) == funkcja(b):
    #     return (a + b) / 2,a,b
    x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
    x0, a, b=sprawdz_warunki(funkcja,x0,a,b)
    return x0,a,b

#realizacja regula falsi dla wielomianu
def falsi_wielomianu(a,b,wspolczynniki,horner_a,horner_b):
    # if horner_a == horner_b:
    #     return a,b,(a + b) / 2
    x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
    horner_x0 = horner(x0, wspolczynniki)
    if horner_x0 == 0:
        return a,b,x0
    if horner_x0 * horner_b < 0:
        a = x0
    if horner_x0 * horner_a < 0:
        b = x0
    return a,b,x0

#ogólna realizacja regula falsi dla wszystkich wbudowanych funkcji
def falsi(a, b, wspolczynniki, epsilon,iteracje, kryterium, czy_wielomian,funkcja):
    if czy_wielomian:
        horner_a = horner(a, wspolczynniki)
        horner_b = horner(b, wspolczynniki)
        # dokładność
        if kryterium == 'a':
            # if horner_a == horner_b: #TU DODAŁAM
            #     return (a + b) / 2
            x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
            horner_x0 = horner(x0, wspolczynniki)
            while abs(horner_x0) >= epsilon:
                a,b,x0=falsi_wielomianu(a,b,wspolczynniki,horner(a, wspolczynniki),horner(b, wspolczynniki))
                horner_x0 = horner(x0, wspolczynniki)
            return x0
        # iteracje
        else:
            x0 = 0
            for i in range(iteracje):
                a,b,x0=falsi_wielomianu(a,b,wspolczynniki,horner(a, wspolczynniki),horner(b, wspolczynniki))
            return x0
    else:
        #dokładność
        if kryterium == 'a':
            # if funkcja(a) == funkcja(b): #TU DODAŁAM
            #     return (a + b) / 2
            x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
            while abs(funkcja(x0)) >= epsilon:
                a,b,x0=falsi_funkcji(a,b,x0)
            return x0
        #iteracje
        else:
            x0 = 0
            for i in range(iteracje):
                a,b,x0=falsi_funkcji(a,b,funkcja)
            return x0

