def check_for_items(row, col):
    global decoration
    global gifts
    global cookies
    global all_items
    global all_collected
    if matrix[position_row][position_col] == "D":
        decoration += 1
        all_items -= 1
    elif matrix[position_row][position_col] == "G":
        gifts += 1
        all_items -= 1
    elif matrix[position_row][position_col] == "C":
        cookies += 1
        all_items -= 1
    if all_items == 0:
        all_collected = True
        print("Merry Christmas!")
        matrix[position_row][position_col] = "Y"


rows, cols = [int(x) for x in input().split(", ")]
matrix = []
position_row = 0
position_col = 0
all_items = 0
for row in range(rows):
    row_input = input().split()
    matrix.append(row_input)
    if "Y" in row_input:
        position_row = row
        position_col = row_input.index("Y")
    if "C" in row_input or "D" in row_input or "G" in row_input:
        all_items += row_input.count("C")
        all_items += row_input.count("D")
        all_items += row_input.count("G")

decoration = 0
gifts = 0
cookies = 0
all_collected = False
command = input()

while command != "End":
    side, steps = command.split("-")
    steps = int(steps)
    if side == "up":
        while steps > 0:
            matrix[position_row][position_col] = "x"
            position_row -= 1
            steps -= 1
            if position_row < 0:
                position_row = rows - 1
            check_for_items(position_row, position_col)
            if all_collected:
                break
            matrix[position_row][position_col] = "Y"
    elif side == "down":
        while steps > 0:
            matrix[position_row][position_col] = "x"
            position_row += 1
            steps -= 1
            if position_row >= rows:
                position_row = 0
            check_for_items(position_row, position_col)
            if all_collected:
                break
            matrix[position_row][position_col] = "Y"
    elif side == "left":
        while steps > 0:
            matrix[position_row][position_col] = "x"
            position_col -= 1
            steps -= 1
            if position_col < 0:
                position_col = cols - 1
            check_for_items(position_row, position_col)
            if all_collected:
                break
            matrix[position_row][position_col] = "Y"
    elif side == "right":
        while steps > 0:
            matrix[position_row][position_col] = "x"
            position_col += 1
            steps -= 1
            if position_col >= cols:
                position_col = 0
            check_for_items(position_row, position_col)
            if all_collected:
                break
            matrix[position_row][position_col] = "Y"
    if all_collected:
        break
    command = input()

print("You've collected:")
print(f"- {decoration} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for el in matrix:
    print(*el)
