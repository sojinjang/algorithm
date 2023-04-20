from collections import defaultdict


def solution(k, tangerine):
    num_tang = 0
    tang_counter = defaultdict(int)

    for tang in tangerine:
        tang_counter[tang] += 1
    sorted_tang_counter = sorted(tang_counter.items(), reverse=True, key=lambda x: x[1])

    for idx, (size, cur_num_tang) in enumerate(sorted_tang_counter):
        num_tang += cur_num_tang
        if num_tang >= k:
            return idx + 1

    return len(sorted_tang_counter)
