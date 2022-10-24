from functools import reduce


def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    diff = []
    for i in range(len(A)):
        diff.append(A[i] * B[i])

    return reduce(lambda x, y: x + y, diff)
