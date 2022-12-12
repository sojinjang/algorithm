import math
import collections


def solution(progresses, speeds):
    days_dq = collections.deque(list(map(lambda x, y: math.ceil((100 - x) / y), progresses, speeds)))
    answer = []
    while True:
        try:
            a = days_dq.popleft()
            count = 1
            if len(days_dq):
                while a >= days_dq[0]:
                    days_dq.popleft()
                    count += 1
                    if not len(days_dq):
                        break
            answer.append(count)
        except IndexError:
            return answer
