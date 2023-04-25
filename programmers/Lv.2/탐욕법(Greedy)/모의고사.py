def solution(answers):
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    ans1 = st1 * (len(answers) // len(st1)) + st1[:len(answers) % len(st1)]
    ans2 = st2 * (len(answers) // len(st2)) + st2[:len(answers) % len(st2)]
    ans3 = st3 * (len(answers) // len(st3)) + st3[:len(answers) % len(st3)]

    count_1, count_2, count_3 = 0, 0, 0
    for i, ans in enumerate(answers):
        if ans == ans1[i]:
            count_1 += 1
        if ans == ans2[i]:
            count_2 += 1
        if ans == ans3[i]:
            count_3 += 1
    correct = [count_1, count_2, count_3]

    return [i + 1 for i in range(3) if correct[i] == max(correct)]
