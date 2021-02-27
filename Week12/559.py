### DO NOT REMOVE THIS
from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
### DO NOT REMOVE THIS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        array=[0]
        
        def dfs(root,tang,array):
            if not root:
                array[0]=max(tang,array[0])
                return
            if len(root.children)==0:
                array[0]=max(tang+1,array[0])
                return
            for child in root.children:
                dfs(child,tang+1,array)
            
        dfs(root,0,array)
        return array[0]
