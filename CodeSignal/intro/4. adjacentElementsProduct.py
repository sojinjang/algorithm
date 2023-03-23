def solution(inputArray):
    max_value = None
    for i in range(len(inputArray) - 1):
        cur_product = inputArray[i] * inputArray[i + 1]
        if not max_value or max_value < cur_product:
            max_value = cur_product

    return max_value
