from typing import Final, List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N: Final[int] = len(nums)
        product: List[int] = [1] * N
        suffix_prod: int = 1

        for i in range(N):
            # Prefix Sum (excluding current element)
            if i > 0:
                product[i] = product[i - 1] * nums[i - 1]

        for i in reversed(range(N)):
            # Postfix Sum
            if i + 1 < N:
                product[i] *= suffix_prod
            suffix_prod *= nums[i]

        return product
