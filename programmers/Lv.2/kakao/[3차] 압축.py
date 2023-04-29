def solution(msg):
    lzw_dict = {}
    answer = []
    start_idx, end_idx = 0, 1
    last_idx = ord("Z") - ord("A") + 1 + 1

    for char_idx in range(ord("A"), ord("Z") + 1):
        lzw_dict[chr(char_idx)] = char_idx - ord("A") + 1

    while end_idx < len(msg) + 1:
        cur_input = msg[start_idx: end_idx]
        if cur_input in lzw_dict:
            end_idx += 1
        else:
            answer.append(lzw_dict[cur_input[:-1]])
            lzw_dict[cur_input] = last_idx
            last_idx += 1
            start_idx = end_idx - 1

    answer.append(lzw_dict[cur_input])

    return answer

