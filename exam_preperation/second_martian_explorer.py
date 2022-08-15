rows = 6
matrix = []
rover_row = 0
rover_col = 0
for row in range(rows):
    row_input = input().split()
    matrix.append(row_input)
    if "E" in row_input:
        rover_row = row
        rover_col = row_input.index("E")

deposit = {"W": [], "M": [], "C": []}
deposit_name = ""
commands = input().split(", ")
game_finished = False
suitable = False
for command in commands:
    if command == "up":
        rover_row -= 1
        if rover_row < 0:
            rover_row = rows - 1
    elif command == "down":
        rover_row += 1
        if rover_row >= rows:
            rover_row = 0
    elif command == "left":
        rover_col -= 1
        if rover_col < 0:
            rover_col = rows - 1
    elif command == "right":
        rover_col += 1
        if rover_col >= rows:
            rover_col = 0
    if matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        game_finished = True
        break
    if matrix[rover_row][rover_col] == "W" or matrix[rover_row][rover_col] == "M" or matrix[rover_row][rover_col] == "C":
        if matrix[rover_row][rover_col] == "W":
            deposit_name = "Water"
            deposit["W"].append([rover_row, rover_col])
        elif matrix[rover_row][rover_col] == "M":
            deposit_name = "Metal"
            deposit["M"].append([rover_row, rover_col])
        elif matrix[rover_row][rover_col] == "C":
            deposit_name = "Concrete"
            deposit["C"].append([rover_row, rover_col])
        print(f"{deposit_name} deposit found at ({rover_row}, {rover_col})")
    matrix[rover_row][rover_col] = "-"
    if deposit["W"] and deposit["M"] and deposit["C"]:
        suitable = True

if suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
