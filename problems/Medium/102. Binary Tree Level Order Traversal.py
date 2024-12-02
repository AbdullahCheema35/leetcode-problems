# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        outer_list: List[List[int]] = []
        next_level: List[TreeNode] = [root] if root else []

        while next_level:
            current_level = next_level
            next_level = []
            for elem in current_level:
                if isinstance(elem.left, TreeNode):
                    next_level.append(elem.left)
                if isinstance(elem.right, TreeNode):
                    next_level.append(elem.right)
            inner_list: List[int] = [node.val for node in current_level]
            outer_list.append(inner_list)

        return outer_list
