from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n: int = len(mat)  # rows
        m: int = len(mat[0])  # cols

        MAX_INT = m * n + 1

        dp: List[List[int]] = [[-1] * m for _ in range(n)]

        def calculate(
            mat: List[List[int]], dp: List[List[int]], i: int, j: int, m: int, n: int
        ) -> int:
            if i >= n or j >= m:
                return MAX_INT
            if dp[i][j] != -1:
                return dp[i][j]
            if mat[i][j] == 0:
                dp[i][j] = 0

            off_by_one_dist: int = min(
                calculate(mat, dp, i, j + 1, m, n),
                calculate(mat, dp, i + 1, j, m, n),
                dp[i - 1][j] if i > 0 and dp[i - 1][j] != -1 else MAX_INT,
                dp[i][j - 1] if j > 0 and dp[i][j - 1] != -1 else MAX_INT,
            )

            dp[i][j] = (off_by_one_dist + 1) if mat[i][j] != 0 else 0
            return dp[i][j]

        calculate(mat, dp, 0, 0, m, n)

        return dp


if __name__ == "__main__":
    input_mat = [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
    ]
    # input_mat[1][1] = 1
    sol = Solution()
    sol.updateMatrix(input_mat)
