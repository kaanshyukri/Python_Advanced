from collections import deque

chocolate = deque(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))
milkshakes = 0

while milkshakes < 5 and chocolate and milk_cups:
    last_chocolate = chocolate.pop()
    first_cup = milk_cups.popleft()

    if last_chocolate <= 0 and first_cup <= 0:
        continue
    if last_chocolate <= 0:
        milk_cups.appendleft(first_cup)
        continue
    if first_cup <= 0:
        chocolate.append(last_chocolate)
        continue
    if last_chocolate == first_cup:
        milkshakes += 1
    else:
        chocolate.append(last_chocolate - 5)
        milk_cups.append(first_cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")
