import itertools
from functools import reduce


def get_intersection_points(line1, line2):
    [A, B, E], [C, D, F] = line1, line2
    denominator = A * D - B * C
    if denominator == 0: return None
    x = (B * F - E * D) / denominator
    y = (E * C - A * F) / denominator
    if float(x).is_integer() and float(y).is_integer():
        return int(x), int(y)


def solution(line):
    line_combinations = list(itertools.combinations(line, 2))
    star_points = []

    for line1, line2 in line_combinations:
        intersection_point = get_intersection_points(line1, line2)
        if intersection_point:
            star_points.append(intersection_point)

    star_points = list(set(star_points))
    if len(star_points) == 1: return ["*"]

    x_sorted_points = sorted(star_points)
    y_sorted_points = sorted(star_points, key=lambda coord: coord[1])
    min_x, max_x = x_sorted_points[0][0], x_sorted_points[-1][0]
    min_y, max_y = y_sorted_points[0][1], y_sorted_points[-1][1]

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [["." for _ in range(width)] for _ in range(height)]

    for row in range(min_x, max_x + 1):
        for col in range(min_y, max_y + 1):
            if (row, col) in star_points:
                grid[max_y - col][abs(min_x - row)] = "*"

    return [reduce(lambda acc, cur: acc + cur, line, "") for line in grid]
