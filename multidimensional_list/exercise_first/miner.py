rows = int(input())
commands = input().split()
matrix = []
game_is_over = False
got_all_coals = False
coals = 0
miner = []
for r in range(rows):
    row = input().split()
    for c in range(len(row)):
        if row[c] == "c":
            coals += 1
        if row[c] == "s":
            miner.append([r, c])
    matrix.append(row)
for command in commands:
    if command == "up":
        if 0 <= miner[0][0] - 1 < rows and 0 <= miner[0][1] < rows:
            miner[0][0] -= 1
            if matrix[miner[0][0]][miner[0][1]] == "c":
                coals -= 1
                matrix[miner[0][0]][miner[0][1]] = "*"
            elif matrix[miner[0][0]][miner[0][1]] == "e":
                game_over = True
    elif command == "left":
        if 0 <= miner[0][0] < rows and 0 <= miner[0][1] - 1 < rows:
            miner[0][1] -= 1
            if matrix[miner[0][0]][miner[0][1]] == "c":
                coals -= 1
                matrix[miner[0][0]][miner[0][1]] = "*"
            elif matrix[miner[0][0]][miner[0][1]] == "e":
                game_is_over = True
    elif command == "right":
        if 0 <= miner[0][0] < rows and 0 <= miner[0][1] + 1 < rows:
            miner[0][1] += 1
            if matrix[miner[0][0]][miner[0][1]] == "c":
                coals -= 1
                matrix[miner[0][0]][miner[0][1]] = "*"
            elif matrix[miner[0][0]][miner[0][1]] == "e":
                game_is_over = True
    elif command == "down":
        if 0 <= miner[0][0] + 1 < rows and 0 <= miner[0][1] < rows:
            miner[0][0] += 1
            if matrix[miner[0][0]][miner[0][1]] == "c":
                coals -= 1
                matrix[miner[0][0]][miner[0][1]] = "*"
            elif matrix[miner[0][0]][miner[0][1]] == "e":
                game_is_over = True
    if game_is_over:
        break
    if coals == 0:
        got_all_coals = True
        break

if got_all_coals:
    print(f"You collected all coal! {miner[0][0], miner[0][1]}")
elif game_is_over:
    print(f"Game over! {miner[0][0], miner[0][1]}")
else:
    print(f"{coals} pieces of coal left. {miner[0][0], miner[0][1]}")
