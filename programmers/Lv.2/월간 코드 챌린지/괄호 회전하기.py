def solution(s):
    bracket_dict = {"(": ")", "[": "]", "{": "}"}
    open_brackets = bracket_dict.keys()
    cnt = len(s)

    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        temp = []
        for item in rotated_s:
            if item in open_brackets:
                temp.append(item)
            else:
                if temp and bracket_dict[temp[-1]] == item:
                    temp.pop()
                elif not temp:
                    cnt -= 1
                    break
        if temp:
            cnt -= 1

    return cnt
