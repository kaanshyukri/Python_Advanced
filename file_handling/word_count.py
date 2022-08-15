import re
words_count = {}
file = open("words.txt", "w")
file.write("quick is fault")
file = open("words.txt", "r")
file_text = open("text.txt", "r")
for line in file:
    for text in file_text:
        for word in line.split():
            regex = fr"\b{word}\b"
            match = re.findall(regex, text.lower())
            if match:
                if word not in words_count:
                    words_count[word] = 0
                words_count[word] += len(match)

sorted_words = sorted(words_count.items(), key=lambda x: (-x[1]))
output_file = open("output.txt", "w")
for key, value in sorted_words:
    output_file.write(f"{key} - {value}\n")
    