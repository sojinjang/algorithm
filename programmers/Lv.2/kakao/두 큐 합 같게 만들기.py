from collections import deque


def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)

    if (sum1 + sum2) % 2:
        return -1

    queue1, queue2 = deque(queue1), deque(queue2)
    cnt = 0

    while True:
        if cnt == 4 * len(queue1):
            return -1
        if sum1 > sum2:
            target_elem = queue1.popleft()
            queue2.append(target_elem)
            sum1 -= target_elem
            sum2 += target_elem
        elif sum1 < sum2:
            target_elem = queue2.popleft()
            queue1.append(target_elem)
            sum1 += target_elem
            sum2 -= target_elem
        else:
            return cnt
        cnt += 1
