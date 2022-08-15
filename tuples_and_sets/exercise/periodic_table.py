n = int(input())
elements = set()

for _ in range(n):
    command = input().split()
    elements = elements.union(command)

for el in elements:
    print(el)