from collections import deque

parentheses = input()
stack = deque()
balanced = True
for ch in parentheses:
    if ch in '[{(':
        stack.append(ch)
    elif not stack:
        balanced = False
        break
    else:
        if f'{stack.pop()}{ch}' not in '[]{}()':
            balanced = False
            break

if balanced and not stack:
    print("YES")
else:
    print("NO")
