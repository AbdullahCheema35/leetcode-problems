# Definition for a binary tree node.
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

hash_map: Dict[int, int] = {}

def recursion(preorder: List[int], inorder: List[int], p_index: int, start: int, end: int) -> Optional[TreeNode]:
    if start>end:
        return None
    node = TreeNode(val=preorder[p_index])    
    index: int =  hash_map[preorder[p_index]]
    node.left = recursion(preorder=preorder, inorder=inorder, p_index=p_index+1, start=start, end=index-1)
    node.right = recursion(preorder=preorder, inorder=inorder, p_index=p_index+1+(index-start), start=index+1, end=end)
    return node

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, key in enumerate(inorder):
            hash_map[key] = i
        return recursion(preorder=preorder, inorder=inorder, p_index=0, start=0, end=len(inorder)-1)