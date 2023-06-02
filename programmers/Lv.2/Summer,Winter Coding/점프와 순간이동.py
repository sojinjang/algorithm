def solution(n):
    ans = 0
    while n:
        if n % 2 > 0:
            ans += 1
            n -= 1
            continue
        n //= 2

    return ans
