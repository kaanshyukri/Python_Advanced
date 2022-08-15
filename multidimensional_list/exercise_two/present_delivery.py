def check():
    global nice_kids
    global presents
    if neighbourhood[santa_row - 1][santa_col] != "-":
        if neighbourhood[santa_row - 1][santa_col] == "V":
            nice_kids -= 1
        presents -= 1
        neighbourhood[santa_row - 1][santa_col] = "-"
    if neighbourhood[santa_row + 1][santa_col] != "-":
        if neighbourhood[santa_row + 1][santa_col] == "V":
            nice_kids -= 1
        presents -= 1
        neighbourhood[santa_row + 1][santa_col] = "-"
    if neighbourhood[santa_row][santa_col - 1] != "-":
        if neighbourhood[santa_row][santa_col - 1] == "V":
            nice_kids -= 1
        neighbourhood[santa_row][santa_col - 1] = "-"
        presents -= 1
    if neighbourhood[santa_row][santa_col + 1] != "-":
        if neighbourhood[santa_row][santa_col + 1] == "V":
            nice_kids -= 1
        presents -= 1
        neighbourhood[santa_row][santa_col + 1] = "-"
    return neighbourhood


presents = int(input())
rows = int(input())
neighbourhood = []
santa_row = 0
santa_col = 0
checked = False
nice_kids = 0
happy_kids = 0
for r in range(rows):
    row = input().split()
    neighbourhood.append(row)
    for c in range(rows):
        if neighbourhood[r][c] == "S":
            santa_row = r
            santa_col = c
        if neighbourhood[r][c] == "V":
            nice_kids += 1
            happy_kids += 1


command = input()
while command != "Christmas morning":
    neighbourhood[santa_row][santa_col] = "-"
    if command == "up":
        if 0 <= santa_row - 1 < rows:
            santa_row -= 1
            if neighbourhood[santa_row][santa_col] == "V":
                presents -= 1
                nice_kids -= 1
            elif neighbourhood[santa_row][santa_col] == "C":
                neighbourhood = check()
    elif command == "right":
        if 0 <= santa_col + 1 < rows:
            santa_col += 1
            if neighbourhood[santa_row][santa_col] == "V":
                presents -= 1
                nice_kids -= 1
            elif neighbourhood[santa_row][santa_col] == "C":
                neighbourhood = check()
    elif command == "left":
        if 0 <= santa_col - 1 < rows:
            santa_col -= 1
            if neighbourhood[santa_row][santa_col] == "V":
                presents -= 1
                nice_kids -= 1
            elif neighbourhood[santa_row][santa_col] == "C":
                neighbourhood = check()
    elif command == "down":
        if 0 <= santa_row + 1 < rows:
            santa_row += 1
            if neighbourhood[santa_row][santa_col] == "V":
                presents -= 1
                nice_kids -= 1
            elif neighbourhood[santa_row][santa_col] == "C":
                neighbourhood = check()
    neighbourhood[santa_row][santa_col] = "S"
    if presents == 0:
        if nice_kids > 0:
            print("Santa ran out of presents!")
        break
    command = input()

for row in neighbourhood:
    print(*row, sep=" ")

if nice_kids == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
