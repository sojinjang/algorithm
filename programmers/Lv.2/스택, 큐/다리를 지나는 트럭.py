def solution(bridge_length, weight, truck_weights):

    time = 0
    crossing_trucks = [0 for _ in range(bridge_length)]

    while crossing_trucks:
        time += 1
        crossing_trucks.pop(0)
        if truck_weights:
            if sum(crossing_trucks) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                crossing_trucks.append(truck)
            else:
                crossing_trucks.append(0)

    return time
