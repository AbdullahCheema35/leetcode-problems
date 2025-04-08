from typing import Final, Tuple

LIMIT: Final[int] = 2**31

def ignore_whitespace(s: str) -> str:
    return s.lstrip()

def check_signedness(s: str) -> Tuple[int, str]:
    if len(s) == 0:
        return 0, ""
    if s[0] == "-":
        return -1, s[1:]
    if s[0] == "+" or s[0].isdigit():
        return 1, (s[1:] if s[0] == "+" else s)
    return 0, ""

def ignore_leading_zeros(s: str) -> str:
    for i, c in enumerate(s):
        if c != "0":
            if c.isdigit():
                return s[i:]
            break
    return ""

def convert_to_number(s: str) -> int:
    curr: int = 0
    for i, c in enumerate(s):
        if c.isdigit():
            curr = curr * 10 + (ord(c) - 48)
            if curr > LIMIT:
                return LIMIT
            continue
        break
    return curr


class Solution:
    def myAtoi(self, s: str) -> int:
        s = ignore_whitespace(s)
        sign, s = check_signedness(s)
        if sign == 0:
            return 0
        
        s = ignore_leading_zeros(s)
        num: int = convert_to_number(s)
        if sign == 1:
            return (LIMIT - 1) if num >= LIMIT else num
        else:
            return -num

        