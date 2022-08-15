def start_end(nums):
    f, s = [int(x) for x in nums.split(",")]
    return set(range(f, s+1))


n = int(input())
current_intersection = set()
for _ in range(n):
    command = input().split("-")
    first = start_end(command[0])
    second = start_end(command[1])
    elements = first.intersection(second)
    if len(elements) > len(current_intersection):
        current_intersection = elements

print(f"Longest intersection is {[x for x in current_intersection]} with length {len(current_intersection)}")
