from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recursive(node: Optional[TreeNode], height: int, maxHeight: int, rsView: List[int]) -> int:
            if node is None:
                return maxHeight
            
            if height > maxHeight:
                maxHeight = height
                rsView.append(node.val)
            
            maxHeight = recursive(node.right, height=height+1, maxHeight=maxHeight, rsView=rsView)
            maxHeight = recursive(node.left, height=height+1, maxHeight=maxHeight, rsView=rsView)
            return maxHeight
        
        answer: List[int] = []
        recursive(root, 0, -1, answer)
        return answer
        