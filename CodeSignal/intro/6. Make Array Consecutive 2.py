def get_num_required_statues(cnt, max_num, left_statues):
    if not left_statues: return cnt
    next_num = left_statues.pop()
    cnt += max_num - next_num - 1
    return get_num_required_statues(cnt, next_num, left_statues)


def solution(statues):
    statues.sort()
    max_num = statues.pop()
    answer = get_num_required_statues(0, max_num, statues)

    return answer
