from collections import deque

bees = deque(map(int, input().split()))
nectars = deque(map(int, input().split()))
symbol = deque(input().split())
honey = 0
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if bee <= nectar:
        s = symbol.popleft()
        if s == "+":
            honey += bee + nectar
        elif s == "-":
            honey += abs(bee - nectar)
        elif s == "*":
            honey += bee * nectar
        elif s == "/":
            if bee == 0:
                pass
            else:
                honey += bee / nectar
    else:
        bees.appendleft(bee)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
