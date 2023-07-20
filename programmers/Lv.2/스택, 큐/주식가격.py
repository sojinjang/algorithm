from collections import deque


def solution(prices):
    price = deque(prices)
    answer = []
    while price:
        p = price.popleft()
        if len(price) == 0:
            answer.append(0)
            return answer
        for i, item in enumerate(price):
            if p > item:
                answer.append(i + 1)
                break
        if len(answer) != len(prices) - len(price):
            answer.append(len(price))

    return answer
