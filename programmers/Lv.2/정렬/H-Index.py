def solution(citations):
    num_papers = len(citations)
    h_list = []
    citations.sort()

    for idx, citation in enumerate(citations):
        h_list.append(min(num_papers - idx, citation))

    return max(h_list)
