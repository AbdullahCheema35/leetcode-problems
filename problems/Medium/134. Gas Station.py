from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N: int = len(gas)
        curr: int = 0
        total: int = 0

        start_index: int = 0

        for i in range(N):
            diff: int = gas[i] - cost[i]
            curr += diff
            total += diff

            if curr < 0:
                start_index = i + 1
                curr = 0

        return start_index if (total >= 0) else -1 