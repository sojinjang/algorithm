from itertools import combinations


def solution(n):
    count = 0
    for num_two in range(n//2+1):
        count += len(list(combinations(list([1]*(n-num_two*2)+[2]*num_two), num_two))) if num_two else 1

    return count % 1234567
