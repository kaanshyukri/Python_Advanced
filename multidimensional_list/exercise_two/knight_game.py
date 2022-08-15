rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(input()))

my_dict = {}
removed_knights = 0
best_key = 0
best_row = 0
best_col = 0
while True:
    for row in range(rows):
        for col in range(rows):
            result = 0
            if matrix[row][col] == "K":
                if 0 <= row + 2 < rows and 0 <= col + 1 < rows:
                    if matrix[row + 2][col + 1] == "K":
                        result += 1
                if 0 <= row + 2 < rows and 0 <= col - 1 < rows:
                    if matrix[row + 2][col - 1] == "K":
                        result += 1
                if 0 <= row + 1 < rows and 0 <= col - 2 < rows:
                    if matrix[row + 1][col - 2] == "K":
                        result += 1
                if 0 <= row + 1 < rows and 0 <= col + 2 < rows:
                    if matrix[row + 1][col + 2] == "K":
                        result += 1
                if 0 <= row - 1 < rows and 0 <= col - 2 < rows:
                    if matrix[row - 1][col - 2] == "K":
                        result += 1
                if 0 <= row - 1 < rows and 0 <= col + 2 < rows:
                    if matrix[row - 1][col + 2] == "K":
                        result += 1
                if 0 <= row - 2 < rows and 0 <= col - 1 < rows:
                    if matrix[row - 2][col - 1] == "K":
                        result += 1
                if 0 <= row - 2 < rows and 0 <= col + 1 < rows:
                    if matrix[row - 2][col + 1] == "K":
                        result += 1
                if result > 0:
                    my_dict[(row, col)] = result
    if len(my_dict) > 0:
        for key, value in my_dict.items():
            if value > best_key:
                best_key = value
                best_row = key[0]
                best_col = key[1]
        matrix[best_row][best_col] = "0"
        removed_knights += 1
        best_key = 0
        my_dict.clear()
    else:
        break

print(removed_knights)

