from itertools import product


def solution(word):
    LEN_WORD = 5
    alphabets = ["A", "E", "I", "O", "U"]
    words = []

    for num_char in range(1, LEN_WORD + 1):
        for word_tuple in product(alphabets, repeat=num_char):
            words.append("".join(word_tuple))

    return sorted(words).index(word) + 1
