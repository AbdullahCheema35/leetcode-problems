from typing import Final


class Solution:
    def hammingWeight(self, n: int) -> int:
        LSB: Final[int] = 1
        set_bits: int = 0
        while n:
            if LSB & n:
                set_bits += 1
            n >>= 1
        return set_bits
