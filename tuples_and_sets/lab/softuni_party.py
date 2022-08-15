n = int(input())
guest_list = set()

for _ in range(n):
    guest_list.add(input())

command = input()

while command != "END":
    if command in guest_list:
        guest_list.remove(command)
    command = input()

guest_list = sorted(guest_list)

print(len(guest_list))
print('\n'.join(guest_list))
