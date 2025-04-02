import numpy as np

#funkcja zwracająca wyrażenie matematyczne w zależności od wyboru użytkownika
def wybor_funkcji(literka):
    if literka == 'a':
        return lambda x: x ** 3 + 5 * x ** 2 - 2 * x - 10
    if literka == 'b':
        return lambda x: 3 * x ** 3 + 3 * x ** 2 - 18 * x
    if literka == 'c':
        return lambda x: np.sin(x)
    if literka == 'd':
        return lambda x: np.cos(x)
    if literka == 'e':
        return lambda x: 2 ** x - 4
    if literka == 'f':
        return lambda x: (1 / 2) ** x - 2
    if literka == 'g':
        return lambda x: np.sin((1 / 2) * x)
    if literka == 'h':
        return lambda x: np.cos(2 * x + 1)

#funkcja służąca przetestowaniu powtarzanych warunków używanych przy bisekcji i regula falsi
def sprawdz_warunki(funkcja,x_srodek,a,b):
    funkcja_x_srodek = funkcja(x_srodek)
    if funkcja_x_srodek == 0:
        return x_srodek,a,b
    if funkcja_x_srodek * funkcja(b) < 0:
        a = x_srodek
    if funkcja_x_srodek * funkcja(a) < 0:
        b = x_srodek
    return x_srodek,a,b

def sprawdz_warunki_wielomianu(a,b,wspolczynniki,x_srodek):
    horner_x_srodek = horner(x_srodek, wspolczynniki)
    if horner_x_srodek == 0:
        return x_srodek, a, b
    if horner_x_srodek * horner(b, wspolczynniki) < 0:
        a = x_srodek
    if horner_x_srodek * horner(a, wspolczynniki) < 0:
        b = x_srodek
    return x_srodek, a, b

#funkcja realizująca schemat hornera
def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik


