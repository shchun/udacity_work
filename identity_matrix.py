#!/usr/bin/env python

def is_identity_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        return False

    for i in range (0, len(matrix)):
        for j in range (1, len(matrix[0])):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

 

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
