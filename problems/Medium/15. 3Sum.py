from typing import Final, List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[List[int]] = []

        TARGET: Final[int] = 0

        distinct_tuples: Set[tuple] = set()

        array_elems: Set[int] = set()

        for i, i_num in enumerate(nums):
            array_elems.clear()
            for _, j_num in enumerate(nums[i + 1 :], i + 1):
                req_elem: int = TARGET - (i_num + j_num)
                if req_elem in array_elems:
                    sorted_triplet: List[int] = sorted([i_num, j_num, req_elem])
                    sorted_tuple: Tuple = tuple(sorted_triplet)
                    if sorted_tuple not in distinct_tuples:
                        triplets.append(sorted_triplet)
                        distinct_tuples.add(sorted_tuple)
                array_elems.add(j_num)

        return triplets
