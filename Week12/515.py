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
import queue
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        q=queue.Queue()
        if not root:
            return []
        q.put(root)
        self.answer=[]
        while q.qsize()>0:
            row=-float('inf')
            for i in range(0,q.qsize()):
                u=q.get()
                if u.left:
                    q.put(u.left)
                if u.right:
                    q.put(u.right)
                row=max(u.val,row)
            self.answer.append(row)
        return self.answer
