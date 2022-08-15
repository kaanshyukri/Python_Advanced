def operate(action, *args):
    result = 0
    if action == "+":
        for el in args:
            result += el
    elif action == "-":
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
    elif action == "*":
        result = 1
        for el in args:
            result *= el
    elif action == "/":
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
    return result


print(operate("+", 10, 1))
print(operate("*", 3, 4, 5, 6))

