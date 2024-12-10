from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n: int = len(mat)  # rows
        m: int = len(mat[0])  # cols

        MAX_DIST = m * n + 1

        dp: List[List[int]] = [[MAX_DIST] * m for _ in range(n)]

        # top-left to bottom-right pass
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

        # bottom-right to top-left pass
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if dp[i][j] != 0:
                    if j < m - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
                    if i < n - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)

        return dp
