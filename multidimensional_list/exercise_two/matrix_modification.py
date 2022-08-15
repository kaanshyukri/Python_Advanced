rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input()

while command != "END":
    command = command.split()
    row, col, number = [int(x) for x in command[1:]]
    if command[0] == "Add":
        if 0 <= row < rows and 0 <= col < rows:
            matrix[row][col] += number
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        if 0 <= row < rows and 0 <= col < rows:
            matrix[row][col] -= number
        else:
            print("Invalid coordinates")
    command = input()

for mat in matrix:
    print(*mat, sep=" ")
