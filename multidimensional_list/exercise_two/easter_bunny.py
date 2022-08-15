rows = int(input())
matrix = []
row_start = 0
col_start = 0
for r in range(rows):
    row_ = input().split()
    matrix.append(row_)
    for c in range(rows):
        if row_[c] == "B":
            row_start = r
            col_start = c
my_dict = {"up": {}, "left": {}, "right": {}, "down": {}}
commands = ["up", "left", "right", "down"]
for command in commands:
    if command == "up":
        for row in range(1, rows):
            if 0 <= row_start - row < rows and matrix[row_start - row][col_start] != "X":
                my_dict["up"][(row_start - row, col_start)] = int(matrix[row_start - row][col_start])
            else:
                break
    elif command == "left":
        for row in range(1, rows):
            if 0 <= col_start - row < rows and matrix[row_start][col_start - row] != "X":
                my_dict["left"][(row_start, col_start - row)] = int(matrix[row_start][col_start - row])
            else:
                break
    elif command == "right":
        for row in range(1, rows):
            if 0 <= col_start + row < rows and matrix[row_start][col_start + row] != "X":
                my_dict["right"][(row_start, col_start + row)] = int(matrix[row_start][col_start + row])
            else:
                break
    else:
        for row in range(1, rows):
            if 0 <= row_start + row < rows and matrix[row_start + row][col_start] != "X":
                my_dict["down"][(row_start + row, col_start)] = int(matrix[row_start + row][col_start])
            else:
                break
best_direction = ""
best_sum = -99999999999999999999999999

for key, value in my_dict.items():
    sum_calc = 0
    for k, v in value.items():
        sum_calc += v
    if sum_calc >= best_sum:
        best_direction = key
        best_sum = sum_calc

print(best_direction)

for key, value in my_dict.items():
    if key == best_direction:
        for b, c in value.items():
            print(f"[{b[0]}, {b[1]}]")

print(best_sum)
