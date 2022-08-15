def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        age = kwargs[name[0]]
        result[name] = age
    result = [f"{key} is {value} years old." for key, value in sorted(result.items(), key=lambda x: x[0])]
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


