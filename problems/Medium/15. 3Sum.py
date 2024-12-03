from typing import Dict, List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[List[int]] = []

        d: dict = {}

        distinct: dict = {}

        TARGET: int = 0

        for i, i_num in enumerate(nums):
            d.clear()
            for j, j_num in enumerate(nums[i + 1 :], i + 1):
                required: int = TARGET - (i_num + j_num)
                if d.get(required) is not None:
                    if (
                        (not distinct.get(i_num))
                        or (not distinct.get(j_num))
                        or (not distinct.get(required))
                    ):
                        distinct[i_num] = 1
                        distinct[j_num] = 1
                        distinct[required] = 1
                        triplets.append([i_num, j_num, required])
                d[j_num] = j

        return triplets
