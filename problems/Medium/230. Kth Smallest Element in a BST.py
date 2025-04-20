from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer: int = -1
        def recursive(node: Optional[TreeNode], k: int, curr_index: int) -> int:
            if node is None:
                return curr_index
            curr_index = recursive(node.left, k, curr_index)
            curr_index += 1
            if curr_index >= k:
                if curr_index == k:
                    nonlocal answer
                    answer = node.val
                return curr_index
            return recursive(node.right, k, curr_index=curr_index)
        recursive(root, k, 0)
        return answer