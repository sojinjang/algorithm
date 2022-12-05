def solution(gems):
    n = len(gems)
    m = len(set(gems))
    answer = [1, n]
    dic = {gems[0]: 1}
    l, r = 0, 0
    while l < n:
        if len(dic) != m:
            r += 1
            if r >= n:
                break
            if gems[r] in dic:
                dic[gems[r]] += 1
            else:
                dic[gems[r]] = 1
        else:
            if r - l < answer[1] - answer[0]:
                answer = [l + 1, r + 1]
            if dic[gems[l]] != 1:
                dic[gems[l]] -= 1
            else:
                del dic[gems[l]]
            l += 1

    return answer
