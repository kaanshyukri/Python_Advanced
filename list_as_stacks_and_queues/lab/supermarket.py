from collections import deque

stack = deque()
name = input()

while name != "End":
    if name == "Paid":
        while stack:
            print(stack.popleft())
    else:
        stack.append(name)
    name = input()
print(f"{len(stack)} people remaining.")
