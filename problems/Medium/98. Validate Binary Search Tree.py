from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode) -> Tuple[bool, int, int]:
            highest, lowest = node.val, node.val

            if node.left:
                is_valid, curr_highest, curr_lowest = validate(node.left)
                if not is_valid or curr_highest >= node.val:
                    return (False, -1, -1)
                highest = max(highest, curr_highest)
                lowest = min(lowest, curr_lowest)

            if node.right:
                is_valid, curr_highest, curr_lowest = validate(node.right)
                if not is_valid or curr_lowest <= node.val:
                    return (False, -1, -1)
                highest = max(highest, curr_highest)
                lowest = min(lowest, curr_lowest)

            return (True, highest, lowest)

        return validate(root)[0] if root else True
