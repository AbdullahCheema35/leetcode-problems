from typing import List


class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.getMin():
            self.min.append(val)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.min.pop()  # pop min count
        self.stack.pop()  # pop stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
