from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # Create a list of size n + 1 to store the number of ways to reach the ith step
        dp: List[int] = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        # Bottom-Up Approach
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return result stored in last element
        return dp[n]
