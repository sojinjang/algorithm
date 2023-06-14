def solution(s):
    sorted_numbers = sorted([int(num) for num in s.split(" ")])
    min_num, max_num = sorted_numbers[0], sorted_numbers[-1]

    return str(min_num) + " " + str(max_num)
