import collections


def solution(id_list, report, k):
    report_dict = collections.defaultdict(list)

    for i in report:
        key, value = i.split(' ')
        report_dict[value].append(key)

    mail_list = []
    for key, val in report_dict.items():
        mail_id = list(set(val))
        if len(mail_id) >= k:
            mail_list.append(mail_id)

    answer = []
    for i in id_list:
        cnt = 0
        for m in mail_list:
            if i in m:
                cnt += 1
        answer.append(cnt)

    return answer
