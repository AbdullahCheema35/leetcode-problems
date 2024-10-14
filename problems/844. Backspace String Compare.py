class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def editor_output(string: str) -> list[str]:
            editor: list[str] = list(string)
            pointer: int = 0

            for c in string:
                if c == "#":
                    pointer = max(pointer - 1, 0)
                else:
                    editor[pointer] = c
                    pointer += 1

            return editor[:pointer]

        return editor_output(s) == editor_output(t)
