def solution(land):
    for row_idx in range(1, len(land)):
        for col_idx in range(4):
            land[row_idx][col_idx] += max(land[row_idx-1][:col_idx] + land[row_idx-1][col_idx+1:])

    return max(land[len(land) - 1])
