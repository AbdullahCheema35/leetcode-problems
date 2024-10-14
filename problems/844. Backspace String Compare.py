class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_editor: list[str] = list(s)
        t_editor: list[str] = list(t)

        s_pointer: int = 0
        t_pointer: int = 0

        for c in s_editor:
            if c == "#":
                s_pointer = max(s_pointer - 1, 0)
            else:
                s_editor[s_pointer] = c
                s_pointer += 1

        for c in t_editor:
            if c == "#":
                t_pointer = max(t_pointer - 1, 0)
            else:
                t_editor[t_pointer] = c
                t_pointer += 1

        return s_editor[:s_pointer] == t_editor[:t_pointer]
