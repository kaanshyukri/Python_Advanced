from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
command = input()

cars_counter = 0
crashed = False

while command != "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if free_window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = free_window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")
