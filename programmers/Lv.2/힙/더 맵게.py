import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) > 1:
        count += 1
        small_1 = heapq.heappop(scoville)
        small_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, small_1 + small_2 * 2)
        if scoville[0] > K:
            return count

    return -1
