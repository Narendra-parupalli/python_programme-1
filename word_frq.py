def word_frq(line):
    words_list = line.split()
    print(words_list)
    word_count = {}

    # Count the frequency word in words_list
    for i in words_list:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    # Sorting the words
    sorted_count = sorted(word_count.items())

    return sorted_count

line = "which is better python 2 or python 3"
frequency = word_frq(line)
print(frequency)
# Printing the sorted word frequency
for word, count in frequency:
    print(f"{word}: {count}")