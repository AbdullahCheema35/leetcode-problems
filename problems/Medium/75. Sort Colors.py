from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for color in range(3):
            for j in range(i+1, len(nums)):
                if nums[j] == color:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]

if __name__ == "__main__":
    nums: List[int] = [8,7,6,5,4,3,2,1,0]
    Solution().sortColors(nums)
    print(nums)
