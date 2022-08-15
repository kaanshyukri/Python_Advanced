rows, columns = [int(x) for x in input().split()]
word = input()
dex = 0

for row in range(rows):
    row_elements = []
    if row % 2 == 0:
        for col in range(columns):
            result = word[dex % len(word)]
            row_elements.append(result)
            dex += 1
        print(*row_elements, sep='')
    else:
        for col in range(columns):
            result = word[dex % len(word)]
            row_elements.append(result)
            dex += 1
        print(*reversed(row_elements), sep='')
