from collections import deque


def solution(n):
    f_dq = deque([1, 2])
    for _ in range(n-3):
        f_dq.append(f_dq[0]+f_dq[1])
        f_dq.popleft()

    return f_dq.pop() % 1234567
