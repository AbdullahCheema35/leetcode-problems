from typing import List, Final


class Solution:
    def countBits(self, n: int) -> List[int]:
        LSB: Final[int] = 1
        ANS: Final[List[int]] = [0] * (n + 1)
        current_MSB: int = 1

        for i in range(1, n + 1):
            if LSB & i:
                ANS[i] = ANS[i - 1] + 1
            elif not i & (i - 1):
                ANS[i] = 1
                current_MSB <<= 1
            else:
                set_bits_except_msb: int = i & (
                    current_MSB - 1
                )  # Get the set bits (number) except the MSB
                ANS[i] = ANS[set_bits_except_msb] + 1

        return ANS
