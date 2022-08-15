def even_odd(*args):
    command = args[-1]
    number = 0 if command == "even" else 1
    num_list = []
    for index in range(len(args)-1):
        if args[index] % 2 == number:
            num_list.append(args[index])

    return num_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))