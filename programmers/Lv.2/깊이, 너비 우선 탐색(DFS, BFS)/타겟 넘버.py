def solution(numbers, target):
    n = len(numbers)
    answer = 0
    queue = [[numbers[0], 0], [-1 * numbers[0], 0]]

    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx == n:
            if temp == target:
                answer += 1
        else:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])

    return answer
