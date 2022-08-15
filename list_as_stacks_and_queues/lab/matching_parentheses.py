from collections import deque

formula = input()
stack = deque()
for index in range(len(formula)):
    if formula[index] == "(":
        stack.append(index)
    elif formula[index] == ")":
        brace = stack.pop()
        print(formula[brace:index+1])

