from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start: int = 0
        end: int = len(nums) - 1
        result: List[int] = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[start]) > abs(nums[end]):
                result[i] = nums[start] ** 2
                start += 1
            else:
                result[i] = nums[end] ** 2
                end -= 1
        return result
