def solution(price, money, count):
    total_price = 0
    for cnt in range(1, count + 1):
        total_price += price * cnt
    left_money = money - total_price

    return left_money * -1 if left_money < 0 else 0
