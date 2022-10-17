def solution(participant, completion):
    remainder = set(participant) - set(completion)
    if bool(remainder):
        answer = list(remainder)[0]
    else:
        cpt_cnt = {}
        pcp_cnt = {}

        for value in participant:
            try:
                pcp_cnt[value] += 1
            except:
                pcp_cnt[value] = 1

        for value in completion:
            try:
                cpt_cnt[value] += 1
            except:
                cpt_cnt[value] = 1

        cpt_values = list(cpt_cnt.values())

        if cpt_values.count(1) == len(cpt_values):
            for i in pcp_cnt.items():
                if i[1] > 1:
                    answer = i[0]
                else:
                    pass
        else:
            for a, b in zip(sorted(pcp_cnt.items()), sorted(cpt_cnt.items())):
                if a == b:
                    pass
                else:
                    answer = a[0]

    return answer
