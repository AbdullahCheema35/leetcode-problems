from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result: int = 0
        for num in nums:
            result ^= num
        return result
