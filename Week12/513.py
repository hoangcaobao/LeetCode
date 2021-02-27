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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q=queue.Queue()
        q.put(root)
        array=[[0,0,root.val]]
        rank=0
        while q.qsize()>0:
            rank+=1
            
            for i in range(0,q.qsize()):
                u=q.get()
                if u.left:
                    q.put(u.left)
                if u.right:
                    q.put(u.right)
                if i%2==0:
                    if array[0][1]<rank:
                        array[0]=[i,rank,u.val]
            
        return array[0][2]
