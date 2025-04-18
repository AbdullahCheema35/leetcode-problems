from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums: List[int], perms: List[List[int]], beginIndex: int) -> None:
            if beginIndex == len(nums) - 1:
                perms.append([num for num in nums])
                return
            
            for i in range(beginIndex, len(nums)):
                nums[i], nums[beginIndex] = nums[beginIndex], nums[i]
                recursive(nums, perms, beginIndex=beginIndex+1)
                nums[i], nums[beginIndex] = nums[beginIndex], nums[i]

        perms: List[List[int]] = []
        recursive(nums, perms, beginIndex=0)
        return perms