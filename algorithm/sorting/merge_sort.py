def mergesort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left_list = unsorted_list[:mid]
        right_list = unsorted_list[mid:]

        mergesort(left_list)
        mergesort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[i]:
                unsorted_list[k] = left_list[i]
                i = i + 1
            else:
                unsorted_list[k] = right_list[j]
                j = j + 1
            k = k + 1

        while i < len(left_list):
            unsorted_list[k] = left_list[i]
            i = i + 1
            k = k + 1

        while j < len(right_list):
            unsorted_list[k] = right_list[i]
            j = j + 1
            k = k + 1


num_list = [9, 6, 2, 4, 1, 3, 7, 5, 8]
mergesort(num_list)
print(num_list)
