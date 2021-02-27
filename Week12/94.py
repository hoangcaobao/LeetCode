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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.answer=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.answer.append(root.val)
            inorder(root.right)
            return self.answer
        return inorder(root)
