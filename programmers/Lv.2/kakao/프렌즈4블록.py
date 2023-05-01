def search_2x2_blocks(m, n, board, empty_block_sign):
    match_block_set = set()
    for i in range(m - 1):
        for j in range(n - 1):
            char = board[i][j]
            if char == empty_block_sign:
                continue
            if board[i + 1][j] == char and board[i][j + 1] == char and board[i + 1][j + 1] == char:
                match_block_set.add((i, j))
                match_block_set.add((i + 1, j))
                match_block_set.add((i, j + 1))
                match_block_set.add((i + 1, j + 1))
    return match_block_set


def remove_blocks(board, match_block_set, empty_block_sign):
    for (i, j) in match_block_set:
        board[i][j] = empty_block_sign
    return board


def pull_down_blocks(m, n, board, empty_block_sign):
    while True:
        is_movable = False
        for i in range(m - 1):
            for j in range(n):
                if board[i][j] and board[i + 1][j] == empty_block_sign:
                    board[i + 1][j] = board[i][j]
                    board[i][j] = empty_block_sign
                    is_movable = True
        if not is_movable: return board


def solution(m, n, board):
    answer = 0
    EMPTY_BLOCK_SIGN = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:
        match_block_set = search_2x2_blocks(m, n, board, EMPTY_BLOCK_SIGN)

        if not bool(match_block_set): return answer

        answer += len(match_block_set)
        board = remove_blocks(board, match_block_set, EMPTY_BLOCK_SIGN)
        board = pull_down_blocks(m, n, board, EMPTY_BLOCK_SIGN)

    return answer

