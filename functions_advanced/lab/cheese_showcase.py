def sorting_cheeses(**kwargs):
    result = ''
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in kwargs:
        result += tuple_[0] + '\n'
        quantity_list = sorted(tuple_[1], reverse=True)
        result += '\n'.join(map(str, quantity_list)) + '\n'
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
