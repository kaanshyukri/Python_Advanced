from collections import deque

elves_energy = deque([int(x) for x in input().split()])
toys = [int(x) for x in input().split()]
days = 1
toys_count = 0
energy_count = 0
finished = False
not_enough_energy = False
while elves_energy and toys:
    not_enough_energy = False
    elf = elves_energy.popleft()
    toy = toys.pop()
    while elf < 5:
        if elves_energy:
            elf = elves_energy.popleft()
        else:
            toys.append(toy)
            finished = True
            break
    if finished:
        break
    if days % 15 == 0:
        if elf >= toy * 2:
            elves_energy.append(elf - toy * 2)
            energy_count += toy * 2
        else:
            not_enough_energy = True
    elif days % 3 == 0:
        if elf >= toy * 2:
            elves_energy.append((elf + 1) - (toy * 2))
            toys_count += 2
            energy_count += toy * 2
        else:
            not_enough_energy = True
    elif days % 5 == 0:
        if elf >= toy:
            elves_energy.append(elf - toy)
            energy_count += toy
        else:
            not_enough_energy = True
    else:
        if elf >= toy:
            elves_energy.append(elf - toy + 1)
            energy_count += toy
            toys_count += 1
        else:
            not_enough_energy = True
    days += 1
    if not_enough_energy:
        elves_energy.append(elf * 2)
        toys.append(toy)

print(f"Toys: {toys_count}")
print(f"Energy: {energy_count}")
if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
if toys:
    print(f"Boxes left: {', '.join([str(x) for x in toys])}")
