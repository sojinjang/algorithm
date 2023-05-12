import re
from itertools import permutations
from functools import reduce


def calculate_expression(split_expression, priority):
    for target_sign in priority:
        temp = []
        idx = 0
        while idx < len(split_expression):
            char = split_expression[idx]
            if char == target_sign:
                num1 = int(temp.pop())
                num2 = int(split_expression[idx + 1])
                if target_sign == "+":
                    temp.append(num1 + num2)
                elif target_sign == "-":
                    temp.append(num1 - num2)
                elif target_sign == "*":
                    temp.append(num1 * num2)
                idx += 2
            else:
                temp.append(char)
                idx += 1
        split_expression = temp
    return abs(split_expression[0])


def solution(expression):
    sign = ["+", "-", "*"]
    signs_found = reduce(lambda acc, cur: acc + [cur] if re.search(re.escape(cur), expression) else acc, sign, [])
    priorities = list(permutations(signs_found))

    regex = "([{}])".format("".join("\\" + s for s in sign))
    split_expression = re.split(regex, expression)
    split_expression = [x for x in split_expression if x != ""]

    max_prize = 0
    for priority in priorities:
        prize = calculate_expression(split_expression, priority)
        max_prize = max(max_prize, prize)

    return max_prize
