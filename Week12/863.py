### DO NOT REMOVE THIS
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
### DO NOT REMOVE THIS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(root,parent):
            if not root:
                return
            root.parent=parent
            dfs(root.left,root)
            dfs(root.right,root)
        
        dfs(root,None)
        visited={target}
        q=queue.Queue()
        q.put([target,0])
        self.answer=[]
        while q.qsize()>0:
            u=q.get()
            if u[1]==K:
                self.answer.append(u[0].val)
            if u[1]>K:
                continue
            if u[0].right and u[0].right not in visited:
                q.put([u[0].right,u[1]+1])
                visited.add(u[0].right)
            if u[0].left and u[0].left not in visited:
                q.put([u[0].left,u[1]+1])
                visited.add(u[0].left)
            if u[0].parent and u[0].parent not in visited:
                q.put([u[0].parent,u[1]+1])
                visited.add(u[0].parent)
        return self.answer
