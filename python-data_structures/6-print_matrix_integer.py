#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = [ ["{:d}".format(imatrix[i][j])  for j in range(len(matrix[0]))] for i in range(len(matrix[0]))]
    return new
