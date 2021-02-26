"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def dfs(node,visited):
    if node in visited:
        return visited[node]
    visited[node]=Node(node.val)
    
    for u in node.neighbors:
        visited[node].neighbors.append(dfs(u,visited))

    return visited[node]
        
        
    
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        
        
        visited = {}
        res = dfs(node,visited)
        return res