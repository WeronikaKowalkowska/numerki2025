import numpy as np

matrix_a=([3,3,1],[2,5,7],[1,2,1])
matrix_b=([3,3,1],[2,5,7],[-4,-10,-14])
matrix_c=([3,3,1],[2,5,7],[-4,-10,-14])
matrix_d=([0.5,-0.0625,0.1875,0.0625],[-0.0625,0.5,0,0],[0.1875,0,0.375,0.125],[0.0625,0,0.125,0.25]) #spełnia warunku przekątniowej dominacji wierszowej
matrix_e=([3,2,1,-1],[5,-1,1,2],[1,-1,1,2],[7,8,1,-7])
matrix_f=([3,-1,2,-1],[3,-1,1,1],[1,2,-1,2],[-1,1,-2,-3])
matrix_g=([0,0,1],[1,0,0],[0,1,0])
matrix_h=([10,-5,1],[4,-7,2],[5,1,4])
matrix_i=([6,-4,2],[-5,5,2],[0.9,0.9,3.6])
matrix_j=([1,0.2,0.3],[0.1,1,-0.3],[-0.1,-0.2,1]) #spełnia warunku przekątniowej dominacji wierszowej

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
    if literka == 'k':
        matrix = []
        vector = []
        test=True
        while test:
            wybor = input("Wybierz jaki plik chcesz wczytać: a) example.csv  b) example2.txt").lower()
            if wybor == "a":
                matrix, vector = read_matrix_from_file("./files/example.csv") #x1=1  x2=2  x3=3  x4=4
                print("Wczytano: ")
                show_matrix(matrix, vector)
                test=False
            elif wybor == "b":
                matrix, vector = read_matrix_from_file("./files/example2.txt") #x1=1,278   x2= 1,262   x3= 0,1508
                print("Wczytano: ")
                show_matrix(matrix, vector)
                test=False
            else:
                print("Niepoprawny wybór macierzy :( . Wybierz ponownie: ")
        return matrix, vector
    if literka == 'l':
        matrix = []
        vector = []
        test=True
        while test:
            howMuch=input("Podaj liczbę równań: ")
            if not howMuch.isdigit():
                print("Niepoprawny wybór liczby :( . Wybierz ponownie: ")
            else:
                test=False
                for i in range(int(howMuch)):
                    print("Podaj ",howMuch, "współczynników ", i, "równania: ")
                    factors=[]
                    for j in range(int(howMuch)):
                        test2=True
                        while test2:
                            temp=input()
                            if not is_float(temp):
                                print("Niepoprawny wybór liczby :( . Wybierz ponownie: ")
                            else:
                                factors.append(float(temp))
                                test2=False
                    matrix.append(factors)
                for i in range(int(howMuch)):
                    print("Podaj ",i,"współczynnik wektora rozwiązania: ")
                    test2=True
                    while test2:
                        temp=input()
                        if not is_float(temp):
                            print("Niepoprawny wybór liczby :( . Wybierz ponownie: ")
                        else:
                            vector.append(float(temp))
                            test2 = False
        return np.array(matrix), np.array(vector)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def read_matrix_from_file(filename):
    matrix = []
    vector = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        values = list(map(int, line.strip().split(';')))
        if len(values) > 1:
            matrix.append(values)
        else:
            vector.append(values[0])

    return np.array(matrix), np.array(vector)


# def gauss_seidel(matrix, last_iter_solution, solution, vector):
#     for i in range(matrix.shape[0]):  # przechodzimy po wierszach
#         a_ii = matrix[i, i]
#         last_sum = 0
#         now_sum = 0
#         for j in range(matrix.shape[1]):  # przechodzimy po kolumnach
#             if j < i:  # podstawiamy to co obliczono w poprzedniej iteracji
#                 last_sum += matrix[i, j] * last_iter_solution[j]
#             elif j > i:
#                 now_sum += matrix[i, j] * solution[j]
#
#         last_iter_solution[i] = (vector[i] - now_sum - last_sum) / a_ii
#
#     for k in range(len(solution)):
#         solution[k] = last_iter_solution[k]  # zapisanie poprzedniogo rozwiązania
#
#     return solution, last_iter_solution
#
# '''def gauss_seidel2(matrix, last_iter_solution, solution, vector):
#     n = len(solution)
#     new_solution = solution.copy()
#     for i in range(n):
#         sum_val = 0
#         for j in range(n):
#             if j != i:
#                 # Use new_solution (updated values) for j < i
#                 sum_val += matrix[i, j] * new_solution[j]
#         new_solution[i] = (vector[i] - sum_val) / matrix[i, i]
#     return new_solution, last_iter_solution'''
#
def gauss_seidel_iterations(matrix, vector, iterations):
    solution = np.zeros(len(matrix))
    last_iter_solution = np.zeros(len(matrix))

    for iter in range(int(iterations)):  #iter - bierząca iteracja
        solution, last_iter_solution = gauss_seidel(matrix, last_iter_solution, solution, vector)
    return solution
