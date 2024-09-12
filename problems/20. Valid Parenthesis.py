class Solution:
    def isValid(self, s: str) -> bool:
        mapping: dict[str, str] = {"[": "]", "{": "}", "(": ")"}
        stack: list[str] = []
        for char in s:
            if char in mapping:
                stack.append(char)
            elif len(stack) > 0:
                popped: str = stack.pop(-1)
                if mapping[popped] != char:
                    return False
            else:
                return False
        return len(stack) == 0
