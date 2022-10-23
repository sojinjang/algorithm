def solution(citations):
    citations.sort()
    h_list = []
    n = len(citations)
    for i, item in enumerate(citations):
        h_list.append(min(n-i, item))
    return max(h_list)
