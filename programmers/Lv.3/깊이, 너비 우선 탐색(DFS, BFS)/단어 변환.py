from functools import reduce


def check_visitable(cur_word, tar_word):
    identical_char_cnt = reduce(lambda acc, cur: acc + int(cur[0] == cur[1]), zip(cur_word, tar_word), 0)
    if identical_char_cnt == len(cur_word) - 1:
        return True
    return False


def dfs(current, target, words, visit, temp, cnt):
    if current == target:
        return temp.append(cnt)

    for i in range(len(words)):
        if not visit[i]:
            if check_visitable(current, words[i]):
                visit[i] = 1
                dfs(words[i], target, words, visit, temp, cnt + 1)
                visit[i] = 0


def solution(begin, target, words):
    if target not in words: return 0

    visit = [0] * len(words)
    temp = []
    dfs(begin, target, words, visit, temp, 0)

    if temp:
        return min(temp)
    return 0
