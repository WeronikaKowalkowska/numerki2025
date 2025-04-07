# from tkinter.scrolledtext import example
#
import numpy as np
#
# # Definicje macierzy
# matrix_a = ([3, 3, 1], [2, 5, 7], [1, 2, 1])
# matrix_b = ([3, 3, 1], [2, 5, 7], [-4, -10, -14])
# matrix_c = ([3, 3, 1], [2, 5, 7], [-4, -10, -14])
# matrix_d = ([0.5, -0.0625, 0.1875, 0.0625],
#             [-0.0625, 0.5, 0, 0],
#             [0.1875, 0, 0.375, 0.125],
#             [0.0625, 0, 0.125, 0.25])
# matrix_e = ([3, 2, 1, -1], [5, -1, 1, 2], [1, -1, 1, 2], [7, 8, 1, -7])
# matrix_f = ([3, -1, 2, -1], [3, -1, 1, 1], [1, 2, -1, 2], [-1, 1, -2, -3])
# matrix_g = ([0, 0, 1], [1, 0, 0], [0, 1, 0])
# matrix_h = ([10, -5, 1], [4, -7, 2], [5, 1, 4])
# matrix_i = ([6, -4, 2], [-5, 5, 2], [0.9, 0.9, 3.6])
# matrix_j = ([1, 0.2, 0.3], [0.1, 1, -0.3], [-0.1, -0.2, 1])
#
#
# # Funkcja wyświetlająca macierz i wektor wyrazów wolnych
# def show_matrix(A, b):
#     for i in range(A.shape[0]):
#         row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
#         print(" + ".join(row), "=", b[i])
#
#
# # Sprawdzenie warunku zbieżności (przekątniowa dominacja)
# def have_solution(A):
#     for i in range(len(A)):
#         a_ii = abs(A[i, i])
#         suma = sum(abs(A[i, j]) for j in range(len(A[i])) if j != i)
#         if a_ii <= suma:
#             return False
#     return True
#
#
# # Schemat Hornera
# def horner(argument, wspolczynniki):
#     wynik = wspolczynniki[0]
#     for i in range(1, len(wspolczynniki)):
#         wynik = wynik * argument + wspolczynniki[i]
#     return wynik
#
#
# # Funkcja wybierająca przykładowe macierze i wektory
# def choose_function(literka):
#     if literka == 'a':
#         return np.array(matrix_a, dtype=float), [12, 33, 8]
#     if literka == 'b':
#         return np.array(matrix_b, dtype=float), [1, 20, -40]
#     if literka == 'c':
#         return np.array(matrix_c, dtype=float), [1, 20, -20]
#     if literka == 'd':
#         return np.array(matrix_d, dtype=float), [1.5, -1.625, 1, 0.4375]
#     if literka == 'e':
#         return np.array(matrix_e, dtype=float), [0, -4, 4, 6]
#     if literka == 'f':
#         return np.array(matrix_f, dtype=float), [-13, 1, 21, -5]
#     if literka == 'g':
#         return np.array(matrix_g, dtype=float), [3, 7, 5]
#     if literka == 'h':
#         return np.array(matrix_h, dtype=float), [3, -4, 19]
#     if literka == 'i':
#         return np.array(matrix_i, dtype=float), [4, 11, 13.5]
#     if literka == 'j':
#         return np.array(matrix_j, dtype=float), [1.5, 0.8, 0.7]
#
#
# # Metoda iteracyjna Gaussa-Seidla z ustaloną liczbą iteracji
# def gauss_seidel_iterations(matrix, vector, iterations):
#     x = np.ones(len(matrix))
#     for _ in range(int(iterations)):
#         for i in range(matrix.shape[0]):
#             sigma = 0
#             for j in range(matrix.shape[1]):
#                 if j != i:
#                     sigma += matrix[i, j] * x[j]
#             x[i] = (vector[i] - sigma) / matrix[i, i]
#     return x
#
#
# # Metoda Gaussa-Seidla z kryterium dokładności (używana norma infinity)
# def gauss_seidel_accuracy(matrix, vector, accuracy):
#     x = np.ones(len(matrix))
#     while True:
#         x_old = x.copy()
#         for i in range(matrix.shape[0]):
#             sigma = 0
#             for j in range(matrix.shape[1]):
#                 if j != i:
#                     sigma += matrix[i, j] * x[j]
#             x[i] = (vector[i] - sigma) / matrix[i, i]
#         if np.linalg.norm(x - x_old, ord=np.inf) < accuracy:
#             break
#     return x
#
#
# # Przykładowe wywołanie funkcji
# if __name__ == "__main__":
#     # Wybieramy przykładową macierz 'a'
#     A, b = choose_function('a')
#     print("Macierz A i wektor b dla przykładu 'a':")
#     show_matrix(A, b)
#
#     if have_solution(A):
#         print("Macierz spełnia warunek przekątniowej dominacji.")
#     else:
#         print("Macierz może nie spełniać warunków zbieżności.")
#
#     # Rozwiązanie metodą Gaussa-Seidla dla ustalonej liczby iteracji
#     iterations = 10
#     sol_iter = gauss_seidel_iterations(A, b, iterations)
#     print(f"Rozwiązanie po {iterations} iteracjach:", sol_iter)
#
#     # Rozwiązanie metodą Gaussa-Seidla z zadanym progiem dokładności
#     acc = 1e-6
#     sol_acc = gauss_seidel_accuracy(A, b, acc)
#     print(f"Rozwiązanie z dokładnością {acc}:", sol_acc)

