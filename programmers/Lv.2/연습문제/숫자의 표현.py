def solution(n):
    answer = 0

    for start in range(1, n + 1):
        sum = 0
        for num in range(start, n + 2):
            sum += num
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break

    return answer
