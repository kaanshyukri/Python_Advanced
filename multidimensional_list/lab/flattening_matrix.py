n = int(input())
matrix = []

for _ in range(n):
    nums = [int(x) for x in input().split(", ")]
    matrix.extend(nums)

print(matrix)
