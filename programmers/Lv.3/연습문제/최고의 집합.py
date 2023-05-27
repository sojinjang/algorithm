def solution(n, s):
    if not s // n: return [-1]

    answer = [s // n for _ in range(n)]
    for i in range(1, s % n + 1):
        answer[-i] += 1

    return answer
