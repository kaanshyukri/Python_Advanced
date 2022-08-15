rows, columns = [int(x) for x in input().split(", ")]
matrix = []
sum_of_column = 0

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for column in range(columns):
    sum_of_column = 0
    for row in range(rows):
        sum_of_column += matrix[row][column]
    print(sum_of_column)
