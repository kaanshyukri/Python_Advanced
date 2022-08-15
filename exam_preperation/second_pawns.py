def check(row, col):
    global game_finished
    global a_capture
    global b_capture
    if matrix[row][col] == "w":
        matrix[row][col] = "-"
        if col == 0:
            if matrix[row-1][col+1] != "-":
                col += 1
                a_capture = True
        elif col == 7:
            if matrix[row-1][col-1] != "-":
                col -= 1
                a_capture = True
        else:
            if matrix[row - 1][col - 1] != "-":
                col -= 1
                a_capture = True
            elif matrix[row-1][col+1] != "-":
                col += 1
                a_capture = True
        row -= 1
        if row == 0:
            game_finished = True
        matrix[row][col] = "w"
    elif matrix[row][col] == "b":
        matrix[row][col] = "-"
        if col == 0:
            if matrix[row+1][col+1] != "-":
                col += 1
                b_capture = True
        elif col == 7:
            if matrix[row+1][col-1] != "-":
                col -= 1
                b_capture = True
        else:
            if matrix[row+1][col-1] != "-":
                col -= 1
                b_capture = True
            elif matrix[row+1][col+1] != "-":
                col += 1
                b_capture = True
        row += 1
        if row == 7:
            game_finished = True
        matrix[row][col] = "b"
    return row, col


rows = 8
matrix = []
white = []
black = []

for row in range(rows):
    row_input = input().split()
    matrix.append(row_input)
    if "w" in row_input:
        white.append(row)
        white.append(row_input.index("w"))
    if "b" in row_input:
        black.append(row)
        black.append(row_input.index("b"))

game_finished = False
b_capture = False
a_capture = False
while not game_finished:
    white[0], white[1] = check(white[0], white[1])
    black[0], black[1] = check(black[0], black[1])
    if a_capture or b_capture or game_finished:
        break


if game_finished:
    if white[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white[1])+ chr(56 - white[0])}.")
    elif black[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black[1]) + chr(56 - black[0])}.")

if a_capture:
    print(f"Game over! White win, capture on {chr(97 + white[1])+ chr(56 - white[0])}.")
if b_capture:
    print(f"Game over! Black win, capture on {chr(97 + black[1]) + chr(56 - black[0])}.")
