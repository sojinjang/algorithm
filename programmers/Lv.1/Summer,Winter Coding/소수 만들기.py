import math
from itertools import combinations


def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    cb = list(combinations(nums, 3))
    prime_num_arr = []
    for i in cb:
        if is_prime_num(sum(i)):
            prime_num_arr.append(sum(i))

    return len(prime_num_arr)
