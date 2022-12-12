def solution(n):
    answer = ''
    kind = ['1', '2', '4']

    while n > 0:
        n -= 1
        answer = kind[n % 3] + answer
        n = n // 3

    return answer
