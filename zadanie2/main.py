from asyncio import wait_for

import numpy as np
import time

from funkcje import *

#W metodach iteracyjnych przed przystapieniem do obliczeń należy sprawdzać czy podana macierz spelnia warunki zbieżności.
#Metody iteracyjne powinny posiadać dwa możliwe warunki stopu: ilość iteracji albo uzyskanie podanej przez użytkownika dokladności (analogicznie do zadania 1).


#MENU
continueProgram=True

while continueProgram:
    print("Wybierz przykład do rozwiązania: ")
    #macierze 3x3
    print("a)")
    chosen_matrix, vector = choose_function('a')
    show_matrix(chosen_matrix, vector)  # x1=1,   x2=2,    x3=3
    print("b)")
    chosen_matrix, vector = choose_function('b')
    show_matrix(chosen_matrix, vector) # nieoznaczony
    print("c)")
    chosen_matrix, vector = choose_function('c')
    show_matrix(chosen_matrix, vector)  # sprzeczny
    #macierze 4x4
    print("d)")
    chosen_matrix, vector = choose_function('d')
    show_matrix(chosen_matrix, vector)  #  x1=2,  x2=-3,  x3=1.5,   x4=0.5
    print("e)")
    chosen_matrix, vector = choose_function('e')
    show_matrix(chosen_matrix, vector)  # sprzeczny
    print("f)")
    chosen_matrix, vector = choose_function('f')
    show_matrix(chosen_matrix, vector)  # x1=1, x2=3, x3=-4, x4=5
    #macierze 3x3
    print("g)")
    chosen_matrix, vector = choose_function('g')
    show_matrix(chosen_matrix, vector)  #  #x1=7,   x2=5,    x3=3
    print("h)")
    chosen_matrix, vector = choose_function('h')
    show_matrix(chosen_matrix, vector)  # x1=1,   x2=2,  ,x3=3
    print("i)")
    chosen_matrix, vector = choose_function('i')
    show_matrix(chosen_matrix, vector)  # sprzeczny
    print("j)")
    chosen_matrix, vector = choose_function('j')
    show_matrix(chosen_matrix, vector)  # x1=1,   x2=1,    x3=1
    print("k)")
    print("wczytaj macierz z pliku")
    print("l)")
    print("zakończ program :(")

    test = True
    letter = ""
    while test:
        letter = input("Wybrano: ").lower()
        if 97 <= ord(letter) <= 107:
            test = False
        elif ord(letter)==108:
            continueProgram = False
            test = False
            #break
        else:
            print("Niepoprawny wybór macierzy :( . Wybierz ponownie: ")

    if not continueProgram:
        break

    test = True
    while test:
        chosen_matrix, vector = choose_function(letter)
        if have_solution(chosen_matrix) is False:
            print("Wybrana macierz nie spełnia warunku przekątniowej dominacji wierszowej, zatem może nie mieć rozwiązania. Wybierz inną macierz.")
            test = False
            time.sleep(3)
        else:
            cryterium= input("Wybierz kryterium stopu: a) liczba iteracji   b) osiągnięcie dokładności wyniku   ").lower()
            if cryterium == "a":
                test2=True
                while test2:
                    iterations=input("Podaj liczbę iteracji do wykonania: ")
                    if iterations.isdigit():
                        print("Wykonuję metodę Gaussa-Seidla dla", iterations, "iteracji: ")
                        chosen_matrix, vector = choose_function(letter)
                        solution = gauss_seidel_iterations(chosen_matrix, vector, iterations)
                        formatted_solution = [str(x).replace('.', ',') for x in solution]
                        print("Rozwiązanie:", '; '.join(formatted_solution))
                        test2 = False
                    else:
                        print("Wprowadzona wartość jest niepoprawna. :( Spróbuj ponownie. ")
                test=False
                time.sleep(3)
            elif cryterium == "b":
                test2 = True
                while test2:
                    accurancy = float(input("Podaj dokładność wyniku: "))
                    if accurancy > 0:
                        print("Wykonuję metodę Gaussa-Seidla dla osiągnięcia dokładnosci", accurancy)
                        chosen_matrix,vector=choose_function(letter)
                        solution = gauss_seidel_accurancy(chosen_matrix, vector, accurancy)
                        formatted_solution = [str(x).replace('.', ',') for x in solution]
                        print("Rozwiązanie:", '; '.join(formatted_solution))
                        test2 = False
                    else:
                        print("Wprowadzona wartość jest niepoprawna. :( Spróbuj ponownie:")

                test = False
                time.sleep(3)
            else:
                print("Niepoprawny wybór kryterium. :( Spróbuj ponownie: ")