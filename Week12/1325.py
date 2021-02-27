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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(root,target):
            if not root:
                return
            root.left=dfs(root.left,target)
            root.right=dfs(root.right,target)
            if root.val==target and not root.right and not root.left:
                return None
            return root
        return dfs(root,target)
