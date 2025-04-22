from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []
        answer: List[int] = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > temperatures[stack[-1]]:
                index: int = stack.pop()
                answer[index] = i - index
            stack.append(i)

        return answer