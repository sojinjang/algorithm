import heapq as hq


def solution(operations):
    INSERT_SIGN = "I"
    MIN_SIGN = "-1"
    temp = []

    for op in operations:
        if op[0] == INSERT_SIGN:
            hq.heappush(temp, int(op[1:]))
        else:
            if str(int(op[1:])) == MIN_SIGN:
                try:
                    hq.heappop(temp)
                except:
                    pass
            else:
                try:
                    temp.pop(-1)
                except:
                    pass

    return [max(temp), min(temp)] if len(temp) else [0, 0]
