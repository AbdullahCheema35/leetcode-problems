from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max: int = 0
        buy: int = 0
        arrLen: int = len(prices)
        for i in range(1, arrLen):
            if prices[i] - prices[buy] > max:
                max = prices[i] - prices[buy]
            if prices[i] < prices[buy]:
                buy = i
        return max
