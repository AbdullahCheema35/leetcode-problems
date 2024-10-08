from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left: int = 0
        for right, _ in enumerate(nums):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
