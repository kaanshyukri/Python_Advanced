from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted = 0
condition = True
while cups:
    if bottles:
        bottle = bottles.pop()
        if bottle >= cups[0]:
            wasted += bottle - cups[0]
            cups.popleft()
        else:
            cups[0] -= bottle
    else:
        condition = False
        break

if condition:
    bottles_list = [str(x) for x in bottles]
    print(f"Bottles: {' '.join(bottles_list)}")
else:
    cup_list = [str(x) for x in cups]
    print(f"Cups: {' '.join(cup_list)}")
print(f"Wasted litters of water: {wasted}")
