import collections


def solution(clothes):
    c_dict = collections.defaultdict(int)

    for c in clothes:
        c_dict[c[1]] += 1

    count = 0
    for _, num in c_dict.items():
        if count == 0:
            count += (num + 1)
        else:
            count *= (num + 1)

    return count - 1
