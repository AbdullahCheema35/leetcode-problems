# from collections import defaultdict


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         d = defaultdict(lambda: 0)
#         for letter in magazine:
#             d[letter] += 1

#         for letter in ransomNote:
#             if d[letter] < 1:
#                 return False
#             d[letter] -= 1

#         return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in set(ransomNote):
            if magazine.count(letter) < ransomNote.count(letter):
                return False

        return True
