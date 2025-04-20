from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def recursive(node: Optional[TreeNode], k: int, curr: int) -> Tuple[int, int]:
            if node is None:
                return 0, -1
            smaller_nodes, kthVal = recursive(node.left, k, curr)
            if kthVal != -1:
                return 0, kthVal
            if curr + smaller_nodes + 1 == k:
                return 0, node.val
            larger_nodes, kthVal = recursive(node.right, k, curr+smaller_nodes+1)
            if kthVal != -1:
                return 0, kthVal
            return curr+smaller_nodes+larger_nodes+1, -1
        return recursive(root, k, 0)[1]