from itertools import permutations


def solution(k, dungeons):
    answer = []
    order_list = list(permutations(dungeons, len(dungeons)))

    for order in order_list:
        fatigue = k
        cnt = 0
        for cur_dungeon in order:
            min_required_fatigue, required_fatigue = cur_dungeon
            if fatigue < min_required_fatigue:
                continue
            fatigue -= required_fatigue
            cnt += 1
        answer.append(cnt)

    return max(answer)
