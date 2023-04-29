def solution(record):
    answer = []
    nickname_dict = {}

    ENTER_KEY = "Enter"
    LEAVE_KEY = "Leave"
    CHANGE_KEY = "Change"

    for desc in record:
        if CHANGE_KEY in desc or ENTER_KEY in desc:
            _, uid, nickname = desc.split(" ")
            nickname_dict[uid] = nickname

    for desc in record:
        if ENTER_KEY in desc:
            _, uid, nickname = desc.split(" ")
            answer.append(nickname_dict[uid] + "님이 들어왔습니다.")
        if LEAVE_KEY in desc:
            _, uid = desc.split(" ")
            answer.append(nickname_dict[uid] + "님이 나갔습니다.")

    return answer
