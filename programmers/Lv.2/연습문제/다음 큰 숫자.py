from collections import Counter


def solution(n):
    n_count = Counter(bin(n))['1']

    answer = n
    while True:
        answer += 1
        if Counter(bin(answer))['1'] == n_count:
            return answer
