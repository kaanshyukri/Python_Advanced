m, n = [int(x) for x in input().split()]

first = set()
second = set()
for _ in range(m):
    first.add(input())

for _ in range(n):
    second.add(input())

unique_elements = first.intersection(second)
print('\n'.join(unique_elements))

