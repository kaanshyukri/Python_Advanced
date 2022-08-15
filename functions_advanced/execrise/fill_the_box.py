def fill_the_box(h, l, w, *args):
    box = h * l * w
    cubes = 0
    for command in args:
        if command == "Finish":
            break
        cubes += command
    if box >= cubes:
        return f"There is free space in the box. You could put {box - cubes} more cubes."
    else:
        return f"No more free space! You have {abs(box - cubes)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))