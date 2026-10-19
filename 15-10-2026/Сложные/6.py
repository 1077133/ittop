def rotate_matrix(matrix):
    if not matrix or not matrix[0]: return []

    rows = len(matrix)
    cols = len(matrix[0])

    rotated = [[0] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            rotated[c][rows - 1 - r] = matrix[r][c]
    return rotated

# проверка
print(rotate_matrix([
    [1, 2, 3],
    [4, 5, 6]
])) # [[4, 1], [5, 2], [6, 3]]