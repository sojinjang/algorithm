from functools import reduce


def solution(n):
    return reduce(lambda x, y: int(x) + int(y), str(n)) if n > 10 else n
