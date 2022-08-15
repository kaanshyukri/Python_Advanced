rows, columns = [int(x) for x in input().split(", ")]
matrix = []
res = 0
for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    res += sum(nums)
    matrix.append(nums)

print(res)
print(matrix)