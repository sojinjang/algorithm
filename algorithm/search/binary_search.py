def iterative_bs(input_arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if input_arr[mid] == target:
            return mid
        elif input_arr[mid] < target:
            low = mid + 1
        elif input_arr[mid] > target:
            high = mid - 1

    return -1


def recursive_bs(input_arr, target, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if input_arr[mid] == target:
            return mid
        elif input_arr[mid] > target:
            return recursive_bs(input_arr, target, low, mid - 1)
        elif input_arr[mid] < target:
            return recursive_bs(input_arr, target, mid + 1, high)
    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

target_idx = recursive_bs(array, x, 0, len(array)-1)

if target_idx != -1:
    print("Element is present at index " + str(target_idx))
else:
    print("Not found")