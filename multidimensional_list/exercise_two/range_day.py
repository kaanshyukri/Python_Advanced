rows = 5
matrix = []

targets = 0
start_row = 0
start_col = 0
all_targets = 0
for r in range(rows):
    row = input().split()
    matrix.append(row)
    for c in range(rows):
        if matrix[r][c] == "A":
            start_row = r
            start_col = c
        if row[c] == "x":
            targets += 1
            all_targets += 1
targets_list = []
commands_num = int(input())
for _ in range(commands_num):
    command = input().split()
    action, direction = command[0:2]
    if action == "shoot":
        if direction == "up":
            for shoot in range(1, rows):
                if 0 <= start_row - shoot < rows and matrix[start_row - shoot][start_col] == "x":
                    matrix[start_row - shoot][start_col] = "."
                    targets -= 1
                    targets_list.append([start_row - shoot, start_col])
                    break
        elif direction == "right":
            for shoot in range(1, rows):
                if 0 <= start_col + shoot < rows and matrix[start_row][start_col + shoot] == "x":
                    matrix[start_row][start_col + shoot] = "."
                    targets -= 1
                    targets_list.append([start_row, start_col + shoot])
                    break
        elif direction == "left":
            for shoot in range(1, rows):
                if 0 <= start_col - shoot < rows and matrix[start_row][start_col - shoot] == "x":
                    matrix[start_row][start_col - shoot] = "."
                    targets -= 1
                    targets_list.append([start_row, start_col - shoot])
                    break
        elif direction == "down":
            for shoot in range(1, rows):
                if 0 <= start_row + shoot < rows and matrix[start_row + shoot][start_col] == "x":
                    matrix[start_row + shoot][start_col] = "."
                    targets -= 1
                    targets_list.append([start_row + shoot, start_col])
                    break

    elif action == "move":
        num = int(command[2])
        if direction == "up":
            if 0 <= start_row - num < rows and matrix[start_row - num][start_col] == ".":
                matrix[start_row][start_col] = "."
                start_row -= num
        elif direction == "right":
            if 0 <= start_col + num < rows and matrix[start_row][start_col + num] == ".":
                matrix[start_row][start_col] = "."
                start_col += num
        elif direction == "left":
            if 0 <= start_col - num < rows and matrix[start_row][start_col - num] == ".":
                matrix[start_row][start_col] = "."
                start_col -= num
        elif direction == "down":
            if 0 <= start_row + num < rows and matrix[start_row + num][start_col] == ".":
                matrix[start_row][start_col] = "."
                start_row += num
    if targets == 0:
        break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
else:
    print(f"Training completed! All {all_targets} targets hit.")

for target in targets_list:
    print(f"[{target[0]}, {target[1]}]")
