rows = 6
matrix = []
for _ in range(rows):
    matrix.append(list(input().split()))
row = 0
col = 0
points = 0
numbers = []
numbers_set = set()
for _ in range(3):
    information = eval(input())
    if information in numbers_set:
        continue
    numbers_set.add(information)
    row = information[0]
    col = information[1]
    if row > rows-1 or col > rows -1:
        continue
    if matrix[row][col] == "B":
        for _ in range(rows-1):
            row -= 1
            if row < 0:
                row = rows - 1
            points += int(matrix[row][col])

prize = ""
if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if 100 <= points <= 199:
        prize = "Football"
    elif 200 <= points <= 299:
        prize = "Teddy Bear"
    elif points >= 300:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {points} points, and you've won {prize}.")