from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        above_row: List[int] = [1] * n

        for _ in range(m - 1):
            curr_row: List[int] = [1] * n
            for i in range(1, n):
                curr_row[i] = curr_row[i - 1] + above_row[i]
            above_row = curr_row

        return above_row[-1]
