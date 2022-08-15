def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    index = []
    if is_inside(row-1, col, size) and matrix[row-1][col] > 0:
        index.append([row-1, col])
    if is_inside(row-1, col-1, size) and matrix[row-1][col-1] > 0:
        index.append([row-1, col-1])
    if is_inside(row-1, col+1, size) and matrix[row-1][col+1] > 0:
        index.append([row-1, col+1])
    if is_inside(row, col-1, size) and matrix[row][col-1] > 0:
        index.append([row, col-1])
    if is_inside(row, col+1, size) and matrix[row][col+1] > 0:
        index.append([row, col+1])
    if is_inside(row+1, col-1, size) and matrix[row+1][col-1] > 0:
        index.append([row+1, col-1])
    if is_inside(row+1, col, size) and matrix[row+1][col] > 0:
        index.append([row+1, col])
    if is_inside(row+1, col+1, size) and matrix[row+1][col+1] > 0:
        index.append([row+1, col+1])
    return index


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()
for bomb in bombs:
    rows, column = [int(x) for x in bomb.split(",")]
    number = matrix[rows][column]
    if matrix[rows][column] > 0:
        matrix[rows][column] = 0
    if number <= 0:
        continue
    for r, c in get_neighbours(rows, column, matrix):
        matrix[r][c] -= number

active = 0
sum_cells = 0
for r in matrix:
    for col in r:
        if col > 0:
            active += 1
            sum_cells += col

print(f"Alive cells: {active}")
print(f"Sum: {sum_cells}")
for nums in matrix:
    print(*nums, sep=" ")
