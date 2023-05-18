#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    result = 0
    last_tower, cur_city, next_city = 0, 0, 0
    num_cities = len(arr)

    while cur_city < num_cities:
        result += 1
        next_city = min(cur_city + k - 1, num_cities)

        while last_tower <= next_city < num_cities and arr[next_city] == 0:
            next_city -= 1

        if next_city < last_tower:
            return -1

        last_tower = next_city + 1
        next_city += k
        cur_city = next_city

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
