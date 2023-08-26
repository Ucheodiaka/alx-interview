#!/usr/bin/python3

""" Given an n x n 2D matrix, rotate it 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """ a function to rotate 2D Matrix at 90 deg clockwise
    - Do not return anything. The matrix must be edited 'in-place'.
    - You can assume the matrix will have 2 dimensions and will not be empty.
    """

    n = len(matrix[0])

    for t in range(n - 1, -1, -1):
        for q in range(0, n):
            matrix[q].append(matrix[t].pop(0))
