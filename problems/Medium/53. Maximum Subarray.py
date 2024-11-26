from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum: int = 0
        max_sum: int = nums[0]
        for elem in nums:
            curr_sum = max(elem, curr_sum + elem)
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
