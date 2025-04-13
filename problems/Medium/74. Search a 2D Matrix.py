from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        start: int = 0
        end: int = rows - 1

        while start<end:
            mid: int = (start + end) // 2
            if target <= matrix[mid][cols-1]:
                end = mid
            else:
                start = mid + 1
        
        assert start == end
        
        row_idx = start
        start, end = 0, cols - 1
        while start < end:
            mid: int = (start + end) // 2
            if target < matrix[row_idx][mid]:
                end = mid - 1
            elif target > matrix[row_idx][mid]:
                start = mid + 1
            else:
                return True
        return matrix[row_idx][start] == target