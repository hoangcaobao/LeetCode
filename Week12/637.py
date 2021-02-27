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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q=queue.Queue()
        q.put(root)
        array=[]
        while q.qsize()>0:
            number=0
            size=q.qsize()
            for i in range(0,q.qsize()):
                u=q.get()
                if u.right:
                    q.put(u.right)
                if u.left:
                    q.put(u.left)
                number+=u.val
            array.append(number/size)
        return array
