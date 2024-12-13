from typing import Final, List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N: Final[int] = len(nums)
        prefix: List[int] = [1] * N
        postfix: List[int] = [1] * N
        product: List[int] = [1] * N

        for i, num in enumerate(nums):
            # Prefix Sum
            if i > 0:
                prefix[i] = prefix[i - 1] * num
            else:
                prefix[i] = num

        for i in reversed(range(N)):
            # Postfix Sum
            if i + 1 < N:
                postfix[i] = postfix[i + 1] * nums[i]
            else:
                postfix[i] = nums[i]

        # Final answer
        for i in range(N):
            if i > 0:
                product[i] *= prefix[i - 1]
            if i + 1 < N:
                product[i] *= postfix[i + 1]

        return product
