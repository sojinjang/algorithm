def solution(year):
    additional_cnt = 1 if bool(year % 100) else 0
    return year//100 + additional_cnt
