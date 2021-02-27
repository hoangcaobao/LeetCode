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
    def rightSideView(self, root: TreeNode) -> List[int]:
        q=[]
        if not root:
            return []
        q.append(root)
        self.answer=[]
        while len(q)>0:
            self.answer.append(q[-1].val)
            for i in range(0,len(q)):
                u=q.pop(0)
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
        return self.answer
