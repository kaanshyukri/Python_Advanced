from math import ceil
name_one, name_two = [x for x in input().split(", ")]
matrix = [input().split() for x in range(7)]
player_one = 501
player_two = 501
player = 1
result = 0
while True:
    row, col = eval(input())
    if not 0 <= row < 7 or not 0 <= col < 7:
        player += 1
        continue
    if matrix[row][col] == "B":
        break
    elif matrix[row][col] == "T":
        result = (int(matrix[0][col]) + int(matrix[row][0]) + int(matrix[6][col]) + int(matrix[row][6])) * 3
    elif matrix[row][col] == "D":
        result = (int(matrix[0][col]) + int(matrix[row][0]) + int(matrix[6][col]) + int(matrix[row][6])) * 2
    else:
        result = int(matrix[row][col])
    if player % 2 == 0:
        player_two -= result
    else:
        player_one -= result
    if player_one <= 0 or player_two <= 0:
        break
    player += 1

if player % 2 == 0:
    print(f"{name_two} won the game with {player//2} throws!")
else:
    print(f"{name_one} won the game with {ceil(player/2)} throws!")

