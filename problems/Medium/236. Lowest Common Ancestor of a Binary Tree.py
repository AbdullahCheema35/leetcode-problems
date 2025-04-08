from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = self.find(root, p, q)
        assert node is not None, "node cannot be None"
        return node
    
    def find(self, node: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if node is None or node == p or node == q:
            return node
        
        left = self.find(node.left, p, q)
        right = self.find(node.right, p, q)

        if left and right:
            return node
        
        return left or right
    