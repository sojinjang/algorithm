import math


def solution(arr):
    answer = arr[0]
    for num in arr:
        answer = (num * answer) // math.gcd(num, answer)
    return answer
