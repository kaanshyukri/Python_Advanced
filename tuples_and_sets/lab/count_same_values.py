numbers = tuple(map(float, input().split()))

numbers_count = {}
for num in numbers:
    if num not in numbers_count:
        numbers_count[num] = 0
    numbers_count[num] += 1

[print(f"{key:.1f} - {value} times") for key, value in numbers_count.items()]
