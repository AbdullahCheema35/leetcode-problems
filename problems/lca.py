from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
class Solution:
    def __init__(self):
        self.pFound: bool = False
        self.qFound: bool = False

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def findLCA(
            node: Optional[TreeNode], p: TreeNode, q: TreeNode
        ) -> Optional[TreeNode]:
            if not node:
                return None
            if node == p:
                self.pFound = True
                if self.qFound:
                    return None
            if node == q:
                self.qFound = True
                if self.pFound:
                    return None

            left: Optional[TreeNode] = findLCA(node.left, p, q)
            if not left and (self.pFound and self.qFound):
                return node
            right: Optional[TreeNode] = findLCA(node.right, p, q)
            if not right and (self.pFound and self.qFound):
                return node
            elif left or right:
                return left or right
            return None

        return findLCA(root, p, q)

    # def findLCA(
    #     self, node: Optional[TreeNode], p: TreeNode, q: TreeNode
    # ) -> Optional[TreeNode]:
    #     if not node:
    #         return None
    #     if node == p:
    #         pFound = True
    #         return node
    #     if node == q:
    #         qFound = True
    #         return node

    #     left = findLCA(node.left)
    #     right = findLCA(node.right)

    #     if left and right:
    #         return node
    #     return left or right
