n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary = []

for i in range(n):
    for j in range(n):
        if i == j:
            primary.append(matrix[i][j])
secondary = []
for r in range(n):
    for k in range(n-1, -1, -1):
        secondary.append(matrix[r][k])
        n -= 1
        break

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
