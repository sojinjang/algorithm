from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        chain_len_dict = defaultdict(int)

        for word in words:
            chain_len_dict[word] = 1
            for excluded_idx in range(len(word)):
                prev_word = word[:excluded_idx] + word[excluded_idx + 1:]
                if prev_word in words:
                    chain_len_dict[word] = max(chain_len_dict[word], chain_len_dict[prev_word] + 1)

        return max(chain_len_dict.values())
