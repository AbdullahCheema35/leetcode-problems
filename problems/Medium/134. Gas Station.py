from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N: int = len(gas)
        diff: List[int] = [0] * N

        total_sum: int = 0

        for i in range(N):
            diff[i] = gas[i] - cost[i]
            total_sum += diff[i]
        
        if total_sum < 0:
            return -1
        
        starting_index: int = 0
        i: int = 0
        
        while i < N:
            while diff[i] < 0:
                i += 1
            
            curr_sum: int = 0
            starting_index = i

            while curr_sum >= 0 and i < N:
                curr_sum += diff[i]
                i += 1
            
        return starting_index