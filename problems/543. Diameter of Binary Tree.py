from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter: int = 0

        def calculate_diameter(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0
            left: int = calculate_diameter(node.left)
            right: int = calculate_diameter(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        calculate_diameter(root)
        return diameter
