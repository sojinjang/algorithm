import heapq


def solution(maps):
    ROW, COL = len(maps), len(maps[0])
    maps = [[float("inf") if maps[r][c] == 1 else 0 for c in range(COL)] for r in range(ROW)]
    maps[0][0] = 1
    trace = []
    heapq.heappush(trace, (1, 0, 0))  # (이동 횟수, 행, 열)
    locate_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (up, right, down, left)

    while trace:
        (cur_cnt, cur_row, cur_col) = heapq.heappop(trace)
        for (dx, dy) in locate_list:
            new_row, new_col = cur_row + dx, cur_col + dy
            if new_row in range(ROW) and new_col in range(COL) and maps[new_row][new_col] != 0:
                if cur_cnt + 1 < maps[new_row][new_col]:
                    maps[new_row][new_col] = cur_cnt + 1
                    heapq.heappush(trace, (maps[new_row][new_col], new_row, new_col))

    return -1 if maps[ROW - 1][COL - 1] == float("inf") else maps[ROW - 1][COL - 1]
