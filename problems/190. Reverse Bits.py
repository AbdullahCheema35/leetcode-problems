from typing import Final


class Solution:
    def reverseBits(self, n: int) -> int:
        LSB: Final[int] = 1
        TOTAL_BITS: Final[int] = 32
        result: int = 0

        for _ in range(TOTAL_BITS):
            curr_bit: int = LSB & n
            result = (result << 1) | curr_bit
            n >>= 1
        return result
