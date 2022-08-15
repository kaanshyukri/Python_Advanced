rows = int(input())
matrix = []
player_row = 0
player_col = 0
player_path = []
for row in range(rows):
    row_input = input().split()
    matrix.append(row_input)
    if "P" in row_input:
        player_row = row
        player_col = row_input.index("P")

player_path.append([player_row, player_col])
game_is_finished = False
coins = 0
matrix[player_row][player_col] = "0"
while coins < 100:
    command = input()
    if command == "up":
        player_row -= 1
        if player_row < 0:
            player_row = rows - 1
    elif command == "down":
        player_row += 1
        if player_row >= rows:
            player_row = 0
    elif command == "left":
        player_col -= 1
        if player_col < 0:
            player_col = rows - 1
    elif command == "right":
        player_col += 1
        if player_col >= rows:
            player_col = 0
    player_path.append([player_row, player_col])
    if matrix[player_row][player_col] == "X":
        game_is_finished = True
        print(f"Game over! You've collected {coins //2} coins.")
        break
    else:
        coins += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = "0"

if not game_is_finished:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
for path in player_path:
    print(path)
