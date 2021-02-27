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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        array1=[]
        array2=[]
        def dfs(root,array):
            if not root:
                return
            if not root.right and not root.left:
                array.append(root.val)
                return
            dfs(root.right,array)
            dfs(root.left,array)
            return
        dfs(root1,array1)
        dfs(root2,array2)
        return array1==array2
