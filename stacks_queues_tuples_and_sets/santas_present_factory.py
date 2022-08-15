from collections import deque

materials = deque(map(int, input().split()))
magic = deque(map(int, input().split()))
toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
while materials and magic:
    material = materials.pop()
    mag = magic.popleft()
    if material < 0 or mag < 0:
        result = abs(mag + material)
        materials.append(result)
    elif material == 0 or mag == 0:
        if material == 0 and mag == 0:
            continue
        elif material == 0:
            magic.appendleft(mag)
        elif mag == 0:
            materials.append(material)
    else:
        result = material * mag
        if result == 150:
            toys["Doll"] += 1
        elif result == 250:
            toys["Wooden train"] += 1
        elif result == 300:
            toys["Teddy bear"] += 1
        elif result == 400:
            toys["Bicycle"] += 1
        else:
            materials.append(material + 15)

if toys["Doll"] > 0 and toys["Wooden train"] > 0 or toys["Teddy bear"] > 0 and toys["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
for key, value in sorted(toys.items()):
    if value > 0:
        print(f"{key}: {value}")
