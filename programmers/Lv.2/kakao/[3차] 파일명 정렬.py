import re

def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    sorted_files = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sorted_files]
