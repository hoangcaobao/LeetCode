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
    def tree2str(self, t: TreeNode) -> str:
        
        def dfs(t):
            if not t:
                return ""
            if not t.left and not t.right:
                return str(t.val)+""
            if not t.right:
                return str(t.val)+"("+dfs(t.left)+")"
            return str(t.val)+"("+dfs(t.left)+")"+"("+dfs(t.right)+")"
        return dfs(t)
