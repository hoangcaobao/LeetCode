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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        dic={}
        q=queue.Queue()
        q.put(root)
        while q.qsize()>0:
            for i in range(0,q.qsize()):
                u=q.get()
                if k-u.val in dic:
                    return True
                dic[u.val]=0

                if u.left:
                    q.put(u.left)
                if u.right:
                    q.put(u.right)
        return False
