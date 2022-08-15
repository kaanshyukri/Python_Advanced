from collections import deque

ramen_list = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while ramen_list and customers:
    ramen = ramen_list.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue
    elif ramen > customer:
        ramen -= customer
        customer = 0
    else:
        customer -= ramen
        ramen = 0
    if ramen > 0:
        ramen_list.append(ramen)
    if customer > 0:
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen_list:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen_list])}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
