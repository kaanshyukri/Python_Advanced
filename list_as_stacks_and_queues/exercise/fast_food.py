from collections import deque

quantity_of_food = int(input())
orders = deque(map(int, input().split()))
condition = True

print(max(orders))
for _ in range(len(orders)):
    if quantity_of_food >= orders[0]:
        order = orders.popleft()
        quantity_of_food -= order
    else:
        condition = False
        new_list = deque(map(str, orders))
        print(f"Orders left: {' '.join(new_list)}")
        break

if condition:
    print("Orders complete")
