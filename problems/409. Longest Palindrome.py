from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        odd = 0
        for v in counter.values():
            res += v // 2
            if not odd and v % 2:
                odd = 1
        return res * 2 + odd
