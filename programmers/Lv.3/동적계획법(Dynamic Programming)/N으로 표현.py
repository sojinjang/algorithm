def solution(N, number):
    possible_set = [0, [N]]

    if N == number: return 1

    for i in range(2, 9):
        temp_set = [int(str(N) * i)]
        for i_half in range(1, i // 2 + 1):
            for x in possible_set[i_half]:
                for y in possible_set[i - i_half]:
                    temp_set.append(x + y)
                    temp_set.append(x - y)
                    temp_set.append(y - x)
                    temp_set.append(x * y)
                    if y != 0:
                        temp_set.append(x / y)
                    if x != 0:
                        temp_set.append(y / x)
            if number in temp_set:
                return i
            possible_set.append(temp_set)

    return -1
