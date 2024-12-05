from typing import Final, List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[List[int]] = []

        TARGET: Final[int] = 0

        # sort the array
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum: int = nums[i] + nums[j] + nums[k]
                if curr_sum > TARGET:
                    k -= 1
                elif curr_sum < TARGET:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return triplets
