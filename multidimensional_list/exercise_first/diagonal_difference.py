n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(" ")])

primary = 0

for i in range(n):
    for j in range(n):
        if i == j:
            primary += matrix[i][j]
secondary = 0
for r in range(n):
    for k in range(n-1, -1, -1):
        secondary += matrix[r][k]
        n -= 1
        break

print(abs(primary - secondary))
