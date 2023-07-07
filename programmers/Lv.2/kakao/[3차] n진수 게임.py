def convert_notation(num, base):
    notation_dict = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B',
        12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    num, remainder = divmod(num, base)

    return convert_notation(num, base) + notation_dict[remainder] if num else notation_dict[remainder]


def solution(n, t, m, p):
    full_answer = ''
    index = 0
    max_index = m * (t - 1) + p - 1

    while index <= max_index:
        for num in range(max_index):
            transformed_num = convert_notation(num, n)
            full_answer += transformed_num
            index += len(transformed_num)

    return "".join([full_answer[time * m + p - 1] for time in range(t)])
