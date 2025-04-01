import numpy as np
#W metodach iteracyjnych przed przystapieniem do obliczeň naležy sprawdzač czy podana macierz spelnia warunki zbiežnošci. Metody iteracyjne powinny posiadač dwa možliwe warunki stopu: ilošč iteracji albo uzyskanie podanej przez
#užytkownika dokladnošci (analogicznie do zadania 1).
matrix_a=([3,3,1],[2,5,7],[1,2,1])
matrix_b=([3,3,1],[2,5,7],[-4,-10,-14])
matrix_c=([3,3,1],[2,5,7],[-4,-10,-14])
matrix_d=([0.5,-0.0625,0.1875,0.0625],[-0.0625,0.5,0,0],[0.1875,0,0.375,0.125],[0.0625,0,0.125,0.25])
matrix_e=([3,2,1,-1],[5,-1,1,2],[1,-1,1,2],[7,8,1,-7])
matrix_f=([3,-1,2,-1],[3,-1,1,1],[1,2,-1,2],[-1,1,-2,-3])
matrix_g=([0,0,1],[1,0,0],[0,1,0])
matrix_h=([10,-5,1],[4,-7,2],[5,1,4])
matrix_i=([6,-4,2],[-5,5,2],[0.9,0.9,3.6])
matrix_j=([1,0.2,0.3],[0.1,1,-0.3],[-0.1,-0.2,1])

#menu
continueProgram=True
while(continueProgram):
    print("Wybierz przykład do rozwiązania: ")
    #macierze 3x3
    print("a) ",matrix_a, " * [x1, x2, x3] = [12, 33, 8]")  #x1=1   x2=2    x3=3
    print("b) ",matrix_b, " * [x1, x2, x3] = [1, 20, -40]") # nieoznaczony
    print("c) ",matrix_c, " * [x1, x2, x3] = [1, 20, -20]") # sprzeczny
    #macierze 4x4
    print("d) ",matrix_d, " * [x1, x2, x3, x4] = [1.5, -1.625, 1, 0.4375]")     #x1=2,  x2=-3,  x3=1.5,     x4=0.5
    print("e) ", matrix_e, " * [x1, x2, x3, x4] = [0, -4, 4, 6]")   #sprzeczny
    print("f) ", matrix_f, " * [x1, x2, x3, x4] = [-13, 1, 21, -5]")    #x1=1, x2=3, x3=-4, x4=5
    #macierze 3x3
    print("g) ",matrix_g, " * [x1, x2, x3] = [3, 7, 5]")  #x1=7   x2=5    x3=3
    print("h) ",matrix_h, " * [x1, x2, x3] = [3, -4, 19]")  #x1=1   x2=2    x3=3
    print("i) ",matrix_i, " * [x1, x2, x3] = [4, 11, 13.5]")  #sprzeczny
    print("j) ",matrix_j, " * [x1, x2, x3] = [1.5, 0.8, 0.7]")  #x1=1   x2=1    x3=1
    print("k) wczytaj macierz z pliku ")
    print("l) zakończ program ")

    test = True
    literka = ""
    while test:
        literka = input("Wybrano: ").lower()
        if 97 <= ord(literka) <= 107:
            test = False
        elif ord(literka)==108:
            continueProgram=False
        else:
            print("Niepoprawny wybór macierzy. Wybierz ponownie: ")

    


