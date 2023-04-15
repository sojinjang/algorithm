def solution(want, number, discount):
    want_dict = {want[i]: number[i] for i in range(len(want))}
    total_num, num_discount_day = sum(number), len(discount)
    answer = 0

    for register_day in range(num_discount_day):
        if len(discount) - register_day < total_num: return answer
        want_dict_copy = want_dict.copy()
        for idx in range(register_day, min(register_day + 10, num_discount_day)):
            if discount[idx] in want_dict.keys() and want_dict_copy[discount[idx]] > 0:
                want_dict_copy[discount[idx]] -= 1
        if sum(want_dict_copy.values()) == 0:
            answer += 1
