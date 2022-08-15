def not_in_boards(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


size = int(input())
matrix = []
alice_row = 0
alice_col = 0
for row_ in range(size):
    row = input().split()
    matrix.append(row)
    for col in range(size):
        if matrix[row_][col] == "A":
            alice_row = row_
            alice_col = col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

teas = 0

while teas < 10:
    matrix[alice_row][alice_col] = "*"
    direction = input()
    row, col = directions[direction](alice_row, alice_col)

    alice_row, alice_col = row, col
    if not not_in_boards(matrix, alice_row, alice_col):
        break
    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break
    if matrix[alice_row][alice_col].isdigit():
        teas += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = "*"

if teas >= 10:
    print(f'She did it! She went to the party.')
else:
    print(f"Alice didn't make it to the tea party.")
for row in matrix:
    print(*row, sep=" ")
