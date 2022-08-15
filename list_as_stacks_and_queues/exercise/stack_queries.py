from collections import deque

number = int(input())
stack = deque()
stack_print = deque()

for _ in range(number):
    n = input()
    if len(n) > 1:
        n = n.split()
        stack.append(int(n[1]))
    elif n == '2':
        if stack:
            stack.pop()
    elif n == '3':
        if stack:
            print(max(stack))
    elif n == '4':
        if stack:
            print(min(stack))

for i in range(len(stack)):
    num = stack.popleft()
    stack_print.appendleft(str(num))

print(', '.join(stack_print))
