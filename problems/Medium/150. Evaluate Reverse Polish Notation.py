from locale import atoi
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = []
        
        for t in tokens:
            if not self.isOperator(t):
                stack.append(t)
                continue
            op2: str = stack.pop(-1)
            op1: str = stack.pop(-1)
            res: int = self.evalExpression(op1, op2, t) 
            stack.append(str(res))
        
        return atoi(stack[-1])


    def evalExpression(self, op1: str, op2: str, operator: str) -> int:
        o1: int = atoi(op1)
        o2: int = atoi(op2)
        if operator == "+":
            return o1 + o2
        if operator == "-":
            return o1 - o2
        if operator == "*":
            return o1 * o2
        if operator == "/":
            return int(o1 / o2)
        return -1
    
    def isOperator(self, token: str) -> bool:
        return token == "+" or token == "-" or token == "*" or token == "/"