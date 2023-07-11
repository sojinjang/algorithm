from collections import deque


def solution(priorities, location):
    p_dq = deque(priorities)
    cnt = 0
    cnt = count_order(cnt, p_dq, location)
    return cnt


def count_order(cnt, p_dq, location):
    for i in range(location + 1):
        j = p_dq.popleft()
        if list(filter(lambda x: x > j, p_dq)):
            p_dq.append(j)
            if i == location:
                cnt = count_order(cnt, p_dq, len(p_dq) - 1)
                return cnt
        else:
            cnt += 1
            if i == location:
                return cnt
