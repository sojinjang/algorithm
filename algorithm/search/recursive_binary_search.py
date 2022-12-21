def recursive_bs(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return recursive_bs(array, x, low, mid - 1)
        elif array[mid] < x:
            return recursive_bs(array, x, mid + 1, high)
    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

target_idx = recursive_bs(array, x, 0, len(array)-1)

if target_idx != -1:
    print("Element is present at index " + str(target_idx))
else:
    print("Not found")