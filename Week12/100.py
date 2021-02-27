### DO NOT REMOVE THIS
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
### DO NOT REMOVE THIS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.answer=True
        def ck(p,q):
            if not p and not q:
                return
            if not p or not q:
                self.answer=False
                return
            if p.val!=q.val:
                self.answer=False
            
            ck(p.right,q.right)
            ck(p.left,q.left)
        
        ck(p,q)
        
        return self.answer
