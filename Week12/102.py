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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.answer=[[]]
        if not root:
            return []
        q=queue.Queue()
        q.put(root)
        while q.qsize()>0:
            self.answer.append([])
            for i in range(0,q.qsize()):
                u=q.get()
                if u.left:
                    q.put(u.left)
                if u.right:
                    q.put(u.right)
                self.answer[-1].append(u.val)
        self.answer.pop(0) 
        return self.answer
