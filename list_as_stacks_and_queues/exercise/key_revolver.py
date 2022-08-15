from collections import deque

price_of_bullet = int(input())
gun_barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligance = int(input())
bullet_used = 0
condition = True
barrel = 0
while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        condition = False
        break
    elif locks:
        barrel += 1
        bullet = bullets.pop()
        bullet_used += 1
        if bullet <= locks[0]:
            print("Bang!")
            locks.popleft()
        else:
            print("Ping!")
        if barrel == gun_barrel:
            if bullets:
                barrel = 0
                print("Reloading!")

if condition:
    earned_money = intelligance - (bullet_used * price_of_bullet)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
