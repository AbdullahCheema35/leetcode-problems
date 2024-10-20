class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse: int = 0
        original: int = x

        while x != 0:
            reverse += x % 10
            x //= 10

        return original == reverse
