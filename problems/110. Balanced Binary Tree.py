# Definition for a binary tree node.
from optparse import Option
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode], balanced: list[bool]) -> int:
            if node is None:
                return 0
            left = check_height(node.left, balanced)
            if not balanced[0]:
                return -1
            right = check_height(node.right, balanced)
            if abs(left - right) > 1:
                balanced[0] = False
            return 1 + max(left, right)

        balanced: list[bool] = [True]

        check_height(root, balanced)
        return balanced[0]
