from typing import Optional, cast


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def findLCA(
            node: Optional["TreeNode"], p: "TreeNode", q: "TreeNode"
        ) -> Optional["TreeNode"]:
            if not node:
                return
            if node.val in (p.val, q.val):
                return node
            left: Optional["TreeNode"] = findLCA(node.left, p, q)
            right: Optional["TreeNode"] = findLCA(node.right, p, q)
            if left and right:
                return node
            return left or right

        return cast(TreeNode, findLCA(root, p, q))
