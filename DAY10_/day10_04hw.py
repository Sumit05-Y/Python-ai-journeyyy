matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def transpose(matrix):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(matrix[j][i])
        result.append(row)
    return result

def add_matrices(m1, m2):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

print_matrix(matrix1)
print()
print_matrix(transpose(matrix1))
print()
print_matrix(add_matrices(matrix1, matrix2))