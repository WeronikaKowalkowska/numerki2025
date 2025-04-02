import numpy as np
from main import *

#funkcja realizująca schemat hornera
def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def choose_function(literka):
    if literka == 'a':
        return matrix_a, [12,33,8]
    if literka == 'b':
        return matrix_b, [1,20,-40]
    if literka == 'c':
        return matrix_c, [1, 20,-20]
    if literka == 'd':
        return matrix_d, [1.5,-1.625, 1, 0.4375]
    if literka == 'e':
        return matrix_e, [0,-4,4,6]
    if literka == 'f':
        return matrix_f, [-13, 1, 21, -5]
    if literka == 'g':
        return matrix_g, [3, 7, 5]
    if literka == 'h':
        return matrix_h, [3, -4,19]
    if literka == 'i':
        return matrix_i, [4, 11, 13.5]
    if literka == 'j':
        return matrix_j, [1.5, 0.8, 0.7]

def gauss_seidel(matrix, vector,solution):

    '''for i in range(0,len(matrix_a)-1):
        solution[i]=
    solution[0]=(1/matrix[0][0])*(vector[0]+solution[1]*matrix[0][1]+solution[2]*matrix[0][2])
    for i in range(3):
    for i in range(0,len(matrix_a[0])-1):
        solution[i] = (1 / matrix[i][i]) * (vector[i] + solution[1] * matrix[i][1] + solution[2] * matrix[i][2])'''
    for i in range(0, len(matrix_a[0]) - 1):
        expression=0
        for j in range(0, len(matrix_a) - 1):
            expression=expression+ solution[j] * matrix[i][j]
        solution[i] = (1 / matrix[i][i]) * (vector[i]+expression)

    return solution

def gauss_seidel_iterations(matrix, vector, iterations):
    solution = []
    for i in range(0,iterations):
        solution = gauss_seidel(matrix, vector,solution)
    return solution


# def gauss_seidel_accurancy(matrix, vector, accurancy):
#     solution = []
#     while for i in range len(matrix): abs(solution[i]-solution[i+1])<accurancy:
#         solution = gauss_seidel(matrix, vector, solution)
#     return solution

def verify_integrity(matrix,vector):
    