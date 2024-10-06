from typing import Optional, cast


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_if_subtree(
            root: Optional[TreeNode], sub_root: Optional[TreeNode]
        ) -> bool:
            if not root or not sub_root:
                return not root and not sub_root
            return (
                root.val == sub_root.val
                and check_if_subtree(root.left, sub_root.left)
                and check_if_subtree(root.right, sub_root.right)
            )

        def pre_order_traversal(root: Optional[TreeNode], sub_root: TreeNode) -> bool:
            if not root:
                return False
            subtree_found: bool = False
            if root.val == sub_root.val:
                subtree_found = check_if_subtree(
                    root.left, sub_root.left
                ) and check_if_subtree(root.right, sub_root.right)
            return (
                subtree_found
                or pre_order_traversal(root.left, sub_root)
                or pre_order_traversal(root.right, sub_root)
            )

        return pre_order_traversal(root, cast(TreeNode, subRoot))
