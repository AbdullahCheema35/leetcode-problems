from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums: List[int], start: int, end: int) -> int:
            pivot: int = nums[end]
            i: int = start - 1

            for j in range(start, end):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            
            i += 1
            nums[i], nums[end] = nums[end], nums[i]
            
            return i
        
        def quickSort(nums: List[int], start: int, end: int) -> None:
            if end <= start:
                return

            pivot_index: int = partition(nums, start, end)

            quickSort(nums, start, pivot_index-1)
            quickSort(nums, pivot_index+1, end)

        quickSort(nums, 0, len(nums)-1)


if __name__ == "__main__":
    nums: List[int] = [8,7,6,5,4,3,2,1,0]
    Solution().sortColors(nums)
    print(nums)
