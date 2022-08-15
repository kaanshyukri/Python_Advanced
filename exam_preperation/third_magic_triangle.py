def get_magic_triangle(num):
    matrix = []
    for row in range(num):
        line = []
        for col in range(row + 1):
            if col == 0:
                line.append(1)
            elif col == row:
                line.append(1)
            else:
                a = matrix[row-1][col]
                b = matrix[row-1][col-1]
                line.append(a + b)
        matrix.append(line)
    return matrix


get_magic_triangle(5)
