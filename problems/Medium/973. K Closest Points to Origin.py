import heapq
from math import sqrt
from typing import List, Tuple


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ORIGIN: Tuple[int, int] = (0, 0)
        distances: dict[Tuple[float, int], int] = {}

        def calculate_distance(point_a: List[int], point_b: Tuple[int, int]) -> float:
            return sqrt(
                ((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2)
            )

        for i, point in enumerate(points):
            distances[(calculate_distance(point, ORIGIN), i)] = 1

        distances_list = list(distances.keys())

        heapq.heapify(distances_list)

        closest_k: List[List[int]] = [[]] * k
        for i in range(k):
            point_index: int = heapq.heappop(distances_list)[1]
            closest_k[i] = points[point_index]

        return closest_k
