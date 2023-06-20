#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from itertools import combinations
from functools import reduce


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    freq_dict = defaultdict(int)

    for start_idx in range(len(s)):
        for end_idx in range(start_idx + 1, len(s) + 1):
            target = "".join(sorted(s[start_idx:end_idx]))
            freq_dict[target] += 1

    anagram_cnt = list(filter(lambda x: x >= 2, freq_dict.values()))
    return reduce(lambda acc, cur: acc + len(list(combinations(range(1, cur + 1), 2))), anagram_cnt, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
