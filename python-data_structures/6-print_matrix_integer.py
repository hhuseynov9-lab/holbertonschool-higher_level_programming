#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = [ [ matrix[i][j]  for j in range(len(matrix[0]))] for i in range(len(matrix[0]))]
    return new
