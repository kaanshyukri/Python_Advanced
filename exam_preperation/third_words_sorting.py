def words_sorting(*args):
    words_dict = {}
    total_sum = 0
    for word in args:
        result = 0
        for w in word:
            result += ord(w)
        total_sum += result
        words_dict[word] = result
    check = "even" if total_sum % 2 == 0 else "odd"
    if check == "even":
        words = [f"{key} - {value}" for key, value in sorted(words_dict.items(), key=lambda x: x[0])]
    else:
        words = [f"{key} - {value}" for key, value in sorted(words_dict.items(), key=lambda x: -x[1])]
    return '\n'.join(words)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

