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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer=1
        def dfs(root):
            if not root:
                return 0
            right=dfs(root.right)
            left=dfs(root.left)
            self.answer=max(self.answer,right+left+1)
            return 1+max(right,left)
        dfs(root)
        return self.answer-1   
