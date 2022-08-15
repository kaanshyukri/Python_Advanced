from collections import deque

liters = int(input())
stack = deque()
name = input()
while name != "Start":
    stack.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        if int(command) <= liters:
            print(f"{stack.popleft()} got water")
            liters -= int(command)
        else:
            print(f"{stack.popleft()} must wait")
    else:
        command = command.split()
        liters += int(command[1])
    command = input()

print(f"{liters} liters left")
