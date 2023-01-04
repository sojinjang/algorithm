def solution(phone_number):
    hide = '*'
    if len(phone_number[:-4]) > 0:
        for i in range(len(phone_number[:-4]) - 1):
            hide += '*'
        answer = hide + phone_number[-4:]
    else:
        answer = phone_number[-4:]

    return answer