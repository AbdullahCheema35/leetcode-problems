from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Array to check if a character has been seen
        seen: List[int] = [
            -1
        ] * 256  # since 's' consists of English letters, digits, symbols and spaces.

        max_length = 0  # stores max length of substring without repeating characters
        start = 0  # stores the starting index of current substring

        for i, char in enumerate(s):
            if (
                seen[ord(char)] >= start
            ):  # this character has already appeared in current substring
                max_length = max(max_length, i - start)
                start = seen[ord(char)] + 1
            seen[ord(char)] = i
        return max(max_length, len(s) - start)
