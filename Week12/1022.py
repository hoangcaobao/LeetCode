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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def convert(number):
            value=0
            for i in range(0,len(number)):
                if int(number[i])==1:
                    value+=2**(len(number)-1-i)
            return value
        
        self.answer=0
        def dfs(root,number):
            if not root:
                return
            if not root.left and not root.right:
                self.answer+=convert(number+str(root.val))
                return
            dfs(root.left,number+str(root.val))
            dfs(root.right,number+str(root.val))
            return
        
        dfs(root,"")
        return self.answer
