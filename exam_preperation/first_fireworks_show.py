from collections import deque

firework_effect = deque([int(x) for x in input().split(", ") if int(x) > 0])
explosive_power = [int(x) for x in input().split(", ") if int(x) > 0]
successfully_prepared = False
fireworks_dict = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
while firework_effect and explosive_power:
    firework = firework_effect.popleft()
    power = explosive_power.pop()
    result = firework + power
    if result % 3 == 0 and result % 5 != 0:
        fireworks_dict["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        fireworks_dict["Willow Fireworks"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        fireworks_dict["Crossette Fireworks"] += 1
    else:
        if firework - 1 > 0:
            firework_effect.append(firework - 1)
        explosive_power.append(power)
    if fireworks_dict["Palm Fireworks"] >= 3 and fireworks_dict["Willow Fireworks"] >= 3 \
            and fireworks_dict["Crossette Fireworks"] >= 3:
        successfully_prepared = True
        break

if successfully_prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effect])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in fireworks_dict.items():
    print(f"{key}: {value}")
