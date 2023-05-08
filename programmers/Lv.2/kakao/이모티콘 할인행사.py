import math
from itertools import product


def get_multiple_of_ten(num):
    return math.ceil(num * 0.1) * 10


def solution(users, emoticons):
    answer = [0, 0]

    users.sort(key=lambda x: x[0])
    min_ratio = get_multiple_of_ten(users[0][0])
    max_ratio = get_multiple_of_ten(users[-1][0])
    ratio_range = list(range(min_ratio, max_ratio + 1, 10))
    discount_permutations = list(product(ratio_range, repeat=len(emoticons)))

    for disc in discount_permutations:
        subscriber = 0
        total_sales = 0
        for user_ratio, user_price in users:
            sales = 0
            for ratio_idx in range(len(disc)):
                if user_ratio <= disc[ratio_idx]:
                    sales += emoticons[ratio_idx] * (100 - disc[ratio_idx]) / 100
                if sales >= user_price:
                    break
            if sales >= user_price:
                sales = 0
                subscriber += 1
            total_sales += sales
            if subscriber >= answer[0]:
                max_sales = max(answer[1], total_sales) if subscriber == answer[0] else total_sales
                answer = [subscriber, max_sales]

    return answer
