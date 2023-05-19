from collections import defaultdict


def solution(n, words):
    passed_words = []
    prev_word = ""
    cnt_dict = defaultdict(int)

    for idx, word in enumerate(words):
        participant_idx = idx % n + 1
        if idx == 0 or prev_word[-1] == word[0]:
            if word not in passed_words:
                cnt_dict[participant_idx] += 1
                passed_words.append(word)
                prev_word = word
                continue

        return [participant_idx, cnt_dict[participant_idx] + 1]

    return [0, 0]
