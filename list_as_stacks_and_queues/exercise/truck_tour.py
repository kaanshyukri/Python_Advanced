from collections import deque

n = int(input())
pumps = deque()
for _ in range(n):
    petrol_pumps = [int(x) for x in input().split()]
    pumps.append(petrol_pumps)

for attempt in range(n):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        #pumps.rotate(-1)
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
