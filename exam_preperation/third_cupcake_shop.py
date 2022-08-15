from collections import deque


def stock_availability(box, *args):
    if args:
        box = deque(box)

        if args[0] == "delivery":
            for index in range(1, len(args)):
                box.append(args[index])
        elif args[0] == "sell":
            if len(args) == 1:
                box.popleft()
            else:
                if str(args[1]).isdigit():
                    for index in range(args[1]):
                        box.popleft()
                        if not box:
                            return list(box)
                else:
                    for index in range(1, len(args)):
                        if args[index] in box:
                            while args[index] in box:
                                box.remove(args[index])
        return list(box)
    else:
        return list(box)


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

print(stock_availability(["cookie"], "delivery"))