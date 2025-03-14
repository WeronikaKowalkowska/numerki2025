
def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

# METODA BISEKCJI
def bisekcja_funkcji(a,b,funkcja,x_srodek):
    #funkcja_x_srodek = funkcja(x_srodek)
    x_srodek, a, b=sprawdz_warunki(funkcja,x_srodek,a,b)
    return x_srodek,a,b

def falsi_funkcji(a,b,funkcja):
    if funkcja(a) == funkcja(b):
        return (a + b) / 2,a,b
    x0 = a - (funkcja(a) / (funkcja(b) - funkcja(a))) * (b - a)
    x0, a, b=sprawdz_warunki(funkcja,x0,a,b)
    return x0,a,b

def sprawdz_warunki(funkcja,x_srodek,a,b):
    funkcja_x_srodek = funkcja(x_srodek)
    if funkcja_x_srodek == 0:
        return x_srodek,a,b
    if funkcja_x_srodek * funkcja(b) < 0:
        a = x_srodek
    if funkcja_x_srodek * funkcja(a) < 0:
        b = x_srodek
    return x_srodek,a,b

def bisekcja_wielomian(a,b,wspolczynniki,x_srodek):
    #x_srodek = (a + b) / 2
    horner_x_srodek = horner(x_srodek, wspolczynniki)
    if horner_x_srodek == 0:
        return x_srodek
    if horner_x_srodek * horner(b, wspolczynniki) < 0:
        a = x_srodek
    if horner_x_srodek * horner(a, wspolczynniki) < 0:
        b = x_srodek
    return x_srodek,a,b

def bisekcja(a, b, wspolczynniki, epsilon,iteracje, kryterium, czy_wielomian,funkcja):
    #x_srodek = (a + b) / 2

    if czy_wielomian:
        # dokladnosc
        if kryterium == 'a':
            x_srodek = 0
            while abs(horner((a + b) / 2, wspolczynniki)) >= epsilon:
                x_srodek,a,b=bisekcja_wielomian(a, b, wspolczynniki, (a + b)/2)
            return x_srodek
        # iteracje
        else:
            #x_srodek = (a + b) / 2
            x_srodek = 0
            for i in range(iteracje):
                x_srodek,a,b = bisekcja_wielomian(a, b, wspolczynniki, (a + b)/2)
            return x_srodek
    else:
        #dokladnosc
        if kryterium == 'a':
            x_srodek = 0
            while abs(funkcja(x_srodek)) >= epsilon:
                x_srodek,a,b=bisekcja_funkcji(a,b,funkcja,(a + b)/2)
            return x_srodek
        #iteracje
        else:
            x_srodek = 0
            for i in range(iteracje):
                x_srodek, a, b = bisekcja_funkcji(a, b, funkcja, (a + b) / 2)
            return x_srodek

def falsi(a, b, wspolczynniki, epsilon,iteracje, kryterium, czy_wielomian,funkcja):
    #x_srodek = (a + b) / 2

    if czy_wielomian:
        horner_a = horner(a, wspolczynniki)
        horner_b = horner(b, wspolczynniki)
        # dokladnosc
        if kryterium == 'a':
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
        #dokladnosc
        if kryterium == 'a':
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

# METODA FALSI


def falsi_wielomianu(a,b,wspolczynniki,horner_a,horner_b):
    if horner_a == horner_b:
        return a,b,(a + b) / 2
    x0 = a - (horner_a / (horner_b - horner_a)) * (b - a)
    horner_x0 = horner(x0, wspolczynniki)
    if horner_x0 == 0:
        return a,b,x0
    if horner_x0 * horner_b < 0:
        a = x0
    if horner_x0 * horner_a < 0:
        b = x0
    return a,b,x0