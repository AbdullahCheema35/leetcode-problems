from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start: int = 0
        end: int = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        return -1
