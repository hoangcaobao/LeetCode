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
import heapq
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array=[]
        heapq.heapify(array)
        q=queue.Queue()
        q.put(root)
        while q.qsize()>0:
            u=q.get()
            heapq.heappush(array,u.val)
            if u.left:
                q.put(u.left)
            if u.right:
                q.put(u.right)
        
        for i in range(1,k):
            heapq.heappop(array)
        return array[0]
