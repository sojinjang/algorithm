from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, start_idx = 0, 0
        used = defaultdict(int)

        for end_idx, char in enumerate(s):
            if char in used and start_idx <= used[char]:
                start_idx = used[char] + 1
            else:
                max_len = max(max_len, end_idx - start_idx + 1)

            used[char] = end_idx

        return max_len
