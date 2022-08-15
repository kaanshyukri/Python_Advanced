def start_spring(**kwargs):
    spring_dict = {}
    result = ""
    for key, value in kwargs.items():
        if value not in spring_dict:
            spring_dict[value] = []
        spring_dict[value].append(key)
    spring_dict = dict(sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in spring_dict.items():
        if value:
            result += key + ":" '\n'
        for v in sorted(value):
            result += "-" + v + "\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
