rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
max_number = -999

max_list = []
for row in range(rows-2):
    for col in range(columns-2):
        numbers = [matrix[row][col], matrix[row][col+1], matrix[row][col+2], matrix[row+1][col], matrix[row+1][col+1],
                   matrix[row+1][col+2], matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]
        if sum(numbers) > max_number:
            max_list = numbers
            max_number = sum(numbers)

print(f"Sum = {sum(max_list)}")
print(f"{max_list[0]} {max_list[1]} {max_list[2]}")
print(f"{max_list[3]} {max_list[4]} {max_list[5]}")
print(f"{max_list[6]} {max_list[7]} {max_list[8]}")
