from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursive(nums: List[int], profits: List[int], i: int) -> int:
            if i < 0:
                return 0
            
            if profits[i] != -1:
                return profits[i]
            
            profits[i] = max(nums[i] + recursive(nums, profits, i-2), recursive(nums, profits, i-1))
            return profits[i]
        
        N: int = len(nums)
        profits: List[int] = [-1] * N
        
        recursive(nums, profits, N-1)
        return profits[N-1]
        