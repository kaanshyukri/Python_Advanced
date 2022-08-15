text = input()
rows = int(input())

matrix = []
row_p = 0
col_p = 0
for row in range(rows):
    row_input = list(input())
    matrix.append(row_input)
    if "P" in row_input:
        row_p = row
        col_p = row_input.index("P")


punished = False
command_count = int(input())
for _ in range(command_count):
    matrix[row_p][col_p] = "-"
    command = input()
    if command == "up":
        row_p -= 1
        if row_p < 0:
            row_p = 0
            punished = True
    elif command == "down":
        row_p += 1
        if row_p == rows:
            row_p = rows - 1
            punished = True
    elif command == "left":
        col_p -= 1
        if col_p < 0:
            col_p = 0
            punished = True
    elif command == "right":
        col_p += 1
        if col_p == rows:
            col_p = rows - 1
            punished = True
    if punished:
        matrix[row_p][col_p] = "P"
        if len(text) > 1:
            text = text[0:len(text)-1]
        else:
            text = ""
        punished = False
    else:
        if matrix[row_p][col_p] != "-":
            text += matrix[row_p][col_p]
        matrix[row_p][col_p] = "P"


print(text)
for element in matrix:
    print(f"{''.join(element)}")
