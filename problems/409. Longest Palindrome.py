class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        res = 0
        odd = 0
        for v in d.values():
            res += v // 2
            if not odd and v % 2:
                odd = 1
        return res * 2 + odd
