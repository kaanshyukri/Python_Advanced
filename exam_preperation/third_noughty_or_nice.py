def naughty_or_nice_list(santa_list, *args, **kwargs):
    kids_dict = {"Nice": [], "Naughty": [], "Not found": []}
    result = ""
    for elements in args:
        elements = elements.split("-")
        if santa_list.count(int(elements[0])) == 1:
            pass
            if elements[0] == "Nice":
                pass
    for final, step in kids_dict.items():
        if step:
            result += f"{final}: {', '.join(step)}\n"
    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
