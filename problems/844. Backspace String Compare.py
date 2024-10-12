from copy import copy, deepcopy


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sEditor: str = ""
        tEditor: str = ""

        for c in s:
            if c == "#":
                sEditor = sEditor[:-1]
            else:
                sEditor += c

        for c in t:
            if c == "#" and len(tEditor) > 0:
                tEditor = tEditor[: len(tEditor) - 1]
            else:
                tEditor += c

        return sEditor == tEditor
