from collections import deque
operators = input().split()
numbers = deque()
for ch in operators:
    if ch in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            if ch == "+":
                result = first + second
            elif ch == "-":
                result = first - second
            elif ch == "*":
                result = first * second
            else:
                result = first // second
            numbers.appendleft(result)
    else:
        numbers.append(int(ch))

print(numbers.popleft())
