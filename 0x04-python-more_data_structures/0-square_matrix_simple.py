#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = [[y ** 2 for y in x] for x in matrix]
    return matrix_new
