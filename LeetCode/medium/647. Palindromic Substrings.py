class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        memo = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 1 or (length == 2 and s[start] == s[end]):
                    memo[start][end] = True
                    cnt += 1
                elif memo[start + 1][end - 1] and s[start] == s[end]:
                    memo[start][end] = True
                    cnt += 1

        return cnt
