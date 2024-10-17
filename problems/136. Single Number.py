from typing import Counter, List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter: Counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k

        return 0
