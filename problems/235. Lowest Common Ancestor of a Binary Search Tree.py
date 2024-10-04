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
        def find_lca(node: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
            if node.val in (p.val, q.val):
                return node
            if p.val < node.val and q.val < node.val:
                return find_lca(node.left, p, q)
            if p.val > node.val and q.val > node.val:
                return find_lca(node.right, p, q)
            return node

        return find_lca(root, p, q)
