from typing import List, Final


class Solution:
    def countBits(self, n: int) -> List[int]:
        LSB: Final[int] = 1
        ANS: Final[List[int]] = [0] * (n + 1)
        ANS[1] = 1
        current_MSB: int = 1

        for i in range(2, n + 1):
            if LSB & i:
                ANS[i] = ANS[i - 1] + 1
            elif not i & i - 1:
                ANS[i] = 1
                current_MSB <<= 1
            else:
                ANS[i] = ANS[(current_MSB - 1) & i] + 1

        return ANS
