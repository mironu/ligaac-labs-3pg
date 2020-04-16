def count1(words_list):
    word_count = {}
    for word in words_list:
        if word.isnumeric():
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
    return {k: v for k, v in sorted(word_count.items(), key=lambda x: x[1])}


if __name__ == "__main__":
    my_string = "We are having 3 numbers of 5 pieces and each of them 2 are having 3 stars 5 3 3"

    words = my_string.split(" ")
    print(count1(words))

