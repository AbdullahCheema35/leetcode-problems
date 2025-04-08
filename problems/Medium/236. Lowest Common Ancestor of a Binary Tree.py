from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        (node, _) = self.find(root, p.val, q.val, 0)
        assert node is not None, "node cannot be None"
        return node
    
    def find(self, node: Optional['TreeNode'], p: int, q: int, found: int) -> Tuple[Optional['TreeNode'], bool]:
        if node is None:
            return None, False
        itself: bool = node.val == p or node.val == q
        found = found + 1 if itself else found
        if itself and found == 2:
            return node, True

        (left, finshed) = self.find(node.left, p, q, found)
        if finshed:
            return (node, True) if itself else (left, True)
        (right, finshed) = self.find(node.right, p, q, found)
        if finshed:
            return (node, True) if itself else (right, True)
        
        finshed = True if ((left and right) or (itself and (left or right))) else False
        
        ret: Optional[TreeNode] = left or right or None

        return (node, finshed) if (itself or (left and right)) else (ret, False)
            

