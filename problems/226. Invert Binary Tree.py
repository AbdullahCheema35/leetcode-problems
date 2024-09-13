from inspect import _void
from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap_children(root)
        return root

    def swap_children(self, head: Optional[TreeNode]) -> None:
        """Swaps the left and right children of a node"""
        if head is None:
            return
        self.swap_children(head.left)
        self.swap_children(head.right)
        temp: Optional[TreeNode] = head.left
        head.left = head.right
        head.right = temp
