from collections import deque

stack = deque(input().split())
n = int(input())

for _ in range(len(stack)-1):
    stack.rotate(-n)
    print(f"Removed {stack.pop()}")

print(f"Last is {stack.pop()}")
