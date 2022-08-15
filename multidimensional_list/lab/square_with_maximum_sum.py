rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
max_number = -999
max_list = None
numbers = None
for row in range(rows-1):
    for col in range(columns-1):
        numbers = [matrix[row][col], matrix[row+1][col], matrix[row][col+1], matrix[row+1][col+1]]
        if sum(numbers) > max_number:
            max_list = numbers
            max_number = sum(numbers)

print(max_list[0], max_list[2])
print(max_list[1], max_list[3])
print(sum(max_list))
