def solution(name):
    char_move = 0
    cursor_move = len(name) - 1
    for idx, char in enumerate(name):
        char_move += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == "A":
            next_idx += 1
        cursor_move = min([cursor_move, 2 * idx + len(name) - next_idx, idx + 2 * (len(name) - next_idx)])

    return char_move + cursor_move
