from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = deque([int(x) for x in input().split() if int(x) > 0])
matches = 0
no_males = False
no_females = False
while males and females:
    male = males.pop()
    female = females.popleft()
    while male % 25 == 0:
        for _ in range(2):
            if males:
                male = males.pop()
            else:
                no_males = True
                break
        if no_males:
            break
    while female % 25 == 0:
        for _ in range(2):
            if females:
                female = females.popleft()
            else:
                no_females = True
                break
        if no_females:
            break
    if no_males or no_females:
        break
    else:
        if male == female:
            matches += 1
        else:
            if male - 2 > 0:
                males.append(male - 2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print(f"Females left: none")
