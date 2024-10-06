from typing import Final


class Solution:
    def reverseBits(self, n: int) -> int:
        LSB: Final[int] = 1
        TOTAL_BITS: Final[int] = 32
        result: int = 0

        for i in range(TOTAL_BITS):
            curr_bit: int = LSB & n
            n = n >> 1
            if curr_bit:
                result |= LSB << (TOTAL_BITS - i - 1)
        return result
