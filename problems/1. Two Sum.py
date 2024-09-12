from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff: int = target - num
            j: int | None = d.get(diff)
            if j is None:
                d[num] = i
            else:
                return [i, j]
        return [0, 1]
