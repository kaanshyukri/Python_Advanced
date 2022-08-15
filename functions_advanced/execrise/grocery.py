def grocery_store(**kwargs):
    result = [f"{key}: {value}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
