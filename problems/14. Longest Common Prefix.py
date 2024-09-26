from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp: str = ""
        for s in zip(*strs):
            if len(set(s)) == 1:
                lcp += s[0]
            else:
                break
        return lcp
