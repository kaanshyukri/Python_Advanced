n = int(input())
matrix = []
location = ()
for _ in range(n):
    matrix.append(list(input()))
symbol = input()
found = False
for row in range(n):
    for column in range(n):
        if matrix[row][column] == symbol:
            location = (row, column)
            print(location)
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
