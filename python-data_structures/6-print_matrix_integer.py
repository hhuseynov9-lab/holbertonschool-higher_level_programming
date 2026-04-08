#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = [print("{:d}".format(matrix[i][j]), end="\n" if (j + 1) % 3 == 0 else " ") for i in range(len(matrix)) for j in range(len(matrix[i]))]
    return new
