import numpy as np

from funkcje import choose_function, gauss_seidel_iterations, gauss_seidel_accurancy, matrix_a, matrix_b, matrix_c, matrix_d, matrix_e, \
    matrix_f, matrix_g, matrix_h, matrix_i, matrix_j, have_solution, show_matrix

from funkcje import gauss_seidel_iterations2

# matrix = np.array(([8,1,2, 3],[1,6,1, -1],[2,1,18, 2],[3, -1, 2, 40]))
# vector = [28, 12, 66, 167]

# matrix=np.array(([3,3,1],[2,5,7],[1,2,1]))
# vector = [12,33,8]

solution = gauss_seidel_iterations(matrix, vector, 5)
print(solution)
solution2 = gauss_seidel_iterations2(matrix, vector, 5)
print(solution2)