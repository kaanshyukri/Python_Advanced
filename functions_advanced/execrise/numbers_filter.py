def even_odd_filter(**kwargs):
    dict_nums = {}
    for key, value in kwargs.items():
        num_list = []
        num = 0 if key == "even" else 1
        if key == "odd":
            for v in value:
                if v % 2 == num:
                    num_list.append(v)
            dict_nums["odd"] = num_list
        else:
            if key == "even":
                for v in value:
                    if v % 2 == num:
                        num_list.append(v)
                dict_nums["even"] = num_list
    return dict(sorted(dict_nums.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
