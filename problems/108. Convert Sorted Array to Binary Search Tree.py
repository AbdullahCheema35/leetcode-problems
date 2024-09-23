from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert_to_bst(start: int, end: int, nums: List[int]) -> Optional[TreeNode]:
            if start < 0 or start > end:
                return None
            root_index: int = (start + end + 1) // 2
            left_node: Optional[TreeNode] = convert_to_bst(start, root_index - 1, nums)
            right_node: Optional[TreeNode] = convert_to_bst(root_index + 1, end, nums)
            root_node = TreeNode(nums[root_index], left_node, right_node)
            return root_node

        return convert_to_bst(0, len(nums) - 1, nums)
