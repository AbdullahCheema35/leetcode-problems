from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d: dict[int, int] = {}
        for num in nums:
            freq: int | None = d.get(num)
            if freq:
                d[num] = freq + 1
            else:
                d[num] = 1

        for k, v in d.items():
            if v == 1:
                return k

        return -1
