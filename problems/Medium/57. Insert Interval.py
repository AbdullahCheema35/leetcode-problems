from typing import Final, List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged: List[List[int]] = []
        N: Final[int] = len(intervals)
        i: int = 0

        if N == 0:
            merged = [newInterval]
            return merged
        if newInterval[1] < intervals[0][0]:
            merged = [newInterval]
            merged.extend(intervals)
            return merged
        if newInterval[0] > intervals[-1][1]:
            merged = intervals
            merged.append(newInterval)
            return merged
        while i < N:
            if newInterval[0] > intervals[i][1]:
                merged.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                merged.append(newInterval)
                merged.extend(intervals[i:])
                return merged
            else:
                start: int = min(newInterval[0], intervals[i][0])
                j: int = i + 1
                while j < N and not (intervals[j][0] > newInterval[1]):
                    j += 1
                end: int = max(newInterval[1], intervals[j - 1][1])
                merged.append([start, end])
                merged.extend(intervals[j:])
                return merged

            i += 1
        return merged