#
# def gauss_seidel_accurancy(matrix, vector, accurancy):
#     solution = np.zeros(len(matrix))
#     last_iter_solution = np.zeros(len(matrix))
#
#     while not check_accurancy(solution, last_iter_solution, accurancy):
#         solution, last_iter_solution = gauss_seidel(matrix, last_iter_solution, solution, vector)
#     return solution
#
# '''def check_accurancy2(solution, last_iter_solution, epsilon):
#     max_diff = max(abs(solution[i] - last_iter_solution[i]) for i in range(len(solution)))
#     max_sol = max(abs(x) for x in solution)
#     return max_diff < epsilon * max_sol if max_sol != 0 else max_diff < epsilon'''
#
# def check_accurancy(solution, last_iter_solution, epsilon):
#     new_solution = []
#
#     for i in range(len(solution)):
#         new_solution.append(abs(solution[i]-last_iter_solution[i]))
#     value=max(new_solution)
#
#     if value < (epsilon*max(solution)):
#         return True
#     else:
#         return False
#
# '''def gauss_seidel_iterations2(matrix, vector, iterations):
#     solution = [1, 1, 1, 1]  # punkt startowy
#
#     for iter in range(iterations):  # bieżąca iteracja
#         for i in range(matrix.shape[0]):  # przechodzimy po wierszach
#             a_ii = matrix[i, i]
#             last_sum = 0
#             now_sum = 0
#             for j in range(matrix.shape[1]):  # przechodzimy po kolumnach
#                 if j < i:  # już zaktualizowane w tej iteracji
#                     last_sum += matrix[i, j] * solution[j]
#                 elif j > i:  # jeszcze nie zaktualizowane
#                     now_sum += matrix[i, j] * solution[j]
#
#             solution[i] = (vector[i] - now_sum - last_sum) / a_ii  # <-- TU aktualizujemy od razu!
#
#     return solution'''

# def gauss_seidel(matrix, old_solution, vector):
#     """
#     Oblicza nowe przybliżenie rozwiązania metodą Gaussa-Seidla.
#     old_solution – poprzednie przybliżenie,
#     vector – wektor wyrazów wolnych.
#     """
#     new_solution = np.copy(old_solution)
#     n = matrix.shape[0]
#     for i in range(n):
#         # Obliczamy sumę dla elementów przed przekątną: wykorzystujemy już zaktualizowane wartości
#         sum_before = np.dot(matrix[i, :i], new_solution[:i])
#         # Obliczamy sumę dla elementów po przekątnej: korzystamy z poprzedniego przybliżenia
#         sum_after = np.dot(matrix[i, i + 1:], old_solution[i + 1:])
#         new_solution[i] = (vector[i] - sum_before - sum_after) / matrix[i, i]
#     return new_solution


def check_accuracy(new_solution, old_solution, tol):
    """
    Sprawdza, czy zbieżność jest osiągnięta.
    Używamy normy infinity, by ocenić maksymalną zmianę między kolejnymi iteracjami.
    Przykładowo, możemy zastosować kryterium względne, zabezpieczając przypadek,
    gdy maksimum new_solution jest zerowe.
    """
    diff = np.abs(new_solution - old_solution)
    max_diff = np.max(diff)

    # Jeśli nowe przybliżenie jest bliskie zeru, stosuj kryterium absolutne.
    if np.max(np.abs(new_solution)) == 0:
        return max_diff < tol
    else:
        relative_error = max_diff / np.max(np.abs(new_solution))
        return relative_error < tol


def gauss_seidel_with_accuracy(matrix, vector, tol, max_iterations=1000):
    """
    Wykonuje iteracje Gaussa-Seidla do momentu osiągnięcia zadanej dokładności tol.
    max_iterations – zabezpieczenie przed nieskończoną pętlą.
    """
    solution = np.zeros(len(vector))
    iteration = 0

    while iteration < max_iterations:
        new_solution = gauss_seidel(matrix, solution, vector)
        # Sprawdzamy czy kryterium zbieżności jest spełnione
        if check_accuracy(new_solution, solution, tol):
            break
        solution = new_solution
        iteration += 1
    return new_solution