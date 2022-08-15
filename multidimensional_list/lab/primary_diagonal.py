n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))
result = 0

for i in range(n):
    for j in range(n):
        if i == j:
            result += matrix[i][j]

print(result)
