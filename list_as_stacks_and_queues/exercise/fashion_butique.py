from collections import deque

clothes = deque(map(int, input().split()))
capacity = int(input())
rack = 1
sum_of_rack = 0
for _ in range(len(clothes)):
        current_clothing = clothes.pop()
        sum_of_rack += current_clothing
        if sum_of_rack == capacity:
            sum_of_rack = 0
            if clothes:
                rack += 1
        elif sum_of_rack > capacity:
            sum_of_rack = 0
            sum_of_rack += current_clothing
            rack += 1


print(rack)