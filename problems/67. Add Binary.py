class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len: int = len(a)
        b_len: int = len(b)

        if a_len < b_len:
            a = "0" * (b_len - a_len) + a
        else:
            b = "0" * (a_len - b_len) + b

        carry: int = 0
        result: str = ""

        for s in zip(a[::-1], b[::-1]):
            carry += int(s[0]) + int(s[1])
            result = str(carry % 2) + result
            carry = carry // 2

        return (str(carry) if carry else "") + result
