from collections import deque

materials_list = [int(x) for x in input().split()]
magic_list = deque([int(x) for x in input().split()])

presents = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}
success = False
while materials_list and magic_list:
    material = materials_list.pop()
    magic = magic_list.popleft()
    result = material + magic
    if result < 100:
        if result % 2 == 0:
            result = material * 2 + magic * 3
        else:
            result = result * 2
    elif result > 499:
        result = result / 2
    if 100 <= result <= 199:
        presents["Gemstone"] += 1
    elif 200 <= result <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        presents["Gold"] += 1
    elif 400 <= result <= 499:
        presents["Diamond Jewellery"] += 1
    if presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0 or \
            presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0:
        success = True

if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_list:
    print(f"Materials left: {', '.join([str(x) for x in materials_list])}")
if magic_list:
    print(f"Magic left: {', '.join([str(x) for x in magic_list])}")

sorted_presents = sorted(presents.items(), key=lambda x: x[0])
for key, value in sorted_presents:
    if value > 0:
        print(f"{key}: {value}")
