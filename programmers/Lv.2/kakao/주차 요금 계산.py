from collections import defaultdict
from math import ceil


def convert_to_minute(hour_and_minute):
    [hour, minute] = hour_and_minute
    return int(hour) * 60 + int(minute)


def calc_time_diff(in_time, out_time):
    return int(convert_to_minute(out_time.split(":"))) - int(convert_to_minute(in_time.split(":")))


def solution(fees, records):
    [standard_time, standard_fee, unit_time, unit_fee] = fees
    in_records = {}
    acc_parking_time_dict = defaultdict(int)
    answer = []

    for record in records:
        [time, car_number, in_or_out] = record.split(" ")
        if in_or_out == "IN":
            in_records[car_number] = time
        else:
            time_diff = calc_time_diff(in_records[car_number], time)
            del in_records[car_number]
            acc_parking_time_dict[car_number] += time_diff
    for car_number, time in in_records.items():
        time_diff = calc_time_diff(time, "23:59")
        acc_parking_time_dict[car_number] += time_diff
    for _, acc_time in sorted(acc_parking_time_dict.items()):
        if int(acc_time) <= standard_time:
            answer.append(standard_fee)
        else:
            acc_fee = standard_fee + ceil((int(acc_time) - standard_time) / unit_time) * unit_fee
            answer.append(acc_fee)

    return answer
