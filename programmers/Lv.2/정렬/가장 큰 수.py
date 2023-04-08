def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_list = alist[:mid]
        right_list = alist[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            left = int(str(left_list[i]) + str(right_list[j]))
            right = int(str(right_list[j]) + str(left_list[i]))

            if left < right:
                alist[k] = left_list[i]
                i += 1
            else:
                alist[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            alist[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            alist[k] = right_list[j]
            j += 1
            k += 1

    return alist


def solution(numbers):
    answer_list = merge_sort(sorted(numbers))
    answer_list.reverse()
    answer = ""
    for i in answer_list:
        answer += str(i)
    if answer[0] == "0":
        answer = "0"

    return answer
