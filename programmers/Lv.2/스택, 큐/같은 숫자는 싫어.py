def solution(arr):
    answer = []

    for elem in arr:
        if not answer or elem != answer[-1]:
            answer.append(elem)

    return answer
