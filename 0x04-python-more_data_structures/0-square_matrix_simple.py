#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ The function calculates the square of each integer in a given 2-dimensional matrix
     It returns a new matrix with the same dimensions as the input matrix
     where each element corresponds to the square of the corresponding element in the original matrix
     The original matrix remains unchanged, and the function does not rely on any external modules
     Regular loops, map, and similar constructs are permitted for the implementation.
     """
    new_matrix = [[elem**2 for elem in inner] for inner in matrix]

    return new_matrix
