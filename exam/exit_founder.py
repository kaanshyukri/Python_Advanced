player_one, player_two = input().split(", ")
player = 1
one_condition = False
two_condition = False
game_end = False
rows = 6
matrix = []

for _ in range(rows):
    matrix.append(list(input().split()))

while not game_end:
    row, col = eval(input())
    if player % 2 == 0 and two_condition:
        player += 1
        two_condition = False
        continue
    elif player % 2 != 0 and one_condition:
        player += 1
        one_condition = False
        continue
    if matrix[row][col] == "W":
        if player % 2 == 0:
            print(f"{player_two} hits a wall and needs to rest.")
            two_condition = True
        else:
            print(f"{player_one} hits a wall and needs to rest.")
            one_condition = True
    elif matrix[row][col] == "T":
        if player % 2 == 0:
            print(f"{player_two} is out of the game! The winner is {player_one}.")
        else:
            print(f"{player_one} is out of the game! The winner is {player_two}.")
        game_end = True
    elif matrix[row][col] == "E":
        if player % 2 == 0:
            print(f"{player_two} found the Exit and wins the game!")
        else:
            print(f"{player_one} found the Exit and wins the game!")
        game_end = True
    player += 1
    if game_end:
        break
