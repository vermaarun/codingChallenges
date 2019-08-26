def rotate_matrix(matrix):
    n = len(matrix[0])
    print "Original matrix"
    print_matrix(matrix)

    layers = n // 2
    for i in range(layers):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]  # save top
            matrix[i][j] = matrix[n - 1 - j][i]  # left -> top
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]  # bottom -> left
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]  # right -> bottom
            matrix[j][n - 1 - i] = temp  # top -> right

    print "Rotated matrix"
    print_matrix(matrix)


def print_matrix(matrix):
    n = len(matrix[0])
    for i in range(n):
        print matrix[i]


if __name__ == "__main__":
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_matrix(mat)
