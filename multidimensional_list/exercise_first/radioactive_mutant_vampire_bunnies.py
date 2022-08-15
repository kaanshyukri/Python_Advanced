rows, columns = [int(x) for x in input().split()]
matrix = []
player = []
for r in range(rows):
    row = input()
    for c in range(len(row)):
        if player:
            break
        if row[c] == "P":
            player.append([r, c])
    matrix.append([row])
commands = input()
won_game = False
for command in commands:
    if command == "U":
        if not 0 <= player[0][0] - 1 <= rows:
            won_game = True
            matrix[player[0][0]][player[0][1]] = "."
        else:
            player[0][0] -= 1
            matrix[player[0][0]][player[0][1]] = "P"
            matrix[player[0][0]+1][player[0][1]] = "."
    elif command == "L":
        pass
    elif command == "R":
        pass
    elif command == "U":
        pass
    if won_game:
        for row in matrix:
            print(*row, sep='')
        print(f"won: {player[0][0]} {player[0][1]}")
        break

