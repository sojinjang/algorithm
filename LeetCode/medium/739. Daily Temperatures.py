from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for idx, cur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur:
                last_idx = stack.pop()
                answer[last_idx] = idx - last_idx
            stack.append(idx)

        return answer
