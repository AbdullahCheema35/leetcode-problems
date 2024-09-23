class MyQueue:

    def __init__(self):
        self.main = []  # Main array which will be used as a stack
        self.helper = []  # Secondary array to store reverse of stack

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        if len(self.helper) > 0:
            return self.helper.pop()
        while len(self.main) > 0:
            poppedElem = self.main.pop()
            self.helper.append(poppedElem)
        return self.helper.pop()

    def peek(self) -> int:
        if len(self.helper) > 0:
            return self.helper[-1]
        while len(self.main) > 0:
            poppedElem = self.main.pop()
            self.helper.append(poppedElem)
        return self.helper[-1]

    def empty(self) -> bool:
        return len(self.main) == 0 and len(self.helper) == 0
