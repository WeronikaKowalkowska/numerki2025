import numpy as np

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

#A to macierz współczynników, a b - wektor wyrazów wolnych
def show_matrix(A, b):
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])

#czy jest spełniony warunek zbieżności metody dla macierzy A
def have_solution(A):
    suma = 0     #suma wartości i-go wiersza
    a_ii = 0    #wartość na przekątnej i-go wiersza
    for i in range(len(A)):
        suma = 0
        a_ii = abs(A[i, i])
        for j in range(len(A[i])):
            if i != j:
                suma += abs(A[i, j])
        if a_ii <= suma:     #żeby było rozwiązanie to musi być a_ii > sum
         return False
    return True

#funkcja realizująca schemat hornera
def horner(argument, wspolczynniki):
    wynik = wspolczynniki[0]
    for i in range(1, len(wspolczynniki)):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik

def choose_function(literka):
    if literka == 'a':
        return np.array(matrix_a), [12,33,8]
    if literka == 'b':
        return np.array(matrix_b), [1,20,-40]
    if literka == 'c':
        return np.array(matrix_c), [1, 20,-20]
    if literka == 'd':
        return np.array(matrix_d), [1.5,-1.625, 1, 0.4375]
    if literka == 'e':
        return np.array(matrix_e), [0,-4,4,6]
    if literka == 'f':
        return np.array(matrix_f), [-13, 1, 21, -5]
    if literka == 'g':
        return np.array(matrix_g), [3, 7, 5]
    if literka == 'h':
        return np.array(matrix_h), [3, -4,19]
    if literka == 'i':
        return np.array(matrix_i), [4, 11, 13.5]
    if literka == 'j':
        return np.array(matrix_j), [1.5, 0.8, 0.7]

def gauss_seidel(matrix, vector, solution):
    # for i in range(0, len(matrix_a[0]) - 1):
    #     expression=0
    #     for j in range(0, len(matrix_a) - 1):
    #         expression=expression + solution[j] * matrix[i][j]
    #     solution[i] = (1 / matrix[i][i]) * (vector[i]+expression)

    return solution

def gauss_seidel_iterations(matrix, vector, iterations):
    solution = [1, 1, 1, 1] #wynik początkowo to zerowy wektor
    last_iter_solution = [1, 1, 1, 1] #wyniki dla poprzedniej iteracji

    for iter in range(iterations):  #iter - bierząca iteracja
        for i in range(matrix.shape[0]): #przechodzimy po wierszach
            a_ii = matrix[i, i]
            last_sum = 0
            now_sum = 0
            for j in range(matrix.shape[1]): #przechodzimy po kolumnach
                if j < i: #podstawiamy to co obliczono w poprzedniej iteracji
                    last_sum += matrix[i, j] * last_iter_solution[j]
                elif j > i:
                    now_sum += matrix[i, j] * solution[j]

            last_iter_solution[i] = (vector[i] - now_sum - last_sum) / a_ii

        for k in range(len(solution)):
            solution[k] = last_iter_solution[k]      #zapisanie poprzedniogo rozwiązania
    # for i in range(0, iterations):
    #     solution = gauss_seidel(matrix, vector, solution)
    return solution

def gauss_seidel_iterations2(matrix, vector, iterations):
    solution = [1, 1, 1, 1]  # punkt startowy

    for iter in range(iterations):  # bieżąca iteracja
        for i in range(matrix.shape[0]):  # przechodzimy po wierszach
            a_ii = matrix[i, i]
            last_sum = 0
            now_sum = 0
            for j in range(matrix.shape[1]):  # przechodzimy po kolumnach
                if j < i:  # już zaktualizowane w tej iteracji
                    last_sum += matrix[i, j] * solution[j]
                elif j > i:  # jeszcze nie zaktualizowane
                    now_sum += matrix[i, j] * solution[j]

            solution[i] = (vector[i] - now_sum - last_sum) / a_ii  # <-- TU aktualizujemy od razu!

    return solution

def gauss_seidel_accurancy(matrix, vector, accurancy):
    solution = np.zeros_like(vector)
    # while for i in range len(matrix):
    #     abs(solution[i]-solution[i+1])<accurancy:
    #     solution = gauss_seidel(matrix, vector, solution)
    return solution

# def verify_integrity(matrix,vector):
