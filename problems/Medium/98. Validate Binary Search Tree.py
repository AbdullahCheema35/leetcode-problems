from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def validate_left(node: TreeNode) -> Tuple[bool, int]:
        #     highest: int = node.val
        #     if node.left:
        #         is_valid, highest = validate_left(node.left)
        #         if not is_valid or node.val <= highest:
        #             return (False, -1)
        #     if node.right:
        #         is_valid, lowest = validate_right(node.right)
        #         if not is_valid or node.val >= lowest:
        #             return (False, -1)
        #     return (True, max(node.val, highest))

        # def validate_right(node: TreeNode) -> Tuple[bool, int]:
        #     lowest: int = node.val
        #     if node.left:
        #         is_valid, highest = validate_left(node.left)
        #         if not is_valid or node.val <= highest:
        #             return (False, -1)
        #     if node.right:
        #         is_valid, lowest = validate_right(node.right)
        #         if not is_valid or node.val >= lowest:
        #             return (False, -1)
        #     return (True, min(node.val, lowest))

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
