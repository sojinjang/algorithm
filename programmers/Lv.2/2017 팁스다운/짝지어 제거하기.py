def solution(some_string):
    if len(some_string) % 2:
        return 0
    temp = []

    for s in some_string:
        if not temp:
            temp.append(s)
        else:
            if temp[-1] == s:
                temp.pop()
            else:
                temp.append(s)

    return 0 if temp else 1
