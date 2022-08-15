from collections import deque

pizza_list = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
pizza_made = 0
while pizza_list and employees:
    pizza_count = pizza_list.popleft()
    if pizza_count > 10 or pizza_count <= 0:
        continue
    pizza = pizza_count
    while pizza_count > 0:
        pizza_count -= employees.pop()
        if pizza_count <= 0:
            pizza_made += pizza
        if not employees:
            pizza_list.appendleft(pizza_count)
            break


if employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_made}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_list])}")
