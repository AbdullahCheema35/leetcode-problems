from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recursion(row: int, col: int, m: int, n: int, dp: List[List[int]]) -> int:
            print(row, col)
            if dp[row][col] != 0:
                return dp[row][col]
            if row == m - 1 or col == n - 1:  # We are in the last row or the last col
                dp[row][col] = 1
            else:
                dp[row][col] = recursion(row + 1, col, m, n, dp) + recursion(
                    row, col + 1, m, n, dp
                )
            return dp[row][col]

        dp: List[List[int]] = [[0] * n for _ in range(m)]
        return recursion(0, 0, m, n, dp)
