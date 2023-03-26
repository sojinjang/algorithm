def solution(sequence):
    n = len(sequence)
    count = 0
    for i in range(n - 1):
        if sequence[i] >= sequence[i+1]:
            count += 1
            if count > 1:
                return False
            if i > 0 and sequence[i-1] >= sequence[i+1]:
                if i < n - 2 and sequence[i] >= sequence[i+2]:
                    return False
    return True
