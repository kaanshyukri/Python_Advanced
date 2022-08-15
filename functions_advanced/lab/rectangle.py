def rectangle(a, b):
    result = ""
    if a != int(a) or b != int(b):
        return "Enter valid values!"
    else:
        return f"Rectangle area: {a * b}\nRectangle perimeter: {2 *(a + b)}"


print(rectangle(2, 10))