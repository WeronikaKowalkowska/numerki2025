import numpy as np
#W metodach iteracyjnych przed przystapieniem do obliczeň naležy sprawdzač czy podana macierz spelnia warunki zbiežnošci. Metody iteracyjne powinny posiadač dwa možliwe warunki stopu: ilošč iteracji albo uzyskanie podanej przez
#užytkownika dokladnošci (analogicznie do zadania 1).
matrix_a=np.array([3,3,1],[2,5,7],[1,2,1])
matrix_b=np.arrat([3,3,1],[2,5,7],[-4,-10,-14])
matrix_c=np.arrat([3,3,1],[2,5,7],[-4,-10,-14])
matrix_d=np.array([0.5,-0.0625,0.1875,0.0625],[-0.0625,0.5,0,0],[0.1875,0,0.375,0.125],[0.0625,0,0.125,0.25])
matrix_e=np.array([3,2,1,-1],[5,-1,1,2],[1,-1,1,2],[7,8,1,-7])
matrix_f=np.array([3,-1,2,-1],[3,-1,1,1],[1,2,-1,2],[-1,1,-2,-3])
matrix_g=np.array([0,0,1],[1,0,0],[0,1,0])
matrix_h=np.array([10,-5,1],[4,-7,2],[5,1,4])
matrix_i=np.array([6,-4,2],[-5,5,2],[0.9,0.9,3.6])
matrix_j=np.array([1,0.2,0.3],[0.1,1,-0.3],[-0.1,-0.2,1])

#menu
continueProgram=True
while(continueProgram):
    print("Wybierz przykład do rozwiązania: ")
