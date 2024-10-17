from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n: int = len(nums)
        total_sum: int = n * (n + 1) // 2

        arr_sum: int = 0

        for num in nums:
            arr_sum += num

        return total_sum - arr_sum
