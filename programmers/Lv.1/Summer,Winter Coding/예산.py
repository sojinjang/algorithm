def solution(d, budget):
    expense = 0
    answer = 0
    for i in sorted(d):
        expense += i
        if expense > budget:
            break
        answer += 1

    return answer
