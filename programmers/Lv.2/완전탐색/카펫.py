def solution(brown, yellow):
    area = brown + yellow
    temp = []
    for i in range(3, area//2):
        if area % i == 0:
            temp.append(i)

    answer = []
    for i in temp:
        if 2*i + 2*(area//i) - 4 == brown:
            answer.append(i)
            if 2*i == 2*(area//i):
                answer.append(i)

    return sorted(answer, reverse=True)
