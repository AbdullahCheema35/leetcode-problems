class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i: int = 0
        j: int = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
