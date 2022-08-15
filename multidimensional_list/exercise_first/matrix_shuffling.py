rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

command = input()

while command != "END":
    command = command.split()
    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if 0 <= row1 < len(matrix) and 0 <= row2 < len(matrix) and 0 <= col1 < columns and 0 <= col2 < columns:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(*row, sep=" ")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()
