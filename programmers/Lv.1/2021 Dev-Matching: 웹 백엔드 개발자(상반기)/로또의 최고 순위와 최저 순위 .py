def solution(lottos, win_nums):
    match_nums = 6 - len(set(win_nums) - set(lottos))
    unknown_nums = lottos.count(0)
    max = match_nums + unknown_nums
    min = match_nums

    trans = [6, 6, 5, 4, 3, 2, 1]

    return trans[max], trans[min]
