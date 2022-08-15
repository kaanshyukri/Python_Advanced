n = int(input())
even = set()
odd = set()
for index in range(1, n+1):
    number = [ord(ch) for ch in input()]
    final_num = sum(number) // index
    if final_num % 2 == 0:
        even.add(final_num)
    else:
        odd.add(final_num)

if sum(even) == sum(odd):
    numbers = even.union(odd)
    print(*numbers, sep=", ")
elif sum(even) < sum(odd):
    numbers = odd.difference(even)
    print(*numbers, sep=", ")
else:
    numbers = even.symmetric_difference(odd)
    print(*numbers, sep=", ")
